# Įvadas į mažus kalbos modelius generatyviajai AI pradedantiesiems
Generatyvioji dirbtinė inteligencija yra įdomi dirbtinio intelekto sritis, kuri sutelkia dėmesį į sistemų kūrimą, gebančių generuoti naują turinį. Šis turinys gali apimti tekstą, vaizdus, muziką ir net visą virtualią aplinką. Viena įdomiausių generatyviosios AI taikymo sričių yra kalbos modeliai.

## Kas yra maži kalbos modeliai?

Mažas kalbos modelis (SLM) yra sumažinta didelio kalbos modelio (LLM) versija, taikanti daug architektūrinių principų ir technikų iš LLM, tačiau turinti ženkliai mažesnį skaičiavimo apkrovą.

SLM yra kalbos modelių poaibis, skirtas generuoti žmogiškai panašų tekstą. Skirtingai nei didesni modeliai, tokie kaip GPT-4, SLM yra kompaktiškesni ir efektyvesni, todėl puikiai tinka taikymams, kuriuose yra ribotos skaičiavimo ištekliai. Nepaisant mažesnio dydžio, jie vis tiek gali atlikti įvairias užduotis. Paprastai SLM sukurti per didelių kalbos modelių suspaudimą ar destiliavimą, siekiant išlaikyti didelę dalį originalaus modelio funkcionalumo ir kalbinių gebėjimų. Modelio dydžio sumažinimas mažina bendrą sudėtingumą, todėl SLM efektyvesni tiek atminties, tiek skaičiavimo poreikio atžvilgiu. Nepaisant šių optimizacijų, SLM gali atlikti platų natūralios kalbos apdorojimo (NLP) užduočių spektrą:

- Teksto generavimas: Kurti nuoseklias ir kontekstualiai tinkamas sakinių ar pastraipų sekas.
- Teksto užbaigimas: Prognozuoti ir užbaigti sakinius pagal pateiktą užuominą.
- Vertimas: Versti tekstą iš vienos kalbos į kitą.
- Santrauka: Trumpinti ilgus tekstus į trumpesnes, lengviau suvokiamas santraukas.

Nors tam tikrais atvejais tenka aukoti našumą ar gilesnį supratimą, palyginti su didesniais modeliais.

## Kaip veikia maži kalbos modeliai?
SLM treniruojami naudojant didžiulius tekstų duomenų kiekius. Mokymo metu jie išmoksta kalbos modelius ir struktūras, leidžiančias generuoti gramatiškai teisingą ir kontekstualiai tinkamą tekstą. Mokymo procesas apima:

- Duomenų rinkimą: didelių tekstų duomenų rinkinių surinkimą iš įvairių šaltinių.
- Duomenų paruošimą: duomenų valymą ir organizavimą, kad jie būtų tinkami mokymui.
- Mokymą: mašininio mokymosi algoritmų naudojimą, kad modelis išmoktų suprasti ir generuoti tekstą.
- Fino sureguliavimą: modelio koregavimą tam, kad pagerinti našumą konkrečiose užduotyse.

SLM kūrimas atitinka augančią poreikį modeliams, kurie gali būti paleidžiami ribotų išteklių aplinkose, pvz., mobiliuosiuose įrenginiuose ar skaičiavimo periferijoje, kur pilnos apimties LLM gali būti nepraktiški dėl didelių išteklių poreikių. Sutelkdami dėmesį į efektyvumą, SLM suderina našumą su prieinamumu, leidžiant taikyti juos platesniuose domenuose.

