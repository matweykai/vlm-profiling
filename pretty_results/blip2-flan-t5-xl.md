## Salesforce/instructblip-flan-t5-xl

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
    "wer_value": 3.074418544769287,
    "latency": 0.2999109442647298,
    "energy": 43.03970333258311,
    "flops": "665.53 GFLOPS"
}

4:

{
    "wer_value": 3.0232558250427246,
    "latency": 0.5948651920572917,
    "energy": 21.653356668154398,
    "flops": "2.89 TFLOPS"
}

8:
{
    "wer_value": 2.8372092247009277,
    "latency": 0.7443758448550577,
    "energy": 14.418440790552841,
    "flops": "2.89 TFLOPS"
}

16:
{
    "wer_value": 2.918604612350464,
    "latency": 0.9226475870232833,
    "energy": 9.730710526830272,
    "flops": "8.7 TFLOPS"
}


2) Image size

224:

COCO:
{
    "wer_value": 0.881649374961853,
    "latency": 0.498832126015111,
    "energy": 5.6178585515733355,
    "flops": "8.23 TFLOPS"
}

ScienceQA:
{
    "wer_value": 9.213333129882812,
    "latency": 1.1003059563887747,
    "energy": 11.631437502409282,
    "flops": "10.21 TFLOPS"
}

TextVQA:
{
    "wer_value": 2.918604612350464,
    "latency": 0.9226475870232833,
    "energy": 9.730710526830272,
    "flops": "8.7 TFLOPS"
}

336:

COCO:
{
    "wer_value": 0.87409508228302,
    "latency": 0.4754901267603824,
    "energy": 5.512587718273464,
    "flops": "8.33 TFLOPS"
}


ScienceQA:
{
    "wer_value": 9.74666690826416,
    "latency": 1.0891546405993011,
    "energy": 11.68848574527523,
    "flops": "10.21 TFLOPS"
}

TextVQA:
{
    "wer_value": 2.746511697769165,
    "latency": 1.014838154039885,
    "energy": 10.52962390529482,
    "flops": "8.66 TFLOPS"
}


448:

COCO:
{
    "wer_value": 0.8747245669364929,
    "latency": 0.46005186060855263,
    "energy": 5.304921052434988,
    "flops": "8.33 TFLOPS"
}


ScienceQA:
{
    "wer_value": 9.359999656677246,
    "latency": 1.0828500205592106,
    "energy": 11.64839802499403,
    "flops": "10.21 TFLOPS"
}

TextVQA:
{
    "wer_value": 2.7558138370513916,
    "latency": 0.9906420673571135,
    "energy": 10.313134868939718,
    "flops": "8.7 TFLOPS"
}


3) Input Length (224 image)

200:

COCO:
{
    "wer_value": 0.881649374961853,
    "latency": 0.498832126015111,
    "energy": 5.6178585515733355,
    "flops": "8.23 TFLOPS"
}

ScienceQA:
{
    "wer_value": 9.213333129882812,
    "latency": 1.1003059563887747,
    "energy": 11.631437502409282,
    "flops": "10.21 TFLOPS"
}

TextVQA:
{
    "wer_value": 2.918604612350464,
    "latency": 0.9226475870232833,
    "energy": 9.730710526830272,
    "flops": "8.7 TFLOPS"
}


100:

COCO:
{
    "wer_value": 0.881649374961853,
    "latency": 0.4931324125591077,
    "energy": 5.755140350576033,
    "flops": "8.23 TFLOPS"
}

ScienceQA:
{
    "wer_value": 9.213333129882812,
    "latency": 1.0994425627055922,
    "energy": 11.591701757489588,
    "flops": "10.21 TFLOPS"
}

TextVQA:
{
    "wer_value": 2.918604612350464,
    "latency": 0.9193938614694694,
    "energy": 9.608298246274915,
    "flops": "8.7 TFLOPS"
}


50:
COCO:
{
    "wer_value": 0.881649374961853,
    "latency": 0.4915301176372327,
    "energy": 5.63949122658947,
    "flops": "8.23 TFLOPS"
}

ScienceQA:
{
    "wer_value": 8.193333625793457,
    "latency": 1.1235731393914474,
    "energy": 11.780735746287464,
    "flops": "9.82 TFLOPS"
}


TextVQA:
{
    "wer_value": 2.918604612350464,
    "latency": 0.927969631797389,
    "energy": 9.66338267556408,
    "flops": "8.7 TFLOPS"
}

4) Optimization

ScienceQA 200 16 CUDA

Eagle
{
    "wer_value": 9.213333129882812,
    "latency": 1.1003059563887747,
    "energy": 11.631437502409282,
    "flops": "10.21 TFLOPS"
}


Compile
{
    "wer_value": 9.213333129882812,
    "latency": 1.098557193153783,
    "energy": 11.645459431305266,
    "flops": "10.21 TFLOPS"
}


Flash
Can't be used


5) GPU vs CPU

{
    "wer_value": 10.293333053588867,
    "latency": 1.7954043161492603,
    "energy": 53.02778070171674,
    "flops": "132.39 TFLOPS"
}

## По слоям
- Достаточно тяжёлые свёртки, которые занимают милисекунды времени
- При увеличении батча нормально скейлится
- Размер изображения фиксированный
