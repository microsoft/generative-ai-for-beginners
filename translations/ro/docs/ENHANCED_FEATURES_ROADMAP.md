# Foia de Parcurs pentru Funcționalități Îmbunătățite și Dezvoltări

Acest document prezintă îmbunătățirile și dezvoltările recomandate pentru curriculumul Generative AI for Beginners, bazate pe o revizuire detaliată a codului și o analiză a celor mai bune practici din industrie.

## Rezumat Executiv

Codul a fost analizat în ceea ce privește securitatea, calitatea codului și eficacitatea educațională. Acest document oferă recomandări pentru remedieri imediate, îmbunătățiri pe termen scurt și dezvoltări viitoare.

---

## 1. Îmbunătățiri de Securitate (Prioritate: Critică)

### 1.1 Remedieri Imediate (Finalizate)

| Problemă | Fișiere Afectate | Stare |
|-------|----------------|--------|
| SECRET_KEY hardcodat | `05-advanced-prompts/python/aoai-solution.py` | Remediat |
| Lipsă validare mediu | Mai multe fișiere JS/TS | Remediat |
| Apeluri de funcții nesigure | `11-integrating-with-function-calling/js-githubmodels/app.js` | Remediat |
| Scurgeri de handle fișiere | `08-building-search-applications/scripts/` | Remediat |
| Lipsă timeout-uri pentru solicitări | `09-building-image-applications/python/` | Remediat |

### 1.2 Caracteristici suplimentare de securitate recomandate

1. **Exemple de limitare a ratei**
   - Adăugați cod exemplu pentru implementarea limitării ratei la apelurile API
   - Demonstrați modele de backoff exponențial

2. **Rotirea cheilor API**
   - Adăugați documentație privind cele mai bune practici pentru rotirea cheilor API
   - Includeți exemple de utilizare a Azure Key Vault sau servicii similare

3. **Integrarea siguranței conținutului**
   - Adăugați exemple folosind Azure Content Safety API
   - Demonstrați modele de moderare pentru input/output

---

## 2. Îmbunătățiri ale Calității Codului

### 2.1 Fișiere de Configurare Adăugate

| Fișier | Scop |
|------|---------|
| `.eslintrc.json` | Reguli de linting JavaScript/TypeScript |
| `.prettierrc` | Standardele de formatare a codului |
| `pyproject.toml` | Configurarea uneltelor Python (Black, Ruff, mypy) |

### 2.2 Utilitare Comune Create

Nou modul `shared/python/` cu:
- `env_utils.py` - Gestionarea variabilelor de mediu
- `input_validation.py` - Validarea și sanitizarea inputurilor
- `api_utils.py` - Învelitori sigure pentru cererile API

### 2.3 Îmbunătățiri Recomandate ale Codului

1. **Acoperire cu tipuri**
   - Adăugați adnotări de tip la toate fișierele Python
   - Activați modul strict TypeScript pentru toate proiectele TS

2. **Standarde pentru documentație**
   - Adăugați docstrings pentru toate funcțiile Python
   - Adăugați comentarii JSDoc pentru toate funcțiile JavaScript/TypeScript

3. **Cadru de testare**
   - Adăugați configurație pytest și teste exemplu _(finalizat: configurație pytest în `pyproject.toml`; teste exemplu pentru utilitarele comune în [`tests/`](../../../tests) rulate în CI)_
   - Adăugați configurație Jest pentru JavaScript/TypeScript

---

## 3. Îmbunătățiri Educaționale

### 3.1 Subiecte Noi ale Lecțiilor

1. **Securitatea în aplicațiile AI** (Lecția propusă 22)
   - Atacuri de injecție de prompt și contramăsuri
   - Gestionarea cheilor API
   - Moderarea conținutului
   - Limitarea ratei și prevenirea abuzurilor

2. **Dezvoltare în producție** (Lecția propusă 23)
   - Containerizare cu Docker
   - Pipeline-uri CI/CD
   - Monitorizare și logging
   - Gestionarea costurilor

3. **Tehnici avansate RAG** (Lecția propusă 24)
   - Căutare hibridă (cuvânt cheie + semantic)
   - Strategii de re-ranking
   - RAG multimodal
   - Metrici de evaluare

### 3.2 Îmbunătățiri ale Lecțiilor Existente

