<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T20:13:50+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "lt"
}
-->
# Vietinis diegimas 🖥️

**Naudokite šį vadovą, jei norite viską paleisti savo kompiuteryje.**  
Turite du pasirinkimus: **(A) natyvus Python + virtual-env** arba **(B) VS Code Dev Container su Docker**.  
Rinkitės, kas jums patogiau—abi parinktys veda prie tų pačių pamokų.

## 1.  Reikalavimai

| Įrankis             | Versija / Pastabos                                                                      |
|---------------------|----------------------------------------------------------------------------------------|
| **Python**          | 3.10 + (atsisiųskite iš <https://python.org>)                                          |
| **Git**             | Naujausia (yra su Xcode / Git for Windows / Linux paketų tvarkykle)                    |
| **VS Code**         | Nebūtinas, bet rekomenduojamas <https://code.visualstudio.com>                         |
| **Docker Desktop**  | *Tik* B pasirinkimui. Nemokamas diegimas: <https://docs.docker.com/desktop/>           |

> 💡 **Patarimas** – Patikrinkite įrankius terminale:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  A pasirinkimas – Natyvus Python (greičiausias)

### 1 žingsnis  Nukopijuokite šį repozitoriją

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### 2 žingsnis Sukurkite ir aktyvuokite virtualią aplinką

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prieš komandų eilutę turėtų atsirasti (.venv)—tai reiškia, kad esate aplinkoje.

### 3 žingsnis Įdiekite priklausomybes

```bash
pip install -r requirements.txt
```

Pereikite prie 3 skyriaus apie [API raktus](../../../00-course-setup)

## 2. B pasirinkimas – VS Code Dev Container (Docker)

Ši repozitorija ir kursas paruošti su [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst), kuriame yra universalus vykdymo aplinka, palaikanti Python3, .NET, Node.js ir Java kūrimą. Susijusi konfigūracija aprašyta faile `devcontainer.json`, esančiame aplanke `.devcontainer/` šios repozitorijos šaknyje.

>**Kodėl verta rinktis šį variantą?**
>Identiška aplinka kaip Codespaces; jokių priklausomybių neatitikimų.

### 0 žingsnis Įdiekite papildomus įrankius

Docker Desktop – patikrinkite, ar ```docker --version``` veikia.
VS Code Remote – Containers plėtinys (ID: ms-vscode-remote.remote-containers).

### 1 žingsnis Atidarykite repozitoriją su VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code aptinka .devcontainer/ ir išmeta pranešimą.

### 2 žingsnis Atidarykite iš naujo konteineryje

Paspauskite “Reopen in Container”. Docker sukurs atvaizdį (pirmą kartą apie 3 min.).
Kai pasirodys terminalo eilutė, būsite konteineryje.

## 2.  C pasirinkimas – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) – tai lengvas [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python ir kelių paketų diegimo įrankis.
Pats Conda yra paketų tvarkyklė, leidžianti lengvai kurti ir keisti skirtingas Python [**virtualias aplinkas**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ir paketus. Taip pat patogu diegti paketus, kurių nėra per `pip`.

### 0 žingsnis  Įdiekite Miniconda

Vadovaukitės [MiniConda diegimo gidu](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), kad ją įdiegtumėte.

```bash
conda --version
```

### 1 žingsnis Sukurkite virtualią aplinką

Sukurkite naują aplinkos failą (*environment.yml*). Jei naudojate Codespaces, sukurkite jį `.devcontainer` kataloge, t.y. `.devcontainer/environment.yml`.

### 2 žingsnis  Užpildykite aplinkos failą

Įtraukite šį fragmentą į savo `environment.yml`

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

### 3 žingsnis Sukurkite savo Conda aplinką

Paleiskite šias komandas komandinėje eilutėje/terminale

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Jei kyla problemų, žiūrėkite [Conda aplinkų gidą](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

## 2  D pasirinkimas – Klasikinis Jupyter / Jupyter Lab (naršyklėje)

> **Kam tai skirta?**  
> Visiems, kurie mėgsta klasikinę Jupyter sąsają arba nori paleisti užrašines be VS Code.  

### 1 žingsnis  Įsitikinkite, kad Jupyter įdiegtas

Norėdami paleisti Jupyter lokaliai, atsidarykite terminalą/komandinę eilutę, nueikite į kurso katalogą ir vykdykite:

```bash
jupyter notebook
```

arba

```bash
jupyterhub
```

Tai paleis Jupyter ir komandinėje eilutėje parodys URL, kuriuo galėsite pasiekti.

Atsidarę tą URL, matysite kurso turinį ir galėsite naršyti po bet kurį `*.ipynb` failą. Pavyzdžiui, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Pridėkite savo API raktus

API raktų saugumas yra labai svarbus kuriant bet kokią programą. Rekomenduojame niekada nelaikyti API raktų tiesiogiai kode. Jei šią informaciją įkelsite į viešą repozitoriją, galite susidurti su saugumo problemomis ar net netikėtomis išlaidomis, jei kas nors tuo pasinaudos.
Štai žingsnis po žingsnio, kaip sukurti `.env` failą Python ir pridėti `GITHUB_TOKEN`:

1. **Eikite į savo projekto katalogą**: Atidarykite terminalą ar komandų eilutę ir nueikite į projekto šaknį, kur norite sukurti `.env` failą.

   ```bash
   cd path/to/your/project
   ```

2. **Sukurkite `.env` failą**: Naudokite mėgstamą teksto redaktorių, kad sukurtumėte naują failą pavadinimu `.env`. Jei naudojate komandų eilutę, galite naudoti `touch` (Unix sistemose) arba `echo` (Windows):

   Unix sistemos:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Redaguokite `.env` failą**: Atidarykite `.env` failą teksto redaktoriuje (pvz., VS Code, Notepad++ ar kitame). Pridėkite šią eilutę, pakeisdami `your_github_token_here` į savo tikrą GitHub raktą:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Išsaugokite failą**: Išsaugokite pakeitimus ir uždarykite redaktorių.

5. **Įdiekite `python-dotenv`**: Jei dar neturite, įdiekite `python-dotenv` paketą, kad galėtumėte įkelti aplinkos kintamuosius iš `.env` failo į Python programą. Įdiekite su `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Įkelkite aplinkos kintamuosius į Python skriptą**: Savo Python kode naudokite `python-dotenv` paketą, kad įkeltumėte kintamuosius iš `.env` failo:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Viskas! Sėkmingai sukūrėte `.env` failą, pridėjote GitHub raktą ir įkėlėte jį į Python programą.

🔐 Niekada neįkelkite .env—jis jau yra .gitignore.
Pilnas tiekėjų instrukcijas rasite [`providers.md`](03-providers.md).

## 4. Kas toliau?

| Noriu…              | Eiti į…                                                                  |
|---------------------|--------------------------------------------------------------------------|
| Pradėti 1 pamoką    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| Nustatyti LLM tiekėją | [`providers.md`](03-providers.md)                                      |
| Susipažinti su kitais mokiniais | [Prisijunkite prie Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Problemos ir sprendimai

| Simptomas                                   | Sprendimas                                                        |
|---------------------------------------------|-------------------------------------------------------------------|
| `python not found`                          | Pridėkite Python į PATH arba iš naujo atidarykite terminalą       |
| `pip` negali sukurti wheels (Windows)       | `pip install --upgrade pip setuptools wheel` ir bandykite dar kartą.|
| `ModuleNotFoundError: dotenv`               | Paleiskite `pip install -r requirements.txt` (aplinka neįdiegta). |
| Docker build klaida *No space left*         | Docker Desktop ▸ *Settings* ▸ *Resources* → padidinkite disko vietą.|
| VS Code vis prašo atidaryti iš naujo        | Gali būti, kad aktyvios abi parinktys; pasirinkite vieną (venv **arba** container)|
| OpenAI 401 / 429 klaidos                    | Patikrinkite `OPENAI_API_KEY` reikšmę / užklausų limitus.         |
| Klaidos naudojant Conda                     | Įdiekite Microsoft AI bibliotekas su `conda install -c microsoft azure-ai-ml`|

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojame profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už bet kokius nesusipratimus ar neteisingą interpretavimą, kilusį naudojantis šiuo vertimu.