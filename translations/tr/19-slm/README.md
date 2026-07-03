# Üretici Yapay Zeka için Küçük Dil Modellerine Giriş - Başlangıç Seviyesi
Üretici Yapay Zeka, yeni içerikler oluşturabilen sistemler yaratmaya odaklanan yapay zekanın büyüleyici bir alanıdır. Bu içerikler metin ve görüntülerden müzik ve hatta tam sanal ortamlara kadar değişebilir. Üretici yapay zekanın en heyecan verici uygulamalarından biri, dil modelleri alanındadır.

## Küçük Dil Modelleri Nedir?

Küçük Dil Modeli (SLM), büyük dil modelinin (LLM) ölçeklendirilmiş bir varyantını temsil eder ve LLM'lerin birçok mimari ilkesini ve tekniğini kullanırken, hesaplama ayak izini önemli ölçüde azaltır.

SLM'ler, insan benzeri metin üretmek için tasarlanmış dil modellerinin bir alt kümesidir. GPT-4 gibi daha büyük modellerin aksine, SLM'ler daha kompakt ve verimlidir, bu da hesaplama kaynaklarının sınırlı olduğu uygulamalar için idealdir. Küçük olmalarına rağmen, çeşitli görevleri gerçekleştirebilirler. Genellikle SLM'ler, LLM'lerin sıkıştırılması veya damıtılması yoluyla oluşturulur ve orijinal modelin işlevselliğinin ve dil yeteneklerinin önemli bir kısmını korumayı amaçlar. Model boyutundaki bu küçülme genel karmaşıklığı azaltır ve SLM'leri hem bellek kullanımı hem de hesaplama gereksinimleri açısından daha verimli kılar. Bu optimizasyonlara rağmen, SLM'ler aşağıdaki doğal dil işleme (NLP) görevlerini gerçekleştirebilir:

- Metin Üretimi: Tutarlı ve bağlamsal olarak ilgili cümleler veya paragraflar oluşturmak.
- Metin Tamamlama: Verilen bir ipucuna dayanarak cümleleri tahmin etmek ve tamamlamak.
- Çeviri: Metni bir dilden diğerine dönüştürmek.
- Özetleme: Uzun metinleri daha kısa ve daha sindirilebilir özetlere dönüştürmek.

Bunlar, daha büyük modellerine kıyasla bazı performans veya anlayış derinliği açısından ödünler verilerek yapılabilir.

## Küçük Dil Modelleri Nasıl Çalışır?
SLM'ler, büyük miktarda metin verisi üzerinde eğitilir. Eğitim sırasında, dilin kalıplarını ve yapısını öğrenirler, böylece hem dilbilgisi açısından doğru hem de bağlama uygun metinler üretebilirler. Eğitim süreci şunları içerir:

- Veri Toplama: Çeşitli kaynaklardan büyük metin veri kümeleri toplanması.
- Ön İşleme: Verilerin temizlenmesi ve eğitime uygun şekilde düzenlenmesi.
- Eğitim: Modelin metni anlama ve üretme yeteneğini öğretmek için makine öğrenimi algoritmalarının kullanılması.
- İnce Ayar: Modelin belirli görevlerdeki performansını iyileştirmek için ayarlanması.

SLM'lerin geliştirilmesi, tam ölçekli LLM'lerin ağır kaynak gereksinimleri nedeniyle pratik olmayan mobil cihazlar veya uç bilişim platformları gibi kısıtlı kaynak ortamlarında kullanılabilecek modellere artan ihtiyata paraleldir. Verimliliğe odaklanarak, SLM'ler performans ile erişilebilirlik arasındaki dengeyi sağlar ve çeşitli alanlarda daha geniş uygulamalarına olanak tanır.

![slm](../../../translated_images/tr/slm.4058842744d0444a.webp)

## Öğrenim Hedefleri

Bu derste, SLM bilgisini tanıtmayı ve Microsoft Phi-3 ile birleştirerek metin içeriği, görsel ve MoE alanlarında farklı senaryoları öğrenmeyi hedefliyoruz.

Bu dersin sonunda aşağıdaki soruları yanıtlayabilecek duruma gelmeniz beklenmektedir:

- SLM nedir?
- SLM ile LLM arasındaki fark nedir?
- Microsoft Phi-3/3.5 Ailesi nedir?
- Microsoft Phi-3/3.5 Ailesiyle çıkarım nasıl yapılır?

Hazır mısınız? Başlayalım.

## Büyük Dil Modelleri (LLM) ve Küçük Dil Modelleri (SLM) Arasındaki Farklar

Hem LLM'ler hem de SLM'ler, olasılıksal makine öğrenimi temel prensiplerine dayanır ve mimari tasarım, eğitim yöntemleri, veri üretimi süreçleri ve model değerlendirme tekniklerinde benzer yaklaşımları takip eder. Ancak, bu iki model türünü ayıran birkaç önemli faktör vardır.

## Küçük Dil Modellerinin Uygulamaları

SLM'lerin geniş bir uygulama yelpazesi vardır, örneğin:

- Sohbet Botları: Müşteri desteği sağlamak ve kullanıcılarla sohbet bazlı etkileşimlerde bulunmak.
- İçerik Oluşturma: Yazarların fikir üretmesine veya tam makaleler taslağı oluşturmasına yardımcı olmak.
- Eğitim: Öğrencilere yazı ödevlerinde veya yeni diller öğrenirken destek olmak.
- Erişilebilirlik: Metinden sesi dönüştürme sistemleri gibi engelli bireyler için araçlar oluşturmak.

**Boyut**

LLM ve SLM arasındaki temel farklardan biri model ölçeğidir. LLM'ler, örneğin ChatGPT (GPT-4), tahminen 1,76 trilyon parametre içerirken, açık kaynak kodlu SLM'ler olan Mistral 7B gibi modeller çok daha az parametreye — yaklaşık 7 milyar — sahiptir. Bu fark, esasen model mimarisi ve eğitim süreçlerindeki farklılıklardan kaynaklanır. Örneğin, ChatGPT bir kodlayıcı-çözücü çerçevesinde kendi kendine dikkat mekanizması kullanırken, Mistral 7B çözücüye özgü bir model içinde kayar pencere dikkat mekanizması kullanır, bu da daha verimli eğitim sağlar. Bu mimari farklar modellerin karmaşıklığı ve performansı üzerinde derin etkiler yaratır.

**Anlayış**

SLM'ler tipik olarak belirli alanlarda performans için optimize edilir, böylece oldukça uzmanlaşmış ama çoklu bilgi alanları arasında geniş bağlamsal anlayış sağlama yetenekleri sınırlı olabilir. Buna karşılık, LLM'ler daha geniş kapsamlı insan benzeri zekayı taklit etmeye çalışır. Büyük ve çeşitli veri kümelerinde eğitim görmüş LLM'ler, çeşitli alanlarda iyi performans göstererek daha fazla çok yönlülük ve uyarlanabilirlik sunar. Sonuç olarak, LLM'ler doğal dil işleme ve programlama gibi daha geniş kapsamlı görevler için daha uygundur.

**Hesaplama**

LLM'lerin eğitimi ve dağıtımı yüksek kaynak gerektirir ve genellikle büyük GPU kümeleri gibi önemli hesaplama altyapısına ihtiyaç duyar. Örneğin, ChatGPT gibi bir modeli sıfırdan eğitmek, binlerce GPU'nun uzun süre çalışmasını gerektirebilir. Buna karşılık, daha düşük parametre sayısına sahip SLM'ler hesaplama kaynakları açısından daha erişilebilirdir. Mistral 7B gibi modeller, orta seviyede GPU donanımı bulunan yerel makinelerde eğitilebilir ve çalıştırılabilir; ancak eğitim hâlâ birkaç saat ve birden fazla GPU kullanımını gerektirir.

**Önyargı**

LLM'lerde önyargı, başlıca eğitim verilerinin doğasından kaynaklanan bilinen bir sorundur. Bu modeller genellikle internetten açıkça erişilebilir ham verilerle eğitildiğinden, bazı grupları az temsil edebilir veya yanlış temsil edebilir, hatalı etiketleme içerebilir veya lehçe, coğrafi farklılıklar ve dilbilgisel kurallarla şekillenen dilsel önyargılar barındırabilir. Ayrıca, LLM mimarilerinin karmaşıklığı önyargıyı fark edilmeden artırabilir ve dikkatli ince ayar gerektirir. Öte yandan, SLM'ler daha sınırlı, alan odaklı veri kümeleriyle eğitildiği için bu tür önyargılara karşı daha az duyarlıdır, ancak tamamen bağışık değildir.

