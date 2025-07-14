<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:36:49+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "ro"
}
-->
# Configurează-ți Mediul de Dezvoltare

Am configurat acest depozit și curs cu un [container de dezvoltare](https://containers.dev?WT.mc_id=academic-105485-koreyst) care are un runtime universal ce poate suporta dezvoltare în Python3, .NET, Node.js și Java. Configurația aferentă este definită în fișierul `devcontainer.json` aflat în folderul `.devcontainer/` din rădăcina acestui depozit.

Pentru a activa containerul de dezvoltare, pornește-l în [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (pentru un runtime găzduit în cloud) sau în [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (pentru un runtime găzduit local). Consultă [această documentație](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) pentru mai multe detalii despre cum funcționează containerele de dezvoltare în VS Code.

> [!TIP]  
> Recomandăm folosirea GitHub Codespaces pentru un început rapid, cu efort minim. Acesta oferă o [cotă generoasă de utilizare gratuită](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) pentru conturile personale. Configurează [timeout-uri](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) pentru a opri sau șterge codespaces inactive, astfel maximizând utilizarea cotei tale.

## 1. Executarea Temelor

Fiecare lecție va avea teme _opționale_ care pot fi oferite în una sau mai multe limbaje de programare, inclusiv: Python, .NET/C#, Java și JavaScript/TypeScript. Această secțiune oferă îndrumări generale legate de executarea acestor teme.

### 1.1 Temele în Python

Temele în Python sunt oferite fie ca aplicații (`.py`), fie ca notebook-uri Jupyter (`.ipynb`).  
- Pentru a rula notebook-ul, deschide-l în Visual Studio Code, apoi apasă pe _Select Kernel_ (în dreapta sus) și alege opțiunea implicită Python 3. Acum poți folosi _Run All_ pentru a executa întregul notebook.  
- Pentru a rula aplicații Python din linia de comandă, urmează instrucțiunile specifice temei pentru a te asigura că selectezi fișierele corecte și furnizezi argumentele necesare.

## 2. Configurarea Providerilor

Temele **pot** fi configurate să funcționeze cu una sau mai multe implementări de Large Language Model (LLM) printr-un furnizor de servicii suportat, cum ar fi OpenAI, Azure sau Hugging Face. Aceștia oferă un _endpoint găzduit_ (API) la care putem accesa programatic cu acreditările corecte (cheie API sau token). În acest curs discutăm următorii provideri:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) cu modele diverse, inclusiv seria principală GPT.  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) pentru modelele OpenAI cu focus pe pregătirea pentru mediul enterprise  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) pentru modele open-source și server de inferență

**Va trebui să folosești propriile conturi pentru aceste exerciții**. Temele sunt opționale, așa că poți alege să configurezi unul, toți sau niciunul dintre provideri, în funcție de interesele tale. Iată câteva indicații pentru înscriere:

| Înscriere | Cost | Cheie API | Playground | Comentarii |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [Prețuri](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [Pe proiect](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Fără cod, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Mai multe modele disponibile |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [Prețuri](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Trebuie să aplici înainte pentru acces](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Prețuri](https://huggingface.co/pricing) | [Token-uri de acces](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat are modele limitate](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Urmează instrucțiunile de mai jos pentru a _configura_ acest depozit pentru utilizarea cu diferiți provideri. Temele care necesită un anumit provider vor conține unul dintre aceste tag-uri în numele fișierului:  
 - `aoai` - necesită endpoint și cheie Azure OpenAI  
 - `oai` - necesită endpoint și cheie OpenAI  
 - `hf` - necesită token Hugging Face

Poți configura unul, niciunul sau toți providerii. Temele aferente vor genera eroare dacă lipsesc acreditările.

### 2.1. Crearea fișierului `.env`

Presupunem că ai citit deja indicațiile de mai sus, te-ai înscris la providerul relevant și ai obținut acreditările necesare (API_KEY sau token). În cazul Azure OpenAI, presupunem că ai și o implementare validă a unui serviciu Azure OpenAI (endpoint) cu cel puțin un model GPT implementat pentru chat completions.

Următorul pas este să configurezi **variabilele de mediu locale** astfel:

1. Caută în folderul rădăcină un fișier `.env.copy` care ar trebui să conțină ceva similar cu:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Copiază acel fișier în `.env` folosind comanda de mai jos. Acest fișier este _gitignore-d_, pentru a păstra secretele în siguranță.

   ```bash
   cp .env.copy .env
   ```

3. Completează valorile (înlocuiește placeholder-ele din partea dreaptă a `=`) conform descrierii din secțiunea următoare.

3. (Opțional) Dacă folosești GitHub Codespaces, ai opțiunea să salvezi variabilele de mediu ca _secrete Codespaces_ asociate cu acest depozit. În acest caz, nu va trebui să configurezi un fișier local .env. **Totuși, reține că această opțiune funcționează doar dacă folosești GitHub Codespaces.** Va trebui să configurezi fișierul .env dacă folosești Docker Desktop.

### 2.2. Popularea fișierului `.env`

Să aruncăm o privire rapidă asupra numelor variabilelor pentru a înțelege ce reprezintă:

| Variabilă  | Descriere  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Token-ul de acces al utilizatorului pe care îl configurezi în profilul tău |
| OPENAI_API_KEY | Cheia de autorizare pentru utilizarea serviciului OpenAI non-Azure |
| AZURE_OPENAI_API_KEY | Cheia de autorizare pentru serviciul Azure OpenAI |
| AZURE_OPENAI_ENDPOINT | Endpoint-ul implementat pentru o resursă Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Endpoint-ul de implementare a modelului pentru _generare text_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Endpoint-ul de implementare a modelului pentru _embedding-uri text_ |
| | |

Notă: Ultimele două variabile Azure OpenAI reflectă un model implicit pentru chat completions (generare text) și căutare vectorială (embedding-uri). Instrucțiunile pentru configurarea lor vor fi definite în temele relevante.

### 2.3 Configurarea Azure: Din Portal

Valorile pentru endpoint și cheie Azure OpenAI le vei găsi în [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), așa că să începem de acolo.

1. Accesează [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
2. Apasă pe opțiunea **Keys and Endpoint** din bara laterală (meniul din stânga).  
3. Apasă pe **Show Keys** - ar trebui să vezi următoarele: KEY 1, KEY 2 și Endpoint.  
4. Folosește valoarea KEY 1 pentru AZURE_OPENAI_API_KEY  
5. Folosește valoarea Endpoint pentru AZURE_OPENAI_ENDPOINT

Următorul pas este să obținem endpoint-urile pentru modelele specifice pe care le-ai implementat.

1. Apasă pe opțiunea **Model deployments** din bara laterală (meniul din stânga) pentru resursa Azure OpenAI.  
2. În pagina destinată, apasă pe **Manage Deployments**

Aceasta te va duce pe site-ul Azure OpenAI Studio, unde vom găsi celelalte valori, după cum urmează.

### 2.4 Configurarea Azure: Din Studio

1. Navighează la [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **din resursa ta**, așa cum s-a descris mai sus.  
2. Apasă pe fila **Deployments** (bara laterală, stânga) pentru a vedea modelele implementate în prezent.  
3. Dacă modelul dorit nu este implementat, folosește **Create new deployment** pentru a-l implementa.  
4. Vei avea nevoie de un model _text-generation_ - recomandăm: **gpt-35-turbo**  
5. Vei avea nevoie de un model _text-embedding_ - recomandăm **text-embedding-ada-002**

Acum actualizează variabilele de mediu pentru a reflecta _numele implementării_ folosit. De obicei, acesta va fi același cu numele modelului, cu excepția cazului în care l-ai schimbat explicit. De exemplu, ai putea avea:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Nu uita să salvezi fișierul .env când termini**. Poți acum să închizi fișierul și să revii la instrucțiunile pentru rularea notebook-ului.

### 2.5 Configurarea OpenAI: Din Profil

Cheia ta API OpenAI poate fi găsită în contul tău [OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Dacă nu ai una, te poți înscrie și crea o cheie API. Odată ce ai cheia, o poți folosi pentru a completa variabila `OPENAI_API_KEY` în fișierul `.env`.

### 2.6 Configurarea Hugging Face: Din Profil

Token-ul tău Hugging Face poate fi găsit în profilul tău, la secțiunea [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nu posta sau distribui aceste token-uri public. În schimb, creează un token nou pentru utilizarea în acest proiect și copiază-l în fișierul `.env` sub variabila `HUGGING_FACE_API_KEY`. _Notă:_ Tehnic vorbind, acesta nu este o cheie API, dar este folosit pentru autentificare, așa că păstrăm această denumire pentru consistență.

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.