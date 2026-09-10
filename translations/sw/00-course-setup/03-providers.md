# Kuchagua & Kusanidi Mtoa Huduma wa LLM 🔑

Majukumu **yanaweza** pia kusanidiwa kufanya kazi dhidi ya uenezaji mmoja au zaidi wa Mfano Mkubwa wa Lugha (LLM) kupitia mtoa huduma anayeelezwa kama OpenAI, Azure au Hugging Face. Hawa hutoa _sehemu ya mwenyeji_ (API) ambayo tunaweza kufikia kwa njia ya programu kwa kutumia hati sahihi (funguo za API au tokeni). Katika kozi hii, tunazungumzia watoa huduma hawa:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) na mifano mbalimbali ikiwemo mfululizo wa msingi wa GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) kwa mifano ya OpenAI yenye mtazamo wa ustadi wa biashara
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) kwa sehemu moja ya huduma na ufunguo wa API kupata mamia ya mifano kutoka OpenAI, Meta, Mistral, Cohere, Microsoft na zaidi (inachukua nafasi ya GitHub Models, ambayo itasimama mwishoni mwa Julai 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) kwa mifano ya chanzo wazi na seva ya inferensi
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) au [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ikiwa ungependa kuendesha mifano kikamilifu bila mtandao kwenye kifaa chako mwenyewe, bila haja ya usajili wa wingu

**Utahitaji kutumia akaunti zako mwenyewe kwa mazoezi haya**. Majukumu ni hiari hivyo unaweza kuchagua kusanidi mmoja, yote - au hakuna - ya watoa huduma kulingana na maslahi yako. Mwongozo wa kujiandikisha:

| Jisajili | Gharama | Funguo ya API | Ukumbi wa majaribio | Maoni |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Bei](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Bila Msimbo, Mtandao](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Mifano Mingi Inapatikana |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Bei](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Kuanzia Haraka](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Kuanzia Haraka](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Lazima Uombe Kufikia Mbele](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Bei](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Ukaguzi wa Mradi](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Ukumbi wa Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Kiwango cha bure kinapatikana; sehemu moja + ufunguo kwa watoa huduma wengi wa mfano |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Bei](https://huggingface.co/pricing) | [Tokeni za Kufikia](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ina mifano kidogo](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Bure (inaendesha kwenye kifaa chako) | Haitakiwi | [CLI/SDK ya Mitaa](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Sehemu kikamilifu isiyo na mtandao, inayolingana na OpenAI |
| | | | | |

Fuata maelekezo chini ili _kusanidi_ hifadhidata hii kwa matumizi na watoa huduma tofauti. Majukumu yanayohitaji mtoa huduma maalum yata kuwa na mojawapo ya lebo hizi kwenye jina la faili yao:

- `aoai` - inahitaji sehemu ya Azure OpenAI, ufunguo
- `oai` - inahitaji sehemu ya OpenAI, ufunguo
- `hf` - inahitaji tokeni ya Hugging Face
- `githubmodels` - inahitaji sehemu ya Microsoft Foundry Models, ufunguo (GitHub Models itasimama mwishoni mwa Julai 2026)

Unaweza kusanidi mmoja, hakuna, au wote watoa huduma. Majukumu yanayohusiana yatafanya tu kosa la kutokuwepo kwa hati zinazohitajika.

## Unda faili `.env`

Tunadhani tayari umejisomea mwongozo hapo juu na ujisajili kwa mtoa huduma husika, na upate hati za uthibitishaji zinazohitajika (API_KEY au tokeni). Katika kesi ya Azure OpenAI, tunadhani pia una uenezaji halali wa huduma ya Azure OpenAI (sehemu) iliyotumika na mfano mmoja au zaidi wa GPT kwa kumaliza mazungumzo.

Hatua inayofuata ni kusanidi **mabadiliko ya mazingira ya ndani** kama ifuatavyo:

1. Angalia kwenye folda kuu kwa faili `.env.copy` ambayo inapaswa kuwa na maudhui kama haya:

   ```bash
   # Mtoa Huduma wa OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI katika Microsoft Foundry
   ## (Huduma ya Azure OpenAI sasa ni sehemu ya Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Chaguo-msingi kimewekwa! (toleo thabiti la sasa la API ya GA)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Miundo ya Microsoft Foundry (katalogi ya miundo ya wahudumu wengi, inachukua nafasi ya Miundo ya GitHub, ambayo itakoma mwishoni mwa Julai 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Nakili faili hiyo kwa `.env` kwa kutumia amri ifuatayo. Faili hili linatajwa katika _gitignore_, linalinda siri.

   ```bash
   cp .env.copy .env
   ```

3. Jaza maadili (badilisha mstari wa kushoto wa `=`) kama inavyoelezwa katika sehemu inayofuata.

4. (Chaguo) Ikiwa unatumia GitHub Codespaces, una chaguo la kuhifadhi mabadiliko ya mazingira kama _siri za Codespaces_ zinazohusiana na hifadhidata hii. Katika hali hiyo, hutahitaji kusanidi faili la .env la ndani. **Hata hivyo, kumbuka kuwa chaguo hili linafanya kazi tu ukiwa unatumia GitHub Codespaces.** Bado utahitaji kusanidi faili la .env ikiwa unatumia Docker Desktop badala yake.

## Jaza faili `.env`

Hebu tuchunguze kwa haraka majina ya mabadiliko kuelewa maana yake:

| Mabadiliko  | Maelezo  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Hii ni tokeni ya upatikanaji wa mtumiaji uliyoz-sanidi kwenye wasifu wako |
| OPENAI_API_KEY | Hii ni ufunguo wa idhini wa kutumia huduma kwa sehemu zisizo za Azure OpenAI |
| AZURE_OPENAI_API_KEY | Hii ni ufunguo wa idhini wa kutumia huduma hiyo |
| AZURE_OPENAI_ENDPOINT | Hii ni sehemu iliyotumika kwa rasilimali ya Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Hii ni sehemu ya uenezaji wa mfano wa _uzoaji wa maandishi_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Hii ni sehemu ya uenezaji wa mfano wa _mafananisho ya maandishi_ |
| AZURE_INFERENCE_ENDPOINT | Hii ni sehemu ya mradi wako wa Microsoft Foundry, inayotumika kwa Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Hii ni ufunguo wa API kwa mradi wako wa Microsoft Foundry |
| | |

Kumbuka: Mabadiliko ya Azure OpenAI mawili ya mwisho yanaonyesha mfano wa msingi wa kumaliza mazungumzo (uzoaji wa maandishi) na utafutaji wa vekta (mafananisho) mtawalia. Maelekezo ya kusanidi zitafafanuliwa katika majukumu husika.

## Sanidi Azure OpenAI: Kutoka Portal

> **Kumbuka:** Huduma ya Azure OpenAI sasa ni sehemu ya [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Rasilimali na uenezaji bado huonekana katika Azure Portal, lakini usimamizi wa kila siku wa mifano (uenezaji, ukumbi wa majaribio, ufuatiliaji) sasa hufanyika kwenye portal ya Foundry badala ya "Azure OpenAI Studio" ya zamani.

Thamani za sehemu na ufunguo wa Azure OpenAI zitapatikana katika [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) kwa hiyo tuanze hapo.

1. Nenda kwenye [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Bonyeza chaguo la **Funguo na Sehemu** kwenye upau wa upande (menyu upande wa kushoto).
1. Bonyeza **Onyesha Funguo** - unapaswa kuona yafuatayo: UFUNGUO 1, UFUNGUO 2 na Sehemu.
1. Tumia thamani ya UFUNGUO 1 kwa AZURE_OPENAI_API_KEY
1. Tumia thamani ya Sehemu kwa AZURE_OPENAI_ENDPOINT

Ifuatayo, tunahitaji sehemu za mifano maalum tuliyoizeneza.

1. Bonyeza chaguo la **Uenezaji wa mfano** kwenye upau wa upande (menyu kushoto) kwa rasilimali ya Azure OpenAI.
1. Katika ukurasa wa mwisho, bonyeza **Nenda kwenye portal ya Microsoft Foundry** (au **Simamia Uenezaji**, kulingana na aina ya rasilimali yako)

Hii itakupeleka kwenye portal ya Microsoft Foundry, ambapo tutapata thamani zingine kama zilivyoelezwa hapa chini.

## Sanidi Azure OpenAI: Kutoka portal ya Microsoft Foundry

1. Nenda kwenye [portal ya Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **kutoka rasilimali yako** kama ilivyoelezwa hapo juu.
1. Bonyeza kichupo cha **Uenezaji** (upau wa upande, kushoto) kuona mifano iliyotumiwa sasa.
1. Ikiwa mfano unayotaka haujaeneza, tumia **Eneza mfano** kuutumia kutoka kwenye [katalogi ya mifano](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Utahitaji mfano wa _uzoaji wa maandishi_ - tunashauri: **gpt-5-mini**
1. Utahitaji mfano wa _ongeza maandishi_ - tunashauri **text-embedding-3-small**

Sasisha sasa mabadiliko ya mazingira ili kuonyesha _Jina la Uenezaji_ lililotumiwa. Hii kawaida itakuwa sawa na jina la mfano isipokuwa ukibadilisha waziwazi. Kwa mfano, unaweza kuwa na:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Usisahau kuhifadhi faili la .env baada ya kumaliza**. Sasa unaweza kutoka kwenye faili na kurudi kwenye maelekezo ya kuendesha daftari.

## Sanidi OpenAI: Kutoka Wasifu

Ufunguo wako wa API wa OpenAI unaweza kupatikana kwenye [akaunti yako ya OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Ikiwa huna moja, unaweza kujisajili na kuunda ufunguo wa API. Ukipata ufunguo, unaweza kuitumia kujaza kigezo cha `OPENAI_API_KEY` kwenye faili `.env`.

## Sanidi Hugging Face: Kutoka Wasifu

Tokeni yako ya Hugging Face inaweza kupatikana kwenye wasifu wako chini ya [Tokeni za Kufikia](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Usiziweke hadharani au kushiriki. Badala yake, tengeneza tokeni mpya kwa matumizi ya mradi huu na nakili hiyo kwenye faili `.env` chini ya kigezo cha `HUGGING_FACE_API_KEY`. _Kumbuka:_ Hii si funguo halisi ya API lakini hutumika kwa uthibitishaji, hivyo tunahifadhi mtindo huo wa majina kwa mlingano.

## Sanidi Microsoft Foundry Models: Kutoka Portal

> **Kumbuka:** GitHub Models itasimama mwishoni mwa Julai 2026. Microsoft Foundry Models ni mbadala wa moja kwa moja, ukitoa katalogi ya modeli ya bure ya kujaribu na uzoefu wa Azure AI Inference SDK / OpenAI SDK.

1. Nenda [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) na unda (au fungua) mradi wa Foundry.
1. Pitia [katalogi ya mifano](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) na enezaji mfano, kwa mfano `gpt-5-mini`.
1. Kwenye ukurasa wa **Muhtasari** wa mradi, nakili **sehemu** na **funguo ya API**.
1. Tumia thamani ya sehemu kwa `AZURE_INFERENCE_ENDPOINT` na thamani ya ufunguo kwa `AZURE_INFERENCE_CREDENTIAL` kwenye faili `.env`.

## Watoa Huduma wa Nje ya Mtandao / Wenyeji

Ikiwa ungependa kuto tumia mkataba wa wingu kabisa, unaweza kuendesha mifano ya wazi inayolingana moja kwa moja kwenye kifaa chako:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - runtime ya kifaa cha Microsoft. Huchagua moja kwa moja mtoa huduma bora wa utekelezaji (NPU, GPU, au CPU) na huonesha sehemu inayolingana na OpenAI, hivyo unaweza kutumia sehemu kubwa ya msimbo wa mfano katika kozi hii kwa mabadiliko kidogo. Angalia [nyaraka za Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) kuanza, au weka kwa `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - mbadala maarufu wa kuendesha mifano ya wazi kama Llama, Phi, Mistral, na Gemma kwa ndani.


Angalia [Somo la 19: Kujenga kwa kutumia SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) kwa mifano ya vitendo kutumia chaguzi zote mbili.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->