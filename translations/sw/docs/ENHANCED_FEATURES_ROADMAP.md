# Ramani ya Sifa Zilizoboreshwa na Maboresho

Hati hii inaelezea maboresho na nyongeza zinazopendekezwa kwa kozi ya Generative AI kwa Waanzilganaji, kulingana na uhakiki wa kina wa msimbo na uchambuzi wa mbinu bora za sekta.

## Muhtasari wa Utendaji

Msimbo umechambuliwa kwa usalama, ubora wa msimbo, na ufanisi wa kielimu. Hati hii inatoa mapendekezo ya matengenezo ya haraka, maboresho ya muda mfupi, na nyongeza za baadaye.

---

## 1. Maboresho ya Usalama (Kipaumbele: Kikubwa)

### 1.1 Matengenezo ya Haraka (Yamekamilika)

| Tatizo | Faili Zilizohusishwa | Hali |
|-------|----------------|--------|
| SECRET_KEY iliyowekwa moja kwa moja msimboni | `05-advanced-prompts/python/aoai-solution.py` | Imekamilika |
| Ukosefu wa uhakiki wa mazingira | Faili nyingi za JS/TS | Imekamilika |
| Mito ya kazi zisizo salama | `11-integrating-with-function-calling/js-githubmodels/app.js` | Imekamilika |
| Kuachwa kwa mafaili wazi | `08-building-search-applications/scripts/` | Imekamilika |
| Ukosefu wa mipaka ya muda ya maombi | `09-building-image-applications/python/` | Imekamilika |

### 1.2 Sifa Zaidi za Usalama Zinazopendekezwa

1. **Mifano ya Kuzuia Msongamano wa Maombi (Rate Limiting)**
   - Ongeza msimbo wa mfano unaoonyesha jinsi ya kutekeleza kuzuia msongamano wa maombi kwa API
   - Onyesha mifumo ya kurejeleza kwa mkupuo (exponential backoff)

2. **Mzunguko wa Funguo za API**
   - Ongeza nyaraka kuhusu mbinu bora za mzunguko wa funguo za API
   - Jumuisha mifano ya matumizi ya Azure Key Vault au huduma zinazofanana

3. **Muunganiko wa Usalama wa Maudhui**
   - Ongeza mifano inayotumia Azure Content Safety API
   - Onyesha mifumo ya udhibiti wa ingizo/mazao

---

## 2. Maboresho ya Ubora wa Msimbo

### 2.1 Faili za Usanidi Zimeongezwa

| Faili | Kusudi |
|------|---------|
| `.eslintrc.json` | Sheria za linting za JavaScript/TypeScript |
| `.prettierrc` | Viwango vya usanifu wa msimbo |
| `pyproject.toml` | Usanidi wa zana za Python (Black, Ruff, mypy) |

### 2.2 Huduma Iliyoshirikiwa Imetengenezwa

Moduli mpya `shared/python/` yenye:
- `env_utils.py` - Usimamizi wa mabadiliko ya mazingira
- `input_validation.py` - Uhakiki na kusafisha ingizo
- `api_utils.py` - Vikombozi salama vya maombi ya API

### 2.3 Maboresho ya Msimbo Yanayopendekezwa

1. **Ufunuo wa Aina (Type Hints)**
   - Ongeza ufafanuzi wa aina kwa faili zote za Python
   - Washa hali kali ya TypeScript katika miradi yote ya TS

2. **Viwango vya Nyaraka**
   - Ongeza docstrings kwa kazi zote za Python
   - Ongeza maelezo ya JSDoc kwa kazi zote za JavaScript/TypeScript

3. **Mfumo wa Upimaji**
   - Ongeza usanidi wa pytest na mifano ya majaribio _(yamekamilika: usanidi wa pytest ndani ya `pyproject.toml`; mifano ya majaribio kwa huduma zilizoshirikiwa katika [`tests/`](../../../tests) inatekelezwa CI)_
   - Ongeza usanidi wa Jest kwa JavaScript/TypeScript

---

## 3. Maboresho ya Kielimu

### 3.1 Mada Mpya za Somo

1. **Usalama katika Programu za AI** (Somo Lililopendekezwa 22)
   - Mashambulizi ya kuchanganya maagizo na kinga
   - Usimamizi wa funguo za API
   - Udhibiti wa maudhui
   - Kuzuia msongamano na matumizi mabaya

2. **Usambazaji wa Matokeo (Production Deployment)** (Somo Lililopendekezwa 23)
   - Ufungashaji kwa kutumia Docker
   - Mijadala ya CI/CD
   - Ufuatiliaji na kurekodi kumbukumbu
   - Usimamizi wa gharama

