# Įvadas į Mažus Kalbos Modelius Generatyviajai DI pradedantiesiems
Generatyvioji DI yra įdomi dirbtinio intelekto sritis, orientuota į sistemų kūrimą, gebančių generuoti naują turinį. Šis turinys gali apimti tekstą, vaizdus, muziką ir net visus virtualius aplinkos elementus. Viena įdomiausių generatyvios DI pritaikymo sričių yra kalbos modeliai.

## Kas yra Maži Kalbos Modeliai?

Mažas Kalbos Modelis (SLM) yra sumažinta didelio kalbos modelio (LLM) versija, taikanti daugelį LLM architektūrinių principų ir metodų, tačiau turinti gerokai mažesnį skaičiavimo išteklių poreikį.

SLM yra kalbos modelių pogrupis, sukurtas generuoti žmogiškai panašų tekstą. Skirtingai nei jų didesni prototipai, tokie kaip GPT-4, SLM yra kompaktiškesni ir efektyvesni, todėl yra idealūs taikymams, kur riboti skaičiavimo ištekliai. Nepaisant mažesnio dydžio, jie vis dar gali atlikti įvairias užduotis. Paprastai SLM kuriami kompresijos arba distiliavimo būdu iš LLM, siekiant išlaikyti didelę dalį pradinio modelio funkcionalumo ir kalbos gebėjimų. Modelio dydžio sumažinimas sumažina bendrą sudėtingumą, todėl SLM yra efektyvesni tiek atminties naudojimo, tiek skaičiavimo reikalavimų atžvilgiu. Nepaisant šių optimizacijų, SLM gali atlikti įvairias natūralios kalbos apdorojimo (NLP) užduotis:

- Teksto generavimas: kurti nuoseklias ir kontekstualiai tinkamas sakinius ar pastraipas.
- Teksto užbaigimas: prognozuoti ir užbaigti sakinius pagal pateiktą užuominą.
- Vertimas: tekstų konvertavimas iš vienos kalbos į kitą.
- Santraukų rengimas: ilgų tekstų sutrumpinimas į trumpesnes, lengviau suprantamas santraukas.

Nors ir su tam tikrais kompromisais dėl našumo ar supratimo gilumo, palyginti su jų didesniais atitikmenimis.

## Kaip Veikia Maži Kalbos Modeliai?
SLM mokomi naudodami didžiulius tekstinių duomenų kiekius. Mokymo metu jie įsisavina kalbos modelius ir struktūras, leidžiančias generuoti grammatiškai taisyklingą ir kontekstualiai tinkamą tekstą. Mokymo procesas apima:

- Duomenų rinkimą: didelių tekstinių duomenų rinkinių surinkimą iš įvairių šaltinių.
- Išankstinį apdorojimą: duomenų valymą ir organizavimą, kad būtų tinkami mokymui.
- Mokymą: mašininio mokymo algoritmų naudojimą modeliui išmokyti suprasti ir generuoti tekstą.
- Tikslinimą: modelio koregavimą siekiant pagerinti jo našumą konkrečiose užduotyse.

SLM vystymas atitinka vis didėjantį poreikį modeliams, kurie galėtų būti diegiami išteklių ribotose aplinkose, tokiose kaip mobilieji įrenginiai ar kraštinių kompiuterių platformos, kur pilno dydžio LLM gali būti nepraktiški dėl didelių išteklių reikalavimų. Orientuodamiesi į efektyvumą, SLM subalansuoja našumą ir prieinamumą, leidžiantį jų platesnį pritaikymą įvairiose srityse.

