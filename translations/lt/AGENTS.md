# AGENTS.md

## Projekto apžvalga

Šiame talpykloje pateikiama išsami 21 pamokos programa, mokanti Generatyvinio DI pagrindų ir taikomųjų programų kūrimo. Kursas skirtas pradedantiesiems ir apima viską nuo pagrindinių sąvokų iki gamybai paruoštų programų kūrimo.

**Pagrindinės technologijos:**
- Python 3.9+ su bibliotekomis: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript su Node.js ir bibliotekomis: `openai` (Azure OpenAI per v1 galinį tašką + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry modeliai)
- Azure OpenAI Service, OpenAI API ir Microsoft Foundry modeliai (GitHub modeliai bus nutraukti iki 2026 m. liepos pabaigos)
- Jupyter užrašų knygutės interaktyviam mokymuisi
- Dev konteineriai nuoseklei kūrimo aplinkai

**Talpyklos struktūra:**
- 21 numeruotų pamokų katalogai (00-21) su README failais, kodo pavyzdžiais ir užduotimis
- Keli įgyvendinimo variantai: Python, TypeScript ir kartais .NET pavyzdžiai
- Vertimų katalogas su 40+ kalbų versijomis
- Centrinė konfigūracija per `.env` failą (naudokite `.env.copy` kaip šabloną)

## Nustatymo komandos

### Pradinis talpyklos nustatymas

```bash
# Klonuokite saugyklą
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Nukopijuokite aplinkos šabloną
cp .env.copy .env
# Redaguokite .env su savo API raktas ir galiniais taškais
```

### Python aplinkos nustatymas

```bash
# Sukurkite virtualią aplinką
python3 -m venv venv

# Aktyvuokite virtualią aplinką
# macOS/Linux operacinėse sistemose:
source venv/bin/activate
# Windows operacinėje sistemoje:
venv\Scripts\activate

# Įdiekite priklausomybes
pip install -r requirements.txt
```

### Node.js/TypeScript nustatymas

```bash
# Įdiekite pagrindinius priklausomybes (dokumentacijos įrankiams)
npm install

# Norėdami peržiūrėti atskirus pamokos TypeScript pavyzdžius, eikite į konkrečią pamoką:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev konteinerio nustatymas (rekomenduojama)

Talpykloje yra `.devcontainer` konfigūracija GitHub Codespaces arba VS Code Dev konteineriams:

1. Atidarykite talpyklą GitHub Codespaces arba VS Code su Dev Containers plėtiniu
2. Dev konteineris automatiškai:
   - Įdiegia Python priklausomybes iš `requirements.txt`
   - Vykdo po sukūrimo skriptą (`.devcontainer/post-create.sh`)
   - Nustato Jupyter branduolį

## Kūrimo darbo eiga

### Aplinkos kintamieji

Visos pamokos, kurioms reikalingas API prieiga, naudoja aplinkos kintamuosius, apibrėžtus `.env` faile:

- `OPENAI_API_KEY` - OpenAI API raktas
- `AZURE_OPENAI_API_KEY` - Azure OpenAI Microsoft Foundry (Azure OpenAI Service dabar yra Microsoft Foundry dalis: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI galinio taško URL (Foundry išteklių taškas)
- `AZURE_OPENAI_DEPLOYMENT` - Pokalbių užbaigimo modelio diegimo pavadinimas (kurso numatytasis: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Įkėlimo modelio diegimo pavadinimas (kurso numatytasis: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - API versija (numatytoji: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Hugging Face modeliams
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry modelių galinio taško adresas (daugiaprieglobiniai modelių katalogai)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry modelių API raktas (pakeičia nutraukiamą `GITHUB_TOKEN`)
- `AZURE_INFERENCE_CHAT_MODEL` - Ne loginis modelis (pvz., `Llama-3.3-70B-Instruct`), naudojamas pavyzdžiuose su `temperature`, nes loginiai modeliai nepalaiko mėginimų kontrolės

### Modelių konvencijos (svarbu)

- **Numatytasis pokalbių modelis yra `gpt-5-mini`** - dabartinis, nepasenęs **loginis** modelis. Nuo 2026 m. senesni, su temperatūros reguliavimu „mini“ modeliai (`gpt-4o-mini`, `gpt-4.1-mini`) yra *nutraukiami*, todėl mokymo programa standartizuoja GPT-5 šeimą.
- **Loginiai modeliai nepriima `temperature` ir `top_p` parametrų** ir vietoj `max_tokens` naudoja `max_output_tokens` (Responses API) / `max_completion_tokens` (pokalbių užbaigimuose). Nedėkite `temperature`/`top_p`/`max_tokens` pavyzdžiuose, kurie kviečia `gpt-5-mini`.
- **Norint pademonstruoti `temperature`**, pavyzdžiai naudoja **Llama** modelį (`Llama-3.3-70B-Instruct`) per Microsoft Foundry modelių galinį tašką (`AZURE_INFERENCE_CHAT_MODEL`). Loginius modelius valdykite naudodami užklausų konstravimą ir loginę kontrolę, o ne mėginimų reguliavimo rankenėles.
- **Tikslinimas (pamoka 18)** naudoja `gpt-4.1-mini`: GPT-5 palaiko tik pastiprinamojo mokymo (RFT), ne prižiūrimą mokymą (SFT), kaip parodyta ten.
- Pamokos 20 (Mistral) ir 21 (Meta) naudoja `temperature`/`max_tokens`, nes jos taikomos Mistral/Llama modeliams, kurie juos palaiko.

### Python pavyzdžių vykdymas

```bash
# Eiti į pamokos katalogą
cd 06-text-generation-apps/python

