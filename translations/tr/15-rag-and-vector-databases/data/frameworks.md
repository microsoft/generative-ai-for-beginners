<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-07-09T16:31:36+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "tr"
}
-->
# Sinir Ağı Çerçeveleri

Zaten öğrendiğimiz gibi, sinir ağlarını verimli bir şekilde eğitebilmek için iki şey yapmamız gerekiyor:

* Tensörler üzerinde işlem yapmak, örneğin çarpmak, toplamak ve sigmoid veya softmax gibi bazı fonksiyonları hesaplamak
* Tüm ifadelerin gradyanlarını hesaplamak, böylece gradyan inişi optimizasyonu yapabilmek

`numpy` kütüphanesi ilk kısmı yapabilirken, gradyanları hesaplamak için bir mekanizmaya ihtiyacımız var. Önceki bölümde geliştirdiğimiz çerçevede, geri yayılım yapan `backward` metodunun içinde tüm türev fonksiyonlarını manuel olarak programlamak zorundaydık. İdeal olarak, bir çerçeve bize tanımlayabileceğimiz *herhangi bir ifadenin* gradyanlarını hesaplama imkanı vermelidir.

Bir diğer önemli konu ise GPU veya TPU gibi özel hesaplama birimleri üzerinde işlem yapabilmektir. Derin sinir ağı eğitimi *çok fazla* hesaplama gerektirir ve bu hesaplamaları GPU’larda paralel olarak yapabilmek çok önemlidir.

> ✅ 'Paralelleştirmek' terimi, hesaplamaların birden fazla cihaz arasında dağıtılması anlamına gelir.

Şu anda en popüler iki sinir ağı çerçevesi TensorFlow ve PyTorch’tur. Her ikisi de CPU ve GPU üzerinde tensörlerle çalışmak için düşük seviyeli API sağlar. Düşük seviyeli API’nin üzerinde ise sırasıyla Keras ve PyTorch Lightning adında yüksek seviyeli API’ler bulunur.

Düşük Seviyeli API | TensorFlow | PyTorch
------------------|------------|---------
Yüksek Seviyeli API | Keras | PyTorch

Her iki çerçevedeki **düşük seviyeli API’ler**, sözde **hesaplama grafikleri** oluşturmanıza olanak tanır. Bu grafik, verilen giriş parametreleriyle çıktının (genellikle kayıp fonksiyonu) nasıl hesaplanacağını tanımlar ve eğer varsa GPU’da hesaplama için gönderilebilir. Bu hesaplama grafiğini türev alma ve gradyanları hesaplama fonksiyonları vardır; bu gradyanlar model parametrelerini optimize etmek için kullanılır.

**Yüksek seviyeli API’ler** ise sinir ağlarını çoğunlukla **katmanlar dizisi** olarak ele alır ve sinir ağlarının çoğunu çok daha kolay kurmanızı sağlar. Model eğitimi genellikle veriyi hazırlamayı ve ardından işi yapmak için `fit` fonksiyonunu çağırmayı gerektirir.

Yüksek seviyeli API, tipik sinir ağlarını çok hızlı bir şekilde, birçok detayı düşünmeden oluşturmanıza olanak tanır. Aynı zamanda düşük seviyeli API, eğitim süreci üzerinde çok daha fazla kontrol sunar ve bu yüzden yeni sinir ağı mimarileriyle uğraşırken araştırmalarda sıkça kullanılır.

Ayrıca her iki API’yi birlikte kullanabileceğinizi anlamak önemlidir; örneğin, düşük seviyeli API ile kendi ağ katman mimarinizi geliştirebilir ve bunu yüksek seviyeli API ile oluşturulup eğitilen daha büyük ağ içinde kullanabilirsiniz. Ya da yüksek seviyeli API ile katmanlar dizisi olarak bir ağ tanımlayıp, optimizasyonu gerçekleştirmek için kendi düşük seviyeli eğitim döngünüzü kullanabilirsiniz. Her iki API aynı temel kavramları kullanır ve birlikte iyi çalışacak şekilde tasarlanmıştır.

## Öğrenme

Bu kursta, içeriğin çoğunu hem PyTorch hem de TensorFlow için sunuyoruz. Tercih ettiğiniz çerçeveyi seçip sadece ilgili not defterlerini inceleyebilirsiniz. Hangi çerçeveyi seçeceğinizden emin değilseniz, internet üzerindeki **PyTorch vs. TensorFlow** tartışmalarını okuyabilirsiniz. Ayrıca her iki çerçeveyi de inceleyerek daha iyi anlayabilirsiniz.

Mümkün olduğunda, basitlik için Yüksek Seviyeli API’leri kullanacağız. Ancak sinir ağlarının temelden nasıl çalıştığını anlamanın önemli olduğunu düşünüyoruz, bu yüzden başlangıçta düşük seviyeli API ve tensörlerle çalışarak başlıyoruz. Yine de hızlı başlamak ve bu detaylara çok zaman harcamak istemiyorsanız, bunları atlayıp doğrudan yüksek seviyeli API not defterlerine geçebilirsiniz.

