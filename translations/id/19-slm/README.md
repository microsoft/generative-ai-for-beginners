# Pengantar Model Bahasa Kecil untuk AI Generatif bagi Pemula
AI Generatif adalah bidang kecerdasan buatan yang menarik yang berfokus pada pembuatan sistem yang mampu menghasilkan konten baru. Konten ini bisa berupa teks dan gambar hingga musik dan bahkan lingkungan virtual secara keseluruhan. Salah satu aplikasi AI generatif yang paling menarik adalah dalam ranah model bahasa.

## Apa Itu Model Bahasa Kecil?

Model Bahasa Kecil (SLM) merupakan varian yang diperkecil dari model bahasa besar (LLM), yang memanfaatkan banyak prinsip arsitektural dan teknik dari LLM, sambil menunjukkan jejak komputasi yang jauh lebih kecil.

SLM adalah subkelompok model bahasa yang dirancang untuk menghasilkan teks yang menyerupai manusia. Berbeda dengan rekan mereka yang lebih besar seperti GPT-4, SLM lebih ringkas dan efisien, sehingga ideal untuk aplikasi yang sumber dayanya terbatas. Meskipun berukuran lebih kecil, mereka masih dapat melakukan berbagai tugas. Biasanya, SLM dibangun dengan mengompresi atau mendistilasi LLM, dengan tujuan mempertahankan sebagian besar fungsi asli model dan kemampuan linguistiknya. Pengurangan ukuran model ini menurunkan kompleksitas keseluruhan, sehingga SLM lebih efisien dalam penggunaan memori dan kebutuhan komputasi. Meski dengan optimasi ini, SLM masih mampu melakukan berbagai tugas pemrosesan bahasa alami (NLP):

- Generasi Teks: Membuat kalimat atau paragraf yang koheren dan relevan secara kontekstual.
- Penyelesaian Teks: Memprediksi dan melengkapi kalimat berdasarkan prompt yang diberikan.
- Terjemahan: Mengonversi teks dari satu bahasa ke bahasa lain.
- Ringkasan: Merangkum potongan teks panjang menjadi ringkasan yang lebih pendek dan mudah dipahami.

Meskipun ada beberapa kompromi dalam hal performa atau kedalaman pemahaman dibandingkan dengan yang lebih besar.

## Bagaimana Cara Kerja Model Bahasa Kecil?
SLM dilatih menggunakan sejumlah besar data teks. Selama pelatihan, mereka mempelajari pola dan struktur bahasa, memungkinkan mereka menghasilkan teks yang baik secara tata bahasa dan sesuai konteks. Proses pelatihan melibatkan:

- Pengumpulan Data: Mengumpulkan dataset besar teks dari berbagai sumber.
- Pra-pemrosesan: Membersihkan dan mengorganisasi data agar cocok untuk pelatihan.
- Pelatihan: Menggunakan algoritma pembelajaran mesin untuk mengajarkan model bagaimana memahami dan menghasilkan teks.
- Penyesuaian Akhir: Mengatur model untuk meningkatkan performanya pada tugas tertentu.

Pengembangan SLM sejalan dengan kebutuhan yang meningkat akan model yang dapat diterapkan di lingkungan dengan sumber daya terbatas, seperti perangkat seluler atau platform edge computing, di mana LLM skala penuh mungkin tidak praktis karena kebutuhan sumber daya yang besar. Dengan fokus pada efisiensi, SLM menyeimbangkan performa dengan keterjangkauan, memungkinkan penerapan yang lebih luas di berbagai domain.

