<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-05-20T01:58:17+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "tr"
}
-->
# Sinir Ağı Çerçeveleri

Daha önce öğrendiğimiz gibi, sinir ağlarını verimli bir şekilde eğitebilmek için iki şey yapmamız gerekiyor:

* Tensörler üzerinde işlem yapmak, örneğin çarpma, toplama ve sigmoid veya softmax gibi bazı fonksiyonları hesaplamak
* Tüm ifadelerin gradyanlarını hesaplamak, böylece gradyan iniş optimizasyonu gerçekleştirebilmek

`numpy` kütüphanesi ilk kısmı yapabilirken, gradyanları hesaplamak için bir mekanizmaya ihtiyacımız var. Önceki bölümde geliştirdiğimiz çerçevede, `backward` metodunun içinde tüm türev fonksiyonları manuel olarak programlamamız gerekiyordu, bu yöntem geri yayılım yapar. İdeal olarak, bir çerçeve bize tanımlayabileceğimiz *herhangi bir ifadenin* gradyanlarını hesaplama fırsatı vermelidir.

Başka bir önemli nokta, GPU veya TPU gibi özel hesaplama birimleri üzerinde hesaplamalar yapabilmektir. Derin sinir ağı eğitimi *çok fazla* hesaplama gerektirir ve bu hesaplamaları GPU'larda paralelleştirebilmek çok önemlidir.

> ✅ 'Paralelleştirme' terimi, hesaplamaları birden fazla cihaz üzerinde dağıtmak anlamına gelir.

Şu anda en popüler iki sinir çerçevesi: TensorFlow ve PyTorch. Her ikisi de hem CPU hem de GPU üzerinde tensörlerle çalışmak için düşük seviyeli bir API sağlar. Düşük seviyeli API'nin üzerinde, sırasıyla Keras ve PyTorch Lightning olarak adlandırılan daha yüksek seviyeli bir API bulunmaktadır.

Düşük Seviyeli API | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
Yüksek Seviyeli API| Keras| Pytorch

Her iki çerçevedeki **düşük seviyeli API'ler** size **hesaplama grafikleri** oluşturma imkanı tanır. Bu grafik, verilen giriş parametreleriyle çıktının (genellikle kayıp fonksiyonu) nasıl hesaplanacağını tanımlar ve eğer varsa GPU'da hesaplama için gönderilebilir. Bu hesaplama grafiğini farklılaştırmak ve gradyanları hesaplamak için fonksiyonlar vardır, bunlar daha sonra model parametrelerini optimize etmek için kullanılabilir.

**Yüksek seviyeli API'ler**, sinir ağlarını genellikle **katmanlar dizisi** olarak ele alır ve çoğu sinir ağını oluşturmayı çok daha kolay hale getirir. Modeli eğitmek genellikle veriyi hazırlamayı ve ardından işi yapmak için `fit` fonksiyonunu çağırmayı gerektirir.

Yüksek seviyeli API, tipik sinir ağlarını çok hızlı bir şekilde oluşturmanıza olanak tanır, birçok detayla uğraşmanıza gerek kalmaz. Aynı zamanda, düşük seviyeli API, eğitim süreci üzerinde çok daha fazla kontrol sağlar ve bu nedenle yeni sinir ağı mimarileriyle uğraşırken araştırmada çokça kullanılır.

Her iki API'yi birlikte kullanabileceğinizi anlamak da önemlidir, örneğin kendi ağ katmanı mimarinizi düşük seviyeli API kullanarak geliştirebilir ve ardından yüksek seviyeli API ile oluşturulan ve eğitilen daha büyük bir ağ içinde kullanabilirsiniz. Ya da yüksek seviyeli API kullanarak bir katman dizisi olarak bir ağ tanımlayabilir ve ardından optimizasyon yapmak için kendi düşük seviyeli eğitim döngünüzü kullanabilirsiniz. Her iki API de aynı temel kavramları kullanır ve birlikte iyi çalışacak şekilde tasarlanmıştır.

## Öğrenme

Bu derste, PyTorch ve TensorFlow için çoğu içeriği sunuyoruz. Tercih ettiğiniz çerçeveyi seçebilir ve yalnızca ilgili defterleri inceleyebilirsiniz. Hangi çerçeveyi seçeceğinizden emin değilseniz, **PyTorch vs. TensorFlow** ile ilgili internetteki bazı tartışmaları okuyun. Daha iyi bir anlayış kazanmak için her iki çerçeveye de göz atabilirsiniz.

Mümkün olduğunda, basitlik için Yüksek Seviyeli API'leri kullanacağız. Ancak, sinir ağlarının temelden nasıl çalıştığını anlamanın önemli olduğunu düşünüyoruz, bu nedenle başlangıçta düşük seviyeli API ve tensörlerle çalışarak başlıyoruz. Ancak, hızlı bir şekilde ilerlemek ve bu detayları öğrenmek için fazla zaman harcamak istemiyorsanız, bunları atlayabilir ve doğrudan yüksek seviyeli API defterlerine geçebilirsiniz.

## ✍️ Egzersizler: Çerçeveler

