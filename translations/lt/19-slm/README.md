# Įvadas į mažus kalbos modelius generatyviai DI pradedantiesiems
Generatyvus DI yra įdomi dirbtinio intelekto sritis, kuri koncentruojasi į sistemų kūrimą, galinčių generuoti naują turinį. Šis turinys gali būti nuo teksto ir paveikslėlių iki muzikos ir net visų virtualių aplinkų. Viena iš įdomiausių generatyvaus DI taikymo sričių yra kalbos modeliai.

## Kas yra maži kalbos modeliai?

Mažas kalbos modelis (SLM) yra sumažinta didelio kalbos modelio (LLM) versija, naudojanti daugelį LLM architektūrinių principų ir metodų, tačiau turinti ženkliai mažesnį skaičiavimo poreikį.

SLM yra kalbos modelių pogrupis, skirtas generuoti žmogaus kalbai panašų tekstą. Skirtingai nuo didesniųjų, tokių kaip GPT-4, SLM yra kompaktiškesni ir efektyvesni, todėl puikiai tinka taikymams, kur skaičiavimo ištekliai yra riboti. Nepaisant mažesnio dydžio, jie gali atlikti įvairias užduotis. Paprastai SLM sukonstruojami suspaudžiant arba distiliuojant LLM, siekiant išlaikyti didelę dalį originalaus modelio funkcionalumo ir lingvistinių gebėjimų. Modelio dydžio sumažinimas sumažina bendrą sudėtingumą, todėl SLM yra efektyvesni tiek atminties naudojimo, tiek skaičiavimo reikalavimų atžvilgiu. Nepaisant šių optimizacijų, SLM vis dar gali atlikti plačią natūralios kalbos apdorojimo (NLP) užduočių įvairovę:

- Teksto generavimas: kurti nuoseklias ir kontekstualiai tinkamas sakinių arba pastraipų dalis.
- Teksto užbaigimas: prognozuoti ir užbaigti sakinius pagal pateiktą užklausą.
- Vertimas: konvertuoti tekstą iš vienos kalbos į kitą.
- Santraukų rengimas: suspausti ilgas tekstų dalis į trumpesnes, lengviau įsisavinamas santraukas.

Nors tai daroma su tam tikrais našumo ar supratimo gylio kompromisais, palyginti su jų didesnėmis versijomis.

## Kaip veikia maži kalbos modeliai?
SLM mokomi naudojant didžiules tekstinių duomenų apimtis. Mokymo metu jie išmoksta kalbos modelius ir struktūras, kurios leidžia generuoti gramatikos ir konteksto atžvilgiu tinkamą tekstą. Mokymo procesas apima:

- Duomenų surinkimą: didelių tekstinių duomenų rinkinių kaupimą iš įvairių šaltinių.
- Duomenų paruošimą: duomenų valymą ir organizavimą, kad jie būtų tinkami mokymui.
- Mokymą: naudojant mašininio mokymosi algoritmus mokyti modelį suprasti ir generuoti tekstą.
- Tolimesnį mokymą: modelio koregavimą, siekiant pagerinti jo veikimą tam tikrose užduotyse.

SLM vystymas atitinka didėjantį poreikį modeliams, kurie gali būti dislokuojami išteklių ribotose aplinkose, pavyzdžiui, mobiliuosiuose įrenginiuose ar krašto kompiuterijos platformose, kur pilno masto LLM gali būti nepraktiški dėl didelių išteklių reikalavimų. Dėmesys efektyvumui leidžia SLM suderinti našumą ir prieinamumą, leidžiant plačiau taikyti įvairiose srityse.

![slm](../../../translated_images/lt/slm.4058842744d0444a.webp)

## Mokymosi tikslai

Šioje pamokoje norime pristatyti žinias apie SLM ir sujungti jas su Microsoft Phi-3, kad išmoktume skirtingų scenarijų teksto turinyje, vaizduose ir MoE.

Pamokos pabaigoje turėtumėte sugebėti atsakyti į šiuos klausimus:

- Kas yra SLM?
- Kuo skiriasi SLM nuo LLM?
- Kas yra Microsoft Phi-3/3.5 šeima?
- Kaip vykdyti spėjimą su Microsoft Phi-3/3.5 šeima?

Pasiruošę? Pradėkime.

## Skirtumai tarp didelių kalbos modelių (LLM) ir mažų kalbos modelių (SLM)

