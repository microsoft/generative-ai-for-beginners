<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:26:20+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "sw"
}
-->
# Sanidi Mazingira Yako ya Maendeleo

Tumesanidi hazina hii na kozi kwa kutumia [konteina ya maendeleo](https://containers.dev?WT.mc_id=academic-105485-koreyst) ambayo ina mazingira ya kawaida yanayoweza kusaidia maendeleo ya Python3, .NET, Node.js na Java. Mipangilio inayohusiana imefafanuliwa katika faili la `devcontainer.json` lililoko kwenye folda ya `.devcontainer/` katika mzizi wa hazina hii.

Ili kuamsha konteina ya maendeleo, ifungue katika [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (kwa mazingira yanayohifadhiwa kwenye wingu) au katika [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (kwa mazingira yanayohifadhiwa kwenye kifaa cha ndani). Soma [hati hii](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) kwa maelezo zaidi kuhusu jinsi konteina za maendeleo zinavyofanya kazi ndani ya VS Code.

> [!TIP]  
> Tunapendekeza kutumia GitHub Codespaces kwa mwanzo wa haraka na juhudi ndogo. Inatoa [kiwango cha matumizi ya bure](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) kwa akaunti za kibinafsi. Sanidi [kipindi cha muda](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) ili kusimamisha au kufuta codespaces zisizotumika ili kuongeza matumizi ya kiwango chako.

## 1. Kutekeleza Kazi

Kila somo litakuwa na kazi _hiari_ ambazo zinaweza kutolewa katika lugha moja au zaidi za programu ikiwa ni pamoja na: Python, .NET/C#, Java na JavaScript/TypeScript. Sehemu hii inatoa mwongozo wa jumla kuhusu utekelezaji wa kazi hizo.

### 1.1 Kazi za Python

Kazi za Python zinatolewa ama kama programu (faili za `.py`) au daftari za Jupyter (faili za `.ipynb`).
- Ili kuendesha daftari, ifungue katika Visual Studio Code kisha bonyeza _Chagua Kernel_ (kwenye kona ya juu kulia) na uchague chaguo la kawaida la Python 3 linaloonyeshwa. Sasa unaweza _Kukimbia Zote_ ili kutekeleza daftari.
- Ili kuendesha programu za Python kutoka kwenye mstari wa amri, fuata maelekezo maalum ya kazi ili kuhakikisha unachagua faili sahihi na kutoa hoja zinazohitajika.

## 2. Kusania Watoa Huduma

Kazi **zinaweza** pia kusanidiwa kufanya kazi dhidi ya mojawapo au zaidi ya Uwekaji wa Mfano wa Lugha Kubwa (LLM) kupitia mtoa huduma anayeungwa mkono kama OpenAI, Azure au Hugging Face. Hawa hutoa _endpoint iliyohifadhiwa_ (API) ambayo tunaweza kufikia kwa njia ya programu na sifa sahihi (funguo za API au tokeni). Katika kozi hii, tunajadili watoa huduma hawa:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) na mifano mbalimbali ikiwa ni pamoja na mfululizo wa msingi wa GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) kwa mifano ya OpenAI yenye umakini wa utayari wa biashara
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) kwa mifano ya chanzo wazi na seva ya upendeleo

**Utahitaji kutumia akaunti zako mwenyewe kwa mazoezi haya**. Kazi ni hiari hivyo unaweza kuchagua kusanidi mmoja, wote - au hakuna - wa watoa huduma kulingana na maslahi yako. Baadhi ya mwongozo kwa usajili:

| Usajili | Gharama | Funguo za API | Uwanja wa Michezo | Maoni |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Bei](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Msingi wa Mradi](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Hakuna Msimbo, Wavuti](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Mifano Mingi Inapatikana |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Bei](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Mwanzo wa SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Mwanzo wa Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Lazima Uombe Kabla ya Kupata](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Bei](https://huggingface.co/pricing) | [Fungua Tokeni](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ina mifano iliyopunguzwa](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Fuata maelekezo hapa chini ili _kusania_ hazina hii kwa matumizi na watoa huduma tofauti. Kazi zinazohitaji mtoa huduma maalum zitakuwa na mojawapo ya vitambulisho hivi katika jina lao la faili:
 - `aoai` - inahitaji Azure OpenAI endpoint, funguo
 - `oai` - inahitaji OpenAI endpoint, funguo
 - `hf` - inahitaji tokeni ya Hugging Face

Unaweza kusania mmoja, hakuna, au watoa huduma wote. Kazi zinazohusiana zitaonyesha hitilafu tu kwenye sifa zinazokosekana.

### 2.1. Tengeneza faili ya `.env`

Tunadhani kuwa tayari umesoma mwongozo hapo juu na umejiandikisha na mtoa huduma husika, na umepata sifa zinazohitajika za uthibitishaji (API_KEY au tokeni). Katika kesi ya Azure OpenAI, tunadhani pia una uwekaji halali wa Huduma ya Azure OpenAI (endpoint) na angalau mfano mmoja wa GPT uliowekwa kwa kukamilisha mazungumzo.

Hatua inayofuata ni kusanidi **vigezo vya mazingira ya ndani** kama ifuatavyo:

1. Angalia katika folda ya mzizi kwa faili ya `.env.copy` ambayo inapaswa kuwa na maudhui kama haya:

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

2. Nakili faili hiyo hadi `.env` kwa kutumia amri hapa chini. Faili hii ni _gitignore-d_, kuweka siri salama.

   ```bash
   cp .env.copy .env
   ```

3. Jaza maadili (badilisha vishikizi upande wa kulia wa `=`) kama ilivyoelezwa katika sehemu inayofuata.

3. (Hiari) Ikiwa unatumia GitHub Codespaces, una chaguo la kuhifadhi vigezo vya mazingira kama _siri za Codespaces_ zinazohusishwa na hazina hii. Katika kesi hiyo, hautahitaji kusanidi faili ya .env ya ndani. **Hata hivyo, kumbuka kuwa chaguo hili linafanya kazi tu ikiwa unatumia GitHub Codespaces.** Bado utahitaji kusanidi faili ya .env ikiwa unatumia Docker Desktop badala yake.

### 2.2. Jaza faili ya `.env`

Hebu tuangalie haraka majina ya vigezo ili kuelewa yanayowakilisha:

| Kigezo  | Maelezo  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Hii ni tokeni ya ufikiaji wa mtumiaji uliyoisanidi kwenye wasifu wako |
| OPENAI_API_KEY | Hii ni funguo ya idhini ya kutumia huduma kwa ma-OpenAI endpoints yasiyo ya Azure |
| AZURE_OPENAI_API_KEY | Hii ni funguo ya idhini ya kutumia huduma hiyo |
| AZURE_OPENAI_ENDPOINT | Hii ni endpoint iliyowekwa kwa rasilimali ya Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Hii ni endpoint ya mfano wa _uzalishaji wa maandishi_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Hii ni endpoint ya mfano wa _uchapishaji wa maandishi_ |
| | |

Kumbuka: Vigezo viwili vya mwisho vya Azure OpenAI vinaonyesha mfano wa chaguo-msingi kwa kukamilisha mazungumzo (uzalishaji wa maandishi) na utafutaji wa vekta (uchapishaji) mtawalia. Maagizo ya kuyasanidi yatafafanuliwa katika kazi husika.

### 2.3 Sanidi Azure: Kutoka Portal

Maadili ya Azure OpenAI endpoint na funguo yatapatikana katika [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) kwa hivyo tuanze hapo.

1. Nenda kwenye [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Bonyeza chaguo la **Funguo na Endpoint** katika upau wa upande (menyu upande wa kushoto).
1. Bonyeza **Onyesha Funguo** - unapaswa kuona yafuatayo: KEY 1, KEY 2 na Endpoint.
1. Tumia thamani ya KEY 1 kwa AZURE_OPENAI_API_KEY
1. Tumia thamani ya Endpoint kwa AZURE_OPENAI_ENDPOINT

Ifuatayo, tunahitaji endpoints kwa mifano maalum ambayo tumeweka.

1. Bonyeza chaguo la **Uwekaji wa Mifano** katika upau wa upande (menyu ya kushoto) kwa rasilimali ya Azure OpenAI.
1. Katika ukurasa wa marudio, bonyeza **Dhibiti Uwekaji**

Hii itakupeleka kwenye tovuti ya Azure OpenAI Studio, ambapo tutapata maadili mengine kama ilivyoelezwa hapa chini.

### 2.4 Sanidi Azure: Kutoka Studio

1. Nenda kwenye [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **kutoka kwa rasilimali yako** kama ilivyoelezwa hapo juu.
1. Bonyeza kichupo cha **Uwekaji** (upau wa upande, kushoto) ili kuona mifano iliyowekwa sasa.
1. Ikiwa mfano wako unaotaka haujawekwa, tumia **Unda uwekaji mpya** ili kuuweka.
1. Utahitaji mfano wa _uzalishaji wa maandishi_ - tunapendekeza: **gpt-35-turbo**
1. Utahitaji mfano wa _uchapishaji wa maandishi_ - tunapendekeza **text-embedding-ada-002**

Sasa sasisha vigezo vya mazingira ili kuonyesha jina la _Uwekaji_ lililotumika. Hii kawaida itakuwa sawa na jina la mfano isipokuwa uliibadilisha wazi. Kwa hivyo, kama mfano, unaweza kuwa na:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Usisahau kuhifadhi faili ya .env unapomaliza**. Sasa unaweza kutoka kwenye faili na kurudi kwenye maagizo ya kuendesha daftari.

### 2.5 Sanidi OpenAI: Kutoka Profaili

Funguo yako ya API ya OpenAI inaweza kupatikana katika [akaunti yako ya OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ikiwa huna, unaweza kujiandikisha kwa akaunti na kuunda funguo ya API. Mara unapokuwa na funguo, unaweza kuitumia kujaza kigezo `OPENAI_API_KEY` katika faili la `.env`.

### 2.6 Sanidi Hugging Face: Kutoka Profaili

Tokeni yako ya Hugging Face inaweza kupatikana katika wasifu wako chini ya [Tokeni za Ufikiaji](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Usiposti au kushiriki hizi hadharani. Badala yake, unda tokeni mpya kwa matumizi ya mradi huu na nakili hiyo katika faili la `.env` chini ya kigezo `HUGGING_FACE_API_KEY`. _Kumbuka:_ Hii kimsingi si funguo ya API lakini inatumika kwa uthibitishaji hivyo tunadumisha mkataba huo wa jina kwa uthabiti.

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Tunapojitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokamilika. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa maelewano mabaya au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.