# Cesta rozvoja rozšírených funkcií a vylepšení

Tento dokument načrtáva odporúčané vylepšenia a zdokonalenia pre kurz Generatívnej AI pre Začiatočníkov, založené na komplexnom preskúmaní kódu a analýze najlepších priemyselných praktík.

## Výkonný súhrn

Kódová základňa bola analyzovaná z hľadiska bezpečnosti, kvality kódu a vzdelávacej efektívnosti. Tento dokument obsahuje odporúčania pre okamžité opravy, krátkodobé vylepšenia a budúce rozšírenia.

---

## 1. Bezpečnostné vylepšenia (Priorita: Kritická)

### 1.1 Okamžité opravy (dokončené)

| Problém | Súbory, ktoré sa týkajú | Stav |
|---------|-------------------------|------|
| Pevne zadaný SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Opravené |
| Chýbajúca validácia env | Viaceré JS/TS súbory | Opravené |
| Neisté volania funkcií | `11-integrating-with-function-calling/js-githubmodels/app.js` | Opravené |
| Úniky súborových handlerov | `08-building-search-applications/scripts/` | Opravené |
| Chýbajúce timeouty požiadaviek | `09-building-image-applications/python/` | Opravené |

### 1.2 Odporúčané ďalšie bezpečnostné funkcie

1. **Príklady obmedzenia rýchlosti (Rate Limiting)**
   - Pridať príklady kódu ukazujúce implementáciu obmedzenia rýchlosti API volaní
   - Demonštrovať vzory exponenciálneho spätného odkladu

2. **Rotácia API kľúčov**
   - Pridať dokumentáciu najlepších praktík pre rotáciu API kľúčov
   - Zahŕňať príklady použitia Azure Key Vault alebo podobných služieb

3. **Integrácia bezpečnosti obsahu**
   - Pridať príklady využitia Azure Content Safety API
   - Demonštrovať vzory moderovania vstupov/výstupov

---

## 2. Vylepšenia kvality kódu

### 2.1 Pridané konfiguračné súbory

| Súbor | Účel |
|-------|-------|
| `.eslintrc.json` | Pravidlá lintovania JavaScriptu/TypeScriptu |
| `.prettierrc` | Štandardy formátovania kódu |
| `pyproject.toml` | Konfigurácia nástrojov pre Python (Black, Ruff, mypy) |

### 2.2 Vytvorené zdieľané utilitky

Nový modul `shared/python/` obsahujúci:
- `env_utils.py` - Spracovanie environmentálnych premenných
- `input_validation.py` - Validácia a sanitizácia vstupov
- `api_utils.py` - Bezpečné obaly pre API požiadavky

### 2.3 Odporúčané zlepšenia kódu

1. **Pokrytie type hintmi**
   - Pridať type hinty do všetkých Python súborov
   - Povoliť prísny režim pre TypeScript vo všetkých TS projektoch

2. **Štandardy dokumentácie**
   - Pridať docstringy ku všetkým Python funkciám
   - Pridať JSDoc komentáre ku všetkým JavaScript/TypeScript funkciám

3. **Testovací rámec**
   - Pridať konfiguráciu pytest a príkladové testy
   - Pridať konfiguráciu Jest pre JavaScript/TypeScript

---

## 3. Vylepšenia vzdelávania

### 3.1 Nové témy lekcií

1. **Bezpečnosť vo AI aplikáciách** (Navrhovaná lekcia 22)
   - Útoky spojené s prompt injection a obrany proti nim
   - Správa API kľúčov
   - Moderovanie obsahu
   - Obmedzenie rýchlosti a prevencia zneužitia

2. **Nasadenie do produkcie** (Navrhovaná lekcia 23)
   - Kontajnerizácia s Dockerom
   - CI/CD pipeline
   - Monitorovanie a logovanie
   - Manažment nákladov

3. **Pokročilé RAG techniky** (Navrhovaná lekcia 24)
   - Hybridné vyhľadávanie (kľúčové slová + sémantické)
   - Stratégie re-ranking-u
   - Multi-modálny RAG
   - Metódy hodnotenia

### 3.2 Zlepšenia existujúcich lekcií

| Lekcia | Odporúčané vylepšenie |
|--------|-----------------------|
| 06 - Generovanie textu | Pridať príklady streamovanej odpovede |
| 07 - Chatové aplikácie | Pridať vzory pre pamäť konverzácie |
| 08 - Vyhľadávacie aplikácie | Pridať porovnanie vektorových databáz |
| 09 - Generovanie obrázkov | Pridať príklady úprav/variantov obrázkov |
| 11 - Volanie funkcií | Pridať paralelné volanie funkcií |
| 15 - RAG | Pridať porovnanie stratégií chunkovania |
| 17 - AI agenti | Pridať orchestráciu viacerých agentov |

---

## 4. Modernizácia API

### 4.1 Zastarané API vzory na aktualizáciu

| Starý vzor | Nový vzor | Súbory, ktoré sa týkajú |
|------------|-----------|------------------------|
| `openai.api_type = "azure"` | klient `AzureOpenAI()` | Viaceré súbory v `08-building-search-applications/` |
| `openai.ChatCompletion.create()` | `client.chat.completions.create()` | Viaceré notebooky |
| `df.append()` (pandas) | `pd.concat()` | RAG notebook |

