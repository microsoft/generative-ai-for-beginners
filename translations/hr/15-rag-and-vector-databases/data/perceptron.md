<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T17:01:41+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "hr"
}
-->
# Uvod u neuronske mreže: Perceptron

Jedan od prvih pokušaja implementacije nečega sličnog modernoj neuronskoj mreži napravio je Frank Rosenblatt iz Cornell Aeronautical Laboratory 1957. godine. Bila je to hardverska implementacija nazvana "Mark-1", dizajnirana za prepoznavanje primitivnih geometrijskih oblika, poput trokuta, kvadrata i krugova.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Slike s Wikipedije

Ulazna slika predstavljena je nizom od 20x20 fotocelija, tako da je neuronska mreža imala 400 ulaza i jedan binarni izlaz. Jednostavna mreža sadržavala je jedan neuron, također nazvan **threshold logic unit**. Težine neuronske mreže djelovale su poput potenciometara koji su zahtijevali ručno podešavanje tijekom faze učenja.

> ✅ Potenciometar je uređaj koji korisniku omogućuje podešavanje otpora u krugu.

> The New York Times je tada pisao o perceptronu: *zametak elektroničkog računala za koje [Mornarica] očekuje da će moći hodati, govoriti, vidjeti, pisati, reproducirati se i biti svjesno svog postojanja.*

## Model perceptrona

Pretpostavimo da u našem modelu imamo N značajki, u kojem slučaju bi ulazni vektor bio vektor veličine N. Perceptron je model **binarne klasifikacije**, tj. može razlikovati dvije klase ulaznih podataka. Pretpostavit ćemo da za svaki ulazni vektor x izlaz našeg perceptrona može biti +1 ili -1, ovisno o klasi. Izlaz se računa pomoću formule:

y(x) = f(w<sup>T</sup>x)

gdje je f funkcija aktivacije stepenice

## Trening perceptrona

Za treniranje perceptrona potrebno je pronaći vektor težina w koji ispravno klasificira većinu vrijednosti, tj. rezultira najmanjom **pogreškom**. Ta se pogreška definira pomoću **perceptron kriterija** na sljedeći način:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

gdje:

* zbroj se računa preko onih podataka za učenje i koji rezultiraju pogrešnom klasifikacijom
* x<sub>i</sub> su ulazni podaci, a t<sub>i</sub> je ili -1 ili +1 za negativne odnosno pozitivne primjere.

Ovaj kriterij se smatra funkcijom težina w, i potrebno ga je minimizirati. Često se koristi metoda zvana **gradijentni spust**, pri čemu započinjemo s nekim početnim težinama w<sup>(0)</sup>, a zatim na svakom koraku ažuriramo težine prema formuli:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Ovdje je η tzv. **stopa učenja**, a ∇E(w) označava **gradijent** funkcije E. Nakon izračuna gradijenta, dobivamo

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algoritam u Pythonu izgleda ovako:

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## Zaključak

U ovoj lekciji ste naučili o perceptronu, modelu binarne klasifikacije, i kako ga trenirati koristeći vektor težina.

## 🚀 Izazov

Ako želite pokušati izgraditi vlastiti perceptron, isprobajte ovaj laboratorij na Microsoft Learn koji koristi Azure ML dizajner


## Pregled i samostalno učenje

Da biste vidjeli kako možemo koristiti perceptron za rješavanje jednostavnih problema kao i problema iz stvarnog života, te nastavili s učenjem - posjetite Perceptron bilježnicu.

Evo i zanimljivog članka o perceptronima.

## Zadatak

U ovoj lekciji implementirali smo perceptron za zadatak binarne klasifikacije i koristili ga za klasifikaciju između dvije rukom napisane znamenke. U ovom laboratoriju traži se da u potpunosti riješite problem klasifikacije znamenki, tj. odredite koja znamenka najvjerojatnije odgovara danoj slici.

* Upute
* Bilježnica

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.