# AGENTS.md

## Prezentare generală a proiectului

Acest depozit conține un curriculum cuprinzător de 21 de lecții care predau noțiunile fundamentale ale Inteligenței Artificiale Generative și dezvoltarea aplicațiilor. Cursul este conceput pentru începători și acoperă totul, de la conceptele de bază până la construirea aplicațiilor gata de producție.

**Tehnologii cheie:**
- Python 3.9+ cu biblioteci: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript cu Node.js și biblioteci: `openai` (Azure OpenAI prin endpoint-ul v1 + Responses API), `@azure-rest/ai-inference` (Modele Microsoft Foundry)
- Azure OpenAI Service, OpenAI API și Modele Microsoft Foundry (GitHub Models se retrage la sfârșitul lui iulie 2026)
- Jupyter Notebooks pentru învățare interactivă
- Containere Dev pentru mediu de dezvoltare consistent

**Structura depozitului:**
- 21 directoare numerotate corespunzător lecțiilor (00-21) care conțin fișiere README, exemple de cod și teme
- Mai multe implementări: exemple în Python, TypeScript și uneori .NET
- Director pentru traduceri cu peste 40 de versiuni în diferite limbi
- Configurare centralizată prin fișier `.env` (folosiți `.env.copy` ca șablon)

## Comenzi de configurare

### Configurare inițială a depozitului

```bash
# Clonați depozitul
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copiați șablonul de mediu
cp .env.copy .env
# Editează .env cu cheile API și punctele finale
```

### Configurare mediu Python

```bash
# Creează un mediu virtual
python3 -m venv venv

# Activează mediul virtual
# Pe macOS/Linux:
source venv/bin/activate
# Pe Windows:
venv\Scripts\activate

# Instalează dependențele
pip install -r requirements.txt
```

### Configurare Node.js/TypeScript

```bash
# Instalează dependențele la nivel de root (pentru instrumentele de documentație)
npm install

# Pentru exemple TypeScript din lecții individuale, navigați către lecția specifică:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Configurare Dev Container (Recomandat)

Depozitul include o configurație `.devcontainer` pentru GitHub Codespaces sau VS Code Dev Containers:

1. Deschideți depozitul în GitHub Codespaces sau VS Code cu extensia Dev Containers
2. Dev Container va face automat:
   - Instalarea dependențelor Python din `requirements.txt`
   - Executarea scriptului post-creare (`.devcontainer/post-create.sh`)
   - Configurarea nucleului Jupyter

## Flux de lucru pentru dezvoltare

### Variabile de mediu

Toate lecțiile care necesită acces la API folosesc variabile de mediu definite în `.env`:

- `OPENAI_API_KEY` - Pentru OpenAI API
- `AZURE_OPENAI_API_KEY` - Pentru Azure OpenAI în Microsoft Foundry (Azure OpenAI Service este acum parte din Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL-ul endpoint-ului Azure OpenAI (endpoint resursă Foundry)
- `AZURE_OPENAI_DEPLOYMENT` - Numele implementării modelului pentru completare chat
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Numele implementării modelului embeddings
- `AZURE_OPENAI_API_VERSION` - Versiunea API (implicit: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Pentru modelele Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - Endpoint-ul modelelelor Microsoft Foundry (catalog multi-provider)
- `AZURE_INFERENCE_CREDENTIAL` - Cheie API Microsoft Foundry Models (înlocuiește `GITHUB_TOKEN` care se retrage)

### Rularea exemplelor Python

```bash
# Navigați la directorul lecției
cd 06-text-generation-apps/python

# Rulați un script Python
python aoai-app.py
```

### Rularea exemplelor TypeScript

```bash
# Navighează la directorul aplicației TypeScript
cd 06-text-generation-apps/typescript/recipe-app

# Compilează codul TypeScript
npm run build

# Rulează aplicația
npm start
```

### Rularea Jupyter Notebooks

```bash
# Pornește Jupyter în directorul rădăcină al depozitului
jupyter notebook

