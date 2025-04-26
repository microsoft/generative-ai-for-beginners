# Farklı LLM'leri Keşfetme ve Karşılaştırma

[![Farklı LLM'leri Keşfetme ve Karşılaştırma](../../images/02-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson2-gh?WT.mc_id=academic-105485-koreyst)

> _Bu dersin videosunu izlemek için yukarıdaki görsele tıklayın_

Önceki derste, Üretici Yapay Zeka'nın teknoloji dünyasını nasıl değiştirdiğini, Büyük Dil Modellerinin (LLM'ler) nasıl çalıştığını ve bir işletmenin - bizim startup'ımız gibi - bunları kendi kullanım senaryolarına nasıl uygulayıp büyüyebileceğini gördük. Bu bölümde, farklı büyük dil modellerini (LLM'ler) karşılaştırarak avantaj ve dezavantajlarını anlamaya çalışacağız.

Startup'ımızın yolculuğundaki bir sonraki adım, mevcut LLM'lerin durumunu keşfetmek ve hangilerinin kullanım senaryomuz için uygun olduğunu anlamaktır.

## Giriş

Bu ders şunları kapsayacak:

- Mevcut LLM türleri.
- Azure'da kullanım senaryonuz için farklı modelleri test etme, yineleme ve karşılaştırma.
- Bir LLM'in nasıl dağıtılacağı.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra:

- Kullanım senaryonuz için doğru modeli seçebilecek,
- Modelinizin performansını nasıl test edeceğinizi, yineleyeceğinizi ve iyileştireceğinizi anlayacak,
- İşletmelerin modelleri nasıl dağıttığını bileceksiniz.

## Farklı LLM Türlerini Anlama

LLM'ler mimarilerine, eğitim verilerine ve kullanım senaryolarına göre birden fazla kategoriye ayrılabilir. Bu farklılıkları anlamak, startup'ımızın senaryo için doğru modeli seçmesine ve modelin performansını nasıl test edeceğini, yineleyeceğini ve iyileştireceğini anlamasına yardımcı olacaktır.

Birçok farklı LLM modeli türü vardır, model seçiminiz bunları ne için kullanmayı amaçladığınıza, verilerinize, ne kadar ödeme yapmaya hazır olduğunuza ve daha fazlasına bağlıdır.

Modelleri metin, ses, video, görüntü oluşturma vb. için kullanmayı amaçlamanıza bağlı olarak, farklı bir model türünü seçebilirsiniz.

