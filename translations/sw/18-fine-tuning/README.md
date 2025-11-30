<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "807f0d9fc1747e796433534e1be6a98a",
  "translation_date": "2025-10-17T21:16:02+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "sw"
}
-->
[![Mifano ya Chanzo Huria](../../../translated_images/18-lesson-banner.f30176815b1a5074fce9cceba317720586caa99e24001231a92fd04eeb54a121.sw.png)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Kuboresha LLM Yako

Kutumia mifano mikubwa ya lugha kujenga programu za AI zinazozalisha maudhui huja na changamoto mpya. Suala kuu ni kuhakikisha ubora wa majibu (usahihi na umuhimu) katika maudhui yanayozalishwa na mfano kwa ombi fulani la mtumiaji. Katika masomo ya awali, tulijadili mbinu kama uhandisi wa maelekezo na kizazi kilichoongezewa na urejeshaji ambazo zinajaribu kutatua tatizo kwa _kubadilisha maelekezo ya pembejeo_ kwa mfano uliopo.

Katika somo la leo, tunajadili mbinu ya tatu, **kuboresha**, ambayo inajaribu kushughulikia changamoto kwa _kufundisha upya mfano wenyewe_ kwa data ya ziada. Hebu tuingie kwenye maelezo.

## Malengo ya Kujifunza

Somo hili linaanzisha dhana ya kuboresha mifano ya lugha iliyokwisha kufundishwa, linachunguza faida na changamoto za mbinu hii, na linatoa mwongozo wa wakati na jinsi ya kutumia kuboresha ili kuboresha utendaji wa mifano yako ya AI inayozalisha maudhui.

Mwisho wa somo hili, unapaswa kuwa na uwezo wa kujibu maswali yafuatayo:

- Kuboresha mifano ya lugha ni nini?
- Ni lini, na kwa nini, kuboresha ni muhimu?
- Ninawezaje kuboresha mfano uliokwisha kufundishwa?
- Ni vikwazo gani vya kuboresha?

Tayari? Hebu tuanze.

## Mwongozo wa Picha

Unataka kupata picha kubwa ya kile tutakachojadili kabla ya kuanza? Angalia mwongozo huu wa picha unaoelezea safari ya kujifunza kwa somo hili - kutoka kujifunza dhana kuu na motisha ya kuboresha, hadi kuelewa mchakato na mbinu bora za kutekeleza kazi ya kuboresha. Hili ni somo la kuvutia la kuchunguza, kwa hivyo usisahau kuangalia ukurasa wa [Rasilimali](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) kwa viungo vya ziada vya kusaidia safari yako ya kujifunza kwa kujitegemea!

![Mwongozo wa Picha wa Kuboresha Mifano ya Lugha](../../../translated_images/18-fine-tuning-sketchnote.11b21f9ec8a703467a120cb79a28b5ac1effc8d8d9d5b31bbbac6b8640432e14.sw.png)

## Kuboresha mifano ya lugha ni nini?

Kwa ufafanuzi, mifano mikubwa ya lugha imekwisha kufundishwa kwa _kiasi kikubwa cha maandishi_ yaliyotolewa kutoka vyanzo mbalimbali ikiwa ni pamoja na mtandao. Kama tulivyojifunza katika masomo ya awali, tunahitaji mbinu kama _uhandisi wa maelekezo_ na _kizazi kilichoongezewa na urejeshaji_ ili kuboresha ubora wa majibu ya mfano kwa maswali ya mtumiaji ("maelekezo").

Mbinu maarufu ya uhandisi wa maelekezo inahusisha kutoa mwongozo zaidi kwa mfano juu ya kile kinachotarajiwa katika jibu ama kwa kutoa _maelekezo_ (mwongozo wa moja kwa moja) au _kutoa mifano michache_ (mwongozo wa moja kwa moja). Hii inajulikana kama _ujifunzaji wa mifano michache_ lakini ina vikwazo viwili:

- Vikomo vya tokeni za mfano vinaweza kuzuia idadi ya mifano unayoweza kutoa, na kupunguza ufanisi.
- Gharama za tokeni za mfano zinaweza kufanya kuwa ghali kuongeza mifano kwa kila maelekezo, na kupunguza kubadilika.

Kuboresha ni mazoezi ya kawaida katika mifumo ya kujifunza kwa mashine ambapo tunachukua mfano uliokwisha kufundishwa na kuufundisha upya kwa data mpya ili kuboresha utendaji wake kwenye kazi maalum. Katika muktadha wa mifano ya lugha, tunaweza kuboresha mfano uliokwisha kufundishwa _kwa seti ya mifano iliyochaguliwa kwa kazi fulani au uwanja wa maombi_ ili kuunda **mfano maalum** ambao unaweza kuwa sahihi zaidi na muhimu kwa kazi au uwanja huo maalum. Faida ya ziada ya kuboresha ni kwamba inaweza pia kupunguza idadi ya mifano inayohitajika kwa ujifunzaji wa mifano michache - kupunguza matumizi ya tokeni na gharama zinazohusiana.

## Ni lini na kwa nini tunapaswa kuboresha mifano?

Katika _muktadha huu_, tunapozungumzia kuboresha, tunarejelea kuboresha kwa **usimamizi** ambapo kufundisha upya kunafanywa kwa **kuongeza data mpya** ambayo haikuwa sehemu ya seti ya data ya mafunzo ya awali. Hii ni tofauti na mbinu ya kuboresha bila usimamizi ambapo mfano unafundishwa upya kwa data ya awali, lakini kwa vigezo tofauti vya hyper.

Jambo kuu la kukumbuka ni kwamba kuboresha ni mbinu ya juu inayohitaji kiwango fulani cha utaalamu ili kupata matokeo yanayotarajiwa. Ikiwa itafanywa vibaya, inaweza isitoe maboresho yanayotarajiwa, na inaweza hata kupunguza utendaji wa mfano kwa uwanja wako uliolengwa.

Kwa hivyo, kabla ya kujifunza "jinsi" ya kuboresha mifano ya lugha, unahitaji kujua "kwa nini" unapaswa kuchukua njia hii, na "ni lini" kuanza mchakato wa kuboresha. Anza kwa kujiuliza maswali haya:

- **Matumizi**: Je, ni _matumizi_ gani ya kuboresha? Ni kipengele gani cha mfano uliokwisha kufundishwa unataka kuboresha?
- **Njia Mbadala**: Je, umejaribu _mbinu nyingine_ kufikia matokeo yanayotarajiwa? Tumia mbinu hizo kuunda msingi wa kulinganisha.
  - Uhandisi wa maelekezo: Jaribu mbinu kama maelekezo ya mifano michache na mifano ya majibu ya maelekezo yanayofaa. Tathmini ubora wa majibu.
  - Kizazi Kilichoongezewa na Urejeshaji: Jaribu kuongeza maelekezo na matokeo ya maswali yaliyopatikana kwa kutafuta data yako. Tathmini ubora wa majibu.
- **Gharama**: Je, umebaini gharama za kuboresha?
  - Uwezo wa kubadilika - je, mfano uliokwisha kufundishwa unapatikana kwa kuboresha?
  - Juhudi - kwa kuandaa data ya mafunzo, kutathmini & kuboresha mfano.
  - Kompyuta - kwa kuendesha kazi za kuboresha, na kupeleka mfano ulioboreshwa.
  - Data - upatikanaji wa mifano ya ubora wa kutosha kwa athari ya kuboresha.
- **Faida**: Je, umethibitisha faida za kuboresha?
  - Ubora - je, mfano ulioboreshwa ulizidi msingi wa kulinganisha?
  - Gharama - je, inapunguza matumizi ya tokeni kwa kurahisisha maelekezo?
  - Uwezo wa kupanuka - je, unaweza kutumia tena mfano wa msingi kwa nyanja mpya?

Kwa kujibu maswali haya, unapaswa kuwa na uwezo wa kuamua ikiwa kuboresha ni njia sahihi kwa matumizi yako. Kwa kawaida, njia hii ni halali tu ikiwa faida zinazidi gharama. Mara unapojua kuendelea, ni wakati wa kufikiria _jinsi_ unavyoweza kuboresha mfano uliokwisha kufundishwa.

Unataka kupata maarifa zaidi juu ya mchakato wa kufanya maamuzi? Tazama [Kuboresha au kutokuboresha](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Tunawezaje kuboresha mfano uliokwisha kufundishwa?

Ili kuboresha mfano uliokwisha kufundishwa, unahitaji kuwa na:

- mfano uliokwisha kufundishwa wa kuboresha
- seti ya data ya kutumia kwa kuboresha
- mazingira ya mafunzo ya kuendesha kazi ya kuboresha
- mazingira ya kuhifadhi ya kupeleka mfano ulioboreshwa

## Kuboresha Kwa Vitendo

Rasilimali zifuatazo zinatoa mafunzo ya hatua kwa hatua ya kukuelekeza kupitia mfano halisi kwa kutumia mfano ulioteuliwa na seti ya data iliyochaguliwa. Ili kufanyia kazi mafunzo haya, unahitaji akaunti kwa mtoa huduma husika, pamoja na upatikanaji wa mfano na seti za data zinazohusika.

| Mtoa Huduma  | Mafunzo                                                                                                                                                                       | Maelezo                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Jinsi ya kuboresha mifano ya mazungumzo](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Jifunze kuboresha `gpt-35-turbo` kwa uwanja maalum ("msaidizi wa mapishi") kwa kuandaa data ya mafunzo, kuendesha kazi ya kuboresha, na kutumia mfano ulioboreshwa kwa uchambuzi.                                                                                                                                                                                                                                              |
| Azure OpenAI | [Mafunzo ya kuboresha GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Jifunze kuboresha mfano wa `gpt-35-turbo-0613` **kwenye Azure** kwa kuchukua hatua za kuunda & kupakia data ya mafunzo, kuendesha kazi ya kuboresha. Peleka & tumia mfano mpya.                                                                                                                                                                                                                                                                 |
| Hugging Face | [Kuboresha LLMs na Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Chapisho hili la blogu linakuelekeza kuboresha _LLM wazi_ (mfano: `CodeLlama 7B`) kwa kutumia maktaba ya [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst]) na seti za data wazi [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) kwenye Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Kuboresha LLMs na AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (au AutoTrain Advanced) ni maktaba ya python iliyotengenezwa na Hugging Face inayoruhusu kuboresha kwa kazi nyingi tofauti ikiwa ni pamoja na kuboresha LLM. AutoTrain ni suluhisho lisilo na msimbo na kuboresha kunaweza kufanywa kwenye wingu lako mwenyewe, kwenye Hugging Face Spaces au kwa ndani. Inasaidia GUI ya mtandao, CLI na mafunzo kupitia faili za usanidi za yaml.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Kazi

Chagua mojawapo ya mafunzo hapo juu na uyafanyie kazi. _Tunaweza kurudia toleo la mafunzo haya katika Jupyter Notebooks kwenye repo hii kwa marejeleo tu. Tafadhali tumia vyanzo vya asili moja kwa moja kupata matoleo ya hivi karibuni_.

## Kazi Nzuri! Endelea Kujifunza.

Baada ya kukamilisha somo hili, angalia mkusanyiko wetu wa [Kujifunza AI Inayozalisha Maudhui](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuongeza maarifa yako ya AI Inayozalisha Maudhui!

Hongera!! Umekamilisha somo la mwisho kutoka mfululizo wa v2 wa kozi hii! Usikome kujifunza na kujenga. \*\*Angalia ukurasa wa [RASILIMALI](RESOURCES.md?WT.mc_id=academic-105485-koreyst) kwa orodha ya mapendekezo ya ziada kwa mada hii tu.

Mfululizo wetu wa masomo wa v1 pia umesasishwa na kazi zaidi na dhana. Kwa hivyo chukua dakika moja kuboresha maarifa yako - na tafadhali [shiriki maswali na maoni yako](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) ili kutusaidia kuboresha masomo haya kwa jamii.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asilia katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.