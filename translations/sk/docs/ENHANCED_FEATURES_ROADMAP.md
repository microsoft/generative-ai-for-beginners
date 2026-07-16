# Plán rozvoja vylepšených funkcií a vylepšení

Tento dokument načrtáva odporúčané vylepšenia a zlepšenia pre učebný program Generatívnej AI pre začiatočníkov, založené na komplexnej kontrole kódu a analýze najlepších priemyselných postupov.

## Výkonný súhrn

Kódová základňa bola analyzovaná z hľadiska bezpečnosti, kvality kódu a vzdelávacej efektívnosti. Tento dokument poskytuje odporúčania pre okamžité opravy, krátkodobé vylepšenia a budúce rozšírenia.

---

## 1. Vylepšenia bezpečnosti (Priorita: Kritická)

### 1.1 Okamžité opravy (Dokončené)

| Problém | Ovlivnené súbory | Stav |
|-------|----------------|--------|
| Tvrdokódovaný SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Opravené |
| Chýbajúca validácia prostredia | Viacero JS/TS súborov | Opravené |
| Nezabezpečené volania funkcií | `11-integrating-with-function-calling/js-githubmodels/app.js` | Opravené |
| Úniky spracovania súborov | `08-building-search-applications/scripts/` | Opravené |
| Chýbajúce časové limity požiadaviek | `09-building-image-applications/python/` | Opravené |

### 1.2 Odporúčané dodatočné bezpečnostné funkcie

1. **Príklady obmedzenia rýchlosti**
   - Pridajte ukážkový kód, ukazujúci implementáciu obmedzenia rýchlosti API volaní
   - Demonštrácia vzorcov exponenciálneho zotavovania

2. **Rotácia API kľúčov**
   - Pridajte dokumentáciu o najlepších praktikách rotácie API kľúčov
   - Zahrňte príklady použitia Azure Key Vault alebo podobných služieb

3. **Integrácia bezpečnosti obsahu**
   - Pridajte príklady používania Azure Content Safety API
   - Demonštrácia vzorcov moderovania vstupu/výstupu

---

## 2. Vylepšenia kvality kódu

### 2.1 Pridané konfiguračné súbory

| Súbor | Účel |
|------|---------|
| `.eslintrc.json` | Lintovacie pravidlá pre JavaScript/TypeScript |
| `.prettierrc` | Štandardy formátovania kódu |
| `pyproject.toml` | Konfigurácia nástrojov pre Python (Black, Ruff, mypy) |

### 2.2 Vytvorené zdieľané utility

Nový modul `shared/python/` s:
- `env_utils.py` - Spracovanie environmentálnych premenných
- `input_validation.py` - Validácia a sanitizácia vstupov
- `api_utils.py` - Bezpečné API požiadavky (wrapery)

### 2.3 Odporúčané vylepšenia kódu

1. **Pokrytie typovými anotáciami**
   - Pridajte typové anotácie do všetkých Python súborov
   - Povoliť prísny režim TypeScript vo všetkých TS projektoch

2. **Štandardy dokumentácie**
   - Pridajte docstringy ku všetkým Python funkciám
   - Pridajte JSDoc komentáre ku všetkým JavaScript/TypeScript funkciám

3. **Testovací rámec**
   - Pridajte pytest konfiguráciu a príkladové testy _(dokončené: pytest konfigurácia v `pyproject.toml`; príkladové testy pre zdieľané utility v [`tests/`](../../../tests) spustené v CI)_
   - Pridajte Jest konfiguráciu pre JavaScript/TypeScript

---

## 3. Vzdelávacie rozšírenia

### 3.1 Nové témy lekcií

1. **Bezpečnosť v AI aplikáciách** (Navrhovaná lekcia 22)
   - Útoky na injektáž promptu a obrany
   - Správa API kľúčov
   - Moderovanie obsahu
   - Obmedzenie rýchlosti a prevencia zneužitia

2. **Produkčné nasadenie** (Navrhovaná lekcia 23)
   - Kontajnerizácia s Dockerom
   - CI/CD pipeline
   - Monitorovanie a logovanie
   - Manažment nákladov

