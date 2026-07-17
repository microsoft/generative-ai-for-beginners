# Yeni Başlayanlar için Üretken Yapay Zeka İçin Küçük Dil Modellerine Giriş
Üretken Yapay Zeka, yeni içerik oluşturabilen sistemler geliştirmeye odaklanan büyüleyici bir yapay zeka alanıdır. Bu içerik metin ve görsellerden müzik ve hatta tamamı sanal ortamlar oluşturulmasına kadar değişebilir. Üretken yapay zekanın en heyecan verici uygulamalarından biri dil modelleri alanındadır.

## Küçük Dil Modelleri Nedir?

Küçük Dil Modeli (KDM), büyük dil modeli (BDM) prensip ve tekniklerinin çoğunu kullanan, ancak hesaplama gereksinimleri önemli ölçüde azaltılmış küçültülmüş bir büyük dil modeli çeşididir.

KDM'ler, insan benzeri metin üretmek üzere tasarlanmış bir dil modeli alt kümesidir. GPT-4 gibi daha büyük modellerin aksine, KDM'ler daha kompakt ve verimlidir, bu da onları hesaplama kaynaklarının kısıtlı olduğu uygulamalar için ideal hale getirir. Daha küçük olmalarına rağmen çeşitli görevleri yerine getirebilirler. Genellikle KDM'ler, orijinal modelin işlevselliği ve dil yeteneklerinin önemli bir kısmını korumayı hedefleyerek BDM'lerin sıkıştırılması veya damıtılmasıyla oluşturulur. Model boyutundaki bu azalma, hem bellek kullanımı hem de hesaplama açısından KDM'leri daha verimli hale getirerek genel karmaşıklığını azaltır. Bu optimizasyonlara rağmen KDM'ler hala çok geniş bir doğal dil işleme (NLP) görev yelpazesini yerine getirebilir:

- Metin Üretimi: Tutarlı ve bağlam açısından uygun cümleler veya paragraflar oluşturmak.
- Metin Tamamlama: Verilen bir istem üzerine cümleleri tahmin etmek ve tamamlamak.
- Çeviri: Metni bir dilden başka bir dile çevirmek.
- Özetleme: Uzun metinleri daha kısa ve sindirilebilir özetlere dönüştürmek.

Daha büyük modellerle karşılaştırıldığında performans veya anlama derinliği açısından bazı ödünlerle birlikte.

## Küçük Dil Modelleri Nasıl Çalışır?
KDM'ler büyük miktarda metin verisi üzerinde eğitilir. Eğitim sırasında dilin kalıplarını ve yapısını öğrenirler, böylece hem dilbilgisel olarak doğru hem de bağlamsal olarak uygun metinler üretebilirler. Eğitim süreci şunları içerir:

- Veri Toplama: Çeşitli kaynaklardan büyük metin veri setleri toplamak.
- Ön İşleme: Verileri temizleyip eğitim için uygun hale getirmek.
- Eğitim: Makine öğrenimi algoritmaları kullanarak modelin metni anlaması ve üretmesini öğretmek.
- İnce Ayar: Modeli belirli görevlerde performansını artırmak için ayarlamak.

KDM'lerin geliştirilmesi, tam kapsamlı BDM'lerin ağır kaynak gereksinimleri nedeniyle pratik olmayan mobil cihazlar veya kenar bilişim platformları gibi kısıtlı kaynaklı ortamlarda dağıtım ihtiyacının artmasıyla paraleldir. Verimliliğe odaklanarak, KDM'ler performans ile erişilebilirlik arasında denge kurar ve çeşitli alanlarda daha geniş uygulama imkânı sağlar.

![slm](../../../translated_images/tr/slm.4058842744d0444a.webp)

## Öğrenim Hedefleri

Bu derste, KDM hakkında bilgi vermeyi ve Microsoft Phi-3 ile metin içeriği, görsel ve MoE'deki farklı senaryoları öğrenmeyi amaçlıyoruz.

Dersin sonunda aşağıdaki soruları cevaplayabilmeniz beklenmektedir:

- KDM nedir?
- KDM ile BDM arasındaki fark nedir?
- Microsoft Phi-3/3.5 Ailesi nedir?
- Microsoft Phi-3/3.5 Ailesi ile çıkarım nasıl yapılır?

Hazır mısınız? Hadi başlayalım.

## Büyük Dil Modelleri (BDM) ve Küçük Dil Modelleri (KDM) Arasındaki Farklar

