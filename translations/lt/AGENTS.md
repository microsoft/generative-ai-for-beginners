# AGENTAI.md

## Projekto apžvalga

Šiame saugykloje yra išsamus 21 pamokos kursas, mokantis Generatyvinio DI pagrindų ir taikomųjų programų kūrimo. Kursas skirtas pradedantiesiems ir apima viską nuo pagrindinių koncepcijų iki gamybai paruoštų programų kūrimo.

**Pagrindinės technologijos:**
- Python 3.9+ su bibliotekomis: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript su Node.js ir bibliotekomis: `openai` (Azure OpenAI per v1 pabaigos tašką + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Modeliai)
- Azure OpenAI paslauga, OpenAI API ir Microsoft Foundry Modeliai (GitHub Modeliai nutraukiami 2026 m. liepos pabaigoje)
- Jupyter užrašų knygelės interaktyviam mokymuisi
- Dev Containers nuosekliai kūrimo aplinkai

**Saugomos struktūra:**
- 21 sunumeruotų pamokų katalogai (00–21), kuriuose yra README failai, kodo pavyzdžiai ir užduotys
- Keli įgyvendinimai: Python, TypeScript, o kartais ir .NET pavyzdžiai
- Vertimų katalogas su daugiau nei 40 kalbų versijų
- Centralizuota konfigūracija per `.env` failą (naudokite `.env.copy` kaip šabloną)

## Konfigūracijos komandos

### Pradinis saugyklos paruošimas

```bash
# Nuklonuokite saugyklą
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Nukopijuokite aplinkos šabloną
cp .env.copy .env
# Redaguokite .env su savo API raktų ir endpoint'ų informacija
```

### Python aplinkos paruošimas

```bash
# Sukurti virtualią aplinką
python3 -m venv venv

# Aktyvuoti virtualią aplinką
# macOS/Linux sistemoje:
source venv/bin/activate
# Windows sistemoje:
venv\Scripts\activate

# Įdiegti priklausomybes
pip install -r requirements.txt
```

### Node.js/TypeScript paruošimas

```bash
# Įdiekite pagrindines priklausomybes (dokumentacijos įrankiams)
npm install

# Norėdami peržiūrėti atskirų pamokų TypeScript pavyzdžius, eikite į konkrečią pamoką:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev konteinerio paruošimas (rekomenduojama)

Saugykloje įtraukta `.devcontainer` konfigūracija GitHub Codespaces arba VS Code Dev Containers naudojimui:

1. Atidarykite saugyklą GitHub Codespaces arba VS Code su Dev Containers plėtiniu
2. Dev konteineris automatiškai:
   - Įdiegia Python priklausomybes iš `requirements.txt`
   - Paleidžia po sukūrimo scenarijų (`.devcontainer/post-create.sh`)
   - Paruošia Jupyter branduolį

## Vystymo procesas

### Aplinkos kintamieji

Visos pamokos, kurioms reikalingas API prieigos raktas, naudoja `.env` faile apibrėžtus aplinkos kintamuosius:

- `OPENAI_API_KEY` - OpenAI API raktas
- `AZURE_OPENAI_API_KEY` - Azure OpenAI Microsoft Foundry paslaugai (Azure OpenAI Service dabar yra Microsoft Foundry dalis: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI pabaigos taško URL (Foundry paslaugos pabaigos taškas)
- `AZURE_OPENAI_DEPLOYMENT` - Pokalbių modelio diegimo pavadinimas
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Embedding modelio diegimo pavadinimas
- `AZURE_OPENAI_API_VERSION` - API versija (numatytoji: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Hugging Face modelių API raktas
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Modelių pabaigos taškas (daugelio tiekėjų modelių katalogas)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Modelių API raktas (pakeičia nutraukiamą `GITHUB_TOKEN`)

### Python pavyzdžių paleidimas

```bash
# Eiti į pamokos katalogą
cd 06-text-generation-apps/python

# Vykdyti Python skriptą
python aoai-app.py
```

### TypeScript pavyzdžių paleidimas

```bash
# Eikite į TypeScript programos katalogą
cd 06-text-generation-apps/typescript/recipe-app

# Sukurkite TypeScript kodą
npm run build

# Paleiskite programą
npm start
```

### Jupyter užrašų knygelių paleidimas

```bash
# Paleiskite Jupyter saugyklos šaknyje
jupyter notebook

