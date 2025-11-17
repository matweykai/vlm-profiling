## adept/fuyu-8b

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
    "wer_value": 6.613953590393066,
    "latency": 0.07775924057006835,
    "energy": 16.333873325983685,
    "flops": "806.5 GFLOPS"
}

4:
{
    "wer_value": 6.613953590393066,
    "latency": 0.12908639389038087,
    "energy": 7.782273330688477,
    "flops": null
}


8:
{
    "wer_value": 6.613953590393066,
    "latency": 0.26331992821944394,
    "energy": 7.728924337186311,
    "flops": null
}


16:
{
    "wer_value": 6.613953590393066,
    "latency": 0.26069673718904196,
    "energy": 5.028425438362255,
    "flops": null
}



2) Image size

224:

COCO:


ScienceQA:
{
    "wer_value": 31.72333335876465,
    "latency": 0.9814691740337171,
    "energy": 20.432679825707485,
    "flops": null
}


TextVQA:
{
    "wer_value": 6.613953590393066,
    "latency": 0.26069673718904196,
    "energy": 5.028425438362255,
    "flops": null
}


336:

COCO:
-


ScienceQA:
{
    "wer_value": 31.31999969482422,
    "latency": 1.0209658941971629,
    "energy": 23.07925328978321,
    "flops": null
}


TextVQA:
{
    "wer_value": 6.490697860717773,
    "latency": 0.25138838677657277,
    "energy": 6.498414472529762,
    "flops": null
}



448:

COCO:
-


ScienceQA:
{
    "wer_value": 30.06999969482422,
    "latency": 1.1410340672543176,
    "energy": 27.22943311825133,
    "flops": null
}

TextVQA:
{
    "wer_value": 6.486046314239502,
    "latency": 0.40042524558619447,
    "energy": 11.38761622707049,
    "flops": null
}


3) Input Length (224 image)

200:

COCO:
-

ScienceQA:
{
    "wer_value": 31.72333335876465,
    "latency": 0.9814691740337171,
    "energy": 20.432679825707485,
    "flops": null
}


TextVQA:
{
    "wer_value": 6.613953590393066,
    "latency": 0.26069673718904196,
    "energy": 5.028425438362255,
    "flops": null
}



100:

COCO:
-

ScienceQA:
{
    "wer_value": 31.72333335876465,
    "latency": 0.9878217548571135,
    "energy": 20.349643641396572,
    "flops": null
}

TextVQA:
{
    "wer_value": 6.613953590393066,
    "latency": 0.2522939473202354,
    "energy": 4.96600109652469,
    "flops": null
}


50:
COCO:
-

ScienceQA:
{
    "wer_value": 29.899999618530273,
    "latency": 0.9701102584035772,
    "energy": 20.038834432238026,
    "flops": null
}

TextVQA:
{
    "wer_value": 6.613953590393066,
    "latency": 0.25664792070890724,
    "energy": 4.980753288980116,
    "flops": null
}


4) Optimization

ScienceQA 200 16 CUDA

Eagle
{
    "wer_value": 31.72333335876465,
    "latency": 0.9814691740337171,
    "energy": 20.432679825707485,
    "flops": null
}


Compile
{
    "wer_value": 31.72333335876465,
    "latency": 0.9722850277549341,
    "energy": 20.325286180826655,
    "flops": null
}


Flash
Can't be used


5) GPU vs CPU

GPU
{
    "wer_value": 6.613953590393066,
    "latency": 0.07775924057006835,
    "energy": 16.333873325983685,
    "flops": "806.5 GFLOPS"
}

CPU:
{
    "wer_value": 6.609302520751953,
    "latency": 2.599500489501953,
    "energy": 298.41865000406904,
    "flops": "806.5 GFLOPS"
}



## По слоям
- Достаточно тяжёлые свёртки, которые занимают милисекунды времени
- При увеличении батча нормально скейлится
- Размер изображения фиксированный
