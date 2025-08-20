<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T16:57:24+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "pl"
}
-->
# Wprowadzenie do sieci neuronowych: Perceptron

Jedna z pierwszych prób implementacji czegoś podobnego do współczesnej sieci neuronowej została podjęta przez Franka Rosenblatta z Cornell Aeronautical Laboratory w 1957 roku. Była to implementacja sprzętowa nazwana „Mark-1”, zaprojektowana do rozpoznawania prymitywnych figur geometrycznych, takich jak trójkąty, kwadraty i koła.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Obrazy z Wikipedii

Obraz wejściowy był reprezentowany przez tablicę 20x20 fotokomórek, więc sieć neuronowa miała 400 wejść i jedno wyjście binarne. Prosta sieć zawierała jeden neuron, zwany również **jednostką logiki progowej**. Wagi sieci neuronowej działały jak potencjometry, które wymagały ręcznej regulacji podczas fazy treningu.

> ✅ Potencjometr to urządzenie pozwalające użytkownikowi na regulację oporu w obwodzie.

> The New York Times pisał wtedy o perceptronie: *zarodek elektronicznego komputera, który [Marynarka Wojenna] spodziewa się, że będzie potrafił chodzić, mówić, widzieć, pisać, rozmnażać się i być świadomy swojego istnienia.*

## Model perceptronu

Załóżmy, że mamy N cech w naszym modelu, w takim przypadku wektor wejściowy będzie wektorem o rozmiarze N. Perceptron to model **klasyfikacji binarnej**, czyli potrafi rozróżnić dwie klasy danych wejściowych. Założymy, że dla każdego wektora wejściowego x wyjście naszego perceptronu będzie albo +1, albo -1, w zależności od klasy. Wyjście jest obliczane według wzoru:

y(x) = f(w<sup>T</sup>x)

gdzie f to funkcja aktywacji skokowej

## Trenowanie perceptronu

Aby wytrenować perceptron, musimy znaleźć wektor wag w, który sklasyfikuje większość wartości poprawnie, czyli da najmniejszy **błąd**. Ten błąd jest definiowany przez **kryterium perceptronu** w następujący sposób:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

gdzie:

* suma jest liczona dla tych punktów treningowych i, które skutkują błędną klasyfikacją
* x<sub>i</sub> to dane wejściowe, a t<sub>i</sub> to -1 lub +1 dla przykładów negatywnych i pozytywnych odpowiednio.

To kryterium traktujemy jako funkcję wag w, którą musimy zminimalizować. Często stosuje się metodę zwaną **spadkiem gradientu**, w której zaczynamy od pewnych początkowych wag w<sup>(0)</sup>, a następnie na każdym kroku aktualizujemy wagi według wzoru:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Tutaj η to tzw. **współczynnik uczenia**, a ∇E(w) oznacza **gradient** funkcji E. Po obliczeniu gradientu otrzymujemy

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algorytm w Pythonie wygląda tak:

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

## Podsumowanie

W tej lekcji dowiedziałeś się, czym jest perceptron, model klasyfikacji binarnej, oraz jak go wytrenować, używając wektora wag.

## 🚀 Wyzwanie

Jeśli chcesz spróbować zbudować własny perceptron, wypróbuj to laboratorium na Microsoft Learn, które korzysta z Azure ML designer


## Przegląd i samodzielna nauka

Aby zobaczyć, jak można użyć perceptronu do rozwiązania prostego problemu oraz problemów z życia codziennego, i kontynuować naukę – przejdź do notatnika Perceptron.

Oto również ciekawy artykuł o perceptronach.

## Zadanie

W tej lekcji zaimplementowaliśmy perceptron do zadania klasyfikacji binarnej i użyliśmy go do rozróżnienia dwóch ręcznie pisanych cyfr. W tym laboratorium masz za zadanie rozwiązać problem klasyfikacji cyfr w całości, czyli określić, która cyfra najprawdopodobniej odpowiada danemu obrazowi.

* Instrukcje
* Notatnik

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do jak największej dokładności, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.