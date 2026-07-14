# Plan unapređenih značajki i poboljšanja

Ovaj dokument iznosi preporučena poboljšanja i unapređenja za kurikulum Generativne AI za početnike, temeljeći se na sveobuhvatnoj reviziji koda i analizi najboljih industrijskih praksi.

## Izvršni sažetak

Kod je analiziran u pogledu sigurnosti, kvalitete i obrazovne učinkovitosti. Ovaj dokument pruža preporuke za trenutna ispravke, kratkoročna poboljšanja i buduća unapređenja.

---

## 1. Sigurnosna unapređenja (Prioritet: Kritično)

### 1.1 Trenutne ispravke (Završeno)

| Problem | Datoteke koje utječu | Status |
|---------|---------------------|--------|
| Hardkodirani SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Ispravljeno |
| Nedostajuća validacija env varijabli | Više JS/TS datoteka | Ispravljeno |
| Nesigurni pozivi funkcija | `11-integrating-with-function-calling/js-githubmodels/app.js` | Ispravljeno |
| Curjenje datotečnih pokazivača | `08-building-search-applications/scripts/` | Ispravljeno |
| Nedostajuća ograničenja vremena zahtjeva | `09-building-image-applications/python/` | Ispravljeno |

### 1.2 Preporučene dodatne sigurnosne značajke

1. **Primjeri ograničenja brzine (Rate Limiting)**
   - Dodati primjere koda koji pokazuju implementaciju ograničenja brzine za API pozive
   - Demonstrirati obrasce eksponencijalnog ponovnog pokušaja (exponential backoff)

2. **Rotacija API ključeva**
   - Dodati dokumentaciju najboljih praksi za rotaciju API ključeva
   - Uključiti primjere korištenja Azure Key Vault ili sličnih servisa

3. **Integracija sigurnosti sadržaja**
   - Dodati primjere korištenja Azure Content Safety API-ja
   - Demonstrirati obrasce moderacije unosa/izlaza

---

## 2. Poboljšanja kvalitete koda

### 2.1 Dodane konfiguracijske datoteke

| Datoteka | Namjena |
|---------|---------|
| `.eslintrc.json` | Pravila za lintanje JavaScript/TypeScript |
| `.prettierrc` | Standardi formatiranja koda |
| `pyproject.toml` | Konfiguracija Python alata (Black, Ruff, mypy) |

### 2.2 Kreirane zajedničke utilitarne funkcije

Novi `shared/python/` modul s:
- `env_utils.py` - Rukovanje s varijablama okoline
- `input_validation.py` - Validacija i sanitacija unosa
- `api_utils.py` - Sigurne omotnice za API pozive

### 2.3 Preporučena poboljšanja koda

1. **Pokrivenost tipovima (Type Hints)**
   - Dodati tipove u sve Python datoteke
   - Omogućiti strogi TypeScript način rada u svim TS projektima

2. **Standarde dokumentacije**
   - Dodati docstrings u sve Python funkcije
   - Dodati JSDoc komentare u sve JavaScript/TypeScript funkcije

3. **Testni okvir**
   - Dodati pytest konfiguraciju i primjere testova _(završeno: pytest konfiguracija u `pyproject.toml`; primjeri testova za zajedničke utilitarne funkcije u [`tests/`](../../../tests) se izvršavaju u CI)_
   - Dodati Jest konfiguraciju za JavaScript/TypeScript

---

## 3. Obrazovna unapređenja

### 3.1 Novi nastavni sadržaji

1. **Sigurnost u AI aplikacijama** (Predložena lekcija 22)
   - Napadi i obrane od prompt injekcija
   - Upravljanje API ključevima
   - Moderacija sadržaja
   - Ograničenje brzine i prevencija zloupotrebe

2. **Produkcijsko postavljanje** (Predložena lekcija 23)
   - Kontejnerizacija pomoću Dockera
   - CI/CD procesi
   - Nadgledanje i zapisivanje događaja
   - Upravljanje troškovima

