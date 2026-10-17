# Pengenalan kepada Model Bahasa Kecil untuk AI Generatif bagi Pemula
AI generatif adalah bidang kecerdasan buatan yang menarik yang memfokuskan pada penciptaan sistem yang mampu menghasilkan kandungan baru. Kandungan ini boleh merangkumi teks dan imej hingga muzik dan bahkan persekitaran maya sepenuhnya. Salah satu aplikasi paling menarik AI generatif adalah dalam bidang model bahasa.

## Apakah Model Bahasa Kecil?

Model Bahasa Kecil (SLM) adalah varian skala kecil bagi model bahasa besar (LLM), menggunakan banyak prinsip dan teknik seni bina LLM, sambil menunjukkan jejak pengiraan yang jauh lebih rendah.

SLM adalah subset model bahasa yang direka untuk menghasilkan teks yang menyerupai manusia. Berbeza daripada model besar seperti GPT-4, SLM lebih padat dan cekap, menjadikannya sesuai untuk aplikasi dengan sumber pengiraan yang terhad. Walaupun saiznya lebih kecil, SLM masih boleh melaksanakan pelbagai tugas. Biasanya, SLM dibina dengan memampatkan atau mentah LLM, bertujuan untuk mengekalkan sebahagian besar fungsi dan keupayaan bahasa model asal. Pengurangan saiz model ini mengurangkan kerumitan keseluruhan, menjadikan SLM lebih cekap dari segi penggunaan memori dan keperluan pengiraan. Walaupun dengan pengoptimuman ini, SLM masih boleh menjalankan pelbagai tugas pemprosesan bahasa semula jadi (NLP):

- Penjanaan Teks: Mencipta ayat atau perenggan yang koheren dan relevan dengan konteks.
- Penyempurnaan Teks: Meramalkan dan melengkapkan ayat berdasarkan prompt yang diberikan.
- Terjemahan: Menukar teks dari satu bahasa ke bahasa lain.
- Merumuskan: Memadatkan teks panjang menjadi ringkasan yang lebih pendek dan mudah difahami.

Walaupun dengan beberapa kompromi dalam prestasi atau tahap pemahaman berbanding dengan model besar.

## Bagaimana Model Bahasa Kecil Berfungsi?
SLM dilatih dengan sejumlah besar data teks. Semasa latihan, ia belajar pola dan struktur bahasa, membolehkannya menghasilkan teks yang betul dari segi tatabahasa dan sesuai dengan konteks. Proses latihan melibatkan:

- Pengumpulan Data: Mengumpul set data teks yang besar dari pelbagai sumber.
- Pra-pemprosesan: Membersihkan dan menyusun data supaya sesuai untuk latihan.
- Latihan: Menggunakan algoritma pembelajaran mesin untuk mengajar model memahami dan menghasilkan teks.
- Penalaan Halus: Melaraskan model untuk meningkatkan prestasi dalam tugas tertentu.

Pembangunan SLM sejajar dengan keperluan yang meningkat untuk model yang boleh digunakan dalam persekitaran yang terhad sumber, seperti peranti mudah alih atau platform pengkomputeran tepi, di mana LLM berskala penuh mungkin tidak praktikal kerana permintaan sumber yang tinggi. Dengan memberi tumpuan kepada kecekapan, SLM mengimbangi prestasi dengan kebolehcapaian, membolehkan penggunaan yang lebih meluas dalam pelbagai bidang.

