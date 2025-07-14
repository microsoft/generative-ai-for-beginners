<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:46:16+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "tr"
}
-->
# Sinir Ağlarına Giriş. Çok Katmanlı Perceptron

Önceki bölümde, en basit sinir ağı modeli olan tek katmanlı perceptron’u, yani doğrusal iki sınıflı sınıflandırma modelini öğrendiniz.

Bu bölümde, bu modeli daha esnek bir yapıya genişleteceğiz ve şunları yapmamıza olanak tanıyacağız:

* İki sınıflı sınıflandırmanın yanı sıra **çok sınıflı sınıflandırma** yapmak
* Sınıflandırmanın yanı sıra **regresyon problemlerini** çözmek
* Doğrusal olarak ayrılamayan sınıfları ayırmak

Ayrıca, farklı sinir ağı mimarileri oluşturabilmemizi sağlayacak kendi modüler Python çerçevemizi geliştireceğiz.

## Makine Öğrenmesinin Formalizasyonu

Makine Öğrenmesi problemini formalize ederek başlayalım. Diyelim ki etiketleri **Y** olan bir eğitim veri setimiz **X** var ve en doğru tahminleri yapacak bir model *f* inşa etmemiz gerekiyor. Tahminlerin kalitesi **Kayıp fonksiyonu** ℒ ile ölçülür. Aşağıdaki kayıp fonksiyonları sıkça kullanılır:

* Regresyon problemi için, yani bir sayı tahmin etmemiz gerektiğinde, **mutlak hata** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| veya **kare hata** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup> kullanılabilir
* Sınıflandırma için, **0-1 kaybı** (temelde modelin **doğruluğu** ile aynı) veya **lojistik kayıp** kullanılır.

Tek katmanlı perceptron için, *f* fonksiyonu doğrusal bir fonksiyon olarak tanımlanmıştı: *f(x)=wx+b* (burada *w* ağırlık matrisi, *x* giriş özellikleri vektörü, *b* ise bias vektörüdür). Farklı sinir ağı mimarileri için bu fonksiyon daha karmaşık bir biçim alabilir.

> Sınıflandırma durumunda, ağ çıktısı olarak ilgili sınıfların olasılıklarını almak genellikle tercih edilir. Rastgele sayıları olasılıklara dönüştürmek (örneğin çıktıyı normalize etmek) için sıklıkla **softmax** fonksiyonu σ kullanılır ve fonksiyon *f* şu hale gelir: *f(x)=σ(wx+b)*

Yukarıdaki *f* tanımında, *w* ve *b* **parametreler** olarak adlandırılır ve θ=⟨*w,b*⟩ ile gösterilir. Veri seti ⟨**X**,**Y**⟩ verildiğinde, parametrelerin bir fonksiyonu olarak tüm veri seti üzerindeki toplam hatayı hesaplayabiliriz.

> ✅ **Sinir ağı eğitiminin amacı, parametreler θ’yi değiştirerek hatayı minimize etmektir**

## Gradyan İnişi Optimizasyonu

Fonksiyon optimizasyonunda iyi bilinen bir yöntem olan **gradyan inişi** vardır. Fikir, kayıp fonksiyonunun parametrelere göre türevini (çok boyutlu durumda buna **gradyan** denir) hesaplayıp, parametreleri hatayı azaltacak şekilde değiştirmektir. Bu şu şekilde formalize edilebilir:

* Parametreleri rastgele değerlerle başlat w<sup>(0)</sup>, b<sup>(0)</sup>
* Aşağıdaki adımı birçok kez tekrarla:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Eğitim sırasında, optimizasyon adımları tüm veri seti göz önünde bulundurularak hesaplanmalıdır (kayıp tüm eğitim örnekleri üzerinden toplanarak hesaplanır). Ancak pratikte, veri setinden küçük parçalar olan **minibatch**’ler alınır ve gradyanlar bu alt küme üzerinden hesaplanır. Her seferinde rastgele alt küme seçildiği için bu yönteme **stokastik gradyan inişi** (SGD) denir.

## Çok Katmanlı Perceptronlar ve Geri Yayılım

Yukarıda gördüğümüz tek katmanlı ağ, doğrusal olarak ayrılabilen sınıfları sınıflandırabilir. Daha zengin bir model oluşturmak için ağın birkaç katmanını birleştirebiliriz. Matematiksel olarak bu, *f* fonksiyonunun daha karmaşık bir biçim alması ve birkaç adımda hesaplanması anlamına gelir:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Burada, α **doğrusal olmayan aktivasyon fonksiyonu**, σ softmax fonksiyonu ve parametreler θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Gradyan inişi algoritması aynı kalır, ancak gradyanları hesaplamak daha zorlaşır. Zincir türev kuralı kullanılarak türevler şu şekilde hesaplanabilir:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Kayıp fonksiyonunun parametrelere göre türevlerini hesaplamak için zincir türev kuralı kullanılır.

Dikkat edin, tüm bu ifadelerin en solundaki kısım aynıdır, bu yüzden türevleri kayıp fonksiyonundan başlayarak hesaplama grafiğinde "geriye doğru" etkili bir şekilde hesaplayabiliriz. Bu nedenle çok katmanlı perceptron eğitme yöntemi **geri yayılım** veya 'backprop' olarak adlandırılır.

> TODO: resim atıfı

> ✅ Geri yayılımı not defteri örneğimizde çok daha detaylı inceleyeceğiz.

## Sonuç

Bu derste, kendi sinir ağı kütüphanemizi oluşturduk ve bunu basit iki boyutlu bir sınıflandırma görevi için kullandık.

## 🚀 Meydan Okuma

Yanındaki not defterinde, çok katmanlı perceptronlar oluşturup eğitmek için kendi çerçevenizi uygulayacaksınız. Modern sinir ağlarının nasıl çalıştığını ayrıntılı olarak görebileceksiniz.

OwnFramework not defterine geçin ve üzerinde çalışın.

## Gözden Geçirme & Kendi Kendine Çalışma

Geri yayılım, yapay zeka ve makine öğrenmesinde yaygın kullanılan bir algoritmadır ve daha detaylı incelenmeye değerdir.

## Ödev

Bu laboratuvarda, bu derste oluşturduğunuz çerçeveyi kullanarak MNIST el yazısı rakam sınıflandırma problemini çözmeniz isteniyor.

* Talimatlar
* Not defteri

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.