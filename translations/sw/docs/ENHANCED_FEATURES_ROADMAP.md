# Ramani ya Sifa Zilizoboreshwa na Maboresho

Hati hii inaelezea maboresho na maendeleo yanayopendekezwa kwa mtaala wa Generative AI kwa Waanzilishi, kulingana na uchunguzi wa kina wa msimbo na uchambuzi wa mbinu bora za sekta.

## Muhtasari Mkuu

Msimbo umechunguzwa kwa usalama, ubora wa msimbo, na ufanisi wa kielimu. Hati hii inatoa mapendekezo ya marekebisho ya haraka, maboresho ya muda mfupi, na maendeleo ya baadaye.

---

## 1. Maboresho ya Usalama (Kipaumbele: Muhimu Sana)

### 1.1 Marekebisho ya Haraka (Yamekamilika)

| Tatizo | Faili Zinazoathirika | Hali |
|--------|---------------------|-------|
| SECRET_KEY iliyowekwa moja kwa moja | `05-advanced-prompts/python/aoai-solution.py` | Imerekebishwa |
| Ukosefu wa uhakiki wa env | Faili nyingi za JS/TS | Imerekebishwa |
| Mitoaji wa kazi usiolindwa | `11-integrating-with-function-calling/js-githubmodels/app.js` | Imerekebishwa |
| Kutokwa kwa handle za faili | `08-building-search-applications/scripts/` | Imerekebishwa |
| Ukosefu wa wakati wa kuomba | `09-building-image-applications/python/` | Imerekebishwa |

### 1.2 Vipengele vya Usalama Vinavyopendekezwa Zaidi

1. **Mifano ya Kupunguza Kiwango cha Maombi**
   - Ongeza msimbo wa mfano unaoonesha jinsi ya kutekeleza kupunguza kiwango cha maombi kwa API
   - Onyesha mifumo ya kurudi nyuma kwa mng’ao (exponential backoff)

2. **Mzunguko wa Mfunguo za API**
   - Ongeza nyaraka juu ya mbinu bora za kuzungusha funguo za API
   - Jumuisha mifano ya kutumia Azure Key Vault au huduma zinazofanana

3. **Uunganishaji wa Usalama wa Maudhui**
   - Ongeza mifano inayotumia Azure Content Safety API
   - Onyesha mifumo ya urekebishaji wa ingizo/matokeo

---

## 2. Maboresho ya Ubora wa Msimbo

### 2.1 Faili za Usanidi Zimeongezwa

| Faili | Kusudi |
|-------|---------|
| `.eslintrc.json` | Sheria za linting za JavaScript/TypeScript |
| `.prettierrc` | Viwango vya muundo wa msimbo |
| `pyproject.toml` | Usanidi wa zana za Python (Black, Ruff, mypy) |

### 2.2 Vifaa Vilivyoshirikiwa Vimeundwa

Moduli mpya `shared/python/` pamoja na:
- `env_utils.py` - Usimamizi wa mabadiliko ya mazingira
- `input_validation.py` - Uhakiki na usafi wa ingizo
- `api_utils.py` - Weka mzunguko salama wa ombi za API

### 2.3 Maboresho ya Msimbo Yanayopendekezwa

1. **Mwanga wa Aina za Data**
   - Ongeza mwanga wa aina zote za faili za Python
   - Washa hali kali ya TypeScript katika miradi yote ya TS

2. **Viwango vya Nyaraka**
   - Ongeza maelezo ya kazi za Python zote
   - Ongeza maoni ya JSDoc kwenye kazi zote za JavaScript/TypeScript

3. **Mazingira ya Upimaji**
   - Ongeza usanidi wa pytest na mifano ya vipimo
   - Ongeza usanidi wa Jest kwa JavaScript/TypeScript

---

## 3. Maboresho ya Kielimu

### 3.1 Mada Mpya za Masomo