# Vykdyti Python skriptą
python aoai-app.py
```

### TypeScript pavyzdžių vykdymas

```bash
# Eikite į TypeScript programos katalogą
cd 06-text-generation-apps/typescript/recipe-app

# Sukonstruokite TypeScript kodą
npm run build

# Paleiskite programą
npm start
```

### Jupyter užrašų knygų vykdymas

```bash
# Paleiskite Jupyter šakninėje saugyklos direktorijoje
jupyter notebook

# Arba naudokite VS Code su Jupyter plėtiniu
```

### Darbas su skirtingais pamokų tipais

- **„Mokymosi“ pamokos**: dėmesys README.md dokumentacijai ir sąvokoms
- **„Kūrimo“ pamokos**: apima veikiančius kodo pavyzdžius Python ir TypeScript kalbomis
- Kiekviena pamoka turi README.md su teorija, kodo apžvalgomis ir nuorodomis į vaizdo turinį

## Kodo stiliaus gairės

### Python

- Naudokite `python-dotenv` aplinkos kintamųjų valdymui
- Importuokite `openai` biblioteką API sąveikai
- Naudokite `pylint` kodo tikrinimui (kai kurie pavyzdžiai turi `# pylint: disable=all` paprastumui)
- Laikykitės PEP 8 vardų konvencijų
- API duomenis laikykite `.env` faile, niekada kode

### TypeScript

- Naudokite `dotenv` paketą aplinkos kintamiesiems
- TypeScript konfigūracija `tsconfig.json` kiekvienai programai
- Naudokite `openai` paketą Azure OpenAI (klientą nukreipkite į `/openai/v1/` galinį tašką ir kvieskite `client.responses.create`); naudokite `@azure-rest/ai-inference` Microsoft Foundry modeliams
- Naudokite `nodemon` kūrimui su automatinio perkrovimo funkcija
- Statykite prieš paleidžiant: `npm run build`, tada `npm start`

### Bendros konvencijos

- Laikykite kodo pavyzdžius paprastus ir mokomuosius
- Įtraukite komentarus, paaiškinančius pagrindines sąvokas
- Kiekvienos pamokos kodas turėtų būti savarankiškas ir paleidžiamas
- Naudokite nuoseklias vardų schemas: `aoai-` prefiksas Azure OpenAI, `oai-` OpenAI API, `githubmodels-` Microsoft Foundry modeliai (paliktas paveldėtas prefiksas iš GitHub modelių laikotarpio)

