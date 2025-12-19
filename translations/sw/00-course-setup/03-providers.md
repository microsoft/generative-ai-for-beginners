<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b5b016b0eb8a1cef2e3097620d8aa23",
  "translation_date": "2025-12-19T16:31:52+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "sw"
}
-->
# Kuchagua & Kusanidi Mtoa Huduma wa LLM 🔑

Majukumu **yanaweza** pia kusanidiwa kufanya kazi dhidi ya moja au zaidi ya usambazaji wa Mfano Mkubwa wa Lugha (LLM) kupitia mtoa huduma anayeungwa mkono kama OpenAI, Azure au Hugging Face. Hawa hutoa _kiunganishi kilichohudumiwa_ (API) ambacho tunaweza kufikia kwa mpangilio sahihi wa vitambulisho (funguo ya API au tokeni). Katika kozi hii, tunajadili watoa huduma hawa:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) na mifano mbalimbali ikijumuisha mfululizo wa msingi wa GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) kwa mifano ya OpenAI yenye mwelekeo wa utayari wa biashara
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) kwa mifano ya chanzo wazi na seva ya uamuzi

**Utahitaji kutumia akaunti zako mwenyewe kwa mazoezi haya**. Majukumu ni hiari hivyo unaweza kuchagua kusanidi mmoja, wote - au hakuna - wa watoa huduma kulingana na maslahi yako. Mwongozo wa usajili:

