# Membina dengan Model Mistral

## Pengenalan

Pelajaran ini akan merangkumi:
- Meneroka pelbagai Model Mistral
- Memahami kes penggunaan dan senario untuk setiap model
- Meneroka contoh kod yang menunjukkan ciri unik setiap model.

## Model Mistral

Dalam pelajaran ini, kami akan meneroka 3 model Mistral yang berbeza:
**Mistral Large**, **Mistral Small** dan **Mistral Nemo**.

Setiap model ini tersedia secara percuma di [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Kod dalam buku nota ini akan menggunakan model-model ini untuk menjalankan kod.

> **Nota:** GitHub Models akan dihentikan pada akhir Julai 2026. Berikut adalah maklumat lanjut mengenai penggunaan [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) untuk prototaip dengan model AI.


## Mistral Large 2 (2407)
Mistral Large 2 kini merupakan model utama dari Mistral dan direka untuk kegunaan perusahaan.

Model ini adalah peningkatan kepada Mistral Large asal dengan menawarkan
-  Tetingkap Konteks Lebih Besar - 128k berbanding 32k
-  Prestasi lebih baik dalam Tugasan Matematik dan Pengaturcaraan - ketepatan purata 76.9% berbanding 60.4%
-  Peningkatan prestasi pelbagai bahasa - bahasa termasuk: Inggeris, Perancis, Jerman, Sepanyol, Itali, Portugis, Belanda, Rusia, Cina, Jepun, Korea, Arab dan Hindi.

Dengan ciri-ciri ini, Mistral Large cemerlang dalam
- *Penghasilan Diperkaya Pengambilan (RAG)* - disebabkan oleh tetingkap konteks yang lebih besar
- *Panggilan Fungsi* - model ini mempunyai panggilan fungsi asli yang membolehkan integrasi dengan alat dan API luaran. Panggilan ini boleh dibuat secara selari atau satu demi satu secara berurutan.
- *Penjanaan Kod* - model ini cemerlang dalam penjanaan Python, Java, TypeScript dan C++.

### Contoh RAG menggunakan Mistral Large 2

Dalam contoh ini, kami menggunakan Mistral Large 2 untuk menjalankan corak RAG ke atas dokumen teks. Soalan ditulis dalam bahasa Korea dan bertanya tentang aktiviti pengarang sebelum kolej.

Ia menggunakan Model Penjanaan Cohere untuk mencipta penjanaan bagi dokumen teks serta soalan tersebut. Untuk sampel ini, ia menggunakan pakej Python faiss sebagai stor vektor.

Arahan yang dihantar ke model Mistral termasuk soalan dan potongan yang diperoleh yang serupa dengan soalan tersebut. Model kemudian menyediakan respon dalam bahasa semula jadi.

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

# Dapatkan ini dari halaman "Gambaran Keseluruhan" projek Microsoft Foundry anda
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # jarak, indeks
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
Mistral Small adalah satu lagi model dalam keluarga Model Mistral di bawah kategori utama/perusahaan. Seperti namanya, model ini adalah Model Bahasa Kecil (SLM). Kelebihan menggunakan Mistral Small adalah:
- Penjimatan Kos berbanding LLM Mistral seperti Mistral Large dan NeMo - kejatuhan harga 80%
- Latensi rendah - respons lebih pantas berbanding LLM Mistral
- Fleksibel - boleh dideploy di pelbagai persekitaran dengan sekatan sumber yang kurang diperlukan.


Mistral Small sangat sesuai untuk:
- Tugasan berasaskan teks seperti ringkasan, analisis sentimen dan terjemahan.
- Aplikasi yang kerap membuat permintaan kerana kosnya yang berkesan
- Tugasan kod latensi rendah seperti semakan dan cadangan kod

## Perbandingan Mistral Small dan Mistral Large

Untuk menunjukkan perbezaan latensi antara Mistral Small dan Large, jalankan sel di bawah.

Anda akan melihat perbezaan masa respons antara 3-5 saat. Juga perhatikan panjang dan gaya respons untuk arahan yang sama.

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

Berbanding dengan dua model lain yang dibincangkan dalam pelajaran ini, Mistral NeMo adalah satu-satunya model percuma dengan Lesen Apache2.

Ia dilihat sebagai peningkatan kepada LLM sumber terbuka terdahulu dari Mistral, Mistral 7B.

Beberapa ciri lain model NeMo adalah:

- *Tokenisasi lebih cekap:* Model ini menggunakan penanda Tekken berbanding tiktoken yang lebih biasa digunakan. Ini membolehkan prestasi lebih baik untuk lebih banyak bahasa dan kod.

- *Pelarasan Halus (Finetuning):* Model asas tersedia untuk pelarasan halus. Ini memberikan lebih fleksibiliti untuk kes penggunaan yang memerlukan pelarasan halus.

- *Panggilan Fungsi Asli* - Seperti Mistral Large, model ini telah dilatih untuk panggilan fungsi. Ini menjadikannya unik sebagai salah satu model sumber terbuka pertama yang berbuat demikian.


### Perbandingan Penanda Token

Dalam sampel ini, kita akan lihat bagaimana Mistral NeMo mengendalikan tokenisasi berbanding Mistral Large.

Kedua-dua sampel mengambil arahan yang sama tetapi anda akan melihat bahawa NeMo mengembalikan token yang lebih sedikit berbanding Mistral Large.

```bash
pip install mistral-common
```

```python 
# Import pakej yang diperlukan:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Muatkan penukar token Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Tukar senarai mesej kepada token
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

# Kira bilangan token
print(len(tokens))
```

```python
# Import pakej yang diperlukan:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Muatkan penukar kata Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tukar senarai mesej kepada token
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

# Kira bilangan token
print(len(tokens))
```

## Pembelajaran tidak berhenti di sini, teruskan perjalanan

Selepas menyelesaikan pelajaran ini, lihat koleksi [Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif anda!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->