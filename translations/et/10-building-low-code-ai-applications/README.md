# Vähe koodi AI rakenduste loomine

[![Vähe koodi AI rakenduste loomine](../../../translated_images/et/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Klõpsake ülaloleval pildil, et vaadata selle õppetunni videot)_

## Sissejuhatus

Nüüd, kui oleme õppinud pildigeneratsiooni rakenduste loomist, räägime vähekoodist. Generatiivset tehisintellekti saab kasutada mitmesugustes valdkondades, sealhulgas vähekoodi puhul, kuid mis on vähekood ja kuidas saame AI selle hulka lisada?

Rakenduste ja lahenduste loomine on traditsioonilistele arendajatele ja mitte-arendajatele muutunud lihtsamaks tänu Vähe Koodi Arenduse Platvormidele. Vähe Koodi Arenduse Platvormid võimaldavad teil luua rakendusi ja lahendusi vähese või üldse mitte koodiga. See saavutatakse, pakkudes visuaalset arenduskeskkonda, kus saate lohistada komponente rakenduste ja lahenduste ehitamiseks. See võimaldab teil luua rakendusi ja lahendusi kiiremini ja vähemate ressurssidega. Selles õppetunnis sukeldume sügavale, kuidas kasutada Vähe Koodi ja kuidas täiustada vähekoodi arendust AI abil Power Platvormi kaudu.

Power Platform annab organisatsioonidele võimaluse anda oma meeskondadele võimu luua oma lahendusi intuitiivse vähekoodi või üldse mitte-koodi keskkonna kaudu. See keskkond aitab lihtsustada lahenduste loomise protsessi. Power Platformiga saab lahendusi luua päevade või nädalate jooksul, mitte kuude või aastate pärast. Power Platvorm koosneb viiest võtmetoodest: Power Apps, Power Automate, Power BI, Power Pages ja Copilot Studio.

Selles õppetunnis käsitletakse:

- Sissejuhatus generatiivse AI kasutamisse Power Platvormil
- Sissejuhatus Copilot'i ja kuidas seda kasutada
- Generatiivse AI kasutamine rakenduste ja voogude ehitamiseks Power Platvormil
- AI mudelite mõistmine Power Platvormis AI Builderi abil
- Tarkade agentide loomine Microsoft Copilot Studio abil

## Õpieesmärgid

Selle õppetunni lõpuks suudate:

- Mõista, kuidas Copilot töötab Power Platvormis.

- Luua õppurite ülesannete jälgimise rakendus meie haridusettevõttele.

- Luua arve töötlemise voog, mis kasutab AI andmete väljavõtmiseks arvete põhjal.

- Rakendada parimaid tavasid GPT AI malli "Create Text" kasutamisel.

- Mõista, mis on Microsoft Copilot Studio ja kuidas luua sellega targad agentid.

Selles õppetunnis kasutatavad tööriistad ja tehnoloogiad on:

- **Power Apps**, õppurite ülesannete jälgimise rakenduse jaoks, mis pakub vähekoodi arenduskeskkonda rakenduste loomiseks andmete jälgimiseks, haldamiseks ja nendega suhtlemiseks.

- **Dataverse**, õppurite ülesannete jälgimise rakenduse andmete salvestamiseks, kus Dataverse pakub vähekoodi andmeplatvormi rakenduse andmete hoidmiseks.

- **Power Automate**, arve töötlemise voo jaoks, kus teil on vähekoodi arenduskeskkond töövoogude loomiseks arvete töötlemise protsessi automatiseerimiseks.

- **AI Builder**, arve töötlemise AI mudeli jaoks, kus kasutate eelnevalt ehitatud AI mudeleid arvete töötlemiseks meie idufirma jaoks.

## Generatiivne AI Power Platvormil

Vähekoodi arenduse ja rakenduse täiustamine generatiivse AI abil on Power Platvormi peamine fookus. Eesmärk on võimaldada kõigil luua AI-toega rakendusi, saite, armatuurlauasid ja automatiseerida protsesse AI abil, _ilma vajaduseta andmeteaduse teadmiste järele_. See eesmärk saavutatakse generatiivse AI integreerimisega vähekoodi arenduskogemusse Power Platvormil Copilot'i ja AI Builderi vormis.

### Kuidas see töötab?

Copilot on AI-assistent, mis võimaldab teil luua Power Platvormi lahendusi, kirjeldades oma nõudeid mitmes kõneluspõhises sammus loomulikus keeles. Näiteks võite juhendada oma AI-assistenti sõnastama, milliseid välju teie rakendus kasutab, ja see loob nii rakenduse kui ka aluseks oleva andmemudeli või võite täpsustada, kuidas seadistada voogu Power Automates.

Võite kasutada Copilot'i võimalusi ka oma rakenduse ekraanidel funktsioonidena, võimaldades kasutajatel avastada teadmisi vestluslike interaktsioonide kaudu.

AI Builder on Power Platvormis saadaval olev vähekoodi AI-võimekus, mis võimaldab AI mudelite abil automatiseerida protsesse ja prognoosida tulemusi. AI Builderiga saate tuua AI oma rakendustesse ja voogudesse, mis ühenduvad teie andmetega Dataverse'is või erinevates pilvandmetöötluse allikates, nagu SharePoint, OneDrive või Azure.

Copilot on saadaval kõigis Power Platvormi toodetes: Power Apps, Power Automate, Power BI, Power Pages ja Copilot Studio (endine Power Virtual Agents). AI Builder on saadaval Power Appsis ja Power Automatess. Selles õppetunnis keskendume Copilot'i ja AI Builderi kasutamisele Power Appsis ja Power Automatess, et ehitada lahendus meie haridusstartupi jaoks.

### Copilot Power Appsis

Power Apps on osa Power Platvormist ja pakub vähekoodi arenduskeskkonda rakenduste loomiseks andmete jälgimiseks, haldamiseks ja nendega suhtlemiseks. See on rakenduste arendamise teenuste komplekt koos skaleeruva andmeplatvormi ja võimalusega ühendada pilveteenuste ning kohalike andmetega. Power Apps võimaldab teil luua rakendusi, mis töötavad brauserites, tahvelarvutites ja telefonides ning mida saab jagada kolleegidega. Power Apps muudab rakenduste arendamise lihtsaks lihtsa liidese kaudu, nii et iga ärikasutaja või professionaalne arendaja saab luua kohandatud rakendusi. Rakenduse arenduse kogemust täiustatakse ka generatiivse AI abil Copilot'i kaudu.

Copilot AI assistendi funktsioon Power Appsis võimaldab teil kirjeldada, millist rakendust vajate ja millist teavet soovite oma rakenduse kaudu jälgida, koguda või kuvada. Copilot genereerib seejärel teie kirjelduse põhjal vastava Canvas-rakenduse. Seda rakendust saate seejärel vastavalt vajadusele kohandada. AI Copilot genereerib ja soovitab ka Dataverse'i tabelit koos vajalike väljadega teie jälgitavate andmete salvestamiseks ja mõningate näidisandmetega. Selles õppetunnis vaatame hiljem, mis on Dataverse ja kuidas saate seda Power Appsis kasutada. Seejärel saate tabelit vastavalt vajadustele kohandada AI Copilot assistendi funktsiooni kaudu vestluslike sammude abil. See funktsioon on hõlpsasti kättesaadav Power Apps koduekraanilt.

### Copilot Power Automatess

Power Automate, mis on osa Power Platvormist, võimaldab kasutajatel luua automatiseeritud töövooge rakenduste ja teenuste vahel. See aitab automatiseerida korduvaid äriprotsesse, nagu kommunikatsioon, andmete kogumine ja otsuste kinnitamine. Selle lihtne liides lubab iga tasemega kasutajatel (alates algajatest kuni kogenud arendajateni) automatiseerida tööülesandeid. Töövoo loomise kogemust täiustatakse ka generatiivse AI abil Copilot'i kaudu.

Copilot AI assistendi funktsioon Power Automatess võimaldab teil kirjeldada, millist töövoogu vajate ja milliseid toiminguid soovite, et teie töövoog täidaks. Copilot genereerib seejärel teie kirjelduse põhjal töövoo. Seda töövoogu saate vastavalt oma vajadustele kohandada. AI Copilot genereerib ja soovitab ka toiminguid, mida vajate soovitud töö automatiseerimiseks. Selles õppetunnis vaatame hiljem, mis on töövood ja kuidas neid Power Automatess kasutada. Seejärel saate toiminguid AI Copilot assistendi funktsiooni kaudu vestluslike sammude abil kohandada. See funktsioon on hõlpsasti kättesaadav Power Automate koduekraanilt.

## Tarkade agentide loomine Microsoft Copilot Studio abil

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst) (endine Power Virtual Agents) on Power Platvormi vähekoodi liige, mis võimaldab ehitada **AI-agente** — vestluskaaslasi, kes suudavad vastata küsimustele, võtta meetmeid ja automatiseerida ülesandeid teie kasutajate nimel. Nagu ülejäänud Power Platvorm, ehitate neid agente visuaalse, loomulikul keelel põhineva kogemuse kaudu: kirjeldage, mida agent tegema peab, ja Copilot Studio aitab juhiste, teadmiste ja toimingute skeemi koostada.

