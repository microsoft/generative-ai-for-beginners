<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:15:01+00:00",
  "source_file": "AGENTS.md",
  "language_code": "lt"
}
-->
# AGENTS.md

## Projekto apžvalga

Šiame saugykloje pateikiama išsami 21 pamokos mokymo programa, skirta Generatyvinio AI pagrindams ir taikymų kūrimui. Kursas sukurtas pradedantiesiems ir apima viską nuo pagrindinių sąvokų iki gamybai paruoštų taikymų kūrimo.

**Pagrindinės technologijos:**
- Python 3.9+ su bibliotekomis: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript su Node.js ir bibliotekomis: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API ir GitHub Models
- Jupyter Notebooks interaktyviam mokymuisi
- Dev Containers nuosekliai kūrimo aplinkai

**Saugyklos struktūra:**
- 21 numeruotas pamokų katalogas (00-21), kuriuose yra README failai, kodo pavyzdžiai ir užduotys
- Keli įgyvendinimai: Python, TypeScript ir kartais .NET pavyzdžiai
- Vertimų katalogas su daugiau nei 40 kalbų versijomis
- Centralizuota konfigūracija per `.env` failą (naudokite `.env.copy` kaip šabloną)

## Nustatymo komandos

### Pradinis saugyklos nustatymas

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Python aplinkos nustatymas

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

### Node.js/TypeScript nustatymas

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container nustatymas (rekomenduojama)

Saugykla apima `.devcontainer` konfigūraciją, skirtą GitHub Codespaces arba VS Code Dev Containers:

1. Atidarykite saugyklą GitHub Codespaces arba VS Code su Dev Containers plėtiniu
2. Dev Container automatiškai:
   - Įdiegs Python priklausomybes iš `requirements.txt`
   - Paleis post-create skriptą (`.devcontainer/post-create.sh`)
   - Nustatys Jupyter kernelį

## Kūrimo darbo eiga

### Aplinkos kintamieji

Visose pamokose, kuriose reikalinga API prieiga, naudojami aplinkos kintamieji, apibrėžti `.env` faile:

