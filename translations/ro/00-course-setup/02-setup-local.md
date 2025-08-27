<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T19:11:38+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "ro"
}
-->
# Configurare locală 🖥️

**Folosește acest ghid dacă preferi să rulezi totul pe propriul laptop.**  
Ai două variante: **(A) Python nativ + virtual-env** sau **(B) VS Code Dev Container cu Docker**.  
Alege ce ți se pare mai simplu—ambele duc la aceleași lecții.

## 1.  Cerințe preliminare

| Instrument         | Versiune / Observații                                                                |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (descarcă de la <https://python.org>)                                         |
| **Git**            | Ultima versiune (vine cu Xcode / Git for Windows / managerul de pachete Linux)       |
| **VS Code**        | Opțional, dar recomandat <https://code.visualstudio.com>                             |
| **Docker Desktop** | *Doar* pentru Opțiunea B. Instalare gratuită: <https://docs.docker.com/desktop/>     |

> 💡 **Tip** – Verifică instrumentele în terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Opțiunea A – Python nativ (cea mai rapidă)

### Pasul 1  Clonează acest repo

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Pasul 2 Creează & activează un mediu virtual

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Promptul ar trebui să înceapă acum cu (.venv)—asta înseamnă că ești în mediul virtual.

### Pasul 3 Instalează dependențele

```bash
pip install -r requirements.txt
```

Sari la Secțiunea 3 despre [cheile API](../../../00-course-setup)

## 2. Opțiunea B – VS Code Dev Container (Docker)

Am configurat acest repository și curs cu un [container de dezvoltare](https://containers.dev?WT.mc_id=academic-105485-koreyst) care are un runtime universal ce suportă Python3, .NET, Node.js și Java. Configurația aferentă se află în fișierul `devcontainer.json` din folderul `.devcontainer/` la rădăcina acestui repository.

>**De ce să alegi asta?**
>Mediu identic cu Codespaces; fără diferențe de dependențe.

### Pasul 0 Instalează extra-urile

Docker Desktop – confirmă că ```docker --version``` funcționează.
VS Code Remote – extensia Containers (ID: ms-vscode-remote.remote-containers).

### Pasul 1 Deschide repo-ul în VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code detectează .devcontainer/ și afișează un prompt.

### Pasul 2 Redeschide în container

Apasă “Reopen in Container”. Docker va construi imaginea (≈ 3 min prima dată).
Când apare promptul în terminal, ești în container.

## 2.  Opțiunea C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) este un installer ușor pentru instalarea [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python și câteva pachete.
Conda este un manager de pachete care te ajută să configurezi și să schimbi rapid între diferite [**medii virtuale**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) și pachete Python. E util și pentru instalarea pachetelor care nu sunt disponibile prin `pip`.

### Pasul 0  Instalează Miniconda

Urmează [ghidul de instalare MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) pentru configurare.

```bash
conda --version
```

### Pasul 1 Creează un mediu virtual

Creează un fișier nou de mediu (*environment.yml*). Dacă folosești Codespaces, creează-l în directorul `.devcontainer`, deci `.devcontainer/environment.yml`.

### Pasul 2  Completează fișierul de mediu

Adaugă următorul fragment în `environment.yml`

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

### Pasul 3 Creează mediul Conda

Rulează comenzile de mai jos în linia de comandă/terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consultă [ghidul pentru medii Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) dacă întâmpini probleme.

## 2  Opțiunea D – Jupyter clasic / Jupyter Lab (în browser)

> **Pentru cine e?**  
> Pentru cei care preferă interfața clasică Jupyter sau vor să ruleze notebook-uri fără VS Code.  

### Pasul 1  Asigură-te că Jupyter e instalat

Pentru a porni Jupyter local, deschide terminalul/linia de comandă, navighează la directorul cursului și execută:

```bash
jupyter notebook
```

sau

```bash
jupyterhub
```

Asta va porni o instanță Jupyter și URL-ul de acces va fi afișat în fereastra de comandă.

După ce accesezi URL-ul, ar trebui să vezi structura cursului și să poți naviga la orice fișier `*.ipynb`. De exemplu, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Adaugă cheile tale API

Să păstrezi cheile API în siguranță e esențial când construiești orice aplicație. Nu recomandăm să stochezi cheile direct în cod. Dacă le comiți într-un repository public, poți avea probleme de securitate și chiar costuri nedorite dacă cineva le folosește abuziv.
Iată un ghid pas cu pas pentru a crea un fișier `.env` pentru Python și a adăuga `GITHUB_TOKEN`:

1. **Navighează la directorul proiectului**: Deschide terminalul sau command prompt-ul și mergi în directorul principal al proiectului unde vrei să creezi fișierul `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Creează fișierul `.env`**: Folosește editorul preferat pentru a crea un fișier nou numit `.env`. Dacă folosești linia de comandă, poți folosi `touch` (pe sisteme Unix) sau `echo` (pe Windows):

   Sisteme Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Editează fișierul `.env`**: Deschide fișierul `.env` într-un editor de text (ex: VS Code, Notepad++, sau alt editor). Adaugă următoarea linie, înlocuind `your_github_token_here` cu token-ul tău GitHub real:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Salvează fișierul**: Salvează modificările și închide editorul.

5. **Instalează `python-dotenv`**: Dacă nu ai făcut-o deja, trebuie să instalezi pachetul `python-dotenv` pentru a încărca variabilele de mediu din fișierul `.env` în aplicația ta Python. Poți instala cu `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Încarcă variabilele de mediu în scriptul Python**: În scriptul tău Python, folosește pachetul `python-dotenv` pentru a încărca variabilele din fișierul `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Gata! Ai creat fișierul `.env`, ai adăugat token-ul GitHub și l-ai încărcat în aplicația ta Python.

🔐 Nu comita niciodată .env—este deja în .gitignore.
Instrucțiunile complete pentru furnizori sunt în [`providers.md`](03-providers.md).

## 4. Ce urmează?

| Vreau să…           | Mergi la…                                                                 |
|---------------------|---------------------------------------------------------------------------|
| Începe Lecția 1     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)       |
| Configurează un furnizor LLM | [`providers.md`](03-providers.md)                                 |
| Cunoaște alți cursanți | [Alătură-te pe Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Rezolvare probleme

| Simptom                                   | Soluție                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Adaugă Python în PATH sau redeschide terminalul după instalare  |
| `pip` nu poate construi wheels (Windows)  | `pip install --upgrade pip setuptools wheel` apoi încearcă din nou. |
| `ModuleNotFoundError: dotenv`             | Rulează `pip install -r requirements.txt` (mediul nu a fost instalat). |
| Docker build eșuează *No space left*      | Docker Desktop ▸ *Settings* ▸ *Resources* → mărește spațiul pe disc. |
| VS Code tot cere să redeschizi            | Probabil ai ambele opțiuni active; alege una (venv **sau** container)|
| Erori OpenAI 401 / 429                    | Verifică valoarea `OPENAI_API_KEY` / limitele de cereri.        |
| Erori cu Conda                            | Instalează librăriile Microsoft AI cu `conda install -c microsoft azure-ai-ml`|

---

**Declarație de responsabilitate**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm răspunderea pentru eventuale neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.