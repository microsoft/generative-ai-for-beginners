<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "13084c6321a2092841b9a081b29497ba",
  "translation_date": "2025-06-25T11:22:38+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "tr"
}
-->
# Üretken Yapay Zayını Sorumlu Kullanma

> _Bu dersin videosunu izlemek için yukarıdaki resme tıklayın_

Yapay zeka ve özellikle üretken yapay zeka ile büyülenmek kolaydır, ancak bunu sorumlu bir şekilde nasıl kullanacağınızı düşünmeniz gerekir. Çıktının adil, zararsız ve daha fazlasını nasıl sağlayacağınızı düşünmelisiniz. Bu bölüm, size belirtilen bağlamı, dikkate almanız gerekenleri ve yapay zeka kullanımınızı geliştirmek için aktif adımlar atmayı nasıl sağlayacağınızı sunmayı amaçlamaktadır.

## Giriş

Bu derste ele alınacak konular:

- Üretken yapay zeka uygulamaları oluştururken Neden Sorumlu Yapay Zekaya öncelik vermelisiniz.
- Sorumlu Yapay Zekanın temel ilkeleri ve bunların Üretken Yapay Zeka ile ilişkisi.
- Bu Sorumlu Yapay Zeka ilkelerini strateji ve araçlar aracılığıyla nasıl uygulayabilirsiniz.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları öğreneceksiniz:

- Üretken yapay zeka uygulamaları oluştururken Sorumlu Yapay Zekanın önemi.
- Üretken yapay zeka uygulamaları oluştururken Sorumlu Yapay Zekanın temel ilkelerini ne zaman düşünmeli ve uygulamalısınız.
- Sorumlu Yapay Zeka kavramını uygulamaya koymak için hangi araçlar ve stratejiler mevcut.

## Sorumlu Yapay Zeka İlkeleri

Üretken Yapay Zeka heyecanı hiç bu kadar yüksek olmamıştı. Bu heyecan, bu alana birçok yeni geliştirici, dikkat ve finansman getirdi. Üretken Yapay Zekayı kullanarak ürünler ve şirketler oluşturmayı düşünen herkes için bu çok olumlu bir durumken, aynı zamanda sorumlu bir şekilde ilerlemek de önemlidir.

Bu kurs boyunca, startup'ımızı ve yapay zeka eğitim ürünümüzü oluşturmak üzerinde odaklanıyoruz. Sorumlu Yapay Zeka ilkelerini kullanacağız: Adalet, Kapsayıcılık, Güvenilirlik/Güvenlik, Güvenlik ve Gizlilik, Şeffaflık ve Hesap Verebilirlik. Bu ilkelerle, ürünlerimizde Üretken Yapay Zekayı nasıl kullandığımızla ilişkilerini inceleyeceğiz.

## Neden Sorumlu Yapay Zekaya Öncelik Vermelisiniz

Bir ürün oluştururken, kullanıcılarınızın en iyi çıkarlarını göz önünde bulundurarak insan merkezli bir yaklaşım benimsemek en iyi sonuçları sağlar.

Üretken Yapay Zekanın benzersizliği, kullanıcılara yardımcı yanıtlar, bilgi, rehberlik ve içerik oluşturma gücünde yatmaktadır. Bu, birçok manuel adım olmadan yapılabilir ve çok etkileyici sonuçlar doğurabilir. Ancak, uygun planlama ve stratejiler olmadan, kullanıcılarınız, ürününüz ve toplum genelinde bazı zararlı sonuçlara da yol açabilir.

Potansiyel zararlı sonuçlardan bazılarına (hepsi değil) bakalım:

### Halüsinasyonlar

Halüsinasyonlar, bir LLM'nin tamamen anlamsız veya diğer bilgi kaynaklarına göre gerçekte yanlış olan içerik ürettiği durumları tanımlamak için kullanılan bir terimdir.

Örneğin, öğrencilerin bir modele tarihsel sorular sormasına olanak tanıyan bir özellik oluşturduğumuzu varsayalım. Bir öğrenci `Who was the sole survivor of Titanic?` sorusunu sorduğunda

Model aşağıdaki gibi bir yanıt üretiyor:

Bu çok güvenilir ve kapsamlı bir yanıt. Ne yazık ki, yanlış. En azından minimal bir araştırma ile, Titanic felaketinden birden fazla kurtulan olduğunu keşfederiz. Bu konu hakkında araştırmaya yeni başlayan bir öğrenci için, bu yanıt sorgulanmadan kabul edilebilecek kadar ikna edici olabilir. Bunun sonuçları, yapay zeka sisteminin güvenilmez olmasına ve startup'ımızın itibarını olumsuz etkilemesine yol açabilir.

Herhangi bir LLM'nin her iterasyonunda, halüsinasyonları minimize etme performansında iyileşmeler görüyoruz. Bu iyileşmelere rağmen, uygulama geliştiricileri ve kullanıcılar olarak bu sınırlamaların farkında olmamız gerekiyor.

### Zararlı İçerik

Önceki bölümde, bir LLM'nin yanlış veya anlamsız yanıtlar ürettiği durumu ele aldık. Dikkat etmemiz gereken başka bir risk ise, modelin zararlı içerik ile yanıt vermesidir.

Zararlı içerik şu şekilde tanımlanabilir:

- Kendine zarar verme veya belirli gruplara zarar verme talimatları verme veya teşvik etme.
- Nefret dolu veya küçümseyici içerik.
- Herhangi bir saldırı veya şiddet eylemi planlamasına rehberlik etme.
- Yasadışı içerik bulma veya yasadışı eylemler gerçekleştirme talimatları verme.
- Cinsel açıdan açık içerik gösterme.

Startup'ımız için, öğrencilerin bu tür içerikleri görmesini önlemek için doğru araçlara ve stratejilere sahip olduğumuzdan emin olmak istiyoruz.

### Adalet Eksikliği

Adalet, "bir yapay zeka sisteminin önyargıdan ve ayrımcılıktan arınmış olmasını ve herkese adil ve eşit muamele etmesini sağlamak" olarak tanımlanır. Üretken Yapay Zeka dünyasında, modelin çıktısının marjinal grupların dışlayıcı dünya görüşlerini güçlendirmemesini sağlamak istiyoruz.

Bu tür çıktılar, kullanıcılarımız için olumlu ürün deneyimleri oluşturmanın yanı sıra toplumsal zarara da yol açar. Uygulama geliştiricileri olarak, Üretken Yapay Zeka ile çözümler oluştururken her zaman geniş ve çeşitli bir kullanıcı tabanını göz önünde bulundurmalıyız.

## Üretken Yapay Zekayı Sorumlu Bir Şekilde Kullanma

Artık Sorumlu Üretken Yapay Zekanın önemini belirlediğimize göre, yapay zeka çözümlerimizi sorumlu bir şekilde oluşturmak için atabileceğimiz 4 adıma bakalım:

### Potansiyel Zararları Ölçme

Yazılım testinde, bir kullanıcının bir uygulama üzerindeki beklenen eylemlerini test ederiz. Benzer şekilde, kullanıcıların en olası kullanacağı çeşitli istemleri test etmek, potansiyel zararı ölçmek için iyi bir yoldur.

Startup'ımız bir eğitim ürünü oluşturduğundan, eğitimle ilgili istemlerin bir listesini hazırlamak iyi olacaktır. Bu, belirli bir konuyu, tarihsel gerçekleri ve öğrenci hayatıyla ilgili istemleri kapsayabilir.

### Potansiyel Zararları Azaltma

Artık modelin ve yanıtlarının neden olabileceği potansiyel zararı önlemek veya sınırlamak için yollar bulma zamanı. Bunu 4 farklı katmanda inceleyebiliriz:

- **Model**. Doğru kullanım durumu için doğru modeli seçmek. GPT-4 gibi daha büyük ve karmaşık modeller, daha küçük ve daha spesifik kullanım durumlarına uygulandığında zararlı içerik riski daha fazla olabilir. Eğitim verilerinizi kullanarak ince ayar yapmak da zararlı içerik riskini azaltır.

- **Güvenlik Sistemi**. Güvenlik sistemi, zararı azaltmaya yardımcı olan platformda modelin hizmet verdiği araçlar ve yapılandırmalar setidir. Azure OpenAI hizmetindeki içerik filtreleme sistemi buna bir örnektir. Sistemler ayrıca jailbreak saldırılarını ve istenmeyen aktiviteleri, örneğin botlardan gelen talepleri tespit etmelidir.