3. **Mbinu Zaidi za RAG (Retrieval-Augmented Generation)** (Somo Lililopendekezwa 24)
   - Utafutaji mchanganyiko (maneno muhimu + maana)
   - Mikakati ya upangaji upya
   - RAG ya aina nyingi (multi-modal)
   - Mipimo ya tathmini

### 3.2 Maboresho ya Masomo Yanayopo

| Somo | Maboresho Yanayopendekezwa |
|--------|------------------------|
| 06 - Kizazi cha Maandishi | Ongeza mifano ya majibu ya moja kwa moja (streaming) |
| 07 - Programu za Mazungumzo (Chat) | Ongeza mifumo ya kumbukumbu za mazungumzo |
| 08 - Programu za Utafutaji | Ongeza kulinganisha za hifadhidata za vekta |
| 09 - Kizazi cha Picha | Ongeza mifano ya uhariri/varieti za picha |
| 11 - Kufanya Simu za Kazi (Function Calling) | Ongeza simu za kazi sambamba |
| 15 - RAG | Ongeza kulinganisha kwa mikakati ya kugawanya vipande |
| 17 - Maajenti wa AI | Ongeza usimamizi wa maajenti wengi |

---

## 4. Uboreshaji wa API

### 4.1 Mifumo ya API Iliyotelekezwa (Uhamisho Umekamilika)

Sampuli zote za Python na TypeScript za **chat** zimehamishwa kutoka API za Chat Completions kwenda **Responses API** (`client.responses.create(...)` → `response.output_text`).

| Mfiduo wa Kale | Mfiduo Mpya | Hali |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (chat) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | Imekamilika |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | Imekamilika |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | `openai` package `client.responses.create()` → `response.output_text` | Imekamilika |
| `df.append()` (pandas) | `pd.concat()` | Imekamilika |

> **Kumbuka:** Sampuli za Microsoft Foundry Models zinazotumia `azure-ai-inference` / `@azure-rest/ai-inference` SDK (`client.complete()`) zipo bado kwenye Model Inference API, ambayo haisaidii Responses API. `AzureOpenAI()` bado hutumika sehemu zinazofaa (kama embeddings na kizazi cha picha).

### 4.2 Sifa Mpya za API za Kuonyesha

1. **Matokeo Yaliyo Pangwa (Structured Outputs)** (OpenAI)
   - Hali ya JSON
   - Kufanya simu za kazi kwa sera kali za miundo

2. **Uwezo wa Maono**
   - Uchambuzi wa picha na GPT-4o (maono)
   - Maagizo ya aina nyingi (multi-modal)

3. **Zana Zilizojengwa ndani za Responses API** (zinazozirejesha API za Kale za Assistants)
   - Tafsiri ya msimbo
   - Utafutaji wa faili
   - Utafutaji wa wavuti na zana maalum

---

## 5. Maboresho ya Miundombinu

### 5.1 Maboresho ya CI/CD

Imetekelezwa katika [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): Kuangalia na kusanifu msimbo wa Python (Ruff + Black) ni **lazima** katika moduli ya huduma `shared/` inayodumishwa na hutekelezwa kwa ushauri katika mizani mingine ya kozi, pamoja na kuangalia ESLint ya tahadhari kwa JavaScript/TypeScript. Msingi wa mfano ulikuwa:

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

### 5.2 Uangalizi wa Usalama

Imetekelezwa katika [`.github/workflows/security.yml`](../../../.github/workflows/security.yml): Uchambuzi wa CodeQL kwa Python na JavaScript/TypeScript (kila mara baada ya kusukuma msimbo, ombi la kuvuta, na ratiba ya wiki) pamoja na ukaguzi wa utegemezi katika maombi ya kuvuta. Msingi wa mfano ulikuwa:

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

## 6. Maboresho ya Uzoefu wa Mwanaendelezi

### 6.1 Maboresho ya DevContainer

Imetekelezwa katika [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) na [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): kontena sasa ina Pylance, formatter wa Black, Ruff, ESLint, Prettier, na viendelezi vya Copilot, inaruhusu usanifu kwa kuokoa uliounganishwa na usanidi wa Black/Prettier wa repo, na kusanifu zana za maendeleo (`ruff`, `black`, `mypy`, `pytest`) ili [mtiririko wa kazi wa ubora wa msimbo](../../../.github/workflows/code-quality.yml) uweze kurudiwa kiasili. Picha ya msingi ya `mcr.microsoft.com/devcontainers/universal` tayari ina Python na Node, hivyo sifa za ziada hazihitajiki. Msingi wa mfano ulikuwa:

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

### 6.2 Uwanja wa Maingiliano (Interactive Playground)

Fikiria kuongeza:
- Daftari za Jupyter zilizo na funguo za API tayari zimejazwa (kupitia mazingira)
- Maonyesho ya Gradio/Streamlit kwa wanafunzi wanaoona
- Maswali ya maingiliano ya tathmini ya maarifa

---

