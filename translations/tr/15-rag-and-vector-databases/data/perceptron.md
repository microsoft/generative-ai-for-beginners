<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-05-20T02:36:09+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "tr"
}
-->
# Sinir Ağlarına Giriş: Perceptron

Modern sinir ağına benzer bir şeyi uygulamak için yapılan ilk girişimlerden biri, 1957'de Cornell Aeronautical Laboratory'den Frank Rosenblatt tarafından gerçekleştirildi. "Mark-1" adı verilen bu donanım uygulaması, üçgen, kare ve daire gibi ilkel geometrik şekilleri tanımak için tasarlandı.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Resimler Wikipedia'dan

Bir giriş görüntüsü 20x20 fotocell dizisi ile temsil edildi, dolayısıyla sinir ağının 400 girişi ve bir ikili çıktısı vardı. Basit bir ağ, **eşik mantık birimi** olarak da adlandırılan bir nöron içeriyordu. Sinir ağı ağırlıkları, eğitim aşamasında manuel ayarlama gerektiren potansiyometreler gibi davranıyordu.

> ✅ Potansiyometre, kullanıcının bir devrenin direncini ayarlamasına olanak tanıyan bir cihazdır.

> New York Times o zamanlar perceptron hakkında şöyle yazmıştı: *[Deniz Kuvvetleri'nin] yürüyebilecek, konuşabilecek, görebilecek, yazabilecek, kendini üretebilecek ve varlığının farkında olacak bir elektronik bilgisayar embriyosu.*

## Perceptron Modeli

Modelimizde N özelliğe sahip olduğumuzu varsayalım, bu durumda giriş vektörü N boyutunda bir vektör olacaktır. Bir perceptron, iki sınıf arasında ayrım yapabilen bir **ikili sınıflandırma** modelidir. Her giriş vektörü x için perceptronumuzun çıktısının sınıfa bağlı olarak +1 veya -1 olacağını varsayacağız. Çıktı şu formülle hesaplanacaktır:

y(x) = f(w<sup>T</sup>x)

burada f bir adım aktivasyon fonksiyonudur

## Perceptronu Eğitmek

Bir perceptronu eğitmek için, çoğu değeri doğru bir şekilde sınıflandıran, yani en küçük **hata** ile sonuçlanan bir ağırlık vektörü w bulmamız gerekir. Bu hata, **perceptron kriteri** ile şu şekilde tanımlanır:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

burada:

* toplam, yanlış sınıflandırmaya neden olan eğitim veri noktaları i üzerinde alınır
* x<sub>i</sub> giriş verisidir ve t<sub>i</sub> sırasıyla negatif ve pozitif örnekler için -1 veya +1'dir.

Bu kriter, ağırlıklar w'nin bir fonksiyonu olarak kabul edilir ve bunu minimize etmemiz gerekir. Genellikle, **gradyan inişi** adı verilen bir yöntem kullanılır; burada bazı başlangıç ağırlıkları w<sup>(0)</sup> ile başlarız ve ardından her adımda ağırlıkları şu formüle göre güncelleriz:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Burada η, **öğrenme hızı** olarak adlandırılır ve ∇E(w), E'nin **gradyanı**nı ifade eder. Gradyanı hesapladıktan sonra

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Python'daki algoritma şöyle görünür:

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## Sonuç

Bu derste, bir ikili sınıflandırma modeli olan perceptronu ve ağırlık vektörü kullanarak nasıl eğitileceğini öğrendiniz.

## 🚀 Meydan Okuma

Kendi perceptronunuzu oluşturmayı denemek isterseniz, Azure ML tasarımcısını kullanan Microsoft Learn'deki bu laboratuvarı deneyin.

## Gözden Geçirme & Kendi Kendine Çalışma

Perceptronun bir oyuncak problemi ve gerçek yaşam problemlerini nasıl çözebileceğini görmek ve öğrenmeye devam etmek için Perceptron not defterine gidin.

Perceptronlar hakkında ilginç bir makale de burada.

## Ödev

Bu derste, ikili sınıflandırma görevi için bir perceptron uyguladık ve iki el yazısı rakam arasında sınıflandırma yapmak için kullandık. Bu laboratuvarda, verilen bir görüntünün en olası rakamını belirleyerek rakam sınıflandırma problemini tamamen çözmeniz isteniyor.

* Talimatlar
* Not Defteri

**Feragatname**: 
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilinde olan hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.