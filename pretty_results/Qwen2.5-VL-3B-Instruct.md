## Qwen/Qwen2.5-VL-3B-Instruct

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
    "wer_value": 28.216279983520508,
    "latency": 0.8404356453959149,
    "energy": 129.9412200021744,
    "flops": "617.84 GFLOPS"
}


4:
{
    "wer_value": 14.334883689880371,
    "latency": 1.2393468701171875,
    "energy": 48.9808399995168,
    "flops": null
}


8:
{
    "wer_value": 12.095349311828613,
    "latency": 1.352854839124178,
    "energy": 27.695713818073273,
    "flops": null
}


16:
{
    "wer_value": 11.116278648376465,
    "latency": 1.4315514108758225,
    "energy": 15.723574563076621,
    "flops": null
}



2) Image size

224:

COCO:
{
    "wer_value": 1.9965375661849976,
    "latency": 1.4177824835526316,
    "energy": 15.396335527562258,
    "flops": null
}

ScienceQA:
{
    "wer_value": 31.899999618530273,
    "latency": 1.3983496479235198,
    "energy": 15.913652410632686,
    "flops": null
}

TextVQA:
{
    "wer_value": 11.116278648376465,
    "latency": 1.4315514108758225,
    "energy": 15.723574563076621,
    "flops": null
}


336:

COCO:
{
    "wer_value": 1.7869058847427368,
    "latency": 1.5717079628392268,
    "energy": 18.879388156690094,
    "flops": null
}

ScienceQA:
{
    "wer_value": 31.71666717529297,
    "latency": 1.5017343107524672,
    "energy": 17.902699559926987,
    "flops": null
}

TextVQA:
{
    "wer_value": 11.05813980102539,
    "latency": 1.5635441766036184,
    "energy": 18.733766448602342,
    "flops": null
}

448:

COCO:
{
    "wer_value": 1.725841999053955,
    "latency": 1.7735813759251642,
    "energy": 23.503548246726655,
    "flops": null
}

ScienceQA:
{
    "wer_value": 30.753334045410156,
    "latency": 1.6246667416221217,
    "energy": 20.7115438580513,
    "flops": null
}


TextVQA:
{
    "wer_value": 10.958139419555664,
    "latency": 1.7995396985505754,
    "energy": 23.961486840457248,
    "flops": null
}



3) Input Length (224 img)

200:

COCO:
{
    "wer_value": 1.9965375661849976,
    "latency": 1.4177824835526316,
    "energy": 15.396335527562258,
    "flops": null
}

ScienceQA:
{
    "wer_value": 31.899999618530273,
    "latency": 1.3983496479235198,
    "energy": 15.913652410632686,
    "flops": null
}

TextVQA:
{
    "wer_value": 11.116278648376465,
    "latency": 1.4315514108758225,
    "energy": 15.723574563076621,
    "flops": null
}

100:

COCO:
{
    "wer_value": 1.9965375661849976,
    "latency": 1.4313184171977797,
    "energy": 15.536371710007652,
    "flops": null
}

ScienceQA:
{
    "wer_value": 31.729999542236328,
    "latency": 1.3994054597553451,
    "energy": 15.681587718557894,
    "flops": null
}


TextVQA:
{
    "wer_value": 11.116278648376465,
    "latency": 1.416980520148026,
    "energy": 15.54091885842775,
    "flops": null
}


50:
COCO:
{
    "wer_value": 1.9965375661849976,
    "latency": 1.4133769659745066,
    "energy": 15.394378289841768,
    "flops": null
}


ScienceQA:
Не хватает токенов


TextVQA:
{
    "wer_value": 11.116278648376465,
    "latency": 1.4275012014288653,
    "energy": 15.54505043751315,
    "flops": null
}


4) Optimization

ScienceQA 200 16 CUDA

Eagle
{
    "wer_value": 31.899999618530273,
    "latency": 1.3983496479235198,
    "energy": 15.913652410632686,
    "flops": null
}

Compile
{
    "wer_value": 31.899999618530273,
    "latency": 1.4077565789473685,
    "energy": 16.07927960523388,
    "flops": null
}


Flash
{
    "wer_value": 56.939998626708984,
    "latency": 1.939170564350329,
    "energy": 19.248597589501163,
    "flops": "12.09 TFLOPS"
}


5) GPU vs CPU

{
    "wer_value": 10.293333053588867,
    "latency": 1.7954043161492603,
    "energy": 53.02778070171674,
    "flops": "132.39 TFLOPS"
}

## По слоям

