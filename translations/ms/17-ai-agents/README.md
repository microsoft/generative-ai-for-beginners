[![Model Sumber Terbuka](../../../translated_images/ms/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Pengenalan

Ejen AI mewakili perkembangan menarik dalam AI Generatif, membolehkan Model Bahasa Besar (LLM) berkembang daripada pembantu kepada ejen yang mampu mengambil tindakan. Rangka kerja Ejen AI membolehkan pembangun mencipta aplikasi yang memberi LLM akses kepada alat dan pengurusan keadaan. Rangka kerja ini juga meningkatkan keterlihatan, membolehkan pengguna dan pembangun memantau tindakan yang dirancang oleh LLM, sekali gus memperbaiki pengurusan pengalaman.

Pelajaran ini akan meliputi bidang berikut:

- Memahami apa itu Ejen AI - Apakah sebenarnya Ejen AI?
- Meneroka lima Rangka Kerja Ejen AI yang berbeza - Apa yang menjadikannya unik?
- Menerapkan Ejen AI ini ke pelbagai kes penggunaan - Bilakah kita perlu menggunakan Ejen AI?

## Matlamat pembelajaran

Selepas mengikuti pelajaran ini, anda akan dapat:

- Jelaskan apa itu Ejen AI dan bagaimana ia boleh digunakan.
- Memahami perbezaan antara beberapa Rangka Kerja Ejen AI yang popular, dan bagaimana ia berbeza.
- Memahami bagaimana Ejen AI berfungsi untuk membina aplikasi dengannya.

## Apakah Ejen AI?

Ejen AI adalah bidang yang sangat menarik dalam dunia AI Generatif. Dengan keterujaan ini kadang-kadang terdapat kekeliruan tentang istilah dan aplikasinya. Untuk memudahkan dan merangkumi kebanyakan alat yang merujuk kepada Ejen AI, kami akan menggunakan definisi ini:

Ejen AI membolehkan Model Bahasa Besar (LLM) melaksanakan tugas dengan memberi mereka akses kepada **keadaan** dan **alat**.

![Model Ejen](../../../translated_images/ms/what-agent.21f2893bdfd01e6a.webp)

Mari kita takrifkan istilah-istilah ini:

**Model Bahasa Besar** - Ini adalah model yang dirujuk sepanjang kursus ini seperti GPT-3.5, GPT-4, Llama-2, dan lain-lain.

**Keadaan** - Ini merujuk kepada konteks di mana LLM sedang bekerja. LLM menggunakan konteks tindakan lalu dan konteks semasa, membimbing pembuatan keputusannya untuk tindakan seterusnya. Rangka kerja Ejen AI membolehkan pembangun mengekalkan konteks ini dengan lebih mudah.

**Alat** - Untuk melengkapkan tugas yang diminta pengguna dan yang dirancang oleh LLM, LLM memerlukan akses kepada alat. Contoh alat termasuk pangkalan data, API, aplikasi luar atau bahkan LLM lain!

Definisi ini diharap akan memberikan asas yang baik semasa kita melihat bagaimana ia dilaksanakan. Mari kita teroka beberapa rangka kerja Ejen AI yang berbeza:

## Ejen LangChain

[Ejen LangChain](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) adalah pelaksanaan definisi yang kami berikan di atas.

Untuk mengurus **keadaan**, ia menggunakan fungsi terbina dalam yang dipanggil `AgentExecutor`. Fungsi ini menerima `agent` yang ditakrifkan dan `tools` yang tersedia kepadanya.

`AgentExecutor` juga menyimpan sejarah sembang untuk menyediakan konteks perbualan.

![Ejen Langchain](../../../translated_images/ms/langchain-agents.edcc55b5d5c43716.webp)

LangChain menawarkan [katalog alat](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) yang boleh diimport ke dalam aplikasi anda untuk diakses oleh LLM. Ini dibuat oleh komuniti dan pasukan LangChain.

Anda kemudian boleh mentakrifkan alat ini dan menghantarnya ke `AgentExecutor`.

Keterlihatan adalah aspek penting lain apabila bercakap tentang Ejen AI. Adalah penting bagi pembangun aplikasi untuk memahami alat mana yang digunakan oleh LLM dan mengapa. Untuk itu, pasukan LangChain telah membangunkan LangSmith.

## AutoGen

Rangka kerja Ejen AI seterusnya yang akan kita bincangkan adalah [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). Fokus utama AutoGen adalah perbualan. Ejen adalah kedua-duanya **boleh diajak berbual** dan **boleh disesuaikan**.

**Boleh diajak berbual -** LLM boleh memulakan dan meneruskan perbualan dengan LLM lain untuk menyelesaikan tugas. Ini dilakukan dengan mencipta `AssistantAgents` dan memberi mereka mesej sistem khusus.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Boleh disesuaikan** - Ejen boleh ditakrifkan bukan sahaja sebagai LLM tetapi juga sebagai pengguna atau alat. Sebagai pembangun, anda boleh mentakrifkan `UserProxyAgent` yang bertanggungjawab berinteraksi dengan pengguna untuk maklum balas dalam melaksanakan tugas. Maklum balas ini boleh meneruskan pelaksanaan tugas atau menghentikannya.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Keadaan dan Alat

Untuk menukar dan menguruskan keadaan, Ejen pembantu menjana kod Python untuk menyelesaikan tugas.

Berikut adalah contoh proses:

![AutoGen](../../../translated_images/ms/autogen.dee9a25a45fde584.webp)

#### LLM Ditakrifkan dengan Mesej Sistem

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Mesej sistem ini mengarahkan LLM tertentu ini kepada fungsi yang relevan untuk tugasnya. Ingat, dengan AutoGen anda boleh mempunyai pelbagai AssistantAgents yang ditakrifkan dengan mesej sistem yang berbeza.

#### Perbualan Dimulakan oleh Pengguna

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Mesej daripada user_proxy (Manusia) inilah yang akan memulakan proses Ejen meneroka fungsi yang mungkin perlu dijalankan.

#### Fungsi Dilaksanakan

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Setelah sembang awal diproses, Ejen akan menghantar alat yang dicadangkan untuk dipanggil. Dalam kes ini, ia adalah fungsi yang dipanggil `get_weather`. Bergantung pada konfigurasi anda, fungsi ini boleh dijalankan secara automatik dan dibaca oleh Ejen atau boleh dilaksanakan berdasarkan input pengguna.

Anda boleh menemui senarai [contoh kod AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) untuk meneroka lebih lanjut cara memulakan pembinaan.

## Rangka Kerja Ejen Microsoft

[Rangka Kerja Ejen Microsoft](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) adalah SDK sumber terbuka Microsoft untuk membina Ejen AI dan sistem multi-ejen dalam **Python** dan **.NET**. Ia menggabungkan kekuatan dua projek Microsoft terdahulu — ciri perusahaan **Semantic Kernel** dan orkestrasi multi-ejen **AutoGen** — ke dalam satu rangka kerja yang disokong. Jika anda memulakan projek ejen baru hari ini, ini adalah pengganti yang disyorkan kepada AutoGen.

Rangka kerja ini berskala dari **ejen sembang** tunggal hingga ke **aliran kerja multi-ejen** yang kompleks, dan ia berintegrasi terus dengan Microsoft Foundry, Azure OpenAI, dan OpenAI. Ia juga menyediakan pengawasan terbina dalam melalui OpenTelemetry supaya anda boleh mengesan dengan tepat apa yang ejen anda lakukan.

### Keadaan dan Alat

**Keadaan** - Rangka kerja mengurus konteks perbualan untuk anda melalui **benang**. Ejen menyimpan sejarah mesej (permintaan pengguna, panggilan alat, dan hasilnya), jadi setiap giliran membina berdasarkan giliran sebelumnya. Benang juga boleh disimpan, membolehkan perbualan dijeda dan disambung semula kemudian.

**Alat** - Anda memberikan alat kepada ejen dengan menghantar fungsi Python biasa. Parameter yang diberi anotasi jenis secara automatik diubah menjadi skema, supaya model tahu bagaimana dan bila memanggilnya (panggilan fungsi). Rangka kerja juga menyokong pelayan Model Context Protocol (MCP) dan alat hos seperti penafsir kod.

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

Untuk sambung ke Azure OpenAI dalam Microsoft Foundry sebaliknya, hantar titik akhir dan kelayakan anda ke klien:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Aliran kerja multi-ejen

Di mana rangka kerja benar-benar menonjol adalah dalam mengorkestrakan beberapa ejen bersama-sama. Sebagai contoh, anda boleh menjalankan ejen satu demi satu (setiap satu menghantar konteksnya ke ejen berikutnya) atau mengarahkan ke beberapa ejen secara selari dan menggabungkan hasil mereka:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Jalankan ejen secara berurutan, menghantar konteks perbualan sepanjang rantaian
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Sebarkan kepada ejen secara selari, kemudian gabungkan respons mereka
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Untuk memasang rangka kerja dan memulakan:

```bash
pip install agent-framework-core
# Integrasi pilihan
pip install agent-framework-openai       # OpenAI dan Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Anda boleh meneroka lebih lanjut di [repositori Rangka Kerja Ejen Microsoft](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) dan [dokumentasi rasmi](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

Rangka kerja ejen seterusnya yang akan kita teroka adalah [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Ia dikenali sebagai ejen "kod-pertama" kerana ia boleh menggunakan DataFrame dalam Python dan bukan hanya bekerja dengan `strings`. Ini menjadi sangat berguna untuk tugas analisis dan penjanaan data. Contohnya seperti mencipta graf dan carta atau menjana nombor rawak.

### Keadaan dan Alat

Untuk menguruskan keadaan perbualan, TaskWeaver menggunakan konsep `Planner`. `Planner` adalah LLM yang menerima permintaan dari pengguna dan memetakan tugas yang perlu diselesaikan untuk memenuhi permintaan ini.

Untuk melengkapkan tugas, `Planner` diberi akses kepada koleksi alat yang dipanggil `Plugins`. Ini boleh berupa kelas Python atau penafsir kod umum. Plugin ini disimpan sebagai embeddings supaya LLM dapat mencari plugin yang betul dengan lebih baik.

![Taskweaver](../../../translated_images/ms/taskweaver.da8559999267715a.webp)

Berikut adalah contoh plugin untuk mengendalikan pengesanan anomali:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

Kod disahkan sebelum dilaksanakan. Satu lagi ciri untuk mengurus konteks dalam Taskweaver ialah `experience`. Experience membolehkan konteks perbualan disimpan dalam jangka masa panjang dalam fail YAML. Ini boleh dikonfigurasikan supaya LLM bertambah baik dari masa ke masa pada tugas tertentu dengan pendedahan kepada perbualan sebelum ini.

## JARVIS

Rangka kerja ejen terakhir yang akan kita teroka adalah [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Apa yang membuatkan JARVIS unik ialah ia menggunakan LLM untuk mengurus `keadaan` perbualan dan `alat` adalah model AI lain. Setiap model AI adalah model khusus yang melakukan tugas tertentu seperti pengesanan objek, transkripsi atau keterangan imej.

![JARVIS](../../../translated_images/ms/jarvis.762ddbadbd1a3a33.webp)

LLM, sebagai model tujuan umum, menerima permintaan dari pengguna dan mengenal pasti tugas khusus dan apa-apa argumen/data yang diperlukan untuk melengkapkan tugas.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

LLM kemudian memformat permintaan dalam cara yang boleh ditafsir oleh model AI khusus, seperti JSON. Setelah model AI mengembalikan ramalannya berdasarkan tugas, LLM menerima respons.

Jika beberapa model diperlukan untuk melengkapkan tugas, ia juga akan mentafsir respons dari model-model tersebut sebelum menggabungkannya untuk menjana respons kepada pengguna.

Contoh di bawah menunjukkan bagaimana ini berfungsi apabila pengguna meminta penerangan dan kiraan objek dalam gambar:

## Tugasan

Untuk meneruskan pembelajaran mengenai Ejen AI, anda boleh membina dengan Rangka Kerja Ejen Microsoft:

- Satu aplikasi yang mensimulasikan mesyuarat perniagaan dengan pelbagai jabatan sebuah startup pendidikan.
- Cipta mesej sistem yang membimbing LLM memahami persona dan keutamaan yang berbeza, dan membolehkan pengguna membentangkan idea produk baru.
- LLM kemudian harus menjana soalan susulan dari setiap jabatan untuk memperhalusi dan memperbaiki pembentangan dan idea produk.

## Pembelajaran tidak berhenti di sini, teruskan Perjalanan

Selepas melengkapkan pelajaran ini, lihat koleksi [Pembelajaran AI Generatif kami](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk terus meningkatkan pengetahuan AI Generatif anda!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->