## ✍️ Alıştırmalar: Çerçeveler

Öğrenmenize aşağıdaki not defterlerinde devam edin:

Düşük Seviyeli API | TensorFlow+Keras Not Defteri | PyTorch
-------------------|------------------------------|---------
Yüksek Seviyeli API | Keras | *PyTorch Lightning*

Çerçevelerde ustalaştıktan sonra, aşırı öğrenme kavramını tekrar gözden geçirelim.

# Aşırı Öğrenme (Overfitting)

Aşırı öğrenme, makine öğreniminde son derece önemli bir kavramdır ve doğru anlaşılması çok önemlidir!

Aşağıdaki 5 noktayı (grafiklerde `x` ile gösterilmiştir) yaklaşık olarak modelleme problemini düşünelim:

!linear | overfit
-------------------------|--------------------------
**Doğrusal model, 2 parametre** | **Doğrusal olmayan model, 7 parametre**
Eğitim hatası = 5.3 | Eğitim hatası = 0
Doğrulama hatası = 5.1 | Doğrulama hatası = 20

* Solda, iyi bir doğru çizgi yaklaşımı görüyoruz. Parametre sayısı yeterli olduğu için model, nokta dağılımının arkasındaki mantığı doğru anlıyor.
* Sağda ise model çok güçlü. Sadece 5 nokta varken modelin 7 parametresi var, bu yüzden tüm noktalardan geçecek şekilde ayarlanabiliyor ve eğitim hatası 0 oluyor. Ancak bu, modelin verinin arkasındaki doğru deseni anlamasını engelliyor, bu yüzden doğrulama hatası çok yüksek.

Modelin karmaşıklığı (parametre sayısı) ile eğitim örneklerinin sayısı arasında doğru dengeyi kurmak çok önemlidir.

## Aşırı öğrenme neden olur?

  * Yeterli eğitim verisi olmaması
  * Çok güçlü model
  * Giriş verisinde çok fazla gürültü olması

## Aşırı öğrenme nasıl tespit edilir?

Yukarıdaki grafikten görebileceğiniz gibi, aşırı öğrenme çok düşük eğitim hatası ve yüksek doğrulama hatası ile tespit edilir. Normalde eğitim sırasında hem eğitim hem doğrulama hataları azalmaya başlar, ancak bir noktada doğrulama hatası azalmayı durdurup artmaya başlayabilir. Bu aşırı öğrenmenin işaretidir ve muhtemelen bu noktada eğitimi durdurmamız gerektiğinin göstergesidir (ya da en azından modelin bir anlık görüntüsünü almalıyız).

aşırı öğrenme

## Aşırı öğrenme nasıl önlenir?

Aşırı öğrenme olduğunu görürseniz, aşağıdakilerden birini yapabilirsiniz:

 * Eğitim verisi miktarını artırmak
 * Modelin karmaşıklığını azaltmak
 * Daha sonra ele alacağımız Dropout gibi bazı düzenleme (regularization) teknikleri kullanmak

## Aşırı öğrenme ve Bias-Variance Dengesi

Aşırı öğrenme, istatistikte Bias-Variance Dengesi olarak adlandırılan daha genel bir problemin özel bir durumudur. Modelimizdeki hata kaynaklarını düşündüğümüzde iki tür hata görürüz:

* **Bias hataları**, algoritmamızın eğitim verisi ile ilişkiyi doğru yakalayamamasından kaynaklanır. Bu, modelimizin yeterince güçlü olmamasından kaynaklanabilir (**az öğrenme, underfitting**).
* **Variance hataları**, modelin anlamlı ilişki yerine giriş verisindeki gürültüyü yakalamasından kaynaklanır (**aşırı öğrenme, overfitting**).

Eğitim sırasında bias hatası azalırken (model veriyi öğrenirken), variance hatası artar. Aşırı öğrenmeyi önlemek için eğitimi durdurmak önemlidir - ya manuel olarak (aşırı öğrenme tespit edildiğinde) ya da otomatik olarak (düzenleme teknikleri ile).

## Sonuç

Bu derste, en popüler iki yapay zeka çerçevesi olan TensorFlow ve PyTorch için farklı API türleri arasındaki farkları öğrendiniz. Ayrıca çok önemli bir konu olan aşırı öğrenme hakkında bilgi edindiniz.

## 🚀 Görev

Eşlik eden not defterlerinde, en altta 'görevler' bulacaksınız; not defterlerini inceleyip görevleri tamamlayın.

## Gözden Geçirme & Kendi Kendine Çalışma

Aşağıdaki konularda araştırma yapın:

- TensorFlow
- PyTorch
- Aşırı öğrenme

Kendinize şu soruları sorun:

- TensorFlow ve PyTorch arasındaki fark nedir?
- Aşırı öğrenme ile az öğrenme arasındaki fark nedir?

## Ödev

Bu laboratuvarda, PyTorch veya TensorFlow kullanarak tek katmanlı ve çok katmanlı tam bağlı ağlarla iki sınıflandırma problemi çözmeniz istenmektedir.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.