## 7. Usaidizi wa Lugha Nyingi

### 7.1 Ufadhili wa Lugha wa Sasa

| Teknolojia | Masomo Yaliyofunikwa | Hali |
|------------|-----------------|--------|
| Python | Yote | Imekamilika |
| TypeScript | 06-09, 11 | Sehemu |
| JavaScript | 06-08, 11 | Sehemu |
| .NET/C# | Baadhi | Sehemu |

### 7.2 Ongezeko Zinazopendekezwa

1. **Go** - Inakua katika zana za AI/ML
2. **Rust** - Programu zenye utegemezi mkubwa kwa utendaji
3. **Java/Kotlin** - Programu za kampuni kubwa

---

## 8. Uboreshaji wa Utendaji

### 8.1 Maboresho ya Kiwango cha Msimbo

1. **Mifumo ya Async/Await**
   - Ongeza mifano ya async kwa usindikaji wa kundi
   - Onyesha simu za API zinazofanyika kwa wakati mmoja

2. **Mikakati ya Kuweka Akiba (Caching)**
   - Ongeza mifano ya kuweka akiba kwa embeddings
   - Oneshe mifumo ya kuweka akiba ya majibu

3. **Uboreshaji wa Tokeni**
   - Ongeza mifano ya matumizi ya tiktoken
   - Oneshe mbinu za kukandamiza maagizo (prompt compression)

### 8.2 Mifano ya Ufanisi wa Gharama

Ongeza mifano inayoonesha:
- Uteuzi wa mfano kulingana na ugumu wa kazi
- Uhandisi wa maagizo kwa ufanisi wa tokeni
- Usindikaji wa kundi kwa shughuli nyingi

---

## 9. Upatikanaji na Utafutaji Lugha za Kigeni

### 9.1 Hali ya Tafsiri ya Sasa

Tafsiri zote ni **kamili** na zimeundwa moja kwa moja na [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst), ambayo hutengeneza na kuweka toleo la kozi katika lugha 50+ linalolingana na chanzo cha Kiingereza. Yaliyotafsiriwa huwekwa chini ya `translations/` na picha za eneo chini ya `translated_images/`; orodha kamili ya lugha zinapatikana mwanzoni mwa README ya hifadhi.

| Kipengele | Hali |
|--------|--------|
| Ufadhili wa Tafsiri | Kamili — lugha 50+, masomo yote |
| Njia ya Tafsiri | Imekamilishwa kiotomatiki kupitia [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) |
| Inalingana na chanzo cha Kiingereza | Ndiyo — inaibuliwa kiotomatiki |

### 9.2 Maboresho ya Upatikanaji

1. Ongeza maandishi mbadala (alt text) kwa picha zote
2. Hakikisha sampuli za msimbo zina uonyeshaji sahihi wa sintaksia
3. Ongeza nakala za video kwa maudhui yote ya video
4. Hakikisha tofauti ya rangi inakidhi miongozo ya WCAG

---

## 10. Kipaumbele cha Utekelezaji

### Awamu 1: Mara Moja (Wiki 1-2)
- [x] Tengeneza matatizo muhimu ya usalama
- [x] Ongeza usanidi wa ubora wa msimbo
- [x] Unda huduma zilizoshirikiwa
- [x] Andika miongozo ya usalama

### Awamu 2: Muda Mfupi (Wiki 3-4)
- [x] Sasisha mifumo ya API iliyotelekezwa (Chat Completions → Responses API, Python + TypeScript)
- [ ] Ongeza ufafanuzi wa aina kwa faili zote za Python (imefanyika kwa moduli `shared/` inayodumishwa; sampuli za masomo ni rahisi)
- [x] Ongeza mikondo ya CI/CD kwa ubora wa msimbo
- [x] Unda mtiririko wa uangalizi wa usalama

### Awamu 3: Muda wa Kati (Mwezi 2-3)
- [ ] Ongeza somo jipya la usalama
- [ ] Ongeza somo la usambazaji wa matokeo
- [x] Boresha usanidi wa DevContainer
- [ ] Ongeza maonyesho ya maingiliano

### Awamu 4: Muda Mrefu (Mwezi 4+)
- [ ] Ongeza somo la RAG la hali ya juu
- [ ] Panua ufadhili wa lugha
- [ ] Ongeza mkusanyiko kamili wa majaribio
- [ ] Unda programu ya vyeti

---

## Hitimisho

Ramani hii inatoa njia iliyopangwa za kuboresha kozi ya Generative AI kwa Waanzilganaji. Kwa kushughulikia masuala ya usalama, kuiboresha API, na kuongeza maudhui ya kielimu, kozi itawaandalia wanafunzi vizuri zaidi maendeleo ya maombi ya AI halisi.

Kwa maswali au michango, tafadhali fungua suala kwenye hifadhi ya GitHub.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->