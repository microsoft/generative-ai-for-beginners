<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:30:51+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "tr"
}
-->
# Meta Ailesi Modelleriyle İnşa Etmek

## Giriş

Bu ders şunları kapsayacaktır:

- İki ana Meta ailesi modeli - Llama 3.1 ve Llama 3.2'yi keşfetmek
- Her modelin kullanım alanlarını ve senaryolarını anlamak
- Her modelin benzersiz özelliklerini göstermek için kod örneği

## Meta Ailesi Modelleri

Bu derste, Meta ailesinden veya "Llama Sürüsü"nden iki modeli - Llama 3.1 ve Llama 3.2 - keşfedeceğiz.

Bu modeller farklı varyantlarda gelir ve GitHub Model pazarında mevcuttur. AI modelleriyle [prototip oluşturmak](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) için GitHub Modelleri kullanma hakkında daha fazla bilgi burada.

Model Varyantları:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Not: Llama 3 de GitHub Modellerinde mevcuttur ancak bu derste ele alınmayacaktır.*

## Llama 3.1

405 Milyar Parametre ile Llama 3.1, açık kaynak LLM kategorisine girer.

Bu model, daha önceki Llama 3 sürümüne şu yenilikleri ekleyerek bir yükseltme sunar:

- Daha büyük bağlam penceresi - 128k token vs 8k token
- Daha büyük Maksimum Çıktı Tokenları - 4096 vs 2048
- Daha iyi Çok Dilli Destek - eğitim tokenlarının artması nedeniyle

Bunlar, Llama 3.1'in GenAI uygulamaları oluştururken daha karmaşık kullanım senaryolarını ele almasını sağlar, bunlar arasında:
- Yerel Fonksiyon Çağırma - LLM iş akışının dışında harici araçları ve fonksiyonları çağırma yeteneği
- Daha İyi RAG Performansı - daha yüksek bağlam penceresi sayesinde
- Sentetik Veri Üretimi - ince ayar gibi görevler için etkili veri oluşturma yeteneği

### Yerel Fonksiyon Çağırma

Llama 3.1, fonksiyon veya araç çağırmada daha etkili olacak şekilde ince ayarlanmıştır. Ayrıca, modelin kullanıcının yönlendirmesine dayalı olarak kullanılmaları gerektiğini belirleyebileceği iki yerleşik araç vardır. Bu araçlar:

- **Brave Arama** - Web araması yaparak hava durumu gibi güncel bilgileri almak için kullanılabilir
- **Wolfram Alpha** - Kendi fonksiyonlarınızı yazmanız gerekmeksizin daha karmaşık matematiksel hesaplamalar için kullanılabilir.

Ayrıca, LLM'nin çağırabileceği kendi özel araçlarınızı da oluşturabilirsiniz.

Aşağıdaki kod örneğinde:

- Mevcut araçları (brave_search, wolfram_alpha) sistem yönlendirmesinde tanımlarız.
- Belirli bir şehirdeki hava durumu hakkında bir kullanıcı yönlendirmesi göndeririz.
- LLM, Brave Arama aracına bir araç çağrısıyla yanıt verecektir, bu şöyle görünecektir: `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Not: Bu örnek sadece araç çağrısı yapar, sonuçları almak isterseniz Brave API sayfasında ücretsiz bir hesap oluşturmanız ve fonksiyonu tanımlamanız gerekecektir.*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


tool_prompt=f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha
Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="What is the weather in Stockholm?"),

]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## Llama 3.2

LLM olmasına rağmen, Llama 3.1'in bir sınırlaması multimodalitedir. Yani, resimler gibi farklı türde girdileri yönlendirme olarak kullanma ve yanıtlar sağlama yeteneğidir. Bu yetenek, Llama 3.2'nin ana özelliklerinden biridir. Bu özellikler ayrıca şunları içerir:

- Multimodalite - hem metin hem de resim yönlendirmelerini değerlendirme yeteneğine sahiptir
- Küçükten Orta boyuta kadar varyasyonlar (11B ve 90B) - bu, esnek dağıtım seçenekleri sunar
- Yalnızca metin varyasyonları (1B ve 3B) - bu, modelin uç / mobil cihazlarda dağıtılmasına olanak tanır ve düşük gecikme sağlar

Multimodal destek, açık kaynak modeller dünyasında büyük bir adımı temsil eder. Aşağıdaki kod örneği, Llama 3.2 90B'den bir görüntünün analizini almak için hem bir görüntü hem de metin yönlendirmesi alır.

### Llama 3.2 ile Multimodal Destek

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "Llama-3.2-90B-Vision-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="sample.jpg",
                        image_format="jpg",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
```

## Öğrenme burada bitmiyor, Yolculuğa devam edin

Bu dersi tamamladıktan sonra, Generative AI bilginizi artırmak için [Generative AI Öğrenme koleksiyonumuzu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) inceleyin!

**Feragatname**: 
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba gösteriyoruz, ancak otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için, profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan dolayı sorumlu değiliz.