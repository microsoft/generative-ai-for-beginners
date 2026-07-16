# Membangun dengan Model Mistral 

## Pendahuluan 

Pelajaran ini akan membahas: 
- Menjelajahi berbagai Model Mistral 
- Memahami kasus penggunaan dan skenario untuk setiap model 
- Menjelajahi contoh kode yang menunjukkan fitur unik dari setiap model. 

## Model Mistral 

Dalam pelajaran ini, kita akan mengeksplorasi 3 model Mistral yang berbeda: 
**Mistral Large**, **Mistral Small** dan **Mistral Nemo**. 

Setiap model ini tersedia gratis di [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Kode dalam notebook ini akan menggunakan model-model tersebut untuk menjalankan kodenya.

> **Catatan:** GitHub Models akan dihentikan pada akhir Juli 2026. Berikut adalah lebih banyak detail tentang menggunakan [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) untuk membuat prototipe dengan model AI. 


## Mistral Large 2 (2407)
Mistral Large 2 saat ini adalah model unggulan dari Mistral dan dirancang untuk penggunaan perusahaan. 

Model ini merupakan peningkatan dari Mistral Large asli dengan menawarkan 
- Jendela Konteks yang Lebih Besar - 128k vs 32k 
- Kinerja lebih baik pada Tugas Matematika dan Pengkodean - akurasi rata-rata 76,9% vs 60,4% 
- Peningkatan kinerja multibahasa - bahasa yang didukung meliputi: Inggris, Prancis, Jerman, Spanyol, Italia, Portugis, Belanda, Rusia, Cina, Jepang, Korea, Arab, dan Hindi.

Dengan fitur-fitur ini, Mistral Large unggul dalam 
- *Retrieval Augmented Generation (RAG)* - karena jendela konteks yang lebih besar
- *Pemanggilan Fungsi* - model ini memiliki pemanggilan fungsi bawaan yang memungkinkan integrasi dengan alat eksternal dan API. Pemanggilan ini dapat dilakukan secara paralel atau satu per satu secara berurutan.
- *Generasi Kode* - model ini unggul dalam generasi Python, Java, TypeScript, dan C++. 

### Contoh RAG menggunakan Mistral Large 2 

Dalam contoh ini, kami menggunakan Mistral Large 2 untuk menjalankan pola RAG pada dokumen teks. Pertanyaan ditulis dalam bahasa Korea dan menanyakan tentang kegiatan penulis sebelum kuliah. 

Ini menggunakan Model Embeddings Cohere untuk membuat embeddings dari dokumen teks serta pertanyaannya. Untuk contoh ini, digunakan paket Python faiss sebagai penyimpanan vektor. 

Prompt yang dikirim ke model Mistral mencakup pertanyaan dan potongan teks yang diambil yang mirip dengan pertanyaannya. Model kemudian memberikan respons dalam bahasa alami. 

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

# Dapatkan ini dari halaman "Overview" proyek Microsoft Foundry Anda
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
Mistral Small adalah model lain dalam keluarga model Mistral di bawah kategori premier/enterprise. Sesuai namanya, model ini adalah Small Language Model (SLM). Keuntungan menggunakan Mistral Small adalah: 
- Penghematan biaya dibandingkan dengan LLM Mistral seperti Mistral Large dan NeMo - penurunan harga 80%
- Latensi rendah - respons lebih cepat dibandingkan dengan LLM Mistral
- Fleksibel - dapat diterapkan di berbagai lingkungan dengan batasan sumber daya yang lebih sedikit. 


Mistral Small sangat cocok untuk: 
- Tugas berbasis teks seperti ringkasan, analisis sentimen, dan terjemahan. 
- Aplikasi dengan permintaan sering karena efektivitas biayanya 
- Tugas kode latensi rendah seperti review dan saran kode 

## Membandingkan Mistral Small dan Mistral Large 

Untuk menunjukkan perbedaan latensi antara Mistral Small dan Large, jalankan sel di bawah ini. 

Anda akan melihat perbedaan waktu respons antara 3-5 detik. Perhatikan juga panjang dan gaya respons untuk prompt yang sama.  

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

Dibandingkan dengan dua model lain yang dibahas dalam pelajaran ini, Mistral NeMo adalah satu-satunya model gratis dengan Lisensi Apache2. 

Model ini dipandang sebagai peningkatan dari LLM open source sebelumnya dari Mistral, Mistral 7B. 

Beberapa fitur lain dari model NeMo adalah: 

- *Tokenisasi yang lebih efisien:* Model ini menggunakan tokenizer Tekken dibandingkan dengan tiktoken yang lebih umum digunakan. Ini memungkinkan kinerja lebih baik pada lebih banyak bahasa dan kode. 

- *Finetuning:* Model dasar tersedia untuk finetuning. Ini memberikan fleksibilitas lebih untuk kasus penggunaan yang membutuhkan finetuning. 

- *Pemanggilan Fungsi Bawaan* - Seperti Mistral Large, model ini telah dilatih pada pemanggilan fungsi. Ini membuatnya unik sebagai salah satu model open source pertama yang memiliki fitur ini. 


### Membandingkan Tokenizer 

Dalam contoh ini, kita akan melihat bagaimana Mistral NeMo menangani tokenisasi dibandingkan dengan Mistral Large. 

Kedua contoh menggunakan prompt yang sama, tapi Anda harus melihat bahwa NeMo mengembalikan lebih sedikit token dibandingkan Mistral Large. 

```bash
pip install mistral-common
```

```python 
# Impor paket yang dibutuhkan:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Muat tokenizer Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenisasi daftar pesan
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

# Hitung jumlah token
print(len(tokens))
```

```python
# Impor paket yang dibutuhkan:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Muat tokenizer Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenisasi daftar pesan
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

# Hitung jumlah token
print(len(tokens))
```

## Pembelajaran tidak berhenti di sini, lanjutkan perjalanan 

Setelah menyelesaikan pelajaran ini, lihat koleksi [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif Anda!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->