![slm](../../../translated_images/id/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Tujuan Pembelajaran

Dalam pelajaran ini, kami berharap dapat memperkenalkan pengetahuan tentang SLM dan menggabungkannya dengan Microsoft Phi-3 untuk mempelajari berbagai skenario dalam konten teks, visi, dan MoE.

Pada akhir pelajaran ini, Anda seharusnya dapat menjawab pertanyaan berikut:

- Apa itu SLM?
- Apa perbedaan antara SLM dan LLM?
- Apa itu Keluarga Microsoft Phi-3/3.5?
- Bagaimana cara menjalankan inferensi dengan Keluarga Microsoft Phi-3/3.5?

Siap? Mari kita mulai.

## Perbedaan antara Model Bahasa Besar (LLM) dan Model Bahasa Kecil (SLM)

Baik LLM maupun SLM dibangun berdasarkan prinsip dasar pembelajaran mesin probabilistik, mengikuti pendekatan yang serupa dalam desain arsitektur, metodologi pelatihan, proses generasi data, dan teknik evaluasi model. Namun, ada beberapa faktor kunci yang membedakan kedua jenis model ini.

## Aplikasi Model Bahasa Kecil

SLM memiliki berbagai aplikasi, termasuk:

- Chatbot: Memberikan dukungan pelanggan dan berinteraksi dengan pengguna secara percakapan.
- Pembuatan Konten: Membantu penulis dengan menghasilkan ide atau bahkan draft artikel lengkap.
- Pendidikan: Membantu siswa dengan tugas menulis atau belajar bahasa baru.
- Aksesibilitas: Membuat alat untuk individu dengan disabilitas, seperti sistem teks-ke-suara.

**Ukuran**
  
Perbedaan utama antara LLM dan SLM terletak pada skala model. LLM, seperti ChatGPT (GPT-4), dapat memiliki sekitar 1,76 triliun parameter, sedangkan SLM open-source seperti Mistral 7B dirancang dengan jumlah parameter yang jauh lebih sedikit—sekitar 7 miliar. Perbedaan ini terutama disebabkan oleh perbedaan arsitektur model dan proses pelatihan. Misalnya, ChatGPT menggunakan mekanisme self-attention dalam kerangka encoder-decoder, sementara Mistral 7B menggunakan sliding window attention yang memungkinkan pelatihan yang lebih efisien dalam model decoder-only. Variasi arsitektural ini memiliki implikasi mendalam bagi kompleksitas dan performa model-model ini.

**Pemahaman**

SLM biasanya dioptimalkan untuk performa dalam domain tertentu, menjadikannya sangat khusus namun mungkin terbatas dalam kemampuannya memberikan pemahaman kontekstual luas di berbagai bidang pengetahuan. Sebaliknya, LLM bertujuan untuk mensimulasikan kecerdasan mirip manusia secara lebih komprehensif. Dilatih pada dataset besar dan beragam, LLM dirancang agar performa baik di berbagai domain, menawarkan fleksibilitas dan adaptabilitas yang lebih besar. Oleh sebab itu, LLM lebih cocok untuk berbagai tugas lanjutan, seperti pemrosesan bahasa alami dan pemrograman.

**Komputasi**

Pelatihan dan penerapan LLM adalah proses yang memerlukan sumber daya besar, seringkali membutuhkan infrastruktur komputasi signifikan, termasuk klaster GPU besar. Contohnya, pelatihan model seperti ChatGPT dari awal dapat memerlukan ribuan GPU selama waktu yang lama. Sebaliknya, SLM, dengan jumlah parameter yang lebih kecil, lebih mudah diakses dalam hal sumber daya komputasi. Model seperti Mistral 7B dapat dilatih dan dijalankan di mesin lokal dengan GPU yang cukup memadai, meskipun pelatihan memerlukan beberapa jam dengan beberapa GPU.

**Bias**

Bias adalah isu yang diketahui pada LLM, terutama akibat sifat data pelatihan. Model ini sering mengandalkan data mentah terbuka dari internet, yang mungkin kurang atau salah merepresentasikan kelompok tertentu, memasukkan label yang salah, atau mencerminkan bias linguistik yang dipengaruhi oleh dialek, variasi geografis, dan aturan tata bahasa. Selain itu, kompleksitas arsitektur LLM dapat secara tidak sengaja memperburuk bias, yang mungkin tidak disadari tanpa penyesuaian halus yang cermat. Di sisi lain, SLM, yang dilatih pada dataset yang lebih terbatas dan spesifik domain, cenderung kurang rentan terhadap bias seperti itu, walaupun tidak sepenuhnya kebal.

**Inferensi**

Ukuran SLM yang lebih kecil memberikan keuntungan signifikan dalam kecepatan inferensi, memungkinkan mereka menghasilkan output secara efisien pada perangkat keras lokal tanpa memerlukan pemrosesan paralel yang luas. Sebaliknya, LLM, karena ukuran dan kompleksitasnya, sering membutuhkan sumber daya komputasi paralel besar untuk mencapai waktu inferensi yang dapat diterima. Kehadiran banyak pengguna bersamaan juga memperlambat waktu respons LLM, terutama ketika diterapkan secara skala besar.

Secara ringkas, meskipun LLM dan SLM berbagi dasar pembelajaran mesin, mereka berbeda signifikan dalam hal ukuran model, kebutuhan sumber daya, pemahaman kontekstual, kerentanan terhadap bias, dan kecepatan inferensi. Perbedaan ini mencerminkan kesesuaian mereka masing-masing untuk berbagai kasus penggunaan, dengan LLM lebih serbaguna tapi berat sumber daya, dan SLM menawarkan efisiensi spesifik domain dengan kebutuhan komputasi yang lebih rendah.

***Catatan: Dalam pelajaran ini, kita akan memperkenalkan SLM menggunakan Microsoft Phi-3 / 3.5 sebagai contoh.***

## Perkenalan Keluarga Phi-3 / Phi-3.5

Keluarga Phi-3 / 3.5 terutama ditargetkan untuk skenario aplikasi teks, visi, dan Agen (MoE):

### Phi-3 / 3.5 Instruct

Terutama untuk generasi teks, penyelesaian chat, dan ekstraksi informasi konten, dan lain-lain.

**Phi-3-mini**

Model bahasa 3.8B tersedia di Microsoft Foundry, Hugging Face, dan Ollama. Model Phi-3 secara signifikan mengungguli model bahasa dengan ukuran yang sama dan lebih besar pada tolok ukur utama (lihat angka tolok ukur di bawah, angka yang lebih tinggi lebih baik). Phi-3-mini mengungguli model dua kali ukurannya, sementara Phi-3-small dan Phi-3-medium mengungguli model yang lebih besar, termasuk GPT-3.5.

**Phi-3-small & medium**

Dengan hanya 7B parameter, Phi-3-small mengalahkan GPT-3.5T dalam berbagai tolok ukur bahasa, penalaran, pemrograman, dan matematika.

Phi-3-medium dengan 14B parameter melanjutkan tren ini dan mengungguli Gemini 1.0 Pro.

**Phi-3.5-mini**

Kita bisa menganggapnya sebagai peningkatan dari Phi-3-mini. Meskipun parameter tetap sama, model ini meningkatkan kemampuan mendukung banyak bahasa (mendukung lebih dari 20 bahasa: Arab, Cina, Ceko, Denmark, Belanda, Inggris, Finlandia, Prancis, Jerman, Ibrani, Hungaria, Italia, Jepang, Korea, Norwegia, Polandia, Portugis, Rusia, Spanyol, Swedia, Thailand, Turki, Ukraina) dan menambahkan dukungan yang lebih kuat untuk konteks panjang.

Phi-3.5-mini dengan 3.8B parameter mengungguli model bahasa dengan ukuran yang sama dan setara dengan model dua kali ukurannya.

### Phi-3 / 3.5 Vision

Kita dapat memandang model Instruct Phi-3/3.5 sebagai kemampuan Phi untuk memahami, dan Vision adalah apa yang memberi Phi mata untuk memahami dunia.


**Phi-3-Vision**

Phi-3-vision, dengan hanya 4.2B parameter, melanjutkan tren ini dan mengungguli model yang lebih besar seperti Claude-3 Haiku dan Gemini 1.0 Pro V pada tugas penalaran visual umum, OCR, dan pemahaman tabel dan diagram.


**Phi-3.5-Vision**

Phi-3.5-Vision juga merupakan peningkatan dari Phi-3-Vision, menambahkan dukungan untuk banyak gambar. Anda bisa menganggapnya sebagai peningkatan pada penglihatan, tidak hanya dapat melihat gambar, tetapi juga video.

Phi-3.5-vision mengungguli model yang lebih besar seperti Claude-3.5 Sonnet dan Gemini 1.5 Flash di seluruh tugas OCR, pemahaman tabel dan grafik dan setara pada tugas penalaran pengetahuan visual umum. Mendukung input multi-frame, yaitu melakukan penalaran pada beberapa gambar input


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** memungkinkan model dilatih dengan komputasi yang jauh lebih sedikit, yang berarti Anda dapat dengan dramatis meningkatkan ukuran model atau dataset dengan anggaran komputasi yang sama seperti model padat (dense). Secara khusus, model MoE harus mencapai kualitas yang sama dengan model padat serupa jauh lebih cepat selama pra-pelatihan.

Phi-3.5-MoE terdiri dari 16 modul ahli 3.8B. Phi-3.5-MoE dengan hanya 6.6B parameter aktif mencapai tingkat penalaran, pemahaman bahasa, dan matematika yang serupa dengan model yang jauh lebih besar.

Kita dapat menggunakan model Keluarga Phi-3 / 3.5 berdasarkan skenario yang berbeda. Tidak seperti LLM, Anda dapat menerapkan Phi-3/3.5-mini atau Phi-3/3.5-Vision di perangkat edge.


## Cara menggunakan model Keluarga Phi-3 / 3.5

Kami berharap dapat menggunakan Phi-3/3.5 dalam berbagai skenario. Selanjutnya, kita akan menggunakan Phi-3/3.5 berdasarkan skenario yang berbeda.

![phi3](../../../translated_images/id/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inferensi melalui Cloud API

**Model Microsoft Foundry**

> **Catatan:** GitHub Models akan dihentikan pada akhir Juli 2026. [Model Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) adalah penggantinya secara langsung.

Microsoft Foundry Models adalah cara paling langsung. Anda dapat dengan cepat mengakses model Phi-3/3.5-Instruct melalui katalog model Foundry. Dikombinasikan dengan Azure AI Inference SDK / OpenAI SDK, Anda dapat mengakses API melalui kode untuk menyelesaikan panggilan Phi-3/3.5-Instruct. Anda juga bisa menguji berbagai efek melalui Playground.

- Demo: Perbandingan efek Phi-3-mini dan Phi-3.5-mini dalam skenario bahasa Mandarin

![phi3](../../../translated_images/id/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/id/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Atau jika kita ingin menggunakan model visi dan MoE, Anda dapat menggunakan Microsoft Foundry untuk menyelesaikan panggilan. Jika tertarik, Anda dapat membaca Phi-3 Cookbook untuk belajar cara memanggil Phi-3/3.5 Instruct, Vision, MoE melalui Microsoft Foundry [Klik tautan ini](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Selain katalog Microsoft Foundry Models berbasis cloud, Anda juga dapat menggunakan [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) untuk menyelesaikan panggilan terkait. Anda dapat mengunjungi NVIDIA NIM untuk menyelesaikan panggilan API Keluarga Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) adalah kumpulan microservices inferensi yang dipercepat yang dirancang untuk membantu pengembang menerapkan model AI secara efisien di berbagai lingkungan, termasuk cloud, pusat data, dan workstation.

Berikut adalah beberapa fitur utama NVIDIA NIM:

- **Kemudahan Penerapan:** NIM memungkinkan penerapan model AI dengan satu perintah, membuatnya mudah diintegrasikan ke dalam alur kerja yang sudah ada.
- **Performa Optimal:** Menggunakan mesin inferensi yang telah dioptimasi sebelumnya oleh NVIDIA, seperti TensorRT dan TensorRT-LLM, untuk memastikan latensi rendah dan throughput tinggi.
- **Skalabilitas:** NIM mendukung autoscaling di Kubernetes, memungkinkan penanganan beban kerja yang bervariasi secara efektif.
- **Keamanan dan Kontrol:** Organisasi dapat mempertahankan kendali atas data dan aplikasi mereka dengan meng-hosting sendiri microservices NIM di infrastruktur yang mereka kelola.
- **API Standar:** NIM menyediakan API standar industri, memudahkan pembangunan dan integrasi aplikasi AI seperti chatbot, asisten AI, dan lainnya.

NIM merupakan bagian dari NVIDIA AI Enterprise, yang bertujuan untuk menyederhanakan penyebaran dan operasionalisasi model AI, memastikan mereka berjalan efisien pada GPU NVIDIA.

- Demo: Menggunakan NVIDIA NIM untuk memanggil Phi-3.5-Vision-API  [[Klik tautan ini](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Menjalankan Phi-3/3.5 Secara Lokal
Inferensi terkait dengan Phi-3, atau model bahasa apa pun seperti GPT-3, mengacu pada proses menghasilkan respons atau prediksi berdasarkan input yang diterima. Saat Anda memberikan prompt atau pertanyaan ke Phi-3, ia menggunakan jaringan saraf yang telah dilatih untuk memperkirakan respons yang paling mungkin dan relevan dengan menganalisis pola dan hubungan dalam data yang dilatihnya.

**Hugging Face Transformer**
Hugging Face Transformers adalah perpustakaan yang kuat yang dirancang untuk pemrosesan bahasa alami (NLP) dan tugas pembelajaran mesin lainnya. Berikut beberapa poin utama tentangnya:

1. **Model Pra-latih**: Menyediakan ribuan model pra-latih yang dapat digunakan untuk berbagai tugas seperti klasifikasi teks, pengenalan entitas bernama, penjawaban pertanyaan, summarization, penerjemahan, dan pembuatan teks.

2. **Interoperabilitas Framework**: Perpustakaan ini mendukung beberapa framework pembelajaran mendalam, termasuk PyTorch, TensorFlow, dan JAX. Ini memungkinkan Anda melatih model di satu framework dan menggunakannya di framework lain.

3. **Kemampuan Multimodal**: Selain NLP, Hugging Face Transformers juga mendukung tugas di penglihatan komputer (misalnya klasifikasi gambar, deteksi objek) dan pemrosesan audio (misalnya pengenalan suara, klasifikasi audio).

4. **Kemudahan Penggunaan**: Perpustakaan menawarkan API dan alat untuk mengunduh dan menyetel model dengan mudah, membuatnya dapat diakses baik oleh pemula maupun ahli.

5. **Komunitas dan Sumber Daya**: Hugging Face memiliki komunitas yang aktif dan dokumentasi, tutorial, serta panduan yang luas untuk membantu pengguna memulai dan memaksimalkan penggunaan perpustakaan.
[dokumentasi resmi](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) atau [repositori GitHub mereka](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Ini adalah metode yang paling umum digunakan, tetapi juga memerlukan akselerasi GPU. Lagi pula, skenario seperti Vision dan MoE memerlukan banyak perhitungan, yang akan sangat lambat pada CPU jika tidak dikuantisasi.


- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-Instruct [Klik tautan ini](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-Vision [Klik tautan ini](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-MoE [Klik tautan ini](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) adalah platform yang dirancang untuk memudahkan menjalankan model bahasa besar (LLM) secara lokal di mesin Anda. Mendukung berbagai model seperti Llama 3.1, Phi 3, Mistral, dan Gemma 2, antara lain. Platform ini menyederhanakan proses dengan mengemas bobot model, konfigurasi, dan data ke dalam satu paket, membuatnya lebih mudah diakses untuk pengguna yang ingin menyesuaikan dan membuat model mereka sendiri. Ollama tersedia untuk macOS, Linux, dan Windows. Ini alat yang bagus jika Anda ingin bereksperimen atau menyebarkan LLM tanpa bergantung pada layanan cloud. Ollama adalah cara paling langsung, Anda hanya perlu mengeksekusi perintah berikut.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) adalah runtime offline milik Microsoft untuk menjalankan model seperti Phi sepenuhnya pada perangkat keras Anda sendiri - tanpa langganan Azure, kunci API, atau koneksi jaringan diperlukan. Ini secara otomatis memilih penyedia eksekusi terbaik yang tersedia (NPU, GPU, atau CPU) dan menyediakan endpoint kompatibel OpenAI, sehingga kode `openai`/Azure AI Inference SDK yang ada bisa mengarah ke sini dengan sedikit perubahan. Lihat [dokumentasi Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) untuk mulai menggunakan.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Atau gunakan SDK langsung dalam Python:

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
ONNX Runtime adalah proyek sumber terbuka yang memungkinkan inferensi berkinerja tinggi untuk model pembelajaran mesin. Mendukung model dalam format Open Neural Network Exchange (ONNX), yang merupakan standar untuk mewakili model pembelajaran mesin. Inferensi ONNX Runtime dapat mempercepat pengalaman pelanggan dan mengurangi biaya, mendukung model dari framework pembelajaran mendalam seperti PyTorch dan TensorFlow/Keras serta perpustakaan pembelajaran mesin klasik seperti scikit-learn, LightGBM, XGBoost, dll. ONNX Runtime kompatibel dengan berbagai perangkat keras, driver, dan sistem operasi, serta menyediakan kinerja optimal dengan memanfaatkan akselerator perangkat keras bila memungkinkan bersama dengan optimasi dan transformasi grafik.

## Apa itu AI Generatif?
AI generatif mengacu pada sistem AI yang dapat menghasilkan konten baru, seperti teks, gambar, atau musik, berdasarkan data yang telah dilatih. Contohnya termasuk model bahasa seperti GPT-3 dan model generasi gambar seperti Stable Diffusion. Perpustakaan ONNX Runtime untuk GenAI menyediakan loop AI generatif untuk model ONNX, termasuk inferensi dengan ONNX Runtime, pemrosesan logit, pencarian dan sampling, serta manajemen cache KV.

## ONNX Runtime untuk GENAI
ONNX Runtime untuk GENAI memperluas kemampuan ONNX Runtime untuk mendukung model AI generatif. Berikut beberapa fitur utama:

- **Dukungan Platform Luas:** Berfungsi di berbagai platform, termasuk Windows, Linux, macOS, Android, dan iOS.
- **Dukungan Model:** Mendukung banyak model AI generatif populer, seperti LLaMA, GPT-Neo, BLOOM, dan lainnya.
- **Optimasi Kinerja:** Menyertakan optimasi untuk berbagai akselerator perangkat keras seperti GPU NVIDIA, GPU AMD, dan lainnya.
- **Kemudahan Penggunaan:** Menyediakan API untuk integrasi mudah ke aplikasi, memungkinkan Anda menghasilkan teks, gambar, dan konten lainnya dengan kode minimal.
- Pengguna dapat memanggil metode generate() tingkat tinggi, atau menjalankan setiap iterasi model dalam loop, menghasilkan satu token pada satu waktu, dan opsional memperbarui parameter generasi di dalam loop.
- ONNX runtime juga mendukung pencarian greedy/beam dan sampling TopP, TopK untuk menghasilkan urutan token serta pemrosesan logit bawaan seperti penalti pengulangan. Anda juga dapat dengan mudah menambahkan penilaian khusus.

## Memulai
Untuk memulai dengan ONNX Runtime untuk GENAI, Anda dapat mengikuti langkah-langkah ini:

### Instal ONNX Runtime:
```Python
pip install onnxruntime
```
### Instal Ekstensi Generatif AI:
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
### Demo:Menggunakan ONNX Runtime GenAI untuk memanggil Phi-3.5-Vision


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

Selain metode referensi ONNX Runtime, Ollama, dan Foundry Local, kita juga dapat melengkapi referensi model kuantitatif berdasarkan metode referensi model yang disediakan oleh berbagai produsen. Seperti kerangka kerja Apple MLX dengan Apple Metal, Qualcomm QNN dengan NPU, Intel OpenVINO dengan CPU/GPU, dll. Anda juga dapat mendapatkan lebih banyak konten dari [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Lebih Lanjut

Kita telah mempelajari dasar-dasar keluarga Phi-3/3.5, tetapi untuk mempelajari lebih lanjut tentang SLM kita memerlukan pengetahuan lebih. Anda dapat menemukan jawaban di Phi-3 Cookbook. Jika Anda ingin belajar lebih banyak, silakan kunjungi [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->