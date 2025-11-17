# Salesforce/blip2-opt-2.7b

[`Salesforce/blip2-opt-2.7b`](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct) - это модель, которая соединяет предобученные модели компьютерного зрения и LLM для решения мультимодальных задач
- Извлечение визуальных и текстовых эмбеддингов - BLIP
- В качестве языковой модели тут OPT-2.7B


## Device Tests

Dataset: TextVQA
BatchSize: 1
ImageSize:  224
SeqLen:  200
Optimization: fp16

| Device | Latency | Energy  | FLOPS   |
|--------|---------|---------|---------|
| GPU    | 0.032   | 7.449   | 751.3 G |
| CPU    | 1.112   | 128.288 | 751.3 G |


## Batch Tests

Dataset: TextVQA
ImgSize: 224
SeqLen:  200
Optimization: fp16
Device: Cuda

| batch_size | Latency (per batch) | Energy (per sample) |
|------------|---------------------|---------------------|
| 1          | 0.032               | 7.4                 |
| 4          | 0.043               | 2.9                 |
| 8          | 0.069               | 2.3                 |
| 16         | 0.111               | 2.6                 |

![Batch Size plot](/plots/blip2-opt-2.7b/latency_energy_plot.png)


## Image Size Tests

BatchSize: 16
SeqLen:  200
Optimization: fp16
Device: Cuda

| image_size | COCO  | COCO latency | ScienceQA | ScienceQA latency | TextVQA | TextVQA latency |
|------------|-------|--------------|-----------|-------------------|---------|-----------------|
| 224        | 0.995 | 0.121        | 20.883    | 0.103             | 3.753   | 0.111           |
| 336        | 0.994 | 0.116        | 20.883    | 0.100             | 3.751   | 0.084           |
| 448        | 0.993 | 0.120        | 20.883    | 0.101             | 3.751   | 0.105           |


## Sequence Length Tests

BatchSize: 16
ImageSize:  224
Optimization: fp16
Device: Cuda

| Sequence Len | COCO  | COCO latency | ScienceQA | ScienceQA latency | TextVQA | TextVQA latency |
|--------------|-------|--------------|-----------|-------------------|---------|-----------------|
| 200          | 0.995 | 0.121        | 20.883    | 0.103             | 3.753   | 0.111           |
| 100          | 0.995 | 0.122        | 20.883    | 0.103             | 3.753   | 0.115           |
| 50           | 0.995 | 0.122        | 3.753     | 0.110             | 3.753   | 0.110           |


## Optimization Tests

Dataset: ScienceQA
BatchSize: 16
ImageSize:  224
SeqLen:  200
Device: Cuda

| Optimization      | Latency | % of original Latency | FLOPS  | % of original FLOPS | Energy | % of original Energy |
|-------------------|---------|-----------------------|--------|---------------------|--------|----------------------|
| fp16              | 0.103   | 100                   | 12.8 T | 100                 | 2.618  | 100                  |
| Compile           | 0.100   | 97                    | 12.8 T | 100                 | 2.640  | 100.8                |
| Flash Attention 2 | -       | -                     | -      | -                   | -      | -                    |
