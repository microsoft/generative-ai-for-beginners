# Plán vylepšení a zlepšení funkcí

Tento dokument shrnuje doporučená vylepšení a zlepšení kurikula Generative AI for Beginners na základě komplexní revize kódu a analýzy osvědčených postupů v oboru.

## Výkonný souhrn

Kódová základna byla analyzována z hlediska bezpečnosti, kvality kódu a vzdělávací efektivity. Tento dokument poskytuje doporučení pro okamžité opravy, krátkodobá vylepšení a budoucí rozšíření.

---

## 1. Vylepšení bezpečnosti (priorita: kritické)

### 1.1 Okamžité opravy (dokončeno)

| Problém | Ovlivněné soubory | Stav |
|---------|-------------------|------|
| Tvrdě zakódovaný SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Opraveno |
| Chybějící validace prostředí | Více JS/TS souborů | Opraveno |
| Nezabezpečené volání funkcí | `11-integrating-with-function-calling/js-githubmodels/app.js` | Opraveno |
| Úniky souborových handlerů | `08-building-search-applications/scripts/` | Opraveno |
| Chybějící timeouty požadavků | `09-building-image-applications/python/` | Opraveno |

### 1.2 Doporučené další bezpečnostní funkce

1. **Příklady omezování rychlosti (Rate Limiting)**
   - Přidat příkladový kód ukazující implementaci omezení rychlosti API volání
   - Ukázat vzory exponenciálního zpomalování

2. **Rotace API klíčů**
   - Přidat dokumentaci ohledně osvědčených postupů rotace API klíčů
   - Zahrnout příklady použití Azure Key Vault nebo podobných služeb

3. **Integrace ochrany obsahu**
   - Přidat příklady použití Azure Content Safety API
   - Ukázat vzory moderování vstupu/výstupu

---

## 2. Zlepšení kvality kódu

### 2.1 Přidány konfigurační soubory

| Soubor | Účel |
|--------|-------|
| `.eslintrc.json` | Pravidla lintování JavaScript/TypeScript |
| `.prettierrc` | Standardy formátování kódu |
| `pyproject.toml` | Konfigurace nástrojů pro Python (Black, Ruff, mypy) |

### 2.2 Vytvořeny sdílené utility

Nový modul `shared/python/` obsahuje:
- `env_utils.py` - práce s proměnnými prostředí
- `input_validation.py` - validace a sanitizace vstupů
- `api_utils.py` - bezpečné obálky pro API požadavky

### 2.3 Doporučená vylepšení kódu

1. **Pokrytí typovou anotací**
   - Přidat typové anotace do všech Python souborů
   - Zapnout přísný režim TypeScript ve všech TS projektech

2. **Standardy dokumentace**
   - Přidat docstringy ke všem Python funkcím
   - Přidat JSDoc komentáře ke všem JavaScript/TypeScript funkcím

3. **Testovací rámec**
   - Přidat konfiguraci pytest a ukázkové testy
   - Přidat konfiguraci Jest pro JavaScript/TypeScript

---

## 3. Vzdělávací vylepšení

### 3.1 Nová témata lekcí

1. **Bezpečnost v AI aplikacích** (navrhovaná lekce 22)
   - Útoky založené na prompt injection a obrana proti nim
   - Správa API klíčů
   - Moderace obsahu
   - Omezování rychlosti a prevence zneužití

2. **Nasazení do produkce** (navrhovaná lekce 23)
   - Kontejnerizace s Dockerem
   - CI/CD pipeline
   - Monitoring a logování
   - Řízení nákladů

3. **Pokročilé techniky RAG** (navrhovaná lekce 24)
   - Hybridní vyhledávání (klíčová slova + sémantické)
   - Strategie přeřazování výsledků
   - Multimodální RAG
   - Měřítka hodnocení

### 3.2 Zlepšení stávajících lekcí

| Lekce | Doporučené vylepšení |
|--------|---------------------|
| 06 - Generování textu | Přidat příklady streamovaného výstupu |
| 07 - Chatovací aplikace | Přidat vzory paměti konverzace |
| 08 - Vyhledávací aplikace | Přidat porovnání vektorových databází |
| 09 - Generování obrázků | Přidat příklady úprav/variací obrázků |
| 11 - Volání funkcí | Přidat paralelní volání funkcí |
| 15 - RAG | Přidat porovnání strategií dělení chunků |
| 17 - AI agenti | Přidat orchestraci více agentů |

---

## 4. Modernizace API

### 4.1 Zastaralé vzory API k aktualizaci

| Starý vzor | Nový vzor | Ovlivněné soubory |
|------------|-----------|-------------------|
| `openai.api_type = "azure"` | klient `AzureOpenAI()` | Více skriptů v `08-building-search-applications/` |
| `openai.ChatCompletion.create()` | `client.chat.completions.create()` | Více notebooků |
| `df.append()` (pandas) | `pd.concat()` | Notebook RAG |

