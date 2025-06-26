<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-06-25T23:31:47+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "hr"
}
-->
# Uvod u neuronske mreže. Višeslojni perceptron

U prethodnom dijelu ste naučili o najjednostavnijem modelu neuronske mreže - jednoslojnom perceptronu, linearnom modelu za klasifikaciju s dvije klase.

U ovom dijelu ćemo proširiti ovaj model u fleksibilniji okvir koji nam omogućava:

* izvođenje **klasifikacije više klasa** uz klasifikaciju s dvije klase
* rješavanje **problema regresije** uz klasifikaciju
* razdvajanje klasa koje nisu linearno razdvojive

Također ćemo razviti vlastiti modularni okvir u Pythonu koji će nam omogućiti konstruiranje različitih arhitektura neuronskih mreža.

## Formalizacija strojnog učenja

Počnimo s formalizacijom problema strojnog učenja. Pretpostavimo da imamo skup podataka za treniranje **X** s oznakama **Y**, i trebamo izgraditi model *f* koji će davati najtočnije predikcije. Kvaliteta predikcija mjeri se pomoću **funkcije gubitka** ℒ. Često se koriste sljedeće funkcije gubitka:

* Za problem regresije, kada trebamo predvidjeti broj, možemo koristiti **apsolutnu pogrešku** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, ili **kvadratnu pogrešku** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Za klasifikaciju koristimo **0-1 gubitak** (što je u biti isto kao i **točnost** modela), ili **logistički gubitak**.

Za jednoslojni perceptron, funkcija *f* je definirana kao linearna funkcija *f(x)=wx+b* (ovdje je *w* matrica težina, *x* je vektor ulaznih značajki, a *b* je vektor pomaka). Za različite arhitekture neuronskih mreža, ova funkcija može poprimiti složeniji oblik.

> U slučaju klasifikacije, često je poželjno dobiti vjerojatnosti odgovarajućih klasa kao izlaz mreže. Za pretvaranje proizvoljnih brojeva u vjerojatnosti (npr. za normalizaciju izlaza), često koristimo **softmax** funkciju σ, i funkcija *f* postaje *f(x)=σ(wx+b)*

U definiciji *f* iznad, *w* i *b* nazivaju se **parametri** θ=⟨*w,b*⟩. S obzirom na skup podataka ⟨**X**,**Y**⟩, možemo izračunati ukupnu pogrešku na cijelom skupu podataka kao funkciju parametara θ.

> ✅ **Cilj treniranja neuronske mreže je minimizirati pogrešku variranjem parametara θ**

## Optimizacija gradijentnim spuštanjem

Postoji dobro poznata metoda optimizacije funkcija zvana **gradijentno spuštanje**. Ideja je da možemo izračunati derivaciju (u višedimenzionalnom slučaju zvan **gradijent**) funkcije gubitka u odnosu na parametre i mijenjati parametre na način da se pogreška smanji. To se može formalizirati na sljedeći način:

* Inicijaliziraj parametre nekim slučajnim vrijednostima w<sup>(0)</sup>, b<sup>(0)</sup>
* Ponavljaj sljedeći korak mnogo puta:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Tijekom treniranja, koraci optimizacije trebaju biti izračunati uzimajući u obzir cijeli skup podataka (sjeti se da se gubitak računa kao zbroj kroz sve uzorke treniranja). Međutim, u stvarnosti uzimamo male dijelove skupa podataka zvane **minibatches**, i računamo gradijente na temelju podskupa podataka. Budući da se podskup uzima slučajno svaki put, takva metoda se zove **stohastičko gradijentno spuštanje** (SGD).

## Višeslojni perceptroni i povratno širenje

Jednoslojna mreža, kao što smo vidjeli iznad, sposobna je klasificirati linearno razdvojive klase. Da bismo izgradili bogatiji model, možemo kombinirati nekoliko slojeva mreže. Matematički bi to značilo da bi funkcija *f* imala složeniji oblik i bila bi izračunata u nekoliko koraka:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Ovdje je α **nelinearna aktivacijska funkcija**, σ je softmax funkcija, a parametri θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoritam gradijentnog spuštanja ostao bi isti, ali bi bilo teže izračunati gradijente. S obzirom na pravilo diferenciranja po lancu, možemo izračunati derivacije kao:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Pravilo diferenciranja po lancu koristi se za izračunavanje derivacija funkcije gubitka u odnosu na parametre.

Napomena da je lijevi dio svih tih izraza isti, i stoga možemo učinkovito izračunati derivacije počevši od funkcije gubitka i idući "unatrag" kroz računalni graf. Stoga se metoda treniranja višeslojnog perceptrona naziva **povratno širenje**, ili 'backprop'.

> TODO: citat slike

> ✅ Povratno širenje ćemo pokriti puno detaljnije u našem primjeru u bilježnici.

## Zaključak

U ovoj lekciji smo izgradili vlastitu biblioteku neuronskih mreža i koristili smo je za jednostavan zadatak klasifikacije u dvije dimenzije.

## 🚀 Izazov

U pratećoj bilježnici implementirat ćete vlastiti okvir za izgradnju i treniranje višeslojnih perceptrona. Moći ćete detaljno vidjeti kako moderne neuronske mreže funkcioniraju.

Nastavite s bilježnicom OwnFramework i radite kroz nju.

## Pregled i samostalno učenje

Povratno širenje je uobičajeni algoritam korišten u AI i ML, vrijedan dubljeg proučavanja.

## Zadatak

U ovom laboratoriju, traži se od vas da koristite okvir koji ste konstruirali u ovoj lekciji za rješavanje klasifikacije rukom pisanih znamenki MNIST.

* Upute
* Bilježnica

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudi. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.