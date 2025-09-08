<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T18:59:49+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "tr"
}
-->
# Mistral Modelleri ile Çalışmak

## Giriş

Bu derste şunlar ele alınacaktır:  
- Farklı Mistral Modellerinin keşfi  
- Her modelin kullanım alanları ve senaryolarının anlaşılması  
- Kod örnekleri ile her modelin benzersiz özelliklerinin gösterilmesi.

## Mistral Modelleri

Bu derste, 3 farklı Mistral modeli incelenecektir:  
**Mistral Large**, **Mistral Small** ve **Mistral Nemo**.

Bu modellerin her biri Github Model pazarında ücretsiz olarak mevcuttur. Bu not defterindeki kodlar, bu modelleri kullanarak çalıştırılacaktır. Github Modelleri kullanarak [AI modelleri ile prototip oluşturma](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) hakkında daha fazla bilgi için buraya bakabilirsiniz.

## Mistral Large 2 (2407)  
Mistral Large 2, şu anda Mistral’ın amiral gemisi modeli olup kurumsal kullanım için tasarlanmıştır.

Model, orijinal Mistral Large modeline göre şu geliştirmeleri sunar:  
- Daha büyük bağlam penceresi - 128k vs 32k  
- Matematik ve Kodlama görevlerinde daha iyi performans - %76.9 ortalama doğruluk vs %60.4  
- Artan çok dilli performans - desteklenen diller: İngilizce, Fransızca, Almanca, İspanyolca, İtalyanca, Portekizce, Hollandaca, Rusça, Çince, Japonca, Korece, Arapça ve Hintçe.

Bu özelliklerle Mistral Large şu alanlarda öne çıkar:  
- *Retrieval Augmented Generation (RAG)* - daha büyük bağlam penceresi sayesinde  
- *Fonksiyon Çağrısı* - bu model, dış araçlar ve API’lerle entegrasyon sağlayan yerel fonksiyon çağrısı özelliğine sahiptir. Bu çağrılar paralel veya ardışık olarak yapılabilir.  
- *Kod Üretimi* - Python, Java, TypeScript ve C++ kod üretiminde başarılıdır.

### Mistral Large 2 ile RAG Örneği

Bu örnekte, Mistral Large 2 kullanılarak bir metin belgesi üzerinde RAG deseni uygulanmaktadır. Soru Korece yazılmış olup yazarın üniversite öncesi faaliyetleri hakkında bilgi istemektedir.

Metin belgesi ve soru için gömme (embedding) oluşturmak üzere Cohere Embeddings Modeli kullanılır. Bu örnekte, vektör deposu olarak faiss Python paketi tercih edilmiştir.

Mistral modeline gönderilen prompt, hem soruları hem de soruya benzer bulunan metin parçalarını içerir. Model daha sonra doğal dilde yanıt verir.

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

question = "저자가 대학에 오기 전에 주로 했던 두 가지 일은 무엇이었나요?？"

question_embedding = embed_client.embed(
    input=[question],
    model=embed_model_name
)

question_embeddings = np.array(question_embedding.data[0].embedding)


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # distance, index
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
Mistral Small, Mistral ailesinin premier/kurumsal kategorisindeki bir diğer modelidir. Adından da anlaşılacağı üzere, bu model Küçük Dil Modeli (SLM) olarak tasarlanmıştır. Mistral Small kullanmanın avantajları şunlardır:  
- Mistral Large ve NeMo gibi Mistral LLM’lerine kıyasla maliyet tasarrufu - %80 fiyat düşüşü  
- Düşük gecikme süresi - Mistral’ın diğer LLM’lerine göre daha hızlı yanıt  
- Esneklik - farklı ortamlarda, gereken kaynaklar konusunda daha az kısıtlamayla dağıtılabilir.

Mistral Small şu görevler için idealdir:  
- Özetleme, duygu analizi ve çeviri gibi metin tabanlı görevler  
- Sık istek yapılan uygulamalar için maliyet etkinliği nedeniyle  
- İnceleme ve kod önerileri gibi düşük gecikmeli kod görevleri

## Mistral Small ve Mistral Large Karşılaştırması

Mistral Small ve Large arasındaki gecikme farkını göstermek için aşağıdaki hücreleri çalıştırabilirsiniz.

Yanıt süreleri arasında 3-5 saniye fark görmelisiniz. Ayrıca aynı prompt için yanıt uzunlukları ve tarzına da dikkat edin.

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

Bu derste ele alınan diğer iki modele kıyasla, Mistral NeMo Apache2 Lisansına sahip tek ücretsiz modeldir.

Mistral NeMo, Mistral’ın önceki açık kaynak LLM’si olan Mistral 7B’nin bir yükseltmesi olarak görülür.

NeMo modelinin diğer bazı özellikleri şunlardır:

- *Daha verimli tokenizasyon:* Bu model, yaygın kullanılan tiktoken yerine Tekken tokenizer kullanır. Bu sayede daha fazla dil ve kod üzerinde daha iyi performans sağlar.

- *İnce ayar (Finetuning):* Temel model ince ayar için kullanılabilir. Bu, ince ayar gerektiren kullanım senaryoları için daha fazla esneklik sunar.

- *Yerel Fonksiyon Çağrısı* - Mistral Large gibi, bu model de fonksiyon çağrısı eğitimi almıştır. Bu özelliğiyle açık kaynak modeller arasında öncü konumdadır.

### Tokenizer Karşılaştırması

Bu örnekte, Mistral NeMo’nun tokenizasyonu Mistral Large ile nasıl karşılaştırdığına bakacağız.

Her iki örnek de aynı prompt’u kullanır ancak NeMo’nun Mistral Large’a kıyasla daha az token döndürdüğünü göreceksiniz.

```bash
pip install mistral-common
```

```python 
# Import needed packages:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Load Mistral tokenizer

model_name = "open-mistral-nemo	"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenize a list of messages
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
                                "description": "The temperature unit to use. Infer this from the users location.",
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

# Count the number of tokens
print(len(tokens))
```

```python
# Import needed packages:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Load Mistral tokenizer

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenize a list of messages
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
                                "description": "The temperature unit to use. Infer this from the users location.",
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

# Count the number of tokens
print(len(tokens))
```

## Öğrenme burada bitmiyor, yolculuğa devam edin

Bu dersi tamamladıktan sonra, Generative AI bilginizi geliştirmeye devam etmek için [Generative AI Öğrenme koleksiyonumuza](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) göz atabilirsiniz!

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.