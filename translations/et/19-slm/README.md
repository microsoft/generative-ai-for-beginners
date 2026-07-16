# Sissejuhatus väikestesse keelemudelitesse generatiivses tehisintellektis algajatele
Generatiivne tehisintellekt on lummav tehisintellekti valdkond, mis keskendub süsteemide loomisele, mis suudavad genereerida uut sisu. See sisu võib olla tekstist ja piltidest kuni muusika ja tervete virtuaalsete keskkondadeni. Üks põnevamaid generatiivse tehisintellekti rakendusi on keelemudelite valdkonnas.

## Mis on väiksed keelemudelid?

Väike keelemudel (SLM) esindab suures keelemudelis (LLM) põhinevat vähendatud varianti, kasutades paljusid LLM-ide arhitektuurilisi põhimõtteid ja tehnikaid, kuid omades märgatavalt väiksemat arvutuslikku jalajälge.

SLM-id on keelemudelite alamgrupp, mis on loodud inimlaadse teksti genereerimiseks. Erinevalt suurematest mudelitest nagu GPT-4, on SLM-id kompaktsemad ja efektiivsemad, tehes need ideaalseks rakendusteks, kus arvutusvõimsus on piiratud. Hoolimata väiksemast suurusest võivad nad täita mitmesuguseid ülesandeid. Tavaliselt ehitatakse SLM-e LLM-ide kokkusurumisel või destilleerimisel, eesmärgiga säilitada suurem osa algse mudeli funktsionaalsusest ja keelelistest võimetest. Mudeli suuruse vähendamine vähendab üldist keerukust, muutes SLM-id mälu kasutuse ja arvutusvajaduste osas efektiivsemaks. Nende optimeeringute kiuste suudavad SLM-id täita mitmeid loomuliku keele töötluse (NLP) ülesandeid:

- Teksti genereerimine: Ühtsete ja kontekstitundlike lause või lõikude loomine.
- Teksti lõpetamine: Lausetes etteantud vihjete põhjal ennustamine ja täiendamine.
- Tõlkimine: Teksti teisendamine ühest keelest teise.
- Kokkuvõtete tegemine: Pika teksti lühendamine arusaadavamateks kokkuvõteteks.

Kuigi mõningate kompromissidega jõudluse või arusaamise sügavuses võrreldes suuremate mudelitega.

## Kuidas väiksed keelemudelid töötavad?
SLM-e treenitakse suurte tekstikogumike peal. Treeningu käigus õpivad nad keele mustrid ja struktuurid, mis võimaldab neil genereerida nii grammatiliselt korrektset kui ka konteksti sobivat teksti. Treeninguprotsess hõlmab:

- Andmete kogumine: Suurte tekstikogumite kogumine erinevatest allikatest.
- Eeltöötlus: Andmete puhastamine ja organiseerimine, et muuta need treenimiseks sobivaks.
- Treenimine: Masinõppe algoritmide kasutamine, et õpetada mudelil teksti mõistmist ja genereerimist.
- Peenhäälestus: Mudeli täiendav kohandamine konkreetsete ülesannete paremaks täitmiseks.

SLM-ide areng on kooskõlas kasvava vajadusega mudelite järele, mida saab kasutada piiratud ressurssidega keskkondades, nagu mobiilseadmed või servaarvutusplatvormid, kus täismahus LLM-id võivad olla praktiliselt võimatud nende suure ressursikasutuse tõttu. Keskendudes efektiivsusele, tasakaalustavad SLM-id jõudluse ja kättesaadavuse, võimaldades laiemat rakendamist erinevates valdkondades.

![slm](../../../translated_images/et/slm.4058842744d0444a.webp)

## Õpieesmärgid

Selles õppetükis tutvustame SLM-i teadmisi ning ühendame selle Microsoft Phi-3-ga, et õppida erinevaid stsenaariume teksti sisu, nägemise ja MoE osas.

Õppetüki lõpuks peaksite suutma vastata järgmistele küsimustele:

- Mis on SLM?
- Mille poolest erinevad SLM-id ja LLM-id?
- Mis on Microsoft Phi-3/3.5 perekond?
- Kuidas käivitada järeldusi Microsoft Phi-3/3.5 perekonnaga?

Valmis? Alustame.

