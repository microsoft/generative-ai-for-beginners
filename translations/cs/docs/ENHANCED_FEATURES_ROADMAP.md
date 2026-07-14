# Plán vylepšení funkcí a vylepšení

Tento dokument obsahuje doporučená vylepšení a zdokonalení kurikula Generative AI for Beginners, založená na komplexní revizi kódu a analýze nejlepších průmyslových postupů.

## Shrnutí

Kódová základna byla analyzována z hlediska bezpečnosti, kvality kódu a vzdělávací účinnosti. Tento dokument nabízí doporučení pro okamžité opravy, krátkodobá vylepšení a budoucí rozšíření.

---

## 1. Vylepšení bezpečnosti (Priorita: Kritická)

### 1.1 Okamžité opravy (Dokončeno)

| Problém | Ovlivněné soubory | Stav |
|-------|----------------|--------|
| Hardcoded SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Opraveno |
| Chybějící validace prostředí | Více JS/TS souborů | Opraveno |
| Nebezpečné volání funkcí | `11-integrating-with-function-calling/js-githubmodels/app.js` | Opraveno |
| Úniky otevřených souborů | `08-building-search-applications/scripts/` | Opraveno |
| Chybějící timeouty u požadavků | `09-building-image-applications/python/` | Opraveno |

### 1.2 Doporučené další bezpečnostní funkce

1. **Příklady omezení rychlosti (Rate Limiting)**
   - Přidat ukázkový kód implementace omezení rychlosti volání API
   - Demonstrovat vzory exponenciálního zpomalování (exponential backoff)

2. **Rotace API klíčů**
   - Přidat dokumentaci o nejlepších postupech při rotaci API klíčů
   - Zahrnout příklady použití Azure Key Vault nebo podobných služeb

3. **Integrace zabezpečení obsahu**
   - Přidat příklady použití Azure Content Safety API
   - Demonstrovat vzory moderace vstupu/výstupu

---

## 2. Zlepšení kvality kódu

### 2.1 Přidány konfigurační soubory

| Soubor | Účel |
|------|---------|
| `.eslintrc.json` | Pravidla lintování JavaScriptu/TypeScriptu |
| `.prettierrc` | Standardy formátování kódu |
| `pyproject.toml` | Konfigurace nástrojů pro Python (Black, Ruff, mypy) |

### 2.2 Vytvořeny sdílené utility

Nový modul `shared/python/` obsahuje:
- `env_utils.py` - Zpracování proměnných prostředí
- `input_validation.py` - Validace a sanitizace vstupů
- `api_utils.py` - Bezpečné wrappery pro API požadavky

### 2.3 Doporučená vylepšení kódu

1. **Pokrytí typovými anotacemi**
   - Přidat typové nápovědy do všech Python souborů
   - Povolit přísný režim TypeScriptu ve všech TS projektech

2. **Standardy dokumentace**
   - Přidat docstringy ke všem Python funkcím
   - Přidat JSDoc komentáře ke všem JavaScript/TypeScript funkcím

3. **Testovací rámec**
   - Přidat konfiguraci pytest a příkladové testy _(provedeno: konfigurace pytest v `pyproject.toml`; příklady testů pro sdílené utility v [`tests/`](../../../tests) běží v CI)_
   - Přidat konfiguraci Jest pro JavaScript/TypeScript

---

## 3. Vzdělávací vylepšení

### 3.1 Nová témata lekcí

1. **Bezpečnost v AI aplikacích** (Navrhovaná lekce 22)
   - Útoky na injektáž promptů a obrany proti nim
   - Správa API klíčů
   - Moderace obsahu
   - Omezení rychlosti a prevence zneužití

2. **Nasazení do produkce** (Navrhovaná lekce 23)
   - Kontejnery s Dockerem
   - CI/CD pipeline
   - Monitorování a logování
   - Správa nákladů