Öğrenmenizi aşağıdaki defterlerde devam ettirin:

Düşük Seviyeli API | TensorFlow+Keras Defteri | PyTorch
--------------|-------------------------------------|--------------------------------
Yüksek Seviyeli API| Keras | *PyTorch Lightning*

Çerçeveleri ustalıkla öğrendikten sonra, aşırı uyum kavramını tekrar gözden geçirelim.

# Aşırı Uyum

Aşırı uyum, makine öğreniminde son derece önemli bir kavramdır ve doğru anlamak çok önemlidir!

Aşağıdaki 5 noktayı (grafiklerde `x` ile temsil edilen) yaklaşık olarak belirleme sorununu düşünün:

!doğrusal | aşırı uyum
-------------------------|--------------------------
**Doğrusal model, 2 parametre** | **Doğrusal olmayan model, 7 parametre**
Eğitim hatası = 5.3 | Eğitim hatası = 0
Doğrulama hatası = 5.1 | Doğrulama hatası = 20

* Solda, iyi bir doğru çizgisi yaklaşımı görüyoruz. Parametre sayısı uygun olduğu için model, nokta dağılımının arkasındaki fikri doğru anlıyor.
* Sağda, model çok güçlü. Sadece 5 noktamız var ve modelin 7 parametresi olduğu için, tüm noktalardan geçecek şekilde ayarlanabiliyor, böylece eğitim hatası 0 oluyor. Ancak, bu modelin verilerin arkasındaki doğru modeli anlamasını engelliyor, bu nedenle doğrulama hatası çok yüksek.

Modelin zenginliği (parametre sayısı) ile eğitim örnekleri sayısı arasında doğru dengeyi kurmak çok önemlidir.

## Aşırı Uyum Neden Oluşur?

  * Yeterli eğitim verisi yok
  * Çok güçlü model
  * Giriş verilerinde çok fazla gürültü

## Aşırı Uyumu Nasıl Tespit Edilir?

Yukarıdaki grafikten görebileceğiniz gibi, aşırı uyum çok düşük eğitim hatası ve yüksek doğrulama hatası ile tespit edilebilir. Normalde eğitim sırasında hem eğitim hem de doğrulama hatalarının azalmaya başladığını görürüz ve sonra bir noktada doğrulama hatası azalmayı durdurabilir ve yükselmeye başlayabilir. Bu aşırı uyumun bir işareti olacak ve bu noktada eğitimi durdurmamız gerektiğinin bir göstergesi olacak (veya en azından modelin bir anlık görüntüsünü almamız gerektiği).

## Aşırı Uyumu Nasıl Önleyebiliriz?

Aşırı uyumun meydana geldiğini görüyorsanız, aşağıdakilerden birini yapabilirsiniz:

 * Eğitim verilerinin miktarını artırın
 * Modelin karmaşıklığını azaltın
 * Daha sonra ele alacağımız Dropout gibi bir düzenleme tekniği kullanın.

## Aşırı Uyum ve Yanlılık-Çeşitlilik Dengesi

Aşırı uyum, aslında istatistiklerde Yanlılık-Çeşitlilik Dengesi olarak adlandırılan daha genel bir problemin bir örneğidir. Modelimizdeki olası hata kaynaklarını düşünürsek, iki tür hata görebiliriz:

* **Yanlılık hataları**, algoritmamızın eğitim verileri arasındaki ilişkiyi doğru bir şekilde yakalayamamasından kaynaklanır. Modelimizin yeterince güçlü olmamasından kaynaklanabilir (**eksik uyum**).
* **Çeşitlilik hataları**, modelin giriş verilerindeki gürültüyü anlamlı ilişki yerine yakalamaya çalışmasından kaynaklanır (**aşırı uyum**).

Eğitim sırasında, yanlılık hatası azalır (modelimiz verileri yaklaşık olarak öğrenirken) ve çeşitlilik hatası artar. Aşırı uyumu önlemek için eğitimi durdurmak - ya manuel olarak (aşırı uyumu tespit ettiğimizde) ya da otomatik olarak (düzenleme getirerek) - önemlidir.

## Sonuç

Bu derste, en popüler iki AI çerçevesi olan TensorFlow ve PyTorch için çeşitli API'ler arasındaki farkları öğrendiniz. Ayrıca, çok önemli bir konu olan aşırı uyumu öğrendiniz.

## 🚀 Meydan Okuma

İlgili defterlerde, 'görevler' bölümünde bulacağınız görevleri tamamlayın; defterleri inceleyin ve görevleri tamamlayın.

## İnceleme ve Kendi Kendine Çalışma

Aşağıdaki konular hakkında biraz araştırma yapın:

- TensorFlow
- PyTorch
- Aşırı Uyum

Kendinize şu soruları sorun:

- TensorFlow ve PyTorch arasındaki fark nedir?
- Aşırı uyum ve eksik uyum arasındaki fark nedir?

## Ödev

Bu laboratuvarda, PyTorch veya TensorFlow kullanarak tek ve çok katmanlı tam bağlantılı ağlar kullanarak iki sınıflandırma problemini çözmeniz isteniyor.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.