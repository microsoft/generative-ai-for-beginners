# Vytváranie aplikácií na generovanie obrázkov

[![Vytváranie aplikácií na generovanie obrázkov](../../../translated_images/sk/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Viac ako len generovanie textu je možné aj generovanie obrázkov z textových popisov. Obrázky ako modalita sú užitočné v oblastiach MedTech, architektúry, turizmu, vývoja hier, marketingu a ďalších. V tejto lekcii sa pozrieme na dnešné modely **GPT Image** a vytvoríme aplikáciu na generovanie obrázkov.

## Úvod

Generovanie obrázkov umožňuje premeniť prirodzený jazykový prompt na obrázok. V tejto lekcii pracujeme s rodinou modelov **`gpt-image`** od OpenAI - aktuálnou generáciou obrazových modelov dostupných na **[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)** a platforme OpenAI. Tieto modely nahrádzajú staršie modely DALL·E (DALL·E 2/3 sú už zastarané).

Počas celej lekcie používame fiktívny startup, **Edu4All**, ktorý vyvíja nástroje na učenie. Tím chce generovať ilustrácie pre zadania a študijné materiály.

## Ciele učenia

Na konci tejto lekcie budete schopní:

- Vysvetliť, čo je generovanie obrázkov a kde je užitočné.
- Pochopiť rodinu modelov `gpt-image` a ako sa líši od starších modelov DALL·E.
- Vytvoriť aplikáciu na generovanie obrázkov v Pythone (a TypeScripte / .NET).
- Upraviť obrázky a aplikovať bezpečnostné zábrany pomocou metapromptov.

## Čo je generovanie obrázkov?

Modely na generovanie obrázkov vytvárajú obrázky zo vstupného textového promptu. Moderné modely ako `gpt-image` sú založené na technikách transformer + difúzia: model sa počas tréningu učí vzťah medzi textom a obrazmi a potom, na základe promptu, postupne "odšumia" náhodný šum na obrázok zodpovedajúci popisu.

Dve známe rodiny obrazových modelov sú:

- **`gpt-image` (OpenAI)** - súčasná generácia, používaná v tejto lekcii. Podporuje generovanie obrázkov z textu a úpravu obrázkov (inpainting s maskou).
- **Midjourney** - populárny model tretej strany so svojou službou a workflow cez Discord.

> Staršie obrazové modely OpenAI - **DALL·E 2** a **DALL·E 3** - sú zastarané. DALL·E 3 už nie je dostupný pre nové nasadenia a funkcie ako `create_variation` existovali len v DALL·E 2. Pre nové aplikácie používajte modely `gpt-image`.

### Ktorý model `gpt-image` by som mal použiť?

Na Microsoft Foundry sú nasledovné modely **Všeobecne dostupné**:

| Model | Poznámky |
| --- | --- |
| **`gpt-image-2`** | Najnovší a najvýkonnejší model - odporúčaný predvolený. |
| `gpt-image-1.5` | Všeobecne dostupný; silná kvalita s nižšími nákladmi. |
| `gpt-image-1-mini` | Všeobecne dostupný; najrýchlejší / najnižšie náklady. |
| `gpt-image-1` | Len pre náhľad. |

Vždy skontrolujte aktuálny [zoznam modelov Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) pre dostupnosť a regióny.

> **Dôležité:** modely `gpt-image` vracajú generovaný obrázok ako **base64** (`b64_json`), nie ako URL. Váš kód dekóduje base64 reťazec na bajty a uloží ich - neexistuje žiadna URL na stiahnutie obrázka.

## Nastavenie

Ukážky môžete spúšťať proti **Azure OpenAI v Microsoft Foundry** (vzorky `aoai-*`) alebo na **OpenAI platforme** (vzorky `oai-*`).

### 1. Vytvorte a nasadte model

Postupujte podľa návodu [create a resource](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) na vytvorenie zdroja v Microsoft Foundry a potom nasadte obrazový model - odporúča sa **`gpt-image-2`**.

### 2. Nakonfigurujte svoj `.env`

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

Tieto hodnoty nájdete na stránke **Deployments** vášho zdroja v [Foundry portáli](https://ai.azure.com?WT.mc_id=academic-105485-koreyst).

### 3. Nainštalujte knižnice

Vytvorte `requirements.txt`:

```text
python-dotenv
openai
pillow
```

Potom vytvorte a aktivujte virtuálne prostredie a nainštalujte:

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Vytvorte aplikáciu

Vytvorte súbor `app.py` s nasledujúcim kódom. Generuje obrázok a uloží ho ako PNG.

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# Nasmerujte klienta na váš Azure OpenAI (Microsoft Foundry) zdroj.
# Modely obrázkov vyžadujú aktuálnu verziu API - skontrolujte dokumentáciu Foundry pre verziu, ktorú váš model vyžaduje.
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # napr. "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # tiež 1536x1024 (krajina), 1024x1536 (portrét), alebo "auto"
    n=1,
)

# modely gpt-image vracajú base64 (b64_json), nie URL - dekódujte to na bajty.
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

Spustite ho príkazom `python app.py`. Obrázok sa uloží do priečinka `images/`.

> Každé volanie `images.generate` vytvorí iný obrázok pre rovnaký prompt - obrazové modely neakceptujú parameter `temperature` (ten je kontrolou generovania textu). Pre viac variantov API jednoducho zavolajte znova; pre menej variantov zadajte konkrétnejší prompt.

## Úprava obrázkov

Modely `gpt-image` môžu **upravovať** existujúci obrázok: poskytnite obrázok, voliteľnú **masku** (označuje oblasť na zmenu) a prompt popisujúci zmenu. Úpravy sa, podobne ako generovanie, vracajú ako base64.

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
  <img src="../../../translated_images/sk/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sk/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sk/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## Nastavenie hraníc pomocou metapromptov

Keď už viete generovať obrázky, potrebujete zábrany, aby vaša aplikácia nevytvárala nebezpečný alebo neprimeraný obsah. **Metaprompt** je text, ktorý pridáte pred používateľov prompt, aby ste obmedzili výstup modelu.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# odovzdať `prompt` do client.images.generate(...)
```

Každý obrázok sa teraz generuje v rámci hraníc nastavených metapromptom. Kombinujte to s obsahovými filtrami zabudovanými v Microsoft Foundry pre komplexnú ochranu.

## Zadanie - pomôžme študentom

Študenti Edu4All potrebujú obrázky pre svoje úlohy. Vytvorte aplikáciu, ktorá generuje obrázky **pamiatok** (výber pamiatok necháme na vás) umiestnených v rôznych kreatívnych kontextoch - napríklad slávny orientačný bod počas západu slnka s dieťaťom, ktoré sa naň pozerá.

Vyskúšajte to sami, potom porovnajte s referenčnými riešeniami:

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) kompletná aplikácia na generovanie: [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

Tiež prejdite si notebooky v [python/](../../../09-building-image-applications/python) (`aoai-assignment.ipynb` pre Azure, `oai-assignment.ipynb` pre OpenAI).

## Výborná práca! Pokračujte v učení

Po dokončení tejto lekcie navštívte našu [kolekciu na učenie Generatívnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) a naďalej rozvíjajte svoje znalosti o Generatívnej AI!

Pokračujte do lekcie 10 a učte sa ďalej.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->