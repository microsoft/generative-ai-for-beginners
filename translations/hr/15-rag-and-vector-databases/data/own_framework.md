<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:51:56+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "hr"
}
-->
# Uvod u neuronske mreže. Višeslojni perceptron

U prethodnom dijelu ste naučili o najjednostavnijem modelu neuronske mreže - jednoslojnom perceptronu, linearnom modelu za klasifikaciju u dvije klase.

U ovom dijelu proširit ćemo taj model u fleksibilniji okvir koji nam omogućuje:

* izvođenje **višeklasne klasifikacije** uz dvoklasnu
* rješavanje **regresijskih problema** uz klasifikaciju
* razdvajanje klasa koje nisu linearno razdvojive

Također ćemo razviti vlastiti modularni okvir u Pythonu koji će nam omogućiti izgradnju različitih arhitektura neuronskih mreža.

## Formalizacija strojnog učenja

Započnimo formalizacijom problema strojnog učenja. Pretpostavimo da imamo skup podataka za učenje **X** s oznakama **Y**, i trebamo izgraditi model *f* koji će davati što točnije predikcije. Kvaliteta predikcija mjeri se pomoću **funkcije gubitka** ℒ. Često se koriste sljedeće funkcije gubitka:

* Za regresijski problem, kada trebamo predvidjeti broj, možemo koristiti **apsolutnu pogrešku** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| ili **kvadratnu pogrešku** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Za klasifikaciju koristimo **0-1 gubitak** (što je u biti isto kao **točnost** modela) ili **logistički gubitak**.

Za jednoslojni perceptron, funkcija *f* definirana je kao linearna funkcija *f(x)=wx+b* (ovdje je *w* matrica težina, *x* vektor ulaznih značajki, a *b* vektor pristranosti). Za različite arhitekture neuronskih mreža, ta funkcija može imati složeniji oblik.

> U slučaju klasifikacije često je poželjno dobiti vjerojatnosti pripadajućih klasa kao izlaz mreže. Za pretvaranje proizvoljnih brojeva u vjerojatnosti (npr. za normalizaciju izlaza) često koristimo **softmax** funkciju σ, pa funkcija *f* postaje *f(x)=σ(wx+b)*

U definiciji *f* gore, *w* i *b* nazivaju se **parametri** θ=⟨*w,b*⟩. S obzirom na skup podataka ⟨**X**,**Y**⟩, možemo izračunati ukupnu pogrešku na cijelom skupu kao funkciju parametara θ.

> ✅ **Cilj treniranja neuronske mreže je minimizirati pogrešku mijenjanjem parametara θ**

## Optimizacija gradijentnim spustom

Postoji poznata metoda optimizacije funkcija nazvana **gradijentni spust**. Ideja je da možemo izračunati derivaciju (u višedimenzionalnom slučaju nazvanu **gradijent**) funkcije gubitka u odnosu na parametre, i mijenjati parametre tako da se pogreška smanjuje. To se može formalizirati na sljedeći način:

* Inicijaliziraj parametre nekim slučajnim vrijednostima w<sup>(0)</sup>, b<sup>(0)</sup>
* Ponavljaj sljedeći korak mnogo puta:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Tijekom treniranja, koraci optimizacije trebaju se računati uzimajući u obzir cijeli skup podataka (sjetite se da se gubitak računa kao suma kroz sve uzorke za učenje). Međutim, u praksi uzimamo male dijelove skupa podataka nazvane **minibatches** i računamo gradijente na temelju podskupa podataka. Budući da se podskup nasumično bira svaki put, takva metoda naziva se **stohastički gradijentni spust** (SGD).

## Višeslojni perceptroni i backpropagation

Jednoslojna mreža, kao što smo vidjeli, može klasificirati linearno razdvojive klase. Za izgradnju bogatijeg modela možemo kombinirati više slojeva mreže. Matematički to znači da funkcija *f* ima složeniji oblik i računa se u nekoliko koraka:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Ovdje je α **nelinearna aktivacijska funkcija**, σ je softmax funkcija, a parametri θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoritam gradijentnog spusta ostaje isti, ali je teže izračunati gradijente. Primjenom pravila lančane derivacije možemo izračunati derivacije kao:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Pravilo lančane derivacije koristi se za izračun derivacija funkcije gubitka u odnosu na parametre.

Primijetite da je lijevi dio svih ovih izraza isti, pa možemo učinkovito računati derivacije počevši od funkcije gubitka i idući "unatrag" kroz računski graf. Zato se metoda treniranja višeslojnog perceptrona naziva **backpropagation**, ili 'backprop'.

> TODO: citat slike

> ✅ Backpropagation ćemo detaljnije obraditi u našem primjeru u bilježnici.

## Zaključak

U ovoj lekciji izgradili smo vlastitu biblioteku za neuronske mreže i koristili je za jednostavan zadatak klasifikacije u dvije dimenzije.

## 🚀 Izazov

U pratećoj bilježnici implementirat ćete vlastiti okvir za izgradnju i treniranje višeslojnih perceptrona. Moći ćete detaljno vidjeti kako moderne neuronske mreže funkcioniraju.

Nastavite na OwnFramework bilježnicu i radite kroz nju.

## Pregled i samostalno učenje

Backpropagation je uobičajeni algoritam u AI i ML, vrijedi ga proučiti detaljnije.

## Zadatak

U ovom laboratoriju trebate koristiti okvir koji ste izgradili u ovoj lekciji za rješavanje problema klasifikacije rukom pisanih znamenki MNIST.

* Upute
* Bilježnica

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za važne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.