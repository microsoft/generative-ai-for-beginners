# Düşük Kodlu AI Uygulamaları Oluşturma

[![Düşük Kodlu AI Uygulamaları Oluşturma](../../../translated_images/tr/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Dersi izlemek için yukarıdaki görsele tıklayın)_

## Giriş

Artık görüntü oluşturma uygulamalarının nasıl yapılacağını öğrendiğimize göre, düşük koddan bahsedelim. Üretken AI, düşük kod da dahil olmak üzere çeşitli alanlarda kullanılabilir, ancak düşük kod nedir ve AI'yı buna nasıl ekleyebiliriz?

Uygulama ve çözümler oluşturmak, Düşük Kod Geliştirme Platformları sayesinde geleneksel geliştiriciler ve geliştirici olmayanlar için daha kolay hale geldi. Düşük Kod Geliştirme Platformları, çok az veya hiç kod kullanmadan uygulamalar ve çözümler oluşturmanızı sağlar. Bu, sürükle bırak bileşenlerini kullanarak uygulama ve çözümler inşa etmenizi sağlayan görsel bir geliştirme ortamı sunarak başarılır. Bu sayede uygulamalar ve çözümler daha hızlı ve daha az kaynak kullanarak oluşturulabilir. Bu dersimizde, Düşük Kodun nasıl kullanılacağına ve AI kullanarak Power Platform ile düşük kod geliştirmeyi nasıl güçlendireceğimize derinlemesine bakıyoruz.

Power Platform, kuruluşlara ekiplerini sezgisel bir düşük kod ya da kodsuz ortamda kendi çözümlerini geliştirme fırsatı sunar. Bu ortam, çözüm oluşturma sürecini basitleştirir. Power Platform ile çözümler, aylar ya da yıllar yerine günler ya da haftalar içerisinde inşa edilebilir. Power Platform beş temel üründen oluşur: Power Apps, Power Automate, Power BI, Power Pages ve Copilot Studio.

Bu ders şunları içerir:

- Power Platform'da Üretken AI'ya Giriş
- Copilot'a Giriş ve nasıl kullanılacağı
- Power Platform’da Üretken AI kullanarak uygulama ve akışlar oluşturma
- AI Builder ile Power Platform’daki AI Modellerini Anlama
- Microsoft Copilot Studio ile akıllı ajanlar oluşturma

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- Power Platform’da Copilot’un nasıl çalıştığını anlayın.

- Eğitim girişimimiz için bir Öğrenci Ödev Takipçisi Uygulaması oluşturun.

- Faturalardan bilgi çıkarmak için AI kullanan bir Fatura İşleme Akışı oluşturun.

- GPT AI Modeli ile Metin Oluşturma’da en iyi uygulamaları uygulayın.

- Microsoft Copilot Studio'nun ne olduğunu ve onunla akıllı ajanlar oluşturmayı anlayın.

Bu derste kullanacağınız araçlar ve teknolojiler şunlardır:

- **Power Apps**, uygulama oluşturmak, verileri takip etmek, yönetmek ve etkileşim kurmak için düşük kod geliştirme ortamı sağlar; Öğrenci Ödev Takipçisi uygulaması için kullanılır.

- **Dataverse**, Öğrenci Ödev Takipçisi uygulamasının verilerini depolamak için kullanılır ve düşük kodlu veri platformu sağlar.

- **Power Automate**, Fatura İşleme akışı için kullanılır; Fatura işleme sürecini otomatikleştirmek için düşük kod geliştirme ortamı sunar.

- **AI Builder**, Fatura İşleme AI Modeli için kullanılır; önceden oluşturulmuş AI Modelleri ile faturaları işler.

## Power Platform'da Üretken AI

Üretken AI ile düşük kod geliştirme ve uygulama geliştirmeyi güçlendirmek Power Platform'un ana odak alanlarından biridir. Amaç, herkesin herhangi bir veri bilimi bilgisi gerekmeden AI destekli uygulamalar, siteler, panolar ve otomasyon süreçleri oluşturabilmesini sağlamaktır. Bu hedef, Power Platform'da Copilot ve AI Builder şeklinde üretken AI'nın düşük kod geliştirme deneyimine entegrasyonu ile gerçekleştirilir.

### Bu nasıl çalışır?

Copilot, doğal dil kullanarak gereksinimlerinizi bir dizi sohbet adımıyla tarif ederek Power Platform çözümleri oluşturmanızı sağlayan bir AI yardımcısıdır. Örneğin, AI yardımcınıza uygulamanızda hangi alanların kullanılacağını söyleyebilir, hem uygulamayı hem de altında yatan veri modelini oluşturmasını sağlayabilir ya da Power Automate'te bir akışın nasıl kurulacağını belirtebilirsiniz.

Copilot ile çalışan işlevleri, kullanıcıların sohbet aracılığıyla içgörüler keşfetmesini sağlamak için uygulama ekranlarınızda bir özellik olarak kullanabilirsiniz.

AI Builder, Power Platform'daki düşük kodlu bir AI yeteneğidir ve AI Modelleri kullanarak süreçleri otomatikleştirmenize ve sonuçları tahmin etmenize yardımcı olur. AI Builder ile Dataverse ya da SharePoint, OneDrive veya Azure gibi çeşitli bulut veri kaynaklarına bağlanan uygulamalarınıza ve akışlarınıza AI katabilirsiniz.

Copilot, Power Apps, Power Automate, Power BI, Power Pages ve Copilot Studio (eski adıyla Power Virtual Agents) gibi tüm Power Platform ürünlerinde kullanıma sunulmuştur. AI Builder, Power Apps ve Power Automate’te mevcuttur. Bu derste, eğitim girişimimiz için bir çözüm geliştirmek üzere Power Apps ve Power Automate’te Copilot ve AI Builder nasıl kullanılır üzerinde duracağız.

### Power Apps'ta Copilot

Power Platform'un bir parçası olan Power Apps, verileri takip etmek, yönetmek ve onlarla etkileşim kurmak için uygulamalar oluşturulması amacıyla düşük kod geliştirme ortamı sağlar. Bu, ölçeklenebilir bir veri platformu ve bulut hizmetleri ile dahili veri bağlantısı sunan uygulama geliştirme servislerinden oluşan bir pakettir. Power Apps, tarayıcılarda, tabletlerde ve telefonlarda çalışan uygulamalar oluşturmanızı ve iş arkadaşlarınızla paylaşmanızı sağlar. Power Apps, her işletme kullanıcısının veya profesyonel geliştiricinin kolayca özel uygulamalar oluşturmasını sağlamak için basit bir arayüz sunar. Ayrıca uygulama geliştirme deneyimi, Copilot sayesinde Üretken AI ile geliştirilmiştir.

Power Apps'taki Copilot AI asistan özelliği sayesinde, ihtiyaç duyduğunuz uygulamayı ve uygulamanızın takip, toplama ya da gösterme yapmak istediği bilgileri tarif edebilirsiniz. Copilot, tanıma dayalı duyarlı bir Canvas uygulaması oluşturur. Uygulamayı ihtiyaçlarınıza göre daha sonra özelleştirebilirsiniz. AI Copilot ayrıca takip etmek istediğiniz verileri depolamak için gereken alanlar ve örnek veriler ile bir Dataverse Tablosu önerir ve oluşturur. Bu derste Dataverse'in ne olduğu ve Power Apps'ta nasıl kullanılacağına daha sonra bakacağız. Tabloyu, AI Copilot asistanı ile sohbet adımları aracılığıyla ihtiyaçlarınıza göre özelleştirebilirsiniz. Bu özellik Power Apps ana ekranından kolayca erişilebilir.

### Power Automate'te Copilot

Power Platform'un bir parçası olan Power Automate, kullanıcıların uygulamalar ve hizmetler arasında otomatik iş akışları oluşturmasını sağlar. İletişim, veri toplama ve karar onayları gibi tekrarlayan iş süreçlerini otomatikleştirir. Basit arayüzü, her seviyeden kullanıcıya (yeni başlayanlardan deneyimli geliştiricilere) iş görevlerini otomatikleştirme imkanı verir. İş akışı geliştirme deneyimi, Copilot sayesinde Üretken AI ile geliştirilmiştir.

Power Automate'teki Copilot AI asistan özelliği, ihtiyacınız olan akış türünü ve akışınızın gerçekleştirmesini istediğiniz işlemleri tarif etmenizi sağlar. Copilot, tarifinize dayanarak bir akış oluşturur. Akışı ihtiyaçlarınıza göre özelleştirebilirsiniz. AI Copilot ayrıca, otomatikleştirmek istediğiniz görev için gerçekleştirmeniz gereken işlemleri oluşturur ve önerir. Bu derste, Power Automate'te akışların ne olduğu ve nasıl kullanılacağına daha sonra bakacağız. AI Copilot asistanı ile sohbet adımlarıyla işlemleri ihtiyaçlarınıza göre özelleştirebilirsiniz. Bu özellik Power Automate ana ekranından kolayca ulaşılabilir.

## Microsoft Copilot Studio ile Akıllı Ajanlar Oluşturma

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst) (eski adıyla Power Virtual Agents), kullanıcılar adına soruları cevaplayabilen, eylemler gerçekleştirebilen ve görevleri otomatikleştirebilen **AI ajanları** — sohbet tabanlı copilots — oluşturmak için düşük kodlu bir Power Platform üyesidir. Power Platform’un diğer parçaları gibi, bu ajanları görsel ve doğal dil öncelikli bir deneyimde oluşturursunuz: ajanınızın ne yapmasını istediğinizi tarif edersiniz ve Copilot Studio, talimatlarını, bilgisini ve eylemlerini yapılandırmanızda yardımcı olur.

