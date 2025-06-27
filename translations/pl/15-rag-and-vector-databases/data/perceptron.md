<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-06-25T23:39:27+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "pl"
}
-->
# Wprowadzenie do sieci neuronowych: Perceptron

Jednym z pierwszych prób wdrożenia czegoś podobnego do współczesnej sieci neuronowej był projekt Franka Rosenblatta z Cornell Aeronautical Laboratory w 1957 roku. Była to implementacja sprzętowa nazwana "Mark-1", zaprojektowana do rozpoznawania prymitywnych figur geometrycznych, takich jak trójkąty, kwadraty i koła.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Obrazy z Wikipedii

Obraz wejściowy był reprezentowany przez matrycę 20x20 fotokomórek, więc sieć neuronowa miała 400 wejść i jedno binarne wyjście. Prosta sieć zawierała jeden neuron, zwany także **jednostką logiki progowej**. Wagi sieci neuronowej działały jak potencjometry, które wymagały ręcznej regulacji podczas fazy treningowej.

> ✅ Potencjometr to urządzenie, które pozwala użytkownikowi regulować opór w obwodzie.

> The New York Times pisał o perceptronie w tamtym czasie: *embrion elektronicznego komputera, który [Marynarka Wojenna] oczekuje, że będzie w stanie chodzić, mówić, widzieć, pisać, reprodukować się i być świadomym swojego istnienia.*

## Model perceptronu

Załóżmy, że mamy N cech w naszym modelu, w takim przypadku wektor wejściowy byłby wektorem o rozmiarze N. Perceptron to model **klasyfikacji binarnej**, czyli potrafi rozróżnić między dwoma klasami danych wejściowych. Założymy, że dla każdego wektora wejściowego x wyjście naszego perceptronu będzie albo +1, albo -1, w zależności od klasy. Wyjście będzie obliczane za pomocą wzoru:

y(x) = f(w<sup>T</sup>x)

gdzie f jest funkcją aktywacji skoku

## Trenowanie perceptronu

Aby wytrenować perceptron, musimy znaleźć wektor wag w, który klasyfikuje większość wartości poprawnie, czyli daje najmniejszy **błąd**. Ten błąd jest definiowany przez **kryterium perceptronu** w następujący sposób:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

gdzie:

* suma jest brana na tych punktach danych treningowych i, które prowadzą do błędnej klasyfikacji
* x<sub>i</sub> to dane wejściowe, a t<sub>i</sub> to odpowiednio -1 lub +1 dla negatywnych i pozytywnych przykładów.

To kryterium jest traktowane jako funkcja wag w, i musimy ją zminimalizować. Często stosuje się metodę zwaną **gradient descent**, w której zaczynamy z jakimiś początkowymi wagami w<sup>(0)</sup>, a następnie na każdym kroku aktualizujemy wagi zgodnie ze wzorem:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Tutaj η to tak zwana **szybkość uczenia**, a ∇E(w) oznacza **gradient** E. Po obliczeniu gradientu, kończymy z

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

W tej lekcji dowiedziałeś się o perceptronie, który jest modelem klasyfikacji binarnej, oraz jak go wytrenować za pomocą wektora wag.

## 🚀 Wyzwanie

Jeśli chcesz spróbować zbudować własny perceptron, spróbuj tego laboratorium na Microsoft Learn, które wykorzystuje Azure ML designer.

## Przegląd i samodzielna nauka

Aby zobaczyć, jak możemy użyć perceptronu do rozwiązania problemu zabawkowego, a także rzeczywistych problemów, i kontynuować naukę - przejdź do notatnika Perceptron.

Oto ciekawy artykuł o perceptronach.

## Zadanie

W tej lekcji zaimplementowaliśmy perceptron dla zadania klasyfikacji binarnej i użyliśmy go do klasyfikacji między dwoma ręcznie pisanymi cyframi. W tym laboratorium prosisz się o rozwiązanie problemu klasyfikacji cyfr całkowicie, czyli określenie, która cyfra najprawdopodobniej odpowiada danemu obrazowi.

* Instrukcje
* Notatnik

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.