1. **Usalama katika Programu za AI** (Somo lililopendekezwa 22)
   - Mashambulizi ya sindano ya prompt na kinga
   - Usimamizi wa funguo za API
   - Udhibiti wa maudhui
   - Kupunguza kiwango cha maombi na kuzuia matumizi mabaya

2. **Uwekaji Kiwanda wa Uzalishaji** (Somo lililopendekezwa 23)
   - Ufungashaji kwa Docker
   - Mifumo ya CI/CD
   - Ufuatiliaji na kuandika kumbukumbu
   - Usimamizi wa gharama

3. **Mbinu Zaidi za RAG** (Somo lililopendekezwa 24)
   - Utafutaji mchanganyiko (maneno + maana)
   - Mikakati ya upangaji upya
   - RAG za njia nyingi
   - Vipimo vya tathmini

### 3.2 Maboresho kwa Masomo Yanayopo

| Somo | Maboresho Yanayopendekezwa |
|-------|----------------------------|
| 06 - Uundaji wa Maandishi | Ongeza mifano ya majibu ya mtiririko |
| 07 - Programu za Chat | Ongeza mifumo ya kumbukumbu ya mazungumzo |
| 08 - Programu za Utafutaji | Ongeza kulinganisha hifadhidata za vector |
| 09 - Uundaji wa Picha | Ongeza mifano ya uhariri/mbadala wa picha |
| 11 - Kuitisha Kazi | Ongeza kuitisha kazi sambamba |
| 15 - RAG | Ongeza kulinganisha mkakati wa kugawa vipande |
| 17 - Wakala wa AI | Ongeza uratibu wa wakala wengi |

---

## 4. Uboreshaji wa API

### 4.1 Mifumo ya API Iliyoachwa Kutumika Ibadilishwe

| Mfanano wa Kale | Mfanano Mpya | Faili Zinazoathirika |
|-----------------|--------------|---------------------|
| `openai.api_type = "azure"` | `AzureOpenAI()` mteja | Script nyingi katika `08-building-search-applications/` |
| `openai.ChatCompletion.create()` | `client.chat.completions.create()` | Notibuki nyingi |
| `df.append()` (pandas) | `pd.concat()` | Notibuki la RAG |

### 4.2 Vipengele Vipya vya API vya Kuonesha

1. **Matokeo Yenye Muundo** (OpenAI)
   - Hali ya JSON
   - Kuitisha kazi kwa kanuni kali

2. **Uwezo wa Maono**
   - Uchambuzi wa picha na GPT-4V
   - Prompt za njia nyingi

3. **API ya Msaidizi**
   - Mfasiri wa msimbo
   - Utafutaji wa faili
   - Zana maalum

---

## 5. Maboresho ya Miundombinu

### 5.1 Maboresho ya CI/CD

Mtiririko wa kazi wa sasa unashughulikia uthibitishaji wa markdown. Ongezo zinazopendekezwa:

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

### 5.2 Usafishaji wa Usalama

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

## 6. Maboresho ya Uzoefu wa Mtengenezaji

### 6.1 Maboresho ya DevContainer

Sasisha `.devcontainer/devcontainer.json`:

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

### 6.2 Sehemu ya Mageuzi ya Kuingiliana

Fikiria kuongeza:
- Notibuki za Jupyter zilizo na funguo za API zilizowekwa (kupitia mazingira)
- Maonyesho ya Gradio/Streamlit kwa wanafunzi wa kuona
- Maswali ya kuhisabu maarifa kwa kuingiliana

---

## 7. Msaada wa Lugha Mbalimbali

### 7.1 Ufungaji wa Lugha Ulivyo Sasa

| Teknolojia | Masomo Yaliyofunikwa | Hali |
|------------|---------------------|------|
| Python | Yote | Kamili |
| TypeScript | 06-09, 11 | Sehemu |
| JavaScript | 06-08, 11 | Sehemu |
| .NET/C# | Baadhi | Sehemu |

