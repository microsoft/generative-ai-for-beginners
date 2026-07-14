# Configurare locală 🖥️

**Folosește acest ghid dacă preferi să rulezi totul pe propriul laptop.**   
Ai două opțiuni: **(A) Python nativ + virtual-env** sau **(B) Container VS Code Dev cu Docker**.  
Alege ce ți se pare mai ușor—ambele duc la aceleași lecții.

## 1.  Cerințe preliminare

| Unealtă            | Versiune / Observații                                                              |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (descarcă de la <https://python.org>)                                        |
| **Git**            | Ultima versiune (vine cu Xcode / Git pentru Windows / manager pachete Linux)         |
| **VS Code**        | Opcțional, dar recomandat <https://code.visualstudio.com>                           |
| **Docker Desktop** | *Doar* pentru Opțiunea B. Instalare gratuită: <https://docs.docker.com/desktop/>    |

> 💡 **Sfat** – Verifică uneltele în terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Opțiunea A – Python nativ (cel mai rapid)

### Pasul 1  Clonează acest repository

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

Sari la Secțiunea 3 despre [Cheile API](#3-adaugă-cheile-api)

## 2. Opțiunea B – Container VS Code Dev (Docker)

Am configurat acest repository și curs cu un [container de dezvoltare](https://containers.dev?WT.mc_id=academic-105485-koreyst) care are un runtime universal ce poate susține dezvoltare Python3, .NET, Node.js și Java. Configurația aferentă este definită în fișierul `devcontainer.json`, localizat în folderul `.devcontainer/` din rădăcina acestui repository.

>**De ce să alegi asta?**
>Mediu identic cu Codespaces; fără derapaje de dependențe.

### Pasul 0 Instalează suplimentele

Docker Desktop – confirmă că ```docker --version``` funcționează.
Extensia VS Code Remote – Containers (ID: ms-vscode-remote.remote-containers).

### Pasul 1 Deschide repository-ul în VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code detectează `.devcontainer/` și afișează un prompt.

### Pasul 2 Redeschide în container

Apasă “Reopen in Container”. Docker construiește imaginea (≈ 3 min prima dată).
Când apare promptul în terminal, ești în container.

## 2.  Opțiunea C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) este un instalator ușor pentru instalarea [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python și câteva pachete.
Conda este un manager de pachete, care face ușoară configurarea și schimbarea între diferite [medii virtuale](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) și pachete Python. Este util și pentru instalarea pachetelor care nu sunt disponibile prin `pip`.

### Pasul 0  Instalează Miniconda

Urmează [ghidul de instalare MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) pentru a-l configura.

```bash
conda --version
```

### Pasul 1 Creează un mediu virtual

Creează un fișier nou pentru mediu (*environment.yml*). Dacă folosești Codespaces, crează-l în directorul `.devcontainer`, adică `.devcontainer/environment.yml`.

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

### Pasul 3 Creează-ți mediul Conda

Rulează comenzile de mai jos în linia de comandă/terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Sub-calea .devcontainer se aplică doar pentru configurațiile Codespace
conda activate ai4beg
```

Consultă [ghidul pentru mediile Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) dacă întâmpini probleme.

## 2  Opțiunea D – Jupyter clasic / Jupyter Lab (în browser)

> **Pentru cine este?**  
> Pentru oricine iubește interfața clasică Jupyter sau vrea să ruleze notebook-uri fără VS Code.  

### Pasul 1  Asigură-te că Jupyter este instalat

Pentru a porni Jupyter local, deschide terminalul/linia de comandă, navighează în directorul cursului și execută:

```bash
jupyter notebook
```

sau

```bash
jupyterhub
```

Aceasta va porni o instanță Jupyter și URL-ul pentru accesare va fi afișat în fereastra terminalului.

Odată ce accesezi URL-ul, ar trebui să vezi planul cursului și să poți naviga către orice fișier `*.ipynb`. De exemplu, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Adaugă Cheile API

Păstrarea cheilor API în siguranță este importantă atunci când construiești orice tip de aplicație. Recomandăm să nu stochezi niciodată chei API direct în cod. Comițând aceste detalii într-un repository public poate duce la probleme de securitate și chiar costuri nedorite dacă sunt folosite de o persoană rău intenționată.
Iată un ghid pas cu pas pentru a crea un fișier `.env` pentru Python și a adăuga acreditările tale Microsoft Foundry Models:

> **Notă:** Modelele GitHub (și variabila `GITHUB_TOKEN`) se vor retrage la sfârșitul lunii iulie 2026. Acest ghid folosește [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) în schimb. Preferi să lucrezi complet offline? Vezi [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Navighează la Directorul Proiectului**: Deschide terminalul sau command prompt și navighează în directorul rădăcină al proiectului unde vrei să creezi fișierul `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Creează fișierul `.env`**: Folosește editorul tău preferat pentru a crea un fișier nou numit `.env`. Dacă folosești linia de comandă, poți folosi `touch` (pe sisteme Unix) sau `echo` (pe Windows):

   Pe sisteme Unix:

   ```bash
   touch .env
   ```

   Pe Windows:

   ```cmd
   echo . > .env
   ```

3. **Editează fișierul `.env`**: Deschide fișierul `.env` într-un editor de text (de exemplu, VS Code, Notepad++, sau alt editor). Adaugă următoarele linii în fișier, înlocuind valorile cu endpoint-ul și cheia API reale Microsoft Foundry ale proiectului tău:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Salvează fișierul**: Salvează modificările și închide editorul de text.

5. **Instalează `python-dotenv`**: Dacă nu ai făcut-o deja, trebuie să instalezi pachetul `python-dotenv` pentru a încărca variabilele de mediu din fișierul `.env` în aplicația ta Python. Poți instala folosind `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Încarcă variabilele de mediu în scriptul Python**: În scriptul tău Python, folosește pachetul `python-dotenv` pentru a încărca variabilele de mediu din fișierul `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Încarcă variabilele de mediu din fișierul .env
   load_dotenv()

   # Accesează variabilele Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Gata! Ai creat cu succes un fișier `.env`, ai adăugat acreditările Microsoft Foundry Models și le-ai încărcat în aplicația ta Python.

🔐 Nu comite niciodată `.env`—este deja în `.gitignore`.
Instrucțiunile complete ale furnizorului sunt în [`providers.md`](03-providers.md).

## 4. Ce urmează?

| Vreau să…          | Merg la…                                                               |
|---------------------|-------------------------------------------------------------------------|
| Încep Lecția 1     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Configurare Furnizor LLM | [`providers.md`](03-providers.md)                                       |
| Cunoaște alți cursanți | [Alătură-te Discord-ului nostru](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Depanare

| Simptom                                  | Soluție                                                          |
|------------------------------------------|-----------------------------------------------------------------|
| `python not found`                       | Adaugă Python în PATH sau redeschide terminalul după instalare  |
| `pip` nu poate construi roți (Windows) | `pip install --upgrade pip setuptools wheel` apoi încearcă din nou.|
| `ModuleNotFoundError: dotenv`            | Rulează `pip install -r requirements.txt` (mediul nu a fost instalat).|
| Docker build eșuează *No space left*   | Docker Desktop ▸ *Settings* ▸ *Resources* → mărește spațiul disk.|
| VS Code tot cere să redeschizi           | S-ar putea să ai active ambele Opțiuni; alege doar una (venv **sau** container)|
| Erori OpenAI 401 / 429                   | Verifică valoarea `OPENAI_API_KEY` / limitele de rată a cererilor.|
| Erori folosind Conda                     | Instalează librăriile Microsoft AI folosind `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->