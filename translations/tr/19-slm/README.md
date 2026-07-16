# Yeni Başlayanlar için Üretken Yapay Zeka İçin Küçük Dil Modellerine Giriş
Üretken Yapay Zeka, yeni içerik oluşturabilen sistemler yaratmaya odaklanan büyüleyici bir yapay zeka alanıdır. Bu içerik metinden ve görüntülerden müziğe ve hatta tüm sanal ortamlara kadar uzanabilir. Üretken yapay zekanın en heyecan verici uygulamalarından biri dil modelleri alanındadır.

## Küçük Dil Modelleri Nedir?

Küçük Dil Modeli (KDM), büyük dil modeli (BDM) mimari ilkeleri ve tekniklerinden çoğunu kullanan, ancak önemli ölçüde azaltılmış bir hesaplama ayakizine sahip ölçeklendirilmiş bir BDM varyantıdır.

KDM’ler, insan benzeri metinler üretmek için tasarlanmış dil modellerinin bir alt kümesidir. GPT-4 gibi daha büyük muadillerinin aksine, KDM’ler daha kompakt ve verimlidir, bu da onları hesaplama kaynaklarının sınırlı olduğu uygulamalar için ideal kılar. Daha küçük boyutlarına rağmen çeşitli görevleri yerine getirebilirler. Tipik olarak, KDM’ler, orijinal modelin işlevselliği ve dilsel yeteneklerinin önemli bir kısmını korumayı hedefleyerek BDM’lerin sıkıştırılması veya distilasyonu ile oluşturulur. Model boyutundaki bu küçülme, genel karmaşıklığı azaltır ve KDM’leri hem hafıza kullanımı hem de hesaplama gereksinimleri açısından daha verimli hale getirir. Bu optimizasyonlara rağmen, KDM’ler hala çok çeşitli doğal dil işleme (NLP) görevlerini gerçekleştirebilir:

- Metin Üretimi: Tutarlı ve bağlamsal olarak ilgili cümleler veya paragraflar oluşturma.
- Metin Tamamlama: Verilen bir isteme dayanarak cümleleri tahmin etme ve tamamlama.
- Çeviri: Metni bir dilden diğerine çevirme.
- Özetleme: Uzun metin parçalarını daha kısa, daha sindirilebilir özetlere dönüştürme.

Daha büyük muadilleriyle kıyaslandığında performans veya anlama derinliği açısından bazı ödünler verilmiştir.

## Küçük Dil Modelleri Nasıl Çalışır?
KDM’ler çok büyük miktarda metin verisi üzerinde eğitilir. Eğitim sırasında dilin kalıplarını ve yapısını öğrenerek hem dilbilgisel olarak doğru hem de bağlama uygun metinler üretmelerini sağlarlar. Eğitim süreci şunları içerir:

- Veri Toplama: Çeşitli kaynaklardan büyük metin veri setlerini toplama.
- Ön İşleme: Verileri temizleme ve eğitime uygun hale getirme.
- Eğitim: Modeli metni anlama ve üretme konusunda öğretmek için makine öğrenimi algoritmalarını kullanma.
- İnce Ayar: Belirli görevlerde performansı artırmak için modeli ayarlama.

KDM geliştirme, mobil cihazlar veya kenar bilişim platformları gibi kaynak kısıtlı ortamlarda kullanılabilen modeller ihtiyacının artmasıyla paralellik gösterir; çünkü tam ölçekli BDM’ler ağır kaynak gereksinimleri nedeniyle pratik olmayabilir. Verimliliğe odaklanarak KDM’ler, performans ve erişilebilirlik arasında denge kurar ve çeşitli alanlarda daha geniş uygulamalara olanak tanır.

![slm](../../../translated_images/tr/slm.4058842744d0444a.webp)

## Öğrenme Hedefleri

Bu derste, KDM bilgisini tanıtmayı ve bunu Microsoft Phi-3 ile birleştirerek metin içeriği, görme ve MoE’de farklı senaryoları öğrenmeyi amaçlıyoruz.

