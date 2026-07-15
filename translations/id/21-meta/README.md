# Membangun Dengan Model Keluarga Meta 

## Pendahuluan 

Pelajaran ini akan membahas: 

- Menjelajahi dua model keluarga Meta utama - Llama 3.1 dan Llama 3.2 
- Memahami kasus penggunaan dan skenario untuk masing-masing model 
- Contoh kode untuk menunjukkan fitur unik dari masing-masing model 


## Keluarga Model Meta 

Dalam pelajaran ini, kita akan menjelajahi 2 model dari keluarga Meta atau "Llama Herd" - Llama 3.1 dan Llama 3.2.

Model-model ini hadir dalam berbagai varian dan tersedia di [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Catatan:** GitHub Models akan dihentikan pada akhir Juli 2026. Berikut adalah detail lebih lanjut tentang menggunakan [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) untuk membuat prototipe dengan model AI.

Varian Model: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Catatan: Llama 3 juga tersedia di Microsoft Foundry Models tetapi tidak akan dibahas dalam pelajaran ini*

## Llama 3.1 

Dengan 405 Miliar Parameter, Llama 3.1 masuk dalam kategori LLM sumber terbuka. 

Model ini merupakan peningkatan dari rilis awal Llama 3 dengan menawarkan: 

- Jendela konteks yang lebih besar - 128k token dibandingkan 8k token 
- Maksimum Token Output lebih besar - 4096 dibandingkan 2048 
- Dukungan Multibahasa lebih baik - karena peningkatan token pelatihan 

Ini memungkinkan Llama 3.1 untuk menangani kasus penggunaan yang lebih kompleks saat membangun aplikasi GenAI termasuk: 
- Pemanggilan Fungsi Native - kemampuan memanggil alat dan fungsi eksternal di luar alur kerja LLM
- Kinerja RAG lebih baik - karena jendela konteks yang lebih besar 
- Pembuatan Data Sintetis - kemampuan membuat data efektif untuk tugas seperti fine-tuning 

### Pemanggilan Fungsi Native 

Llama 3.1 telah di-fine-tune agar lebih efektif dalam membuat panggilan fungsi atau alat. Model ini juga memiliki dua alat bawaan yang dapat dikenali oleh model untuk digunakan berdasarkan prompt dari pengguna. Alat-alat ini adalah: 

- **Brave Search** - Dapat digunakan untuk mendapatkan informasi terkini seperti cuaca dengan melakukan pencarian web 
- **Wolfram Alpha** - Dapat digunakan untuk perhitungan matematika yang lebih kompleks sehingga tidak perlu menulis fungsi sendiri. 

Anda juga dapat membuat alat khusus Anda sendiri yang dapat dipanggil oleh LLM. 

Dalam contoh kode di bawah ini: 

- Kita mendefinisikan alat yang tersedia (brave_search, wolfram_alpha) dalam prompt sistem. 
- Mengirim prompt pengguna yang menanyakan tentang cuaca di sebuah kota tertentu. 
- LLM akan merespon dengan panggilan alat ke Brave Search yang akan terlihat seperti `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Catatan: Contoh ini hanya membuat panggilan alat, jika Anda ingin mendapatkan hasilnya, Anda perlu membuat akun gratis di halaman Brave API dan mendefinisikan fungsi itu sendiri.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Dapatkan ini dari halaman "Ikhtisar" proyek Microsoft Foundry Anda
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Meta-Llama-3.1-405B-Instruct"

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

Meskipun merupakan LLM, salah satu keterbatasan Llama 3.1 adalah kurangnya multimodalitas. Artinya, ketidakmampuan menggunakan berbagai jenis input seperti gambar sebagai prompt dan memberikan respon. Kemampuan ini merupakan salah satu fitur utama Llama 3.2. Fitur-fitur ini juga meliputi: 

- Multimodalitas - memiliki kemampuan mengevaluasi prompt teks dan gambar 
- Varian ukuran kecil sampai sedang (11B dan 90B) - menyediakan opsi deployment yang fleksibel, 
- Varian hanya teks (1B dan 3B) - memungkinkan model dideploy pada perangkat edge / mobile dan memberikan latensi rendah 

Dukungan multimodal merupakan langkah besar di dunia model open source. Contoh kode di bawah ini mengambil prompt gambar dan teks untuk mendapat analisis gambar dari Llama 3.2 90B. 


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

# Dapatkan ini dari halaman "Ikhtisar" proyek Microsoft Foundry Anda
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
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

Setelah menyelesaikan pelajaran ini, lihat koleksi pembelajaran [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk terus meningkatkan pengetahuan Generative AI Anda!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->