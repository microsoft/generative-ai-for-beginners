<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8b2d4bb727c877ebf9edff8623d16b9",
  "translation_date": "2025-09-06T10:22:24+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "sw"
}
-->
[![Open Source Models](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.sw.png)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## Utangulizi

Ulimwengu wa LLM za chanzo huria ni wa kusisimua na unabadilika kila mara. Somo hili linakusudia kutoa muhtasari wa kina kuhusu mifano ya chanzo huria. Ikiwa unatafuta maelezo kuhusu jinsi mifano ya wamiliki inavyolinganishwa na mifano ya chanzo huria, nenda kwenye somo la ["Kuchunguza na Kulinganisha LLM Tofauti"](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Somo hili pia litagusia mada ya kurekebisha lakini maelezo zaidi yanaweza kupatikana kwenye somo la ["Kurekebisha LLM"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Malengo ya Kujifunza

- Kupata uelewa wa mifano ya chanzo huria  
- Kuelewa faida za kufanya kazi na mifano ya chanzo huria  
- Kuchunguza mifano ya chanzo huria inayopatikana kwenye Hugging Face na Azure AI Studio  

## Mifano ya Chanzo Huria ni Nini?

Programu ya chanzo huria imekuwa na mchango mkubwa katika ukuaji wa teknolojia katika nyanja mbalimbali. Open Source Initiative (OSI) imefafanua [vigezo 10 vya programu](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) ili kuainishwa kama chanzo huria. Kanuni ya chanzo lazima isambazwe wazi chini ya leseni iliyoidhinishwa na OSI.

Ingawa maendeleo ya LLM yana vipengele vinavyofanana na maendeleo ya programu, mchakato si sawa kabisa. Hii imeleta mijadala mingi katika jamii kuhusu ufafanuzi wa chanzo huria katika muktadha wa LLM. Ili mfano ulingane na ufafanuzi wa jadi wa chanzo huria, taarifa zifuatazo zinapaswa kupatikana hadharani:

- Seti za data zilizotumika kufundisha mfano.  
- Uzito kamili wa mfano kama sehemu ya mafunzo.  
- Kanuni ya tathmini.  
- Kanuni ya kurekebisha.  
- Uzito kamili wa mfano na vipimo vya mafunzo.  

Kwa sasa, kuna mifano michache tu inayolingana na vigezo hivi. [Mfano wa OLMo ulioundwa na Taasisi ya Allen ya Akili ya Kijumla (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) ni mojawapo inayolingana na kategoria hii.

Kwa somo hili, tutarejelea mifano kama "mifano huria" kuanzia sasa kwani huenda haifanyi kazi na vigezo vilivyotajwa hapo juu wakati wa kuandika.

## Faida za Mifano Huria

**Inaweza Kubadilishwa Sana** - Kwa kuwa mifano huria hutolewa na maelezo ya kina ya mafunzo, watafiti na watengenezaji wanaweza kurekebisha mambo ya ndani ya mfano. Hii inawezesha uundaji wa mifano maalum sana ambayo imeboreshwa kwa kazi maalum au eneo la utafiti. Baadhi ya mifano ni kama kizazi cha kanuni, operesheni za hisabati, na biolojia.

**Gharama** - Gharama kwa kila tokeni ya kutumia na kupeleka mifano hii ni ya chini kuliko ile ya mifano ya wamiliki. Wakati wa kujenga programu za Generative AI, inapaswa kufanyika tathmini ya utendaji dhidi ya bei kulingana na matumizi yako.

![Model Cost](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.sw.png)  
Chanzo: Artificial Analysis  

**Uwezo wa Kubadilika** - Kufanya kazi na mifano huria kunakuwezesha kubadilika kwa kutumia mifano tofauti au kuichanganya. Mfano wa hili ni [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst) ambapo mtumiaji anaweza kuchagua mfano unaotumika moja kwa moja kwenye kiolesura cha mtumiaji:

![Choose Model](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.sw.png)

## Kuchunguza Mifano Huria Tofauti

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), iliyotengenezwa na Meta ni mfano huria ulioboreshwa kwa programu za mazungumzo. Hii ni kutokana na mbinu yake ya kurekebisha, ambayo ilijumuisha kiasi kikubwa cha mazungumzo na maoni ya binadamu. Kwa mbinu hii, mfano huzalisha matokeo yanayolingana zaidi na matarajio ya binadamu, ambayo hutoa uzoefu bora wa mtumiaji.

Baadhi ya mifano iliyoboreshwa ya Llama ni pamoja na [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), ambayo inazingatia Kijapani na [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), ambayo ni toleo lililoboreshwa la mfano wa msingi.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) ni mfano huria unaolenga sana utendaji wa juu na ufanisi. Inatumia mbinu ya Mixture-of-Experts ambayo inachanganya kundi la mifano maalum ya wataalamu katika mfumo mmoja ambapo kulingana na pembejeo, mifano fulani huchaguliwa kutumika. Hii inafanya hesabu kuwa bora zaidi kwani mifano inashughulikia tu pembejeo ambazo imebobea.

Baadhi ya mifano iliyoboreshwa ya Mistral ni pamoja na [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), ambayo inazingatia uwanja wa matibabu na [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), ambayo inafanya hesabu za hisabati.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) ni LLM iliyoundwa na Taasisi ya Ubunifu wa Teknolojia (**TII**). Falcon-40B ilifundishwa kwa vigezo bilioni 40 ambavyo vimeonyeshwa kufanya vizuri zaidi kuliko GPT-3 kwa bajeti ndogo ya hesabu. Hii ni kutokana na matumizi yake ya algoriti ya FlashAttention na multiquery attention ambayo inawezesha kupunguza mahitaji ya kumbukumbu wakati wa kutoa matokeo. Kwa muda huu wa kutoa matokeo uliopunguzwa, Falcon-40B inafaa kwa programu za mazungumzo.

Baadhi ya mifano iliyoboreshwa ya Falcon ni pamoja na [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), msaidizi aliyejengwa juu ya mifano huria na [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), ambayo hutoa utendaji wa juu zaidi kuliko mfano wa msingi.

## Jinsi ya Kuchagua

Hakuna jibu moja la kuchagua mfano huria. Mahali pazuri pa kuanzia ni kutumia kipengele cha kuchuja kwa kazi cha Azure AI Studio. Hii itakusaidia kuelewa ni aina gani za kazi mfano umefundishwa. Hugging Face pia ina LLM Leaderboard ambayo inaonyesha mifano inayofanya vizuri zaidi kulingana na vipimo fulani.

Unapotafuta kulinganisha LLMs katika aina tofauti, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) ni rasilimali nyingine nzuri:

![Model Quality](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.sw.png)  
Chanzo: Artificial Analysis  

Ikiwa unafanya kazi kwenye matumizi maalum, kutafuta mifano iliyoboreshwa inayolenga eneo hilo inaweza kuwa na ufanisi. Kujaribu mifano huria mbalimbali ili kuona jinsi inavyofanya kazi kulingana na matarajio yako na ya watumiaji wako ni mazoezi mazuri.

## Hatua Zifuatazo

Sehemu bora kuhusu mifano huria ni kwamba unaweza kuanza kufanya kazi nayo haraka. Angalia [Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), ambayo ina mkusanyiko maalum wa Hugging Face na mifano hii tuliyojadili hapa.

## Kujifunza hakuishii hapa, endelea na Safari

Baada ya kukamilisha somo hili, angalia [Mkusanyiko wa Kujifunza Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuongeza maarifa yako ya Generative AI!

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.