# Mistral Modelleri ile İnşa Etme 

## Giriş 

Bu ders şunları kapsayacak: 
- Farklı Mistral Modellerini keşfetmek 
- Her modelin kullanım durumlarını ve senaryolarını anlamak 
- Her modelin benzersiz özelliklerini gösteren kod örneklerini incelemek.

## Mistral Modelleri 

Bu derste, 3 farklı Mistral modelini keşfedeceğiz: 
**Mistral Large**, **Mistral Small** ve **Mistral Nemo**. 

Bu modellerin her biri [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) üzerinde ücretsiz olarak mevcuttur. Bu not defterindeki kod, kodu çalıştırmak için bu modelleri kullanacaktır.

> **Not:** GitHub Modelleri Temmuz 2026 sonunda kapanacaktır. AI modelleriyle prototipleme yapmak için [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) kullanımı hakkında daha fazla bilgiyi buradan alabilirsiniz. 


## Mistral Large 2 (2407)
Mistral Large 2 şu anda Mistral’ın amiral gemisi modelidir ve kurumsal kullanım için tasarlanmıştır. 

Model, orijinal Mistral Large modeline göre şu geliştirmeleri sunar: 
- Daha Büyük Bağlam Penceresi - 128k vs 32k 
- Matematik ve Kodlama Görevlerinde Daha İyi Performans - %76.9 ortalama doğruluk vs %60.4 
- Artan çok dilli performans - diller şunları içerir: İngilizce, Fransızca, Almanca, İspanyolca, İtalyanca, Portekizce, Hollandaca, Rusça, Çince, Japonca, Korece, Arapça ve Hintçe.

Bu özelliklerle, Mistral Large şu konularda mükemmeldir: 
- *Getiri Artırılmış Üretim (RAG)* - daha büyük bağlam penceresi nedeniyle
- *Fonksiyon Çağrısı* - bu model yerel fonksiyon çağrısına sahiptir, bu da harici araçlar ve API'lerle entegrasyona imkan tanır. Bu çağrılar paralel olarak veya sırayla yapılabilir. 
- *Kod Üretimi* - bu model Python, Java, TypeScript ve C++ üretiminde mükemmeldir. 

### Mistral Large 2 kullanarak RAG Örneği 

Bu örnekte, bir metin belgesi üzerinde RAG deseni çalıştırmak için Mistral Large 2 kullanıyoruz. Soru Korece yazılmış ve yazarın üniversite öncesi faaliyetlerini soruyor. 

Metin belgesi ile sorunun gömme (embedding) vektörlerini oluşturmak için Cohere Embeddings Modeli kullanılmaktadır. Bu örnek için vektör deposu olarak faiss Python paketi kullanılmaktadır. 

Mistral modeline gönderilen istem, hem soruları hem de soruya benzer şekilde alınan parçaları içerir. Model daha sonra doğal dil yanıtı sağlar. 

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

# Bunları Microsoft Foundry projenizin "Genel Bakış" sayfasından alın
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-large"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

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
Mistral Small, Mistral ailesinde premier/kurumsal kategori altında başka bir modeldir. İsminin de gösterdiği gibi, bu model Küçük Dil Modelidir (SLM). Mistral Small kullanımının avantajları şunlardır: 
- Mistral LLM'leri gibi Mistral Large ve NeMo ile kıyaslandığında maliyet tasarrufu - %80 fiyat düşüşü
- Düşük gecikme süresi - Mistral’ın LLM'lerine kıyasla daha hızlı yanıt
- Esnek - gerekli kaynaklar konusunda daha az kısıtlamalarla farklı ortamlarda dağıtılabilir. 


Mistral Small için ideal kullanım alanları: 
- Özetleme, duygu analizi ve çeviri gibi metin tabanlı görevler. 
- Maliyet etkinliği nedeniyle sık sık istek yapılan uygulamalar 
- İnceleme ve kod önerileri gibi düşük gecikmeli kod görevleri 

## Mistral Small ve Mistral Large karşılaştırması 

Mistral Small ve Large arasındaki gecikme farklarını göstermek için aşağıdaki hücreleri çalıştırın. 

Aynı istem için yanıt süreleri arasında 3-5 saniye fark görmelisiniz. Ayrıca yanıt uzunluklarına ve tarzına dikkat edin.  

```python 

import os 
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-small"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

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

endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-large"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

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

Bu derste ele alınan diğer iki modele kıyasla, Mistral NeMo Apache2 Lisansına sahip tek ücretsiz modeldir. 

Mistral NeMo, Mistral’ın önceki açık kaynak LLM'si olan Mistral 7B için bir yükseltme olarak görülmektedir. 

NeMo modelinin diğer bazı özellikleri şunlardır: 

- *Daha verimli tokenizasyon:* Bu model, daha yaygın kullanılan tiktoken yerine Tekken tokenizer kullanır. Bu, daha fazla dil ve kodda daha iyi performans sağlar. 

- *İnce Ayar (Finetuning):* Temel model ince ayar için kullanılabilir. Bu, ince ayarın gerekli olabileceği kullanım durumları için daha fazla esneklik sağlar. 

- *Yerleşik Fonksiyon Çağrısı* - Mistral Large gibi, bu model fonksiyon çağrısı için eğitilmiştir. Bu, onu bu yetkiye sahip ilk açık kaynak modellerden biri olarak benzersiz kılar. 


### Tokenizer Karşılaştırması 

Bu örnekte, Mistral NeMo'nun tokenizasyonunu Mistral Large ile karşılaştıracağız. 

Her iki örnek aynı istemi alır ancak NeMo’nun Mistral Large’dan daha az token döndürdüğünü görmelisiniz. 

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

# Mistral tokenizer yükle

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Bir mesajlar listesi tokenize et
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

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Bir mesaj listesini belirtkleştir
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

## Öğrenme burada bitmiyor, yolculuğa devam edin

Bu dersi tamamladıktan sonra, [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) koleksiyonumuzu inceleyerek Üretken AI bilginizi geliştirmeye devam edin!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->