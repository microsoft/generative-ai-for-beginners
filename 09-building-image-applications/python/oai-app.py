from openai import OpenAI, OpenAIError
import os
import requests
from requests.exceptions import RequestException
from PIL import Image
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# SECURITY: Validate API key is present
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is required. Please set it in your .env file.")

client = OpenAI(api_key=api_key)


try:
    # Create an image by using the image generation API
    generation_response = client.images.generate(
        model="dall-e-3",
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=1
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    print(generation_response)

    image_url = generation_response.data[0].url  # extract image URL from response

    # SECURITY: Add timeout and error handling for HTTP request
    try:
        response = requests.get(image_url, timeout=30)
        response.raise_for_status()  # Raise exception for HTTP errors
        generated_image = response.content
    except RequestException as req_err:
        print(f"Failed to download generated image: {req_err}")
        raise

    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# SECURITY: Catch specific OpenAI exceptions
except OpenAIError as err:
    print(f"OpenAI API error: {err}")

# ---creating variation below---


response = client.images.create_variation(
  image=open(image_path, "rb"),
  n=1,
  size="1024x1024"
)