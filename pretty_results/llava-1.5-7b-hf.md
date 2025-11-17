## llava-hf/llava-1.5-7b-hf

Базовый конфиг:
Speed:
- device - **cuda**
- optimization - **fp16**

Quality (3 datasets):
- img_size - **224**
- batch_size - **1**
- max_input_len - **200**




1) batch_size: 1, 4, 8, 16

1:

{
    "wer_value": 8.134883880615234,
    "latency": 0.34951892890930175,
    "energy": 93.81820333957673,
    "flops": "11.03 TFLOPS"
}

4:

{
    "wer_value": 8.181395530700684,
    "latency": 0.6605584716796875,
    "energy": 60.31847666581472,
    "flops": "44.13 TFLOPS"
}

8:
{
    "wer_value": 8.153488159179688,
    "latency": 0.9708955720600329,
    "energy": 52.949095393482004,
    "flops": "88.26 TFLOPS"
}

16:
{
    "wer_value": 8.181395530700684,
    "latency": 1.6246062718441612,
    "energy": 49.785277411080244,
    "flops": "132.39 TFLOPS"
}


2) Input Length

200:

COCO:
{
    "wer_value": 3.3509600162506104,
    "latency": 1.8351214214124176,
    "energy": 54.43341228209044,
    "flops": "132.39 TFLOPS"
}

ScienceQA:
{
    "wer_value": 10.293333053588867,
    "latency": 1.7954043161492603,
    "energy": 53.02778070171674,
    "flops": "132.39 TFLOPS"
}

TextVQA:
{
    "wer_value": 8.181395530700684,
    "latency": 1.6246062718441612,
    "energy": 49.785277411080244,
    "flops": "132.39 TFLOPS"
}


100:

COCO:
{
    "wer_value": 3.348756790161133,
    "latency": 1.5829825824938324,
    "energy": 44.44379166552895,
    "flops": "102.51 TFLOPS"
}

ScienceQA:
{
    "wer_value": 11.743332862854004,
    "latency": 1.6632482717413652,
    "energy": 47.85400328876679,
    "flops": "114.28 TFLOPS"
}


TextVQA:
{
    "wer_value": 8.134883880615234,
    "latency": 1.4299011391087582,
    "energy": 41.51552631562216,
    "flops": "104.31 TFLOPS"
}

50:
COCO:
{
    "wer_value": 3.348756790161133,
    "latency": 1.5691488229851975,
    "energy": 44.43349122635105,
    "flops": "102.51 TFLOPS"
}

ScienceQA:
{
    "wer_value": 20.299999237060547,
    "latency": 1.6030098234477796,
    "energy": 45.623339912347625,
    "flops": "107.9 TFLOPS"
}

TextVQA:
{
    "wer_value": 8.134883880615234,
    "latency": 1.4329336226613898,
    "energy": 41.171735747864375,
    "flops": "104.31 TFLOPS"
}

3) Optimization

ScienceQA 200 16 CUDA

Eagle
{
    "wer_value": 10.293333053588867,
    "latency": 1.7954043161492603,
    "energy": 53.02778070171674,
    "flops": "132.39 TFLOPS"
}

Compile
{
    "wer_value": 10.220000267028809,
    "latency": 1.6683042763157894,
    "energy": 48.43908004436577,
    "flops": "114.28 TFLOPS"
}

Flash
{
    "wer_value": 10.34666633605957,
    "latency": 2.1963042763157894,
    "energy": 63.129849782115535,
    "flops": "111.01 TFLOPS"
}

4) GPU vs CPU

{
    "wer_value": 8.134883880615234,
    "latency": 0.34951892890930175,
    "energy": 93.81820333957673,
    "flops": "11.03 TFLOPS"
}

{
    "wer_value": 8.195348739624023,
    "latency": 8.373709375813803,
    "energy": 961.2696200005213,
    "flops": "8.58 TFLOPS"
}

## По слоям
- Достаточно тяжёлые свёртки, которые занимают милисекунды времени
- При увеличении батча нормально скейлится
- Размер изображения фиксированный
