# Salesforce/instructblip-flan-t5-xl

[`InstructBLIP`](https://huggingface.co/Salesforce/instructblip-flan-t5-xl) — это доработанная версия модели BLIP-2, настроенная с помощью инструкций (instruction tuning) для решения различных задач, связывающих зрение и язык. Как и BLIP-2, её архитектура состоит из трех основных компонентов:

- Визуальный кодировщик: Модуль, похожий на CLIP, который преобразует входное изображение в набор визуальных эмбеддингов.
- Q-Former (Querying Transformer): BERT-подобный проектор, который выступает в роли моста между визуальным кодировщиком и языковой моделью
- LLM: в данной конкретной модели в качестве языковой модели используется Flan-T5-xl. Веса визуального кодировщика и языковой модели заморожены, а обучение происходит только в Q-Former, что позволяет эффективно связывать две модальности.


## Device Tests

Dataset: TextVQA
BatchSize: 1
ImageSize:  224
SeqLen:  200
Optimization: fp16

| Device | Latency | Energy   | FLOPS   |
|--------|---------|----------|---------|
| GPU    | 0.299   | 43.441   | 801.5 G |
| CPU    | 2.231   | 412.123  | 801.5 G |


## Batch Tests

Dataset: TextVQA
ImgSize: 224
SeqLen:  200
Optimization: fp16
Device: Cuda

| batch_size | Latency (per batch) | Energy (per sample) |
|------------|---------------------|---------------------|
| 1          | 0.299               | 43                  |
| 4          | 0.595               | 22                  |
| 8          | 0.744               | 14                  |
| 16         | 0.922               | 10                  |

![Batch Size plot](/plots/blip2-flan-t5-xl/latency_energy_plot.png)


## Image Size Tests

BatchSize: 16
SeqLen:  200
Optimization: fp16
Device: Cuda

| image_size | COCO  | COCO latency | ScienceQA | ScienceQA latency | TextVQA | TextVQA latency |
|------------|-------|--------------|-----------|-------------------|---------|-----------------|
| 224        | 0.881 | 0.498        | 9.213     | 1.100             | 2.918   | 0.922           |
| 336        | 0.874 | 0.475        | 9.746     | 1.089             | 2.746   | 1.014           |
| 448        | 0.874 | 0.460        | 9.359     | 1.082             | 2.755   | 0.990           |


![Image Size plot](/plots/blip2-flan-t5-xl/latency_img_size_plot.png)


## Sequence Length Tests

BatchSize: 16
ImageSize:  224
Optimization: fp16
Device: Cuda

| Sequence Len | COCO  | COCO latency | ScienceQA | ScienceQA latency | TextVQA | TextVQA latency |
|--------------|-------|--------------|-----------|-------------------|---------|-----------------|
| 200          | 0.881 | 0.498        | 9.213     | 1.100             | 2.918   | 0.922           |
| 100          | 0.881 | 0.493        | 9.213     | 1.099             | 2.918   | 0.919           |
| 50           | 0.881 | 0.491        | 8.193     | 1.123             | 2.918   | 0.927           |

![Sequence length plot](/plots/blip2-flan-t5-xl/latency_seq_plot.png)


## Optimization Tests

Dataset: ScienceQA
BatchSize: 16
ImageSize:  224
SeqLen:  200
Device: Cuda

| Optimization      | Latency | % of original Latency | FLOPS   | % of original FLOPS | Energy | % of original Energy |
|-------------------|---------|-----------------------|---------|---------------------|--------|----------------------|
| fp16              | 1.100   | 100                   | 10.21 T | 100                 | 11.631 | 100                  |
| Compile           | 1.098   | 99.8                  | 10.21 T | 100                 | 11.645 | 100.1                |
| Flash Attention 2 | -       | -                     | -       | -                   | -      | -                    |
