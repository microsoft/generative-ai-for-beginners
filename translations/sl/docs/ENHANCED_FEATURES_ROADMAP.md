# Načrt izboljšav in nadgradenj

Ta dokument podrobno opisuje priporočene nadgradnje in izboljšave kurikuluma Generativna umetna inteligenca za začetnike, na podlagi obsežnega pregleda kode in analize najboljših praks v industriji.

## Povzetek

Koda je bila analizirana glede varnosti, kakovosti kode in izobraževalne učinkovitosti. Ta dokument vsebuje priporočila za takojšnje popravke, kratkoročne izboljšave in prihodnje nadgradnje.

---

## 1. Izboljšave varnosti (Prioriteta: Kritično)

### 1.1 Tekoči popravki (Dokončano)

| Težava | Vplivane datoteke | Status |
|--------|-------------------|--------|
| Vnaprej določena SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Popravljeno |
| Manjkajoča validacija okolja | Več datotek JS/TS | Popravljeno |
| Nevarni klici funkcij | `11-integrating-with-function-calling/js-githubmodels/app.js` | Popravljeno |
| Puščanje datotečnih ročajev | `08-building-search-applications/scripts/` | Popravljeno |
| Manjkajoči request timeouti | `09-building-image-applications/python/` | Popravljeno |

### 1.2 Priporočene dodatne varnostne funkcije

1. **Primeri omejevanja hitrosti**
   - Dodati primer kode, ki prikazuje, kako uvesti omejevanje hitrosti za API klice
   - Prikazati vzorce eksponentnega vračanja nazaj (exponential backoff)

2. **Rotacija API ključev**
   - Dodati dokumentacijo o najboljših praksah za rotacijo API ključev
   - Vključiti primere uporabe Azure Key Vault ali podobnih storitev

3. **Integracija varnosti vsebine**
   - Dodati primere uporabe Azure Content Safety API
   - Prikazati vzorce moderacije vhodnih/izhodnih podatkov

---

## 2. Izboljšave kakovosti kode

### 2.1 Dodane konfiguracijske datoteke

| Datoteka | Namen |
|----------|-------|
| `.eslintrc.json` | Pravila za lintanje JavaScript/TypeScript |
| `.prettierrc` | Standardi oblikovanja kode |
| `pyproject.toml` | Konfiguracija orodij za Python (Black, Ruff, mypy) |

### 2.2 Ustvarjene skupne pomožne funkcije

Nov modul `shared/python/` z:
- `env_utils.py` - upravljanje z okoljskimi spremenljivkami
- `input_validation.py` - validacija in čiščenje vhodnih podatkov
- `api_utils.py` - varni ovoji za API zahteve

### 2.3 Priporočene izboljšave kode

1. **Pokritost z oznakami tipov**
   - Dodati oznake tipov v vse Python datoteke
   - Omogočiti strog režim TypeScript v vseh TS projektih

2. **Standardi dokumentacije**
   - Dodati docstrings v vse Python funkcije
   - Dodati JSDoc komentarje v vse JavaScript/TypeScript funkcije

3. **Testni okvir**
   - Dodati konfiguracijo za pytest in primere testov
   - Dodati konfiguracijo Jest za JavaScript/TypeScript

---

## 3. Izobraževalne nadgradnje

### 3.1 Nove teme lekcij

1. **Varnost v AI aplikacijah** (Predlagana lekcija 22)
   - Napadi in zaščite pred vbrizgavanjem promptov (prompt injection)
   - Upravljanje API ključev
   - Moderacija vsebin
   - Omejevanje hitrosti in preprečevanje zlorab

2. **Produktivna implementacija** (Predlagana lekcija 23)
   - Kontejnerizacija z Dockerjem
   - CI/CD cevovodi
   - Nadzor in beleženje
   - Upravljanje stroškov

3. **Napredne RAG tehnike** (Predlagana lekcija 24)
   - Hibridno iskanje (ključna beseda + semantično)
   - Strategije ponovnega razvrščanja (re-ranking)
   - Večmodalni RAG
   - Merila ocenjevanja

### 3.2 Izboljšave obstoječih lekcij

| Lekcija | Priporočena izboljšava |
|---------|-----------------------|
| 06 - Generiranje besedila | Dodati primere pretočnih odzivov (streaming) |
| 07 - Klepetalne aplikacije | Dodati vzorce pomnilnika pogovora |
| 08 - Iskalne aplikacije | Dodati primerjavo vektorskih baz podatkov |
| 09 - Generiranje slik | Dodati primere urejanja/varijacij slik |
| 11 - Klicanje funkcij | Dodati vzporedno klicanje funkcij |
| 15 - RAG | Dodati primerjavo strategij razdeljevanja vsebine |
| 17 - AI agenti | Dodati orkestracijo več agentov |

---

## 4. Posodobitev API-jev

### 4.1 Zastarele API vzorce posodobiti

