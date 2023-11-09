import openai
import os
import requests
from PIL import Image
import dotenv

# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
openai.api_key = os.environ['AZURE_OPENAI_KEY']     

# Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
openai.api_version = '2023-06-01-preview'
openai.api_type = 'azure'

image_dir = os.path.join(os.curdir, 'images')

# Initialize the image path (note the filetype should be png)
image_path = os.path.join(image_dir, 'generated-image.png')

# ---creating variation below---
try:
    print("LOG creating variation")
    response = openai.Image.create_variation(
        image=open("generated-image.png", "rb"),
        n=1,
        size="1024x1024"
    )

    image_path = os.path.join(image_dir, 'generated_variation.png')

    image_url = response['data'][0]['url']

    print("LOG downloading image")
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()
except openai.error.InvalidRequestError as err:
    print(err)