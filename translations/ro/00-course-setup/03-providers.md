# Alegerea și configurarea unui furnizor LLM 🔑

Temele **pot** fi configurate să funcționeze cu una sau mai multe implementări de modele mari de limbaj (LLM) printr-un furnizor de servicii suportat, cum ar fi OpenAI, Azure sau Hugging Face. Acestea oferă un _endpoint găzduit_ (API) la care putem accesa programatic cu acreditările corecte (cheie API sau token). În acest curs, discutăm despre acești furnizori:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) cu modele diverse, inclusiv seria principală GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) pentru modelele OpenAI cu accent pe pregătirea pentru mediul enterprise
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) pentru modele open-source și server de inferență

**Va trebui să folosiți propriile conturi pentru aceste exerciții**. Temele sunt opționale, așa că puteți alege să configurați unul, toți - sau niciunul - dintre furnizori în funcție de interesele dvs. Câteva indicații pentru înscriere:

| Înscriere | Cost | Cheie API | Playground | Comentarii |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Prețuri](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Pe bază de proiect](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Fără cod, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Mai multe modele disponibile |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Prețuri](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Trebuie să aplicați în prealabil pentru acces](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Prețuri](https://huggingface.co/pricing) | [Tokenuri de acces](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat are modele limitate](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Urmați instrucțiunile de mai jos pentru a _configura_ acest depozit pentru utilizarea cu diferiți furnizori. Temele care necesită un furnizor specific vor conține una dintre aceste etichete în numele fișierului:

- `aoai` - necesită endpoint și cheie Azure OpenAI
- `oai` - necesită endpoint și cheie OpenAI
- `hf` - necesită token Hugging Face

Puteți configura unul, niciunul sau toți furnizorii. Temele aferente vor genera pur și simplu o eroare dacă lipsesc acreditările.

## Creați fișierul `.env`

Presupunem că ați citit deja indicațiile de mai sus, v-ați înscris la furnizorul relevant și ați obținut acreditările necesare de autentificare (API_KEY sau token). În cazul Azure OpenAI, presupunem că aveți și o implementare validă a unui serviciu Azure OpenAI (endpoint) cu cel puțin un model GPT implementat pentru completare chat.

Următorul pas este să configurați **variabilele de mediu locale** astfel:

1. Căutați în folderul rădăcină un fișier `.env.copy` care ar trebui să aibă conținut ca acesta:

   ```bash
   # Furnizor OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Implicit este setat!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Copiați acel fișier în `.env` folosind comanda de mai jos. Acest fișier este _gitignore-d_, păstrând secretele în siguranță.

   ```bash
   cp .env.copy .env
   ```

3. Completați valorile (înlocuiți locurile rezervate din partea dreaptă a `=`) așa cum este descris în secțiunea următoare.

4. (Opțional) Dacă folosiți GitHub Codespaces, aveți opțiunea să salvați variabilele de mediu ca _secrete Codespaces_ asociate cu acest depozit. În acest caz, nu va trebui să configurați un fișier .env local. **Totuși, rețineți că această opțiune funcționează doar dacă folosiți GitHub Codespaces.** Va trebui să configurați fișierul .env dacă folosiți Docker Desktop.

## Completați fișierul `.env`

Să aruncăm o privire rapidă asupra numelor variabilelor pentru a înțelege ce reprezintă:

| Variabilă  | Descriere  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Acesta este tokenul de acces al utilizatorului pe care îl configurați în profilul dvs. |
| OPENAI_API_KEY | Aceasta este cheia de autorizare pentru utilizarea serviciului pentru endpointuri non-Azure OpenAI |
| AZURE_OPENAI_API_KEY | Aceasta este cheia de autorizare pentru utilizarea serviciului Azure OpenAI |
| AZURE_OPENAI_ENDPOINT | Acesta este endpointul implementat pentru o resursă Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Acesta este endpointul de implementare a modelului de _generare text_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Acesta este endpointul de implementare a modelului de _embedding text_ |
| | |

Notă: Ultimele două variabile Azure OpenAI reflectă un model implicit pentru completarea chat (generare text) și căutare vectorială (embedding-uri) respectiv. Instrucțiunile pentru configurarea lor vor fi definite în temele relevante.

## Configurați Azure: Din Portal

Valorile endpointului și cheii Azure OpenAI se găsesc în [Portalul Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), așa că să începem de acolo.

1. Accesați [Portalul Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Faceți clic pe opțiunea **Keys and Endpoint** în bara laterală (meniul din stânga).
1. Faceți clic pe **Show Keys** - ar trebui să vedeți următoarele: CHEIA 1, CHEIA 2 și Endpoint.
1. Folosiți valoarea CHEIA 1 pentru AZURE_OPENAI_API_KEY
1. Folosiți valoarea Endpoint pentru AZURE_OPENAI_ENDPOINT

Următorul pas este să obținem endpointurile pentru modelele specifice pe care le-am implementat.

1. Faceți clic pe opțiunea **Model deployments** în bara laterală (meniul din stânga) pentru resursa Azure OpenAI.
1. În pagina destinație, faceți clic pe **Manage Deployments**

Aceasta vă va duce la site-ul Azure OpenAI Studio, unde vom găsi celelalte valori descrise mai jos.

## Configurați Azure: Din Studio

1. Navigați la [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **din resursa dvs.** așa cum este descris mai sus.
1. Faceți clic pe fila **Deployments** (bara laterală, stânga) pentru a vedea modelele implementate în prezent.
1. Dacă modelul dorit nu este implementat, folosiți **Create new deployment** pentru a-l implementa.
1. Veți avea nevoie de un model de _generare text_ - recomandăm: **gpt-35-turbo**
1. Veți avea nevoie de un model de _embedding text_ - recomandăm **text-embedding-ada-002**

Acum actualizați variabilele de mediu pentru a reflecta _Numele implementării_ folosit. Acesta va fi de obicei același cu numele modelului, cu excepția cazului în care l-ați schimbat explicit. Deci, ca exemplu, ați putea avea:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Nu uitați să salvați fișierul .env când terminați**. Puteți acum să închideți fișierul și să reveniți la instrucțiunile pentru rularea notebook-ului.

## Configurați OpenAI: Din profil

Cheia API OpenAI poate fi găsită în contul dvs. [OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Dacă nu aveți una, vă puteți înscrie pentru un cont și crea o cheie API. Odată ce aveți cheia, o puteți folosi pentru a completa variabila `OPENAI_API_KEY` în fișierul `.env`.

## Configurați Hugging Face: Din profil

Tokenul Hugging Face poate fi găsit în profilul dvs. la [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nu postați sau distribuiți aceste tokenuri public. În schimb, creați un token nou pentru utilizarea în acest proiect și copiați-l în fișierul `.env` sub variabila `HUGGING_FACE_API_KEY`. _Notă:_ Tehnic, acesta nu este o cheie API, dar este folosit pentru autentificare, așa că păstrăm această convenție de denumire pentru consistență.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->