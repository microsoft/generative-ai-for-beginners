[![Open Source Models](../../../translated_images/id/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Pendahuluan

Agen AI mewakili perkembangan menarik dalam Generative AI, memungkinkan Large Language Models (LLM) berkembang dari asisten menjadi agen yang mampu mengambil tindakan. Kerangka kerja Agen AI memungkinkan pengembang membuat aplikasi yang memberi LLM akses ke alat dan manajemen status. Kerangka ini juga meningkatkan visibilitas, memungkinkan pengguna dan pengembang memantau tindakan yang direncanakan oleh LLM, sehingga memperbaiki manajemen pengalaman.

Pelajaran ini akan mencakup area berikut:

- Memahami apa itu Agen AI - Apa sebenarnya Agen AI itu?
- Menjelajahi lima Framework Agen AI yang berbeda - Apa yang membuat mereka unik?
- Menerapkan Agen AI tersebut ke berbagai kasus penggunaan - Kapan kita harus menggunakan Agen AI?

## Tujuan pembelajaran

Setelah mengikuti pelajaran ini, Anda akan dapat:

- Menjelaskan apa itu Agen AI dan bagaimana mereka dapat digunakan.
- Memahami perbedaan antara beberapa Framework Agen AI populer, dan bagaimana mereka berbeda.
- Memahami bagaimana Agen AI berfungsi untuk membangun aplikasi dengan mereka.

## Apa Itu Agen AI?

Agen AI adalah bidang yang sangat menarik dalam dunia Generative AI. Bersama dengan kegembiraan ini kadang muncul kebingungan mengenai istilah dan penerapannya. Untuk membuatnya sederhana dan mencakup sebagian besar alat yang merujuk pada Agen AI, kami akan menggunakan definisi ini:

Agen AI memungkinkan Large Language Models (LLM) melakukan tugas dengan memberi mereka akses ke **status** dan **alat**.

![Agent Model](../../../translated_images/id/what-agent.21f2893bdfd01e6a.webp)

Mari definisikan istilah-istilah ini:

**Large Language Models** - Ini adalah model yang disebutkan sepanjang kursus ini seperti GPT-3.5, GPT-4, Llama-2, dll.

**Status** - Ini merujuk pada konteks tempat LLM bekerja. LLM menggunakan konteks dari tindakan masa lalunya dan konteks saat ini, membimbing pengambilan keputusan untuk tindakan selanjutnya. Kerangka Kerja Agen AI memudahkan pengembang menjaga konteks ini.

**Alat** - Untuk menyelesaikan tugas yang diminta pengguna dan telah direncanakan oleh LLM, LLM membutuhkan akses ke alat. Contoh alat bisa berupa basis data, API, aplikasi eksternal atau bahkan LLM lain!

Definisi ini diharapkan memberi Anda landasan yang baik ke depan saat kita melihat bagaimana mereka diimplementasikan. Mari jelajahi beberapa kerangka kerja Agen AI yang berbeda:

## LangChain Agents

[LangChain Agents](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) adalah implementasi dari definisi yang kami berikan di atas.

Untuk mengelola **status**, ia menggunakan fungsi bawaan yang disebut `AgentExecutor`. Ini menerima `agent` yang sudah ditentukan dan `tools` yang tersedia untuknya.

`Agent Executor` juga menyimpan riwayat obrolan untuk memberikan konteks percakapan.

![Langchain Agents](../../../translated_images/id/langchain-agents.edcc55b5d5c43716.webp)

LangChain menawarkan [katalog alat](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) yang dapat diimpor ke aplikasi Anda di mana LLM dapat mengaksesnya. Ini dibuat oleh komunitas dan tim LangChain.

Anda kemudian dapat menentukan alat ini dan memberikannya ke `Agent Executor`.

Visibilitas adalah aspek penting lainnya saat membahas Agen AI. Penting bagi pengembang aplikasi untuk memahami alat mana yang digunakan LLM dan mengapa. Untuk itu, tim di LangChain telah mengembangkan LangSmith.

## AutoGen

Kerangka kerja Agen AI berikut yang akan kita bahas adalah [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Fokus utama AutoGen adalah percakapan. Agen bersifat **dapat diajak bicara** dan **dapat disesuaikan**.

**Dapat diajak bicara -** LLM bisa memulai dan melanjutkan percakapan dengan LLM lain untuk menyelesaikan tugas. Ini dilakukan dengan membuat `AssistantAgents` dan memberi mereka pesan sistem khusus.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Dapat disesuaikan** - Agen dapat didefinisikan tidak hanya sebagai LLM tetapi juga sebagai pengguna atau alat. Sebagai pengembang, Anda dapat mendefinisikan `UserProxyAgent` yang bertugas berinteraksi dengan pengguna untuk umpan balik dalam menyelesaikan tugas. Umpan balik ini dapat melanjutkan atau menghentikan pelaksanaan tugas.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Status dan Alat

Untuk mengubah dan mengelola status, agen asisten menghasilkan kode Python untuk menyelesaikan tugas.

Berikut contoh prosesnya:

![AutoGen](../../../translated_images/id/autogen.dee9a25a45fde584.webp)

#### LLM Didefinisikan dengan Pesan Sistem

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Pesan sistem ini mengarahkan LLM tertentu ini ke fungsi yang relevan untuk tugasnya. Ingat, dengan AutoGen Anda bisa memiliki beberapa AssistantAgents dengan pesan sistem berbeda.

#### Obrolan Dimulai oleh Pengguna

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Pesan dari user_proxy (Manusia) ini yang akan memulai proses Agen untuk mengeksplorasi fungsi yang mungkin harus dijalankan.

#### Fungsi Dijalankan

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Setelah obrolan awal diproses, Agen akan mengirimkan alat yang disarankan untuk dipanggil. Dalam kasus ini, itu sebuah fungsi bernama `get_weather`. Bergantung pada konfigurasi Anda, fungsi ini bisa dijalankan otomatis dan dibaca oleh Agen atau dijalankan berdasarkan input pengguna.

Anda dapat menemukan daftar [contoh kode AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) untuk mengeksplorasi lebih lanjut bagaimana memulai pembuatan.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) adalah SDK open-source Microsoft untuk membangun Agen AI dan sistem multi-agen dalam **Python** dan **.NET**. Ini menggabungkan kekuatan dua proyek Microsoft sebelumnya — fitur enterprise dari **Semantic Kernel** dan orkestrasi multi-agen dari **AutoGen** — ke dalam satu kerangka kerja yang didukung. Jika Anda memulai proyek agen baru hari ini, ini adalah pengganti yang direkomendasikan untuk AutoGen.

Kerangka ini dapat diskalakan dari satu **agen obrolan** hingga **alur kerja multi-agen** yang kompleks, dan terintegrasi langsung dengan Microsoft Foundry, Azure OpenAI, dan OpenAI. Ia juga menyediakan pengamatan bawaan melalui OpenTelemetry sehingga Anda dapat melacak apa yang dilakukan agen Anda secara tepat.

### Status dan Alat

**Status** - Kerangka mengelola konteks percakapan untuk Anda melalui **threads**. Agen melacak riwayat pesan (permintaan pengguna, panggilan alat, dan hasilnya), sehingga setiap giliran membangun atas yang sebelumnya. Threads juga dapat disimpan agar percakapan dapat dijeda dan dilanjutkan nanti.

**Alat** - Anda memberikan alat kepada agen dengan melewatkan fungsi Python biasa. Parameter yang dianotasi tipe otomatis menjadi skema, sehingga model tahu bagaimana dan kapan memanggilnya (pemanggilan fungsi). Kerangka juga mendukung server Model Context Protocol (MCP) dan alat yang dihosting seperti interpreter kode.

Berikut contoh agen tunggal dengan alat kustom:

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

Untuk menghubungkan ke Azure OpenAI di Microsoft Foundry, lewati endpoint dan kredensial Anda ke klien:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Alur kerja multi-agen

Keunggulan kerangka adalah mengorkestrasi beberapa agen bersama-sama. Misalnya, Anda dapat menjalankan agen satu per satu (masing-masing meneruskan konteks ke yang berikutnya) atau menyebar ke beberapa agen secara paralel dan mengagregasi hasilnya:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Jalankan agen secara berurutan, meneruskan konteks percakapan sepanjang rantai
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Sebarkan ke agen secara paralel, kemudian gabungkan respons mereka
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Untuk menginstal kerangka dan memulai:

```bash
pip install agent-framework-core
# Integrasi opsional
pip install agent-framework-openai       # OpenAI dan Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Anda dapat mengeksplorasi lebih lanjut di [repositori Microsoft Agent Framework](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) dan [dokumentasi resmi](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Kerangka agen berikut yang akan kita jelajahi adalah [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Ini dikenal sebagai agen "code-first" karena alih-alih hanya bekerja dengan `strings`, ia dapat bekerja dengan DataFrames di Python. Ini sangat berguna untuk analisis data dan tugas pembuatan. Ini bisa berupa membuat grafik dan bagan atau menghasilkan angka acak.

### Status dan Alat

Untuk mengelola status percakapan, TaskWeaver menggunakan konsep `Planner`. `Planner` adalah LLM yang menerima permintaan dari pengguna dan memetakan tugas yang perlu diselesaikan untuk memenuhi permintaan tersebut.

Untuk menyelesaikan tugas, `Planner` dikenalkan pada koleksi alat yang disebut `Plugins`. Ini bisa berupa kelas Python atau interpreter kode umum. Plugin ini disimpan sebagai embedding agar LLM dapat mencari plugin yang tepat dengan lebih baik.

![Taskweaver](../../../translated_images/id/taskweaver.da8559999267715a.webp)

Berikut contoh plugin untuk menangani deteksi anomali:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Kode diverifikasi sebelum dieksekusi. Fitur lain untuk mengelola konteks di Taskweaver adalah `experience`. Experience memungkinkan konteks percakapan disimpan dalam jangka panjang di file YAML. Ini dapat dikonfigurasi agar LLM meningkat seiring waktu pada tugas tertentu dengan paparan percakapan sebelumnya.

## JARVIS

Kerangka agen terakhir yang kita jelajahi adalah [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Yang membuat JARVIS unik adalah ia menggunakan LLM untuk mengelola `status` percakapan dan `alat` adalah model AI lainnya. Setiap model AI adalah model khusus yang melakukan tugas tertentu seperti pendeteksian objek, transkripsi atau pemberian caption gambar.

![JARVIS](../../../translated_images/id/jarvis.762ddbadbd1a3a33.webp)

LLM, sebagai model serbaguna, menerima permintaan dari pengguna dan mengidentifikasi tugas spesifik serta argumen/data yang diperlukan untuk menyelesaikan tugas.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM kemudian memformat permintaan dengan cara agar model AI khusus dapat menginterpretasinya, seperti JSON. Setelah model AI mengembalikan prediksi berdasarkan tugas, LLM menerima respons tersebut.

Jika beberapa model diperlukan untuk menyelesaikan tugas, ia juga akan menginterpretasikan respons dari model-model tersebut sebelum menggabungkannya untuk menghasilkan respons kepada pengguna.

Contoh di bawah ini menunjukkan bagaimana ini bekerja saat pengguna meminta deskripsi dan jumlah objek dalam sebuah gambar:

## Tugas

Untuk melanjutkan pembelajaran Anda tentang Agen AI Anda dapat membangun dengan Microsoft Agent Framework:

- Sebuah aplikasi yang mensimulasikan rapat bisnis dengan berbagai departemen dari startup pendidikan.
- Buat pesan sistem yang memandu LLM dalam memahami persona dan prioritas berbeda, dan memungkinkan pengguna mengajukan ide produk baru.
- Kemudian LLM harus menghasilkan pertanyaan lanjutan dari setiap departemen untuk menyempurnakan dan meningkatkan pitch serta ide produk.

## Pembelajaran tidak berhenti di sini, lanjutkan Perjalanan

Setelah menyelesaikan pelajaran ini, lihat [koleksi Pembelajaran Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan Generative AI Anda!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->