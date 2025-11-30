<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-08-25T12:47:28+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "lt"
}
-->
# Įvadas į neuroninius tinklus. Daugiasluoksnis perceptronas

Ankstesniame skyriuje susipažinote su pačiu paprasčiausiu neuroninio tinklo modeliu – vieno sluoksnio perceptronu, kuris yra linijinis dviejų klasių klasifikatorius.

Šiame skyriuje išplėsime šį modelį į lankstesnę sistemą, kuri leis mums:

* atlikti **daugiaklasę klasifikaciją** be dviejų klasių atskyrimo
* spręsti **regresijos uždavinius** be klasifikacijos
* atskirti klases, kurios nėra linijiškai atskiriamos

Taip pat sukursime savo modulinę sistemą Python kalba, kuri leis konstruoti įvairias neuroninių tinklų architektūras.

## Mašininio mokymosi formalizavimas

Pradėkime nuo mašininio mokymosi uždavinio formalizavimo. Tarkime, turime mokymo duomenų rinkinį **X** su žymėmis **Y**, ir turime sukurti modelį *f*, kuris darytų kuo tikslesnes prognozes. Prognozių kokybė matuojama **nuostolių funkcija** ℒ. Dažniausiai naudojamos šios nuostolių funkcijos:

* Regresijos uždaviniui, kai reikia prognozuoti skaičių, galime naudoti **absoliutinę paklaidą** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| arba **kvadratinę paklaidą** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Klasifikacijai naudojame **0-1 nuostolį** (kuris iš esmės atitinka modelio **tikslumą**), arba **logistinį nuostolį**.

Vieno sluoksnio perceptronui funkcija *f* buvo apibrėžta kaip linijinė funkcija *f(x)=wx+b* (čia *w* – svorių matrica, *x* – įvesties požymių vektorius, o *b* – poslinkio vektorius). Skirtingoms neuroninių tinklų architektūroms ši funkcija gali būti sudėtingesnė.

> Klasifikacijos atveju dažnai norime, kad tinklo išvestis būtų atitinkamų klasių tikimybės. Norint paversti bet kokius skaičius į tikimybes (pvz., normalizuoti išvestį), dažnai naudojama **softmax** funkcija σ, ir tada funkcija *f* tampa *f(x)=σ(wx+b)*

Aukščiau pateiktoje *f* apibrėžtyje *w* ir *b* vadinami **parametrais** θ=⟨*w,b*⟩. Turėdami duomenų rinkinį ⟨**X**,**Y**⟩, galime apskaičiuoti bendrą klaidą visame rinkinyje kaip parametrų θ funkciją.

> ✅ **Neuroninio tinklo mokymo tikslas – sumažinti klaidą keičiant parametrus θ**

## Gradientinis nuolydžio mažinimas

Yra gerai žinomas funkcijų optimizavimo metodas, vadinamas **gradientiniu nuolydžio mažinimu**. Jo esmė – galime apskaičiuoti nuostolių funkcijos išvestinę (daugiamatėje erdvėje vadinamą **gradientu**) pagal parametrus ir keisti parametrus taip, kad klaida mažėtų. Tai galima formalizuoti taip:

* Inicializuojame parametrus atsitiktinėmis reikšmėmis w<sup>(0)</sup>, b<sup>(0)</sup>
* Kartojame šį žingsnį daug kartų:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Mokymo metu optimizavimo žingsniai turėtų būti skaičiuojami pagal visą duomenų rinkinį (prisiminkite, kad nuostolis skaičiuojamas kaip suma per visus mokymo pavyzdžius). Tačiau realybėje imame mažas duomenų dalis, vadinamas **minipartijomis** (minibatches), ir gradientus skaičiuojame pagal duomenų pogrupį. Kadangi kiekvieną kartą pogrupis parenkamas atsitiktinai, šis metodas vadinamas **stochastiniu gradientiniu nuolydžio mažinimu** (SGD).

## Daugiasluoksniai perceptronai ir atgalinis sklidimas

Vieno sluoksnio tinklas, kaip matėme, gali klasifikuoti tik linijiškai atskiriamas klases. Norėdami sukurti sudėtingesnį modelį, galime sujungti kelis tinklo sluoksnius. Matematiškai tai reiškia, kad funkcija *f* bus sudėtingesnės formos ir bus skaičiuojama keliais žingsniais:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Čia α yra **nelinijinė aktyvacijos funkcija**, σ – softmax funkcija, o parametrai θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Gradientinio nuolydžio mažinimo algoritmas išlieka toks pats, tačiau gradientus apskaičiuoti tampa sudėtingiau. Pagal grandinės išvestinės taisyklę galime išvestines apskaičiuoti taip:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Grandinės išvestinės taisyklė naudojama nuostolių funkcijos išvestinėms pagal parametrus apskaičiuoti.

Atkreipkite dėmesį, kad visų šių išraiškų kairiausioji dalis yra ta pati, todėl galime efektyviai skaičiuoti išvestines pradedant nuo nuostolių funkcijos ir einant „atgal“ per skaičiavimų grafą. Todėl daugiasluoksnio perceptrono mokymo metodas vadinamas **atgaliniu sklidimu** (angl. backpropagation) arba 'backprop'.



> TODO: paveikslėlio šaltinis

> ✅ Atgalinį sklidimą detaliau nagrinėsime mūsų užrašinėje (notebook) pateiktame pavyzdyje.  

## Išvada

Šioje pamokoje sukūrėme savo neuroninių tinklų biblioteką ir panaudojome ją paprastai dvimatės klasifikacijos užduočiai.

## 🚀 Iššūkis

Pridedamoje užrašinėje įgyvendinsite savo sistemą daugiasluoksnių perceptronų kūrimui ir mokymui. Galėsite detaliai pamatyti, kaip veikia šiuolaikiniai neuroniniai tinklai.

Pereikite prie OwnFramework užrašinės ir ją išspręskite.



## Kartojimas ir savarankiškas mokymasis

Atgalinis sklidimas yra dažnai naudojamas algoritmas dirbtiniame intelekte ir mašininio mokymosi srityje, todėl verta jį išsamiau išstudijuoti

## Užduotis

Šioje laboratorijoje turite panaudoti šioje pamokoje sukurtą sistemą MNIST ranka rašytų skaitmenų klasifikavimo uždaviniui išspręsti.

* Instrukcijos
* Užrašinė

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbios informacijos atveju rekomenduojame profesionalų žmogaus vertimą. Mes neatsakome už nesusipratimus ar neteisingą interpretavimą, kilusį dėl šio vertimo naudojimo.