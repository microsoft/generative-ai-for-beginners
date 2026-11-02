# Pengantar Model Bahasa Kecil untuk AI Generatif bagi Pemula
AI Generatif adalah bidang kecerdasan buatan yang menarik yang berfokus pada penciptaan sistem yang mampu menghasilkan konten baru. Konten ini dapat berupa teks dan gambar hingga musik dan bahkan seluruh lingkungan virtual. Salah satu aplikasi paling menarik dari AI generatif adalah di bidang model bahasa.

## Apa Itu Model Bahasa Kecil?

Model Bahasa Kecil (SLM) merupakan varian yang diperkecil dari model bahasa besar (LLM), menggunakan banyak prinsip arsitektur dan teknik dari LLM, namun dengan jejak komputasi yang jauh lebih kecil.

SLM adalah subset dari model bahasa yang dirancang untuk menghasilkan teks yang menyerupai bahasa manusia. Berbeda dengan model besar seperti GPT-4, SLM lebih kompak dan efisien, sehingga ideal untuk aplikasi yang memiliki sumber daya komputasi terbatas. Meskipun ukurannya lebih kecil, SLM tetap dapat melakukan berbagai tugas. Biasanya, SLM dibangun dengan cara mengompresi atau mendistilasi LLM, dengan tujuan mempertahankan sebagian besar fungsi dan kemampuan linguistik dari model aslinya. Pengurangan ukuran model ini menurunkan kompleksitas keseluruhan, membuat SLM lebih efisien baik dalam penggunaan memori maupun kebutuhan komputasi. Meskipun demikian, SLM dapat melakukan berbagai tugas pemrosesan bahasa alami (NLP):

- Pembuatan Teks: Membuat kalimat atau paragraf yang koheren dan relevan secara konteks.
- Penyelesaian Teks: Memprediksi dan menyelesaikan kalimat berdasarkan prompt yang diberikan.
- Terjemahan: Mengonversi teks dari satu bahasa ke bahasa lain.
- Ringkasan: Merangkum teks panjang menjadi bagian yang lebih pendek dan mudah dipahami.

Meski dengan beberapa kompromi dalam kinerja atau kedalaman pemahaman dibandingkan model besar.

## Bagaimana Cara Kerja Model Bahasa Kecil?
SLM dilatih menggunakan sejumlah besar data teks. Selama pelatihan, mereka mempelajari pola dan struktur bahasa, sehingga dapat menghasilkan teks yang benar secara tata bahasa dan sesuai konteks. Proses pelatihan melibatkan:

- Pengumpulan Data: Mengumpulkan dataset teks besar dari berbagai sumber.
- Pra-pemrosesan: Membersihkan dan mengorganisir data agar cocok untuk pelatihan.
- Pelatihan: Menggunakan algoritma pembelajaran mesin untuk mengajarkan model memahami dan menghasilkan teks.
- Penyesuaian: Menyesuaikan model untuk meningkatkan kinerjanya pada tugas-tugas tertentu.

Pengembangan SLM sejalan dengan meningkatnya kebutuhan model yang bisa diterapkan di lingkungan dengan keterbatasan sumber daya, seperti perangkat mobile atau platform edge computing, di mana LLM skala penuh mungkin tidak praktis karena kebutuhan sumber daya yang besar. Dengan fokus pada efisiensi, SLM menyeimbangkan kinerja dengan aksesibilitas, memungkinkan aplikasi yang lebih luas di berbagai domain.

