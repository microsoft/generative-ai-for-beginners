# Membina Dengan Model Keluarga Meta

## Pengenalan

Pelajaran ini akan merangkumi:

- Meneroka dua model utama keluarga Meta - Llama 3.1 dan Llama 3.2
- Memahami kes penggunaan dan senario untuk setiap model
- Contoh kod untuk menunjukkan ciri unik setiap model

## Keluarga Model Meta

Dalam pelajaran ini, kita akan meneroka 2 model dari keluarga Meta atau "Llama Herd" - Llama 3.1 dan Llama 3.2.

Model-model ini datang dalam variasi yang berbeza dan tersedia di pasaran Model GitHub. Berikut adalah maklumat lanjut tentang menggunakan Model GitHub untuk [mencipta prototaip dengan model AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Variasi Model:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Nota: Llama 3 juga tersedia di Model GitHub tetapi tidak akan dibincangkan dalam pelajaran ini*

## Llama 3.1

Dengan 405 Bilion Parameter, Llama 3.1 tergolong dalam kategori LLM sumber terbuka.

Model ini merupakan peningkatan kepada keluaran sebelumnya Llama 3 dengan menawarkan:

- Tetingkap konteks lebih besar - 128k token berbanding 8k token
- Maksimum Token Keluaran lebih besar - 4096 berbanding 2048
- Sokongan Multibahasa lebih baik - disebabkan peningkatan dalam token latihan

Ini membolehkan Llama 3.1 mengendalikan kes penggunaan yang lebih kompleks ketika membina aplikasi GenAI termasuk:
- Panggilan Fungsi Asli - keupayaan untuk memanggil alat dan fungsi luaran di luar aliran kerja LLM
- Prestasi RAG lebih baik - disebabkan oleh tetingkap konteks yang lebih tinggi
- Penghasilan Data Sintetik - keupayaan untuk mencipta data yang berkesan untuk tugasan seperti penalaan halus

### Panggilan Fungsi Asli

Llama 3.1 telah disesuaikan untuk menjadi lebih berkesan dalam membuat panggilan fungsi atau alat. Ia juga mempunyai dua alat terbina dalam yang boleh dikenal pasti oleh model sebagai perlu digunakan berdasarkan arahan daripada pengguna. Alat ini adalah:

- **Brave Search** - Boleh digunakan untuk mendapatkan maklumat terkini seperti cuaca dengan melakukan carian web
- **Wolfram Alpha** - Boleh digunakan untuk pengiraan matematik yang lebih kompleks supaya anda tidak perlu menulis fungsi sendiri.

Anda juga boleh mencipta alat khusus anda sendiri yang boleh dipanggil oleh LLM.

Dalam contoh kod di bawah:

- Kami mendefinisikan alat yang tersedia (brave_search, wolfram_alpha) dalam arahan sistem.
- Menghantar arahan pengguna yang bertanya tentang cuaca di sebuah bandar tertentu.
- LLM akan bertindak balas dengan panggilan alat kepada alat Brave Search yang akan kelihatan seperti ini `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Nota: Contoh ini hanya membuat panggilan alat, jika anda ingin mendapatkan keputusan, anda perlu membuat akaun percuma di halaman API Brave dan mendefinisikan fungsi itu sendiri.*

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

Walaupun merupakan LLM, satu kekangan Llama 3.1 ialah kekurangan multimodaliti. Iaitu, ketidakmampuan menggunakan jenis input yang berbeza seperti imej sebagai arahan dan memberikan respons. Keupayaan ini adalah salah satu ciri utama Llama 3.2. Ciri-ciri ini juga termasuk:

- Multimodaliti - mempunyai keupayaan untuk menilai kedua-dua arahan teks dan imej
- Variasi saiz kecil hingga sederhana (11B dan 90B) - ini menyediakan pilihan pelaksanaan yang fleksibel,
- Variasi hanya teks (1B dan 3B) - ini membolehkan model digunakan pada peranti edge / mudah alih dan menyediakan latensi rendah

Sokongan multimodal ini mewakili langkah besar dalam dunia model sumber terbuka. Contoh kod di bawah mengambil kedua-dua input imej dan teks untuk mendapatkan analisis imej dari Llama 3.2 90B.

### Sokongan Multimodal dengan Llama 3.2

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

## Pembelajaran tidak berhenti di sini, teruskan perjalanan

Selepas melengkapkan pelajaran ini, semak [koleksi Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif anda!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber rujukan yang sah. Untuk maklumat yang penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->