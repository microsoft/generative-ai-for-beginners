# Načrt izboljšav in nadgradenj

Ta dokument povzema priporočene izboljšave in nadgradnje učnega načrta Generative AI for Beginners, temelječe na celovitem pregledu kode in analizi najboljših praks v industriji.

## Povzetek za vodstvo

Koda je bila analizirana glede varnosti, kakovosti kode in izobraževalne učinkovitosti. Ta dokument poda priporočila za takojšnje popravke, izboljšave na kratki rok in prihodnje nadgradnje.

---

## 1. Varnostne izboljšave (Prednost: Kritično)

### 1.1 Tekoči popravki (Zaključeno)

| Težava | Vplivane datoteke | Status |
|-------|----------------|--------|
| Trdo kodiran SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Popravljeno |
| Manjkajoča validacija okolja | Več JS/TS datotek | Popravljeno |
| Nevarni klici funkcij | `11-integrating-with-function-calling/js-githubmodels/app.js` | Popravljeno |
| Izpusti ročajev datotek | `08-building-search-applications/scripts/` | Popravljeno |
| Manjkajoči zahtevi za timeout | `09-building-image-applications/python/` | Popravljeno |

### 1.2 Priporočene dodatne varnostne funkcije

1. **Primeri omejevanja hitrosti**
   - Dodajte primer kode, ki prikazuje, kako uvesti omejevanje hitrosti za API klice
   - Prikažite vzorce eksponentnega vračanja nazaj

2. **Rotacija API ključev**
   - Dodajte dokumentacijo o najboljših praksah za rotacijo API ključev
   - Vključite primere uporabe Azure Key Vault ali podobnih storitev

3. **Integracija varnosti vsebine**
   - Dodajte primere uporabe Azure Content Safety API
   - Prikažite vzorce moderiranja vhodnih/izhodnih podatkov

---

## 2. Izboljšave kakovosti kode

### 2.1 Dodane konfiguracijske datoteke

| Datoteka | Namen |
|------|---------|
| `.eslintrc.json` | Pravila za lintanje JavaScript/TypeScript |
| `.prettierrc` | Standardi oblikovanja kode |
| `pyproject.toml` | Konfiguracija orodij za Python (Black, Ruff, mypy) |

### 2.2 Ustvarjene deljene pripomočke

Novi modul `shared/python/` z:
- `env_utils.py` - Upravljanje okoljskih spremenljivk
- `input_validation.py` - Validacija in sanacija vhodnih podatkov
- `api_utils.py` - Varnostni ovoji za klice API

### 2.3 Priporočene izboljšave kode

1. **Pokritost s tipi**
   - Dodajte tipizirane napovedi v vse Python datoteke
   - Omogočite strogi način TypeScript za vse TS projekte

2. **Standardi dokumentacije**
   - Dodajte docstring-e v vse Python funkcije
   - Dodajte JSDoc komentarje v vse JavaScript/TypeScript funkcije

3. **Testni okvir**
   - Dodajte konfiguracijo pytest in primere testov _(izvedeno: pytest konfiguracija v `pyproject.toml`; primeri testov za deljene pripomočke v [`tests/`](../../../tests) se izvajajo v CI)_
   - Dodajte konfiguracijo Jest za JavaScript/TypeScript

---

## 3. Izobraževalne izboljšave

### 3.1 Nove teme lekcij

1. **Varnost v AI aplikacijah** (Predlagana lekcija 22)
   - Napadi in obrambe pred vbrizgavanjem promptov
   - Upravljanje API ključev
   - Moderiranje vsebine
   - Omejevanje hitrosti in preprečevanje zlorab

2. **Produkcijska uvedba** (Predlagana lekcija 23)
   - Kontejnerizacija z Dockerjem
   - CI/CD pipeline-i
   - Nadzor in beleženje
   - Upravljanje stroškov

3. **Napredne RAG tehnike** (Predlagana lekcija 24)
   - Hibridno iskanje (ključna beseda + semantično)
   - Strategije ponovnega razvrščanja
   - Večmodalni RAG
   - Merjenje učinkovitosti

