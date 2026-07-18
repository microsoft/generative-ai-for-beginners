# AGENTS.md

## Muhtasari wa Mradi

Hifadhi hii ina mitaala kamili ya masomo 21 inayofundisha misingi ya AI za Uzalishaji na uendelezaji wa matumizi. Kozi hii imetengenezwa kwa wanaoanza na inashughulikia kila kitu kuanzia dhana za msingi hadi kujenga matumizi yanayoweza kutumika.

**Teknolojia Muhimu:**
- Python 3.9+ na maktaba: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript na Node.js na maktaba: `openai` (Azure OpenAI kupitia sehemu ya v1 + API ya Majibu), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Huduma ya Azure OpenAI, API ya OpenAI, na Microsoft Foundry Models (GitHub Models itakoma mwishoni mwa Julai 2026)
- Daftari la Jupyter kwa kujifunza kwa mwingiliano
- Dev Containers kwa mazingira ya maendeleo thabiti

**Muundo wa Hifadhi:**
- Taka la masomo yaliyo na nambari 21 (00-21) lina README, mifano ya msimbo, na kazi za nyumbani
- Utekelezaji mwingi: mifano ya Python, TypeScript, na wakati mwingine .NET
- Saraka ya Tafsiri na toleo la lugha zaidi ya 40
- Mipangilio midogo kupitia faili `.env` (tumieni `.env.copy` kama kiolezo)

## Amri za Kusanidi

### Kusanidi Hifadhi ya Awali

```bash
# Nakili hifadhi
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
# Sakinisha utegemezi wa ngazi ya mzizi (kwa zana za nyaraka)
npm install

# Kwa mifano ya TypeScript ya somo binafsi, nenda kwenye somo maalum:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Kusanidi Dev Container (Inapendekezwa)

Hifadhi ina usanidi wa `.devcontainer` kwa GitHub Codespaces au VS Code Dev Containers:

1. Fungua hifadhi katika GitHub Codespaces au VS Code na kiendelezi cha Dev Containers
2. Dev Container ita:
   - Sajili tegemezi za Python kutoka `requirements.txt`
   - Endesha script ya baadaye-uundaji (`.devcontainer/post-create.sh`)
   - Sanidi kernel ya Jupyter

## Mtiririko wa Maendeleo

### Mabadiliko ya Mazingira

Masomo yote yanayohitaji upatikanaji wa API hutumia mabadiliko ya mazingira yaliyobainishwa katika `.env`:

- `OPENAI_API_KEY` - Kwa API ya OpenAI
- `AZURE_OPENAI_API_KEY` - Kwa Azure OpenAI katika Microsoft Foundry (Huduma ya Azure OpenAI sasa ni sehemu ya Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL ya sehemu ya mwisho ya Azure OpenAI (sehemu ya rasilimali Foundry)
- `AZURE_OPENAI_DEPLOYMENT` - Jina la usambazaji wa mfano wa mazungumzo (chaguo-msingi cha kozi: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Jina la usambazaji wa mfano wa embeddings (chaguo-msingi cha kozi: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - Toleo la API (chaguo-msingi: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Kwa mifano ya Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - Sehemu ya Microsoft Foundry Models (katalogi ya mfano wa wanatoa wengi)
- `AZURE_INFERENCE_CREDENTIAL` - Kitufe cha API cha Microsoft Foundry Models (kinachochukua nafasi ya `GITHUB_TOKEN` inayostaafu)
- `AZURE_INFERENCE_CHAT_MODEL` - Mfano usiotumia uamuzi (km. `Llama-3.3-70B-Instruct`) unaotumika katika mifano ya `temperature`, kwani mifano ya uamuzi haiji na udhibiti wa sampuli

### Kanuni za Mfano (muhimu)

- **Mfano wa mazungumzo wa chaguo-msingi ni `gpt-5-mini`** - mfano wa sasa, usioachwa kwa ajili ya **uamuzi**. Kuanzia 2026 mifano ya awali ya "mini" yenye uwezo wa joto (`gpt-4o-mini`, `gpt-4.1-mini`) zinaondolewa, hivyo mitaala huweka viwango vya familia ya GPT-5.
- **Mifano ya uamuzi hailali `temperature` na `top_p`**, na hutumia `max_output_tokens` (API ya Majibu) / `max_completion_tokens` (ukamilishaji wa mazungumzo) badala ya `max_tokens`. Usiongeze `temperature`/`top_p`/`max_tokens` kwa mifano inayopita kwenye `gpt-5-mini`.
- **Ili kuonyesha `temperature`**, mifano hutumia mfano wa **Llama** (`Llama-3.3-70B-Instruct`) kupitia sehemu ya Microsoft Foundry Models (`AZURE_INFERENCE_CHAT_MODEL`). Elekeza mifano ya uamuzi kwa uhandisi wa maelekezo + udhibiti wa uamuzi badala ya viashiria vya sampuli.
- **Urekebishaji (somo la 18)** unaongeza `gpt-4.1-mini`: GPT-5 inaunga mkono tu urekebishaji wa kuimarisha (RFT), si urekebishaji wa chini ya usimamizi (SFT) unaooneshwa hapo.
- Masomo 20 (Mistral) na 21 (Meta) bado yanatumia `temperature`/`max_tokens` kwa sababu yanawalenga mifano ya Mistral/Llama, ambayo inaunga mkono hayo.

### Kuendesha Mifano ya Python

```bash
# Naviga kwenye saraka ya somo
cd 06-text-generation-apps/python