## Suurte keelemudelite (LLM) ja väikeste keelemudelite (SLM) erinevused

Nii LLM-id kui SLM-id on ehitatud tõenäosusliku masinõppe põhialustele, järgides sarnaseid põhimõtteid arhitektuuri kujunduses, treeningmeetodites, andmete genereerimise protsessides ja mudelite hindamises. Kuid mitmed olulised tegurid eristavad neid kahe mudelitüübi vahel.

## Väikeste keelemudelite rakendused

SLM-idel on lai rakenduste spekter, sealhulgas:

- Vestlusrobotid: Klienditoe pakkumine ja kasutajatega vestluses suhtlemine.
- Sisuloomine: Kirjanike abistamine ideede genereerimisel või isegi tervete artiklite koostamisel.
- Haridus: Õpilaste abistamine kirjutamisülesannete täitmisel või uute keeltek õppimisel.
- Juurdepääsetavus: Tööriistade loomine puuetega inimestele, näiteks tekstist kõneks süsteemid.

**Suurus**
  
Peamine erinevus LLM-ide ja SLM-ide vahel peitub mudelite mastaabis. LLM-id, nagu ChatGPT (GPT-4), võivad sisaldada hinnanguliselt 1,76 triljonit parameetrit, samas kui avatud lähtekoodiga SLM-id nagu Mistral 7B on disainitud oluliselt väiksema parameetrite arvuga—umbes 7 miljardit. See erinevus tuleneb peamiselt mudeli arhitektuuri ja treeningprotsesside erinevustest. Näiteks kasutab ChatGPT enda tähelepanu mehhanismi kodeerija-dekodeerija raamistikus, samal ajal kui Mistral 7B kasutab libiseva akna tähelepanu, mis võimaldab efektiivsemat treeningut ainult dekodeerija mudelis. See arhitektuuriline erinevus mõjutab oluliselt nende mudelite keerukust ja jõudlust.

**Mõistmine**

SLM-e optimeeritakse tavaliselt konkreetsete valdkondade jõudluseks, muutes need väga spetsialiseerituks, kuid potentsiaalselt piiratud suutlikkusega pakkuda laiaulatuslikku kontekstuaalset arusaamist mitmes teadmistevaldkonnas. Seevastu LLM-id püüavad simuleerida inimlaadset intelligentsust laiemal tasemel. Treenitud suurte ja mitmekesiste andmekogumite peal, on LLM-id kavandatud hästi toimima mitmes valdkonnas, pakkudes suuremat mitmekülgsust ja kohanemisvõimet. Seetõttu sobivad LLM-id paremini laiematesse järeltöötluse ülesannetesse, nagu loomuliku keele töötlus ja programmeerimine.

**Arvutusvõimsus**

LLM-ide treenimine ja kasutuselevõtt on väga ressursimahukad protsessid, nõudes sageli suurehulgalist arvutusinfrastruktuuri, sealhulgas suurte GPU klastrite kasutamist. Näiteks võib sellise mudeli nagu ChatGPT nullist treenimine nõuda tuhandeid GPU-sid pika aja jooksul. SLM-id, oma väiksema parameetrite arvuga, on arvutusressursside osas kättesaadavamad. Mudelid nagu Mistral 7B saab treenida ja käitada kohalikus masinas mõõduka GPU jõudlusega, kuigi treenimine nõuab ikkagi mitmetunnist tööd mitme GPU peal.

**Eelarvamus**

Eelarvamus on tuntud probleem LLM-ide puhul, peamiselt seoses treeningandmete olemusega. Need mudelid tuginevad sageli internetist pärit toorandmetele, mis võivad alahinnata või moonutada teatud gruppe, sisaldada valesid märgistusi või kajastada keelelisi eelarvamusi, mida mõjutavad murded, geograafilised erinevused ja grammatikanormid. Lisaks võib LLM-ide keeruline arhitektuur eelarvamust ettearvamatult võimendada, mis võib jääda märkamata ilma hoolika peenhäälestuseta. Teisalt on SLM-id, mis on treenitud piiratud, valdkonnapõhistel andmestikel, loomupäraselt vähem vastuvõtlikud sellistele eelarvamustele, kuigi nad ei ole täiesti immuunsed.

**Järeldus**

