<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-05-20T02:35:53+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "pl"
}
-->
# Wprowadzenie do sieci neuronowych: Perceptron

Jednym z pierwszych prób wdrożenia czegoś podobnego do współczesnej sieci neuronowej była praca Franka Rosenblatta z Cornell Aeronautical Laboratory w 1957 roku. Była to implementacja sprzętowa nazwana "Mark-1", zaprojektowana do rozpoznawania prymitywnych figur geometrycznych, takich jak trójkąty, kwadraty i koła.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Obrazy z Wikipedii

Obraz wejściowy był reprezentowany przez matrycę fotokomórek 20x20, więc sieć neuronowa miała 400 wejść i jedno wyjście binarne. Prosta sieć zawierała jeden neuron, nazywany także **jednostką logiczną progową**. Wagi sieci neuronowej działały jak potencjometry, które wymagały ręcznej regulacji podczas fazy treningowej.

> ✅ Potencjometr to urządzenie, które pozwala użytkownikowi regulować opór w obwodzie.

> The New York Times pisał wtedy o perceptronie: *zarodek elektronicznego komputera, który [Marynarka Wojenna] spodziewa się, że będzie potrafił chodzić, mówić, widzieć, pisać, reprodukować się i być świadomym swojego istnienia.*

## Model Perceptronu

Załóżmy, że mamy N cech w naszym modelu, w takim przypadku wektor wejściowy byłby wektorem o rozmiarze N. Perceptron jest modelem **klasyfikacji binarnej**, czyli potrafi odróżniać dwie klasy danych wejściowych. Założymy, że dla każdego wektora wejściowego x wyjście naszego perceptronu będzie wynosiło +1 lub -1, w zależności od klasy. Wyjście będzie obliczane za pomocą wzoru:

y(x) = f(w<sup>T</sup>x)

gdzie f jest funkcją aktywacji typu schodkowego

## Trenowanie Perceptronu

Aby wytrenować perceptron, musimy znaleźć wektor wag w, który klasyfikuje większość wartości poprawnie, czyli prowadzi do najmniejszego **błędu**. Ten błąd jest zdefiniowany przez **kryterium perceptronu** w następujący sposób:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

gdzie:

* suma jest brana dla tych punktów danych treningowych i, które prowadzą do błędnej klasyfikacji
* x<sub>i</sub> to dane wejściowe, a t<sub>i</sub> to -1 lub +1 odpowiednio dla negatywnych i pozytywnych przykładów.

To kryterium jest traktowane jako funkcja wag w, i musimy je zminimalizować. Często stosuje się metodę zwaną **gradient descent**, w której zaczynamy od pewnych początkowych wag w<sup>(0)</sup>, a następnie na każdym kroku aktualizujemy wagi zgodnie ze wzorem:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Tutaj η jest tak zwanym **współczynnikiem uczenia**, a ∇E(w) oznacza **gradient** E. Po obliczeniu gradientu, kończymy z

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

W tej lekcji nauczyłeś się o perceptronie, który jest modelem klasyfikacji binarnej, oraz jak go trenować za pomocą wektora wag.

## 🚀 Wyzwanie

Jeśli chcesz spróbować zbudować własny perceptron, wypróbuj to laboratorium na Microsoft Learn, które wykorzystuje projektanta Azure ML.

## Przegląd i Samodzielna Nauka

Aby zobaczyć, jak możemy użyć perceptronu do rozwiązania problemu zabawkowego oraz problemów rzeczywistych, i kontynuować naukę - przejdź do notatnika Perceptron.

Tutaj znajduje się również interesujący artykuł o perceptronach.

## Zadanie

W tej lekcji zaimplementowaliśmy perceptron do zadania klasyfikacji binarnej i użyliśmy go do klasyfikacji dwóch cyfr ręcznie pisanych. W tym laboratorium jesteś proszony o całkowite rozwiązanie problemu klasyfikacji cyfr, czyli określenie, która cyfra najprawdopodobniej odpowiada danemu obrazowi.

* Instrukcje
* Notatnik

**Zrzeczenie się odpowiedzialności**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji o krytycznym znaczeniu zaleca się profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.