# AGENTS.md

## Prehľad projektu

Tento repozitár obsahuje komplexný kurz s 21 lekciami, ktorý učí základy Generatívnej AI a vývoj aplikácií. Kurz je určený pre začiatočníkov a pokrýva všetko od základných konceptov až po vytváranie aplikácií pripravených na produkciu.

**Kľúčové technológie:**
- Python 3.9+ s knižnicami: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript s Node.js a knižnicami: `openai` (Azure OpenAI cez v1 endpoint + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API a Microsoft Foundry Models (GitHub Models budú ukončené koncom júla 2026)
- Jupyter Notebooky pre interaktívne učenie
- Dev Containery pre konzistentné vývojové prostredie

**Štruktúra repozitára:**
- 21 adresárov s číslovanými lekciami (00-21) obsahujúcich README, príklady kódu a úlohy
- Viaceré implementácie: príklady v Pythone, TypeScript a niekedy .NET
- Adresár pre preklady s 40+ jazykovými verziami
- Centralizovaná konfigurácia cez súbor `.env` (použiť `.env.copy` ako šablónu)

## Príkazy na nastavenie

### Počiatočné nastavenie repozitára

```bash
# Klonujte repozitár
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Skopírujte šablónu prostredia
cp .env.copy .env
# Upravte súbor .env s vašimi API kľúčmi a koncovými bodmi
```

### Nastavenie Python prostredia

```bash
# Vytvorte virtuálne prostredie
python3 -m venv venv

# Aktivujte virtuálne prostredie
# Na macOS/Linux:
source venv/bin/activate
# Na Windows:
venv\Scripts\activate

# Nainštalujte závislosti
pip install -r requirements.txt
```

### Nastavenie Node.js/TypeScript

```bash
# Nainštalujte závislosti na úrovni root (pre dokumentačné nástroje)
npm install

# Pre jednotlivé príklady TypeScriptu z lekcií prejdite na konkrétnu lekciu:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Nastavenie Dev Containera (odporúčané)

Repozitár obsahuje konfiguráciu `.devcontainer` pre GitHub Codespaces alebo VS Code Dev Containery:

1. Otvorte repozitár v GitHub Codespaces alebo VS Code s rozšírením Dev Containers
2. Dev Container automaticky:
   - Nainštaluje Python závislosti zo súboru `requirements.txt`
   - Spustí skript post-create (`.devcontainer/post-create.sh`)
   - Nastaví Jupyter kernel

## Vývojový pracovný tok

### Premenné prostredia

Všetky lekcie vyžadujúce prístup k API používajú premenné prostredia definované v `.env`:

- `OPENAI_API_KEY` - Pre OpenAI API
- `AZURE_OPENAI_API_KEY` - Pre Azure OpenAI v Microsoft Foundry (Azure OpenAI Service je teraz súčasťou Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL endpoint Azure OpenAI (Foundry resource endpoint)
- `AZURE_OPENAI_DEPLOYMENT` - Názov nasadenia modelu chat completion
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Názov nasadenia modelu embeddings
- `AZURE_OPENAI_API_VERSION` - Verzia API (predvolené: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Pre Hugging Face modely
- `AZURE_INFERENCE_ENDPOINT` - Endpoint Microsoft Foundry Models (katalóg modelov od viacerých poskytovateľov)
- `AZURE_INFERENCE_CREDENTIAL` - API kľúč pre Microsoft Foundry Models (nahrádza končiaci sa `GITHUB_TOKEN`)

### Spustenie Python príkladov

```bash
# Prejdite do adresára lekcie
cd 06-text-generation-apps/python

# Spustite Python skript
python aoai-app.py
```

### Spustenie TypeScript príkladov

```bash
# Prejdite do adresára aplikácie TypeScript
cd 06-text-generation-apps/typescript/recipe-app

# Zostavte kód TypeScript
npm run build

# Spustite aplikáciu
npm start
```

### Spustenie Jupyter Notebookov

```bash
# Spustite Jupyter v koreňovom adresári repozitára
jupyter notebook

# Alebo použite VS Code s rozšírením Jupyter
```

### Práca s rôznymi typmi lekcií

- **Lekcie "Learn"**: Zamerané na dokumentáciu README.md a koncepty
- **Lekcie "Build"**: Obsahujú funkčné príklady kódu v Pythone a TypeScript
- Každá lekcia má README.md s teóriou, prehľadom kódu a odkazmi na video obsah

## Pravidlá štýlu kódu

### Python

- Používajte `python-dotenv` na správu premenných prostredia
- Importujte knižnicu `openai` pre interakcie s API
- Používajte `pylint` na lintovanie (niektoré príklady obsahujú `# pylint: disable=all` pre zjednodušenie)
- Dodržiavajte pomenovacie konvencie podľa PEP 8
- Ukladajte API prihlasovacie údaje do súboru `.env`, nikdy nie priamo do kódu

### TypeScript

- Používajte balík `dotenv` pre premenné prostredia
- Konfigurácia TypeScript v `tsconfig.json` pre každú aplikáciu
- Používajte balík `openai` pre Azure OpenAI (nastavte klienta na endpoint `/openai/v1/` a volajte `client.responses.create`); používajte `@azure-rest/ai-inference` pre Microsoft Foundry Models
- Používajte `nodemon` pre vývoj s automatickým znovunačítaním
- Pred spustením najprv zostavte: `npm run build` potom `npm start`

### Všeobecné konvencie

- Udržiavajte príklady kódu jednoduché a vzdelávacie
- Pridajte komentáre vysvetľujúce kľúčové koncepty
- Kód každej lekcie by mal byť samostatný a spustiteľný
- Používajte konzistentné pomenovanie: prefix `aoai-` pre Azure OpenAI, `oai-` pre OpenAI API, `githubmodels-` pre Microsoft Foundry Models (legacy prefix z éry GitHub Models je zachovaný)

## Pravidlá dokumentácie

### Štýl Markdown

- Všetky URL musia byť v tvare `[text](../../url)` bez pridaných medzier
- Relatívne odkazy musia začínať na `./` alebo `../`
- Všetky odkazy na Microsoft domény musia obsahovať sledovací ID: `?WT.mc_id=academic-105485-koreyst`
- V URL neuvádzajte lokálne špecifické krajiny (vyhnite sa `/en-us/`)
- Obrázky ukladajte v priečinku `./images` s popisnými názvami
- Používajte anglické znaky, čísla a pomlčky v názvoch súborov

### Podpora prekladov

- Repozitár podporuje 40+ jazykov cez automatizované GitHub Actions
- Preklady sa ukladajú v priečinku `translations/`
- Neposielajte čiastočné preklady
- Strojové preklady nie sú akceptované
- Preložené obrázky sú v priečinku `translated_images/`

## Testovanie a overovanie

### Kontroly pred odoslaním

Tento repozitár používa GitHub Actions na overovanie. Pred odoslaním PR:

1. **Skontrolujte Markdown odkazy**:
   ```bash
   # Pracovný tok validate-markdown.yml kontroluje:
   # - Poškodené relatívne cesty
   # - Chýbajúce identifikátory sledovania na cestách
   # - Chýbajúce identifikátory sledovania na URL adresách
   # - URL adresy s miestnou lokalizáciou krajiny
   # - Poškodené externé URL adresy
   ```

2. **Manuálne testovanie**:
   - Otestujte Python príklady: Aktivujte venv a spustite skripty
   - Otestujte TypeScript príklady: `npm install`, `npm run build`, `npm start`
   - Overte, že premenné prostredia sú správne nastavené
   - Skontrolujte, či API kľúče fungujú s príkladmi kódu

3. **Príklady kódu**:
   - Zabezpečte, aby celý kód bežal bez chýb
   - Testujte s Azure OpenAI aj OpenAI API, keď je to možné
   - Overte, že príklady fungujú s Microsoft Foundry Models, kde sú podporované

### Bez automatizovaných testov

Toto je vzdelávací repozitár zameraný na tutoriály a príklady. Žiadne jednotkové ani integračné testy sa nespúšťajú. Overovanie prebieha hlavne:
- Manuálnym testovaním príkladov kódu
- GitHub Actions na validáciu Markdown
- Komunitným hodnotením vzdelávacieho obsahu

## Pravidlá pre Pull Requesty

### Pred odoslaním

1. Otestujte zmeny v kóde v Pythone a TypeScripte, keď je to možné
2. Spustite validáciu Markdown (automaticky pri PR)
3. Overte, že sledovacie ID sú na všetkých Microsoft URL
4. Skontrolujte platnosť relatívnych odkazov
5. Overte správne odkazy na obrázky

### Formát názvu PR

- Používajte popisné názvy: `[Lesson 06] Oprav chybu v Python príklade` alebo `Aktualizácia README pre lekciu 08`
- Používajte čísla issues, keď je to vhodné: `Fixes #123`

### Popis PR

- Vysvetlite, čo sa zmenilo a prečo
- Odkážte na súvisiace issues
- Pri zmenách v kóde uveďte, ktoré príklady ste testovali
- Pri PR prekladoch zahrňte všetky súbory pre úplný preklad

### Požiadavky na príspevky

- Podpíšte Microsoft CLA (automaticky pri prvom PR)
- Vytvorte fork repozitára vo svojom účte pred zmenami
- Jeden PR na logickú zmenu (nespájajte nesúvisiace opravy)
- Snažte sa, aby PR boli zamerané a malé, keď je to možné

## Bežné pracovné toky

### Pridanie nového príkladu kódu

1. Prejdite do príslušného adresára lekcie
2. Vytvorte príklad v podpriečinku `python/` alebo `typescript/`
3. Dodržiavajte pomenovacie pravidlá: `{provider}-{example-name}.{py|ts|js}`
4. Testujte s aktuálnymi API povereniami
5. Dokumentujte nové premenné prostredia v README lekcie

### Aktualizácia dokumentácie

1. Upraviť README.md v adresári lekcie
2. Dodržiavať pravidlá Markdown (sledovacie ID, relatívne odkazy)
3. Preklady sú spravované GitHub Actions (neupravovať manuálne)
4. Otestovať platnosť všetkých odkazov

### Práca s Dev Containermi

1. Repozitár obsahuje `.devcontainer/devcontainer.json`
2. Skript post-create automaticky inštaluje Python závislosti
3. Rozšírenia pre Python a Jupyter sú predkonfigurované
4. Prostredie je založené na `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Nasadenie a publikovanie

Toto je učebný repozitár - neexistuje proces nasadenia. Kurz sa využíva cez:

1. **GitHub Repozitár**: Priamy prístup ku kódu a dokumentácii
2. **GitHub Codespaces**: Okamžité vývojové prostredie s prednastavením
3. **Microsoft Learn**: Obsah môže byť zverejňovaný na oficiálnej vzdelávacej platforme
4. **docsify**: Dokumentačný web generovaný z Markdown (pozri `docsifytopdf.js` a `package.json`)

### Tvorba dokumentačného webu

```bash
# Vygenerujte PDF z dokumentácie (ak je to potrebné)
npm run convert
```

## Riešenie problémov

### Bežné problémy

**Chyby importu Pythonu**:
- Overte, či je aktivované virtuálne prostredie
- Spustite `pip install -r requirements.txt`
- Skontrolujte, či verzia Pythonu je 3.9+

**Chyby kompilácie TypeScriptu**:
- Spustite `npm install` v príslušnom adresári aplikácie
- Skontrolujte kompatibilitu verzie Node.js
- Vymažte `node_modules` a znova nainštalujte, ak je to potrebné

**Chyby autentifikácie API**:
- Overte existenciu a správne hodnoty súboru `.env`
- Skontrolujte, či API kľúče sú platné a nevypršali
- Overte, či sú URL endpointy správne pre váš región

**Chýbajúce premenné prostredia**:
- Skopírujte `.env.copy` do `.env`
- Vyplňte všetky požadované hodnoty pre aktuálnu lekciu
- Po aktualizácii `.env` reštartujte aplikáciu

## Ďalšie zdroje

- [Sprievodca nastavením kurzu](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Pravidlá príspevkov](./CONTRIBUTING.md)
- [Kód správania](./CODE_OF_CONDUCT.md)
- [Bezpečnostná politika](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Zbierka pokročilých príkladov kódu](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Poznámky špecifické pre projekt

- Toto je **vzdelávací repozitár** zameraný na učenie, nie na produkčný kód
- Príklady sú úmyselne jednoduché a zamerané na výučbu konceptov
- Kvalita kódu je vyvážená s jasnosťou výučby
- Každá lekcia je samostatná a dá sa dokončiť nezávisle
- Repozitár podporuje viacerých poskytovateľov API: Azure OpenAI, OpenAI, Microsoft Foundry Models a offline poskytovateľov ako Foundry Local a Ollama
- Obsah je viacjazyčný s automatizovanými prekladovými pracovnými tokmi
- Aktívna komunita na Discorde pre otázky a podporu

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->