# AGENTS.md

## Prezentare generală a proiectului

Acest depozit conține un curriculum cuprinzător de 21 de lecții care predau elementele fundamentale ale AI Generativ și dezvoltarea aplicațiilor. Cursul este conceput pentru începători și acoperă totul, de la concepte de bază până la construirea aplicațiilor pregătite pentru producție.

**Tehnologii cheie:**
- Python 3.9+ cu biblioteci: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript cu Node.js și biblioteci: `openai` (Azure OpenAI prin endpoint-ul v1 + API-ul Responses), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Serviciul Azure OpenAI, API-ul OpenAI și Microsoft Foundry Models (GitHub Models va fi retras la sfârșitul lunii iulie 2026)
- Jupyter Notebooks pentru învățare interactivă
- Dev Containers pentru un mediu de dezvoltare consistent

**Structura depozitului:**
- 21 directoare numerotate pentru lecții (00-21) conținând README-uri, exemple de cod și teme
- Implementări multiple: exemple în Python, TypeScript și uneori .NET
- Directorul de traduceri cu peste 40 de versiuni în limbi diferite
- Configurare centralizată prin fișierul `.env` (folosește `.env.copy` ca șablon)

## Comenzi de configurare

### Configurarea inițială a depozitului

```bash
# Clonați depozitul
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copiați șablonul de mediu
cp .env.copy .env
# Editați .env cu cheile API și punctele finale
```

### Configurarea mediului Python

```bash
# Creează mediu virtual
python3 -m venv venv

# Activează mediul virtual
# Pe macOS/Linux:
source venv/bin/activate
# Pe Windows:
venv\Scripts\activate

# Instalează dependențele
pip install -r requirements.txt
```

### Configurarea Node.js/TypeScript

```bash
# Instalează dependențele la nivel de root (pentru uneltele de documentație)
npm install

# Pentru exemplele TypeScript ale unei lecții individuale, navigați la lecția specifică:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Configurarea Dev Container (Recomandat)

Depozitul include o configurație `.devcontainer` pentru GitHub Codespaces sau VS Code Dev Containers:

1. Deschide depozitul în GitHub Codespaces sau VS Code cu extensia Dev Containers
2. Dev Container va face următoarele automat:
   - Instalează dependențele Python din `requirements.txt`
   - Rulează scriptul post-creare (`.devcontainer/post-create.sh`)
   - Configurează kernelul Jupyter

## Fluxul de lucru pentru dezvoltare

### Variabile de mediu

Toate lecțiile care necesită acces la API folosesc variabile de mediu definite în `.env`:

- `OPENAI_API_KEY` - Pentru API-ul OpenAI
- `AZURE_OPENAI_API_KEY` - Pentru Azure OpenAI în Microsoft Foundry (Serviciul Azure OpenAI este acum parte a Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL-ul endpoint-ului Azure OpenAI (endpoint-ul resursei Foundry)
- `AZURE_OPENAI_DEPLOYMENT` - Numele implementării modelului de completare chat (implicitul cursului: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Numele implementării modelului de embeddings (implicitul cursului: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - Versiunea API-ului (implicit: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Pentru modelele Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - Endpoint-ul Microsoft Foundry Models (catalog de modele multi-furnizor)
- `AZURE_INFERENCE_CREDENTIAL` - Cheia API Microsoft Foundry Models (înlocuiește `GITHUB_TOKEN` care se retrage)
- `AZURE_INFERENCE_CHAT_MODEL` - Un model fără abilitate de raționament (ex: `Llama-3.3-70B-Instruct`) folosit în exemplele cu `temperature`, deoarece modelele de raționament nu suportă controale de eșantionare

### Convenții pentru modele (important)

- **Modelul implicit de chat este `gpt-5-mini`** - un model actual, **de raționament**, care nu este depreciat. Din 2026, modelele mai vechi "mini" capabile de temperatura (`gpt-4o-mini`, `gpt-4.1-mini`) sunt în *proces de retragere*, astfel că curriculum-ul se standardizează pe familia GPT-5.
- **Modelele de raționament resping `temperature` și `top_p`** și folosesc în schimb `max_output_tokens` (Responses API) / `max_completion_tokens` (completări chat) în loc de `max_tokens`. Nu adăuga `temperature`/`top_p`/`max_tokens` în exemplele care apelează `gpt-5-mini`.
- **Pentru a demonstra `temperature`**, exemplele folosesc un model **Llama** (`Llama-3.3-70B-Instruct`) prin endpoint-ul Microsoft Foundry Models (`AZURE_INFERENCE_CHAT_MODEL`). Modelele de raționament se dirijează prin inginerie de prompt + controale de raționament în loc de ajustări de eșantionare.
- **Fine-tuning (lecția 18)** păstrează `gpt-4.1-mini`: GPT-5 suportă numai fine-tuning cu întărire (RFT), nu fine-tuning supravegheat (SFT) prezentat acolo.
- Lecțiile 20 (Mistral) și 21 (Meta) păstrează `temperature`/`max_tokens` pentru că țintesc modele Mistral/Llama, care le suportă.

### Executarea exemplelor Python

```bash
# Navigați la directorul lecției
cd 06-text-generation-apps/python

