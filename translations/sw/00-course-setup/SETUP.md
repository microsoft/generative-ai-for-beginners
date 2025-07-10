<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:35:04+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "sw"
}
-->
# Sanidi Mazingira Yako ya Maendeleo

Tumesanidi hazina hii na kozi hii kwa kutumia [kontena la maendeleo](https://containers.dev?WT.mc_id=academic-105485-koreyst) ambalo lina runtime ya Universal inayoweza kuunga mkono maendeleo ya Python3, .NET, Node.js na Java. Mipangilio inayohusiana imefafanuliwa katika faili la `devcontainer.json` lililoko katika folda ya `.devcontainer/` kwenye mzizi wa hazina hii.

Ili kuanzisha kontena la maendeleo, liendeshe katika [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (kwa runtime inayohudumiwa kwenye wingu) au katika [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (kwa runtime inayohudumiwa kwenye kifaa chako). Soma [nyaraka hii](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) kwa maelezo zaidi kuhusu jinsi kontena za maendeleo zinavyofanya kazi ndani ya VS Code.

> [!TIP]  
> Tunapendekeza kutumia GitHub Codespaces kwa kuanza haraka na juhudi kidogo. Inatoa [kiasi cha matumizi bure](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) kwa akaunti za binafsi. Sanidi [muda wa kusitisha](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) ili kuacha au kufuta codespaces zisizotumika ili kutumia vizuri kiasi chako.

## 1. Kutekeleza Majukumu

Kila somo litakuwa na majukumu _hiari_ ambayo yanaweza kutolewa kwa lugha moja au zaidi za programu ikiwa ni pamoja na: Python, .NET/C#, Java na JavaScript/TypeScript. Sehemu hii inatoa mwongozo wa jumla kuhusu jinsi ya kutekeleza majukumu hayo.

### 1.1 Majukumu ya Python

Majukumu ya Python hutolewa kama programu (`.py` files) au daftari za Jupyter (`.ipynb` files).  
- Ili kuendesha daftari, lifungue katika Visual Studio Code kisha bonyeza _Select Kernel_ (juu kulia) na chagua chaguo la Python 3 la msingi lililoonyeshwa. Sasa unaweza _Run All_ kuendesha daftari lote.  
- Ili kuendesha programu za Python kutoka kwenye mstari wa amri, fuata maelekezo maalum ya kazi ili kuhakikisha unachagua faili sahihi na kutoa hoja zinazohitajika.

## 2. Kusanidi Watoa Huduma

Majukumu **yanaweza** pia kusanidiwa kufanya kazi dhidi ya moja au zaidi ya usambazaji wa Large Language Model (LLM) kupitia mtoa huduma anayeunga mkono kama OpenAI, Azure au Hugging Face. Hawa hutoa _endpoint iliyohudumiwa_ (API) ambayo tunaweza kufikia kwa njia ya programu kwa kutumia vyeti sahihi (funguo za API au tokeni). Katika kozi hii, tunajadili watoa huduma hawa:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) na mifano mbalimbali ikiwemo mfululizo wa msingi wa GPT.  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) kwa mifano ya OpenAI yenye mwelekeo wa utayari wa biashara  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) kwa mifano ya chanzo huria na seva ya inference

**Utahitaji kutumia akaunti zako mwenyewe kwa mazoezi haya**. Majukumu ni hiari hivyo unaweza kuchagua kusanidi mmoja, yote - au hakuna - wa watoa huduma kulingana na maslahi yako. Mwongozo wa usajili:

