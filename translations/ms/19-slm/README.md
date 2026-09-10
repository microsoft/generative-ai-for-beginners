# Pengenalan kepada Model Bahasa Kecil untuk AI Generatif bagi Pemula
AI generatif adalah bidang kecerdasan buatan yang menarik yang menumpukan pada penciptaan sistem yang mampu menghasilkan kandungan baru. Kandungan ini boleh merangkumi teks dan imej hingga muzik dan bahkan persekitaran maya sepenuhnya. Salah satu aplikasi AI generatif yang paling menarik adalah dalam domain model bahasa.

## Apakah Model Bahasa Kecil?

Model Bahasa Kecil (SLM) mewakili varian yang diperkecil dari model bahasa besar (LLM), memanfaatkan banyak prinsip seni bina dan teknik LLM, sementara menunjukkan jejak pengkomputeran yang jauh lebih rendah. 

SLM adalah subset model bahasa yang direka untuk menghasilkan teks seperti manusia. Berbeza dengan rakan besar mereka, seperti GPT-4, SLM lebih padat dan cekap, menjadikannya sesuai untuk aplikasi di mana sumber pengkomputeran adalah terhad. Walaupun saiznya lebih kecil, mereka masih boleh menjalankan pelbagai tugas. Biasanya, SLM dibina dengan memampatkan atau mengekstrak LLM, bertujuan untuk mengekalkan sebahagian besar fungsi dan kebolehan linguistik model asal. Pengurangan saiz model ini mengurangkan kerumitan keseluruhan, menjadikan SLM lebih cekap dari segi penggunaan memori dan keperluan pengkomputeran. Walaupun dengan pengoptimuman ini, SLM masih boleh melaksanakan pelbagai tugas pemprosesan bahasa semulajadi (NLP):

- Penjanaan Teks: Mencipta ayat atau perenggan yang koheren dan berkaitan konteks.
- Lengkap Teks: Meramalkan dan melengkapkan ayat berdasarkan arahan yang diberikan.
- Terjemahan: Menukar teks dari satu bahasa ke bahasa lain.
- Ringkasan: Memadatkan teks panjang menjadi ringkasan yang lebih pendek dan mudah dikaji.

Walaupun dengan beberapa pertukaran dalam prestasi atau kedalaman pemahaman berbanding dengan rakan besar mereka. 

## Bagaimana Model Bahasa Kecil Berfungsi?
SLM dilatih menggunakan sejumlah besar data teks. Semasa latihan, mereka mempelajari corak dan struktur bahasa, membolehkan mereka menghasilkan teks yang betul dari segi tatabahasa dan sesuai konteks. Proses latihan melibatkan:

- Pengumpulan Data: Mengumpul dataset besar teks dari pelbagai sumber.
- Pra-pemprosesan: Membersih dan menyusun data agar sesuai untuk latihan.
- Latihan: Menggunakan algoritma pembelajaran mesin untuk mengajar model bagaimana memahami dan menghasilkan teks.
- Penalaan Halus: Melaraskan model untuk meningkatkan prestasi dalam tugas-tugas khusus.

Pembangunan SLM sejajar dengan keperluan yang semakin meningkat untuk model yang boleh digunakan dalam persekitaran yang menghadkan sumber, seperti peranti mudah alih atau platform pengkomputeran edge, di mana LLM skala penuh mungkin tidak praktikal kerana permintaan sumber yang tinggi. Dengan menumpukan pada kecekapan, SLM mengimbangi prestasi dengan aksesibiliti, membolehkan aplikasi lebih luas di pelbagai domain.

![slm](../../../translated_images/ms/slm.4058842744d0444a.webp)

## Objektif Pembelajaran

Dalam pelajaran ini, kami berharap memperkenalkan pengetahuan tentang SLM dan menggabungkannya dengan Microsoft Phi-3 untuk mempelajari pelbagai senario dalam kandungan teks, visi dan MoE.

Pada akhir pelajaran ini, anda sepatutnya boleh menjawab soalan berikut:

- Apakah SLM?
- Apakah perbezaan antara SLM dan LLM?
- Apakah Keluarga Microsoft Phi-3/3.5?
- Bagaimana menjalankan inferens dengan Keluarga Microsoft Phi-3/3.5?

