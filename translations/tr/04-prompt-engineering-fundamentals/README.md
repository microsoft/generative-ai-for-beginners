<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-06-25T12:39:25+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "tr"
}
-->
# İstem Mühendisliği Temelleri

## Giriş
Bu modül, üretken yapay zeka modellerinde etkili istemler oluşturmak için gerekli kavramlar ve teknikleri ele alır. LLM'ye yazdığınız istemin biçimi de önemlidir. Özenle hazırlanmış bir istem, daha kaliteli bir yanıt elde etmenizi sağlayabilir. Ancak _istem_ ve _istem mühendisliği_ gibi terimler tam olarak ne anlama gelir? Ve LLM'ye gönderdiğim istem _girdisini_ nasıl geliştirebilirim? Bu bölümde ve bir sonrakinde bu soruları yanıtlamaya çalışacağız.

_Üretken Yapay Zeka_, kullanıcı taleplerine yanıt olarak yeni içerik (örneğin, metin, görüntü, ses, kod vb.) oluşturma kapasitesine sahiptir. Bunu, doğal dil ve kod kullanımı için eğitilmiş olan OpenAI'nin GPT ("Generative Pre-trained Transformer") serisi gibi _Büyük Dil Modelleri_ kullanarak başarır.

Kullanıcılar artık bu modellerle sohbet gibi tanıdık paradigmalar kullanarak etkileşimde bulunabilir, teknik uzmanlık veya eğitim gerektirmez. Modeller _istem tabanlıdır_ - kullanıcılar bir metin girişi (istem) gönderir ve AI yanıtını (tamamlama) geri alır. Ardından, yanıt beklentilerini karşılayana kadar istemlerini rafine ederek "AI ile sohbet edebilirler."

"İstemler" artık üretken yapay zeka uygulamaları için birincil _programlama arayüzü_ haline gelir, modellere ne yapmaları gerektiğini söyler ve geri dönen yanıtların kalitesini etkiler. "İstem Mühendisliği", tutarlı ve kaliteli yanıtlar sunmak için istemlerin _tasarımı ve optimizasyonu_ üzerine odaklanan hızla büyüyen bir çalışma alanıdır.

## Öğrenme Hedefleri

Bu derste, İstem Mühendisliğinin ne olduğunu, neden önemli olduğunu ve belirli bir model ve uygulama amacı için daha etkili istemleri nasıl oluşturabileceğimizi öğreniyoruz. İstem mühendisliğinin temel kavramlarını ve en iyi uygulamalarını anlayacağız - ve bu kavramların gerçek örneklere uygulandığını görebileceğimiz etkileşimli bir Jupyter Notebooks "kum havuzu" ortamı hakkında bilgi edineceğiz.

Bu dersin sonunda şunları yapabileceğiz:

1. İstem mühendisliğinin ne olduğunu ve neden önemli olduğunu açıklayın.
2. Bir istemin bileşenlerini ve nasıl kullanıldıklarını tanımlayın.
3. İstem mühendisliği için en iyi uygulamaları ve teknikleri öğrenin.
4. Öğrenilen teknikleri, bir OpenAI uç noktası kullanarak gerçek örneklere uygulayın.

## Anahtar Terimler

İstem Mühendisliği: AI modellerini istenen çıktılar üretmeye yönlendirmek için girdileri tasarlama ve rafine etme pratiği.
Tokenizasyon: Metni, modelin anlayabileceği ve işleyebileceği daha küçük birimlere, yani tokenlere dönüştürme süreci.
Talimatla Ayarlanmış LLM'ler: Yanıt doğruluğunu ve alaka düzeyini artırmak için belirli talimatlarla ince ayarlanmış Büyük Dil Modelleri (LLM'ler).

## Öğrenme Kum Havuzu

İstem mühendisliği şu anda bilimden çok sanat gibidir. Bu konuda sezgimizi geliştirmek için en iyi yol, _daha fazla pratik yapmak_ ve uygulama alanı uzmanlığını önerilen tekniklerle ve modele özgü optimizasyonlarla birleştiren bir deneme-yanılma yaklaşımını benimsemektir.

Bu derse eşlik eden Jupyter Notebook, öğrendiklerinizi deneyebileceğiniz bir _kum havuzu_ ortamı sağlar - ister ders sırasında ister kod mücadelesinin bir parçası olarak. Egzersizleri gerçekleştirmek için şunlara ihtiyacınız olacak:

1. **Bir Azure OpenAI API anahtarı** - dağıtılmış bir LLM için hizmet uç noktası.
2. **Bir Python Çalışma Zamanı** - Notebook'un çalıştırılabileceği bir ortam.
3. **Yerel Çevre Değişkenleri** - _hazırlanmak için şimdi [KURULUM](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) adımlarını tamamlayın_.

Notebook, _başlangıç_ egzersizleri ile birlikte gelir - ancak daha fazla örnek veya fikir denemek ve istem tasarımı için sezginizi geliştirmek için kendi _Markdown_ (açıklama) ve _Kod_ (istem talepleri) bölümlerinizi eklemeniz teşvik edilir.

## Resimli Rehber

Bu derste ele alınan konuların genel bir resmini görmek ister misiniz? Her birinde düşünmeniz gereken ana konuları ve önemli çıkarımları size bir fikir veren bu resimli rehberi inceleyin. Ders yol haritası, temel kavramları ve zorlukları anlamaktan, ilgili istem mühendisliği teknikleri ve en iyi uygulamalarla ele almaya kadar sizi yönlendirir. Bu rehberdeki "Gelişmiş Teknikler" bölümü, bu müfredatın _bir sonraki_ bölümünde ele alınan içeriğe atıfta bulunur.

## Girişimimiz

Şimdi, _bu konunun_ [eğitime yapay zeka yeniliği getirme](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst) misyonumuzla nasıl ilişkili olduğunu konuşalım. Kişiselleştirilmiş öğrenmenin yapay zeka destekli uygulamalarını geliştirmek istiyoruz - bu yüzden uygulamamızın farklı kullanıcılarının istemleri nasıl "tasarlayabileceğini" düşünelim:

- **Yöneticiler**, AI'dan _müfredat verilerini analiz ederek kapsama alanındaki boşlukları belirlemesini_ isteyebilir. AI, sonuçları özetleyebilir veya kodla görselleştirebilir.
- **Eğitimciler**, AI'dan _hedef kitle ve konu için bir ders planı oluşturmasını_ isteyebilir. AI, belirli bir formatta kişiselleştirilmiş planı oluşturabilir.
- **Öğrenciler**, AI'dan _zor bir konuda onlara öğretmenlik yapmasını_ isteyebilir. AI, şimdi öğrencilere seviyelerine göre uyarlanmış dersler, ipuçları ve örneklerle rehberlik edebilir.

