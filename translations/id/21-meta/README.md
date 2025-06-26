<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:33:39+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "id"
}
-->
# Membangun dengan Model Keluarga Meta

## Pengantar

Pelajaran ini akan membahas:

- Menjelajahi dua model utama keluarga Meta - Llama 3.1 dan Llama 3.2
- Memahami penggunaan dan skenario untuk setiap model
- Contoh kode untuk menunjukkan fitur unik dari setiap model

## Keluarga Model Meta

Dalam pelajaran ini, kita akan menjelajahi 2 model dari keluarga Meta atau "Kawanan Llama" - Llama 3.1 dan Llama 3.2

Model-model ini tersedia dalam berbagai varian dan tersedia di pasar Model GitHub. Berikut adalah detail lebih lanjut tentang menggunakan Model GitHub untuk [membuat prototipe dengan model AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Varian Model:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Catatan: Llama 3 juga tersedia di Model GitHub tetapi tidak akan dibahas dalam pelajaran ini*

## Llama 3.1

Dengan 405 Miliar Parameter, Llama 3.1 termasuk dalam kategori LLM sumber terbuka.

Mode ini adalah peningkatan dari rilis sebelumnya Llama 3 dengan menawarkan:

- Jendela konteks lebih besar - 128k token vs 8k token
- Maksimum Output Token lebih besar - 4096 vs 2048
- Dukungan Multibahasa Lebih Baik - karena peningkatan dalam token pelatihan

Ini memungkinkan Llama 3.1 untuk menangani kasus penggunaan yang lebih kompleks saat membangun aplikasi GenAI termasuk:
- Pemanggilan Fungsi Asli - kemampuan untuk memanggil alat dan fungsi eksternal di luar alur kerja LLM
- Performa RAG Lebih Baik - karena jendela konteks yang lebih tinggi
- Pembuatan Data Sintetis - kemampuan untuk membuat data efektif untuk tugas seperti penyetelan halus

### Pemanggilan Fungsi Asli

Llama 3.1 telah disetel untuk lebih efektif dalam melakukan panggilan fungsi atau alat. Ia juga memiliki dua alat bawaan yang dapat diidentifikasi oleh model sebagai perlu digunakan berdasarkan prompt dari pengguna. Alat-alat ini adalah:

- **Brave Search** - Dapat digunakan untuk mendapatkan informasi terbaru seperti cuaca dengan melakukan pencarian web
- **Wolfram Alpha** - Dapat digunakan untuk perhitungan matematis yang lebih kompleks sehingga Anda tidak perlu menulis fungsi Anda sendiri.

Anda juga dapat membuat alat kustom Anda sendiri yang dapat dipanggil oleh LLM.

Dalam contoh kode di bawah ini:

- Kami mendefinisikan alat yang tersedia (brave_search, wolfram_alpha) dalam prompt sistem.
- Mengirimkan prompt pengguna yang menanyakan tentang cuaca di kota tertentu.
- LLM akan merespons dengan panggilan alat ke alat Brave Search yang akan terlihat seperti ini `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Catatan: Contoh ini hanya membuat panggilan alat, jika Anda ingin mendapatkan hasilnya, Anda perlu membuat akun gratis di halaman API Brave dan mendefinisikan fungsi itu sendiri`

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

Meskipun menjadi LLM, satu keterbatasan yang dimiliki Llama 3.1 adalah multimodalitas. Artinya, mampu menggunakan berbagai jenis input seperti gambar sebagai prompt dan memberikan respons. Kemampuan ini adalah salah satu fitur utama dari Llama 3.2. Fitur-fitur ini juga termasuk:

- Multimodalitas - memiliki kemampuan untuk mengevaluasi baik teks maupun gambar sebagai prompt
- Variasi ukuran kecil hingga menengah (11B dan 90B) - ini memberikan opsi penerapan yang fleksibel,
- Variasi teks saja (1B dan 3B) - ini memungkinkan model untuk diterapkan pada perangkat edge / mobile dan memberikan latensi rendah

Dukungan multimodal ini mewakili langkah besar dalam dunia model sumber terbuka. Contoh kode di bawah ini mengambil baik gambar maupun teks sebagai prompt untuk mendapatkan analisis gambar dari Llama 3.2 90B.

### Dukungan Multimodal dengan Llama 3.2

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

## Pembelajaran tidak berhenti di sini, lanjutkan Perjalanan

Setelah menyelesaikan pelajaran ini, lihat [Koleksi Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif Anda!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber otoritatif. Untuk informasi penting, disarankan menggunakan penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang salah yang timbul dari penggunaan terjemahan ini.