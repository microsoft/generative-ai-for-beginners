<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T19:02:08+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "id"
}
-->
# Membangun dengan Model Mistral

## Pendahuluan

Pelajaran ini akan membahas:  
- Menjelajahi berbagai Model Mistral  
- Memahami kasus penggunaan dan skenario untuk setiap model  
- Contoh kode yang menunjukkan fitur unik dari setiap model.

## Model Mistral

Dalam pelajaran ini, kita akan menjelajahi 3 model Mistral yang berbeda:  
**Mistral Large**, **Mistral Small**, dan **Mistral Nemo**.

Masing-masing model ini tersedia gratis di Github Model marketplace. Kode dalam notebook ini akan menggunakan model-model tersebut untuk menjalankan kode. Berikut adalah informasi lebih lanjut tentang menggunakan Github Models untuk [membuat prototipe dengan model AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)  
Mistral Large 2 saat ini adalah model unggulan dari Mistral dan dirancang untuk penggunaan perusahaan.

Model ini merupakan peningkatan dari Mistral Large asli dengan menawarkan  
- Jendela Konteks Lebih Besar - 128k vs 32k  
- Performa lebih baik pada Tugas Matematika dan Pemrograman - akurasi rata-rata 76,9% vs 60,4%  
- Peningkatan performa multibahasa - bahasa yang didukung meliputi: Inggris, Prancis, Jerman, Spanyol, Italia, Portugis, Belanda, Rusia, Cina, Jepang, Korea, Arab, dan Hindi.

Dengan fitur-fitur ini, Mistral Large unggul dalam  
- *Retrieval Augmented Generation (RAG)* - berkat jendela konteks yang lebih besar  
- *Function Calling* - model ini memiliki fungsi pemanggilan native yang memungkinkan integrasi dengan alat dan API eksternal. Pemanggilan ini bisa dilakukan secara paralel atau berurutan.  
- *Code Generation* - model ini sangat baik dalam menghasilkan kode Python, Java, TypeScript, dan C++.

### Contoh RAG menggunakan Mistral Large 2

Dalam contoh ini, kita menggunakan Mistral Large 2 untuk menjalankan pola RAG pada sebuah dokumen teks. Pertanyaannya ditulis dalam bahasa Korea dan menanyakan tentang aktivitas penulis sebelum kuliah.

Model menggunakan Cohere Embeddings untuk membuat embedding dari dokumen teks serta pertanyaan. Untuk contoh ini, digunakan paket Python faiss sebagai vector store.

Prompt yang dikirim ke model Mistral mencakup pertanyaan dan potongan teks yang diambil dan mirip dengan pertanyaan tersebut. Model kemudian memberikan jawaban dalam bahasa alami.

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
Mistral Small adalah model lain dalam keluarga Mistral yang termasuk kategori premier/enterprise. Sesuai namanya, model ini adalah Small Language Model (SLM). Keuntungan menggunakan Mistral Small adalah:  
- Hemat biaya dibandingkan dengan LLM Mistral seperti Mistral Large dan NeMo - penurunan harga hingga 80%  
- Latensi rendah - respons lebih cepat dibandingkan LLM Mistral lainnya  
- Fleksibel - dapat diterapkan di berbagai lingkungan dengan persyaratan sumber daya yang lebih sedikit.

Mistral Small sangat cocok untuk:  
- Tugas berbasis teks seperti ringkasan, analisis sentimen, dan terjemahan.  
- Aplikasi dengan permintaan yang sering karena biaya yang efisien  
- Tugas kode dengan latensi rendah seperti review dan saran kode

## Membandingkan Mistral Small dan Mistral Large

Untuk melihat perbedaan latensi antara Mistral Small dan Large, jalankan sel di bawah ini.

Anda akan melihat perbedaan waktu respons sekitar 3-5 detik. Perhatikan juga panjang dan gaya respons pada prompt yang sama.

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

Dibandingkan dengan dua model lain yang dibahas dalam pelajaran ini, Mistral NeMo adalah satu-satunya model gratis dengan lisensi Apache2.

Model ini dianggap sebagai peningkatan dari LLM open source sebelumnya dari Mistral, yaitu Mistral 7B.

Beberapa fitur lain dari model NeMo adalah:

- *Tokenisasi yang lebih efisien:* Model ini menggunakan tokenizer Tekken dibandingkan tiktoken yang lebih umum digunakan. Ini memungkinkan performa yang lebih baik untuk berbagai bahasa dan kode.

- *Finetuning:* Model dasar tersedia untuk finetuning. Ini memberikan fleksibilitas lebih untuk kasus penggunaan yang membutuhkan penyesuaian model.

- *Native Function Calling* - Seperti Mistral Large, model ini telah dilatih untuk pemanggilan fungsi. Ini menjadikannya salah satu model open source pertama yang memiliki kemampuan ini.

### Membandingkan Tokenizer

Dalam contoh ini, kita akan melihat bagaimana Mistral NeMo menangani tokenisasi dibandingkan dengan Mistral Large.

Kedua contoh menggunakan prompt yang sama, namun Anda akan melihat bahwa NeMo mengembalikan token yang lebih sedikit dibandingkan Mistral Large.

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

## Pembelajaran tidak berhenti di sini, lanjutkan Perjalanan

Setelah menyelesaikan pelajaran ini, lihat koleksi [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan Anda tentang Generative AI!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.