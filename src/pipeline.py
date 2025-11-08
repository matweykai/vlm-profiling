import numpy as np
from tqdm import tqdm
from transformers import AutoProcessor

import torch
from torch.utils.data import DataLoader
from torch.profiler import profile, ProfilerActivity, schedule, record_function

from torchmetrics import WordErrorRate
from zeus.monitor import ZeusMonitor
from calflops import calculate_flops


def on_trace_ready(prof, output_path: str):
    prof.export_chrome_trace(output_path)


def test_setup(model: torch.nn.Module, data_loader: DataLoader, processor: AutoProcessor, device: str, trace_path: str):
    with torch.no_grad():
        model.eval()  # Ensure model is in evaluation mode
        model.to(device)

        scheduler_config = schedule(
            skip_first=1,
            wait=1,
            warmup=1,
            active=2,
            repeat=1,
        )

        monitor = ZeusMonitor(gpu_indices=[0])

        # Use CUDA events for more accurate GPU timing
        starter = torch.cuda.Event(enable_timing=True)
        ender = torch.cuda.Event(enable_timing=True)

        latency_list = []  # Store latency for each batch
        energy_list = []
        wer_metric = WordErrorRate()

        if device == 'cuda':
            activities = [
                ProfilerActivity.CPU,
                ProfilerActivity.CUDA,
            ]
        else:
            activities = [
                ProfilerActivity.CPU,
            ]

        with profile(
            activities=activities,
            schedule=scheduler_config,
            record_shapes=True,
            on_trace_ready=lambda p: on_trace_ready(p, trace_path),
        ) as prof:
            
            with torch.no_grad():
                for data_batch in tqdm(data_loader, desc='Processing data'):
                    inputs_batch = {k: v.to(device) for k, v in data_batch['input'].items()}
                    responses_batch = data_batch['response']

                    monitor.begin_window("iteration")
                    starter.record()
                    
                    with record_function('GENERATION_STEP'):
                        pred = model.generate(**inputs_batch, max_new_tokens=70, do_sample=False)
                    torch.cuda.synchronize()
                    
                    ender.record()
                    energy_measurement = monitor.end_window("iteration")

                    # Record time by sample
                    latency_list.append(starter.elapsed_time(ender) / len(responses_batch) / 1000)

                    # Record energy by sample
                    energy_list.append(energy_measurement.gpu_energy[0] / len(responses_batch))

                    decoded_preds = [
                        processor.decode(temp_output[2:], skip_special_tokens=True)
                        for temp_output in pred
                    ]

                    wer_metric.update(decoded_preds, responses_batch)

                    prof.step()

        wer_results = wer_metric.compute()

        avg_latency_ms = float(np.mean(latency_list))
        energy_consumption = float(np.mean(energy_list))
        flops, _, _ = calculate_flops(
            model,
            kwargs=inputs_batch,
            forward_mode='generate',
            include_backPropagation=False,
            print_results=True,
        )

    return {
        'wer_value': wer_results.item(),
        'latency': avg_latency_ms,
        'energy': energy_consumption,
        'flops': flops,
    }