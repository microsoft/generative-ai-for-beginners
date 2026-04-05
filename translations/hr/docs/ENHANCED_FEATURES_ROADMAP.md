# Plan poboljšanih značajki i unapređenja

Ovaj dokument sažima preporučena poboljšanja i unapređenja za nastavni program Generativna AI za početnike, na temelju detaljne revizije koda i analize najboljih industrijskih praksi.

## Izvršni sažetak

Kodna baza je analizirana s aspekta sigurnosti, kvalitete koda i edukativne učinkovitosti. Ovaj dokument daje preporuke za hitne popravke, kratkoročna poboljšanja i buduće nadogradnje.

---

## 1. Poboljšanja sigurnosti (Prioritet: Kritično)

### 1.1 Hitni popravci (Dovršeno)

| Problem | Datoteke | Status |
|---------|----------|--------|
| Hardkodirani SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Popravljeno |
| Nedostaje provjera env varijabli | Više JS/TS datoteka | Popravljeno |
| Nesigurni pozivi funkcija | `11-integrating-with-function-calling/js-githubmodels/app.js` | Popravljeno |
| Curjenje file handle-a | `08-building-search-applications/scripts/` | Popravljeno |
| Nedostaju timeouti za requeste | `09-building-image-applications/python/` | Popravljeno |

### 1.2 Preporučene dodatne sigurnosne značajke

1. **Primjeri ograničavanja broja poziva (Rate Limiting)**
   - Dodati primjere koda za implementaciju ograničenja korištenja API poziva
   - Demonstrirati obrasce eksponencijalnog vraćanja natrag (exponential backoff)

2. **Rotacija API ključeva**
   - Dodati dokumentaciju o najboljim praksama rotacije API ključeva
   - Uključiti primjere korištenja Azure Key Vaulta ili sličnih servisa

3. **Integracija sigurnosti sadržaja**
   - Dodati primjere s Azure Content Safety API-jem
   - Demonstrirati obrasce moderacije ulaznih/izlaznih podataka

---

## 2. Poboljšanja kvalitete koda

### 2.1 Dodani konfiguracijski fajlovi

| Datoteka | Svrha |
|----------|--------|
| `.eslintrc.json` | Pravila za lintanje JavaScript/TypeScript |
| `.prettierrc` | Standardi formatiranja koda |
| `pyproject.toml` | Konfiguracija Python alata (Black, Ruff, mypy) |

### 2.2 Kreirane zajedničke komponente

Novi `shared/python/` modul s:
- `env_utils.py` - Rukovanje varijablama okoline
- `input_validation.py` - Validacija i sanitizacija ulaza
- `api_utils.py` - Sigurni omotači za API pozive

### 2.3 Preporučena poboljšanja koda

1. **Pokriće tipovima (type hints)**
   - Dodati type hintove u sve Python datoteke
   - Omogućiti strogi način rada (strict mode) u svim TypeScript projektima

2. **Standardi dokumentacije**
   - Dodati docstringove za sve Python funkcije
   - Dodati JSDoc komentare za sve JavaScript/TypeScript funkcije

3. **Okvir za testiranje**
   - Dodati pytest konfiguraciju i primjere testova
   - Dodati Jest konfiguraciju za JavaScript/TypeScript

---

## 3. Edukativna poboljšanja

### 3.1 Nove teme lekcija

1. **Sigurnost u AI aplikacijama** (Predložena lekcija 22)
   - Napadi injektiranja promptova i obrane
   - Upravljanje API ključevima
   - Moderacija sadržaja
   - Ograničavanje upotrebe i prevencija zloupotrebe

2. **Produkcijsko postavljanje** (Predložena lekcija 23)
   - Kontejnerizacija s Dockerom
   - CI/CD pipelinei
   - Praćenje i logiranje
   - Upravljanje troškovima

3. **Napredne RAG tehnike** (Predložena lekcija 24)
   - Hibridna pretraga (ključna riječ + semantička)
   - Strategije ponovnog rangiranja
   - Multi-modalni RAG
   - Metodologije evaluacije

### 3.2 Poboljšanja postojećih lekcija

| Lekcija | Preporučeno poboljšanje |
|---------|-------------------------|
| 06 - Generiranje teksta | Dodati primjere streaming odgovora |
| 07 - Chat aplikacije | Dodati obrasce memorije razgovora |
| 08 - Pretraživačke aplikacije | Dodati usporedbu vektorskih baza podataka |
| 09 - Generiranje slika | Dodati primjere uređivanja/varijacija slika |
| 11 - Pozivanje funkcija | Dodati paralelno pozivanje funkcija |
| 15 - RAG | Dodati usporedbu strategija segmentiranja |
| 17 - AI agenti | Dodati orkestraciju s više agenata |

---

## 4. Modernizacija API-ja

### 4.1 Zastarjeli obrasci API-ja koje treba ažurirati