Sedia? Mari kita mulakan.

## Perbezaan antara Model Bahasa Besar (LLM) dan Model Bahasa Kecil (SLM)

Kedua-dua LLM dan SLM dibina berdasarkan prinsip asas pembelajaran mesin probabilistik, mengikuti pendekatan yang serupa dalam reka bentuk seni bina, metodologi latihan, proses penjanaan data, dan teknik penilaian model. Namun, beberapa faktor utama membezakan kedua jenis model ini.

## Aplikasi Model Bahasa Kecil

SLM mempunyai pelbagai aplikasi, termasuk:

- Chatbot: Menyediakan sokongan pelanggan dan berinteraksi dengan pengguna secara perbualan.
- Penciptaan Kandungan: Membantu penulis dengan menjana idea atau malah menulis artikel sepenuhnya.
- Pendidikan: Membantu pelajar dengan tugasan menulis atau mempelajari bahasa baru.
- Aksesibiliti: Mewujudkan alat untuk individu dengan kecacatan, seperti sistem teks-ke-ucapan.

**Saiz**
  
Perbezaan utama antara LLM dan SLM terletak pada skala model. LLM, seperti ChatGPT (GPT-4), boleh terdiri daripada anggaran 1.76 trilion parameter, manakala SLM sumber terbuka seperti Mistral 7B direka dengan parameter yang jauh lebih sedikit—sekitar 7 bilion. Jurang ini kebanyakannya disebabkan oleh perbezaan dalam seni bina model dan proses latihan. Contohnya, ChatGPT menggunakan mekanisme perhatian diri dalam rangka kerja pengekod-penyahkod, manakala Mistral 7B menggunakan perhatian tetingkap gelongsor, yang membolehkan latihan lebih efisien dalam model penyahkod sahaja. Variasi seni bina ini mempunyai impak mendalam terhadap kerumitan dan prestasi model-model ini.

**Pemahaman**

SLM biasanya dioptimumkan untuk prestasi dalam domain tertentu, menjadikannya sangat khusus tetapi mungkin terhad dalam kebolehan untuk menyediakan pemahaman konteks yang luas merentas pelbagai bidang ilmu. Sebaliknya, LLM bertujuan untuk mensimulasikan kecerdasan seperti manusia pada tahap yang lebih komprehensif. Dilatih pada dataset yang sangat besar dan pelbagai, LLM direka untuk berprestasi baik dalam pelbagai domain, menawarkan lebih banyak kepelbagaian dan kebolehsuaian. Oleh itu, LLM lebih sesuai untuk pelbagai tugasan hiliran, seperti pemprosesan bahasa semula jadi dan pengaturcaraan.

**Pengkomputeran**

Latihan dan penyebaran LLM memerlukan proses yang intensif sumber, sering memerlukan infrastruktur pengkomputeran yang besar termasuk kluster GPU berskala besar. Sebagai contoh, melatih model seperti ChatGPT dari awal mungkin memerlukan ribuan GPU sepanjang tempoh yang panjang. Berbeza dengan itu, SLM, dengan jumlah parameter yang lebih kecil, lebih mudah diakses dari segi sumber pengkomputeran. Model seperti Mistral 7B boleh dilatih dan dijalankan pada mesin tempatan yang dilengkapi dengan kemampuan GPU sederhana, walaupun latihan masih memerlukan beberapa jam merentas pelbagai GPU.

**Bias**

Bias adalah isu yang diketahui dalam LLM, terutama disebabkan oleh sifat data latihan. Model ini sering bergantung pada data mentah yang tersedia secara terbuka dari internet, yang mungkin kurang atau salah mewakili kumpulan tertentu, memasukkan pelabelan yang salah, atau mencerminkan bias linguistik yang dipengaruhi oleh dialek, variasi geografi, dan peraturan tatabahasa. Selain itu, kerumitan seni bina LLM boleh secara tidak sengaja memburukkan bias ini, yang mungkin terlepas tanpa penalaan yang teliti. Sebaliknya, SLM, yang dilatih pada dataset yang lebih terhad dan khusus domain, secara semula jadi kurang terdedah kepada bias sebegini, walaupun mereka tidak kebal daripadanya.

**Inferens**