### 4.2 Nové API funkcie na demonštráciu

1. **Štruktúrované výstupy** (OpenAI)
   - Režim JSON
   - Volanie funkcií so striktnými schémami

2. **Vizuálne schopnosti**
   - Analýza obrázkov s GPT-4V
   - Multi-modálne prompty

3. **API asistenti**
   - Interpret kódu
   - Vyhľadávanie súborov
   - Vlastné nástroje

---

## 5. Vylepšenia infraštruktúry

### 5.1 Vylepšenia CI/CD

Súčasné workflow zvládajú validáciu markdownu. Odporúčané prídavky:

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

### 5.2 Bezpečnostné skenovanie

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

## 6. Vylepšenia vývoja

### 6.1 Vylepšenia DevContainer

Aktualizovať `.devcontainer/devcontainer.json`:

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

### 6.2 Interaktívne playgroundy

Zvážiť pridanie:
- Jupyter notebookov s predvyplnenými API kľúčmi (cez env)
- Gradio/Streamlit demá pre vizuálnych študentov
- Interaktívne kvízy na overenie vedomostí

---

## 7. Podpora viacerých jazykov

### 7.1 Súčasné pokrytie jazykov

| Technológia | Pokryté lekcie | Stav |
|-------------|----------------|------|
| Python      | Všetky         | Kompletné |
| TypeScript  | 06-09, 11      | Čiastočné |
| JavaScript  | 06-08, 11      | Čiastočné |
| .NET/C#     | Niektoré       | Čiastočné |

### 7.2 Odporúčané rozšírenia

1. **Go** - Rastuaci nástroj pre AI/ML
2. **Rust** - Aplikácie citlivé na výkon
3. **Java/Kotlin** - Podnikové aplikácie

---

## 8. Optimalizácie výkonu

### 8.1 Optimalizácie na úrovni kódu

1. **Async/Await vzory**
   - Pridať asynchrónne príklady pre spracovanie dávok
   - Demonštrovať súbežné API volania

2. **Stratégie cachovania**
   - Pridať príklady cachovania embeddingov
   - Demonštrovať vzory cachovania odpovedí

3. **Optimalizácia tokenov**
   - Pridať príklady použitia tiktoken
   - Demonštrovať techniky kompresie promptov

### 8.2 Príklady optimalizácie nákladov

Pridať príklady demonštrujúce:
- Výber modelu na základe zložitosti úlohy
- Prompt engineering pre efektívne tokeny
- Spracovanie dávok pre hromadné operácie

---

## 9. Prístupnosť a internacionalizácia

### 9.1 Súčasný stav prekladu

| Jazyk      | Stav       |
|------------|------------|
| Angličtina | Kompletné  |
| Čínština (zjednodušená) | Kompletné |
| Japončina  | Kompletné  |
| Kórejčina  | Kompletné  |
| Španielčina| Čiastočné  |
| Portugalčina | Čiastočné |
| Turečtina  | Čiastočné  |
| Poľština   | Čiastočné  |

### 9.2 Vylepšenia prístupnosti

1. Pridať alt text ku všetkým obrázkom
2. Zabezpečiť správne zvýraznenie syntaxe v ukážkach kódu
3. Pridať prepisy videí ku všetkému video obsahu
4. Zabezpečiť kontrast farieb podľa WCAG smerníc

---

## 10. Priorita implementácie

### Fáza 1: Okamžité (Týždeň 1-2)
- [x] Opraviť kritické bezpečnostné problémy
- [x] Pridať konfiguráciu na kvalitu kódu
- [x] Vytvoriť zdieľané utilitky
- [x] Zdokumentovať bezpečnostné pokyny

### Fáza 2: Krátkodobé (Týždeň 3-4)
- [ ] Aktualizovať zastarané API vzory
- [ ] Pridať type hinty do všetkých Python súborov
- [ ] Pridať CI/CD workflow pre kvalitu kódu
- [ ] Vytvoriť workflow pre bezpečnostné skenovanie

### Fáza 3: Strednodobé (Mesiac 2-3)
- [ ] Pridať novú lekciu o bezpečnosti
- [ ] Pridať lekciu o nasadení do produkcie
- [ ] Zlepšiť nastavenie DevContainer
- [ ] Pridať interaktívne demo

### Fáza 4: Dlhodobé (Mesiac 4+)
- [ ] Pridať pokročilú lekciu RAG
- [ ] Rozšíriť pokrytie jazykov
- [ ] Pridať komplexnú testovaciu sadu
- [ ] Vytvoriť certifikačný program

---

## Záver

Táto roadmapa poskytuje štruktúrovaný prístup k vylepšovaniu kurzu Generatívnej AI pre Začiatočníkov. Riešením bezpečnostných otázok, modernizáciou API a pridaním vzdelávacieho obsahu bude kurz lepšie pripravený na vývoj skutočných AI aplikácií.

Pre otázky alebo príspevky, prosím, otvorte issue na GitHub repozitári.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte, prosím, na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z používania tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->