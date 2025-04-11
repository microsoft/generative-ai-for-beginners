# Tworzenie Zaawansowanych Promptów

[![Tworzenie Zaawansowanych Promptów](../../images/05-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson5-gh?WT.mc_id=academic-105485-koreyst?WT.mc_id=academic-105485-koreyst)

Przypomnijmy kilka wniosków z poprzedniego rozdziału:

> Inżynieria promptów to proces, w którym **kierujemy model w stronę bardziej trafnych odpowiedzi** poprzez dostarczanie bardziej użytecznych instrukcji lub kontekstu.

Istnieją też dwa kroki w tworzeniu promptów: konstruowanie promptu poprzez dostarczanie odpowiedniego kontekstu, oraz druga część - _optymalizacja_, czyli jak stopniowo ulepszać prompt.

Na tym etapie mamy podstawowe zrozumienie, jak pisać prompty, ale musimy zagłębić się bardziej. W tym rozdziale przejdziesz od wypróbowywania różnych promptów do zrozumienia, dlaczego jeden prompt jest lepszy od drugiego. Nauczysz się konstruować prompty, stosując podstawowe techniki, które można zastosować do dowolnego LLM.

## Wprowadzenie

W tym rozdziale omówimy następujące tematy:

- Rozszerzenie wiedzy o inżynierii promptów poprzez zastosowanie różnych technik do Twoich promptów.
- Konfigurowanie promptów w celu zróżnicowania wyników.

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafić:

- Stosować techniki inżynierii promptów, które poprawiają wyniki Twoich promptów.
- Wykonywać promptowanie, które jest zróżnicowane lub deterministyczne.

## Inżynieria promptów

Inżynieria promptów to proces tworzenia promptów, które przyniosą pożądany rezultat. Inżynieria promptów to więcej niż tylko pisanie tekstowego promptu. Inżynieria promptów nie jest dyscypliną inżynieryjną, to raczej zestaw technik, które można zastosować, aby uzyskać pożądany wynik.

### Przykład promptu

Weźmy podstawowy prompt, taki jak ten:

> Wygeneruj 10 pytań dotyczących geografii.

W tym prompcie stosujesz w rzeczywistości zestaw różnych technik promptowania.

Rozłóżmy to na części.

- **Kontekst**, określasz, że powinno to dotyczyć "geografii".
- **Ograniczenie wyników**, chcesz nie więcej niż 10 pytań.

### Ograniczenia prostego promptowania

Możesz otrzymać lub nie otrzymać pożądanego wyniku. Pytania zostaną wygenerowane, ale geografia to duży temat i możesz nie dostać tego, czego chcesz, z następujących powodów:

- **Duży temat**, nie wiesz, czy będzie to o krajach, stolicach, rzekach i tak dalej.
- **Format**, co jeśli chciałeś, aby pytania były sformatowane w określony sposób?

Jak widać, jest wiele do rozważenia przy tworzeniu promptów.

Do tej pory widzieliśmy prosty przykład promptu, ale generatywna sztuczna inteligencja jest zdolna do znacznie więcej, aby pomóc ludziom w różnych rolach i branżach. Przyjrzyjmy się teraz kilku podstawowym technikom.

### Techniki promptowania

Najpierw musimy zrozumieć, że promptowanie jest _emergentną_ właściwością LLM, co oznacza, że nie jest to funkcja wbudowana w model, a raczej coś, co odkrywamy w trakcie korzystania z modelu.

Istnieje kilka podstawowych technik, których możemy używać do promptowania LLM. Przyjrzyjmy się im.

- **Promptowanie zero-shot**, to najbardziej podstawowa forma promptowania. Jest to pojedynczy prompt żądający odpowiedzi od LLM wyłącznie na podstawie jego danych treningowych.
- **Promptowanie few-shot**, ten rodzaj promptowania kieruje LLM poprzez dostarczenie 1 lub więcej przykładów, na których może bazować przy generowaniu odpowiedzi.
- **Chain-of-thought (łańcuch myślowy)**, ten rodzaj promptowania mówi LLM, jak rozbić problem na kroki.
- **Generated knowledge (wygenerowana wiedza)**, aby poprawić odpowiedź promptu, możesz dodatkowo dostarczyć wygenerowane fakty lub wiedzę do swojego promptu.
- **Least to most (od najmniejszego do największego)**, podobnie jak chain-of-thought, ta technika polega na rozbiciu problemu na serię kroków, a następnie prośbie o wykonanie tych kroków po kolei.
- **Self-refine (samodoskonalenie)**, ta technika polega na krytykowaniu wyników LLM, a następnie prośbie o ich ulepszenie.
- **Maieutic prompting (promptowanie majeutyczne)**. Chodzi tu o to, aby upewnić się, że odpowiedź LLM jest poprawna, prosząc o wyjaśnienie różnych części odpowiedzi. Jest to forma samodoskonalenia.

### Promptowanie zero-shot

Ten styl promptowania jest bardzo prosty, składa się z pojedynczego promptu. Ta technika to prawdopodobnie to, czego używasz, gdy zaczynasz uczyć się o LLM. Oto przykład:

- Prompt: "Czym jest algebra?"
- Odpowiedź: "Algebra to gałąź matematyki, która bada symbole matematyczne i reguły manipulowania tymi symbolami."

### Promptowanie few-shot

Ten styl promptowania pomaga modelowi poprzez dostarczenie kilku przykładów wraz z prośbą. Składa się z pojedynczego promptu z dodatkowymi danymi specyficznymi dla zadania. Oto przykład:

- Prompt: "Napisz wiersz w stylu Szekspira. Oto kilka przykładów sonetów szekspirowskich.:
  Sonet 18: 'Shall I compare thee to a summer's day? Thou art more lovely and more temperate...'
  Sonet 116: 'Let me not to the marriage of true minds Admit impediments. Love is not love Which alters when it alteration finds...'
  Sonet 132: 'Thine eyes I love, and they, as pitying me, Knowing thy heart torment me with disdain,...'
  Teraz napisz sonet o pięknie księżyca."
- Odpowiedź: "Upon the sky, the moon doth softly gleam, In silv'ry light that casts its gentle grace,..."

Przykłady dostarczają LLM kontekstu, formatu lub stylu pożądanego wyniku. Pomagają modelowi zrozumieć konkretne zadanie i generować dokładniejsze i bardziej odpowiednie odpowiedzi.

### Chain-of-thought (łańcuch myślowy)

Chain-of-thought to bardzo interesująca technika, ponieważ polega na przeprowadzeniu LLM przez serię kroków. Idea polega na instruowaniu LLM w taki sposób, aby zrozumiał, jak coś zrobić. Rozważmy następujący przykład, z i bez chain-of-thought:

    - Prompt: "Alicja ma 5 jabłek, wyrzuca 3 jabłka, daje 2 Bobowi, a Bob oddaje jej jedno, ile jabłek ma Alicja?"
    - Odpowiedź: 5

LLM odpowiada 5, co jest niepoprawne. Prawidłowa odpowiedź to 1 jabłko, biorąc pod uwagę obliczenie (5 -3 -2 + 1 = 1).

Jak więc możemy nauczyć LLM, aby robił to poprawnie?

Spróbujmy chain-of-thought. Zastosowanie chain-of-thought oznacza:

1. Daj LLM podobny przykład.
1. Pokaż obliczenie i jak obliczyć to poprawnie.
1. Podaj oryginalny prompt.

Oto jak:

- Prompt: "Lisa ma 7 jabłek, wyrzuca 1 jabłko, daje 4 jabłka Bartowi, a Bart oddaje jej jedno:
  7 -1 = 6
  6 -4 = 2
  2 +1 = 3
  Alicja ma 5 jabłek, wyrzuca 3 jabłka, daje 2 Bobowi, a Bob oddaje jej jedno, ile jabłek ma Alicja?"
  Odpowiedź: 1

Zauważ, jak piszemy znacznie dłuższe prompty z innym przykładem, obliczeniem, a następnie oryginalnym promptem i dochodzimy do poprawnej odpowiedzi 1.

Jak widać, chain-of-thought to bardzo potężna technika.

### Generated knowledge (wygenerowana wiedza)

Często, gdy chcesz skonstruować prompt, chcesz to zrobić, używając własnych danych firmy. Chcesz, aby część promptu pochodziła z firmy, a druga część powinna być faktycznym promptem, którym jesteś zainteresowany.

Na przykład, tak może wyglądać Twój prompt, jeśli działasz w branży ubezpieczeniowej:

```text
{{company}}: {{company_name}}
{{products}}:
{{products_list}}
Proszę zaproponować ubezpieczenie przy następującym budżecie i wymaganiach:
Budżet: {{budget}}
Wymagania: {{requirements}}
```

Powyżej widać, jak prompt jest skonstruowany przy użyciu szablonu. W szablonie znajduje się szereg zmiennych, oznaczonych przez `{{zmienna}}`, które zostaną zastąpione rzeczywistymi wartościami z API firmy.

Oto przykład, jak może wyglądać prompt po zastąpieniu zmiennych treścią z Twojej firmy:

```text
Firma ubezpieczeniowa: ACME Insurance
Produkty ubezpieczeniowe (koszt miesięczny):
- Samochód, tani, 500 USD
- Samochód, drogi, 1100 USD
- Dom, tani, 600 USD
- Dom, drogi, 1200 USD
- Życie, tanie, 100 USD

Proszę zaproponować ubezpieczenie przy następującym budżecie i wymaganiach:
Budżet: $1000
Wymagania: Ubezpieczenie samochodu, domu i życia
```

Uruchomienie tego promptu przez LLM spowoduje wygenerowanie odpowiedzi takiej jak ta:

```output
Biorąc pod uwagę budżet i wymagania, proponujemy następujący pakiet ubezpieczeniowy od ACME Insurance:
- Samochód, tani, 500 USD
- Dom, tani, 600 USD
- Życie, tanie, 100 USD
Całkowity koszt: $1,200 USD
```

Jak widać, sugeruje również ubezpieczenie na życie, czego nie powinien robić. Ten wynik jest wskazówką, że musimy zoptymalizować prompt, zmieniając go, aby był jaśniejszy w tym, na co może pozwolić. Po kilku _próbach i błędach_, dochodzimy do następującego promptu:

```text
Firma ubezpieczeniowa: ACME Insurance
Produkty ubezpieczeniowe (koszt miesięczny):
- typ: Samochód, tani, koszt: 500 USD
- typ: Samochód, drogi, koszt: 1100 USD
- typ: Dom, tani, koszt: 600 USD
- typ: Dom, drogi, koszt: 1200 USD
- typ: Życie, tanie, koszt: 100 USD

Proszę zaproponować ubezpieczenie przy następującym budżecie i wymaganiach:
Budżet: $1000 ogranicz wybór do typów: Samochód, Dom
```

Zauważ, jak dodanie _typ_ i _koszt_, a także użycie słowa kluczowego _ogranicz_ pomaga LLM zrozumieć, czego chcemy.

Teraz otrzymujemy następującą odpowiedź:

```output
Biorąc pod uwagę budżet i wymagania, proponujemy ubezpieczenie Samochód, Tanie, które kosztuje 500 USD miesięcznie.
```

Celem tego przykładu było pokazanie, że nawet przy użyciu podstawowej techniki, takiej jak _wygenerowana wiedza_, nadal musimy w większości przypadków optymalizować prompt, aby uzyskać pożądany wynik.

### Least-to-most (od najmniejszego do największego)

Idea promptowania Least-to-most polega na rozbiciu większego problemu na podproblemy. W ten sposób pomagasz kierować LLM, jak "pokonać" większy problem. Dobrym przykładem mogłaby być analiza danych, gdzie możesz poprosić LLM o podzielenie problemu w następujący sposób:

> Prompt: Jak wykonać analizę danych w 5 krokach?

Twój asystent AI odpowie:

1. Zbierz dane
1. Oczyść dane
1. Przeanalizuj dane
1. Wizualizuj dane
1. Zaprezentuj dane

### Self-refine (samodoskonalenie), krytyka wyników

W przypadku generatywnych AI i LLM nie możesz ufać wynikom. Musisz je weryfikować. Ostatecznie, LLM po prostu przedstawia Ci to, co jest najbardziej prawdopodobne do powiedzenia, a nie to, co jest poprawne. Dlatego dobrym pomysłem jest poproszenie LLM o skrytykowanie samego siebie, co prowadzi nas do techniki self-refine.

Działa to w następujący sposób:

1. Początkowy prompt proszący LLM o rozwiązanie problemu
1. LLM odpowiada
1. Krytykujesz odpowiedź i prosisz AI o ulepszenie
1. LLM odpowiada ponownie, tym razem uwzględniając krytykę i sugerując rozwiązania, które wymyślił

Możesz powtarzać ten proces tyle razy, ile chcesz.

Oto przykład wykorzystujący tę technikę:

> Prompt: "Stwórz API webowe w Pythonie z trasami products i customers"

Odpowiedź AI:

```python
import flask
app = Flask(__name__)

@app.route('/products')
def products():
    return 'Products'

@app.route('/customers')
def customers():
    return 'Customers'
```

> Prompt: zaproponuj 3 ulepszenia powyższego kodu

Odpowiedź AI:

```text
Oczywiście, oto trzy sugestie ulepszeń kodu:

Zaimportuj prawidłowy moduł: Pierwsza linia powinna importować Flask zamiast flask. Prawidłowa instrukcja importu powinna brzmieć from flask import Flask.

Dodaj funkcję main: Dodaj blok if __name__ == '__main__': na końcu pliku, aby uruchomić aplikację po wykonaniu pliku.

Użyj f-strings: Użyj f-strings do formatowania instrukcji return w funkcjach tras. Na przykład, return 'Products' można zmienić na return f'To jest strona {request.path}'.
```

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/products')
def products():
    return f'To jest strona {request.path}'

@app.route('/customers')
def customers():
    return f'To jest strona {request.path}'

if __name__ == '__main__':
    app.run()
```

Jak widać, powyższa odpowiedź AI ulepsza pierwszy sugerowany kod dzięki krytyce pierwszej odpowiedzi.

### Maieutic prompting (promptowanie majeutyczne)

Promptowanie majeutyczne to technika podobna do self-refine, ale bardziej skupia się na prośbie o wyjaśnienie przez LLM. Celem jest zmniejszenie niespójności w wynikach LLM, aby upewnić się, że dochodzi do poprawnej odpowiedzi. Proces do naśladowania to:

1. Poproś LLM o odpowiedź na pytanie
1. Dla każdej części odpowiedzi poproś LLM o bardziej szczegółowe wyjaśnienie.
1. Jeśli istnieją niespójności, odrzuć części, które są niespójne.

Powtarzaj kroki 2 i 3, aż przejdziesz przez wszystkie części i będziesz zadowolony z odpowiedzi.

Oto przykładowy prompt:

> prompt: Jak mogę stworzyć plan kryzysowy, aby złagodzić skutki pandemii w 5 krokach?
> Odpowiedź LLM:

```text
1. Zidentyfikuj ryzyka
1. Zidentyfikuj interesariuszy
1. Zidentyfikuj zasoby
1. Zidentyfikuj działania
1. Zidentyfikuj kanały komunikacji
```

Zidentyfikowano 5 kroków, ale czy możemy ustalić, czy jest to poprawne? Poprośmy LLM o wyjaśnienie każdego kroku:

> prompt: Wyjaśnij pierwszy krok bardziej szczegółowo, jakie są ryzyka szczegółowo związane z pandemią?

```text
Ryzyka są następujące:

- Utrata życia
- Utrata biznesu
- Utrata reputacji
- Utrata klientów
- Utrata pracowników
```

Na tym etapie chcemy upewnić się, że LLM jest poprawny, więc prosimy go o bardziej szczegółowe wyjaśnienie pierwszego ryzyka i mamy nadzieję, że jest zgodne z powyższą odpowiedzią:

> prompt: W pandemii, które ryzyko jest największe i dlaczego?

```text
Największym ryzykiem jest utrata życia, ponieważ jest to najważniejsza rzecz do ochrony.
```

> Jakie są dwa największe ryzyka w pandemii?

```text
Dwa największe ryzyka to utrata życia i utrata biznesu.
```

Na tym etapie LLM jest spójny i wymienia "życie" i "biznes" jako dwa największe ryzyka. Możemy teraz przejść do następnego kroku i czuć się dość pewnie. Jednak nie powinniśmy ślepo ufać LLM, zawsze powinniśmy weryfikować wyniki.

## Różnicowanie wyników

LLM są z natury niedeterministyczne, co oznacza, że za każdym razem, gdy uruchamiasz ten sam prompt, otrzymasz różne wyniki. Wypróbuj na przykład następujący prompt:

> "Wygeneruj kod dla API webowego w Pythonie"

```python
# Importuj niezbędne moduły
import flask
from flask import request, jsonify

# Utwórz aplikację Flask
app = flask.Flask(__name__)

# Utwórz trasę dla API
@app.route('/api', methods=['GET'])
def api():
    # Pobierz dane z żądania
    data = request.args

    # Przetwórz dane
    result = process_data(data)

    # Zwróć wynik jako JSON
    return jsonify(result)

# Funkcja do przetwarzania danych
def process_data(data):
    # Zrób coś z danymi
    result = data + 1

    # Zwróć wynik
    return result

# Uruchom aplikację
if __name__ == '__main__':
    app.run()

```

Uruchomienie tego samego promptu ponownie generuje nieco inną odpowiedź:

```python
#importuj niezbędne pakiety
import flask
from flask import request, jsonify

#utwórz aplikację Flask
app = flask.Flask(__name__)
app.config["DEBUG"] = True

#utwórz listę książek
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

#utwórz endpoint dla API
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Books API</h1>
<p>A prototype API for retrieving books.</p>'''

#utwórz endpoint, aby zwrócić wszystkie książki
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

#utwórz endpoint, aby zwrócić pojedynczą książkę
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    #sprawdź, czy ID zostało podane jako część URL
    #jeśli ID jest podane, przypisz je do zmiennej
    #jeśli nie podano ID, wyświetl błąd
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    #utwórz pustą listę dla naszych wyników
    results = []

    #przejdź przez dane i dopasuj wyniki, które pasują do żądanego ID
    #ID są unikalne, ale inne pola mogą zwrócić wiele wyników
    for book in books:
        if book['id'] == id:
            results.append(book)

    #użyj funkcji jsonify z Flask, aby przekonwertować naszą listę
    #słowników Pythona na format JSON
    return jsonify(results)

app.run()
```

> Czy zróżnicowane wyniki to problem?

Zależy od tego, co próbujesz zrobić. Jeśli chcesz konkretnej odpowiedzi, to jest to problem. Jeśli nie masz nic przeciwko zróżnicowanym wynikom, takim jak "Wygeneruj dowolne 3 pytania dotyczące geografii", to nie jest to problem.

### Używanie temperatury do różnicowania wyników

Ok, więc zdecydowaliśmy, że chcemy ograniczyć wyniki, aby były bardziej przewidywalne, czyli bardziej deterministyczne. Jak to zrobić?

Temperatura to wartość między 0 a 1, gdzie 0 jest najbardziej deterministyczna, a 1 najbardziej zróżnicowana. Domyślna wartość to 0,7. Zobaczmy, co się stanie przy dwóch uruchomieniach tego samego promptu z temperaturą ustawioną na 0,1:

> "Wygeneruj kod dla API webowego w Pythonie"

```python
#importuj niezbędne biblioteki
import flask
from flask import request, jsonify

#utwórz instancję klasy Flask
app = flask.Flask(__name__)

#utwórz endpoint dla API
@app.route('/api/v1/endpoint', methods=['GET'])
def api_endpoint():
    #pobierz dane żądania
    data = request.get_json()

    #przetwórz dane
    result = process_data(data)

    #zwróć wynik
    return jsonify(result)

#funkcja do przetwarzania danych
def process_data(data):
    #przetwórz dane
    result = {'result': 'success'}

    #zwróć wynik
    return result

#uruchom aplikację Flask
if __name__ == '__main__':
    app.run()

```

Uruchomienie promptu ponownie daje nam taki wynik:

```python
#importuj niezbędne biblioteki
import flask
from flask import request, jsonify

#utwórz aplikację Flask
app = flask.Flask(__name__)

#utwórz trasę dla API
@app.route('/api', methods=['GET'])
def api_call():
    #pobierz dane z żądania
    data = request.get_json()

    #przetwórz dane
    result = process_data(data)

    #zwróć wynik
    return jsonify(result)

#zdefiniuj funkcję process_data
def process_data(data):
    #zrób coś z danymi
    result = data + 1

    #zwróć wynik
    return result

#uruchom aplikację
if __name__ == '__main__':
    app.run()

```

Między tymi dwoma wynikami jest tylko niewielka różnica. Zróbmy teraz odwrotnie, ustawmy temperaturę na 0,9:

```python
# Importuj niezbędne biblioteki
import flask
from flask import request, jsonify

# Utwórz aplikację Flask
app = flask.Flask(__name__)

# Utwórz trasę dla API
@app.route('/api', methods=['GET'])
def api_call():
    # Pobierz dane z żądania
    data = request.args

    # Przetwórz dane
    result = process_data(data)

    # Zwróć wynik
    return jsonify(result)

# Funkcja do przetwarzania danych
def process_data(data):
    # Zrób coś z danymi
    result = data + 1

    # Zwróć wynik
    return result

# Uruchom aplikację
if __name__ == '__main__':
    app.run()

```

a druga próba przy wartości temperatury 0,9:

```python
import flask
from flask import request, jsonify

# utwórz aplikację Flask
app = flask.Flask(__name__)
app.config['DEBUG'] = True

# utwórz przykładowe dane
books = [
    {'id': 0, 'title': 'A Fire Upon The Deep', 'author': 'Vernor Vinge', 'first_sentence': 'The coldsleep itself was dreamless.', 'year_published': '1992'},
    {'id': 1, 'title': 'The Ones Who Walk Away From Omelas', 'author': 'Ursula K. Le Guin', 'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.', 'published': '1973'},
    {'id': 2, 'title': 'Dhalgren', 'author': 'Samuel R. Delany', 'first_sentence': 'to wound the autumnal city.', 'published': '1975'}
]

# utwórz endpoint
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to our book API!</h1>'''

@app.route('/api/v1/resources/books

```

Jak widać, wyniki nie mogłyby być bardziej zróżnicowane.

> Uwaga, istnieje więcej parametrów, które można zmienić, aby zróżnicować wyniki, takie jak top-k, top-p, kara za powtórzenia, kara za długość i kara za różnorodność, ale są one poza zakresem tego programu nauczania.

## Dobre praktyki

Istnieje wiele praktyk, które możesz zastosować, aby uzyskać to, czego chcesz. Znajdziesz swój własny styl w miarę korzystania z promptowania coraz częściej.

Oprócz technik, które omówiliśmy, istnieje kilka dobrych praktyk, które warto wziąć pod uwagę podczas promptowania LLM.

Oto kilka dobrych praktyk do rozważenia:

- **Określ kontekst**. Kontekst ma znaczenie, im więcej możesz określić, takich jak domena, temat itp., tym lepiej.
- **Ogranicz wyniki**. Jeśli chcesz określonej liczby elementów lub określonej długości, określ to.
- **Określ zarówno co, jak i jak**. Pamiętaj, aby wspomnieć zarówno o tym, czego chcesz, jak i jak to chcesz, na przykład "Stwórz API webowe w Pythonie z trasami products i customers, podziel je na 3 pliki".
- **Używaj szablonów**. Często będziesz chciał wzbogacić swoje prompty o dane z Twojej firmy. Użyj szablonów, aby to zrobić. Szablony mogą mieć zmienne, które zastępujesz rzeczywistymi danymi.
- **Pisz poprawnie**. LLM mogą dostarczyć Ci poprawną odpowiedź, ale jeśli piszesz poprawnie, uzyskasz lepszą odpowiedź.

## Zadanie

Oto kod w Pythonie pokazujący, jak zbudować proste API przy użyciu Flask:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()
```

Użyj asystenta AI, takiego jak GitHub Copilot lub ChatGPT, i zastosuj technikę "self-refine", aby ulepszyć kod.

## Rozwiązanie

Proszę spróbuj rozwiązać zadanie, dodając odpowiednie prompty do kodu.

> [!TIP]
> Sformułuj prompt prosząc o ulepszenie, dobrym pomysłem jest ograniczenie liczby ulepszeń. Możesz również poprosić o ulepszenie w określony sposób, na przykład architekturę, wydajność, bezpieczeństwo itp.

[Rozwiązanie](../../python/aoai-solution.py?WT.mc_id=academic-105485-koreyst)

## Sprawdzenie wiedzy

Dlaczego miałbym użyć promptowania chain-of-thought? Pokaż mi 1 poprawną odpowiedź i 2 niepoprawne odpowiedzi.

1. Aby nauczyć LLM, jak rozwiązać problem.
1. B, Aby nauczyć LLM znajdowania błędów w kodzie.
1. C, Aby poinstruować LLM, aby znalazł różne rozwiązania.

A: 1, ponieważ chain-of-thought polega na pokazaniu LLM, jak rozwiązać problem, dostarczając mu serię kroków oraz podobnych problemów i sposobów ich rozwiązania.

## 🚀 Wyzwanie

Właśnie użyłeś techniki self-refine w zadaniu. Weź dowolny program, który zbudowałeś, i zastanów się, jakie ulepszenia chciałbyś w nim wprowadzić. Teraz użyj techniki self-refine, aby zastosować proponowane zmiany. Co sądzisz o wyniku, lepszy czy gorszy?

## Świetna Praca! Kontynuuj Naukę

Po ukończeniu tej lekcji sprawdź naszą [kolekcję materiałów dydaktycznych dotyczących Generatywnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby kontynuować podnoszenie swojej wiedzy o Generatywnej AI!

Przejdź do Lekcji 6, aby zobaczyć, jak możesz zacząć [budować aplikacje generujące tekst](../../../06-text-generation-apps/translations/pl/README.md?WT.mc_id=academic-105485-koreyst)!
