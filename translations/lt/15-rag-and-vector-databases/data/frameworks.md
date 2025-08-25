<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-08-25T12:47:04+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "lt"
}
-->
# Neuroninių tinklų karkasai

Kaip jau sužinojome, norint efektyviai treniruoti neuroninius tinklus, reikia dviejų dalykų:

* Dirbti su tenzoriais, pvz., dauginti, sudėti ir skaičiuoti tam tikras funkcijas, tokias kaip sigmoidinė ar softmax
* Skaičiuoti visų išraiškų gradientus, kad būtų galima atlikti gradientinį nusileidimą optimizavimui

Nors `numpy` biblioteka gali atlikti pirmąją dalį, mums reikia mechanizmo gradientams skaičiuoti. Mūsų ankstesniame karkase, kurį kūrėme praėjusioje dalyje, visus išvestinių funkcijų skaičiavimus turėjome programuoti rankiniu būdu `backward` metode, kuris atlieka atgalinį sklidimą. Idealiu atveju, karkasas turėtų suteikti galimybę skaičiuoti *bet kurios išraiškos* gradientus, kurią galime apibrėžti.

Kitas svarbus dalykas – galimybė atlikti skaičiavimus GPU ar kitose specializuotose skaičiavimo įrenginiuose, pvz., TPU. Giliųjų neuroninių tinklų mokymui reikia *labai daug* skaičiavimų, todėl galimybė juos paralelizuoti GPU yra labai svarbi.

> ✅ Terminas „paralelizuoti“ reiškia paskirstyti skaičiavimus per kelis įrenginius.

Šiuo metu du populiariausi neuroninių tinklų karkasai yra: TensorFlow ir PyTorch. Abu jie suteikia žemo lygio API darbui su tenzoriais tiek CPU, tiek GPU. Ant žemo lygio API yra ir aukštesnio lygio API, atitinkamai vadinami Keras ir PyTorch Lightning.

Low-Level API | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
High-level API| Keras| Pytorch

**Žemo lygio API** abiejuose karkasuose leidžia kurti vadinamuosius **skaičiavimų grafus**. Šis grafas apibrėžia, kaip apskaičiuoti išvestį (dažniausiai nuostolių funkciją) su duotais įvesties parametrais ir gali būti perduotas skaičiavimui GPU, jei jis prieinamas. Yra funkcijos, leidžiančios diferencijuoti šį skaičiavimų grafą ir apskaičiuoti gradientus, kuriuos vėliau galima naudoti modelio parametrų optimizavimui.

**Aukšto lygio API** dažniausiai traktuoja neuroninius tinklus kaip **sluoksnių seką** ir leidžia daug lengviau konstruoti daugumą neuroninių tinklų. Modelio mokymas paprastai reikalauja paruošti duomenis ir tada iškviesti `fit` funkciją.

Aukšto lygio API leidžia labai greitai sukurti tipinius neuroninius tinklus, nesirūpinant daugybe detalių. Tuo pačiu metu žemo lygio API suteikia daug daugiau kontrolės mokymo procesui, todėl jie dažnai naudojami tyrimuose, kai dirbama su naujomis neuroninių tinklų architektūromis.

Taip pat svarbu suprasti, kad abi API galima naudoti kartu, pvz., galite sukurti savo tinklo sluoksnio architektūrą naudodami žemo lygio API ir tada naudoti ją didesniame tinkle, sukurtame ir apmokytame su aukšto lygio API. Arba galite apibrėžti tinklą kaip sluoksnių seką su aukšto lygio API ir tada naudoti savo žemo lygio mokymo ciklą optimizavimui. Abi API remiasi tais pačiais pagrindiniais principais ir yra sukurtos taip, kad gerai veiktų kartu.

## Mokymasis

Šiame kurse daugumą turinio pateikiame tiek PyTorch, tiek TensorFlow karkasams. Galite pasirinkti jums patinkantį karkasą ir dirbti tik su atitinkamais užrašais. Jei nesate tikri, kurį karkasą pasirinkti, pasiskaitykite diskusijas internete apie **PyTorch vs. TensorFlow**. Taip pat galite pasižiūrėti į abu karkasus, kad geriau suprastumėte skirtumus.

Kur įmanoma, naudosime aukšto lygio API dėl paprastumo. Tačiau manome, kad svarbu suprasti, kaip neuroniniai tinklai veikia nuo pagrindų, todėl pradžioje dirbsime su žemo lygio API ir tenzoriais. Visgi, jei norite greitai pradėti ir nenorite gilintis į šias detales, galite jas praleisti ir iškart pereiti prie aukšto lygio API užrašų.

## ✍️ Pratimai: Karkasai

Tęskite mokymąsi šiuose užrašuose:

Low-Level API | TensorFlow+Keras Notebook | PyTorch
--------------|-------------------------------------|--------------------------------
High-level API| Keras | *PyTorch Lightning*

