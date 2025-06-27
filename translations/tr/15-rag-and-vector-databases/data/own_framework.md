<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-06-25T23:23:51+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "tr"
}
-->
# Sinir Ağlarına Giriş. Çok Katmanlı Algılayıcı

Önceki bölümde, en basit sinir ağı modeli olan tek katmanlı algılayıcıyı, doğrusal iki sınıflı sınıflandırma modelini öğrendiniz.

Bu bölümde, bu modeli daha esnek bir çerçeveye genişleteceğiz ve bu sayede:

* iki sınıfa ek olarak **çok sınıflı sınıflandırma** gerçekleştirebiliriz
* sınıflandırmaya ek olarak **regresyon problemlerini** çözebiliriz
* doğrusal olarak ayrılmayan sınıfları ayırabiliriz

Ayrıca, farklı sinir ağı mimarileri oluşturmamıza olanak tanıyacak kendi modüler çerçevemizi Python'da geliştireceğiz.

## Makine Öğreniminin Formalizasyonu

Makine Öğrenimi problemini formalize ederek başlayalım. Elimizde **X** eğitim veri seti ve **Y** etiketleri olduğunu varsayalım ve en doğru tahminleri yapacak bir model *f* inşa etmemiz gerekiyor. Tahminlerin kalitesi **Kayıp fonksiyonu** ℒ ile ölçülür. Aşağıdaki kayıp fonksiyonları sıkça kullanılır:

* Bir sayı tahmin etmemiz gerektiğinde, regresyon problemi için **mutlak hata** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| veya **karesel hata** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup> kullanabiliriz.
* Sınıflandırma için, **0-1 kaybı** (temelde modelin **doğruluğu** ile aynıdır) veya **lojistik kayıp** kullanırız.

Tek katmanlı algılayıcı için, *f* fonksiyonu doğrusal bir fonksiyon olarak tanımlanmıştır: *f(x)=wx+b* (burada *w* ağırlık matrisi, *x* girdi özellikleri vektörü ve *b* yanlılık vektörüdür). Farklı sinir ağı mimarileri için bu fonksiyon daha karmaşık bir form alabilir.

> Sınıflandırma durumunda, ağ çıktısı olarak ilgili sınıfların olasılıklarını elde etmek genellikle arzu edilir. Keyfi sayıları olasılıklara dönüştürmek için (örneğin, çıktıyı normalize etmek için) genellikle **softmax** fonksiyonu σ kullanırız ve *f* fonksiyonu *f(x)=σ(wx+b)* olur.

Yukarıdaki *f* tanımında, *w* ve *b* **parametreler** olarak adlandırılır: θ=⟨*w,b*⟩. Veri seti ⟨**X**,**Y**⟩ verildiğinde, parametreler θ'nın bir fonksiyonu olarak tüm veri seti üzerindeki genel hatayı hesaplayabiliriz.

> ✅ **Sinir ağı eğitiminin amacı, parametreleri θ değiştirerek hatayı minimize etmektir**

## Gradyan İnişi Optimizasyonu

**Gradyan inişi** olarak adlandırılan iyi bilinen bir fonksiyon optimizasyon yöntemi vardır. Fikir, kayıp fonksiyonunun parametrelere göre türevini (çok boyutlu durumda **gradyan** olarak adlandırılır) hesaplayarak, hatanın azalacağı şekilde parametreleri değiştirmektir. Bu şu şekilde formalize edilebilir:

* Parametreleri bazı rastgele değerlerle başlat: w<sup>(0)</sup>, b<sup>(0)</sup>
* Aşağıdaki adımı birçok kez tekrarla:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Eğitim sırasında, optimizasyon adımlarının tüm veri seti dikkate alınarak hesaplanması gerekir (hatırlayın ki kayıp, tüm eğitim örnekleri üzerinden bir toplam olarak hesaplanır). Ancak, gerçek hayatta **minibatch** adı verilen veri setinin küçük parçalarını alırız ve gradyanları veri alt kümesine dayalı olarak hesaplarız. Her seferinde alt küme rastgele alındığı için, bu yöntem **stokastik gradyan inişi** (SGD) olarak adlandırılır.

## Çok Katmanlı Algılayıcılar ve Geriye Yayılım

Yukarıda gördüğümüz gibi, tek katmanlı bir ağ doğrusal olarak ayrılabilen sınıfları sınıflandırabilir. Daha zengin bir model inşa etmek için, ağın birkaç katmanını birleştirebiliriz. Matematiksel olarak bu, *f* fonksiyonunun daha karmaşık bir form alacağı ve birkaç adımda hesaplanacağı anlamına gelir:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Burada, α bir **doğrusal olmayan aktivasyon fonksiyonu**, σ bir softmax fonksiyonu ve parametreler θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Gradyan inişi algoritması aynı kalır, ancak gradyanları hesaplamak daha zor olur. Zincir türev kuralı verilmişken, türevleri şu şekilde hesaplayabiliriz:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Zincir türev kuralı, kayıp fonksiyonunun parametrelere göre türevlerini hesaplamak için kullanılır.

Tüm bu ifadelerin en sol kısmı aynıdır, bu nedenle kayıp fonksiyonundan başlayarak ve "geri" giderek hesaplama grafiği boyunca türevleri etkili bir şekilde hesaplayabiliriz. Bu nedenle, çok katmanlı bir algılayıcıyı eğitme yöntemi **geriye yayılım** veya 'backprop' olarak adlandırılır.

> TODO: görsel alıntı

> ✅ Geriye yayılımı çok daha ayrıntılı olarak not defteri örneğimizde ele alacağız.

## Sonuç

Bu derste, kendi sinir ağı kütüphanemizi inşa ettik ve bunu basit bir iki boyutlu sınıflandırma görevi için kullandık.

## 🚀 Meydan Okuma

Eşlik eden not defterinde, çok katmanlı algılayıcılar oluşturmak ve eğitmek için kendi çerçevenizi uygulayacaksınız. Modern sinir ağlarının nasıl çalıştığını ayrıntılı olarak görebileceksiniz.

OwnFramework not defterine geçin ve üzerinde çalışın.

## Gözden Geçirme & Kendi Kendine Çalışma

Geriye yayılım, AI ve ML'de yaygın olarak kullanılan bir algoritmadır, daha ayrıntılı olarak çalışmaya değer.

## Ödev

Bu laboratuvarda, bu derste inşa ettiğiniz çerçeveyi kullanarak MNIST el yazısı rakam sınıflandırmasını çözmeniz isteniyor.

* Talimatlar
* Not defteri

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) AI çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından doğabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.