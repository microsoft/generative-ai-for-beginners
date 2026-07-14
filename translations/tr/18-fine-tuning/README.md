[![Open Source Models](../../../translated_images/tr/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# LLM'inizi İnce Ayarlama

Büyük dil modellerini üretken yapay zeka uygulamaları oluşturmak için kullanmak yeni zorlukları beraberinde getirir. Ana mesele, modelin belirli bir kullanıcı isteği için oluşturduğu içeriğin yanıt kalitesini (doğruluk ve alaka) sağlamaktır. Önceki derslerde, var olan modele _girdi olarak verilen istemi değiştirerek_ problemi çözmeye çalışan istem mühendisliği ve bilgi artırımlı üretim gibi teknikleri tartıştık.

Bugünün dersinde, bu zorluğu _modeli kendisini ek verilerle yeniden eğiterek_ ele almaya çalışan üçüncü bir teknik olan **ince ayarlamayı** ele alıyoruz. Detaylara dalalım.

## Öğrenme Hedefleri

Bu ders, önceden eğitilmiş dil modelleri için ince ayarlama kavramını tanıtır, bu yaklaşımın faydalarını ve zorluklarını inceler ve jeneratif yapay zeka modellerinizin performansını artırmak için ince ayarlamayı ne zaman ve nasıl kullanacağınıza dair rehberlik sağlar.

Bu dersin sonunda aşağıdaki soruları yanıtlayabilecek duruma gelmelisiniz:

- Dil modellerinde ince ayarlama nedir?
- İnce ayarlama ne zaman ve neden faydalıdır?
- Önceden eğitilmiş bir modeli nasıl ince ayar yapabilirim?
- İnce ayarlamanın sınırlamaları nelerdir?

Hazır mısınız? Hadi başlayalım.

## Görselleştirilmiş Rehber

Derse başlamadan önce genel resmi görmek ister misiniz? Bu görselleştirilmiş rehbere göz atın; bu rehber, ince ayarlamanın temel kavramlarını ve motivasyonunu öğrenmekten, ince ayarlama görevini yürütmenin süreç ve en iyi uygulamalarını anlamaya kadar öğrenme yolculuğunu anlatır. Bu keşif için büyüleyici bir konudur, bu yüzden kendi başınıza öğrenme yolculuğunuzu desteklemek için ek bağlantılar içeren [Kaynaklar](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) sayfasını unutmayın!

![Dil Modellerinin İnce Ayarlanmasına Görsel Rehber](../../../translated_images/tr/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Dil modellerinde ince ayarlama nedir?

Tanım olarak, büyük dil modelleri internet de dahil olmak üzere çeşitli kaynaklardan alınan büyük miktarda metin üzerinde _önceden eğitilmiştir_. Önceki derslerde öğrendiğimiz gibi, modelin kullanıcının sorularına ("istemlere") verdiği yanıtların kalitesini artırmak için _istem mühendisliği_ ve _bilgi artırımlı üretim_ gibi tekniklere ihtiyacımız vardır.

Popüler bir istem mühendisliği tekniği, modele yanıtın ne olması gerektiği konusunda daha fazla rehberlik vermek için _talimatlar_ (açık rehberlik) sağlamak veya _birkaç örnek vermektir_ (örtük rehberlik). Buna _birkac atışta öğrenme_ denir ancak iki sınırı vardır:

- Model belirteç (token) sınırları, verebileceğiniz örnek sayısını kısıtlayabilir ve etkinliği azaltabilir.
- Model belirteç maliyetleri, her isteme örnek eklemeyi pahalı hale getirebilir ve esnekliği sınırlar.

İnce ayarlama, önceden eğitilmiş bir modeli alıp, belirli bir görevdeki performansını geliştirmek amacıyla yeni verilerle yeniden eğitmek olan makine öğrenimi sistemlerinde yaygın bir uygulamadır. Dil modelleri bağlamında, önceden eğitilmiş modeli _belirli bir görev veya uygulama alanı için özenle seçilmiş örneklerle_ ince ayarlayabiliriz ve böylece o belirli görev veya alan için daha doğru ve alakalı olabilecek **özel bir model** oluşturabiliriz. İnce ayarlamanın yan faydalarından biri de, birkaç atışta öğrenme için gereken örnek sayısını azaltarak belirteç kullanımını ve ilişkili maliyetleri düşürmesidir.

## Modelleri ne zaman ve neden ince ayarlamalıyız?

_Buradaki_ bağlamda, ince ayarlamadan bahsederken, yeniden eğitimin **orijinal eğitim veri setinde yer almayan yeni veriler eklenerek yapılan denetimli** ince ayarlama olduğunu kastediyoruz. Bu, modelin orijinal veriler üzerinde farklı hiperparametrelerle yeniden eğitildiği denetimsiz ince ayarlamadan farklıdır.

Unutulmaması gereken önemli nokta, ince ayarlamanın istenen sonuçları almak için belirli bir uzmanlık seviyesi gerektiren gelişmiş bir teknik olduğudur. Yanlış yapıldığında beklenen iyileştirmeleri sağlamayabilir ve hedeflediğiniz alan için model performansını düşürebilir.

Bu yüzden dil modellerini "nasıl" ince ayarlayacağınızı öğrenmeden önce, bu yolu "neden" seçmeniz gerektiğini ve ince ayarlama sürecine "ne zaman" başlamanız gerektiğini bilmelisiniz. Kendinize şu soruları sorun:

- **Kullanım Durumu**: İnce ayarlama için _kullanım durumunuz_ nedir? Mevcut önceden eğitilmiş modelin hangi yönünü geliştirmek istiyorsunuz?
- **Alternatifler**: İstenen sonuçlara ulaşmak için _başka teknikler_ denediniz mi? Bunları karşılaştırma için bir temel oluşturmak üzere kullanın.
  - İstem mühendisliği: İlgili istem yanıtlarının örnekleriyle birkaç atışta istem tekniklerini deneyin. Yanıt kalitesini değerlendirin.
  - Bilgi Artırımlı Üretim: Verilerinizi arama yoluyla alınan sorgu sonuçlarıyla istemleri artırmayı deneyin. Yanıt kalitesini değerlendirin.
- **Maliyetler**: İnce ayarlama maliyetlerini belirlediniz mi?
  - İncelenebilirlik - önceden eğitilmiş model ince ayarlamaya uygun mu?
  - Çaba - eğitim verisini hazırlama, modeli değerlendirme ve iyileştirme için gereken emek.
  - Hesaplama - ince ayarlama işleri yürütmek ve ince ayarlanmış modeli dağıtmak için gereken işlem gücü.
  - Veri - ince ayarlamanın etkisi için yeterli kalitede örneklere erişim.
- **Faydalar**: İnce ayarlamanın faydalarını doğruladınız mı?
  - Kalite - ince ayarlanmış model temel modeli geçti mi?
  - Maliyet - istemleri basitleştirerek belirteç kullanımını azaltıyor mu?
  - Genişletilebilirlik - temel modeli yeni alanlar için yeniden kullanabilir misiniz?

Bu soruları yanıtlayarak, ince ayarlamanın kullanım durumunuz için uygun olup olmadığına karar verebilirsiniz. İdeal olarak, faydalar maliyetlerden fazla olduğu sürece yaklaşım geçerlidir. Devam etmeye karar verdiğinizde, önceden eğitilmiş modeli _nasıl_ ince ayarlayacağınıza odaklanma zamanı gelmiştir.

Karar verme süreci hakkında daha fazla bilgi edinmek ister misiniz? [İnce ayar yapmalı mı yoksa yapmamalı mı?](https://www.youtube.com/watch?v=0Jo-z-MFxJs) videosunu izleyin.

## Önceden eğitilmiş bir modeli nasıl ince ayarlayabiliriz?

Önceden eğitilmiş bir modeli ince ayarlamak için şunlara ihtiyacınız vardır:

- İnce ayar yapılacak önceden eğitilmiş model
- İnce ayarlama için kullanılacak veri kümesi
- İnce ayarlama işini çalıştırmak için eğitim ortamı
- İnce ayarlanmış modeli dağıtmak için barındırma ortamı

## İnce Ayarlama Uygulamada

> **Not:** Aşağıdaki bazı eğitimlerde referans verilen `gpt-35-turbo` / `gpt-3.5-turbo`, çıkarım ve ince ayar için emekliye ayrılmıştır. Bugün yeni bir ince ayarlama işi başlatıyorsanız, bunun yerine şu an desteklenen bir modeli hedefleyin - örneğin `gpt-4o-mini` veya `gpt-4.1-mini`. Güncel ince ayarlanabilir modeller listesini görmek için [İnce Ayarlama Modelleri Listesine](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) bakabilirsiniz. Bu eğitimlerdeki kavramlar ve adımlar hala geçerlidir.

Aşağıdaki kaynaklar, seçilmiş bir model ve özenle seçilmiş bir veri kümesi kullanarak gerçek bir örnek üzerinden adım adım eğitimler sağlar. Bu eğitimleri uygulamak için, belirli sağlayıcıda hesap sahibi olmanız ve ilgili model ile veri kümelerine erişiminiz olmalıdır.

| Sağlayıcı     | Eğitim                                                                                                                                                                       | Açıklama                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Sohbet modellerini nasıl ince ayarlarım](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Belirli bir alan ("tarif asistanı") için `gpt-35-turbo` modelini eğitimi için veri hazırlayıp ince ayar işini başlatmayı ve ince ayarlanmış modeli çıkarım için kullanmayı öğrenin.                                                                                                                                                                                                                                              |
| Azure OpenAI | [GPT 3.5 Turbo ince ayar eğitimi](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst) | **Azure üzerinde** `gpt-35-turbo-0613` modelini ince ayarlamak için eğitim verisi oluşturup yükleme, ince ayar işini yürütme adımlarını öğrenin. Yeni modeli dağıtın ve kullanın.                                                                                                                                                                                                                                                                 |
| Hugging Face | [Hugging Face ile LLM ince ayarı](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Bu blog yazısı, [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) kütüphanesi ve [Transformer Pekiştirmeli Öğrenme (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) kullanarak Hugging Face üzerinde açık bir LLM'nin (örneğin: `CodeLlama 7B`) nasıl ince ayar yapıldığını anlatır. Ayrıca açık [veri setleri](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) de kullanılmaktadır. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [AutoTrain ile LLM ince ayarı](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (veya AutoTrain Advanced), Hugging Face tarafından geliştirilen ve LLM ince ayarı dahil birçok görev için ince ayar yapılmasını sağlayan python kütüphanesidir. AutoTrain, kod yazmadan bir çözümdür ve ince ayar kendi bulut ortamınızda, Hugging Face Spaces'te veya lokalde yapılabilir. Web tabanlı GUI, CLI ve yaml konfigürasyon dosyaları ile eğitim desteklenir.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Unsloth ile LLM ince ayarı](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth, LLM ince ayarı ve pekiştirmeli öğrenmeyi (RL) destekleyen açık kaynaklı bir çerçevedir. Unsloth, hazır [notebook'lar](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) ile yerel eğitim, değerlendirme ve dağıtımı kolaylaştırır. Ayrıca metin-konuşma (TTS), BERT ve multimodal modelleri destekler. Başlamak için adım adım [LLM İnce Ayar Kılavuzunu](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) okuyun.                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Ödev

Yukarıdaki eğitimlerden birini seçin ve üzerinden geçin. _Bu eğitimlerin bir versiyonunu yalnızca referans amaçlı olarak bu depo içinde Jupyter Notebook'larda çoğaltabiliriz. En güncel sürümleri doğrudan orijinal kaynaklardan kullanınız_.

## Harika İş! Öğrenmeye Devam Edin.

Bu dersi tamamladıktan sonra, jeneratif yapay zeka bilginizi geliştirmeye devam etmek için [Jeneratif AI Öğrenme koleksiyonumuza](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) göz atın!

Tebrikler!! Bu kursun v2 serisindeki son dersi de tamamladınız! Öğrenmeyi ve inşa etmeyi bırakmayın. \*\*Bu konu için ek öneriler listesine ulaşmak için [KAYNAKLAR](RESOURCES.md?WT.mc_id=academic-105485-koreyst) sayfasına göz atın.

v1 ders serimiz de daha fazla ödev ve kavram ile güncellendi. Bilginizi tazelemek için bir dakikanızı ayırın ve lütfen [sorularınızı ve geri bildirimlerinizi paylaşarak](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) bu derslerin topluluk için geliştirilmesine yardımcı olun.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->