SLM-ide väiksem suurus annab neile olulise eelise järelduskiiruse osas, võimaldades toota väljundeid efektiivselt kohalikul riistvaral ilma vajaduseta mahuka paralleeltöötluse järele. LLM-id seevastu, oma suuruse ja keerukuse tõttu, vajavad sageli märkimisväärseid paralleelseid arvutusressursse, et saavutada vastuvõetavad järelduse ajad. Mitme samaaegse kasutaja juuresolekul aeglustub LLM-ide reageerimise kiirus veelgi, eriti kui neid kasutatakse suuremas mahus.

Kokkuvõttes jagavad nii LLM-id kui ka SLM-id masinõppe aluseid, kuid erinevad oluliselt mudeli suuruse, ressursinõuete, kontekstuaalse mõistmise, eelarvamuse vastuvõtlikkuse ja järelduskiiruse poolest. Need erinevused peegeldavad nende sobivust erinevateks kasutusjuhtudeks, kus LLM-id on mitmekülgsemad, kuid ressursimahukamad, ja SLM-id pakuvad valdkonnapõhist efektiivsust väiksema arvutuskoormusega.

***Märkus: Selles õppetükis tutvustame SLM-i näitena Microsoft Phi-3 / 3.5 põhjal.***

## Tutvustus Phi-3 / Phi-3.5 perekonnast

Phi-3 / 3.5 perekond keskendub peamiselt tekstile, nägemisele ja Agent (MoE) rakendusstsenaariumidele:

### Phi-3 / 3.5 Instruct

Peamiselt tekstigeneratsiooni, vestluste lõpetamise ja sisuteabe eraldamise jaoks jne.

**Phi-3-mini**

3,8 miljardi parameetriga keelemudel on saadaval Microsoft Foundry, Hugging Face ja Ollama platvormidel. Phi-3 mudelid ületavad märkimisväärselt sarnase ja suurema suurusega keelemudeleid võtmerakendustes (vt allolevaid võrdlustulemusi, kõrgemad arvud on paremad). Phi-3-mini ületab oma suuruselt kaks korda suuremaid mudeleid, samas kui Phi-3-small ja Phi-3-medium ületavad suuremaid mudeleid, sealhulgas GPT-3.5.

**Phi-3-small & medium**

Phi-3-small 7 miljardi parameetriga ületab GPT-3.5T mitmetes keele-, loogika-, kodeerimis- ja matemaatikavõrdlustes.

Phi-3-medium, millel on 14 miljardit parameetrit, jätkab seda suundumust ja ületab Gemini 1.0 Pro mudeli.

**Phi-3.5-mini**

Seda võib pidada Phi-3-mini uuenduseks. Kuigi parameetrite arv jääb samaks, paraneb võimekus toetada mitut keelt (toetab 20+ keelt: araabia, hiina, tšehhi, taani, hollandi, inglise, soome, prantsuse, saksa, heebrea, ungari, itaalia, jaapani, korea, norra, poola, portugali, vene, hispaania, rootsi, tai, türgi, ukraina) ning lisandub tugevam tugi pikkadele kontekstidele.

Phi-3.5-mini 3,8 miljardi parameetriga ületab sama suurusega keelemudeleid ning on tasemel kaks korda suuremate mudelitega.

### Phi-3 / 3.5 Vision

Võime mõelda Phi-3/3.5 Instruct mudelit Phi võimena mõista ning Vision kui Phi silmad maailma mõistmiseks.


**Phi-3-Vision**

Phi-3-vision, millel on vaid 4,2 miljardit parameetrit, jätkab seda traditsiooni ja ületab suuremaid mudeleid nagu Claude-3 Haiku ja Gemini 1.0 Pro V üldise visuaalse mõtlemise ülesannetes, OCR-is ning tabelite ja diagrammide mõistmisel.


**Phi-3.5-Vision**

Phi-3.5-Vision on samuti uuendus Phi-3-Visionist, lisades mitme pildi toe. Seda võib nimetada nägemise paranemiseks — mitte ainult piltide, vaid ka videote nägemiseks.

Phi-3.5-vision ületab suuremaid mudeleid nagu Claude-3.5 Sonnet ja Gemini 1.5 Flash OCR-is, tabelite ja diagrammide mõistmise ülesannetes ning on võrdväärne üldiste visuaalse teadmise mõtlemise ülesannetes. Toetab mitme kaadri sisendit, st saab teha järeldusi mitme sisendpildi põhjal.


