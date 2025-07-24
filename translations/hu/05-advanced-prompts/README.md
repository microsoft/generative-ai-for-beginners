<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:38:17+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "hu"
}
-->

# Kód generálása Python Web API-hoz

Ebben az útmutatóban megmutatjuk, hogyan készíthetsz egyszerű Python Web API-t a Flask keretrendszer segítségével.

## Előkészületek

Először is, győződj meg róla, hogy telepítve van a Flask:

```bash
pip install Flask
```

## Alap API létrehozása

Hozz létre egy `app.py` fájlt, és írd be a következő kódot:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Egyszerű üdvözlő végpont
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, világ!")

if __name__ == '__main__':
    app.run(debug=True)
```

## Az API futtatása

Futtasd az alkalmazást a következő paranccsal:

```bash
python app.py
```

Most már elérhető az API a `http://127.0.0.1:5000/hello` címen.

## További lépések

- Adj hozzá POST végpontokat az adatok fogadásához
- Használj adatbázist az adatok tárolásához
- Implementálj hitelesítést és jogosultságkezelést

[!TIP] Használhatsz más keretrendszereket is, például FastAPI-t, ha modernebb megoldást szeretnél.
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

Ha újra lefuttatjuk a promptot, ezt az eredményt kapjuk:

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

Csak egy apró különbség van a két kimenet között. Most csináljuk meg fordítva, állítsuk a hőmérsékletet 0,9-re:

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

és a második próbálkozás 0,9-es hőmérséklet értékkel:

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

Ahogy látható, az eredmények nagyon eltérőek lehetnek.

> Megjegyzés, hogy még több paramétert is módosíthatsz a kimenet változatosságának növelésére, például top-k, top-p, ismétlési büntetés, hosszúság büntetés és diverzitás büntetés, de ezek nem tartoznak ennek a tananyagnak a témakörébe.

## Jó gyakorlatok

Számos módszer létezik, amivel megpróbálhatod elérni, amit szeretnél. Ahogy egyre többet használod a promptokat, kialakul majd a saját stílusod.

A korábban bemutatott technikák mellett érdemes figyelembe venni néhány jó gyakorlatot is, amikor egy LLM-et kérdezel.

Íme néhány jó gyakorlat, amit érdemes szem előtt tartani:

- **Határozd meg a kontextust**. A kontextus számít, minél pontosabban meg tudod adni például a domaint, témát, annál jobb.
- Korlátozd a kimenetet. Ha egy adott számú elemet vagy hosszúságot szeretnél, jelezd ezt.
- **Add meg, hogy mit és hogyan**. Ne felejtsd el megemlíteni, hogy mit szeretnél és hogyan, például: „Készíts egy Python Web API-t products és customers útvonalakkal, oszd 3 fájlra”.
- **Használj sablonokat**. Gyakran szeretnéd a promptjaidat a céged adataival gazdagítani. Ehhez használj sablonokat, amelyek változókat tartalmaznak, amiket tényleges adatokra cserélsz.
- **Helyesen írj**. Az LLM-ek helyes választ adhatnak, de ha helyesen írsz, jobb válaszokat kapsz.

## Feladat

Íme egy Python kód, ami megmutatja, hogyan építsünk egyszerű API-t Flask segítségével:

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

Használj AI asszisztenst, például GitHub Copilotot vagy ChatGPT-t, és alkalmazd a „self-refine” technikát a kód javítására.

## Megoldás

Próbáld megoldani a feladatot úgy, hogy megfelelő promptokat adsz a kódhoz.

> [!TIP]
> Fogalmazz meg egy promptot, amiben kéred a javítást, érdemes korlátozni, hogy hány javítást kérsz. Kérheted azt is, hogy egy adott szempont szerint javítson, például architektúra, teljesítmény, biztonság stb.

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## Tudásellenőrzés

Miért használnám a chain-of-thought promptolást? Mutass 1 helyes és 2 helytelen választ.

1. Hogy megtanítsuk az LLM-nek, hogyan oldjon meg egy problémát.
1. B, Hogy megtanítsuk az LLM-nek, hogyan találjon hibákat a kódban.
1. C, Hogy utasítsuk az LLM-et, hogy különböző megoldásokat találjon ki.

A: 1, mert a chain-of-thought arról szól, hogy megmutatjuk az LLM-nek, hogyan oldjon meg egy problémát lépésről lépésre, hasonló problémákat és azok megoldását bemutatva.

## 🚀 Kihívás

Most épp a self-refine technikát használtad a feladatban. Vegyél elő bármilyen programot, amit készítettél, és gondold át, milyen fejlesztéseket szeretnél rajta végrehajtani. Ezután használd a self-refine technikát a javasolt változtatások alkalmazására. Mit gondolsz, jobb vagy rosszabb lett az eredmény?

## Szép munka! Folytasd a tanulást

A lecke elvégzése után nézd meg a [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) gyűjteményünket, hogy tovább fejleszd a Generatív AI ismereteidet!

Lépj tovább a 6. leckébe, ahol a Prompt Engineering tudásunkat alkalmazva [szöveg generáló alkalmazásokat építünk](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.