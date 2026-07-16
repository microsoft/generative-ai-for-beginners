# Pengantar Model Bahasa Kecil untuk AI Generatif bagi Pemula  
AI generatif adalah bidang kecerdasan buatan yang menarik yang berfokus pada penciptaan sistem yang mampu menghasilkan konten baru. Konten ini bisa berupa teks dan gambar hingga musik dan bahkan seluruh lingkungan virtual. Salah satu aplikasi paling menarik dari AI generatif adalah di ranah model bahasa.  

## Apa Itu Model Bahasa Kecil?  

Model Bahasa Kecil (SLM) merupakan varian skala kecil dari model bahasa besar (LLM), memanfaatkan banyak prinsip arsitektural dan teknik dari LLM, sambil menunjukkan jejak komputasi yang jauh lebih kecil.  

SLM adalah subset dari model bahasa yang dirancang untuk menghasilkan teks yang menyerupai tulisan manusia. Berbeda dengan rekan-rekan besarnya, seperti GPT-4, SLM lebih ringkas dan efisien, membuatnya ideal untuk aplikasi di mana sumber daya komputasi terbatas. Meskipun ukurannya kecil, mereka masih bisa melakukan berbagai tugas. Biasanya, SLM dibuat dengan mengompres atau mendistilasi LLM, dengan tujuan mempertahankan sebagian besar fungsi dan kemampuan linguistik model asli. Pengurangan ukuran model ini mengurangi kompleksitas secara keseluruhan, membuat SLM lebih efisien dalam hal penggunaan memori dan kebutuhan komputasi. Meskipun dioptimalkan demikian, SLM masih dapat melakukan berbagai tugas pemrosesan bahasa alami (NLP):  

- Pembuatan Teks: Membuat kalimat atau paragraf yang koheren dan relevan secara kontekstual.  
- Penyelesaian Teks: Memprediksi dan melengkapi kalimat berdasarkan prompt yang diberikan.  
- Penerjemahan: Mengubah teks dari satu bahasa ke bahasa lain.  
- Merangkum: Memadatkan potongan teks panjang menjadi ringkasan yang lebih pendek dan mudah dicerna.  

Meskipun ada beberapa kompromi dalam performa atau kedalaman pemahaman dibandingkan dengan model yang lebih besar.  

## Bagaimana Cara Kerja Model Bahasa Kecil?  
SLM dilatih pada sejumlah besar data teks. Selama pelatihan, mereka belajar pola dan struktur bahasa, memungkinkan mereka menghasilkan teks yang tata bahasanya benar dan sesuai konteks. Proses pelatihan meliputi:  

- Pengumpulan Data: Mengumpulkan dataset teks besar dari berbagai sumber.  
- Pra-pemrosesan: Membersihkan dan mengorganisir data agar cocok untuk pelatihan.  
- Pelatihan: Menggunakan algoritma pembelajaran mesin untuk mengajarkan model memahami dan menghasilkan teks.  
- Penyesuaian: Mengatur model agar meningkatkan performa pada tugas khusus.  

Pengembangan SLM selaras dengan kebutuhan yang meningkat akan model yang dapat diterapkan pada lingkungan dengan sumber daya terbatas, seperti perangkat mobile atau platform komputasi edge, di mana LLM skala penuh mungkin tidak praktis karena permintaan sumber dayanya yang besar. Dengan fokus pada efisiensi, SLM menyeimbangkan performa dan aksesibilitas, memungkinkan aplikasi yang lebih luas di berbagai bidang.  

![slm](../../../translated_images/id/slm.4058842744d0444a.webp)  

## Tujuan Pembelajaran  

Dalam pelajaran ini, kami berharap mengenalkan pengetahuan tentang SLM dan menggabungkannya dengan Microsoft Phi-3 untuk mempelajari berbagai skenario dalam konten teks, visi, dan MoE.  

Pada akhir pelajaran ini, Anda seharusnya dapat menjawab pertanyaan-pertanyaan berikut:  

- Apa itu SLM?  
- Apa perbedaan antara SLM dan LLM?  
- Apa itu keluarga Microsoft Phi-3/3.5?  
- Bagaimana cara menjalankan inferensi dengan keluarga Microsoft Phi-3/3.5?  

