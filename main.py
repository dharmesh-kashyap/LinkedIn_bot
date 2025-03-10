# main.py

from grok_integration.grok_text_generator import generate_text
from grok_integration.grok_image_generator import generate_image
from linkedin_api.linkedin_poster import register_image_upload, upload_image, create_post

def main():
    # Define the prompt for text generation
    text_prompt = "Share insights on the latest trends in artificial intelligence."

    # Generate post content using Grok
    post_content = generate_text(text_prompt)
    print(f"Generated Post Content: {post_content}")

    # Define the prompt for image generation
    image_prompt = "A futuristic representation of AI in everyday life"
    image_path = "ai_future_image.jpg"

    # Generate image using Grok
    generate_image(image_prompt, image_path)
    print(f"Image generated and saved to {image_path}")

    # Register image upload on LinkedIn
    upload_info = register_image_upload()
    upload_url = upload_info['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest']['uploadUrl']
    asset = upload_info['value']['asset']
    print("Image upload registered with LinkedIn.")

    # Upload image to LinkedIn
    upload_image(upload_url, image_path)
    print("Image uploaded to LinkedIn.")

    # Create LinkedIn post with the uploaded image
    create_post(asset, post_content)
    print("LinkedIn post created successfully.")

if __name__ == "__main__":
    main()
