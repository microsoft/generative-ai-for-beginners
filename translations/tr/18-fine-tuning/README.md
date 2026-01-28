<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3772dcd23a98e2010f53ce8b9c583631",
  "translation_date": "2026-01-18T18:14:52+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "tr"
}
-->
[![Open Source Models](../../../../../translated_images/tr/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# LLM’inizi İnce Ayarlama

Büyük dil modellerini kullanarak üretken yapay zeka uygulamaları geliştirmek yeni zorlukları beraberinde getirir. Temel bir konu, modelin belirli bir kullanıcı talebine yönelik içerikte sağladığı yanıtlarda kaliteyi (doğruluk ve alaka) güvence altına almaktır. Önceki derslerde, bu sorunu mevcut modele _girdi olarak verilen istemi değiştirerek_ çözmeye çalışan istem mühendisliği ve geri getirme destekli üretim gibi teknikleri ele aldık.

Bugünkü dersimizde, bu zorluğu _modelin kendisini ek veriyle yeniden eğiterek_ çözmeye çalışan üçüncü bir teknik olan **ince ayarlama**yı tartışacağız. Detaylara dalalım.

## Öğrenme Hedefleri

Bu ders, önceden eğitilmiş dil modelleri için ince ayar kavramını tanıtır, bu yaklaşımın faydalarını ve zorluklarını keşfeder ve üretken yapay zeka modellerinizin performansını artırmak için ince ayarın ne zaman ve nasıl kullanılacağına dair rehberlik sağlar.

Bu dersin sonunda şu soruları yanıtlayabilmelisiniz:

- Dil modelleri için ince ayar nedir?
- İnce ayar ne zaman ve neden faydalıdır?
- Önceden eğitilmiş bir modeli nasıl ince ayarlayabilirim?
- İnce ayarın sınırlamaları nelerdir?

Hazır mısınız? Başlayalım.

## Görsel Rehber

İnce ayarın temel kavramlarını ve motivasyonunu öğrenmekten, ince ayar süreci ve en iyi uygulamaları anlamaya kadar öğrenme yolculuğumuzu anlatan bu çizimli rehbere bir göz atmak ister misiniz? Keşif için büyüleyici bir konu, bu yüzden kendi kendinize öğrenme yolculuğunuzu destekleyecek ek bağlantılar için [Kaynaklar](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) sayfasını unutmayın!

![İnce Ayar için Dil Modelleri Çizimli Rehberi](../../../../../translated_images/tr/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Dil modelleri için ince ayar nedir?

Tanımı gereği, büyük dil modelleri internet de dahil olmak üzere çeşitli kaynaklardan toplanan büyük miktarda metin üzerinde _önceden eğitilmiştir_. Önceki derslerde öğrendiğimiz gibi, modelin kullanıcı sorularına ("isteme") verdiği yanıtların kalitesini artırmak için _istem mühendisliği_ ve _geri getirme destekli üretim_ gibi tekniklere ihtiyacımız vardır.

Popüler bir istem mühendisliği tekniği, modele yanıtla ne beklendiğine dair daha fazla rehberlik sağlamaktır; bu ya _talimatlar_ (açık rehberlik) vererek ya da _birkaç örnek sunarak_ (örtülü rehberlik). Bu _az örnek öğrenme_ olarak adlandırılır, ancak iki sınırı vardır:

- Model token sınırları, verebileceğiniz örnek sayısını kısıtlayabilir ve etkinliğini azaltabilir.
- Model token maliyetleri, her isteme örnek eklemeyi pahalı hale getirebilir ve esnekliği kısıtlayabilir.

İnce ayar, makine öğrenmesi sistemlerinde sık kullanılan bir uygulamadır; önceden eğitilmiş bir modeli alır ve belirli bir görevdeki performansını artırmak için yeni verilerle yeniden eğitiriz. Dil modelleri bağlamında, önceden eğitilmiş modeli _verilen bir görev veya uygulama alanı için seçilmiş bir örnek kümesiyle_ ince ayarlayarak, o belirli görev veya alanda daha doğru ve alakalı olabilecek **özel bir model** oluşturabiliriz. İnce ayarın yan faydalarından biri de az örnek öğrenme için gereken örnek sayısını azaltabilmesi, böylece token kullanımını ve ilgili maliyetleri düşürmesidir.

## İnce ayarı ne zaman ve neden yapmalıyız?

_Bu_ bağlamda ince ayardan bahsettiğimizde, orijinal eğitim veri setinde olmayan **yeni veri ekleyerek** yapılan **denetimli** ince ayarı kastediyoruz. Bu, modelin orijinal veri üzerinde farklı hiperparametrelerle yeniden eğitildiği denetimsiz ince ayardan farklıdır.

Unutulmaması gereken kilit nokta, ince ayarın istenilen sonuçları almak için belirli bir uzmanlık düzeyi gerektiren gelişmiş bir teknik olduğudur. Yanlış yapılırsa beklenen iyileştirmeleri sağlamayabilir ve hedeflenen alan için modelin performansını düşürebilir.

Bu nedenle, "nasıl" ince ayar yapacağınızı öğrenmeden önce, "neden" bu yolu tercih etmeniz gerektiğini ve ince ayar yapmaya "ne zaman" başlamanız gerektiğini bilmelisiniz. Önce şu soruları kendinize sorun:

- **Kullanım Senaryosu**: İnce ayar yapma amacınız nedir? Mevcut önceden eğitilmiş modelin hangi yönünü geliştirmek istiyorsunuz?
- **Alternatifler**: İstenilen sonuçları elde etmek için _başka teknikleri_ denediniz mi? Bunları referans oluşturmak için kullanın.
  - İstem mühendisliği: İlgili yanıt örnekleriyle az örnekli istemleri deneyin. Yanıtların kalitesini değerlendirin.
  - Geri Getirme Destekli Üretim: Verinizi aratarak alınan sorgu sonuçlarıyla istemleri zenginleştirin. Yanıtların kalitesini değerlendirin.
- **Maliyetler**: İnce ayarın maliyetlerini belirlediniz mi?
  - İncelenebilirlik – önceden eğitilmiş model ince ayara açık mı?
  - Çaba – eğitim verisi hazırlama, modeli değerlendirip iyileştirme
  - Hesaplama – ince ayar işleri çalıştırmak ve ince ayarlı modeli dağıtmak için gereken
  - Veri – ince ayar etkisi için yeterli nitelikte örneklere erişim
- **Faydalar**: İnce ayarın faydalarını teyit ettiniz mi?
  - Kalite – ince ayarlı model referans modeli geçti mi?
  - Maliyet – basitleştirilmiş istemlerle token kullanımını azalttı mı?
  - Genişletilebilirlik – temel modeli yeni alanlarda kullanabilir misiniz?

Bu sorulara verdiğiniz yanıtlar, ince ayarın kullanım senaryonuza uygun olup olmadığını belirlemenize yardımcı olmalıdır. İdeal olarak, faydalar maliyetlerden fazla olduğunda bu yaklaşım geçerlidir. İlerlemeye karar verdiğinizde, önceden eğitilmiş modeli _nasıl_ ince ayarlayabileceğinizi düşünmenin zamanı gelir.

Karar verme süreci hakkında daha fazla bilgi mi istiyorsunuz? [İnce ayar yapmalı mı, yapmamalı mı?](https://www.youtube.com/watch?v=0Jo-z-MFxJs) başlıklı videoyu izleyin.

## Önceden eğitilmiş modeli nasıl ince ayarlayabiliriz?

Önceden eğitilmiş bir modeli ince ayarlamak için ihtiyacınız olanlar:

- İnce ayar yapılacak önceden eğitilmiş model
- İnce ayar için kullanılacak veri seti
- İnce ayar işi çalıştırılacak eğitim ortamı
- İnce ayarlı modeli dağıtmak için barındırma ortamı

## İnce Ayar Uygulaması

Aşağıdaki kaynaklar, seçilmiş bir modeli önceden seçilmiş bir veri setiyle gerçek bir örnek üzerinden adım adım anlatan eğitimler sağlar. Bu eğitimleri kullanmak için ilgili sağlayıcıda bir hesabınızın olması ve gerekli model ile veri setlerine erişiminizin bulunması gerekir.

| Sağlayıcı     | Eğitim                                                                                                                                                                       | Açıklama                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Chat modellerini nasıl ince ayarlayacağınız](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | `gpt-35-turbo` modelini belirli bir alan ("tarif asistanı") için eğitimin verisini hazırlayarak, ince ayar işini çalıştırarak ve ince ayarlı modeli çıkarım için kullanarak nasıl ince ayarlayacağınızı öğrenin.                                                                                                                                                                                                                                              |
| Azure OpenAI | [GPT 3.5 Turbo ince ayar eğitimi](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | **Azure üzerinde** `gpt-35-turbo-0613` modelini ince ayarlamak için eğitim verisi oluşturma ve yükleme, ince ayar işini çalıştırma, yeni modeli dağıtma ve kullanma adımlarını öğrenin.                                                                                                                                                                                                                                                                 |
| Hugging Face | [Hugging Face ile LLM ince ayarı](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Bu blog yazısı, Hugging Face’in [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) kütüphanesi ve [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst]) kullanarak açık kaynak bir LLM'nin (örneğin `CodeLlama 7B`) nasıl ince ayarlanacağını ve Hugging Face üzerinde açık [veri setleriyle](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) yapılan uygulamalı örneği anlatır. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [AutoTrain ile LLM ince ayarı](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (veya AutoTrain Advanced), Hugging Face tarafından geliştirilen, LLM ince ayar da dahil birçok görevi kolaylaştıran python kütüphanesidir. AutoTrain kodlama gerektirmeyen bir çözümdür ve ince ayar işlemi kendi bulutunuzda, Hugging Face Spaces’te veya yerel olarak yapılabilir. Web tabanlı GUI, CLI ve yaml yapılandırma dosyasıyla eğitim destekler.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Unsloth ile LLM ince ayarı](https://github.com/unslothai/unsloth)                                                         | Unsloth, LLM ince ayar ve pekiştirmeli öğrenmeyi (RL) destekleyen açık kaynaklı bir çerçevedir. Kullanıma hazır [defterler](https://github.com/unslothai/notebooks) ile yerel eğitim, değerlendirme ve dağıtımı kolaylaştırır. Ayrıca metinden sese (TTS), BERT ve çok modal modelleri destekler. Başlamak için adım adım [LLM İnce Ayar Rehberi](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) okunabilir.                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Ödev

Yukarıdaki eğitimlerden birini seçin ve inceleyin. _Bu eğitimlerin Jupyter Notebooks sürümleri yalnızca referans için bu depoda çoğaltılabilir. Lütfen en güncel sürümleri doğrudan orijinal kaynaklardan edinin_.

## Harika İş! Öğrenmeye Devam Et.

Bu dersi tamamladıktan sonra, üretken yapay zeka bilginizi geliştirmeye devam etmek için [Üretken AI Öğrenme koleksiyonumuza](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) göz atın!

Tebrikler!! Bu kursun v2 serisindeki son dersi tamamladınız! Öğrenmeye ve geliştirmeye devam edin. \*\*Sadece bu konu için ek öneriler listesini görmek üzere [KAYNAKLAR](RESOURCES.md?WT.mc_id=academic-105485-koreyst) sayfasını kontrol edin.

v1 ders serimiz de daha fazla ödev ve kavram ile güncellendi. Bilginizi tazelemek için bir dakikanızı ayırın - ve lütfen [sorularınızı ve geri bildirimlerinizi](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) paylaşarak topluluk için bu dersleri geliştirmemize yardım edin.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hata veya yanlışlık içerebileceği unutulmamalıdır. Yetkili kaynak olarak belgenin orijinal dili dikkate alınmalıdır. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yanlış yorumlardan sorumlu tutulamayız.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->