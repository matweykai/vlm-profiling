import torch
from transformers import LlavaForConditionalGeneration


def get_model(model_name: str, device: str, optimization: str) -> torch.nn.Module:
    lower_name = model_name.split('/')[-1].lower()

    attention_type = 'flash_attention_2' if optimization == 'flash_attn' else 'eager'

    if lower_name.startswith('llava'):
        model = LlavaForConditionalGeneration.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            attn_implementation=attention_type,
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
