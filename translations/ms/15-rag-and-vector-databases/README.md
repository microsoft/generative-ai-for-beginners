# Penjanaan Dipertingkatkan dengan Pencarian (RAG) dan Pangkalan Data Vektor

[![Penjanaan Dipertingkatkan dengan Pencarian (RAG) dan Pangkalan Data Vektor](../../../translated_images/ms/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Dalam pelajaran aplikasi carian, kami secara ringkas mempelajari cara mengintegrasikan data sendiri ke dalam Model Bahasa Besar (LLMs). Dalam pelajaran ini, kita akan mendalami lagi konsep pemerkasaan data anda dalam aplikasi LLM anda, mekanik proses tersebut dan kaedah penyimpanan data, termasuk kedua-dua embeddings dan teks.

> **Video Akan Datang Tidak Lama Lagi**

## Pengenalan

Dalam pelajaran ini kami akan membincangkan perkara berikut:

- Pengenalan kepada RAG, apa itu dan mengapa ia digunakan dalam AI (kecerdasan buatan).

- Memahami apa itu pangkalan data vektor dan mencipta satu untuk aplikasi kami.

- Contoh praktikal bagaimana mengintegrasikan RAG ke dalam sebuah aplikasi.

## Matlamat Pembelajaran

Selepas menyelesaikan pelajaran ini, anda akan dapat:

- Menjelaskan kepentingan RAG dalam pengambilan dan pemprosesan data.

- Menyediakan aplikasi RAG dan memerkasakan data anda ke LLM

- Integrasi berkesan RAG dan Pangkalan Data Vektor dalam Aplikasi LLM.

## Senario Kami: meningkatkan LLM kami dengan data kami sendiri

Untuk pelajaran ini, kami mahu menambah nota kami sendiri ke dalam startup pendidikan, yang membolehkan chatbot mendapatkan lebih banyak maklumat mengenai subjek yang berbeza. Menggunakan nota yang kami ada, pelajar akan dapat belajar dengan lebih baik dan memahami topik-topik berbeza, menjadikannya lebih mudah untuk mengulangkaji untuk peperiksaan mereka. Untuk mencipta senario kami, kami akan menggunakan:

- `Azure OpenAI:` LLM yang akan kami gunakan untuk mencipta chatbot kami

- `Pelajaran AI untuk pemula tentang Rangkaian Neural`: ini akan menjadi data yang kami perkasakan LLM kami

- `Azure AI Search` dan `Azure Cosmos DB:` pangkalan data vektor untuk menyimpan data kami dan mencipta indeks carian

Pengguna akan dapat mencipta kuiz latihan daripada nota mereka, kad imbasan ulangkaji dan meringkaskannya menjadi ulasan ringkas. Untuk bermula, mari kita lihat apa itu RAG dan bagaimana ia berfungsi:

## Penjanaan Dipertingkatkan dengan Pencarian (RAG)

Chatbot kuasa LLM memproses arahan pengguna untuk menjana respons. Ia direka untuk interaktif dan berinteraksi dengan pengguna mengenai pelbagai topik. Walau bagaimanapun, responsnya terhad kepada konteks yang disediakan dan data latihan asasnya. Sebagai contoh, had pengetahuan GPT-4 adalah September 2021, bermakna, ia tidak mempunyai pengetahuan tentang peristiwa yang berlaku selepas tempoh ini. Selain itu, data yang digunakan untuk melatih LLM mengecualikan maklumat sulit seperti nota peribadi atau manual produk syarikat.

### Bagaimana RAG (Penjanaan Dipertingkatkan dengan Pencarian) berfungsi

![lukisan menunjukkan bagaimana RAG berfungsi](../../../translated_images/ms/how-rag-works.f5d0ff63942bd3a6.webp)

Misalnya anda ingin melancarkan chatbot yang mencipta kuiz daripada nota anda, anda memerlukan sambungan ke pangkalan pengetahuan. Di sinilah RAG membantu. RAG beroperasi seperti berikut:

- **Pangkalan pengetahuan:** Sebelum pengambilan, dokumen ini perlu dimasukkan dan diproses terlebih dahulu, biasanya memecahkan dokumen besar kepada kepingan kecil, menukarnya kepada teks embedding dan menyimpannya dalam pangkalan data.

- **Pertanyaan Pengguna:** pengguna bertanya soalan

- **Pengambilan:** Apabila pengguna bertanya soalan, model embedding mengambil maklumat berkaitan daripada pangkalan pengetahuan kami untuk memberikan lebih konteks yang akan dimasukkan ke dalam arahan.

- **Penjanaan Dipertingkatkan:** LLM meningkatkan respons berdasarkan data yang diperoleh. Ini membolehkan respons yang dijana bukan sahaja berdasarkan data pralatih tetapi juga maklumat relevan dari konteks tambahan. Data yang diperoleh digunakan untuk memerkasakan respons LLM. LLM kemudian mengembalikan jawapan kepada soalan pengguna.

![lukisan menunjukkan seni bina RAG](../../../translated_images/ms/encoder-decode.f2658c25d0eadee2.webp)

Seni bina untuk RAG dilaksanakan menggunakan transformer yang terdiri daripada dua bahagian: pengekod dan penyahkod. Contohnya, apabila pengguna bertanya soalan, teks input 'dienkod' menjadi vektor yang menangkap maksud perkataan dan vektor tersebut 'didekod' ke dalam indeks dokumen kami dan menjana teks baru berdasarkan pertanyaan pengguna. LLM menggunakan model encoder-decoder untuk menjana output.

Dua pendekatan apabila melaksanakan RAG menurut kertas cadangan: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) adalah:

- **_RAG-Sequence_** menggunakan dokumen yang diperoleh untuk meramalkan jawapan terbaik kepada pertanyaan pengguna

- **RAG-Token** menggunakan dokumen untuk menjana token seterusnya, kemudian mengambilnya untuk menjawab pertanyaan pengguna

### Mengapa anda perlu menggunakan RAG? 

- **Kekayaan maklumat:** memastikan respons teks adalah terkini dan semasa. Oleh itu, ia meningkatkan prestasi dalam tugas khusus domain dengan mengakses pangkalan pengetahuan dalaman.

- Mengurangkan rekaan dengan menggunakan **data yang boleh disahkan** dalam pangkalan pengetahuan untuk memberikan konteks kepada pertanyaan pengguna.

- Ia adalah **berkos efektif** kerana ia lebih ekonomik berbanding penalaan halus LLM

## Mencipta pangkalan pengetahuan

Aplikasi kami berdasarkan data peribadi kami iaitu pelajaran Rangkaian Neural dalam kurikulum AI Untuk Pemula.

### Pangkalan Data Vektor

Pangkalan data vektor, berbeza dengan pangkalan data tradisional, adalah pangkalan data khusus yang direka untuk menyimpan, mengurus dan mencari vektor yang dibenamkan. Ia menyimpan representasi berangka dokumen. Memecahkan data kepada embeddings berangka memudahkan sistem AI kami memahami dan memproses data.

Kami menyimpan embeddings kami dalam pangkalan data vektor kerana LLM mempunyai had bilangan token yang diterima sebagai input. Oleh kerana anda tidak boleh memberikan keseluruhan embeddings kepada LLM, kami perlu memecahkannya kepada kepingan dan apabila pengguna bertanya soalan, embeddings yang paling serupa dengan soalan akan dikembalikan bersama dengan arahan. Pecahan juga mengurangkan kos berdasarkan bilangan token yang dihantar melalui LLM.

Beberapa pangkalan data vektor popular termasuk Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant dan DeepLake. Anda boleh mencipta model Azure Cosmos DB menggunakan CLI Azure dengan arahan berikut:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Dari teks ke embeddings

Sebelum kami menyimpan data kami, kami perlu menukarnya menjadi embeddings vektor sebelum ia disimpan dalam pangkalan data. Jika anda bekerja dengan dokumen besar atau teks panjang, anda boleh memecahkannya berdasarkan pertanyaan yang dijangka. Pecahan boleh dilakukan pada peringkat ayat, atau pada peringkat perenggan. Oleh kerana pecahan mendapat makna dari perkataan sekitar, anda boleh menambah beberapa konteks lain ke dalam pecahan itu, contohnya, dengan menambah tajuk dokumen atau memasukkan beberapa teks sebelum atau selepas pecahan. Anda boleh memecahkan data seperti berikut:

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

    # Jika bahagian terakhir tidak mencapai panjang minimum, tambahkan juga
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Setelah dipecahkan, kami boleh menyematkan teks kami menggunakan model embedding yang berbeza. Beberapa model yang boleh anda gunakan termasuk: word2vec, ada-002 oleh OpenAI, Azure Computer Vision dan banyak lagi. Pemilihan model yang digunakan bergantung pada bahasa yang anda gunakan, jenis kandungan yang disandikan (teks/gambar/audio), saiz input yang boleh disandikan dan panjang output embedding.

Contoh teks disematkan menggunakan model `text-embedding-ada-002` dari OpenAI adalah:
![embedding perkataan kucing](../../../translated_images/ms/cat.74cbd7946bc9ca38.webp)

## Pengambilan dan Carian Vektor

Apabila pengguna bertanya soalan, pengambil mengubahnya menjadi vektor menggunakan penyandi pertanyaan, kemudian mencari melalui indeks carian dokumen kami untuk vektor yang relevan dalam dokumen yang berkaitan dengan input. Setelah selesai, ia menukar kedua-dua vektor input dan vektor dokumen ke dalam teks dan menghantarnya melalui LLM.

### Pengambilan

Pengambilan berlaku apabila sistem cuba mencari dokumen dari indeks yang memenuhi kriteria carian dengan cepat. Matlamat pengambil adalah mendapatkan dokumen yang akan digunakan untuk memberikan konteks dan memerkasakan LLM pada data anda.

Terdapat beberapa cara untuk melakukan carian dalam pangkalan data kami seperti:

- **Carian kata kunci** - digunakan untuk carian teks

- **Carian vektor** - menukar dokumen dari teks ke representasi vektor menggunakan model embedding, membolehkan **carian semantik** menggunakan maksud perkataan. Pengambilan dilakukan dengan menyoal dokumen yang representasi vektornya paling hampir dengan soalan pengguna.

- **Hibrid** - gabungan kedua-dua carian kata kunci dan vektor.

Cabaran dengan pengambilan muncul apabila tiada respons serupa dengan pertanyaan dalam pangkalan data, sistem akan mengembalikan maklumat terbaik yang boleh didapati, namun, anda boleh menggunakan taktik seperti menetapkan jarak maksimum untuk kaitan atau menggunakan carian hibrid yang menggabungkan kedua-dua carian kata kunci dan vektor. Dalam pelajaran ini kami akan menggunakan carian hibrid, gabungan kedua-dua carian vektor dan kata kunci. Kami akan menyimpan data kami dalam dataframe dengan lajur yang mengandungi kepingan serta embeddings.

### Kesamaan Vektor

Pengambil akan mencari melalui pangkalan pengetahuan untuk embeddings yang hampir bersama, jiran terdekat, kerana mereka adalah teks yang serupa. Dalam senario, apabila pengguna bertanya soalan, ia pertama disematkan kemudian dipadankan dengan embeddings serupa. Ukuran biasa yang digunakan untuk mengukur betapa serupa vektor yang berbeza ialah kesamaan kosinus yang berdasarkan sudut antara dua vektor.

Kita boleh mengukur kesamaan menggunakan alternatif lain yang boleh digunakan adalah jarak Euclidean iaitu garisan lurus antara titik akhir vektor dan produk dot yang mengukur jumlah hasil darab elemen-elemen sepadan dua vektor.

### Indeks carian

Apabila melakukan pengambilan, kita perlu membina indeks carian untuk pangkalan pengetahuan kita sebelum melakukan carian. Indeks akan menyimpan embeddings kita dan boleh dengan cepat mengambil kepingan paling serupa walaupun dalam pangkalan data besar. Kita boleh mencipta indeks kita secara tempatan menggunakan:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Cipta indeks carian
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Untuk membuat kueri pada indeks, anda boleh menggunakan kaedah kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```

### Penyusunan semula

Setelah anda menyoal pangkalan data, anda mungkin perlu menyusun hasil dari yang paling relevan. LLM penyusun semula menggunakan Pembelajaran Mesin untuk meningkatkan kaitan hasil carian dengan mengaturnya dari yang paling relevan. Menggunakan Azure AI Search, penyusunan semula dilakukan secara automatik untuk anda menggunakan penyusun semula semantik. Contoh bagaimana penyusunan semula berfungsi menggunakan jiran terdekat:

```python
# Cari dokumen yang paling serupa
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Cetak dokumen yang paling serupa
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

Langkah terakhir adalah menambah LLM kami ke dalam campuran untuk dapat memperoleh respons yang berasaskan data kami. Kami boleh melaksanakannya seperti berikut:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Tukar soalan kepada vektor pertanyaan
    query_vector = create_embeddings(user_input)

    # Cari dokumen yang paling serupa
    distances, indices = nbrs.kneighbors([query_vector])

    # tambah dokumen kepada pertanyaan untuk memberikan konteks
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # gabungkan sejarah dan input pengguna
    history.append(user_input)

    # buat objek mesej
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # gunakan API Respon untuk menjana respons
    response = client.responses.create(
        model="gpt-5-mini",
        max_output_tokens=800,
        input=messages,
        store=False,
    )

    return response.output_text

chatbot(user_input)
```

## Menilai aplikasi kami

### Metrik Penilaian

- Kualiti respons yang diberikan memastikan ia kedengaran semula jadi, lancar dan seperti manusia

- Pemerkasaan data: menilai sama ada respons datang dari dokumen yang disediakan

- Kaitannya: menilai respons padan dan berkaitan dengan soalan yang ditanya

- Kefasihan - sama ada respons masuk akal dari segi tatabahasa

## Kes Penggunaan untuk menggunakan RAG (Penjanaan Dipertingkatkan dengan Pencarian) dan pangkalan data vektor

Terdapat banyak kes penggunaan di mana panggilan fungsi boleh memperbaiki aplikasi anda seperti:

- Soal Jawab: memerkasakan data syarikat anda ke dalam chat yang boleh digunakan oleh pekerja untuk bertanya soalan.

- Sistem Cadangan: di mana anda boleh mencipta sistem yang memadankan nilai paling serupa contohnya filem, restoran dan banyak lagi.

- Perkhidmatan chatbot: anda boleh menyimpan sejarah chat dan mempersonalisasikan perbualan berdasarkan data pengguna.

- Carian imej berdasarkan embeddings vektor, berguna untuk pengenalan imej dan pengesanan anomali.

## Ringkasan

Kami telah membincangkan aspek asas RAG daripada menambah data kami ke aplikasi, pertanyaan pengguna dan output. Untuk memudahkan penciptaan RAG, anda boleh menggunakan rangka kerja seperti Semanti Kernel, Langchain atau Autogen.

## Tugasan

Untuk meneruskan pembelajaran Penjanaan Dipertingkatkan dengan Pencarian (RAG), anda boleh membina:

- Membangunkan antaramuka hadapan untuk aplikasi menggunakan rangka kerja pilihan anda

- Menggunakan rangka kerja, sama ada LangChain atau Semantic Kernel, dan mencipta semula aplikasi anda.

Tahniah kerana menamatkan pelajaran 👏.

## Pembelajaran tidak berhenti di sini, teruskan perjalanan

Selepas menamatkan pelajaran ini, lihat koleksi [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif anda!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->