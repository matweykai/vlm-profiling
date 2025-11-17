# llava-hf/llava-1.5-7b-hf

[`llava-hf/llava-1.5-7b-hf`](https://huggingface.co/llava-hf/llava-1.5-7b-hf) - это VLM основанная на модели LLaMA, в которой добавили визуальный проектор. Имеет фиксированный размер изображения, поэтому тестирование по размеру изображений не проводилось.

## Device Tests

Dataset: TextVQA
BatchSize: 1
ImageSize:  224
SeqLen:  200
Optimization: fp16

| Device | Latency | Energy  | FLOPS   |
|--------|---------|---------|---------|
| GPU    | 0.349   | 93.818  | 11.03 T |
| CPU    | 8.373   | 961.269 | 8.58 T  |


## Batch Tests

Dataset: TextVQA
ImgSize: 224
SeqLen:  200
Optimization: fp16
Device: Cuda

| batch_size | Latency (per batch) | Energy (per sample) |
|------------|---------------------|---------------------|
| 1          | 0.349               | 94                  |
| 4          | 0.660               | 60                  |
| 8          | 0.971               | 53                  |
| 16         | 1.624               | 50                  |


## Sequence Length Tests

BatchSize: 16
ImageSize:  224
Optimization: fp16
Device: Cuda

| Sequence Len | COCO  | COCO latency | ScienceQA | ScienceQA latency | TextVQA | TextVQA latency |
|--------------|-------|--------------|-----------|-------------------|---------|-----------------|
| 200          | 3.351 | 1.835        | 10.293    | 1.795             | 8.181   | 1.624           |
| 100          | 3.348 | 1.582        | 11.743    | 1.663             | 8.134   | 1.429           |
| 50           | 3.348 | 1.569        | 20.299    | 1.603             | 8.134   | 1.432           |


## Optimization Tests

Dataset: ScienceQA
BatchSize: 16
ImageSize:  224
SeqLen:  200
Device: Cuda

| Optimization      | Latency | % of original Latency | FLOPS    | % of original FLOPS | Energy | % of original Energy |
|-------------------|---------|-----------------------|----------|---------------------|--------|----------------------|
| fp16              | 1.795   | 100                   | 132.39 T | 100                 | 53.027 | 100                  |
| Compile           | 1.668   | 92.9                  | 114.28 T | 86                  | 48.439 | 91.3                 |
| Flash Attention 2 | 2.196   | 122.3                 | 111.01 T | 83.8                | 63.129 | 119                  |