3. **Pokročilé RAG techniky** (Navrhovaná lekce 24)
   - Hybridní vyhledávání (klíčové slovo + semantické)
   - Strategie opětovného řazení
   - Multimodální RAG
   - Evaluační metriky

### 3.2 Vylepšení existujících lekcí

| Lekce | Doporučené vylepšení |
|--------|------------------------|
| 06 - Generování textu | Přidat příklady streamovaného výstupu |
| 07 - Chatovací aplikace | Přidat vzory paměti konverzace |
| 08 - Vyhledávací aplikace | Přidat porovnání vektorových databází |
| 09 - Generování obrázků | Přidat příklady úprav/variací obrázků |
| 11 - Volání funkcí | Přidat paralelní volání funkcí |
| 15 - RAG | Přidat porovnání strategií dělení na bloky |
| 17 - AI agenti | Přidat orchestraci multi-agentů |

---

## 4. Modernizace API

### 4.1 Zastaralé vzory API (Migrace dokončena)

Všechny ukázky Python a TypeScript **chatu** byly migrovány z Chat Completions API na **Responses API** (`client.responses.create(...)` → `response.output_text`).

| Starý vzor | Nový vzor | Stav |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (chat) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | Dokončeno |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | Dokončeno |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | `openai` balíček `client.responses.create()` → `response.output_text` | Dokončeno |
| `df.append()` (pandas) | `pd.concat()` | Dokončeno |

> **Poznámka:** Ukázky Microsoft Foundry Models používající `azure-ai-inference` / `@azure-rest/ai-inference` SDK (`client.complete()`) zůstávají na Model Inference API, které Responses API nepodporuje. `AzureOpenAI()` je záměrně zachováno tam, kde je relevantní (embeddingy a generování obrázků).

### 4.2 Nové funkce API k demonstraci

1. **Strukturované výstupy** (OpenAI)
   - JSON režim
   - Volání funkcí s přísnými schématy

2. **Vizuální schopnosti**
   - Analýza obrázků pomocí GPT-4o (vision)
   - Multimodální promptování

3. **Nástroje v Responses API** (nahrazuje staré Assistants API)
   - Interpret kódu
   - Vyhledávání souborů
   - Webové vyhledávání a vlastní nástroje

---

## 5. Zlepšení infrastruktury

### 5.1 Vylepšení CI/CD

Implementováno v [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): Python lintování/formátování (Ruff + Black) je **vynucováno** na udržovaném modulu `shared/` a běží **doporučeně** na zbytku kurikula, plus doporučený ESLint průchod pro JavaScript/TypeScript. Ilustrační výchozí stav byl:

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

### 5.2 Bezpečnostní skenování

Implementováno v [`.github/workflows/security.yml`](../../../.github/workflows/security.yml): Analýza CodeQL pro Python a JavaScript/TypeScript (při pushnutí, pull requestu a týdenním plánu) plus kontrola závislostí u pull requestů. Ilustrační výchozí stav byl:

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

## 6. Zlepšení vývojářské zkušenosti

### 6.1 Vylepšení DevContaineru

Implementováno v [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) a [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): kontejner nyní obsahuje rozšíření Pylance, Black formatter, Ruff, ESLint, Prettier a Copilot, povoluje formátování při ukládání připojené k repozitářové konfiguraci Black/Prettier a instaluje vývojářské nástroje (`ruff`, `black`, `mypy`, `pytest`) pro možnost lokální reprodukce [code-quality workflow](../../../.github/workflows/code-quality.yml). Základní obraz `mcr.microsoft.com/devcontainers/universal` již obsahuje Python a Node, takže nejsou potřeba další funkce. Ilustrační výchozí stav byl:

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

### 6.2 Interaktivní hřiště (Playground)

Zvážit přidání:
- Jupyter notebooků s předvyplněnými API klíči (přes prostředí)
- Gradio/Streamlit demo pro vizuální studenty
- Interaktivních kvízů pro ověření znalostí

---

## 7. Podpora vícero jazyků

### 7.1 Aktuální pokrytí jazyků

