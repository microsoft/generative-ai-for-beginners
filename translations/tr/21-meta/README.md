<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:11:07+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "tr"
}
-->
# Meta Ailesi Modelleriyle İnşa Etme

## Giriş

Bu derste ele alınacak konular:

- İki ana Meta ailesi modeli - Llama 3.1 ve Llama 3.2'yi keşfetme
- Her modelin kullanım alanları ve senaryolarını anlama
- Her modelin benzersiz özelliklerini gösteren kod örneği

## Meta Ailesi Modelleri

Bu derste Meta ailesinden veya "Llama Sürüsü"nden 2 modeli - Llama 3.1 ve Llama 3.2 - keşfedeceğiz.

Bu modeller farklı varyantlarda gelir ve GitHub Model pazarında mevcuttur. AI modelleriyle [prototip oluşturma](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) için GitHub Modellerini kullanma hakkında daha fazla bilgi burada.

Model Varyantları:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Not: Llama 3 de GitHub Modellerinde mevcuttur ancak bu derste ele alınmayacaktır*

## Llama 3.1

405 Milyar Parametre ile Llama 3.1, açık kaynak LLM kategorisine girer.

Model, önceki Llama 3 sürümüne şu şekilde bir yükseltme sunar:

- Daha geniş bağlam penceresi - 128k token vs 8k token
- Daha büyük Maksimum Çıktı Tokenları - 4096 vs 2048
- Daha iyi Çok Dilli Destek - eğitim tokenlarının artışı nedeniyle

Bu özellikler, Llama 3.1'in GenAI uygulamaları oluştururken daha karmaşık kullanım senaryolarını ele almasını sağlar:
- Yerel Fonksiyon Çağrısı - LLM iş akışının dışında harici araçları ve fonksiyonları çağırma yeteneği
- Daha İyi RAG Performansı - daha yüksek bağlam penceresi nedeniyle
- Sentetik Veri Üretimi - ince ayar gibi görevler için etkili veri oluşturma yeteneği

### Yerel Fonksiyon Çağrısı

Llama 3.1, fonksiyon veya araç çağrıları yapmada daha etkili olacak şekilde ince ayar yapılmıştır. Ayrıca, kullanıcının isteğine göre kullanılacak iki yerleşik araç vardır. Bu araçlar:

- **Brave Search** - Web araması yaparak hava durumu gibi güncel bilgileri almak için kullanılabilir
- **Wolfram Alpha** - Daha karmaşık matematiksel hesaplamalar için kullanılabilir, böylece kendi fonksiyonlarınızı yazmanıza gerek kalmaz.

Ayrıca LLM'in çağırabileceği kendi özel araçlarınızı da oluşturabilirsiniz.

Aşağıdaki kod örneğinde:

- Sisteme mevcut araçları (brave_search, wolfram_alpha) tanımlarız.
- Belirli bir şehirdeki hava durumu hakkında bir kullanıcı isteği göndeririz.
- LLM, Brave Search aracını çağırarak şu şekilde yanıt verecektir `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Not: Bu örnek sadece araç çağrısı yapar, sonuçları almak isterseniz, Brave API sayfasında ücretsiz bir hesap oluşturmanız ve fonksiyonu tanımlamanız gerekecektir*

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

Bir LLM olmasına rağmen, Llama 3.1'in bir sınırlaması çoklu modluluk eksikliğidir. Yani, farklı türdeki girdileri, örneğin resimleri istem olarak kullanma ve yanıt sağlama yeteneği. Bu yetenek, Llama 3.2'nin ana özelliklerinden biridir. Bu özellikler ayrıca şunları içerir:

- Çoklu Modluluk - hem metin hem de görüntü istemlerini değerlendirme yeteneği
- Küçük ve Orta boyut varyasyonları (11B ve 90B) - bu, esnek dağıtım seçenekleri sunar,
- Yalnızca metin varyasyonları (1B ve 3B) - bu, modelin uç / mobil cihazlarda dağıtılmasını sağlar ve düşük gecikme süresi sunar

Çoklu modluluk desteği, açık kaynak modeller dünyasında büyük bir adımı temsil eder. Aşağıdaki kod örneği, hem bir görüntü hem de metin istemi alarak Llama 3.2 90B'den görüntünün analizini alır.

### Llama 3.2 ile Çoklu Modluluk Desteği

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

Bu dersi tamamladıktan sonra, Generative AI bilginizi geliştirmeye devam etmek için [Generative AI Öğrenme koleksiyonumuzu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) inceleyin!

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından doğabilecek yanlış anlama veya yanlış yorumlamalardan sorumlu değiliz.