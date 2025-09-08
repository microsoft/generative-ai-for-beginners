<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:31:44+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "pl"
}
-->

> "Generuj kod dla Python Web API"
```python
#import necessary libraries
import flask
from flask import request, jsonify

#create an instance of the Flask class
app = flask.Flask(__name__)

#create an endpoint for the API
@app.route('/api/v1/endpoint', methods=['GET'])
def api_endpoint():
    #get the request data
    data = request.get_json()

    #process the data
    result = process_data(data)

    #return the result
    return jsonify(result)

#function to process the data
def process_data(data):
    #process the data
    result = {'result': 'success'}

    #return the result
    return result

#run the Flask app
if __name__ == '__main__':
    app.run()

```

Ponowne uruchomienie promptu daje nam taki wynik:

```python
#import necessary libraries
import flask
from flask import request, jsonify

#create a Flask app
app = flask.Flask(__name__)

#create a route for the API
@app.route('/api', methods=['GET'])
def api_call():
    #get the data from the request
    data = request.get_json()

    #process the data
    result = process_data(data)

    #return the result
    return jsonify(result)

#define the process_data function
def process_data(data):
    #do something with the data
    result = data + 1

    #return the result
    return result

#run the app
if __name__ == '__main__':
    app.run()

```

Różnica między tymi dwoma wynikami jest minimalna. Tym razem zróbmy odwrotnie i ustawmy temperaturę na 0.9:

```python
# Import necessary libraries
import flask
from flask import request, jsonify

# Create a Flask app
app = flask.Flask(__name__)

# Create a route for the API
@app.route('/api', methods=['GET'])
def api_call():
    # Get the data from the request
    data = request.args

    # Process the data
    result = process_data(data)

    # Return the result
    return jsonify(result)

# Function to process the data
def process_data(data):
    # Do something with the data
    result = data + 1

    # Return the result
    return result

# Run the app
if __name__ == '__main__':
    app.run()

```

a to druga próba z temperaturą ustawioną na 0.9:

```python
import flask
from flask import request, jsonify

# create the Flask app
app = flask.Flask(__name__)
app.config['DEBUG'] = True

# create some test data
books = [
    {'id': 0, 'title': 'A Fire Upon The Deep', 'author': 'Vernor Vinge', 'first_sentence': 'The coldsleep itself was dreamless.', 'year_published': '1992'},
    {'id': 1, 'title': 'The Ones Who Walk Away From Omelas', 'author': 'Ursula K. Le Guin', 'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.', 'published': '1973'},
    {'id': 2, 'title': 'Dhalgren', 'author': 'Samuel R. Delany', 'first_sentence': 'to wound the autumnal city.', 'published': '1975'}
]

# create an endpoint
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to our book API!</h1>'''

@app.route('/api/v1/resources/books

```

Jak widać, rezultaty są znacznie bardziej zróżnicowane.

> Pamiętaj, że istnieje więcej parametrów, które możesz zmieniać, aby uzyskać różnorodne wyniki, takich jak top-k, top-p, repetition penalty, length penalty czy diversity penalty, ale te tematy wykraczają poza zakres tego kursu.

## Dobre praktyki

Istnieje wiele praktyk, które możesz stosować, aby uzyskać oczekiwany efekt. Z czasem, korzystając z promptów, wypracujesz swój własny styl.

Oprócz technik, które omówiliśmy, warto pamiętać o kilku dobrych praktykach podczas tworzenia promptów dla LLM.

Oto kilka z nich:

- **Określ kontekst**. Kontekst ma znaczenie – im więcej szczegółów podasz, takich jak dziedzina, temat itp., tym lepiej.
- Ogranicz wynik. Jeśli chcesz określoną liczbę elementów lub konkretną długość, zaznacz to.
- **Określ zarówno co, jak i jak**. Pamiętaj, aby wskazać zarówno co chcesz, jak i w jaki sposób, np. „Stwórz Python Web API z trasami products i customers, podziel je na 3 pliki”.
- **Używaj szablonów**. Często będziesz chciał wzbogacić swoje prompta o dane z firmy. Wykorzystaj do tego szablony, które mogą zawierać zmienne zastępowane rzeczywistymi danymi.
- **Poprawna pisownia**. LLM może udzielić poprawnej odpowiedzi, ale jeśli poprawnie napiszesz prompt, otrzymasz lepszy rezultat.

## Zadanie

Oto kod w Pythonie pokazujący, jak zbudować prostą API za pomocą Flask:

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

Skorzystaj z asystenta AI, takiego jak GitHub Copilot lub ChatGPT, i zastosuj technikę „self-refine”, aby ulepszyć ten kod.

## Rozwiązanie

Spróbuj rozwiązać zadanie, dodając odpowiednie prompta do kodu.

> [!TIP]
> Sformułuj prompt z prośbą o ulepszenie, dobrze jest ograniczyć liczbę proponowanych zmian. Możesz też poprosić o poprawę w konkretnym obszarze, np. architektura, wydajność, bezpieczeństwo itp.

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## Sprawdzenie wiedzy

Dlaczego warto stosować chain-of-thought prompting? Pokaż 1 poprawną odpowiedź i 2 błędne.

1. Aby nauczyć LLM, jak rozwiązywać problem.
1. B, Aby nauczyć LLM znajdowania błędów w kodzie.
1. C, Aby nakazać LLM wymyślanie różnych rozwiązań.

Odpowiedź: 1, ponieważ chain-of-thought polega na pokazaniu LLM, jak rozwiązać problem, dostarczając mu serii kroków oraz podobnych problemów i sposobów ich rozwiązania.

## 🚀 Wyzwanie

Właśnie użyłeś techniki self-refine w zadaniu. Weź dowolny program, który stworzyłeś, i zastanów się, jakie ulepszenia chciałbyś wprowadzić. Następnie zastosuj technikę self-refine, aby wprowadzić proponowane zmiany. Jak oceniasz efekt – lepszy czy gorszy?

## Świetna robota! Kontynuuj naukę

Po ukończeniu tej lekcji sprawdź naszą [kolekcję Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby dalej rozwijać swoją wiedzę o Generative AI!

Przejdź do Lekcji 6, gdzie zastosujemy naszą wiedzę o Prompt Engineering, [tworząc aplikacje do generowania tekstu](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.