# Endesha script ya Python
python aoai-app.py
```

### Kuendesha Mifano ya TypeScript

```bash
# Elekea kwenye saraka ya programu ya TypeScript
cd 06-text-generation-apps/typescript/recipe-app

# Jenga msimbo wa TypeScript
npm run build

# Endesha programu
npm start
```

### Kuendesha Daftari la Jupyter

```bash
# Anza Jupyter katika mzizi wa hifadhidata
jupyter notebook

# Au tumia VS Code na programu-jalizi ya Jupyter
```

### Kufanya kazi na Aina Tofauti za Masomo

- **Masomo ya "Jifunze"**: Lenga kwenye nyaraka za README.md na dhana
- **Masomo ya "Jenga"**: Yanajumuisha mifano ya kazi kwa Python na TypeScript
- Kila somo lina README.md yenye nadharia, maelezo ya msimbo, na viungo vya maudhui ya video

## Miongozo ya Mtindo wa Msimbo

### Python

- Tumia `python-dotenv` kwa usimamizi wa mabadiliko ya mazingira
- Ingiza maktaba `openai` kwa mwingiliano wa API
- Tumia `pylint` kwa ukaguzi wa msimbo (mifano mingine ina `# pylint: disable=all` kwa urahisi)
- Fuata kanuni za uandishi wa PEP 8
- Hifadhi taarifa za API katika faili `.env`, kamwe si msimbos

### TypeScript

- Tumia kifurushi `dotenv` kwa mabadiliko ya mazingira
- Usanidi wa TypeScript katika `tsconfig.json` kwa kila app
- Tumia kifurushi `openai` kwa Azure OpenAI (elekeza mteja kwa sehemu ya mwisho `/openai/v1/` na piga `client.responses.create`); tumia `@azure-rest/ai-inference` kwa Microsoft Foundry Models
- Tumia `nodemon` kwa maendeleo na upakiaji wa mara kwa mara
- Tafuta kabla ya kuendesha: `npm run build` kisha `npm start`

### Kanuni za Jumla

- Fanya mifano ya msimbo iwe rahisi na elimu
- Jumuisha maelezo ya maoni yanayofafanua dhana kuu
- Msimbo wa kila somo unapaswa kujitegemea na kuweza kuendesha
- Tumia majina thabiti: kiambatanisho `aoai-` kwa Azure OpenAI, `oai-` kwa API ya OpenAI, `githubmodels-` kwa Microsoft Foundry Models (kiambatanisho cha zamani kinachohifadhiwa kutoka enzi za GitHub Models)

## Miongozo ya Nyaraka

### Mtindo wa Markdown

