# Patobulintų funkcijų ir patobulinimų planas

Šiame dokumente apžvelgiami rekomenduojami patobulinimai ir patobulinimai Generatyviosios AI pradedantiesiems kursui, remiantis išsamia kodo peržiūra ir pramonės gerosios praktikos analize.

## Santrauka

Kodo bazė buvo analizuojama dėl saugumo, kodo kokybės ir mokomojo efektyvumo. Šiame dokumente pateikiamos rekomendacijos dėl skubaus taisymo, trumpalaikių patobulinimų ir ateities atnaujinimų.

---

## 1. Saugumo patobulinimai (Prioritetas: Kritinis)

### 1.1 Skubūs pataisymai (Atlikta)

| Problema | Paveikti failai | Būsena |
|-------|----------------|--------|
| Užkoduotas SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Ištaisyta |
| Trūksta aplinkos kintamųjų validacijos | Keli JS/TS failai | Ištaisyta |
| Nesaugūs funkcijų kvietimai | `11-integrating-with-function-calling/js-githubmodels/app.js` | Ištaisyta |
| Failų valdiklių nutekėjimas | `08-building-search-applications/scripts/` | Ištaisyta |
| Trūksta užklausų laiko ribojimų | `09-building-image-applications/python/` | Ištaisyta |

### 1.2 Rekomenduojamos papildomos saugumo funkcijos

1. **Ribojimo pavyzdžiai**
   - Pridėti pavyzdinį kodą, kaip įgyvendinti užklausų greičio ribojimą API kvietimams
   - Demonstruoti eksponentinio atidėjimo (exponential backoff) modelius

2. **API raktų keitimas**
   - Pridėti dokumentaciją apie gerąją praktiką API raktų keitimui
   - Įtraukti pavyzdžius, kaip naudoti Azure Key Vault ar panašias paslaugas

3. **Turinio saugos integracija**
   - Pridėti pavyzdžius naudojant Azure Content Safety API
   - Demonstruoti įėjimo/išėjimo moderavimo modelius

---

## 2. Kodo kokybės patobulinimai

### 2.1 Pridėti konfigūracijos failai

| Failas | Paskirtis |
|------|---------|
| `.eslintrc.json` | JavaScript/TypeScript linterio taisyklės |
| `.prettierrc` | Kodo formatavimo standartai |
| `pyproject.toml` | Python įrankių konfigūracija (Black, Ruff, mypy) |

### 2.2 Sukurtos bendrinamos paslaugos

Naujas `shared/python/` modulis su:
- `env_utils.py` - Aplinkos kintamųjų valdymas
- `input_validation.py` - Įvesties validacija ir sanitizacija
- `api_utils.py` - Saugūs API užklausų įvyniojimai

### 2.3 Rekomenduojami kodo patobulinimai

1. **Tipų anotacijų aprėptis**
   - Pridėti tipų anotacijas visuose Python failuose
   - Įjungti griežtą TypeScript režimą visuose TS projektuose

2. **Dokumentacijos standartai**
   - Pridėti docstring’us visoms Python funkcijoms
   - Pridėti JSDoc komentarus visoms JavaScript/TypeScript funkcijoms

3. **Testavimo karkasas**
   - Pridėti pytest konfigūraciją ir pavyzdinius testus _(atlikta: pytest konfigūracija `pyproject.toml`; pavyzdiniai testai bendrinamoms paslaugoms [`tests/`](../../../tests), vykdomi CI aplinkoje)_
   - Pridėti Jest konfigūraciją JavaScript/TypeScript

---

## 3. Mokymo patobulinimai

### 3.1 Naujos pamokų temos

1. **Saugumas AI programose** (siūloma pamoka 22)
   - Prompto įterpimo atakos ir gynyba
   - API raktų valdymas
   - Turinio moderavimas
   - Greičio ribojimas ir piktnaudžiavimo prevencija

2. **Produkcijos diegimas** (siūloma pamoka 23)
   - Docker konteinerizacija
   - CI/CD pipingai
   - Stebėjimas ir žurnalas
   - Sąnaudų valdymas

3. **Išplėstiniai RAG metodai** (siūloma pamoka 24)
   - Hibridinis paieška (raktažodis + semantika)
   - Perreitingavimo strategijos
   - Multimodalinė RAG
   - Vertinimo metrika

