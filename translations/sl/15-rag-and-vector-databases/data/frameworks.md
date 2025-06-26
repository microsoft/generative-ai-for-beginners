<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-06-25T23:12:24+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "sl"
}
-->
# Okvirji nevronskih mrež

Kot smo že izvedeli, da bi lahko učinkovito trenirali nevronske mreže, moramo storiti dve stvari:

* Operirati s tenzorji, npr. množiti, seštevati in izračunavati nekatere funkcije, kot sta sigmoid ali softmax
* Izračunati gradient vseh izrazov, da bi lahko izvedli optimizacijo z gradientnim spustom

Medtem ko knjižnica `numpy` lahko opravi prvi del, potrebujemo nek mehanizem za izračun gradientov. V našem okviru, ki smo ga razvili v prejšnjem razdelku, smo morali ročno programirati vse funkcije derivatov znotraj metode `backward`, ki izvaja povratno propagacijo. Idealno bi bilo, da nam okvir omogoči izračun gradientov *kateregakoli izraza*, ki ga lahko definiramo.

Druga pomembna stvar je možnost izvajanja izračunov na GPU ali katerikoli drugi specializirani enoti za izračun, kot je TPU. Trening globokih nevronskih mrež zahteva *veliko* izračunov, in možnost paralelizacije teh izračunov na GPU-jih je zelo pomembna.

> ✅ Izraz 'paralelizirati' pomeni porazdelitev izračunov na več naprav.

Trenutno sta dva najbolj priljubljena nevronska okvirja: TensorFlow in PyTorch. Oba zagotavljata nizkoločljivostni API za operiranje s tenzorji na CPU-ju in GPU-ju. Na vrhu nizkoločljivostnega API-ja obstaja tudi višjelokostni API, imenovan Keras in PyTorch Lightning.

Nizkoločljivostni API | TensorFlow | PyTorch
--------------|-------------------------------------|--------------------------------
Višjelokostni API | Keras | PyTorch Lightning

**Nizkoločljivostni API-ji** v obeh okvirjih omogočajo gradnjo tako imenovanih **računalniških grafov**. Ta graf definira, kako izračunati izhod (običajno funkcijo izgube) z danimi vhodnimi parametri, in ga lahko pošljemo za izračun na GPU, če je na voljo. Obstajajo funkcije za diferenciacijo tega računalniškega grafa in izračun gradientov, ki jih lahko nato uporabimo za optimizacijo parametrov modela.

**Višjelokostni API-ji** v veliki meri obravnavajo nevronske mreže kot **zaporedje plasti**, in s tem olajšajo konstrukcijo večine nevronskih mrež. Trening modela običajno zahteva pripravo podatkov in nato klic funkcije `fit`, da opravi delo.

Višjelokostni API omogoča hitro konstrukcijo tipičnih nevronskih mrež, ne da bi se morali ukvarjati z veliko podrobnostmi. Hkrati pa nizkoločljivostni API ponuja veliko več nadzora nad procesom treninga, zato se veliko uporablja v raziskavah, ko se ukvarjamo z novimi arhitekturami nevronskih mrež.

Pomembno je tudi razumeti, da lahko oba API-ja uporabljate skupaj, npr. lahko razvijete svojo arhitekturo sloja mreže z uporabo nizkoločljivostnega API-ja in jo nato uporabite znotraj večje mreže, konstruirane in trenirane z višjelokostnim API-jem. Ali pa lahko definirate mrežo z uporabo višjelokostnega API-ja kot zaporedje plasti, nato pa uporabite svoj nizkoločljivostni zanko za trening za izvedbo optimizacije. Oba API-ja uporabljata enake osnovne koncepte in sta zasnovana tako, da dobro delujeta skupaj.

## Učenje

V tem tečaju ponujamo večino vsebine tako za PyTorch kot za TensorFlow. Lahko izberete svoj najljubši okvir in preučite le ustrezne zvezke. Če niste prepričani, kateri okvir izbrati, preberite nekaj razprav na internetu o **PyTorch proti TensorFlow**. Prav tako si lahko ogledate oba okvirja, da dobite boljše razumevanje.

Kjer je mogoče, bomo za enostavnost uporabili višjelokostne API-je. Vendar verjamemo, da je pomembno razumeti, kako nevronske mreže delujejo od začetka, zato na začetku začnemo z delom z nizkoločljivostnim API-jem in tenzorji. Vendar, če želite hitro začeti in ne želite porabiti veliko časa za učenje teh podrobnosti, lahko te preskočite in se usmerite neposredno v zvezke višjelokostnega API-ja.

