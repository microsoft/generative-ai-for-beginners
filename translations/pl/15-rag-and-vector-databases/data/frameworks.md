<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-07-09T16:31:16+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "pl"
}
-->
# Frameworki sieci neuronowych

Jak już wiemy, aby efektywnie trenować sieci neuronowe, musimy zrobić dwie rzeczy:

* Operować na tensorach, np. mnożyć, dodawać oraz obliczać funkcje takie jak sigmoid czy softmax
* Obliczać gradienty wszystkich wyrażeń, aby móc przeprowadzić optymalizację metodą spadku gradientu

Chociaż biblioteka `numpy` radzi sobie z pierwszą częścią, potrzebujemy mechanizmu do obliczania gradientów. W naszym frameworku, który stworzyliśmy w poprzedniej sekcji, musieliśmy ręcznie programować wszystkie funkcje pochodnych w metodzie `backward`, która realizuje propagację wsteczną. Idealnie, framework powinien dawać możliwość obliczania gradientów *dowolnego wyrażenia*, które zdefiniujemy.

Kolejną ważną rzeczą jest możliwość wykonywania obliczeń na GPU lub innych wyspecjalizowanych jednostkach obliczeniowych, takich jak TPU. Trening głębokich sieci neuronowych wymaga *bardzo dużej* liczby obliczeń, a możliwość ich równoległego wykonywania na GPU jest niezwykle istotna.

> ✅ Termin 'parallelize' oznacza rozdzielenie obliczeń na wiele urządzeń.

Obecnie dwa najpopularniejsze frameworki do sieci neuronowych to: TensorFlow i PyTorch. Oba oferują niskopoziomowe API do operacji na tensorach zarówno na CPU, jak i GPU. Na bazie niskopoziomowego API dostępne są także wyższe poziomy API, odpowiednio Keras i PyTorch Lightning.

Low-Level API | TensorFlow | PyTorch
--------------|-------------------------------------|--------------------------------
High-level API| Keras | PyTorch

**Niskopoziomowe API** w obu frameworkach pozwalają budować tzw. **grafy obliczeniowe**. Graf ten definiuje, jak obliczyć wynik (zwykle funkcję straty) dla podanych parametrów wejściowych i może być wykonany na GPU, jeśli jest dostępne. Istnieją funkcje do różniczkowania tego grafu i obliczania gradientów, które następnie można wykorzystać do optymalizacji parametrów modelu.

**Wysokopoziomowe API** traktują sieci neuronowe jako **sekwencję warstw** i znacznie ułatwiają budowę większości sieci neuronowych. Trening modelu zwykle wymaga przygotowania danych, a następnie wywołania funkcji `fit`, która wykonuje cały proces.

Wysokopoziomowe API pozwala szybko tworzyć typowe sieci neuronowe bez martwienia się o wiele szczegółów. Jednocześnie niskopoziomowe API dają dużo większą kontrolę nad procesem treningu, dlatego są często wykorzystywane w badaniach, gdy pracujemy z nowymi architekturami sieci neuronowych.

Ważne jest też zrozumienie, że można używać obu API razem, np. można stworzyć własną architekturę warstwy sieci korzystając z niskopoziomowego API, a następnie użyć jej w większej sieci zbudowanej i trenowanej za pomocą wysokopoziomowego API. Można też zdefiniować sieć jako sekwencję warstw w wysokopoziomowym API, a następnie użyć własnej pętli treningowej na niskim poziomie do optymalizacji. Oba API opierają się na tych samych podstawowych koncepcjach i zostały zaprojektowane tak, aby dobrze ze sobą współpracować.

## Nauka

W tym kursie oferujemy większość materiałów zarówno dla PyTorch, jak i TensorFlow. Możesz wybrać preferowany framework i przejść tylko przez odpowiadające mu notatniki. Jeśli nie jesteś pewien, który framework wybrać, przeczytaj dyskusje w internecie na temat **PyTorch vs. TensorFlow**. Możesz też zapoznać się z oboma frameworkami, aby lepiej je zrozumieć.

Tam, gdzie to możliwe, będziemy korzystać z wysokopoziomowych API dla uproszczenia. Jednak uważamy, że ważne jest zrozumienie działania sieci neuronowych od podstaw, dlatego na początku zaczynamy od pracy z niskopoziomowym API i tensorami. Jeśli jednak chcesz szybko zacząć i nie chcesz poświęcać dużo czasu na naukę tych szczegółów, możesz pominąć ten etap i przejść od razu do notatników z wysokopoziomowym API.

