<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-06-25T23:23:26+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "pl"
}
-->
# Wprowadzenie do Sieci Neuronowych. Perceptron Wielowarstwowy

W poprzedniej sekcji nauczyłeś się o najprostszym modelu sieci neuronowej - perceptronie jednowarstwowym, będącym liniowym modelem klasyfikacji dwuklasowej.

W tej sekcji rozszerzymy ten model do bardziej elastycznego frameworku, który pozwoli nam na:

* przeprowadzanie **klasyfikacji wieloklasowej** oprócz dwuklasowej
* rozwiązywanie **problemów regresji** oprócz klasyfikacji
* rozdzielanie klas, które nie są liniowo separowalne

Opracujemy również własny modułowy framework w Pythonie, który pozwoli nam na budowanie różnych architektur sieci neuronowych.

## Formalizacja Uczenia Maszynowego

Zacznijmy od formalizacji problemu Uczenia Maszynowego. Załóżmy, że mamy zbiór danych treningowych **X** z etykietami **Y**, i musimy zbudować model *f*, który będzie dokonywał jak najdokładniejszych prognoz. Jakość prognoz mierzona jest za pomocą **funkcji straty** ℒ. Często używane funkcje straty to:

* W przypadku problemu regresji, gdy musimy przewidzieć liczbę, możemy użyć **błędu bezwzględnego** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, lub **błędu kwadratowego** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Dla klasyfikacji używamy **straty 0-1** (która jest zasadniczo taka sama jak **dokładność** modelu), lub **straty logistycznej**.

Dla perceptronu jednowarstwowego, funkcja *f* była zdefiniowana jako funkcja liniowa *f(x)=wx+b* (gdzie *w* jest macierzą wag, *x* jest wektorem cech wejściowych, a *b* jest wektorem przesunięcia). Dla różnych architektur sieci neuronowych, ta funkcja może przyjąć bardziej złożoną formę.

> W przypadku klasyfikacji, często pożądane jest uzyskanie prawdopodobieństw odpowiadających klas jako wyjście sieci. Aby przekształcić dowolne liczby na prawdopodobieństwa (np. aby znormalizować wyjście), często używamy funkcji **softmax** σ, a funkcja *f* staje się *f(x)=σ(wx+b)*

W powyższej definicji *f*, *w* i *b* nazywane są **parametrami** θ=⟨*w,b*⟩. Mając zbiór danych ⟨**X**,**Y**⟩, możemy obliczyć ogólny błąd na całym zbiorze danych jako funkcję parametrów θ.

> ✅ **Celem treningu sieci neuronowej jest minimalizacja błędu poprzez zmianę parametrów θ**

## Optymalizacja za pomocą Gradientu

Istnieje dobrze znana metoda optymalizacji funkcji zwana **gradientem zstępującym**. Idea polega na tym, że możemy obliczyć pochodną (w przypadku wielowymiarowym nazywaną **gradientem**) funkcji straty względem parametrów i zmieniać parametry w taki sposób, aby błąd się zmniejszał. Można to sformalizować w następujący sposób:

* Zainicjuj parametry losowymi wartościami w<sup>(0)</sup>, b<sup>(0)</sup>
* Powtarzaj następujący krok wiele razy:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Podczas treningu, kroki optymalizacji powinny być obliczane z uwzględnieniem całego zbioru danych (pamiętaj, że strata jest obliczana jako suma przez wszystkie próbki treningowe). Jednak w rzeczywistości bierzemy małe porcje zbioru danych zwane **minipaczkami**, i obliczamy gradienty na podstawie podzbioru danych. Ponieważ podzbiór jest wybierany losowo za każdym razem, taka metoda nazywa się **stochastycznym gradientem zstępującym** (SGD).

## Perceptrony Wielowarstwowe i Wsteczna Propagacja

Sieć jednowarstwowa, jak widzieliśmy powyżej, jest zdolna do klasyfikacji klas liniowo separowalnych. Aby zbudować bogatszy model, możemy połączyć kilka warstw sieci. Matematycznie oznaczałoby to, że funkcja *f* miałaby bardziej złożoną formę i byłaby obliczana w kilku krokach:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Tutaj, α jest **nieliniową funkcją aktywacji**, σ jest funkcją softmax, a parametry θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algorytm gradientu zstępującego pozostałby taki sam, ale trudniej byłoby obliczyć gradienty. Zgodnie z regułą różniczkowania łańcuchowego, możemy obliczyć pochodne jako:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Reguła różniczkowania łańcuchowego jest używana do obliczania pochodnych funkcji straty względem parametrów.

Zauważ, że lewa część wszystkich tych wyrażeń jest taka sama, dlatego możemy efektywnie obliczać pochodne zaczynając od funkcji straty i idąc "wstecz" przez graf obliczeniowy. Dlatego metoda trenowania perceptronu wielowarstwowego nazywa się **wsteczną propagacją**, lub 'backprop'.

> TODO: cytowanie obrazu

> ✅ Omówimy wsteczną propagację znacznie bardziej szczegółowo w naszym przykładzie w notatniku.  

## Podsumowanie

W tej lekcji zbudowaliśmy własną bibliotekę sieci neuronowych i użyliśmy jej do prostego zadania klasyfikacji dwuwymiarowej.

## 🚀 Wyzwanie

W towarzyszącym notatniku zaimplementujesz własny framework do budowania i trenowania perceptronów wielowarstwowych. Będziesz mógł zobaczyć szczegółowo, jak działają nowoczesne sieci neuronowe.

Przejdź do notatnika OwnFramework i przepracuj go.

## Przegląd i Samodzielna Nauka

Wsteczna propagacja jest powszechnym algorytmem używanym w AI i ML, warto go studiować bardziej szczegółowo.

## Zadanie

W tym laboratorium zostaniesz poproszony o użycie frameworku, który skonstruowałeś w tej lekcji, do rozwiązania problemu klasyfikacji ręcznie pisanych cyfr MNIST.

* Instrukcje
* Notatnik

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się o dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uważany za źródło autorytatywne. Dla informacji o kluczowym znaczeniu zaleca się profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.