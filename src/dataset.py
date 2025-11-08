import json
from pathlib import Path

from PIL import Image
from transformers import AutoProcessor, AutoTokenizer
from torch.utils.data import Dataset


class ValidationDataset(Dataset):
    def __init__(
        self,
        src_folder: str,
        img_size: int,
        max_input_len: int,
        model_name: str,
        json_name: str = 'samples.json',
        cached: bool = True,
    ) -> None:
        super().__init__()
        self._src_folder = Path(src_folder)
        self._cached = cached
        self._img_size = img_size
        self._processor = AutoProcessor.from_pretrained(model_name)
        self._tokenizer = AutoTokenizer.from_pretrained(model_name)
        self._max_input_len = max_input_len

        self._labels = self._prepare_labels_from_json(self._src_folder / json_name)

    def _preprocess_sample(self, data_sample: dict) -> dict:
        img = Image.open(data_sample['image_path'])
        img.thumbnail((self._img_size, self._img_size))

        conversation = [
            {
                'role': 'user',
                'content': [
                    {'type': 'text', 'text': data_sample['request']},
                    {'type': 'image'},
                ]
            }
        ]

        prompt = self._processor.apply_chat_template(conversation, add_generation_prompt=True)

        tokenized_prompt = self._tokenizer(
            prompt,
            truncation=True,
            max_length=self._max_input_len,
        )

        truncated_prompt = self._tokenizer.decode(tokenized_prompt['input_ids'])

        # Process image and text, with truncation
        inputs = self._processor(
            images=img,
            text=truncated_prompt,
            return_tensors='pt',
            padding=True,
        )

        inputs = {k: v.squeeze(0) for k, v in inputs.items()}

        return {
            'input': inputs,
            'response': data_sample['response'],
        }

    def _prepare_labels_from_json(self, json_path: Path) -> list[dict]:
        with open(json_path, 'r') as file:
            raw_json = json.load(file)
        
        if self._cached:
            raw_json = [self._preprocess_sample(temp_sample) for temp_sample in raw_json]

        return raw_json
    
    def __getitem__(self, index) -> dict:
        temp_sample = self._labels[index]

        if not self._cached:
            temp_sample = self._preprocess_sample(temp_sample)

        return temp_sample
    
    def __len__(self) -> int:
        return len(self._labels)
