<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5cf0b10ab3c485e6334101f5784f1f3",
  "translation_date": "2025-12-19T17:56:06+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "lt"
}
-->
# Vietinis nustatymas 🖥️

**Naudokite šį vadovą, jei norite viską paleisti savo nešiojamajame kompiuteryje.**  
Turite du kelius: **(A) natūralus Python + virtual-env** arba **(B) VS Code Dev konteineris su Docker**.  
Pasirinkite, kas atrodo lengviau – abu veda į tas pačias pamokas.

## 1.  Prieš sąlygos

| Įrankis            | Versija / Pastabos                                                                   |
|--------------------|-------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (gaukite iš <https://python.org>)                                            |
| **Git**            | Naujausia (ateina su Xcode / Git Windows / Linux paketų tvarkykle)                   |
| **VS Code**        | Pasirinktinai, bet rekomenduojama <https://code.visualstudio.com>                    |
| **Docker Desktop** | *Tik* B variantui. Nemokama instaliacija: <https://docs.docker.com/desktop/>         |

> 💡 **Patarimas** – Patikrinkite įrankius terminale:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Variant A – Natūralus Python (greičiausias)

### 1 žingsnis  Nuklonuokite šį repozitoriją

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

✅ Komandinės eilutės pradžia dabar turėtų būti (.venv) – tai reiškia, kad esate aplinkoje.

### 3 žingsnis Įdiekite priklausomybes

```bash
pip install -r requirements.txt
```

Praleiskite į 3 skyrių apie [API raktus](../../../00-course-setup)

## 2. Variant B – VS Code Dev konteineris (Docker)

Ši repozitorija ir kursas sukonfigūruoti su [kūrimo konteineriu](https://containers.dev?WT.mc_id=academic-105485-koreyst), kuris turi Universalų vykdymo laiką, palaikantį Python3, .NET, Node.js ir Java kūrimą. Susijusi konfigūracija apibrėžta faile `devcontainer.json`, esančiame `.devcontainer/` kataloge šios repozitorijos šaknyje.

>**Kodėl rinktis šį?**  
>Tai identiška aplinka kaip Codespaces; nėra priklausomybių neatitikimų.

### 0 žingsnis Įdiekite papildinius

Docker Desktop – patikrinkite, ar veikia ```docker --version```.  
VS Code Remote – Containers plėtinys (ID: ms-vscode-remote.remote-containers).

### 1 žingsnis Atidarykite repozitoriją VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code aptinka .devcontainer/ ir rodo užklausą.

### 2 žingsnis Atidarykite iš naujo konteineryje

Spustelėkite „Reopen in Container“. Docker sukuria atvaizdą (≈ 3 min pirmą kartą).  
Kai pasirodo terminalo eilutė, esate konteineryje.

## 2.  Variant C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) yra lengvas diegimo įrankis, skirtas įdiegti [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python ir keletą paketų.  
Conda yra paketų tvarkyklė, leidžianti lengvai sukurti ir perjungti tarp skirtingų Python [**virtualių aplinkų**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ir paketų. Taip pat naudinga diegiant paketus, kurių nėra per `pip`.

### 0 žingsnis  Įdiekite Miniconda

Sekite [MiniConda diegimo vadovą](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

```bash
conda --version
```

### 1 žingsnis Sukurkite virtualią aplinką

Sukurkite naują aplinkos failą (*environment.yml*). Jei naudojate Codespaces, sukurkite jį `.devcontainer` kataloge, t.y. `.devcontainer/environment.yml`.

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

Paleiskite žemiau pateiktas komandas savo komandinėje eilutėje/terminale

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer poskelis taikomas tik Codespace nustatymams
conda activate ai4beg
```

Jei kyla problemų, žiūrėkite [Conda aplinkų vadovą](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

## 2  Variant D – Klasikinis Jupyter / Jupyter Lab (naršyklėje)

> **Kam tai skirta?**  
> Visiems, kurie mėgsta klasikinę Jupyter sąsają arba nori paleisti užrašų knygutes be VS Code.

### 1 žingsnis  Įsitikinkite, kad Jupyter įdiegtas

Norėdami paleisti Jupyter lokaliai, atidarykite terminalą/komandinę eilutę, eikite į kurso katalogą ir vykdykite:

```bash
jupyter notebook
```

arba

```bash
jupyterhub
```

Tai paleis Jupyter instanciją, o URL, kuriuo galima pasiekti, bus parodytas komandinės eilutės lange.

Prisijungę prie URL, turėtumėte matyti kurso struktūrą ir galėti naršyti bet kurį `*.ipynb` failą. Pavyzdžiui, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Pridėkite savo API raktus

Svarbu saugiai laikyti savo API raktus, kai kuriate bet kokią programą. Rekomenduojame nerodyti API raktų tiesiogiai kode. Viešai paskelbus šiuos duomenis, gali kilti saugumo problemų ir net nepageidaujamų išlaidų, jei juos naudos kenkėjas.  
Štai žingsnis po žingsnio vadovas, kaip sukurti `.env` failą Python ir pridėti `GITHUB_TOKEN`:

1. **Eikite į savo projekto katalogą**: Atidarykite terminalą arba komandų eilutę ir eikite į savo projekto šaknies katalogą, kur norite sukurti `.env` failą.

   ```bash
   cd path/to/your/project
   ```

2. **Sukurkite `.env` failą**: Naudodami mėgstamą teksto redaktorių sukurkite naują failą pavadinimu `.env`. Jei naudojate komandų eilutę, galite naudoti `touch` (Unix sistemose) arba `echo` (Windows):

   Unix sistemos:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Redaguokite `.env` failą**: Atidarykite `.env` failą teksto redaktoriuje (pvz., VS Code, Notepad++ ar kitame). Pridėkite šią eilutę, pakeisdami `your_github_token_here` savo tikru GitHub raktu:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Išsaugokite failą**: Išsaugokite pakeitimus ir uždarykite redaktorių.

5. **Įdiekite `python-dotenv`**: Jei dar neįdiegėte, turėsite įdiegti paketą `python-dotenv`, kad galėtumėte įkelti aplinkos kintamuosius iš `.env` failo į savo Python programą. Galite įdiegti naudodami `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Įkelkite aplinkos kintamuosius į Python skriptą**: Savo Python skripte naudokite `python-dotenv` paketą, kad įkeltumėte aplinkos kintamuosius iš `.env` failo:

   ```python
   from dotenv import load_dotenv
   import os

   # Įkelti aplinkos kintamuosius iš .env failo
   load_dotenv()

   # Pasiekti GITHUB_TOKEN kintamąjį
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Viskas! Sėkmingai sukūrėte `.env` failą, pridėjote GitHub raktą ir įkėlėte jį į savo Python programą.

🔐 Niekada neįtraukite .env į commit – jis jau yra .gitignore faile.  
Pilnos tiekėjo instrukcijos yra [`providers.md`](03-providers.md).

## 4. Kas toliau?

| Noriu…             | Eiti į…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Pradėti 1 pamoką    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Nustatyti LLM tiekėją | [`providers.md`](03-providers.md)                                       |
| Susipažinti su kitais mokiniais | [Prisijunkite prie mūsų Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Problemų sprendimas

| Simptomas                                | Sprendimas                                                      |
|-----------------------------------------|----------------------------------------------------------------|
| `python not found`                       | Pridėkite Python į PATH arba iš naujo atidarykite terminalą po diegimo |
| `pip` negali sukurti ratų (Windows)     | `pip install --upgrade pip setuptools wheel` ir bandykite dar kartą. |
| `ModuleNotFoundError: dotenv`            | Vykdykite `pip install -r requirements.txt` (aplinka nebuvo įdiegta). |
| Docker build nepavyksta *No space left* | Docker Desktop ▸ *Settings* ▸ *Resources* → padidinkite disko dydį. |
| VS Code nuolat siūlo atidaryti iš naujo | Gali būti aktyvūs abu variantai; pasirinkite vieną (venv **arba** konteinerį) |
| OpenAI 401 / 429 klaidos                 | Patikrinkite `OPENAI_API_KEY` reikšmę / užklausų dažnio ribas.  |
| Klaidos naudojant Conda                  | Įdiekite Microsoft AI bibliotekas su `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->