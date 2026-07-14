# Farklı LLM'leri Keşfetmek ve Karşılaştırmak

[![Farklı LLM'leri Keşfetmek ve Karşılaştırmak](../../../translated_images/tr/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Bu dersin videosunu izlemek için yukarıdaki görsele tıklayın_

Önceki derste, Üretken Yapay Zekanın teknoloji ortamını nasıl değiştirdiğini, Büyük Dil Modellerinin (LLM'ler) nasıl çalıştığını ve bir işletmenin - bizim startup'ımız gibi - bunları kullanım senaryolarına nasıl uygulayıp büyütebileceğini gördük! Bu bölümde, farklı türde büyük dil modellerini (LLM'ler) karşılaştırıp kıyaslayarak avantajlarını ve dezavantajlarını anlamaya çalışacağız.

Startup'ımızın yolculuğundaki bir sonraki adım, LLM'lerin mevcut ortamını keşfetmek ve hangilerinin kullanım senaryomuza uygun olduğunu anlamak.

## Giriş

Bu ders şunları kapsayacak:

- Mevcut ortamda farklı LLM türleri.
- Azure'da kullanım senaryonuza yönelik farklı modelleri test etme, yineleme ve karşılaştırma.
- Bir LLM nasıl dağıtılır.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra:

- Kullanım senaryonuza uygun modeli seçebileceksiniz.
- Modelinizi nasıl test edeceğinizi, yineleyeceğinizi ve performansını nasıl artıracağınızı anlayabileceksiniz.
- İşletmelerin modelleri nasıl dağıttığını bileceksiniz.

## Farklı LLM Türlerini Anlamak

LLM'ler, mimarileri, eğitim verileri ve kullanım amaçlarına göre çeşitli kategorilere ayrılabilir. Bu farklılıkları anlamak, startup'ımızın senaryoya uygun doğru modeli seçmesine ve performansı test etmek, yinelemek ve artırmak için nasıl yaklaşacağını anlamasına yardımcı olacaktır.

Pek çok farklı LLM modeli var; model seçiminiz ne için kullanacağınız, veriniz, ne kadar ödeme yapmaya hazır olduğunuz gibi faktörlere bağlıdır.

Modelleri metin, ses, video, görüntü üretimi gibi amaçlarla kullanmayı planlıyorsanız, farklı türde modelleri tercih edebilirsiniz.

- **Ses ve konuşma tanıma**. Whisper tarzı modeller hâlâ genel amaçlı konuşma tanıma için faydalıdır, ancak üretim tercihleri şimdi ayrıca `gpt-4o-transcribe`, `gpt-4o-mini-transcribe` ve diarizasyon varyantları gibi yeni konuşmadan metne modelleri de içerir. Senaryonuz için dil kapsamını, diarizasyonu, gerçek zamanlı desteği, gecikmeyi ve maliyeti değerlendirin. Detaylı bilgi için [OpenAI konuşmadan metne dokümantasyonuna](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst) bakın.

- **Görüntü üretimi**. DALL-E ve Midjourney bilinen görüntü üretim seçenekleridir, ancak mevcut OpenAI görüntü API'leri `gpt-image-2` gibi GPT Image modelleri üzerine odaklanır; Stable Diffusion, Imagen, Flux ve diğer model aileleri de yaygın tercihlerdir. İstek uyumu, düzenleme desteği, stil kontrolü, güvenlik gereklilikleri ve lisanslamayı karşılaştırın. Daha fazla bilgi için [OpenAI görüntü üretim kılavuzuna](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) ve bu müfredatın 9. Bölümüne bakın.

- **Metin üretimi**. Metin modelleri şimdi frontier modeller, düşünme modelleri, daha küçük düşük gecikmeli modeller ve açık ağırlıklı modeller arasında çeşitlilik gösterir. Güncel örnekler arasında OpenAI GPT-5.x modelleri, Anthropic Claude 4.x modelleri, Google Gemini 3.x modelleri, Meta Llama 4 modelleri ve Mistral modeller var. Sadece yayın tarihi veya fiyata göre seçim yapmayın; görev kalitesi, gecikme, bağlam penceresi, araç kullanımı, güvenlik davranışı, bölgesel erişilebilirlik ve toplam maliyeti karşılaştırın. Azure'da mevcut modelleri karşılaştırmak için [Microsoft Foundry model kataloğu](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) iyi bir kaynaktır.

- **Çok modüllülük (Multi-modality)**. Pek çok güncel model sadece metin işlemiyor. Bazıları görüntü, ses veya video girişlerini kabul ediyor; bazıları araç çağırabiliyor; bazı özel modeller ise görüntü, ses veya video üretebiliyor. Örneğin, OpenAI'nin mevcut modelleri metin ve görüntü girişini destekler, Gemini modelleri varyanta bağlı olarak metin, kod, görüntü, ses ve video girişlerini destekleyebilir ve Llama 4 Scout ile Maverick açık ağırlıklı yerel multimodal modellerdir. Bir iş akışı kurmadan önce her model kartında desteklenen giriş ve çıkış modlarını kontrol edin.

Bir model seçmek temel yetenekler sağlar, ancak bu her zaman yeterli olmayabilir. Genellikle şirketinize özgü veriler vardır ve bunları LLM'e bir şekilde anlatmanız gerekir. Bu konuda yaklaşım için birkaç farklı seçenek bulunmakta, bunları sonraki bölümlerde ele alacağız.

### Foundation Modeller ve LLM'ler Arasındaki Fark

Foundation Model terimi [Stanford araştırmacıları tarafından ortaya konmuş](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) ve şu kriterlere sahip bir yapay zeka modeli olarak tanımlanmıştır:

- **Denetimsiz ya da kendi kendine denetimli öğrenme ile eğitilmişlerdir**, yani etiketlenmemiş çok modlu veriler üzerinde eğitilirler, eğitim süreçleri için insan anotasyonu veya etiketlemeye ihtiyaç duymazlar.
- **Çok büyük modellerdir**, milyarlarca parametre üzerinde eğitilmiş çok derin sinir ağlarına dayanırlar.
- **Genellikle diğer modeller için bir ‘temel’ olarak hizmet etmeleri amaçlanır**, yani diğer modellerin üzerine inşa edilmek üzere başlangıç noktası olarak kullanılabilirler, bu ince ayar ile yapılabilir.

![Foundation Models ve LLM'ler](../../../translated_images/tr/FoundationModel.e4859dbb7a825c94.webp)

Görsel kaynağı: [Foundation Models and Large Language Models için Temel Rehber | Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Bu ayrımı daha da netleştirmek için, tarihi bir örnek olarak ChatGPT'yi ele alalım. İlk ChatGPT versiyonları GPT-3.5 foundation model olarak kullanıyordu. OpenAI, sohbet spesifik veriler ve hizalama teknikleri kullanarak sohbet robotları gibi senaryolarda daha iyi performans gösteren ince ayarlanmış bir versiyon oluşturdu. Modern yapay zeka servisleri genellikle birkaç model varyantı arasında geçiş yapar, bu yüzden servis adı ile altında yatan model ismi her zaman aynı değildir.

![Foundation Model](../../../translated_images/tr/Multimodal.2c389c6439e0fc51.webp)

Görsel kaynağı: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Açık Ağırlıklı / Açık Kaynak ve Telifli Modeller

LLM'leri kategorize etmenin bir diğer yolu da açık ağırlıklı, açık kaynak veya telifli olmalarıdır.

Açık kaynak ve açık ağırlıklı modeller, model parçalarını inceleme, indirme veya özelleştirme için erişilebilir kılar, ancak lisansları farklıdır. Bazıları tamamen açık kaynaktır, bazıları ise kullanım kısıtlamaları olan açık ağırlıklı modellerdir. Bu modeller, işletmelerin dağıtım, veri yerelliği, maliyet veya özelleştirme üzerinde daha fazla kontrol istediğinde faydalıdır. Ancak ekipler üretim ortamında kullanmadan önce lisans şartlarını, sunum maliyetlerini, bakımını, güvenlik güncellemelerini ve değerlendirme kalitesini incelemelidir. Örnekler arasında [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), bazı [Mistral modelleri](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst) ve [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst) üzerinde barındırılan birçok model bulunur.

Telifli modeller bir sağlayıcı tarafından sahiplenilir ve barındırılır. Bu modeller genellikle yönetilen üretim kullanımı için optimize edilir ve güçlü destek, güvenlik sistemleri, araç entegrasyonu ve ölçeklendirme sunabilir. Ancak müşteriler genellikle model ağırlıklarını gözlemleyemez veya değiştiremez; gizlilik, saklama, uyumluluk ve kabul edilebilir kullanım için sağlayıcı şartlarını incelemeleri gerekmektedir. Örnekler arasında [OpenAI modelleri](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst) ve [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst) modelleri bulunur.

### Gömme (Embedding), Görüntü Üretimi ve Metin & Kod Üretimi

LLM'ler ürettikleri çıktıya göre de kategorize edilebilir.

Gömme modelleri, metni sayısal bir biçime dönüştürebilen, yani giriş metninin sayısal temsili olan embedding üreten modellerdir. Gömme, makinelerin kelimeler veya cümleler arasındaki ilişkiyi daha kolay anlamasını sağlar ve diğer modeller tarafından, örneğin sınıflandırma veya sayısal veride daha iyi performans gösteren kümeleme modellerinde giriş olarak kullanılabilir. Gömme modelleri genellikle, veri bolluğunun fazla olduğu vekil bir görev için model oluşturulup bu model ağırlıklarının (embeddinglerin) sonraki görevlerde tekrar kullanıldığı transfer öğrenmede kullanılır. Bu kategoriye örnek olarak [OpenAI gömme modelleri](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst) verilebilir.

![Gömme](../../../translated_images/tr/Embedding.c3708fe988ccf760.webp)

Görüntü üretimi modelleri, görüntü üreten modellere denir. Bu modeller genellikle görüntü düzenleme, sentezleme ve çeviri için kullanılır. Görüntü üretimi modelleri genellikle [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst) gibi geniş görüntü veri setleri üzerinde eğitilir ve yeni görüntüler oluşturabilir veya var olan görüntüleri inpainting, süper çözünürlük ve renklendirme teknikleri ile düzenleyebilir. Örnekler arasında [GPT Image modelleri](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [Stable Diffusion modelleri](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst) ve Imagen modelleri bulunmaktadır.

![Görüntü üretimi](../../../translated_images/tr/Image.349c080266a763fd.webp)

Metin ve kod üretimi modelleri, metin veya kod üreten modellere denir. Bu modeller genellikle metin özetleme, çeviri ve soru yanıtlama için kullanılır. Metin üretim modelleri genellikle [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst) gibi büyük metin veri setleri üzerinde eğitilir ve yeni metin üretebilir veya soruları yanıtlayabilir. Kod üretim modelleri, örneğin [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), GitHub gibi büyük kod veri setleri üzerinde eğitilir ve yeni kod yazabilir veya mevcut koddaki hataları düzeltebilir.

![Metin ve kod üretimi](../../../translated_images/tr/Text.a8c0cf139e5cc2a0.webp)

### Encoder-Decoder ve Sadece Decoder

LLM'lerin farklı mimarileri hakkında konuşmak için bir benzetme yapalım.

Yöneticiniz size öğrenciler için bir quiz hazırlama görevi verdiğini hayal edin. İki iş arkadaşınız var; biri içeriğin oluşturulmasından, diğeri gözden geçirilmesinden sorumlu.

İçerik oluşturucu sadece bir decoder modeline benzer: konuyu görür, sizin yazdıklarınızı kontrol eder ve ardından o bağlama dayanarak içerik üretmeye devam eder. İlgi çekici ve bilgilendirici içerik yazmada çok iyidir, ancak görev sadece sınıflandırma, getirme veya bilgiyi kodlama ise her zaman en iyi tercih değildir. Decoder-only model ailesine örnekler GPT ve Llama modelleridir.

Gözden geçiren ise sadece bir Encoder modeline benzer; yazılan kursu ve cevapları inceler, aralarındaki ilişkiyi fark eder ve bağlamı anlar, ama içerik üretmede iyi değildir. Sadece Encoder modele örnek olarak BERT verilebilir.

Bir de hem oluşturup hem gözden geçirebilen biri olduğunu hayal edin; bu Encoder-Decoder modelidir. Örnek olarak BART ve T5 modelleri verilebilir.

### Servis ve Model Arasındaki Fark

Şimdi, bir servis ve bir model arasındaki farkı konuşalım. Servis, bir Bulut Servis Sağlayıcısı tarafından sunulan bir ürün olup, genellikle modeller, veriler ve diğer bileşenlerin birleşimidir. Model ise servisin temel bileşeni olup, genellikle bir foundation model, örneğin bir LLM'dir.

Servisler genellikle üretim kullanımı için optimize edilmiştir ve grafiksel kullanıcı arayüzü üzerinden modellerden daha kolay kullanılabilir. Ancak servisler her zaman ücretsiz değildir ve kullanım sahibinin ekipman ve kaynaklarını kullanmak karşılığında abonelik veya ödeme gerektirebilir; böylece maliyetlerin optimize edilmesi ve kolay ölçeklenme sağlanır. Örnek olarak, pay-as-you-go ücretlendirme planı sunan [Azure OpenAI Servisi](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst) verilebilir. Bu servis ayrıca modellerin yeteneklerinin üstünde kurumsal düzeyde güvenlik ve sorumlu yapay zeka çerçevesi sunar.

Modeller, sinir ağı öğeleri; parametreler, ağırlıklar, mimari, belirteçleyici ve destekleyici yapılandırmadan oluşur. Bir modeli yerel veya özel bir ortamda çalıştırmak uygun donanım, sunum altyapısı, izleme ile uyumlu açık kaynak/açık ağırlıklı lisans veya ticari lisans gerektirir. Llama 4 veya Mistral gibi açık ağırlıklı modeller kendi kendine barındırılabilir, ancak yine de hesaplama gücü ve operasyonel uzmanlık gerektirir.

## Azure'da Performansı Anlamak İçin Farklı Modellerle Nasıl Test Edilir ve İterasyon Yapılır


Ekibimiz mevcut LLM ortamını keşfedip senaryoları için iyi adayları belirledikten sonra, bir sonraki adım bunları verileri ve iş yükleri üzerinde test etmektir. Bu, deneyler ve ölçümlerle yapılan yinelemeli bir süreçtir.
Önceki paragraflarda bahsettiğimiz modellerin çoğu (OpenAI modelleri, Llama 4 ve Mistral gibi açık ağırlıklı modeller ve Hugging Face modelleri) [Microsoft Foundry Modelleri](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst) içinde kullanılabilir.

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), eskiden Azure AI Studio/Azure AI Foundry olarak bilinen, AI uygulamaları ve ajanları oluşturmak için birleşik bir Azure platformudur. Deneyimden değerlendirmeye, dağıtımdan izlemeye ve yönetişime kadar yaşam döngüsünü yönetmede geliştiricilere yardımcı olur. Microsoft Foundry’deki model kataloğu kullanıcıya:

- Katalogdaki ilgi duyulan temel modeli bulma şansı sunar; Azure tarafından satılan modeller ve ortaklar ile topluluk sağlayıcılarından modeller de dahildir. Kullanıcılar, görev, sağlayıcı, lisans, dağıtım seçeneği veya isim bazında filtreleme yapabilir.

![Model kataloğu](../../../translated_images/tr/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- Model kartını gözden geçirme olanağı sağlar; amaçlanan kullanım ve eğitim verileri detaylı açıklamalar, kod örnekleri ve dahili değerlendirme kütüphanesindeki sonuçlar yer alır.

![Model kartı](../../../translated_images/tr/ModelCard.598051692c6e400d.webp)

- İş senaryosunu karşılayan modeli belirlemek için sektördeki modeller ve veri setleri arasındaki kıyaslamaları [Model Kıyaslamaları](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst) paneli üzerinden yapma imkanı.

![Model kıyaslamaları](../../../translated_images/tr/ModelBenchmarks.254cb20fbd06c03a.webp)

- Desteklenen modelleri özel eğitim verileriyle ince ayar yaparak belirli bir iş yükündeki model performansını artırma ve Microsoft Foundry’nin deney ve takip yeteneklerinden faydalanma.

![Model ince ayarı](../../../translated_images/tr/FineTuning.aac48f07142e36fd.webp)

- Orijinal önceden eğitilmiş modeli veya ince ayar yapılmış sürümü, yönetilen hesaplama veya sunucusuz dağıtım seçenekleri kullanarak uzak gerçek zamanlı çıkarım uç noktasına dağıtarak uygulamanın bunu tüketmesini sağlama.

![Model dağıtımı](../../../translated_images/tr/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> Katalogdaki tüm modeller şu anda ince ayar yapmaya ve/veya kullandıkça öde dağıtımına açık değildir. Modelin yetenekleri ve kısıtlamaları hakkında detaylar için model kartını kontrol edin.

## LLM sonuçlarını geliştirme

Startup ekibimizle farklı türde LLM’leri ve farklı modelleri karşılaştırmamızı, test verileri üzerinde değerlendirmemizi, performansı artırmamızı ve çıkarım uç noktalarına dağıtım yapmamızı sağlayan bir bulut platformunu (Microsoft Foundry) inceledik.

Peki, önceden eğitilmiş bir modeli kullanmak yerine ne zaman ince ayar yapmayı düşünmeliler? Belirli iş yüklerinde model performansını artırmak için başka yaklaşımlar var mı?

Bir işletmenin LLM’den ihtiyaç duyduğu sonuçları elde etmek için kullanabileceği birkaç yaklaşım vardır. Üretimde LLM dağıtırken farklı eğitim derecelerine sahip farklı tür modeller seçebilirsiniz; bunlar farklı karmaşıklık, maliyet ve kalite seviyelerine sahiptir. İşte bazı farklı yaklaşımlar:

- **Bağlam ile istem geliştirme (Prompt engineering)**. Fikir, ihtiyacınız olan yanıtları almak için istem sırasında yeterli bağlam sağlamaktır.

- **Retrieval Augmented Generation, RAG**. Verileriniz örneğin bir veritabanı veya web uç noktasında olabilir; istem zamanında bu verinin veya bir alt kümesinin dahil edilmesini sağlamak için ilgili veriyi alıp kullanıcının istemine ekleyebilirsiniz.

- **İnce ayar yapılmış model**. Burada modeli kendi verilerinizle daha fazla eğitmiş olursunuz; bu, modelin ihtiyaçlarınıza daha kesin ve duyarlı olmasını sağlar ancak maliyetli olabilir.

![LLM dağıtımı](../../../translated_images/tr/Deploy.18b2d27412ec8c02.webp)

Resim kaynağı: [Dört Yolla İşletmeler LLM’leri Dağıtıyor | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Bağlamlı İstem Geliştirme

Önceden eğitilmiş LLM’ler, tamamlanacak kısa bir cümle veya soru gibi kısa bir istemle bile genel doğal dil görevlerinde çok iyi çalışır – buna “sıfır atış” (zero-shot) öğrenme denir.

Ancak kullanıcı, sorgusunu ayrıntılı istek ve örneklerle — yani Bağlam ile — şekillendirebildikçe, yanıt o kadar doğru ve kullanıcının beklentilerine yakın olur. Burada, istemde yalnızca bir örnek varsa “bir atış” (one-shot) öğrenmeden, birden fazla örnek varsa “birkaç atış” (few-shot) öğrenmeden bahsederiz.
Bağlam ile istem geliştirme, işe başlamak için en uygun maliyetli yaklaşımdır.

### Retrieval Augmented Generation (RAG)

LLM’lerin sınırlaması, yanıt oluşturmak için yalnızca eğitimlerinde kullanılan verileri kullanabilmeleridir. Bu, eğitim süreçlerinden sonra gerçekleşen gerçekler hakkında bir şey bilmedikleri ve halka açık olmayan (şirket içi) bilgilere erişemedikleri anlamına gelir.
Bu, istemi dış veri parçaları (belge parçaları) ile genişleten ve istem uzunluk sınırlarını dikkate alan RAG tekniğiyle aşılabilir. Bu, çeşitli önceden tanımlanmış veri kaynaklarından faydalı parçaları alan ve bunları istem bağlamına ekleyen [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst) gibi vektör veritabanı araçları tarafından desteklenir.

Bu teknik, bir işletmenin yeterli veri, zaman veya kaynağı olmadığı durumlarda LLM’yi ince ayar yapmak yerine belirli bir iş yükünde performansı artırmasını ve gerçek dışı, güncel olmayan veya desteklenmeyen yanıt risklerini azaltmasını sağlar.

### İnce ayar yapılmış model

İnce ayar, transfer öğrenimini kullanarak modeli belirli bir alt görev veya problemi çözmek için ‘uyarlayan’ bir süreçtir. Birkaç atış öğrenme ve RAG’den farklı olarak, yeni ağırlıklar ve önyargılarla yeni bir model oluşturur. Tek bir girdi (istem) ve buna bağlı çıktı (tamamlama) içeren eğitim örnekleri gerektirir.
Tercih edilen yaklaşım aşağıdaki durumlar için uygundur:

- **Daha küçük, görev özel modeller kullanmak**. Bir işletme, büyük bir öncü modeli tekrar tekrar istemek yerine daha dar bir görev için daha küçük bir modeli ince ayar yapmak isteyebilir, bu daha düşük maliyetli ve hızlı bir çözüm olur.

- **Gecikmeyi (latency) dikkate almak**. Belirli bir kullanım durumu için gecikme önemliyse, çok uzun istemler kullanmak veya öğrenilmesi gereken örnek sayısı istem uzunluk sınırı ile uymaz.

- **Kararlı davranışı uyarlamak**. Bir işletmenin çok sayıda yüksek kaliteli örneği varsa ve modelin tutarlı şekilde görev kalıbını, çıktı formatını, tonu veya alan spesifik stilini izlemesini isterse. Esas sorun sık değişen güncel gerçekler veya özel bilgi ise yalnızca ince ayara güvenmek yerine RAG kullanılmalıdır.

### Eğitilmiş model

Baştan sona bir LLM eğitmek şüphesiz benimsenmesi en zor ve karmaşık yaklaşımdır; büyük miktarda veri, uzman kaynaklar ve uygun hesaplama gücü gerektirir. Bu seçenek yalnızca bir işletmenin alan-spesifik bir kullanım durumu ve büyük miktarda alan odaklı verisi olduğu senaryoda düşünülmelidir.

## Bilgi Kontrolü

LLM tamamlama sonuçlarını geliştirmek için iyi bir yaklaşım ne olabilir?

1. Bağlam ile istem geliştirme
1. RAG
1. İnce ayar yapılmış model

C: Üçü de yardımcı olabilir. Hızlı iyileştirmeler için bağlam ile istem geliştirmeyle başlayın ve modelin güncel gerçeklere veya özel iş verilerine ihtiyacı varsa RAG kullanın. Yeterince yüksek kaliteli örnek olduğunda ve modelin tutarlı şekilde görev, format, ton veya alan kalıbını izlemesi gerektiğinde ince ayarı tercih edin.

## 🚀 Zorluk

İşiniz için [RAG kullanımını](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) daha detaylı okuyun.

## Harika İş, Öğrenmeye Devam Et

Bu dersi tamamladıktan sonra, Generatif AI bilginizi geliştirmeye devam etmek için [Generative AI Öğrenme koleksiyonumuzu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) inceleyin!

Sorumlu Generatif AI kullanımına nasıl [yapı kuracağımızı] (../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst) göreceğimiz 3. Derse gidin!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->