# Sissejuhatus väikestesse keelemudelitesse generatiivse tehisintellekti jaoks algajatele
Generatiivne tehisintellekt on põnev tehisintellekti valdkond, mis keskendub süsteemide loomisele, mis suudavad genereerida uut sisu. See sisu võib ulatuda tekstist ja piltidest kuni muusika ja isegi tervete virtuaalsete keskkondadeni. Üks põnevamaid generatiivse tehisintellekti rakendusi on keelemudelite valdkonnas.

## Mis on väikesed keelemudelid?

Väike keelemudel (SLM) kujutab endast suurt keelemudelit (LLM) vähendatud versiooni, kasutades paljusid suurte keelemudelite arhitektuurilisi põhimõtteid ja tehnikaid, kuid omades oluliselt väiksemat arvutuslikku jalajälge.

Väikesed keelemudelid on keelemudelite alamkomplekt, mis on loodud inimkeele sarnase teksti genereerimiseks. Erinevalt suurematest mudelitest, nagu GPT-4, on SLM-id kompaktsed ja tõhusad, mistõttu sobivad nad hästi rakendusteks, kus arvutusressursid on piiratud. Hoolimata oma väiksemast suurusest, suudavad nad siiski täita erinevaid ülesandeid. Tavaliselt konstrueeritakse SLM-e suurte keelemudelite kokkusurumise või destilleerimise teel, püüdes säilitada suure osa algse mudeli funktsionaalsusest ja keelelistest võimetest. Mudeli suuruse vähendamine vähendab üldist keerukust, muutes SLM-id nii mälu kasutuse kui arvutusnõuete osas efektiivsemaks. Hoolimata neist optimeerimistest suudavad SLM-id täita laiaulatuslikke loomuliku keele töötlemise (NLP) ülesandeid:

- Teksti genereerimine: sidusate ja kontekstuaalselt asjakohaste lausete või lõikude loomine.
- Teksti lõpetamine: lausete ennustamine ja lõpetamine antud vihje põhjal.
- Tõlkimine: teksti teisendamine ühest keelest teise.
- Kokkuvõtete tegemine: pikkade tekstide kokkusurumine lühemateks, kergemini seeditavateks kokkuvõteteks.

Kuigi mõningate kompromissidega jõudluses või mõistmise sügavuses võrreldes suuremate mudelitega.

## Kuidas väiksed keelemudelid töötavad?
SLM-e treenitakse suurte tekstikogumite peal. Treeningu käigus õpivad nad keele mustreid ja struktuure, võimaldades genereerida nii grammatikaliselt korrektselt kui ka kontekstuaalselt asjakohaselt teksti. Treeninguprotsess hõlmab:

- Andmete kogumine: suurte tekstikogude kogumine erinevatest allikatest.
- Eeltöötlemine: andmete puhastamine ja organiseerimine, et muuta need sobivaks treenimiseks.
- Treenimine: masinõppe algoritmide kasutamine, et õpetada mudelit teksti mõistma ja genereerima.
- Täpsustamine: mudeli täpsustamine, et parandada selle jõudlust konkreetsetel ülesannetel.

SLM-ide areng lähtub suurenevast vajadusest mudelite järele, mida saab kasutada piiratud ressurssidega keskkondades, näiteks mobiilseadmetes või servaarvutuse platvormidel, kus suured LLM-id võivad olla liiga ressursimahukad. Keskendudes tõhususele, tasakaalustab SLM jõudlust ja ligipääsetavust, võimaldades laialdasemat kasutamist erinevates valdkondades.

![slm](../../../translated_images/et/slm.4058842744d0444a.webp)

## Õpieesmärgid

Selles õppetükis loodame tutvustada SLM-i teadmisi ja ühendada seda Microsoft Phi-3-ga, et õppida erinevaid stsenaariume tekstisisu, nägemise ja MoE osas.

Õppetüki lõpuks peaksite suutma vastata järgmistele küsimustele:

- Mis on SLM?
- Mis vahe on SLM-il ja LLM-il?
- Mis on Microsoft Phi-3/3.5 perekond?
- Kuidas käivitada ennustust Microsoft Phi-3/3.5 perekonnaga?

Valmis? Alustame.

## Suurte keelemudelite (LLM) ja väikeste keelemudelite (SLM) erinevused

