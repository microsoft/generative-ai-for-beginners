<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-05-20T01:57:51+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "pl"
}
-->
# Frameworky sieci neuronowych

Jak już się nauczyliśmy, aby móc efektywnie trenować sieci neuronowe, musimy zrobić dwie rzeczy:

* Operować na tensorach, np. mnożyć, dodawać i obliczać pewne funkcje, takie jak sigmoid czy softmax
* Obliczać gradienty wszystkich wyrażeń, aby przeprowadzić optymalizację metodą gradientu

Podczas gdy biblioteka `numpy` może zrobić pierwszą część, potrzebujemy mechanizmu do obliczania gradientów. W naszym frameworku, który opracowaliśmy w poprzedniej sekcji, musieliśmy ręcznie programować wszystkie funkcje pochodne wewnątrz metody `backward`, która wykonuje propagację wsteczną. Idealnie, framework powinien dawać nam możliwość obliczania gradientów *dowolnego wyrażenia*, które możemy zdefiniować.

Kolejną ważną rzeczą jest możliwość wykonywania obliczeń na GPU lub innych specjalistycznych jednostkach obliczeniowych, takich jak TPU. Trening głębokich sieci neuronowych wymaga *wiele* obliczeń, a możliwość ich równoległego wykonywania na GPU jest bardzo ważna.

> ✅ Termin 'równoległe wykonywanie' oznacza rozdzielenie obliczeń na wiele urządzeń.

Obecnie dwa najpopularniejsze frameworki sieci neuronowych to: TensorFlow i PyTorch. Oba zapewniają niskopoziomowe API do operacji na tensorach zarówno na CPU, jak i GPU. Na niskopoziomowym API znajduje się również wyższopoziomowe API, zwane odpowiednio Keras i PyTorch Lightning.

Niskopoziomowe API | TensorFlow| PyTorch
------------------|-------------------------------------|--------------------------------
Wyższopoziomowe API| Keras| Pytorch

**Niskopoziomowe API** w obu frameworkach pozwalają na budowanie tzw. **grafów obliczeniowych**. Ten graf definiuje, jak obliczyć wynik (zazwyczaj funkcję straty) z podanymi parametrami wejściowymi i może być przesłany do obliczeń na GPU, jeśli jest dostępny. Istnieją funkcje do różnicowania tego grafu obliczeniowego i obliczania gradientów, które mogą być następnie użyte do optymalizacji parametrów modelu.

**Wyższopoziomowe API** traktują sieci neuronowe jako **sekwencję warstw** i ułatwiają konstruowanie większości sieci neuronowych. Trenowanie modelu zazwyczaj wymaga przygotowania danych, a następnie wywołania funkcji `fit`, aby wykonać zadanie.

Wyższopoziomowe API pozwala na szybkie konstruowanie typowych sieci neuronowych bez martwienia się o wiele szczegółów. Jednocześnie niskopoziomowe API oferuje dużo większą kontrolę nad procesem treningu i dlatego jest często używane w badaniach, gdy pracujemy z nowymi architekturami sieci neuronowych.

Ważne jest również zrozumienie, że można używać obu API razem, np. można opracować własną architekturę warstwy sieciowej za pomocą niskopoziomowego API, a następnie użyć jej wewnątrz większej sieci skonstruowanej i trenowanej za pomocą wyższopoziomowego API. Można również zdefiniować sieć za pomocą wyższopoziomowego API jako sekwencję warstw, a następnie użyć własnej pętli treningowej na niskim poziomie do przeprowadzenia optymalizacji. Oba API korzystają z tych samych podstawowych koncepcji i są zaprojektowane, aby dobrze ze sobą współpracować.

## Nauka

W tym kursie oferujemy większość treści zarówno dla PyTorch, jak i TensorFlow. Możesz wybrać preferowany framework i przejść tylko przez odpowiadające mu notatniki. Jeśli nie jesteś pewien, który framework wybrać, przeczytaj kilka dyskusji w internecie na temat **PyTorch vs. TensorFlow**. Możesz także przyjrzeć się obu frameworkom, aby lepiej je zrozumieć.

Tam, gdzie to możliwe, będziemy używać wyższopoziomowych API dla prostoty. Jednak uważamy, że ważne jest zrozumienie, jak działają sieci neuronowe od podstaw, dlatego na początku zaczynamy od pracy z niskopoziomowym API i tensorami. Jeśli jednak chcesz szybko zacząć i nie chcesz poświęcać dużo czasu na naukę tych szczegółów, możesz je pominąć i przejść bezpośrednio do notatników wyższopoziomowego API.

## ✍️ Ćwiczenia: Frameworky

Kontynuuj naukę w następujących notatnikach:

