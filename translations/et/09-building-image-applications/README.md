# Pildigeneratsiooni rakenduste loomine

[![Pildigeneratsiooni rakenduste loomine](../../../translated_images/et/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Suurte keelemudelite (LLM) võimekus ei piirdu vaid teksti genereerimisega. Saad luua ka pilte tekstikirjelduste põhjal. Pildid kui andmekandja on kasulikud MedTechi, arhitektuuri, turismi, mänguarenduse, turunduse ja paljude teiste valdkondade jaoks. Selles õppetükis vaatleme tänaseid **GPT pildimudeleid** ja ehitame pildigeneratsiooni rakenduse.

## Sissejuhatus

Pildigeneratsioon võimaldab muuta loomuliku keelelise viite pildiks. Selles õppetükis kasutame OpenAI **`gpt-image`** mudelite pere — praeguse põlvkonna pildimudelid, mis on saadaval **[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)** ja OpenAI platvormil. Need mudelid asendavad vanemad DALL·E mudelid (DALL·E 2/3 on päritolu).

Kogu õppetüki vältel kasutame väljamõeldud idufirmat **Edu4All**, mis arendab õppevahendeid. Meeskond soovib genereerida joonistusi ülesannete ja õppematerjalide jaoks.

## Õpieesmärgid

Selle õppetüki lõpuks oskad sa:

- Selgitada, mis on pildigeneratsioon ja kus see on kasulik.
- Mõista `gpt-image` mudelite perekonda ja kuidas see erineb päritolu DALL·E mudelitest.
- Ehitada pildigeneratsiooni rakendus Pythonis (ja TypeScript / .NET-is).
- Muuta pilte ja rakendada ohutuspiire metavättidega.

## Mis on pildigeneratsioon?

Pildigeneraatormudelid loovad pilte tekstilise viite põhjal. Moodsaid mudeleid nagu `gpt-image` ehitatakse transformer- ja difusioonitehnikate kombinatsioonina: mudel õpib välja tekstide ja piltide seosed treeningu käigus ning seejärel, saades viite, "puhastab" juhusliku müra iteratiivselt pildiks, mis vastab kirjeldusele.

Kaks hästi tuntud pildimudelite perekonda on:

- **`gpt-image` (OpenAI)** – praegune põlvkond, kasutusel selles õppetükis. Toetab tekstist pildiks genereerimist ja piltide muutmist (inpainting maskiga).
- **Midjourney** – populaarne kolmanda osapoole mudel, oma teenusega ja Discord-põhise töövooga.

> Vanemad OpenAI pildimudelid – **DALL·E 2** ja **DALL·E 3** – on päritolu. DALL·E 3 pole enam saadaval uutesse juurutustesse, ja funktsioonid nagu `create_variation` olid olemas ainult DALL·E 2-s. Uute rakenduste jaoks kasuta `gpt-image` mudeleid.

### Millist `gpt-image` mudelit kasutada?

Microsoft Foundrys on järgmised mudelid **üldiselt saadaval**:

| Mudel | Märkused |
| --- | --- |
| **`gpt-image-2`** | Viimane ja võimsaim pildimudel – soovitatav vaikimisi. |
| `gpt-image-1.5` | Üldiselt saadaval; hea kvaliteet madalama hinnaga. |
| `gpt-image-1-mini` | Üldiselt saadaval; kiireim / madalaim hind. |
| `gpt-image-1` | Ainult eelvaade. |

Kontrolli alati praegust [Foundry pildimudelite nimekirja](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) saadavuse ja regioonide kohta.

> **Oluline:** `gpt-image` mudelid tagastavad genereeritud pildi **base64** kujul (`b64_json`), mitte URL-ina. Sinu kood dekodeerib base64 stringi baitideks ja salvestab selle – pildi URL-i ei ole allalaadimiseks.

## Seadistamine

Võid proovida näiteid käitada **Azure OpenAI Microsoft Foundrys** (näited `aoai-*`) või **OpenAI platvormil** (näited `oai-*`).

### 1. Loo ja juuruta mudel

Järgi juhist [kuidas luua ressursi](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) Microsoft Foundry ressursi loomiseks, seejärel juuruta pildimudel – soovituslik on **`gpt-image-2`**.

### 2. Konfigureeri oma `.env`

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

Leia need väärtused oma ressursi **Juurutuste** leheküljel [Foundry portaali](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) kaudu.

### 3. Paigalda teegid

Loo `requirements.txt`:

```text
python-dotenv
openai
pillow
```

Seejärel loo ja aktiveeri virtuaalne keskkond ning paigalda vajalikud paketid:

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\aktiveeri
pip install -r requirements.txt
```

## Rakenduse ehitamine

Loo fail `app.py` järgmise koodiga. See genereerib pildi ja salvestab selle PNG-na.

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# Suunake klient oma Azure OpenAI (Microsoft Foundry) ressursile.
# Pildimudelid vajavad uusimat API versiooni - kontrollige Foundry dokumentatsioonist, millist versiooni teie mudel nõuab.
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # nt "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # samuti 1536x1024 (maastik), 1024x1536 (portree) või "auto"
    n=1,
)

# gpt-image mudelid tagastavad base64 (b64_json), mitte URL-i - dekodeerige see baitideks.
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

Käivita see käsuga `python app.py`. PNG-fail salvestatakse kataloogi `images/`.

> Iga kutsung `images.generate` meetodile loob sama viite puhul erineva pildi – pildimudelid ei kasuta `temperature` parameetrit (see on teksti genereerimise juhtimise jaoks). Mitmekesisuse saamiseks kutsuge API uuesti; erinevuse vähendamiseks täpsusta oma viidet.

## Piltide muutmine

`gpt-image` mudelid suudavad olemasolevat pilti ka **muuta**: edastad pildi, valikulise **maski** (mis märgib piirkonna muutmiseks) ja viite, mis kirjeldab muudatust. Nagu genereerimisel, tagastatakse muutused base64 vormingus.

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
  <img src="../../../translated_images/et/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/et/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/et/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## Piiride seadmine metavättidega

Kui oled pildid genereerimisvalmis teinud, vajad ohutuspiirdeid, et su rakendus ei looks ebaohutut ega kaubamärgivälist sisu. **Metaväide** on tekst, mille lisad kasutaja viite ees, et mudeli väljundit piirata.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# edasta `prompt` kliendile images.generate(...)
```

Nüüd genereeritakse iga pilt metaväite poolt seatud piirides. Ühenda see Microsoft Foundry sisseehitatud sisufiltritega kaitseks põhjalikumalt.

## Ülesanne – võimaldame õpilastel

Edu4Alli õpilased vajavad pilte oma ülesannete jaoks. Ehitada rakendus, mis genereerib pilte **monumentidest** (millised monumentidest, otsustad sina) erinevates loovates kontekstides – näiteks kuulus maamärk päikeseloojangul lapse silmade all.

Proovi ise, seejärel järgi võrdluseks lahendusi:

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) täielik genereerimisrakendus: [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

Töötle ka läbi märkmikud kaustas [python/](../../../09-building-image-applications/python) (`aoai-assignment.ipynb` Azure jaoks ja `oai-assignment.ipynb` OpenAI jaoks).

## Väga hea töö! Jätka õppimist

Pärast selle õppetüki läbimist vaata meie [Generatiivse tehisintellekti õppimise kogu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et jätkata oma generatiivse tehisintellekti teadmiste tõstmist!

Liigu järgmisele, 10. õppetükile, et edasi õppida.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->