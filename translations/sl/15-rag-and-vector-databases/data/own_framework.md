<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:52:12+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "sl"
}
-->
# Uvod v nevronske mreže. Večplastni perceptron

V prejšnjem poglavju ste spoznali najpreprostejši model nevronske mreže – enoplastni perceptron, linearen model za dvo-razredno klasifikacijo.

V tem poglavju bomo ta model razširili v bolj prilagodljiv okvir, ki nam omogoča:

* izvajanje **večrazredne klasifikacije** poleg dvo-razredne
* reševanje **regresijskih problemov** poleg klasifikacije
* ločevanje razredov, ki niso linearno ločljivi

Razvili bomo tudi lasten modularni okvir v Pythonu, ki nam bo omogočil sestavljanje različnih arhitektur nevronskih mrež.

## Formalizacija strojnega učenja

Začnimo s formalizacijo problema strojnega učenja. Predpostavimo, da imamo učni niz podatkov **X** z oznakami **Y** in želimo zgraditi model *f*, ki bo dajal čim natančnejše napovedi. Kakovost napovedi merimo z **funkcijo izgube** ℒ. Pogosto uporabljene funkcije izgube so:

* Za regresijski problem, ko napovedujemo število, lahko uporabimo **absolutno napako** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| ali **kvadratno napako** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Za klasifikacijo uporabljamo **0-1 izgubo** (kar je v bistvu enako kot **natančnost** modela) ali **logistično izgubo**.

Za enoplastni perceptron je bila funkcija *f* definirana kot linearna funkcija *f(x)=wx+b* (tukaj je *w* matrika uteži, *x* vektor vhodnih značilk, *b* pa vektor pristranskosti). Pri različnih arhitekturah nevronskih mrež lahko ta funkcija zavzame bolj zapleteno obliko.

> Pri klasifikaciji je pogosto zaželeno, da kot izhod mreže dobimo verjetnosti pripadajočih razredov. Za pretvorbo poljubnih števil v verjetnosti (npr. za normalizacijo izhoda) pogosto uporabimo **softmax** funkcijo σ, in funkcija *f* postane *f(x)=σ(wx+b)*

V zgornji definiciji *f* sta *w* in *b* imenovana **parametra** θ=⟨*w,b*⟩. Glede na podatkovni niz ⟨**X**,**Y**⟩ lahko izračunamo skupno napako na celotnem naboru kot funkcijo parametrov θ.

> ✅ **Cilj učenja nevronske mreže je minimizirati napako z variiranjem parametrov θ**

## Optimizacija z gradientnim spustom

Obstaja dobro znana metoda optimizacije funkcij, imenovana **gradientni spust**. Ideja je, da lahko izračunamo odvod (v večdimenzionalnem primeru **gradient**) funkcije izgube glede na parametre in parametre spreminjamo tako, da se napaka zmanjša. To lahko formaliziramo takole:

* Inicializiramo parametre z naključnimi vrednostmi w<sup>(0)</sup>, b<sup>(0)</sup>
* Večkrat ponovimo naslednji korak:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Med učenjem naj bi optimizacijske korake računali na celotnem naboru podatkov (spomnimo se, da je izguba izračunana kot vsota preko vseh učnih primerov). V praksi pa vzamemo majhne dele podatkov, imenovane **minibatches**, in izračunamo gradient glede na podmnožico podatkov. Ker je podmnožica vsakič izbrana naključno, temu pravimo **stohastični gradientni spust** (SGD).

## Večplastni perceptroni in povratno širjenje napake

Enoplastna mreža, kot smo videli zgoraj, zmore klasificirati linearno ločljive razrede. Za gradnjo bogatejšega modela lahko združimo več plasti mreže. Matematično to pomeni, da bo funkcija *f* imela bolj zapleteno obliko in se bo izračunala v več korakih:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Tukaj je α **nenelinearna aktivacijska funkcija**, σ pa softmax funkcija, parametri pa θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoritem gradientnega spusta ostane enak, a izračun gradientov je zahtevnejši. Glede na pravilo verižne diferenciacije lahko odvode izračunamo kot:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Za izračun odvodov funkcije izgube glede na parametre uporabimo pravilo verižne diferenciacije.

Opazimo, da je levi del vseh izrazov enak, zato lahko odvode učinkovito računamo, začenši pri funkciji izgube in se premikamo "nazaj" skozi računski graf. Metoda učenja večplastnega perceptrona se zato imenuje **povratno širjenje napake** ali 'backprop'.

> TODO: navedba slike

> ✅ Povratno širjenje bomo podrobneje obravnavali v našem primerku zvezka.

## Zaključek

V tej lekciji smo zgradili lastno knjižnico nevronskih mrež in jo uporabili za preprosto dvodimenzionalno klasifikacijsko nalogo.

## 🚀 Izziv

V spremljajočem zvezku boste implementirali lasten okvir za gradnjo in učenje večplastnih perceptronov. Podrobno boste spoznali, kako delujejo sodobne nevronske mreže.

Nadaljujte v OwnFramework zvezek in ga preglejte.

## Pregled in samostojno učenje

Povratno širjenje je pogost algoritem v AI in ML, ki ga je vredno podrobneje preučiti.

## Naloga

V tej vaji uporabite okvir, ki ste ga zgradili v tej lekciji, za reševanje klasifikacije ročno pisanih številk MNIST.

* Navodila
* Zvezek

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.