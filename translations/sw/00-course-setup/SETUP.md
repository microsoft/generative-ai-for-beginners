<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:56:37+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "sw"
}
-->
# Tengeneza Mazingira Yako ya Kukuza

Tumetengeneza hifadhi hii na kozi kwa kutumia [kontena la maendeleo](https://containers.dev?WT.mc_id=academic-105485-koreyst) ambalo lina Universal runtime inayoweza kusaidia ukuzaji wa Python3, .NET, Node.js na Java. Usanidi unaohusiana umefafanuliwa kwenye faili la `devcontainer.json` lililopo kwenye folda ya `.devcontainer/` katika mzizi wa hifadhi hii.

Ili kuamsha kontena la maendeleo, lifungue katika [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (kwa runtime inayohifadhiwa kwenye wingu) au katika [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (kwa runtime inayohifadhiwa kwenye kifaa cha ndani). Soma [hati hii](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) kwa maelezo zaidi juu ya jinsi kontena za maendeleo zinavyofanya kazi ndani ya VS Code.

> [!TIP]  
> Tunapendekeza kutumia GitHub Codespaces kwa kuanza haraka na juhudi kidogo. Inatoa [kiwango cha bure cha matumizi](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) kwa akaunti za kibinafsi. Sanidi [wakati wa kusubiri](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) ili kusimamisha au kufuta codespaces zisizotumika ili kuongeza matumizi yako ya kiwango.

## 1. Kutekeleza Kazi za Nyumbani

Kila somo litakuwa na kazi za nyumbani _zisizo za lazima_ ambazo zinaweza kutolewa katika lugha moja au zaidi za programu ikiwa ni pamoja na: Python, .NET/C#, Java na JavaScript/TypeScript. Sehemu hii inatoa mwongozo wa jumla kuhusiana na kutekeleza kazi hizo.

### 1.1 Kazi za Nyumbani za Python

Kazi za nyumbani za Python zinatolewa aidha kama programu (`.py` files) au vitabu vya Jupyter (`.ipynb` files).
- Ili kuendesha kitabu cha Jupyter, kifungue katika Visual Studio Code kisha bonyeza _Select Kernel_ (kwenye kona ya juu kulia) na chagua chaguo la Python 3 lililoonyeshwa. Sasa unaweza _Run All_ ili kutekeleza kitabu hicho.
- Ili kuendesha programu za Python kutoka mstari wa amri, fuata maelekezo maalum ya kazi ya nyumbani ili kuhakikisha unachagua faili sahihi na kutoa hoja zinazohitajika.

## 2. Kusanya Watoa Huduma

Kazi za nyumbani **zinaweza** pia kutengenezwa kufanya kazi dhidi ya moja au zaidi ya mitandao mikubwa ya modeli za lugha (LLM) kupitia mtoa huduma aliyeungwa mkono kama OpenAI, Azure au Hugging Face. Hizi zinatoa _endpoint inayohifadhiwa_ (API) ambayo tunaweza kuifikia kimipango kwa kutumia hati sahihi (API key au token). Katika kozi hii, tunajadili watoa huduma hawa:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) na modeli mbalimbali ikiwa ni pamoja na mfululizo wa msingi wa GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) kwa modeli za OpenAI zilizo na utayari wa kibiashara katika kuzingatia
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) kwa modeli za chanzo wazi na seva ya uelekezi

**Utahitaji kutumia akaunti zako mwenyewe kwa mazoezi haya**. Kazi za nyumbani si lazima hivyo unaweza kuchagua kusanidi mmoja, wote - au hakuna - wa watoa huduma kulingana na maslahi yako. Baadhi ya mwongozo wa kujisajili:

| Usajili | Gharama | API Key | Playground | Maoni |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Bei](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Kwa Mradi](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Hakuna-Kodi, Wavuti](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Modeli Nyingi Zinapatikana |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Bei](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Lazima Uombe Mapema Kwa Upatikanaji](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Bei](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ina modeli chache](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Fuata maelekezo hapa chini ili _kusanya_ hifadhi hii kwa matumizi na watoa huduma tofauti. Kazi za nyumbani zinazohitaji mtoa huduma maalum zitakuwa na moja ya vitambulisho hivi kwenye jina la faili lao:
 - `aoai` - inahitaji Azure OpenAI endpoint, key
 - `oai` - inahitaji OpenAI endpoint, key
 - `hf` - inahitaji Hugging Face token

Unaweza kusanidi mmoja, hakuna, au wote wa watoa huduma. Kazi za nyumbani zinazohusiana zitasababisha makosa endapo hati za kuthibitisha hazipo.

### 2.1. Tengeneza faili la `.env`

Tunadhani kuwa tayari umesoma mwongozo hapo juu na kujisajili na mtoa huduma husika, na kupata hati za uthibitisho zinazohitajika (API_KEY au token). Kwa upande wa Azure OpenAI, tunadhani pia una uwekaji halali wa Huduma ya Azure OpenAI (endpoint) na angalau modeli moja ya GPT iliyowekwa kwa kukamilisha mazungumzo.

Hatua inayofuata ni kusanidi **mabadiliko ya mazingira ya ndani** kama ifuatavyo:

1. Angalia kwenye folda ya mzizi kwa faili la `.env.copy` ambalo linapaswa kuwa na maudhui kama haya:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Nakili faili hilo hadi `.env` kwa kutumia amri hapa chini. Faili hili ni _gitignore-d_, linalinda siri zako.

   ```bash
   cp .env.copy .env
   ```

3. Jaza maadili (badilisha vishikizi upande wa kulia wa `=`) kama ilivyoelezwa katika sehemu inayofuata.

3. (Chaguo) Ikiwa unatumia GitHub Codespaces, una chaguo la kuhifadhi mabadiliko ya mazingira kama _Codespaces secrets_ yanayohusiana na hifadhi hii. Katika hali hiyo, hautahitaji kusanidi faili ya ndani ya .env. **Hata hivyo, kumbuka kuwa chaguo hili linafanya kazi tu ikiwa unatumia GitHub Codespaces.** Bado utahitaji kusanidi faili ya .env ikiwa unatumia Docker Desktop badala yake.

### 2.2. Jaza faili la `.env`

Hebu tuangalie kwa haraka majina ya mabadiliko ili kuelewa yanachowakilisha:

| Mabadiliko  | Maelezo  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Hii ni token ya ufikiaji wa mtumiaji uliyoseti katika wasifu wako |
| OPENAI_API_KEY | Hii ni hati ya uthibitisho kwa kutumia huduma kwa endpoints za OpenAI zisizo za Azure |
| AZURE_OPENAI_API_KEY | Hii ni hati ya uthibitisho kwa kutumia huduma hiyo |
| AZURE_OPENAI_ENDPOINT | Hii ni endpoint iliyowekwa kwa rasilimali ya Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Hii ni endpoint ya modeli ya _uzalishaji wa maandishi_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Hii ni endpoint ya modeli ya _uwekaji maandishi_ |
| | |

Kumbuka: Mabadiliko mawili ya mwisho ya Azure OpenAI yanaonyesha modeli ya default kwa kukamilisha mazungumzo (uzalishaji wa maandishi) na utafutaji wa vekta (uwekaji) mtawalia. Maelekezo ya kuwasanidi yatafafanuliwa katika kazi za nyumbani husika.

### 2.3 Sanidi Azure: Kutoka Portal

Thamani za endpoint na key za Azure OpenAI zitapatikana katika [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) hivyo hebu tuanze huko.

1. Nenda kwenye [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Bonyeza chaguo la **Keys and Endpoint** kwenye menyu ya upande (menyu upande wa kushoto).
1. Bonyeza **Show Keys** - unapaswa kuona yafuatayo: KEY 1, KEY 2 na Endpoint.
1. Tumia thamani ya KEY 1 kwa AZURE_OPENAI_API_KEY
1. Tumia thamani ya Endpoint kwa AZURE_OPENAI_ENDPOINT

Ifuatayo, tunahitaji endpoints za modeli maalum ambazo tumetumia.

1. Bonyeza chaguo la **Model deployments** kwenye menyu ya upande (menyu ya kushoto) kwa rasilimali ya Azure OpenAI.
1. Katika ukurasa wa marudio, bonyeza **Manage Deployments**

Hii itakupeleka kwenye tovuti ya Azure OpenAI Studio, ambapo tutapata maadili mengine kama ilivyoelezwa hapa chini.

### 2.4 Sanidi Azure: Kutoka Studio

1. Tembelea [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **kutoka rasilimali yako** kama ilivyoelezwa hapo juu.
1. Bonyeza kichupo cha **Deployments** (menyu ya upande, kushoto) ili kuona modeli zilizowekwa sasa.
1. Ikiwa modeli yako inayotakiwa haijawekwa, tumia **Create new deployment** ili kuiweka.
1. Utahitaji modeli ya _uzalishaji wa maandishi_ - tunapendekeza: **gpt-35-turbo**
1. Utahitaji modeli ya _uwekaji maandishi_ - tunapendekeza **text-embedding-ada-002**

Sasa sasisha mabadiliko ya mazingira ili kuakisi _jina la Deployment_ lililotumika. Hii itakuwa kawaida sawa na jina la modeli isipokuwa umeibadilisha waziwazi. Kwa hivyo, kama mfano, unaweza kuwa na:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Usisahau kuhifadhi faili ya .env ukimaliza**. Sasa unaweza kutoka kwenye faili na kurudi kwenye maelekezo ya kuendesha kitabu cha Jupyter.

### 2.5 Sanidi OpenAI: Kutoka Profaili

Hati yako ya OpenAI API inaweza kupatikana katika [akaunti yako ya OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ikiwa huna moja, unaweza kujisajili kwa akaunti na kuunda API key. Mara baada ya kuwa na key, unaweza kuitumia kujaza mabadiliko ya `OPENAI_API_KEY` katika faili la `.env`.

### 2.6 Sanidi Hugging Face: Kutoka Profaili

Token yako ya Hugging Face inaweza kupatikana katika wasifu wako chini ya [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Usichapishe au kushiriki hizi hadharani. Badala yake, unda token mpya kwa matumizi ya mradi huu na nakili hiyo kwenye faili la `.env` chini ya mabadiliko ya `HUGGING_FACE_API_KEY`. _Kumbuka:_ Hii si key ya API kimsingi lakini inatumika kwa uthibitisho hivyo tunahifadhi jina hilo kwa uthabiti.

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuelewana. Hati asilia katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo chenye mamlaka. Kwa habari muhimu, tafsiri ya kitaalamu ya kibinadamu inapendekezwa. Hatutawajibika kwa maelewano mabaya au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.