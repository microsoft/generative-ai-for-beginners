<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d46aad0917a1a342d613e2c13d457da5",
  "translation_date": "2025-06-25T16:37:13+00:00",
  "source_file": "08-building-search-applications/README.md",
  "language_code": "ms"
}
-->
# Membina Aplikasi Carian

[![Pengenalan kepada AI Generatif dan Model Bahasa Besar](../../../translated_images/08-lesson-banner.8fff48c566dad08a1cbb9f4b4a2c16adfdd288a7bbfffdd30770b466fe08c25c.ms.png)](https://aka.ms/gen-ai-lesson8-gh?WT.mc_id=academic-105485-koreyst)

> > _Klik gambar di atas untuk menonton video pelajaran ini_

LLM lebih daripada sekadar chatbot dan penjanaan teks. Ia juga boleh digunakan untuk membina aplikasi carian menggunakan Embedding. Embedding adalah representasi berangka data yang juga dikenali sebagai vektor, dan boleh digunakan untuk carian semantik data.

Dalam pelajaran ini, anda akan membina aplikasi carian untuk startup pendidikan kami. Startup kami adalah organisasi bukan untung yang menyediakan pendidikan percuma kepada pelajar di negara membangun. Startup kami mempunyai sejumlah besar video YouTube yang boleh digunakan oleh pelajar untuk mempelajari tentang AI. Startup kami ingin membina aplikasi carian yang membolehkan pelajar mencari video YouTube dengan menaip soalan.

Sebagai contoh, seorang pelajar mungkin menaip 'Apa itu Jupyter Notebooks?' atau 'Apa itu Azure ML' dan aplikasi carian akan memulangkan senarai video YouTube yang berkaitan dengan soalan tersebut, dan lebih baik lagi, aplikasi carian akan memulangkan pautan ke tempat dalam video di mana jawapan kepada soalan tersebut terletak.

## Pengenalan

Dalam pelajaran ini, kita akan meliputi:

- Carian Semantik vs Carian Kata Kunci.
- Apa itu Text Embeddings.
- Mencipta Indeks Text Embeddings.
- Mencari Indeks Text Embeddings.

## Matlamat Pembelajaran

Selepas menyelesaikan pelajaran ini, anda akan dapat:

- Membezakan antara carian semantik dan carian kata kunci.
- Menerangkan apa itu Text Embeddings.
- Mencipta aplikasi menggunakan Embeddings untuk mencari data.

## Kenapa membina aplikasi carian?

Mencipta aplikasi carian akan membantu anda memahami cara menggunakan Embeddings untuk mencari data. Anda juga akan belajar bagaimana membina aplikasi carian yang boleh digunakan oleh pelajar untuk mencari maklumat dengan cepat.

Pelajaran ini termasuk Indeks Embedding bagi transkrip YouTube untuk saluran YouTube Microsoft [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1). AI Show adalah saluran YouTube yang mengajar anda tentang AI dan pembelajaran mesin. Indeks Embedding mengandungi Embeddings untuk setiap transkrip YouTube sehingga Okt 2023. Anda akan menggunakan Indeks Embedding untuk membina aplikasi carian untuk startup kami. Aplikasi carian ini memulangkan pautan ke tempat dalam video di mana jawapan kepada soalan terletak. Ini adalah cara yang bagus untuk pelajar mencari maklumat yang mereka perlukan dengan cepat.

Berikut adalah contoh pertanyaan semantik untuk soalan 'bolehkah anda menggunakan rstudio dengan azure ml?'. Lihat url YouTube, anda akan melihat url tersebut mengandungi cap masa yang membawa anda ke tempat dalam video di mana jawapan kepada soalan tersebut terletak.

![Pertanyaan semantik untuk soalan "bolehkah anda menggunakan rstudio dengan Azure ML"](../../../translated_images/query-results.bb0480ebf025fac69c5179ad4d53b6627d643046838c857dc9e2b1281f1cdeb7.ms.png)

## Apa itu carian semantik?

Sekarang anda mungkin tertanya-tanya, apa itu carian semantik? Carian semantik adalah teknik carian yang menggunakan semantik, atau makna, perkataan dalam pertanyaan untuk memulangkan hasil yang relevan.

Berikut adalah contoh carian semantik. Katakan anda ingin membeli kereta, anda mungkin mencari 'kereta impian saya', carian semantik memahami bahawa anda tidak `dreaming` tentang kereta, tetapi anda sedang mencari kereta `ideal` anda. Carian semantik memahami niat anda dan memulangkan hasil yang relevan. Alternatifnya adalah `keyword search` yang secara literal mencari impian tentang kereta dan sering memulangkan hasil yang tidak relevan.

## Apa itu Text Embeddings?

[Text embeddings](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst) adalah teknik representasi teks yang digunakan dalam [pemprosesan bahasa semulajadi](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst). Text embeddings adalah representasi berangka semantik teks. Embeddings digunakan untuk mewakili data dengan cara yang mudah difahami oleh mesin. Terdapat banyak model untuk membina text embeddings, dalam pelajaran ini, kita akan menumpukan pada penjanaan embeddings menggunakan Model Embedding OpenAI.

Berikut adalah contoh, bayangkan teks berikut adalah dalam transkrip daripada salah satu episod di saluran YouTube AI Show:

```text
Today we are going to learn about Azure Machine Learning.
```

Kami akan menghantar teks tersebut kepada OpenAI Embedding API dan ia akan memulangkan embedding yang terdiri daripada 1536 nombor yang juga dikenali sebagai vektor. Setiap nombor dalam vektor mewakili aspek yang berbeza daripada teks tersebut. Untuk ringkasan, berikut adalah 10 nombor pertama dalam vektor.

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```

## Bagaimana Indeks Embedding dicipta?

Indeks Embedding untuk pelajaran ini dicipta dengan beberapa skrip Python. Anda akan menemui skrip bersama arahan dalam [README](./scripts/README.md?WT.mc_id=academic-105485-koreyst) dalam folder 'scripts' untuk pelajaran ini. Anda tidak perlu menjalankan skrip ini untuk melengkapkan pelajaran ini kerana Indeks Embedding telah disediakan untuk anda.

Skrip tersebut menjalankan operasi berikut:

1. Transkrip untuk setiap video YouTube dalam senarai main [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) dimuat turun.
2. Menggunakan [Fungsi OpenAI](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-koreyst), percubaan dibuat untuk mengekstrak nama penceramah dari 3 minit pertama transkrip YouTube. Nama penceramah untuk setiap video disimpan dalam Indeks Embedding yang dinamakan `embedding_index_3m.json`.
3. Teks transkrip kemudian dibahagikan kepada **segmen teks 3 minit**. Segmen tersebut termasuk kira-kira 20 perkataan yang bertindih dari segmen seterusnya untuk memastikan bahawa Embedding untuk segmen tidak terputus dan untuk memberikan konteks carian yang lebih baik.
4. Setiap segmen teks kemudian dihantar kepada OpenAI Chat API untuk meringkaskan teks menjadi 60 perkataan. Ringkasan juga disimpan dalam Indeks Embedding `embedding_index_3m.json`.
5. Akhirnya, teks segmen dihantar kepada OpenAI Embedding API. Embedding API memulangkan vektor 1536 nombor yang mewakili makna semantik segmen tersebut. Segmen bersama vektor OpenAI Embedding disimpan dalam Indeks Embedding `embedding_index_3m.json`.

### Pangkalan Data Vektor

Untuk kesederhanaan pelajaran, Indeks Embedding disimpan dalam fail JSON yang dinamakan `embedding_index_3m.json` dan dimuatkan ke dalam Pandas DataFrame. Walau bagaimanapun, dalam pengeluaran, Indeks Embedding akan disimpan dalam pangkalan data vektor seperti [Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst), [Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst), [Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst), [Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst), untuk menamakan beberapa.

## Memahami kesamaan kosinus

Kita telah belajar tentang text embeddings, langkah seterusnya adalah belajar cara menggunakan text embeddings untuk mencari data dan khususnya mencari embeddings yang paling serupa dengan pertanyaan yang diberikan menggunakan kesamaan kosinus.

### Apa itu kesamaan kosinus?

Kesamaan kosinus adalah ukuran kesamaan antara dua vektor, anda juga akan mendengar ini dirujuk sebagai `nearest neighbor search`. Untuk melakukan carian kesamaan kosinus, anda perlu _menvektor_ teks _pertanyaan_ menggunakan OpenAI Embedding API. Kemudian hitung _kesamaan kosinus_ antara vektor pertanyaan dan setiap vektor dalam Indeks Embedding. Ingat, Indeks Embedding mempunyai vektor untuk setiap segmen teks transkrip YouTube. Akhirnya, urutkan hasil mengikut kesamaan kosinus dan segmen teks dengan kesamaan kosinus tertinggi adalah yang paling serupa dengan pertanyaan.

Dari perspektif matematik, kesamaan kosinus mengukur kosinus sudut antara dua vektor yang diproyeksikan dalam ruang multidimensi. Ukuran ini bermanfaat, kerana jika dua dokumen jauh berasingan oleh jarak Euclidean kerana saiz, mereka masih boleh mempunyai sudut yang lebih kecil antara mereka dan oleh itu kesamaan kosinus yang lebih tinggi. Untuk maklumat lanjut tentang persamaan kesamaan kosinus, lihat [Kesamaan kosinus](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst).

## Membina aplikasi carian pertama anda

Seterusnya, kita akan belajar cara membina aplikasi carian menggunakan Embeddings. Aplikasi carian ini akan membolehkan pelajar mencari video dengan menaip soalan. Aplikasi carian akan memulangkan senarai video yang berkaitan dengan soalan tersebut. Aplikasi carian juga akan memulangkan pautan ke tempat dalam video di mana jawapan kepada soalan terletak.

Penyelesaian ini dibina dan diuji pada Windows 11, macOS, dan Ubuntu 22.04 menggunakan Python 3.10 atau lebih baru. Anda boleh memuat turun Python dari [python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

## Tugasan - membina aplikasi carian, untuk membolehkan pelajar

Kami memperkenalkan startup kami pada permulaan pelajaran ini. Sekarang adalah masa untuk membolehkan pelajar membina aplikasi carian untuk penilaian mereka.

Dalam tugasan ini, anda akan mencipta Perkhidmatan Azure OpenAI yang akan digunakan untuk membina aplikasi carian. Anda akan mencipta Perkhidmatan Azure OpenAI berikut. Anda memerlukan langganan Azure untuk melengkapkan tugasan ini.

### Mulakan Azure Cloud Shell

1. Log masuk ke [portal Azure](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst).
2. Pilih ikon Cloud Shell di penjuru kanan atas portal Azure.
3. Pilih **Bash** untuk jenis persekitaran.

#### Cipta kumpulan sumber

> Untuk arahan ini, kami menggunakan kumpulan sumber yang dinamakan "semantic-video-search" di East US.
> Anda boleh menukar nama kumpulan sumber, tetapi apabila menukar lokasi untuk sumber,
> periksa [jadual ketersediaan model](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```shell
az group create --name semantic-video-search --location eastus
```

#### Cipta sumber Perkhidmatan Azure OpenAI

Dari Azure Cloud Shell, jalankan arahan berikut untuk mencipta sumber Perkhidmatan Azure OpenAI.

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

#### Dapatkan titik akhir dan kunci untuk penggunaan dalam aplikasi ini

Dari Azure Cloud Shell, jalankan arahan berikut untuk mendapatkan titik akhir dan kunci untuk sumber Perkhidmatan Azure OpenAI.

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

#### Menyebarkan model Embedding OpenAI

Dari Azure Cloud Shell, jalankan arahan berikut untuk menyebarkan model Embedding OpenAI.

```shell
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --sku-capacity 100 --sku-name "Standard"
```

## Penyelesaian

Buka [notebook penyelesaian](../../../08-building-search-applications/python/aoai-solution.ipynb) di GitHub Codespaces dan ikuti arahan dalam Jupyter Notebook.

Apabila anda menjalankan notebook, anda akan diminta untuk memasukkan pertanyaan. Kotak input akan kelihatan seperti ini:

![Kotak input untuk pengguna memasukkan pertanyaan](../../../translated_images/notebook-search.1e320b9c7fcbb0bc1436d98ea6ee73b4b54ca47990a1c952b340a2cadf8ac1ca.ms.png)

## Kerja Hebat! Teruskan Pembelajaran Anda

Selepas melengkapkan pelajaran ini, lihat koleksi pembelajaran [AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif anda!

Pergi ke Pelajaran 9 di mana kita akan melihat bagaimana untuk [membina aplikasi penjanaan imej](../09-building-image-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.