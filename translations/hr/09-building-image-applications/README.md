# Izrada aplikacija za generiranje slika

[![Izrada aplikacija za generiranje slika](../../../translated_images/hr/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Postoji više od generiranja teksta kod LLM-ova. Također možete generirati slike iz tekstualnih opisa. Slike kao modalitet su korisne u medicinskoj tehnologiji, arhitekturi, turizmu, razvoju igara, marketingu i drugdje. U ovom ćemo satu pogledati današnje **GPT Image** modele i izgraditi aplikaciju za generiranje slika.

## Uvod

Generiranje slika omogućava vam da prirodni jezični upit pretvorite u sliku. U ovom satu radimo s obitelji modela **`gpt-image`** iz OpenAI-ja - trenutnom generacijom modela slika dostupnih na **[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)** i OpenAI platformi. Ti modeli zamjenjuju starije DALL·E modele (DALL·E 2/3 su naslijeđeni).

Kroz cijeli sat koristimo fiktivni startup, **Edu4All**, koji razvija alate za učenje. Tim želi generirati ilustracije za zadatke i materijale za učenje.

## Ciljevi učenja

Na kraju ovog sata moći ćete:

- Objasniti što je generiranje slika i gdje je korisno.
- Razumjeti obitelj modela `gpt-image` i kako se razlikuju od naslijeđenih DALL·E modela.
- Izraditi aplikaciju za generiranje slika u Pythonu (te TypeScriptu / .NET-u).
- Uređivati slike i primjenjivati sigurnosne mjere pomoću metaprompta.

## Što je generiranje slika?

Modeli generiranja slika stvaraju slike iz tekstualnog upita. Moderni modeli poput `gpt-image` temelje se na tehnikama transformera + difuzije: model uči odnos između teksta i slika tijekom treniranja, zatim, na temelju upita, iterativno "odšumljava" slučajnu buku u sliku koja odgovara opisu.

Dvije dobro poznate obitelji modela slika su:

- **`gpt-image` (OpenAI)** - trenutna generacija, korištena u ovom satu. Podržava generiranje slika iz teksta i uređivanje slika (inpainting s maskom).
- **Midjourney** - popularni model treće strane s vlastitom uslugom i radnim tijekom temeljenim na Discordu.

> Stariji OpenAI modeli slika - **DALL·E 2** i **DALL·E 3** - su naslijeđeni. DALL·E 3 više nije dostupan za nova implementiranja, a značajke poput `create_variation` postojale su samo u DALL·E 2. Za nove aplikacije koristite modele `gpt-image`.

### Koji `gpt-image` model trebam koristiti?

Na Microsoft Foundry dostupni su sljedeći modeli kao **Opće dostupni**:

| Model | Napomene |
| --- | --- |
| **`gpt-image-2`** | Najnoviji i najsposobniji model za slike - preporučeni zadani model. |
| `gpt-image-1.5` | Opće dostupan; jaka kvaliteta po nižoj cijeni. |
| `gpt-image-1-mini` | Opće dostupan; najbrži / najjeftiniji. |
| `gpt-image-1` | Samo pregled. |

Uvijek provjerite trenutni [popis modela slika u Foundryju](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) za dostupnost i regije.

> **Važno:** modeli `gpt-image` vraćaju generiranu sliku kao **base64** (`b64_json`), a ne kao URL. Vaš kod dekodira base64 niz u bajtove i sprema sliku - ne postoji URL slike za preuzimanje.

## Postavljanje

Možete pokrenuti primjere protiv **Azure OpenAI u Microsoft Foundryju** (primjeri `aoai-*`) ili **OpenAI platforme** (primjeri `oai-*`).

### 1. Izradite i implementirajte model

Slijedite vodič za [izradu resursa](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) da biste izradili Microsoft Foundry resurs, zatim implementirajte model slika - preporuča se **`gpt-image-2`**.

### 2. Konfigurirajte svoj `.env`

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

Vrijednosti pronađite na stranici **Deployments** vašeg resursa u [Foundry portalu](https://ai.azure.com?WT.mc_id=academic-105485-koreyst).

### 3. Instalirajte biblioteke

Izradite `requirements.txt`:

```text
python-dotenv
openai
pillow
```

Zatim izradite i aktivirajte virtualno okruženje te instalirajte:

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Izrada aplikacije

Izradite `app.py` s sljedećim kodom. Generira sliku i sprema je kao PNG.

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# Usmjerite klijenta na vaš Azure OpenAI (Microsoft Foundry) resurs.
# Modeli za slike trebaju nedavnu verziju API-ja - provjerite Foundry dokumentaciju za verziju koju vaš model zahtijeva.
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # npr. "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # također 1536x1024 (pejzaž), 1024x1536 (portret) ili "auto"
    n=1,
)

# gpt-image modeli vraćaju base64 (b64_json), ne URL - dekodirajte ga u bajtove.
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

Pokrenite ga s `python app.py`. Dobit ćete PNG spremljen u `images/`.

> Svaki poziv `images.generate` proizvodi drugačiju sliku za isti upit - modeli slika ne koriste parametar `temperature` (to je kontrola generiranja teksta). Za raznolikost jednostavno pozovite API ponovno; za smanjivanje raznolikosti, učinite svoj upit preciznijim.

## Uređivanje slika

`gpt-image` modeli mogu **uređivati** postojeću sliku: dostavite sliku, opcionalnu **masku** (koja označava područje za promjenu) i upit koji opisuje promjenu. Kao i generiranje, uređene slike vraćaju se u base64 formatu.

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
  <img src="../../../translated_images/hr/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/hr/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/hr/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## Postavljanje granica s metapromptima

Nakon što možete generirati slike, trebate sigurnosne mjere da vaša aplikacija ne proizvodi nesiguran ili neprikladan sadržaj. **Metaprompt** je tekst koji pridodate korisničkom upitu kako biste ograničili izlaz modela.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# proslijedi `prompt` funkciji client.images.generate(...)
```

Svaka se slika sada generira unutar granica postavljenih metapromptom. To kombinirajte s filtrima sadržaja ugrađenima u Microsoft Foundry za duboku obranu.

## Zadatak - omogućimo studentima

Studenti Edu4All trebaju slike za svoje zadatke. Napravite aplikaciju koja generira slike **spomenika** (koje spomenike odaberete, ovisi o vama) smještenih u različite, kreativne kontekste - na primjer, poznati poznati lokalitet u zalazak sunca sa djetetom koje gleda.

Isprobajte sami, zatim usporedite s referentnim rješenjima:

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) potpuna aplikacija za generiranje: [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

Također obradite bilježnice u [python/](../../../09-building-image-applications/python) (`aoai-assignment.ipynb` za Azure, `oai-assignment.ipynb` za OpenAI).

## Odličan posao! Nastavite učiti

Nakon završetka ovog sata, pogledajte našu [kolekciju za Generativnu AI edukaciju](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) da nastavite razvijati svoje znanje o Generativnoj AI!

Krenite na lekciju 10 da nastavite s učenjem.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->