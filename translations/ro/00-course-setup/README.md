<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:59:33+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ro"
}
-->
# Începerea acestui curs

Suntem foarte entuziasmați că începi acest curs și suntem curioși să vedem ce te inspiră să creezi cu AI Generativ!

Pentru a-ți asigura succesul, această pagină detaliază pașii de configurare, cerințele tehnice și unde să obții ajutor, dacă este necesar.

## Pași de Configurare

Pentru a începe acest curs, va trebui să completezi următorii pași.

### 1. Fork acest Repo

[Fork întregul repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) în contul tău de GitHub pentru a putea modifica orice cod și a completa provocările. Poți de asemenea să [acordezi o stea (🌟) acestui repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) pentru a-l găsi mai ușor și pentru a descoperi repo-uri similare.

### 2. Creează un Codespace

Pentru a evita problemele de dependență atunci când rulezi codul, îți recomandăm să rulezi acest curs într-un [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Acesta poate fi creat selectând opțiunea `Code` pe versiunea forked a acestui repo și selectând opțiunea **Codespaces**.

![Dialog care arată butoanele pentru a crea un codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Stocarea Cheilor API

Este important să-ți păstrezi cheile API în siguranță atunci când construiești orice tip de aplicație. Îți recomandăm să nu stochezi cheile API direct în codul tău. Angajarea acestor detalii într-un depozit public ar putea duce la probleme de securitate și chiar costuri nedorite dacă sunt utilizate de o persoană rău intenționată.
Iată un ghid pas cu pas despre cum să creezi un fișier `.env` pentru Python și să adaugi `GITHUB_TOKEN`:

1. **Navighează la Directorul Proiectului Tău**: Deschide terminalul sau linia de comandă și navighează la directorul rădăcină al proiectului tău unde dorești să creezi fișierul `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Creează Fișierul `.env`**: Folosește editorul de text preferat pentru a crea un fișier nou numit `.env`. Dacă folosești linia de comandă, poți folosi `touch` (on Unix-based systems) or `echo` (pe Windows):

   Sisteme bazate pe Unix:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Editează Fișierul `.env`**: Deschide fișierul `.env` într-un editor de text (de exemplu, VS Code, Notepad++ sau orice alt editor). Adaugă următoarea linie în fișier, înlocuind `your_github_token_here` cu tokenul tău GitHub real:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Salvează Fișierul**: Salvează modificările și închide editorul de text.

5. **Instalează pachetul `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` pentru a încărca variabilele de mediu din fișierul `.env` în aplicația ta Python. Poți să-l instalezi folosind `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Încarcă Variabilele de Mediu în Scriptul Tău Python**: În scriptul tău Python, folosește pachetul `python-dotenv` pentru a încărca variabilele de mediu din fișierul `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Asta e tot! Ai creat cu succes un fișier `.env`, ai adăugat tokenul tău GitHub și l-ai încărcat în aplicația ta Python.

## Cum să Rulezi Local pe Calculatorul Tău

Pentru a rula codul local pe calculatorul tău, va trebui să ai instalată o versiune de [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Pentru a folosi apoi depozitul, trebuie să-l clonezi:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Odată ce ai totul verificat, poți începe!

## Pași Opționali

### Instalarea Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) este un instalator ușor pentru instalarea [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, precum și câteva pachete.
Conda în sine este un manager de pachete, care face ușoară configurarea și comutarea între diferite [**medii virtuale**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) și pachete Python. De asemenea, este util pentru instalarea pachetelor care nu sunt disponibile prin `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Mergi mai departe și completează fișierul de mediu cu fragmentul de mai jos:

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

Dacă întâmpini erori folosind conda, poți instala manual Bibliotecile Microsoft AI folosind următoarea comandă într-un terminal.

```
conda install -c microsoft azure-ai-ml
```

Fișierul de mediu specifică dependențele de care avem nevoie. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` este cea mai recentă versiune majoră a Python.

Cu asta făcut, poți merge mai departe și crea mediul tău Conda rulând comenzile de mai jos în linia de comandă/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consultă [ghidul mediilor Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) dacă întâmpini probleme.

### Utilizarea Visual Studio Code cu extensia de suport Python

Îți recomandăm să folosești editorul [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) cu extensia de suport Python [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalată pentru acest curs. Totuși, aceasta este mai mult o recomandare și nu o cerință definitivă.

> **Notă**: Prin deschiderea depozitului cursului în VS Code, ai opțiunea de a configura proiectul într-un container. Acest lucru se datorează directorului [special `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) găsit în cadrul depozitului cursului. Mai multe despre asta mai târziu.

> **Notă**: Odată ce clonezi și deschizi directorul în VS Code, acesta îți va sugera automat să instalezi o extensie de suport pentru Python.

> **Notă**: Dacă VS Code îți sugerează să redeschizi depozitul într-un container, refuză această solicitare pentru a folosi versiunea locală instalată de Python.

### Utilizarea Jupyter în Browser

Poți de asemenea să lucrezi la proiect folosind mediul [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direct în browserul tău. Atât Jupyter clasic, cât și [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferă un mediu de dezvoltare plăcut cu caracteristici precum completarea automată, evidențierea codului etc.

Pentru a porni Jupyter local, mergi la terminal/linia de comandă, navighează la directorul cursului și execută:

```bash
jupyter notebook
```

sau

```bash
jupyterhub
```

Acest lucru va porni o instanță Jupyter și URL-ul pentru a accesa aceasta va fi afișat în fereastra liniei de comandă.

Odată ce accesezi URL-ul, ar trebui să vezi structura cursului și să poți naviga la orice fișier `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` unde poți vizualiza codul și rezultatele.

## Utilizarea Serviciului Azure OpenAI pentru prima dată

Dacă este prima dată când lucrezi cu serviciul Azure OpenAI, te rugăm să urmezi acest ghid despre cum să [creezi și să implementezi o resursă Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Utilizarea API-ului OpenAI pentru prima dată

Dacă este prima dată când lucrezi cu API-ul OpenAI, te rugăm să urmezi ghidul despre cum să [creezi și să utilizezi Interfața.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Întâlnește alți cursanți

Am creat canale pe serverul nostru oficial [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) pentru a întâlni alți cursanți. Aceasta este o modalitate excelentă de a face networking cu alți antreprenori, constructori, studenți și oricine dorește să își îmbunătățească abilitățile în AI Generativ.

[![Alătură-te canalului discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Echipa de proiect va fi de asemenea pe acest server Discord pentru a ajuta orice cursant.

## Contribuie

Acest curs este o inițiativă open-source. Dacă vezi zone de îmbunătățire sau probleme, te rugăm să creezi un [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) sau să înregistrezi o [problemă GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Echipa de proiect va urmări toate contribuțiile. Contribuirea la open source este o modalitate uimitoare de a-ți construi cariera în AI Generativ.

Majoritatea contribuțiilor necesită să fii de acord cu un Acord de Licență a Contribuitorului (CLA) care declară că ai dreptul și efectiv ne acorzi drepturile de a folosi contribuția ta. Pentru detalii, vizitează [CLA, site-ul Acordului de Licență a Contribuitorului](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Important: când traduci text în acest repo, te rugăm să te asiguri că nu folosești traducerea automată. Vom verifica traducerile prin comunitate, așa că te rugăm să te oferi voluntar pentru traduceri doar în limbile în care ești competent.

Când trimiți un pull request, un bot CLA va determina automat dacă trebuie să furnizezi un CLA și va decora PR-ul corespunzător (de exemplu, etichetă, comentariu). Urmează pur și simplu instrucțiunile furnizate de bot. Va trebui să faci asta doar o dată pentru toate depozitele care folosesc CLA-ul nostru.

Acest proiect a adoptat [Codul de Conduită Open Source al Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pentru mai multe informații, citește FAQ-ul Codului de Conduită sau contactează [Email opencode](opencode@microsoft.com) pentru orice întrebări sau comentarii suplimentare.

## Să Începem

Acum că ai completat pașii necesari pentru a finaliza acest curs, să începem prin a obține o [introducere în AI Generativ și LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională umană. Nu suntem responsabili pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.