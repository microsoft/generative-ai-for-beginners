<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-06-25T23:39:41+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "tr"
}
-->
# Sinir Ağlarına Giriş: Perceptron

Modern bir sinir ağına benzer bir şey uygulamak için yapılan ilk girişimlerden biri, 1957 yılında Cornell Havacılık Laboratuvarı'ndan Frank Rosenblatt tarafından gerçekleştirilmiştir. Bu, üçgenler, kareler ve daireler gibi ilkel geometrik şekilleri tanımak için tasarlanmış "Mark-1" adlı bir donanım uygulamasıydı.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Görseller Wikipedia'dan alınmıştır

Bir giriş görüntüsü 20x20 fotohücre dizisiyle temsil edildi, bu nedenle sinir ağının 400 girişi ve bir ikili çıktısı vardı. Basit bir ağ, **eşik mantık birimi** olarak da adlandırılan bir nöron içeriyordu. Sinir ağı ağırlıkları, eğitim aşamasında manuel ayarlama gerektiren potansiyometreler gibi davrandı.

> ✅ Potansiyometre, kullanıcının bir devrenin direncini ayarlamasına olanak tanıyan bir cihazdır.

> The New York Times o dönemde perceptron hakkında şöyle yazdı: *[Donanmanın] yürümesini, konuşmasını, görmesini, yazmasını, kendini kopyalamasını ve varlığının farkında olmasını beklediği elektronik bir bilgisayar embriyosu.*

## Perceptron Modeli

Modelimizde N özelliğe sahip olduğumuzu varsayalım, bu durumda giriş vektörü N boyutunda bir vektör olacaktır. Bir perceptron, **ikili sınıflandırma** modelidir, yani iki sınıf giriş verisi arasında ayrım yapabilir. Her giriş vektörü x için perceptronumuzun çıktısının sınıfa bağlı olarak ya +1 ya da -1 olacağını varsayacağız. Çıktı şu formülle hesaplanacaktır:

y(x) = f(w<sup>T</sup>x)

burada f bir basamak aktivasyon fonksiyonudur

## Perceptron Eğitimi

Bir perceptron eğitmek için, çoğu değeri doğru sınıflandıran, yani en küçük **hata** ile sonuçlanan bir ağırlık vektörü w bulmamız gerekir. Bu hata, aşağıdaki şekilde tanımlanan **perceptron kriteri** ile tanımlanır:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

burada:

* toplam, yanlış sınıflandırma ile sonuçlanan eğitim veri noktaları i üzerinde alınır
* x<sub>i</sub> giriş verisidir ve t<sub>i</sub> negatif ve pozitif örnekler için sırasıyla -1 veya +1'dir.

Bu kriter, ağırlıkların w bir fonksiyonu olarak kabul edilir ve bunu minimize etmemiz gerekir. Genellikle, başlangıç ağırlıkları w<sup>(0)</sup> ile başladığımız ve her adımda ağırlıkları şu formüle göre güncellediğimiz **gradyan inişi** adlı bir yöntem kullanılır:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Burada η, **öğrenme hızı** olarak adlandırılır ve ∇E(w) E'nin **gradyanı**nı ifade eder. Gradyanı hesapladıktan sonra şu sonuca ulaşırız:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Python'da algoritma şu şekilde görünür:

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

Bu derste, ikili sınıflandırma modeli olan bir perceptron ve onu bir ağırlık vektörü kullanarak nasıl eğiteceğiniz hakkında bilgi edindiniz.

## 🚀 Meydan Okuma

Kendi perceptronunuzu oluşturmayı denemek isterseniz, Azure ML tasarımcısını kullanan Microsoft Learn'deki bu laboratuvarı deneyin.

## İnceleme ve Kendi Kendine Çalışma

Bir oyuncak problemi ve gerçek hayattaki problemleri çözmek için perceptronu nasıl kullanabileceğimizi görmek ve öğrenmeye devam etmek için Perceptron defterine gidin.

Ayrıca, perceptronlar hakkında ilginç bir makale de burada.

## Ödev

Bu derste, ikili sınıflandırma görevi için bir perceptron uyguladık ve bunu iki el yazısı rakam arasında sınıflandırmak için kullandık. Bu laboratuvarda, rakam sınıflandırma problemini tamamen çözmeniz, yani verilen bir görüntünün hangi rakama karşılık geldiğini belirlemeniz isteniyor.

* Talimatlar
* Defter

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için, profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlama veya yanlış yorumlamalardan sorumlu değiliz.