Tiek LLM, tiek SLM remiasi pagrindiniais tikimybinio mašininio mokymosi principais, naudojant panašius architektūrinius sprendimus, mokymo metodologijas, duomenų generavimo procesus ir modelių vertinimo metodus. Tačiau yra keli esminiai veiksniai, skiriantys šiuos du modelių tipus.

## Mažų kalbos modelių taikymas

SLM turi platų taikymų spektrą, įskaitant:

- Pokalbių robotai: teikti klientų aptarnavimą ir bendrauti su vartotojais pokalbių forma.
- Turinys kūrimas: padėti rašytojams generuoti idėjas arba net rašyti visus straipsnius.
- Švietimas: padėti mokiniams rašymo užduotyse ar mokantis naujų kalbų.
- Prieinamumas: kurti įrankius neįgaliems žmonėms, pavyzdžiui, teksto į garsą sistemas.

**Dydis**
  
Pagrindinis skirtumas tarp LLM ir SLM yra modelių mastas. LLM, pavyzdžiui, ChatGPT (GPT-4), gali turėti apie 1,76 trilijono parametrų, o atvirojo kodo SLM, kaip Mistral 7B, turi gerokai mažiau parametrų – apie 7 milijardus. Šis skirtumas daugiausia lemia modelio architektūros ir mokymo procesų skirtumai. Pavyzdžiui, ChatGPT naudoja savidėmes mechanizmą enkoderio-dekoderio struktūroje, o Mistral 7B naudoja slydimo lango dėmesį, leidžiantį efektyviau mokyti vienoje dekoderio modelio pusėje. Šis architektūrinis skirtumas ženkliai veikia modelių sudėtingumą ir veikimą.

**Supratimas**

SLM paprastai optimizuojami veikimui specifinėse srityse, todėl jie yra labai specializuoti, bet riboti savo gebėjimu suteikti platų kontekstinį supratimą keliuose žinių laukuose. Priešingai, LLM siekia imituoti žmogaus intelektą platesniu lygiu. Mokomi dideliais, įvairiais duomenų rinkiniais, LLM yra sukurti gerai veikti įvairiose srityse, suteikdami didesnį universalumą ir prisitaikymą. Todėl LLM labiau tinka platesniam spektrui užduočių, pavyzdžiui, natūralios kalbos apdorojimui ir programavimui.

**Skaičiavimai**

LLM mokymas ir diegimas yra daug išteklių reikalaujantys procesai, dažnai reikalaujantys didelės skaičiavimo infrastruktūros, įskaitant dideles GPU klasterių sistemas. Pavyzdžiui, modelio kaip ChatGPT mokymas nuo nulio gali reikalauti tūkstančių GPU ilgesnį laiką. Priešingai, SLM, turintys mažesnį parametrų skaičių, yra prieinamesni skaičiavimo išteklių prasme. Tokie modeliai kaip Mistral 7B gali būti mokomi ir veikiami vietinėse mašinose su vidutinio pajėgumo GPU, nors mokymas vis tiek reikalauja kelių valandų keliuose GPU.

**Šališkumas**

Šališkumas yra žinoma problema LLM, daugiausia dėl mokymo duomenų pobūdžio. Šie modeliai dažnai remiasi neapdorotais, atvirais interneto duomenimis, kurie gali nepakankamai atspindėti ar neteisingai atvaizduoti tam tikras grupes, įvesti klaidingą žymėjimą ar atspindėti lingvistinius šališkumus, paveiktus dialekto, geografinių skirtumų ir gramatikos taisyklių. Be to, LLM architektūrų sudėtingumas gali netyčia sustiprinti šališkumą, kuris gali būti nepastebėtas be atidaus tolesnio mokymo. Priešingai, SLM, mokomi ribotesniais, domeno specifiniais duomenų rinkiniais, yra mažiau linkę į tokius šališkumus, tačiau jie nuo jų nėra apsaugoti.

**Spėjimas**

SLM sumažintas dydis suteikia žymų pranašumą spėjimo greičio atžvilgiu, leidžiant jiems efektyviai generuoti rezultatus vietinėje techninėje įrangoje be plataus daugiaparametrinio apdorojimo poreikio. Priešingai, LLM dėl savo dydžio ir sudėtingumo dažnai reikalauja didelių paralelinių skaičiavimo išteklių, norint pasiekti priimtiną spėjimo laiką. Didelis vienalaikinių vartotojų kiekis dar labiau lėtina LLM atsakymo laiką, ypač didelio masto diegimuose.

