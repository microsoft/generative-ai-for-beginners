# Pengenalan kepada Model Bahasa Kecil untuk AI Generatif untuk Pemula
AI Generatif adalah bidang kecerdasan buatan yang menarik yang memfokuskan pada penciptaan sistem yang mampu menghasilkan kandungan baru. Kandungan ini boleh berupa teks dan imej sehingga muzik dan bahkan seluruh persekitaran maya. Salah satu aplikasi paling menarik AI generatif adalah dalam bidang model bahasa.

## Apakah Model Bahasa Kecil?

Model Bahasa Kecil (SLM) mewakili varian berskala kecil daripada model bahasa besar (LLM), menggunakan banyak prinsip arkitektur dan teknik LLM, sambil menunjukkan jejak pengkomputeran yang jauh lebih rendah.

SLM adalah subset model bahasa yang direka untuk menjana teks yang menyerupai manusia. Berbeza dengan rakan besar mereka, seperti GPT-4, SLM lebih kecil dan cekap, menjadikannya sesuai untuk aplikasi di mana sumber pengkomputeran terhad. Walaupun saiznya lebih kecil, mereka masih boleh melaksanakan pelbagai tugas. Biasanya, SLM dibina dengan memampatkan atau mendistilasi LLM, bertujuan untuk mengekalkan sebahagian besar fungsi asal model dan keupayaan linguistik. Pengurangan saiz model ini mengurangkan kerumitan secara keseluruhan, menjadikan SLM lebih cekap dari segi penggunaan memori dan keperluan pengkomputeran. Walaupun dengan pengoptimuman ini, SLM masih dapat melaksanakan pelbagai tugas pemprosesan bahasa semulajadi (NLP):

- Penjanaan Teks: Mencipta ayat atau perenggan yang koheren dan relevan secara konteks.
- Penyempurnaan Teks: Meramalkan dan melengkapkan ayat berdasarkan prompt yang diberikan.
- Terjemahan: Menukar teks dari satu bahasa ke bahasa lain.
- Penjumlahan: Memampatkan teks panjang menjadi ringkasan yang lebih pendek dan mudah difahami.

Walaupun dengan beberapa kompromi dalam prestasi atau kedalaman pemahaman berbanding rakan besar mereka.

## Bagaimana Model Bahasa Kecil Berfungsi?
SLM dilatih menggunakan sejumlah besar data teks. Semasa latihan, mereka mempelajari corak dan struktur bahasa, membolehkan mereka menjana teks yang gramatis betul dan sesuai secara konteks. Proses latihan melibatkan:

- Pengumpulan Data: Mengumpul dataset besar teks dari pelbagai sumber.
- Pra-pemprosesan: Membersihkan dan menyusun data agar sesuai untuk latihan.
- Latihan: Menggunakan algoritma pembelajaran mesin untuk mengajar model bagaimana memahami dan menjana teks.
- Penalaan Halus: Melaraskan model untuk memperbaiki prestasinya pada tugas tertentu.

Pembangunan SLM sejajar dengan keperluan yang meningkat untuk model yang boleh dikerahkan di persekitaran dengan sumber terhad, seperti peranti mudah alih atau platform pengkomputeran tepi, di mana LLM berskala penuh mungkin tidak praktikal kerana permintaan sumber yang tinggi. Dengan menumpukan pada kecekapan, SLM mengimbangi prestasi dengan kemudahan capaian, membolehkan penggunaan yang lebih meluas dalam pelbagai bidang.

![slm](../../../translated_images/ms/slm.4058842744d0444a.webp)

## Objektif Pembelajaran

Dalam pelajaran ini, kami berharap dapat memperkenalkan pengetahuan tentang SLM dan menggabungkannya dengan Microsoft Phi-3 untuk mempelajari pelbagai senario dalam kandungan teks, visi dan MoE.

Pada akhir pelajaran ini, anda harus dapat menjawab soalan berikut:

- Apakah itu SLM?
- Apakah perbezaan antara SLM dan LLM?
- Apakah Keluarga Microsoft Phi-3/3.5?
- Bagaimana menjalankan inferens dengan Keluarga Microsoft Phi-3/3.5?

Sedia? Mari kita mulakan.

