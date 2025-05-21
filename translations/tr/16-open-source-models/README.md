<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0bba96e53ab841d99db731892a51fab8",
  "translation_date": "2025-05-20T06:55:24+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "tr"
}
-->
## Giriş

Açık kaynaklı LLM'lerin dünyası heyecan verici ve sürekli gelişiyor. Bu ders, açık kaynak modellerine derinlemesine bir bakış sunmayı amaçlıyor. Eğer özel modellerin açık kaynak modellerle nasıl karşılaştırıldığını merak ediyorsanız, ["Farklı LLM'leri Keşfetmek ve Karşılaştırmak" dersine](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst) göz atabilirsiniz. Bu ders ayrıca ince ayar konusunu da kapsayacak, ancak daha detaylı bir açıklama için ["LLM'lere İnce Ayar Yapma" dersine](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst) bakabilirsiniz.

## Öğrenme Hedefleri

- Açık kaynaklı modelleri anlamak
- Açık kaynaklı modellerle çalışmanın avantajlarını anlamak
- Hugging Face ve Azure AI Studio'da mevcut açık modelleri keşfetmek

## Açık Kaynak Modeller Nedir?

Açık kaynak yazılımı, teknolojinin çeşitli alanlarda büyümesinde önemli bir rol oynamıştır. Açık Kaynak Girişimi (OSI), bir yazılımın açık kaynak olarak sınıflandırılması için [10 kriter tanımlamıştır](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst). Kaynak kodu, OSI tarafından onaylanmış bir lisans altında açıkça paylaşılmalıdır.

LLM'lerin geliştirilmesi, yazılım geliştirmeye benzer unsurlar taşısa da süreç tam olarak aynı değildir. Bu durum, LLM'ler bağlamında açık kaynak tanımı üzerine toplulukta birçok tartışma getirmiştir. Bir modelin geleneksel açık kaynak tanımına uygun olması için aşağıdaki bilgilerin kamuya açık olması gerekir:

- Modeli eğitmek için kullanılan veri setleri.
- Eğitim sürecinin bir parçası olarak tam model ağırlıkları.
- Değerlendirme kodu.
- İnce ayar kodu.
- Tam model ağırlıkları ve eğitim metrikleri.

Şu anda bu kriterlere uyan sadece birkaç model bulunmaktadır. [Allen Institute for Artificial Intelligence (AllenAI) tarafından oluşturulan OLMo modeli](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) bu kategoriye uyan bir modeldir.

Bu ders için, yazım sırasında yukarıdaki kriterlere uymayabilecekleri için modelleri "açık modeller" olarak adlandıracağız.

## Açık Modellerin Avantajları

**Yüksek Derecede Özelleştirilebilir** - Açık modeller, detaylı eğitim bilgileri ile yayınlandığından, araştırmacılar ve geliştiriciler modelin iç işleyişini değiştirebilir. Bu, belirli bir görev veya çalışma alanı için ince ayar yapılmış son derece özel modellerin oluşturulmasını sağlar. Bunun bazı örnekleri kod üretimi, matematiksel işlemler ve biyolojidir.

**Maliyet** - Bu modelleri kullanmanın ve dağıtmanın token başına maliyeti, özel modellere göre daha düşüktür. Üretken AI uygulamaları oluştururken, kullanım durumunuza göre bu modellerle çalışırken performans ve fiyatı değerlendirmek önemlidir.

**Esneklik** - Açık modellerle çalışmak, farklı modelleri kullanma veya birleştirme konusunda esneklik sağlar. Bunun bir örneği, kullanıcı arayüzünde kullanılan modeli doğrudan seçebileceğiniz [HuggingChat Asistanları](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst)dir.

## Farklı Açık Modelleri Keşfetmek

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), Meta tarafından geliştirilmiş ve sohbet tabanlı uygulamalar için optimize edilmiş bir açık modeldir. Bu, büyük miktarda diyalog ve insan geri bildirimi içeren ince ayar yöntemi sayesinde mümkündür. Bu yöntemle model, insan beklentilerine daha uygun sonuçlar üretir, bu da daha iyi bir kullanıcı deneyimi sağlar.

Llama'nın ince ayar yapılmış bazı versiyonları arasında Japonca'da uzmanlaşmış [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst) ve temel modelin geliştirilmiş bir versiyonu olan [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst) bulunmaktadır.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst), yüksek performans ve verimlilik odaklı bir açık modeldir. Mixture-of-Experts yaklaşımını kullanır, bu da bir grup uzman modeli bir araya getirerek, girdiye bağlı olarak belirli modellerin seçilmesini sağlar. Bu, hesaplamayı daha etkili hale getirir çünkü modeller yalnızca uzmanlaştıkları girdileri ele alır.

Mistral'ın ince ayar yapılmış bazı versiyonları arasında tıbbi alana odaklanan [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst) ve matematiksel hesaplamalar yapan [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst) bulunmaktadır.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst), Teknoloji İnovasyon Enstitüsü (**TII**) tarafından oluşturulan bir LLM'dir. Falcon-40B, 40 milyar parametre üzerinde eğitilmiş olup, daha düşük hesaplama bütçesi ile GPT-3'ten daha iyi performans gösterdiği görülmüştür. Bu, FlashAttention algoritması ve çoklu sorgu dikkatini kullanarak çıkarım süresindeki bellek gereksinimlerini azaltması sayesinde mümkündür. Azaltılmış çıkarım süresi ile Falcon-40B, sohbet uygulamaları için uygundur.

Falcon'un ince ayar yapılmış bazı versiyonları arasında açık modeller üzerine inşa edilmiş bir asistan olan [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst) ve temel modelden daha yüksek performans sunan [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst) bulunmaktadır.

## Nasıl Seçilir

Açık model seçimi için tek bir doğru cevap yoktur. Başlamak için iyi bir yer, Azure AI Studio'nun görev bazlı filtreleme özelliğini kullanmaktır. Bu, modelin hangi tür görevler için eğitildiğini anlamanıza yardımcı olacaktır. Hugging Face ayrıca belirli metriklere göre en iyi performans gösteren modelleri gösteren bir LLM Liderlik Tablosu tutar.

Farklı türler arasında LLM'leri karşılaştırırken, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) başka bir harika kaynaktır.

Belirli bir kullanım durumu üzerinde çalışırken, aynı alana odaklanmış ince ayar yapılmış versiyonları aramak etkili olabilir. Kullanıcılarınızın ve sizin beklentilerinize göre nasıl performans gösterdiklerini görmek için birden fazla açık modelle denemeler yapmak iyi bir uygulamadır.

## Sonraki Adımlar

Açık modellerin en iyi yanı, onlarla çalışmaya oldukça hızlı bir şekilde başlayabilmenizdir. Burada tartıştığımız modellerin yer aldığı belirli bir Hugging Face koleksiyonunu içeren [Azure AI Studio Model Kataloğuna](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) göz atın.

## Öğrenme burada bitmiyor, Yolculuğa devam edin

Bu dersi tamamladıktan sonra, Üretken AI bilginizi geliştirmeye devam etmek için [Generative AI Learning koleksiyonumuza](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) göz atın!

**Sorumluluk Reddi**: 
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini unutmayın. Belgenin orijinal dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda ortaya çıkabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.