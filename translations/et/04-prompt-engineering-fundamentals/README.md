# Päringu Insenertehnika Alused

[![Päringu Insenertehnika Alused](../../../translated_images/et/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Sissejuhatus
See moodul käsitleb olulisi mõisteid ja tehnikaid tõhusate päringute loomisel generatiivsete tehisintellekti mudelite jaoks. Kuidas sa kirjutad oma päringu LLM-ile on samuti oluline. Hoolikalt koostatud päring võib saavutada parema vastuste kvaliteedi. Kuid mida täpselt tähendavad mõisted nagu _päring_ ja _päringu insenertehnika_? Ja kuidas ma saan parandada päringu _sisendit_, mida ma LLM-ile saadan? Need on küsimused, millele püüame vastata käesolevas ja järgnevates peatükkides.

_Generatiivne tehisintellekt_ suudab luua uut sisu (nt tekst, pildid, heli, kood jms) kasutajate päringutele vastuses. Seda saavutatakse kasutades _suurte keelemudelite_ nagu OpenAI GPT ("Generative Pre-trained Transformer") seeria, mida on treenitud kasutama loomulikku keelt ja koodi.

Kasutajad saavad nüüd nendega suhelda tuttavate paradigmade kaudu nagu vestlus, ilma et oleks vaja tehnilisi teadmisi või koolitust. Mudelid töötavad _päringupõhiselt_ – kasutajad saadavad tekstisisendi (päringu) ja saavad tagasi tehisintellekti vastuse (täienduse). Nad saavad seejärel AI-ga "vestelda" järjepidevalt, mitme vooruga, täiendades oma päringut, kuni vastus vastab nende ootustele.

"Päringud" muutuvad nüüd generatiivsete AI rakenduste peamiseks _programmeermisliideseks_, mis ütlevad mudelitele, mida teha ja mõjutavad tagastatud vastuste kvaliteeti. "Päringu insenertehnika" on kiiresti kasvav uurimisvaldkond, mis keskendub päringute _disainile ja optimeerimisele_, eesmärgiga tagada järjepidevad ja kvaliteetsed vastused suures mahus.

## Õpieesmärgid

Selles õppetükis õpime, mis on päringu insenertehnika, miks see on tähtis ja kuidas saame koostada tõhusamaid päringuid antud mudeli ja rakenduse eesmärgi jaoks. Mõistame põhikontseptsioone ja parimaid tavasid päringute insenertehnikas – ning tutvume interaktiivse Jupyteri märkmiku "liivakastiga", kus saame neid kontseptsioone reaalses näites rakendada.

Selle õppetüki lõpuks oskame:

1. Selgitada, mis on päringu insenertehnika ja miks see oluline on.
2. Kirjeldada päringu komponente ja nende kasutust.
3. Õppida päringu insenertehnika parimaid tavasid ja tehnikaid.
4. Rakendada õpitud tehnikaid reaalsetes näidetes, kasutades OpenAI lõpp-punkti.

## Peamised mõisted

Päringu insenertehnika: Tehisintellekti mudelite juhendamiseks soovitud väljundite tootmiseks sisendite kujundamise ja täiustamise praktika.
Tokeniseerimine: Teksti teisendamise protsess väiksemateks üksusteks, mida nimetatakse tokeniteks, mida mudel suudab mõista ja töödelda.
Juhendusega treenitud LLM-id: Suured keelemudelid, mida on peenhäälestatud konkreetsete juhistega, et parandada nende vastuste täpsust ja asjakohasust.

## Õppimise liivakast

Päringu insenertehnika on praegu rohkem kunst kui teadus. Parim viis oma intuitsiooni parandamiseks on _rohkem harjutada_ ja rakendada katse-eksituse meetodit, mis ühendab rakendusvaldkonna ekspertiisi soovitatud tehnikate ja mudelispetsiifiliste optimeerimistega.

Selle õppetüki Jupyteri märkmik pakub _liivakasti_ keskkonna, kus saad testiida õpitut – kas jooksvalt või koodiülesande osana õppetüki lõpus. Harjutuste täitmiseks vajad:

1. **Azure OpenAI API võtit** – teenuse lõpp-punkti väljaantud LLM-ile.
2. **Python'i jooksutamiskeskkonda** – kus märkmikku saab täita.
3. **Kohalikke keskkonnamuutujaid** – _täida nüüd [SEADISTUS](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) sammud, et valmis saada_.

Märkmik sisaldab _algus_ harjutusi – kuid sind julgustatakse lisama ka oma _Markdown_ (kirjeldus) ja _Koodi_ (päringu taotluste) sektsioone, et proovida rohkem näiteid või ideid – ning arendada oma intuitsiooni päringu disainis.

## Illustreeritud juhend

Kas soovid saada suuremat ülevaadet sellest, mida see õppetükk katab, enne sukeldumist? Vaata seda illustreeritud juhendit, mis annab sulle aimu peamistest käsitletavatest teemadest ja võtmevõttest, mille üle mõelda igas neist. Õppetüki teejuht viib sind põhikontseptsioonide ja väljakutsete mõistmisest nende lahendamise juurde asjakohaste päringu insenertehnika tehnikate ja parimate tavadega. Pane tähele, et selle juhendi jaotis "Täpsemad tehnikad" viitab järgmises õppekava peatükis käsitletavale sisule.

![Illustreeritud juhend päringu insenertehnikasse](../../../translated_images/et/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Meie idufirma

Nüüd räägime, kuidas _see teema_ seostub meie idufirma missiooniga [tuua AI innovatsiooni haridusse](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Me tahame luua AI-jõulisi rakendusi _isikliku õppe_ toetamiseks – mõtleme siis, kuidas erinevad kasutajad meie rakendust kasutades päringuid "kujundavad":

- **Administraatorid** võivad paluda AI-l _analüüsida õppekava andmeid, et tuvastada kaetud teemade lüngad_. AI saab tulemusi kokku võtta või neid koodiga visualiseerida.
- **Õpetajad** võivad paluda AI-l _luua õppetunni plaan sihtrühma ja teema jaoks_. AI saab koostada personaalse plaani määratud vormingus.
- **Õpilased** võivad paluda AI-l _õpetada neid keerulises aines_. AI saab juhendada õpilasi nende tasemele kohandatud tundide, vihjete ja näidetega.

See on alles jäämäe tipp. Vaata [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – avatud lähtekoodiga päringute kogu, mida kureerivad hariduseksperdid – et saada laiem arusaam võimalustest! _Proovi mõnda neist päringutest liivakastis või OpenAI mänguväljal, et näha, mis juhtub!_

<!--
ÕPPETÜKI MALL:
See üksus peaks käsitlema põhikontseptsiooni #1.
Kinnista kontseptsiooni näidete ja viidetega.

KONTSPTSIOON #1:
Päringu insenertehnika.
Määra see ja selgita, miks see vajalik on.
-->

## Mis on päringu insenertehnika?

Alustasime seda õppetükki, määratledes **päringu insenertehnikat** kui protsessi päringutekstide (päringute) kujundamiseks ja optimeerimiseks, et pakkuda järjepidevaid ja kvaliteetseid vastuseid (täiendusi) antud rakenduse eesmärgi ja mudeli jaoks. Seda võib vaadelda ka kaheastmelise protsessina:

- _kujundamine_ algse päringu jaoks antud mudelis ja eesmärgil
- _täiustamine_ päringu iteratiivseks parandamiseks vastuse kvaliteedis

See on tingimata katse-eksituse protsess, mis nõuab kasutaja intuitsiooni ja pingutust optimaalse tulemuse saavutamiseks. Miks see siis oluline on? Selle küsimuse vastamiseks peame esmalt mõistma kolme mõistet:

- _Tokeniseerimine_ = kuidas mudel "näeb" päringut
- _Põhimudelitena LLM-id_ = kuidas põhimudel "töötab" päringuga
- _Juhendusega treenitud LLM-id_ = kuidas mudel näeb nüüd "ülesandeid"

### Tokeniseerimine

LLM näeb päringuid kui _tokenite jada_, kus erinevad mudelid (või sama mudeli versioonid) võivad sama päringu tokeniseerida erinevalt. Kuna LLM-e on treenitud tokenitel (mitte toortekstil), mõjutab päringute tokeniseerimine otseselt genereeritud vastuse kvaliteeti.

Intuitsiooni saamiseks tokeniseerimisest proovi näiteks tööriista [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) allpool toodud näidet. Kopeeri oma päring ja vaata, kuidas seda tokeniteks teisendatakse, pöörates tähelepanu tühikute ja punktuatsiooni käsitsemisele. Pane tähele, et see näide kasutab vanemat LLM-i (GPT-3) – nii et uuema mudeliga katsetamisel võib tulemus olla erinev.

![Tokeniseerimine](../../../translated_images/et/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Kontseptsioon: Põhimudelid

Kui päring on tokeniseeritud, siis ["Põhimudeli" (Base LLM)](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) põhifunktsiooniks on selle tokenite jadat prognoosida. Kuna LLM-e on treenitud ulatuslike tekstikogumitega, tunnevad nad hästi tokenite statistilisi seoseid ning saavad seda prognoosi õige kindlusega teha. Tuleb märkida, et nad ei mõista päringus kasutatud sõnade _tähendust_; nad näevad mustrit, mida saavad järgmise prognoosiga "täita". Nad saavad prognoosida jadat edasi, kuni kasutaja sekkumine või mõni eelnevalt määratletud tingimus selle lõpetab.

Kas soovid näha, kuidas päringul põhinev täiendamine töötab? Sisesta ülaltoodud päring [Microsoft Foundry mänguväljakule](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) vaikeseadetega. Süsteem on konfigureeritud võtma päringuid informatsiooni päringutena – nii et peaksid nägema vastust, mis vastab sellele kontekstile.

Ent mis siis, kui kasutaja tahaks näha midagi konkreetset, mis vastab mõnele kriteeriumile või ülesande eesmärgile? Siin tulevad mängu _juhendusega treenitud_ LLM-id.

![Põhimudeli LLM vestluse täiendamine](../../../translated_images/et/04-playground-chat-base.65b76fcfde0caa67.webp)

### Kontseptsioon: Juhendusega treenitud LLM-id

[Juhendusega treenitud LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) algab põhimudelist ja täiustab seda näidete või sisend/väljund paaride (näiteks mitme vooruga "sõnumite") abil, mis võivad sisaldada selgeid juhiseid – ning tehisintellekti vastus püüab neid juhiseid järgida.

See kasutab tehnikaid nagu inimtagasisidega tugevdamisõpe (RLHF), mis suudab mudelit õpetada _juhiseid järgima_ ja _tagasisidest õppima_, nii et see toodab vastuseid, mis sobivad paremini praktiliste rakenduste jaoks ja on kasutaja eesmärkide suhtes asjakohasemad.

Proovime järele – külasta eelmise päringu kontekstit vastav _süsteemi sõnum_ ja muuda see järgmise juhisega:

> _Kokkuvõtle sulle antud sisu teise klassi õpilase jaoks. Hoia tulemus ühe lõigu pikkune, 3–5 punktiga._

Näed, kuidas tulemus on nüüd häälestatud peegeldama soovitud eesmärki ja vormingut? Õpetaja saab selle vastuse nüüd otse oma tunnis slaididel kasutada.

![Juhendusega treenitud LLM vestluse täiendamine](../../../translated_images/et/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Miks meil on vaja päringu insenertehnikat?

Nüüd, kui teame, kuidas LLM-id päringuid töötlevad, räägime, _miks_ meil on päringu insenertehnika vaja. Vastus peitub selles, et praegustel LLM-idel on omajagu väljakutseid, mis muudavad _usaldusväärsete ja järjepidevate täienduste_ saamise keeruliseks ilma pingutusteta päringu koostamisel ja optimeerimisel. Näiteks:

1. **Mudeli vastused on stokastilised.** _Sama päring_ tõenäoliselt toodab erinevate mudelite või mudeli versioonidega erinevaid vastuseid. Ja see võib anda erinevaid tulemusi ka _sama mudeli_ kasutamisel erinevatel kordadel. _Päringu insenertehnika tehnikad aitavad meil neid varieerumisi minimaliseerida, pakkudes paremaid kontrollmehhanisme_.

1. **Mudelid võivad genereerida väljamõeldud vastuseid.** Mudelid on eelnevalt treenitud _suurtel, kuid piiratud_ andmestikel, mis tähendab, et neil puudub teadmine mõistetest väljaspool seda treeningut. Seetõttu võivad nad esitada täiendusi, mis on ebatäpsed, fantaasiarikkad või otseselt vastuolus tuntud faktidega. _Päringu insenertehnika tehnikad aitavad kasutajatel selliseid väljamõeldisi tuvastada ja leevendada, nt nõudes AI-lt allikaviiteid või põhjendusi_.

1. **Mudelite võimekus varieerub.** Uuemad mudelid või mudelipõlvkonnad omavad rikkalikumaid võimeid, kuid toovad kaasa unikaalseid eripärasid ning kulude ja keerukuse kompromisse. _Päringu insenertehnika aitab välja töötada parimaid tavasid ja töövooge, mis varjavad erinevusi ning kohanevad mudelispetsiifiliste nõuetega skaleeritavalt ja sujuvalt_.

Näeme seda praktikas OpenAI või Azure OpenAI mänguväljakul:

- Kasuta sama päringut erinevate LLM-de juurutuste puhul (nt OpenAI, Azure OpenAI, Hugging Face) – kas märkasid erinevusi?
- Kasuta sama päringut korduvalt sama LLM juurutuse juures (nt Azure OpenAI mänguväljak) – kuidas need varieerumised erinesid?

### Väljamõeldiste näide

Selles kursuses kasutame mõistet **"väljamõeldis"** viitamaks nähtusele, kus LLM-id mõnikord genereerivad faktuaalselt ebatäpset informatsiooni oma piirangute või muude tingimuste tõttu. Võid olla kuulnud ka mõistet _"hallutsinatsioonid"_ populaarsetes artiklites või teadustöös. Soovitame siiski kasutada _"väljamõeldis"_ terminit, et vältida käitumise antropomorfiseerimist, omistades masinajuhitud tulemusele inimlikke omadusi. See toetab ka [Vastutustundliku AI juhiseid](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) terminoloogia vaatenurgast, eemaldades termineid, mis mõnes kontekstis võivad olla solvavad või mittekaasavad.

Soovid tunnet saada, kuidas väljamõeldised toimivad? Mõtle päringule, mis palub AI-l genereerida sisu olemasolemata teema kohta (et veenduda, et seda ei leidu treeningandmestikus). Näiteks – proovisin järgmist päringut:

> **Päring:** genereeri õppetunni plaan Marsi sõja kohta aastast 2076.

Veebipäring näitas mulle, et leidub ilukirjanduslikke kirjeldusi (nt telesarjad või raamatud) Marsi sõdadest, kuid mitte aastast 2076. Tervislik mõistus ütleb, et aasta 2076 on _tulevikus_, seega ei saa see olla seotud päris sündmusega.


Mida siis juhtub, kui me kasutame seda prompti erinevate LLM-i teenusepakkujatega?

> **Vastus 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/et/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Vastus 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/et/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Vastus 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/et/04-fabrication-huggingchat.faf82a0a51278956.webp)

Nagu oodata oli, toodab iga mudel (või mudeli versioon) veidi erinevaid vastuseid tänu juhuslikule käitumisele ja mudeli võimekuse erinevustele. Näiteks üks mudel sihib 8. klassi taset, samas kui teine arvestab keskkooliõpilasega. Kuid kõik kolm mudelit lõid vastuseid, mis võivad veenda teadmatus kasutajat, et sündmus oli tõeline.

Promptide insenertehnika meetodid nagu _metaprompting_ ja _temperatuuri seadistamine_ võivad mõningal määral vähendada mudeli väljamõeldisi. Uued promptide insenertehnika _arhitektuurid_ integreerivad sujuvalt uusi tööriistu ja tehnikaid prompti voogu, et neid mõjusid vähendada või leevendada.

## Juhtumiuuring: GitHub Copilot

Lõpetame selle osa, saades aimu, kuidas promptide insenertehnikat kasutatakse reaalses maailmas ühe juhtumiuuringu näitel: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot on sinu "tehisintellekti paarisprogrammeeri­ja" - see teisendab tekstikäsud kooditäidisteks ja on integreeritud sinu arenduskeskkonda (nt Visual Studio Code) sujuva kasutajakogemuse jaoks. Allolevates blogide seerias on dokumenteeritud, et varasem versioon põhines OpenAI Codex mudelil - insenerid mõistsid kiiresti vajadust mudelit täpsemalt häälestada ja arendada paremaid promptide insenertehnikaid koodikvaliteedi parandamiseks. Juulis nad [esitlesid täiustatud tehisintellek­ti mudelit, mis läheb Codex-ist kaugemale](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) veelgi kiiremaks soovitamiseks.

Loe postitusi järjekorras, et jälgida nende õppeteekonda.

- **Mai 2023** | [GitHub Copilot paraneb sinu koodi mõistmisel](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mai 2023** | [GitHub sees: Töötades LLM-idega GitHub Copiloti taga](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Juuni 2023** | [Kuidas kirjutada paremaid handiseid GitHub Copilotile](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Juuli 2023** | [.. GitHub Copilot läheb Codex-ist kaugemale täiustatud tehisintellekti mudeliga](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Juuli 2023** | [Arendaja juhend promptide insenertehnikaks ja LLM-ideks](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **September 2023** | [Kuidas ehitada ettevõtte LLM rakendust: õppetunnid GitHub Copilotilt](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Võid sirvida ka nende [Inseneriblogi](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst), kus on postitusi nagu [see siin](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), mis näitab, kuidas neid mudeleid ja tehnikaid rakendatakse reaalse maailma lahenduste loomiseks.

---

<!--
ÕPPEPLAANIMALL:
See osa peaks käsitlema põhikontsepti #2.
Kinnita kontseptsiooni näidete ja viidetega.

KONTSEPT #2:
Prompti kujundamine.
Illustreeritud näidetega.
-->

## Promptide ülesehitus

Oleme näinud, miks promptide insenertehnika on oluline – nüüd mõistame, kuidas promptid on _ehitatud_, et saaksime hinnata erinevaid tehnikaid tõhusamaks promptide kujundamiseks.

### Põhiprompt

Alustame põhipromptist: tekstisisend, mis saadetakse mudelile ilma muu kontekstita. Näiteks, kui saadame USA hümni esimesed sõnad OpenAI [Completion API-le](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), siis see koheselt _täidab_ vastuse järgmiste ridadega, illustreerides põhilist ennustuskäitumist.

| Prompt (sisend)   | Täidise (väljundi)                                                                                                                          |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Tundub, et alustad lauluga "The Star-Spangled Banner", USA riigihümn. Täis­laulusõnad on ...                                                |

### Kompleksne prompt

Lisame nüüd konteksti ja juhised sellele põhipromptile. [Chat Completion API](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) võimaldab meil konstrueerida keeruka prompti _sõnumite_ kogumina, milles on:

- Sissetulevad/väljaminevad paarid, mis peegeldavad _kasutaja_ sisestust ja _abilise_ vastust.
- Süsteemisõnum, mis seab abilise käitumise või isiksuse konteksti.

Nüüd on taotlus alljärgnevas vormis, kus _tokeniseerimine_ haarab efektiivselt relevantset teavet kontekstist ja vestlusest. Süsteemse konteksti muutmine võib värskete vastuste kvaliteeti mõjutada sama oluliselt kui kasutaja sisendid.

```python
response = client.responses.create(
    model="gpt-5-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Juhenduspõhine prompt

Ülaltoodud näidetes oli kasutaja prompt lihtne tekstipäring, mida võidi tõlgendada infotaotluseks. _Juhenduspõhiste_ promptide puhul saame seda teksti kasutada ülesande täpsemaks määratlemiseks, andes tehisintellektile paremaid juhiseid. Näide:

| Prompt (sisend)                                                                                                                                                                                                                         | Täidis (väljund)                                                                                                        | Juhendustüüp       |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Kirjuta Ameerika kodusõja kirjeldus                                                                                                                                                                                                   | _tagastas lihtsa lõigu_                                                                                                  | Lihtne              |
| Kirjuta Ameerika kodusõja kirjeldus. Too välja tähtsamad kuupäevad ja sündmused ning kirjuta nende tähtsusest                                                                                                                        | _tagastas lõigu koos nimekirjaga tähtsatest kuupäevadest ja kirjeldustest_                                               | Komplekssed          |
| Kirjuta Ameerika kodusõja kirjeldus 1 lõigus. Too 3 peamist võtmekuupäeva koos tähtsusega. Too veel 3 peamist ajaloolist tegelast ja nende panust. Tagasta väljund JSON-failina            | _tagastab ulatuslikumaid andmeid tekstiboksis, vormindatuna JSON-ina, mida saad kopeerida ja vajadusel valideerida_         | Komplekssed. Vormindatud. |

## Põhisisu

Ülaltoodud näidetes oli prompt endiselt suhteliselt avatud, võimaldades LLM-il otsustada, milline osa selle eelõppemehhanismist on relevantne. _Põhisisu_ disainimall jagab sisendteksti kaheks osaks:

- juhend (tegevus)
- asjakohane sisu (mis mõjutab tegevust)

Näide, kus juhis on "kokkuvõtke see 2 lauses".

| Prompt (sisend)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Täidis (väljund)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter on päikesest viies planeet ja suurim Päikesesüsteemis. See on gaasihiiglane, mille mass on tuhandik Päikese massist, kuid kaks ja pool korda suurem kui kõik teised planeedid kokku. Jupiter on üks eredamaid objekti, mida palja silmaga öötaevas näha saab, ja see on tuntud iidsetest tsivilisatsioonidest juba enne ajaloo algust. Selle nimi tuleb Rooma jumala Jupiteri järgi.[19] Maalt vaadates võib Jupiter olla piisavalt ere, et peegeldunud valgus tekitab nähtavaid varje,[20] ja keskmiselt on see öötaeva kolmas eredaim looduslik objekt pärast Kuud ja Veenust. <br/> **Kokkuvõtke see 2 lühikeses lauses** | Jupiter, päikesest viies planeet, on Päikesesüsteemi suurim ja tuntud kui üks eredamaid taevalaotusel nähtavaid objekte. Nime sai see Rooma jumala Jupiteri järgi ja on gaasihiiglane, mille mass on kaks ja pool korda suurem kui kõigi teiste planeetideühikute kogum. |

Põhisisu segmenti saab kasutada mitmel viisil, et anda tõhusamaid juhiseid:

- **Näited** - mudelile ei öelda otseselt, mida teha, vaid antakse näited, mida teha ja lastakse mudelil mustrit tuletada.
- **Vihjed** - juhisele järgneb "vihje", mis suunab mudelit relevantsemate vastusteni.
- **Mustrid** - korduvkasutatavad 'retseptid' promptide jaoks koos kohatäiteks muutuja-dega, mida saab kohandada konkreetseteks juhtudeks.

Vaatame neid teemasid praktikas.

### Näidete kasutamine

See lähenemine kasutab põhisisu, et "toita mudelit" soovitud väljundi näidetega antud juhise põhjal ning võimaldab mudelil tuletada mustrikäitumise. Näidete arvu põhjal võib olla null-korral promptimine, ühe-korral promptimine, mõne-korral promptimine jne.

Prompt koosneb nüüd kolmest komponendist:

- Ülesande kirjeldus
- Mõned näited soovitud väljundi kohta
- Uue näite algus (mis muutub kaudseks ülesande kirjelduseks)

| Õppimise tüüp | Prompt (sisend)                                                                                                                                        | Täidis (väljund)          |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------- |
| Null-korral   | "The Sun is Shining". Tõlgi hispaania keelde                                                                                                         | "El Sol está brillando".   |
| Ühe-korral    | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso".|
| Mõne-korral   | Mängija jooksis baasidel => Pesapall <br/> Mängija lõi ässa => Tennis <br/> Mängija lõi kuue => Kriket <br/> Mängija tegi slam-dunki =>                 | Korvpall                  |
|               |                                                                                                                                                       |                           |

Märka, kuidas me pidime null-korral promptimisel andma otsese juhise ("Tõlgi hispaania keelde"), kuid ühe-korral promptimisel tuletatakse see juba ise. Mõne-korrase näide näitab, kuidas rohkemate näidete lisamine võimaldab mudelil teha täpsemaid järeldusi ilma täiendavate juhisteta.

### Prompti vihjed

Teine tehnika põhisisu kasutamisel on vihjete andmine näidete asemel. Sel juhul anname mudelile suunise, alustades vastava vormingu näitega. Mudel siis "võtab vihje vastu" ja jätkab antud stiilis.

| Vihjete arv   | Prompt (sisend)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Täidis (väljund)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter on päikesest viies planeet ja suurim Päikesesüsteemis. See on gaasihiiglane, mille mass on tuhandik Päikese massist, kuid kaks ja pool korda suurem kui kõik teised planeedid kokku. Jupiter on üks eredamaid objekti, mida palja silmaga öötaevas näha saab, ja see on tuntud iidsetest tsivilisatsioonidest juba enne ajaloo algust. <br/>**Kokkuvõtke see**                                       | Jupiter on suurim planeet meie Päikesesüsteemis ja päikesest viies planeet. See on gaasihiiglane, mille mass on 1/1000 Päikese massist, kuid raskem kui kõik teised planeedid kokku. Iidsetest tsivilisatsioonidest on Jupiter teada olnud kaua ja see on öötaevas kergesti nähtav.. |
| 1              | Jupiter on päikesest viies planeet ja suurim Päikesesüsteemis. See on gaasihiiglane, mille mass on tuhandik Päikese massist, kuid kaks ja pool korda suurem kui kõik teised planeedid kokku. Jupiter on üks eredamaid objekti, mida palja silmaga öötaevas näha saab, ja see on tuntud iidsetest tsivilisatsioonidest juba enne ajaloo algust. <br/>**Kokkuvõtke see** <br/> Mida me õppisime, on see, et Jupiter | on päikesest viies planeet ja suurim Päikesesüsteemis. See on gaasihiiglane, mille mass on tuhandik Päikese massist, kuid kaks ja pool korda suurem kui kõik teised planeedid kokku. See on palja silmaga hõlpsasti nähtav ja on tuntud iidsetest aegadest.                       |

| 2              | Jupiter on Päikesest viies planeet ja Päikesesüsteemi suurim. See on gaasihiid, mille mass on üks tuhandik Päikese massist, kuid kaks ja pool korda suurem kui kõigi teiste Päikesesüsteemi planeetide masside summa. Jupiter on üks eredamaid palja silmaga öötaevas nähtavaid objekte ning on olnud tuntud iidsetele tsivilisatsioonidele juba enne ajaloo kirjalikku algust. <br/>**Kokkuvõte** <br/> Kolm peamist fakti, mida õppisime:         | 1. Jupiter on Päikesest viies planeet ja Päikesesüsteemi suurim. <br/> 2. See on gaasihiid, mille mass on üks tuhandik Päikese massist...<br/> 3. Jupiter on olnud palja silmaga nähtav juba antiikajast alates ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Päringu mallid

Päringu mall on _eelnevalt määratletud päringu retsept_, mida saab salvestada ja vajadusel uuesti kasutada, et juhendada sujuvamaid kasutajakogemusi ulatuslikult. Lihtsamas vormis on see lihtsalt päringunäidete kogum nagu [see OpenAI näide](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), mis pakub nii interaktiivseid päringu komponente (kasutaja ja süsteemi sõnumid) kui ka API-põhise päringu formaati - taaskasutuse toetamiseks.

Keerulisemas vormis nagu [see näide LangChainist](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) sisaldab see _kohatäiteid_, mida saab asendada andmetega mitmest allikast (kasutaja sisend, süsteemi kontekst, välised andmeallikad jne) dünaamilise päringu loomiseks. See võimaldab meil koostada taaskasutatavate päringute kogu, mida saab programmi abil kasutada järjepidevate kasutajakogemuste loomiseks ulatuslikult.

Lõpuks seisneb mallide tegelik väärtus võimes luua ja avaldada _päringukogusid_ vertikaalsete rakendusvaldkondade jaoks - kus päringu mall on nüüd _optimeeritud_, et peegeldada rakenduspõhist konteksti või näiteid, mis muudavad vastused sihtrühmale asjakohasemaks ja täpsemaks. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) hoidla on suurepärane näide sellest lähenemisest, koondades haridusvaldkonna päringute kogu, mille rõhk on olulistel eesmärkidel nagu tunniplaani koostamine, õppekava disain, õpilaste juhendamine jms.

## Toetav sisu

Kui me mõtleme päringu koostamist kui juhist (ülesande) ja sihtmärki (põhisisu), siis _teisene sisu_ on nagu lisakontekst, mida me anname, et **mõnel viisil väljundit mõjutada**. See võib olla häälestusparameetrid, vormindusjuhised, teema taksonoomiad jne, mis aitavad mudelil kohandada vastust soovitud kasutajaeesmärkide või ootustega.

Näiteks: kui meil on kursusekataloog, mis sisaldab põhjalikku metainfot (nimi, kirjeldus, tase, metatähed, õppejõud jne) kõigi õppekava välistingimustes olevate kursuste kohta:

- me saame määratleda juhise "kokkuvõtke sügissemestri 2023 kursuste kataloog"
- me saame kasutada peamist sisu, et anda mõned soovitud väljundi näited
- me saame kasutada teisest sisust, et määratleda 5 enim huvi pakkuvat "märksõna"

Nüüd saab mudel pakkuda kokkuvõtet vormingus, mida näitavad paar eeskuju - kuid kui tulemuses on mitu märksõna, saab ta anda prioriteedi teisest sisust määratud viiele märksõnale.

---

<!--
ÕPPEPLANEERIMISE MALL:
See üksus peaks hõlmama põhikontseptsiooni #1.
Tugevdage kontseptsiooni näidete ja viidetega.

KONTSEPTSIOON #3:
Päringute inseneritehnika tehnikad.
Millised on mõned põhilised tehnikad päringute inseneritehnikas?
Illustreerige seda mõnede harjutustega.
-->

## Parimad tavad päringu koostamisel

Nüüd, kui me teame, kuidas päringuid saab _koostada_, võime hakata mõtlema, kuidas neid _kujundada_, võttes arvesse parimaid tavasid. Võime seda käsitleda kahes osas - õige _mõtteviisi_ omamine ja sobivate _tehnikate_ rakendamine.

### Päringu inseneritehnika mõtteviis

Päringu inseneritehnika on katsumus- ja eksitusprotsess, seega pidage meeles kolme laiemat juhist:

1. **Valdkonna mõistmine on oluline.** Vastuse täpsus ja asjakohasus sõltub _valdkonnast_, milles rakendus või kasutaja tegutseb. Kasutage oma intuitsiooni ja valdkonnapädevust, et _kohandada tehnikaid_ veelgi. Näiteks määrake süsteemi päringutes _valdkonnapõhised isiksused_ või kasutage kasutaja päringutes _valdkonnapõhiseid malle_. Lisage teisene sisu, mis peegeldab valdkonnapõhist konteksti, või kasutage _valdkonnapõhiseid viiteid ja näiteid_, et juhendada mudelit tuttavate kasutusmusterite suunas.

2. **Mudelipõhine mõistmine on oluline.** Teame, et mudelid on oma olemuselt stokastilised. Kuid mudelite rakendused võivad erineda seoses kasutatava treeningandmestikuga (eelõppe teadmised), nende pakutavate võimalustega (nt API või SDK kaudu) ja optimeeritud sisutüübiga (nt kood, pildid või tekst). Mõistke enda kasutatava mudeli tugevusi ja nõrkusi ning kasutage seda teadmist, et _prioriseerida ülesandeid_ või ehitada _kohandatud malle_, mis on optimeeritud mudeli võimalustele.

3. **Iteratsioon ja valideerimine on olulised.** Mudelid arenevad kiiresti ja nii ka päringuinseneritehnika tehnikad. Valdkonnaeksperdina võite omada lisakonteksti või kriteeriume _oma_ spetsiifilise rakenduse jaoks, mis ei pruugi kehtida laiemale kogukonnale. Kasutage päringu inseneritehnika tööriistu ja tehnikaid, et "kiirendada" päringu koostamist, seejärel korduge ja valideerige tulemusi oma intuitsiooni ja valdkonnapädevuse abil. Salvestage oma tähelepanekud ja looge **teadmistebaas** (nt päringukogud), mida teised saavad kasutada uue lähtepunktina kiiremateks iteratsioonideks tulevikus.

## Parimad protseduurid

Vaatame nüüd levinud parimaid tavasid, mida soovitavad [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) ja [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) praktikandid.

| Mida                             | Miks                                                                                                                                                                                                                                              |
| :-------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hinnake uusimaid mudeleid.      | Uued mudelisukupõlved tõenäoliselt pakuvad paremaid omadusi ja kvaliteeti - kuid võivad tuua kaasa ka kõrgemaid kulusid. Hinnake nende mõju ja seejärel tehke üleminekuga seotud otsused.                                                            |
| Eraldage juhised ja kontekst     | Kontrollige, kas teie mudel/teenusepakkuja määratleb _piirajad_, mis eristavad juhiseid, põhisisu ja teisest sisu selgemalt. See aitab mudelitel tähemärkidele anda täpsemaid kaalu.                                                             |
| Olge spetsiifiline ja selge      | Andke rohkem detaile soovitud konteksti, tulemuse, pikkuse, formaadi, stiili jms kohta. See parandab nii vastuste kvaliteeti kui järjepidevust. Salvestage retseptid taaskasutatavates mallides.                                                     |
| Olge kirjeldav, kasutage näiteid | Mudelid võivad reageerida paremini "näita ja räägi" lähenemise korral. Alustage `zero-shot` meetodiga, kus annate juhise (kuid mitte näiteid), seejärel proovige `few-shot` meetodit täpsustamiseks, pakkudes paar näidet soovitud väljundist. Kasutage võrdlusi. |
| Kasutage vihjeid vastuste alustamiseks | Suunake mudelit soovitud tulemuse poole, andes hüüdsõnade või fraaside algused, mida ta saab vastuse alustamiseks kasutada.                                                                                                                       |
| Korrake vajalikul juhul         | Mõnikord peate mudelile korduvalt juhiseid andma. Lisage juhised nii enne kui pärast põhisisu, kasutage juhist ja vihjet jms. Korduge ja valideerige, et näha, mis toimib.                                                                          |
| Järjestus loeb                  | Informatsiooni esitamise järjekord mudelile võib mõjutada väljundit, isegi õppekordustes tänu värske mälu eelistusele. Proovige erinevaid variante, et näha, mis töötab kõige paremini.                                                            |
| Andke mudelile "väljatulek"    | Paku mudelile _varuvastus_, mida ta saab anda, kui ei suuda mingil põhjusel ülesannet täita. See võib vähendada vale- või väljamõeldud vastuste tekkimise tõenäosust.                                                                              |
|                                  |                                                                                                                                                                                                                                                   |

Nagu iga parima tava puhul, pidage meeles, et _teie kogemus võib varieeruda_ mudeli, ülesande ja valdkonna järgi. Kasutage neid lähtepunktina ja iteratsioonideks, et leida enda jaoks parim. Hinnake pidevalt oma päringu inseneritehnika protsessi, kui uued mudelid ja tööriistad muutuvad kättesaadavaks, keskendudes protsessi skaleeritavusele ja vastuste kvaliteedile.

<!--
ÕPPEPLANEERIMISE MALL:
See üksus peaks pakkuma koodiülesannet, kui see on asjakohane

ÜLESANNE:
Link Jupyter notebook'ile, mis sisaldab ainult koodi kommentaare juhistes (koodilõigud on tühjad).

LAHENDUS:
Link koopia sellele notebookile, kus päringud on täidetud ja käivitatud, näidates ühe näite lahendust.
-->

## Ülesanne

Palju õnne! Sa jõudsid tunni lõpuni! On aeg mõnda neist kontseptsioonidest ja tehnikatest proovile panna tõeliste näidetega!

Meie ülesande jaoks kasutame Jupyter notebook'i koos harjutustega, mida saate interaktiivselt täita. Samuti saate notebooki laiendada oma Markdown ja koodirakkudega, et iseseisvalt ideid ja tehnikaid uurida.

### Alustamiseks tehke fork hoidlast, seejärel

- (Soovituslik) Käivitage GitHub Codespaces
- (Või) Kloonige hoidla oma kohalikku seadmesse ning kasutage seda Docker Desktopiga
- (Või) Avage notebook oma eelistatud notebook-tarkvara keskkonnas.

### Seejärel seadistage oma keskkonnamuutujad

- Kopeerige hoidla juurkaustas olev `.env.copy` fail `.env` nimega ja täitke `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` ja `AZURE_OPENAI_DEPLOYMENT` väärtused. Tulge tagasi [Learning Sandbox jaotisesse](#õppimise-liivakast), et õppida, kuidas seda teha.

### Seejärel avage Jupyter notebook

- Valige töötlusmootori kernel. Kui kasutate võimalusi 1 või 2, valige lihtsalt dev konteineri vaikimisi pakutav Python 3.10.x kernel.

Olete valmis harjutusi läbi viima. Pange tähele, et siin pole _õigeid ega valesid_ vastuseid - see on katsetamine ja intuitsiooni arendamine selle kohta, mis konkreetsele mudelile ja rakendusvaldkonnale sobib.

_Seetõttu pole selles tunnis koodilahenduse lõike. Selle asemel on notebookis markdown-rakud pealkirjaga "Minu lahendus:", mis näevad ühe näidisväljundi viitena._

 <!--
ÕPPEPLANEERIMISE MALL:
Lõpetage jaotis kokkuvõtte ning iseseisva õppimise ressurssidega.
-->

## Teadmiste kontroll

Milline järgmistest on hea päring, mis järgib mõistlikke parimaid tavasid?

1. Näita mulle pilti punasest autost
2. Näita mulle pilti punasest Volvost XC90 mudelist, mis on parkis kalju ääres päikeseloojangul
3. Näita mulle pilti punasest Volvo XC90 mudelist

Vastus: 2 on parim, kuna see annab üksikasju "mida" ja läheb spetsiifikasse (mitte lihtsalt üks auto, vaid konkreetne margi ja mudeli järgi) ning kirjeldab ka kogu stseeni. 3 on järgmine parim, kuna sisaldab samuti palju kirjeldust.

## 🚀 Väljakutse

Proovi kasutada "vihje" tehnikat päringuga: Täienda lauset "Näita mulle pilti punasest autost margiga Volvo ja ". Mida see vastab, ja kuidas saaksid seda parandada?

## Väga hea! Jätka õppimist

Kas soovid õppida rohkem erinevate päringu inseneritehnika kontseptsioonide kohta? Mine [edaspidise õppimise lehele](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et leida selle teema kohta teisi suurepäraseid ressursse.

Mine 5. õppetundi, kus vaatleme [edasijõudnud päringu tehnikat](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->