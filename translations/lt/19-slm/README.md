# Įvadas į mažus kalbos modelius generatyviajai dirbtinio intelekto sričiai pradedantiesiems
Generatyvioji DI yra įdomi dirbtinio intelekto sritis, kuri koncentruojasi į sistemų, gebančių generuoti naują turinį, kūrimą. Šis turinys gali būti įvairus – nuo teksto ir vaizdų iki muzikos ir net visų virtualių aplinkų. Viena įdomiausių generatyviosios DI taikymo sričių yra kalbos modeliai.

## Kas yra Maži kalbos modeliai?

Mažas kalbos modelis (SLM) yra sumažinta didelio kalbos modelio (LLM) versija, naudojanti daugelį architektūrinių principų ir technikų iš LLM, bet turinti ženkliai mažesnį skaičiavimo pėdsaką.

SLM yra kalbos modelių poaibis, sukurtas generuoti žmogui panašų tekstą. Skirtingai nuo didesnių modelių, tokių kaip GPT-4, SLM yra kompaktiškesni ir efektyvesni, todėl idealiai tinka programoms, kur ribotos skaičiavimo ištekliai. Nepaisant mažesnio dydžio, jie gali atlikti įvairias užduotis. Paprastai SLM susidaromi suspaudžiant ar distiliuojant LLM, siekiant išlaikyti didelę dalį originalaus modelio funkcionalumo ir lingvistinių gebėjimų. Modelio dydžio sumažinimas mažina bendrą sudėtingumą, todėl SLM yra efektyvesni tiek atminties naudojimo, tiek skaičiavimo reikalavimų atžvilgiu. Nepaisant šių optimizacijų, SLM gali atlikti daug įvairių natūralios kalbos apdorojimo (NLP) užduočių:

- Teksto generavimas: Kurti nuoseklias ir kontekstualiai tinkamas sakinių ar pastraipų sekas.
- Teksto užbaigimas: Prognozuoti ir užbaigti sakinius pagal pateiktą pradžią.
- Vertimas: Konvertuoti tekstą iš vienos kalbos į kitą.
- Santrauka: Trumpinti ilgus tekstus į trumpesnes, įprasminamas santraukas.

Nors tai daroma su tam tikrais kompromisais našume ar supratimo gilumoje, palyginti su didesniais modeliais.

## Kaip veikia Maži kalbos modeliai?
SLM mokomi naudojant didžiulius teksto duomenų kiekius. Mokymo metu jie mokosi kalbos struktūras ir modelius, leidžiančius generuoti gramatiškai taisyklingą ir kontekstualiai tinkamą tekstą. Mokymo procesas apima:

- Duomenų rinkimą: surinkti didelius teksto duomenų rinkinius iš įvairių šaltinių.
- Išankstinį apdorojimą: išvalyti ir organizuoti duomenis, paruošiant juos mokymui.
- Mokymą: naudojant mašininio mokymosi algoritmus išmokyti modelį suprasti ir generuoti tekstą.
- Tolesnį tobulinimą: modelio pritaikymą, siekiant pagerinti jo našumą konkrečiose užduotyse.

SLM kūrimas atitinka didėjantį poreikį modeliams, kuriuos galima diegti išteklių ribotose aplinkose, tokiose kaip mobilieji įrenginiai ar edge kompiuterijos platformos, kur pilno masto LLM gali būti nepraktiški dėl didelių išteklių poreikių. Dėl efektyvumo dėmesio, SLM suderina našumą su prieinamumu, leidžiančiu plačiau taikyti įvairiose srityse.

![slm](../../../translated_images/lt/slm.4058842744d0444a.webp)

## Mokymosi tikslai

Šioje pamokoje tikimės pristatyti žinias apie SLM ir kartu su Microsoft Phi-3 sužinoti apie skirtingus scenarijus teksto turinyje, vaizduose ir MoE.

Pamokos pabaigoje turėtumėte sugebėti atsakyti į šiuos klausimus:

- Kas yra SLM?
- Kuo SLM skiriasi nuo LLM?
- Kas yra Microsoft Phi-3/3.5 šeima?
- Kaip atlikti inferenciją naudojant Microsoft Phi-3/3.5 šeimą?

Pasiruošę? Pradėkime.

## Didelių kalbos modelių (LLM) ir mažų kalbos modelių (SLM) skirtumai

