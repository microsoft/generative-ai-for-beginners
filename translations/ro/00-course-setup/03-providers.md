# Alegerea și configurarea unui furnizor LLM 🔑

Temele **pot** fi, de asemenea, configurate să funcționeze cu una sau mai multe implementări de modele mari de limbaj (LLM) prin intermediul unui furnizor de servicii acceptat, cum ar fi OpenAI, Azure sau Hugging Face. Acestea oferă un _endpoint găzduit_ (API) la care putem accesa programatic cu credențialele potrivite (cheie API sau token). În acest curs discutăm acești furnizori:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) cu modele diverse, inclusiv seria principală GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) pentru modelele OpenAI cu focus pe pregătirea pentru mediul enterprise
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) pentru un singur endpoint și cheie API pentru acces la sute de modele de la OpenAI, Meta, Mistral, Cohere, Microsoft și altele (înlocuiește GitHub Models, care va fi retras la sfârșitul lui iulie 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) pentru modele open-source și server de inferență
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) sau [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) dacă preferi să rulezi modelele complet offline pe propriul dispozitiv, fără a necesita un abonament cloud

**Va trebui să folosești propriile tale conturi pentru aceste exerciții**. Temele sunt opționale, astfel încât poți alege să configurezi unul, toți sau niciunul dintre furnizori în funcție de interesele tale. Iată câteva recomandări pentru înscriere:

