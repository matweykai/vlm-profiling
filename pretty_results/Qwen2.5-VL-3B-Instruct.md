# Qwen/Qwen2.5-VL-3B-Instruct

[`Qwen2.5-VL-3B-Instruct`](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct) - это многомодальная модель с 3 миллиардами параметров от Alibaba Cloud, которая способна обрабатывать и понимать изображения, видео и текст. Основные части архитектуры:
- Используется оптимизированный ViT. Часть слоев использует обычнй Attention, а другая часть — Window Attention для повышения эффективности вычислений и скорости обработки
- В качестве декодера используется языковая модель Qwen2.5

## Device Tests

Dataset: TextVQA
BatchSize: 1
ImageSize:  224
SeqLen:  200
Optimization: fp16

| Device | Latency | Energy  | FLOPS    |
|--------|---------|---------|----------|
| GPU    | 0.840   | 129.212 | 617.84 G |
| CPU    | 4.561   | 523.995 | 617.84 G |

## Batch Tests

Dataset: TextVQA
ImgSize: 224
SeqLen:  200
Optimization: fp16
Device: Cuda

| batch_size | Latency (per batch) | Energy (per sample) |
|------------|---------------------|---------------------|
| 1          | 0.840               | 129                 |
| 4          | 1.239               | 48                  |
| 8          | 1.352               | 28                  |
| 16         | 1.431               | 16                  |


## Image Size Tests

BatchSize: 16
SeqLen:  200
Optimization: fp16
Device: Cuda


| image_size | COCO  | COCO latency | ScienceQA | ScienceQA latency | TextVQA | TextVQA latency |
|------------|-------|--------------|-----------|-------------------|---------|-----------------|
| 224        | 1.996 | 1.417        | 31.899    | 1.398             | 11.116  | 1.431           |
| 336        | 1.786 | 1.571        | 31.716    | 1.501             | 11.058  | 1.563           |
| 448        | 1.725 | 1.773        | 30.753    | 1.624             | 10.958  | 1.799           |


## Sequence Length Tests

BatchSize: 16
ImageSize:  224
Optimization: fp16
Device: Cuda

| Sequence Len | COCO  | COCO latency | ScienceQA | ScienceQA latency | TextVQA | TextVQA latency |
|--------------|-------|--------------|-----------|-------------------|---------|-----------------|
| 200          | 1.996 | 1.417        | 31.899    | 1.398             | 11.116  | 1.431           |
| 100          | 1.996 | 1.431        | 31.729    | 1.399             | 11.116  | 1.416           |
| 50           | 1.996 | 1.413        | -         | -                 | 11.116  | 1.427           |

## Optimization Tests

Dataset: ScienceQA
BatchSize: 16
ImageSize:  224
SeqLen:  200
Device: Cuda

| Optimization      | Latency | % of original Latency | FLOPS  | % of original FLOPS | Energy | % of original Energy |
|-------------------|---------|-----------------------|--------|---------------------|--------|----------------------|
| fp16              | 1.398   | 100                   | 96.3 T | 100                 | 15.913 | 100                  |
| Compile           | 1.407   | 100.6                 | 96.3 T | 100                 | 16.079 | 101.4                |
| Flash Attention 2 | 1.939   | 138.7                 | 96.3 T | 100                 | 19.248 | 120.96               |