- URL zote lazima ziwe zimefungwa ndani ya muundo wa `[text](../../url)` bila nafasi za ziada
- Viungo vya ndani lazima vianze na `./` au `../`
- Viungo vyote kwa maeneo ya Microsoft lazima viwe na kitambulisho cha ufuatiliaji: `?WT.mc_id=academic-105485-koreyst`
- Epuka maeneo ya lugha maalum ya nchi katika URL (epuka `/en-us/`)
- Picha zimehifadhiwa katika saraka `./images` zikiwa na majina ya kuelezea
- Tumia herufi za Kiingereza, nambari, na dashini katika majina ya faili

### Msaada wa Tafsiri

- Hifadhi inaunga mkono lugha zaidi ya 40 kupitia GitHub Actions moja kwa moja
- Tafsiri zimehifadhiwa katika saraka `translations/`
- Usitume tafsiri zisizokamilika
- Tafsiri za mashine hazikubaliwa
- Picha zilizotafsiriwa zinahifadhiwa katika saraka `translated_images/`

## Upimaji na Uthibitishaji

### Ukaguzi wa Kabla ya Kuwasilisha

Hifadhi hii inatumia GitHub Actions kwa uthibitishaji. Kabla ya kuwasilisha PR:

1. **Kagua Viungo vya Markdown**:
   ```bash
   # Kazi ya validate-markdown.yml inakagua:
   # - Njia za uhusiano zilizovunjika
   # - Vitambulisho vya ufuatiliaji vinavyokosekana kwenye njia
   # - Vitambulisho vya ufuatiliaji vinavyokosekana kwenye URL
   # - URL zilizo na eneo la nchi
   # - URL za nje zilizovunjika
   ```

2. **Upimaji wa Mikono**:
   - Jaribu mifano ya Python: Weka venv na endesha skripti
   - Jaribu mifano ya TypeScript: `npm install`, `npm run build`, `npm start`
   - Hakikisha mabadiliko ya mazingira yamepangwa ipasavyo
   - Angalia kama funguo za API zinafanya kazi na mifano ya msimbo

3. **Mifano ya Msimbo**:
   - Hakikisha msimbo wote unaendesha bila makosa
   - Jaribu na Azure OpenAI na API ya OpenAI inapobidi
   - Hakikisha mifano inafanya kazi na Microsoft Foundry Models pale inapoungwa mkono

### Hakuna Majaribio ya Moja kwa Moja

Hii ni hifadhi ya elimu inayojikita kwenye mafunzo na mifano. Hakuna majaribio ya kitengo au utekelezaji wa pamoja wa kuendesha. Uthibitishaji ni hasa:
- Upimaji wa mikono wa mifano ya msimbo
- GitHub Actions kwa uthibitishaji wa Markdown
- Mapitio ya jamii ya maudhui ya elimu

## Miongozo ya Omba Mchango

### Kabla ya Kuwasilisha

1. Jaribu mabadiliko ya msimbo kwa Python na TypeScript inapowezekana
2. Endesha uthibitishaji wa Markdown (hufanyika moja kwa moja wakati wa PR)
3. Hakikisha vitambulisho vya ufuatiliaji vipo kwa URL zote za Microsoft
4. Kagua viungo vya ndani ni halali
5. Hakikisha picha zimetajwa ipasavyo

### Muundo wa Kichwa cha PR

- Tumia vichwa vinavyoelezea: `[Lesson 06] Rekebisha kosa la somo la Python` au `Sasisha README kwa somo la 08`
- Taja nambari za masuala inapobidi: `Fixes #123`

### Maelezo ya PR

- Eleza kilichobadilishwa na kwa nini
- Taja masuala yanayohusiana
- Kwa mabadiliko ya msimbo, taja mifano iliyojaribiwa
- Kwa PR za tafsiri, jumuisha faili zote kwa tafsiri kamili

### Mahitaji ya Michango

- Saini Microsoft CLA (hufanyika moja kwa moja kwenye PR ya kwanza)
- Fanya fork ya hifadhi kwa akaunti yako kabla ya kufanya mabadiliko
- PR moja kwa mabadiliko mantiki (usichanganye marekebisho yasiyohusiana)
- Fanya PR zihakikishwe na ndogo inapowezekana

## Mtiririko wa Kazi wa Kawaida

