<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:11:02+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ro"
}
-->
# AGENTS.md

## Prezentare Generală a Proiectului

Acest depozit conține un curriculum cuprinzător de 21 lecții care predă fundamentele AI Generativ și dezvoltarea aplicațiilor. Cursul este conceput pentru începători și acoperă totul, de la concepte de bază până la construirea aplicațiilor pregătite pentru producție.

**Tehnologii Cheie:**
- Python 3.9+ cu biblioteci: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript cu Node.js și biblioteci: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Serviciul Azure OpenAI, API-ul OpenAI și Modelele GitHub
- Jupyter Notebooks pentru învățare interactivă
- Containere de dezvoltare pentru un mediu de dezvoltare consistent

**Structura Depozitului:**
- 21 directoare de lecții numerotate (00-21) care conțin fișiere README, exemple de cod și teme
- Implementări multiple: Python, TypeScript și uneori exemple .NET
- Director de traduceri cu versiuni în peste 40 de limbi
- Configurație centralizată prin fișierul `.env` (folosiți `.env.copy` ca șablon)

## Comenzi de Configurare

### Configurarea Inițială a Depozitului

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Configurarea Mediului Python

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configurarea Node.js/TypeScript

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Configurarea Containerului de Dezvoltare (Recomandat)

Depozitul include o configurație `.devcontainer` pentru GitHub Codespaces sau VS Code Dev Containers:

1. Deschideți depozitul în GitHub Codespaces sau VS Code cu extensia Dev Containers
2. Containerul de dezvoltare va instala automat:
   - Dependențele Python din `requirements.txt`
   - Scriptul post-creare (`.devcontainer/post-create.sh`)
   - Kernel-ul Jupyter

## Flux de Lucru pentru Dezvoltare

### Variabile de Mediu

Toate lecțiile care necesită acces la API folosesc variabile de mediu definite în `.env`:

- `OPENAI_API_KEY` - Pentru API-ul OpenAI
- `AZURE_OPENAI_API_KEY` - Pentru Serviciul Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL-ul endpoint-ului Azure OpenAI
- `AZURE_OPENAI_DEPLOYMENT` - Numele implementării modelului de completare chat
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Numele implementării modelului de embeddings
- `AZURE_OPENAI_API_VERSION` - Versiunea API (implicit: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Pentru modelele Hugging Face
- `GITHUB_TOKEN` - Pentru Modelele GitHub

### Rularea Exemplului Python

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### Rularea Exemplului TypeScript

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Rularea Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Lucrul cu Diferite Tipuri de Lecții

- Lecțiile **"Learn"**: Se concentrează pe documentația README.md și concepte
- Lecțiile **"Build"**: Includ exemple de cod funcționale în Python și TypeScript
- Fiecare lecție are un README.md cu teorie, explicații ale codului și linkuri către conținut video

## Ghiduri de Stil pentru Cod

### Python

- Folosiți `python-dotenv` pentru gestionarea variabilelor de mediu
- Importați biblioteca `openai` pentru interacțiuni cu API-ul
- Folosiți `pylint` pentru verificarea codului (unele exemple includ `# pylint: disable=all` pentru simplitate)
- Respectați convențiile de denumire PEP 8
- Stocați acreditările API în fișierul `.env`, niciodată în cod

### TypeScript

- Folosiți pachetul `dotenv` pentru variabile de mediu
- Configurația TypeScript în `tsconfig.json` pentru fiecare aplicație
- Folosiți `@azure/openai` sau `@azure-rest/ai-inference` pentru serviciile Azure
- Folosiți `nodemon` pentru dezvoltare cu reîncărcare automată
- Compilați înainte de rulare: `npm run build` apoi `npm start`

### Convenții Generale

- Păstrați exemplele de cod simple și educative
- Includeți comentarii care explică conceptele cheie
- Codul fiecărei lecții trebuie să fie autonom și executabil
- Folosiți denumiri consistente: prefixul `aoai-` pentru Azure OpenAI, `oai-` pentru API-ul OpenAI, `githubmodels-` pentru Modelele GitHub

## Ghiduri de Documentare

### Stil Markdown

- Toate URL-urile trebuie să fie în formatul `[text](../../url)` fără spații suplimentare
- Linkurile relative trebuie să înceapă cu `./` sau `../`
- Toate linkurile către domeniile Microsoft trebuie să includă ID-ul de urmărire: `?WT.mc_id=academic-105485-koreyst`
- Fără locale specifice țării în URL-uri (evitați `/en-us/`)
- Imaginile stocate în folderul `./images` cu denumiri descriptive
- Folosiți caractere englezești, numere și cratime în denumirile fișierelor

### Suport pentru Traduceri

- Depozitul suportă peste 40 de limbi prin GitHub Actions automatizate
- Traducerile sunt stocate în directorul `translations/`
- Nu trimiteți traduceri parțiale
- Traducerile automate nu sunt acceptate
- Imaginile traduse sunt stocate în directorul `translated_images/`

## Testare și Validare

### Verificări înainte de trimitere

Acest depozit folosește GitHub Actions pentru validare. Înainte de a trimite PR-uri:

1. **Verificați Linkurile Markdown**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Testare Manuală**:
   - Testați exemplele Python: Activați venv și rulați scripturile
   - Testați exemplele TypeScript: `npm install`, `npm run build`, `npm start`
   - Verificați că variabilele de mediu sunt configurate corect
   - Asigurați-vă că cheile API funcționează cu exemplele de cod

3. **Exemple de Cod**:
   - Asigurați-vă că tot codul rulează fără erori
   - Testați atât cu Azure OpenAI, cât și cu API-ul OpenAI, când este aplicabil
   - Verificați că exemplele funcționează cu Modelele GitHub, unde sunt suportate

### Fără Teste Automatizate

Acesta este un depozit educațional axat pe tutoriale și exemple. Nu există teste unitare sau de integrare de rulat. Validarea este în principal:
- Testare manuală a exemplelor de cod
- GitHub Actions pentru validarea Markdown
- Revizuirea comunității a conținutului educațional

## Ghiduri pentru Pull Request-uri

### Înainte de Trimitere

1. Testați modificările codului atât în Python, cât și în TypeScript, când este aplicabil
2. Rulați validarea Markdown (declanșată automat pe PR)
3. Asigurați-vă că ID-urile de urmărire sunt prezente pe toate URL-urile Microsoft
4. Verificați că linkurile relative sunt valide
5. Verificați că imaginile sunt referite corect

### Formatul Titlului PR

- Folosiți titluri descriptive: `[Lesson 06] Fix Python example typo` sau `Update README for lesson 08`
- Referiți numerele problemelor, când este aplicabil: `Fixes #123`

### Descrierea PR

- Explicați ce a fost schimbat și de ce
- Link către problemele asociate
- Pentru modificările de cod, specificați ce exemple au fost testate
- Pentru PR-urile de traducere, includeți toate fișierele pentru o traducere completă

### Cerințe pentru Contribuție

- Semnați Microsoft CLA (automat la primul PR)
- Faceți fork depozitului în contul dvs. înainte de a face modificări
- Un PR per modificare logică (nu combinați remedieri fără legătură)
- Păstrați PR-urile concentrate și mici, când este posibil

## Fluxuri de Lucru Comune

### Adăugarea unui Nou Exemplu de Cod

1. Navigați la directorul lecției corespunzătoare
2. Creați exemplul în subdirectorul `python/` sau `typescript/`
3. Respectați convenția de denumire: `{provider}-{example-name}.{py|ts|js}`
4. Testați cu acreditări API reale
5. Documentați orice variabile de mediu noi în README-ul lecției

### Actualizarea Documentației

1. Editați README.md în directorul lecției
2. Respectați ghidurile Markdown (ID-uri de urmărire, linkuri relative)
3. Actualizările traducerilor sunt gestionate de GitHub Actions (nu editați manual)
4. Testați toate linkurile pentru validitate

### Lucrul cu Containere de Dezvoltare

1. Depozitul include `.devcontainer/devcontainer.json`
2. Scriptul post-creare instalează automat dependențele Python
3. Extensiile pentru Python și Jupyter sunt pre-configurate
4. Mediul se bazează pe `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Implementare și Publicare

Acesta este un depozit de învățare - nu există un proces de implementare. Curriculum-ul este consumat prin:

1. **Depozitul GitHub**: Acces direct la cod și documentație
2. **GitHub Codespaces**: Mediu de dezvoltare instant cu configurare predefinită
3. **Microsoft Learn**: Conținutul poate fi distribuit pe platforma oficială de învățare
4. **docsify**: Site de documentație construit din Markdown (vezi `docsifytopdf.js` și `package.json`)

### Construirea Site-ului de Documentație

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Depanare

### Probleme Comune

**Erori de Import Python**:
- Asigurați-vă că mediul virtual este activat
- Rulați `pip install -r requirements.txt`
- Verificați că versiunea Python este 3.9+

**Erori de Compilare TypeScript**:
- Rulați `npm install` în directorul aplicației specifice
- Verificați că versiunea Node.js este compatibilă
- Goliți `node_modules` și reinstalați, dacă este necesar

**Erori de Autentificare API**:
- Verificați că fișierul `.env` există și are valori corecte
- Verificați că cheile API sunt valide și nu au expirat
- Asigurați-vă că URL-urile endpoint-urilor sunt corecte pentru regiunea dvs.

**Variabile de Mediu Lipsă**:
- Copiați `.env.copy` în `.env`
- Completați toate valorile necesare pentru lecția la care lucrați
- Reporniți aplicația după actualizarea `.env`

## Resurse Suplimentare

- [Ghid de Configurare a Cursului](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Ghiduri de Contribuție](./CONTRIBUTING.md)
- [Cod de Conduită](./CODE_OF_CONDUCT.md)
- [Politica de Securitate](./SECURITY.md)
- [Discord Azure AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Colecție de Exemple de Cod Avansate](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Note Specifice Proiectului

- Acesta este un **depozit educațional** axat pe învățare, nu pe cod de producție
- Exemplele sunt intenționat simple și axate pe predarea conceptelor
- Calitatea codului este echilibrată cu claritatea educațională
- Fiecare lecție este autonomă și poate fi completată independent
- Depozitul suportă mai mulți furnizori de API: Azure OpenAI, OpenAI și Modelele GitHub
- Conținutul este multilingv, cu fluxuri de lucru automate de traducere
- Comunitate activă pe Discord pentru întrebări și suport

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.