### 3.2 Izboljšave obstoječih lekcij

| Lekcija | Priporočena izboljšava |
|--------|------------------------|
| 06 - Generiranje besedila | Dodajte primere pretočnih odzivov |
| 07 - Chat aplikacije | Dodajte vzorce pogovorne memorije |
| 08 - Iskalne aplikacije | Dodajte primerjavo vektorskih baz podatkov |
| 09 - Generiranje slik | Dodajte primere urejanja/variacij slik |
| 11 - Klic funkcij | Dodajte vzporedni klic funkcij |
| 15 - RAG | Dodajte primerjavo strategije razdelitve |
| 17 - AI agenti | Dodajte orkestracijo več agentov |

---

## 4. Modernizacija API

### 4.1 Zastareli vzorci API (Migracija zaključena)

Vsi Python in TypeScript **chat** primeri so bili migrirani iz Chat Completions API na **Responses API** (`client.responses.create(...)` → `response.output_text`).

| Stari vzorec | Nov vzorec | Status |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (chat) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | Zaključeno |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | Zaključeno |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | `openai` paket `client.responses.create()` → `response.output_text` | Zaključeno |
| `df.append()` (pandas) | `pd.concat()` | Zaključeno |

> **Opomba:** Primeri Microsoft Foundry Models, ki uporabljajo `azure-ai-inference` / `@azure-rest/ai-inference` SDK (`client.complete()`), ostajajo na Model Inference API, ki ne podpira Responses API. `AzureOpenAI()` je namensko ohranjen tam, kjer je še veljaven (vdelave in generiranje slik).

### 4.2 Nove funkcije API za demonstracijo

1. **Strukturirani izhodi** (OpenAI)
   - JSON način
   - Klic funkcij z natančnimi shemami

2. **Vidne zmožnosti**
   - Analiza slik z GPT-4o (vision)
   - Večmodalni prompti

3. **Orodja vgrajena v Responses API** (nadomešča zastareli Assistants API)
   - Interpreter kode
   - Iskanje datotek
   - Iskanje po spletu in prilagojena orodja

---

## 5. Izboljšave infrastrukture

### 5.1 Izboljšave CI/CD

Implementirano v [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): Python lintanje/formatiranje (Ruff + Black) je **prisilno** za vzdrževani modul `shared/` in se izvaja **svetovalno** za preostanek učnega načrta, poleg tega je svetovalni prehod ESLint za JavaScript/TypeScript. Ilustrativna izhodiščna točka je bila:

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

### 5.2 Varnostno pregledovanje

Implementirano v [`.github/workflows/security.yml`](../../../.github/workflows/security.yml): analiza CodeQL za Python in JavaScript/TypeScript (ob push-u, pull requestu in tedenskih urnikih) ter pregled odvisnosti pri pull requestih. Ilustrativna izhodiščna točka je bila:

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

## 6. Izboljšave izkušnje razvijalcev

### 6.1 Izboljšave DevContainer

Implementirano v [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) in [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): container zdaj vključuje razširitve Pylance, Black, Ruff, ESLint, Prettier in Copilot, omogoča oblikovanje ob shranjevanju povezano s konfiguracijo Black/Prettier iz repozitorija ter namesti orodja za razvoj (`ruff`, `black`, `mypy`, `pytest`), da je [workflow za kakovost kode](../../../.github/workflows/code-quality.yml) mogoče reproducirati lokalno. Osnovna slika `mcr.microsoft.com/devcontainers/universal` že vsebuje Python in Node, zato dodatnih funkcij ni potrebno. Ilustrativna izhodiščna točka je bila:

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

### 6.2 Interaktivno igrališče

Razmislite o dodajanju:
- Jupiter zvezkov z vnaprej izpolnjenimi API ključi (prek okolja)
- Demo-ja Gradio/Streamlit za vizualne učence
- Interaktivnih kvizov za ocenjevanje znanja

---

## 7. Podpora več jezikom

### 7.1 Trenutna pokritost jezikov

