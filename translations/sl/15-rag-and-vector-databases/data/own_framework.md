<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-05-20T02:28:29+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "sl"
}
-->
# Uvod v nevronske mreže. Večplastni perceptron

V prejšnjem razdelku ste spoznali najpreprostejši model nevronske mreže - enoplastni perceptron, linearen model za dvoplastno klasifikacijo.

V tem razdelku bomo ta model razširili v bolj prilagodljiv okvir, ki nam bo omogočil:

* izvajanje **večplastne klasifikacije** poleg dvoplastne
* reševanje **regresijskih problemov** poleg klasifikacije
* ločevanje razredov, ki niso linearno ločljivi

Razvili bomo tudi svoj modularni okvir v Pythonu, ki nam bo omogočil konstrukcijo različnih arhitektur nevronskih mrež.

## Formalizacija strojnega učenja

Začnimo z formalizacijo problema strojnega učenja. Predpostavimo, da imamo učni podatkovni niz **X** z oznakami **Y**, in potrebujemo zgraditi model *f*, ki bo podajal najbolj natančne napovedi. Kakovost napovedi merimo z **funkcijo izgube** ℒ. Pogosto uporabljene funkcije izgube so:

* Pri regresijskem problemu, ko moramo napovedati število, lahko uporabimo **absolutno napako** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, ali **kvadratno napako** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Pri klasifikaciji uporabljamo **0-1 izgubo** (ki je v bistvu enaka **natančnosti** modela), ali **logistično izgubo**.

Pri enoplastnem perceptronu je bila funkcija *f* definirana kot linearna funkcija *f(x)=wx+b* (tu je *w* matrica uteži, *x* je vektor vhodnih značilnosti, in *b* je vektor pristranskosti). Pri različnih arhitekturah nevronskih mrež lahko ta funkcija dobi bolj zapleteno obliko.

> Pri klasifikaciji je pogosto zaželeno, da dobimo verjetnosti ustreznih razredov kot izhod mreže. Za pretvorbo poljubnih številk v verjetnosti (npr. za normalizacijo izhoda) pogosto uporabljamo **softmax** funkcijo σ, in funkcija *f* postane *f(x)=σ(wx+b)*

V zgornji definiciji *f* sta *w* in *b* imenovana **parametra** θ=⟨*w,b*⟩. Glede na podatkovni niz ⟨**X**,**Y**⟩ lahko izračunamo skupno napako na celotnem podatkovnem nizu kot funkcijo parametrov θ.

> ✅ **Cilj treniranja nevronske mreže je zmanjšati napako s spreminjanjem parametrov θ**

## Optimizacija s spustom po gradientu

Obstaja dobro znana metoda optimizacije funkcij, imenovana **spust po gradientu**. Ideja je, da lahko izračunamo odvod (v večdimenzionalnem primeru imenovan **gradient**) funkcije izgube glede na parametre, in spreminjamo parametre tako, da se napaka zmanjša. To lahko formaliziramo takole:

* Inicializiramo parametre z nekimi naključnimi vrednostmi w<sup>(0)</sup>, b<sup>(0)</sup>
* Večkrat ponovimo naslednji korak:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Med treniranjem naj bi bili koraki optimizacije izračunani ob upoštevanju celotnega podatkovnega niza (spomnite se, da se izguba izračuna kot vsota skozi vse učne vzorce). V resničnem življenju pa vzamemo majhne dele podatkovnega niza, imenovane **minibatches**, in izračunamo gradient na podlagi podniza podatkov. Ker je podniz vsakokrat naključno izbran, je taka metoda imenovana **stohastični spust po gradientu** (SGD).

## Večplastni perceptroni in povratno razširjanje

Enoplastna mreža, kot smo videli zgoraj, je sposobna klasificirati linearno ločljive razrede. Za izgradnjo bogatejšega modela lahko kombiniramo več plasti mreže. Matematično bi to pomenilo, da ima funkcija *f* bolj zapleteno obliko, in bo izračunana v več korakih:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Tu je α **ne-linearna aktivacijska funkcija**, σ je softmax funkcija, in parametri θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoritem spusta po gradientu ostane enak, vendar bo težje izračunati gradiente. Glede na pravilo verižne diferenciacije lahko izračunamo odvode kot:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Pravilo verižne diferenciacije se uporablja za izračun odvoda funkcije izgube glede na parametre.

Upoštevajte, da je levi del vseh teh izrazov enak, zato lahko učinkovito izračunamo odvode, začenši z funkcijo izgube in gremo "nazaj" skozi računski graf. Tako se metoda treniranja večplastnega perceptrona imenuje **povratno razširjanje**, ali 'backprop'.

## Zaključek

V tej lekciji smo zgradili svojo knjižnico nevronskih mrež in jo uporabili za preprosto dvodimenzionalno klasifikacijsko nalogo.

## 🚀 Izziv

V priloženi beležnici boste implementirali svoj okvir za gradnjo in treniranje večplastnih perceptronov. Videli boste podrobnosti delovanja sodobnih nevronskih mrež.

Nadaljujte v beležnici OwnFramework in jo predelajte.

## Pregled & Samostojno učenje

Povratno razširjanje je pogost algoritem, uporabljen v AI in ML, vreden podrobnejšega študija.

## Naloga

V tem laboratoriju morate uporabiti okvir, ki ste ga zgradili v tej lekciji, za reševanje klasifikacije ročno pisanih številk MNIST.

* Navodila
* Beležnica

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije se priporoča profesionalni prevod s strani človeka. Ne odgovarjamo za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.