3. **Napredne RAG tehnike** (Predložena lekcija 24)
   - Hibridno pretraživanje (ključna riječ + semantički)
   - Strategije re-rankiranja
   - Multimodalni RAG
   - Mjerni sustavi evaluacije

### 3.2 Poboljšanja postojećih lekcija

| Lekcija | Preporučeno unapređenje |
|---------|-----------------------|
| 06 - Generiranje teksta | Dodati primjere streaminga odgovora |
| 07 - Chat aplikacije | Dodati obrasce za memoriju razgovora |
| 08 - Pretraživačke aplikacije | Dodati usporedbu vektorskih baza podataka |
| 09 - Generiranje slika | Dodati primjere uređivanja i varijacija slika |
| 11 - Pozivanje funkcija | Dodati paralelno pozivanje funkcija |
| 15 - RAG | Dodati usporedbu strategija razbijanja na cjeline |
| 17 - AI agenti | Dodati orkestraciju više agenata |

---

## 4. Modernizacija API-ja

### 4.1 Zastarjeli API obrasci (Migracija dovršena)

Svi Python i TypeScript **chat** primjeri su migrirani s Chat Completions API-ja na **Responses API** (`client.responses.create(...)` → `response.output_text`).

| Stari obrazac | Novi obrazac | Status |
|--------------|--------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (chat) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | Dovršeno |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | Dovršeno |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | `openai` paket `client.responses.create()` → `response.output_text` | Dovršeno |
| `df.append()` (pandas) | `pd.concat()` | Dovršeno |

> **Napomena:** Primjeri Microsoft Foundry modela koji koriste `azure-ai-inference` / `@azure-rest/ai-inference` SDK (`client.complete()`) ostaju na Model Inference API-ju, koji ne podržava Responses API. `AzureOpenAI()` je namjerno zadržan gdje je još valjan (embeddings i generiranje slika).

### 4.2 Nove API značajke za demonstraciju

1. **Strukturirani rezultati** (OpenAI)
   - JSON mod
   - Pozivanje funkcija sa strogim šemama

2. **Vizijske mogućnosti**
   - Analiza slika s GPT-4o (vision)
   - Multimodalni prompti

3. **Alati ugrađeni u Responses API** (zamjenjuje naslijeđeni Assistants API)
   - Tumač koda
   - Pretraživanje datoteka
   - Web pretraživanje i prilagođeni alati

---

## 5. Infrastrukturna poboljšanja

### 5.1 Poboljšanja CI/CD-a

Implementirano u [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): Python lintanje/formatiranje (Ruff + Black) je **strogo primijenjeno** na održavani `shared/` utilitarni modul i radi **savjetodavno** na ostatku kurikuluma, plus savjetodavni ESLint prolaz za JavaScript/TypeScript. Ilustrativna početna točka je bila:

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

Implementirano u [`.github/workflows/security.yml`](../../../.github/workflows/security.yml): Analiza CodeQL za Python i JavaScript/TypeScript (pri push, pull requestu i tjednom rasporedu) plus pregled ovisnosti na pull requestovima. Ilustrativna početna točka je bila:

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

### 6.1 Poboljšanja DevContainer-a

Implementirano u [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) i [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): kontejner sada sadrži Pylance, Black formatirator, Ruff, ESLint, Prettier i Copilot ekstenzije, omogućuje formatiranje pri spremanju povezano s konfiguracijom Black/Prettier repozitorija i instalira razvojne alate (`ruff`, `black`, `mypy`, `pytest`) kako bi se [code-quality workflow](../../../.github/workflows/code-quality.yml) mogao reproducirati lokalno. Bazna slika `mcr.microsoft.com/devcontainers/universal` već uključuje Python i Node, stoga nisu potrebne dodatne značajke. Ilustrativna početna točka je bila:

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

### 6.2 Interaktivni poligon

Razmisliti o dodavanju:
- Jupyter bilježnica s unaprijed unesenim API ključevima (putem okoline)
- Gradio/Streamlit demoza za vizualne učenike
- Interaktivnih kvizova za provjeru znanja

---

## 7. Višejezična podrška

### 7.1 Trenutna podrška jezika

