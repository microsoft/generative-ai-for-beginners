# Mistral Modelleri ile İnşa Etme

## Giriş

Bu derste şunlar ele alınacaktır:  
- Farklı Mistral Modellerini keşfetmek  
- Her modelin kullanım durumları ve senaryolarını anlamak  
- Her modelin benzersiz özelliklerini gösteren kod örneklerini incelemek.

## Mistral Modelleri

Bu derste, 3 farklı Mistral modelini keşfedeceğiz:  
**Mistral Large**, **Mistral Small** ve **Mistral Nemo**.

Bu modellerin her biri GitHub Model pazarında ücretsiz olarak mevcuttur. Bu not defterindeki kod, bu modelleri kullanarak çalıştırılacaktır. GitHub Modellerini kullanarak [AI modelleri ile prototip oluşturma](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) hakkında daha fazla bilgi için buraya bakabilirsiniz.

## Mistral Large 2 (2407)  
Mistral Large 2, şu anda Mistral'in amiral gemisi modeli olup kurumsal kullanım için tasarlanmıştır.

Model, orijinal Mistral Large modeline göre şu yükseltmeleri sunar:  
- Daha Büyük Bağlam Penceresi - 128k vs 32k  
- Matematik ve Kodlama Görevlerinde Daha İyi Performans - %76,9 ortalama doğruluk vs %60,4  
- Artırılmış çok dilli performans - diller arasında: İngilizce, Fransızca, Almanca, İspanyolca, İtalyanca, Portekizce, Felemenkçe, Rusça, Çince, Japonca, Korece, Arapça ve Hintçe.

Bu özelliklerle Mistral Large aşağıda başarılıdır:  
- *Geri Getirime Dayalı Üretim (RAG)* - daha büyük bağlam penceresi sayesinde  
- *Fonksiyon Çağrısı* - bu model, harici araçlar ve API’lerle entegrasyon sağlayan yerel fonksiyon çağrısı destekler. Bu çağrılar paralel veya ardışık sırayla yapılabilir.  
- *Kod Üretimi* - Python, Java, TypeScript ve C++ üretiminde üstün performans gösterir.

### Mistral Large 2 ile RAG Örneği

Bu örnekte, Mistral Large 2 kullanarak bir metin belgesi üzerinde RAG deseni uygulanmaktadır. Soru Korece yazılmıştır ve yazarın üniversite öncesi faaliyetlerini sormaktadır.

Cohere Embeddings Model, metin belgesi ve sorunun gömme vektörlerini oluşturmak için kullanılır. Bu örnek için faiss Python paketi vektör deposu olarak tercih edilmiştir.

Mistral modeline gönderilen istem, hem soruları hem de soruya benzer şekilde elde edilen parçaları içerir. Model daha sonra doğal dil yanıtı verir.

```python 
pip install faiss-cpu
```
  
```python 
import requests
import numpy as np
import faiss
import os

from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference import EmbeddingsClient

endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-large"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = requests.get('https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/paul_graham/paul_graham_essay.txt')
text = response.text

chunk_size = 2048
chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
len(chunks)

embed_model_name = "cohere-embed-v3-multilingual" 

embed_client = EmbeddingsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token)
)

embed_response = embed_client.embed(
    input=chunks,
    model=embed_model_name
)



text_embeddings = []
for item in embed_response.data:
    length = len(item.embedding)
    text_embeddings.append(item.embedding)
text_embeddings = np.array(text_embeddings)


d = text_embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(text_embeddings)

question = "저자가 대학에 오기 전에 주로 했던 두 가지 일은 무엇이었나요?"

question_embedding = embed_client.embed(
    input=[question],
    model=embed_model_name
)

question_embeddings = np.array(question_embedding.data[0].embedding)


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # mesafe, indeks
retrieved_chunks = [chunks[i] for i in I.tolist()[0]]

prompt = f"""
Context information is below.
---------------------
{retrieved_chunks}
---------------------
Given the context information and not prior knowledge, answer the query.
Query: {question}
Answer:
"""


chat_response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content=prompt),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(chat_response.choices[0].message.content)
```
  

## Mistral Small  
Mistral Small, Mistral ailesinde premier/kurumsal kategori altında yer alan bir başka modeldir. Adından da anlaşılacağı üzere bu model Küçük Dil Modeli (SLM)dir. Mistral Small kullanmanın avantajları şunlardır:  
- Mistral Large ve NeMo gibi Mistral LLM'lerine kıyasla maliyet tasarrufu sağlar - %80 fiyat düşüşü  
- Düşük gecikme süresi - Mistral LLM'lerine göre daha hızlı yanıt  
- Esnek - Gereken kaynaklar konusunda daha az kısıtlamayla farklı ortamlarda konuşlandırılabilir.