**Çıkarım**

SLM'lerin küçük boyutu, çıkarım hızında önemli avantaj sağlar ve geniş paralel işlem gerektirmeden yerel donanımda verimli çıktı üretmelerine olanak tanır. LLM'ler ise boyutları ve karmaşıklıkları nedeniyle kabul edilebilir çıkarım süreleri elde etmek için büyük paralel hesaplama kaynaklarına ihtiyaç duyar. Çok sayıda eşzamanlı kullanıcı olduğunda, LLM'lerin yanıt süreleri, özellikle büyük ölçekli dağıtımlarda daha da yavaşlayabilir.

Özetle, LLM'ler ve SLM'ler makine öğrenimi temelinde ortak bir yapıya sahip olsa da, model büyüklüğü, kaynak gereksinimleri, bağlamsal anlayış, önyargıya yatkınlık ve çıkarım hızı açısından önemli farklılıklar gösterirler. Bu farklılıklar, LLM'lerin daha çok yönlü ancak kaynak açısından ağır, SLM'lerin ise alan odaklı ve daha az hesaplama gerektiren verimli çözümler sunduğunu yansıtır.

***Not: Bu derste, SLM örneği olarak Microsoft Phi-3 / 3.5 kullanılacaktır.***

## Phi-3 / Phi-3.5 Ailesine Giriş

Phi-3 / 3.5 Ailesi, esas olarak metin, görsel ve Agent (MoE) uygulama senaryolarını hedefler:

### Phi-3 / 3.5 Instruct

Başlıca metin üretimi, sohbet tamamlama ve içerik bilgi çıkarımı gibi görevler için.

**Phi-3-mini**

3.8B parametreli dil modeli Microsoft Azure AI Studio, Hugging Face ve Ollama platformlarında bulunmaktadır. Phi-3 modelleri, eşit ve daha büyük boyutlu dil modellerini temel kıyaslamalarda önemli ölçüde geride bırakır (aşağıdaki kıyaslama rakamlarına bakınız, yüksek rakamlar daha iyidir). Phi-3-mini, kendi boyutunun iki katı büyüklüğündeki modelleri geride bırakırken, Phi-3-small ve Phi-3-medium GPT-3.5 dahil daha büyük modellerden daha üstün sonuçlar elde eder.

**Phi-3-small ve medium**

Sadece 7B parametreye sahip Phi-3-small, çeşitli dil, akıl yürütme, kodlama ve matematik kriterlerinde GPT-3.5T'yi geçer.

14B parametreli Phi-3-medium bu trendi sürdürür ve Gemini 1.0 Pro modelini geride bırakır.

**Phi-3.5-mini**

Phi-3-mini'nin bir yükseltmesi olarak düşünülebilir. Parametre sayısı değişmez, ancak çoklu dil desteği geliştirilmiş (20+ dili destekler: Arapça, Çince, Çekçe, Danca, Felemenkçe, İngilizce, Fince, Fransızca, Almanca, İbranice, Macarca, İtalyanca, Japonca, Korece, Norveççe, Lehçe, Portekizce, Rusça, İspanyolca, İsveççe, Tayca, Türkçe, Ukraynaca) ve uzun bağlam desteği güçlendirilmiştir.

3.8B parametreli Phi-3.5-mini, aynı boyuttaki dil modellerini geride bırakır ve kendi boyutunun iki katı büyüklüğündeki modellerle boy ölçüşür.

### Phi-3 / 3.5 Vision

Phi-3/3.5'in Instruct modeli Phi'nin anlama yeteneği iken, Vision ise Phi'ye dünyayı anlama "gözleri" sağlar.

**Phi-3-Vision**

4.2B parametreye sahip Phi-3-vision, bu trendi sürdürür ve Claude-3 Haiku ve Gemini 1.0 Pro V gibi daha büyük modelleri genel görsel akıl yürütme, OCR, tablo ve diyagram anlama görevlerinde geride bırakır.

**Phi-3.5-Vision**

Phi-3.5-Vision aynı zamanda Phi-3-Vision'ın bir yükseltmesidir, çoklu görüntü desteği ekler. Görmede gelişme olarak düşünebilirsiniz, sadece resimleri değil, aynı zamanda videoları da görebilirsiniz.

