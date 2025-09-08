<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:11:50+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "id"
}
-->
# Membangun Dengan Model Keluarga Meta

## Pendahuluan

Pelajaran ini akan membahas:

- Menjelajahi dua model utama keluarga Meta - Llama 3.1 dan Llama 3.2  
- Memahami kasus penggunaan dan skenario untuk masing-masing model  
- Contoh kode untuk menunjukkan fitur unik dari setiap model  

## Keluarga Model Meta

Dalam pelajaran ini, kita akan mengeksplorasi 2 model dari keluarga Meta atau "Llama Herd" - Llama 3.1 dan Llama 3.2

Model-model ini hadir dalam berbagai varian dan tersedia di GitHub Model marketplace. Berikut adalah detail lebih lanjut tentang penggunaan GitHub Models untuk [membuat prototipe dengan model AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Varian Model:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*Catatan: Llama 3 juga tersedia di GitHub Models tapi tidak akan dibahas dalam pelajaran ini*

## Llama 3.1

Dengan 405 Miliar Parameter, Llama 3.1 termasuk dalam kategori LLM open source.

Model ini merupakan peningkatan dari rilis sebelumnya Llama 3 dengan menawarkan:

- Jendela konteks yang lebih besar - 128k token dibandingkan 8k token  
- Maksimum Token Output yang lebih besar - 4096 dibandingkan 2048  
- Dukungan Multibahasa yang lebih baik - berkat peningkatan jumlah token pelatihan  

Hal ini memungkinkan Llama 3.1 untuk menangani kasus penggunaan yang lebih kompleks saat membangun aplikasi GenAI, termasuk:  
- Native Function Calling - kemampuan memanggil alat dan fungsi eksternal di luar alur kerja LLM  
- Performa RAG yang lebih baik - berkat jendela konteks yang lebih besar  
- Pembuatan Data Sintetis - kemampuan membuat data efektif untuk tugas seperti fine-tuning  

### Native Function Calling

Llama 3.1 telah disesuaikan agar lebih efektif dalam melakukan pemanggilan fungsi atau alat. Model ini juga memiliki dua alat bawaan yang dapat dikenali untuk digunakan berdasarkan prompt dari pengguna. Alat-alat tersebut adalah:

- **Brave Search** - Dapat digunakan untuk mendapatkan informasi terkini seperti cuaca dengan melakukan pencarian web  
- **Wolfram Alpha** - Dapat digunakan untuk perhitungan matematika yang lebih kompleks sehingga tidak perlu menulis fungsi sendiri  

Anda juga dapat membuat alat kustom sendiri yang dapat dipanggil oleh LLM.

Dalam contoh kode di bawah ini:

- Kita mendefinisikan alat yang tersedia (brave_search, wolfram_alpha) dalam prompt sistem.  
- Mengirim prompt pengguna yang menanyakan tentang cuaca di suatu kota.  
- LLM akan merespons dengan pemanggilan alat ke Brave Search yang akan terlihat seperti ini `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*Catatan: Contoh ini hanya melakukan pemanggilan alat, jika Anda ingin mendapatkan hasilnya, Anda perlu membuat akun gratis di halaman Brave API dan mendefinisikan fungsi tersebut sendiri*

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

Meskipun merupakan LLM, salah satu keterbatasan Llama 3.1 adalah multimodalitas. Artinya, kemampuan menggunakan berbagai jenis input seperti gambar sebagai prompt dan memberikan respons. Kemampuan ini adalah salah satu fitur utama dari Llama 3.2. Fitur-fitur lainnya meliputi:

- Multimodalitas - mampu mengevaluasi prompt teks dan gambar  
- Varian ukuran kecil hingga menengah (11B dan 90B) - memberikan opsi penyebaran yang fleksibel  
- Varian hanya teks (1B dan 3B) - memungkinkan model dijalankan di perangkat edge / mobile dengan latensi rendah  

Dukungan multimodal ini merupakan langkah besar dalam dunia model open source. Contoh kode di bawah ini menggunakan prompt gambar dan teks untuk mendapatkan analisis gambar dari Llama 3.2 90B.

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

Setelah menyelesaikan pelajaran ini, lihat koleksi [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan Anda tentang Generative AI!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.