[![Model Open Source](../../../translated_images/id/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Pendahuluan

AI Agents merupakan perkembangan menarik dalam AI Generatif, memungkinkan Large Language Models (LLMs) berkembang dari asisten menjadi agen yang mampu mengambil tindakan. Kerangka kerja AI Agent memungkinkan pengembang membuat aplikasi yang memberi LLM akses ke alat dan manajemen status. Kerangka kerja ini juga meningkatkan visibilitas, memungkinkan pengguna dan pengembang memantau tindakan yang direncanakan oleh LLM, sehingga meningkatkan pengelolaan pengalaman.

Pelajaran ini akan membahas area berikut:

- Memahami apa itu AI Agent - Apa sebenarnya AI Agent itu?
- Menjelajahi lima kerangka kerja AI Agent yang berbeda - Apa yang membuatnya unik?
- Menerapkan AI Agents ini ke berbagai kasus penggunaan - Kapan kita harus menggunakan AI Agents?

## Tujuan Pembelajaran

Setelah mengikuti pelajaran ini, Anda akan dapat:

- Menjelaskan apa itu AI Agents dan bagaimana mereka dapat digunakan.
- Memahami perbedaan antara beberapa Kerangka Kerja AI Agent populer, dan bagaimana mereka berbeda.
- Memahami bagaimana AI Agents berfungsi untuk membangun aplikasi dengan mereka.

## Apa Itu AI Agents?

AI Agents adalah bidang yang sangat menarik dalam dunia AI Generatif. Bersama dengan kegembiraan ini sering muncul kebingungan istilah dan penerapannya. Untuk menyederhanakan dan mencakup sebagian besar alat yang merujuk pada AI Agents, kami akan menggunakan definisi berikut:

AI Agents memungkinkan Large Language Models (LLMs) melakukan tugas dengan memberi mereka akses ke **status** dan **alat**.

![Model Agen](../../../translated_images/id/what-agent.21f2893bdfd01e6a.webp)

Mari kita definisikan istilah-istilah ini:

**Large Language Models** - Ini adalah model yang dirujuk sepanjang kursus ini seperti GPT-5, GPT-4o, dan Llama 3.3, dll.

**Status** - Ini merujuk pada konteks di mana LLM bekerja. LLM menggunakan konteks tindakan sebelumnya dan konteks sekarang, membimbing pengambilan keputusannya untuk tindakan berikutnya. Kerangka kerja AI Agent memungkinkan pengembang untuk mempertahankan konteks ini dengan lebih mudah.

**Alat** - Untuk menyelesaikan tugas yang diminta pengguna dan dirancang oleh LLM, LLM membutuhkan akses ke alat. Beberapa contoh alat bisa berupa basis data, API, aplikasi eksternal, atau bahkan LLM lain!

Definisi ini diharapkan memberi Anda dasar yang baik ke depan saat kita melihat bagaimana mereka diimplementasikan. Mari jelajahi beberapa kerangka kerja AI Agent yang berbeda:

## LangChain Agents

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) adalah implementasi dari definisi yang telah kami berikan di atas.

Untuk mengelola **status** , ia menggunakan fungsi bawaan yang disebut `AgentExecutor`. Fungsi ini menerima `agent` yang didefinisikan dan `tools` yang tersedia untuknya.

`Agent Executor` juga menyimpan riwayat obrolan untuk memberikan konteks percakapan.

![Langchain Agents](../../../translated_images/id/langchain-agents.edcc55b5d5c43716.webp)

LangChain menawarkan [katalog alat](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) yang dapat diimpor ke aplikasi Anda agar LLM dapat mengaksesnya. Alat-alat ini dibuat oleh komunitas dan tim LangChain.

Anda kemudian dapat mendefinisikan alat-alat ini dan meneruskannya ke `Agent Executor`.

Visibilitas adalah aspek penting lainnya saat membahas AI Agents. Penting bagi pengembang aplikasi untuk memahami alat mana yang digunakan LLM dan mengapa.. Untuk itu, tim di LangChain mengembangkan LangSmith.

## AutoGen

Kerangka kerja AI Agent berikutnya yang akan kita bahas adalah [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Fokus utama AutoGen adalah percakapan. Agen bersifat **dapat berbicara** dan **dapat disesuaikan**.

**Dapat berbicara -** LLM dapat memulai dan melanjutkan percakapan dengan LLM lain untuk menyelesaikan tugas. Ini dilakukan dengan membuat `AssistantAgents` dan memberikan mereka pesan sistem tertentu.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Dapat disesuaikan** - Agen dapat didefinisikan tidak hanya sebagai LLM tetapi juga sebagai pengguna atau alat. Sebagai pengembang, Anda dapat mendefinisikan `UserProxyAgent` yang bertanggung jawab untuk berinteraksi dengan pengguna untuk umpan balik dalam menyelesaikan tugas. Umpan balik ini dapat melanjutkan pelaksanaan tugas atau menghentikannya.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Status dan Alat

Untuk mengubah dan mengelola status, agen asisten menghasilkan kode Python untuk menyelesaikan tugas.

Berikut adalah contoh prosesnya:

![AutoGen](../../../translated_images/id/autogen.dee9a25a45fde584.webp)

#### LLM Didefinisikan dengan Pesan Sistem

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Pesan sistem ini mengarahkan LLM tertentu ini ke fungsi yang relevan untuk tugasnya. Ingat, dengan AutoGen Anda dapat memiliki beberapa AssistantAgents yang didefinisikan dengan pesan sistem yang berbeda.

#### Obrolan Dimulai oleh Pengguna

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Pesan dari user_proxy (Manusia) ini akan memulai proses Agen untuk mengeksplorasi fungsi yang mungkin harus dijalankan.

#### Fungsi Dieksekusi

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Setelah obrolan awal diproses, Agen akan mengirimkan alat yang disarankan untuk dipanggil. Dalam kasus ini, itu adalah fungsi bernama `get_weather`. Tergantung pada konfigurasi Anda, fungsi ini dapat secara otomatis dijalankan dan dibaca oleh Agen atau dapat dijalankan berdasarkan input pengguna.

Anda dapat menemukan daftar [contoh kode AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) untuk mengeksplorasi lebih lanjut cara memulai pembangunan.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) adalah SDK open-source Microsoft untuk membangun AI Agents dan sistem multi-agen dalam **Python** dan **.NET**. Ini menggabungkan kekuatan dua proyek Microsoft sebelumnya — fitur perusahaan dari **Semantic Kernel** dan orkestrasi multi-agen dari **AutoGen** — ke dalam satu kerangka kerja yang didukung. Jika Anda memulai proyek agen baru hari ini, ini adalah penerus yang direkomendasikan dari AutoGen.

Kerangka kerja ini dapat diskalakan dari satu **agen obrolan** hingga **alur kerja multi-agen** yang kompleks, dan terintegrasi langsung dengan Microsoft Foundry, Azure OpenAI, dan OpenAI. Ia juga menyediakan observabilitas bawaan melalui OpenTelemetry sehingga Anda dapat melacak apa yang dilakukan agen Anda secara tepat.

### Status dan Alat

**Status** - Kerangka kerja mengelola konteks percakapan untuk Anda melalui **threads**. Agen melacak riwayat pesan (permintaan pengguna, panggilan alat, dan hasilnya), sehingga setiap giliran dibangun berdasarkan giliran sebelumnya. Threads juga dapat dipertahankan, memungkinkan percakapan dijeda dan dilanjutkan nanti.

**Alat** - Anda memberi agen alat dengan meneruskan fungsi Python biasa. Parameter yang diberi anotasi tipe secara otomatis diubah menjadi skema, sehingga model tahu kapan dan bagaimana memanggilnya (panggilan fungsi). Kerangka kerja juga mendukung server Model Context Protocol (MCP) dan alat yang dihosting seperti interpreter kode.

Berikut adalah contoh satu agen dengan alat khusus:

```python
import asyncio
from typing import Annotated

from pydantic import Field
from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient


def get_weather(
    location: Annotated[str, Field(description="The location to get the weather for.")],
) -> str:
    """Get the weather for a given location."""
    return f"The weather in {location} is sunny with a high of 22°C."


async def main():
    agent = Agent(
        client=OpenAIChatClient(),
        instructions="You are a helpful assistant that can answer weather questions.",
        tools=[get_weather],
    )

    response = await agent.run("What's the weather in Amsterdam?")
    print(response)


asyncio.run(main())
```

Untuk terhubung ke Azure OpenAI di Microsoft Foundry, berikan endpoint dan kredensial Anda ke klien:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Alur kerja multi-agen

Kekuatan kerangka kerja ini benar-benar terlihat dalam orkestrasi beberapa agen bersama-sama. Misalnya, Anda dapat menjalankan agen satu per satu (masing-masing meneruskan konteks ke yang berikutnya) atau menjalankan beberapa agen secara paralel dan menggabungkan hasilnya:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Jalankan agen secara berurutan, meneruskan konteks percakapan sepanjang rantai
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Menyebarkan ke agen secara paralel, kemudian menggabungkan respons mereka
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Untuk menginstal kerangka kerja dan mulai:

```bash
pip install agent-framework-core
# Integrasi opsional
pip install agent-framework-openai       # OpenAI dan Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Anda dapat menjelajahi lebih lanjut di [repositori Microsoft Agent Framework](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) dan [dokumentasi resmi](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Kerangka kerja agen berikut yang akan kita jelajahi adalah [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Ini dikenal sebagai agen "code-first" karena alih-alih bekerja hanya dengan `string`, ia bisa bekerja dengan DataFrame di Python. Ini menjadi sangat berguna untuk tugas analisis data dan generasi. Misalnya seperti membuat grafik dan diagram atau menghasilkan angka acak.

### Status dan Alat

Untuk mengelola status percakapan, TaskWeaver menggunakan konsep `Planner`. `Planner` adalah LLM yang mengambil permintaan dari pengguna dan memetakan tugas yang harus diselesaikan untuk memenuhi permintaan tersebut.

Untuk menyelesaikan tugas, `Planner` diberikan akses ke kumpulan alat yang disebut `Plugins`. Ini bisa berupa kelas Python atau interpreter kode umum. Plugin ini disimpan sebagai embedding agar LLM dapat mencari plugin yang tepat dengan lebih baik.

![Taskweaver](../../../translated_images/id/taskweaver.da8559999267715a.webp)

Berikut adalah contoh plugin untuk menangani deteksi anomali:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Kode diverifikasi sebelum dieksekusi. Fitur lain untuk mengelola konteks di Taskweaver adalah `experience`. Experience memungkinkan konteks percakapan disimpan dalam jangka panjang di file YAML. Ini dapat dikonfigurasi sehingga LLM meningkat seiring waktu dalam tugas tertentu asalkan terpapar pada percakapan sebelumnya.

## JARVIS

Kerangka kerja agen terakhir yang akan kita jelajahi adalah [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Yang membuat JARVIS unik adalah ia menggunakan LLM untuk mengelola `status` percakapan dan `tools` adalah model AI lain. Setiap model AI ini adalah model khusus yang melakukan tugas tertentu seperti deteksi objek, transkripsi, atau memberi keterangan gambar.

![JARVIS](../../../translated_images/id/jarvis.762ddbadbd1a3a33.webp)

LLM, sebagai model tujuan umum, menerima permintaan dari pengguna dan mengidentifikasi tugas spesifik serta argumen/data yang dibutuhkan untuk menyelesaikan tugas tersebut.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM kemudian memformat permintaan dalam cara yang dapat dipahami oleh model AI khusus, seperti JSON. Setelah model AI mengembalikan prediksi berdasarkan tugas, LLM menerima respons tersebut.

Jika beberapa model diperlukan untuk menyelesaikan tugas, LLM juga akan menginterpretasikan respons dari model-model tersebut sebelum menggabungkannya untuk menghasilkan respons kepada pengguna.

Contoh di bawah menunjukkan bagaimana ini bekerja saat pengguna meminta deskripsi dan jumlah objek dalam sebuah gambar:

## Tugas

Untuk melanjutkan pembelajaran AI Agents Anda, Anda dapat membangun dengan Microsoft Agent Framework:

- Sebuah aplikasi yang mensimulasikan rapat bisnis dengan berbagai departemen dari startup pendidikan.
- Buat pesan sistem yang membimbing LLM dalam memahami persona dan prioritas yang berbeda, dan memungkinkan pengguna mengajukan ide produk baru.
- LLM kemudian harus menghasilkan pertanyaan tindak lanjut dari masing-masing departemen untuk menyempurnakan dan meningkatkan pitch dan ide produk.

## Pembelajaran tidak berhenti di sini, lanjutkan Perjalanan

Setelah menyelesaikan pelajaran ini, lihat koleksi [Belajar AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif Anda!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->