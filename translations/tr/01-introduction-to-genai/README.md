<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f53ba0fa49164f9323043f1c6b11f2b1",
  "translation_date": "2025-05-19T13:13:28+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "tr"
}
-->
# Üretken Yapay Zeka ve Büyük Dil Modellerine Giriş

_(Bu dersin videosunu izlemek için yukarıdaki resme tıklayın)_

Üretken yapay zeka, metin, resim ve diğer içerik türlerini üretebilen yapay zekadır. Bu teknolojiyi harika yapan şey, yapay zekayı demokratikleştirmesidir; herkes, doğal dilde yazılmış bir cümle gibi basit bir metin istemiyle kullanabilir. Java veya SQL gibi bir dil öğrenmenize gerek yok, sadece kendi dilinizi kullanarak ne istediğinizi belirtin ve yapay zeka modelinden bir öneri çıkacaktır. Bunun uygulamaları ve etkisi çok büyük; raporlar yazabilir veya anlayabilir, uygulamalar yazabilir ve daha fazlasını saniyeler içinde yapabilirsiniz.

Bu müfredatta, girişimimizin eğitim dünyasında yeni senaryoları açığa çıkarmak için üretken yapay zekayı nasıl kullandığını ve uygulamanın sosyal etkileri ve teknoloji sınırlamaları ile ilgili kaçınılmaz zorlukları nasıl ele aldığımızı inceleyeceğiz.

## Giriş

Bu derste ele alınacak konular:

- İş senaryosuna giriş: girişim fikrimiz ve misyonumuz.
- Üretken yapay zeka ve mevcut teknoloji manzarasına nasıl ulaştık.
- Büyük dil modellerinin iç işleyişi.
- Büyük Dil Modellerinin ana yetenekleri ve pratik kullanım örnekleri.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra, şunları anlayacaksınız:

- Üretken yapay zekanın ne olduğunu ve Büyük Dil Modellerinin nasıl çalıştığını.
- Eğitim senaryolarına odaklanarak, büyük dil modellerini farklı kullanım durumları için nasıl kullanabileceğinizi.

## Senaryo: eğitim girişimimiz

Üretken Yapay Zeka (AI), bir zamanlar imkansız olduğu düşünülen sınırları zorlayarak yapay zeka teknolojisinin zirvesini temsil eder. Üretken yapay zeka modellerinin birçok yeteneği ve uygulaması vardır, ancak bu müfredat için eğitimde devrim yaratmasını nasıl sağladığını kurgusal bir girişim üzerinden inceleyeceğiz. Bu girişime _bizim girişimimiz_ olarak atıfta bulunacağız. Girişimimiz, eğitim alanında, küresel ölçekte öğrenme erişimini artırma, eğitime eşit erişim sağlama ve her öğrencinin ihtiyaçlarına göre kişiselleştirilmiş öğrenme deneyimleri sunma gibi iddialı bir misyon bildirimiyle çalışıyor.

