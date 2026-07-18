[![Açık Kaynak Modeller](../../../translated_images/tr/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# LLM'nizi İnce Ayarlama

Büyük dil modellerini kullanarak üretken yapay zeka uygulamaları geliştirmek, yeni zorlukları beraberinde getirir. Temel bir sorun, modele verilen kullanıcı isteği doğrultusunda oluşturulan içeriğin yanıt kalitesini (doğruluk ve alaka) sağlamaktır. Önceki derslerde, mevcut modele _girdi istemini değiştirme_ yoluyla problemi çözmeye çalışan prompt mühendisliği ve retrieval-augmentasyonlu üretim gibi teknikleri tartıştık.

Bugünkü derste, üçüncü bir teknik olan **ince ayarlama**yı tartışıyoruz; bu teknik, ek verilerle _modeli kendisini yeniden eğitme_ yoluyla zorluğu çözmeye çalışır. Detaylara dalalım.

## Öğrenme Hedefleri

Bu ders, önceden eğitilmiş dil modelleri için ince ayarlama kavramını tanıtır, bu yaklaşımın faydalarını ve zorluklarını keşfeder ve üretken yapay zeka modellerinizin performansını artırmak için ince ayarlamayı ne zaman ve nasıl kullanacağınıza dair rehberlik sağlar.

Dersin sonunda, aşağıdaki soruları yanıtlayabilmeniz beklenir:

- Dil modelleri için ince ayarlama nedir?
- İnce ayarlama ne zaman ve neden yararlıdır?
- Önceden eğitilmiş bir modeli nasıl ince ayarlayabilirim?
- İnce ayarlamanın sınırlamaları nelerdir?

Hazır mısınız? Haydi başlayalım.

## Görselleştirilmiş Rehber

Konuya girmeden önce neyi kapsayacağımızın genel resmini görmek ister misiniz? Bu dersin öğrenme yolculuğunu anlatan görselleştirilmiş rehbere göz atın - ince ayarlamanın temel kavramlarını ve motivasyonunu öğrenmekten proses ve en iyi uygulamaları anlamaya kadar. Bu keşif için büyüleyici bir konu, bu yüzden kendi kendinize öğrenme yolculuğunuzu desteklemek için ek bağlantılar içeren [Kaynaklar](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) sayfasını unutmayın!

![Dil Modellerini İnce Ayarlamaya Görsel Rehber](../../../translated_images/tr/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Dil modelleri için ince ayarlama nedir?

Tanımı gereği, büyük dil modelleri internet dahil çeşitli kaynaklardan alınan büyük metin miktarları üzerinde _önceden eğitilmiştir_. Önceki derslerde öğrendiğimiz gibi, kullanıcının sorularına ("promplar") verilen yanıtların kalitesini artırmak için _prompt mühendisliği_ ve _retrieval-augmentasyonlu üretim_ gibi tekniklere ihtiyacımız vardır.

Popüler bir prompt mühendisliği tekniği, modele yanıt beklentisi hakkında daha fazla rehberlik vermek için _talimatlar_ (açık rehberlik) sağlamak veya _birkaç örnek vermek_ (örtük rehberlik) içerir. Bu, _few-shot learning_ olarak adlandırılır ancak iki sınırlamaya sahiptir:

- Model token sınırları verebileceğiniz örnek sayısını kısıtlayabilir ve etkinliği sınırlar.
- Model token maliyetleri, her prompt için örnek eklemeyi pahalı hale getirebilir ve esnekliği sınırlar.

İnce ayarlama, önceden eğitilmiş bir modeli belirli bir görevde performansını artırmak için yeni verilerle yeniden eğitmek için yaygın bir makine öğrenimi uygulamasıdır. Dil modelleri bağlamında, önceden eğitilmiş modeli _belirli bir görev veya uygulama alanı için özenle seçilmiş örnekler kümesi ile_ ince ayarlayarak o alana özgü daha doğru ve alakalı olabilecek **özel bir model** oluşturabiliriz. İnce ayarlamanın yan faydası, few-shot learning için gereken örnek sayısını azaltarak token kullanımını ve ilgili maliyetleri düşürmesidir.

## Modelleri ne zaman ve neden ince ayarlamalıyız?

_Bu_ bağlamda, ince ayarlamadan bahsederken, yeniden eğitimin orijinal eğitim veri setinin parçası olmayan **yeni veri eklenerek** yapıldığı **denetimli** ince ayarlamadan söz ediyoruz. Bu, modelin orijinal veriler üzerinde fakat farklı hiperparametrelerle yeniden eğitildiği denetimsiz ince ayarlama yaklaşımından farklıdır.

Hatırlanması gereken önemli şey, ince ayarlamanın istenen sonuçları elde etmek için belirli bir uzmanlık seviyesi gerektiren gelişmiş bir teknik olduğudur. Yanlış yapılırsa, beklenen iyileştirmeleri sağlamayabilir ve hatta hedeflenen alan için model performansını bozabilir.

Bu nedenle, "dil modellerini nasıl ince ayarlayacağınızı" öğrenmeden önce, "neden" bu yolu seçmeniz gerektiğini ve "ne zaman" ince ayarlama sürecine başlamanız gerektiğini bilmelisiniz. Kendinize şu soruları sorun:

- **Kullanım Durumu**: İnce ayarlama için sizin _kullanım durumunuz_ nedir? Mevcut önceden eğitilmiş modelin hangi yönünü geliştirmek istiyorsunuz?
- **Alternatifler**: İstenen sonuçlara ulaşmak için _başka teknikleri_ denediniz mi? Karşılaştırma için bir temel oluşturmak üzere bunları kullanın.
  - Prompt mühendisliği: İlgili prompt yanıtları ile few-shot prompting gibi teknikleri deneyin. Yanıtların kalitesini değerlendirin.
  - Retrieval Augmented Generation: Verilerinizi arama yoluyla geri getirilen sorgu sonuçları ile promptları artırmayı deneyin. Yanıtların kalitesini değerlendirin.
- **Maliyetler**: İnce ayarlamanın maliyetlerini belirlediniz mi?
  - Ayarlanabilirlik - önceden eğitilmiş model ince ayarlamaya uygun mu?
  - Çaba - eğitim verilerini hazırlama, modeli değerlendirme ve iyileştirme için gereken süreç.
  - Hesaplama - ince ayarlama işlerini çalıştırma ve ince ayarlanmış modeli dağıtma için gereken kaynaklar.
  - Veri - ince ayarlamanın etkisi için yeterli kalitede örneklere erişim.
- **Faydalar**: İnce ayarlamanın faydalarını doğruladınız mı?
  - Kalite - ince ayarlanmış model temel modeli geçti mi?
  - Maliyet - promptları basitleştirerek token kullanımını azaltıyor mu?
  - Genişletilebilirlik - temel modeli yeni alanlara uyarlayabilir misiniz?

Bu soruları yanıtlayarak, ince ayarlamanın sizin kullanım durumunuz için doğru yaklaşım olup olmadığına karar verebilmelisiniz. İdeal olarak, yaklaşım yalnızca faydalar maliyetlerden yüksekse geçerlidir. Devam etmeye karar verdiğinizde, önceden eğitilmiş modeli _nasıl_ ince ayarlayabileceğinizi düşünme zamanı gelmiştir.

Karar verme süreci hakkında daha fazla bilgi edinmek ister misiniz? [İnce ayarlamalı mı, ince ayarlamamalı mı](https://www.youtube.com/watch?v=0Jo-z-MFxJs) videosunu izleyin.

## Önceden Eğitilmiş Model Nasıl İnce Ayarlanır?

Önceden eğitilmiş bir modeli ince ayarlamak için şunlara ihtiyacınız vardır:

- İnce ayar yapılacak önceden eğitilmiş model
- İnce ayarlama için kullanılacak veri seti
- İnce ayarlama işini çalıştıracak eğitim ortamı
- İnce ayarlı modeli dağıtmak için barındırma ortamı

## Microsoft Foundry Üzerinde İnce Ayarlama

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), Azure üzerinde özel modellerin ince ayarını, dağıtımını ve yönetimini yaptığınız yerdir (önceden Azure OpenAI Studio ve Azure AI Studio olarak ayrı olanları bir araya getirir). Bir iş başlatmadan önce, Foundry'nin size sunduğu seçenekleri ve platformun önerdiği en iyi uygulamaları anlamak faydalıdır. Alt yapıda Foundry, modelleri verimli biçimde ince ayarlamak için **LoRA (düşük sıra uyarlama)** kullanır; böylece her ağırlığın yeniden eğitilmesinden daha hızlı ve uygun maliyetli bir eğitim sağlanır.

### 1. Adım: Eğitim Tekniği Seçin

Foundry üç ince ayarlama tekniğini destekler. **SFT ile başlayın** - en geniş senaryo yelpazesini kapsar.

| Teknik | Ne Yapar | Ne Zaman Kullanılır |
| --- | --- | --- |
| **Denetimli İnce Ayarlama (SFT)** | Modeli istediğiniz yanıtları üretmeyi öğrenmesi için giriş/çıkış örnek çiftleriyle eğitir. | Çoğu görev için varsayılan: alan uzmanlığı, görev performansı, stil ve ton, talimat izleme ve dil uyarlaması. |
| **Doğrudan Tercih Optimizasyonu (DPO)** | _Tercih edilen ve edilmeyen_ yanıt çiftlerinden öğrenerek çıktıları insan tercihleriyle hizalar. | Karşılaştırmalı geri bildirim olduğunda yanıt kalitesi, güvenlik ve hizalamayı iyileştirmek için. |
| **Pekiştirmeli İnce Ayarlama (RFT)** | _Derecelendiricilerden_ gelen ödül sinyallerini kullanan pekiştirmeli öğrenmeyle karmaşık davranışları optimize eder. | Objektif, mantık ağırlıklı alanlar (matematik, kimya, fizik) için, doğru/yanlış cevapların belli olduğu durumlar. Daha fazla ML uzmanlığı gerektirir. |

### 2. Adım: Eğitim Seviyesi Seçin

Foundry, eğitimin nasıl ve nerede yapılacağını seçmenize izin verir:

- **Standart** - kaynak bölgenizde eğitim yapar ve veri yerel olmasını garanti eder. Verinin belli bir bölgede kalması gerektiğinde kullanın.
- **Global** - bölgenizin dışındaki kapasiteyi kullanarak daha ucuz ve hızlı sıraya alma sağlar (veriler ve ağırlıklar eğitimin yapıldığı bölgeye kopyalanır). Veri yerel olmaması durumunda iyi bir varsayılan.
- **Geliştirici** - en düşük maliyet, boş kapasite kullanır, gecikme/SLA garantisi yoktur (işler kesilebilir ve devam ettirilebilir). Deneyler için ideal.

### 3. Adım: Temel Modeli Seçin

İnce ayarlanabilir modeller arasında OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini`, ve `gpt-4.1-nano` (SFT; 4o/4.1 ailesi ayrıca DPO'yu destekler), akıl yürütme modelleri `o4-mini` ve `gpt-5` (RFT), ayrıca açık kaynak modeller `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct` ve `gpt-oss-20b` (Foundry kaynaklarında SFT) bulunur. Desteklenen yöntemler, bölgeler ve kullanılabilirlik için güncel [İnce Ayarlama Model Listesi](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) sayfasını her zaman kontrol edin.

> Foundry iki mod sunar: **sunucusuz** (tüketim bazlı fiyatlandırma, GPU kotası yönetimi yok, OpenAI ve seçili modeller) ve **yönetilen hesaplama** (en geniş model yelpazesi için Azure Machine Learning ile kendi VM'lerinizi getirirsiniz). Çoğu kişi sunucusuzla başlamalıdır.

### Foundry en iyi uygulamalar

- **İlk olarak baz modeli ölçün.** İnce ayar yapmadan önce prompt mühendisliği ve RAG ile temel modeli ölçerek kazancı kanıtlayın.
- **Küçük başlayıp sonra büyütün.** Yaklaşımı doğrulamak için 50-100 kaliteli örnekle başlayın, sonra üretimde 500+ örneğe çıkın. Kalite miktardan önemlidir - düşük kaliteli örnekleri eleyin.
- **Veriyi doğru formatlayın.** Eğitim ve doğrulama dosyaları JSONL, UTF-8 **BOM ile**, 512 MB altında, sohbet-tamamlamaları mesaj formatında olmalı. Aşırı uyum için doğrulama dosyası mutlaka ekleyin.
- **Eğitim sırasında kullandığınız sistem istemini çıkarımda da kullanın.** Eğitme sırasında kullandığınız sistem mesajını model çağrısında da kullanın.
- **Kontrol noktalarını değerlendirin - sonuncuyu körü körüne dağıtmayın.** Foundry son üç epoch'u dağıtılabilir kontrol noktaları olarak tutar; `train_loss` / `valid_loss` ve token doğruluğunu izleyerek en iyi genelleştiren seçin.
- **İnce ayarlı modeli temel modelle karşılaştırırken kalite ile birlikte token maliyetini ölçün.**
- **Sürekli ince ayarlama ile yineleyin.** Önceden ince ayarlanan bir modeli yeni verilerle tekrar ince ayarlayabilirsiniz (OpenAI modellerinde desteklenir).
- **Barındırma maliyetlerini göz önünde bulundurun.** Dağıtılan özel model saatlik faturalandırılır, ve kullanılmayan dağıtım 15 gün sonra kaldırılır - ihtiyacınız olmayanları temizleyin.

[Bir modeli ince ayarlama ile özelleştirme](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) öğreticisi üzerinden baştan sona çalışın ve diğer teknikler için [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) ve [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst) kılavuzlarına göz atın.

## İnce Ayarlamanın Uygulamalı Örneği

Aşağıdaki kaynaklar, şu anda desteklenen bir model ve özenle seçilmiş bir veri setiyle gerçek bir örneği adım adım anlatan öğreticiler sağlar. Bunları çalıştırmak için ilgili model ve veri setlerine erişiminizin bulunduğu sağlayıcıda bir hesabınızın olması gerekir.

| Sağlayıcı     | Öğretici                                                                                                                                                                       | Açıklama                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Sohbet modellerini nasıl ince ayarlarsınız](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Bir OpenAI sohbet modelini ("tarif asistanı") belirli bir alan için ince ayarlamayı öğrenin: eğitim verisi hazırlama, ince ayarlama işini çalıştırma ve ince ayarlanan modeli çıkarım için kullanma.                                                                                                                                                                                                                                              |
| Microsoft Foundry | [Bir modeli ince ayarlama ile özelleştirme](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Microsoft Foundry üzerinde şu anda desteklenen `gpt-4.1-mini` gibi bir modeli ince ayarlamayı öğrenin: eğitim ve doğrulama verilerini hazırlama ve yükleme, ince ayarlama işini çalıştırma, ardından yeni modeli dağıtma ve kullanma.                                                                                                                                                                                                                                                                 |

| Hugging Face | [Hugging Face ile LLM'lerin İnce Ayarı](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Bu blog yazısı, Hugging Face'deki [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) kütüphanesi ve açık [veri setleri](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) ile [Transformer Takviyeli Öğrenme (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) kullanarak _açık LLM_'nin (örn: `CodeLlama 7B`) ince ayarını yapmanızı adım adım anlatıyor. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [AutoTrain ile LLM'lerin İnce Ayarı](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (veya AutoTrain Advanced), Hugging Face tarafından geliştirilen ve LLM ince ayarı da dahil olmak üzere birçok farklı görev için ince ayar yapılmasını sağlayan bir python kütüphanesidir. AutoTrain, kodsuz bir çözüm sunar ve ince ayar işlemi kendi bulutunuzda, Hugging Face Spaces üzerinde veya yerel olarak yapılabilir. Hem web tabanlı GUI, CLI hem de yaml yapılandırma dosyaları ile eğitim desteklenir.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Unsloth ile LLM'lerin İnce Ayarı](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth, LLM ince ayarı ve takviyeli öğrenmeyi (RL) destekleyen açık kaynak bir çerçevedir. Unsloth, kullanıma hazır [notebook'lar](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) ile yerel eğitim, değerlendirme ve dağıtımı kolaylaştırır. Ayrıca metinden sese (TTS), BERT ve çok modlu modelleri de destekler. Başlamak için adım adım [LLM'lerin İnce Ayarı Rehberi](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) okuyabilirsiniz.                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Ödev

Yukarıdaki eğitimlerden birini seçip adım adım inceleyin. _Bu eğitimlerin bir versiyonunu sadece referans amaçlı olarak bu depoda Jupyter Notebook'larda çoğaltabiliriz. Lütfen en güncel sürümleri almak için orijinal kaynakları doğrudan kullanın_.

## Harika İş! Öğrenmeye Devam Et.

Bu ders tamamlandıktan sonra, [Generative AI Öğrenme koleksiyonumuza](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) göz atarak Üretken AI bilginizi geliştirmeye devam edin!

Tebrikler!! Bu kursun v2 serisindeki son dersi tamamladınız! Öğrenmeyi ve geliştirmeyi bırakmayın. \*\*Sadece bu konu için ek önerilerin bulunduğu listeye ulaşmak için [KAYNAKLAR](RESOURCES.md?WT.mc_id=academic-105485-koreyst) sayfasını kontrol edin.

v1 ders serimiz de daha fazla ödev ve kavramla güncellendi. Bir dakikanızı ayırıp bilginizi tazeleyin - ve lütfen bu dersleri topluluk için geliştirmemize yardımcı olmak adına [sorularınızı ve geri bildirimlerinizi paylaşın](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->