Nii LLM-id kui ka SLM-id põhinevad tõenäosuslikul masinõppel, järgides sarnaseid arhitektuurilisi disainilahendusi, treeningmeetodeid, andmete genereerimise protsesse ja mudelite hindamistehnikaid. Siiski eristavad neid mitmed põhiaspektid.

## Väikeste keelemudelite rakendused

SLM-idel on lai rakendusala, sealhulgas:

- Vestlusbotid: klienditoe pakkumine ja kasutajatega vestluses suhtlemine.
- Sisuloome: kirjanike abistamine ideede genereerimisel või isegi tervete artiklite koostamisel.
- Haridus: õpilaste abistamine kirjutamisülesannete täitmisel või uute keelte õppimisel.
- Juurdepääsetavus: abivahendite loomine puuetega inimeste jaoks, näiteks tekst kõneks süsteemid.

**Suurus**
  
Peamine erinevus LLM-ide ja SLM-ide vahel seisneb mudelite mahus. LLM-id, nagu ChatGPT (GPT-4), võivad koosneda hinnanguliselt 1,76 triljonist parameetrist, samas kui avatud lähtekoodiga SLM-id, nagu Mistral 7B, on loodud oluliselt väiksema parameetrite arvuga — umbes 7 miljardit. See erinevus tuleneb peamiselt erinevustest mudeli arhitektuuris ja treeninguprotsessis. Näiteks kasutab ChatGPT self-attention mehhanismi kodeerija-dekodeerija raamistikus, samas kui Mistral 7B kasutab libiseva akna tähelepanu, mis võimaldab tõhusamat treenimist ainult dekodeerija mudelis. See arhitektuuriline erinevus mõjutab oluliselt nende mudelite keerukust ja jõudlust.

**Mõistmine**

SLM-e optimeeritakse tavaliselt jõudluseks konkreetsetes valdkondades, muutes need väga spetsialiseerituks, kuid potentsiaalselt piiratud suutlikkusega pakkuda laiemat kontekstitunnetust mitmel teadmiste alal. Vastupidiselt püüavad LLM-id simuleerida inimese-laadset intelligentsust laiemal tasandil. Treenitud suurte ja mitmekesiste andmekogude peal, on LLM-id loodud hästi toimima eri valdkondades, pakkudes suuremat mitmekülgsust ja kohanemisvõimet. Seetõttu sobivad LLM-id laiemale ülesannete valikule, näiteks loomulik keele töötlemine ja programmeerimine.

**Arvutusvõimsus**

LLM-ide treenimine ja kasutamine on ressursimahukad protsessid, sageli vajavad nad märkimisväärset arvutusinfrastruktuuri, sealhulgas suuremahulisid GPU klastreid. Näiteks mudeli, nagu ChatGPT, treenimine algusest peale võib nõuda tuhandeid GPU-sid pika aja jooksul. Vastupidiselt on SLM-id väiksema parameetrite arvuga kergemini ligipääsetavad arvutusressursside osas. Sellised mudelid nagu Mistral 7B saab treenida ja käivitada kohalikus masinas, kus on mõõduka võimsusega GPU, kuigi treening nõuab ikkagi mitme GPU puhul mitut tundi.

**Kaldumus**

Kaldumus on tuntud probleem LLM-ides, mis tuleneb peamiselt treeningandmete iseloomust. Need mudelid toetuvad sageli internetist saadud avatud, töödeldud andmetele, mis võivad teatud gruppe alahinnata või valesti esindada, tuua kaasa vale märgistamise või peegeldada keelelisi eelarvamusi, mida mõjutavad dialektid, geograafilised eripärad ja grammatikareeglid. Lisaks võib keerukas LLM arhitektuur süvendada kaldumusi, mis võivad tähelepanuta jääda ilma hoolika täpsustamiseta. Teiselt poolt, SLM-id, mida treenitakse kitsamates, valdkonnaspetsiifilistes andmekogudes, on loomulikult vähem vastuvõtlikud nendele kallutatustele, kuid siiski mitte immuunsed.

**Järeldamine**

