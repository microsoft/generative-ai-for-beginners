# Täiendatud funktsioonide ja parenduste teekaart

See dokument kirjeldab soovitatud täiustusi ja parandusi Generative AI for Beginners kursuse jaoks, tuginedes põhjalikule koodiülevaatele ja tööstuse parimate tavade analüüsile.

## Kokkuvõte

Koodibaasi on analüüsitud turvalisuse, koodi kvaliteedi ja haridusliku tõhususe osas. See dokument annab soovitused kiirete paranduste, lühiajaliste täiustuste ja tulevaste täiustuste kohta.

---

## 1. Turvalisuse täiustused (Prioriteet: kriitiline)

### 1.1 Kiired parandused (tehtud)

| Probleem | Mõjutatud failid | Staatus |
|-------|----------------|--------|
| Kõvakodeeritud SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Parandatud |
| Puuduv keskkonnavalideerimine | Mitmed JS/TS failid | Parandatud |
| Ebaturvalised funktsioonikutsed | `11-integrating-with-function-calling/js-githubmodels/app.js` | Parandatud |
| Failikäepideme lekked | `08-building-search-applications/scripts/` | Parandatud |
| Puuduvad päringu ajaülesanded | `09-building-image-applications/python/` | Parandatud |

### 1.2 Soovitatud täiendavad turvafunktsioonid

1. **Kiirusepiirangute näited**
   - Lisa näidiskood, mis demonstreerib API kutsete kiirusepiirangu rakendamist
   - Näita eksponentsiaalse taandumise mustreid

2. **API võtme rotatsioon**
   - Lisa dokumentatsioon parimate tavade kohta API võtmete rotatsiooniks
   - Kaasa näited Azure Key Vaulti või sarnaste teenuste kasutamisest

3. **Sisuturvalisuse integreerimine**
   - Lisa näited Azure Content Safety API kasutamisest
   - Demonstreeri sisendi/väljundi modereerimise mustreid

---

## 2. Koodi kvaliteedi parendused

### 2.1 Lisatud konfiguratsioonifailid

| Fail | Eesmärk |
|------|---------|
| `.eslintrc.json` | JavaScript/TypeScript lintimisreeglid |
| `.prettierrc` | Koodi vormindamise standardid |
| `pyproject.toml` | Pythoni tööriistade konfiguratsioon (Black, Ruff, mypy) |

### 2.2 Loodud jagatud utiliidid

Uus `shared/python/` moodul koos:
- `env_utils.py` - Keskkonnamuutujate haldus
- `input_validation.py` - Sisendi valideerimine ja puhastus
- `api_utils.py` - Turvalised API päringute kapslid

### 2.3 Soovitatud koodi parendused

1. **Tüübiviidete (type hints) ulatus**
   - Lisa tüübiviited kõigile Pythoni failidele
   - Luba ranget tüüpi kontrolli TypeScripti projektides

2. **Dokumentatsiooni standardid**
   - Lisa dokstrings kõikidele Python funktsioonidele
   - Lisa JSDoc kommentaarid kõigile JavaScript/TypeScript funktsioonidele

3. **Testimisraamistik**
   - Lisa pytest konfiguratsioon ja näidistestid _(tehtud: pytest konfig `pyproject.toml` failis; jagatud utiliitide näidistestid asuvad [`tests/`](../../../tests) kaustas ja jooksevad CI-s)_
   - Lisa Jest konfiguratsioon JavaScript/TypeScript jaoks

---

## 3. Hariduslikud täiustused

### 3.1 Uued õppetemad

1. **Turvalisus AI rakendustes** (ettepanek õppetund 22)
   - Prompt'i süstimise rünnakud ja kaitsed
   - API võtmete haldus
   - Sisu modereerimine
   - Kiiruse piiramine ja väärkasutuse ennetamine

2. **Tootmisesse juurutamine** (ettepanek õppetund 23)
   - Konteineriseerimine Dockeriga
   - CI/CD torujuhtmed
   - Jälgimine ja logimine
   - Kulude haldamine

3. **Arenenud RAG tehnikad** (ettepanek õppetund 24)
   - Hübriidotsing (märksõna + semantiline)
   - Ümberjärjestamise strateegiad
   - Mitme modaaliga RAG
   - Hindamismeetrikad