## Dokumentacijos gairės

### Markdown stilius

- Visos URL turi būti apgaubtos `[tekstas](../../url)` formatu be papildomų tarpų
- Santykinės nuorodos turi prasidėti su `./` arba `../`
- Visos nuorodos į Microsoft domenus turi turėti stebėjimo ID: `?WT.mc_id=academic-105485-koreyst`
- URL adresuose neturi būti šalių specifinių lokalizacijų (vengti `/en-us/`)
- Vaizdai laikomi `./images` kataloge su aprašomaisiais pavadinimais
- Failų pavadinimuose naudokite anglų raides, skaičius ir brūkšnelius

### Vertimo palaikymas

- Talpykla palaiko 40+ kalbų per automatizuotas GitHub Actions
- Vertimai saugomi `translations/` kataloge
- Nepateikite dalinių vertimų
- Mašininiai vertimai nepriimami
- Išversti vaizdai laikomi `translated_images/` kataloge

## Testavimas ir tikrinimas

### Prieš pateikiant

Ši talpykla naudoja GitHub Actions tikrinimui. Prieš teikiant PR:

1. **Patikrinkite Markdown nuorodas**:
   ```bash
   # validate-markdown.yml darbo eiga tikrina:
   # - Sugadintas reliatyvus takas
   # - Trūksta sekimo ID keliuose
   # - Trūksta sekimo ID URL adresuose
   # - URL adresai su šalies lokalėmis
   # - Sugadinti išoriniai URL adresai
   ```

2. **Rankinis testavimas**:
   - Testuokite Python pavyzdžius: aktyvuokite venv ir vykdykite skriptus
   - Testuokite TypeScript pavyzdžius: `npm install`, `npm run build`, `npm start`
   - Patikrinkite, ar tinkamai sukonfigūruoti aplinkos kintamieji
   - Patikrinkite, ar API raktai veikia su kodo pavyzdžiais

3. **Kodo pavyzdžiai**:
   - Užtikrinkite, kad visas kodas veikia be klaidų
   - Testuokite tiek su Azure OpenAI, tiek su OpenAI API, kai taikoma
   - Patikrinkite, ar pavyzdžiai veikia su Microsoft Foundry modeliais, kur palaikoma

### Nėra automatinių testų

Tai mokomoji talpykla, skirta pamokoms ir pavyzdžiams. Nėra vienetinių ar integracinių testų. Tikrinimas pagrinde:
- Rankinis kodo pavyzdžių testavimas
- GitHub Actions Markdown tikrinimui
- Bendruomenės turinio švietimo vertinimas

## Pull request gairės

### Prieš pateikiant

1. Testuokite kodo pakeitimus tiek Python, tiek TypeScript, kai taikoma
2. Vykdykite Markdown tikrinimą (automatiškai paleidžiamas PR metu)
3. Užtikrinkite, kad visi Microsoft URL turi stebėjimo ID
4. Patikrinkite santykinių nuorodų galiojimą
5. Patvirtinkite vaizdų teisingą nuorodą

### PR antraštės formatas

- Naudokite aprašomas antraštes: `[Lesson 06] Fix Python example typo` arba `Update README for lesson 08`
- Nuoroda į susijusius issues, kai taikoma: `Fixes #123`

### PR aprašymas

- Paaiškinkite, kas buvo pakeista ir kodėl
- Nuorodinkite susijusius klausimus
- Nurodykite, kurie pavyzdžiai buvo testuoti, jei tai kodo pakeitimai
- Vertimų PR, pateikite visus failus, kad vertimas būtų pilnas

### Indėlio reikalavimai

- Pasirašykite Microsoft CLA (automatiškai pirmame PR)
- Prieš keisdami, atsisiųskite talpyklą į savo paskyrą
- Vienas PR vienam logiškam pakeitimui (nesujunkite nesusijusių pataisymų)
- Stenkitės, kad PR būtų orientuoti ir nedideli