Meie haridusettevõtte jaoks võiksite ehitada agendi, kes vastab õpilaste küsimustele kursuste kohta, kontrollib ülesannete tähtaegu ja saadab isegi e-kirju juhendajale — kõik ilma koodi kirjutamata.

Siin on mõned uusimad võimalused, mis teevad Copilot Studio võimsaks:

- **Generatiivsed vastused teie teadmistest**. Selle asemel, et iga vestlust käsitsi kirjutada, saate ühendada **teadmiste allikad** — avalikud veebisaidid, SharePoint, OneDrive, Dataverse, üleslaaditud failid või ettevõtte andmed konnektorite kaudu — ja agent genereerib neist põhjendatud vastused.

- **Generatiivne orkestreerimine**. Selle asemel, et tugineda jäikadele käivitusfraasidele, kasutab agent AI-d päringu mõistmiseks ja dünaamiliselt otsustab, milliseid teadmisi, teemasid ja toiminguid kombineerida selle täitmiseks, sealhulgas mitme sammu ahelat.

- **Toimingud ja konnektorid**. Agendid saavad *tegutseda*, mitte ainult vestelda. Võite anda agendile toiminguid, mida toetavad 1500+ eelnevalt ehitatud Power Platvormi konnektorid, Power Automate vood, kohandatud REST API-d, promptid või **Model Context Protocol (MCP)** serverid.

