<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2210a0466c812d9defc4df2d9a709ff9",
  "translation_date": "2026-01-18T18:43:23+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "ms"
}
-->
# Retrieval Augmented Generation (RAG) dan Pangkalan Data Vektor

[![Retrieval Augmented Generation (RAG) and Vector Databases](../../../../../translated_images/ms/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Dalam pelajaran aplikasi carian, kita telah mempelajari secara ringkas bagaimana untuk mengintegrasikan data anda sendiri ke dalam Model Bahasa Besar (LLM). Dalam pelajaran ini, kita akan menyelami lebih lanjut tentang konsep memanfaatkan data anda dalam aplikasi LLM anda, mekanik proses tersebut dan kaedah untuk menyimpan data, termasuk kedua-dua embedding dan teks.

> **Video Akan Datang Tidak Lama Lagi**

## Pengenalan

Dalam pelajaran ini kami akan membincangkan perkara berikut:

- Pengenalan kepada RAG, apa itu dan mengapa ia digunakan dalam AI (kecerdasan buatan).

- Memahami apa itu pangkalan data vektor dan mencipta satu untuk aplikasi kita.

- Contoh praktikal bagaimana untuk mengintegrasikan RAG ke dalam aplikasi.

## Matlamat Pembelajaran

Selepas menamatkan pelajaran ini, anda akan dapat:

- Menjelaskan kepentingan RAG dalam pengambilan dan pemprosesan data.

- Menyediakan aplikasi RAG dan memanfaatkan data anda ke dalam LLM

- Integrasi berkesan RAG dan Pangkalan Data Vektor dalam Aplikasi LLM.

## Senario Kami: meningkatkan LLM kami dengan data kami sendiri

Untuk pelajaran ini, kami mahu menambah nota kami sendiri ke dalam startup pendidikan, yang membolehkan chatbot mendapatkan lebih banyak maklumat mengenai pelbagai subjek. Menggunakan nota yang kami ada, pelajar akan dapat belajar dengan lebih baik dan memahami pelbagai topik, menjadikan ia lebih mudah untuk ulang kaji untuk peperiksaan mereka. Untuk mencipta senario kami, kami akan menggunakan:

- `Azure OpenAI:` LLM yang akan kami gunakan untuk mencipta chatbot kami

- `Pelajaran AI untuk pemula mengenai Rangkaian Neural:` ini adalah data yang akan kami gunakan untuk memanfaatkan LLM kami

- `Azure AI Search` dan `Azure Cosmos DB:` pangkalan data vektor untuk menyimpan data kami dan mencipta indeks carian

Pengguna akan dapat mencipta kuiz latihan dari nota mereka, kad imbas ulang dan meringkaskan kepada gambaran ringkas. Untuk mula, mari kita lihat apa itu RAG dan bagaimana ia berfungsi:

## Retrieval Augmented Generation (RAG)

Chatbot yang dikuasakan oleh LLM memproses arahan pengguna untuk menghasilkan jawapan. Ia direka untuk menjadi interaktif dan berinteraksi dengan pengguna mengenai pelbagai topik. Walau bagaimanapun, jawapan yang diberikannya adalah terhad kepada konteks yang disediakan dan data latihan asasnya. Contohnya, GPT-4 mempunyai had pengetahuan sehingga September 2021, bermakna ia tidak mengetahui peristiwa yang berlaku selepas tempoh tersebut. Selain itu, data yang digunakan untuk melatih LLM tidak termasuk maklumat sulit seperti nota peribadi atau manual produk syarikat.

### Bagaimana RAG (Retrieval Augmented Generation) berfungsi

![drawing showing how RAGs work](../../../../../translated_images/ms/how-rag-works.f5d0ff63942bd3a6.webp)

Katakan anda ingin melancarkan chatbot yang menghasilkan kuiz dari nota anda, anda memerlukan sambungan ke pangkalan pengetahuan. Inilah kegunaan RAG. RAG beroperasi seperti berikut:

- **Pangkalan pengetahuan:** Sebelum pengambilan, dokumen ini perlu diingesti dan diproses terlebih dahulu, biasanya dengan memecah dokumen besar kepada bahagian yang lebih kecil, menukar mereka kepada embedding teks dan menyimpannya dalam pangkalan data.

- **Pertanyaan Pengguna:** pengguna mengemukakan soalan

- **Pengambilan:** Apabila pengguna mengemukakan soalan, model embedding mengambil maklumat relevan dari pangkalan pengetahuan untuk memberikan konteks lebih yang akan dimasukkan dalam arahan.

- **Generasi Bertambah:** LLM meningkatkan jawapan berdasarkan data yang diambil. Ini membolehkan jawapan bukan sahaja berdasarkan data pra-latih tetapi juga maklumat relevan dari konteks yang ditambah. Data yang diambil digunakan untuk memperkaya jawapan LLM. LLM kemudian mengembalikan jawapan kepada soalan pengguna.

![drawing showing how RAGs architecture](../../../../../translated_images/ms/encoder-decode.f2658c25d0eadee2.webp)

Seni bina untuk RAG dilaksanakan menggunakan transformer yang terdiri dari dua bahagian: encoder dan decoder. Contohnya, apabila pengguna mengemukakan soalan, teks input 'dienkodkan' ke dalam vektor yang menangkap makna perkataan dan vektor 'didekodkan' ke indeks dokumen kita dan menghasilkan teks baru berdasarkan pertanyaan pengguna. LLM menggunakan kedua-dua model encoder-decoder untuk menghasilkan output.

Dua pendekatan dalam melaksanakan RAG menurut kertas cadangan: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) adalah:

- **_RAG-Sequence_** menggunakan dokumen yang diambil untuk meramalkan jawapan terbaik kepada pertanyaan pengguna

- **RAG-Token** menggunakan dokumen untuk menghasilkan token seterusnya, kemudian mengambilnya untuk menjawab pertanyaan pengguna

### Kenapa anda perlu menggunakan RAG? 

- **Kekayaan maklumat:** memastikan jawapan teks adalah terkini dan sedia ada. Oleh itu meningkatkan prestasi dalam tugas khusus domain dengan mengakses pangkalan pengetahuan dalaman.

- Mengurangkan ciptaan palsu dengan menggunakan **data yang boleh disahkan** dalam pangkalan pengetahuan untuk memberikan konteks kepada pertanyaan pengguna.

- Ia adalah **berkesan kos** kerana ia lebih murah berbanding menala LLM secara mendalam

## Mencipta sebuah pangkalan pengetahuan

Aplikasi kami berdasarkan data peribadi kami iaitu, pelajaran Rangkaian Neural dalam kurikulum AI Untuk Pemula.

### Pangkalan Data Vektor

Pangkalan data vektor, berbeza dengan pangkalan data tradisional, adalah pangkalan data khusus yang direka untuk menyimpan, mengurus dan mencari vektor embedding. Ia menyimpan representasi nombor dokumen. Memecahkan data kepada embedding nombor memudahkan sistem AI kami memahami dan memproses data.

Kami menyimpan embedding kami dalam pangkalan data vektor kerana LLM mempunyai had bilangan token yang diterima sebagai input. Oleh kerana anda tidak boleh memindahkan keseluruhan embedding kepada LLM, kita perlu memecahkannya kepada bahagian-bahagian kecil dan apabila pengguna mengemukakan soalan, embedding yang paling serupa dengan soalan itu akan dikembalikan bersama arahan. Memecah juga mengurangkan kos pada jumlah token yang diproses oleh LLM.

Beberapa pangkalan data vektor yang popular termasuk Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant dan DeepLake. Anda boleh mencipta model Azure Cosmos DB menggunakan Azure CLI dengan arahan berikut:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Dari teks kepada embedding

Sebelum kami menyimpan data kami, kami perlu menukar ia kepada embedding vektor sebelum disimpan dalam pangkalan data. Jika anda bekerja dengan dokumen besar atau teks panjang, anda boleh memecahkannya berdasarkan pertanyaan yang anda jangka. Memecah boleh dilakukan pada peringkat ayat, atau perenggan. Oleh kerana pemecahan memperoleh makna dari perkataan di sekelilingnya, anda boleh menambah konteks lain pada sesebuah chunk, contohnya dengan menambah tajuk dokumen atau menyertakan beberapa teks sebelum atau selepas chunk itu. Anda boleh memecahkan data seperti berikut:

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

    # Jika bahagian terakhir tidak mencapai panjang minimum, tambahkannya juga
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Setelah dipecahkan, kita boleh melarutkan teks kita menggunakan pelbagai model embedding. Beberapa model yang boleh digunakan termasuk: word2vec, ada-002 oleh OpenAI, Azure Computer Vision dan banyak lagi. Pemilihan model bergantung kepada bahasa yang anda gunakan, jenis kandungan yang dienkod (teks/gambar/audio), saiz input yang boleh dienkod dan panjang keluaran embedding.

Contoh embedding teks menggunakan model OpenAI `text-embedding-ada-002` adalah:
![an embedding of the word cat](../../../../../translated_images/ms/cat.74cbd7946bc9ca38.webp)

## Pengambilan dan Carian Vektor

Apabila pengguna mengemukakan soalan, retriever menukar soalan itu kepada vektor menggunakan encoder pertanyaan, ia kemudian mencari menerusi indeks carian dokumen kami untuk vektor relevan dalam dokumen yang berkaitan dengan input. Setelah selesai, ia menukar kedua-dua vektor input dan vektor dokumen kepada teks dan menghantarnya melalui LLM.

### Pengambilan

Pengambilan berlaku apabila sistem cuba mencari dokumen dengan pantas dari indeks yang memenuhi kriteria carian. Matlamat retriever adalah mendapatkan dokumen yang akan digunakan untuk memberikan konteks dan memanfaatkan LLM dengan data anda.

Terdapat beberapa cara untuk melakukan carian dalam pangkalan data seperti:

- **Carian kata kunci** - digunakan untuk carian teks

- **Carian vektor** - menukar dokumen dari teks kepada representasi vektor menggunakan model embedding, membenarkan **carian semantik** menggunakan makna perkataan. Pengambilan dilakukan dengan mencari dokumen yang representasi vektornya paling hampir dengan soalan pengguna.

- **Hibrid** - gabungan carian kata kunci dan carian vektor.

Cabaran dalam pengambilan berlaku jika tiada jawapan serupa kepada pertanyaan dalam pangkalan data, sistem kemudiannya akan mengembalikan maklumat terbaik yang boleh diperoleh, namun anda boleh menggunakan taktik seperti menetapkan jarak maksimum untuk kesesuaian atau menggunakan carian hibrid yang menggabungkan kedua-dua kata kunci dan carian vektor. Dalam pelajaran ini kami akan menggunakan carian hibrid, gabungan carian vektor dan kata kunci. Kami akan menyimpan data kami dalam dataframe dengan lajur yang mengandungi chunk serta embedding.

### Kesamaan Vektor

Retriever akan mencari melalui pangkalan pengetahuan untuk embedding yang dekat antara satu sama lain, jiran terdekat, kerana mereka adalah teks yang serupa. Dalam senario apabila pengguna mengemukakan pertanyaan, ia pertama kali di-embed dan dipadankan dengan embedding serupa. Ukuran yang biasa digunakan untuk menentukan kesamaan vektor adalah kesamaan kosinus yang berdasarkan sudut antara dua vektor.

Kita boleh mengukur kesamaan menggunakan alternatif lain seperti jarak Euclidean yang merupakan garis lurus antara titik akhir vektor dan hasil darab titik yang mengukur jumlah hasil darab elemen yang bersesuaian dari dua vektor.

### Indeks carian

Apabila melakukan pengambilan, kita perlu membina indeks carian untuk pangkalan pengetahuan kita sebelum melakukan carian. Indeks menyimpan embedding kita dan boleh dengan cepat mengambil chunk yang paling serupa walaupun dalam pangkalan data yang besar. Kita boleh mencipta indeks secara tempatan dengan:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Cipta indeks carian
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Untuk menyoal indeks, anda boleh menggunakan kaedah kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```

### Penilaian semula

Setelah anda mengemukakan pertanyaan kepada pangkalan data, anda mungkin perlu menyusun keputusan daripada yang paling relevan. LLM penilai semula menggunakan Pembelajaran Mesin untuk meningkatkan kesesuaian hasil carian dengan menyusunnya mengikut keutamaan. Menggunakan Azure AI Search, penilaian semula dilakukan secara automatik melalui penilai semula bersemantik. Contoh bagaimana penilaian semula berfungsi menggunakan jiran terdekat:

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

Langkah terakhir adalah menambahkan LLM kita ke dalam campuran untuk dapatkan jawapan yang berasaskan data kita. Kita boleh melaksanakannya seperti berikut:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Tukar soalan kepada vektor pertanyaan
    query_vector = create_embeddings(user_input)

    # Cari dokumen yang paling serupa
    distances, indices = nbrs.kneighbors([query_vector])

    # tambah dokumen kepada pertanyaan untuk menyediakan konteks
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # gabungkan sejarah dan input pengguna
    history.append(user_input)

    # cipta objek mesej
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # gunakan penyelesaian sembang untuk menghasilkan respons
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```

## Menilai aplikasi kami

### Metodologi Penilaian

- Kualiti jawapan yang diberikan memastikan ia kedengaran semula jadi, lancar dan seperti manusia

- Keteguhan data: menilai sama ada jawapan datang dari dokumen yang disediakan

- Kesesuaian: menilai jawapan sesuai dan berkaitan dengan soalan yang ditanya

- Kelancaran - sama ada jawapan masuk akal dari segi tatabahasa

## Kes Penggunaan untuk menggunakan RAG (Retrieval Augmented Generation) dan pangkalan data vektor

Banyak kes penggunaan berlainan di mana panggilan fungsi boleh meningkatkan aplikasi anda seperti:

- Soalan dan Jawapan: memanfaatkan data syarikat anda ke chat yang boleh digunakan oleh pekerja untuk bertanya soalan.

- Sistem Cadangan: di mana anda boleh mencipta sistem yang memadankan nilai paling serupa contohnya filem, restoran dan banyak lagi.

- Perkhidmatan chatbot: anda boleh menyimpan sejarah perbualan dan mempersonalisasi perbualan berdasarkan data pengguna.

- Carian imej berdasarkan embedding vektor, berguna dalam pengenalan imej dan pengesanan anomali.

## Rumusan

Kami telah membincangkan bidang asas RAG dari menambah data dalam aplikasi, pertanyaan pengguna dan output. Untuk memudahkan penciptaan RAG, anda boleh menggunakan rangka kerja seperti Semanti Kernel, Langchain atau Autogen.

## Tugasan

Untuk meneruskan pembelajaran Retrieval Augmented Generation (RAG) anda boleh membina:

- Bangunkan front-end untuk aplikasi menggunakan rangka kerja pilihan anda

- Gunakan rangka kerja, sama ada LangChain atau Semantic Kernel, dan bina semula aplikasi anda.

Tahniah kerana menamatkan pelajaran 👏.

## Pembelajaran tidak berhenti di sini, teruskan Perjalanan

Selepas menamatkan pelajaran ini, lihat koleksi [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan Generative AI anda!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, harap maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->