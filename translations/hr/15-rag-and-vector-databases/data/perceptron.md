<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-05-20T06:44:28+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "hr"
}
-->
# Uvod u Neuronske Mreže: Perceptron

Jedan od prvih pokušaja implementacije nečega sličnog modernoj neuronskoj mreži napravio je Frank Rosenblatt iz Cornell Aeronautical Laboratory 1957. godine. Bila je to hardverska implementacija nazvana "Mark-1", dizajnirana za prepoznavanje primitivnih geometrijskih figura, kao što su trokuti, kvadrati i krugovi.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Slike s Wikipedije

Ulazna slika bila je predstavljena nizom fotocelija 20x20, tako da je neuronska mreža imala 400 ulaza i jedan binarni izlaz. Jednostavna mreža sadržavala je jedan neuron, također nazvan **jedinica logičkog praga**. Težine neuronske mreže djelovale su kao potenciometri koji su zahtijevali ručno podešavanje tijekom faze treniranja.

> ✅ Potenciometar je uređaj koji omogućuje korisniku podešavanje otpornosti kruga.

> The New York Times je tada pisao o perceptronu: *embrij elektroničkog računala za koje [mornarica] očekuje da će moći hodati, govoriti, vidjeti, pisati, reproducirati se i biti svjestan svog postojanja.*

## Model Perceptrona

Pretpostavimo da imamo N značajki u našem modelu, u kojem slučaju ulazni vektor bi bio vektor veličine N. Perceptron je model **binarne klasifikacije**, tj. može razlikovati dvije klase ulaznih podataka. Pretpostavit ćemo da za svaki ulazni vektor x izlaz našeg perceptrona bi bio ili +1 ili -1, ovisno o klasi. Izlaz će se izračunati pomoću formule:

y(x) = f(w<sup>T</sup>x)

gdje je f funkcija aktivacije koraka

## Treniranje Perceptrona

Da bismo trenirali perceptron, moramo pronaći vektor težina w koji ispravno klasificira većinu vrijednosti, tj. rezultira najmanjom **greškom**. Ova greška je definirana **kriterijem perceptrona** na sljedeći način:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

gdje:

* suma se uzima na onim točkama podataka za treniranje i koje rezultiraju pogrešnom klasifikacijom
* x<sub>i</sub> je ulazni podatak, a t<sub>i</sub> je ili -1 ili +1 za negativne i pozitivne primjere.

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

U ovoj lekciji ste naučili o perceptronu, koji je model binarne klasifikacije, i kako ga trenirati koristeći vektor težina.

## 🚀 Izazov

Ako želite pokušati izgraditi vlastiti perceptron, isprobajte ovaj laboratorij na Microsoft Learn koji koristi Azure ML designer.

## Pregled i Samostalno Učenje

Da biste vidjeli kako možemo koristiti perceptron za rješavanje jednostavnih problema kao i problema iz stvarnog života, i nastaviti s učenjem - posjetite Perceptron bilježnicu.

Evo zanimljivog članka o perceptronima.

## Zadatak

U ovoj lekciji smo implementirali perceptron za zadatak binarne klasifikacije, i koristili smo ga za klasifikaciju između dvije rukom pisane znamenke. U ovom laboratoriju, od vas se traži da riješite problem klasifikacije znamenki u cijelosti, tj. odredite koja je znamenka najvjerojatnije povezana s danom slikom.

* Upute
* Bilježnica

**Odricanje odgovornosti**:  
Ovaj dokument je preveden koristeći AI uslugu prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne odgovaramo za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.