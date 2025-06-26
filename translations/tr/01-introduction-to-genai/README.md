<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-06-25T09:52:14+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "tr"
}
-->
# Üretken Yapay Zeka ve Büyük Dil Modellerine Giriş

_(Bu dersin videosunu izlemek için yukarıdaki resme tıklayın)_

Üretken Yapay Zeka, metin, resim ve diğer içerik türlerini üretebilen bir yapay zekadır. Bu teknolojiyi harika yapan şey, yapay zekayı demokratikleştirmesidir; herkes yalnızca doğal bir dilde yazılmış bir cümle kadar basit bir metin girdisiyle bunu kullanabilir. Java veya SQL gibi bir dil öğrenmenize gerek yok, ihtiyacınız olan tek şey kendi dilinizi kullanarak ne istediğinizi belirtmek ve bir yapay zeka modelinden bir öneri almak. Bunun uygulamaları ve etkisi büyüktür; raporlar yazabilir veya anlayabilir, uygulamalar yazabilir ve daha fazlasını saniyeler içinde yapabilirsiniz.

Bu müfredatta, girişimimizin eğitim dünyasında yeni senaryoları açığa çıkarmak için üretken yapay zekayı nasıl kullandığını ve uygulamanın sosyal etkileri ve teknoloji sınırlamalarıyla ilgili kaçınılmaz zorlukları nasıl ele aldığımızı inceleyeceğiz.

## Giriş

Bu derste ele alınacak konular:

- İş senaryosuna giriş: girişim fikrimiz ve misyonumuz.
- Üretken yapay zeka ve mevcut teknoloji manzarasına nasıl ulaştığımız.
- Büyük dil modelinin iç işleyişi.
- Büyük Dil Modellerinin ana yetenekleri ve pratik kullanım durumları.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra, şunları anlayacaksınız:

- Üretken yapay zekanın ne olduğunu ve Büyük Dil Modellerinin nasıl çalıştığını.
- Farklı kullanım durumları için büyük dil modellerinden nasıl yararlanabileceğinizi, özellikle eğitim senaryolarına odaklanarak.

## Senaryo: eğitim girişimimiz

Üretken Yapay Zeka (AI), bir zamanlar imkansız olduğu düşünülen sınırları zorlayan yapay zeka teknolojisinin zirvesini temsil eder. Üretken yapay zeka modellerinin çeşitli yetenekleri ve uygulamaları vardır, ancak bu müfredat için kurgusal bir girişim aracılığıyla eğitimi nasıl devrim niteliğinde değiştirdiğini inceleyeceğiz. Bu girişime _bizim girişimimiz_ olarak atıfta bulunacağız. Girişimimiz, eğitim alanında faaliyet gösterir ve iddialı misyon bildirgesi şudur:

> _öğrenimde erişilebilirliği küresel ölçekte artırmak, eğitimde eşit erişimi sağlamak ve her öğrenciye ihtiyaçlarına göre kişiselleştirilmiş öğrenme deneyimleri sunmak_.

