# Începutul cursului

Suntem foarte entuziasmați că ai început acest curs și că vei vedea inspirația pentru a crea cu ajutorul AI Generativ!

Pentru a-ți asigura succesul, această pagină delimitează pașii de configurare, cerințele tehnice și unde poți obține ajutor dacă este nevoie.

## Pașii de configurare

Pentru a începe cursul, va trebui să finalizezi următorii pași.

### 1. Fă un fork acestui repo

[Fă un fork al întregului repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) pe contul tău GitHub pentru a putea modifica orice cod și a finaliza provocările. De asemenea, poți [da un star (🌟) acestui repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) pentru a-l găsi mai ușor alături de alte repo-uri similare.

### 2. Creează un codespace

Pentru a evita orice probleme de dependență la rularea codului, recomandăm să rulezi acest curs într-un [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

În fork-ul tău: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/ro/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Adaugă un secret

1. ⚙️ Iconița de roată dințată -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Denumește-l OPENAI_API_KEY, lipește cheia ta, Salvează.

### 3. Ce urmează?

| Vreau să…          | Du-mă la…                                                              |
|---------------------|-------------------------------------------------------------------------|
| Încep Lecția 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| Lucrez offline      | [`setup-local.md`](02-setup-local.md)                                    |
| Configurez un Furnizor LLM | [`providers.md`](03-providers.md)                                     |
| Cunosc alți cursanți | [Alătură-te Discord-ului nostru](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Depanare

| Simptom                                   | Soluție                                                           |
|-------------------------------------------|-----------------------------------------------------------------|
| Construirea containerului blocată > 10 min | **Codespaces ➜ „Rebuild Container”**                            |
| `python: command not found`               | Terminalul nu s-a atașat; apasă **+** ➜ *bash*                   |
| `401 Unauthorized` de la OpenAI           | `OPENAI_API_KEY` greșit sau expirat                              |
| VS Code afișează „Dev container mounting…”  | Reîncarcă fila browser-ului — uneori Codespaces pierde conexiunea |
| Lipsă kernel pentru notebook                | Meniul notebook-ului ➜ **Kernel ▸ Select Kernel ▸ Python 3**    |

   Sistemele bazate pe Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Editează fișierul `.env`**: Deschide fișierul `.env` într-un editor de text (ex: VS Code, Notepad++ sau alt editor). Adaugă următoarea linie în fișier, înlocuind `your_github_token_here` cu token-ul tău GitHub real:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Salvează fișierul**: Salvează modificările și închide editorul de text.

5. **Instalează `python-dotenv`**: Dacă nu ai făcut deja, va trebui să instalezi pachetul `python-dotenv` pentru a încărca variabilele de mediu din fișierul `.env` în aplicația ta Python. Poți instala folosind `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Încarcă variabilele de mediu în scriptul Python**: În scriptul tău Python, folosește pachetul `python-dotenv` pentru a încărca variabilele din fișierul `.env`:

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

## Cum rulezi local pe calculatorul tău

Pentru a rula codul local pe calculator, trebuie să ai instalată o versiune de [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Pentru a folosi apoi depozitul, trebuie să îl clonezi:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

După ce ai totul pregătit, poți începe!

## Pași opționali

### Instalarea Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) este un installer ușor pentru instalarea [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, precum și câteva pachete.
Conda este un manager de pachete care facilitează configurarea și comutarea între diferite [**medii virtuale**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python și pachete. Este util și pentru instalarea pachetelor care nu sunt disponibile prin `pip`.

Poți urma [ghidul de instalare MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) pentru configurare.

După instalarea Miniconda, trebuie să clonezi [depozitul](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (dacă nu ai făcut-o deja)

Apoi trebuie să creezi un mediu virtual. Pentru asta, creează un fișier de mediu (_environment.yml_). Dacă folosești Codespaces, creează fișierul în directorul `.devcontainer`, astfel `.devcontainer/environment.yml`.

Completează fișierul tău de mediu cu fragmentul de mai jos:

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

Dacă primești erori când folosești conda, poți instala manual bibliotecile Microsoft AI folosind comanda următoare în terminal.

```
conda install -c microsoft azure-ai-ml
```

Fișierul de mediu specifică dependențele necesare. `<environment-name>` este numele pe care îl vrei pentru mediul Conda, iar `<python-version>` este versiunea de Python dorită, de exemplu, `3` fiind cea mai recentă versiune majoră.

După aceasta, creează mediul Conda rulând comenzile de mai jos în linia de comandă/terminal:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Subcalea .devcontainer se aplică doar configurărilor Codespace
conda activate ai4beg
```

Consultă [ghidul pentru medii Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) dacă întâmpini probleme.

### Folosirea Visual Studio Code cu extensia pentru Python

Recomandăm să folosești editorul [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) cu [extensia de suport Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalată pentru acest curs. Totuși, aceasta este o recomandare și nu o cerință obligatorie.

> **Notă**: Deschizând repo-ul cursului în VS Code, ai opțiunea să configurezi proiectul într-un container. Acest lucru este posibil datorită directorului special [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) din repo-ul cursului. Mai multe detalii mai târziu.

> **Notă**: După ce clonezi și deschizi directorul în VS Code, îți va sugera automat să instalezi extensia de suport Python.

> **Notă**: Dacă VS Code sugerează să redeschizi repo-ul într-un container, refuză pentru a folosi versiunea locală de Python instalată.

### Folosirea Jupyter în browser

Poți lucra și în proiect folosind mediul [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direct în browser. Atât Jupyter clasic, cât și [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferă un mediu de dezvoltare plăcut cu facilități precum auto-completare, evidențierea codului etc.

Pentru a porni Jupyter local, deschide terminalul/linia de comandă, navighează în directorul cursului și execută:

```bash
jupyter notebook
```

sau

```bash
jupyterhub
```

Aceasta va porni o instanță de Jupyter, iar URL-ul pentru acces va fi afișat în fereastra terminalului.

Odată ce accesezi URL-ul, ar trebui să vezi structura cursului și să poți naviga la orice fișier `*.ipynb`. De exemplu, `08-building-search-applications/python/oai-solution.ipynb`.

### Rularea într-un container

O alternativă la configurarea locală pe calculator sau în Codespace este să folosești un [container](<https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Directorul special `.devcontainer` din repo-ul cursului face posibil ca VS Code să configureze proiectul într-un container. În afara Codespaces, acest lucru necesită instalarea Docker, și sincer, implică ceva muncă, așa că recomandăm acest lucru doar celor cu experiență în lucru cu containere.

Una dintre cele mai sigure metode de a-ți proteja cheile API când folosești GitHub Codespaces este folosirea Codspace Secrets. Urmează ghidul privind [gestionarea secretelor în Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) pentru detalii.

## Lecții și cerințe tehnice

Cursul conține 6 lecții teoretice și 6 lecții de programare.

Pentru lecțiile de programare folosim Azure OpenAI Service. Va trebui să ai acces la Azure OpenAI și o cheie API pentru a rula acest cod. Poți aplica pentru acces completând [această cerere](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

În timp ce aștepți procesarea cererii, fiecare lecție de programare include și un fișier `README.md` unde poți vedea codul și rezultatele.

## Folosirea Azure OpenAI Service pentru prima dată

Dacă este prima dată când lucrezi cu Azure OpenAI service, te rugăm să urmezi acest ghid despre cum să [creezi și să implementezi un serviciu Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Folosirea API-ului OpenAI pentru prima dată

Dacă este prima dată când folosești API-ul OpenAI, urmează ghidul despre cum să [creezi și să folosești interfața.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Cunoaște alți cursanți

Am creat canale în serverul nostru oficial [Discord AI Community](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) pentru a putea cunoaște alți cursanți. Este o modalitate excelentă de a face networking cu alți antreprenori, constructori, studenți și oricine dorește să avanseze în AI Generativ.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Echipa proiectului va fi prezentă și pe acest Discord pentru a ajuta cursanții.

## Contribuie

Acest curs este o inițiativă open-source. Dacă observi zone de îmbunătățire sau probleme, te rugăm să creezi un [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) sau să raportezi un [issue GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Echipa proiectului va urmări toate contribuțiile. Contribuția la open source este o cale excelentă de a-ți construi o carieră în AI Generativ.

Majoritatea contribuțiilor necesită să fii de acord cu un Acord de Licență pentru Contribuitori (CLA) care declară că ai dreptul și efectiv cedezi drepturile noastre să folosim contribuția ta. Detalii găsești pe [site-ul CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Important: când traduci text în acest repo, asigură-te că NU folosești traducere automată. Vom verifica traducerile prin comunitate, așa că te rugăm să oferi traduceri doar în limbi în care ești fluent.

La trimiterea unui pull request, un bot CLA va determina automat dacă trebuie să furnizezi CLA și va marca PR-ul corespunzător (ex: etichetă, comentariu). Urmează instrucțiunile date de bot. Acest pas îl vei face o singură dată, valabil pentru toate repo-urile care folosesc CLA-ul nostru.

Acest proiect a adoptat [Codul de Conduită Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pentru mai multe informații citește FAQ-ul privind Codul de Conduită sau contactează [Email opencode](opencode@microsoft.com) pentru întrebări suplimentare.

## Hai să începem!
Acum că ați finalizat pașii necesari pentru a parcurge acest curs, să începem prin a obține o [introducere în AI Generativ și LLM-uri](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinarea responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un traducător uman. Nu ne asumăm responsabi­litatea pentru eventualele neînțelegeri sau interpretări greșite ce pot apărea în urma utilizării acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->