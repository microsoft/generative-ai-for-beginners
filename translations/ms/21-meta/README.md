<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:12:01+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "ms"
}
-->
# Membina Dengan Model Keluarga Meta

## Pengenalan

Pelajaran ini akan merangkumi:

- Meneroka dua model utama keluarga Meta - Llama 3.1 dan Llama 3.2
- Memahami kes penggunaan dan senario untuk setiap model
- Contoh kod untuk menunjukkan ciri unik setiap model

## Keluarga Model Meta

Dalam pelajaran ini, kita akan meneroka 2 model dari keluarga Meta atau "Llama Herd" - Llama 3.1 dan Llama 3.2

Model-model ini datang dalam variasi yang berbeza dan tersedia di pasaran Model GitHub. Berikut adalah maklumat lanjut mengenai penggunaan Model GitHub untuk [membuat prototaip dengan model AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Variasi Model:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*Nota: Llama 3 juga tersedia di Model GitHub tetapi tidak akan dibincangkan dalam pelajaran ini*

## Llama 3.1

Dengan 405 Bilion Parameter, Llama 3.1 tergolong dalam kategori LLM sumber terbuka.

Model ini adalah peningkatan kepada keluaran terdahulu Llama 3 dengan menawarkan:

- Tetingkap konteks yang lebih besar - 128k token berbanding 8k token  
- Maksimum Token Output yang lebih besar - 4096 berbanding 2048  
- Sokongan Multibahasa yang lebih baik - disebabkan peningkatan token latihan  

Ini membolehkan Llama 3.1 mengendalikan kes penggunaan yang lebih kompleks apabila membina aplikasi GenAI termasuk:  
- Panggilan Fungsi Asli - keupayaan untuk memanggil alat dan fungsi luaran di luar aliran kerja LLM  
- Prestasi RAG yang lebih baik - disebabkan tetingkap konteks yang lebih tinggi  
- Penjanaan Data Sintetik - keupayaan untuk menghasilkan data berkesan untuk tugasan seperti penalaan halus  

### Panggilan Fungsi Asli

Llama 3.1 telah ditala halus untuk menjadi lebih berkesan dalam membuat panggilan fungsi atau alat. Ia juga mempunyai dua alat terbina dalam yang boleh dikenal pasti oleh model sebagai perlu digunakan berdasarkan arahan daripada pengguna. Alat-alat ini adalah:

- **Brave Search** - Boleh digunakan untuk mendapatkan maklumat terkini seperti cuaca dengan melakukan carian web  
- **Wolfram Alpha** - Boleh digunakan untuk pengiraan matematik yang lebih kompleks supaya anda tidak perlu menulis fungsi sendiri.  

Anda juga boleh mencipta alat tersuai anda sendiri yang boleh dipanggil oleh LLM.

Dalam contoh kod di bawah:

- Kami mentakrifkan alat yang tersedia (brave_search, wolfram_alpha) dalam arahan sistem.  
- Menghantar arahan pengguna yang bertanya tentang cuaca di sebuah bandar tertentu.  
- LLM akan memberi respons dengan panggilan alat kepada Brave Search yang akan kelihatan seperti ini `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Nota: Contoh ini hanya membuat panggilan alat, jika anda ingin mendapatkan keputusan, anda perlu membuat akaun percuma di halaman Brave API dan mentakrifkan fungsi itu sendiri*

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

Walaupun merupakan LLM, satu kekangan yang ada pada Llama 3.1 adalah multimodaliti. Iaitu, keupayaan menggunakan jenis input yang berbeza seperti imej sebagai arahan dan memberikan respons. Keupayaan ini adalah salah satu ciri utama Llama 3.2. Ciri-ciri lain termasuk:

- Multimodaliti - mempunyai keupayaan untuk menilai kedua-dua arahan teks dan imej  
- Variasi saiz kecil hingga sederhana (11B dan 90B) - ini menyediakan pilihan pelaksanaan yang fleksibel,  
- Variasi hanya teks (1B dan 3B) - ini membolehkan model digunakan pada peranti edge / mudah alih dan memberikan latensi rendah  

Sokongan multimodal ini merupakan satu langkah besar dalam dunia model sumber terbuka. Contoh kod di bawah mengambil kedua-dua arahan imej dan teks untuk mendapatkan analisis imej daripada Llama 3.2 90B.

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

## Pembelajaran tidak berhenti di sini, teruskan Perjalanan

Selepas menamatkan pelajaran ini, lihat koleksi [Pembelajaran AI Generatif kami](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk terus meningkatkan pengetahuan AI Generatif anda!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.