# Pengenalan Model Bahasa Kecil untuk AI Generatif bagi Pemula
AI Generatif adalah bidang kecerdasan buatan yang menarik yang berfokus pada pembuatan sistem yang mampu menghasilkan konten baru. Konten ini dapat berupa teks dan gambar hingga musik dan bahkan lingkungan virtual secara keseluruhan. Salah satu aplikasi paling menarik dari AI generatif adalah dalam ranah model bahasa.

## Apa Itu Model Bahasa Kecil?

Model Bahasa Kecil (SLM) merupakan varian yang diperkecil dari model bahasa besar (LLM), memanfaatkan banyak prinsip arsitektural dan teknik LLM, sambil menunjukkan jejak komputasi yang jauh lebih kecil.

SLM adalah subset model bahasa yang dirancang untuk menghasilkan teks yang menyerupai bahasa manusia. Berbeda dengan model yang lebih besar, seperti GPT-4, SLM lebih ringkas dan efisien, membuatnya ideal untuk aplikasi di mana sumber daya komputasi terbatas. Meskipun ukurannya lebih kecil, mereka masih dapat melakukan berbagai tugas. Biasanya, SLM dibuat dengan mengompres atau mendistilasi LLM, bertujuan untuk mempertahankan sebagian besar fungsi asli dan kemampuan linguistik model tersebut. Pengurangan ukuran model ini menurunkan kompleksitas keseluruhan, membuat SLM lebih efisien baik dari segi penggunaan memori maupun kebutuhan komputasi. Meskipun telah dioptimalkan, SLM masih dapat melakukan berbagai tugas pemrosesan bahasa alami (NLP):

- Generasi Teks: Membuat kalimat atau paragraf yang koheren dan relevan secara kontekstual.
- Penyelesaian Teks: Memprediksi dan melengkapi kalimat berdasarkan prompt yang diberikan.
- Terjemahan: Mengubah teks dari satu bahasa ke bahasa lain.
- Ringkasan: Merangkum teks yang panjang menjadi ringkasan yang lebih singkat dan mudah dicerna.

Meski dengan beberapa kompromi dalam performa atau kedalaman pemahaman dibandingkan dengan model yang lebih besar.

## Bagaimana Cara Kerja Model Bahasa Kecil?
SLM dilatih menggunakan data teks dalam jumlah besar. Selama pelatihan, mereka mempelajari pola dan struktur bahasa, memungkinkan mereka untuk menghasilkan teks yang tata bahasanya benar dan sesuai konteks. Proses pelatihan meliputi:

- Pengumpulan Data: Mengumpulkan dataset teks besar dari berbagai sumber.
- Pralangkah: Membersihkan dan mengorganisasi data agar sesuai untuk pelatihan.
- Pelatihan: Menggunakan algoritme pembelajaran mesin untuk mengajarkan model bagaimana memahami dan menghasilkan teks.
- Penyesuaian: Mengatur model untuk meningkatkan performanya pada tugas-tugas tertentu.

Pengembangan SLM sejalan dengan kebutuhan yang meningkat akan model yang dapat diterapkan di lingkungan dengan sumber daya terbatas, seperti perangkat mobile atau platform edge computing, di mana LLM berskala penuh tidak praktis karena permintaan sumber daya yang tinggi. Dengan fokus pada efisiensi, SLM menyeimbangkan performa dengan aksesibilitas, memungkinkan aplikasi yang lebih luas di berbagai domain.

![slm](../../../translated_images/id/slm.4058842744d0444a.webp)

## Tujuan Pembelajaran

Dalam pelajaran ini, kami berharap dapat memperkenalkan pengetahuan tentang SLM dan menggabungkannya dengan Microsoft Phi-3 untuk mempelajari berbagai skenario dalam konten teks, visi, dan MoE.

Di akhir pelajaran ini, Anda diharapkan dapat menjawab pertanyaan-pertanyaan berikut:

- Apa itu SLM?
- Apa perbedaan antara SLM dan LLM?
- Apa itu Keluarga Microsoft Phi-3/3.5?
- Bagaimana cara menjalankan inferensi dengan Keluarga Microsoft Phi-3/3.5?