| Lecție | Îmbunătățire Recomandată |
|--------|------------------------|
| 06 - Generare Text | Adăugați exemple de răspuns în streaming |
| 07 - Aplicații de chat | Adăugați modele de memorie pentru conversații |
| 08 - Aplicații de căutare | Adăugați comparație de baze de date vectoriale |
| 09 - Generare imagine | Adăugați exemple de editare/variație a imaginii |
| 11 - Apelare de funcții | Adăugați apelare paralelă de funcții |
| 15 - RAG | Adăugați comparație de strategii de împărțire pe bucăți |
| 17 - Agenți AI | Adăugați orchestrare multi-agent |

---

## 4. Modernizarea API-ului

### 4.1 Modele API deprecate (Migrare finalizată)

Toate exemplele Python și TypeScript pentru **chat** au fost migrate de la Chat Completions API la **Responses API** (`client.responses.create(...)` → `response.output_text`).

| Model Vechi | Model Nou | Stare |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (chat) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | Finalizat |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | Finalizat |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | pachetul `openai` `client.responses.create()` → `response.output_text` | Finalizat |
| `df.append()` (pandas) | `pd.concat()` | Finalizat |

> **Notă:** Exemplele Microsoft Foundry Models care folosesc SDK-ul `azure-ai-inference` / `@azure-rest/ai-inference` (`client.complete()`) rămân pe Model Inference API, care nu suportă Responses API. `AzureOpenAI()` este păstrat intenționat unde este încă valabil (embedding-uri și generare de imagini).

### 4.2 Caracteristici noi ale API-ului de demonstrat

1. **Ieșiri structurate** (OpenAI)
   - Modul JSON
   - Apel de funcții cu scheme stricte

2. **Capabilități vizuale**
   - Analiza imaginilor cu GPT-4o (vision)
   - Prompts multimodale

3. **Instrumente încorporate în Responses API** (înlocuiește vechiul Assistants API)
   - Interpret de cod
   - Căutare fișiere
   - Căutare web și instrumente personalizate

---

## 5. Îmbunătățiri de Infrastructură

### 5.1 Îmbunătățiri CI/CD

Implementat în [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): linting/formatare Python (Ruff + Black) este **impus** pe modulul de utilitare `shared/` întreținut și rulează **consultativ** pe restul curriculumului, plus o trecere consultativă ESLint pentru JavaScript/TypeScript. Linia de bază ilustrativă a fost:

```yaml
# .github/workflows/code-quality.yml
name: Code Quality

on: [push, pull_request]

jobs:
  python-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - run: pip install ruff black mypy
      - run: ruff check .
      - run: black --check .

  js-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npx eslint .
```

### 5.2 Scanare de securitate

Implementat în [`.github/workflows/security.yml`](../../../.github/workflows/security.yml): analiză CodeQL pentru Python și JavaScript/TypeScript (la push, pull request și program săptămânal) plus o revizuire a dependențelor pe pull requests. Linia de bază ilustrativă a fost:

```yaml
# .github/workflows/security.yml
name: Security Scan

on: [push, pull_request]

jobs:
  codeql:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: javascript, python
      - uses: github/codeql-action/analyze@v3

  dependency-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/dependency-review-action@v4
```

---

## 6. Îmbunătățiri ale Experienței Dezvoltatorului

### 6.1 Îmbunătățiri DevContainer

Implementat în [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) și [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): containerul include acum extensiile Pylance, Black formatter, Ruff, ESLint, Prettier și Copilot, activează formatarea la salvare conectată la configurația Black/Prettier a depozitului și instalează uneltele de dezvoltare (`ruff`, `black`, `mypy`, `pytest`) pentru a reproduce acasă workflow-ul [code-quality](../../../.github/workflows/code-quality.yml). Imaginea de bază `mcr.microsoft.com/devcontainers/universal` include deja Python și Node, deci nu sunt necesare caracteristici suplimentare. Linia de bază ilustrativă a fost:

```json
{
  "name": "Generative AI for Beginners",
  "image": "mcr.microsoft.com/devcontainers/universal:2",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.11"
    },
    "ghcr.io/devcontainers/features/node:1": {
      "version": "20"
    }
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-toolsai.jupyter",
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "github.copilot"
      ],
      "settings": {
        "python.formatting.provider": "black",
        "editor.formatOnSave": true
      }
    }
  },
  "postCreateCommand": "pip install -e .[dev] && npm install"
}
```

### 6.2 Teren de joacă interactiv

