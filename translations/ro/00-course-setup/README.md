<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:16:58+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ro"
}
-->
# Începutul acestui curs

Suntem foarte entuziasmați să începi acest curs și să vezi ce te inspiră să construiești cu Generative AI!

Pentru a-ți asigura succesul, această pagină prezintă pașii de configurare, cerințele tehnice și unde poți găsi ajutor dacă ai nevoie.

## Pașii de configurare

Pentru a începe să urmezi acest curs, va trebui să parcurgi următorii pași.

### 1. Fă un fork la acest repo

[Fă un fork la întregul repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) în contul tău de GitHub pentru a putea modifica codul și a finaliza provocările. De asemenea, poți [da star (🌟) acestui repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) pentru a-l găsi mai ușor pe el și pe cele conexe.

### 2. Creează un codespace

Pentru a evita problemele legate de dependențe când rulezi codul, recomandăm să folosești [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Acesta poate fi creat selectând opțiunea `Code` pe versiunea ta fork-uită a repo-ului și apoi alegând opțiunea **Codespaces**.

![Dialog care arată butoanele pentru crearea unui codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Stocarea cheilor tale API

Este important să păstrezi cheile API în siguranță atunci când construiești orice tip de aplicație. Recomandăm să nu stochezi cheile API direct în codul tău. Comitearea acestor detalii într-un repo public poate duce la probleme de securitate și chiar costuri nedorite dacă sunt folosite de persoane rău intenționate.  
Iată un ghid pas cu pas despre cum să creezi un fișier `.env` pentru Python și să adaugi `GITHUB_TOKEN`:

1. **Navighează în directorul proiectului tău**: Deschide terminalul sau linia de comandă și mergi în directorul rădăcină al proiectului unde vrei să creezi fișierul `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Creează fișierul `.env`**: Folosește editorul tău preferat pentru a crea un fișier nou numit `.env`. Dacă folosești linia de comandă, poți folosi `touch` (pe sisteme Unix) sau `echo` (pe Windows):

   Sisteme Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Editează fișierul `.env`**: Deschide fișierul `.env` într-un editor de text (de exemplu, VS Code, Notepad++ sau alt editor). Adaugă următoarea linie în fișier, înlocuind `your_github_token_here` cu token-ul tău GitHub real:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Salvează fișierul**: Salvează modificările și închide editorul de text.

5. **Instalează `python-dotenv`**: Dacă nu ai făcut-o deja, trebuie să instalezi pachetul `python-dotenv` pentru a încărca variabilele de mediu din fișierul `.env` în aplicația ta Python. Poți să-l instalezi folosind `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Încarcă variabilele de mediu în scriptul tău Python**: În scriptul tău Python, folosește pachetul `python-dotenv` pentru a încărca variabilele de mediu din fișierul `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Cam asta e! Ai creat cu succes un fișier `.env`, ai adăugat token-ul GitHub și l-ai încărcat în aplicația ta Python.

## Cum să rulezi local pe calculatorul tău

Pentru a rula codul local pe calculator, trebuie să ai instalată o versiune de [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Pentru a folosi apoi repository-ul, trebuie să-l clonezi:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

După ce ai totul pregătit, poți începe!

## Pași opționali

### Instalarea Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) este un instalator ușor pentru instalarea [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, precum și câteva pachete.  
Conda este un manager de pachete care facilitează configurarea și comutarea între diferite [**medii virtuale**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python și pachete. Este util și pentru instalarea pachetelor care nu sunt disponibile prin `pip`.

Poți urma [ghidul de instalare MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) pentru a-l configura.

După ce ai instalat Miniconda, trebuie să clonezi [repository-ul](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (dacă nu ai făcut-o deja).

Apoi, trebuie să creezi un mediu virtual. Pentru asta, cu Conda, creează un fișier nou de mediu (_environment.yml_). Dacă urmezi pașii folosind Codespaces, creează-l în directorul `.devcontainer`, adică `.devcontainer/environment.yml`.

Completează fișierul de mediu cu fragmentul de mai jos:

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

Dacă întâmpini erori folosind conda, poți instala manual Microsoft AI Libraries folosind comanda următoare în terminal.

```
conda install -c microsoft azure-ai-ml
```

Fișierul de mediu specifică dependențele necesare. `<environment-name>` este numele pe care vrei să-l folosești pentru mediul Conda, iar `<python-version>` este versiunea de Python dorită, de exemplu, `3` pentru cea mai recentă versiune majoră.

După ce ai făcut asta, poți crea mediul Conda rulând comenzile de mai jos în linia de comandă/terminal:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consultă [ghidul pentru mediile Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) dacă întâmpini probleme.

### Folosirea Visual Studio Code cu extensia de suport Python

Recomandăm să folosești editorul [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) cu [extensia de suport Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalată pentru acest curs. Totuși, aceasta este doar o recomandare, nu o cerință obligatorie.

> **Note**: Deschizând repository-ul cursului în VS Code, ai opțiunea să configurezi proiectul într-un container. Acest lucru este posibil datorită directorului special [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) din repository-ul cursului. Vom vorbi mai multe despre asta mai târziu.

> **Note**: După ce clonezi și deschizi directorul în VS Code, acesta îți va sugera automat să instalezi extensia de suport Python.

> **Note**: Dacă VS Code îți sugerează să redeschizi repository-ul într-un container, refuză această cerere pentru a folosi versiunea locală de Python instalată pe calculator.

### Folosirea Jupyter în browser

Poți lucra și în proiect folosind mediul [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direct în browser. Atât Jupyter clasic, cât și [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferă un mediu de dezvoltare plăcut, cu funcții precum completare automată, evidențierea codului etc.

Pentru a porni Jupyter local, deschide terminalul/linia de comandă, navighează în directorul cursului și execută:

```bash
jupyter notebook
```

sau

```bash
jupyterhub
```

Aceasta va porni o instanță Jupyter, iar URL-ul pentru acces va fi afișat în fereastra terminalului.

Odată ce accesezi URL-ul, ar trebui să vezi structura cursului și să poți naviga către orice fișier `*.ipynb`. De exemplu, `08-building-search-applications/python/oai-solution.ipynb`.

### Rularea într-un container

O alternativă la configurarea totul pe calculatorul tău sau în Codespace este să folosești un [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Directorul special `.devcontainer` din repository-ul cursului permite VS Code să configureze proiectul într-un container. În afara Codespaces, acest lucru necesită instalarea Docker și, sincer, implică ceva muncă, așa că recomandăm această variantă doar celor cu experiență în lucrul cu containere.

Una dintre cele mai bune metode de a-ți păstra cheile API în siguranță când folosești GitHub Codespaces este folosirea Codespace Secrets. Te rugăm să urmezi ghidul [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) pentru a afla mai multe.

## Lecții și cerințe tehnice

Cursul are 6 lecții conceptuale și 6 lecții de programare.

Pentru lecțiile de programare, folosim Azure OpenAI Service. Vei avea nevoie de acces la serviciul Azure OpenAI și de o cheie API pentru a rula codul. Poți aplica pentru acces [completând această cerere](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

În timp ce aștepți procesarea cererii, fiecare lecție de programare include și un fișier `README.md` unde poți vedea codul și rezultatele.

## Folosirea Azure OpenAI Service pentru prima dată

Dacă este prima dată când lucrezi cu serviciul Azure OpenAI, te rugăm să urmezi acest ghid despre cum să [creezi și să implementezi o resursă Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Folosirea OpenAI API pentru prima dată

Dacă este prima dată când lucrezi cu OpenAI API, te rugăm să urmezi ghidul despre cum să [creezi și să folosești interfața.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Cunoaște alți cursanți

Am creat canale în serverul nostru oficial [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) pentru a cunoaște alți cursanți. Este o modalitate excelentă de a face networking cu alți antreprenori, dezvoltatori, studenți și oricine dorește să avanseze în Generative AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Echipa proiectului va fi de asemenea prezentă pe acest server Discord pentru a ajuta cursanții.

## Contribuie

Acest curs este o inițiativă open-source. Dacă observi zone care pot fi îmbunătățite sau probleme, te rugăm să creezi un [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) sau să raportezi un [issue pe GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Echipa proiectului va urmări toate contribuțiile. Contribuția la open source este o modalitate excelentă de a-ți dezvolta cariera în Generative AI.

Majoritatea contribuțiilor necesită să fii de acord cu un Acord de Licență pentru Contribuitor (CLA) prin care declari că ai dreptul și efectiv ne acorzi drepturile de a folosi contribuția ta. Pentru detalii, vizitează [site-ul CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Important: când traduci text în acest repo, te rugăm să nu folosești traducere automată. Vom verifica traducerile prin comunitate, așa că te rugăm să te oferi voluntar doar pentru limbile în care ești fluent.

Când trimiți un pull request, un bot CLA va determina automat dacă trebuie să furnizezi un CLA și va marca PR-ul corespunzător (de exemplu, cu etichetă sau comentariu). Urmează pur și simplu instrucțiunile oferite de bot. Va trebui să faci asta o singură dată pentru toate repo-urile care folosesc CLA-ul nostru.

Acest proiect a adoptat [Codul de Conduită Open Source Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pentru mai multe informații, citește FAQ-ul Codului de Conduită sau contactează [Email opencode](opencode@microsoft.com) pentru întrebări sau comentarii suplimentare.

## Să începem

Acum că ai parcurs pașii necesari pentru a urma acest curs, hai să începem cu o [introducere în Generative AI și LLM-uri](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.