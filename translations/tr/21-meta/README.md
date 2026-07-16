# Meta Ailesi Modelleri ile İnşa Etmek

## Giriş

Bu ders şunları kapsayacak:

- İki ana Meta aile modeli - Llama 3.1 ve Llama 3.2'yi keşfetmek
- Her modelin kullanım senaryolarını anlamak
- Her modelin benzersiz özelliklerini göstermek için kod örneği


## Meta Aile Modelleri

Bu derste, Meta ailesinden veya "Llama Sürüsü"nden 2 modeli keşfedeceğiz - Llama 3.1 ve Llama 3.2.

Bu modeller farklı varyantlarda gelir ve [Microsoft Foundry Modelleri kataloğunda](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) mevcuttur.

> **Not:** GitHub Modelleri Temmuz 2026 sonunda kullanımdan kaldırılacaktır. AI modelleriyle prototip oluşturmak için [Microsoft Foundry Modelleri](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) hakkında daha fazla bilgi burada bulunmaktadır.

Model Varyantları:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Not: Llama 3, Microsoft Foundry Modellerinde de mevcuttur ancak bu derste ele alınmayacaktır*

## Llama 3.1

405 Milyar Parametre ile Llama 3.1 açık kaynak LLM kategorisine girer.

Model, önceki sürüm Llama 3'e şu yönden geliştirmeler sunar:

- Daha büyük bağlam penceresi - 128k token vs 8k token
- Daha büyük Maksimum Çıktı Tokenı - 4096 vs 2048
- Daha iyi Çok-dilli Destek - eğitim token sayısındaki artış sayesinde

Bunlar Llama 3.1'in GenAI uygulamaları geliştirirken daha karmaşık kullanım senaryolarını ele almasını sağlar:
- Yerel Fonksiyon Çağırma - LLM iş akışının dışındaki harici araçları ve fonksiyonları çağırabilme yeteneği
- Daha İyi RAG Performansı - daha yüksek bağlam penceresi sayesinde
- Sentetik Veri Üretimi - ince ayar gibi görevler için etkili veri oluşturabilme yeteneği

### Yerel Fonksiyon Çağırma

Llama 3.1, fonksiyon veya araç çağrılarında daha etkili olmak üzere ince ayar yapılmıştır. Ayrıca model, kullanıcıdan gelen isteme bağlı olarak kullanılması gereken iki yerleşik araca sahiptir. Bu araçlar:

- **Brave Search** - Web araması yaparak hava durumu gibi güncel bilgileri almak için kullanılabilir
- **Wolfram Alpha** - Kendi fonksiyonlarınızı yazmanıza gerek kalmadan daha karmaşık matematiksel hesaplamalar için kullanılabilir.

Kendi özel araçlarınızı da oluşturup LLM'in çağırmasını sağlayabilirsiniz.

Aşağıdaki kod örneğinde:

- Sistem isteminde mevcut araçlar (brave_search, wolfram_alpha) tanımlanır.
- Belirli bir şehirdeki hava durumunu soran kullanıcı istemi gönderilir.
- LLM, Brave Search aracını çağıran şu şekilde yanıt verir: `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Not: Bu örnek sadece araç çağrısı yapar, sonuçları almak isterseniz Brave API sayfasında ücretsiz hesap oluşturmalı ve fonksiyonun kendisini tanımlamalısınız.*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Bunları Microsoft Foundry projenizin "Genel Bakış" sayfasından alın
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Meta-Llama-3.1-405B-Instruct"

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

Llama 3.1 bir LLM olmasına rağmen, bir sınırlama olarak multimodalite desteği yoktur. Yani, görüntü gibi farklı giriş türlerini istem olarak kullanıp yanıt verme yeteneği yoktur. Bu yetenek Llama 3.2'nin ana özelliklerinden biridir. Bu özellikler ayrıca şunları içerir:

- Multimodalite - hem metin hem de görüntü istemlerini değerlendirebilme kabiliyeti
- Küçük ve Orta boy varyantlar (11B ve 90B) - esnek dağıtım seçenekleri sağlar
- Sadece metin varyantları (1B ve 3B) - modelin uç / mobil cihazlarda dağıtılmasına olanak verir ve düşük gecikme sunar

Multimodal destek, açık kaynak modeller dünyasında büyük bir adımdır. Aşağıdaki kod örneği hem görüntü hem de metin istemi alarak Llama 3.2 90B tarafından görüntü analizi yapmaktadır.


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

# Bunları Microsoft Foundry projenizin "Genel Bakış" sayfasından alın
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
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

## Öğrenme burada bitmiyor, yolculuğa devam edin

Bu dersi tamamladıktan sonra, [Üretken AI Öğrenme koleksiyonumuzu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) inceleyerek Üretken AI bilginizi geliştirmeye devam edin!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->