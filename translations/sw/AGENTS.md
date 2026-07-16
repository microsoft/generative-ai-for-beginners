# AGENTS.md

## Muhtasari wa Mradi

Hifadhidata hii ina mtaala kamili wa masomo 21 unaofundisha misingi ya AI Inayotengeneza na maendeleo ya matumizi. Kozi hii imeundwa kwa wanaoanza na inashughulikia kila kitu kutoka dhana za msingi hadi kujenga programu za tayari kutumika.

**Teknolojia Muhimu:**
- Python 3.9+ na maktaba: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript na Node.js na maktaba: `openai` (Azure OpenAI kupitia kituo cha v1 + API ya Majibu), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Huduma ya Azure OpenAI, OpenAI API, na Microsoft Foundry Models (GitHub Models inaondoka mwisho wa Julai 2026)
- Daftari la Jupyter kwa kujifunza kwa mwingiliano
- Kontena za Maendeleo kwa mazingira thabiti ya maendeleo

**Muundo wa Hifadhidata:**
- Saraka za masomo 21 zenye namba (00-21) zenye README, mifano ya nambari, na kazi za nyumbani
- Utekelezaji mbalimbali: Python, TypeScript, na baadhi ya mifano ya .NET
- Saraka ya Tafsiri zenye matoleo ya lugha 40+
- Usanidi wa kati kupitia faili la `.env` (tumia `.env.copy` kama kiolezo)

## Amri za Kufunga

### Kusanidi Hifadhidata ya Kwanza

```bash
# Nakili hifadhidata
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Nakili kiolezo cha mazingira
cp .env.copy .env
# Hariri .env na funguo zako za API na vituo vya mwisho
```

### Kusanidi Mazingira ya Python

```bash
# Unda mazingira ya virtual
python3 -m venv venv

# Washa mazingira ya virtual
# Kwenye macOS/Linux:
source venv/bin/activate
# Kwenye Windows:
venv\Scripts\activate

# Sakinisha utegemezi
pip install -r requirements.txt
```

### Kusanidi Node.js/TypeScript

```bash
# Sakinisha utegemezi wa kiwango cha mzizi (kwa zana za nyaraka)
npm install

# Kwa mifano ya TypeScript ya somo binafsi, nenda kwenye somo maalum:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Kusanidi Kontena la Maendeleo (Inayopendekezwa)

Hifadhidata hii ina usanidi wa `.devcontainer` kwa GitHub Codespaces au VS Code Dev Containers:

1. Fungua hifadhidata kwenye GitHub Codespaces au VS Code na ugani wa Dev Containers
2. Kontena la Maendeleo litafanya moja kwa moja:
   - Sakinisha mahitaji ya Python kutoka `requirements.txt`
   - Endesha skripti ya baada ya kuunda (`.devcontainer/post-create.sh`)
   - Sanidi kernel ya Jupyter

## Mtiririko wa Maendeleo

### Mabadiliko ya Mazingira

Masomo yote yanayohitaji ufikiaji wa API yanatumia mabadiliko ya mazingira yaliyoainishwa kwenye `.env`:

- `OPENAI_API_KEY` - Kwa OpenAI API
- `AZURE_OPENAI_API_KEY` - Kwa Azure OpenAI ndani ya Microsoft Foundry (Huduma ya Azure OpenAI sasa ni sehemu ya Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL ya kituo cha Azure OpenAI (kituo cha rasilimali ya Foundry)
- `AZURE_OPENAI_DEPLOYMENT` - Jina la utekelezaji wa mfano wa mazungumzo
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Jina la utekelezaji wa mfano wa embeddings
- `AZURE_OPENAI_API_VERSION` - Toleo la API (chaguo-msingi: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Kwa mifano ya Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - Kituo cha Microsoft Foundry Models (katalogi ya mifano wa watoa huduma wengi)
- `AZURE_INFERENCE_CREDENTIAL` - API key ya Microsoft Foundry Models (inachukua nafasi ya `GITHUB_TOKEN` inayohamia)

### Kuendesha Mifano ya Python

```bash
# Elekea kwenye saraka ya somo
cd 06-text-generation-apps/python

# Endesha script ya Python
python aoai-app.py
```

### Kuendesha Mifano ya TypeScript

```bash
# Elekea kwenye saraka ya programu ya TypeScript
cd 06-text-generation-apps/typescript/recipe-app

# Jenge msimbo wa TypeScript
npm run build

# Endesha programu
npm start
```

### Kuendesha Daftari la Jupyter

```bash
# Anzisha Jupyter kwenye mzizi wa hifadhidata
jupyter notebook

