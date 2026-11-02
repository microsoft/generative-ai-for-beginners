# Membangun Dengan Model Keluarga Meta 

## Pendahuluan 

Pelajaran ini akan membahas: 

- Menjelajahi dua model utama keluarga Meta - Llama 3.1 dan Llama 3.2, serta alternatif yang saat ini tersedia yang digunakan dalam contoh kode (Llama 3.3 dan Llama 4) 
- Memahami kasus penggunaan dan skenario untuk setiap model 
- Contoh kode untuk menunjukkan fitur unik dari setiap model 


## Keluarga Model Meta 

Dalam pelajaran ini, kita akan menjelajahi 2 model dari keluarga Meta atau "Llama Herd" - Llama 3.1 dan Llama 3.2. Contoh kode yang dapat dijalankan menggunakan Llama 3.3 dan Llama 4, yang saat ini merupakan alternatif yang tersedia dalam katalog Microsoft Foundry Models.

Model-model ini hadir dalam berbagai varian dan tersedia dalam [katalog Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Catatan:** GitHub Models akan dihentikan pada akhir Juli 2026. Berikut adalah rincian lebih lanjut tentang menggunakan [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) untuk prototipe dengan model AI.

> **Catatan:** Versi model spesifik yang awalnya digunakan untuk pelajaran ini (Llama 3.1 70B/405B Instruct, Llama 3.2 11B/90B Vision Instruct) telah dihentikan dari katalog Microsoft Foundry Models. Contoh kode di bawah menggunakan `Llama-3.3-70B-Instruct` dan `Llama-4-Scout-17B-16E-Instruct` sebagai alternatif yang saat ini tersedia dalam katalog Microsoft Foundry Models, sehingga masih dapat dijalankan hari ini.

Varian Model (seperti yang awalnya dibahas dalam pelajaran ini): 
- Llama 3.1 - 70B Instruct (dihentikan) 
- Llama 3.1 - 405B Instruct (dihentikan) 
- Llama 3.2 - 11B Vision Instruct (dihentikan) 
- Llama 3.2 - 90B Vision Instruct (dihentikan) 

Alternatif yang saat ini tersedia yang digunakan dalam contoh kode: 
- Llama 3.3 - 70B Instruct (`Llama-3.3-70B-Instruct`) 
- Llama 4 Scout - 17B 16E Instruct (`Llama-4-Scout-17B-16E-Instruct`) 

*Catatan: Varian Llama 3 yang dibahas di atas dipertahankan untuk konteks historis dan tidak lagi tersedia dalam Microsoft Foundry Models.*

## Llama 3.1 

Dengan 405 Miliar Parameter, Llama 3.1 termasuk dalam kategori LLM sumber terbuka. 

Model ini adalah peningkatan dari rilis sebelumnya Llama 3 dengan menawarkan: 

- Jendela konteks lebih besar - 128k token vs 8k token 
- Maksimum Token Output lebih besar - 4096 vs 2048 
- Dukungan Multibahasa lebih baik - karena peningkatan token pelatihan 

Ini memungkinkan Llama 3.1 untuk menangani kasus penggunaan yang lebih kompleks saat membangun aplikasi GenAI termasuk: 
- Pemanggilan Fungsi Native - kemampuan untuk memanggil alat dan fungsi eksternal di luar alur kerja LLM
- Kinerja RAG lebih baik - karena jendela konteks yang lebih besar 
- Generasi Data Sintetis - kemampuan untuk membuat data efektif untuk tugas seperti penyempurnaan 

### Pemanggilan Fungsi Native 

Llama 3.1 telah disesuaikan agar lebih efektif dalam membuat panggilan fungsi atau alat. Model ini juga memiliki dua alat bawaan yang dapat dikenali model sebagai yang perlu digunakan berdasarkan prompt dari pengguna. Alat-alat ini adalah: 

- **Brave Search** - Dapat digunakan untuk mendapatkan informasi terbaru seperti cuaca dengan melakukan pencarian web 
- **Wolfram Alpha** - Dapat digunakan untuk perhitungan matematika yang lebih kompleks sehingga tidak perlu menulis fungsi sendiri. 

Anda juga dapat membuat alat khusus sendiri yang dapat dipanggil oleh LLM. 

Dalam contoh kode di bawah ini: 

- Kami mendefinisikan alat yang tersedia (brave_search, wolfram_alpha) dalam prompt sistem. 
- Mengirim prompt pengguna yang menanyakan tentang cuaca di suatu kota. 
- LLM akan merespons dengan panggilan alat ke alat Brave Search yang akan terlihat seperti ini `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Catatan: Contoh ini hanya membuat panggilan alat, jika Anda ingin mendapatkan hasilnya, Anda perlu membuat akun gratis di halaman Brave API dan mendefinisikan fungsinya sendiri.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Meta-Llama-3.1-405B-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-3.3-70B-Instruct, a currently available alternative, instead
model_name = "Llama-3.3-70B-Instruct"

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

Meskipun merupakan LLM, salah satu keterbatasan Llama 3.1 adalah kurangnya multimodalitas. Yaitu, ketidakmampuan menggunakan jenis input yang berbeda seperti gambar sebagai prompt dan memberikan respons. Kemampuan ini adalah salah satu fitur utama dari Llama 3.2. Fitur-fitur ini juga meliputi: 

- Multimodalitas - memiliki kemampuan untuk mengevaluasi prompt teks dan gambar 
- Variasi ukuran kecil hingga sedang (11B dan 90B) - ini memberikan opsi deploy yang fleksibel, 
- Variasi hanya teks (1B dan 3B) - ini memungkinkan model di-deploy di perangkat edge / mobile dan menyediakan latensi rendah 

Dukungan multimodal mewakili langkah besar di dunia model sumber terbuka. Contoh kode di bawah ini menerima prompt gambar dan teks untuk mendapatkan analisis gambar. Karena Llama 3.2 90B Vision Instruct telah dihentikan, contoh tersebut menggunakan `Llama-4-Scout-17B-16E-Instruct`, alternatif multimodal bawaan yang saat ini tersedia. 


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

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Llama-3.2-90B-Vision-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-4-Scout-17B-16E-Instruct, a currently available natively multimodal alternative, instead
model_name = "Llama-4-Scout-17B-16E-Instruct"

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

Setelah menyelesaikan pelajaran ini, lihat [koleksi Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif Anda!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->