Apibendrinant, nors tiek LLM, tiek SLM remiasi mašininio mokymosi pagrindais, jie žymiai skiriasi modelio dydžiu, išteklių poreikiais, kontekstinio supratimo gyliais, polinkiu į šališkumą ir spėjimo greičiu. Šie skirtumai atspindi jų tinkamumą skirtingoms naudojimo sritims – LLM yra universalesni, bet išteklių reiklūs, o SLM suteikia domeno specifinį efektyvumą su mažesniais skaičiavimo reikalavimais.

***Pastaba: šioje pamokoje SLM pristatysime naudodami Microsoft Phi-3 / 3.5 kaip pavyzdį.***

## Phi-3 / Phi-3.5 šeimos pristatymas

Phi-3 / 3.5 šeima daugiausia dėmesio skiria teksto, vaizdo ir agentų (MoE) taikymo scenarijams:

### Phi-3 / 3.5 Instruct

Pagrindinė paskirtis – teksto generavimas, pokalbių užbaigimas ir turinio informacijos išgavimas.

**Phi-3-mini**

3.8 milijardo parametrų kalbos modelis yra prieinamas Microsoft Foundry, Hugging Face ir Ollama platformose. Phi-3 modeliai žymiai lenkia tokio pat dydžio ar didesnius kalbos modelius pagrindiniuose etalonuose (žr. žemiau etalonų skaičius – kuo didesnis, tuo geriau). Phi-3-mini lenkia dvigubai didesnius modelius, o Phi-3-small ir Phi-3-medium lenkia dar didesnius modelius, įskaitant GPT-3.5.

**Phi-3-small ir medium**

Turint vos 7 milijardus parametrų, Phi-3-small lenkia GPT-3.5T įvairiuose kalbos, logikos, programavimo ir matematikos etalonuose.

Phi-3-medium su 14 milijardų parametrų tęsia šią tendenciją ir lenkia Gemini 1.0 Pro.

**Phi-3.5-mini**

Galima laikyti Phi-3-mini patobulinimu. Nors parametrai nepasikeitė, pagerėjo daugiakalbystės palaikymas (daugiau nei 20 kalbų: arabų, kinų, čekų, danų, olandų, anglų, suomių, prancūzų, vokiečių, hebrajų, vengrų, italų, japonų, korėjiečių, norvegų, lenkų, portugalų, rusų, ispanų, švedų, tailandų, turkų, ukrainiečių) ir sustiprintas ilgalaikio konteksto palaikymas.

Phi-3.5-mini su 3.8 milijardo parametrų lenkia tokio pat dydžio kalbos modelius ir prilygsta dvigubai didesniems modeliams.

### Phi-3 / 3.5 Vision

Galima sakyti, kad Phi-3/3.5 Instruct modelis atspindi Phi gebėjimą suprasti, o Vision suteikia Phi akis pasaulio suvokimui.


**Phi-3-Vision**

Phi-3-vision, turintis tik 4.2 milijardus parametrų, tęsia šią tendenciją ir lenkia didesnius modelius, tokius kaip Claude-3 Haiku ir Gemini 1.0 Pro V, bendrose vaizdinės logikos, OCR ir lentelių bei diagramų supratimo užduotyse.


**Phi-3.5-Vision**

Phi-3.5-Vision taip pat yra Phi-3-Vision patobulinimas, pridedantis daugelio vaizdų palaikymą. Jį galima laikyti regos gerinimu – ne tik matomos nuotraukos, bet ir vaizdo įrašai.

Phi-3.5-vision lenkia didesnius modelius, tokius kaip Claude-3.5 Sonnet ir Gemini 1.5 Flash, OCR, lentelių ir diagramų supratimo užduotyse, o bendrų vizualinių žinių loginio mąstymo užduotyse prilygsta jiems. Palaikomas daugelio kadrų įvestis, t.y., atliekamas loginis mąstymas apie kelis įvesties vaizdus.


### Phi-3.5-MoE

***Mišriųjų ekspertų modelis (MoE)*** leidžia modeliams būti išankstiniais mokomiems su žymiai mažesniais skaičiavimo ištekliais, tai reiškia, kad galima dramatiškai didinti modelio ar duomenų rinkinio dydį su tokiais pat sąnaudų biudžetais, kaip tankiems modeliams. Konkretūs MoE modeliai turėtų pasiekti tokį pat kokybės lygį kaip tankūs modeliai daug greičiau per išankstinį mokymą.