Siap? Mari kita mulai.

## Perbedaan antara Model Bahasa Besar (LLM) dan Model Bahasa Kecil (SLM)

Baik LLM maupun SLM dibangun atas prinsip dasar pembelajaran mesin probabilistik, mengikuti pendekatan serupa dalam desain arsitektur, metodologi pelatihan, proses pengumpulan data, dan teknik evaluasi model. Namun, ada beberapa faktor kunci yang membedakan kedua jenis model ini.

## Aplikasi Model Bahasa Kecil

SLM memiliki beragam aplikasi, termasuk:

- Chatbot: Memberikan dukungan pelanggan dan berinteraksi dengan pengguna secara percakapan.
- Pembuatan Konten: Membantu penulis dengan menghasilkan ide atau bahkan menyusun artikel lengkap.
- Pendidikan: Membantu siswa dengan tugas menulis atau belajar bahasa baru.
- Aksesibilitas: Membuat alat bagi individu dengan disabilitas, seperti sistem teks-ke-suara.

**Ukuran**

Perbedaan utama antara LLM dan SLM terletak pada skala model. LLM, seperti ChatGPT (GPT-4), dapat memiliki sekitar 1,76 triliun parameter, sementara SLM sumber terbuka seperti Mistral 7B dirancang dengan parameter jauh lebih sedikit—sekitar 7 miliar. Perbedaan ini terutama disebabkan oleh arsitektur model dan proses pelatihannya. Misalnya, ChatGPT menggunakan mekanisme self-attention dalam kerangka encoder-decoder, sedangkan Mistral 7B menggunakan sliding window attention yang memungkinkan pelatihan yang lebih efisien dalam model decoder saja. Variasi arsitektur ini berdampak besar pada kompleksitas dan performa model.

**Pemahaman**

SLM biasanya dioptimalkan untuk performa dalam domain tertentu, membuatnya sangat khusus tapi mungkin terbatas dalam kemampuan memberikan pemahaman konteks yang luas di berbagai bidang ilmu. Sebaliknya, LLM bertujuan meniru kecerdasan menyerupai manusia pada tingkat yang lebih menyeluruh. Dilatih pada dataset besar dan beragam, LLM dirancang untuk tampil baik di berbagai domain, menawarkan fleksibilitas dan kemampuan adaptasi yang lebih besar. Oleh karena itu, LLM lebih cocok untuk berbagai tugas lanjutan, seperti pemrosesan bahasa alami dan pemrograman.

**Komputasi**

Pelatihan dan penerapan LLM adalah proses yang memerlukan sumber daya besar, seringkali membutuhkan infrastruktur komputasi yang besar, termasuk klaster GPU berskala besar. Sebagai contoh, melatih model seperti ChatGPT dari awal mungkin memerlukan ribuan GPU dalam waktu yang lama. Sebaliknya, SLM, dengan jumlah parameter yang lebih kecil, lebih mudah diakses dari segi sumber daya komputasi. Model seperti Mistral 7B dapat dilatih dan dijalankan pada mesin lokal dengan kemampuan GPU sedang, meskipun pelatihannya tetap memerlukan beberapa jam di beberapa GPU.

**Bias**

Bias adalah isu yang dikenal pada LLM, terutama karena sifat data pelatihannya. Model-model ini sering menggunakan data mentah yang tersedia secara bebas dari internet, yang mungkin kurang merepresentasikan atau salah merepresentasikan kelompok tertentu, memasukkan pelabelan yang keliru, atau mencerminkan bias linguistik yang dipengaruhi oleh dialek, variasi geografis, dan aturan tata bahasa. Selain itu, kompleksitas arsitektur LLM bisa secara tidak sengaja memperparah bias yang mungkin tidak terdeteksi tanpa penyetelan khusus. Sebaliknya, SLM yang dilatih pada dataset domain khusus yang lebih terbatas secara inheren kurang rentan terhadap bias tersebut, meskipun tidak sepenuhnya kebal.

**Inferensi**

Ukuran yang lebih kecil dari SLM memberinya keuntungan signifikan dalam hal kecepatan inferensi, memungkinkan mereka menghasilkan output secara efisien pada perangkat keras lokal tanpa kebutuhan pemrosesan paralel yang ekstensif. Sebaliknya, LLM, karena ukuran dan kompleksitasnya, sering kali membutuhkan sumber daya komputasi paralel yang besar untuk mencapai waktu inferensi yang memadai. Kehadiran pengguna bersamaan yang banyak juga memperlambat waktu respons LLM, terutama saat digunakan dalam skala besar.

Singkatnya, meskipun LLM dan SLM memiliki dasar pembelajaran mesin yang sama, mereka berbeda signifikan dalam ukuran model, kebutuhan sumber daya, pemahaman konteks, kerentanan terhadap bias, dan kecepatan inferensi. Perbedaan ini mencerminkan kesesuaian masing-masing untuk kasus penggunaan berbeda, dengan LLM lebih serbaguna tapi berat sumber daya, dan SLM menawarkan efisiensi khusus domain dengan kebutuhan komputasi yang lebih rendah.

***Catatan: Dalam pelajaran ini, kita akan memperkenalkan SLM menggunakan Microsoft Phi-3 / 3.5 sebagai contoh.***

## Memperkenalkan Keluarga Phi-3 / Phi-3.5

Keluarga Phi-3 / 3.5 terutama menargetkan skenario aplikasi teks, visi, dan Agen (MoE):

### Phi-3 / 3.5 Instruct

Utamanya untuk generasi teks, penyelesaian chat, dan ekstraksi informasi konten, dll.

**Phi-3-mini**

Model bahasa 3.8B tersedia di Microsoft Foundry, Hugging Face, dan Ollama. Model Phi-3 jauh mengungguli model bahasa dengan ukuran sama dan lebih besar pada tolok ukur utama (lihat angka tolok ukur di bawah, angka lebih tinggi lebih baik). Phi-3-mini mengungguli model dengan ukuran dua kali lipat, sementara Phi-3-small dan Phi-3-medium mengungguli model yang lebih besar, termasuk GPT-3.5.

**Phi-3-small & medium**

Dengan hanya 7B parameter, Phi-3-small mengalahkan GPT-3.5T pada berbagai tolok ukur bahasa, penalaran, pengkodean, dan matematika.

Phi-3-medium dengan 14B parameter melanjutkan tren ini dan mengungguli Gemini 1.0 Pro.

**Phi-3.5-mini**

Kita bisa menganggapnya sebagai upgrade dari Phi-3-mini. Meski parameter tetap sama, kemampuan mendukung banyak bahasa meningkat (mendukung lebih dari 20 bahasa: Arab, Cina, Ceko, Denmark, Belanda, Inggris, Finlandia, Perancis, Jerman, Ibrani, Hungaria, Italia, Jepang, Korea, Norwegia, Polandia, Portugis, Rusia, Spanyol, Swedia, Thailand, Turki, Ukraina) dan menambah dukungan lebih kuat untuk konteks panjang.

Phi-3.5-mini dengan 3.8B parameter mengungguli model bahasa dengan ukuran sama dan setara dengan model dua kali lipat ukurannya.

### Phi-3 / 3.5 Vision

Kita bisa menganggap model Instruct dari Phi-3/3.5 sebagai kemampuan Phi untuk memahami, dan Vision adalah yang memberi Phi mata untuk memahami dunia.


**Phi-3-Vision**

Phi-3-vision, dengan hanya 4.2B parameter, melanjutkan tren ini dan mengungguli model lebih besar seperti Claude-3 Haiku dan Gemini 1.0 Pro V pada tugas penalaran visual umum, OCR, serta pemahaman tabel dan diagram.


**Phi-3.5-Vision**

Phi-3.5-Vision juga merupakan peningkatan dari Phi-3-Vision, menambah dukungan untuk banyak gambar. Anda dapat menganggapnya sebagai peningkatan penglihatan, tidak hanya bisa melihat gambar, tetapi juga video.