Siap? Mari kita mulai.  

## Perbedaan antara Model Bahasa Besar (LLM) dan Model Bahasa Kecil (SLM)  

Baik LLM maupun SLM dibangun atas prinsip dasar pembelajaran mesin probabilistik, mengikuti pendekatan serupa dalam desain arsitektur, metodologi pelatihan, proses pembuatan data, dan teknik evaluasi model. Namun, beberapa faktor kunci membedakan kedua tipe model ini.  

## Aplikasi Model Bahasa Kecil  

SLM memiliki berbagai aplikasi, termasuk:  

- Chatbot: Memberikan dukungan pelanggan dan berinteraksi dengan pengguna secara percakapan.  
- Pembuatan Konten: Membantu penulis dengan menghasilkan ide atau bahkan menyusun artikel lengkap.  
- Pendidikan: Membantu siswa dalam tugas menulis atau belajar bahasa baru.  
- Aksesibilitas: Membuat alat untuk individu dengan disabilitas, seperti sistem teks-ke-suara.  

**Ukuran**  
 
Perbedaan utama antara LLM dan SLM terletak pada skala model. LLM, seperti ChatGPT (GPT-4), dapat memiliki sekitar 1,76 triliun parameter, sementara SLM open-source seperti Mistral 7B dirancang dengan parameter jauh lebih sedikit—sekitar 7 miliar. Perbedaan ini terutama disebabkan oleh arsitektur model dan proses pelatihan yang berbeda. Misalnya, ChatGPT menggunakan mekanisme self-attention dalam kerangka encoder-decoder, sedangkan Mistral 7B menggunakan sliding window attention, yang memungkinkan pelatihan lebih efisien dalam model decoder saja. Perbedaan arsitektur ini berdampak besar pada kompleksitas dan performa model-model ini.  

**Pemahaman**  

SLM biasanya dioptimalkan untuk kinerja dalam domain tertentu, membuatnya sangat khusus tapi mungkin terbatas kemampuannya untuk menyediakan pemahaman konteks luas di berbagai bidang pengetahuan. Sebaliknya, LLM bertujuan mensimulasikan kecerdasan seperti manusia secara lebih menyeluruh. Dilatih pada dataset besar dan beragam, LLM dirancang agar baik dalam berbagai domain, menawarkan fleksibilitas dan adaptabilitas yang lebih besar. Oleh karena itu, LLM lebih cocok untuk beragam tugas lanjutan, seperti pemrosesan bahasa alami dan pemrograman.  

**Komputasi**  

Pelatihan dan penerapan LLM adalah proses yang memakan banyak sumber daya, sering memerlukan infrastruktur komputasi besar, termasuk klaster GPU skala besar. Misalnya, melatih model seperti ChatGPT dari awal bisa memerlukan ribuan GPU selama periode waktu yang lama. Sebaliknya, SLM, dengan jumlah parameter yang lebih kecil, lebih mudah diakses dari segi sumber daya komputasi. Model seperti Mistral 7B bisa dilatih dan dijalankan di mesin lokal dengan kemampuan GPU sedang, meski pelatihan masih membutuhkan beberapa jam di beberapa GPU.  

**Bias**  

Bias adalah masalah yang dikenal pada LLM, terutama karena sifat data pelatihannya. Model ini sering mengandalkan data mentah yang tersedia secara bebas dari internet, yang mungkin kurang merepresentasikan atau salah merepresentasikan kelompok tertentu, memperkenalkan label yang salah, atau mencerminkan bias linguistik yang dipengaruhi dialek, variasi geografis, dan aturan tata bahasa. Selain itu, kompleksitas arsitektur LLM dapat secara tidak sengaja memperburuk bias, yang mungkin tidak terdeteksi tanpa penyesuaian yang cermat. Di sisi lain, SLM, yang dilatih pada dataset domain tertentu yang lebih terbatas, secara inheren kurang rentan terhadap bias tersebut, meskipun tidak sepenuhnya kebal.  

**Inferensi**  

