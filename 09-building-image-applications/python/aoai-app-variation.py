from openai import AzureOpenAI
import os
import requests
from PIL import Image
import dotenv
import json

# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
client = AzureOpenAI(
  api_key=os.environ['AZURE_OPENAI_KEY'],  # this is also the default, it can be omitted
  api_version = "2023-12-01-preview",
  azure_endpoint=os.environ['AZURE_OPENAI_ENDPOINT'] 
  )

model = os.environ['AZURE_OPENAI_DEPLOYMENT']

image_dir = os.path.join(os.curdir, 'images')

# Initialize the image path (note the filetype should be png)
image_path = os.path.join(image_dir, 'generated-image.png')
print(image_path)
image = Image.open(image_path)
image.show()

# ---creating variation below---
try:
    print("LOG creating variation")
    result = client.images.create_variation(
        image=open(image_path, "rb"),
        n=1,
        size="1024x1024"
    )

    client.images.create_variation()
    response = json.loads(result.model_dump_json())

    image_path = os.path.join(image_dir, 'generated_variation.png')

    image_url = response['data'][0]['url']

    print("LOG downloading image")
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()
#except openai.error.InvalidRequestError as err:
#    print(err)
    
finally:
    print("completed!")