![slm](../../../translated_images/lt/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Mokymosi Tikslai

Šioje pamokoje sieksime supažindinti su SLM žiniomis ir derinti jas su Microsoft Phi-3, kad išmoktumėme skirtingų scenarijų teksto turinyje, regos ir MoE srityse.

Pamokos pabaigoje turėtumėte sugebėti atsakyti į šiuos klausimus:

- Kas yra SLM?
- Kuo skiriasi SLM ir LLM?
- Kas yra Microsoft Phi-3/3.5 šeima?
- Kaip paleisti nuoseklų modelio veikimą su Microsoft Phi-3/3.5 šeima?

Pasiruošę? Pradėkime.

## Skirtumai tarp Didelių Kalbos Modelių (LLM) ir Mažų Kalbos Modelių (SLM)

Tiek LLM, tiek SLM pagrįsti probabilistinio mašininio mokymosi pagrindais, laikosi panašių architektūros dizaino, mokymo metodų, duomenų generavimo ir modelių vertinimo principų. Tačiau keletas svarbių veiksnių skiria šiuos modelių tipus.

## Mažų Kalbos Modelių Pritaikymas

SLM plačiai taikomi šiose srityse:

- Pokalbių robotai: klientų aptarnavimui ir pokalbių vedimui su vartotojais.
- Turinys: rašytojams padėjimas generuoti idėjas ar net parengti visus straipsnius.
- Švietimas: pagalba studentams rašymo užduotyse ar naujų kalbų mokyme.
- Prieinamumas: įrankių kūrimas neįgaliesiems, pavyzdžiui, teksto į kalbą sistemos.

**Dydis**
  
Pagrindinis skirtumas tarp LLM ir SLM yra modelio dydis. LLM, pvz., ChatGPT (GPT-4), gali turėti apie 1,76 trilijono parametrų, tuo tarpu atviro kodo SLM, kaip Mistral 7B, turi gerokai mažiau parametrų – maždaug 7 milijardus. Šis skirtumas daugiausia yra dėl modelio architektūros ir mokymo proceso skirtumų. Pvz., ChatGPT naudoja savęs dėmesio mechanizmą enkoderio-dekoderio struktūroje, o Mistral 7B – slankiojančio lango dėmesį dekoderio modelyje, kuris leidžia efektyviau mokyti. Ši architektūrinė variacija daro didelę įtaką šių modelių sudėtingumui ir našumui.

**Supratimas**

SLM paprastai optimizuojami atlikti veiklą specifinėse srityse, todėl jie yra labai specializuoti, bet gali būti riboti suteikiant platesnį kontekstinį supratimą per įvairias žinių sritis. Priešingai, LLM stengiasi simuliuoti žmogiškai panašų intelektą platesniu mastu. Mokyti dideliuose, įvairiuose duomenų rinkiniuose, LLM gali sėkmingai veikti įvairiose srityse, siūlydami didesnį lankstumą ir prisitaikymą. Todėl LLM labiau tinka platesniam spektrui užduočių, tokių kaip natūralaus kalbos apdorojimas ir programavimas.

**Skaičiavimas**

LLM mokymas ir taikymas yra išteklius reikalaujantys procesai, dažnai reikalaujantys didelės skaičiavimo infrastruktūros, įskaitant didelės apimties GPU klasterius. Pavyzdžiui, mokyti modelį kaip ChatGPT nuo nulio gali tekti tūkstančiams GPU per ilgą laiką. Priešingai, SLM su mažesniu parametrų skaičiumi yra labiau prieinami skaičiavimo išteklių atžvilgiu. Tokius modelius kaip Mistral 7B galima mokyti ir paleisti vietinėse mašinose su vidutinėmis GPU galimybėmis, nors mokymas vis tiek reikalauja kelių valandų per kelis GPU.

**Šališkumas**

Šališkumas yra gerai žinoma problema LLM, daugiausia dėl mokymo duomenų pobūdžio. Šie modeliai dažnai naudoja žalią, viešai prieinamą interneto duomenų bazę, kuri gali mažiau ar netinkamai reprezentuoti tam tikras grupes, įvesti klaidingą žymėjimą arba atspindėti lingvistinius šališkumus, lemiančius dialektai, geografinės variacijos ir gramatikos taisyklės. Be to, LLM architektūros sudėtingumas gali netyčia sustiprinti šį šališkumą, kuris gali likti nepastebėtas be kruopštaus tikslinimo. Priešingai, SLM, mokyti labiau ribotuose, domenuose specifiniuose duomenų rinkiniuose, yra mažiau linkę į tokius šališkumus, nors ir nėra nuo jų visiškai apsaugoti.

**Prognozavimas**

SLM mažesnis dydis suteikia jiems reikšmingą pranašumą prognozavimo greičio atžvilgiu, leidžiant efektyviai generuoti rezultatus vietinėje techninėje įrangoje be plačių lygiagretinio apdorojimo poreikių. Priešingai, LLM dėl savo dydžio ir sudėtingumo dažnai reikalauja didelių lygiagrečių skaičiavimo išteklių, kad pasiektų priimtinus prognozavimo laikus. Daug vartotojų vienu metu dar labiau sulėtina LLM atsako laiką, ypač kai jie diegiami dideliu mastu.

Apibendrinant, nors tiek LLM, tiek SLM yra pagrįsti mašininiu mokymusi, jie žymiai skiriasi modelio dydžio, išteklių reikalavimų, kontekstinio supratimo, šališkumo jautrumo ir prognozavimo greičio atžvilgiu. Šie skirtumai atspindi jų tinkamumą skirtingiems naudojimo atvejams – LLM yra universalesni, bet reikalauja daug išteklių, o SLM pasižymi didesniu specifiniu efektyvumu su mažesniais skaičiavimo reikalavimais.

***Pastaba: Šioje pamokoje SLM pristatysime naudodami Microsoft Phi-3 / 3.5 kaip pavyzdį.***

## Phi-3 / Phi-3.5 šeimos pristatymas

Phi-3 / 3.5 šeima daugiausia skirta teksto, regos ir Agento (MoE) taikymo scenarijams:

### Phi-3 / 3.5 Instrukcija

Daugiausia skirta teksto generavimui, pokalbių pabaigimui ir turinio informacijos išgavimui ir pan.

**Phi-3-mini**

3,8 mlrd. parametrų kalbos modelis prieinamas Microsoft Foundry, Hugging Face ir Ollama platformose. Phi-3 modeliai žymiai lenkia tuo pačiu ar didesniu dydžiu kalbos modelius pagrindiniuose etalonuose (žr. žemiau pateiktus etalonų rezultatus, kuo didesnis skaičius, tuo geriau). Phi-3-mini pranoksta dvigubai didesnius modelius, o Phi-3-small ir Phi-3-medium pranoksta didesnius modelius, įskaitant GPT-3.5.

**Phi-3-small ir medium**

Tik su 7 mlrd. parametrų Phi-3-small lenkia GPT-3.5T įvairiuose kalbos, samprotavimo, kodavimo ir matematikos etalonuose.

Phi-3-medium su 14 mlrd. parametrų tęsią šią tendenciją ir pranoksta Gemini 1.0 Pro modelį.

**Phi-3.5-mini**

Tai galime laikyti Phi-3-mini atnaujinimu. Parametrai lieka tie patys, tačiau pagerėja daugiausiai kalbų palaikymas (palaiko 20+ kalbų: arabų, kinų, čekų, danų, olandų, anglų, suomių, prancūzų, vokiečių, hebrajų, vengrų, italų, japonų, korėjiečių, norvegų, lenkų, portugalų, rusų, ispanų, švedų, tailandiečių, turkų, ukrainiečių) ir sustiprinamas ilgų kontekstų palaikymas.

Phi-3.5-mini su 3,8 mlrd. parametrų pranoksta tos pačios apimties kalbos modelius ir yra prilygintas dvigubai didesniems modeliams.

### Phi-3 / 3.5 Regėjimas

Galima manyti, kad Phi-3/3.5 Instruct modelis yra Phi gebėjimas suprasti, o Vision suteikia Phi akis, kad jis suprastų pasaulį.


**Phi-3-Regėjimas**

Phi-3-Vision, turintis tik 4,2 mlrd. parametrų, tęsia šią tendenciją ir pranoksta didesnius modelius, tokius kaip Claude-3 Haiku ir Gemini 1.0 Pro V bendrose vizualinio samprotavimo užduotyse, OCR, lentelių ir diagramų supratimo užduotyse.


**Phi-3.5-Regėjimas**

Phi-3.5-Vision yra Phi-3-Vision atnaujinimas, pridedantis kelių vaizdų palaikymą. Tai yra regėjimo pagerinimas – dabar galite matyti ne tik paveikslėlius, bet ir vaizdo įrašus.

Phi-3.5-Vision pranoksta didesnius modelius, tokius kaip Claude-3.5 Sonnet ir Gemini 1.5 Flash OCR, lentelių ir diagramų supratimo užduotyse bei yra lygus bendrame vizualinės žinios samprotavime. Palaiko kelių kadrų įvestį, t.y., atlieka samprotavimą pagal kelis įvesties vaizdus.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** leidžia modeliams būti išankstiniam apmokymui sunaudojant kur kas mažiau skaičiavimo išteklių, tai reiškia, kad galite žymiai padidinti modelio arba duomenų rinkinio dydį, turint tokį patį skaičiavimo biudžetą kaip tankus modelis. Ypač, MoE modelis turėtų pasiekti tokią pačią kokybę kaip tankus modelis daug greičiau mokymo metu.

Phi-3.5-MoE sudaro 16x3.8B ekspertų modulių. Phi-3.5-MoE su tik 6,6 mlrd. aktyvių parametrų pasiekia panašų samprotavimo, kalbos supratimo ir matematikos lygį kaip daug didesni modeliai.

Phi-3/3.5 šeimos modelius galime naudoti skirtinguose scenarijuose. Skirtingai nuo LLM, Phi-3/3.5-mini arba Phi-3/3.5-Vision galite diegti krašto įrenginiuose.


## Kaip naudoti Phi-3/3.5 šeimos modelius

Tikimės naudoti Phi-3/3.5 įvairiuose scenarijuose. Toliau naudosime Phi-3/3.5, atsižvelgdami į skirtingas situacijas.

![phi3](../../../translated_images/lt/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Prognozavimas per Debesies API

**Microsoft Foundry Modeliai**

> **Pastaba:** GitHub Models bus nutraukti 2026 m. liepos pabaigoje. [Microsoft Foundry Modeliai](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) yra tiesioginis pakaitalas.

> **Pastaba:** Visa Phi-3/3.5 šeima (Instruct, Vision ir MoE variantai) buvo išimta iš Microsoft Foundry Modelių katalogo 2025-08-30. Vietoje jų naudokite `Phi-4` (Instruct) arba `Phi-4-mini-instruct` – žemiau pateikti Phi-3/3.5 pavyzdžiai vis dar veikia per Hugging Face, Ollama, ONNX Runtime ir NVIDIA NIM.

Microsoft Foundry Modeliai dabar siūlo Phi-4 įpėdinius. Naudokite `Phi-4` arba `Phi-4-mini-instruct` vietoje nutrauktų Phi-3/3.5 modelių, kai sekate debesies API pavyzdžius.

- Demo: Phi-3-mini ir Phi-3.5-mini poveikio palyginimas Kinijos scenarijuose

![phi3](../../../translated_images/lt/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/lt/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Jei norite naudoti regos (multimodalinius) modelius debesyje, naudokite dabar prieinamus `Phi-4-multimodal-instruct` per Microsoft Foundry vietoje nutrauktų Phi-3/3.5 Vision modelių; teksto užduotims naudokite `Phi-4` arba `Phi-4-mini-instruct`. Phi-3.5 MoE modelis buvo nutrauktas Microsoft Foundry, tad naudokite kitas šioje pamokoje aprašytas galimybes (pvz., Hugging Face), jei norite eksperimentuoti. Jei domina, galite perskaityti Phi receptų knygą, kaip kviesti Phi modelius per Microsoft Foundry [Spustelėkite šią nuorodą](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Be debesyje esančio Microsoft Foundry Modelių katalogo, galite naudoti ir [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) atlikti susijusius kvietimus. Galite apsilankyti NVIDIA NIM, kad įvykdytumėte Phi-3/3.5 šeimos API kvietimus. NVIDIA NIM (NVIDIA Inference Microservices) yra greitinamosios prognozės mikroservisų rinkinys, sukurtas padėti kūrėjams efektyviai diegti DI modelius įvairiose aplinkose, įskaitant debesis, duomenų centrus ir darbo vietas.

Štai keletas pagrindinių NVIDIA NIM savybių:

- **Diegimo paprastumas:** NIM leidžia diegti DI modelius vienu komandos įsakymu, todėl juos lengva integruoti į esamus darbo procesus.
- **Optimizuotas našumas:** Jis naudoja NVIDIA iš anksto optimizuotas spėjimo variklius, tokius kaip TensorRT ir TensorRT-LLM, užtikrinant mažą delsą ir didelį pralaidumą.
- **Mastelio keitimas:** NIM palaiko automatinį mastelio keitimą Kubernetes, leidžiantį efektyviai tvarkyti kintančius darbo krūvius.
- **Saugumas ir kontrolė:** Organizacijos gali išlaikyti kontrolę savo duomenų ir programų atžvilgiu savarankiškai talpindamos NIM mikroservisus savo valdomoje infrastruktūroje.
- **Standartinės API:** NIM teikia pramonės standartų API, todėl paprasta kurti ir integruoti DI programas, tokias kaip pokalbių robotai, DI asistentai ir kt.

NIM yra NVIDIA AI Enterprise dalis, kurios tikslas – supaprastinti DI modelių diegimą ir eksploatavimą, užtikrinant jų efektyvų veikimą NVIDIA GPU.

- Demonstracija: kaip naudoti NVIDIA NIM kviečiant Phi-3.5-Vision-API [[Spustelėkite šią nuorodą](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5 paleidimas vietoje
Spėjimas, susijęs su Phi-3 ar bet kokiu kalbos modeliu, pavyzdžiui, GPT-3, reiškia atsakymų ar prognozių generavimo procesą, pagrįstą gaunama įvestimi. Kai pateikiate užklausą ar klausimą Phi-3, jis naudoja savo apmokytą neuroninį tinklą, kad įvertintų tikėtiniausią ir tinkamiausią atsakymą, analizuodamas duomenyse išmoktas sąsajas ir ryšius.

**Hugging Face Transformer**
Hugging Face Transformers – tai galinga biblioteka, skirta natūralios kalbos apdorojimui (NLP) ir kitoms mašininio mokymosi užduotims. Štai keletas svarbių faktų apie ją:

1. **Iš anksto apmokyti modeliai**: Ji suteikia tūkstančius iš anksto apmokytų modelių, kurie gali būti naudojami įvairioms užduotims, tokioms kaip teksto klasifikavimas, vardų atpažinimas, klausimų atsakymas, santraukų rengimas, vertimas ir teksto generavimas.

2. **Sistemų suderinamumas:** Biblioteka palaiko kelis giluminio mokymosi karkasus, įskaitant PyTorch, TensorFlow ir JAX. Tai leidžia apmokyti modelį viename karkase ir naudoti jį kitame.

3. **Daugiarūšės galimybės:** Be NLP, Hugging Face Transformers palaiko užduotis kompiuterinėje vizijoje (pvz., vaizdų klasifikacija, objektų atpažinimas) ir garso apdorojime (pvz., balso atpažinimas, garso klasifikacija).

4. **Paprastas naudojimas:** Biblioteka siūlo API ir įrankius, skirtus lengvai atsisiųsti ir tobulinti modelius, todėl ji yra prieinama tiek pradedantiesiems, tiek ekspertams.

5. **Bendruomenė ir ištekliai:** Hugging Face turi gyvybingą bendruomenę bei išsamią dokumentaciją, mokymus ir vadovus, kurie padeda vartotojams pradėti ir pilnai išnaudoti biblioteką.
[Oficiali dokumentacija](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) arba jų [GitHub saugykla](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Tai dažniausiai naudojamas metodas, tačiau reikalinga GPU pagreitinimas. Galiausiai, tokios scenarijai kaip Vision ir MoE reikalauja daug skaičiavimų, kurie būtų labai lėti CPU, jei jie nėra kiekybiškai apdoroti.


- Demonstracija: kaip naudoti Transformer kviečiant Phi-3.5-Instruct [Spustelėkite šią nuorodą](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demonstracija: kaip naudoti Transformer kviečiant Phi-3.5-Vision [Spustelėkite šią nuorodą](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demonstracija: kaip naudoti Transformer kviečiant Phi-3.5-MoE [Spustelėkite šią nuorodą](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) yra platforma, sukurta palengvinti didelių kalbos modelių (LLM) paleidimą vietoje jūsų įrenginyje. Ji palaiko įvairius modelius, tokius kaip Llama 3.1, Phi 3, Mistral ir Gemma 2, bei kitus. Platforma supaprastina procesą, sujungdama modelio svorius, konfigūraciją ir duomenis į vieną paketą, todėl vartotojams lengviau pritaikyti ir kurti savo modelius. Ollama veikia macOS, Linux ir Windows sistemose. Tai puikus įrankis, jei norite eksperimentuoti ar diegti LLM be priklausomybės nuo debesijos paslaugų. Ollama yra pats tiesiausias būdas, jums tereikia vykdyti šią komandą.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) yra Microsoft neprisijungimo režimo, įrenginio viduje veikianti aplinka, skirta modeliams, tokiems kaip Phi, vykdyti visiškai jūsų pačių aparatinėje įrangoje – nereikia Azure prenumeratos, API rakto ar tinklo ryšio. Ji automatiškai parenka geriausią įmanomą vykdymo teikėją (NPU, GPU arba CPU) ir pateikia OpenAI suderinamą galinį tašką, todėl esamas `openai`/Azure AI Inference SDK kodas gali būti nukreiptas į jį su minimaliomis pakeitimais. Žr. [Foundry Local dokumentaciją](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) pradžiai.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Arba naudokite SDK tiesiogiai Python kalba:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) yra daugiaplatforminis spėjimo ir mokymosi mašininio mokymosi variklis. ONNX Runtime Generatyviajam DI (GENAI) yra galingas įrankis, padedantis efektyviai vykdyti generatyviuosius DI modelius įvairiose platformose.

## Kas yra ONNX Runtime?
ONNX Runtime yra atviro kodo projektas, leidžiantis vykdyti didelės spartos mašininio mokymosi modelių spėjimą. Jis palaiko modelius Open Neural Network Exchange (ONNX) formatu, kuris yra standartas mašininio mokymosi modelių atvaizdavimui. ONNX Runtime spėjimai gali pagreitinti vartotojų patirtį ir sumažinti kaštus, palaikydamas modelius iš giluminio mokymosi karkasų, tokių kaip PyTorch ir TensorFlow/Keras, bei klasikinių mašininio mokymosi bibliotekų, tokių kaip scikit-learn, LightGBM, XGBoost ir kt. ONNX Runtime suderinamas su įvairia aparatine įranga, tvarkyklėmis ir operacinėmis sistemomis, teikdamas optimalų našumą naudodamas aparatinės įrangos pagreitintuvus kartu su grafinių optimizacijų ir transformacijų taikymu.

## Kas yra Generatyvusis DI?
Generatyvusis DI reiškia DI sistemas, kurios gali kurti naują turinį, pavyzdžiui, tekstą, vaizdus ar muziką, remiantis apmokymui naudotais duomenimis. Pavyzdžiai: kalbos modeliai, tokie kaip GPT-3, ir vaizdų generavimo modeliai, tokie kaip Stable Diffusion. ONNX Runtime for GenAI biblioteka suteikia generatyvinį DI ciklą ONNX modeliams, įskaitant spėjimą su ONNX Runtime, logitų apdorojimą, paiešką ir mėginius, bei KV talpyklos valdymą.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI išplečia ONNX Runtime galimybes, kad palaikytų generatyvuosius DI modelius. Štai keletas pagrindinių funkcijų:

- **Plati platformų palaikymas:** Veikia įvairiose platformose, įskaitant Windows, Linux, macOS, Android ir iOS.
- **Modelių palaikymas:** Palaiko daugelį populiarių generatyvių DI modelių, tokių kaip LLaMA, GPT-Neo, BLOOM ir kt.
- **Našumo optimizavimas:** Įtraukia optimizacijas skirtingiems aparatinės įrangos pagreitintuvams, tokiems kaip NVIDIA GPU, AMD GPU ir kt.
- **Paprastas naudojimas:** Teikia API lengvai integracijai į programas, leidžiančias generuoti tekstą, vaizdus ir kitą turinį su minimaliu kiekiu kodo.
- Vartotojai gali kviesti aukšto lygio generate() metodą arba vykdyti kiekvieną modelio iteraciją cikle, generuodami po vieną ženklą vienu metu ir, jei pageidaujama, atnaujindami generavimo parametrus ciklo viduje.
- ONNX Runtime taip pat palaiko greedy/beam paiešką bei TopP, TopK mėginius, generuojančius ženklų sekas, ir integruotą logitų apdorojimą, pavyzdžiui, kartojimo bausmes. Taip pat galite lengvai pridėti savo pasirinktinius įvertinimus.

## Pradžia
Norėdami pradėti naudoti ONNX Runtime for GENAI, galite atlikti šiuos veiksmus:

### Įdiekite ONNX Runtime:
```Python
pip install onnxruntime
```
### Įdiekite Generatyvaus DI plėtinius:
```Python
pip install onnxruntime-genai
```

### Paleiskite modelį: čia paprastas pavyzdys Python kalba:
```Python
import onnxruntime_genai as og

model = og.Model('path_to_your_model.onnx')

tokenizer = og.Tokenizer(model)

input_text = "Hello, how are you?"

input_tokens = tokenizer.encode(input_text)

output_tokens = model.generate(input_tokens)

output_text = tokenizer.decode(output_tokens)

print(output_text) 
```
### Demonstracija: naudojant ONNX Runtime GenAI kviečiant Phi-3.5-Vision


```python

import onnxruntime_genai as og

model_path = './Your Phi-3.5-vision-instruct ONNX Path'

img_path = './Your Image Path'

model = og.Model(model_path)

processor = model.create_multimodal_processor()

tokenizer_stream = processor.create_stream()

text = "Your Prompt"

prompt = "<|user|>\n"

prompt += "<|image_1|>\n"

prompt += f"{text}<|end|>\n"

prompt += "<|assistant|>\n"

image = og.Images.open(img_path)

inputs = processor(prompt, images=image)

params = og.GeneratorParams(model)

params.set_inputs(inputs)

params.set_search_options(max_length=3072)

generator = og.Generator(model, params)

while not generator.is_done():

    generator.compute_logits()
    
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    
    output = tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


**Kiti**

Be ONNX Runtime, Ollama ir Foundry Local paminėtų metodų, taip pat galime užbaigti kiekybinių modelių nuorodą, remdamiesi skirtingų gamintojų pateiktais modelių nuorodų metodais. Pavyzdžiui, Apple MLX karkasas su Apple Metal, Qualcomm QNN su NPU, Intel OpenVINO su CPU/GPU ir pan. Platesnės informacijos galite rasti [Phi-3 receptų knygoje](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Daugiau

Išmokome Phi-3/3.5 šeimos pagrindus, tačiau norint daugiau sužinoti apie SLM, reikia daugiau žinių. Atsakymus rasite Phi-3 receptų knygoje. Jei norite sužinoti daugiau, apsilankykite [Phi-3 receptų knygoje](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->