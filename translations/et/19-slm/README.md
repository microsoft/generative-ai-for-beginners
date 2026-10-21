# Sissejuhatus väikestesse keeltesse mudelitesse generatiivses tehisintellektis algajatele
Generatiivne tehisintellekt on põnev tehisintellekti valdkond, mis keskendub süsteemide loomisele, mis suudavad genereerida uut sisu. See sisu võib ulatuda tekstist ja piltidest kuni muusika ja isegi tervete virtuaalsete keskkondadeni. Üks põnevamaid generatiivse tehisintellekti rakendusi on keelemudelites.

## Mis on väikesed keelemudelid?

Väike keelemudel (SLM) on suures keelemudelis (LLM) põhinev väiksem variant, mis kasutab ära paljusid LLMide arhitektuurilisi põhimõtteid ja tehnikaid, kuid omab märkimisväärselt väiksemat arvutuskoormust.

SLM-id on keelemudelite alamrühm, mis on loodud inimese moodi teksti genereerimiseks. Erinevalt oma suurematest vastetest, nagu GPT-4, on SLM-id kompaktsemad ja tõhusamad, muutes need ideaalseks rakendusteks, kus arvutusressursid on piiratud. Hoolimata oma väiksemast suurusest, suudavad nad siiski täita mitmesuguseid ülesandeid. Tavaliselt ehitatakse SLM-e, kokkusurutud või destilleeritud LLM-idest, eesmärgiga säilitada algse mudeli suur osa funktsionaalsusest ja keelelistest võimetest. Mudeli suuruse vähendamine vähendab üldist keerukust, muutes SLM-id mälukasutuse ja arvutusnõudmiste osas tõhusamaks. Hoolimata nendest optimeerimistest, suudavad SLM-id siiski täita laia valikut loomuliku keele töötlemise (NLP) ülesandeid:

- Tekstigeneratsioon: Korrektsete ja kontekstitundlike lause või lõikude loomine.
- Teksti täiendamine: Lausete ennustamine ja täiendamine antud vihje põhjal.
- Tõlkimine: Teksti ümberarvutamine ühest keelest teise.
- Kokkuvõtete koostamine: Pikkade tekstide kokkusurumine lühemateks, hõlpsamini omastatavateks kokkuvõteteks.

Kuigi mõningate järeleandmistega jõudluses või sügavuses võrreldes suuremate mudelitega.

## Kuidas väikesed keelemudelid töötavad?
SLM-e treenitakse tohutul hulgal tekstandmetel. Treeningu käigus õpivad nad keele mustreid ja struktuure, võimaldades neil genereerida nii grammatiliselt korrektset kui ka kontekstuaalselt sobivat teksti. Treeninguprotsess hõlmab:

- Andmete kogumine: Suurte tekstikogumite kogumine erinevatest allikatest.
- Eeltöötlus: Andmete puhastamine ja korraldamine treenimiseks sobivaks.
- Treening: Masinõppe algoritmide kasutamine, et õpetada mudelit teksti mõistma ja genereerima.
- Täiustamine: Mudeli kohandamine, et parandada selle sooritust kindlatel ülesannetel.

SLM-ide areng vastab kasvavale vajadusele mudelite järele, mida saab kasutada ressursside piirangutega keskkondades, nagu mobiilseadmed või servaarvutuse platvormid, kus täielikult ulatuslikke LLM-e võib olla ebapraktiline nende suure ressursinõudluse tõttu. Keskendudes tõhususele tasakaalustavad SLM-id jõudlust ja kättesaadavust, võimaldades laialdasemat rakendamist erinevates valdkondades.

