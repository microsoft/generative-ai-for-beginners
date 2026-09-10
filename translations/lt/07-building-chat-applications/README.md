# Generatyviosios AI pagrindu veikiančių pokalbių programėlių kūrimas

[![Generatyviosios AI pagrindu veikiančių pokalbių programėlių kūrimas](../../../translated_images/lt/07-lesson-banner.a279b937f2843833.webp)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Paspauskite aukščiau esančią nuotrauką, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

Kadangi jau matėme, kaip galime kurti teksto generavimo programas, pažvelkime į pokalbių programėles.

Pokalbių programėlės tapo neatsiejama mūsų kasdienio gyvenimo dalimi, siūlančios ne tik paprastą laisva besikeičiančią komunikaciją. Jos yra svarbi klientų aptarnavimo, techninės pagalbos ir net sudėtingų konsultacinių sistemų dalis. Tikėtina, kad neseniai gavote pagalbą iš pokalbių programėlės. Integruodami pažangias technologijas, tokias kaip generatyvioji AI, į šias platformas, didėja sudėtingumas ir iššūkiai.

Kai kuriuos klausimus turime išspręsti:

- **Programėlės kūrimas**. Kaip efektyviai sukurti ir sklandžiai integruoti šias AI pagrindu veikiančias programėles specifiniams naudojimo atvejams?
- **Stebėsena**. Įdiegus, kaip galime stebėti ir užtikrinti, kad programėlės veikia aukščiausio kokybės lygio, tiek funkcionalumo, tiek laikantis [atsakingos AI šešių principų](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

Žengdami į automatizacijos ir sklandžios žmogaus ir mašinos sąveikos amžių, tampa esminė supratimas, kaip generatyvioji AI keičia pokalbių programėlių apimtį, gylį ir prisitaikomumą. Šioje pamokoje išnagrinėsime architektūros aspektus, kurie palaiko šias sudėtingas sistemas, gilinsimės į metodus jas tobulinti specifiniams uždaviniams ir įvertinsime matavimus bei kritinius aspektus, svarbius atsakingam AI taikymui.

## Įvadas

Ši pamoka apima:

- Technikas, kaip efektyviai kurti ir integruoti pokalbių programėles.
- Kaip pritaikyti personalizavimą ir tobulinimą programėlėms.
- Strategijas ir svarstymus, kaip efektyviai stebėti pokalbių programėles.

## Mokymosi tikslai

Pamokos pabaigoje galėsite:

- Apibūdinti svarstymus, kaip kurti ir integruoti pokalbių programėles į esamas sistemas.
- Personalizuoti pokalbių programėles konkretiems naudojimo atvejams.
- Nustatyti pagrindinius rodiklius ir svarstymus efektyviai stebėti ir palaikyti AI pagrindu veikiančių pokalbių programėlių kokybę.
- Užtikrinti, kad pokalbių programėlės atsakingai naudotų AI.

## Generatyviosios AI integravimas į pokalbių programėles

Pokalbių programėlių tobulinimas generatyviosios AI pagalba nėra tik apie jų sumanumo didinimą; tai optimizuojamos jų architektūros, veikimo ir vartotojo sąsajos aspektai, siekiant užtikrinti kokybišką vartotojo patirtį. Tai apima architektūros pagrindus, API integracijas ir vartotojo sąsajos svarstymus. Ši dalis pateiks išsamų žemėlapį, kaip naviguoti sudėtingose srityse, nesvarbu, ar prisijungiate prie esamų sistemų, ar kuriate nepriklausomas platformas.

Šios dalies pabaigoje būsite įgudę efektyviai kurti ir integruoti pokalbių programėles.

### Pokalbių robotas ar pokalbių programėlė?

Prieš pradedant kurti pokalbių programėles, palyginkime „pokalbių robotus“ ir „AI pagrindu veikiančias pokalbių programėles“, kurios atlieka skirtingas funkcijas ir vaidmenis. Pokalbių roboto pagrindinis tikslas – automatizuoti specifines pokalbių užduotis, tokias kaip dažniausiai užduodamų klausimų atsakymai ar siuntos sekimas. Paprastai jis veikia pagal taisykles arba sudėtingus AI algoritmus. Priešingai, AI pagrindu veikianti pokalbių programėlė yra daug platesnė aplinka, skirta įvairių skaitmeninių komunikacijos formų, tokių kaip tekstiniai, balso ir vaizdo pokalbiai tarp žmonių, facilitatavimui. Jos pagrindinis bruožas – generatyviosios AI modelio integracija, kuri sukuria niuansuotas, žmogaus kalbą primenančias diskusijas, generuodama atsakymus pagal įvairiausius įvesties ir kontekstinius signalus. Generatyviosios AI pagrindu veikianti pokalbių programėlė gali vykdyti atvirus diskursus, prisitaikyti prie kintančių pokalbių kontekstų bei kurti kūrybiškus ar sudėtingus dialogus.

Žemiau pateikta lentelė išdėsto pagrindinius skirtumus ir panašumus, kad geriau suprastume jų unikalius vaidmenis skaitmeninėje komunikacijoje.

| Pokalbių robotas                   | Generatyviosios AI pagrindu veikianti pokalbių programėlė    |
| --------------------------------- | ----------------------------------------------------------- |
| Užduotims skirtas ir taisyklių valdomas | Konteksto suvokimas                                         |
| Dažnai integruotas į didesnes sistemas | Gali talpinti vieną ar kelis pokalbių robotus                |
| Ribotas į programą įtrauktų funkcijų   | Apima generatyviosios AI modelius                            |
| Specializuotos ir struktūruotos sąveikos | Geba vykdyti atvirus diskursus                                |

### Iš anksto sukurtų funkcijų naudojimas su SDK ir API

Kuriant pokalbių programėlę, puikus pirmas žingsnis yra įvertinti, kas jau yra pasiekiama rinkoje. Naudojant SDK ir API, kad sukurtumėte pokalbių programėles, yra naudingas strateginis pasirinkimas dėl įvairių priežasčių. Integruodami gerai dokumentuotas SDK ir API, strategiškai pozicionuojate savo programėlę ilgalaikei sėkmei, spręsdami skalės didėjimo ir priežiūros klausimus.

- **Pagreitina kūrimo procesą ir sumažina apkrovą**: Pasikliovimas jau sukurtomis funkcijomis vietoj brangaus jų kūrimo leidžia sutelkti dėmesį į svarbesnius programėlės aspektus, pavyzdžiui, verslo logiką.
- **Geresnis našumas**: Kuriant funkcionalumą nuo nulio, anksčiau ar vėliau kyla klausimas: „Kaip tai išsiplės? Ar ši programėlė gali tvarkyti staigų vartotojų antplūdį?“ Gerai prižiūrimi SDK ir API dažnai turi įmontuotus sprendimus šiems klausimams.
- **Lengvesnė priežiūra**: Atnaujinimai ir patobulinimai paprastai valdomi lengvai, kadangi dauguma API ir SDK tiesiog reikalauja bibliotekos atnaujinimo, kai pasirodo naujesnė versija.
- **Prieiga prie pažangiausių technologijų**: Naudojant modelius, kurie buvo tiksliai paruošti ir apmokyti plačiuose duomenų rinkiniuose, jūsų programėlė įgyja natūralios kalbos galimybių.

Funkcijų prieigos prie SDK ar API dažniausiai reikalauja leidimo naudotis teikiamomis paslaugomis, dažnai per unikalų raktą arba autentifikavimo žetoną. Naudosime OpenAI Python biblioteką, kad pamatytume, kaip tai atrodo. Taip pat galite išbandyti šią pamoką savarankiškai toliau pateiktuose [OpenAI užduoties užduotyne](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) arba [Azure OpenAI užduoties užduotyne](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys).

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

Aukščiau pateiktame pavyzdyje naudojamas GPT-5 mini modelis su Responses API užbaigia paraginimą, tačiau atkreipkite dėmesį, kad API raktas nustatomas iš anksto. Jei rakto nenustatytumėte, gautumėte klaidą.

## Vartotojo patirtis (UX)

Bendro pobūdžio UX principai taikomi pokalbių programėlėms, tačiau čia yra papildomų svarstymų, kurie tampa ypač svarbūs dėl įtrauktų mašininio mokymosi komponentų.

- **Mechanizmas neaiškumams spręsti**: Generatyviosios AI modeliai kartais sukuria dviprasmius atsakymus. Funkcija, leidžianti vartotojams prašyti paaiškinimų, gali būti naudinga susidūrus su šia problema.
- **Konteksto išlaikymas**: Pažangūs generatyviosios AI modeliai sugeba prisiminti kontekstą pokalbyje, tai gali būti vertingas vartotojo patirties priedas. Leidimas vartotojams valdyti ir kontroliuoti kontekstą gerina patirtį, bet įveda riziką saugoti jautrią informaciją. Svarstymai, kiek ilgai ši informacija saugoma, pavyzdžiui, įvedant saugojimo politiką, gali subalansuoti konteksto poreikį su privatumu.
- **Personalizavimas**: Gebėjimas mokytis ir prisitaikyti leidžia AI modeliams pasiūlyti individualią vartotojo patirtį. Vartotojo patirties pritaikymas per funkcijas, tokias kaip vartotojo profiliai, ne tik suteikia vartotojui supratimo jausmą, bet ir padeda efektyviau rasti konkrečius atsakymus, taip sukuriant efektyvesnę ir malonesnę sąveiką.

Vienas tokių personalizavimo pavyzdžių yra „Custom instructions“ nustatymai OpenAI ChatGPT. Jie leidžia pateikti informaciją apie save, kuri gali būti svarbus kontekstas jūsų paraginimams. Štai pavyzdys, kaip veikia vartotojo instrukcija.

![Custom Instructions Settings in ChatGPT](../../../translated_images/lt/custom-instructions.b96f59aa69356fcf.webp)

Šis „profilis“ skatina ChatGPT paruošti pamokos planą apie susietas eilutes. Pastebėkite, kad ChatGPT atsižvelgia į tai, kad vartotojas gali norėti giliau išsamios pamokos pagal jos patirtį.

![Komentaras ChatGPT, prašantis pamokos plano apie susietas eilutes](../../../translated_images/lt/lesson-plan-prompt.cc47c488cf1343df.webp)

### Microsoft sistemos žinutės karkasas dideliems kalbos modeliams

[Microsoft pateikė rekomendacijas](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst), kaip efektyviai rašyti sistemos žinutes generuojant atsakymus iš LLM, suskirstytas į 4 sritis:

1. Apibrėžti, kam modelis skirtas, taip pat jo galimybes ir ribotumus.
2. Apibrėžti modelio išvesties formatą.
3. Pateikti specifinius pavyzdžius, iliustruojančius modelio numatomą elgesį.
4. Pateikti papildomas elgesio apsaugas.

### Prieinamumas

Nesvarbu, ar vartotojas turi regos, klausos, motorikos ar pažinimo sutrikimų, gerai sukurta pokalbių programėlė turėtų būti prieinama visiems. Žemiau pateikiamas sąrašas specifinių funkcijų, skirtų pagerinti prieinamumą įvairiems vartotojų sutrikimams.

- **Funkcijos regos sutrikimams**: Aukšto kontrasto temos ir keičiamo dydžio tekstas, suderinamumas su ekrano skaitytuvais.
- **Funkcijos klausos sutrikimams**: Teksto į kalbą ir kalbos į tekstą funkcijos, vizualiniai signalai garso pranešimams.
- **Funkcijos motorikos sutrikimams**: Palaikymas klaviatūros navigacijai, balso komandos.
- **Funkcijos pažinimo sutrikimams**: Supaprastintos kalbos parinktys.

## Personalizavimas ir tobulinimas domenui specifiniams kalbos modeliams

Įsivaizduokite pokalbių programėlę, kuri supranta jūsų įmonės žargoną ir numato specifinius klausimus, kuriuos dažnai užduoda vartotojai. Yra keli būdai, verti paminėjimo:

- **Naudojimasis DSL modeliais**. DSL reiškia domenui specifinę kalbą. Galite naudoti vadinamąjį DSL modelį, apmokytą konkrečiame domene, kad jis suprastų jo sąvokas ir scenarijus.
- **Taikyti tobulinimą (fine-tuning)**. Tobulinimas yra procesas, kai modelis toliau mokomas su specifiniais duomenimis.

## Personalizavimas: DSL naudojimas

Naudojimasis domenui specifiniais kalbos modeliais (DSL modeliais) gali pagerinti vartotojo įsitraukimą, suteikiant specializuotą, kontekstualiai reikšmingą sąveiką. Tai modelis, apmokytas arba tobulintas suprasti ir generuoti tekstus, susijusius su konkrečia sritimi, industrija ar tema. DSL modelio naudojimo galimybės svyruoja nuo pilno mokymo nuo nulio iki jau esamų modelių naudojimo per SDK ir API. Kita galimybė – tobulinimas, kai paimamas jau iš anksto apmokytas modelis ir pritaikomas specifiniam domenui.

## Personalizavimas: taikyti tobulinimą

Tobulinimas dažnai svarstomas, kai iš anksto apmokytas modelis nepakankamai gerai veikia specializuotoje srityje ar konkrečioje užduotyje.

Pavyzdžiui, medicinos užklausos yra sudėtingos ir reikalauja daug konteksto. Kai medikas diagnozuoja pacientą, tai remiasi įvairiais veiksniais, tokiais kaip gyvenimo būdas ar esamos ligos, ir gali net remtis naujausiais medicinos žurnalais savo diagnozei pagrįsti. Tokiuose niuansuotuose scenarijuose bendros paskirties AI pokalbių programėlė negali būti patikimu šaltiniu.

### Scenarijus: medicinos programėlė

Įsivaizduokite pokalbių programėlę, skirtą padėti medicinos specialistams greitai rasti gydymo gaires, vaistų sąveiką ar naujausius tyrimų rezultatus.

Bendros paskirties modelis gali tikti, atsakant į pagrindinius medicinos klausimus ar teikiant bendrą patarimą, tačiau gali susidurti su sunkumais šiais atvejais:

- **Labai specifinės ar sudėtingos situacijos**. Pavyzdžiui, neurologas gali paklausti programėlės: „Kokios yra dabartinės geriausios praktikos gydant vaikus, kuriems pasireiškia vaistams atspari epilepsija?“
- **Trūksta naujausių pasiekimų**. Bendros paskirties modelis gali nepavykti pateikti naujausiais neurologijos ir farmakologijos pasiekimais pagrįsto atsakymo.

Tokiais atvejais modelio papildomas apmokymas specializuotame medicininiame duomenų rinkinyje žymiai pagerina jo gebėjimą tiksliai ir patikimai spręsti sudėtingus medicininius klausimus. Tam reikia turėti prieigą prie didelio ir aktualaus duomenų rinkinio, atspindinčio domenui būdingus iššūkius ir klausimus.

## Aukštos kokybės AI pagrįstos pokalbių patirties svarstymai

Šiame skyriuje aprašomi kriterijai „aukštos kokybės“ pokalbių programėlėms, įskaitant veiksmingų rodiklių fiksavimą ir atsakingą AI technologijos taikymo sistemą.

### Pagrindiniai rodikliai

Norint palaikyti aukštos kokybės programėlės veikimą, būtina stebėti pagrindinius rodiklius ir svarstymus. Šie matavimai ne tik užtikrina programėlės funkcionalumą, bet ir vertina AI modelio kokybę bei vartotojo patirtį. Žemiau pateiktas sąrašas apima bazinius, AI ir vartotojo patirties rodiklius, į kuriuos reikėtų atkreipti dėmesį.

| Rodiklis                     | Apibrėžimas                                                                                                           | Svarstymai pokalbių programėlės kūrėjui                         |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Veikimo laikas**           | Matuoja laiką, kiek programėlė yra veikianti ir prieinama vartotojams.                                                | Kaip sumažinsite neveikimo laiką?                              |
| **Atsakymo laikas**           | Laikas nuo vartotojo užklausos iki programėlės atsakymo.                                                              | Kaip optimizuosite užklausų apdorojimą, kad pagerintumėte atsakymų laiką? |
| **Tikslumas (Precision)**     | Tikrųjų teigiamų prognozių santykis su visomis teigiamomis prognozėmis.                                              | Kaip patikrinsite savo modelio tikslumą?                        |
| **Atgavimas (Recall)**        | Tikrųjų teigiamų prognozių santykis su realiu teigiamų atvejų skaičiumi.                                            | Kaip matuosite ir gerinsite atkūrimą?                           |
| **F1 balas**                  | Tikslumo ir atgavimo harmoninis vidurkis, balansuojantis abu aspektus.                                               | Koks jūsų tikslinis F1 balas? Kaip subalansuosite tikslumą ir atkūrimą? |
| **Sutrikimo lygis (Perplexity)** | Matuoja, kaip gerai modelio prognozuojamas tikimybių pasiskirstymas atitinka faktinį duomenų pasiskirstymą.           | Kaip mažinsite sutrikimo lygį?                                 |
| **Vartotojo pasitenkinimo rodikliai** | Matuoja vartotojo požiūrį į programėlę. Dažnai renkama apklausų būdu.                                                | Kaip dažnai rinksite vartotojų atsiliepimus? Kaip prisitaikysite pagal juos? |
| **Klaidų dažnis**             | Modelio klaidų suprantant arba kuriant išvestį dažnis.                                                               | Kokias strategijas turite klaidų dažnio mažinimui?             |
| **Permokymo ciklai**          | Dažnis, kuriuo modelis atnaujinamas, įtraukiant naujus duomenis ir įžvalgas.                                          | Kaip dažnai perkursite modelį? Kas inicijuoja modelio perkūrimą?  |

| **Anomalijų nustatymas**    | Įrankiai ir technikos nustatyti neįprastus modelius, kurie nesilaiko numatytos elgsenos.                                   | Kaip reaguosite į anomalijas?                                            |

### Atsakingos dirbtinio intelekto praktikos įgyvendinimas pokalbių programėlėse

„Microsoft“ požiūris į atsakingą DI nustatė šešis principus, kurie turėtų vadovauti DI kūrimui ir naudojimui. Žemiau pateikti principai, jų apibrėžimai ir dalykai, kuriuos pokalbių programėlės kūrėjas turėtų apsvarstyti bei kodėl jie turėtų būti rimtai vertinami.

| Principai             | „Microsoft“ apibrėžimas                               | Apsvarstymai pokalbių programėlės kūrėjui                            | Kodėl tai svarbu                                                                       |
| ---------------------- | ----------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Teisingumas           | DI sistemos turėtų visus žmones vertinti teisingai. | Užtikrinti, kad pokalbių programėlė nediskriminuotų pagal naudotojo duomenis. | Sukurti pasitikėjimą ir įtrauktį tarp naudotojų; išvengti teisinių pasekmių.           |
| Patikimumas ir saugumas | DI sistemos turėtų veikti patikimai ir saugiai.       | Vykdyti testavimą ir avarinius sprendimus, kad sumažintumėte klaidų ir rizikų.  | Užtikrinti naudotojų pasitenkinimą ir išvengti galimos žalos.                          |
| Privatumas ir saugumas | DI sistemos turi būti saugios ir gerbti privatumo taisykles.  | Įdiegti stiprią šifravimą ir duomenų apsaugos priemones.              | Apsaugoti jautrius naudotojų duomenis ir laikytis privatumo įstatymų.                  |
| Įtrauktis              | DI sistemos turi suteikti galią visiems ir įtraukti žmones. | Kurti sąsajas, patogias ir prieinamas įvairioms auditorijoms.         | Užtikrinti, kad platesnis žmonių ratas galėtų efektyviai naudotis programėle.          |
| Skaidrumas             | DI sistemos turi būti suprantamos.                    | Teikti aiškią dokumentaciją ir paaiškinimus dėl DI atsakymų.          | Naudotojai labiau pasitiki sistema, jei supranta, kaip priimami sprendimai.            |
| Atsakomybė             | Žmonės turi būti atsakingi už DI sistemas.            | Nustatyti aiškų procesą DI sprendimų tikrinimui ir tobulinimui.       | Leidžia nuolat gerinti ir koreguoti, jei padaromos klaidos.                            |

## Užduotis

Žr. [assignment](../../../07-building-chat-applications/python). Ji jus ves per seriją pratimų – nuo pirmųjų pokalbių užklausų vykdymo iki teksto klasifikavimo ir santraukų sudarymo bei daugiau. Atkreipkite dėmesį, kad užduotys prieinamos skirtingomis programavimo kalbomis!

## Puikiai! Tęskite kelionę

Baigę šią pamoką, peržiūrėkite mūsų [Generatyvinio DI mokymosi kolekciją](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), kad toliau gilintumėte savo žinias apie generatyvinį DI!

Eikite į 8-ą pamoką, kur sužinosite, kaip pradėti [kurti paieškos programėles](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->