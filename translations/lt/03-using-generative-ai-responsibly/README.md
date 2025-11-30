<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d57fad773cbeb69c5dd62e65c34200d",
  "translation_date": "2025-10-18T02:24:51+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "lt"
}
-->
# Atsakingas generatyviosios dirbtinio intelekto naudojimas

[![Atsakingas generatyviosios dirbtinio intelekto naudojimas](../../../translated_images/03-lesson-banner.1ed56067a452d97709d51f6cc8b6953918b2287132f4909ade2008c936cd4af9.lt.png)](https://youtu.be/YOp-e1GjZdA?si=7Wv4wu3x44L1DCVj)

> _Spustelėkite aukščiau esančią nuotrauką, kad peržiūrėtumėte šios pamokos vaizdo įrašą_

Dirbtinis intelektas, ypač generatyvusis dirbtinis intelektas, gali būti labai įdomus, tačiau svarbu apsvarstyti, kaip jį naudoti atsakingai. Reikia atsižvelgti į tokius dalykus kaip užtikrinimas, kad rezultatai būtų teisingi, nekenksmingi ir pan. Šis skyrius siekia suteikti jums kontekstą, ką reikėtų apsvarstyti ir kaip imtis aktyvių veiksmų, kad pagerintumėte savo dirbtinio intelekto naudojimą.

## Įvadas

Šioje pamokoje aptarsime:

- Kodėl turėtumėte teikti pirmenybę atsakingam dirbtiniam intelektui, kurdami generatyvaus dirbtinio intelekto programas.
- Pagrindinius atsakingo dirbtinio intelekto principus ir jų ryšį su generatyviuoju dirbtiniu intelektu.
- Kaip pritaikyti šiuos atsakingo dirbtinio intelekto principus per strategijas ir įrankius.

## Mokymosi tikslai

Baigę šią pamoką, jūs žinosite:

- Kodėl svarbu atsakingai naudoti dirbtinį intelektą, kuriant generatyvaus dirbtinio intelekto programas.
- Kada galvoti apie atsakingo dirbtinio intelekto principus ir juos taikyti, kuriant generatyvaus dirbtinio intelekto programas.
- Kokie įrankiai ir strategijos yra prieinami, kad atsakingo dirbtinio intelekto koncepcija būtų įgyvendinta.

## Atsakingo dirbtinio intelekto principai

Generatyvaus dirbtinio intelekto entuziazmas niekada nebuvo toks didelis. Šis susidomėjimas pritraukė daugybę naujų kūrėjų, dėmesio ir finansavimo į šią sritį. Nors tai yra labai teigiamas dalykas tiems, kurie nori kurti produktus ir įmones, naudojančias generatyvųjį dirbtinį intelektą, svarbu elgtis atsakingai.

Viso kurso metu mes sutelkiame dėmesį į savo startuolio ir mūsų dirbtinio intelekto švietimo produkto kūrimą. Naudosime atsakingo dirbtinio intelekto principus: teisingumą, įtraukimą, patikimumą/saugumą, saugumą ir privatumą, skaidrumą bei atsakomybę. Remdamiesi šiais principais, nagrinėsime, kaip jie susiję su generatyvaus dirbtinio intelekto naudojimu mūsų produktuose.

## Kodėl turėtumėte teikti pirmenybę atsakingam dirbtiniam intelektui

Kuriant produktą, žmogaus poreikių centrinis požiūris, atsižvelgiant į vartotojo interesus, duoda geriausius rezultatus.

Generatyvaus dirbtinio intelekto unikalumas slypi jo gebėjime kurti naudingus atsakymus, informaciją, patarimus ir turinį vartotojams. Tai galima padaryti be daugybės rankinių veiksmų, o rezultatai gali būti labai įspūdingi. Tačiau be tinkamo planavimo ir strategijų tai gali sukelti neigiamų pasekmių vartotojams, produktui ir visuomenei apskritai.

Pažvelkime į kai kurias (bet ne visas) galimas neigiamas pasekmes:

### Halucinacijos

Halucinacijos yra terminas, naudojamas apibūdinti, kai LLM sukuria turinį, kuris yra visiškai nesąmoningas arba akivaizdžiai klaidingas, remiantis kitais informacijos šaltiniais.

Pavyzdžiui, tarkime, kad kuriame funkciją savo startuoliui, kuri leidžia studentams užduoti istorinius klausimus modeliui. Studentas užduoda klausimą „Kas buvo vienintelis „Titaniko“ išgyvenęs žmogus?“

Modelis pateikia atsakymą, panašų į šį:

![Klausimas: „Kas buvo vienintelis „Titaniko“ išgyvenęs žmogus?“](../../../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp)

> _(Šaltinis: [Flying bisons](https://flyingbisons.com?WT.mc_id=academic-105485-koreyst))_

Tai labai užtikrintas ir išsamus atsakymas. Deja, jis yra neteisingas. Net ir minimaliai pasidomėjus, galima sužinoti, kad „Titaniko“ katastrofą išgyveno daugiau nei vienas žmogus. Studentui, kuris tik pradeda tyrinėti šią temą, šis atsakymas gali būti pakankamai įtikinamas, kad nebūtų kvestionuojamas ir būtų laikomas faktu. Tokios pasekmės gali lemti, kad dirbtinio intelekto sistema bus nepatikima ir neigiamai paveiks mūsų startuolio reputaciją.

Kiekviename LLM atnaujinimo etape matome našumo patobulinimus, mažinančius halucinacijas. Nepaisant šių patobulinimų, mes, kaip programų kūrėjai ir vartotojai, vis tiek turime būti sąmoningi dėl šių apribojimų.

### Kenksmingas turinys

Ankstesniame skyriuje aptarėme, kai LLM pateikia neteisingus ar nesąmoningus atsakymus. Kitas rizikos veiksnys, kurį turime žinoti, yra modelio atsakymai su kenksmingu turiniu.

Kenksmingas turinys gali būti apibrėžtas kaip:

- Instrukcijų teikimas arba skatinimas žaloti save ar tam tikras grupes.
- Neapykantos kupinas ar žeminantis turinys.
- Smurtinių veiksmų ar atakų planavimo gairės.
- Instrukcijos, kaip rasti nelegalią medžiagą ar vykdyti neteisėtus veiksmus.
- Seksualiai aiškus turinys.

Mūsų startuoliui svarbu užtikrinti, kad turėtume tinkamus įrankius ir strategijas, kad tokio tipo turinys nebūtų matomas studentams.

### Teisingumo trūkumas

Teisingumas apibrėžiamas kaip „užtikrinimas, kad dirbtinio intelekto sistema būtų laisva nuo šališkumo ir diskriminacijos bei kad ji visus vertintų teisingai ir vienodai.“ Generatyvaus dirbtinio intelekto pasaulyje norime užtikrinti, kad modelio rezultatai neįtvirtintų išskirtinių požiūrių į marginalizuotas grupes.

Tokie rezultatai ne tik kenkia teigiamai vartotojų patirčiai, bet ir daro papildomą žalą visuomenei. Kaip programų kūrėjai, visada turėtume atsižvelgti į platų ir įvairų vartotojų ratą, kurdami sprendimus su generatyviuoju dirbtiniu intelektu.

## Kaip atsakingai naudoti generatyvųjį dirbtinį intelektą

Dabar, kai nustatėme atsakingo generatyvaus dirbtinio intelekto svarbą, pažvelkime į 4 žingsnius, kuriuos galime atlikti, kad atsakingai kurtume savo dirbtinio intelekto sprendimus:

![Mažinimo ciklas](../../../translated_images/mitigate-cycle.babcd5a5658e1775d5f2cb47f2ff305cca090400a72d98d0f9e57e9db5637c72.lt.png)

### Įvertinkite galimą žalą

Programinės įrangos testavime mes testuojame numatomus vartotojo veiksmus programoje. Panašiai, testuojant įvairius vartotojų labiausiai tikėtinus užklausų tipus, yra geras būdas įvertinti galimą žalą.

Kadangi mūsų startuolis kuria švietimo produktą, būtų naudinga paruošti švietimo tematikos užklausų sąrašą. Tai galėtų apimti tam tikrą dalyką, istorinius faktus ir užklausas apie studentų gyvenimą.

### Mažinkite galimą žalą

Dabar laikas rasti būdus, kaip galime užkirsti kelią arba apriboti modelio ir jo atsakymų sukeltą galimą žalą. Tai galime nagrinėti 4 skirtingais lygiais:

![Mažinimo sluoksniai](../../../translated_images/mitigation-layers.377215120b9a1159a8c3982c6bbcf41b6adf8c8fa04ce35cbaeeb13b4979cdfc.lt.png)

- **Modelis**. Pasirinkti tinkamą modelį tinkamam naudojimo atvejui. Didesni ir sudėtingesni modeliai, tokie kaip GPT-4, gali kelti didesnę kenksmingo turinio riziką, kai taikomi mažesniems ir konkretesniems naudojimo atvejams. Naudojant mokymo duomenis modelio pritaikymui taip pat sumažinama kenksmingo turinio rizika.

- **Saugos sistema**. Saugos sistema yra įrankių ir konfigūracijų rinkinys platformoje, aptarnaujančioje modelį, kuris padeda mažinti žalą. Pavyzdžiui, turinio filtravimo sistema „Azure OpenAI“ paslaugoje. Sistemos taip pat turėtų aptikti „jailbreak“ atakas ir nepageidaujamą veiklą, pvz., užklausas iš botų.

- **Metapromptas**. Metapromptai ir pagrindimas yra būdai, kaip galime nukreipti arba apriboti modelį, remdamiesi tam tikru elgesiu ir informacija. Tai gali būti sistemos įvestys, apibrėžiančios tam tikras modelio ribas. Be to, pateikiant rezultatus, kurie yra labiau susiję su sistemos apimtimi ar sritimi.

Taip pat galima naudoti technikas, tokias kaip informacijos paieškos papildyta generacija (RAG), kad modelis trauktų informaciją tik iš patikimų šaltinių. Vėlesnėje šio kurso pamokoje aptarsime [paieškos programų kūrimą](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst).

- **Vartotojo patirtis**. Galutinis sluoksnis yra ten, kur vartotojas tiesiogiai sąveikauja su modeliu per mūsų programos sąsają. Tokiu būdu galime suprojektuoti UI/UX, kad apribotume vartotojo įvestis, kurias jis gali siųsti modeliui, taip pat tekstą ar vaizdus, rodomus vartotojui. Diegiant dirbtinio intelekto programą, taip pat turime būti skaidrūs apie tai, ką mūsų generatyvaus dirbtinio intelekto programa gali ir ko negali.

Mes turime visą pamoką, skirtą [AI programų UX projektavimui](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst).

- **Įvertinkite modelį**. Darbas su LLM gali būti sudėtingas, nes ne visada turime kontrolę dėl duomenų, kuriuos modelis buvo apmokytas. Nepaisant to, visada turėtume vertinti modelio našumą ir rezultatus. Vis dar svarbu matuoti modelio tikslumą, panašumą, pagrįstumą ir rezultatų aktualumą. Tai padeda užtikrinti skaidrumą ir pasitikėjimą suinteresuotaisiais ir vartotojais.

### Valdykite atsakingą generatyvaus dirbtinio intelekto sprendimą

Operacinės praktikos kūrimas aplink jūsų dirbtinio intelekto programas yra galutinis etapas. Tai apima bendradarbiavimą su kitomis mūsų startuolio dalimis, tokiomis kaip teisinė ir saugumo komandos, siekiant užtikrinti, kad laikomės visų reguliavimo politikų. Prieš paleidžiant, taip pat norime sukurti planus, susijusius su pristatymu, incidentų valdymu ir atšaukimu, kad išvengtume bet kokios žalos mūsų vartotojams.

## Įrankiai

Nors atsakingo dirbtinio intelekto sprendimų kūrimas gali atrodyti kaip daug darbo, tai yra pastangos, kurios vertos dėmesio. Augant generatyvaus dirbtinio intelekto sričiai, daugiau įrankių, padedančių kūrėjams efektyviai integruoti atsakomybę į savo darbo eigą, tobulės. Pavyzdžiui, [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) gali padėti aptikti kenksmingą turinį ir vaizdus per API užklausą.

## Žinių patikrinimas

Kokius dalykus reikia apsvarstyti, kad užtikrintumėte atsakingą dirbtinio intelekto naudojimą?

1. Kad atsakymas būtų teisingas.  
2. Kenksmingas naudojimas, kad dirbtinis intelektas nebūtų naudojamas nusikalstamais tikslais.  
3. Užtikrinimas, kad dirbtinis intelektas būtų laisvas nuo šališkumo ir diskriminacijos.  

A: Teisingi atsakymai yra 2 ir 3. Atsakingas dirbtinis intelektas padeda apsvarstyti, kaip sumažinti kenksmingą poveikį, šališkumą ir daugiau.

## 🚀 Iššūkis

Perskaitykite apie [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) ir pažiūrėkite, ką galite pritaikyti savo naudojimui.

## Puikus darbas, tęskite mokymąsi

Baigę šią pamoką, peržiūrėkite mūsų [Generatyvaus dirbtinio intelekto mokymosi kolekciją](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau gilintumėte savo žinias apie generatyvųjį dirbtinį intelektą!

Eikite į 4 pamoką, kurioje aptarsime [Pagrindinius užklausų kūrimo principus](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingą interpretaciją, atsiradusią naudojant šį vertimą.