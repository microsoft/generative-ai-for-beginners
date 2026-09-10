# Skapa bildgenereringsapplikationer

[![Skapa bildgenereringsapplikationer](../../../translated_images/sv/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Det finns mer i LLMs än textgenerering. Du kan också generera bilder från textbeskrivningar. Bilder som modalitet är användbara inom MedTech, arkitektur, turism, spelutveckling, marknadsföring och mer. I denna lektion tittar vi på dagens **GPT Image**-modeller och bygger en bildgenereringsapp.

## Introduktion

Bildgenerering låter dig förvandla en natur-språkig prompt till en bild. I denna lektion arbetar vi med **`gpt-image`** familjen av modeller från OpenAI – den nuvarande generationen av bildmodeller tillgängliga på **[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)** och OpenAI-plattformen. Dessa modeller ersätter de äldre DALL·E-modellerna (DALL·E 2/3 är föråldrade).

Under lektionen använder vi en fiktiv startup, **Edu4All**, som bygger lärverktyg. Teamet vill generera illustrationer för uppgifter och studiematerial.

## Lärandemål

I slutet av denna lektion kommer du att kunna:

- Förklara vad bildgenerering är och var det är användbart.
- Förstå familjen `gpt-image` modeller och hur de skiljer sig från de äldre DALL·E-modellerna.
- Bygga en bildgenereringsapp i Python (och TypeScript / .NET).
- Redigera bilder och tillämpa säkerhetsåtgärder med metaprompter.

## Vad är bildgenerering?

Bildgenereringsmodeller skapar bilder från en textprompt. Moderna modeller som `gpt-image` är byggda på transformer- och diffusionsmetoder: modellen lär sig sambandet mellan text och bilder under träning, och sedan, givet en prompt, iterativt "borttagande av brus" från slumpmässigt brus till en bild som matchar beskrivningen.

Två välkända familjer av bildmodeller är:

- **`gpt-image` (OpenAI)** – den nuvarande generationen, som används i denna lektion. Den stödjer text-till-bild-generering och bildredigering (inpainting med mask).
- **Midjourney** – en populär tredjepartsmodell med egen tjänst och Discord-baserat arbetsflöde.

> Äldre OpenAI-bildmodeller – **DALL·E 2** och **DALL·E 3** – är föråldrade. DALL·E 3 är inte längre tillgänglig för nya distributioner, och funktioner som `create_variation` fanns endast i DALL·E 2. Använd `gpt-image`-modellerna för nya applikationer.

### Vilken `gpt-image`-modell ska jag använda?

På Microsoft Foundry är följande **generellt tillgängliga**:

| Modell | Anteckningar |
| --- | --- |
| **`gpt-image-2`** | Den senaste och mest kapabla bildmodellen – rekommenderas som standard. |
| `gpt-image-1.5` | Generellt tillgänglig; stark kvalitet till lägre kostnad. |
| `gpt-image-1-mini` | Generellt tillgänglig; snabbast / lägst kostnad. |
| `gpt-image-1` | Endast förhandsvisning. |

Kontrollera alltid den aktuella [Foundry-listan över bildmodeller](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) för tillgänglighet och regioner.

> **Viktigt:** `gpt-image`-modeller returnerar den genererade bilden som **base64** (`b64_json`), inte som en URL. Din kod avkodar base64-strängen till bytes och sparar den – det finns ingen bild-URL att ladda ner.

## Setup

Du kan köra exemplen mot **Azure OpenAI i Microsoft Foundry** (exemplen `aoai-*`) eller **OpenAI-plattformen** (exemplen `oai-*`).

### 1. Skapa och distribuera en modell

Följ guiden [skapa en resurs](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) för att skapa en Microsoft Foundry-resurs, distribuer sedan en bildmodell – **`gpt-image-2`** rekommenderas.

### 2. Konfigurera din `.env`

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

Hitta dessa värden på **Deployments**-sidan för din resurs i [Foundry-portalen](https://ai.azure.com?WT.mc_id=academic-105485-koreyst).

### 3. Installera biblioteken

Skapa en `requirements.txt`:

```text
python-dotenv
openai
pillow
```

Skapa sedan och aktivera en virtuell miljö och installera:

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Bygg appen

Skapa `app.py` med följande kod. Den genererar en bild och sparar den som en PNG.

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# Peka klienten mot din Azure OpenAI (Microsoft Foundry) resurs.
# Bildmodeller kräver en nyare API-version - kontrollera Foundry-dokumentationen för den version som din modell kräver.
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # t.ex. "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # även 1536x1024 (landskap), 1024x1536 (porträtt) eller "auto"
    n=1,
)

# gpt-image-modeller returnerar base64 (b64_json), inte en URL - avkoda det till bytes.
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

Kör den med `python app.py`. Du får en PNG sparad under `images/`.

> Varje anrop till `images.generate` producerar en annan bild för samma prompt – bildmodeller har inte en `temperature`-parameter (det är en textgenereringskontroll). För att få variation, anropa API:et igen; för att minska variationen, gör din prompt mer specifik.

## Redigera bilder

`gpt-image`-modeller kan **redigera** en befintlig bild: ge bilden, en valfri **mask** (som markerar området att ändra), och en prompt som beskriver ändringen. Liksom vid generering returneras redigeringarna som base64.

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
  <img src="../../../translated_images/sv/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sv/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sv/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## Sätta gränser med metaprompter

När du kan generera bilder behöver du skyddsåtgärder så att din app inte producerar osäkert eller icke-varumärkesenligt innehåll. En **metaprompt** är text som du lägger till före användarens prompt för att begränsa modellens output.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# skicka `prompt` till client.images.generate(...)
```

Varje bild genereras nu inom de gränser som metaprompten sätter. Kombinera detta med innehållsfiltren som är inbyggda i Microsoft Foundry för ett försvar i flera lager.

## Uppgift – låt oss hjälpa studenter

Edu4All-studenter behöver bilder till sina bedömningar. Bygg en app som genererar bilder av **monument** (vilka monument det blir bestämmer du) placerade i olika, kreativa sammanhang – till exempel en känd landmärke vid solnedgång med ett barn som tittar på.

Prova själv, jämför sedan med referenslösningarna:

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) fullständig genereringsapp: [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

Arbeta också igenom notebook-filerna i [python/](../../../09-building-image-applications/python) (`aoai-assignment.ipynb` för Azure, `oai-assignment.ipynb` för OpenAI).

## Bra jobbat! Fortsätt ditt lärande

Efter att ha slutfört denna lektion, kolla in vår [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) för att fortsätta nivå upp din Generative AI-kunskap!

Gå till lektion 10 för att fortsätta lära dig.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->