| Tehnologija | Pokrite lekcije | Status |
|------------|-----------------|--------|
| Python | Vse | Popolno |
| TypeScript | 06-09, 11 | Delno |
| JavaScript | 06-08, 11 | Delno |
| .NET/C# | Nekatere | Delno |

### 7.2 Priporočene dopolnitve

1. **Go** - rast orodij za AI/ML
2. **Rust** - aplikacije, kritične za zmogljivost
3. **Java/Kotlin** - poslovne aplikacije

---

## 8. Optimizacije zmogljivosti

### 8.1 Optimizacije na nivoju kode

1. **Vzorec Async/Await**
   - Dodajte asinhrone primere za obdelavo serij
   - Pokažite vzporedne klice API

2. **Strategije predpomnjenja**
   - Dodajte primere predpomnjenja vdelav
   - Prikažite vzorce predpomnjenja odgovorov

3. **Optimizacija tokenov**
   - Dodajte primere uporabe tiktoken
   - Prikažite tehnike stiskanja promptov

### 8.2 Primeri optimizacije stroškov

Dodajte primere, ki prikazujejo:
- Izbiro modela glede na zahtevnost naloge
- Inženiring promptov za učinkovito rabo tokenov
- Serijsko obdelavo za količinske operacije

---

## 9. Dostopnost in internacionalizacija

### 9.1 Trenutni status prevodov

Vsi prevodi so **popolni** in avtomatsko ustvarjeni z [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst), ki ohranja več kot 50 jezikov učnega načrta skladno z izvirnikom v angleščini. Prevedena vsebina je shranjena pod `translations/`, lokalizirane slike pod `translated_images/`; celoten seznam razpoložljivih jezikov je objavljen na vrhu README v repozitoriju.

| Vidik | Status |
|--------|--------|
| Pokritost prevodov | Popolno — več kot 50 jezikov, vse lekcije |
| Metoda prevoda | Avtomatizirano prek [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) |
| Sinhronizacija z angleškim izvirnikom | Da — samodejno obnovljeno |

### 9.2 Izboljšave dostopnosti

1. Dodajte alt besedilo v vse slike
2. Zagotovite pravilno osvetlitev sintakse v primerih kode
3. Dodajte prepis videov za vse video vsebine
4. Zagotovite barvni kontrast po WCAG smernicah

---

## 10. Prednostna izvedba

### Faza 1: Takojšnje (1-2 teden)
- [x] Popravite kritične varnostne težave
- [x] Dodajte konfiguracijo kakovosti kode
- [x] Ustvarite deljene pripomočke
- [x] Dokumentirajte varnostna navodila

### Faza 2: Kratkoročno (3-4 teden)
- [x] Posodobite zastarele vzorce API (Chat Completions → Responses API, Python + TypeScript)
- [ ] Dodajte tipizirane napovedi v vse Python datoteke (izvedeno za vzdrževani modul `shared/`; primeri lekcij so ostali preprosti)
- [x] Dodajte CI/CD workflow-e za kakovost kode
- [x] Ustvarite workflow za varnostno pregledovanje

### Faza 3: Srednjeročno (2-3 mesec)
- [ ] Dodajte novo lekcijo o varnosti
- [ ] Dodajte lekcijo o produkcijski uvedbi
- [x] Izboljšajte nastavitev DevContainer
- [ ] Dodajte interaktivne demoje

### Faza 4: Dolgoročno (4+ mesec)
- [ ] Dodajte napredno lekcijo o RAG
- [ ] Razširite jezikovno pokritost
- [ ] Dodajte obsežen testni paket
- [ ] Ustvarite certifikacijski program

---

## Zaključek

Ta načrt predstavlja strukturiran pristop k izboljšanju učnega načrta Generative AI for Beginners. Z reševanjem varnostnih vprašanj, modernizacijo API-jev in dodajanjem izobraževalne vsebine bo tečaj bolje pripravil študente na razvoj AI aplikacij v resničnem svetu.

Za vprašanja ali prispevke odprite težavo v GitHub repozitoriju.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->