![slm](../../../translated_images/id/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Tujuan Pembelajaran

Dalam pelajaran ini, kami berharap dapat memperkenalkan pengetahuan tentang SLM dan menggabungkannya dengan Microsoft Phi-3 untuk mempelajari skenario berbeda dalam konten teks, visi, dan MoE.

Pada akhir pelajaran ini, Anda seharusnya dapat menjawab pertanyaan berikut:

- Apa itu SLM?
- Apa perbedaan antara SLM dan LLM?
- Apa itu Keluarga Microsoft Phi-3/3.5?
- Bagaimana menjalankan inferensi dengan Keluarga Microsoft Phi-3/3.5?

Siap? Mari kita mulai.

## Perbedaan antara Model Bahasa Besar (LLM) dan Model Bahasa Kecil (SLM)

Baik LLM maupun SLM dibangun berdasarkan prinsip dasar pembelajaran mesin probabilistik, mengikuti pendekatan serupa dalam desain arsitektur, metodologi pelatihan, proses pembuatan data, dan teknik evaluasi model. Namun, ada beberapa faktor utama yang membedakan kedua tipe model ini.

## Aplikasi Model Bahasa Kecil

SLM memiliki berbagai aplikasi, termasuk:

- Chatbots: Memberikan dukungan pelanggan dan berinteraksi dengan pengguna secara percakapan.
- Pembuatan Konten: Membantu penulis dengan menghasilkan ide atau bahkan menyusun artikel lengkap.
- Pendidikan: Membantu siswa dengan tugas menulis atau mempelajari bahasa baru.
- Aksesibilitas: Menciptakan alat untuk individu dengan disabilitas, seperti sistem teks ke ucapan.

**Ukuran**
  
Perbedaan utama antara LLM dan SLM terletak pada skala model. LLM, seperti ChatGPT (GPT-4), terdiri dari sekitar 1,76 triliun parameter, sementara SLM sumber terbuka seperti Mistral 7B dirancang dengan jumlah parameter yang jauh lebih sedikit—sekitar 7 milyar. Perbedaan ini terutama disebabkan oleh perbedaan arsitektur model dan proses pelatihan. Misalnya, ChatGPT menggunakan mekanisme self-attention dalam kerangka kerja encoder-decoder, sedangkan Mistral 7B menggunakan sliding window attention, yang memungkinkan pelatihan lebih efisien dalam model decoder-only. Variasi arsitektur ini memiliki dampak besar pada kompleksitas dan kinerja model.

**Pemahaman**

SLM biasanya dioptimalkan untuk kinerja dalam domain tertentu, menjadikannya sangat khusus tapi mungkin terbatas dalam kemampuan memberikan pemahaman kontekstual luas di berbagai bidang pengetahuan. Sebaliknya, LLM bertujuan meniru kecerdasan mirip manusia dalam tingkat lebih komprehensif. Dilatih dengan dataset besar dan beragam, LLM dirancang untuk bekerja baik di berbagai domain, menawarkan fleksibilitas dan adaptabilitas lebih besar. Oleh karena itu, LLM lebih cocok untuk beragam tugas hilir, seperti pemrosesan bahasa alami dan pemrograman.

**Komputasi**

Pelatihan dan penerapan LLM adalah proses yang intensif sumber daya, sering memerlukan infrastruktur komputasi besar, termasuk klaster GPU skala besar. Misalnya, pelatihan model seperti ChatGPT dari awal mungkin memerlukan ribuan GPU selama periode waktu lama. Sebaliknya, SLM dengan jumlah parameter yang lebih kecil lebih mudah diakses dalam hal sumber daya komputasi. Model seperti Mistral 7B dapat dilatih dan dijalankan pada mesin lokal dengan kemampuan GPU sedang, meskipun pelatihan masih memerlukan beberapa jam dengan beberapa GPU.

**Bias**

Bias adalah masalah yang diketahui pada LLM, terutama karena sifat data pelatihan. Model ini sering bergantung pada data mentah yang tersedia secara terbuka di internet, yang mungkin kurang merepresentasikan atau salah menggambarkan kelompok tertentu, memperkenalkan pelabelan yang salah, atau mencerminkan bias linguistik yang dipengaruhi oleh dialek, variasi geografis, dan aturan tata bahasa. Selain itu, kompleksitas arsitektur LLM dapat secara tidak sengaja memperburuk bias, yang mungkin tidak terdeteksi tanpa penyesuaian yang cermat. Sebaliknya, SLM yang dilatih pada dataset yang lebih terbatas dan spesifik domain, secara inheren lebih tahan terhadap bias tersebut, meskipun tidak sepenuhnya kebal.

**Inferensi**

Ukuran yang lebih kecil dari SLM memberi keuntungan signifikan dalam kecepatan inferensi, memungkinkan mereka menghasilkan keluaran dengan efisien pada perangkat keras lokal tanpa perlu pemrosesan paralel yang ekstensif. Sebaliknya, LLM karena ukuran dan kompleksitasnya seringkali memerlukan sumber daya komputasi paralel besar untuk mencapai waktu inferensi yang dapat diterima. Kehadiran banyak pengguna secara bersamaan semakin memperlambat waktu respons LLM, terutama saat digunakan secara massal.

Singkatnya, meskipun LLM dan SLM memiliki dasar pembelajaran mesin yang sama, mereka berbeda secara signifikan dalam ukuran model, kebutuhan sumber daya, pemahaman kontekstual, kerentanan terhadap bias, dan kecepatan inferensi. Perbedaan ini mencerminkan kesesuaian mereka untuk berbagai kasus penggunaan, dengan LLM lebih serbaguna namun berat sumber daya, dan SLM menawarkan efisiensi spesifik domain dengan kebutuhan komputasi yang lebih rendah.

***Catatan: Dalam pelajaran ini, kami akan memperkenalkan SLM menggunakan Microsoft Phi-3 / 3.5 sebagai contoh.***

## Memperkenalkan Keluarga Phi-3 / Phi-3.5

Keluarga Phi-3 / 3.5 terutama menargetkan skenario aplikasi teks, visi, dan Agen (MoE):

### Phi-3 / 3.5 Instruct

Utamanya untuk pembuatan teks, penyelesaian obrolan, dan ekstraksi informasi konten, dll.

**Phi-3-mini**

Model bahasa 3.8B tersedia di Microsoft Foundry, Hugging Face, dan Ollama. Model Phi-3 secara signifikan mengungguli model bahasa dengan ukuran yang sama dan lebih besar dalam tolok ukur utama (lihat angka tolok ukur di bawah, angka lebih tinggi lebih baik). Phi-3-mini mengungguli model dua kali ukurannya, sementara Phi-3-small dan Phi-3-medium mengungguli model lebih besar, termasuk GPT-3.5.

**Phi-3-small & medium**

Dengan hanya 7B parameter, Phi-3-small mengalahkan GPT-3.5T pada berbagai tolok ukur bahasa, penalaran, pengkodean, dan matematika.

Phi-3-medium dengan 14B parameter melanjutkan tren ini dan mengungguli Gemini 1.0 Pro.

**Phi-3.5-mini**

Kita dapat menganggapnya sebagai peningkatan dari Phi-3-mini. Meskipun parameter tetap sama, ia meningkatkan kemampuan mendukung banyak bahasa (mendukung 20+ bahasa: Arab, Cina, Ceko, Denmark, Belanda, Inggris, Finlandia, Perancis, Jerman, Ibrani, Hungaria, Italia, Jepang, Korea, Norwegia, Polandia, Portugis, Rusia, Spanyol, Swedia, Thailand, Turki, Ukraina) dan menambah dukungan kuat untuk konteks panjang.

Phi-3.5-mini dengan 3.8B parameter mengungguli model bahasa dengan ukuran sama dan sejajar dengan model dua kali ukurannya.

### Phi-3 / 3.5 Vision

Kita dapat menganggap model Instruct dari Phi-3/3.5 sebagai kemampuan Phi untuk memahami, dan Vision adalah yang memberi Phi 'mata' untuk memahami dunia.


**Phi-3-Vision**

Phi-3-vision, dengan hanya 4.2B parameter, melanjutkan tren ini dan mengungguli model lebih besar seperti Claude-3 Haiku dan Gemini 1.0 Pro V pada tugas penalaran visual umum, OCR, dan pemahaman tabel serta diagram.


**Phi-3.5-Vision**

Phi-3.5-Vision juga merupakan peningkatan dari Phi-3-Vision, menambah dukungan untuk banyak gambar. Anda dapat menganggapnya sebagai peningkatan dalam visi, tidak hanya dapat melihat gambar, tetapi juga video.

Phi-3.5-vision mengungguli model lebih besar seperti Claude-3.5 Sonnet dan Gemini 1.5 Flash dalam tugas OCR, pemahaman tabel dan grafik, dan setara pada tugas penalaran pengetahuan visual umum. Mendukung input multi-frame, yaitu melakukan penalaran pada beberapa gambar input.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** memungkinkan model dilatih sebelumnya dengan komputasi yang jauh lebih sedikit, yang berarti Anda dapat meningkatkan ukuran model atau dataset dengan anggaran komputasi yang sama seperti model padat. Secara khusus, model MoE harus mencapai kualitas yang sama dengan lawan padatnya jauh lebih cepat selama pretraining.

Phi-3.5-MoE terdiri dari 16x3.8B modul ahli. Phi-3.5-MoE dengan hanya 6.6B parameter aktif mencapai level penalaran, pemahaman bahasa, dan matematika yang serupa dengan model jauh lebih besar.

Kita dapat menggunakan model Keluarga Phi-3/3.5 berdasarkan skenario yang berbeda. Berbeda dengan LLM, Anda dapat menerapkan Phi-3/3.5-mini atau Phi-3/3.5-Vision di perangkat edge.


## Cara menggunakan model Keluarga Phi-3/3.5

Kami berharap menggunakan Phi-3/3.5 dalam berbagai skenario. Selanjutnya, kami akan menggunakan Phi-3/3.5 berdasarkan skenario berbeda.

![phi3](../../../translated_images/id/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferensi melalui API Cloud

**Model Microsoft Foundry**

> **Catatan:** Model GitHub akan dihentikan pada akhir Juli 2026. [Model Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) adalah pengganti langsungnya.

> **Catatan:** Seluruh keluarga Phi-3/3.5 (varian Instruct, Vision, dan MoE) dihentikan dari katalog Model Microsoft Foundry pada 2025-08-30. Gunakan `Phi-4` (Instruct) atau `Phi-4-mini-instruct` di sana sebagai gantinya — contoh Phi-3/3.5 di bawah ini masih dapat digunakan melalui Hugging Face, Ollama, ONNX Runtime, dan NVIDIA NIM.

Model Microsoft Foundry kini menyediakan penerus Phi-4. Gunakan `Phi-4` atau `Phi-4-mini-instruct` sebagai pengganti model Phi-3/3.5 yang sudah dihentikan saat mengikuti contoh API cloud.

- Demo: Perbandingan efek Phi-3-mini dan Phi-3.5-mini dalam skenario bahasa Cina

![phi3](../../../translated_images/id/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/id/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Jika Anda ingin menggunakan model visi (multimodal) di cloud, gunakan `Phi-4-multimodal-instruct` yang tersedia saat ini melalui Microsoft Foundry sebagai pengganti model Phi-3/3.5 Vision yang sudah dihentikan; untuk tugas teks gunakan `Phi-4` atau `Phi-4-mini-instruct`. Model Phi-3.5 MoE telah dihentikan dari Microsoft Foundry, jadi gunakan pilihan lain yang dijelaskan dalam pelajaran ini (misalnya Hugging Face) jika ingin bereksperimen dengannya. Jika tertarik, Anda bisa membaca Phi Cookbook untuk belajar cara memanggil model Phi melalui Microsoft Foundry [Klik tautan ini](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Selain katalog Model Microsoft Foundry berbasis cloud, Anda juga dapat menggunakan [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) untuk melengkapi panggilan terkait. Anda dapat mengunjungi NVIDIA NIM untuk menyelesaikan panggilan API Keluarga Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) adalah serangkaian layanan mikro inferensi yang dipercepat yang dirancang untuk membantu pengembang menerapkan model AI secara efisien di berbagai lingkungan, termasuk cloud, pusat data, dan workstation.

Berikut beberapa fitur utama NVIDIA NIM:

- **Kemudahan Penyebaran:** NIM memungkinkan penyebaran model AI dengan satu perintah, membuatnya mudah diintegrasikan ke dalam alur kerja yang sudah ada.
- **Performa Teroptimasi:** Ia memanfaatkan mesin inferensi pra-teroptimasi NVIDIA, seperti TensorRT dan TensorRT-LLM, untuk menjamin latensi rendah dan throughput tinggi.
- **Skalabilitas:** NIM mendukung autoscaling di Kubernetes, memungkinkan penanganan beban kerja yang bervariasi secara efektif.
- **Keamanan dan Kontrol:** Organisasi dapat mempertahankan kendali atas data dan aplikasi mereka dengan meng-hosting sendiri layanan mikro NIM pada infrastruktur yang mereka kelola sendiri.
- **API Standar:** NIM menyediakan API standar industri, memudahkan pembangunan dan integrasi aplikasi AI seperti chatbot, asisten AI, dan lainnya.

NIM adalah bagian dari NVIDIA AI Enterprise, yang bertujuan menyederhanakan penyebaran dan operasionalisasi model AI, memastikan mereka berjalan efisien pada GPU NVIDIA.

- Demo: Menggunakan NVIDIA NIM untuk memanggil Phi-3.5-Vision-API  [[Klik tautan ini](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Menjalankan Phi-3/3.5 Secara Lokal
Inferensi terkait Phi-3, atau model bahasa apa pun seperti GPT-3, mengacu pada proses menghasilkan respons atau prediksi berdasarkan input yang diterima. Saat Anda memberikan prompt atau pertanyaan kepada Phi-3, ia menggunakan jaringan saraf terlatihnya untuk menginfersikan respons yang paling mungkin dan relevan dengan menganalisis pola dan hubungan dalam data yang telah dilatih.

**Hugging Face Transformer**
Hugging Face Transformers adalah pustaka kuat yang dirancang untuk pemrosesan bahasa alami (NLP) dan tugas pembelajaran mesin lainnya. Berikut beberapa poin kunci tentangnya:

1. **Model Pra-latih**: Menyediakan ribuan model yang telah dipra-latih yang dapat digunakan untuk berbagai tugas seperti klasifikasi teks, pengenalan entitas bernama, menjawab pertanyaan, meringkas, menerjemahkan, dan menghasilkan teks.

2. **Interoperabilitas Framework**: Pustaka mendukung berbagai framework pembelajaran mendalam, termasuk PyTorch, TensorFlow, dan JAX. Ini memungkinkan Anda melatih model di satu framework dan menggunakannya di framework lain.

3. **Kemampuan Multimodal**: Selain NLP, Hugging Face Transformers juga mendukung tugas dalam visi komputer (misalnya klasifikasi gambar, deteksi objek) dan pemrosesan audio (misalnya pengenalan suara, klasifikasi audio).

4. **Kemudahan Penggunaan**: Pustaka menawarkan API dan alat untuk mengunduh dan menyempurnakan model dengan mudah, membuatnya dapat diakses oleh pemula maupun ahli.

5. **Komunitas dan Sumber Daya**: Hugging Face memiliki komunitas yang hidup dan dokumentasi yang luas, tutorial, dan panduan untuk membantu pengguna memulai dan memaksimalkan penggunaan pustaka.
[dokumentasi resmi](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) atau [repositori GitHub mereka](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Ini adalah metode yang paling umum digunakan, tetapi juga membutuhkan akselerasi GPU. Karena, skenario seperti Vision dan MoE memerlukan banyak perhitungan, yang akan sangat lambat di CPU jika tidak dikwantisasi.


- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-Instruct [Klik tautan ini](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-Vision [Klik tautan ini](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-MoE [Klik tautan ini](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) adalah platform yang dirancang untuk mempermudah menjalankan model bahasa besar (LLM) secara lokal di mesin Anda. Mendukung berbagai model seperti Llama 3.1, Phi 3, Mistral, dan Gemma 2, antara lain. Platform ini menyederhanakan proses dengan menggabungkan bobot model, konfigurasi, dan data menjadi satu paket, sehingga lebih mudah diakses oleh pengguna untuk menyesuaikan dan membuat model mereka sendiri. Ollama tersedia untuk macOS, Linux, dan Windows. Ini adalah alat yang bagus jika Anda ingin bereksperimen atau menyebarkan LLM tanpa bergantung pada layanan cloud. Ollama adalah cara paling langsung, Anda hanya perlu mengeksekusi perintah berikut.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) adalah runtime offline di perangkat dari Microsoft untuk menjalankan model seperti Phi sepenuhnya di perangkat keras Anda sendiri - tanpa langganan Azure, kunci API, atau koneksi jaringan. Ia secara otomatis memilih penyedia eksekusi terbaik yang tersedia (NPU, GPU, atau CPU) dan menyediakan endpoint kompatibel OpenAI, sehingga kode `openai`/Azure AI Inference SDK yang sudah ada dapat diarahkan ke sana dengan perubahan minimal. Lihat [dokumentasi Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) untuk memulai.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Atau gunakan SDK langsung di Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime untuk GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) adalah akselerator pembelajaran mesin lintas platform untuk inferensi dan pelatihan. ONNX Runtime untuk Generative AI (GENAI) adalah alat kuat yang membantu Anda menjalankan model AI generatif secara efisien di berbagai platform.

## Apa itu ONNX Runtime?
ONNX Runtime adalah proyek sumber terbuka yang memungkinkan inferensi berperforma tinggi dari model pembelajaran mesin. Mendukung model dalam format Open Neural Network Exchange (ONNX), yang merupakan standar untuk merepresentasikan model pembelajaran mesin. Inferensi ONNX Runtime dapat memungkinkan pengalaman pelanggan lebih cepat dan biaya lebih rendah, mendukung model dari framework pembelajaran mendalam seperti PyTorch dan TensorFlow/Keras serta pustaka pembelajaran mesin klasik seperti scikit-learn, LightGBM, XGBoost, dll. ONNX Runtime kompatibel dengan berbagai perangkat keras, driver, dan sistem operasi, serta memberikan performa optimal dengan memanfaatkan akselerator perangkat keras yang tersedia bersama optimasi dan transformasi graf.

## Apa itu Generative AI?
Generative AI mengacu pada sistem AI yang dapat menghasilkan konten baru, seperti teks, gambar, atau musik, berdasarkan data yang telah dilatih. Contohnya termasuk model bahasa seperti GPT-3 dan model generasi gambar seperti Stable Diffusion. Perpustakaan ONNX Runtime untuk GenAI menyediakan siklus AI generatif untuk model ONNX, termasuk inferensi dengan ONNX Runtime, pemrosesan logits, pencarian dan pengambilan sampel, serta manajemen cache KV.

## ONNX Runtime untuk GENAI
ONNX Runtime untuk GENAI memperluas kemampuan ONNX Runtime untuk mendukung model AI generatif. Berikut beberapa fitur utamanya:

- **Dukungan Platform Luas:** Bekerja di berbagai platform, termasuk Windows, Linux, macOS, Android, dan iOS.
- **Dukungan Model:** Mendukung banyak model AI generatif populer seperti LLaMA, GPT-Neo, BLOOM, dan lainnya.
- **Optimasi Performa:** Termasuk optimasi untuk berbagai akselerator perangkat keras seperti GPU NVIDIA, GPU AMD, dan lainnya.
- **Kemudahan Penggunaan:** Menyediakan API untuk integrasi mudah ke aplikasi, memungkinkan Anda membuat teks, gambar, dan konten lain dengan kode minimal.
- Pengguna dapat memanggil metode generate() tingkat tinggi, atau menjalankan setiap iterasi model dalam loop, menghasilkan satu token sekaligus, dan opsional memperbarui parameter generasi di dalam loop.
- ONNX runtime juga mendukung pencarian greedy/beam dan pengambilan sampel TopP, TopK untuk menghasilkan urutan token serta pemrosesan logits bawaan seperti penalti pengulangan. Anda juga dapat dengan mudah menambahkan penilaian kustom.

## Memulai
Untuk memulai dengan ONNX Runtime untuk GENAI, Anda dapat mengikuti langkah-langkah berikut:

### Instal ONNX Runtime:
```Python
pip install onnxruntime
```
### Instal Ekstensi AI Generatif:
```Python
pip install onnxruntime-genai
```

### Jalankan Model: Berikut contoh sederhana dalam Python:
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


**Lainnya**

Selain ONNX Runtime, Ollama, dan metode referensi Foundry Local, kita juga dapat melengkapi referensi model kuantitatif berdasarkan metode referensi model yang disediakan oleh berbagai produsen. Seperti framework Apple MLX dengan Apple Metal, Qualcomm QNN dengan NPU, Intel OpenVINO dengan CPU/GPU, dll. Anda juga dapat mendapatkan lebih banyak konten dari [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Lebih Lanjut

Kita telah mempelajari dasar-dasar Keluarga Phi-3/3.5, tetapi untuk belajar lebih banyak tentang SLM kita perlu pengetahuan lebih lanjut. Anda bisa menemukan jawabannya di Phi-3 Cookbook. Jika ingin belajar lebih lanjut, silakan kunjungi [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->