# Arba naudokite VS Code su Jupyter plėtiniu
```

### Darbas su skirtingomis pamokų rūšimis

- **„Learn“ pamokos**: dėmesys README.md dokumentacijai ir koncepcijoms
- **„Build“ pamokos**: įtraukti veikiantys kodo pavyzdžiai Python ir TypeScript kalbomis
- Kiekvienoje pamokoje yra README.md su teorija, kodo apžvalgomis ir nuorodomis į vaizdo įrašus

## Kodo stiliaus gairės

### Python

- Naudokite `python-dotenv` aplinkos kintamiesiems valdyti
- Importuokite `openai` biblioteką API sąveikai
- Naudokite `pylint` kodui tikrinti (kai kurie pavyzdžiai naudoja `# pylint: disable=all` paprastumui)
- Laikykitės PEP 8 vardų konvencijų
- API duomenys saugomi `.env` faile, niekada nečiuo Kodas

### TypeScript

- Naudokite `dotenv` paketą aplinkos kintamiesiems
- TypeScript konfiguracija faile `tsconfig.json` kiekvienai programai
- Naudokite `openai` paketą Azure OpenAI (kreipkitės į `/openai/v1/` pabaigos tašką ir iškvieskite `client.responses.create`); naudokite `@azure-rest/ai-inference` Microsoft Foundry Modeliams
- Naudokite `nodemon` vystymui su automatinio perkrovimo funkcija
- Statykite prieš paleidžiant: `npm run build` tada `npm start`

### Bendros konvencijos

- Laikykite kodo pavyzdžius paprastus ir mokomuosius
- Įtraukite komentarus, paaiškinančius svarbias koncepcijas
- Kiekvienos pamokos kodas turi būti savarankiškas ir paleidžiamas
- Naudokite nuoseklius vardus: `aoai-` prefiksas Azure OpenAI, `oai-` prefiksas OpenAI API, `githubmodels-` Microsoft Foundry Modeliams (paliktas senasis prefiksas iš GitHub Modelių eros)

## Dokumentacijos gairės

### Markdown stilius

- Visos URL turi būti įvyniotos į formą `[text](../../url)` be papildomų tarpų
- Santykinės nuorodos turi prasidėti nuo `./` arba `../`
- Visos nuorodos į Microsoft domenus turi turėti sekimo ID: `?WT.mc_id=academic-105485-koreyst`
- Nedėkite apskrities tikslių lokalizacijų URL (venkite `/en-us/`)
- Vaizdai saugomi `./images` aplanke su aprašomais pavadinimais
- Failų pavadinimuose naudokite anglų raides, skaičius ir brūkšnelius

### Vertimų palaikymas

- Saugykla palaiko daugiau nei 40 kalbų per automatinį GitHub Actions
- Vertimai saugomi `translations/` kataloge
- Neskelbkite dalinių vertimų
- Mašininių vertimų nepriimame
- Išverstų vaizdų saugojimas `translated_images/` kataloge

## Testavimas ir patvirtinimas

### Prieš pateikiant tikrinimus

Ši saugykla naudoja GitHub Actions patikrinimams. Prieš pateikiant PR:

1. **Patikrinkite Markdown nuorodas**:
   ```bash
   # validate-markdown.yml darbo eiga tikrina:
   # - Sugadintas santykinis kelias
   # - Trūkstami sekimo identifikatoriai keliuose
   # - Trūkstami sekimo identifikatoriai URL adresuose
   # - URL su šalies lokalizacija
   # - Sugadinti išoriniai URL adresaiv
   ```

2. **Rankinis testavimas**:
   - Išbandykite Python pavyzdžius: suaktyvinkite venv ir paleiskite skriptus
   - Išbandykite TypeScript pavyzdžius: `npm install`, `npm run build`, `npm start`
   - Patikrinkite, ar yra tinkamai sukonfigūruoti aplinkos kintamieji
   - Įsitikinkite, kad API raktai veikia su kodo pavyzdžiais

3. **Kodo pavyzdžiai**:
   - Įsitikinkite, kad visas kodas veikia be klaidų
   - Išbandykite tiek su Azure OpenAI, tiek su OpenAI API, kai taikoma
   - Patikrinkite pavyzdžius su Microsoft Foundry Modeliais, kur palaikoma

### Nėra automatinių testų

Tai edukacinė saugykla, orientuota į pamokas ir pavyzdžius. Nėra vienetinių ar integracinių testų. Patvirtinimas daugiausia:
- Rankinis kodo pavyzdžių testavimas
- GitHub Actions – Markdown validacija
- Bendruomenės atsiliepimai apie mokomąją medžiagą

## „Pull Request“ gairės

### Prieš pateikiant

1. Išbandykite kodo pakeitimus Python ir TypeScript kalbomis, kai taikoma
2. Paleiskite Markdown validaciją (automatiškai, pateikus PR)
3. Įsitikinkite, kad visose Microsoft URL yra sekimo ID
4. Patikrinkite, ar santykinės nuorodos yra galiojančios
5. Patikrinkite, ar vaizdai tinkamai nurodyti

### PR pavadinimo formatas