# Rulați un script Python
python aoai-app.py
```

### Executarea exemplelor TypeScript

```bash
# Navigați la directorul aplicației TypeScript
cd 06-text-generation-apps/typescript/recipe-app

# Construiți codul TypeScript
npm run build

# Rulați aplicația
npm start
```

### Executarea Jupyter Notebooks

```bash
# Porniți Jupyter în rădăcina depozitului
jupyter notebook

# Sau folosiți VS Code cu extensia Jupyter
```

### Lucrul cu tipuri diferite de lecții

- **Lecții „Learn”**: Se concentrează pe documentația README.md și concepte
- **Lecții „Build”**: Include exemple de cod funcționale în Python și TypeScript
- Fiecare lecție are un README.md cu teorie, explicații de cod și linkuri către conținut video

## Linii directoare pentru stilul codului

### Python

- Folosește `python-dotenv` pentru gestionarea variabilelor de mediu
- Importă biblioteca `openai` pentru interacțiuni cu API-ul
- Folosește `pylint` pentru linting (unele exemple includ `# pylint: disable=all` pentru simplitate)
- Urmează convențiile de denumire PEP 8
- Stochează credențialele API în fișierul `.env`, niciodată în cod

### TypeScript

- Folosește pachetul `dotenv` pentru variabile de mediu
- Configurarea TypeScript în `tsconfig.json` pentru fiecare aplicație
- Folosește pachetul `openai` pentru Azure OpenAI (direcționează clientul către endpoint-ul `/openai/v1/` și apelează `client.responses.create`); folosește `@azure-rest/ai-inference` pentru Microsoft Foundry Models
- Folosește `nodemon` pentru dezvoltare cu reîncărcare automată
- Construiește înainte de rulare: `npm run build` apoi `npm start`

### Convenții Generale

- Păstrează exemplele de cod simple și educaționale
- Include comentarii care explică conceptele cheie
- Codul fiecărei lecții ar trebui să fie autonom și executabil
- Folosește denumiri consistente: prefix `aoai-` pentru Azure OpenAI, `oai-` pentru OpenAI API, `githubmodels-` pentru Microsoft Foundry Models (prefix moștenit din era GitHub Models)

## Linii directoare pentru documentație

### Stil Markdown

- Toate URL-urile trebuie încadrate în format `[text](../../url)` fără spații suplimentare
- Link-urile relative trebuie să înceapă cu `./` sau `../`
- Toate link-urile către domenii Microsoft trebuie să includă ID de urmărire: `?WT.mc_id=academic-105485-koreyst`
- Evită localizările specifice pe țări în URL-uri (evită `/en-us/`)
- Imaginile sunt stocate în folderul `./images` cu denumiri descriptive
- Folosește caractere englezești, cifre și cratime în numele fișierelor

### Suport pentru traduceri

- Depozitul suportă peste 40 de limbi prin GitHub Actions automatizate
- Traducerile sunt stocate în directorul `translations/`
- Nu trimite traduceri parțiale
- Traducerile automate nu sunt acceptate
- Imaginile traduse sunt stocate în directorul `translated_images/`

## Testare și validare

### Verificări înainte de trimitere

Acest depozit folosește GitHub Actions pentru validare. Înainte de a trimite PR-uri:

1. **Verifică link-urile Markdown**:
   ```bash
   # Fluxul de lucru validate-markdown.yml verifică:
   # - Căi relative rupte
   # - Lipsa ID-urilor de urmărire pe căi
   # - Lipsa ID-urilor de urmărire pe URL-uri
   # - URL-uri cu localizare de țară
   # - URL-uri externe rupte
   ```

2. **Testare manuală**:
   - Testează exemplele Python: activează venv și rulează scripturile
   - Testează exemplele TypeScript: `npm install`, `npm run build`, `npm start`
   - Verifică configurarea corectă a variabilelor de mediu
   - Verifică dacă cheile API funcționează cu exemplele de cod

3. **Exemple de cod**:
   - Asigură-te că tot codul rulează fără erori
   - Testează cu ambele Azure OpenAI și API OpenAI când este aplicabil
   - Verifică dacă exemplele funcționează cu Microsoft Foundry Models acolo unde sunt suportate

### Fără teste automate

