import json
from pathlib import Path
from argparse import ArgumentParser

from torch.utils.data import DataLoader
from transformers import AutoProcessor

from src.pipeline import test_setup
from src.models import get_model
from src.dataset import ValidationDataset


def main(parsed_args):
    device = parsed_args.device
    model = get_model(
        model_name=parsed_args.model_name,
        optimization=parsed_args.optimization,
        device=device,
    )

    if parsed_args.cached:
        print('CACHE IS ON! BE CAREFUL WITH RAM')

    dataset = ValidationDataset(
        src_folder=parsed_args.src_folder,
        img_size=parsed_args.img_size,
        max_input_len=parsed_args.max_input_len,
        model_name=parsed_args.model_name,
        cached=parsed_args.cached,
    )

    data_loader = DataLoader(
        dataset,
        batch_size=parsed_args.batch_size,
        shuffle=False,
        num_workers=4,
        pin_memory=True,
    )

    processor = AutoProcessor.from_pretrained(parsed_args.model_name)

    results_folder = Path(f'results/{parsed_args.model_name.split('/')[1]}_{parsed_args.img_size}_{parsed_args.max_input_len}_{parsed_args.device}_{parsed_args.optimization}_{parsed_args.batch_size}')
    results_folder.mkdir(exist_ok=True)

    trace_name = results_folder / 'trace.json'
    exp_results = test_setup(model, data_loader, processor, device, str(trace_name))

    with open(results_folder / 'results.json', 'w') as file:
        json.dump(exp_results, file, indent=4)


def parse_args():
    parser = ArgumentParser(description='Benchmark models on validation dataset')
    
    parser.add_argument(
        '--src_folder',
        type=str,
        required=True,
        help='Path to the source folder containing validation data'
    )

    parser.add_argument(
        '--model_name',
        type=str,
        required=True,
        help='Name of the model to benchmark (e.g., "microsoft/trocr-base-stage1")'
    )

    parser.add_argument(
        '--img_size',
        type=int,
        required=True,
        help='Image size as height and width (e.g., --img_size 384)'
    )

    parser.add_argument(
        '--batch_size',
        type=int,
        required=True,
        help='Batch size for DataLoader'
    )

    parser.add_argument(
        '--optimization',
        type=str,
        required=True,
        default='fp16',
        help='Specifies optimizations if needed'
    )

    parser.add_argument(
        '--device',
        type=str,
        required=True,
        default='cuda',
        help='Device to run the benchmark on (e.g., "cuda", "cpu", "cuda:0")'
    )
    
    parser.add_argument(
        '--max_input_len',
        type=int,
        required=True,
        help='Maximum input sequence length for the model'
    )
    
    parser.add_argument(
        '--cached',
        default=False,
        action='store_true',
        help='Whether to use cached dataset (default: False)'
    )
    
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(args)