Eğitim girişimimiz için, öğrencilerin derslerle ilgili sorularına cevap veren, ödev son teslim tarihlerine bakabilen ve hatta bir eğitmene e-posta gönderebilen — tüm bunları kod yazmadan yapabilen — bir ajan oluşturabilirsiniz.

İşte Copilot Studio’yu güçlü kılan en son özelliklerden bazıları:

- **Bilgilerinize dayalı üretken cevaplar**. Her sohbeti elle yazmak yerine, **bilgi kaynakları** — halka açık web siteleri, SharePoint, OneDrive, Dataverse, yüklenen dosyalar veya bağlayıcılar yoluyla kurumsal veriler — bağlayabilir ve ajan bu kaynaklardan temellendirilmiş cevaplar oluşturur.

- **Üretken orkestrasyon**. Katı tetikleyici ifadelerine bağlı kalmak yerine, ajan bir isteği yapay zeka ile anlayıp, karşılamak için hangi bilgi, konu ve eylemlerin birleştirileceğine dinamik olarak karar verir, birkaç adımı zincirleme yapabilir.

- **Eylemler ve bağlayıcılar**. Ajanlar sadece sohbet etmekle kalmaz, aynı zamanda hareket de edebilirler. 1.500'den fazla önceden oluşturulmuş Power Platform bağlayıcıları, Power Automate akışları, özel REST API'leri, istemler veya **Model Context Protocol (MCP)** sunucuları ile desteklenmiş eylemler verebilirsiniz.