Niskopoziomowe API | TensorFlow+Keras Notebook | PyTorch
------------------|-------------------------------------|--------------------------------
Wyższopoziomowe API| Keras | *PyTorch Lightning*

Po opanowaniu frameworków, przypomnijmy sobie pojęcie przeuczenia.

# Przeuczenie

Przeuczenie to niezwykle ważna koncepcja w uczeniu maszynowym i bardzo ważne jest, aby ją zrozumieć!

Rozważmy następujący problem aproksymacji 5 punktów (reprezentowanych przez `x` na poniższych wykresach):

!liniowy | przeuczenie
-------------------------|--------------------------
**Model liniowy, 2 parametry** | **Model nieliniowy, 7 parametrów**
Błąd treningowy = 5.3 | Błąd treningowy = 0
Błąd walidacyjny = 5.1 | Błąd walidacyjny = 20

* Po lewej widzimy dobrą aproksymację liniową. Ponieważ liczba parametrów jest odpowiednia, model dobrze rozumie rozkład punktów.
* Po prawej model jest zbyt potężny. Ponieważ mamy tylko 5 punktów, a model ma 7 parametrów, może dostosować się w taki sposób, że przechodzi przez wszystkie punkty, powodując, że błąd treningowy wynosi 0. Jednak to uniemożliwia modelowi zrozumienie właściwego wzorca danych, dlatego błąd walidacyjny jest bardzo wysoki.

Bardzo ważne jest znalezienie właściwej równowagi między bogactwem modelu (liczbą parametrów) a liczbą próbek treningowych.

## Dlaczego występuje przeuczenie

  * Za mało danych treningowych
  * Zbyt potężny model
  * Zbyt duży szum w danych wejściowych

## Jak wykryć przeuczenie

Jak widać na powyższym wykresie, przeuczenie można wykryć przez bardzo niski błąd treningowy i wysoki błąd walidacyjny. Zazwyczaj podczas treningu widzimy, że zarówno błędy treningowe, jak i walidacyjne zaczynają się zmniejszać, a następnie w pewnym momencie błąd walidacyjny może przestać się zmniejszać i zacząć rosnąć. To będzie znak przeuczenia i wskazówka, że prawdopodobnie powinniśmy zatrzymać trening w tym momencie (lub przynajmniej zrobić migawkę modelu).

przeuczenie

## Jak zapobiegać przeuczeniu

Jeśli zauważysz, że występuje przeuczenie, możesz zrobić jedno z następujących:

 * Zwiększyć ilość danych treningowych
 * Zmniejszyć złożoność modelu
 * Użyć techniki regularizacji, takiej jak Dropout, którą omówimy później.

## Przeuczenie a kompromis między błędem uprzedzenia a błędem zmienności

Przeuczenie jest w rzeczywistości przypadkiem bardziej ogólnego problemu w statystyce, zwanego kompromisem między błędem uprzedzenia a błędem zmienności. Jeśli rozważymy możliwe źródła błędu w naszym modelu, możemy wyróżnić dwa rodzaje błędów:

* **Błędy uprzedzenia** są spowodowane tym, że nasz algorytm nie jest w stanie poprawnie uchwycić relacji między danymi treningowymi. Może to wynikać z faktu, że nasz model nie jest wystarczająco potężny (**niedouczenie**).
* **Błędy zmienności**, które są spowodowane tym, że model aproksymuje szum w danych wejściowych zamiast znaczącej relacji (**przeuczenie**).

Podczas treningu błąd uprzedzenia maleje (gdy nasz model uczy się aproksymować dane), a błąd zmienności rośnie. Ważne jest, aby zatrzymać trening - albo ręcznie (gdy wykryjemy przeuczenie) albo automatycznie (wprowadzając regularizację) - aby zapobiec przeuczeniu.

## Podsumowanie

W tej lekcji nauczyłeś się o różnicach między różnymi API dla dwóch najpopularniejszych frameworków AI, TensorFlow i PyTorch. Ponadto nauczyłeś się o bardzo ważnym temacie, przeuczeniu.

## 🚀 Wyzwanie

W towarzyszących notatnikach znajdziesz 'zadania' na dole; przejdź przez notatniki i wykonaj zadania.

## Przegląd i Samodzielne Studia

Przeprowadź badania na następujące tematy:

- TensorFlow
- PyTorch
- Przeuczenie

Zadaj sobie następujące pytania:

- Jaka jest różnica między TensorFlow a PyTorch?
- Jaka jest różnica między przeuczeniem a niedouczeniem?

## Zadanie

W tym laboratorium prosisz się o rozwiązanie dwóch problemów klasyfikacyjnych za pomocą sieci w pełni połączonych jednowarstwowych i wielowarstwowych, używając PyTorch lub TensorFlow.

**Zrzeczenie się odpowiedzialności**:  
Ten dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.