<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-06-25T23:02:38+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "tr"
}
-->
# Sinir Ağı Çerçeveleri

Zaten öğrendiğimiz gibi, sinir ağlarını verimli bir şekilde eğitebilmek için iki şey yapmamız gerekiyor:

* Tensörler üzerinde işlem yapmak, örneğin çarpmak, toplamak ve sigmoid veya softmax gibi bazı fonksiyonları hesaplamak
* Tüm ifadelerin gradyanlarını hesaplamak, böylece gradyan inişi optimizasyonunu gerçekleştirmek

`numpy` kütüphanesi ilk kısmı yapabilse de, gradyanları hesaplayacak bir mekanizmaya ihtiyacımız var. Önceki bölümde geliştirdiğimiz çerçevede, geri yayılım yapan `backward` yönteminin içine tüm türev fonksiyonları manuel olarak programlamamız gerekiyordu. İdeal olarak, bir çerçeve, tanımlayabileceğimiz *herhangi bir ifadenin* gradyanlarını hesaplama fırsatını bize sunmalıdır.

Diğer önemli bir konu, GPU veya TPU gibi diğer özel hesaplama birimlerinde hesaplamaları gerçekleştirebilmektir. Derin sinir ağı eğitimi *çok fazla* hesaplama gerektirir ve bu hesaplamaları GPU'larda paralel hale getirebilmek çok önemlidir.

> ✅ 'Paralelize' terimi, hesaplamaları birden fazla cihaza dağıtmak anlamına gelir.

Şu anda, en popüler iki sinir çerçevesi: TensorFlow ve PyTorch'tur. Her ikisi de hem CPU hem de GPU üzerinde tensörlerle çalışmak için düşük seviyeli bir API sağlar. Düşük seviyeli API'nin üstünde, sırasıyla Keras ve PyTorch Lightning olarak adlandırılan daha yüksek seviyeli bir API de vardır.

Düşük Seviye API | TensorFlow| PyTorch
----------------|-------------------------------------|--------------------------------
Yüksek Seviye API| Keras| Pytorch

Her iki çerçevedeki **düşük seviyeli API'ler**, sözde **hesaplama grafikleri** oluşturmanıza olanak tanır. Bu grafik, verilen giriş parametreleriyle çıktının (genellikle kayıp fonksiyonu) nasıl hesaplanacağını tanımlar ve GPU üzerinde hesaplama için gönderilebilir. Bu hesaplama grafiğini farklılaştırmak ve gradyanları hesaplamak için fonksiyonlar vardır, bunlar daha sonra model parametrelerini optimize etmek için kullanılabilir.

**Yüksek seviyeli API'ler** sinir ağlarını oldukça fazla bir şekilde bir **katmanlar dizisi** olarak ele alır ve çoğu sinir ağının yapımını çok daha kolay hale getirir. Modeli eğitmek genellikle verileri hazırlamayı ve ardından işi yapmak için bir `fit` fonksiyonu çağırmayı gerektirir.

Yüksek seviyeli API, tipik sinir ağlarını birçok detayı düşünmeden çok hızlı bir şekilde oluşturmanıza olanak tanır. Aynı zamanda, düşük seviyeli API eğitim süreci üzerinde çok daha fazla kontrol sunar ve bu nedenle yeni sinir ağı mimarileri ile uğraştığınızda araştırmada çok kullanılırlar.

Ayrıca, her iki API'yi birlikte kullanabileceğinizi anlamak da önemlidir, örneğin, düşük seviyeli API kullanarak kendi ağ katmanı mimarinizi geliştirebilir ve ardından yüksek seviyeli API ile oluşturulmuş ve eğitilmiş daha büyük ağ içinde kullanabilirsiniz. Veya bir ağı, yüksek seviyeli API kullanarak bir katmanlar dizisi olarak tanımlayabilir ve ardından optimizasyonu gerçekleştirmek için kendi düşük seviyeli eğitim döngünüzü kullanabilirsiniz. Her iki API de aynı temel kavramları kullanır ve birlikte iyi çalışacak şekilde tasarlanmıştır.

## Öğrenme

Bu kursta, içeriğin çoğunu hem PyTorch hem de TensorFlow için sunuyoruz. Tercih ettiğiniz çerçeveyi seçebilir ve sadece ilgili not defterlerini inceleyebilirsiniz. Hangi çerçeveyi seçeceğinizden emin değilseniz, **PyTorch vs. TensorFlow** ile ilgili internetteki bazı tartışmaları okuyun. Daha iyi bir anlayış elde etmek için her iki çerçeveye de bakabilirsiniz.

Mümkün olduğunda, basitlik için Yüksek Seviye API'leri kullanacağız. Ancak, sinir ağlarının temelden nasıl çalıştığını anlamanın önemli olduğuna inanıyoruz, bu nedenle başlangıçta düşük seviyeli API ve tensörlerle çalışarak başlıyoruz. Ancak, hızlı bir şekilde başlamak ve bu detayları öğrenmeye çok fazla zaman harcamak istemiyorsanız, bunları atlayabilir ve doğrudan yüksek seviyeli API not defterlerine geçebilirsiniz.

## ✍️ Alıştırmalar: Çerçeveler

Aşağıdaki not defterlerinde öğrenmeye devam edin:

Düşük Seviye API | TensorFlow+Keras Not Defteri | PyTorch
-----------------|-------------------------------------|--------------------------------
Yüksek Seviye API| Keras | *PyTorch Lightning*

Çerçevelerde ustalaştıktan sonra, aşırı öğrenme kavramını gözden geçirelim.

# Aşırı Öğrenme

Aşırı öğrenme, makine öğreniminde son derece önemli bir kavramdır ve bunu doğru anlamak çok önemlidir!

Aşağıdaki 5 noktayı (aşağıdaki grafiklerde `x` ile temsil edilen) yaklaşık olarak tahmin etme problemini düşünün:

!doğrusal | aşırı öğrenme
-------------------------|--------------------------
**Doğrusal model, 2 parametre** | **Doğrusal olmayan model, 7 parametre**
Eğitim hatası = 5.3 | Eğitim hatası = 0
Doğrulama hatası = 5.1 | Doğrulama hatası = 20

* Solda, iyi bir doğru çizgisi yaklaştırması görüyoruz. Parametre sayısı uygun olduğu için model, nokta dağılımının arkasındaki fikri doğru alıyor.
* Sağda, model çok güçlü. Sadece 5 noktamız olduğu ve modelin 7 parametresi olduğu için, model tüm noktalardan geçecek şekilde ayarlanabilir ve eğitim hatasını 0 yapabilir. Ancak, bu modelin verilerin arkasındaki doğru deseni anlamasını engeller, bu nedenle doğrulama hatası çok yüksektir.

Modelin zenginliği (parametre sayısı) ile eğitim örneklerinin sayısı arasında doğru dengeyi kurmak çok önemlidir.

## Neden aşırı öğrenme olur

  * Yeterli eğitim verisi yok
  * Çok güçlü model
  * Giriş verilerinde çok fazla gürültü

## Aşırı öğrenme nasıl tespit edilir

Yukarıdaki grafikten görebileceğiniz gibi, aşırı öğrenme, çok düşük bir eğitim hatası ve yüksek bir doğrulama hatası ile tespit edilebilir. Genellikle eğitim sırasında hem eğitim hem de doğrulama hatalarının azalmaya başladığını göreceğiz ve ardından bir noktada doğrulama hatası azalmayı durdurabilir ve yükselmeye başlayabilir. Bu, aşırı öğrenmenin bir işareti olacak ve muhtemelen bu noktada eğitimi durdurmamız gerektiğinin göstergesi olacak (veya en azından modelin bir anlık görüntüsünü alacağız).

aşırı öğrenme

## Aşırı öğrenme nasıl önlenir

Aşırı öğrenmenin meydana geldiğini görüyorsanız, aşağıdakilerden birini yapabilirsiniz:

 * Eğitim verilerinin miktarını artırın
 * Modelin karmaşıklığını azaltın
 * Daha sonra ele alacağımız Dropout gibi bazı düzenleme tekniklerini kullanın.

## Aşırı Öğrenme ve Yanlılık-Çeşitlilik Dengesi

Aşırı öğrenme aslında istatistiklerde Yanlılık-Çeşitlilik Dengesi olarak adlandırılan daha genel bir problemin bir örneğidir. Modelimizdeki olası hata kaynaklarını düşünürsek, iki tür hata görebiliriz:

* **Yanlılık hataları**, algoritmamızın eğitim verileri arasındaki ilişkiyi doğru bir şekilde yakalayamamasından kaynaklanır. Bu, modelimizin yeterince güçlü olmamasından kaynaklanabilir (**yetersiz öğrenme**).
* **Çeşitlilik hataları**, modelin girdi verilerindeki gürültüyü anlamlı bir ilişki yerine yaklaşık olarak alması nedeniyle ortaya çıkar (**aşırı öğrenme**).

Eğitim sırasında, yanlılık hatası azalır (modelimiz verileri tahmin etmeyi öğrendikçe) ve çeşitlilik hatası artar. Aşırı öğrenmeyi önlemek için eğitimi durdurmak önemlidir - ya manuel olarak (aşırı öğrenmeyi tespit ettiğimizde) ya da otomatik olarak (düzenleme getirerek).

## Sonuç

Bu derste, en popüler iki AI çerçevesi, TensorFlow ve PyTorch için çeşitli API'ler arasındaki farkları öğrendiniz. Ayrıca, çok önemli bir konu olan aşırı öğrenmeyi öğrendiniz.

## 🚀 Meydan Okuma

Eşlik eden not defterlerinde, alt kısımda 'görevler' bulacaksınız; not defterlerini inceleyin ve görevleri tamamlayın.

## Gözden Geçirme ve Kendi Kendine Çalışma

Aşağıdaki konular hakkında biraz araştırma yapın:

- TensorFlow
- PyTorch
- Aşırı öğrenme

Kendinize şu soruları sorun:

- TensorFlow ve PyTorch arasındaki fark nedir?
- Aşırı öğrenme ve yetersiz öğrenme arasındaki fark nedir?

## Ödev

Bu laboratuvarda, PyTorch veya TensorFlow kullanarak tek ve çok katmanlı tam bağlantılı ağlar kullanarak iki sınıflandırma problemini çözmeniz isteniyor.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda ortaya çıkabilecek yanlış anlaşılmalardan veya yanlış yorumlamalardan sorumlu değiliz.