Tiek LLM, tiek SLM yra sukurti remiantis tikėtinosios mašininio mokymosi pagrindais, jų architektūros dizainas, mokymo metodikos, duomenų generavimo procesai ir modelių vertinimo metodai yra panašūs. Tačiau keli svarbūs veiksniai skiria šiuos du modelių tipus.

## Mažų kalbos modelių taikymas

SLM naudojami įvairiose srityse, įskaitant:

- Pokalbių robotai: teikti klientų palaikymą ir bendrauti su naudotojais pokalbio forma.
- Turinys kūrimas: padėti rašytojams generuoti idėjas arba net rengti visus straipsnius.
- Švietimas: padėti studentams rašymo užduotyse ar mokantis naujų kalbų.
- Prieinamumas: kurti įrankius neįgaliesiems, pavyzdžiui, teksto į kalbą sistemas.

**Dydis**
  
Pagrindinis skirtumas tarp LLM ir SLM yra modelių mastas. LLM, kaip ChatGPT (GPT-4), gali turėti apie 1,76 trilijono parametrų, o atviro kodo SLM, tokie kaip Mistral 7B, sukurti su ženkliai mažesniu parametrų skaičiumi – maždaug 7 milijardais. Šis skirtumas daugiausia kyla iš architektūros ir mokymo procesų skirtumų. Pavyzdžiui, ChatGPT naudoja savidėmes mechanizmą koderio-dekoderio pagrindu, o Mistral 7B naudoja slenkamąjį lango dėmesį, leidžiantį efektyviau mokytis dekoderio modeliui. Šis architektūrinis skirtumas turi gilių pasekmių modelių sudėtingumui ir našumui.

**Supratimas**

SLM įprastai optimizuojami veikimui specifinėse srityse, todėl tampa labai specializuoti, bet galimai riboti plačiai kontekstinei informacijai iš skirtingų žinių sričių. Priešingai, LLM siekia imituoti žmogaus intelektą platesniu mastu. Mokomi didelių ir įvairių duomenų rinkinių, LLM sukurti taip, kad gerai veiktų įvairiose srityse, pasižymi daugiau universalumo ir prisitaikymo galimybių. Dėl to LLM labiau tinkami platesnėms užduotims, pavyzdžiui, natūralios kalbos apdorojimui ir programavimui.

**Skaičiavimai**

LLM mokymas ir diegimas reikalauja daug resursų, dažnai reikia didelės skaičiavimo infrastruktūros, įskaitant dideles GPU klasterių sistemas. Pavyzdžiui, visiškas ChatGPT mokymas gali reikalauti tūkstančių GPU per ilgą laiką. Priešingai, SLM, su mažesniu parametrų skaičiumi, yra prieinamesni naudojant mažesnius skaičiavimo išteklius. Tokius modelius kaip Mistral 7B galima mokyti ir vykdyti vietinėse mašinose su vidutinėmis GPU galimybėmis, nors mokymas užtrunka kelias valandas keliose GPU.

**Šališkumas**

Šališkumas yra žinoma problema LLM, daugiausia dėl mokymo duomenų pobūdžio. Šie modeliai dažnai remiasi neapdorotais viešai prieinamais internetiniais duomenimis, kurie gali nepakankamai ar klaidingai atstovauti tam tikras grupes, įvesti klaidingą ženklinimą ar atspindėti lingvistines šališkumo formas, susijusias su dialektu, geografiniais skirtumais ir gramatinėmis taisyklėmis. Be to, sudėtinga LLM architektūra gali netyčia stiprinti šališkumą, kuris gali likti nepastebėtas be kruopštaus tobulinimo. Kitoje pusėje, SLM, būdami mokyti iš labiau apribotų ir sritinių duomenų rinkinių, yra mažiau linkę į tokias šališkumo formas, tačiau ir jie nėra visiškai apsaugoti nuo jų.

**Inferencija**

Mažesnis SLM dydis suteikia jiems reikšmingą pranašumą inferencijos greičio atžvilgiu, leidžiant efektyviai generuoti rezultatus vietinėje technikoje be reikalo naudoti didelį lygiagretų apdorojimą. Priešingai, LLM, dėl dydžio ir sudėtingumo, dažnai reikalauja reikšmingų lygiagrečių skaičiavimo išteklių priimtino inferencijos laiko pasiekimui. Daug naudotojų vienu metu apsunkina LLM reakcijos laiką, ypač diegiant didelio masto sistemose.

