# Kuchagua na Kusanidi Mtoa Huduma wa LLM 🔑

Majukumu **yanaweza** pia kusanidiwa kufanya kazi dhidi ya moja au zaidi ya usambazaji wa Mfano Mkubwa wa Lugha (LLM) kupitia mtoa huduma aliyeletwa kama msaada kama OpenAI, Azure au Hugging Face. Hawa hutoa _sehemu ya mwenyeji_ (API) ambayo tunaweza kuipata kwa mpango kwa kutumia vibali sahihi (funguo za API au tokeni). Katika kozi hii, tunajadili watoa huduma hawa:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) na mifano mbalimbali ikiwa ni pamoja na mfululizo kuu wa GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) kwa mifano ya OpenAI ikiwa na kuzingatia utayari wa kampuni
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) kwa sehemu moja na funguo ya API kupata mamia ya mifano kutoka OpenAI, Meta, Mistral, Cohere, Microsoft na zaidi (inachukua nafasi ya GitHub Models, ambayo itafutwa mwishoni mwa Julai 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) kwa mifano ya chanzo wazi na seva ya uchambuzi
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) au [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ikiwa ungependa kuendesha mifano kikamilifu bila mtandao kwenye kifaa chako, bila haja ya usajili wa wingu

**Utahitaji kutumia akaunti zako binafsi kwa mazoezi haya**. Majukumu ni hiari hivyo unaweza kuchagua kusanidi moja, zote - au hakuna - wa watoa huduma kwa kuzingatia mambo unayovutiwa nayo. Mwongozo wa usajili:

| Usajili | Gharama | Funguo za API | Uwanja wa Mchezo | Maoni |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Bei](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Inayotegemea Mradi](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Bila Msimbo, Tovuti](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Mifano Mingi Inapatikana |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Bei](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Kuanzia haraka](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Kuanzia haraka](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Inahitajika Kuomba Mapema Kuwahi Kupata] (https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Bei](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Ukurasa wa Muhtasari wa Mradi](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Uwanja wa Mchezo wa Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Kiwango cha bure kinapatikana; sehemu moja + funguo kwa watoa huduma wengi wa mfano |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Bei](https://huggingface.co/pricing) | [Tokoni za Ufikiaji](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ina mifano michache](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Bure (inaendeshwa kifaa chako) | Hakihitajiki | [CLI/SDK ya Ndani](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Sehemu ya mwenyeji kikamilifu bila mtandao, inayoendana na OpenAI |
| | | | | |

Fuata maelekezo hapa chini ili _kusanidi_ hifadhidata hii kwa kutumia watoa huduma tofauti. Majukumu yanayohitaji mtoa huduma maalum yataonyesha moja ya lebo hizi katika jina la faili:

- `aoai` - inahitaji sehemu ya Azure OpenAI, funguo
- `oai` - inahitaji sehemu ya OpenAI, funguo
- `hf` - inahitaji tokeni ya Hugging Face
- `githubmodels` - inahitaji sehemu ya Microsoft Foundry Models, funguo (GitHub Models itafutwa mwishoni mwa Julai 2026)

Unaweza kusanidi moja, hakuna, au wote watoa huduma. Majukumu yanayohusiana yatatokea hitilafu endapo vibali vitakosekana.

## Unda faili la `.env`

Tunachukulia kuwa tayari umesoma mwongozo hapo juu na kusajiliwa na mtoa huduma husika, na kupata vibali vya uthibitishaji vinavyohitajika (API_KEY au tokeni). Katika kesi ya Azure OpenAI, tunachukulia pia kuwa una usambazaji halali wa Huduma ya Azure OpenAI (sehemu) na angalau mfano mmoja wa GPT uliowekwa kwa ajili ya kukamilisha mazungumzo.

Hatua inayofuata ni kusanidi **mabadiliko ya mazingira ya ndani** kama ifuatavyo:

1. Angalia katika saraka kuu faili `.env.copy` inayopaswa kuwa na maudhui kama haya:

   ```bash
   # Mtoa huduma wa OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI katika Microsoft Foundry
   ## (Huduma ya Azure OpenAI sasa ni sehemu ya Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Chaguo-msingi kimewekwa! (toleo thabiti la sasa la GA API)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Mifano ya Microsoft Foundry (katalogi ya mifano ya watoa huduma wengi, inachukua nafasi ya Mifano ya GitHub, ambayo itatolewa mwisho wa Julai 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Nakili faili hiyo kuwa `.env` kwa kutumia amri hapa chini. Faili hii imewekwa katika _gitignore_, ikilinda siri.

   ```bash
   cp .env.copy .env
   ```

3. Jaza thamani (badilisha nafasi za kushoto ya `=`) kama inavyoelezwa katika sehemu ifuatayo.

4. (Hiari) Ikiwa unatumia GitHub Codespaces, una chaguo la kuhifadhi mabadiliko ya mazingira kama _siri za Codespaces_ zinazohusiana na hifadhidata hii. Katika hali hiyo, hautahitaji kusanidi faili la .env la ndani. **Hata hivyo, kumbuka kuwa chaguo hili linafanya kazi tu ikiwa unatumia GitHub Codespaces.** Bado utahitaji kusanidi faili la .env ikiwa unatumia Docker Desktop badala yake.

## Jaza faili la `.env`

Hebu tuchunguze jina la vigezo ili kuelewa kinachowakilishwa:

| Kigezo | Maelezo |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Hii ni tokeni ya ufikiaji ya mtumiaji unayosanidi kwenye wasifu wako |
| OPENAI_API_KEY | Hii ni funguo ya idhini ya kutumia huduma kwa sehemu zisizo za Azure OpenAI |
| AZURE_OPENAI_API_KEY | Hii ni funguo ya idhini ya kutumia huduma hiyo |
| AZURE_OPENAI_ENDPOINT | Hii ni sehemu iliyoanzishwa ya rasilimali ya Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Hii ni sehemu ya usambazaji wa mfano wa _utengenezaji wa maandishi_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Hii ni sehemu ya usambazaji wa mfano wa _uwekaji wa maandishi_ |
| AZURE_INFERENCE_ENDPOINT | Hii ni sehemu kwa mradi wako wa Microsoft Foundry, hutumika kwa Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Hii ni funguo ya API ya mradi wako wa Microsoft Foundry |
| | |

Kumbuka: Vigezo viwili vya mwisho vya Azure OpenAI vinaonyesha mfano wa chaguo la kukamilisha mazungumzo (utengenezaji wa maandishi) na utafutaji wa vector (uwekaji) mtawaliwa. Maelekezo ya kuvitumia yataelezwa katika mazoezi husika.

## Sanidi Azure OpenAI: Kutoka Portal

> **Kumbuka:** Huduma ya Azure OpenAI sasa ni sehemu ya [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Rasilimali na usambazaji bado huonekana kwenye Portal ya Azure, lakini usimamizi wa kila siku wa mfano (usambazaji, uwanja wa mchezo, ufuatiliaji) sasa hufanyika kwenye portal ya Foundry badala ya "Azure OpenAI Studio" iliyokuwa huru zamani.

Thamani za sehemu na funguo za Azure OpenAI zitapatikana kwenye [Portal ya Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) hivyo tuanze huko.

1. Nenda kwenye [Portal ya Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Bonyeza chaguo la **Funguo na Sehemu** kwenye menyu ya pembeni (menu upande wa kushoto).
1. Bonyeza **Onyesha Funguo** - unapaswa kuona yafuatayo: KEY 1, KEY 2 pamoja na Sehemu.
1. Tumia thamani ya KEY 1 kwa AZURE_OPENAI_API_KEY
1. Tumia thamani ya Sehemu kwa AZURE_OPENAI_ENDPOINT

Ifuatayo, tunahitaji sehemu za mifano maalum tuliyo isambaza.

1. Bonyeza chaguo la **Usambazaji wa mifano** kwenye menyu ya pembeni (upande wa kushoto) kwa rasilimali ya Azure OpenAI.
1. Katika ukurasa wa lengo, bonyeza **Nenda kwenye portal ya Microsoft Foundry** (au **Simamia Usambazaji**, kulingana na aina ya rasilimali yako)

Hii itakupeleka kwenye portal ya Microsoft Foundry, ambapo tutapata thamani nyingine kama inavyoelezwa hapa chini.

## Sanidi Azure OpenAI: Kutoka portal ya Microsoft Foundry

1. Elekea kwenye [portal ya Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **kutoka rasilimali yako** kama ilivyoelezwa hapo juu.
1. Bonyeza kichupo cha **Usambazaji** (menyu ya pembeni, kushoto) kuangalia mifano iliyosambazwa kwa sasa.
1. Ikiwa mfano unaotaka haujasambazwa, tumia **Sambaza mfano** kuusambaza kutoka [katalogi ya mifano](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Utahitaji mfano wa _utengenezaji wa maandishi_ - tunapendekeza: **gpt-4o-mini**
1. Utahitaji mfano wa _uwekaji wa maandishi_ - tunapendekeza **text-embedding-3-small**

Sasa sasisha mabadiliko ya mazingira kuakisi _Jina la Usambazaji_ ulilotumiwa. Hii kawaida itakuwa sawa na jina la mfano isipokuwa umeibadilisha waziwazi. Kwa mfano, unaweza kuwa na:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Usisahau kuhifadhi faili ya .env baada ya kumaliza**. Sasa unaweza kutoka kwenye faili na kurudi kwenye maelekezo ya kuendesha daftari la mazoezi.

## Sanidi OpenAI: Kutoka Wasifu

Funguo yako ya API ya OpenAI inaweza kupatikana kwenye [akaunti yako ya OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ikiwa huna moja, unaweza kusajili akaunti na kuunda funguo ya API. Ukipata funguo, unaweza kuitumia kujaza kigezo cha `OPENAI_API_KEY` kwenye faili la `.env`.

## Sanidi Hugging Face: Kutoka Wasifu

Tokeni yako ya Hugging Face inaweza kupatikana kwenye wasifu wako chini ya [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Usisite au usishirikishe hadharani. Badala yake, tengeneza tokeni mpya kwa matumizi ya mradi huu na uikilishe kwenye faili la `.env` chini ya kigezo cha `HUGGING_FACE_API_KEY`. _Kumbuka:_ Hii si funguo ya API kiufundi lakini hutumika kwa uthibitishaji hivyo tunahifadhi jina hili kwa ajili ya umoja.

## Sanidi Microsoft Foundry Models: Kutoka Portal

> **Kumbuka:** GitHub Models itafutwa mwishoni mwa Julai 2026. Microsoft Foundry Models ni mbadala wa moja kwa moja, ukitoa katalogi ya mfano wa bure wa kujaribu na uzoefu wa SDK ya Azure AI Inference / OpenAI SDK.

1. Nenda kwa [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) na unda (au fungua) mradi wa Foundry.
1. Pitia [katalogi ya mifano](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) na sambaza mfano, kwa mfano `gpt-4o-mini`.
1. Kwenye ukurasa wa Muhtasari wa mradi, nakili **sehemu** na **funguo za API**.
1. Tumia thamani ya sehemu kwa `AZURE_INFERENCE_ENDPOINT` na thamani ya funguo kwa `AZURE_INFERENCE_CREDENTIAL` kwenye faili lako la `.env`.

## Watoa Huduma Wasio Mtandaoni / Wa Ndani

Ikiwa ungependa kuto tumia usajili wa wingu kabisa, unaweza kuendesha mifano inayoendana moja kwa moja kwenye kifaa chako mwenyewe:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - mazingira ya mwendo wa Microsoft kwenye kifaa. Huchagua kiotomatiki mtoa huduma bora wa utekelezaji (NPU, GPU, au CPU) na hutoa sehemu inayoendana na OpenAI, hivyo unaweza kutumia sehemu kubwa ya mfano wa msimbo katika kozi hii kwa mabadiliko madogo. Angalia [nyaraka za Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) kuanza, au usakinishe kwa `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - mbadala maarufu kwa kuendesha mifano wazi kama Llama, Phi, Mistral, na Gemma ndani ya kifaa.


Angalia [Somo la 19: Kuunda na SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) kwa mifano ya vitendo ikitumia chaguzi zote mbili.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->