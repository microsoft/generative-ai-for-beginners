# Începeți cu acest curs

Suntem foarte entuziasmați să începeți acest curs și să vedeți ce veți fi inspirați să creați cu AI Generativ!

Pentru a vă asigura succesul, această pagină prezintă pașii de configurare, cerințele tehnice și unde puteți obține ajutor dacă este necesar.

## Pași de configurare

Pentru a începe acest curs, va trebui să finalizați următorii pași.

### 1. Fork la acest Repo

[Faceți fork la întregul repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) în contul dvs. GitHub pentru a putea modifica orice cod și a finaliza provocările. De asemenea, puteți [star-ui acest repo (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) pentru a-l găsi mai ușor pe el și pe altele similare.

### 2. Creați un codespace

Pentru a evita problemele cu dependențele atunci când rulați codul, recomandăm să rulați acest curs într-un [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

În fork-ul dvs.: **Code -> Codespaces -> New on main**

![Dialog care arată butoanele pentru crearea unui codespace](../../../translated_images/ro/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Adăugați un secret

1. ⚙️ Iconița rotiță -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Numiți OPENAI_API_KEY, lipiți cheia dvs., apăsați Save.

### 3. Ce urmează?

| Vreau să…         | Merg la…                                                                 |
|-------------------|-------------------------------------------------------------------------|
| Încep Lecția 1     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Lucrez offline     | [`setup-local.md`](02-setup-local.md)                                   |
| Configurez un furnizor LLM | [`providers.md`](03-providers.md)                                    |
| Cunosc alți cursanți | [Alăturați-vă Discord-ului nostru](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Rezolvarea problemelor


| Simptom                                   | Remediere                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| Construirea containerului blocată > 10 min| **Codespaces ➜ „Rebuild Container”**                           |
| `python: command not found`                | Terminalul nu s-a atașat; faceți clic pe **+** ➜ *bash*           |
| `401 Unauthorized` de la OpenAI            | `OPENAI_API_KEY` greșit / expirat                                |
| VS Code afișează „Dev container mounting…” | Reîmprospătați fila browserului—Codespaces uneori pierde conexiunea |
| Kernel-ul notebook lipsă                   | Meniul notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Sisteme bazate pe Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Editați fișierul `.env`**: Deschideți fișierul `.env` într-un editor de text (de ex., VS Code, Notepad++ sau orice alt editor). Adăugați următoarele linii în fișier, înlocuind locurile marcate cu puncte cu endpoint-ul și cheia reale pentru Microsoft Foundry Models (vedeți [`providers.md`](03-providers.md) pentru cum să obțineți acestea):

   > **Notă:** GitHub Models (și variabila sa `GITHUB_TOKEN`) se retrage la sfârșitul lunii iulie 2026. Folosiți în schimb [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Salvați fișierul**: Salvați modificările și închideți editorul de text.

5. **Instalați `python-dotenv`**: Dacă nu ați făcut-o deja, va trebui să instalați pachetul `python-dotenv` pentru a încărca variabilele de mediu din fișierul `.env` în aplicația Python. Puteți să-l instalați folosind `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Încărcați variabilele de mediu în scriptul Python**: În scriptul dvs. Python, folosiți pachetul `python-dotenv` pentru a încărca variabilele de mediu din fișierul `.env`:

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

Acesta este tot! Ați creat cu succes un fișier `.env`, ați adăugat acreditările Microsoft Foundry Models și le-ați încărcat în aplicația dvs. Python.

## Cum să rulați local pe calculatorul dvs.

Pentru a rula codul local pe calculatorul dvs., trebuie să aveți instalată o versiune de [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Pentru a folosi apoi depozitul, trebuie să îl clonați:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Când aveți totul verificat, puteți începe!

## Pași opționali

### Instalarea Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) este un instalator ușor pentru instalarea [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, precum și câteva pachete.
Conda însăși este un manager de pachete, care facilitează configurarea și comutarea între diferite [mediile virtuale](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) de Python și pachetele aferente. Este de asemenea utilă pentru instalarea pachetelor care nu sunt disponibile prin `pip`.

Puteți urma ghidul de instalare [MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) pentru a o configura.

Cu Miniconda instalat, trebuie să clonați [repozitoriul](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (dacă nu ați făcut-o deja).

Apoi, trebuie să creați un mediu virtual. Pentru asta, cu Conda, creați un fișier nou de mediu (_environment.yml_). Dacă urmați alături folosind Codespaces, creați acest fișier în directorul `.devcontainer`, deci `.devcontainer/environment.yml`.

Completați fișierul de mediu cu fragmentul de mai jos:

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

Dacă întâmpinați erori folosind conda, puteți instala manual librăriile Microsoft AI folosind următoarea comandă în terminal.

```
conda install -c microsoft azure-ai-ml
```

Fișierul de mediu specifică dependențele de care avem nevoie. `<environment-name>` este numele pe care doriți să-l folosiți pentru mediul Conda, iar `<python-version>` este versiunea Python pe care doriți să o folosiți, de exemplu `3` este cea mai nouă versiune majoră Python.

După acest pas, puteți crea mediul Conda rulând comenzile de mai jos în linia de comandă/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Calea sub .devcontainer se aplică doar configurărilor Codespace
conda activate ai4beg
```

Consultați [ghidul pentru mediile Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) dacă întâmpinați probleme.

### Folosind Visual Studio Code cu extensia de suport Python

Recomandăm utilizarea editorului [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) cu extensia de [suport Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) instalată pentru acest curs. Totuși, aceasta este doar o recomandare și nu o cerință obligatorie.

> **Notă**: Deschizând depozitul cursului în VS Code, aveți opțiunea să configurați proiectul într-un container. Acest lucru este posibil datorită directorului special [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) găsit în depozitul cursului. Mai multe detalii ulterior.

> **Notă**: Odată ce clonați și deschideți directorul în VS Code, acesta vă va sugera automat să instalați o extensie de suport Python.

> **Notă**: Dacă VS Code vă sugerează să redeschideți depozitul într-un container, refuzați această solicitare pentru a folosi versiunea Python instalată local.

### Folosind Jupyter în browser

Puteți lucra și în proiect folosind mediul [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direct în browserul dvs. Atât Jupyter clasic, cât și [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) oferă un mediu de dezvoltare plăcut cu funcții precum completare automată, evidențiere a codului, etc.

Pentru a porni Jupyter local, accesați terminalul/linia de comandă, navigați în directorul cursului și executați:

```bash
jupyter notebook
```

sau

```bash
jupyterhub
```

Aceasta va porni o instanță Jupyter și URL-ul de acces va fi afișat în fereastra liniei de comandă.

Odată ce accesați URL-ul, ar trebui să vedeți structura cursului și să puteți naviga către orice fișier `*.ipynb`. De exemplu, `08-building-search-applications/python/oai-solution.ipynb`.

### Rularea într-un container

O alternativă la configurarea totul pe calculatorul dvs. sau în Codespace este să folosiți un [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Directorul special `.devcontainer` din depozitul cursului face posibil ca VS Code să configureze proiectul într-un container. În afara Codespaces, acest lucru va necesita instalarea Docker, și, sincer, implică ceva muncă, așa că recomandăm această variantă doar celor cu experiență în lucrul cu containere.

Una dintre cele mai bune metode de a păstra cheile API în siguranță când folosiți GitHub Codespaces este prin utilizarea Secretelor din Codespace. Vă rugăm să urmați ghidul [manage secrets for your codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) pentru mai multe informații.


## Lecții și cerințe tehnice

Cursul are 6 lecții conceptuale și 6 lecții de codare.

Pentru lecțiile de codare, folosim Azure OpenAI Service. Veți avea nevoie de acces la serviciul Azure OpenAI și o cheie API pentru a rula acest cod. Puteți solicita accesul completând [această cerere](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

În timp ce așteptați procesarea cererii, fiecare lecție de codare include și un fișier `README.md` unde puteți vedea codul și rezultatele.

## Folosind serviciul Azure OpenAI pentru prima dată

Dacă este prima dată când lucrați cu serviciul Azure OpenAI, vă rugăm să urmați acest ghid despre cum să [creați și să implementați o resursă Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst).

## Folosind API-ul OpenAI pentru prima dată

Dacă este prima dată când lucrați cu API-ul OpenAI, vă rugăm să urmați ghidul despre cum să [creați și să utilizați Interfața](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst).

## Cunoașteți alți cursanți

Am creat canale pe serverul oficial [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) pentru a cunoaște alți cursanți. Aceasta este o modalitate excelentă de a face networking cu alți antreprenori, dezvoltatori, studenți și oricine dorește să avanseze în AI Generativ.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Echipa proiectului va fi de asemenea pe acest server Discord pentru a ajuta cursanții.

## Contribuiți

Acest curs este o inițiativă open-source. Dacă observați zone de îmbunătățire sau probleme, vă rugăm să creați un [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) sau să raportați o [problemă pe GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Echipa proiectului va urmări toate contribuțiile. Contribuția la open source este o metodă excelentă de a vă dezvolta cariera în AI Generativ.

Majoritatea contribuțiilor necesită să acceptați un Acord de Licență pentru Contribuitori (CLA) care declară că aveți dreptul și efectiv acordați drepturile de a folosi contribuția dvs. Pentru detalii, vizitați [site-ul CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Important: când traduceți text în acest repo, vă rugăm să nu folosiți traducerea automată. Vom verifica traducerile prin comunitate, deci vă rugăm să vă oferiți voluntar pentru traduceri doar dacă stăpâniți limba respectivă.

Când trimiteți un pull request, un bot CLA va determina automat dacă trebuie să oferiți un CLA și va decora PR-ul corespunzător (de ex., etichetă, comentariu). Urmați pur și simplu instrucțiunile oferite de bot. Acest lucru trebuie făcut o singură dată pentru toate depozitele care folosesc CLA-ul nostru.


Acest proiect a adoptat [Codul de Conduită Open Source Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Pentru mai multe informații, citiți Întrebările frecvente despre Codul de Conduită sau contactați [Email opencode](opencode@microsoft.com) pentru orice întrebări sau comentarii suplimentare.

## Să Începem

Acum că ați finalizat pașii necesari pentru a termina acest curs, să începem cu o [introducere în AI Generativ și LLM-uri](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->