| Stari vzorec | Novi vzorec | Vplivane datoteke |
|--------------|------------|-------------------|
| `openai.api_type = "azure"` | klient `AzureOpenAI()` | Več skript v `08-building-search-applications/` |
| `openai.ChatCompletion.create()` | `client.chat.completions.create()` | Več zvezkov (notebookov) |
| `df.append()` (pandas) | `pd.concat()` | RAG notebook |

### 4.2 Nove API funkcionalnosti za demonstracijo

1. **Strukturirani izhodi** (OpenAI)
   - JSON način
   - Klicanje funkcij z natančnimi shemami

2. **Zmožnosti vida**
   - Analiza slik z GPT-4V
   - Večmodalni prompti

3. **API za asistente**
   - Koder za kodo (code interpreter)
   - Iskanje datotek
   - Prilagojena orodja

---

## 5. Izboljšave infrastrukture

### 5.1 Izboljšave CI/CD

Trenutni poteki dela preverjajo markdown validacijo. Priporočene dopolnitve:

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

### 5.2 Varnostno skeniranje

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

## 6. Izboljšave za razvijalce

### 6.1 Izboljšave DevContainer

Posodobitev `.devcontainer/devcontainer.json`:

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

Razmisliti o dodajanju:
- Jupyter zvezkov s prednaloženimi API ključi (prek okolja)
- Demo predstavitev z Gradio/Streamlit za vizualne učence
- Interaktivnih kvizov za ocenjevanje znanja

---

## 7. Podpora več jezikom

### 7.1 Trenutna pokritost jezikov

| Tehnologija | Pokrite lekcije | Status |
|-------------|-----------------|--------|
| Python | Vse | Popolno |
| TypeScript | 06-09, 11 | Delno |
| JavaScript | 06-08, 11 | Delno |
| .NET/C# | Nekatere | Delno |

### 7.2 Priporočene dodatne podprti jeziki

1. **Go** - Naraščajoča podpora za AI/ML orodja
2. **Rust** - Aplikacije z zahtevno zmogljivostjo
3. **Java/Kotlin** - Podjetniške aplikacije

---

## 8. Optimizacije zmogljivosti

### 8.1 Optimizacije na nivoju kode

1. **Vzorec Async/Await**
   - Dodati asinh primere za obdelavo množic (batch processing)
   - Prikazati vzorce vzporednih API klicev

2. **Strategije predpomnjenja**
   - Dodati primere predpomnjenja vdelav (embedding caching)
   - Prikazati vzorce predpomnjenja odzivov

3. **Optimizacija števila tokenov**
   - Dodati primere uporabe tiktoken
   - Prikazati tehnike stiskanja promptov

### 8.2 Primeri optimizacije stroškov

Dodati primere, ki prikazujejo:
- Izbiro modela glede na kompleksnost naloge
- Oblikovanje promptov za učinkovito porabo tokenov
- Batch obdelavo za množične operacije

---

## 9. Dostopnost in internacionalizacija

### 9.1 Trenutni status prevodov

| Jezik | Status |
|-------|--------|
| Angleščina | Popolno |
| Kitajščina (poenostavljena) | Popolno |
| Japonščina | Popolno |
| Korejščina | Popolno |
| Španščina | Delno |
| Portugalščina | Delno |
| Turščina | Delno |
| Poljščina | Delno |

### 9.2 Izboljšave dostopnosti

1. Dodati alt besedilo v vse slike
2. Zagotoviti pravilno označevanje sintakse v primerih kode
3. Dodati transkripte videov za vso video vsebino
4. Zagotoviti kontrast barv po smernicah WCAG

---

## 10. Prioriteta izvedbe

### Faza 1: Tekoče (1.-2. teden)
- [x] Popraviti kritične varnostne težave
- [x] Dodati konfiguracijo za kakovost kode
- [x] Ustvariti skupne pomožne funkcije
- [x] Dokumentirati varnostne smernice

### Faza 2: Kratkoročno (3.-4. teden)
- [ ] Posodobiti zastarele API vzorce
- [ ] Dodati oznake tipov v vse Python datoteke
- [ ] Dodati CI/CD poteke za kakovost kode
- [ ] Ustvariti potek za varnostno skeniranje

### Faza 3: Srednjeročno (2.-3. mesec)
- [ ] Dodati novo varnostno lekcijo
- [ ] Dodati lekcijo o produkcijski implementaciji
- [ ] Izboljšati DevContainer nastavitve
- [ ] Dodati interaktivne demonstracije

### Faza 4: Dolgoročno (4. mesec in naprej)
- [ ] Dodati napredno RAG lekcijo
- [ ] Razširiti pokritost jezikov
- [ ] Dodati obsežen testni paket
- [ ] Ustvariti program certificiranja

---

## Zaključek

Ta načrt ponuja strukturiran pristop za izboljšanje kurikuluma Generativna umetna inteligenca za začetnike. Z reševanjem varnostnih vprašanj, modernizacijo API-jev in dodajanjem izobraževalnih vsebin bo tečaj bolje pripravil študente za razvoj AI aplikacij v resničnem svetu.

Za vprašanja ali prispevke, prosimo, odprite težavo (issue) v GitHub repozitoriju.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v naročnem jeziku naj se šteje za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitna nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->