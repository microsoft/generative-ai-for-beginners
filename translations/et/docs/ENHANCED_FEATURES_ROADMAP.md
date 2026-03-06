# Täiustatud funktsioonide ja täiustuste teekaart

See dokument kirjeldab soovitatud täiustusi ja parendusi Generative AI for Beginners kursuse jaoks, tuginedes põhjalikule koodi ülevaatele ja tööstuse parimate tavade analüüsile.

## Juhatuse kokkuvõte

Koodibaas on analüüsitud turvalisuse, koodi kvaliteedi ja haridusliku tõhususe osas. See dokument pakub soovitusi koheseks kõrvaldamiseks, lühi- ja pikaajalisteks täiustusteks.

---

## 1. Turvalisuse täiustused (Prioriteet: Kriitiline)

### 1.1 Kohesed parandused (tehtud)

| Probleem | Mõjutatud failid | Staatus |
|----------|------------------|---------|
| Hardcodeeritud SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Parandatud |
| Keskkonna muutujate valideerimise puudumine | Mitmed JS/TS failid | Parandatud |
| Ohtlikud funktsioonikutsed | `11-integrating-with-function-calling/js-githubmodels/app.js` | Parandatud |
| Failikäitlejate lekked | `08-building-search-applications/scripts/` | Parandatud |
| Päringu time-outi puudumine | `09-building-image-applications/python/` | Parandatud |

### 1.2 Soovitatud täiendavad turvaomadused

1. **Päringute kiirusepiirangu näited**
   - Lisa näidiskood, mis näitab, kuidas rakendada API päringute kiirusepiirangut
   - Näita eksponentsiaalse tagasiveo mustreid

2. **API võtmete rotatsioon**
   - Lisa dokumentatsioon parimate praktikate kohta API võtmete vahetamiseks
   - Kaasa näited Azure Key Vaulti või sarnaste teenuste kasutamisest

3. **Sisuturvalisuse integreerimine**
   - Lisa näited Azure Content Safety API kasutamisest
   - Näita sisendi/väljundi modereerimise mustreid

---

## 2. Koodi kvaliteedi parandused

### 2.1 Lisatud konfiguratsioonifailid

| Fail | Eesmärk |
|-------|----------|
| `.eslintrc.json` | JavaScript/TypeScript lintimise reeglid |
| `.prettierrc` | Koodi vormindamise standardid |
| `pyproject.toml` | Pythoni tööriistade konfiguratsioon (Black, Ruff, mypy) |

### 2.2 Loodud jagatud utiliidid

Uus `shared/python/` moodul koos:
- `env_utils.py` - Keskkonnamuutujate käsitlemine
- `input_validation.py` - Sisendi valideerimine ja puhastamine
- `api_utils.py` - Turvalised API päringu wrapperid

### 2.3 Soovitatud koodiparandused

1. **Tüübiviidete ulatus**
   - Lisa tüübiviited kõigile Python failidele
   - Luba ranget TypeScripti režiimi kõigis TS projektides

2. **Dokumenteerimisstandardid**
   - Lisa docstringid kõigile Python funktsioonidele
   - Lisa JSDoc kommentaarid kõigile JavaScript/TypeScript funktsioonidele

3. **Testimiskeskkond**
   - Lisa pytest konfiguratsioon ja näidistestid
   - Lisa Jest konfiguratsioon JavaScript/TypeScript jaoks

---

## 3. Hariduslikud täiustused

### 3.1 Uued õppetemad

1. **Turvalisus tehisintellekti rakendustes** (ettepanek: Õppetund 22)
   - Prompt injection rünnakud ja kaitsed
   - API võtmete haldamine
   - Sisutöötlus
   - Kiirusepiirang ja väärkasutuse ennetamine

2. **Tootmiskeskkonna juurutamine** (ettepanek: Õppetund 23)
   - Konteineriseerimine Dockeriga
   - CI/CD torujuhtmed
   - Jälgimine ja logimine
   - Kulude haldamine

3. **Täiustatud RAG tehnikad** (ettepanek: Õppetund 24)
   - Hübriidotsing (märksõna + semantiline)
   - Ümberhindamise strateegiad
   - Mitme modaaliga RAG
   - Hinnangumõõdikud

### 3.2 Olemasolevate õppetundide täiustused

| Õppetund | Soovitatud täiustus |
|----------|--------------------|
| 06 - Teksti genereerimine | Lisa voogedastuse vastuse näited |
| 07 - Vestlusrakendused | Lisa vestluse mälupatt
ernid |
| 08 - Otsingurakendused | Lisa vektorandmebaasi võrdlus |
| 09 - Pildigeneratsioon | Lisa pilditöötluse/muutmise näited |
| 11 - Funktsioonikõned | Lisa paralleelsete funktsioonikõnede näited |
| 15 - RAG | Lisa tükkideks jagamise strateegiate võrdlus |
| 17 - AI agendid | Lisa mitme agendi orkestreerimine |

---

## 4. API moderniseerimine

### 4.1 Uuendatavad aegunud API mustrid

| Vana muster | Uus muster | Mõjutatud failid |
|-------------|------------|------------------|
| `openai.api_type = "azure"` | `AzureOpenAI()` klient | Mitmed skriptid kaustas `08-building-search-applications/` |
| `openai.ChatCompletion.create()` | `client.chat.completions.create()` | Mitmed märkmikud |
| `df.append()` (pandas) | `pd.concat()` | RAG märkmik |

