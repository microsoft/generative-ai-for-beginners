<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:19:58+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "id"
}
-->
# Membangun dengan Model Mistral

## Pendahuluan

Pelajaran ini akan membahas:
- Mengeksplorasi berbagai Model Mistral
- Memahami kasus penggunaan dan skenario untuk setiap model
- Contoh kode menunjukkan fitur unik dari setiap model.

## Model Mistral

Dalam pelajaran ini, kita akan mengeksplorasi 3 model Mistral yang berbeda: **Mistral Large**, **Mistral Small**, dan **Mistral Nemo**.

Setiap model ini tersedia gratis di pasar Model Github. Kode dalam notebook ini akan menggunakan model-model ini untuk menjalankan kode. Berikut adalah lebih banyak detail tentang menggunakan Model Github untuk [membuat prototipe dengan model AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 saat ini adalah model unggulan dari Mistral dan dirancang untuk penggunaan perusahaan.

Model ini merupakan peningkatan dari Mistral Large asli dengan menawarkan
- Jendela Konteks yang Lebih Besar - 128k vs 32k
- Kinerja lebih baik pada Tugas Matematika dan Pemrograman - rata-rata akurasi 76,9% vs 60,4%
- Peningkatan kinerja multibahasa - bahasa termasuk: Inggris, Prancis, Jerman, Spanyol, Italia, Portugis, Belanda, Rusia, Cina, Jepang, Korea, Arab, dan Hindi.

Dengan fitur-fitur ini, Mistral Large unggul dalam
- *Retrieval Augmented Generation (RAG)* - karena jendela konteks yang lebih besar
- *Panggilan Fungsi* - model ini memiliki panggilan fungsi bawaan yang memungkinkan integrasi dengan alat dan API eksternal. Panggilan ini dapat dilakukan baik secara paralel atau satu demi satu secara berurutan.
- *Pembuatan Kode* - model ini unggul dalam pembuatan Python, Java, TypeScript, dan C++.

### Contoh RAG menggunakan Mistral Large 2

Dalam contoh ini, kita menggunakan Mistral Large 2 untuk menjalankan pola RAG pada dokumen teks. Pertanyaannya ditulis dalam bahasa Korea dan menanyakan tentang aktivitas penulis sebelum kuliah.

Ini menggunakan Model Embeddings Cohere untuk membuat embeddings dari dokumen teks serta pertanyaan. Untuk contoh ini, digunakan paket Python faiss sebagai penyimpanan vektor.

Prompt yang dikirim ke model Mistral mencakup pertanyaan dan potongan yang diambil yang mirip dengan pertanyaan. Model kemudian memberikan respons dalam bahasa alami.

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
Mistral Small adalah model lain dalam keluarga model Mistral di bawah kategori premier/perusahaan. Seperti namanya, model ini adalah Small Language Model (SLM). Keuntungan menggunakan Mistral Small adalah:
- Penghematan biaya dibandingkan dengan LLM Mistral seperti Mistral Large dan NeMo - penurunan harga 80%
- Latensi rendah - respons lebih cepat dibandingkan dengan LLM Mistral
- Fleksibel - dapat diterapkan di berbagai lingkungan dengan lebih sedikit batasan pada sumber daya yang dibutuhkan.

Mistral Small sangat baik untuk:
- Tugas berbasis teks seperti ringkasan, analisis sentimen, dan terjemahan.
- Aplikasi di mana permintaan sering dilakukan karena efektivitas biayanya
- Tugas kode dengan latensi rendah seperti ulasan dan saran kode

## Membandingkan Mistral Small dan Mistral Large

Untuk menunjukkan perbedaan dalam latensi antara Mistral Small dan Large, jalankan sel di bawah ini.

Anda harus melihat perbedaan dalam waktu respons antara 3-5 detik. Juga perhatikan panjang dan gaya respons atas prompt yang sama.

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

Dibandingkan dengan dua model lain yang dibahas dalam pelajaran ini, Mistral NeMo adalah satu-satunya model gratis dengan Lisensi Apache2.

Ini dianggap sebagai peningkatan dari LLM open source sebelumnya dari Mistral, Mistral 7B.

Beberapa fitur lain dari model NeMo adalah:

- *Tokenisasi lebih efisien:* Model ini menggunakan tokenizer Tekken dibandingkan dengan tiktoken yang lebih umum digunakan. Ini memungkinkan kinerja yang lebih baik pada lebih banyak bahasa dan kode.

- *Penyetelan Halus:* Model dasar tersedia untuk penyetelan halus. Ini memungkinkan lebih banyak fleksibilitas untuk kasus penggunaan di mana penyetelan halus mungkin diperlukan.

- *Panggilan Fungsi Bawaan* - Seperti Mistral Large, model ini telah dilatih pada panggilan fungsi. Ini membuatnya unik sebagai salah satu model open source pertama yang melakukannya.

### Membandingkan Tokenizer

Dalam contoh ini, kita akan melihat bagaimana Mistral NeMo menangani tokenisasi dibandingkan dengan Mistral Large.

Kedua contoh mengambil prompt yang sama tetapi Anda harus melihat bahwa NeMo mengembalikan lebih sedikit token dibandingkan dengan Mistral Large.

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

## Belajar tidak berhenti di sini, lanjutkan Perjalanan

Setelah menyelesaikan pelajaran ini, lihat [koleksi Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif Anda!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk mencapai akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi penting, disarankan menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.