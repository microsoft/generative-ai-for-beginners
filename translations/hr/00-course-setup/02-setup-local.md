<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T19:38:38+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "hr"
}
-->
# Lokalna instalacija 🖥️

**Koristite ovaj vodič ako želite sve pokrenuti na svom laptopu.**  
Imate dva izbora: **(A) izvorni Python + virtual-env** ili **(B) VS Code Dev Container s Dockerom**.  
Odaberite što vam je lakše—oba vode do istih lekcija.

## 1. Preduvjeti

| Alat                | Verzija / Napomena                                                                |
|---------------------|-----------------------------------------------------------------------------------|
| **Python**          | 3.10 + (preuzmite s <https://python.org>)                                         |
| **Git**             | Najnovija (dolazi s Xcode / Git for Windows / Linux paket menadžerom)             |
| **VS Code**         | Nije obavezno, ali preporučeno <https://code.visualstudio.com>                    |
| **Docker Desktop**  | *Samo* za opciju B. Besplatna instalacija: <https://docs.docker.com/desktop/>     |

> 💡 **Savjet** – Provjerite alate u terminalu:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Opcija A – Izvorni Python (najbrže)

### Korak 1  Klonirajte ovaj repozitorij

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Korak 2  Kreirajte i aktivirajte virtualno okruženje

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prompt bi sada trebao počinjati s (.venv)—to znači da ste unutar okruženja.

### Korak 3  Instalirajte ovisnosti

```bash
pip install -r requirements.txt
```

Preskočite na odjeljak 3 o [API ključevima](../../../00-course-setup)

## 2. Opcija B – VS Code Dev Container (Docker)

Ovaj repozitorij i tečaj su postavljeni s [razvojnim kontenerom](https://containers.dev?WT.mc_id=academic-105485-koreyst) koji ima univerzalno okruženje i podržava Python3, .NET, Node.js i Java razvoj. Konfiguracija se nalazi u datoteci `devcontainer.json` u mapi `.devcontainer/` na vrhu repozitorija.

>**Zašto odabrati ovo?**
>Identično okruženje kao Codespaces; nema razlika u ovisnostima.

### Korak 0  Instalirajte dodatke

Docker Desktop – provjerite da ```docker --version``` radi.
VS Code Remote – Containers ekstenzija (ID: ms-vscode-remote.remote-containers).

### Korak 1  Otvorite repozitorij u VS Codeu

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code prepoznaje .devcontainer/ i prikazuje prompt.

### Korak 2  Otvorite u kontejneru

Kliknite “Reopen in Container”. Docker gradi sliku (≈ 3 min prvi put).
Kad se pojavi terminal, nalazite se unutar kontejnera.

## 2. Opcija C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lagani instalacijski program za [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python i nekoliko paketa.
Conda je menadžer paketa koji olakšava postavljanje i prebacivanje između različitih Python [**virtualnih okruženja**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) i paketa. Također je koristan za instalaciju paketa koji nisu dostupni putem `pip`.

### Korak 0  Instalirajte Miniconda

Slijedite [MiniConda vodič za instalaciju](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) za postavljanje.

```bash
conda --version
```

### Korak 1  Kreirajte virtualno okruženje

Kreirajte novu datoteku okruženja (*environment.yml*). Ako radite u Codespaces, kreirajte je unutar `.devcontainer` direktorija, dakle `.devcontainer/environment.yml`.

### Korak 2  Popunite datoteku okruženja

Dodajte sljedeći isječak u svoj `environment.yml`

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

### Korak 3  Kreirajte Conda okruženje

Pokrenite sljedeće naredbe u terminalu

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Pogledajte [Conda vodič za okruženja](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ako naiđete na probleme.

## 2. Opcija D – Klasični Jupyter / Jupyter Lab (u pregledniku)

> **Za koga je ovo?**  
> Za sve koji vole klasično Jupyter sučelje ili žele pokretati bilježnice bez VS Codea.  

### Korak 1  Provjerite je li Jupyter instaliran

Za pokretanje Jupytera lokalno, otvorite terminal, idite u direktorij tečaja i pokrenite:

```bash
jupyter notebook
```

ili

```bash
jupyterhub
```

Ovo će pokrenuti Jupyter i URL za pristup bit će prikazan u terminalu.

Kada otvorite URL, trebali biste vidjeti sadržaj tečaja i moći se kretati do bilo koje `*.ipynb` datoteke. Na primjer, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Dodajte svoje API ključeve

Važno je čuvati API ključeve sigurno kad razvijate aplikacije. Preporučujemo da ih ne spremate izravno u kod. Ako ih slučajno pošaljete u javni repozitorij, to može dovesti do sigurnosnih problema i neželjenih troškova ako ih netko zloupotrijebi.
Evo koraka kako kreirati `.env` datoteku za Python i dodati `GITHUB_TOKEN`:

1. **Idite u direktorij projekta**: Otvorite terminal ili Command Prompt i idite u glavni direktorij projekta gdje želite kreirati `.env` datoteku.

   ```bash
   cd path/to/your/project
   ```

2. **Kreirajte `.env` datoteku**: Koristite omiljeni uređivač teksta za kreiranje nove datoteke imena `.env`. Ako ste u terminalu, možete koristiti `touch` (na Unix sustavima) ili `echo` (na Windowsu):

   Unix sustavi:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Uredite `.env` datoteku**: Otvorite `.env` u uređivaču teksta (npr. VS Code, Notepad++ ili bilo kojem drugom). Dodajte sljedeći redak, zamijenite `your_github_token_here` sa svojim GitHub tokenom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Spremite datoteku**: Spremite promjene i zatvorite uređivač.

5. **Instalirajte `python-dotenv`**: Ako već niste, instalirajte paket `python-dotenv` za učitavanje varijabli okruženja iz `.env` datoteke u Python aplikaciju. Instalirajte ga pomoću `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Učitajte varijable okruženja u Python skriptu**: U Python skripti koristite `python-dotenv` za učitavanje varijabli iz `.env` datoteke:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

To je to! Uspješno ste kreirali `.env` datoteku, dodali GitHub token i učitali ga u Python aplikaciju.

🔐 Nikad ne šaljite .env—već je u .gitignore.
Pune upute za pružatelje usluga su u [`providers.md`](03-providers.md).

## 4. Što dalje?

| Želim…              | Idi na…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Započeti lekciju 1  | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Postaviti LLM pružatelja | [`providers.md`](03-providers.md)                                  |
| Upoznati druge polaznike | [Pridruži se našem Discordu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Rješavanje problema

| Simptom                                   | Rješenje                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Dodajte Python u PATH ili ponovno otvorite terminal nakon instalacije |
| `pip` ne može izgraditi wheels (Windows)  | `pip install --upgrade pip setuptools wheel` pa pokušajte ponovno. |
| `ModuleNotFoundError: dotenv`             | Pokrenite `pip install -r requirements.txt` (okruženje nije instalirano). |
| Docker build ne uspije *No space left*    | Docker Desktop ▸ *Settings* ▸ *Resources* → povećajte veličinu diska. |
| VS Code stalno traži ponovno otvaranje    | Možda su obje opcije aktivne; odaberite jednu (venv **ili** container)|
| OpenAI 401 / 429 greške                   | Provjerite vrijednost `OPENAI_API_KEY` / ograničenja zahtjeva.  |
| Greške s Conda                            | Instalirajte Microsoft AI biblioteke s `conda install -c microsoft azure-ai-ml`|

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na svom izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.