<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:59:30+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "ro"
}
-->
# Configurează Mediul Tău de Dezvoltare

Am configurat acest depozit și curs cu un [container de dezvoltare](https://containers.dev?WT.mc_id=academic-105485-koreyst) care are un runtime universal ce poate susține dezvoltarea în Python3, .NET, Node.js și Java. Configurația relevantă este definită în fișierul `devcontainer.json` situat în folderul `.devcontainer/` la rădăcina acestui depozit.

Pentru a activa containerul de dezvoltare, lansează-l în [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (pentru un runtime găzduit în cloud) sau în [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (pentru un runtime găzduit pe dispozitiv local). Citește [această documentație](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) pentru mai multe detalii despre cum funcționează containerele de dezvoltare în VS Code.  

> [!TIP]  
> Recomandăm utilizarea GitHub Codespaces pentru un start rapid cu efort minim. Oferă o [cotă de utilizare gratuită](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) generoasă pentru conturi personale. Configurează [timeout-uri](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) pentru a opri sau șterge codespaces inactive pentru a maximiza utilizarea cotei tale.


## 1. Executarea Temelor

Fiecare lecție va avea teme _opționale_ care pot fi oferite într-una sau mai multe limbaje de programare, inclusiv: Python, .NET/C#, Java și JavaScript/TypeScript. Această secțiune oferă îndrumări generale legate de executarea acestor teme.

### 1.1 Teme Python

Temele Python sunt oferite fie ca aplicații (fișiere `.py`) sau notebook-uri Jupyter (fișiere `.ipynb`). 
- Pentru a rula notebook-ul, deschide-l în Visual Studio Code, apoi apasă _Select Kernel_ (în dreapta sus) și selectează opțiunea implicită Python 3 afișată. Poți acum să apeși _Run All_ pentru a executa notebook-ul.
- Pentru a rula aplicații Python din linia de comandă, urmează instrucțiunile specifice temei pentru a te asigura că selectezi fișierele corecte și oferi argumentele necesare.

## 2. Configurarea Furnizorilor

Temele **pot** fi configurate să funcționeze cu una sau mai multe implementări de modele de limbaj mare (LLM) printr-un furnizor de servicii suportat, cum ar fi OpenAI, Azure sau Hugging Face. Acestea oferă un _endpoint găzduit_ (API) la care putem accesa programatic cu credențialele corecte (cheie API sau token). În acest curs, discutăm despre acești furnizori:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) cu modele diverse, inclusiv seria de bază GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) pentru modele OpenAI cu accent pe pregătirea pentru întreprinderi
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) pentru modele open-source și server de inferență

**Va trebui să folosești propriile conturi pentru aceste exerciții**. Temele sunt opționale, așa că poți alege să configurezi unul, toți - sau niciunul - dintre furnizori, în funcție de interesele tale. Câteva îndrumări pentru înscriere:

| Înscriere | Cost | Cheie API | Playground | Comentarii |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Prețuri](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Pe bază de proiect](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Fără cod, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Multiple modele disponibile |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Prețuri](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Trebuie să aplici în avans pentru acces](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Prețuri](https://huggingface.co/pricing) | [Token-uri de acces](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat are modele limitate](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Urmează instrucțiunile de mai jos pentru a _configura_ acest depozit pentru utilizare cu diferiți furnizori. Temele care necesită un furnizor specific vor conține unul dintre aceste tag-uri în numele fișierului:
 - `aoai` - necesită endpoint Azure OpenAI, cheie
 - `oai` - necesită endpoint OpenAI, cheie
 - `hf` - necesită token Hugging Face

Poți configura unul, niciunul, sau toți furnizorii. Temele relevante vor da eroare în cazul lipsei credențialelor.

###  2.1. Creează fișierul `.env`

Presupunem că ai citit deja îndrumările de mai sus și te-ai înscris la furnizorul relevant, obținând credențialele necesare pentru autentificare (API_KEY sau token). În cazul Azure OpenAI, presupunem că ai și o implementare validă a unui serviciu Azure OpenAI (endpoint) cu cel puțin un model GPT implementat pentru completare de chat.

Următorul pas este să configurezi **variabilele de mediu locale** astfel:

1. Caută în folderul rădăcină un fișier `.env.copy` care ar trebui să aibă conținut similar cu acesta:

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

2. Copiază acel fișier în `.env` folosind comanda de mai jos. Acest fișier este _gitignore-d_, păstrând secretele în siguranță.

   ```bash
   cp .env.copy .env
   ```

3. Completează valorile (înlocuiește locurile rezervate din partea dreaptă a `=`) așa cum este descris în secțiunea următoare.

3. (Opțiune) Dacă folosești GitHub Codespaces, ai opțiunea de a salva variabilele de mediu ca _secrete Codespaces_ asociate cu acest depozit. În acest caz, nu va trebui să configurezi un fișier .env local. **Totuși, notează că această opțiune funcționează doar dacă folosești GitHub Codespaces.** Va trebui să configurezi totuși fișierul .env dacă folosești Docker Desktop.

### 2.2. Completează fișierul `.env`

Să aruncăm o privire rapidă asupra numelor de variabile pentru a înțelege ce reprezintă:

| Variabilă  | Descriere  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Acesta este token-ul de acces al utilizatorului pe care l-ai configurat în profilul tău |
| OPENAI_API_KEY | Aceasta este cheia de autorizare pentru utilizarea serviciului pentru endpoint-uri non-Azure OpenAI |
| AZURE_OPENAI_API_KEY | Aceasta este cheia de autorizare pentru utilizarea acelui serviciu |
| AZURE_OPENAI_ENDPOINT | Acesta este endpoint-ul implementat pentru o resursă Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Acesta este endpoint-ul de implementare a modelului _text generation_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Acesta este endpoint-ul de implementare a modelului _text embeddings_ |
| | |

Notă: Ultimele două variabile Azure OpenAI reflectă un model implicit pentru completarea de chat (generare de text) și căutare vectorială (embeddings), respectiv. Instrucțiuni pentru setarea lor vor fi definite în temele relevante.

### 2.3 Configurează Azure: Din Portal

Valorile endpoint-ului și cheii Azure OpenAI vor fi găsite în [Portalul Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), așa că să începem acolo.

1. Mergi la [Portalul Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Apasă opțiunea **Keys and Endpoint** în bara laterală (meniul din stânga).
1. Apasă **Show Keys** - ar trebui să vezi următoarele: KEY 1, KEY 2 și Endpoint.
1. Folosește valoarea KEY 1 pentru AZURE_OPENAI_API_KEY
1. Folosește valoarea Endpoint pentru AZURE_OPENAI_ENDPOINT

Următorul pas este să obținem endpoint-urile pentru modelele specifice pe care le-am implementat.

1. Apasă opțiunea **Model deployments** în bara laterală (meniul din stânga) pentru resursa Azure OpenAI.
1. În pagina de destinație, apasă **Manage Deployments**

Acest lucru te va duce la site-ul web Azure OpenAI Studio, unde vom găsi celelalte valori, așa cum este descris mai jos.

### 2.4 Configurează Azure: Din Studio

1. Navighează la [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **din resursa ta** așa cum este descris mai sus.
1. Apasă pe tab-ul **Deployments** (bara laterală, stânga) pentru a vedea modelele implementate în prezent.
1. Dacă modelul dorit nu este implementat, folosește **Create new deployment** pentru a-l implementa.
1. Vei avea nevoie de un model _text-generation_ - recomandăm: **gpt-35-turbo**
1. Vei avea nevoie de un model _text-embedding_ - recomandăm **text-embedding-ada-002**

Acum actualizează variabilele de mediu pentru a reflecta numele _Deployment_ utilizat. Acesta va fi de obicei același cu numele modelului, cu excepția cazului în care l-ai schimbat explicit. Deci, ca exemplu, ai putea avea:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Nu uita să salvezi fișierul .env când ai terminat**. Poți acum să ieși din fișier și să te întorci la instrucțiunile pentru rularea notebook-ului.

### 2.5 Configurează OpenAI: Din Profil

Cheia ta API OpenAI poate fi găsită în [contul tău OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Dacă nu ai una, te poți înscrie pentru un cont și crea o cheie API. Odată ce ai cheia, o poți folosi pentru a completa variabila `OPENAI_API_KEY` în fișierul `.env`.

### 2.6 Configurează Hugging Face: Din Profil

Token-ul tău Hugging Face poate fi găsit în profilul tău sub [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nu le posta sau împărtăși public. În schimb, creează un nou token pentru utilizarea acestui proiect și copiază-l în fișierul `.env` sub variabila `HUGGING_FACE_API_KEY`. _Notă:_ Acesta nu este tehnic o cheie API, dar este folosit pentru autentificare, așa că păstrăm acea convenție de denumire pentru consistență.

**Declinarea responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să obținem acuratețe, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională umană. Nu suntem răspunzători pentru niciun fel de neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.