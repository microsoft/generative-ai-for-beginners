# Retrieval Augmented Generation (RAG) dan Database Vektor

[![Retrieval Augmented Generation (RAG) dan Database Vektor](../../../translated_images/id/15-lesson-banner.ac49e59506175d4f.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Dalam pelajaran aplikasi pencarian, kami secara singkat belajar bagaimana mengintegrasikan data Anda sendiri ke dalam Large Language Models (LLMs). Dalam pelajaran ini, kami akan menyelami lebih jauh konsep memasang data Anda dalam aplikasi LLM Anda, mekanisme prosesnya dan metode untuk menyimpan data, termasuk baik embeddings maupun teks.

> **Video Segera Hadir**

## Pendahuluan

Dalam pelajaran ini, kita akan membahas hal-hal berikut:

- Pengenalan tentang RAG, apa itu dan mengapa digunakan dalam AI (kecerdasan buatan).

- Memahami apa itu database vektor dan membuatnya untuk aplikasi kita.

- Contoh praktis bagaimana mengintegrasikan RAG dalam sebuah aplikasi.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan bisa:

- Menjelaskan pentingnya RAG dalam pengambilan dan pemrosesan data.

- Mengatur aplikasi RAG dan menancapkan LLM dengan data Anda

- Mengintegrasikan RAG dan database vektor secara efektif dalam aplikasi LLM.

## Skenario Kami: meningkatkan LLM kami dengan data kami sendiri

Untuk pelajaran ini, kami ingin menambahkan catatan kami sendiri ke startup pendidikan, yang memungkinkan chatbot mendapatkan lebih banyak informasi tentang berbagai mata pelajaran. Dengan menggunakan catatan yang kami miliki, pelajar dapat belajar lebih baik dan memahami berbagai topik, sehingga memudahkan untuk mengulang pelajaran mereka untuk ujian. Untuk membuat skenario kami, kami akan menggunakan:

- `Azure OpenAI:` LLM yang akan kami gunakan untuk membuat chatbot kami

- `AI for beginners' lesson on Neural Networks`: ini akan menjadi data yang kita tanamkan pada LLM kami

- `Azure AI Search` dan `Azure Cosmos DB:` database vektor untuk menyimpan data kami dan membuat indeks pencarian

Pengguna akan dapat membuat kuis latihan dan flashcard untuk mengulang dari catatan mereka serta meringkas catatan tersebut menjadi ringkasan singkat. Untuk memulai, mari kita lihat apa itu RAG dan bagaimana cara kerjanya:

## Retrieval Augmented Generation (RAG)

Chatbot yang didukung LLM memproses prompt pengguna untuk menghasilkan respons. Ini dirancang agar interaktif dan berinteraksi dengan pengguna dalam berbagai topik. Namun, responsnya terbatas pada konteks yang diberikan dan data pelatihan dasarnya. Misalnya, cutoff pengetahuan GPT-4 adalah September 2021, artinya, ia tidak mengetahui peristiwa yang terjadi setelah periode ini. Selain itu, data yang digunakan untuk melatih LLM mengecualikan informasi rahasia seperti catatan pribadi atau manual produk perusahaan.

### Bagaimana RAG (Retrieval Augmented Generation) bekerja

![gambar yang menunjukkan cara kerja RAG](../../../translated_images/id/how-rag-works.f5d0ff63942bd3a6.webp?WT.mc_id=academic-105485-koreyst)

Misalkan Anda ingin menerapkan chatbot yang membuat kuis dari catatan Anda, Anda akan memerlukan koneksi ke basis pengetahuan. Di sinilah RAG membantu. RAG bekerja sebagai berikut:

- **Basis pengetahuan:** Sebelum pengambilan, dokumen-dokumen ini perlu dimasukkan dan diproses terlebih dahulu, biasanya dengan memecah dokumen besar menjadi potongan-potongan lebih kecil, mengubahnya menjadi embedding teks dan menyimpannya dalam database.

- **Pertanyaan Pengguna:** pengguna mengajukan pertanyaan

- **Pengambilan:** Saat pengguna mengajukan pertanyaan, model embedding mengambil informasi relevan dari basis pengetahuan untuk memberikan konteks lebih yang akan dimasukkan ke prompt.

- **Augmented Generation:** LLM meningkatkan responsnya berdasarkan data yang diambil. Ini memungkinkan respons yang dibuat tidak hanya berdasarkan data pra-latih tetapi juga informasi relevan dari konteks tambahan. Data yang diambil digunakan untuk memperkuat respons LLM. LLM kemudian memberikan jawaban atas pertanyaan pengguna.

![Diagram yang menunjukkan arsitektur RAG](../../../translated_images/id/encoder-decode.f2658c25d0eadee2.webp?WT.mc_id=academic-105485-koreyst)

RAG menggabungkan retriever dengan generator: query diubah menjadi vektor, dicocokkan dengan indeks dokumen untuk menemukan potongan teks relevan, dan potongan tersebut diberikan sebagai konteks ke LLM, yang menghasilkan respons. Retriever dan generator bisa menggunakan model yang berbeda; RAG tidak memerlukan encoder-decoder transformer.

Dua pendekatan saat mengimplementasikan RAG menurut makalah yang diusulkan: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) adalah:

- **_RAG-Sequence_** menggunakan dokumen yang diambil untuk memprediksi jawaban terbaik atas pertanyaan pengguna

- **RAG-Token** menggunakan dokumen untuk menghasilkan token berikutnya, kemudian mengambilnya untuk menjawab pertanyaan pengguna

### Mengapa Anda harus menggunakan RAG? 

- **Kekayaan informasi:** memastikan respons teks selalu terbaru dan aktual. Ini meningkatkan performa pada tugas spesifik domain dengan mengakses basis pengetahuan internal.

- Mengurangi fabrikasi dengan menggunakan **data yang dapat diverifikasi** dalam basis pengetahuan untuk memberikan konteks pada pertanyaan pengguna.

- Ini **hemat biaya** karena lebih ekonomis dibandingkan melakukan fine-tuning pada LLM

## Membuat basis pengetahuan

Aplikasi kami didasarkan pada data pribadi kami, yaitu pelajaran Neural Network dari kurikulum AI untuk Pemula.

### Database Vektor

Database vektor, berbeda dengan database tradisional, adalah database khusus yang dirancang untuk menyimpan, mengelola, dan mencari vektor embedded. Ia menyimpan representasi numerik dari dokumen. Memecah data menjadi embedding numerik memudahkan sistem AI kami untuk memahami dan memproses data.

Karena LLM memiliki batasan jumlah token masukan, dokumen kami bagi menjadi potongan-potongan sebelum diembed. Saat pengguna mengajukan pertanyaan, embedding yang paling mirip dengan query mengidentifikasi potongan teks relevan, yang dikembalikan dengan prompt. Pemecahan potongan juga mengurangi jumlah token yang diberikan ke LLM dan oleh karena itu dapat mengurangi biaya.

Beberapa database vektor populer termasuk Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant dan DeepLake. Anda dapat membuat model Azure Cosmos DB menggunakan Azure CLI dengan perintah berikut:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Dari teks ke embeddings

Sebelum menyimpan data kita, kita perlu mengubahnya menjadi vector embeddings sebelum disimpan dalam database. Jika Anda bekerja dengan dokumen besar atau teks panjang, Anda dapat memotongnya berdasarkan query yang Anda harapkan. Pemecahan potongan bisa dilakukan pada tingkat kalimat, atau paragraf. Karena pemecahan potongan mengambil makna dari kata-kata di sekitarnya, Anda bisa menambahkan konteks lain ke potongan, misalnya dengan menambahkan judul dokumen atau menyertakan teks sebelum atau sesudah potongan. Anda dapat memecah data sebagai berikut:

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

Setelah dipotong, kita kemudian dapat mengembed teks menggunakan berbagai model embedding. Beberapa model yang bisa digunakan termasuk: word2vec, ada-002 oleh OpenAI, Azure Computer Vision, dan banyak lagi. Pemilihan model tergantung pada bahasa yang digunakan, jenis konten yang dikodekan (teks/gambar/audio), ukuran input yang bisa dikodekan dan panjang output embedding.

Contoh teks embedded menggunakan model `text-embedding-ada-002` dari OpenAI adalah:
![embedding dari kata kucing](../../../translated_images/id/cat.74cbd7946bc9ca38.webp?WT.mc_id=academic-105485-koreyst)

## Pengambilan dan Pencarian Vektor

Ketika pengguna mengajukan pertanyaan, retriever mengubahnya menjadi vektor menggunakan query encoder, kemudian mencari melalui indeks pencarian dokumen kami untuk vektor relevan dalam dokumen yang terkait dengan input. Setelah selesai, kedua vektor input dan dokumen diubah menjadi teks dan dilewatkan ke LLM.

### Pengambilan

Pengambilan terjadi saat sistem mencoba dengan cepat menemukan dokumen dari indeks yang memenuhi kriteria pencarian. Tujuan retriever adalah mendapatkan dokumen yang akan digunakan untuk memberikan konteks dan menancapkan LLM pada data Anda.

Ada beberapa cara melakukan pencarian dalam database kami seperti:

- **Pencarian kata kunci** - digunakan untuk pencarian teks

- **Pencarian vektor** - mengubah dokumen dari teks ke representasi vektor menggunakan model embedding, memungkinkan **pencarian semantik** menggunakan makna kata. Pengambilan dilakukan dengan menanyakan dokumen yang representasi vektornya paling dekat dengan pertanyaan pengguna.

- **Hibrida** - kombinasi pencarian kata kunci dan pencarian vektor.

Tantangan dalam pengambilan muncul ketika tidak ada respons yang mirip dengan query dalam database, sistem kemudian akan mengembalikan informasi terbaik yang bisa didapat, namun Anda dapat menggunakan taktik seperti mengatur jarak maksimum untuk relevansi atau menggunakan pencarian hibrida yang menggabungkan pencarian kata kunci dan vektor. Dalam pelajaran ini kami akan menggunakan pencarian hibrida, kombinasi pencarian vektor dan kata kunci. Kami akan menyimpan data dalam dataframe dengan kolom yang berisi potongan serta embedding.

### Kesamaan Vektor

Retriever akan mencari melalui basis pengetahuan untuk embeddings yang berdekatan—tetangga terdekat—karena mereka mewakili teks yang mirip. Dalam skenario ini, ketika pengguna mengirim query, ia terlebih dahulu di-embed dan kemudian dicocokkan dengan embedding serupa. Pengukuran yang paling umum digunakan untuk membandingkan kesamaan vektor adalah cosine similarity, yang didasarkan pada sudut antara dua vektor.

Metode lain yang dapat digunakan untuk mengukur kesamaan termasuk jarak Euclidean, yang merupakan garis lurus antara ujung vektor, dan dot product, yang mengukur jumlah produk elemen-elemen yang bersesuaian dalam dua vektor.

### Indeks pencarian

Saat melakukan pengambilan, kita perlu membangun indeks pencarian untuk basis pengetahuan kita sebelum melakukan pencarian. Indeks akan menyimpan embedding dan dapat dengan cepat mengambil potongan paling mirip bahkan dalam database besar. Kita dapat membuat indeks secara lokal menggunakan:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Penyortiran ulang

Setelah Anda melakukan query pada database, Anda mungkin perlu mengurutkan hasil dari yang paling relevan. LLM penyortir ulang menggunakan Machine Learning untuk meningkatkan relevansi hasil pencarian dengan mengurutkannya dari yang paling relevan. Menggunakan Azure AI Search, penyortiran ulang dilakukan otomatis untuk Anda menggunakan semantic reranker. Contoh cara kerja penyortiran ulang menggunakan tetangga terdekat:

```python
# Find the most similar documents
distances, indices = nbrs.kneighbors([query_vector])

# Print the three most similar documents with their distance to the question
for distance, index in zip(distances[0][:3], indices[0][:3]):
    print(flattened_df['chunks'].iloc[index])
    print(flattened_df['path'].iloc[index])
    print(distance)
```

## Menggabungkan semuanya

Langkah terakhir adalah menambahkan LLM kita ke dalam campuran agar bisa mendapatkan respons yang didasarkan pada data kita. Kita dapat mengimplementasikannya sebagai berikut:

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
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # use the Responses API to generate a response
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

### Metrik Evaluasi

- Kualitas respons yang diberikan memastikan terdengar alami, lancar dan seperti manusia

- Keterkaitan data: mengevaluasi apakah respons berasal dari dokumen yang diberikan

- Relevansi: mengevaluasi apakah respons sesuai dan terkait dengan pertanyaan yang diajukan

- Kelancaran - apakah respons masuk akal secara tata bahasa

## Kasus Penggunaan untuk menggunakan RAG (Retrieval Augmented Generation) dan database vektor

Ada banyak kasus penggunaan berbeda di mana RAG dapat meningkatkan aplikasi Anda, seperti:

- Tanya Jawab: menanamkan data perusahaan Anda ke dalam chat yang dapat digunakan karyawan untuk mengajukan pertanyaan.

- Sistem Rekomendasi: di mana Anda dapat membuat sistem yang mencocokkan nilai paling mirip misalnya film, restoran dan banyak lagi.

- Layanan Chatbot: Anda dapat menyimpan riwayat chat dan mempersonalisasi obrolan berdasarkan data pengguna.

- Pencarian gambar berdasarkan embedding vektor, berguna saat melakukan pengenalan gambar dan deteksi anomali.

## Ringkasan

Kita telah membahas area dasar RAG mulai dari menambahkan data kita ke aplikasi, query pengguna, dan output. Untuk memudahkan pembuatan RAG, Anda dapat menggunakan kerangka kerja seperti Semantic Kernel, LangChain atau AutoGen.

## Tugas

Untuk melanjutkan pembelajaran Anda tentang Retrieval Augmented Generation (RAG) Anda dapat membangun:

- Bangun front-end untuk aplikasi menggunakan framework pilihan Anda

- Manfaatkan framework, baik LangChain atau Semantic Kernel, dan buat ulang aplikasi Anda.

Selamat telah menyelesaikan pelajaran 👏.

## Pembelajaran tidak berhenti di sini, lanjutkan Perjalanan Anda

Setelah menyelesaikan pelajaran ini, lihat koleksi [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan Generative AI Anda!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->