Phi-3.5-vision mengungguli model lebih besar seperti Claude-3.5 Sonnet dan Gemini 1.5 Flash dalam tugas OCR, pemahaman tabel dan bagan serta setara pada tugas penalaran pengetahuan visual umum. Mendukung input multi-frame, yakni melakukan penalaran pada beberapa gambar input


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** memungkinkan model untuk dipra-latih dengan jauh lebih sedikit komputasi, yang berarti Anda dapat meningkatkan skala model atau ukuran dataset secara dramatis dengan anggaran komputasi yang sama seperti model padat. Khususnya, model MoE dapat mencapai kualitas yang sama dengan model padatnya jauh lebih cepat selama pra-pelatihan.

Phi-3.5-MoE terdiri dari 16 modul ahli 3.8B. Phi-3.5-MoE dengan hanya 6.6B parameter aktif mencapai tingkat penalaran, pemahaman bahasa, dan matematika yang mirip dengan model yang jauh lebih besar.

Kita dapat menggunakan model Keluarga Phi-3/3.5 berdasarkan skenario yang berbeda. Berbeda dengan LLM, Anda bisa meluncurkan Phi-3/3.5-mini atau Phi-3/3.5-Vision pada perangkat edge.


## Cara menggunakan model Keluarga Phi-3/3.5

Kami berharap menggunakan Phi-3/3.5 dalam berbagai skenario. Berikutnya, kita akan menggunakan Phi-3/3.5 berdasarkan berbagai skenario.

![phi3](../../../translated_images/id/phi3.655208c3186ae381.webp)

### Inferensi melalui API Cloud

**Model Microsoft Foundry**

> **Catatan:** Model GitHub akan dihentikan pada akhir Juli 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) adalah penggantinya secara langsung.

Microsoft Foundry Models adalah cara paling langsung. Anda dapat dengan cepat mengakses model Phi-3/3.5-Instruct melalui katalog model Foundry. Dikombinasikan dengan Azure AI Inference SDK / OpenAI SDK, Anda dapat mengakses API melalui kode untuk menyelesaikan panggilan Phi-3/3.5-Instruct. Anda juga dapat mencoba berbagai efek melalui Playground.

- Demo: Perbandingan efek Phi-3-mini dan Phi-3.5-mini dalam skenario bahasa Cina