Ukuran SLM yang lebih kecil memberikan keuntungan signifikan dalam kecepatan inferensi, memungkinkan mereka menghasilkan output secara efisien pada perangkat lokal tanpa kebutuhan proses paralel yang luas. Sebaliknya, LLM, karena ukuran dan kompleksitasnya, sering memerlukan sumber daya komputasi paralel besar untuk mencapai waktu inferensi yang dapat diterima. Keberadaan banyak pengguna secara bersamaan juga memperlambat waktu respons LLM, terutama jika diterapkan secara skala besar.  

Singkatnya, meskipun LLM dan SLM memiliki dasar yang sama dalam pembelajaran mesin, mereka sangat berbeda dalam ukuran model, kebutuhan sumber daya, pemahaman konteks, kerentanan terhadap bias, dan kecepatan inferensi. Perbedaan ini mencerminkan kesesuaian mereka untuk berbagai kasus penggunaan, dengan LLM lebih serbaguna tapi berat sumber daya, dan SLM menawarkan efisiensi domain-spesifik dengan tuntutan komputasi yang lebih rendah.  

***Catatan: Dalam pelajaran ini, kami akan mengenalkan SLM menggunakan Microsoft Phi-3 / 3.5 sebagai contoh.***  

## Mengenal Keluarga Phi-3 / Phi-3.5  

Keluarga Phi-3 / 3.5 terutama menargetkan skenario aplikasi teks, visi, dan Agen (MoE):  

### Phi-3 / 3.5 Instruct  

Terutama untuk pembuatan teks, penyelesaian chat, dan ekstraksi informasi konten, dll.  

**Phi-3-mini**  

Model bahasa 3,8 miliar parameter tersedia di Microsoft Foundry, Hugging Face, dan Ollama. Model Phi-3 secara signifikan mengungguli model bahasa dengan ukuran yang sama dan lebih besar pada tolok ukur utama (lihat angka tolok ukur di bawah, angka lebih tinggi lebih baik). Phi-3-mini mengungguli model dua kali ukurannya, sedangkan Phi-3-small dan Phi-3-medium mengungguli model yang lebih besar, termasuk GPT-3.5.  

**Phi-3-small & medium**  

Dengan hanya 7 miliar parameter, Phi-3-small mengalahkan GPT-3.5T pada berbagai tolok ukur bahasa, penalaran, pengkodean, dan matematika.  

Phi-3-medium dengan 14 miliar parameter melanjutkan tren ini dan mengungguli Gemini 1.0 Pro.  

**Phi-3.5-mini**  

Kita bisa menganggapnya sebagai peningkatan dari Phi-3-mini. Walaupun parameternya tetap sama, model ini meningkatkan kemampuan untuk mendukung banyak bahasa (mendukung 20+ bahasa: Arab, Cina, Ceko, Danish, Belanda, Inggris, Finlandia, Prancis, Jerman, Ibrani, Hungaria, Italia, Jepang, Korea, Norwegia, Polandia, Portugis, Rusia, Spanyol, Swedia, Thailand, Turki, Ukraina) dan menambahkan dukungan lebih kuat untuk konteks panjang.  

Phi-3.5-mini dengan 3,8 miliar parameter mengungguli model bahasa dengan ukuran sama dan setara dengan model dua kali ukurannya.  

### Phi-3 / 3.5 Vision  

Kita bisa menganggap model Instruct Phi-3/3.5 sebagai kemampuan Phi untuk memahami, dan Vision adalah yang memberi Phi mata untuk memahami dunia.  


**Phi-3-Vision**  

Phi-3-vision, dengan hanya 4,2 miliar parameter, melanjutkan tren ini dan mengungguli model yang lebih besar seperti Claude-3 Haiku dan Gemini 1.0 Pro V pada tugas penalaran visual umum, OCR, dan pemahaman tabel serta diagram.  


**Phi-3.5-Vision**  

Phi-3.5-Vision juga merupakan peningkatan dari Phi-3-Vision, menambahkan dukungan untuk gambar ganda. Anda bisa menganggapnya sebagai peningkatan dalam visi, tidak hanya bisa melihat gambar, tetapi juga video.  

