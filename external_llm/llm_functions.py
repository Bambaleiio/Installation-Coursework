import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from huggingface_hub import login

import os
from dotenv import load_dotenv, dotenv_values

from extra import clean_line

load_dotenv()

# Mistral requires token-access
token = os.getenv('HUGGINGFACE_TOKEN')
login(token=token)

# Quantization config for 8GB VRAM GPU (4-bit quantization)
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
)

tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")

model = AutoModelForCausalLM.from_pretrained(
    "mistralai/Mistral-7B-Instruct-v0.2",
    device_map='auto',
    quantization_config=quantization_config,
    token=token
)

def classify_emotion(text):
    prompt = (
        "Return 'Happy' if text is happy, 'Sad' if text is sad, 'Angry' if text is angry, "
        "'Fearful' if text is fearful, 'Surprised' if text does surprise, and 'Neutral' otherwise."
        f'Text: "{text}"\n\n'
        "Response with one word only.\n"
    )

    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

    outputs = model.generate(**inputs, max_new_tokens=5, temperature=0.0)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    emotion = response.strip().split()[-1]
    return emotion


def generate_synonyms(text):
    prompt = (
        "Provide synonyms for the following text, one per line, with no extra commentary.\n\n"
        f"Text: \"{text}\"\n"
    )

    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

    outputs = model.generate(
        **inputs,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.8
    )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    lines = [line.strip() for line in response.split("\n") if line.strip()]

    synonyms = [clean_line(line) for line in lines]
    return synonyms