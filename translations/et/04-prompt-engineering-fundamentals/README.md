<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8b3cb38518cf4fe7714d2f5e74dfa3eb",
  "translation_date": "2025-10-11T11:30:07+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "et"
}
-->
# Promptide kujundamise alused

[![Promptide kujundamise alused](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.et.png)](https://aka.ms/gen-ai-lesson4-gh?WT.mc_id=academic-105485-koreyst)

## Sissejuhatus
See moodul käsitleb olulisi kontseptsioone ja tehnikaid tõhusate promptide loomiseks generatiivsete AI mudelite jaoks. Kuidas te oma prompti LLM-ile kirjutate, on samuti oluline. Hoolikalt koostatud prompt võib anda parema kvaliteediga vastuse. Aga mida täpselt tähendavad sellised terminid nagu _prompt_ ja _promptide kujundamine_? Ja kuidas ma saan parandada prompti _sisendit_, mida ma LLM-ile saadan? Need on küsimused, millele püüame vastata selles peatükis ja järgmises.

_Generatiivne AI_ suudab luua uut sisu (nt teksti, pilte, heli, koodi jne) vastuseks kasutaja päringutele. See saavutatakse _suurte keelemudelite_ abil, nagu OpenAI GPT ("Generative Pre-trained Transformer") seeria, mis on treenitud kasutama loomulikku keelt ja koodi.

Kasutajad saavad nüüd nende mudelitega suhelda tuttavate paradigmade, nagu vestlus, kaudu, ilma et neil oleks vaja tehnilisi teadmisi või koolitust. Mudelid on _promptipõhised_ – kasutajad saadavad tekstisisendi (prompti) ja saavad tagasi AI vastuse (täitmise). Nad saavad seejärel "vestelda AI-ga" iteratiivselt, mitme pöördega vestlustes, täpsustades oma prompti, kuni vastus vastab nende ootustele.

"Promptid" muutuvad nüüd generatiivsete AI rakenduste peamiseks _programmeerimisliideseks_, mis ütlevad mudelitele, mida teha, ja mõjutavad tagastatud vastuste kvaliteeti. "Promptide kujundamine" on kiiresti kasvav uurimisvaldkond, mis keskendub promptide _kujundamisele ja optimeerimisele_, et pakkuda järjepidevaid ja kvaliteetseid vastuseid suurel skaalal.

## Õpieesmärgid

Selles õppetükis õpime, mis on promptide kujundamine, miks see on oluline ja kuidas me saame luua tõhusamaid prompte konkreetse mudeli ja rakenduse eesmärgi jaoks. Me mõistame promptide kujundamise põhikontseptsioone ja parimaid tavasid – ning õpime tundma interaktiivset Jupyter Notebooki "liivakasti" keskkonda, kus saame neid kontseptsioone rakendada reaalsete näidete abil.

Õppetunni lõpuks suudame:

1. Selgitada, mis on promptide kujundamine ja miks see on oluline.
2. Kirjeldada prompti komponente ja nende kasutamist.
3. Õppida parimaid tavasid ja tehnikaid promptide kujundamiseks.
4. Rakendada õpitud tehnikaid reaalsete näidete abil, kasutades OpenAI lõpp-punkti.

## Olulised terminid

Promptide kujundamine: Praktika, mis hõlmab sisendite kujundamist ja täpsustamist, et suunata AI mudeleid soovitud väljundite loomise poole.
Tokeniseerimine: Teksti jagamise protsess väiksemateks üksusteks, mida nimetatakse tokeniteks, mida mudel suudab mõista ja töödelda.
Instruktsioonidega häälestatud LLM-id: Suured keelemudelid (LLM-id), mida on täpsustatud konkreetsete juhistega, et parandada nende vastuste täpsust ja asjakohasust.

## Õppimise liivakast

Promptide kujundamine on praegu rohkem kunst kui teadus. Parim viis selle intuitsiooni parandamiseks on _rohkem harjutada_ ja kasutada katse-eksituse lähenemist, mis ühendab rakenduse valdkonna teadmised soovitatud tehnikate ja mudelispetsiifiliste optimeerimistega.

Selle õppetunni juurde kuuluv Jupyter Notebook pakub _liivakasti_ keskkonda, kus saate õpitut kohe proovida – kas õppetunni käigus või koodiväljakutse osana. Harjutuste täitmiseks vajate:

1. **Azure OpenAI API võtit** – teenuse lõpp-punkti juurdepääsuks juurutatud LLM-ile.
2. **Python Runtime'i** – keskkonda, kus Notebooki saab käivitada.
3. **Kohalikke keskkonnamuutujaid** – _täitke [SEADISTUS](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) sammud kohe, et olla valmis_.

Notebook sisaldab _algajatele mõeldud_ harjutusi – kuid teil soovitatakse lisada oma _Markdown_ (kirjeldus) ja _Code_ (prompti päringud) sektsioone, et proovida rohkem näiteid või ideid – ja arendada oma intuitsiooni promptide kujundamise osas.

## Illustreeritud juhend

Kas soovite enne süvenemist saada ülevaate sellest, mida see õppetund hõlmab? Vaadake seda illustreeritud juhendit, mis annab ülevaate peamistest käsitletavatest teemadest ja olulisematest mõtetest, mida igaühe kohta meeles pidada. Õppetunni teekond viib teid põhikontseptsioonide ja väljakutsete mõistmisest nende lahendamiseni asjakohaste promptide kujundamise tehnikate ja parimate tavade abil. Pange tähele, et juhendi "Edasijõudnud tehnikad" osa viitab järgmises peatükis käsitletavale sisule.

![Promptide kujundamise illustreeritud juhend](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.et.png)

## Meie startup

Räägime nüüd, kuidas _see teema_ seostub meie startupi missiooniga [tuua AI innovatsioon haridusse](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Me tahame luua AI-põhiseid rakendusi _personaalset õppimist_ toetamiseks – seega mõtleme, kuidas erinevad meie rakenduse kasutajad võiksid "kujundada" prompte:

- **Administraatorid** võivad paluda AI-l _analüüsida õppekava andmeid, et tuvastada katvuse lünki_. AI saab tulemusi kokku võtta või visualiseerida neid koodiga.
- **Õpetajad** võivad paluda AI-l _luua õppetundide plaan sihtrühma ja teema jaoks_. AI saab koostada personaalset plaani kindlaksmääratud formaadis.
- **Õpilased** võivad paluda AI-l _õpetada neid raskes aines_. AI saab nüüd juhendada õpilasi tundide, vihjete ja näidetega, mis on kohandatud nende tasemele.

See on vaid jäämäe tipp. Vaadake [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) – avatud lähtekoodiga promptide raamatukogu, mille on koostanud hariduseksperdid – et saada laiem ülevaade võimalustest! _Proovige mõnda neist promptidest liivakastis või OpenAI Playgroundis, et näha, mis juhtub!_

<!--
ÕPPETUNNI MALL:
See üksus peaks käsitlema põhikontseptsiooni #1.
Tugevdage kontseptsiooni näidete ja viidetega.

KONTSEPTSIOON #1:
Promptide kujundamine.
Defineerige see ja selgitage, miks seda vaja on.
-->

## Mis on promptide kujundamine?

Alustasime seda õppetundi, määratledes **promptide kujundamise** kui protsessi, mis hõlmab tekstisisendite (promptide) _kujundamist ja optimeerimist_, et pakkuda järjepidevaid ja kvaliteetseid vastuseid (täitmisi) konkreetse rakenduse eesmärgi ja mudeli jaoks. Seda võib vaadelda kui kahesammulist protsessi:

- _kujundamine_ algse prompti jaoks konkreetse mudeli ja eesmärgi jaoks
- _täpsustamine_ prompti iteratiivselt, et parandada vastuse kvaliteeti

See on paratamatult katse-eksituse protsess, mis nõuab kasutaja intuitsiooni ja pingutust, et saavutada optimaalsed tulemused. Miks see siis oluline on? Sellele küsimusele vastamiseks peame esmalt mõistma kolme kontseptsiooni:

- _Tokeniseerimine_ = kuidas mudel "näeb" prompti
- _Baasmudelid_ = kuidas põhjalik mudel "töötleb" prompti
- _Instruktsioonidega häälestatud mudelid_ = kuidas mudel suudab nüüd "näha ülesandeid"

### Tokeniseerimine

LLM näeb prompti kui _tokenite järjestust_, kus erinevad mudelid (või mudeli versioonid) võivad sama prompti tokeniseerida erinevalt. Kuna LLM-id on treenitud tokenite (mitte toorteksti) põhjal, mõjutab promptide tokeniseerimise viis otseselt genereeritud vastuse kvaliteeti.

Et saada intuitsiooni, kuidas tokeniseerimine töötab, proovige tööriistu nagu [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst), mis on näidatud allpool. Kopeerige oma prompt – ja vaadake, kuidas see muudetakse tokeniteks, pöörates tähelepanu sellele, kuidas käsitletakse tühikuid ja kirjavahemärke. Pange tähele, et see näide näitab vanemat LLM-i (GPT-3) – seega võib uuema mudeliga proovimine anda erineva tulemuse.

![Tokeniseerimine](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.et.png)

### Kontseptsioon: Põhimudelid

Kui prompt on tokeniseeritud, on ["Baasmudeli"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (või põhjaliku mudeli) peamine funktsioon ennustada tokenit selles järjestuses. Kuna LLM-id on treenitud massiivsete tekstikogumite põhjal, on neil hea arusaam tokenite vahelisest statistilisest seosest ja nad suudavad seda ennustust teha teatud kindlusega. Pange tähele, et nad ei mõista sõnade _tähendust_ promptis või tokenis; nad näevad lihtsalt mustrit, mida nad saavad "täita" järgmise ennustusega. Nad võivad jätkata järjestuse ennustamist, kuni kasutaja sekkub või kehtestatakse mõni eelnevalt määratud tingimus.

Kas soovite näha, kuidas promptipõhine täitmine töötab? Sisestage ülaltoodud prompt Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) vaikeseadetega. Süsteem on konfigureeritud käsitlema prompti kui teabe päringut – seega peaksite nägema täitmist, mis rahuldab selle konteksti.

Aga mis siis, kui kasutaja soovib näha midagi konkreetset, mis vastab teatud kriteeriumidele või ülesande eesmärgile? Siin tulevad mängu _instruktsioonidega häälestatud_ LLM-id.

![Baasmudeli vestluse täitmine](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.et.png)

### Kontseptsioon: Instruktsioonidega häälestatud LLM-id

[Instruktsioonidega häälestatud LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) algab põhjaliku mudeliga ja täpsustab seda näidete või sisend/väljund paaridega (nt mitme pöördega "sõnumid"), mis võivad sisaldada selgeid juhiseid – ja AI vastus püüab järgida seda juhist.

See kasutab tehnikaid nagu tugevdatud õppimine inimeste tagasisidega (RLHF), mis suudab treenida mudelit _juhiseid järgima_ ja _tagasisidest õppima_, et see toodaks vastuseid, mis sobivad paremini praktiliste rakenduste jaoks ja on kasutaja eesmärkidega asjakohasemad.

Proovime seda – vaadake uuesti ülaltoodud prompti, kuid muutke nüüd _süsteemi sõnumit_, et anda järgmine juhis kontekstiks:

> _Kokkuvõtke teile antud sisu teise klassi õpilase jaoks. Hoidke tulemus ühe lõiguna, kus on 3–5 punktloendit._

Vaadake, kuidas tulemus on nüüd häälestatud soovitud eesmärgi ja formaadi kajastamiseks? Õpetaja saab nüüd seda vastust otse kasutada oma klassi slaidides.

![Instruktsioonidega häälestatud LLM-i vestluse täitmine](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.et.png)

## Miks me vajame promptide kujundamist?

Nüüd, kui me teame, kuidas LLM-id töötlevad prompte, räägime _miks_ me vajame promptide kujundamist. Vastus peitub selles, et praegused LLM-id esitavad mitmeid väljakutseid, mis muudavad _usaldusväärsete ja järjepidevate täitmiste_ saavutamise keerulisemaks ilma prompti koostamise ja optimeerimisele pingutust panemata. Näiteks:

1. **Mudelivastused on juhuslikud.** _Sama prompt_ võib tõenäoliselt anda erinevaid vastuseid erinevate mudelite või mudeliversioonidega. Ja see võib isegi anda erinevaid tulemusi _sama mudeliga_ erinevatel aegadel. _Promptide kujundamise tehnikad aitavad meil neid variatsioone minimeerida, pakkudes paremaid juhiseid_.

1. **Mudelid võivad vastuseid fabritseerida.** Mudelid on eelnevalt treenitud _suure, kuid piiratud_ andmekogumiga, mis tähendab, et neil puudub teadmine treeningu ulatusest väljaspool olevate kontseptsioonide kohta. Selle tulemusena võivad nad anda täitmisi, mis on ebatäpsed, väljamõeldud või otseselt vastuolulised teadaolevate faktidega. _Promptide kujundamise tehnikad aitavad kasutajatel tuvastada ja leevendada selliseid fabritseerimisi, näiteks paludes AI-l viiteid või põhjendusi_.

1. **Mudelite võimekus varieerub.** Uuematel mudelitel või mudelipõlvkondadel on rikkamad võimekused, kuid need toovad kaasa ka unikaalseid iseärasusi ja kompromisse kulude ja keerukuse osas. _Promptide kujundamine aitab meil välja töötada parimad tavad ja töövood, mis abstraktivad erinevused ja kohanduvad mudelispetsiifiliste nõuetega skaleeritaval ja sujuval viisil_.

Vaatame seda tegevuses OpenAI või Azure OpenAI Playgroundis:

- Kasutage sama prompti erinevate LLM-i juurutustega (nt OpenAI, Azure OpenAI, Hugging Face) – kas nägite variatsioone?
- Kasutage sama prompti korduvalt _sama_ LLM-i juurutusega (nt Azure OpenAI Playground) – kuidas need variatsioonid erinesid?

### Fabritseerimiste näide

Selles kursuses kasutame terminit **"fabritseerimine"**, et viidata nähtusele, kus LLM-id mõnikord genereerivad faktuaalselt ebatäpset teavet treeningu piirangute või muude piirangute tõttu. Võite olla kuulnud seda nimetatavat ka _"hallutsinatsioonideks"_ populaarsetes artiklites või teadusartiklites. Kuid me soovitame tungivalt kasutada terminit _"fabritseerimine"_, et me ei omistaks inimlikku omadust masinapõhisele tulemusele. See tugevdab ka [Vastutustundliku AI juhiseid](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) terminoloogia perspektiivist, eemaldades terminid, mis võivad olla teatud kontekstis solvavad või mittekaasavad.

Kas soovite saada aimu, kuidas fabritseerimised toimivad? Mõelge promptile, mis juhendab AI-d looma sisu olematu teema kohta (et tagada, et seda ei leidu treeningandmestikus). Näiteks – ma proovisin seda prompti:

> **Prompt:** loo õppetundide plaan Marsi sõja kohta aastal 2076.
Veebist otsides leidsin, et Marsi sõdadest on loodud väljamõeldud lugusid (näiteks telesarjad või raamatud) – kuid mitte aastal 2076. Terve mõistus ütleb ka, et 2076 on _tulevikus_ ja seega ei saa seda seostada päris sündmusega.

Mis juhtub, kui kasutame seda sisendit erinevate LLM-i pakkujatega?

> **Vastus 1**: OpenAI Playground (GPT-35)

![Vastus 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.et.png)

> **Vastus 2**: Azure OpenAI Playground (GPT-35)

![Vastus 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.et.png)

> **Vastus 3**: Hugging Face Chat Playground (LLama-2)

![Vastus 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.et.png)

Nagu oodatud, genereerib iga mudel (või mudeli versioon) veidi erinevaid vastuseid tänu juhuslikule käitumisele ja mudeli võimekuse variatsioonidele. Näiteks üks mudel sihib 8. klassi tasemel publikut, samas kui teine eeldab keskkooli taset. Kuid kõik kolm mudelit genereerisid vastuseid, mis võivad veenda informeerimata kasutajat, et sündmus oli tõeline.

Sisenditehnikaid nagu _metasisestamine_ ja _temperatuuri seadistamine_ saab kasutada mudeli väljamõeldiste vähendamiseks teatud määral. Uued sisenditehnika _arhitektuurid_ integreerivad sujuvalt uusi tööriistu ja meetodeid sisendvoogu, et leevendada või vähendada mõningaid neist mõjudest.

## Juhtumiuuring: GitHub Copilot

Lõpetame selle osa, saades ülevaate, kuidas sisenditehnikaid kasutatakse päriselu lahendustes, vaadates ühte juhtumiuuringut: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot on teie "AI paarisprogrammeerija" – see teisendab tekstisisendid koodisoovitusteks ja on integreeritud teie arenduskeskkonda (näiteks Visual Studio Code), pakkudes sujuvat kasutuskogemust. Nagu allpool dokumenteeritud blogisarjas, põhines varaseim versioon OpenAI Codex mudelil – insenerid mõistsid kiiresti vajadust mudelit täpsustada ja arendada paremaid sisenditehnikaid, et parandada koodi kvaliteeti. Juulis [tutvustati täiustatud AI mudelit, mis ületab Codexi](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst), pakkudes veelgi kiiremaid soovitusi.

Lugege postitusi järjekorras, et jälgida nende õppeprotsessi.

- **Mai 2023** | [GitHub Copilot muutub paremaks teie koodi mõistmisel](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mai 2023** | [GitHubi sees: Töötamine GitHub Copiloti taga olevate LLM-idega](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Juuni 2023** | [Kuidas kirjutada paremaid sisendeid GitHub Copilotile](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Juuli 2023** | [.. GitHub Copilot ületab Codexi täiustatud AI mudeliga](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Juuli 2023** | [Arendaja juhend sisenditehnika ja LLM-ide kohta](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **September 2023** | [Kuidas luua ettevõtte LLM-i rakendust: Õppetunnid GitHub Copilotilt](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Samuti saate sirvida nende [inseneriblogi](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) rohkemate postituste jaoks, nagu [see](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), mis näitab, kuidas neid mudeleid ja tehnikaid _rakendatakse_ päriselu rakenduste arendamiseks.

---

## Sisendi koostamine

Oleme näinud, miks sisenditehnika on oluline – nüüd mõistame, kuidas sisendeid _koostatakse_, et saaksime hinnata erinevaid tehnikaid tõhusama sisendi kujundamiseks.

### Lihtne sisend

Alustame lihtsast sisendist: tekstisisend, mis saadetakse mudelile ilma täiendava kontekstita. Siin on näide – kui saadame USA rahvushümni esimesed sõnad OpenAI [Completion API-le](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), täidab mudel vastuse koheselt järgmiste ridadega, illustreerides põhilist ennustuskäitumist.

| Sisend (Input)     | Väljund (Output)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Tundub, et alustate USA rahvushümni "The Star-Spangled Banner" sõnadega. Täielikud sõnad on ... |

### Keeruline sisend

Nüüd lisame konteksti ja juhiseid sellele lihtsale sisendile. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) võimaldab meil koostada keerulise sisendi _sõnumite_ kogumina, mis sisaldab:

- Sisend/väljund paare, mis kajastavad _kasutaja_ sisendit ja _assistendi_ vastust.
- Süsteemi sõnumit, mis määrab assistendi käitumise või isiksuse konteksti.

Päring on nüüd allpool toodud kujul, kus _tokeniseerimine_ tõhusalt haarab kontekstist ja vestlusest asjakohase teabe. Süsteemi konteksti muutmine võib olla sama mõjus vastuste kvaliteedile kui kasutaja sisendite muutmine.

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

### Juhendav sisend

Eelnevates näidetes oli kasutaja sisend lihtne tekstipäring, mida võis tõlgendada teabe päringuna. _Juhendavate_ sisendite puhul saame kasutada seda teksti ülesande täpsemaks määratlemiseks, pakkudes AI-le paremat juhendamist. Siin on näide:

| Sisend (Input)                                                                                                                                                                                                                         | Väljund (Output)                                                                                                        | Juhendi tüüp       |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Kirjuta kirjeldus kodusõjast                                                                                                                                                                                                   | _tagastati lihtne lõik_                                                                                              | Lihtne              |
| Kirjuta kirjeldus kodusõjast. Lisa olulised kuupäevad ja sündmused ning kirjelda nende tähtsust                                                                                                                                     | _tagastati lõik, millele järgnes oluliste sündmuste kuupäevade loetelu koos kirjeldustega_                                             | Keeruline             |
| Kirjuta kirjeldus kodusõjast ühes lõigus. Lisa 3 punktiga olulised kuupäevad ja nende tähtsus. Lisa veel 3 punktiga olulised ajaloolised tegelased ja nende panus. Tagasta väljund JSON-failina | _tagastati ulatuslikumad detailid tekstikastis, vormindatud JSON-ina, mida saab vajadusel kopeerida ja valideerida_ | Keeruline. Vormindatud. |

## Peamine sisu

Eelnevates näidetes oli sisend endiselt üsna avatud, võimaldades LLM-il otsustada, milline osa selle eelõpetatud andmestikust on asjakohane. _Peamise sisu_ kujundusmustriga jagatakse sisendtekst kaheks osaks:

- juhend (tegevus)
- asjakohane sisu (mis mõjutab tegevust)

Siin on näide, kus juhendiks on "kokkuvõtke see 2 lauses".

| Sisend (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Väljund (Output)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter on viies planeet Päikesest ja suurim Päikesesüsteemis. See on gaasihiiglane, mille mass on tuhandik Päikese massist, kuid kaks ja pool korda suurem kui kõigi teiste Päikesesüsteemi planeetide mass kokku. Jupiter on üks eredamaid objekte, mida palja silmaga öötaevas näha, ja seda on tuntud iidsetest tsivilisatsioonidest alates enne kirjalikku ajalugu. See on nime saanud Rooma jumala Jupiteri järgi.[19] Maa pealt vaadates võib Jupiter olla piisavalt ere, et selle peegeldunud valgus heidaks nähtavaid varje,[20] ja keskmiselt on see öötaevas kolmas eredaim looduslik objekt pärast Kuud ja Veenust. <br/> **Kokkuvõtke see 2 lühikeses lauses** | Jupiter, viies planeet Päikesest, on suurim Päikesesüsteemis ja tuntud kui üks eredamaid objekte öötaevas. Rooma jumala Jupiteri järgi nime saanud gaasihiiglase mass on kaks ja pool korda suurem kui kõigi teiste Päikesesüsteemi planeetide mass kokku. |

Peamise sisu segmenti saab kasutada mitmel viisil, et saavutada tõhusamaid juhiseid:

- **Näited** – selle asemel, et öelda mudelile, mida teha, kasutades selgesõnalist juhendit, andke sellele näiteid, mida teha, ja laske mudelil mustrit järeldada.
- **Vihjed** – järgige juhendit "vihjega", mis suunab vastuse, juhatades mudeli asjakohasemate vastuste poole.
- **Mallid** – need on korduvkasutatavad "retseptid" sisendite jaoks, millel on kohandatavad kohatäited (muutujad) konkreetsete kasutusjuhtude jaoks.

Vaatame neid tegevuses.

### Näidete kasutamine

See on lähenemine, kus kasutate peamist sisu, et "toita mudelit" mõne näitega soovitud väljundist antud juhendi jaoks, ja lasete mudelil mustrit järeldada. Näidete arvu põhjal saame kasutada nullnäidise, ühenäidise, väheste näidiste sisestamist jne.

Sisend koosneb nüüd kolmest komponendist:

- Ülesande kirjeldus
- Mõned näited soovitud väljundist
- Uue näite algus (mis muutub kaudseks ülesande kirjelduseks)

| Õppimise tüüp | Sisend (Input)                                                                                                                                        | Väljund (Output)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Nullnäidis     | "Päike paistab". Tõlkige hispaania keelde                                                                                                            | "El Sol está brillando".    |
| Ühenäidis      | "Päike paistab" => ""El Sol está brillando". <br> "See on külm ja tuuline päev" =>                                                                 | "Es un día frío y ventoso". |
| Väheste näidistega      | Mängija jooksis baaside vahel => Pesapall <br/> Mängija lõi ässa => Tennis <br/> Mängija lõi kuue => Kriket <br/> Mängija tegi pealtpaneku => | Korvpall                  |
|               |                                                                                                                                                       |                             |

Pange tähele, kuidas pidime nullnäidise sisestamise puhul andma selgesõnalise juhendi ("Tõlkige hispaania keelde"), kuid see järeldatakse ühenäidise sisestamise näites. Väheste näidiste näide näitab, kuidas rohkemate näidiste lisamine võimaldab mudelitel teha täpsemaid järeldusi ilma täiendavate juhisteta.

### Sisendi vihjed

Teine tehnika peamise sisu kasutamiseks on _vihjete_ pakkumine, mitte näidete andmine. Sel juhul anname mudelile tõuke õiges suunas, _alustades_ seda soovitud vastuse vormingut kajastava lõiguga. Mudel "võtab vihje" ja jätkab samas suunas.

| Vihjete arv | Sisend (Input)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Väljund (Output)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter on viies planeet Päikesest ja suurim Päikesesüsteemis. See on gaasihiiglane, mille mass on tuhandik Päikese massist, kuid kaks ja pool korda suurem kui kõigi teiste Päikesesüsteemi planeetide mass kokku. Jupiter on üks eredamaid objekte, mida palja silmaga öötaevas näha, ja seda on tuntud iidsetest tsivilisatsioonidest alates enne kirjalikku ajalugu. <br/>**Kokkuvõtke see**                                       | Jupiter on suurim planeet meie Päikesesüsteemis ja viies Päikesest. See on gaasihiiglane, mille mass on 1/1000 Päikese massist, kuid see on raskem kui kõik teised planeedid kokku. Iidsed tsivilisatsioonid on Jupiteri juba ammu tundnud ja see on öötaevas kergesti nähtav. |
| 1              | Jupiter on Päikesest viies planeet ja suurim Päikesesüsteemis. See on gaasihiid, mille mass on tuhandik Päikese massist, kuid kaks ja pool korda suurem kui kõigi teiste Päikesesüsteemi planeetide mass kokku. Jupiter on üks eredamaid objekte, mida saab öötaevas palja silmaga näha, ja seda on tuntud juba iidsetest tsivilisatsioonidest alates enne kirjaliku ajaloo algust. <br/>**Kokkuvõte** <br/> Mida me õppisime: Jupiter | on Päikesest viies planeet ja suurim Päikesesüsteemis. See on gaasihiid, mille mass on tuhandik Päikese massist, kuid kaks ja pool korda suurem kui kõigi teiste planeetide mass kokku. Seda on lihtne palja silmaga näha ja seda on tuntud juba iidsetest aegadest.                        |
| 2              | Jupiter on Päikesest viies planeet ja suurim Päikesesüsteemis. See on gaasihiid, mille mass on tuhandik Päikese massist, kuid kaks ja pool korda suurem kui kõigi teiste Päikesesüsteemi planeetide mass kokku. Jupiter on üks eredamaid objekte, mida saab öötaevas palja silmaga näha, ja seda on tuntud juba iidsetest tsivilisatsioonidest alates enne kirjaliku ajaloo algust. <br/>**Kokkuvõte** <br/> 3 peamist fakti, mida õppisime:         | 1. Jupiter on Päikesest viies planeet ja suurim Päikesesüsteemis. <br/> 2. See on gaasihiid, mille mass on tuhandik Päikese massist...<br/> 3. Jupiter on olnud palja silmaga nähtav juba iidsetest aegadest ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Mallid

Mall on _eeldefineeritud retsept_, mida saab salvestada ja vajadusel uuesti kasutada, et pakkuda järjepidevamat kasutajakogemust suuremas mahus. Lihtsaimas vormis on see lihtsalt kogum näiteid, nagu [see OpenAI näide](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst), mis sisaldab nii interaktiivseid kasutaja ja süsteemi sõnumeid kui ka API-põhist päringuvormingut - toetades taaskasutust.

Keerukamas vormis, nagu [see LangChain näide](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), sisaldab see _kohatäiteid_, mida saab asendada andmetega erinevatest allikatest (kasutaja sisend, süsteemi kontekst, välised andmeallikad jne), et luua dünaamiliselt mall. See võimaldab luua taaskasutatavate mallide raamatukogu, mida saab kasutada järjepidevate kasutajakogemuste **programmiliseks** pakkumiseks suuremas mahus.

Lõpuks seisneb mallide tegelik väärtus _malliraamatukogude_ loomises ja avaldamises vertikaalsete rakendusvaldkondade jaoks - kus mall on nüüd _optimeeritud_, et kajastada rakendusepõhist konteksti või näiteid, mis muudavad vastused sihtrühmale asjakohasemaks ja täpsemaks. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) repository on suurepärane näide sellest lähenemisest, koondades hariduse valdkonna jaoks mallide raamatukogu, rõhutades olulisi eesmärke nagu õppetundide planeerimine, õppekava kujundamine, õpilaste juhendamine jne.

## Täiendav sisu

Kui mõtleme mallide koostamisele kui ülesande (instruction) ja sihtmärgi (primary content) määratlemisele, siis _sekundaarne sisu_ on nagu täiendav kontekst, mida pakume, et **mõjutada väljundit mingil viisil**. See võib olla häälestusparameetrid, vormindusjuhised, teemade taksonoomiad jne, mis aitavad mudelil _kohandada_ oma vastust vastavalt soovitud kasutaja eesmärkidele või ootustele.

Näiteks: Arvestades kursuse kataloogi, mis sisaldab ulatuslikku metaandmestikku (nimi, kirjeldus, tase, metaandmete sildid, juhendaja jne) kõigi õppekavas olevate kursuste kohta:

- saame määratleda juhise "kokkuvõtke sügise 2023 kursuse kataloog"
- saame kasutada esmast sisu, et pakkuda mõningaid näiteid soovitud väljundist
- saame kasutada sekundaarset sisu, et tuvastada 5 peamist huvipakkuvat "silti".

Nüüd saab mudel pakkuda kokkuvõtet näidatud formaadis - kuid kui tulemusel on mitu silti, saab see prioriteediks seada 5 sekundaarse sisuga määratud silti.

---

<!--
ÕPPETUNNI MALL:
See osa peaks hõlmama põhikontsepti #1.
Tugevdage kontsepti näidete ja viidetega.

KONTSEPT #3:
Mallide koostamise tehnikad.
Millised on mõned põhilised tehnikad mallide koostamiseks?
Illustreerige seda harjutustega.
-->

## Mallide koostamise parimad tavad

Nüüd, kui teame, kuidas malle saab _koostada_, saame hakata mõtlema, kuidas neid _kujundada_, et kajastada parimaid tavasid. Võime mõelda sellele kahes osas - omades õiget _mõtteviisi_ ja rakendades õigeid _tehnikaid_.

### Mallide koostamise mõtteviis

Mallide koostamine on katse-eksituse protsess, seega pidage meeles kolme laia juhendavat tegurit:

1. **Valdkonna mõistmine on oluline.** Vastuse täpsus ja asjakohasus sõltub _valdkonnast_, kus rakendus või kasutaja tegutseb. Kasutage oma intuitsiooni ja valdkonna teadmisi, et **kohandada tehnikaid** veelgi. Näiteks määratlege süsteemi mallides _valdkonnaspetsiifilised isiksused_ või kasutage kasutaja mallides _valdkonnaspetsiifilisi malle_. Pakkuge sekundaarset sisu, mis kajastab valdkonnaspetsiifilist konteksti, või kasutage _valdkonnaspetsiifilisi vihjeid ja näiteid_, et suunata mudel tuttavate kasutusmustrite poole.

2. **Mudeli mõistmine on oluline.** Me teame, et mudelid on olemuselt juhuslikud. Kuid mudeli rakendused võivad samuti erineda kasutatava treeningandmestiku (eelõpetatud teadmised), pakutavate võimaluste (nt API või SDK kaudu) ja optimeeritud sisutüübi (nt kood vs pildid vs tekst) poolest. Mõistke kasutatava mudeli tugevusi ja piiranguid ning kasutage seda teadmist, et _prioriteerida ülesandeid_ või luua _kohandatud malle_, mis on optimeeritud mudeli võimaluste jaoks.

3. **Iteratsioon ja valideerimine on olulised.** Mudelid arenevad kiiresti, nagu ka mallide koostamise tehnikad. Valdkonna eksperdina võib teil olla muu kontekst või kriteeriumid, mis kehtivad _teie_ konkreetse rakenduse puhul, kuid ei pruugi kehtida laiemale kogukonnale. Kasutage mallide koostamise tööriistu ja tehnikaid, et "kiirendada" mallide koostamist, seejärel iterige ja valideerige tulemusi, kasutades oma intuitsiooni ja valdkonna teadmisi. Salvestage oma teadmised ja looge **teadmistebaas** (nt mallide raamatukogud), mida teised saavad kasutada uue baasina, et tulevikus kiiremini iteratsiooni teha.

## Parimad tavad

Vaatame nüüd levinud parimaid tavasid, mida soovitavad [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) ja [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) praktikud.

| Mis                              | Miks                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Hinnake uusimaid mudeleid.       | Uue põlvkonna mudelitel on tõenäoliselt paremad funktsioonid ja kvaliteet - kuid need võivad olla ka kulukamad. Hinnake nende mõju ja tehke seejärel migratsiooniotsuseid.                                                                                |
| Eraldage juhised ja kontekst   | Kontrollige, kas teie mudel/pakkuja määratleb _eraldajad_, et eristada juhiseid, esmast ja sekundaarset sisu selgemalt. See võib aidata mudelitel määrata täpsemalt kaalu tokenitele.                                                         |
| Olge konkreetne ja selge             | Andke rohkem üksikasju soovitud konteksti, tulemuse, pikkuse, vormingu, stiili jne kohta. See parandab vastuste kvaliteeti ja järjepidevust. Salvestage retseptid taaskasutatavates mallides.                                                          |
| Olge kirjeldav, kasutage näiteid      | Mudelid võivad paremini reageerida "näita ja räägi" lähenemisviisile. Alustage `null-laskmise` lähenemisviisiga, kus annate juhise (kuid mitte näiteid), seejärel proovige `mõne-laskmise` lähenemist, pakkudes mõningaid näiteid soovitud väljundist. Kasutage analoogiaid. |
| Kasutage vihjeid, et alustada vastuseid | Suunake mudel soovitud tulemuse poole, andes sellele mõned juhtivad sõnad või fraasid, mida see saab kasutada vastuse alustamiseks.                                                                                                               |
| Korrake vajadusel                       | Mõnikord peate mudelile end kordama. Andke juhised enne ja pärast esmast sisu, kasutage juhist ja vihjet jne. Iterige ja valideerige, et näha, mis töötab.                                                         |
| Järjekord on oluline                     | Teave, mille järjekorras mudelile esitate, võib mõjutada väljundit, isegi õppimise näidetes, tänu hiljutise kallutatuse efektile. Proovige erinevaid võimalusi, et näha, mis töötab kõige paremini.                                                               |
| Andke mudelile "taganemisvõimalus"           | Andke mudelile _varuvastus_, mida see saab pakkuda, kui see ei suuda ülesannet mingil põhjusel täita. See võib vähendada mudelite valede või väljamõeldud vastuste genereerimise tõenäosust.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

Nagu iga parima tava puhul, pidage meeles, et _teie kogemus võib varieeruda_ sõltuvalt mudelist, ülesandest ja valdkonnast. Kasutage neid lähtepunktina ja iterige, et leida, mis teie jaoks kõige paremini töötab. Hindage pidevalt oma mallide koostamise protsessi, kui uued mudelid ja tööriistad muutuvad kättesaadavaks, keskendudes protsessi skaleeritavusele ja vastuste kvaliteedile.

<!--
ÕPPETUNNI MALL:
See osa peaks pakkuma koodiväljakut, kui see on asjakohane.

VÄLJAKUTSE:
Linkige Jupyter Notebook, kus juhised on ainult koodikommentaarides (koodiosad on tühjad).

LAHENDUS:
Linkige selle Notebooki koopia, kus mallid on täidetud ja käivitatud, näidates, milline üks näide võiks olla.
-->

## Ülesanne

Palju õnne! Olete jõudnud õppetunni lõpuni! Nüüd on aeg panna mõned neist kontseptsioonidest ja tehnikatest proovile reaalse näidetega!

Meie ülesande jaoks kasutame Jupyter Notebooki, kus saate harjutusi interaktiivselt täita. Samuti saate Notebooki laiendada oma Markdowni ja koodirakkudega, et uurida ideid ja tehnikaid iseseisvalt.

### Alustamiseks, forkige repo, seejärel

- (Soovitatav) Käivitage GitHub Codespaces
- (Alternatiiv) Kloonige repo oma kohalikku seadmesse ja kasutage seda Docker Desktopiga
- (Alternatiiv) Avage Notebook oma eelistatud Notebooki käituskeskkonnas.

### Järgmiseks, konfigureerige oma keskkonnamuutujad

- Kopeerige repo juurfail `.env.copy` failiks `.env` ja täitke `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` ja `AZURE_OPENAI_DEPLOYMENT` väärtused. Tulge tagasi [õppimise liivakasti sektsiooni](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals), et õppida, kuidas.

### Järgmiseks, avage Jupyter Notebook

- Valige käitusmootori kernel. Kui kasutate valikuid 1 või 2, valige lihtsalt arenduskonteineri vaikimisi Python 3.10.x kernel.

Olete valmis harjutusi käivitama. Pange tähele, et siin pole _õigeid ja valesid_ vastuseid - lihtsalt võimaluste uurimine katse-eksituse meetodil ja intuitsiooni loomine selle kohta, mis töötab antud mudeli ja rakendusvaldkonna jaoks.

_Sel põhjusel pole selles õppetunnis koodilahenduste segmente. Selle asemel on Notebookis Markdowni rakud pealkirjaga "Minu lahendus:", mis näitab ühte näidisväljundit viitena._

 <!--
ÕPPETUNNI MALL:
Lõpetage sektsioon kokkuvõtte ja ressurssidega iseseisvaks õppimiseks.
-->

## Teadmiste kontroll

Milline järgmistest on hea mall, mis järgib mõningaid mõistlikke parimaid tavasid?

1. Näita mulle punast autot
2. Näita mulle punast autot, mark Volvo ja mudel XC90, mis on pargitud kalju ääres päikeseloojangu ajal
3. Näita mulle punast autot, mark Volvo ja mudel XC90

A: 2, see on parim mall, kuna see annab üksikasju "mille kohta" ja läheb spetsiifikasse (mitte lihtsalt ükskõik milline auto, vaid konkreetne mark ja mudel) ning kirjeldab ka üldist seadet. 3 on järgmine parim, kuna see sisaldab samuti palju kirjeldust.

## 🚀 Väljakutse

Proovige kasutada "vihje" tehnikat malliga: Lõpeta lause "Näita mulle punast autot, mark Volvo ja ". Mida see vastab ja kuidas saaks seda parandada?

## Suurepärane töö! Jätkake õppimist

Kas soovite rohkem õppida erinevate mallide koostamise kontseptsioonide kohta? Minge [jätkuõppe lehele](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et leida selle teema kohta muid suurepäraseid ressursse.

Liikuge edasi õppetundi 5, kus vaatame [täiustatud mallide koostamise tehnikaid](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.