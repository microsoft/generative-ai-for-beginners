<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-05-20T02:19:32+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "tr"
}
-->
# Sinir Ağlarına Giriş. Çok Katmanlı Algılayıcı

Önceki bölümde, en basit sinir ağı modeli olan tek katmanlı algılayıcıyı, yani iki sınıflı bir doğrusal sınıflandırma modelini öğrendiniz.

Bu bölümde bu modeli daha esnek bir çerçeveye genişleteceğiz, böylece:

* iki sınıfa ek olarak **çok sınıflı sınıflandırma** yapabiliriz
* sınıflandırmaya ek olarak **regresyon problemlerini** çözebiliriz
* doğrusal olarak ayrılabilir olmayan sınıfları ayırabiliriz

Ayrıca, farklı sinir ağı mimarileri oluşturmamıza olanak tanıyacak kendi modüler çerçevemizi Python'da geliştireceğiz.

## Makine Öğrenmesinin Formalizasyonu

Makine Öğrenmesi problemini formüle ederek başlayalım. Diyelim ki **X** adlı bir eğitim veri setimiz ve **Y** adlı etiketlerimiz var ve en doğru tahminleri yapacak bir model *f* oluşturmalıyız. Tahminlerin kalitesi **Kayıp fonksiyonu** ℒ ile ölçülür. Aşağıdaki kayıp fonksiyonları sıkça kullanılır:

* Regresyon problemi için, bir sayı tahmin etmemiz gerektiğinde, **mutlak hata** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| veya **karesel hata** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup> kullanabiliriz
* Sınıflandırma için, **0-1 kaybı** (temelde modelin **doğruluğu** ile aynıdır) veya **lojistik kayıp** kullanırız.

Tek seviyeli algılayıcı için, *f* fonksiyonu *f(x)=wx+b* şeklinde doğrusal bir fonksiyon olarak tanımlanmıştır (burada *w* ağırlık matrisi, *x* girdi özelliklerinin vektörü ve *b* önyargı vektörüdür). Farklı sinir ağı mimarileri için, bu fonksiyon daha karmaşık bir form alabilir.

> Sınıflandırma durumunda, ağ çıktısı olarak ilgili sınıfların olasılıklarını elde etmek genellikle arzu edilir. Keyfi sayıları olasılıklara dönüştürmek (örneğin, çıktıyı normalize etmek) için sıklıkla **softmax** fonksiyonu σ kullanırız ve *f* fonksiyonu *f(x)=σ(wx+b)* olur

Yukarıdaki *f* tanımında, *w* ve *b* **parametreler** olarak adlandırılır θ=⟨*w,b*⟩. Veri seti ⟨**X**,**Y**⟩ verildiğinde, parametreler θ'nın bir fonksiyonu olarak tüm veri seti üzerinde toplam hatayı hesaplayabiliriz.

> ✅ **Sinir ağı eğitiminin amacı, parametreleri θ değiştirerek hatayı en aza indirmektir**

## Gradient Descent Optimizasyonu

Fonksiyon optimizasyonunun iyi bilinen bir yöntemi olan **gradient descent** vardır. Fikir, parametrelere göre kayıp fonksiyonunun türevini (çok boyutlu durumda **gradient** olarak adlandırılır) hesaplayabileceğimiz ve parametreleri hatanın azalacağı şekilde değiştirebileceğimizdir. Bu şu şekilde formüle edilebilir:

* Parametreleri bazı rastgele değerlerle başlat w<sup>(0)</sup>, b<sup>(0)</sup>
* Aşağıdaki adımı birçok kez tekrarla:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Eğitim sırasında, optimizasyon adımlarının tüm veri seti dikkate alınarak hesaplanması gerekir (unutmayın ki kayıp, tüm eğitim örnekleri üzerinden bir toplam olarak hesaplanır). Ancak, gerçek hayatta veri setinin küçük parçaları olan **minibatch**'leri alırız ve verilerin bir alt kümesine dayanarak gradyanları hesaplarız. Her seferinde rastgele bir alt küme alındığı için, bu yöntem **stokastik gradient descent** (SGD) olarak adlandırılır.

## Çok Katmanlı Algılayıcılar ve Geri Yayılım

Yukarıda gördüğümüz gibi, tek katmanlı ağ doğrusal olarak ayrılabilir sınıfları sınıflandırabilir. Daha zengin bir model oluşturmak için ağın birkaç katmanını birleştirebiliriz. Matematiksel olarak, *f* fonksiyonu daha karmaşık bir form alacak ve birkaç adımda hesaplanacaktır:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Burada, α **doğrusal olmayan aktivasyon fonksiyonu**, σ softmax fonksiyonu ve parametreler θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>'dir.

Gradient descent algoritması aynı kalır, ancak gradyanları hesaplamak daha zor olur. Zincir türevleme kuralı verilmişken, türevleri şu şekilde hesaplayabiliriz:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Zincir türevleme kuralı, parametrelere göre kayıp fonksiyonunun türevlerini hesaplamak için kullanılır.

Bu ifadelerin sol tarafındaki kısmı aynı olduğundan, türevleri etkili bir şekilde kayıp fonksiyonundan başlayarak ve hesaplama grafiği boyunca "geri giderek" hesaplayabiliriz. Dolayısıyla, çok katmanlı bir algılayıcıyı eğitme yöntemi **geri yayılım** veya 'backprop' olarak adlandırılır.

> TODO: görsel kaynak

> ✅ Not defteri örneğimizde geri yayılımı çok daha detaylı ele alacağız.

## Sonuç

Bu derste, kendi sinir ağı kütüphanemizi oluşturduk ve bunu basit bir iki boyutlu sınıflandırma görevi için kullandık.

## 🚀 Meydan Okuma

Eşlik eden not defterinde, çok katmanlı algılayıcılar oluşturmak ve eğitmek için kendi çerçevenizi uygulayacaksınız. Modern sinir ağlarının nasıl çalıştığını detaylı olarak görebileceksiniz.

OwnFramework not defterine geçin ve üzerinde çalışın.

## İnceleme ve Kendi Kendine Çalışma

Geri yayılım, AI ve ML'de yaygın olarak kullanılan bir algoritmadır, daha detaylı incelenmeye değerdir.

## Ödev

Bu laboratuvarda, bu derste oluşturduğunuz çerçeveyi kullanarak MNIST el yazısı rakam sınıflandırmasını çözmeniz isteniyor.

* Talimatlar
* Not defteri

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlaşılma veya yanlış yorumlamalardan sorumlu değiliz.