<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T19:11:56+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "ro"
}
-->
# Alegerea și Configurarea unui Furnizor LLM 🔑

Temele **pot** fi configurate să funcționeze cu una sau mai multe implementări de Large Language Model (LLM) prin intermediul unui furnizor de servicii suportat, precum OpenAI, Azure sau Hugging Face. Acestea oferă un _endpoint găzduit_ (API) la care putem accesa programatic cu acreditările potrivite (cheie API sau token). În acest curs, discutăm despre următorii furnizori:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) cu modele diverse, inclusiv seria principală GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) pentru modelele OpenAI cu accent pe utilizarea în mediul enterprise
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) pentru modele open-source și server de inferență

**Va trebui să folosești propriile conturi pentru aceste exerciții**. Temele sunt opționale, așa că poți alege să configurezi unul, toate - sau niciunul - dintre furnizori, în funcție de interesele tale. Câteva indicații pentru înscriere:

| Înscriere | Cost | Cheie API | Playground | Comentarii |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Prețuri](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Pe proiect](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Sunt disponibile mai multe modele |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Prețuri](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Trebuie să aplici în avans pentru acces](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Prețuri](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat are modele limitate](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Urmează instrucțiunile de mai jos pentru a _configura_ acest depozit pentru utilizarea cu diferiți furnizori. Temele care necesită un anumit furnizor vor conține unul dintre aceste tag-uri în numele fișierului:

- `aoai` - necesită endpoint și cheie Azure OpenAI
- `oai` - necesită endpoint și cheie OpenAI
- `hf` - necesită token Hugging Face

Poți configura unul, niciunul sau toți furnizorii. Temele aferente vor da eroare dacă lipsesc acreditările.

## Creează fișierul `.env`

Presupunem că ai citit deja indicațiile de mai sus, te-ai înscris la furnizorul relevant și ai obținut acreditările necesare pentru autentificare (API_KEY sau token). În cazul Azure OpenAI, presupunem că ai și o implementare validă a serviciului Azure OpenAI (endpoint) cu cel puțin un model GPT implementat pentru chat completion.

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

2. Copiază acel fișier ca `.env` folosind comanda de mai jos. Acest fișier este _gitignore-d_, astfel încât secretele rămân în siguranță.

   ```bash
   cp .env.copy .env
   ```

3. Completează valorile (înlocuiește placeholder-ele din dreapta semnului `=`) așa cum este descris în secțiunea următoare.

4. (Opțional) Dacă folosești GitHub Codespaces, ai opțiunea să salvezi variabilele de mediu ca _Codespaces secrets_ asociate acestui depozit. În acest caz, nu va mai fi nevoie să configurezi un fișier .env local. **Totuși, reține că această opțiune funcționează doar dacă folosești GitHub Codespaces.** Va trebui totuși să configurezi fișierul .env dacă folosești Docker Desktop.

## Completează fișierul `.env`

Să aruncăm o privire rapidă asupra numelor variabilelor pentru a înțelege ce reprezintă:

| Variabilă  | Descriere  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Acesta este token-ul de acces pe care îl setezi în profilul tău |
| OPENAI_API_KEY | Aceasta este cheia de autorizare pentru utilizarea serviciului pentru endpoint-urile non-Azure OpenAI |
| AZURE_OPENAI_API_KEY | Aceasta este cheia de autorizare pentru utilizarea acelui serviciu |
| AZURE_OPENAI_ENDPOINT | Acesta este endpoint-ul implementat pentru o resursă Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Acesta este endpoint-ul de implementare a modelului _text generation_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Acesta este endpoint-ul de implementare a modelului _text embeddings_ |
| | |

Notă: Ultimele două variabile Azure OpenAI reflectă un model implicit pentru chat completion (generare de text) și căutare vectorială (embeddings). Instrucțiunile pentru setarea lor vor fi definite în temele relevante.

## Configurează Azure: Din Portal

Valorile pentru endpoint și cheie Azure OpenAI se găsesc în [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), așa că să începem de acolo.

1. Accesează [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Dă click pe opțiunea **Keys and Endpoint** din bara laterală (meniul din stânga).
1. Apasă pe **Show Keys** - ar trebui să vezi următoarele: KEY 1, KEY 2 și Endpoint.
1. Folosește valoarea KEY 1 pentru AZURE_OPENAI_API_KEY
1. Folosește valoarea Endpoint pentru AZURE_OPENAI_ENDPOINT

În continuare, avem nevoie de endpoint-urile pentru modelele specifice pe care le-am implementat.

1. Dă click pe opțiunea **Model deployments** din bara laterală (meniul din stânga) pentru resursa Azure OpenAI.
1. Pe pagina de destinație, apasă pe **Manage Deployments**

Acest lucru te va duce pe site-ul Azure OpenAI Studio, unde vom găsi celelalte valori, așa cum este descris mai jos.

## Configurează Azure: Din Studio

1. Navighează la [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **din resursa ta** așa cum am descris mai sus.
1. Dă click pe tab-ul **Deployments** (bara laterală, stânga) pentru a vedea modelele implementate în prezent.
1. Dacă modelul dorit nu este implementat, folosește **Create new deployment** pentru a-l implementa.
1. Vei avea nevoie de un model _text-generation_ - recomandăm: **gpt-35-turbo**
1. Vei avea nevoie de un model _text-embedding_ - recomandăm **text-embedding-ada-002**

Acum actualizează variabilele de mediu pentru a reflecta _Deployment name_ folosit. De obicei, acesta va fi același cu numele modelului, dacă nu l-ai schimbat explicit. De exemplu, ai putea avea:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Nu uita să salvezi fișierul .env când ai terminat**. Poți ieși acum din fișier și să revii la instrucțiunile pentru rularea notebook-ului.

## Configurează OpenAI: Din Profil

Cheia ta OpenAI API poate fi găsită în [contul tău OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Dacă nu ai una, poți să-ți faci un cont și să creezi o cheie API. Odată ce ai cheia, o poți folosi pentru a completa variabila `OPENAI_API_KEY` în fișierul `.env`.

## Configurează Hugging Face: Din Profil

Token-ul tău Hugging Face poate fi găsit în profilul tău, la secțiunea [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nu posta sau distribui aceste date public. Creează un token nou pentru acest proiect și copiază-l în fișierul `.env` la variabila `HUGGING_FACE_API_KEY`. _Notă:_ Tehnic, acesta nu este o cheie API, dar este folosit pentru autentificare, așa că păstrăm această denumire pentru consistență.

---

**Declarație de responsabilitate**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm răspunderea pentru eventuale neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.