Acesta este un depozit educațional axat pe tutoriale și exemple. Nu există teste unitare sau de integrare de rulat. Validarea se face în principal prin:
- Testare manuală a exemplelor de cod
- GitHub Actions pentru validarea Markdown-ului
- Revizuire comunitară a conținutului educațional

## Linii directoare pentru Pull Request-uri

### Înainte de trimitere

1. Testează modificările de cod în Python și TypeScript când este cazul
2. Rulează validarea Markdown (se declanșează automat la PR)
3. Asigură-te că ID-urile de urmărire sunt prezente pe toate URL-urile Microsoft
4. Verifică validitatea link-urilor relative
5. Verifică dacă imaginile sunt referențiate corect

### Formatul titlului PR-ului

- Folosește titluri descriptive: `[Lesson 06] Corectare greșeală în exemplul Python` sau `Actualizare README pentru lecția 08`
- Referințe la numerele problemelor când este cazul: `Fixes #123`

### Descrierea PR-ului

- Explică ce a fost modificat și de ce
- Leagă problemele relevante
- Pentru modificări de cod, specifică ce exemple au fost testate
- Pentru PR-urile de traducere, include toate fișierele pentru o traducere completă

### Cerințe pentru contribuție

- Semnează CLA Microsoft (automat la primul PR)
- Fă fork la depozit în contul tău înainte de a face schimbări
- Un PR per schimbare logică (nu combina corecturi nelegate)
- Păstrează PR-urile concentrate și mici când este posibil

## Fluxuri de lucru Comune

### Adăugarea unui nou exemplu de cod

1. Navighează la directorul lecției corespunzătoare
2. Creează exemplul în subdirectorul `python/` sau `typescript/`
3. Urmează convenția de denumire: `{provider}-{example-name}.{py|ts|js}`
4. Testează cu credențiale API reale
5. Documentează orice variabile de mediu noi în README-ul lecției

### Actualizarea documentației

1. Editează README.md în directorul lecției
2. Urmează liniile directoare Markdown (ID-uri de urmărire, link-uri relative)
3. Actualizările traducerilor sunt gestionate de GitHub Actions (nu edita manual)
4. Testează dacă toate link-urile sunt valide

### Lucrul cu Dev Containers

1. Depozitul include `.devcontainer/devcontainer.json`
2. Scriptul post-creare instalează automat dependențele Python
3. Extensiile pentru Python și Jupyter sunt preconfigurate
4. Mediul este bazat pe `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Implementare și publicare

Acesta este un depozit de învățare - nu există un proces de implementare. Curriculum-ul este destinat pentru:

1. **Depozitul GitHub**: Acces direct la cod și documentație
2. **GitHub Codespaces**: Mediu de dezvoltare instant cu configurare predefinită
3. **Microsoft Learn**: Conținutul poate fi publicat pe platforma oficială de învățare
4. **docsify**: Site de documentație construit din Markdown (vezi `docsifytopdf.js` și `package.json`)

### Construirea site-ului de documentație

```bash
# Generează PDF din documentație (dacă este necesar)
npm run convert
```

## Depanare

### Probleme frecvente

**Erori de import Python**:
- Asigură-te că mediul virtual este activat
- Rulează `pip install -r requirements.txt`
- Verifică versiunea Python este 3.9+

**Erori de build TypeScript**:
- Rulează `npm install` în directorul aplicației specifice
- Verifică compatibilitatea versiunii Node.js
- Șterge `node_modules` și reinstalează dacă este necesar

**Erori de autentificare API**:
- Verifică dacă fișierul `.env` există și are valorile corecte
- Verifică dacă cheile API sunt valide și nu au expirat
- Asigură-te că URL-urile endpoint-ului sunt corecte pentru regiunea ta

**Variabile de mediu lipsă**:
- Copiază `.env.copy` în `.env`
- Completează toate valorile cerute pentru lecția la care lucrezi
- Repornește aplicația după actualizarea `.env`

## Resurse suplimentare

- [Ghid de configurare a cursului](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Linii directoare pentru contribuții](./CONTRIBUTING.md)
- [Codul de conduită](./CODE_OF_CONDUCT.md)
- [Politica de securitate](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Colecție de exemple avansate de cod](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Note specifice proiectului

- Acesta este un **depozit educațional** axat pe învățare, nu pe cod de producție
- Exemplele sunt intenționat simple și concentrate pe predarea conceptelor
- Calitatea codului este echilibrată cu claritatea educațională
- Fiecare lecție este autonomă și poate fi finalizată independent
- Depozitul suportă multiple furnizori API: Azure OpenAI, OpenAI, Microsoft Foundry Models și furnizori offline precum Foundry Local și Ollama
- Conținutul este multilingv cu fluxuri de lucru automate pentru traduceri
- Comunitate activă pe Discord pentru întrebări și suport

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->