## ✍️ Ćwiczenia: Frameworki

Kontynuuj naukę w następujących notatnikach:

Low-Level API | TensorFlow+Keras Notebook | PyTorch
--------------|-------------------------------------|--------------------------------
High-level API| Keras | *PyTorch Lightning*

Po opanowaniu frameworków, podsumujmy pojęcie overfittingu.

# Overfitting

Overfitting to niezwykle ważne pojęcie w uczeniu maszynowym i bardzo istotne jest, aby je dobrze zrozumieć!

Rozważmy problem aproksymacji 5 punktów (oznaczonych jako `x` na poniższych wykresach):

!linear | overfit
-------------------------|--------------------------
**Model liniowy, 2 parametry** | **Model nieliniowy, 7 parametrów**
Błąd treningowy = 5.3 | Błąd treningowy = 0
Błąd walidacyjny = 5.1 | Błąd walidacyjny = 20

* Po lewej widzimy dobrą liniową aproksymację. Ponieważ liczba parametrów jest odpowiednia, model dobrze uchwycił rozkład punktów.
* Po prawej model jest zbyt złożony. Ponieważ mamy tylko 5 punktów, a model ma 7 parametrów, może tak się dopasować, że przejdzie przez wszystkie punkty, co daje błąd treningowy równy 0. Jednak uniemożliwia to modelowi zrozumienie prawidłowego wzoru danych, dlatego błąd walidacyjny jest bardzo wysoki.

Bardzo ważne jest znalezienie właściwej równowagi między złożonością modelu (liczbą parametrów) a liczbą próbek treningowych.

## Dlaczego występuje overfitting

  * Za mało danych treningowych
  * Model zbyt złożony
  * Zbyt dużo szumu w danych wejściowych

## Jak wykryć overfitting

Jak widać na powyższym wykresie, overfitting można wykryć po bardzo niskim błędzie treningowym i wysokim błędzie walidacyjnym. Zazwyczaj podczas treningu oba błędy – treningowy i walidacyjny – zaczynają spadać, a następnie w pewnym momencie błąd walidacyjny przestaje maleć i zaczyna rosnąć. To jest sygnał overfittingu i wskazówka, że powinniśmy prawdopodobnie zatrzymać trening w tym momencie (lub przynajmniej zrobić migawkę modelu).

overfitting

## Jak zapobiegać overfittingowi

Jeśli zauważysz, że występuje overfitting, możesz zrobić jedną z następujących rzeczy:

 * Zwiększyć ilość danych treningowych
 * Zmniejszyć złożoność modelu
 * Zastosować technikę regularizacji, taką jak Dropout, którą omówimy później.

## Overfitting a kompromis Bias-Variance

Overfitting jest właściwie przypadkiem bardziej ogólnego problemu w statystyce zwanego kompromisem Bias-Variance. Jeśli rozważymy możliwe źródła błędów w naszym modelu, możemy wyróżnić dwa typy błędów:

* **Błędy bias** są spowodowane tym, że nasz algorytm nie potrafi poprawnie uchwycić zależności w danych treningowych. Może to wynikać z faktu, że model nie jest wystarczająco złożony (**underfitting**).
* **Błędy wariancji**, które wynikają z tego, że model aproksymuje szum w danych wejściowych zamiast istotnych zależności (**overfitting**).

Podczas treningu błąd bias maleje (gdy model uczy się aproksymować dane), a błąd wariancji rośnie. Ważne jest, aby zatrzymać trening – albo ręcznie (gdy wykryjemy overfitting), albo automatycznie (poprzez wprowadzenie regularizacji) – aby zapobiec overfittingowi.

## Podsumowanie

W tej lekcji dowiedziałeś się o różnicach między różnymi API w dwóch najpopularniejszych frameworkach AI, TensorFlow i PyTorch. Ponadto poznałeś bardzo ważny temat, jakim jest overfitting.

## 🚀 Wyzwanie

W dołączonych notatnikach znajdziesz na dole „zadania”; przejdź przez notatniki i wykonaj te zadania.

## Powtórka i samodzielna nauka

Zrób research na następujące tematy:

- TensorFlow
- PyTorch
- Overfitting

Zadaj sobie następujące pytania:

- Jaka jest różnica między TensorFlow a PyTorch?
- Jaka jest różnica między overfittingiem a underfittingiem?

## Zadanie

W tym laboratorium masz rozwiązać dwa problemy klasyfikacji, używając jedno- i wielowarstwowych w pełni połączonych sieci, korzystając z PyTorch lub TensorFlow.

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.