| Technologie | Pokryté lekce | Stav |
|------------|-----------------|--------|
| Python | Všechny | Kompletní |
| TypeScript | 06-09, 11 | Částečné |
| JavaScript | 06-08, 11 | Částečné |
| .NET/C# | Některé | Částečné |

### 7.2 Doporučené doplnění

1. **Go** - Stále rostoucí v AI/ML nástrojích
2. **Rust** - Výkonově kritické aplikace
3. **Java/Kotlin** - Podnikové aplikace

---

## 8. Optimalizace výkonnosti

### 8.1 Optimalizace na úrovni kódu

1. **Asynchronní vzory (Async/Await)**
   - Přidat asynchronní příklady pro dávkové zpracování
   - Demonstrovat souběžné volání API

2. **Strategie kešování**
   - Přidat příklady kešování embeddingů
   - Demonstrovat vzory kešování odpovědí

3. **Optimalizace tokenů**
   - Přidat příklady použití tiktoken
   - Demonstrovat techniky komprese promptů

### 8.2 Příklady optimalizace nákladů

Přidat příklady demonstrující:
- Výběr modelu na základě složitosti úlohy
- Inženýrství promptů pro efektivitu tokenů
- Dávkové zpracování pro hromadné operace

---

## 9. Přístupnost a internacionalizace

### 9.1 Aktuální stav překladu

Všechny překlady jsou **kompletní** a generovány automaticky pomocí [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst), který vytváří a udržuje synchronizované verze kurikula ve více než 50 jazycích s anglickým zdrojem. Přeložený obsah se nachází v `translations/` a lokalizované obrázky v `translated_images/`; úplný seznam dostupných jazyků je uveden na začátku README repozitáře.

| Aspekt | Stav |
|--------|--------|
| Pokrytí překladu | Kompletní — 50+ jazyků, všechny lekce |
| Metoda překladu | Automatizovaná přes [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) |
| Synchronizace s anglickým zdrojem | Ano — automaticky obnovováno |

### 9.2 Vylepšení přístupnosti

1. Přidat alt text ke všem obrázkům
2. Zajistit správné zvýraznění syntaxe v příkladech kódu
3. Přidat přepisy videí ke všem videím
4. Zajistit barevný kontrast odpovídající WCAG směrnicím

---

## 10. Priorita implementace

### Fáze 1: Okamžité (Týdny 1-2)
- [x] Opravit kritické bezpečnostní problémy
- [x] Přidat konfiguraci kvality kódu
- [x] Vytvořit sdílené utility
- [x] Zdokumentovat bezpečnostní pokyny

### Fáze 2: Krátkodobé (Týdny 3-4)
- [x] Aktualizovat zastaralé vzory API (Chat Completions → Responses API, Python + TypeScript)
- [ ] Přidat typové nápovědy do všech Python souborů (provedeno pro udržovaný modul `shared/`; vzorky lekcí zůstávají jednoduché)
- [x] Přidat CI/CD workflow pro kvalitu kódu
- [x] Vytvořit workflow pro bezpečnostní skenování

### Fáze 3: Střednědobé (Měsíce 2-3)
- [ ] Přidat novou lekci o bezpečnosti
- [ ] Přidat lekci o nasazení do produkce
- [x] Vylepšit nastavení DevContaineru
- [ ] Přidat interaktivní demo

### Fáze 4: Dlouhodobé (Měsíce 4+)
- [ ] Přidat pokročilou lekci o RAG
- [ ] Rozšířit pokrytí jazyků
- [ ] Přidat komplexní testovací sadu
- [ ] Vytvořit certifikační program

---

## Závěr

Tento plán poskytuje strukturovaný přístup ke zlepšení kurikula Generative AI for Beginners. Řešením bezpečnostních problémů, modernizací API a přidáním vzdělávacího obsahu bude kurz lépe připravovat studenty na vývoj AI aplikací v reálném světě.

Pro dotazy nebo příspěvky prosím otevřete issue v GitHubovém repozitáři.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->