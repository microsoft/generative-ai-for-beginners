# Generatiivse tehisintellekti jõul töötavate vestlusrakenduste loomine

[![Generatiivse tehisintellekti jõul töötavate vestlusrakenduste loomine](../../../translated_images/et/07-lesson-banner.a279b937f2843833.webp)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Video vaatamiseks klõpsake ülaloleval pildil)_

Nüüd, kui oleme näinud, kuidas tekstiloomerakendusi üles ehitada, vaatame vestlusrakendusi.

Vestlusrakendused on muutunud meie igapäevaelu osaks, pakkudes enamat kui lihtsalt juhuslikku vestlusviisi. Need on lahutamatud klienditeenindusest, tehnilisest toetusest ja isegi keerukatest nõustamissüsteemidest. On tõenäoline, et saite mitte liiga kaua aega tagasi abi vestlusrakendusest. Nii kui integreerime sellesse platvormidesse tänapäevaseid tehnoloogiaid, nagu generatiivne tehisintellekt, kasvab ka keerukus ja väljakutsed.

Mõned küsimused, millele peame vastused leidma, on:

- **Rakenduse loomine**. Kuidas ehitada tõhusalt ja sujuvalt integreerida AI-jõul töötavaid rakendusi konkreetseteks kasutusjuhtudeks?
- **Jälgimine**. Kui rakendus on juurutatud, kuidas saame jälgida ja tagada nende kõrgeima kvaliteedi nii funktsionaalsuse kui ka [vastutustundliku tehisintellekti kuue põhimõtte](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) järgimise osas?

Kuna liigume aina enam automatiseerimise ja sujuvate inimese ja masina interaktsioonide ajastusse, muutub oluliseks mõista, kuidas generatiivne tehisintellekt muudab vestlusrakenduste ulatust, sügavust ja kohandatavust. See õppetund uurib arhitektuuri aspekte, mis toetavad neid keerulisi süsteeme, süveneb nende peenhäälestamise meetoditesse konkreetsete valdkondlike ülesannete jaoks ja hindab mõõdikuid ning kaalutlusi, mis on asjakohased vastutustundliku AI-lahenduse tagamiseks.

## Sissejuhatus

See õppetund käsitleb:

- Meetodeid vestlusrakenduste tõhusaks ehitamiseks ja integreerimiseks.
- Kuidas rakendada rakenduste kohandamist ja peenhäälestust.
- Strateegiaid ja kaalutlusi vestlusrakenduste tõhusaks jälgimiseks.

## Õpieesmärgid

Õppetunni lõpuks oskate:

- Kirjeldada kaalutlusi vestlusrakenduste ehitamiseks ja olemasolevatesse süsteemidesse integreerimiseks.
- Kohandada vestlusrakendusi konkreetsetele kasutusjuhtudele.
- Tuvastada olulisi mõõdikuid ja kaalutlusi AI-jõul töötavate vestlusrakenduste kvaliteedi tõhusaks jälgimiseks ja tagamiseks.
- Tagada, et vestlusrakendused kasutaksid tehisintellekti vastutustundlikult.

## Generatiivse AI integreerimine vestlusrakendustesse

Vestlusrakenduste täiustamine generatiivse tehisintellekti abil ei seisne ainult nende targemaks tegemises; see on seotud nende arhitektuuri, jõudluse ja kasutajaliidese optimeerimisega kvaliteetse kasutajakogemuse pakkumiseks. See hõlmab arhitektuuriliste alustalade, API integratsioonide ja kasutajaliidese kaalutluste uurimist. Selle osa eesmärk on pakkuda teile terviklikku teejuhti nende keeruliste maastike navigatsiooniks, olenemata sellest, kas sisestate need olemasolevatesse süsteemidesse või ehitate neid iseseisvate platvormidena.

Selle osa lõpuks omandate vajaliku teadmistepagasi vestlusrakenduste tõhusaks ülesehitamiseks ja integreerimiseks.

### Vestlusrobot või vestlusrakendus?

