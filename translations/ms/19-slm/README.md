# Pengenalan kepada Model Bahasa Kecil untuk AI Generatif bagi Pemula
AI generatif adalah bidang kecerdasan buatan yang menarik yang memfokuskan pada penciptaan sistem yang mampu menghasilkan kandungan baru. Kandungan ini boleh merangkumi teks dan imej hingga muzik dan persekitaran maya sepenuhnya. Salah satu aplikasi AI generatif yang paling mengujakan adalah dalam bidang model bahasa.

## Apakah Model Bahasa Kecil?

Model Bahasa Kecil (SLM) mewakili varian berskala kecil bagi model bahasa besar (LLM), menggunakan banyak prinsip dan teknik seni bina LLM, sambil menunjukkan jejak pengkomputeran yang jauh lebih kecil. 

SLM adalah subset model bahasa yang direka untuk menjana teks seperti manusia. Tidak seperti yang lebih besar, seperti GPT-4, SLM lebih padat dan cekap, menjadikannya sesuai untuk aplikasi di mana sumber pengkomputeran terhad. Walaupun bersaiz kecil, ia boleh melakukan pelbagai tugas. Biasanya, SLM dibina dengan memampatkan atau memurnikan LLM, bertujuan mengekalkan sebahagian besar fungsi dan kemampuan linguistik model asal. Pengurangan saiz model ini mengurangkan kerumitan keseluruhan, menjadikan SLM lebih cekap dari segi penggunaan memori dan keperluan pengkomputeran. Walaupun dengan pengoptimuman ini, SLM masih boleh melakukan pelbagai tugas pemprosesan bahasa semula jadi (NLP):

- Penjanaan Teks: Mencipta ayat atau perenggan yang koheren dan relevan dengan konteks.
- Lengkapkan Teks: Meramalkan dan melengkapkan ayat berdasarkan petunjuk yang diberikan.
- Terjemahan: Menukar teks dari satu bahasa ke bahasa lain.
- Ringkasan: Memendekkan teks panjang kepada ringkasan yang lebih mudah difahami.

Walaupun dengan beberapa kompromi dalam prestasi atau kedalaman pemahaman berbanding model yang lebih besar.

## Bagaimana Model Bahasa Kecil Berfungsi?
SLM dilatih menggunakan sejumlah besar data teks. Semasa latihan, mereka mempelajari corak dan struktur bahasa, yang membolehkan mereka menghasilkan teks yang betul dari segi tatabahasa dan sesuai dengan konteks. Proses latihan melibatkan:

- Pengumpulan Data: Mengumpul dataset besar teks dari pelbagai sumber.
- Pralepas: Membersih dan mengatur data supaya sesuai untuk latihan.
- Latihan: Menggunakan algoritma pembelajaran mesin untuk mengajar model memahami dan menjana teks.
- Penalaan Halus: Menyesuaikan model untuk meningkatkan prestasi pada tugas tertentu.

Pembangunan SLM sejajar dengan keperluan semakin meningkat bagi model yang boleh digunakan dalam persekitaran dengan sumber terhad, seperti peranti mudah alih atau platform pengkomputeran tepi, di mana LLM berskala penuh mungkin tidak praktikal sebab permintaan sumber yang tinggi. Dengan fokus pada kecekapan, SLM mengimbangi prestasi dengan aksesibiliti, membolehkan aplikasi lebih meluas dalam pelbagai domain.

