<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78bbeed50fd4dc9fdee931f5daf98cb3",
  "translation_date": "2025-10-17T16:16:11+00:00",
  "source_file": "12-designing-ux-for-ai-applications/README.md",
  "language_code": "tr"
}
-->
# AI Uygulamaları için UX Tasarımı

[![AI Uygulamaları için UX Tasarımı](../../../translated_images/12-lesson-banner.c53c3c7c802e8f563953ce388f6a987ca493472c724d924b060be470951c53c8.tr.png)](https://youtu.be/VKbCejSICA8?si=MKj7GQYHfXRZyWW6)

> _(Bu dersin videosunu izlemek için yukarıdaki görsele tıklayın)_

Kullanıcı deneyimi, uygulama geliştirme sürecinin çok önemli bir yönüdür. Kullanıcıların uygulamanızı verimli bir şekilde kullanarak görevlerini yerine getirebilmesi gerekir. Verimli olmak bir şeydir, ancak uygulamaları herkesin kullanabileceği şekilde tasarlamak, yani onları _erişilebilir_ hale getirmek de gereklidir. Bu bölüm, bu alana odaklanacak ve umarız insanların kullanmak isteyeceği bir uygulama tasarlamanıza yardımcı olacaktır.

## Giriş

Kullanıcı deneyimi, bir kullanıcının belirli bir ürün veya hizmetle, ister bir sistem, araç veya tasarım olsun, nasıl etkileşimde bulunduğu ve kullandığıdır. AI uygulamaları geliştirirken, geliştiriciler yalnızca kullanıcı deneyiminin etkili olmasını sağlamakla kalmaz, aynı zamanda etik olmasına da odaklanır. Bu derste, kullanıcı ihtiyaçlarını karşılayan Yapay Zeka (AI) uygulamalarının nasıl oluşturulacağını ele alıyoruz.

Ders şu alanları kapsayacaktır:

- Kullanıcı Deneyimine Giriş ve Kullanıcı İhtiyaçlarını Anlama
- Güven ve Şeffaflık için AI Uygulamaları Tasarlama
- İşbirliği ve Geri Bildirim için AI Uygulamaları Tasarlama

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra:

- Kullanıcı ihtiyaçlarını karşılayan AI uygulamalarını nasıl oluşturacağınızı anlayacaksınız.
- Güven ve işbirliğini teşvik eden AI uygulamaları tasarlayabileceksiniz.

### Ön Koşul

Biraz zaman ayırarak [kullanıcı deneyimi ve tasarım düşüncesi](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst) hakkında daha fazla okuyun.

## Kullanıcı Deneyimine Giriş ve Kullanıcı İhtiyaçlarını Anlama

Hayali eğitim girişimimizde, iki ana kullanıcı grubumuz var: öğretmenler ve öğrenciler. Her iki kullanıcının da kendine özgü ihtiyaçları vardır. Kullanıcı merkezli bir tasarım, ürünlerin hedef kitlesi için uygun ve faydalı olmasını sağlayarak kullanıcıyı önceliklendirir.

Uygulama, iyi bir kullanıcı deneyimi sağlamak için **kullanışlı, güvenilir, erişilebilir ve hoş** olmalıdır.

### Kullanışlılık

Kullanışlı olmak, uygulamanın amacına uygun işlevselliğe sahip olması anlamına gelir; örneğin, notlandırma sürecini otomatikleştirmek veya tekrar için flash kartlar oluşturmak gibi. Notlandırma sürecini otomatikleştiren bir uygulama, önceden tanımlanmış kriterlere göre öğrencilerin çalışmalarına doğru ve verimli bir şekilde puan verebilmelidir. Benzer şekilde, tekrar flash kartları oluşturan bir uygulama, verilerine dayanarak ilgili ve çeşitli sorular oluşturabilmelidir.

### Güvenilirlik

Güvenilir olmak, uygulamanın görevini tutarlı bir şekilde ve hatasız yerine getirebilmesi anlamına gelir. Ancak, AI tıpkı insanlar gibi mükemmel değildir ve hatalara yatkın olabilir. Uygulamalar, insan müdahalesi veya düzeltme gerektiren hatalar veya beklenmedik durumlarla karşılaşabilir. Hataları nasıl ele alıyorsunuz? Dersin son bölümünde, AI sistemlerinin ve uygulamalarının işbirliği ve geri bildirim için nasıl tasarlandığını ele alacağız.

### Erişilebilirlik

Erişilebilir olmak, kullanıcı deneyimini çeşitli yeteneklere sahip kullanıcılara, engelli bireyler de dahil olmak üzere, genişletmek anlamına gelir. Erişilebilirlik yönergeleri ve ilkelerine uyarak, AI çözümleri daha kapsayıcı, kullanılabilir ve tüm kullanıcılar için faydalı hale gelir.

### Hoş

Hoş olmak, uygulamanın kullanımı keyifli olması anlamına gelir. Çekici bir kullanıcı deneyimi, kullanıcı üzerinde olumlu bir etki yaratabilir, onları uygulamaya geri dönmeye teşvik edebilir ve işletme gelirini artırabilir.

![AI'de UX ile ilgili hususları gösteren bir görsel](../../../translated_images/uxinai.d5b4ed690f5cefff0c53ffcc01b480cdc1828402e1fdbc980490013a3c50935a.tr.png)

Her zorluk AI ile çözülemez. AI, kullanıcı deneyiminizi manuel görevleri otomatikleştirmek veya kullanıcı deneyimlerini kişiselleştirmek gibi alanlarda desteklemek için devreye girer.

## Güven ve Şeffaflık için AI Uygulamaları Tasarlama

AI uygulamaları tasarlarken güven oluşturmak çok önemlidir. Güven, bir kullanıcının uygulamanın işi yapacağına, sonuçları tutarlı bir şekilde teslim edeceğine ve sonuçların kullanıcının ihtiyaçlarına uygun olduğuna dair güvenini sağlar. Bu alandaki bir risk, güvensizlik ve aşırı güvendir. Güvensizlik, bir kullanıcının bir AI sistemine az veya hiç güven duymaması durumunda ortaya çıkar ve bu, kullanıcının uygulamanızı reddetmesine yol açar. Aşırı güven, bir kullanıcının bir AI sisteminin yeteneklerini fazla tahmin etmesi durumunda ortaya çıkar ve kullanıcıların AI sistemine çok fazla güvenmesine neden olur. Örneğin, notlandırmayı otomatikleştiren bir sistemde aşırı güven, öğretmenin bazı kağıtları gözden geçirmemesi ve notlandırma sisteminin doğru çalıştığından emin olmamasıyla sonuçlanabilir. Bu, öğrenciler için adaletsiz veya yanlış notlara ya da geri bildirim ve iyileştirme fırsatlarının kaçırılmasına yol açabilir.

Güveni tasarımın merkezine yerleştirmenin iki yolu açıklanabilirlik ve kontroldür.

### Açıklanabilirlik

AI, gelecekteki nesillere bilgi aktarmak gibi kararlar alırken öğretmenlerin ve ebeveynlerin AI kararlarının nasıl alındığını anlaması kritik önem taşır. Bu, açıklanabilirliktir - AI uygulamalarının kararları nasıl aldığını anlamak. Açıklanabilirlik için tasarım yapmak, AI'nın çıktıya nasıl ulaştığını vurgulayan ayrıntılar eklemeyi içerir. Hedef kitle, çıktının bir insan tarafından değil, AI tarafından oluşturulduğunun farkında olmalıdır. Örneğin, "Şimdi öğretmeninizle sohbet etmeye başlayın" demek yerine "İhtiyaçlarınıza uyum sağlayan ve kendi hızınızda öğrenmenize yardımcı olan AI öğretmenini kullanın" diyebilirsiniz.

![AI uygulamalarında açıklanabilirliği açıkça gösteren bir uygulama açılış sayfası](../../../translated_images/explanability-in-ai.134426a96b498fbfdc80c75ae0090aedc0fc97424ae0734fccf7fb00a59a20d9.tr.png)

Bir diğer örnek, AI'nın kullanıcı ve kişisel verileri nasıl kullandığıdır. Örneğin, öğrenci kişiliğine sahip bir kullanıcı, kişiliğine bağlı olarak sınırlamalara sahip olabilir. AI, soruların cevaplarını açıklayamayabilir ancak kullanıcının bir problemi nasıl çözebileceğini düşünmesine yardımcı olabilir.

![Kişiliğe dayalı sorulara yanıt veren AI](../../../translated_images/solving-questions.b7dea1604de0cbd2e9c5fa00b1a68a0ed77178a035b94b9213196b9d125d0be8.tr.png)

Açıklanabilirliğin son önemli kısmı, açıklamaların basitleştirilmesidir. Öğrenciler ve öğretmenler AI uzmanı olmayabilir, bu nedenle uygulamanın ne yapıp ne yapamayacağına dair açıklamalar basit ve anlaşılır olmalıdır.

![AI yetenekleri hakkında basitleştirilmiş açıklamalar](../../../translated_images/simplified-explanations.4679508a406c3621fa22bad4673e717fbff02f8b8d58afcab8cb6f1aa893a82f.tr.png)

### Kontrol

Üretken AI, AI ile kullanıcı arasında bir işbirliği yaratır; örneğin, bir kullanıcı farklı sonuçlar için istemleri değiştirebilir. Ayrıca, bir çıktı oluşturulduktan sonra, kullanıcılar sonuçları değiştirerek kontrol hissi kazanmalıdır. Örneğin, Bing'i kullanırken, format, ton ve uzunluğa göre isteminizi özelleştirebilirsiniz. Ayrıca, çıktınıza değişiklikler ekleyebilir ve çıktıyı aşağıda gösterildiği gibi değiştirebilirsiniz:

![İstem ve çıktıyı değiştirme seçenekleriyle Bing arama sonuçları](../../../translated_images/bing1.293ae8527dbe2789b675c8591c9fb3cb1aa2ada75c2877f9aa9edc059f7a8b1c.tr.png)

Bing'deki bir diğer özellik, kullanıcının uygulama üzerinde kontrol sahibi olmasını sağlayan, AI'nın kullandığı verilere katılma veya çıkma seçeneğidir. Bir okul uygulaması için bir öğrenci, notlarını ve öğretmen kaynaklarını tekrar materyali olarak kullanmak isteyebilir.

![İstem ve çıktıyı değiştirme seçenekleriyle Bing arama sonuçları](../../../translated_images/bing2.309f4845528a88c28c1c9739fb61d91fd993dc35ebe6fc92c66791fb04fceb4d.tr.png)

> AI uygulamaları tasarlarken, kullanıcıların aşırı güven duymalarını ve yetenekleri hakkında gerçekçi olmayan beklentiler oluşturmalarını önlemek için kasıtlı olmak önemlidir. Bunu yapmanın bir yolu, istemler ve sonuçlar arasında sürtünme yaratmaktır. Kullanıcıya bunun bir AI olduğunu ve bir insan olmadığını hatırlatmak.

## İşbirliği ve Geri Bildirim için AI Uygulamaları Tasarlama

Daha önce belirtildiği gibi, üretken AI, kullanıcı ve AI arasında bir işbirliği yaratır. Çoğu etkileşim, bir kullanıcının bir istem girmesi ve AI'nın bir çıktı üretmesiyle gerçekleşir. Peki ya çıktı yanlışsa? Uygulama hataları nasıl ele alıyor? AI kullanıcıyı mı suçluyor yoksa hatayı açıklamak için zaman mı ayırıyor?

AI uygulamaları, geri bildirim alacak ve verecek şekilde tasarlanmalıdır. Bu, yalnızca AI sisteminin gelişmesine yardımcı olmakla kalmaz, aynı zamanda kullanıcılarla güven oluşturur. Tasarımda bir geri bildirim döngüsü dahil edilmelidir; örneğin, basit bir beğenme veya beğenmeme seçeneği olabilir.

Bunu ele almanın bir diğer yolu, sistemin yeteneklerini ve sınırlamalarını açıkça iletmektir. Bir kullanıcı, AI'nın yeteneklerinin ötesinde bir şey talep ettiğinde, bununla başa çıkmanın bir yolu olmalıdır, aşağıda gösterildiği gibi.

![Geri bildirim verme ve hataları ele alma](../../../translated_images/feedback-loops.7955c134429a94663443ad74d59044f8dc4ce354577f5b79b4bd2533f2cafc6f.tr.png)

Sistem hataları, kullanıcının AI'nın kapsamı dışındaki bilgilerle ilgili yardıma ihtiyaç duyabileceği veya uygulamanın bir kullanıcının kaç soru/konu oluşturabileceği konusunda bir sınırı olabileceği durumlarda yaygındır. Örneğin, sınırlı konularla (örneğin, Tarih ve Matematik) eğitilmiş bir AI uygulaması, Coğrafya ile ilgili soruları ele alamayabilir. Bunu hafifletmek için, AI sistemi şu şekilde bir yanıt verebilir: "Üzgünüm, ürünümüz aşağıdaki konularla ilgili verilerle eğitilmiştir....., sorduğunuz soruya yanıt veremem."

AI uygulamaları mükemmel değildir, bu nedenle hata yapmaları kaçınılmazdır. Uygulamalarınızı tasarlarken, kullanıcıların geri bildirimde bulunabilmesi ve hataların basit ve kolay anlaşılır bir şekilde ele alınabilmesi için alan yaratmalısınız.

## Ödev

Şimdiye kadar oluşturduğunuz herhangi bir AI uygulamasını ele alın ve aşağıdaki adımları uygulamayı düşünün:

- **Hoş:** Uygulamanızı nasıl daha hoş hale getirebilirsiniz? Her yerde açıklamalar ekliyor musunuz? Kullanıcıyı keşfetmeye teşvik ediyor musunuz? Hata mesajlarınızı nasıl ifade ediyorsunuz?

- **Kullanışlılık:** Bir web uygulaması oluşturun. Uygulamanızın hem fare hem de klavye ile gezilebilir olduğundan emin olun.

- **Güven ve şeffaflık:** AI'ya ve çıktısına tamamen güvenmeyin, sürece bir insan ekleyerek çıktıyı doğrulama yollarını düşünün. Ayrıca güven ve şeffaflığı sağlamak için diğer yolları düşünün ve uygulayın.

- **Kontrol:** Kullanıcının uygulamaya sağladığı veriler üzerinde kontrol sahibi olmasını sağlayın. Kullanıcının AI uygulamasında veri toplama işlemine katılma veya çıkma seçeneğini uygulayın.

<!-- ## [Ders sonrası test](../../../12-designing-ux-for-ai-applications/quiz-url) -->

## Öğrenmeye Devam Edin!

Bu dersi tamamladıktan sonra, [Üretken AI Öğrenme koleksiyonumuzu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) inceleyerek Üretken AI bilginizi geliştirmeye devam edin!

13. Derse geçin, burada [AI uygulamalarını güvence altına almayı](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) ele alacağız!

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.