### 4.2 Uued API omadused demonstratsiooniks

1. **Struktureeritud väljundid** (OpenAI)
   - JSON-režiim
   - Funktsioonikõned rangete skeemidega

2. **Visiooni võimalused**
   - Pildianalüüs GPT-4V abil
   - Mitmemodaalsed promptid

3. **Assistentide API**
   - Koodi interpreteerija
   - Faili otsing
   - Kohandatud tööriistad

---

## 5. Taristu täiustused

### 5.1 CI/CD täiustused

Praegused töövood tegelevad markdown valideerimisega. Soovitatavad täiendused:

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

### 5.2 Turvalisusskaneerimine

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

## 6. Arendajakogemuse täiustused

### 6.1 DevContainer täiustused

Uuenda faili `.devcontainer/devcontainer.json`:

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
- Jupyter märkmikud eelnevalt täidetud API võtmest (keskkonna kaudu)
- Gradio/Streamliti demo visuaalsetele õppijatele
- Interaktiivsed viktoriinid teadmiste hindamiseks

---

## 7. Mitmekeelne tugi

### 7.1 Praegune keelte katvus

| Tehnoloogia | Kaetud õppetunnid | Staatus |
|-------------|--------------------|---------|
| Python | Kõik | Täielik |
| TypeScript | 06-09, 11 | Osaline |
| JavaScript | 06-08, 11 | Osaline |
| .NET/C# | Mõned | Osaline |

### 7.2 Soovitatavad täiendused

1. **Go** - AI/ML tööriistades kasvav keel
2. **Rust** - Sooritusvõime kriitilised rakendused
3. **Java/Kotlin** - Ettevõtte rakendused

---

## 8. Töökindluse optimeerimine

### 8.1 Koodi tasandi optimeerimised

1. **Async/Await mustrid**
   - Lisa async näited partii töötlemiseks
   - Näita samaaegseid API päringuid

2. **Vahemällu salvestamise strateegiad**
   - Lisa embedingu vahemällu salvestamise näited
   - Näita vastuse vahemällu salvestamise mustreid

3. **Tokenite optimeerimine**
   - Lisa tiktoken kasutamise näited
   - Näita promptide kokkusurumise tehnikaid

### 8.2 Kuluoptimeerimise näited

Lisa näited, mis demonstreerivad:
- Mudeli valikut ülesande keerukuse järgi
- Prompti insenerlust tõhusa tokenikasutuse jaoks
- Partii töötlemist mahuoperatsioonideks

---

## 9. Juurdepääsetavus ja rahvusvahelistumine

### 9.1 Praegune tõlke staatuse ülevaade

| Keel | Staatus |
|-------|---------|
| Inglise | Täielik |
| Hiina (lihtsustatud) | Täielik |
| Jaapani | Täielik |
| Korea | Täielik |
| Hispaania | Osaline |
| Port (ugali) | Osaline |
| Türgi | Osaline |
| Poola | Osaline |

### 9.2 Juurdepääsetavuse täiustused

1. Lisa kõigile piltidele alt-tekst
2. Tagada koodinäidete õige süntaksitõstmine
3. Lisa videotõlked kogu videomaterjalile
4. Tagada värvikontrasti vastavus WCAG juhistele

---

## 10. Rakendamise prioriteet

### Faas 1: Kohene (1.–2. nädal)
- [x] Paranda kriitilised turvaprobleemid
- [x] Lisa koodi kvaliteedi konfiguratsioon
- [x] Loo jagatud utiliidid
- [x] Dokumenteeri turvalisuse juhised

### Faas 2: Lühiajaline (3.–4. nädal)
- [ ] Uuenda aegunud API mustreid
- [ ] Lisa tüübiviited kõigile Python failidele
- [ ] Lisa CI/CD töövood koodi kvaliteedi jaoks
- [ ] Loo turvalisuse skaneerimise töövoog

### Faas 3: Keskmine (2.–3. kuu)
- [ ] Lisa uus turvalisuse õppetund
- [ ] Lisa tootmiskeskkonna juurutamise õppetund
- [ ] Paranda DevContainer seadistust
- [ ] Lisa interaktiivsed demonstreerimised

### Faas 4: Pikaajaline (4. kuu+)
- [ ] Lisa täiustatud RAG õppetund
- [ ] Laienda keelte katvust
- [ ] Lisa põhjalik testide komplekt
- [ ] Loo sertifitseerimisprogramm

---

## Kokkuvõte

See teekaart pakub struktureeritud lähenemist Generative AI for Beginners kursuse täiustamiseks. Turvaaspektide käsitlemise, APIde moderniseerimise ja haridusliku sisu lisamise kaudu valmistab kursus üliõpilasi paremini ette tõeliste tehisintellekti rakenduste arendamiseks.

Küsimuste või panuste korral palun avage probleem GitHubi hoidlas.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Eksklusiivne vastutusest loobumine**:
See dokument on tõlgitud kasutades tehisintellekti tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgendused võivad sisaldada vigu või ebatäpsusi. Originaaldokument oma algkeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta ühegi arusaamatuse või valesti mõistmise eest, mis võib tekkida selle tõlke kasutamisest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->