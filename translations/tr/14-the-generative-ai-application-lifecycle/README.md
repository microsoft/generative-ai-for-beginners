[![Fonksiyon çağrımı ile entegrasyon](../../../translated_images/tr/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# Üretken AI Uygulama Yaşam Döngüsü

Tüm AI uygulamaları için önemli bir soru, AI özelliklerinin alaka düzeyidir; çünkü AI hızla gelişen bir alandır. Uygulamanızın ilgili, güvenilir ve sağlam kalmasını sağlamak için sürekli izlemeniz, değerlendirmeniz ve iyileştirmeniz gerekir. İşte bu noktada üretken AI yaşam döngüsü devreye girer.

Üretken AI yaşam döngüsü, üretken AI uygulamasını geliştirme, dağıtma ve bakım aşamalarında size rehberlik eden bir çerçevedir. Hedeflerinizi tanımlamanıza, performansınızı ölçmenize, zorluklarınızı belirlemenize ve çözümlerinizi uygulamanıza yardımcı olur. Ayrıca uygulamanızı alanınızın etik ve yasal standartları ile paydaşlarınızın beklentilerine uyumlu hale getirmenize de yardımcı olur. Üretken AI yaşam döngüsünü takip ederek, uygulamanızın her zaman değer sağlamasını ve kullanıcılarınızı memnun etmesini sağlayabilirsiniz.

## Giriş

Bu bölümde şunları yapacaksınız:

- MLOps'tan LLMOps'a Paradigma Değişimini Anlamak
- LLM Yaşam Döngüsü
- Yaşam Döngüsü Araçları
- Yaşam Döngüsü Ölçütlendirme ve Değerlendirme

## MLOps'tan LLMOps'a Paradigma Değişimini Anlamak

LLM'ler, Yapay Zeka cephesinde yeni bir araçtır; analiz ve üretim görevlerinde inanılmaz güçlüdürler, ancak bu güç AI ve Klasik Makine Öğrenimi görevlerini nasıl kolaylaştırdığımız konusunda bazı sonuçlar doğurur.

Bununla birlikte, bu aracı dinamik bir şekilde ve doğru teşviklerle adapte etmek için yeni bir Paradigma’ya ihtiyacımız var. Eski AI uygulamalarını "ML Uygulamaları" olarak ve yeni AI uygulamalarını "GenAI Uygulamaları" ya da sadece "AI Uygulamaları" olarak kategorize edebiliriz; bu, o dönemde kullanılan ana teknoloji ve teknikleri yansıtır. Bu anlatımızı birçok şekilde değiştirir, aşağıdaki karşılaştırmaya bakın.

![LLMOps ve MLOps karşılaştırması](../../../translated_images/tr/01-llmops-shift.29bc933cb3bb0080.webp)

Dikkat edin LLMOps'ta, daha çok Uygulama Geliştiricilere odaklanıyoruz, entegrasyonları önemli bir nokta olarak kullanıyor, "Hizmet olarak Modeller" kullanıyor ve metrikler için şu noktalara odaklanıyoruz.

- Kalite: Yanıt kalitesi
- Zararlı Etki: Sorumlu AI
- Doğruluk: Yanıtın dayanağı (Mantıklı mı? Doğru mu?)
- Maliyet: Çözüm Bütçesi
- Gecikme: Ortalama token yanıt süresi

## LLM Yaşam Döngüsü

Öncelikle yaşam döngüsünü ve yapılan değişiklikleri anlamak için bir sonraki infografike bakalım.

![LLMOps infografiği](../../../translated_images/tr/02-llmops.70a942ead05a7645.webp)

Gördüğünüz gibi, bu klasik MLOps yaşam döngülerinden farklıdır. LLM'lerin birçok yeni gereksinimi vardır, örneğin Prompting, kaliteyi artırmak için farklı teknikler (İnce Ayar, RAG, Meta-Promptlar), sorumluluk ve Sorumlu AI ile farklı değerlendirme ve nihayetinde yeni değerlendirme metrikleri (Kalite, Zararlı Etki, Doğruluk, Maliyet ve Gecikme).

Örneğin, nasıl fikir oluşturduğumuza bakın. Hipotezlerinin doğru olup olamayacağını test etmek için çeşitli LLM'lerde denemeler yapmak amacıyla prompt mühendisliği kullanıyoruz.

Bunun doğrusal değil, entegre döngüler, yinelemeli ve kapsamlı bir döngü olduğunu unutmayın.

Bu adımları nasıl keşfedebiliriz? Bir yaşam döngüsü nasıl kurarız detayına inelim.

![LLMOps İş Akışı](../../../translated_images/tr/03-llm-stage-flows.3a1e1c401235a6cf.webp)

Bu biraz karmaşık görünebilir, önce üç büyük adıma odaklanalım.

1. Fikir Üretme/Keşfetme: Keşif, burada iş ihtiyaçlarımıza göre keşif yapabiliriz. Prototipleme, bir [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) oluşturup hipotezimiz için yeterince verimli olup olmadığını test etmek.
1. İnşa Etme/Geliştirme: Uygulama, şimdi daha büyük veri setleri için değerlendiriyoruz, ince ayar ve RAG gibi teknikleri uygulayarak çözümümüzün sağlamlığını kontrol ediyoruz. Eğer sağlam değilse, akışı yeniden uygulamak, yeni adımlar eklemek veya veriyi yeniden yapılandırmak yardımcı olabilir. Akışımızı ve ölçeğimizi test ettikten ve metriklerimizi kontrol ettikten sonra bir sonraki adıma hazırdır.
1. Operasyonlaştırma: Entegrasyon, şimdi sistemimize İzleme ve Uyarı Sistemleri ekliyor, dağıtım yapıyor ve Uygulamamıza uygulama entegrasyonu sağlıyoruz.

Ardından, güvenlik, uyumluluk ve yönetim üzerine odaklanan kapsamlı bir Yönetim döngümüz var.

Tebrikler, artık AI Uygulamanız hazır ve çalışır durumda. Pratik deneyim için [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst) adresine göz atabilirsiniz.

Şimdi, hangi araçları kullanabiliriz?

## Yaşam Döngüsü Araçları

Araçlar için, Microsoft [Azure AI Platformu](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) ve [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst), döngünüzü kolayca uygulamanızı ve hazırlamanızı sağlar.

[Azure AI Platformu](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst), [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) kullanımına olanak tanır. Microsoft Foundry (eski adıyla Azure AI Studio), modelleri, örnekleri ve araçları keşfetmenizi, kaynaklarınızı yönetmenizi, UI geliştirme akışlarını ve Kod-Öncelikli geliştirme için SDK/CLI seçeneklerini kullanmanızı sağlayan bir web portalıdır.

![Azure AI olanakları](../../../translated_images/tr/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI, operasyonlarınızı, servislerinizi, projelerinizi, vektör araması ve veritabanı ihtiyaçlarınızı yönetmek için birden fazla kaynağı kullanmanıza olanak tanır.

![Azure AI ile LLMOps](../../../translated_images/tr/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

PromptFlow ile Kavram Kanıtından (POC) büyük ölçekli uygulamalara kadar:

- Görsel ve işlevsel araçlarla VS Code'dan uygulamalar tasarla ve oluştur
- AI kalitesi için uygulamalarını kolayca test et ve ince ayar yap
- Hızlı entegrasyon için Microsoft Foundry kullanarak Bulut ile Entegre et ve yinele, Push ve dağıt

![PromptFlow ile LLMOps](../../../translated_images/tr/06-llm-promptflow.a183eba07a3a7fdf.webp)

## Harika! Öğrenmeye Devam Et!

Muhteşem, şimdi [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst) ile kavramları kullanarak uygulamanın nasıl yapılandırıldığını daha fazla öğren, Bulut Savunuculuğunun bu kavramları gösterimlere nasıl eklediğini kontrol et. Daha fazla içerik için, [Ignite etkinlik oturumumuzu] inceleyin!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Şimdi, üretken AI'yı nasıl etkilediğini anlamak için [Retrieval Augmented Generation ve Vektör Veritabanlarına](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) ilişkin Ders 15'e göz atın ve daha etkileyici Uygulamalar oluşturun!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->