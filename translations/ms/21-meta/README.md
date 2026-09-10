# Membina Dengan Model Keluarga Meta 

## Pengenalan 

Pelajaran ini akan meliputi: 

- Meneroka dua model utama keluarga Meta - Llama 3.1 dan Llama 3.2 
- Memahami kes penggunaan dan senario untuk setiap model 
- Contoh kod untuk menunjukkan ciri unik setiap model 


## Keluarga Model Meta 

Dalam pelajaran ini, kami akan meneroka 2 model dari keluarga Meta atau "Llama Herd" - Llama 3.1 dan Llama 3.2.

Model-model ini datang dalam varian yang berbeza dan tersedia dalam [katalog Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Nota:** GitHub Models akan dihentikan pada akhir Julai 2026. Berikut adalah maklumat lanjut tentang menggunakan [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) untuk membuat prototaip dengan model AI.

Varian Model: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Nota: Llama 3 juga tersedia dalam Microsoft Foundry Models tetapi tidak akan dibincangkan dalam pelajaran ini*

## Llama 3.1 

Dengan 405 Bilion Parameter, Llama 3.1 tergolong dalam kategori LLM sumber terbuka. 

Model ini adalah peningkatan daripada keluaran awal Llama 3 dengan menawarkan: 

- Tetingkap konteks yang lebih besar - 128k token berbanding 8k token 
- Token Output Maksimum yang lebih besar - 4096 berbanding 2048 
- Sokongan Multibahasa yang lebih baik - disebabkan peningkatan token latihan 

Ini membolehkan Llama 3.1 menangani kes penggunaan yang lebih kompleks apabila membina aplikasi GenAI termasuk: 
- Panggilan Fungsi Asli - keupayaan untuk memanggil alat dan fungsi luaran di luar aliran kerja LLM
- Prestasi RAG yang lebih baik - disebabkan tetingkap konteks yang lebih tinggi 
- Penjanaan Data Sintetik - keupayaan untuk mencipta data berkesan untuk tugasan seperti penalaan halus 

### Panggilan Fungsi Asli 

Llama 3.1 telah ditalaan halus untuk menjadi lebih berkesan dalam membuat panggilan fungsi atau alat. Ia juga mempunyai dua alat terbina dalam yang model boleh kenal pasti sebagai perlu digunakan berdasarkan arahan dari pengguna. Alat-alat ini adalah: 

- **Brave Search** - Boleh digunakan untuk mendapatkan maklumat terkini seperti cuaca dengan melakukan carian web 
- **Wolfram Alpha** - Boleh digunakan untuk pengiraan matematik yang lebih kompleks jadi menulis fungsi sendiri tidak diperlukan. 

Anda juga boleh mencipta alat tersuai anda sendiri yang LLM boleh panggil. 

Dalam contoh kod di bawah: 

- Kami mentakrifkan alat yang tersedia (brave_search, wolfram_alpha) dalam arahan sistem. 
- Menghantar arahan pengguna yang bertanya tentang cuaca di sesuatu bandar. 
- LLM akan membalas dengan panggilan alat ke alat Brave Search yang akan kelihatan seperti ini `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Nota: Contoh ini hanya membuat panggilan alat, jika anda ingin mendapatkan keputusan, anda perlu membuat akaun percuma di halaman API Brave dan mendefinisikan fungsi itu sendiri.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Dapatkan ini dari halaman "Gambaran Keseluruhan" projek Microsoft Foundry anda
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

Walaupun merupakan LLM, satu kekurangan Llama 3.1 ialah kekurangan multimodaliti. Iaitu, ketidakmampuan menggunakan jenis input yang berbeza seperti imej sebagai arahan dan memberikan respons. Keupayaan ini adalah salah satu ciri utama Llama 3.2. Ciri-ciri ini juga termasuk: 

- Multimodaliti - mempunyai keupayaan untuk menilai arahan teks dan imej 
- Variasi saiz kecil hingga sederhana (11B dan 90B) - ini menyediakan pilihan penggunaan yang fleksibel, 
- Variasi hanya teks (1B dan 3B) - ini membolehkan model digunakan pada peranti edge / mudah alih dan memberikan latensi rendah 

Sokongan multimodal mewakili langkah besar dalam dunia model sumber terbuka. Contoh kod di bawah mengambil kedua-dua arahan imej dan teks untuk mendapatkan analisis imej dari Llama 3.2 90B. 


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

# Dapatkan ini dari halaman "Gambaran Keseluruhan" projek Microsoft Foundry anda
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

## Pembelajaran tidak berhenti di sini, teruskan perjalanan

Selepas menamatkan pelajaran ini, lihat koleksi [Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif anda!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->