### 3.2 Esamų pamokų patobulinimai

| Pamoka | Rekomenduojamas patobulinimas |
|--------|------------------------|
| 06 - Teksto generavimas | Pridėti srautinio atsakymo pavyzdžius |
| 07 - Pokalbių programos | Pridėti pokalbių atminties modelius |
| 08 - Paieškos programos | Pridėti vektorinių duomenų bazių palyginimą |
| 09 - Vaizdų generavimas | Pridėti vaizdų redagavimo/pokyčių pavyzdžius |
| 11 - Funkcijų kvietimas | Pridėti lygiagretų funkcijų kvietimą |
| 15 - RAG | Pridėti dalių (chunking) strategijų palyginimą |
| 17 - AI agentai | Pridėti daugiaprogramių agentų koordinavimą |

---

## 4. API modernizavimas

### 4.1 Pasenę API modeliai (migracija atlikta)

Visi Python ir TypeScript **chat** pavyzdžiai buvo perkelti nuo Chat Completions API prie **Responses API** (`client.responses.create(...)` → `response.output_text`).

| Senasis modelis | Naujas modelis | Būsena |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (chat) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | Atlikta |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | Atlikta |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | `openai` paketas `client.responses.create()` → `response.output_text` | Atlikta |
| `df.append()` (pandas) | `pd.concat()` | Atlikta |

> **Pastaba:** Microsoft Foundry Models pavyzdžiai, naudojantys `azure-ai-inference` / `@azure-rest/ai-inference` SDK (`client.complete()`) lieka naudoti Model Inference API, kuris nepalaiko Responses API. `AzureOpenAI()` yra tyčia paliktas ten, kur vis dar teisingas (embedding’ai ir vaizdų generavimas).

### 4.2 Naujos API funkcijos demonstravimui

1. **Struktūruotos išvestys** (OpenAI)
   - JSON režimas
   - Funkcijų kvietimas su griežtai apibrėžtomis schemomis

2. **Vizijos galimybės**
   - Vaizdų analizė su GPT-4o (vizija)
   - Multimodalūs promptai

3. **Responses API įmontuoti įrankiai** (pakeičia senąjį Assistants API)
   - Kodo interpretatorius
   - Failų paieška
   - Tinklo paieška ir pritaikyti įrankiai

---

## 5. Infrastruktūros patobulinimai

### 5.1 CI/CD patobulinimai

Įgyvendinta [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): Python lintinimo/formatavimo (Ruff + Black) taisyklės yra **privalomos** palaikomame `shared/` modulyje ir vykdomos kaip **teisės patarimas** likusioje kurso dalyje, taip pat patarimų ESLint peržiūra JavaScript/TypeScript. Iliustracinė bazė buvo:

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

### 5.2 Saugumo skenavimas

Įgyvendinta [`.github/workflows/security.yml`](../../../.github/workflows/security.yml): CodeQL analizė Python ir JavaScript/TypeScript (push, pull request bei savaitinis tvarkaraštis) papildomai su priklausomybių peržiūra pull request metu. Iliustracinė bazė buvo:

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

## 6. Kūrėjo patirties patobulinimai

### 6.1 DevContainer patobulinimai

Įgyvendinta [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) ir [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): konteineris dabar komplektuoja Pylance, Black formatavimo įrankį, Ruff, ESLint, Prettier ir Copilot plėtinius, įjungia formatavimą saugojimo metu susietą su repo Black/Prettier konfigūracija, ir įdiegia kūrėjo įrankius (`ruff`, `black`, `mypy`, `pytest`), kad [code-quality workflow](../../../.github/workflows/code-quality.yml) būtų galima pakartoti lokaliai. `mcr.microsoft.com/devcontainers/universal` bazinis paveikslėlis jau apima Python ir Node, tad papildomos funkcijos nereikalingos. Iliustracinė bazė buvo:

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

### 6.2 Interaktyvi pavyzdžių aplinka

Siūloma pridėti:
- Jupyter užrašų knygeles su iš anksto įkrautais API raktais (per aplinkos kintamuosius)
- Gradio/Streamlit demonstracijas vizualiems mokiniams
- Interaktyvias viktorinas žinių įvertinimui

---

## 7. Daugiakalbė palaikymas

### 7.1 Esama kalbų aprėptis

