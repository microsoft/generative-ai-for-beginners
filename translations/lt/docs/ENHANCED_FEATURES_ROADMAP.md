# Patobulintų funkcijų ir patobulinimų gairių planas

Šiame dokumente pateikiami rekomenduojami patobulinimai ir patobulinimai pradedantiesiems skirtam Generatyviosios dirbtinio intelekto kursui, remiantis išsamia kodo apžvalga ir pramonės geriausių praktikų analize.

## Santrauka

Codebase buvo ištirtas dėl saugumo, kodo kokybės ir mokymo efektyvumo. Šiame dokumente pateikiamos rekomendacijos dėl skubių pataisymų, trumpalaikių patobulinimų ir ateities tobulinimų.

---

## 1. Saugumo patobulinimai (Prioritetas: Kritinis)

### 1.1 Skubios pataisos (įvykdytos)

| Problema | Paveikti failai | Būsena |
|----------|-----------------|---------|
| Įkoduotas SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Sutvarkyta |
| Trūksta aplinkos kintamųjų validacijos | Keletas JS/TS failų | Sutvarkyta |
| Nesaugūs funkcijų kvietimai | `11-integrating-with-function-calling/js-githubmodels/app.js` | Sutvarkyta |
| Failų tvarkyklių nutekėjimas | `08-building-search-applications/scripts/` | Sutvarkyta |
| Trūksta užklausų laiko limitų | `09-building-image-applications/python/` | Sutvarkyta |

### 1.2 Rekomenduojamos papildomos saugumo funkcijos

1. **Ribojimo pavyzdžiai**
   - Pridėti pavyzdinį kodą, rodantį, kaip įgyvendinti užklausų ribojimą API kvietimams
   - Demonstruoti eksponentinio atsitraukimo (exponential backoff) modelius

2. **API raktų sukimasis**
   - Pridėti dokumentaciją apie geriausias praktikas API raktų sukimui
   - Įtraukti pavyzdžių, naudojant Azure Key Vault ar panašias paslaugas

3. **Turinio saugumo integracija**
   - Pridėti pavyzdžių su Azure Content Safety API naudojimu
   - Demonstruoti įėjimo/išėjimo moderavimo modelius

---

## 2. Kodo kokybės patobulinimai

### 2.1 Pridėti konfigūracijos failai

| Failas | Paskirtis |
|--------|-----------|
| `.eslintrc.json` | JavaScript/TypeScript lintingo taisyklės |
| `.prettierrc` | Kodo formatavimo standartai |
| `pyproject.toml` | Python įrankių konfigūracija (Black, Ruff, mypy) |

### 2.2 Sukurti bendri įrankiai

Naujas `shared/python/` modulis su:
- `env_utils.py` - aplinkos kintamųjų valdymas
- `input_validation.py` - įvesties validacija ir sanitarizacija
- `api_utils.py` - saugūs API užklausų įvyniojimai

### 2.3 Rekomenduojami kodo patobulinimai

1. **Tipų anotacijų aprėptis**
   - Pridėti tipų anotacijas visuose Python failuose
   - Įjungti griežtą TypeScript režimą visuose TS projektuose

2. **Dokumentacijos standartai**
   - Pridėti docstring’us visoms Python funkcijoms
   - Pridėti JSDoc komentarus visoms JavaScript/TypeScript funkcijoms

3. **Testavimo sistema**
   - Pridėti pytest konfigūraciją ir pavyzdinius testus
   - Pridėti Jest konfigūraciją JavaScript/TypeScript

---

## 3. Mokymo patobulinimai

### 3.1 Naujos pamokų temos

1. **Saugumas DI programose** (Siūloma 22 pamoka)
   - Užklausų injekcijos atakos ir apsauga
   - API raktų valdymas
   - Turinio moderavimas
   - Užklausų ribojimas ir piktnaudžiavimo prevencija

2. **Produkcijos diegimas** (Siūloma 23 pamoka)
   - Docker konteinerizacija
   - CI/CD vamzdynai
   - Stebėjimas ir žurnalo pildymas
   - Kaštų valdymas

3. **Pažangios RAG technikos** (Siūloma 24 pamoka)
   - Hibridinė paieška (raktažodžių + semantinė)
   - Perklasifikavimo strategijos
   - Daugiaplomė RAG
   - Vertinimo metrika

### 3.2 Esamų pamokų patobulinimai

| Pamoka | Rekomenduojamas patobulinimas |
|--------|-------------------------------|
| 06 - Teksto generavimas | Pridėti srautinio atsakymo pavyzdžius |
| 07 - Pokalbių programos | Pridėti pokalbio atminties modelius |
| 08 - Paieškos programos | Pridėti vektorių duomenų bazės palyginimą |
| 09 - Vaizdų generavimas | Pridėti vaizdų redagavimo/variacijų pavyzdžius |
| 11 - Funkcijų kvietimas | Pridėti lygiagretų funkcijų kvietimą |
| 15 - RAG | Pridėti fragmentavimo strategijų palyginimą |
| 17 - DI agentai | Pridėti daugiaagentinę orkestraciją |

---

## 4. API modernizavimas

### 4.1 Pasenusių API modelių atnaujinimas

| Senas modelis | Naujas modelis | Paveikti failai |
|---------------|---------------|-----------------|
| `openai.api_type = "azure"` | `AzureOpenAI()` klientas | Keletas skriptų `08-building-search-applications/` |
| `openai.ChatCompletion.create()` | `client.chat.completions.create()` | Keletas notebook’ų |
| `df.append()` (pandas) | `pd.concat()` | RAG notebook’as |

