<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0bba96e53ab841d99db731892a51fab8",
  "translation_date": "2025-05-20T07:01:21+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "sw"
}
-->
## Utangulizi

Dunia ya LLMs za chanzo wazi ni ya kusisimua na inabadilika kila wakati. Somo hili linakusudia kutoa mtazamo wa kina juu ya mifano ya chanzo wazi. Ikiwa unatafuta maelezo juu ya jinsi mifano ya wamiliki inavyolinganishwa na mifano ya chanzo wazi, nenda kwenye somo la ["Kuchunguza na Kulinganisha LLMs Tofauti"](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Somo hili pia litashughulikia mada ya kurekebisha lakini maelezo zaidi yanaweza kupatikana kwenye somo la ["Kurekebisha LLMs"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Malengo ya Kujifunza

- Kupata uelewa wa Mifano ya Chanzo Wazi
- Kuelewa faida za kufanya kazi na Mifano ya Chanzo Wazi
- Kuchunguza mifano ya wazi inayopatikana kwenye Hugging Face na Azure AI Studio

## Mifano ya Chanzo Wazi ni Nini?

Programu ya chanzo wazi imekuwa na jukumu muhimu katika ukuaji wa teknolojia katika nyanja mbalimbali. Mpango wa Chanzo Wazi (OSI) umefafanua [vigezo 10 vya programu](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) ili kuainishwa kama chanzo wazi. Kanuni ya chanzo lazima ishirikishwe wazi chini ya leseni iliyokubaliwa na OSI.

Wakati maendeleo ya LLM yana vipengele sawa na maendeleo ya programu, mchakato si sawa kabisa. Hii imeleta mjadala mkubwa katika jamii kuhusu ufafanuzi wa chanzo wazi katika muktadha wa LLMs. Ili mfano ulingane na ufafanuzi wa jadi wa chanzo wazi, taarifa ifuatayo inapaswa kupatikana kwa umma:

- Seti za data zilizotumika kufundisha mfano.
- Uzito kamili wa mfano kama sehemu ya mafunzo.
- Kanuni ya tathmini.
- Kanuni ya kurekebisha.
- Uzito kamili wa mfano na vipimo vya mafunzo.

Kwa sasa kuna mifano michache tu inayolingana na vigezo hivi. [Mfano wa OLMo ulioundwa na Taasisi ya Allen kwa Akili Bandia (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) ni moja inayofaa katika kundi hili.

Kwa somo hili, tutarejelea mifano kama "mifano wazi" kuendelea mbele kwani huenda isilingane na vigezo hapo juu wakati wa kuandika.

## Faida za Mifano Wazi

**Inayoweza Kubadilishwa Sana** - Kwa kuwa mifano wazi hutolewa na maelezo ya kina ya mafunzo, watafiti na waendelezaji wanaweza kubadilisha mambo ya ndani ya mfano. Hii inawezesha kuunda mifano maalum sana ambayo imerekebishwa kwa kazi maalum au eneo la utafiti. Baadhi ya mifano ya hili ni uzalishaji wa nambari, operesheni za kihisabati na biolojia.

**Gharama** - Gharama kwa kila tokeni kwa kutumia na kupeleka mifano hii ni ya chini kuliko ile ya mifano ya wamiliki. Unapojenga programu za AI za kizazi, kuangalia utendaji dhidi ya bei wakati wa kufanya kazi na mifano hii kwenye kesi yako ya matumizi inapaswa kufanywa.

**Uwezo wa Kubadilika** - Kufanya kazi na mifano wazi hukuwezesha kuwa na uwezo wa kubadilika katika kutumia mifano tofauti au kuichanganya. Mfano wa hili ni [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst) ambapo mtumiaji anaweza kuchagua mfano unaotumika moja kwa moja kwenye kiolesura cha mtumiaji:

## Kuchunguza Mifano Tofauti ya Wazi

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), iliyoendelezwa na Meta ni mfano wazi ambao umeboreshwa kwa programu za msingi wa mazungumzo. Hii ni kutokana na mbinu yake ya kurekebisha, ambayo ilijumuisha kiasi kikubwa cha mazungumzo na maoni ya binadamu. Kwa mbinu hii, mfano hutoa matokeo zaidi yanayolingana na matarajio ya binadamu ambayo yanatoa uzoefu bora wa mtumiaji.

Baadhi ya mifano ya matoleo yaliyorekebishwa ya Llama ni pamoja na [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), ambayo inabobea katika Kijapani na [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), ambayo ni toleo lililoboreshwa la mfano wa msingi.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) ni mfano wazi wenye mkazo mkubwa wa utendaji wa juu na ufanisi. Inatumia mbinu ya Mchanganyiko wa Wataalam ambayo inachanganya kundi la mifano maalum ya wataalam katika mfumo mmoja ambapo kulingana na pembejeo, mifano fulani huchaguliwa kutumika. Hii inafanya hesabu kuwa bora zaidi kwani mifano inashughulikia tu pembejeo ambayo wamebobea nayo.

Baadhi ya mifano ya matoleo yaliyorekebishwa ya Mistral ni pamoja na [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), ambayo inazingatia uwanja wa matibabu na [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), ambayo inafanya hesabu za kihisabati.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) ni LLM iliyoundwa na Taasisi ya Ubunifu wa Teknolojia (**TII**). Falcon-40B ilifundishwa kwenye vigezo bilioni 40 ambayo imeonyeshwa kufanya vizuri zaidi kuliko GPT-3 na bajeti ndogo ya hesabu. Hii ni kutokana na matumizi yake ya algorithm ya FlashAttention na umakini wa uchunguzi mwingi ambao unaiwezesha kupunguza mahitaji ya kumbukumbu wakati wa utambuzi. Kwa wakati huu wa utambuzi uliopunguzwa, Falcon-40B inafaa kwa programu za mazungumzo.