| Tehnologija | Pokrivene lekcije | Status |
|------------|-------------------|--------|
| Python | Sve | Potpuno |
| TypeScript | 06-09, 11 | Djelomično |
| JavaScript | 06-08, 11 | Djelomično |
| .NET/C# | Neke | Djelomično |

### 7.2 Preporučeni dodaci

1. **Go** - Rast u AI/ML alatima
2. **Rust** - Aplikacije kritične na performanse
3. **Java/Kotlin** - Enterprise aplikacije

---

## 8. Optimizacije izvedbe

### 8.1 Optimizacije na razini koda

1. **Async/Await obrasci**
   - Dodati primjere async batch obrade
   - Demonstrirati paralelne API pozive

2. **Strategije keširanja**
   - Dodati primjere keširanja embeddingsa
   - Demonstrirati obrasce keširanja odgovora

3. **Optimizacija tokena**
   - Dodati primjere korištenja tiktoken
   - Demonstrirati tehnike kompresije prompta

### 8.2 Primjeri optimizacije troškova

Dodati primjere koji pokazuju:
- Odabir modela na temelju složenosti zadatka
- Prompt engineering za efikasnost tokena
- Batch obradu za velike operacije

---

## 9. Pristupačnost i internacionalizacija

### 9.1 Trenutni status prevođenja

Svi prijevodi su **dovršeni** i generirani automatski putem [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst), koji proizvodi i održava sinkronizirane verzije kurikuluma na više od 50 jezika s izvornim engleskim sadržajem. Prevedeni sadržaj nalazi se u `translations/` dok su lokalizirane slike u `translated_images/`; potpuni popis dostupnih jezika objavljen je na vrhu README datoteke repozitorija.

| Aspekt | Status |
|--------|--------|
| Pokrivenost prijevoda | Potpuna — 50+ jezika, sve lekcije |
| Metoda prijevoda | Automatizirana putem [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) |
| Održava sinkronizaciju s izvornim engleskim sadržajem | Da — automatski regenerirana |

### 9.2 Poboljšanja pristupačnosti

1. Dodati alt tekst za sve slike
2. Osigurati pravilno isticanje sintakse u primjerima koda
3. Dodati transkripte videa za sav video sadržaj
4. Osigurati kontrast boja u skladu sa WCAG smjernicama

---

## 10. Prioritet implementacije

### Faza 1: Trenutna (tjedan 1-2)
- [x] Ispraviti kritične sigurnosne probleme
- [x] Dodati konfiguraciju kvalitete koda
- [x] Kreirati zajedničke utilitarne funkcije
- [x] Dokumentirati sigurnosne smjernice

### Faza 2: Kratkoročno (tjedan 3-4)
- [x] Ažurirati zastarjele API obrasce (Chat Completions → Responses API, Python + TypeScript)
- [ ] Dodati type hintove u sve Python datoteke (završeno za održavani `shared/` modul; primjeri za lekcije ostavljeni jednostavnima)
- [x] Dodati CI/CD workflow-e za kvalitetu koda
- [x] Kreirati workflow za sigurnosno skeniranje

### Faza 3: Srednjoročno (mjesec 2-3)
- [ ] Dodati novu lekciju o sigurnosti
- [ ] Dodati lekciju o produkcijskom postavljanju
- [x] Poboljšati DevContainer postavke
- [ ] Dodati interaktivne demo primjere

### Faza 4: Dugoročno (mjesec 4+)
- [ ] Dodati naprednu lekciju o RAG-u
- [ ] Proširiti podršku jezicima
- [ ] Dodati sveobuhvatan paket testova
- [ ] Kreirati program certificiranja

---

## Zaključak

Ovaj plan pruža strukturirani pristup unapređenju kurikuluma Generativne AI za početnike. Rješavajući sigurnosne probleme, modernizirajući API-je i dodajući obrazovni sadržaj, tečaj će bolje pripremiti polaznike za razvoj AI aplikacija u stvarnom svijetu.

Za pitanja ili doprinose, molimo otvorite issue na GitHub repozitoriju.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->