Phi-3.5-vision mengungguli model yang lebih besar seperti Claude-3.5 Sonnet dan Gemini 1.5 Flash dalam tugas OCR, pemahaman tabel dan grafik, dan setara pada tugas penalaran pengetahuan visual umum. Mendukung input multi-frame, yaitu melakukan penalaran pada banyak gambar input  


### Phi-3.5-MoE  

***Mixture of Experts (MoE)*** memungkinkan model untuk dilatih dengan komputasi jauh lebih sedikit, yang berarti Anda dapat memperbesar ukuran model atau dataset secara dramatis dengan anggaran komputasi yang sama dengan model padat. Secara khusus, model MoE harus mencapai kualitas yang sama dengan padanannya yang padat lebih cepat selama pra-pelatihan.  

Phi-3.5-MoE terdiri dari 16 modul ahli 3,8 miliar. Phi-3.5-MoE dengan hanya 6,6 miliar parameter aktif mencapai tingkat penalaran, pemahaman bahasa, dan matematika yang serupa dengan model yang jauh lebih besar.  

Kita dapat menggunakan model keluarga Phi-3/3.5 berdasarkan berbagai skenario. Berbeda dengan LLM, Anda bisa men-deploy Phi-3/3.5-mini atau Phi-3/3.5-Vision pada perangkat edge.  


## Cara Menggunakan Model Keluarga Phi-3/3.5  

Kami berharap menggunakan Phi-3/3.5 dalam berbagai skenario. Selanjutnya, kami akan menggunakan Phi-3/3.5 berdasarkan berbagai skenario.  

![phi3](../../../translated_images/id/phi3.655208c3186ae381.webp)  

### Inferensi lewat API Cloud  

**Microsoft Foundry Models**  

> **Catatan:** GitHub Models akan dihentikan pada akhir Juli 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) adalah penggantinya secara langsung.  

Microsoft Foundry Models adalah cara paling langsung. Anda dapat dengan cepat mengakses model Phi-3/3.5-Instruct melalui katalog model Foundry. Dikombinasikan dengan Azure AI Inference SDK / OpenAI SDK, Anda dapat mengakses API melalui kode untuk menyelesaikan panggilan Phi-3/3.5-Instruct. Anda juga dapat menguji berbagai efek melalui Playground.  

- Demo: Perbandingan efek Phi-3-mini dan Phi-3.5-mini dalam skenario bahasa Mandarin  

![phi3](../../../translated_images/id/gh1.126c6139713b622b.webp)  

![phi35](../../../translated_images/id/gh2.07d7985af66f178d.webp)  


**Microsoft Foundry**  

Atau jika kita ingin menggunakan model visi dan MoE, Anda dapat menggunakan Microsoft Foundry untuk menyelesaikan panggilan. Jika tertarik, Anda dapat membaca Phi-3 Cookbook untuk belajar cara memanggil Phi-3/3.5 Instruct, Vision, MoE melalui Microsoft Foundry [Klik tautan ini](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)  


**NVIDIA NIM**  

Selain katalog Microsoft Foundry Models berbasis cloud, Anda juga dapat menggunakan [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) untuk menyelesaikan panggilan terkait. Anda dapat mengunjungi NVIDIA NIM untuk menyelesaikan panggilan API keluarga Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) adalah sekumpulan layanan mikro inferensi yang dipercepat dirancang untuk membantu pengembang menerapkan model AI secara efisien di berbagai lingkungan, termasuk cloud, pusat data, dan workstation.  

Berikut beberapa fitur utama NVIDIA NIM:  

- **Kemudahan Deploy:** NIM memungkinkan penerapan model AI hanya dengan satu perintah, membuatnya mudah diintegrasikan ke dalam alur kerja yang sudah ada.  

- **Kinerja Dioptimalkan:** Ia memanfaatkan mesin inference yang telah dioptimalkan sebelumnya dari NVIDIA, seperti TensorRT dan TensorRT-LLM, untuk memastikan latensi rendah dan throughput tinggi.
- **Skalabilitas:** NIM mendukung autoscaling di Kubernetes, memungkinkan penanganan beban kerja yang bervariasi secara efektif.
- **Keamanan dan Kontrol:** Organisasi dapat mempertahankan kontrol atas data dan aplikasi mereka dengan menghosting sendiri layanan mikro NIM pada infrastruktur yang mereka kelola sendiri.
- **API Standar:** NIM menyediakan API standar industri, sehingga mudah untuk membangun dan mengintegrasikan aplikasi AI seperti chatbot, asisten AI, dan lainnya.

