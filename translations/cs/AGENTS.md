# AGENTS.md

## Přehled projektu

Tento repozitář obsahuje komplexní kurikulum se 21 lekcemi, které učí základy Generativní AI a vývoj aplikací. Kurz je určen pro začátečníky a pokrývá vše od základních konceptů až po tvorbu aplikací připravených pro produkci.

**Klíčové technologie:**
- Python 3.9+ s knihovnami: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript s Node.js a knihovnami: `openai` (Azure OpenAI přes v1 endpoint + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API a Microsoft Foundry Models (GitHub Models bude ukončen koncem července 2026)
- Jupyter Notebooks pro interaktivní učení
- Dev kontejnery pro konzistentní vývojové prostředí

**Struktura repozitáře:**
- 21 číslovaných adresářů lekcí (00-21) obsahujících README, příklady kódu a úkoly
- Více implementací: Python, TypeScript a někdy příklady .NET
- Adresář překladů s více než 40 jazykovými verzemi
- Centralizovaná konfigurace přes `.env` soubor (použijte `.env.copy` jako šablonu)

## Příkazy pro nastavení

### Počáteční nastavení repozitáře

```bash
# Naklonujte repozitář
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Zkopírujte šablonu prostředí
cp .env.copy .env
# Upravte .env se svými klíči API a koncovými body
```

### Nastavení Python prostředí

```bash
# Vytvořit virtuální prostředí
python3 -m venv venv

# Aktivovat virtuální prostředí
# Na macOS/Linuxu:
source venv/bin/activate
# Na Windows:
venv\Scripts\activate

# Nainstalovat závislosti
pip install -r requirements.txt
```

### Nastavení Node.js/TypeScript

```bash
# Nainstalujte závislosti na úrovni root (pro nástroje dokumentace)
npm install

# Pro jednotlivé příklady TypeScript lekcí přejděte do konkrétní lekce:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Nastavení Dev kontejneru (doporučeno)

Repozitář obsahuje konfiguraci `.devcontainer` pro GitHub Codespaces nebo VS Code Dev kontejnery:

1. Otevřete repozitář v GitHub Codespaces nebo ve VS Code s rozšířením Dev Containers
2. Dev kontejner automaticky:
   - Nainstaluje Python závislosti z `requirements.txt`
   - Spustí post-create skript (`.devcontainer/post-create.sh`)
   - Nastaví Jupyter kernel

## Vývojový workflow

### Environment Variables

Všechny lekce vyžadující přístup k API používají proměnné prostředí definované v `.env`:

- `OPENAI_API_KEY` - Pro OpenAI API
- `AZURE_OPENAI_API_KEY` - Pro Azure OpenAI v Microsoft Foundry (Azure OpenAI Service je nyní součástí Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL koncového bodu Azure OpenAI (Foundry resource endpoint)
- `AZURE_OPENAI_DEPLOYMENT` - Název deploymentu modelu pro chat completions
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Název deploymentu modelu embeddings
- `AZURE_OPENAI_API_VERSION` - Verze API (výchozí: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Pro modely Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - Endpoint Microsoft Foundry Models (katalog modelů od více poskytovatelů)
- `AZURE_INFERENCE_CREDENTIAL` - API klíč Microsoft Foundry Models (nahrazuje ukončený `GITHUB_TOKEN`)

### Spouštění Python příkladů

```bash
# Přejděte do adresáře lekce
cd 06-text-generation-apps/python

# Spusťte skript Pythonu
python aoai-app.py
```

### Spouštění TypeScript příkladů

```bash
# Přejděte do adresáře aplikace TypeScript
cd 06-text-generation-apps/typescript/recipe-app

# Sestavte kód TypeScript
npm run build

# Spusťte aplikaci
npm start
```

### Spouštění Jupyter Notebooks

```bash
# Spusťte Jupyter v kořenovém adresáři repozitáře
jupyter notebook

# Nebo použijte VS Code s rozšířením Jupyter
```

### Práce s různými typy lekcí

- **Lekce typu "Learn"**: Zaměřují se na dokumentaci README.md a koncepty
- **Lekce typu "Build"**: Obsahují funkční příklady v Pythonu a TypeScriptu
- Každá lekce má README.md s teorií, průchodem kódu a odkazy na video obsah

## Směrnice pro styl kódu

### Python

- Používejte `python-dotenv` pro správu proměnných prostředí
- Importujte knihovnu `openai` pro interakci s API
- Používejte `pylint` pro linting (některé příklady obsahují `# pylint: disable=all` pro zjednodušení)
- Dodržujte pojmenovací konvence PEP 8
- Ukládejte API přihlašovací údaje do `.env` souboru, nikdy přímo v kódu

### TypeScript

- Používejte balíček `dotenv` pro proměnné prostředí
- Konfigurace TypeScriptu je v `tsconfig.json` pro každou aplikaci
- Používejte balíček `openai` pro Azure OpenAI (klienta směřujte na endpoint `/openai/v1/` a volejte `client.responses.create`); použijte `@azure-rest/ai-inference` pro Microsoft Foundry Models
- Používejte `nodemon` pro vývoj s automatickým restartem
- Před spuštěním spusťte sestavení: `npm run build` a poté `npm start`

### Obecné konvence

- Udržujte příklady kódu jednoduché a vzdělávací
- Přidávejte komentáře vysvětlující klíčové koncepty
- Kód každé lekce by měl být samostatný a spustitelný
- Používejte konzistentní pojmenování: prefix `aoai-` pro Azure OpenAI, `oai-` pro OpenAI API, `githubmodels-` pro Microsoft Foundry Models (zachovaný legacy prefix z éry GitHub Models)

## Směrnice pro dokumentaci

### Markdown styl

- Všechny URL adresy musí být zabaleny v `[text](../../url)` formátu bez mezer navíc
- Relativní odkazy musí začínat `./` nebo `../`
- Všechny odkazy na domény Microsoftu musí obsahovat tracking ID: `?WT.mc_id=academic-105485-koreyst`
- Žádné lokalizace specifické pro zemi v URL adrese (vyhněte se `/en-us/`)
- Obrázky jsou uloženy ve složce `./images` s popisnými názvy
- Používejte anglické znaky, čísla a pomlčky v názvech souborů

### Podpora překladů

- Repozitář podporuje více než 40 jazyků prostřednictvím automatizovaných GitHub Actions
- Překlady jsou uloženy v adresáři `translations/`
- Neposílejte částečné překlady
- Strojové překlady nejsou akceptovány
- Přeložené obrázky jsou uloženy v adresáři `translated_images/`

## Testování a validace

### Kontroly před odesláním

Tento repozitář používá GitHub Actions pro validaci. Před odesláním PR:

1. **Zkontrolujte Markdown odkazy**:
   ```bash
   # Workflow validate-markdown.yml kontroluje:
   # - Poškozené relativní cesty
   # - Chybějící sledovací ID na cestách
   # - Chybějící sledovací ID na URL adresách
   # - URL adresy s místním nastavením země
   # - Poškozené externí URL adresy
   ```

2. **Manuální testování**:
   - Otestujte Python příklady: Aktivujte venv a spusťte skripty
   - Otestujte TypeScript příklady: `npm install`, `npm run build`, `npm start`
   - Ověřte správné nastavení proměnných prostředí
   - Zkontrolujte, že API klíče fungují s příklady kódu

3. **Příklady kódu**:
   - Zajistěte, že celý kód běží bez chyb
   - Testujte s oběma: Azure OpenAI a OpenAI API, pokud je to možné
   - Ověřte, že příklady fungují s Microsoft Foundry Models tam, kde je podpora

### Žádné automatizované testy

Toto je vzdělávací repozitář zaměřený na tutoriály a příklady. Nejsou zde žádné jednotkové nebo integrační testy k spuštění. Validace zahrnuje především:
- Manuální testování příkladů kódu
- GitHub Actions pro validaci Markdown
- Komunitní kontrola vzdělávacího obsahu

## Směrnice pro Pull Requesty

### Před odesláním

1. Otestujte změny kódu v Pythonu i TypeScriptu, pokud je to možné
2. Spusťte validaci Markdown (automaticky spuštěno na PR)
3. Ujistěte se, že tracking ID jsou na všech Microsoft URL adresách
4. Zkontrolujte, že relativní odkazy jsou platné
5. Ověřte správné odkazy na obrázky

### Formát názvu PR

- Používejte popisné názvy: `[Lesson 06] Fix Python example typo` nebo `Update README for lesson 08`
- Pokud je to vhodné, odkazujte na čísla issue: `Fixes #123`

### Popis PR

- Vysvětlete, co bylo změněno a proč
- Přidejte odkazy na související issues
- U kódových změn uveďte, které příklady byly testovány
- U překladových PR zahrňte všechny soubory pro kompletní překlad

### Požadavky na příspěvky

- Podepište Microsoft CLA (automatické při prvním PR)
- Před úpravami proveďte fork repozitáře na svůj účet
- Jeden PR na jednu logickou změnu (neslučujte nesouvisející opravy)
- Pokud možno držte PR malé a zaměřené

## Běžné workflow

### Přidání nového příkladu kódu

1. Přejděte do odpovídajícího adresáře lekce
2. Vytvořte příklad v podadresáři `python/` nebo `typescript/`
3. Dodržujte pojmenovací konvenci: `{provider}-{example-name}.{py|ts|js}`
4. Otestujte s aktuálními API přihlašovacími údaji
5. Zdokumentujte nové proměnné prostředí v README lekce

### Aktualizace dokumentace

1. Upravte README.md v adresáři lekce
2. Dodržujte Markdown směrnice (tracking ID, relativní odkazy)
3. Aktualizace překladů zajišťují GitHub Actions (neupravujte ručně)
4. Otestujte, že všechny odkazy jsou platné

### Práce s Dev kontejnery

1. Repozitář obsahuje `.devcontainer/devcontainer.json`
2. Post-create skript automaticky instaluje Python závislosti
3. Rozšíření pro Python a Jupyter jsou přednastavená
4. Prostředí je založeno na `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Deployment a publikace

Toto je vzdělávací repozitář – žádný proces nasazení neexistuje. Kurikulum je využíváno:

1. **GitHub Repozitář**: Přímý přístup ke kódu a dokumentaci
2. **GitHub Codespaces**: Okamžité vývojové prostředí s předkonfigurovaným nastavením
3. **Microsoft Learn**: Obsah může být syndikován na oficiální vzdělávací platformu
4. **docsify**: Dokumentační web postavený na Markdownu (viz `docsifytopdf.js` a `package.json`)

### Tvorba dokumentačního webu

```bash
# Vygenerujte PDF z dokumentace (pokud je potřeba)
npm run convert
```

## Řešení problémů

### Běžné problémy

**Chyby importu v Pythonu**:
- Ujistěte se, že je aktivováno virtuální prostředí
- Spusťte `pip install -r requirements.txt`
- Zkontrolujte, že verze Pythonu je 3.9+

**Chyby při sestavování TypeScriptu**:
- Spusťte `npm install` ve specifickém adresáři aplikace
- Zkontrolujte kompatibilní verzi Node.js
- Vymažte `node_modules` a znovu nainstalujte, pokud je potřeba

**Chyby autentifikace API**:
- Ověřte, že `.env` soubor existuje a obsahuje správné hodnoty
- Zkontrolujte, že API klíče jsou platné a nevypršely
- Ujistěte se, že endpoint URL jsou správné pro váš region

**Chybějící proměnné prostředí**:
- Zkopírujte `.env.copy` na `.env`
- Vyplňte všechny požadované hodnoty pro lekci, na které pracujete
- Po aktualizaci `.env` restartujte aplikaci

## Další zdroje

- [Průvodce nastavením kurzu](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Směrnice pro příspěvky](./CONTRIBUTING.md)
- [Kodex chování](./CODE_OF_CONDUCT.md)
- [Zásady bezpečnosti](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Sbírka pokročilých ukázek kódu](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Poznámky specifické pro projekt

- Toto je **vzdělávací repozitář** zaměřený na učení, nikoli produkční kód
- Příklady jsou úmyslně jednoduché a zaměřené na výuku konceptů
- Kvalita kódu je vyvážena s jasností pro vzdělávání
- Každá lekce je samostatná a může být dokončena nezávisle
- Repozitář podporuje více API poskytovatelů: Azure OpenAI, OpenAI, Microsoft Foundry Models a offline poskytovatele jako Foundry Local a Ollama
- Obsah je vícejazyčný s automatizovanými překladatelskými workflowy
- Aktivní komunita na Discordu pro dotazy a podporu

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->