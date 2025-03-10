# utils/helpers.py

import requests

def download_image(image_url, output_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            file.write(response.content)
    else:
        raise Exception(f"Failed to download image: {response.text}")