Saiz SLM yang dikurangkan memberikan kelebihan ketara dari segi kelajuan inferens, membolehkan mereka menjana output dengan cekap pada perkakasan tempatan tanpa keperluan pemprosesan selari yang meluas. Sebaliknya, LLM, kerana saiz dan kerumitannya, sering memerlukan sumber pengiraan selari yang besar untuk mencapai masa inferens yang boleh diterima. Kehadiran pelbagai pengguna serentak juga memperlahankan masa respons LLM, terutamanya apabila disebarkan pada skala besar.

Ringkasnya, walaupun LLM dan SLM berkongsi asas pembelajaran mesin, mereka berbeza secara signifikan dari segi saiz model, keperluan sumber, pemahaman konteks, kerentanan terhadap bias, dan kelajuan inferens. Perbezaan ini mencerminkan kesesuaian masing-masing untuk kegunaan yang berbeza, dengan LLM lebih serba boleh tetapi memerlukan sumber yang banyak, manakala SLM menawarkan kecekapan khusus domain dengan keperluan pengkomputeran yang dikurangkan.

***Nota: Dalam pelajaran ini, kami akan memperkenalkan SLM menggunakan Microsoft Phi-3 / 3.5 sebagai contoh.***

## Memperkenalkan Keluarga Phi-3 / Phi-3.5

Keluarga Phi-3 / 3.5 terutama menumpukan pada senario aplikasi teks, visi, dan Agen (MoE):

### Phi-3 / 3.5 Instruct

Terutamanya untuk penjanaan teks, pelengkap perbualan, dan pengektrakan maklumat kandungan, dll.

**Phi-3-mini**

Model bahasa 3.8B tersedia di Microsoft Foundry, Hugging Face, dan Ollama. Model Phi-3 mengatasi model bahasa setara dan lebih besar dengan ketara pada penanda aras utama (lihat nombor penanda aras di bawah, nombor yang lebih tinggi adalah lebih baik). Phi-3-mini mengatasi model yang dua kali saiznya, manakala Phi-3-small dan Phi-3-medium mengatasi model yang lebih besar, termasuk GPT-3.5.

**Phi-3-small & medium**

Dengan hanya 7B parameter, Phi-3-small mengalahkan GPT-3.5T dalam pelbagai penanda aras bahasa, penalaran, pengaturcaraan, dan matematik.

Phi-3-medium dengan 14B parameter meneruskan trend ini dan mengatasi Gemini 1.0 Pro.

**Phi-3.5-mini**

Kita boleh menganggapnya sebagai peningkatan dari Phi-3-mini. Walaupun parameter kekal sama, ia meningkatkan keupayaan untuk menyokong pelbagai bahasa (menyokong 20+ bahasa: Arab, Cina, Czech, Denmark, Belanda, Inggeris, Finland, Perancis, Jerman, Ibrani, Hungary, Itali, Jepun, Korea, Norway, Poland, Portugis, Rusia, Sepanyol, Sweden, Thai, Turki, Ukraine) ​​dan menambah sokongan lebih kuat untuk konteks panjang.

Phi-3.5-mini dengan 3.8B parameter mengatasi model bahasa saiz sama dan setaraf dengan model dua kali ganda saiznya.

### Phi-3 / 3.5 Vision

Kita boleh menganggap model Instruct Phi-3/3.5 sebagai keupayaan Phi untuk memahami, dan Vision adalah apa yang memberi ‘mata’ kepada Phi untuk memahami dunia.


**Phi-3-Vision**

Phi-3-vision, dengan hanya 4.2B parameter, meneruskan trend ini dan mengatasi model yang lebih besar seperti Claude-3 Haiku dan Gemini 1.0 Pro V dalam tugas penalaran visual umum, OCR, dan pemahaman jadual dan rajah.


**Phi-3.5-Vision**

Phi-3.5-Vision juga merupakan peningkatan dari Phi-3-Vision, menambah sokongan untuk pelbagai imej. Anda boleh menganggapnya sebagai peningkatan dalam visi, bukan sahaja boleh melihat gambar, tetapi juga video.

