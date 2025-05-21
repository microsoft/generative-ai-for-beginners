<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-05-19T15:31:25+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "tr"
}
-->
# Prompt Mühendisliği Temelleri

## Giriş
Bu modül, üretici yapay zeka modellerinde etkili yönlendirmeler oluşturmak için temel kavramlar ve teknikleri kapsar. Bir LLM'ye (Büyük Dil Modeli) yazdığınız yönlendirme şekli de önemlidir. Özenle hazırlanmış bir yönlendirme, daha kaliteli bir yanıt elde edebilir. Ancak _yönlendirme_ ve _yönlendirme mühendisliği_ gibi terimler tam olarak ne anlama gelir? Ve LLM'ye gönderdiğim yönlendirme _girişini_ nasıl geliştirebilirim? Bu bölümde ve bir sonraki bölümde bu soruları yanıtlamaya çalışacağız.

_Üretici Yapay Zeka_, kullanıcı taleplerine yanıt olarak yeni içerik (ör. metin, resimler, ses, kod vb.) oluşturabilir. Bunu, doğal dil ve kod kullanımı için eğitilmiş OpenAI'nin GPT ("Üretici Ön Eğitimli Dönüştürücü") serisi gibi _Büyük Dil Modelleri_ kullanarak başarır.

Kullanıcılar artık bu modellerle sohbet gibi tanıdık paradigmalar kullanarak etkileşimde bulunabilirler, teknik uzmanlık veya eğitim gerektirmeden. Modeller _yönlendirme tabanlıdır_ - kullanıcılar bir metin girişi (yönlendirme) gönderir ve AI yanıtını (tamamlama) geri alır. Ardından, beklentilerini karşılayana kadar yönlendirmelerini geliştirerek, çok dönüşlü sohbetlerde AI ile "sohbet edebilirler".

"Yönlendirmeler" artık üretici yapay zeka uygulamaları için birincil _programlama arayüzü_ haline gelerek, modellere ne yapmaları gerektiğini söyleyip dönen yanıtların kalitesini etkiler. "Yönlendirme Mühendisliği", tutarlı ve kaliteli yanıtları ölçekli olarak sunmak için yönlendirmelerin _tasarımı ve optimizasyonu_ üzerine odaklanan hızla büyüyen bir çalışma alanıdır.

## Öğrenme Hedefleri

Bu derste, Yönlendirme Mühendisliğinin ne olduğunu, neden önemli olduğunu ve belirli bir model ve uygulama hedefi için daha etkili yönlendirmeler nasıl oluşturabileceğimizi öğreniyoruz. Yönlendirme mühendisliğinin temel kavramlarını ve en iyi uygulamalarını anlayacağız - ve bu kavramların gerçek örneklere uygulandığını görebileceğimiz etkileşimli bir Jupyter Notebooks "sandbox" ortamı hakkında bilgi edineceğiz.

Bu dersin sonunda şunları yapabileceğiz:

1. Yönlendirme mühendisliğinin ne olduğunu ve neden önemli olduğunu açıklayın.
2. Bir yönlendirmenin bileşenlerini ve nasıl kullanıldıklarını tanımlayın.
3. Yönlendirme mühendisliği için en iyi uygulamaları ve teknikleri öğrenin.
4. Öğrenilen teknikleri, bir OpenAI uç noktası kullanarak gerçek örneklere uygulayın.

## Anahtar Terimler

Yönlendirme Mühendisliği: AI modellerini istenen çıktıları üretmeye yönlendirmek için girdileri tasarlama ve iyileştirme pratiği.
Tokenizasyon: Metni, bir modelin anlayabileceği ve işleyebileceği daha küçük birimlere, yani tokenlara dönüştürme süreci.
Talimat Ayarlı LLM'ler: Yanıt doğruluğunu ve alaka düzeyini artırmak için belirli talimatlarla ince ayar yapılmış Büyük Dil Modelleri (LLM'ler).

## Öğrenme Alanı

Yönlendirme mühendisliği şu anda bilimden çok sanattır. Bu konuda sezgimizi geliştirmek için en iyi yol, _daha fazla pratik yapmak_ ve uygulama alanı uzmanlığını önerilen teknikler ve model özel optimizasyonlarla birleştiren bir deneme-yanılma yaklaşımını benimsemektir.

Bu derse eşlik eden Jupyter Notebook, öğrendiklerinizi denemeniz için bir _sandbox_ ortamı sağlar - derse katılırken veya sonunda kod meydan okumasının bir parçası olarak. Alıştırmaları gerçekleştirmek için şunlara ihtiyacınız olacak:

1. **Bir Azure OpenAI API anahtarı** - dağıtılmış bir LLM için hizmet uç noktası.
2. **Bir Python Çalışma Zamanı** - Not Defteri'nin çalıştırılabileceği.
3. **Yerel Çevre Değişkenleri** - _hazırlık için [AYARLAMA](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) adımlarını şimdi tamamlayın_.

Not defteri, _başlangıç_ alıştırmaları ile birlikte gelir - ancak kendi _Markdown_ (açıklama) ve _Kod_ (yönlendirme talepleri) bölümlerini eklemeye teşvik edilirsiniz - daha fazla örnek veya fikir denemek ve yönlendirme tasarımı için sezginizi geliştirmek için.

## Resimli Rehber

Bu derste ele alınan konuları derinlemesine incelemeden önce büyük resmi görmek ister misiniz? Bu resimli rehber, kapsanan ana konuların ve her birinde düşünmeniz gereken önemli çıkarımların bir özetini sunar. Ders yol haritası, temel kavramları ve zorlukları anlamaktan, bunları ilgili yönlendirme mühendisliği teknikleri ve en iyi uygulamalarla ele almaya kadar sizi götürür. Bu rehberdeki "Gelişmiş Teknikler" bölümü, bu müfredatın _bir sonraki_ bölümünde ele alınan içeriğe atıfta bulunmaktadır.

## Startup'ımız

Şimdi, _bu konunun_ [eğitime yapay zeka yenilikleri getirme](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst) misyonumuza nasıl bağlandığını konuşalım. Kişiselleştirilmiş öğrenme için yapay zeka destekli uygulamalar oluşturmak istiyoruz - bu yüzden uygulamamızın farklı kullanıcılarının nasıl "yönlendirme" tasarlayabileceğini düşünelim:

- **Yöneticiler**, AI'dan _müfredat verilerini analiz ederek kapsama alanındaki boşlukları belirlemesini_ isteyebilir. AI, sonuçları özetleyebilir veya bunları kodla görselleştirebilir.
- **Eğitmenler**, AI'dan _hedef kitle ve konu için bir ders planı oluşturmasını_ isteyebilir. AI, belirtilen formatta kişiselleştirilmiş planı oluşturabilir.
- **Öğrenciler**, AI'dan _zor bir konuda rehberlik etmelerini_ isteyebilir. AI, artık öğrencilere seviyelerine uygun dersler, ipuçları ve örneklerle rehberlik edebilir.

