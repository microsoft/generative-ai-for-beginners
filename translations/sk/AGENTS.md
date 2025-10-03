<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:10:41+00:00",
  "source_file": "AGENTS.md",
  "language_code": "sk"
}
-->
# AGENTS.md

## Prehľad projektu

Tento repozitár obsahuje komplexný 21-lekciový kurz, ktorý učí základy generatívnej AI a vývoj aplikácií. Kurz je určený pre začiatočníkov a pokrýva všetko od základných konceptov až po vytváranie aplikácií pripravených na produkciu.

**Kľúčové technológie:**
- Python 3.9+ s knižnicami: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript s Node.js a knižnicami: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API a GitHub Models
- Jupyter Notebooks pre interaktívne učenie
- Dev Containery pre konzistentné vývojové prostredie

**Štruktúra repozitára:**
- 21 očíslovaných adresárov lekcií (00-21) obsahujúcich README súbory, príklady kódu a úlohy
- Viacero implementácií: Python, TypeScript a občas .NET príklady
- Adresár preklady s viac ako 40 jazykovými verziami
- Centralizovaná konfigurácia cez súbor `.env` (použite `.env.copy` ako šablónu)

## Príkazy na nastavenie

### Počiatočné nastavenie repozitára

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Nastavenie Python prostredia

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

### Nastavenie Node.js/TypeScript

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Nastavenie Dev Containera (odporúčané)

Repozitár obsahuje konfiguráciu `.devcontainer` pre GitHub Codespaces alebo VS Code Dev Containery:

1. Otvorte repozitár v GitHub Codespaces alebo VS Code s rozšírením Dev Containers
2. Dev Container automaticky:
   - Nainštaluje Python závislosti zo súboru `requirements.txt`
   - Spustí post-create skript (`.devcontainer/post-create.sh`)
   - Nastaví Jupyter kernel

## Vývojový pracovný postup

### Premenné prostredia

Všetky lekcie vyžadujúce prístup k API používajú premenné prostredia definované v `.env`:

- `OPENAI_API_KEY` - Pre OpenAI API
- `AZURE_OPENAI_API_KEY` - Pre Azure OpenAI Service
- `AZURE_OPENAI_ENDPOINT` - URL endpointu Azure OpenAI
- `AZURE_OPENAI_DEPLOYMENT` - Názov nasadenia modelu na dokončenie chatu
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Názov nasadenia modelu na embeddings
- `AZURE_OPENAI_API_VERSION` - Verzia API (predvolené: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Pre modely Hugging Face
- `GITHUB_TOKEN` - Pre GitHub Models

### Spúšťanie Python príkladov

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### Spúšťanie TypeScript príkladov

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Spúšťanie Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Práca s rôznymi typmi lekcií

- **Lekcie "Learn"**: Zamerané na dokumentáciu README.md a koncepty
- **Lekcie "Build"**: Obsahujú funkčné príklady kódu v Pythone a TypeScripte
- Každá lekcia má README.md s teóriou, prehľadom kódu a odkazmi na video obsah

## Štandardy kódu

### Python

- Používajte `python-dotenv` na správu premenných prostredia
- Importujte knižnicu `openai` na interakciu s API
- Používajte `pylint` na lintovanie (niektoré príklady obsahujú `# pylint: disable=all` pre zjednodušenie)
- Dodržiavajte konvencie pomenovania PEP 8
- Uchovávajte prihlasovacie údaje API v súbore `.env`, nikdy nie v kóde

### TypeScript

- Používajte balík `dotenv` na premenné prostredia
- Konfigurácia TypeScript v `tsconfig.json` pre každú aplikáciu
- Používajte `@azure/openai` alebo `@azure-rest/ai-inference` pre služby Azure
- Používajte `nodemon` na vývoj s automatickým načítaním
- Pred spustením zostavte: `npm run build` a potom `npm start`

### Všeobecné konvencie

- Udržujte príklady kódu jednoduché a edukatívne
- Zahrňte komentáre vysvetľujúce kľúčové koncepty
- Kód každej lekcie by mal byť samostatný a spustiteľný
- Používajte konzistentné pomenovanie: predpona `aoai-` pre Azure OpenAI, `oai-` pre OpenAI API, `githubmodels-` pre GitHub Models

## Štandardy dokumentácie

### Štýl Markdown

- Všetky URL musia byť obalené vo formáte `[text](../../url)` bez dodatočných medzier
- Relatívne odkazy musia začínať `./` alebo `../`
- Všetky odkazy na domény Microsoft musia obsahovať sledovacie ID: `?WT.mc_id=academic-105485-koreyst`
- Žiadne krajiny špecifické lokality v URL (vyhnite sa `/en-us/`)
- Obrázky uložené v priečinku `./images` s popisnými názvami
- Používajte anglické znaky, čísla a pomlčky v názvoch súborov

### Podpora prekladov

- Repozitár podporuje viac ako 40 jazykov prostredníctvom automatizovaných GitHub Actions
- Preklady sú uložené v adresári `translations/`
- Neposielajte čiastočné preklady
- Strojové preklady nie sú akceptované
- Preložené obrázky sú uložené v adresári `translated_images/`

## Testovanie a validácia

### Kontroly pred odoslaním

Tento repozitár používa GitHub Actions na validáciu. Pred odoslaním PR:

1. **Kontrola odkazov v Markdown**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Manuálne testovanie**:
   - Testujte Python príklady: Aktivujte venv a spustite skripty
   - Testujte TypeScript príklady: `npm install`, `npm run build`, `npm start`
   - Overte, že premenné prostredia sú správne nakonfigurované
   - Skontrolujte, že API kľúče fungujú s príkladmi kódu

3. **Príklady kódu**:
   - Uistite sa, že všetok kód funguje bez chýb
   - Testujte s Azure OpenAI aj OpenAI API, ak je to možné
   - Overte, že príklady fungujú s GitHub Models, kde je to podporované

### Žiadne automatizované testy

Toto je edukatívny repozitár zameraný na tutoriály a príklady. Neexistujú žiadne jednotkové alebo integračné testy na spustenie. Validácia je primárne:
- Manuálne testovanie príkladov kódu
- GitHub Actions na validáciu Markdown
- Komunitná kontrola edukatívneho obsahu

## Pokyny pre Pull Requesty

### Pred odoslaním

1. Testujte zmeny kódu v Pythone aj TypeScripte, ak je to možné
2. Spustite validáciu Markdown (automaticky spustené pri PR)
3. Uistite sa, že sledovacie ID sú prítomné na všetkých Microsoft URL
4. Skontrolujte, že relatívne odkazy sú platné
5. Overte, že obrázky sú správne referencované

### Formát názvu PR

- Používajte popisné názvy: `[Lekcia 06] Oprava preklepu v Python príklade` alebo `Aktualizácia README pre lekciu 08`
- Odkazujte na čísla problémov, ak je to možné: `Fixes #123`

### Popis PR

- Vysvetlite, čo bolo zmenené a prečo
- Odkazujte na súvisiace problémy
- Pri zmenách kódu špecifikujte, ktoré príklady boli testované
- Pri prekladoch PR zahrňte všetky súbory pre kompletný preklad

### Požiadavky na príspevky

- Podpíšte Microsoft CLA (automaticky pri prvom PR)
- Forknite repozitár do svojho účtu pred vykonaním zmien
- Jeden PR na logickú zmenu (nekombinujte nesúvisiace opravy)
- Udržujte PR zamerané a malé, ak je to možné

## Bežné pracovné postupy

### Pridanie nového príkladu kódu

1. Prejdite do príslušného adresára lekcie
2. Vytvorte príklad v podadresári `python/` alebo `typescript/`
3. Dodržujte konvenciu pomenovania: `{provider}-{example-name}.{py|ts|js}`
4. Testujte s aktuálnymi API prihlasovacími údajmi
5. Dokumentujte všetky nové premenné prostredia v README lekcie

### Aktualizácia dokumentácie

1. Upravte README.md v adresári lekcie
2. Dodržujte pokyny pre Markdown (sledovacie ID, relatívne odkazy)
3. Aktualizácie prekladov sú spracované GitHub Actions (neupravujte manuálne)
4. Testujte, že všetky odkazy sú platné

### Práca s Dev Containermi

1. Repozitár obsahuje `.devcontainer/devcontainer.json`
2. Post-create skript automaticky nainštaluje Python závislosti
3. Rozšírenia pre Python a Jupyter sú predkonfigurované
4. Prostredie je založené na `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Nasadenie a publikovanie

Toto je vzdelávací repozitár - neexistuje proces nasadenia. Kurz je využívaný:

1. **GitHub Repozitár**: Priamy prístup ku kódu a dokumentácii
2. **GitHub Codespaces**: Okamžité vývojové prostredie s predkonfigurovaným nastavením
3. **Microsoft Learn**: Obsah môže byť syndikovaný na oficiálnu vzdelávaciu platformu
4. **docsify**: Dokumentačná stránka vytvorená z Markdown (pozrite `docsifytopdf.js` a `package.json`)

### Vytvorenie dokumentačnej stránky

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Riešenie problémov

### Bežné problémy

**Chyby pri importe Pythonu**:
- Uistite sa, že virtuálne prostredie je aktivované
- Spustite `pip install -r requirements.txt`
- Skontrolujte, že verzia Pythonu je 3.9+

**Chyby pri zostavovaní TypeScriptu**:
- Spustite `npm install` v konkrétnom adresári aplikácie
- Skontrolujte, že verzia Node.js je kompatibilná
- Vymažte `node_modules` a znovu nainštalujte, ak je to potrebné

**Chyby autentifikácie API**:
- Overte, že súbor `.env` existuje a má správne hodnoty
- Skontrolujte, že API kľúče sú platné a nevypršali
- Uistite sa, že URL endpointov sú správne pre váš región

**Chýbajúce premenné prostredia**:
- Skopírujte `.env.copy` do `.env`
- Vyplňte všetky požadované hodnoty pre lekciu, na ktorej pracujete
- Reštartujte aplikáciu po aktualizácii `.env`

## Ďalšie zdroje

- [Príručka nastavenia kurzu](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Pokyny pre prispievanie](./CONTRIBUTING.md)
- [Kódex správania](./CODE_OF_CONDUCT.md)
- [Bezpečnostná politika](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Zbierka pokročilých príkladov kódu](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Poznámky k projektu

- Toto je **vzdelávací repozitár** zameraný na učenie, nie produkčný kód
- Príklady sú zámerne jednoduché a zamerané na výučbu konceptov
- Kvalita kódu je vyvážená s edukatívnou jasnosťou
- Každá lekcia je samostatná a môže byť dokončená nezávisle
- Repozitár podporuje viacerých poskytovateľov API: Azure OpenAI, OpenAI a GitHub Models
- Obsah je viacjazyčný s automatizovanými pracovnými postupmi pre preklady
- Aktívna komunita na Discorde pre otázky a podporu

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.