## Dažnos darbo eigos

### Naujų kodo pavyzdžių pridėjimas

1. Eikite į atitinkamą pamokos katalogą
2. Sukurkite pavyzdį `python/` arba `typescript/` poaplankiuose
3. Laikykitės vardų konvencijos: `{provider}-{example-name}.{py|ts|js}`
4. Testuokite su tikrais API raktas
5. Dokumentuokite naujus aplinkos kintamuosius pamokos README

### Dokumentacijos atnaujinimas

1. Redaguokite README.md pamokos kataloge
2. Laikykitės Markdown gairių (stebėjimo ID, santykinės nuorodos)
3. Vertimai atnaujinami per GitHub Actions (redaguoti rankiniu būdu negalima)
4. Patikrinkite, ar visos nuorodos galioja

### Darbas su Dev konteineriais

1. Talpykloje yra `.devcontainer/devcontainer.json`
2. Po sukūrimo skriptas automatiškai įdiegia Python priklausomybes
3. Python ir Jupyter plėtiniai iš anksto sukonfigūruoti
4. Aplinka paremta `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Diegimas ir publikavimas

Tai mokymosi talpykla - nėra diegimo proceso. Mokymo programa yra prieinama per:

1. **GitHub talpykla**: tiesioginis kodų ir dokumentacijos pasiekiamumas
2. **GitHub Codespaces**: iškart paruošta kūrimo aplinka su konfigūracija
3. **Microsoft Learn**: turinys gali būti transliuojamas oficialioje mokymosi platformoje
4. **docsify**: dokumentacijos svetainė, sukuriama iš Markdown (žr. `docsifytopdf.js` ir `package.json`)

### Dokumentacijos svetainės kūrimas

```bash
# Sugeneruoti PDF iš dokumentacijos (jei reikia)
npm run convert
```

## Gedimų šalinimas

### Dažnos problemos

**Python importavimo klaidos**:
- Įsitikinkite, kad virtuali aplinka aktyvuota
- Vykdykite `pip install -r requirements.txt`
- Patikrinkite, kad Python versija būtų 3.9 ar naujesnė

**TypeScript kūrimo klaidos**:
- Vykdykite `npm install` konkrečiame programos kataloge
- Patikrinkite, ar Node.js versija yra suderinama
- Išvalykite `node_modules` ir perinstaliuokite, jei reikia

**API autentifikavimo klaidos**:
- Įsitikinkite, kad `.env` failas egzistuoja ir turi teisingas reikšmes
- Patikrinkite, ar API raktai galioja ir nėra pasibaigę
- Patikrinkite, kad galinių taškų URL teisingi jūsų regionui

**Trūksta aplinkos kintamųjų**:
- Nukopijuokite `.env.copy` į `.env`
- Užpildykite visus reikalingus reikšmes dirbant su pamoka
- Po `.env` atnaujinimo iš naujo paleiskite programą

## Papildomi ištekliai

- [Kurso nustatymo vadovas](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Indėlių gairės](./CONTRIBUTING.md)
- [Elgesio kodeksas](./CODE_OF_CONDUCT.md)
- [Saugumo politika](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Išplėstiniai kodų pavyzdžiai](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projekto specifinės pastabos

- Tai yra **mokomoji talpykla**, orientuota į mokymąsi, o ne į gamybos kodą
- Pavyzdžiai sąmoningai paprasti ir sutelkti į sąvokų mokymą
- Kodo kokybė subalansuota su mokymosi aiškumu
- Kiekviena pamoka yra savarankiška ir gali būti baigiama nepriklausomai
- Talpykla palaiko kelis API teikėjus: Azure OpenAI, OpenAI, Microsoft Foundry modelius ir neprisijungusius tiekėjus, tokius kaip Foundry Local ir Ollama
- Turinys yra daugiakalbis su automatizuotais vertimo procesais
- Aktyvi bendruomenė Discord platformoje klausimams ir palaikymui

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->