### 3.2 Olemasolevate õppetundide parendused

| Õppetund | Soovitatud parendus |
|--------|------------------------|
| 06 - Teksti genereerimine | Lisa voogedastusvastuste näited |
| 07 - Vestlusrakendused | Lisa vestluse mälu mustrid |
| 08 - Otsingurakendused | Lisa vektoriandmebaasi võrdlus |
| 09 - Pildi genereerimine | Lisa pildi redigeerimise/muutmise näited |
| 11 - Funktsioonikutsed | Lisa paralleelsed funktsioonikutsed |
| 15 - RAG | Lisa tükkide strateegiate võrdlus |
| 17 - AI agendid | Lisa mitme agendi orkestreerimine |

---

## 4. API moderniseerimine

### 4.1 Aegunud API mustrid (Migratsioon tehtud)

Kõik Python ja TypeScripti **vestluse** näited on üle viidud Chat Completions API-st Responses API-le (`client.responses.create(...)` → `response.output_text`).

| Vana muster | Uus muster | Staatus |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (vestlus) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | Tehtud |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | Tehtud |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | `openai` paketist `client.responses.create()` → `response.output_text` | Tehtud |
| `df.append()` (pandas) | `pd.concat()` | Tehtud |

> **Märkus:** Microsoft Foundry mudelite näited, mis kasutavad `azure-ai-inference` / `@azure-rest/ai-inference` SDK-d (`client.complete()`), jäävad Model Inference API kasutajaks, mis ei toeta Responses API-d. `AzureOpenAI()` on teadlikult alles hoitud seal, kus see on endiselt sobilik (embedid ja pildigeneratsioon).

### 4.2 Uued API funktsioonid näitamiseks

1. **Struktureeritud väljundid** (OpenAI)
   - JSON režiim
   - Funktsioonikutsed rangete skeemidega

2. **Visuaalsed võimed**
   - Pildianalüüs GPT-4o (vision) abil
   - Mitme modaaliga promptid

3. **Responses API sisseehitatud tööriistad** (asendab vanade Assistants API)
   - Koodi tõlgendaja
   - Failiotsing
   - Veebipõhine otsing ja kohandatud tööriistad

---

## 5. Taristu täiustused

### 5.1 CI/CD täiustused

Rakendatud failis [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): Python lintimine/vormindamine (Ruff + Black) on **kohustuslik** hallatavale `shared/` utiliitide moodulile ja **soovitav** ülejäänud kursusele, samuti on soovitav ESLinti läbimine JavaScript/TypeScripti jaoks. Illustreeriv algväärtus oli:

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

### 5.2 Turvalisuse skaneerimine

Rakendatud failis [`.github/workflows/security.yml`](../../../.github/workflows/security.yml): CodeQL analüüs Pythonile ja JavaScript/TypeScriptile (pushi, pull requesti ja nädalapõhise graafiku ajal) ning sõltuvuste ülevaatus pull requestidel. Illustreeriv algväärtus oli:

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

## 6. Arendajakogemuse parandused

### 6.1 DevContainer täiustused