| Usajili | Gharama | Funguo ya API | Uwanja wa Mchezo | Maoni |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Bei](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Kipindi cha mradi](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Bila Msimbo, Mtandao](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Mifano Mingi Inayopatikana |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Bei](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Mwanzilishi wa SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Mwanzilishi wa Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Lazima Uombe Kabla ya Kupata Ufikiaji](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Bei](https://huggingface.co/pricing) | [Tokeni za Ufikiaji](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ina mifano michache](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Fuata maelekezo hapa chini ili _kusanidi_ hazina hii kwa matumizi na watoa huduma tofauti. Majukumu yanayohitaji mtoa huduma maalum yataonyesha moja ya lebo hizi kwenye jina la faili:
 - `aoai` - inahitaji endpoint na funguo za Azure OpenAI  
 - `oai` - inahitaji endpoint na funguo za OpenAI  
 - `hf` - inahitaji tokeni ya Hugging Face

Unaweza kusanidi mmoja, hakuna, au wote watoa huduma. Majukumu yanayohusiana yataonyesha kosa la vyeti vinapokosekana.

###  2.1. Tengeneza faili `.env`

Tunadhani tayari umesoma mwongozo hapo juu na umejisajili kwa mtoa huduma husika, na umepata vyeti vinavyohitajika vya uthibitishaji (API_KEY au tokeni). Kwa Azure OpenAI, tunadhani pia una usambazaji halali wa Azure OpenAI Service (endpoint) na angalau mfano mmoja wa GPT umewekwa kwa ajili ya kukamilisha mazungumzo.

Hatua inayofuata ni kusanidi **mabadiliko ya mazingira ya eneo lako** kama ifuatavyo:

1. Tafuta katika folda ya mzizi faili la `.env.copy` ambalo linapaswa kuwa na maudhui kama haya:

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

2. Nakili faili hiyo kwa jina `.env` kwa kutumia amri ifuatayo. Faili hili limewekwa kwenye _gitignore_, linahifadhi siri salama.

   ```bash
   cp .env.copy .env
   ```

3. Jaza thamani (badilisha sehemu za nafasi upande wa kulia wa `=`) kama ilivyoelezwa katika sehemu inayofuata.

3. (Hiari) Ikiwa unatumia GitHub Codespaces, una chaguo la kuhifadhi mabadiliko ya mazingira kama _siri za Codespaces_ zinazohusiana na hazina hii. Katika hali hiyo, hautahitaji kusanidi faili la .env la eneo lako. **Hata hivyo, kumbuka kuwa chaguo hili linafanya kazi tu ikiwa unatumia GitHub Codespaces.** Bado utahitaji kusanidi faili la .env ikiwa unatumia Docker Desktop badala yake.

### 2.2. Jaza faili `.env`

Tuchukue muhtasari wa majina ya mabadiliko ili kuelewa yanayowakilisha:

| Kigezo  | Maelezo  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Hii ni tokeni ya ufikiaji ya mtumiaji uliyoanzisha kwenye wasifu wako |
| OPENAI_API_KEY | Hii ni funguo ya idhini ya kutumia huduma kwa endpoints zisizo za Azure OpenAI |
| AZURE_OPENAI_API_KEY | Hii ni funguo ya idhini ya kutumia huduma hiyo |
| AZURE_OPENAI_ENDPOINT | Hii ni endpoint iliyosambazwa kwa rasilimali ya Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Hii ni endpoint ya usambazaji wa mfano wa _utengenezaji wa maandishi_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Hii ni endpoint ya usambazaji wa mfano wa _embedding za maandishi_ |
| | |

Kumbuka: Mabadiliko mawili ya mwisho ya Azure OpenAI yanaonyesha mfano wa msingi kwa ajili ya kukamilisha mazungumzo (utengenezaji wa maandishi) na utafutaji wa vector (embedding) mtawalia. Maelekezo ya kuyapanga yatafafanuliwa katika majukumu husika.

### 2.3 Sanidi Azure: Kutoka Portal

Thamani za endpoint na funguo za Azure OpenAI zitapatikana katika [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) hivyo tuanze hapo.

1. Nenda kwenye [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
1. Bonyeza chaguo la **Keys and Endpoint** kwenye menyu ya pembeni (kushoto).  
1. Bonyeza **Show Keys** - utapata yafuatayo: KEY 1, KEY 2 na Endpoint.  
1. Tumia thamani ya KEY 1 kwa AZURE_OPENAI_API_KEY  
1. Tumia thamani ya Endpoint kwa AZURE_OPENAI_ENDPOINT  

Ifuatayo, tunahitaji endpoints za mifano maalum tuliyoisambaza.

1. Bonyeza chaguo la **Model deployments** kwenye menyu ya pembeni (kushoto) kwa rasilimali ya Azure OpenAI.  
1. Ukifika kwenye ukurasa wa lengo, bonyeza **Manage Deployments**

Hii itakupeleka kwenye tovuti ya Azure OpenAI Studio, ambapo tutapata thamani nyingine kama ilivyoelezwa hapa chini.

### 2.4 Sanidi Azure: Kutoka Studio

1. Nenda kwenye [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **kutoka kwenye rasilimali yako** kama ilivyoelezwa hapo juu.  
1. Bonyeza kichupo cha **Deployments** (pembeni kushoto) kuona mifano iliyosambazwa kwa sasa.  
1. Ikiwa mfano unaotaka haujasambazwa, tumia **Create new deployment** kuusambaza.  
1. Utahitaji mfano wa _text-generation_ - tunapendekeza: **gpt-35-turbo**  
1. Utahitaji mfano wa _text-embedding_ - tunapendekeza **text-embedding-ada-002**

Sasa sasisha mabadiliko ya mazingira kuonyesha _Jina la Usambazaji_ lililotumika. Hii kawaida itakuwa sawa na jina la mfano isipokuwa umebadilisha kwa makusudi. Kwa mfano, unaweza kuwa na:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Usisahau kuhifadhi faili la .env baada ya kumaliza**. Sasa unaweza kutoka kwenye faili na kurudi kwenye maelekezo ya kuendesha daftari.

### 2.5 Sanidi OpenAI: Kutoka Wasifu

Funguo yako ya API ya OpenAI inaweza kupatikana katika [akaunti yako ya OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ikiwa huna, unaweza kujisajili na kuunda funguo ya API. Ukipata funguo, tumia kuijaza kwenye kigezo cha `OPENAI_API_KEY` katika faili la `.env`.

### 2.6 Sanidi Hugging Face: Kutoka Wasifu

Tokeni yako ya Hugging Face inaweza kupatikana kwenye wasifu wako chini ya [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Usizitangaze au kuzishirikisha hadharani. Badala yake, tengeneza tokeni mpya kwa matumizi ya mradi huu na nakili hiyo kwenye faili la `.env` chini ya kigezo cha `HUGGING_FACE_API_KEY`. _Kumbuka:_ Hii si funguo ya API kiufundi lakini hutumika kwa uthibitishaji hivyo tunahifadhi jina hili kwa usawa.

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.