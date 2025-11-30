<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "807f0d9fc1747e796433534e1be6a98a",
  "translation_date": "2025-10-17T16:21:45+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "tr"
}
-->
[![Açık Kaynak Modeller](../../../translated_images/18-lesson-banner.f30176815b1a5074fce9cceba317720586caa99e24001231a92fd04eeb54a121.tr.png)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# LLM'inizi İnce Ayar Yapma

Büyük dil modellerini kullanarak üretken yapay zeka uygulamaları oluşturmak yeni zorlukları beraberinde getirir. Önemli bir konu, modelin belirli bir kullanıcı isteği için ürettiği içeriğin yanıt kalitesini (doğruluk ve alaka düzeyi) sağlamaktır. Önceki derslerde, mevcut modeli _girdi istemini değiştirerek_ bu sorunu çözmeye çalışan istem mühendisliği ve bilgi alma ile artırılmış üretim gibi teknikleri tartıştık.

Bugünkü derste, bu zorluğu _modeli kendisini ek verilerle yeniden eğiterek_ çözmeye çalışan üçüncü bir teknik olan **ince ayar yapmayı** ele alıyoruz. Detaylara dalalım.

## Öğrenme Hedefleri

Bu ders, önceden eğitilmiş dil modelleri için ince ayar yapma kavramını tanıtır, bu yaklaşımın faydalarını ve zorluklarını keşfeder ve üretken yapay zeka modellerinizin performansını artırmak için ince ayar yapmayı ne zaman ve nasıl kullanacağınız konusunda rehberlik sağlar.

Bu dersin sonunda şu soruları yanıtlayabilecek durumda olmalısınız:

- Dil modelleri için ince ayar nedir?
- İnce ayar ne zaman ve neden faydalıdır?
- Önceden eğitilmiş bir model nasıl ince ayar yapılabilir?
- İnce ayar yapmanın sınırlamaları nelerdir?

Hazır mısınız? Hadi başlayalım.

## Resimli Kılavuz

Derinlemesine dalmadan önce ele alacağımız konuların genel bir özetini görmek ister misiniz? Bu ders için öğrenme yolculuğunu - ince ayar yapmanın temel kavramlarını ve motivasyonunu öğrenmekten, süreci ve ince ayar görevini yürütmek için en iyi uygulamaları anlamaya kadar - açıklayan resimli kılavuza göz atın. Bu keşif için büyüleyici bir konu, bu yüzden kendi kendine öğrenme yolculuğunuzu desteklemek için ek bağlantılar içeren [Kaynaklar](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) sayfasını kontrol etmeyi unutmayın!

![Dil Modellerine İnce Ayar Yapma için Resimli Kılavuz](../../../translated_images/18-fine-tuning-sketchnote.11b21f9ec8a703467a120cb79a28b5ac1effc8d8d9d5b31bbbac6b8640432e14.tr.png)

## Dil modelleri için ince ayar nedir?

Tanım olarak, büyük dil modelleri internet dahil çeşitli kaynaklardan alınan büyük miktarda metin üzerinde _önceden eğitilmiştir_. Önceki derslerde öğrendiğimiz gibi, modelin kullanıcı sorularına ("istemlere") verdiği yanıtların kalitesini artırmak için _istem mühendisliği_ ve _bilgi alma ile artırılmış üretim_ gibi tekniklere ihtiyaç duyarız.

Popüler bir istem mühendisliği tekniği, modele yanıtın ne olması gerektiği konusunda daha fazla rehberlik sağlamak için ya _talimatlar_ (açık rehberlik) ya da _birkaç örnek vermek_ (örtük rehberlik) içerir. Bu, _az örnekli öğrenme_ olarak adlandırılır ancak iki sınırlaması vardır:

- Modelin token sınırları, verebileceğiniz örnek sayısını sınırlayabilir ve etkinliği azaltabilir.
- Modelin token maliyetleri, her isteme örnek eklemeyi pahalı hale getirebilir ve esnekliği sınırlayabilir.

İnce ayar yapma, önceden eğitilmiş bir modeli alıp yeni verilerle yeniden eğiterek belirli bir görevdeki performansını artırdığımız makine öğrenimi sistemlerinde yaygın bir uygulamadır. Dil modelleri bağlamında, önceden eğitilmiş modeli _belirli bir görev veya uygulama alanı için özenle seçilmiş bir örnek setiyle_ ince ayar yaparak, bu belirli görev veya alan için daha doğru ve alakalı olabilecek bir **özel model** oluşturabiliriz. İnce ayar yapmanın yan faydalarından biri, az örnekli öğrenme için gereken örnek sayısını azaltarak token kullanımını ve ilgili maliyetleri düşürebilmesidir.

## Modelleri ne zaman ve neden ince ayar yapmalıyız?

_Bu_ bağlamda, ince ayar yapmaktan bahsettiğimizde, yeniden eğitimin **orijinal eğitim veri setinin bir parçası olmayan yeni veriler eklenerek** yapıldığı **denetimli** ince ayar yapmayı kastediyoruz. Bu, modelin orijinal veriler üzerinde ancak farklı hiperparametrelerle yeniden eğitildiği denetimsiz ince ayar yaklaşımından farklıdır.

Unutulmaması gereken önemli şey, ince ayar yapmanın istenen sonuçları elde etmek için belirli bir uzmanlık düzeyi gerektiren ileri düzey bir teknik olduğudur. Yanlış yapılırsa, beklenen iyileştirmeleri sağlamayabilir ve hatta modelin hedeflenen alan için performansını düşürebilir.

Bu nedenle, dil modellerine "nasıl" ince ayar yapacağınızı öğrenmeden önce, bu yolu neden seçmeniz gerektiğini ve ince ayar yapma sürecine "ne zaman" başlamanız gerektiğini bilmelisiniz. Kendinize şu soruları sorun:

- **Kullanım Durumu**: İnce ayar yapma için _kullanım durumunuz_ nedir? Mevcut önceden eğitilmiş modelin hangi yönünü geliştirmek istiyorsunuz?
- **Alternatifler**: İstenen sonuçları elde etmek için _diğer teknikleri_ denediniz mi? Bunları karşılaştırma için bir temel oluşturmak için kullanın.
  - İstem mühendisliği: İlgili istem yanıtlarının örnekleriyle az örnekli istem tekniklerini deneyin. Yanıtların kalitesini değerlendirin.
  - Bilgi Alma ile Artırılmış Üretim: İstemleri verilerinizi arayarak alınan sorgu sonuçlarıyla artırmayı deneyin. Yanıtların kalitesini değerlendirin.
- **Maliyetler**: İnce ayar yapmanın maliyetlerini belirlediniz mi?
  - Ayarlanabilirlik - önceden eğitilmiş model ince ayar için uygun mu?
  - Çaba - eğitim verilerini hazırlama, modeli değerlendirme ve iyileştirme için gereken çaba.
  - Hesaplama - ince ayar görevlerini çalıştırma ve ince ayar yapılmış modeli dağıtma için gereken hesaplama.
  - Veri - ince ayar etkisi için yeterli kaliteli örneklere erişim.
- **Faydalar**: İnce ayar yapmanın faydalarını doğruladınız mı?
  - Kalite - ince ayar yapılmış model temel modeli geride bıraktı mı?
  - Maliyet - istemleri basitleştirerek token kullanımını azaltıyor mu?
  - Genişletilebilirlik - temel modeli yeni alanlar için yeniden kullanabilir misiniz?

Bu soruları yanıtlayarak, ince ayar yapmanın kullanım durumunuz için doğru yaklaşım olup olmadığını belirleyebilirsiniz. İdeal olarak, yaklaşım yalnızca faydalar maliyetlerden ağır basıyorsa geçerlidir. Devam etmeye karar verdiğinizde, önceden eğitilmiş modele _nasıl_ ince ayar yapabileceğinizi düşünme zamanı gelmiştir.

Karar verme süreci hakkında daha fazla bilgi mi almak istiyorsunuz? [İnce ayar yapmalı mı yapmamalı mı](https://www.youtube.com/watch?v=0Jo-z-MFxJs) videosunu izleyin.

## Önceden eğitilmiş bir modele nasıl ince ayar yapabiliriz?

Önceden eğitilmiş bir modele ince ayar yapmak için şunlara sahip olmanız gerekir:

- ince ayar yapılacak önceden eğitilmiş bir model
- ince ayar için kullanılacak bir veri seti
- ince ayar görevini çalıştırmak için bir eğitim ortamı
- ince ayar yapılmış modeli dağıtmak için bir barındırma ortamı

## İnce Ayar Yapma Uygulamada

Aşağıdaki kaynaklar, seçilen bir model ve özenle seçilmiş bir veri seti kullanarak gerçek bir örneği adım adım anlatan eğitimler sağlar. Bu eğitimleri tamamlamak için ilgili sağlayıcıda bir hesaba ve ilgili model ve veri setlerine erişime ihtiyacınız vardır.

| Sağlayıcı    | Eğitim                                                                                                                                                                       | Açıklama                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Chat modellerine nasıl ince ayar yapılır](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst) | `gpt-35-turbo` modeline belirli bir alan ("tarif asistanı") için ince ayar yapmayı öğrenin: eğitim verilerini hazırlama, ince ayar görevini çalıştırma ve ince ayar yapılmış modeli çıkarım için kullanma.                                                                                                                                                                                                                      |
| Azure OpenAI | [GPT 3.5 Turbo ince ayar eğitimi](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Eğitim verilerini oluşturma ve yükleme, ince ayar görevini çalıştırma adımlarını izleyerek **Azure'da** bir `gpt-35-turbo-0613` modeline ince ayar yapmayı öğrenin. Yeni modeli dağıtın ve kullanın.                                                                                                                                                                                                                              |
| Hugging Face | [Hugging Face ile LLM'lere ince ayar yapma](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                      | Bu blog yazısı, [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) kütüphanesi ve [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst]) ile açık [veri setleri](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) kullanarak bir _açık LLM_ (ör: `CodeLlama 7B`) modeline ince ayar yapmayı anlatır. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [AutoTrain ile LLM'lere ince ayar yapma](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                | AutoTrain (veya AutoTrain Advanced), Hugging Face tarafından geliştirilen ve LLM ince ayarını içeren birçok farklı görev için ince ayar yapılmasına olanak tanıyan bir Python kütüphanesidir. AutoTrain, kodsuz bir çözümdür ve ince ayar kendi bulutunuzda, Hugging Face Spaces üzerinde veya yerel olarak yapılabilir. Hem web tabanlı bir GUI, CLI ve yaml yapılandırma dosyalarıyla eğitim desteği sunar.                                                |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Ödev

Yukarıdaki eğitimlerden birini seçin ve adımları izleyin. _Bu repo içinde bu eğitimlerin bir versiyonunu yalnızca referans için Jupyter Notebooks'ta çoğaltabiliriz. En son sürümleri almak için lütfen doğrudan orijinal kaynakları kullanın_.

## Harika İş! Öğrenmeye Devam Edin.

Bu dersi tamamladıktan sonra, Üretken Yapay Zeka bilginizi geliştirmeye devam etmek için [Üretken Yapay Zeka Öğrenme koleksiyonumuzu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kontrol edin!

Tebrikler!! Bu kursun v2 serisinden son dersi tamamladınız! Öğrenmeyi ve inşa etmeyi bırakmayın. **Bu konuyla ilgili ek öneriler listesi için [KAYNAKLAR](RESOURCES.md?WT.mc_id=academic-105485-koreyst) sayfasına göz atın.**

v1 ders serimiz de daha fazla ödev ve kavramlarla güncellendi. Bu yüzden bilginizi tazelemek için bir dakikanızı ayırın - ve lütfen [sorularınızı ve geri bildirimlerinizi paylaşın](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) topluluk için bu dersleri geliştirmemize yardımcı olun.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmez.