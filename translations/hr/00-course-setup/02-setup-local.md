<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5cf0b10ab3c485e6334101f5784f1f3",
  "translation_date": "2025-12-19T17:24:49+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "hr"
}
-->
# Lokalna postava 🖥️

**Koristite ovaj vodič ako želite sve pokretati na vlastitom prijenosnom računalu.**  
Imate dva puta: **(A) izvorni Python + virtualno okruženje** ili **(B) VS Code Dev Container s Dockerom**.  
Odaberite onaj koji vam je lakši—obje opcije vode do istih lekcija.

## 1.  Preduvjeti

| Alat               | Verzija / Napomene                                                                  |
|--------------------|------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (preuzmite s <https://python.org>)                                          |
| **Git**            | Najnovija verzija (dolazi s Xcode / Git za Windows / Linux paket menadžer)          |
| **VS Code**        | Opcionalno, ali preporučeno <https://code.visualstudio.com>                         |
| **Docker Desktop** | *Samo* za Opciju B. Besplatna instalacija: <https://docs.docker.com/desktop/>      |

> 💡 **Savjet** – Provjerite alate u terminalu:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Opcija A – Izvorni Python (najbrže)

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

✅ Prompt bi sada trebao počinjati s (.venv)—to znači da ste unutar okruženja.

### Korak 3 Instalirajte ovisnosti

```bash
pip install -r requirements.txt
```

Preskočite na Sekciju 3 o [API ključevima](../../../00-course-setup)

## 2. Opcija B – VS Code Dev Container (Docker)

Postavili smo ovaj repozitorij i tečaj s [razvojnim kontejnerom](https://containers.dev?WT.mc_id=academic-105485-koreyst) koji ima univerzalno runtime okruženje koje podržava Python3, .NET, Node.js i Java razvoj. Povezana konfiguracija definirana je u datoteci `devcontainer.json` koja se nalazi u mapi `.devcontainer/` u korijenu ovog repozitorija.

>**Zašto odabrati ovo?**  
>Identično okruženje kao Codespaces; bez problema s ovisnostima.

### Korak 0 Instalirajte dodatke

Docker Desktop – provjerite radi li ```docker --version```.
VS Code Remote – Containers ekstenzija (ID: ms-vscode-remote.remote-containers).

### Korak 1 Otvorite repozitorij u VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code detektira .devcontainer/ i pojavit će se upit.

### Korak 2 Ponovno otvorite u kontejneru

Kliknite “Reopen in Container”. Docker gradi sliku (≈ 3 min prvi put).  
Kad se pojavi terminal prompt, unutar ste kontejnera.

## 2.  Opcija C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) je lagani instalacijski program za instalaciju [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Pythona, kao i nekoliko paketa.  
Conda je upravitelj paketa koji olakšava postavljanje i prebacivanje između različitih Python [**virtualnih okruženja**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) i paketa. Također je koristan za instalaciju paketa koji nisu dostupni putem `pip`.

### Korak 0  Instalirajte Miniconda

Slijedite [MiniConda instalacijski vodič](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) za postavljanje.

```bash
conda --version
```

### Korak 1 Kreirajte virtualno okruženje

Kreirajte novu datoteku okruženja (*environment.yml*). Ako pratite koristeći Codespaces, kreirajte je unutar direktorija `.devcontainer`, dakle `.devcontainer/environment.yml`.

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

Pokrenite naredbe u vašem komandnom retku/terminalu

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer podputanja se primjenjuje samo na Codespace postavke
conda activate ai4beg
```

Pogledajte [Conda vodič za okruženja](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ako naiđete na probleme.

## 2  Opcija D – Klasični Jupyter / Jupyter Lab (u vašem pregledniku)

> **Za koga je ovo?**  
> Za sve koji vole klasično Jupyter sučelje ili žele pokretati bilježnice bez VS Code-a.  

### Korak 1  Provjerite je li Jupyter instaliran

Za pokretanje Jupyter lokalno, otvorite terminal/komandni redak, navigirajte do direktorija tečaja i izvršite:

```bash
jupyter notebook
```

ili

```bash
jupyterhub
```

Ovo će pokrenuti Jupyter instancu i URL za pristup bit će prikazan u prozoru komandnog retka.

Kad pristupite URL-u, trebali biste vidjeti sadržaj tečaja i moći navigirati do bilo koje `*.ipynb` datoteke. Na primjer, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Dodajte svoje API ključeve

Važno je čuvati svoje API ključeve sigurno prilikom izrade bilo koje vrste aplikacije. Preporučujemo da ne pohranjujete API ključeve izravno u kod. Slanje tih podataka u javni repozitorij može dovesti do sigurnosnih problema pa čak i neželjenih troškova ako ih koristi zlonamjerna osoba.  
Evo korak-po-korak vodiča kako napraviti `.env` datoteku za Python i dodati `GITHUB_TOKEN`:

1. **Idite u direktorij svog projekta**: Otvorite terminal ili komandni redak i navigirajte do korijenskog direktorija vašeg projekta gdje želite kreirati `.env` datoteku.

   ```bash
   cd path/to/your/project
   ```

2. **Kreirajte `.env` datoteku**: Koristite svoj omiljeni uređivač teksta za kreiranje nove datoteke nazvane `.env`. Ako koristite komandni redak, možete koristiti `touch` (na Unix sustavima) ili `echo` (na Windowsu):

   Unix sustavi:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Uredite `.env` datoteku**: Otvorite `.env` datoteku u uređivaču teksta (npr. VS Code, Notepad++ ili bilo koji drugi uređivač). Dodajte sljedeći redak u datoteku, zamjenjujući `your_github_token_here` stvarnim GitHub tokenom:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Spremite datoteku**: Spremite promjene i zatvorite uređivač teksta.

5. **Instalirajte `python-dotenv`**: Ako već niste, trebate instalirati paket `python-dotenv` za učitavanje varijabli okoline iz `.env` datoteke u vašu Python aplikaciju. Možete ga instalirati koristeći `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Učitajte varijable okoline u vaš Python skript**: U vašem Python skriptu koristite paket `python-dotenv` za učitavanje varijabli okoline iz `.env` datoteke:

   ```python
   from dotenv import load_dotenv
   import os

   # Učitaj varijable okoline iz .env datoteke
   load_dotenv()

   # Pristupi varijabli GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

To je to! Uspješno ste kreirali `.env` datoteku, dodali svoj GitHub token i učitali ga u Python aplikaciju.

🔐 Nikada ne šaljite .env u repozitorij—već je u .gitignore.  
Cjelovite upute za pružatelje usluga nalaze se u [`providers.md`](03-providers.md).

## 4. Što dalje?

| Želim…              | Idem na…                                                               |
|---------------------|------------------------------------------------------------------------|
| Početi Lekciju 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)    |
| Postaviti LLM pružatelja | [`providers.md`](03-providers.md)                                    |
| Upoznati druge polaznike | [Pridruži se našem Discordu](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Rješavanje problema

| Simptom                                   | Rješenje                                                        |
|-------------------------------------------|----------------------------------------------------------------|
| `python not found`                        | Dodajte Python u PATH ili ponovno otvorite terminal nakon instalacije |
| `pip` ne može izgraditi wheels (Windows) | `pip install --upgrade pip setuptools wheel` pa pokušajte ponovno. |
| `ModuleNotFoundError: dotenv`             | Pokrenite `pip install -r requirements.txt` (okruženje nije instalirano). |
| Docker build ne uspijeva *No space left*  | Docker Desktop ▸ *Settings* ▸ *Resources* → povećajte veličinu diska. |
| VS Code stalno traži ponovno otvaranje    | Možda imate aktivne obje opcije; odaberite jednu (venv **ili** container) |
| OpenAI 401 / 429 greške                   | Provjerite vrijednost `OPENAI_API_KEY` / ograničenja brzine zahtjeva. |
| Greške pri korištenju Conde                | Instalirajte Microsoft AI biblioteke koristeći `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->