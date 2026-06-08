# Prompt Mühendisliği Temelleri

[![Prompt Mühendisliği Temelleri](../../../translated_images/tr/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Giriş
Bu modül, üretken yapay zeka modellerinde etkili istemler oluşturmak için temel kavramlar ve teknikleri kapsar. Bir LLM'ye isteminizi yazma şekliniz de önemlidir. Özenle hazırlanmış bir istem, daha kaliteli bir yanıt elde edebilir. Peki tam olarak _istem_ ve _istem mühendisliği_ gibi terimler ne anlama geliyor? Ve LLM'ye gönderdiğim istem _girişini_ nasıl iyileştiririm? Bu bölüm ve bir sonraki bölümde bu soruları yanıtlamaya çalışacağız.

_Uretken yapay zeka_, kullanıcı taleplerine yanıt olarak yeni içerik (örneğin, metin, görsel, ses, kod vb.) oluşturabilir. Bunu, doğal dil ve kod kullanımına yönelik eğitilmiş OpenAI'ın GPT ("Generative Pre-trained Transformer") serisi gibi _Büyük Dil Modelleri_ (LLM) kullanarak başarır.

Kullanıcılar artık herhangi bir teknik uzmanlığa veya eğitime ihtiyaç duymadan sohbet gibi tanıdık paradigmalar aracılığıyla bu modellerle etkileşime girebilir. Modeller _istem tabanlıdır_ - kullanıcılar bir metin girdisi (istem) gönderir ve yapay zekadan yanıt alır (tamamlama). Daha sonra çok turlu sohbetler halinde "yapay zeka ile sohbet" ederek istemlerini yanıt beklentilerine uyana kadar yineleyebilirler.

"İstemler" artık üretken yapay zeka uygulamalarında modellerin ne yapacağını bildiren ve dönen yanıtların kalitesini etkileyen birincil _programlama arayüzü_ haline gelir. "İstem Mühendisliği", tutarlı ve kaliteli yanıtlar sunmak için istemlerin _tasarlanması ve optimize edilmesi_ üzerine hızla gelişen bir çalışma alanıdır.

## Öğrenme Hedefleri

Bu derste, İstem Mühendisliği'nin ne olduğunu, neden önemli olduğunu ve belirli bir model ve uygulama hedefi için daha etkili istemlerin nasıl oluşturulacağını öğreniyoruz. İstem mühendisliği için temel kavramları ve en iyi uygulamaları anlayacak ve bu kavramların gerçek örneklere nasıl uygulandığını görebileceğimiz interaktif bir Jupyter Notebooks "sandbox" ortamını keşfedeceğiz.

Bu dersin sonunda şunları yapabileceğiz:

1. İstem mühendisliğinin ne olduğunu ve neden önemli olduğunu açıklamak.
2. Bir istemin bileşenlerini ve nasıl kullanıldığını tanımlamak.
3. İstem mühendisliği için en iyi uygulama ve teknikleri öğrenmek.
4. Öğrenilen teknikleri gerçek örneklere OpenAI uç noktası kullanarak uygulamak.

## Temel Terimler

İstem Mühendisliği: Yapay zeka modellerini istenen çıktılar üretmeye yönlendirmek için girdileri tasarlama ve iyileştirme uygulaması.  
Tokenizasyon: Metni modelin anlayıp işleyebileceği daha küçük birimler olan tokenlara dönüştürme süreci.  
Talimat Ayarlı LLM'ler: Tepki doğruluğunu ve alakasını artırmak için belirli talimatlarla ince ayar yapılmış Büyük Dil Modelleri (LLM).

## Öğrenme Sandbox'u

İstem mühendisliği şu anda daha çok bir sanat olarak kabul edilir. Buna dair sezgimizi geliştirmek için en iyi yol _daha fazla pratik yapmak_ ve uygulama alanı uzmanlığını önerilen teknikler ve modele özgü optimizasyonlarla birleştiren deneme-yanılma yaklaşımını benimsemektir.

Bu dersle birlikte gelen Jupyter Not Defteri, öğrendiklerinizi uygulayabileceğiniz bir _sandbox_ ortamı sağlar - ister derste ister ders sonunda kod meydan okuması sırasında. Egzersizleri çalıştırmak için şunlara ihtiyacınız olacak:

1. **Bir Azure OpenAI API anahtarı** - konuşlandırılmış bir LLM için servis uç noktası.  
2. **Bir Python Çalışma Zamanı** - Not Defterinin çalıştırılabilmesi için.  
3. **Yerel Ortam Değişkenleri** - _Hazırlanmak için [KURULUM](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) adımlarını tamamlayın_.

Defter, _başlangıç_ egzersizleriyle birlikte gelir - ancak kendi _Markdown_ (açıklama) ve _Kod_ (istem istekleri) bölümlerinizi ekleyerek daha fazla örnek veya fikir deneyebilir ve istem tasarımı konusundaki sezginizi geliştirebilirsiniz.

## Görsel Rehber

Derse başlamadan önce bu dersin genel kapsamını görmek ister misiniz? Bu görsel rehber, ana konular ve her biri için düşünmeniz gereken önemli çıkarımlar hakkında size bir fikir verir. Ders yol haritası, temel kavramları ve zorlukları anlamaktan ilgili istem mühendisliği teknikleri ve en iyi uygulamalarla çözümlemeye kadar ilerler. Rehberdeki "İleri Teknikler" bölümü, bu müfredatın _bir sonraki_ bölümünde ele alınacak içeriğe atıfta bulunur.

![Prompt Mühendisliğine Görsel Rehber](../../../translated_images/tr/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Girişimimiz

Şimdi, _bu konunun_ [yapay zeka yeniliğini eğitime getirmek](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst) misyonumuza nasıl bağlandığından bahsedelim. Kişiselleştirilmiş öğrenmenin yapay zeka destekli uygulamalarını geliştirmek istiyoruz - bu yüzden uygulamamızın farklı kullanıcılarının istemleri nasıl "tasarlayabileceği" üzerine düşünelim:

- **Yöneticiler**, müfredat verilerini analiz ederek kapsama alanındaki boşlukları tespit etmesi için yapay zekaya istekte bulunabilir. AI, sonuçları özetleyebilir veya kodla görselleştirebilir.  
- **Eğitmenler**, hedef kitle ve konu için ders planı oluşturmasını yapay zekadan isteyebilir. Yapay zeka, belirtilen formatta kişiselleştirilmiş planı oluşturabilir.  
- **Öğrenciler**, zor bir konuda kendilerine öğretmenlik yapmasını isteyebilir. Yapay zeka, öğrencilerin seviyelerine uygun dersler, ipuçları ve örneklerle rehberlik yapabilir.

Bu sadece buzdağının görünen kısmı. Geniş olanakları görmek için eğitim uzmanları tarafından derlenen açık kaynaklı istemler kütüphanı [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) adresine göz atın! _Bu istemlerin bazılarını sandbox'ta veya OpenAI Playground'da çalıştırmayı deneyin ve neler olduğunu görün!_

<!--
LESSON TEMPLATE:
Bu ünite temel kavram #1'i kapsamalıdır.
Kavramı örnekler ve referanslarla pekiştirin.

KAVRAM #1:
İstem Mühendisliği.
Tanımlayın ve neden gerektiğini açıklayın.
-->

## İstem Mühendisliği Nedir?

Derse, belirli bir uygulama hedefi ve model için tutarlı ve kaliteli yanıtlar (tamamlamalar) sunmak üzere metin girdilerini (istemleri) _tasarlama ve optimize etme_ süreci olarak **İstem Mühendisliği** kavramını tanımlayarak başladık. Bunu 2 adımlı bir süreç olarak düşünebiliriz:

- Belirli bir model ve hedef için ilk istemi _tasarlamak_  
- Yanıt kalitesini artırmak için istemi yinelemelerle _iyileştirmek_

Bu, en iyi sonuçları elde etmek için kullanıcı sezgisi ve çabası gerektiren zorunlu bir deneme-yanılma sürecidir. Peki neden önemli? Bu soruyu yanıtlamak için önce üç kavramı anlamamız gerekir:

- _Tokenizasyon_ = modelin istemi nasıl "gördüğü"  
- _Temel LLM'ler_ = temel modelin istemi nasıl "işlediği"  
- _Talimat Ayarlı LLM'ler_ = modelin artık "görevleri" nasıl görebildiği

### Tokenizasyon

Bir LLM, istemleri _token dizisi_ olarak görür; farklı modeller (veya bir modelin farklı sürümleri) aynı istemi farklı şekillerde tokenize edebilir. LLM'ler tokenlar üzerinde eğitildiğinden (ham metin üzerinde değil), istemlerin nasıl tokenize edildiği üretilen yanıtın kalitesi üzerinde doğrudan etkilidir.

Tokenizasyonun nasıl çalıştığına dair sezgi kazanmak için aşağıdaki gibi araçları deneyin: [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst). İsteminizi kopyalayın ve bunun tokenlara nasıl dönüştüğüne, boşluk karakterleri ve noktalama işaretlerinin nasıl işlendiğine dikkat edin. Bu örnek daha eski bir LLM'yi (GPT-3) göstermektedir - daha yeni bir modelde farklı bir sonuç elde etmek mümkündür.

![Tokenizasyon](../../../translated_images/tr/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Kavram: Temel Modeller

Bir istem tokenize edildikten sonra, ["Temel LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (veya Temel Model) temel işlevi, o dizideki tokeni tahmin etmektir. LLM'ler, devasa metin veri kümeleri üzerinde eğitildiğinden tokenlar arasındaki istatistiksel ilişkileri iyi bilir ve bu tahmini belli bir güvenle yapabilirler. İstemdeki kelimelerin _anlamını_ anlamazlar; sadece bir sonraki tahminleri ile "tamamlayabilecekleri" bir desen görürler. Kullanıcı müdahalesi ya da önceden belirlenmiş bir koşul gerçekleşinceye kadar diziyi tahmin etmeye devam edebilirler.

İstem tabanlı tamamlama nasıl çalışır görmek ister misiniz? Yukarıdaki istemi Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) içine varsayılan ayarlarla girin. Sistem, istemleri bilgi istekleri olarak ele alacak şekilde yapılandırılmıştır - dolayısıyla bu bağlamı karşılayan bir tamamlama görmelisiniz.

Peki ya kullanıcı, bazı kriterlere veya görev hedeflerine uygun belirli bir şeyi görmek isterse? İşte burada _talimat ayarlı_ LLM'ler devreye girer.

![Temel LLM Sohbet Tamamlama](../../../translated_images/tr/04-playground-chat-base.65b76fcfde0caa67.webp)

### Kavram: Talimat Ayarlı LLM'ler

Bir [Talimat Ayarlı LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst), temel modelle başlar ve açık talimatlar içerebilen örnekler veya giriş/çıkış çiftleri (örneğin, çok turlu "mesajlar") ile ince ayar yapılır; yapay zekanın yanıtı bu talimatı takip etmeye çalışır.

Bu, İnsan Geribildirimi ile Takviyeli Öğrenme (RLHF) gibi teknikleri kullanarak modeli _talimatları takip etmeye_ ve _geribildirimden öğrenmeye_ eğitmek üzere kullanılır; böylece pratik uygulamalara daha uygun ve kullanıcı hedefleriyle daha alakalı yanıtlar üretir.

Deneyelim - yukarıdaki istemi tekrar ziyaret edin ancak şimdi _sistem mesajını_ şu bağlamı sağlamak üzere değiştirin:

> _Verilen içeriği ikinci sınıf öğrencisi için özetleyin. Sonucu 3-5 maddeyle bir paragraf halinde tutun._

Sonucun artık istenen hedef ve biçime göre ayarlandığını görüyor musunuz? Bir eğitimci bu yanıtı doğrudan o sınıf için slaytlarında kullanabilir.

![Talimat Ayarlı LLM Sohbet Tamamlama](../../../translated_images/tr/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Neden İstem Mühendisliğine İhtiyacımız Var?

Artık istemlerin LLM'ler tarafından nasıl işlendiğini anladığımıza göre, istem mühendisliğine neden ihtiyacımız olduğunu konuşalım. Cevap, mevcut LLM'lerin bazı zorluklar ortaya koymasıyla ilgilidir; bu zorluklar, istem yapısına ve optimizasyonuna çaba sarf edilmeden _güvenilir ve tutarlı tamamlamalar_ elde etmeyi zorlaştırır. Örneğin:

1. **Model yanıtları stokastiktir.** _Aynı istem_, farklı modellerde veya model sürümlerinde muhtemelen farklı yanıtlar verecektir. Hatta _aynı model_ ile tekrarlandığında zamanla farklı sonuçlar üretilebilir. _İstem mühendisliği teknikleri, bu varyasyonları daha iyi sınırlar sunarak minimize etmemize yardımcı olur._

1. **Modeller yanıt uydurabilir.** Modeller önceden _büyük ama sınırlı_ veri kümeleriyle eğitildiğinden, eğitim kapsamı dışındaki kavramlar hakkında bilgi eksikliği vardır. Sonuç olarak, yanlış, hayali veya bilinen gerçeklerle doğrudan çelişen tamamlamalar üretebilirler. _İstem mühendisliği teknikleri, kullanıcıların yapay zekadan kaynaklar veya gerekçelendirme talep ederek bu uydurmaları tespit edip azaltmasına yardımcı olur._

1. **Model yetenekleri farklılık gösterecek.** Yeni modeller veya model nesilleri daha zengin yetenekler sunar ama maliyet & karmaşıklıkta kendine özgü farklılıklar ve ödünleşmeler getirir. _İstem mühendisliği, farkları soyutlayan ve model-spesifik gereksinimlere ölçeklenebilir, kesintisiz uyum sağlayan en iyi uygulamalar ve iş akışları geliştirmemize olanak tanır._

Bunu OpenAI veya Azure OpenAI Playground'da pratik yapalım:

- Farklı LLM dağıtımları (örneğin OpenAI, Azure OpenAI, Hugging Face) ile aynı istemi kullanın - varyasyonları gördünüz mü?  
- Aynı LLM dağıtımı (örneğin Azure OpenAI Playground) ile aynı istemi tekrar tekrar kullanın - bu varyasyonlar nasıl farklılaştı?

### Uydurmalar Örneği

Bu derste, LLM'lerin eğitimlerindeki kısıtlar veya diğer nedenlerle bazen gerçeklere aykırı bilgi üretmesini **"uydurma"** terimiyle ifade ediyoruz. Bu duruma popüler makalelerde veya araştırma makalelerinde bazen _"halüsinasyon"_ denir. Ancak davranışı insan benzeri bir özelliğe atfetmemek için _"uydurma"_ teriminin kullanılmasını şiddetle tavsiye ediyoruz. Bu aynı zamanda [Sorumlu Yapay Zeka yönergeleri](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) açısından da uygun, bazı bağlamlarda saldırgan veya kapsayıcı olmayan terimlerin kaldırılmasını pekiştirir.

Uydurmaların nasıl çalıştığını anlamak ister misiniz? Yapay zekanın eğitim veri setinde bulunmayan var olmayan bir konu için içerik üretmesini isteyen bir istem düşünün. Örneğin - şu istemi denedim:

> **İstem:** 2076 Mars Savaşı hakkında bir ders planı oluştur.
Bir web araması bana Mars savaşları hakkında kurgusal anlatımlar (örneğin, televizyon dizileri veya kitaplar) olduğunu gösterdi — ancak 2076 yılında hiçbir şey yoktu. Sağduyu da 2076’nın _gelecekte_ olduğunu ve dolayısıyla gerçek bir olayla ilişkilendirilemeyeceğini söylüyor.

Peki bu istemi farklı LLM sağlayıcılarıyla çalıştırdığımızda ne oluyor?

> **Yanıt 1**: OpenAI Playground (GPT-35)

![Yanıt 1](../../../translated_images/tr/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Yanıt 2**: Azure OpenAI Playground (GPT-35)

![Yanıt 2](../../../translated_images/tr/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Yanıt 3**: : Hugging Face Chat Playground (LLama-2)

![Yanıt 3](../../../translated_images/tr/04-fabrication-huggingchat.faf82a0a51278956.webp)

Beklendiği üzere, her model (veya model sürümü) rassal davranışlar ve model yeteneklerindeki farklılıklar nedeniyle biraz farklı yanıtlar üretiyor. Örneğin, bir model 8. sınıf seviyesini hedeflerken diğeriyse lise öğrencisini varsayıyor. Ancak üç model de, bilgi sahibi olmayan bir kullanıcıyı olayın gerçek olduğuna ikna edebilecek yanıtlar üretti.

_Metaprompting_ ve _sıcaklık yapılandırması_ gibi istem mühendisliği teknikleri, model uydurmalarını belli ölçüde azaltabilir. Yeni istem mühendisliği _mimarisileri_ de, bu etkilerin bazılarını hafifletmek veya azaltmak amacıyla araçları ve teknikleri sorunsuz biçimde istem akışına entegre eder.

## Vaka Analizi: GitHub Copilot

Bu bölümü kapatırken, gerçek dünyadaki çözümlerde istem mühendisliğinin nasıl kullanıldığını anlamak için bir vaka çalışmasına bakalım: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot, sizin "Yapay Zeka Ortak Programcınız"dır — metin istemlerini kod tamamlama haline dönüştürür ve geliştirme ortamınıza (ör. Visual Studio Code) entegre edilmiştir, böylece sorunsuz bir kullanıcı deneyimi sunar. Aşağıdaki blog dizisinde belgelenen üzere, ilk sürüm OpenAI Codex modeline dayanıyordu — mühendisler hızla modeli ince ayar yapma ve daha iyi istem mühendisliği teknikleri geliştirme ihtiyacını fark etti, böylece kod kalitesini artırdılar. Temmuz ayında, [Codex’in ötesine geçen geliştirilmiş yapay zeka modelini tanıttılar](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst), daha hızlı öneriler için.

Öğrenme yolculuklarını takip etmek için yazıları sırasıyla okuyun.

- **Mayıs 2023** | [GitHub Copilot, Kodunuzu Anlama Konusunda Daha İyi Oluyor](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mayıs 2023** | [GitHub’ın İçinden: GitHub Copilot’un Arkasındaki LLM’lerle Çalışmak](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Haziran 2023** | [GitHub Copilot İçin Daha İyi İstemler Nasıl Yazılır](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Temmuz 2023** | [GitHub Copilot, Geliştirilmiş Yapay Zeka Modeliyle Codex’in Ötesinde](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Temmuz 2023** | [Bir Geliştiricinin İstem Mühendisliği ve LLM Rehberi](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Eylül 2023** | [Bir Kurumsal LLM Uygulaması Nasıl Kurulur: GitHub Copilot’tan Dersler](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Ayrıca, [Mühendislik bloglarını](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) gezerek, bu modellerin ve tekniklerin gerçek dünya uygulamalarını nasıl _uygulandığını_ gösteren [şu gibi](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) daha fazla yazıya ulaşabilirsiniz.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## İstem Oluşturma

İstem mühendisliğinin neden önemli olduğunu gördük — şimdi, daha etkili istem tasarımı için farklı teknikleri değerlendirebilmemiz adına, istemlerin nasıl _oluşturulduğunu_ anlayalım.

### Temel İstem

Temel istemle başlayalım: modele başka bir bağlam verilmeden gönderilen bir metin girişi. Örneğin, ABD milli marşının ilk birkaç kelimesini OpenAI [Tamamlama API’sine](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) gönderdiğimizde, yanıtı anında bir sonraki birkaç satırla _tamamlar_, temel tahmin davranışını gösterir.

| İstem (Girdi)       | Tamamlama (Çıktı)                                                                                                                           |
| :------------------ | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see  | Sanki ABD’nin milli marşı "The Star-Spangled Banner"ın sözlerini yazmaya başlamışsınız gibi geliyor. Tam sözler ... olarak nedir ...     |

### Karmaşık İstem

Şimdi o temel isteme bağlam ve talimat ekleyelim. [Chat Tamamlama API](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst), karmaşık bir istemi, şu bileşenlerden oluşan bir _mesajlar_ koleksiyonu halinde oluşturmamıza izin verir:

- _Kullanıcı_ girişi ve _asistan_ yanıtını yansıtan giriş/çıkış çiftleri.
- Asistan davranışını veya kişiliğini belirleyen sistem mesajı.

İstek artık aşağıdaki biçimdedir, burada _tokenizasyon_ bağlam ve sohbetten ilgili bilgileri etkili şekilde yakalar. Artık sistem bağlamını değiştirmek, verilen kullanıcı girdileri kadar tamamlama kalitesini etkileyebilir.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Talimat İstemi

Yukarıdaki örneklerde kullanıcı istemi, bilgi talebi olarak yorumlanabilecek sade bir metin sorgusuydu. _Talimat_ istemleriyle, yapay zekaya görevi daha ayrıntılı belirtebilir ve daha iyi yol gösterici sağlayabiliriz. İşte bir örnek:

| İstem (Girdi)                                                                                                                                                                                                                         | Tamamlama (Çıktı)                                                                                                        | Talimat Türü      |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :---------------- |
| İç Savaş ile ilgili bir açıklama yaz                                                                                                              | _basit bir paragraf döndürüldü_                                                                                              | Basit             |
| İç Savaş ile ilgili bir açıklama yaz. Önemli tarihleri ve olayları ver, önemlerini anlat                                                                                 | _bir paragraf döndürdü ardından önemli olay tarihleri ve açıklamaları içeren bir liste_                                         | Karmaşık          |
| İç Savaş hakkında 1 paragrafta açıklama yaz. 3 maddeyle önemli tarihleri ve önemlerini ver. 3 maddeyle önemli tarihi kişiler ve katkılarını anlat. Çıktıyı JSON dosyası olarak döndür | _daha kapsamlı detaylar döndürür, dosyaya kopyalanıp doğrulanabilen JSON biçiminde_                                            | Karmaşık. Formatlı |

## Birincil İçerik

Yukarıdaki örneklerde, istem hâlâ oldukça açık uçluydu; modelin önceden eğitildiği veri setinden hangisinin ilgili olduğuna kendisi karar verebiliyordu. _Birincil içerik_ tasarım kalıbında, giriş metni ikiye ayrılır:

- bir talimat (eylem)
- eylemi etkileyen ilgili içerik

Burada, talimatın "Bunu 2 cümlede özetle" olduğu bir örnek var.

| İstem (Girdi)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Tamamlama (Çıktı)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jüpiter, Güneş’ten beşinci gezegen ve Güneş Sistemi’nin en büyüğüdür. Bir gaz devidir; kütlesi Güneş’in binde biri, ancak Güneş Sistemi’ndeki diğer tüm gezegenlerin toplam iki buçuk katıdır. Jüpiter, açık havada çıplak gözle görülebilen en parlak cisimlerden biridir ve antik uygarlıklar tarafından kayıtlı tarihten önce bilinmektedir. Roma tanrısı Jüpiter’in adını taşır.[19] Dünya’dan bakıldığında, yansıtılan ışığıyla gölgeler oluşturacak kadar parlak olabilir,[20] ve ay ve Venüs’ten sonra gece gökyüzündeki ortalama üçüncü en parlak doğal cisimdir. <br/> **Bunu 2 kısa cümleyle özetle** | Jüpiter, Güneş’ten beşinci gezegen olup Güneş Sistemi’nin en büyüğüdür ve gece gökyüzündeki en parlak cisimlerden biridir. Roma tanrısı Jüpiter’in adını taşır, kütlesi Güneş Sistemi’ndeki diğer tüm gezegenlerin toplamının iki buçuk katıdır. |

Birincil içerik bölümü, daha etkili talimatlar için çeşitli yollarla kullanılabilir:

- **Örnekler** — modele ne yapacağını açık talimat vermek yerine, örnekler sunarak modeli istediğiniz desenleri çıkarmaya yönlendirin.
- **İşaretler** — talimatın ardından, tamamlama için modeli hedefe yönlendiren bir "işaret" ekleyin.
- **Şablonlar** — değişkenlerle (placeholders) tanımlanmış "tarifler" olan tekrar kullanılabilir istemlerdir; belirli kullanım durumlarında veriyle özelleştirilebilir.

Şimdi bunları uygulamalı inceleyelim.

### Örnekler Kullanma

Bu yöntem, birincil içeriği modele talimat verilen çıktı örnekleri vermek ve böylece modelin istenen çıktı modelini çıkarmasına olanak tanımaktır. Verilen örnek sayısına göre sıfır atışlı, tek atışlı, az sayıda örnekli istemler yapılabilir.

İstem artık üç bileşenden oluşur:

- Bir görev tanımı
- İstenen çıktının birkaç örneği
- Yeni örneğin başlangıcı (dolaylı görev tanımı olur)

| Öğrenme Türü  | İstem (Girdi)                                                                                                                                        | Tamamlama (Çıktı)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Sıfır Atışlı  | "The Sun is Shining". İspanyolcaya çevir                                                                                                            | "El Sol está brillando".    |
| Tek Atışlı    | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Az Örnekli    | Oyuncu koşuları tamamladı => Beyzbol <br/> Oyuncu as vuruşu yaptı => Tenis <br/> Oyuncu altı sayı yaptı => Kriket <br/> Oyuncu smaç yaptı =>           | Basketbol                  |
|               |                                                                                                                                                       |                             |

Görüyorsunuz, sıfır atışta açık talimat ("İspanyolcaya çevir") vermek gerekirken, tek atışta bu örneklerden çıkarılıyor. Az örnekli ise hiç talimat vermeden, daha fazla örnek ekleyerek modeli daha doğru çıkarımlar yapmaya yönlendiriyor.

### İstem İşaretleri

Birincil içerikten yararlanmanın bir diğer yöntemi de örnekler yerine _işaretler_ sağlamaktır. Burada, model uygun yanıt biçimini yansıtan bir parçayla _başlatılır_, böylece model o biçimde devam eder.

| İşaret Sayısı  | İstem (Girdi)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Tamamlama (Çıktı)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jüpiter, Güneş’ten beşinci gezegen ve Güneş Sistemi’nin en büyüğüdür. Bir gaz devidir; kütlesi Güneş’in binde biri, ancak Güneş Sistemi’ndeki diğer tüm gezegenlerin toplam iki buçuk katıdır. Jüpiter, açık havada çıplak gözle görülebilen en parlak cisimlerden biridir ve antik uygarlıklar tarafından kayıtlı tarihten önce bilinmektedir. <br/>**Bunu Özetle**                                       | Jüpiter, Güneş Sistemi’nin en büyük gezegeni ve Güneş’ten beşinci gezegendir. Kütlesi Güneş’in binde biri olsa da, diğer tüm gezegenlerden daha ağırdır. Antik uygarlıklar Jüpiter’i uzun zamandır bilmektedir ve gece gökyüzünde kolayca görülür.                                                               |
| 1              | Jüpiter, Güneş'ten beşinci gezegen ve Güneş Sistemi'ndeki en büyüğüdür. Kütlesi Güneş'in binde biri kadar olan bir gaz devi olup, Güneş Sistemi'ndeki diğer tüm gezegenlerin birleşik kütlesinin iki buçuk katıdır. Jüpiter, gece gökyüzünde çıplak gözle görülebilen en parlak nesnelerden biridir ve kayıtlı tarihten önceki antik uygarlıklar tarafından bilinmektedir. <br/>**Bunu Özetle** <br/> Öğrendiklerimiz şudur: Jüpiter | Güneş'ten beşinci gezegen ve Güneş Sistemi'ndeki en büyüğüdür. Kütlesi Güneş'in binde biri kadar olan bir gaz devidir, ancak diğer tüm gezegenlerin birleşik kütlesinin iki buçuk katıdır. Çıplak gözle kolayca görülebilir ve antik zamanlardan beri bilinmektedir.                        |
| 2              | Jüpiter, Güneş'ten beşinci gezegen ve Güneş Sistemi'ndeki en büyüğüdür. Kütlesi Güneş'in binde biri kadar olan bir gaz devi olup, Güneş Sistemi'ndeki diğer tüm gezegenlerin birleşik kütlesinin iki buçuk katıdır. Jüpiter, gece gökyüzünde çıplak gözle görülebilen en parlak nesnelerden biridir ve kayıtlı tarihten önceki antik uygarlıklar tarafından bilinmektedir. <br/>**Bunu Özetle** <br/> Öğrendiğimiz İlk 3 Gerçek:         | 1. Jüpiter, Güneş'ten beşinci gezegen ve Güneş Sistemi'ndeki en büyüğüdür. <br/> 2. Kütlesi Güneş'in binde biri kadar olan bir gaz devidir...<br/> 3. Jüpiter antik çağlardan beri çıplak gözle görünür durumdadır ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### İpucu Şablonları

Bir ipucu şablonu, ölçeklenebilir şekilde daha tutarlı kullanıcı deneyimleri sağlamak için gerektiğinde saklanıp yeniden kullanılabilen _önceden tanımlanmış ipucu reçetesi_dir. En basit haliyle, [OpenAI'nın bu örneğinde](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) olduğu gibi, hem etkileşimli ipucu bileşenlerini (kullanıcı ve sistem mesajları) hem de API tabanlı istek formatını sağlayan bir ipucu örnekleri koleksiyonudur - yeniden kullanımı desteklemek amacıyla.

Daha karmaşık bir biçimde, [LangChain'in bu örneğinde](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) olduğu gibi, çeşitli kaynaklardan (kullanıcı girişi, sistem bağlamı, harici veri kaynakları vb.) alınan verilerle dinamik olarak bir ipucu oluşturmak için değiştirilebilen _yer tutucular_ içerir. Bu da, sürekli kullanımla tutarlı kullanıcı deneyimleri sağlamak için **programatik olarak** kullanılabilen yeniden kullanılabilir ipucu kütüphaneleri oluşturmayı mümkün kılar.

Son olarak, şablonların gerçek değeri, bir uygulama alanına özgü bağlam veya örnekler içerecek şekilde _uyarlanmış_ ve yayımlanmış _ipucu kütüphaneleri_ yaratma yeteneğinde yatar - böylece yanıtlar hedeflenen kullanıcı kitlesi için daha alakalı ve doğru olur. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) deposu, ders planlaması, müfredat tasarımı ve öğrenci eğitimi gibi önemli hedeflere odaklanarak eğitim alanına yönelik bir ipucu kütüphanesi derleyen harika bir örnektir.

## Destekleyici İçerik

Eğer ipucu yapısını bir talimat (görev) ve hedef (birincil içerik) olarak düşünürsek, _ikincil içerik_ ise çıktıyı **bir şekilde etkilemek** amacıyla sağladığımız ek bağlam gibidir. Bu, modelin yanıtını istenen kullanıcı hedeflerine veya beklentilerine uygun hale getirmesine yardımcı olabilecek ayar parametreleri, biçimlendirme talimatları, konu taksonomileri vb. olabilir.

Örneğin: Müfredattaki tüm mevcut kursların ayrıntılı meta verilerine (isim, açıklama, seviye, meta veri etiketleri, eğitmen vb.) sahip bir kurs kataloğu göz önüne alındığında:

- "2023 Güz dönemi kurs kataloğunu özetle" şeklinde bir talimat belirleyebiliriz
- İstenen çıktı için birkaç örnek sağlayan birincil içerik kullanabiliriz
- İlgi çekici en iyi 5 "etiketi" belirlemek için ikincil içerik kullanabiliriz.

Böylece model, birkaç örnekle gösterilen formatta bir özet sunabilir - ancak bir sonuçta birden fazla etiket varsa, ikincil içerikte belirttiğimiz 5 etiketi önceliklendirebilir.

---

<!--
DERS ŞABLONU:
Bu ünitede temel kavram #1 ele alınmalı.
Kavram örnekler ve referanslarla pekiştirilmeli.

KAVRAM #3:
İpucu Mühendisliği Teknikleri.
İpucu mühendisliği için bazı temel teknikler nelerdir?
Birkaç egzersizle açıklayın.
-->

## İpucu Hazırlamada En İyi Uygulamalar

İpucu nasıl _oluşturulacağını_ öğrendiğimize göre, onları _tasarlamaya_ ilişkin en iyi uygulamaları düşünmeye başlayabiliriz. Bunu iki kısımda düşünebiliriz - doğru _zihin yapısı_na sahip olmak ve doğru _teknikleri_ uygulamak.

### İpucu Mühendisliği Zihin Yapısı

İpucu mühendisliği, deneme-yanılma sürecidir; bu nedenle üç geniş rehber faktörü aklınızda tutun:

1. **Alan Bilgisi Önemlidir.** Yanıt doğruluğu ve alaka, uygulamanın veya kullanıcının faaliyet gösterdiği _alan_ ile ilişkilidir. Sezgilerinizi ve alan uzmanlığınızı kullanarak **teknikleri özelleştirin**. Örneğin, sistem ipuçlarında _alana özgü kişilikler_ tanımlayın veya kullanıcı ipuçlarında _alan bazlı şablonlar_ kullanın. Alan bağlamlarını yansıtan ikincil içerik sağlayın veya modeli tanıdık kullanım kalıplarına yönlendirmek için _alan özel ipuçları ve örnekler_ kullanın.

2. **Modeli Anlamak Önemlidir.** Modellerin doğası gereği rastgele olduğunu biliyoruz. Ancak model uygulamaları, kullandıkları eğitim veri seti (önceden eğitilmiş bilgi), sağladıkları yetenekler (ör., API veya SDK üzerinden) ve optimize edildikleri içerik türü (ör., kod vs. görüntü vs. metin) açısından farklılık gösterebilir. Kullandığınız modelin güçlü ve zayıf yanlarını anlayın ve bu bilgiyi _görev önceliklendirmesi_ veya _model yeteneklerine optimize edilmiş özelleştirilmiş şablonlar_ oluşturmak için kullanın.

3. **Yineleme ve Doğrulama Önemlidir.** Modeller hızla gelişiyor, ipucu mühendisliği teknikleri de öyle. Alan uzmanı olarak, sizin belirli uygulamanızla ilişkili farklı bağlam veya kriterleriniz olabilir; bunlar genel topluluk için geçerli olmayabilir. İpucu mühendisliği araçları ve tekniklerini kullanarak ipucu oluşturmaya "hızlı başlangıç" yapın, ardından kendi sezgileriniz ve uzmanlığınızla sonuçları yineleyin ve doğrulayın. Gözlemlerinizi kaydedin ve başkalarının daha hızlı yinelemeler yapabileceği bir **bilgi tabanı** (ör., ipucu kütüphaneleri) oluşturun.

## En İyi Uygulamalar

Şimdi, [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) ve [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) uzmanlarının önerdiği yaygın en iyi uygulamalara bakalım.

| Ne                              | Neden                                                                                                                                                                                                                                               |
| :------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| En yeni modelleri değerlendirin | Yeni model nesilleri muhtemelen daha gelişmiş özellikler ve kalite sunar - ancak maliyeti de artabilir. Etkisini değerlendirin ve ardından geçiş kararları verin.                                                                                     |
| Talimatları ve bağlamı ayırın   | Modelinizin/sağlayıcınızın talimatları, birincil ve ikincil içerikleri daha net ayırmak için _sınırlayıcılar_ tanımlayıp tanımlamadığını kontrol edin. Bu, modelin tokenlara daha doğru ağırlık vermesine yardımcı olabilir.                            |
| Spesifik ve net olun            | İstenen bağlam, çıktı, uzunluk, format, stil vb. hakkında daha fazla ayrıntı verin. Bu, yanıt kalitesi ve tutarlılığını artırır. Tarifleri yeniden kullanılabilir şablonlarda kaydedin.                                                             |
| Betimleyici olun, örnekler kullanın   | Modeller, "göster ve anlat" yaklaşımına daha iyi yanıt verebilir. Önce talimat (örneksiz, sıfır vuruş) verip sonra birkaç örnek (az vuruş) ile rafine etmeyi deneyin. Analoji kullanın.                                                               |
| Yanıtları başlatmak için ipuçları kullanın | Yanıt için başlangıç olarak kullanılabilecek bazı öncü kelime veya ifadeler vererek modeli istenen sonuca yönlendirin.                                                                                                                               |
| Tekrarlayın                     | Bazen modeli tekrarlamanız gerekebilir. Talimatları birincil içerikten önce ve sonra verin, talimat ve ipucunu birlikte kullanın vb. Ne işe yaradığını görmek için yineleyin ve doğrulayın.                                                         |
| Sıra Önemlidir                 | Bilgiyi modele sunma sırası çıktıyı etkileyebilir; öğrenme örneklerinde bile, yakınlık önceliği nedeniyle. En iyi sonucu görmek için farklı seçenekleri deneyin.                                                                                      |
| Modele bir “çıkış” verin        | Modelin görevi tamamlayamadığında verebileceği bir _geri dönüş_ yanıtı sağlayın. Bu, modelin yanlış veya uydurma yanıtlar üretme olasılığını azaltabilir.                                                                                            |
|                                |                                                                                                                                                                                                                                                    |

Herhangi bir en iyi uygulamada olduğu gibi, _sizin deneyiminiz model, görev ve alana göre farklılık gösterebilir_. Bunları başlangıç noktası olarak kullanın ve size en uygun olanı bulmak için yineleyin. Yeni modeller ve araçlar kullanılabilir hale geldikçe, süreç ölçeklenebilirliğine ve yanıt kalitesine odaklanarak ipucu mühendisliği sürecinizi sürekli yeniden değerlendirin.

<!--
DERS ŞABLONU:
Bu ünitede uygulanabilir ise bir kod görevi verin

GÖREV:
Yalnızca kod yorumları içeren, kod bölümleri boş bir Jupyter Not defterine bağlantı.

ÇÖZÜM:
O not defterinin doldurulmuş ve çalıştırılmış bir kopyasına bağlantı, referans için bir örnek çıktı gösterir.
-->

## Ödev

Tebrikler! Dersin sonuna geldiniz! Şimdi bu kavramlar ve tekniklerin bazılarının gerçek örneklerle test edilme zamanı!

Ödevimiz için, etkileşimli olarak tamamlayabileceğiniz egzersizler içeren bir Jupyter Not defteri kullanacağız. Kendi fikirlerinizi ve tekniklerinizi keşfetmek için not defterini Markdown ve Kod hücreleri ile genişletebilirsiniz.

### Başlamak için, repo'yu çatalla ve ardından

- (Önerilen) GitHub Codespaces’i başlatın
- (Alternatif) Repositoriyi yerel aygıtınıza klonlayın ve Docker Desktop ile kullanın
- (Alternatif) Tercih ettiğiniz Not defteri çalışma zaman ortamı ile Not defterini açın.

### Sonra, ortam değişkenlerinizi yapılandırın

- Depo kökündeki `.env.copy` dosyasını `.env` olarak kopyalayın ve `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` ve `AZURE_OPENAI_DEPLOYMENT` değerlerini doldurun. Nasıl yapacağını öğrenmek için [Öğrenme Kum Havuzu bölümü](#öğrenme-sandboxu)'ne geri dönün.

### Sonra, Jupyter Not defterini açın

- Çalışma zamanı çekirdeğini seçin. 1 veya 2. seçenek kullanılıyorsa, geliştirme konteynerinin sağladığı varsayılan Python 3.10.x çekirdeğini seçmeniz yeterlidir.

Egzersizleri çalıştırmaya hazırsınız. Burada doğru ya da yanlış cevaplar yoktur - sadece deneme-yanılma yoluyla seçenekleri keşfetmek ve belirli bir model ve uygulama alanı için neyin işe yaradığını sezmek amaçlanmıştır.

_Bu nedenle ders içinde Kod Çözüm bölümleri yoktur. Bunun yerine, Not defteri "Çözümüm:" başlıklı Markdown hücreleri içerir ve referans için tek bir örnek çıktı gösterir._

 <!--
DERS ŞABLONU:
Bölümü özetle kapatıp kendi kendine öğrenme için kaynaklar sağlayın.
-->

## Bilgi Kontrolü

Aşağıdakilerden hangisi makul bazı en iyi uygulamaları takip eden iyi bir ipucudur?

1. Bana kırmızı bir arabanın resmini göster
2. Bana kırmızı Volvo marka XC90 model bir arabanın güneş batarken bir uçurum kenarında park edilmiş resmini göster
3. Bana kırmızı Volvo marka XC90 model bir arabanın resmini göster

Cevap: 2, çünkü hem "ne" olduğu hakkında detay verir hem de çevreyi tanımlar (sadece herhangi bir araba değil, belirli bir marka ve model). 3 ise oldukça açıklayıcı olduğu için ikinci en iyisidir.

## 🚀 Zorluk

"İpucu" tekniğini kullanarak şu ipucu ile deneyin: Cümleyi tamamla "Bana kırmızı Volvo marka bir arabanın ... göster". Model ne yanıt veriyor ve siz bunu nasıl geliştirirsiniz?

## Harika İş! Öğrenmeye Devam Et

Farklı İpucu Mühendisliği kavramları hakkında daha fazla bilgi edinmek ister misiniz? Bu konudaki diğer harika kaynakları bulmak için [devam eden öğrenme sayfasına](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) gidin.

Devamında, 5. Derse gidin; burada [ileri ipucu tekniklerine](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst) bakacağız!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->