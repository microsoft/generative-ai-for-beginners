<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:45:59+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "pl"
}
-->
# Wprowadzenie do sieci neuronowych. Wielowarstwowy perceptron

W poprzedniej części poznaliście najprostszy model sieci neuronowej – jednowarstwowy perceptron, liniowy model klasyfikacji dwuklasowej.

W tej sekcji rozszerzymy ten model do bardziej elastycznego frameworku, który pozwoli nam:

* wykonywać **klasyfikację wieloklasową** oprócz dwuklasowej
* rozwiązywać **problemy regresji** oprócz klasyfikacji
* rozdzielać klasy, które nie są liniowo separowalne

Stworzymy również własny modułowy framework w Pythonie, który umożliwi budowanie różnych architektur sieci neuronowych.

## Formalizacja uczenia maszynowego

Zacznijmy od formalizacji problemu uczenia maszynowego. Załóżmy, że mamy zbiór treningowy **X** z etykietami **Y** i musimy zbudować model *f*, który będzie dawał jak najdokładniejsze przewidywania. Jakość przewidywań mierzymy za pomocą **funkcji straty** ℒ. Często stosowane funkcje straty to:

* Dla problemu regresji, gdy przewidujemy liczbę, możemy użyć **błędu bezwzględnego** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| lub **błędu kwadratowego** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Dla klasyfikacji stosujemy **0-1 loss** (co w praktyce odpowiada **dokładności** modelu) lub **logistyczną funkcję straty**.

Dla jednowarstwowego perceptronu funkcja *f* była zdefiniowana jako funkcja liniowa *f(x)=wx+b* (gdzie *w* to macierz wag, *x* to wektor cech wejściowych, a *b* to wektor biasów). W przypadku różnych architektur sieci neuronowych funkcja ta może przyjmować bardziej złożoną formę.

> W przypadku klasyfikacji często chcemy, aby wyjściem sieci były prawdopodobieństwa odpowiadających klas. Aby przekształcić dowolne liczby w prawdopodobieństwa (np. znormalizować wyjście), często stosujemy funkcję **softmax** σ, a funkcja *f* przyjmuje postać *f(x)=σ(wx+b)*

W powyższej definicji *f*, *w* i *b* nazywamy **parametrami** θ=⟨*w,b*⟩. Mając zbiór danych ⟨**X**,**Y**⟩, możemy obliczyć całkowity błąd na całym zbiorze jako funkcję parametrów θ.

> ✅ **Celem trenowania sieci neuronowej jest minimalizacja błędu przez zmianę parametrów θ**

## Optymalizacja metodą spadku gradientu

Istnieje dobrze znana metoda optymalizacji funkcji zwana **spadkiem gradientu**. Polega ona na tym, że możemy obliczyć pochodną (w przypadku wielowymiarowym nazywaną **gradientem**) funkcji straty względem parametrów i zmieniać parametry tak, aby błąd malał. Można to sformalizować następująco:

* Inicjalizujemy parametry losowymi wartościami w<sup>(0)</sup>, b<sup>(0)</sup>
* Powtarzamy wielokrotnie następujący krok:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup> - η ∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup> - η ∂ℒ/∂b

Podczas treningu kroki optymalizacji powinny być liczone na podstawie całego zbioru danych (pamiętaj, że strata jest sumą po wszystkich próbkach treningowych). Jednak w praktyce bierzemy małe porcje danych zwane **minibatchami** i obliczamy gradienty na podstawie podzbioru danych. Ponieważ podzbiór jest wybierany losowo za każdym razem, taka metoda nazywa się **stochastycznym spadkiem gradientu** (SGD).

## Wielowarstwowe perceptrony i propagacja wsteczna

Jednowarstwowa sieć, jak widzieliśmy powyżej, potrafi klasyfikować klasy liniowo separowalne. Aby zbudować bogatszy model, możemy połączyć kilka warstw sieci. Matematycznie oznacza to, że funkcja *f* przyjmie bardziej złożoną formę i będzie obliczana w kilku krokach:
* z<sub>1</sub> = w<sub>1</sub>x + b<sub>1</sub>
* z<sub>2</sub> = w<sub>2</sub>α(z<sub>1</sub>) + b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Tutaj α to **nieliniowa funkcja aktywacji**, σ to funkcja softmax, a parametry θ = ⟨*w<sub>1</sub>, b<sub>1</sub>, w<sub>2</sub>, b<sub>2</sub>*⟩.

Algorytm spadku gradientu pozostaje ten sam, ale obliczanie gradientów staje się trudniejsze. Z wykorzystaniem reguły łańcuchowej różniczkowania możemy obliczyć pochodne jako:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Reguła łańcuchowa jest używana do obliczania pochodnych funkcji straty względem parametrów.

Zauważ, że lewostronna część wszystkich tych wyrażeń jest taka sama, dzięki czemu możemy efektywnie obliczać pochodne zaczynając od funkcji straty i idąc „wstecz” przez graf obliczeniowy. Metoda trenowania wielowarstwowego perceptronu nazywa się **propagacją wsteczną**, lub po prostu 'backprop'.

> TODO: cytowanie obrazka

> ✅ Omówimy backpropagation znacznie dokładniej w naszym przykładzie w notatniku.

## Podsumowanie

W tej lekcji stworzyliśmy własną bibliotekę sieci neuronowych i wykorzystaliśmy ją do prostego zadania klasyfikacji dwuwymiarowej.

## 🚀 Wyzwanie

W dołączonym notatniku zaimplementujesz własny framework do budowy i trenowania wielowarstwowych perceptronów. Będziesz mógł dokładnie zobaczyć, jak działają nowoczesne sieci neuronowe.

Przejdź do notatnika OwnFramework i przepracuj go.

## Powtórka i samodzielna nauka

Propagacja wsteczna to powszechny algorytm stosowany w AI i ML, warto zgłębić go bardziej szczegółowo.

## Zadanie

W tym laboratorium masz za zadanie wykorzystać framework, który stworzyłeś w tej lekcji, do rozwiązania problemu klasyfikacji ręcznie pisanych cyfr MNIST.

* Instrukcje
* Notatnik

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do jak największej dokładności, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.