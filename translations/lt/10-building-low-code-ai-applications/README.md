# Žemo Kodo AI Programėlių Kūrimas

[![Žemo Kodo AI Programėlių Kūrimas](../../../translated_images/lt/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Paspauskite aukščiau esančią nuotrauką, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

## Įvadas

Dabar, kai sužinojome, kaip kurti vaizdą generuojančias programėles, pakalbėkime apie žemą kodą. Sugeneruojamasis AI gali būti naudojamas įvairiose srityse, įskaitant žemą kodą, bet kas yra žemas kodas ir kaip mes galime pridėti AI prie jo?

Programėlių ir sprendimų kūrimas tapo lengvesnis tiek tradiciniams kūrėjams, tiek neprogramuotojams naudojant žemo kodo kūrimo platformas. Žemo kodo kūrimo platformos leidžia kurti programėles ir sprendimus su mažu ar visai be kodo. Tai pasiekiama suteikiant vizualią kūrimo aplinką, kurioje galite vilkti ir mesti komponentus, kad kurtumėte programėles ir sprendimus. Tai leidžia kurti programas ir sprendimus greičiau ir sunaudojant mažiau resursų. Šioje pamokoje gilinsimės, kaip naudoti žemą kodą ir kaip pagerinti žemo kodo kūrimą su AI naudojant Power Platformą.

Power Platform suteikia organizacijoms galimybę įgalinti jų komandas kurti savo sprendimus naudojant intuityvią žemo arba be kodo aplinką. Ši aplinka padeda supaprastinti sprendimų kūrimo procesą. Naudojant Power Platform sprendimai gali būti kuriami per dienas ar savaites vietoje mėnesių ar metų. Power Platform susideda iš penkių pagrindinių produktų: Power Apps, Power Automate, Power BI, Power Pages ir Copilot Studio.

Šioje pamokoje aptariama:

- Įvadas į generuojamąjį AI Power Platformoje
- Įvadas į Copilot ir kaip jį naudoti
- Generuojamojo AI naudojimas kuriant programėles ir srautus Power Platformoje
- AI modelių supratimas Power Platformoje naudojant AI Builder
- Protingų agentų kūrimas su Microsoft Copilot Studio

## Mokymosi tikslai

Iki šios pamokos pabaigos jūs sugebėsite:

- Suprasti, kaip veikia Copilot Power Platformoje.

- Sukurti Studentų Užduočių Sekimo programėlę mūsų švietimo startuoliui.

- Sukurti Sąskaitų Apdorojimo srautą, kuris naudoja AI informacijai iš sąskaitų išgauti.

- Taikyti geriausias praktikas naudojant GPT AI modelį „Create Text“.

- Suprasti, kas yra Microsoft Copilot Studio ir kaip su juo kurti protingus agentus.

Šios pamokos metu naudosite šiuos įrankius ir technologijas:

- **Power Apps** — Studentų Užduočių Sekimo programėlei kurti, kuri suteikia žemo kodo kūrimo aplinką programėlių kūrimui, skirtų duomenų sekimui, valdymui ir sąveikai.

- **Dataverse** — duomenų saugojimui Studentų Užduočių Sekimo programėlėje. Dataverse suteikia žemo kodo duomenų platformą programėlės duomenų saugojimui.

- **Power Automate** — Sąskaitų Apdorojimo srautui, kur turėsite žemo kodo kūrimo aplinką darbo procesų kūrimui, automatizuojančiam sąskaitų apdorojimo procesą.

- **AI Builder** — Sąskaitų Apdorojimo AI modeliui, kur naudosite iš anksto sukurtus AI modelius mūsų startuolio sąskaitoms apdoroti.

## Generuojamasis AI Power Platformoje

Žemo kodo kūrimo ir programėlių pagerinimas naudojant generuojamąjį AI yra svarbiausia Power Platformos kryptis. Tikslas - suteikti galimybę visiems kurti AI palaikomas programėles, svetaines, informacijos suvestines ir automatizuoti procesus su AI, _nereikalaujant jokios duomenų mokslo patirties_. Šis tikslas pasiekiamas integruojant generuojamąjį AI į žemo kodo kūrimo patirtį Power Platformoje per Copilot ir AI Builder.

### Kaip tai veikia?

Copilot yra AI asistentas, leidžiantis jums kurti Power Platform sprendimus aprašant savo reikalavimus serija pokalbių etapų natūralia kalba. Pavyzdžiui, galite nurodyti savo AI asistentui pasakyti, kokius laukus naudos jūsų programėlė, ir jis sukurs tiek programėlę, tiek pagrindinį duomenų modelį, arba galite nurodyti, kaip sukurti srautą Power Automate.

Galite naudoti Copilot funkcijas kaip funkciją savo programėlės ekranuose, leidžiančią vartotojams atrasti įžvalgas per pokalbius.

AI Builder yra žemo kodo AI galimybė Power Platformoje, leidžianti naudoti AI modelius, kad padėtų automatizuoti procesus ir prognozuoti rezultatus. Su AI Builder galite įtraukti AI į savo programėles ir srautus, kurie jungiasi prie jūsų duomenų Dataverse arba įvairiuose debesų duomenų šaltiniuose, tokiuose kaip SharePoint, OneDrive ar Azure.

Copilot yra prieinamas visuose Power Platform produktuose: Power Apps, Power Automate, Power BI, Power Pages ir Copilot Studio (anksčiau Power Virtual Agents). AI Builder yra prieinamas Power Apps ir Power Automate. Šioje pamokoje mes sutelksime dėmesį, kaip naudoti Copilot ir AI Builder Power Apps ir Power Automate programose, kad sukurtume sprendimą mūsų švietimo startuoliui.

### Copilot Power Apps

Kaip Power Platform dalis, Power Apps suteikia žemo kodo kūrimo aplinką programėlių kūrimui, skirtų duomenų sekimui, valdymui ir sąveikai. Tai programėlių kūrimo paslaugų komplektas su plečiamąja duomenų platforma ir galimybe jungtis prie debesų paslaugų ir vietinių duomenų šaltinių. Power Apps leidžia kurti programas, kurios veikia naršyklėse, planšetėse ir telefonuose, ir kurias galima dalintis su kolegomis. Power Apps palengvina programėlių kūrimą vartotojams paprasta sąsaja, todėl kiekvienas verslo vartotojas ar profesionalus kūrėjas gali sukurti pasirinktines programėles. Programėlių kūrimo patirtis taip pat pagerinta generuojamuoju AI per Copilot.

Copilot AI asistento funkcija Power Apps leidžia jums aprašyti, kokio tipo programėlę jums reikia ir kokią informaciją norite, kad jūsų programėlė sektų, rinktų arba rodytų. Tada Copilot sugeneruoja reaguojančią Canvas programėlę pagal jūsų aprašymą. Po to galite pritaikyti programėlę savo poreikiams. AI Copilot taip pat generuoja ir siūlo Dataverse lentelę su laukais, kurių reikia jūsų norimiems sekamiems duomenims saugoti, taip pat pateikia pavyzdinius duomenis. Šioje pamokoje vėliau aptarsime, kas yra Dataverse ir kaip galite jį naudoti Power Apps. Tada galite pritaikyti lentelę savo poreikiams naudodami AI Copilot asistento funkciją per pokalbio žingsnius. Ši funkcija yra lengvai prieinama iš Power Apps pradžios ekrano.

### Copilot Power Automate

Kaip Power Platform dalis, Power Automate leidžia vartotojams kurti automatizuotus darbo srautus tarp programėlių ir paslaugų. Jis padeda automatizuoti pasikartojančius verslo procesus, tokius kaip komunikacija, duomenų rinkimas ir sprendimų patvirtinimai. Jo paprasta sąsaja leidžia vartotojams bet kokio techninio lygio (nuo pradedančiųjų iki patyrusių kūrėjų) automatizuoti darbo užduotis. Darbo srautų kūrimo patirtis taip pat pagerinta generuojamuoju AI per Copilot.

Copilot AI asistento funkcija Power Automate leidžia jums aprašyti, kokio tipo srauto jums reikia ir kokius veiksmus norite, kad srautas atliktų. Tada Copilot sugeneruoja srautą pagal jūsų aprašymą. Po to galite pritaikyti srautą savo poreikiams. AI Copilot taip pat generuoja ir siūlo veiksmus, kuriuos reikia atlikti užduočiai automatizuoti. Šioje pamokoje vėliau aptarsime, kas yra srautai ir kaip juos naudoti Power Automate. Tada galite pritaikyti veiksmus savo poreikiams naudodami AI Copilot asistento funkciją per pokalbio žingsnius. Ši funkcija yra lengvai prieinama iš Power Automate pradžios ekrano.

## Protingų agentų kūrimas su Microsoft Copilot Studio

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst) (anksčiau Power Virtual Agents) yra žemo kodo Power Platform narys, skirtas kurti **AI agentus** — pokalbių palydovus, galinčius atsakyti į klausimus, atlikti veiksmus ir automatizuoti užduotis jūsų vartotojams. Kaip ir visa Power Platform, šiuos agentus kuriate vizualioje, natūralios kalbos prioritetą teikiančioje patirtyje: jūs aprašote, ką norite, kad agentas darytų, o Copilot Studio padeda struktūrizuoti jo nurodymus, žinias ir veiksmus.

Mūsų švietimo startuoliui galite sukurti agentą, kuris atsako į studentų klausimus apie kursus, tikrina užduočių terminus ir net siunčia elektroninius laiškus dėstytojui — visa tai nerašant kodo.

Štai keletas naujausių funkcijų, kurios daro Copilot Studio galingą:

- **Generuojami atsakymai iš jūsų žinių**. Vietoj to, kad rašytumėte kiekvieną pokalbį rankomis, galite prijungti **žinių šaltinius** — viešas svetaines, SharePoint, OneDrive, Dataverse, įkeltus failus ar įmonės duomenis per jungtis — ir agentas generuoja pagrįstus atsakymus iš jų.

- **Generuojama orkestracija**. Vietoj griežtų pažadinimo frazių agentas naudoja AI, kad suprastų užklausą ir dinamiškai nuspręstų, kurią informaciją, temas ir veiksmus derinti, įskaitant kelių žingsnių sujungimą.

- **Veiksmai ir jungtys**. Agentai gali *daryti* dalykus, ne tik pokalbius. Galite suteikti agentui veiksmus, remiamus daugiau nei 1,500 iš anksto sukurtų Power Platform jungčių, Power Automate srautų, pasirinktinių REST API, užklausų arba **Model Context Protocol (MCP)** serverių.

- **Autonominiai agentai**. Agentai nėra ribojami tik pokalbių lange atsakyti. Galite kurti **autonominius agentus**, kurie yra paleidžiami įvykių — pavyzdžiui, naujo el. laiško, įrašo Dataverse arba failo įkėlimo — ir tada veikia fone, kad užbaigtų užduotį.

- **Daugiagentinė orkestracija**. Agentai gali kviesti kitus agentus. Copilot Studio agentas gali perduoti arba būti papildytas kitų agentų, įskaitant agentus, paskelbtus Microsoft 365 Copilot, ir agentus, sukurtus Microsoft Foundry.

- **Modelių pasirinkimas**. Be įmontuotų modelių, galite įtraukti modelius iš Microsoft Foundry modelių katalogo, kad pritaikytumėte, kaip jūsų agentas mąsto ir atsako.

- **Publikavimas bet kur**. Sukurtas agentas gali būti publikuojamas keliose kanalų vietose — Microsoft Teams, Microsoft 365 Copilot, svetainėje arba pasirinktoje programėlėje ir kt. — su saugumo, autentifikavimo ir analizės valdymu per Power Platform administravimo patirtį.

Galite pradėti kurti savo pirmąjį agentą adresu [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) ir sužinoti daugiau [Microsoft Copilot Studio dokumentacijoje](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst).

## Užduotis: valdyti studentų užduotis ir sąskaitas mūsų startuoliui, naudojant Copilot

Mūsų startuolis teikia internetinius kursus studentams. Startuolis sparčiai išaugo ir dabar sunkiai spėja tenkinti kursų paklausą. Startuolis samdė jus kaip Power Platform kūrėją, kad padėtumėte sukurti žemo kodo sprendimą, kuris padėtų jiems valdyti studentų užduotis ir sąskaitas. Jų sprendimas turėtų padėti stebėti ir valdyti studentų užduotis per programėlę ir automatizuoti sąskaitų apdorojimą per darbo srautą. Jums buvo paprašyta naudoti generuojamąjį AI sprendimui sukurti.

Pradedant naudoti Copilot, galite naudoti [Power Platform Copilot Prompt Library](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko), kad pradėtumėte su užklausomis. Ši biblioteka sudaro užklausų sąrašą, kuriomis galite naudotis kuriant programas ir srautus su Copilot. Taip pat galite naudoti bibliotekos užklausas, kad gautumėte idėją, kaip aprašyti savo reikalavimus Copilot.

### Sukurkite Studentų Užduočių Sekimo Programėlę Mūsų Startuoliui

Mūsų startuolio pedagogai sunkiai sekė studentų užduotis. Jie naudojo skaičiuoklę užduotims sekti, bet tai tapo sunku valdyti, kadangi studentų skaičius išaugo. Jie paprašė jūsų sukurti programėlę, kuri padėtų sekti ir valdyti studentų užduotis. Programėlė turėtų leisti pridėti naujas užduotis, peržiūrėti užduotis, atnaujinti užduotis ir ištrinti užduotis. Programėlė taip pat turėtų leisti pedagogams ir studentams peržiūrėti užduotis, kurios jau įvertintos, ir tas, kurios dar neįvertintos.

Programėlę kursite naudodami Copilot Power Apps pagal toliau nurodytus žingsnius:

1. Eikite į [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) pradžios ekraną.

1. Naudokite teksto sritį pradžios ekrane, kad aprašytumėte programėlę, kurią norite sukurti. Pavyzdžiui, **_Noriu sukurti programėlę studentų užduočių sekimui ir valdymui_**. Paspauskite **Siųsti** mygtuką, kad išsiųstumėte užklausą AI Copilot.

![Aprašykite programėlę, kurią norite kurti](../../../translated_images/lt/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. AI Copilot pasiūlys Dataverse lentelę su laukais, kurių jums reikia norint saugoti norimus sekti duomenis, ir kai kuriuos pavyzdinius duomenis. Tada galite pritaikyti lentelę pagal savo poreikius naudodami AI Copilot asistento funkciją per pokalbio žingsnius.

   > **Svarbu**: Dataverse yra pagrindinė duomenų platforma Power Platformoje. Tai žemo kodo duomenų platforma, skirta programėlės duomenų saugojimui. Tai pilnai valdoma paslauga, kuri saugiai saugo duomenis Microsoft debesyje ir yra įdiegta jūsų Power Platform aplinkoje. Ji turi įmontuotas duomenų valdymo funkcijas, tokias kaip duomenų klasifikacija, duomenų kilmė, detali prieigos kontrolė ir kt. Apie Dataverse galite sužinoti daugiau [čia](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Siūlomi laukai jūsų naujoje lentelėje](../../../translated_images/lt/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. Pedagogai nori siųsti el. laiškus studentams, kurie pateikė savo užduotis, kad juos informuotų apie užduočių eigą. Galite naudoti Copilot, kad pridėtumėte naują lauką lentelėje, skirtą studento el. pašto saugojimui. Pavyzdžiui, galite naudoti šią užklausą, kad pridėtumėte naują lauką: **_Noriu pridėti stulpelį studento el. paštui saugoti_**. Paspauskite **Siųsti** mygtuką, kad išsiųstumėte užklausą AI Copilot.

![Naujo lauko pridėjimas](../../../translated_images/lt/copilot-new-column.35e15ff21acaf274.webp)

1. AI Copilot sugeneruos naują lauką, kurį tada galėsite pritaikyti pagal savo poreikius.


1. Baigę darbą su lentele, spustelėkite mygtuką **Create app**, kad sukurtumėte programėlę.

1. AI „Copilot“ generuos reaguojančią Canvas programėlę pagal jūsų aprašymą. Tuomet galite pritaikyti programėlę pagal savo poreikius.

1. Mokytojams, norintiems siųsti el. laiškus mokiniams, galite naudoti „Copilot“, kad pridėtumėte naują ekraną programėlėje. Pavyzdžiui, galite naudoti šį užklausos tekstą, norėdami pridėti naują ekraną programėlėje: **_Noriu pridėti ekraną el. laiškams mokiniams siųsti_**. Spustelėkite mygtuką **Send**, kad siųstumėte užklausą AI „Copilot“.

![Adding a new screen via a prompt instruction](../../../translated_images/lt/copilot-new-screen.2e0bef7132a17392.webp)

1. AI „Copilot“ sugeneruos naują ekraną, kurį vėliau galėsite pritaikyti pagal savo poreikius.

1. Baigę darbą su programėle, spustelėkite mygtuką **Save**, kad išsaugotumėte programėlę.

1. Norėdami pasidalinti programėle su mokytojais, spustelėkite mygtuką **Share**, o tada vėl spustelėkite mygtuką **Share**. Tuomet įveskite jų el. pašto adresus, kad pasidalintumėte programėle su mokytojais.

> **Jūsų namų darbas**: Ką tik sukurta programėlė yra geras pradžia, tačiau ją galima patobulinti. Su el. pašto funkcija mokytojai gali siųsti el. laiškus mokiniams tik rankiniu būdu, įvesdami jų el. pašto adresus. Ar galite naudodami „Copilot“ sukurti automatizaciją, kuri leistų mokytojams automatiškai siųsti el. laiškus mokiniams, kai šie pateikia savo užduotis? Užuomina – tinkamu užklausa galite naudoti „Copilot“ Power Automate platformoje šiam tikslui įgyvendinti.

### Sukurkite sąskaitų informacijos lentelę mūsų startuoliui

Mūsų startuolio finansų komanda sunkiai sekė sąskaitas. Jie naudojosi skaičiuokle, kad sekytų sąskaitas, tačiau tai tapo sudėtinga tvarkyti augant sąskaitų skaičiui. Jie paprašė jūsų sukurti lentelę, kuri padėtų saugoti, sekti ir valdyti gautų sąskaitų informaciją. Lentelė turėtų būti naudojama automatizacijai kurti, kuri ištrauktų visą sąskaitų informaciją ir saugotų ją lentelėje. Taip pat lentelė turi leisti finansų komandai matyti, kurios sąskaitos buvo apmokėtos ir kurios ne.

Power Platform pagrindą sudaro duomenų platforma Dataverse, kuri leidžia saugoti duomenis jūsų programėlėms ir sprendimams. Dataverse suteikia mažo kodo duomenų platformą programėlių duomenų saugojimui. Tai visiškai valdomas servisas, kuris saugiai laiko duomenis Microsoft debesyje ir yra įdiegtas jūsų Power Platform aplinkoje. Jame yra įdiegtos duomenų valdymo galimybės, tokios kaip duomenų klasifikacija, duomenų kilmė, smulkios prieigos kontrolės ir kitų. Sužinokite daugiau [apie Dataverse čia](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Kodėl turėtume naudoti Dataverse mūsų startuoliui? Standartinės ir individualiai sukurtos lentelės Dataverse suteikia saugią ir debesyje esančią duomenų saugyklą. Lentelės leidžia saugoti skirtingų tipų duomenis, panašiai kaip kelias darbaknyges naudojate vienoje Excel darbo knygoje. Galite naudoti lenteles saugoti duomenis, kurie yra specifiniai jūsų organizacijai ar verslo poreikiams. Kai kurie privalumai, kuriuos mūsų startuolis gaus naudodamas Dataverse, yra, bet neapsiriboja:

- **Lengva valdyti**: Tiek metaduomenys, tiek duomenys saugomi debesyje, todėl jums nereikia rūpintis, kaip jie saugomi ar valdomi. Galite susitelkti į programėlių ir sprendimų kūrimą.

- **Saugus**: Dataverse suteikia saugią ir debesyje esančią duomenų saugyklą. Galite kontroliuoti, kas turi prieigą prie jūsų lentelėse saugomų duomenų ir kokiu būdu naudoti vaidmenų pagrindu nustatomą saugumą.

- **Turtingi metaduomenys**: Duomenų tipai ir ryšiai yra tiesiogiai naudojami Power Apps aplinkoje

- **Logika ir patikra**: Galite naudoti verslo taisykles, skaičiuojamus laukus ir patikros taisykles verslo logikai vykdyti ir duomenų tikslumui palaikyti.

Dabar, kai žinote, kas yra Dataverse ir kodėl turėtumėte jį naudoti, pažvelkime, kaip galite naudoti „Copilot“, kad sukurtumėte lentelę Dataverse, kuri atitiks mūsų finansų komandos reikalavimus.

> **Pastaba** : Šią lentelę naudosite kitame skyriuje automatizacijai sukurti, kuri ištrauks visą sąskaitų informaciją ir saugos ją lentelėje.

Norėdami sukurti lentelę Dataverse naudodami „Copilot“, atlikite žemiau pateiktus veiksmus:

1. Eikite į [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) pagrindinį ekraną.

2. Kairėje navigacijos juostoje pasirinkite **Tables**, tada spustelėkite **Describe the new Table**.

![Select new table](../../../translated_images/lt/describe-new-table.0792373eb757281e.webp)

1. Ekrane **Describe the new Table** naudokite teksto lauką, kad aprašytumėte lentelę, kurią norite sukurti. Pavyzdžiui, **_Noriu sukurti lentelę, kurioje būtų saugoma sąskaitų informacija_**. Spustelėkite mygtuką **Send**, kad siųstumėte užklausą AI „Copilot“.

![Describe the table](../../../translated_images/lt/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. AI „Copilot“ pasiūlys Dataverse lentelę su laukais, kurių jums reikia saugoti norimus duomenis, ir šiek tiek pavyzdinių duomenų. Tuomet galite pritaikyti lentelę pagal savo poreikius naudodami AI „Copilot“ asistentą pokalbių forma.

![Suggested Dataverse table](../../../translated_images/lt/copilot-dataverse-table.b3bc936091324d9d.webp)

1. Finansų komanda nori siųsti el. laišką tiekėjui, kad atnaujintų juos apie sąskaitos dabartinę būseną. Galite naudoti „Copilot“, norėdami pridėti naują lauką lentelėje tiekėjo el. pašto adresui saugoti. Pavyzdžiui, galite naudoti šį užklausos tekstą: **_Noriu pridėti stulpelį tiekėjo el. pašto adresui saugoti_**. Spustelėkite mygtuką **Send**, kad siųstumėte užklausą AI „Copilot“.

1. AI „Copilot“ sugeneruos naują lauką, kurį vėliau galėsite pritaikyti pagal savo poreikius.

1. Baigę darbą su lentele, spustelėkite mygtuką **Create**, kad sukurtumėte lentelę.

## AI modeliai Power Platform su AI Builder

AI Builder yra mažo kodo AI galimybė Power Platform, leidžianti naudoti AI modelius, kad padėtų automatizuoti procesus ir prognozuoti rezultatus. Su AI Builder galite įtraukti AI į savo programėles ir srautus, kurie jungiasi prie duomenų Dataverse ar įvairiuose debesų duomenų šaltiniuose, tokiuose kaip SharePoint, OneDrive ar Azure.

## Iš anksto paruošti AI modeliai ir individualūs AI modeliai

AI Builder suteikia du AI modelių tipus: iš anksto paruoštus AI modelius ir individualius AI modelius. Iš anksto paruošti AI modeliai yra Microsoft apmokyti ir paruošti naudoti Power Platform. Jie padeda pridėti intelektą jūsų programėlėms ir srautams be duomenų rinkimo, savo modelių kūrimo, mokymo ar publikavimo. Šiuos modelius galite naudoti procesų automatizavimui ir rezultatų prognozėms.

Kai kurie iš anksto paruoštų AI modelių Power Platform yra:

- **Pagrindinių frazių išgavimas**: Šis modelis ištraukia pagrindines frazes iš teksto.
- **Kalbos atpažinimas**: Šis modelis nustato teksto kalbą.
- **Nuotaikos analizė**: Šis modelis atpažįsta teigiamą, neigiamą, neutralią ar mišrią nuotaiką tekste.
- **Vizitinės kortelės skaitytuvas**: Šis modelis ištraukia informaciją iš vizitinių kortelių.
- **Teksto atpažinimas**: Šis modelis ištraukia tekstą iš nuotraukų.
- **Objektų aptikimas**: Šis modelis aptinka ir ištraukia objektus iš nuotraukų.
- **Dokumentų apdorojimas**: Šis modelis ištraukia informaciją iš formų.
- **Sąskaitų faktūrų apdorojimas**: Šis modelis ištraukia informaciją iš sąskaitų faktūrų.

Naudodami individualius AI modelius galite įtraukti savo modelį į AI Builder, kad jis veiktų kaip bet kuris kitas AI Builder modelis, leidžiantis jį apmokyti su savo duomenimis. Šiuos modelius galite naudoti procesams automatizuoti bei rezultatams prognozuoti Power Apps ir Power Automate aplinkoje. Naudojant savo modelį taikomi tam tikri apribojimai. Daugiau skaitykite apie šiuos [apribojimus](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![AI builder models](../../../translated_images/lt/ai-builder-models.8069423b84cfc47f.webp)

## Užduotis #2 - Sukurkite sąskaitų apdorojimo srautą mūsų startuoliui

Finansų komanda turi sunkumų apdorojant sąskaitas. Jie naudoja skaičiuoklę sąskaitoms sekti, bet dėl didėjančio sąskaitų skaičiaus tai tapo sunku valdyti. Jie paprašė jūsų sukurti darbo eigos sprendimą, kuris padėtų apdoroti sąskaitas su AI. Darbo eiga turi leisti išgauti informaciją iš sąskaitų ir saugoti informaciją Dataverse lentelėje. Taip pat darbo eiga turi leisti išsiųsti el. laišką finansų komandai su išgauta informacija.

Dabar, kai žinote, kas yra AI Builder ir kodėl jį naudoti, pažvelkime, kaip naudojant ankstesnę Invoice Processing AI Model AI Builder kuriama darbo eiga padės finansų komandai apdoroti sąskaitas.

Norėdami sukurti darbo eigą, kuri padėtų finansų komandai apdoroti sąskaitas su Invoice Processing AI Model AI Builder, atlikite šiuos veiksmus:

1. Eikite į [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst) pagrindinį ekraną.

2. Naudokite teksto lauką pagrindiniame ekrane, kad aprašytumėte norimą sukurti darbo eigą. Pavyzdžiui, **_Apdoroti sąskaitą, kai ji atkeliauja į mano pašto dėžutę_**. Spustelėkite mygtuką **Send**, kad siųstumėte užklausą AI „Copilot“.

   ![Copilot power automate](../../../translated_images/lt/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. AI „Copilot“ pasiūlys jums veiksmus, kuriuos reikia atlikti, kad automatizuotumėte norimą užduotį. Galite spustelėti mygtuką **Next**, kad pereitumėte į kitus žingsnius.

4. Kitame žingsnyje Power Automate prašys nustatyti srautui reikalingus ryšius. Baigę spustelėkite mygtuką **Create flow**, kad sukurtumėte darbo eigą.

5. AI „Copilot“ sugeneruos darbo eigą, kurią vėliau galėsite pritaikyti pagal savo poreikius.

6. Atnaujinkite srauto aktyvatorių ir nustatykite **Folder** į aplanką, kuriame bus saugomos sąskaitos. Pavyzdžiui, galite nustatyti aplanką į **Inbox**. Spustelėkite **Show advanced options** ir nustatykite **Only with Attachments** į **Yes**. Tai užtikrins, kad srautas veiks tik gavus el. laišką su priedu šiame aplanke.

7. Pašalinkite šiuos veiksmus iš srauto: **HTML to text**, **Compose**, **Compose 2**, **Compose 3** ir **Compose 4**, nes jų nenaudosite.

8. Pašalinkite veiksmo **Condition** iš srauto, nes jo nenaudosite. Jis turėtų atrodyti kaip šiame ekrano paveikslėlyje:

   ![power automate, remove actions](../../../translated_images/lt/powerautomate-remove-actions.7216392fe684ceba.webp)

9. Spustelėkite mygtuką **Add an action** ir ieškokite **Dataverse**. Pasirinkite veiksmą **Add a new row**.

10. Veiksme **Extract Information from invoices** atnaujinkite **Invoice File**, nurodydami **Attachment Content** iš el. laiško. Tai užtikrins, kad srautas ištrauks informaciją iš sąskaitos priedo.

11. Pasirinkite lentelę, kurią sukūrėte anksčiau. Pavyzdžiui, galite pasirinkti lentelę **Invoice Information**. Pasirinkite dinaminį turinį iš ankstesnio veiksmo, kad užpildytumėte šiuos laukus:

    - ID
    - Suma
    - Data
    - Pavadinimas
    - Būsena - nustatykite **Būsena** kaip **Laukiama**.
    - Tiekėjo el. paštas - naudokite dinaminį turinį **From** iš trigerio **When a new email arrives**.

    ![power automate add row](../../../translated_images/lt/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. Baigę darbą su srautu, spustelėkite mygtuką **Save**, kad išsaugotumėte srautą. Galite išbandyti srautą, siųsdami el. laišką su sąskaita į nurodytą aplanką trigerio nustatyme.

> **Jūsų namų darbas**: Sukurtas srautas yra gera pradžia, dabar pagalvokite, kaip sukurti automatizaciją, kuri leistų mūsų finansų komandai išsiųsti el. laišką tiekėjui, atnaujinant jį apie esamą sąskaitos būseną. Užuomina: srautas turi veikti, kai sąskaitos būsena pasikeičia.

## Naudokite teksto generavimo AI modelį Power Automate

GPT AI modelis AI Builder leidžia generuoti tekstą pagal užklausą ir veikia per Microsoft Azure OpenAI Service. Ši galimybė leidžia įtraukti GPT (Generative Pre-Trained Transformer) technologiją į programas ir darbo srautus, sukuriant įvairius automatizuotus srautus bei naudingas programas.

GPT modeliai yra intensyviai apmokyti dideliais duomenų kiekiais, todėl gali generuoti tekstą, kuris labai panašus į žmogaus kalbą, gavus užklausą. Integruoto darbo srauto automatizavimo atveju, tokie AI modeliai kaip GPT gali būti naudojami įvairioms užduotims supaprastinti ir automatizuoti.

Pavyzdžiui, galite kurti srautus, kurie automatiškai generuoja tekstą įvairioms paskirtims, tokioms kaip el. laiškų juodraščiai, produktų aprašymai ir pan. Taip pat galite naudoti modelį tekstui generuoti įvairiose programėlėse, pavyzdžiui, pokalbių robotuose ir klientų aptarnavimo programose, kurios leidžia klientų aptarnavimo agentams efektyviai ir greitai atsakyti klientų užklausoms.

![create a prompt](../../../translated_images/lt/create-prompt-gpt.69d429300c2e870a.webp)


Norėdami sužinoti, kaip naudoti šį AI modelį Power Automate, pereikite per [Pridėti intelekto su AI Builder ir GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko) modulį.

## Puikus darbas! Tęskite mokymąsi

Baigę šią pamoką, peržiūrėkite mūsų [Generatyvios AI mokymosi kolekciją](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau gilintumėte žinias apie generatyvią AI!

Norite suasmeninti ir gauti daugiau naudos iš Copilot? Išnagrinėkite [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) — bendruomenės siūlomą instrukcijų, agentų, įgūdžių ir konfigūracijų rinkinį, padedantį geriau išnaudoti GitHub Copilot.

Eikite į 11 pamoką, kurioje sužinosime, kaip [integruoti generatyvią AI su funkcijų kvietimu](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->