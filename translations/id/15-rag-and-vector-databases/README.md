<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4b0266fbadbba7ded891b6485adc66d",
  "translation_date": "2025-10-17T20:44:58+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "id"
}
-->
# Retrieval Augmented Generation (RAG) dan Basis Data Vektor

[![Retrieval Augmented Generation (RAG) dan Basis Data Vektor](../../../translated_images/15-lesson-banner.ac49e59506175d4fc6ce521561dab2f9ccc6187410236376cfaed13cde371b90.id.png)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Dalam pelajaran aplikasi pencarian, kita telah mempelajari secara singkat cara mengintegrasikan data Anda sendiri ke dalam Model Bahasa Besar (LLM). Dalam pelajaran ini, kita akan mendalami lebih jauh konsep menanamkan data Anda ke dalam aplikasi LLM, mekanisme prosesnya, dan metode penyimpanan data, termasuk embedding dan teks.

> **Video Segera Hadir**

## Pengantar

Dalam pelajaran ini, kita akan membahas:

- Pengantar RAG, apa itu dan mengapa digunakan dalam AI (kecerdasan buatan).

- Memahami apa itu basis data vektor dan membuatnya untuk aplikasi kita.

- Contoh praktis tentang cara mengintegrasikan RAG ke dalam aplikasi.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan dapat:

- Menjelaskan pentingnya RAG dalam pengambilan dan pemrosesan data.

- Menyiapkan aplikasi RAG dan menanamkan data Anda ke dalam LLM.

- Integrasi yang efektif antara RAG dan Basis Data Vektor dalam Aplikasi LLM.

## Skenario Kita: meningkatkan LLM dengan data kita sendiri

Untuk pelajaran ini, kita ingin menambahkan catatan kita sendiri ke dalam startup pendidikan, yang memungkinkan chatbot mendapatkan lebih banyak informasi tentang berbagai subjek. Dengan menggunakan catatan yang kita miliki, pelajar akan dapat belajar lebih baik dan memahami berbagai topik, sehingga mempermudah mereka untuk mempersiapkan ujian. Untuk membuat skenario kita, kita akan menggunakan:

- `Azure OpenAI:` LLM yang akan kita gunakan untuk membuat chatbot kita.

- `Pelajaran AI untuk Pemula tentang Jaringan Neural:` ini akan menjadi data yang kita tanamkan ke dalam LLM kita.

- `Azure AI Search` dan `Azure Cosmos DB:` basis data vektor untuk menyimpan data kita dan membuat indeks pencarian.

Pengguna akan dapat membuat kuis latihan dari catatan mereka, kartu flash revisi, dan merangkum catatan menjadi ringkasan singkat. Untuk memulai, mari kita lihat apa itu RAG dan bagaimana cara kerjanya:

## Retrieval Augmented Generation (RAG)

Chatbot yang didukung LLM memproses permintaan pengguna untuk menghasilkan respons. Chatbot ini dirancang untuk interaktif dan berinteraksi dengan pengguna dalam berbagai topik. Namun, responsnya terbatas pada konteks yang diberikan dan data pelatihan dasarnya. Misalnya, pengetahuan GPT-4 hanya sampai September 2021, artinya, ia tidak memiliki pengetahuan tentang peristiwa yang terjadi setelah periode tersebut. Selain itu, data yang digunakan untuk melatih LLM tidak mencakup informasi rahasia seperti catatan pribadi atau manual produk perusahaan.

### Cara kerja RAG (Retrieval Augmented Generation)

![gambar menunjukkan cara kerja RAG](../../../translated_images/how-rag-works.f5d0ff63942bd3a638e7efee7a6fce7f0787f6d7a1fca4e43f2a7a4d03cde3e0.id.png)

Misalkan Anda ingin menerapkan chatbot yang membuat kuis dari catatan Anda, Anda akan memerlukan koneksi ke basis pengetahuan. Di sinilah RAG menjadi solusi. RAG bekerja sebagai berikut:

- **Basis pengetahuan:** Sebelum pengambilan, dokumen-dokumen ini perlu dimasukkan dan diproses terlebih dahulu, biasanya dengan memecah dokumen besar menjadi potongan-potongan kecil, mengubahnya menjadi embedding teks, dan menyimpannya dalam basis data.

- **Permintaan pengguna:** pengguna mengajukan pertanyaan.

- **Pengambilan:** Ketika pengguna mengajukan pertanyaan, model embedding mengambil informasi relevan dari basis pengetahuan kita untuk memberikan lebih banyak konteks yang akan dimasukkan ke dalam permintaan.

- **Generasi yang Ditingkatkan:** LLM meningkatkan responsnya berdasarkan data yang diambil. Ini memungkinkan respons yang dihasilkan tidak hanya berdasarkan data yang telah dilatih sebelumnya tetapi juga informasi relevan dari konteks tambahan. Data yang diambil digunakan untuk meningkatkan respons LLM. LLM kemudian memberikan jawaban atas pertanyaan pengguna.

![gambar menunjukkan arsitektur RAG](../../../translated_images/encoder-decode.f2658c25d0eadee2377bb28cf3aee8b67aa9249bf64d3d57bb9be077c4bc4e1a.id.png)

Arsitektur RAG diimplementasikan menggunakan transformer yang terdiri dari dua bagian: encoder dan decoder. Misalnya, ketika pengguna mengajukan pertanyaan, teks input 'dikodekan' menjadi vektor yang menangkap makna kata-kata dan vektor tersebut 'didekodekan' ke dalam indeks dokumen kita dan menghasilkan teks baru berdasarkan permintaan pengguna. LLM menggunakan model encoder-decoder untuk menghasilkan output.

Dua pendekatan dalam menerapkan RAG menurut makalah yang diusulkan: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) adalah:

- **_RAG-Sequence_** menggunakan dokumen yang diambil untuk memprediksi jawaban terbaik atas permintaan pengguna.

- **RAG-Token** menggunakan dokumen untuk menghasilkan token berikutnya, lalu mengambilnya untuk menjawab permintaan pengguna.

### Mengapa menggunakan RAG?

- **Kekayaan informasi:** memastikan respons teks selalu terkini. Oleh karena itu, meningkatkan kinerja pada tugas-tugas spesifik domain dengan mengakses basis pengetahuan internal.

- Mengurangi fabrikasi dengan menggunakan **data yang dapat diverifikasi** dalam basis pengetahuan untuk memberikan konteks pada permintaan pengguna.

- **Efisien biaya** karena lebih ekonomis dibandingkan dengan fine-tuning LLM.

## Membuat basis pengetahuan

Aplikasi kita didasarkan pada data pribadi kita yaitu pelajaran Jaringan Neural dari kurikulum AI For Beginners.

### Basis Data Vektor

Basis data vektor, berbeda dengan basis data tradisional, adalah basis data khusus yang dirancang untuk menyimpan, mengelola, dan mencari vektor embedding. Basis data ini menyimpan representasi numerik dari dokumen. Memecah data menjadi embedding numerik mempermudah sistem AI kita untuk memahami dan memproses data.

Kita menyimpan embedding kita dalam basis data vektor karena LLM memiliki batas jumlah token yang dapat diterima sebagai input. Karena Anda tidak dapat memberikan seluruh embedding ke LLM, kita perlu memecahnya menjadi potongan-potongan kecil dan ketika pengguna mengajukan pertanyaan, embedding yang paling mirip dengan pertanyaan akan dikembalikan bersama dengan permintaan. Pemecahan juga mengurangi biaya pada jumlah token yang diteruskan melalui LLM.

Beberapa basis data vektor populer termasuk Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant, dan DeepLake. Anda dapat membuat model Azure Cosmos DB menggunakan Azure CLI dengan perintah berikut:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Dari teks ke embedding