# Au tumia VS Code na kiendelezi cha Jupyter
```

### Kufanya Kazi na Aina Tofauti za Masomo

- **Masomo ya "Jifunze"**: Angazia nyaraka za README.md na dhana
- **Masomo ya "Jenga"**: Yanajumuisha mifano ya nambari inayofanya kazi kwa Python na TypeScript
- Kila somo lina README.md yenye nadharia, maelezo ya nambari, na viungo vya maudhui ya video

## Mwongozo wa Mtindo wa Nambari

### Python

- Tumia `python-dotenv` kwa usimamizi wa mabadiliko ya mazingira
- Ingiza maktaba ya `openai` kwa mwingiliano na API
- Tumia `pylint` kwa ukaguzi wa nambari (mifano mingine ina `# pylint: disable=all` kwa urahisi)
- Fuata kanuni za jina za PEP 8
- Hifadhi nyaraka za API kwenye faili `.env`, kamwe siyo katika nambari

### TypeScript

- Tumia kifurushi cha `dotenv` kwa mabadiliko ya mazingira
- Usaidizi wa TypeScript kwenye `tsconfig.json` kwa kila programu
- Tumia kifurushi cha `openai` kwa Azure OpenAI (elekeza mteja kwa kituo cha `/openai/v1/` na piga `client.responses.create`); tumia `@azure-rest/ai-inference` kwa Microsoft Foundry Models
- Tumia `nodemon` kwa maendeleo na upakiaji otomatiki
- Jenga kabla ya kuendesha: `npm run build` kisha `npm start`

### Kanuni za Jumla

- Hifadhi mifano ya nambari kuwa rahisi na ya elimu
- Jumuisha maoni yanayofafanua dhana kuu
- Kila nambari ya somo iwe yenye uhuru na inaweza kuendeshwa
- Tumia majina thabiti: kiambatanishi `aoai-` kwa Azure OpenAI, `oai-` kwa OpenAI API, `githubmodels-` kwa Microsoft Foundry Models (kiambatanishi cha zamani kilichoachwa kutoka enzi ya GitHub Models)

## Mwongozo wa Nyaraka

### Mtindo wa Markdown

- URL zote lazima zifunikwe katika muundo wa `[text](../../url)` bila nafasi za ziada
- Viungo vya uhusiano lazima vitaanze na `./` au `../`
- Viungo vyote vya maeneo ya Microsoft lazima viwe na kitambulisho cha ufuatiliaji: `?WT.mc_id=academic-105485-koreyst`
- Epuka matumizi ya maeneo maalum ya nchi katika URL (epuka `/en-us/`)
- Picha zinahifadhiwa katika saraka ya `./images` zikibeba majina yenye maelezo
- Tumia herufi za Kiingereza, nambari, na alama za dash katika majina ya faili

### Msaada wa Tafsiri

- Hifadhidata inasaidia lugha 40+ kupitia GitHub Actions otomatiki
- Tafsiri zinahifadhiwa katika saraka ya `translations/`
- Usitumie tafsiri za sehemu
- Tafsiri za mashine hazikubaliki
- Picha zilizotafsiriwa zinahifadhiwa katika saraka ya `translated_images/`

## Upimaji na Uthibitishaji

### Ukaguzi Kabla ya Kuwasilisha

Hifadhidata hii inatumia GitHub Actions kwa uthibitishaji. Kabla ya kuwasilisha PRs:

1. **Kagua Viungo vya Markdown**:
   ```bash
   # Kazi ya validate-markdown.yml inakagua:
   # - Njia za kiraka zilizo kuvunjika
   # - IDs za ufuatiliaji zinazokosekana kwenye njia
   # - IDs za ufuatiliaji zinazokosekana kwenye URLs
   # - URLs zilizo na eneo la nchi
   # - URLs za nje zilizo kuvunjika
   ```

2. **Upimaji wa Mikono**:
   - Jaribu mifano ya Python: Washa venv na endesha skripti
   - Jaribu mifano ya TypeScript: `npm install`, `npm run build`, `npm start`
   - Thibitisha mabadiliko ya mazingira yamewekwa sawa
   - Kagua funguo za API zinafanya kazi na mifano ya nambari

3. **Mifano ya Nambari**:
   - Hakikisha nambari zote zinafanya kazi bila makosa
   - Jaribu na Azure OpenAI na OpenAI API inapowezekana
   - Thibitisha mifano inafanya kazi na Microsoft Foundry Models pale panapoungwa mkono

### Hakuna Majaribio ya Otomatiki

Hii ni hifadhidata ya kielimu inayolenga mafunzo na mifano. Hakuna majaribio ya kitengo au ya muunganisho ya kuendesha. Uthibitishaji ni hasa:
- Upimaji wa mikono wa mifano ya nambari
- GitHub Actions kwa uthibitishaji wa Markdown
- Ukaguzi wa jamii ya maudhui ya elimu

## Mwongozo wa OMBI LA VIONGOZI

### Kabla ya Kuwasilisha

1. Jaribu mabadiliko ya nambari kwa Python na TypeScript inapowezekana
2. Endesha uthibitishaji wa Markdown (unaanzishwa moja kwa moja kwenye PR)
3. Hakikisha kitambulisho cha ufuatiliaji kiko kwenye URL zote za Microsoft
4. Kagua viungo vya uhusiano viko halali
5. Thibitisha picha zimetajwa ipasavyo

### Muundo wa Kichwa cha PR

