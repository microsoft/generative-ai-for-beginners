# Generatif Yapay Zeka ve Büyük Dil Modellerine Giriş

[![Generatif Yapay Zeka ve Büyük Dil Modellerine Giriş](../../images/01-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson-1-gh?WT.mc_id=academic-105485-koreyst)

_(Bu dersin videosunu izlemek için yukarıdaki görsele tıklayın)_

Generatif Yapay Zeka, metin, görseller ve diğer içerik türlerini üretebilen yapay zekadır. Bu teknolojiyi harika kılan şey, yapay zekayı demokratikleştirmesidir; herkes yalnızca doğal bir dilde yazılmış bir metin istemiyle kullanabilir. Bir şeyler başarmak için Java veya SQL gibi bir programlama dili öğrenmenize gerek yoktur. Kendi dilinizi kullanarak ne istediğinizi belirtirsiniz ve bir yapay zeka modeli size öneriler sunar. Bunun uygulamaları ve etkisi büyüktür; raporları anlayabilir, uygulamalar yazabilir ve daha fazlasını saniyeler içinde gerçekleştirebilirsiniz.

Bu eğitim programında, girişimimizin eğitim dünyasında yeni senaryoları nasıl açığa çıkarmak için generatif yapay zekayı kullandığını ve bu teknolojinin sosyal etkileri ile sınırlamalarını nasıl ele aldığımızı keşfedeceğiz.

## Giriş

Bu ders şunları kapsayacaktır:

- İş senaryosuna giriş: girişim fikrimiz ve misyonumuz.
- Generatif yapay zeka ve mevcut teknoloji manzarasına nasıl ulaştığımız.
- Büyük Dil Modellerinin (LLM) iç yapısı.
- Büyük Dil Modellerinin başlıca yetenekleri ve pratik kullanım alanları.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları anlayacaksınız:

- Generatif yapay zekanın ne olduğu ve Büyük Dil Modellerinin nasıl çalıştığı.
- Büyük Dil Modellerini farklı kullanım senaryolarında, özellikle eğitim odaklı nasıl kullanabileceğiniz.

## Senaryo: Eğitim Girişimimiz

Generatif Yapay Zeka (AI), yapay zeka teknolojisinin zirvesini temsil eder ve bir zamanlar imkansız görülen şeylerin sınırlarını zorlar. Generatif yapay zeka modellerinin birçok yeteneği ve uygulaması vardır, ancak bu eğitim programı kapsamında bunun eğitimi nasıl devrim niteliğinde dönüştürdüğünü keşfedeceğiz.

Kurgusal girişimimiz olan _bizim girişimimiz_, eğitim alanında faaliyet gösteriyor ve şu iddialı misyonu benimsemiştir:

> _Öğrenimde erişilebilirliği küresel ölçekte iyileştirmek, eğitimde eşitliği sağlamak ve her öğrencinin ihtiyaçlarına göre kişiselleştirilmiş öğrenme deneyimleri sunmak._

Bu hedefe ulaşmanın en güçlü yollarından birinin Büyük Dil Modelleri (LLM) olduğunu biliyoruz.

Generatif yapay zekanın eğitimde devrim yaratması beklenmektedir. Öğrenciler, 7/24 sanal öğretmenler aracılığıyla geniş bilgi ve örnekler alırken, öğretmenler öğrencilerini değerlendirmek ve geri bildirim sağlamak için yenilikçi araçlardan faydalanabilirler.

![Monitöre bakan beş genç öğrenci - DALLE2 ile oluşturuldu](../../images/students-by-DALLE2.png?WT.mc_id=academic-105485-koreyst)

Başlangıç olarak, müfredat boyunca kullanacağımız bazı temel kavramları ve terminolojiyi tanımlayalım.

## Generatif Yapay Zeka Nasıl Ortaya Çıktı?

Son zamanlarda üretken YZ modellerinin duyurulmasıyla yaratılan olağanüstü _hype_'a rağmen, bu teknoloji onlarca yıllık bir geçmişe sahiptir ve ilk araştırma çabaları 60'lı yıllara kadar uzanmaktadır. Şu anda, örneğin [OpenAI ChatGPT](https://openai.com/chatgpt) veya web araması Bing konuşmaları için bir GPT modeli kullanan [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst) tarafından gösterildiği gibi, konuşma gibi insan bilişsel yeteneklerine sahip YZ ile bir noktadayız.

Biraz geriye gidersek, yapay zekanın ilk prototipleri, bir grup uzmandan elde edilen ve bir bilgisayarda temsil edilen bir bilgi tabanına dayanan, daktiloyla yazılmış sohbet robotlarından oluşuyordu. Bilgi tabanındaki yanıtlar, girdi metninde görünen anahtar kelimeler tarafından tetikleniyordu.
Ancak, kısa süre sonra daktiloyla yazılmış sohbet robotları kullanan böyle bir yaklaşımın iyi ölçeklenmediği anlaşıldı.

### Yapay zekaya istatistiksel bir yaklaşım: Makine Öğrenimi

90'lı yıllarda metin analizine istatistiksel bir yaklaşımın uygulanmasıyla bir dönüm noktası yaşandı. Bu, makine öğrenimi olarak bilinen ve açıkça programlanmadan verilerden kalıplar öğrenebilen yeni algoritmaların geliştirilmesine yol açtı. Bu yaklaşım, makinelerin insan dilini anlamayı simüle etmesine olanak tanır: metin-etiket eşleştirmeleri üzerinde istatistiksel bir model eğitilir ve modelin bilinmeyen girdi metnini, mesajın amacını temsil eden önceden tanımlanmış bir etiketle sınıflandırmasını sağlar.

### Sinir ağları ve modern sanal asistanlar

Son yıllarda, daha büyük miktarda veriyi ve daha karmaşık hesaplamaları işleyebilen donanımın teknolojik gelişimi, yapay zeka alanındaki araştırmaları teşvik ederek sinir ağları veya derin öğrenme algoritmaları olarak bilinen gelişmiş makine öğrenimi algoritmalarının geliştirilmesine yol açmıştır.

Sinir ağları (ve özellikle Tekrarlayan Sinir Ağları - RNN'ler) doğal dil işlemeyi önemli ölçüde geliştirerek metnin anlamının daha anlamlı bir şekilde temsil edilmesini sağladı ve bir cümledeki bir kelimenin bağlamına değer verdi.

Bu, yeni yüzyılın ilk on yılında doğan, insan dilini yorumlama, bir ihtiyacı belirleme ve bunu karşılamak için bir eylem gerçekleştirme konusunda çok yetkin olan sanal asistanlara güç veren teknolojidir - önceden tanımlanmış bir komut dosyası ile cevap vermek veya 3. taraf bir hizmeti kullanmak gibi.

### Günümüz, Üretken Yapay Zeka

İşte bugün derin öğrenmenin bir alt kümesi olarak görülebilecek Üretken Yapay Zekaya böyle ulaştık.

![AI, ML, DL ve Generative AI](../../images/AI-diagram.png?WT.mc_id=academic-105485-koreyst)

Yapay zeka alanında onlarca yıl süren araştırmalardan sonra, _Transformer_ adı verilen yeni bir model mimarisi, RNN'lerin sınırlarını aşarak çok daha uzun metin dizilerini girdi olarak alabildi. Transformatörler dikkat mekanizmasına dayanır ve modelin aldığı girdilere farklı ağırlıklar vermesini, metin dizisindeki sıralarına bakılmaksızın en alakalı bilgilerin yoğunlaştığı yerlere 'daha fazla dikkat etmesini' sağlar.

Metinsel girdiler ve çıktılarla çalıştıkları için Büyük Dil Modelleri (LLM'ler) olarak da bilinen son nesil yapay zeka modellerinin çoğu gerçekten de bu mimariye dayanmaktadır. Kitaplar, makaleler ve web siteleri gibi çeşitli kaynaklardan elde edilen büyük miktarda etiketsiz veri üzerinde eğitilen bu modellerin ilginç yanı, çok çeşitli görevlere uyarlanabilmeleri ve yaratıcılığa benzer bir şekilde dilbilgisi açısından doğru metinler üretebilmeleridir. Böylece, bir makinenin girdi metnini 'anlama' kapasitesini inanılmaz bir şekilde artırmakla kalmadılar, aynı zamanda insan dilinde orijinal bir yanıt üretme kapasitelerini de sağladılar.

## Büyük dil modelleri nasıl çalışır?

Bir sonraki bölümde farklı türde Üretken Yapay Zeka modellerini inceleyeceğiz, ancak şimdilik OpenAI GPT (Generative Pre-trained Transformer) modellerine odaklanarak büyük dil modellerinin nasıl çalıştığına bir göz atalım.

- **Tokenizer, metinden sayılara**: Büyük Dil Modelleri girdi olarak bir metin alır ve çıktı olarak bir metin oluşturur. Ancak, istatistiksel modeller olduklarından, metin dizilerinden çok sayılarla daha iyi çalışırlar. Bu nedenle modele gelen her girdi, çekirdek model tarafından kullanılmadan önce bir tokenizer tarafından işlenir. Bir belirteç, değişken sayıda karakterden oluşan bir metin yığınıdır, bu nedenle belirteçleyicinin ana görevi girdiyi bir belirteç dizisine bölmektir. Daha sonra her bir token, orijinal metin yığınının tamsayı kodlaması olan bir token indeksi ile eşleştirilir.

![Tokenizer örneği](../../images/tokenizer-example.png?WT.mc_id=academic-105485-koreyst)

- **Çıktı belirteçlerini tahmin etme**: Girdi olarak n belirteç verildiğinde (maksimum n bir modelden diğerine değişir), model çıktı olarak bir belirteci tahmin edebilir. Bu belirteç daha sonra genişleyen bir pencere modelinde bir sonraki yinelemenin girdisine dahil edilir ve bir (veya birden fazla) cümleyi yanıt olarak alma konusunda daha iyi bir kullanıcı deneyimi sağlar. Bu, ChatGPT ile oynadıysanız, bazen neden bir cümlenin ortasında duruyormuş gibi göründüğünü fark etmiş olabilirsiniz.

- **Seçim süreci, olasılık dağılımı**: Çıktı belirteci, model tarafından mevcut metin dizisinden sonra ortaya çıkma olasılığına göre seçilir. Bunun nedeni, modelin eğitimine dayalı olarak hesaplanan tüm olası 'sonraki belirteçler' üzerinde bir olasılık dağılımı tahmin etmesidir. Ancak, her zaman ortaya çıkan dağılımdan en yüksek olasılığa sahip belirteç seçilmez. Modelin deterministik olmayan bir şekilde hareket ettiği bir şekilde bu seçime bir dereceye kadar rastgelelik eklenir - aynı girdi için tam olarak aynı çıktıyı almayız. Bu rastgelelik derecesi yaratıcı düşünme sürecini simüle etmek için eklenmiştir ve sıcaklık adı verilen bir model parametresi kullanılarak ayarlanabilir.

## Girişimimiz Büyük Dil Modellerinden nasıl yararlanabilir?

Artık büyük bir dil modelinin iç işleyişini daha iyi anladığımıza göre, iş senaryomuzu göz önünde bulundurarak, oldukça iyi gerçekleştirebilecekleri en yaygın görevlerin bazı pratik örneklerini görelim.
Bir Büyük Dil Modelinin ana yeteneğinin _doğal dilde yazılmış bir metin girdisinden başlayarak sıfırdan bir metin oluşturmak_ olduğunu söylemiştik.

Peki ama ne tür bir metinsel girdi ve çıktı?
Büyük bir dil modelinin girdisi komut istemi olarak bilinirken, çıktı ise tamamlama olarak bilinir; bu terim, mevcut girdiyi tamamlamak için bir sonraki belirteci üreten model mekanizmasını ifade eder. İstemin ne olduğunu ve modelimizden en iyi şekilde yararlanacak şekilde nasıl tasarlanacağını derinlemesine inceleyeceğiz. Ancak şimdilik, bir komut isteminin şunları içerebileceğini söyleyelim:

- Modelden beklediğimiz çıktı türünü belirten bir **talimat**. Bu talimat bazen bazı örnekler veya bazı ek veriler içerebilir.

  1. Yapılandırılmamış verilerden içgörülerin çıkarılmasıyla birlikte bir makalenin, kitabın, ürün incelemelerinin ve daha fazlasının özetlenmesi.
    
    ![Özetleme örneği](../../images/summarization-example.png?WT.mc_id=academic-105485-koreyst)
  
  2. Bir makale, bir deneme, bir ödev veya daha fazlası için yaratıcı fikir ve tasarım.
      
     ![Yaratıcı yazma örneği](../../images/creative-writing-example.png?WT.mc_id=academic-105485-koreyst)

- Bir aracı ile konuşma şeklinde sorulan bir **soru**.
  
  ![Konuşma örneği](../../images/conversation-example.png?WT.mc_id=academic-105485-koreyst)

- Tamamlanacak bir **metin yığını**, ki bu dolaylı olarak bir yazma yardımı talebidir.
  
  ![Metin tamamlama örneği](../../images/text-completion-example.png?WT.mc_id=academic-105485-koreyst)

- Açıklama ve belgeleme isteğiyle birlikte bir **kod** yığını veya belirli bir görevi yerine getiren bir kod parçası oluşturmayı isteyen bir yorum.
  
  ![Kodlama örneği](../../images/coding-example.png?WT.mc_id=academic-105485-koreyst)

Yukarıdaki örnekler oldukça basittir ve Büyük Dil Modelleri yeteneklerinin kapsamlı bir gösterimi olmak istememektedir. Sadece, özellikle eğitim bağlamlarıyla sınırlı olmamak üzere, üretken yapay zeka kullanımının potansiyelini göstermek istemektedirler.

Ayrıca, üretken bir YZ modelinin çıktısı mükemmel değildir ve bazen modelin yaratıcılığı ona karşı çalışabilir, bu da insan kullanıcının gerçekliğin bir gizemi olarak yorumlayabileceği veya saldırgan olabileceği kelimelerin bir kombinasyonu olan bir çıktı ile sonuçlanabilir. Üretken YZ zeki değildir - en azından eleştirel ve yaratıcı muhakeme veya duygusal zekayı da içeren daha kapsamlı zeka tanımında; deterministik değildir ve güvenilir değildir, çünkü hatalı referanslar, içerik ve ifadeler gibi uydurmalar doğru bilgilerle birleştirilebilir ve ikna edici ve kendinden emin bir şekilde sunulabilir. İlerleyen derslerde, tüm bu sınırlamalarla ilgileneceğiz ve bunları azaltmak için neler yapabileceğimizi göreceğiz.

## Görev

Göreviniz [Üretken Yapay Zeka](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) hakkında daha fazla araştırma yapmak ve şu anda kullanılmayan bir alanda üretken yapay zekayı nasıl kullanabileceğinizi belirlemektir. Bu teknolojiyi eklediğinizde, geleneksel yöntemlerden nasıl farklı bir etki yaratır? Daha önce yapamadığınız bir şeyi yapabilir misiniz, yoksa sadece daha hızlı mı olursunuz?

Hayalinizdeki yapay zeka girişiminin nasıl görüneceğini açıklayan 300 kelimelik bir özet yazın. "Sorun", "Yapay Zekayı Nasıl Kullanırım", "Etkisi" gibi başlıklar ekleyin ve isteğe bağlı olarak bir iş planı da dahil edebilirsiniz.

Bu görevi tamamlarsanız [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) programına başvurmaya bile hazır olabilirsiniz! Azure, OpenAI kredileri, mentorluk ve daha fazlasını sunduğumuz bu programı inceleyin. 🚀

## Bilgi Kontrolü

Büyük dil modelleri hakkında hangisi doğrudur?

1. Her zaman tamamen aynı yanıtı alırsınız.
2. Her şeyi mükemmel yapar; toplama işlemlerinde harikadır, çalışır durumda kod üretir vb.
3. Aynı istemi (prompt) kullanmanıza rağmen yanıt değişebilir. Ayrıca, ister metin ister kod olsun, size iyi bir ilk taslak sunmada mükemmeldir. Ancak, sonuçları geliştirmeniz gerekir.

Cevap: 3, bir LLM (Büyük Dil Modeli) deterministik değildir, yani yanıtları değişebilir. Ancak, bu değişkenliği bir sıcaklık ayarı ile kontrol edebilirsiniz. Ayrıca, her şeyi mükemmel yapmasını beklememelisiniz; asıl amacı sizin için ağır işleri yapmak ve genellikle geliştirmeniz gereken iyi bir ilk denemeyi sunmaktır.

## Harika İş! Yolculuğa Devam Edin 🚀

Bu dersi tamamladıktan sonra [Üretken Yapay Zeka Öğrenme Koleksiyonumuzu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) inceleyerek Üretken Yapay Zeka bilginizi geliştirmeye devam edin!

Ders 2'ye geçerek farklı LLM türlerini nasıl [keşfedip karşılaştırabileceğinizi](../../../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst) öğrenin!