| Technologija | Apimtis pamokų | Būsena |
|------------|-----------------|--------|
| Python | Visos | Baigta |
| TypeScript | 06-09, 11 | Iš dalies |
| JavaScript | 06-08, 11 | Iš dalies |
| .NET/C# | Kai kurios | Iš dalies |

### 7.2 Rekomenduojami papildymai

1. **Go** - augantis AI/ML įrankių naudojimas
2. **Rust** - našumo kritinėms programoms
3. **Java/Kotlin** - verslo programoms

---

## 8. Veikimo optimizavimas

### 8.1 Kodo lygmens optimizacijos

1. **Async/Await modeliai**
   - Pridėti asinchroninių pavyzdžių partijų apdorojimui
   - Demonstruoti lygiagrečius API kvietimus

2. **Talpyklos strategijos**
   - Pridėti įterpimų kešavimo pavyzdžius
   - Demonstruoti atsakymų kešavimo modelius

3. **Tokenų optimizavimas**
   - Pridėti tiktoken naudojimo pavyzdžius
   - Demonstruoti promptų suspaudimo technikas

### 8.2 Sąnaudų optimizavimo pavyzdžiai

Pridėti pavyzdžius, demonstruojančius:
- Modelio parinkimą pagal užduoties sudėtingumą
- Promptų inžineriją dėl tokenų efektyvumo
- Partišką apdorojimą didelėms operacijoms

---

## 9. Prieinamumas ir internacionalizacija

### 9.1 Esama vertimų būklė

Visi vertimai yra **baigti** ir generuojami automatiškai naudojant [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst), kuris palaiko ir suderina daugiau nei 50 kalbų versijų kurso turinį su anglų šaltiniu. Išverstas turinys yra `translations/` kataloge, o lokalizuoti vaizdai – `translated_images/`; pilnas kalbų sąrašas paskelbtas repozitorijos README pradžioje.

| Aspektas | Būsena |
|--------|--------|
| Vertimo aprėptis | Baigta — 50+ kalbų, visos pamokos |
| Vertimo metodas | Automatizuotas per [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) |
| Sinchronizuojama su anglų šaltiniu | Taip — automatiškai regeneruojama |

### 9.2 Prieinamumo patobulinimai

1. Pridėti alt tekstus visiems paveikslėliams
2. Užtikrinti tinkamą sintaksės paryškinimą kodo pavyzdžiuose
3. Pridėti vaizdo įrašų transkriptus visam vaizdo turiniui
4. Užtikrinti spalvų kontrastą pagal WCAG gaires

---

## 10. Įgyvendinimo prioritetas

### 1 fazė: Skubi (1–2 savaitės)
- [x] Ištaisyti kritines saugumo problemas
- [x] Pridėti kodo kokybės konfigūraciją
- [x] Sukurti bendrinamas paslaugas
- [x] Dokumentuoti saugumo gaires

### 2 fazė: Trumpalaikė (3–4 savaitės)
- [x] Atnaujinti pasenusius API modelius (Chat Completions → Responses API, Python + TypeScript)
- [ ] Pridėti tipų anotacijas visiems Python failams (padaryta palaikomame `shared/` modulyje; pamokų pavyzdžiai palikti paprasti)
- [x] Pridėti CI/CD darbo eigas kodo kokybei
- [x] Sukurti saugumo skeno darbo eigą

### 3 fazė: Vidutinės trukmės (2–3 mėnesiai)
- [ ] Pridėti naują saugumo pamoką
- [ ] Pridėti gamybos diegimo pamoką
- [x] Patobulinti DevContainer konfigūraciją
- [ ] Pridėti interaktyvias demonstracijas

### 4 fazė: Ilgalaikė (4 ir daugiau mėnesių)
- [ ] Pridėti pažangią RAG pamoką
- [ ] Išplėsti kalbų aprėptį
- [ ] Pridėti visapusišką testų rinkinį
- [ ] Sukurti sertifikavimo programą

---

## Išvada

Šis planas pateikia struktūruotą požiūrį į Generatyviosios AI pradedantiesiems kurso tobulinimą. Sprendžiant saugumo klausimus, modernizuojant API ir pridedant mokomąją medžiagą, kursas geriau pasiruoš kursantams realių AI programų kūrimui.

Dėl klausimų ar indėlių prašome atidaryti problemą GitHub repozitorijoje.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->