Apibendrinant, nors tiek LLM, tiek SLM yra mašininio mokymosi pagrindais, jie ženkliai skiriasi modelio dydžiu, išteklių poreikiais, kontekstiniu supratimu, polinkiu į šališkumą ir inferencijos greičiu. Šie skirtumai atspindi jų tinkamumą įvairiems naudojimo atvejams, LLM būdami universalesni, bet skaičiavimo išteklius reikalaujantys, o SLM suteikia efektyvumą pagal sritis su mažesniais techniniais reikalavimais.

***Pastaba: šioje pamokoje SLM supažindinsime naudojant Microsoft Phi-3 / 3.5 pavyzdį.***

## Phi-3 / Phi-3.5 šeimos pristatymas

Phi-3 / 3.5 šeima daugiausia orientuota į teksto, vaizdų ir Agent (MoE) taikymo scenarijus:

### Phi-3 / 3.5 Instruct

Pagrindinės paskirtys: teksto generavimas, pokalbių užbaigimas, turinio informacijos išgavimas ir pan.

**Phi-3-mini**

3.8B kalbos modelis prieinamas Microsoft Foundry, Hugging Face ir Ollama platformose. Phi-3 modeliai reikšmingai pranoksta savo lygio ir net didesnius kalbos modelius pagrindiniuose etalonų testuose (žr. žemiau esančius etalonų skaičius, didesni skaičiai – geriau). Phi-3-mini pranoksta modelius, turinčius dvigubai daugiau parametrų, o Phi-3-small ir Phi-3-medium lenkia dar didesnius modelius, įskaitant GPT-3.5.

**Phi-3-small ir medium**

Phi-3-small su vos 7B parametrais lenkia GPT-3.5T įvairiuose kalbos, samprotavimo, programavimo ir matematikos etalonuose.

Phi-3-medium su 14B parametrais tęsia šią tendenciją ir lenkia Gemini 1.0 Pro.

**Phi-3.5-mini**

Galima laikyti tai Phi-3-mini atnaujinimu. Parametrų skaičius lieka tas pats, bet pagerėja kelias kalbas palaikanti funkcija (palaiko 20+ kalbų: arabų, kinų, čekų, danų, olandų, anglų, suomių, prancūzų, vokiečių, hebrajų, vengrų, italų, japonų, korėjiečių, norvegų, lenkų, portugalų, rusų, ispanų, švedų, tajų, turkų, ukrainiečių) ir pridedama stipresnė ilgų kontekstų palaikymo galimybė.

Phi-3.5-mini su 3.8B parametrais pranoksta tokio paties dydžio kalbos modelius ir yra lygiavertis modeliams, turintiems dvigubai daugiau parametrų.

### Phi-3 / 3.5 Vision

Galima manyti, kad Phi-3/3.5 Instruct modelis atspindi Phi gebėjimą suprasti, o Vision suteikia Phi akis, kad jis galėtų suprasti pasaulį.


**Phi-3-Vision**

Phi-3-Vision, turintis tik 4.2B parametrų, tęsia šią tendenciją ir pranoksta didesnius modelius, tokius kaip Claude-3 Haiku ir Gemini 1.0 Pro V, bendrose vizualinio samprotavimo, OCR, lentelių ir diagramų supratimo užduotyse.


**Phi-3.5-Vision**

Phi-3.5-Vision taip pat yra Phi-3-Vision atnaujinimas, pridedantis palaikymą kelioms nuotraukoms. Tai galima laikyti regėjimo pagerinimu – ne tik gali matyti paveikslėlius, bet ir vaizdo įrašus.

Phi-3.5-Vision pranoksta didesnius modelius, tokius kaip Claude-3.5 Sonnet ir Gemini 1.5 Flash, OCR, lentelių ir diagramų supratimo užduotyse, ir yra lygiavertis bendro vizualinio žinių samprotavimo užduotyse. Palaiko kelių kadrų įvestį, t.y., atlieka samprotavimą pagal kelis įvaizdinius įrašus.


### Phi-3.5-MoE

