<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T19:12:15+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ro"
}
-->
# Începe cu acest curs

Suntem foarte entuziasmați să începi acest curs și să vedem ce te inspiră să construiești cu AI Generativ!

Pentru a te asigura că ai succes, această pagină prezintă pașii de configurare, cerințele tehnice și unde poți găsi ajutor dacă ai nevoie.

## Pași de configurare

Pentru a începe acest curs, va trebui să parcurgi următorii pași.

### 1. Fă un fork la acest repo

[Fă fork la întregul acest repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) în contul tău de GitHub pentru a putea modifica codul și a rezolva provocările. Poți de asemenea să [acordezi o stea (🌟) acestui repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ca să-l găsești mai ușor, împreună cu alte repo-uri similare.

### 2. Creează un codespace

Pentru a evita problemele de dependențe când rulezi codul, îți recomandăm să urmezi acest curs într-un [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

În fork-ul tău: **Code -> Codespaces -> New on main**

![Dialog care arată butoanele pentru a crea un codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Adaugă un secret

1. ⚙️ Pictograma gear -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Denumește OPENAI_API_KEY, lipește cheia ta, Salvează.

### 3.  Ce urmează?

| Vreau să…           | Mergi la…                                                                |
|---------------------|--------------------------------------------------------------------------|
| Începe Lecția 1     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| Lucrează offline    | [`setup-local.md`](02-setup-local.md)                                    |
| Configurează un furnizor LLM | [`providers.md`](providers.md)                                  |
| Cunoaște alți cursanți | [Alătură-te pe Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Ghid de depanare


| Simptom                                   | Soluție                                                          |
|-------------------------------------------|------------------------------------------------------------------|
| Container build blocat > 10 min           | **Codespaces ➜ “Rebuild Container”**                             |
| `python: command not found`               | Terminalul nu s-a atașat; apasă pe **+** ➜ *bash*                |
| `401 Unauthorized` de la OpenAI           | `OPENAI_API_KEY` greșit / expirat                                |
| VS Code afișează “Dev container mounting…”| Reîncarcă tab-ul din browser—Codespaces uneori pierde conexiunea |
| Kernel notebook lipsă                     | Meniu Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Sisteme bazate pe Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Editează fișierul `.env`**: Deschide fișierul `.env` într-un editor de text (de exemplu, VS Code, Notepad++ sau orice alt editor). Adaugă următoarea linie în fișier, înlocuind `your_github_token_here` cu token-ul tău GitHub real:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Salvează fișierul**: Salvează modificările și închide editorul de text.

5. **Instalează `python-dotenv`**: Dacă nu ai făcut-o deja, va trebui să instalezi pachetul `python-dotenv` pentru a încărca variabilele de mediu din fișierul `.env` în aplicația ta Python. Îl poți instala folosind `pip`:

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

Gata! Ai creat cu succes un fișier `.env`, ai adăugat token-ul tău GitHub și l-ai încărcat în aplicația ta Python.

## Cum rulezi local pe calculatorul tău

Pentru a rula codul local pe calculatorul tău, trebuie să ai instalată o versiune de [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Pentru a folosi apoi repository-ul, trebuie să-l clonezi:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

După ce ai totul descărcat, poți începe!

## Pași opționali

### Instalarea Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) este un instalator ușor pentru [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python și câteva pachete.
Conda este un manager de pachete care face ușoară configurarea și comutarea între diferite [**medii virtuale**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python și pachete. Este util și pentru instalarea pachetelor care nu sunt disponibile prin `pip`.

Poți urma [ghidul de instalare MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) pentru a-l configura.

După ce ai instalat Miniconda, trebuie să clonezi [repository-ul](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (dacă nu ai făcut-o deja)

Apoi, trebuie să creezi un mediu virtual. Pentru a face asta cu Conda, creează un nou fișier de mediu (_environment.yml_). Dacă urmezi pașii folosind Codespaces, creează acest fișier în directorul `.devcontainer`, deci `.devcontainer/environment.yml`.

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

Dacă întâmpini erori folosind conda, poți instala manual bibliotecile Microsoft AI folosind următoarea comandă în terminal.

```
conda install -c microsoft azure-ai-ml
```

Fișierul de mediu specifică dependențele de care avem nevoie. `<environment-name>` se referă la numele pe care vrei să-l folosești pentru mediul tău Conda, iar `<python-version>` este versiunea de Python pe care vrei să o folosești, de exemplu, `3` este cea mai recentă versiune majoră de Python.

După ce ai făcut asta, poți crea mediul Conda rulând comenzile de mai jos în linia de comandă/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Consultă [ghidul pentru medii Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) dacă întâmpini probleme.

### Folosirea Visual Studio Code cu extensia de suport Python

Îți recomandăm să folosești editorul [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) cu [extensia de suport Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalată pentru acest curs. Totuși, aceasta este doar o recomandare, nu o cerință obligatorie.

> **Note**: Dacă deschizi repository-ul cursului în VS Code, ai opțiunea să configurezi proiectul într-un container. Acest lucru este posibil datorită directorului [special `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) din repository. Vom reveni la acest subiect mai târziu.

> **Note**: După ce clonezi și deschizi directorul în VS Code, acesta îți va sugera automat să instalezi extensia de suport Python.

> **Note**: Dacă VS Code îți sugerează să redeschizi repository-ul într-un container, refuză această solicitare pentru a folosi versiunea de Python instalată local.

### Folosirea Jupyter în browser

Poți lucra la proiect și folosind [mediul Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direct în browser. Atât Jupyter clasic, cât și [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferă un mediu de dezvoltare plăcut, cu funcții precum completare automată, evidențiere a codului etc.

Pentru a porni Jupyter local, deschide terminalul/linia de comandă, navighează la directorul cursului și execută:

```bash
jupyter notebook
```

sau

```bash
jupyterhub
```

Aceasta va porni o instanță Jupyter, iar URL-ul de acces va fi afișat în fereastra terminalului.

După ce accesezi URL-ul, ar trebui să vezi structura cursului și să poți naviga la orice fișier `*.ipynb`. De exemplu, `08-building-search-applications/python/oai-solution.ipynb`.

### Rularea într-un container

O alternativă la configurarea pe calculatorul tău sau în Codespace este să folosești un [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Directorul special `.devcontainer` din repository-ul cursului permite ca VS Code să configureze proiectul într-un container. În afara Codespaces, acest lucru necesită instalarea Docker și, sincer, implică ceva muncă, așa că recomandăm această opțiune doar celor cu experiență în lucru cu containere.

Una dintre cele mai bune metode de a-ți păstra cheile API în siguranță când folosești GitHub Codespaces este să folosești Codespace Secrets. Urmează [ghidul de gestionare a secretelor Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) pentru a afla mai multe.

## Lecții și cerințe tehnice

Cursul are 6 lecții de concepte și 6 lecții de programare.

Pentru lecțiile de programare, folosim Azure OpenAI Service. Vei avea nevoie de acces la serviciul Azure OpenAI și de o cheie API pentru a rula acest cod. Poți solicita acces [completând această cerere](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Cât timp aștepți procesarea cererii, fiecare lecție de programare include și un fișier `README.md` unde poți vedea codul și rezultatele.

## Folosirea Azure OpenAI Service pentru prima dată

Dacă este prima dată când lucrezi cu serviciul Azure OpenAI, urmează acest ghid despre [cum să creezi și să implementezi o resursă Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Folosirea OpenAI API pentru prima dată

Dacă este prima dată când folosești OpenAI API, urmează ghidul despre [cum să creezi și să folosești interfața.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Cunoaște alți cursanți

Am creat canale pe [serverul nostru oficial AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) pentru a cunoaște alți cursanți. Este o modalitate excelentă de a face networking cu alți antreprenori, dezvoltatori, studenți și oricine vrea să avanseze în AI Generativ.

[![Alătură-te canalului discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Echipa de proiect va fi prezentă și pe acest server Discord pentru a ajuta cursanții.

## Contribuie

Acest curs este o inițiativă open-source. Dacă vezi zone care pot fi îmbunătățite sau probleme, te rugăm să creezi un [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) sau să raportezi o [problemă pe GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Echipa de proiect va urmări toate contribuțiile. A contribui la open source este o modalitate excelentă de a-ți construi cariera în AI Generativ.

Majoritatea contribuțiilor necesită să fii de acord cu un Contributor License Agreement (CLA) care declară că ai dreptul și chiar acorzi drepturile de a folosi contribuția ta. Pentru detalii, vizitează [site-ul CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Important: când traduci text în acest repo, te rugăm să te asiguri că nu folosești traducere automată. Vom verifica traducerile prin comunitate, așa că te rugăm să te oferi voluntar doar pentru limbile în care ești fluent.

Când trimiți un pull request, un CLA-bot va determina automat dacă trebuie să furnizezi un CLA și va marca PR-ul corespunzător (de exemplu, etichetă, comentariu). Urmează pur și simplu instrucțiunile oferite de bot. Va trebui să faci acest lucru o singură dată pentru toate repository-urile care folosesc CLA-ul nostru.

Acest proiect a adoptat [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pentru mai multe informații, citește FAQ-ul Codului de Conduită sau contactează [Email opencode](opencode@microsoft.com) pentru întrebări sau comentarii suplimentare.

## Hai să începem
Acum că ai parcurs pașii necesari pentru a finaliza acest curs, hai să începem cu o [introducere în Generative AI și LLM-uri](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Declarație de responsabilitate**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm răspunderea pentru orice neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.