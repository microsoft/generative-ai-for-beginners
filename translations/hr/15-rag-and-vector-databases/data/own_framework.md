<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-05-20T02:27:59+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "hr"
}
-->
# Uvod u Neuronske Mreže. Višeslojni Perceptron

U prethodnom dijelu naučili ste o najjednostavnijem modelu neuronske mreže - jednoslojnom perceptronu, linearnom modelu za klasifikaciju s dvije klase.

U ovom dijelu proširit ćemo ovaj model u fleksibilniji okvir, što nam omogućuje:

* izvođenje **višeklasne klasifikacije** uz klasifikaciju s dvije klase
* rješavanje **problema regresije** uz klasifikaciju
* razdvajanje klasa koje nisu linearno razdvojive

Također ćemo razviti vlastiti modularni okvir u Pythonu koji će nam omogućiti konstrukciju različitih arhitektura neuronskih mreža.

## Formalizacija Strojnog Učenja

Počnimo s formalizacijom problema Strojnog Učenja. Pretpostavimo da imamo skup podataka za treniranje **X** s oznakama **Y**, i trebamo izgraditi model *f* koji će davati najtočnije predikcije. Kvaliteta predikcija mjeri se pomoću **funkcije gubitka** ℒ. Sljedeće funkcije gubitka često se koriste:

* Za problem regresije, kada trebamo predvidjeti broj, možemo koristiti **apsolutnu pogrešku** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, ili **kvadratnu pogrešku** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Za klasifikaciju, koristimo **0-1 gubitak** (što je u biti isto što i **točnost** modela), ili **logistički gubitak**.

Za jednoslojni perceptron, funkcija *f* bila je definirana kao linearna funkcija *f(x)=wx+b* (ovdje je *w* matrica težina, *x* je vektor ulaznih značajki, a *b* je vektor pristranosti). Za različite arhitekture neuronskih mreža, ova funkcija može poprimiti složeniji oblik.

> U slučaju klasifikacije, često je poželjno dobiti vjerojatnosti odgovarajućih klasa kao izlaz mreže. Za pretvaranje proizvoljnih brojeva u vjerojatnosti (npr. za normalizaciju izlaza), često koristimo **softmax** funkciju σ, i funkcija *f* postaje *f(x)=σ(wx+b)*

U definiciji *f* iznad, *w* i *b* nazivaju se **parametri** θ=⟨*w,b*⟩. S obzirom na skup podataka ⟨**X**,**Y**⟩, možemo izračunati ukupnu pogrešku na cijelom skupu podataka kao funkciju parametara θ.

> ✅ **Cilj treniranja neuronske mreže je minimizirati pogrešku mijenjajući parametre θ**

## Optimizacija Gradijentnim Spustom

Postoji dobro poznata metoda optimizacije funkcije nazvana **gradijentni spust**. Ideja je da možemo izračunati derivat (u višedimenzionalnom slučaju zvan **gradijent**) funkcije gubitka s obzirom na parametre, i mijenjati parametre na način da se pogreška smanjuje. Ovo se može formalizirati na sljedeći način:

* Inicijalizirajte parametre s nekim slučajnim vrijednostima w<sup>(0)</sup>, b<sup>(0)</sup>
* Ponavljajte sljedeći korak mnogo puta:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Tijekom treniranja, koraci optimizacije trebali bi se računati uzimajući u obzir cijeli skup podataka (sjetite se da se gubitak računa kao zbroj kroz sve uzorke za treniranje). Međutim, u stvarnom životu uzimamo male dijelove skupa podataka zvane **minibatches**, i računamo gradijente na temelju podskupa podataka. Budući da se podskup uzima nasumično svaki put, takva metoda naziva se **stohastički gradijentni spust** (SGD).

## Višeslojni Perceptroni i Unatragna Propagacija

Jednoslojna mreža, kao što smo vidjeli gore, sposobna je klasificirati linearno razdvojive klase. Da bismo izgradili bogatiji model, možemo kombinirati nekoliko slojeva mreže. Matematički bi to značilo da bi funkcija *f* imala složeniji oblik i bila bi izračunata u nekoliko koraka:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Ovdje je α **nelinearna aktivacijska funkcija**, σ je softmax funkcija, a parametri θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoritam gradijentnog spusta ostao bi isti, ali bi bilo teže izračunati gradijente. S obzirom na pravilo lančanog diferenciranja, možemo izračunati derivate kao:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Pravilo lančanog diferenciranja koristi se za izračunavanje derivata funkcije gubitka s obzirom na parametre.

Napomena da je lijevi dio svih tih izraza isti, i stoga možemo učinkovito izračunati derivate počevši od funkcije gubitka i idući "unatrag" kroz računski graf. Stoga se metoda treniranja višeslojnog perceptrona naziva **unatragna propagacija**, ili 'backprop'.

> TODO: citiranje slike

> ✅ Detaljnije ćemo obraditi unatragnu propagaciju u našem primjeru bilježnice.

## Zaključak

U ovoj lekciji izgradili smo vlastitu biblioteku neuronskih mreža i koristili smo je za jednostavan zadatak klasifikacije u dvije dimenzije.

## 🚀 Izazov

U pratećoj bilježnici implementirat ćete vlastiti okvir za izgradnju i treniranje višeslojnih perceptrona. Moći ćete vidjeti detaljno kako moderne neuronske mreže djeluju.

Prijeđite na bilježnicu OwnFramework i prođite kroz nju.

## Pregled i Samostalno Učenje

Unatragna propagacija je uobičajeni algoritam koji se koristi u AI i ML, vrijedan detaljnijeg proučavanja.

## Zadatak

U ovom laboratoriju, traži se da koristite okvir koji ste izgradili u ovoj lekciji za rješavanje klasifikacije rukom pisanih znamenki MNIST.

* Upute
* Bilježnica

**Odricanje odgovornosti**:  
Ovaj dokument je preveden koristeći AI uslugu prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako se trudimo da postignemo tačnost, molimo vas da budete svjesni da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne snosimo odgovornost za nesporazume ili pogrešne interpretacije koji mogu proizaći iz korištenja ovog prijevoda.