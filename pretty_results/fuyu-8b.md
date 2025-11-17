# adept/fuyu-8b


[`adept/fuyu-8b`](https://huggingface.co/adept/fuyu-8b) - это VLM, в которой попытались сделать максимально простую, но эффективную архитектуру. Здесь нет отдельного обработчика визуальных токенов. Они объединяются с текстовыми и напрямую подаются в LLM.


## Device Tests

Dataset: TextVQA
BatchSize: 1
ImageSize:  224
SeqLen:  200
Optimization: fp16

| Device | Latency | Energy  | FLOPS   |
|--------|---------|---------|---------|
| GPU    | 0.077   | 16.333  | 806.5 G |
| CPU    | 2.599   | 298.418 | 806.5 G |


## Batch Tests

Dataset: TextVQA
ImgSize: 224
SeqLen:  200
Optimization: fp16
Device: Cuda

| batch_size | Latency (per batch) | Energy (per sample) |
|------------|---------------------|---------------------|
| 1          | 0.078               | 16.3                |
| 4          | 0.129               | 7.8                 |
| 8          | 0.263               | 7.72                |
| 16         | 0.260               | 5.02                |

![Batch Size plot](/plots/fuyu-8b/latency_energy_plot.png)

## Image Size Tests

BatchSize: 16
SeqLen:  200
Optimization: fp16
Device: Cuda

| image_size | COCO | COCO latency | ScienceQA | ScienceQA latency | TextVQA | TextVQA latency |
|------------|------|--------------|-----------|-------------------|---------|-----------------|
| 224        | -    | -            | 31.723    | 0.981             | 6.613   | 0.260           |
| 336        | -    | -            | 31.319    | 1.020             | 6.490   | 0.251           |
| 448        | -    | -            | 30.069    | 1.141             | 6.486   | 0.400           |


## Sequence Length Tests

BatchSize: 16
ImageSize:  224
Optimization: fp16
Device: Cuda

| Sequence Len | COCO | COCO latency | ScienceQA | ScienceQA latency | TextVQA | TextVQA latency |
|--------------|------|--------------|-----------|-------------------|---------|-----------------|
| 200          | -    | -            | 31.723    | 0.981             | 6.613   | 0.260           |
| 100          | -    | -            | 31.723    | 0.987             | 6.613   | 0.252           |
| 50           | -    | -            | 29.899    | 0.970             | 6.613   | 0.256           |


## Optimization Tests

Dataset: ScienceQA
BatchSize: 16
ImageSize:  224
SeqLen:  200
Device: Cuda

| Optimization      | Latency | % of original Latency | FLOPS  | % of original FLOPS | Energy | % of original Energy |
|-------------------|---------|-----------------------|--------|---------------------|--------|----------------------|
| fp16              | 0.981   | 100                   | 12.9 T | 100                 | 20.432 | 100                  |
| Compile           | 0.972   | 99                    | 12.7 T | 98                  | 20.325 | 99.4                 |
| Flash Attention 2 | -       | -                     | -      | -                   | -      | -                    |