Dersin sonunda aşağıdaki soruları cevaplayabilecek durumda olmalısınız:

- KDM nedir?
- KDM ile BDM arasındaki fark nedir?
- Microsoft Phi-3/3.5 Ailesi nedir?
- Microsoft Phi-3/3.5 Ailesi ile nasıl çıkarım yapılır?

Hazır mısınız? Başlayalım.

## Büyük Dil Modelleri (BDM) ile Küçük Dil Modelleri (KDM) Arasındaki Farklar

Hem BDM’ler hem de KDM’ler, mimari tasarım, eğitim metodolojileri, veri üretim süreçleri ve model değerlendirme tekniklerinde benzer yaklaşımları izleyen olasılıksal makine öğrenimi ilkelerine dayanmaktadır. Ancak bu iki model türünü birbirinden ayıran birkaç temel faktör vardır.

## Küçük Dil Modellerinin Uygulamaları

KDM’ler geniş bir uygulama yelpazesine sahiptir, bunlar arasında:

- Sohbet Robotları: Müşteri desteği sağlama ve kullanıcılarla sohbet şeklinde etkileşime geçme.
- İçerik Oluşturma: Yazarları fikir üretme veya hatta tam makaleler taslaklama konusunda destekleme.
- Eğitim: Öğrencilere yazı ödevlerinde veya yeni diller öğrenmede yardımcı olma.
- Erişilebilirlik: Metinden sese sistemleri gibi engelli bireyler için araçlar oluşturma.

**Boyut**
  
BDM’ler ve KDM’ler arasındaki temel ayrım modellerin ölçeğindedir. ChatGPT (GPT-4) gibi BDM’ler yaklaşık 1.76 trilyon parametre içerebilirken, Mistral 7B gibi açık kaynak KDM’ler çok daha az parametreyle tasarlanmıştır — yaklaşık 7 milyar. Bu fark esas olarak model mimarisi ve eğitim süreçlerindeki farklılıklardan kaynaklanır. Örneğin, ChatGPT, bir kodlayıcı-çözücü yapısında kendi kendine dikkat mekanizması kullanırken, Mistral 7B sadece çözücü model içinde daha verimli eğitim sağlayan kayan pencere dikkat mekanizması kullanır. Bu mimari fark, modellerin karmaşıklığı ve performansı üzerinde derin etkiler yaratır.

**Anlama**

KDM’ler genellikle belirli alanlardaki performans için optimize edilmiştir, bu da onları oldukça uzmanlaştırılmış ancak çoklu bilgi alanlarında geniş kapsamlı bağlam anlayışı sağlama yeteneklerinde sınırlı yapar. Buna karşılık BDM’ler insan benzeri zekâyı daha kapsamlı düzeyde simüle etmeye çalışır. Büyük ve çeşitli veri setleri üzerinde eğitilen BDM’ler farklı alanlarda iyi performans gösterecek şekilde tasarlanmıştır, böylece daha fazla esneklik ve uyarlanabilirlik sunarlar. Bu nedenle, BDM’ler doğal dil işleme ve programlama gibi daha geniş yelpazedeki görevler için daha uygundur.

**Hesaplama**

BDM’lerin eğitimi ve dağıtımı kaynak gerektiren süreçlerdir ve genellikle büyük ölçekli GPU kümeleri gibi önemli hesaplama altyapıları gerektirir. Örneğin, ChatGPT gibi bir modeli sıfırdan eğitmek, binlerce GPU’nun uzun süreler boyunca kullanılması anlamına gelebilir. Buna karşılık KDM’ler daha küçük parametre sayılarına sahip olduklarından hesaplama kaynakları açısından daha erişilebilirdir. Mistral 7B gibi modeller, orta düzey GPU özelliklerine sahip yerel makinelerde eğitilip çalıştırılabilir, ancak eğitim yine de çoklu GPU’larda birkaç saat gerektirir.

**Önyargı**