- Tumia vichwa vinavyoelezea: `[Somo 06] Rekebisha kosa la mfano wa Python` au `Sasisha README kwa somo 08`
- Rejelea nambari za maswala inapowezekana: `Inarekebisha #123`

### Maelezo ya PR

- Eleza kilichobadilishwa na kwa nini
- Weka viungo kwa maswala yanayohusiana
- Kwa mabadiliko ya nambari, taja mifano iliyojaribiwa
- Kwa PR za tafsiri, jumuisha faili zote kwa tafsiri kamili

### Vigezo vya Michango

- Saini Microsoft CLA (moja kwa moja kwenye PR ya kwanza)
- Fanya forksi ya hifadhidata kwa akaunti yako kabla ya kufanya mabadiliko
- PR moja kwa mabadiliko ya maana (usichanganye marekebisho yasiyohusiana)
- Weka PR kuwa na muktadha na ndogo inapowezekana

## Mitiririko ya Kazi ya Kawaida

### Kuongeza Mfano Mpya wa Nambari

1. Nenda kwenye saraka ya somo husika
2. Unda mfano katika saraka ndogo ya `python/` au `typescript/`
3. Fuata kanuni ya majina: `{provider}-{example-name}.{py|ts|js}`
4. Jaribu kwa kutumia nyaraka halali za API
5. Andika mabadiliko yoyote ya mabadiliko ya mazingira katika README ya somo

### Kusasisha Nyaraka

1. Hariri README.md katika saraka ya somo
2. Fuata mwongozo wa Markdown (kitambulisho cha ufuatiliaji, viungo vya uhusiano)
3. Sasisho la tafsiri linaendeshwa na GitHub Actions (usihariri kwa mikono)
4. Jaribu viungo vyote kuhakikisha vinafanana

### Kufanya Kazi na Kontena za Maendeleo

1. Hifadhidata ina `.devcontainer/devcontainer.json`
2. Skripti ya baada ya kuunda inasakinisha otomatiki mahitaji ya Python
3. Viendelezi vya Python na Jupyter vimesanidiwa kabla
4. Mazingira yanategemea `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Uenezaji na Kuchapisha

Hii ni hifadhidata ya kujifunza - hakuna mchakato wa uenezaji. Mtaala unatumika na:

1. **Hifadhidata ya GitHub**: Ufikiaji wa moja kwa moja wa nambari na nyaraka
2. **GitHub Codespaces**: Mazingira ya maendeleo ya haraka yenye usanidi tayari
3. **Microsoft Learn**: Maudhui yanaweza kusambazwa kwenye jukwaa rasmi la kujifunza
4. **docsify**: Tovuti ya nyaraka inajengwa kutoka Markdown (ona `docsifytopdf.js` na `package.json`)

### Kujenga Tovuti ya Nyaraka

```bash
# Tengeneza PDF kutoka kwa nyaraka (ikiwa inahitajika)
npm run convert
```

## Matatizo na Ufumbuzi

### Changamoto Zilizojitokeza Mara kwa Mara

**Makosa ya Kuwasilisha Python**:
- Hakikisha mazingira ya mtandao yamewashwa
- Endesha `pip install -r requirements.txt`
- Angalia toleo la Python likiwa 3.9+

**Makosa ya Ujenzi wa TypeScript**:
- Endesha `npm install` katika saraka ya programu husika
- Hakikisha toleo la Node.js linaendana
- Futa `node_modules` na zindua tena ikiwa inahitajika

**Makosa ya Uthibitishaji wa API**:
- Thibitisha faili la `.env` lipo na lina maadili sahihi
- Angalia funguo za API ni halali na hazijakwisha muda wake
- Hakikisha URL za vituo ni sahihi kwa mkoa wako

**Mabadiliko ya Mazingira Yanayokosekana**:
- Nakili `.env.copy` kwa `.env`
- Jaza maadili yote yanayohitajika kwa somo unalofanyia kazi
- Anzisha tena programu baada ya kusasisha `.env`

## Rasilimali Zaidi

- [Mwongozo wa Kusanidi Kozi](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Mwongozo wa Michango](./CONTRIBUTING.md)
- [Kanuni za Maadili](./CODE_OF_CONDUCT.md)
- [Sera ya Usalama](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Mkusanyiko wa Mifano ya Nambari ya Juu](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Maelezo Mahususi ya Mradi

- Hii ni **hifadhidata ya kielimu** inayolenga kujifunza, si nambari ya uzalishaji
- Mifano ni rahisi kwa makusudi na inalenga kufundisha dhana
- Ubora wa nambari umezingatia uwazi wa elimu
- Kila somo lina uhuru na linaweza kukamilishwa kwa kujitegemea
- Hifadhidata inaunga mkono watoa huduma wa API wengi: Azure OpenAI, OpenAI, Microsoft Foundry Models, na watoa huduma wa nje kama Foundry Local na Ollama
- Maudhui ni mengi ya lugha na yana mchakato wa tafsiri otomatiki
- Kuna jamii hai kwenye Discord kwa maswali na msaada

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->