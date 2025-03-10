# grok_integration/grok_text_generator.py

import requests
from config.config import XAI_API_KEY

def generate_text(prompt):
    url = "https://api.x.ai/v1/completions"
    headers = {
        "Authorization": f"Bearer {XAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "grok-2-1212",
        "prompt": prompt,
        "max_tokens": 100
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['text'].strip()
    else:
        raise Exception(f"Text generation failed: {response.text}")
