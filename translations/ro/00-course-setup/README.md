# Începutul cursului

Suntem foarte entuziasmați că începi acest curs și vrem să vezi ce te inspiră să construiești cu AI Generativ!

Pentru a-ți asigura succesul, această pagină prezintă pașii de configurare, cerințele tehnice și unde poți obține ajutor dacă este necesar.

## Pași pentru configurare

Pentru a începe să urmezi acest curs, trebuie să parcurgi următorii pași.

### 1. Fă fork la acest depozit

[Fă fork la întregul depozit](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) în contul tău GitHub pentru a putea modifica codul și a finaliza provocările. Poți, de asemenea, să [acordă o stea (🌟) acestui depozit](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) pentru a-l găsi mai ușor împreună cu depozitele conexe.

### 2. Creează un codespace

Pentru a evita problemele cu dependențele când rulezi codul, recomandăm să rulezi acest curs într-un [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

În fork-ul tău: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/ro/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Adaugă un secret

1. ⚙️ Pictograma roată dințată -> Command Palette -> Codespaces : Manage user secret -> Add a new secret.
2. Denumește OPENAI_API_KEY, lipește cheia ta, Salvează.

### 3. Ce urmează?

| Vreau să…             | Merg la…                                                                  |
|-----------------------|---------------------------------------------------------------------------|
| Încep Lecția 1        | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)        |
| Lucrez offline        | [`setup-local.md`](02-setup-local.md)                                     |
| Configurez un Furnizor LLM | [`providers.md`](03-providers.md)                                     |
| Întâlnesc alți cursanți | [Alătură-te Discord-ului nostru](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Depanare


| Simptom                                    | Soluție                                                         |
|--------------------------------------------|-----------------------------------------------------------------|
| Construirea containerului blocată > 10 min | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`                  | Terminalul nu s-a atașat; apasă **+** ➜ *bash*                 |
| `401 Unauthorized` de la OpenAI              | `OPENAI_API_KEY` incorectă / expirat                             |
| VS Code afișează “Dev container mounting…”  | Reîncarcă fila browser-ului — uneori Codespaces pierde conexiunea|
| Kernel-ul notebook-ului lipsește             | Meniul notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Sisteme bazate pe Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Editează fișierul `.env`**: Deschide fișierul `.env` într-un editor de text (ex., VS Code, Notepad++ sau alt editor). Adaugă următoarele linii în fișier, înlocuind valorile generice cu endpoint-ul și cheia ta reală pentru Microsoft Foundry Models (consultă [`providers.md`](03-providers.md) pentru cum să obții acestea):

   > **Notă:** Modelele GitHub (și variabila `GITHUB_TOKEN`) vor fi retrase la sfârșitul lunii iulie 2026. Folosește în schimb [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Salvează fișierul**: Salvează modificările și închide editorul de text.

5. **Instalează `python-dotenv`**: Dacă nu ai făcut-o deja, trebuie să instalezi pachetul `python-dotenv` pentru a încărca variabilele de mediu din fișierul `.env` în aplicația ta Python. Poți să-l instalezi folosind `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Încarcă variabilele de mediu în scriptul tău Python**: În scriptul Python, folosește pachetul `python-dotenv` pentru a încărca variabilele de mediu din fișierul `.env`:

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

Asta este! Ai creat cu succes un fișier `.env`, ți-ai adăugat acreditările Microsoft Foundry Models și le-ai încărcat în aplicația ta Python.

## Cum să rulezi local pe calculatorul tău

Pentru a rula codul local pe calculatorul tău, trebuie să ai instalată o versiune de [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Pentru a folosi apoi depozitul, trebuie să-l clonezi:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Odată ce ai totul descărcat, poți începe să lucrezi!

## Pași Opționali

### Instalarea Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) este un instalator ușor pentru instalarea [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, precum și câteva pachete.
Conda este un manager de pachete care facilitează configurarea și schimbarea între diferite [medii virtuale](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python și pachetele aferente. De asemenea, este util pentru instalarea pachetelor care nu sunt disponibile prin `pip`.

Poți urma [ghidul de instalare MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) pentru a-l configura.

După ce ai instalat Miniconda, trebuie să clonezi [depozitul](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (dacă nu ai făcut-o deja)

Următorul pas este să creezi un mediu virtual. Pentru a face asta cu Conda, creează un fișier nou de mediu (_environment.yml_). Dacă urmărești cursul folosind Codespaces, creează acest fișier în directorul `.devcontainer`, adică `.devcontainer/environment.yml`.

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

Dacă întâmpini erori folosind conda, poți instala manual Bibliotecile Microsoft AI folosind comanda următoare într-un terminal.

```
conda install -c microsoft azure-ai-ml
```

Fișierul de mediu specifică dependențele de care avem nevoie. `<environment-name>` este numele pe care vrei să-l folosești pentru mediul tău Conda, iar `<python-version>` este versiunea de Python dorită, de exemplu, `3` este ultima versiune majoră de Python.

După ce ai terminat, poți crea mediul Conda rulând comenzile de mai jos în linia/tastatura de comandă.

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Sub-calea .devcontainer se aplică doar configurărilor Codespace
conda activate ai4beg
```

Consultă [Ghidul mediilor Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) dacă întâmpini probleme.

### Folosirea Visual Studio Code cu extensia de suport Python

Recomandăm folosirea editorului [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) cu extensia de suport [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalată pentru acest curs. Aceasta este însă o recomandare și nu o cerință definitivă.

> **Notă**: Deschizând depozitul cursului în VS Code, ai opțiunea de a configura proiectul într-un container. Acest lucru este posibil datorită directorului special [ `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) găsit în depozitul cursului. Vom detalia mai târziu.

> **Notă**: După ce clonezi și deschizi directorul în VS Code, îți va sugera automat să instalezi o extensie de suport pentru Python.

> **Notă**: Dacă VS Code îți sugerează să redeschizi depozitul într-un container, refuză această solicitare pentru a folosi versiunea Python instalată local.

### Folosirea Jupyter în browser

Poți lucra de asemenea pe proiect folosind mediul [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) chiar în browserul tău. Atât Jupyter clasic, cât și [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferă un mediu de dezvoltare plăcut cu funcționalități precum completare automată, evidențiere de cod etc.

Pentru a porni Jupyter local, deschide terminalul/tastatura de comandă, navighează către directorul cursului și execută:

```bash
jupyter notebook
```

sau

```bash
jupyterhub
```

Aceasta va porni o instanță Jupyter și URL-ul pentru accesarea acesteia va fi afișat în fereastra liniei de comandă.

După ce accesezi URL-ul, ar trebui să vezi structura cursului și să poți naviga la orice fișier `*.ipynb`. De exemplu, `08-building-search-applications/python/oai-solution.ipynb`.

### Rularea într-un container

O alternativă pentru a configura totul pe calculatorul tău sau în Codespace este să folosești un [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Folderul special `.devcontainer` din depozitul cursului face posibil pentru VS Code să configureze proiectul într-un container. În afara Codespaces, acest lucru necesită instalarea Docker și, sincer, implică ceva muncă, așa că recomandăm această opțiune doar celor cu experiență în utilizarea containerelor.

Una dintre cele mai bune metode de a-ți păstra cheile API securizate când folosești GitHub Codespaces este utilizarea Secretelor Codespace. Te rugăm să urmezi ghidul de [gestionare a secretelor în Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) pentru a afla mai multe.


## Lecții și cerințe tehnice

Cursul conține lecții “Learn” care explică conceptele AI Generativ și lecții “Build” cu exemple practice de cod atât în **Python**, cât și în **TypeScript** acolo unde este posibil.

Pentru lecțiile de programare folosim Azure OpenAI în Microsoft Foundry. Vei avea nevoie de un abonament Azure și o cheie API. Accesul este deschis - nu este nevoie de aplicație - așa că poți [crea o resursă Microsoft Foundry și implementa un model](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) pentru a obține endpoint-ul și cheia.

Fiecare lecție de programare include de asemenea un fișier `README.md` unde poți vizualiza codul și rezultatele fără să rulezi ceva.

## Folosirea serviciului Azure OpenAI pentru prima dată

Dacă este prima dată când lucrezi cu serviciul Azure OpenAI, te rugăm să urmezi acest ghid despre cum să [creezi și să implementezi o resursă Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst).

## Folosirea API-ului OpenAI pentru prima dată

Dacă este prima dată când lucrezi cu API-ul OpenAI, te rugăm să urmezi ghidul despre cum să [crezi și să folosești Interfața](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst).

## Întâlnește alți cursanți

Am creat canale pe serverul nostru oficial [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) pentru a întâlni alți cursanți. Aceasta este o modalitate excelentă de a-ți crea rețele cu alți antreprenori, dezvoltatori, studenți și oricine dorește să avanseze în AI Generativ.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Echipa de proiect va fi și ea pe acest server Discord pentru a ajuta cursanții.

## Contribuie

Acest curs este o inițiativă open-source. Dacă observi zone de îmbunătățit sau probleme, te rugăm să creezi un [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) sau un [issue pe GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Echipa de proiect va urmări toate contribuțiile. A contribui la open source este o metodă minunată de a-ți construi o carieră în AI Generativ.

Majoritatea contribuțiilor necesită să fii de acord cu un Acord de Licență pentru Contribuitori (CLA) declarând că ai dreptul și efectiv ne acorzi drepturile de a folosi contribuția ta. Pentru detalii, vizitează [site-ul CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Important: când traduci text în acest depozit, te rugăm să nu folosești traducere automată. Vom verifica traducerile prin comunitate, deci te rugăm să te oferi voluntar doar pentru traduceri în limbi în care te descurci.


Când trimiteți un pull request, un CLA-bot va determina automat dacă trebuie să furnizați un CLA și va decora PR-ul corespunzător (de exemplu, etichetă, comentariu). Urmați pur și simplu instrucțiunile oferite de bot. Va trebui să faceți acest lucru o singură dată pentru toate depozitele care folosesc CLA-ul nostru.

Acest proiect a adoptat [Codul de Conduită pentru Codul Deschis Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pentru mai multe informații, citiți FAQ-ul Codului de Conduită sau contactați [Email opencode](opencode@microsoft.com) pentru orice întrebări sau comentarii suplimentare.

## Să începem

Acum că ați finalizat pașii necesari pentru a parcurge acest curs, să începem cu o [introducere în Generative AI și LLM-uri](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->