## Perbezaan antara Model Bahasa Besar (LLM) dan Model Bahasa Kecil (SLM)

Kedua-dua LLM dan SLM dibina berdasarkan prinsip asas pembelajaran mesin probabilistik, mengikuti pendekatan yang serupa dalam reka bentuk arkitektur, metodologi latihan, proses penjanaan data, dan teknik penilaian model. Walau bagaimanapun, beberapa faktor penting membezakan kedua-dua jenis model ini.

## Aplikasi Model Bahasa Kecil

SLM mempunyai pelbagai aplikasi, termasuk:

- Chatbot: Menyediakan sokongan pelanggan dan berinteraksi dengan pengguna secara perbualan.
- Penciptaan Kandungan: Membantu penulis dengan menjana idea atau draf keseluruhan artikel.
- Pendidikan: Membantu pelajar dalam tugasan menulis atau belajar bahasa baru.
- Aksesibiliti: Mencipta alat untuk individu dengan kecacatan, seperti sistem teks ke suara.

**Saiz**
  
Perbezaan utama antara LLM dan SLM ialah pada skala model. LLM, seperti ChatGPT (GPT-4), boleh mempunyai anggaran 1.76 trilion parameter, manakala SLM sumber terbuka seperti Mistral 7B direka dengan parameter jauh lebih sedikit—kira-kira 7 bilion. Perbezaan ini terutama disebabkan oleh perbezaan dalam arkitektur model dan proses latihan. Sebagai contoh, ChatGPT menggunakan mekanisme perhatian kendiri dalam kerangka pengekod-penyahkod, manakala Mistral 7B menggunakan perhatian tetingkap gelongsor, yang membolehkan latihan lebih cekap dalam model hanya penyahkod. Variasi arkitektur ini mempunyai implikasi mendalam bagi kerumitan dan prestasi model-model ini.

**Pemahaman**

SLM biasanya dioptimumkan untuk prestasi dalam domain tertentu, menjadikannya sangat khusus tetapi mungkin terhad dalam kemampuan untuk memberikan pemahaman konteks yang luas merentasi pelbagai bidang pengetahuan. Sebaliknya, LLM bertujuan meniru kecerdasan seperti manusia pada tahap yang lebih menyeluruh. Dilatih menggunakan dataset besar dan pelbagai, LLM direka untuk berprestasi baik merentasi pelbagai domain, menawarkan lebih serba guna dan kebolehsuaian. Oleh itu, LLM lebih sesuai untuk pelbagai tugas hiliran, seperti pemprosesan bahasa semulajadi dan pengaturcaraan.

**Pengkomputeran**

Latihan dan penyebaran LLM memerlukan sumber yang besar, sering kali memerlukan infrastruktur pengkomputeran yang signifikan, termasuk kluster GPU berskala besar. Contohnya, melatih model seperti ChatGPT dari awal mungkin memerlukan ribuan GPU dalam tempoh yang panjang. Berbeza dengan itu, SLM, dengan jumlah parameter yang lebih kecil, lebih mudah diakses dari segi sumber pengkomputeran. Model seperti Mistral 7B boleh dilatih dan dijalankan pada mesin tempatan yang dilengkapi GPU sederhana, walaupun latihan masih memerlukan beberapa jam menggunakan beberapa GPU.

**Bias**

Bias adalah isu yang diketahui dalam LLM, terutama disebabkan oleh sifat data latihan. Model ini sering bergantung pada data mentah yang tersedia secara terbuka dari internet, yang mungkin menggambarkan kelompok tertentu secara kurang atau salah, memasukkan pelabelan yang salah, atau mencerminkan bias linguistik yang dipengaruhi oleh dialek, variasi geografi, dan peraturan tatabahasa. Selain itu, kerumitan arkitektur LLM boleh tanpa disedari memburukkan bias, yang mungkin tidak disedari tanpa penalaan halus yang teliti. Sebaliknya, SLM yang dilatih pada dataset yang lebih terhad dan domain-spesifik, secara asasnya kurang terdedah kepada bias sebegini, walaupun tidak terkecuali daripada mereka.

**Inferens**