Išmokę dirbti su karkasais, prisiminkime, kas yra per didelis pritaikymas (overfitting).

# Per didelis pritaikymas (Overfitting)

Per didelis pritaikymas yra labai svarbi sąvoka mašininio mokymosi srityje, ir labai svarbu ją suprasti teisingai!

Apsvarstykite šią užduotį – aproksimuoti 5 taškus (grafikuose žymimi „x“):

!linear | overfit
-------------------------|--------------------------
**Tiesinis modelis, 2 parametrai** | **Netiesinis modelis, 7 parametrai**
Mokymo klaida = 5.3 | Mokymo klaida = 0
Validacijos klaida = 5.1 | Validacijos klaida = 20

* Kairėje matome gerą tiesės aproksimaciją. Kadangi parametrų skaičius tinkamas, modelis teisingai supranta taškų pasiskirstymą.
* Dešinėje modelis per stiprus. Kadangi turime tik 5 taškus, o modelis turi 7 parametrus, jis gali prisitaikyti taip, kad praeitų per visus taškus, todėl mokymo klaida tampa 0. Tačiau tai neleidžia modeliui suprasti tikrojo duomenų dėsningumo, todėl validacijos klaida labai didelė.

Labai svarbu rasti tinkamą pusiausvyrą tarp modelio sudėtingumo (parametrų skaičiaus) ir mokymo pavyzdžių kiekio.

## Kodėl atsiranda per didelis pritaikymas

  * Per mažai mokymo duomenų
  * Per sudėtingas modelis
  * Per daug triukšmo įvesties duomenyse

## Kaip atpažinti per didelį pritaikymą

Kaip matote iš aukščiau pateikto grafiko, per didelį pritaikymą galima atpažinti pagal labai mažą mokymo klaidą ir didelę validacijos klaidą. Paprastai mokymo metu matysime, kad tiek mokymo, tiek validacijos klaidos pradeda mažėti, o vėliau validacijos klaida gali nustoti mažėti ir pradėti didėti. Tai bus ženklas, kad vyksta per didelis pritaikymas, ir signalas, kad reikėtų sustabdyti mokymą (arba bent jau išsaugoti modelio būseną).

overfitting

## Kaip išvengti per didelio pritaikymo

Jei matote, kad vyksta per didelis pritaikymas, galite imtis šių veiksmų:

 * Padidinti mokymo duomenų kiekį
 * Sumažinti modelio sudėtingumą
 * Naudoti reguliavimo metodus, pvz., Dropout, kurį aptarsime vėliau.

## Per didelis pritaikymas ir šališkumo-variacijos kompromisas

Per didelis pritaikymas iš tikrųjų yra platesnės statistikos problemos, vadinamos šališkumo-variacijos kompromisu, atvejis. Jei pažvelgsime į galimus mūsų modelio klaidų šaltinius, galime išskirti du klaidų tipus:

* **Šališkumo klaidos** atsiranda, kai mūsų algoritmas nesugeba teisingai atspindėti ryšio tarp mokymo duomenų. Tai gali būti dėl to, kad modelis per silpnas (**per mažas pritaikymas**, underfitting).
* **Variacijos klaidos** atsiranda, kai modelis pradeda atkartoti triukšmą įvesties duomenyse, o ne tikrąjį ryšį (**per didelis pritaikymas**, overfitting).

Mokymo metu šališkumo klaida mažėja (modelis mokosi aproksimuoti duomenis), o variacijos klaida didėja. Svarbu sustabdyti mokymą – arba rankiniu būdu (pastebėjus per didelį pritaikymą), arba automatiškai (įvedant reguliavimą) – kad išvengtume per didelio pritaikymo.

## Išvada

Šioje pamokoje sužinojote apie skirtingus dviejų populiariausių AI karkasų – TensorFlow ir PyTorch – API lygius. Taip pat susipažinote su labai svarbia tema – per dideliu pritaikymu.

## 🚀 Iššūkis

Papildomuose užrašuose apačioje rasite „užduotis“; pereikite per užrašus ir atlikite užduotis.

## Apžvalga ir savarankiškas mokymasis

Pasidomėkite šiomis temomis:

- TensorFlow
- PyTorch
- Per didelis pritaikymas (Overfitting)

Užduokite sau šiuos klausimus:

- Kuo skiriasi TensorFlow ir PyTorch?
- Kuo skiriasi per didelis pritaikymas ir per mažas pritaikymas?

## Užduotis

Šioje laboratorijoje turite išspręsti dvi klasifikavimo užduotis, naudodami vieno ir kelių sluoksnių pilnai sujungtus tinklus su PyTorch arba TensorFlow.

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbios informacijos atveju rekomenduojame profesionalų žmogaus vertimą. Mes neatsakome už nesusipratimus ar neteisingą interpretavimą, kilusį dėl šio vertimo naudojimo.