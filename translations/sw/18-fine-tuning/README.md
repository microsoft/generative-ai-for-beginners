[![Mfano Wazi wa Chanzo](../../../translated_images/sw/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Kuimarisha LLM Yako

Kutumia mifano mikubwa ya lugha kujenga programu za AI zinazozalisha huleta changamoto mpya. Tatizo kuu ni kuhakikisha ubora wa majibu (usahihi na umuhimu) katika maudhui yanayozalishwa na mfano kwa ombi la mtumiaji fulani. Katika masomo yaliyopita, tulijadili mbinu kama uhandisi wa maelekezo na kizazi kilichoimarishwa kwa uvutaji ambacho kinajaribu kutatua tatizo kwa _kubadilisha maelekezo yaliyowekwa_ kwa mfano uliopo.

Katika somo la leo, tunajadili mbinu ya tatu, **kuimarisha zaidi**, ambayo inajaribu kushughulikia changamoto hiyo kwa _kurejesha mafunzo ya mfano wenyewe_ na data mpya. Hebu tuchunguze maelezo zaidi.

## Malengo ya Kujifunza

Somo hili linaleta wazo la kuimarisha zaidi mifano ya lugha iliyofunzwa awali, linaangalia faida na changamoto za mbinu hii, na hutoa mwongozo juu ya wakati na jinsi ya kutumia kuimarisha ili kuboresha utendaji wa mifano yako ya AI inayozalisha.

Mwisho wa somo hili, unapaswa kuwa na uwezo wa kujibu maswali yafuatayo:

- Kuimarisha zaidi ni nini katika mifano ya lugha?
- Lini, na kwa nini, kuimarisha zaidi ni muhimu?
- Ninawezaje kuimarisha mfano uliowekwa awali?
- Ni vikwazo gani vya kuimarisha zaidi?

Tayari? Hebu tuanze.

## Mwongozo Uliochora

Unataka kuelewa picha kubwa ya tutakachojifunza kabla ya kuingia undani? Angalia mwongozo huu uliyochorwa unaoelezea safari ya kujifunza kwa somo hili - kutoka kwa kujifunza dhana kuu na motisha ya kuimarisha zaidi, hadi kuelewa mchakato na mbinu bora za kutekeleza kazi ya kuimarisha. Hili ni somo la kuvutia kwa uchunguzi, hivyo usisahau kuangalia ukurasa wa [Rasilimali](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) kwa viungo vya ziada kusaidia safari yako ya kujifunza yenye mwongozo binafsi!

![Mwongozo uliyochora wa Kuimarisha Mifano ya Lugha](../../../translated_images/sw/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Kuimarisha zaidi ni nini katika mifano ya lugha?

Kwa ufafanuzi, mifano mikubwa ya lugha ni _iliyofunzwa awali_ na kiasi kikubwa cha maandishi kutoka vyanzo mbalimbali ikiwemo intaneti. Kama tulivyojifunza katika masomo yaliyopita, tunahitaji mbinu kama _uhandisi wa maelekezo_ na _kizazi kilichoimarishwa kwa uvutaji_ ili kuboresha ubora wa majibu ya mfano kwa maswali ya mtumiaji ("maelekezo").

Mbinu maarufu ya uhandisi wa maelekezo ni kumpa mfano mwongozo zaidi juu ya kinachotakiwa katika jibu kwa kutoa _maelekezo_ (mwongozo wazi) au _kumtoa baadhi ya mifano_ (mwongozo usio wazi). Hii huitwa _kujifunza kwa mifano michache_ lakini ina vikwazo viwili:

- Mipaka ya tokeni ya mfano inaweza kupunguza idadi ya mifano unayoweza kutoa, na kupunguza ufanisi.
- Gharama za tokeni za mfano zinaweza kufanya gharama kuwa kubwa kuongeza mifano kwa kila maelekezo, na kupunguza unyumbufu.

Kuimarisha zaidi ni mazoea ya kawaida katika mifumo ya mashine inayojifunza ambapo tunachukua mfano uliowekwa awali na kuurejesha mafunzo na data mpya ili kuboresha utendaji wake kwa kazi fulani. Katika muktadha wa mifano ya lugha, tunaweza kuimarisha mfano uliowekwa awali _na seti iliyochaguliwa ya mifano kwa kazi au eneo la matumizi fulani_ kuunda **mfano maalum** ambao unaweza kuwa sahihi zaidi na unaohusiana zaidi kwa kazi au eneo hilo. Faida ya pembeni ya kuimarisha zaidi ni kwamba pia inaweza kupunguza idadi ya mifano inayohitajika kwa kujifunza kwa mifano michache - kupunguza matumizi ya tokeni na gharama zinazohusiana.

## Lini na kwa nini tunapaswa kuimarisha zaidi mifano?

Katika _muktadha huu_, tunapotaja kuimarisha zaidi, tunarejelea **kuimarisha kwa usimamizi** ambapo urejeshaji wa mafunzo hufanywa kwa **kuongeza data mpya** ambayo haikuwa sehemu ya seti ya data ya mafunzo ya awali. Hii ni tofauti na mbinu isiyo na usimamizi ambapo mfano huwekwa mafunzo tena na data asilia, lakini kwa hyperparameter tofauti.

Kitu kikuu cha kukumbuka ni kwamba kuimarisha zaidi ni mbinu ya hali ya juu inayohitaji kiwango fulani cha utaalamu kupata matokeo yanayotarajiwa. Ikiwa itafanywa vibaya, inaweza isilete maboresho yanayotarajiwa, na hata kupunguza utendaji wa mfano kwa eneo lako linalolengwa.

Hivyo, kabla hujajifunza "jinsi" ya kuimarisha zaidi mifano ya lugha, unahitaji kujua "kwa nini" unapaswa kuchukua njia hii, na "lini" kuanza mchakato wa kuimarisha. Anza kwa kujiuliza maswali haya:

- **Matumizi**: Ni _matumizi gani_ ya kuimarisha unayo? Ni kipengele gani cha mfano ulioko unayotaka kuboresha?
- **Mbinu mbadala**: Je, umekuwa ukijaribu _mbinu nyingine_ kupata matokeo unayotaka? Zitumie kuanzisha msingi wa kulinganisha.
  - Uhandisi wa maelekezo: Jaribu mbinu kama maelekezo ya mifano michache yenye majibu husika. Tathmini ubora wa majibu.
  - Kizazi kilichoimarishwa kwa uvutaji: Jaribu kuongeza maelekezo na matokeo ya utafutaji kupitia data yako. Tathmini ubora wa majibu.
- **Gharama**: Je, umebaini gharama za kuimarisha zaidi?
  - Uwezekano wa kurekebisha - je mfano uliowekwa awali unapatikana kwa kuimarisha zaidi?
  - Juhudi - kwa kuandaa data ya mafunzo, kutathmini na kuboresha mfano.
  - Uwezeshaji wa kompyuta - kwa kuendesha kazi za kuimarisha, na kupeleka mfano ulioboreshwa
  - Data - upatikanaji wa mifano ya ubora wa kutosha kwa athari ya kuimarisha
- **Faida**: Je, umethibitisha faida za kuimarisha zaidi?
  - Ubora - je mfano ulioboreshwa ulizidi msingi?
  - Gharama - je inapunguza matumizi ya tokeni kwa kurahisisha maelekezo?
  - Uwezo wa kupanua - je unaweza kutumia mfano wa msingi kwa maeneo mapya?

Kwa kujibu maswali haya, unapaswa kuwa na uwezo wa kuamua kama kuimarisha zaidi ni mbinu sahihi kwa matumizi yako. Kiufupi, mbinu ni halali tu ikiwa faida zinazidi gharama. Mara tu unapobainisha kuendelea, ni wakati wa kufikiria _jinsi_ unavyoweza kuimarisha mfano uliowekwa awali.

Unataka kupata maarifa zaidi juu ya mchakato wa uamuzi? Tazama [Kuimarisha au kutoimarisha](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Tunawezaje kuimarisha mfano uliowekwa awali?

Ili kuimarisha mfano uliowekwa awali, unahitaji kuwa na:

- mfano uliowekwa awali wa kuimarisha
- seti ya data ya matumizi ya kuimarisha
- mazingira ya mafunzo kuendesha kazi ya kuimarisha
- mazingira ya kuhifadhi kupeleka mfano ulioboreshwa

## Kuimarisha Katika Microsoft Foundry

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ni mahali unapoimarisha, kupeleka, na kusimamia mifano maalum kwenye Azure leo (inachanganya yale yaliyokuwa Azure OpenAI Studio na Azure AI Studio). Kabla ya kuanzisha kazi, ni vyema kuelewa chaguzi Foundry linakupa - na mbinu bora ambazo jukwaa linapendekeza. Ndani ya mfumo, Foundry hutumia **LoRA (mfanano wa kiwango cha chini)** kuimarisha mifano kwa ufanisi, ambayo huifanya mafunzo kuwa ya haraka na nafuu zaidi kuliko kurekebisha kila uzito.

### Hatua 1: Chagua mbinu ya mafunzo

Foundry ina msaada wa mbinu tatu za kuimarisha. **Anza na SFT** - inashughulikia aina nyingi zaidi za matukio.

| Mbinu | Inayofanya | Wakati wa kuitumia |
| --- | --- | --- |
| **Kuimarisha Kwa Usimamizi (SFT)** | Huongeza mafunzo kwa jozi za mfano/mwisho ili mfano ujifunze kutoa majibu unayotaka. | Chaguo chaguo kwa kazi nyingi: utaalam wa eneo, utendaji wa kazi, mtindo na sauti, kufuata maelekezo, na mabadiliko ya lugha. |
| **Uboreshaji wa Mapendeleo ya Moja kwa Moja (DPO)** | Hujifunza kutoka kwa jozi za majibu _yanayopendelewa dhidi ya yasiyopendelewa_ kulingana na mapendeleo ya binadamu. | Kuboresha ubora wa jibu, usalama, na ulinganifu wakati una mrejesho wa kulinganisha. |
| **Kuimarisha Kwa Reinforcement (RFT)** | Inatumia ishara za zawadi kutoka kwa _wasimamizi_ kuboresha tabia ngumu kwa kujifunza kwa reinforcement. | Maeneo ya malengo, yenye uzito wa hoja (hisabati, kemia, fizikia) na majibu sahihi/siyosahihi wazi. Inahitaji utaalamu zaidi wa ML. |

### Hatua 2: Chagua daraja la mafunzo

Foundry inakuwezesha kuchagua jinsi na wapi mafunzo yataendeshwa:

- **Kawaida** - hufunza katika eneo la rasilimali yako na huhakikisha makazi ya data. Tumia wakati data lazima ibaki katika eneo fulani.
- **Ulimwenguni** - nafuu na haraka kwa kunyonya uwezo zaidi ya eneo lako (data na uzito hukopiwa hadi eneo la mafunzo). Chaguo nzuri wakati makazi ya data si sharti.
- **Mwanazuoni** - gharama ndogo zaidi, ikitumia uwezo usiotumika bila dhamana za ucheleweshaji/SLA (kazi zinaweza kusitishwa na kuanzishwa tena). Inafaa kwa majaribio.

### Hatua 3: Chagua mfano wa msingi

Mifano inayoweza kuimarishwa ni pamoja na OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini`, na `gpt-4.1-nano` (SFT; familia ya 4o/4.1 pia inasaidia DPO), mifano ya hoja `o4-mini` na `gpt-5` (RFT), pamoja na mifano ya chanzo wazi kama `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct`, na `gpt-oss-20b` (SFT kwenye rasilimali za Foundry). Kila wakati hakikisha kuangalia [Orodha ya mifano ya Kuimarisha](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) kwa mbinu zinazotolewa, maeneo, na upatikanaji.

> Foundry hutoa njia mbili: **bila seva** (bei ya matumizi, hakuna kibali cha GPU cha kusimamia, OpenAI na mifano iliyochaguliwa) na **kompyuta inayoendeshwa** (leta VM zako mwenyewe kupitia Azure Machine Learning kwa anuwai kubwa zaidi ya mifano). Watu wengi wanapaswa kuanza na isiyo na seva.

### Mbinu Bora za Foundry

- **Kipimo cha msingi kwanza.** Pima mfano wa msingi na uhandisi wa maelekezo na RAG _kabla_ ya kuimarisha, ili uweze kuonyesha faida.
- **Anza kidogo, kisha pandisha.** Anza na mifano 50-100 ya ubora wa juu kuthibitisha mbinu, kisha ongeza hadi 500+ kwa uzalishaji. Ubora hupita wingi - tofautisha mifano duni.
- **Panga data ipasavyo.** Faili za mafunzo na tathmini lazima ziwe JSONL, UTF-8 **na BOM**, chini ya 512 MB, zikitumia muundo wa ujumbe wa mazungumzo. Daima jumuisha faili ya tathmini ili uangalie mafunzo kupita kiasi.
- **Dumisha maelekezo ya mfumo wakati wa utabiri.** Tumia ujumbe huo wa mfumo ulio tumia wakati wa mafunzo unapoita mfano.
- **Tathmini vidokezo vya hali - usipeleke bila kufikiria.** Foundry huhifadhi epoksi tatu za mwisho kama vidokezo vya kuweza kupeleka; chagua kinachojumlisha vyema kwa kuangalia `train_loss` / `valid_loss` na usahihi wa tokeni.
- **Pima gharama ya tokeni sambamba na ubora** unapotathmini mfano ulioboreshwa dhidi ya msingi.
- **Rudia na kuimarisha mfululizo.** Unaweza kuimarisha mfano ulioboreshwa tayari na data mpya (inakubaliwa kwa mifano ya OpenAI).
- **Tazama gharama za kuhifadhi.** Mfano maalum ulipelekwa hulipishwa kwa saa, na upelekeaji usiotumika hufutwa baada ya siku 15 - safisha kile usichohitaji.

Fanya kupitia mafunzo ya hatua kwa hatua katika [Boresha mfano kwa kuimarisha zaidi](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst), na ona mwongozo wa [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) na [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst) unapokuwa tayari kwa mbinu nyingine.

## Kuimarisha Katika Vitendo

Rasilimali zifuatazo zinatoa mafunzo hatua kwa hatua yanayokuongoza kupitia mfano halisi kwa mfano unaoendeshwa kwa sasa na dataset iliyochaguliwa. Ili kufanya kazi nazo, unahitaji akaunti kwa muuzaji husika pamoja na upatikanaji wa mfano husika na dataset.

| Muuzaji     | Mafunzo                                                                                                                                                                       | Maelezo                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Jinsi ya kuimarisha mifano ya mazungumzo](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)     | Jifunze kuimarisha mfano wa mazungumzo wa OpenAI wa hivi karibuni kwa eneo fulani ("msaidizi wa mapishi") kwa kuandaa data ya mafunzo, kuendesha kazi ya kuimarisha, na kutumia mfano ulioboreshwa kwa utabiri.                                                                                                                                                                                                                                                               |
| Microsoft Foundry | [Boresha mfano kwa kuimarisha zaidi](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Jifunze kuimarisha mfano unaoendeshwa kwa sasa kama `gpt-4.1-mini` **kutumia Azure** na Microsoft Foundry: andaa na pakia data za mafunzo na tathmini, endesha kazi ya kuimarisha, kisha peleka na tumia mfano mpya.                                                                                                                                                                                                                                                               |

| Hugging Face | [Kufinyaza LLMs kwa Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Kifungu hiki cha blogu kinakuelekeza jinsi ya kufinyaza _open LLM_ (mfano: `CodeLlama 7B`) kwa kutumia maktaba ya [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) kwa kutumia [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) za wazi kwenye Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Kufinyaza LLMs kwa AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (au AutoTrain Advanced) ni maktaba ya python iliyotengenezwa na Hugging Face inayoruhusu kufinyaza kazi nyingi tofauti ikijumuisha kufinyaza LLM. AutoTrain ni suluhisho lisilo na msimbo na ufinyzaji unaweza kufanyika katika wingu lako mwenyewe, kwenye Hugging Face Spaces au kwa ndani (locally). Inasaidia GUI ya mtandao, CLI na mafunzo kupitia faili za usanidi za yaml.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Kufinyaza LLMs kwa Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth ni mfumo wazi wa chanzo unaounga mkono kufinyazwa LLM na kujifunza kwa kuzidisha (RL). Unsloth hufanya mafunzo ya ndani, tathmini, na utekelezaji kuwa rahisi kwa kutumia [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) tayari kwa matumizi. Pia inasaidia maandishi kwa sauti (TTS), BERT na mifano ya multimodal. Ili kuanza, soma mwongozo wao wa hatua kwa hatua wa [Kufinyaza LLMs](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Kazi ya Nyumbani

Chagua moja ya mafunzo yaliyotajwa hapo juu na yapitie. _Tunaweza kuiga toleo la mafunzo haya katika Jupyter Notebooks katika repoo hii kwa ajili ya rejea tu. Tafadhali tumia vyanzo asili moja kwa moja kupata matoleo ya hivi karibuni_.

## Kazi Njema! Endelea Kujifunza.

Baada ya kumaliza somo hili, angalia [Mkusanyiko wa Kujifunza AI ya Kutengeneza](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kuendelea kuongeza maarifa yako kuhusu AI ya Kutengeneza!

Hongera!! Umefanikiwa kumaliza somo la mwisho kutoka kwa mfululizo wa v2 kwa kozi hii! Usisahau kuendelea kujifunza na kujenga. \*\*Tafadhali angalia ukurasa wa [RASILIMALI](RESOURCES.md?WT.mc_id=academic-105485-koreyst) kwa orodha ya mapendekezo zaidi kuhusu mada hii tu.

Mfululizo wetu wa v1 wa masomo pia umeboreshwa na kazi za nyumbani na dhana zaidi. Kwa hiyo chukua dakika moja kufufua maarifa yako - na tafadhali [shirikisha maswali na maoni yako](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) kusaidia kuboresha masomo haya kwa jamii.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->