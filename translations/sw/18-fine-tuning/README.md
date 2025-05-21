<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "68664f7e754a892ae1d8d5e2b7bd2081",
  "translation_date": "2025-05-20T07:55:32+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "sw"
}
-->
# Kuboresha LLM Yako

Kutumia mifano mikubwa ya lugha kujenga programu za AI zinazozalisha maudhui kunakuja na changamoto mpya. Tatizo kuu ni kuhakikisha ubora wa majibu (usahihi na umuhimu) katika maudhui yanayozalishwa na mfano kwa ombi la mtumiaji. Katika masomo yaliyopita, tulijadili mbinu kama uhandisi wa maombi na kizazi kinachoongezewa na urejeshaji ambazo zinajaribu kutatua tatizo kwa _kubadilisha ingizo la ombi_ kwa mfano uliopo.

Katika somo la leo, tunajadili mbinu ya tatu, **kuboresha**, ambayo inajaribu kushughulikia changamoto kwa _kufundisha upya mfano yenyewe_ na data ya ziada. Hebu tuingie kwenye maelezo.

## Malengo ya Kujifunza

Somo hili linaanzisha dhana ya kuboresha mifano ya lugha iliyo tayari kufundishwa, inachunguza faida na changamoto za njia hii, na inatoa mwongozo juu ya lini na jinsi ya kutumia kuboresha ili kuboresha utendaji wa mifano yako ya AI inayozalisha maudhui.

Mwisho wa somo hili, unapaswa kuwa na uwezo wa kujibu maswali yafuatayo:

- Kuboresha kwa mifano ya lugha ni nini?
- Lini, na kwa nini, kuboresha ni muhimu?
- Ninawezaje kuboresha mfano ulio tayari kufundishwa?
- Je, ni mipaka gani ya kuboresha?

Tayari? Hebu tuanze.

## Mwongozo wa Picha

Unataka kupata picha kubwa ya kile tutakachojadili kabla hatujaingia ndani? Angalia mwongozo huu wa picha unaoelezea safari ya kujifunza kwa somo hili - kutoka kujifunza dhana kuu na motisha ya kuboresha, kuelewa mchakato na mbinu bora za kutekeleza kazi ya kuboresha. Hii ni mada ya kuvutia ya kuchunguza, kwa hivyo usisahau kuangalia ukurasa wa [Rasilimali](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) kwa viungo vya ziada vya kusaidia safari yako ya kujifunza kwa kujiongoza!

## Kuboresha kwa mifano ya lugha ni nini?

Kwa ufafanuzi, mifano mikubwa ya lugha imefundishwa awali kwenye idadi kubwa ya maandiko yanayotoka vyanzo mbalimbali ikiwemo mtandao. Kama tulivyojifunza katika masomo yaliyopita, tunahitaji mbinu kama _uhandisi wa maombi_ na _kizazi kinachoongezewa na urejeshaji_ ili kuboresha ubora wa majibu ya mfano kwa maswali ya mtumiaji ("maombi").

Mbinu maarufu ya uhandisi wa maombi inahusisha kutoa mwongozo zaidi kwa mfano juu ya kile kinachotarajiwa katika jibu ama kwa kutoa _maelekezo_ (mwongozo wa wazi) au _kutoa mifano michache_ (mwongozo wa siri). Hii inajulikana kama _kujifunza kwa mifano michache_ lakini ina mapungufu mawili:

- Mipaka ya tokeni za mfano inaweza kuzuia idadi ya mifano unayoweza kutoa, na kupunguza ufanisi.
- Gharama za tokeni za mfano zinaweza kufanya iwe ghali kuongeza mifano kwa kila ombi, na kupunguza kubadilika.

