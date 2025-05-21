<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-05-20T02:19:11+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "pl"
}
-->
# Wprowadzenie do sieci neuronowych. Perceptron wielowarstwowy

W poprzedniej sekcji dowiedziałeś się o najprostszym modelu sieci neuronowej - perceptronie jednowarstwowym, modelu liniowej klasyfikacji dwuklasowej.

W tej sekcji rozszerzymy ten model do bardziej elastycznego frameworka, który pozwoli nam na:

* przeprowadzanie **klasyfikacji wieloklasowej** oprócz dwuklasowej
* rozwiązywanie **problemów regresji** oprócz klasyfikacji
* rozdzielanie klas, które nie są liniowo separowalne

Rozwiniemy również własny modułowy framework w Pythonie, który pozwoli nam konstruować różne architektury sieci neuronowych.

## Formalizacja uczenia maszynowego

Zacznijmy od formalizacji problemu uczenia maszynowego. Załóżmy, że mamy zbiór danych treningowych **X** z etykietami **Y**, i musimy zbudować model *f*, który będzie dokonywał najdokładniejszych przewidywań. Jakość przewidywań jest mierzalna przez **funkcję strat** ℒ. Często używane są następujące funkcje strat:

* W przypadku problemu regresji, kiedy musimy przewidzieć liczbę, możemy użyć **błędu bezwzględnego** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, lub **błędu kwadratowego** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* W przypadku klasyfikacji, używamy **straty 0-1** (która jest w zasadzie tym samym co **dokładność** modelu), lub **straty logistycznej**.

Dla perceptronu jednowarstwowego, funkcja *f* była definiowana jako funkcja liniowa *f(x)=wx+b* (tutaj *w* to macierz wag, *x* to wektor cech wejściowych, a *b* to wektor biasu). Dla różnych architektur sieci neuronowych, ta funkcja może przyjąć bardziej złożoną formę.

> W przypadku klasyfikacji często pożądane jest uzyskanie prawdopodobieństw odpowiadających klas jako wyjście sieci. Aby przekształcić dowolne liczby na prawdopodobieństwa (np. aby znormalizować wyjście), często używamy funkcji **softmax** σ, i funkcja *f* staje się *f(x)=σ(wx+b)*

W definicji *f* powyżej, *w* i *b* nazywane są **parametrami** θ=⟨*w,b*⟩. Mając zbiór danych ⟨**X**,**Y**⟩, możemy obliczyć całkowity błąd na całym zbiorze danych jako funkcję parametrów θ.

> ✅ **Celem treningu sieci neuronowej jest minimalizacja błędu poprzez zmienianie parametrów θ**

## Optymalizacja metodą gradientu prostego

Istnieje dobrze znana metoda optymalizacji funkcji zwana **metodą gradientu prostego**. Pomysł polega na tym, że możemy obliczyć pochodną (w przypadku wielowymiarowym nazywaną **gradientem**) funkcji strat względem parametrów i zmieniać parametry w taki sposób, aby błąd się zmniejszał. Można to sformalizować w następujący sposób:

* Zainicjuj parametry losowymi wartościami w<sup>(0)</sup>, b<sup>(0)</sup>
* Powtarzaj następujący krok wiele razy:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Podczas treningu, kroki optymalizacji powinny być obliczane z uwzględnieniem całego zbioru danych (pamiętaj, że strata jest obliczana jako suma przez wszystkie próbki treningowe). Jednak w rzeczywistości bierzemy małe części zbioru danych zwane **minibatchami** i obliczamy gradienty na podstawie podzbioru danych. Ponieważ podzbiór jest wybierany losowo za każdym razem, taka metoda nazywana jest **stochastycznym gradientem prostym** (SGD).

## Perceptrony wielowarstwowe i wsteczna propagacja błędów

Jednowarstwowa sieć, jak widzieliśmy powyżej, jest zdolna do klasyfikowania klas liniowo separowalnych. Aby zbudować bogatszy model, możemy połączyć kilka warstw sieci. Matematycznie oznaczałoby to, że funkcja *f* miałaby bardziej złożoną formę i byłaby obliczana w kilku krokach:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Tutaj, α jest **nieliniową funkcją aktywacji**, σ jest funkcją softmax, a parametry θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algorytm gradientu prostego pozostanie taki sam, ale obliczanie gradientów będzie bardziej skomplikowane. Z uwagi na regułę różniczkowania łańcuchowego, możemy obliczyć pochodne jako:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Reguła różniczkowania łańcuchowego jest używana do obliczania pochodnych funkcji strat względem parametrów.

Zauważ, że lewa część wszystkich tych wyrażeń jest taka sama, dlatego możemy skutecznie obliczać pochodne, zaczynając od funkcji strat i idąc "wstecz" przez graf obliczeniowy. Dlatego metoda trenowania perceptronu wielowarstwowego nazywa się **wsteczną propagacją błędów**, lub 'backprop'.

> TODO: cytowanie obrazu

> ✅ W naszym przykładowym notatniku omówimy wsteczną propagację błędów znacznie bardziej szczegółowo.

## Podsumowanie

W tej lekcji zbudowaliśmy własną bibliotekę sieci neuronowych i użyliśmy jej do prostego zadania klasyfikacji dwuwymiarowej.

## 🚀 Wyzwanie

W dołączonym notatniku zaimplementujesz własny framework do budowania i trenowania perceptronów wielowarstwowych. Będziesz mógł zobaczyć szczegółowo, jak działają nowoczesne sieci neuronowe.

Przejdź do notatnika OwnFramework i przepracuj go.

## Przegląd i samodzielne studia

Wsteczna propagacja błędów jest powszechnym algorytmem używanym w AI i ML, warto ją zgłębić bardziej szczegółowo.

## Zadanie

W tym laboratorium jesteś proszony o użycie frameworka, który skonstruowałeś w tej lekcji, do rozwiązania klasyfikacji ręcznie pisanych cyfr MNIST.

* Instrukcje
* Notatnik

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uważany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się profesjonalne tłumaczenie przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.