3. **Pokročilé RAG techniky** (Navrhovaná lekcia 24)
   - Hybridné vyhľadávanie (kľúčové slová + sémantika)
   - Stratégií pre reranking
   - Multi-modálny RAG
   - Evaluačné metriky

### 3.2 Vylepšenia existujúcich lekcií

| Lekcia | Odporúčané vylepšenie |
|--------|------------------------|
| 06 - Generovanie textu | Pridajte príklady streamovania odpovedí |
| 07 - Chatové aplikácie | Pridajte vzory pamäte konverzácie |
| 08 - Vyhľadávacie aplikácie | Pridajte porovnanie vektorových databáz |
| 09 - Generovanie obrázkov | Pridajte príklady úprav a variácií obrázkov |
| 11 - Volanie funkcií | Pridajte paralelné volania funkcií |
| 15 - RAG | Pridajte porovnanie stratégií delenia na bloky |
| 17 - AI agenti | Pridajte viacagentovú orchestráciu |

---

## 4. Modernizácia API

### 4.1 Zastaralé API vzory (Migrácia dokončená)

Všetky Python a TypeScript **chat** ukážky boli migrované z Chat Completions API na **Responses API** (`client.responses.create(...)` → `response.output_text`).

| Starý vzor | Nový vzor | Stav |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (chat) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | Dokončené |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | Dokončené |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | `openai` balík `client.responses.create()` → `response.output_text` | Dokončené |
| `df.append()` (pandas) | `pd.concat()` | Dokončené |

> **Poznámka:** Ukážky Microsoft Foundry Models používajúce `azure-ai-inference` / `@azure-rest/ai-inference` SDK (`client.complete()`) zostávajú na Model Inference API, ktoré nepodporuje Responses API. `AzureOpenAI()` je úmyselne zachované tam, kde je stále platné (embeddingy a generovanie obrázkov).

### 4.2 Nové API funkcie na demonštráciu

1. **Štruktúrované výstupy** (OpenAI)
   - JSON režim
   - Volanie funkcií s prísnymi schémami

2. **Vizuálne schopnosti**
   - Analýza obrázkov s GPT-4o (vision)
   - Multi-modálne promptové vzory

3. **Vstavané nástroje Responses API** (nahrádza legacy Assistants API)
   - Interpret kódu
   - Vyhľadávanie súborov
   - Webové vyhľadávanie a vlastné nástroje

---

## 5. Vylepšenia infraštruktúry

### 5.1 Vylepšenia CI/CD

Implementované v [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): Python lintovanie/formátovanie (Ruff + Black) je **vynútené** na udržiavanom module `shared/` utilít a beží **len odporúčajúco** v ostatnej časti kurzu, plus odporúčajúce ESLint prechádzanie pre JavaScript/TypeScript. Ilustratívny základ bol:

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

### 5.2 Skanning bezpečnosti

Implementované v [`.github/workflows/security.yml`](../../../.github/workflows/security.yml): analýza CodeQL pre Python a JavaScript/TypeScript (pri push, pull requeste a týždenne) plus prehliadka závislostí pri pull requestoch. Ilustratívny základ bol:

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

## 6. Vylepšenia vývoja pre vývojárov

### 6.1 Vylepšenia DevContaineru

Implementované v [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) a [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): kontajner teraz obsahuje Pylance, Black formatter, Ruff, ESLint, Prettier a Copilot rozšírenia, povoluje formátovanie pri ukladaní previazané na konfiguráciu Black/Prettier repozitára a inštaluje vývojárske nástroje (`ruff`, `black`, `mypy`, `pytest`), aby sa [code-quality workflow](../../../.github/workflows/code-quality.yml) dal lokálne replikovať. Základný obraz `mcr.microsoft.com/devcontainers/universal` už obsahuje Python a Node, takže ďalšie featury nie sú potrebné. Ilustratívny základ bol:

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

### 6.2 Interaktívna herňa

Zvážte pridanie:
- Jupyter notebookov s predvyplnenými API kľúčmi (cez prostredie)
- Gradio/Streamlit demo pre vizuálnych študentov
- Interaktívnych kvízov na overenie znalostí

---

## 7. Podpora viacerých jazykov

### 7.1 Aktuálne pokrytie jazykov

