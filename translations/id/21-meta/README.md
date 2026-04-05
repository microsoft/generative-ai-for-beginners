# Membangun Dengan Model Keluarga Meta

## Pendahuluan

Pelajaran ini akan membahas:

- Menjelajahi dua model utama keluarga Meta - Llama 3.1 dan Llama 3.2
- Memahami kasus penggunaan dan skenario untuk setiap model
- Contoh kode untuk menunjukkan fitur unik dari setiap model

## Keluarga Model Meta

Dalam pelajaran ini, kita akan menjelajahi 2 model dari keluarga Meta atau "Llama Herd" - Llama 3.1 dan Llama 3.2.

Model-model ini tersedia dalam berbagai varian dan tersedia di GitHub Model marketplace. Berikut adalah rincian lebih lanjut tentang penggunaan GitHub Models untuk [membuat prototipe dengan model AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Varian Model:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Catatan: Llama 3 juga tersedia di GitHub Models tetapi tidak akan dibahas dalam pelajaran ini*

## Llama 3.1

Dengan 405 Miliar Parameter, Llama 3.1 termasuk dalam kategori LLM sumber terbuka.

Model ini merupakan peningkatan dari rilis sebelumnya Llama 3 dengan menawarkan:

- Jendela konteks lebih besar - 128k token vs 8k token
- Maksimum Token Output lebih besar - 4096 vs 2048
- Dukungan Multibahasa yang lebih baik - karena peningkatan token pelatihan

Hal ini memungkinkan Llama 3.1 menangani kasus penggunaan yang lebih kompleks saat membangun aplikasi GenAI termasuk:
- Panggilan Fungsi Native - kemampuan untuk memanggil alat eksternal dan fungsi di luar alur kerja LLM
- Kinerja RAG yang Lebih Baik - karena jendela konteks yang lebih besar
- Generasi Data Sintetik - kemampuan untuk membuat data yang efektif untuk tugas seperti fine-tuning

### Panggilan Fungsi Native

Llama 3.1 telah disesuaikan agar lebih efektif dalam melakukan panggilan fungsi atau alat. Model ini juga memiliki dua alat bawaan yang dapat diidentifikasi oleh model sebagai yang perlu digunakan berdasarkan prompt dari pengguna. Alat-alat tersebut adalah:

- **Brave Search** - Dapat digunakan untuk mendapatkan informasi terkini seperti cuaca dengan melakukan pencarian web
- **Wolfram Alpha** - Dapat digunakan untuk perhitungan matematika yang lebih kompleks sehingga Anda tidak perlu menulis fungsi sendiri.

Anda juga dapat membuat alat khusus Anda sendiri yang dapat dipanggil oleh LLM.

Dalam contoh kode di bawah ini:

- Kami mendefinisikan alat yang tersedia (brave_search, wolfram_alpha) dalam prompt sistem.
- Mengirim prompt pengguna yang menanyakan tentang cuaca di sebuah kota tertentu.
- LLM akan merespons dengan panggilan alat ke Brave Search yang akan terlihat seperti ini `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Catatan: Contoh ini hanya melakukan panggilan alat, jika Anda ingin mendapatkan hasilnya, Anda perlu membuat akun gratis di halaman Brave API dan mendefinisikan fungsi itu sendiri.

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

Meski merupakan LLM, salah satu keterbatasan Llama 3.1 adalah kurangnya multimodalitas. Artinya, ketidakmampuan menggunakan berbagai jenis input seperti gambar sebagai prompt dan memberikan respons. Kemampuan ini adalah salah satu fitur utama dari Llama 3.2. Fitur-fitur tersebut juga meliputi:

- Multimodalitas - memiliki kemampuan untuk mengevaluasi prompt teks dan gambar
- Varian berukuran kecil sampai sedang (11B dan 90B) - memberikan opsi penerapan yang fleksibel,
- Varian hanya teks (1B dan 3B) - memungkinkan model diterapkan di perangkat edge / mobile dan memberikan latensi rendah

Dukungan multimodal ini merupakan langkah besar di dunia model sumber terbuka. Contoh kode di bawah ini mengambil input gambar dan teks untuk mendapatkan analisis gambar dari Llama 3.2 90B.

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


## Pembelajaran tidak berhenti di sini, lanjutkan perjalanan

Setelah menyelesaikan pelajaran ini, lihat koleksi [Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif Anda!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber otoritatif. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang salah yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->