- **Metaprompt**. Metapromptlar ve yerleştirme, belirli davranışlar ve bilgilere dayalı olarak modeli yönlendirme veya sınırlama yollarıdır. Bu, modelin belirli sınırlarını tanımlamak için sistem girdilerini kullanmak olabilir. Ayrıca, sistemin kapsamına veya alanına daha uygun çıktılar sağlamak olabilir.

Bu, modelin yalnızca güvenilir kaynaklardan seçilen bilgileri çekmesini sağlamak için Bilgi Getirme ile Zenginleştirilmiş Üretim (RAG) gibi teknikleri kullanmak olabilir. Bu kursta daha sonra [arama uygulamaları oluşturma](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst) dersi bulunmaktadır.

- **Kullanıcı Deneyimi**. Son katman, kullanıcının modelle doğrudan uygulamamızın arayüzü aracılığıyla bir şekilde etkileşime girdiği yerdir. Bu şekilde, kullanıcıyı modele gönderebileceği girdilerin türleri ve kullanıcıya gösterilen metin veya görüntüler üzerinde sınırlandırarak UI/UX tasarlayabiliriz. Yapay zeka uygulamasını dağıtırken, Üretken Yapay Zeka uygulamamızın ne yapabileceği ve yapamayacağı konusunda şeffaf olmamız da gerekmektedir.

[AI Uygulamaları için UX Tasarımı](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) konusuna adanmış bir dersimiz bulunmaktadır.

- **Modeli Değerlendirme**. LLM'lerle çalışmak zorlu olabilir çünkü modelin eğitildiği veriler üzerinde her zaman kontrol sahibi olmayabiliriz. Bununla birlikte, modelin performansını ve çıktısını her zaman değerlendirmeliyiz. Modelin doğruluğunu, benzerliğini, yerleşikliği ve çıktının alaka düzeyini ölçmek hala önemlidir. Bu, paydaşlara ve kullanıcılara şeffaflık ve güven sağlar.

### Sorumlu Üretken Yapay Zeka Çözümünü İşletme

Yapay zeka uygulamalarınız etrafında operasyonel bir uygulama oluşturmak son aşamadır. Bu, tüm düzenleyici politikalara uygun olduğumuzdan emin olmak için startup'ımızın diğer bölümleriyle, örneğin Hukuk ve Güvenlik ile ortaklık kurmayı içerir. Başlatmadan önce, teslimat, olayları ele alma ve geri alma planları oluşturmak istiyoruz, böylece kullanıcılarımıza herhangi bir zarar vermeyi önleyebiliriz.

## Araçlar

Sorumlu Yapay Zeka çözümleri geliştirme işi çok gibi görünse de, çabaya değer bir iştir. Üretken Yapay Zeka alanı büyüdükçe, geliştiricilerin sorumluluğu iş akışlarına verimli bir şekilde entegre etmelerine yardımcı olacak daha fazla araç olgunlaşacaktır. Örneğin, [Azure AI İçerik Güvenliği](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) API isteği aracılığıyla zararlı içerik ve görüntüleri tespit etmeye yardımcı olabilir.

## Bilgi Kontrolü

Sorumlu yapay zeka kullanımını sağlamak için dikkat etmeniz gereken bazı şeyler nelerdir?

1. Cevabın doğru olması.
1. Zararlı kullanım, yapay zekanın suç amaçlı kullanılmaması.
1. Yapay zekanın önyargıdan ve ayrımcılıktan arındırılmış olduğunun sağlanması.

A: 2 ve 3 doğrudur. Sorumlu Yapay Zeka, zararlı etkileri ve önyargıları nasıl azaltabileceğinizi düşünmenize yardımcı olur ve daha fazlasını sağlar.

## 🚀 Zorluk

[Azure AI İçerik Güvenliği](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) hakkında bilgi edinin ve kullanımınız için neler benimseyebileceğinizi görün.

## Harika İş, Öğrenmeye Devam Edin

Bu dersi tamamladıktan sonra [Üretken Yapay Zeka Öğrenme koleksiyonumuza](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) göz atarak Üretken Yapay Zeka bilginizi artırmaya devam edin!

Ders 4'e gidin, burada [İstek Mühendisliği Temellerine](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst) bakacağız!

**Feragatname**: 
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.