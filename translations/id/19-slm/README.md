# Pengantar Model Bahasa Kecil untuk AI Generatif bagi Pemula
AI Generatif adalah bidang kecerdasan buatan yang menarik yang berfokus pada penciptaan sistem yang mampu menghasilkan konten baru. Konten ini dapat berupa teks dan gambar hingga musik dan bahkan seluruh lingkungan virtual. Salah satu aplikasi AI generatif yang paling menarik adalah dalam ranah model bahasa.

## Apa Itu Model Bahasa Kecil?

Model Bahasa Kecil (SLM) mewakili varian yang diperkecil dari model bahasa besar (LLM), memanfaatkan banyak prinsip arsitektural dan teknik LLM, sementara menunjukkan jejak komputasi yang jauh lebih kecil.

SLM adalah subset dari model bahasa yang dirancang untuk menghasilkan teks mirip manusia. Berbeda dengan rekan mereka yang lebih besar, seperti GPT-4, SLM lebih ringkas dan efisien, sehingga ideal untuk aplikasi di mana sumber daya komputasi terbatas. Meskipun ukurannya lebih kecil, mereka masih dapat melakukan berbagai tugas. Biasanya, SLM dibangun dengan mengompres atau mendistilasi LLM, bertujuan mempertahankan sebagian besar fungsi asli dan kemampuan linguistik model tersebut. Pengurangan ukuran model ini menurunkan keseluruhan kompleksitas, membuat SLM lebih efisien baik dalam penggunaan memori maupun kebutuhan komputasi. Meskipun dengan optimasi ini, SLM masih dapat melakukan berbagai tugas pemrosesan bahasa alami (NLP):

- Generasi Teks: Membuat kalimat atau paragraf yang koheren dan relevan secara kontekstual.
- Penyelesaian Teks: Memprediksi dan menyelesaikan kalimat berdasarkan petunjuk yang diberikan.
- Terjemahan: Mengkonversi teks dari satu bahasa ke bahasa lain.
- Ringkasan: Merangkum teks panjang menjadi ringkasan yang lebih singkat dan mudah dipahami.

Meskipun dengan beberapa kompromi dalam kinerja atau kedalaman pemahaman dibandingkan dengan rekan yang lebih besar.

## Bagaimana Cara Kerja Model Bahasa Kecil?
SLM dilatih menggunakan sejumlah besar data teks. Selama pelatihan, mereka mempelajari pola dan struktur bahasa, memungkinkan mereka menghasilkan teks yang benar secara tata bahasa dan sesuai konteks. Proses pelatihan meliputi:

- Pengumpulan Data: Mengumpulkan dataset besar teks dari berbagai sumber.
- Pra-pemrosesan: Membersihkan dan mengorganisasi data agar sesuai untuk pelatihan.
- Pelatihan: Menggunakan algoritma pembelajaran mesin untuk mengajarkan model cara memahami dan menghasilkan teks.
- Penyempurnaan: Menyesuaikan model untuk meningkatkan kinerjanya pada tugas tertentu.

Pengembangan SLM sejalan dengan kebutuhan yang meningkat akan model yang dapat diterapkan di lingkungan dengan sumber daya terbatas, seperti perangkat seluler atau platform edge computing, di mana LLM skala penuh mungkin tidak praktis karena kebutuhan sumber daya yang besar. Dengan fokus pada efisiensi, SLM menyeimbangkan kinerja dengan aksesibilitas, memungkinkan aplikasi yang lebih luas di berbagai domain.