- Naudokite apibūdinančius pavadinimus: `[Lesson 06] Sutvarkytas Python pavyzdžio rašybos klaida` arba `Atnaujintas README 08 pamokai`
- Nurodykite numerį susijusių problemų atveju: `Fixes #123`

### PR aprašymas

- Paaiškinkite, kas buvo pakeista ir kodėl
- Nuoroda į susijusias problemas
- Pakeitimams kode nurodykite, kurie pavyzdžiai buvo išbandyti
- Vertimo PR atveju pateikite visus failus už pilną vertimą

### Indėlio reikalavimai

- Pasirašykite Microsoft CLA (automatiškai pirmam PR)
- Šakinkite saugyklą į savo paskyrą prieš darydami pakeitimus
- Vienas PR vienam logiškam pakeitimui (nesujunkite nesusijusių pataisų)
- PR stenkitės daryti tiksliais ir mažais

## Dažniausi darbo srautai

### Naujo kodo pavyzdžio pridėjimas

1. Eikite į atitinkamo pamokos katalogą
2. Sukurkite pavyzdį `python/` arba `typescript/` posistemyje
3. Laikykitės vardų konvencijos: `{provider}-{example-name}.{py|ts|js}`
4. Išbandykite su tikrais API raktais
5. Užregistruokite naujus aplinkos kintamuosius pamokos README faile

### Dokumentacijos atnaujinimas

1. Redaguokite README.md pamokos kataloge
2. Laikykitės Markdown gairių (sekimo ID, santykinės nuorodos)
3. Vertimų atnaujinimai tvarkomi GitHub Actions (nerašykite ranka)
4. Patikrinkite, ar visos nuorodos galioja

### Darbas su Dev konteineriais

1. Saugykloje yra `.devcontainer/devcontainer.json`
2. Po sukūrimo scenarijus automatiškai įdiegia Python priklausomybes
3. Iš anksto sukonfigūruoti Python ir Jupyter plėtiniai
4. Aplinka pagrįsta `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Diegimas ir paskelbimas

Tai mokymosi saugykla – nėra diegimo proceso. Kursas yra pasiekiamas per:

1. **GitHub saugykla**: tiesioginis prieigos kodas ir dokumentacija
2. **GitHub Codespaces**: momentinė kūrimo aplinka su iš anksto sukonfigūruota aplinka
3. **Microsoft Learn**: turinys gali būti paskelbtas oficialioje mokymosi platformoje
4. **docsify**: dokumentacijos svetainė kuriama iš Markdown (žiūrėkite `docsifytopdf.js` ir `package.json`)

### Dokumentacijos svetainės kūrimas

```bash
# Sugeneruoti PDF iš dokumentacijos (jei reikalinga)
npm run convert
```

## Problemų šalinimas

### Dažnos problemos

**Python importavimo klaidos**:
- Įsitikinkite, kad virtuali aplinka suaktyvinta
- Paleiskite `pip install -r requirements.txt`
- Patikrinkite, ar Python versija yra 3.9 ar naujesnė

**TypeScript kompiliavimo klaidos**:
- Paleiskite `npm install` toje pačioje programos direktorijoje
- Patikrinkite Node.js suderinamumą
- Išvalykite `node_modules` ir perinstaliuokite, jei reikia

**API autentifikavimo klaidos**:
- Patikrinkite, ar egzistuoja `.env` failas su teisingomis reikšmėmis
- Patikrinkite, ar API raktai galioja ir nėra pasibaigę
- Įsitikinkite, kad pabaigos taško URL yra teisingas jūsų regionui

**Trūksta aplinkos kintamųjų**:
- Nukopijuokite `.env.copy` į `.env`
- Užpildykite visus reikalingus laukus pagal pamoką, kurioje dirbate
- Po atnaujinimo perkraukite programą

## Papildomi ištekliai

- [Kurso paruošimo vadovas](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Indėlio gairės](./CONTRIBUTING.md)
- [Elgesio kodeksas](./CODE_OF_CONDUCT.md)
- [Saugumo politika](./SECURITY.md)
- [Azure DI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Pažangių kodo pavyzdžių rinkinys](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projekto specifinės pastabos

- Tai **edukacinė saugykla** skirta mokymuisi, o ne gamybos kodui
- Pavyzdžiai sąmoningai paprasti ir orientuoti į koncepcijų mokymąsi
- Kodo kokybė derinama su edukaciniu aiškumu
- Kiekviena pamoka yra savarankiška ir gali būti užbaigta nepriklausomai
- Saugykla palaiko kelis API tiekėjus: Azure OpenAI, OpenAI, Microsoft Foundry Modelius ir neprisijungimo tiekėjus kaip Foundry Local ir Ollama
- Turinys daugiakalbis su automatizuotais vertimo procesais
- Aktyvi bendruomenė „Discord“ klausimams ir palaikymui

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->