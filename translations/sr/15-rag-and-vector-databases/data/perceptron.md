<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-05-20T06:44:12+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "sr"
}
-->
# Uvod u neuronske mreže: Perceptron

Jedan od prvih pokušaja implementacije nečega sličnog savremenoj neuronskoj mreži izvršio je Frank Rosenblatt iz Cornell Aeronautical Laboratory 1957. godine. To je bila hardverska implementacija nazvana "Mark-1", dizajnirana da prepoznaje primitivne geometrijske figure, kao što su trouglovi, kvadrati i krugovi.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Slike sa Wikipedije

Ulazna slika je predstavljena nizom fotocelija od 20x20, tako da je neuronska mreža imala 400 ulaza i jedan binarni izlaz. Jednostavna mreža je sadržala jedan neuron, koji se takođe naziva **jedinica logičkog praga**. Težine neuronske mreže delovale su kao potenciometri koji su zahtevali ručno podešavanje tokom faze obuke.

> ✅ Potenciometar je uređaj koji omogućava korisniku da podešava otpor u kolu.

> The New York Times je tada pisao o perceptronu: *embrion elektronskog računara za koji [mornarica] očekuje da će moći da hoda, govori, vidi, piše, reprodukuje se i bude svestan svog postojanja.*

## Model perceptrona

Pretpostavimo da imamo N karakteristika u našem modelu, u kom slučaju bi ulazni vektor bio vektor veličine N. Perceptron je model **binarne klasifikacije**, tj. može da razlikuje između dve klase ulaznih podataka. Pretpostavićemo da za svaki ulazni vektor x izlaz našeg perceptrona bude ili +1 ili -1, u zavisnosti od klase. Izlaz će se izračunavati pomoću formule:

y(x) = f(w<sup>T</sup>x)

gde je f stepenasta funkcija aktivacije

## Obuka perceptrona

Da bismo obučili perceptron, treba da pronađemo vektor težina w koji klasifikuje većinu vrednosti tačno, tj. rezultira najmanjom **greškom**. Ova greška je definisana **kriterijumom perceptrona** na sledeći način:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

gde:

* suma se uzima za one tačke podataka za obuku i koje rezultiraju pogrešnom klasifikacijom
* x<sub>i</sub> je ulazni podatak, a t<sub>i</sub> je ili -1 ili +1 za negativne i pozitivne primere odgovarajuće.

Ovaj kriterijum se smatra funkcijom težina w, i treba da ga minimiziramo. Često se koristi metoda zvana **spuštanje niz gradijent**, u kojoj počinjemo sa nekim početnim težinama w<sup>(0)</sup>, a zatim u svakom koraku ažuriramo težine prema formuli:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Ovde je η tzv. **stopa učenja**, a ∇E(w) označava **gradijent** E. Nakon što izračunamo gradijent, dobijamo

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algoritam u Python-u izgleda ovako:

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

U ovoj lekciji ste naučili o perceptronu, koji je model binarne klasifikacije, i kako ga obučiti koristeći vektor težina.

## 🚀 Izazov

Ako želite da pokušate da napravite svoj perceptron, isprobajte ovu laboratoriju na Microsoft Learn koja koristi Azure ML dizajner.

## Pregled i samostalno učenje

Da biste videli kako možemo koristiti perceptron za rešavanje jednostavnog problema kao i problema iz stvarnog života, i da nastavite sa učenjem - idite na beležnicu o perceptronu.

Evo zanimljivog članka o perceptronima.

## Zadatak

U ovoj lekciji smo implementirali perceptron za zadatak binarne klasifikacije, i koristili smo ga za klasifikaciju između dve rukom pisane cifre. U ovoj laboratoriji, od vas se traži da rešite problem klasifikacije cifara u celosti, tj. da odredite koja cifra najverovatnije odgovara datoj slici.

* Uputstva
* Beležnica

**Одричање од одговорности**:  
Овај документ је преведен користећи услугу превођења вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо ка тачности, молимо вас да будете свесни да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације, препоручује се професионални превод од стране људи. Не сносимо одговорност за било какве неспоразуме или погрешна тумачења која произилазе из коришћења овог превода.