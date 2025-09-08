<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8b2d4bb727c877ebf9edff8623d16b9",
  "translation_date": "2025-09-06T10:17:29+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "tr"
}
-->
[![Açık Kaynak Modeller](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.tr.png)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## Giriş

Açık kaynaklı LLM'lerin dünyası heyecan verici ve sürekli değişiyor. Bu ders, açık kaynak modellerine derinlemesine bir bakış sunmayı amaçlıyor. Eğer özel modellerin açık kaynak modellerle nasıl karşılaştırıldığını öğrenmek istiyorsanız, ["Farklı LLM'leri Keşfetmek ve Karşılaştırmak" dersi](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst) bölümüne göz atabilirsiniz. Bu ders ayrıca ince ayar konusunu ele alacak, ancak daha ayrıntılı bir açıklama için ["LLM'lere İnce Ayar Yapmak" dersi](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst) bölümüne bakabilirsiniz.

## Öğrenme Hedefleri

- Açık kaynak modellerini anlamak
- Açık kaynak modellerle çalışmanın faydalarını kavramak
- Hugging Face ve Azure AI Studio'daki açık modelleri keşfetmek

## Açık Kaynak Modeller Nedir?

Açık kaynak yazılım, teknolojinin çeşitli alanlarda büyümesinde önemli bir rol oynamıştır. Açık Kaynak Girişimi (OSI), bir yazılımın açık kaynak olarak sınıflandırılması için [10 kriter](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) tanımlamıştır. Kaynak kodu, OSI tarafından onaylanmış bir lisans altında açıkça paylaşılmalıdır.

LLM'lerin geliştirilmesi, yazılım geliştirmeye benzer unsurlar içerirken, süreç tam olarak aynı değildir. Bu durum, LLM'ler bağlamında açık kaynak tanımı üzerine toplulukta birçok tartışma yaratmıştır. Bir modelin geleneksel açık kaynak tanımına uygun olması için aşağıdaki bilgilerin kamuya açık olması gerekir:

- Modeli eğitmek için kullanılan veri setleri.
- Eğitim sürecinin bir parçası olarak tam model ağırlıkları.
- Değerlendirme kodu.
- İnce ayar kodu.
- Tam model ağırlıkları ve eğitim metrikleri.

Şu anda bu kriterlere uyan çok az model bulunmaktadır. [Allen Institute for Artificial Intelligence (AllenAI) tarafından oluşturulan OLMo modeli](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) bu kategoriye uyan bir örnektir.

Bu ders için, yazım sırasında yukarıdaki kriterlere uymayabilecek modelleri "açık modeller" olarak adlandıracağız.

## Açık Modellerin Faydaları

**Son Derece Özelleştirilebilir** - Açık modeller ayrıntılı eğitim bilgileriyle yayınlandığından, araştırmacılar ve geliştiriciler modelin iç yapısını değiştirebilir. Bu, belirli bir görev veya çalışma alanı için ince ayar yapılmış son derece özel modellerin oluşturulmasını sağlar. Örnekler arasında kod üretimi, matematiksel işlemler ve biyoloji bulunmaktadır.

**Maliyet** - Bu modelleri kullanma ve dağıtma maliyeti, özel modellere göre daha düşüktür. Üretken Yapay Zeka uygulamaları oluştururken, bu modellerle çalışırken performans ve fiyat arasındaki dengeyi göz önünde bulundurmak önemlidir.

![Model Maliyeti](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.tr.png)  
Kaynak: Artificial Analysis

**Esneklik** - Açık modellerle çalışmak, farklı modelleri kullanma veya birleştirme konusunda esneklik sağlar. Bunun bir örneği, kullanıcıların doğrudan arayüzde kullanılan modeli seçebildiği [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst) uygulamasıdır:

![Model Seç](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.tr.png)

## Farklı Açık Modelleri Keşfetmek

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), Meta tarafından geliştirilen ve sohbet tabanlı uygulamalar için optimize edilmiş bir açık modeldir. Bu, büyük miktarda diyalog ve insan geri bildirimi içeren ince ayar yöntemi sayesinde mümkün olmuştur. Bu yöntemle model, insan beklentilerine daha uygun sonuçlar üreterek daha iyi bir kullanıcı deneyimi sağlar.

Llama'nın ince ayar yapılmış bazı versiyonları arasında Japonca'ya odaklanan [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst) ve temel modelin geliştirilmiş bir versiyonu olan [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst) bulunmaktadır.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst), yüksek performans ve verimliliğe odaklanan bir açık modeldir. Mixture-of-Experts yaklaşımını kullanır; bu, bir grup uzman modelin bir sistemde birleştirilmesi ve girdiye bağlı olarak belirli modellerin seçilmesi anlamına gelir. Bu, modellerin yalnızca uzmanlaştıkları girdileri ele alması nedeniyle hesaplamayı daha etkili hale getirir.

Mistral'ın ince ayar yapılmış bazı versiyonları arasında tıbbi alana odaklanan [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst) ve matematiksel hesaplama yapan [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst) bulunmaktadır.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst), Teknoloji İnovasyon Enstitüsü (**TII**) tarafından oluşturulan bir LLM'dir. Falcon-40B, 40 milyar parametre üzerinde eğitilmiş olup, daha az hesaplama bütçesiyle GPT-3'ten daha iyi performans gösterdiği kanıtlanmıştır. Bu, FlashAttention algoritması ve çoklu sorgu dikkat mekanizması kullanımı sayesinde gerçekleşmiştir; bu, çıkarım zamanında bellek gereksinimlerini azaltır. Azaltılmış çıkarım süresiyle Falcon-40B, sohbet uygulamaları için uygundur.

Falcon'un ince ayar yapılmış bazı versiyonları arasında açık modeller üzerine inşa edilmiş bir asistan olan [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst) ve temel modelden daha yüksek performans sunan [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst) bulunmaktadır.

## Nasıl Seçilir?

Bir açık model seçmek için tek bir doğru cevap yoktur. Başlamak için iyi bir yer, Azure AI Studio'nun görev bazlı filtreleme özelliğini kullanmaktır. Bu, modelin hangi tür görevler için eğitildiğini anlamanıza yardımcı olur. Hugging Face ayrıca belirli metriklere göre en iyi performans gösteren modelleri gösteren bir LLM Liderlik Tablosu tutmaktadır.

Farklı türlerdeki LLM'leri karşılaştırmak için [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) başka bir harika kaynaktır:

![Model Kalitesi](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.tr.png)  
Kaynak: Artificial Analysis

Belirli bir kullanım durumu üzerinde çalışıyorsanız, aynı alana odaklanan ince ayar yapılmış versiyonları aramak etkili olabilir. Kullanıcılarınızın beklentilerine göre performanslarını görmek için birden fazla açık modeli denemek de iyi bir uygulamadır.

## Sonraki Adımlar

Açık modellerin en iyi yanı, onlarla çalışmaya oldukça hızlı bir şekilde başlayabilmenizdir. Burada tartıştığımız modelleri içeren özel bir Hugging Face koleksiyonuna sahip olan [Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) bölümüne göz atabilirsiniz.

## Öğrenme burada bitmiyor, yolculuğa devam edin

Bu dersi tamamladıktan sonra, [Üretken Yapay Zeka Öğrenme koleksiyonumuza](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) göz atarak Üretken Yapay Zeka bilginizi geliştirmeye devam edin!

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.