Phi-3.5-MoE sudaro 16x3.8 mlrd. ekspertų modulių. Phi-3.5-MoE su vos 6.6 mlrd. aktyvių parametrų pasiekia panašų lygį loginio mąstymo, kalbos supratimo ir matematikos srityse kaip ir daug didesni modeliai.

Phi-3/3.5 šeimos modelius galime naudoti pagal skirtingus scenarijus. Skirtingai nuo LLM, galite dislokuoti Phi-3/3.5-mini arba Phi-3/3.5-Vision į krašto įrenginius.


## Kaip naudoti Phi-3/3.5 šeimos modelius

Norime naudoti Phi-3/3.5 skirtingose situacijose. Toliau naudosime Phi-3/3.5 pagal šiuos scenarijus.

![phi3](../../../translated_images/lt/phi3.655208c3186ae381.webp)

### Spėjimas per debesies API

**Microsoft Foundry modeliai**

> **Pastaba:** GitHub modeliai nutraukiami 2026 m. liepos pabaigoje. [Microsoft Foundry modeliai](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) yra tiesioginė alternatyva.

Microsoft Foundry modeliai yra tiesiausias kelias. Galite greitai pasiekti Phi-3/3.5-Instruct modelį per Foundry modelių katalogą. Derindami su Azure AI Inference SDK / OpenAI SDK, galite pasiekti API per kodą, kad atliktumėte Phi-3/3.5-Instruct iškvietimą. Taip pat galite išbandyti įvairius efektus per Playground.

- Demonstracija: Phi-3-mini ir Phi-3.5-mini efektų palyginimas kinų kalbos scenarijuose

