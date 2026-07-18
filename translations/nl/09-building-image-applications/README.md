# Imagegeneratie-applicaties bouwen

[![Imagegeneratie-applicaties bouwen](../../../translated_images/nl/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Er is meer aan LLM's dan alleen tekstgeneratie. Je kunt ook afbeeldingen genereren op basis van tekstbeschrijvingen. Afbeeldingen als modaliteit zijn nuttig in MedTech, architectuur, toerisme, game-ontwikkeling, marketing en meer. In deze les bekijken we de huidige **GPT Image**-modellen en bouwen we een app voor afbeeldingsgeneratie.

## Introductie

Afbeeldingsgeneratie laat je een natuurlijke taalprompt omzetten in een afbeelding. In deze les werken we met de **`gpt-image`** modelreeks van OpenAI – de huidige generatie afbeeldingsmodellen die beschikbaar zijn op **[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)** en het OpenAI-platform. Deze modellen vervangen de oudere DALL·E-modellen (DALL·E 2/3 zijn legacy).

Gedurende de les gebruiken we een fictieve startup, **Edu4All**, die leermiddelen ontwikkelt. Het team wil illustraties genereren voor opdrachten en studiemateriaal.

## Leerdoelen

Aan het einde van deze les kun je:

- Uitleggen wat afbeeldingsgeneratie is en waar het nuttig voor is.
- Begrijpen wat de `gpt-image` modelreeks is en hoe deze verschilt van de legacy DALL·E-modellen.
- Een app voor afbeeldingsgeneratie bouwen in Python (en TypeScript / .NET).
- Afbeeldingen bewerken en veiligheidsmaatregelen toepassen met metaprompts.

## Wat is afbeeldingsgeneratie?

Afbeeldingsgeneratiemodellen creëren afbeeldingen op basis van een tekstprompt. Moderne modellen zoals `gpt-image` zijn gebouwd op transformer + diffusie-technieken: het model leert tijdens training de relatie tussen tekst en afbeeldingen, en geeft vervolgens, gegeven een prompt, iteratief "ruis weg" om een afbeelding te maken die overeenkomt met de beschrijving.

Twee bekende modelseries voor afbeeldingen zijn:

- **`gpt-image` (OpenAI)** - de huidige generatie, gebruikt in deze les. Ondersteunt tekst-naar-afbeelding generatie en beeldbewerking (inpainting met een masker).
- **Midjourney** - een populair model van derden met een eigen service en Discord-werkstroom.

> Oudere OpenAI-afbeeldingsmodellen - **DALL·E 2** en **DALL·E 3** - zijn legacy. DALL·E 3 is niet meer beschikbaar voor nieuwe implementaties, en functies zoals `create_variation` bestonden alleen in DALL·E 2. Gebruik voor nieuwe toepassingen de `gpt-image` modellen.

### Welk `gpt-image` model moet ik gebruiken?

Op Microsoft Foundry zijn de volgende modellen **Algemeen Beschikbaar**:

| Model | Opmerkingen |
| --- | --- |
| **`gpt-image-2`** | Het nieuwste en meest capabele afbeeldingsmodel - aanbevolen standaard. |
| `gpt-image-1.5` | Algemeen beschikbaar; sterke kwaliteit tegen lagere kosten. |
| `gpt-image-1-mini` | Algemeen beschikbaar; snelst / laagste kosten. |
| `gpt-image-1` | Alleen preview. |

Controleer altijd de actuele [Foundry-afbeeldingsmodellenlijst](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) voor beschikbaarheid en regio's.

> **Belangrijk:** `gpt-image` modellen geven de gegenereerde afbeelding terug als **base64** (`b64_json`), niet als een URL. Je code decodeert de base64-string naar bytes en slaat die op - er is geen afbeeldings-URL om te downloaden.

## Setup

Je kunt de voorbeelden draaien tegen **Azure OpenAI in Microsoft Foundry** (de `aoai-*` voorbeelden) of het **OpenAI platform** (de `oai-*` voorbeelden).

### 1. Maak een model aan en depploy

Volg de [resource aanmaken](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) gids om een Microsoft Foundry resource aan te maken, en deploy vervolgens een afbeeldingsmodel - **`gpt-image-2`** wordt aanbevolen.

### 2. Configureer je `.env`

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

Vind deze waarden op de **Deployments** pagina van je resource in het [Foundry portaal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst).

### 3. Installeer de libraries

Maak een `requirements.txt` aan:

```text
python-dotenv
openai
pillow
```

Maak daarna een virtuele omgeving aan, activeer die en installeer:

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activeren
pip install -r requirements.txt
```

## Bouw de app

Maak `app.py` met de volgende code. Het genereert een afbeelding en slaat die op als PNG.

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# Richt de client op uw Azure OpenAI (Microsoft Foundry) resource.
# Beeldmodellen hebben een recente API-versie nodig - controleer de Foundry-documentatie voor de versie die uw model vereist.
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # bijv. "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # ook 1536x1024 (landschap), 1024x1536 (portret), of "auto"
    n=1,
)

# gpt-image modellen geven base64 (b64_json) terug, geen URL - decodeer het naar bytes.
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

Voer het uit met `python app.py`. Je krijgt een PNG opgeslagen onder `images/`.

> Elke oproep naar `images.generate` produceert een andere afbeelding voor dezelfde prompt - afbeeldingsmodellen gebruiken geen `temperature` parameter (dat is een controle bij tekstgeneratie). Voor variatie roep je de API gewoon opnieuw aan; om variatie te verminderen maak je je prompt specifieker.

## Afbeeldingen bewerken

`gpt-image` modellen kunnen een bestaande afbeelding **bewerken**: geef de afbeelding, een optioneel **masker** (dat het te wijzigen gebied markeert), en een prompt die de wijziging beschrijft. Net als bij generatie worden bewerkingen als base64 teruggegeven.

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
  <img src="../../../translated_images/nl/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/nl/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/nl/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## Grenzen stellen met metaprompts

Zodra je afbeeldingen kunt genereren, heb je beschermingsmaatregelen nodig zodat je app geen onveilige of off-brand inhoud produceert. Een **metaprompt** is tekst die je aan het begin van de gebruikersprompt toevoegt om de output van het model te beperken.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# geef `prompt` door aan client.images.generate(...)
```

Elke afbeelding wordt nu binnen de door de metaprompt gestelde grenzen gegenereerd. Combineer dit met de contentfilters die ingebouwd zijn in Microsoft Foundry voor defence in depth.

## Opdracht - laten we studenten helpen

Edu4All studenten hebben afbeeldingen nodig voor hun opdrachten. Bouw een app die afbeeldingen genereert van **monumenten** (welke monumenten bepaal jij) geplaatst in verschillende, creatieve contexten - bijvoorbeeld een bekend herkenningspunt bij zonsondergang met een kind dat kijkt.

Probeer het zelf, en vergelijk daarna met de referentieoplossingen:

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) volledige generatie-app: [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

Werk ook door de notebooks in [python/](../../../09-building-image-applications/python) (`aoai-assignment.ipynb` voor Azure, `oai-assignment.ipynb` voor OpenAI).

## Goed gedaan! Ga door met leren

Na het voltooien van deze les, bekijk onze [Generative AI Learning collectie](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) om je Generative AI-kennis verder te verdiepen!

Ga door naar les 10 om verder te leren.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->