![slm](../../../translated_images/et/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Õpieesmärgid

Selles õppetükis loodame tutvustada teadmisi SLMidest ja ühendada see Microsoft Phi-3-ga, et õppida erinevaid stsenaariume tekstisisu, nägemise ja MoE osas.

Õppetüki lõpus peaksid saama vastata järgmistele küsimustele:

- Mis on SLM?
- Mis vahe on SLM-il ja LLM-il?
- Mis on Microsoft Phi-3/3.5 perekond?
- Kuidas teha järeldust Microsoft Phi-3/3.5 perekonnaga?

Valmis? Alustame.

## Erinevused suurte keelemudelite (LLMid) ja väikeste keelemudelite (SLMid) vahel

Nii LLMid kui ka SLMid põhinevad tõenäosusel põhineva masinõppe alustel, järgides sarnaseid lähenemisviise arhitektuuri disainis, treeningu meetodites, andmete genereerimise protsessides ning mudeli hindamistehnikates. Kuid mitmed olulised tegurid eristavad neid kahte mudelitüüpi.

## Väikeste keeltemudelite rakendused

SLM-idel on lai rakenduste spekter, sealhulgas:

- Vestlusrobotid: Klienditoe pakkumine ja kasutajatega vestlemine.
- Sisu loomine: Kirjanike abistamine ideede genereerimisel või isegi tervete artiklite koostamisel.
- Haridus: Õpilaste abistamine kirjutamisülesannete või uute keelte õppimisel.
- Juurdepääsetavus: Tööriistade loomine puudega inimestele, nagu tekstist kõneks süsteemid.

**Suurus**
  
Peamine erinevus LLM-ide ja SLM-ide vahel seisneb mudelite suuruses. LLM-id, nagu ChatGPT (GPT-4), võivad sisaldada hinnanguliselt 1,76 triljonit parameetrit, samal ajal kui avatud lähtekoodiga SLM-id nagu Mistral 7B on loodud oluliselt vähemate – umbes 7 miljardi – parameetriga. See erinevus tuleneb peamiselt mudeli arhitektuurist ja treeningprotsessidest. Näiteks kasutab ChatGPT ise tähelepanumehhanismi kodeerija-dekodeerija raamistikus, samas kui Mistral 7B kasutab libiseva aknaga tähelepanu, mis võimaldab efektiivsemat treeningut ainult dekodeerijat sisaldavas mudelis. See arhitektuuriline erinevus mõjutab oluliselt nende mudelite keerukust ja jõudlust.

**Mõistmine**

SLM-id on tavaliselt optimeeritud soorituseks kindlates valdkondades, muutes need väga spetsialiseerituks, kuid potentsiaalselt piiratud võimega pakkuda laiapõhjalist kontekstuaalset mõistmist mitmes teadmiste valdkonnas. Seevastu LLM-id püüavad simuleerida inimlikku intelligentsust laiemal tasandil. Treenitud mahtudel ja mitmekesistel andmestikel, on LLM-id loodud hästi toimima paljudes valdkondades, pakkudes suuremat mitmekülgsust ja kohanemisvõimet. Seetõttu sobivad LLM-id paremini laiaulatuslikele alamülesannete komplektidele, nagu loomuliku keele töötlemine ja programmeerimine.

**Arvutusvõimsus**

LLM-ide treenimine ja kasutusele võtmine on ressursimahukad protsessid, nõudes tihti ulatuslikku tehnilist infrastruktuuri, sealhulgas suures koguses GPU klastreid. Näiteks mudeli nagu ChatGPT treenimine algusest võib nõuda tuhandeid GPUsid pika aja jooksul. Vastupidiselt on SLM-id oma väiksemate parameetrite arvu tõttu arvutusressursside poolest kättesaadavamad. Mudelid nagu Mistral 7B saab treenida ja käitada kohalikus arvutis keskmise GPU võimekusega, kuigi treening nõuab ikka mitu tundi mitmel GPU-l järjest.

**Eelarvamus**

Eelarvamus on LLM-ide tuntud probleem, peamiselt treeningandmete iseloomu tõttu. Need mudelid toetuvad sageli internetist kogutud toormonsetele ja avalikult kättesaadavatele andmetele, mis võivad mingite gruppide esitamist alahinnata või moonutada, sisaldada vale märgistusi või peegeldada keelelisi eelarvamusi, mida mõjutavad murde, geograafilised variatsioonid ja grammatikanormid. Lisaks võib LLM-ide arhitektuuride keerukus eelarvamust alateadlikult suurendada, mida ei pruugi hoolika täpsustamise nélkül märgata. Teisalt, SLM-id, mis on treenitud kitsamates, spetsiifilistes domeeniandmetes, on loomulikult vähem vastuvõtlikud sellistele eelarvamustele, kuigi täiesti immuunsed nad siiski ei ole.

**Järelduskiirus**

SLM-ide väiksem suurus annab neile märkimisväärse eelise järelduskiiruses, võimaldades neil tõhusalt toota väljundeid kohalikus riistvaras ilma ulatusliku paralleeltöötluseta. Vastupidiselt nõuavad LLM-id oma suuruse ja keerukuse tõttu sageli märkimisväärseid paralleelseid arvutusressursse, et saavutada aktsepteeritavad järeldusajad. Mitme samaaegse kasutaja olemasolu aeglustab veelgi LLM-ide vastamisaegu, eriti ulatusliku kasutuse korral.

Kokkuvõttes, kuigi nii LLM-id kui ka SLM-id tuginevad masinõppe põhialustele, erinevad need märkimisväärselt mudeli suuruse, ressursinõudluse, kontekstuaalse mõistmise, eelarvamusele vastuvõtlikkuse ja järelduskiiruse poolest. Need erinevused peegeldavad nende vastavat sobivust erinevateks kasutusjuhtumiteks, kus LLM-id on mitmekülgsemad, kuid ressursimahukamad ning SLM-id pakuvad valdkonnapõhist tõhusust vähendatud arvutusvajadusega.

***Märkus: Selles õppetükis tutvustame SLM-i kasutades näitena Microsoft Phi-3 / 3.5 mudelit.***

## Phi-3 / Phi-3.5 perekonna tutvustus

Phi-3 / 3.5 perekond on peamiselt suunatud teksti, nägemise ja agendi (MoE) rakenduse stsenaariumidele:

### Phi-3 / 3.5 juhendatud mudel

Peamiselt tekstigeneratsiooniks, vestluse täiendamiseks ja sisulise info väljavõtmiseks jne.

**Phi-3-mini**

3,8 miljardi parameetriga keelemudel on saadaval Microsoft Foundry, Hugging Face ja Ollama platvormidel. Phi-3 mudelid ületavad olulisel määral sama või suurematest mudelitest paremust võtmetestidel (vt allpool võrdlustulemusi, kõrgemad numbrid on paremad). Phi-3-mini on võimekam kui kaks korda suuremad mudelid, samas kui Phi-3-small ja Phi-3-medium on parem kui suuremad mudelid, sealhulgas GPT-3.5.

**Phi-3-small & medium**

Phi-3-small koos vaid 7 miljardiga parameetreid ületab GPT-3.5T mitmes keele-, loogika-, kodeerimis- ja matemaatika testides.

Phi-3-medium 14 miljardi parameetriga jätkab seda suundumust ja ületab Gemini 1.0 Pro mudeli.

**Phi-3.5-mini**

Võib mõelda sellele kui uuendusele Phi-3-mini suhtes. Parameetrid jäävad samaks, kuid see parandab mitmekeelset toetust (toetab 20+ keelt: araabia, hiina, tšehhi, taani, hollandi, inglise, soome, prantsuse, saksa, heebrea, ungari, itaalia, jaapani, korea, norra, poola, portugali, vene, hispaania, rootsi, tai, türgi, ukraina) ning lisab tugevamat tuge pikale kontekstile.

Phi-3.5-mini 3,8 miljardi parameetriga ületab sama suurusega keelemudeleid ja on võrdväärne kaks korda suuremate mudelitega.

### Phi-3 / 3.5 nägemismudelid

Võime mõelda Phi-3/3.5 juhendatud mudelit kui Phi võimet mõista ning nägemine annab Phi-le silmad maailma mõistmiseks.


**Phi-3-Vision**

Phi-3-vision, ainult 4,2 miljardit parameetrit omades, jätkab seda trendi ja ületab suuremaid mudeleid nagu Claude-3 Haiku ja Gemini 1.0 Pro V üldistel visuaalse mõtlemise ülesannetel, OCR-il ning tabelite ja diagrammide mõistmisel.


**Phi-3.5-Vision**

Phi-3.5-Vision on samuti uuendus Phi-3-Visionist, lisades mitme pildi toe. Võib mõelda sellele kui nägemise parandusele: mitte ainult saab pilte näha, vaid ka videoid.

Phi-3.5-vision ületab suuremaid mudeleid nagu Claude-3.5 Sonnet ja Gemini 1.5 Flash OCR, tabeli ja diagrammi mõistmise ülesannetes ning on võrdväärne üldiste visuaalse teadmise mõtlemise ülesannetes. Toetab mitme kaadri sisendit, st suudab teha järeldusi mitme sisendpildi põhjal.


### Phi-3.5-MoE

***Ekspertide segu (MoE)*** võimaldab mudelitel olla treenitud palju vähemate arvutusressurssidega, mis tähendab, et mudeli või andmestiku suurust saab dramaatiliselt suurendada samade arvutusvahendite juures kui tiheda mudeli puhul. Eriti peaks MoE mudel saavutama sama kvaliteedi kui tema tihe vaste palju kiiremini treeningfaasis.

Phi-3.5-MoE koosneb 16x3,8 miljardilisest eksperdi moodulist. Phi-3.5-MoE vaid 6,6 miljardi aktiivse parameetriga saavutab sarnase mõtlemis-, keele mõistmise ja matemaatika taseme palju suuremate mudelitega.

Phi-3/3.5 perekonna mudelit saab kasutada erinevates stsenaariumites. Erinevalt LLM-ist saab Phi-3/3.5-mini või Phi-3/3.5-Vision deployida servaseadmetele.


## Kuidas kasutada Phi-3/3.5 perekonna mudeleid

Loodame kasutada Phi-3/3.5 erinevates stsenaariumites. Järgmises osas kasutame Phi-3/3.5 erinevate stsenaariumite põhjal.

![phi3](../../../translated_images/et/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Järeldamine pilve API-de kaudu

**Microsoft Foundry mudelid**

> **Märkus:** GitHub mudelid lõpetavad tegevuse 2026. aasta juuli lõpus. [Microsoft Foundry mudelid](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) on otsene asendus.

Microsoft Foundry mudelid on kõige otsesem tee. Saate kiirelt ligi Phi-3/3.5-Instruct mudelile Foundry mudelikataloogi kaudu. Koos Azure AI Inference SDK / OpenAI SDK-ga pääsete API-le koodi kaudu ligi, et teha Phi-3/3.5-Instruct kõnesid. Samuti saate erinevaid tulemusi testida Playgroundis.

- Demo: Phi-3-mini ja Phi-3.5-mini tulemuste võrdlus hiina keelsetes stsenaariumites

![phi3](../../../translated_images/et/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/et/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Või kui soovite kasutada nägemise ja MoE mudeleid, saate Microsoft Foundry kaudu kõne teha. Kui olete huvitatud, võite lugeda Phi-3 kokaraamatut, et õppida, kuidas Phi-3/3.5-Instruct, Vision, MoE kutsuda Microsoft Foundry kaudu [Klikkige siin](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Lisaks pilvepõhisele Microsoft Foundry mudelikataloogile saate kasutada ka [NVIDIA NIM-i](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst), et teha seotud kõnesid. Võite külastada NVIDIA NIM-i, et teha Phi-3/3.5 perekonna API kõnesid. NVIDIA NIM (NVIDIA Inference Microservices) on komplekt kiirendatud järeldusteenuseid, mis on loodud abistama arendajaid AI mudelite tõhusal juurutamisel eri keskkondades, sealhulgas pilvedes, andmekeskustes ja tööjaamades.

Siin on mõned NVIDIA NIM-i võtmeomadused:

- **Lihtne juurutada:** NIM võimaldab AI mudelide juurutamist ühe käsuga, muutes integratsiooni olemasolevates töölõikudes lihtsaks.
- **Optimeeritud jõudlus:** See kasutab NVIDIA eeloptimeeritud järeldusmootoreid nagu TensorRT ja TensorRT-LLM, et tagada madal latentsus ja kõrge läbilasevus.
- **Skaalautuvus:** NIM toetab automaatset skaaleerimist Kuberneteses, võimaldades efektiivselt toime tulla muutuvate töökoormustega.
- **Turvalisus ja kontroll:** Organisatsioonid saavad säilitada kontrolli oma andmete ja rakenduste üle, isetegutsedes NIM mikroteenuseid oma hallatavas infrastruktuuris.
- **Standardseid API-sid:** NIM pakub tööstusharu standarditele vastavaid API-sid, mis muudavad AI rakenduste nagu vestlusrobotid, AI assistendid ja muud loomise ning integreerimise lihtsaks.

NIM on osa NVIDIA AI Enterprise'ist, mille eesmärk on lihtsustada AI mudelite kasutuselevõttu ja operatsioonide haldust, tagades nende tõhusa töö NVIDIA GPU-del.

- Demo: NVIDIA NIM-i kasutamine Phi-3.5-Vision-API kutsumiseks [[Kliki sellel lingil](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5 lokaalne käitamine
Phi-3 või mis tahes keelemudeli nagu GPT-3 puhul viitab järeldamine protsessile, mille käigus genereeritakse vastuseid või prognoose sisendi põhjal. Kui annate Phi-3-le käsku või küsimuse, kasutab see oma treenitud närvivõrku, et analüüsida treeningandmetes olevaid mustreid ja seoseid ning järeldada kõige tõenäolisem ja asjakohasem vastus.

**Hugging Face Transformer**
Hugging Face Transformers on võimas teek, mis on loodud loomuliku keele töötlemiseks (NLP) ja muudele masinõppe ülesannetele. Siin on mõned olulised punktid selle kohta:

1. **Eeltreenitud mudelid**: See pakub tuhandeid eeltreenitud mudeleid, mida saab kasutada erinevate ülesannete täitmiseks, nagu tekstiklassifikatsioon, nimetatud üksuste tuvastamine, küsimustele vastamine, kokkuvõtete tegemine, tõlkimine ja teksti genereerimine.

2. **Raamistike ühilduvus**: Teek toetab mitut sügava õppimise raamistiku, sealhulgas PyTorch, TensorFlow ja JAX. See võimaldab treenida mudelit ühes raamistikus ja kasutada seda teises.

3. **Multimodaalsed võimekused**: Lisaks NLP-le toetavad Hugging Face Transformers ülesandeid ka arvutinägemises (nt pildiklassifikatsioon, objektide tuvastamine) ja heli töötlemises (nt kõnetuvastus, heli klassifikatsioon).

4. **Lihtne kasutus**: Teek pakub API-sid ja tööriistu mudelite lihtsaks allalaadimiseks ja peenhäälestamiseks, muutes selle ligipääsetavaks nii algajatele kui ka ekspertidele.

5. **Kogukond ja ressursid**: Hugging Face'il on aktiivne kogukond ning ulatuslik dokumentatsioon, juhendid ja õpetused, mis aitavad kasutajatel alustamiseks ja teegi maksimaalseks kasutamiseks.
[ametlik dokumentatsioon](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) või nende [GitHubi hoidla](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

See on kõige sagedamini kasutatav meetod, kuid see nõuab ka GPU kiirendust. Lõppude lõpuks vajavad sellised stsenaariumid nagu Vision ja MoE palju arvutusi, mis oleksid ilma kvantiseerimiseta CPU peal väga aeglased.


- Demo: Transformeriga Phi-3.5-Instruct kutsumine [Kliki sellel lingil](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformeriga Phi-3.5-Vision kutsumine [Kliki sellel lingil](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformeriga Phi-3.5-MoE kutsumine [Kliki sellel lingil](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) on platvorm, mis on loodud selleks, et lihtsustada suurte keelemudelite (LLM) lokaalset käitamist teie masinas. See toetab erinevaid mudeleid, nagu Llama 3.1, Phi 3, Mistral ja Gemma 2, teiste hulgas. Platvorm pakub lihtsustust, koondades mudelite kaalud, konfiguratsiooni ja andmed ühte paketti, muutes selle kasutajatele oma mudelite kohandamise ja loomise lihtsamaks. Ollama on saadaval macOS, Linuxi ja Windowsi jaoks. See on suurepärane tööriist, kui soovite eksperimenteerida või kasutada LLM-e ilma pilveteenustest sõltumata. Ollama on kõige otsesem viis, peate lihtsalt käivitama järgmise käsu.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) on Microsofti offline- ja seadmel põhinev täitmiskeskkond, mis võimaldab mudeleid nagu Phi täielikult oma riistvaral jooksutada – ei ole vaja Azure tellimust, API võtit ega võrguühendust. See valib automaatselt parima saadaoleva täitmisteenuse (NPU, GPU või CPU) ja pakub OpenAI-ga ühilduvat liidest, nii et olemasolev `openai`/Azure AI Inference SDK kood saab seda kasutada minimaalse muudatusega. Alustamiseks vaadake [Foundry Local dokumentatsiooni](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst).

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Või kasutage SDK-d otse Pythonis:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime GenAI jaoks**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) on platvormideülene masinõppe mudelite järeldus- ja treenimiskiirendi. ONNX Runtime Generatiivse AI (GENAI) jaoks on tõhus tööriist, mis aitab teil generatiivseid AI mudeleid erinevatel platvormidel tõhusalt käivitada.

## Mis on ONNX Runtime?
ONNX Runtime on avatud lähtekoodiga projekt, mis võimaldab masinõppemudelite kõrgtasemelist järeldamist. See toetab mudeleid Open Neural Network Exchange (ONNX) vormingus, mis on masinõppemudelite esitamise standard. ONNX Runtime järeldus võib võimaldada kiirem kliendikogemust ja madalamaid kulusid, toetades mudeleid sügava õppimise raamistikest nagu PyTorch ja TensorFlow/Keras ning ka klassikalistest masinõppe teekidest nagu scikit-learn, LightGBM, XGBoost jne. ONNX Runtime on ühilduv erineva riistvara, draiverite ja operatsioonisüsteemidega ning pakub optimaalset jõudlust, kasutades seal, kus sobib, riistvarakiirendeid koos graafi optimeerimiste ja teisendustega.

## Mis on generatiivne tehisintellekt?
Generatiivne AI viitab AI süsteemidele, mis suudavad luua uut sisu, nagu tekst, pildid või muusika, põhinedes treeningandmetel. Näideteks on keelemudelid nagu GPT-3 ja pildigeneratsioonimudelid nagu Stable Diffusion. ONNX Runtime GenAI teek pakub generatiivse AI silmust ONNX mudelitele, sealhulgas järeldust ONNX Runtime abil, logitite töötlemist, otsingut ja proovivõttu ning KV vahemälu haldust.

## ONNX Runtime GENAI jaoks
ONNX Runtime GENAI jaoks laiendab ONNX Runtime võimalusi, toetades generatiivseid AI mudeleid. Siin on mõned peamised omadused:

- **Lai platvormide toetus:** Töötab erinevatel platvormidel, sh Windows, Linux, macOS, Android ja iOS.
- **Mudelitoetus:** Toetab paljusid populaarseid generatiivseid AI mudeleid, nagu LLaMA, GPT-Neo, BLOOM ja teised.
- **Jõudluse optimeerimine:** Sisaldab optimeerimisi erinevatele riistvarakiirenditele nagu NVIDIA GPU-d, AMD GPU-d ja teised.
- **Lihtne kasutada:** Pakub API-sid lihtsaks integreerimiseks rakendustesse, võimaldades teil genereerida teksti, pilte ja muud sisu minimaalsete koodimuudatustega.
- Kasutajad saavad kutsuda kõrgetasemelist meetodit generate() või jooksutada mudeli igat iteratsiooni silmuses, genereerides ühe sümboli korraga ning vajadusel uuendades generatsiooni parameetreid silmuses.
- ONNX runtime toetab ka ahnet/kiirte otsingut ja TopP, TopK proovivõttu tokenite järjestuste genereerimiseks ning sisseehitatud logitite töötlemist, nagu korduste karistused. Samuti on lihtne lisada kohandatud hindamist.

## Alustamine
ONNX Runtime GENAI kasutamise alustamiseks võite järgida neid samme:

### Paigaldage ONNX Runtime:
```Python
pip install onnxruntime
```
### Paigaldage generatiivse AI laiendused:
```Python
pip install onnxruntime-genai
```

### Käivitage mudel: siin on lihtne näide Pythonis:
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

Lisaks ONNX Runtime'ile, Ollama'le ja Foundry Locali viitamiseks võime täiendada ka kvantitatiivsete mudelite viiteid, mis põhinevad erinevate tootjate mudeliviitamisel. Näiteks Apple MLX raamistik Apple Metaliga, Qualcomm QNN NPU-ga, Intel OpenVINO CPU/GPU-ga jne. Rohkem sisu leiate ka [Phi-3 kokaraamatust](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Rohkem

Oleme õppinud Phi-3/3.5 perekonna põhialuseid, kuid SLM-st rohkem teadmiseks vajame lisa teadmisi. Vastuseid leiate Phi-3 kokaraamatust. Kui soovite rohkem teada, palun külastage [Phi-3 kokaraamatut](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->