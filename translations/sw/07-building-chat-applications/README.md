<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5308963a56cfbad2d73b0fa99fe84b3",
  "translation_date": "2025-10-17T21:16:29+00:00",
  "source_file": "07-building-chat-applications/README.md",
  "language_code": "sw"
}
-->
# Kujenga Programu za Gumzo Zinazotumia AI ya Kizazi

[![Kujenga Programu za Gumzo Zinazotumia AI ya Kizazi](../../../translated_images/07-lesson-banner.a279b937f2843833fe28b4597f51bdef92d0ad03efee7ba52d0f166dea7574e5.sw.png)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Bofya picha hapo juu kutazama video ya somo hili)_

Sasa tumeona jinsi tunavyoweza kujenga programu za kizazi cha maandishi, hebu tuangalie programu za gumzo.

Programu za gumzo zimekuwa sehemu ya maisha yetu ya kila siku, zikitoa zaidi ya njia ya mawasiliano ya kawaida. Zinakuwa sehemu muhimu za huduma kwa wateja, msaada wa kiufundi, na hata mifumo ya ushauri wa hali ya juu. Inawezekana umepata msaada kutoka kwa programu ya gumzo hivi karibuni. Tunapojumuisha teknolojia za hali ya juu kama AI ya kizazi katika majukwaa haya, ugumu huongezeka na changamoto pia.

Maswali kadhaa yanayohitaji majibu ni:

- **Kujenga programu**. Je, tunawezaje kujenga kwa ufanisi na kuunganisha programu hizi zinazotumia AI kwa matumizi maalum?
- **Kufuatilia**. Baada ya kuzindua, tunawezaje kufuatilia na kuhakikisha kuwa programu zinafanya kazi kwa kiwango cha juu cha ubora, kwa upande wa utendaji na kufuata [kanuni sita za AI inayowajibika](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

Tunapoendelea zaidi katika enzi inayofafanuliwa na kiotomatiki na mwingiliano wa mashine na binadamu bila mshono, kuelewa jinsi AI ya kizazi inavyobadilisha upeo, kina, na uwezo wa programu za gumzo kunakuwa muhimu. Somo hili litachunguza vipengele vya usanifu vinavyounga mkono mifumo hii tata, kuchunguza mbinu za kuiboresha kwa kazi maalum za kikoa, na kutathmini vipimo na masuala muhimu ya kuhakikisha matumizi ya AI inayowajibika.

## Utangulizi

Somo hili linashughulikia:

- Mbinu za kujenga na kuunganisha programu za gumzo kwa ufanisi.
- Jinsi ya kutumia ubinafsishaji na uboreshaji kwa programu.
- Mikakati na masuala ya kufuatilia programu za gumzo kwa ufanisi.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- Eleza masuala ya kujenga na kuunganisha programu za gumzo katika mifumo iliyopo.
- Binafsisha programu za gumzo kwa matumizi maalum.
- Tambua vipimo muhimu na masuala ya kufuatilia na kudumisha ubora wa programu za gumzo zinazotumia AI.
- Hakikisha programu za gumzo zinatumia AI kwa uwajibikaji.

## Kuunganisha AI ya Kizazi katika Programu za Gumzo

Kuimarisha programu za gumzo kupitia AI ya kizazi si tu kuhusu kuzifanya kuwa na akili zaidi; ni kuhusu kuboresha usanifu wake, utendaji, na kiolesura cha mtumiaji ili kutoa uzoefu bora wa mtumiaji. Hii inahusisha kuchunguza misingi ya usanifu, ujumuishaji wa API, na masuala ya kiolesura cha mtumiaji. Sehemu hii inalenga kukupa ramani kamili ya kuvinjari mandhari haya magumu, iwe unazijumuisha katika mifumo iliyopo au unazijenga kama majukwaa ya pekee.

Mwisho wa sehemu hii, utakuwa na ujuzi unaohitajika kujenga na kuunganisha programu za gumzo kwa ufanisi.

### Chatbot au Programu ya Gumzo?

Kabla ya kuanza kujenga programu za gumzo, hebu tulinganishe 'chatbots' dhidi ya 'programu za gumzo zinazotumia AI,' ambazo zina majukumu na kazi tofauti. Kusudi kuu la chatbot ni kuendesha kazi maalum za mazungumzo, kama kujibu maswali yanayoulizwa mara kwa mara au kufuatilia kifurushi. Kwa kawaida inatawaliwa na mantiki inayotegemea sheria au algorithimu za AI tata. Kwa upande mwingine, programu ya gumzo inayotumia AI ni mazingira pana zaidi yaliyoundwa kuwezesha aina mbalimbali za mawasiliano ya kidijitali, kama gumzo la maandishi, sauti, na video kati ya watumiaji wa binadamu. Kipengele chake kinachofafanua ni ujumuishaji wa mfano wa AI ya kizazi unaosimulia mazungumzo ya kina, ya kibinadamu, ukizalisha majibu kulingana na aina mbalimbali za pembejeo na vidokezo vya muktadha. Programu ya gumzo inayotumia AI ya kizazi inaweza kushiriki katika mazungumzo ya kikoa wazi, kubadilika na muktadha wa mazungumzo yanayobadilika, na hata kutoa mazungumzo ya ubunifu au tata.

Jedwali hapa chini linaonyesha tofauti na kufanana muhimu ili kutusaidia kuelewa majukumu yao ya kipekee katika mawasiliano ya kidijitali.

| Chatbot                               | Programu ya Gumzo Inayotumia AI ya Kizazi |
| ------------------------------------- | ----------------------------------------- |
| Inalenga kazi maalum na inategemea sheria | Inatambua muktadha                        |
| Mara nyingi hujumuishwa katika mifumo mikubwa | Inaweza kuwa na chatbot moja au nyingi    |
| Inategemea kazi zilizopangwa           | Inajumuisha mifano ya AI ya kizazi        |
| Mawasiliano maalum na yaliyopangwa     | Ina uwezo wa mazungumzo ya kikoa wazi     |

### Kutumia Vipengele Vilivyotengenezwa Tayari na SDKs na APIs

Unapojenga programu ya gumzo, hatua nzuri ya kwanza ni kutathmini kilichopo tayari. Kutumia SDKs na APIs kujenga programu za gumzo ni mkakati wenye faida kwa sababu mbalimbali. Kwa kuunganisha SDKs na APIs zilizoandikwa vizuri, unaiweka programu yako kimkakati kwa mafanikio ya muda mrefu, ukishughulikia masuala ya upanuzi na matengenezo.

- **Inaharakisha mchakato wa maendeleo na kupunguza gharama**: Kutegemea vipengele vilivyotengenezwa tayari badala ya mchakato wa gharama kubwa wa kuvitengeneza mwenyewe hukuruhusu kuzingatia vipengele vingine vya programu yako unavyoweza kuona kuwa muhimu zaidi, kama mantiki ya biashara.
- **Utendaji bora**: Unapojenga vipengele kutoka mwanzo, hatimaye utajiuliza "Je, inapanuka? Je, programu hii ina uwezo wa kushughulikia ongezeko la ghafla la watumiaji?" SDK na API zinazotunzwa vizuri mara nyingi zina suluhisho zilizojengwa kwa masuala haya.
- **Matengenezo rahisi**: Sasisho na maboresho ni rahisi kusimamia kwani API na SDK nyingi zinahitaji tu sasisho la maktaba wakati toleo jipya linatolewa.
- **Ufikiaji wa teknolojia ya kisasa**: Kutumia mifano iliyoboreshwa na kufundishwa kwenye seti kubwa za data hutoa programu yako uwezo wa lugha ya asili.

Kupata utendaji wa SDK au API kwa kawaida kunahusisha kupata ruhusa ya kutumia huduma zinazotolewa, ambayo mara nyingi hufanyika kupitia matumizi ya ufunguo wa kipekee au tokeni ya uthibitishaji. Tutatumia Maktaba ya Python ya OpenAI kuchunguza jinsi hii inavyoonekana. Unaweza pia kujaribu mwenyewe katika [notebook ya OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) au [notebook ya Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) kwa somo hili.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

chat_completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Suggest two titles for an instructional lesson on chat applications for generative AI."}])
```

Mfano hapo juu unatumia mfano wa GPT-3.5 Turbo kukamilisha ombi, lakini angalia kuwa ufunguo wa API umewekwa kabla ya kufanya hivyo. Ungepata hitilafu ikiwa usingeweka ufunguo.

## Uzoefu wa Mtumiaji (UX)

Kanuni za jumla za UX zinatumika kwa programu za gumzo, lakini hapa kuna masuala ya ziada yanayokuwa muhimu hasa kutokana na vipengele vya kujifunza kwa mashine vinavyohusika.

- **Mfumo wa kushughulikia utata**: Mifano ya AI ya kizazi mara nyingine huzalisha majibu ya utata. Kipengele kinachoruhusu watumiaji kuuliza ufafanuzi kinaweza kusaidia iwapo watakutana na tatizo hili.
- **Uhifadhi wa muktadha**: Mifano ya hali ya juu ya AI ya kizazi ina uwezo wa kukumbuka muktadha ndani ya mazungumzo, ambayo inaweza kuwa mali muhimu kwa uzoefu wa mtumiaji. Kuwapa watumiaji uwezo wa kudhibiti na kusimamia muktadha huboresha uzoefu wa mtumiaji, lakini huanzisha hatari ya kuhifadhi taarifa nyeti za mtumiaji. Masuala ya muda wa kuhifadhi taarifa hizi, kama kuanzisha sera ya uhifadhi, yanaweza kusawazisha hitaji la muktadha dhidi ya faragha.
- **Ubinafsishaji**: Kwa uwezo wa kujifunza na kubadilika, mifano ya AI hutoa uzoefu wa kibinafsi kwa mtumiaji. Kubinafsisha uzoefu wa mtumiaji kupitia vipengele kama maelezo ya mtumiaji si tu humfanya mtumiaji ajisikie kueleweka, lakini pia husaidia katika kutafuta majibu maalum, na kuunda mwingiliano wa ufanisi na wa kuridhisha.

Mfano mmoja wa ubinafsishaji ni mipangilio ya "Maelekezo Maalum" katika ChatGPT ya OpenAI. Inakuruhusu kutoa taarifa kuhusu wewe ambayo inaweza kuwa muktadha muhimu kwa maombi yako. Hapa kuna mfano wa maelekezo maalum.

![Mipangilio ya Maelekezo Maalum katika ChatGPT](../../../translated_images/custom-instructions.b96f59aa69356fcfed456414221919e8996f93c90c20d0d58d1bc0221e3c909f.sw.png)

Maelezo haya ya "wasifu" yanamshawishi ChatGPT kuunda mpango wa somo kuhusu orodha zilizounganishwa. Angalia kuwa ChatGPT inazingatia kuwa mtumiaji anaweza kutaka mpango wa somo wa kina zaidi kulingana na uzoefu wake.

![Ombi katika ChatGPT kwa mpango wa somo kuhusu orodha zilizounganishwa](../../../translated_images/lesson-plan-prompt.cc47c488cf1343df5d67aa796a1acabca32c380e5b782971e289f6ab8b21cf5a.sw.png)

### Mfumo wa Ujumbe wa Mfumo wa Microsoft kwa Mifano Mikubwa ya Lugha

[Microsoft imetoa mwongozo](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) wa kuandika ujumbe wa mfumo mzuri wakati wa kuzalisha majibu kutoka kwa LLMs uliogawanywa katika maeneo 4:

1. Kufafanua ni nani mfano unalenga, pamoja na uwezo wake na mapungufu.
2. Kufafanua muundo wa matokeo ya mfano.
3. Kutoa mifano maalum inayoonyesha tabia inayokusudiwa ya mfano.
4. Kutoa vizuizi vya ziada vya tabia.

### Ufikivu

Iwe mtumiaji ana ulemavu wa kuona, kusikia, mwendo, au utambuzi, programu ya gumzo iliyoundwa vizuri inapaswa kutumika na wote. Orodha ifuatayo inavunja vipengele maalum vinavyolenga kuboresha ufikivu kwa ulemavu mbalimbali wa mtumiaji.

- **Vipengele kwa Ulemavu wa Kuona**: Mandhari yenye utofauti wa juu na maandishi yanayoweza kubadilishwa ukubwa, utangamano wa wasomaji wa skrini.
- **Vipengele kwa Ulemavu wa Kusikia**: Kazi za maandishi-kwa-sauti na sauti-kwa-maandishi, vidokezo vya kuona kwa arifa za sauti.
- **Vipengele kwa Ulemavu wa Mwendo**: Msaada wa urambazaji wa kibodi, amri za sauti.
- **Vipengele kwa Ulemavu wa Utambuzi**: Chaguo za lugha rahisi.

## Ubinafsishaji na Uboreshaji kwa Mifano ya Lugha Maalum ya Kikoa

Fikiria programu ya gumzo inayofahamu istilahi ya kampuni yako na kutarajia maswali maalum ambayo msingi wake wa watumiaji mara nyingi huwa nayo. Kuna njia kadhaa zinazostahili kutajwa:

- **Kutumia mifano ya DSL**. DSL inasimama kwa lugha maalum ya kikoa. Unaweza kutumia mfano wa DSL unaoitwa hivyo uliofundishwa kwenye kikoa maalum kuelewa dhana zake na hali zake.
- **Tumia uboreshaji**. Uboreshaji ni mchakato wa kufundisha zaidi mfano wako kwa data maalum.

## Ubinafsishaji: Kutumia DSL

Kutumia mifano ya lugha maalum ya kikoa (DSL Models) kunaweza kuboresha ushirikiano wa mtumiaji kwa kutoa mwingiliano maalum, unaofaa muktadha. Ni mfano uliofundishwa au ulioboreshwa kuelewa na kuzalisha maandishi yanayohusiana na uwanja maalum, tasnia, au somo. Chaguo za kutumia mfano wa DSL zinaweza kutofautiana kutoka kufundisha moja kutoka mwanzo, hadi kutumia zilizopo kupitia SDKs na APIs. Chaguo jingine ni uboreshaji, ambao unahusisha kuchukua mfano uliokwisha kufundishwa na kuubadilisha kwa kikoa maalum.

## Ubinafsishaji: Tumia Uboreshaji

Uboreshaji mara nyingi huzingatiwa wakati mfano uliokwisha kufundishwa unashindwa katika kikoa maalum au kazi maalum.

Kwa mfano, maswali ya matibabu ni magumu na yanahitaji muktadha mwingi. Wakati mtaalamu wa matibabu anapogundua mgonjwa, inategemea mambo mbalimbali kama mtindo wa maisha au hali zilizopo, na inaweza hata kutegemea majarida ya matibabu ya hivi karibuni kuthibitisha utambuzi wao. Katika hali kama hizi za kina, programu ya gumzo ya AI ya matumizi ya jumla haiwezi kuwa chanzo cha kuaminika.

### Hali: programu ya matibabu

Fikiria programu ya gumzo iliyoundwa kusaidia wataalamu wa matibabu kwa kutoa marejeleo ya haraka kwa miongozo ya matibabu, mwingiliano wa dawa, au matokeo ya utafiti wa hivi karibuni.

Mfano wa matumizi ya jumla unaweza kuwa wa kutosha kwa kujibu maswali ya msingi ya matibabu au kutoa ushauri wa jumla, lakini inaweza kuwa na changamoto kwa yafuatayo:

- **Kesi maalum au ngumu sana**. Kwa mfano, mtaalamu wa neva anaweza kuuliza programu, "Ni mbinu bora za sasa za kudhibiti kifafa kisichotibika kwa watoto?"
- **Ukosefu wa maendeleo ya hivi karibuni**. Mfano wa matumizi ya jumla unaweza kuwa na changamoto kutoa jibu la sasa linalojumuisha maendeleo ya hivi karibuni katika neva na famasia.

Katika hali kama hizi, kuboresha mfano kwa seti ya data maalum ya matibabu kunaweza kuboresha kwa kiasi kikubwa uwezo wake wa kushughulikia maswali haya magumu ya matibabu kwa usahihi na kwa kuaminika. Hii inahitaji ufikiaji wa seti kubwa na inayofaa ya data inayowakilisha changamoto na maswali maalum ya kikoa yanayohitaji kushughulikiwa.

## Masuala ya Uzoefu wa Gumzo wa AI wa Ubora wa Juu

Sehemu hii inaelezea vigezo vya programu za gumzo za "ubora wa juu," ambavyo vinajumuisha kukamata vipimo vinavyoweza kuchukuliwa hatua na kufuata mfumo unaotumia teknolojia ya AI kwa uwajibikaji.

### Vipimo Muhimu

Ili kudumisha utendaji wa ubora wa juu wa programu, ni muhimu kufuatilia vipimo muhimu na masuala. Vipimo hivi si tu vinahakikisha utendaji wa programu lakini pia vinatathmini ubora wa mfano wa AI na uzoefu wa mtumiaji. Hapa chini kuna orodha inayoshughulikia vipimo vya msingi, AI, na uzoefu wa mtumiaji vya kuzingatia.

| Kipimo                        | Ufafanuzi                                                                                                             | Masuala kwa Msanidi wa Gumzo                                              |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Uptime**                    | Inapima muda ambao programu inafanya kazi na inapatikana kwa watumiaji.                                                | Utapunguza vipi muda wa kutofanya kazi?                                   |
| **Response Time**             | Muda unaochukuliwa na programu kujibu swali la mtumiaji.                                                              | Utaboreshaje usindikaji wa maswali ili kuboresha muda wa majibu?          |
| **Precision**                 | Uwiano wa utabiri sahihi wa chanya kwa jumla ya utabiri wa chanya.                                                     | Utathibitishaje usahihi wa mfano wako?                                    |
| **Recall (Sensitivity)**      | Uwiano wa utabiri sahihi wa chanya kwa idadi halisi ya chanya.                                                         | Utapima na kuboresha vipi recall?                                         |
| **F1 Score**                  | Wastani wa harmonic wa precision na recall, unaosawazisha biashara kati ya zote mbili.                                 | Lengo lako la F1 Score ni nini? Utasawazishaje precision na recall?       |
| **Perplexity**                | Inapima jinsi usambazaji wa uwezekano uliotabiriwa na mfano unavyolingana na usambazaji halisi wa data.                 | Utapunguza vipi perplexity?                                               |
| **User Satisfaction Metrics** | Inapima mtazamo wa mtumiaji kuhusu programu. Mara nyingi hukusanywa kupitia tafiti.                                     | Utakusanya mara ngapi maoni ya mtumiaji? Utabadilika vipi kulingana nayo? |
| **Error Rate**                | Kiwango ambacho mfano unakosea katika kuelewa au kutoa matokeo.                                                        | Una mikakati gani ya kupunguza viwango
| **Utambuzi wa Mambo Yasiyo ya Kawaida** | Zana na mbinu za kutambua mifumo isiyo ya kawaida ambayo haifuati tabia inayotarajiwa. | Utajibu vipi mambo yasiyo ya kawaida? |

### Kutekeleza Mazoea ya AI ya Uwajibikaji katika Programu za Gumzo

Mbinu ya Microsoft kuhusu AI ya Uwajibikaji imebainisha kanuni sita ambazo zinapaswa kuongoza maendeleo na matumizi ya AI. Hapa chini kuna kanuni hizo, maana yake, na mambo ambayo msanidi wa programu ya gumzo anapaswa kuzingatia na kwa nini ni muhimu kuyazingatia.

| Kanuni                 | Maana ya Microsoft                                   | Mambo ya Kuzingatia kwa Msanidi wa Programu ya Gumzo                  | Kwa Nini Ni Muhimu                                                                      |
| ---------------------- | ---------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Usawa                  | Mifumo ya AI inapaswa kuwatendea watu wote kwa usawa. | Hakikisha programu ya gumzo haibagui kulingana na data ya mtumiaji.   | Kujenga uaminifu na ushirikiano miongoni mwa watumiaji; kuepuka athari za kisheria.      |
| Uaminifu na Usalama    | Mifumo ya AI inapaswa kufanya kazi kwa uaminifu na usalama. | Tekeleza majaribio na hatua za kuzuia ili kupunguza makosa na hatari. | Inahakikisha kuridhika kwa mtumiaji na kuzuia madhara yanayoweza kutokea.               |
| Faragha na Usalama     | Mifumo ya AI inapaswa kuwa salama na kuheshimu faragha. | Tekeleza usimbaji wa hali ya juu na hatua za kulinda data.            | Kulinda data nyeti ya mtumiaji na kufuata sheria za faragha.                            |
| Ushirikishi            | Mifumo ya AI inapaswa kuwawezesha wote na kuwahusisha watu. | Buni UI/UX inayoweza kufikiwa na rahisi kutumia kwa hadhira mbalimbali. | Inahakikisha watu wengi zaidi wanaweza kutumia programu kwa ufanisi.                   |
| Uwazi                  | Mifumo ya AI inapaswa kueleweka.                     | Toa nyaraka wazi na maelezo ya sababu za majibu ya AI.                | Watumiaji wana uwezekano mkubwa wa kuamini mfumo ikiwa wanaweza kuelewa jinsi maamuzi yanavyofanywa. |
| Uwajibikaji            | Watu wanapaswa kuwajibika kwa mifumo ya AI.          | Weka mchakato wazi wa kukagua na kuboresha maamuzi ya AI.             | Inawezesha uboreshaji endelevu na hatua za kurekebisha iwapo kuna makosa.               |

## Kazi

Tazama [kazi](../../../07-building-chat-applications/python). Itakupitisha kwenye mfululizo wa mazoezi kuanzia kuendesha maelekezo ya kwanza ya gumzo, hadi kuainisha na kufupisha maandishi na zaidi. Kumbuka kwamba kazi zinapatikana katika lugha tofauti za programu!

## Kazi Nzuri! Endelea na Safari

Baada ya kukamilisha somo hili, angalia [mkusanyiko wa Kujifunza AI ya Kizazi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuongeza maarifa yako kuhusu AI ya Kizazi!

Nenda kwenye Somo la 8 ili kuona jinsi unavyoweza kuanza [kujenga programu za utafutaji](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya kiasili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.