Phi-3.5-vision, Claude-3.5 Sonnet ve Gemini 1.5 Flash gibi daha büyük modelleri OCR, tablo ve grafik anlama görevlerinde geride bırakır ve genel görsel bilgi akıl yürütme görevlerinde eşdeğerdir. Çoklu kare girdisini destekler, yani birden fazla giriş görüntüsü üzerinde akıl yürütme yapabilir.

### Phi-3.5-MoE

***Uzman Karışımı (MoE)***, modellerin çok daha az hesaplama ile önceden eğitilmesini sağlar; bu da aynı hesaplama bütçesiyle model ya da veri seti boyutunu dramatik şekilde büyütebileceğiniz anlamına gelir. Özellikle, MoE modeller önceden eğitme sırasında aynı kaliteyi yoğun modellere kıyasla çok daha hızlı elde etmelidir.

Phi-3.5-MoE, 16x3.8B uzman modüllerinden oluşur. Sadece 6.6B aktif parametreye sahip Phi-3.5-MoE, çok daha büyük modeller kadar akıl yürütme, dil anlama ve matematikte benzer seviyede performans gösterir.

Phi-3/3.5 Ailesi modelini farklı senaryolara göre kullanabiliriz. LLM'den farklı olarak Phi-3/3.5-mini veya Phi-3/3.5-Vision'ı uç cihazlarda dağıtabilirsiniz.

## Phi-3/3.5 Ailesi Modelleri Nasıl Kullanılır?

Phi-3/3.5'i farklı senaryolarda kullanmayı planlıyoruz. Sonraki adımda senaryolara göre Phi-3/3.5 kullanacağız.

![phi3](../../../translated_images/tr/phi3.655208c3186ae381.webp)

### Bulut API'leri ile Çıkarım

**GitHub Modelleri**

GitHub Modelleri en doğrudan yoldur. Phi-3/3.5-Instruct modeline GitHub Modelleri üzerinden hızlıca erişebilirsiniz. Azure AI Inference SDK / OpenAI SDK ile birleştirildiğinde API'ye kod yoluyla erişip Phi-3/3.5-Instruct çağrısını tamamlayabilirsiniz. Ayrıca farklı sonuçları Playground üzerinden test edebilirsiniz.

- Demo: Phi-3-mini ve Phi-3.5-mini'nin Çince senaryolardaki karşılaştırması

![phi3](../../../translated_images/tr/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/tr/gh2.07d7985af66f178d.webp)


**Azure AI Studio**

Veya görsel ve MoE modellerini kullanmak istiyorsanız, Azure AI Studio kullanarak çağrıyı tamamlayabilirsiniz. İlgileniyorsanız, Phi-3/3.5 Instruct, Vision, MoE modellerini Azure AI Studio üzerinden nasıl çağıracağınızı öğrenmek için Phi-3 Kullanım Kılavuzu'nu okuyabilirsiniz [Bu bağlantıya tıklayın](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Azure ve GitHub tarafından sağlanan bulut tabanlı Model Kataloğu çözümlerine ek olarak, Phi-3/3.5 Ailesi ile ilgili çağrıları tamamlamak için [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) hizmetini de kullanabilirsiniz. NVIDIA NIM (NVIDIA Inference Microservices), geliştiricilerin yapay zeka modellerini bulutlar, veri merkezleri ve iş istasyonları gibi çeşitli ortamlara verimli şekilde dağıtmasına yardımcı olmak için tasarlanmış hızlandırılmış çıkarım mikroservisleri setidir.

NVIDIA NIM'in bazı temel özellikleri şunlardır:

- **Kolay Dağıtım:** NIM, yapay zeka modellerini tek bir komutla dağıtmaya imkan vererek mevcut iş akışlarına kolay entegrasyon sağlar.
- **Optimum Performans:** TensorRT ve TensorRT-LLM gibi NVIDIA'nın önceden optimize edilmiş çıkarım motorlarını kullanarak düşük gecikme ve yüksek verimlilik sunar.
- **Ölçeklenebilirlik:** Kubernetes üzerinde otomatik ölçeklendirmeyi destekler ve değişken iş yüklerini etkin şekilde yönetir.
- **Güvenlik ve Kontrol:** Kuruluşlar, NIM mikroservislerini kendi yönetilen altyapılarında barındırarak verileri ve uygulamalar üzerinde kontrol sahibi olabilirler.
- **Standart API'ler:** NIM, chatbotlar, AI asistanları ve daha fazlası gibi yapay zeka uygulamaları oluşturmayı ve entegre etmeyi kolaylaştıran sektör standartı API'ler sağlar.

