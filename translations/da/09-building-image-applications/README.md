# Byg applikationer til billedgenerering

[![Byg applikationer til billedgenerering](../../../translated_images/da/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Der er mere i LLM'er end blot tekstgenerering. Du kan også generere billeder ud fra tekstbeskrivelser. Billeder som modalitet er nyttige inden for MedTech, arkitektur, turisme, spiludvikling, markedsføring og mere. I denne lektion ser vi på dagens **GPT Image** modeller og bygger en app til billedgenerering.

## Introduktion

Billedgenerering lader dig omdanne en naturligt formuleret prompt til et billede. I denne lektion arbejder vi med **`gpt-image`** familien af modeller fra OpenAI - den nuværende generation af billedmodeller tilgængelig på **[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)** og OpenAI-platformen. Disse modeller erstatter de ældre DALL·E modeller (DALL·E 2/3 er forældede).

Gennem lektionen bruger vi en fiktiv startup, **Edu4All**, der udvikler læringsværktøjer. Teamet ønsker at generere illustrationer til opgaver og studiematerialer.

## Læringsmål

Når du er færdig med denne lektion, vil du kunne:

- Forklare hvad billedgenerering er, og hvor det er brugbart.
- Forstå `gpt-image` model-familien og hvordan den adskiller sig fra de ældre DALL·E modeller.
- Bygge en app til billedgenerering i Python (og TypeScript / .NET).
- Redigere billeder og anvende sikkerhedsforanstaltninger med metaprompts.

## Hvad er billedgenerering?

Billedgenereringsmodeller skaber billeder ud fra en tekstprompt. Moderne modeller som `gpt-image` er bygget på transformer- og diffusions-teknikker: modellen lærer sammenhængen mellem tekst og billeder under træningen, og derefter "denoiser" den gentagne gange tilfældig støj til et billede, der matcher beskrivelsen.

To velkendte familier af billedmodeller er:

- **`gpt-image` (OpenAI)** - den nuværende generation, brugt i denne lektion. Den understøtter tekst-til-billede generering og billedredigering (inpainting med maske).
- **Midjourney** - en populær tredjepartsmodel med egen service og workflow via Discord.

> Ældre OpenAI billedmodeller - **DALL·E 2** og **DALL·E 3** - er forældede. DALL·E 3 er ikke længere tilgængelig for nye udrulninger, og funktioner som `create_variation` fandtes kun i DALL·E 2. Brug `gpt-image` modellerne til nye applikationer.

### Hvilken `gpt-image` model skal jeg bruge?

På Microsoft Foundry er følgende **Generelt Tilgængelige**:

| Model | Noter |
| --- | --- |
| **`gpt-image-2`** | Den nyeste og mest kapable billedmodel - anbefalet standard. |
| `gpt-image-1.5` | Generelt tilgængelig; stærk kvalitet til lavere omkostning. |
| `gpt-image-1-mini` | Generelt tilgængelig; hurtigst / billigst. |
| `gpt-image-1` | Kun til forhåndsvisning. |

Tjek altid den aktuelle [Foundry billedmodeller liste](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) for tilgængelighed og regioner.

> **Vigtigt:** `gpt-image` modeller returnerer det genererede billede som **base64** (`b64_json`), ikke som en URL. Din kode skal afkode base64-strengen til bytes og gemme den - der findes ingen billed-URL til download.

## Opsætning

Du kan køre eksemplerne mod **Azure OpenAI i Microsoft Foundry** (de `aoai-*` eksempler) eller **OpenAI-platformen** (de `oai-*` eksempler).

### 1. Opret og deploy en model

Følg guiden til [oprettelse af en ressource](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) for at oprette en Microsoft Foundry-ressource, og deploy herefter en billedmodel - **`gpt-image-2`** anbefales.

### 2. Konfigurer din `.env`

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

Find disse værdier på siden **Deployments** for din ressource i [Foundry-portalen](https://ai.azure.com?WT.mc_id=academic-105485-koreyst).

### 3. Installer bibliotekerne

Opret en `requirements.txt`:

```text
python-dotenv
openai
pillow
```

Så opret og aktiver et virtuelt miljø og installer:

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Byg appen

Opret `app.py` med følgende kode. Den genererer et billede og gemmer det som PNG.

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# Peg klienten mod din Azure OpenAI (Microsoft Foundry) ressource.
# Billedmodeller kræver en nyere API-version - tjek Foundry-dokumentationen for den, din model kræver.
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # f.eks. "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # også 1536x1024 (landskab), 1024x1536 (portræt), eller "auto"
    n=1,
)

# gpt-image modeller returnerer base64 (b64_json), ikke en URL - dekod det til bytes.
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

Kør den med `python app.py`. Du får en PNG gemt under `images/`.

> Hver kald til `images.generate` producerer et forskelligt billede for samme prompt - billedmodeller tager ikke en `temperature` parameter (det er en kontrol for tekstgenerering). For at få variation, kald blot API'en igen; for at reducere variation, gør din prompt mere specifik.

## Redigering af billeder

`gpt-image` modeller kan **redigere** et eksisterende billede: giv billedet, en valgfri **maske** (som markerer området der skal ændres), og en prompt der beskriver ændringen. Ligesom ved generering returneres redigeringer som base64.

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
  <img src="../../../translated_images/da/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/da/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/da/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## Sæt grænser med metaprompts

Når du kan generere billeder, har du brug for sikkerhedsforanstaltninger, så din app ikke producerer unsafe eller off-brand indhold. En **metaprompt** er tekst, som du føjer foran brugerens prompt for at begrænse modellens output.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# giv `prompt` til client.images.generate(...)
```

Hvert billede genereres nu inden for de grænser, metaprompten sætter. Kombiner dette med de indbyggede indholdsfiltre i Microsoft Foundry for dybdegående beskyttelse.

## Opgave - lad os hjælpe eleverne

Edu4Alls elever har brug for billeder til deres vurderinger. Byg en app, der genererer billeder af **monumenter** (hvilke monumenter er op til dig) placeret i forskellige, kreative kontekster - for eksempel et berømt vartegn i solnedgang med et barn, der betragter det.

Prøv det selv, og sammenlign derefter med reference-løsningerne:

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) fuld genereringsapp: [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

Arbejd også igennem notebooks i [python/](../../../09-building-image-applications/python) (`aoai-assignment.ipynb` for Azure, `oai-assignment.ipynb` for OpenAI).

## Fremragende arbejde! Fortsæt din læring

Når du har gennemført denne lektion, så tjek vores [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) for at fortsætte med at udvikle din viden om Generativ AI!

Gå videre til lektion 10 for at fortsætte læringen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->