Baadhi ya mifano ya matoleo yaliyorekebishwa ya Falcon ni [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), msaidizi aliyejengwa kwenye mifano wazi na [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), ambayo inatoa utendaji wa juu kuliko mfano wa msingi.

## Jinsi ya Kuchagua

Hakuna jibu moja kwa kuchagua mfano wazi. Mahali pazuri pa kuanzia ni kwa kutumia kipengele cha kuchuja kazi cha Azure AI Studio. Hii itakusaidia kuelewa ni aina gani za kazi ambazo mfano umefundishwa. Hugging Face pia inadumisha Ubao wa Viongozi wa LLM ambao unaonyesha mifano inayofanya vizuri zaidi kulingana na vipimo fulani.

Unapotaka kulinganisha LLMs kwenye aina tofauti, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) ni rasilimali nyingine nzuri:

Ikiwa unafanya kazi kwenye kesi maalum ya matumizi, kutafuta matoleo yaliyorekebishwa ambayo yanalenga eneo hilo hilo kunaweza kuwa na ufanisi. Kufanya majaribio na mifano mingi wazi ili kuona jinsi inavyofanya kazi kulingana na matarajio yako na ya watumiaji wako ni mazoezi mengine mazuri.

## Hatua Zifuatazo

Sehemu bora kuhusu mifano wazi ni kwamba unaweza kuanza kufanya kazi nayo haraka sana. Angalia [Katalogi ya Mfano ya Azure AI Studio](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), ambayo ina mkusanyiko maalum wa Hugging Face na mifano hii tuliyojadili hapa.

## Kujifunza hakuishii hapa, endelea na Safari

Baada ya kumaliza somo hili, angalia [mkusanyiko wetu wa Kujifunza AI ya Kizazi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuongeza maarifa yako ya AI ya Kizazi!

**Kanusho**: 
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya kiasili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatuwajibiki kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.