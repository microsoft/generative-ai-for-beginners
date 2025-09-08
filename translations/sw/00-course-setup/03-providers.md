<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T18:39:00+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "sw"
}
-->
# Kuchagua na Kusanidi Mtoa Huduma wa LLM 🔑

Majukumu **yanaweza** pia kusanidiwa kufanya kazi na moja au zaidi ya miundombinu ya Large Language Model (LLM) kupitia mtoa huduma anayeungwa mkono kama OpenAI, Azure au Hugging Face. Hawa wanatoa _endpoint_ (API) ambayo tunaweza kufikia kwa njia ya programu tukitumia vitambulisho sahihi (API key au token). Katika kozi hii, tunajadili watoa huduma hawa:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) ikiwa na mifano mbalimbali ikiwemo GPT kuu.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) kwa mifano ya OpenAI inayolenga matumizi ya kibiashara
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) kwa mifano ya wazi na seva ya inference

**Utahitaji kutumia akaunti zako binafsi kwa mazoezi haya**. Majukumu haya ni hiari, hivyo unaweza kuchagua kusanidi mmoja, wote - au hata usisanidi yeyote - kulingana na matakwa yako. Mwongozo wa kujisajili:

| Jisajili | Gharama | API Key | Playground | Maoni |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Bei](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Kulingana na Mradi](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Bila-Kodi, Wavuti](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Mifano Mingi Inapatikana |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Bei](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Lazima Uombe Mapema Kupata Ufikiaji](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Bei](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ina mifano michache tu](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Fuata maelekezo hapa chini ili _kusanidi_ jalada hili kwa matumizi na watoa huduma tofauti. Majukumu yanayohitaji mtoa huduma maalum yatakuwa na moja ya vitambulisho hivi kwenye jina la faili:

- `aoai` - inahitaji Azure OpenAI endpoint, key
- `oai` - inahitaji OpenAI endpoint, key
- `hf` - inahitaji Hugging Face token

Unaweza kusanidi mmoja, hakuna, au wote. Majukumu yanayohusiana yatatoa kosa tu endapo vitambulisho havipo.

## Tengeneza faili `.env`

Tunadhani tayari umesoma mwongozo hapo juu na umejisajili kwa mtoa huduma husika, na kupata vitambulisho vya uthibitisho vinavyohitajika (API_KEY au token). Kwa Azure OpenAI, tunadhani pia una _deployment_ halali ya Azure OpenAI Service (endpoint) yenye angalau mfano mmoja wa GPT uliowekwa kwa ajili ya chat completion.

Hatua inayofuata ni kusanidi **environment variables** zako za ndani kama ifuatavyo:

1. Tafuta faili la `.env.copy` kwenye folda kuu ambalo linapaswa kuwa na maudhui kama haya:

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

2. Nakili faili hilo na uliite `.env` kwa kutumia amri hii hapa chini. Faili hili limewekwa kwenye _gitignore_, hivyo siri zako zitabaki salama.

   ```bash
   cp .env.copy .env
   ```

3. Jaza thamani (badilisha sehemu za kulia za `=`) kama ilivyoelezwa kwenye sehemu inayofuata.

4. (Hiari) Kama unatumia GitHub Codespaces, una chaguo la kuhifadhi environment variables kama _Codespaces secrets_ zinazohusishwa na jalada hili. Katika hali hiyo, hutahitaji kusanidi faili la .env kwenye kompyuta yako. **Hata hivyo, kumbuka chaguo hili linafanya kazi tu ukiwa unatumia GitHub Codespaces.** Bado utahitaji kusanidi faili la .env kama unatumia Docker Desktop badala yake.

## Jaza faili la `.env`

Tuchunguze haraka majina ya variable ili kuelewa zinawakilisha nini:

| Variable  | Maelezo  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Hii ni access token uliyoipata kwenye wasifu wako |
| OPENAI_API_KEY | Hii ni key ya uthibitisho kwa matumizi ya huduma kwa endpoints zisizo za Azure OpenAI |
| AZURE_OPENAI_API_KEY | Hii ni key ya uthibitisho kwa matumizi ya huduma hiyo |
| AZURE_OPENAI_ENDPOINT | Hii ni endpoint uliyo-deploy kwa rasilimali ya Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Hii ni endpoint ya _text generation_ model deployment |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Hii ni endpoint ya _text embeddings_ model deployment |
| | |

Kumbuka: Variable mbili za mwisho za Azure OpenAI zinaonyesha mfano chaguo-msingi wa chat completion (text generation) na vector search (embeddings) mtawalia. Maelekezo ya kuzisanidi yatatolewa kwenye majukumu husika.

## Sanidi Azure: Kutoka Portal

Thamani za Azure OpenAI endpoint na key zitapatikana kwenye [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) hivyo tuanze hapo.

1. Nenda kwenye [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Bonyeza chaguo la **Keys and Endpoint** kwenye menyu ya upande wa kushoto.
1. Bonyeza **Show Keys** - unapaswa kuona: KEY 1, KEY 2 na Endpoint.
1. Tumia thamani ya KEY 1 kwa AZURE_OPENAI_API_KEY
1. Tumia thamani ya Endpoint kwa AZURE_OPENAI_ENDPOINT

Sasa tunahitaji endpoints za mifano maalum tuliyoweka.

1. Bonyeza chaguo la **Model deployments** kwenye menyu ya upande wa kushoto kwa rasilimali ya Azure OpenAI.
1. Kwenye ukurasa unaofuata, bonyeza **Manage Deployments**

Hii itakupeleka kwenye tovuti ya Azure OpenAI Studio, ambapo tutapata thamani nyingine kama ilivyoelezwa hapa chini.

## Sanidi Azure: Kutoka Studio

1. Nenda kwenye [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **kutoka kwenye rasilimali yako** kama ilivyoelezwa hapo juu.
1. Bonyeza tab ya **Deployments** (sidebar, kushoto) kuona mifano iliyowekwa kwa sasa.
1. Kama mfano unaotaka haujawekwa, tumia **Create new deployment** kuuweka.
1. Utahitaji mfano wa _text-generation_ - tunapendekeza: **gpt-35-turbo**
1. Utahitaji mfano wa _text-embedding_ - tunapendekeza **text-embedding-ada-002**

Sasa sasisha environment variables ili ziendane na _Deployment name_ uliotumia. Mara nyingi hii itakuwa sawa na jina la mfano isipokuwa kama uliibadilisha. Kwa mfano, unaweza kuwa na:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Usisahau kuhifadhi faili la .env ukimaliza**. Sasa unaweza kutoka kwenye faili na kurudi kwenye maelekezo ya kuendesha notebook.

## Sanidi OpenAI: Kutoka Wasifu

API key yako ya OpenAI inapatikana kwenye [akaunti yako ya OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Kama huna, unaweza kujisajili na kutengeneza API key. Ukishapata key, tumia kujaza variable ya `OPENAI_API_KEY` kwenye faili la `.env`.

## Sanidi Hugging Face: Kutoka Wasifu

Token yako ya Hugging Face inapatikana kwenye wasifu wako chini ya [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Usichapishe wala kushiriki token hizi hadharani. Badala yake, tengeneza token mpya kwa ajili ya mradi huu na nakili kwenye faili la `.env` chini ya variable `HUGGING_FACE_API_KEY`. _Kumbuka:_ Hii siyo API key kiufundi lakini inatumika kwa uthibitisho, hivyo tumeacha jina hilo kwa ajili ya ulinganifu.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya utafsiri wa binadamu wa kitaalamu. Hatutawajibika kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.