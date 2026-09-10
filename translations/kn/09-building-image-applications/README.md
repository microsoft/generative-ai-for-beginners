# ಚಿತ್ರ ರಚನೆ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದು

[![ಚಿತ್ರ ರಚನೆ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದು](../../../translated_images/kn/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM‌ಗಳಿಗಿಂತ ಪಠ್ಯ ರಚನೆ ಮಾತ್ರವಲ್ಲ. ನೀವು ಪಠ್ಯ ವಿವರಣೆಗಳಿಂದ ಚಿತ್ರಗಳನ್ನು ರಚಿಸಬಹುದು. ಚಿತ್ರಗಳು ಒಂದು ಮಾದರಿಯಾಗಿ ಮೆಡ್‌ಟೆಕ್, ವಾಸ್ತುಶಿಲ್ಪ, ಪ್ರವಾಸೋದ್ಯಮ, ಆಟಗಳ ಅಭಿವೃದ್ಧಿ, ಮಾರ್ಕೆಟಿಂಗ್ ಮತ್ತು ಇನ್ನಿತರ ವಲಯಗಳಲ್ಲಿ ಉಪಯುಕ್ತವಾಗಿವೆ. ಈ ಪಾಠದಲ್ಲಿ ನಾವು ಇಂದಿನ **GPT ಚಿತ್ರ** ಮಾದರಿಗಳನ್ನು ನೋಡುತ್ತೇವೆ ಮತ್ತು ಚಿತ್ರ ರಚನೆ ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ನಿರ್ಮಿಸುತ್ತೇವೆ.

## ಪರಿಚಯ

ಚಿತ್ರ ರಚನೆ ಸ್ವಾಭಾವಿಕ ಭಾಷೆಯ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಚಿತ್ರದಲ್ಲಿ ಪರಿವರ್ತಿಸುವುದಾಗಿದೆ. ಈ ಪಾಠದಲ್ಲಿ ನಾವು OpenAI ನ **`gpt-image`** ಮಾದರಿಗಳ ಕುಟುಂಬದೊಂದಿಗೆ ಕೆಲಸ ಮಾಡುತ್ತೇವೆ - ಇದು **[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)** ಮತ್ತು OpenAI ವೇದಿಕೆಯಲ್ಲಿ ಲಭ್ಯವಿರುವ ಪ್ರಸ್ತುತ ಚಿತ್ರ ಮಾದರಿಗಳ ತಲೆಮಾರಾಗಿದೆ. ಈ ಮಾದರಿಗಳು ಹಳೆಯ DALL·E ಮಾದರಿಗಳನ್ನು (DALL·E 2/3 ಹಳೆಯದು) ಬದಲಾಯಿಸುತ್ತವೆ.

ಪಾಠದ ಅವಧಿಯಲ್ಲಿ ನಾವು ಕಲ್ಪನೆಗೆ ಸ್ಟಾರ್ಟ್‌ಅಪ್, **Edu4All**, ಇನ್ನು ತಿಳಿಯುತ್ತೇವೆ, ಇದು ಕಲಿಕಾ ಸಾಧನಗಳನ್ನು ನಿರ್ಮಿಸುತ್ತದೆ. ತಂಡವು ಕಾರ್ಯಗಳ ಪರಿಣಾಮಚಿತ್ರಗಳು ಮತ್ತು ಅಧ್ಯಯನ ಸಾಮಗ್ರಿಗಳಿಗೆ ಚಿತ್ರಗಳನ್ನು ರಚಿಸಲು ಬಯಸುತ್ತದೆ.

## ಕಲಿಕೆಯ ಗುರಿಗಳು

ಈ ಪಾಠದ ಅಂತ್ಯಕ್ಕೆ ನೀವು ಇದನ್ನು ಮಾಡಬಹುದು:

- ಚಿತ್ರ ರಚನೆ ಯಿ ಏನೆಂದು ತಿಳಿದುಕೊಳ್ಳುವುದು ಮತ್ತು ಅದು ಎಲ್ಲಿ ಉಪಯುಕ್ತವಾಗಿದೆ ಎಂದು ವಿವರಿಸುವುದು.
- `gpt-image` ಮಾದರಿ ಕುಟುಂಬವನ್ನು ಮತ್ತು ಅದು ಹಳೆಯ DALL·E ಮಾದರಿಗಳಿಂದ ಹೇಗಾಗಿರುತ್ತದೆ ಎಂಬುದನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು.
- ಪೈಥಾನ್ (ಮತ್ತು ಟೈಪ್ಸ್ಕ್ರಿಪ್ಟ್ / .NET) ನಲ್ಲಿ ಚಿತ್ರ ರಚನೆ ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ನಿರ್ಮಿಸುವುದು.
- ಚಿತ್ರಗಳನ್ನು ಸಂಪಾದಿಸಿ ಮತ್ತು ಸುರಕ್ಷತಾ ಗಾರ್ಡ್‌ರೇಲ್ಗಳನ್ನು ಮೆಟಾಪ್ರಾಂಪ್ಟ್ಗಳೊಂದಿಗೆ ಅನ್ವಯಿಸುವುದು.

## ಚಿತ್ರ ರಚನೆ ಎಂದರೇನು?

ಚಿತ್ರ ರಚನೆ ಮಾದರಿಗಳು ಪಠ್ಯ ಪ್ರಾಂಪ್ಟ್‌ನಿಂದ ಚಿತ್ರಗಳನ್ನು ರಚಿಸುತ್ತವೆ. `gpt-image`ಂಥ ಆಧುನಿಕ ಮಾದರಿಗಳು ಟ್ರಾನ್ಸ್‌ಫಾರ್ಮರ್ + ಡಿಫ್ಯೂಷನ್ ತಂತ್ರಜ್ಞಾನಗಳ ಮೇಲೆ ನಿರ್ಮಿತವಾಗಿವೆ: ಮಾದರಿ ತರಬೇತಿ ಸಮಯದಲ್ಲಿ ಪಠ್ಯ ಮತ್ತು ಚಿತ್ರಗಳ ನಡುವಿನ ಸಂಬಂಧವನ್ನು ಕಲಿಯುತ್ತದೆ, ನಂತರ ಪ್ರಾಂಪ್ಟ್ ನೀಡಿದಾಗ, "ಡುಷಿತ"ವಾಗಿರುವ ಕದ್ಯಮ ಶಬ್ದವನ್ನು ದೊರಸುವ ಮೂಲಕ ವಿವರಣೆಗೆ ಹೊಂದುವ ಚಿತ್ರವನ್ನು ಕ್ರಮೇಣ ರಚಿಸುತ್ತದೆ.

ಎರಡು ಪ್ರಸಿದ್ಧ ಚಿತ್ರ ಮಾದರಿ ಕುಟುಂಬಗಳು:

- **`gpt-image` (OpenAI)** - ಇಂದಿನ ತಲೆಮಾರಿನ ಮಾದರಿ, ಈ ಪಾಠದಲ್ಲಿ ಉಪಯೋಗವಾಗಿದೆ. ಇದು ಪಠ್ಯದಿಂದ ಚಿತ್ರ ನಿರ್ಮಾಣ ಮತ್ತು ಚಿತ್ರ ಸಂಪಾದನೆ (ಮಾಸ್ಕ್ ಜೊತೆಗೆ ಇನಪೇಯಿಂಟಿಂಗ್) ಬೆಂಬಲಿಸುತ್ತದೆ.
- **ಮಿಡ್‌ಜಾರ್ನಿ** - ತನ್ನ ಸ್ವಂತ ಸೇವೆ ಮತ್ತು Discord ಆಧಾರಿತ ಕಾರ್ಯಚಟುವಟಿಕೆಳ್ಳಿರುವ ಜನಪ್ರಿಯ ಮೂರನೇ ಪಕ್ಷ ಮಾದರಿ.

> ಹಳೆಯ OpenAI ಚಿತ್ರ ಮಾದರಿಗಳು - **DALL·E 2** ಮತ್ತು **DALL·E 3** - ಹಳೆಯದು. DALL·E 3 ಹೊಸ ನಿಯೋಜನೆಗಳಿಗಾಗಿ ಲಭ್ಯವಿಲ್ಲ, ಮತ್ತು `create_variation` ಫೀಚರ್ ಡಿಎಲ್·ಇ 2ರಲ್ಲಿ ಮಾತ್ರ ಇತ್ತು. ಹೊಸ ಅಪ್ಲಿಕೇಶನ್ಗಳಿಗೆ `gpt-image` ಮಾದರಿಗಳನ್ನು ಬಳಸಿ.

### ಯಾವ `gpt-image` ಮಾದರಿಯನ್ನು ಬಳಸದರಿ?

Microsoft Foundry ನಲ್ಲಿ ಕೆಳಕಂಡವು **ಸಾಮಾನ್ಯವಾಗಿ ಲಭ್ಯವಿರುತ್ತವೆ**:

| ಮಾದರಿ | ಟಿಪ್ಪಣಿಗಳು |
| --- | --- |
| **`gpt-image-2`** | ಇತ್ತೀಚಿನ ಮತ್ತು ಶ್ರೇಷ್ಠ ಸಾಮರ್ಥ್ಯದ ಚಿತ್ರ ಮಾದರಿ - ಶಿಫಾರಸು ಮಾಡಿದ ಡಿಫಾಲ್ಟ್. |
| `gpt-image-1.5` | ಸಾಮಾನ್ಯ ಲಭ್ಯತೆ; ಕಡಿಮೆ ವೆಚ್ಚದಲ್ಲಿ ಉತ್ತಮ ಗುಣಮಟ್ಟ. |
| `gpt-image-1-mini` | ಸಾಮಾನ್ಯ ಲಭ್ಯತೆ; ವೇಗವಾಗಿ ಮತ್ತು ಕಡಿಮೆ ವೆಚ್ಚ. |
| `gpt-image-1` | ಪೂರ್ವಕಟ್ಟು ಪ್ರದರ್ಶನ ಮಾತ್ರ. |

ಸದ್ಯದ [Foundry ಚಿತ್ರ ಮಾದರಿ ಪಟ್ಟಿ](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) ಲಭ್ಯತೆ ಮತ್ತು ಪ್ರಾದೇಶಿಕ ಮಾಹಿತಿಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.

> **ಮುಖ್ಯ:** `gpt-image` ಮಾದರಿಗಳು ರಚಿಸಿದ ಚಿತ್ರವನ್ನು **base64** (`b64_json`) ರೂಪದಲ್ಲಿ ನೀಡುತ್ತವೆ, URL ಆಗಿಯೂ ಅಲ್ಲ. ನಿಮ್ಮ ಕೋಡ್ ಆ base64 ಸರಣಿಯನ್ನು ಬೈಟ್ಗಳಾಗಿ ಡಿಕೋಡ್ ಮಾಡಿ ಉಳಿಸುತ್ತದೆ - ಡೌನ್ಲೋಡ್ ಮಾಡಲು ಚಿತ್ರ URL ಇಲ್ಲ.

## ಸಿದ್ಧತೆ

ನೀವು ಮಾದರಿಗಳನ್ನು **Azure OpenAI Microsoft Foundry** ( `aoai-*` ಮಾದರಿಗಳು) ಅಥವಾ **OpenAI ವೇದಿಕೆ** ( `oai-*` ಮಾದರಿಗಳು) ನಲ್ಲಿ ಚಲಾಯಿಸಬಹುದು.

### 1. ಮಾದರಿ ರಚಿಸಿ ಮತ್ತು ನಿಯೋಜಿಸಿ

[ಮೂಲಸೌಕರ್ಯ ರಚಿಸುವ](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) ಮಾರ್ಗಸೂಚಿಯನ್ನು ಅನುಸರಿಸಿ Microsoft Foundry ಮೂಲಸೌಕರ್ಯವನ್ನು ನಿರ್ಮಿಸಿ ಮತ್ತು ನಂತರ ಚಿತ್ರ ಮಾದರಿಯನ್ನು ನಿಯೋಜಿಸಿ - **`gpt-image-2`** ಶಿಫಾರಸು ಮಾಡಿದುದು.

### 2. ನಿಮ್ಮ `.env` ಅನ್ನು ವಿನ್ಯಾಸಗೊಳಿಸಿ

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

ನೀವು ಈ ಮೌಲ್ಯಗಳನ್ನು ನಿಮ್ಮ Foundry ಪೋರ್ಟಲ್‌ನ **Deployments** ಪುಟದಲ್ಲಿ ಕಾಣಬಹುದು.

### 3. ಗ್ರಂಥಾಲಯಗಳನ್ನು ಸ್ಥಾಪಿಸಿ

`requirements.txt` ಅನ್ನು ಸೃಷ್ಟಿಸಿ:

```text
python-dotenv
openai
pillow
```

ನಂತರ ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ಸೃಷ್ಠಿಸಿ ಮತ್ತು ಸಕ್ರಿಯಗೊಳಿಸಿ ಮತ್ತು ಸ್ಥಾಪಿಸಿಕೊಳ್ಳಿ:

```bash
python3 -m venv venv
source venv/bin/activate        # ವಿಂಡೋಸ್: venv\Scripts\activate
pip install -r requirements.txt
```

## ಅಪ್ಲಿಕೇಶನ್ ರಚನೆ

ಕೆಳಗಿನ ಕೋಡ್‌ನೊಂದಿಗೆ `app.py`ನ್ನು ಸೃಷ್ಟಿಸಿ. ಇದು ಒಂದು ಚಿತ್ರ ರಚಿಸಿ PNG ಆಗಿ ಉಳಿಸುತ್ತದೆ.

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# ಕ್ಲೈಯೆಂಟ್ ಅನ್ನು ನಿಮ್ಮ ಅಜೂರ್ ಓಪನ್‌ಎಐ (ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ) ಸಂಪನ್ಮೂಲಕ್ಕೆ ಸೂಚಿಸಿ.
# ಚಿತ್ರ ಮಾದರಿಗಳು ಹೊಸತಾದ API ಆವೃತ್ತಿಯನ್ನು ಬೇಕು - ನಿಮ್ಮ ಮಾದರಿ ಅಗತ್ಯವಿರುವ ಆವೃತ್ತಿಗಾಗಿ ಫೌಂಡ್ರಿ ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # ಉದಾ. "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # ಜೊತೆಗೆ 1536x1024 (ಲ್ಯಾಂಡ್‌ಸ್ಕೇಪ್), 1024x1536 (ಪೋರ್ಟ್ರೇಟ್), ಅಥವಾ "ಆಟೋ"
    n=1,
)

# gpt-image ಮಾದರಿಗಳು ಯುಆರ್‌ಎಲ್ ಅಲ್ಲದೆ ಬೇಸ್64 (b64_json) ಅನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತವೆ - ಅದನ್ನು bait್ಗಳಿಗೆ ಡಿಕೋಡ್ ಮಾಡಿ.
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

`python app.py` ನೊಂದಿಗೆ ಚಲಾಯಿಸಿ. `images/` ಅಡಿಯಲ್ಲಿ PNG ಉಳಿಸಿ ಪಡೆಯುತ್ತೀರಿ.

> `images.generate` ತಲೆಬಾಣಿಗೆ ಪ್ರತಿ ಕರೆ ಒಂದೇ ಪ್ರಾಂಪ್ಟ್‌ಗೆ ವಿವಿಧ ಚಿತ್ರಗಳನ್ನು ಉತ್ಪಾದಿಸುತ್ತದೆ - ಚಿತ್ರ ಮಾದರಿಗಳು `temperature` ನಿಯಂತ್ರಣವನ್ನು ತೆಗೆದುಕೊಳ್ಳದು (ಅದು ಪಠ್ಯ ರಚನೆ ನಿಯಂತ್ರಣ). ವಿಭಿನ್ನತೆಗಾಗಿ ಮತ್ತೆ API ಅನ್ನು ಕರೆಮಾಡಿರಿ; ಕಡಿಮೆ ಮಾಡಲು ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಸ್ಪಷ್ಟವಾಗಿರಿಸಿ.

## ಚಿತ್ರ ಸಂಪಾದನೆ

`gpt-image` ಮಾದರಿಗಳು ಈಗ ಇರುವ ಚಿತ್ರವನ್ನು **ಸಂಪಾದನೆ** ಮಾಡಬಹುದು: ಚಿತ್ರ, ಐಚ್ಛಿಕ **ಮಾಸ್ಕ** (ಬದಲಾಯಿಸಬೇಕಾದ ಪ್ರದೇಶ ಗುರುತಿಸುವುದು) ಮತ್ತು ಬದಲಾವಣೆಯ ವಿವರಣೆ ಇರುವ ಪ್ರಾಂಪ್ಟ್ ನೀಡಿ. ರಚನೆ ಹಾಗೆಯೇ, ಸಂಪಾದನೆಗಳು ಬೇಸ್64ನಲ್ಲಿ ಮರಳುತ್ತವೆ.

```python
result = client.images.edit(
    model=deployment,
    image=open("sunlit_lounge.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="A sunlit indoor lounge area with a pool containing a flamingo",
)
image_bytes = base64.b64decode(result.data[0].b64_json)
with open("images/edited-image.png", "wb") as f:
    f.write(image_bytes)
```

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/kn/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/kn/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/kn/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## ಮೆಟಾಪ್ರಾಂಪ್ಟ್ಗಳೊಂದಿಗೆ ಗಡಿಗಳನ್ನು ನಿಗದಿಪಡಿಸುವುದು

ನೀವು ಚಿತ್ರಗಳನ್ನು ರಚಿಸಬಲ್ಲಾಗುವ ನಂತರ, ನೀವು ನೀವು ಅಪ್ಲಿಕೇಶನ್ ಅಪಾಯಕಾರಿ ಅಥವಾ ಬ್ರ್ಯಾಂಡ್ ವಿರುದ್ಧ ವಿಷಯವನ್ನು ಉತ್ಪಾದಿಸದ ರೀತಿಯಲ್ಲಿ ರಕ್ಷಣೆ ಬೇಕಾಗುತ್ತದೆ. **ಮೆಟಾಪ್ರಾಂಪ್ಟ್** ಎಂಬುದು ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ಗೆ ಮೊದಲಿಗೆ ಸೇರಿಸುವ ಪಠ್ಯ, ಇದರಿಂದ ಮಾದರಿಯ output ನಿರ್ಬಂಧವಾಗುತ್ತದೆ.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# `prompt` ಅನ್ನು client.images.generate(...) ಗೆ ನೀಡಿ
```

ಈಗ ಪ್ರತಿಯೊಬ್ಬ ಚಿತ್ರವೂ ಮೆಟಾಪ್ರಾಂಪ್ಟ್ ಮೂಲಕ ಹೇರಳಿಸಿರುವ ಗಡಿಗಳೊಳಗಿಂದ ಉಂಟಾಗುತ್ತದೆ. ಇದನ್ನು Microsoft Foundry ನಲ್ಲಿ ನಿರ್ಮಿತ ವಿಷಯ ತಡೆಗಟ್ಟುವಿಕೆಯನ್ನು ಜೊತೆಗಿಟ್ಟುಕೊಳ್ಳಿ.

## ಕೆಲಸ - ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ ಸಹಾಯ ಮಾಡೋಣ

Edu4All ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ ಅವರ ಮೌಲ್ಯಮಾಪನಗಳಿಗೆ ಚಿತ್ರಗಳು ಬೇಕಾಗಿವೆ. ನೀವು ಸಾಹಸ ಮತ್ತು ಸೃಜನಶೀಲ ಪರಿಸರಗಳಲ್ಲಿ **ಸ್ಮಾರಕಗಳು** (ನೀವು ಯಾವ ಸ್ಮಾರಕಗಳನ್ನು ಎಂಬುದು ನಿಮ್ಮ ನಿರ್ಧಾರ) ಇರುವ ಚಿತ್ರಗಳನ್ನು ರಚಿಸುವ ಅಪ್ಲಿಕೇಶನ್ ನಿರ್ಮಿಸಿ - ಉದಾಹರಣೆಗೆ, ಸೂರ್ಯಾಸ್ತದಲ್ಲಿ ಒಂದು ಪ್ರಸಿದ್ಧ ನೆಲೆ ಕೇಂದ್ರದಲ್ಲಿ ಗುಮ್ಮಟ ನೋಡುತ್ತಿರುವ ಬಾಲಕ.

ಸ್ವತಃ ಪ್ರಯತ್ನಿಸಿ, ನಂತರ ಉದಾಹರಣೆ ಪರಿಹಾರಗಳೊಂದಿಗೆ ಹೋಲಿಸಿ:

- ಪೈಥಾನ್ (ಅಜ್ಯುರ್): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- ಪೈಥಾನ್ (ಅಜ್ಯುರ್) ಪೂರ್ಣ ರಚನಾ ಅಪ್ಲಿಕೇಶನ್: [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- ಪೈಥಾನ್ (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- ಟೈಪ್ಸ್ಕ್ರಿಪ್ಟ್ (ಅಜ್ಯುರ್): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (ಅಜ್ಯುರ್): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

[python/](../../../09-building-image-applications/python) ನೋಟ್ಬುಕ್‌ಗಳ ಮೂಲಕ ಕೆಲಸ ಮಾಡಿ (`aoai-assignment.ipynb` - ಅಜ್ಯುರ್, `oai-assignment.ipynb` - OpenAI).

## ಅದ್ಭುತ ಕೆಲಸ! ನಿಮ್ಮ ಅಧ್ಯಯನವನ್ನು ಮುಂದುವರೆಸಿ

ಈ ಪಾಠವನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ಮೇಲೆ, ನಮ್ಮ [ತ್ಪನ್ನಾತ್ಮಕ AI ಅಧ್ಯಯನ ಸಂಗ್ರಹ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ಅನ್ನು ನೋಡಿ ನಿಮ್ಮ ತತ್ವಾತ್ಮಕ AI ಜ್ಞಾನವನ್ನು ಮತ್ತಷ್ಟು ಅಭಿವೃದ್ಧಿಪಡಿಸಿಕೊಳ್ಳಿ!

ಪಾಠ 10ಕ್ಕೆ ಹೋಗಿ ಮುಂದುವರಣೆ ಕಲಿಯಿರಿ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->