# Sau folosește VS Code cu extensia Jupyter
```

### Lucrul cu tipuri diferite de lecții

- Lecțiile **"Learn"**: Se concentrează pe documentația README.md și concepte
- Lecțiile **"Build"**: Include exemple funcționale de cod în Python și TypeScript
- Fiecare lecție are un README.md cu teorie, explicații de cod și linkuri către conținut video

## Ghiduri de stil pentru cod

### Python

- Folosiți `python-dotenv` pentru gestionarea variabilelor de mediu
- Importați biblioteca `openai` pentru interacțiuni cu API
- Folosiți `pylint` pentru linting (unele exemple includ `# pylint: disable=all` pentru simplitate)
- Urmați convențiile de denumire PEP 8
- Stocați acreditările API în fișierul `.env`, niciodată în cod

### TypeScript

- Folosiți pachetul `dotenv` pentru variabile de mediu
- Configurație TypeScript în `tsconfig.json` pentru fiecare aplicație
- Folosiți pachetul `openai` pentru Azure OpenAI (direcționați clientul către endpoint-ul `/openai/v1/` și apelați `client.responses.create`); folosiți `@azure-rest/ai-inference` pentru modelele Microsoft Foundry
- Folosiți `nodemon` pentru dezvoltare cu auto-reîncărcare
- Compilați înainte de rulare: `npm run build` apoi `npm start`

### Convenții generale

- Păstrați exemplele de cod simple și educative
- Includeți comentarii care explică conceptele cheie
- Codul fiecărei lecții trebuie să fie autonom și rulabil
- Folosiți o denumire consistentă: prefix `aoai-` pentru Azure OpenAI, `oai-` pentru OpenAI API, `githubmodels-` pentru Microsoft Foundry Models (prefixul moștenit din era GitHub Models)

## Ghiduri pentru documentație

### Stil Markdown

- Toate URL-urile trebuie învelite în formatul `[text](../../url)` fără spații suplimentare
- Link-urile relative trebuie să înceapă cu `./` sau `../`
- Toate link-urile către domenii Microsoft trebuie să includă ID de urmărire: `?WT.mc_id=academic-105485-koreyst`
- Evitați localele specifice țărilor în URL-uri (evitați `/en-us/`)
- Imaginile sunt stocate în folderul `./images` cu nume descriptive
- Folosiți caractere englezești, cifre și cratime în denumirile fișierelor

### Suport pentru traduceri

- Depozitul suportă peste 40 de limbi prin GitHub Actions automatizate
- Traducerile sunt stocate în directorul `translations/`
- Nu trimiteți traduceri parțiale
- Traducerile automate (machine translations) nu sunt acceptate
- Imaginile traduse sunt stocate în directorul `translated_images/`

## Testare și validare

### Verificări înainte de trimitere

Acest depozit folosește GitHub Actions pentru validare. Înainte de a trimite pull requests:

1. **Verificați link-urile Markdown**:
   ```bash
   # Fluxul de lucru validate-markdown.yml verifică:
   # - Căi relative rupte
   # - ID-uri de urmărire lipsă pe căi
   # - ID-uri de urmărire lipsă pe URL-uri
   # - URL-uri cu localizare pe țară
   # - URL-uri externe rupte
   ```

2. **Testare manuală**:
   - Testați exemplele Python: activați venv și rulați scripturile
   - Testați exemplele TypeScript: `npm install`, `npm run build`, `npm start`
   - Verificați dacă variabilele de mediu sunt configurate corect
   - Asigurați-vă că cheile API funcționează cu exemplele de cod

3. **Exemple de cod**:
   - Asigurați-vă că tot codul rulează fără erori
   - Testați atât cu Azure OpenAI, cât și cu OpenAI API când este aplicabil
   - Verificați că exemplele funcționează și cu modelele Microsoft Foundry unde sunt suportate

### Fără teste automate

Acesta este un depozit educațional concentrat pe tutoriale și exemple. Nu există teste unitare sau de integrare de rulat. Validarea constă în principal în:
- Testare manuală a exemplelor de cod
- GitHub Actions pentru validarea Markdown
- Recenzie comunitară a conținutului educațional

## Ghiduri pentru Pull Requests

### Înainte de trimitere

1. Testați modificările de cod atât în Python, cât și în TypeScript când este cazul
2. Rulați validarea Markdown (activată automat la PR)
3. Asigurați prezența ID-urilor de tracking pe toate URL-urile Microsoft
4. Verificați că link-urile relative sunt valide
5. Verificați că imaginile sunt referențiate corect

