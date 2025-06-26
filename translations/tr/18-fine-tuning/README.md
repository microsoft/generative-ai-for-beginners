<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "68664f7e754a892ae1d8d5e2b7bd2081",
  "translation_date": "2025-06-26T00:41:32+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "tr"
}
-->
[![Open Source Models](../../../translated_images/18-lesson-banner.f30176815b1a5074fce9cceba317720586caa99e24001231a92fd04eeb54a121.tr.png)](https://aka.ms/gen-ai-lesson18-gh?WT.mc_id=academic-105485-koreyst)

# LLM'inizi İnce Ayarlama

Büyük dil modellerini kullanarak üretken yapay zeka uygulamaları geliştirmek yeni zorluklar getirir. Ana sorun, modelin belirli bir kullanıcı isteği için ürettiği içeriğin yanıt kalitesini (doğruluk ve alaka düzeyi) sağlamaktır. Önceki derslerde, mevcut modele _girdi istemini değiştirerek_ sorunu çözmeye çalışan istem mühendisliği ve geri getirme ile zenginleştirilmiş üretim gibi teknikleri tartıştık.

Bugünkü dersimizde, ek veri ile _modeli yeniden eğiterek_ zorluğun üstesinden gelmeye çalışan üçüncü bir teknik olan **ince ayar** konusunu ele alacağız. Detaylara dalalım.

## Öğrenme Hedefleri

Bu ders, önceden eğitilmiş dil modelleri için ince ayar kavramını tanıtır, bu yaklaşımın faydalarını ve zorluklarını keşfeder ve üretken yapay zeka modellerinizin performansını artırmak için ince ayarın ne zaman ve nasıl kullanılacağı konusunda rehberlik sağlar.

Bu dersin sonunda, aşağıdaki soruları yanıtlayabilecek durumda olmalısınız:

- Dil modelleri için ince ayar nedir?
- İnce ayar ne zaman ve neden faydalıdır?
- Önceden eğitilmiş bir model nasıl ince ayarlanabilir?
- İnce ayarın sınırlamaları nelerdir?

Hazır mısınız? Başlayalım.

## Resimli Rehber

Detaylara girmeden önce neleri ele alacağımızın büyük resmini görmek ister misiniz? Bu ders için öğrenme yolculuğunu anlatan resimli rehbere göz atın - ince ayarın temel kavramlarını ve motivasyonunu öğrenmekten, ince ayar görevini yürütme sürecini ve en iyi uygulamaları anlamaya kadar. Bu keşif için büyüleyici bir konu, bu yüzden kendi kendine öğrenme yolculuğunuzu desteklemek için ek bağlantılar için [Kaynaklar](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) sayfasını kontrol etmeyi unutmayın!

![Dil Modellerinin İnce Ayarına Resimli Rehber](../../../translated_images/18-fine-tuning-sketchnote.11b21f9ec8a703467a120cb79a28b5ac1effc8d8d9d5b31bbbac6b8640432e14.tr.png)

## Dil modelleri için ince ayar nedir?

Tanım olarak, büyük dil modelleri internet dahil çeşitli kaynaklardan alınan büyük miktarlarda metin üzerinde _önceden eğitilmiştir_. Önceki derslerde öğrendiğimiz gibi, modelin kullanıcının sorularına ("istemlerine") verdiği yanıtların kalitesini artırmak için _istem mühendisliği_ ve _geri getirme ile zenginleştirilmiş üretim_ gibi tekniklere ihtiyacımız var.

Popüler bir istem mühendisliği tekniği, modele ya _talimatlar_ (açık rehberlik) sağlayarak ya da _birkaç örnek vererek_ (örtük rehberlik) yanıtta neyin beklendiği konusunda daha fazla rehberlik sağlamayı içerir. Bu, _az örnekli öğrenme_ olarak adlandırılır ancak iki sınırlaması vardır:

- Modelin token sınırları, verebileceğiniz örnek sayısını sınırlayabilir ve etkinliği kısıtlayabilir.
- Model token maliyetleri, her isteğe örnek eklemeyi pahalı hale getirebilir ve esnekliği sınırlayabilir.

İnce ayar, önceden eğitilmiş bir modeli alıp yeni verilerle yeniden eğiterek belirli bir görevdeki performansını artırmak için makine öğrenimi sistemlerinde yaygın bir uygulamadır. Dil modelleri bağlamında, önceden eğitilmiş modeli _belirli bir görev veya uygulama alanı için özenle seçilmiş bir örnek setiyle_ ince ayarlayarak, bu belirli görev veya alan için daha doğru ve alakalı olabilecek **özel bir model** oluşturabiliriz. İnce ayarın bir yan faydası da az örnekli öğrenme için gereken örnek sayısını azaltabilmesidir - bu da token kullanımını ve ilgili maliyetleri azaltır.

## Modelleri ne zaman ve neden ince ayarlamalıyız?

_Bu_ bağlamda, ince ayardan bahsederken, yeniden eğitmenin **orijinal eğitim veri setinin bir parçası olmayan yeni veriler ekleyerek** yapıldığı **denetimli** ince ayarı kastediyoruz. Bu, modelin orijinal veriler üzerinde, ancak farklı hiperparametrelerle yeniden eğitildiği denetimsiz ince ayar yaklaşımından farklıdır.

Hatırlanması gereken ana şey, ince ayarın, istenen sonuçları elde etmek için belirli bir uzmanlık düzeyi gerektiren gelişmiş bir teknik olduğudur. Yanlış yapıldığında, beklenen iyileştirmeleri sağlamayabilir ve hatta hedeflenen alan için modelin performansını düşürebilir.

Bu yüzden, dil modellerini nasıl ince ayarlayacağınızı öğrenmeden önce, bu yolu neden seçmeniz gerektiğini ve ince ayar sürecine ne zaman başlamanız gerektiğini bilmelisiniz. Kendinize şu soruları sorarak başlayın:

- **Kullanım Durumu**: İnce ayar için _kullanım durumunuz_ nedir? Mevcut önceden eğitilmiş modelin hangi yönünü geliştirmek istiyorsunuz?
- **Alternatifler**: İstenen sonuçları elde etmek için _diğer teknikleri_ denediniz mi? Bunları karşılaştırma için bir temel oluşturmak için kullanın.
  - İstem mühendisliği: İlgili istem yanıtlarının örnekleriyle az örnekli istem tekniklerini deneyin. Yanıtların kalitesini değerlendirin.
  - Geri Getirme ile Zenginleştirilmiş Üretim: İstemleri, verilerinizi arayarak alınan sorgu sonuçlarıyla zenginleştirmeyi deneyin. Yanıtların kalitesini değerlendirin.
- **Maliyetler**: İnce ayarın maliyetlerini belirlediniz mi?
  - Ayarlanabilirlik - önceden eğitilmiş model ince ayar için uygun mu?
  - Çaba - eğitim verilerini hazırlama, modeli değerlendirme ve iyileştirme için.
  - Hesaplama - ince ayar işleri yürütmek ve ince ayarlı modeli dağıtmak için
  - Veri - ince ayarın etkisi için yeterli kaliteli örneklere erişim
- **Faydalar**: İnce ayarın faydalarını doğruladınız mı?
  - Kalite - ince ayarlı model, temel modeli geçti mi?
  - Maliyet - istemleri basitleştirerek token kullanımını azaltıyor mu?
  - Genişletilebilirlik - temel modeli yeni alanlar için yeniden kullanabilir misiniz?

Bu soruları yanıtlayarak, ince ayarın kullanım durumunuz için doğru yaklaşım olup olmadığını belirleyebilmelisiniz. İdeal olarak, yaklaşım ancak faydalar maliyetlerden ağır basarsa geçerlidir. Devam etmeye karar verdiğinizde, önceden eğitilmiş modeli _nasıl_ ince ayarlayabileceğinizi düşünme zamanı gelmiştir.

Karar verme süreci hakkında daha fazla bilgi edinmek ister misiniz? [İnce ayar yapmak mı, yapmamak mı](https://www.youtube.com/watch?v=0Jo-z-MFxJs) izleyin.

## Önceden eğitilmiş bir modeli nasıl ince ayarlayabiliriz?

Önceden eğitilmiş bir modeli ince ayarlamak için ihtiyacınız olanlar:

- ince ayar yapılacak önceden eğitilmiş bir model
- ince ayar için kullanılacak bir veri seti
- ince ayar işini yürütmek için bir eğitim ortamı
- ince ayarlı modeli dağıtmak için bir barındırma ortamı

## İnce Ayar Uygulamada

Aşağıdaki kaynaklar, seçilmiş bir model ve özenle seçilmiş bir veri seti kullanarak gerçek bir örnek üzerinden adım adım eğitimler sunar. Bu eğitimleri çalışmak için, ilgili model ve veri setlerine erişimle birlikte belirli sağlayıcıda bir hesaba ihtiyacınız var.

| Sağlayıcı    | Eğitim                                                                                                                                                                          | Açıklama                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| OpenAI       | [Sohbet modelleri nasıl ince ayarlanır](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)        | Eğitim verilerini hazırlayarak, ince ayar işini yürüterek ve çıkarım için ince ayarlı modeli kullanarak belirli bir alan ("tarif asistanı") için bir `gpt-35-turbo` ince ayarlamayı öğrenin.                                                                                                                                                                                                                                       |
| Azure OpenAI | [GPT 3.5 Turbo ince ayar eğitimi](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst)    | Eğitim verilerini oluşturma ve yükleme adımlarını atarak, ince ayar işini yürüterek bir `gpt-35-turbo-0613` modelini **Azure'da** ince ayarlamayı öğrenin. Yeni modeli dağıtın ve kullanın.                                                                                                                                                                                                                                             |
| Hugging Face | [Hugging Face ile LLM'leri ince ayarlama](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                           | Bu blog yazısı, açık bir LLM'yi (örneğin: `CodeLlama 7B`) [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) kütüphanesi ve açık [veri setleri](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) ile [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) kullanarak ince ayarlamanızı anlatır. |
|              |                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 🤗 AutoTrain | [AutoTrain ile LLM'leri ince ayarlama](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                    | AutoTrain (veya AutoTrain Advanced), Hugging Face tarafından geliştirilen ve birçok farklı görev için ince ayar yapılmasına olanak tanıyan bir python kütüphanesidir. AutoTrain, kodsuz bir çözümdür ve ince ayar işlemi kendi bulutunuzda, Hugging Face Spaces'te veya yerel olarak yapılabilir. Hem web tabanlı bir GUI, CLI hem de yaml yapılandırma dosyaları aracılığıyla eğitim destekler.                                          |
|              |                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## Görev

Yukarıdaki eğitimlerden birini seçin ve onları adım adım izleyin. _Bu eğitimlerin bir versiyonunu yalnızca referans için bu depoda Jupyter Notebooks'ta çoğaltabiliriz. En son sürümleri almak için lütfen doğrudan orijinal kaynakları kullanın_.

## Harika İş! Öğrenmeye Devam Edin.

Bu dersi tamamladıktan sonra, Üretken Yapay Zeka bilginizi artırmaya devam etmek için [Üretken Yapay Zeka Öğrenme koleksiyonumuzu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) inceleyin!

Tebrikler!! Bu kurs için v2 serisinin son dersini tamamladınız! Öğrenmeyi ve inşa etmeyi bırakmayın. \*\*Sadece bu konu için ek öneriler listesi için [KAYNAKLAR](RESOURCES.md?WT.mc_id=academic-105485-koreyst) sayfasını kontrol edin.

V1 ders serimiz de daha fazla ödev ve kavramla güncellendi. Bu yüzden bilginizi tazelemek için bir dakikanızı ayırın - ve lütfen bu dersleri topluluk için iyileştirmemize yardımcı olmak için [sorularınızı ve geri bildirimlerinizi paylaşın](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan dolayı sorumluluk kabul etmiyoruz.