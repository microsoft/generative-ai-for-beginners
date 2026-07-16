# AGENTS.md

## Prehľad projektu

Tento repozitár obsahuje komplexný 21-dielny kurz učenia základov generatívnej AI a vývoja aplikácií. Kurz je navrhnutý pre začiatočníkov a pokrýva všetko od základných konceptov po budovanie produkčne pripravených aplikácií.

**Kľúčové technológie:**
- Python 3.9+ s knižnicami: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript s Node.js a knižnicami: `openai` (Azure OpenAI cez v1 endpoint + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API a Microsoft Foundry Models (GitHub Models končí na konci júla 2026)
- Jupyter Zápisníky pre interaktívne učenie
- Dev Containers pre konzistentné vývojové prostredie

**Štruktúra repozitára:**
- 21 číslovaných adresárov lekcií (00-21) obsahujúcich README, ukážky kódu a zadania
- Viacero implementácií: Python, TypeScript a občas .NET príklady
- Adresár s prekladmi s viac ako 40 jazykovými verziami
- Centralizovaná konfigurácia cez `.env` súbor (použite `.env.copy` ako šablónu)

## Príkazy na nastavenie

### Počiatočné nastavenie repozitára

```bash
# Naklonujte repozitár
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Skopírujte šablónu prostredia
cp .env.copy .env
# Upravte .env so svojimi API kľúčmi a koncovými bodmi
```

### Nastavenie Python prostredia

```bash
# Vytvoriť virtuálne prostredie
python3 -m venv venv

# Aktivovať virtuálne prostredie
# Na macOS/Linux:
source venv/bin/activate
# Na Windows:
venv\Scripts\activate

# Nainštalovať závislosti
pip install -r requirements.txt
```

### Nastavenie Node.js/TypeScript

```bash
# Nainštalujte závislosti na úrovni root (pre nástroje na dokumentáciu)
npm install

# Pre jednotlivé príklady TypeScript v lekciách prejdite na konkrétnu lekciu:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Nastavenie Dev Container (odporúčané)

Repozitár obsahuje `.devcontainer` konfiguráciu pre GitHub Codespaces alebo VS Code Dev Containers:

1. Otvorte repozitár v GitHub Codespaces alebo vo VS Code s rozšírením Dev Containers
2. Dev Container automaticky:
   - Nainštaluje Python závislosti z `requirements.txt`
   - Spustí post-create skript (`.devcontainer/post-create.sh`)
   - Nastaví Jupyter jadro

## Vývojový pracovný tok

### Premenné prostredia

Všetky lekcie vyžadujúce prístup k API používajú premenné prostredia definované v `.env`:

- `OPENAI_API_KEY` - Pre OpenAI API
- `AZURE_OPENAI_API_KEY` - Pre Azure OpenAI v Microsoft Foundry (Azure OpenAI Service je teraz súčasťou Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL Azure OpenAI endpointu (Foundry resource endpoint)
- `AZURE_OPENAI_DEPLOYMENT` - Názov nasadenia chat modelu (predvolené v kurze: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Názov nasadenia embeddings modelu (predvolené v kurze: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - Verzia API (predvolené: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Pre Hugging Face modely
- `AZURE_INFERENCE_ENDPOINT` - Endpoint Microsoft Foundry Models (katalóg modelov viacerých poskytovateľov)
- `AZURE_INFERENCE_CREDENTIAL` - API kľúč Microsoft Foundry Models (nahrádza ukončený `GITHUB_TOKEN`)
- `AZURE_INFERENCE_CHAT_MODEL` - Model bez schopnosti uvažovania (napr. `Llama-3.3-70B-Instruct`), používaný v príkladoch s `temperature`, pretože modely s uvažovaním nepodporujú ovládanie vzorkovania

### Konvencie modelov (dôležité)

- **Predvolený chat model je `gpt-5-mini`** - aktuálny, nepodpísaný **model s uvažovaním**. K roku 2026 staršie mini modely podporujúce reguláciu teploty (`gpt-4o-mini`, `gpt-4.1-mini`) sa *vyradzujú*, preto kurz používa jednotne rodinu GPT-5.
- **Modely s uvažovaním odmietajú `temperature` a `top_p`** a namiesto `max_tokens` používajú `max_output_tokens` (Responses API) / `max_completion_tokens` (chat completions). Nepridávajte `temperature`/`top_p`/`max_tokens` do príkladov volajúcich `gpt-5-mini`.
- **Na demonštráciu `temperature`** sa používajú vzorky s **Llama** modelom (`Llama-3.3-70B-Instruct`) cez Microsoft Foundry Models endpoint (`AZURE_INFERENCE_CHAT_MODEL`). Ovládajte modely s uvažovaním prompt engineeringom + ovládaním uvažovania namiesto vzorkovaním.
- **Doladenie (lekcia 18)** používa stále `gpt-4.1-mini`: GPT-5 podporuje len reinforcement fine-tuning (RFT), nie supervised fine-tuning (SFT), ktoré je uvedené tam.
- Lekcie 20 (Mistral) a 21 (Meta) stále používajú `temperature`/`max_tokens`, pretože sú určené pre Mistral/Llama modely, ktoré ich podporujú.

### Spúšťanie Python príkladov

```bash
# Prejdite do adresára lekcie
cd 06-text-generation-apps/python

# Spustite Python skript
python aoai-app.py
```

### Spúšťanie TypeScript príkladov

```bash
# Prejdite do adresára aplikácie TypeScript
cd 06-text-generation-apps/typescript/recipe-app

# Zostavte kód v TypeScripte
npm run build

# Spustite aplikáciu
npm start
```

### Spúšťanie Jupyter zápisníkov

```bash
# Spustite Jupyter v koreňovom adresári repozitára
jupyter notebook

# Alebo použite VS Code s rozšírením Jupyter
```

### Práca s rôznymi typmi lekcií

- **Lekcie "Learn"**: Zameranie na dokumentáciu README.md a koncepty
- **Lekcie "Build"**: Obsahujú funkčné ukážky kódu v Pythone a TypeScripte
- Každá lekcia má README.md s teóriou, prechádzaním kódu a odkazmi na video obsah

## Usmernenia pre štýl kódu

### Python

- Používajte `python-dotenv` na správu premenných prostredia
- Importujte knižnicu `openai` pre API interakcie
- Používajte `pylint` na lintovanie (niektoré príklady majú `# pylint: disable=all` pre jednoduchosť)
- Dodržujte pomenovanie podľa PEP 8
- Ukladajte API prístupové údaje do súboru `.env`, nikdy v kóde

### TypeScript

- Používajte balík `dotenv` na premenné prostredia
- Konfigurácia TypeScript v `tsconfig.json` pre každú aplikáciu
- Používajte balík `openai` pre Azure OpenAI (nasmerujte klienta na endpoint `/openai/v1/` a volajte `client.responses.create`); používajte `@azure-rest/ai-inference` pre Microsoft Foundry Models
- Používajte `nodemon` na vývoj s automatickým reloadom
- Pred spustením vykonajte build: `npm run build` potom `npm start`

### Všeobecné konvencie

- Udržujte príklady kódu jednoduché a edukačné
- Pridávajte komentáre vysvetľujúce kľúčové koncepty
- Kód v každej lekcii by mal byť samostatný a spustiteľný
- Používajte konzistentné pomenovanie: prefix `aoai-` pre Azure OpenAI, `oai-` pre OpenAI API, `githubmodels-` pre Microsoft Foundry Models (pôvodný prefix z éry GitHub Models je zachovaný)

## Usmernenia pre dokumentáciu

### Štýl Markdown

- Všetky URL musia byť zapuzdrené vo formáte `[text](../../url)` bez medzier navyše
- Relatívne odkazy musia začínať na `./` alebo `../`
- Všetky odkazy na domény Microsoft musia obsahovať sledovací ID: `?WT.mc_id=academic-105485-koreyst`
- Žiadne špecifické lokality podľa krajín v URL (vyhýbajte sa `/en-us/`)
- Obrázky ukladané v adresári `./images` s popisnými názvami
- Používajte anglické znaky, čísla a pomlčky v názvoch súborov

### Podpora prekladu

- Repozitár podporuje viac ako 40 jazykov cez automatizované GitHub Actions
- Preklady sú uložené v adresári `translations/`
- Neposielajte čiastočné preklady
- Strojové preklady nie sú akceptované
- Preložené obrázky sú uložené v adresári `translated_images/`

## Testovanie a validácia

### Kontroly pred odoslaním

Tento repozitár používa GitHub Actions na validáciu. Pred odoslaním PR:

1. **Skontrolujte Markdown odkazy**:
   ```bash
   # Pracovný tok validate-markdown.yml kontroluje:
   # - Neplatné relatívne cesty
   # - Chýbajúce identifikátory sledovania na cestách
   # - Chýbajúce identifikátory sledovania na URL adresách
   # - URL adresy s miestnou krajinou
   # - Neplatné externé URL adresy
   ```

2. **Manuálne testovanie**:
   - Otestujte Python príklady: aktivujte venv a spustite skripty
   - Otestujte TypeScript príklady: `npm install`, `npm run build`, `npm start`
   - Overte správnosť nastavenia premenných prostredia
   - Skontrolujte, či API kľúče fungujú s ukážkami kódu

3. **Príklady kódu**:
   - Zabezpečte, aby všetok kód bežal bez chýb
   - Testujte s Azure OpenAI aj OpenAI API, ak je to vhodné
   - Overte funkčnosť s Microsoft Foundry Models, kde je podporované

### Žiadne automatizované testy

Toto je vzdelávací repozitár zameraný na tutoriály a príklady. Nie sú tu jednotkové alebo integračné testy. Validácia je primárne:
- Manuálne testovanie príkladov kódu
- GitHub Actions pre Markdown validáciu
- Recenzia vzdelávacieho obsahu komunitou

## Pokyny pre Pull Requesty

### Pred odoslaním

1. Otestujte zmeny kódu v Pythone a TypeScripte, ak je to vhodné
2. Spustite Markdown validáciu (automaticky pri PR)
3. Skontrolujte prítomnosť sledovacích ID na všetkých Microsoft URL
4. Skontrolujte platnosť relatívnych odkazov
5. Overte správne odkazy na obrázky

### Formát názvu PR

- Používajte popisné názvy: `[Lekcia 06] Oprav chyba v príklade Python` alebo `Aktualizovať README pre lekciu 08`
- Odkazujte na čísla issues, ak je to vhodné: `Fixes #123`

### Popis PR

- Vysvetlite, čo bolo zmenené a prečo
- Priložte odkazy na súvisiace issues
- Pri zmenách kódu uveďte, ktoré príklady boli testované
- Pri prekladových PR zahrňte všetky súbory pre kompletný preklad

### Požiadavky na príspevky

- Podpíšte Microsoft CLA (automatické pri prvom PR)
- Vytvorte fork repozitára na svoj účet pred vykonaním zmien
- Jeden PR na logickú zmenu (nespájajte nesúvisiace opravy)
- Držte PR menšie a zamerané, pokiaľ je to možné

## Bežné pracovné toky

### Pridanie nového príkladu kódu

1. Prejdite do príslušného adresára lekcie
2. Vytvorte príklad v podadresári `python/` alebo `typescript/`
3. Dodržujte názvový vzor: `{provider}-{example-name}.{py|ts|js}`
4. Testujte so skutočnými API kľúčmi
5. Zdokumentujte nové premenné prostredia v README lekcie

### Aktualizácia dokumentácie

1. Upraviť README.md v adresári lekcie
2. Dodržiavať Markdown pravidlá (sledovacie ID, relatívne odkazy)
3. Aktualizáciu prekladov zabezpečujú GitHub Actions (neupravujte manuálne)
4. Otestovať platnosť všetkých odkazov

### Práca s Dev Containers

1. Repozitár obsahuje `.devcontainer/devcontainer.json`
2. Post-create skript automaticky inštaluje Python závislosti
3. Rozšírenia pre Python a Jupyter sú predkonfigurované
4. Prostredie je založené na `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Deploy a publikovanie

Toto je vzdelávací repozitár - neexistuje žiadny deploy proces. Kurz sa využíva:

1. **GitHub Repozitár**: Priamy prístup ku kódu a dokumentácii
2. **GitHub Codespaces**: Okamžité vývojové prostredie s prednastaveným setupom
3. **Microsoft Learn**: Obsah môže byť zdieľaný na oficiálnej vzdelávacej platforme
4. **docsify**: Dokumentačná stránka generovaná z Markdown (pozri `docsifytopdf.js` a `package.json`)

### Vytvorenie dokumentačnej stránky

```bash
# Generovať PDF z dokumentácie (ak je potrebné)
npm run convert
```

## Riešenie problémov

### Bežné problémy

**Chyby importu Pythonu**:
- Uistite sa, že je aktivované virtuálne prostredie
- Spustite `pip install -r requirements.txt`
- Skontrolujte, že verzia Pythonu je 3.9+

**Chyby pri buildovaní TypeScriptu**:
- Spustite `npm install` v konkrétnom adresári aplikácie
- Skontrolujte kompatibilitu verzie Node.js
- Vymažte `node_modules` a preinštalujte, ak je to potrebné

**Chyby autentifikácie API**:
- Overte existenciu `.env` súboru a správne hodnoty
- Skontrolujte platnosť a neexspiráciu API kľúčov
- Uistite sa, že URL endpointov sú správne pre váš región

**Chýbajúce premenné prostredia**:
- Skopírujte `.env.copy` do `.env`
- Vyplňte všetky potrebné hodnoty pre aktuálnu lekciu
- Po aktualizácii `.env` reštartujte aplikáciu

## Ďalšie zdroje

- [Sprievodca nastavením kurzu](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Pokyny na príspevky](./CONTRIBUTING.md)
- [Kód správania](./CODE_OF_CONDUCT.md)
- [Bezpečnostná politika](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Zbierka pokročilých ukážok kódu](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Poznámky k projektu

- Toto je **vzdelávací repozitár** zameraný na učenie, nie produkčný kód
- Príklady sú zámerne jednoduché a zamerané na výučbu konceptov
- Kvalita kódu je vyvážená s edukačnou zrozumiteľnosťou
- Každá lekcia je samostatná a môže byť dokončená nezávisle
- Repozitár podporuje viacerých poskytovateľov API: Azure OpenAI, OpenAI, Microsoft Foundry Models a offline poskytovateľov ako Foundry Local a Ollama
- Obsah je viacjazyčný s automatizovanými pracovnými tokmi prekladu
- Aktívna komunita na Discorde pre otázky a podporu

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->