Väiksem suurus annab SLM-idele olulise eelise järeldamise kiiruse osas, võimaldades neil tõhusalt väljundeid genereerida kohalikul riistvaral ilma ulatusliku paralleeltöötluseta. Vastupidiselt vajavad LLM-id oma suuruse ja keerukuse tõttu sageli märkimisväärseid paralleelseid arvutusressursse, et saavutada sobivaid järeldamiskiirusi. Mitme samaaegse kasutaja olemasolu aeglustab LLM-ide vastamise kiirust veelgi, eriti massilisel juurutamisel.

Kokkuvõttes, kuigi nii LLM-id kui ka SLM-id jagavad masinõppe alusprintsiipi, erinevad nad oluliselt mudeli suuruse, ressursinõuete, konteksti mõistmise, kalduvuse kallutatusele ja järeldamiskiiruse poolest. Need erinevused peegeldavad nende vastavat sobivust erinevateks kasutusjuhtudeks, kus LLM-id on mitmekülgsemad, kuid ressursimahukamad, ja SLM-id pakuvad kitsama valdkonna efektiivsust vähendatud arvutusnõuetega.

***Märkus: Selles õppetükis tutvustame SLM-i, kasutades näitena Microsoft Phi-3 / 3.5 mudelit.***

## Phi-3 / Phi-3.5 perekonna tutvustus

Phi-3 / 3.5 perekond keskendub peamiselt teksti-, nägemis- ja agendi (MoE) rakendusskenaarumitele:

### Phi-3 / 3.5 juhendamine

Peamiselt tekstigeneratsiooni, vestluse lõpetamise ja sisuteabe väljavõtmise jaoks jne.

**Phi-3-mini**

3,8 miljardi parameetriga keelemudel on saadaval Microsoft Foundry, Hugging Face ja Ollama platvormidel. Phi-3 mudelid ületavad märkimisväärselt võrdse ja suurema suurusega keelemudeleid põhiseaduslike võrdlusaluste osas (vt allpool benchmark-numbrid, kõrgemad numbrid on paremad). Phi-3-mini ületab poole suuremate mudelite tulemusi, samal ajal kui Phi-3-small ja Phi-3-medium ületavad suuremaid mudeleid, sealhulgas GPT-3.5.

**Phi-3-small & medium**

Phi-3-small, millel on kõigest 7 miljardi parameetrit, ületab GPT-3.5T erinevatel keele-, mõtlemis-, kodeerimis- ja matemaatika võrdlusalustel.

Phi-3-medium 14 miljardi parameetriga jätkab seda trendi ja ületab Gemini 1.0 Pro.

**Phi-3.5-mini**

Võib mõelda seda kui Phi-3-mini väljalaske täiendust. Kuigi parameetrite arv ei muutu, parendab see mitmekeelse toe (toetab 20+ keelt: araabia, hiina, tšehhi, taani, hollandi, inglise, soome, prantsuse, saksa, heebrea, ungari, itaalia, jaapani, korea, norra, poola, portugali, vene, hispaania, rootsi, tai, türgi, ukraina) ja lisab tugevama tuge pika konteksti jaoks.

Phi-3.5-mini 3,8 miljardi parameetriga on oma suuruses ülekaalus võrreldes teiste keelemudelitega ja on võrdväärne poole suuremate mudelitega.

### Phi-3 / 3.5 nägemine

Võime mõelda Phi-3/3.5-Instruct mudelit kui Phi võimet mõista ning Vision on see, mis annab Phi-le silmad maailma mõistmiseks.


**Phi-3-Vision**

Phi-3-vision, millel on kõigest 4,2 miljardit parameetrit, jätkab seda trendi ja ületab suuremaid mudeleid nagu Claude-3 Haiku ja Gemini 1.0 Pro V üldistel visuaalsel mõtlemise ülesannetel, OCR-il ning tabelite ja diagrammide mõistmisel.


**Phi-3.5-Vision**

Phi-3.5-Vision on samuti Phi-3-Vision täiendatud versioon, lisades toe mitmele pildile. Võime seda pidada visiidi parenduseks — mitte ainult piltide, vaid ka videote nägemiseks.

Phi-3.5-vision ületab suuremaid mudeleid nagu Claude-3.5 Sonnet ja Gemini 1.5 Flash OCR-is, tabelite ja diagrammide mõistmisel ning on võrdne üldise visuaalse teadmiste mõtlemise ülesannetes. Toetab mitme kaadri sisendit, st mõtlemist mitme sisendpildi põhjal


### Phi-3.5-MoE

