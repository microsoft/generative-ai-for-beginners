# Yeni Başlayanlar için Üretken Yapay Zeka için Küçük Dil Modellerine Giriş
Üretken Yapay Zeka, yeni içerik oluşturabilen sistemler yaratmaya odaklanan büyüleyici bir yapay zeka alanıdır. Bu içerik metin, görüntü, müzik ve hatta tamamen sanal ortamlar olabilir. Üretken yapay zekanın en heyecan verici uygulamalarından biri dil modelleri alanındadır.

## Küçük Dil Modelleri Nedir?

Küçük Dil Modeli (SLM), büyük dil modellerinin (LLM) birçok mimari prensibini ve tekniğini kullanan, ancak hesaplama ayak izi önemli ölçüde azaltılmış ölçeklendirilmiş bir çeşididir.

SLM'ler, insan benzeri metin oluşturmak için tasarlanmış dil modeli alt kümesidir. GPT-4 gibi büyük modellerin aksine, SLM'ler daha kompakt ve verimlidir, bu da sınırlı hesaplama kaynaklarının olduğu uygulamalar için idealdir. Küçük boyutlarına rağmen çeşitli görevleri yerine getirebilirler. Genellikle, SLM'ler LLM'lerin sıkıştırılması veya damıtılmasıyla oluşturulur ve orijinal modelin işlevselliğinin ve dilsel yeteneklerinin büyük bir kısmını korumayı hedefler. Model boyutundaki bu küçülme, bellek kullanımı ve hesaplama gereksinimleri açısından SLM'leri daha verimli kılar. Bu optimizasyonlara rağmen, SLM'ler doğal dil işleme (NLP) görevlerinin geniş bir yelpazesini yapabilir:

- Metin Oluşturma: Tutarlı ve bağlama uygun cümleler veya paragraflar yaratmak.
- Metin Tamamlama: Verilen bir ipucuya dayanarak cümleleri tahmin edip tamamlamak.
- Çeviri: Metni bir dilden başka bir dile çevirmek.
- Özetleme: Uzun metin parçalarını daha kısa, sindirilebilir özetlere indirgemek.

Bazı performans veya anlayış derinliği açısından büyük modellerine göre bazı dezavantajlar olsa da.

## Küçük Dil Modelleri Nasıl Çalışır?
SLM'ler çok miktarda metin verisi üzerinde eğitilir. Eğitim sırasında dilin kalıplarını ve yapılarını öğrenirler, böylece hem dilbilgisel olarak doğru hem de bağlama uygun metin üretebilirler. Eğitim süreci şunları içerir:

- Veri Toplama: Çeşitli kaynaklardan büyük metin veri setleri toplamak.
- Ön İşleme: Veriyi temizleyip düzenleyerek eğitime uygun hale getirmek.
- Eğitim: Modeli metni anlayıp oluşturmayı öğrenmesi için makine öğrenimi algoritmalarıyla eğitmek.
- İnce Ayar: Modelin belirli görevlerdeki performansını iyileştirmek için ayarlamalar yapmak.

SLM'lerin geliştirilmesi, tam ölçekli LLM'lerin ağır kaynak gereksinimleri nedeniyle pratik olmadığı mobil cihazlar veya uç bilişim platformları gibi kaynak kısıtlı ortamlarda dağıtılabilen modellere olan artan ihtiyaca uygundur. Verimlilik odaklı yaklaşımlarıyla SLM'ler, performans ve erişilebilirlik arasında denge kurar, böylece çeşitli alanlarda daha geniş uygulama imkanı sunar.

