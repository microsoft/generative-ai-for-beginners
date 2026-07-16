[![Modeli za Chanzo Huria](../../../translated_images/sw/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Kurekebisha LLM Yako Kwa Umakini

Kutumia mifano mikubwa ya lugha kujenga programu za AI zinazotengeneza maudhui kunakuja na changamoto mpya. Tatizo kuu ni kuhakikisha ubora wa majibu (usalama na uhusiano) katika maudhui yanayotengenezwa na mfano kwa ombi la mtumiaji. Katika masomo ya awali, tulijadili mbinu kama uhandisi wa maelekezo na uzalishaji unaosaidiwa na urejeshaji ambao hujaribu kutatua tatizo kwa _kubadilisha maelekezo ya kuingia_ kwa mfano uliopo.

Katika somo la leo, tunajadili mbinu ya tatu, **kurekebisha kwa umakini**, ambayo hujaribu kushughulikia changamoto kwa _kufunza tena mfano yenyewe_ kwa data za ziada. Hebu tuzingatie maelezo ya kina.

## Malengo ya Kujifunza

Somo hili linaanzisha dhana ya kurekebisha kwa umakini kwa mifano ya lugha iliyoandaliwa awali, linachunguza faida na changamoto za mbinu hii, na linatoa mwongozo wa lini na jinsi ya kutumia kurekebisha kwa umakini kuboresha utendaji wa mifano yako ya AI inayozalisha maudhui.

Mwisho wa somo hili, unapaswa uwezo wa kujibu maswali yafuatayo:

- Kurekebisha kwa umakini ni nini kwa mifano ya lugha?
- Lini, na kwa nini, kurekebisha kwa umakini ni muhimu?
- Ninawezaje kurekebisha mfano uliotanguliwa na kufunzwa?
- Ni vikwazo gani vya kurekebisha kwa umakini?

Tayari? Hebu tuanze.

## Mwongozo Uliopigwa Picha

Unataka kuona picha kubwa ya yale tutakayojifunza kabla ya kuanza? Angalia mwongozo huu uliopigwa picha unaoelezea safari ya kujifunza kwa somo hili - kutoka kujifunza dhana kuu na motisha ya kurekebisha kwa umakini, hadi kuelewa mchakato na mbinu bora za kutekeleza kazi ya kurekebisha kwa umakini. Hili ni somo lenye mvuto wa kipekee kwa uchunguzi, usisahau kutembelea ukurasa wa [Rasilimali](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) kwa viungo zaidi vya kuunga mkono safari yako ya kujifunza kwa kujiongoza mwenyewe!

![Mwongozo Uliopigwa Picha wa Kurekebisha Mifano ya Lugha](../../../translated_images/sw/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Kurekebisha kwa umakini ni nini kwa mifano ya lugha?

Kwa ufafanuzi, mifano mikubwa ya lugha ni _iliyonafunzwa awali_ kwenye kiasi kikubwa cha maandishi yanayotokana na vyanzo mbalimbali ikijumuisha mtandao wa intaneti. Kama tulivyojifunza katika masomo ya awali, tunahitaji mbinu kama _uhandisi wa maelekezo_ na _uzalishaji unaosaidiwa na urejeshaji_ kuboresha ubora wa majibu ya mfano kwa maswali ya mtumiaji ("maelekezo").

Mbinu maarufu ya uhandisi wa maelekezo ni kumpa mfano mwongozo zaidi juu ya kile kinachotarajiwa katika jibu kwa kutoa _maelekezo_ (mwongozo wa wazi) au _kumpa mifano michache_ (mwongozo wa siri). Hii huitwa _ujifunzaji wa mifano michache_ lakini ina vikwazo viwili:

- Vizingiti vya tokeni vya mfano vinaweza kupunguza idadi ya mifano unayoweza kutoa, na kupunguza ufanisi.
- Gharama za tokeni za mfano zinaweza kufanya kuwa ghali kuongeza mifano kwa kila maelekezo, na kupunguza utegemezi.

Kurekebisha kwa umakini ni mazoezi ya kawaida katika mifumo ya kujifunza mashine ambapo tunachukua mfano uliotanguliwa na kurekebisha tena kwa data mpya ili kuboresha utendaji wake kwenye kazi fulani. Katika muktadha wa mifano ya lugha, tunaweza kurekebisha mfano uliotanguliwa _kwa seti iliyochaguliwa ya mifano kwa kazi fulani au eneo la matumizi_ ili kuunda **mfano maalum** ambao unaweza kuwa sahihi na unaohusiana zaidi kwa kazi au eneo hilo. Faida ya pembeni ya kurekebisha kwa umakini ni kwamba pia inaweza kupunguza idadi ya mifano inayohitajika kwa ujifunzaji wa mifano michache - kupunguza matumizi ya tokeni na gharama zinazohusiana.

## Lini na kwa nini tunapaswa kurekebisha mifano kwa umakini?

Katika _muktadha huu_, tunapozungumzia kurekebisha kwa umakini, tunarejelea **kurekebisha kwa umakini wa usimamizi** ambapo funzo jipya huendeshwa kwa **kuongeza data mpya** ambayo haikuwa sehemu ya seti ya mafunzo ya awali. Hii ni tofauti na mbinu ya kurekebisha kwa umakini isiyo na usimamizi ambapo mfano hufunzwa tena kwa data ya awali, lakini na vigezo tofauti.

Jambo kuu la kukumbuka ni kwamba kurekebisha kwa umakini ni mbinu ya hali ya juu ambayo inahitaji kiwango fulani cha utaalamu kupata matokeo yanayotarajiwa. Ikiwa itafanywa vibaya, inaweza isitoa maboresho yanayotarajiwa, na hata kupunguza utendaji wa mfano kwa eneo lako linalolengwa.

Hivyo, kabla hujajifunza "jinsi" ya kurekebisha mifano ya lugha kwa umakini, unahitaji kujua "kwanini" unapaswa kuchukua njia hii, na "lini" kuanza mchakato wa kurekebisha kwa umakini. Anza kwa kujiuliza maswali haya:

- **Matumizi**: Ni matumizi gani ya _kurekebisha kwa umakini_ unayotaka kufanya? Ni kipengele gani cha mfano uliotanguliwa unaotaka kuboresha?
- **Mbadala**: Je, umeshajaribu _mbinu nyingine_ kupata matokeo yanayotarajiwa? Zitumi ili kuweka msingi wa kulinganisha.
  - Uhandisi wa maelekezo: Jaribu mbinu kama maelekezo ya mifano michache yenye mifano ya majibu yanayohusiana. Tathmini ubora wa majibu.
  - Uzalishaji Unaosaidiwa na Urejeshaji: Jaribu kuongeza maelekezo na matokeo ya utafutaji yanayopatikana kwa kusaka data zako. Tathmini ubora wa majibu.
- **Gharama**: Je, umebaini gharama za kurekebisha kwa umakini?
  - Inaweza kurekebishwa - Je, mfano uliotanguliwa upo tayari kwa kurekebishwa?
  - Jitihada - kwa kuandaa data ya mafunzo, kutathmini & kuboresha mfano.
  - Kompyuta - kwa kuendesha kazi za kurekebisha kwa umakini, na kupeleka mfano uliorekebishwa
  - Data - upatikanaji wa mifano ya ubora wa kutosha kwa athari za kurekebisha kwa umakini
- **Faida**: Je, umehakikisha faida za kurekebisha kwa umakini?
  - Ubora - Je, mfano uliorekebishwa ulikuwa bora kuliko msingi?
  - Gharama - Je, hupunguzia matumizi ya tokeni kwa kurahisisha maelekezo?
  - Uwezo wa kubadilisha - Je, unaweza kutumia tena mfano wa msingi kwa maeneo mapya?

Kwa kujibu maswali haya, unapaswa kuwa na uwezo wa kuamua kama kurekebisha kwa umakini ni mbinu sahihi kwa matumizi yako. Kwa kweli, mbinu ni halali tu ikiwa faida ni zaidi ya gharama. Mara tu unapokuwa tayari kuendelea, ni wakati wa kufikiria _jinsi_ unavyoweza kurekebisha mfano uliotanguliwa.

Unataka kupata maarifa zaidi juu ya mchakato wa kufanya maamuzi? Tazama [Kurekebisha au kutorekecha?](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Tunawezaje kurekebisha mfano uliotanguliwa?

Ili kurekebisha mfano uliotanguliwa, unahitaji kuwa na:

- mfano uliotanguliwa wa kurekebisha
- seti ya data ya kutumia kwa kurekebisha
- mazingira ya mafunzo kuendesha kazi ya kurekebisha
- mazingira ya mwenyeji kupeleka mfano uliorekebishwa

## Kurekebisha Katika Matendo

> **Kumbuka:** `gpt-35-turbo` / `gpt-3.5-turbo`, zinazotajwa katika baadhi ya mafunzo hapa chini, zimesitishwa kwa uamuzi na kurekebisha. Ikiwa unaanza kazi mpya ya kurekebisha leo, lenga mfano unaounga mkono sasa - kwa mfano `gpt-4o-mini` au `gpt-4.1-mini`. Angalia [Orodha ya mifano ya kurekebishwa](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) kwa seti ya sasa ya mifano inayoweza kurekebishwa. Dhana na hatua katika mafunzo haya bado zinatumika.

Rasilimali zifuatazo zinatoa mafunzo hatua kwa hatua kukuelekeza kupitia mfano halisi ukitumia mfano uliochaguliwa na seti ya data iliyochaguliwa. Ili kufanya mafunzo haya, unahitaji akaunti kwa mtoa huduma maalum, pamoja na upatikanaji wa mfano na seti za data husika.

| Mtoa Huduma | Mafunzo                                                                                                                                                                      | Maelezo                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Jinsi ya kurekebisha mifano ya mazungumzo](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst) | Jifunze kurekebisha `gpt-35-turbo` kwa eneo maalum ("msaidizi wa mapishi") kwa kuandaa data ya mafunzo, kuendesha kazi ya kurekebisha, na kutumia mfano uliorekebishwa kwa uamuzi.                                                                                                                                                                                                                                                 |
| Azure OpenAI | [Mafunzo ya kurekebisha GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst) | Jifunze kurekebisha mfano `gpt-35-turbo-0613` **kwa Azure** kwa kuchukua hatua za kuunda na kupakia data za mafunzo, kuendesha kazi ya kurekebisha. Peleka na tumia mfano mpya.                                                                                                                                                                                                                                                    |
| Hugging Face | [Kurekebisha LLMs na Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                              | Chapisho hili la blogu linakuongoza jinsi ya kurekebisha _LLM huru_ (mfano: `CodeLlama 7B`) ukitumia maktaba ya [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) kwa seti za data huru kwenye Hugging Face.                                                                        |
|              |                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 🤗 AutoTrain | [Kurekebisha LLMs na AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                        | AutoTrain (au AutoTrain Advanced) ni maktaba ya python iliyotengenezwa na Hugging Face inayoruhusu kurekebisha kwa mafanikio kwa kazi tofauti nyingi ikiwa ni pamoja na kurekebisha LLM. AutoTrain ni suluhisho la bila msimbo na kurekebisha kunaweza kufanywa katika wingu lako mwenyewe, kwenye Hugging Face Spaces au eneo lako. Inaunga mkono GUI ya wavuti, CLI na mafunzo kupitia faili za usanidi za yaml.                                                                            |
|              |                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 🦥 Unsloth | [Kurekebisha LLMs na Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                           | Unsloth ni mfumo wa chanzo wazi unaounga mkono kurekebisha LLM na kujifunza kwa kuimarisha (RL). Unsloth hurahisisha mafunzo ya ndani, tathmini, na utoaji kwa kutumia [daftari](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) tayari kwa matumizi. Pia inaunga mkono maandishi-kuyabadilisha-sauti (TTS), BERT na mifano ya multimodal. Ili kuanza, soma [Mwongozo wa Kurekebisha LLMs](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) hatua kwa hatua.                                          |
|              |                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
## Kazi ya Nyumbani

Chagua moja ya mafunzo yaliyopo hapo juu na uyatumie. _Huenda tukafanikisha toleo la mafunzo haya kwenye Jupyter Notebooks katika hifadhi hii kwa ajili ya rejeleo tu. Tafadhali tumia vyanzo asilia moja kwa moja kupata matoleo ya hivi karibuni_.

## Kazi Nzuri! Endelea Kujifunza.

Baada ya kumaliza somo hili, tembelea mkusanyiko wetu wa [Kujifunza AI Inayozalisha](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kuendelea kuinua maarifa yako ya AI Inayozalisha!

Hongera!! Umeimaliza somo la mwisho kutoka mfululizo wa v2 kwa kozi hii! Usisite kujifunza na kujenga. \*\*Angalia ukurasa wa [RASILIMALI](RESOURCES.md?WT.mc_id=academic-105485-koreyst) kwa orodha ya mapendekezo ya ziada kwa mada hii pekee.

Mfululizo wetu wa v1 wa masomo pia umeboreshwa kwa kazi zaidi na dhana zaidi. Hivyo chukua dakika moja kuhuisha maarifa yako - na tafadhali [shirikisha maswali na maoni yako](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) kutusaidia kuboresha masomo haya kwa jamii.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->