### 4.2 Nové funkce API k demonstrování

1. **Strukturované výstupy** (OpenAI)
   - JSON režim
   - Volání funkcí s přísnými schématy

2. **Vision schopnosti**
   - Analýza obrázků s GPT-4V
   - Multimodální promptování

3. **API pro asistenty**
   - Interpret kódu
   - Vyhledávání souborů
   - Vlastní nástroje

---

## 5. Zlepšení infrastruktury

### 5.1 Rozšíření CI/CD

Současné workflow zajišťují validaci markdownu. Doporučená rozšíření:

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

## 6. Zlepšení zkušenosti vývojáře

### 6.1 Vylepšení DevContaineru

Aktualizace `.devcontainer/devcontainer.json`:

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

### 6.2 Interaktivní playground

Zvážit přidání:
- Jupyter notebooků s předvyplněnými API klíči (pomocí prostředí)
- Gradio/Streamlit ukázek pro vizuální typy
- Interaktivních kvízů pro ověření znalostí

---

## 7. Podpora více jazyků

### 7.1 Současné pokrytí jazyků

| Technologie | Pokryté lekce | Stav |
|-------------|--------------|------|
| Python | Všechny | Kompletní |
| TypeScript | 06-09, 11 | Částečné |
| JavaScript | 06-08, 11 | Částečné |
| .NET/C# | Některé | Částečné |

### 7.2 Doporučená rozšíření

1. **Go** - Narůstající v AI/ML nástrojích  
2. **Rust** - Výkonově kritické aplikace  
3. **Java/Kotlin** - Podnikové aplikace  

---

## 8. Optimalizace výkonu

### 8.1 Optimalizace na úrovni kódu

1. **Vzory async/await**
   - Přidat async příklady pro zpracování dávky
   - Ukázat paralelní API volání

2. **Caching strategie**
   - Přidat příklady kešování embeddingů
   - Ukázat vzory kešování odpovědí

3. **Optimalizace tokenů**
   - Přidat příklady používání tiktoken
   - Ukázat techniky komprese promptů

### 8.2 Příklady optimalizací nákladů

Přidat příklady ukazující:
- Výběr modelu dle složitosti úkolu
- Prompt engineering pro efektivitu tokenů
- Dávkové zpracování pro hromadné operace

---

## 9. Přístupnost a internacionalizace

### 9.1 Stav překladů

| Jazyk | Stav |
|-------|------|
| Angličtina | Kompletní |
| Čínština (zjednodušená) | Kompletní |
| Japonština | Kompletní |
| Korejština | Kompletní |
| Španělština | Částečná |
| Portugalština | Částečná |
| Turečtina | Částečná |
| Polština | Částečná |

### 9.2 Zlepšení přístupnosti

1. Přidat alt text ke všem obrázkům  
2. Zajistit správné zvýraznění syntaxe v ukázkách kódu  
3. Přidat přepisy videí ke všem video materiálům  
4. Zajistit barevný kontrast v souladu s WCAG směrnicemi  

---

## 10. Priorita implementace

### Fáze 1: Okamžité (týdny 1-2)
- [x] Opravit kritické bezpečnostní problémy
- [x] Přidat konfiguraci kvality kódu
- [x] Vytvořit sdílené utility
- [x] Zdokumentovat bezpečnostní pokyny

### Fáze 2: Krátkodobé (týdny 3-4)
- [ ] Aktualizovat zastaralé API vzory
- [ ] Přidat typové anotace do všech Python souborů
- [ ] Přidat CI/CD workflow pro kvalitu kódu
- [ ] Vytvořit workflow pro bezpečnostní skenování

### Fáze 3: Střednědobé (měsíce 2-3)
- [ ] Přidat novou bezpečnostní lekci
- [ ] Přidat lekci o produkčním nasazení
- [ ] Vylepšit nastavení DevContaineru
- [ ] Přidat interaktivní ukázky

### Fáze 4: Dlouhodobé (měsíc 4+)
- [ ] Přidat pokročilou lekci RAG
- [ ] Rozšířit pokrytí jazyků
- [ ] Přidat komplexní testovací sadu
- [ ] Vytvořit certifikační program

---

## Závěr

Tento plán nabízí strukturovaný přístup ke zlepšení kurikula Generative AI for Beginners. Řešením bezpečnostních problémů, modernizací API a rozšiřováním vzdělávacího obsahu bude kurz lépe připravovat studenty na vývoj AI aplikací v reálném světě.

Pro dotazy nebo příspěvky prosím otevřete issue v GitHub repozitáři.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za závazný zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nepřebíráme žádnou odpovědnost za případné nedorozumění nebo nesprávné výklady vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->