Hem BDM'ler hem de KDM'ler temelinde olasılıksal makine öğrenimi prensiplerine dayanır, mimari tasarımlarında, eğitim yöntemlerinde, veri üretim süreçlerinde ve model değerlendirme tekniklerinde benzer yaklaşımlar izler. Ancak bu iki model türünü ayıran birkaç önemli faktör vardır.

## Küçük Dil Modellerinin Uygulama Alanları

KDM'ler aşağıdaki alanlarda yaygın olarak kullanılır:

- Sohbet Botları: Müşteri desteği vermek ve kullanıcılarla sohbet etmek.
- İçerik Oluşturma: Yazarlara fikir üretme veya makale taslakları oluşturma konusunda yardımcı olmak.
- Eğitim: Öğrencilere yazı ödevlerinde veya yeni diller öğrenmede destek olmak.
- Erişilebilirlik: Metin okuma sistemleri gibi engelli bireyler için araçlar oluşturmak.

**Boyut**
 
BDM ile KDM arasındaki temel farklardan biri model ölçeğidir. ChatGPT (GPT-4) gibi BDM'ler yaklaşık 1,76 trilyon parametreye sahip olabilirken, açık kaynaklı KDM'ler, örneğin Mistral 7B, çok daha az parametreyle tasarlanmıştır — yaklaşık 7 milyar. Bu fark öncelikle model mimarisi ve eğitim süreçlerinden kaynaklanır. Örneğin, ChatGPT, kod çözücü-şifreleyici yapısı içinde kendine dikkat mekanizması kullanırken, Mistral 7B ise sadece kod çözücü modelinde daha verimli eğitim sağlayan kaydırmalı pencere dikkat mekanizması kullanır. Bu mimari farklılıklar, modellerin karmaşıklığı ve performans üzerinde derin etkiler yaratır.

**Anlama**

KDM'ler genellikle belirli alanlarda performans için optimize edilmiştir, bu yüzden oldukça uzmanlaşmış ancak çok sayıda bilgi alanında geniş bağlamsal anlayış sağlama kapasitesi sınırlı olabilir. Buna karşılık, BDM'ler, insan benzeri zekayı daha kapsamlı şekilde taklit etmeyi amaçlar. Büyük, çeşitli veri setleri üzerinde eğitilen BDM'ler, farklı alanlarda iyi performans gösterecek şekilde tasarlanmıştır ve daha fazla esneklik ve uyarlanabilirlik sunar. Bu nedenle, BDM'ler doğal dil işleme ve programlama gibi daha geniş bir yelpazedeki görevler için daha uygundur.

**Hesaplama**

BDM'lerin eğitimi ve devreye alınması kaynak yoğun süreçlerdir ve sıklıkla büyük ölçekli GPU küme altyapısı gerektirir. Örneğin, ChatGPT gibi bir modeli sıfırdan eğitmek, uzun süre boyunca binlerce GPU ihtiyacı doğurabilir. Buna karşılık, KDM'ler daha az parametreye sahip oldukları için hesaplama açısından daha erişilebilir durumdadır. Mistral 7B gibi modeller, orta seviye GPU donanımlarına sahip yerel makinelerde eğitilip çalıştırılabilir; ancak eğitim gene de birden fazla GPU üzerinde birkaç saat sürebilir.

**Önyargı**

Önyargı, BDM'lerde eğitim verilerinin doğasından kaynaklanan bilinen bir sorundur. Bu modeller genellikle internetten alınan ham, açık erişimli verilere dayanır; bu veriler belirli grupları yeterince temsil etmeyebilir veya yanlış temsil edebilir, yanlış etiketlendirmeler içerebilir veya lehçe, coğrafi farklılıklar ve dilbilgisi kurallarından kaynaklanan dilsel önyargılar barındırabilir. Ayrıca BDM'lerin mimari karmaşıklığı, dikkatli ince ayar yapılmadığında önyargıyı daha da artırabilir. Öte yandan, KDM'ler daha sınırlı ve alan odaklı veri setlerinde eğitildikleri için bu tür önyargılara karşı daha az duyarlıdır, ancak tamamen bağışıktırlar demek değildir.

**Çıkarım**

