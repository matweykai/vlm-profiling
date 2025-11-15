import torch
from transformers import LlavaForConditionalGeneration, Qwen2_5_VLForConditionalGeneration


def get_model(model_name: str, device: str, optimization: str) -> torch.nn.Module:
    lower_name = model_name.split('/')[-1].lower()

    attention_type = 'flash_attention_2' if optimization == 'flash_attn' else 'eager'

    print('Attention type:', attention_type)

    if lower_name.startswith('llava'):
        model = LlavaForConditionalGeneration.from_pretrained(
            model_name,
            dtype=torch.bfloat16,
            attn_implementation=attention_type,
            low_cpu_mem_usage=True,
            device_map=device,
        )
    elif lower_name.startswith('qwen'):
        model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
            model_name,
            dtype=torch.float16,
            attn_implementation=attention_type,
            low_cpu_mem_usage=True,
            device_map=device,
        )

    if optimization == 'compile':
        model = torch.compile(model, mode="reduce-overhead")
        print('MODEL COMPILED')

    return model


class LLMWrapper(torch.nn.Module):
    def __init__(self, model):
        super().__init__()
        self.model = model

    def forward(self, input):
        return self.model.generate(**input, max_new_tokens=100, do_sample=False)
