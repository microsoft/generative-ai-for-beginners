<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0bba96e53ab841d99db731892a51fab8",
  "translation_date": "2025-06-25T23:56:17+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "tr"
}
-->
## Giriş

Açık kaynaklı LLM'lerin dünyası heyecan verici ve sürekli gelişiyor. Bu ders, açık kaynak modellerine derinlemesine bir bakış sunmayı amaçlıyor. Eğer açık kaynak modelleri ile özel modellerin nasıl karşılaştırıldığını öğrenmek istiyorsanız, ["Farklı LLM'leri Keşfetmek ve Karşılaştırmak" dersi](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst) bölümüne gidin. Bu ders aynı zamanda ince ayar konusunu da ele alacak, ancak daha ayrıntılı bir açıklama ["LLM'lere İnce Ayar Yapmak" dersi](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst) bölümünde bulunabilir.

## Öğrenme Hedefleri

- Açık kaynaklı modelleri anlama
- Açık kaynaklı modellerle çalışmanın faydalarını anlama
- Hugging Face ve Azure AI Studio'da mevcut olan açık modelleri keşfetme

## Açık Kaynak Modeller Nedir?

Açık kaynaklı yazılım, çeşitli alanlarda teknolojinin büyümesinde kritik bir rol oynamıştır. Açık Kaynak Girişimi (OSI), yazılımın açık kaynak olarak sınıflandırılması için [10 kriter](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) tanımlamıştır. Kaynak kodu, OSI tarafından onaylanmış bir lisans altında açıkça paylaşılmalıdır.

LLM'lerin geliştirilmesi, yazılım geliştirmeye benzer unsurlar taşırken, süreç tam olarak aynı değildir. Bu durum, LLM'ler bağlamında açık kaynak tanımının tartışılmasına yol açmıştır. Bir modelin geleneksel açık kaynak tanımına uygun olması için aşağıdaki bilgilerin kamuya açık olması gerekmektedir:

- Modeli eğitmek için kullanılan veri setleri.
- Eğitim sürecinin bir parçası olarak tam model ağırlıkları.
- Değerlendirme kodu.
- İnce ayar kodu.
- Tam model ağırlıkları ve eğitim metrikleri.

Şu anda bu kriterlere uyan sadece birkaç model bulunmaktadır. [Allen Institute for Artificial Intelligence (AllenAI) tarafından oluşturulan OLMo modeli](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) bu kategoriye uyan bir örnektir.

Bu ders için, yazım sırasında yukarıdaki kriterlere uymayabileceklerinden dolayı modelleri "açık modeller" olarak adlandıracağız.

## Açık Modellerin Faydaları

**Yüksek Derecede Özelleştirilebilir** - Açık modeller ayrıntılı eğitim bilgileriyle yayınlandığı için, araştırmacılar ve geliştiriciler modelin iç işleyişini değiştirebilir. Bu, belirli bir görev veya çalışma alanı için ince ayar yapılmış son derece özel modellerin oluşturulmasını sağlar. Buna kod üretimi, matematiksel işlemler ve biyoloji gibi bazı örnekler verilebilir.

**Maliyet** - Bu modelleri kullanma ve dağıtma maliyeti, özel modellere göre daha düşüktür. Üretken AI uygulamaları oluştururken, bu modellerle çalışırken performans ve fiyatı göz önünde bulundurmalısınız.

**Esneklik** - Açık modellerle çalışmak, farklı modelleri kullanma veya birleştirme konusunda esneklik sağlar. Bunun bir örneği, kullanıcı arayüzünde kullanılacak modeli doğrudan seçebileceğiniz [HuggingChat Asistanları](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst)'dır.

## Farklı Açık Modelleri Keşfetme

### Llama 2

Meta tarafından geliştirilen [LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), sohbet tabanlı uygulamalar için optimize edilmiş bir açık modeldir. Bu, büyük miktarda diyalog ve insan geri bildirimi içeren ince ayar yöntemi nedeniyle ortaya çıkmıştır. Bu yöntemle, model insan beklentilerine daha uygun sonuçlar üretir ve daha iyi bir kullanıcı deneyimi sağlar.

Llama'nın ince ayar yapılmış bazı versiyonları arasında Japonca konusunda uzmanlaşmış [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst) ve temel modelin geliştirilmiş bir versiyonu olan [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst) bulunmaktadır.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst), yüksek performans ve verimliliğe odaklanan bir açık modeldir. Uzmanlar karışımı yaklaşımını kullanır, bu da belirli bir girdiye bağlı olarak bir grup uzman modelin seçildiği bir sistemi birleştirir. Bu, modellerin yalnızca uzmanlaştıkları girdileri ele alması nedeniyle hesaplamayı daha etkili hale getirir.

Mistral'ın ince ayar yapılmış bazı versiyonları arasında tıp alanına odaklanan [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst) ve matematiksel hesaplamalar yapan [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst) bulunmaktadır.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst), Teknoloji İnovasyon Enstitüsü (TII) tarafından oluşturulmuş bir LLM'dir. Falcon-40B, 40 milyar parametre üzerinde eğitilmiş olup daha az hesaplama bütçesiyle GPT-3'ten daha iyi performans göstermektedir. Bu, FlashAttention algoritması ve çoklu sorgu dikkatini kullanarak çıkarım zamanında bellek gereksinimlerini azaltması sayesinde gerçekleşmiştir. Azaltılmış çıkarım süresi ile Falcon-40B sohbet uygulamaları için uygundur.

Falcon'un ince ayar yapılmış bazı versiyonları arasında açık modeller üzerine inşa edilmiş bir asistan olan [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst) ve temel modelden daha yüksek performans sunan [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst) bulunmaktadır.

## Nasıl Seçilir

Açık bir model seçmek için tek bir doğru cevap yoktur. Başlamak için iyi bir yer, Azure AI Studio'nun görev bazında filtreleme özelliğini kullanmaktır. Bu, modelin hangi tür görevler için eğitildiğini anlamanıza yardımcı olacaktır. Hugging Face ayrıca belirli metriklere dayalı en iyi performans gösteren modelleri gösteren bir LLM Lider Tablosu tutmaktadır.

Farklı türler arasında LLM'leri karşılaştırmak istendiğinde, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) başka bir harika kaynaktır.

Belirli bir kullanım durumu üzerinde çalışırken, aynı alana odaklanmış ince ayar yapılmış versiyonları aramak etkili olabilir. Birden fazla açık modeli deneyerek, bunların sizin ve kullanıcılarınızın beklentilerine göre nasıl performans gösterdiğini görmek başka iyi bir uygulamadır.

## Sonraki Adımlar

Açık modellerle çalışmaya hızlı bir şekilde başlayabilirsiniz. Burada tartıştığımız modellerin bulunduğu özel bir Hugging Face koleksiyonu içeren [Azure AI Studio Model Kataloğu](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)'na göz atın.

## Öğrenme burada durmuyor, Yolculuğa devam edin

Bu dersi tamamladıktan sonra, Üretken AI bilginizi geliştirmeye devam etmek için [Generative AI Learning koleksiyonumuzu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) inceleyin!

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için, profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.