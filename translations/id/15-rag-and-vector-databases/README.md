# Retrieval Augmented Generation (RAG) dan Basis Data Vektor

[![Retrieval Augmented Generation (RAG) dan Basis Data Vektor](../../../translated_images/id/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Dalam pelajaran aplikasi pencarian, kita secara singkat mempelajari cara mengintegrasikan data Anda sendiri ke dalam Large Language Models (LLMs). Dalam pelajaran ini, kita akan membahas lebih dalam tentang konsep membumikan data Anda dalam aplikasi LLM, mekanisme prosesnya, dan metode penyimpanan data, termasuk embedding dan teks.

> **Video Segera Hadir**

## Pendahuluan

Dalam pelajaran ini kita akan membahas hal-hal berikut:

- Pengenalan RAG, apa itu dan mengapa digunakan dalam AI (kecerdasan buatan).

- Memahami apa itu basis data vektor dan membuat satu untuk aplikasi kita.

- Contoh praktis bagaimana mengintegrasikan RAG ke dalam aplikasi.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan mampu:

- Menjelaskan pentingnya RAG dalam pengambilan dan pemrosesan data.

- Menyiapkan aplikasi RAG dan membumikan data Anda ke LLM

- Integrasi efektif RAG dan Basis Data Vektor dalam Aplikasi LLM.

## Skenario Kami: meningkatkan LLM kami dengan data kami sendiri

Untuk pelajaran ini, kami ingin menambahkan catatan kami sendiri ke startup pendidikan, yang memungkinkan chatbot mendapatkan lebih banyak informasi tentang berbagai subjek. Dengan menggunakan catatan yang kami miliki, pembelajar akan dapat belajar lebih baik dan memahami berbagai topik, sehingga lebih mudah untuk mengulang pelajaran sebelum ujian. Untuk membuat skenario kami, kami akan menggunakan:

- `Azure OpenAI:` LLM yang akan kami gunakan untuk membuat chatbot kami

- `Pelajaran AI untuk pemula tentang Jaringan Saraf`: ini akan menjadi data yang membumikan LLM kami

- `Azure AI Search` dan `Azure Cosmos DB:` basis data vektor untuk menyimpan data kami dan membuat indeks pencarian

Pengguna akan dapat membuat kuis latihan dari catatan mereka, kartu flash pengulangan dan meringkasnya menjadi rangkuman singkat. Untuk memulai, mari kita lihat apa itu RAG dan bagaimana cara kerjanya:

## Retrieval Augmented Generation (RAG)

Chatbot bertenaga LLM memproses prompt pengguna untuk menghasilkan respons. Dirancang untuk interaktif dan berinteraksi dengan pengguna pada berbagai topik. Namun, responsnya terbatas pada konteks yang diberikan dan data pelatihan dasarnya. Misalnya, GPT-4 memiliki batas pengetahuan sampai September 2021, artinya, tidak mengetahui kejadian setelah periode tersebut. Selain itu, data yang digunakan untuk melatih LLM mengecualikan informasi rahasia seperti catatan pribadi atau manual produk perusahaan.

### Cara kerja RAG (Retrieval Augmented Generation)

![gambar yang menunjukkan cara kerja RAG](../../../translated_images/id/how-rag-works.f5d0ff63942bd3a6.webp)

Misalkan Anda ingin menerapkan chatbot yang membuat kuis dari catatan Anda, Anda memerlukan koneksi ke basis pengetahuan. Di sinilah RAG berperan. RAG bekerja sebagai berikut:

- **Basis pengetahuan:** Sebelum pengambilan, dokumen ini perlu dimasukkan dan diproses sebelumnya, biasanya dengan memecah dokumen besar menjadi potongan-potongan kecil, mengubahnya menjadi embedding teks dan menyimpannya dalam basis data.

- **Query pengguna:** pengguna mengajukan pertanyaan

- **Pengambilan:** Ketika pengguna mengajukan pertanyaan, model embedding mengambil informasi relevan dari basis pengetahuan kita untuk menyediakan konteks tambahan yang akan dimasukkan ke dalam prompt.

- **Generasi bertambah:** LLM meningkatkan responsnya berdasarkan data yang diambil. Ini memungkinkan respons yang dihasilkan tidak hanya berdasarkan data pra-latih tetapi juga informasi relevan dari konteks tambahan. Data yang diambil digunakan untuk memperkaya respons LLM. LLM kemudian mengembalikan jawaban atas pertanyaan pengguna.

![gambar yang menunjukkan arsitektur RAG](../../../translated_images/id/encoder-decode.f2658c25d0eadee2.webp)

Arsitektur RAG diimplementasikan menggunakan transformer yang terdiri dari dua bagian: encoder dan decoder. Misalnya, ketika pengguna mengajukan pertanyaan, teks input 'diencode' menjadi vektor yang menangkap makna kata dan vektor tersebut 'didecode' ke indeks dokumen kita dan menghasilkan teks baru berdasarkan query pengguna. LLM menggunakan model encoder-decoder untuk menghasilkan output.

Dua pendekatan dalam mengimplementasikan RAG menurut paper yang diusulkan: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) adalah:

- **_RAG-Sequence_** menggunakan dokumen yang diambil untuk memprediksi jawaban terbaik untuk query pengguna

- **RAG-Token** menggunakan dokumen untuk menghasilkan token berikutnya, kemudian mengambil dokumen tersebut untuk menjawab query pengguna

### Mengapa Anda menggunakan RAG? 

- **Kekayaan informasi:** memastikan respons teks adalah terkini dan up to date. Oleh karena itu, meningkatkan kinerja pada tugas spesifik domain dengan mengakses basis pengetahuan internal.

- Mengurangi fabrikasi dengan memanfaatkan **data yang dapat diverifikasi** dalam basis pengetahuan untuk memberikan konteks pada query pengguna.

- **Biaya efektif** karena lebih ekonomis dibandingkan melakukan fine-tuning LLM

## Membuat basis pengetahuan

Aplikasi kita berdasarkan pada data pribadi kita yaitu pelajaran Jaringan Saraf pada kurikulum AI Untuk Pemula.

### Basis Data Vektor

Basis data vektor, berbeda dengan basis data tradisional, adalah basis data khusus yang dirancang untuk menyimpan, mengelola dan mencari embedded vektor. Ini menyimpan representasi numerik dari dokumen. Memecah data menjadi embedding numerik memudahkan sistem AI kami untuk memahami dan memproses data.

Kami menyimpan embedding kami dalam basis data vektor karena LLM memiliki batas jumlah token yang mereka terima sebagai input. Karena Anda tidak bisa melewatkan seluruh embedding ke LLM, kita perlu memecahnya menjadi potongan kecil dan ketika pengguna mengajukan pertanyaan, embedding yang paling mirip dengan pertanyaan akan dikembalikan bersama dengan prompt. Pemecahan juga mengurangi biaya dari jumlah token yang diteruskan ke LLM.

Beberapa basis data vektor populer termasuk Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant dan DeepLake. Anda dapat membuat model Azure Cosmos DB menggunakan Azure CLI dengan perintah berikut:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Dari teks ke embedding

Sebelum kita menyimpan data, kita harus mengubahnya menjadi embedding vektor terlebih dahulu sebelum disimpan di basis data. Jika Anda bekerja dengan dokumen besar atau teks panjang, Anda dapat memecahnya berdasarkan query yang Anda perkirakan. Pemecahan dapat dilakukan pada tingkat kalimat, atau tingkat paragraf. Karena pemecahan mengambil makna dari kata-kata di sekitarnya, Anda dapat menambahkan konteks lain ke sebuah potongan, contohnya, dengan menambahkan judul dokumen atau menyertakan beberapa teks sebelum atau sesudah potongan tersebut. Anda dapat memecah data sebagai berikut:

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

    # Jika potongan terakhir tidak mencapai panjang minimum, tetap tambahkan
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Setelah dipotong, kita bisa menyematkan teks kita menggunakan berbagai model embedding. Beberapa model yang dapat digunakan meliputi: word2vec, ada-002 oleh OpenAI, Azure Computer Vision dan banyak lagi. Memilih model yang digunakan tergantung pada bahasa yang Anda gunakan, jenis konten yang dikodekan (teks/gambar/audio), ukuran input yang dapat dikodekan dan panjang keluaran embedding.

Contoh teks embedding menggunakan model `text-embedding-ada-002` dari OpenAI adalah:
![embedding kata cat](../../../translated_images/id/cat.74cbd7946bc9ca38.webp)

## Pengambilan dan Pencarian Vektor

Ketika pengguna mengajukan pertanyaan, retriever mengubahnya menjadi sebuah vektor menggunakan query encoder, kemudian mencari melalui indeks pencarian dokumen kita untuk vektor yang relevan dalam dokumen yang terkait dengan masukan. Setelah selesai, ia mengonversi baik vektor input dan vektor dokumen menjadi teks dan melewatkannya melalui LLM.

### Pengambilan

Pengambilan terjadi ketika sistem mencoba dengan cepat menemukan dokumen dari indeks yang memenuhi kriteria pencarian. Tujuan retriever adalah mendapatkan dokumen yang akan digunakan untuk memberikan konteks dan membumikan LLM pada data Anda.

Ada beberapa cara melakukan pencarian dalam basis data kita seperti:

- **Pencarian kata kunci** - digunakan untuk pencarian teks

- **Pencarian vektor** - mengubah dokumen dari teks ke representasi vektor menggunakan model embedding, memungkinkan **pencarian semantik** menggunakan makna kata. Pengambilan akan dilakukan dengan meng-query dokumen yang representasi vektornya paling dekat dengan pertanyaan pengguna.

- **Hibrida** - gabungan dari pencarian kata kunci dan vektor.

Tantangan pengambilan muncul ketika tidak ada respons serupa di basis data, sistem kemudian akan mengembalikan informasi terbaik yang bisa didapat, namun Anda bisa menggunakan taktik seperti mengatur jarak maksimum untuk relevansi atau menggunakan pencarian hibrida yang menggabungkan kata kunci dan pencarian vektor. Dalam pelajaran ini kita akan menggunakan pencarian hibrida, kombinasi pencarian vektor dan kata kunci. Kita akan menyimpan data ke dalam dataframe dengan kolom yang berisi potongan serta embedding.

### Kemiripan Vektor

Retriever akan mencari di basis pengetahuan embedding yang berdekatan, tetangga terdekat, karena teks tersebut mirip. Dalam skenario pengguna mengajukan query, query tersebut pertama di-embed lalu dicocokkan dengan embedding serupa. Pengukuran umum yang digunakan untuk mengetahui seberapa mirip vektor yang berbeda adalah kemiripan kosinus (cosine similarity) yang berdasarkan sudut antara dua vektor.

Kita dapat mengukur kemiripan menggunakan alternatif lain seperti jarak Euclidean yaitu garis lurus antara ujung vektor dan dot product yang mengukur jumlah hasil perkalian elemen-elemen yang bersesuaian dari dua vektor.

### Indeks pencarian

Saat melakukan pengambilan, kita perlu membangun indeks pencarian untuk basis pengetahuan sebelum melakukan pencarian. Indeks akan menyimpan embedding kita dan dapat dengan cepat mengambil potongan serupa meskipun dalam basis data yang besar. Kita dapat membuat indeks secara lokal menggunakan:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Buat indeks pencarian
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Untuk menanyakan indeks, Anda dapat menggunakan metode kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```

### Penyusunan ulang peringkat (Re-ranking)

Setelah Anda melakukan query ke basis data, Anda mungkin perlu mengurutkan hasil dari yang paling relevan. LLM reranking memanfaatkan Machine Learning untuk meningkatkan relevansi hasil pencarian dengan mengurutkannya dari yang paling relevan. Menggunakan Azure AI Search, penyusunan ulang peringkat dilakukan otomatis menggunakan semantic reranker. Contoh cara kerja reranking dengan tetangga terdekat:

```python
# Temukan dokumen yang paling mirip
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Cetak dokumen yang paling mirip
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Menyatukan semuanya

Langkah terakhir adalah menambahkan LLM kita sehingga dapat memberikan respons yang dibumikan pada data kita. Kita dapat mengimplementasikannya sebagai berikut:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Ubah pertanyaan menjadi vektor kueri
    query_vector = create_embeddings(user_input)

    # Temukan dokumen yang paling mirip
    distances, indices = nbrs.kneighbors([query_vector])

    # tambahkan dokumen ke kueri untuk memberikan konteks
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # gabungkan riwayat dan masukan pengguna
    history.append(user_input)

    # buat objek pesan
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # gunakan API Respon untuk menghasilkan respons
    response = client.responses.create(
        model="gpt-5-mini",
        max_output_tokens=800,
        input=messages,
        store=False,
    )

    return response.output_text

chatbot(user_input)
```

## Mengevaluasi aplikasi kita

### Metode Evaluasi

- Kualitas respons yang diberikan memastikan terdengar alami, lancar dan seperti manusia

- Groundedness data: mengevaluasi apakah respons berasal dari dokumen yang diberikan

- Relevansi: mengevaluasi apakah respons cocok dan terkait dengan pertanyaan yang diajukan

- Kelancaran - apakah respons masuk akal secara gramatikal

## Kasus Penggunaan untuk menggunakan RAG (Retrieval Augmented Generation) dan basis data vektor

Ada banyak kasus penggunaan berbeda dimana panggilan fungsi dapat meningkatkan aplikasi Anda seperti:

- Tanya Jawab: membumikan data perusahaan Anda ke chat yang dapat digunakan oleh karyawan untuk mengajukan pertanyaan.

- Sistem Rekomendasi: dimana Anda dapat membuat sistem yang mencocokkan nilai paling mirip misalnya film, restoran dan lain-lain.

- Layanan chatbot: Anda dapat menyimpan riwayat chat dan mempersonalisasi percakapan berdasarkan data pengguna.

- Pencarian gambar berbasis embedding vektor, berguna saat melakukan pengenalan gambar dan deteksi anomali.

## Ringkasan

Kita telah membahas area dasar RAG mulai dari penambahan data ke aplikasi, query pengguna sampai output. Untuk mempermudah pembuatan RAG, Anda dapat menggunakan kerangka kerja seperti Semanti Kernel, Langchain atau Autogen.

## Tugas

Untuk melanjutkan pembelajaran Retrieval Augmented Generation (RAG) Anda dapat membangun:

- Bangun front-end untuk aplikasi menggunakan framework pilihan Anda

- Manfaatkan framework, baik LangChain atau Semantic Kernel, lalu buat ulang aplikasi Anda.

Selamat telah menyelesaikan pelajaran ini 👏.

## Pembelajaran tidak berhenti di sini, teruskan Perjalanan Anda

Setelah menyelesaikan pelajaran ini, lihat koleksi [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan Anda tentang Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->