Rakendatud failides [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) ja [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): konteinerisse on nüüd lisatud Pylance, Black vormindaja, Ruff, ESLint, Prettier ja Copiloti laiendused, lubatud on salvestamisel vormindamine, mis on ühendatud repomallide Black/Prettier konfiguratsiooniga, ning paigaldatud arendustööriistad (`ruff`, `black`, `mypy`, `pytest`), mis võimaldavad [code-quality workflow't](../../../.github/workflows/code-quality.yml) lokaalselt korrata. Base Image `mcr.microsoft.com/devcontainers/universal` sisaldab juba Pythonit ja Node'i, nii et lisafunktsionaalsust pole vaja. Illustreeriv algväärtus oli:

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

### 6.2 Interaktiivne mänguväljak

Kaalu lisamist:
- Jupyter märkmikud eelväidetud API võtmestega (keskkonna kaudu)
- Gradio/Streamlit demo visuaalsetele õppijatele
- Interaktiivsed viktoriinid teadmiste hindamiseks

---

## 7. Mitmekeelne tugi

### 7.1 Praegune keelte katvus

| Tehnoloogia | Katvusega õppetunnid | Staatus |
|------------|-----------------|--------|
| Python | Kõik | Täielik |
| TypeScript | 06-09, 11 | Osaline |
| JavaScript | 06-08, 11 | Osaline |
| .NET/C# | Mõned | Osaline |

### 7.2 Soovitatud lisandused

1. **Go** - kasvav AI/ML tööriistades
2. **Rust** - jõudlust vajavad rakendused
3. **Java/Kotlin** - ettevõtte rakendused

---

## 8. Jõudluse optimeerimine

### 8.1 Kooditase optimeerimine

1. **Async/Await mustrid**
   - Lisa asünkroonsed näited eraldi töötluseks
   - Demonstreeri samaaegsete API kutsede mustreid

2. **Vahemälustrateegiad**
   - Lisa näited embed'de vahemällu salvestamisest
   - Demonstreeri vastuste vahemälu mustreid

3. **Tokeni optimeerimine**
   - Lisa tiktoken kasutamisnäited
   - Demonstreeri prompt'i tihendamise tehnikaid

### 8.2 Kulu optimeerimise näited

Lisa näited, mis demonstreerivad:
- Mudeli valik vastavalt ülesande keerukusele
- Prompt inseneritöö tokenite efektiivsuseks
- Pakkide töötlemine hulgitöödeks

---

## 9. Juurdepääsetavus ja rahvusvahelistumine

### 9.1 Praegune tõlke staatus

Kõik tõlked on **täielikud** ja genereeritud automaatselt [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) poolt, mis toodab ja hoiab enam kui 50 keeles kursuse sisu inglise allikale sünkroonis. Tõlgitud materjalid on kaustas `translations/` ja lokaliseeritud pildid `translated_images/`; saadaval olevate keelte täielik nimekiri on avaldatud hoidla README faili alguses.

| Aspekt | Staatus |
|--------|--------|
| Tõlke katvus | Täielik — üle 50 keele, kõik õppetunnid |
| Tõlke meetod | Automatiseeritud [Azure Co-op Translator'i](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) abil |
| Inglise lähtekoodiga sünkroonis | Jah — automaatselt uuendatud |

### 9.2 Juurdepääsetavuse parandused

1. Lisa kõigile piltidele alt-tekst
2. Tagada koodinäidete korrektne süntaksitoe esitus
3. Lisa videote tekstilised transkriptsioonid
4. Tagada värvikontrasti kooskõla WCAG juhistega

---

## 10. Rakendamise prioriteet

### Faas 1: Kiire (1.-2. nädal)
- [x] Paranda kriitilised turvaprobleemid
- [x] Lisa koodi kvaliteedi konfiguratsioon
- [x] Loo jagatud utiliidid
- [x] Dokumenteeri turvalisuse juhised

### Faas 2: Lühiajaline (3.-4. nädal)
- [x] Uuenda aegunud API mustrid (Chat Completions → Responses API, Python + TypeScript)
- [ ] Lisa tüübiviited kõigile Python failidele (tehtud hallatavale `shared/` moodulile; õppetundide näited lihtsana)
- [x] Lisa CI/CD töövood koodi kvaliteedile
- [x] Loo turvalisuse skaneerimise töövoog

### Faas 3: Keskmise tähtajaga (2.-3. kuu)
- [ ] Lisa uus turvalisuse õppetund
- [ ] Lisa tootmisse juurutamise õppetund
- [x] Paranda DevContainer seadistus
- [ ] Lisa interaktiivsed demo'd

### Faas 4: Pikaajaline (4. kuu ja edaspidi)
- [ ] Lisa arenenud RAG õppetund
- [ ] Laienda keelekatvust
- [ ] Lisa põhjalik testide komplekt
- [ ] Loo sertifitseerimisprogramm

---

## Kokkuvõte

See teekaart pakub struktureeritud lähenemist Generative AI for Beginners kursuse parendamiseks. Turvaprobleemide käsitlemine, API-de moderniseerimine ja haridusliku sisu lisamine valmistab kursuse paremini ette tudengeid reaalse AI rakenduste arendamiseks.

Küsimuste või panuste puhul palun avage probleem GitHubi hoidlas.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->