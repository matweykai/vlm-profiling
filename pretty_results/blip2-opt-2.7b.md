## Salesforce/blip2-opt-2.7b

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
    "wer_value": 3.753488302230835,
    "latency": 0.032462475783030194,
    "energy": 7.449036664962769,
    "flops": "751.3 GFLOPS"
}

4:

{
    "wer_value": 3.753488302230835,
    "latency": 0.04363453399658203,
    "energy": 2.9354233344395957,
    "flops": "3.15 TFLOPS"
}

8:
{
    "wer_value": 3.753488302230835,
    "latency": 0.06926369867826764,
    "energy": 2.314842104911804,
    "flops": "3.15 TFLOPS"
}

16:
{
    "wer_value": 3.753488302230835,
    "latency": 0.11120067937750566,
    "energy": 2.6188980257302,
    "flops": "9.46 TFLOPS"
}


2) Image size

224:

COCO:
{
    "wer_value": 0.995278537273407,
    "latency": 0.12150613885176807,
    "energy": 2.484860743869815,
    "flops": "9.08 TFLOPS"
}

ScienceQA:
{
    "wer_value": 20.883333206176758,
    "latency": 0.10358256530761718,
    "energy": 2.618108553321738,
    "flops": "12.8 TFLOPS"
}

TextVQA:
{
    "wer_value": 3.753488302230835,
    "latency": 0.11120067937750566,
    "energy": 2.6188980257302,
    "flops": "9.46 TFLOPS"
}


336:

COCO:
{
    "wer_value": 0.9940195083618164,
    "latency": 0.11608276367187499,
    "energy": 2.518562498845552,
    "flops": "9.08 TFLOPS"
}

ScienceQA:
{
    "wer_value": 20.883333206176758,
    "latency": 0.10039841963115491,
    "energy": 2.8174725880748346,
    "flops": "12.8 TFLOPS"
}


TextVQA:
{
    "wer_value": 3.7511627674102783,
    "latency": 0.08471654490420692,
    "energy": 2.044020832630626,
    "flops": "9.46 TFLOPS"
}


448:

COCO:
{
    "wer_value": 0.9937047362327576,
    "latency": 0.12047969938579356,
    "energy": 2.641231360665539,
    "flops": "9.08 TFLOPS"
}

ScienceQA:
{
    "wer_value": 20.883333206176758,
    "latency": 0.10121610460783308,
    "energy": 2.3807675446334637,
    "flops": "12.8 TFLOPS"
}

TextVQA:
{
    "wer_value": 3.7511627674102783,
    "latency": 0.10587666180259303,
    "energy": 2.212878291544161,
    "flops": "9.46 TFLOPS"
}

3) Input Length (224 image)

200:

COCO:
{
    "wer_value": 0.995278537273407,
    "latency": 0.12150613885176807,
    "energy": 2.484860743869815,
    "flops": "9.08 TFLOPS"
}

ScienceQA:
{
    "wer_value": 20.883333206176758,
    "latency": 0.10358256530761718,
    "energy": 2.618108553321738,
    "flops": "12.8 TFLOPS"
}

TextVQA:
{
    "wer_value": 3.753488302230835,
    "latency": 0.11120067937750566,
    "energy": 2.6188980257302,
    "flops": "9.46 TFLOPS"
}


100:

COCO:
{
    "wer_value": 0.995278537273407,
    "latency": 0.12282569222701224,
    "energy": 2.5732258767412417,
    "flops": "9.08 TFLOPS"
}


ScienceQA:
{
    "wer_value": 20.883333206176758,
    "latency": 0.10323174406352796,
    "energy": 2.432131579047755,
    "flops": "12.8 TFLOPS"
}


TextVQA:
{
    "wer_value": 3.753488302230835,
    "latency": 0.115392872057463,
    "energy": 2.3626743413900075,
    "flops": "9.46 TFLOPS"
}


50:
COCO:
{
    "wer_value": 0.995278537273407,
    "latency": 0.12275400282207287,
    "energy": 2.679577849936067,
    "flops": "9.08 TFLOPS"
}

ScienceQA:
{
    "wer_value": 3.753488302230835,
    "latency": 0.11043517785323291,
    "energy": 2.4434177640237307,
    "flops": "9.46 TFLOPS"
}

TextVQA:
{
    "wer_value": 3.753488302230835,
    "latency": 0.11043517785323291,
    "energy": 2.4434177640237307,
    "flops": "9.46 TFLOPS"
}

4) Optimization

ScienceQA 200 16 CUDA

Eagle
{
    "wer_value": 20.883333206176758,
    "latency": 0.10358256530761718,
    "energy": 2.618108553321738,
    "flops": "12.8 TFLOPS"
}


Compile
{
    "wer_value": 20.883333206176758,
    "latency": 0.10099617064626591,
    "energy": 2.6409868425444554,
    "flops": "12.8 TFLOPS"
}


Flash
Can't be used


5) GPU vs CPU

{
    "wer_value": 3.753488302230835,
    "latency": 0.032462475783030194,
    "energy": 7.449036664962769,
    "flops": "751.3 GFLOPS"
}

{
    "wer_value": 3.753488302230835,
    "latency": 1.1128258199055991,
    "energy": 128.28880000273386,
    "flops": "751.3 GFLOPS"
}

## По слоям
- Достаточно тяжёлые свёртки, которые занимают милисекунды времени
- При увеличении батча нормально скейлится
- Размер изображения фиксированный