- **Iseseisvad agendid**. Agendid ei ole piiratud vaid vestlusaknas vastamisega. Võite ehitada **iseseisvaid agente**, keda käivitavad sündmused — näiteks uus e-kiri, uus kirje Dataverse'is või faili üleslaadimine — ja kes siis taustal tegutsevad, et ülesande lõpetada.

- **Mitme agendi orkestreerimine**. Agendid saavad kutsuda teisi agente. Copilot Studio agent saab üle anda või seda laiendada teiste agentidega, sealhulgas agentidega, mis on avaldatud Microsoft 365 Copilot'is ja Microsoft Foundrys loodud agentidega.

- **Mudeli valik**. Lisaks sisseehitatud mudelitele saate tuua mudeleid Microsoft Foundry mudelikataloogist, et kohandada, kuidas teie agent mõtleb ja vastab.

- **Avalda kõikjal**. Kui agent on loodud, saab selle avaldada mitmel kanalil — Microsoft Teams, Microsoft 365 Copilot, veebisaitil või kohandatud rakenduses ja mujal — koos turvalisuse, autentimise ja analüütika haldamisega läbi Power Platvormi haldustööriistade.

Esimese agendi loomisega saate alustada aadressil [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) ja lisateavet leiate [Microsoft Copilot Studio dokumentatsioonist](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst).