NIM adalah bagian dari NVIDIA AI Enterprise, yang bertujuan untuk menyederhanakan penerapan dan operasionalisasi model AI, memastikan mereka berjalan secara efisien di GPU NVIDIA.

- Demo: Menggunakan NVIDIA NIM untuk memanggil Phi-3.5-Vision-API  [[Klik tautan ini](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Menjalankan Phi-3/3.5 Secara Lokal
Inference terkait Phi-3, atau model bahasa seperti GPT-3, mengacu pada proses menghasilkan respons atau prediksi berdasarkan input yang diterimanya. Ketika Anda memberikan prompt atau pertanyaan kepada Phi-3, ia menggunakan jaringan neural terlatihnya untuk menyimpulkan respons yang paling mungkin dan relevan dengan menganalisis pola dan hubungan dalam data yang telah dilatih.

**Hugging Face Transformer**
Hugging Face Transformers adalah perpustakaan yang kuat yang dirancang untuk pengolahan bahasa alami (NLP) dan tugas pembelajaran mesin lainnya. Berikut beberapa poin penting tentangnya:

1. **Model Pra-latih**: Menyediakan ribuan model yang sudah dilatih sebelumnya yang dapat digunakan untuk berbagai tugas seperti klasifikasi teks, pengenalan entitas bernama, menjawab pertanyaan, meringkas, menerjemahkan, dan menghasilkan teks.

2. **Interoperabilitas Kerangka Kerja:** Perpustakaan mendukung beberapa kerangka kerja pembelajaran mendalam, termasuk PyTorch, TensorFlow, dan JAX. Ini memungkinkan Anda melatih model di satu kerangka dan menggunakannya di kerangka lain.

3. **Kemampuan Multimodal:** Selain NLP, Hugging Face Transformers juga mendukung tugas di bidang penglihatan komputer (misalnya klasifikasi gambar, deteksi objek) dan pemrosesan audio (misalnya pengenalan suara, klasifikasi audio).

4. **Kemudahan Penggunaan:** Perpustakaan menyediakan API dan alat untuk dengan mudah mengunduh dan menyetel model, membuatnya dapat diakses bagi pemula maupun ahli.

5. **Komunitas dan Sumber Daya:** Hugging Face memiliki komunitas yang hidup dan dokumentasi luas, tutorial, serta panduan untuk membantu pengguna memulai dan memanfaatkan perpustakaan secara maksimal.
[dokumentasi resmi](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) atau repositori [GitHub mereka](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Ini adalah metode yang paling umum digunakan, tetapi juga membutuhkan akselerasi GPU. Bagaimanapun, skenario seperti Vision dan MoE memerlukan banyak perhitungan, yang akan sangat lambat pada CPU jika tidak diquantize.


- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-Instruct [Klik tautan ini](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-Vision [Klik tautan ini](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-MoE [Klik tautan ini](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) adalah platform yang dirancang untuk mempermudah menjalankan model bahasa besar (LLM) secara lokal di mesin Anda. Ia mendukung berbagai model seperti Llama 3.1, Phi 3, Mistral, dan Gemma 2, di antaranya. Platform ini menyederhanakan proses dengan menggabungkan bobot model, konfigurasi, dan data ke dalam satu paket, sehingga lebih mudah bagi pengguna untuk menyesuaikan dan membuat model mereka sendiri. Ollama tersedia untuk macOS, Linux, dan Windows. Ini adalah alat yang sangat baik jika Anda ingin bereksperimen atau menerapkan LLM tanpa bergantung pada layanan cloud. Ollama adalah cara paling langsung, Anda hanya perlu menjalankan perintah berikut.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) adalah runtime offline milik Microsoft untuk dijalankan secara lokal di perangkat Anda guna menjalankan model seperti Phi sepenuhnya di perangkat keras Anda sendiri - tanpa langganan Azure, kunci API, atau koneksi jaringan. Ia secara otomatis memilih penyedia eksekusi terbaik yang tersedia (NPU, GPU, atau CPU) dan menyediakan endpoint yang kompatibel dengan OpenAI, sehingga kode SDK `openai`/Azure AI Inference yang sudah ada dapat diarahkan ke sini dengan perubahan minimal. Lihat [dokumentasi Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) untuk memulai.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) adalah akselerator pembelajaran mesin lintas platform untuk inference dan pelatihan. ONNX Runtime untuk Generative AI (GENAI) adalah alat yang kuat yang membantu Anda menjalankan model AI generatif secara efisien di berbagai platform.

## Apa itu ONNX Runtime?
ONNX Runtime adalah proyek sumber terbuka yang memungkinkan inference berkinerja tinggi dari model pembelajaran mesin. Ia mendukung model dalam format Open Neural Network Exchange (ONNX), yang merupakan standar untuk merepresentasikan model pembelajaran mesin. Inference ONNX Runtime dapat memungkinkan pengalaman pelanggan yang lebih cepat dan biaya lebih rendah, mendukung model dari kerangka pembelajaran mendalam seperti PyTorch dan TensorFlow/Keras serta pustaka pembelajaran mesin klasik seperti scikit-learn, LightGBM, XGBoost, dll. ONNX Runtime kompatibel dengan perangkat keras, driver, dan sistem operasi yang berbeda, serta memberikan performa optimal dengan memanfaatkan akselerator perangkat keras bila memungkinkan bersama dengan optimasi dan transformasi grafik.

## Apa itu Generative AI?
Generative AI merujuk pada sistem AI yang dapat menghasilkan konten baru, seperti teks, gambar, atau musik, berdasarkan data yang telah dilatih. Contohnya termasuk model bahasa seperti GPT-3 dan model generasi gambar seperti Stable Diffusion. Perpustakaan ONNX Runtime untuk GenAI menyediakan loop generatif AI untuk model ONNX, termasuk inference dengan ONNX Runtime, pemrosesan logits, pencarian dan sampling, serta manajemen cache KV.

## ONNX Runtime untuk GENAI
ONNX Runtime untuk GENAI memperluas kemampuan ONNX Runtime untuk mendukung model AI generatif. Berikut beberapa fitur utama:

- **Dukungan Platform Luas:** Berfungsi di berbagai platform, termasuk Windows, Linux, macOS, Android, dan iOS.
- **Dukungan Model:** Mendukung banyak model AI generatif populer, seperti LLaMA, GPT-Neo, BLOOM, dan lainnya.
- **Optimasi Kinerja:** Termasuk optimasi untuk berbagai akselerator perangkat keras seperti GPU NVIDIA, GPU AMD, dan lainnya.
- **Kemudahan Penggunaan:** Menyediakan API untuk integrasi mudah ke dalam aplikasi, memungkinkan Anda menghasilkan teks, gambar, dan konten lainnya dengan kode minimal.
- Pengguna dapat memanggil metode generate() tingkat tinggi, atau menjalankan setiap iterasi model dalam loop, menghasilkan satu token sekaligus, dan opsi memperbarui parameter generasi di dalam loop.
- ONNX runtime juga mendukung pencarian greedy/beam dan sampling TopP, TopK untuk menghasilkan urutan token serta pemrosesan logits bawaan seperti penalti pengulangan. Anda juga dapat dengan mudah menambahkan penilaian khusus.

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

Selain metode referensi ONNX Runtime, Ollama, dan Foundry Local, kita juga dapat melengkapi referensi model kuantitatif berdasarkan metode referensi model yang disediakan oleh produsen berbeda. Seperti kerangka kerja Apple MLX dengan Apple Metal, Qualcomm QNN dengan NPU, Intel OpenVINO dengan CPU/GPU, dll. Anda juga dapat mendapatkan lebih banyak konten dari [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Selengkapnya

Kita telah mempelajari dasar-dasar Keluarga Phi-3/3.5, tetapi untuk mempelajari lebih lanjut tentang SLM kita memerlukan pengetahuan tambahan. Anda bisa menemukan jawabannya di Phi-3 Cookbook. Jika ingin belajar lebih banyak, silakan kunjungi [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->