### Formatul titlului PR

- Folosiți titluri descriptive: `[Lesson 06] Corectare greșeală exemplu Python` sau `Actualizare README pentru lecția 08`
- Referențiați numerele issue-urilor când este cazul: `Fixes #123`

### Descrierea PR

- Explicați ce s-a schimbat și de ce
- Includeți linkuri către issue-uri aferente
- Pentru modificări de cod, specificați care exemple au fost testate
- Pentru PR-uri de traducere, includeți toate fișierele pentru o traducere completă

### Cerințe pentru contribuții

- Semnați CLA Microsoft (automat la primul PR)
- Dați fork depozitului în contul dvs. înainte de a face modificări
- Un singur PR per schimbare logică (nu combinați corecturi nelegate)
- Mențineți PR-urile concentrate și mici când este posibil

## Fluxuri comune de lucru

### Adăugarea unui exemplu nou de cod

1. Navigați la directorul lecției corespunzătoare
2. Creați exemplul în subdirectorul `python/` sau `typescript/`
3. Urmați convenția de denumire: `{provider}-{example-name}.{py|ts|js}`
4. Testați cu acreditările API reale
5. Documentați orice variabilă nouă de mediu în README-ul lecției

### Actualizarea documentației

1. Editează README.md din directorul lecției
2. Urmați ghidurile Markdown (ID-uri de tracking, link-uri relative)
3. Actualizările traducerilor sunt gestionate de GitHub Actions (nu editați manual)
4. Testați că toate link-urile sunt valide

### Lucrul cu Dev Containers

1. Depozitul include `.devcontainer/devcontainer.json`
2. Scriptul post-creare instalează automat dependențele Python
3. Extensiile pentru Python și Jupyter sunt preconfigurate
4. Mediul se bazează pe `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Implementare și publicare

Acesta este un depozit de învățare - nu există proces de implementare. Curriculumul este accesat prin:

1. **Depozitul GitHub**: Acces direct la cod și documentație
2. **GitHub Codespaces**: Mediu instant de dezvoltare cu configurație predefinită
3. **Microsoft Learn**: Conținut care poate fi redistribuit pe platforma oficială de învățare
4. **docsify**: Site de documentație construit din Markdown (vezi `docsifytopdf.js` și `package.json`)

### Construirea site-ului de documentație

```bash
# Generează PDF din documentație (dacă este necesar)
npm run convert
```

## Depanare

### Probleme comune

**Erori de import Python**:
- Asigurați-vă că mediul virtual este activat
- Rulați `pip install -r requirements.txt`
- Verificați să fie versiunea Python 3.9+

**Erori de build TypeScript**:
- Rulați `npm install` în directorul specific aplicației
- Verificați că versiunea Node.js este compatibilă
- Ștergeți `node_modules` și reinstalați dacă este necesar

**Erori de autentificare API**:
- Verificați dacă fișierul `.env` există și are valori corecte
- Verificați că cheile API sunt valide și neexpirate
- Asigurați-vă că URL-urile endpoint-ului sunt corecte pentru regiunea dvs.

**Variabile de mediu lipsă**:
- Copiați `.env.copy` în `.env`
- Completați toate valorile necesare pentru lecția pe care lucrați
- Reporniti aplicația după actualizarea `.env`

## Resurse suplimentare

- [Ghid de configurare curs](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Ghid de contribuție](./CONTRIBUTING.md)
- [Cod de conduită](./CODE_OF_CONDUCT.md)
- [Politica de securitate](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Colecție de exemple avansate de cod](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Note specifice proiectului

- Acesta este un **depozit educațional** axat pe învățare, nu pe cod de producție
- Exemplele sunt intenționat simple și concentrate pe predarea conceptelor
- Calitatea codului este echilibrată cu claritatea educațională
- Fiecare lecție este autonomă și poate fi finalizată independent
- Depozitul suportă mai mulți furnizori API: Azure OpenAI, OpenAI, Microsoft Foundry Models și furnizori offline precum Foundry Local și Ollama
- Conținutul este multilingv cu fluxuri automate de traducere
- Comunitate activă pe Discord pentru întrebări și suport

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->