Saiz yang dikurangkan pada SLM memberi mereka kelebihan ketara dari segi kelajuan inferens, membolehkan mereka menghasilkan output secara cekap pada perkakasan tempatan tanpa memerlukan pemprosesan selari yang meluas. Sebaliknya, LLM, kerana saiz dan kerumitannya, sering memerlukan sumber pengkomputeran selari yang besar untuk mencapai masa inferens yang boleh diterima. Kehadiran pelbagai pengguna serentak juga melambatkan masa tindak balas LLM, terutamanya apabila dikerahkan dalam skala besar.

Kesimpulannya, walaupun LLM dan SLM berkongsi asas pembelajaran mesin yang sama, mereka sangat berbeza dari segi saiz model, keperluan sumber, pemahaman konteks, kecenderungan kepada bias, dan kelajuan inferens. Perbezaan ini mencerminkan kesesuaian masing-masing untuk kegunaan berbeza, dengan LLM lebih serba guna tetapi memerlukan sumber tinggi, dan SLM menawarkan kecekapan domain-spesifik dengan keperluan pengkomputeran yang dikurangkan.

***Nota: Dalam pelajaran ini, kami akan memperkenalkan SLM menggunakan Microsoft Phi-3 / 3.5 sebagai contoh.***

## Pengenalan kepada Keluarga Phi-3 / Phi-3.5

Keluarga Phi-3 / 3.5 terutamanya menyasarkan senario aplikasi teks, visi, dan Agen (MoE):

### Phi-3 / 3.5 Instruct

Terutamanya untuk penjanaan teks, penyempurnaan perbualan, dan pengektrakan maklumat kandungan, dan lain-lain.

**Phi-3-mini**

Model bahasa 3.8B tersedia di Microsoft Foundry, Hugging Face, dan Ollama. Model Phi-3 dengan ketara mengatasi model bahasa bersaiz sama dan lebih besar dalam penanda aras utama (lihat nombor penanda aras di bawah, nombor lebih tinggi lebih baik). Phi-3-mini mengatasi model yang dua kali lebih besar, manakala Phi-3-small dan Phi-3-medium mengatasi model lebih besar, termasuk GPT-3.5.

**Phi-3-small & medium**

Dengan hanya 7B parameter, Phi-3-small mengalahkan GPT-3.5T dalam pelbagai penanda aras bahasa, penaakulan, pengekodan, dan matematik.

Phi-3-medium dengan 14B parameter meneruskan trend ini dan mengatasi Gemini 1.0 Pro.

**Phi-3.5-mini**

Kita boleh menganggapnya sebagai peningkatan kepada Phi-3-mini. Walaupun parameter kekal sama, ia meningkatkan keupayaan menyokong pelbagai bahasa (menyokong 20+ bahasa: Arab, Cina, Ceko, Denmark, Belanda, Inggeris, Finland, Perancis, Jerman, Ibrani, Hungary, Itali, Jepun, Korea, Norway, Poland, Portugis, Rusia, Sepanyol, Sweden, Thai, Turki, Ukraine) dan menambah sokongan lebih kuat untuk konteks panjang.

Phi-3.5-mini dengan 3.8B parameter mengatasi model bahasa saiz sama dan setanding dengan model dua kali saiznya.

### Phi-3 / 3.5 Vision

Kita boleh menganggap model Instruct Phi-3/3.5 sebagai keupayaan Phi untuk memahami, dan Vision adalah apa yang memberi Phi ‘mata’ untuk memahami dunia.


**Phi-3-Vision**

Phi-3-vision, dengan hanya 4.2B parameter, meneruskan trend ini dan mengatasi model lebih besar seperti Claude-3 Haiku dan Gemini 1.0 Pro V dalam tugasan penaakulan visual am, OCR, serta pemahaman jadual dan rajah.


**Phi-3.5-Vision**

Phi-3.5-Vision juga merupakan peningkatan kepada Phi-3-Vision, menambah sokongan untuk berbilang imej. Anda boleh menganggapnya sebagai peningkatan dalam visi, bukan sahaja boleh melihat gambar, malah video juga.