![slm](../../../translated_images/tr/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Öğrenme Hedefleri

Bu derste, SLM bilgisi tanıtılacak ve Microsoft Phi-3 ile birleştirilerek metin içeriği, görsel ve MoE alanındaki farklı senaryolar öğretilecektir.

Ders sonunda aşağıdaki sorulara cevap verebilmeniz hedeflenmektedir:

- SLM nedir?
- SLM ile LLM arasındaki fark nedir?
- Microsoft Phi-3/3.5 ailesi nedir?
- Microsoft Phi-3/3.5 ailesiyle çıkarım (inference) nasıl yapılır?

Hazır mısınız? Başlayalım.

## Büyük Dil Modelleri (LLM'ler) ve Küçük Dil Modelleri (SLM'ler) Arasındaki Farklar

Hem LLM'ler hem de SLM'ler olasılıksal makine öğrenimi temelleri üzerine inşa edilmiştir, mimari tasarım, eğitim yöntemleri, veri oluşturma süreçleri ve model değerlendirme tekniklerinde benzer yaklaşımlar takip ederler. Ancak bu iki model türünü ayıran bazı temel faktörler vardır.

## Küçük Dil Modellerinin Uygulamaları

SLM'lerin çok çeşitli uygulamaları vardır, bunlar arasında:

- Sohbet Botları: Müşteri desteği sağlama ve kullanıcılarla konuşma yoluyla etkileşim.
- İçerik Oluşturma: Yazarların fikir üretmesine veya makaleler taslaklamasına yardımcı olmak.
- Eğitim: Öğrencilere yazı ödevlerinde veya yeni diller öğrenmede yardım etmek.
- Erişilebilirlik: Metni sese dönüştürme sistemleri gibi engelli bireyler için araçlar oluşturmak.

**Boyut**
  
LLM'ler ile SLM'ler arasındaki temel farklardan biri model ölçeğindedir. ChatGPT (GPT-4) gibi LLM'ler tahmini olarak 1,76 trilyon parametre içerirken, açık kaynak SLM'ler örneğin Mistral 7B önemli ölçüde daha az parametre içerir—yaklaşık 7 milyar parametre. Bu fark, model mimarisi ve eğitim süreçlerindeki farklılıklardan kaynaklanmaktadır. Örneğin, ChatGPT kod çözücü-şifreleyici çerçevesinde kendi kendine dikkat mekanizması kullanırken, Mistral 7B kaydırmalı pencere dikkat mekanizması kullanır ve bu da sadece kod çözücü modeli içinde daha verimli eğitime olanak tanır. Bu mimari fark, modellerin karmaşıklığı ve performansı üzerinde derin etkiler yaratır.

**Anlama**

SLM'ler genellikle belirli alanlardaki performans için optimize edilir, bu nedenle oldukça uzmanlaşmış ancak çok sayıda bilgi alanında geniş bağlamsal anlayış sağlamada sınırlı olabilirler. Buna karşın, LLM'ler daha kapsamlı düzeyde insan benzeri zekayı simüle etmeyi hedefler. Çok çeşitli ve büyük veri setleriyle eğitilen LLM'ler, birçok alanda iyi performans göstererek daha fazla çok yönlülük ve uyarlanabilirlik sunar. Sonuç olarak, LLM'ler doğal dil işleme ve programlama gibi daha geniş yelpazede görevler için daha uygundur.

**Hesaplama**

LLM'lerin eğitimi ve dağıtımı büyük ölçekli GPU kümeleri gibi önemli hesaplama altyapısı gerektiren kaynak yoğun süreçlerdir. Örneğin, ChatGPT gibi bir modeli sıfırdan eğitmek uzun süreler boyunca binlerce GPU gerektirebilir. Buna karşın, daha küçük parametre sayılarına sahip olan SLM'ler, hesaplama kaynakları açısından daha erişilebilirdir. Mistral 7B gibi modeller, orta düzeyde GPU özelliklerine sahip yerel makinelerde eğitilebilir ve çalıştırılabilir, ancak eğitim yine de birkaç GPU üzerinde saatler alır.

**Önyargı**

Önyargı, LLM'lerde bilinen bir sorundur ve çoğunlukla eğitim verilerinin doğasından kaynaklanır. Bu modeller genellikle internetten toplanan ham, açık veriye dayanır; bu da belirli grupların eksik temsil edilmesi, hatalı etiketlenme veya lehçe, coğrafi varyasyonlar ve dilbilgisi kurallarından etkilenmiş dilsel önyargılar içerebilir. Ayrıca, LLM mimarilerinin karmaşıklığı önyargıyı istemeden artırabilir ve bu da dikkatli ince ayar olmadan fark edilmeyebilir. Öte yandan, SLM'ler daha sınırlı, alan spesifik veri setleriyle eğitildikleri için bu tür önyargılara daha az maruz kalır, ancak tamamen bağışıksız değillerdir.

**Çıkarım (Inference)**

Küçük modellerin boyutunun azalması, yerel donanımda geniş paralel işlem gerektirmeden hızlı çıktı üretmelerine olanak tanır ve onlara çıkarım hızı açısından önemli bir avantaj sağlar. Aksine, LLM'ler büyüklükleri ve karmaşıklıkları nedeniyle kabul edilebilir çıkarım süreleri için genellikle büyük paralel hesaplama kaynaklarına ihtiyaç duyar. Çoklu eşzamanlı kullanıcı varlığı da ölçeklenmiş kullanımda LLM'lerin yanıt sürelerini yavaşlatır.

Özetle, LLM'ler ve SLM'ler makine öğrenimi temelinde ortak yapılsa da, model boyutu, kaynak gereksinimleri, bağlamsal anlama, önyargı duyarlılığı ve çıkarım hızı bakımından ciddi farklılıklar gösterirler. Bu ayrımlar, bu modellerin kullanım alanlarının uygunluğunu şekillendirir; LLM'ler daha çok yönlü ancak kaynak yoğun iken, SLM'ler daha dar alanda verimli ve daha az hesaplama gerektiren çözümler sunar.

***Not: Bu derste, örnek olarak Microsoft Phi-3 / 3.5 kullanılarak SLM tanıtılacaktır.***

## Phi-3 / Phi-3.5 Ailesi Tanıtımı

Phi-3 / 3.5 ailesi ağırlıklı olarak metin, görsel ve Ajan (MoE) uygulama senaryolarını hedefler:

### Phi-3 / 3.5 Instruct

Özellikle metin oluşturma, sohbet tamamlama ve içerik bilgi çıkarımı vb. için.

**Phi-3-mini**

3.8B parametreli dil modeli Microsoft Foundry, Hugging Face ve Ollama üzerinde mevcuttur. Phi-3 modelleri, önemli kıyaslamalarda (aşağıdaki kıyaslama sayıları, yüksek değerler daha iyidir) benzer veya büyük boyutlu dil modellerine kıyasla önemli ölçüde daha başarılıdır. Phi-3-mini iki katı büyüklükteki modelleri geride bırakır, Phi-3-small ve Phi-3-medium ise GPT-3.5 dahil büyük modelleri geride bırakır.

**Phi-3-small & medium**

Sadece 7 milyar parametre ile Phi-3-small çeşitli dil, akıl yürütme, kodlama ve matematik kıyaslamalarında GPT-3.5T'yi geçer.

14 milyar parametreli Phi-3-medium bu trendi sürdürür ve Gemini 1.0 Pro'dan daha iyi performans gösterir.

**Phi-3.5-mini**

Bunu Phi-3-mini'nin bir yükseltmesi olarak düşünebiliriz. Parametre sayısı değişmese de çoklu dili destekleme yeteneği geliştirilmiştir (20+ dili destekler: Arapça, Çince, Çekçe, Danca, Hollandaca, İngilizce, Fince, Fransızca, Almanca, İbranice, Macarca, İtalyanca, Japonca, Korece, Norveççe, Lehçe, Portekizce, Rusça, İspanyolca, İsveççe, Tayca, Türkçe, Ukraynaca) ve uzun bağlam desteği güçlendirilmiştir.

3.8B parametreli Phi-3.5-mini, aynı boyuttaki dil modellerini geride bırakır ve iki katı büyüklükteki modellerle eşdeğerdir.

### Phi-3 / 3.5 Vision

Phi-3/3.5'ün Instruct modeli Phi'nin anlama yeteneği olarak düşünülebilir, Vision ise Phi'ye dünyayı anlaması için gözler kazandırır.


**Phi-3-Vision**

Sadece 4.2B parametreli Phi-3-vision trendi sürdürüyor ve genel görsel akıl yürütme görevlerinde, OCR'da, tablo ve diyagram anlama görevlerinde Claude-3 Haiku ve Gemini 1.0 Pro gibi daha büyük modellerden daha iyi performans gösteriyor.


**Phi-3.5-Vision**

Phi-3.5-Vision ayrıca Phi-3-Vision'in bir yükseltmesidir, çoklu resim desteği ekler. Bunu görüşte bir gelişme olarak düşünebilirsiniz; artık sadece resim değil, video da görebilir.

Phi-3.5-vision OCR, tablo ve grafik anlama görevlerinde Claude-3.5 Sonnet ve Gemini 1.5 Flash gibi daha büyük modelleri geçer, genel görsel bilgi akıl yürütme görevlerinde ise benzer performans gösterir. Çoklu kare girişi destekler, yani birden çok giriş görüntüsünde akıl yürütme yapabilir.


### Phi-3.5-MoE

***Uzmanlar Karışımı (MoE)*** modellerin çok daha az hesaplama ile önceden eğitilmesini sağlar, bu da aynı hesaplama bütçesi ile model veya veri seti boyutunu dramatik olarak artırabilirsiniz. Özellikle, bir MoE modeli yoğun modele kıyasla ön eğitim sırasında aynı kaliteyi çok daha hızlı elde etmelidir.

Phi-3.5-MoE 16x3.8B uzman modülleri içerir. Sadece 6.6B aktif parametre ile Phi-3.5-MoE çok daha büyük modeller kadar akıl yürütme, dil anlama ve matematik başarısı gösterir.

Phi-3/3.5 Aile modeli farklı senaryolara göre kullanılabilir. LLM'lerin aksine Phi-3/3.5-mini veya Phi-3/3.5-Vision uç cihazlarda dağıtılabilir.


## Phi-3/3.5 Aile modelleri nasıl kullanılır

Phi-3/3.5'i farklı senaryolarda kullanmayı umuyoruz. Sonraki adımda farklı senaryolara göre Phi-3/3.5'i kullanacağız.

![phi3](../../../translated_images/tr/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Bulut API'leri ile Çıkarım

**Microsoft Foundry Modelleri**

> **Not:** GitHub Modelleri Temmuz 2026 sonunda emekliye ayrılıyor. [Microsoft Foundry Modelleri](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), doğrudan yerini alacak.

Microsoft Foundry Modelleri en doğrudan yoldur. Foundry model kataloğundan Phi-3/3.5-Instruct modeline hızlıca erişebilirsiniz. Azure AI Inference SDK / OpenAI SDK ile kod üzerinden API erişimi yapabilir ve Phi-3/3.5-Instruct çağrısını tamamlayabilirsiniz. Playground üzerinden farklı etkileri test edebilirsiniz.

- Demo: Çin senaryolarında Phi-3-mini ve Phi-3.5-mini etkilerinin karşılaştırması

![phi3](../../../translated_images/tr/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/tr/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Görüntü ve MoE modellerini kullanmak istiyorsanız Microsoft Foundry aracılığıyla çağrıyı gerçekleştirebilirsiniz. İlginiz varsa, Phi-3 Tarif Kitabını okuyarak Microsoft Foundry üzerinden Phi-3/3.5 Instruct, Vision, MoE çağrılarının nasıl yapılacağını öğrenebilirsiniz [Bu bağlantıya tıklayın](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Bulut tabanlı Microsoft Foundry modeller kataloğuna ek olarak, ilgili çağrıları tamamlamak için [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) kullanılabilir. NVIDIA NIM (NVIDIA Inference Microservices), bulutlar, veri merkezleri ve iş istasyonları dahil çeşitli ortamlar genelinde AI modellerinin verimli dağıtımını sağlamak için tasarlanmış hızlandırılmış çıkarım mikroservisleri setidir.

İşte NVIDIA NIM'in bazı temel özellikleri:

- **Kolay Dağıtım:** NIM, AI modellerinin tek bir komutla dağıtılmasına olanak sağlar, mevcut iş akışlarına entegrasyonunu kolaylaştırır.
- **Optimize Edilmiş Performans:** TensorRT ve TensorRT-LLM gibi NVIDIA'nın önceden optimize edilmiş çıkarım motorlarından yararlanarak düşük gecikme ve yüksek verimlilik sağlar.
- **Ölçeklenebilirlik:** NIM, Kubernetes üzerinde otomatik ölçeklendirmeyi destekleyerek farklı iş yükleriyle etkili şekilde başa çıkar.
- **Güvenlik ve Kontrol:** Kuruluşlar verileri ve uygulamalar üzerinde kontrolü sürdürmek için NIM mikroservislerini kendi yönetilen altyapılarında barındırabilir.
- **Standart API'ler:** NIM, sohbet botları, AI asistanları ve daha fazlası gibi AI uygulamaları oluşturmayı ve entegre etmeyi kolaylaştıran endüstri standardı API'ler sağlar.

NIM, AI modellerinin dağıtımını ve operasyonel hale getirilmesini basitleştirmeyi amaçlayan NVIDIA AI Enterprise'ın bir parçasıdır ve bu modellerin NVIDIA GPU'larda verimli çalışmasını sağlar.

- Demo: NVIDIA NIM kullanarak Phi-3.5-Vision-API çağırma [[Bu bağlantıya tıklayın](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5'i Yerelde Çalıştırma
Phi-3 veya GPT-3 gibi herhangi bir dil modeliyle ilgili çıkarım, aldığı girdiye dayalı olarak yanıtlar veya tahminler üretme sürecini ifade eder. Phi-3'e bir istem veya soru verdiğinizde, eğitildiği verilerdeki desenleri ve ilişkileri analiz ederek en olası ve ilgili yanıtı çıkaran eğitimli sinir ağını kullanır.

**Hugging Face Transformer**
Hugging Face Transformers, doğal dil işleme (NLP) ve diğer makine öğrenimi görevleri için tasarlanmış güçlü bir kütüphanedir. İşte bazı önemli noktalar:

1. **Önceden Eğitilmiş Modeller**: Metin sınıflandırma, varlık tanıma, soru-cevap, özetleme, çeviri ve metin üretimi gibi çeşitli görevlerde kullanılabilecek binlerce önceden eğitilmiş model sağlar.

2. **Çerçeve Uyumluluğu**: Kütüphane, PyTorch, TensorFlow ve JAX dahil olmak üzere birden fazla derin öğrenme çerçevesini destekler. Bu, bir modelin bir çerçevede eğitilip diğerinde kullanılmasını sağlar.

3. **Multimodal Yetenekler**: NLP'nin yanı sıra Hugging Face Transformers, bilgisayarla görme (örneğin, görüntü sınıflandırma, nesne tespiti) ve ses işleme (örneğin, konuşma tanıma, ses sınıflandırma) görevlerini de destekler.

4. **Kullanım Kolaylığı**: Kütüphane, modelleri indirip ince ayar yapmayı kolaylaştıran API'ler ve araçlar sunar, böylece hem yeni başlayanlar hem de uzmanlar için erişilebilir.

5. **Topluluk ve Kaynaklar**: Hugging Face'in canlı bir topluluğu vardır ve kullanıcıların başlamasına ve kütüphaneyi en iyi şekilde kullanmasına yardımcı olacak geniş dokümantasyon, eğitimler ve kılavuzlar bulunur.
[resmi dokümantasyon](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) veya [GitHub deposu](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Bu en yaygın kullanılan yöntemdir, ancak aynı zamanda GPU hızlandırması gerektirir. Sonuçta, Vision ve MoE gibi senaryolar çok sayıda hesaplama gerektirir ve bu hesaplamalar kuantize edilmemişse CPU'da çok yavaş olur.


- Demo: Transformer kullanarak Phi-3.5-Instruct çağırma [Bu bağlantıya tıklayın](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformer kullanarak Phi-3.5-Vision çağırma [Bu bağlantıya tıklayın](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformer kullanarak Phi-3.5-MoE çağırma [Bu bağlantıya tıklayın](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), büyük dil modellerini (LLM'ler) yerel olarak makinenizde daha kolay çalıştırmak için tasarlanmış bir platformdur. Llama 3.1, Phi 3, Mistral ve Gemma 2 gibi çeşitli modelleri destekler. Platform, model ağırlıklarını, yapılandırmayı ve veriyi tek bir paket halinde sunarak kullanıcıların kendi modellerini özelleştirmesini ve oluşturmasını daha erişilebilir hale getirir. Ollama macOS, Linux ve Windows için mevcuttur. Bulut hizmetlerine bağlı kalmadan LLM'lerle denemeler yapmak veya dağıtmak istiyorsanız mükemmel bir araçtır. Ollama en doğrudan yoldur, aşağıdaki komutu çalıştırmanız yeterlidir.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst), Phi gibi modelleri tamamen kendi donanımınızda çalıştırmak için Microsoft'un çevrimdışı, cihaz bazlı çalışma zamanıdır - Azure aboneliği, API anahtarı veya ağ bağlantısı gerekmez. Mevcut en iyi yürütme sağlayıcısını (NPU, GPU veya CPU) otomatik olarak seçer ve OpenAI uyumlu bir uç nokta sunar, böylece mevcut `openai`/Azure AI Inference SDK kodları minimal değişiklikle ona yönlendirilebilir. Başlamak için [Foundry Local dokümantasyonuna](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) bakın.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Ya da SDK'yı doğrudan Python'da kullanın:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime for GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst), çapraz platform çıkarım ve eğitim makine öğrenimi hızlandırıcısıdır. ONNX Runtime for Generative AI (GENAI), üretken AI modellerini farklı platformlarda verimli çalıştırmanıza yardımcı olan güçlü bir araçtır.

## ONNX Runtime Nedir?
ONNX Runtime, makine öğrenimi modellerinin yüksek performanslı çıkarımını sağlayan açık kaynak bir projedir. Makine öğrenimi modellerini temsil etmek için standart bir format olan Open Neural Network Exchange (ONNX) formatındaki modelleri destekler. ONNX Runtime çıkarımı daha hızlı müşteri deneyimleri ve düşük maliyetler sağlar. Derin öğrenme çerçeveleri olan PyTorch ve TensorFlow/Keras'ın yanı sıra klasik makine öğrenimi kütüphaneleri olan scikit-learn, LightGBM, XGBoost vb. modelleri destekler. ONNX Runtime farklı donanımlar, sürücüler ve işletim sistemleri ile uyumludur ve uygun donanım hızlandırıcıları yanı sıra grafik optimizasyonları ve dönüşümleri ile optimal performans sunar.

## Üretken AI Nedir?
Üretken AI, eğitildiği verilere dayanarak metin, görüntü veya müzik gibi yeni içerik üretebilen AI sistemlerini ifade eder. Örnekler arasında GPT-3 gibi dil modelleri ve Stable Diffusion gibi görüntü üretim modelleri bulunur. ONNX Runtime for GenAI kütüphanesi, ONNX modelleri için üretken AI döngüsünü sağlar; bu, ONNX Runtime ile çıkarım, logit işleme, arama ve örnekleme, KV önbellek yönetimini içerir.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI, ONNX Runtime'in yeteneklerini üretken AI modellerini destekleyecek şekilde genişletir. İşte bazı önemli özellikler:

- **Geniş Platform Desteği:** Windows, Linux, macOS, Android ve iOS dahil çeşitli platformlarda çalışır.
- **Model Desteği:** LLaMA, GPT-Neo, BLOOM ve daha birçok popüler üretken AI modelini destekler.
- **Performans Optimizasyonu:** NVIDIA GPU'lar, AMD GPU'lar ve daha fazlası gibi çeşitli donanım hızlandırıcılar için optimizasyonlar içerir.
- **Kullanım Kolaylığı:** Uygulamalara kolayca entegre edilebilen API'ler sağlar; çok az kodla metin, görüntü ve diğer içerikleri üretebilirsiniz.
- Kullanıcılar yüksek seviyeli generate() metodunu çağırabilir veya modeli bir döngü içinde her defasında bir token üreterek çalıştırabilir ve isteğe bağlı olarak döngü içinde üretim parametrelerini güncelleyebilir.
- ONNX runtime aynı zamanda açgözlü/kiriş araması ve TopP, TopK örneklemeyi destekler; token dizileri oluşturabilir ve tekrarlama cezaları gibi yerleşik logit işleme işlevleri vardır. Ayrıca özel skorlamalar kolayca eklenebilir.

## Başlarken
ONNX Runtime for GENAI ile başlamak için şu adımları izleyebilirsiniz:

### ONNX Runtime Kurulumu:
```Python
pip install onnxruntime
```
### Üretken AI Uzantılarını Kurun:
```Python
pip install onnxruntime-genai
```

### Bir Model Çalıştırın: İşte Python'da basit bir örnek:
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
### Demo: ONNX Runtime GenAI ile Phi-3.5-Vision çağırma


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

ONNX Runtime, Ollama ve Foundry Local referans yöntemlerine ek olarak, farklı üreticilerin sağladığı model referans yöntemlerine dayalı kantitatif modellerin referansını da tamamlayabiliriz. Örneğin Apple Metal ile Apple MLX framework, NPU ile Qualcomm QNN, CPU/GPU ile Intel OpenVINO vb. Daha fazla içerik için [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst) sayfasına da göz atabilirsiniz.


## Daha Fazlası

Phi-3/3.5 Ailesinin temellerini öğrendik, ancak SLM hakkında daha fazla bilgi edinmek için daha fazla bilgiye ihtiyaç var. Cevapları Phi-3 Cookbook'ta bulabilirsiniz. Daha fazla bilgi edinmek isterseniz, lütfen [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst) adresini ziyaret edin.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->