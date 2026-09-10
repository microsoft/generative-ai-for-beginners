# பட உருவாக்கும் செயலிகள் கட்டமைத்தல்

[![பட உருவாக்கும் செயலிகள் கட்டமைத்தல்](../../../translated_images/ta/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLMகளில் உரை உருவாக்கம் மட்டுமல்ல. உரைக் விளக்கங்களிலிருந்து படங்களை உருவாக்கவும் முடியும். படங்கள் ஒரு தொகுதியின்படியே மருத்துவ தொழில்நுட்பம், கட்டிடக்கலை, சுற்றுலா, விளையாட்டு மேம்பாடு, சந்தைப்படுத்தல் மற்றும் பல துறைகளில் உதவிக்கரமாக உள்ளன. இந்த பாடத்தில் நாம் இன்றைய **GPT பட** மாதிரிகளைப் பற்றி தெரிந்து பட உருவாக்கும் செயலியை கட்டமைப்போம்.

## அறிமுகம்

படம் உருவாக்கம் இயல்பான மொழி கோரிக்கையைப் பிரதி படமாக மாற்றுகிறது. இந்த பாடத்தில் நாம் OpenAI இன் **`gpt-image`** குடும்ப மாதிரிகள் - தற்போதைய தலைமுறை பட மாதிரிகள், **[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)** மற்றும் OpenAI தளத்தில் கிடைக்கும் மாதிரிகளைப் பயன்படுத்துவோம். இவை பழைய DALL·E மாதிரிகளை மாற்றியுள்ளன (DALL·E 2/3 பழமையானவை).

பாடத்தின் முழுக்க, நாம் கற்பனைமிக்க ஒரு தொடக்கம் நிறுவனமான **Edu4All**-ஐ பயன்படுத்துகிறோம், இது கற்கை கருவிகள் உருவாக்குகிறது. அந்நிறுவன குழு பணிகள் மற்றும் கல்வி பொருட்களுக்கான விளக்கப்படங்களை உருவாக்க விரும்புகிறது.

## கற்றல் குறிக்கோள்கள்

இந்த பாடம் முடிவில் நீங்கள்:

- படம் உருவாக்கம் என்றதைக் கூறிக் கொள்வதோடு, எங்கு பயனுள்ளதாக இருக்கும் என்பது புரியும்.
- `gpt-image` மாதிரி குடும்பத்தைப் புரிந்துகொள்வதும் பழைய DALL·E மாதிரிகளுக்கு எப்படி வேறுபடுகிறது என்பதும்.
- Python (மற்றும் TypeScript / .NET) பயிலர்கள் பட உருவாக்க செயலியை கட்டமைத்தல்.
- படங்களை திருத்துதல் மற்றும் பாதுகாப்பு நிரல்களை (metaprompts) பயன்படுத்துதல்.

## படம் உருவாக்கம் என்றால் என்ன?

படம் உருவாக்கும் மாதிரிகள் ஒரு உரை கோரிக்கையிலிருந்து படங்களை உருவாக்குகின்றன. சமகால மாதிரிகள், உதாரணத்திற்கு `gpt-image` ஆகியவை மாற்றி + பரவல் தொழில்நுட்பங்களை அடிப்படையாகக் கொண்டு உருவாக்கப்பட்டவை: மாதிரி பயிற்சியில் உரை மற்றும் பட உறவை கற்றுக்கொண்டு, பிறகு, கோரிக்கைக்கேற்ப, பட விளக்கத்துக்கு பொருந்தும் படமாக காணாமல் பாயும் சத்தத்தைக் "தூய்மையாக்க" செய்கிறது.

இரண்டு பிரபலமான பட மாதிரி குடும்பங்கள்:

- **`gpt-image` (OpenAI)** - தற்போதைய தலைமுறை, இந்த பாடத்தில் பயன்படுத்தப்படுகிறது. உரை-முதல்-பட உருவாக்கத்தையும் பட திருத்தத்தையும் (முகப்பatisation) ஆதரிக்கிறது.
- **Midjourney** - தனிப்பட்ட சேவை மற்றும் Discord அடிப்படையிலான பணிவழிகள் உள்ள பிரபலமான மூன்றாம் தரப்பு மாதிரி.

> பழைய OpenAI பட மாதிரிகள் - **DALL·E 2** மற்றும் **DALL·E 3** - பழமையானவை. DALL·E 3 புதிய அமைப்புகளில் கிடைக்காது, மற்றும் `create_variation` போன்ற அம்சங்கள் DALL·E 2-ல் மட்டுமே இருந்தன. புதிய செயலிகளுக்கு `gpt-image` மாதிரிகளைப் பயன்படுத்தவும்.

### எந்த `gpt-image` மாதிரியை பயன்படுத்த வேண்டும்?

Microsoft Foundryல் பின்வருவன **பொதுவாக கிடைக்கும்**:

| மாதிரி | குறிப்பு |
| --- | --- |
| **`gpt-image-2`** | சமீபத்திய மற்றும் மிகவும் திறமையான பட மாதிரி - பரிந்துரைக்கப்படும் இயல்பு. |
| `gpt-image-1.5` | பொதுவாக கிடைக்கும்; குறைந்த செலவில் உயர்ந்த தரம். |
| `gpt-image-1-mini` | பொதுவாக கிடைக்கும்; மிக வேகமாகவும் குறைந்த செலவும். |
| `gpt-image-1` | முன்னோட்டம் மட்டும். |

உள்ளூர் மற்றும் கிடைக்கும் நிலைகளை அறிய எப்போதும் தற்போதைய [Foundry பட மாதிரிகள் பட்டியலை](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) பார்க்கவும்.

> **முக்கியம்:** `gpt-image` மாதிரிகள் உருவாக்கிய படத்தை ஒரு URL ஆக அல்ல, **base64** (`b64_json`) வடிவில் அளிக்கின்றன. உங்கள் குறியீடு base64 வரிசையை பைட்டுகளாக மாற்றி சேமிக்கின்றது - பதிவிறக்குவதற்கு பட URL இல்லை.

## அமைப்பு

நீங்கள் **Microsoft Foundry இல் Azure OpenAI** (அல்லது `aoai-*` உதாரணங்கள்) அல்லது **OpenAI தளம்** (`oai-*` உதாரணங்கள்) மூலம் மாதிரிகளை இயக்கலாம்.

### 1. மாதிரியை உருவாக்கவும் செலுத்தவும்

Microsoft Foundry வளத்தை உருவாக்க [create a resource](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) வழிகாட்டியின்படி பின்பற்றவும், பிறகு பட மாதிரியை பணியில் வைக்கவும் - **`gpt-image-2`** பரிந்துரைக்கப்படுகிறது.

### 2. உங்கள் `.env` ஐ அமைக்கவும்

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

உங்கள் Foundry வளத்தின் **Deployments** பக்கத்தில் இந்த மதிப்புகளை காணலாம் [Foundry portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst).

### 3. நூலகங்களை நிறுவவும்

`requirements.txt` உருவாக்கவும்:

```text
python-dotenv
openai
pillow
```

பிறகு ஒரு மெய்நிகர் சுற்றுப்பாதையை உருவாக்கி செயல்படுத்தி, நிறுவவும்:

```bash
python3 -m venv venv
source venv/bin/activate        # விண்டோஸ்: venv\Scripts\activate
pip install -r requirements.txt
```

## செயலி கட்டமைத்தல்

பின்வரும் குறியீடு உடன் `app.py` உருவாக்கவும். இது ஒரு படம் உருவாக்கி PNG ஆகச் சேமிக்கும்.

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# கிளையண்டை உங்கள் Azure OpenAI (Microsoft Foundry) வளத்தின் மீது குறிக்கவும்.
# பட மாடல்கள் சமீபத்திய API பதிப்பு தேவை - உங்கள் மாடல் எதைப் பயன்படுத்துகிறது என்பதற்கான Foundry ஆவணங்களைச் சரிபார்க்கவும்.
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # உதாரணத்திற்கு "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # மேலும் 1536x1024 (உருவம்), 1024x1536 (நிலையாக), அல்லது "auto"
    n=1,
)

# gpt-image மாடல்கள் URL அல்லாமல் base64 (b64_json) கொடுக்கும் - அதனை பைட்டுகளாக மாற்றவும்.
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

`python app.py` உடன் இயக்கவும். `images/` கோப்புறைக்கு PNG சேமிக்கப்படும்.

> ஒவ்வொரு `images.generate` அழைப்பும் ஒரே கோரிக்கைக்கு வேறுபட்ட படத்தை உருவாக்கும் - படம் மாதிரிகள் `temperature` என்ற அளவுகோளை காணவில்லை (அது உரை உருவாக்கக் கட்டுப்பாடு). விதிவிலக்கை பெற, API ஐ மீண்டும் அழைக்கவும்; குறைக்க, உங்கள் கோரிக்கையை குவியுங்கள்.

## படங்களை திருத்துதல்

`gpt-image` மாதிரிகள் ஒரு படத்தை **திருத்தலாம்**: படத்தை கொடுக்கவும், விருப்பமான **முகப்பatisation** (மாற்ற வேண்டிய பகுதியை குறிக்கும்), மற்றும் மாற்றத்தை விவரிக்கும் ஒரு கோரிக்கையை அளிக்கவும். உருவாக்கம் போல திருத்தங்களும் base64 ஆக வழங்கப்படும்.

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
  <img src="../../../translated_images/ta/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/ta/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/ta/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## metapromptகளை பயன்படுத்தி எல்லைகளை அமைத்தல்

நீங்கள் படங்களை உருவாக்கும் போது, உங்கள் செயலி பாதுகாப்பற்ற அல்லது பிராண்டுக்கு முரண்பட்ட உள்ளடக்கம் தானாக உருவாக்காமல் இருக்க உதவி ரீதியான எல்லைகள் வேண்டும். **metaprompt** என்பது பயனரின் கோரிக்கைக்கு முன்னதாக இடப்படும் உரை, இதனால் மாதிரி வெளிப்பாடு கட்டுப்படுத்தப்படுகிறது.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# `prompt` ஐ client.images.generate(...) க்கு அனுப்புக
```

இப்போது எல்லா படங்களும் metaprompt வழங்கிய எல்லைகளுக்குள் உருவாக்கப்படும். இதனுடன் Microsoft Foundry உள்ளடக்க வடிகட்டிகளையும் சேர்த்து பாதுகாப்பை வலுப்படுத்துங்கள்.

## பணிகள் - மாணவர்களுக்கு உதவுவோம்

Edu4All மாணவர்களுக்கு அவர்களின் மதிப்பீடுகளுக்கான படங்கள் தேவை. **சின்னசின்ன நினைவிடங்களின்** படங்களை வேறு, ரசிக்கக்கூடிய சூழல்களில் (உதாரணமாக, ஒரு புகழ்பெற்ற இடதிகாலையில் ஒரு குழந்தை பார்ப்பது போன்ற) உருவாக்கும் செயலியை கட்டமைக்கவும்.

நீங்கள் முயற்சித்து பாருங்கள், பிறகு குறிப்பிட்ட தீர்வுகளுடன் ஒப்பிடுங்கள்:

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) முழு உருவாக்க செயலி: [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

மேலும் [python/](../../../09-building-image-applications/python) உள்ள நோட்டு பாடங்களில் படியுங்கள் (`aoai-assignment.ipynb` Azureக்கு, `oai-assignment.ipynb` OpenAIக்கு).

## சிறந்த வேலை! உங்கள் கற்றலை தொடருங்கள்

இந்த பாடம் முடிந்ததும், எங்கள் [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) பார்க்கவும், உங்கள் கணித எழுச்சியைத் தொடரவும்!

அடுத்த பாடமான பாடம் 10க்கு செல்லவும்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->