Phi-3.5-vision mengatasi model lebih besar seperti Claude-3.5 Sonnet dan Gemini 1.5 Flash dalam tugasan OCR, pemahaman jadual dan carta dan setanding dalam tugasan penaakulan pengetahuan visual am. Menyokong input berbilang bingkai, iaitu melakukan penaakulan pada pelbagai imej input.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** membolehkan model dilatih terlebih dahulu dengan jauh kurang pengiraan, yang bermaksud anda boleh meningkatkan skala model atau dataset dengan bajet pengiraan yang sama seperti model padat. Khususnya, model MoE harus mencapai kualiti yang sama dengan padanan padatnya dengan lebih cepat semasa pra-latihan.

Phi-3.5-MoE terdiri daripada 16 modul pakar 3.8B. Phi-3.5-MoE dengan hanya 6.6B parameter aktif mencapai tahap penaakulan, pemahaman bahasa, dan matematik yang sama seperti model yang jauh lebih besar.

Kita boleh menggunakan model Keluarga Phi-3/3.5 berdasarkan pelbagai senario. Berbeza dengan LLM, anda boleh menggunakan Phi-3/3.5-mini atau Phi-3/3.5-Vision pada peranti tepi.


## Cara menggunakan model Keluarga Phi-3/3.5

Kami berharap menggunakan Phi-3/3.5 dalam pelbagai senario. Seterusnya, kita akan menggunakan Phi-3/3.5 berdasarkan pelbagai senario.

![phi3](../../../translated_images/ms/phi3.655208c3186ae381.webp)

### Inferens melalui API Awan

**Model Microsoft Foundry**

> **Nota:** Model GitHub akan dihentikan pada akhir Julai 2026. [Model Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) adalah pengganti langsung.

Model Microsoft Foundry adalah cara paling langsung. Anda boleh dengan cepat mengakses model Phi-3/3.5-Instruct melalui katalog model Foundry. Digabungkan dengan Azure AI Inference SDK / OpenAI SDK, anda boleh mengakses API melalui kod untuk menyempurnakan panggilan Phi-3/3.5-Instruct. Anda juga boleh menguji pelbagai kesan melalui Playground.

- Demo: Perbandingan kesan Phi-3-mini dan Phi-3.5-mini dalam senario Cina

