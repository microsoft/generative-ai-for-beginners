<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ffb706de93ef518f31e0a675c66dfce1",
  "translation_date": "2025-10-17T16:14:37+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "tr"
}
-->
# Gelişmiş İstekler Oluşturma

[![Gelişmiş İstekler Oluşturma](../../../translated_images/05-lesson-banner.522610fd4a2cd82dbed66bb7e6fe104ed6da172e085dbb4d9100b28dc73ed435.tr.png)](https://youtu.be/BAjzkaCdRok?si=NmUIyRf7-cDgbjtt)

Önceki bölümden bazı öğrenimleri tekrar gözden geçirelim:

> İstek _mühendisliği_, modele daha faydalı talimatlar veya bağlam sağlayarak **daha alakalı yanıtlar vermesini sağlama sürecidir**.

İstek yazmanın iki adımı vardır: bağlam sağlayarak isteği oluşturmak ve ikinci adım olan _optimizasyon_, yani isteği kademeli olarak iyileştirme.

Bu noktada, istek yazma konusunda temel bir anlayışa sahibiz, ancak daha derine inmemiz gerekiyor. Bu bölümde, farklı istekleri denemekten bir isteğin neden diğerinden daha iyi olduğunu anlamaya geçeceksiniz. Herhangi bir LLM için uygulanabilecek bazı temel teknikleri takip ederek istekler oluşturmayı öğreneceksiniz.

## Giriş

Bu bölümde aşağıdaki konuları ele alacağız:

- İstek mühendisliği bilginizi, isteklerinize farklı teknikler uygulayarak genişletmek.
- Çıktıyı değiştirmek için isteklerinizi yapılandırmak.

## Öğrenme hedefleri

Bu dersi tamamladıktan sonra şunları yapabileceksiniz:

- İsteklerinizin sonucunu iyileştiren istek mühendisliği tekniklerini uygulamak.
- Çeşitli veya deterministik istekler gerçekleştirmek.

## İstek mühendisliği

İstek mühendisliği, istenen sonucu üretecek istekler oluşturma sürecidir. İstek mühendisliği sadece bir metin isteği yazmaktan ibaret değildir. İstek mühendisliği bir mühendislik disiplini değil, istenen sonucu elde etmek için uygulanabilecek bir dizi tekniktir.

### Bir istek örneği

Basit bir istek örneği alalım:

> Coğrafya hakkında 10 soru oluştur.

Bu istekte aslında farklı istek tekniklerinin bir setini uyguluyorsunuz.

Bunu parçalayalım.

- **Bağlam**, "coğrafya" hakkında olması gerektiğini belirtiyorsunuz.
- **Çıktıyı sınırlama**, en fazla 10 soru istiyorsunuz.

### Basit isteklerin sınırlamaları

İstediğiniz sonucu elde edebilirsiniz veya edemeyebilirsiniz. Sorularınız oluşturulacaktır, ancak coğrafya geniş bir konu olduğundan ve aşağıdaki nedenlerden dolayı istediğiniz şeyi elde edemeyebilirsiniz:

- **Geniş konu**, ülkeler, başkentler, nehirler vb. hakkında olup olmayacağını bilmiyorsunuz.
- **Format**, soruların belirli bir formatta olmasını istiyorsanız ne olacak?

Gördüğünüz gibi, istek oluştururken dikkate alınması gereken çok şey var.

Şimdiye kadar basit bir istek örneği gördük, ancak üretken yapay zeka, çeşitli roller ve endüstrilerde insanlara yardımcı olmak için çok daha fazlasını yapabilir. Şimdi bazı temel teknikleri keşfedelim.

### İstek teknikleri

Öncelikle, isteklerin bir LLM'nin _ortaya çıkan_ bir özelliği olduğunu anlamamız gerekiyor, yani bu modelde yerleşik bir özellik değil, model kullanıldıkça keşfedilen bir şeydir.

Bir LLM'yi yönlendirmek için kullanabileceğimiz bazı temel teknikler vardır. Bunları inceleyelim.

- **Sıfır atış isteği**, bu en temel istek türüdür. LLM'den yalnızca eğitim verilerine dayanarak bir yanıt talep eden tek bir istektir.
- **Az atış isteği**, bu tür istek, LLM'yi yanıtını oluştururken dayanabileceği bir veya daha fazla örnek sağlayarak yönlendirir.
- **Düşünce zinciri**, bu tür istek, LLM'ye bir problemi adım adım nasıl çözmesi gerektiğini söyler.
- **Üretilmiş bilgi**, bir isteğin yanıtını iyileştirmek için isteğinize ek olarak üretilmiş gerçekler veya bilgiler sağlayabilirsiniz.
- **Azdan çoğa**, düşünce zinciri gibi, bu teknik bir problemi bir dizi adıma bölmek ve ardından bu adımların sırayla gerçekleştirilmesini istemekle ilgilidir.
- **Kendi kendini iyileştirme**, bu teknik, LLM'nin çıktısını eleştirmek ve ardından iyileştirmesini istemekle ilgilidir.
- **Maieutik istek**, burada istediğiniz şey, LLM'nin yanıtının doğru olduğundan emin olmak ve yanıtın çeşitli bölümlerini açıklamasını istemektir. Bu, kendi kendini iyileştirme türüdür.

### Sıfır atış isteği

Bu istek tarzı çok basittir, tek bir isteği içerir. Bu teknik muhtemelen LLM'ler hakkında öğrenmeye başladığınızda kullandığınız tekniktir. İşte bir örnek:

- İstek: "Cebir nedir?"
- Yanıt: "Cebir, matematiksel sembolleri ve bu sembolleri manipüle etme kurallarını inceleyen matematiğin bir dalıdır."

### Az atış isteği

Bu istek tarzı, modelin isteğin yanında birkaç örnek sağlayarak yardımcı olur. Tek bir istek ve ek görev spesifik verilerden oluşur. İşte bir örnek:

- İstek: "Shakespeare tarzında bir şiir yaz. İşte Shakespeare'in birkaç sonesi:
  Sone 18: 'Seni bir yaz gününe benzetebilir miyim? Sen daha güzel ve daha ılımlısın...'
  Sone 116: 'Gerçek zihinlerin evliliğine engel koymayayım. Aşk, değişim bulduğunda değişen aşk değildir...'
  Sone 132: 'Gözlerini seviyorum ve onlar, bana acıyarak, Kalbini biliyor, beni hor görerek işkence ediyor,...'
  Şimdi, ayın güzelliği hakkında bir sone yaz."
- Yanıt: "Gökyüzünde ay yumuşakça parlıyor, Gümüş ışıkta zarifçe yayılan..."

Örnekler, LLM'ye istenen çıktının bağlamını, formatını veya tarzını sağlar. Modelin belirli görevi anlamasına ve daha doğru ve alakalı yanıtlar üretmesine yardımcı olur.

### Düşünce zinciri

Düşünce zinciri çok ilginç bir tekniktir çünkü LLM'yi bir dizi adımdan geçirme ile ilgilidir. Fikir, LLM'ye bir şeyi nasıl yapacağını anlayacak şekilde talimat vermektir. Düşünce zinciri olmadan ve düşünce zinciri ile bir örneği düşünün:

    - İstek: "Alice'in 5 elması var, 3 elmayı atıyor, 2 elmayı Bob'a veriyor ve Bob birini geri veriyor, Alice'in kaç elması var?"
    - Yanıt: 5

LLM 5 yanıtını verir, bu yanlış. Doğru yanıt 1 elmadır, hesaplama (5 -3 -2 + 1 = 1) göz önüne alındığında.

Peki LLM'ye bunu doğru yapmayı nasıl öğretebiliriz?

Düşünce zincirini deneyelim. Düşünce zincirini uygulamak şu anlama gelir:

1. LLM'ye benzer bir örnek verin.
1. Hesaplamayı gösterin ve doğru şekilde nasıl hesaplanacağını gösterin.
1. Orijinal isteği sağlayın.

İşte nasıl yapılacağı:

- İstek: "Lisa'nın 7 elması var, 1 elmayı atıyor, 4 elmayı Bart'a veriyor ve Bart birini geri veriyor:
  7 -1 = 6
  6 -4 = 2
  2 +1 = 3  
  Alice'in 5 elması var, 3 elmayı atıyor, 2 elmayı Bob'a veriyor ve Bob birini geri veriyor, Alice'in kaç elması var?"
  Yanıt: 1

Gördüğünüz gibi, düşünce zinciri çok güçlü bir tekniktir.

### Üretilmiş bilgi

Çoğu zaman bir istek oluşturmak istediğinizde, bunu kendi şirketinizin verilerini kullanarak yapmak istersiniz. İsteğin bir kısmının şirketten, diğer kısmının ise ilgilendiğiniz asıl isteğin olması gerekir.

Bir örnek olarak, sigorta sektöründe olduğunuzu varsayalım, isteğiniz şu şekilde görünebilir:

```text
{{company}}: {{company_name}}
{{products}}:
{{products_list}}
Please suggest an insurance given the following budget and requirements:
Budget: {{budget}}
Requirements: {{requirements}}
```

Yukarıda, isteğin bir şablon kullanılarak nasıl oluşturulduğunu görüyorsunuz. Şablonda `{{variable}}` ile belirtilen bir dizi değişken vardır ve bunlar bir şirket API'sinden gelen gerçek değerlerle değiştirilecektir.

Değişkenler şirketinizden gelen içerikle değiştirildikten sonra isteğin nasıl görünebileceğine bir örnek:

```text
Insurance company: ACME Insurance
Insurance products (cost per month):
- Car, cheap, 500 USD
- Car, expensive, 1100 USD
- Home, cheap, 600 USD
- Home, expensive, 1200 USD
- Life, cheap, 100 USD

Please suggest an insurance given the following budget and requirements:
Budget: $1000
Requirements: Car, Home, and Life insurance
```

Bu isteği bir LLM üzerinden çalıştırmak şu yanıtı üretecektir:

```output
Given the budget and requirements, we suggest the following insurance package from ACME Insurance:
- Car, cheap, 500 USD
- Home, cheap, 600 USD
- Life, cheap, 100 USD
Total cost: $1,200 USD
```

Gördüğünüz gibi, aynı zamanda Hayat sigortasını da öneriyor, ki bunu yapmamalı. Bu sonuç, isteği daha net hale getirmek için değiştirerek optimize etmemiz gerektiğinin bir göstergesidir. Biraz _deneme yanılma_ ile şu isteğe ulaşıyoruz:

```text
Insurance company: ACME Insurance
Insurance products (cost per month):
- type: Car, cheap, cost: 500 USD
- type: Car, expensive, cost: 1100 USD
- type: Home, cheap, cost: 600 USD
- type: Home, expensive, cost: 1200 USD
- type: Life, cheap, cost: 100 USD

Please suggest an insurance given the following budget and requirements:
Budget: $1000 restrict choice to types: Car, Home
```

Gördüğünüz gibi, _tür_ ve _maliyet_ eklemek ve ayrıca _kısıtlama_ anahtar kelimesini kullanmak, LLM'nin ne istediğimizi anlamasına yardımcı oluyor.

Şimdi şu yanıtı alıyoruz:

```output
Given the budget and requirements, we suggest the Car, Cheap insurance product which costs 500 USD per month.
```

Bu örneğin amacı, _üretilmiş bilgi_ gibi temel bir teknik kullansak bile, çoğu durumda istenen sonucu elde etmek için isteği optimize etmemiz gerektiğini göstermektir.

### Azdan çoğa

Azdan çoğa isteme fikri, daha büyük bir problemi alt problemlere bölmektir. Bu şekilde, LLM'ye daha büyük problemi nasıl "fethedeceği" konusunda rehberlik edersiniz. Veri bilimi için iyi bir örnek şu şekilde olabilir:

> İstek: Veri bilimi nasıl 5 adımda yapılır?

AI asistanınız şu şekilde yanıt verir:

1. Veri toplama
1. Veriyi temizleme
1. Veriyi analiz etme
1. Veriyi görselleştirme
1. Veriyi sunma

### Kendi kendini iyileştirme, sonuçları eleştirme

Üretken yapay zekalar ve LLM'ler ile çıktıya güvenemezsiniz. Onu doğrulamanız gerekir. Sonuçta, LLM size doğru olanı değil, söylemesi en olası olanı sunar. Bu nedenle, LLM'ye kendini eleştirmesini istemek iyi bir fikirdir, bu da bizi kendi kendini iyileştirme tekniğine götürür.

Nasıl çalışır:

1. LLM'den bir problemi çözmesini isteyen ilk istek
1. LLM yanıt verir
1. Yanıtı eleştirir ve AI'dan iyileştirmesini istersiniz
1. LLM tekrar yanıt verir, bu kez eleştiriyi dikkate alır ve önerdiği çözümleri sunar

Bu süreci istediğiniz kadar tekrarlayabilirsiniz.

İşte bu tekniği kullanan bir örnek:

> İstek: "Ürünler ve müşteriler rotaları olan bir Python Web API oluştur"

AI Yanıtı:

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

> İstek: Yukarıdaki kodun 3 iyileştirmesini öner

AI Yanıtı:

```text
Sure, here are three suggestions to improve the code:

Import the correct module: The first line should import Flask instead of flask. The correct import statement should be from flask import Flask.

Add a main function: Add a if __name__ == '__main__': block to the end of the file to run the application when the file is executed.

Use f-strings: Use f-strings to format the return statements in the route functions. For example, return 'Products' can be changed to return f'This is the {request.path} page'.
```

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/products')
def products():
    return f'This is the {request.path} page'

@app.route('/customers')
def customers():
    return f'This is the {request.path} page'

if __name__ == '__main__':
    app.run()
```

Gördüğünüz gibi, yukarıdaki AI yanıtı, ilk önerilen kodu eleştirerek iyileştiriyor.

### Maieutik istek

Maieutik istek, kendi kendini iyileştirmeye benzer bir tekniktir, ancak daha çok LLM'den kendini açıklamasını istemekle ilgilidir. Amaç, LLM'nin çıktısındaki tutarsızlıkları azaltmak ve doğru sonuca ulaşmasını sağlamaktır. İzlenecek iş akışı:

1. LLM'den bir soruyu yanıtlamasını isteyin
1. Yanıtın her bir bölümü için LLM'den daha ayrıntılı açıklama yapmasını isteyin.
1. Tutarsızlıklar varsa, tutarsız olan bölümleri çıkarın.

2 ve 3'ü tüm bölümleri gözden geçirene ve yanıtla tatmin olana kadar tekrarlayın.

İşte bir örnek istek:

> İstek: Bir pandemiyi hafifletmek için bir kriz planı nasıl 5 adımda oluşturulur?
> LLM yanıtı:

```text
1. Identify the risks
1. Identify the stakeholders
1. Identify the resources
1. Identify the actions
1. Identify the communication channels
```

5 adımı belirledi, ancak bunun doğru olup olmadığını belirleyebilir miyiz? LLM'den her adımı daha ayrıntılı açıklamasını isteyelim:

> İstek: İlk adımı daha ayrıntılı açıklayın, bir pandemideki riskler nelerdir?

```text
The risks are the following:

- Loss of life
- Loss of business
- Loss of reputation
- Loss of customers
- Loss of employees
```

Bu noktada, LLM'nin doğru olduğundan emin olmak istiyoruz, bu yüzden ilk riski daha ayrıntılı açıklamasını istiyoruz ve yukarıdaki yanıtla tutarlı olmasını umuyoruz:

> İstek: Bir pandemide en büyük risk nedir ve neden?

```text
The biggest risk is loss of life because it's the most important thing to protect.
```

> Bir pandemideki en büyük iki risk nedir?

```text
The two biggest risks are loss of life and loss of business.
```

Bu noktada, LLM tutarlı ve "hayat" ve "iş"i en büyük iki risk olarak belirtiyor. Şimdi bir sonraki adıma geçebilir ve oldukça emin hissedebiliriz. Ancak, LLM'ye körü körüne güvenmemeliyiz, çıktıyı her zaman doğrulamalıyız.

## Çıktınızı çeşitlendirin

LLM'ler doğası gereği deterministik değildir, yani aynı isteği her çalıştırdığınızda farklı sonuçlar alırsınız. Örneğin şu isteği deneyin:

> "Bir Python Web API için kod oluştur"

```python
# Import necessary modules
import flask
from flask import request, jsonify

# Create a Flask app
app = flask.Flask(__name__)

# Create a route for the API
@app.route('/api', methods=['GET'])
def api():
    # Get the data from the request
    data = request.args

    # Process the data
    result = process_data(data)

    # Return the result as JSON
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

Aynı isteği tekrar çalıştırmak biraz farklı bir yanıt oluşturur:

```python
#import necessary packages
import flask
from flask import request, jsonify

#create the Flask application
app = flask.Flask(__name__)
app.config["DEBUG"] = True

#create a list of books
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

#create an endpoint for the API
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Books API</h1>
<p>A prototype API for retrieving books.</p>'''

#create an endpoint to return all books
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

#create an endpoint to return a single book
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    #check if an ID was provided as part of the URL
    #if ID is provided, assign it to a variable
    #if no ID is provided, display an error
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    #create an empty list for our results
    results = []

    #loop through the data and match results that fit the requested ID
    #IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    #use the jsonify function from Flask to convert our list of
    #Python dictionaries to the JSON format
    return jsonify(results)

app.run()
```

> Peki çeşitlendirilmiş çıktı bir sorun mu?

Ne yapmaya çalıştığınıza bağlı. Belirli bir yanıt istiyorsanız bu bir sorun. "Coğrafya hakkında herhangi 3 soru oluştur" gibi çeşitlendirilmiş bir çıktı istiyorsanız, bu bir sorun değildir.

### Çıktınızı çeşitlendirmek için sıcaklık kullanma

Tamam, çıktıyı daha öngörülebilir, yani daha deterministik olacak şekilde sınırlamak istediğimize karar verdik. Bunu nasıl yaparız?

Sıcaklık, 0 ile 1 arasında bir değerdir; burada 0 en deterministik ve 1 en çeşitlendirilmiş olanıdır. Varsayılan değer 0.7'dir. Sıcaklık 0.1 olarak ayarlandığında aynı isteğin iki çalıştırmasında ne olduğunu görelim:

> "Bir Python Web API için kod oluştur"

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

İsteği tekrar çalıştırmak şu sonucu verir:

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

Bu iki çıktı arasında yalnızca küçük bir fark var. Bu sefer tam tersini yapalım, sıcaklığı 0.9 olarak ayarlayalım:

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

Gördüğünüz gibi, sonuçlar daha farklı olamazdı.

> Unutmayın, çıktıyı çeşitlendirmek için değiştirebileceğiniz daha fazla parametre var, örneğin top-k, top-p, tekrar cezası, uzunluk cezası ve çeşitlilik cezası, ancak bunlar bu müfredatın kapsamı dışında.

## İyi Uygulamalar

İstediğiniz sonuçları elde etmek için uygulayabileceğiniz birçok yöntem var. Prompting'i daha fazla kullandıkça kendi tarzınızı bulacaksınız.

Ele aldığımız tekniklere ek olarak, bir LLM'yi yönlendirirken dikkate alınması gereken bazı iyi uygulamalar vardır.

İşte dikkate almanız gereken bazı iyi uygulamalar:

- **Bağlamı belirtin**. Bağlam önemlidir, alan, konu gibi ne kadar çok ayrıntı verebilirseniz o kadar iyi olur.
- Çıktıyı sınırlayın. Belirli bir öğe sayısı veya belirli bir uzunluk istiyorsanız, bunu belirtin.
- **Hem ne istediğinizi hem de nasıl istediğinizi belirtin**. Ne istediğinizi ve nasıl istediğinizi belirtmeyi unutmayın, örneğin "Ürünler ve müşteriler rotaları olan bir Python Web API oluştur, bunu 3 dosyaya böl".
- **Şablonlar kullanın**. Çoğu zaman, şirketinizden gelen verilerle prompt'larınızı zenginleştirmek isteyeceksiniz. Bunu yapmak için şablonlar kullanın. Şablonlar, gerçek verilerle değiştirebileceğiniz değişkenlere sahip olabilir.
- **Doğru yazın**. LLM'ler size doğru bir yanıt verebilir, ancak doğru yazarsanız daha iyi bir yanıt alırsınız.

## Ödev

İşte Flask kullanarak basit bir API oluşturmayı gösteren Python kodu:

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

GitHub Copilot veya ChatGPT gibi bir yapay zeka asistanı kullanın ve kodu iyileştirmek için "self-refine" tekniğini uygulayın.

## Çözüm

Kodda uygun prompt'lar ekleyerek ödevi çözmeyi deneyin.

> [!TIP]
> İyileştirme istemek için bir prompt oluşturun, iyileştirme sayısını sınırlamak iyi bir fikir olabilir. Ayrıca mimari, performans, güvenlik gibi belirli bir şekilde iyileştirme istemek de mümkündür.

[Çözüm](../../../05-advanced-prompts/python/aoai-solution.py)

## Bilgi Kontrolü

Neden chain-of-thought prompting kullanmalıyım? Bana 1 doğru ve 2 yanlış yanıt gösterin.

1. LLM'ye bir problemi nasıl çözeceğini öğretmek için.
1. B, LLM'ye koddaki hataları bulmayı öğretmek için.
1. C, LLM'ye farklı çözümler üretmesini öğretmek için.

A: 1, çünkü chain-of-thought, LLM'ye bir problemi nasıl çözeceğini göstermek için bir dizi adım ve benzer problemler ile nasıl çözüldüklerini sağlamaktır.

## 🚀 Zorluk

Ödevde self-refine tekniğini kullandınız. Şimdi oluşturduğunuz herhangi bir programı alın ve ona hangi iyileştirmeleri uygulamak istediğinizi düşünün. Ardından önerilen değişiklikleri uygulamak için self-refine tekniğini kullanın. Sonuç hakkında ne düşündünüz, daha iyi mi yoksa daha kötü mü?

## Harika İş! Öğrenmeye Devam Edin

Bu dersi tamamladıktan sonra, Generative AI bilginizi geliştirmeye devam etmek için [Generative AI Öğrenme koleksiyonumuza](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) göz atın!

Prompt Engineering bilgimizi kullanarak [metin oluşturma uygulamaları](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst) oluşturacağımız 6. Derse geçin.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.