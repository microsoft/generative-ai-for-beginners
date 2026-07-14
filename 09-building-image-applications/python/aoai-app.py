from openai import AzureOpenAI, BadRequestError
import os
from PIL import Image
import dotenv
import json
import base64

# import dotenv
dotenv.load_dotenv()

 

# Assign the API version (check the Microsoft Foundry docs for the current API version required by your model)
client = AzureOpenAI(
  api_key=os.environ['AZURE_OPENAI_API_KEY'],  # this is also the default, it can be omitted
  api_version = "2025-04-01-preview",
  azure_endpoint=os.environ['AZURE_OPENAI_ENDPOINT'] 
  )

model = os.environ['AZURE_OPENAI_DEPLOYMENT']


try:
    # Create an image by using the image generation API

    result = client.images.generate(
        model=model,
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils. It says "hello"',    # Enter your prompt text here
        size='1024x1024',
        n=1
    )

    generation_response = json.loads(result.model_dump_json())
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    # gpt-image models return the image as base64 (b64_json), not a URL
    image_b64 = generation_response["data"][0]["b64_json"]
    generated_image = base64.b64decode(image_b64)
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
#except BadRequestError as err:
#    print(err)

finally:
    print("completed!")