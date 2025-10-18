<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6b7629b8ee4d7d874a27213e903d86a7",
  "translation_date": "2025-10-18T02:26:17+00:00",
  "source_file": "02-exploring-and-comparing-different-llms/README.md",
  "language_code": "lt"
}
-->
# Tyrinėjimas ir skirtingų LLM palyginimas

[![Tyrinėjimas ir skirtingų LLM palyginimas](../../../translated_images/02-lesson-banner.ef94c84979f97f60f07e27d905e708cbcbdf78707120553ccab27d91c947805b.lt.png)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Spustelėkite aukščiau esančią nuotrauką, kad peržiūrėtumėte šios pamokos vaizdo įrašą_

Ankstesnėje pamokoje aptarėme, kaip generatyvinis dirbtinis intelektas keičia technologijų pasaulį, kaip veikia dideli kalbos modeliai (LLM) ir kaip verslas – kaip mūsų startuolis – gali juos pritaikyti savo poreikiams ir augti! Šiame skyriuje mes lyginsime ir kontrastuosime skirtingus didelius kalbos modelius (LLM), kad geriau suprastume jų privalumus ir trūkumus.

Kitas mūsų startuolio kelionės žingsnis – ištirti dabartinį LLM kraštovaizdį ir suprasti, kurie modeliai yra tinkami mūsų poreikiams.

## Įvadas

Šioje pamokoje aptarsime:

- Skirtingus LLM tipus dabartiniame kraštovaizdyje.
- Modelių testavimą, iteravimą ir palyginimą jūsų poreikiams Azure platformoje.
- Kaip diegti LLM.

## Mokymosi tikslai

Baigę šią pamoką, galėsite:

- Pasirinkti tinkamą modelį savo poreikiams.
- Suprasti, kaip testuoti, iteruoti ir gerinti modelio veikimą.
- Žinoti, kaip verslai diegia modelius.

## Supraskite skirtingus LLM tipus

LLM gali būti klasifikuojami pagal jų architektūrą, mokymo duomenis ir naudojimo paskirtį. Šių skirtumų supratimas padės mūsų startuoliui pasirinkti tinkamą modelį konkrečiam scenarijui ir suprasti, kaip testuoti, iteruoti ir gerinti veikimą.

Yra daugybė skirtingų LLM modelių, o jūsų pasirinkimas priklauso nuo to, kam juos ketinate naudoti, kokius duomenis turite, kiek esate pasiruošę investuoti ir kitų veiksnių.

Priklausomai nuo to, ar ketinate naudoti modelius tekstui, garsui, vaizdo įrašams, vaizdų generavimui ir pan., galite pasirinkti skirtingą modelio tipą.

- **Garsas ir kalbos atpažinimas**. Šiam tikslui puikiai tinka Whisper tipo modeliai, nes jie yra universalūs ir skirti kalbos atpažinimui. Jie mokomi įvairiais garso duomenimis ir gali atlikti daugiakalbį kalbos atpažinimą. Sužinokite daugiau apie [Whisper tipo modelius čia](https://platform.openai.com/docs/models/whisper?WT.mc_id=academic-105485-koreyst).

- **Vaizdų generavimas**. Vaizdų generavimui DALL-E ir Midjourney yra du gerai žinomi pasirinkimai. DALL-E siūlo Azure OpenAI. [Skaitykite daugiau apie DALL-E čia](https://platform.openai.com/docs/models/dall-e?WT.mc_id=academic-105485-koreyst) ir taip pat 9 skyriuje šioje mokymo programoje.

- **Teksto generavimas**. Dauguma modelių yra mokomi teksto generavimui, ir jūs turite didelį pasirinkimą nuo GPT-3.5 iki GPT-4. Jie skiriasi kainomis, o GPT-4 yra brangiausias. Verta apsilankyti [Azure OpenAI žaidimų aikštelėje](https://oai.azure.com/portal/playground?WT.mc_id=academic-105485-koreyst), kad įvertintumėte, kurie modeliai geriausiai atitinka jūsų poreikius pagal galimybes ir kainą.

- **Daugiarūšis**. Jei norite dirbti su įvairių tipų duomenimis įvestyje ir išvestyje, galite apsvarstyti modelius, tokius kaip [gpt-4 turbo su vizija arba gpt-4o](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models?WT.mc_id=academic-105485-koreyst) – naujausi OpenAI modelių leidimai – kurie sujungia natūralios kalbos apdorojimą su vizualiniu supratimu, leidžiant sąveikauti per daugiarūšes sąsajas.

Pasirinkus modelį, gaunate tam tikras pagrindines galimybes, kurios gali būti nepakankamos. Dažnai turite įmonės specifinius duomenis, kuriuos kažkaip reikia pateikti LLM. Yra keletas skirtingų būdų, kaip tai padaryti, apie tai daugiau sužinosite kitose sekcijose.

### Pagrindiniai modeliai prieš LLM

Terminas „Pagrindinis modelis“ buvo [sukurtas Stanfordo tyrėjų](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) ir apibrėžtas kaip dirbtinio intelekto modelis, atitinkantis tam tikrus kriterijus, tokius kaip:

- **Jie mokomi naudojant nesupervizuotą mokymąsi arba savarankišką mokymąsi**, tai reiškia, kad jie mokomi naudojant nepažymėtus daugiarūšius duomenis ir jiems nereikia žmogaus anotacijų ar duomenų žymėjimo mokymo procesui.
- **Jie yra labai dideli modeliai**, pagrįsti labai giliomis neuronų tinklais, mokomais milijardais parametrų.
- **Jie paprastai skirti būti „pagrindu“ kitiems modeliams**, tai reiškia, kad jie gali būti naudojami kaip pradinis taškas kitiems modeliams, kurie gali būti sukurti ant jų, pavyzdžiui, atliekant smulkius patobulinimus.

![Pagrindiniai modeliai prieš LLM](../../../translated_images/FoundationModel.e4859dbb7a825c94b284f17eae1c186aabc21d4d8644331f5b007d809cf8d0f2.lt.png)

Vaizdo šaltinis: [Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Norėdami dar labiau paaiškinti šį skirtumą, paimkime ChatGPT kaip pavyzdį. Pirmoji ChatGPT versija buvo sukurta remiantis GPT-3.5 modeliu kaip pagrindiniu modeliu. Tai reiškia, kad OpenAI naudojo tam tikrus pokalbių duomenis, kad sukurtų pritaikytą GPT-3.5 versiją, kuri buvo specializuota gerai veikti pokalbių scenarijuose, tokiuose kaip pokalbių robotai.

![Pagrindinis modelis](../../../translated_images/Multimodal.2c389c6439e0fc51b0b7b226d95d7d900d372ae66902d71b8ce5ec4951b8efbe.lt.png)

Vaizdo šaltinis: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Atvirojo kodo prieš nuosavybės modelius

Kitas būdas klasifikuoti LLM yra pagal tai, ar jie yra atvirojo kodo, ar nuosavybės.

Atvirojo kodo modeliai yra viešai prieinami ir gali būti naudojami bet kieno. Juos dažnai pateikia įmonė, kuri juos sukūrė, arba mokslinių tyrimų bendruomenė. Šiuos modelius galima peržiūrėti, modifikuoti ir pritaikyti įvairiems LLM naudojimo atvejams. Tačiau jie ne visada yra optimizuoti gamybos naudojimui ir gali būti ne tokie efektyvūs kaip nuosavybės modeliai. Be to, atvirojo kodo modelių finansavimas gali būti ribotas, jie gali būti neprižiūrimi ilgą laiką arba neatnaujinami pagal naujausius tyrimus. Populiarių atvirojo kodo modelių pavyzdžiai yra [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html?WT.mc_id=academic-105485-koreyst), [Bloom](https://huggingface.co/bigscience/bloom) ir [LLaMA](https://llama.meta.com).

Nuosavybės modeliai yra įmonės valdomi modeliai, kurie nėra viešai prieinami. Šie modeliai dažnai yra optimizuoti gamybos naudojimui. Tačiau jų negalima peržiūrėti, modifikuoti ar pritaikyti skirtingiems naudojimo atvejams. Be to, jie ne visada yra nemokami ir gali reikalauti prenumeratos ar mokėjimo už naudojimą. Taip pat vartotojai neturi kontrolės dėl duomenų, naudojamų modelio mokymui, todėl jie turi pasitikėti modelio savininku, kad būtų užtikrintas duomenų privatumas ir atsakingas dirbtinio intelekto naudojimas. Populiarių nuosavybės modelių pavyzdžiai yra [OpenAI modeliai](https://platform.openai.com/docs/models/overview?WT.mc_id=academic-105485-koreyst), [Google Bard](https://sapling.ai/llm/bard?WT.mc_id=academic-105485-koreyst) arba [Claude 2](https://www.anthropic.com/index/claude-2?WT.mc_id=academic-105485-koreyst).

### Įterpimas prieš vaizdų generavimą prieš tekstų ir kodų generavimą

LLM taip pat gali būti klasifikuojami pagal jų generuojamą išvestį.

Įterpimai yra modelių rinkinys, galintis konvertuoti tekstą į skaitinę formą, vadinamą įterpimu, kuris yra skaitinė įvesties teksto reprezentacija. Įterpimai palengvina mašinoms suprasti žodžių ar sakinių tarpusavio ryšius ir gali būti naudojami kaip įvestys kitiems modeliams, tokiems kaip klasifikavimo modeliai ar klasterizavimo modeliai, kurie geriau veikia su skaitiniais duomenimis. Įterpimo modeliai dažnai naudojami perkėlimo mokymuisi, kai modelis kuriamas pakaitiniam uždaviniui, kuriam yra gausu duomenų, o tada modelio svoriai (įterpimai) yra panaudojami kitoms užduotims. Šios kategorijos pavyzdys yra [OpenAI įterpimai](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Įterpimas](../../../translated_images/Embedding.c3708fe988ccf76073d348483dbb7569f622211104f073e22e43106075c04800.lt.png)

Vaizdų generavimo modeliai yra modeliai, kurie generuoja vaizdus. Šie modeliai dažnai naudojami vaizdų redagavimui, sintezei ir vertimui. Vaizdų generavimo modeliai dažnai mokomi didelėmis vaizdų duomenų bazėmis, tokiomis kaip [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), ir gali būti naudojami naujiems vaizdams generuoti arba esamiems vaizdams redaguoti naudojant įterpimą, superrezoliuciją ir spalvinimo technikas. Pavyzdžiai: [DALL-E-3](https://openai.com/dall-e-3?WT.mc_id=academic-105485-koreyst) ir [Stable Diffusion modeliai](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst).

![Vaizdų generavimas](../../../translated_images/Image.349c080266a763fd255b840a921cd8fc526ed78dc58708fa569ff1873d302345.lt.png)

Teksto ir kodo generavimo modeliai yra modeliai, kurie generuoja tekstą arba kodą. Šie modeliai dažnai naudojami teksto santraukų sudarymui, vertimui ir klausimų atsakymui. Teksto generavimo modeliai dažnai mokomi didelėmis teksto duomenų bazėmis, tokiomis kaip [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), ir gali būti naudojami naujam tekstui generuoti arba atsakyti į klausimus. Kodo generavimo modeliai, tokie kaip [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), dažnai mokomi didelėmis kodų duomenų bazėmis, tokiomis kaip GitHub, ir gali būti naudojami naujam kodui generuoti arba esamų kodų klaidoms taisyti.

![Teksto ir kodo generavimas](../../../translated_images/Text.a8c0cf139e5cc2a0cd3edaba8d675103774e6ddcb3c9fc5a98bb17c9a450e31d.lt.png)

### Kodavimo-dekodavimo prieš tik dekodavimo modelius

Norėdami aptarti skirtingus LLM architektūros tipus, pasinaudokime analogija.

Įsivaizduokite, kad jūsų vadovas davė jums užduotį parengti viktoriną studentams. Turite du kolegas: vienas atsakingas už turinio kūrimą, o kitas – už jo peržiūrą.

Turinio kūrėjas yra kaip tik dekodavimo modelis, jis gali pažvelgti į temą ir tai, ką jau parašėte, ir tada sukurti kursą remdamasis tuo. Jie labai gerai kuria įdomų ir informatyvų turinį, tačiau nėra labai geri suprasti temą ir mokymosi tikslus. Kai kurie dekodavimo modelių pavyzdžiai yra GPT šeimos modeliai, tokie kaip GPT-3.

Recenzentas yra kaip tik kodavimo modelis, jis žiūri į parašytą kursą ir atsakymus, pastebėdamas ryšį tarp jų ir suprasdamas kontekstą, tačiau jis nėra geras kuriant turinį. Kodavimo modelio pavyzdys būtų BERT.

Įsivaizduokite, kad galime turėti ir tokį asmenį, kuris galėtų kurti ir peržiūrėti viktoriną – tai yra kodavimo-dekodavimo modelis. Kai kurie pavyzdžiai būtų BART ir T5.

### Paslauga prieš modelį

Dabar pakalbėkime apie skirtumą tarp paslaugos ir modelio. Paslauga yra produktas, kurį siūlo debesų paslaugų teikėjas ir kuris dažnai yra modelių, duomenų ir kitų komponentų derinys. Modelis yra pagrindinis paslaugos komponentas ir dažnai yra pagrindinis modelis, pvz., LLM.

Paslaugos dažnai optimizuojamos gamybos naudojimui ir dažnai yra lengviau naudojamos nei modeliai, naudojant grafinę vartotojo sąsają. Tačiau paslaugos ne visada yra nemokamos ir gali reikalauti prenumeratos ar mokėjimo už naudojimą, mainais už galimybę naudotis paslaugos savininko įranga ir ištekliais, optimizuoti išlaidas ir lengvai plėstis. Paslaugos pavyzdys yra [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), kuri siūlo mokėjimo už naudojimą planą, tai reiškia, kad vartotojai apmokestinami proporcingai pagal tai, kiek jie naudoja paslaugą. Be to, Azure OpenAI Service siūlo įmonės lygio saugumą ir atsakingo dirbtinio intelekto sistemą, papildančią modelių galimybes.

Modeliai yra tik neuronų tinklas su parametrais, svoriais ir kitais komponentais. Tai leidžia įmonėms juos paleisti vietoje, tačiau tam reikės įsigyti įrangą, sukurti struktūrą mastelio keitimui ir įsigyti licenciją arba naudoti atvirojo kodo modelį. Modelis, kaip LLaMA, yra prieinamas naudoti, tačiau jam reikalinga skaičiavimo galia, kad galėtų veikti.

## Kaip testuoti ir iteruoti su skirtingais modeliais, kad suprastumėte jų veikimą Azure

Kai mūsų komanda ištyrė dabartinį LLM kraštovaizdį ir nustatė keletą gerų kandidatų savo scenarijams, kitas žingsnis yra jų testavimas su savo duomenimis ir darbo krūviu. Tai yra iteracinis procesas, atliekamas eksperimentais ir matavimais.
Dauguma modelių, kuriuos paminėjome ankstesnėse pastraipose (OpenAI modeliai, atvirojo kodo modeliai, tokie kaip Llama2, ir Hugging Face transformers), yra pasiekiami [Modelių kataloge](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview?WT.mc_id=academic-105485-koreyst) [Azure AI studijoje](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst).

[Azure AI studija](https://learn.microsoft.com/azure/ai-studio/what-is-ai-studio?WT.mc_id=academic-105485-koreyst) yra debesų platforma, sukurta kūrėjams, norintiems kurti generatyviosios AI programas ir valdyti visą kūrimo ciklą – nuo eksperimentavimo iki vertinimo – sujungiant visas Azure AI paslaugas į vieną centrą su patogia grafinio vartotojo sąsaja. Modelių katalogas Azure AI studijoje leidžia vartotojui:

- Rasti dominančią bazinį modelį kataloge – tiek nuosavą, tiek atvirojo kodo, filtruojant pagal užduotį, licenciją ar pavadinimą. Siekiant pagerinti paiešką, modeliai yra suskirstyti į kolekcijas, tokias kaip Azure OpenAI kolekcija, Hugging Face kolekcija ir kt.

![Modelių katalogas](../../../translated_images/AzureAIStudioModelCatalog.3cf8a499aa8ba0314f2c73d4048b3225d324165f547525f5b7cfa5f6c9c68941.lt.png)

- Peržiūrėti modelio kortelę, įskaitant išsamų aprašymą apie numatomą naudojimą ir mokymo duomenis, kodo pavyzdžius ir vertinimo rezultatus vidinėje vertinimo bibliotekoje.

![Modelio kortelė](../../../translated_images/ModelCard.598051692c6e400d681a713ba7717e8b6e5e65f08d12131556fcec0f1789459b.lt.png)

- Palyginti modelių ir pramonėje prieinamų duomenų rinkinių etalonus, kad būtų galima įvertinti, kuris modelis geriausiai atitinka verslo scenarijų, naudojant [Modelių etalonų](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst) skydelį.

![Modelių etalonai](../../../translated_images/ModelBenchmarks.254cb20fbd06c03a4ca53994585c5ea4300a88bcec8eff0450f2866ee2ac5ff3.lt.png)

- Priderinti modelį prie individualių mokymo duomenų, siekiant pagerinti modelio našumą konkrečioje užduotyje, pasinaudojant Azure AI studijos eksperimentavimo ir stebėjimo galimybėmis.

![Modelio pritaikymas](../../../translated_images/FineTuning.aac48f07142e36fddc6571b1f43ea2e003325c9c6d8e3fc9d8834b771e308dbf.lt.png)

- Diegti originalų iš anksto apmokytą modelį arba pritaikytą versiją nuotoliniam realaus laiko prognozavimui – valdomam skaičiavimui – arba serverio neturinčiam API galutiniam taškui – [mokėjimas pagal naudojimą](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview#model-deployment-managed-compute-and-serverless-api-pay-as-you-go?WT.mc_id=academic-105485-koreyst) – kad programos galėtų jį naudoti.

![Modelio diegimas](../../../translated_images/ModelDeploy.890da48cbd0bccdb4abfc9257f3d884831e5d41b723e7d1ceeac9d60c3c4f984.lt.png)

> [!NOTE]
> Ne visi kataloge esantys modeliai šiuo metu yra pasiekiami pritaikymui ir/arba mokėjimui pagal naudojimą. Patikrinkite modelio kortelę, kad sužinotumėte daugiau apie modelio galimybes ir apribojimus.

## LLM rezultatų gerinimas

Kartu su mūsų startuolio komanda ištyrėme įvairius LLM tipus ir debesų platformą (Azure Machine Learning), leidžiančią palyginti skirtingus modelius, vertinti juos pagal testavimo duomenis, gerinti našumą ir diegti juos prognozavimo galutiniuose taškuose.

Bet kada reikėtų apsvarstyti galimybę pritaikyti modelį, o ne naudoti iš anksto apmokytą? Ar yra kitų būdų, kaip pagerinti modelio našumą konkrečiose užduotyse?

Yra keletas būdų, kuriuos verslas gali naudoti norėdamas pasiekti norimus rezultatus iš LLM. Galite pasirinkti skirtingų tipų modelius su skirtingais mokymo lygiais, kai diegiate LLM gamyboje, su skirtingais sudėtingumo, kainos ir kokybės lygiais. Štai keletas skirtingų požiūrių:

- **Konteksto pagrįstas užklausų kūrimas**. Idėja yra pateikti pakankamai konteksto užklausoje, kad gautumėte reikiamus atsakymus.

- **Informacijos paieška ir generavimas (RAG)**. Jūsų duomenys gali būti duomenų bazėje arba interneto galutiniame taške, pavyzdžiui, kad užtikrintumėte, jog šie duomenys arba jų dalis būtų įtraukti užklausos metu, galite surinkti atitinkamus duomenis ir įtraukti juos į vartotojo užklausą.

- **Pritaikytas modelis**. Čia modelis papildomai apmokomas jūsų duomenimis, todėl jis tampa tikslesnis ir labiau atitinka jūsų poreikius, tačiau tai gali būti brangu.

![LLM diegimas](../../../translated_images/Deploy.18b2d27412ec8c02871386cbe91097c7f2190a8c6e2be88f66392b411609a48c.lt.png)

Nuotraukos šaltinis: [Keturi būdai, kaip įmonės diegia LLM | Fiddler AI tinklaraštis](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Konteksto pagrįstas užklausų kūrimas

Iš anksto apmokyti LLM labai gerai veikia bendruose natūralios kalbos užduotyse, net jei jiems pateikiama trumpa užklausa, pvz., sakinys, kurį reikia užbaigti, arba klausimas – vadinamasis „nulinio pavyzdžio“ mokymasis.

Tačiau kuo daugiau vartotojas gali suformuluoti savo užklausą, pateikdamas išsamų prašymą ir pavyzdžius – Kontekstą – tuo tikslesnis ir artimesnis vartotojo lūkesčiams bus atsakymas. Tokiu atveju kalbame apie „vieno pavyzdžio“ mokymąsi, jei užklausoje yra tik vienas pavyzdys, ir „kelių pavyzdžių mokymąsi“, jei yra keli pavyzdžiai. Konteksto pagrįstas užklausų kūrimas yra pats ekonomiškiausias būdas pradėti.

### Informacijos paieška ir generavimas (RAG)

LLM turi apribojimą, kad jie gali naudoti tik tuos duomenis, kurie buvo panaudoti jų mokymo metu, kad sugeneruotų atsakymą. Tai reiškia, kad jie nieko nežino apie faktus, įvykusius po jų mokymo proceso, ir negali pasiekti ne viešos informacijos (pvz., įmonės duomenų). 

Tai galima įveikti naudojant RAG – techniką, kuri papildo užklausą išoriniais duomenimis dokumentų fragmentų pavidalu, atsižvelgiant į užklausos ilgio apribojimus. Tai palaiko vektorinės duomenų bazės įrankiai (tokie kaip [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)), kurie suranda naudingus fragmentus iš įvairių iš anksto apibrėžtų duomenų šaltinių ir prideda juos prie užklausos konteksto.

Ši technika yra labai naudinga, kai verslas neturi pakankamai duomenų, laiko ar išteklių pritaikyti LLM, tačiau vis tiek nori pagerinti našumą konkrečioje užduotyje ir sumažinti klaidų riziką, t. y., realybės iškraipymą ar žalingą turinį.

### Pritaikytas modelis

Pritaikymas yra procesas, kuris pasinaudoja perkėlimo mokymusi, kad „pritaikytų“ modelį konkrečiai užduočiai arba išspręstų tam tikrą problemą. Skirtingai nuo kelių pavyzdžių mokymosi ir RAG, jis sukuria naują modelį su atnaujintais svoriais ir šališkumu. Tam reikia mokymo pavyzdžių rinkinio, sudaryto iš vieno įvesties (užklausos) ir susijusio išvesties (atsakymo).

Tai būtų pageidaujamas požiūris, jei:

- **Naudojami pritaikyti modeliai**. Verslas norėtų naudoti pritaikytus mažiau pajėgius modelius (pvz., įterpimo modelius), o ne aukštos kokybės modelius, kas leistų pasiekti ekonomiškesnį ir greitesnį sprendimą.

- **Apsvarstoma delsimo problema**. Delsimas yra svarbus konkrečiam naudojimo atvejui, todėl negalima naudoti labai ilgų užklausų arba pavyzdžių skaičius, kurį modelis turėtų išmokti, netelpa į užklausos ilgio limitą.

- **Nuolatinis atnaujinimas**. Verslas turi daug aukštos kokybės duomenų ir patikimų etikečių bei išteklių, reikalingų šiuos duomenis nuolat atnaujinti.

### Apmokytas modelis

LLM mokymas nuo nulio neabejotinai yra pats sunkiausias ir sudėtingiausias požiūris, reikalaujantis didžiulio duomenų kiekio, kvalifikuotų išteklių ir tinkamos skaičiavimo galios. Šią galimybę reikėtų svarstyti tik tuo atveju, jei verslas turi specifinį domeno naudojimo atvejį ir didelį domeno duomenų kiekį.

## Žinių patikrinimas

Koks galėtų būti geras požiūris, siekiant pagerinti LLM užklausų rezultatus?

1. Konteksto pagrįstas užklausų kūrimas  
1. RAG  
1. Pritaikytas modelis  

A:3, jei turite laiko, išteklių ir aukštos kokybės duomenų, pritaikymas yra geresnis pasirinkimas norint išlikti aktualiems. Tačiau, jei norite pagerinti rezultatus ir neturite pakankamai laiko, verta pirmiausia apsvarstyti RAG.

## 🚀 Iššūkis

Sužinokite daugiau apie tai, kaip galite [naudoti RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) savo verslui.

## Puikus darbas, tęskite mokymąsi

Baigę šią pamoką, peržiūrėkite mūsų [Generatyviosios AI mokymosi kolekciją](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau gilintumėte savo žinias apie generatyviąją AI!

Eikite į 3 pamoką, kurioje aptarsime, kaip [atsakingai naudoti generatyviąją AI](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.