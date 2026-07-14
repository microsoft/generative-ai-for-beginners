# Prompt Mühendisliğinin Temelleri

[![Prompt Engineering Fundamentals](../../../translated_images/tr/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Giriş
Bu modül, üretken yapay zeka modellerinde etkili promptlar oluşturmak için temel kavramlar ve teknikleri kapsar. Bir LLM’ye promptunuzu nasıl yazdığınız da önemlidir. Özenle hazırlanmış bir prompt daha iyi yanıt kalitesi elde edebilir. Peki _prompt_ ve _prompt mühendisliği_ gibi terimler tam olarak ne anlama geliyor? Ve LLM’ye gönderdiğim prompt _girişini_ nasıl iyileştirebilirim? Bu bölümde ve bir sonraki bölümde bu soruları cevaplamaya çalışacağız.

_Üretken Yapay Zeka_, kullanıcı taleplerine yanıt olarak yeni içerik (ör., metin, görsel, ses, kod vb.) oluşturabilir. Bunu, doğal dil ve kod kullanımı için eğitilmiş OpenAI’nin GPT ("Generative Pre-trained Transformer") serisi gibi _Büyük Dil Modelleri_ (Large Language Models) kullanarak başarır.

Kullanıcılar artık teknik bilgi veya eğitim gerektirmeden sohbet gibi tanıdık paradigmalarla bu modellerle etkileşime geçebilir. Modeller _prompt tabanlıdır_ - kullanıcılar bir metin girdisi (prompt) gönderir ve AI yanıtı (tamamlama) alır. Ardından yanıt beklentilerine uyana kadar iteratif, çok adımlı sohbetlerle "AI ile sohbet edebilirler".

"Promptlar" şimdi üretken yapay zeka uygulamalarının birincil _programlama arayüzü_ haline gelmiştir; modellere ne yapacaklarını söyler ve dönen yanıtların kalitesini etkiler. "Prompt Mühendisliği" ise tutarlı ve kaliteli yanıtlar sağlamak için promptların _tasarımı ve optimizasyonu_ üzerine hızla büyüyen bir çalışma alanıdır.

## Öğrenme Hedefleri

Bu derste, Prompt Mühendisliği’nin ne olduğunu, neden önemli olduğunu ve belirli bir model ve uygulama hedefi için daha etkili promptlar nasıl oluşturabileceğimizi öğreniyoruz. Prompt mühendisliğinin temel kavramlarını ve en iyi uygulamalarını anlayacak - gerçek örneklere uygulanan etkileşimli Jupyter Notebook “sandbox” ortamını keşfedeceğiz.

Dersin sonunda şunları yapabileceğiz:

1. Prompt mühendisliğinin ne olduğunu ve neden önemli olduğunu açıklayabiliriz.
2. Bir promptun bileşenlerini ve bunların nasıl kullanıldığını tanımlayabiliriz.
3. Prompt mühendisliği için en iyi uygulama ve teknikleri öğrenebiliriz.
4. Öğrenilen teknikleri gerçek örneklere, OpenAI uç noktası kullanarak uygulayabiliriz.

## Temel Terimler

Prompt Mühendisliği: Yapay zeka modellerini istenen çıktıların üretilmesine yönlendirmek için girişlerin tasarlanması ve iyileştirilmesi uygulaması.
Tokenizasyon: Metni, modelin anlayıp işleyebileceği daha küçük birimler olan tokenlara dönüştürme süreci.
Talimatlarla İncelenmiş LLM’ler: Yanıt doğruluğunu ve alaka düzeyini artırmak için belirli talimatlarla ince ayar yapılmış Büyük Dil Modelleri.

## Öğrenme Sandbox’ı

Prompt mühendisliği şu anda daha çok bir sanat olup, sezgimizi geliştirmek için _daha fazla pratik yapmak_ ve uygulama alanı uzmanlığı ile önerilen teknikleri ve model spesifik optimizasyonları harmanlayan deneme-yanılma yaklaşımını benimsemek en iyisidir.

Bu derse eşlik eden Jupyter Notebook, öğrendiklerinizi deneyebileceğiniz bir _sandbox_ ortamı sağlar - ister ilerledikçe ister sonundaki kod meydan okumasının bir parçası olarak. Alıştırmaları çalıştırmak için şunlara ihtiyacınız olacak:

1. **Bir Azure OpenAI API anahtarı** - dağıtılmış bir LLM için servis uç noktası.
2. **Bir Python Çalışma Zamanı** - Notebook’un çalıştırılabileceği ortam.
3. **Yerel Çevresel Değişkenler** - hazır olmak için şimdi [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) adımlarını tamamlayın.

Notebook, _başlangıç_ alıştırmaları ile gelir - ancak daha fazla örnek veya fikir denemek için kendi _Markdown_ (açıklama) ve _Kod_ (prompt istekleri) bölümlerinizi eklemeniz ve prompt tasarımı sezginizi geliştirmeniz teşvik edilir.

## Görselleştirilmiş Kılavuz

Bu derse başlamadan önce genel resmi görmek ister misiniz? İşte ana konuları ve her biri için düşünmeniz gereken temel çıkarımları size sunan görselleştirilmiş bir kılavuz. Ders yol haritası, temel kavramları ve zorlukları anlamaktan başlayıp ilgili prompt mühendisliği teknikleri ve en iyi uygulamalarla bunlara çözüm getirmeye kadar ilerler. Bu kılavuzdaki "İleri Teknikler" bölümü, müfredatın _bir sonraki_ bölümünde ele alınan içeriğe atıfta bulunur.

![Prompt Mühendisliğine Görsel Kılavuz](../../../translated_images/tr/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Girişimimiz

Şimdi, _bu konunun_ [yapay zekayı eğitime taşıma misyonumuzla](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst) nasıl ilişkili olduğuna bakalım. _Kişiselleştirilmiş öğrenme_ alanında yapay zeka destekli uygulamalar geliştirmek istiyoruz - o halde uygulamamızın farklı kullanıcılarının nasıl promptlar "tasarlayabileceğini" düşünelim:

- **Yöneticiler**, yapay zekadan _müfredat verilerini analiz edip boşlukları tespit etmesini_ isteyebilir. Yapay zeka sonuçları özetleyebilir veya kodla görselleştirebilir.
- **Eğitimciler**, yapay zekadan _hedef kitle ve konu için bir ders planı oluşturmasını_ isteyebilir. Yapay zeka belirli bir formatta kişiselleştirilmiş planı oluşturabilir.
- **Öğrenciler**, yapay zekadan _zor bir konuda onlara öğretmenlik yapmasını_ isteyebilir. Yapay zeka artık düzeylerine uygun dersler, ipuçları ve örneklerle rehberlik yapabilir.

Bu daha başlangıç. Eğitim uzmanları tarafından seçilen açık kaynaklı bir prompt kütüphanesi olan [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) ile geniş imkanları keşfedin! _Bu promptları sandbox'ta ya da OpenAI Playground’da çalıştırmayı deneyin ve ne olduğunu görün!_

<!--
DERS ŞABLONU:
Bu birim temel kavram #1’i kapsamalı.
Konuyu örnekler ve referanslarla pekiştirin.

KAVRAM #1:
Prompt Mühendisliği.
Tanımlayın ve neden gerekli olduğunu açıklayın.
-->

## Prompt Mühendisliği Nedir?

Bu derse, belirli bir uygulama hedefi ve model için tutarlı ve kaliteli yanıtlar (tamalamalar) sağlamak üzere metin girdilerinin (promptların) _tasarlanması ve optimize edilmesi_ süreci olarak **Prompt Mühendisliği**ni tanımlayarak başladık. Bunu iki aşamalı bir süreç olarak düşünebiliriz:

- Belirli bir model ve hedef için ilk promptu _tasarlamak_
- Yanıt kalitesini artırmak için promptu yineleyerek _iyileştirmek_

Bu, optimal sonuçlar için kullanıcı sezgisi ve çabası gerektiren deneme-yanılma temelli bir süreçtir. Peki neden önemlidir? Bu sorunun cevabı için önce üç kavramı anlamamız gerekiyor:

- _Tokenizasyon_ = modelin promptu "nasıl gördüğü"
- _Temel LLM’ler_ = temel modelin promptu "nasıl işlediği"
- _Talimatlarla İncelenmiş LLM’ler_ = model artık "görevleri" nasıl görebilir

### Tokenizasyon

Bir LLM, promptları _token dizisi_ olarak görür ve farklı modeller (ya da model versiyonları) aynı promptu farklı şekillerde tokenlara ayırabilir. LLM’ler tokenlar üzerinde eğitildiği için (ham metin üzerinde değil), promptların nasıl tokenlaştırıldığı yaratılan yanıt kalitesini doğrudan etkiler.

Tokenizasyonun nasıl çalıştığına sezgi kazanmak için aşağıdaki gibi araçları deneyebilirsiniz: [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst). Promptunuzu kopyalayın - ve boşluk karakterleri ile noktalama işaretlerinin nasıl işlendiğine dikkat ederek tokenlara nasıl dönüştüğünü görün. Bu örnek eski bir LLM (GPT-3) gösterdiğinden, daha yeni bir modelde farklı sonuçlar alabilirsiniz.

![Tokanizasyon](../../../translated_images/tr/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Kavram: Temel Modeller

Prompt tokenlandıktan sonra, ["Temel LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (veya Temel Model) ana işlevi bu dizideki tokenları tahmin etmektir. LLM’ler devasa metin veri setlerinde eğitildiğinden tokenlar arasındaki istatistiksel ilişkileri iyi bilir ve bu tahmini makul bir güvenle yapabilir. Ancak prompt veya token içindeki kelimelerin _anlamını_ anlamazlar; sadece "tamamlayabilecekleri" bir desen görürler. Kullanıcı müdahalesi veya önceden belirlenmiş koşul tarafından durdurulana kadar diziyi tahmin etmeye devam edebilirler.

Prompt tabanlı tamamlama nasıl çalışıyor görmek ister misiniz? Yukarıdaki promptu varsayılan ayarlarla [Microsoft Foundry playground](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)’a yazın. Sistem promptları bilgi talebi olarak işlemek üzere ayarlanmıştır - bu yüzden bu bağlama uygun bir tamamlama görmelisiniz.

Peki ya kullanıcı belirli kriterleri ya da görev hedefine uygun bir şey görmek isterse? İşte burada _talimatlarla incelenmiş_ LLM’ler devreye girer.

![Temel LLM Sohbet Tamamlama](../../../translated_images/tr/04-playground-chat-base.65b76fcfde0caa67.webp)

### Kavram: Talimatlarla İncelenmiş LLM’ler

Bir [Talimatlarla İncelenmiş LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst), temel modelle başlar ve net talimatlar içeren örnekler ya da giriş/çıkış çiftleri (ör., çok adımlı "mesajlar") ile ince ayar yapar - ve AI yanıtı bu talimatları izlemeye çalışır.

Bu, modelin _talimatları izlemesini_ ve _geri bildirimlerden öğrenmesini_ sağlayan İnsan Geri Bildirimi ile Pekiştirmeli Öğrenme (RLHF) gibi teknikler kullanarak modelin pratik uygulamalara daha uygun ve kullanıcı hedeflerine daha ilgili yanıtlar üretmesini sağlar.

Hadi deneyelim - yukarıdaki prompte geri dönün, ancak şimdi _sistem mesajını_ aşağıdaki talimat bağlamıyla değiştirin:

> _Sağlanan içeriği ikinci sınıf bir öğrenci için özetleyin. Sonucu 3-5 maddeyle bir paragrafla sınırlayın._

Sonucun istenen hedef ve formata göre ayarlandığını gördünüz mü? Bir eğitimci bu yanıtı doğrudan o dersin slaytlarında kullanabilir.

![Talimatlarla İncelenmiş LLM Sohbet Tamamlama](../../../translated_images/tr/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Neden Prompt Mühendisliğine İhtiyacımız Var?

Promptların LLM’ler tarafından nasıl işlendiğini öğrendiğimize göre, şimdi prompt mühendisliğine _neden_ ihtiyaç duyduğumuzu konuşalım. Cevap, mevcut LLM’lerin _güvenilir ve tutarlı tamamlama_ sağlama konusunda bazı zorluklar taşıması ve prompt yapımı ile optimizasyonuna çaba harcamadan bu amaçların zor ulaşılması gerçeğinde yatıyor. Örneğin:

1. **Model yanıtları stokastiktir.** _Aynı prompt_ farklı modellerde veya model sürümlerinde farklı yanıtlar üretebilir. Hatta _aynı model_ ile farklı zamanlarda değişen sonuçlar çıkabilir. _Prompt mühendisliği teknikleri bu varyasyonları azaltmak için daha iyi koruma sağlar_.

1. **Modeller yanlış yanıtlar uydurabilir.** Modeller _büyük ama sınırlı_ veri setleriyle önceden eğitildiğinden, eğitim kapsamı dışında kalan kavramlara dair bilgileri eksiktir. Sonuç olarak gerçeğe aykırı, hayali veya bilinen gerçeklerle çelişen tamamalara yol açabilirler. _Prompt mühendisliği teknikleri, yapay zekaya kaynak veya mantık talep ederek bu yanlışları tespit edip azaltmaya yardım eder_.

1. **Model yetenekleri değişkenlik gösterir.** Yeni modeller veya model nesilleri daha zengin yeteneklere sahip olur ancak maliyet ve karmaşıklıkta farklılıklar ve özgün tuhaflıklar getirir. _Prompt mühendisliği, farklılıkları soyutlayan ve model özel gereksinimlerine ölçeklenebilir, sorunsuz adaptasyon sağlayan en iyi uygulamalar ve iş akışları geliştirmemize olanak sağlar_.

Bunu OpenAI veya Azure OpenAI Playground’da deneyelim:

- Farklı LLM dağıtımlarıyla (örneğin OpenAI, Azure OpenAI, Hugging Face) aynı promptu kullanın - varyasyonları gördünüz mü?
- Aynı LLM dağıtımıyla (örneğin Azure OpenAI playground) aynı promptu tekrar tekrar kullanın - varyasyonlar nasıl farklılık gösterdi?

### Yanlış Yanıt Örneği

Bu derste, LLM’lerin bazen eğitimlerindeki sınırlamalar veya diğer kısıtlamalar nedeniyle gerçek dışı bilgi üretmesi durumuna **"yanlış yanıt" (fabrication)** terimini kullanıyoruz. Popüler makalelerde veya araştırma yazılarında buna _"halüsinasyon"_ da denebilir. Ancak biz bu davranışa insanî bir özellik atfetmemek için _"yanlış yanıt"_ teriminin kullanılmasını öneriyoruz. Bu aynı zamanda [Sorumlu Yapay Zeka yönergeleri](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) açısından da terminolojiyi güçlendirir, bazı bağlamlarda saldırgan veya dışlayıcı olabilecek terimlerin ortadan kaldırılmasını sağlar.

Yanlış yanıtların nasıl çalıştığına dair bir fikir edinmek ister misiniz? Modellerin eğitim veri kümesinde bulunmayan varsayımsal bir konu için içerik üretmesini isteyen bir prompt düşünün. Örneğin - şu promptu denedim:

> **Prompt:** 2076 Mars Savaşı hakkında bir ders planı oluştur.

Web araması, 2076’da Mars savaşları hakkında (örneğin televizyon dizileri veya kitaplar gibi) kurgusal örnekler olduğunu gösterdi - ancak 2076 yılına dair gerçek bir olay yok. Sağduyu da 2076’nın _gelecekte_ olduğunu ve bu yüzden gerçek bir olayla ilişkilendirilemeyeceğini söyler.


Peki, bu istemi farklı LLM sağlayıcıları ile çalıştırdığımızda ne olur?

> **Yanıt 1**: OpenAI Playground (GPT-35)

![Yanıt 1](../../../translated_images/tr/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Yanıt 2**: Azure OpenAI Playground (GPT-35)

![Yanıt 2](../../../translated_images/tr/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Yanıt 3**: : Hugging Face Chat Playground (LLama-2)

![Yanıt 3](../../../translated_images/tr/04-fabrication-huggingchat.faf82a0a51278956.webp)

Beklendiği gibi, her model (veya model versiyonu) stokastik davranış ve model yeteneklerindeki farklılıklar sayesinde biraz farklı yanıtlar üretiyor. Örneğin, bir model 8. sınıf öğrencisine hitap ederken diğeri lise öğrencisi varsayıyor. Ancak üç model de, olayın gerçek olduğuna inanabilecek bilgisiz bir kullanıcıyı ikna edebilecek yanıtlar üretti.

_Metaprompting_ ve _sıcaklık yapılandırması_ gibi prompt mühendisliği teknikleri, model uydurmalarını bir ölçüde azaltabilir. Yeni prompt mühendisliği _mimari_ yaklaşımları, bu etkileri hafifletmek veya azaltmak için yeni araçları ve teknikleri prompt akışına sorunsuzca entegre eder.

## Vaka İncelemesi: GitHub Copilot

Bu bölümü, gerçek dünya çözümlerinde prompt mühendisliğinin nasıl kullanıldığına dair bir vaka incelemesi olan [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst) üzerinden bir fikir edinerek tamamlayalım.

GitHub Copilot, sizin "Yapay Zeka Eş Programcınız"dır - metin istemlerini kod tamamlama haline dönüştürür ve geliştirme ortamınıza (örneğin Visual Studio Code) entegre edilmiştir, böylece kesintisiz bir kullanıcı deneyimi sağlar. Aşağıda belirtilen blog serisinde belgelendiği gibi, en erken versiyon OpenAI Codex modeline dayanıyordu - mühendisler hızla modelin ince ayarına ve daha iyi prompt mühendisliği teknikleri geliştirmeye ihtiyaç olduğunu fark etti ve kod kalitesini artırmayı hedeflediler. Temmuz ayında, daha hızlı öneriler için [Codex’i aşan geliştirilmiş bir AI modeli](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) tanıttılar.

Öğrenme yolculuklarını takip etmek için yazıları sırayla okuyunuz.

- **Mayıs 2023** | [GitHub Copilot, Kodunuzu Anlamada Daha İyi Hale Geliyor](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mayıs 2023** | [GitHub İçinde: GitHub Copilot Arkasındaki LLM’lerle Çalışmak](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Haziran 2023** | [GitHub Copilot için Daha İyi Promtlar Nasıl Yazılır](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Temmuz 2023** | [.. GitHub Copilot, Geliştirilmiş AI Modeli ile Codex’i Aşıyor](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Temmuz 2023** | [Bir Geliştirici için Prompt Mühendisliği ve LLM Rehberi](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Eylül 2023** | [Şirket İçin LLM Uygulaması Nasıl Kurulur: GitHub Copilot’tan Dersler](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Ayrıca, bu modellerin ve tekniklerin gerçek dünya uygulamalarını nasıl _uyguladığına_ dair daha fazla yazı için [Mühendislik bloglarını](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) ve [şuradaki örnek yazıyı](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) inceleyebilirsiniz.

---

<!--
DERS ŞABLONU:
Bu birim, temel kavram #2’yi kapsamalıdır.
Kavramı örnekler ve referanslarla pekiştirin.

KAVRAM #2:
Prompt Tasarımı.
Örneklerle açıklanmıştır.
-->

## Prompt Oluşturma

Prompt mühendisliğinin neden önemli olduğunu gördük - şimdi daha etkili prompt tasarımı için farklı teknikleri değerlendirebilmek adına istemlerin nasıl _oluşturulduğunu_ anlayalım.

### Temel Prompt

Temel prompt ile başlayalım: modele başka bir bağlam verilmeden gönderilen bir metin girdisi. İşte bir örnek - ABD milli marşının ilk birkaç sözcüğünü OpenAI [Completion API](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst)’ye gönderdiğimizde, yanıtı sonraki satırlarla anında _tamamlar_, temel tahmin davranışını gösterir.

| İstem (Girdi)       | Tamamlama (Çıktı)                                                                                                                          |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Sanki ABD milli marşı "The Star-Spangled Banner"ın sözlerinin başlangıcını yazıyorsunuz. Tam sözleri şunlardır ...                        |

### Karmaşık Prompt

Şimdi o temel promta bağlam ve talimatlar ekleyelim. [Chat Completion API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst), karmaşık bir promptu _mesajlar_ koleksiyonu olarak oluşturmamıza olanak tanır:

- Kullanıcı girişi ve yardımcı yanıtını yansıtan giriş/çıkış çiftleri.
- Yardımcı davranışı veya kişiliği için bağlamı ayarlayan sistem mesajı.

İstek artık aşağıdaki formda olup, _tokenizasyon_ bağlam ve konuşmadan ilgili bilgileri etkili biçimde yakalar. Sistem bağlamını değiştirmek, verilen kullanıcı girdileri kadar tamamlamaların kalitesini etkileyebilir.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Talimatlı Prompt

Yukarıdaki örneklerde kullanıcı promptu, bilgi talebi olarak yorumlanabilecek basit bir metin sorgusuydu. _Talimatlı_ promptlarda, yapay zekaya daha iyi rehberlik için metin görevleri daha ayrıntılı belirtmekte kullanılır. İşte bir örnek:

| İstem (Girdi)                                                                                                                                                                                                                         | Tamamlama (Çıktı)                                                                                                        | Talimat Türü        |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Write a description of the Civil War                                                                                                                                                                                                   | _basit bir paragraf döndürüldü_                                                                                           | Basit               |
| Write a description of the Civil War. Provide key dates and events and describe their significance                                                                                                                                     | _başlıca olay tarihleri ile liste halinde açıklamalar takip eden paragraf döndürüldü_                                       | Karmaşık            |
| Write a description of the Civil War in 1 paragraph. Provide 3 bullet points with key dates and their significance. Provide 3 more bullet points with key historical figures and their contributions. Return the output as a JSON file | _bir metin kutusunda JSON formatında daha ayrıntılı bilgiler döndürülür; bunu dosyaya yapıştırıp doğrulayabilirsiniz_        | Karmaşık. Formatlı.  |

## Birincil İçerik

Yukarıdaki örneklerde, prompt hâlâ oldukça geniş bırakılmış ve LLM’nin önceden eğitildiği veri kümesinden hangisinin ilgili olduğuna karar vermesine izin verilmiştir. _Birincil içerik_ tasarım deseninde, giriş metni iki kısma ayrılır:

- bir talimat (eylem)
- eylemi etkileyen ilgili içerik

İşte talimatın "bunu 2 cümlede özetle" olduğu bir örnek.

| İstem (Girdi)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Tamamlama (Çıktı)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jüpiter, Güneş'ten beşinci gezegendir ve Güneş Sistemi'nin en büyüğüdür. Jüpiter, Güneş'in kütlesinin binde biri kadar bir kütleye sahip olan bir gaz devidir, ancak Güneş Sistemi'ndeki diğer tüm gezegenlerin toplam kütlesinin iki buçuk katıdır. Jüpiter, çıplak gözle görülebilen en parlak cisimlerden biridir ve tarih öncesi çağlardan beri bilinir. Roma tanrısı Jüpiter'in adını almıştır.[19] Dünya'dan bakıldığında, yansıyan ışığı görünür gölgeler oluşturacak kadar parlak olabilir,[20] ve ortalama olarak Ay ve Venüs'ten sonra gece gökyüzündeki üçüncü en parlak doğal cisimdir. <br/> **Bunu 2 kısa cümlede özetle** | Jüpiter, Güneş'ten beşinci gezegen olup Güneş Sistemi'nin en büyüğüdür ve gece gökyüzündeki en parlak cisimlerden biridir. Roma tanrısı Jüpiter'in adını taşıyan bu gaz devi, Güneş Sistemi'ndeki diğer tüm gezegenlerin iki buçuk katı kütleye sahiptir.        |

Birincil içerik bölümü, daha etkili talimatlar vermek için çeşitli şekillerde kullanılabilir:

- **Örnekler** - modele ne yapacağını açıkça söylemek yerine, ne yapacağını örneklerle gösterip desenleri çıkarmasını sağlamak.
- **İpuçları** - talimatı, tamamlamaları daha ilgili hale getirmek için yönlendiren "ipuçlarıyla" takip etmek.
- **Şablonlar** - özel verilerle uyarlanabilen yer tutucular (değişkenler) içeren tekrar edilebilir prompt reçeteleri.

Bunları uygulamada keşfedelim.

### Örnekleri Kullanmak

Bu yaklaşımda, bir göreve yönelik istenen çıktı için bazı örnekleri "modeli beslemek" adına birincil içerik kullanılır ve model istenen çıktının desenini çıkarır. Verilen örnek sayısına bağlı olarak sıfır-görüşlü, bir-görüşlü, birkaç-görüşlü istemler yapılabilir.

Prompt artık üç bileşenden oluşur:

- Bir görev açıklaması
- İstenen çıktıdan birkaç örnek
- Yeni bir örnek başlangıcı (ki bu örtülü bir görev açıklaması olur)

| Öğrenme Türü | İstem (Girdi)                                                                                                                                        | Tamamlama (Çıktı)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Sıfır-görüşlü | "Güneş Parlıyor". İspanyolcaya çevir                                                                                                                 | "El Sol está brillando".    |
| Bir-görüşlü   | "Güneş Parlıyor" => "El Sol está brillando". <br> "Soğuk ve Rüzgarlı Bir Gün" =>                                                                        | "Es un día frío y ventoso". |
| Birkaç-görüşlü | Oyuncu koşu yollarını geçti => Beyzbol <br/> Oyuncu as vuruşu yaptı => Tenis <br/> Oyuncu altılık vurdu => Kriket <br/> Oyuncu smaç yaptı =>             | Basketbol                  |
|               |                                                                                                                                                       |                             |

Sıfır-görüşlü istemde açık talimat ("İspanyolcaya çevir") verdiğimizi, ancak bir-görüşlü örnekte bunun çıkarıldığını ve birkaç-görüşlü örneğin daha fazla örnekle modellerin ek talimat olmadan daha doğru çıkarımlar yapmasına nasıl olanak sağladığını gözlemleyin.

### Prompt İpuçları

Birincil içerikle başka bir teknik ise örnekler yerine _ipuçları_ sağlamaktır. Bu durumda model, istenen yanıt biçimini yansıtan kısa bir parçayla _başlatılarak_ doğru yöne yönlendirilir. Model bu "ipuçunu" alır ve bu tarzda devam eder.

| İpucu Sayısı | İstem (Girdi)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Tamamlama (Çıktı)                                                                                                                                                                                                                                                                                       |
| :----------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0            | Jüpiter, Güneş'ten beşinci gezegendir ve Güneş Sistemi'nin en büyüğüdür. Jüpiter, Güneş'in kütlesinin binde biri kadar bir kütleye sahip olan bir gaz devidir, ancak Güneş Sistemi'ndeki diğer tüm gezegenlerin toplam kütlesinin iki buçuk katıdır. Jüpiter, çıplak gözle görülebilen en parlak cisimlerden biridir ve tarih öncesi çağlardan beri bilinir. <br/>**Bunu Özetle**                                       | Jüpiter, Güneş Sistemi'ndeki en büyük gezegen ve Güneş'ten beşinci sıradadır. Güneş'in binde biri olan kütlesi vardır ama diğer tüm gezegenlerin toplamından daha ağırdır. Antik uygarlıklar tarafından uzun zamandır bilinmekte ve gece gökyüzünde kolayca görülebilmektedir. |
| 1            | Jüpiter, Güneş'ten beşinci gezegendir ve Güneş Sistemi'nin en büyüğüdür. Jüpiter, Güneş'in kütlesinin binde biri kadar bir kütleye sahip olan bir gaz devidir, ancak Güneş Sistemi'ndeki diğer tüm gezegenlerin toplam kütlesinin iki buçuk katıdır. Jüpiter, çıplak gözle görülebilen en parlak cisimlerden biridir ve tarih öncesi çağlardan beri bilinir. <br/>**Bunu Özetle** <br/> Öğrendiklerimiz Jüpiter'in | Güneş'ten beşinci gezegen ve Güneş Sistemi'nin en büyüğü olduğunu gösterir. Güneş'in binde biri kütlesine sahip gaz devi, diğer gezegenlerin toplam iki buçuk katıdır. Çıplak gözle görülebilir ve tarihten beri bilinmektedir.                          |

| 2              | Jüpiter, Güneş'ten beşinci gezegen ve Güneş Sistemi'ndeki en büyük gezegendir. Kütlesi, Güneş'in kütlesinin binde biri kadar olan bir gaz devidir, ancak diğer tüm gezegenlerin toplam kütlesinin iki buçuk katıdır. Jüpiter, çıplak gözle gece gökyüzünde görülebilen en parlak cisimlerden biridir ve tarihin kayıtlara geçmesinden önceki eski uygarlıklar tarafından bilinmektedir. <br/>**Özetle** <br/> Öğrendiğimiz İlk 3 Gerçek:         | 1. Jüpiter, Güneş'ten beşinci gezegen ve Güneş Sistemi'ndeki en büyük gezegendir. <br/> 2. Kütlesi, Güneş'in kütlesinin binde biri kadar olan bir gaz devidir...<br/> 3. Jüpiter, eski zamanlardan beri çıplak gözle görünmüştür ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### İstek Şablonları

Bir istek şablonu, ihtiyaç duyulduğunda saklanabilen ve yeniden kullanılabilen _önceden tanımlanmış bir istek tarifidir_, daha tutarlı kullanıcı deneyimlerini büyük ölçekte sağlamaya yöneliktir. En basit haliyle, [OpenAI'den bu örnek](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) gibi kullanıcı ve sistem mesajları içeren interaktif istek bileşenlerini ve API tabanlı istek formatını destekleyen bir istek örnekleri koleksiyonudur - yeniden kullanım için.

Daha karmaşık biçiminde, [LangChain'den bu örnekte](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) olduğu gibi, _yer tutucular_ içerir ve bu yer tutucular çeşitli kaynaklardan (kullanıcı girişi, sistem bağlamı, dış veri kaynakları vb.) gelen verilerle değiştirilebilir, böylece dinamik olarak bir istek oluşturulabilir. Bu, tutarlı kullanıcı deneyimlerini **programatik olarak** yönetmek için yeniden kullanılabilir isteklerden oluşan bir kitaplık oluşturmayı sağlar.

Son olarak, şablonların gerçek değeri, dikey uygulama alanları için _istek kütüphaneleri_ oluşturma ve yayınlama yeteneğinde yatar - burada istek şablonu, uygulamaya özgü bağlamları veya örnekleri yansıtacak şekilde _optimize edilmiş_ ve hedeflenen kullanıcı kitlesi için yanıtların daha alakalı ve doğru olmasını sağlar. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) deposu, ders planlama, müfredat tasarımı, öğrenci eğitimi gibi temel hedeflere vurgu yaparak eğitim alanı için isteklere odaklanan bir kitaplık örneği olarak harika bir örnektir.

## Destekleyici İçerik

İsteğin yapılandırmasını bir talimat (görev) ve hedef (birincil içerik) olarak düşünürsek, _ikincil içerik_, çıktıyı **bir şekilde etkilemek için** sağladığımız ek bağlam gibidir. Bu, yanıtı istenilen kullanıcı hedeflerine veya beklentilerine uyacak şekilde _uyarlamaya_ yardımcı olabilecek ayar parametreleri, biçimlendirme talimatları, konu sınıflandırmaları vb. olabilir.

Örneğin: Müfredattaki tüm mevcut kursların kapsamlı meta verilerine (isim, açıklama, seviye, meta etiketler, eğitmen vb.) sahip bir kurs kataloğu verildiğinde:

-  "2023 Güz dönemi için kurs kataloğunu özetle" talimatını tanımlayabiliriz
-  Birincil içerik olarak istenen çıktının birkaç örneğini sağlayabiliriz
-  İkincil içerik olarak en ilgi çekici 5 "etiketi" belirleyebiliriz.

Şimdi model, birkaç örnekle gösterilen formatta bir özet sağlayabilir - ancak bir sonuç birden çok etikete sahipse, ikincil içerikte belirlenen 5 etikete öncelik verebilir.

---

<!--
DERS ŞABLONU:
Bu ünitede temel kavram #1 ele alınmalıdır.
Kavram, örnekler ve referanslarla pekiştirilmelidir.

KAVRAM #3:
İstek Mühendisliği Teknikleri.
İstek mühendisliği için bazı temel teknikler nelerdir?
Bazı alıştırmalarla örnekleyin.
-->

## İstek Verme En İyi Uygulamaları

Artık isteklerin nasıl _oluşturulabileceğini_ öğrendiğimize göre, onları en iyi uygulamaları yansıtacak şekilde _tasarlamayı_ düşünebiliriz. Bunu iki bölümde düşünebiliriz - doğru _zihniyete_ sahip olmak ve doğru _teknikleri_ uygulamak.

### İstek Mühendisliği Zihniyeti

İstek Mühendisliği deneme-yanılma sürecidir, bu yüzden üç geniş kılavuz faktörü aklınızda tutun:

1. **Alan Anlayışı Önemlidir.** Yanıt doğruluğu ve alaka seviyesi, uygulamanın veya kullanıcının çalıştığı _alanda_ bir fonksiyondur. Sezgilerinizi ve alan uzmanlığınızı kullanarak **teknikleri daha da özelleştirin**. Örneğin, sistem isteklerinizde _alan-spesifik kişilikler_ tanımlayın ya da kullanıcı isteklerinizde _alan-spesifik şablonlar_ kullanın. Alan-spesifik bağlamları yansıtan ikincil içerik sağlayın veya modeli aşina olduğu kullanım kalıplarına yönlendirmek için _alan-spesifik işaretler ve örnekler_ kullanın.

2. **Model Anlayışı Önemlidir.** Modellerin doğası gereği stokastik olduğunu biliyoruz. Ancak model uygulamaları kullandıkları eğitim veri seti (önceden eğitilmiş bilgi), sundukları yetenekler (örneğin API veya SDK aracılığıyla) ve optimize edildikleri içerik türü (kod, görüntü, metin gibi) açısından değişiklik gösterebilir. Kullandığınız modelin güçlü ve zayıf yanlarını anlayın ve bu bilgiyi kullanarak _görevleri önceliklendirin_ veya modelin yeteneklerine optimize edilmiş _özelleştirilmiş şablonlar_ oluşturun.

3. **Yineleme ve Doğrulama Önemlidir.** Modeller hızla gelişmekte ve istek mühendisliği teknikleri de öyle. Bir alan uzmanı olarak, genel topluluğa uymayabilecek kendinize özgü başka bağlamlar veya kriterlere sahip olabilirsiniz. İstek mühendisliği araçlarını ve tekniklerini "başlangıç noktası" olarak kullanın, ardından sezgileriniz ve alan uzmanlığınızla sonuçları yineleyin ve doğrulayın. Gözlemlerinizi kaydedin ve başkalarının da hızlı tekrarlar için kullanabileceği bir **bilgi tabanı** (örneğin, istek kitaplıkları) oluşturun.

## En İyi Uygulamalar

Şimdi, [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) ve [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) uygulayıcıları tarafından önerilen yaygın en iyi uygulamalara bakalım.

| Ne Yapmalı                        | Neden                                                                                                                                                                                                                                            |
| :-------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| En son modelleri değerlendirin.  | Yeni model nesilleri muhtemelen geliştirilmiş özellikler ve kaliteye sahip olacak - ancak daha yüksek maliyetler de getirebilir. Etkilerini değerlendirin ve ardından geçiş kararları alın.                                                         |
| Talimatları ve bağlamı ayırın.  | Modelinizin/sağlayıcınızın talimatlar, birincil ve ikincil içerikleri daha net ayırmak için _sınırlandırıcı_ tanımlayıp tanımlamadığını kontrol edin. Bu, modellerin tokenlara daha doğru ağırlık vermesine yardımcı olabilir.                      |
| Spesifik ve açık olun.            | İstenen bağlam, çıktı, uzunluk, format, stil vb. hakkında daha fazla ayrıntı verin. Bu, yanıtların kalitesini ve tutarlılığını artıracaktır. Tarifleri yeniden kullanılabilir şablonlarda yakalayın.                                               |
| Açıklayıcı olun, örnekler kullanın. | Modeller, "göster ve anlat" yaklaşımına daha iyi yanıt verebilir. Önce talimat verdiğiniz (örneğin sıfır örnekle) `sıfır atış` yaklaşımı ile başlayın, ardından istenen çıktının birkaç örneğini sağlayarak `birkaç atış` yöntemiyle iyileştirin. Benzetmeler kullanın. |
| Tamamlama için ipuçları kullanın | Yanıt için başlangıç noktası olarak kullanabileceği bazı öncü kelimeler veya ifadeler vererek modeli istenen sonuca yönlendirin.                                                                                                                |
| İkna edici olun                  | Bazen modeli tekrar etmek gerekebilir. Birincil içeriğinizden önce ve sonra talimatlar verin, talimat ile ipucu kullanın vb. Ne işe yaradığını görmek için yineleyin ve doğrulayın.                                                              |
| Sıra önemlidir                  | Bilgileri modele sunma sırası, çıktıyı etkileyebilir; öğrenme örneklerinde bile, sonunculuk yanlılığı nedeniyle. En iyi sonucu görmek için farklı seçenekleri deneyin.                                                                         |
| Modele bir “çıkış” seçeneği verin | Modelin herhangi bir nedenle görevi tamamlayamadığında verebileceği _geri dönüş_ tamamlama yanıtı verin. Bu, modellerin yanlış veya uydurma yanıtlar oluşturma olasılığını azaltabilir.                                                        |
|                                   |                                                                                                                                                                                                                                                  |

Herhangi bir en iyi uygulamada olduğu gibi, _kendi durumunuz model, görev ve alana bağlı olarak değişebilir_. Bunları başlangıç noktası olarak kullanın ve size en uygun olanı bulmak için yineleyin. Yeni modeller ve araçlar kullanılabilir hale geldikçe istek mühendisliği sürecinizi süreç ölçeklendirilebilirliği ve yanıt kalitesine odaklanarak sürekli olarak yeniden değerlendirin.

<!--
DERS ŞABLONU:
Bu ünitede uygun ise bir kod meydan okuması verilmelidir

MEYDAN OKUMA:
Talimatlarda yalnızca kod yorumları bulunan bir Jupyter Not Defteri bağlantısı (kod bölümleri boş).

ÇÖZÜM:
İsteklerle doldurulmuş ve çalıştırılmış o Not Defterinin bir kopyasına bağlantı, nasıl bir örnek çıktı olabileceğini gösterir.
-->

## Ödev

Tebrikler! Dersin sonuna geldiniz! Şimdi o kavramları ve teknikleri gerçek örneklerle test etme zamanı!

Ödevimiz için, etkileşimli olarak tamamlayabileceğiniz egzersizler içeren bir Jupyter Not Defteri kullanacağız. Kendi Markdown ve Kod hücrelerinizle Not Defterini genişleterek fikirleri ve teknikleri kendi başınıza keşfedebilirsiniz.

### Başlamak için, deposu çatalla, sonra

- (Önerilen) GitHub Codespaces başlat
- (Alternatif olarak) Depoyu yerel cihazınıza klonlayın ve Docker Desktop ile kullanın
- (Alternatif olarak) Not Defterini tercih ettiğiniz Not Defteri çalışma ortamıyla açın.

### Sonra, ortam değişkenlerinizi yapılandırın

- Depo kökündeki `.env.copy` dosyasını `.env` olarak kopyalayın ve `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` ve `AZURE_OPENAI_DEPLOYMENT` değerlerini doldurun. Nasıl yapılacağını öğrenmek için [Öğrenme Sandbox bölümüne](#öğrenme-sandbox’ı) geri dönün.

### Sonra, Jupyter Not Defterini açın

- Çalışma zamanı çekirdeğini seçin. 1. veya 2. seçeneği kullanıyorsanız, geliştirici konteyneri tarafından sağlanan varsayılan Python 3.10.x çekirdeğini seçmeniz yeterlidir.

Egzersizleri çalıştırmaya hazırsınız. Burada _doğru veya yanlış_ cevaplar yoktur - sadece deneme-yanılma ile seçenekleri keşfetmek ve belirli bir model ile uygulama alanı için neyin işe yaradığını sezgisel olarak kavramaktır.

_Bu nedenle bu derste Kod Çözüm bölümleri yoktur. Bunun yerine, Not Defteri'nde "Çözümüm:" başlıklı Markdown hücreleri olacaktır ve referans olarak bir örnek çıkışı gösterir._

 <!--
DERS ŞABLONU:
Bölümü bir özet ve kendi kendine öğrenim için kaynaklar ile sarın.
-->

## Bilgi Kontrolü

Aşağıdakilerden hangisi makul bazı en iyi uygulamalara uygun iyi bir istektir?

1. Bana kırmızı bir arabanın resmini göster
2. Gün batımında bir uçurum kenarında park etmiş Volvo marka ve XC90 model kırmızı bir arabanın resmini göster
3. Volvo marka ve XC90 model kırmızı bir arabanın resmini göster

C: 2, en iyi istek, Çünkü "ne" hakkında detay sağlar ve belirli marka ve model gibi spesifik özelliklere girer ve ayrıca genel ortamı da tanımlar. 3 ikinci en iyisi çünkü çok sayıda açıklama içerir.

## 🚀 Meydan Okuma

İstekle “çıkarma” tekniğini uygulamaya çalış: Cümleyi tamamla "Bana Volvo marka ve ... olan kırmızı arabanın resmini göster". Ne cevap veriyor ve bunu nasıl geliştirirsin?

## Harika İş! Öğrenmeye Devam Et

Farklı İstek Mühendisliği kavramları hakkında daha fazla bilgi edinmek ister misiniz? Bu konudaki diğer harika kaynakları bulmak için [devam eden öğrenme sayfasına](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) gidin.

Ders 5'e gidin; burada [ileri istek verme tekniklerine](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst) bakacağız!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->