Kuboresha ni mazoezi ya kawaida katika mifumo ya kujifunza kwa mashine ambapo tunachukua mfano ulio tayari kufundishwa na kuufundisha upya na data mpya ili kuboresha utendaji wake kwenye kazi maalum. Katika muktadha wa mifano ya lugha, tunaweza kuboresha mfano ulio tayari kufundishwa _na seti iliyopangwa ya mifano kwa kazi au uwanja wa maombi fulani_ ili kuunda **mfano maalum** ambao unaweza kuwa sahihi zaidi na muhimu kwa kazi au uwanja huo maalum. Faida ya upande ya kuboresha ni kwamba inaweza pia kupunguza idadi ya mifano inayohitajika kwa kujifunza kwa mifano michache - kupunguza matumizi ya tokeni na gharama zinazohusiana.

## Lini na kwa nini tunapaswa kuboresha mifano?

Katika _muktadha huu_, tunapozungumzia kuboresha, tunarejelea kuboresha kwa **usimamizi** ambapo kufundisha upya kunafanywa kwa **kuongeza data mpya** ambayo haikuwa sehemu ya seti ya awali ya mafunzo. Hii ni tofauti na njia ya kuboresha isiyo na usimamizi ambapo mfano unafundishwa upya kwenye data ya awali, lakini kwa vigezo tofauti vya hyper.

Jambo kuu la kukumbuka ni kwamba kuboresha ni mbinu ya juu ambayo inahitaji kiwango fulani cha utaalamu ili kupata matokeo yanayotakiwa. Ikiwa imefanywa vibaya, inaweza isitoe maboresho yanayotarajiwa, na inaweza hata kudhoofisha utendaji wa mfano kwa uwanja wako ulioainishwa.

Kwa hivyo, kabla ya kujifunza "jinsi" ya kuboresha mifano ya lugha, unahitaji kujua "kwa nini" unapaswa kuchukua njia hii, na "lini" kuanza mchakato wa kuboresha. Anza kwa kujiuliza maswali haya:

- **Matumizi**: Je, ni _matumizi_ gani yako ya kuboresha? Ni kipengele gani cha mfano wa sasa ulio tayari kufundishwa unataka kuboresha?
- **Njia mbadala**: Je, umejaribu _mbinu nyingine_ kufikia matokeo yanayotakiwa? Zitumia kuunda msingi wa kulinganisha.
  - Uhandisi wa maombi: Jaribu mbinu kama maombi ya mifano michache na mifano ya majibu ya maombi husika. Tathmini ubora wa majibu.
  - Kizazi Kinachoongezewa na Urejeshaji: Jaribu kuongeza maombi na matokeo ya maswali yaliyorejeshwa kwa kutafuta data yako. Tathmini ubora wa majibu.
- **Gharama**: Je, umebaini gharama za kuboresha?
  - Uwezo wa kurekebisha - je, mfano ulio tayari kufundishwa unapatikana kwa kuboresha?
  - Jitihada - kwa kuandaa data ya mafunzo, kutathmini na kuboresha mfano.
  - Kompyuta - kwa kuendesha kazi za kuboresha, na kupeleka mfano ulioboreshwa
  - Data - upatikanaji wa mifano ya kutosha yenye ubora kwa athari ya kuboresha
- **Faida**: Je, umethibitisha faida za kuboresha?
  - Ubora - je, mfano ulioboreshwa ulizidi msingi?
  - Gharama - je, inapunguza matumizi ya tokeni kwa kurahisisha maombi?
  - Upanuzi - je, unaweza kutumia tena mfano wa msingi kwa maeneo mapya?

Kwa kujibu maswali haya, unapaswa kuwa na uwezo wa kuamua ikiwa kuboresha ni njia sahihi kwa matumizi yako. Kwa kawaida, njia hii ni halali tu ikiwa faida zinazidi gharama. Mara unapoamua kuendelea, ni wakati wa kufikiria _jinsi_ unavyoweza kuboresha mfano ulio tayari kufundishwa.

