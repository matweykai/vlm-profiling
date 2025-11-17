# VLM Profiling

Данный проект выполняется в рамках курса ИТМО "Efficient Deep Learning Models". Целью является изучение возможностей масштабирования современных VLM по различным направлениям (размер изображения, размер запроса, оптимизация).

## Описание железа
Все тесты выполнялись в данной конфигурации:
- CPU - Intel(R) Xeon(R) Platinum 8462Y+ (32 ядра, 2 потока)
- GPU - H100
- CUDA - 12.2
- Nvidia Driver - 535.161.08

## Установка зависимостей
1. Желательно использовать `python3.12`, тк на этой версии писался репозиторий
1. Сначала надо установить зависимости из requirements.txt: `python3.12 -m pip install -r requirements.txt`
1. Далее необходимо скачать flash-attn `python3.12 -m pip install flash-attn==2.8.3 --no-build-isolation`

## Запуск эксперимента
```
python main.py --src_folder datasets/TextVQA \
--model_name llava-hf/llava-1.5-7b-hf \
--img_size 224 \
--batch_size 1 \
--optimization fp16 \
--device cuda \
--max_input_len 200 \
--cached
```

## Описание экспериментов

Результаты экспериментов находятся в директории [`pretty_results`](pretty_results).

### Данные

Данные находятся в директории [`datasets`](datasets):

- `COCO_cap` - сэмпл из 300 примеров датасета [COCO Caption](https://www.kaggle.com/datasets/nikhil7280/coco-image-caption). Входной промпт тут один, отличаются только изображения и ожидаемый ответ.

- `ScienceQA` - сэмпл из 300 примеров датасета [ScienceQA](https://scienceqa.github.io). Вопросы на научную тематику. Датасет вариативен как по промптам, так и по изображениям.

- `TextVQA` - сэмпл из 300 примеров датасета [TextVQA](https://textvqa.org). Вопросы по тексту, изображённому на картинках. Датасет вариативен как по промптам, так и по изображениям.


### Метрики

- Latency - время обработки одного сэмпла данных (иногда это 1 пример, а иногда батч)
- Energy - энергия потраченная на один пример данных (т.е если был батч данных, то общая энергия разделится на размер батча). Измеряется в джоулях.
- FLOPS - кол-во операций, которое тратится на инференс модели с батчом данных (в результатах экспов фиксировались значения только для батча размером 1)
- Качество - качество измерялось по метрике WER с оригинальным ответом, который был в датасете

### Модели
В рамках данного проекта рассматриваются данные модели:
- [`blip2-flan-t5-xl`](pretty_results/blip2-flan-t5-xl.md)
- [`blip2-opt-2.7b`](pretty_results/blip2-opt-2.7b.md)
- [`fuyu-8b`](pretty_results/fuyu-8b.md)
- [`llava-1.5-7b-hf`](pretty_results/llava-1.5-7b-hf.md)
- [`Qwen2.5-VL-3B-Instruct`](pretty_results/Qwen2.5-VL-3B-Instruct.md)