KDM'lerin küçültülmüş boyutu, çıkarım hızı açısından büyük bir avantaj sağlar; geniş paralel işlem gücü olmadan yerel donanımda verimli çıktı üretmelerine imkân tanır. Buna karşılık, BDM'ler boyutları ve karmaşıklıkları nedeniyle kabul edilebilir çıkarım sürelerine ulaşmak için genellikle önemli paralel hesaplama kaynaklarına ihtiyaç duyar. Aynı anda birden çok kullanıcının bulunması, BDM'lerin yanıt sürelerini özellikle büyük ölçekte dağıtıldığında daha da yavaşlatır.

Özetle, BDM ve KDM, makine öğreniminde ortak bir temele dayansalar da, model boyutu, kaynak gereksinimleri, bağlamsal anlama, önyargıya yatkınlık ve çıkarım hızı açısından önemli farklılıklar gösterirler. Bu farklar, kullanım durumlarına göre uygunluklarını belirler; BDM'ler daha çok yönlü ancak kaynak yoğun, KDM'ler ise belirli alanlarda daha verimli ve daha az hesaplama talebiyle öne çıkar.

***Not: Bu derste örnek olarak Microsoft Phi-3/3.5 kullanılarak KDM tanıtılacaktır.***

## Phi-3 / Phi-3.5 Ailesi Tanıtımı

Phi-3 / 3.5 Ailesi başlıca metin, görsel ve Ajan (MoE) uygulama senaryolarına yöneliktir:

### Phi-3 / 3.5 Instruct

Başlıca metin üretimi, sohbet tamamlama ve içerik bilgi çıkarımı için kullanılır.

**Phi-3-mini**

3.8B parametreli dil modeli Microsoft Foundry, Hugging Face ve Ollama’da mevcuttur. Phi-3 modelleri, anahtar kıyaslama testlerinde eşit ve daha büyük boyutlu dil modellerinden önemli ölçüde daha iyi performans gösterir (aşağıdaki kıyaslama rakamlarına bakınız, rakamlar ne kadar yüksekse o kadar iyidir). Phi-3-mini, kendi boyutunun iki katı büyüklüğündeki modelleri geride bırakırken, Phi-3-small ve Phi-3-medium, GPT-3.5 dahil daha büyük modelleri geçmektedir.

**Phi-3-small & medium**

Sadece 7B parametreye sahip Phi-3-small, dil, muhakeme, kodlama ve matematik kıyaslama testlerinde GPT-3.5T’yi yener.

14B parametreli Phi-3-medium bu eğilimi sürdürür ve Gemini 1.0 Pro’dan daha iyi performans gösterir.

**Phi-3.5-mini**

Bunu Phi-3-mini'nin bir yükseltmesi olarak düşünebiliriz. Parametre sayısı aynı kalmakla birlikte, birden çok dili destekleme yeteneğini geliştirir (20’den fazla dili destekler: Arapça, Çince, Çekçe, Danca, Hollandaca, İngilizce, Fince, Fransızca, Almanca, İbranice, Macarca, İtalyanca, Japonca, Korece, Norveççe, Lehçe, Portekizce, Rusça, İspanyolca, İsveççe, Tayca, Türkçe, Ukraynaca) ve uzun bağlam desteğini güçlendirir.

3.8B parametreli Phi-3.5-mini, aynı boyuttaki dil modellerini geride bırakır ve kendi boyutunun iki katı büyüklüğündeki modellerle yarışır.

### Phi-3 / 3.5 Vision

Phi-3/3.5 Instruct modelini Phi'nin anlama yeteneği, Vision'u ise Phi'nin dünyayı görmesini sağlayan özellik olarak düşünebiliriz.


**Phi-3-Vision**

Sadece 4.2B parametreye sahip Phi-3-vision, genel görsel muhakeme görevlerinde, OCR’da ve tablo ile diyagram anlama alanlarında Claude-3 Haiku ve Gemini 1.0 Pro gibi daha büyük modelleri geride bırakmaya devam eder.


**Phi-3.5-Vision**

Phi-3.5-Vision, Phi-3-Vision'un bir yükseltmesidir, çoklu görüntü desteği ekler. Bunu sadece fotoğrafları değil, videoları da görebilen gelişmiş bir görüş olarak düşünebilirsiniz.

Phi-3.5-vision, OCR, tablo ve grafik anlama görevlerinde Claude-3.5 Sonnet ve Gemini 1.5 Flash gibi daha büyük modelleri geride bırakır ve genel görsel bilgi muhakeme alanında eşit performans gösterir. Çoklu kare girişini destekler, yani birden çok giriş görüntüsü üzerinde muhakeme yapabilir.


### Phi-3.5-MoE

