<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:09:50+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "tr"
}
-->
# Meta Aile Modelleri ile İnşa Etmek

## Giriş

Bu derste şunlar ele alınacak:

- İki ana Meta aile modeli olan Llama 3.1 ve Llama 3.2’nin keşfi  
- Her modelin kullanım alanları ve senaryolarının anlaşılması  
- Her modelin benzersiz özelliklerini gösteren kod örneği  

## Meta Aile Modelleri

Bu derste, Meta ailesinden veya "Llama Sürüsü"nden 2 modeli inceleyeceğiz: Llama 3.1 ve Llama 3.2

Bu modeller farklı varyantlarda sunulmakta ve GitHub Model pazarında bulunabilir. GitHub Modelleri kullanarak [AI modelleri ile prototip oluşturma](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) hakkında daha fazla bilgi için buraya bakabilirsiniz.

Model Varyantları:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*Not: Llama 3 de GitHub Modellerinde mevcut ancak bu derste ele alınmayacak*

## Llama 3.1

405 Milyar Parametre ile Llama 3.1 açık kaynak LLM kategorisine girer.

Bu model, önceki sürüm Llama 3’e göre şu geliştirmeleri sunar:

- Daha büyük bağlam penceresi - 128k token vs 8k token  
- Daha yüksek Maksimum Çıktı Token sayısı - 4096 vs 2048  
- Daha iyi Çokdillilik Desteği - eğitim token sayısındaki artış sayesinde  

Bunlar, Llama 3.1’in GenAI uygulamaları geliştirirken daha karmaşık kullanım senaryolarını yönetmesini sağlar, örneğin:  
- Native Function Calling - LLM iş akışının dışındaki harici araç ve fonksiyonları çağırabilme yeteneği  
- Daha iyi RAG Performansı - daha büyük bağlam penceresi sayesinde  
- Sentetik Veri Üretimi - ince ayar gibi görevler için etkili veri oluşturabilme  

### Native Function Calling

Llama 3.1, fonksiyon veya araç çağrılarında daha etkili olması için ince ayarlandı. Ayrıca, modelin kullanıcıdan gelen isteme göre kullanılması gerektiğini anlayabileceği iki yerleşik aracı vardır. Bu araçlar:

- **Brave Search** - Web araması yaparak güncel bilgiler (örneğin hava durumu) alınabilir  
- **Wolfram Alpha** - Daha karmaşık matematiksel hesaplamalar için kullanılabilir, kendi fonksiyonlarınızı yazmanıza gerek kalmaz  

Ayrıca, LLM’nin çağırabileceği kendi özel araçlarınızı da oluşturabilirsiniz.

Aşağıdaki kod örneğinde:

- Sistem isteminde kullanılabilir araçlar (brave_search, wolfram_alpha) tanımlanır.  
- Belirli bir şehirdeki hava durumu hakkında kullanıcı istemi gönderilir.  
- LLM, Brave Search aracını çağıran bir yanıt verir, bu şu şekilde görünür: `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*Not: Bu örnek sadece araç çağrısını yapar, sonuçları almak için Brave API sayfasında ücretsiz bir hesap oluşturmanız ve fonksiyonu tanımlamanız gerekir*

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

Bir LLM olmasına rağmen, Llama 3.1’in bir sınırlaması multimodalite yani farklı türde girdileri (örneğin görseller) istem olarak kullanabilme ve yanıt verebilme yeteneğidir. Bu yetenek Llama 3.2’nin temel özelliklerinden biridir. Diğer özellikler şunlardır:

- Multimodalite - hem metin hem de görsel istemlerini değerlendirebilme  
- Küçük ve Orta boy varyantlar (11B ve 90B) - esnek dağıtım seçenekleri sunar  
- Sadece metin varyantları (1B ve 3B) - modelin uç / mobil cihazlarda düşük gecikmeyle çalışmasını sağlar  

Multimodal destek, açık kaynak modeller dünyasında büyük bir adımdır. Aşağıdaki kod örneği, hem görsel hem de metin istemi alarak Llama 3.2 90B’den görsel analizi yapar.

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

## Öğrenme burada bitmiyor, yolculuğa devam edin

Bu dersi tamamladıktan sonra, Generative AI bilginizi geliştirmeye devam etmek için [Generative AI Öğrenme koleksiyonumuza](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) göz atabilirsiniz!

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.