# Membina dengan Model Mistral

## Pengenalan

Pelajaran ini akan merangkumi:
- Meneroka pelbagai Model Mistral
- Memahami kes penggunaan dan senario untuk setiap model
- Meneroka contoh kod yang menunjukkan ciri unik setiap model.

## Model Mistral

Dalam pelajaran ini, kita akan meneroka 3 model Mistral yang berbeza:
**Mistral Large**, **Mistral Small** dan **Mistral Nemo**.

Setiap model ini tersedia secara percuma di pasar Model GitHub. Kod dalam buku nota ini akan menggunakan model-model ini untuk menjalankan kod. Berikut adalah maklumat lanjut tentang menggunakan Model GitHub untuk [membuat prototaip dengan model AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 kini adalah model utama dari Mistral dan direka untuk kegunaan perusahaan.

Model ini merupakan peningkatan kepada Mistral Large asal dengan menawarkan
- Tetingkap Konteks Lebih Besar - 128k berbanding 32k
- Prestasi lebih baik untuk Tugasan Matematik dan Pengkodan - ketepatan purata 76.9% berbanding 60.4%
- Peningkatan prestasi berbilang bahasa - bahasa termasuk: Inggeris, Perancis, Jerman, Sepanyol, Itali, Portugis, Belanda, Rusia, Cina, Jepun, Korea, Arab, dan Hindi.

Dengan ciri-ciri ini, Mistral Large cemerlang dalam
- *Generasi Augmentasi Pemulihan (RAG)* - disebabkan oleh tetingkap konteks yang lebih besar
- *Pemanggilan Fungsi* - model ini mempunyai pemanggilan fungsi asli yang membolehkan integrasi dengan alat dan API luaran. Panggilan ini boleh dibuat secara selari atau satu demi satu secara berurutan.
- *Penjanaan Kod* - model ini cemerlang dalam penjanaan Python, Java, TypeScript dan C++.

### Contoh RAG menggunakan Mistral Large 2

Dalam contoh ini, kami menggunakan Mistral Large 2 untuk menjalankan corak RAG ke atas dokumen teks. Soalan ditulis dalam bahasa Korea dan bertanya tentang aktiviti pengarang sebelum kolej.

Ia menggunakan Model Embeddings Cohere untuk mencipta embeddings bagi dokumen teks serta soalan. Untuk contoh ini, ia menggunakan pakej Python faiss sebagai penyimpanan vektor.

Arahan yang dihantar kepada model Mistral termasuk kedua-dua soalan dan bahagian yang diperoleh yang serupa dengan soalan tersebut. Model kemudian memberikan jawapan dalam bahasa semula jadi.

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
Mistral Small adalah model lain dalam keluarga Mistral di bawah kategori premier/perusahaan. Seperti namanya, model ini adalah Model Bahasa Kecil (SLM). Kelebihan menggunakan Mistral Small adalah ia:
- Penjimatan Kos berbanding LLM Mistral seperti Mistral Large dan NeMo - penurunan harga sebanyak 80%
- Latensi rendah - respons lebih pantas berbanding LLM Mistral
- Fleksibel - boleh digunakan merentas persekitaran berbeza dengan kurang sekatan ke atas sumber yang diperlukan.

Mistral Small sesuai untuk:
- Tugasan berasaskan teks seperti penjumlahan, analisis sentimen dan terjemahan.
- Aplikasi dimana permintaan kerap dibuat kerana keberkesanan kosnya
- Tugasan kod latensi rendah seperti ulasan dan cadangan kod

## Membandingkan Mistral Small dan Mistral Large

Untuk menunjukkan perbezaan latensi antara Mistral Small dan Large, jalankan sel di bawah.

Anda akan melihat perbezaan masa respons antara 3-5 saat. Juga perhatikan panjang dan gaya respons pada arahan yang sama.

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

Berbanding dengan dua model lain yang dibincangkan dalam pelajaran ini, Mistral NeMo adalah satu-satunya model percuma dengan Lesen Apache2.

Ia dilihat sebagai peningkatan kepada LLM sumber terbuka terdahulu dari Mistral, Mistral 7B.

Beberapa ciri lain model NeMo adalah:

- *Tokenisasi lebih cekap:* Model ini menggunakan pengekod Tekken berbanding tiktoken yang lebih biasa digunakan. Ini membolehkan prestasi yang lebih baik merentas lebih banyak bahasa dan kod.

- *Penghalusan:* Model asas tersedia untuk penghalusan. Ini membolehkan lebih fleksibiliti untuk kes penggunaan di mana penghalusan mungkin diperlukan.

- *Pemanggilan Fungsi Asli* - Seperti Mistral Large, model ini telah dilatih untuk pemanggilan fungsi. Ini menjadikannya unik sebagai salah satu model sumber terbuka pertama yang melakukan perkara ini.

### Membandingkan Pengekod Token

Dalam contoh ini, kita akan melihat bagaimana Mistral NeMo mengendalikan tokenisasi berbanding dengan Mistral Large.

Kedua-dua contoh mengambil arahan yang sama tetapi anda akan melihat NeMo mengembalikan token yang lebih sedikit daripada Mistral Large.

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

# Muatkan pentoken Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenkan senarai mesej
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

# Muatkan pengekod Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenkan senarai mesej
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

# Hitung bilangan token
print(len(tokens))
```

## Pembelajaran tidak berhenti di sini, teruskan perjalanan

Selepas melengkapkan pelajaran ini, lihat koleksi [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif anda!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau tafsiran yang salah yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->