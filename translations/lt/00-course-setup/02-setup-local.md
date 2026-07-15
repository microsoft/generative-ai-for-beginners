# Vietinis nustatymas 🖥️

**Naudokite šį vadovą, jei norite viską paleisti savo nešiojamajame kompiuteryje.**   
Turite du kelius: **(A) gimtasis Python + virtual-env** arba **(B) VS Code Dev konteineris su Docker**.  
Pasirinkite, kas atrodo paprasčiau—abu veda į tas pačias pamokas.

## 1.  Prieš tai

| Įrankis            | Versija / Pastabos                                                                 |
|--------------------|-----------------------------------------------------------------------------------|
| **Python**         | 3.10 + (parsisiųskite iš <https://python.org>)                                    |
| **Git**            | Naujausia (yra su Xcode / Git Windows / Linux paketų tvarkyklėje)                 |
| **VS Code**        | Pasirinktinai, bet rekomenduojama <https://code.visualstudio.com>                  |
| **Docker Desktop** | *Tik* B variantui. Nemokamai: <https://docs.docker.com/desktop/>                   |

> 💡 **Patarimas** – Patikrinkite įrankius terminale:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  A variantas – gimtasis Python (greičiausias)

### 1 žingsnis  Nuklonuokite šį repo

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### 2 žingsnis Sukurkite ir aktyvuokite virtualią aplinką

```bash
python -m venv .venv          # sukurti vieną
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Komandinės eilutės pradžioje dabar turi būti (.venv)—tai reiškia, kad esate aplinkoje.

### 3 žingsnis Įdiekite priklausomybes

```bash
pip install -r requirements.txt
```

Praleiskite į 3 skirsnį apie [API raktus](#3-pridėkite-savo-api-raktus)

## 2. B variantas – VS Code Dev konteineris (Docker)

Šis repo ir kursas sukonfigūruoti su [plėtros konteineriu](https://containers.dev?WT.mc_id=academic-105485-koreyst), kuriame yra universalus vykdymo aplinka palaikanti Python3, .NET, Node.js ir Java vystymą. Susijusi konfigūracija apibrėžta `devcontainer.json` faile, esančiame `.devcontainer/` aplanke šio repo šaknyje.

>**Kodėl rinktis šį?**
>Identiška aplinka kaip Codespaces; nėra papildomų priklausomybių neatitikimų.

### 0 žingsnis Įdiekite papildinius

Docker Desktop – patikrinkite, kad veikia ```docker --version```.
VS Code Remote – Containers plėtinys (ID: ms-vscode-remote.remote-containers).

### 1 žingsnis Atidarykite repo VS Code

Failas ▸ Atidaryti katalogą…  → generative-ai-for-beginners

VS Code aptinka .devcontainer/ ir išmeta pranešimą.

### 2 žingsnis Atidarykite iš naujo konteineryje

Spauskite “Reopen in Container”. Docker pastatys atvaizdą (≈ 3 min pirmą kartą).
Kai atsiras terminalo žymeklis, esate konteineryje.

## 2. C variantas – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) yra lengvas įdiegėjas, skirtas įdiegti [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python ir keletą paketų.
Conda yra paketų tvarkyklė, leidžianti lengvai sukurti ir keisti skirtingas Python [**virtualias aplinkas**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) bei paketus. Ji taip pat naudinga įdiegiant paketus, kurių nėra `pip`.

### 0 žingsnis Įdiekite Miniconda

Sekite [MiniConda diegimo vadovą](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) diegimui.

```bash
conda --version
```

### 1 žingsnis Sukurkite virtualią aplinką

Sukurkite naują aplinkos failą (*environment.yml*). Jei dirbate su Codespaces, sukurkite jį `.devcontainer` kataloge, tai yra `.devcontainer/environment.yml`.

### 2 žingsnis Užpildykite aplinkos failą

Pridėkite šį fragmentą į `environment.yml`

```yml
name: <environment-name>
channels:
 - defaults
 - microsoft
dependencies:
- python=<python-version>
- openai
- python-dotenv
- pip
- pip:
    - azure-ai-ml

```

### 3 žingsnis Sukurkite Conda aplinką

Vykdykite žemiau esančias komandas savo konsolėje/terminale

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer poskelis taikomas tik Codespace konfigūracijoms
conda activate ai4beg
```

Susidūrę su problemomis žr. [Conda aplinkų vadovą](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

## 2. D variantas – klasikinis Jupyter / Jupyter Lab (naršyklėje)

> **Kam tai?**  
> Visiems, kas mėgsta klasikines Jupyter sąsajas arba nori paleisti užrašų knygutes be VS Code.  

### 1 žingsnis Užtikrinkite, kad Jupyter įdiegtas

Norėdami paleisti Jupyter vietoje, terminale eikite į kursų katalogą ir įvykdykite:

```bash
jupyter notebook
```

arba

```bash
jupyterhub
```

Tai paleis Jupyter instanciją, ir jos URL bus rodoma komandinės eilutės lange.

Atidarius URL, matysite kursų turinį ir galėsite naršyti į bet kurį `*.ipynb` failą. Pavyzdžiui, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Pridėkite savo API raktus

Svarbu saugiai laikyti API raktus kuriant bet kokią programėlę. Rekomenduojame nerodyti API raktų tiesiogiai kode. Viešai skelbiami duomenys gali sukelti saugumo problemų ir net nenumatytų išlaidų, jei juos naudos kenksmingi asmenys.
Čia pateikiamas išsamus vadovas, kaip sukurti `.env` failą Python ir pridėti Microsoft Foundry Models kredencialus:

> **Pastaba:** GitHub Models (ir `GITHUB_TOKEN` kintamasis) bus nutrauktas 2026 m. liepos pabaigoje. Vietoje jo naudojami [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Norite dirbti visiškai neprisijungę? Žr. [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Eikite į projektų katalogą**: atidarykite terminalą arba komandinę eilutę ir nueikite į savo projekto šakninį katalogą, kur norite sukurti `.env` failą.

   ```bash
   cd path/to/your/project
   ```

2. **Sukurkite `.env` failą**: naudokite mėgstamą teksto redaktorių naujam failui pavadinimu `.env` sukurti. Jei naudojate komandų eilutę, galite panaudoti `touch` (Unix sistemose) arba `echo` (Windows):

   Unix systemoms:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Redaguokite `.env` failą**: atidarykite `.env` redaktoriuje (pvz., VS Code, Notepad++ ar kitur). Pridėkite šias eilutes, pakeisdami vietas realiais Microsoft Foundry projekto endpointu ir API raktu:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Išsaugokite failą**: išsaugokite pakeitimus ir uždarykite redaktorių.

5. **Įdiekite `python-dotenv`**: jei dar neįdiegta, įdiekite `python-dotenv` paketą, kad galėtumėte įkelti aplinkos kintamuosius iš `.env` į savo Python programą. Naudokite `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Įkelkite aplinkos kintamuosius į Python skriptą**: savo Python faile naudokite `python-dotenv`, kad įkeltumėte kintamuosius iš `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Įkelti aplinkos kintamuosius iš .env failo
   load_dotenv()

   # Prieiga prie Microsoft Foundry Models kintamųjų
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Viskas! Sėkmingai sukūrėte `.env` failą, pridėjote Microsoft Foundry Models kredencialus ir įkėlėte juos į Python programą.

🔐 Niekuomet nekelkite .env į git—jis jau įrašytas .gitignore.
Pilnas tiekėjų nurodymų rinkinys yra [`providers.md`](03-providers.md).

## 4. Kas toliau?

| Noriu…             | Eiti į…                                                                 |
|--------------------|-------------------------------------------------------------------------|
| Pradėti 1 pamoką   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Susikonfigūruoti LLM tiekėją | [`providers.md`](03-providers.md)                                 |
| Susipažinti su kitais mokiniais | [Prisijunkite prie mūsų Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Trikčių šalinimas

| Simptomas                               | Sprendimas                                                      |
|----------------------------------------|----------------------------------------------------------------|
| `python not found`                      | Įtraukite Python į PATH arba iš naujo atidarykite terminalą po diegimo|
| `pip` nepavyksta sukompiliuoti wheel (Windows) | `pip install --upgrade pip setuptools wheel`, tada bandykite dar kartą.|
| `ModuleNotFoundError: dotenv`           | Vykdykite `pip install -r requirements.txt` (env nebuvo įdiegtas).|
| Docker build nepavyksta *No space left*| Docker Desktop ▸ *Nustatymai* ▸ *Ištekliai* → padidinkite disko dydį.|
| VS Code nuolat siūlo perkrauti          | Galbūt veikia abu variantai; pasirinkite vieną (venv **arba** konteinerį)|
| OpenAI 401 / 429 klaidos                 | Patikrinkite `OPENAI_API_KEY` reikšmę / užklausų ribojimus.     |
| Claidžia naudojant Conda                 | Įdiekite Microsoft AI bibliotekas su `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->