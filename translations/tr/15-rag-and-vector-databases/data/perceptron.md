<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T16:57:37+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "tr"
}
-->
# Sinir Ağlarına Giriş: Perceptron

Modern bir sinir ağına benzer bir şeyi uygulamaya yönelik ilk girişimlerden biri, 1957 yılında Cornell Aeronautical Laboratory’den Frank Rosenblatt tarafından yapıldı. Bu, "Mark-1" adlı bir donanım uygulamasıydı ve üçgen, kare ve daire gibi temel geometrik şekilleri tanımak için tasarlanmıştı.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Görseller Wikipedia’dan alınmıştır

Girdi görüntüsü 20x20 fotohücre dizisiyle temsil ediliyordu, böylece sinir ağı 400 girişe ve bir ikili çıkışa sahipti. Basit bir ağ, aynı zamanda **eşik mantık birimi** olarak da adlandırılan tek bir nöron içeriyordu. Sinir ağı ağırlıkları, eğitim aşamasında manuel ayar gerektiren potansiyometreler gibi çalışıyordu.

> ✅ Potansiyometre, kullanıcının bir devrenin direncini ayarlamasına olanak tanıyan bir cihazdır.

> The New York Times o dönemde perceptron hakkında şöyle yazmıştı: *[Donanma’nın] yürüyebilen, konuşabilen, görebilen, yazabilen, kendini çoğaltabilen ve varlığının farkında olan bir elektronik bilgisayarın embriyosu.*

## Perceptron Modeli

Modelimizde N özellik olduğunu varsayalım, bu durumda giriş vektörü N boyutlu bir vektör olur. Perceptron, **ikili sınıflandırma** modeli olup, yani giriş verisini iki sınıf arasında ayırt edebilir. Her giriş vektörü x için perceptronumuzun çıktısının, sınıfa bağlı olarak +1 veya -1 olacağını varsayacağız. Çıktı şu formülle hesaplanır:

y(x) = f(w<sup>T</sup>x)

burada f bir basamak aktivasyon fonksiyonudur

## Perceptron Eğitimi

Bir perceptronu eğitmek için, çoğu değeri doğru sınıflandıran yani en küçük **hata**yı veren ağırlıklar vektörü w’yi bulmamız gerekir. Bu hata, **perceptron kriteri** ile şu şekilde tanımlanır:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

burada:

* toplam, yanlış sınıflandırmaya yol açan eğitim verisi noktaları i üzerinde alınır
* x<sub>i</sub> giriş verisi, t<sub>i</sub> ise negatif ve pozitif örnekler için sırasıyla -1 veya +1’dir.

Bu kriter, ağırlıklar w’nin bir fonksiyonu olarak kabul edilir ve minimize edilmelidir. Genellikle, **gradyan inişi** adı verilen bir yöntem kullanılır; burada bazı başlangıç ağırlıkları w<sup>(0)</sup> ile başlanır ve her adımda ağırlıklar şu formüle göre güncellenir:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Burada η, **öğrenme hızı** olarak adlandırılır ve ∇E(w), E’nin **gradyanını** gösterir. Gradyan hesaplandıktan sonra sonuç olarak

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

elde edilir.

Python’daki algoritma şu şekildedir:

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

Bu derste, ikili sınıflandırma modeli olan perceptron’u ve onu ağırlıklar vektörü kullanarak nasıl eğitebileceğinizi öğrendiniz.

## 🚀 Meydan Okuma

Kendi perceptron’unuzu oluşturmayı denemek isterseniz, Azure ML designer kullanan Microsoft Learn’daki bu laboratuvarı deneyebilirsiniz.

## İnceleme & Kendi Kendine Çalışma

Perceptron’u hem basit bir problem hem de gerçek hayat problemlerini çözmek için nasıl kullanabileceğimizi görmek ve öğrenmeye devam etmek için Perceptron defterine gidin.

Ayrıca perceptronlar hakkında ilginç bir makale de burada.

## Ödev

Bu derste, ikili sınıflandırma görevi için bir perceptron uyguladık ve iki el yazısı rakamı arasında sınıflandırma yaptık. Bu laboratuvarda ise, verilen bir görüntüye en uygun rakamın hangisi olduğunu belirleyerek rakam sınıflandırma problemini tamamen çözmeniz isteniyor.

* Talimatlar
* Defter

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.