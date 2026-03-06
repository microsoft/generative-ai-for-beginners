# Meta Aile Modelleri ile İnşa Etmek

## Giriş

Bu ders şunları kapsayacaktır:

- İki ana Meta aile modelini keşfetmek - Llama 3.1 ve Llama 3.2
- Her model için kullanım durumları ve senaryolarını anlamak
- Her modelin benzersiz özelliklerini göstermek için kod örneği

## Meta Aile Modelleri

Bu derste, Meta ailesinden veya "Llama Sürüsü"nden 2 modeli keşfedeceğiz - Llama 3.1 ve Llama 3.2.

Bu modeller farklı varyantlarda gelir ve GitHub Model pazar yerinde mevcuttur. AI modelleriyle [prototip oluşturmak](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) için GitHub Modellerini kullanma hakkında daha fazla bilgi burada.

Model Varyantları:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct

*Not: Llama 3 de GitHub Modellerinde mevcuttur ancak bu ders kapsamında ele alınmayacaktır*

## Llama 3.1

405 Milyar Parametre ile Llama 3.1, açık kaynak LLM kategorisine girer.

Model, daha önceki Llama 3 sürümüne göre şunları sunan bir yükseltmedir:

- Daha büyük bağlam penceresi - 8k token vs 128k token  
- Daha büyük Maksimum Çıktı Tokeni - 2048 vs 4096  
- Daha iyi Çok Dilli Destek - eğitim token sayısındaki artış sayesinde

Bunlar, Llama 3.1’in GenAI uygulamaları geliştirilirken daha karmaşık kullanım durumlarını ele almasını sağlar, bunlar arasında:
- Yerel Fonksiyon Çağrısı - LLM iş akışı dışındaki harici araçları ve fonksiyonları çağırabilme yeteneği  
- Daha İyi RAG Performansı - daha yüksek bağlam penceresi nedeniyle  
- Sentetik Veri Üretimi - ince ayar gibi görevler için etkili veri oluşturabilme yeteneği

### Yerel Fonksiyon Çağrısı

Llama 3.1, fonksiyon veya araç çağrılarında daha etkili olacak şekilde ince ayar yapılmıştır. Ayrıca modelin, kullanıcının istemine bağlı olarak kullanılmaları gerektiğini belirleyebildiği iki yerleşik aracı vardır. Bu araçlar şunlardır:

- **Brave Search** - Web araması yaparak hava durumu gibi güncel bilgileri almak için kullanılabilir  
- **Wolfram Alpha** - Daha karmaşık matematiksel hesaplamalar için kullanılabilir, böylece kendi fonksiyonlarınızı yazmanız gerekmez.

Kendi özel araçlarınızı da oluşturabilir ve LLM’nin çağırmasını sağlayabilirsiniz.

Aşağıdaki kod örneğinde:

- Sistemde kullanılabilir araçları (brave_search, wolfram_alpha) tanımlıyoruz.  
- Belirli bir şehirde hava durumu hakkında kullanıcı istemi gönderiyoruz.  
- LLM, Brave Search aracına şu şekilde bir çağrı yaparak cevap verecektir `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Not: Bu örnek yalnızca araç çağrısı yapar; sonuçları almak isterseniz, Brave API sayfasında ücretsiz bir hesap oluşturmanız ve fonksiyonu tanımlamanız gerekecektir.*

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

Bir LLM olmasına rağmen, Llama 3.1’in bir sınırlaması çok modlu olmamasıdır. Yani, görüntüler gibi farklı türde girdileri istem olarak kullanamama ve yanıt verememe durumu. Bu yetenek Llama 3.2’nin temel özelliklerinden biridir. Ayrıca bu özellikler şunları içerir:

- Çok modluluk - hem metin hem de görüntü istemlerini değerlendirebilme  
- Küçük ve Orta boy varyantlar (11B ve 90B) - esnek dağıtım seçenekleri sağlıyor  
- Sadece metin varyantları (1B ve 3B) - modelin uç / mobil cihazlarda dağıtılmasına ve düşük gecikme sağlamasına olanak tanır

Çok modlu destek, açık kaynak modeller dünyasında büyük bir adımdır. Aşağıdaki kod örneği, hem bir görüntü hem de metin istemi alarak Llama 3.2 90B’den görüntü analizi alır.

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

Bu dersi tamamladıktan sonra, Generative AI bilgi seviyenizi artırmak için [Generative AI Öğrenme koleksiyonumuzu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) inceleyin!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi tavsiye edilir. Bu çevirinin kullanımı sonucunda ortaya çıkabilecek herhangi bir yanlış anlama veya yorumlama nedeniyle sorumluluk kabul edilmemektedir.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->