# Käsuplaneerimise põhialused

[![Käsuplaneerimise põhialused](../../../translated_images/et/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Sissejuhatus
See moodul käsitleb olulisi mõisteid ja tehnikaid tõhusate käskude loomiseks generatiivsetes tehisintellekti mudelites. Viis, kuidas kirjutate käsu LLM-ile, on samuti oluline. Hoolikalt koostatud käsk võib saavutada parema vastuse kvaliteedi. Kuid mida täpselt tähendavad sellised mõisted nagu _käsk_ ja _käsuplaneerimine_? Ja kuidas ma saan parendada käsu _sisendit_, mida ma LLM-ile saadan? Neile küsimustele püüame vastuseid leida käesolevas ja järgmisel peatükil.

_Generatiivne tehisintellekt_ suudab luua uut sisu (nt teksti, pilte, heli, koodi jne) vastuseks kasutaja päringutele. Selle saavutamiseks kasutatakse _suurekeelseid mudeleid_ nagu OpenAI GPT ("Generative Pre-trained Transformer") seeria, mis on koolitatud loomuliku keele ja koodi kasutamiseks.

Kasutajad saavad nüüd nendega suhelda tuttavate paradigmade kaudu, näiteks vestluse kaudu, ilma tehniliste teadmisteta või koolituseta. Mudelid on _käskudel põhinevad_ – kasutajad saadavad tekstisisendi (käsu) ja saavad vastu tehisintellekti vastuse (täienduse). Nad saavad seejärel "vestelda tehisintellektiga" iteratiivselt, mitmevoorulistes vestlustes, täiustades oma käsku, kuni vastus vastab nende ootustele.

"Käsud" muutuvad nüüd generatiivsete tehisintellekti rakenduste peamiseks _programmeermisliideseks_, mis annab mudelitele juhised ja mõjutab tagastatavate vastuste kvaliteeti. "Käsuplaneerimine" on kiiresti kasvav uurimisvaldkond, mis keskendub _käskude kavandamisele ja optimeerimisele_, et pakkuda järjepidevaid ja kvaliteetseid vastuseid suurel hulgal.

## Õpieesmärgid

Selles õppetükis saame teada, mis on käsuplaneerimine, miks see on oluline ja kuidas saame luua tõhusamaid käske konkreetse mudeli ja rakenduse eesmärgi jaoks. Mõistame põhimõisteid ja parimaid tavasid käsuplaneerimiseks ning tutvume interaktiivse Jupyteri märkmikute "liivakasti" keskkonnaga, kus saame neid mõisteid rakendada reaalses näidetes.

Selle õppetüki lõpuks suudame:

1. Selgitada, mis on käsuplaneerimine ja miks see oluline on.
2. Kirjeldada käsu komponente ja nende kasutust.
3. Õppida käsuplaneerimise parimaid tavasid ja tehnikaid.
4. Rakendada õpitud tehnikaid reaalsele näitele, kasutades OpenAI lõpp-punkti.

## Olulised terminid

Käsuplaneerimine: Tehisintellekti mudelite suunamisel soovitud tulemuste saavutamiseks sisendite kavandamise ja täpsustamise praktika.
Tokeniseerimine: Teksti teisendamine väiksemateks üksusteks ehk tokeniteks, mida mudel suudab mõista ja töödelda.
Juhenditega kohandatud LLM-id: Suurekeelsed mudelid, mis on edasiõpetatud konkreetsete juhendite abil, et parandada vastuste täpsust ja asjakohasust.

## Õppimise liivakast

Käsuplaneerimine on praegu pigem kunst kui teadus. Intuitsiooni parandamiseks on parim harjutada ja kasutada katse-eksituse lähenemist, mis ühendab rakendusvaldkonna teadmised soovitatud tehnikate ja mudelispetsiifiliste optimeerimistega.

Selle õppetükiga kaasnev Jupyteri märkmik pakub _liivakasti_ keskkonda, kus saad proovida õpitut - kas õppetüki jooksul või koodi väljakutse raames lõpus. Harjutuste täitmiseks vajad:

1. **Azure OpenAI API võtit** – teenuse lõpp-punkti juurdepääsuks kasutusel olevale LLM-ile.
2. **Python käitusaega** – märkmiku täitmiseks.
3. **Kohalikke keskkonnamuutujaid** – _täida nüüd [SEADISTAMISE](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) sammud, et valmis saada_.

Märkmikus on kaasas _algus_ harjutused – kuid sind julgustatakse lisama omaenda _Markdown_ (kirjeldus) ja _Code_ (käsupäringud) sektsioone, et proovida rohkem näiteid või ideid ning ehitada üles oma intuitsioon käsu kujundamisel.

## Illustratiivne juhend

Kas soovid enne süvenemist saada ülevaadet sellest, mida see õppetükk hõlmab? Vaata seda illustratiivset juhendit, mis annab sulle ülevaate peamistest käsitletavatest teemadest ja võtmeideedest, millele mõelda. Õppetüki teejuht viib sind läbi põhimõistete ja väljakutsete mõistmise kuni asjakohaste käsuplaneerimise tehnikate ja parimate tavade rakendamiseni. Pane tähele, et "Täpsemad tehnikad" osa selles juhendis viitab järgmisel peatükil käsitletavatele teemadele.

![Illustratiivne juhend käsuplaneerimisele](../../../translated_images/et/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Meie idufirma

Räägime nüüd, kuidas _see teema_ on seotud meie idufirma missiooniga [tuua haridusse tehisintellekti uuenduslikkus](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Soovime luua tehisintellektil põhinevaid rakendusi _isiklikuks õppimiseks_ – seega mõtleme, kuidas meie rakenduse erinevad kasutajad võiksid "kujundada" käske:

- **Administraatorid** võivad paluda tehisintellektil _analüüsida õppekava andmeid, et tuvastada lünki_. Tehisintellekt saab tulemusi kokku võtta või visualiseerida koodi abil.
- **Õpetajad** võivad paluda tehisintellektil _luua õppetund sihtrühmale ja teemal_. Tehisintellekt saab koostada isikupärastatud plaani kindlas formaadis.
- **Õpilased** võivad paluda tehisintellektil _õpetada neid keerulises aines_. Tehisintellekt juhendab õpilasi nüüd õppetundide, vihjete ja näidete abil, mis on kohandatud nende tasemele.

See on alles jäämäe tipp. Uuri [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – haridusekspertide kureeritud avatud lähtekoodiga käsude kogu – et saada laiem arusaam võimalustest! _Proovi neid käske liivakastis või OpenAI mänguväljakul, et näha, mis juhtub!_

<!--
ÕPPETEKSTI MALL:
See üksus peaks hõlmama põhimõistet nr 1.
Tuua mõistele lisatugevus näidete ja viidetega.

PÕHIMÕISTE #1:
Käsuplaneerimine.
Defineerida ning selgitada, miks seda vaja on.
-->

## Mis on käsuplaneerimine?

Alustasime seda õppetundi selle defineerimisega kui **käsuplaneerimist**, mis on tekstisisendite (käskude) _kujundamise ja optimeerimise_ protsess, et tagada järjepidevad ja kvaliteetsed vastused (täiendused) konkreetse rakenduse eesmärgi ja mudeli jaoks. Seda võib vaadelda kui kahesammulist protsessi:

- algse käsu _kujundamine_ konkreetse mudeli ja eesmärgi jaoks
- käsu _täpsustamine_ iteratiivselt vastuse kvaliteedi parandamiseks

See on tingimata katse-eksituse protsess, mis nõuab kasutaja intuitsiooni ja pingutust optimaalse tulemuse saavutamiseks. Miks see siis oluline on? Sellele vastamiseks peame esmalt mõistma kolme mõistet:

- _Tokeniseerimine_ = kuidas mudel käsu "näeb"
- _Alus LLM-id_ = kuidas baas-mudel käsu "töötab"
- _Juhenditega kohandatud LLM-id_ = kuidas mudel nüüd näeb "ülesandeid"

### Tokeniseerimine

LLM näeb käske kui _tokenite jada_, kus erinevad mudelid (või mudeli versioonid) võivad sama käsku tokeniseerida eri viisidel. Kuna LLM-id on koolitatud tokenite peale (mitte tooteksti peale), mõjutab käsu tokeniseerimine otseselt loodava vastuse kvaliteeti.

Tokeniseerimise paremaks mõistmiseks proovi tööriistu nagu [OpenAI tokeniseerija](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst), mis on näidatud allpool. Kleepi oma käsk sisse ja vaata, kuidas see tokeniteks teisendatakse, pöörates tähelepanu tühikute ja kirjavahemärkide töötlemisele. Pane tähele, et näide kasutab vanemat LLM-i (GPT-3) – uuemate mudelitega katsetamisel võivad tulemused erineda.

![Tokeniseerimine](../../../translated_images/et/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Mõiste: Baasmudelid

Kui käsk on tokeniseeritud, on "Alus LLM"-i (või baas-mudeli) peamine ülesanne ennustada selle jada järgmist tokenit. Kuna LLM-id on koolitatud tohutute tekstikogumitega, on neil hea statistiline tunnetus tokenite vaheliste suhete kohta ning nad saavad selle ennustuse usaldusväärselt teha. Pane tähele, et nad ei mõista käskudes või tokenites olevate sõnade _tähendust_; nad näevad mustrit, mida nad võivad oma järgmise ennustusega "täita". Ennustamine jätkub, kuni kasutaja sekkub või täidetakse eelnevalt määratletud tingimus.

Kas soovid näha, kuidas käsupõhine täiendamine töötab? Sisesta ülaltoodud käsk [Microsoft Foundry mänguväljakule](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) vaikeväärtustega. Süsteem käsitleb käske teabe päringutena, seega peaksid saama vastuse, mis sobib konteksti.

Aga mis siis, kui kasutaja soovib midagi konkreetset, mis vastaks mõnele kriteeriumile või ülesande eesmärgile? Siin tulevad mängu _juhenditega kohandatud_ LLM-id.

![Alus LLM vestluse täiendamine](../../../translated_images/et/04-playground-chat-base.65b76fcfde0caa67.webp)

### Mõiste: Juhenditega kohandatud LLM-id

[Juhenditega kohandatud LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) algab baas-mudelilt, millele tehakse täiendõpe näidete või sisend/väljund paaridega (nt mitme vooru "sõnumid"), mis sisaldavad selgeid juhiseid – ning tehisintellekti vastus püüab neid juhiseid järgida.

Selleks kasutatakse meetodeid nagu inimtagasisidel põhinev tugevdamisõpe (RLHF), mis koolitab mudelit _juhiseid järgima_ ja _tagasisidest õppima_, et produktsioon vastaks paremini praktilistele rakendustele ja kasutaja eesmärkidele.

Proovime seda – muuda ülaltoodud käsus _süsteemisõnum_ järgmiste juhistega kontekstiks:

> _Kokkuvõtke antud sisu teise klassi õpilase jaoks. Hoidke tulemus ühe lõiguna koos 3–5 täppidega._

Näed, kuidas tulemus nüüd on häälestatud vastama soovitud eesmärgile ja vormingule? Õpetaja saab seda vastust otse kasutada oma esitlustes selle klassi jaoks.

![Juhenditega kohandatud LLM vestluse täiendamine](../../../translated_images/et/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Miks me vajame käsuplaneerimist?

Nüüd, kui teame, kuidas LLM-id käske töötlevad, räägime, _miks_ me vajame käsuplaneerimist. Vastus peitub selles, et praegused LLM-id tekitavad mitmeid väljakutseid, mis muudavad _usaldusväärsete ja järjepidevate vastuste_ saavutamise keerulisemaks ilma pingutusteta käsu koostamisel ja optimeerimisel. Näiteks:

1. **Mudelivastused on stokhastilised.** _Sama käsk_ võib erinevate mudelite või mudeliversioonide puhul anda erinevaid vastuseid. Ja isegi _samaga mudeliga_ võivad erinevatel kordadel tulemused erineda. _Käsuplaneerimise tehnikad aitavad neid varieeruvusi vähendada, pakkudes paremaid piiranguid_.

1. **Mudelid võivad vastuseid väljamõelda.** Mudelid on koolitatud _ülisuurele, kuid piiratud_ andmestikule, mistõttu neil puudub teadmine väljaspool koolitusandmestikku olevaid kontseptsioone. Selle tulemusena võivad nad toodada täiendusi, mis on ebatäpsed, väljamõeldud või mõneti vastuolus teadaolevate faktidega. _Käsuplaneerimise tehnikad aitavad kasutajatel selliseid väljamõeldisi tuvastada ja neile vastu astuda, nt paludes tsiteeringuid või põhjendusi_.

1. **Mudelite võimekus varieerub.** Uuemad mudelid või mudelite põlvkonnad pakuvad rohkem võimalusi, kuid toovad kaasa ka unikaalseid eripärasid ning kulude ja keerukuse kompromisse. _Käsuplaneerimine aitab meil arendada parimaid tavasid ja töövooge, mis abstraktiseerivad erinevusi ning kohanduvad mudelispetsiifiliste nõuetega skaleeritaval ja sujuval viisil_.

Vaatame seda praktikas OpenAI või Azure OpenAI mänguväljakul:

- Kasuta sama käsu erinevate LLM-i juurutustega (nt OpenAI, Azure OpenAI, Hugging Face) – kas märkad erinevusi?
- Kasuta sama käsku korduvalt ühe _jaama_ LLM puhul (nt Azure OpenAI mänguväljak) – kuidas need varieeruvused erinesid?

### Väljamõeldiste näide

Selles kursuses kasutame mõistet **"väljamõeldis"**, mis viitab nähtusele, kus LLM-id mõnikord genereerivad faktipõhiselt ebatäpset teavet nende koolituse või muude piirangute tõttu. Seda on populaarteaduses või uurimustes nimetatud ka _"hallutsinatsioonideks"_. Kuid soovitame kasutada _"väljamõeldis"_ terminina, et vältida käitumise antropomorfiseerimist, seostades masina väljundit inimlike omadustega. See toetab ka [Vastutustundliku tehisintellekti juhiseid](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) terminoloogia seisukohast, eemaldades sõnu, mida mõnedes kontekstides võib pidada solvavaks või mitte-sisse võtvaks.

Kas soovid aru saada, kuidas väljamõeldised toimivad? Mõtle käsule, mis palub tehisintellektil luua sisu mitteolemasoleva teema kohta (et tagada, et seda pole koolitusandmestikus). Näiteks kasutasin seda käsku:

> **Käsk:** loo õppetund Marsi sõjast 2076. aastal.

Veebipäring näitas, et on olemas väljamõeldud kirjeldused (nt telesarjad või raamatud) Marsi sõdadest – kuid mitte 2076. aastal. Tervemõistus ütleb ka, et 2076. aasta on _tulevikus_, seega ei saa see olla seotud reaalse sündmusega.


Mis siis juhtub, kui me käivitame selle päringu erinevate LLM-teenusepakkujatega?

> **Vastus 1**: OpenAI Playground (GPT-35)

![Response 1](../../../translated_images/et/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Vastus 2**: Azure OpenAI Playground (GPT-35)

![Response 2](../../../translated_images/et/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Vastus 3**: : Hugging Face Chat Playground (LLama-2)

![Response 3](../../../translated_images/et/04-fabrication-huggingchat.faf82a0a51278956.webp)

Nagu oodatud, toodab iga mudel (või mudeli versioon) veidi erinevaid vastuseid tänu stokastilisele käitumisele ja mudeli võimekuse erinevustele. Näiteks suunab üks mudel 8. klassi tasemele, samas kui teine eeldab keskkooliõpilast. Kuid kõik kolm mudelit genereerisid vastuseid, mis võiksid veenda teadmata kasutajat, et sündmus oli tõeline.

Päringu inseneritehnika meetodid nagu _metaprompting_ ja _temperatuuri seadistamine_ võivad mõnevõrra vähendada mudeli väljamõeldisi. Uued päringu inseneri _arhitektuurid_ integreerivad sujuvalt uued tööriistad ja meetodid päringu voogu, et leevendada või vähendada mõningaid neist mõjudest.

## Juhtumiuuring: GitHub Copilot

Lõpetame selle osa sellega, et saame aru, kuidas päringu inseneritehnikat kasutatakse reaalses maailmas, vaadates ühte juhtumiuuringut: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot on sinu "AI paariprogrammeerija" – see teisendab teksipäringud koodilõikudeks ja on integreeritud sinu arenduskeskkonda (näiteks Visual Studio Code), pakkudes sujuvat kasutajakogemust. Nagu alljärgnevate blogiseeriate põhjal on dokumenteeritud, põhines esialgne versioon OpenAI Codex mudelil – insenerid mõistsid kiiresti vajadust mudelit peenhäälestada ja arendada paremaid päringu inseneri tehnikaid, et parandada koodi kvaliteeti. Juulis [esitlesid nad täiustatud AI mudelit, mis läheb Codexist kaugemale](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) veelgi kiiremaks soovituste tegemiseks.

Loe postitusi järjest, et jälgida nende õppimisprotsessi.

- **Mai 2023** | [GitHub Copilot mõistab su koodi paremini](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mai 2023** | [GitHub sees: tööd GitHub Copiloti taga olevate LLM-idega](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Juuni 2023** | [Kuidas kirjutada paremaid päringuid GitHub Copilot jaoks](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Juuli 2023** | [GitHub Copilot läheb Codexist kaugemale täiustatud AI mudeliga](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Juuli 2023** | [Arendaja juhend päringu insenerile ja LLM-idele](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Sept 2023** | [Kuidas ehitada ettevõtte LLM-rakendus: õppetunnid GitHub Copilotist](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Sa võid ka sirvida nende [inseneriblogi](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst), kus on rohkem postitusi nagu [see](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), mis näitab, kuidas neid mudeleid ja tehnikaid _rakendatakse_ reaalse maailma rakenduste arendamisel.

---

<!--
ÕPPEMATERJALI MALL:
See üksus peaks katma põhikontseptsiooni #2.
Kinnita kontseptsiooni näidete ja viidetega.

KONTSEPTSIOON #2:
Päringu kujundamine.
Illustreeritud näidetega.
-->

## Päringu koostamine

Oleme näinud, miks päringu inseneritehnika on oluline – nüüd mõistame, kuidas päringud on _koostatud_, et saaksime hinnata erinevaid tehnikaid tõhusama päringu kujundamiseks.

### Lihtne päring

Alustame lihtsast päringust: tekstisisend, mis saadetakse mudelile ilma muude kontekstideta. Näide - kui saata US riigihümni esimesed sõnad OpenAI [Completion API-le](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), siis see kohe _täidab_ vastuse järgmiste ridadega, illustreerides põhilist ennustuskäitumist.

| Päring (sisend)     | Täitmine (väljund)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Tundub, nagu alustaksid sa USA riigihümni "The Star-Spangled Banner" sõnu. Täielik tekst on ...                                            |

### Kompleksne päring

Lisame nüüd konteksti ja juhised sellele lihtsale päringule. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) võimaldab ehitada komplekspäringut _sõnumite_ kogumikuna, kus:

- Sisendi/väljundi paarid, mis peegeldavad _kasutaja_ sisendit ja _abistaja_ vastust.
- Süsteemisõnum, mis seab konteksti abilise käitumiseks või isikupäraks.

Taotlus on nüüd alljärgnevas vormis, kus _tokeniseerimine_ haarab tõhusalt kontekstist ja vestlusest asjakohast teavet. Süsteemi konteksti muutmine võib seega mõjutada täitmiste kvaliteeti sama palju kui kasutaja poolt esitatud sisendid.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Juhise päring

Ülaltoodud näidetes oli kasutaja päring lihtne tekstipäring, mida saab tõlgendada kui info taotlust. _Juhiste_ päringute korral saame seda teksti kasutada, et täpsemalt määratleda ülesannet, pakkudes AI-le paremat juhendamist. Näide:

| Päring (sisend)                                                                                                                                                                                                                         | Täitmine (väljund)                                                                                                        | Juhise tüüp        |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Kirjuta Ameerika kodusõja kirjeldus                                                                                                                                                                                                    | _tagastati lihtne lõik_                                                                                                    | Lihtne              |
| Kirjuta Ameerika kodusõja kirjeldus. Too välja olulised kuupäevad ja sündmused ning kirjelda nende tähendust                                                                                                                               | _tagastati lõik ja nimekiri olulistest sündmuste kuupäevadest koos kirjeldustega_                                           | Kompleksne          |
| Kirjuta Ameerika kodusõja kirjeldus ühes lõigus. Too välja 3 märksõna oluliste kuupäevade ja nende tähendusega. Too 3 lisamärksõna ajalooliste tegelaste ja nende panustega. Tagasta väljund JSON-failina | _tagastab tekstikastis põhjalikuma detailsema teabe, vormindatuna JSON-vormingus, mida saab kopeerida ja vajadusel valideerida_ | Kompleksne. Vormindatud. |

## Põhisisu

Ülaltoodud näidetes oli päring siiski üsna avatud, lubades LLM-il otsustada, milline osa selle eelnevalt treenitud andmestikust on asjakohane. _Põhisisu_ kujundusmustri korral jaguneb sisendtekst kaheks osaks:

- juhis (tegevus)
- asjakohane sisu (mis mõjutab tegevust)

Näide, kus juhis on "kokkuvõtke see 2 lauses".

| Päring (sisend)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Täitmine (väljund)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter on päikesest viies planeet ja suurim Päikesesüsteemis. See on gaasihiid, mille mass on üks tuhandik Päikese massist, kuid kahe ja poole korra suurem kui kõigi teiste Päikesesüsteemi planeetide masside summa. Jupiter on üks eredamaid palja silmaga nähtavaid objektid öötaevas ja on olnud tuntud iidsetest tsivilisatsioonidest enne kirjaliku ajaloo algust. Selle nimi tuleneb Rooma jumal Jupiterist.[19] Maa pealt vaadates võib Jupiter olla piisavalt hele, et selle peegeldav valgus heidaks nähtavaid varje,[20] ja on keskmiselt kolmandaks kõige eredam looduslik objekt öötaevas pärast Kuut ja Veenust. <br/> **Kokkuvõtke see 2 lühikeses lauses** | Jupiter, päikesest viies planeet, on suurim Päikesesüsteemis ja tuntud kui üks eredamaid objekte öötaevas. Nime saanud Rooma jumala Jupiteri järgi, on see gaasihiid, mille mass on kahe ja poole korra suurem kui kõigi teiste planeetide ühismass. |

Põhisisu segmenti saab kasutada erinevalt, et anda tõhusamaid juhiseid:

- **Näited** - selle asemel, et anda mudelile otsene juhis, anna talle näiteid, mida teha, ja lase tal mustrit tuletada.
- **Vihjed** - järelda juhisele "vihje", mis suunab täitmisi, juhatades mudelit asjakohasemate vastusteni.
- **Mallid** - need on korduvad 'retseptid' päringutele koos kohatäitjatega (muutujad), mida saab konkreetsete andmetega kohandada konkreetsete kasutusjuhtude jaoks.

Uurime neid lähemalt tegutsemas.

### Näidete kasutamine

See on lähenemine, kus kasutatakse põhisisu, et "toita mudelile" näiteid soovitud väljundist antud juhise jaoks, lubades tal mustri tuletada. Näidete arvu põhjal võib teha null-löögiga päringu, ühe löögi päringu, mõne löögi päringu jne.

Päring koosneb nüüd kolmest komponendist:

- Ülesande kirjeldus
- Mõned näited soovitud väljundist
- Uue näite algus (mis muutub kaudseks ülesande kirjelduseks)

| Õpipõhimõte | Päring (sisend)                                                                                                                                         | Täitmine (väljund)      |
| :------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------- |
| Null-löök    | "Päike paistab". Tõlgi hispaania keelde.                                                                                                              | "El Sol está brillando". |
| Ühe löögiga | "Päike paistab" => ""El Sol está brillando". <br> "On külm ja tuuline päev" =>                                                                             | "Es un día frío y ventoso". |
| Mõne löögiga | Mängija jooksis alustest => Pesapall <br/> Mängija lõi ässa => Tennis <br/> Mängija lõi kuueste => Kriket <br/> Mängija tegi panuse => Korvpall           | Korvpall                 |
|               |                                                                                                                                                       |                          |

Pane tähele, et null-löögiga päringus pidime andma otsese juhise ("Tõlgi hispaania keelde"), kuid ühe löögi näites see tuletatakse ära. Mõne löögi näide näitab, kuidas rohkemate näidete lisamine võimaldab mudelitel teha täpsemaid järeldusi ilma lisajuhisteta.

### Päringu vihjed

Teine tehnika põhisisu kasutamiseks on anda _vihjeid_ näidete asemel. Sel juhul anname mudelile tõuke õiges suunas, alustades lõiguga, mis peegeldab soovitud vastuse formaati. Mudel "mõistab vihjet" ja jätkab samas stiilis.

| Vihjete arv | Päring (sisend)                                                                                                                                                                                                                                                                                                                                                                                                                                              | Täitmine (väljund)                                                                                                                                                                                                                                                                                       |
| :---------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0           | Jupiter on päikesest viies planeet ja suurim Päikesesüsteemis. See on gaasihiid, mille mass on üks tuhandik Päikese massist, kuid kahe ja poole korra suurem kui kõigi teiste Päikesesüsteemi planeetide masside summa. Jupiter on üks eredamaid palja silmaga nähtavaid objektid öötaevas ja on olnud tuntud iidsetest tsivilisatsioonidest enne kirjaliku ajaloo algust. <br/>**Kokkuvõtke see**                                | Jupiter on suurim planeet Päikesesüsteemis ja päikesest viies planeet. See on gaasihiid, mille mass on 1/1000 Päikese massist, kuid raskem kui kõik teised planeedid kokku. Iidsetel tsivilisatsioonidel on Jupiter pikka aega tuntud ja see on öötaevas hõlpsasti nähtav.                             |
| 1           | Jupiter on päikesest viies planeet ja suurim Päikesesüsteemis. See on gaasihiid, mille mass on üks tuhandik Päikese massist, kuid kahe ja poole korra suurem kui kõigi teiste Päikesesüsteemi planeetide masside summa. Jupiter on üks eredamaid palja silmaga nähtavaid objektid öötaevas ja on olnud tuntud iidsetest tsivilisatsioonidest enne kirjaliku ajaloo algust. <br/>**Kokkuvõtke see** <br/> Mida me õppisime, on see, et Jupiter | on päikesest viies planeet ja suurim Päikesesüsteemis. See on gaasihiid, mille mass on üks tuhandik Päikese massist, kuid kahe ja poole korra suurem kui kõigi teiste planeetide koosmass. See on palja silmaga hõlpsasti nähtav ja tuntud iidsetest aegadest.                                            |

| 2              | Jupiter on päikesesüsteemi viies planeet Päikesest ning suurim planeet Päikesesüsteemis. See on gaasihiiglane, mille mass on üks tuhandik Päikese massist, kuid kaks ja pool korda suurem kui kõigi teiste päikesesüsteemi planeetide mass kokku. Jupiter on üks eredamaid palja silmaga öötaevas nähtavaid objekte ning see on olnud tuntud muistsete tsivilisatsioonide seas juba enne ajaloolise kirja algust. <br/>**Kokkuvõte** <br/> 3 peamist fakti, mida õppisime:         | 1. Jupiter on päikesesüsteemi viies planeet Päikesest ning suurim Päikesesüsteemis. <br/> 2. See on gaasihiiglane, mille mass on üks tuhandik Päikese massist...<br/> 3. Jupiter on olnud palja silmaga nähtav juba muistsetest aegadest...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Päringumallid

Päringumall on _eelmääratletud päringu retsept_, mida saab vajadusel salvestada ja uuesti kasutada, et pakkuda suurel hulgal järjepidevamaid kasutajakogemusi. Lihtsaimal kujul on see lihtsalt kogumik päringu näidetest, nagu [see OpenAI näide](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst), mis pakub nii interaktiivseid päringu komponente (kasutaja ja süsteemi sõnumeid) kui ka API-põhist päringu vormingut – taaskasutuse toetamiseks.

Keerukamas vormis, nagu [see LangChain näide](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), sisaldab see _kohatäiteid_, mida saab asendada andmetega erinevatest allikatest (kasutaja sisend, süsteemi kontekst, välised andmeallikad jne), et genereerida päring dünaamiliselt. See võimaldab meil luua taaskasutatavate päringute raamatukogu, mida saab kasutada järjepidevate kasutajakogemuste loomisel **programmiliselt** suurel hulgal.

Lõpuks seisneb mallide tõeline väärtus võimes luua ja avaldada _päringu raamatukogusid_ vertikaalsete rakendusvaldkondade jaoks – kus päringumall on nüüd _optimeeritud_, et kajastada rakendusele spetsiifilist konteksti või näiteid, mis muudavad vastused sihtrühma jaoks asjakohasemaks ja täpsemaks. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) hoidla on suurepärane näide sellest lähenemisest, koondades haridusvaldkonna jaoks päringuraamatukogu, keskendudes olulistele eesmärkidele nagu õppetöö planeerimine, õppekava koostamine, õpilaste juhendamine jne.

## Toetav sisu

Kui mõtleme päringu koostamisele kui juhise (ülesande) ja sihtmärgi (esmane sisu) olemasolule, siis _teisene sisu_ on nagu täiendav kontekst, mida pakume, et **mingil moel mõjutada väljundit**. See võib olla seadistamisparameetrid, vormindusjuhised, teemade taksonoomiad jne, mis aitavad mudelil oma vastust kohandada vastavalt soovitud kasutajate eesmärkidele või ootustele.

Näiteks: Kui on olemas kursuse kataloog koos ulatusliku metaandmete (nimi, kirjeldus, tase, metaandmete märgendid, juhendaja jne) komplektiga kõigi õppekava kursuste kohta:

- saame määratleda juhise "kokkuvõtte kursuse kataloog sügiseks 2023"
- saame esmast sisu kasutada paaril näitel soovitud väljundi esitamiseks
- saame teisest sisu kasutada, et tuvastada 5 kõige olulisemat "märgendit"

Nüüd saab mudel pakkuda kokkuvõtet näidete vormingus – kuid kui tulemuses on mitu märgendit, saab prioritiseerida teisese sisu kaudu tuvastatud 5 märgendit.

---

<!--
ÕPPEKAVATEMPLAAT:
See jaotis peaks katma põhikontseptsiooni nr 1.
Tugevdage kontseptsiooni näidete ja viidetega.

KONTSEPTSIOON NR 3:
Päringu insenertehnika tehnikad.
Millised on mõned põhilised päringu insenertehnika tehnikad?
Illustreerige seda mõningate harjutustega.
-->

## Päringu parimad praktikad

Nüüd, kui teame, kuidas päringuid saab _koostada_, võime hakata mõtlema, kuidas neid _disainida_, et peegeldada parimaid praktikaid. Võime mõelda sellele kahes osas – õigele _mõtteviisile_ ja õigele _tehnikale_.

### Päringu insenertehnika mõtteviis

Päringu insenertehnika on katse-eksituse protsess, nii et pea meeles kolme põhilist juhist:

1. **Valdkonna mõistmine on oluline.** Vastuse täpsus ja asjakohasus sõltub _valdkonnast_, milles rakendus või kasutaja tegutseb. Kasuta oma intuitsiooni ja valdkonna ekspertiisi, et **kohandada tehnikaid** täpsemalt. Näiteks määra süsteemi päringutes valdkonnaspetsiifilisi isikupärasid või kasuta kasutajate päringutes valdkonnaspetsiifilisi malle. Paku teisest sisust valdkonnaspetsiifilist konteksti või kasuta _valdkonnaspetsiifilisi vihjeid ja näiteid_, et juhendada mudelit tuttavate kasutusmustrite suunas.

2. **Mudeli mõistmine on oluline.** Teame, et mudelid on oma olemuselt stokhastilised. Kuid mudelid võivad erineda kasutatud treeningandmestiku (eelõppteadmised), pakutavate võimaluste (nt API või SDK kaudu) ja optimeerimise sisu tüübi (nt kood vs pildid vs tekst) poolest. Mõista mudeli tugevusi ja piiranguid ning kasuta seda teadmist, et _prioriseerida ülesandeid_ või luua _kohandatud malle_, mis on optimeeritud mudeli võimsusele.

3. **Iteratsioon ja valideerimine on olulised.** Mudelid arenevad kiiresti ja samamoodi arenevad ka päringu insenertehnika tehnikad. Valdkonna eksperdina võid sul olla ka oma rakenduse spetsiifiline kontekst või kriteeriumid, mis ei pruugi laiemale kogukonnale kehtida. Kasuta päringu insenertehnika tööriistu ja tehnikaid, et "alustada kiirendatud päringu koostamist", seejärel korda ja vali tulemused oma intuitsiooni ja valdkonna asjatundlikkuse põhjal. Salvestage oma teadmised ja loo **teadmusbaas** (nt päringuraamatukogud), mida teised saavad kasutada uut baasjoontena kiiremate iteratsioonide jaoks tulevikus.

## Parimad praktikad

Vaatame nüüd tavalisi parimaid praktikaid, mida soovitavad [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) ja [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) spetsialistid.

| Mida                             | Miks                                                                                                                                                                                                                                              |
| :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hinda uusimaid mudeleid.        | Uued mudeligeneratsioonid võivad sisaldada täiustatud funktsioone ja kvaliteeti – kuid võivad põhjustada ka kõrgemaid kulusid. Hinda nende mõju ja tee migratsiooniga seotud otsused.                                                               |
| Eristage juhised ja kontekst    | Uuri, kas sinu mudel/teenusepakkuja määratleb _piirajad_, et eristada juhiseid, esmaseid ja teiseseid sisu selgemalt. See aitab mudelitel määrata tähemärkidele täpsemalt kaalu.                                                                   |
| Ole konkreetne ja selge          | Anna rohkem üksikasju soovitud konteksti, tulemuse, pikkuse, vormingu, stiili jm kohta. See parandab nii vastuste kvaliteeti kui järjepidevust. Salvestage retseptid taaskasutatavatesse mallidesse.                                                  |
| Ole kirjeldav, kasuta näiteid    | Mudelid võivad paremini reageerida "näita ja räägi" lähenemisele. Alusta `null-pildiga` (zero-shot), kus annad juhise (aga ei anna näiteid) ning seejärel proovi `mõne-sõltuvat` (few-shot) täiustust, andes mõned soovitud väljundi näited. Kasuta analoogiaid. |
| Kasuta vihjeid täitude käivitamiseks | Juhenda mudelit soovitud tulemuse suunas, andes sellele mõne juhtiva sõna või fraasi, mida see saab vastuse alustamiseks kasutada.                                                                                                                  |
| Korda ja kinnita               | Mõnikord peate mudelile endale mitmeid kordi kordama. Anna juhised enne ja pärast esmast sisu, kasuta juhist ja vihjet vms. Korda ja vali, milline lähenemine töötab.                                                                                |
| Järjestus on tähtis             | Teave mudelile esitamise järjekord võib avaldada mõju väljundile, ka õpikenäidetes recency ehk hiljuti sisestatud mõju tõttu. Proovi erinevaid variante, et näha, mis töötab kõige paremini.                                                           |
| Anna mudelile "väljapääs"        | Anna mudelile _tagasipöördumisvastus_, mida ta saab anda, kui ta mingil põhjusel ei suuda ülesannet lõpetada. See võib vähendada valet või väljamõeldud vastuste tekkimise tõenäosust.                                                              |
|                                 |                                                                                                                                                                                                                                                   |

Nagu igas parimas praktikas, pea meeles, et _tulemused võivad mudelist, ülesandest ja valdkonnast sõltuvalt erineda_. Kasuta neid kui lähtepunkti ja korda, et leida parim lahendus endale. Hinda pidevalt uuesti oma päringu insenertehnika protsessi, kuna uus mudelid ning tööriistad muutuvad kättesaadavaks, keskendudes protsessi skaleeritavusele ja vastuste kvaliteedile.

<!--
ÕPPEKAVATEMPLAAT:
See jaotis peaks pakkuma koodiväljakutset, kui see on asjakohane

VÄLJAKUTSE:
Link Jupyteri märkmikule, kus juhistes on ainult koodikommentaarid (koodi osad on tühjad).

LAHENDUS:
Link selle märkmiku koopiale, kus päringud on täidetud ja käivitatud, näidates üht näidet.
-->

## Ülesanne

Palju õnne! Sa jõudsid õppetüki lõpuni! On aeg panna mõned neist kontseptsioonidest ja tehnikaist proovile tõeliste näidetega!

Meie ülesandes kasutame Jupyteri märkmikku, mille harjutusi saad interaktiivselt täita. Sa võid lisaks märkmele laiendada ka oma Markdown ja koodirakkudega, et iseseisvalt uurida ideid ja tehnikaid.

### Alustamiseks klooni hoidla, seejärel

- (Soovitatav) Käivita GitHub Codespaces
- (Valikuline) Klooni hoidla oma lokaalsele seadmele ja kasuta seda Docker Desktopiga
- (Valikuline) Ava märkmik oma eelistatud märkmikukeskkonnas.

### Seejärel seadista oma keskkonnamuutujad

- Kopeeri hoidla juurest fail `.env.copy` nimega `.env` ja täida `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` ja `AZURE_OPENAI_DEPLOYMENT` väärtused. Tule tagasi [õppimise sandboxi sektsiooni](#õppimise-liivakast), et teada saada, kuidas.

### Seejärel ava Jupyteri märkmik

- Vali täitmiskeskkonna kernel. Kui kasutad valikuid 1 või 2, valige lihtsalt vaikimisi Python 3.10.x kernel, mille pakub dev konteiner.

Oled valmis harjutusi jooksma. Pane tähele, et siin pole _õigeid ega valesid_ vastuseid – lihtsalt õpid läbi katse-eksituse ning arendad intuitsiooni, mis töötab antud mudeli ja rakendusvaldkonna puhul.

_Seetõttu pole sellel õppetükil koodi lahendusosa. Selle asemel on märkmikus Markdown-rakud pealkirjaga "Minu lahendus:", mis näitavad ühe näidistulemuse viidet._

 <!--
ÕPPEKAVATEMPLAAT:
Seo jaotis kokku kokkuvõtte ja iseõppematerjalidega.
-->

## Teadmiste kontroll

Milline järgnevatest on hea päring, järgides mõistlikke parimaid praktikaid?

1. Näita mulle punase auto pilti
2. Näita mulle punase auto pilti mark Volvo ja mudel XC90, mis on parkimas kalju ääres päikeseloojangul
3. Näita mulle punase auto pilti mark Volvo ja mudel XC90

V: 2 on parim päring, kuna see annab üksikasju "mida" ja läheb detailidesse (mitte lihtsalt auto, vaid konkreetne mark ja mudel) ning kirjeldab ka üldist olukorda. 3 on järgmiseks parim, kuna sisaldab samuti palju kirjelduselemente.

## 🚀 Väljakutse

Proovi kasutada "vihje" tehnikat päringuga: Täienda lauset "Näita mulle punase auto pilti mark Volvo ja ". Mida see vastab ja kuidas saaksid seda parendada?

## Suurepärane töö! Jätka õppimist

Kas soovid rohkem teada saada erinevatest päringu insenertehnika kontseptsioonidest? Mine [edasijõudnute õppimise lehele](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kus on selle teema kohta muud suurepärased ressursid.

Liigu peatüki 5 juurde, kus vaatleme [edasijõudnud päringu tehnikat](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->