# Meta Ailesi Modelleri ile İnşa Etmek 

## Giriş 

Bu ders şunları kapsayacak: 

- İki ana Meta aile modeli - Llama 3.1 ve Llama 3.2'nin keşfi 
- Her modelin kullanım durumları ve senaryolarının anlaşılması 
- Her modelin benzersiz özelliklerini gösteren kod örneği 


## Meta Ailesi Modelleri 

Bu derste, Meta ailesinden veya "Llama Sürüsü"nden 2 modeli inceleyeceğiz - Llama 3.1 ve Llama 3.2.

Bu modeller farklı varyantlarda gelir ve [Microsoft Foundry Models katalogunda](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) mevcuttur.

> **Not:** GitHub Modelleri Temmuz 2026 sonunda emekliye ayrılıyor. AI modelleri ile prototip oluşturmak için [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) kullanımı hakkında daha fazla detay burada.

Model Varyantları: 
- Llama 3.1 - 70B Öğretim 
- Llama 3.1 - 405B Öğretim 
- Llama 3.2 - 11B Görsel Öğretim 
- Llama 3.2 - 90B Görsel Öğretim 

*Not: Llama 3 ayrıca Microsoft Foundry Models'de mevcuttur ancak bu ders kapsamında ele alınmayacaktır*

## Llama 3.1 

405 Milyar Parametre ile Llama 3.1 açık kaynak LLM kategorisine girer. 

Model, önceki sürüm Llama 3’e kıyasla şu iyileştirmeleri sunar: 

- Daha büyük bağlam penceresi - 8k token yerine 128k token 
- Daha büyük Maksimum Çıktı Token'ları - 2048 yerine 4096 
- Daha iyi Çokdillilik Desteği - eğitim tokenlarında artış sayesinde 

Bunlar, Llama 3.1’in GenAI uygulamaları oluştururken daha karmaşık kullanım durumlarıyla başa çıkabilmesini sağlar, örneğin: 
- Yerel Fonksiyon Çağrısı - LLM iş akışının dışındaki dış araçları ve fonksiyonları çağırabilme yeteneği
- Daha İyi RAG Performansı - daha yüksek bağlam penceresi sayesinde 
- Sentetik Veri Üretimi - ince ayar gibi görevler için etkili veri oluşturabilme yeteneği 

### Yerel Fonksiyon Çağrısı 

Llama 3.1, fonksiyon veya araç çağrılarında daha etkili olması için ince ayar yapılmıştır. Ayrıca, modelin kullanıcıdan gelen isteme bağlı olarak kullanılması gerektiğini belirleyebileceği iki yerleşik aracı vardır. Bu araçlar: 

- **Brave Search** - Web araması yaparak güncel bilgiler (örneğin hava durumu) alabilir 
- **Wolfram Alpha** - Daha karmaşık matematiksel hesaplamalar için kullanılabilir, kendi fonksiyonlarınızı yazmanız gerekmez. 

Ayrıca LLM’nin çağırabileceği kendi özel araçlarınızı da oluşturabilirsiniz. 

Aşağıdaki kod örneğinde: 

- Sistem isteminde mevcut araçlar (brave_search, wolfram_alpha) tanımlanır. 
- Belirli bir şehirdeki hava durumu hakkında soran bir kullanıcı istemi gönderilir. 
- LLM, Brave Search aracını çağıran şu şekilde bir cevap verecektir: `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Not: Bu örnek yalnızca araç çağrısı yapar; sonuçları almak isterseniz Brave API sayfasında ücretsiz bir hesap oluşturmalı ve fonksiyonun kendisini tanımlamalısınız.

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

Llama 3.1 bir LLM olmasına rağmen, bir sınırlaması çok modluluğunun olmamasıdır. Yani, görsel gibi farklı türde girişleri istem olarak kullanamaması ve yanıt vermemesi. Bu yetenek Llama 3.2’nin ana özelliklerinden biridir. Bu özellikler ayrıca şunları içerir: 

- Çok modluluk - hem metin hem görsel istemleri değerlendirebilme yeteneği 
- Küçük ila Orta boy varyantlar (11B ve 90B) - esnek dağıtım seçenekleri sunar, 
- Sadece metin varyantları (1B ve 3B) - bu modelin uç / mobil cihazlarda dağıtılmasını sağlar ve düşük gecikme sunar 

Çok modlu destek, açık kaynak modeller dünyasında büyük bir adımdır. Aşağıdaki kod örneği hem bir görsel hem de metin istemi alarak Llama 3.2 90B’den görsel analizi alır. 


### Llama 3.2 ile Çok Modlu Destek

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

Bu dersi tamamladıktan sonra, [Üretici AI Öğrenme koleksiyonumuza](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) göz atarak Üretici AI bilginizi artırmaya devam edin!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->