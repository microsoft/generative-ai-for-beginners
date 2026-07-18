# AGENTS.md

## Přehled projektu

Toto úložiště obsahuje rozsáhlý 21-lekcí učební plán učící základy generativní AI a vývoje aplikací. Kurz je navržen pro začátečníky a pokrývá vše od základních konceptů až po vytváření aplikací připravených pro produkci.

**Klíčové technologie:**
- Python 3.9+ s knihovnami: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript s Node.js a knihovnami: `openai` (Azure OpenAI přes v1 endpoint + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API a Microsoft Foundry Models (GitHub Models je na konci července 2026 ukončován)
- Jupyter Notebooks pro interaktivní učení
- Dev kontejnery pro konzistentní vývojové prostředí

**Struktura úložiště:**
- 21 číslovaných složek lekcí (00-21) obsahujících README, příklady kódu a úkoly
- Více implementací: Python, TypeScript a někdy .NET příklady
- Složka překladů s více než 40 jazykovými verzemi
- Centralizovaná konfigurace pomocí `.env` souboru (použijte `.env.copy` jako šablonu)

## Příkazy pro nastavení

### Inicializace úložiště

```bash
# Klonujte repozitář
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Zkopírujte šablonu prostředí
cp .env.copy .env
# Upravte soubor .env s vašimi API klíči a koncovými body
```

### Nastavení Python prostředí

```bash
# Vytvořit virtuální prostředí
python3 -m venv venv

# Aktivovat virtuální prostředí
# Na macOS/Linux:
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

# Pro jednotlivé příklady TypeScriptu z lekcí přejděte ke konkrétní lekci:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Nastavení Dev kontejneru (doporučeno)

Úložiště obsahuje konfiguraci `.devcontainer` pro GitHub Codespaces nebo VS Code Dev kontejnery:

1. Otevřete úložiště v GitHub Codespaces nebo VS Code s rozšířením Dev Containers
2. Dev Container automaticky:
   - Nainstaluje Python závislosti ze souboru `requirements.txt`
   - Spustí post-create skript (`.devcontainer/post-create.sh`)
   - Nastaví Jupyter kernel

## Vývojový pracovní postup

### Proměnné prostředí

Všechny lekce vyžadující přístup k API používají proměnné prostředí definované v `.env`:

- `OPENAI_API_KEY` - Pro OpenAI API
- `AZURE_OPENAI_API_KEY` - Pro Azure OpenAI v Microsoft Foundry (Azure OpenAI Service je nyní součástí Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL endpointu Azure OpenAI (endpoint Foundry resource)
- `AZURE_OPENAI_DEPLOYMENT` - Název deploymentu modelu pro chat completion (výchozí pro kurz: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Název deploymentu embeddings modelu (výchozí pro kurz: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - Verze API (výchozí: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Pro Hugging Face modely
- `AZURE_INFERENCE_ENDPOINT` - Endpoint Microsoft Foundry Models (katalog modelů s více poskytovateli)
- `AZURE_INFERENCE_CREDENTIAL` - API klíč Microsoft Foundry Models (nahrazuje ukončovaný `GITHUB_TOKEN`)
- `AZURE_INFERENCE_CHAT_MODEL` - Model bez reasoning (např. `Llama-3.3-70B-Instruct`) používaný v příkladech s `temperature`, protože reasoning modely nepodporují ovládací prvky vzorkování

### Konvence modelů (důležité)

- **Výchozí chat model je `gpt-5-mini`** - aktuální, nedeprecated **reasoning** model. Od roku 2026 starší mini modely s podporou temperature (`gpt-4o-mini`, `gpt-4.1-mini`) *bude ukončeny*, proto kurz standardizuje rodinu GPT-5.
- **Reasoning modely odmítají `temperature` a `top_p`**, místo toho používají `max_output_tokens` (Responses API) / `max_completion_tokens` (chat completions) místo `max_tokens`. **Nepřidávejte** `temperature`/`top_p`/`max_tokens` do ukázek volajících `gpt-5-mini`.
- **Pro demonstraci `temperature`** ukázky používají **Llama** model (`Llama-3.3-70B-Instruct`) přes endpoint Microsoft Foundry Models (`AZURE_INFERENCE_CHAT_MODEL`). Řiďte reasoning modely pomocí prompt engineering a reasoning ovládacích prvků místo sampling parametrů.
- **Fine-tuning (lekce 18)** používá stále `gpt-4.1-mini`: GPT-5 podporuje pouze reinforcement fine-tuning (RFT), ne supervised fine-tuning (SFT) jako tam uvedeno.
- Lekce 20 (Mistral) a 21 (Meta) používají `temperature`/`max_tokens`, protože cílují na Mistral/Llama modely, jež je podporují.

### Spouštění Python příkladů

```bash
# Přejděte do složky s lekcí
cd 06-text-generation-apps/python

# Spusťte Python skript
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

- **"Learn" lekce**: Zaměřují se na dokumentaci README.md a koncepty
- **"Build" lekce**: Obsahují fungující příklady kódu v Pythonu a TypeScriptu
- Každá lekce má README.md s teorií, popisem kódu a odkazy na video obsah

## Směrnice kódovacího stylu

### Python

- Používejte `python-dotenv` pro správu proměnných prostředí
- Importujte knihovnu `openai` pro interakce s API
- Používejte `pylint` pro linting (některé příklady obsahují `# pylint: disable=all` pro jednoduchost)
- Dodržujte pojmenovávací konvence PEP 8
- Ukládejte API klíče do `.env` souboru, nikdy ne v kódu

### TypeScript

- Používejte balíček `dotenv` pro proměnné prostředí
- Konfigurace TypeScriptu v `tsconfig.json` pro každou aplikaci
- Používejte balíček `openai` pro Azure OpenAI (klienta směřujte na `/openai/v1/` endpoint a volejte `client.responses.create`); používejte `@azure-rest/ai-inference` pro Microsoft Foundry Models
- Používejte `nodemon` pro vývoj s automatickým reloadem
- Kompilujte před spuštěním: `npm run build` a poté `npm start`

### Obecné konvence

- Držte příklady kódu jednoduché a vzdělávací
- Zahrňte komentáře vysvětlující klíčové koncepty
- Kód každé lekce by měl být samostatný a spustitelný
- Používejte konzistentní pojmenování: prefix `aoai-` pro Azure OpenAI, `oai-` pro OpenAI API, `githubmodels-` pro Microsoft Foundry Models (legacy prefix z doby GitHub Models)

## Směrnice pro dokumentaci

### Markdown styl

- Všechny URL musí být zapsány ve formátu `[text](../../url)` bez mezer navíc
- Relativní odkazy musí začínat `./` nebo `../`
- Všechny odkazy na Microsoft domény musí obsahovat tracking ID: `?WT.mc_id=academic-105485-koreyst`
- Nepoužívejte země-specifické locale v URL (vyhněte se `/en-us/`)
- Obrázky ukládejte do složky `./images` s popisnými názvy
- Používejte anglické znaky, čísla a pomlčky v názvech souborů

### Podpora překladu

- Úložiště podporuje 40+ jazyků pomocí automatizovaných GitHub Actions
- Překlady jsou uloženy ve složce `translations/`
- Neposílejte částečné překlady
- Strojové překlady nejsou akceptovány
- Přeložené obrázky uložené ve složce `translated_images/`

## Testování a ověřování

### Kontroly před odesláním

Toto úložiště používá GitHub Actions pro validaci. Před odesláním PR:

1. **Zkontrolujte Markdown odkazy**:
   ```bash
   # Workflow validate-markdown.yml kontroluje:
   # - Poškozené relativní cesty
   # - Chybějící identifikátory sledování na cestách
   # - Chybějící identifikátory sledování na URL
   # - URL s národním lokalizačním nastavením
   # - Poškozené externí URL
   ```

2. **Manuální testování**:
   - Testujte Python příklady: Aktivujte venv a spusťte skripty
   - Testujte TypeScript příklady: `npm install`, `npm run build`, `npm start`
   - Ověřte, že proměnné prostředí jsou správně nastaveny
   - Zkontrolujte, že API klíče fungují s příklady kódu

3. **Příklady kódu**:
   - Zajistěte, že vše běží bez chyb
   - Testujte s Azure OpenAI i OpenAI API, pokud je to relevantní
   - Ověřte, že příklady fungují s Microsoft Foundry Models tam, kde je podpora

### Bez automatizovaných testů

Toto je vzdělávací úložiště zaměřené na tutoriály a příklady. Nejsou zde žádné jednotkové ani integrační testy. Validace probíhá především:
- Manuálním testováním příkladů kódu
- GitHub Actions pro validaci Markdownu
- Revizí vzdělávacího obsahu komunitou

## Směrnice pro Pull Requesty

### Před odesláním

1. Otestujte změny v kódu v Pythonu i TypeScriptu, pokud je vhodné
2. Proveďte validaci Markdownu (automaticky při PR)
3. Ověřte, že všechny Microsoft URL obsahují tracking ID
4. Zkontrolujte správnost relativních odkazů
5. Ověřte, že obrázky jsou správně odkazované

### Formát názvu PR

- Používejte výstižné názvy: `[Lesson 06] Oprava překlepu v Python příkladu` nebo `Update README pro lekci 08`
- Pokud možno odkazujte na čísla issue: `Fixes #123`

### Popis PR

- Vysvětlete, co bylo změněno a proč
- Přidejte odkazy na související issue
- U kódových změn uveďte, které příklady byly testovány
- U příspěvků s překlady přiložte všechny soubory kompletního překladu

### Požadavky na přispívání

- Podepište Microsoft CLA (automaticky při prvním PR)
- Nejprve forkujte úložiště do svého účtu před změnami
- Jeden PR pro jednu logickou změnu (nesloučujte nesouvisející opravy)
- Držte PR co nejvíce zaměřené a malé

## Běžné pracovní postupy

### Přidání nového příkladu kódu

1. Přejděte do příslušné lekce
2. Vytvořte příklad ve složce `python/` nebo `typescript/`
3. Dodržujte pojmenovací konvenci: `{provider}-{název-příkladu}.{py|ts|js}`
4. Testujte s aktuálními API klíči
5. Zdokumentujte nové proměnné prostředí v README lekce

### Aktualizace dokumentace

1. Upravte README.md v adresáři lekce
2. Dodržujte Markdown guidelines (tracking ID, relativní odkazy)
3. Překlady aktualizuje GitHub Actions (neupravujte ručně)
4. Ověřte platnost všech odkazů

### Práce s Dev kontejnery

1. Úložiště obsahuje `.devcontainer/devcontainer.json`
2. Post-create skript automaticky instaluje Python závislosti
3. Rozšíření pro Python a Jupyter jsou přednastavené
4. Prostředí je založeno na `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Nasazení a publikování

Toto je učební úložiště - neexistuje žádný nasazovací proces. Kurz je dostupný přes:

1. **GitHub Repository**: Přímý přístup ke kódu a dokumentaci
2. **GitHub Codespaces**: Okamžité vývojové prostředí s přednastavením
3. **Microsoft Learn**: Obsah může být syndikován do oficiální platformy pro výuku
4. **docsify**: Dokumentační web generovaný z Markdownu (viz `docsifytopdf.js` a `package.json`)

### Vytvoření dokumentačního webu

```bash
# Vygenerovat PDF z dokumentace (pokud je potřeba)
npm run convert
```

## Řešení problémů

### Běžné problémy

**Python Import chyby**:
- Ujistěte se, že virtuální prostředí je aktivováno
- Spusťte `pip install -r requirements.txt`
- Zkontrolujte, že verze Pythonu je 3.9+

**Chyby kompilace TypeScriptu**:
- Spusťte `npm install` ve složce dané aplikace
- Ověřte kompatibilitu verze Node.js
- Vymažte `node_modules` a znovu nainstalujte, pokud je potřeba

**Chyby autentizace API**:
- Zkontrolujte, že `.env` soubor existuje a má správné hodnoty
- Zkontrolujte platnost a nevypršení API klíčů
- Ujistěte se, že endpoint URL je správný pro váš region

**Chybějící proměnné prostředí**:
- Zkopírujte `.env.copy` do `.env`
- Vyplňte všechny požadované hodnoty pro lekci, na které pracujete
- Restartujte aplikaci po aktualizaci `.env`

## Další zdroje

- [Průvodce nastavením kurzu](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Směrnice pro přispívání](./CONTRIBUTING.md)
- [Kodex chování](./CODE_OF_CONDUCT.md)
- [Bezpečnostní politika](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Sbírka pokročilých příkladů kódu](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Poznámky specifické pro projekt

- Toto je **vzdělávací úložiště** zaměřené na výuku, nikoliv produkční kód
- Příklady jsou záměrně jednoduché a zaměřené na výuku konceptů
- Kvalita kódu je vyvážená s jasností výuky
- Každá lekce je samostatná a může být dokončena nezávisle
- Úložiště podporuje více poskytovatelů API: Azure OpenAI, OpenAI, Microsoft Foundry Models a offline poskytovatele jako Foundry Local a Ollama
- Obsah je vícejazyčný s automatizovanými překladovými workflow
- Aktivní komunita na Discordu pro dotazy a podporu

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->