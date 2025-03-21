# Üretici Yapay Zekayı Sorumlu Kullanma

[![Üretici Yapay Zekayı Sorumlu Kullanma](../../images/03-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson3-gh?WT.mc_id=academic-105485-koreyst)

> _Bu dersin videosunu izlemek için yukarıdaki görsele tıklayın_

Yapay zeka ve özellikle üretici yapay zekaya hayran kalmak kolaydır, ancak bunu nasıl sorumlu bir şekilde kullanacağınızı düşünmeniz gerekir. Çıktının adil, zararsız ve daha fazlası olmasını nasıl sağlayacağınız gibi şeyleri düşünmeniz gerekir. Bu bölüm, size bahsedilen bağlamı, neyi düşünmeniz gerektiğini ve yapay zeka kullanımınızı iyileştirmek için aktif adımlar atmayı nasıl sağlayacağınızı anlatmayı amaçlamaktadır.

## Giriş

Bu ders şunları kapsayacak:

- Üretici Yapay Zeka uygulamaları oluştururken Sorumlu Yapay Zekaya neden öncelik vermelisiniz.
- Sorumlu Yapay Zekanın temel ilkeleri ve bunların Üretici Yapay Zeka ile nasıl ilişkili olduğu.
- Bu Sorumlu Yapay Zeka ilkelerini strateji ve araçlar yoluyla pratiğe nasıl dökebilirsiniz.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları bileceksiniz:

- Üretici Yapay Zeka uygulamaları oluştururken Sorumlu Yapay Zekanın önemi.
- Üretici Yapay Zeka uygulamaları oluştururken Sorumlu Yapay Zekanın temel ilkelerini ne zaman düşünüp uygulayacağınız.
- Sorumlu Yapay Zeka kavramını pratiğe dökmek için hangi araç ve stratejilerin mevcut olduğu.

## Sorumlu Yapay Zeka İlkeleri

Üretici Yapay Zekaya olan heyecan hiç bu kadar yüksek olmamıştı. Bu heyecan, bu alana birçok yeni geliştirici, dikkat ve finansman getirdi. Bu, Üretici Yapay Zekayı kullanarak ürün ve şirket kurmak isteyen herkes için çok olumlu olsa da, sorumlu bir şekilde ilerlememiz de önemlidir.

Bu kurs boyunca, startup'ımızı ve yapay zeka eğitim ürünümüzü oluşturmaya odaklanıyoruz. Sorumlu Yapay Zekanın ilkelerini kullanacağız: Adillik, Kapsayıcılık, Güvenilirlik/Güvenlik, Güvenlik ve Gizlilik, Şeffaflık ve Hesap Verebilirlik. Bu ilkelerle, ürünlerimizde Üretici Yapay Zekayı kullanımımızla nasıl ilişkili olduklarını keşfedeceğiz.

## Neden Sorumlu Yapay Zekaya Öncelik Vermelisiniz

Bir ürün oluştururken, kullanıcılarınızın çıkarlarını göz önünde bulundurarak insan merkezli bir yaklaşım benimsemek en iyi sonuçları verir.

Üretici Yapay Zekanın benzersizliği, kullanıcılar için yararlı yanıtlar, bilgiler, rehberlik ve içerik oluşturma gücüdür. Bu, çok etkileyici sonuçlara yol açabilecek birçok manuel adım olmadan yapılabilir. Uygun planlama ve stratejiler olmadan, ne yazık ki kullanıcılarınız, ürününüz ve bir bütün olarak toplum için bazı zararlı sonuçlara da yol açabilir.

Bu potansiyel zararlı sonuçlardan bazılarına (hepsine değil) bakalım:

### Halüsinasyonlar

Halüsinasyonlar, bir LLM'nin ya tamamen anlamsız ya da diğer bilgi kaynaklarına dayanarak faktüel olarak yanlış olduğunu bildiğimiz içerik ürettiğinde kullanılan bir terimdir.

Örneğin, startup'ımız için öğrencilerin bir modele tarihsel sorular sormasına izin veren bir özellik oluşturduğumuzu düşünelim. Bir öğrenci `Titanic'in tek hayatta kalanı kimdi?` sorusunu soruyor.

Model aşağıdaki gibi bir yanıt üretiyor:

![Titanic'in tek hayatta kalanı kimdi" diyen istem](../../../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp?WT.mc_id=academic-105485-koreyst)

> _(Kaynak: [Flying bisons](https://flyingbisons.com?WT.mc_id=academic-105485-koreyst))_

Bu çok güvenli ve kapsamlı bir yanıt. Ne yazık ki, yanlış. Minimal bir araştırmayla bile, Titanic felaketinden birden fazla hayatta kalan olduğu ortaya çıkardı. Bu konuyu yeni araştırmaya başlayan bir öğrenci için, bu yanıt sorgulanmayacak ve gerçek olarak kabul edilecek kadar ikna edici olabilir. Bunun sonuçları, yapay zeka sisteminin güvenilmez olmasına ve startup'ımızın itibarını olumsuz etkilemesine yol açabilir.

Herhangi bir LLM'nin her iterasyonunda, halüsinasyonları en aza indirme konusunda performans iyileştirmeleri gördük. Bu iyileştirmeye rağmen, uygulama geliştiricileri ve kullanıcılar olarak bu sınırlamaların farkında olmaya devam etmeliyiz.

### Zararlı İçerik

Daha önceki bölümde bir LLM'nin yanlış veya anlamsız yanıtlar ürettiği durumları ele aldık. Farkında olmamız gereken bir diğer risk de modelin zararlı içerikle yanıt vermesidir.

Zararlı içerik şöyle tanımlanabilir:

- Kendine zarar verme veya belirli gruplara zarar verme talimatları verme veya teşvik etme.
- Nefret dolu veya aşağılayıcı içerik.
- Her türlü saldırı veya şiddet eyleminin planlanmasına rehberlik etme.
- Yasa dışı içerik bulma veya yasa dışı eylemler gerçekleştirme konusunda talimatlar verme.
- Cinsel açıdan açık içerik gösterme.

Startup'ımız için, öğrencilerin bu tür içerikleri görmesini engellemek için doğru araç ve stratejilere sahip olduğumuzdan emin olmak istiyoruz.

### Adillik Eksikliği

Adillik, "bir yapay zeka sisteminin önyargı ve ayrımcılıktan arındırılmış olmasını ve herkese adil ve eşit davranmasını sağlamak" olarak tanımlanır. Üretici Yapay Zeka dünyasında, marjinalleştirilmiş grupların dışlayıcı dünya görüşlerinin model çıktısı tarafından pekiştirilmemesini sağlamak istiyoruz.

Bu tür çıktılar sadece kullanıcılarımız için olumlu ürün deneyimleri oluşturmada yıkıcı olmakla kalmaz, aynı zamanda toplumsal zarara da neden olur. Uygulama geliştiricileri olarak, Üretici Yapay Zeka ile çözümler oluştururken her zaman geniş ve çeşitli bir kullanıcı tabanını akılda tutmalıyız.

## Üretici Yapay Zekayı Sorumlu Bir Şekilde Nasıl Kullanılır

Şimdi Sorumlu Üretici Yapay Zekanın önemini belirlediğimize göre, yapay zeka çözümlerimizi sorumlu bir şekilde oluşturmak için atabileceğimiz 4 adıma bakalım:

![Azaltma Döngüsü](../../images/mitigate-cycle.png?WT.mc_id=academic-105485-koreyst)

### Potansiyel Zararları Ölçme

Yazılım testinde, bir uygulamada kullanıcının beklenen eylemlerini test ederiz. Benzer şekilde, kullanıcıların en çok kullanması muhtemel çeşitli istemleri test etmek, potansiyel zararı ölçmek için iyi bir yoldur.

Startup'ımız bir eğitim ürünü oluşturduğu için, eğitimle ilgili istemler listesi hazırlamak iyi olacaktır. Bu, belirli bir konuyu, tarihsel gerçekleri ve öğrenci yaşamı hakkındaki istemleri kapsayabilir.

### Potansiyel Zararları Azaltma

Şimdi model ve yanıtlarının neden olabileceği potansiyel zararı önlemenin veya sınırlamanın yollarını bulma zamanı. Buna 4 farklı katmanda bakabiliriz:

![Azaltma Katmanları](../../images/mitigation-layers.png?WT.mc_id=academic-105485-koreyst)

- **Model**. Doğru kullanım senaryosu için doğru modeli seçmek. GPT-4 gibi daha büyük ve karmaşık modeller, daha küçük ve spesifik kullanım senaryolarına uygulandığında zararlı içerik riski oluşturabilir. Eğitim verilerinizi ince ayar için kullanmak da zararlı içerik riskini azaltır.

- **Güvenlik Sistemi**. Güvenlik sistemi, modele hizmet veren platformda zararı azaltmaya yardımcı olan bir dizi araç ve yapılandırmadır. Buna örnek olarak Azure OpenAI hizmetindeki içerik filtreleme sistemi verilebilir. Sistemler ayrıca jailbreak saldırılarını ve botlardan gelen istekler gibi istenmeyen aktiviteleri tespit etmelidir.

- **Meta İstem**. Meta istemler ve temellendirme, modeli belirli davranışlara ve bilgilere göre yönlendirmenin veya sınırlamanın yollarıdır. Bu, modelin belirli sınırlarını tanımlamak için sistem girdilerini kullanmak olabilir. Ayrıca, sistemin kapsamına veya alanına daha uygun çıktılar sağlamak da olabilir.

Ayrıca, modelin yalnızca güvenilir kaynaklardan bilgi çekmesini sağlamak için Geri Alma Artırılmış Üretim (RAG) gibi teknikleri kullanmak da olabilir. Bu kursta daha sonra [arama uygulamaları oluşturma](../../../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst) hakkında bir ders var.

- **Kullanıcı Deneyimi**. Son katman, kullanıcının uygulamamızın arayüzü üzerinden bir şekilde modelle doğrudan etkileşime girdiği yerdir. Bu şekilde, kullanıcının modele gönderebileceği girdi türlerini ve kullanıcıya gösterilen metin veya görselleri sınırlamak için UI/UX'i tasarlayabiliriz. Yapay zeka uygulamasını dağıtırken, Üretici Yapay ZekA uygulamamızın neler yapıp yapamayacağı konusunda da şeffaf olmalıyız.

[Yapay Zeka Uygulamaları için UX Tasarımı](../../../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) konusuna adanmış bir dersimiz var.

- **Modeli değerlendirme**. LLM'lerle çalışmak zor olabilir çünkü modelin eğitildiği veriler üzerinde her zaman kontrolümüz olmaz. Yine de, modelin performansını ve çıktılarını her zaman değerlendirmeliyiz. Modelin doğruluğunu, benzerliğini, temellendirilmişliğini ve çıktının uygunluğunu ölçmek hala önemlidir. Bu, paydaşlara ve kullanıcılara şeffaflık ve güven sağlamaya yardımcı olur.

### Sorumlu Bir Üretici Yapay Zeka Çözümünü İşletme

Yapay zeka uygulamalarınız etrafında operasyonel bir uygulama oluşturmak son aşamadır. Bu, tüm düzenleyici politikalara uygun olduğumuzdan emin olmak için startup'ımızın Hukuk ve Güvenlik gibi diğer bölümleriyle ortaklık kurmayı içerir. Lansmandan önce, kullanıcılarımıza yönelik herhangi bir zararın büyümesini önlemek için teslimat, olayları ele alma ve geri alma planları da oluşturmak istiyoruz.

## Araçlar

Sorumlu Yapay Zeka çözümleri geliştirme işi çok gibi görünse de, bu çaba değer. Üretici Yapay ZekA alanı büyüdükçe, geliştiricilerin sorumluluğu iş akışlarına verimli bir şekilde entegre etmelerine yardımcı olacak daha fazla araç olgunlaşacaktır. Örneğin, [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) bir API isteği aracılığıyla zararlı içerik ve görselleri tespit etmeye yardımcı olabilir.

## Bilgi Kontrolü

Sorumlu yapay zeka kullanımını sağlamak için nelere dikkat etmeniz gerekir?

1. Yanıtın doğru olması.
2. Zararlı kullanım, yapay zekanın suç amaçlı kullanılmaması.
3. Yapay zekanın önyargı ve ayrımcılıktan arındırılmış olmasını sağlamak.

C: 2 ve 3 doğrudur. Sorumlu Yapay ZekA, zararlı etkileri ve önyargıları ve daha fazlasını nasıl azaltacağınızı düşünmenize yardımcı olur.

## 🚀 Challenge

[Azure AI İçerik Güvenliği](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) hakkında bilgi edinin ve kullanımınız için neler benimseyebileceğinize bakın.

## Harika İş, Öğrenmeye Devam Edin

Bu dersi tamamladıktan sonra, Üretici Yapay ZekA bilginizi artırmaya devam etmek için [Üretici Yapay ZekA Öğrenme koleksiyonumuza](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) göz atın!

[İstem Mühendisliği Temelleri](../../../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst) konusunu inceleyeceğimiz Ders 4'e geçin!