Önyargı, BDM’lerde bilinen bir sorundur ve esas olarak eğitim verilerinin doğası nedeniyle ortaya çıkar. Bu modeller genellikle internetten açıkça erişilebilir ham verilere dayanır, bu veriler bazı grupları az temsil edebilir veya yanlış temsil edebilir, hatalı etiketlendirmeler içerebilir veya lehçe, coğrafi farklılıklar ve dilbilgisi kurallarının etkilediği dilsel önyargılar yansıtabilir. Ayrıca, BDM mimarilerinin karmaşıklığı, dikkatli ince ayar yapılmadığında önyargıyı istemeden artırabilir. Öte yandan, daha sınırlı, alan-spesifik veri setlerinde eğitilen KDM’ler bu tür önyargılara daha az maruz kalır, ancak tamamen bağışık değildir.

**Çıkarım**

KDM’lerin küçültülmüş boyutu onlara çıkarım hızı açısından önemli bir avantaj sağlar, böylece yerel donanım üzerinde verimli şekilde çıktı üretebilirler ve geniş çaplı paralel işlemeye ihtiyaç duymazlar. Buna karşılık BDM’ler, boyutları ve karmaşıklıkları nedeniyle kabul edilebilir çıkarım süreleri için genellikle önemli paralel hesaplama kaynaklarına gereksinim duyar. Çoklu eşzamanlı kullanıcıların varlığı, özellikle büyük çapta dağıtıldığında BDM’lerin yanıt sürelerini daha da yavaşlatır.

Özetle, hem BDM’ler hem de KDM’ler makine öğreniminde ortak bir temele sahip olmakla birlikte, model boyutu, kaynak gereksinimleri, bağlamsal anlama, önyargıya yatkınlık ve çıkarım hızı bakımından önemli farklılıklar gösterirler. Bu farklılıklar, BDM’lerin daha esnek ancak kaynak tüketimi yüksek, KDM’lerin ise daha alan-spesifik verimli ve daha düşük hesaplama talebiyle farklı kullanım durumlarına uygunluğunu yansıtır.

***Not: Bu derste, Microsoft Phi-3 / 3.5 örneği kullanılarak KDM tanıtılacaktır.***

## Phi-3 / Phi-3.5 Ailesini Tanıtmak

Phi-3 / 3.5 Ailesi esas olarak metin, görme ve Ajan (MoE) uygulama senaryolarına odaklanır:

### Phi-3 / 3.5 Instruct

Esas olarak metin üretimi, sohbet tamamlama ve içerik bilgi çıkarımı gibi görevler için.

**Phi-3-mini**

3.8 milyar parametreli bu dil modeli Microsoft Foundry, Hugging Face ve Ollama platformlarında mevcuttur. Phi-3 modelleri, eşit veya daha büyük boyuttaki dil modellerini önemli ölçüde geride bırakır (aşağıdaki benchmark sayıları daha yüksek olan daha iyidir). Phi-3-mini, kendi boyutunun iki katı büyüklüğündeki modelleri geride bırakırken, Phi-3-small ve Phi-3-medium daha büyük modelleri, hatta GPT-3.5’i geçer.

**Phi-3-small & medium**

Sadece 7 milyar parametre ile Phi-3-small, birçok dil, muhakeme, kodlama ve matematik benchmark’ında GPT-3.5T’yi yeniyor.

14 milyar parametreli Phi-3-medium bu eğilimi sürdürerek Gemini 1.0 Pro’yu geçiyor.

**Phi-3.5-mini**

Phi-3-mini’nin bir yükseltmesi olarak düşünülebilir. Parametre sayısı değişmemiş olmasına rağmen, çoklu dili destekleme yeteneğini geliştirir (20+ dili destekler: Arapça, Çince, Çekçe, Danca, Hollandaca, İngilizce, Fince, Fransızca, Almanca, İbranice, Macarca, İtalyanca, Japonca, Korece, Norveççe, Lehçe, Portekizce, Rusça, İspanyolca, İsveççe, Tayca, Türkçe, Ukraynaca) ve uzun bağlam desteğini güçlendirir.