![phi3](../../../translated_images/lt/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/lt/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Jei norime naudoti vizijos ir MoE modelius, taip pat galime pasinaudoti Microsoft Foundry norint atlikti iškvietimus. Jei domina, galite perskaityti Phi-3 Virtuvės knygą, kaip iškviesti Phi-3/3.5 Instruct, Vision, MoE per Microsoft Foundry [spustelėkite šią nuorodą](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Be debesijos Microsoft Foundry modelių katalogo, taip pat galite naudoti [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) susijusiems iškvietimams atlikti. Galite apsilankyti NVIDIA NIM, kad atliktumėte Phi-3/3.5 šeimos API iškvietimus. NVIDIA NIM (NVIDIA Inference Microservices) yra rinkinys pagreitintų spėjimo mikropaslaugų, skirtų padėti kūrėjams efektyviai diegti DI modelius įvairiose aplinkose, įskaitant debesis, duomenų centrus ir darbo vietas.

Čia yra keletas NVIDIA NIM pagrindinių funkcijų:

- **Diegimo paprastumas:** NIM leidžia diegti DI modelius viena komanda, todėl labai paprasta integruoti į esamus darbo procesus.

- **Optimizuotas veiksmingumas:** Jis naudoja NVIDIA iš anksto optimizuotus interpretavimo variklius, tokius kaip TensorRT ir TensorRT-LLM, užtikrindamas žemą vėlavimą ir didelį pralaidumą.
- **Mastelio keitimas:** NIM palaiko automatinį mastelio keitimą Kubernetes, leidžiantį efektyviai tvarkyti kintamus darbo krūvius.
- **Saugumas ir kontrolė:** Organizacijos gali išlaikyti kontrolę savo duomenims ir programoms, savarankiškai talpindamos NIM mikroservisus savo valdomoje infrastruktūroje.
- **Standartizuoti API:** NIM suteikia pramonės standartų API, todėl lengva kurti ir integruoti AI programas, tokias kaip pokalbių robotai, AI asistentai ir kt.

NIM yra NVIDIA AI Enterprise dalis, kurios tikslas – supaprastinti AI modelių diegimą ir eksploatavimą, užtikrinant efektyvų jų veikimą NVIDIA GPU.

- Demonstracija: Naudojant NVIDIA NIM kvietimui Phi-3.5-Vision-API [[Spustelėkite šią nuorodą](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5 paleidimas vietoje
Interpretacija, susijusi su Phi-3 ar bet kuriuo kalbos modeliu, pavyzdžiui, GPT-3, reiškia atsakymų ar prognozių generavimo procesą pagal pateiktą įvestį. Kai pateikiate promptą ar klausimą Phi-3, jis naudoja savo apmokytą neuroninį tinklą, kad įžvelgtų tikėtiniausią ir tinkamiausią atsakymą, analizuodamas duomenų, kuriais buvo apmokytas, modelius ir ryšius.

**Hugging Face Transformer**
Hugging Face Transformers yra galinga biblioteka, skirta natūralios kalbos apdorojimui (NLP) ir kitiems mašininio mokymosi uždaviniams. Štai keletas svarbiausių faktų apie ją:

1. **Iš anksto apmokyti modeliai:** Biblioteka siūlo tūkstančius iš anksto apmokytų modelių, kurie gali būti naudojami įvairiems darbams, tokiems kaip teksto klasifikacija, pavadintų vienetų atpažinimas, klausimų atsakymas, santrauka, vertimas ir teksto generavimas.

2. **Framework tarpusavio suderinamumas:** Biblioteka palaiko kelis giliųjų mokymosi karkasus, įskaitant PyTorch, TensorFlow ir JAX. Tai leidžia išmokyti modelį viename karkase ir naudoti jį kitame.

3. **Daugiaplatformės galimybės:** Be NLP, Hugging Face Transformers taip pat palaiko darbus kompiuterinėje vizijoje (pvz., vaizdų klasifikavimas, objektų aptikimas) ir garso apdorojime (pvz., kalbos atpažinimas, garso klasifikavimas).

4. **Paprastas naudojimas:** Biblioteka siūlo API ir įrankius, leidžiančius lengvai atsisiųsti ir koreguoti modelius, todėl ji prieinama tiek pradedantiesiems, tiek ekspertams.

5. **Bendruomenė ir ištekliai:** Hugging Face turi gyvą bendruomenę, plačią dokumentaciją, pamokas ir gidus, kurie padeda vartotojams pradėti darbą ir maksimaliai išnaudoti biblioteką.
[oficiali dokumentacija](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) arba jų [GitHub saugykla](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Tai dažniausiai naudojamas metodas, tačiau jis taip pat reikalauja GPU pagreičio. Galiausiai, tokios srities kaip Vision ir MoE užduotys reikalauja daug skaičiavimų ir procesas bus labai lėtas CPU, jei modeliai nėra kiekybiškai sureguliuoti.


- Demonstracija: Naudojant Transformer kvietimui Phi-3.5-Instruct [Spustelėkite šią nuorodą](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demonstracija: Naudojant Transformer kvietimui Phi-3.5-Vision [Spustelėkite šią nuorodą](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demonstracija: Naudojant Transformer kvietimui Phi-3.5-MoE [Spustelėkite šią nuorodą](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) yra platforma, skirta palengvinti didelių kalbos modelių (LLM) vietinį vykdymą jūsų kompiuteryje. Ji palaiko įvairius modelius, tokius kaip Llama 3.1, Phi 3, Mistral ir Gemma 2 bei kitus. Platforma supaprastina procesą, pakuodama modelio svorius, konfiguraciją ir duomenis į vieną paketą, todėl vartotojams lengviau pritaikyti ir kurti savo modelius. Ollama yra prieinama macOS, Linux ir Windows sistemoms. Tai puikus įrankis, jei norite eksperimentuoti ar diegti LLM be debesijos paslaugų priklausomybės. Ollama yra tiesiausias kelias – tereikia vykdyti šią komandą.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) yra „Microsoft“ neprisijungus veikianti, įrenginyje vykdoma aplinka modeliams, tokiems kaip Phi, paleisti visiškai jūsų nuosavoje aparatinėje įrangoje – nereikia Azure prenumeratos, API rakto ar tinklo ryšio. Ji automatiškai pasirenka geriausią vykdymo teikėją (NPU, GPU ar CPU) ir suteikia OpenAI suderinamą galinį tašką, tad esamas `openai`/Azure AI Inference SDK kodas gali būti nukreiptas į ją su minimaliais pakeitimais. Peržiūrėkite [Foundry Local dokumentaciją](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) pradžiai.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Arba naudokite SDK tiesiogiai Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime for GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) yra kryžminės platformos interpretavimo ir mokymo mašininio mokymosi pagreitinimo įrankis. ONNX Runtime for Generative AI (GENAI) yra galingas įrankis, padedantis efektyviai vykdyti generatyvius AI modelius įvairiose platformose.

## Kas yra ONNX Runtime?
ONNX Runtime yra atviro kodo projektas, leidžiantis greitai interpretuoti mašininio mokymosi modelius. Jis palaiko modelius Open Neural Network Exchange (ONNX) formatu, kuris yra standartas mašininio mokymosi modelių atvaizdavimui. ONNX Runtime interpretavimas gali pagreitinti klientų patirtį ir sumažinti sąnaudas, palaikydamas modelius iš giliosios mokymosi karkasų, tokių kaip PyTorch ir TensorFlow/Keras, taip pat klasikines mašininio mokymosi bibliotekas, tokias kaip scikit-learn, LightGBM, XGBoost ir kt. ONNX Runtime suderinamas su įvairia aparatine įranga, tvarkyklėmis ir operacinėmis sistemomis bei suteikia optimalų našumą, panaudodamas aparatūros pagreitintuvus, kai tai įmanoma, kartu su grafų optimizacijomis ir transformacijomis.

## Kas yra generatyvioji AI?
Generatyvioji AI reiškia AI sistemas, kurios gali kurti naują turinį, pavyzdžiui, tekstą, paveikslus ar muziką, remiantis duomenimis, kuriais jos buvo apmokytos. Pavyzdžiai yra kalbos modeliai, tokie kaip GPT-3, ir vaizdų generavimo modeliai, tokie kaip Stable Diffusion. ONNX Runtime for GenAI biblioteka suteikia generatyvios AI ciklą ONNX modeliams, įskaitant interpretavimą su ONNX Runtime, logitų apdorojimą, paiešką bei mėginių ėmimą ir KV talpyklos valdymą.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI išplečia ONNX Runtime galimybes, palaikydama generatyvių AI modelių vykdymą. Štai keletas svarbių funkcijų:

- **Platus platformų palaikymas:** Veikia įvairiose platformose, įskaitant Windows, Linux, macOS, Android ir iOS.
- **Modelių palaikymas:** Palaiko daugelį populiarių generatyvių AI modelių, tokių kaip LLaMA, GPT-Neo, BLOOM ir kt.
- **Veikimo optimizavimas:** Apima optimizacijas skirtingiems aparatūros pagreitintuvams, tokiems kaip NVIDIA GPU, AMD GPU ir kiti.
- **Paprastas naudojimas:** Suteikia API lengvai integracijai į programas, leidžiančias generuoti tekstą, paveikslus ir kitą turinį su minimalia kodo rašymo apimtimi.
- Vartotojai gali kviesti aukšto lygio generate() metodą arba vykdyti kiekvieną modelio iteraciją cikle, generuodami po vieną ženklą vienu metu ir neprivalomai atnaujindami generavimo parametrus ciklo viduje.
- ONNX Runtime taip pat palaiko godžiąją/šviesųjį paiešką ir TopP, TopK mėginių ėmimą norint generuoti žodžių sekas bei integruotą logitų apdorojimą, tokią kaip pasikartojimų baudos. Taip pat galite lengvai pridėti vartotojo apibrėžtą įvertinimą.

## Pradžia
Norėdami pradėti naudotis ONNX Runtime for GENAI, galite atlikti šiuos veiksmus:

### Įdiekite ONNX Runtime:
```Python
pip install onnxruntime
```
### Įdiekite Generatyvios AI plėtinius:
```Python
pip install onnxruntime-genai
```

### Vykdykite modelį: Štai paprastas pavyzdys Python kalba:
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
### Demonstracija: Naudojant ONNX Runtime GenAI kvietimui Phi-3.5-Vision


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

Be ONNX Runtime, Ollama ir Foundry Local nuorodų metodų, galime taip pat užbaigti kiekybinių modelių apžvalgą, remdamiesi skirtingų gamintojų pateiktais modelių nuorodų metodais. Pavyzdžiui, Apple MLX karkasas su Apple Metal, Qualcomm QNN su NPU, Intel OpenVINO su CPU/GPU ir kt. Daugiau medžiagos galite rasti [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).


## Daugiau

Mes išmokome Phi-3/3.5 šeimos pagrindus, tačiau norint sužinoti daugiau apie SLM, reikia papildomų žinių. Atsakymus rasite Phi-3 Cookbook. Jei norite sužinoti daugiau, apsilankykite [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->