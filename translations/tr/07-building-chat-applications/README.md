# Üretken AI Destekli Sohbet Uygulamaları Geliştirme

[![Üretken AI Destekli Sohbet Uygulamaları Geliştirme](../../../translated_images/tr/07-lesson-banner.a279b937f2843833.webp)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Bu dersin videosunu izlemek için yukarıdaki görsele tıklayın)_

Artık metin üretimi uygulamalarını nasıl inşa edebileceğimizi gördüğümüze göre, sohbet uygulamalarına göz atalım.

Sohbet uygulamaları, yalnızca gündelik konuşma aracı olmaktan öteye geçerek günlük hayatımıza entegre oldu. Müşteri hizmetleri, teknik destek ve hatta sofistike danışmanlık sistemlerinin ayrılmaz parçaları haline geldiler. Muhtemelen çok uzun zaman olmadan bir sohbet uygulamasından yardım aldınız. Bu platformlara üretken AI gibi daha gelişmiş teknolojileri entegre ettikçe, karmaşıklık ve beraberinde zorluklar da artar.

Cevaplandırmamız gereken bazı sorular şunlardır:

- **Uygulama geliştirme.** Bu AI destekli uygulamaları belirli kullanım durumları için nasıl verimli ve sorunsuz bir şekilde inşa edip entegre edebiliriz?
- **İzleme.** Dağıtım sonrası, uygulamaların işlevsellik ve [sorumlu AI'nın altı prensibine](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) uyum açısından en yüksek kalite düzeyinde çalıştığını nasıl izleyip garanti altına alabiliriz?

Otomasyon ve sorunsuz insan-makine etkileşimlerinin şekillendirdiği bir çağda ilerlerken, üretken AI'nın sohbet uygulamalarının kapsamını, derinliğini ve uyarlanabilirliğini nasıl dönüştürdüğünü anlamak zorunlu hale geliyor. Bu ders, bu karmaşık sistemleri destekleyen mimari yönleri inceleyecek, alan-spesifik görevler için ince ayar metodolojilerine değinecek ve sorumlu AI dağıtımını sağlamak için ilgili metrikleri ve değerlendirme kriterlerini ele alacak.

## Giriş

Bu ders şunları kapsar:

- Sohbet uygulamalarını verimli şekilde inşa etme ve entegre etme teknikleri.
- Uygulamalara özelleştirme ve ince ayar yapma yöntemleri.
- Sohbet uygulamalarını etkili bir şekilde izlemek için stratejiler ve dikkate alınması gerekenler.

## Öğrenme Hedefleri

Bu dersin sonunda, şunları yapabilmeniz beklenir:

- Sohbet uygulamalarını mevcut sistemlere entegre ederken dikkat edilmesi gerekenleri tanımlayabilmek.
- Sohbet uygulamalarını özel kullanım durumları için özelleştirebilmek.
- AI destekli sohbet uygulamalarının kalitesini etkili şekilde izlemek ve korumak için temel metrikleri ve değerlendirme kriterlerini belirleyebilmek.
- Sohbet uygulamalarında AI'nın sorumlu şekilde kullanılmasını sağlayabilmek.

## Üretken AI'nın Sohbet Uygulamalarına Entegrasyonu

Sohbet uygulamalarını üretken AI ile geliştirmek yalnızca onları daha akıllı yapmakla ilgili değildir; mimari yapılarını, performanslarını ve kullanıcı arayüzlerini optimize ederek kaliteli bir kullanıcı deneyimi sunmakla ilgilidir. Bu, mimari temellerin, API entegrasyonlarının ve kullanıcı arayüzü hususlarının araştırılmasını kapsar. Bu bölüm, ister mevcut sistemlere entegre ediyor olun, ister bağımsız platformlar olarak inşa edin, bu karmaşık alanlarda size kapsamlı bir rehberlik sunmayı amaçlamaktadır.

Bölüm sonunda, sohbet uygulamalarını verimli şekilde inşa etme ve entegre etme konusunda uzmanlığa sahip olacaksınız.

### Sohbet Botu (Chatbot) mu, Sohbet Uygulaması mı?

Sohbet uygulamalarını inşa etmeye dalmadan önce, farklı roller ve işlevlere sahip olan ‘chatbotlar’ ile ‘AI destekli sohbet uygulamalarını’ karşılaştıralım. Bir chatbotun ana amacı, sık sorulan soruları yanıtlamak veya bir paketin takibini yapmak gibi belirli konuşma görevlerinin otomasyonudur. Genellikle kural tabanlı mantık veya karmaşık AI algoritmaları tarafından yönetilir. Buna karşılık, AI destekli sohbet uygulaması, insan kullanıcılar arasında metin, ses ve video sohbetleri gibi çeşitli dijital iletişim biçimlerini kolaylaştırmak üzere tasarlanmış çok daha geniş kapsamlı bir ortamdır. Ayırt edici özelliği, çok çeşitli girdi ve bağlamsal ipuçlarına dayanarak yanıtlar üreten, ince detaylı insan benzeri sohbetleri taklit eden üretken AI modelinin entegrasyonudur. Üretken AI destekli sohbet uygulaması, açık alan tartışmalarına katılabilir, gelişen sohbet bağlamlarına uyum sağlayabilir ve hatta yaratıcı ya da karmaşık diyaloglar oluşturabilir.

Aşağıdaki tablo, benzersiz dijital iletişim rollerini anlamamıza yardımcı olmak için temel farkları ve benzerlikleri özetlemektedir.

| Chatbot                               | Üretken AI Destekli Sohbet Uygulaması      |
| ------------------------------------- | -------------------------------------- |
| Görev Odaklı ve kural bazlı           | Bağlam farkındalığına sahip              |
| Çoğu zaman daha büyük sistemlere entegre  | Bir veya birden fazla chatbot barındırabilir   |
| Programlanmış işlevlerle sınırlı        | Üretken AI modellerini içerir            |
| Uzmanlaşmış ve yapılandırılmış etkileşimler | Açık alan tartışmalarına uygun          |

### SDK ve API ile önceden oluşturulmuş işlevleri kullanmak

Bir sohbet uygulaması geliştirirken, mevcut olanları değerlendirmek iyi bir ilk adımdır. Sohbet uygulamalarını SDK ve API kullanarak oluşturmak çeşitli avantajlara sahiptir. İyi dokümante edilmiş SDK ve API'leri entegre ederek, uygulamanızın uzun vadeli başarısı için stratejik bir konum elde etmiş olursunuz ve ölçeklenebilirlik ile bakım endişelerini yönetirsiniz.

- **Geliştirme sürecini hızlandırır ve yükü azaltır**: Önceden oluşturulmuş işlevlere güvenmek, bunları kendiniz kurarken harcanacak maliyeti azaltır ve böylece iş uygulamanızın daha önemli olarak gördüğünüz diğer alanlarına (örneğin iş mantığı) odaklanmanızı sağlar.
- **Daha iyi performans**: İşlevleri sıfırdan geliştirirken sonunda "Nasıl ölçeklendirilir? Bu uygulama ani kullanıcı artışlarını kaldırabilir mi?" sorularını sorarsınız. İyi yönetilen SDK ve API'lerde bu endişelere yönelik yerleşik çözümler bulunur.
- **Bakımı kolaydır**: Çoğu API ve SDK, yeni sürüm yayinlandığında sadece kütüphanenin güncellenmesini gerektirdiği için güncellemeler ve iyileştirmeler kolayca yapılabilir.
- **En yeni teknolojilere erişim**: Geniş veri setleri üzerinde ince ayar yapılmış ve eğitilmiş modelleri kullanmak, uygulamanıza doğal dil yetenekleri kazandırır.

Bir SDK veya API işlevselliğine erişim genellikle benzersiz bir anahtar veya kimlik doğrulama belirteci kullanarak sağlanır. Bunu keşfetmek için OpenAI Python Kütüphanesini kullanacağız. Ayrıca bu dersi kendi başınıza deneyimlemek için aşağıdaki [OpenAI için not defteri](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) veya [Azure OpenAI Hizmetleri için not defteri](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) mevcuttur.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

response = client.responses.create(model="gpt-4o-mini", input="Suggest two titles for an instructional lesson on chat applications for generative AI.", store=False)
print(response.output_text)
```

Yukarıdaki örnek, yanıta tamamlamak üzere GPT-4o mini modelini Responses API ile kullanır, ancak API anahtarı önceden ayarlanmıştır. Anahtar ayarlanmazsa hata alırsınız.

## Kullanıcı Deneyimi (UX)

Genel UX prensipleri sohbet uygulamalarına uygulanır, ancak burada makine öğrenimi bileşenleri nedeniyle özellikle önemli bazı ek hususlar vardır.

- **Belirsizliği giderme mekanizması**: Üretken AI modelleri zaman zaman belirsiz cevaplar üretebilir. Kullanıcıların açıklama istemesine izin veren bir özellik bu sorunun üstesinden gelmede yardımcı olabilir.
- **Bağlamın korunması**: Gelişmiş üretken AI modellerinin bir konuşma içindeki bağlamı hatırlayabilme yeteneği vardır ve bu kullanıcı deneyimi için gerekli bir varlık olabilir. Kullanıcıların bağlamı kontrol edip yönetebilmesi deneyimi iyileştirir, ancak hassas kullanıcı bilgilerini tutma riski doğurur. Bilginin ne kadar süre saklanacağı gibi hususlar (örneğin, saklama politikaları getirerek) bağlama duyulan ihtiyaç ile gizlilik arasındaki dengeyi sağlar.
- **Kişiselleştirme**: Öğrenip uyum sağlama yeteneğine sahip AI modelleri, kullanıcıya özel bir deneyim sunar. Kullanıcı profilleri gibi özelliklerle deneyimin kişiselleştirilmesi, kullanıcının anlaşıldığını hissetmesini sağlamakla kalmaz, aynı zamanda spesifik cevapları bulmasını kolaylaştırır ve etkileşimi daha verimli ve tatmin edici hale getirir.

Kişiselleştirmeye bir örnek olarak OpenAI'nin ChatGPT'sindeki "Özel talimatlar" ayarları gösterilebilir. Buradan, istemleriniz için önemli olabilecek sizinle ilgili bilgileri girebilirsiniz. İşte bir özel talimat örneği.

![ChatGPT Özel Talimatlar Ayarları](../../../translated_images/tr/custom-instructions.b96f59aa69356fcf.webp)

Bu "profil", ChatGPT'ye bağlı listeler hakkında bir ders planı oluşturmasını söyler. ChatGPT’nin kullanıcının deneyimine dayanarak daha ayrıntılı bir ders planı isteyebileceğini dikkate aldığını fark edin.

![ChatGPT'de bağlı listeler hakkında bir ders planı için istem](../../../translated_images/tr/lesson-plan-prompt.cc47c488cf1343df.webp)

### Büyük Dil Modelleri için Microsoft Sistem Mesaj Çerçevesi

[Microsoft, LLM'lerden yanıt üretirken etkili sistem mesajları yazılması için rehberlik sağlamıştır](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst), bu rehber dört alana ayrılmıştır:

1. Modelin kim için olduğu ve yetenekleri ile sınırlamalarının tanımlanması.
2. Modelin çıktı formatının belirlenmesi.
3. Modelin amaçlanan davranışını gösteren spesifik örneklerin sağlanması.
4. Ek davranışsal koruyucu önlemlerin sağlanması.

### Erişilebilirlik

Kullanıcı görsel, işitsel, motor veya bilişsel engellere sahip olsun, iyi tasarlanmış bir sohbet uygulaması herkes tarafından kullanılabilir olmalıdır. Aşağıdaki liste, çeşitli kullanıcı engellerine yönelik erişilebilirliği artırmak için tasarlanmış özellikleri detaylandırır.

- **Görme Engeli için Özellikler**: Yüksek kontrast temalar ve yeniden boyutlandırılabilir metin, ekran okuyucu uyumluluğu.
- **İşitme Engeli için Özellikler**: Metinden sese ve sesten metne işlevleri, ses bildirimleri için görsel ipuçları.
- **Motor Engeli için Özellikler**: Klavye navigasyon desteği, sesli komutlar.
- **Bilişsel Engeli için Özellikler**: Basitleştirilmiş dil seçenekleri.

## Alan-Spesifik Dil Modelleri için Özelleştirme ve İnce Ayar

Şirketinizin jargonunu anlayan ve kullanıcılarının sıkça sorduğu belirli soruları önceden tahmin eden bir sohbet uygulamasını hayal edin. Bahsetmeye değer birkaç yaklaşım vardır:

- **DSL modellerinden yararlanma**. DSL, alan-spesifik dil anlamına gelir. Belirli bir alan için eğitilmiş bir DSL modeli, o alanın kavramlarını ve senaryolarını anlamak üzere kullanılabilir.
- **İnce ayar uygulama**. İnce ayar, modelinizi özel verilerle daha ileriye taşıma işlemidir.

## Özelleştirme: Bir DSL Kullanmak

Alan-spesifik dil modellerinden (DSL Modelleri) yararlanmak, uzmanlaşmış ve bağlamsal olarak ilgili etkileşimler sağlayarak kullanıcı bağlılığını artırabilir. Bu, belirli bir alan, sektör veya konuya ilişkin metni anlamak ve üretmek üzere eğitilen veya ince ayar yapılan bir modeldir. Bir DSL modeli kullanma seçenekleri sıfırdan eğitmeyi, SDK ve API'ler yoluyla mevcut modelleri kullanmayı içerebilir. Diğer bir seçenek ise, önceden eğitilmiş bir modeli alıp belirli bir alan için uyarlamak olan ince ayardır.

## Özelleştirme: İnce Ayar Uygulama

İnce ayar, önceden eğitilmiş bir modelin uzman bir alan veya belirli bir görev için yetersiz kaldığı durumlarda sıklıkla düşünülür.

Örneğin, tıbbi sorular karmaşıktır ve çok bağlam gerektirir. Bir sağlık profesyonelinin hastayı teşhis etmesi, yaşam tarzı veya önceden var olan durumlar gibi çeşitli faktörlere dayanabilir ve teşhisini doğrulamak için güncel tıbbi dergilere başvurabilir. Böyle nüanslı senaryolarda, genel amaçlı AI sohbet uygulaması güvenilir bir kaynak olamaz.

### Senaryo: bir tıbbi uygulama

Tedavi rehberlerine, ilaç etkileşimlerine veya güncel araştırma bulgularına hızlı referans sağlamak amacıyla tasarlanmış bir sohbet uygulamasını düşünün.

Temel tıbbi soruları yanıtlamak veya genel tavsiye vermek için genel amaçlı bir model yeterli olabilir, ancak aşağıdaki konularda zorlanabilir:

- **Çok özel veya karmaşık vakalar**. Örneğin, bir nörolog uygulamaya "Pediatrik hastalarda ilaç direncine sahip epilepsinin yönetiminde güncel en iyi uygulamalar nelerdir?" diye sorabilir.
- **Son gelişmelerden yoksunluk**. Genel amaçlı model, nöroloji ve farmakolojideki en son gelişmeleri içeren güncel cevapları vermekte zorlanabilir.

Bu gibi durumlarda, özel tıbbi bir veri setiyle modeli ince ayar yapmak, bu karmaşık tıbbi soruları daha doğru ve güvenilir şekilde yanıtlayabilme yeteneğini önemli ölçüde artırabilir. Bu, alan-spesifik zorlukları ve çözülmesi gereken soruları temsil eden büyük ve ilgili bir veri setine erişim gerektirir.

## Yüksek Kaliteli AI Destekli Sohbet Deneyimi için Dikkat Edilmesi Gerekenler

Bu bölüm, "yüksek kaliteli" sohbet uygulamaları için kriterleri özetler; bu kriterler hem uygulanabilir metriklerin yakalanmasını hem de AI teknolojisinin sorumlu kullanımını sağlayan bir çerçeveye uyumu içerir.

### Temel Metrikler

Uygulamanın yüksek kaliteli performansını sürdürmek için temel metrikler ve değerlendirme kriterlerini takip etmek önemlidir. Bu ölçümler sadece uygulamanın işlevselliğini garanti etmekle kalmaz, aynı zamanda AI modelinin ve kullanıcı deneyiminin kalitesini de değerlendirir. Aşağıda göz önünde bulundurmanız gereken temel, AI ve kullanıcı deneyimi metriklerinin bir listesi bulunmaktadır.

| Metrik                      | Tanım                                                                                                               | Sohbet Geliştiricisi için Dikkat Edilecekler                    |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------|
| **Çalışır Durum Süresi (Uptime)** | Uygulamanın kullanıcılar tarafından erişilebilir ve çalışır olduğu süreyi ölçer.                                    | Kesinti süresini nasıl minimize edeceksiniz?                     |
| **Yanıt Süresi**             | Uygulamanın kullanıcının sorgusuna yanıt vermesi için geçen süre.                                                    | Yanıt süresini iyileştirmek için sorgu işleme optimizasyonu nasıl yapılır? |
| **Doğruluk (Precision)**     | Gerçek pozitif tahminlerin toplam pozitif tahminlere oranı.                                                           | Modelinizin doğruluğunu nasıl doğrulayacaksınız?                 |
| **Duyarlılık (Recall, Sensitivity)** | Gerçek pozitif tahminlerin gerçek pozitiflerin toplamına oranı.                                                     | Duyarlılığı nasıl ölçecek ve artıracaksınız?                     |
| **F1 Skoru**                | Doğruluk ve duyarlılığın dengelendiği harmonik ortalama.                                                             | Hedef F1 skorunuz nedir? Doğruluk ve duyarlılık arasında nasıl denge kuracaksınız? |
| **Karışıklık (Perplexity)** | Modelin tahmin ettiği olasılık dağılımının veri kümesinin gerçek dağılımıyla ne kadar iyi eşleştiğini ölçer.           | Karışıklığı nasıl minimize edeceksiniz?                          |
| **Kullanıcı Memnuniyeti Metrikleri** | Kullanıcının uygulama algısını ölçer. Genellikle anket yoluyla toplanır.                                            | Ne sıklıkla kullanıcı geri bildirimi toplayacaksınız? Buna göre nasıl uyum sağlayacaksınız? |
| **Hata Oranı**              | Modelin anlamada veya çıktı üretiminde yaptığı hataların oranı.                                                        | Hata oranlarını azaltmak için hangi stratejilere sahipsiniz?    |
| **Yeniden Eğitim Döngüleri** | Modelin yeni veri ve bilgilerle güncellenme sıklığı.                                                                   | Modeli ne sıklıkla yeniden eğiteceksiniz? Yeniden eğitim döngüsünü ne tetikleyecek? |

| **Anomali Tespiti**         | Beklenen davranışa uymayan olağandışı kalıpları tanımlamak için araçlar ve teknikler.                        | Anomalilere nasıl yanıt vereceksiniz?                                        |

### Sohbet Uygulamalarında Sorumlu Yapay Zeka Uygulamalarını Gerçekleştirmek

Microsoft'un Sorumlu Yapay Zeka yaklaşımı, yapay zeka geliştirme ve kullanımını yönlendirmesi gereken altı ilkeyi belirlemiştir. Aşağıda ilkeler, tanımları ve bir sohbet geliştiricisinin dikkate alması gereken hususlar ile neden ciddi almaları gerektiği yer almaktadır.

| İlkeler               | Microsoft’un Tanımı                                | Sohbet Geliştiricisinin Dikkat Etmesi Gerekenler                       | Neden Önemlidir                                                                     |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Adillik               | Yapay zeka sistemleri tüm insanlara adil davranmalıdır.            | Sohbet uygulamasının kullanıcı verilerine dayanarak ayrımcılık yapmamasını sağla.  | Kullanıcılar arasında güven ve kapsayıcılık oluşturmak için; yasal sonuçlardan kaçınmak.                |
| Güvenilirlik ve Güvenlik | Yapay zeka sistemleri güvenilir ve güvenli performans göstermelidir.        | Hataları ve riskleri en aza indirmek için test ve hata önleme mekanizmaları uygula.         | Kullanıcı memnuniyetini sağlamak ve potansiyel zararları önlemek için.                                 |
| Gizlilik ve Güvenlik   | Yapay zeka sistemleri güvenli olmalı ve gizliliğe saygı duymalıdır.      | Güçlü şifreleme ve veri koruma önlemleri uygula.              | Hassas kullanıcı verilerini korumak ve gizlilik yasalarına uymak için.                         |
| Kapsayıcılık          | Yapay zeka sistemleri herkesi güçlendirmeli ve insanları dahil etmelidir. | Farklı kitleler için erişilebilir ve kullanımı kolay bir UI/UX tasarla. | Uygulamayı daha geniş bir yelpazede insanın etkin şekilde kullanmasını sağlar.                   |
| Şeffaflık           | Yapay zeka sistemleri anlaşılır olmalıdır.                  | Yapay zeka yanıtlarının net belgelenmesini ve mantığını sağla.            | Kararların nasıl alındığını anlayabiliyorlarsa kullanıcılar bir sisteme daha çok güvenir. |
| Hesap Verebilirlik         | İnsanlar yapay zeka sistemleri için hesap verebilir olmalıdır.          | Yapay zeka kararlarının denetlenmesi ve geliştirilmesi için net bir süreç oluştur.     | Hatalar durumunda sürekli iyileştirme ve düzeltici önlemler alınmasını sağlar.               |

## Ödev

[Ödeve](../../../07-building-chat-applications/python) bakın. İlk sohbet istemlerinizi çalıştırmaktan, metin sınıflandırma ve özetlemeye kadar bir dizi alıştırmadan geçirecek. Ödevlerin farklı programlama dillerinde mevcut olduğunu fark edin!

## Harika İş! Yolculuğa Devam Et

Bu dersi tamamladıktan sonra, Jeneratif Yapay Zeka bilginizi geliştirmeye devam etmek için [Jeneratif Yapay Zeka Öğrenme koleksiyonumuzu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) inceleyin!

Arama uygulamaları geliştirmeye nasıl başlayabileceğinizi görmek için Ders 8’e geçin [arama uygulamaları inşa etme](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->