| Technológia | Pokryté lekcie | Stav |
|------------|-----------------|--------|
| Python | Všetky | Dokončené |
| TypeScript | 06-09, 11 | Čiastočné |
| JavaScript | 06-08, 11 | Čiastočné |
| .NET/C# | Niektoré | Čiastočné |

### 7.2 Odporúčané doplnky

1. **Go** - Rastúce v AI/ML nástrojoch
2. **Rust** - Výkonovo kritické aplikácie
3. **Java/Kotlin** - Podnikové aplikácie

---

## 8. Optimalizácie výkonu

### 8.1 Optimalizácie na úrovni kódu

1. **Async/Await vzory**
   - Pridajte async príklady pre hromadné spracovanie
   - Demonštrujte súbežné API volania

2. **Caching stratégie**
   - Pridajte príklady cachovania embeddingov
   - Demonštrujte vzory cachovania odpovedí

3. **Optimalizácia tokenov**
   - Pridajte príklady použitia tiktoken
   - Demonštrujte techniky kompresie promptov

### 8.2 Príklady optimalizácie nákladov

Pridajte príklady demonštrujúce:
- Výber modelu podľa zložitosti úlohy
- Prompt engineering pre efektívnosť tokenov
- Hromadné spracovanie pre veľké operácie

---

## 9. Prístupnosť a internacionalizácia

### 9.1 Aktuálny stav prekladu

Všetky preklady sú **úplné** a generované automaticky pomocou [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst), ktorý udržiava viac ako 50 jazykových verzií kurzu synchronizovaných s anglickým zdrojom. Prekladaný obsah sa nachádza v `translations/` a lokalizované obrázky v `translated_images/`; zoznam dostupných jazykov je zverejnený v hornej časti README repozitára.

| Aspekt | Stav |
|--------|--------|
| Pokrytie prekladom | Úplné — 50+ jazykov, všetky lekcie |
| Metóda prekladu | Automatizované cez [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) |
| Synchronizované s anglickým zdrojom | Áno — automatická regenerácia |

### 9.2 Vylepšenia prístupnosti

1. Pridajte alt text ku všetkým obrázkom
2. Zabezpečte, aby ukážky kódu mali správne zvýraznenie syntaxe
3. Pridajte prepisy videí ku všetkému video obsahu
4. Zabezpečte farebný kontrast podľa smerníc WCAG

---

## 10. Priorita implementácie

### Fáza 1: Okamžité (Týždeň 1-2)
- [x] Opraviť kritické bezpečnostné problémy
- [x] Pridať konfiguráciu kvality kódu
- [x] Vytvoriť zdieľané utility
- [x] Zdokumentovať bezpečnostné smernice

### Fáza 2: Krátkodobé (Týždeň 3-4)
- [x] Aktualizovať zastarané API vzory (Chat Completions → Responses API, Python + TypeScript)
- [ ] Pridať typové anotácie do všetkých Python súborov (dokončené pre udržiavaný modul `shared/`; študijné príklady zjednodušené)
- [x] Pridať CI/CD workflow pre kvalitu kódu
- [x] Vytvoriť workflow pre bezpečnostné skenovanie

### Fáza 3: Strednodobé (Mesiac 2-3)
- [ ] Pridať novú bezpečnostnú lekciu
- [ ] Pridať lekciu produkčného nasadenia
- [x] Vylepšiť nastavenie DevContaineru
- [ ] Pridať interaktívne demo

### Fáza 4: Dlhodobé (Mesiac 4+)
- [ ] Pridať pokročilú lekciu RAG
- [ ] Rozšíriť pokrytie jazykov
- [ ] Pridať komplexnú testovaciu súpravu
- [ ] Vytvoriť certifikačný program

---

## Záver

Tento plán rozvoja poskytuje štruktúrovaný prístup k zlepšovaniu učebného programu Generatívnej AI pre začiatočníkov. Riešením bezpečnostných otázok, modernizáciou API a rozšírením vzdelávacieho obsahu bude kurz lepšie pripravovať študentov na reálny vývoj AI aplikácií.

Pre otázky alebo príspevky, prosím otvorte issue na GitHub repozitári.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->