- **Ses ve konuşma tanıma**. Bu amaç için, Whisper tipi modeller genel amaçlı ve konuşma tanımaya yönelik oldukları için harika bir seçimdir. Çeşitli ses verileriyle eğitilmiştir ve çok dilli konuşma tanıma yapabilir. [Whisper tipi modeller hakkında buradan](https://platform.openai.com/docs/models/whisper?WT.mc_id=academic-105485-koreyst) daha fazla bilgi edinebilirsiniz.

- **Görüntü oluşturma**. Görüntü oluşturma için, DALL-E ve Midjourney çok iyi bilinen iki seçenektir. DALL-E, Azure OpenAI tarafından sunulmaktadır. [DALL-E hakkında buradan](https://platform.openai.com/docs/models/dall-e?WT.mc_id=academic-105485-koreyst) ve bu müfredatın 9. Bölümünden daha fazla bilgi edinebilirsiniz.

- **Metin oluşturma**. Çoğu model metin oluşturma üzerine eğitilmiştir ve GPT-3.5'ten GPT-4'e kadar geniş bir seçenek yelpazesine sahipsiniz. GPT-4'ün en pahalı olduğu farklı maliyetlerle gelirler. Yetenek ve maliyet açısından hangi modellerin ihtiyaçlarınıza en uygun olduğunu değerlendirmek için [Azure OpenAI playground](https://oai.azure.com/portal/playground?WT.mc_id=academic-105485-koreyst)'a göz atmanızda fayda var.

- **Çoklu modalite**. Girdi ve çıktıda birden fazla veri türünü işlemeyi düşünüyorsanız, doğal dil işlemeyi görsel anlama ile birleştirebilen ve çoklu modal arayüzler aracılığıyla etkileşime olanak tanıyan [gpt-4 turbo with vision veya gpt-4](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models?WT.mc_id=academic-105485-koreyst) gibi modellere - OpenAI modellerinin en son sürümlerine - bakabilirsiniz.

Bir model seçmek, temel yetenekler elde etmek anlamına gelir, ancak bu her zaman yeterli olmayabilir. Çoğu zaman, modelinize şirketinize özel verileri aktarmanız gerekir. Bunu yapmanın birkaç farklı yolu vardır; bunlara ilerleyen bölümlerde daha ayrıntılı değineceğiz.

### Temel Modeller ve Büyük Dil Modelleri (LLM'ler)

"Temel Model" terimi, [Stanford araştırmacıları tarafından ortaya atılmıştır](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) ve şu kriterleri karşılayan yapay zeka modellerini tanımlamak için kullanılır:

- **Denetimsiz öğrenme veya kendi kendine denetimli öğrenme ile eğitilirler**, etiketlenmemiş çok modlu verilerle eğitildikleri ve eğitim süreçlerinde insan tarafından yapılan veri açıklamalarına veya etiketlemelere ihtiyaç duymadıkları anlamına gelir.
- **Çok büyük modellerdir**, milyarlarca parametre içeren çok derin sinir ağlarına dayanırlar.
- **Diğer modeller için bir "temel" olarak kullanılmaları amaçlanır**,  başka modellerin bu temel model üzerine inşa edilebileceği anlamına gelir; bu işlem genellikle ince ayar (fine-tuning) ile gerçekleştirilir.

![Temel Modeller ve LLM'ler](../../images/FoundationModel.png?WT.mc_id=academic-105485-koreyst)

Görsel kaynağı: [Essential Guide to Foundation Models and Large Language Models | Babar M Bhatti tarafından | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Bu ayrımı daha net hale getirmek için ChatGPT'yi örnek alalım. ChatGPT'nin ilk versiyonunu oluşturmak için GPT-3.5 adlı bir model temel model olarak kullanıldı. Yani, OpenAI, GPT-3.5 modelini sohbet senaryolarında daha iyi performans gösterecek şekilde özel sohbet verileriyle özelleştirdi.

![Temel Model](../../images/Multimodal.png?WT.mc_id=academic-105485-koreyst)

Görsel Kaynağı: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Açık Kaynak ve Tescilli Modeller

Bir başka LLM kategorisi, modellerin açık kaynak mı yoksa tescilli mi olduğuna dayalıdır.

Açık kaynak modeller, halka açık olan ve herkes tarafından kullanılabilen modellerdir. Genellikle modelin geliştiricileri veya araştırma toplulukları tarafından yayımlanırlar. Bu modeller incelenebilir, değiştirilebilir ve farklı kullanım senaryolarına göre özelleştirilebilir. Ancak, her zaman üretim kullanımı için optimize edilmemiş olabilirler ve tescilli modellere kıyasla performans açısından daha zayıf olabilirler. Ayrıca, açık kaynak modellerin finansmanı sınırlı olabilir, uzun vadede bakımları sağlanamayabilir veya en son araştırmalarla güncellenmeyebilirler. Popüler açık kaynak modellere örnek olarak [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html?WT.mc_id=academic-105485-koreyst), [Bloom](https://huggingface.co/bigscience/bloom) ve  [LLaMA](https://llama.meta.com) verilebilir.

Tescilli modeller, bir şirketin sahip olduğu ve halka açık olmayan modellerdir. Genellikle üretim ortamı için optimize edilmiştir. Ancak, kullanıcılar bu modelleri inceleyemez, değiştiremez veya farklı kullanım senaryolarına göre özelleştiremez. Ayrıca, genellikle ücretsiz olarak sunulmazlar ve kullanım için abonelik veya ödeme gerektirebilirler. Kullanıcılar, modelin eğitiminde kullanılan veriler üzerinde kontrole sahip olamazlar ve veri gizliliği ile sorumlu yapay zeka ilkelerinin model sahibi tarafından sağlanmasına güvenmek zorundadırlar. Popüler tescilli modellere örnek olarak [OpenAI modelleri](https://platform.openai.com/docs/models/overview?WT.mc_id=academic-105485-koreyst), [Google Bard](https://sapling.ai/llm/bard?WT.mc_id=academic-105485-koreyst) ve [Claude 2](https://www.anthropic.com/index/claude-2?WT.mc_id=academic-105485-koreyst) verilebilir.

### Gömme, Görüntü Üretimi ve Metin/Kod Üretimi

LLM'ler, ürettikleri çıktılara göre de kategorize edilebili

Gömme (Embedding) modelleri, metni sayısal bir forma dönüştürerek makinelerin kelimeler veya cümleler arasındaki ilişkileri anlamasını sağlar. Bu modeller genellikle sınıflandırma veya kümeleme gibi diğer yapay zeka modelleri için giriş verisi olarak kullanılır. Örneğin [OpenAI embedding modelleri](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Gömme (Embedding)](../../images/Embedding.png?WT.mc_id=academic-105485-koreyst)

Görüntü Üretimi modelleri, yeni görüntüler oluşturabilir veya mevcut görüntüleri düzenleyebilir. Örneğin, [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), [DALL-E-3](https://openai.com/dall-e-3?WT.mc_id=academic-105485-koreyst) ve [Stable Diffusion models](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst).

![Görsel oluşturucu](../../images/Image.png?WT.mc_id=academic-105485-koreyst)

Metin ve kod oluşturma modelleri, metin veya kod üreten modellerdir. Bu modeller genellikle metin özetleme, çeviri ve soru-cevap gibi görevler için kullanılır. Metin oluşturma modelleri genellikle [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst) gibi büyük metin veri kümeleri üzerinde eğitilir ve yeni metinler oluşturmak veya soruları yanıtlamak için kullanılabilir. Kod oluşturma modelleri, [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst) gibi, genellikle GitHub gibi büyük kod veri kümeleri üzerinde eğitilir ve yeni kod üretmek veya mevcut koddaki hataları düzeltmek için kullanılabilir.

![Metin ve Kod Oluşturucu](../../images/Text.png?WT.mc_id=academic-105485-koreyst)

### Kodlayıcı-Kod Çözücü ve Sadece Kod Çözücü Karşılaştırması

LLM'lerin farklı mimari türleri hakkında konuşmak için bir benzetme kullanalım.

Yöneticinizin size öğrenciler için bir sınav yazma görevi verdiğini düşünün. İki iş arkadaşınız var; biri içeriği oluşturmaktan, diğeri ise bunları gözden geçirmekten sorumlu.

İçerik oluşturucu, sadece Kod Çözücü model gibidir, konuya bakabilir ve zaten yazdıklarınızı görebilir ve buna dayanarak bir ders yazabilir. İlgi çekici ve bilgilendirici içerik yazmakta çok iyidirler, ancak konuyu ve öğrenme hedeflerini anlamakta çok iyi değildirler. Kod Çözücü modellere örnek olarak GPT-3 gibi GPT ailesi modelleri verilebilir.

İnceleyici, sadece Kodlayıcı model gibidir, yazılan dersi ve cevapları inceler, aralarındaki ilişkiyi fark eder ve bağlamı anlar, ancak içerik üretmekte iyi değildir. Sadece Kodlayıcı modele örnek olarak BERT verilebilir.

Sınavı hem oluşturabilen hem de gözden geçirebilen birisine de sahip olabileceğimizi düşünün, bu bir Kodlayıcı-Kod Çözücü modeldir. BART ve T5 buna örnek olarak verilebilir.

### Hizmet ve Model Karşılaştırması

Şimdi, bir hizmet ve model arasındaki farkı konuşalım. Hizmet, bir Bulut Hizmet Sağlayıcısı tarafından sunulan bir üründür ve genellikle modeller, veriler ve diğer bileşenlerin bir kombinasyonudur. Model, bir hizmetin temel bileşenidir ve genellikle LLM gibi bir temel modeldir.

Hizmetler genellikle üretim kullanımı için optimize edilmiştir ve grafiksel kullanıcı arayüzü sayesinde modellerden daha kolay kullanılır. Ancak, hizmetler her zaman ücretsiz değildir ve hizmet sahibinin ekipman ve kaynaklarından yararlanmak, giderleri optimize etmek ve kolayca ölçeklendirmek karşılığında kullanmak için abonelik veya ödeme gerektirebilir. Bir hizmet örneği olarak [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst) verilebilir; kullandıkça öde fiyatlandırma planı sunar, yani kullanıcılar hizmeti ne kadar kullandıklarına göre orantılı olarak ücretlendirilir. Ayrıca, Azure OpenAI Service, modellerin yeteneklerinin üzerine kurumsal düzeyde güvenlik ve sorumlu yapay zeka çerçevesi sunar.

Modeller sadece parametreler, ağırlıklar ve diğerleriyle birlikte Sinir Ağıdır. Şirketlerin yerel olarak çalıştırmasına izin vermek için ekipman satın almaları, ölçeklendirme için bir yapı kurmaları ve lisans satın almaları veya açık kaynaklı bir model kullanmaları gerekir. LLaMA gibi bir model kullanılabilir durumdadır, ancak modeli çalıştırmak için hesaplama gücü gerektirir.

## Azure'da Farklı Modellerin Performansını Anlamak İçin Test ve Yineleme

Ekibimiz mevcut LLM'lerin durumunu keşfettikten ve senaryoları için iyi adayları belirledikten sonra, bir sonraki adım bunları kendi verileri ve iş yükleri üzerinde test etmektir. Bu, deneyler ve ölçümlerle yapılan yinelemeli bir süreçtir.
Önceki paragraflarda bahsettiğimiz modellerin çoğu (OpenAI modelleri, Llama2 gibi açık kaynak modeller ve Hugging Face dönüştürücüleri) [Azure AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)'daki [Model Kataloğu](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview?WT.mc_id=academic-105485-koreyst)'nda mevcuttur.

[Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/what-is-ai-studio?WT.mc_id=academic-105485-koreyst), geliştiricilerin üretici yapay zeka uygulamaları oluşturması ve tüm geliştirme yaşam döngüsünü - denemeden değerlendirmeye kadar - kullanışlı bir GUI ile tüm Azure AI hizmetlerini tek bir merkezde birleştirerek yönetmesi için tasarlanmış bir Bulut Platformudur. Azure AI Studio'daki Model Kataloğu kullanıcıya şunları sağlar:

- Katalogda ilgilenilen Temel Modeli bulma - özel veya açık kaynak, görev, lisans veya ada göre filtreleme. Aranabilirliği artırmak için modeller Azure OpenAI koleksiyonu, Hugging Face koleksiyonu ve daha fazlası gibi koleksiyonlara ayrılmıştır.

![Model kataloğu](../../images/AzureAIStudioModelCatalog.png?WT.mc_id=academic-105485-koreyst)

- Model kartını inceleme, amaçlanan kullanım ve eğitim verileri hakkında ayrıntılı açıklama, kod örnekleri ve dahili değerlendirmeler kütüphanesindeki değerlendirme sonuçları dahil.

![Model kartı](../../images/ModelCard.png?WT.mc_id=academic-105485-koreyst)

- İş senaryosuna uygun olanı değerlendirmek için [Model Karşılaştırmaları](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst) paneli aracılığıyla sektörde mevcut modeller ve veri setleri arasında karşılaştırma yapma.

![Model karşılaştırmaları](../../images/ModelBenchmarks.png?WT.mc_id=academic-105485-koreyst)

- Azure AI Studio'nun deneme ve izleme yeteneklerinden yararlanarak, belirli bir iş yükünde model performansını iyileştirmek için modeli özel eğitim verileri üzerinde ince ayarlama.

![Model ince ayarı](../../images/FineTuning.png?WT.mc_id=academic-105485-koreyst)

- Uygulamaların tüketebilmesi için orijinal önceden eğitilmiş modeli veya ince ayarlı versiyonu uzak gerçek zamanlı çıkarım - yönetilen hesaplama - veya sunucusuz api uç noktasına - [kullandıkça öde](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview#model-deployment-managed-compute-and-serverless-api-pay-as-you-go?WT.mc_id=academic-105485-koreyst) - dağıtma.

![Model dağıtımı](../../images/ModelDeploy.png?WT.mc_id=academic-105485-koreyst)

> [!NOT]
> Katalogdaki tüm modeller şu anda ince ayar ve/veya kullandıkça öde dağıtımı için mevcut değildir. Model yetenekleri ve sınırlamaları hakkında ayrıntılar için model kartını kontrol edin.

## LLM Sonuçlarını İyileştirme

Startup ekibimizle farklı LLM türlerini ve farklı modelleri karşılaştırmamızı, test verileri üzerinde değerlendirmemizi, performansı iyileştirmemizi ve çıkarım uç noktalarına dağıtmamızı sağlayan bir Bulut Platformunu (Azure Machine Learning) keşfettik.

Peki önceden eğitilmiş bir model kullanmak yerine ne zaman bir modeli ince ayarlamayı düşünmeliler? Belirli iş yüklerinde model performansını iyileştirmek için başka yaklaşımlar var mı?

Bir işletmenin bir LLM'den ihtiyaç duyduğu sonuçları alması için kullanabileceği birkaç yaklaşım vardır. Üretimde bir LLM dağıtırken farklı karmaşıklık, maliyet ve kalite seviyeleriyle farklı eğitim derecelerine sahip farklı model türleri seçebilirsiniz. İşte bazı farklı yaklaşımlar:

- **Bağlamla istem mühendisliği**. Fikir, ihtiyacınız olan yanıtları aldığınızdan emin olmak için istem verirken yeterli bağlam sağlamaktır.

- **Geri Alma Artırılmış Üretim, RAG**. Verileriniz örneğin bir veritabanında veya web uç noktasında bulunabilir, bu verinin veya bir alt kümesinin istem zamanında dahil edilmesini sağlamak için ilgili verileri alabilir ve kullanıcının isteminin bir parçası haline getirebilirsiniz.

- **İnce ayarlı model**. Burada, modeli kendi verileriniz üzerinde daha fazla eğittiniz, bu da modelin ihtiyaçlarınıza daha kesin ve duyarlı olmasını sağladı ancak maliyetli olabilir.

![LLM'lerin dağıtımı](../../images/Deploy.png?WT.mc_id=academic-105485-koreyst)

Görsel kaynağı: [İşletmelerin LLM'leri Dağıtmasının Dört Yolu | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Bağlamla İstem Mühendisliği

Önceden eğitilmiş LLM'ler, kısa bir istemle bile - tamamlanacak bir cümle veya bir soru gibi - genel doğal dil görevlerinde çok iyi çalışır - buna "sıfır-atış" öğrenme denir.

Ancak, kullanıcı sorgusunu ne kadar detaylı bir istek ve örneklerle - Bağlam - çerçeveleyebilirse, yanıt o kadar doğru ve kullanıcının beklentilerine yakın olacaktır. Bu durumda, istem yalnızca bir örnek içeriyorsa "tek-atış" öğrenmeden, birden fazla örnek içeriyorsa "az-atış öğrenme"den bahsederiz.
Bağlamla istem mühendisliği, başlamak için en maliyet-etkin yaklaşımdır.

### Geri Alma Artırılmış Üretim (RAG)

LLM'ler yalnızca eğitimleri sırasında kullanılan verileri bir yanıt üretmek için kullanabilme sınırlamasına sahiptir. Bu, eğitim süreçlerinden sonra gerçekleşen olaylar hakkında hiçbir şey bilmedikleri ve halka açık olmayan bilgilere (şirket verileri gibi) erişemedikleri anlamına gelir.
Bu, RAG ile aşılabilir; istem uzunluğu sınırlarını dikkate alarak, belge parçaları şeklinde dış verilerle istemi artıran bir tekniktir. Bu, çeşitli önceden tanımlanmış veri kaynaklarından yararlı parçaları alan ve bunları istem Bağlamına ekleyen Vektör veritabanı araçları (örneğin [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) tarafından desteklenir.

Bu teknik, bir işletmenin bir LLM'yi ince ayarlamak için yeterli verisi, zamanı veya kaynağı olmadığında, ancak yine de belirli bir iş yükünde performansı iyileştirmek ve uydurma risklerini azaltmak istediğinde çok yararlıdır, yani gerçeğin mistifikasyonu veya zararlı içerik.

### İnce Ayarlı Model

İnce ayarlama, modeli bir alt görev için 'uyarlamak' veya belirli bir sorunu çözmek için transfer öğrenmeden yararlanan bir süreçtir. Az-atış öğrenme ve RAG'den farklı olarak, güncellenmiş ağırlıklar ve yanlılıklarla yeni bir model oluşturulmasıyla sonuçlanır. Tek bir girdi (istem) ve ilişkili çıktısından (tamamlama) oluşan bir eğitim örnekleri seti gerektirir.
Şu durumlarda tercih edilen yaklaşım olacaktır:

- **İnce ayarlı modeller kullanma**. Bir işletme, daha maliyet etkin ve hızlı bir çözümle sonuçlanan yüksek performanslı modeller yerine ince ayarlı daha az yetenekli modeller (gömme modelleri gibi) kullanmak isteyebilir.

- **Gecikmeyi dikkate alma**. Belirli bir kullanım senaryosu için gecikme önemlidir, bu nedenle çok uzun istemler kullanmak mümkün değildir veya modelden öğrenilmesi gereken örnek sayısı istem uzunluğu sınırına uymaz.

- **Güncel kalma**. Bir işletmenin çok sayıda yüksek kaliteli verisi ve temel gerçek etiketleri ile bu verileri zaman içinde güncel tutmak için gereken kaynakları vardır.

### Eğitilmiş Model

Sıfırdan bir LLM eğitmek şüphesiz benimsenmesi en zor ve en karmaşık yaklaşımdır, büyük miktarda veri, yetenekli kaynaklar ve uygun hesaplama gücü gerektirir. Bu seçenek yalnızca bir işletmenin alana özgü bir kullanım senaryosu ve büyük miktarda alan merkezli verisi olduğu bir senaryoda düşünülmelidir.

## Bilgi Kontrolü

LLM tamamlama sonuçlarını iyileştirmek için iyi bir yaklaşım ne olabilir?

1. Bağlamla istem mühendisliği
2. RAG
3. İnce ayarlı model

C:3, eğer zamanınız, kaynaklarınız ve yüksek kaliteli verileriniz varsa, güncel kalmak için ince ayarlama daha iyi bir seçenektir. Ancak, işleri iyileştirmek istiyorsanız ve zamanınız kısıtlıysa, önce RAG'ı düşünmek faydalı olabilir.

## 🚀 Challenge

İşletmeniz için [RAG'ı nasıl kullanabileceğiniz](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) hakkında daha fazla bilgi edinin.

## Harika İş, Öğrenmeye Devam Edin

Bu dersi tamamladıktan sonra, Üretici Yapay Zeka bilginizi artırmaya devam etmek için [Üretici Yapay Zeka Öğrenme koleksiyonumuza](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) göz atın!

[Üretici Yapay Zeka'yı Sorumlu Bir Şekilde Oluşturma](../../../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst) konusunu inceleyeceğimiz Ders 3'e geçin!
