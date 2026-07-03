# Promptimisinseneri põhitõed

[![Promptimisinseneri põhitõed](../../../translated_images/et/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Sissejuhatus
See moodul käsitleb olulisi mõisteid ja tehnikaid tõhusate promptide loomiseks genereerivas tehisintellektis. Kuidas sa kirjutad oma prompti LLM-ile, on samuti tähtis. Hoolikalt koostatud prompt võib saavutada parema vastuse kvaliteedi. Kuid mida täpselt tähendab terminid nagu _prompt_ ja _promptimise inseneritöö_? Ja kuidas parandada prompti _sisendit_, mida ma LLM-ile saadan? Need on küsimused, millele püüame selles ja järgmisel peatükil vastuseid leida.

_Genereeriv tehisintellekt_ suudab luua uut sisu (nt teksti, pilte, heli, koodi jne) vastuseks kasutajate päringutele. Seda tehakse kasutades _suurte keelemudelite_ (Large Language Models) nagu OpenAI GPT („Generative Pre-trained Transformer“) seeria, mis on treenitud kasutama loomulikku keelt ja koodi.

Kasutajad saavad nüüd nendega suhelda tuttavate paradigmade kaudu, näiteks vestlusena, ilma et neil oleks vaja tehnilist ekspertiisi või koolitust. Mudelid on _promptele tuginevad_ – kasutajad saadavad teksti sisendi (prompti) ja saavad vastuseks tehisintellekti väljundi (täiendus). Nad saavad siis "vestelda tehisintellektiga" iteratiivselt, mitme vooru jooksul, täpsustades oma prompti, kuni vastus vastab ootustele.

„Promptid“ muutuvad nüüd peamiseks _programmeerimisliideseks_ genereerivate tehisintellekti rakenduste jaoks, andes mudelitele juhiseid ja mõjutades tagastatud vastuste kvaliteeti. „Promptimise inseneritöö“ on kiiresti kasvav uurimisvaldkond, mis keskendub promptide _kujundamisele ja optimeerimisele_, et pakkuda järjepidevaid ja kvaliteetseid vastuseid suurel hulgal.

## Õpieesmärgid

Selles peatükis õpime, mis on promptimise inseneritöö, miks see on oluline ning kuidas kujundada tõhusamaid prompte antud mudeli ja rakendusotstarbe jaoks. Saame aru põhikontseptsioonidest ja parimatest tavadest promptimise inseneritöös – ning tutvume interaktiivse Jupyter Notebooki „liivakasti“ keskkonnaga, kus saad neid kontseptsioone reaalses näidetes rakendada.

Selle peatüki lõpuks oskame:

1. Selgitada, mis on promptimise inseneritöö ja miks see on oluline.
2. Kirjeldada prompti komponente ja nende kasutust.
3. Õppida parimaid põhimõtteid ja tehnikaid promptimise inseneritöös.
4. Rakendada õpitud tehnikaid reaalses näites, kasutades OpenAI lõpp-punkti.

## Põhimõisted

Promptimise inseneritöö: Praktika kujundada ja täiustada sisendeid, et suunata tehisintellekti mudeleid soovitud väljundite tootmiseks.  
Tokeniseerimine: Teksti muundamine väiksemateks üksusteks, mida mudel suudab mõista ja töödelda, nimetatud tokeniteks.  
Juhistega häälestatud LLM-id: Suured keelemudelid, mis on täiendavalt häälestatud konkreetsete juhistega, et parandada nende vastuste täpsust ja asjakohasust.

## Õppimise liivakast

Promptimise inseneritöö on praegu pigem kunst kui teadus. Parim viis selle tunnetuse parandamiseks on _rohkem harjutada_ ja omaks võtta katse-eksituse meetod, mis ühendab rakenduse domeenispetsialisti teadmist soovitatud tehnikate ja mudelispetsiifiliste optimeeringutega.

Selle peatüki juurde kuuluv Jupyter Notebook pakub _liivakasti_ keskkonda, kus saad õpitut katsetada – kas edasi liikudes või koodiväljakutse osana lõpus. Harjutuste läbiviimiseks vajad:

1. **Azure OpenAI API võtit** – teenuse lõpp-punkti juurdepääsu juba juurutatud LLM-ile.  
2. **Python keskkonda** – kus Notebooki saab käivitada.  
3. **Kohalikke keskkonnamuutujaid** – _täida nüüd [SEADISTUS](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) sammud, et valmis saada_.

Notebookiga on kaasas _algusülesanded_ – kuid sind julgustatakse lisama oma _Markdown_ (kirjeldus) ja _Code_ (promptide päringud) sektsioone, et proovida rohkem näiteid või ideid ning arendada oma taiplikkust promptide kujundamisel.

## Illustreeritud juhend

Soovid saada ülevaadet teemadest, mida see peatükk käsitleb, enne kui otsa sisse sukeldud? Vaata seda illustreeritud juhendit, mis annab sulle tunde peamistest käsitletavatest teemadest ja võtmetähtsusega mõtetest, mida igas punktis kaaluda. Peatüki tegevuskava viib sind põhikontseptsioonide ja väljakutsete mõistmisest nende lahendamiseni asjakohaste promptimise inseneritöö tehnikate ja parimate tavadega. Pane tähele, et selle juhendi „Täpsemad tehnikad“ osa viitab materjalile, mis kaetakse selle õppekava _järgimises_ peatükis.

![Juhend promptimise inseneritöösse](../../../translated_images/et/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Meie idufirma

Räägime nüüd, kuidas _see teema_ seostub meie idufirma missiooniga [tuua AI uuendusi haridusse](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Tahame ehitada AI-põhiseid rakendusi _isikliku õppimise_ jaoks – mõtleme siis, kuidas meie rakenduse erinevad kasutajad võiksid „kujundada“ prompte:

- **Administraatorid** võivad paluda AI-l _analüüsida õppekava andmeid, et leida puudujääke_. AI saab kokku võtta tulemused või visualiseerida neid koodiga.  
- **Õpetajad** võivad paluda AI-l _genereerida õppetund sihtrühma ja teema jaoks_. AI saab koostada isikupärastatud plaani määratud vormingus.  
- **Õpilased** võivad paluda AI-l _juhendada neid raskes aines_. AI saab nüüd juhendada õpilasi tundide, vihjete ja näidetega, mis sobivad nende tasemele.

See on vaid jäämäe tipp. Vaata [Hariduse promptid](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – avatud lähtekoodiga promptide kogu, mida kureerivad hariduseksperdid – et saada laiem ülevaade võimalustest! _Proovi mõnda neist promptidest liivakastis või OpenAI mänguväljakul ja vaata, mis juhtub!_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## Mis on promptimise inseneritöö?

Alustasime seda peatükki, määratledes **promptimise inseneritöö** kui protsessi, milleks on tekstisisendite (promptide) _kujundamine ja optimeerimine_, et anda järjepidevaid ja kvaliteetseid vastuseid antud rakenduse eesmärgile ja mudelile. Saame seda mõelda kui kaheastmelist protsessi:

- _kujundada_ algne prompt antud mudelile ja eesmärgile  
- _täiustada_ prompti iteratiivselt vastuse kvaliteedi parandamiseks

See on vajalikult katse-eksituse meetod, mis nõuab kasutaja intuitsiooni ja pingutust optimaalseks tulemuseks. Miks see siis oluline on? Sellele vastamiseks peame esmalt mõistma kolme mõistet:

- _Tokeniseerimine_ = kuidas mudel „näeb“ prompti  
- _Põhimudelite_ toimimine = kuidas baaskeelemudel prompti „tööleb“  
- _Juhistega häälestatud LLM-id_ = kuidas mudel saab nüüd „töid“ näha

### Tokeniseerimine

LLM näeb prompti kui _tokenite jada_, kus erinevad mudelid (või sama mudeli versioonid) võivad sama prompti tokeniseerida erinevalt. Kuna LLM-id on treenitud tokenitele (mitte tooraine tekstile), mõjutab prompti tokeniseerimine otseselt vastuse kvaliteeti.

Intuitsiooni saamiseks, kuidas tokeniseerimine töötab, proovi tööriistu nagu [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst), mida on näidatud allpool. Kopeeri oma prompt sinna – ja vaata, kuidas see tokeniteks muundub, pöörates tähelepanu tühikute ja kirjavahemärkide käsitlemisele. Pane tähele, et see näide kasutab vanemat LLM-i (GPT-3) – seega uue mudeliga võib tulemus erineda.

![Tokeniseerimine](../../../translated_images/et/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Kontseptsioon: Põhimudelid

Kui prompt on tokeniseeritud, on ["Põhipõhimudeli"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (või Foundation mudeli) põhiülesanne ennustada järgmist tokenit antud jadas. Kuna LLM-id on treenitud tohutul hulgal tekstidel, tunnetavad nad statistilisi seoseid tokenite vahel ja suudavad seda ennustust teha teataval täpsusel. Pane tähele, nad ei mõista prompti või tokeni sõnade _tähendust_; nad näevad mustrit, mida saab „täita“ järgnevate ennustustega. Nad võivad jätkata jada ennustamist, kuni kasutaja sekkub või kehtib mõni eelnevalt määratletud tingimus.

Soovid näha, kuidas promptipõhine täiendamine toimib? Sisesta ülaltoodud prompt Azure OpenAI Studio [_Vestlusmänguväljakule_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) vaikeseadistustega. Süsteem on seadistatud käsitlema prompti informatsioonipäringuna – nii näed vastust, mis rahuldab selle konteksti.

Aga mis siis, kui kasutaja tahab näha midagi konkreetset, mis vastab mingile kriteeriumile või ülesande eesmärgile? Siin tulevad mängu _juhistega häälestatud_ LLM-id.

![Põhimudeli vestluse täiendamine](../../../translated_images/et/04-playground-chat-base.65b76fcfde0caa67.webp)

### Kontseptsioon: Juhistega häälestatud LLM-id

[Juhistega häälestatud LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) alustab põhimudelist ja täiustab seda näidete või sisend-väljund-paaridega (nt mitme vooru „sõnumitega“), mis sisaldavad selgeid juhiseid – ning AI vastab püüdes neid juhiseid järgida.

See kasutab tehnikaid nagu inimeste tagasisidega tugevdatud õppimine (RLHF), mis õpetab mudelit _juhiseid järgima_ ja _tagasisidest õppima_, nii et vastused sobivad paremini praktilisteks rakendusteks ja on kasutaja eesmärkidele asjakohasemad.

Proovime seda – mine tagasi ülaltoodud prompti juurde, aga muuda nüüd _süsteemisõnumit_, pakkudes järgmist juhist kontekstina:

> _Kokkuvõtke teile antud sisu teise klassi õpilasele. Piira tulemus ühe lõigu ja 3-5-e punktiga._

Näed, kuidas tulemus on nüüd häälestatud soovitud eesmärgile ja vormingule? Õpetaja saab selle vastuse otse kasutada oma tunni slaididel.

![Juhistega häälestatud LLM vestluse täiendamine](../../../translated_images/et/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Miks meil on vaja promptimise inseneritööd?

Nüüd, kui teame, kuidas LLM-id promte töötlevad, räägime, _miks_ meil on promptimise inseneritöö vaja. Vastus peitub selles, et tänased LLM-id esitavad mitmeid väljakutseid, mis muudavad _usaldusväärsete ja järjepidevate vastuste_ saavutamise keerulisemaks ilma promptide ülesehitusele ja optimeerimisele pingutust panemata. Näiteks:

1. **Mudelite vastused on juhuslikud.** _Sama prompt_ võib anda erinevaid vastuseid erinevates mudelites või mudeli versioonides. Ja isegi _samas mudelis_ erinevatel aegadel võivad vastused erineda. _Promptimise inseneritöö tehnikaid saab kasutada nende variatsioonide minimeerimiseks, pakkudes paremaid piiranguid_.

1. **Mudeli vastused võivad olla väljamõeldised.** Mudelid on eelnevalt treenitud _suurtel, kuid piiratud_ andmekogudel, mistõttu neil puudub teadmine väljaspool seda koolitusulatusest. Selle tulemusena võivad nad toota täiendusi, mis on ebatäpsed, kujuteldavad või otseselt vastuolus teadaolevate faktidega. _Promptimise inseneritöö abil saavad kasutajad tuvastada ja vähendada selliseid väljamõeldisi, näiteks küsides AI-lt allikaid või põhjendusi_.

1. **Mudelite võimed varieeruvad.** Uuemad mudelid või mudelite generatsioonid omavad rikkalikumaid võimeid, kuid toovad kaasa ka unikaalseid eripärasid ja kulutaseme ning keerukuse kompromisse. _Promptimise inseneritöö aitab välja töötada parimaid tavasid ja töövooge, mis abstraktivad erinevused ja kohanduvad mudelispetsiifiliste nõuetega skaleeritaval ja sujuval viisil_.

Vaatame seda praktikas OpenAI või Azure OpenAI mänguväljakul:

- Kasuta sama prompti erinevate LLM-juurutustega (nt OpenAI, Azure OpenAI, Hugging Face) – kas täheldasid variatsiooni?  
- Kasuta sama prompti korduvalt _samas_ LLM-juurutuses (nt Azure OpenAI mänguväljak) – kuidas need variatsioonid erinesid?

### Näide väljamõeldistest

Selles kursuses kasutame terminit **„väljamõeldis“** viitamaks nähtusele, kus LLM-id mõnikord genereerivad faktuaalselt ebatäpseid andmeid oma koolituspiirangute või teiste tegurite tõttu. Võid olla kuulnud ka termini _„hallutsinatsioonid“_ populaarsetes artiklites või teadusuuringutes. Kuid soovitame tungivalt kasutada _„väljamõeldis“_, et mitte inimesele omast käitumist masina poolt juhitud tulemusele valesti taibata. See toetab ka [Vastutustundliku tehisintellekti juhiseid](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) terminoloogilisest vaatevinklist, eemaldades termineid, mida võib pidada solvavateks või mittekaasavateks mõnes kontekstis.

Tahad tunda, kuidas väljamõeldised toimivad? Mõtle promptile, mis palub AI-l genereerida sisu eksisteerimatu teema kohta (et veenduda, et see ei ole koolitusandmetes). Näiteks – ma proovisin sellist prompti:

> **Prompt:** genereeri tunniplaan teemal „Marslaste sõda aastal 2076“.
Veebipõhine otsing näitas mulle, et Marsi sõdade kohta on ilmunud väljamõeldud kirjeldusi (nt telesarjad või raamatud) – kuid mitte aastal 2076. Mõistuspäraselt ütleb see, et 2076 on _tulevikus_ ning seega ei saa seda seostada reaalse sündmusega.

Mis siis juhtub, kui me selle käsu käivitame erinevate LLM-i pakkujatega?

> **Vastus 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/et/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Vastus 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/et/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Vastus 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/et/04-fabrication-huggingchat.faf82a0a51278956.webp)

Nagu oodata, toodab iga mudel (või mudeliversioon) tänu stokhastilisele käitumisele ja mudelivõimekuse erinevustele veidi erinevaid vastuseid. Näiteks on üks mudel suunatud 8. klassi tasemele, teise puhul arvatakse, et kasutaja on keskkooliõpilane. Kuid kõik kolm mudelit lõid vastuseid, mis võiksid veenda teavet mitteomavat kasutajat sündmuse reaalsuses.

Käsu insener-tehnikad, nagu _metakäsustamine_ ja _temperatuuri seadistamine_, võivad vähendada mudeli väljamõeldisi teatud määral. Uued käsu insener-tehnikate _arhitektuurid_ integreerivad sujuvalt uusi tööriistu ja meetodeid käsuvoogu, et neid efekte leevendada või vähendada.

## Juhtumiuuring: GitHub Copilot

Lõpetame selle lõigu tunnetusega, kuidas käsu insener-tehnikat kasutatakse reaalse maailma lahendustes, vaadates üht juhtumiuuringut: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot on sinu "tehisintellekti paarisprogrammeeri" abimees – see teisendab teksti käsud koodilõppudeks ja on integreeritud sinu arenduskeskkonda (nt Visual Studio Code) sujuvaks kasutajakogemuseks. Järgnevas blogiseerias on dokumenteeritud, et varasem versioon põhines OpenAI Codex mudelil – insenerid mõistsid kiiresti vajadust mudelit täpsustada ja arendada paremaid käsu insener-tehnikaid koodi kvaliteedi parandamiseks. Juulis [esitlesid nad täiustatud tehisintellekti mudelit, mis läheb Codexist kaugemale](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) veelgi kiiremaks soovitusteks.

Loe postitusi järjekorras, et jälgida nende õpikogemust.

- **Mai 2023** | [GitHub Copilot mõistab sinu koodi paremini](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mai 2023** | [GitHub sees: Töötamine GitHub Copiloti taga olevate LLM-idega](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Juuni 2023** | [Kuidas kirjutada paremaid käske GitHub Copilotile](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Juuli 2023** | [.. GitHub Copilot läheb Codexist kaugemale täiustatud AI mudeliga](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Juuli 2023** | [Arendaja teejuht käsu insener-tehnikate ja LLM-idega](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **September 2023** | [Kuidas ehitada ettevõttesisene LLM-rakendus: õppetunnid GitHub Copilotilt](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Sa võid uurida ka nende [Inseneriblogi](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) veel postitusi nagu [see siinne](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), mis näitab, kuidas neid mudeleid ja tehnikaid _rakendatakse_ reaalse maailma rakenduste loomiseks.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## Käsu koostamine

Olemas on arusaam, miks käsu insener-tehnika on oluline – nüüd vaatame, kuidas käske _koostatakse_, et me saaksime hinnata erinevaid meetodeid efektiivsema käsukujunduse jaoks.

### Lihtne käsk

Alustame lihtsast käsust: tekstisisend, mis saadetakse mudelile ilma muude kontekstideta. Näiteks – kui saata USA hümni esimesed sõnad OpenAI [Completion API-le](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), täieneb vastus koheselt järgmiste ridadega, näidates põhiennustuse käitumist.

| Käsk (sisend)        | Täiendamine (väljastus)                                                                                                                                               |
| :------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Oh say can you see   | Tundub, et alustad sõnadega "The Star-Spangled Banner", mis on USA hümn. Täis tekst on ...                                                                            |

### Kompleksne käsk

Lisa nüüd sellele lihtsale käsule kontekst ja juhised. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) võimaldab koondada komplekse käsu mitmest _sõnumist_ koosnevasti:

- Sisendi/väljundi paarid, mis peegeldavad _kasutaja_ sisendit ja _abilise_ vastust.
- Süsteemi sõnum, mis seab abi käitumise või isiksuse konteksti.

Päring on nüüd alljärgnevas vormis, kus _tokeniseerimine_ haarab efektiivselt kontekstist ja vestlusest asjakohase info. Seega võib süsteemi konteksti vahetus avaldada sama suurt mõju täienduste kvaliteedile kui kasutaja antavad sisendid.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Juhise käsk

Ülaltoodud näidetes oli kasutaja käsk lihtne tekstipäring, mida saab tõlgendada teabepäringuna. _Juhise_ käsustamisel saame kasutada seda teksti ülesande täpsemaks määratluseks, andes AI-le parema juhise. Näide:

| Käsk (sisend)                                                                                              | Täiendamine (väljastus)                                                    | Juhise tüüp      |
| :--------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------- | :---------------- |
| Kirjuta kirjelduse Kodusõjast                                                                                | _tagastas lihtsa lõigu_                                                    | Lihtne            |
| Kirjuta kirjelduse Kodusõjast. Too välja olulised kuupäevad ja sündmused ning selgita nende tähendust          | _tagastas lõigu, millele järgnes nimekiri olulistest kuupäevadest koos seletustega_ | Kompleksne        |
| Kirjuta kirjelduse Kodusõjast 1 lõigus. Too 3 punkti oluliste kuupäevade ja mõjude kohta. Too veel 3 punkti tähtsate ajalooliste tegelaste ja panuste kohta. Tagasta väljund JSON-failina | _tagastab põhjaliku sisu tekstikastis, vormistatud JSON-ina, mida saad vajadusel koopida, faili salvestada ja valideerida_ | Kompleksne. Vormindatud. |

## Peamine sisu

Ülaltoodud näidetes oli käsk endiselt suhteliselt avatud, lubades LLM-il ise otsustada, milline osa eeltreenitud andmetest asjakohane on. _Peamise sisu_ disainimustriga jagatakse sisendtekst kaheks osaks:

- juhis (tegevus)
- vastav sisu (mõjutab tegevust)

Näide, kus juhis on "kokkuvõtte tee 2 lauses".

| Käsk (sisend)                                                                                                                                                     | Täiendamine (väljastus)                                                                                                                                                             |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter on Päikesest viies planeet ja Päikesesüsteemi suurim. See on gaasihiid, mille mass on tuhandik Päikese massist, kuid kaks ja pool korda suurem kui kõik teised planeedid kokku. Jupiter on üks eredamaid palja silmaga nähtavaid objekte öötaevas ning on olnud tuntud iidsetest tsivilisatsioonidest enne ajaloo kirja pandud aega. Selle nimi on tuletatud Rooma jumalast Jupiterist.[19] Maa pealt vaadates võib Jupiter olla piisavalt hele, et selle peegeldatud valgus visandaks nähtavaid varje,[20] ning see on keskmiselt kolmas eredaim looduslik objekt öötaevas pärast Kuu ja Veenust. <br/> **Kokkuvõtte sellest 2 lühikese lausega** | Jupiter, Päikesest viies planeet, on suurim Päikesesüsteemis ja tuntud kui üks eredamaid öötaeva objekte. Nimeliselt Rooma jumal Jupiter, on tegu gaasihiidega, mille mass on kaks ja pool korda suurem kui kõik teised planeedid kokku. |

Peamise sisu segmenti võib kasutada mitmeti, et suunata efektiivsemaid juhiseid:

- **Näited** – selle asemel, et anda mudelile otsene juhis, anna talle näited, mida teha, ja lase tal mustrit tuletada.
- **Vihjed** – juhise järel esita "vihje", mis suunab täiendust, juhatades mudelit asjakohasema vastuse suunas.
- **Mallid** – korduvad 'retseptid' käskude jaoks koos kohatäitjate (muutujate) ja andmetega, mida saab konkreetse juhtumi jaoks kohandada.

Vaatame seda praktikas.

### Näidete kasutamine

Selle meetodi puhul kasutatakse peamist sisu, et "toita mudelit" mõne näitega soovitud väljundi kohta antud juhise jaoks ja lasta tal mustrit tuletada. Sõltuvalt näidete arvust võib tegu olla nullkontsaga, ühe näite või mõnenäitega stiiliga käsustamisega.

Käsk koosneb nüüd kolmest komponendist:

- ülesande kirjeldus
- mõned näited soovitud väljundist
- uue näite algus (mis muutub implitsiitseks ülesande kirjelduseks)

| Õppimise tüüp | Käsk (sisend)                                                                                                                                         | Täiendamine (väljastus)      |
| :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------- |
| Nullkontsa     | "The Sun is Shining". Tõlgi hispaaniakeelde                                                                                                        | "El Sol está brillando".      |
| Ühe näitega   | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                           | "Es un día frío y ventoso".   |
| Mõnenäitega   | Mängija jooksis kordused => Pesapall <br/> Mängija pani ässaks => Tennis <br/> Mängija lööb kuus => Kriket <br/> Mängija sooritab slämmi =>        | Korvpall                      |
|               |                                                                                                                                                     |                              |

Pane tähele, kuidas nullkontsa käsus tuli anda otsene juhis ("Tõlgi hispaaniakeelde"), kuid ühe näitega käsus on see juba implitsiitne. Mõnenäitega näide näitab, et rohkemate näidete lisamine võimaldab mudelil täpsemini mustrit tuletada ilma lisajuhisteta.

### Käsu vihjed

Teine peamise sisu kasutamise tehnika on anda _vihjeid_ mitte näiteid. Sel juhul antakse mudelile suunis, alustades lõiguga, mis peegeldab soovitud vastuse vormingut. Mudeel "võtab vihje üles" ja jätkab samas stiilis.

| Vihjete arv | Käsk (sisend)                                                                                                                                                                                                                                                                                                                                                                                                                     | Täiendamine (väljastus)                                                                                                                                                                                                                                      |
| :----------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0            | Jupiter on Päikesest viies planeet ja suurim Päikesesüsteemis. See on gaasihiid, mille mass on tuhandik Päikese massist, kuid kaks ja pool korda suurem kui kõik teised planeedid kokku. Jupiter on üks eredamaid palja silmaga nähtavaid objekte öötaevas ning on olnud tuntud iidsetest tsivilisatsioonidest enne ajaloo kirja pandud aega. <br/>**Kokkuvõte sellest**                          | Jupiter on Päikesesüsteemi suurim planeet ja viies Päikese suhtes. See on gaasihiid, mille mass on 1/1000 Päikese massist, kuid vähemalt kõikide teiste planeetide masside summa. Iidsetest tsivilisatsioonidest on Jupiter olnud kaua tuntud ja on kergesti nähtav öötaevas. |
| 1              | Jupiter on Päikesest viies planeet ning Päikesesüsteemi suurim planeet. See on gaasihiiglane, mille mass on Päikese massist tuhandik, kuid ühtekokku kahekordne ja pool kõigi teiste Päikesesüsteemi planeetide massidest. Jupiter on üks eredamaid palja silmaga nähtavaid objekte öises taevas ja seda on tuntud iidsetest tsivilisatsioonidest juba enne kirjaloolist aega. <br/>**Kokkuvõte** <br/> Mida me õppisime, on see, et Jupiter | on Päikesest viies planeet ning Päikesesüsteemi suurim planeet. See on gaasihiiglane, mille mass on Päikese massist tuhandik, kuid see on kahe ja poole korra suurem kui teiste planeetide ühisema. See on hõlpsasti palja silmaga nähtav ja seda on tuntud alates antiiksest ajast.                        |
| 2              | Jupiter on Päikesest viies planeet ning Päikesesüsteemi suurim planeet. See on gaasihiiglane, mille mass on Päikese massist tuhandik, kuid kahe ja poole korra suurem kui kõigi teiste Päikesesüsteemi planeetide ühisema. Jupiter on üks eredamaid palja silmaga nähtavaid objekte öises taevas ning seda on tuntud iidsetest tsivilisatsioonidest juba enne kirjalikke allikaid. <br/>**Kokkuvõte** <br/> Top 3 fakti, mida õppisime:         | 1. Jupiter on Päikesest viies planeet ning Päikesesüsteemi suurim planeet. <br/> 2. See on gaasihiiglane, mille mass on Päikese massist tuhandik...<br/> 3. Jupiter on palja silmaga nähtav olnud juba iidsetest aegadest ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Prompti malli

Prompti mall on _eelnevalt määratletud juhis prompti jaoks_, mida saab salvestada ja taaskasutada vastavalt vajadusele, et pakkuda järjepidevamat kasutajakogemust suurel hulgal. Kõige lihtsamas vormis on see lihtsalt kogumik prompti näidetest nagu [see OpenAI näide](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), mis pakub nii interaktiivseid prompti komponente (kasutaja ja süsteemi sõnumid) kui ka API-põhist päringu vormingut - et toetada korduskasutust.

Raskemates vormides, nagu [LangChain'i näide](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), sisaldab see _kohatäiteid_, mida saab asendada andmetega mitmetest allikatest (kasutaja sisend, süsteemi kontekst, välised andmeallikad jne), et genereerida prompt dünaamiliselt. See võimaldab meil luua taaskasutatavate promptide raamatukogu, mida saab kasutada, et juhtida järjepidevaid kasutajakogemusi **programmiliselt** suurel hulgal.

Lõpuks seisneb mallide tõeline väärtus vertikaalsete rakendusvaldkondade jaoks mõeldud _promptide raamatukogude_ loomises ja avaldamises – kus prompti mall on nüüd _optimeeritud_, et peegeldada konkreetsete rakenduste konteksti või näiteid, mis muudavad vastused sihtrühmale asjakohasemaks ja täpsemaks. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) hoidla on suurepärane näide sellest lähenemisest, kogudes hariduse valdkonna promptide raamatukogu, kus rõhutatakse võtmeteemasid nagu tunni planeerimine, õppekava koostamine, õpilaste juhendamine jms.

## Tugimaterjalid

Kui me mõtleme promptide koostamisele kui juhise (ülesande) ja sihtmärgi (põhisisu) olemasolule, siis _teisene sisu_ on nagu lisakontekst, mida me anname, et **mõjutada väljundit mingil viisil**. See võib olla häälestusparameetrid, vormindusjuhised, teemad ja taksonoomiad jmt, mis aitavad mudelil _kohandada_ oma vastuseid vastavalt kasutaja eesmärkidele või ootustele.

Näiteks: antud hooaja kursuste kataloog koos ulatusliku metainfoga (nimi, kirjeldus, tase, meta-sildid, juhendaja jms) kõigi saadaolevate kursuste kohta õppekavas:

- me võime määratleda juhise "kokkuvõtte tee sügis 2023 kursuste kataloogist"
- me võime kasutada põhisisu, et anda paar näidet soovitud väljundist
- me võime kasutada teisest sisu, et tuvastada 5 huvipakkuvamat „sildi“.

Nüüd saab mudel anda kokkuvõtte näidatud vormingus – kuid kui tulemus sisaldab mitut silti, saab ta prioriteerida teisest sisust tuvastatud 5 silti.

---

<!--
TUNNIMALL:
See üksus peaks käsitlema põhikontseptsiooni #1.
Toetada kontseptsiooni näidete ja viidetega.

KONTSEPTSIOON #3:
Promptide inseneritehnikad.
Millised on mõned põhitehnikad promptide inseneri jaoks?
Illustreerida harjutustega.
-->

## Parimad tavad promptide koostamisel

Nüüd, kui me teame, kuidas promptide koostamine toimib, võime hakata mõtlema nende _kujundamisele_, et järgida parimaid tavasid. Seda saab vaadelda kahes osas – õige _mõtteviisi_ omamine ja sobivate _tehnikate_ rakendamine.

### Promptide insenerimise mõtteviis

Promptide insenerimine on katse-eksituse meetod, mistõttu pea meeles kolme laiemat juhist:

1. **Valdkonna tundmine on oluline.** Vastuse täpsus ja asjakohasus sõltub _valdkonnast_, kus rakendus või kasutaja tegutseb. Kasuta oma intuitsiooni ja valdkonna teadmisi, et veelgi kohandada _tehnikaid_. Näiteks määra _valdkonnapõhised isiksused_ oma süsteemi promptides või kasuta _valdkonnapõhiseid malle_ kasutaja promptides. Paku teisest sisu, mis peegeldab valdkonnapõhist konteksti, või kasuta _valdkonnapõhiseid vihjeid ja näiteid_, et suunata mudelit tuttavate kasutusmustrite poole.

2. **Mudeli tundmine loeb.** Teame, et mudelid on loodult juhuslikud ehk stokastilised. Kuid mudelid võivad erineda kasutatava treeningandmestiku (eelõpetatud teadmised), võimaluste (nt API või SDK kaudu) ja optimeeritud sisutüübi (nt kood vs pildid vs tekst) poolest. Mõista, millised on sinu mudeli tugevused ja piirangud, ning kasuta seda teadmist, et _prioriseerida ülesandeid_ või luua _kohandatud malle_, mis on optimeeritud mudeli võimetele.

3. **Iteratsioon ja valideerimine on tähtsad.** Mudelid arenevad kiiresti, samuti promptide insenerimise tehnikad. Sinu kui valdkonna eksperdi jaoks võib olla ka muid kontekste või kriteeriume, mis ei pruugi laiemale kogukonnale kehtida. Kasuta promptide tööriistu ja tehnikaid, et “kiirendada” prompti loomist, seejärel korda ja valideeri tulemusi oma intuitsiooni ja valdkonna teadmiste põhjal. Kogu oma tähelepanekud ja loo **teadmusbaas** (nt promptide raamatukogud), mida teised saavad kasutada uue baasena kiiremaks iteratsiooniks tulevikus.

## Parimad tavad

Vaatame nüüd mõningaid üldisi parimaid tavasid, mida soovitavad [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) ja [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) praktikad.

| Mida                              | Miks                                                                                                                                                                                                                                           |
| :-------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hinda uusimaid mudeleid.           | Uued mudelisukupõlved toovad tõenäoliselt paremaid funktsioone ja kvaliteeti – aga võivad tuua ka kõrgemaid kulusid. Testi nende mõju, seejärel tee migratsioonialased otsused.                                                                       |
| Erista juhiseid ja konteksti        | Kontrolli, kas sinu mudel/teenusepakkuja määratleb juhtmärke (delimitereid), mis aitavad selgelt eristada juhiseid, põhisisu ja teisest sisu. See aitab mudelil tokenitele täpsemaid kaalutisi määrata.                                            |
| Ole konkreetne ja selge            | Anna detailselt teada soovitud kontekstist, tulemusest, pikkusest, vormingust, stiilist jms. See parandab nii kvaliteeti kui ka vastuste järjepidevust. Kirjuta retseptid taaskasutatavatena mallidesse.                                          |
| Ole kirjeldav, kasuta näiteid      | Mudelid reageerivad sageli paremini “näita ja räägi” lähenemisele. Alusta `zero-shot` prooviga, kus annad juhise (aga mitte näiteid) ja seejärel kasuta `few-shot` meetodit, kus tood mõned soovitud väljundi näited. Kasuta analoogiaid.         |
| Kasuta vihjeid, et alustada täitmisi | Suunamise eesmärgil paku mõningaid juhtlaused või fraasid, mida mudel saab kasutada vastuse alustamiseks.                                                                                                                                    |
| Korda, kui vaja                    | Mõnikord võib olla vajalik prompti mudelile mitu korda suunata. Kasuta juhiseid nii enne kui pärast põhisisu, kasuta nii juhist kui vihjet jne. Korda ja valideeri, et näha, mis töötab.                                                    |
| Järjestus loeb                     | Informatsiooni esitusjärjestus mudelile võib mõjutada väljundit, ka õppekõrguse näidetes, tänu hiljutise info eelistamisele. Proovi erinevaid võimalusi ja vaata, mis töötab kõige paremini.                                                  |
| Paku mudelile “välja pääsemist”     | Määra mudelile tagavaravastus, mida ta saab anda, kui ülesannet ei õnnestu kuidagi lõpetada. See vähendab valeinfo või väljamõeldud vastuste tekkimist.                                                                                       |
|                                   |                                                                                                                                                                                                                                               |

Nagu iga parima tava puhul, pea meeles, et _sinu kogemus võib varieeruda_ mudeli, ülesande ja valdkonna põhjal. Kasuta neid lähtepunktina ja korda, et leida just sulle sobiv viis. Jälgi pidevalt promptide insenerimise protsessi, kuna uued mudelid ja tööriistad tulevad turule, keskendudes protsessi skaleeritavusele ja vastuste kvaliteedile.

<!--
TUNNIMALL:
Sellesse üksusesse lisa koodiväljakutse, kui see sobib.

VÄLJAKUTSE:
Lingiga Jupyter Notebook’ile, kus juhised on ainult kommentaarid (koodi osad on tühjad).

LAHENDUS:
Link sama notebooki koopiale, kus promptid on täidetud ja käivitatud, tuues ühe näite väljundist.
-->

## Kodune ülesanne

Palju õnne! Jõudsid tunni lõpuni! On aeg testida mõnda neist kontseptsioonidest ja meetoditest reaalsete näidete peal!

Me kasutame selleks Jupyter Notebooki, kus on harjutused, mida saad interaktiivselt teha. Samuti saad laiendada notebook’i oma Markdown’i ja koodi rakkudega, et uurida ideid ja meetodeid omal käel.

### Alustamiseks tee repo forkimine, seejärel

- (Soovituslik) Käivita GitHub Codespaces
- (Alternatiiv) klooni repo oma seadmesse ja kasuta seda Docker Desktopiga
- (Alternatiiv) Ava notebook oma eelistatud keskkonnas.

### Järgmiseks seadista oma keskkonnamuutujad

- Kopeeri repo juurest fail `.env.copy` faili `.env` ja täida väljad `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` ja `AZURE_OPENAI_DEPLOYMENT`. Tagasi tulles vaata [Õppimise Liivakasti](#õppimise-liivakast) juhiseid.

### Ava seejärel Jupyter Notebook

- Vali täitmise kernel. Kui valid variandid 1 või 2, siis vali lihtsalt dev containeri poolt pakutav vaikimisi Python 3.10.x kerneli.

Oled valmis harjutusi jooksutama. Pane tähele, et siin pole _õigeid ega valesid_ vastuseid – lihtsalt katsetad erinevaid võimalusi ja kogud tunnetust, mis mudel ja rakendus domeenile sobib.

_Sellepärast pole selles tunnis koodi lahenduste osi. Selle asemel on notebook’is Markdown lahtrid pealkirjaga "Minu lahendus:", mis näitab üht näidende väljundit võrdluseks._

 <!--
TUNNIMALL:
Järgmises lõigus on kokkuvõte ja ressursid iseseisvaks õppeks.
-->

## Teadmiste kontroll

Milline järgnevatest on hea prompt mõne mõistlikku head tava järgides?

1. Näita mulle pilti punasest autost
2. Näita mulle pilti punasest Volvomehhanismiga XC90 mudeli autost, mis on kaljunuki ääres päikeseloojangul
3. Näita mulle pilti punasest Volvomehhanismiga XC90 mudelist

A: 2, see on parim prompt, sest see annab üksikasjad "mida" ja läheb spetsiifikateni (mitte lihtsalt üks auto, vaid konkreetne marka ja mudel) ning kirjeldab ka üldist keskkonda. 3 on järgmine parim, sest see sisaldab ka palju kirjeldust.

## 🚀 Väljakutse

Proovi kasutada vihje tehnikaid promptiga: Täienda lauset "Näita mulle pilti punasest Volvomehhanismiga XC90 mudelist ja ". Mida see vastab ja kuidas saaksid seda täiustada?

## Väga hea töö! Jätka õppimist

Kas soovid õppida rohkem erinevaid promptide insenerimise kontseptsioone? Mine [jätkuõppe lehele](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kus on teema kohta teisi suurepäraseid ressursse.

Mine edasi 5. tunnile, kus vaatleme [edasijõudnumaid promptide tehnikaid](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->