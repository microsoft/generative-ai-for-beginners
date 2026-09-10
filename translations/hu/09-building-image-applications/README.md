# Képalkotó alkalmazások készítése

[![Képalkotó alkalmazások készítése](../../../translated_images/hu/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

A nagy nyelvi modellek többre képesek, mint csupán szöveggenerálás. Szöveges leírásokból képeket is létrehozhatsz. A képek, mint modalitás, hasznosak az orvostechnikában, építészetben, turizmusban, játékfejlesztésben, marketingben és még sok más területen. Ebben a leckében megnézzük a mai **GPT Image** modelleket, és elkészítünk egy képalkotó alkalmazást.

## Bevezetés

A képalkotás lehetővé teszi, hogy egy természetes nyelvű utasításból képet készíts. Ebben a leckében az OpenAI **`gpt-image`** családjával dolgozunk - ez a jelenlegi generációja a képmodelleknek, amely elérhető a **[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)** és az OpenAI platformon. Ezek a modellek váltják fel a korábbi DALL·E modelleket (a DALL·E 2/3 már örökség).

A lecke során egy fiktív startupot, az **Edu4All**-t használunk példaként, amely tanulási eszközöket fejleszt. A csapat célja, hogy illusztrációkat generáljon házi feladatokhoz és tananyagokhoz.

## Tanulási célok

A lecke végére képes leszel:

- Megmagyarázni, mi az a képalkotás és hol hasznos.
- Megérteni a `gpt-image` modell családot és azt, hogyan különbözik az örökség DALL·E modellektől.
- Képalkotó alkalmazást építeni Pythonban (és TypeScriptben / .NET-ben).
- Képeket szerkeszteni és biztonsági korlátokat alkalmazni metapromptokkal.

## Mi az a képalkotás?

A képalkotó modellek szöveges utasításból állítanak elő képet. A modern modellek, mint a `gpt-image`, transformer + diffúziós technikákra épülnek: a modell a tanulás során megtanulja a szöveg és a képek közötti kapcsolatot, majd egy utasítás hatására iteratívan "zajmentesíti" a véletlenszerű zajt olyan képpé, amely megfelel a leírásnak.

Két jól ismert képmodell család:

- **`gpt-image` (OpenAI)** - a jelenlegi generáció, ezt használjuk ebben a leckében. Támogatja a szövegből kép generálást és a kép szerkesztését (maszkolt felületáthúzás).
- **Midjourney** - népszerű harmadik féltől származó modell, saját szolgáltatással és Discord alapú munkafolyamattal.

> A régebbi OpenAI képmodellek - **DALL·E 2** és **DALL·E 3** - örökségnek számítanak. A DALL·E 3 már nem érhető el új üzembe helyezésekhez, és olyan funkciók, mint a `create_variation`, csak a DALL·E 2-ben léteztek. Új alkalmazásokhoz a `gpt-image` modelleket használd.

### Melyik `gpt-image` modellt használjam?

A Microsoft Foundryban a következők **Általánosan Elérhetőek**:

| Modell | Megjegyzések |
| --- | --- |
| **`gpt-image-2`** | A legújabb és legjobb képmodell - alapértelmezett ajánlás. |
| `gpt-image-1.5` | Általánosan elérhető; jó minőség alacsonyabb költséggel. |
| `gpt-image-1-mini` | Általánosan elérhető; a leggyorsabb / legolcsóbb. |
| `gpt-image-1` | Csak előnézet. |

Mindig ellenőrizd a aktuális [Foundry képmodellek listáját](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) az elérhetőség és régiók miatt.

> **Fontos:** `gpt-image` modellek a generált képet **base64** formátumban (`b64_json`) adják vissza, nem URL-ként. A kódodnak dekódolnia kell a base64 karakterláncot bájtokká, majd el kell mentenie – nincs letölthető kép URL.

## Beállítás

A példákat futtathatod az **Azure OpenAI Microsoft Foundryban** (az `aoai-*` példák) vagy az **OpenAI platformon** (az `oai-*` példák).

### 1. Modell létrehozása és telepítése

Kövesd a [resource létrehozása](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) útmutatót egy Microsoft Foundry erőforrás létrehozásához, majd telepíts egy képmodellt - ajánlott a **`gpt-image-2`**.

### 2. `.env` konfigurálása

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

Ezeket az értékeket a resource **Telepítések** oldalán találod a [Foundry portálon](https://ai.azure.com?WT.mc_id=academic-105485-koreyst).

### 3. Könyvtárak telepítése

Hozz létre egy `requirements.txt` fájlt:

```text
python-dotenv
openai
pillow
```

Ezután hozd létre és aktiváld a virtuális környezetet, majd telepítsd:

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Alkalmazás építése

Készíts `app.py` fájlt az alábbi kóddal. Ez egy képet generál és PNG-ként menti.

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# Állítsa be az ügyfelet az Azure OpenAI (Microsoft Foundry) erőforrására.
# A képmintákhoz egy friss API verzió szükséges - ellenőrizze a Foundry dokumentációját a modellje által igényelt verzióhoz.
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # pl. "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # továbbá 1536x1024 (fekvő), 1024x1536 (álló) vagy "auto"
    n=1,
)

# a gpt-image modellek base64 (b64_json) formátumban adnak vissza adatot, nem URL-t - dekódolja bájtokra.
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

Futásához használd a `python app.py` parancsot. Egy PNG fájl mentődik az `images/` mappába.

> Minden `images.generate` hívás ugyanarra az utasításra más képet generál – a képmodellek nem használnak `temperature` paramétert (ez szöveggenerálási vezérlő). A változatosságért hívd meg újra az API-t; a változatosság csökkentéséhez tedd konkrétabbá az utasítást.

## Képek szerkesztése

A `gpt-image` modellek képesek meglévő képet **szerkeszteni**: megadsz egy képet, opcionálisan egy **maszkot** (ami meghatározza a szerkesztendő területet), és egy utasítást a változtatásról. A szerkesztett képek is base64 formátumban térnek vissza.

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
  <img src="../../../translated_images/hu/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/hu/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/hu/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## Határok felállítása metapromptokkal

Amint képes vagy képeket generálni, biztonsági korlátokra van szükség, hogy az alkalmazásod ne készítsen veszélyes vagy céges arculathoz nem illő tartalmat. A **metaprompt** olyan szöveg, amit a felhasználó utasítása elé helyezel, hogy korlátozd a modell kimenetét.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# add meg a `prompt` értéket a client.images.generate(...) függvénynek
```

Minden kép mostantól a metaprompt által szabott határok között készül. Ezt társítsd a Microsoft Foundry beépített tartalomszűrőivel a mélyreható védelem érdekében.

## Feladat - engedélyezzük a diákokat

Az Edu4All diákjainak képekre van szükségük a feladataikhoz. Készíts egy alkalmazást, amely **műemlékek** képeit generálja (hogy melyek, az rajtad áll), különböző, kreatív helyzetekben - például egy híres nevezetesség naplementében, egy gyerekkel a közelben.

Próbáld ki magad, majd hasonlítsd össze a referencia megoldásokkal:

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) teljes képalkotó alkalmazás: [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

Dolgozz át a jegyzetfüzeteken is a [python/](../../../09-building-image-applications/python) mappában (`aoai-assignment.ipynb` Azurehoz, `oai-assignment.ipynb` OpenAI-hoz).

## Nagyszerű munka! Folytasd a tanulást

Miután befejezted ezt a leckét, nézd meg [Generatív AI Tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább mélyítsd Generatív AI ismereteidet!

Lépj a 10. leckére a tanulás folytatásához.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->