Bu sadece buzdağının görünen kısmı. [Eğitim İçin Yönlendirmeler](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - eğitim uzmanları tarafından derlenen açık kaynaklı bir yönlendirme kütüphanesini inceleyin - olanaklar hakkında daha geniş bir fikir edinmek için! _Bu yönlendirmelerden bazılarını sandbox ortamında çalıştırmayı veya OpenAI Playground'u kullanarak neler olduğunu görmeyi deneyin!_

## Yönlendirme Mühendisliği Nedir?

Bu derse **Yönlendirme Mühendisliğini** belirli bir uygulama hedefi ve model için tutarlı ve kaliteli yanıtlar (tamamlamalar) sunmak amacıyla metin girişlerini (yönlendirmeler) _tasarlama ve optimize etme_ süreci olarak tanımlayarak başladık. Bunu 2 adımlı bir süreç olarak düşünebiliriz:

- Belirli bir model ve hedef için başlangıç yönlendirmesini _tasarlamak_
- Yanıtın kalitesini artırmak için yönlendirmeyi _iteratif olarak iyileştirmek_

Bu, en iyi sonuçları elde etmek için kullanıcı sezgisi ve çabası gerektiren bir deneme-yanılma sürecidir. Peki neden önemlidir? Bu soruyu yanıtlamak için önce üç kavramı anlamamız gerekiyor:

- _Tokenizasyon_ = modelin yönlendirmeyi nasıl "gördüğü"
- _Temel LLM'ler_ = temel modelin bir yönlendirmeyi nasıl "işlediği"
- _Talimat Ayarlı LLM'ler_ = modelin artık "görevleri" nasıl görebildiği

### Tokenizasyon

Bir LLM, yönlendirmeleri _token dizisi_ olarak görür, burada farklı modeller (veya bir modelin farklı sürümleri) aynı yönlendirmeyi farklı şekillerde tokenleştirebilir. LLM'ler tokenlar üzerinde eğitildiği için (ham metin üzerinde değil), yönlendirmelerin nasıl tokenleştirildiği, üretilen yanıtın kalitesi üzerinde doğrudan etkiye sahiptir.

Tokenizasyonun nasıl çalıştığına dair bir sezgi edinmek için aşağıda gösterilen [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) gibi araçları deneyin. Yönlendirmenizi kopyalayın - ve bunun tokenlara nasıl dönüştüğünü görün, boşluk karakterleri ve noktalama işaretlerinin nasıl ele alındığına dikkat edin. Bu örneğin eski bir LLM'yi (GPT-3) gösterdiğini unutmayın - bu nedenle daha yeni bir modelle denemek farklı bir sonuç üretebilir.

### Kavram: Temel Modeller

Bir yönlendirme tokenleştirildikten sonra, ["Temel LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (veya Temel model) işlevi, bu dizideki tokenı tahmin etmektir. LLM'ler büyük metin veri setleri üzerinde eğitildiğinden, tokenlar arasındaki istatistiksel ilişkiler hakkında iyi bir anlayışa sahiptirler ve bu tahmini biraz güvenle yapabilirler. Yönlendirme veya token içindeki kelimelerin _anlamını_ anlamadıklarını unutmayın; sadece bir sonraki tahminleriyle "tamamlayabilecekleri" bir desen görürler. Kullanıcı müdahalesi veya önceden belirlenmiş bir koşul tarafından sonlandırılana kadar diziyi tahmin etmeye devam edebilirler.

Yönlendirme tabanlı tamamlamanın nasıl çalıştığını görmek ister misiniz? Yukarıdaki yönlendirmeyi varsayılan ayarlarla Azure OpenAI Studio [_Sohbet Oyun Alanı_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst)'na girin. Sistem, yönlendirmeleri bilgi talepleri olarak işlemeye ayarlanmıştır - bu nedenle bu bağlamı tatmin eden bir tamamlamayı görmelisiniz.

Ancak kullanıcı, belirli bir kriter veya görev hedefini karşılayan bir şey görmek isteseydi ne olurdu? İşte bu noktada _talimat ayarlı_ LLM'ler devreye girer.

### Kavram: Talimat Ayarlı LLM'ler

[Bir Talimat Ayarlı LLM](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst), temel modelle başlar ve örnekler veya giriş/çıkış çiftleri (örneğin, çok dönüşlü "mesajlar") ile ince ayar yapılır, bu da açık talimatlar içerebilir - ve AI'nın yanıtı bu talimatı izlemeye çalışır.

Bu, modelin _talimatları izlemesini_ ve _geri bildirimden öğrenmesini_ sağlayan, modelin pratik uygulamalara daha uygun ve kullanıcı hedeflerine daha alakalı yanıtlar üretmesini sağlayan İnsan Geri Bildirimi ile Takviye Öğrenme (RLHF) gibi teknikler kullanır.

Hadi deneyelim - yukarıdaki yönlendirmeye tekrar göz atın, ancak şimdi _sistem mesajını_ şu talimatı bağlam olarak sağlamak üzere değiştirin:

> _İkinci sınıf bir öğrenci için sağladığınız içeriği özetleyin. Sonucu 3-5 madde işareti ile bir paragraf olarak tutun._

Sonucun şimdi istenen hedefi ve formatı nasıl yansıttığını görüyor musunuz? Bir eğitimci artık bu yanıtı doğrudan o sınıf için slaytlarında kullanabilir.

## Neden Yönlendirme Mühendisliğine İhtiyacımız Var?

Artık yönlendirmelerin LLM'ler tarafından nasıl işlendiğini bildiğimize göre, neden yönlendirme mühendisliğine ihtiyacımız olduğunu konuşalım. Cevap, mevcut LLM'lerin _güvenilir ve tutarlı tamamlamaları_ daha fazla çaba sarf etmeden başarmayı zorlaştıran bir dizi zorluk sunmasında yatar. Örneğin:

1. **Model yanıtları stokastiktir.** _Aynı yönlendirme_, farklı modeller veya model sürümleriyle muhtemelen farklı yanıtlar üretecektir. Ve hatta farklı zamanlarda _aynı modelle_ farklı sonuçlar üretebilir. _Yönlendirme mühendisliği teknikleri, daha iyi kılavuzlar sağlayarak bu varyasyonları en aza indirmemize yardımcı olabilir_.

2. **Modeller yanıtları uydurabilir.** Modeller, _büyük ama sınırlı_ veri setleriyle önceden eğitildiğinden, bu eğitim kapsamı dışındaki kavramlar hakkında bilgi sahibi değildirler. Sonuç olarak, yanlış, hayali veya bilinen gerçeklerle doğrudan çelişen tamamlamalar üretebilirler. _Yönlendirme mühendisliği teknikleri, kullanıcıların AI'dan alıntılar veya akıl yürütme istemesi gibi fabrika uydurmalarını tanımlamasına ve hafifletmesine yardımcı olur_.

3. **Modellerin yetenekleri değişiklik gösterecektir.** Daha yeni modeller veya model nesilleri daha zengin yeteneklere sahip olacak, ancak aynı zamanda maliyet ve karmaşıklık açısından benzersiz tuhaflıklar ve ödünler getirecektir. _Yönlendirme mühendisliği, farklılıkları soyutlayan ve model özel gereksinimlere uyum sağlayan en iyi uygulamaları ve iş akışlarını ölçeklenebilir, sorunsuz bir şekilde geliştirmemize yardımcı olabilir_.

Bunu OpenAI veya Azure OpenAI Playground'da görelim:

- Aynı yönlendirmeyi farklı LLM dağıtımlarıyla (örneğin, OpenAI, Azure OpenAI, Hugging Face) kullanın - varyasyonları gördünüz mü?
- Aynı yönlendirmeyi _aynı_ LLM dağıtımıyla (örneğin, Azure OpenAI oyun alanı) tekrar tekrar kullanın - bu varyasyonlar nasıl farklılaştı?

### Uydurma Örneği

Bu kursta, LLM'lerin bazen eğitimlerindeki sınırlamalar veya diğer kısıtlamalar nedeniyle gerçeğe aykırı bilgi ürettikleri fenomeni referans almak için **"uydurma"** terimini kullanıyoruz. Ayrıca bunu popüler makalelerde veya araştırma makalelerinde _"halüsinasyonlar"_ olarak duymuş olabilirsiniz. Ancak, bir makine tarafından üretilen bir sonucu insan benzeri bir özellik atfederek antropomorfize etmeyelim diye _"uydurma"_ terimini kullanmanızı şiddetle öneririz. Bu aynı zamanda terminoloji açısından [Sorumlu AI yönergelerini](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) güçlendirir ve bazı bağlamlarda saldırgan veya kapsayıcı olmayan terimleri de ortadan kaldırır.

Uydurmaların nasıl çalıştığını görmek ister misiniz? AI'ya eğitim veri setinde bulunmayan bir konu için içerik üretme talimatı veren bir yönlendirme düşünün (böylece eğitim veri setinde bulunmadığından emin olun). Örneğin - bu yönlendirmeyi denedim:

> **Yönlendirme:** 2076 Mars Savaşı hakkında bir ders planı oluşturun.

Bir web araması, Mars savaşları hakkında (örneğin, televizyon dizileri veya kitaplar) kurgusal hesaplar olduğunu gösterdi - ancak 2076'da değil. Ortak akıl ayrıca 2076'nın _gelecekte_ olduğunu ve bu nedenle gerçek bir olayla ilişkilendirilemeyeceğini söylüyor.

Peki bu yönlendirmeyi farklı LLM sağlayıcılarıyla çalıştırdığımızda ne olur?

> **Yanıt 1**: OpenAI Playground (GPT-35)

> **Yanıt 2**: Azure OpenAI Playground (GPT-35)

> **Yanıt 3**: : Hugging Face Chat Playground (LLama-2)

Beklendiği gibi, her model (veya model sürümü) stokastik davranış ve model yetenek varyasyonları sayesinde biraz farklı yanıtlar üretiyor. Örneğin, bir model 8. sınıf izleyici kitlesini hedef alırken, diğeri lise öğrencisini varsayıyor. Ancak her üç model de bir bilgisi olmayan kullanıcıyı olayın gerçek olduğuna ikna edebilecek yanıtlar üretti

Metaprompting ve sıcaklık yapılandırması gibi yönlendirme mühendisliği teknikleri, model uydurmalarını bir dereceye kadar azaltabilir. Yeni yönlendirme mühendisliği _mimari_leri de bu etkileri hafifletmek veya azaltmak için yeni araçları ve teknikleri sorunsuz bir şekilde yönlendirme akışına dahil eder.

## Vaka Çalışması: GitHub Copilot

Bu bölümü, gerçek dünya çözümlerinde yönlendirme mühendisliğinin nasıl kullanıldığını anlamak için bir Vaka Çalışması: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst) ile kapatalım.

GitHub Copilot, "AI Çift Programcınız"dır - metin yönlendirmelerini kod tamamlama haline getirir ve kesintisiz bir kullanıcı deneyimi için geliştirme ortamınıza (örneğin,
Sonuç olarak, şablonların gerçek değeri, dikey uygulama alanları için _istem kütüphaneleri_ oluşturma ve yayınlama yeteneğinde yatar - burada istem şablonu artık uygulamaya özgü bağlamı veya yanıtları hedeflenen kullanıcı kitlesi için daha alakalı ve doğru hale getiren örnekleri yansıtacak şekilde _optimize edilmiştir_. [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) deposu, bu yaklaşımın harika bir örneğidir; ders planlama, müfredat tasarımı, öğrenci rehberliği gibi anahtar hedeflere vurgu yaparak eğitim alanı için bir istem kütüphanesi derler.

## Destekleyici İçerik

İstem oluşturmayı bir talimat (görev) ve bir hedef (ana içerik) olarak düşünürsek, _ikincil içerik_ **çıkışı bir şekilde etkilemek** için sağladığımız ek bağlam gibidir. Modelin yanıtını istenen kullanıcı hedeflerine veya beklentilerine uygun hale getirmesine yardımcı olabilecek ayar parametreleri, biçimlendirme talimatları, konu taksonomileri vb. olabilir.

Örneğin: Müfredattaki mevcut tüm dersler hakkında kapsamlı meta verilerle (isim, açıklama, seviye, meta veri etiketleri, eğitmen vb.) bir ders kataloğu verildiğinde:

- "2023 Güz dönemi için ders kataloğunu özetle" talimatını tanımlayabiliriz
- İstenen çıktının birkaç örneğini sağlamak için ana içeriği kullanabiliriz
- İlgi çekici ilk 5 "etiketi" belirlemek için ikincil içeriği kullanabiliriz.

Şimdi, model birkaç örnekle gösterilen formatta bir özet sağlayabilir - ancak bir sonuç birden fazla etikete sahipse, ikincil içerikte belirlenen 5 etiketi önceliklendirebilir.

---

<!--
DERS ŞABLONU:
Bu birim, temel kavram #1'i kapsamalıdır.
Kavramı örnekler ve referanslarla pekiştirin.

KAVRAM #3:
İstem Mühendisliği Teknikleri.
İstem mühendisliği için bazı temel teknikler nelerdir?
Bunu bazı alıştırmalarla gösterin.
-->

## İstemleme En İyi Uygulamaları

Artık istemlerin nasıl _oluşturulabileceğini_ bildiğimize göre, bunları en iyi uygulamaları yansıtacak şekilde nasıl _tasarlayabileceğimizi_ düşünmeye başlayabiliriz. Bunu iki bölümde düşünebiliriz - doğru _zihniyet_ ve doğru _teknikleri_ uygulamak.

### İstem Mühendisliği Zihniyeti

İstem Mühendisliği bir deneme-yanılma sürecidir, bu yüzden üç geniş yönlendirici faktörü aklınızda bulundurun:

1. **Alan Anlayışı Önemlidir.** Yanıt doğruluğu ve ilgililiği, uygulamanın veya kullanıcının çalıştığı _alanın_ bir fonksiyonudur. Teknikleri daha fazla **özelleştirmek** için sezginizi ve alan uzmanlığınızı uygulayın. Örneğin, sistem istemlerinizde _alana özgü kişilikler_ tanımlayın veya kullanıcı istemlerinizde _alana özgü şablonlar_ kullanın. Alana özgü bağlamları yansıtan ikincil içerik sağlayın veya modeli tanıdık kullanım kalıplarına yönlendirmek için _alana özgü ipuçları ve örnekler_ kullanın.

2. **Model Anlayışı Önemlidir.** Modellerin doğası gereği stokastik olduğunu biliyoruz. Ancak model uygulamaları, kullandıkları eğitim veri seti (önceden eğitilmiş bilgi), sağladıkları yetenekler (örneğin, API veya SDK aracılığıyla) ve optimize edildikleri içerik türü (örneğin, kod vs. görüntüler vs. metin) açısından da farklılık gösterebilir. Kullandığınız modelin güçlü ve zayıf yönlerini anlayın ve bu bilgiyi _görevleri önceliklendirmek_ veya modelin yeteneklerine göre optimize edilmiş _özelleştirilmiş şablonlar_ oluşturmak için kullanın.

3. **Yineleme ve Doğrulama Önemlidir.** Modeller hızla gelişiyor ve istem mühendisliği teknikleri de öyle. Bir alan uzmanı olarak, daha geniş topluluğa uygulanmayabilecek başka bağlamlar veya kriterler _sizin_ özel uygulamanız olabilir. İstem mühendisliği araçlarını ve tekniklerini istem oluşturmayı "hızlandırmak" için kullanın, ardından kendi sezginiz ve alan uzmanlığınızla sonuçları yineleyin ve doğrulayın. İçgörülerinizi kaydedin ve başkaları tarafından yeni bir temel olarak kullanılabilecek bir **bilgi tabanı** (örneğin, istem kütüphaneleri) oluşturun, gelecekteki yinelemeleri hızlandırmak için.

## En İyi Uygulamalar

Şimdi [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) ve [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) uygulayıcıları tarafından önerilen yaygın en iyi uygulamalara bir göz atalım.

| Ne                                | Neden                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| En son modelleri değerlendirin.   | Yeni model nesilleri muhtemelen geliştirilmiş özelliklere ve kaliteye sahip olacaktır - ancak daha yüksek maliyetler de getirebilir. Etkilerini değerlendirin, ardından geçiş kararları verin.                                                        |
| Talimatlar ve bağlamı ayırın      | Modelinizin/sağlayıcınızın talimatları, birincil ve ikincil içeriği daha net ayırt etmek için _sınırlandırıcılar_ tanımlayıp tanımlamadığını kontrol edin. Bu, modellerin ağırlıkları daha doğru bir şekilde atamasına yardımcı olabilir.                   |
| Belirli ve net olun               | İstenen bağlam, sonuç, uzunluk, biçim, stil vb. hakkında daha fazla ayrıntı verin. Bu, yanıtların hem kalitesini hem de tutarlılığını artıracaktır. Tarifleri yeniden kullanılabilir şablonlarda yakalayın.                                           |
| Açıklayıcı olun, örnekler kullanın | Modeller "göster ve anlat" yaklaşımına daha iyi yanıt verebilir. `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` değerleriyle başlayın. Nasıl öğrenileceğini öğrenmek için [Öğrenme Alanı bölümüne](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) geri dönün.

### Şimdi, Jupyter Notebook'u açın

- Çalışma zamanı çekirdeğini seçin. Seçenek 1 veya 2'yi kullanıyorsanız, yalnızca geliştirici konteyner tarafından sağlanan varsayılan Python 3.10.x çekirdeğini seçin.

Egzersizleri çalıştırmaya hazırsınız. Burada _doğru ve yanlış_ cevaplar olmadığını unutmayın - sadece deneme-yanılma yoluyla seçenekleri keşfetmek ve belirli bir model ve uygulama alanı için neyin işe yaradığını anlamak.

_Bu nedenle, bu derste Kod Çözümü bölümleri yoktur. Bunun yerine, Notebook'ta referans için bir örnek çıktı gösteren "Benim Çözümüm:" başlıklı Markdown hücreleri olacaktır._

 <!--
DERS ŞABLONU:
Bölümü bir özet ve kendi kendine öğrenme için kaynaklarla tamamlayın.
-->

## Bilgi Kontrolü

Aşağıdakilerden hangisi bazı makul en iyi uygulamaları takip eden iyi bir istemdir?

1. Bana kırmızı bir araba resmi göster
2. Bana güneş batarken bir uçurum kenarında park etmiş Volvo marka ve XC90 model kırmızı bir araba resmi göster
3. Bana Volvo marka ve XC90 model kırmızı bir araba resmi göster

Cevap: 2, en iyi istemdir çünkü "ne" hakkında ayrıntılar sağlar ve belirli bir marka ve modelle (sadece herhangi bir araba değil) ilgilidir ve ayrıca genel ayarı tanımlar. 3, aynı zamanda çok fazla açıklama içerdiği için bir sonraki en iyisidir.

## 🚀 Meydan Okuma

"Volvo marka kırmızı bir araba resmi göster ve " cümlesini tamamla istemi ile "ipucu" tekniğini kullanabilir misiniz? Ne yanıt veriyor ve bunu nasıl geliştirebilirsiniz?

## Harika İş! Öğrenmeye Devam Edin

Farklı İstem Mühendisliği kavramları hakkında daha fazla bilgi edinmek ister misiniz? Bu konuyla ilgili diğer harika kaynakları bulmak için [devam eden öğrenme sayfasına](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) gidin.

[ileri istem tekniklerine](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst) bakacağımız 5. Derse gidin!

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.