- **Otonom ajanlar**. Ajanlar sadece sohbet penceresinde yanıt vermekle sınırlı değildir. Yeni bir e-posta, Dataverse'e yeni bir kayıt ya da yüklenen bir dosya gibi olaylarla tetiklenen **otonom ajanlar** oluşturabilir ve ardından bir görevi tamamlamak için arka planda hareket ederler.

- **Çoklu ajan orkestrasyonu**. Ajanlar diğer ajanları çağırabilir. Bir Copilot Studio ajanı, Microsoft 365 Copilot'a yayınlanan veya Microsoft Foundry'de oluşturulan diğer ajanlara devredebilir veya onları genişletebilir.

- **Model seçimi**. Yerleşik modellerin ötesinde, agentınızın nasıl düşünmesi ve yanıtlamasını özelleştirmek için Microsoft Foundry model kataloğundan modeller getirebilirsiniz.

- **Her yere yayınlama**. Bir ajan oluşturulduktan sonra, Microsoft Teams, Microsoft 365 Copilot, bir web sitesi veya özel bir uygulama gibi birden çok kanala — güvenlik, kimlik doğrulama ve analitik Power Platform yönetim deneyimi üzerinden yönetilerek — yayınlanabilir.

İlk ajanınızı oluşturmaya [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) adresinden başlayabilir ve [Microsoft Copilot Studio dokümantasyonunda](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst) daha fazla bilgi edinebilirsiniz.

## Ödev: Girişimimiz için öğrenci ödevlerini ve faturaları Copilot kullanarak yönetin