![phi3](../../../translated_images/ms/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/ms/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Atau jika kita mahu menggunakan model visi dan MoE, anda boleh menggunakan Microsoft Foundry untuk melengkapkan panggilan. Jika berminat, anda boleh membaca Buku Masakan Phi-3 untuk belajar bagaimana memanggil Phi-3/3.5 Instruct, Vision, MoE melalui Microsoft Foundry [Klik pautan ini](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Selain katalog model Microsoft Foundry berasaskan awan, anda juga boleh menggunakan [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) untuk melengkapkan panggilan berkaitan. Anda boleh melawat NVIDIA NIM untuk melengkapkan panggilan API Keluarga Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) adalah set mikrosistem inferens yang dipercepatkan direka untuk membantu pembangun mengerahkan model AI dengan cekap merentasi pelbagai persekitaran, termasuk awan, pusat data, dan stesen kerja.

Berikut beberapa ciri utama NVIDIA NIM:

- **Kemudahan Penyebaran:** NIM membolehkan penyebaran model AI dengan satu perintah, menjadikannya mudah untuk disepadukan dalam aliran kerja sedia ada.

- **Prestasi Optimum:** Ia menggunakan enjin inferens yang telah dioptimumkan oleh NVIDIA, seperti TensorRT dan TensorRT-LLM, untuk memastikan latensi rendah dan throughput tinggi.
- **Skalabiliti:** NIM menyokong autoscaling pada Kubernetes, membenarkannya mengendalikan beban kerja yang berbeza dengan berkesan.
- **Keselamatan dan Kawalan:** Organisasi boleh mengekalkan kawalan ke atas data dan aplikasi mereka dengan menghoskan sendiri mikroservis NIM pada infrastruktur yang diurus sendiri.
- **API Standard:** NIM menyediakan API standard industri, memudahkan pembinaan dan integrasi aplikasi AI seperti chatbot, pembantu AI, dan banyak lagi.

NIM adalah sebahagian daripada NVIDIA AI Enterprise, yang bertujuan untuk mempermudah pelaksanaan dan pengoperasian model AI, memastikan ia berjalan dengan cekap pada GPU NVIDIA.

- Demo: Menggunakan NVIDIA NIM untuk memanggil Phi-3.5-Vision-API  [[Klik pautan ini](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Menjalankan Phi-3/3.5 Secara Tempatan
Inferens yang berkaitan dengan Phi-3, atau mana-mana model bahasa seperti GPT-3, merujuk kepada proses menjana respons atau ramalan berdasarkan input yang diterimanya. Apabila anda memberikan arahan atau soalan kepada Phi-3, ia menggunakan rangkaian neural terlatihnya untuk meneka respons yang paling mungkin dan relevan dengan menganalisis corak dan hubungan dalam data yang telah dilatih.

**Hugging Face Transformer**
Hugging Face Transformers adalah perpustakaan yang kuat direka untuk pemprosesan bahasa semula jadi (NLP) dan tugas pembelajaran mesin lain. Berikut adalah beberapa poin penting mengenainya:

1. **Model Terlatih Awal**: Ia menyediakan ribuan model terlatih awal yang boleh digunakan untuk pelbagai tugas seperti klasifikasi teks, pengecaman entiti bernama, menjawab soalan, ringkasan, terjemahan, dan penjanaan teks.

2. **Keserasian Rangka Kerja:** Perpustakaan ini menyokong pelbagai rangka kerja pembelajaran mendalam, termasuk PyTorch, TensorFlow, dan JAX. Ini membolehkan anda melatih model dalam satu rangka kerja dan menggunakannya di rangka kerja lain.

3. **Kebolehan Multimodal:** Selain NLP, Hugging Face Transformers juga menyokong tugas dalam penglihatan komputer (contohnya, klasifikasi imej, pengesanan objek) dan pemprosesan audio (contohnya, pengecaman pertuturan, klasifikasi audio).

4. **Mudah Digunakan:** Perpustakaan ini menawarkan API dan alat untuk memuat turun dan menyesuaikan model dengan mudah, menjadikannya dapat diakses oleh pemula dan pakar.

5. **Komuniti dan Sumber:** Hugging Face mempunyai komuniti yang aktif dan dokumentasi terperinci, tutorial, dan panduan untuk membantu pengguna bermula dan memanfaatkan perpustakaan dengan optimum.
[dokumentasi rasmi](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) atau repositori [GitHub mereka](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Ini adalah kaedah yang paling kerap digunakan, tetapi ia juga memerlukan pemajuan GPU. Lagipun, senario seperti Vision dan MoE memerlukan banyak pengiraan, yang akan menjadi sangat perlahan di CPU jika tidak dikualitikan.


- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-Instruct [Klik pautan ini](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-Vision [Klik pautan ini](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-MoE [Klik pautan ini](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) adalah platform yang direka untuk memudahkan menjalankan model bahasa besar (LLM) secara tempatan pada mesin anda. Ia menyokong pelbagai model seperti Llama 3.1, Phi 3, Mistral, dan Gemma 2, antara lain. Platform ini mempermudah proses dengan menggabungkan berat model, konfigurasi, dan data ke dalam satu pakej, menjadikannya lebih mudah bagi pengguna untuk menyesuaikan dan mencipta model mereka sendiri. Ollama tersedia untuk macOS, Linux, dan Windows. Ia adalah alat yang hebat jika anda ingin bereksperimen dengan atau melancarkan LLM tanpa bergantung pada perkhidmatan awan. Ollama adalah cara yang paling langsung, anda hanya perlu melaksanakan arahan berikut.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) adalah runtime luar talian pada peranti Microsoft untuk menjalankan model seperti Phi sepenuhnya pada perkakasan anda sendiri - tiada langganan Azure, kunci API, atau sambungan rangkaian diperlukan. Ia secara automatik memilih penyedia pelaksanaan terbaik yang tersedia (NPU, GPU, atau CPU) dan mendedahkan titik akhir yang serasi dengan OpenAI, jadi kod SDK inferens AI `openai`/Azure yang sedia ada boleh menunjuk ke arahnya dengan perubahan minimum. Lihat [dokumentasi Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) untuk bermula.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) adalah pemecut inferens dan latihan pembelajaran mesin merentasi platform. ONNX Runtime untuk Generative AI (GENAI) adalah alat yang kuat yang membantu anda menjalankan model AI generatif dengan cekap di pelbagai platform.

## Apa itu ONNX Runtime?
ONNX Runtime adalah projek sumber terbuka yang membolehkan inferens berprestasi tinggi bagi model pembelajaran mesin. Ia menyokong model dalam format Open Neural Network Exchange (ONNX), yang merupakan standard untuk mewakili model pembelajaran mesin. Inferens ONNX Runtime dapat mempercepat pengalaman pelanggan dan mengurangkan kos, menyokong model daripada rangka kerja pembelajaran mendalam seperti PyTorch dan TensorFlow/Keras serta perpustakaan pembelajaran mesin klasik seperti scikit-learn, LightGBM, XGBoost, dan lain-lain. ONNX Runtime serasi dengan pelbagai perkakasan, pemacu, dan sistem operasi, dan menyediakan prestasi optimum dengan memanfaatkan pemecut perkakasan di mana sesuai berserta pengoptimuman dan transformasi graf.

## Apa itu Generative AI?
Generative AI merujuk kepada sistem AI yang boleh menjana kandungan baru, seperti teks, imej, atau muzik, berdasarkan data yang telah dilatih ke atasnya. Contohnya termasuk model bahasa seperti GPT-3 dan model penjanaan imej seperti Stable Diffusion. Perpustakaan ONNX Runtime untuk GenAI menyediakan gelung AI generatif untuk model ONNX, termasuk inferens dengan ONNX Runtime, pemprosesan logits, carian dan pensampelan, serta pengurusan cache KV.

## ONNX Runtime untuk GENAI
ONNX Runtime untuk GENAI meluaskan keupayaan ONNX Runtime untuk menyokong model AI generatif. Berikut adalah beberapa ciri utama:

- **Sokongan Platform Luas:** Ia berfungsi di pelbagai platform, termasuk Windows, Linux, macOS, Android, dan iOS.
- **Sokongan Model:** Ia menyokong banyak model AI generatif popular, seperti LLaMA, GPT-Neo, BLOOM, dan lain-lain.
- **Pengoptimuman Prestasi:** Ia termasuk pengoptimuman untuk pelbagai pemecut perkakasan seperti GPU NVIDIA, GPU AMD, dan lain-lain.
- **Mudah Digunakan:** Ia menyediakan API untuk integrasi mudah ke aplikasi, membolehkan anda menjana teks, imej, dan kandungan lain dengan kod yang minimum.
- Pengguna boleh memanggil kaedah generate() tahap tinggi, atau menjalankan setiap iterasi model dalam gelung, menjana satu token pada satu masa, dan secara pilihan mengemas kini parameter penjanaan di dalam gelung.
- Runtime ONNX juga menyokong carian tamak/beam dan pensampelan TopP, TopK untuk menjana urutan token dan pemprosesan logits terbina dalam seperti penalti pengulangan. Anda juga boleh dengan mudah menambah penilaian tersuai.

## Bermula
Untuk memulakan dengan ONNX Runtime untuk GENAI, anda boleh mengikuti langkah-langkah berikut:

### Pasang ONNX Runtime:
```Python
pip install onnxruntime
```
### Pasang Sambungan Generative AI:
```Python
pip install onnxruntime-genai
```

### Jalankan Model: Berikut adalah contoh mudah dalam Python:
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


**Lain-lain**

Selain daripada ONNX Runtime, Ollama, dan kaedah rujukan Foundry Local, kita juga boleh melengkapkan rujukan model kuantitatif berdasarkan kaedah model yang disediakan oleh pelbagai pengeluar. Seperti rangka kerja Apple MLX dengan Apple Metal, Qualcomm QNN dengan NPU, Intel OpenVINO dengan CPU/GPU, dan lain-lain. Anda juga boleh mendapatkan lebih banyak kandungan dari [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Lagi

Kita telah mempelajari asas keluarga Phi-3/3.5, tetapi untuk belajar lebih lanjut tentang SLM kita memerlukan lebih banyak pengetahuan. Anda boleh mendapatkan jawapan dalam Phi-3 Cookbook. Jika anda ingin belajar lebih banyak, sila lawati [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->