### Phi-3.5-MoE

***Ekspertide segu (Mixture of Experts, MoE)*** võimaldab mudeleid eeltreenida palju vähemate arvutusressurssidega, mis tähendab, et sama arvutusressursiga saab mudeli või andmekogu suurust märgatavalt suurendada. Eriti peab MoE mudel saavutama sama kvaliteedi kui tihedalt ühendatud dense mudel palju kiiremini eeltreenimisel.

Phi-3.5-MoE sisaldab 16x3,8 miljardi parameetriga ekspertmoduuli. Phi-3.5-MoE, millel on vaid 6,6 miljardit aktiivset parameetrit, saavutab sarnase järelmõistmise, keele mõistmise ja matemaatika taseme kui palju suuremad mudelid.

Saame kasutada Phi-3/3.5 perekonna mudeleid erinevates stsenaariumites. Erinevalt LLM-ist saab Phi-3/3.5-mini või Phi-3/3.5-Vision mudelit paigaldada servaseadmetele.


## Kuidas kasutada Phi-3/3.5 perekonna mudeleid

Soovime kasutada Phi-3/3.5 eri stsenaariumites. Järgmisena kasutame Phi-3/3.5 mudelit vastavalt erinevatele stsenaariumitele.

![phi3](../../../translated_images/et/phi3.655208c3186ae381.webp)

### Järelduste tegemine pilveteenuse API-de kaudu

**Microsoft Foundry mudelid**

> **Märkus:** GitHub Models lõpetab töösuhet 2026. aasta juuli lõpus. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) on otsene asendus.

Microsoft Foundry mudelid on kõige otsesem tee. Saate kiiresti ligi Phi-3/3.5-Instruct mudelile Foundry mudelikataloogi kaudu. Kombineerituna Azure AI Inference SDK / OpenAI SDK-ga, saate API-le juurdepääsu koodi kaudu, et lõpule viia Phi-3/3.5-Instruct kutsed. Võite katsetada erinevaid tulemusi ka Playgroundis.

- Demo: Phi-3-mini ja Phi-3.5-mini efektide võrdlus hiina keele stsenaariumites