Bu sadece buzdağının görünen kısmı. [Eğitim için İstemler](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - eğitim uzmanları tarafından küratörlüğü yapılmış açık kaynak istemler kütüphanesini inceleyin - olanakların daha geniş bir anlamını elde etmek için! _Bu istemlerden bazılarını kum havuzunda çalıştırmayı veya OpenAI Playground'da ne olduğunu görmek için deneyin!_

## İstem Mühendisliği Nedir?

Bu derse, **İstem Mühendisliğini** belirli bir uygulama amacı ve model için tutarlı ve kaliteli yanıtlar (tamamlamalar) sağlamak üzere metin girdilerini (istemleri) _tasarlama ve optimize etme_ süreci olarak tanımlayarak başladık. Bunu 2 aşamalı bir süreç olarak düşünebiliriz:

- Belirli bir model ve amaç için ilk istemi _tasarlama_
- Yanıtın kalitesini artırmak için istemi _iteratif olarak iyileştirme_

Bu, optimal sonuçlar elde etmek için kullanıcı sezgisi ve çabasını gerektiren bir deneme-yanılma sürecidir. Peki neden önemlidir? Bu soruyu yanıtlamak için önce üç kavramı anlamamız gerekiyor:

- _Tokenizasyon_ = modelin istemi nasıl "gördüğü"
- _Temel LLM'ler_ = temel modelin bir istemi nasıl "işlediği"
- _Talimatla Ayarlanmış LLM'ler_ = modelin artık "görevleri" nasıl görebileceği

### Tokenizasyon

Bir LLM, istemleri _token dizisi_ olarak görür, burada farklı modeller (veya model versiyonları) aynı istemi farklı şekillerde tokenize edebilir. LLM'ler tokenlar üzerinde (ham metin üzerinde değil) eğitildiği için, istemlerin nasıl tokenleştirildiği, üretilen yanıtın kalitesi üzerinde doğrudan bir etkiye sahiptir.

Tokenizasyonun nasıl çalıştığına dair bir sezgi kazanmak için, aşağıda gösterilen [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) gibi araçları deneyin. İsteminizi kopyalayın - ve bunun tokenlara nasıl dönüştüğünü görün, boşluk karakterlerinin ve noktalama işaretlerinin nasıl ele alındığına dikkat edin. Bu örneğin daha eski bir LLM (GPT-3) gösterdiğini unutmayın - bu yüzden daha yeni bir modelle denemek farklı bir sonuç üretebilir.

### Kavram: Temel Modeller

Bir istem tokenize edildikten sonra, ["Temel LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (veya Temel model) ana işlevi, o dizideki tokeni tahmin etmektir. LLM'ler büyük metin veri kümeleri üzerinde eğitildiğinden, tokenlar arasındaki istatistiksel ilişkiler hakkında iyi bir sezgiye sahiptirler ve bu tahmini bir güvenle yapabilirler. İstemdeki veya token'daki kelimelerin _anlamını_ anlamazlar; sadece bir sonraki tahminleriyle "tamamlayabilecekleri" bir desen görürler. Kullanıcı müdahalesi veya önceden belirlenmiş bir koşulla sonlandırılana kadar diziyi tahmin etmeye devam edebilirler.

İstem tabanlı tamamlamanın nasıl çalıştığını görmek ister misiniz? Yukarıdaki istemi varsayılan ayarlarla Azure OpenAI Studio [_Sohbet Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) içine girin. Sistem, istemleri bilgi talepleri olarak ele alacak şekilde yapılandırılmıştır - bu nedenle bu bağlamı tatmin eden bir tamamlamayı görmelisiniz.

Ancak kullanıcı belirli kriterlere veya görev amacına uygun bir şey görmek istiyorsa ne olur? İşte burada _talimatla ayarlanmış_ LLM'ler devreye girer.

### Kavram: Talimatla Ayarlanmış LLM'ler

[Instruction Tuned LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst), temel modelle başlar ve örnekler veya girdi/çıktı çiftleri (örneğin, çok dönüşlü "mesajlar") ile ince ayarlanır ve bunlar net talimatlar içerebilir - ve AI'nın yanıtı bu talimatı izlemeye çalışır.

Bu, modelin _talimatları takip etmesini_ ve _geri bildirimden öğrenmesini_ sağlayarak yanıtların pratik uygulamalara daha uygun ve kullanıcı hedeflerine daha alakalı olmasını sağlamak için, İnsan Geri Bildirimi ile Takviyeli Öğrenme (RLHF) gibi teknikler kullanır.

Deneyelim - yukarıdaki istemi yeniden ziyaret edin, ancak şimdi _sistem mesajını_ şu talimatı bağlam olarak sağlamak için değiştirin:

> _İkinci sınıf öğrencisi için sağlanan içeriği özetleyin. Sonucu 3-5 maddeyle bir paragraf olarak tutun._

Sonucun şimdi istenen hedefi ve formatı nasıl yansıttığını görün? Bir eğitimci, şimdi bu yanıtı doğrudan o sınıf için slaytlarına ekleyebilir.

## Neden İstem Mühendisliğine İhtiyacımız Var?

Artık istemlerin LLM'ler tarafından nasıl işlendiğini bildiğimize göre, _neden_ istem mühendisliğine ihtiyacımız olduğunu konuşalım. Cevap, mevcut LLM'lerin, istem yapımı ve optimizasyonu için çaba harcamadan _güvenilir ve tutarlı tamamlamalar_ elde etmeyi daha zorlaştıran bir dizi zorluk sunduğu gerçeğinde yatmaktadır. Örneğin:

1. **Model yanıtları stokastiktir.** _Aynı istem_, muhtemelen farklı modeller veya model versiyonları ile farklı yanıtlar üretecektir. Ve hatta _aynı model_ ile farklı zamanlarda farklı sonuçlar üretebilir. _İstem mühendisliği teknikleri, daha iyi koruma sağlamak için bu varyasyonları en aza indirmemize yardımcı olabilir_.

2. **Modeller yanıtlar üretebilir.** Modeller, _büyük ama sınırlı_ veri kümeleriyle önceden eğitildiğinden, eğitim kapsamı dışındaki kavramlar hakkında bilgiye sahip değildirler. Sonuç olarak, yanlış, hayali veya bilinen gerçeklerle doğrudan çelişen tamamlamalar üretebilirler. _İstem mühendisliği teknikleri, kullanıcıların bu tür hayalleri tanımlamalarına ve azaltmalarına yardımcı olabilir, örneğin AI'dan alıntılar veya akıl yürütme istemek gibi_.

3. **Model yetenekleri değişkenlik gösterecektir.** Daha yeni modeller veya model nesilleri daha zengin yeteneklere sahip olacak, ancak aynı zamanda maliyet ve karmaşıklıkta benzersiz tuhaflıklar ve ödünler getirecektir. _İstem mühendisliği, model spesifik gereksinimlere ölçeklenebilir, sorunsuz bir şekilde uyum sağlayarak farklılıkları soyutlayan en iyi uygulamaları ve iş akışlarını geliştirmemize yardımcı olabilir_.

Bunu OpenAI veya Azure OpenAI Playground'da eylem halinde görelim:

- Aynı istemi farklı LLM dağıtımlarıyla (örneğin, OpenAI, Azure OpenAI, Hugging Face) kullanın - varyasyonları gördünüz mü?
- Aynı istemi _aynı_ LLM dağıtımıyla (örneğin, Azure OpenAI playground) tekrarlayın - bu varyasyonlar nasıl farklılaştı?

### Hayaller Örneği

Bu kursta, LLM'lerin bazen eğitim sınırlamaları veya diğer kısıtlamalar nedeniyle gerçek olmayan bilgiler ürettiği fenomeni referans almak için **"hayal"** terimini kullanıyoruz. Bunu popüler makalelerde veya araştırma makalelerinde _"halüsinasyonlar"_ olarak da duymuş olabilirsiniz. Ancak, makine güdümlü bir sonuca insan benzeri bir özelliği atfederek davranışı antropomorfize etmemek için _"hayal"_ terimini kullanmanızı şiddetle öneriyoruz. Bu, terminoloji açısından [Sorumlu AI yönergelerini](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) de güçlendirir, bazı bağlamlarda saldırgan veya kapsayıcı olmayan kabul edilebilecek terimleri kaldırır.

Hayallerin nasıl çalıştığını anlamak ister misiniz? Eğitim veri kümesinde bulunmayan bir konu için AI'dan içerik oluşturmasını isteyen bir istem düşünün (bulunmadığından emin olmak için). Örneğin - bu istemi denedim:

> **İstem:** 2076 Mars Savaşı hakkında bir ders planı oluşturun.

Bir web araması, Mars savaşları hakkında kurgusal hesaplar olduğunu gösterdi (örneğin, televizyon dizileri veya kitaplar) - ancak 2076'da değil. Sağduyu ayrıca bize 2076'nın _gelecekte_ olduğunu ve dolayısıyla gerçek bir olayla ilişkilendirilemeyeceğini söyler.

Peki bu istemi farklı LLM sağlayıcılarıyla çalıştırdığımızda ne olur?

Beklendiği gibi, her model (veya model versiyonu), stokastik davranış ve model yetenek varyasyonları sayesinde biraz farklı yanıtlar üretti. Örneğin, bir model 8. sınıf izleyici kitlesini hedef alırken, diğeri bir lise öğrencisini varsaydı. Ancak üç model de uninforme bir kullanıcıyı olayın gerçek olduğuna ikna edebilecek yanıtlar üretti

_Metaprompting_ ve _sıcaklık yapılandırması_ gibi istem mühendisliği teknikleri, model hayallerini bir dereceye kadar azaltabilir. Yeni istem mühendisliği _mimarileri_ ayrıca bu etkileri hafifletmek veya azaltmak için yeni araçları ve teknikleri istem akışına sorunsuz bir şekilde entegre eder.

## Vaka Çalışması: GitHub Copilot

Bu bölümü, gerçek dünya çözümlerinde istem mühendisliğinin nasıl kullanıldığını anlamak için bir Vaka Çalışması: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst) ile kapatalım.

GitHub Copilot, "AI Çift Programcınız"dır - metin istemlerini kod tamamlama dönüştürür ve geliştirme ortamınıza (örneğin, Visual Studio Code) entegre edilmiştir, böylece kesintisiz bir kullanıcı deneyimi sunar. Aşağıdaki blog dizisinde belgelenen ilk sürüm, OpenAI Codex modeline dayanıyordu - mühendisler, kod kalitesini artırmak için modeli ince ayarlama ve daha iyi istem mühendisliği teknikleri geliştirme ihtiyacını hızla fark etti. Temmuz ayında, [Codex'in ötesine geçen ve geliştirilmiş bir AI modeliyle daha hızlı öneriler sunan](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) bir modeli tanıttılar.

Öğrenme yolculuklarını takip etmek için gönderileri sırayla okuyun.

- **Mayıs 2023** | [GitHub Copilot Kodunuzu Anlamada Daha İyi Hale Geliyor](https://github.blog
Sonuç olarak, şablonların gerçek değeri, dikey uygulama alanları için _istek kütüphaneleri_ oluşturma ve yayınlama yeteneğinde yatar - burada istek şablonu, uygulamaya özgü bağlamı veya yanıtları hedef kullanıcı kitlesi için daha alakalı ve doğru hale getiren örnekleri yansıtacak şekilde _optimize edilmiştir_. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) deposu, bu yaklaşımın harika bir örneğidir; ders planlaması, müfredat tasarımı, öğrenci eğitimi gibi ana hedeflere vurgu yaparak eğitim alanı için bir istek kütüphanesi derler.

## Destekleyici İçerik

İstek oluşturmayı bir talimat (görev) ve bir hedef (ana içerik) olarak düşünürsek, _ikincil içerik_ **çıkışı bir şekilde etkilemek için** sağladığımız ek bağlam gibidir. Modelin yanıtını istenen kullanıcı hedeflerine veya beklentilerine uygun hale getirmesine yardımcı olabilecek ayar parametreleri, biçimlendirme talimatları, konu sınıflandırmaları vb. olabilir.

Örneğin: Müfredatta yer alan tüm dersler hakkında kapsamlı meta veriler (isim, açıklama, seviye, meta veri etiketleri, eğitmen vb.) içeren bir ders kataloğu verildiğinde:

- "2023 Sonbahar ders kataloğunu özetle" talimatını tanımlayabiliriz
- İstenilen çıkışın birkaç örneğini sağlamak için ana içeriği kullanabiliriz
- İlgi çeken ilk 5 "etiketi" belirlemek için ikincil içeriği kullanabiliriz.

Artık model, birkaç örnekle gösterilen formatta bir özet sağlayabilir - ancak bir sonuç birden fazla etiket içeriyorsa, ikincil içerikte belirlenen 5 etiketi önceliklendirebilir.

---

## İstek En İyi Uygulamaları

Artık isteklerin nasıl _oluşturulabileceğini_ bildiğimize göre, en iyi uygulamaları yansıtacak şekilde nasıl _tasarlanabileceğini_ düşünmeye başlayabiliriz. Bunu iki bölümde düşünebiliriz - doğru _zihniyete_ sahip olmak ve doğru _teknikleri_ uygulamak.

### İstek Mühendisliği Zihniyeti

İstek Mühendisliği bir deneme-yanılma sürecidir, bu yüzden üç geniş yönlendirici faktörü akılda tutun:

1. **Alan Anlayışı Önemlidir.** Yanıtın doğruluğu ve alaka düzeyi, uygulamanın veya kullanıcının çalıştığı _alanın_ bir fonksiyonudur. Teknikleri daha da **özelleştirmek** için sezginizi ve alan uzmanlığınızı uygulayın. Örneğin, sistem isteklerinizde _alana özgü kişilikler_ tanımlayın veya kullanıcı isteklerinizde _alana özgü şablonlar_ kullanın. Alan özel bağlamları yansıtan ikincil içerik sağlayın veya modeli tanıdık kullanım kalıplarına yönlendirmek için _alana özgü ipuçları ve örnekler_ kullanın.

2. **Model Anlayışı Önemlidir.** Modellerin doğası gereği stokastik olduğunu biliyoruz. Ancak model uygulamaları, kullandıkları eğitim veri seti (önceden eğitilmiş bilgi), sağladıkları yetenekler (örneğin, API veya SDK aracılığıyla) ve optimize edildikleri içerik türü (örneğin, kod vs. görüntüler vs. metin) açısından da farklılık gösterebilir. Kullandığınız modelin güçlü ve zayıf yönlerini anlayın ve bu bilgiyi _görevleri önceliklendirmek_ veya modelin yeteneklerine optimize edilmiş _özelleştirilmiş şablonlar_ oluşturmak için kullanın.

3. **Yineleme ve Doğrulama Önemlidir.** Modeller hızla gelişiyor ve istek mühendisliği teknikleri de öyle. Bir alan uzmanı olarak, daha geniş topluluğa uymayan _özel_ uygulamanız için başka bağlam veya kriterlere sahip olabilirsiniz. İstek mühendisliği araçlarını ve tekniklerini "istek oluşturmayı başlatmak" için kullanın, ardından kendi sezginizi ve alan uzmanlığınızı kullanarak sonuçları yineleyin ve doğrulayın. İçgörülerinizi kaydedin ve diğerleri tarafından gelecekte daha hızlı yinelemeler için yeni bir temel olarak kullanılabilecek bir **bilgi tabanı** (örneğin, istek kütüphaneleri) oluşturun.

## En İyi Uygulamalar

Şimdi [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) ve [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) uygulayıcıları tarafından önerilen ortak en iyi uygulamalara bakalım.

| Ne                                | Neden                                                                                                                                                                                                                                             |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| En yeni modelleri değerlendirin.  | Yeni model nesilleri muhtemelen geliştirilmiş özelliklere ve kaliteye sahip olacaktır - ancak daha yüksek maliyetler de getirebilir. Etkilerini değerlendirin, ardından geçiş kararları alın.                                                      |
| Talimatları ve bağlamı ayırın     | Modelinizin/sağlayıcınızın talimatları, birincil ve ikincil içeriği daha net bir şekilde ayırt etmek için _sınırlandırıcılar_ tanımlayıp tanımlamadığını kontrol edin. Bu, modellerin kelimelere daha doğru ağırlık vermesine yardımcı olabilir.       |
| Spesifik ve net olun              | İstenilen bağlam, sonuç, uzunluk, format, stil vb. hakkında daha fazla ayrıntı verin. Bu, yanıtların hem kalitesini hem de tutarlılığını artıracaktır. Yeniden kullanılabilir şablonlarda tarifleri yakalayın.                                      |
| Açıklayıcı olun, örnekler kullanın| Modeller "göster ve anlat" yaklaşımına daha iyi yanıt verebilir. `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember that _your mileage may vary_ based on the model, the task and the domain. Use these as a starting point, and iterate to find what works best for you. Constantly re-evaluate your prompt engineering process as new models and tools become available, with a focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Congratulations! You made it to the end of the lesson! It's time to put some of those concepts and techniques to the test with real examples!

For our assignment, we'll be using a Jupyter Notebook with exercises you can complete interactively. You can also extend the Notebook with your own Markdown and Code cells to explore ideas and techniques on your own.

### To get started, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use it with Docker Desktop
- (Alternatively) Open the Notebook with your preferred Notebook runtime environment.

### Next, configure your environment variables

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` değerleriyle başlayın. [Learning Sandbox bölümüne](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) geri dönerek nasıl yapıldığını öğrenin.

### Şimdi, Jupyter Notebook'u açın

- Çalışma zamanı çekirdeğini seçin. 1 veya 2 seçeneklerini kullanıyorsanız, yalnızca geliştirme konteyneri tarafından sağlanan varsayılan Python 3.10.x çekirdeğini seçin.

Alıştırmaları çalıştırmaya hazırsınız. Burada _doğru ve yanlış_ cevaplar olmadığını unutmayın - sadece deneme-yanılma yoluyla seçenekleri keşfetmek ve belirli bir model ve uygulama alanı için neyin işe yaradığını anlamak.

_Bu nedenle, bu derste Kod Çözüm segmentleri yoktur. Bunun yerine, Notebook, referans için bir örnek çıktıyı gösteren "Çözümüm:" başlıklı Markdown hücrelerine sahip olacaktır._

## Bilgi kontrolü

Aşağıdakilerden hangisi makul en iyi uygulamaları takip eden iyi bir istektir?

1. Bana kırmızı bir araba resmi göster
2. Bana Volvo marka ve XC90 model, güneş batarken bir uçurumun kenarında park etmiş kırmızı bir araba resmi göster
3. Bana Volvo marka ve XC90 model kırmızı bir araba resmi göster

A: 2, en iyi istektir çünkü "ne" hakkında detaylar sağlar ve ayrıntılara girer (sadece herhangi bir araba değil, belirli bir marka ve model) ve ayrıca genel ortamı tanımlar. 3, sonraki en iyisidir çünkü o da çok fazla açıklama içerir.

## 🚀 Meydan Okuma

İsteği tamamlayarak "Volvo marka kırmızı bir araba resmi göster" cümlesi ile "ipucu" tekniğinden yararlanıp yararlanamayacağınıza bakın. Ne yanıt verir ve bunu nasıl geliştirirsiniz?

## Harika İş! Öğrenmeye Devam Edin

Farklı İstek Mühendisliği kavramları hakkında daha fazla bilgi edinmek ister misiniz? Bu konuyla ilgili diğer harika kaynakları bulmak için [devam eden öğrenme sayfasına](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) gidin.

5. Derse geçin, burada [ileri seviye istek tekniklerine](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst) bakacağız!

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki versiyonu yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlama veya yanlış yorumlamalardan sorumlu değiliz.