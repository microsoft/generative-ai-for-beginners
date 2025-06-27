<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-06-25T23:45:29+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "hr"
}
-->
# Uvod u neuronske mreže: Perceptron

Jedan od prvih pokušaja implementacije nečega sličnog modernoj neuronskoj mreži napravio je Frank Rosenblatt iz Cornell Aeronautical Laboratory 1957. godine. Bila je to hardverska implementacija nazvana "Mark-1", dizajnirana za prepoznavanje primitivnih geometrijskih figura, kao što su trokuti, kvadrati i krugovi.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Slike s Wikipedije

Ulazna slika bila je predstavljena mrežom fotocelija veličine 20x20, pa je neuronska mreža imala 400 ulaza i jedan binarni izlaz. Jednostavna mreža sadržavala je jedan neuron, također nazvan **jedinica logičkog praga**. Težine neuronske mreže djelovale su kao potenciometri koji su zahtijevali ručno podešavanje tijekom faze treniranja.

> ✅ Potenciometar je uređaj koji omogućuje korisniku podešavanje otpora u krugu.

> New York Times je tada pisao o perceptronu: *embrij elektroničkog računala za koje [mornarica] očekuje da će moći hodati, govoriti, vidjeti, pisati, reproducirati se i biti svjestan svog postojanja.*

## Model perceptrona

Pretpostavimo da imamo N značajki u našem modelu, u kojem slučaju ulazni vektor bi bio vektor veličine N. Perceptron je model za **binarnu klasifikaciju**, tj. može razlikovati između dvije klase ulaznih podataka. Pretpostavit ćemo da za svaki ulazni vektor x izlaz našeg perceptrona bude ili +1 ili -1, ovisno o klasi. Izlaz će se izračunati pomoću formule:

y(x) = f(w<sup>T</sup>x)

gdje je f funkcija aktivacije koraka

## Treniranje perceptrona

Za treniranje perceptrona trebamo pronaći vektor težina w koji klasificira većinu vrijednosti ispravno, tj. rezultira najmanjom **pogreškom**. Ova pogreška je definirana **kriterijem perceptrona** na sljedeći način:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

gdje:

* zbroj se uzima na onim točkama trening podataka i koje rezultiraju pogrešnom klasifikacijom
* x<sub>i</sub> su ulazni podaci, a t<sub>i</sub> je ili -1 ili +1 za negativne i pozitivne primjere.

Ovaj kriterij se smatra funkcijom težina w, i trebamo ga minimizirati. Često se koristi metoda nazvana **gradijentni spust**, u kojoj počinjemo s nekim početnim težinama w<sup>(0)</sup>, a zatim u svakom koraku ažuriramo težine prema formuli:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Ovdje je η tzv. **stopa učenja**, a ∇E(w) označava **gradijent** E. Nakon što izračunamo gradijent, završavamo s

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

U ovoj lekciji ste naučili o perceptronu, koji je model za binarnu klasifikaciju, i kako ga trenirati koristeći vektor težina.

## 🚀 Izazov

Ako želite pokušati izgraditi vlastiti perceptron, isprobajte ovaj laboratorij na Microsoft Learn koji koristi Azure ML designer.

## Pregled & Samostalno učenje

Da biste vidjeli kako možemo koristiti perceptron za rješavanje jednostavnog problema kao i stvarnih problema, i da nastavite učiti - idite na Perceptron bilježnicu.

Evo zanimljivog članka o perceptronima također.

## Zadatak

U ovoj lekciji implementirali smo perceptron za zadatak binarne klasifikacije i koristili ga za klasifikaciju između dvije rukom pisane znamenke. U ovom laboratoriju od vas se traži da u potpunosti riješite problem klasifikacije znamenki, tj. odredite koja znamenka najvjerojatnije odgovara danoj slici.

* Upute
* Bilježnica

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku treba smatrati mjerodavnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne odgovaramo za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.