## Ülesanne: Halda meie idufirma õppurite ülesandeid ja arveid, kasutades Copilot'i

Meie idufirma pakub õppuritele veebikursusi. Ettevõte on kiiresti kasvanud ja kogu nõudlusega kursustele on raske sammu pidada. Idufirma palkas teid Power Platvormi arendajana, et aidata neil luua vähekoodi lahendus õppurite ülesannete ja arvete haldamiseks. Nende lahendus peaks aitama jälgida ja hallata õppurite ülesandeid rakenduse kaudu ning automatiseerida arve töötlemise protsessi töövoo kaudu. Teil palutakse kasutada generatiivset AI-d lahenduse väljatöötamiseks.

Kui alustate Copilot'i kasutamist, võite alustada [Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) abil. See teek sisaldab nimekirja promptidest, mida saate kasutada rakenduste ja voogude loomiseks Co-pilot'iga. Võite kasutada ka teegi prompte, et saada aimu, kuidas oma nõudeid Copilot'ile kirjeldada.

### Looge meie idufirma jaoks õppurite ülesannete jälgimise rakendus

Meie idufirma haridustöötajad on vaeva näinud õppurite ülesannete jälgimisega. Nad on kasutanud tabelarvutit ülesannete jälgimiseks, kuid see on muutunud keeruliseks hallata, kui õppurite arv on kasvanud. Nad palusid teil ehitada rakendus, mis aitab neil õppurite ülesandeid jälgida ja hallata. Rakendus peaks võimaldama lisada uusi ülesandeid, vaadata ülesandeid, uuendada ülesandeid ja kustutada ülesandeid. Rakendus peaks samuti võimaldama haridustöötajatel ja õppuritel vaadata hinnatud ja hindamata ülesandeid.

Loote rakenduse Copilot'i abil Power Appsis järgides alljärgnevaid samme:

1. Navigeerige [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) avakuvale.

1. Kasutage avakuval tekstiala rakenduse kirjeldamiseks, mida soovite luua. Näiteks **_Ma tahan luua rakendust, et jälgida ja hallata õppurite ülesandeid_**. Klõpsake AI Copilot'ile prompti saatmiseks nuppu **Saada**.

