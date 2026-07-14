# Lokalna Postava 🖥️

**Koristite ovaj vodič ako radije sve pokrećete na vlastitom laptopu.**   
Imate dva puta: **(A) nativni Python + virtual-env** ili **(B) VS Code Dev Container s Dockerom**.  
Odaberite što vam je lakše—obje opcije vode do istih lekcija.

## 1.  Preduvjeti

| Alat               | Verzija / Napomene                                                                   |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (dohvatite ga sa <https://python.org>)                                        |
| **Git**            | Najnoviji (dolazi s Xcode / Git za Windows / paketni upravitelj za Linux)            |
| **VS Code**        | Opcionalno, ali preporučeno <https://code.visualstudio.com>                          |
| **Docker Desktop** | *Samo* za Opciju B. Besplatna instalacija: <https://docs.docker.com/desktop/>       |

> 💡 **Savjet** – Provjerite alate u terminalu:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Opcija A – Nativni Python (najbrže)

### Korak 1  Klonirajte ovaj repozitorij

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Korak 2 Kreirajte i aktivirajte virtualno okruženje

```bash
python -m venv .venv          # napravi jedan
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prompt sada treba početi s (.venv)—to znači da ste unutar okruženja.

### Korak 3 Instalirajte ovisnosti

```bash
pip install -r requirements.txt
```

Preskočite na Odjeljak 3 za [API ključeve](#3-dodajte-vaše-api-ključeve)

## 2. Opcija B – VS Code Dev Container (Docker)

Postavili smo ovaj repozitorij i tečaj s [razvojnim kontejnerom](https://containers.dev?WT.mc_id=academic-105485-koreyst) koji ima univerzalno okruženje za Python3, .NET, Node.js i Java razvoj. Povezana konfiguracija definirana je u datoteci `devcontainer.json` koja se nalazi u mapi `.devcontainer/` u korijenu ovog repozitorija.

>**Zašto odabrati ovo?**
>Identično okruženje kao Codespaces; nema problema s ovisnostima.

### Korak 0 Instalirajte dodatke

Docker Desktop – potvrdite da ```docker --version``` radi.
VS Code Remote – Containers ekstenzija (ID: ms-vscode-remote.remote-containers).

### Korak 1 Otvorite repozitorij u VS Code-u

Datoteka ▸ Otvori mapu…  → generative-ai-for-beginners

VS Code detektira .devcontainer/ i pojavit će se prompt.

### Korak 2 Ponovno otvaranje u kontejneru

Kliknite “Reopen in Container”. Docker gradi sliku (≈ 3 min prvi put).
Kada terminal prompt bude vidljiv, unutar ste kontejnera.

## 2.  Opcija C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lagani instalacijski program za instalaciju [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python-a i nekoliko paketa.
Conda sama po sebi je upravitelj paketa koji olakšava postavljanje i prebacivanje između različitih Python [**virtualnih okruženja**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) i paketa. Također je korisna za instalaciju paketa koji nisu dostupni putem `pip`.

### Korak 0  Instalirajte Miniconda

Slijedite [Vodič za instalaciju MiniConde](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) za postavljanje.

```bash
conda --version
```

### Korak 1 Kreirajte virtualno okruženje

Kreirajte novu datoteku okruženja (*environment.yml*). Ako koristite Codespaces, kreirajte je unutar direktorija `.devcontainer`, dakle `.devcontainer/environment.yml`.

### Korak 2  Popunite datoteku okruženja

Dodajte sljedeći isječak u vašu `environment.yml`

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

### Korak 3 Kreirajte Conda okruženje

Pokrenite donje naredbe u svom naredbenom retku/terminalu

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer podputanja odnosi se samo na Codespace postavke
conda activate ai4beg
```

Pogledajte [Vodič za Conda okruženja](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ako naiđete na poteškoće.

## 2  Opcija D – Klasični Jupyter / Jupyter Lab (u vašem pregledniku)

> **Za koga je ovo?**  
> Za sve koji vole klasični Jupyter ili žele pokretati bilježnice bez VS Code-a.  

### Korak 1  Provjerite je li Jupyter instaliran

Za pokretanje Jupyter-a lokalno, otvorite terminal/naredbeni redak, idite u direktorij tečaja i izvršite:

```bash
jupyter notebook
```

ili

```bash
jupyterhub
```

Ovo će pokrenuti Jupyter instancu i URL za pristup bit će prikazan u prozoru naredbenog retka.

Kada pristupite URL-u, trebali biste vidjeti sadržaj tečaja i moći pristupiti bilo kojoj `*.ipynb` datoteci. Na primjer, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Dodajte Vaše API Ključeve

Čuvanje vaših API ključeva sigurnim je važno kod izrade bilo koje vrste aplikacije. Preporučujemo da ne spremate API ključeve izravno u vaš kod. Spremanje ovih podataka u javni repozitorij može dovesti do sigurnosnih problema pa čak i neželjenih troškova ako ih iskoristi zlonamjerna osoba.
Evo korak-po-korak vodiča kako kreirati `.env` datoteku za Python i dodati svoje Microsoft Foundry modele akreditive:

> **Napomena:** GitHub modeli (i njegova varijabla `GITHUB_TOKEN`) bit će povučeni krajem srpnja 2026. Ovaj vodič koristi [Microsoft Foundry Modele](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) umjesto toga. Radite li radije potpuno offline? Pogledajte [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Idite do direktorija vašeg projekta**: Otvorite terminal ili naredbeni redak i idite do korijenskog direktorija vašeg projekta gdje želite kreirati `.env` datoteku.

   ```bash
   cd path/to/your/project
   ```

2. **Kreirajte `.env` datoteku**: Koristite omiljeni uređivač teksta da kreirate novu datoteku nazvanu `.env`. Ako koristite naredbeni redak, možete koristiti `touch` (na Unix-based sustavima) ili `echo` (na Windowsu):

   Unix-based sustavi:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Uredite `.env` datoteku**: Otvorite `.env` datoteku u uređivaču teksta (npr. VS Code, Notepad++, ili bilo kojem drugom). Dodajte sljedeće retke u datoteku, zamjenjujući pokazatelje stvarnim Microsoft Foundry projekt endpointom i API ključem:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Spremite datoteku**: Spremite promjene i zatvorite uređivač teksta.

5. **Instalirajte `python-dotenv`**: Ako ga još nemate, instalirajte paket `python-dotenv` kako biste mogli učitati varijable okruženja iz `.env` datoteke u vašu Python aplikaciju. Možete ga instalirati pomoću `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Učitajte varijable okruženja u vaš Python skript**: U vašem Python skriptu koristite paket `python-dotenv` za učitavanje varijabli okruženja iz `.env` datoteke:

   ```python
   from dotenv import load_dotenv
   import os

   # Učitaj varijable okoline iz .env datoteke
   load_dotenv()

   # Pristupi varijablama Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

To je to! Uspješno ste kreirali `.env` datoteku, dodali svoje Microsoft Foundry modele akreditive i učitali ih u svoju Python aplikaciju.

🔐 Nikada ne commitajte `.env`—već je u `.gitignore`.
Cjelovite upute za providere nalaze se u [`providers.md`](03-providers.md).

## 4. Što slijedi?

| Želim…                | Idi na…                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| Početak Lekcije 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Postaviti LLM Providera | [`providers.md`](03-providers.md)                                       |
| Upoznati druge učenike | [Pridruži se našem Discordu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Rješavanje problema

| Simptom                                  | Rješenje                                                           |
|------------------------------------------|-------------------------------------------------------------------|
| `python not found`                       | Dodajte Python u PATH ili ponovno otvorite terminal nakon instalacije |
| `pip` ne može graditi wheels (Windows)   | Pokrenite `pip install --upgrade pip setuptools wheel` i pokušajte ponovno. |
| `ModuleNotFoundError: dotenv`             | Pokrenite `pip install -r requirements.txt` (okruženje nije instalirano). |
| Docker build ne uspijeva *Nema prostora*  | Docker Desktop ▸ *Settings* ▸ *Resources* → povećajte veličinu diska. |
| VS Code stalno traži ponovno otvaranje   | Možda imate aktivne obje opcije; odaberite jednu (venv **ili** kontejner) |
| OpenAI 401 / 429 pogreške                 | Provjerite vrijednost `OPENAI_API_KEY` / ograničenja brzine zahtjeva. |
| Pogreške pri korištenju Conde             | Instalirajte Microsoft AI biblioteke pomoću `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->