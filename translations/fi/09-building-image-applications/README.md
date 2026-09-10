# Kuvageneraattorisovellusten rakentaminen

[![Kuvageneraattorisovellusten rakentaminen](../../../translated_images/fi/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM-mallien mahdollisuudet eivät rajoitu pelkkään tekstintuotantoon. Voit myös luoda kuvia tekstikuvausten pohjalta. Kuvien käyttö medteknologiassa, arkkitehtuurissa, matkailussa, pelikehityksessä, markkinoinnissa ja monilla muilla aloilla on hyödyllistä. Tässä oppitunnissa tutustumme tämän päivän **GPT Image** -malleihin ja rakennamme kuvageneraattorisovelluksen.

## Johdanto

Kuvagenerointi mahdollistaa luonnollisen kielen kehotteen muuttamisen kuvaksi. Tässä oppitunnissa työskentelemme OpenAI:n **`gpt-image`** -malliperheen kanssa – nykyisen sukupolven kuvamallit, jotka ovat saatavilla **[Microsoft Foundryssä](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)** ja OpenAI-alustalla. Nämä mallit korvaavat vanhemmat DALL·E-mallit (DALL·E 2/3 ovat vanhentuneita).

Oppitunnin aikana käytämme kuvitteellista startup-yritystä, **Edu4All**, joka kehittää oppimisvälineitä. Tiimi haluaa luoda kuvituksia tehtäviin ja opiskelumateriaaleihin.

## Oppimistavoitteet

Oppitunnin lopussa pystyt:

- Selittämään, mitä kuvagenerointi on ja missä sitä voi hyödyntää.
- Ymmärtämään `gpt-image` -malliperheen ja sen erot vanhoihin DALL·E-malleihin verrattuna.
- Rakentamaan kuvageneraattorisovelluksen Pythonilla (ja TypeScriptillä / .NETillä).
- Muokkaamaan kuvia ja käyttämään turvarajauksia metakehotteiden avulla.

## Mikä on kuvagenerointi?

Kuvagenerointimallit luovat kuvia tekstikehotteesta. Nykyaikaiset mallit, kuten `gpt-image`, perustuvat muunnin- ja diffuusiotekniikoihin: malli oppii tekstin ja kuvien välisen suhteen harjoitteluvaiheessa, minkä jälkeen se annettua kehotetta käyttäen iteratiivisesti "poistaa kohinaa" satunnaisesta melusta luodakseen kuvan, joka vastaa kuvausta.

Kaksi tunnettuja kuvamalliperhettä ovat:

- **`gpt-image` (OpenAI)** – nykyinen sukupolvi, jota käytämme tässä oppitunnissa. Tukee tekstistä kuvaan -generaatiota ja kuvien muokkausta (maalausta maskin avulla).
- **Midjourney** – suosittu kolmannen osapuolen malli omalla palvelullaan ja Discord-pohjaisella työnkululla.

> Vanhemmat OpenAI:n kuvamallit - **DALL·E 2** ja **DALL·E 3** - ovat vanhentuneita. DALL·E 3 ei ole enää saatavilla uusiin käyttöönottoihin, ja ominaisuudet kuten `create_variation` löytyivät vain DALL·E 2:sta. Käytä `gpt-image` -malleja uusissa sovelluksissa.

### Minkä `gpt-image` -mallin pitäisi valita?

Microsoft Foundryssa seuraavat ovat **Laajasti saatavilla**:

| Malli | Huomautuksia |
| --- | --- |
| **`gpt-image-2`** | Uusin ja kyvykäin kuvamalli – suositeltu oletus. |
| `gpt-image-1.5` | Laajasti saatavilla; hyvä laatu edullisemmalla hinnalla. |
| `gpt-image-1-mini` | Laajasti saatavilla; nopein / edullisin. |
| `gpt-image-1` | Vain esikatselu. |

Tarkista aina nykyinen [Foundryn kuvamallien lista](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) saatavuuden ja alueiden osalta.

> **Tärkeää:** `gpt-image` -mallit palauttavat luodun kuvan **base64-muodossa** (`b64_json`), eivät URL-osoitteena. Koodisi dekoodaa base64-merkkijonon tavuiksi ja tallentaa sen – latauslinkkiä kuvalle ei ole.

## Ympäristön valmistelu

Voit suorittaa esimerkit sekä **Azure OpenAI:n Microsoft Foundryssä** ( `aoai-*` -esimerkit) että **OpenAI-alustalla** ( `oai-*` -esimerkit).

### 1. Luo ja ota käyttöön malli

Noudata [resurssin luomisen](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) ohjetta luodaksesi Microsoft Foundryn resurssin ja ota käyttöön kuvamalli – **`gpt-image-2`** on suositeltu.

### 2. Määritä `.env`-tiedostosi

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

Löydät nämä arvot resurssisi **Deployments**-sivulta [Foundryn portaalissa](https://ai.azure.com?WT.mc_id=academic-105485-koreyst).

### 3. Asenna kirjastot

Luo `requirements.txt`:

```text
python-dotenv
openai
pillow
```

Sitten luo ja aktivoi virtuaaliympäristö ja asenna:

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Rakenna sovellus

Luo `app.py` seuraavalla koodilla. Se luo kuvan ja tallentaa sen PNG-muodossa.

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# Suuntaa asiakas Azure OpenAI (Microsoft Foundry) -resurssiisi.
# Kuvamallit tarvitsevat äskettäisen API-version - tarkista Foundryn dokumentaatiosta, mitä versiota mallisi vaatii.
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # esim. "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # myös 1536x1024 (maisema), 1024x1536 (muotokuva) tai "auto"
    n=1,
)

# gpt-kuvamallit palauttavat base64-koodin (b64_json), eivät URL-osoitetta - dekoodaa se tavuiksi.
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

Suorita komennolla `python app.py`. Saat PNG-kuvan tallennettuna kansioon `images/`.

> Jokainen kutsu `images.generate` tuottaa eri kuvan samalla kyselyllä – kuvamalleilla ei ole `temperature`-parametria (se on tekstigeneraation ohjaus). Monipuolisuuden saamiseksi kutsu API uudelleen; monipuolisuuden vähentämiseksi tee kehotteestasi tarkempi.

## Kuvien muokkaus

`gpt-image` -mallit voivat **muokata** olemassa olevaa kuvaa: anna kuva, valinnainen **maski** (joka merkitsee muutettavan alueen) ja kehotteena muutoksen kuvaus. Kuten generoinnissa, muokatut kuvat palautetaan base64-muodossa.

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
  <img src="../../../translated_images/fi/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/fi/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/fi/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## Rajojen asettaminen metakehotteilla

Kun osaat generoida kuvia, tarvitset turvarajat, jotta sovelluksesi ei tuota epäasiallista tai brändistä poikkeavaa sisältöä. **Metakehotteessa** on tekstiä, jonka lisäät käyttäjän kehotteen eteen rajoittaaksesi mallin tuloksia.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# välitä `prompt` client.images.generate(...) -metodille
```

Jokainen kuva generoidaan nyt metakehotteen asettamien rajojen sisällä. Yhdistä tämä Microsoft Foundryn sisältösuodattimiin syväsuojaa varten.

## Tehtävä – anna apua opiskelijoille

Edu4Allin opiskelijat tarvitsevat kuvia arviointeihinsa. Rakenna sovellus, joka generoi kuvia **muistomerkeistä** (mitkä muistomerkit valitset, on sinun päätettävissä) eri luovissa tilanteissa – esimerkiksi tunnettu maamerkki auringonlaskussa lapsen katsellessa.

Kokeile itse ja vertaa referenssiratkaisuihin:

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) täydellinen generointisovellus: [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

Työstä myös läpi notebookit kansiossa [python/](../../../09-building-image-applications/python) (`aoai-assignment.ipynb` Azurelle, `oai-assignment.ipynb` OpenAI:lle).

## Hienoa työtä! Jatka oppimista

Kun olet suorittanut tämän oppitunnin, tutustu [Generative AI Learning -kokoelmaamme](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ja jatka generatiivisen tekoälyn osaamisesi kehittämistä!

Siirry oppitunnille 10 jatkaaksesi oppimista.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->