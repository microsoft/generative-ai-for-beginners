<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-17T22:06:37+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ro"
}
-->
# Începem acest curs

Suntem foarte entuziasmați să începeți acest curs și să vedem ce vă inspiră să creați cu ajutorul Inteligenței Artificiale Generative!

Pentru a vă asigura succesul, această pagină prezintă pașii de configurare, cerințele tehnice și unde puteți găsi ajutor, dacă este necesar.

## Pași de configurare

Pentru a începe acest curs, va trebui să finalizați următorii pași.

### 1. Faceți un fork al acestui depozit

[Faceți un fork al întregului depozit](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) în contul dvs. GitHub pentru a putea modifica orice cod și a finaliza provocările. De asemenea, puteți [adăuga o stea (🌟) acestui depozit](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) pentru a-l găsi mai ușor, împreună cu alte depozite conexe.

### 2. Creați un Codespace

Pentru a evita orice probleme de dependență atunci când rulați codul, vă recomandăm să urmați acest curs într-un [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

În fork-ul dvs.: **Code -> Codespaces -> New on main**

![Dialog care arată butoanele pentru a crea un codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Adăugați un secret

1. ⚙️ Pictograma roată -> Command Palette -> Codespaces : Manage user secret -> Add a new secret.  
2. Denumiți-l OPENAI_API_KEY, lipiți cheia dvs., Salvați.

### 3. Ce urmează?

| Vreau să…           | Mergi la…                                                               |
|---------------------|-------------------------------------------------------------------------|
| Încep Lecția 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Lucrez offline      | [`setup-local.md`](02-setup-local.md)                                   |
| Configurez un furnizor LLM | [`providers.md`](03-providers.md)                                        |
| Cunosc alți cursanți | [Alăturați-vă pe Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Depanare

| Simptom                                   | Soluție                                                          |
|-------------------------------------------|------------------------------------------------------------------|
| Construcția containerului durează > 10 min| **Codespaces ➜ “Rebuild Container”**                             |
| `python: command not found`               | Terminalul nu s-a conectat; faceți clic pe **+** ➜ *bash*        |
| `401 Unauthorized` de la OpenAI           | Cheie `OPENAI_API_KEY` greșită / expirată                        |
| VS Code afișează “Dev container mounting…”| Reîmprospătați fila browserului—uneori Codespaces pierde conexiunea |
| Kernel-ul notebook-ului lipsește          | Meniul Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Sisteme bazate pe Unix:

   ```bash
   touch .env
   ```
  
   Windows:

   ```cmd
   echo . > .env
   ```
  
3. **Editați fișierul `.env`**: Deschideți fișierul `.env` într-un editor de text (de exemplu, VS Code, Notepad++ sau alt editor). Adăugați următoarea linie în fișier, înlocuind `your_github_token_here` cu token-ul dvs. GitHub real:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```
  
4. **Salvați fișierul**: Salvați modificările și închideți editorul de text.

5. **Instalați `python-dotenv`**: Dacă nu ați făcut-o deja, va trebui să instalați pachetul `python-dotenv` pentru a încărca variabilele de mediu din fișierul `.env` în aplicația dvs. Python. Puteți să-l instalați folosind `pip`:

   ```bash
   pip install python-dotenv
   ```
  
6. **Încărcați variabilele de mediu în scriptul dvs. Python**: În scriptul dvs. Python, utilizați pachetul `python-dotenv` pentru a încărca variabilele de mediu din fișierul `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```
  
Asta e tot! Ați creat cu succes un fișier `.env`, ați adăugat token-ul GitHub și l-ați încărcat în aplicația dvs. Python.

## Cum să rulați local pe computerul dvs.

Pentru a rula codul local pe computerul dvs., va trebui să aveți instalată o versiune de [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Pentru a utiliza apoi depozitul, trebuie să-l clonați:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```
  
Odată ce ați descărcat totul, puteți începe!

## Pași opționali

### Instalarea Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) este un instalator ușor pentru instalarea [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, precum și câteva pachete.  
Conda în sine este un manager de pachete care facilitează configurarea și comutarea între diferite [**medii virtuale**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python și pachete. Este, de asemenea, util pentru instalarea pachetelor care nu sunt disponibile prin `pip`.

Puteți urma [ghidul de instalare MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) pentru a-l configura.

Cu Miniconda instalat, trebuie să clonați [depozitul](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (dacă nu ați făcut-o deja).

Apoi, trebuie să creați un mediu virtual. Pentru a face acest lucru cu Conda, creați un nou fișier de mediu (_environment.yml_). Dacă urmați cursul folosind Codespaces, creați acest fișier în directorul `.devcontainer`, astfel `.devcontainer/environment.yml`.

Completați fișierul de mediu cu următorul fragment:

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
  
Dacă întâmpinați erori folosind conda, puteți instala manual bibliotecile Microsoft AI utilizând următoarea comandă într-un terminal.

```
conda install -c microsoft azure-ai-ml
```
  
Fișierul de mediu specifică dependențele de care avem nevoie. `<environment-name>` se referă la numele pe care doriți să-l utilizați pentru mediul Conda, iar `<python-version>` este versiunea de Python pe care doriți să o utilizați, de exemplu, `3` este cea mai recentă versiune majoră de Python.

După ce ați terminat, puteți crea mediul Conda rulând comenzile de mai jos în linia de comandă/terminal:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```
  
Consultați [ghidul pentru medii Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) dacă întâmpinați probleme.

### Utilizarea Visual Studio Code cu extensia de suport pentru Python

Recomandăm utilizarea editorului [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) cu extensia de suport pentru [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalată pentru acest curs. Totuși, aceasta este mai mult o recomandare și nu o cerință obligatorie.

> **Notă**: Deschizând depozitul cursului în VS Code, aveți opțiunea de a configura proiectul într-un container. Acest lucru este posibil datorită directorului [special `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) găsit în cadrul depozitului cursului. Mai multe despre acest subiect mai târziu.

> **Notă**: Odată ce clonați și deschideți directorul în VS Code, acesta vă va sugera automat să instalați o extensie de suport pentru Python.

> **Notă**: Dacă VS Code vă sugerează să redeschideți depozitul într-un container, refuzați această solicitare pentru a utiliza versiunea locală instalată de Python.

### Utilizarea Jupyter în browser

Puteți lucra, de asemenea, la proiect utilizând mediul [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direct în browserul dvs. Atât Jupyter clasic, cât și [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferă un mediu de dezvoltare plăcut, cu funcții precum completarea automată, evidențierea codului etc.

Pentru a porni Jupyter local, accesați terminalul/linia de comandă, navigați la directorul cursului și executați:

```bash
jupyter notebook
```
  
sau

```bash
jupyterhub
```
  
Aceasta va porni o instanță Jupyter, iar URL-ul pentru a o accesa va fi afișat în fereastra liniei de comandă.

Odată ce accesați URL-ul, ar trebui să vedeți structura cursului și să puteți naviga la orice fișier `*.ipynb`. De exemplu, `08-building-search-applications/python/oai-solution.ipynb`.

### Rularea într-un container

O alternativă la configurarea tuturor pe computerul dvs. sau în Codespace este utilizarea unui [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Directorul special `.devcontainer` din cadrul depozitului cursului face posibil ca VS Code să configureze proiectul într-un container. În afara Codespaces, acest lucru va necesita instalarea Docker și, sincer, implică ceva muncă, așa că recomandăm această opțiune doar celor cu experiență în lucrul cu containere.

Una dintre cele mai bune modalități de a vă păstra cheile API în siguranță atunci când utilizați GitHub Codespaces este utilizarea secretelor Codespace. Vă rugăm să urmați [ghidul de gestionare a secretelor Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) pentru a afla mai multe despre acest subiect.

## Lecții și cerințe tehnice

Cursul are 6 lecții de concepte și 6 lecții de codare.

Pentru lecțiile de codare, folosim Azure OpenAI Service. Veți avea nevoie de acces la serviciul Azure OpenAI și de o cheie API pentru a rula acest cod. Puteți aplica pentru acces completând [acest formular](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

În timp ce așteptați procesarea cererii dvs., fiecare lecție de codare include și un fișier `README.md` unde puteți vizualiza codul și rezultatele.

## Utilizarea Azure OpenAI Service pentru prima dată

Dacă este prima dată când lucrați cu serviciul Azure OpenAI, vă rugăm să urmați acest ghid despre cum să [creați și să implementați o resursă Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Utilizarea API-ului OpenAI pentru prima dată

Dacă este prima dată când lucrați cu API-ul OpenAI, vă rugăm să urmați ghidul despre cum să [creați și să utilizați interfața.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Cunoașteți alți cursanți

Am creat canale pe serverul nostru oficial de Discord al comunității AI [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) pentru a cunoaște alți cursanți. Aceasta este o modalitate excelentă de a vă conecta cu alți antreprenori, creatori, studenți și oricine dorește să își îmbunătățească cunoștințele în Inteligența Artificială Generativă.

[![Alăturați-vă canalului de Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Echipa de proiect va fi, de asemenea, prezentă pe acest server Discord pentru a ajuta cursanții.

## Contribuiți

Acest curs este o inițiativă open-source. Dacă observați zone care pot fi îmbunătățite sau probleme, vă rugăm să creați un [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) sau să înregistrați o [problemă pe GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Echipa de proiect va urmări toate contribuțiile. Contribuirea la open source este o modalitate extraordinară de a vă dezvolta cariera în domeniul Inteligenței Artificiale Generative.

Majoritatea contribuțiilor necesită să fiți de acord cu un Acord de Licență pentru Contribuitori (CLA) care declară că aveți dreptul și, de fapt, acordați drepturile de a utiliza contribuția dvs. Pentru detalii, vizitați [site-ul CLA, Acord de Licență pentru Contribuitori](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Important: atunci când traduceți textul din acest depozit, vă rugăm să vă asigurați că nu utilizați traduceri automate. Vom verifica traducerile prin intermediul comunității, așa că vă rugăm să vă oferiți voluntar pentru traduceri doar în limbile în care sunteți competenți.

Când trimiteți un pull request, un bot CLA va determina automat dacă trebuie să furnizați un CLA și va marca PR-ul în mod corespunzător (de exemplu, etichetă, comentariu). Trebuie doar să urmați instrucțiunile furnizate de bot. Va trebui să faceți acest lucru o singură dată pentru toate depozitele care utilizează CLA-ul nostru.

Acest proiect a adoptat [Codul de Conduită Open Source al Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pentru mai multe informații, citiți FAQ-ul Codului de Conduită sau contactați [Email opencode](opencode@microsoft.com) pentru întrebări sau comentarii suplimentare.

## Să începem
Acum că ați finalizat pașii necesari pentru a termina acest curs, să începem prin a obține o [introducere în AI generativă și LLM-uri](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.