Girişim ekibimiz, bu hedefe ulaşmanın, modern zamanların en güçlü araçlarından biri olan Büyük Dil Modellerini (LLM'ler) kullanmadan mümkün olmayacağının farkında.

Üretken yapay zekanın, öğrencilerin 24 saat sanal öğretmenlere sahip olması, öğretmenlerin öğrencilerini değerlendirmek ve geri bildirim vermek için yenilikçi araçlar kullanabilmesiyle bugün öğrenme ve öğretme şeklini devrim yaratması bekleniyor.

Başlamak için, müfredat boyunca kullanacağımız bazı temel kavramları ve terminolojiyi tanımlayalım.

## Üretken yapay zekayı nasıl elde ettik?

Son zamanlarda üretken yapay zeka modellerinin duyurulmasıyla yaratılan olağanüstü _hype_ 'a rağmen, bu teknoloji 60'lı yıllara kadar uzanan araştırma çabalarıyla onlarca yıl süren bir süreçtir. Şimdi, insan bilişsel yeteneklerine sahip yapay zekanın, örneğin [OpenAI ChatGPT](https://openai.com/chatgpt) veya [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst) gibi, Bing aramalarında GPT modeli kullanan web sohbetleri gibi konuşma yetenekleriyle bir noktadayız.

Biraz geri dönersek, yapay zekanın ilk prototipleri, bir uzman grubundan alınan bilgi tabanına dayanan ve bir bilgisayara temsil edilen yazılı sohbet botlarıydı. Bilgi tabanındaki cevaplar, giriş metninde geçen anahtar kelimelerle tetiklenirdi.
Ancak, yazılı sohbet botları kullanmanın ölçeklenebilir olmadığı kısa sürede anlaşıldı.

### Yapay zekaya istatistiksel bir yaklaşım: Makine Öğrenimi

90'lı yıllarda, metin analizine istatistiksel bir yaklaşım uygulanmasıyla bir dönüm noktası geldi. Bu, veri üzerinde açıkça programlanmadan öğrenen desenler geliştiren yeni algoritmaların - makine öğrenimi olarak bilinen - geliştirilmesine yol açtı. Bu yaklaşım, makinelerin insan dilini anlama simülasyonunu mümkün kılar: bir istatistiksel model, metin-etiket eşleştirmeleri üzerinde eğitilir, böylece model, bilinmeyen giriş metnini, mesajın niyetini temsil eden önceden tanımlanmış bir etiketle sınıflandırabilir.

### Sinir ağları ve modern sanal asistanlar

Son yıllarda, daha fazla veri ve daha karmaşık hesaplamaları işleyebilen donanımın teknolojik evrimi, yapay zeka araştırmalarını teşvik ederek, sinir ağları veya derin öğrenme algoritmaları olarak bilinen gelişmiş makine öğrenimi algoritmalarının geliştirilmesine yol açtı.

Sinir ağları (özellikle Tekrarlayan Sinir Ağları – RNN'ler), doğal dil işleme alanında önemli ölçüde gelişmeler sağladı ve bir cümledeki bir kelimenin bağlamını değerlendirerek metnin anlamını daha anlamlı bir şekilde temsil etme yeteneği sağladı.

Bu, insan dilini yorumlamada çok yetenekli olan, bir ihtiyacı belirleyen ve tatmin etmek için bir eylem gerçekleştiren - önceden tanımlanmış bir senaryoyla yanıt vermek veya üçüncü taraf bir hizmeti tüketmek gibi - yeni yüzyılın ilk on yılında doğan sanal asistanları güçlendiren teknolojidir.

### Günümüz, Üretken Yapay Zeka

İşte böylece bugün Üretken Yapay Zeka'ya ulaştık, derin öğrenmenin bir alt kümesi olarak görülebilir.

Yapay zeka alanındaki on yıllarca süren araştırmalardan sonra, _Transformer_ adı verilen yeni bir model mimarisi, RNN'lerin sınırlarını aşarak, daha uzun metin dizilerini girdi olarak alabilme yeteneğine sahip oldu. Transformerlar, dikkat mekanizmasına dayanır, modelin aldığı girdilere farklı ağırlıklar vermesini sağlar, metin dizisindeki sırasına bakılmaksızın en alakalı bilgilerin yoğunlaştığı yerlere 'daha fazla dikkat' eder.

Son zamanlardaki üretken yapay zeka modellerinin çoğu – metinsel girdiler ve çıktılarla çalıştıkları için Büyük Dil Modelleri (LLM'ler) olarak da bilinir – bu mimariye dayanmaktadır. Bu modellerin ilginç olan yanı – kitaplar, makaleler ve web siteleri gibi çeşitli kaynaklardan etiketlenmemiş büyük miktarda veri üzerinde eğitilmiş – çok çeşitli görevlere uyarlanabilmeleri ve yaratıcı bir şekilde doğru dilbilgisi ile metin üretebilmeleridir. Yani, sadece bir makinenin giriş metnini 'anlama' kapasitesini olağanüstü bir şekilde artırmakla kalmadılar, aynı zamanda insan dilinde özgün bir yanıt üretme kapasitesini de sağladılar.

## Büyük dil modelleri nasıl çalışır?

Bir sonraki bölümde, farklı türde Üretken Yapay Zeka modellerini inceleyeceğiz, ancak şimdilik büyük dil modellerinin nasıl çalıştığına, OpenAI GPT (Üretken Önceden Eğitilmiş Transformer) modellerine odaklanarak bir göz atalım.

- **Tokenlaştırıcı, metni sayılara dönüştürme**: Büyük Dil Modelleri bir metni girdi olarak alır ve bir metni çıktı olarak üretir. Ancak, istatistiksel modeller olduklarından, metin dizileri yerine sayılarla daha iyi çalışırlar. Bu yüzden, modelin her girdisi, çekirdek model tarafından kullanılmadan önce bir tokenlaştırıcı tarafından işlenir. Bir token, değişken sayıda karakterden oluşan bir metin parçasıdır, bu yüzden tokenlaştırıcının ana görevi, girdiyi bir token dizisine ayırmaktır. Ardından, her token bir token indeksine, yani orijinal metin parçasının tamsayı kodlamasına eşlenir.

- **Çıktı tokenlarını tahmin etme**: n token girdi olarak verildiğinde (maksimum n modelden modele değişir), model bir tokenı çıktı olarak tahmin edebilir. Bu token, bir veya daha fazla cümle yanıtı almak için daha iyi bir kullanıcı deneyimi sağlayan genişleyen bir pencere deseninde bir sonraki iterasyonun girdisine dahil edilir. Bu, eğer ChatGPT ile oynadıysanız, bazen bir cümlenin ortasında duruyormuş gibi göründüğünü fark etmiş olabileceğinizi açıklar.

- **Seçim süreci, olasılık dağılımı**: Çıktı tokenı, mevcut metin dizisinden sonra gerçekleşme olasılığına göre model tarafından seçilir. Bu, modelin eğitimi temel alarak tüm olası 'sonraki tokenlar' üzerinde bir olasılık dağılımı tahmin etmesi nedeniyle olur. Ancak, her zaman en yüksek olasılığa sahip token, sonuçta ortaya çıkan dağılımdan seçilmez. Bu seçime bir derece rastgelelik eklenir, modelin belirleyici olmayan bir şekilde davranmasını sağlar - aynı girdi için tam olarak aynı çıktıyı almayız. Bu rastgelelik derecesi, yaratıcı düşünme sürecini simüle etmek için eklenir ve sıcaklık adı verilen bir model parametresi kullanılarak ayarlanabilir.

## Girişimimiz Büyük Dil Modellerini nasıl kullanabilir?

Artık büyük dil modellerinin iç işleyişini daha iyi anladığımıza göre, iş senaryomuza göz atarak en yaygın görevlerin bazılarını oldukça iyi gerçekleştirebilecekleri pratik örneklere bakalım.
Bir Büyük Dil Modelinin ana yeteneğinin _doğal dilde yazılmış bir metin girdisinden başlayarak sıfırdan bir metin üretmek_ olduğunu söyledik.

Peki, ne tür bir metin girişi ve çıkışı?
Bir büyük dil modelinin girişi bir istem olarak bilinirken, çıkışı bir tamamlama olarak bilinir, bu terim modelin mevcut girdi metnini tamamlamak için bir sonraki tokenı üretme mekanizmasına atıfta bulunur. Bir istemin ne olduğunu ve modelimizden en iyi şekilde yararlanmak için nasıl tasarlanacağını derinlemesine inceleyeceğiz. Ancak şimdilik, bir istemin şunları içerebileceğini söyleyelim:

- Modelden beklediğimiz çıktı türünü belirten bir **talimat**. Bu talimat bazen bazı örnekler veya ek veriler içerebilir.

  1. Bir makale, kitap, ürün incelemeleri ve daha fazlasının özeti, yapılandırılmamış verilerden içgörüler çıkarma ile birlikte.
  
  2. Bir makale, deneme, ödev veya daha fazlasının yaratıcı fikir üretimi ve tasarımı.
  
- Bir ajanla yapılan bir konuşma şeklinde sorulan bir **soru**.

- Tamamlanacak bir **metin parçası**, ki bu örtük olarak yazma yardımı istemidir.

- Belirli bir görevi gerçekleştiren bir kod parçası oluşturmasını isteyen bir yorum veya açıklama ve belgeleme isteği ile birlikte bir **kod parçası**.

Yukarıdaki örnekler oldukça basittir ve Büyük Dil Modellerinin yeteneklerinin kapsamlı bir gösterimi olarak tasarlanmamıştır. Eğitim bağlamlarıyla sınırlı olmamakla birlikte üretken yapay zekanın potansiyelini göstermeyi amaçlarlar.

Ayrıca, üretken yapay zeka modelinin çıktısı mükemmel değildir ve bazen modelin yaratıcılığı ona karşı çalışabilir, insan kullanıcının gerçekliği çarpıtma olarak yorumlayabileceği bir kelime kombinasyonu veya saldırgan bir çıktı üretebilir. Üretken yapay zeka zeki değildir - en kapsamlı zeka tanımı, eleştirel ve yaratıcı düşünme veya duygusal zekayı içeren - belirleyici değildir ve güvenilir değildir, çünkü yanlış referanslar, içerikler ve ifadeler doğru bilgilerle birleştirilip ikna edici ve güvenli bir şekilde sunulabilir. İlerleyen derslerde, bu sınırlamalarla başa çıkacağız ve onları hafifletmek için neler yapabileceğimizi göreceğiz.

## Görev

Göreviniz, [üretken yapay zeka](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) hakkında daha fazla okumak ve bugün üretken yapay zekayı eklemek isteyeceğiniz bir alanı belirlemeye çalışmaktır. "Eski yöntemle" yapmaktan farklı olarak etkisi nasıl olurdu, daha önce yapamadığınız bir şeyi yapabilir misiniz, yoksa daha mı hızlısınız? Hayalinizdeki yapay zeka girişiminin nasıl görüneceğine dair "Problem", "AI'yi Nasıl Kullanırım", "Etki" ve isteğe bağlı olarak bir iş planı gibi başlıklar içeren 300 kelimelik bir özet yazın.

Bu görevi yaptıysanız, Microsoft'un inkübatörüne, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) başvurmak için hazır olabilirsiniz. Azure, OpenAI, mentorluk ve daha fazlası için krediler sunuyoruz, göz atın!

## Bilgi Kontrolü

Büyük dil modelleri hakkında ne doğrudur?

1. Her seferinde aynı yanıtı alırsınız.
2. Her şeyi mükemmel yapar, sayı ekleme, çalışan kod üretme vb. konularda harikadır.
3. Yanıt, aynı istemi kullanmasına rağmen değişebilir. Ayrıca size bir şeyin ilk taslağını vermede harikadır, ister metin ister kod olsun. Ancak sonuçları iyileştirmeniz gerekir.

A: 3, bir LLM belirleyici değildir, yanıt değişir, ancak sıcaklık ayarı aracılığıyla değişkenliğini kontrol edebilirsiniz. Ayrıca, mükemmel şeyler yapmasını beklememelisiniz, sizin için ağır işleri yapıyor, bu genellikle üzerinde kademeli olarak iyileştirmeniz gereken bir şeyin iyi bir ilk denemesini almanız anlamına gelir.

## Harika İş! Yolculuğa Devam Et

Bu dersi tamamladıktan sonra, Üretken Yapay Zeka bilgilerinizi geliştirmek için [Üretken Yapay Zeka Öğrenme koleksiyonumuza](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) göz atın!

Farklı LLM türlerini [keşfetme ve karşılaştırma](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst) konusunu inceleyeceğimiz 2. Derse geçin!

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı AI çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.