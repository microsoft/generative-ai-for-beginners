import os
import base64
import dotenv
from PIL import Image
from openai import AzureOpenAI

dotenv.load_dotenv()

client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # e.g. gpt-image-1.5
IMAGES = os.path.join("09-building-image-applications", "images")
os.makedirs(IMAGES, exist_ok=True)


def save_b64(b64, name):
    path = os.path.join(IMAGES, name)
    with open(path, "wb") as f:
        f.write(base64.b64decode(b64))
    print("saved", path, os.path.getsize(path), "bytes")
    return path


def generate(prompt, name, size="1024x1024"):
    r = client.images.generate(model=deployment, prompt=prompt, size=size, n=1)
    return save_b64(r.data[0].b64_json, name)


# 1) Base image: a sunlit indoor lounge
base_path = generate(
    "A sunlit indoor lounge area with large windows, warm daylight, wooden floor, "
    "potted plants and a cozy modern interior. Open, empty floor space in the "
    "foreground. Photorealistic.",
    "sunlit_lounge.png",
)

# 2) Mask: RGBA, same size. Transparent = area the model is allowed to edit.
#    Make the lower-center foreground transparent (where the pool + flamingo will go).
with Image.open(base_path) as im:
    w, h = im.size
mask = Image.new("RGBA", (w, h), (0, 0, 0, 255))  # fully opaque = keep
px = mask.load()
top = int(h * 0.52)  # start of the editable region
for y in range(top, h):
    for x in range(0, w):
        px[x, y] = (0, 0, 0, 0)  # transparent = edit here
mask_path = os.path.join(IMAGES, "mask.png")
mask.save(mask_path)
print("saved", mask_path, os.path.getsize(mask_path), "bytes")

# 3) Result: actually edit the base image using the mask
try:
    r = client.images.edit(
        model=deployment,
        image=open(base_path, "rb"),
        mask=open(mask_path, "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo",
        size="1024x1024",
        n=1,
    )
    save_b64(r.data[0].b64_json, "sunlit_lounge_result.png")
except Exception as e:  # pylint: disable=broad-except
    print("edit failed, generating result directly:", e)
    generate(
        "A sunlit indoor lounge area with large windows and wooden floor, and a "
        "swimming pool in the foreground containing a pink flamingo. Photorealistic.",
        "sunlit_lounge_result.png",
    )

# 4) Startup illustration for the Edu4All scenario
generate(
    "A friendly flat vector illustration of a small education-technology startup "
    "team building AI-powered learning tools. Diverse people with laptops, books "
    "and lightbulb ideas, colorful, modern, minimal, on a light background.",
    "startup.png",
)

print("done")