Girişimimiz öğrencilere çevrim içi kurslar sunmaktadır. Girişim hızla büyüdü ve şimdi kurs taleplerine ayak uydurmakta zorlanıyor. Girişim, öğrenci ödevlerini ve faturalarını yönetmelerine yardımcı olacak düşük kodlu bir çözüm geliştirmek üzere sizi Power Platform geliştiricisi olarak işe aldı. Çözümlerine, öğrenci ödevlerini bir uygulama aracılığıyla takip edip yönetebilen ve fatura işleme sürecini bir iş akışı ile otomatikleştirebilen bir sistem kazandırmak istiyorlar. Size üretilen AI’yı kullanarak bu çözümü geliştirmeniz talep edildi.

Copilot kullanmaya başladığınızda, [Power Platform Copilot İstem Kütüphanesini](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) istemlere başlamak için kullanabilirsiniz. Bu kütüphane, Copilot ile uygulama ve akış oluşturmak için kullanabileceğiniz istemlerin bir listesini içerir. Ayrıca, Copilot'a gereksinimlerinizi nasıl tarif edeceğiniz hakkında fikir edinmek için de yararlıdır.

### Girişimimiz için Öğrenci Ödev Takipçisi Uygulaması Oluşturun

Girişimimizdeki öğretmenler öğrenci ödevlerini takip etmekte zorlanıyorlar. Ödevleri takip etmek için bir elektronik tablo kullanıyorlardı ama öğrenci sayısı artınca yönetmek zorlaştı. Onlar, öğrenci ödevlerini takip edip yönetmelerine yardımcı olacak bir uygulama yapmanızı istiyorlar. Uygulama, yeni ödev ekleme, ödevleri görüntüleme, güncelleme ve silme işlemlerini yapabilmelidir. Ayrıca öğretmenler ve öğrenciler, notlandırılmış ve notlandırılmamış ödevleri görebilmelidir.

Uygulamayı, Power Apps'te Copilot kullanarak aşağıdaki adımlarla oluşturacaksınız:

1. [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) ana ekranına gidin.

1. Ana ekrandaki metin alanını kullanarak oluşturmak istediğiniz uygulamayı tarif edin. Örneğin, **_Öğrenci ödevlerini takip ve yönetmek için bir uygulama oluşturmak istiyorum_**. Ardından **Gönder** düğmesine tıklayarak istemi AI Copilot'a gönderin.