***Ekspertide segu (MoE)*** võimaldab mudelitel olla eeltreenitud palju väiksema arvutuskoormusega, mis tähendab, et saate oluliselt suurendada mudeli või andmekogu suurust sama arvutus eelarvega kui tihe mudel. Eriti peaks MoE mudel saavutama sama kvaliteedi kui selle tihe vaste palju kiiremini eeltreenimise ajal.

Phi-3.5-MoE koosneb 16×3,8 miljardi parameetriga eksperdimoodulist. Phi-3.5-MoE, millel on vaid 6,6 miljardit aktiivset parameetrit, saavutab sarnase mõtlemis-, keele mõistmise ja matemaatika taseme kui palju suuremad mudelid.

Phi-3/3.5 perekonna mudelit saab kasutada erinevates stsenaariumites. Erinevalt LLM-ist võite Phi-3/3.5-mini või Phi-3/3.5-Vision kasutada servaseadmetes.


## Kuidas kasutada Phi-3/3.5 perekonna mudeleid

Loodame kasutada Phi-3/3.5 erinevates stsenaariumites. Järgmises osas kasutame Phi-3/3.5 erinevate stsenaariumite põhjal.

![phi3](../../../translated_images/et/phi3.655208c3186ae381.webp)

### Järeldamine pilve API-de kaudu

**Microsoft Foundry mudelid**

> **Märkus:** GitHubi mudelid lõpetavad tegevuse 2026. aasta juuli lõpus. [Microsoft Foundry mudelid](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) on otsene asendus.

Microsoft Foundry mudelid on kõige otsesem viis. Saate kiiresti juurde pääseda Phi-3/3.5-Instruct mudelile Foundry mudelikataloogi kaudu. Koos Azure AI Inference SDK / OpenAI SDK-ga saate API-le ligipääsu koodi kaudu, et lõpetada Phi-3/3.5-Instruct käsklus. Samuti saate Playground'is testida erinevaid efekte.

- Demo: Võrdlus Phi-3-mini ja Phi-3.5-mini mõjust hiina stsenaariumites