Unataka kupata ufahamu zaidi juu ya mchakato wa kufanya maamuzi? Tazama [Kuboresha au kutokuboresha](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Tunawezaje kuboresha mfano ulio tayari kufundishwa?

Ili kuboresha mfano ulio tayari kufundishwa, unahitaji kuwa na:

- mfano ulio tayari kufundishwa wa kuboresha
- seti ya data ya kutumia kwa kuboresha
- mazingira ya mafunzo ya kuendesha kazi ya kuboresha
- mazingira ya mwenyeji ya kupeleka mfano ulioboreshwa

## Kuboresha Katika Vitendo

Rasilimali zifuatazo zinatoa mafunzo ya hatua kwa hatua ya kukutembeza kupitia mfano halisi kwa kutumia mfano uliochaguliwa na seti ya data iliyopangwa. Ili kufanya kazi kupitia mafunzo haya, unahitaji akaunti kwa mtoa huduma maalum, pamoja na upatikanaji wa mfano na seti za data husika.

| Mtoa huduma  | Mafunzo                                                                                                                                                                       | Maelezo                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Jinsi ya kuboresha mifano ya mazungumzo](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Jifunze kuboresha `gpt-35-turbo` kwa uwanja maalum ("msaidizi wa mapishi") kwa kuandaa data ya mafunzo, kuendesha kazi ya kuboresha, na kutumia mfano ulioboreshwa kwa kutambua.                                                                                                                                                                                                                                              |
| Azure OpenAI | [Mafunzo ya kuboresha GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Jifunze kuboresha mfano wa `gpt-35-turbo-0613` **kwenye Azure** kwa kuchukua hatua za kuunda na kupakia data ya mafunzo, kuendesha kazi ya kuboresha. Peleka na tumia mfano mpya.                                                                                                                                                                                                                                                                 |
| Hugging Face | [Kuboresha LLMs na Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Chapisho hili la blogu linakutembeza kuboresha _LLM wazi_ (mfano: `CodeLlama 7B`) kwa kutumia maktaba ya [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) & [Kujifunza kwa Kuimarisha kwa Transformer (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst]) na [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) kwenye Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Kuboresha LLMs na AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (au AutoTrain Advanced) ni maktaba ya python iliyotengenezwa na Hugging Face inayoruhusu kuboresha kwa kazi nyingi tofauti ikiwa ni pamoja na kuboresha LLM. AutoTrain ni suluhisho lisilo na msimbo na kuboresha kunaweza kufanywa kwenye wingu lako mwenyewe, kwenye Hugging Face Spaces au ndani ya nchi. Inasaidia GUI ya msingi wa wavuti, CLI na mafunzo kupitia faili za usanidi za yaml.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Kazi

Chagua moja ya mafunzo hapo juu na pitia. _Tunaweza kurudia toleo la mafunzo haya katika Jupyter Notebooks katika hifadhi hii kwa marejeleo tu. Tafadhali tumia vyanzo asili moja kwa moja kupata matoleo ya hivi karibuni_.

## Kazi Nzuri! Endelea Kujifunza.

Baada ya kumaliza somo hili, angalia mkusanyiko wetu wa [Kujifunza AI Inayozalisha Maudhui](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuinua maarifa yako ya AI Inayozalisha Maudhui!

Hongera!! Umehitimisha somo la mwisho kutoka kwa mfululizo wa v2 wa kozi hii! Usikome kujifunza na kujenga. **Angalia ukurasa wa [RASILIMALI](RESOURCES.md?WT.mc_id=academic-105485-koreyst) kwa orodha ya mapendekezo ya ziada kwa mada hii tu.

Mfululizo wetu wa masomo wa v1 pia umesasishwa na kazi zaidi na dhana. Kwa hivyo chukua dakika moja kusasisha maarifa yako - na tafadhali [shiriki maswali na maoni yako](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) ili kutusaidia kuboresha masomo haya kwa jamii.

**Kanusho**: 
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwepo kwa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatuwajibiki kwa kutokuelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.