![phi3](../../../translated_images/et/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/et/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Kui soovite kasutada nägemise ja MoE mudeleid, saate selleks kasutada Microsoft Foundryt. Kui olete huvitatud, võite lugeda Phi-3 kokaraamatut, kuidas teha Phi-3/3.5 Instruct, Vision ja MoE kutseid Microsoft Foundry kaudu [Klõpsake siin](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Lisaks pilvepõhisele Microsoft Foundry mudelikataloogile saate kasutada ka [NVIDIA NIM-i](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) seotud kutsete tegemiseks. Võite külastada NVIDIA NIM-i, et lõpetada Phi-3/3.5 perekonna API-kutsed. NVIDIA NIM (NVIDIA Inference Microservices) on kiirendatud järeldusmikroteenuste komplekt, mis on loodud arendajate abistamiseks AI mudelite efektiivseks juurutamiseks erinevates keskkondades, sealhulgas pilvedes, andmekeskustes ja tööjaamades.

Siin on mõned peamised NVIDIA NIM-i omadused:

- **Paigaldamise lihtsus:** NIM võimaldab AI mudelite käivitamist ühe käsuga, mistõttu on seda lihtne integreerida olemasolevatesse töövoogudesse.

- **Optimeeritud jõudlus:** Kasutab NVIDIA eeloptimeeritud inferentsimootoreid, näiteks TensorRT ja TensorRT-LLM, et tagada madal latentsus ja suur läbilaskevõime.
- **Skaalautuvus:** NIM toetab Kubernetes autoskaalimist, võimaldades tõhusalt hallata erinevat koormust.
- **Turvalisus ja juur kontroll:** Organisatsioonid saavad säilitada kontrolli oma andmete ja rakenduste üle, hoides NIM mikroteenuseid ise hallataval infrastruktuuril.
- **Standardne API:** NIM pakub tööstusharu standardseid API-sid, mis teeb lihtsaks AI rakenduste nagu vestlusrobotid, AI assistendid ja muud ülesehitamise ning integreerimise.

NIM on osa NVIDIA AI Enterprise’ist, mille eesmärk on lihtsustada AI mudelite juurutamist ja opereerimist, tagades nende tõhusa töö NVIDIA GPU-del.

- Demo: NVIDIA NIM-i kasutamine Phi-3.5-Vision-API kutsumiseks [[Klõpsa siia](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5 lokaalne käitamine
Inferents Phi-3 kontekstis, või mis tahes keelemudeliga nagu GPT-3, viitab protsessile, kus genereeritakse vastuseid või prognoose sisendi põhjal. Kui sa esitad Phi-3-le prompti või küsimuse, kasutab see oma treenitud närvivõrku, et tuletada kõige tõenäolisem ja asjakohasem vastus, analüüsides mustreid ja suhteid treeningandmetes.

**Hugging Face Transformer**
Hugging Face Transformers on võimas teek, mis on loodud loomuliku keele töötlemise (NLP) ja muude masinõppe ülesannete jaoks. Siin on mõned olulised punktid:

1. **Eeltreenitud mudelid**: Pakub tuhandeid eeltreenitud mudeleid, mida saab kasutada mitme ülesande jaoks nagu teksti klassifitseerimine, nimetatud üksuste tuvastamine, küsimustele vastamine, kokkuvõtete tegemine, tõlge ja teksti genereerimine.

2. **Raamistike ühilduvus:** Teek toetab mitut süvaõppe raamistiku, sealhulgas PyTorch, TensorFlow ja JAX. See võimaldab sul mudelit treenida ühes raamistikus ja kasutada seda teises.

3. **Multimodaalsed võimalused:** Lisaks NLP-le toetab Hugging Face Transformers ka arvutinägemise ülesandeid (nt pildiklassifitseerimine, objektide tuvastamine) ning heli töötlemist (nt kõnetuvastus, heli klassifitseerimine).

4. **Lihtne kasutus:** Teek pakub API-sid ja tööriistu mudelite lihtsaks allalaadimiseks ja peenhäälestamiseks, muutes selle ligipääsetavaks nii algajatele kui ka ekspertidele.

5. **Kogukond ja ressursid:** Hugging Face’il on elav kogukond ja ulatuslik dokumentatsioon, juhendid ning õpetused, mis aitavad kasutajatel alustada ja teeki maksimaalselt ära kasutada.
[ametlik dokumentatsioon](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) või nende [GitHub hoidla](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

See on kõige sagedamini kasutatav meetod, kuid nõuab ka GPU kiirendust. Lõppude lõppuks nõuavad sellised stsenaariumid nagu Vision ja MoE palju arvutusi, mis oleksid CPU-l väga aeglased, kui neid ei kvantiseerita.


- Demo: Transformeriga Phi-3.5-Instructi kutsumine [Klõpsa siia](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformeriga Phi-3.5-Visioni kutsumine [Klõpsa siia](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformeriga Phi-3.5-MoE kutsumine [Klõpsa siia](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) on platvorm, mis lihtsustab suurte keelemudelite (LLM) lokaalset käitamist sinu masinal. See toetab erinevaid mudeleid nagu Llama 3.1, Phi 3, Mistral ja Gemma 2 ning teisi. Platvorm lihtsustab protsessi, pakkides mudeli kaalu, konfiguratsiooni ja andmed ühte paketti, muutes selle kasutajatele ligipääsetavamaks, et neid kohandada ja oma mudeleid luua. Ollama on saadaval macOS, Linuxi ja Windowsi jaoks. See on suurepärane tööriist, kui soovid eksperimenteerida või juurutada LLM-e ilma pilveteenustest sõltumata. Ollama on kõige otsemaid tee, vaja on lihtsalt käivitada järgmine käsk.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) on Microsofti offline käituskeskkond seadmes, mis võimaldab käitada mudeleid nagu Phi täielikult oma riistvaral - pole vaja Azure tellimust, API võtit ega võrguseost. See valib automaatselt parima olemasoleva täitmise pakkuja (NPU, GPU või CPU) ning pakub OpenAI-ga ühilduvat lõpp-punkti, et olemasolev `openai`/Azure AI Inference SDK kood saaks seda kasutada minimaalsete muudatustega. Vaata [Foundry Local dokumentatsiooni](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst), et alustada.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Või kasuta SDK-d otse Pythonis:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime GenAI jaoks**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) on platvormideülene inferentsi ja treeningu masinaõppe kiirendaja. ONNX Runtime Generatiivse AI (GENAI) jaoks on võimas tööriist, mis aitab sul tõhusalt käitada generatiivseid AI mudeleid eri platvormidel.

## Mis on ONNX Runtime?
ONNX Runtime on avatud lähtekoodiga projekt, mis võimaldab kõrge jõudlusega masinaõppe mudelite inferentsi. See toetab Open Neural Network Exchange (ONNX) formaadis mudeleid, mis on standard masinaõppemudelite esitamiseks. ONNX Runtime inferents võimaldab kiirendada kliendikogemust ja vähendada kulusid, toetades mudeleid süvaõppe raamistikest nagu PyTorch ja TensorFlow/Keras ning klassikalisi masinaõppe raamatukogusid nagu scikit-learn, LightGBM, XGBoost jne. ONNX Runtime on ühilduv erineva riistvara, draiverite ja operatsioonisüsteemidega ning pakub optimaalset jõudlust, kasutades vajaduse korral riistvarakiirendajaid koos graafiku optimeerimise ja transformatsioonidega.

## Mis on generatiivne AI?
Generatiivne AI viitab AI süsteemidele, mis suudavad luua uut sisu nagu tekst, pildid või muusika, põhinedes treeningandmetel. Näideteks on keelemudelid nagu GPT-3 ja pildigeneratsioonimudelid nagu Stable Diffusion. ONNX Runtime GenAI teek pakub generatiivse AI tsüklit ONNX mudelite jaoks, kaasates inferentsi ONNX Runtime abil, logits töötlemise, otsingu ja proovivõtu ning KV kohvri halduse.

## ONNX Runtime GENAI jaoks
ONNX Runtime GENAI jaoks laiendab ONNX Runtime võimeid toetada generatiivseid AI mudeleid. Siin on mõned olulised omadused:

- **Lai platvormituge:** Toimib erinevatel platvormidel, sealhulgas Windows, Linux, macOS, Android ja iOS.
- **Mudeli tugi:** Toetab palju populaarseid generatiivseid AI mudeleid, näiteks LLaMA, GPT-Neo, BLOOM ja teised.
- **Jõudluse optimeerimine:** Sisaldab optimeerimisi erinevate riistvarakiirendajate jaoks nagu NVIDIA GPU-d, AMD GPU-d ja teised.
- **Kasutusmugavus:** Pakub API-sid lihtsaks integreerimiseks rakendustesse, võimaldades teksti, piltide ja muu sisu genereerimist minimaalse koodiga.
- Kasutajad saavad kutsuda kõrgetasemelist generate() meetodit või jooksutada mudelit iteratiivselt tsüklis, genereerides ühe märgi korraga ning soovi korral uuendades genereerimisparameetreid tsükli sees.
- ONNX runtime toetab ka greedy/beam otsingut ning TopP, TopK proovivõttu tokeni järjendite genereerimiseks ja sisseehitatud logits töötlemist nagu korduskaristused. Samuti saad hõlpsasti lisada kohandatud skoorimist.

## Alustamine
ONNX Runtime GENAI kasutamise alustamiseks võid järgida järgnevaid samme:

### Installi ONNX Runtime:
```Python
pip install onnxruntime
```
### Installi Generative AI laiendused:
```Python
pip install onnxruntime-genai
```

### Käivita mudel: Siin on lihtne näide Pythonis:
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

Lisaks ONNX Runtime’ile, Ollamale ja Foundry Local viitetavadele meetoditele, saame täita ka kvantitatiivsete mudelite viite, mis põhineb eri tootjate mudeliviidetel. Nii näiteks Apple MLX raamistik Apple Metali jaoks, Qualcomm QNN koos NPU-ga, Intel OpenVINO koos CPU/GPU-ga jne. Lisainfot leiad ka [Phi-3 Cookbook’ist](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Rohkem

Oleme õppinud Phi-3/3.5 perekonna algtõed, kuid SLM kohta rohkem õppimiseks vajame põhjalikumat teadmist. Vastuseid leiab Phi-3 Cookbook’ist. Kui soovid rohkem teada, külasta palun [Phi-3 Cookbook’i](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->