Girişim ekibimiz, bu hedefe modern zamanların en güçlü araçlarından biri olan Büyük Dil Modelleri (LLM'ler) olmadan ulaşamayacağımızın farkındadır.

Üretken yapay zekanın, öğrencilerin 24 saat sanal öğretmenlere sahip olması, öğretmenlerin ise öğrencilerini değerlendirmek ve geri bildirim vermek için yenilikçi araçlardan yararlanabilmesiyle, bugün öğrenme ve öğretme şeklini devrim niteliğinde değiştirmesi bekleniyor.

Başlamak için, müfredat boyunca kullanacağımız bazı temel kavramları ve terminolojiyi tanımlayalım.

## Üretken Yapay Zekaya nasıl ulaştık?

Son zamanlarda üretken yapay zeka modellerinin duyurulmasıyla yaratılan olağanüstü _hype_'a rağmen, bu teknoloji onlarca yıl süren bir çalışmanın ürünüdür ve ilk araştırma çabaları 60'lara kadar uzanmaktadır. Şu anda, insan bilişsel yeteneklerine sahip bir yapay zeka noktasındayız, örneğin [OpenAI ChatGPT](https://openai.com/chatgpt) veya [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst) gibi, Bing aramaları için GPT modelini kullanan sohbetler.

Biraz geriye gidersek, yapay zekanın ilk prototipleri, bir uzman grubundan çıkarılan bilgi tabanına dayanan daktilo yazılı sohbet robotlarıydı. Bilgi tabanındaki cevaplar, giriş metninde görünen anahtar kelimelerle tetiklenirdi. Ancak, bu yaklaşımın, daktilo yazılı sohbet robotlarını kullanmanın, iyi ölçeklenmediği kısa sürede anlaşıldı.

### Yapay Zekaya İstatistiksel Bir Yaklaşım: Makine Öğrenimi

90'lar sırasında metin analizine istatistiksel bir yaklaşım uygulanmasıyla bir dönüm noktası geldi. Bu, verilerden açıkça programlanmadan öğrenme desenleri yapabilen yeni algoritmaların – makine öğrenimi olarak bilinen – geliştirilmesine yol açtı. Bu yaklaşım, makinelerin insan dilini anlama simülasyonu yapmasına olanak tanır: bir istatistiksel model, metin-etiket eşleşmeleri üzerinde eğitilir ve bu, modelin bilinmeyen giriş metnini, mesajın amacını temsil eden önceden tanımlanmış bir etiketle sınıflandırmasını sağlar.

### Sinir ağları ve modern sanal asistanlar

Son yıllarda, daha büyük veri miktarlarını ve daha karmaşık hesaplamaları işleyebilen donanımın teknolojik evrimi, yapay zeka araştırmalarını teşvik etti ve sinir ağları veya derin öğrenme algoritmaları olarak bilinen gelişmiş makine öğrenimi algoritmalarının geliştirilmesine yol açtı.

Sinir ağları (özellikle Tekrarlayan Sinir Ağları – RNN'ler), doğal dil işleme alanında önemli gelişmeler sağladı ve bir cümledeki bir kelimenin bağlamını değerlendirerek metnin anlamını daha anlamlı bir şekilde temsil etme yeteneğini kazandı.

Bu teknoloji, yeni yüzyılın ilk on yılında doğan sanal asistanları güçlendirdi ve insan dilini yorumlama, bir ihtiyacı tanımlama ve bunu karşılamak için bir eylem gerçekleştirme konusunda oldukça yetenekli hale getirdi – örneğin, önceden tanımlanmış bir senaryo ile yanıt verme veya üçüncü taraf bir hizmeti tüketme gibi.

### Günümüzde, Üretken Yapay Zeka

İşte böylece bugün Üretken Yapay Zekaya geldik, bu da derin öğrenmenin bir alt kümesi olarak görülebilir.

Yapay zeka alanında onlarca yıllık araştırmadan sonra, _Transformer_ adı verilen yeni bir model mimarisi, RNN'lerin sınırlarını aşarak çok daha uzun metin dizilerini girdi olarak alabilen bir yapı oluşturdu. Transformerlar, aldıkları girdilere farklı ağırlıklar vererek, metin dizisindeki sıralarına bakılmaksızın en alakalı bilgilerin yoğunlaştığı yerlere 'daha fazla dikkat' etmelerini sağlayan dikkat mekanizmasına dayanır.

Son zamanlardaki üretken yapay zeka modellerinin çoğu – aynı zamanda Büyük Dil Modelleri (LLM'ler) olarak da bilinir, çünkü metin girdileri ve çıktıları ile çalışırlar – gerçekten bu mimariye dayanır. Bu modellerin ilginç yanı – kitaplar, makaleler ve web siteleri gibi çeşitli kaynaklardan büyük miktarda etiketlenmemiş veriler üzerinde eğitilmiş olmalarıdır – çeşitli görevlere uyarlanabilmeleri ve yaratıcı bir benzerlikle dilbilgisi açısından doğru metin üretebilmeleridir. Yani, sadece bir makinenin bir giriş metnini 'anlama' kapasitesini inanılmaz bir şekilde artırmakla kalmadılar, aynı zamanda insan dilinde orijinal bir yanıt oluşturma kapasitelerini de sağladılar.

## Büyük dil modelleri nasıl çalışır?

Bir sonraki bölümde farklı türlerde Üretken Yapay Zeka modellerini inceleyeceğiz, ancak şimdilik büyük dil modellerinin nasıl çalıştığına bir göz atalım, özellikle OpenAI GPT (Üretken Ön Eğitimli Transformer) modellerine odaklanarak.

- **Tokenizasyon, metinden sayılara**: Büyük Dil Modelleri bir metni giriş olarak alır ve bir metni çıktı olarak üretir. Ancak, istatistiksel modeller oldukları için, metin dizilerinden çok sayılarla daha iyi çalışırlar. Bu nedenle, modelin her girişi, çekirdek model tarafından kullanılmadan önce bir tokenizatör tarafından işlenir. Bir token, değişken sayıda karakterden oluşan bir metin parçasıdır, bu yüzden tokenizatörün ana görevi, girişi bir dizi tokene ayırmaktır. Daha sonra, her token bir token indeksine eşlenir, bu da orijinal metin parçasının tamsayı kodlamasıdır.

- **Çıktı tokenlarını tahmin etme**: n tokenı giriş olarak verildiğinde (maksimum n modelden modele değişir), model bir tokenı çıktı olarak tahmin edebilir. Bu token daha sonra, bir (veya birden fazla) cümle olarak bir yanıt almanın daha iyi bir kullanıcı deneyimini sağlayan genişleyen bir pencere deseni içinde bir sonraki yinelemenin girdisine dahil edilir. Bu, eğer ChatGPT ile oynadıysanız, bazen bir cümlenin ortasında duruyor gibi göründüğünü fark etmiş olabileceğinizi açıklar.

- **Seçim süreci, olasılık dağılımı**: Çıktı tokenı, mevcut metin dizisinden sonra ortaya çıkma olasılığına göre model tarafından seçilir. Bunun nedeni, modelin, eğitimi temel alınarak hesaplanan tüm olası 'sonraki tokenlar' üzerinde bir olasılık dağılımı tahmin etmesidir. Ancak, her zaman en yüksek olasılığa sahip token seçilmez. Bu seçime bir derece rastgelelik eklenir, bu şekilde model deterministik olmayan bir şekilde hareket eder - aynı giriş için tam olarak aynı çıktıyı almayız. Bu rastgelelik derecesi, yaratıcı düşünme sürecini simüle etmek için eklenir ve sıcaklık adı verilen bir model parametresi kullanılarak ayarlanabilir.

## Girişimimiz Büyük Dil Modellerinden nasıl yararlanabilir?

Artık büyük dil modelinin iç işleyişini daha iyi anladığımıza göre, iş senaryomuza odaklanarak, en yaygın görevlerin bazı pratik örneklerini görelim.
Büyük Dil Modelinin ana yeteneğinin _doğal dilde yazılmış bir metin girdisinden başlayarak sıfırdan bir metin üretmek_ olduğunu söyledik.

Ama ne tür bir metin girdisi ve çıktısı?
Büyük dil modelinin girdisi bir prompt olarak bilinirken, çıktısı bir tamamlama olarak bilinir; bu, modelin mevcut girişi tamamlamak için bir sonraki tokenı üretme mekanizmasına atıfta bulunur. Bir promptun ne olduğunu ve modelimizden en iyi şekilde yararlanmak için nasıl tasarlanacağını derinlemesine inceleyeceğiz. Ancak şimdilik, bir promptun şunları içerebileceğini söyleyelim:

- Modelden beklediğimiz çıktı türünü belirten bir **talimat**. Bu talimat bazen bazı örnekler veya ek veriler içerebilir.

  1. Bir makale, kitap, ürün incelemeleri ve daha fazlasının özetlenmesi ve yapılandırılmamış verilerden içgörülerin çıkarılması.

  2. Bir makale, bir deneme, bir ödev veya daha fazlasının yaratıcı tasarımı ve ideasyonu.

- Bir temsilci ile bir konuşma şeklinde sorulan bir **soru**.

- Yazma yardımı için dolaylı bir talep olan **tamamlanacak bir metin parçası**.

- Belirli bir görevi yerine getiren bir kod parçası oluşturulması talebi veya açıklanması ve belgelenmesi istenen bir **kod parçası**.

Yukarıdaki örnekler oldukça basittir ve Büyük Dil Modellerinin yeteneklerinin kapsamlı bir gösterimi olarak tasarlanmamıştır. Eğitim bağlamlarıyla sınırlı olmamakla birlikte, üretken yapay zekayı kullanmanın potansiyelini göstermeyi amaçlarlar.

Ayrıca, bir üretken yapay zeka modelinin çıktısı mükemmel değildir ve bazen modelin yaratıcılığı ona karşı çalışabilir, insan kullanıcı tarafından gerçekliğin çarpıtılması olarak yorumlanabilecek veya saldırgan olabilecek bir çıktı oluşturabilir. Üretken yapay zeka zeki değildir - en azından zekanın daha kapsamlı tanımında, eleştirel ve yaratıcı akıl yürütme veya duygusal zekayı içeren; deterministik değildir ve güvenilir değildir, çünkü yanlış referanslar, içerikler ve ifadeler doğru bilgilerle birleşip ikna edici ve güven verici bir şekilde sunulabilir. Sonraki derslerde, bu sınırlamalarla başa çıkacağız ve bunları hafifletmek için neler yapabileceğimizi göreceğiz.

## Görev

Göreviniz, [üretken yapay zeka](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) hakkında daha fazla okumak ve bugün üretken yapay zekayı ekleyeceğiniz bir alan belirlemeye çalışmak. Etki, "eski yöntemle" yapmaktan nasıl farklı olur, daha önce yapamayacağınız bir şeyi yapabilir misiniz veya daha hızlı mısınız? Hayalinizdeki yapay zeka girişiminin nasıl görüneceğini 300 kelimelik bir özet olarak yazın ve "Sorun", "Yapay Zekayı Nasıl Kullanırdım", "Etkisi" ve isteğe bağlı olarak bir iş planı gibi başlıklar ekleyin.

Bu görevi yaptıysanız, Microsoft'un kuluçka programına, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst)'a başvurmaya hazır olabilirsiniz; Azure, OpenAI, mentorluk ve çok daha fazlası için kredi sunuyoruz, bir göz atın!

## Bilgi Kontrolü

Büyük dil modelleri hakkında ne doğrudur?

1. Her seferinde tam olarak aynı yanıtı alırsınız.
1. Her şeyi mükemmel yapar, sayıları toplamada harikadır, çalışan kod üretir vb.
1. Yanıt, aynı prompt kullanılsa bile değişebilir. Ayrıca size bir şeyin ilk taslağını verir, ister metin ister kod olsun. Ancak sonuçları iyileştirmeniz gerekir.

C: 3, bir LLM deterministik değildir, yanıt değişir, ancak varyansını bir sıcaklık ayarı ile kontrol edebilirsiniz. Ayrıca, her şeyi mükemmel yapmasını beklememelisiniz, sizin için ağır işleri yapmak için burada, bu genellikle bir şeyi yavaş yavaş iyileştirmeniz gereken iyi bir ilk deneme elde ettiğiniz anlamına gelir.

## Harika İş! Yolculuğa Devam Edin

Bu dersi tamamladıktan sonra, Üretken Yapay Zeka bilginizi artırmaya devam etmek için [Üretken Yapay Zeka Öğrenme koleksiyonumuzu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) inceleyin!

Farklı LLM türlerini nasıl keşfedeceğimizi ve karşılaştıracağımızı inceleyeceğimiz 2. Derse geçin!

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için, profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.