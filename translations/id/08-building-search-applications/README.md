<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d46aad0917a1a342d613e2c13d457da5",
  "translation_date": "2025-07-09T12:59:04+00:00",
  "source_file": "08-building-search-applications/README.md",
  "language_code": "id"
}
-->
# Membangun Aplikasi Pencarian

[![Introduction to Generative AI and Large Language Models](../../../translated_images/08-lesson-banner.8fff48c566dad08a1cbb9f4b4a2c16adfdd288a7bbfffdd30770b466fe08c25c.id.png)](https://aka.ms/gen-ai-lesson8-gh?WT.mc_id=academic-105485-koreyst)

> > _Klik gambar di atas untuk menonton video pelajaran ini_

LLM tidak hanya untuk chatbot dan pembuatan teks. Anda juga bisa membangun aplikasi pencarian menggunakan Embeddings. Embeddings adalah representasi numerik dari data yang juga dikenal sebagai vektor, dan dapat digunakan untuk pencarian semantik pada data.

Dalam pelajaran ini, Anda akan membangun aplikasi pencarian untuk startup pendidikan kami. Startup kami adalah organisasi nirlaba yang menyediakan pendidikan gratis bagi siswa di negara berkembang. Startup kami memiliki banyak video YouTube yang bisa digunakan siswa untuk belajar tentang AI. Startup kami ingin membangun aplikasi pencarian yang memungkinkan siswa mencari video YouTube dengan mengetikkan sebuah pertanyaan.

Misalnya, seorang siswa mungkin mengetik 'Apa itu Jupyter Notebooks?' atau 'Apa itu Azure ML' dan aplikasi pencarian akan mengembalikan daftar video YouTube yang relevan dengan pertanyaan tersebut, dan yang lebih baik lagi, aplikasi pencarian akan mengembalikan tautan ke bagian dalam video di mana jawaban atas pertanyaan tersebut berada.

## Pendahuluan

Dalam pelajaran ini, kita akan membahas:

- Pencarian Semantik vs Pencarian Kata Kunci.
- Apa itu Text Embeddings.
- Membuat Indeks Text Embeddings.
- Mencari dalam Indeks Text Embeddings.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan dapat:

- Menjelaskan perbedaan antara pencarian semantik dan pencarian kata kunci.
- Menjelaskan apa itu Text Embeddings.
- Membuat aplikasi menggunakan Embeddings untuk mencari data.

## Mengapa membangun aplikasi pencarian?

Membangun aplikasi pencarian akan membantu Anda memahami cara menggunakan Embeddings untuk mencari data. Anda juga akan belajar bagaimana membangun aplikasi pencarian yang dapat digunakan siswa untuk menemukan informasi dengan cepat.

Pelajaran ini mencakup Indeks Embedding dari transkrip YouTube untuk saluran Microsoft [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1). AI Show adalah saluran YouTube yang mengajarkan tentang AI dan machine learning. Indeks Embedding berisi Embeddings untuk setiap transkrip YouTube hingga Oktober 2023. Anda akan menggunakan Indeks Embedding ini untuk membangun aplikasi pencarian untuk startup kami. Aplikasi pencarian akan mengembalikan tautan ke bagian dalam video di mana jawaban atas pertanyaan berada. Ini adalah cara yang sangat baik bagi siswa untuk menemukan informasi yang mereka butuhkan dengan cepat.

Berikut adalah contoh kueri semantik untuk pertanyaan 'bisakah Anda menggunakan rstudio dengan azure ml?'. Perhatikan URL YouTube, Anda akan melihat URL tersebut mengandung timestamp yang membawa Anda ke bagian dalam video di mana jawaban atas pertanyaan tersebut berada.

![Kueri semantik untuk pertanyaan "can you use rstudio with Azure ML"](../../../translated_images/query-results.bb0480ebf025fac69c5179ad4d53b6627d643046838c857dc9e2b1281f1cdeb7.id.png)

## Apa itu pencarian semantik?

Mungkin Anda bertanya-tanya, apa itu pencarian semantik? Pencarian semantik adalah teknik pencarian yang menggunakan makna kata-kata dalam kueri untuk mengembalikan hasil yang relevan.

Berikut contoh pencarian semantik. Misalnya Anda ingin membeli mobil, Anda mungkin mencari 'mobil impian saya', pencarian semantik memahami bahwa Anda tidak sedang `bermimpi` tentang mobil, melainkan Anda mencari mobil `ideal` Anda. Pencarian semantik memahami niat Anda dan mengembalikan hasil yang relevan. Alternatifnya adalah `pencarian kata kunci` yang secara harfiah mencari kata-kata tentang mimpi dan sering mengembalikan hasil yang tidak relevan.

## Apa itu Text Embeddings?

[Text embeddings](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst) adalah teknik representasi teks yang digunakan dalam [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst). Text embeddings adalah representasi numerik semantik dari teks. Embeddings digunakan untuk merepresentasikan data dengan cara yang mudah dipahami oleh mesin. Ada banyak model untuk membuat text embeddings, dalam pelajaran ini, kita akan fokus pada pembuatan embeddings menggunakan OpenAI Embedding Model.

Berikut contohnya, bayangkan teks berikut ada dalam transkrip salah satu episode di saluran YouTube AI Show:

```text
Today we are going to learn about Azure Machine Learning.
```

Kita akan mengirim teks tersebut ke OpenAI Embedding API dan API akan mengembalikan embedding berupa 1536 angka yang disebut vektor. Setiap angka dalam vektor mewakili aspek berbeda dari teks tersebut. Untuk ringkasnya, berikut 10 angka pertama dalam vektor tersebut.

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```

## Bagaimana Indeks Embedding dibuat?

Indeks Embedding untuk pelajaran ini dibuat dengan serangkaian skrip Python. Anda dapat menemukan skrip beserta instruksinya di [README](./scripts/README.md?WT.mc_id=academic-105485-koreyst) dalam folder 'scripts' untuk pelajaran ini. Anda tidak perlu menjalankan skrip ini untuk menyelesaikan pelajaran karena Indeks Embedding sudah disediakan.

Skrip melakukan operasi berikut:

1. Transkrip untuk setiap video YouTube dalam playlist [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) diunduh.
2. Menggunakan [OpenAI Functions](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-koreyst), dilakukan upaya untuk mengekstrak nama pembicara dari 3 menit pertama transkrip YouTube. Nama pembicara untuk setiap video disimpan dalam Indeks Embedding bernama `embedding_index_3m.json`.
3. Teks transkrip kemudian dibagi menjadi **segmen teks 3 menit**. Segmen ini mencakup sekitar 20 kata yang tumpang tindih dari segmen berikutnya untuk memastikan Embedding segmen tidak terpotong dan memberikan konteks pencarian yang lebih baik.
4. Setiap segmen teks kemudian dikirim ke OpenAI Chat API untuk meringkas teks menjadi 60 kata. Ringkasan ini juga disimpan dalam Indeks Embedding `embedding_index_3m.json`.
5. Akhirnya, teks segmen dikirim ke OpenAI Embedding API. API Embedding mengembalikan vektor berisi 1536 angka yang mewakili makna semantik segmen tersebut. Segmen beserta vektor OpenAI Embedding disimpan dalam Indeks Embedding `embedding_index_3m.json`.

### Database Vektor

Untuk kesederhanaan pelajaran, Indeks Embedding disimpan dalam file JSON bernama `embedding_index_3m.json` dan dimuat ke dalam Pandas DataFrame. Namun, dalam produksi, Indeks Embedding biasanya disimpan dalam database vektor seperti [Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst), [Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst), [Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst), [Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst), dan lain-lain.

## Memahami cosine similarity

Kita sudah belajar tentang text embeddings, langkah berikutnya adalah belajar bagaimana menggunakan text embeddings untuk mencari data dan khususnya menemukan embeddings yang paling mirip dengan kueri menggunakan cosine similarity.

### Apa itu cosine similarity?

Cosine similarity adalah ukuran kesamaan antara dua vektor, Anda juga mungkin mendengar ini disebut sebagai `nearest neighbor search`. Untuk melakukan pencarian cosine similarity, Anda perlu _mengubah kueri_ menjadi _vektor_ menggunakan OpenAI Embedding API. Kemudian hitung _cosine similarity_ antara vektor kueri dan setiap vektor dalam Indeks Embedding. Ingat, Indeks Embedding memiliki vektor untuk setiap segmen teks transkrip YouTube. Terakhir, urutkan hasil berdasarkan cosine similarity dan segmen teks dengan nilai cosine similarity tertinggi adalah yang paling mirip dengan kueri.

Dari sudut pandang matematika, cosine similarity mengukur kosinus sudut antara dua vektor yang diproyeksikan dalam ruang multidimensi. Pengukuran ini berguna karena jika dua dokumen berjauhan berdasarkan jarak Euclidean karena ukuran, mereka masih bisa memiliki sudut yang lebih kecil di antara mereka dan karenanya memiliki cosine similarity yang lebih tinggi. Untuk informasi lebih lanjut tentang persamaan cosine similarity, lihat [Cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst).

## Membangun aplikasi pencarian pertama Anda

Selanjutnya, kita akan belajar bagaimana membangun aplikasi pencarian menggunakan Embeddings. Aplikasi pencarian ini akan memungkinkan siswa mencari video dengan mengetikkan sebuah pertanyaan. Aplikasi pencarian akan mengembalikan daftar video yang relevan dengan pertanyaan tersebut. Aplikasi pencarian juga akan mengembalikan tautan ke bagian dalam video di mana jawaban atas pertanyaan tersebut berada.

Solusi ini dibangun dan diuji pada Windows 11, macOS, dan Ubuntu 22.04 menggunakan Python 3.10 atau versi lebih baru. Anda dapat mengunduh Python dari [python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

## Tugas - membangun aplikasi pencarian untuk memudahkan siswa

Kami memperkenalkan startup kami di awal pelajaran ini. Sekarang saatnya memudahkan siswa untuk membangun aplikasi pencarian untuk penilaian mereka.

Dalam tugas ini, Anda akan membuat Azure OpenAI Services yang akan digunakan untuk membangun aplikasi pencarian. Anda akan membuat Azure OpenAI Services berikut. Anda memerlukan langganan Azure untuk menyelesaikan tugas ini.

### Mulai Azure Cloud Shell

1. Masuk ke [portal Azure](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst).
2. Pilih ikon Cloud Shell di pojok kanan atas portal Azure.
3. Pilih **Bash** sebagai tipe lingkungan.

#### Membuat resource group

> Untuk instruksi ini, kami menggunakan resource group bernama "semantic-video-search" di East US.
> Anda dapat mengganti nama resource group, tetapi saat mengganti lokasi resource,
> periksa [tabel ketersediaan model](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```shell
az group create --name semantic-video-search --location eastus
```

#### Membuat resource Azure OpenAI Service

Dari Azure Cloud Shell, jalankan perintah berikut untuk membuat resource Azure OpenAI Service.

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

#### Mendapatkan endpoint dan kunci untuk digunakan dalam aplikasi ini

Dari Azure Cloud Shell, jalankan perintah berikut untuk mendapatkan endpoint dan kunci untuk resource Azure OpenAI Service.

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

#### Men-deploy model OpenAI Embedding

Dari Azure Cloud Shell, jalankan perintah berikut untuk men-deploy model OpenAI Embedding.

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

## Solusi

Buka [notebook solusi](../../../08-building-search-applications/python/aoai-solution.ipynb) di GitHub Codespaces dan ikuti instruksi dalam Jupyter Notebook.

Saat menjalankan notebook, Anda akan diminta memasukkan kueri. Kotak input akan terlihat seperti ini:

![Kotak input untuk pengguna memasukkan kueri](../../../translated_images/notebook-search.1e320b9c7fcbb0bc1436d98ea6ee73b4b54ca47990a1c952b340a2cadf8ac1ca.id.png)

## Kerja Bagus! Lanjutkan Pembelajaran Anda

Setelah menyelesaikan pelajaran ini, lihat koleksi [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan Anda tentang Generative AI!

Lanjut ke Pelajaran 9 di mana kita akan melihat cara [membangun aplikasi pembuatan gambar](../09-building-image-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.