![Kirjeldage rakendust, mida soovite luua](../../../translated_images/et/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. AI Copilot soovitab Dataverse'i tabelit koos vajalike väljadega teie jälgitavate andmete salvestamiseks ja mõningate näidisandmetega. Seejärel saate tabelit kohandada vastavalt oma vajadustele AI Copilot assistendi funktsiooni kaudu vestluslike sammude abil.

   > **Tähtis**: Dataverse on Power Platvormi aluseks olev andmeplatvorm. See on vähekoodi andmeplatvorm rakenduse andmete hoidmiseks. See on täielikult hallatav teenus, mis salvestab andmeid turvaliselt Microsofti pilves ning on teie Power Platvormi keskkonnas. Sellega kaasnevad sisseehitatud andmehalduskeskused, nagu andmete klassifikatsioon, päritolu jälgimine, peenhäälestatud juurdepääsukontroll ja palju muud. Lisateavet Dataverse'i kohta leiate [siit](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Uue tabeli soovitatud väljad](../../../translated_images/et/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. Haridustöötajad soovivad saata e-kirju õppuritele, kes on ülesanded esitanud, et hoida neid kursis ülesannete edenemisega. Võite kasutada Copilot'i, et lisada tabelisse uus veerg õppuri e-posti aadressi salvestamiseks. Näiteks võite kasutada järgmist prompti: **_Ma tahan lisada veeru õppuri e-posti salvestamiseks_**. Klõpsake AI Copilot'ile prompti saatmiseks nuppu **Saada**.

![Uue välja lisamine](../../../translated_images/et/copilot-new-column.35e15ff21acaf274.webp)

1. AI Copilot genereerib uue välja ja seejärel saate välja kohandada vastavalt oma vajadustele.


1. Kui olete tabeli koostamisega lõpetanud, klõpsake rakenduse loomiseks nuppu **Create app**.

1. AI Copilot loob teie kirjelduse põhjal reageeriva Canvas rakenduse. Seejärel saate rakendust oma vajadustele kohandada.

1. Õpetajate jaoks, kes soovivad saata õpilastele e-kirju, saate Copiloti abil rakendusele uue ekraani lisada. Näiteks võite järgmise juhise abil rakendusele ekraani lisada: **_Ma tahan lisada ekraani õpilastele e-kirjade saatmiseks_**. Klõpsake juhise saatmiseks AI Copilotile nuppu **Send**.

![Uue ekraani lisamine juhise abil](../../../translated_images/et/copilot-new-screen.2e0bef7132a17392.webp)

1. AI Copilot loob uue ekraani ja seejärel saate seda vastavalt oma vajadustele kohandada.

1. Kui olete rakendusega valmis, klõpsake selle salvestamiseks nuppu **Save**.

1. Rakenduse õpetajatega jagamiseks klõpsake nuppu **Share** ja seejärel uuesti nuppu **Share**. Seejärel saate rakenduse jagada, sisestades nende e-posti aadressid.

> **Teie ülesanne**: äsjavalminud rakendus on hea algus, kuid seda saab täiustada. E-posti funktsiooni puhul saavad õpetajad saata e-kirju õpilastele käsitsi, sisestades nende e-posti aadresse. Kas saate Copiloti abil luua automatiseerimise, mis võimaldab õpetajatel saata e-kirju õpilastele automaatselt, kui nad esitlevad oma ülesandeid? Teie vihje on, et õige juhise abil saate Copiloti kasutada Power Automate'is selle ülesande lahendamiseks.

### Arendame meie idufirmale arvete info tabeli

Meie idufirma finantstiim on vaeva näinud arvete jälgimisega. Nad on kasutanud arvete jälgimiseks kalkuleerimislehte, kuid kui arvete arv on kasvanud, on hakanud see muutuma raskesti hallatavaks. Nad palusid teil üles ehitada tabel, mis aitab neil salvestada, jälgida ja hallata saabunud arvete andmeid. Tabelit tuleks kasutada automatiseerimise loomiseks, mis tõmbab kõik arveandmed välja ja salvestab need tabelisse. Samuti peaks tabel võimaldama finantstiimil näha, millised arved on tasutud ja millised mitte.

Power Platform sisaldab aluseks olevat andmeplatvormi nimega Dataverse, mis võimaldab teil oma rakenduste ja lahenduste andmeid talletada. Dataverse pakub madala koodiga andmeplatvormi rakenduseandmete salvestamiseks. See on täielikult hallatav teenus, mis turvaliselt salvestab andmed Microsofti pilves ja mis on häälestatud teie Power Platformi keskkonnas. See sisaldab sisseehitatud andmevalitsemise funktsioone, nagu andmete klassifikatsioon, andmejoonised, peenhäälestatud juurdepääsukontroll jpm. Lisateavet saate lugeda [Dataverse'i kohta siit](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Miks peaksime meie idufirma jaoks kasutama Dataverse'i? Dataverse'i standard- ja kohandatud tabelid pakuvad teie andmete turvalist ja pilvepõhist salvestusvõimalust. Tabelid võimaldavad talletada erinevat tüüpi andmeid, sarnaselt mitme töölehe kasutamisele ühes Exceli töövihikus. Tabelid võimaldavad teil salvestada andmeid, mis on spetsiifilised teie organisatsiooni või ettevõtte vajadustele. Mõned eelised, mida meie idufirma Dataverse'i kasutamisest saab, on järgmised, kuid mitte ainult:

- **Lihtne hallata**: nii metaandmed kui ka andmed salvestatakse pilves, nii et te ei pea muretsema nende salvestamise ega haldamise detailide pärast. Võite keskenduda oma rakenduste ja lahenduste loomisele.

- **Turvaline**: Dataverse pakub teie andmete jaoks turvalist ja pilvepõhist salvestusvõimalust. Te saate kontrollida, kes pääseb teie tabelite andmetele ligi ja kuidas nad sellele ligi pääsevad, kasutades rollipõhist turvalisust.

- **Rikkalikud metaandmed**: andmetüübid ja -seosed on kasutatavad otse Power Appsis.

- **Loogika ja valideerimine**: ärireeglite, arvutatud väljade ja valideerimisreeglite abil saate rakendada äriloogikat ja tagada andmete täpsuse.

Nüüd, kui teate, mis on Dataverse ja miks seda kasutada, vaatame, kuidas saate Copiloti abil Dataverse'i tabeli luua meie finantstiimi vajaduste jaoks.

> **Märkus** : Järgmises osas kasutate seda tabelit automatiseerimise loomiseks, mis tõmbab kõik arveandmed välja ja salvestab need tabelisse.

Dataverse'is tabeli loomiseks Copiloti abil järgige alltoodud samme:

1. Minge [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) avalehele.

2. Vasakul navigeerimisribalt valige **Tables** ja seejärel klõpsake **Describe the new Table**.

![Vali uus tabel](../../../translated_images/et/describe-new-table.0792373eb757281e.webp)

1. Ekraanil **Describe the new Table** kasutage tekstiala, et kirjeldada loodavat tabelit. Näiteks: **_Ma tahan luua tabeli arveandmete salvestamiseks_**. Klõpsake juhise AI Copilotile saatmiseks nuppu **Send**.

![Kirjelda tabelit](../../../translated_images/et/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. AI Copilot pakub välja Dataverse tabeli koos väljadega, mida vajate andmete salvestamiseks, mida soovite jälgida, ning mõningate näidandmetega. Seejärel saate kasutades AI Copiloti vestlusassistendi funktsiooni tabelit vastavalt vajadusele kohandada.

![Soovitatud Dataverse tabel](../../../translated_images/et/copilot-dataverse-table.b3bc936091324d9d.webp)

1. Finantstiim soovib saata tarnijale e-kirja, et neid teavitada arve hetkeseisust. Copiloti abil saate tabelile uue välja lisada, kuhu salvestada tarnija e-posti aadress. Näiteks võite kasutada järgmist juhist: **_Ma tahan lisada veeru tarnija e-posti salvestamiseks_**. Klõpsake juhise saatmiseks AI Copilotile nuppu **Send**.

1. AI Copilot lisab uue välja ja seejärel saate seda vastavalt vajadusele kohandada.

1. Kui olete tabeli koostamise lõpetanud, klõpsake tabeli loomiseks nuppu **Create**.

## AI mudelid Power Platformis AI Builderiga

AI Builder on madala koodiga tehisintellekti võimekus Power Platformis, mis võimaldab kasutada AI-mudeleid protsesside automatiseerimiseks ja tulemuste ennustamiseks. AI Builderiga saate lisada tehisintellekti oma rakendustesse ja voogudesse, mis ühenduvad teie andmetega Dataverse'is või erinevates pilvandmeallikates, nagu SharePoint, OneDrive või Azure.

## Eelnevalt valmis AI mudelid vs kohandatud AI mudelid

AI Builder pakub kahte tüüpi AI mudeleid: eelnevalt valmiskujundatud AI mudelid ja kohandatud AI mudelid. Eelnevalt valmiskujundatud mudelid on Microsofti treenitud ja Power Platformis valmis kasutamiseks. Need aitavad teil lisada oma rakendustele ja voogudele intelligentsust ilma, et peaksite ise andmeid koguma ning oma mudeleid looma, treenima ja avaldama. Nende mudelite abil saate automatiseerida protsesse ja ennustada tulemusi.

Mõned eelnevalt valmis AI mudelid, mis on Power Platformis saadaval:

- **Põhiväljendite väljavõtmine**: see mudel väljastab tekstist põhilised väljendid.
- **Keele tuvastamine**: see mudel tuvastab tekstikeele.
- **Sentimendi analüüs**: see mudel tuvastab teksti positiivse, negatiivse, neutraalse või segatud meeleolu.
- **Visiitkaardi lugeja**: see mudel väljastab infot visiitkaartidelt.
- **Teksti äratundmine**: see mudel loeb tekstipilte.
- **Objektide tuvastamine**: see mudel tuvastab ja eraldab objekte piltidelt.
- **Dokumentide töötlemine**: see mudel väljastab infot vormidelt.
- **Arvete töötlemine**: see mudel väljastab infot arvete põhjal.

Kohandatud AI mudelitega saate tuua AI Builderisse oma mudeli, mis töötab nagu iga AI Builderi kohandatud mudel, võimaldades teil mudelit treenida oma andmete abil. Neid mudeleid saab kasutada nii Power Appsis kui ka Power Automates protsesside automatiseerimiseks ja tulemuste ennustamiseks. Oma mudeli kasutamisel kehtivad piirangud. Loe lisaks nendest [piirangutest](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![AI Builderi mudelid](../../../translated_images/et/ai-builder-models.8069423b84cfc47f.webp)

## Ülesanne #2 - arendage meie idufirma jaoks arve töötlemise voog

Finantstiim on vaeva näinud arvete töötlemisega. Nad on kasutanud arvete jälgimiseks kalkuleerimislehte, kuid suure arvearvu tõttu on see muutunud raskesti hallatavaks. Nad palusid teil luua töövoog, mis aitab neil AI abil arveid töödelda. Töövoog peaks võimaldama neil arveldokumentidest info välja võtta ja salvestada see Dataverse'i tabelisse. Samuti peaks töövoog võimaldama saata ekstraktitud teabega e-kirja finantstiimile.

Nüüd, kui teate, mis on AI Builder ja miks kasutada, vaatame, kuidas kasutada varem käsitletud arve töötlemise AI mudelit AI Builderis, et arendada töövoog, mis aitab finantstiimil arveid töödelda.

Arve töötlemiseks AI mudelit kasutava töövoo loomiseks järgige alljärgnevaid samme:

1. Minge [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst) avalehele.

2. Kasutage avalehel tekstiala, et kirjeldada loomist soovitud töövoogu. Näiteks: **_Töötle arve, kui see jõuab minu postkasti_**. Klõpsake juhise AI Copilotile saatmiseks nuppu **Send**.

   ![Copilot power automate](../../../translated_images/et/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. AI Copilot pakub ülesande täitmiseks vajalikke samme. Klõpsake edasiliikumiseks nuppu **Next**.

4. Järgmisel sammul kutsub Power Automate teid üles seadistama ühendused, mida voog vajab. Kui olete lõpetanud, klõpsake nuppu **Create flow**, et voog luua.

5. AI Copilot loob voo ning saate seda vastavalt oma vajadustele kohandada.

6. Uuendage voo käivitajat, seadistades kaustaks selle kausta, kuhu arved salvestatakse. Näiteks seadistage kaustaks **Inbox**. Klõpsake **Show advanced options** ja seadistage **Only with Attachments** väärtuseks **Yes**. See tagab, et voog töötab ainult siis, kui kaustas saabub manus.

7. Eemaldage voost järgmised toimingud: **HTML to text**, **Compose**, **Compose 2**, **Compose 3** ja **Compose 4**, sest neid te ei kasuta.

8. Eemaldage voost ka toiming **Condition**, sest seda te ei kasuta. See peaks välja nägema nagu järgmises ekraanipildis:

   ![power automate, eemalda toimingud](../../../translated_images/et/powerautomate-remove-actions.7216392fe684ceba.webp)

9. Klõpsake nuppu **Add an action** ja otsige **Dataverse**. Valige toiming **Add a new row**.

10. Toimingus **Extract Information from invoices** seadistage **Invoice File** viitama e-kirja manuselt pärit **Attachment Content** peale. See tagab, et voog tõmbab info välja arve manuselt.

11. Valige tabel, mille varem lõite. Näiteks võite valida tabeli **Invoice Information**. Täitke alljärgnevad väljad eelneva toimingu dünaamilise sisuga:

    - ID
    - Summa
    - Kuupäev
    - Nimi
    - Staatus - seadistage **Status** väärtuseks **Pending**.
    - Tarnija e-post - kasutage dünaamilist sisu **From** **When a new email arrives** käivitajast.

    ![power automate lisa rida](../../../translated_images/et/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. Kui voog on lõplikult valmis, klõpsake selle salvestamiseks nuppu **Save**. Voo testimiseks saatke e-kiri arvega kausta, mille varem käivitajas määrasite.

> **Teie ülesanne**: äsjaloodud voog on hea algus, nüüd peate välja mõtlema, kuidas luua automatiseerimine, mis võimaldab meie finantstiimil saata tarnijale e-kirja, et neid teavitada arve hetkeseisust. Vihje: voog peab käivituma siis, kui arve staatus muutub.

## Kasutage Power Automate’is tekstigeneratsiooni AI mudelit

AI Builderi GPT mudel Create Text võimaldab teil teksti genereerida juhise põhjal ning töötab Microsoft Azure OpenAI teenusega. Selle võimekuse abil saate integreerida GPT (Generative Pre-Trained Transformer) tehnoloogia oma rakendustesse ja voogudesse, luues mitmesuguseid automatiseeritud voo ja tarkarakendusi.

GPT mudelid käivad läbi põhjaliku treeningu suurte andmehulkadega, võimaldades neil genereerida teksti, mis sarnaneb inimkeelele, kui neile antakse juhis. Töövoo automatiseerimisse ühendatuna saab GPT-tüüpi AI mudeleid kasutada paljude ülesannete efektiivseks automatiseerimiseks.

Näiteks saate luua vooge, mis automaatselt genereerivad tekste mitmesugusteks eesmärkideks, nagu e-kirjade mustandid, toodete kirjeldused jms. Mudelit saate kasutada ka näiteks vestlusrobotites ja klienditeeninduse rakendustes, võimaldades tugispetsialistidel tõhusamalt ja kiiremini vastata klientide päringutele.

![loo juhis](../../../translated_images/et/create-prompt-gpt.69d429300c2e870a.webp)


Selle AI-mudeli kasutamise õppimiseks Power Automates, vaadake läbi [Lisa intelligentsust AI Builderi ja GPT abil](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko) moodul.

## Suurepärane töö! Jätka õppimist

Pärast selle õppetüki läbimist vaata meie [Generatiivse AI õppimise kollektsiooni](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), et jätkata oma generatiivse AI teadmiste tõstmist!

Kas soovid kohandada ja saada Copilotist rohkem kasu? Avastage [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) — kogukonna panustatud juhiste, agentide, oskuste ja konfiguratsioonide kogu, mis aitab teil GitHub Copilotist maksimumi võtta.

Liigu õppetüki 11 juurde, kus vaatame, kuidas [integreerida generatiivset AI funktsioonikõnega](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->