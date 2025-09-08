<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-07-09T16:38:26+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "sl"
}
-->
# Okviri za nevronske mreže

Kot smo že spoznali, za učinkovito učenje nevronskih mrež moramo narediti dve stvari:

* Operirati s tenzorji, npr. množiti, seštevati in izračunati nekatere funkcije, kot sta sigmoid ali softmax
* Izračunati gradient vseh izrazov, da lahko izvedemo optimizacijo z metodo gradientnega spusta

Medtem ko knjižnica `numpy` zmore prvo nalogo, potrebujemo mehanizem za izračun gradientov. V našem okviru, ki smo ga razvili v prejšnjem poglavju, smo morali vse odvode ročno programirati znotraj metode `backward`, ki izvaja backpropagation. Idealno bi bilo, da nam okvir omogoča izračun gradientov *kateregakoli izraza*, ki ga lahko definiramo.

Pomembno je tudi, da lahko izvajamo izračune na GPU ali drugih specializiranih procesnih enotah, kot je TPU. Globoko učenje nevronskih mrež zahteva *veliko* izračunov, zato je zelo pomembno, da jih lahko paraleliziramo na GPU-jih.

> ✅ Izraz 'paralelizirati' pomeni razporediti izračune na več naprav.

Trenutno sta najbolj priljubljena okvira za nevronske mreže TensorFlow in PyTorch. Oba nudita nizkonivojski API za delo s tenzorji tako na CPU kot na GPU. Nad nizkonivojskim API-jem pa obstaja tudi višjenivojski API, imenovan Keras oziroma PyTorch Lightning.

Nizkonivojski API | TensorFlow | PyTorch
-----------------|------------|---------
Višjenivojski API| Keras      | PyTorch

**Nizkonivojski API-ji** v obeh okvirih omogočajo gradnjo t.i. **računalniških grafov**. Ta graf določa, kako izračunati izhod (običajno funkcijo izgube) za dane vhodne parametre in ga je mogoče poslati v izračun na GPU, če je na voljo. Obstajajo funkcije za diferenciranje tega računalniškega grafa in izračun gradientov, ki jih nato uporabimo za optimizacijo parametrov modela.

**Višjenivojski API-ji** obravnavajo nevronske mreže kot **zaporedje plasti** in poenostavijo gradnjo večine nevronskih mrež. Učenje modela običajno zahteva pripravo podatkov in nato klic funkcije `fit`, ki opravi delo.

Višjenivojski API omogoča hitro sestavo tipičnih nevronskih mrež brez skrbi za podrobnosti. Hkrati nizkonivojski API ponuja večji nadzor nad procesom učenja, zato se pogosto uporablja v raziskavah, ko delamo z novimi arhitekturami nevronskih mrež.

Pomembno je razumeti, da lahko oba API-ja uporabljamo skupaj, npr. lahko razvijete lastno arhitekturo plasti z nizkonivojskim API-jem in jo nato uporabite znotraj večje mreže, zgrajene in naučene z višjenivojskim API-jem. Ali pa definirate mrežo z višjenivojskim API-jem kot zaporedje plasti in nato uporabite svoj nizkonivojski učni zanko za optimizacijo. Oba API-ja temeljita na istih osnovnih konceptih in sta zasnovana za dobro medsebojno delovanje.

## Učenje

V tem tečaju ponujamo večino vsebin tako za PyTorch kot za TensorFlow. Izberete lahko svoj priljubljeni okvir in sledite ustreznim zvezkom. Če niste prepričani, kateri okvir izbrati, preberite nekaj razprav na spletu o **PyTorch vs. TensorFlow**. Lahko si ogledate tudi oba okvirja, da bolje razumete.

Kjer je mogoče, bomo zaradi enostavnosti uporabljali višjenivojske API-je. Vendar menimo, da je pomembno razumeti, kako nevronske mreže delujejo od temeljev, zato začnemo z nizkonivojskim API-jem in tenzorji. Če pa želite hitro začeti in se ne želite ukvarjati s podrobnostmi, lahko te dele preskočite in se takoj lotite višjenivojskih API zvezkov.

## ✍️ Vaje: Okviri

Nadaljujte z učenjem v naslednjih zvezkih:

Nizkonivojski API | TensorFlow+Keras zvezek | PyTorch
-----------------|--------------------------|---------
Višjenivojski API| Keras                    | *PyTorch Lightning*