![slm](../../../translated_images/lt/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Mokymosi tikslai

Šio pamokos metu siekiame supažindinti su SLM žiniomis ir susieti jas su Microsoft Phi-3, kad išmoktumėte skirtingų scenarijų teksto, vaizdų ir MoE srityse.

Pamokos pabaigoje turėtumėte mokėti atsakyti į šiuos klausimus:

- Kas yra SLM?
- Kuo skiriasi SLM nuo LLM?
- Kas yra Microsoft Phi-3/3.5 šeima?
- Kaip vykdyti išvedimą su Microsoft Phi-3/3.5 šeima?

Pasiruošę? Pradėkime.

## Skirtumai tarp didelių kalbos modelių (LLM) ir mažų kalbos modelių (SLM)

Tiek LLM, tiek SLM remiasi tikimybinio mašininio mokymosi pagrindais, panašiomis architektūros, mokymo, duomenų generavimo ir modelio vertinimo metodikomis. Tačiau keletas pagrindinių veiksnių skiria šiuos modelių tipus.

## Mažų kalbos modelių taikymo sritys

SLM turi platų taikymo spektrą, įskaitant:

- Pokalbių robotai: teikti klientų aptarnavimą ir bendrauti su vartotojais pokalbių forma.
- Turinys kūrimas: padėti rašytojams generuoti idėjas ar net kurti visus straipsnius.
- Švietimas: padėti studentams rašyti užduotis ar mokytis naujų kalbų.
- Prieinamumas: kurti priemones neįgaliems, pvz., teksto į kalbą sistemas.

**Dydis**
  
Pagrindinis skirtumas tarp LLM ir SLM yra modelio mastelis. LLM, pavyzdžiui, ChatGPT (GPT-4), gali turėti apie 1,76 trilijono parametrų, tuo tarpu atvirojo kodo SLM, tokie kaip Mistral 7B, turi žymiai mažiau – apie 7 milijardus parametrų. Šis skirtumas daugiausia susijęs su architektūra ir mokymo procesu. Pavyzdžiui, ChatGPT naudoja savos dėmesio mechanizmą su dekoderiu ir užkoduotoju, o Mistral 7B taiko slenkamojo lango dėmesį, leidžiantį efektyviau mokytis tik su dekoderiu. Šis architektūrinis skirtumas turi didelės įtakos sudėtingumui ir našumui.

**Supratimas**

SLM dažniausiai optimizuojami tam tikriems domenams, todėl yra labai specializuoti, bet gali būti riboti plačiajam kontekstiniam supratimui keliuose srityse. Priešingai, LLM siekia imituoti žmogišką intelektą platesniu mastu. Jie treniruojami su įvairiais dideliais duomenų rinkiniais ir sugeba dirbti įvairiuose domenuose, pasižymint didesniu universalumu ir prisitaikymu. Todėl LLM geriau tinka platesniam spektrui užduočių, pavyzdžiui, natūralios kalbos apdorojimui ir programavimui.

**Skaičiavimas**

LLM mokymas ir diegimas yra išteklius reikalaujantys procesai, dažnai reikalaujantys didelių GPU klasterių. Pavyzdžiui, treniruojant ChatGPT nuo nulio, gali prireikti tūkstančių GPU ir daugybės valandų. Priešingai, SLM, turint mažesnį parametrų skaičių, yra prieinamesni skaičiavimo išteklių prasme. Pavyzdžiui, Mistral 7B galima treniruoti ir naudoti vietiniuose kompiuteriuose su vidutinėmis GPU galimybėmis, nors mokymas vis tiek užtrunka kelias valandas keliuose GPU.

**Šališkumas**

Šališkumas yra žinoma problema LLM, daugiausia dėl treniruočių duomenų pobūdžio. Šie modeliai dažnai remiasi interneto atvirais duomenimis, kurie gali nepakankamai atspindėti tam tikras grupes, turėti klaidinančius ženklinimus arba atspindėti lingvistinius šališkumus, susijusius su dialektais, geografiniais skirtumais ir gramatinėmis taisyklėmis. Be to, LLM architektūros sudėtingumas gali netyčia padidinti šališkumą, kuriam nesant kruopštaus fino sureguliavimo gali likti nepastebėtam. Kita vertus, SLM, mokomi ribotais, specifiniais duomenų rinkiniais, yra mažiau linkę į tokius šališkumus, nors nėra visiškai apsaugoti.

**Išvedimas**

Mažesnis SLM dydis suteikia reikšmingą pranašumą išvedimo greičio atžvilgiu, leidžiant efektyviai generuoti rezultatus vietinėje įrangoje be didelio lygiagretaus skaičiavimo poreikio. Priešingai, LLM dėl savo dydžio ir sudėtingumo dažnai reikalauja didelių lygiagrečių išteklių, kad pasiektų priimtinus atsakymo laikus. Daug vartotojų vienu metu dar labiau sulėtina LLM atsakymo laiką, ypač naudojant juos masteliais.

Apibendrinant, nors LLM ir SLM remiasi panašiais mašininio mokymosi principais, jie ženkliai skiriasi modelio dydžiu, resursų poreikiais, kontekstiniu supratimu, šališkumo linksmumu ir išvedimo greičiu. Šie skirtumai atspindi jų tinkamumą skirtingoms taikymo sritims – LLM yra universalesni, bet reikalauja daug resursų, o SLM – efektyvesni specifiniams domenams, su mažesniais skaičiavimo poreikiais.

***Pastaba: šioje pamokoje supažindinsime su SLM naudojant Microsoft Phi-3 / 3.5 modelių pavyzdį.***

## Supažindinimas su Phi-3 / Phi-3.5 šeima

Phi-3 / 3.5 šeima daugiausia skirta tekstų, vizijos ir agentų (MoE) taikymo scenarijams:

### Phi-3 / 3.5 Instruct

Pagrinde skirta teksto generavimui, pokalbių užbaigimui ir turinio informacijos išgavimui ir pan.

**Phi-3-mini**

3,8 mlrd. parametrų kalbos modelis yra prieinamas Microsoft Foundry, Hugging Face ir Ollama platformose. Phi-3 modeliai reikšmingai pranoksta tokio pat dydžio arba didesnius kalbos modelius pagrindiniuose testuose (žr. testų rezultatus žemiau, didesni skaičiai geresni). Phi-3-mini pranoksta modelius, kurie yra du kartus didesni, o Phi-3-small ir Phi-3-medium pranoksta dar didesnius modelius, įskaitant GPT-3.5.

**Phi-3-small ir medium**

Su tik 7 mlrd. parametrų, Phi-3-small pranoksta GPT-3.5T įvairiuose kalbos, loginio mastymo, programavimo ir matematikos testuose.

14 mlrd. parametrų Phi-3-medium tęsia šią tendenciją ir pranoksta Gemini 1.0 Pro modelį.

**Phi-3.5-mini**

Galime laikyti tai Phi-3-mini patobulinimu. Parametrai išlieka tie patys, tačiau pagerėja galimybė palaikyti kelias kalbas (palaiko daugiau nei 20 kalbų: arabų, kinų, čekų, danų, olandų, anglų, suomių, prancūzų, vokiečių, hebrajų, vengrų, italų, japonų, korėjiečių, norvegų, lenkų, portugalų, rusų, ispanų, švedų, tailandų, turkų, ukrainiečių) ir pridedama stipresnė ilgų kontekstų palaikymo galimybė.

Phi-3.5-mini su 3,8 mlrd. parametru pranoksta tokio pat dydžio kalbos modelius ir yra lygiavertis su modeliais, kurie yra du kartus didesni.

### Phi-3 / 3.5 Vision

Galime laikyti, kad Phi-3/3.5 Instruct modelis suteikia Phi gebėjimą suprasti tekstus, o Vision yra tai, kas suteikia Phi akis pasaulio supratimui.


**Phi-3-Vision**

Phi-3-vision, turintis tik 4,2 mlrd. parametrų, tęsia šią tendenciją ir pranoksta didesnius modelius, tokius kaip Claude-3 Haiku ir Gemini 1.0 Pro V, bendrose vizualinio mastymo užduotyse, OCR, lentelių ir diagramų supratime.


**Phi-3.5-Vision**

Phi-3.5-Vision taip pat yra Phi-3-Vision patobulinimas, pridėdamas palaikymą kelioms nuotraukoms. Galima sakyti, kad tai yra vizijos patobulinimas – ne tik gali matyti paveikslėlius, bet ir vaizdo įrašus.

Phi-3.5-vision pranoksta didesnius modelius, tokius kaip Claude-3.5 Sonnet ir Gemini 1.5 Flash OCR, lentelių, diagramų užduotyse ir yra lygiavertis bendro išsilavinimo vizualinio supratimo užduotyse. Palaiko kelių kadrų įvestį, tai yra, gali atlikti mastymą pagal kelis įvesties paveikslėlius.


### Phi-3.5-MoE

***Mišrių ekspertų modelis (MoE)*** leidžia modeliams būti iš anksto apmokytiems su daug mažesne skaičiavimo sąnauda, tai reiškia, kad galite ženkliai padidinti modelio arba duomenų rinkinio dydį turėdami tokį pat skaičiavimo biudžetą kaip tankus modelis. Ypač MoE modelis turėtų pasiekti tokį pat kokybės lygį kaip tankus modelis daug greičiau iš anksto treniravimo metu.

Phi-3.5-MoE susideda iš 16 x 3,8 mlrd. ekspertų modulių. Phi-3.5-MoE su vos 6,6 mlrd. aktyvių parametrų pasiekia panašų loginio mastymo, kalbos supratimo ir matematikos našumą kaip žymiai didesni modeliai.

Galime naudoti Phi-3/3.5 šeimos modelius skirtingoms scenarijoms. Skirtingai nuo LLM, galima diegti Phi-3/3.5-mini arba Phi-3/3.5-Vision periferinėje įrangoje.


## Kaip naudoti Phi-3/3.5 šeimos modelius

Tikimės naudoti Phi-3/3.5 skirtingose scenarijose. Toliau naudosime Phi-3/3.5 pagrindu skirtingoms situacijoms.

![phi3](../../../translated_images/lt/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Išvedimas per debesų API

**Microsoft Foundry modeliai**

> **Pastaba:** GitHub modeliai bus nutraukti 2026 m. liepos pabaigoje. [Microsoft Foundry modeliai](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) yra tiesioginė jų pakaitalas.

Microsoft Foundry modeliai yra tiesiausias kelias. Galite greitai pasiekti Phi-3/3.5-Instruct modelį per Foundry modelių katalogą. Derinant su Azure AI Inference SDK / OpenAI SDK, galite pasiekti API per kodą ir atlikti Phi-3/3.5-Instruct užklausas. Taip pat galite išbandyti įvairius efektus per žaidimų aikštelę (Playground).

- Demonstracija: Phi-3-mini ir Phi-3.5-mini efektų palyginimas kinų kalbos scenarijuose

![phi3](../../../translated_images/lt/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/lt/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Arba, jeigu norite naudoti vizijos ir MoE modelius, galite naudoti Microsoft Foundry užklausoms atlikti. Jei domina, galite perskaityti Phi-3 virtuvės knygą (cookbook), kaip naudoti Phi-3/3.5 Instruct, Vision, MoE per Microsoft Foundry [Spustelėkite čia](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Be debesų pagrindu veikiančio Microsoft Foundry modelių katalogo, taip pat galite naudoti [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) atlikti susijusias užklausas. Apsilankykite NVIDIA NIM, kad atliktumėte Phi-3/3.5 šeimos API užklausas. NVIDIA NIM (NVIDIA Inference Microservices) yra greitai veikiančių išvedimo mikropaslaugų rinkinys, sukurtas padėti kūrėjams efektyviai diegti AI modelius įvairiose aplinkose, įskaitant debesis, duomenų centrus ir darbostotis.

Štai keletas pagrindinių NVIDIA NIM savybių:

- **Paprastas diegimas:** NIM leidžia AI modelius paleisti vienu komandų sakiniu, todėl lengva integruoti į esamus darbo procesus.
- **Optimizuotas našumas:** įgalina naudoti NVIDIA iš anksto apdorotus išvedimo variklius, tokius kaip TensorRT ir TensorRT-LLM, užtikrinant mažą delsą ir didelį pralaidumą.
- **Mastelio keitimas:** NIM palaiko automatinį skalavimą Kubernetes, leidžiantį efektyviai valdyti kintantį darbo krūvį.
- **Saugumas ir kontrolė:** organizacijos gali išlaikyti kontrolę savo duomenims ir programoms veikiant savarankiškai valdomose infrastruktūrose su NIM mikropaslaugomis.
- **Standartiniai API:** NIM suteikia pramoninius standartinius API, leidžiančius lengvai kurti ir integruoti DI programas, tokias kaip pokalbių robotai, DI asistentai ir kt.

NIM yra NVIDIA AI Enterprise dalis, kurios tikslas – supaprastinti DI modelių diegimą ir eksploatavimą, užtikrinant jų efektyvų veikimą NVIDIA GPU.

- Demo: Naudojant NVIDIA NIM kvietimui Phi-3.5-Vision-API  [[Spustelėkite šią nuorodą](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5 vietinis paleidimas
Inferencija, susijusi su Phi-3 ar bet kokiu kalbos modeliu, pavyzdžiui, GPT-3, reiškia procesą, kai generuojamos atsakomosios žinutės ar prognozės remiantis gaunamu įvesties duomenimis. Pateikus užklausą ar klausimą Phi-3, jis naudoja apmokytą neuroninį tinklą, kad įvertintų tikėtiniausią ir aktualiausią atsakymą, analizuoja duomenų, kuriais buvo apmokytas, šablonus ir ryšius.

**Hugging Face Transformer**
Hugging Face Transformers yra galinga biblioteka, skirta natūralios kalbos apdorojimui (NLP) ir kitoms mašininio mokymosi užduotims. Štai keletas pagrindinių punktų apie ją:

1. **Iš anksto apmokyti modeliai**: Siūlo tūkstančius iš anksto apmokytų modelių, skirtų įvairioms užduotims, tokioms kaip teksto klasifikavimas, vardų atpažinimas, klausimų atsakymas, santraukų kūrimas, vertimas ir teksto generavimas.

2. **Kelių sistemų sąveika**: Biblioteka palaiko kelias giluminio mokymosi sistemas, įskaitant PyTorch, TensorFlow ir JAX. Tai leidžia apmokyti modelį vienoje sistemoje ir naudoti kitoje.

3. **Daugiakanalės galimybės**: Be NLP, Hugging Face Transformers palaiko užduotis kompiuterinėje vizijoje (pvz., vaizdų klasifikavimas, objektų aptikimas) ir garso apdorojime (pvz., kalbos atpažinimas, garso klasifikavimas).

4. **Lengva naudoti**: Biblioteka suteikia API ir įrankius modelių atsisiuntimui ir derinimui, todėl yra prieinama tiek pradedantiesiems, tiek ekspertams.

5. **Bendruomenė ir ištekliai**: Hugging Face turi gyvą bendruomenę, plačią dokumentaciją, mokymus ir gidus, padedančius vartotojams pradėti ir maksimaliai išnaudoti šią biblioteką.
[oficiali dokumentacija](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) arba jų [GitHub saugykla](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Tai dažniausiai naudojamas metodas, tačiau taip pat reikalinga GPU spartinimas. Juk tokiose srityse kaip Vision ir MoE reikia daug skaičiavimų, kurie CPU be kvantizavimo būtų labai lėti.


- Demo: Naudojant Transformer kvietimui Phi-3.5-Instruct [Spustelėkite šią nuorodą](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Naudojant Transformer kvietimui Phi-3.5-Vision [Spustelėkite šią nuorodą](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Naudojant Transformer kvietimui Phi-3.5-MoE [Spustelėkite šią nuorodą](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) yra platforma, skirta palengvinti didelių kalbos modelių (LLM) paleidimą vietoje jūsų įrenginyje. Ji palaiko įvairius modelius, tokius kaip Llama 3.1, Phi 3, Mistral ir Gemma 2, tarp kitų. Platforma supaprastina procesą sujungdama modelio svorius, konfigūraciją ir duomenis į vieną paketą, todėl vartotojams lengviau pritaikyti ir kurti savo modelius. Ollama yra prieinama macOS, Linux ir Windows sistemoms. Tai puikus įrankis, jei norite eksperimentuoti arba diegti LLM nepasikliaudami debesų paslaugomis. Ollama yra pats tiesiausias būdas, tereikia įvykdyti šią komandą.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) yra „Microsoft“ neprisijungęs, vietinis vykdymo laikotarpis modeliams, tokiems kaip Phi, kurie visiškai veikia ant jūsų nuosavo aparatinės įrangos – nereikia Azure prenumeratos, API rakto ar tinklo ryšio. Automatiškai parenka geriausią galimą vykdymo teikėją (NPU, GPU arba CPU) ir suteikia OpenAI suderinamą galinį tašką, todėl esamas `openai`/Azure AI Inference SDK kodas gali jį pasiekti su minimaliais pakeitimais. Norėdami pradėti, žiūrėkite [Foundry Local dokumentaciją](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst).

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

**ONNX Runtime generatyviajam DI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) yra daugiaplatforminė mašininio mokymosi inferencijos ir apmokymo spartintuvo platforma. ONNX Runtime generatyviajam DI (GENAI) yra galingas įrankis, padedantis efektyviai paleisti generatyvius DI modelius įvairiose platformose.

## Kas yra ONNX Runtime?
ONNX Runtime yra atvirojo kodo projektas, leidžiantis atlikti aukšto našumo mašininio mokymosi modelių inferenciją. Jis palaiko modelius Open Neural Network Exchange (ONNX) formatu, kuris yra standartas mašininio mokymosi modelių reprezentavimui.ONNX Runtime inferencija gali užtikrinti greitesnę naudotojų patirtį ir mažesnes išlaidas, palaikydamas modelius iš giluminio mokymosi sistemų, tokių kaip PyTorch ir TensorFlow/Keras, taip pat klasikinių mašininio mokymosi bibliotekų, pavyzdžiui, scikit-learn, LightGBM, XGBoost ir kt. ONNX Runtime yra suderinamas su įvairiomis aparatinės įrangos, tvarkyklių ir operacinių sistemų konfigūracijomis ir suteikia optimalų veikimą, pasinaudodamas aparatinės įrangos spartintuvais, kai įmanoma, kartu taikydamas grafų optimizacijas ir transformacijas.

## Kas yra generatyvusis DI?
Generatyvusis DI reiškia DI sistemas, galinčias kurti naują turinį, pavyzdžiui, tekstą, vaizdus ar muziką, remdamiesi duomenimis, kuriais jos buvo apmokytos. Pavyzdžiai yra kalbos modeliai, tokie kaip GPT-3, ir vaizdų generavimo modeliai, tokie kaip Stable Diffusion. ONNX Runtime generatyviam DI biblioteka suteikia generatyviąją DI kilpą ONNX modeliams, įskaitant inferenciją su ONNX Runtime, logitų apdorojimą, paiešką ir atrinkimą bei KV talpyklos valdymą.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI plečia ONNX Runtime galimybes, kad palaikytų generatyviuosius DI modelius. Štai keletas pagrindinių funkcijų:

- **Plati platformų palaikymas:** veikia įvairiose platformose, įskaitant Windows, Linux, macOS, Android ir iOS.
- **Modelių palaikymas:** palaiko daugybę populiarių generatyviųjų DI modelių, tokių kaip LLaMA, GPT-Neo, BLOOM ir kt.
- **Veikimo optimizavimas:** apima optimizacijas įvairiems aparatinės įrangos spartintuvams, tokiems kaip NVIDIA GPU, AMD GPU ir kiti.
- **Patogus naudojimas:** suteikia API paprastai integracijai į programas, leidžiančias generuoti tekstą, vaizdus ir kitą turinį su minimaliu kodo kiekiu.
- Vartotojai gali kvieti aukšto lygio generate() metodą arba vykdyti kiekvieną modelio iteraciją cikle, generuodami po vieną žetoną ir pagal pageidavimą atnaujindami generavimo parametrus ciklo metu.
- ONNX runtime taip pat palaiko greedy/beam paiešką ir TopP, TopK atrinkimą žetonų sekų generavimui bei integruotą logitų apdorojimą, pvz., pasikartojimų bausmes. Taip pat galite lengvai pridėti pasirinktinius įvertinimus.

## Pradžia
Norėdami pradėti darbą su ONNX Runtime for GENAI, galite atlikti šiuos veiksmus:

### Įdiekite ONNX Runtime:
```Python
pip install onnxruntime
```
### Įdiekite Generatyviojo DI plėtinius:
```Python
pip install onnxruntime-genai
```

### Paleiskite modelį: štai paprastas pavyzdys Python kalba:
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
### Demo: Naudojant ONNX Runtime GenAI kvietimui Phi-3.5-Vision


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

Be ONNX Runtime, Ollama ir Foundry Local nuorodų metodų, galime taip pat užbaigti kiekybinių modelių apžvalgą remdamiesi skirtingų gamintojų pateiktais modelių nuorodų metodais. Pavyzdžiui, Apple MLX sistema su Apple Metal, Qualcomm QNN su NPU, Intel OpenVINO su CPU/GPU ir kt. Daugiau informacijos rasite [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Daugiau

Mes išmokome Phi-3/3.5 šeimos pagrindus, tačiau norėdami sužinoti daugiau apie SLM, mums reikia daugiau žinių. Atsakymus rasite Phi-3 Cookbook. Jei norite sužinoti daugiau, apsilankykite [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->