| Usajili | Gharama | Funguo ya API | Uwanja wa Mchezo | Maoni |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Bei](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Kulingana na Mradi](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Bila Msimbo, Mtandao](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Mifano Mingi Inapatikana |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Bei](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Anza Haraka ya SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Anza Haraka ya Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Lazima Uombe Kabla ya Kupata Ufikiaji](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Bei](https://huggingface.co/pricing) | [Tokeni za Ufikiaji](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ina mifano michache](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Fuata maelekezo hapa chini ili _kusanidi_ hifadhidata hii kwa matumizi na watoa huduma tofauti. Majukumu yanayohitaji mtoa huduma maalum yataonyesha moja ya lebo hizi kwenye jina la faili:

- `aoai` - inahitaji kiunganishi cha Azure OpenAI, funguo
- `oai` - inahitaji kiunganishi cha OpenAI, funguo
- `hf` - inahitaji tokeni ya Hugging Face

Unaweza kusanidi mmoja, hakuna, au wote watoa huduma. Majukumu yanayohusiana yataonyesha tu kosa la kukosa vitambulisho.

## Tengeneza faili `.env`

Tunadhani tayari umesoma mwongozo hapo juu na kusajiliwa na mtoa huduma husika, na kupata vitambulisho vinavyohitajika vya uthibitishaji (API_KEY au tokeni). Katika kesi ya Azure OpenAI, tunadhani pia una usambazaji halali wa Huduma ya Azure OpenAI (kiunganishi) na angalau mfano mmoja wa GPT umewekwa kwa ajili ya kukamilisha mazungumzo.

Hatua inayofuata ni kusanidi **mabadiliko ya mazingira ya ndani** kama ifuatavyo:

1. Angalia kwenye folda kuu faili `.env.copy` ambayo inapaswa kuwa na maudhui kama haya:

   ```bash
   # Mtoa huduma wa OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Chaguo-msingi kimewekwa!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Nakili faili hiyo hadi `.env` kwa kutumia amri hapa chini. Faili hii ni _gitignore-d_, ikihifadhi siri salama.

   ```bash
   cp .env.copy .env
   ```

3. Jaza thamani (badilisha sehemu za nafasi upande wa kulia wa `=`) kama ilivyoelezwa katika sehemu inayofuata.

4. (Hiari) Ikiwa unatumia GitHub Codespaces, una chaguo la kuhifadhi mabadiliko ya mazingira kama _siri za Codespaces_ zinazohusiana na hifadhidata hii. Katika hali hiyo, hautahitaji kusanidi faili la .env la ndani. **Hata hivyo, kumbuka kuwa chaguo hili hufanya kazi tu ikiwa unatumia GitHub Codespaces.** Bado utahitaji kusanidi faili la .env ikiwa unatumia Docker Desktop badala yake.

## Jaza faili `.env`

Tuchukulie haraka majina ya mabadiliko kuelewa yanayowakilisha:

| Kigezo  | Maelezo  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Hii ni tokeni ya ufikiaji ya mtumiaji uliyoanzisha kwenye wasifu wako |
| OPENAI_API_KEY | Hii ni funguo ya idhini ya kutumia huduma kwa viunganishi vya OpenAI visivyo vya Azure |
| AZURE_OPENAI_API_KEY | Hii ni funguo ya idhini ya kutumia huduma hiyo |
| AZURE_OPENAI_ENDPOINT | Hii ni kiunganishi kilichosambazwa kwa rasilimali ya Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Hii ni kiunganishi cha usambazaji wa mfano wa _utengenezaji wa maandishi_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Hii ni kiunganishi cha usambazaji wa mfano wa _uwekaji wa maandishi_ |
| | |

Kumbuka: Mabadiliko mawili ya mwisho ya Azure OpenAI yanaonyesha mfano wa chaguo-msingi kwa kukamilisha mazungumzo (utengenezaji wa maandishi) na utafutaji wa vekta (uwekaji) mtawalia. Maelekezo ya kuyasanidi yataelezwa katika majukumu husika.

## Sanidi Azure: Kutoka Portal

Thamani za kiunganishi na funguo za Azure OpenAI zitapatikana kwenye [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) hivyo tuanze hapo.

1. Nenda kwenye [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Bonyeza chaguo la **Keys and Endpoint** kwenye upau wa upande (menyu upande wa kushoto).
1. Bonyeza **Show Keys** - unapaswa kuona yafuatayo: KEY 1, KEY 2 na Endpoint.
1. Tumia thamani ya KEY 1 kwa AZURE_OPENAI_API_KEY
1. Tumia thamani ya Endpoint kwa AZURE_OPENAI_ENDPOINT

Ifuatayo, tunahitaji viunganishi vya mifano maalum tuliyoisambaza.

1. Bonyeza chaguo la **Model deployments** kwenye upau wa upande (menyu kushoto) kwa rasilimali ya Azure OpenAI.
1. Katika ukurasa wa mwisho, bonyeza **Manage Deployments**

Hii itakupeleka kwenye tovuti ya Azure OpenAI Studio, ambapo tutapata thamani nyingine kama ilivyoelezwa hapa chini.

## Sanidi Azure: Kutoka Studio

1. Nenda kwenye [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **kutoka rasilimali yako** kama ilivyoelezwa hapo juu.
1. Bonyeza kichupo cha **Deployments** (upau wa upande, kushoto) kuona mifano iliyosambazwa kwa sasa.
1. Ikiwa mfano unaotaka haujasambazwa, tumia **Create new deployment** kuusambaza.
1. Utahitaji mfano wa _utengenezaji wa maandishi_ - tunapendekeza: **gpt-35-turbo**
1. Utahitaji mfano wa _uwekaji wa maandishi_ - tunapendekeza **text-embedding-ada-002**

Sasa sasisha mabadiliko ya mazingira kuonyesha _Jina la Usambazaji_ lililotumika. Hii kawaida itakuwa sawa na jina la mfano isipokuwa umeibadilisha waziwazi. Kwa mfano, unaweza kuwa na:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Usisahau kuhifadhi faili la .env ukimaliza**. Sasa unaweza kutoka kwenye faili na kurudi kwenye maelekezo ya kuendesha daftari la kumbukumbu.

## Sanidi OpenAI: Kutoka Wasifu

Funguo yako ya API ya OpenAI inaweza kupatikana kwenye [akaunti yako ya OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ikiwa huna, unaweza kujisajili kwa akaunti na kuunda funguo ya API. Ukipata funguo, unaweza kuitumia kujaza kigezo cha `OPENAI_API_KEY` kwenye faili la `.env`.

## Sanidi Hugging Face: Kutoka Wasifu

Tokeni yako ya Hugging Face inaweza kupatikana kwenye wasifu wako chini ya [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Usizitangaze au kuzishirikisha hadharani. Badala yake, unda tokeni mpya kwa matumizi ya mradi huu na nakili hiyo kwenye faili la `.env` chini ya kigezo cha `HUGGING_FACE_API_KEY`. _Kumbuka:_ Hii si funguo ya API kiufundi lakini hutumika kwa uthibitishaji hivyo tunahifadhi jina hili kwa muafaka.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kiarifa cha Kukataa**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatuna dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->