<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T10:57:02+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "tr"
}
-->
# Mistral Modelleri ile İnşa Etme

## Giriş

Bu ders şunları kapsayacak:
- Farklı Mistral Modellerini keşfetme
- Her model için kullanım alanlarını ve senaryoları anlama
- Kod örnekleri her modelin benzersiz özelliklerini gösterir.

## Mistral Modelleri

Bu derste, 3 farklı Mistral modelini keşfedeceğiz:
**Mistral Large**, **Mistral Small** ve **Mistral Nemo**.

Bu modellerin her biri Github Model pazarında ücretsiz olarak mevcuttur. Bu not defterindeki kod, bu modelleri kullanarak kodu çalıştıracaktır. AI modelleriyle [prototipleme yapma](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) hakkında daha fazla bilgi için buraya bakın.

## Mistral Large 2 (2407)
Mistral Large 2, Mistral'ın şu anda amiral gemisi modeli olup, kurumsal kullanım için tasarlanmıştır.

Model, orijinal Mistral Large'a aşağıdaki geliştirmeleri sunar:
- Daha Büyük Bağlam Penceresi - 128k vs 32k
- Matematik ve Kodlama Görevlerinde Daha İyi Performans - %76.9 ortalama doğruluk vs %60.4
- Artan çok dilli performans - diller: İngilizce, Fransızca, Almanca, İspanyolca, İtalyanca, Portekizce, Hollandaca, Rusça, Çince, Japonca, Korece, Arapça ve Hintçe.

Bu özelliklerle, Mistral Large şu konularda mükemmeldir:
- *Retrieval Augmented Generation (RAG)* - daha büyük bağlam penceresi sayesinde
- *Fonksiyon Çağırma* - bu model, harici araçlar ve API'lerle entegrasyona olanak tanıyan yerel fonksiyon çağırma özelliğine sahiptir. Bu çağrılar hem paralel hem de ardışık olarak yapılabilir.
- *Kod Üretimi* - bu model Python, Java, TypeScript ve C++ üretiminde mükemmeldir.

### Mistral Large 2 Kullanarak RAG Örneği

Bu örnekte, bir metin belgesi üzerinde bir RAG deseni çalıştırmak için Mistral Large 2 kullanıyoruz. Soru Korece yazılmış ve yazarın üniversite öncesi aktiviteleri hakkında soruyor.

Metin belgesinin ve sorunun gömülü hallerini oluşturmak için Cohere Embeddings Model kullanıyor. Bu örnek için faiss Python paketi bir vektör deposu olarak kullanılıyor.

Mistral modeline gönderilen istem, hem soruları hem de soruya benzer olan alınan parçaları içerir. Model daha sonra doğal dilde bir yanıt sağlar.

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
Mistral Small, Mistral model ailesindeki bir başka model olup, premier/kurumsal kategori altında yer alır. İsminin de belirttiği gibi, bu model Küçük Dil Modeli (SLM) olarak bilinir. Mistral Small kullanmanın avantajları şunlardır:
- Mistral LLM'leri gibi Mistral Large ve NeMo'ya kıyasla maliyet tasarrufu - %80 fiyat düşüşü
- Düşük gecikme - Mistral'ın LLM'lerine kıyasla daha hızlı yanıt
- Esnek - farklı ortamlarda daha az kaynak gereksinimi ile dağıtılabilir.

Mistral Small, şu konularda harikadır:
- Özetleme, duygu analizi ve çeviri gibi metin tabanlı görevler.
- Maliyet etkinliği nedeniyle sık sık istek yapılan uygulamalar
- Kod inceleme ve kod önerileri gibi düşük gecikmeli kod görevleri

## Mistral Small ve Mistral Large Karşılaştırması

Mistral Small ve Large arasındaki gecikme farkını göstermek için aşağıdaki hücreleri çalıştırın.

Aynı istem üzerinde yanıt süreleri arasında 3-5 saniye fark görmelisiniz. Ayrıca yanıt uzunluklarına ve tarzına dikkat edin.

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

Bu derste tartışılan diğer iki modele kıyasla, Mistral NeMo Apache2 Lisansı ile tek ücretsiz modeldir.

Mistral'ın daha önceki açık kaynak LLM'si olan Mistral 7B'ye bir yükseltme olarak görülmektedir.

NeMo modelinin bazı diğer özellikleri şunlardır:

- *Daha verimli tokenizasyon:* Bu model, daha yaygın kullanılan tiktoken yerine Tekken tokenlaştırıcıyı kullanır. Bu, daha fazla dil ve kod üzerinde daha iyi performans sağlar.

- *İnce Ayar:* Temel model ince ayar için kullanılabilir. Bu, ince ayar gerektirebilecek kullanım senaryoları için daha fazla esneklik sağlar.

- *Yerel Fonksiyon Çağırma* - Mistral Large gibi, bu model fonksiyon çağırma konusunda eğitilmiştir. Bu, ilk açık kaynak modellerden biri olarak benzersiz kılar.

### Tokenizer Karşılaştırması

Bu örnekte, Mistral NeMo'nun tokenizasyonu Mistral Large ile karşılaştırılarak incelenecektir.

Her iki örnek de aynı istemi alır ancak NeMo'nun daha az token geri döndüğünü görmelisiniz.

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

## Öğrenme burada bitmez, Yolculuğa Devam Edin

Bu dersi tamamladıktan sonra, Generative AI bilginizi geliştirmeye devam etmek için [Generative AI Öğrenme koleksiyonumuzu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) inceleyin!

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çabalasak da, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.