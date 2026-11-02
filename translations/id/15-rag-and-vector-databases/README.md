# Generasi Ditingkatkan dengan Pengambilan (RAG) dan Basis Data Vektor

[![Generasi Ditingkatkan dengan Pengambilan (RAG) dan Basis Data Vektor](../../../translated_images/id/15-lesson-banner.ac49e59506175d4f.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Dalam pelajaran aplikasi pencarian, kita sedikit mempelajari bagaimana mengintegrasikan data Anda sendiri ke dalam Model Bahasa Besar (LLM). Dalam pelajaran ini, kita akan mendalami lebih jauh konsep dasar data Anda dalam aplikasi LLM Anda, mekanika prosesnya, dan metode penyimpanan data, termasuk baik embeddings maupun teks.

> **Video Segera Hadir**

## Pendahuluan

Dalam pelajaran ini kita akan membahas hal berikut:

- Pengantar tentang RAG, apa itu dan mengapa digunakan dalam AI (kecerdasan buatan).

- Memahami apa itu basis data vektor dan membuatnya untuk aplikasi kita.

- Contoh praktis tentang cara mengintegrasikan RAG ke dalam aplikasi.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan dapat:

- Menjelaskan pentingnya RAG dalam pengambilan dan pemrosesan data.

- Menyiapkan aplikasi RAG dan mendasar LLM dengan data Anda

- Mengintegrasikan RAG dan basis data vektor secara efektif dalam aplikasi LLM.

## Skenario Kita: meningkatkan LLM kita dengan data kita sendiri

Untuk pelajaran ini, kita ingin menambahkan catatan kita sendiri ke startup pendidikan, yang memungkinkan chatbot mendapatkan lebih banyak informasi tentang berbagai subjek. Dengan menggunakan catatan yang kita miliki, pelajar dapat belajar lebih baik dan memahami berbagai topik, sehingga lebih mudah untuk mengulang pelajaran untuk ujian mereka. Untuk membuat skenario kita, kita akan menggunakan:

- `Azure OpenAI:` LLM yang akan kita gunakan untuk membuat chatbot kita

- `AI for beginners' lesson on Neural Networks`: ini akan menjadi data yang menjadi dasar LLM kita

- `Azure AI Search` dan `Azure Cosmos DB:` basis data vektor untuk menyimpan data dan membuat indeks pencarian

Pengguna dapat membuat kuis latihan dan flashcard revisi dari catatan mereka serta meringkas catatan tersebut menjadi ikhtisar yang ringkas. Untuk memulai, mari kita lihat apa itu RAG dan bagaimana cara kerjanya:

## Generasi Ditingkatkan dengan Pengambilan (RAG)

Chatbot yang didukung oleh LLM memproses prompt pengguna untuk menghasilkan respons. Dirancang untuk interaktif dan berinteraksi dengan pengguna pada berbagai topik. Namun, responsnya terbatas pada konteks yang diberikan dan data pelatihan dasarnya. Sebagai contoh, batas pengetahuan GPT-4 adalah September 2021, artinya, ia tidak memiliki pengetahuan tentang kejadian yang terjadi setelah periode tersebut. Selain itu, data yang digunakan untuk melatih LLM tidak mencakup informasi rahasia seperti catatan pribadi atau manual produk perusahaan.

### Bagaimana RAG (Generasi Ditingkatkan dengan Pengambilan) bekerja

![gambar yang menunjukkan cara kerja RAG](../../../translated_images/id/how-rag-works.f5d0ff63942bd3a6.webp?WT.mc_id=academic-105485-koreyst)

Misalkan Anda ingin menerapkan chatbot yang membuat kuis dari catatan Anda, Anda membutuhkan koneksi ke basis pengetahuan. Di sinilah RAG berperan. RAG bekerja sebagai berikut:

- **Basis pengetahuan:** Sebelum pengambilan, dokumen ini perlu diproses dan dipersiapkan, biasanya dengan memecah dokumen besar menjadi bagian-bagian kecil, mengubahnya menjadi embedding teks, dan menyimpannya di basis data.

- **Pertanyaan Pengguna:** pengguna mengajukan pertanyaan

- **Pengambilan:** Ketika pengguna mengajukan pertanyaan, model embedding mengambil informasi relevan dari basis pengetahuan untuk memberikan konteks tambahan yang akan dimasukkan ke prompt.

- **Generasi Ditingkatkan:** LLM meningkatkan responsnya berdasarkan data yang diambil. Ini memungkinkan respons yang dihasilkan tidak hanya didasarkan pada data pelatihan tetapi juga informasi relevan dari konteks tambahan. Data yang diambil digunakan untuk meningkatkan respons LLM. LLM kemudian mengembalikan jawaban untuk pertanyaan pengguna.

![Diagram yang menunjukkan arsitektur RAG](../../../translated_images/id/encoder-decode.f2658c25d0eadee2.webp?WT.mc_id=academic-105485-koreyst)

RAG menggabungkan pengambil dengan generator: pertanyaan diubah menjadi vektor, dicocokkan dengan indeks dokumen untuk menemukan bagian teks relevan, dan bagian itu disediakan sebagai konteks ke LLM, yang menghasilkan respons. Pengambil dan generator dapat menggunakan model berbeda; RAG tidak memerlukan transformer encoder-decoder.

Dua pendekatan saat mengimplementasikan RAG menurut makalah yang diusulkan: [Retrieval-Augmented Generation for Knowledge intensive NLP (pemrosesan bahasa alami) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) adalah:

- **_RAG-Sequence_** menggunakan dokumen yang diambil untuk memprediksi jawaban terbaik untuk pertanyaan pengguna

- **RAG-Token** menggunakan dokumen untuk menghasilkan token berikutnya, kemudian mengambilnya untuk menjawab pertanyaan pengguna

### Mengapa Anda menggunakan RAG?

- **Kekayaan informasi:** memastikan respons teks mutakhir dan terbaru. Oleh karena itu, meningkatkan kinerja pada tugas domain spesifik dengan mengakses basis pengetahuan internal.

- Mengurangi fabrikasi dengan menggunakan **data yang dapat diverifikasi** dalam basis pengetahuan untuk memberikan konteks pada pertanyaan pengguna.

- Ini **hemat biaya** karena lebih ekonomis dibandingkan melakukan fine-tuning pada LLM

## Membuat basis pengetahuan

Aplikasi kita didasarkan pada data pribadi kita, yaitu pelajaran Neural Network dari kurikulum AI untuk Pemula.

### Basis Data Vektor

Basis data vektor, berbeda dengan basis data tradisional, adalah basis data khusus yang dirancang untuk menyimpan, mengelola, dan mencari vektor embedding. Basis data ini menyimpan representasi numerik dokumen. Memecah data menjadi embedding numerik memudahkan sistem AI kita memahami dan memproses data.

Karena LLM memiliki batas jumlah token input, kita memecah dokumen menjadi potongan sebelum membuat embedding. Ketika pengguna mengajukan pertanyaan, embedding yang paling mirip dengan query mengidentifikasi potongan teks relevan, yang dikembalikan bersama prompt. Pemecahan potongan juga mengurangi jumlah token yang diteruskan ke LLM dan karenanya dapat mengurangi biaya.

Beberapa basis data vektor populer termasuk Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant, dan DeepLake. Anda dapat membuat model Azure Cosmos DB menggunakan Azure CLI dengan perintah berikut:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Dari teks ke embedding

Sebelum kita menyimpan data, kita perlu mengubahnya menjadi embedding vektor sebelum disimpan di basis data. Jika Anda bekerja dengan dokumen besar atau teks panjang, Anda bisa memecahnya berdasarkan pertanyaan yang diharapkan. Pemecahan potongan bisa dilakukan di tingkat kalimat, atau tingkat paragraf. Karena pemecahan potongan mengambil makna dari kata-kata di sekitarnya, Anda bisa menambahkan konteks lain ke potongan, misalnya dengan menambahkan judul dokumen atau memasukkan teks sebelum atau sesudah potongan. Anda bisa memecah data seperti berikut:

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

Setelah dipotong, kita bisa memasukkan teks kita ke dalam berbagai model embedding. Beberapa model yang bisa Anda gunakan antara lain: word2vec, ada-002 oleh OpenAI, Azure Computer Vision, dan banyak lagi. Pemilihan model untuk digunakan akan bergantung pada bahasa yang Anda gunakan, jenis konten yang dikodekan (teks/gambar/audio), ukuran input yang dapat dikodekan, dan panjang output embedding.

Contoh teks embedding menggunakan model `text-embedding-ada-002` OpenAI adalah:
![embedding dari kata cat](../../../translated_images/id/cat.74cbd7946bc9ca38.webp?WT.mc_id=academic-105485-koreyst)

## Pengambilan dan Pencarian Vektor

Ketika pengguna mengajukan pertanyaan, pengambil mengubahnya menjadi vektor menggunakan pengkode query, kemudian mencari di indeks pencarian dokumen kita untuk vektor relevan di dokumen yang terkait dengan input. Setelah selesai, ia mengubah vektor input dan vektor dokumen menjadi teks dan meneruskannya ke LLM.

### Pengambilan

Pengambilan terjadi ketika sistem berusaha dengan cepat menemukan dokumen dari indeks yang memenuhi kriteria pencarian. Tujuan pengambil adalah memperoleh dokumen yang akan digunakan untuk memberikan konteks dan mendasar LLM pada data Anda.

Ada beberapa cara melakukan pencarian dalam basis data kita seperti:

- **Pencarian kata kunci** - digunakan untuk pencarian teks

- **Pencarian vektor** - mengubah dokumen dari teks menjadi representasi vektor menggunakan model embedding, memungkinkan pencarian **semantik** menggunakan arti kata. Pengambilan dilakukan dengan mengajukan pertanyaan pada dokumen yang representasi vektornya paling dekat dengan pertanyaan pengguna.

- **Hibrida** - kombinasi antara pencarian kata kunci dan vektor.

Tantangan pada pengambilan muncul ketika tidak ada respons serupa untuk query dalam basis data, sistem akan mengembalikan informasi terbaik yang bisa didapat, namun Anda bisa menggunakan taktik seperti mengatur jarak maksimum untuk relevansi atau menggunakan pencarian hibrida yang mengombinasikan pencarian kata kunci dan vektor. Dalam pelajaran ini kita akan menggunakan pencarian hibrida, kombinasi pencarian vektor dan kata kunci. Kita akan menyimpan data ke dalam dataframe dengan kolom yang berisi potongan serta embedding.

### Kesamaan Vektor

Pengambil akan mencari di database pengetahuan embedding yang berdekatan—tetangga terdekat—karena mereka mewakili teks yang mirip. Dalam skenario ini, saat pengguna mengajukan query, query tersebut terlebih dahulu di-embedding, kemudian dicocokkan dengan embedding serupa. Pengukuran yang paling umum digunakan untuk membandingkan kesamaan vektor adalah cosine similarity, yang didasarkan pada sudut antara dua vektor.

Metode lain yang bisa kita gunakan untuk mengukur kesamaan termasuk jarak Euclidean, yaitu garis lurus antara titik ujung vektor, dan dot product, yang mengukur jumlah produk elemen-elemen yang bersesuaian dalam dua vektor.

### Indeks pencarian

Saat melakukan pengambilan, kita perlu membangun indeks pencarian untuk basis pengetahuan sebelum pencarian dilakukan. Indeks akan menyimpan embedding dan dapat dengan cepat mengambil potongan paling mirip bahkan di basis data yang besar. Kita bisa membuat indeks secara lokal menggunakan:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Penyusunan ulang peringkat

Setelah Anda mengajukan query ke basis data, Anda mungkin perlu mengurutkan hasil dari yang paling relevan. LLM penyusun ulang peringkat memanfaatkan Pembelajaran Mesin untuk meningkatkan relevansi hasil pencarian dengan mengurutkannya dari yang paling relevan. Dengan Azure AI Search, penyusunan ulang peringkat dilakukan secara otomatis menggunakan penyusun ulang semantic. Contoh cara kerja penyusunan ulang peringkat menggunakan tetangga terdekat:

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

- Kualitas respons yang diberikan, memastikan terdengar alami, lancar, dan seperti manusia

- Keterdasaran data: mengevaluasi apakah respons berasal dari dokumen yang diberikan

- Relevansi: mengevaluasi apakah respons sesuai dan terkait dengan pertanyaan yang diajukan

- Kelancaran - apakah respons masuk akal secara tata bahasa

## Kasus Penggunaan untuk menggunakan RAG (Generasi Ditingkatkan dengan Pengambilan) dan basis data vektor

Ada banyak kasus penggunaan berbeda di mana RAG dapat meningkatkan aplikasi Anda, seperti:

- Tanya Jawab: mendasar data perusahaan Anda ke dalam chat yang dapat digunakan oleh karyawan untuk mengajukan pertanyaan.

- Sistem Rekomendasi: di mana Anda dapat membuat sistem yang mencocokkan nilai paling mirip misalnya film, restoran, dan banyak lagi.

- Layanan chatbot: Anda dapat menyimpan riwayat obrolan dan mempersonalisasi percakapan berdasarkan data pengguna.

- Pencarian gambar berdasarkan embedding vektor, berguna saat melakukan pengenalan gambar dan deteksi anomali.

## Ringkasan

Kita telah membahas area fundamental RAG dari menambahkan data kita ke aplikasi, pertanyaan pengguna hingga keluaran. Untuk mempermudah pembuatan RAG, Anda dapat menggunakan kerangka kerja seperti Semantic Kernel, LangChain atau AutoGen.

## Tugas

Untuk melanjutkan pembelajaran Anda tentang Generasi Ditingkatkan dengan Pengambilan (RAG) Anda dapat membangun:

- Membangun front-end untuk aplikasi menggunakan kerangka kerja pilihan Anda

- Memanfaatkan kerangka kerja, baik LangChain atau Semantic Kernel, dan membuat ulang aplikasi Anda.

Selamat telah menyelesaikan pelajaran 👏.

## Pembelajaran tidak berhenti di sini, lanjutkan Perjalanan

Setelah menyelesaikan pelajaran ini, lihat koleksi [Pembelajaran AI Generatif kami](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk terus meningkatkan pengetahuan AI Generatif Anda!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->