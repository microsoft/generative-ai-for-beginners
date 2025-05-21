<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-05-20T02:09:33+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "sl"
}
-->
# Okviri za nevronske mreže

Kot smo že spoznali, za učinkovito treniranje nevronskih mrež moramo narediti dve stvari:

* Upravljati s tenzorji, npr. množiti, seštevati in izračunavati nekatere funkcije, kot so sigmoid ali softmax
* Izračunati gradient vseh izrazov, da lahko izvedemo optimizacijo z gradientnim spustom

Čeprav knjižnica `numpy` lahko opravi prvi del, potrebujemo nek mehanizem za izračun gradientov. V našem okviru, ki smo ga razvili v prejšnjem poglavju, smo morali ročno programirati vse funkcije derivacij znotraj metode `backward`, ki izvaja povratno propagacijo. Idealno bi bilo, da bi nam okvir omogočal izračun gradientov *kateregakoli izraza*, ki ga lahko definiramo.

Druga pomembna stvar je zmožnost izvajanja izračunov na GPU ali drugih specializiranih enotah, kot je TPU. Treniranje globokih nevronskih mrež zahteva *veliko* izračunov, zato je zelo pomembno, da lahko te izračune paraleliziramo na GPU.

> ✅ Izraz 'paralelizirati' pomeni razdeliti izračune na več naprav.

Trenutno sta dva najbolj priljubljena okvira za nevronske mreže: TensorFlow in PyTorch. Oba nudita nizkonivojski API za delo s tenzorji na CPU in GPU. Poleg nizkonivojskega API-ja obstaja tudi višjenivojski API, imenovan Keras in PyTorch Lightning.

Nizkonivojski API | TensorFlow| PyTorch
------------------|-------------------------------------|--------------------------------
Višjenivojski API| Keras| Pytorch

**Nizkonivojski API-ji** v obeh okvirih vam omogočajo gradnjo tako imenovanih **računalniških grafov**. Ta graf definira, kako izračunati izhod (običajno funkcijo izgube) z danimi vhodnimi parametri, in ga je mogoče prenesti na GPU za izračun, če je na voljo. Obstajajo funkcije za diferenciacijo tega računalniškega grafa in izračun gradientov, ki se lahko nato uporabijo za optimizacijo parametrov modela.

**Višjenivojski API-ji** obravnavajo nevronske mreže kot **zaporedje slojev**, kar olajša konstrukcijo večine nevronskih mrež. Treniranje modela običajno zahteva pripravo podatkov in nato klic funkcije `fit`, da opravi delo.

Višjenivojski API vam omogoča hitro konstrukcijo tipičnih nevronskih mrež, ne da bi se morali ukvarjati z veliko podrobnostmi. Hkrati pa nizkonivojski API nudi veliko več nadzora nad procesom treniranja, zato se veliko uporablja v raziskavah, ko se ukvarjate z novimi arhitekturami nevronskih mrež.

Pomembno je tudi razumeti, da lahko oba API-ja uporabljate skupaj, npr. lahko razvijete svojo arhitekturo slojev mreže z nizkonivojskim API-jem in jo nato uporabite znotraj večje mreže, zgrajene in trenirane z višjenivojskim API-jem. Ali pa lahko definirate mrežo z višjenivojskim API-jem kot zaporedje slojev in nato uporabite svoj nizkonivojski cikel treniranja za optimizacijo. Oba API-ja uporabljata iste osnovne koncepte in sta zasnovana tako, da dobro delujeta skupaj.

## Učenje

V tem tečaju ponujamo večino vsebine tako za PyTorch kot za TensorFlow. Lahko izberete svoj najljubši okvir in preučite samo ustrezne zvezke. Če niste prepričani, kateri okvir izbrati, preberite nekaj razprav na internetu o **PyTorch vs. TensorFlow**. Prav tako si lahko ogledate oba okvira, da bolje razumete.

Kjer je mogoče, bomo uporabljali višjenivojske API-je zaradi enostavnosti. Vendar verjamemo, da je pomembno razumeti, kako nevronske mreže delujejo od začetka, zato bomo na začetku začeli z delom z nizkonivojskim API-jem in tenzorji. Vendar, če želite hitro začeti in ne želite porabiti veliko časa za učenje teh podrobnosti, jih lahko preskočite in se takoj posvetite zvezkom z višjenivojskim API-jem.

## ✍️ Vaje: Okviri

