<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-06-25T23:02:12+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "pl"
}
-->
# Frameworky Sieci Neuronowych

Jak już się nauczyliśmy, aby efektywnie trenować sieci neuronowe, musimy zrobić dwie rzeczy:

* Operować na tensorach, np. mnożyć, dodawać i obliczać niektóre funkcje, takie jak sigmoid czy softmax
* Obliczać gradienty wszystkich wyrażeń, aby móc przeprowadzić optymalizację metodą gradientu prostego

Podczas gdy biblioteka `numpy` może wykonać pierwszą część, potrzebujemy mechanizmu do obliczania gradientów. W naszym frameworku, który opracowaliśmy w poprzedniej sekcji, musieliśmy ręcznie programować wszystkie funkcje pochodne wewnątrz metody `backward`, która wykonuje wsteczną propagację. Idealnie, framework powinien dawać nam możliwość obliczania gradientów *dowolnego wyrażenia*, które możemy zdefiniować.

Kolejną ważną rzeczą jest możliwość wykonywania obliczeń na GPU lub innych specjalistycznych jednostkach obliczeniowych, takich jak TPU. Trening głębokich sieci neuronowych wymaga *wielu* obliczeń, a możliwość ich równoległego wykonywania na GPU jest bardzo ważna.

> ✅ Termin 'równoległy' oznacza rozdzielenie obliczeń na wiele urządzeń.

Obecnie dwa najpopularniejsze frameworki sieci neuronowych to: TensorFlow i PyTorch. Oba zapewniają niskopoziomowe API do operowania na tensorach zarówno na CPU, jak i GPU. Na szczycie niskopoziomowego API znajduje się również wyższopoziomowe API, odpowiednio nazwane Keras i PyTorch Lightning.

Niskopoziomowe API | TensorFlow| PyTorch
------------------|-------------------------------------|--------------------------------
Wyższopoziomowe API| Keras| Pytorch

**Niskopoziomowe API** w obu frameworkach pozwala na budowanie tzw. **grafów obliczeniowych**. Graf ten definiuje, jak obliczyć wynik (zwykle funkcję straty) z podanymi parametrami wejściowymi i może być przesłany do obliczeń na GPU, jeśli jest dostępny. Istnieją funkcje do różnicowania tego grafu obliczeniowego i obliczania gradientów, które mogą być następnie użyte do optymalizacji parametrów modelu.

**Wyższopoziomowe API** traktuje sieci neuronowe jako **sekwencję warstw**, co znacznie ułatwia konstruowanie większości sieci neuronowych. Trenowanie modelu zwykle wymaga przygotowania danych, a następnie wywołania funkcji `fit`, aby wykonać zadanie.

Wyższopoziomowe API pozwala na szybkie konstruowanie typowych sieci neuronowych bez martwienia się o wiele szczegółów. Jednocześnie, niskopoziomowe API oferuje znacznie większą kontrolę nad procesem treningu, dlatego jest często używane w badaniach, gdy mamy do czynienia z nowymi architekturami sieci neuronowych.

Ważne jest również zrozumienie, że można używać obu API razem, np. można opracować własną architekturę warstwy sieci przy użyciu niskopoziomowego API, a następnie używać jej wewnątrz większej sieci skonstruowanej i trenowanej za pomocą wyższopoziomowego API. Można również zdefiniować sieć przy użyciu wyższopoziomowego API jako sekwencję warstw, a następnie używać własnej niskopoziomowej pętli treningowej do przeprowadzania optymalizacji. Oba API korzystają z tych samych podstawowych koncepcji i są zaprojektowane tak, aby dobrze współpracować.

## Nauka

W tym kursie oferujemy większość treści zarówno dla PyTorch, jak i TensorFlow. Możesz wybrać preferowany framework i przejść tylko przez odpowiednie notatniki. Jeśli nie jesteś pewien, który framework wybrać, przeczytaj dyskusje w internecie na temat **PyTorch vs. TensorFlow**. Możesz również przyjrzeć się obu frameworkom, aby lepiej je zrozumieć.

Gdzie to możliwe, będziemy używać wyższopoziomowych API dla uproszczenia. Jednak uważamy, że ważne jest zrozumienie, jak sieci neuronowe działają od podstaw, dlatego na początku zaczynamy od pracy z niskopoziomowym API i tensorami. Jednak jeśli chcesz szybko zacząć i nie chcesz poświęcać dużo czasu na naukę tych szczegółów, możesz je pominąć i przejść bezpośrednio do notatników z wyższopoziomowym API.

## ✍️ Ćwiczenia: Frameworki

Kontynuuj naukę w następujących notatnikach:

Niskopoziomowe API | Notatnik TensorFlow+Keras | PyTorch
------------------|-------------------------------------|--------------------------------
Wyższopoziomowe API| Keras | *PyTorch Lightning*