***Uzmanlar Karışımı (MoE)***, modellerin çok daha az hesaplama ile önceden eğitilmesini mümkün kılar, bu da aynı hesaplama bütçesiyle model veya veri seti boyutunu dramatik şekilde artırmanıza olanak tanır. Özellikle, MoE modeli ön eğitim sırasında yoğun model muadilinden çok daha hızlı aynı kaliteyi sağlamalıdır.

Phi-3.5-MoE, 16x3.8B uzman modüllerinden oluşur. Sadece 6.6B aktif parametreye sahip Phi-3.5-MoE, çok daha büyük modellerle benzer seviyede muhakeme, dil anlama ve matematik başarır.

Phi-3/3.5 Ailesi modelini farklı senaryolara göre kullanabiliriz. LLM’lerin aksine, Phi-3/3.5-mini veya Phi-3/3.5-Vision'ı kenar cihazlarda dağıtabilirsiniz.


## Phi-3/3.5 Aile modelleri nasıl kullanılır

Phi-3/3.5’i farklı senaryolarda kullanmayı umuyoruz. Sonraki bölümde farklı senaryolara dayalı Phi-3/3.5 kullanımını inceleyeceğiz.

![phi3](../../../translated_images/tr/phi3.655208c3186ae381.webp)

### Bulut API'leri aracılığıyla çıkarım

**Microsoft Foundry Modelleri**

> **Not:** GitHub Modelleri, Temmuz 2026 sonunda kullanımdan kaldırılacaktır. [Microsoft Foundry Modelleri](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) doğrudan yerini alacaktır.

Microsoft Foundry Modelleri en doğrudan yoldur. Phi-3/3.5-Instruct modeline Foundry model kataloğu üzerinden hızlıca erişebilirsiniz. Azure AI Inference SDK / OpenAI SDK ile kombine ederek, API'ye kod üzerinden ulaşabilir ve Phi-3/3.5-Instruct çağrısını tamamlayabilirsiniz. Ayrıca Playground üzerinden farklı etkileri test edebilirsiniz.

- Demo: Phi-3-mini ve Phi-3.5-mini'nin Çince senaryolardaki etkilerinin kıyaslaması

