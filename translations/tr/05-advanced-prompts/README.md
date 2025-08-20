<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:32:11+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "tr"
}
-->

> "Python Web API için kod oluştur"
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

İstemi tekrar çalıştırmak bize şu sonucu veriyor:

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

Bu iki çıktı arasında sadece küçük bir fark var. Bu sefer tam tersini yapalım, sıcaklık değerini 0.9 olarak ayarlayalım:

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

ve sıcaklık değeri 0.9 olan ikinci deneme:

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

Gördüğünüz gibi, sonuçlar oldukça farklı.

> [!NOTE] Çıktıyı çeşitlendirmek için değiştirebileceğiniz top-k, top-p, tekrar cezası, uzunluk cezası ve çeşitlilik cezası gibi başka parametreler de vardır ancak bunlar bu müfredatın kapsamı dışındadır.

## İyi uygulamalar

İstediğinizi elde etmek için uygulayabileceğiniz birçok yöntem var. İstem kullanımı arttıkça kendi tarzınızı geliştireceksiniz.

Ele aldığımız tekniklere ek olarak, bir LLM’ye istem verirken göz önünde bulundurmanız gereken bazı iyi uygulamalar vardır.

Dikkate almanız gereken bazı iyi uygulamalar şunlardır:

- **Bağlamı belirtin**. Bağlam önemlidir, alan, konu gibi ne kadar çok belirtebilirseniz o kadar iyi olur.
- Çıktıyı sınırlandırın. Belirli sayıda öğe veya belirli bir uzunluk istiyorsanız bunu belirtin.
- **Hem ne istediğinizi hem nasıl istediğinizi belirtin**. Ne istediğinizi ve nasıl istediğinizi belirtmeyi unutmayın, örneğin “products ve customers rotalarına sahip bir Python Web API oluştur, 3 dosyaya böl”.
- **Şablonlar kullanın**. Genellikle istemlerinizi şirketinizden gelen verilerle zenginleştirmek istersiniz. Bunu yapmak için şablonlar kullanın. Şablonlarda gerçek verilerle değiştireceğiniz değişkenler olabilir.
- **Doğru yazım kullanın**. LLM’ler doğru yanıt verebilir ancak doğru yazarsanız daha iyi yanıt alırsınız.

## Ödev

Flask kullanarak basit bir API oluşturmayı gösteren Python kodu burada:

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

GitHub Copilot veya ChatGPT gibi bir yapay zeka asistanı kullanarak "self-refine" (kendini geliştirme) tekniğini uygulayın ve kodu iyileştirin.

## Çözüm

Lütfen uygun istemler ekleyerek ödevi çözmeyi deneyin.

> [!TIP]
> İyileştirme yapmasını istemek için bir istem oluşturun, kaç tane iyileştirme yapılacağını sınırlamak iyi bir fikirdir. Ayrıca mimari, performans, güvenlik gibi belirli bir şekilde iyileştirmesini de isteyebilirsiniz.

[Çözüm](../../../05-advanced-prompts/python/aoai-solution.py)

## Bilgi kontrolü

Neden chain-of-thought (düşünce zinciri) istemi kullanırım? Bana 1 doğru cevap ve 2 yanlış cevap göster.

1. LLM’ye bir problemi nasıl çözeceğini öğretmek için.
1. B, LLM’ye koddaki hataları bulmayı öğretmek için.
1. C, LLM’ye farklı çözümler üretmesini öğretmek için.

A: 1, çünkü düşünce zinciri, LLM’ye bir problemi çözmeyi, adım adım ve benzer problemlerle nasıl çözüldüğünü göstererek öğretmektir.

## 🚀 Meydan Okuma

Ödevde self-refine tekniğini kullandınız. Yaptığınız herhangi bir programı alın ve ona uygulamak istediğiniz geliştirmeleri düşünün. Şimdi self-refine tekniğini kullanarak önerilen değişiklikleri uygulayın. Sonuç hakkında ne düşündünüz, daha iyi mi yoksa daha kötü mü oldu?

## Harika İş! Öğrenmeye Devam Et

Bu dersi tamamladıktan sonra, Generative AI bilginizi geliştirmeye devam etmek için [Generative AI Learning koleksiyonumuza](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) göz atın!

Prompt Engineering bilgimizi uygulayacağımız ve [metin üretim uygulamaları oluşturacağımız](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst) 6. derse geçin.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.