3.8 milyar parametreli Phi-3.5-mini, aynı boyuttaki dil modellerini geride bırakır ve kendi boyutunun iki katı olan modellerle başa baştır.

### Phi-3 / 3.5 Vision

Phi-3/3.5 Instruct modelini Phi’nin anlama yeteneği olarak düşünebiliriz ve Vision ise Phi’ye dünyayı anlama gözleri verir.


**Phi-3-Vision**

Sadece 4.2 milyar parametreye sahip Phi-3-vision, genel görsel muhakeme görevlerinde, OCR, tablo ve diyagram anlama görevlerinde Claude-3 Haiku ve Gemini 1.0 Pro V gibi daha büyük modelleri geride bırakmaya devam eder.


**Phi-3.5-Vision**

Phi-3.5-Vision, Phi-3-Vision’ın bir yükseltmesidir; birden fazla görüntüyü destekler. Görme alanında bir iyileştirme olarak düşünebilirsiniz; sadece resimleri değil, videoları da görebilir.

Phi-3.5-vision, OCR, tablo ve grafik anlama görevlerinde Claude-3.5 Sonnet ve Gemini 1.5 Flash gibi daha büyük modelleri geride bırakır; genel görsel bilgi muhakemesi görevlerinde ise denk performans gösterir. Çoklu kare girişini destekler, yani çoklu giriş görüntüleri üzerinde muhakeme yapabilir.


### Phi-3.5-MoE

***Mixture of Experts (MoE)***, modellerin çok daha az hesaplamayla önceden eğitilmesini mümkün kılar, bu da aynı hesaplama bütçesi ile model veya veri seti boyutunun dramatik şekilde artırılabileceği anlamına gelir. Özellikle, bir MoE modeli, ön eğitim sırasında yoğun model muadiline kıyasla aynı kaliteyi çok daha hızlı elde etmelidir.

Phi-3.5-MoE, 16x3.8 milyar parametreli uzman modüllerden oluşur. Sadece 6.6 milyar aktif parametreye sahip Phi-3.5-MoE, çok daha büyük modellerle benzer seviyede muhakeme, dil anlama ve matematik başarısına ulaşır.

Phi-3/3.5 Ailesi modelini farklı senaryolara göre kullanabiliriz. BDM’nin aksine, Phi-3/3.5-mini veya Phi-3/3.5-Vision’ı kenar cihazlarında dağıtabilirsiniz.


## Phi-3/3.5 Aile Modellerinin Kullanımı

Phi-3/3.5’i farklı senaryolarda kullanmayı umuyoruz. Sonraki adımda, farklı senaryolara göre Phi-3/3.5 kullanacağız.

![phi3](../../../translated_images/tr/phi3.655208c3186ae381.webp)

### Bulut API’leri Üzerinden Çıkarım

**Microsoft Foundry Modelleri**

> **Not:** GitHub Modelleri Temmuz 2026 sonunda kullanımdan kaldırılacak. [Microsoft Foundry Modelleri](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) doğrudan yerini alacaktır.

Microsoft Foundry Modelleri en doğrudan yoldur. Phi-3/3.5-Instruct modeline Foundry model kataloğu aracılığıyla hızlıca erişebilirsiniz. Azure AI Inference SDK / OpenAI SDK ile API çağrısını kod yoluyla tamamlayabilirsiniz. Ayrıca farklı etkileri Playground üzerinden test edebilirsiniz.

- Demo: Çin senaryolarında Phi-3-mini ve Phi-3.5-mini etkilerinin karşılaştırması

