<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:08:48+00:00",
  "source_file": "AGENTS.md",
  "language_code": "sw"
}
-->
# AGENTS.md

## Muhtasari wa Mradi

Hifadhi hii ina mtaala wa masomo 21 unaofundisha misingi ya AI ya kizazi na maendeleo ya programu. Kozi imeundwa kwa wanaoanza na inashughulikia kila kitu kuanzia dhana za msingi hadi kujenga programu zinazofaa kwa uzalishaji.

**Teknolojia Muhimu:**
- Python 3.9+ na maktaba: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript na Node.js na maktaba: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Huduma ya Azure OpenAI, OpenAI API, na GitHub Models
- Jupyter Notebooks kwa kujifunza kwa maingiliano
- Dev Containers kwa mazingira thabiti ya maendeleo

**Muundo wa Hifadhi:**
- Saraka za masomo 21 zilizo na namba (00-21) zenye READMEs, mifano ya msimbo, na kazi za nyumbani
- Utekelezaji mbalimbali: Python, TypeScript, na wakati mwingine mifano ya .NET
- Saraka ya tafsiri yenye matoleo ya lugha zaidi ya 40
- Usanidi wa kati kupitia faili `.env` (tumia `.env.copy` kama kiolezo)

## Amri za Usanidi

### Usanidi wa Awali wa Hifadhi

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Usanidi wa Mazingira ya Python

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

### Usanidi wa Node.js/TypeScript

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Usanidi wa Dev Container (Inapendekezwa)

Hifadhi hii inajumuisha usanidi wa `.devcontainer` kwa GitHub Codespaces au VS Code Dev Containers:

1. Fungua hifadhi katika GitHub Codespaces au VS Code na kiendelezi cha Dev Containers
2. Dev Container itaweka moja kwa moja:
   - Maktaba za Python kutoka `requirements.txt`
   - Kificho cha baada ya kuunda (`.devcontainer/post-create.sh`)
   - Usanidi wa kernel ya Jupyter

## Mtiririko wa Kazi wa Maendeleo

### Vigezo vya Mazingira

Masomo yote yanayohitaji ufikiaji wa API hutumia vigezo vya mazingira vilivyofafanuliwa katika `.env`:

- `OPENAI_API_KEY` - Kwa OpenAI API
- `AZURE_OPENAI_API_KEY` - Kwa Huduma ya Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL ya mwisho ya Azure OpenAI
- `AZURE_OPENAI_DEPLOYMENT` - Jina la utekelezaji wa mfano wa kukamilisha mazungumzo
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Jina la utekelezaji wa mfano wa embeddings
- `AZURE_OPENAI_API_VERSION` - Toleo la API (chaguo-msingi: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Kwa mifano ya Hugging Face
- `GITHUB_TOKEN` - Kwa GitHub Models

### Kuendesha Mifano ya Python

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### Kuendesha Mifano ya TypeScript

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Kuendesha Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Kufanya Kazi na Aina Tofauti za Masomo

- **Masomo ya "Learn"**: Yanazingatia README.md na dhana
- **Masomo ya "Build"**: Yanajumuisha mifano ya msimbo inayofanya kazi katika Python na TypeScript
- Kila somo lina README.md yenye nadharia, maelezo ya msimbo, na viungo vya maudhui ya video

## Miongozo ya Mtindo wa Msimbo

### Python

- Tumia `python-dotenv` kwa usimamizi wa vigezo vya mazingira
- Ingiza maktaba ya `openai` kwa mwingiliano wa API
- Tumia `pylint` kwa ukaguzi wa msimbo (baadhi ya mifano inajumuisha `# pylint: disable=all` kwa urahisi)
- Fuata kanuni za PEP 8 za majina
- Hifadhi hati za API katika faili `.env`, kamwe si katika msimbo

### TypeScript

- Tumia kifurushi cha `dotenv` kwa vigezo vya mazingira
- Usanidi wa TypeScript katika `tsconfig.json` kwa kila programu
- Tumia `@azure/openai` au `@azure-rest/ai-inference` kwa huduma za Azure
- Tumia `nodemon` kwa maendeleo na upakiaji upya kiotomatiki
- Jenga kabla ya kuendesha: `npm run build` kisha `npm start`

### Miongozo ya Jumla

- Weka mifano ya msimbo rahisi na ya kielimu
- Jumuisha maelezo yanayofafanua dhana muhimu
- Msimbo wa kila somo unapaswa kuwa wa kujitegemea na unaoweza kuendeshwa
- Tumia majina thabiti: kiambishi awali `aoai-` kwa Azure OpenAI, `oai-` kwa OpenAI API, `githubmodels-` kwa GitHub Models

## Miongozo ya Nyaraka

### Mtindo wa Markdown

- URL zote lazima ziwe katika muundo wa `[maandishi](../../url)` bila nafasi za ziada
- Viungo vya jamaa lazima vianze na `./` au `../`
- Viungo vyote vya kikoa cha Microsoft lazima vijumuishe ID ya ufuatiliaji: `?WT.mc_id=academic-105485-koreyst`
- Hakuna maeneo maalum ya nchi katika URL (epuka `/en-us/`)
- Picha zihifadhiwe katika folda ya `./images` na majina yanayoelezea
- Tumia herufi za Kiingereza, namba, na dashes katika majina ya faili

### Msaada wa Tafsiri

- Hifadhi inasaidia lugha zaidi ya 40 kupitia GitHub Actions za kiotomatiki
- Tafsiri zinahifadhiwa katika saraka ya `translations/`
- Usitumie tafsiri za sehemu
- Tafsiri za mashine hazikubaliki
- Picha zilizotafsiriwa zinahifadhiwa katika saraka ya `translated_images/`

## Upimaji na Uthibitishaji

### Ukaguzi Kabla ya Kuwasilisha

Hifadhi hii inatumia GitHub Actions kwa uthibitishaji. Kabla ya kuwasilisha PRs:

1. **Angalia Viungo vya Markdown**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Upimaji wa Mwongozo**:
   - Jaribu mifano ya Python: Washa venv na endesha hati
   - Jaribu mifano ya TypeScript: `npm install`, `npm run build`, `npm start`
   - Hakikisha vigezo vya mazingira vimewekwa vizuri
   - Angalia kwamba funguo za API zinafanya kazi na mifano ya msimbo

3. **Mifano ya Msimbo**:
   - Hakikisha msimbo wote unaendeshwa bila makosa
   - Jaribu na Azure OpenAI na OpenAI API inapowezekana
   - Thibitisha mifano inafanya kazi na GitHub Models pale inaposaidiwa

### Hakuna Upimaji wa Kiotomatiki

Hii ni hifadhi ya kielimu inayolenga mafunzo na mifano. Hakuna upimaji wa vitengo au upimaji wa muunganisho wa kuendesha. Uthibitishaji unategemea:
- Upimaji wa mwongozo wa mifano ya msimbo
- GitHub Actions kwa uthibitishaji wa Markdown
- Mapitio ya jamii ya maudhui ya kielimu

## Miongozo ya Pull Request

### Kabla ya Kuwasilisha

1. Jaribu mabadiliko ya msimbo katika Python na TypeScript inapowezekana
2. Endesha uthibitishaji wa Markdown (unaendeshwa kiotomatiki kwenye PR)
3. Hakikisha ID za ufuatiliaji zipo kwenye URL zote za Microsoft
4. Angalia kwamba viungo vya jamaa ni sahihi
5. Thibitisha picha zinarejelewa vizuri

### Muundo wa Kichwa cha PR

- Tumia vichwa vinavyoelezea: `[Lesson 06] Fix Python example typo` au `Update README for lesson 08`
- Rejelea namba za masuala inapowezekana: `Fixes #123`

### Maelezo ya PR

- Eleza kilichobadilishwa na kwa nini
- Unganisha na masuala yanayohusiana
- Kwa mabadiliko ya msimbo, eleza ni mifano gani iliyojaribiwa
- Kwa PR za tafsiri, jumuisha faili zote kwa tafsiri kamili

### Mahitaji ya Mchango

- Saini Microsoft CLA (kiotomatiki kwenye PR ya kwanza)
- Fork hifadhi kwenye akaunti yako kabla ya kufanya mabadiliko
- PR moja kwa mabadiliko ya kimantiki (usichanganye marekebisho yasiyohusiana)
- Weka PRs zikiwa zinalenga na ndogo inapowezekana

## Mtiririko wa Kazi wa Kawaida

### Kuongeza Mfano Mpya wa Msimbo

1. Nenda kwenye saraka ya somo husika
2. Unda mfano katika saraka ya `python/` au `typescript/`
3. Fuata muundo wa majina: `{provider}-{example-name}.{py|ts|js}`
4. Jaribu na hati halisi za API
5. Andika nyaraka za vigezo vipya vya mazingira katika README ya somo

### Kusasisha Nyaraka

1. Hariri README.md katika saraka ya somo
2. Fuata miongozo ya Markdown (ID za ufuatiliaji, viungo vya jamaa)
3. Sasisha tafsiri zinashughulikiwa na GitHub Actions (usihariri mwenyewe)
4. Jaribu viungo vyote ni sahihi

### Kufanya Kazi na Dev Containers

1. Hifadhi inajumuisha `.devcontainer/devcontainer.json`
2. Kificho cha baada ya kuunda huweka maktaba za Python kiotomatiki
3. Viendelezi vya Python na Jupyter vimewekwa awali
4. Mazingira yanategemea `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Uchapishaji na Usambazaji

Hii ni hifadhi ya kujifunza - hakuna mchakato wa uchapishaji. Mtaala unatumika kupitia:

1. **Hifadhi ya GitHub**: Ufikiaji wa moja kwa moja wa msimbo na nyaraka
2. **GitHub Codespaces**: Mazingira ya maendeleo ya papo hapo na usanidi uliowekwa awali
3. **Microsoft Learn**: Maudhui yanaweza kusambazwa kwenye jukwaa rasmi la kujifunza
4. **docsify**: Tovuti ya nyaraka iliyojengwa kutoka Markdown (angalia `docsifytopdf.js` na `package.json`)

### Kujenga Tovuti ya Nyaraka

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Utatuzi wa Matatizo

### Masuala ya Kawaida

**Makosa ya Uingizaji wa Python**:
- Hakikisha mazingira ya kawaida yamewashwa
- Endesha `pip install -r requirements.txt`
- Angalia toleo la Python ni 3.9+

**Makosa ya Ujenzi wa TypeScript**:
- Endesha `npm install` katika saraka ya programu husika
- Angalia toleo la Node.js linapatana
- Futa `node_modules` na usakinishe tena ikiwa inahitajika

**Makosa ya Uthibitishaji wa API**:
- Thibitisha faili `.env` ipo na ina maadili sahihi
- Angalia funguo za API ni halali na hazijaisha muda wake
- Hakikisha URL za mwisho ni sahihi kwa eneo lako

**Vigezo vya Mazingira Vilivyokosekana**:
- Nakili `.env.copy` hadi `.env`
- Jaza maadili yote yanayohitajika kwa somo unalofanya kazi
- Anzisha tena programu yako baada ya kusasisha `.env`

## Rasilimali za Ziada

- [Mwongozo wa Usanidi wa Kozi](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Miongozo ya Kuchangia](./CONTRIBUTING.md)
- [Kanuni za Maadili](./CODE_OF_CONDUCT.md)
- [Sera ya Usalama](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Mkusanyiko wa Mifano ya Msimbo wa Juu](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Vidokezo Maalum vya Mradi

- Hii ni **hifadhi ya kielimu** inayolenga kujifunza, si msimbo wa uzalishaji
- Mifano imeundwa kuwa rahisi na inayolenga kufundisha dhana
- Ubora wa msimbo unalinganishwa na uwazi wa kielimu
- Kila somo ni la kujitegemea na linaweza kukamilishwa kivyake
- Hifadhi inasaidia watoa huduma mbalimbali wa API: Azure OpenAI, OpenAI, na GitHub Models
- Maudhui ni ya lugha nyingi na mtiririko wa tafsiri za kiotomatiki
- Jamii inayofanya kazi kwenye Discord kwa maswali na msaada

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.