![phi3](../../../translated_images/tr/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/tr/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Görsel ve MoE modellerini kullanmak istersek, Microsoft Foundry ile çağrıyı gerçekleştirebiliriz. İlgileniyorsanız, Phi-3 Cookbook'u okuyarak Microsoft Foundry üzerinden Phi-3/3.5 Instruct, Vision, MoE nasıl çağrılır öğrenebilirsiniz [Bu linke tıklayın](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Bulut tabanlı Microsoft Foundry Modelleri kataloğuna ek olarak, [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) ile ilgili çağrıları gerçekleştirebilirsiniz. NVIDIA NIM, Phi-3/3.5 Aile API çağrılarını tamamlamak için kullanılabilir. NVIDIA NIM (NVIDIA Inference Microservices), geliştiricilerin bulutlar, veri merkezleri ve iş istasyonları da dahil çeşitli ortamlarda AI modellerini etkili şekilde konuşlandırmalarına yardımcı olan hızlandırılmış çıkarım mikroservisler setidir.

NVIDIA NIM'in bazı önemli özellikleri şunlardır:

- **Dağıtım Kolaylığı:** NIM, AI modellerinin tek bir komutla dağıtımını sağlar, böylece mevcut iş akışlarına entegre etmek kolaydır.

- **Optimize Edilmiş Performans:** Düşük gecikme ve yüksek verimlilik sağlamak için TensorRT ve TensorRT-LLM gibi NVIDIA’nın önceden optimize edilmiş çıkarım motorlarını kullanır.
- **Ölçeklenebilirlik:** NIM, Kubernetes üzerinde otomatik ölçeklendirmeyi destekleyerek değişen iş yüklerini etkili bir şekilde yönetmesini sağlar.
- **Güvenlik ve Kontrol:** Kuruluşlar, NIM mikroservislerini kendi yönetilen altyapılarında barındırarak verileri ve uygulamalar üzerinde kontrol sahibi olabilirler.
- **Standart API’ler:** NIM, sohbet botları, yapay zeka asistanları ve daha fazlası gibi AI uygulamaları geliştirmeyi ve entegre etmeyi kolaylaştıran sektör standartlarında API’ler sunar.

NIM, NVIDIA AI Enterprise’ın bir parçasıdır ve AI modellerinin dağıtımını ve işletilmesini basitleştirerek, NVIDIA GPU’larda verimli çalışmasını sağlar.

- Demo: NVIDIA NIM kullanarak Phi-3.5-Vision-API çağırma [[Bu bağlantıya tıklayın](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5’i Yerelde Çalıştırma
Phi-3 veya GPT-3 gibi herhangi bir dil modeli ile ilgili çıkarım, aldığı girdiye dayanarak yanıtlar veya tahminler üretme sürecidir. Phi-3’e bir soru ya da istem verdiğinizde, eğitildiği verilerdeki kalıpları ve ilişkileri analiz ederek en olası ve ilgili yanıtı tahmin etmek için eğitilmiş sinir ağını kullanır.

**Hugging Face Transformer**
Hugging Face Transformers, doğal dil işleme (NLP) ve diğer makine öğrenimi görevleri için tasarlanmış güçlü bir kitaplıktır. İşte bazı önemli noktalar:

1. **Önceden Eğitilmiş Modeller**: Metin sınıflandırma, adlandırılmış varlık tanıma, soru yanıtlama, özetleme, çeviri ve metin oluşturma gibi çeşitli görevler için kullanılabilecek binlerce önceden eğitilmiş model sunar.

2. **Çerçeve Uyumluluğu**: Kitaplık, PyTorch, TensorFlow ve JAX dahil olmak üzere birden fazla derin öğrenme çerçevesini destekler. Bu, bir çerçevede model eğitip diğerinde kullanmanıza olanak tanır.

3. **Multimodal Yetenekler**: NLP’nin yanı sıra Hugging Face Transformers, bilgisayarla görme (örneğin, görsel sınıflandırma, nesne tespiti) ve ses işleme (örneğin, konuşma tanıma, ses sınıflandırma) görevlerini de destekler.

4. **Kolay Kullanım**: Kitaplık, modelleri kolayca indirip ince ayar yapmanızı sağlayan API’ler ve araçlar sunar; hem yeni başlayanlar hem de uzmanlar için erişilebilirdir.

5. **Topluluk ve Kaynaklar**: Hugging Face, canlı bir topluluğa sahiptir ve kullanıcıların başlamasına ve kitaplıktan en iyi şekilde yararlanmasına yardımcı olacak kapsamlı dokümantasyon, öğreticiler ve rehberler sağlar.
[resmi dokümantasyon](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) veya [GitHub depoları](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst) üzerinden erişebilirsiniz.

Bu en yaygın kullanılan yöntemdir ancak GPU hızlandırması gerektirir. Sonuçta, Vision ve MoE gibi senaryolar çok fazla hesaplama gerektirir, eğer kuantize edilmezlerse CPU üzerinde oldukça yavaş çalışır.


- Demo: Transformer kullanarak Phi-3.5-Instruct çağırma [Bu bağlantıya tıklayın](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformer kullanarak Phi-3.5-Vision çağırma [Bu bağlantıya tıklayın](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformer kullanarak Phi-3.5-MoE çağırma [Bu bağlantıya tıklayın](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), büyük dil modellerini (LLM) yerel olarak makinenizde çalıştırmayı kolaylaştırmak için tasarlanmış bir platformdur. Llama 3.1, Phi 3, Mistral ve Gemma 2 gibi çeşitli modelleri destekler. Platform, model ağırlıklarını, yapılandırmasını ve verilerini tek bir pakete dahil ederek işlemi basitleştirir; böylece kullanıcılar kendi modellerini özelleştirip oluşturabilirler. Ollama, macOS, Linux ve Windows için mevcuttur. Eğer LLM’lerle deneme yapmak veya konuşlandırmak istiyorsanız ve bulut servislerine bağlı kalmak istemiyorsanız harika bir araçtır. Ollama en doğrudan yoldur; sadece aşağıdaki komutu çalıştırmanız gerekir.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst), Phi gibi modelleri tamamen kendi donanımınızda, çevrimdışı ve cihaz üzerinde çalıştırmak için Microsoft’un sunduğu bir çalışma zamanıdır - Azure aboneliği, API anahtarı veya ağ bağlantısı gerektirmez. En iyi yürütme sağlayıcısını (NPU, GPU veya CPU) otomatik olarak seçer ve OpenAI uyumlu bir uç nokta sunar, böylece mevcut `openai`/Azure AI Inference SDK kodları minimum değişiklikle ona yönlendirilebilir. Başlamak için [Foundry Local dokümantasyonuna](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) bakabilirsiniz.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Veya SDK’yı Python’da doğrudan kullanabilirsiniz:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**GenAI için ONNX Runtime**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst), çapraz platform destekli çıkarım ve eğitim makine öğrenimi hızlandırıcısıdır. GenAI için ONNX Runtime (GENAI), üretken AI modellerini çeşitli platformlarda verimli bir şekilde çalıştırmanıza yardımcı olan güçlü bir araçtır.

## ONNX Runtime Nedir?
ONNX Runtime, makine öğrenimi modellerinin yüksek performanslı çıkarımını mümkün kılan açık kaynaklı bir projedir. Open Neural Network Exchange (ONNX) formatındaki modelleri destekler; bu format makine öğrenimi modellerini temsil etmek için bir standarttır. ONNX Runtime çıkarımı, PyTorch ve TensorFlow/Keras gibi derin öğrenme çerçevelerinden ve scikit-learn, LightGBM, XGBoost gibi klasik makine öğrenimi kütüphanelerinden gelen modelleri destekleyerek daha hızlı müşteri deneyimleri ve düşük maliyetler sağlar. ONNX Runtime farklı donanımlar, sürücüler ve işletim sistemleriyle uyumludur ve donanım hızlandırıcılarını, grafik optimizasyonları ve dönüşümleri kullanarak optimal performans sunar.

## Üretken AI Nedir?
Üretken AI, eğitildiği verilere dayanarak metin, görüntü veya müzik gibi yeni içerikler üretebilen AI sistemlerini ifade eder. Örnekler arasında GPT-3 gibi dil modelleri ve Stable Diffusion gibi görüntü oluşturma modelleri bulunur. ONNX Runtime for GenAI kütüphanesi, ONNX modelleri için üretken AI döngüsünü sağlar; buna ONNX Runtime ile çıkarım, logits işleme, arama ve örnekleme ile KV önbellek yönetimi dahildir.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI, ONNX Runtime’ın yeteneklerini üretken AI modellerini destekleyecek şekilde genişletir. İşte bazı önemli özellikleri:

- **Geniş Platform Desteği:** Windows, Linux, macOS, Android ve iOS dahil çeşitli platformlarda çalışır.
- **Model Desteği:** LLaMA, GPT-Neo, BLOOM ve diğer popüler üretken AI modellerini destekler.
- **Performans Optimizasyonu:** NVIDIA GPU’lar, AMD GPU’lar ve diğerleri gibi farklı donanım hızlandırıcıları için optimizasyonlar içerir.
- **Kolay Kullanım:** Metin, görüntü ve diğer içerikleri minimal kod ile üretmenizi sağlayan uygulamalara kolay entegrasyon için API’ler sunar.
- Kullanıcılar yüksek seviyede generate() metodunu çağırabilir veya her döngüde modeli bir token üretecek şekilde çalıştırabilir ve opsiyonel olarak döngü içinde üretim parametrelerini güncelleyebilir.
- ONNX runtime ayrıca açgözlü/kiriş arama, TopP, TopK örnekleme ve yineleme cezaları gibi yerleşik logits işleme özelliklerini destekler. Ayrıca kolayca özel puanlama ekleyebilirsiniz.

## Başlarken
ONNX Runtime for GENAI kullanmaya başlamak için aşağıdaki adımları izleyebilirsiniz:

### ONNX Runtime Kurulumu:
```Python
pip install onnxruntime
```
### Üretken AI Uzantılarını Kurun:
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
### Demo: ONNX Runtime GenAI kullanarak Phi-3.5-Vision çağırma


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

ONNX Runtime, Ollama ve Foundry Local referans yöntemlerine ek olarak, farklı üreticilerin sağladığı model referans yöntemlerine dayalı kantitatif modellerin referanslarını da tamamlayabiliriz. Örneğin Apple Metal ile Apple MLX çerçevesi, NPU destekli Qualcomm QNN, CPU/GPU destekli Intel OpenVINO gibi. Daha fazla içeriğe [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst) üzerinden ulaşabilirsiniz.


## Daha Fazlası

Phi-3/3.5 Ailesinin temellerini öğrendik, ancak SLM hakkında daha fazla bilgi edinmek için daha çok bilgiye ihtiyacımız var. Yanıtları Phi-3 Cookbook’ta bulabilirsiniz. Daha fazla öğrenmek isterseniz, lütfen [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst) sayfasını ziyaret edin.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->