Po opanowaniu frameworków, podsumujmy pojęcie nadmiernego dopasowania.

# Nadmierne Dopasowanie

Nadmierne dopasowanie to niezwykle ważne pojęcie w uczeniu maszynowym i bardzo ważne jest, aby je zrozumieć!

Rozważmy następujący problem aproksymacji 5 punktów (reprezentowanych przez `x` na poniższych wykresach):

!liniowy | nadmierne dopasowanie
-------------------------|--------------------------
**Model liniowy, 2 parametry** | **Model nieliniowy, 7 parametrów**
Błąd treningowy = 5.3 | Błąd treningowy = 0
Błąd walidacyjny = 5.1 | Błąd walidacyjny = 20

* Po lewej widzimy dobre przybliżenie prostą linią. Ponieważ liczba parametrów jest odpowiednia, model dobrze rozumie rozkład punktów.
* Po prawej model jest zbyt potężny. Ponieważ mamy tylko 5 punktów, a model ma 7 parametrów, może dostosować się w taki sposób, aby przechodzić przez wszystkie punkty, co powoduje, że błąd treningowy wynosi 0. Jednak to uniemożliwia modelowi zrozumienie poprawnego wzorca w danych, dlatego błąd walidacyjny jest bardzo wysoki.

Bardzo ważne jest znalezienie odpowiedniej równowagi między bogactwem modelu (liczba parametrów) a liczbą próbek treningowych.

## Dlaczego występuje nadmierne dopasowanie

  * Niewystarczająca ilość danych treningowych
  * Zbyt potężny model
  * Zbyt dużo szumu w danych wejściowych

## Jak wykryć nadmierne dopasowanie

Jak widać na powyższym wykresie, nadmierne dopasowanie można wykryć po bardzo niskim błędzie treningowym i wysokim błędzie walidacyjnym. Zwykle podczas treningu widzimy, że zarówno błędy treningowe, jak i walidacyjne zaczynają się zmniejszać, a następnie w pewnym momencie błąd walidacyjny może przestać się zmniejszać i zacząć rosnąć. To będzie znak nadmiernego dopasowania i wskaźnik, że powinniśmy prawdopodobnie przerwać trening w tym momencie (lub przynajmniej zrobić migawkę modelu).

nadmierne dopasowanie

## Jak zapobiec nadmiernemu dopasowaniu

Jeśli zauważysz, że występuje nadmierne dopasowanie, możesz zrobić jedno z poniższych:

 * Zwiększyć ilość danych treningowych
 * Zmniejszyć złożoność modelu
 * Zastosować technikę regularizacji, taką jak Dropout, którą rozważymy później.

## Nadmierne Dopasowanie i Kompromis Błąd-Przekrój

Nadmierne dopasowanie jest w rzeczywistości przypadkiem bardziej ogólnego problemu w statystyce, zwanego Kompromisem Błąd-Przekrój. Jeśli rozważymy możliwe źródła błędu w naszym modelu, możemy wyróżnić dwa rodzaje błędów:

* **Błędy uprzedzenia** są spowodowane tym, że nasz algorytm nie jest w stanie poprawnie uchwycić relacji między danymi treningowymi. Może to wynikać z faktu, że nasz model nie jest wystarczająco potężny (**niedopasowanie**).
* **Błędy wariancji**, które są spowodowane tym, że model aproksymuje szum w danych wejściowych zamiast znaczącej relacji (**nadmierne dopasowanie**).

Podczas treningu błąd uprzedzenia maleje (nasz model uczy się aproksymować dane), a błąd wariancji rośnie. Ważne jest, aby przerwać trening - albo ręcznie (gdy wykryjemy nadmierne dopasowanie), albo automatycznie (poprzez wprowadzenie regularizacji) - aby zapobiec nadmiernemu dopasowaniu.

## Podsumowanie

W tej lekcji nauczyłeś się o różnicach między różnymi API dla dwóch najpopularniejszych frameworków AI, TensorFlow i PyTorch. Dodatkowo nauczyłeś się o bardzo ważnym temacie, nadmiernym dopasowaniu.

## 🚀 Wyzwanie

W towarzyszących notatnikach znajdziesz 'zadania' na dole; przejdź przez notatniki i wykonaj zadania.

## Przegląd i Samodzielna Nauka

Przeprowadź badania na następujące tematy:

- TensorFlow
- PyTorch
- Nadmierne dopasowanie

Zadaj sobie następujące pytania:

- Jaka jest różnica między TensorFlow a PyTorch?
- Jaka jest różnica między nadmiernym dopasowaniem a niedopasowaniem?

## Zadanie

W tym laboratorium jesteś proszony o rozwiązanie dwóch problemów klasyfikacyjnych przy użyciu sieci w pełni połączonych z jedną i wieloma warstwami, korzystając z PyTorch lub TensorFlow.

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się o dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uważany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.