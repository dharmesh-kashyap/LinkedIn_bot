# grok_integration/grok_image_generator.py

import requests
from config.config import XAI_API_KEY
from utils.helpers import download_image

def generate_image(prompt, output_path):
    url = "https://api.x.ai/v1/images/generate"
    headers = {
        "Authorization": f"Bearer {XAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024"
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        image_url = response.json()['data'][0]['url']
        download_image(image_url, output_path)
    else:
        raise Exception(f"Image generation failed: {response.text}")