Mistral Small için ideal kullanım alanları:  
- Özetleme, duygu analizi ve çeviri gibi metin tabanlı görevler.  
- Sık istek yapılan uygulamalar için maliyet etkinliği nedeniyle uygun.  
- İnceleme ve kod önerileri gibi düşük gecikmeli kod görevleri.

## Mistral Small ile Mistral Large Karşılaştırması

Mistral Small ile Large arasındaki gecikme farklarını göstermek için aşağıdaki hücreleri çalıştırın.

Yanıt sürelerinde 3-5 saniye arasında fark görmelisiniz. Ayrıca aynı istem için yanıt uzunlukları ve stilini not edin.

```python 

import os 
endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-small"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful coding assistant."),
        UserMessage(content="Can you write a Python function to the fizz buzz test?"),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(response.choices[0].message.content)

```
  
```python 

import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-large"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful coding assistant."),
        UserMessage(content="Can you write a Python function to the fizz buzz test?"),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(response.choices[0].message.content)

```
  

## Mistral NeMo

Bu derste ele alınan diğer iki modele kıyasla, Mistral NeMo Apache2 Lisansıyla sunulan tek ücretsiz modeldir.

Mistral NeMo, Mistral’in önceki açık kaynak LLM’si olan Mistral 7B’ye bir yükseltme olarak görülmektedir.

NeMo modelinin diğer bazı özellikleri şunlardır:

- *Daha verimli tokenizasyon:* Bu model, daha yaygın kullanılan tiktoken yerine Tekken tokenlaştırıcıyı kullanır. Bu sayede daha fazla dil ve kod üzerinde daha iyi performans sağlar.

- *İnce ayar yapabilme:* Temel model ince ayar yapılabilir olarak sunulmaktadır. Bu, ince ayarın gerekli olabileceği kullanım durumlarına daha fazla esneklik katmaktadır.

- *Yerel Fonksiyon Çağrısı* - Mistral Large gibi, bu model de fonksiyon çağrısı üzerine eğitilmiştir. Bu, onu ilk açık kaynak modellerinden biri olarak benzersiz kılar.

### Tokenlaştırıcıların Karşılaştırılması

Bu örnekte, Mistral NeMo’nun tokenizasyonu Mistral Large ile nasıl ele aldığına bakacağız.

Her iki örnek de aynı istemi alır ancak NeMo’nun Mistral Large’dan daha az token döndürdüğünü görmelisiniz.

```bash
pip install mistral-common
```
  
```python 
# Gerekli paketleri içe aktar:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral belirleyicisini yükle

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Mesajlar listesini belirleyiciye dönüştür
tokenized = tokenizer.encode_chat_completion(
    ChatCompletionRequest(
        tools=[
            Tool(
                function=Function(
                    name="get_current_weather",
                    description="Get the current weather",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA",
                            },
                            "format": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "The temperature unit to use. Infer this from the user's location.",
                            },
                        },
                        "required": ["location", "format"],
                    },
                )
            )
        ],
        messages=[
            UserMessage(content="What's the weather like today in Paris"),
        ],
        model=model_name,
    )
)
tokens, text = tokenized.tokens, tokenized.text

# Belirteç sayısını say
print(len(tokens))
```
  
```python
# Gerekli paketleri içe aktar:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral tokenlaştırıcısını yükle

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Bir mesaj listesini tokenle
tokenized = tokenizer.encode_chat_completion(
    ChatCompletionRequest(
        tools=[
            Tool(
                function=Function(
                    name="get_current_weather",
                    description="Get the current weather",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA",
                            },
                            "format": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "The temperature unit to use. Infer this from the user's location.",
                            },
                        },
                        "required": ["location", "format"],
                    },
                )
            )
        ],
        messages=[
            UserMessage(content="What's the weather like today in Paris"),
        ],
        model=model_name,
    )
)
tokens, text = tokenized.tokens, tokenized.text

# Token sayısını say
print(len(tokens))
```
  

## Öğrenme burada bitmez, yolculuğa devam edin

Bu dersi tamamladıktan sonra, Generative AI bilgi seviyenizi artırmak için [Generative AI Öğrenme koleksiyonumuza](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) göz atmayı unutmayın!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Sorumluluk Reddi**:
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstermemize rağmen, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilindeki hali ile resmi ve yetkili kaynak olarak kabul edilmelidir. Önemli bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum farklılıklarından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->