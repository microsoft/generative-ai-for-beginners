<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a83aac52158c23161046cbd13faa2b",
  "translation_date": "2025-10-17T21:20:00+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "sw"
}
-->
[![Miundo ya Chanzo Huria](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.sw.png)](https://youtu.be/CuICgfuHFSg?si=x8SpFRUsIxM9dohN)

## Utangulizi

Ulimwengu wa LLM za chanzo huria ni wa kusisimua na unabadilika kila wakati. Somo hili linakusudia kutoa muhtasari wa kina kuhusu miundo ya chanzo huria. Ikiwa unatafuta maelezo kuhusu jinsi miundo ya wamiliki inavyolinganishwa na miundo ya chanzo huria, nenda kwenye somo la ["Kuchunguza na Kulinganisha LLM Tofauti"](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Somo hili pia litashughulikia mada ya kurekebisha lakini maelezo zaidi yanaweza kupatikana kwenye somo la ["Kurekebisha LLM"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Malengo ya Kujifunza

- Kupata uelewa wa Miundo ya Chanzo Huria
- Kuelewa faida za kufanya kazi na Miundo ya Chanzo Huria
- Kuchunguza miundo ya chanzo huria inayopatikana kwenye Hugging Face na Azure AI Studio

## Miundo ya Chanzo Huria ni nini?

Programu ya chanzo huria imekuwa na jukumu muhimu katika ukuaji wa teknolojia katika nyanja mbalimbali. Mpango wa Chanzo Huria (OSI) umefafanua [vigezo 10 vya programu](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) ili kuainishwa kama chanzo huria. Msimbo wa chanzo lazima ushirikishwe wazi chini ya leseni iliyoidhinishwa na OSI.

Ingawa maendeleo ya LLM yana vipengele sawa na maendeleo ya programu, mchakato si sawa kabisa. Hii imeleta mjadala mwingi katika jamii kuhusu ufafanuzi wa chanzo huria katika muktadha wa LLM. Ili modeli iweze kuendana na ufafanuzi wa jadi wa chanzo huria, taarifa zifuatazo zinapaswa kupatikana hadharani:

- Seti za data zilizotumika kufundisha modeli.
- Uzito kamili wa modeli kama sehemu ya mafunzo.
- Msimbo wa tathmini.
- Msimbo wa kurekebisha.
- Uzito kamili wa modeli na vipimo vya mafunzo.

Kwa sasa kuna modeli chache tu zinazolingana na vigezo hivi. [Modeli ya OLMo iliyoundwa na Taasisi ya Allen ya Akili Bandia (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) ni moja inayolingana na kategoria hii.

Kwa somo hili, tutarejelea modeli kama "miundo huria" kuendelea mbele kwani huenda zisilingane na vigezo vilivyo hapo juu wakati wa kuandika.

## Faida za Miundo Huria

**Inaweza Kubadilishwa Sana** - Kwa kuwa miundo huria hutolewa na maelezo ya kina ya mafunzo, watafiti na watengenezaji wanaweza kurekebisha mambo ya ndani ya modeli. Hii inawezesha uundaji wa modeli maalum sana ambazo zimeboreshwa kwa kazi maalum au eneo la utafiti. Baadhi ya mifano ya hili ni kizazi cha msimbo, operesheni za hisabati na biolojia.

**Gharama** - Gharama kwa kila tokeni ya kutumia na kupeleka modeli hizi ni ya chini kuliko ile ya modeli za wamiliki. Wakati wa kujenga programu za AI za kizazi, kuangalia utendaji dhidi ya bei wakati wa kufanya kazi na modeli hizi kwa kesi yako ya matumizi inapaswa kufanywa.

![Gharama ya Modeli](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.sw.png)  
Chanzo: Artificial Analysis

**Uwezo wa Kubadilika** - Kufanya kazi na miundo huria kunakuwezesha kubadilika kwa kutumia modeli tofauti au kuzichanganya. Mfano wa hili ni [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst) ambapo mtumiaji anaweza kuchagua modeli inayotumika moja kwa moja kwenye kiolesura cha mtumiaji:

![Chagua Modeli](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.sw.png)

## Kuchunguza Miundo Huria Tofauti

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), iliyotengenezwa na Meta ni modeli huria ambayo imeboreshwa kwa programu za mazungumzo. Hii ni kutokana na mbinu yake ya kurekebisha, ambayo ilijumuisha kiwango kikubwa cha mazungumzo na maoni ya binadamu. Kwa mbinu hii, modeli hutoa matokeo zaidi yanayolingana na matarajio ya binadamu ambayo hutoa uzoefu bora wa mtumiaji.

Baadhi ya mifano ya matoleo yaliyorekebishwa ya Llama ni pamoja na [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), ambayo inajikita katika Kijapani na [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), ambayo ni toleo lililoboreshwa la modeli ya msingi.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) ni modeli huria yenye mtazamo mkubwa wa utendaji wa hali ya juu na ufanisi. Inatumia mbinu ya Mixture-of-Experts ambayo inachanganya kundi la modeli maalum za wataalamu katika mfumo mmoja ambapo kulingana na pembejeo, modeli fulani huchaguliwa kutumika. Hii inafanya hesabu kuwa bora zaidi kwani modeli zinashughulikia tu pembejeo ambazo zimebobea.

Baadhi ya mifano ya matoleo yaliyorekebishwa ya Mistral ni pamoja na [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), ambayo inajikita katika uwanja wa matibabu na [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), ambayo inafanya hesabu za hisabati.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) ni LLM iliyoundwa na Taasisi ya Ubunifu wa Teknolojia (**TII**). Falcon-40B ilifundishwa kwa vigezo bilioni 40 ambavyo vimeonyeshwa kufanya vizuri zaidi kuliko GPT-3 kwa bajeti ndogo ya hesabu. Hii ni kutokana na matumizi yake ya algorithmi ya FlashAttention na umakini wa maswali mengi ambayo inawezesha kupunguza mahitaji ya kumbukumbu wakati wa utabiri. Kwa muda huu mfupi wa utabiri, Falcon-40B inafaa kwa programu za mazungumzo.

Baadhi ya mifano ya matoleo yaliyorekebishwa ya Falcon ni [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), msaidizi aliyejengwa juu ya miundo huria na [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), ambayo hutoa utendaji wa juu kuliko modeli ya msingi.

## Jinsi ya Kuchagua

Hakuna jibu moja la kuchagua modeli huria. Sehemu nzuri ya kuanzia ni kutumia kipengele cha kuchuja kwa kazi cha Azure AI Studio. Hii itakusaidia kuelewa ni aina gani za kazi ambazo modeli imefundishwa. Hugging Face pia ina LLM Leaderboard ambayo inaonyesha modeli zinazofanya vizuri zaidi kulingana na vipimo fulani.

Unapotafuta kulinganisha LLMs katika aina tofauti, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) ni rasilimali nyingine nzuri:

![Ubora wa Modeli](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.sw.png)  
Chanzo: Artificial Analysis

Ikiwa unafanya kazi kwenye kesi maalum ya matumizi, kutafuta matoleo yaliyorekebishwa ambayo yanazingatia eneo hilo hilo kunaweza kuwa na ufanisi. Kujaribu modeli huria nyingi ili kuona jinsi zinavyofanya kazi kulingana na matarajio yako na ya watumiaji wako ni mazoezi mazuri.

## Hatua Zifuatazo

Sehemu bora kuhusu miundo huria ni kwamba unaweza kuanza kufanya kazi nayo haraka. Angalia [Katalogi ya Modeli ya Azure AI Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), ambayo ina mkusanyiko maalum wa Hugging Face na modeli hizi tulizojadili hapa.

## Kujifunza hakuishii hapa, endelea na Safari

Baada ya kukamilisha somo hili, angalia [Mkusanyiko wa Kujifunza AI ya Kizazi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuongeza maarifa yako ya AI ya Kizazi!

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.