## ✍️ Vaje: Okvirji

Nadaljujte z učenjem v naslednjih zvezkih:

Nizkoločljivostni API | TensorFlow+Keras Zvezek | PyTorch
--------------|-------------------------------------|--------------------------------
Višjelokostni API | Keras | *PyTorch Lightning*

Ko obvladate okvirje, ponovimo pojem prekomernega prileganja.

# Prekomerno prileganje

Prekomerno prileganje je izjemno pomemben koncept v strojnem učenju, in zelo pomembno je, da ga pravilno razumemo!

Upoštevajte naslednji problem približevanja 5 točk (predstavljenih z `x` na grafih spodaj):

!linearno | prekomerno prileganje
-------------------------|--------------------------
**Linearen model, 2 parametra** | **Nelinearen model, 7 parametrov**
Napaka treninga = 5.3 | Napaka treninga = 0
Napaka validacije = 5.1 | Napaka validacije = 20

* Na levi strani vidimo dobro približanje s premico. Ker je število parametrov ustrezno, model pravilno razume razporeditev točk.
* Na desni strani je model premočan. Ker imamo le 5 točk, model pa ima 7 parametrov, se lahko prilagodi tako, da gre skozi vse točke, kar povzroči, da je napaka treninga 0. Vendar to preprečuje modelu, da bi razumel pravilni vzorec podatkov, zato je napaka validacije zelo visoka.

Zelo pomembno je najti pravilno ravnovesje med bogatostjo modela (številom parametrov) in številom vzorcev za trening.

## Zakaj pride do prekomernega prileganja

  * Premalo podatkov za trening
  * Preveč zmogljiv model
  * Preveč šuma v vhodnih podatkih

## Kako zaznati prekomerno prileganje

Kot lahko vidite na zgornjem grafu, prekomerno prileganje lahko zaznamo z zelo nizko napako treninga in visoko napako validacije. Običajno med treningom vidimo, da se napake treninga in validacije začnejo zmanjševati, nato pa se napaka validacije morda neha zmanjševati in začne naraščati. To bo znak prekomernega prileganja in indikator, da bi morali verjetno prenehati s treningom (ali vsaj narediti posnetek modela).

## Kako preprečiti prekomerno prileganje

Če vidite, da se pojavlja prekomerno prileganje, lahko storite eno od naslednjega:

 * Povečajte količino podatkov za trening
 * Zmanjšajte kompleksnost modela
 * Uporabite neko tehniko regularizacije, kot je Dropout, ki jo bomo obravnavali kasneje.

## Prekomerno prileganje in kompromis med pristranskostjo in varianco

Prekomerno prileganje je dejansko primer bolj generičnega problema v statistiki, imenovanega kompromis med pristranskostjo in varianco. Če upoštevamo možne vire napake v našem modelu, lahko vidimo dva tipa napak:

* **Napake pristranskosti** so posledica tega, da naš algoritem ne more pravilno zajeti razmerja med podatki za trening. To je lahko posledica dejstva, da naš model ni dovolj zmogljiv (**premalo prileganje**).
* **Napake variance**, ki so posledica modela, ki približuje šum v vhodnih podatkih namesto smiselnega razmerja (**prekomerno prileganje**).

Med treningom se napaka pristranskosti zmanjšuje (ko se naš model uči približevati podatke), in napaka variance povečuje. Pomembno je, da trening ustavimo - bodisi ročno (ko zaznamo prekomerno prileganje) ali samodejno (z uvedbo regularizacije) - da preprečimo prekomerno prileganje.

## Zaključek

V tej lekciji ste se naučili o razlikah med različnimi API-ji za dva najbolj priljubljena AI okvirja, TensorFlow in PyTorch. Poleg tega ste se naučili o zelo pomembni temi, prekomernem prileganju.

## 🚀 Izziv

V spremljajočih zvezkih boste našli 'naloge' na dnu; preučite zvezke in dokončajte naloge.

## Pregled & Samostojno učenje

Raziskujte naslednje teme:

- TensorFlow
- PyTorch
- Prekomerno prileganje

Vprašajte se naslednja vprašanja:

- Kakšna je razlika med TensorFlow in PyTorch?
- Kakšna je razlika med prekomernim prileganjem in premalo prileganjem?

## Naloga

V tem laboratoriju ste pozvani, da rešite dve klasifikacijski nalogi z uporabo enoslojnih in večslojnih popolnoma povezanih mrež z uporabo PyTorch ali TensorFlow.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Medtem ko si prizadevamo za natančnost, vas prosimo, da se zavedate, da lahko samodejni prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem maternem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije se priporoča strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.