![slm](../../../translated_images/ms/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Objektif Pembelajaran

Dalam pelajaran ini, kami berharap dapat memperkenalkan pengetahuan tentang SLM dan menggabungkannya dengan Microsoft Phi-3 untuk mempelajari pelbagai senario dalam kandungan teks, penglihatan dan MoE.

Menjelang akhir pelajaran ini, anda seharusnya dapat menjawab soalan berikut:

- Apakah SLM?
- Apakah perbezaan antara SLM dan LLM?
- Apakah Keluarga Microsoft Phi-3/3.5?
- Bagaimana menjalankan inferens dengan Keluarga Microsoft Phi-3/3.5?

Sedia? Mari kita mula.

## Perbezaan antara Model Bahasa Besar (LLMs) dan Model Bahasa Kecil (SLMs)

Kedua-dua LLM dan SLM dibina berdasarkan prinsip asas pembelajaran mesin probabilistik, mengikuti pendekatan serupa dalam reka bentuk seni bina, metodologi latihan, proses penjanaan data, dan teknik penilaian model. Walau bagaimanapun, terdapat beberapa faktor utama yang membezakan kedua-dua jenis model ini.

## Aplikasi Model Bahasa Kecil

SLM mempunyai pelbagai aplikasi, termasuk:

- Chatbot: Menyediakan sokongan pelanggan dan berinteraksi dengan pengguna secara perbualan.
- Penciptaan Kandungan: Membantu penulis dengan menjana idea atau bahkan draf artikel penuh.
- Pendidikan: Membantu pelajar dengan tugasan penulisan atau pembelajaran bahasa baru.
- Aksesibiliti: Mewujudkan alat untuk individu kurang upaya, seperti sistem teks-ke-ucapan.

**Saiz**
  
Perbezaan utama antara LLM dan SLM terletak pada saiz model. LLM seperti ChatGPT (GPT-4) mengandungi anggaran 1.76 trilion parameter, manakala SLM sumber terbuka seperti Mistral 7B direka dengan parameter yang jauh lebih sedikit—kira-kira 7 bilion. Perbezaan ini terutama disebabkan oleh variasi seni bina model dan proses latihan. Contohnya, ChatGPT menggunakan mekanisme perhatian sendiri dalam kerangka pengode-pengode, manakala Mistral 7B menggunakan tumpuan tingkap gelongsor yang membolehkan latihan lebih cekap dalam model pengode sahaja. Variasi seni bina ini mempunyai impak mendalam terhadap kerumitan dan prestasi model-model ini.

**Pemahaman**

SLM biasanya dioptimumkan untuk prestasi dalam domain tertentu, menjadikannya sangat khusus tetapi mungkin terhad dalam keupayaan untuk menyediakan pemahaman konteks luas merentasi pelbagai bidang ilmu. Sebaliknya, LLM bertujuan meniru kecerdasan seperti manusia pada tahap yang lebih menyeluruh. Dilatih pada dataset besar dan pelbagai, LLM direka untuk berprestasi baik dalam pelbagai domain, menawarkan fleksibiliti dan adaptasi yang lebih tinggi. Oleh itu, LLM lebih sesuai untuk pelbagai tugas hiliran seperti pemprosesan bahasa semula jadi dan pengaturcaraan.

**Pengkomputeran**

Latihan dan penerapan LLM adalah proses yang memerlukan sumber besar, selalunya memerlukan infrastruktur pengkomputeran yang signifikan termasuk kluster GPU berskala besar. Contohnya, melatih model seperti ChatGPT dari awal mungkin memerlukan beribu-ribu GPU selama tempoh yang panjang. Sebaliknya, SLM dengan jumlah parameter yang lebih kecil lebih mesra dari segi sumber pengkomputeran. Model seperti Mistral 7B boleh dilatih dan dijalankan pada mesin tempatan dengan keupayaan GPU sederhana, walaupun latihan masih memerlukan beberapa jam merentasi pelbagai GPU.

**Bias**

Bias adalah isu yang diketahui dalam LLM, terutamanya disebabkan sifat data latihan. Model ini selalunya bergantung pada data mentah yang tersedia secara terbuka dari internet, yang mungkin kurang atau salah menggambarkan kumpulan tertentu, memperkenalkan label yang salah, atau mencerminkan bias linguistik yang dipengaruhi oleh dialek, variasi geografi, dan aturan tatabahasa. Selain itu, kompleksiti seni bina LLM boleh secara tidak sengaja memperburuk bias, yang mungkin tidak disedari tanpa penalaan halus yang teliti. Sebaliknya, SLM, yang dilatih pada dataset domain-specific yang lebih terhad, secara semula jadi kurang terdedah kepada bias sebegini, walaupun tidak bebas dari mereka.

**Inferens**

Saiz SLM yang diperkecil memberikan kelebihan ketara dari segi kelajuan inferens, membolehkannya menghasilkan output dengan cekap pada perkakasan tempatan tanpa keperluan pemprosesan selari yang luas. Sebaliknya, LLM, disebabkan saiz dan kerumitannya, sering memerlukan sumber pengkomputeran selari yang besar untuk mencapai masa inferens yang boleh diterima. Kehadiran pengguna serentak yang banyak juga melambatkan masa respons LLM, terutamanya apabila digunakan secara berskala.

Kesimpulannya, walaupun LLM dan SLM berkongsi asas pembelajaran mesin, mereka berbeza secara signifikan dari segi saiz model, keperluan sumber, pemahaman konteks, kecenderungan kepada bias, dan kelajuan inferens. Perbezaan ini mencerminkan kesesuaian masing-masing untuk kegunaan berbeza, di mana LLM lebih serbaguna tetapi berat sumber, dan SLM menawarkan kecekapan domain-spesifik dengan tuntutan pengkomputeran yang dikurangkan.

***Nota: Dalam pelajaran ini, kami akan memperkenalkan SLM menggunakan Microsoft Phi-3 / 3.5 sebagai contoh.***

## Memperkenalkan Keluarga Phi-3 / Phi-3.5

Keluarga Phi-3 / 3.5 menyasarkan terutamanya senario aplikasi teks, penglihatan, dan Ejen (MoE):

### Phi-3 / 3.5 Instruct

Terutamanya untuk penjanaan teks, penyelesaian perbualan, dan pengekstrakan maklumat kandungan, dan lain-lain.

**Phi-3-mini**

Model bahasa 3.8B tersedia di Microsoft Foundry, Hugging Face, dan Ollama. Model Phi-3 mengatasi model bahasa bersaiz sama dan lebih besar secara signifikan dalam penanda aras utama (lihat angka penanda aras di bawah, angka lebih tinggi lebih baik). Phi-3-mini mengatasi model dua kali ganda saiznya, manakala Phi-3-small dan Phi-3-medium mengatasi model yang lebih besar, termasuk GPT-3.5.

**Phi-3-small & medium**

Dengan hanya 7B parameter, Phi-3-small mengalahkan GPT-3.5T dalam pelbagai penanda aras bahasa, penaakulan, pengkodan, dan matematik.

Phi-3-medium dengan 14B parameter meneruskan trend ini dan mengatasi Gemini 1.0 Pro.

**Phi-3.5-mini**

Kita boleh menganggapnya sebagai peningkatan dari Phi-3-mini. Walaupun parameter kekal tidak berubah, ia meningkatkan keupayaan menyokong pelbagai bahasa (menyokong lebih 20 bahasa: Arab, Cina, Czech, Denmark, Belanda, Inggeris, Finland, Perancis, Jerman, Ibrani, Hungary, Itali, Jepun, Korea, Norway, Poland, Portugis, Rusia, Sepanyol, Sweden, Thai, Turki, Ukraine) dan menambah sokongan yang lebih kuat untuk konteks panjang.

Phi-3.5-mini dengan 3.8B parameter mengatasi model bahasa bersaiz sama dan setanding dengan model dua kali ganda saiznya.

### Phi-3 / 3.5 Vision

Kita boleh menganggap model Instruct Phi-3/3.5 sebagai keupayaan Phi untuk memahami, dan Vision adalah apa yang memberi Phi mata untuk memahami dunia.


**Phi-3-Vision**

Phi-3-vision, dengan hanya 4.2B parameter, meneruskan trend ini dan mengatasi model lebih besar seperti Claude-3 Haiku dan Gemini 1.0 Pro V dalam tugas penaakulan visual umum, OCR, dan pemahaman jadual serta diagram.


**Phi-3.5-Vision**

Phi-3.5-Vision juga adalah peningkatan dari Phi-3-Vision, menambah sokongan untuk pelbagai imej. Anda boleh menganggapnya sebagai peningkatan dalam penglihatan, bukan sahaja boleh melihat gambar, tetapi juga video.

Phi-3.5-vision mengatasi model lebih besar seperti Claude-3.5 Sonnet dan Gemini 1.5 Flash dalam tugas OCR, pemahaman jadual dan carta serta setanding dalam tugas penaakulan pengetahuan visual umum. Menyokong input berbingkai pelbagai, iaitu melakukan penaakulan pada pelbagai imej input


### Phi-3.5-MoE

***Campuran Pakar (MoE)*** membolehkan model dilatih untuk masa latihan yang jauh lebih sedikit, bermakna anda boleh skala model atau saiz dataset dengan ketara menggunakan bajet pengkomputeran yang sama seperti model padat. Secara khusus, model MoE sepatutnya mencapai kualiti yang sama dengan model padatnya dengan lebih cepat semasa pra-latihan.

Phi-3.5-MoE terdiri daripada 16 modul pakar 3.8B. Phi-3.5-MoE dengan hanya 6.6B parameter aktif mencapai tahap penaakulan, pemahaman bahasa, dan matematik yang serupa dengan model yang jauh lebih besar

Kita boleh menggunakan model Keluarga Phi-3/3.5 berdasarkan senario berbeza. Tidak seperti LLM, anda boleh menggunakan Phi-3/3.5-mini atau Phi-3/3.5-Vision pada peranti tepi.


## Cara menggunakan model Keluarga Phi-3/3.5

Kami berharap menggunakan Phi-3/3.5 dalam pelbagai senario. Seterusnya, kita akan menggunakan Phi-3/3.5 berdasarkan pelbagai senario.

![phi3](../../../translated_images/ms/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferens melalui Cloud API

**Model Microsoft Foundry**

> **Nota:** Model GitHub akan dihentikan pada akhir Julai 2026. [Model Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) adalah pengganti terusannya.

> **Nota:** Keseluruhan keluarga Phi-3/3.5 (varian Instruct, Vision dan MoE) telah dihentikan dari katalog Model Microsoft Foundry pada 2025-08-30. Gunakan `Phi-4` (Instruct) atau `Phi-4-mini-instruct` sebagai gantian — contoh Phi-3/3.5 di bawah masih berfungsi melalui Hugging Face, Ollama, ONNX Runtime dan NVIDIA NIM.

Model Microsoft Foundry kini menyediakan pengganti Phi-4. Gunakan `Phi-4` atau `Phi-4-mini-instruct` sebagai ganti model Phi-3/3.5 yang telah dihentikan semasa mengikuti contoh API awan.

- Demonstrasi: Perbandingan kesan Phi-3-mini dan Phi-3.5-mini dalam senario bahasa Cina

![phi3](../../../translated_images/ms/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/ms/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Jika anda ingin menggunakan model penglihatan (multimodal) di awan, gunakan `Phi-4-multimodal-instruct` yang tersedia sekarang melalui Microsoft Foundry sebagai ganti model Phi-3/3.5 Vision yang telah dihentikan; untuk tugas teks gunakan `Phi-4` atau `Phi-4-mini-instruct`. Model Phi-3.5 MoE telah dihentikan dari Microsoft Foundry, jadi gunakan pilihan lain yang diterangkan dalam pelajaran ini (contohnya Hugging Face) jika anda ingin mencuba. Jika berminat, anda boleh membaca Buku Masak Phi untuk belajar bagaimana memanggil model Phi melalui Microsoft Foundry [Klik pautan ini](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Selain katalog Model Microsoft Foundry berasaskan awan, anda juga boleh menggunakan [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) untuk melengkapkan panggilan berkaitan. Anda boleh melawat NVIDIA NIM untuk melengkapkan panggilan API keluarga Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) ialah satu set mikroservis inferens dipercepat yang direka untuk membantu pembangun melaksanakan model AI dengan cekap di pelbagai persekitaran, termasuk awan, pusat data dan stesen kerja.

Berikut adalah beberapa ciri utama NVIDIA NIM:

- **Mudah untuk Dideploy:** NIM membolehkan penyebaran model AI dengan satu arahan, menjadikannya mudah untuk diintegrasikan ke dalam aliran kerja sedia ada.
- **Prestasi Teroptimum:** Ia menggunakan enjin inferens yang telah dioptimumkan oleh NVIDIA, seperti TensorRT dan TensorRT-LLM, untuk memastikan latensi rendah dan keluaran tinggi.
- **Kebolehsuaian:** NIM menyokong autoscaling pada Kubernetes, membolehkannya mengendalikan beban kerja yang berbeza dengan berkesan.
- **Keselamatan dan Kawalan:** Organisasi boleh mengekalkan kawalan ke atas data dan aplikasi mereka dengan menghos NIM microservices pada infrastruktur yang mereka urus sendiri.
- **API Standard:** NIM menyediakan API standard industri, memudahkan pembangunan dan integrasi aplikasi AI seperti chatbot, pembantu AI, dan lain-lain.

NIM adalah sebahagian daripada NVIDIA AI Enterprise, yang bertujuan untuk memudahkan penyebaran dan pengoperasian model AI, memastikan ia berjalan dengan cekap pada GPU NVIDIA.

- Demo: Menggunakan NVIDIA NIM untuk memanggil Phi-3.5-Vision-API  [[Klik pautan ini](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Menjalankan Phi-3/3.5 Secara Tempatan
Inferens berkaitan dengan Phi-3, atau mana-mana model bahasa seperti GPT-3, merujuk kepada proses menjana respons atau ramalan berdasarkan input yang diterimanya. Apabila anda memberikan prompt atau soalan kepada Phi-3, ia menggunakan rangkaian neural yang telah dilatih untuk menyimpulkan respons yang paling mungkin dan relevan dengan menganalisis corak dan hubungan dalam data yang dilatih.

**Hugging Face Transformer**
Hugging Face Transformers adalah perpustakaan yang kuat direka untuk pemprosesan bahasa semula jadi (NLP) dan tugas pembelajaran mesin lain. Berikut adalah beberapa perkara penting mengenainya:

1. **Model Sudah Dilatih:** Ia menyediakan ribuan model yang telah dilatih yang boleh digunakan untuk pelbagai tugas seperti klasifikasi teks, pengecaman entiti dinamakan, menjawab soalan, meringkaskan, terjemahan, dan penjanaan teks.

2. **Interoperabiliti Rangka Kerja:** Perpustakaan ini menyokong pelbagai rangka kerja pembelajaran mendalam, termasuk PyTorch, TensorFlow, dan JAX. Ini membolehkan anda melatih model dalam satu rangka kerja dan menggunakan dalam yang lain.

3. **Keupayaan Multimodal:** Selain NLP, Hugging Face Transformers juga menyokong tugas dalam penglihatan komputer (contohnya, klasifikasi imej, pengesanan objek) dan pemprosesan audio (contohnya, pengecaman pertuturan, klasifikasi audio).

4. **Mudah Digunakan:** Perpustakaan menawarkan API dan alat untuk memuat turun dan melaras model dengan mudah, menjadikannya dapat diakses untuk pemula dan pakar.

5. **Komuniti dan Sumber:** Hugging Face mempunyai komuniti yang aktif dan dokumentasi yang luas, tutorial, dan panduan untuk membantu pengguna memulakan dan memaksimakan penggunaan perpustakaan.
[dokumentasi rasmi](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) atau repositori [GitHub mereka](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Ini adalah kaedah yang paling kerap digunakan, tetapi ia juga memerlukan pecutan GPU. Lagipun, senario seperti Vision dan MoE memerlukan banyak pengiraan, yang akan sangat perlahan pada CPU jika tidak diquantize.


- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-Instruct [Klik pautan ini](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-Vision [Klik pautan ini](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-MoE [Klik pautan ini](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) adalah platform yang direka untuk memudahkan menjalankan model bahasa besar (LLM) secara tempatan pada komputer anda. Ia menyokong pelbagai model seperti Llama 3.1, Phi 3, Mistral, dan Gemma 2, antara lain. Platform ini memudahkan proses dengan menggabungkan berat model, konfigurasi, dan data ke dalam satu pakej, menjadikannya lebih mudah untuk pengguna mengubahsuai dan mencipta model mereka sendiri. Ollama tersedia untuk macOS, Linux, dan Windows. Ia adalah alat yang bagus jika anda ingin mencuba atau menyebarkan LLM tanpa bergantung pada perkhidmatan awan. Ollama adalah cara yang paling langsung, anda hanya perlu melaksanakan arahan berikut.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) adalah runtime tanpa talian Microsoft yang berjalan di atas peranti untuk menjalankan model seperti Phi sepenuhnya pada perkakasan anda sendiri - tiada langganan Azure, kunci API, atau sambungan rangkaian diperlukan. Ia secara automatik memilih penyedia pelaksanaan terbaik yang ada (NPU, GPU, atau CPU) dan menyediakan titik akhir yang serasi dengan OpenAI, jadi kod `openai`/Azure AI Inference SDK yang sedia ada boleh menunjuk kepadanya dengan perubahan minimal. Lihat [dokumentasi Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) untuk bermula.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Atau guna SDK terus dalam Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime untuk GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) adalah pecutan pembelajaran mesin lintas platform untuk inferens dan latihan. ONNX Runtime untuk Generative AI (GENAI) adalah alat kuat yang membantu anda menjalankan model AI generatif dengan cekap merentas pelbagai platform.

## Apakah ONNX Runtime?
ONNX Runtime adalah projek sumber terbuka yang membolehkan inferens berprestasi tinggi bagi model pembelajaran mesin. Ia menyokong model dalam format Open Neural Network Exchange (ONNX), yang merupakan standard untuk mewakili model pembelajaran mesin. Inferens ONNX Runtime boleh mempercepat pengalaman pelanggan dan mengurangkan kos, menyokong model dari rangka kerja pembelajaran mendalam seperti PyTorch dan TensorFlow/Keras serta perpustakaan pembelajaran mesin klasik seperti scikit-learn, LightGBM, XGBoost, dan lain-lain. ONNX Runtime serasi dengan pelbagai perkakasan, pemandu, dan sistem operasi, serta menyediakan prestasi optimum dengan memanfaatkan pecut perkakasan di samping pengoptimuman graf dan transformasi.

## Apakah Generative AI?
Generative AI merujuk kepada sistem AI yang dapat menjana kandungan baru, seperti teks, imej, atau muzik, berdasarkan data yang telah dilatih. Contohnya termasuk model bahasa seperti GPT-3 dan model penjanaan imej seperti Stable Diffusion. Perpustakaan ONNX Runtime untuk GenAI menyediakan gelung AI generatif untuk model ONNX, termasuk inferens dengan ONNX Runtime, pemprosesan logits, carian dan pensampelan, serta pengurusan cache KV.

## ONNX Runtime untuk GENAI
ONNX Runtime untuk GENAI memperluas keupayaan ONNX Runtime untuk menyokong model AI generatif. Berikut adalah beberapa ciri utama:

- **Sokongan Platform Meluas:** Ia berfungsi pada pelbagai platform, termasuk Windows, Linux, macOS, Android, dan iOS.
- **Sokongan Model:** Ia menyokong banyak model AI generatif popular, seperti LLaMA, GPT-Neo, BLOOM, dan lain-lain.
- **Pengoptimuman Prestasi:** Ia termasuk pengoptimuman untuk pelbagai pecut perkakasan seperti GPU NVIDIA, GPU AMD, dan lain-lain.
- **Mudah Digunakan:** Ia menyediakan API untuk integrasi mudah ke dalam aplikasi, membolehkan anda menjana teks, imej, dan kandungan lain dengan kod yang minimum.
- Pengguna boleh memanggil kaedah generate() peringkat tinggi, atau menjalankan setiap iterasi model dalam gelung, menjana satu token pada satu masa, dan secara pilihan mengemaskini parameter penjanaan dalam gelung tersebut.
- ONNX runtime juga menyokong carian greedy/beam dan pensampelan TopP, TopK untuk menjana urutan token dan pemprosesan logits terbina dalam seperti penalti pengulangan. Anda juga boleh menambah pemarkahan khusus dengan mudah.

## Memulakan
Untuk memulakan dengan ONNX Runtime untuk GENAI, anda boleh mengikuti langkah-langkah berikut:

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


**Lain-lain**

Selain daripada kaedah rujukan ONNX Runtime, Ollama, dan Foundry Local, kita juga boleh melengkapkan rujukan model kuantitatif berdasarkan kaedah rujukan model yang disediakan oleh pengeluar yang berbeza. Seperti rangka kerja Apple MLX dengan Apple Metal, Qualcomm QNN dengan NPU, Intel OpenVINO dengan CPU/GPU, dan lain-lain. Anda juga boleh mendapatkan lebih banyak kandungan dari [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Lebih Lanjut

Kita telah mempelajari asas-asas Keluarga Phi-3/3.5, tetapi untuk belajar lebih lanjut tentang SLM kita memerlukan lebih banyak pengetahuan. Anda boleh mencari jawapan dalam Phi-3 Cookbook. Jika anda ingin belajar lebih banyak, sila lawati [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->