![slm](../../../translated_images/id/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Tujuan Pembelajaran

Dalam pelajaran ini, kami berharap dapat memperkenalkan pengetahuan tentang SLM dan menggabungkannya dengan Microsoft Phi-3 untuk mempelajari berbagai skenario dalam konten teks, visi, dan MoE.

Pada akhir pelajaran ini, Anda diharapkan dapat menjawab pertanyaan berikut:

- Apa itu SLM?
- Apa perbedaan antara SLM dan LLM?
- Apa itu Keluarga Microsoft Phi-3/3.5?
- Bagaimana cara menjalankan inferensi dengan Keluarga Microsoft Phi-3/3.5?

Siap? Mari kita mulai.

## Perbedaan antara Model Bahasa Besar (LLM) dan Model Bahasa Kecil (SLM)

Baik LLM dan SLM dibangun berdasarkan prinsip dasar pembelajaran mesin probabilistik, mengikuti pendekatan serupa dalam desain arsitektural, metodologi pelatihan, proses pembuatan data, dan teknik evaluasi model. Namun, beberapa faktor kunci membedakan kedua jenis model ini.

## Aplikasi Model Bahasa Kecil

SLM memiliki berbagai aplikasi, termasuk:

- Chatbot: Memberikan dukungan pelanggan dan berinteraksi dengan pengguna secara percakapan.
- Pembuatan Konten: Membantu penulis dengan menghasilkan ide atau bahkan menyusun seluruh artikel.
- Pendidikan: Membantu siswa dengan tugas menulis atau belajar bahasa baru.
- Aksesibilitas: Membuat alat untuk individu dengan disabilitas, seperti sistem teks-ke-suara.

**Ukuran**
  
Perbedaan utama antara LLM dan SLM terletak pada skala modelnya. LLM, seperti ChatGPT (GPT-4), dapat mencakup sekitar 1,76 triliun parameter, sedangkan SLM sumber terbuka seperti Mistral 7B dirancang dengan parameter yang jauh lebih sedikit—sekitar 7 miliar. Perbedaan ini terutama disebabkan oleh arsitektur model dan proses pelatihan yang berbeda. Misalnya, ChatGPT menggunakan mekanisme self-attention dalam kerangka encoder-decoder, sementara Mistral 7B memakai sliding window attention, yang memungkinkan pelatihan lebih efisien dalam model decoder-only. Variasi arsitektural ini memiliki implikasi besar pada kompleksitas dan kinerja model-model ini.

**Pemahaman**

SLM biasanya dioptimalkan untuk performa dalam domain tertentu, menjadikannya sangat khusus tetapi berpotensi terbatas dalam kemampuannya memberikan pemahaman kontekstual luas di berbagai bidang pengetahuan. Sebaliknya, LLM berupaya mensimulasikan kecerdasan mirip manusia pada tingkat yang lebih komprehensif. Dilatih dengan dataset yang sangat besar dan beragam, LLM dirancang untuk bekerja baik di berbagai domain, menawarkan fleksibilitas dan adaptabilitas yang lebih tinggi. Karena itu, LLM lebih cocok untuk berbagai tugas hilir, seperti pemrosesan bahasa alami dan pemrograman.

**Komputasi**

Pelatihan dan penerapan LLM adalah proses yang membutuhkan sumber daya besar, sering kali memerlukan infrastruktur komputasi yang signifikan, termasuk klaster GPU skala besar. Misalnya, melatih model seperti ChatGPT dari awal mungkin membutuhkan ribuan GPU selama waktu yang lama. Sebaliknya, SLM dengan jumlah parameter yang lebih kecil lebih mudah diakses dari segi sumber daya komputasi. Model seperti Mistral 7B dapat dilatih dan dijalankan di mesin lokal dengan kemampuan GPU sedang, meskipun pelatihan tetap membutuhkan beberapa jam menggunakan beberapa GPU.

**Bias**

Bias adalah masalah yang diketahui pada LLM, terutama karena sifat data pelatihan. Model ini sering mengandalkan data mentah yang tersedia secara terbuka di internet, yang mungkin kurang merepresentasikan atau malah salah merepresentasikan kelompok tertentu, memperkenalkan pelabelan yang keliru, atau mencerminkan bias linguistik yang dipengaruhi oleh dialek, variasi geografis, dan aturan tata bahasa. Selain itu, kompleksitas arsitektur LLM dapat tanpa sengaja memperparah bias, yang mungkin tidak disadari tanpa penyempurnaan yang cermat. Di sisi lain, SLM yang dilatih pada dataset yang lebih terbatas dan domain-spesifik secara inheren kurang rentan terhadap bias tersebut, walaupun tidak sepenuhnya kebal.

**Inferensi**

Ukuran yang lebih kecil memberikan keuntungan signifikan bagi SLM dalam hal kecepatan inferensi, memungkinkan mereka menghasilkan output secara efisien pada perangkat keras lokal tanpa kebutuhan pemrosesan paralel yang luas. Sebaliknya, LLM karena ukuran dan kompleksitasnya, sering memerlukan sumber daya komputasi paralel yang besar untuk mencapai waktu inferensi yang dapat diterima. Kehadiran banyak pengguna sekaligus juga memperlambat waktu respons LLM, terutama saat diterapkan dalam skala besar.

Singkatnya, meskipun LLM dan SLM berbagi dasar pembelajaran mesin, mereka berbeda signifikan dari segi ukuran model, kebutuhan sumber daya, pemahaman kontekstual, kerentanan terhadap bias, dan kecepatan inferensi. Perbedaan ini mencerminkan kesesuaian mereka untuk kasus penggunaan yang berbeda, dengan LLM lebih serbaguna tetapi memakan sumber daya besar, dan SLM menawarkan efisiensi domain-spesifik dengan kebutuhan komputasi yang lebih rendah.

***Catatan: Dalam pelajaran ini, kita akan memperkenalkan SLM menggunakan Microsoft Phi-3 / 3.5 sebagai contoh.***

## Memperkenalkan Keluarga Phi-3 / Phi-3.5

Keluarga Phi-3 / 3.5 terutama menargetkan skenario aplikasi teks, visi, dan Agen (MoE):

### Phi-3 / 3.5 Instruct

Terutama untuk generasi teks, penyelesaian obrolan, dan ekstraksi informasi konten, dll.

**Phi-3-mini**

Model bahasa 3,8 miliar parameter tersedia di Microsoft Foundry, Hugging Face, dan Ollama. Model Phi-3 secara signifikan mengungguli model bahasa dengan ukuran yang sama dan lebih besar pada tolok ukur utama (lihat angka tolok ukur di bawah, angka yang lebih tinggi lebih baik). Phi-3-mini mengungguli model dua kali ukurannya, sedangkan Phi-3-small dan Phi-3-medium mengungguli model yang lebih besar, termasuk GPT-3.5.

**Phi-3-small & medium**

Dengan hanya 7 miliar parameter, Phi-3-small mengalahkan GPT-3.5T pada berbagai tolok ukur bahasa, penalaran, pengkodean, dan matematika.

Phi-3-medium dengan 14 miliar parameter melanjutkan tren ini dan mengungguli Gemini 1.0 Pro.

**Phi-3.5-mini**

Kita bisa menganggapnya sebagai peningkatan dari Phi-3-mini. Meski parameternya tetap sama, kemampuan untuk mendukung berbagai bahasa meningkat (mendukung 20+ bahasa: Arab, Cina, Ceko, Denmark, Belanda, Inggris, Finlandia, Prancis, Jerman, Ibrani, Hungaria, Italia, Jepang, Korea, Norwegia, Polandia, Portugis, Rusia, Spanyol, Swedia, Thai, Turki, Ukraina) dan menambahkan dukungan lebih kuat untuk konteks panjang.

Phi-3.5-mini dengan 3,8 miliar parameter mengungguli model bahasa dengan ukuran sama dan setara dengan model yang dua kali lebih besar.

### Phi-3 / 3.5 Vision

Kita dapat menganggap model Instruct Phi-3/3.5 sebagai kemampuan Phi untuk memahami, dan Vision memberikan Phi mata untuk memahami dunia.


**Phi-3-Vision**

Phi-3-vision, dengan hanya 4,2 miliar parameter, melanjutkan tren ini dan mengungguli model yang lebih besar seperti Claude-3 Haiku dan Gemini 1.0 Pro V dalam tugas penalaran visual umum, OCR, serta pemahaman tabel dan diagram.


**Phi-3.5-Vision**

Phi-3.5-Vision juga merupakan peningkatan dari Phi-3-Vision, menambahkan dukungan untuk beberapa gambar. Anda bisa menganggapnya sebagai peningkatan visi, tidak hanya dapat melihat gambar, tetapi juga video.

Phi-3.5-vision mengungguli model yang lebih besar seperti Claude-3.5 Sonnet dan Gemini 1.5 Flash dalam tugas OCR, pemahaman tabel dan grafik serta setara dalam tugas penalaran pengetahuan visual umum. Mendukung input multi-frame, yakni melakukan penalaran pada beberapa gambar input.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** memungkinkan model untuk dipra-latih dengan komputasi jauh lebih sedikit, yang berarti Anda dapat secara dramatis memperbesar ukuran model atau dataset dengan anggaran komputasi yang sama seperti model padat. Secara khusus, model MoE harus mencapai kualitas yang sama dengan rekan padatnya jauh lebih cepat selama pra-pelatihan.

Phi-3.5-MoE terdiri dari 16 modul ahli 3,8 miliar. Phi-3.5-MoE dengan hanya 6,6 miliar parameter aktif mencapai tingkat penalaran, pemahaman bahasa, dan matematika yang mirip dengan model yang jauh lebih besar.

Kita dapat menggunakan model Keluarga Phi-3/3.5 berdasarkan berbagai skenario. Berbeda dengan LLM, Anda dapat menerapkan Phi-3/3.5-mini atau Phi-3/3.5-Vision pada perangkat edge.


## Cara menggunakan model Keluarga Phi-3/3.5

Kami berharap menggunakan Phi-3/3.5 dalam berbagai skenario. Selanjutnya, kami akan menggunakan Phi-3/3.5 berdasarkan skenario yang berbeda.

![phi3](../../../translated_images/id/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferensi melalui API Cloud

**Model Microsoft Foundry**

> **Catatan:** GitHub Models akan dihentikan pada akhir Juli 2026. [Model Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) adalah pengganti langsungnya.

> **Catatan:** Seluruh keluarga Phi-3/3.5 (varian Instruct, Vision, dan MoE) telah dihentikan dari katalog Microsoft Foundry Models pada tanggal 2025-08-30. Gunakan `Phi-4` (Instruct) atau `Phi-4-mini-instruct` di sana sebagai gantinya — contoh Phi-3/3.5 di bawah ini masih berfungsi melalui Hugging Face, Ollama, ONNX Runtime, dan NVIDIA NIM.

Microsoft Foundry Models kini menyediakan penerus Phi-4. Gunakan `Phi-4` atau `Phi-4-mini-instruct` sebagai pengganti model Phi-3/3.5 yang sudah dihentikan saat mengikuti contoh API cloud.

- Demo: Perbandingan efek Phi-3-mini dan Phi-3.5-mini dalam skenario bahasa Cina

![phi3](../../../translated_images/id/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/id/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Jika Anda ingin menggunakan model visi (multimodal) di cloud, gunakan `Phi-4-multimodal-instruct` yang saat ini tersedia melalui Microsoft Foundry gantikan model Phi-3/3.5 Vision yang sudah dihentikan; untuk tugas teks gunakan `Phi-4` atau `Phi-4-mini-instruct`. Model Phi-3.5 MoE telah dihentikan dari Microsoft Foundry, jadi gunakan opsi lain yang dijelaskan dalam pelajaran ini (misalnya Hugging Face) jika Anda ingin bereksperimen dengannya. Jika tertarik, Anda dapat membaca Phi Cookbook untuk belajar cara memanggil model Phi melalui Microsoft Foundry [Klik tautan ini](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Selain katalog Model Microsoft Foundry berbasis cloud, Anda juga dapat menggunakan [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) untuk menyelesaikan panggilan terkait. Anda dapat mengunjungi NVIDIA NIM untuk menyelesaikan panggilan API keluarga Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) adalah seperangkat mikroservis inferensi yang dipercepat, dirancang untuk membantu pengembang menerapkan model AI dengan efisien di berbagai lingkungan, termasuk cloud, pusat data, dan workstation.

Berikut beberapa fitur utama dari NVIDIA NIM:

- **Kemudahan Penyebaran:** NIM memungkinkan penyebaran model AI dengan satu perintah, sehingga mudah untuk diintegrasikan ke dalam alur kerja yang sudah ada.
- **Performa Teroptimasi:** Ini memanfaatkan mesin inferensi yang sudah dioptimalkan sebelumnya dari NVIDIA, seperti TensorRT dan TensorRT-LLM, untuk memastikan latensi rendah dan throughput tinggi.
- **Skalabilitas:** NIM mendukung autoscaling di Kubernetes, sehingga dapat menangani beban kerja yang bervariasi secara efektif.
- **Keamanan dan Kontrol:** Organisasi dapat mempertahankan kontrol atas data dan aplikasi mereka dengan menghosting sendiri layanan mikro NIM di infrastruktur yang mereka kelola.
- **API Standar:** NIM menyediakan API standar industri, mempermudah pembangunan dan integrasi aplikasi AI seperti chatbot, asisten AI, dan lainnya.

NIM adalah bagian dari NVIDIA AI Enterprise, yang bertujuan untuk menyederhanakan penyebaran dan operasionalisasi model AI, memastikan mereka berjalan efisien di GPU NVIDIA.

- Demo: Menggunakan NVIDIA NIM untuk memanggil Phi-3.5-Vision-API  [[Klik tautan ini](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Menjalankan Phi-3/3.5 Secara Lokal
Inferensi terkait Phi-3, atau model bahasa apa pun seperti GPT-3, mengacu pada proses menghasilkan respons atau prediksi berdasarkan input yang diterimanya. Saat Anda memberikan prompt atau pertanyaan kepada Phi-3, ia menggunakan jaringan saraf terlatihnya untuk menyimpulkan respons yang paling mungkin dan relevan dengan menganalisis pola dan hubungan dalam data yang dilatihnya.

**Hugging Face Transformer**
Hugging Face Transformers adalah perpustakaan kuat yang dirancang untuk pemrosesan bahasa alami (NLP) dan tugas pembelajaran mesin lainnya. Berikut beberapa poin kunci tentangnya:

1. **Model Pra-latih**: Menyediakan ribuan model yang telah dilatih sebelumnya yang dapat digunakan untuk berbagai tugas seperti klasifikasi teks, pengenalan entitas bernama, menjawab pertanyaan, ringkasan, terjemahan, dan generasi teks.

2. **Interoperabilitas Framework**: Perpustakaan ini mendukung berbagai framework pembelajaran mendalam, termasuk PyTorch, TensorFlow, dan JAX. Ini memungkinkan Anda melatih model di satu framework dan menggunakannya di framework lain.

3. **Kemampuan Multimodal**: Selain NLP, Hugging Face Transformers juga mendukung tugas di bidang penglihatan komputer (misalnya, klasifikasi gambar, deteksi objek) dan pemrosesan audio (misalnya, pengenalan suara, klasifikasi audio).

4. **Kemudahan Penggunaan**: Perpustakaan ini menyediakan API dan alat untuk mengunduh dan menyetel model dengan mudah, membuatnya dapat diakses oleh pemula maupun ahli.

5. **Komunitas dan Sumber Daya**: Hugging Face memiliki komunitas yang aktif dan dokumentasi luas, tutorial, serta panduan untuk membantu pengguna memulai dan memaksimalkan penggunaan perpustakaan.
[dokumentasi resmi](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) atau [repositori GitHub mereka](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Ini adalah metode yang paling umum digunakan, tetapi juga memerlukan akselerasi GPU. Bagaimanapun, skenario seperti Vision dan MoE memerlukan banyak perhitungan, yang akan sangat lambat pada CPU jika tidak dikwantisasi.


- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-Instruct [Klik tautan ini](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-Vision [Klik tautan ini](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-MoE [Klik tautan ini](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) adalah platform yang dirancang untuk memudahkan menjalankan model bahasa besar (LLM) secara lokal di mesin Anda. Ia mendukung berbagai model seperti Llama 3.1, Phi 3, Mistral, dan Gemma 2, antara lain. Platform ini menyederhanakan proses dengan menggabungkan bobot model, konfigurasi, dan data ke dalam satu paket, menjadikannya lebih mudah diakses bagi pengguna untuk menyesuaikan dan membuat model mereka sendiri. Ollama tersedia untuk macOS, Linux, dan Windows. Ini adalah alat yang bagus jika Anda ingin bereksperimen atau menyebarkan LLM tanpa bergantung pada layanan cloud. Ollama adalah cara paling langsung, Anda hanya perlu menjalankan perintah berikut.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) adalah runtime offline di perangkat dari Microsoft untuk menjalankan model seperti Phi sepenuhnya di perangkat keras Anda sendiri — tanpa perlu langganan Azure, kunci API, atau koneksi jaringan. Ia secara otomatis memilih penyedia eksekusi terbaik yang tersedia (NPU, GPU, atau CPU) dan menyediakan endpoint kompatibel OpenAI, sehingga kode `openai`/Azure AI Inference SDK yang sudah ada dapat langsung menggunakannya dengan perubahan minimal. Lihat [dokumentasi Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) untuk memulai.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) adalah akselerator mesin pembelajaran lintas platform untuk inferensi dan pelatihan. ONNX Runtime untuk Generative AI (GENAI) adalah alat kuat yang membantu Anda menjalankan model AI generatif secara efisien di berbagai platform.

## Apa itu ONNX Runtime?
ONNX Runtime adalah proyek sumber terbuka yang memungkinkan inferensi performa tinggi dari model pembelajaran mesin. Ini mendukung model dalam format Open Neural Network Exchange (ONNX), yang merupakan standar untuk merepresentasikan model pembelajaran mesin. Inferensi ONNX Runtime dapat memungkinkan pengalaman pelanggan yang lebih cepat dan biaya lebih rendah, mendukung model dari framework pembelajaran mendalam seperti PyTorch dan TensorFlow/Keras serta perpustakaan pembelajaran mesin klasik seperti scikit-learn, LightGBM, XGBoost, dan lain-lain. ONNX Runtime kompatibel dengan perangkat keras, driver, dan sistem operasi yang berbeda, serta menyediakan performa optimal dengan memanfaatkan akselerator perangkat keras jika tersedia bersama optimasi dan transformasi graf.

## Apa itu Generative AI?
Generative AI mengacu pada sistem AI yang dapat menghasilkan konten baru, seperti teks, gambar, atau musik, berdasarkan data yang telah dilatih. Contohnya termasuk model bahasa seperti GPT-3 dan model generasi gambar seperti Stable Diffusion. Perpustakaan ONNX Runtime untuk GenAI menyediakan siklus generatif AI untuk model ONNX, termasuk inferensi dengan ONNX Runtime, pemrosesan logits, pencarian dan sampling, serta manajemen cache KV.

## ONNX Runtime untuk GENAI
ONNX Runtime untuk GENAI memperluas kemampuan ONNX Runtime untuk mendukung model AI generatif. Berikut beberapa fitur utama:

- **Dukungan Platform Luas:** Bekerja di berbagai platform, termasuk Windows, Linux, macOS, Android, dan iOS.
- **Dukungan Model:** Mendukung banyak model AI generatif populer, seperti LLaMA, GPT-Neo, BLOOM, dan lainnya.
- **Optimasi Performa:** Termasuk optimasi untuk berbagai akselerator perangkat keras seperti GPU NVIDIA, GPU AMD, dan lainnya.
- **Kemudahan Penggunaan:** Menyediakan API untuk integrasi mudah ke aplikasi, memungkinkan Anda menghasilkan teks, gambar, dan konten lain dengan kode minimal.
- Pengguna dapat memanggil metode generate() tingkat tinggi, atau menjalankan tiap iterasi model dalam sebuah loop, menghasilkan satu token sekaligus, serta secara opsional memperbarui parameter generasi di dalam loop.
- ONNX runtime juga mendukung pencarian greedy/beam dan sampling TopP, TopK untuk menghasilkan urutan token serta pemrosesan logits bawaan seperti penalti pengulangan. Anda juga dapat menambahkan penilaian khusus dengan mudah.

## Memulai
Untuk memulai dengan ONNX Runtime untuk GENAI, Anda dapat mengikuti langkah-langkah berikut:

### Instal ONNX Runtime:
```Python
pip install onnxruntime
```
### Instal Ekstensi Generative AI:
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

Selain metode referensi ONNX Runtime, Ollama, dan Foundry Local, kita juga dapat melengkapi referensi model kuantitatif berdasarkan metode referensi model yang disediakan oleh produsen berbeda. Seperti framework Apple MLX dengan Apple Metal, Qualcomm QNN dengan NPU, Intel OpenVINO dengan CPU/GPU, dll. Anda juga dapat mendapatkan lebih banyak konten dari [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Lebih Lanjut

Kita telah mempelajari dasar-dasar Phi-3/3.5 Family, tetapi untuk mempelajari lebih lanjut tentang SLM kita memerlukan lebih banyak pengetahuan. Anda dapat menemukan jawabannya di Phi-3 Cookbook. Jika Anda ingin belajar lebih banyak, silakan kunjungi [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->