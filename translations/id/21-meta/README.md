# Membangun Dengan Model Keluarga Meta

## Pengenalan

Pelajaran ini akan membahas:

- Menjelajahi dua model utama keluarga Meta - Llama 3.1 dan Llama 3.2, serta alternatif yang saat ini tersedia yang digunakan dalam contoh kode (Llama 3.3 dan Llama 4)
- Memahami kasus penggunaan dan skenario untuk setiap model
- Contoh kode untuk menunjukkan fitur unik dari setiap model


## Keluarga Model Meta

Dalam pelajaran ini, kita akan mengeksplorasi 2 model dari keluarga Meta atau "Llama Herd" - Llama 3.1 dan Llama 3.2. Contoh kode yang dapat dijalankan menggunakan Llama 3.3 dan Llama 4, yang saat ini merupakan alternatif yang tersedia dalam katalog Model Microsoft Foundry.

Model-model ini tersedia dalam berbagai varian dan tersedia di [katalog Model Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Catatan:** Model GitHub akan dihentikan pada akhir Juli 2026. Berikut adalah lebih banyak detail tentang menggunakan [Model Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) untuk membuat prototipe dengan model AI.

> **Catatan:** Versi model spesifik yang digunakan saat pelajaran ini ditulis (Llama 3.1 70B/405B Instruct, Llama 3.2 11B/90B Vision Instruct) telah dihentikan dari katalog Model Microsoft Foundry. Contoh kode di bawah ini menggunakan `Llama-3.3-70B-Instruct` dan `Llama-4-Scout-17B-16E-Instruct` sebagai alternatif yang saat ini tersedia dalam katalog Model Microsoft Foundry, sehingga masih dapat dijalankan hari ini.

Varian Model (sesuai dengan yang dibahas dalam pelajaran ini):
- Llama 3.1 - 70B Instruct (dihentikan)
- Llama 3.1 - 405B Instruct (dihentikan)
- Llama 3.2 - 11B Vision Instruct (dihentikan)
- Llama 3.2 - 90B Vision Instruct (dihentikan)

Alternatif yang saat ini tersedia yang digunakan dalam contoh kode:
- Llama 3.3 - 70B Instruct (`Llama-3.3-70B-Instruct`)
- Llama 4 Scout - 17B 16E Instruct (`Llama-4-Scout-17B-16E-Instruct`)

*Catatan: Varian Llama 3 yang dibahas di atas disimpan untuk konteks sejarah dan tidak lagi tersedia di Model Microsoft Foundry.*

## Llama 3.1

Dengan 405 Miliar Parameter, Llama 3.1 masuk dalam kategori LLM sumber terbuka.

Model ini merupakan peningkatan dari rilis sebelumnya Llama 3 dengan menawarkan:

- Jendela konteks yang lebih besar - 128k token vs 8k token
- Maksimal Token Output yang lebih besar - 4096 vs 2048
- Dukungan Multibahasa yang lebih baik - karena peningkatan token pelatihan

Ini memungkinkan Llama 3.1 menangani kasus penggunaan yang lebih kompleks saat membangun aplikasi GenAI termasuk:
- Pemanggilan Fungsi Asli - kemampuan untuk memanggil alat dan fungsi eksternal di luar alur kerja LLM
- Performa RAG yang Lebih Baik - karena jendela konteks yang lebih besar
- Pembuatan Data Sintetis - kemampuan untuk membuat data efektif untuk tugas seperti penyetelan lanjutan

### Pemanggilan Fungsi Asli

Llama 3.1 telah disetel dengan baik agar lebih efektif dalam melakukan pemanggilan fungsi atau alat. Model ini juga memiliki dua alat bawaan yang dapat dikenali model sebagai kebutuhan untuk digunakan berdasarkan prompt dari pengguna. Alat-alat ini adalah:

- **Brave Search** - Dapat digunakan untuk mendapatkan informasi terkini seperti cuaca dengan melakukan pencarian web
- **Wolfram Alpha** - Dapat digunakan untuk perhitungan matematis yang lebih kompleks sehingga penulisan fungsi sendiri tidak diperlukan.

Anda juga dapat membuat alat kustom sendiri yang dapat dipanggil oleh LLM.

Dalam contoh kode di bawah ini:

- Kami mendefinisikan alat yang tersedia (brave_search, wolfram_alpha) dalam prompt sistem.
- Mengirim prompt pengguna yang menanyakan tentang cuaca di kota tertentu.
- LLM akan merespon dengan pemanggilan alat ke alat Brave Search yang akan terlihat seperti ini `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Catatan: Contoh ini hanya melakukan pemanggilan alat, jika Anda ingin mendapatkan hasilnya, Anda perlu membuat akun gratis di halaman API Brave dan mendefinisikan fungsi itu sendiri.

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

Meskipun merupakan LLM, salah satu keterbatasan Llama 3.1 adalah kurangnya multimodalitas. Artinya, ketidakmampuan menggunakan jenis input yang berbeda seperti gambar sebagai prompt dan memberikan respons. Kemampuan ini merupakan salah satu fitur utama dari Llama 3.2. Fitur-fitur ini juga termasuk:

- Multimodalitas - memiliki kemampuan untuk mengevaluasi prompt teks dan gambar
- Variasi ukuran kecil hingga menengah (11B dan 90B) - ini memberikan opsi penyebaran yang fleksibel,
- Variasi hanya teks (1B dan 3B) - ini memungkinkan model untuk disebarkan di edge / perangkat mobile dan menyediakan latensi rendah

Dukungan multimodal ini merupakan langkah besar di dunia model sumber terbuka. Contoh kode di bawah ini menggunakan prompt gambar dan teks untuk mendapatkan analisis gambar. Karena Llama 3.2 90B Vision Instruct telah dihentikan, contoh menggunakan `Llama-4-Scout-17B-16E-Instruct`, alternatif multimodal asli yang saat ini tersedia.


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

Setelah menyelesaikan pelajaran ini, lihat koleksi [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan Generative AI Anda!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->