![phi3](../../../translated_images/id/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/id/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Atau jika kita ingin menggunakan model vision dan MoE, Anda dapat menggunakan Microsoft Foundry untuk menyelesaikan panggilan. Jika tertarik, Anda dapat membaca Phi-3 Cookbook untuk mempelajari cara memanggil Phi-3/3.5 Instruct, Vision, MoE melalui Microsoft Foundry [Klik tautan ini](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Selain katalog Model Microsoft Foundry berbasis cloud, Anda juga dapat menggunakan [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) untuk menyelesaikan panggilan terkait. Anda dapat mengunjungi NVIDIA NIM untuk menyelesaikan panggilan API Keluarga Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) adalah kumpulan layanan mikro inferensi yang dipercepat yang dirancang untuk membantu pengembang menerapkan model AI secara efisien di berbagai lingkungan, termasuk cloud, pusat data, dan workstation.

Berikut beberapa fitur utama NVIDIA NIM:

- **Kemudahan Penyebaran:** NIM memungkinkan penyebaran model AI dengan satu perintah, memudahkan integrasi ke dalam alur kerja yang ada.

- **Performa yang Dioptimalkan:** Ini memanfaatkan mesin inferensi yang sudah dioptimalkan sebelumnya dari NVIDIA, seperti TensorRT dan TensorRT-LLM, untuk memastikan latensi rendah dan throughput tinggi.
- **Skalabilitas:** NIM mendukung autoscaling di Kubernetes, memungkinkan untuk menangani beban kerja yang bervariasi secara efektif.
- **Keamanan dan Kontrol:** Organisasi dapat mempertahankan kontrol atas data dan aplikasi mereka dengan meng-host sendiri layanan mikro NIM di infrastruktur yang mereka kelola.
- **API Standar:** NIM menyediakan API standar industri, memudahkan pembangunan dan integrasi aplikasi AI seperti chatbot, asisten AI, dan lainnya.

NIM adalah bagian dari NVIDIA AI Enterprise, yang bertujuan menyederhanakan penyebaran dan operasionalisasi model AI, memastikan mereka berjalan secara efisien di GPU NVIDIA.

- Demo: Menggunakan NVIDIA NIM untuk memanggil Phi-3.5-Vision-API [[Klik tautan ini](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Menjalankan Phi-3/3.5 Secara Lokal
Inferensi terkait Phi-3, atau model bahasa apapun seperti GPT-3, merujuk pada proses menghasilkan respons atau prediksi berdasarkan input yang diterima. Ketika Anda memberikan prompt atau pertanyaan ke Phi-3, ia menggunakan jaringan saraf terlatihnya untuk menyimpulkan respons yang paling mungkin dan relevan dengan menganalisis pola dan hubungan dalam data yang telah dilatih.

**Hugging Face Transformer**
Hugging Face Transformers adalah pustaka yang kuat yang dirancang untuk pemrosesan bahasa alami (NLP) dan tugas pembelajaran mesin lainnya. Berikut beberapa poin kunci tentangnya:

1. **Model Terlatih:** Menyediakan ribuan model terlatih yang dapat digunakan untuk berbagai tugas seperti klasifikasi teks, pengenalan entitas bernama, menjawab pertanyaan, meringkas, menerjemahkan, dan menghasilkan teks.

2. **Interoperabilitas Framework:** Pustaka ini mendukung beberapa framework pembelajaran mendalam, termasuk PyTorch, TensorFlow, dan JAX. Ini memungkinkan Anda melatih model di satu framework dan menggunakannya di framework lain.

3. **Kemampuan Multimodal:** Selain NLP, Hugging Face Transformers juga mendukung tugas dalam penglihatan komputer (misalnya klasifikasi gambar, deteksi objek) dan pemrosesan audio (misalnya pengenalan suara, klasifikasi audio).

4. **Mudah Digunakan:** Pustaka ini menawarkan API dan alat untuk dengan mudah mengunduh dan menyetel model, membuatnya dapat diakses oleh pemula maupun pakar.

5. **Komunitas dan Sumber Daya:** Hugging Face memiliki komunitas yang hidup dan dokumentasi, tutorial, serta panduan yang luas untuk membantu pengguna memulai dan memaksimalkan pustaka ini.
[dokumentasi resmi](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) atau [repositori GitHub mereka](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Ini adalah metode yang paling sering digunakan, tetapi juga memerlukan akselerasi GPU. Bagaimanapun, skenario seperti Vision dan MoE membutuhkan banyak perhitungan, yang akan sangat lambat di CPU jika tidak dikwantisasi.


- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-Instruct [Klik tautan ini](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-Vision [Klik tautan ini](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-MoE [Klik tautan ini](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) adalah platform yang dirancang untuk memudahkan menjalankan model bahasa besar (LLM) secara lokal di perangkat Anda. Ia mendukung berbagai model seperti Llama 3.1, Phi 3, Mistral, dan Gemma 2, dan lainnya. Platform ini menyederhanakan proses dengan mengemas bobot model, konfigurasi, dan data menjadi satu paket, sehingga lebih mudah diakses untuk pengguna menyesuaikan dan membuat model mereka sendiri. Ollama tersedia untuk macOS, Linux, dan Windows. Ini adalah alat yang bagus jika Anda ingin bereksperimen dengan atau menyebarkan LLM tanpa bergantung pada layanan cloud. Ollama adalah cara paling langsung, Anda hanya perlu menjalankan perintah berikut.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) adalah runtime offline, di perangkat dari Microsoft untuk menjalankan model seperti Phi sepenuhnya di perangkat keras Anda sendiri - tidak memerlukan langganan Azure, kunci API, atau koneksi jaringan. Ia secara otomatis memilih penyedia eksekusi terbaik yang tersedia (NPU, GPU, atau CPU) dan menyediakan endpoint yang kompatibel dengan OpenAI, sehingga kode SDK `openai`/Azure AI Inference yang ada dapat diarahkan ke sini dengan perubahan minimal. Lihat [dokumentasi Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) untuk memulai.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) adalah akselerator pembelajaran mesin lintas platform untuk inferensi dan pelatihan. ONNX Runtime untuk Generative AI (GENAI) adalah alat yang kuat yang membantu Anda menjalankan model AI generatif secara efisien di berbagai platform.

## Apa itu ONNX Runtime?
ONNX Runtime adalah proyek sumber terbuka yang memungkinkan inferensi performa tinggi untuk model pembelajaran mesin. Ini mendukung model dalam format Open Neural Network Exchange (ONNX), yang merupakan standar untuk mewakili model pembelajaran mesin. Inferensi ONNX Runtime dapat memungkinkan pengalaman pelanggan yang lebih cepat dan biaya lebih rendah, mendukung model dari berbagai framework pembelajaran mendalam seperti PyTorch dan TensorFlow/Keras serta perpustakaan pembelajaran mesin klasik seperti scikit-learn, LightGBM, XGBoost, dan lainnya. ONNX Runtime kompatibel dengan berbagai perangkat keras, driver, dan sistem operasi, serta memberikan performa optimal dengan memanfaatkan akselerator perangkat keras sesuai kebutuhan bersama optimisasi dan transformasi grafik.

## Apa itu Generative AI?
Generative AI mengacu pada sistem AI yang dapat menghasilkan konten baru, seperti teks, gambar, atau musik, berdasarkan data yang telah mereka latih. Contohnya termasuk model bahasa seperti GPT-3 dan model generasi gambar seperti Stable Diffusion. Perpustakaan ONNX Runtime untuk GenAI menyediakan loop AI generatif untuk model ONNX, termasuk inferensi dengan ONNX Runtime, pemrosesan logits, pencarian dan sampling, serta manajemen cache KV.

## ONNX Runtime untuk GENAI
ONNX Runtime untuk GENAI memperluas kemampuan ONNX Runtime untuk mendukung model AI generatif. Berikut beberapa fitur utama:

- **Dukungan Platform Luas:** Berfungsi di berbagai platform, termasuk Windows, Linux, macOS, Android, dan iOS.
- **Dukungan Model:** Mendukung banyak model AI generatif populer, seperti LLaMA, GPT-Neo, BLOOM, dan lainnya.
- **Optimasi Performa:** Meliputi optimasi untuk berbagai akselerator perangkat keras seperti GPU NVIDIA, GPU AMD, dan lainnya.
- **Kemudahan Penggunaan:** Menyediakan API untuk integrasi mudah ke dalam aplikasi, memungkinkan Anda menghasilkan teks, gambar, dan konten lain dengan kode minimal.
- Pengguna dapat memanggil metode generate() tingkat tinggi, atau menjalankan iterasi model dalam loop, menghasilkan satu token sekaligus, dan secara opsional memperbarui parameter generasi di dalam loop.
- ONNX runtime juga mendukung greedy/beam search dan sampling TopP, TopK untuk menghasilkan rangkaian token serta pemrosesan logits bawaan seperti penalti pengulangan. Anda juga dapat dengan mudah menambahkan scoring kustom.

## Memulai
Untuk memulai dengan ONNX Runtime untuk GENAI, Anda dapat mengikuti langkah-langkah berikut:

### Pasang ONNX Runtime:
```Python
pip install onnxruntime
```
### Pasang Ekstensi Generative AI:
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

Selain metode referensi ONNX Runtime, Ollama, dan Foundry Local, kita juga dapat melengkapi referensi model kuantisasi berdasarkan metode referensi model dari berbagai produsen. Seperti Apple MLX framework dengan Apple Metal, Qualcomm QNN dengan NPU, Intel OpenVINO dengan CPU/GPU, dan lain-lain. Anda juga dapat mendapatkan lebih banyak konten dari [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Selengkapnya

Kita telah mempelajari dasar-dasar Keluarga Phi-3/3.5, tetapi untuk mempelajari lebih lanjut tentang SLM kita memerlukan lebih banyak pengetahuan. Anda dapat menemukan jawabannya di Phi-3 Cookbook. Jika ingin mempelajari lebih jauh, silakan kunjungi [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->