![phi3](../../../translated_images/et/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/et/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Kui soovite kasutada nägemis- ja MoE mudeleid, saate Microsoft Foundry abil päringuid lõpetada. Kui olete huvitatud, saate lugeda Phi-3 retseptiraamatut, et teada saada, kuidas Microsoft Foundry kaudu Phi-3/3.5 Instruct, Vision ja MoE mudeleid kutsuda [klõpsake seda linki](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Lisaks pilvepõhisele Microsoft Foundry mudelikataloogile saate seotud päringute tegemiseks kasutada ka [NVIDIA NIM-i](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst). Võite külastada NVIDIA NIM-i, et sooritada Phi-3/3.5 perekonna API kõnesid. NVIDIA NIM (NVIDIA Inference Microservices) on komplekt kiirendatud järelduse mikroteenuseid, mis on loodud aitama arendajatel AI mudeleid tõhusalt erinevates keskkondades juurutada, sealhulgas pilvedes, andmekeskustes ja tööjaamades.

Siin on mõned NVIDIA NIM-i peamised omadused:

- **Kasutuse hõlbustamine:** NIM võimaldab AI mudelite juurutamist ühe käsuga, muutes selle olemasolevasse töövoogu integreerimise lihtsaks.

- **Optimeeritud jõudlus:** Kasutab NVIDIA eeloptimeeritud järeldusmootoreid, nagu TensorRT ja TensorRT-LLM, et tagada madal latentsus ja kõrge läbilaskevõime.
- **Skaalautuvus:** NIM toetab Kubernetesis automaatset skaaleerimist, võimaldades tõhusalt hallata erinevaid töökoormusi.
- **Turvalisus ja kontroll:** Organisatsioonid saavad hoida kontrolli oma andmete ja rakenduste üle, majutades NIM mikroteenuseid oma hallatud infrastruktuuris.
- **Standardseid API-sid:** NIM pakub tööstusharu standardseid API-sid, muutes lihtsaks AI-rakenduste nagu juturobotite, AI-assistentide ja muu loomise ja integreerimise.

NIM on osa NVIDIA AI Enterprisest, mis on suunatud AI mudelite juurutamise ja opereerimise lihtsustamisele, tagades nende tõhusa toimimise NVIDIA GPU-del.

- Demo: NVIDIA NIM kasutamine Phi-3.5-Vision-API kutsumiseks [[Klõpsake seda linki](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5 kohalik käitamine
Järeldus Phi-3 või mõne muu keelemudeli nagu GPT-3 puhul tähendab protsessi, kus genereeritakse vastuseid või prognoose sisendi põhjal. Kui esitate Phi-3-le sõnumi või küsimuse, kasutab see treenitud närvivõrku kõige tõenäolisema ja asjakohasema vastuse tuletamiseks, analüüsides andmetes olevad mustrid ja seosed, mille põhjal see on treenitud.

**Hugging Face Transformer**
Hugging Face Transformers on võimas teek, mis on loodud loomuliku keele töötlemise (NLP) ja muude masinõppe ülesannete jaoks. Siin on mõned peamised punktid:

1. **Eeltreenitud mudelid**: Pakub tuhandeid eeltreenitud mudeleid, mida saab kasutada mitmeteks ülesanneteks nagu tekstiklassifikatsioon, nimetatud üksuste tuvastamine, küsimustele vastamine, kokkuvõtete tegemine, tõlkimine ja teksti genereerimine.

2. **Raamistiku ühilduvus:** Raamatukogu toetab mitut süvaõppe raamistiku, sealhulgas PyTorch, TensorFlow ja JAX-i. See võimaldab teil mudelit treenida ühes raamistikus ja kasutada teises.

3. **Multimodaalsed võimalused:** Peale NLP toetab Hugging Face Transformers ka arvutinägemise ülesandeid (nt pildi klassifitseerimine, objektituvastus) ja helitöötlust (nt kõnetuvastus, heliklassifikatsioon).

4. **Lihtne kasutada:** Raamatukogu pakub API-sid ja tööriistu mudelite hõlpsaks allalaadimiseks ja peenhäälestamiseks, muutes selle ligipääsetavaks nii algajatele kui ka ekspertidele.

5. **Kogukond ja ressursid:** Hugging Facel on aktiivne kogukond ning põhjalik dokumentatsioon, juhendid ja õpetused, mis aitavad kasutajatel alustada ja raamatukogust maksimaalselt kasu saada.
[ametlik dokumentatsioon](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) või nende [GitHubi hoidla](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

See on kõige sagedamini kasutatud meetod, kuid see nõuab ka GPU kiirendust. Lõppude lõpuks nõuavad näiteks Vision ja MoE stsenaariumid palju arvutusi, mis oleksid CPU-l väga aeglased, kui neid ei kvantiseerita.


- Demo: Transformeriga Phi-3.5-Instruct kutsumine [Klõpsake seda linki](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformeriga Phi-3.5-Vision kutsumine [Klõpsake seda linki](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformeriga Phi-3.5-MoE kutsumine [Klõpsake seda linki](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) on platvorm, mis on loodud suure keelemudeli (LLM) kohalikuks jooksutamiseks teie arvutis lihtsamaks muutmiseks. See toetab mitmeid mudeleid nagu Llama 3.1, Phi 3, Mistral ja Gemma 2, teiste hulgas. Platvorm lihtsustab protsessi, sidudes mudeli kaalud, konfiguratsiooni ja andmed üheks paketiks, muutes selle kasutajatele kergemini kohandatavaks ja võimaldades oma mudelite loomist. Ollama on saadaval macOS-i, Linuxi ja Windowsi jaoks. See on suurepärane vahend, kui soovite eksperimenteerida või juurutada LLM-e ilma pilveteenustesse tuginemata. Ollama on kõige sirgjoonelisem tee, peate lihtsalt käivitama järgmise käsu.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) on Microsofti võrguühenduseta, seadmes töötav täidesaatvakeskkond, mis võimaldab mudelite nagu Phi täielikku jooksmist teie enda riistvaral – pole vaja Azure tellimust, API võtit ega võrguühendust. See valib automaatselt parima saadaval oleva täitjapakkuja (NPU, GPU või CPU) ja pakub OpenAI-ühilduvat lõpp-punkti, nii et olemasolev `openai`/Azure AI järeldus-SDK kood saab sellele viidata minimaalselt muudetuna. Vaadake [Foundry Local dokumentatsiooni](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst), et alustada.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Või kasutage SDK-d otse Pythoni kaudu:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime GenAI jaoks**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) on platvormideülene järeldus- ja treeningmasinõppe kiirendi. ONNX Runtime Generatiivse AI (GENAI) jaoks on võimas tööriist, mis aitab teil generatiivseid AI mudeleid mitmes platvormis tõhusalt jooksutada. 

## Mis on ONNX Runtime?
ONNX Runtime on avatud lähtekoodiga projekt, mis võimaldab kõrge jõudlusega masinõppemudelite järeldusi. See toetab mudeleid Open Neural Network Exchange (ONNX) formaadis, mis on masinõppemudelite esitamise standard. ONNX Runtime järeldus võimaldab kiirem kliendikogemust ja madalamaid kulusid, toetades süvaõpperaamistike nagu PyTorch ja TensorFlow/Keras ning klassikalisi masinõppeteeke nagu scikit-learn, LightGBM, XGBoost jne. ONNX Runtime on ühilduv erinevate riistvarade, draiverite ja operatsioonisüsteemidega ning tagab optimaalse jõudluse, kasutades riistvarakiirendusi, kus see on kohaldatav, koos graafi optimeerimise ja teisendustega.

## Mis on generatiivne AI?
Generatiivne AI tähendab süsteeme, mis suudavad genereerida uut sisu, näiteks teksti, pilte või muusikat, põhinedes treeningandmetel. Näiteks keelemudelid nagu GPT-3 ja pildigeneratsioonimudelid nagu Stable Diffusion. ONNX Runtime GenAI teek pakub generatiivse AI tsüklit ONNX mudelite jaoks, sh järeldusi ONNX Runtime abil, logitsite töötlemist, otsingut ja proovivõttu ning KV vahemälu haldamist.

## ONNX Runtime GENAI jaoks
ONNX Runtime GENAI jaoks laiendab ONNX Runtime võimeid generatiivsete AI mudelite toetamiseks. Siin on mõned peamised funktsioonid:

- **Lai platvormitugi:** Toimib mitmetel platvormidel, sh Windows, Linux, macOS, Android ja iOS.
- **Mudelitugi:** Toetab paljusid populaarseid generatiivseid AI mudeleid, nagu LLaMA, GPT-Neo, BLOOM ja teised.
- **Jõudluse optimeerimine:** Sisaldab optimeerimisi erinevate riistvarakiirendajate jaoks nagu NVIDIA GPU-d, AMD GPU-d jpt.
- **Lihtne kasutada:** Pakub API-sid rakendustesse lihtsaks integreerimiseks, võimaldades teil genereerida teksti, pilte ja muud sisu minimaalse koodiga.
- Kasutajad saavad kutsuda kõrgetasemelist generate() meetodit või jooksutada mudeli iga iteratsiooni tsüklis, genereerides ühe sümboli korraga ja vajadusel uuendades tsükli sees genereerimise parameetreid.
- ONNX runtime toetab ka ahnet/kiirreidu otsingut ja TopP, TopK proovivõttu tokenite järjestuste genereerimiseks ning sisseehitatud logitsite töötlemist, nagu korduskaristused. Samuti on lihtne lisada kohandatud hindeid.

## Alustamine
Alustamiseks ONNX Runtime GENAI-ga võite järgida neid samme:

### Paigalda ONNX Runtime:
```Python
pip install onnxruntime
```
### Paigalda Generative AI laiendused:
```Python
pip install onnxruntime-genai
```

### Käivita mudel: Siin on lihtne näide Pythoni keeles:
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
### Demo: ONNX Runtime GenAI kasutamine Phi-3.5-Vision kutsumiseks


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


**Muud**

Lisaks ONNX Runtime-le, Ollamale ja Foundry Local viidetega meetoditele võime ka jätkata kvantitatiivsete mudelite viidet erinevate tootjate pakutud mudeli viidetel põhinevate meetoditega. Näiteks Apple MLX raamistik Apple Metali, Qualcomm QNN NPU, Intel OpenVINO CPU/GPU jne. Rohkem sisu leiate ka [Phi-3 Kokaraamatust](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Rohkem

Oleme õppinud Phi-3/3.5 perekonna põhialuseid, kuid SLM kohta õppimiseks vajame rohkem teadmisi. Vastused leiate Phi-3 Kokaraamatust. Kui soovite rohkem teada saada, külastage palun [Phi-3 Kokaraamatut](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->