<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-05-20T02:27:33+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "sr"
}
-->
# Uvod u Neuronske Mreže. Višeslojni Perceptron

U prethodnom delu, naučili ste o najjednostavnijem modelu neuronske mreže - jednoslojnom perceptronu, linearnom modelu za klasifikaciju sa dve klase.

U ovom delu proširićemo ovaj model u fleksibilniji okvir, koji nam omogućava da:

* izvodimo **klasifikaciju sa više klasa** pored klasifikacije sa dve klase
* rešavamo **probleme regresije** pored klasifikacije
* razdvojimo klase koje nisu linearno razdvojive

Takođe ćemo razviti sopstveni modularni okvir u Python-u koji će nam omogućiti konstruisanje različitih arhitektura neuronskih mreža.

## Formalizacija Mašinskog Učenja

Počnimo sa formalizacijom problema Mašinskog Učenja. Pretpostavimo da imamo trening skup podataka **X** sa etiketama **Y**, i da treba da izgradimo model *f* koji će davati što tačnija predviđanja. Kvalitet predviđanja meri se pomoću **funkcije gubitka** ℒ. Sledeće funkcije gubitka se često koriste:

* Za problem regresije, kada treba da predvidimo broj, možemo koristiti **apsolutnu grešku** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, ili **kvadratnu grešku** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Za klasifikaciju, koristimo **0-1 gubitak** (što je u suštini isto kao i **tačnost** modela), ili **logistički gubitak**.

Za jednoslojni perceptron, funkcija *f* je definisana kao linearna funkcija *f(x)=wx+b* (ovde je *w* matrica težina, *x* je vektor ulaznih karakteristika, a *b* je vektor pristrasnosti). Za različite arhitekture neuronskih mreža, ova funkcija može imati složeniji oblik.

> U slučaju klasifikacije, često je poželjno dobiti verovatnoće odgovarajućih klasa kao izlaz mreže. Da bismo pretvorili proizvoljne brojeve u verovatnoće (npr. da normalizujemo izlaz), često koristimo **softmax** funkciju σ, i funkcija *f* postaje *f(x)=σ(wx+b)*

U definiciji *f* iznad, *w* i *b* se nazivaju **parametri** θ=⟨*w,b*⟩. Dati skup podataka ⟨**X**,**Y**⟩, možemo izračunati ukupnu grešku na celom skupu podataka kao funkciju parametara θ.

> ✅ **Cilj obuke neuronske mreže je da minimizira grešku variranjem parametara θ**

## Optimizacija Gradijentnim Spuštanjem

Postoji dobro poznata metoda optimizacije funkcije zvana **gradijentno spuštanje**. Ideja je da možemo izračunati derivat (u višedimenzionalnom slučaju zvan **gradijent**) funkcije gubitka u odnosu na parametre, i menjati parametre na takav način da se greška smanjuje. Ovo se može formalizovati na sledeći način:

* Inicijalizujte parametre nekim slučajnim vrednostima w<sup>(0)</sup>, b<sup>(0)</sup>
* Ponavljajte sledeći korak mnogo puta:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Tokom obuke, koraci optimizacije bi trebalo da se računaju uzimajući u obzir ceo skup podataka (setite se da se gubitak računa kao zbir kroz sve uzorke obuke). Međutim, u stvarnom životu uzimamo male delove skupa podataka zvane **minibatchevi**, i računamo gradijente na osnovu podskupa podataka. Pošto se podskup uzima nasumično svaki put, takva metoda se naziva **stohastičko gradijentno spuštanje** (SGD).

## Višeslojni Perceptroni i Unazadna Propagacija

Jednoslojna mreža, kao što smo videli iznad, je sposobna da klasifikuje linearno razdvojive klase. Da bismo izgradili bogatiji model, možemo kombinovati nekoliko slojeva mreže. Matematički to bi značilo da funkcija *f* ima složeniji oblik i da će se računati u nekoliko koraka:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Ovde je α **nelinearna aktivaciona funkcija**, σ je softmax funkcija, a parametri θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algoritam gradijentnog spuštanja bi ostao isti, ali bi bilo teže izračunati gradijente. Dato pravilo diferencijacije lanca, možemo izračunati derivate kao:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Pravilo diferencijacije lanca se koristi za izračunavanje derivata funkcije gubitka u odnosu na parametre.

Napomena da je levi deo svih tih izraza isti, i tako možemo efikasno izračunati derivate počevši od funkcije gubitka i idući "unazad" kroz računsku mrežu. Stoga se metoda obuke višeslojnog perceptrona naziva **unazadna propagacija**, ili 'backprop'.

> TODO: citiranje slike

> ✅ Pokrićemo unazadnu propagaciju mnogo detaljnije u našem primeru u beležnici.

## Zaključak

U ovoj lekciji, izgradili smo sopstvenu biblioteku neuronskih mreža i koristili smo je za jednostavan dvodimenzionalni zadatak klasifikacije.

## 🚀 Izazov

U pratećoj beležnici, implementiraćete sopstveni okvir za izgradnju i obuku višeslojnih perceptrona. Moći ćete detaljno videti kako funkcionišu moderne neuronske mreže.

Pređite na beležnicu OwnFramework i radite kroz nju.

## Pregled i Samostalno Učenje

Unazadna propagacija je uobičajen algoritam korišćen u AI i ML, vredan je detaljnijeg proučavanja.

## Zadatak

U ovoj laboratoriji, traži se da koristite okvir koji ste konstruisali u ovoj lekciji da rešite klasifikaciju rukom pisanih cifara iz MNIST skupa podataka.

* Uputstva
* Beležnica

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге превођења уз помоћ вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да постигнемо тачност, молимо вас да будете свесни да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације, препоручује се професионални људски превод. Не сносимо одговорност за било каква погрешна схватања или погрешна тумачења која произилазе из употребе овог превода.