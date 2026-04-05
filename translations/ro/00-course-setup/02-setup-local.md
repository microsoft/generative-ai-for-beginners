# Configurare locală 🖥️

**Folosește acest ghid dacă preferi să rulezi totul pe propriul laptop.**  
Ai două opțiuni: **(A) Python nativ + virtual-env** sau **(B) VS Code Dev Container cu Docker**.  
Alege ce ți se pare mai ușor—ambele duc la aceleași lecții.

## 1.  Cerințe preliminare

| Unealtă            | Versiune / Note                                                                      |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (descarcă de la <https://python.org>)                                         |
| **Git**            | Ultima versiune (vine cu Xcode / Git pentru Windows / manager de pachete Linux)       |
| **VS Code**        | Opțional, dar recomandat <https://code.visualstudio.com>                             |
| **Docker Desktop** | *Doar* pentru Opțiunea B. Instalare gratuită: <https://docs.docker.com/desktop/>     |

> 💡 **Sfat** – Verifică uneltele în terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Opțiunea A – Python nativ (cea mai rapidă)

### Pasul 1  Clonează acest repo

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Pasul 2 Creează și activează un mediu virtual

```bash
python -m venv .venv          # fă unul
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Promptul ar trebui acum să înceapă cu (.venv)—asta înseamnă că ești în mediul virtual.

### Pasul 3 Instalează dependențele

```bash
pip install -r requirements.txt
```

Sari la Secțiunea 3 despre [Cheile API](../../../00-course-setup)

## 2. Opțiunea B – VS Code Dev Container (Docker)

Am configurat acest repository și curs cu un [container de dezvoltare](https://containers.dev?WT.mc_id=academic-105485-koreyst) care are un runtime universal ce poate suporta dezvoltare Python3, .NET, Node.js și Java. Configurația aferentă este definită în fișierul `devcontainer.json` aflat în folderul `.devcontainer/` din rădăcina acestui repository.

>**De ce să alegi asta?**  
>Mediu identic cu Codespaces; fără derapaje de dependențe.

### Pasul 0 Instalează elementele suplimentare

Docker Desktop – confirmă că ```docker --version``` funcționează.  
Extensia VS Code Remote – Containers (ID: ms-vscode-remote.remote-containers).

### Pasul 1 Deschide repo-ul în VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code detectează .devcontainer/ și afișează un prompt.

### Pasul 2 Redeschide în container

Click pe „Reopen in Container”. Docker construiește imaginea (≈ 3 min prima dată).  
Când apare promptul terminalului, ești în container.

## 2.  Opțiunea C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) este un instalator ușor pentru instalarea [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, precum și câteva pachete.  
Conda este un manager de pachete, care face ușoară configurarea și comutarea între diferite [**medii virtuale**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python și pachete. Este util și pentru instalarea pachetelor care nu sunt disponibile prin `pip`.

### Pasul 0  Instalează Miniconda

Urmează [ghidul de instalare MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) pentru configurare.

```bash
conda --version
```

### Pasul 1 Creează un mediu virtual

Creează un fișier nou de mediu (*environment.yml*). Dacă folosești Codespaces, creează-l în directorul `.devcontainer`, adică `.devcontainer/environment.yml`.

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
conda env create --name ai4beg --file .devcontainer/environment.yml # Subcalea .devcontainer se aplică doar configurațiilor Codespace
conda activate ai4beg
```

Consultă [ghidul mediilor Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) dacă întâmpini probleme.

## 2  Opțiunea D – Jupyter clasic / Jupyter Lab (în browser)

> **Pentru cine este?**  
> Oricine iubește interfața clasică Jupyter sau vrea să ruleze notebook-uri fără VS Code.  

### Pasul 1  Asigură-te că Jupyter este instalat

Pentru a porni Jupyter local, deschide terminalul/linia de comandă, navighează la directorul cursului și execută:

```bash
jupyter notebook
```

sau

```bash
jupyterhub
```

Aceasta va porni o instanță Jupyter și URL-ul pentru acces va fi afișat în fereastra liniei de comandă.

Odată ce accesezi URL-ul, ar trebui să vezi structura cursului și să poți naviga la orice fișier `*.ipynb`. De exemplu, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Adaugă-ți Cheile API

Păstrarea cheilor API în siguranță este importantă când construiești orice tip de aplicație. Recomandăm să nu stochezi cheile API direct în cod. Comitearea acestor detalii într-un repository public poate cauza probleme de securitate și chiar costuri nedorite dacă sunt folosite de o persoană rău intenționată.  
Iată un ghid pas cu pas pentru a crea un fișier `.env` pentru Python și a adăuga `GITHUB_TOKEN`:

1. **Navighează la directorul proiectului tău**: Deschide terminalul sau linia de comandă și navighează la directorul rădăcină al proiectului unde vrei să creezi fișierul `.env`.

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

3. **Editează fișierul `.env`**: Deschide fișierul `.env` într-un editor de text (ex. VS Code, Notepad++, sau alt editor). Adaugă următoarea linie în fișier, înlocuind `your_github_token_here` cu token-ul tău GitHub real:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Salvează fișierul**: Salvează modificările și închide editorul de text.

5. **Instalează `python-dotenv`**: Dacă nu ai făcut-o deja, trebuie să instalezi pachetul `python-dotenv` pentru a încărca variabilele de mediu din fișierul `.env` în aplicația ta Python. Poți instala cu `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Încarcă variabilele de mediu în scriptul tău Python**: În scriptul Python, folosește pachetul `python-dotenv` pentru a încărca variabilele de mediu din fișierul `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Încarcă variabilele de mediu din fișierul .env
   load_dotenv()

   # Accesează variabila GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Gata! Ai creat cu succes un fișier `.env`, ai adăugat token-ul GitHub și l-ai încărcat în aplicația ta Python.

🔐 Nu comita niciodată .env—este deja în .gitignore.  
Instrucțiuni complete pentru furnizori sunt în [`providers.md`](03-providers.md).

## 4. Ce urmează?

| Vreau să…          | Merg la…                                                               |
|--------------------|------------------------------------------------------------------------|
| Încep Lecția 1     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Configurez un furnizor LLM | [`providers.md`](03-providers.md)                                  |
| Întâlnesc alți cursanți | [Alătură-te Discord-ului nostru](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Depanare

| Simptom                                   | Soluție                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Adaugă Python în PATH sau redeschide terminalul după instalare  |
| `pip` nu poate construi wheels (Windows) | `pip install --upgrade pip setuptools wheel` apoi încearcă din nou. |
| `ModuleNotFoundError: dotenv`             | Rulează `pip install -r requirements.txt` (mediul nu a fost instalat). |
| Docker build eșuează *No space left*      | Docker Desktop ▸ *Settings* ▸ *Resources* → mărește spațiul pe disc. |
| VS Code tot cere să redeschizi             | Poate ai ambele opțiuni active; alege una (venv **sau** container) |
| Erori OpenAI 401 / 429                     | Verifică valoarea `OPENAI_API_KEY` / limitele de rată ale cererilor. |
| Erori folosind Conda                      | Instalează librăriile Microsoft AI cu `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->