Phi-3.5-vision mengatasi model lebih besar seperti Claude-3.5 Sonnet dan Gemini 1.5 Flash dalam tugas OCR, pemahaman jadual dan carta, serta setaraf dalam tugas penalaran pengetahuan visual umum. Menyokong input pelbagai bingkai, iaitu, melaksanakan penalaran pada banyak imej input


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** membolehkan model dipra-latih dengan pengiraan yang jauh lebih sedikit, yang bermakna anda boleh mengembangkan saiz model atau dataset secara dramatik dengan bajet pengiraan yang sama seperti model padat. Secara khusus, model MoE harus mencapai kualiti yang sama dengan rakan padatnya dengan lebih cepat semasa pra-latihan.

Phi-3.5-MoE terdiri daripada 16 modul pakar 3.8B. Phi-3.5-MoE dengan hanya 6.6B parameter aktif mencapai tahap penalaran, pemahaman bahasa, dan matematik setara dengan model yang jauh lebih besar.

Kita boleh menggunakan model Keluarga Phi-3/3.5 berdasarkan senario berbeza. Tidak seperti LLM, anda boleh menyebarkan Phi-3/3.5-mini atau Phi-3/3.5-Vision pada peranti edge.


## Cara menggunakan model Keluarga Phi-3/3.5

Kami berharap menggunakan Phi-3/3.5 dalam pelbagai senario. Seterusnya, kami akan menggunakan Phi-3/3.5 berdasarkan senario yang berbeza.

![phi3](../../../translated_images/ms/phi3.655208c3186ae381.webp)

### Inferens melalui Cloud APIs

**Model Microsoft Foundry**

> **Nota:** Model GitHub akan dihentikan pada akhir Julai 2026. [Model Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) adalah pengganti terusannya.

Model Microsoft Foundry adalah cara paling langsung. Anda boleh dengan cepat mengakses model Phi-3/3.5-Instruct melalui katalog model Foundry. Digabungkan dengan Azure AI Inference SDK / OpenAI SDK, anda boleh mengakses API melalui kod untuk melengkapkan panggilan Phi-3/3.5-Instruct. Anda juga boleh menguji pelbagai kesan melalui Playground.

- Demo: Perbandingan kesan Phi-3-mini dan Phi-3.5-mini dalam senario bahasa Cina