- `OPENAI_API_KEY` - OpenAI API
- `AZURE_OPENAI_API_KEY` - Azure OpenAI Service
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI paslaugos URL
- `AZURE_OPENAI_DEPLOYMENT` - Pokalbių modelio diegimo pavadinimas
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Embedding modelio diegimo pavadinimas
- `AZURE_OPENAI_API_VERSION` - API versija (numatytoji: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Hugging Face modeliams
- `GITHUB_TOKEN` - GitHub Models

### Python pavyzdžių paleidimas

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### TypeScript pavyzdžių paleidimas

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Jupyter Notebooks paleidimas

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Darbas su skirtingais pamokų tipais

- **"Learn" pamokos**: Dėmesys README.md dokumentacijai ir sąvokoms
- **"Build" pamokos**: Apima veikiančius kodo pavyzdžius Python ir TypeScript
- Kiekviena pamoka turi README.md su teorija, kodo apžvalga ir nuorodomis į vaizdo turinį

## Kodo stiliaus gairės

### Python

- Naudokite `python-dotenv` aplinkos kintamųjų valdymui
- Importuokite `openai` biblioteką API sąveikai
- Naudokite `pylint` kodo tikrinimui (kai kurie pavyzdžiai apima `# pylint: disable=all` dėl paprastumo)
- Laikykitės PEP 8 pavadinimų konvencijų
- API kredencialus saugokite `.env` faile, niekada kode

### TypeScript

- Naudokite `dotenv` paketą aplinkos kintamiesiems
- TypeScript konfigūracija `tsconfig.json` kiekvienai programai
- Naudokite `@azure/openai` arba `@azure-rest/ai-inference` Azure paslaugoms
- Naudokite `nodemon` kūrimui su automatinio perkrovimo funkcija
- Prieš paleidžiant: `npm run build`, tada `npm start`

### Bendros konvencijos

- Kodo pavyzdžiai turi būti paprasti ir edukaciniai
- Įtraukite komentarus, paaiškinančius pagrindines sąvokas
- Kiekvienos pamokos kodas turi būti savarankiškas ir paleidžiamas
- Naudokite nuoseklius pavadinimus: `aoai-` Azure OpenAI, `oai-` OpenAI API, `githubmodels-` GitHub Models

## Dokumentacijos gairės

### Markdown stilius

- Visos URL turi būti apgaubtos `[tekstą](../../url)` formatu be papildomų tarpų
- Santykinės nuorodos turi prasidėti `./` arba `../`
- Visos nuorodos į Microsoft domenus turi turėti sekimo ID: `?WT.mc_id=academic-105485-koreyst`
- Nenaudokite šalių specifinių lokalizacijų URL (vengti `/en-us/`)
- Vaizdai saugomi `./images` kataloge su aprašomaisiais pavadinimais
- Failų pavadinimuose naudokite anglų simbolius, skaičius ir brūkšnelius

### Vertimo palaikymas

- Saugykla palaiko daugiau nei 40 kalbų per automatizuotus GitHub Actions
- Vertimai saugomi `translations/` kataloge
- Nepateikite dalinių vertimų
- Mašininiai vertimai nepriimami
- Išversti vaizdai saugomi `translated_images/` kataloge

## Testavimas ir validacija

### Prieš pateikimą

Ši saugykla naudoja GitHub Actions validacijai. Prieš pateikiant PR:

1. **Patikrinkite Markdown nuorodas**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Rankinis testavimas**:
   - Testuokite Python pavyzdžius: aktyvuokite venv ir paleiskite skriptus
   - Testuokite TypeScript pavyzdžius: `npm install`, `npm run build`, `npm start`
   - Patikrinkite, ar aplinkos kintamieji tinkamai sukonfigūruoti
   - Įsitikinkite, kad API raktai veikia su kodo pavyzdžiais

3. **Kodo pavyzdžiai**:
   - Įsitikinkite, kad visas kodas veikia be klaidų
   - Testuokite su Azure OpenAI ir OpenAI API, kai taikoma
   - Patikrinkite, ar pavyzdžiai veikia su GitHub Models, kur tai palaikoma

### Nėra automatizuotų testų

Tai edukacinė saugykla, orientuota į pamokas ir pavyzdžius. Nėra vienetinių ar integracinių testų. Validacija daugiausia:
- Rankinis kodo pavyzdžių testavimas
- GitHub Actions Markdown validacijai
- Bendruomenės peržiūra edukacinio turinio

## Pull Request gairės

### Prieš pateikimą

1. Testuokite kodo pakeitimus tiek Python, tiek TypeScript, kai taikoma
2. Paleiskite Markdown validaciją (automatiškai paleidžiama PR metu)
3. Įsitikinkite, kad sekimo ID yra visose Microsoft URL
4. Patikrinkite, ar santykinės nuorodos galioja
5. Patikrinkite, ar vaizdai tinkamai nurodyti

### PR pavadinimo formatas

- Naudokite aprašomuosius pavadinimus: `[Pamoka 06] Taisymas Python pavyzdžio klaidos` arba `Atnaujinti README pamokai 08`
- Nurodykite problemų numerius, kai taikoma: `Taiso #123`

### PR aprašymas

- Paaiškinkite, kas buvo pakeista ir kodėl
- Nuorodos į susijusias problemas
- Kodo pakeitimams nurodykite, kurie pavyzdžiai buvo testuoti
- Vertimo PR atveju įtraukite visus failus, kad vertimas būtų pilnas

### Reikalavimai prisidėjimui

- Pasirašykite Microsoft CLA (automatiškai pirmame PR)
- Prieš atlikdami pakeitimus, fork'inkite saugyklą į savo paskyrą
- Vienas PR per logišką pakeitimą (nesujunkite nesusijusių taisymų)
- PR turi būti koncentruoti ir maži, kai įmanoma

## Dažnos darbo eigos

### Naujo kodo pavyzdžio pridėjimas

1. Eikite į atitinkamą pamokos katalogą
2. Sukurkite pavyzdį `python/` arba `typescript/` subkataloge
3. Laikykitės pavadinimų konvencijos: `{provider}-{example-name}.{py|ts|js}`
4. Testuokite su tikrais API kredencialais
5. Dokumentuokite naujus aplinkos kintamuosius pamokos README

### Dokumentacijos atnaujinimas

1. Redaguokite README.md pamokos kataloge
2. Laikykitės Markdown gairių (sekimo ID, santykinės nuorodos)
3. Vertimų atnaujinimus tvarko GitHub Actions (neredaguokite rankiniu būdu)
4. Testuokite, ar visos nuorodos galioja

### Darbas su Dev Containers

1. Saugykla apima `.devcontainer/devcontainer.json`
2. Post-create skriptas automatiškai įdiegia Python priklausomybes
3. Python ir Jupyter plėtiniai yra iš anksto sukonfigūruoti
4. Aplinka pagrįsta `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Diegimas ir publikavimas

Tai mokymosi saugykla - nėra diegimo proceso. Mokymo programa naudojama:

1. **GitHub saugykla**: Tiesioginė prieiga prie kodo ir dokumentacijos
2. **GitHub Codespaces**: Momentinė kūrimo aplinka su iš anksto sukonfigūruotu nustatymu
3. **Microsoft Learn**: Turinys gali būti platinamas oficialioje mokymosi platformoje
4. **docsify**: Dokumentacijos svetainė, sukurta iš Markdown (žr. `docsifytopdf.js` ir `package.json`)

### Dokumentacijos svetainės kūrimas

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Trikčių šalinimas

### Dažnos problemos

**Python importavimo klaidos**:
- Įsitikinkite, kad virtuali aplinka aktyvuota
- Paleiskite `pip install -r requirements.txt`
- Patikrinkite, ar Python versija yra 3.9+

**TypeScript kūrimo klaidos**:
- Paleiskite `npm install` konkretaus programos kataloge
- Patikrinkite, ar Node.js versija suderinama
- Išvalykite `node_modules` ir iš naujo įdiekite, jei reikia

**API autentifikavimo klaidos**:
- Patikrinkite, ar `.env` failas egzistuoja ir turi teisingas reikšmes
- Patikrinkite, ar API raktai galioja ir nėra pasibaigę
- Įsitikinkite, kad URL yra teisingi jūsų regionui

**Trūksta aplinkos kintamųjų**:
- Nukopijuokite `.env.copy` į `.env`
- Užpildykite visas reikalingas reikšmes pamokai, su kuria dirbate
- Perkraukite savo programą po `.env` atnaujinimo

## Papildomi ištekliai

- [Kurso nustatymo vadovas](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Prisidėjimo gairės](./CONTRIBUTING.md)
- [Elgesio kodeksas](./CODE_OF_CONDUCT.md)
- [Saugumo politika](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Išplėstinių kodo pavyzdžių kolekcija](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projekto specifinės pastabos

- Tai yra **edukacinė saugykla**, orientuota į mokymąsi, o ne gamybos kodą
- Pavyzdžiai yra tyčia paprasti ir orientuoti į sąvokų mokymą
- Kodo kokybė subalansuota su edukaciniu aiškumu
- Kiekviena pamoka yra savarankiška ir gali būti baigta nepriklausomai
- Saugykla palaiko kelis API tiekėjus: Azure OpenAI, OpenAI ir GitHub Models
- Turinys yra daugiakalbis su automatizuotais vertimo darbo srautais
- Aktyvi bendruomenė Discord platformoje klausimams ir pagalbai

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.