| Stari obrazac | Novi obrazac | Datoteke |
|---------------|-------------|----------|
| `openai.api_type = "azure"` | `AzureOpenAI()` klijent | Više skripti u `08-building-search-applications/` |
| `openai.ChatCompletion.create()` | `client.chat.completions.create()` | Više bilježnica |
| `df.append()` (pandas) | `pd.concat()` | RAG bilježnica |

### 4.2 Nove značajke API-ja za demonstraciju

1. **Strukturirani izlazi** (OpenAI)
   - JSON način rada
   - Pozivanje funkcija sa strogo definiranim šemama

2. **Vizijske mogućnosti**
   - Analiza slika s GPT-4V
   - Multi-modalni promptovi

3. **Assistants API**
   - Interpreter koda
   - Pretraživanje datoteka
   - Prilagođeni alati

---

## 5. Infrastrukturna poboljšanja

### 5.1 CI/CD unaprjeđenja

Trenutni workflowi pokrivaju provjeru markdown sintakse. Preporučeni dodaci:

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

### 5.2 Sigurnosno skeniranje

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

## 6. Poboljšanja iskustva programera

### 6.1 Poboljšanja DevContainera

Ažurirati `.devcontainer/devcontainer.json`:

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

### 6.2 Interaktivno okruženje

Razmotriti dodavanje:
- Jupyter bilježnica s unaprijed postavljenim API ključevima (putem okoliša)
- Gradio/Streamlit demo primjera za vizualne učenike
- Interaktivnih kvizova za procjenu znanja

---

## 7. Podrška za više jezika

### 7.1 Trenutno pokrivanje jezika

| Tehnologija | Lekcije | Status |
|-------------|---------|--------|
| Python | Sve | Potpuno |
| TypeScript | 06-09, 11 | Djelomično |
| JavaScript | 06-08, 11 | Djelomično |
| .NET/C# | Neke | Djelomično |

### 7.2 Preporučeni dodaci

1. **Go** - Rast u AI/ML alatima
2. **Rust** - Aplikacije zahtjevne za performanse
3. **Java/Kotlin** - Enterprise aplikacije

---

## 8. Optimizacija performansi

### 8.1 Optimizacije na razini koda

1. **Async/Await obrasci**
   - Dodati async primjere za batch obradu
   - Demonstrirati konkurentne API pozive

2. **Strategije keširanja**
   - Dodati primjere keširanja embeddinga
   - Demonstrirati obrasce keširanja odgovora

3. **Optimizacija tokena**
   - Dodati primjere korištenja tiktoken
   - Demonstrirati tehnike kompresije promptova

### 8.2 Primjeri optimizacije troškova

Dodati primjere za:
- Odabir modela prema složenosti zadatka
- Inženjering promptova za efikasnost tokena
- Batch obradu za puno operacija

---

## 9. Pristupačnost i internacionalizacija

### 9.1 Trenutni status prijevoda

| Jezik | Status |
|--------|--------|
| Engleski | Potpuno |
| Kineski (pojednostavljeni) | Potpuno |
| Japanski | Potpuno |
| Korejski | Potpuno |
| Španjolski | Djelomično |
| Portugalski | Djelomično |
| Turski | Djelomično |
| Poljski | Djelomično |

### 9.2 Poboljšanja pristupačnosti

1. Dodati alt tekst za sve slike
2. Osigurati ispravno isticanje sintakse kod primjera
3. Dodati transkripte za sve video materijale
4. Osigurati kontrast boja u skladu s WCAG smjernicama

---

## 10. Prioriteti implementacije

### Faza 1: Hitno (Tjedan 1-2)
- [x] Popraviti kritične sigurnosne probleme
- [x] Dodati konfiguraciju za kvalitetu koda
- [x] Kreirati zajedničke komponente
- [x] Dokumentirati sigurnosne smjernice

### Faza 2: Kratkoročno (Tjedan 3-4)
- [ ] Ažurirati zastarjele obrasce API-ja
- [ ] Dodati type hintove u sve Python datoteke
- [ ] Dodati CI/CD workflowe za kvalitetu koda
- [ ] Kreirati workflow za sigurnosno skeniranje

### Faza 3: Srednjoročno (Mjesec 2-3)
- [ ] Dodati novu lekciju o sigurnosti
- [ ] Dodati lekciju o produkcijskom postavljanju
- [ ] Poboljšati DevContainer postavke
- [ ] Dodati interaktivne demonstracije

### Faza 4: Dugoročno (Mjesec 4+)
- [ ] Dodati naprednu RAG lekciju
- [ ] Proširiti jezično pokrivanje
- [ ] Dodati opsežan skup testova
- [ ] Kreirati program certificiranja

---

## Zaključak

Ovaj plan donosi strukturiran pristup unaprjeđenju nastavnog programa Generativna AI za početnike. Rješavanjem sigurnosnih pitanja, modernizacijom API-ja i dodavanjem edukativnog sadržaja, tečaj će bolje pripremiti učenike za razvoj stvarnih AI aplikacija.

Za pitanja ili doprinose, molimo otvorite issue na GitHub repozitoriju.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument je preveden uz pomoć AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za važne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizađu iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->