### Kuongeza Mfano Mpya wa Msimbo

1. Nenda kwenye saraka inayohusika ya somo
2. Unda mfano ndani ya saraka ndogo ya `python/` au `typescript/`
3. Fuata kanuni ya majina: `{provider}-{example-name}.{py|ts|js}`
4. Jaribu kwa kutumia funguo halisi za API
5. Andika mabadiliko yoyote ya mazingira kwenye README ya somo

### Kusasisha Nyaraka

1. Hariri README.md katika saraka ya somo
2. Fuata miongozo ya Markdown (vitambulisho vya kufuatilia, viungo vya ndani)
3. Sasisho la tafsiri hufanywa na GitHub Actions (usihariri kwa mikono)
4. Jaribu viungo vyote ni halali

### Kufanya kazi na Dev Containers

1. Hifadhi ina `.devcontainer/devcontainer.json`
2. Script ya baada ya uundaji inasakinisha tegemezi za Python kiotomatiki
3. Viendelezi vya Python na Jupyter vimesanidiwa awali
4. Mazingira yanatokana na `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Ueneaji na Kuchapisha

Hii ni hifadhi ya kujifunza - hakuna mchakato wa ueneaji. Mitaala hutumiwa na:

1. **Hifadhi ya GitHub**: Upatikanaji wa moja kwa moja kwa msimbo na nyaraka
2. **GitHub Codespaces**: Mazingira ya maendeleo ya papo hapo yenye usanidi wa awali
3. **Microsoft Learn**: Maudhui yanaweza kusambazwa kwenye jukwaa rasmi la kujifunza
4. **docsify**: Tovuti ya nyaraka inayojengwa kutoka Markdown (angalia `docsifytopdf.js` na `package.json`)

### Kujenga Tovuti ya Nyaraka

```bash
# Tengeneza PDF kutoka kwa nyaraka (ikiwa inahitajika)
npm run convert
```

## Utaftaji wa Matatizo

### Masuala ya Kawaida

**Makosa ya Kuingiza Python**:
- Hakikisha mazingira ya kibinafsi yamewashwa
- Endesha `pip install -r requirements.txt`
- Kagua toleo la Python lisiwe chini ya 3.9

**Makosa ya Kujengea TypeScript**:
- Endesha `npm install` katika saraka maalum ya app
- Hakikisha toleo la Node.js linafaa
- Safisha `node_modules` na usakinishe tena inapobidi

**Makosa ya Uthibitishaji wa API**:
- Hakikisha faili `.env` ipo na ina thamani sahihi
- Kagua funguo za API zikiwa halali na hazijapungua muda wake
- Hakikisha URL za sehemu za mwisho ni sahihi kwa eneo lako

**Mabadiliko ya Mazingira Yaliyokosekana**:
- Nakili `.env.copy` hadi `.env`
- Jaza thamani zote zinazohitajika kwa somo unalofanyia kazi
- Anzisha tena programu baada ya kusasisha `.env`

## Rasilimali Zaidi

- [Mwongozo wa Kusanidi Kozi](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Miongozo ya Kuchangia](./CONTRIBUTING.md)
- [Kanuni za Tabia](./CODE_OF_CONDUCT.md)
- [Sera ya Usalama](./SECURITY.md)
- [Discord ya Azure AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Mkusanyiko wa Mifano ya Msimbo wa Juu](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Vidokezo Maalum vya Mradi

- Hii ni **hifadhi ya elimu** inayolenga kujifunza, si msimbo wa uzalishaji
- Mifano ni rahisi kwa makusudi na inalenga kufundisha dhana
- Ubora wa msimbo umeunganishwa na uwazi wa elimu
- Kila somo ni huru na linaweza kukamilishwa kwa kujitegemea
- Hifadhi inaunga mkono watoa huduma wa API wengi: Azure OpenAI, OpenAI, Microsoft Foundry Models, na watoa huduma wa nje kama Foundry Local na Ollama
- Maudhui ni mengi kwa lugha na yana mizunguko ya tafsiri ya moja kwa moja
- Jumuiya hai kwenye Discord kwa maswali na msaada

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->