### 7.2 Ongezo Zinazopendekezwa

1. **Go** - Inaongezeka katika zana za AI/ML
2. **Rust** - Programu muhimu kwa utendaji
3. **Java/Kotlin** - Programu za biashara

---

## 8. Maboresho ya Utendaji

### 8.1 Maboresho ya Ngazi ya Msimbo

1. **Mifumo ya Async/Await**
   - Ongeza mifano ya async kwa usindikaji wa kundi
   - Onyesha kuitwa kwa API kwa wakati mmoja

2. **Mikakati ya Kuweka Kache**
   - Ongeza mifano ya kuweka kache embeddings
   - Onyesha mifumo ya kuweka kache majibu

3. **Uboreshaji wa Tokeni**
   - Ongeza mifano ya matumizi ya tiktoken
   - Onyesha mbinu za kusindika prompt

### 8.2 Mifano ya Kuokoa Gharama

Ongeza mifano inayothibitisha:
- Uchaguzi wa modeli kulingana na ugumu wa kazi
- Usanifu wa prompt kwa ufanisi wa tokeni
- Usindikaji wa kundi kwa shughuli kubwa

---

## 9. Ufikikaji na Utafsiri wa Kimataifa

### 9.1 Hali ya Utafsiri Sasa

| Lugha | Hali |
|--------|-------|
| Kiingereza | Kamili |
| Kichina (Rahisi) | Kamili |
| Kijapani | Kamili |
| Kikorea | Kamili |
| Kihispania | Sehemu |
| Kireno | Sehemu |
| Kituruki | Sehemu |
| Kipolishi | Sehemu |

### 9.2 Maboresho ya Ufikikaji

1. Ongeza maandishi ya alt kwa picha zote
2. Hakikisha mifano ya msimbo ina muonekano sahihi wa msimbo
3. Ongeza maandishi ya video kwa maudhui yote ya video
4. Hakikisha tofauti ya rangi inakidhi miongozo ya WCAG

---

## 10. Kipaumbele cha Utekelezaji

### Awamu ya 1: Mara Moja (Wiki 1-2)
- [x] Rekebisha masuala makubwa ya usalama
- [x] Ongeza usanidi wa ubora wa msimbo
- [x] Unda vifaa vilivyoshirikiwa
- [x] Andika miongozo ya usalama

### Awamu ya 2: Muda Mfupi (Wiki 3-4)
- [ ] Sasisha mifumo ya API iliyotumiwa
- [ ] Ongeza mwanga wa aina kwa faili zote za Python
- [ ] Ongeza mtiririko wa CI/CD kwa ubora wa msimbo
- [ ] Unda mtiririko wa usafishaji wa usalama

### Awamu ya 3: Muda wa Kati (Miezi 2-3)
- [ ] Ongeza somo jipya la usalama
- [ ] Ongeza somo la uwekaji kiwanda
- [ ] Boreshaji wa usanidi wa DevContainer
- [ ] Ongeza maonyesho ya kuingiliana

### Awamu ya 4: Muda Mrefu (Miezi 4+)
- [ ] Ongeza somo la RAG la hali ya juu
- [ ] Panua ufunikaji wa lugha
- [ ] Ongeza kifurushi kamili cha vipimo
- [ ] Unda mpango wa vyeti

---

## Hitimisho

Ramani hii inatoa njia iliyoainishwa ya kuboresha mtaala wa Generative AI kwa Waanzilishi. Kwa kushughulikia masuala ya usalama, kuboresha APIs, na kuongeza maudhui ya kielimu, kozi itawaandaa wanafunzi kwa maendeleo ya kweli ya programu za AI.

Kwa maswali au michango, tafadhali fungua tatizo kwenye hazina ya GitHub.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kiarifu cha Kukataa**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kufikia usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au dosari. Hati asili kwa lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatuna wajibu wowote kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->