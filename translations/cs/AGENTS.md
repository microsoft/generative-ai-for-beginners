<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:10:04+00:00",
  "source_file": "AGENTS.md",
  "language_code": "cs"
}
-->
# AGENTS.md

## Přehled projektu

Tento repozitář obsahuje komplexní učební plán o 21 lekcích, který učí základy generativní AI a vývoj aplikací. Kurz je určen pro začátečníky a pokrývá vše od základních konceptů až po tvorbu aplikací připravených pro produkci.

**Klíčové technologie:**
- Python 3.9+ s knihovnami: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript s Node.js a knihovnami: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API a GitHub Models
- Jupyter Notebooks pro interaktivní učení
- Dev Containers pro konzistentní vývojové prostředí

**Struktura repozitáře:**
- 21 očíslovaných adresářů lekcí (00-21) obsahujících README, příklady kódu a úkoly
- Více implementací: Python, TypeScript a někdy i příklady v .NET
- Adresář překladů s více než 40 jazykovými verzemi
- Centralizovaná konfigurace prostřednictvím souboru `.env` (použijte `.env.copy` jako šablonu)

## Příkazy pro nastavení

### Počáteční nastavení repozitáře

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Nastavení prostředí Python

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Nastavení Node.js/TypeScript

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Nastavení Dev Container (doporučeno)

Repozitář obsahuje konfiguraci `.devcontainer` pro GitHub Codespaces nebo VS Code Dev Containers:

1. Otevřete repozitář v GitHub Codespaces nebo VS Code s rozšířením Dev Containers
2. Dev Container automaticky:
   - Nainstaluje Python závislosti ze souboru `requirements.txt`
   - Spustí skript po vytvoření (`.devcontainer/post-create.sh`)
   - Nastaví Jupyter kernel

## Vývojový pracovní postup

### Proměnné prostředí

Všechny lekce vyžadující přístup k API používají proměnné prostředí definované v `.env`:

- `OPENAI_API_KEY` - Pro OpenAI API
- `AZURE_OPENAI_API_KEY` - Pro Azure OpenAI Service
- `AZURE_OPENAI_ENDPOINT` - URL endpointu Azure OpenAI
- `AZURE_OPENAI_DEPLOYMENT` - Název nasazení modelu pro chat completion
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Název nasazení modelu pro embeddings
- `AZURE_OPENAI_API_VERSION` - Verze API (výchozí: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Pro modely Hugging Face
- `GITHUB_TOKEN` - Pro GitHub Models

### Spouštění Python příkladů

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### Spouštění TypeScript příkladů

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Spouštění Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Práce s různými typy lekcí

- **Lekce "Learn"**: Zaměřují se na dokumentaci README.md a koncepty
- **Lekce "Build"**: Obsahují funkční příklady kódu v Pythonu a TypeScriptu
- Každá lekce má README.md s teorií, průvodcem kódem a odkazy na video obsah

## Pokyny pro styl kódu

### Python

- Používejte `python-dotenv` pro správu proměnných prostředí
- Importujte knihovnu `openai` pro interakce s API
- Používejte `pylint` pro lintování (některé příklady obsahují `# pylint: disable=all` pro zjednodušení)
- Dodržujte konvence pojmenování podle PEP 8
- Uchovávejte API přihlašovací údaje v souboru `.env`, nikdy v kódu

### TypeScript

- Používejte balíček `dotenv` pro proměnné prostředí
- Konfigurace TypeScriptu v `tsconfig.json` pro každou aplikaci
- Používejte `@azure/openai` nebo `@azure-rest/ai-inference` pro služby Azure
- Používejte `nodemon` pro vývoj s automatickým reloadem
- Před spuštěním sestavte: `npm run build` a poté `npm start`

### Obecné konvence

- Udržujte příklady kódu jednoduché a vzdělávací
- Zahrňte komentáře vysvětlující klíčové koncepty
- Kód každé lekce by měl být samostatný a spustitelný
- Používejte konzistentní pojmenování: prefix `aoai-` pro Azure OpenAI, `oai-` pro OpenAI API, `githubmodels-` pro GitHub Models

## Pokyny pro dokumentaci

### Styl Markdown

- Všechny URL musí být obaleny ve formátu `[text](../../url)` bez dalších mezer
- Relativní odkazy musí začínat `./` nebo `../`
- Všechny odkazy na domény Microsoftu musí obsahovat tracking ID: `?WT.mc_id=academic-105485-koreyst`
- Žádné lokální specifické URL (vyhněte se `/en-us/`)
- Obrázky uložené ve složce `./images` s popisnými názvy
- Používejte anglické znaky, čísla a pomlčky v názvech souborů

### Podpora překladů

- Repozitář podporuje více než 40 jazyků prostřednictvím automatizovaných GitHub Actions
- Překlady jsou uloženy v adresáři `translations/`
- Nepodávejte částečné překlady
- Strojové překlady nejsou přijímány
- Přeložené obrázky jsou uloženy v adresáři `translated_images/`

## Testování a validace

### Kontroly před odesláním

Tento repozitář používá GitHub Actions pro validaci. Před odesláním PR:

1. **Kontrola odkazů v Markdown**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Ruční testování**:
   - Testujte Python příklady: Aktivujte venv a spusťte skripty
   - Testujte TypeScript příklady: `npm install`, `npm run build`, `npm start`
   - Ověřte, že proměnné prostředí jsou správně nakonfigurovány
   - Zkontrolujte, že API klíče fungují s příklady kódu

3. **Příklady kódu**:
   - Ujistěte se, že všechny kódy běží bez chyb
   - Testujte s Azure OpenAI i OpenAI API, pokud je to možné
   - Ověřte, že příklady fungují s GitHub Models, kde je to podporováno

### Žádné automatizované testy

Toto je vzdělávací repozitář zaměřený na tutoriály a příklady. Neexistují žádné jednotkové nebo integrační testy. Validace je primárně:
- Ruční testování příkladů kódu
- GitHub Actions pro validaci Markdown
- Komunitní recenze vzdělávacího obsahu

## Pokyny pro pull requesty

### Před odesláním

1. Testujte změny kódu v Pythonu i TypeScriptu, pokud je to relevantní
2. Spusťte validaci Markdown (automaticky spuštěno při PR)
3. Ujistěte se, že všechny Microsoft URL obsahují tracking ID
4. Zkontrolujte, že relativní odkazy jsou platné
5. Ověřte, že obrázky jsou správně odkazovány

### Formát názvu PR

- Používejte popisné názvy: `[Lekce 06] Oprava překlepu v Python příkladu` nebo `Aktualizace README pro lekci 08`
- Odkazujte na čísla problémů, pokud je to relevantní: `Fixes #123`

### Popis PR

- Vysvětlete, co bylo změněno a proč
- Odkazujte na související problémy
- U změn kódu specifikujte, které příklady byly testovány
- U překladů PR zahrňte všechny soubory pro kompletní překlad

### Požadavky na příspěvky

- Podepište Microsoft CLA (automaticky při prvním PR)
- Forkujte repozitář do svého účtu před provedením změn
- Jeden PR na jednu logickou změnu (nekombinujte nesouvisející opravy)
- Udržujte PR zaměřené a co nejmenší

## Běžné pracovní postupy

### Přidání nového příkladu kódu

1. Přejděte do příslušného adresáře lekce
2. Vytvořte příklad v podadresáři `python/` nebo `typescript/`
3. Dodržujte konvenci pojmenování: `{provider}-{example-name}.{py|ts|js}`
4. Testujte s aktuálními API přihlašovacími údaji
5. Dokumentujte nové proměnné prostředí v README lekce

### Aktualizace dokumentace

1. Upravte README.md v adresáři lekce
2. Dodržujte pokyny pro Markdown (tracking ID, relativní odkazy)
3. Aktualizace překladů jsou zpracovány GitHub Actions (neupravujte ručně)
4. Testujte, že všechny odkazy jsou platné

### Práce s Dev Containers

1. Repozitář obsahuje `.devcontainer/devcontainer.json`
2. Skript po vytvoření automaticky nainstaluje Python závislosti
3. Rozšíření pro Python a Jupyter jsou předem nakonfigurována
4. Prostředí je založeno na `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Nasazení a publikování

Toto je vzdělávací repozitář - neexistuje proces nasazení. Učební plán je využíván:

1. **GitHub Repozitář**: Přímý přístup ke kódu a dokumentaci
2. **GitHub Codespaces**: Okamžité vývojové prostředí s předem nakonfigurovaným nastavením
3. **Microsoft Learn**: Obsah může být syndikován na oficiální vzdělávací platformu
4. **docsify**: Dokumentační web vytvořený z Markdown (viz `docsifytopdf.js` a `package.json`)

### Vytvoření dokumentačního webu

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Řešení problémů

### Běžné problémy

**Chyby importu Pythonu**:
- Ujistěte se, že je aktivováno virtuální prostředí
- Spusťte `pip install -r requirements.txt`
- Zkontrolujte, že verze Pythonu je 3.9+

**Chyby sestavení TypeScriptu**:
- Spusťte `npm install` ve specifickém adresáři aplikace
- Zkontrolujte, že verze Node.js je kompatibilní
- Vymažte `node_modules` a znovu nainstalujte, pokud je to nutné

**Chyby autentizace API**:
- Ověřte, že soubor `.env` existuje a má správné hodnoty
- Zkontrolujte, že API klíče jsou platné a nevypršely
- Ujistěte se, že URL endpointů jsou správné pro váš region

**Chybějící proměnné prostředí**:
- Zkopírujte `.env.copy` do `.env`
- Vyplňte všechny požadované hodnoty pro lekci, na které pracujete
- Restartujte aplikaci po aktualizaci `.env`

## Další zdroje

- [Průvodce nastavením kurzu](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Pokyny pro přispívání](./CONTRIBUTING.md)
- [Kodex chování](./CODE_OF_CONDUCT.md)
- [Bezpečnostní politika](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Sbírka pokročilých příkladů kódu](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Poznámky specifické pro projekt

- Toto je **vzdělávací repozitář** zaměřený na učení, nikoli produkční kód
- Příklady jsou záměrně jednoduché a zaměřené na výuku konceptů
- Kvalita kódu je vyvážena srozumitelností pro vzdělávací účely
- Každá lekce je samostatná a může být dokončena nezávisle
- Repozitář podporuje více poskytovatelů API: Azure OpenAI, OpenAI a GitHub Models
- Obsah je vícejazyčný s automatizovanými pracovními postupy překladu
- Aktivní komunita na Discordu pro dotazy a podporu

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.