***Ekspertų mišinys (MoE)*** leidžia modeliams būti išankstiniam mokymui su žymiai mažesnėmis skaičiavimo išlaidomis, o tai reiškia, kad galite žymiai išplėsti modelio ar duomenų rinkinio dydį naudojant tą patį skaičiavimo biudžetą kaip tankus modelis. Ypač, MoE modelis turėtų pasiekti tokį pat kokybės lygį kaip ir jo tankus analogas daug greičiau išankstinio mokymo metu.

Phi-3.5-MoE sudarytas iš 16x3.8B ekspertų modulių. Phi-3.5-MoE su vos 6.6B aktyvių parametrų pasiekia panašų samprotavimo, kalbos supratimo ir matematikos lygį kaip daug didesni modeliai.

Galime naudoti Phi-3/3.5 šeimos modelį atsižvelgdami į skirtingus scenarijus. Skirtingai nuo LLM, Phi-3/3.5-mini arba Phi-3/3.5-Vision galima diegti kraštiniuose įrenginiuose.


## Kaip naudoti Phi-3/3.5 šeimos modelius

Tikimės naudoti Phi-3/3.5 skirtinguose scenarijuose. Toliau naudosime Phi-3/3.5 pagal skirtingas situacijas.

![phi3](../../../translated_images/lt/phi3.655208c3186ae381.webp)

### Inferencija per debesijos API

**Microsoft Foundry Modeliai**

> **Pastaba:** GitHub Modeliai bus nutraukti iki 2026 m. liepos pabaigos. [Microsoft Foundry Modeliai](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) yra tiesioginė pakeitimo alternatyva.

Microsoft Foundry Modeliai yra tiesiausias būdas. Per Foundry modelių katalogą galite greitai pasiekti Phi-3/3.5-Instruct modelį. Kombinuojant su Azure AI Inference SDK / OpenAI SDK, API pasiekiama per kodą, atliekant Phi-3/3.5-Instruct užklausą. Taip pat galite išbandyti įvairius efektus per Playground.

- Demo: Phi-3-mini ir Phi-3.5-mini efektų palyginimas kinų kalbos scenarijuose