![slm](../../../translated_images/ms/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Objektif Pembelajaran

Dalam pelajaran ini, kami berharap dapat memperkenalkan pengetahuan tentang SLM dan menggabungkannya dengan Microsoft Phi-3 untuk mempelajari senario berbeza dalam kandungan teks, visi dan MoE.

Menjelang akhir pelajaran ini, anda sepatutnya dapat menjawab soalan berikut:

- Apakah itu SLM?
- Apakah perbezaan antara SLM dan LLM?
- Apakah Keluarga Microsoft Phi-3/3.5?
- Bagaimana menjalankan inferens dengan Keluarga Microsoft Phi-3/3.5?

Bersedia? Mari kita mulakan.

## Perbezaan antara Model Bahasa Besar (LLM) dan Model Bahasa Kecil (SLM)

Kedua-dua LLM dan SLM dibina berdasarkan prinsip asas pembelajaran mesin probabilistik, mengikuti pendekatan yang serupa dalam reka bentuk seni bina, metodologi latihan, proses penjanaan data, dan teknik penilaian model. Namun, ada beberapa faktor utama yang membezakan kedua-dua jenis model ini.

## Aplikasi Model Bahasa Kecil

SLM mempunyai pelbagai aplikasi, termasuk:

- Chatbot: Memberi sokongan pelanggan dan berinteraksi dengan pengguna secara perbualan.
- Penciptaan Kandungan: Membantu penulis dengan menghasilkan idea atau bahkan menulis draf artikel lengkap.
- Pendidikan: Membantu pelajar dengan tugasan penulisan atau pembelajaran bahasa baharu.
- Kebolehcapaian: Mencipta alat untuk individu kurang upaya, seperti sistem teks-ke-ucapan.

**Saiz**
  
Perbezaan utama antara LLM dan SLM terletak pada skala model. LLM seperti ChatGPT (GPT-4), boleh mengandungi anggaran 1.76 trilion parameter, manakala SLM sumber terbuka seperti Mistral 7B direka dengan parameter yang jauh lebih sedikit — kira-kira 7 bilion. Perbezaan ini terutamanya disebabkan oleh perbezaan dalam seni bina model dan proses latihan. Contohnya, ChatGPT menggunakan mekanisme perhatian kendiri dalam rangka kerja pengkode-pengekod, manakala Mistral 7B menggunakan perhatian tingkap gelongsor, yang membolehkan latihan lebih cekap dalam model pengekod sahaja. Variasi seni bina ini mempunyai implikasi mendalam terhadap kerumitan dan prestasi model-model ini.

**Pemahaman**

SLM biasanya dioptimumkan untuk prestasi dalam domain tertentu, menjadikannya sangat pakar tetapi mungkin terhad dalam keupayaan untuk memberikan pemahaman konteks luas merentas pelbagai bidang ilmu. Sebaliknya, LLM bertujuan mensimulasikan kecerdasan mirip manusia pada tahap yang lebih menyeluruh. Dilatih dengan set data besar dan pelbagai, LLM direka untuk berprestasi baik dalam pelbagai domain, menawarkan kepelbagaian dan penyesuaian yang lebih tinggi. Oleh itu, LLM lebih sesuai untuk pelbagai tugas hiliran, seperti pemprosesan bahasa semula jadi dan pengaturcaraan.

**Pengkomputeran**

Latihan dan penggunaan LLM adalah proses yang menggunakan sumber yang tinggi, sering memerlukan infrastruktur pengkomputeran yang besar, termasuk kluster GPU skala besar. Contohnya, melatih model seperti ChatGPT dari awal mungkin memerlukan ribuan GPU selama tempoh yang panjang. Sebaliknya, SLM dengan bilangan parameter yang lebih kecil lebih mudah diakses dari segi sumber pengkomputeran. Model seperti Mistral 7B boleh dilatih dan dijalankan pada mesin tempatan yang dilengkapi dengan kemampuan GPU sederhana, walaupun latihannya masih memerlukan beberapa jam menggunakan pelbagai GPU.

**Bias**

Bias adalah isu yang diketahui dalam LLM, terutamanya disebabkan oleh sifat data latihan. Model ini sering bergantung pada data mentah yang tersedia secara terbuka di internet, yang mungkin kurang mewakili atau salah mewakili kumpulan tertentu, memperkenalkan pelabelan yang salah, atau memaparkan bias linguistik yang dipengaruhi oleh dialek, variasi geografi, dan peraturan tatabahasa. Tambahan pula, kerumitan seni bina LLM boleh dengan tidak sengaja memburukkan bias, yang mungkin tidak disedari tanpa penalaan halus yang berhati-hati. Sebaliknya, SLM yang dilatih dengan set data domain yang lebih terhad biasanya kurang terdedah kepada bias sedemikian, walaupun tidak kebal daripadanya.

**Inferens**

Saiz SLM yang lebih kecil memberikan kelebihan ketara dari segi kelajuan inferens, membolehkan ia menghasilkan output dengan cekap pada perkakasan tempatan tanpa memerlukan pemprosesan selari yang meluas. Sebaliknya, LLM, disebabkan saiz dan kerumitannya, sering memerlukan sumber pengiraan selari yang besar untuk mencapai masa inferens yang boleh diterima. Kehadiran pengguna serentak yang ramai juga melambatkan masa respons LLM, terutama apabila digunakan secara besar-besaran.

Ringkasnya, walaupun LLM dan SLM berkongsi asas pembelajaran mesin, mereka berbeza dengan ketara dari segi saiz model, keperluan sumber, pemahaman konteks, keterdedahan kepada bias, dan kelajuan inferens. Perbezaan ini mencerminkan kesesuaian masing-masing untuk kegunaan berbeza, dengan LLM lebih serba boleh tetapi menggunakan banyak sumber, dan SLM menawarkan kecekapan khusus domain dengan keperluan pengiraan yang dikurangkan.

***Nota: Dalam pelajaran ini, kami akan memperkenalkan SLM menggunakan Microsoft Phi-3 / 3.5 sebagai contoh.***

## Pengenalan Keluarga Phi-3 / Phi-3.5

Keluarga Phi-3 / 3.5 terutamanya menyasarkan senario aplikasi teks, visi, dan Agen (MoE):

### Phi-3 / 3.5 Instruct

Terutamanya untuk penjanaan teks, penyempurnaan perbualan, dan ekstraksi maklumat kandungan, dan lain-lain.

**Phi-3-mini**

Model bahasa 3.8B tersedia di Microsoft Foundry, Hugging Face, dan Ollama. Model Phi-3 mengatasi model bahasa dengan saiz sama dan lebih besar dalam penanda aras utama (lihat nombor penanda aras di bawah, nombor lebih tinggi adalah lebih baik). Phi-3-mini mengatasi model dua kali ganda saiznya, manakala Phi-3-small dan Phi-3-medium mengatasi model yang lebih besar, termasuk GPT-3.5.

**Phi-3-small & medium**

Dengan hanya 7B parameter, Phi-3-small mengatasi GPT-3.5T dalam pelbagai penanda aras bahasa, penaakulan, pengaturcaraan, dan matematik.

Phi-3-medium dengan 14B parameter meneruskan trend ini dan mengatasi Gemini 1.0 Pro.

**Phi-3.5-mini**

Kita boleh anggap ia sebagai peningkatan Phi-3-mini. Walaupun bilangan parameter tidak berubah, ia meningkatkan sokongan untuk pelbagai bahasa (menyokong 20+ bahasa: Arab, Cina, Czech, Denmark, Belanda, Inggeris, Finland, Perancis, Jerman, Ibrani, Hungary, Itali, Jepun, Korea, Norway, Poland, Portugis, Rusia, Sepanyol, Sweden, Thai, Turki, Ukraine) dan menambah sokongan lebih kukuh untuk konteks panjang.

Phi-3.5-mini dengan 3.8B parameter mengatasi model bahasa dengan saiz yang sama dan setaraf dengan model dua kali ganda saiznya.

### Phi-3 / 3.5 Vision

Kita boleh anggap model Instruct Phi-3/3.5 sebagai kebolehan Phi untuk memahami, dan Vision adalah apa yang memberi "mata" kepada Phi untuk memahami dunia.


**Phi-3-Vision**

Phi-3-vision, dengan hanya 4.2B parameter, meneruskan trend ini dan mengatasi model yang lebih besar seperti Claude-3 Haiku dan Gemini 1.0 Pro V dalam tugas penaakulan visual umum, OCR, dan pemahaman jadual serta rajah.


**Phi-3.5-Vision**

Phi-3.5-Vision juga adalah peningkatan daripada Phi-3-Vision, menambah sokongan untuk berbilang imej. Anda boleh menganggapnya sebagai peningkatan dalam visi, bukan sahaja boleh melihat gambar, tetapi juga video.

Phi-3.5-vision mengatasi model lebih besar seperti Claude-3.5 Sonnet dan Gemini 1.5 Flash merentas tugas OCR, pemahaman jadual dan carta, dan setaraf dalam tugas penaakulan pengetahuan visual umum. Menyokong input berbilang bingkai, iaitu membuat penaakulan pada pelbagai input imej.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** membolehkan model dilatih dahulu dengan penggunaan pengiraan yang jauh lebih rendah, yang bermaksud anda boleh meningkatkan saiz model atau set data secara dramatik dengan bajet pengiraan yang sama seperti model padat. Secara khusus, model MoE sepatutnya mencapai kualiti yang sama dengan padanannya yang padat dengan lebih cepat semasa pralatihan.

Phi-3.5-MoE terdiri daripada 16 modul pakar 3.8B. Phi-3.5-MoE dengan hanya 6.6B parameter aktif mencapai tahap penaakulan, kefahaman bahasa, dan matematik yang serupa dengan model yang jauh lebih besar.

Kita boleh menggunakan model Keluarga Phi-3/3.5 berdasarkan senario berbeza. Berbeza dengan LLM, anda boleh melaksanakan Phi-3/3.5-mini atau Phi-3/3.5-Vision pada peranti edge.


## Cara menggunakan model Keluarga Phi-3/3.5

Kami berharap untuk menggunakan Phi-3/3.5 dalam pelbagai senario. Seterusnya, kita akan menggunakan Phi-3/3.5 berdasarkan senario berbeza.

![phi3](../../../translated_images/ms/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferens melalui API Awan

**Model Microsoft Foundry**

> **Nota:** Model GitHub akan dihentikan pada akhir Julai 2026. [Model Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) adalah pengganti langsung.

Model Microsoft Foundry adalah cara paling langsung. Anda boleh dengan cepat mengakses model Phi-3/3.5-Instruct melalui katalog model Foundry. Digabungkan dengan Azure AI Inference SDK / OpenAI SDK, anda boleh mengakses API melalui kod untuk melengkapkan panggilan Phi-3/3.5-Instruct. Anda juga boleh menguji kesan berbeza melalui Playground.

- Demo: Perbandingan kesan Phi-3-mini dan Phi-3.5-mini dalam senario bahasa Cina

![phi3](../../../translated_images/ms/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/ms/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Jika ingin menggunakan model visi dan MoE, anda boleh menggunakan Microsoft Foundry untuk melengkapkan panggilan tersebut. Jika berminat, anda boleh membaca Buku Resepi Phi-3 untuk mengetahui cara memanggil Phi-3/3.5 Instruct, Vision, MoE melalui Microsoft Foundry [Klik pautan ini](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Selain katalog Model Microsoft Foundry yang berasaskan awan, anda juga boleh menggunakan [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) untuk melengkapkan panggilan berkaitan. Anda boleh melawat NVIDIA NIM untuk membuat panggilan API bagi Keluarga Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) adalah satu set mikroservis inferens dipercepat yang direka untuk membantu pembangun melaksanakan model AI dengan cekap merentas pelbagai persekitaran, termasuk awan, pusat data, dan stesen kerja.

Berikut adalah beberapa ciri utama NVIDIA NIM:

- **Kemudahan Pelaksanaan:** NIM membolehkan pelaksanaan model AI dengan satu arahan, memudahkan integrasi ke dalam aliran kerja sedia ada.
- **Prestasi Dioptimumkan:** Ia menggunakan enjin inferens yang telah dioptimumkan NVIDIA, seperti TensorRT dan TensorRT-LLM, untuk memastikan kelewatan rendah dan kelajuan tinggi.
- **Skalabiliti:** NIM menyokong auto-skala pada Kubernetes, membolehkan pengendalian beban kerja yang berubah-ubah dengan berkesan.
- **Keselamatan dan Kawalan:** Organisasi boleh mengekalkan kawalan ke atas data dan aplikasi mereka dengan menghoskan sendiri mikroservis NIM pada infrastruktur mereka yang diuruskan.
- **API Standard:** NIM menyediakan API standard industri, memudahkan untuk membina dan mengintegrasikan aplikasi AI seperti chatbot, pembantu AI, dan banyak lagi.

NIM adalah sebahagian daripada NVIDIA AI Enterprise, yang bertujuan untuk mempermudah pengoperasian dan pelaksanaan model AI, memastikan mereka berjalan dengan cekap pada GPU NVIDIA.

- Demo: Menggunakan NVIDIA NIM untuk memanggil Phi-3.5-Vision-API  [[Klik pautan ini](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Menjalankan Phi-3/3.5 secara Tempatan
Inferens berkaitan dengan Phi-3, atau mana-mana model bahasa seperti GPT-3, merujuk kepada proses menghasilkan respons atau ramalan berdasarkan input yang diterimanya. Apabila anda memberikan prompt atau soalan kepada Phi-3, ia menggunakan rangkaian neural yang telah dilatih untuk meneka respons yang paling mungkin dan relevan dengan menganalisa corak dan hubungan dalam data yang telah dilatih.

**Hugging Face Transformer**
Hugging Face Transformers adalah perpustakaan yang kuat direka untuk pemprosesan bahasa semula jadi (NLP) dan tugas-tugas pembelajaran mesin lain. Berikut adalah beberapa perkara utama mengenainya:

1. **Model Pralatih**: Ia menyediakan beribu-ribu model pralatih yang boleh digunakan untuk pelbagai tugas seperti klasifikasi teks, pengecaman entiti bernama, menjawab soalan, meringkaskan, terjemahan, dan penjanaan teks.

2. **Kebolehoperasian Rangka Kerja:** Perpustakaan ini menyokong pelbagai rangka kerja pembelajaran mendalam, termasuk PyTorch, TensorFlow, dan JAX. Ini membolehkan anda melatih model dalam satu rangka kerja dan menggunakannya dalam rangka kerja lain.

3. **Keupayaan Multimodal:** Selain NLP, Hugging Face Transformers juga menyokong tugas dalam penglihatan komputer (contoh: klasifikasi imej, pengesanan objek) dan pemprosesan audio (contoh: pengecaman suara, klasifikasi audio).

4. **Mudah Digunakan:** Perpustakaan ini menawarkan API dan alat untuk memuat turun dan melaras model dengan mudah, menjadikannya mudah diakses untuk pemula dan pakar.

5. **Komuniti dan Sumber:** Hugging Face mempunyai komuniti yang aktif dan dokumentasi yang luas, tutorial, serta panduan untuk membantu pengguna memulakan dan memanfaatkannya sepenuhnya.
[dokumentasi rasmi](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) atau repositori [GitHub mereka](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Ini adalah kaedah yang paling biasa digunakan, tetapi ia juga memerlukan pecutan GPU. Lagipun, senario seperti Vision dan MoE memerlukan banyak pengiraan, yang akan menjadi sangat perlahan pada CPU jika mereka tidak dikuantakan.


- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-Instruct [Klik pautan ini](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-Vision [Klik pautan ini](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-MoE [Klik pautan ini](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) adalah platform yang direka untuk memudahkan menjalankan model bahasa besar (LLM) secara tempatan pada mesin anda. Ia menyokong pelbagai model seperti Llama 3.1, Phi 3, Mistral, dan Gemma 2, antara lain. Platform ini mempermudah proses dengan menggabungkan berat model, konfigurasi, dan data ke dalam satu pakej, menjadikannya lebih mudah untuk pengguna menyesuaikan dan mencipta model mereka sendiri. Ollama tersedia untuk macOS, Linux, dan Windows. Ia adalah alat yang hebat jika anda ingin mencuba atau melaksanakan LLM tanpa bergantung pada perkhidmatan awan. Ollama adalah cara paling langsung, anda hanya perlu melaksanakan arahan berikut.


```bash

ollama run phi3.5

```

**Foundry Tempatan**

[Foundry Tempatan](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ialah runtime luar talian milik Microsoft yang berjalan pada peranti anda untuk menjalankan model seperti Phi sepenuhnya pada perkakasan anda sendiri - tanpa langganan Azure, kunci API, atau sambungan rangkaian diperlukan. Ia secara automatik memilih penyedia pelaksanaan terbaik yang tersedia (NPU, GPU, atau CPU) dan menyediakan titik akhir yang serasi dengan OpenAI, supaya kod `openai`/Azure AI Inference SDK sedia ada boleh menggunakan dengan perubahan minimum. Lihat [dokumentasi Foundry Tempatan](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) untuk bermula.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Atau gunakan SDK terus dalam Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime untuk GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) adalah pemecut inferens dan latihan pembelajaran mesin pelbagai platform. ONNX Runtime untuk Generative AI (GENAI) adalah alat yang kuat yang membantu anda menjalankan model AI generatif dengan cekap merentasi pelbagai platform.

## Apakah ONNX Runtime?
ONNX Runtime adalah projek sumber terbuka yang membolehkan inferens prestasi tinggi model pembelajaran mesin. Ia menyokong model dalam format Open Neural Network Exchange (ONNX), yang merupakan standard untuk mewakili model pembelajaran mesin. Inferens ONNX Runtime dapat mempercepat pengalaman pengguna dan mengurangkan kos, menyokong model daripada rangka kerja pembelajaran mendalam seperti PyTorch dan TensorFlow/Keras serta perpustakaan pembelajaran mesin klasik seperti scikit-learn, LightGBM, XGBoost, dll. ONNX Runtime serasi dengan perkakasan, pemandu, dan sistem pengendalian yang berlainan, serta menyediakan prestasi optimal dengan memanfaatkan pemecut perkakasan apabila sesuai berserta pengoptimuman dan transformasi grafik.

## Apakah AI Generatif?
AI Generatif merujuk kepada sistem AI yang dapat menghasilkan kandungan baru, seperti teks, imej, atau muzik, berdasarkan data yang telah dilatih. Contoh termasuk model bahasa seperti GPT-3 dan model penjanaan imej seperti Stable Diffusion. Perpustakaan ONNX Runtime untuk GenAI menyediakan loop AI generatif untuk model ONNX, termasuk inferens dengan ONNX Runtime, pemprosesan logits, carian dan pensampelan, serta pengurusan cache KV.

## ONNX Runtime untuk GENAI
ONNX Runtime untuk GENAI meluaskan kemampuan ONNX Runtime untuk menyokong model AI generatif. Berikut adalah beberapa ciri utama:

- **Sokongan Platform Luas:** Ia berfungsi pada pelbagai platform, termasuk Windows, Linux, macOS, Android, dan iOS.
- **Sokongan Model:** Ia menyokong banyak model generatif AI popular, seperti LLaMA, GPT-Neo, BLOOM, dan lainnya.
- **Pengoptimuman Prestasi:** Termasuk pengoptimuman untuk pelbagai pemecut perkakasan seperti GPU NVIDIA, GPU AMD, dan lagi2.
- **Mudah Digunakan:** Menyediakan API untuk integrasi mudah ke dalam aplikasi, membolehkan anda menghasilkan teks, imej, dan kandungan lain dengan sedikit kod.
- Pengguna boleh memanggil kaedah generate() berperingkat tinggi, atau menjalankan setiap iterasi model dalam gelung, menghasilkan satu token pada satu masa, dan secara pilihan mengemas kini parameter penjanaan di dalam gelung.
- ONNX runtime juga menyokong carian tamak/beam dan pensampelan TopP, TopK untuk menghasilkan urutan token dan pemprosesan logits terbina dalam seperti penalti pengulangan. Anda juga boleh menambah skor tersuai dengan mudah.

## Bermula
Untuk bermula dengan ONNX Runtime untuk GENAI, anda boleh ikut langkah berikut:

### Pasang ONNX Runtime:
```Python
pip install onnxruntime
```
### Pasang Sambungan AI Generatif:
```Python
pip install onnxruntime-genai
```

### Jalankan Model: Berikut adalah contoh ringkas dalam Python:
```Python
import onnxruntime_genai as og

model = og.Model('path_to_your_model.onnx')

tokenizer = og.Tokenizer(model)

input_text = "Hello, how are you?"

input_tokens = tokenizer.encode(input_text)

output_tokens = model.generate(input_tokens)

output_text = tokenizer.decode(output_tokens)

print(output_text) 
```
### Demo: Menggunakan ONNX Runtime GenAI untuk memanggil Phi-3.5-Vision


```python

import onnxruntime_genai as og

model_path = './Your Phi-3.5-vision-instruct ONNX Path'

img_path = './Your Image Path'

model = og.Model(model_path)

processor = model.create_multimodal_processor()

tokenizer_stream = processor.create_stream()

text = "Your Prompt"

prompt = "<|user|>\n"

prompt += "<|image_1|>\n"

prompt += f"{text}<|end|>\n"

prompt += "<|assistant|>\n"

image = og.Images.open(img_path)

inputs = processor(prompt, images=image)

params = og.GeneratorParams(model)

params.set_inputs(inputs)

params.set_search_options(max_length=3072)

generator = og.Generator(model, params)

while not generator.is_done():

    generator.compute_logits()
    
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    
    output = tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


**Lain-Lain**

Selain ONNX Runtime, Ollama, dan kaedah rujukan Foundry Tempatan, kita juga boleh melengkapkan rujukan model kuantitatif berdasarkan kaedah rujukan model yang disediakan oleh pengeluar yang berbeza. Seperti rangka kerja Apple MLX dengan Apple Metal, Qualcomm QNN dengan NPU, Intel OpenVINO dengan CPU/GPU, dan lain-lain. Anda juga boleh mendapatkan lebih banyak kandungan dari [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Lebih Lanjut

Kita telah mempelajari asas keluarga Phi-3/3.5, tetapi untuk belajar lebih lanjut tentang SLM kita memerlukan lebih banyak pengetahuan. Anda boleh mencari jawapan dalam Phi-3 Cookbook. Jika anda ingin belajar lebih lanjut, sila lawati [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->