![phi3](../../../translated_images/tr/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/tr/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Ya da görme ve MoE modellerini kullanmak istersek, Microsoft Foundry ile çağrıyı gerçekleştirebilirsiniz. İlgileniyorsanız, Phi-3 Cookbook’u okuyarak Microsoft Foundry üzerinden Phi-3/3.5 Instruct, Vision, MoE’nin nasıl çağrılacağını öğrenebilirsiniz [Bu bağlantıya tıklayın](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Bulut tabanlı Microsoft Foundry Modelleri kataloğunun yanı sıra, ilgili çağrıları tamamlamak için [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) kullanabilirsiniz. NVIDIA NIM (NVIDIA Inference Microservices), geliştiricilerin bulutlar, veri merkezleri ve iş istasyonları dahil olmak üzere çeşitli ortamlarda AI modellerini verimli şekilde dağıtmalarına yardımcı olmak üzere tasarlanmış hızlandırılmış çıkarım mikro servisleri setidir.

İşte NVIDIA NIM’in bazı önemli özellikleri:

- **Kolay Dağıtım:** NIM, AI modellerinin tek bir komutla dağıtımını mümkün kılarak mevcut iş akışlarına entegrasyonu basitleştirir.

- **Optimize Edilmiş Performans:** Düşük gecikme ve yüksek verimlilik sağlamak için TensorRT ve TensorRT-LLM gibi NVIDIA’nın önceden optimize edilmiş çıkarım motorlarını kullanır.
- **Ölçeklenebilirlik:** NIM, Kubernetes üzerinde otomatik ölçeklendirmeyi destekleyerek değişken iş yüklerini etkili bir şekilde yönetmesini sağlar.
- **Güvenlik ve Kontrol:** Kuruluşlar, NIM mikroservislerini kendi yönetilen altyapılarında barındırarak veri ve uygulamaları üzerinde kontrol sahibi olabilirler.
- **Standart API’ler:** NIM, chatbotlar, AI asistanları ve daha fazlası gibi AI uygulamalarını kolayca oluşturmak ve entegre etmek için endüstri standardı API’ler sunar.

NIM, NVIDIA AI Enterprise’ın bir parçasıdır ve AI modellerinin dağıtımını ve operasyonelleştirilmesini basitleştirerek NVIDIA GPU’larında verimli çalışmasını sağlar.

- Demo: NVIDIA NIM kullanarak Phi-3.5-Vision-API çağırma [[Bu bağlantıya tıklayın](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5’ü Yerelde Çalıştırmak
Phi-3 veya GPT-3 gibi herhangi bir dil modeline ilişkin çıkarım (inference), aldığı girdiye dayanarak yanıtlar veya tahminler oluşturma sürecine denir. Phi-3’e bir soru veya komut verdiğinizde, eğitildiği verideki desenleri ve ilişkileri analiz ederek en olası ve ilgili yanıtı oluşturmak için eğitilmiş sinir ağını kullanır.

**Hugging Face Transformer**
Hugging Face Transformers, doğal dil işleme (NLP) ve diğer makine öğrenimi görevleri için tasarlanmış güçlü bir kütüphanedir. İşte bu kütüphane hakkında bazı önemli noktalar:

1. **Önceden Eğitilmiş Modeller:** Metin sınıflandırma, adlandırılmış varlık tanıma, soru yanıtlama, özetleme, çeviri ve metin üretimi gibi çeşitli görevler için kullanılabilecek binlerce önceden eğitilmiş model sunar.

2. **Çerçeve Uyumluluğu:** Kütüphane, PyTorch, TensorFlow ve JAX gibi birçok derin öğrenme çerçevesini destekler. Bu sayede bir modeli bir çerçevede eğitip diğerinde kullanabilirsiniz.

3. **Multimodal Yetkinlikler:** NLP’nin yanı sıra, Hugging Face Transformers bilgisayarlı görme (örneğin, görüntü sınıflandırma, nesne algılama) ve ses işleme (örneğin, konuşma tanıma, ses sınıflandırma) görevlerini de destekler.

4. **Kullanım Kolaylığı:** Kütüphane, modelleri kolayca indirip ince ayar yapmanızı sağlayan API’ler ve araçlar sunar; hem yeni başlayanlar hem de uzmanlar için erişilebilirdir.

5. **Topluluk ve Kaynaklar:** Hugging Face zengin bir topluluğa ve kapsamlı dökümantasyon, eğitim ve rehberlere sahiptir; kullanıcıların başlamasına ve kütüphaneden en iyi şekilde faydalanmasına yardımcı olur.
[resmi dökümantasyon](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) veya onların [GitHub deposu](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Bu en yaygın kullanılan yöntemdir ancak GPU hızlandırması gerektirir. Sonuçta Vision ve MoE gibi senaryolar çok fazla hesaplama gerektirir ve bunlar quantize edilmemişse CPU’da çok yavaş çalışacaktır.


- Demo: Transformer kullanarak Phi-3.5-Instruct çağırma [Bu bağlantıya tıklayın](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformer kullanarak Phi-3.5-Vision çağırma [Bu bağlantıya tıklayın](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformer kullanarak Phi-3.5-MoE çağırma [Bu bağlantıya tıklayın](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), büyük dil modellerini (LLM’ler) yerelde, kendi makinenizde çalıştırmayı kolaylaştırmak için tasarlanmış bir platformdur. Llama 3.1, Phi 3, Mistral ve Gemma 2 gibi çeşitli modelleri destekler. Platform, model ağırlıkları, yapılandırma ve veriyi tek bir paket halinde sunarak kullanıcıların kendi modellerini özelleştirmesini ve oluşturmasını daha erişilebilir hale getirir. Ollama macOS, Linux ve Windows için mevcuttur. Bulut servislerine bağlı kalmadan LLM’lerle denemeler yapmak veya dağıtmak isteyenler için harika bir araçtır. Ollama en doğrudan yoldur, sadece aşağıdaki komutu çalıştırmanız yeterlidir.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst), Microsoft’un çevrimdışı, cihaz üzerinde çalışan bir çalışma zamanı ortamıdır; Phi gibi modelleri tamamen kendi donanımınızda çalıştırmanızı sağlar - Azure aboneliği, API anahtarı veya ağ bağlantısı gerekmez. Mevcut en iyi yürütme sağlayıcısını (NPU, GPU veya CPU) otomatik olarak seçer ve OpenAI uyumlu bir uç nokta sunar, böylece mevcut `openai` / Azure AI Inference SDK kodları minimum değişiklikle bu uç noktayı kullanabilir. Başlamak için [Foundry Local dökümantasyonunu](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) inceleyin.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Veya SDK’yı doğrudan Python’da kullanabilirsiniz:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime for GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst), çapraz platform çıkarım ve eğitim için bir makine öğrenimi hızlandırıcıdır. ONNX Runtime for Generative AI (GENAI), üretken AI modellerini çeşitli platformlarda verimli çalıştırmanıza yardımcı olan güçlü bir araçtır.

## ONNX Runtime Nedir?
ONNX Runtime, makine öğrenimi modellerinin yüksek performanslı çıkarımını sağlayan açık kaynaklı bir projedir. Open Neural Network Exchange (ONNX) formatındaki modelleri destekler; bu, makine öğrenimi modellerini temsil etmek için standart bir formattır. ONNX Runtime çıkarımı, PyTorch ve TensorFlow/Keras gibi derin öğrenme çerçevelerinden ve scikit-learn, LightGBM, XGBoost gibi klasik makine öğrenimi kütüphanelerinden modelleri destekleyerek daha hızlı müşteri deneyimleri ve daha düşük maliyetler sağlar. Farklı donanımlar, sürücüler ve işletim sistemleri ile uyumludur ve grafik optimizasyonları ve dönüşümlerinin yanında donanım hızlandırıcılarından yararlanarak optimum performans sunar.

## Üretken AI Nedir?
Üretken AI, üzerinde eğitildiği verilere dayanarak yeni içerikler (metin, görsel, müzik gibi) oluşturabilen AI sistemlerini ifade eder. Örnekler arasında GPT-3 gibi dil modelleri ve Stable Diffusion gibi görsel üretim modelleri bulunur. ONNX Runtime for GenAI kütüphanesi, ONNX modeller için üretken AI döngüsünü sağlar; buna ONNX Runtime ile çıkarım, logit işleme, arama ve örnekleme ile KV önbellek yönetimi dahildir.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI, ONNX Runtime’ın yeteneklerini üretken AI modellerini destekleyecek şekilde genişletir. Bazı önemli özellikleri şunlardır:

- **Geniş Platform Desteği:** Windows, Linux, macOS, Android ve iOS dahil olmak üzere çeşitli platformlarda çalışır.
- **Model Desteği:** LLaMA, GPT-Neo, BLOOM ve daha birçok popüler üretken AI modelini destekler.
- **Performans Optimizasyonu:** NVIDIA GPU’lar, AMD GPU’lar ve daha fazlası gibi farklı donanım hızlandırıcıları için optimizasyonlar içerir.
- **Kullanım Kolaylığı:** Uygulamalara kolay entegrasyon için API’ler sunar; minimum kod ile metin, görsel ve diğer içeriklerin üretimini sağlar.
- Kullanıcılar yüksek seviyede generate() metodunu çağırabilir veya modeli döngü içinde çalıştırıp her seferinde bir token üretebilir ve döngü içinde üretim parametrelerini güncelleyebilir.
- ONNX runtime ayrıca greedy/beam search ve TopP, TopK örnekleme desteği ile token dizileri üretmeyi ve tekrarlama cezaları gibi gömülü logit işleme özelliklerini destekler. Ayrıca özel skorlamalar kolaylıkla eklenebilir.

## Başlangıç
ONNX Runtime for GENAI ile başlamak için şu adımları izleyebilirsiniz:

### ONNX Runtime Kurulumu:
```Python
pip install onnxruntime
```
### Üretken AI Eklentilerini Kurun:
```Python
pip install onnxruntime-genai
```

### Bir Model Çalıştırın: İşte Python’da basit bir örnek:
```Python
import onnxruntime_genai as og

model = og.Model('path_to_your_model.onnx')

tokenizer = og.Tokenizer(model)

input_text = "Hello, how are you?"

input_tokens = tokenizer.encode(input_text)

output_tokens = model.generate(input_tokens)

output_text = tokenizer.decode(output_tokens)

print(output_text) 
```
### Demo: ONNX Runtime GenAI kullanarak Phi-3.5-Vision çağrısı


```python

import onnxruntime_genai as og

model_path = './Your Phi-3.5-vision-instruct ONNX Path'

img_path = './Your Image Path'

model = og.Model(model_path)

processor = model.create_multimodal_processor()

tokenizer_stream = processor.create_stream()

text = "Your Prompt"

prompt = "<|user|>\n"

prompt += "<|image_1|>\n"

prompt += f"{text}<|end|>\n"

prompt += "<|assistant|>\n"

image = og.Images.open(img_path)

inputs = processor(prompt, images=image)

params = og.GeneratorParams(model)

params.set_inputs(inputs)

params.set_search_options(max_length=3072)

generator = og.Generator(model, params)

while not generator.is_done():

    generator.compute_logits()
    
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    
    output = tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


**Diğerleri**

ONNX Runtime, Ollama ve Foundry Local referans yöntemlerine ek olarak, farklı üreticilerin sağladığı model referans yöntemlerine dayalı kantitatif modellerin referanslarını da tamamlayabiliriz. Örneğin Apple Metal ile Apple MLX çerçevesi, Qualcomm QNN ile NPU, Intel OpenVINO ile CPU/GPU vb. Daha fazla içeriği [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst) adresinden edinebilirsiniz.


## Daha Fazlası

Phi-3/3.5 Ailesinin temellerini öğrendik, ancak SLM hakkında daha fazla bilgi edinmek için daha fazla bilgiye ihtiyacımız var. Cevapları Phi-3 Cookbook’ta bulabilirsiniz. Daha fazlasını öğrenmek istiyorsanız, lütfen [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst) ziyaret edin.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->