Enne kui sukeldume vestlusrakenduste loomisse, võrreldagem 'vestlusroboteid' ja 'AI-jõul töötavaid vestlusrakendusi', millel on erinevad rollid ja funktsioonid. Vestlusroboti peamine eesmärk on automatiseerida kindlaid vestlust ülesandeid, näiteks vastata sageli esitatavatele küsimustele või jälgida paketti. See on tavaliselt juhitud reeglipõhise loogika või keerukate tehisintellekti algoritmidega. Seevastu AI-jõul töötav vestlusrakendus on palju laiem keskkond, mis võimaldab mitut tüüpi digitaalseid suhtlusviise, näiteks tekstivestlused, häälvestlused ja videovestlused inimkasutajate vahel. Selle määravaks omaduseks on generatiivse AI mudeli integreerimine, mis simuleerib nüansirikkaid, inimlaadseid vestlusi, genereerides vastuseid laia valiku sisendi ja kontekstuaalsete vihjete põhjal. Generatiivse tehisintellekti jõul töötav vestlusrakendus suudab kaasata avatud domeeni aruteludesse, kohanduda muutuvate vestluskontekstidega ja isegi luua loomingulisi või keerukaid dialooge.

Alljärgnev tabel toob esile peamised erinevused ja sarnasused, et aidata mõista nende unikaalseid rolle digitaalses kommunikatsioonis.

| Vestlusrobot                        | Generatiivse tehisintellekti jõul töötav vestlusrakendus          |
| ---------------------------------- | --------------------------------------------------------------- |
| Ülesandekeskne ja reeglipõhine      | Kontekstitundlik                                                  |
| Sageli integreeritud suurematesse süsteemidesse | Võib majutada ühte või mitut vestlusrobotit              |
| Piiratud programmeeritud funktsioonidega         | Sisaldab generatiivseid tehisintellekti mudeleid             |
| Spetsialiseerunud ja struktureeritud interaktsioonid | Võimeline avatud domeeni aruteludeks                        |

### Eelvalmis funktsioonide kasutamine SDK-de ja API-de abil

Vestlusrakendust luues on väga hea esimene samm hinnata, mis on juba olemas. SDK-de ja API-de kasutamine vestlusrakenduste ehitamisel on kasulik mitmel põhjusel. Integreerides hästi dokumenteeritud SDK-sid ja API-sid, positsioneerite oma rakenduse strateegiliselt pikaajalise edu jaoks, lahendades skaleeritavuse ja hooldusega seotud küsimusi.

- **Arendab arendusprotsessi kiiresti ja vähendab koormust**: Eelvalmis funktsioonidele toetumine, selle asemel et neid ise kulukalt ehitada, võimaldab keskenduda rakenduse teistele olulistele aspektidele, näiteks äriloogikale.
- **Parem jõudlus**: Funktsioonide nullist ehitamisel küsid lõpuks endalt „Kuidas see skaleerub? Kas see rakendus suudab toime tulla kasutajate järsu vooga?“ Hästi hooldatud SDK-del ja API-del on sageli sisseehitatud lahendused nendele probleemidele.
- **Lihtsam hooldus**: Uuendused ja täiustused on lihtsamad hallata, kuna enamik API-sid ja SDK-sid nõuavad lihtsalt teegi uuendamist, kui ilmub uuem versioon.
- **Juurdepääs tipptasemel tehnoloogiale**: Mudelite kasutamine, mida on põhjalikult peenhäälestatud ja koolitatud mahukatel andmestikel, annab teie rakendusele loomuliku keele käsitlemise võimekuse.

SDK või API funktsionaalsuse kasutamiseks tuleb tavaliselt saada luba teenuste kasutamiseks, mis toimub sageli unikaalse võtme või autentimistempli kaudu. Me kasutame selle uurimiseks OpenAI Python teeki. Võite ise seda proovida järgnevas [OpenAI töövihikus](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) või [Azure OpenAI teenuste töövihikus](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) selle õppetunni jaoks.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