![Oluşturmak istediğiniz uygulamayı tarif edin](../../../translated_images/tr/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. AI Copilot, takip etmek istediğiniz verileri depolamak için gereken alanlar ve örnek veriler içeren bir Dataverse Tablosu önerir. Ardından, bu tabloyu, sohbet adımlarıyla AI Copilot asistanını kullanarak ihtiyaçlarınıza göre özelleştirebilirsiniz.

   > **Önemli**: Dataverse, Power Platform’un altında yatan veri platformudur. Uygulamaların verilerini depolamak için düşük kodlu bir veri platformudur. Microsoft Bulutu’nda güvenli bir şekilde verilere sahip tam yönetilen bir hizmettir ve Power Platform ortamınız içinde sağlanır. Veri sınıflandırması, veri kökeni takibi, ayrıntılı erişim kontrolü gibi yerleşik veri yönetişimi özellikleri içerir. Dataverse hakkında daha fazla bilgiyi [buradan](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko) öğrenebilirsiniz.

   ![Yeni tablonuzdaki önerilen alanlar](../../../translated_images/tr/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. Öğretmenler, ödevlerini teslim eden öğrencilere, ödevlerin ilerleyişi hakkında güncelleme yapmak için e-postalar gönderme ihtiyacı duyuyor. Copilot’u kullanarak öğrenci e-postasını depolamak için tabloya yeni bir alan ekleyebilirsiniz. Örneğin şu istemi kullanabilirsiniz: **_Öğrenci e-postasını depolamak için bir sütun eklemek istiyorum_**. Ardından **Gönder** düğmesine tıklayarak istemi AI Copilot’a gönderin.

![Yeni alan ekleme](../../../translated_images/tr/copilot-new-column.35e15ff21acaf274.webp)

1. AI Copilot yeni alanı oluşturacak ve siz alanı ihtiyaçlarınıza göre özelleştirebileceksiniz.


1. Tabloyu tamamladıktan sonra, uygulamayı oluşturmak için **Uygulamayı oluştur** düğmesine tıklayın.

1. AI Copilot, açıklamanıza dayalı olarak duyarlı bir Canvas uygulaması oluşturacaktır. Ardından uygulamayı ihtiyaçlarınıza göre özelleştirebilirsiniz.

1. Eğitimcilerin öğrencilere e-posta göndermesi için, Copilot’u kullanarak uygulamaya yeni bir ekran ekleyebilirsiniz. Örneğin, uygulamaya yeni bir ekran eklemek için şu istemi kullanabilirsiniz: **_Öğrencilere e-posta göndermek için bir ekran eklemek istiyorum_**. İstemi AI Copilot’a göndermek için **Gönder** düğmesine tıklayın.

![Bir istem talimatı ile yeni ekran ekleme](../../../translated_images/tr/copilot-new-screen.2e0bef7132a17392.webp)

1. AI Copilot yeni bir ekran oluşturacaktır ve ardından ekranı ihtiyaçlarınıza göre özelleştirebilirsiniz.

1. Uygulamayı tamamladıktan sonra, uygulamayı kaydetmek için **Kaydet** düğmesine tıklayın.

1. Uygulamayı eğitimcilerle paylaşmak için **Paylaş** düğmesine tıklayın ve ardından tekrar **Paylaş** düğmesine tıklayın. Ardından uygulamayı eğitimcilerle e-posta adreslerini girerek paylaşabilirsiniz.

> **Ödeviniz**: Az önce oluşturduğunuz uygulama iyi bir başlangıçtır ancak geliştirilebilir. E-posta özelliği ile eğitimciler yalnızca e-posta adreslerini yazarak öğrencilere manuel olarak e-posta gönderebilmektedir. Copilot’u kullanarak eğitimcilerin ödevlerini teslim ettiklerinde öğrencilere otomatik olarak e-posta göndermelerini sağlayacak bir otomasyon oluşturabilir misiniz? İpucunuz: doğru istemle Power Automate'te Copilot'u kullanabilirsiniz.

### Startup'ımız için Fatura Bilgi Tablosu Oluşturma

Startup'ımızın finans ekibi fatura takibinde zorlanıyor. Faturaları takip etmek için bir elektronik tablo kullanıyorlardı ancak fatura sayısının artmasıyla bu yönetilmesi zor hale geldi. Aldıkları faturaların bilgilerini depolamaya, takip etmeye ve yönetmeye yardımcı olacak bir tablo oluşturmanızı istediler. Bu tablo, tüm fatura bilgilerini çıkaracak ve tabloya depolayacak bir otomasyon oluşturmak için kullanılmalıdır. Ayrıca tablo, finans ekibinin ödenmiş ve ödenmemiş faturaları görmesini sağlamalıdır.

Power Platform’un temelinde, uygulamalarınız ve çözümleriniz için veri depolamanızı sağlayan Dataverse adlı bir veri platformu vardır. Dataverse, uygulamanızın verilerini saklamak için düşük kodlu bir veri platformu sağlar. Microsoft Bulut’ta verileri güvenli bir şekilde depolayan ve Power Platform ortamınızda kullanıma sunulan tamamen yönetilen bir hizmettir. Veri sınıflandırması, veri kökeni, ince taneli erişim kontrolü gibi yerleşik veri yönetişimi yetenekleriyle birlikte gelir. Daha fazla bilgi için [buradan Dataverse'i öğrenebilirsiniz](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Startup'ımız için neden Dataverse kullanmalıyız? Dataverse içindeki standart ve özel tablolar, verileriniz için güvenli ve bulut tabanlı bir depolama seçeneği sunar. Tablolar, bir Excel çalışma kitabındaki birden çok çalışma sayfası kullanmaya benzer şekilde farklı veri türlerini saklamanızı sağlar. Tabloyu, kuruluşunuzun veya işletmenizin belirli ihtiyaçlarına uygun verileri saklamak için kullanabilirsiniz. Startup’ımızın Dataverse kullanarak elde edeceği bazı faydalar şunlardır ancak bunlarla sınırlı değildir:

- **Kolay yönetim**: Hem öznitelikler hem de veriler bulutta depolandığı için nasıl saklandıkları veya yönetildikleri konusunda endişelenmenize gerek yoktur. Uygulamalarınızı ve çözümlerinizi oluşturmaya odaklanabilirsiniz.

- **Güvenli**: Dataverse, verileriniz için güvenli ve bulut tabanlı bir depolama seçeneği sağlar. Rollere dayalı güvenlik kullanarak tablolarınızdaki verilere kimin erişebileceğini ve nasıl erişeceğini kontrol edebilirsiniz.

- **Zengin öznitelik**: Veri türleri ve ilişkiler doğrudan Power Apps içinde kullanılır

- **Mantık ve doğrulama**: İş kurallarını, hesaplanmış alanları ve doğrulama kurallarını kullanarak iş mantığını uygulayabilir ve veri doğruluğunu koruyabilirsiniz.

Artık Dataverse’in ne olduğunu ve neden kullanmanız gerektiğini bildiğinize göre, finans ekibimizin ihtiyaçlarını karşılamak için Dataverse'te bir tablo oluşturmak için Copilot’u nasıl kullanabileceğinize bakalım.

> **Not** : Bu tabloyu bir sonraki bölümde tüm fatura bilgilerini çıkaracak ve tabloya depolayacak bir otomasyon oluşturmak için kullanacaksınız.

Copilot kullanarak Dataverse’te tablo oluşturmak için aşağıdaki adımları izleyin:

1. [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst) ana ekranına gidin.

2. Sol gezinme çubuğunda **Tablolar** seçeneğine tıklayın ve ardından **Yeni tabloyu tanımla** düğmesini seçin.

![Yeni tabloyu seçin](../../../translated_images/tr/describe-new-table.0792373eb757281e.webp)

1. **Yeni tabloyu tanımla** ekranında, oluşturmak istediğiniz tabloyu tanımlamak için metin alanını kullanın. Örneğin, **_Fatura bilgilerini depolamak için bir tablo oluşturmak istiyorum_**. İstemi AI Copilot’a göndermek için **Gönder** düğmesine tıklayın.

![Tabloyu tanımla](../../../translated_images/tr/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. AI Copilot, takip etmek istediğiniz verileri depolamak için gereken alanlarla birlikte bir Dataverse Tablosu ve bazı örnek veriler önerecektir. Ardından AI Copilot asistan özelliğini kullanarak sohbet adımlarıyla tabloyu ihtiyaçlarınıza göre özelleştirebilirsiniz.

![Önerilen Dataverse tablosu](../../../translated_images/tr/copilot-dataverse-table.b3bc936091324d9d.webp)

1. Finans ekibi, tedarikçiye faturalarının mevcut durumu hakkında güncelleme yapmak için e-posta göndermek istiyor. Tedarikçi e-postasını saklamak için tabloya yeni bir alan eklemek üzere Copilot’u kullanabilirsiniz. Örneğin, tabloya yeni bir alan eklemek için şu istemi kullanabilirsiniz: **_Tedarikçi e-postasını saklamak için bir sütun eklemek istiyorum_**. İstemi AI Copilot’a göndermek için **Gönder** düğmesine tıklayın.

1. AI Copilot yeni bir alan oluşturacaktır ve ardından alanı ihtiyaçlarınıza göre özelleştirebilirsiniz.

1. Tabloyu tamamladıktan sonra, tabloyu oluşturmak için **Oluştur** düğmesine tıklayın.

## Power Platform'da AI Builder ile AI Modelleri

AI Builder, Power Platform’da bulunan düşük kodlu bir AI yeteneğidir ve süreçlerinizi otomatikleştirmeniz ve sonuçları tahmin etmeniz için AI Modelleri kullanmanızı sağlar. AI Builder ile, Dataverse veya SharePoint, OneDrive ya da Azure gibi çeşitli bulut veri kaynaklarında verilerinize bağlanan uygulamalarınız ve akışlarınızda AI teknolojisini kullanabilirsiniz.

## Önceden Oluşturulmuş AI Modelleri vs Özel AI Modelleri

AI Builder, Önceden Oluşturulmuş AI Modelleri ve Özel AI Modelleri olmak üzere iki tür AI Modeli sağlar. Önceden Oluşturulmuş AI Modelleri, Microsoft tarafından eğitilmiş ve Power Platform'da kullanıma hazır modellerdir. Bu modeller, kendi modellerinizi oluşturup eğitmek ve yayımlamak zorunda kalmadan uygulamalarınıza ve akışlarınıza zeka katmanıza yardımcı olur. Bu modelleri süreçleri otomatikleştirmek ve sonuçları tahmin etmek için kullanabilirsiniz.

Power Platform’da bulunan bazı Önceden Oluşturulmuş AI Modelleri şunlardır:

- **Anahtar İfade Çıkarımı**: Bu model metinden anahtar ifadeleri çıkarır.
- **Dil Tespiti**: Bu model bir metnin dilini tespit eder.
- **Duygu Analizi**: Bu model metindeki olumlu, olumsuz, nötr veya karışık duyguyu tespit eder.
- **Kartvizit Okuyucu**: Bu model kartvizitlerden bilgi çıkarır.
- **Metin Tanıma**: Bu model görüntülerden metin çıkarır.
- **Nesne Algılama**: Bu model görüntülerden nesneleri algılar ve çıkarır.
- **Doküman işleme**: Bu model formlardan bilgi çıkarır.
- **Fatura İşleme**: Bu model faturalardan bilgi çıkarır.

Özel AI Modelleri ile kendi modelinizi AI Builder’a getirerek, kendi verilerinizle modeli eğitmenize imkan sağlar ve model, diğer AI Builder özel modelleri gibi işlev görür. Bu modelleri hem Power Apps hem de Power Automate’de süreçleri otomatikleştirmek ve sonuçları tahmin etmek için kullanabilirsiniz. Kendi modelinizi kullanırken bazı sınırlamalar geçerlidir. Bu sınırlamaları [buradan](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst) okuyabilirsiniz.

![AI builder modelleri](../../../translated_images/tr/ai-builder-models.8069423b84cfc47f.webp)

## Ödev #2 - Startup'ımız için Fatura İşleme Akışı Oluşturma

Finans ekibi fatura işlemede zorlanıyor. Faturaları takip etmek için bir elektronik tablo kullanıyorlardı ancak fatura sayısının artmasıyla bu yönetimi zorlaştırıyor. AI kullanarak faturaları işleme konusunda onlara yardımcı olacak bir iş akışı oluştarmanızı istediler. İş akışı, faturalarından bilgileri çıkarıp bu bilgileri bir Dataverse tablosunda depolayabilmelidir. Ayrıca iş akışı, çıkarılan bilgilerle finans ekibine e-posta göndermeyi sağlamalıdır.

Artık AI Builder’ın ne olduğunu ve neden kullanmanız gerektiğini bildiğinize göre, daha önce öğrendiğimiz gibi AI Builder’daki Fatura İşleme AI Modelini kullanarak finans ekibinin faturaları işlemesine yardımcı olacak bir iş akışını nasıl oluşturabileceğinize bakalım.

AI Builder’daki Fatura İşleme AI Modelini kullanarak finans ekibinin faturaları işlemesine yardımcı olacak bir iş akışı oluşturmak için aşağıdaki adımları izleyin:

1. [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst) ana ekranına gidin.

2. Ana ekrandaki metin alanını iş akışınızı tanımlamak için kullanın. Örneğin, **_Posta kutuma gelen bir faturayı işle_**. İstemi AI Copilot’a göndermek için **Gönder** düğmesine tıklayın.

   ![Copilot power automate](../../../translated_images/tr/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. AI Copilot, otomatikleştirmek istediğiniz görevi gerçekleştirmek için gereken eylemleri önerecektir. Sonraki adımlara geçmek için **İleri** düğmesine tıklayabilirsiniz.

4. Bir sonraki adımda, Power Automate akış için gerekli bağlantıları kurmanız için sizi yönlendirecektir. Tamamladıktan sonra iş akışını oluşturmak için **Akış oluştur** düğmesine tıklayın.

5. AI Copilot, bir akış oluşturacak ve ardından akışı ihtiyaçlarınıza göre özelleştirebilirsiniz.

6. Akışın tetikleyicisini güncelleyin ve **Klasör**ü faturaların depolanacağı klasöre ayarlayın. Örneğin, klasörü **Gelen Kutusu** olarak belirleyebilirsiniz. **Gelişmiş seçenekleri göster** seçeneğine tıklayın ve **Yalnızca Ekleri Olan** seçeneğini **Evet** olarak ayarlayın. Bu, akışın yalnızca ekli bir e-posta bu klasöre geldiğinde çalışmasını sağlar.

7. Akıştan aşağıdaki eylemleri kaldırın: **HTML'den metin**, **Oluştur**, **Oluştur 2**, **Oluştur 3** ve **Oluştur 4** çünkü bunları kullanmayacaksınız.

8. Akıştan **Koşul** eylemini kaldırın çünkü bunu kullanmayacaksınız. Ekran görüntüsü aşağıdaki gibi olmalıdır:

   ![power automate, eylemleri kaldır](../../../translated_images/tr/powerautomate-remove-actions.7216392fe684ceba.webp)

9. **Bir eylem ekle** düğmesine tıklayın ve **Dataverse** arayın. **Yeni bir satır ekle** eylemini seçin.

10. **Faturalardan Bilgi Çıkar** eyleminde, **Fatura Dosyası**nı e-postadan gelen **Ek İçeriği** olarak güncelleyin. Bu, akışın fatura ekinden bilgi çıkarmasını sağlayacaktır.

11. Daha önce oluşturduğunuz **Tablo**yu seçin. Örneğin, **Fatura Bilgi** tablosunu seçebilirsiniz. Aşağıdaki alanları doldurmak için önceki eylemden dinamik öğeleri seçin:

    - Kimlik (ID)
    - Tutar (Amount)
    - Tarih (Date)
    - İsim (Name)
    - Durum - **Durum**u **Beklemede** olarak ayarlayın.
    - Tedarikçi E-postası - **Yeni bir e-posta geldiğinde** tetikleyicisinden **Kimden** dinamik içeriğini kullanın.

    ![power automate satır ekle](../../../translated_images/tr/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. Akışı tamamladıktan sonra **Kaydet** düğmesine tıklayarak akışı kaydedin. Ardından, e-postanıza fatura ekli bir e-posta göndererek akışı test edebilirsiniz.

> **Ödeviniz**: Az önce oluşturduğunuz akış iyi bir başlangıçtır, şimdi finans ekibimizin tedarikçiye faturalarının mevcut durumu hakkında güncelleme göndermesini sağlayacak bir otomasyon nasıl oluşturabileceğinizi düşünmelisiniz. İpucunuz: Akış, fatura durumunda değişiklik olduğunda çalışmalıdır.

## Power Automate'te Metin Üretimi AI Modeli kullanımı

AI Builder’daki GPT ile Metin Oluşturma AI Modeli, bir isteme dayalı metin oluşturmanızı sağlar ve Microsoft Azure OpenAI Hizmeti tarafından desteklenir. Bu yetenekle, GPT (Generative Pre-Trained Transformer) teknolojisini uygulamalarınıza ve akışlarınıza entegre ederek çeşitli otomatik akışlar ve sezgisel uygulamalar oluşturabilirsiniz.

GPT modelleri, geniş veri kümeleri üzerinde kapsamlı eğitimden geçer ve bir istem sunulduğunda insan diline çok yakın metin üretir. İş akışı otomasyonuyla entegre edildiğinde, GPT gibi AI modelleri geniş görevlerin otomatikleştirilmesi ve kolaylaştırılması için kullanılabilir.

Örneğin, e-postalar taslakları, ürün açıklamaları ve daha fazlası gibi çeşitli kullanım senaryoları için otomatik metin oluşturma akışları oluşturabilir, ayrıca GPT modelini sohbet botları ve müşteri hizmetleri uygulamaları gibi müşteri sorgularına etkili ve verimli yanıt vermeyi sağlayan uygulamalarda kullanabilirsiniz.

![bir istem oluştur](../../../translated_images/tr/create-prompt-gpt.69d429300c2e870a.webp)


Power Automate'te bu Yapay Zeka Modelini nasıl kullanacağınızı öğrenmek için [Yapay Zeka Oluşturucu ve GPT ile zekâ ekleme](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko) modülünü inceleyin.

## Harika İş! Öğrenmeninize Devam Edin

Bu dersi tamamladıktan sonra, Üretken Yapay Zeka bilginizi geliştirmeye devam etmek için [Üretken Yapay Zeka Öğrenme koleksiyonumuzu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) inceleyin!

Copilot'u özelleştirmek ve daha fazla fayda sağlamak mı istiyorsunuz? GitHub Copilot'dan en iyi şekilde yararlanmanıza yardımcı olacak talimatlar, ajanlar, yetenekler ve yapılandırmaların toplandığı, topluluk katkılı [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) koleksiyonunu keşfedin.

Üretken Yapay Zekayı Fonksiyon Çağırma ile nasıl entegre edeceğimizi göreceğimiz Ders 11'e geçin: [Fonksiyon Çağırma ile Entegrasyon](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->