### 4.2 Naujos API funkcijos demonstravimas

1. **Struktūruoti atsakymai** (OpenAI)
   - JSON režimas
   - Funkcijų kvietimas su griežtomis schemomis

2. **Vizio galimybės**
   - Vaizdų analizė su GPT-4V
   - Daugiaplomiai užklausos modeliai

3. **Asistentų API**
   - Kodo interpretatorius
   - Failų paieška
   - Individualūs įrankiai

---

## 5. Infrastruktūros patobulinimai

### 5.1 CI/CD patobulinimai

Esami darbo srautai apdoroja markdown validaciją. Rekomenduojamos pridėtinės dalys:

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

Atnaujinti `.devcontainer/devcontainer.json`:

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

### 6.2 Interaktyvus žaidimų laukas

Rekomenduojama pridėti:
- Jupyter notebook’us su iš anksto įrašytais API raktais (per aplinkos kintamuosius)
- Gradio/Streamlit demonstracijas vizualiems mokymosi stiliams
- Interaktyvias viktorinas žinių tikrinimui

---

## 7. Daugiakalbė palaikymas

### 7.1 Dabartinis kalbų aprėptis

| Technologija | Įtrauktos pamokos | Būsena |
|--------------|-------------------|--------|
| Python | Visos | Užbaigta |
| TypeScript | 06-09, 11 | Iš dalies |
| JavaScript | 06-08, 11 | Iš dalies |
| .NET/C# | Kai kurios | Iš dalies |

### 7.2 Rekomenduojamos papildomos kalbos

1. **Go** - sparčiai auganti DI/ML įrankių kalba
2. **Rust** - kritinėms našumo programoms
3. **Java/Kotlin** - verslo programoms

---

## 8. Veikimo optimizavimai

### 8.1 Kodo lygio optimizacijos

1. **Async/Await modeliai**
   - Pridėti async pavyzdžius partijų apdorojimui
   - Demonstruoti lygiagretinių API užklausų modelius

2. **Talpyklos strategijos**
   - Pridėti įterpinių talpyklos pavyzdžius
   - Demonstruoti atsakymų talpyklos modelius

3. **Žetonų optimizavimas**
   - Pridėti tiktoken naudojimo pavyzdžius
   - Demonstruoti užklausų glaudinimo technikas

### 8.2 Kaštų optimizavimo pavyzdžiai

Pridėti pavyzdžius, rodant:
- Modelių pasirinkimą pagal užduoties sudėtingumą
- Užklausų inžineriją žetonų taupymui
- Partijų apdorojimą masinėms operacijoms

---

## 9. Prieinamumas ir internacionalizacija

### 9.1 Dabartinė vertimų būklė

| Kalba | Būsena |
|-------|--------|
| Anglų | Užbaigta |
| Kinų (supaprastinta) | Užbaigta |
| Japonų | Užbaigta |
| Korėjiečių | Užbaigta |
| Ispanų | Iš dalies |
| Portugalų | Iš dalies |
| Turkų | Iš dalies |
| Lenkų | Iš dalies |

### 9.2 Prieinamumo gerinimai

1. Pridėti alt tekstą visiems paveikslėliams
2. Užtikrinti tinkamą sintaksės paryškinimą kodo pavyzdžiuose
3. Pridėti vaizdo transkriptus visam vaizdo turiniui
4. Užtikrinti spalvų kontrastą pagal WCAG gaires

---

## 10. Įgyvendinimo prioritetas

### 1 etapas: Skubi (1-2 savaitės)
- [x] Ištaisyti kritines saugumo problemas
- [x] Pridėti kodo kokybės konfigūraciją
- [x] Sukurti bendrus įrankius
- [x] Dokumentuoti saugumo gaires

### 2 etapas: Trumpalaikis (3-4 savaitės)
- [ ] Atnaujinti pasenusius API modelius
- [ ] Pridėti tipų anotacijas visiems Python failams
- [ ] Pridėti CI/CD darbo srautus kodo kokybei
- [ ] Sukurti saugumo skenavimo darbo srautą

### 3 etapas: Vidutinis laikotarpis (2-3 mėn.)
- [ ] Pridėti naują saugumo pamoką
- [ ] Pridėti produkcijos diegimo pamoką
- [ ] Pagerinti DevContainer nustatymą
- [ ] Pridėti interaktyvias demonstracijas

### 4 etapas: Ilgalaikis (4+ mėn.)
- [ ] Pridėti pažangią RAG pamoką
- [ ] Išplėsti kalbų aprėptį
- [ ] Pridėti išsamų testų rinkinį
- [ ] Sukurti sertifikavimo programą

---

## Išvada

Šis gairių planas pateikia struktūruotą požiūrį, kaip patobulinti Generatyviosios dirbtinio intelekto pradedantiesiems kursą. Sprendžiant saugumo problemas, modernizuojant API ir pridedant mokymo turinį, kursas geriau paruoš studentus realių DI programų kūrimui.

Dėl klausimų ar indėlių prašome atidaryti problemą GitHub saugykloje.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome turėti omenyje, kad automatizuoti vertimai gali turėti klaidų arba netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmogiškas vertimas. Mes neatsakome už jokius nesusipratimus ar neteisingą vertimą, kilusius naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->