Ko boste obvladali okvire, si osvežimo pojem prekomernega prileganja.

# Prekomerno prileganje (Overfitting)

Prekomerno prileganje je izjemno pomemben koncept v strojni inteligenci in zelo pomembno je, da ga pravilno razumemo!

Razmislimo o problemu približevanja 5 točk (na grafih spodaj označenih z `x`):

!linear | overfit
-------------------------|--------------------------
**Linearen model, 2 parametra** | **Nelinearen model, 7 parametrov**
Napaka učenja = 5.3 | Napaka učenja = 0
Napaka validacije = 5.1 | Napaka validacije = 20

* Na levi vidimo dobro linearno približanje. Ker je število parametrov ustrezno, model pravilno zajame vzorec razporeditve točk.
* Na desni je model premočan. Ker imamo le 5 točk, model s 7 parametri lahko prilagodi funkcijo tako, da gre skozi vse točke, zaradi česar je napaka učenja 0. Vendar to preprečuje modelu, da bi razumel pravi vzorec podatkov, zato je napaka validacije zelo visoka.

Zelo pomembno je najti pravo ravnovesje med kompleksnostjo modela (številom parametrov) in številom učnih vzorcev.

## Zakaj pride do prekomernega prileganja

  * Premalo učnih podatkov
  * Model je premočan
  * Preveč šuma v vhodnih podatkih

## Kako zaznati prekomerno prileganje

Kot lahko vidite na zgornjem grafu, lahko prekomerno prileganje zaznamo po zelo nizki napaki učenja in visoki napaki validacije. Običajno med učenjem vidimo, da se napaki učenja in validacije sprva zmanjšujeta, nato pa se napaka validacije ustavi in začne naraščati. To je znak prekomernega prileganja in indikator, da bi morali učenje verjetno ustaviti (ali vsaj narediti posnetek modela).

prekomerno prileganje

## Kako preprečiti prekomerno prileganje

Če opazite, da prihaja do prekomernega prileganja, lahko naredite eno od naslednjega:

 * Povečajte količino učnih podatkov
 * Zmanjšajte kompleksnost modela
 * Uporabite tehniko regularizacije, kot je Dropout, ki jo bomo obravnavali kasneje.

## Prekomerno prileganje in kompromis med pristranskostjo in varianco

Prekomerno prileganje je pravzaprav primer bolj splošnega problema v statistiki, imenovanega kompromis med pristranskostjo in varianco (Bias-Variance Tradeoff). Če pogledamo možne vire napak v našem modelu, lahko razlikujemo dve vrsti napak:

* **Napake zaradi pristranskosti (Bias errors)** nastanejo, ker naš algoritem ne more pravilno zajeti odnosa med učnimi podatki. To se lahko zgodi, če model ni dovolj zmogljiv (**podprileganje**).
* **Napake zaradi variance (Variance errors)** nastanejo, ko model približuje šum v vhodnih podatkih namesto smiselnih vzorcev (**prekomerno prileganje**).

Med učenjem se napaka zaradi pristranskosti zmanjšuje (model se uči približevati podatke), napaka zaradi variance pa narašča. Pomembno je, da učenje ustavimo – bodisi ročno (ko zaznamo prekomerno prileganje) ali samodejno (z uvedbo regularizacije) – da preprečimo prekomerno prileganje.

## Zaključek

V tej lekciji ste spoznali razlike med različnimi API-ji za dva najbolj priljubljena AI okvira, TensorFlow in PyTorch. Poleg tega ste se naučili o zelo pomembni temi, prekomernem prileganju.

## 🚀 Izziv

V spremljajočih zvezkih boste na dnu našli 'naloge'; preglejte zvezke in jih dokončajte.

## Pregled in samostojno učenje

Raziskujte naslednje teme:

- TensorFlow
- PyTorch
- Prekomerno prileganje

Vprašajte se:

- Kakšna je razlika med TensorFlow in PyTorch?
- Kakšna je razlika med prekomernim prileganjem in podprileganjem?

## Naloga

V tej laboratorijski vaji morate rešiti dva problema klasifikacije z uporabo enoplastnih in večplastnih popolnoma povezanih mrež z uporabo PyTorch ali TensorFlow.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.