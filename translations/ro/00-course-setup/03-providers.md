# Alegerea și configurarea unui furnizor LLM 🔑

Tema **poate** fi configurată să funcționeze cu una sau mai multe implementări Large Language Model (LLM) prin intermediul unui furnizor de servicii suportat, cum ar fi OpenAI, Azure sau Hugging Face. Acestea oferă un _endpoint găzduit_ (API) la care putem accesa programatic cu acreditările corecte (cheia API sau tokenul). În acest curs, discutăm despre acești furnizori:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) cu modele diverse, inclusiv seria principală GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) pentru modelele OpenAI, cu focus pe pregătirea pentru utilizare enterprise
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) pentru un singur endpoint și cheia API pentru accesarea a sute de modele de la OpenAI, Meta, Mistral, Cohere, Microsoft și alții (înlocuiește GitHub Models, care se va retrage la sfârșitul lunii iulie 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) pentru modele open source și server de inferență
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) sau [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) dacă dorești să rulezi modelele complet offline pe propriul dispozitiv, fără a fi necesar un abonament cloud

**Veți avea nevoie să folosiți propriile conturi pentru aceste exerciții**. Temele sunt opționale, deci puteți alege să configurați unul, pe toate sau niciunul dintre furnizori în funcție de interesele voastre. Iată câteva indicații pentru înscriere:

| Înscriere | Cost | Cheie API | Playground | Comentarii |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Tarife](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Pe bază de proiect](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Fără cod, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Mai multe modele disponibile |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Tarife](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Trebuie să aplici anterior pentru acces](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Tarife](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Pagina de overview a proiectului](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Tier gratuit disponibil; un endpoint + cheie pentru mulți furnizori de modele |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Tarife](https://huggingface.co/pricing) | [Token-uri de acces](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat are modele limitate](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Gratuit (rulează pe dispozitivul tău) | Nu este nevoie | [CLI/SDK local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Endpoint complet offline, compatibil OpenAI |
| | | | | |

Urmați instrucțiunile de mai jos pentru a _configura_ acest depozit pentru utilizarea cu furnizori diferiți. Temele care necesită un furnizor specific vor conține una dintre aceste etichete în numele fișierului:

- `aoai` - necesită endpoint și cheie Azure OpenAI
- `oai` - necesită endpoint și cheie OpenAI
- `hf` - necesită token Hugging Face
- `githubmodels` - necesită endpoint și cheie Microsoft Foundry Models (GitHub Models se va retrage la sfârșitul lui iulie 2026)

Puteți configura unul, niciunul sau toți furnizorii. Temele aferente vor afișa o eroare dacă lipsesc acreditările.

## Crearea fișierului `.env`

Presupunem că ați citit deja indicațiile de mai sus, v-ați înscris la furnizorul relevant și ați obținut acreditările de autentificare necesare (API_KEY sau token). În cazul Azure OpenAI, presupunem că aveți de asemenea o implementare validă a unui serviciu Azure OpenAI (endpoint) cu cel puțin un model GPT implementat pentru chat completion.

Următorul pas este să configurați **variabilele de mediu locale** astfel:

1. Căutați în folderul rădăcină un fișier `.env.copy` care ar trebui să aibă conținut asemănător cu acesta:

   ```bash
   # Furnizor OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI în Microsoft Foundry
   ## (Serviciul Azure OpenAI este acum parte din Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Implicit este setat! (versiunea API stabilă GA curentă)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Modele Microsoft Foundry (catalog de modele multi-furnizor, înlocuiește Modelele GitHub, care se retrage la sfârșitul lunii iulie 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Copiați acel fișier în `.env` folosind comanda de mai jos. Acest fișier este _gitignore-uit_, pentru a păstra secretele în siguranță.

   ```bash
   cp .env.copy .env
   ```

3. Completați valorile (înlocuind marcajele din partea dreaptă a `=`) conform descrierii din secțiunea următoare.

4. (Opțional) Dacă folosiți GitHub Codespaces, aveți opțiunea să salvați variabilele de mediu ca _secrete Codespaces_ asociate cu acest depozit. În acest caz, nu va mai fi nevoie să configurați un fișier local .env. **Cu toate acestea, rețineți că această opțiune funcționează numai dacă folosiți GitHub Codespaces.** Va trebui totuși să configurați fișierul .env dacă folosiți Docker Desktop.

## Popularea fișierului `.env`

Haideți să aruncăm o privire rapidă asupra numelor variabilelor pentru a înțelege ce reprezintă:

| Variabilă  | Descriere  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Acesta este token-ul de acces utilizator pe care îl configurezi în profilul tău |
| OPENAI_API_KEY | Aceasta este cheia de autorizare pentru utilizarea serviciului la endpoint-urile non-Azure OpenAI |
| AZURE_OPENAI_API_KEY | Aceasta este cheia de autorizare pentru utilizarea serviciului Azure OpenAI |
| AZURE_OPENAI_ENDPOINT | Acesta este endpoint-ul implementat pentru o resursă Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Acesta este endpoint-ul de implementare al modelului de _generare text_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Acesta este endpoint-ul de implementare al modelului de _încorporare text_ |
| AZURE_INFERENCE_ENDPOINT | Acesta este endpoint-ul pentru proiectul tău Microsoft Foundry, folosit pentru Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Aceasta este cheia API pentru proiectul tău Microsoft Foundry |
| | |

Notă: Ultimele două variabile Azure OpenAI reflectă un model implicit pentru chat completion (generare text) și căutare vectorială (embedding-uri), respectiv. Instrucțiunile pentru configurarea acestora vor fi definite în temele relevante.

## Configurarea Azure OpenAI: Din portal

> **Notă:** Azure OpenAI Service face acum parte din [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Resursele și implementările încă apar în Portalul Azure, dar gestionarea zilnică a modelelor (implementări, playground, monitorizare) se face acum în portalul Foundry în locul vechiului „Azure OpenAI Studio” standalone.

Valorile pentru endpoint și cheie Azure OpenAI vor fi găsite în [portalul Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), deci să începem de acolo.

1. Mergi la [portalul Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Click pe opțiunea **Keys and Endpoint** din bara laterală (meniul din stânga).
1. Click pe **Show Keys** - vei vedea următoarele: CHEIE 1, CHEIE 2 și Endpoint.
1. Folosește valoarea CHEIE 1 pentru AZURE_OPENAI_API_KEY
1. Folosește valoarea Endpoint pentru AZURE_OPENAI_ENDPOINT

Următorul pas este să obținem endpoint-urile pentru modelele specifice implementate.

1. Click pe opțiunea **Model deployments** din bara laterală (meniul din stânga) pentru resursa Azure OpenAI.
1. În pagina destinată, click pe **Go to Microsoft Foundry portal** (sau **Manage Deployments**, în funcție de tipul resursei tale)

Acest lucru te va duce la portalul Microsoft Foundry, unde vom găsi celelalte valori conform descrierii de mai jos.

## Configurarea Azure OpenAI: Din portalul Microsoft Foundry

1. Navighează la [portalul Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **din resursa ta**, așa cum am descris mai sus.
1. Click pe fila **Deployments** (bara laterală, stânga) pentru a vedea modelele implementate în prezent.
1. Dacă modelul dorit nu este implementat, folosește **Deploy model** pentru a-l implementa din [catalogul de modele](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Vei avea nevoie de un model de _generare text_ - recomandăm: **gpt-4o-mini**
1. Vei avea nevoie de un model de _embedding text_ - recomandăm **text-embedding-3-small**

Acum actualizează variabilele de mediu pentru a reflecta _Numele implementării_ folosit. Acesta va fi, de obicei, același cu numele modelului, dacă nu l-ai schimbat explicit. De exemplu, ai putea avea:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Nu uita să salvezi fișierul .env când termini**. Poți acum să închizi fișierul și să revii la instrucțiunile pentru rularea notebook-ului.

## Configurarea OpenAI: Din profil

Cheia ta API OpenAI poate fi găsită în contul tău [OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Dacă nu ai una, poți să te înscrii pentru un cont și să creezi o cheie API. După ce ai cheia, o poți folosi pentru a completa variabila `OPENAI_API_KEY` în fișierul `.env`.

## Configurarea Hugging Face: Din profil

Token-ul tău Hugging Face poate fi găsit în profilul tău, la secțiunea [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nu posta sau împărtăși aceste date public. În schimb, creează un token nou pentru utilizarea în acest proiect și copiază-l în fișierul `.env` sub variabila `HUGGING_FACE_API_KEY`. _Notă:_ Tehnic, acesta nu este o cheie API, dar este folosit pentru autentificare, așa că păstrăm această denumire pentru consistență.

## Configurarea Microsoft Foundry Models: Din portal

> **Notă:** GitHub Models se va retrage la sfârșitul lui iulie 2026. Microsoft Foundry Models este înlocuitorul direct, oferind același catalog cu modele gratuite de încercat și experiența SDK Azure AI Inference / OpenAI SDK.

1. Mergi la [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) și creează (sau deschide) un proiect Foundry.
1. Răsfoiește [catalogul de modele](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) și implementează un model, de exemplu `gpt-4o-mini`.
1. Pe pagina de **Overview** a proiectului, copiază **endpoint-ul** și **cheia API**.
1. Folosește valoarea endpoint-ului pentru `AZURE_INFERENCE_ENDPOINT` și cheia pentru `AZURE_INFERENCE_CREDENTIAL` în fișierul tău `.env`.

## Furnizori offline / locali

Dacă preferi să nu folosești deloc un abonament cloud, poți rula modele compatibile deschise direct pe propriul dispozitiv:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - runtime-ul Microsoft pe dispozitiv. Selectează automat cel mai bun furnizor de execuție (NPU, GPU sau CPU) și expune un endpoint compatibil OpenAI, așa că poți reutiliza majoritatea codului exemplu din acest curs cu modificări minime. Vezi documentația [Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) pentru pornire sau instalează cu `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - o alternativă populară pentru rularea locală a modelelor deschise precum Llama, Phi, Mistral și Gemma.


Vezi [Lecția 19: Construind cu SLM-uri](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) pentru exemple practice folosind ambele opțiuni.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->