Sebelum kita menyimpan data kita, kita perlu mengonversinya menjadi embedding vektor sebelum disimpan dalam basis data. Jika Anda bekerja dengan dokumen besar atau teks panjang, Anda dapat memecahnya berdasarkan permintaan yang Anda harapkan. Pemecahan dapat dilakukan pada tingkat kalimat, atau pada tingkat paragraf. Karena pemecahan mengambil makna dari kata-kata di sekitarnya, Anda dapat menambahkan beberapa konteks lain ke potongan, misalnya, dengan menambahkan judul dokumen atau menyertakan beberapa teks sebelum atau setelah potongan. Anda dapat memecah data sebagai berikut:

```python
def split_text(text, max_length, min_length):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(' '.join(current_chunk)) < max_length and len(' '.join(current_chunk)) > min_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = []

    # If the last chunk didn't reach the minimum length, add it anyway
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Setelah dipecah, kita kemudian dapat meng-embed teks kita menggunakan berbagai model embedding. Beberapa model yang dapat Anda gunakan termasuk: word2vec, ada-002 oleh OpenAI, Azure Computer Vision, dan banyak lagi. Memilih model yang akan digunakan akan bergantung pada bahasa yang Anda gunakan, jenis konten yang dikodekan (teks/gambar/audio), ukuran input yang dapat dikodekan, dan panjang output embedding.

Contoh teks yang di-embed menggunakan model `text-embedding-ada-002` dari OpenAI adalah:
![embedding dari kata kucing](../../../translated_images/cat.74cbd7946bc9ca380a8894c4de0c706a4f85b16296ffabbf52d6175df6bf841e.id.png)

## Pengambilan dan Pencarian Vektor

Ketika pengguna mengajukan pertanyaan, retriever mengubahnya menjadi vektor menggunakan encoder permintaan, kemudian mencari melalui indeks pencarian dokumen kita untuk vektor relevan dalam dokumen yang terkait dengan input. Setelah selesai, ia mengonversi vektor input dan vektor dokumen menjadi teks dan meneruskannya melalui LLM.

### Pengambilan

Pengambilan terjadi ketika sistem mencoba dengan cepat menemukan dokumen dari indeks yang memenuhi kriteria pencarian. Tujuan retriever adalah mendapatkan dokumen yang akan digunakan untuk memberikan konteks dan menanamkan LLM pada data Anda.

Ada beberapa cara untuk melakukan pencarian dalam basis data kita seperti:

- **Pencarian kata kunci** - digunakan untuk pencarian teks.

- **Pencarian semantik** - menggunakan makna semantik dari kata-kata.

- **Pencarian vektor** - mengonversi dokumen dari teks ke representasi vektor menggunakan model embedding. Pengambilan dilakukan dengan menanyakan dokumen yang representasi vektornya paling dekat dengan pertanyaan pengguna.

- **Hibrida** - kombinasi antara pencarian kata kunci dan pencarian vektor.

Tantangan dengan pengambilan muncul ketika tidak ada respons yang mirip dengan permintaan dalam basis data, sistem kemudian akan mengembalikan informasi terbaik yang dapat mereka temukan, namun, Anda dapat menggunakan taktik seperti menetapkan jarak maksimum untuk relevansi atau menggunakan pencarian hibrida yang menggabungkan pencarian kata kunci dan vektor. Dalam pelajaran ini kita akan menggunakan pencarian hibrida, kombinasi antara pencarian vektor dan kata kunci. Kita akan menyimpan data kita ke dalam dataframe dengan kolom yang berisi potongan-potongan serta embedding.

### Kesamaan Vektor

Retriever akan mencari melalui basis pengetahuan untuk embedding yang berdekatan, tetangga terdekat, karena mereka adalah teks yang serupa. Dalam skenario di mana pengguna mengajukan permintaan, permintaan tersebut pertama-tama di-embed kemudian dicocokkan dengan embedding yang serupa. Pengukuran umum yang digunakan untuk menemukan seberapa mirip vektor yang berbeda adalah kesamaan kosinus yang didasarkan pada sudut antara dua vektor.

Kita dapat mengukur kesamaan menggunakan alternatif lain seperti jarak Euclidean yang merupakan garis lurus antara titik akhir vektor dan produk titik yang mengukur jumlah produk elemen-elemen yang sesuai dari dua vektor.

### Indeks Pencarian

Saat melakukan pengambilan, kita perlu membangun indeks pencarian untuk basis pengetahuan kita sebelum melakukan pencarian. Indeks akan menyimpan embedding kita dan dapat dengan cepat mengambil potongan yang paling mirip bahkan dalam basis data yang besar. Kita dapat membuat indeks kita secara lokal menggunakan:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Re-ranking

Setelah Anda melakukan pencarian dalam basis data, Anda mungkin perlu mengurutkan hasil dari yang paling relevan. LLM re-ranking memanfaatkan Pembelajaran Mesin untuk meningkatkan relevansi hasil pencarian dengan mengurutkannya dari yang paling relevan. Menggunakan Azure AI Search, re-ranking dilakukan secara otomatis untuk Anda menggunakan semantic reranker. Contoh cara kerja re-ranking menggunakan tetangga terdekat:

```python
# Find the most similar documents
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Print the most similar documents
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Menggabungkan semuanya