Luați în considerare adăugarea:
- Notebook-uri Jupyter cu chei API pre-completate (prin mediu)
- Demo-uri Gradio/Streamlit pentru învățare vizuală
- Chestionare interactive pentru evaluarea cunoștințelor

---

## 7. Suport Multilingv

### 7.1 Acoperirea lingvistică curentă

| Tehnologie | Lecții acoperite | Stare |
|------------|-----------------|--------|
| Python | Toate | Complet |
| TypeScript | 06-09, 11 | Parțial |
| JavaScript | 06-08, 11 | Parțial |
| .NET/C# | Unele | Parțial |

### 7.2 Adăugiri recomandate

1. **Go** - Creștere în uneltele AI/ML
2. **Rust** - Aplicații critice pentru performanță
3. **Java/Kotlin** - Aplicații enterprise

---

## 8. Optimizări de Performanță

### 8.1 Optimizări la nivel de cod

1. **Modele Async/Await**
   - Adăugați exemple async pentru procesare în batch
   - Demonstrați apeluri API concurente

2. **Strategii de caching**
   - Adăugați exemple de caching pentru embedding-uri
   - Demonstrați modele de caching pentru răspunsuri

3. **Optimizare de tokeni**
   - Adăugați exemple de utilizare tiktoken
   - Demonstrați tehnici de compresie a promptului

### 8.2 Exemple de optimizare a costurilor

Adăugați exemple care demonstrează:
- Selectarea modelului în funcție de complexitatea sarcinii
- Ingineria promptului pentru eficiență în tokeni
- Procesarea în batch pentru operațiuni în masă

---

## 9. Accesibilitate și Internaționalizare

### 9.1 Stadiul traducerilor curente

Toate traducerile sunt **complete** și generate automat de [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst), care produce și menține sincronizate peste 50 de versiuni lingvistice ale curriculumului cu sursa în engleză. Conținutul tradus este sub `translations/` și imaginile localizate sub `translated_images/`; lista completă a limbilor disponibile este publicată în partea de sus a README-ului din depozit.

| Aspect | Stare |
|--------|--------|
| Acoperire traduceri | Completă — peste 50 de limbi, toate lecțiile |
| Metoda traducerii | Automatizată prin [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) |
| Menținut sincronizat cu sursa în engleză | Da — regenerat automat |

### 9.2 Îmbunătățiri pentru accesibilitate

1. Adăugați text alternativ tuturor imaginilor
2. Asigurați evidențierea sintaxei pentru exemple de cod
3. Adăugați transcrieri video pentru tot conținutul video
4. Asigurați contrastul culorilor conform ghidurilor WCAG

---

## 10. Prioritatea Implementării

### Faza 1: Imediat (Săptămânile 1-2)
- [x] Remediați probleme critice de securitate
- [x] Adăugați configurații pentru calitatea codului
- [x] Creați utilitare comune
- [x] Documentați ghidurile de securitate

### Faza 2: Pe termen scurt (Săptămânile 3-4)
- [x] Actualizați modelele API deprecate (Chat Completions → Responses API, Python + TypeScript)
- [ ] Adăugați adnotări de tip la toate fișierele Python (finalizat pentru modulul `shared/`; exemplele din lecții au fost păstrate simple)
- [x] Adăugați workflow-uri CI/CD pentru calitatea codului
- [x] Creați workflow pentru scanare de securitate

### Faza 3: Pe termen mediu (Lunile 2-3)
- [ ] Adăugați lecția nouă de securitate
- [ ] Adăugați lecția de dezvoltare în producție
- [x] Îmbunătățiți configurarea DevContainer
- [ ] Adăugați demo-uri interactive

### Faza 4: Pe termen lung (Luna 4+)
- [ ] Adăugați lecția avansată RAG
- [ ] Extindeți suportul lingvistic
- [ ] Adăugați o suită completă de teste
- [ ] Creați program de certificare

---

## Concluzie

Această foaie de parcurs oferă o abordare structurată pentru îmbunătățirea curriculumului Generative AI for Beginners. Prin abordarea preocupărilor de securitate, modernizarea API-urilor și adăugarea de conținut educațional, cursul va pregăti mai bine studenții pentru dezvoltarea aplicațiilor AI în lumea reală.

Pentru întrebări sau contribuții, vă rugăm să deschideți o problemă pe depozitul GitHub.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->