![phi3](../../../translated_images/ms/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/ms/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

Atau jika kita ingin menggunakan model visi dan MoE, anda boleh menggunakan Microsoft Foundry untuk melengkapkan panggilan. Jika berminat, anda boleh membaca Buku Resipi Phi-3 untuk belajar bagaimana memanggil Phi-3/3.5 Instruct, Vision, MoE melalui Microsoft Foundry [Klik pautan ini](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Selain katalog Model Microsoft Foundry berasaskan awan, anda juga boleh menggunakan [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) untuk melengkapkan panggilan berkaitan. Anda boleh melawat NVIDIA NIM untuk melengkapkan panggilan API Keluarga Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) adalah satu set mikroskhidmat inferens dipercepat yang direka untuk membantu pemaju menyebarkan model AI dengan cekap merentas pelbagai persekitaran, termasuk awan, pusat data, dan stesen kerja.

Berikut adalah beberapa ciri utama NVIDIA NIM:

- **Kemudahan Penyebaran:** NIM membolehkan penyebaran model AI dengan satu perintah, menjadikannya mudah untuk disepadukan ke dalam aliran kerja sedia ada.

- **Prestasi Dioptimumkan:** Ia memanfaatkan enjin inferens yang telah dioptimumkan pra oleh NVIDIA, seperti TensorRT dan TensorRT-LLM, untuk memastikan latensi rendah dan throughput tinggi.
- **Skalabiliti:** NIM menyokong autoscaling pada Kubernetes, membolehkannya mengendalikan beban kerja yang berbeza dengan berkesan.
- **Keselamatan dan Kawalan:** Organisasi boleh mengekalkan kawalan ke atas data dan aplikasi mereka dengan menghoskan sendiri perkhidmatan mikro NIM pada infrastruktur mereka yang diuruskan sendiri.
- **API Standard:** NIM menyediakan API standard industri, memudahkan pembinaan dan integrasi aplikasi AI seperti chatbot, pembantu AI, dan lain-lain.

NIM adalah sebahagian daripada NVIDIA AI Enterprise, yang bertujuan memudahkan penyebaran dan pengoperasian model AI, memastikan ia berjalan dengan cekap pada GPU NVIDIA.

- Demo: Menggunakan NVIDIA NIM untuk memanggil Phi-3.5-Vision-API  [[Klik pautan ini](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Menjalankan Phi-3/3.5 Secara Tempatan
Inferens berkenaan dengan Phi-3, atau mana-mana model bahasa seperti GPT-3, merujuk kepada proses menghasilkan respons atau ramalan berdasarkan input yang diterimanya. Apabila anda memberikan petunjuk atau soalan kepada Phi-3, ia menggunakan rangkaian neural yang telah dilatih untuk membuat inferens respons yang paling mungkin dan relevan dengan menganalisis corak dan hubungan dalam data yang dilatih.

**Hugging Face Transformer**
Hugging Face Transformers adalah perpustakaan yang kuat direka untuk pemprosesan bahasa semulajadi (NLP) dan tugas pembelajaran mesin lain. Berikut adalah beberapa perkara utama mengenainya:

1. **Model Pra-latih**: Ia menyediakan beribu-ribu model pra-latih yang boleh digunakan untuk pelbagai tugasan seperti klasifikasi teks, pengecaman entiti bernama, menjawab soalan, meringkaskan, menterjemah, dan penjanaan teks.

2. **Interoperabiliti Rangka Kerja:** Perpustakaan ini menyokong pelbagai rangka kerja pembelajaran mendalam, termasuk PyTorch, TensorFlow, dan JAX. Ini membolehkan anda melatih model dalam satu rangka kerja dan menggunakannya dalam rangka kerja lain.

3. **Keupayaan Multimodal:** Selain NLP, Hugging Face Transformers juga menyokong tugasan dalam penglihatan komputer (contohnya, klasifikasi imej, pengesanan objek) dan pemprosesan audio (contohnya, pengecaman ucapan, klasifikasi audio).

4. **Mudah Digunakan:** Perpustakaan ini menawarkan API dan alat untuk memuat turun dan menyesuaikan model dengan mudah, menjadikannya boleh diakses untuk pemula dan pakar.

5. **Komuniti dan Sumber:** Hugging Face mempunyai komuniti yang aktif serta dokumentasi, tutorial, dan panduan yang meluas untuk membantu pengguna memulakan dan memanfaatkan perpustakaan ini sepenuhnya.
[dokumentasi rasmi](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) atau repositori mereka di [GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Ini adalah kaedah yang paling kerap digunakan, tetapi ia juga memerlukan pecutan GPU. Lagipun, senario seperti Vision dan MoE memerlukan banyak pengiraan, yang akan menjadi sangat perlahan pada CPU jika tidak dikualitikan.


- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-Instruct [Klik pautan ini](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-Vision [Klik pautan ini](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Menggunakan Transformer untuk memanggil Phi-3.5-MoE [Klik pautan ini](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) adalah platform yang direka untuk memudahkan menjalankan model bahasa besar (LLM) secara tempatan pada mesin anda. Ia menyokong pelbagai model seperti Llama 3.1, Phi 3, Mistral, dan Gemma 2, antara lain. Platform ini memudahkan proses dengan menggabungkan berat model, konfigurasi, dan data ke dalam satu pakej, menjadikannya lebih mudah untuk pengguna menyesuaikan dan membuat model mereka sendiri. Ollama tersedia untuk macOS, Linux, dan Windows. Ia adalah alat yang hebat jika anda ingin bereksperimen dengan atau menyebarkan LLM tanpa bergantung pada perkhidmatan awan. Ollama adalah cara paling langsung, anda hanya perlu melaksanakan arahan berikut.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) adalah runtime tanpa sambungan internet Microsoft untuk menjalankan model seperti Phi sepenuhnya pada perkakasan anda sendiri - tiada langganan Azure, kunci API, atau sambungan rangkaian diperlukan. Ia secara automatik memilih penyedia pelaksanaan terbaik yang tersedia (NPU, GPU, atau CPU) dan memaparkan endpoint yang serasi dengan OpenAI, jadi kod SDK `openai`/Azure AI Inference sedia ada boleh diarahkan kepadanya dengan perubahan minimum. Lihat [dokumentasi Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) untuk memulakan.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) adalah pemecut mesin pembelajaran rentas platform untuk inferens dan latihan. ONNX Runtime untuk Generative AI (GENAI) adalah alat yang kuat yang membantu anda menjalankan model AI generatif dengan cekap merentas pelbagai platform.

## Apakah ONNX Runtime?
ONNX Runtime adalah projek sumber terbuka yang membolehkan inferens berprestasi tinggi untuk model pembelajaran mesin. Ia menyokong model dalam format Open Neural Network Exchange (ONNX), yang merupakan standard untuk mewakili model pembelajaran mesin. Inferens ONNX Runtime boleh membolehkan pengalaman pelanggan yang lebih pantas dan kos yang lebih rendah, menyokong model daripada rangka kerja pembelajaran mendalam seperti PyTorch dan TensorFlow/Keras serta perpustakaan pembelajaran mesin klasik seperti scikit-learn, LightGBM, XGBoost, dan lain-lain. ONNX Runtime serasi dengan pelbagai perkakasan, pemandu, dan sistem operasi, dan menyediakan prestasi optimum dengan memanfaatkan pemecut perkakasan di mana yang berkenaan berserta pengoptimuman dan transformasi graf.

## Apakah AI Generatif?
AI generatif merujuk kepada sistem AI yang boleh menghasilkan kandungan baru, seperti teks, imej, atau muzik, berdasarkan data yang telah dilatih ke atasnya. Contohnya termasuk model bahasa seperti GPT-3 dan model penjanaan imej seperti Stable Diffusion. Perpustakaan ONNX Runtime untuk GenAI menyediakan kitaran AI generatif untuk model ONNX, termasuk inferens dengan ONNX Runtime, pemprosesan logits, pencarian dan pensampelan, serta pengurusan cache KV.

## ONNX Runtime untuk GENAI
ONNX Runtime untuk GENAI meluaskan keupayaan ONNX Runtime untuk menyokong model AI generatif. Berikut adalah beberapa ciri utama:

- **Sokongan Pelbagai Platform:** Ia berfungsi pada pelbagai platform, termasuk Windows, Linux, macOS, Android, dan iOS.
- **Sokongan Model:** Ia menyokong banyak model AI generatif popular, seperti LLaMA, GPT-Neo, BLOOM, dan lain-lain.
- **Pengoptimuman Prestasi:** Ia termasuk pengoptimuman untuk pelbagai pemecut perkakasan seperti GPU NVIDIA, GPU AMD, dan lain-lain.
- **Mudah Digunakan:** Ia menyediakan API untuk integrasi mudah ke dalam aplikasi, membolehkan anda menjana teks, imej, dan kandungan lain dengan kod yang minimum.
- Pengguna boleh memanggil kaedah generate() tahap tinggi, atau menjalankan setiap iterasi model dalam gelung, menjana satu token pada satu masa, dan secara pilihan mengemas kini parameter penjanaan dalam gelung tersebut.
- Runtime ONNX juga menyokong carian tamak/beam dan pensampelan TopP, TopK untuk menjana urutan token serta pemprosesan logits terbina dalam seperti penalti pengulangan. Anda juga boleh dengan mudah menambah penilaian tersuai.

## Mula Menggunakan
Untuk mula menggunakan ONNX Runtime untuk GENAI, anda boleh mengikuti langkah-langkah berikut:

### Pasang ONNX Runtime:
```Python
pip install onnxruntime
```
### Pasang Sambungan AI Generatif:
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

Selain daripada ONNX Runtime, Ollama, dan kaedah rujukan Foundry Local, kita juga boleh melengkapkan rujukan model kuantitatif berdasarkan kaedah rujukan model yang disediakan oleh pelbagai pengeluar. Seperti rangka kerja Apple MLX dengan Apple Metal, Qualcomm QNN dengan NPU, Intel OpenVINO dengan CPU/GPU, dan lain-lain. Anda juga boleh mendapatkan lebih banyak kandungan dari [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Lebih Lagi

Kita telah mempelajari asas-asas Keluarga Phi-3/3.5, tetapi untuk mengetahui lebih lanjut tentang SLM kita memerlukan lebih banyak pengetahuan. Anda boleh mendapatkan jawapan dalam Phi-3 Cookbook. Jika anda ingin belajar lebih lanjut, sila lawati [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->