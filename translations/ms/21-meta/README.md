# Membina Dengan Model Keluarga Meta 

## Pengenalan 

Pelajaran ini akan merangkumi: 

- Meneroka dua model utama keluarga Meta - Llama 3.1 dan Llama 3.2, serta alternatif yang tersedia sekarang yang digunakan dalam contoh kod (Llama 3.3 dan Llama 4) 
- Memahami kes penggunaan dan senario untuk setiap model 
- Contoh kod untuk menunjukkan ciri unik setiap model 


## Keluarga Model Meta 

Dalam pelajaran ini, kita akan meneroka 2 model dari keluarga Meta atau "Llama Herd" - Llama 3.1 dan Llama 3.2. Contoh kod yang boleh dijalankan menggunakan Llama 3.3 dan Llama 4, yang merupakan alternatif yang kini tersedia dalam katalog Model Microsoft Foundry.

Model-model ini datang dalam varian yang berbeza dan tersedia dalam [katalog Model Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Nota:** Model GitHub akan bersara pada akhir Julai 2026. Berikut adalah maklumat lanjut mengenai penggunaan [Model Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) untuk membuat prototaip dengan model AI.

> **Nota:** Versi model khusus yang asalnya digunakan dalam pelajaran ini (Llama 3.1 70B/405B Instruct, Llama 3.2 11B/90B Vision Instruct) telahpun dikeluarkan dari katalog Model Microsoft Foundry. Contoh kod di bawah menggunakan `Llama-3.3-70B-Instruct` dan `Llama-4-Scout-17B-16E-Instruct` sebagai alternatif yang kini tersedia dalam katalog Model Microsoft Foundry, jadi ia masih boleh dijalankan hari ini.

Varian Model (seperti yang asalnya dibincangkan dalam pelajaran ini): 
- Llama 3.1 - 70B Instruct (dikeluarkan) 
- Llama 3.1 - 405B Instruct (dikeluarkan) 
- Llama 3.2 - 11B Vision Instruct (dikeluarkan) 
- Llama 3.2 - 90B Vision Instruct (dikeluarkan) 

Alternatif yang kini tersedia dan digunakan dalam contoh kod: 
- Llama 3.3 - 70B Instruct (`Llama-3.3-70B-Instruct`) 
- Llama 4 Scout - 17B 16E Instruct (`Llama-4-Scout-17B-16E-Instruct`) 

*Nota: Varian Llama 3 yang dibincangkan di atas dikekalkan untuk konteks sejarah dan tidak lagi tersedia dalam Model Microsoft Foundry.*

## Llama 3.1 

Dengan 405 Bilion Parameter, Llama 3.1 tergolong dalam kategori LLM sumber terbuka. 

Model ini merupakan peningkatan kepada keluaran awal Llama 3 dengan menawarkan: 

- Tingkap konteks yang lebih besar - 128k token berbanding 8k token 
- Maksimum Token Output lebih besar - 4096 berbanding 2048 
- Sokongan Multibahasa yang lebih baik - disebabkan peningkatan token latihan 

Ini membolehkan Llama 3.1 mengendalikan kes penggunaan yang lebih kompleks apabila membina aplikasi GenAI termasuk: 
- Panggilan Fungsi Asli - kemampuan memanggil alat dan fungsi luaran selain aliran kerja LLM
- Prestasi RAG Lebih Baik - disebabkan tingkap konteks yang lebih besar 
- Penjanaan Data Sintetik - kemampuan untuk mencipta data yang berkesan untuk tugasan seperti penyelarasan halus 

### Panggilan Fungsi Asli 

Llama 3.1 telah diselaraskan untuk menjadi lebih berkesan membuat panggilan fungsi atau alat. Ia juga mempunyai dua alat terbina dalam yang model boleh kenal pasti perlu digunakan berdasarkan arahan dari pengguna. Alat-alat ini ialah: 

- **Brave Search** - Boleh digunakan untuk mendapatkan maklumat terkini seperti cuaca dengan melakukan carian web 
- **Wolfram Alpha** - Boleh digunakan untuk pengiraan matematik yang lebih kompleks jadi penulisan fungsi sendiri tidak diperlukan. 

Anda juga boleh mencipta alat khusus sendiri yang boleh dipanggil oleh LLM. 

Dalam contoh kod di bawah: 

- Kami mentakrifkan alat yang tersedia (brave_search, wolfram_alpha) dalam arahan sistem. 
- Menghantar arahan pengguna yang bertanya tentang cuaca di sebuah bandar tertentu. 
- LLM akan membalas dengan panggilan alat kepada alat Brave Search yang akan kelihatan seperti ini `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Nota: Contoh ini hanya membuat panggilan alat, jika anda ingin mendapatkan keputusan, anda perlu mencipta akaun percuma di halaman API Brave dan mentakrifkan fungsi itu sendiri.

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

Walaupun merupakan LLM, satu kekangan Llama 3.1 ialah kekurangan multimodality. Iaitu, ketidakmampuan menggunakan jenis input yang berbeza seperti imej sebagai arahan dan menyediakan respons. Keupayaan ini adalah salah satu ciri utama Llama 3.2. Ciri-ciri ini juga termasuk: 

- Multimodality - mempunyai keupayaan menilai kedua-dua teks dan arahan imej 
- Variasi Saiz Kecil hingga Sederhana (11B dan 90B) - ini menyediakan pilihan penerapan yang fleksibel, 
- Variasi Teks sahaja (1B dan 3B) - ini membolehkan model digunakan pada peranti tepi / mudah alih dan menyediakan kelewatan rendah 

Sokongan multimodal mewakili langkah besar dalam dunia model sumber terbuka. Contoh kod di bawah mengambil kedua-dua arahan imej dan teks untuk mendapatkan analisis imej. Oleh kerana Llama 3.2 90B Vision Instruct telah dikeluarkan, contoh ini menggunakan `Llama-4-Scout-17B-16E-Instruct`, alternatif multimodal asli yang kini tersedia. 


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

## Pembelajaran tidak berhenti di sini, teruskan perjalanan

Selepas menamatkan pelajaran ini, periksa koleksi [Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif anda!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->