![phi3](../../../translated_images/lt/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/lt/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Jei norite naudoti vizijos ir MoE modelius, taip pat galite naudoti Microsoft Foundry užklausai atlikti. Jei domina, galite perskaityti Phi-3 Cookbook, kaip atlikti Phi-3/3.5 Instruct, Vision, MoE užklausas per Microsoft Foundry [Spustelėkite čia](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Be debesijos pagrindu veikiančio Microsoft Foundry Modelių katalogo, taip pat galite naudoti [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) užklausoms atlikti. NVIDIA NIM (NVIDIA Inference Microservices) yra pagreitintų inferencijos mikroservisų rinkinys, sukurtas padėti kūrėjams efektyviai diegti DI modelius įvairiose aplinkose, įskaitant debesijas, duomenų centrus ir darbo stotis.

Štai keletas svarbių NVIDIA NIM funkcijų:

- **Paprastas diegimas:** NIM leidžia diegti DI modelius vienu komandos paleidimu, todėl lengva integruoti į esamus darbo srautus.

- **Optimizuotas našumas:** Jis naudoja NVIDIA iš anksto optimizuotus apdorojimo variklius, tokius kaip TensorRT ir TensorRT-LLM, užtikrindamas mažą vėlavimą ir didelį pralaidumą.
- **Mastelio keitimas:** NIM palaiko automatinį mastelio keitimą Kubernetes, leidžiantį efektyviai tvarkyti kintančias apkrovas.
- **Saugumas ir valdymas:** Organizacijos gali išlaikyti kontrolę savo duomenims ir programoms savarankiškai diegdamos NIM mikroservisus savo valdomoje infrastruktūroje.
- **Standartiniai API:** NIM teikia pramonės standartus atitinkančius API, todėl lengva kurti ir integruoti AI programas, tokias kaip pokalbių robotai, AI asistentai ir kt.

NIM yra NVIDIA AI Enterprise dalis, kurios tikslas – supaprastinti AI modelių diegimą ir eksploatavimą, užtikrinant efektyvų jų veikimą NVIDIA GPU.

- Demonstracija: NVIDIA NIM naudojimas Phi-3.5-Vision-API kvietimui [[Spauskite čia](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5 paleidimas lokaliai
Apdorojimas, susijęs su Phi-3 ar bet kuriuo kalbos modeliu, tokiu kaip GPT-3, reiškia atsakymų ar prognozių generavimo procesą remiantis įvestimi. Kai pateikiate užklausą arba klausimą Phi-3, jis naudoja savo išmokytą neuroninį tinklą, kad prognozuotų tikėtiniausią ir aktualiausią atsakymą, analizuodamas modelio treniravimo duomenų šablonus ir ryšius.

**Hugging Face Transformer**
Hugging Face Transformers yra galinga biblioteka, skirta natūralios kalbos apdorojimui (NLP) ir kitoms mašininio mokymosi užduotims. Štai keletas svarbiausių jos aspektų:

1. **Iš anksto apmokyti modeliai:** Biblioteka teikia tūkstančius iš anksto apmokytų modelių, skirtų įvairioms užduotims, tokioms kaip teksto klasifikavimas, atpažinimo vardinių objektų, klausimų-atsakymų, santraukų sudarymo, vertimo ir teksto generavimo.

2. **Sistemų tarpusavio suderinamumas:** Biblioteka palaiko kelis giluminio mokymo karkasus, įskaitant PyTorch, TensorFlow ir JAX. Tai leidžia viename karkase treniruoti modelį ir naudoti jį kitame.

3. **Daugiapoliai gebėjimai:** Be NLP, Hugging Face Transformers taip pat palaiko užduotis kompiuterinėje vizijoje (pvz., vaizdų klasifikacija, objektų atpažinimas) ir garso apdorojime (pvz., kalbos atpažinimas, garso klasifikacija).

4. **Paprastas naudojimas:** Biblioteka siūlo API ir įrankius patogiam modelių atsisiuntimui ir derinimui, todėl ji prieinama tiek pradedantiesiems, tiek ekspertams.

5. **Bendruomenė ir ištekliai:** Hugging Face turi gyvybingą bendruomenę ir išsamią dokumentaciją, mokomuosius ir gidus, kurie padeda pradėti darbą ir pilnai išnaudoti biblioteką.
[oficiali dokumentacija](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) arba jų [GitHub saugykla](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Tai dažniausiai naudojamas metodas, tačiau jis taip pat reikalauja GPU pagreitinto apdorojimo. Galų gale, tokios situacijos kaip Vision ir MoE reikalauja daug skaičiavimų, kurie be kiekybinimo CPU būtų labai lėti.


- Demonstracija: Transformer naudojimas Phi-3.5-Instruct kvietimui [Spauskite čia](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demonstracija: Transformer naudojimas Phi-3.5-Vision kvietimui [Spauskite čia](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demonstracija: Transformer naudojimas Phi-3.5-MoE kvietimui [Spauskite čia](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) yra platforma, skirta palengvinti didelių kalbos modelių (LLM) paleidimą lokaliai jūsų kompiuteryje. Ji palaiko įvairius modelius, tokius kaip Llama 3.1, Phi 3, Mistral ir Gemma 2 bei kitus. Platforma supaprastina procesą sujungdama modelio svorius, konfigūraciją ir duomenis į vieną paketą, todėl vartotojams lengviau pritaikyti ir kurti savo modelius. Ollama prieinama macOS, Linux ir Windows sistemoms. Tai puikus įrankis tiems, kurie nori eksperimentuoti arba diegti LLM be debesų paslaugų. Ollama yra tiesiausias kelias, tereikia vykdyti šią komandą.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) yra Microsoft neprisijungimo režimo vykdymo aplinka modeliams, tokiems kaip Phi, veikti visiškai jūsų pačių aparatinėje įrangoje – nereikia Azure prenumeratos, API rakto ar tinklo ryšio. Jis automatiškai pasirenka geriausiai prieinamą vykdymo tiekėją (NPU, GPU arba CPU) ir pateikia OpenAI suderinamą galinį tašką, tad esamas `openai`/Azure AI Inference SDK kodas gali jį naudoti su minimaliais pakeitimais. Daugiau informacijos rasite [Foundry Local dokumentacijoje](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst).

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Arba naudokite SDK tiesiogiai Python kalboje:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime generatyviai AI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) yra daugiaplatformė mašininio mokymosi greitinimo aplinka inferencijai ir treniravimui. ONNX Runtime generatyviai AI (GENAI) yra galingas įrankis, padedantis efektyviai vykdyti generatyvių AI modelių inferenciją įvairiose platformose.

## Kas yra ONNX Runtime?
ONNX Runtime yra atviro kodo projektas, leidžiantis aukšto našumo mašininio mokymosi modelių inferenciją. Jis palaiko modelius Open Neural Network Exchange (ONNX) formatu, kuris yra standartas mašininio mokymosi modelių atvaizdavimui. ONNX Runtime inferencija leidžia greičiau aptarnauti klientus ir sumažinti išlaidas, palaikydama modelius iš giluminio mokymosi karkasų, tokių kaip PyTorch ir TensorFlow/Keras, taip pat klasikinių mašininio mokymosi bibliotekų, tokių kaip scikit-learn, LightGBM, XGBoost ir kt. ONNX Runtime suderinamas su skirtinga aparatine įranga, tvarkyklėmis ir operacinėmis sistemomis, siūlydamas optimalų našumą naudodamas aparatinio spartinimo galimybes kartu su grafų optimizacijomis ir transformacijomis.

## Kas yra Generatyvi AI?
Generatyvi AI reiškia AI sistemas, gebančias generuoti naują turinį – pvz., tekstą, vaizdus ar muziką – remiantis jomis apmokytais duomenimis. Pavyzdžiai apima kalbos modelius, tokius kaip GPT-3, ir vaizdų generavimo modelius, tokius kaip Stable Diffusion. ONNX Runtime for GenAI biblioteka teikia generatyvios AI ciklą ONNX modeliams, įskaitant inferenciją su ONNX Runtime, logitų apdorojimą, paiešką ir mėginių ėmimą bei KV talpyklos valdymą.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI išplečia ONNX Runtime galimybes, palaikydama generatyvius AI modelius. Štai keletas pagrindinių funkcijų:

- **Plati platformų palaikymas:** Veikia įvairiose platformose, įskaitant Windows, Linux, macOS, Android ir iOS.
- **Modelių palaikymas:** Palaiko daugelį populiarių generatyvių AI modelių, tokių kaip LLaMA, GPT-Neo, BLOOM ir kt.
- **Našumo optimizavimas:** Apima optimizacijas įvairiems aparatūros spartintuvams, tokiems kaip NVIDIA GPU, AMD GPU ir kiti.
- **Paprastas naudojimas:** Teikia API patogiam integravimui į programas, leidžiančias generuoti tekstą, vaizdus ir kitą turinį su minimaliu kodo kiekiu.
- Vartotojai gali iškviesti aukšto lygio generate() metodą arba vykdyti kiekvieną modelio iteraciją cikle, generuodami po vieną ženklą ir, esant reikalui, keisdami generavimo parametrus ciklo viduje.
- ONNX Runtime taip pat palaiko godžią (greedy)/spindulių paiešką (beam search) ir TopP, TopK mėginių ėmimą ženklų sekų generavimui bei įmontuotą logitų apdorojimą, pvz., kartojimų bausmes. Taip pat galite lengvai pridėti savo įvertinimus.

## Pradžia
Norėdami pradėti naudoti ONNX Runtime for GENAI, atlikite šiuos veiksmus:

### Įdiekite ONNX Runtime:
```Python
pip install onnxruntime
```
### Įdiekite Generatyvios AI plėtinius:
```Python
pip install onnxruntime-genai
```

### Paleiskite modelį: Štai paprastas pavyzdys Python kalboje:
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
### Demonstracija: ONNX Runtime GenAI naudojimas Phi-3.5-Vision kvietimui


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

Be ONNX Runtime, Ollama ir Foundry Local referencinių metodų, taip pat galime papildyti kiekybinių modelių pavyzdžius pagal įvairių gamintojų pateiktus modelių referencinius metodus. Pavyzdžiui, Apple MLX karkasas su Apple Metal, Qualcomm QNN su NPU, Intel OpenVINO su CPU/GPU ir kt. Daugiau informacijos rasite [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Daugiau

Mes išmokome Phi-3/3.5 šeimos pagrindus, tačiau norint sužinoti daugiau apie SLM, reikia daugiau žinių. Atsakymus galite rasti Phi-3 Cookbook. Jei norite sužinoti daugiau, apsilankykite [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->