| Înscriere | Cost | Cheie API | Playground | Comentarii |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Prețuri](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Pe bază de proiect](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Multiple modele disponibile |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Prețuri](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Trebuie să aplici în prealabil pentru acces](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Prețuri](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Pagina de prezentare a proiectului](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Tier gratuit disponibil; un endpoint + cheie pentru mulți furnizori de modele |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Prețuri](https://huggingface.co/pricing) | [Token-uri de acces](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat are modele limitate](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Gratuit (rulează pe dispozitivul tău) | Nu este necesar | [CLI/SDK local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Endpoint complet offline, compatibil OpenAI |
| | | | | |

Urmează instrucțiunile de mai jos pentru a _configura_ acest depozit pentru utilizare cu diferiți furnizori. Temele care necesită un furnizor specific vor conține unul dintre aceste etichete în numele fișierului:

- `aoai` - necesită endpoint și cheie Azure OpenAI
- `oai` - necesită endpoint și cheie OpenAI
- `hf` - necesită token Hugging Face
- `githubmodels` - necesită endpoint și cheie Microsoft Foundry Models (GitHub Models va fi retras la sfârșitul lui iulie 2026)

Poți configura unul, niciunul sau toți furnizorii. Temele asociate vor da eroare dacă lipsesc credențialele.

## Creează fișierul `.env`

Presupunem că ai citit deja recomandările de mai sus și te-ai înscris la furnizorul relevant, obținând credențialele de autentificare necesare (API_KEY sau token). În cazul Azure OpenAI, presupunem că ai și o implementare validă a unui serviciu Azure OpenAI (endpoint) cu cel puțin un model GPT implementat pentru completare chat.

Următorul pas este să configurezi **variabilele de mediu locale** astfel:

1. Caută în folderul rădăcină un fișier `.env.copy` care ar trebui să conțină ceva similar cu următorul:

   ```bash
   # Furnizor OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI în Microsoft Foundry
   ## (Serviciul Azure OpenAI face acum parte din Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Implicit este setat! (versiunea API stabilă curentă GA)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Modele Microsoft Foundry (catalog model multi-furnizor, înlocuiește Modelele GitHub, care se retrag la sfârșitul lunii iulie 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Copiază acel fișier în `.env` folosind comanda de mai jos. Acest fișier este _gitignore-d_, pentru a păstra secretele în siguranță.

   ```bash
   cp .env.copy .env
   ```

3. Completează valorile (înlocuiește substituenții din dreapta semnului `=`) așa cum este descris în secțiunea următoare.

4. (Opțional) Dacă utilizezi GitHub Codespaces, ai opțiunea să salvezi variabilele de mediu ca _secrete Codespaces_ asociate cu acest depozit. În acest caz, nu va trebui să configurezi un fișier .env local. **Totuși, reține că această opțiune funcționează doar dacă folosești GitHub Codespaces.** Va trebui să configurezi fișierul .env în continuare dacă folosești Docker Desktop.

## Completează fișierul `.env`

Haide să aruncăm o privire rapidă asupra numelor variabilelor pentru a înțelege ce reprezintă:

| Variabilă  | Descriere  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Acesta este token-ul de acces al utilizatorului pe care îl configurezi în profilul tău |
| OPENAI_API_KEY | Aceasta este cheia de autorizare pentru utilizarea serviciului pentru endpoint-urile non-Azure OpenAI |
| AZURE_OPENAI_API_KEY | Aceasta este cheia de autorizare pentru utilizarea acelui serviciu |
| AZURE_OPENAI_ENDPOINT | Acesta este endpoint-ul implementat pentru o resursă Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Acesta este endpoint-ul de implementare a modelului _generare de text_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Acesta este endpoint-ul de implementare a modelului pentru _încorporări de text_ |
| AZURE_INFERENCE_ENDPOINT | Acesta este endpoint-ul pentru proiectul tău Microsoft Foundry, utilizat pentru Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Aceasta este cheia API pentru proiectul tău Microsoft Foundry |
| | |

Notă: Ultimele două variabile Azure OpenAI reflectă un model implicit pentru completarea chat-ului (generarea de text) respectiv căutare vectorială (încorporări). Instrucțiunile pentru configurarea lor vor fi definite în temele relevante.

## Configurare Azure OpenAI: Din Portal

> **Notă:** Serviciul Azure OpenAI face acum parte din [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Resursele și implementările încă apar în Azure Portal, dar gestionarea zilnică a modelelor (implementări, playground, monitorizare) se face acum în portalul Foundry, în locul vechiului "Azure OpenAI Studio" independent.

Valorile endpoint și cheie Azure OpenAI vor fi găsite în [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), așa că să începem de acolo.

1. Accesează [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Dă clic pe opțiunea **Keys and Endpoint** în bara laterală (meniu din stânga).
1. Dă clic pe **Show Keys** - ar trebui să vezi următoarele: CHEIA 1, CHEIA 2 și Endpoint.
1. Folosește valoarea CHEIA 1 pentru AZURE_OPENAI_API_KEY
1. Folosește valoarea Endpoint pentru AZURE_OPENAI_ENDPOINT

Următorul pas este să obținem endpoint-urile pentru modelele specifice pe care le-am implementat.

1. Dă clic pe opțiunea **Model deployments** din bara laterală (meniu din stânga) pentru resursa Azure OpenAI.
1. În pagina destinată, dă clic pe **Go to Microsoft Foundry portal** (sau **Manage Deployments**, în funcție de tipul resursei tale)

Aceasta te va duce în portalul Microsoft Foundry, unde vom găsi celelalte valori, așa cum este descris mai jos.

## Configurare Azure OpenAI: Din portalul Microsoft Foundry

1. Navighează la [portalul Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **din resursa ta**, așa cum s-a descris mai sus.
1. Dă clic pe fila **Deployments** (bara laterală, stânga) pentru a vedea modelele implementate în prezent.
1. Dacă modelul dorit nu este implementat, folosește **Deploy model** pentru a-l implementa din [catalogul de modele](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Vei avea nevoie de un model de _generare text_ – recomandăm: **gpt-5-mini**
1. Vei avea nevoie de un model de _încorporare text_ – recomandăm **text-embedding-3-small**

Acum actualizează variabilele de mediu pentru a reflecta _numele implementării_ folosit. Acesta va fi, de obicei, același cu numele modelului, dacă nu l-ai schimbat explicit. De exemplu, ai putea avea:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Nu uita să salvezi fișierul .env când termini**. Poți acum să închizi fișierul și să revii la instrucțiunile pentru rularea notebook-ului.

## Configurare OpenAI: Din profil

Cheia ta API OpenAI poate fi găsită în [contul tău OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Dacă nu ai una, te poți înscrie pentru un cont și poți crea o cheie API. Odată ce ai cheia, o poți folosi pentru a popula variabila `OPENAI_API_KEY` în fișierul `.env`.

## Configurare Hugging Face: Din profil

Token-ul tău Hugging Face poate fi găsit în profilul tău, sub [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Nu posta sau distribui public aceste token-uri. În schimb, creează un token nou pentru utilizarea acestui proiect și copiază-l în fișierul `.env` sub variabila `HUGGING_FACE_API_KEY`. _Notă:_ Aceasta tehnic nu este o cheie API, dar este folosită pentru autentificare, așa că păstrăm această convenție de denumire pentru consistență.

## Configurare Microsoft Foundry Models: Din portal

> **Notă:** GitHub Models va fi retras la sfârșitul lui iulie 2026. Microsoft Foundry Models este înlocuitorul direct, oferind același catalog de modele gratuit de încercat și experiența Azure AI Inference SDK / OpenAI SDK.

1. Accesează [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) și creează (sau deschide) un proiect Foundry.
1. Navighează în [catalogul de modele](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) și implementează un model, de exemplu `gpt-5-mini`.
1. Pe pagina de **Overview** a proiectului, copiază **endpoint-ul** și **cheia API**.
1. Folosește valoarea endpoint pentru `AZURE_INFERENCE_ENDPOINT` și cheia pentru `AZURE_INFERENCE_CREDENTIAL` în fișierul tău `.env`.

## Furnizori offline / locali

Dacă preferi să nu folosești deloc un abonament cloud, poți rula modele open compatibile direct pe propriul tău dispozitiv:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - runtime-ul Microsoft pe dispozitiv. Selectează automat cel mai bun furnizor de execuție (NPU, GPU sau CPU) și expune un endpoint compatibil OpenAI, astfel încât poți reutiliza majoritatea codului exemplu din acest curs cu modificări minime. Vezi [documentația Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) pentru început, sau instalează cu `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - o alternativă populară pentru rularea modelelor open precum Llama, Phi, Mistral și Gemma local.


Vezi [Lecția 19: Construirea cu SLM-uri](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) pentru exemple practice folosind ambele opțiuni.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->