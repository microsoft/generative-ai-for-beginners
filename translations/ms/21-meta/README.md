# Membina Dengan Model Keluarga Meta 

## Pengenalan 

Pelajaran ini akan merangkumi: 

- Meneroka dua model utama keluarga Meta - Llama 3.1 dan Llama 3.2 
- Memahami kes penggunaan dan senario untuk setiap model 
- Contoh kod untuk menunjukkan ciri unik setiap model 


## Keluarga Model Meta 

Dalam pelajaran ini, kita akan meneroka 2 model dari keluarga Meta atau "Llama Herd" - Llama 3.1 dan Llama 3.2.

Model-model ini datang dalam pelbagai variasi dan tersedia dalam [katalog Model Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Nota:** GitHub Models akan dihentikan pada akhir Julai 2026. Berikut adalah lebih banyak butiran mengenai penggunaan [Model Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) untuk membuat prototaip dengan model AI.

Variasi Model: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Nota: Llama 3 juga tersedia dalam Model Microsoft Foundry tetapi tidak akan dibincangkan dalam pelajaran ini*

## Llama 3.1 

Dengan 405 Billion Parameter, Llama 3.1 tergolong dalam kategori LLM sumber terbuka. 

Model ini merupakan peningkatan kepada keluaran terdahulu Llama 3 dengan menawarkan: 

- Tetingkap konteks lebih besar - 128k token berbanding 8k token 
- Maksimum Token Output lebih besar - 4096 berbanding 2048 
- Sokongan Berbilang Bahasa lebih baik - disebabkan peningkatan token latihan 

Ini membolehkan Llama 3.1 mengendalikan kes penggunaan yang lebih kompleks semasa membina aplikasi GenAI termasuk: 
- Panggilan Fungsi Asli - keupayaan untuk memanggil alat dan fungsi luaran di luar aliran kerja LLM
- Prestasi RAG lebih baik - disebabkan tetingkap konteks yang lebih tinggi 
- Penjanaan Data Sintetik - keupayaan untuk mencipta data berkesan untuk tugasan seperti penalaan halus 

### Panggilan Fungsi Asli 

Llama 3.1 telah ditalaan dengan lebih berkesan untuk membuat panggilan fungsi atau alat. Ia juga mempunyai dua alat terbina dalam yang boleh dikenalpasti oleh model sebagai perlu digunakan berdasarkan prompt daripada pengguna. Alat-alat ini adalah: 

- **Brave Search** - Boleh digunakan untuk mendapatkan maklumat terkini seperti cuaca dengan melakukan carian web 
- **Wolfram Alpha** - Boleh digunakan untuk pengiraan matematik yang lebih kompleks supaya penulisan fungsi sendiri tidak diperlukan. 

Anda juga boleh mencipta alat tersuai anda sendiri yang boleh dipanggil oleh LLM. 

Dalam contoh kod di bawah: 

- Kami mentakrifkan alat yang tersedia (brave_search, wolfram_alpha) dalam prompt sistem. 
- Hantar prompt pengguna yang bertanya tentang cuaca di suatu bandar. 
- LLM akan memberi respons dengan panggilan alat ke alat Brave Search yang akan kelihatan seperti ini `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Nota: Contoh ini hanya membuat panggilan alat, jika anda ingin mendapatkan keputusan, anda perlu membuat akaun percuma di halaman API Brave dan mentakrifkan fungsi itu sendiri.

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

Walaupun menjadi LLM, salah satu kekangan Llama 3.1 ialah ketiadaan multimodaliti. Iaitu, ketidakmampuan menggunakan jenis input yang berbeza seperti imej sebagai prompt dan memberikan respons. Keupayaan ini adalah salah satu ciri utama Llama 3.2. Ciri-ciri ini juga termasuk: 

- Multimodaliti - mempunyai keupayaan untuk menilai kedua-dua prompt teks dan imej 
- Variasi saiz kecil hingga sederhana (11B dan 90B) - ini menyediakan pilihan pelaksanaan yang fleksibel, 
- Variasi teks sahaja (1B dan 3B) - ini membolehkan model digunakan pada peranti edge / mudah alih dan menyediakan latensi rendah 

Sokongan multimodal mewakili satu langkah besar dalam dunia model sumber terbuka. Contoh kod di bawah mengambil kedua-dua prompt imej dan teks untuk mendapatkan analisis imej daripada Llama 3.2 90B. 


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

# Dapatkan ini dari halaman "Overview" projek Microsoft Foundry anda
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

Selepas menamatkan pelajaran ini, semak koleksi [Pembelajaran AI Generatif kami](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk terus meningkatkan pengetahuan AI Generatif anda!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->