Langkah terakhir adalah menambahkan LLM kita ke dalam proses untuk mendapatkan respons yang ditanamkan pada data kita. Kita dapat mengimplementasikannya sebagai berikut:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Convert the question to a query vector
    query_vector = create_embeddings(user_input)

    # Find the most similar documents
    distances, indices = nbrs.kneighbors([query_vector])

    # add documents to query  to provide context
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # combine the history and the user input
    history.append(user_input)

    # create a message object
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": history[-1]}
    ]

    # use chat completion to generate a response
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```

## Mengevaluasi aplikasi kita

### Metrik Evaluasi

- Kualitas respons yang diberikan memastikan terdengar alami, lancar, dan seperti manusia.

- Penanaman data: mengevaluasi apakah respons berasal dari dokumen yang disediakan.

- Relevansi: mengevaluasi apakah respons sesuai dan terkait dengan pertanyaan yang diajukan.

- Kelancaran - apakah respons masuk akal secara tata bahasa.

## Kasus Penggunaan RAG (Retrieval Augmented Generation) dan basis data vektor

Ada banyak kasus penggunaan berbeda di mana pemanggilan fungsi dapat meningkatkan aplikasi Anda seperti:

- Tanya Jawab: menanamkan data perusahaan Anda ke dalam chat yang dapat digunakan oleh karyawan untuk mengajukan pertanyaan.

- Sistem Rekomendasi: di mana Anda dapat membuat sistem yang mencocokkan nilai-nilai yang paling mirip, misalnya film, restoran, dan banyak lagi.

- Layanan Chatbot: Anda dapat menyimpan riwayat chat dan mempersonalisasi percakapan berdasarkan data pengguna.

- Pencarian gambar berdasarkan embedding vektor, berguna saat melakukan pengenalan gambar dan deteksi anomali.

## Ringkasan

Kita telah membahas area fundamental RAG dari menambahkan data kita ke aplikasi, permintaan pengguna, dan output. Untuk menyederhanakan pembuatan RAG, Anda dapat menggunakan kerangka kerja seperti Semantic Kernel, Langchain, atau Autogen.

## Tugas

Untuk melanjutkan pembelajaran Anda tentang Retrieval Augmented Generation (RAG) Anda dapat membangun:

- Membuat front-end untuk aplikasi menggunakan kerangka kerja pilihan Anda.

- Memanfaatkan kerangka kerja, baik LangChain atau Semantic Kernel, dan membuat ulang aplikasi Anda.

Selamat telah menyelesaikan pelajaran ini 👏.

## Pembelajaran tidak berhenti di sini, lanjutkan Perjalanan Anda

Setelah menyelesaikan pelajaran ini, lihat [koleksi Pembelajaran AI Generatif kami](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk terus meningkatkan pengetahuan AI Generatif Anda!

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang salah yang timbul dari penggunaan terjemahan ini.