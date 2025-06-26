<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-06-25T23:32:11+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "sl"
}
-->
# Uvod v nevronske mreže. Večplastni perceptron

V prejšnjem poglavju ste spoznali najpreprostejši model nevronske mreže - enoplastni perceptron, linearni model za klasifikacijo v dveh razredih.

V tem poglavju bomo razširili ta model v bolj fleksibilen okvir, ki nam bo omogočil:

* izvajanje **klasifikacije več razredov** poleg dveh razredov
* reševanje **regresijskih problemov** poleg klasifikacije
* ločevanje razredov, ki niso linearno ločljivi

Prav tako bomo razvili naš modularni okvir v Pythonu, ki nam bo omogočil sestavljanje različnih arhitektur nevronskih mrež.

## Formalizacija strojnega učenja

Začnimo z formalizacijo problema strojnega učenja. Predpostavimo, da imamo učno množico podatkov **X** z oznakami **Y**, in moramo zgraditi model *f*, ki bo zagotavljal najbolj natančne napovedi. Kakovost napovedi se meri z **funkcijo izgube** ℒ. Pogosto se uporabljajo naslednje funkcije izgube:

* Pri regresijskem problemu, ko moramo napovedati število, lahko uporabimo **absolutno napako** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, ali **kvadratno napako** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Pri klasifikaciji uporabljamo **0-1 izgubo** (ki je v bistvu enaka kot **natančnost** modela), ali **logistično izgubo**.

Za enoplastni perceptron je bila funkcija *f* definirana kot linearna funkcija *f(x)=wx+b* (kjer je *w* matrica uteži, *x* je vektor vhodnih značilnosti, in *b* je pristranskostni vektor). Za različne arhitekture nevronskih mrež lahko ta funkcija dobi bolj kompleksno obliko.

> Pri klasifikaciji je pogosto zaželeno, da kot izhod mreže dobimo verjetnosti ustreznih razredov. Za pretvorbo poljubnih številk v verjetnosti (npr. za normalizacijo izhoda) pogosto uporabljamo **softmax** funkcijo σ, in funkcija *f* postane *f(x)=σ(wx+b)*

V zgornji definiciji *f* sta *w* in *b* imenovana **parametra** θ=⟨*w,b*⟩. Glede na množico podatkov ⟨**X**,**Y**⟩ lahko izračunamo skupno napako na celotni množici podatkov kot funkcijo parametrov θ.

> ✅ **Cilj treniranja nevronske mreže je minimizirati napako z variacijo parametrov θ**

## Optimizacija z gradientnim spustom

Obstaja dobro znana metoda optimizacije funkcij, imenovana **gradientni spust**. Ideja je, da lahko izračunamo odvod (v večdimenzionalnem primeru imenovan **gradient**) funkcije izgube glede na parametre, in spreminjamo parametre na način, da se napaka zmanjša. To lahko formaliziramo na naslednji način:

* Inicializiramo parametre z nekimi naključnimi vrednostmi w<sup>(0)</sup>, b<sup>(0)</sup>
* Večkrat ponovimo naslednji korak:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Med treniranjem naj bi se koraki optimizacije izračunavali glede na celotno množico podatkov (spomnite se, da se izguba izračuna kot vsota skozi vse učne vzorce). V resničnem življenju pa vzamemo majhne dele množice podatkov, imenovane **miniserije**, in izračunamo gradiente na podlagi podmnožice podatkov. Ker se podmnožica vsakič vzame naključno, se takšna metoda imenuje **stohastični gradientni spust** (SGD).

## Večplastni perceptroni in povratno razširjanje

Enoplastna mreža, kot smo videli zgoraj, je sposobna klasificirati linearno ločljive razrede. Za gradnjo bogatejšega modela lahko združimo več plasti mreže. Matematično bi to pomenilo, da bi funkcija *f* imela bolj kompleksno obliko, in bi bila izračunana v več korakih:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Tukaj je α **ne-linearna aktivacijska funkcija**, σ je softmax funkcija, in parametri θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoritem gradientnega spusta bi ostal enak, vendar bi bilo težje izračunati gradiente. Glede na pravilo verižne diferenciacije lahko izračunamo odvode kot:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Pravilo verižne diferenciacije se uporablja za izračun odvoda funkcije izgube glede na parametre.

Opazite, da je levi del vseh teh izrazov enak, zato lahko učinkovito izračunamo odvode, začenši z funkcijo izgube in gremo "nazaj" skozi računski graf. Tako se metoda treniranja večplastnega perceptrona imenuje **povratno razširjanje**, ali 'backprop'.

> TODO: sklic na sliko

> ✅ Povratno razširjanje bomo podrobneje obravnavali v našem zvezku z zgledom.

## Zaključek

V tej lekciji smo zgradili lastno knjižnico nevronskih mrež in jo uporabili za preprosto dvodimenzionalno klasifikacijsko nalogo.

## 🚀 Izziv

V spremljajočem zvezku boste implementirali svoj okvir za gradnjo in treniranje večplastnih perceptronov. Videli boste podrobno, kako delujejo sodobne nevronske mreže.

Nadaljujte z zvezkom OwnFramework in ga preučite.

## Pregled & Samostojno učenje

Povratno razširjanje je pogost algoritem, ki se uporablja v AI in ML, vredno ga je preučiti podrobneje.

## Naloga

V tem laboratoriju boste pozvani, da uporabite okvir, ki ste ga zgradili v tej lekciji, za reševanje klasifikacije ročno napisanih številk MNIST.

* Navodila
* Zvezek

**Izjava o omejitvi odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI prevajanja [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da se zavedate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije se priporoča profesionalni človeški prevod. Ne odgovarjamo za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.