# linkedin_api/linkedin_poster.py

import requests
from config.config import LINKEDIN_ACCESS_TOKEN

def register_image_upload():
    register_url = 'https://api.linkedin.com/v2/assets?action=registerUpload'
    headers = {
        'Authorization': f'Bearer {LINKEDIN_ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    upload_request_body = {
        "registerUploadRequest": {
            "owner": "urn:li:person:YOUR_PERSON_URN",
            "recipes": ["urn:li:digitalmediaRecipe:feedshare-image"],
            "serviceRelationships": [
                {
                    "relationshipType": "OWNER",
                    "identifier": "urn:li:userGeneratedContent"
                }
            ],
            "supportedUploadMechanism": ["SYNCHRONOUS_UPLOAD"]
        }
    }
    response = requests.post(register_url, headers=headers, json=upload_request_body)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Image upload registration failed: {response.text}")

def upload_image(upload_url, image_path):
    headers = {
        'Authorization': f'Bearer {LINKEDIN_ACCESS_TOKEN}',
        'Content-Type': 'application/octet-stream'
    }
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
    response = requests.post(upload_url, headers=headers, data=image_data)
    if response.status_code != 201:
        raise Exception(f"Image upload failed: {response.text}")

def create_post(asset, text):
    post_url = 'https://api.linkedin.com/v2/ugcPosts'
    headers = {
        'Authorization': f'Bearer {LINKEDIN_ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    post_data = {
        "author": "urn:li:person:YOUR_PERSON_URN",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": text
                },
                "shareMediaCategory": "IMAGE",
                "media": [
                    {
                        "status": "READY",
                        "description": {
                            "text": "Image description here"
                        },
                        "media": asset,
                        "title": {
                            "text": "Image title here"
                        }
                    }
                ]
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    response = requests.post(post_url, headers=headers, json=post_data)
    if response.status_code != 201:
        raise Exception(f"Post creation failed: {response.text}")
