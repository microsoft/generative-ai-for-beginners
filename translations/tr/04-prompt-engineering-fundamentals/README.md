# İstek Mühendisliğinin Temelleri

[![İstek Mühendisliğinin Temelleri](../../../translated_images/tr/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Giriş
Bu modül, üretken yapay zekâ modellerinde etkili istekler oluşturmak için temel kavramları ve teknikleri kapsar. Büyük Dil Modeline (LLM) yazdığınız istek şekli de önemlidir. Özenle hazırlanmış bir istek, daha iyi bir yanıt kalitesi elde edebilir. Peki tam olarak _istek_ ve _istek mühendisliği_ gibi terimler ne anlama geliyor? Ve LLM'ye gönderdiğimiz istek _girdiğini_ nasıl iyileştirebiliriz? Bu soruları bu bölümde ve sonraki bölümde yanıtlamaya çalışacağız.

_Üretken Yapay Zekâ_, kullanıcı taleplerine yanıt olarak yeni içerik (örneğin, metin, resim, ses, kod vb.) oluşturabilir. Bunu doğal dil ve kod kullanmak üzere eğitilmiş OpenAI'nin GPT ("Üretken Önceden Eğitilmiş Dönüştürücü") serisi gibi _Büyük Dil Modelleri_ (LLM) ile başarır.

Kullanıcılar artık bu modellerle teknik bilgi veya eğitim olmadan, sohbet gibi tanıdık paradigmalar kullanarak etkileşim kurabiliyorlar. Modeller _istek tabanlıdır_ - kullanıcılar bir metin girdisi (istek) gönderir ve yapay zekânın yanıtını (tamamlama) alır. Ardından çok turlu görüşmelerle "yapay zekâyla sohbet" edebilir, isteklerini beklentilerine uyana kadar yineleyerek geliştirebilirler.

"İstekler" artık üretken yapay zekâ uygulamaları için ana _programlama arayüzü_ haline gelir, modellere ne yapacaklarını söyler ve dönen yanıtların kalitesini etkiler. "İstek Mühendisliği", ölçekli tutarlı ve kaliteli yanıtlar sağlamak için _tasarım ve optimizasyon_ üzerine odaklanan hızla büyüyen bir çalışma alanıdır.

## Öğrenme Hedefleri

Bu derste, İstek Mühendisliğinin ne olduğunu, neden önemli olduğunu ve verilen bir model ve uygulama hedefi için daha etkili istekler nasıl oluşturabileceğimizi öğreniyoruz. Temel kavramları ve istek mühendisliği için en iyi uygulamaları anlayacak - ayrıca gerçek örneklerde uygulanan bu kavramları görebileceğimiz etkileşimli Jupyter Notebook "oyun alanı" ortamını tanıyacağız.

Bu dersin sonunda şunları yapabileceğiz:

1. İstek mühendisliğinin ne olduğunu ve neden önemli olduğunu açıklamak.
2. İsteğin bileşenlerini tanımlamak ve nasıl kullanıldığını anlatmak.
3. İstek mühendisliği için en iyi uygulama ve teknikleri öğrenmek.
4. Öğrenilen teknikleri gerçek örneklere uygulamak; OpenAI uç noktası kullanmak.

## Anahtar Terimler

İstek Mühendisliği: Yapay zekâ modellerini istenilen çıktılar üretmeye yönlendirmek için girdilerin tasarlanması ve iyileştirilmesi uygulaması.
Tokenizasyon: Metni modelin anlayıp işleyebileceği daha küçük birimler (token'lar) haline dönüştürme süreci.
Talimat-Ayarlanmış LLM'ler: Yanıt doğruluğu ve alaka düzeyini artırmak için belirli talimatlarla ince ayar yapılmış Büyük Dil Modelleri.

## Öğrenme Oyun Alanı

İstek mühendisliği şu anda daha çok sanatla ilgilidir. Sezgimizi geliştirmek için en iyi yol _daha çok pratik yapmak_ ve uygulama alanı uzmanlığını önerilen tekniklerle ve model-özel optimizasyonlarla birleştiren deneme-yanılma yaklaşımını benimsemektir.

Bu derse eşlik eden Jupyter Notebook, öğrendiklerinizi deneyebileceğiniz bir _oyun alanı_ ortamı sağlar - ilerledikçe veya sonunda yapacağınız kod meydan okuması bölümünde. Egzersizleri çalıştırmak için şunlara ihtiyacınız olacak:

1. **Bir Azure OpenAI API anahtarı** - dağıtılmış bir LLM için hizmet uç noktası.
2. **Bir Python Çalışma Zamanı** - Notebook'u çalıştırmak için.
3. **Yerel Ortam Değişkenleri** - _hazırlık için [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) adımlarını şimdi tamamlayın_.

Notebook başlangıç egzersizleri ile gelir - ancak kendi _Markdown_ (açıklama) ve _Kod_ (istek talepleri) bölümlerinizi ekleyerek daha fazla örnek veya fikir denemeniz ve istek tasarımı konusunda sezginizi geliştirmeniz teşvik edilir.

## Görselleştirilmiş Rehber

Bu derse başlamadan önce kapsamın ana hatlarını görmek ister misiniz? Bu görselleştirilmiş rehber, ele alınan temel konular ve her biri için düşünmeniz gereken önemli çıkarımlar hakkında size bir fikir verir. Ders yol haritası, temel kavramları ve zorlukları anlamanızdan başlayarak ilgili istek mühendisliği teknikleri ve en iyi uygulamalarla bunları ele almaya götürür. Bu rehberdeki "İleri Teknikler" bölümü, bu müfredatın _bir sonraki_ bölümündeki içeriğe atıfta bulunmaktadır.

![İstek Mühendisliğine Görselleştirilmiş Rehber](../../../translated_images/tr/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Girişimimiz

Şimdi, _bu konu_nun [eğitime yapay zekâ yeniliği getirme](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst) girişimimizle nasıl ilişkili olduğunu konuşalım. Amacımız, _kişiselleştirilmiş öğrenme_ için yapay zekâ destekli uygulamalar geliştirmek - o halde uygulamamızın farklı kullanıcılarının istekleri nasıl "tasarlayabileceğini" düşünelim:

- **Yöneticiler**, AI'dan _müfredat verilerini analiz ederek kapsam boşluklarını belirlemesini_ isteyebilir. AI sonuçları özetleyebilir veya kod ile görselleştirebilir.
- **Eğitmenler**, AI'dan _hedef kitle ve konu için bir ders planı oluşturmasını_ isteyebilir. AI belirtilen formatta kişiselleştirilmiş planı hazırlayabilir.
- **Öğrenciler**, AI'dan _zor bir konuda onları eğitmesini_ isteyebilir. AI şimdi öğrencilere seviyelerine uygun dersler, ipuçları ve örnekler sunabilir.

Bu sadece buzdağının görünen kısmı. Daha geniş imkanları görmek için eğitim uzmanları tarafından derlenen açık kaynaklı istek kütüphanesi [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst)'a göz atın! _Bu istekleri oyun alanında veya OpenAI Playground'da çalıştırmayı deneyin ve ne olduğunu görün!_

<!--
DERS ŞABLONU:
Bu ünitede temel kavram #1 ele alınmalıdır.
Konuyu örnekler ve referanslarla pekiştirin.

KAVRAM #1:
İstek Mühendisliği.
Tanımlayın ve neden gerekli olduğunu açıklayın.
-->

## İstek Mühendisliği Nedir?

Bu derse **İstek Mühendisliği**ni, belirli bir uygulama hedefi ve model için tutarlı ve kaliteli yanıtlar (tamalamalar) sağlamak üzere metin girdilerini (istekleri) _tasarlama ve optimize etme_ süreci olarak tanımlayarak başladık. Bunu 2 aşamalı bir süreç olarak düşünebiliriz:

- Belirli bir model ve hedef için ilk isteği _tasarlamak_
- Yanıt kalitesini artırmak için isteği yineleyerek _iyileştirmek_

Bu, optimum sonuçlar için kullanıcı sezgisi ve çaba gerektiren doğası gereği deneme-yanılma sürecidir. Peki neden önemlidir? Bu soruyu yanıtlamak için önce üç kavramı anlamamız gerekir:

- _Tokenizasyon_ = modelin isteği "görme" biçimi
- _Temel LLM'ler_ = temel modelin isteği nasıl "işlediği"
- _Talimat-Ayarlanmış LLM'ler_ = modelin artık "görevleri" nasıl görebildiği

### Tokenizasyon

Bir LLM, istekleri _token dizisi_ olarak görür; farklı modeller (veya model sürümleri) aynı isteği farklı şekillerde tokenlaştırabilir. LLM'ler token'lar üzerinde (ham metin üzerinde değil) eğitildiklerinden, tokenizasyon şekli üretilen yanıt kalitesini doğrudan etkiler.

Tokenizasyonun nasıl çalıştığı hakkında sezgi geliştirmek için aşağıda gösterilen [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) gibi araçları deneyin. İsteğinizi kopyalayın ve tokenlara nasıl dönüştüğünü görün; boşluk karakterleri ve noktalama işaretlerinin nasıl ele alındığına dikkat edin. Bu örnek eski bir LLM (GPT-3) gösteriyor - daha yeni modellerle denemek farklı sonuçlar verebilir.

![Tokenizasyon](../../../translated_images/tr/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Kavram: Temel Modeller

Bir istek tokenize edildikten sonra, ["Temel LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (veya Temel model) dizideki tokeni tahmin etmeye çalışır. LLM'ler büyük metin veri setlerinde eğitildiği için tokenlar arasındaki istatistiksel ilişkileri iyi bilir ve bu tahmini belirli bir güvenle yapabilir. Kelimelerin _anlamını_ anlayamazlar; sadece "tamamlayabilecekleri" bir kalıp görürler. Kullanıcı müdahalesi veya önceden belirlenmiş bir koşul tarafından durdurulana kadar tahmine devam edebilirler.

İstek tabanlı tamamlama işlemini görmek ister misiniz? Yukarıdaki isteği varsayılan ayarlarla [Microsoft Foundry oyun alanı](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)'na girin. Sistem, istekleri bilgi talepleri olarak değerlendirecek şekilde yapılandırılmıştır - bu nedenle bu bağlama uygun bir tamamlama görmelisiniz.

Peki ya kullanıcı belirli bir kriter veya görev hedefine uygun bir yanıt görmek isterse? İşte burada _talimat-ayarlanmış_ LLM'ler devreye girer.

![Temel LLM Sohbet Tamamlama](../../../translated_images/tr/04-playground-chat-base.65b76fcfde0caa67.webp)

### Kavram: Talimat-Ayarlanmış LLM'ler

Bir [Talimat Ayarlanmış LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst), temel model ile başlar ve örnekler veya girdi/çıktı çiftleri (ör., çok tur "mesajlar") kullanarak ince ayar yapar; bu girdiler açık talimatlar içerir ve yapay zekânın yanıtı bu talimatları izlemeye çalışır.

Bu, Modelin _talimatları izlemeyi_ ve _geri bildirimden öğrenmeyi_ öğrenmesini sağlayan İnsan Geri Bildirimi ile Pekiştirmeli Öğrenme (RLHF) gibi teknikler kullanır. Böylece cevaplar pratik uygulamalara daha uygun ve kullanıcı hedeflerine daha alakalı olur.

Hadi deneyelim - yukarıdaki isteğe dönün ve _sistem mesajını_ aşağıdaki talimatı bağlam olarak verin:

> _Elinizdeki içeriği ikinci sınıf öğrencisi için özetleyin. Sonucu 3-5 madde ile bir paragraf halinde tutun._

Sonucun istenen hedef ve formata uygun hale getirildiğini gördünüz mü? Bir eğitimci artık bu yanıtı doğrudan sınıf sunumunda kullanabilir.

![Talimat Ayarlanmış LLM Sohbet Tamamlama](../../../translated_images/tr/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## Neden İstek Mühendisliğine İhtiyacımız Var?

İsteklerin LLM'ler tarafından nasıl işlendiğini öğrendiğimize göre, şimdi de _neden_ istek mühendisliğine ihtiyacımız olduğunu konuşalım. Cevap, mevcut LLM'lerin _güvenilir ve tutarlı tamamalara_ ulaşmayı zorlaştıran pek çok zorluk barındırmasında yatar; bu nedenle istek yapısına ve optimizasyona efor vermek gerekir. Örneğin:

1. **Model yanıtları rastgeledir.** _Aynı istek_, farklı modeller veya model sürümleriyle farklı yanıtlar verebilir. Ve _aynı model_ ile farklı zamanlarda değişik sonuçlar doğurabilir. _İstek mühendisliği teknikleri bu varyasyonları minimize etmeye yardımcı olabilir, daha iyi sınırlar sağlayarak_.

1. **Modeller uydurma yapabilir.** Modeller _büyük fakat sınırlı_ veri setleriyle önceden eğitildiğinden, eğitim kapsamı dışındaki kavramlarla ilgili bilgi eksikliği vardır. Bunun sonucu olarak hatalı, hayali veya gerçek bilgilerle tam ters düşen yanıtlar üretebilirler. _İstek mühendisliği teknikleri, kullanıcıların bu uydurmaları tespit etmesine ve hafifletmesine yardımcı olur; örneğin yapay zekadan kaynakça istemek veya mantıklı çıkarımlar talep etmek gibi_.

1. **Modellerin yetenekleri farklı olur.** Yeni modeller veya nesiller daha güçlü özelliklere sahip olur ama maliyet ve karmaşıklıkta özgün zorluklar ve takaslar getirir. _İstek mühendisliği en iyi uygulamalar ve iş akışları geliştirerek farkları soyutlayabilir, model özel gereksinimlere ölçeklenebilir ve sorunsuz uyum sağlayabilir_.

Bunu OpenAI veya Azure OpenAI Playground’da uygulamada görelim:

- Aynı isteği farklı LLM dağıtımları (ör., OpenAI, Azure OpenAI, Hugging Face) ile kullanın - varyasyonlar gördünüz mü?
- Aynı isteği _aynı_ LLM dağıtımı ile tekrar tekrar kullanın (ör., Azure OpenAI playground) - bu varyasyonlar nasıl farklılık gösterdi?

### Uydurma Örneği

Bu kursta, LLM'lerin bazen eğitim sınırlamaları veya diğer kısıtlar nedeniyle yanlış bilgi üretmesi olgusunu ifade etmek için **"uydurma"** terimini kullanıyoruz. Popüler makalelerde veya araştırmalarda buna _"halüsinasyonlar"_ denildiğini de duymuş olabilirsiniz. Ancak _"uydurma"_ terimini kullanmanızı şiddetle tavsiye ediyoruz; böylece bir makine kaynaklı sonucu yanlışlıkla insanlaştırarak insan benzeri bir özellik atfetmemiş oluruz. Bu aynı zamanda terminoloji açısından [Sorumlu Yapay Zekâ yönergelerini](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) destekler, bazı bağlamlarda saldırgan veya kapsayıcı olmayan terimleri ortadan kaldırır.

Uydurmaların nasıl işlediğine dair bir fikriniz olsun mu? AI'yı, eğitim veri setinde bulunmadığından emin olmak için var olmayan bir konu hakkında içerik üretmesi talimatını veren bir isteği düşünün. Örneğin - şu isteği denedim:

> **İstek:** 2076 Mars Savaşı hakkında bir ders planı oluşturun.

Web araması, Mars savaşları hakkında kurgusal hikayeler (örneğin dizi veya kitap) olduğunu gösterdi - ancak 2076 yılı için değil. Sağduyu da 2076'nın _gelecekte_ olduğunu ve gerçek bir olayla ilişkilendirilemeyeceğini söyler.


Peki, bu istemi farklı LLM sağlayıcılarıyla çalıştırdığımızda ne oluyor?

> **Yanıt 1**: OpenAI Playground (GPT-35)

![Yanıt 1](../../../translated_images/tr/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Yanıt 2**: Azure OpenAI Playground (GPT-35)

![Yanıt 2](../../../translated_images/tr/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Yanıt 3**: : Hugging Face Chat Playground (LLama-2)

![Yanıt 3](../../../translated_images/tr/04-fabrication-huggingchat.faf82a0a51278956.webp)

Beklendiği gibi, her model (veya model sürümü), stokastik davranış ve model yeteneklerindeki farklılıklar nedeniyle biraz farklı yanıtlar üretir. Örneğin, bir model 8. sınıf öğrencisini hedeflerken diğeri lise öğrencisi varsayımı yapıyor. Ancak üç model de bilinçsiz bir kullanıcıyı olayın gerçek olduğuna ikna edebilecek yanıtlar üretti.

_Metaprompting_ ve _sıcaklık yapılandırması_ gibi istem mühendisliği teknikleri, model uydurmalarını bir dereceye kadar azaltabilir. Yeni istem mühendisliği _mimarileri_ ayrıca bazı bu etkileri hafifletmek veya azaltmak için yeni araçları ve teknikleri istem akışına sorunsuzca entegre eder.

## Vaka İncelemesi: GitHub Copilot

Bu bölümü, gerçek dünyadaki çözümlerde istem mühendisliğinin nasıl kullanıldığını anlamak için bir Vaka İncelemesine bakarak tamamlayalım: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot sizin "Yapay Zeka Eş Programcınız"dır - metin istemlerini kod tamamlamalarına dönüştürür ve geliştirme ortamınıza (örneğin Visual Studio Code) entegre edilmiştir, kesintisiz bir kullanıcı deneyimi sağlar. Aşağıdaki blog serilerinde belgelenen erken sürümü OpenAI Codex modeline dayanıyordu - mühendisler modelin yeniden ayarlanması ve kod kalitesini artırmak için daha iyi istem mühendisliği teknikleri geliştirilmesi gerektiğini hızla fark ettiler. Temmuz ayında, daha da hızlı öneriler için [Codex'in ötesine geçen geliştirilmiş bir AI modeli](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) piyasaya sürdüler.

Öğrenme yolculuklarını takip etmek için yazıları sırasıyla okuyun.

- **Mayıs 2023** | [GitHub Copilot Kodunuzu Anlamada Daha İyi Oluyor](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mayıs 2023** | [GitHub İçinden: GitHub Copilot Arkasındaki LLM’lerle Çalışmak](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Haziran 2023** | [GitHub Copilot İçin Daha İyi İstemler Nasıl Yazılır](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Temmuz 2023** | [.. GitHub Copilot, Geliştirilmiş AI Modeliyle Codex’in Ötesine Geçiyor](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Temmuz 2023** | [Bir Geliştiricinin İstem Mühendisliği ve LLM’ler Rehberi](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Eylül 2023** | [Kurumsal Bir LLM Uygulaması Nasıl Kurulur: GitHub Copilot’tan Dersler](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

Ayrıca [Mühendislik bloglarını](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) şöyle örnek [bir yazı](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) gibi göz atabilirsiniz. Bu yazı, bu modellerin ve tekniklerin gerçek dünya uygulamalarını yönlendirmek için nasıl _uygulandığını_ göstermektedir.

---

<!--
DERS ŞABLONU:
Bu birim temel kavram #2'yi kapsamalıdır.
Kavramı örnekler ve referanslarla güçlendirin.

KAVRAM #2:
İstem Tasarımı.
Örneklerle gösterilmiştir.
-->

## İstem Oluşturma

İstem mühendisliğinin neden önemli olduğunu gördük - şimdi istemlerin nasıl _oluşturulduğunu_ anlayalım ki, daha etkili istem tasarımı için farklı teknikleri değerlendirebilelim.

### Temel İstem

Temel istemle başlayalım: modele başka bir bağlam olmadan gönderilen bir metin girişi. İşte bir örnek - ABD milli marşının ilk birkaç kelimesini OpenAI [Completion API'sine](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) gönderdiğimizde model anında yanıtı sonraki birkaç satırla _tamamlar_, temel tahmin davranışını gösterir.

| İstem (Girdi)        | Tamamlama (Çıktı)                                                                                                                             |
| :------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see    | "The Star-Spangled Banner" (Yıldızlı Bayrak Marşı), Amerika Birleşik Devletleri milli marşının sözlerine başlamış gibi görünüyorsunuz. Tam sözler ... |

### Karmaşık İstem

Şimdi bu temel isteme bağlam ve talimat ekleyelim. [Chat Completion API](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst), bir koleksiyon olarak karmaşık bir istem oluşturmamıza izin verir: _mesajlar_ içeren,

- _kullanıcı_ girişi ve _yardımcı_ yanıtını yansıtan giriş/çıkış çiftleri.
- Yardımcının davranışı veya kişiliği için bağlam belirleyen sistem mesajı.

İstek artık aşağıdaki şeklindedir, burada _tokenizasyon_ bağlam ve konuşmadan ilgili bilgileri etkin şekilde yakalar. Sistem bağlamının değiştirilmesi, sağlanan kullanıcı girdileri kadar tamamlamaların kalitesi üzerinde etkili olabilir.

```python
response = client.responses.create(
    model="gpt-5-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Talimat İstemi

Yukarıdaki örneklerde kullanıcı istemi, bilgi talebi olarak yorumlanabilecek basit bir metin sorgusuydu. _Talimat_ istemlerinde, bu metni görevi daha ayrıntılı belirtmek için kullanabilir ve AI’ye daha iyi rehberlik sağlayabiliriz. İşte bir örnek:

| İstem (Girdi)                                                                                                                                                                                                                         | Tamamlama (Çıktı)                                                                                                        | Talimat Türü       |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Write a description of the Civil War                                                                                                                                                                                                   | _basit bir paragraf döndü_                                                                                                | Basit              |
| Write a description of the Civil War. Provide key dates and events and describe their significance                                                                                                                                     | _paragrafın ardından olay tarihlerini ve açıklamalarını içeren liste döndü_                                             | Karmaşık           |
| Write a description of the Civil War in 1 paragraph. Provide 3 bullet points with key dates and their significance. Provide 3 more bullet points with key historical figures and their contributions. Return the output as a JSON file | _daha kapsamlı ayrıntılar döner, JSON biçiminde metin kutusunda, dosyaya yapıştırıp doğrulayabilirsiniz_                 | Karmaşık. Biçimlendirilmiş. |

## Birincil İçerik

Yukarıdaki örneklerde, istem hala oldukça açık uçlu, LLM’nin önceden eğitilmiş veri seti içinde hangi kısmın ilgili olduğuna karar vermesine izin veriyor. _Birincil içerik_ tasarım deseninde ise, giriş metni iki kısma ayrılır:

- bir talimat (eylem)
- eylemi etkileyen ilgili içerik

İşte "bunu 2 cümlede özetle" talimatı verilen örnek.

| İstem (Girdi)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Tamamlama (Çıktı)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jupiter, Güneş'ten beşinci gezegen ve Güneş Sistemi'nde en büyüğüdür. Güneş'in kütlesinin binde biri kadar bir kütleye sahip bir gaz devidir, ancak Güneş Sistemi'ndeki diğer tüm gezegenlerin toplamından iki buçuk kat fazladır. Jüpiter, çıplak gözle gece gökyüzünde görülebilen en parlak nesnelerden biridir ve tarih öncesinden beri eski uygarlıklar tarafından bilinmektedir. Roma tanrısı Jüpiter'in adını almıştır.[19] Dünya'dan bakıldığında, yansıyan ışığı görünür gölgeler oluşturacak kadar parlak olabilir,[20] ve ortalama olarak Ay ve Venüs'ten sonra gece gökyüzündeki en parlak üçüncü doğal nesnedir. <br/> **Bunu 2 kısa cümle olarak özetleyin** | Jupiter, Güneş'ten beşinci gezegen olup Güneş Sistemi'ndeki en büyük gezegendir ve gece gökyüzündeki en parlak nesnelerden biridir. Roma tanrısı Jüpiter'in adını taşıyan bu gaz devi, Güneş Sistemi'ndeki diğer tüm gezegenlerin toplam kütlesinin iki buçuk katıdır. |

Birincil içerik bölümü, daha etkili talimatlar vermek için çeşitli şekillerde kullanılabilir:

- **Örnekler** - modele ne yapacağını açıkça talimat vermek yerine, ne yapması gerektiğine dair örnekler verip kalıbı çıkarılması sağlanır.
- **İpuçları** - talimattan sonra tamamlamayı yönlendiren ve modeli daha ilgili yanıtlar vermeye sevk eden bir "ipuçları" verilir.
- **Şablonlar** - bunlar, belirli kullanım durumları için veriyle özelleştirilebilen değişkenler (yer tutucular) içeren tekrar edilebilir istem "tarifleri"dir.

Bunları uygulamada keşfedelim.

### Örnekleri Kullanmak

Bu yaklaşımda birincil içerik, modele belirli bir talimat için istenen çıktıdan bazı örnekler "verilir" ve model bu örneklerden kalıbı çıkarır. Verilen örnek sayısına bağlı olarak sıfır-görüşlü, tek-görüşlü, az-görüşlü istemleme gibi teknikler uygulanabilir.

İstem artık üç bileşenden oluşur:

- Bir görev açıklaması
- İstenen çıktıya ait birkaç örnek
- Yeni bir örneğin başlangıcı (bu gizli bir görev açıklaması olur)

| Öğrenme Türü | İstem (Girdi)                                                                                                                              | Tamamlama (Çıktı)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Sıfır-görüşlü | "The Sun is Shining". İspanyolcaya çevir                                                                                                  | "El Sol está brillando".    |
| Tek-görüşlü   | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                     | "Es un día frío y ventoso". |
| Az-görüşlü   | Oyuncu koşularını bitirdi => Beyzbol <br/> Oyuncu as vurdu => Tenis <br/> Oyuncu altılık vurdu => Kriket <br/> Oyuncu smaç yaptı =>         | Basketbol                  |
|               |                                                                                                                                          |                             |

Sıfır-görüşlü istemlemede açık talimat ("İspanyolcaya çevir") vermemiz gerektiğine dikkat edin, ancak tek-görüşlü örnekte bu çıkarılmıştır. Az-görüşlü örnek, daha fazla örnek eklemenin ek talimat verilmeksizin modellerin daha doğru çıkarımlar yapmasını sağladığını gösteriyor.

### İstem İpuçları

Birincil içeriği kullanmanın diğer bir yöntemi, örnekler yerine _ipuçları_ sağlamaktır. Bu durumda, modelin doğru yönde başlaması için istenilen yanıt biçimini yansıtan bir parçayla _başlatıyoruz_. Model "ipuçunu alır" ve bu doğrultuda devam eder.

| İpucu Sayısı | İstem (Girdi)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Tamamlama (Çıktı)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Jupiter, Güneş'ten beşinci gezegen ve Güneş Sistemi'nde en büyüğüdür. Güneş'in kütlesinin binde biri kadar bir kütleye sahip bir gaz devidir, ancak Güneş Sistemi'ndeki diğer tüm gezegenlerin toplamından iki buçuk kat fazladır. Jüpiter, çıplak gözle gece gökyüzünde görülebilen en parlak nesnelerden biridir ve tarih öncesinden beri eski uygarlıklar tarafından bilinmektedir. <br/>**Bunu Özetle**                                       | Jupiter, Güneş Sistemi'ndeki en büyük gezegendir ve Güneş'ten beşinci sıradadır. Güneş'in binde biri kütlesinde bir gaz devidir, ancak diğer tüm gezegenlerden daha ağırdır. Eski uygarlıklar tarafından uzun zamandır bilinmekte ve gece gökyüzünde kolayca görünür. |
| 1              | Jupiter, Güneş'ten beşinci gezegen ve Güneş Sistemi'nde en büyüğüdür. Güneş'in kütlesinin binde biri kadar bir kütleye sahip bir gaz devidir, ancak Güneş Sistemi'ndeki diğer tüm gezegenlerin toplamından iki buçuk kat fazladır. Jüpiter, çıplak gözle gece gökyüzünde görülebilen en parlak nesnelerden biridir ve tarih öncesinden beri eski uygarlıklar tarafından bilinmektedir. <br/>**Bunu Özetle** <br/> Bildiğimiz şu ki Jupiter | Güneş'ten beşinci gezegendir ve Güneş Sistemi'ndeki en büyük gezegendir. Güneş'in kütlesinin binde biri kadar bir kütleye sahip bir gaz devidir, ancak diğer tüm gezegenlerin toplamından iki buçuk kat fazladır. Çıplak gözle görünür ve eski zamanlardan beri bilinmektedir.                        |

| 2              | Jüpiter, Güneş'ten beşinci gezegen ve Güneş Sistemi'nin en büyüğüdür. Güneş'in kütlesinin binde biri kadar olan bir gaz devidir, ancak Güneş Sistemi'ndeki diğer tüm gezegenlerin toplam kütlesinin iki buçuk katıdır. Jüpiter, çıplak gözle gece gökyüzünde görülebilen en parlak cisimlerden biridir ve yazılı tarihten önceki kadim medeniyetlerce bilinmektedir. <br/>**Bunu Özetle** <br/> Öğrendiğimiz İlk 3 Gerçek:         | 1. Jüpiter, Güneş'ten beşinci gezegen ve Güneş Sistemi'nin en büyüğüdür. <br/> 2. Güneş'in kütlesinin binde biri kadar olan bir gaz devidir...<br/> 3. Jüpiter, antik çağlardan beri çıplak gözle görülebilmektedir ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### İstek Şablonları

Bir istek şablonu, ölçeklendirilmiş olarak daha tutarlı kullanıcı deneyimleri sağlamak için gerektiğinde saklanıp yeniden kullanılabilen _önceden tanımlanmış bir istek tarifi_ dir. En basit haliyle, etkileşimli istek bileşenlerini (kullanıcı ve sistem mesajları) ve API aracılığıyla yapılan istek formatını sağlayan [OpenAI'den bu örnek](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) gibi bir istek örnekleri koleksiyonudur - yeniden kullanım için destek sağlar.

Daha karmaşık formunda, [LangChain'den bu örnek](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst) gibi, _yer tutucular_ içerir ve bunlar çeşitli kaynaklardan (kullanıcı girişi, sistem bağlamı, dış veri kaynakları vb.) gelen verilerle değiştirilerek dinamik olarak istek oluşturulabilir. Bu sayede, tutarlı kullanıcı deneyimlerini **programatik olarak** ölçeklendirmek için yeniden kullanılabilir istekler kütüphanesi oluşturabiliriz.

Son olarak, şablonların gerçek değeri, istek şablonunun artık belirli uygulamaya özgü bağlam veya örnekleri yansıtacak şekilde _optimize edildiği_, yanıtları hedef kullanıcı kitlesi için daha alakalı ve doğru hale getiren _istek kütüphaneleri_ oluşturup yayınlama yeteneğindedir. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) deposu bu yaklaşıma harika bir örnek olup, ders planlama, müfredat tasarımı, öğrenci eğitimi gibi temel hedeflere odaklanan eğitim alanına yönelik istek koleksiyonunu düzenlemektedir.

## Destekleyici İçerik

İstemi bir talimat (görev) ve hedef (birincil içerik) olarak düşünürsek, _ikincil içerik_, çıktıyı **bir şekilde etkilemek için** sağladığımız ek bağlam gibidir. Bu, modelin yanıtını istenen kullanıcı hedeflerine veya beklentilerine uygun hale getirmesine yardımcı olabilecek ince ayar parametreleri, biçimlendirme talimatları, konu taksonomileri vb. olabilir.

Örneğin: Müfredattaki tüm mevcut kursların ayrıntılı meta verisi (isim, açıklama, seviye, meta etiketleri, eğitmen vb.) olan bir kurs kataloğu verildiğinde:

- "2023 Güz dönemi için kurs kataloğunu özetle" talimatı tanımlayabiliriz.
- Birincil içerik olarak istenen çıktıdan birkaç örnek sunabiliriz.
- İkincil içerik olarak ilgilenilen ilk 5 "etiketi" belirtebiliriz.

Şimdi, model birkaç örnekte gösterilen formatta bir özet sunabilir - ancak bir sonuçta birden fazla etiket varsa, ikincil içerikte tanımlanan 5 etiketi önceliklendirebilir.

---

<!--
DERS ŞABLONU:
Bu ünitede temel kavram #1 ele alınmalıdır.
Kavramı örnekler ve referanslarla pekiştirin.

KAVRAM #3:
İstek Mühendisliği Teknikleri.
İstek mühendisliği için bazı temel teknikler nelerdir?
Bunu bazı egzersizlerle gösterin.
-->

## İstek İyi Uygulamaları

Artık isteklerin nasıl _oluşturulacağını_ bildiğimize göre, onları en iyi uygulamaları yansıtacak şekilde nasıl _tasarlayabileceğimizi_ düşünmeye başlayabiliriz. Bunu iki bölümde düşünebiliriz - doğru _zihniyet_'e sahip olmak ve doğru _teknik_leri uygulamak.

### İstek Mühendisliği Zihniyeti

İstek mühendisliği deneme-yanılma sürecidir, bu yüzden üç geniş rehber faktörü aklınızda tutun:

1. **Alan Anlayışı Önemlidir.** Yanıt doğruluğu ve alaka, o uygulamanın veya kullanıcının faaliyet gösterdiği _alan_ın bir fonksiyonudur. Sezginizi ve alan uzmanlığınızı kullanarak **teknikleri daha da özelleştirin**. Örneğin, sistem isteklerinizde _alan-a özgü kişilikler_ tanımlayın veya kullanıcı isteklerinde _alan-a özgü şablonlar_ kullanın. Alan-a özgü bağlamları yansıtan ikincil içerik sağlayın veya modeli tanıdık kullanım desenlerine yönlendirmek için _alan-a özgü ipuçları ve örnekler_ kullanın.

2. **Model Anlayışı Önemlidir.** Modellerin doğası gereği stokastik olduğunu biliyoruz. Ancak model uygulamaları, kullandıkları eğitim veri setleri (önceden eğitilmiş bilgi), sağladıkları yetenekler (örneğin API veya SDK üzerinden) ve optimize edildikleri içerik türü (örn. kod, resim, metin) açısından değişiklik gösterebilir. Kullandığınız modelin güçlü ve zayıf yönlerini anlayın ve bu bilgiyi görevleri _önceliklendirmek_ veya modelin yeteneklerine uygun _özelleştirilmiş şablonlar_ oluşturmak için kullanın.

3. **İterasyon & Doğrulama Önemlidir.** Modeller hızla evriliyor, istek mühendisliği teknikleri de öyle. Alan uzmanı olarak, genel topluluk için geçerli olmayan kendi uygulamanıza özel başka bağlam veya kriterleriniz olabilir. İstek mühendisliği araçları ve tekniklerini kullanarak istek oluşturmayı "hızlandırın", sonra sezginiz ve alan uzmanlığınızla sonuçları yineleyin ve doğrulayın. Bulduğunuz dersleri kaydedin ve başkalarının daha hızlı iterasyonlar yapması için kullanılabilecek bir **bilgi tabanı** (örneğin istek kütüphaneleri) oluşturun.

## En İyi Uygulamalar

Şimdi, [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) ve [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) uygulayıcıları tarafından önerilen yaygın en iyi uygulamalara göz atalım.

| Ne Yapmalı                        | Neden                                                                                                                                                                                                                                         |
| :-------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| En yeni modelleri değerlendirin. | Yeni model nesilleri geliştirilmiş özellikler ve kaliteye sahip olabilir - ancak daha yüksek maliyetlere de yol açabilir. Etkisini değerlendirin, ardından geçiş kararları alın.                                                                |
| Talimatları ve bağlamı ayırın    | Modelinizin/sağlayıcınızın talimatları, birincil ve ikincil içerikleri daha net ayırt etmek için _sınırlayıcılar_ belirleyip belirlemediğini kontrol edin. Bu, modellere tokenlere ağırlık verme konusunda daha doğru yardımcı olabilir.          |
| Spesifik ve net olun             | İstenen bağlam, sonuç, uzunluk, format, stil vb. hakkında daha fazla detay verin. Bu, yanıtların kalitesini ve tutarlılığını artırır. Tarifleri yeniden kullanılabilir şablonlarda yakalayın.                                               |
| Betimleyici olun, örnek kullanın | Modeller "göster ve anlat" yaklaşımına daha iyi yanıt verebilir. Önce bir `sıfır-atış` yaklaşımıyla talimat verin (örnek olmadan) sonra istenen çıktının birkaç örneğini sağlayarak `birkaç atış` ile rafine edin. Benzetmeler kullanın.          |
| Tamamlama için ipuçları verin   | Yanıt için başlangıç noktası olarak kullanabileceği bazı öncül kelime veya ifadelere yönlendirerek istenen sonucu teşvik edin.                                                                                                                |
| Tekrar edin Küçük çapta          | Bazen modeli tekrar etmeniz gerekebilir. Birincil içeriğinizden önce ve sonra talimat verin, talimatla ipucunu birlikte kullanın vb. Ne işe yarıyor görmek için yineleyin ve doğrulayın.                                                      |
| Sıra Önemlidir                   | Bilgiyi modele verme sırası çıktı üzerinde etkili olabilir, örneğin öğrenme örneklerinde yakınlık yanlılığı nedeniyle. En iyi sonucu görmek için farklı seçenekleri deneyin.                                                                   |
| Modele "çıkış yolu" verin        | Modelin herhangi bir nedenle görevi tamamlayamazsa sağlayabileceği bir _yedek_ tamamlama yanıtı verin. Bu, modelin yanlış veya uydurma cevaplar üretme ihtimalini azaltabilir.                                                                |
|                                  |                                                                                                                                                                                                                                               |

Herhangi bir en iyi uygulamada olduğu gibi, _deneyiminiz modele, göreve ve alana bağlı olarak farklı olabilir_. Bunları bir başlangıç noktası olarak kullanın ve sizin için en iyisini bulmak için yineleyin. Yeni modeller ve araçlar çıktıkça, süreç ölçeklenebilirliği ve yanıt kalitesi odaklı olarak istek mühendisliği sürecinizi sürekli değerlendirin.

<!--
DERS ŞABLONU:
Bu ünitede, uygunsa bir kod meydan okuması verilmelidir.

MEYDAN OKUMA:
Ancakça açıklamalar kod talimatlarında olan, kod bölümleri boş olan bir Jupyter Notebook'a bağlantı verin.

ÇÖZÜM:
İsteklerin doldurulmuş ve çalıştırılmış halinin bulunduğu o Notebook'un bir kopyasına bağlantı verin, bir örnek çıktı nasıl olabileceğini gösterin.
-->

## Ödev

Tebrikler! Dersin sonuna geldiniz! Şimdi bazı kavramları ve teknikleri gerçek örneklerle test etme zamanı!

Ödevimiz için, etkileşimli tamamlayabileceğiniz bir Jupyter Notebook kullanacağız. Ayrıca kendi Markdown ve Kod hücrelerinizle Notebook'u genişleterek kendi başınıza fikirler ve teknikler keşfedebilirsiniz.

### Başlamak için, depo'yu çatallayın, sonra

- (Önerilen) GitHub Codespaces'i başlatın
- (Alternatif olarak) Depoyu yerel cihazınıza klonlayın ve Docker Desktop ile kullanın
- (Alternatif olarak) Tercih ettiğiniz Notebook çalışma zamanı ortamıyla Notebook'u açın.

### Sonra, ortam değişkenlerinizi yapılandırın

- Depo kökündeki `.env.copy` dosyasını `.env` olarak kopyalayın ve `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` ve `AZURE_OPENAI_DEPLOYMENT` değerlerini doldurun. Nasıl yapılacağını öğrenmek için [Learning Sandbox bölümüne](#öğrenme-oyun-alanı) geri dönün.

### Sonra, Jupyter Notebook'u açın

- Çalışma zamanı çekirdeğini seçin. Seçenek 1 veya 2'yi kullanıyorsanız, geliştirme konteyneri tarafından sağlanan varsayılan Python 3.10.x çekirdeğini seçmeniz yeterli.

Artık alıştırmaları çalıştırmaya hazırsınız. Burada _doğru veya yanlış_ cevaplar olmadığını unutmayın - sadece deneme-yanılma yoluyla seçenekleri keşfetmek ve belirli bir model ve uygulama alanı için neyin işe yaradığını sezgisel olarak öğrenmek için.

_Bu nedenle bu derste Kod Çözümü parçaları yoktur. Bunun yerine, Notebook'ta "Benim Çözümüm:" başlıklı Markdown hücreleri olacak ve bunlar referans için bir örnek çıktı gösterecek._

 <!--
DERS ŞABLONU:
Bölümü bir özet ve kendi kendine öğrenme kaynakları ile sarın.
-->

## Bilgi Kontrolü

Aşağıdakilerden hangisi makul en iyi uygulamaları takip eden iyi bir istemdir?

1. Bana kırmızı araba resmi göster
2. Bana bir uçurum kenarında park etmiş, güneşin battığı bir ortamda Volvo marka ve XC90 modelinde kırmızı araba resmi göster
3. Bana Volvo marka ve XC90 modelinde kırmızı araba resmi göster

C: 2, en iyi istek çünkü "ne" olduğunu detaylandırıyor ve spesifiklere kadar iniyor (herhangi bir araba değil, belirli marka ve model) ve ayrıca genel ortamı tarif ediyor. 3 ise çokça betimleme içerdiği için ikinci en iyi.

## 🚀 Meydan Okuma

İstemle "tamamla" tekniğini kullanmayı deneyin: "Bana Volvo marka ve ..." cümlesini tamamlayın. Ne yanıt veriyor ve nasıl geliştirirdiniz?

## Harika İş! Öğrenmeye Devam Et

Farklı İstek Mühendisliği kavramlarını öğrenmek ister misiniz? Bu konudaki diğer harika kaynakları bulmak için [devam eden öğrenme sayfasına](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) gidin.

İleri istek tekniklerine bakacağımız 5. Derse geçebilirsiniz: [ileri istek teknikleri](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->