NIM, NVIDIA GPU'larda verimli çalışmayı garanti ederek AI modellerinin dağıtımını ve operasyonunu basitleştirmeyi amaçlayan NVIDIA AI Enterprise'ın bir parçasıdır.

- Demo: NVIDIA NIM kullanarak Phi-3.5-Vision-API çağırma [[Buraya tıklayın](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Phi-3/3.5'i Yerelde Çalıştırma
Phi-3 veya GPT-3 gibi herhangi bir dil modeline ilişkin çıkarım, aldığı girdiye dayanarak yanıtlar veya tahminler üretme sürecini ifade eder. Phi-3’e bir istem ya da soru verdiğinizde, eğitildiği verilerdeki desenleri ve ilişkileri analiz ederek en olası ve ilgili yanıtı çıkarır.

**Hugging Face Transformer**  
Hugging Face Transformers, doğal dil işleme (NLP) ve diğer makine öğrenimi görevleri için tasarlanmış güçlü bir kütüphanedir. İşte bazı önemli noktalar:

1. **Önceden Eğitilmiş Modeller:** Metin sınıflandırma, isim tanıma, soru yanıtlama, özetleme, çeviri ve metin üretimi gibi çeşitli görevler için kullanılabilen binlerce önceden eğitilmiş model sunar.

2. **Çerçeve Uyumluluğu:** Kütüphane, PyTorch, TensorFlow ve JAX gibi birçok derin öğrenme çerçevesini destekler. Bu, bir modeli bir çerçevede eğitip başka bir çerçevede kullanmanıza olanak tanır.

3. **Çok Modlu Yetenekler:** NLP’nin yanı sıra Hugging Face Transformers, bilgisayar görüşü (ör. görüntü sınıflandırma, nesne algılama) ve ses işleme (ör. konuşma tanıma, ses sınıflandırma) görevlerini de destekler.

4. **Kullanım Kolaylığı:** Modelleri kolayca indirip ince ayar yapmanıza olanak tanıyan API'ler ve araçlar sunar, hem yeni başlayanlara hem de uzmanlara erişilebilir kılar.

5. **Topluluk ve Kaynaklar:** Hugging Face, canlı bir topluluğa ve kullanıcıların başlamasına ve kütüphaneyi en iyi şekilde kullanmasına yardımcı olacak kapsamlı dokümantasyon, eğitimler ve rehberler sağlar.  
[resmi dokümantasyon](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) veya [GitHub deposu](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Bu en yaygın kullanılan yöntemdir, ancak GPU hızlandırması gerektirir. Sonuçta, Vision ve MoE gibi senaryolar çok sayıda hesaplama gerektirir ve kuantize edilmezlerse CPU üzerinde çok yavaş çalışır.

- Demo: Transformer ile Phi-3.5-Instruct çağırma [Buraya tıklayın](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformer ile Phi-3.5-Vision çağırma [Buraya tıklayın](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Transformer ile Phi-3.5-MoE çağırma [Buraya tıklayın](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**  
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), büyük dil modellerini (LLM) yerel olarak makinenizde çalıştırmayı kolaylaştırmak için tasarlanmış bir platformdur. Llama 3.1, Phi 3, Mistral ve Gemma 2 gibi çeşitli modelleri destekler. Platform, model ağırlıkları, yapılandırma ve verileri tek bir paket halinde sunarak kullanıcıların kendi modellerini özelleştirmesini ve oluşturmasını kolaylaştırır. Ollama macOS, Linux ve Windows için mevcuttur. Bulut hizmetlerine güvenmeden LLM’lerle denemeler yapmak veya dağıtım yapmak istiyorsanız harika bir araçtır. Ollama en doğrudan yol olup, aşağıdaki komutu çalıştırmanız yeterlidir.

```bash

ollama run phi3.5

```


**GenAI için ONNX Runtime**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst), çok platformlu çıkarım ve eğitim için bir makine öğrenmesi hızlandırıcısıdır. GenAI için ONNX Runtime (GENAI), farklı platformlarda üretken AI modellerini verimli şekilde çalıştırmanıza yardımcı olan güçlü bir araçtır.

## ONNX Runtime Nedir?  
ONNX Runtime, makine öğrenmesi modellerinin yüksek performanslı çıkarımını sağlayan açık kaynaklı bir projedir. Open Neural Network Exchange (ONNX) formatındaki modelleri destekler; ONNX, makine öğrenmesi modellerinin gösterimi için standarttır. ONNX Runtime çıkarımı, PyTorch ve TensorFlow/Keras gibi derin öğrenme çerçevelerinin yanı sıra scikit-learn, LightGBM, XGBoost gibi klasik makine öğrenimi kütüphanelerini destekleyen modeller için daha hızlı müşteri deneyimleri ve daha düşük maliyetler sağlar. ONNX Runtime farklı donanımlar, sürücüler ve işletim sistemleri ile uyumludur ve uygun olduğu durumlarda donanım hızlandırıcılarını kullanarak grafik optimizasyonları ve dönüşümleri sayesinde optimal performans sunar.

## Üretken AI Nedir?  
Üretken AI, eğitildiği verilere dayanarak metin, görüntü veya müzik gibi yeni içerik üretebilen yapay zeka sistemlerini ifade eder. Örnekler arasında GPT-3 gibi dil modelleri ve Stable Diffusion gibi görüntü üretim modelleri bulunur. ONNX Runtime için GenAI kitaplığı, ONNX modelleri için üretken AI döngüsünü sağlar; bu, ONNX Runtime ile çıkarım, logits işleme, arama ve örnekleme, KV önbellek yönetimi gibi özellikleri içerir.

## GENAI için ONNX Runtime  
GENAI için ONNX Runtime, ONNX Runtime yeteneklerini üretken AI modellerini destekleyecek şekilde genişletir. İşte bazı temel özellikler:

- **Geniş Platform Desteği:** Windows, Linux, macOS, Android ve iOS gibi çeşitli platformlarda çalışır.
- **Model Desteği:** LLaMA, GPT-Neo, BLOOM ve daha birçok popüler üretken AI modelini destekler.
- **Performans Optimizasyonu:** NVIDIA GPU’lar, AMD GPU’lar ve daha fazlası gibi farklı donanım hızlandırıcılar için optimizasyonlar sunar.
- **Kullanım Kolaylığı:** Uygulamalara kolay entegrasyon için API’ler sağlar; böylece minimal kod ile metin, görüntü ve diğer içerikler üretilebilir.
- Kullanıcılar üst düzey generate() yöntemini çağırabilir veya döngü içinde modelin her yinelemesini çalıştırarak token token çıktı üretebilir ve üretim parametrelerini döngü içinde isteğe bağlı olarak güncelleyebilir.
- ONNX Runtime, token dizileri üretmek için greedy/beam araması ve TopP, TopK örneklemesini destekler; tekrarlama cezaları gibi yerleşik logits işlemleri vardır. Ayrıca kolayca özel skorlamalar ekleyebilirsiniz.

## Başlarken  
GENAI için ONNX Runtime ile başlamak için şu adımları izleyebilirsiniz:

### ONNX Runtime Yükleyin:  
```Python
pip install onnxruntime
```
### Üretken AI Uzantılarını Yükleyin:  
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

ONNX Runtime ve Ollama referans yöntemlerine ek olarak, farklı üreticilerin sağladığı model referans yöntemlerine dayanan kuantitatif modellerin referansını da tamamlayabiliriz. Örneğin Apple Metal ile Apple MLX çerçevesi, Qualcomm QNN ile NPU, Intel OpenVINO ile CPU/GPU vb. Daha fazla içeriği [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst) adresinden edinebilirsiniz.


## Daha Fazla

Phi-3/3.5 Ailesinin temellerini öğrendik, ancak SLM hakkında daha fazlasını öğrenmek için daha fazla bilgiye ihtiyacımız var. Yanıtları Phi-3 Cookbook’ta bulabilirsiniz. Daha fazla bilgi edinmek isterseniz, lütfen [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst) ziyaret edin.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->