Nadaljujte z učenjem v naslednjih zvezkih:

Nizkonivojski API | TensorFlow+Keras Zvezek | PyTorch
------------------|-------------------------------------|--------------------------------
Višjenivojski API| Keras | *PyTorch Lightning*

Ko obvladate okvire, ponovimo koncept prenaučenja.

# Prenaučenje

Prenaučenje je izjemno pomemben koncept v strojnem učenju in zelo pomembno je, da ga pravilno razumemo!

Razmislite o naslednjem problemu približevanja 5 točk (predstavljenih z `x` na grafih spodaj):

!linear | prenaučenje
----------------------|--------------------------
**Linearen model, 2 parametra** | **Nelinearen model, 7 parametrov**
Napaka pri treniranju = 5.3 | Napaka pri treniranju = 0
Napaka pri validaciji = 5.1 | Napaka pri validaciji = 20

* Na levi vidimo dobro približanje s premico. Ker je število parametrov ustrezno, model pravilno razume razporeditev točk.
* Na desni je model preveč zmogljiv. Ker imamo le 5 točk in model ima 7 parametrov, se lahko prilagodi tako, da gre skozi vse točke, kar povzroči, da je napaka pri treniranju 0. Vendar to prepreči modelu, da bi razumel pravi vzorec podatkov, zato je napaka pri validaciji zelo visoka.

Zelo pomembno je doseči pravilno ravnotežje med bogastvom modela (število parametrov) in številom vzorcev za treniranje.

## Zakaj pride do prenaučenja

  * Premalo podatkov za treniranje
  * Preveč zmogljiv model
  * Preveč šuma v vhodnih podatkih

## Kako zaznati prenaučenje

Kot lahko vidite iz zgornjega grafa, lahko prenaučenje zaznamo z zelo nizko napako pri treniranju in visoko napako pri validaciji. Običajno med treniranjem vidimo, da se napake pri treniranju in validaciji začneta zmanjševati, nato pa se lahko na neki točki napaka pri validaciji preneha zmanjševati in začne naraščati. To bo znak prenaučenja in indikator, da bi morali verjetno prenehati s treniranjem na tej točki (ali vsaj narediti posnetek modela).

prenaučenje

## Kako preprečiti prenaučenje

Če opazite, da se pojavlja prenaučenje, lahko storite eno od naslednjega:

 * Povečajte količino podatkov za treniranje
 * Zmanjšajte kompleksnost modela
 * Uporabite tehniko regularizacije, kot je Dropout, ki jo bomo obravnavali kasneje.

## Prenaučenje in kompromis med pristranskostjo in varianco

Prenaučenje je pravzaprav primer bolj splošnega problema v statistiki, imenovanega kompromis med pristranskostjo in varianco. Če razmislimo o možnih virih napak v našem modelu, lahko vidimo dve vrsti napak:

* **Napake pristranskosti** so povzročene zaradi nezmožnosti našega algoritma, da pravilno zajame razmerje med podatki za treniranje. To lahko izhaja iz dejstva, da naš model ni dovolj zmogljiv (**premalo prileganje**).
* **Napake variance**, ki jih povzroča model, ki približuje šum v vhodnih podatkih namesto smiselnega razmerja (**prenaučenje**).

Med treniranjem se napaka pristranskosti zmanjšuje (ko naš model uči približevati podatke), medtem ko se napaka variance povečuje. Pomembno je prenehati s treniranjem - bodisi ročno (ko zaznamo prenaučenje) ali samodejno (z uvedbo regularizacije) - da preprečimo prenaučenje.

## Zaključek

V tej lekciji ste spoznali razlike med različnimi API-ji za dva najbolj priljubljena AI okvira, TensorFlow in PyTorch. Poleg tega ste spoznali zelo pomembno temo, prenaučenje.

## 🚀 Izziv

V spremljajočih zvezkih boste našli 'naloge' na dnu; preglejte zvezke in dokončajte naloge.

## Pregled & Samostojno učenje

Raziskujte naslednje teme:

- TensorFlow
- PyTorch
- Prenaučenje

Vprašajte se naslednja vprašanja:

- Kakšna je razlika med TensorFlow in PyTorch?
- Kakšna je razlika med prenaučenjem in premalo prileganjem?

## Naloga

V tej delavnici morate rešiti dve klasifikacijski nalogi z uporabo enoplastnih in večplastnih popolnoma povezanih mrež z uporabo PyTorch ali TensorFlow.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.