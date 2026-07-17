[![Open Source Models](../../../translated_images/ms/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Pengenalan

Ejen AI mewakili perkembangan yang menarik dalam AI Generatif, membolehkan Model Bahasa Besar (LLM) berkembang dari pembantu menjadi ejen yang mampu mengambil tindakan. Rangka kerja Ejen AI membolehkan pembangun mencipta aplikasi yang memberi LLM akses kepada alat dan pengurusan keadaan. Rangka kerja ini juga meningkatkan keterlihatan, membolehkan pengguna dan pembangun memantau tindakan yang dirancang oleh LLM, dengan itu meningkatkan pengurusan pengalaman.

Pelajaran ini akan meliputi bidang berikut:

- Memahami apa itu Ejen AI - Apa sebenarnya Ejen AI?
- Meneroka lima Rangka Kerja Ejen AI yang berbeza - Apa yang menjadikannya unik?
- Mengaplikasikan Ejen AI ini kepada pelbagai kes penggunaan - Bila kita harus menggunakan Ejen AI?

## Matlamat pembelajaran

Selepas mengambil pelajaran ini, anda akan dapat:

- Menjelaskan apa itu Ejen AI dan bagaimana ia boleh digunakan.
- Memahami perbezaan antara beberapa Rangka Kerja Ejen AI yang popular, dan bagaimana ia berbeza.
- Memahami bagaimana Ejen AI berfungsi untuk membina aplikasi dengannya.

## Apakah Ejen AI?

Ejen AI adalah bidang yang sangat menarik dalam dunia AI Generatif. Dengan keseronokan ini kadangkala datang kekeliruan istilah dan aplikasinya. Untuk memudahkan dan merangkumi kebanyakan alat yang merujuk kepada Ejen AI, kami akan menggunakan definisi ini:

Ejen AI membolehkan Model Bahasa Besar (LLM) melaksanakan tugas dengan memberikan mereka akses kepada **keadaan** dan **alat**.

![Agent Model](../../../translated_images/ms/what-agent.21f2893bdfd01e6a.webp)

Mari kita definisikan istilah ini:

**Model Bahasa Besar** - Ini adalah model yang dirujuk sepanjang kursus ini seperti GPT-5, GPT-4o, dan Llama 3.3, dan lain-lain.

**Keadaan** - Ini merujuk pada konteks di mana LLM bekerja. LLM menggunakan konteks tindakan masa lalu dan konteks semasa, membimbing pembuatan keputusannya untuk tindakan selanjutnya. Rangka Kerja Ejen AI membolehkan pembangun mengekalkan konteks ini dengan lebih mudah.

**Alat** - Untuk menyelesaikan tugas yang diminta pengguna dan dirancang oleh LLM, LLM memerlukan akses kepada alat. Contoh alat boleh jadi pangkalan data, API, aplikasi luaran atau bahkan LLM lain!

Definisi ini diharap dapat memberi anda asas yang baik semasa kita melihat bagaimana ia dilaksanakan. Mari kita terokai beberapa rangka kerja Ejen AI yang berbeza:

## Ejen LangChain

[Ejen LangChain](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) adalah pelaksanaan definisi yang telah kami berikan di atas.

Untuk mengurus **keadaan**, ia menggunakan fungsi terbina dalam yang dipanggil `AgentExecutor`. Ini menerima `agent` yang ditakrifkan dan `tools` yang tersedia kepadanya.

`Agent Executor` juga menyimpan sejarah sembang untuk menyediakan konteks perbualan.

![Langchain Agents](../../../translated_images/ms/langchain-agents.edcc55b5d5c43716.webp)

LangChain menawarkan [katalog alat](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) yang boleh diimport ke dalam aplikasi anda di mana LLM boleh mendapatkan akses kepadanya. Ini dibuat oleh komuniti dan oleh pasukan LangChain.

Anda kemudiannya boleh mendefinisikan alat ini dan memberikannya kepada `Agent Executor`.

Keterlihatan adalah aspek penting lain apabila bercakap tentang Ejen AI. Penting bagi pembangun aplikasi untuk memahami alat mana yang digunakan oleh LLM dan mengapa. Untuk itu, pasukan di LangChain telah membangunkan LangSmith.

## AutoGen

Rangka kerja Ejen AI seterusnya yang akan kita bincangkan ialah [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Fokus utama AutoGen adalah perbualan. Ejen adalah kedua-duanya **boleh berbual** dan **boleh disesuaikan**.

**Boleh berbual -** LLM boleh memulakan dan meneruskan perbualan dengan LLM lain untuk menyelesaikan tugas. Ini dilakukan dengan membuat `AssistantAgents` dan memberikan mesej sistem yang spesifik kepada mereka.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Boleh disesuaikan** - Ejen boleh ditakrifkan bukan hanya sebagai LLM tetapi juga sebagai pengguna atau alat. Sebagai pembangun, anda boleh mendefinisikan `UserProxyAgent` yang bertanggungjawab berinteraksi dengan pengguna untuk maklum balas dalam menyelesaikan tugas. Maklum balas ini boleh meneruskan pelaksanaan tugas atau menghentikannya.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Keadaan dan Alat

Untuk mengubah dan mengurus keadaan, seorang ejen pembantu menghasilkan kod Python untuk menyelesaikan tugas.

Berikut adalah contoh prosesnya:

![AutoGen](../../../translated_images/ms/autogen.dee9a25a45fde584.webp)

#### LLM Ditakrifkan dengan Mesej Sistem

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Mesej sistem ini mengarahkan LLM khusus ini fungsi mana yang relevan untuk tugasan yang dihadapi. Ingat, dengan AutoGen anda boleh mempunyai beberapa AssistantAgents yang ditakrifkan dengan mesej sistem yang berbeza.

#### Sembang Dimulakan oleh Pengguna

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Mesej dari user_proxy (Manusia) ini adalah yang akan memulakan proses ejen untuk meneroka fungsi yang mungkin perlu dilaksanakan.

#### Fungsi Dilaksanakan

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Setelah sembang awal diproses, ejen akan menghantar alat yang dicadangkan untuk dipanggil. Dalam kes ini, ia adalah fungsi yang dipanggil `get_weather`. Bergantung pada konfigurasi anda, fungsi ini boleh dilaksanakan secara automatik dan dibaca oleh ejen atau boleh dilaksanakan berdasarkan input pengguna.

Anda boleh mendapatkan senarai [contoh kod AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) untuk menerokai bagaimana memulakan pembinaan.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) adalah SDK sumber terbuka Microsoft untuk membina Ejen AI dan sistem multi-ejen dalam kedua-dua **Python** dan **.NET**. Ia menggabungkan kekuatan dua projek Microsoft terdahulu — ciri enterprise **Semantic Kernel** dan orkestrasi multi-ejen **AutoGen** — ke dalam satu rangka kerja yang disokong. Jika anda memulakan projek ejen baru hari ini, ini adalah penerus yang disyorkan untuk AutoGen.

Rangka kerja ini berkembang dari satu **ejen sembang** sehingga **aliran kerja multi-ejen** yang kompleks, dan ia berintegrasi secara langsung dengan Microsoft Foundry, Azure OpenAI, dan OpenAI. Ia juga menyediakan kebolehlihatan terbina dalam melalui OpenTelemetry supaya anda boleh menjejaki dengan tepat apa yang dilakukan oleh ejen anda.

### Keadaan dan Alat

**Keadaan** - Rangka kerja mengurus konteks perbualan untuk anda melalui **benang**. Ejen menyimpan sejarah mesej (permintaan pengguna, panggilan alat, dan hasilnya), jadi setiap giliran dibina berdasarkan yang sebelumnya. Benang juga boleh disimpan, membolehkan perbualan dihentikan dan disambung semula kemudian.

**Alat** - Anda memberikan alat kepada ejen dengan menyerahkan fungsi Python biasa. Parameter yang dianotasi secara jenis secara automatik ditukar menjadi skema, jadi model tahu cara dan bila untuk memanggilnya (pemanggilan fungsi). Rangka kerja juga menyokong pelayan Model Context Protocol (MCP) dan alat yang dihoskan seperti penafsir kod.

Berikut adalah contoh ejen tunggal dengan alat khusus:

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

Untuk menyambung ke Azure OpenAI dalam Microsoft Foundry, berikan titik akhir dan kelayakan anda kepada klien:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Aliran kerja multi-ejen

Di mana rangka kerja ini benar-benar menonjol adalah mengorkestrakan beberapa ejen bersama-sama. Sebagai contoh, anda boleh menjalankan ejen satu demi satu (setiap satu menyerahkan konteksnya kepada yang berikut) atau mengagihkan ke beberapa ejen secara selari dan mengagregatkan hasil mereka:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Jalankan ejen secara berurutan, sambil meneruskan konteks perbualan sepanjang rantai
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Sebarkan kepada ejen secara selari, kemudian gabungkan respons mereka
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Untuk memasang rangka kerja dan bermula:

```bash
pip install agent-framework-core
# Integrasi pilihan
pip install agent-framework-openai       # OpenAI dan Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Anda boleh meneroka lebih lanjut di [repositori Microsoft Agent Framework](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) dan [dokumentasi rasmi](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Rangka kerja ejen seterusnya yang akan kita terokai ialah [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Ia dikenali sebagai ejen "berkod dahulu" kerana bukannya hanya bekerja dengan `strings`, ia boleh bekerja dengan DataFrames dalam Python. Ini sangat berguna untuk tugas analisis data dan penjanaan. Ini boleh menjadi seperti membuat graf dan carta atau menjana nombor rawak.

### Keadaan dan Alat

Untuk mengurus keadaan perbualan, TaskWeaver menggunakan konsep `Planner`. `Planner` adalah LLM yang mengambil permintaan dari pengguna dan merancang tugasan yang perlu diselesaikan untuk memenuhi permintaan ini.

Untuk melaksanakan tugasan itu, `Planner` diberi akses kepada koleksi alat yang dipanggil `Plugins`. Ini boleh menjadi kelas Python atau penafsir kod umum. Plugin ini disimpan sebagai embedding supaya LLM dapat mencari plugin yang betul dengan lebih baik.

![Taskweaver](../../../translated_images/ms/taskweaver.da8559999267715a.webp)

Berikut adalah contoh plugin untuk mengendalikan pengesanan anomali:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Kod ini disahkan sebelum dilaksanakan. Satu lagi ciri untuk mengurus konteks dalam Taskweaver adalah `experience`. Experience membolehkan konteks perbualan disimpan dalam jangka masa panjang dalam fail YAML. Ini boleh dikonfigurasikan supaya LLM bertambah baik dari masa ke masa pada tugas tertentu dengan pendedahan kepada perbualan lalu.

## JARVIS

Rangka kerja ejen terakhir yang akan kita terokai adalah [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Apa yang menjadikan JARVIS unik ialah ia menggunakan LLM untuk mengurus `keadaan` perbualan dan `alat`nya adalah model AI lain. Setiap model AI adalah model khusus yang menjalankan tugasan tertentu seperti pengesanan objek, transkripsi atau keterangan imej.

![JARVIS](../../../translated_images/ms/jarvis.762ddbadbd1a3a33.webp)

LLM, sebagai model tujuan umum, menerima permintaan dari pengguna dan mengenal pasti tugasan khusus dan sebarang argumen/data yang diperlukan untuk menyelesaikan tugasan tersebut.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM kemudian memformat permintaan dalam cara yang boleh ditafsir oleh model AI khusus, seperti JSON. Setelah model AI mengembalikan ramalannya berdasarkan tugasan, LLM menerima tindak balas tersebut.

Jika beberapa model diperlukan untuk melaksanakan tugasan itu, ia juga akan mentafsirkan tindak balas daripada model-model tersebut sebelum menyatukannya untuk menghasilkan tindak balas kepada pengguna.

Contoh di bawah menunjukkan bagaimana ini berfungsi apabila pengguna meminta penerangan dan kiraan objek dalam gambar:

## Tugasan

Untuk meneruskan pembelajaran anda tentang Ejen AI anda boleh membina dengan Microsoft Agent Framework:

- Sebuah aplikasi yang mensimulasikan mesyuarat perniagaan dengan jabatan-jabatan berbeza dalam sebuah startup pendidikan.
- Buat mesej sistem yang membimbing LLM untuk memahami persona dan keutamaan berbeza, dan membolehkan pengguna memberi cadangan idea produk baru.
- LLM kemudian harus menjana soalan susulan dari setiap jabatan untuk memperbaiki dan menambah baik cadangan dan idea produk

## Pembelajaran tidak terhenti di sini, teruskan Perjalanan

Selepas menyelesaikan pelajaran ini, lihat [koleksi Pembelajaran AI Generatif kami](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk terus meningkatkan pengetahuan AI Generatif anda!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->