response = client.responses.create(model="gpt-5-mini", input="Suggest two titles for an instructional lesson on chat applications for generative AI.", store=False)
print(response.output_text)
```

Ülaltoodud näide kasutab GPT-5 mini mudelit koos Responses API-ga, et täita prompt, kuid pane tähele, et API võti on määratud enne seda. Kui sa võtme ei määra, saad veateate.

## Kasutajakogemus (UX)

Üldised UX põhimõtted kehtivad ka vestlusrakenduste puhul, kuid siin on mõned lisaküsimused, mis muutuvad eriti oluliseks masinõppe komponentide tõttu.

- **Ambiguiteedi lahenduse mehhanism**: Generatiivsed AI mudelid annavad mõnikord ebamääraseid vastuseid. Kasutajatel võib olla kasulik võimalus küsida täpsustusi, kui selline probleem tekib.
- **Konteksti säilitamine**: Täiustatud generatiivsete AI mudelite võime vestluse konteksti meeles pidada võib kasutajakogemuse jaoks olla vajalik omand. Kasutajatele konteksti juhtimise ja haldamise võimaldamine parandab kogemust, kuid tekitab riski tundliku kasutajateabe säilitamisel. Kaaluge, kui kaua sellist teavet hoitakse, näiteks säilituspoliitika kehtestamise teel, et tasakaalustada konteksti vajadust privaatsusega.
- **Isikupärastamine**: Õppimis- ja kohandumisvõimega AI mudelid pakuvad kasutajale individuaalset kogemust. Kasutajakogemuse kohandamine näiteks kasutajaprofiilide kaudu mitte ainult ei pane kasutajat tundma, et teda mõistetakse, vaid aitab ka kiiremini ja rahuldustpakkuvamalt leida soovitud vastuseid.

Näiteks on OpenAI ChatGPT „Kohandatud juhiste“ seaded, mis võimaldavad anda enda kohta teavet, mis võib olla tähtis teie promptide kontekstis. Siin on näide kohandatud juhisest.

![Kohandatud juhised ChatGPT-s](../../../translated_images/et/custom-instructions.b96f59aa69356fcf.webp)

See „profiil“ suunab ChatGPT looma õppetundi seotud listidest. Märka, et ChatGPT võtab arvesse, et kasutaja võib soovida põhjalikumat õppetundi oma kogemuse põhjal.

![Prompt ChatGPT-s õppetundi plaani kohta seotud listidest](../../../translated_images/et/lesson-plan-prompt.cc47c488cf1343df.webp)

### Microsofti Süsteemiteate raamistik suurte keelemudelite jaoks

[Microsoft on andnud juhiseid](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst), kuidas kirjutada tõhusaid süsteemiteateid LLM-idelt vastuste genereerimisel, mis jagunevad neljaks valdkonnaks:

1. Määratle, kelle jaoks mudel on mõeldud, ning selle võimed ja piirangud.
2. Määratle mudeli väljundvorming.
3. Esita konkreetsed näited, mis demonstreerivad mudeli soovitud käitumist.
4. Paku täiendavaid käitumise turvavöösid.

### Juurdepääsetavus

Kas kasutajal on nägemis-, kuulmis-, motoorsed või kognitiivsed puudujäägid, hästi kujundatud vestlusrakendus peaks olema kõigile kasutatav. Järgnev nimekiri toob ära spetsiifilised funktsioonid, mis parandavad juurdepääsetavust eri puuetega kasutajatele.

- **Funktsioonid nägemispuudega kasutajatele**: Kõrge kontrastsusega teemad ja muudetava suurusega tekst, ekraanilugerite tugi.
- **Funktsioonid kuulmispuudega kasutajatele**: Teksti kõneks ja kõne tekstiks funktsioonid, visuaalsed märguanded heliteavituste jaoks.
- **Funktsioonid motoorsete puuetega kasutajatele**: Klaviatuuriga navigeerimise tugi, häälkäsklused.
- **Funktsioonid kognitiivsete puuetega kasutajatele**: Lihtsustatud keelevalikud.

## Kohandamine ja peenhäälestamine valdkonnaspetsiifiliste keelemudelite jaoks

Kujutage ette vestlusrakendust, mis mõistab teie ettevõtte erikeelt ja oskab ette näha kasutajate sagedasi konkreetseid päringuid. On paar lähenemist, mida tasub mainida:

- **Valdkonnaspetsiifiliste keelemudelite kasutamine (DSL)**. DSL tähendab valdkonnaspetsiifilist keelt. Saate kasutada nn DSL-mudelit, mis on koolitatud konkreetse valdkonna mõistmiseks ja stsenaariumite töötlemiseks.
- **Peenhäälestuse rakendamine**. Peenhäälestus on protsess, mille käigus koolitate mudelit täiendavalt konkreetsete andmetega.

## Kohandamine: DSL kasutamine

Valdkonnaspetsiifiliste keelemudelite (DSL mudelid) kasutamine võib suurendada kasutajate kaasatust, pakkudes spetsialiseeritud ja kontekstuaalselt asjakohaseid interaktsioone. See mudel on koolitatud või peenhäälestatud, et mõista ja genereerida teksti, mis on seotud konkreetse valdkonna, tööstuse või teemaga. DSL mudelite kasutamise valikud võivad ulatuda nullist koolitamisest olemasolevate SDK-de ja API-de kaudu kasutamiseni. Teine võimalus on peenhäälestus, mis hõlmab olemasoleva eelkoolitatud mudeli kohandamist konkreetseks valdkonnaks.

## Kohandamine: Peenhäälestuse rakendamine

Peenhäälestamine tuleb sageli mängu siis, kui eelkoolitatud mudel jääb spetsialiseerunud valdkonnas või konkreetses ülesandes nõrgaks.

Näiteks on meditsiinilised päringud keerulised ja vajavad palju konteksti. Kui meditsiinitöötaja diagnoosib patsienti, tugineb ta mitmesugustele teguritele, nagu elustiil või olemasolevad seisundid, ning võib isegi toetuda hiljutistele meditsiiniajakirjadele diagnoosi kinnitamiseks. Sellistes nüansirohketes olukordades ei saa üldotstarbeline AI vestlusrakendus olla usaldusväärne allikas.

### Näide: meditsiinirakendus

Mõelge vestlusrakendusele, mis aitab meditsiinitöötajaid, pakkudes kiiret juurdepääsu ravijuhistele, ravimite koostoimetele või hiljutistele uurimistulemustele.

Üldotstarbeline mudel võib piisata põhilistele meditsiinilistele küsimustele vastamiseks või üldiste nõuannete pakkumiseks, kuid võib rasketeks osutuda järgnevas:

- **Väga spetsiifilised või keerukad juhtumid**. Näiteks võib neuroloog küsida rakenduselt: „Millised on praegused parimad praktikad ravimiresistentse epilepsia juhtimiseks lastel?“
- **Vajaka viimastest teadusavastustest**. Üldotstarbeline mudel võib raskustega pakkuda ajakohast vastust, mis sisaldab neuroloogia ja farmakoloogia viimatiseid arenguid.

Sellistes olukordades võib peenhäälestus spetsiaalse meditsiinilise andmestikuga oluliselt parandada mudeli võimekust käsitleda keerulisi meditsiinipäringuid täpsemini ja usaldusväärsemalt. Selleks on vaja juurdepääsu suurele ja asjakohasele andmestikule, mis esindab valdkonnaspetsiifilisi väljakutseid ja küsimusi.

## Kvaliteetse AI-põhise vestluskogemuse kaalutlused

See jaotis kirjeldab „kõrgekvaliteediliste“ vestlusrakenduste kriteeriume, mis hõlmavad tegutsemisvõimeliste mõõdikute kogumist ja raamistiku järgimist, mis vastutustundlikult kasutab tehisintellekti tehnoloogiat.

### Peamised mõõdikud

Rakenduse kõrgekvaliteedilise jõudluse tagamiseks on oluline jälgida võtmemõõdikuid ja kaalutlusi. Need mõõtmised tagavad mitte ainult rakenduse funktsionaalsuse, vaid ka hindavad AI mudeli ja kasutajakogemuse kvaliteeti. Alljärgnev nimekiri hõlmab põhimeetrikad, AI ja kasutuskogemuse mõõdikud, mida kaaluda.

| Mõõdik                       | Definitsioon                                                                                                           | Arvestused vestlusrakenduse arendajale                          |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **Tööaeg**                   | Mõõdab aega, mil rakendus on töökorras ja kasutajatele ligipääsetav.                                                    | Kuidas vähendate seisakuid?                                     |
| **Reageerimisaeg**           | Aeg, mis kulub rakendusel kasutaja päringule vastamiseks.                                                              | Kuidas optimeerite päringute töötlemist, et parandada reageerimisaega? |
| **Täpsus**                   | Tõepoolsete positiivsete ennustuste suhe kõigi positiivsete ennustuste hulgas.                                         | Kuidas valideerite mudeli täpsust?                              |
| **Kõrvaleastumine (tundlikkus)** | Tõepoolsete positiivsete ennustuste suhe tegelike positiivsete arvule.                                                    | Kuidas mõõdate ja parandate kõrvaleastumist?                   |
| **F1 skoor**                 | Täpsuse ja kõrvaleastumise harmooniline keskmine, mis tasakaalustab nende vahelised kompromissid.                      | Mis on teie siht-F1 skoor? Kuidas tasakaalustate täpsust ja kõrvaleastumist? |
| **Segadustegur**             | Mõõdab, kui hästi mudeli poolt prognoositud tõenäosusjaotus vastab tegeliku andmestiku jaotusele.                        | Kuidas vähendate segadustegurit?                               |
| **Kasutajate rahulolu mõõdikud** | Mõõdab kasutaja tajutud kogemust rakendusega. Sageli kogutakse küsitluste kaudu.                                        | Kui sageli kogute kasutajate tagasisidet? Kuidas kohandute selle põhjal? |
| **Vigade määr**              | Sagedus, mil mudel teeb mõistmis- või väljundvigu.                                                                     | Millised strateegiad teil on vigade määra vähendamiseks?       |
| **Ülekoolituskorrad**       | Kui sageli mudelit uuendatakse uute andmete ja teadmistega kohandamiseks.                                              | Kui tihti treenite mudelit uuesti? Mis käivitab uusõppe tsükli?|

| **Anomaaliate tuvastamine** | Tööriistad ja tehnikad ebatavaliste mustrite tuvastamiseks, mis ei vasta oodatud käitumisele.                        | Kuidas reageerite anomaaliatele?                                        |

### Vastutustundliku tehisintellekti tavade rakendamine vestlusrakendustes

Microsofti lähenemine vastutustundlikule tehisintellektile on tuvastanud kuus põhimõtet, mis peaksid juhima tehisintellekti arendamist ja kasutamist. Allpool on põhimõtted, nende definitsioon ning asjad, mida vestluse arendaja peaks kaaluma ja miks neid tuleks tõsiselt võtta.

| Põhimõtted          | Microsofti definitsioon                                        | Vestluse arendaja kaalutlused                                         | Miks see on oluline                                                               |
| ------------------- | ------------------------------------------------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Õiglus              | Tehisintellekti süsteemid peaksid kõiki inimesi õiglaselt kohtlema. | Tagada, et vestlusrakendus ei diskrimineeriks kasutajate andmete alusel. | Usalduse ja kaasatuse loomine kasutajate seas; väldib juriidilisi tagajärgi.     |
| Usaldusväärsus ja ohutus | Tehisintellekti süsteemid peaksid toimima usaldusväärselt ja ohutult. | Rakendada testimist ja vigadega arvestamist, et minimeerida vigu ja riske. | Tagab kasutajate rahulolu ja väldib võimalikke kahjustusi.                       |
| Privaatsus ja turvalisus | Tehisintellekti süsteemid peaksid olema turvalised ja austama privaatsust. | Rakendada tugevat krüpteerimist ja andmekaitse meetmeid.             | Tundlike kasutajaandmete kaitsmine ja privaatsusseadustele vastavus.             |
| Kaasatus            | Tehisintellekti süsteemid peaksid kõiki võimestama ja kaasama. | Kujundada kasutajaliides, mis on ligipääsetav ja lihtsasti kasutatav mitmekesisele publikule. | Tagab laiemale kasutajaskonnale rakenduse tõhusa kasutamise.                      |
| Läbipaistvus         | Tehisintellekti süsteemid peaksid olema arusaadavad.         | Pakkuda selget dokumentatsiooni ja põhjendust tehisintellekti vastuste osas. | Kasutajad usaldavad süsteemi rohkem, kui nad mõistavad, kuidas otsused tehakse. |
| Vastutus            | Inimesed peaksid vastutama tehisintellekti süsteemide eest.   | Luuakse selge protsess tehisintellekti otsuste auditeerimiseks ja parandamiseks. | Võimaldab pidevat täiustamist ja vigade korral parandusmeetmeid.                 |

## Ülesanne

Vaata [ülesannet](../../../07-building-chat-applications/python). See viib sind läbi mitme harjutuse, alustades esimeste vestluse üleskutsete käivitamisest kuni teksti klassifitseerimise ja kokkuvõtete tegemiseni ja rohkem. Märka, et ülesanded on saadaval erinevates programmeerimiskeeltes!

## Tubli töö! Jätka teekonda

Pärast selle õppetunni lõpetamist vaata meie [Generatiivse tehisintellekti õppimiskogu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et jätkata oma generatiivse tehisintellekti teadmiste taseme tõstmist!

Suundu 8. õppetundi, et näha, kuidas saad alustada [otsingurakenduste loomist](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->