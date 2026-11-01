# Penjanaan Dipertingkatkan dengan Pengambilan (RAG) dan Pangkalan Data Vektor

[![Penjanaan Dipertingkatkan dengan Pengambilan (RAG) dan Pangkalan Data Vektor](../../../translated_images/ms/15-lesson-banner.ac49e59506175d4f.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Dalam pelajaran aplikasi carian, kita secara ringkas mempelajari cara mengintegrasikan data anda sendiri ke dalam Model Bahasa Besar (LLM). Dalam pelajaran ini, kita akan menyelami lebih lanjut konsep meletakkan asas data anda dalam aplikasi LLM anda, mekanik proses tersebut dan kaedah untuk menyimpan data, termasuk kedua-dua pembenaman dan teks.

> **Video Akan Datang Tidak Lama Lagi**

## Pengenalan

Dalam pelajaran ini kita akan membincangkan perkara berikut:

- Pengenalan kepada RAG, apakah ia dan mengapa ia digunakan dalam AI (kecerdasan buatan).

- Memahami apakah pangkalan data vektor dan mencipta satu untuk aplikasi kita.

- Contoh praktikal bagaimana mengintegrasikan RAG ke dalam aplikasi.

## Matlamat Pembelajaran

Selepas menyelesaikan pelajaran ini, anda akan boleh:

- Jelaskan kepentingan RAG dalam pengambilan dan pemprosesan data.

- Menyediakan aplikasi RAG dan meletakkan asas LLM dengan data anda

- Mengintegrasikan RAG dan pangkalan data vektor secara berkesan dalam aplikasi LLM.

## Senario Kita: meningkatkan LLM kita dengan data kita sendiri

Untuk pelajaran ini, kita mahu menambah nota kita sendiri ke dalam startup pendidikan, yang membolehkan chatbot mendapat maklumat lebih lanjut mengenai pelbagai subjek. Dengan menggunakan nota yang kita ada, pelajar akan dapat belajar dengan lebih baik dan faham pelbagai topik, menjadikannya lebih mudah untuk ulang kaji bagi peperiksaan mereka. Untuk mencipta senario kita, kita akan menggunakan:

- `Azure OpenAI:` LLM yang akan kita gunakan untuk mencipta chatbot kita

- `AI for beginners' lesson on Neural Networks`: ini akan menjadi data yang kita letakkan asas LLM kita padanya

- `Azure AI Search` dan `Azure Cosmos DB:` pangkalan data vektor untuk menyimpan data kita dan mencipta indeks carian

Pengguna akan dapat membuat kuiz latihan dan kad ulang kaji dari nota mereka dan meringkaskan nota tersebut menjadi gambaran ringkas. Untuk mula, mari kita lihat apa itu RAG dan bagaimana ia berfungsi:

## Penjanaan Dipertingkatkan dengan Pengambilan (RAG)

Chatbot yang dikuasakan oleh LLM memproses arahan pengguna untuk menghasilkan jawapan. Ia direka untuk interaktif dan berinteraksi dengan pengguna mengenai pelbagai topik. Walau bagaimanapun, jawapannya terhad kepada konteks yang diberi dan data latihan asasnya. Sebagai contoh, had pengetahuan GPT-4 ialah September 2021, bermakna, ia tidak mengetahui peristiwa yang berlaku selepas tempoh itu. Selain itu, data yang digunakan untuk melatih LLM mengecualikan maklumat sulit seperti nota peribadi atau manual produk syarikat.

### Bagaimana RAG (Penjanaan Dipertingkatkan dengan Pengambilan) berfungsi

![lukisan menunjukkan bagaimana RAG berfungsi](../../../translated_images/ms/how-rag-works.f5d0ff63942bd3a6.webp?WT.mc_id=academic-105485-koreyst)

Katakan anda ingin menjalankan chatbot yang mencipta kuiz dari nota anda, anda memerlukan sambungan ke pangkalan pengetahuan. Di sinilah RAG memainkan peranan. RAG beroperasi seperti berikut:

- **Pangkalan pengetahuan:** Sebelum pengambilan, dokumen ini perlu dimasukkan dan dipra-proses, biasanya memecahkan dokumen besar kepada bahagian lebih kecil, menukarnya kepada pembenaman teks dan menyimpannya dalam pangkalan data.

- **Soalan Pengguna:** pengguna bertanya soalan

- **Pengambilan:** Apabila pengguna bertanya soalan, model pembenaman mengeluarkan maklumat berkaitan dari pangkalan pengetahuan kita untuk memberikan konteks tambahan yang akan digabungkan dalam arahan.

- **Penjanaan Dipertingkatkan:** LLM meningkatkan jawapannya berdasarkan data yang diperoleh. Ia membolehkan jawapan yang dijana bukan sahaja berdasarkan data latihan sebelumnya tetapi juga maklumat berkaitan dari konteks yang ditambah. Data yang diperoleh digunakan untuk memperkayakan jawapan LLM. LLM kemudian memberikan jawapan kepada soalan pengguna.

![Diagram menunjukkan seni bina RAG](../../../translated_images/ms/encoder-decode.f2658c25d0eadee2.webp?WT.mc_id=academic-105485-koreyst)

RAG menggabungkan pengambil dan penjana: soalan ditukar menjadi vektor, dipadankan dengan indeks dokumen untuk mencari bahagian teks berkaitan, dan bahagian tersebut diberikan sebagai konteks kepada LLM, yang menjana jawapan. Pengambil dan penjana mungkin menggunakan model yang berbeza; RAG tidak memerlukan transformer penyandi-pemudah.

Dua pendekatan apabila melaksanakan RAG mengikut kertas cadangan: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) adalah:

- **_RAG-Sequence_** menggunakan dokumen yang diambil untuk meramal jawapan terbaik kepada pertanyaan pengguna

- **RAG-Token** menggunakan dokumen untuk menjana token seterusnya, kemudian mengambilnya untuk menjawab pertanyaan pengguna

### Mengapa anda ingin menggunakan RAG? 

- **Kekayaan maklumat:** memastikan respons teks adalah terkini dan semasa. Oleh itu, ia meningkatkan prestasi pada tugas khusus domain dengan mengakses pangkalan pengetahuan dalaman.

- Mengurangkan rekaan dengan menggunakan **data yang boleh disahkan** dalam pangkalan pengetahuan untuk memberikan konteks kepada pertanyaan pengguna.

- Ia adalah **berkesan dari segi kos** kerana ia lebih ekonomik berbanding menyesuaikan LLM

## Mewujudkan pangkalan pengetahuan

Aplikasi kami berdasarkan data peribadi kami, iaitu pelajaran Neural Network daripada kurikulum AI for Beginners.

### Pangkalan Data Vektor

Pangkalan data vektor, tidak seperti pangkalan data tradisional, adalah pangkalan data khusus yang direka untuk menyimpan, mengurus dan mencari vektor terbenam. Ia menyimpan perwakilan berangka dokumen. Memecahkan data kepada terbenam berangka memudahkan sistem AI kami memahami dan memproses data.

Oleh kerana LLM mempunyai had pada bilangan token input, kami memecahkan dokumen kepada ketulan sebelum menanamkannya. Apabila pengguna bertanya soalan, terbenam yang paling serupa dengan pertanyaan akan mengenal pasti ketulan teks yang relevan, yang dikembalikan bersama arahan. Pemecahan ketulan juga mengurangkan bilangan token yang dihantar ke LLM dan oleh itu boleh mengurangkan kos.

Beberapa pangkalan data vektor popular termasuk Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant dan DeepLake. Anda boleh membuat model Azure Cosmos DB menggunakan Azure CLI dengan arahan berikut:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Dari teks ke terbenam

Sebelum kami menyimpan data kami, kami perlu menukarnya kepada terbenam vektor sebelum ia disimpan dalam pangkalan data. Jika anda bekerja dengan dokumen besar atau teks panjang, anda boleh memecahkan mereka berdasarkan pertanyaan yang anda jangkakan. Pemecahan boleh dilakukan pada tahap ayat, atau pada tahap perenggan. Oleh kerana pemecahan ketulan memperoleh makna daripada perkataan di sekelilingnya, anda boleh menambah beberapa konteks lain pada ketulan, contohnya, dengan menambah tajuk dokumen atau memasukkan beberapa teks sebelum atau selepas ketulan. Anda boleh memecahkan data seperti berikut:

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

Setelah dipecahkan, kami boleh menanam teks kami menggunakan model terbenam yang berbeza. Beberapa model yang anda boleh gunakan termasuk: word2vec, ada-002 oleh OpenAI, Azure Computer Vision dan banyak lagi. Pemilihan model untuk digunakan bergantung pada bahasa yang anda gunakan, jenis kandungan yang dienkod (teks/gambar/audio), saiz input yang boleh dienkod dan panjang output terbenam.

Contoh teks yang ditanam menggunakan model `text-embedding-ada-002` OpenAI adalah:
![satu terbenam perkataan cat](../../../translated_images/ms/cat.74cbd7946bc9ca38.webp?WT.mc_id=academic-105485-koreyst)

## Pencarian dan Carian Vektor

Apabila pengguna bertanya soalan, pengambil akan mengubahnya menjadi vektor menggunakan pengekod pertanyaan, kemudian ia mencari melalui indeks carian dokumen kami untuk vektor yang relevan dalam dokumen yang berkaitan dengan input. Setelah selesai, ia menukar kedua-dua vektor input dan vektor dokumen menjadi teks dan menghantarnya melalui LLM.

### Pencarian

Pencarian berlaku apabila sistem cuba mencari dengan cepat dokumen dari indeks yang memenuhi kriteria carian. Matlamat pengambil adalah untuk mendapatkan dokumen yang akan digunakan untuk memberikan konteks dan mendasari LLM pada data anda.

Terdapat beberapa cara untuk melakukan carian dalam pangkalan data kami seperti:

- **Carian kata kunci** - digunakan untuk carian teks

- **Carian vektor** - menukar dokumen dari teks ke perwakilan vektor menggunakan model terbenam, membolehkan **carian semantik** menggunakan makna perkataan. Pencarian akan dilakukan dengan menyoal dokumen yang perwakilan vektornya paling hampir kepada soalan pengguna.

- **Hibrid** - gabungan kedua-dua carian kata kunci dan carian vektor.

Satu cabaran dengan pencarian timbul apabila tiada respons serupa kepada pertanyaan dalam pangkalan data, sistem akan mengembalikan maklumat terbaik yang boleh diperoleh, bagaimanapun, anda boleh menggunakan taktik seperti menetapkan jarak maksimum untuk kepentingan atau menggunakan carian hibrid yang menggabungkan kata kunci dan carian vektor. Dalam pelajaran ini kami akan menggunakan carian hibrid, gabungan kedua-dua carian vektor dan kata kunci. Kami akan menyimpan data kami ke dalam dataframe dengan lajur yang mengandungi ketulan serta terbenam.

### Kesamaan Vektor

Pengambil akan mencari melalui pangkalan pengetahuan untuk terbenam yang berdekatan—jiran terdekat—kerana mereka mewakili teks yang serupa. Dalam senario ini, apabila pengguna menghantar pertanyaan, ianya pertama ditanam dan kemudian dipadankan dengan terbenam yang serupa. Ukuran paling biasa digunakan untuk membandingkan kesamaan vektor adalah kesamaan kosinus, yang berdasarkan sudut antara dua vektor.

Ukuran lain yang boleh digunakan untuk mengukur kesamaan termasuk jarak Euclidean, iaitu garis lurus antara hujung vektor, dan hasil noktah, yang mengukur jumlah hasil darab unsur yang sepadan dalam dua vektor.

### Indeks carian

Apabila melakukan pencarian, kita perlu membina indeks carian untuk pangkalan pengetahuan kita sebelum melakukan pencarian. Indeks akan menyimpan terbenam kami dan boleh dengan cepat mengambil ketulan yang paling serupa walaupun dalam pangkalan data besar. Kita boleh membuat indeks secara tempatan menggunakan:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Pengurutan semula

Setelah anda menyoal pangkalan data, anda mungkin perlu menyusun keputusan dari yang paling relevan. LLM pengurutan semula menggunakan Pembelajaran Mesin untuk meningkatkan kaitan keputusan carian dengan mengatur mereka dari yang paling relevan. Menggunakan Azure AI Search, pengurutan semula dilakukan secara automatik untuk anda menggunakan penyusun semula semantik. Contoh bagaimana pengurutan semula berfungsi menggunakan jiran terdekat:

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

Langkah terakhir adalah menambah LLM kami ke dalam campuran untuk dapat mendapatkan respons yang berasaskan data kami. Kami boleh melaksanakannya seperti berikut:

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

## Menilai aplikasi kami

### Metod Evaluasi

- Kualiti respons yang diberikan memastikan ia kedengaran semula jadi, lancar dan seperti manusia

- Keasasan data: menilai sama ada respons datang dari dokumen yang diberikan

- Kepentingan: menilai sama ada respons sepadan dan berkaitan dengan soalan yang ditanya

- Kelancaran - sama ada respons membuat makna secara tatabahasa

## Kes Penggunaan untuk menggunakan RAG (Generasi Dipertingkatkan Pencarian) dan pangkalan data vektor

Terdapat banyak kes penggunaan berbeza di mana RAG boleh meningkatkan aplikasi anda, seperti:

- Soalan dan Jawapan: mendasari data syarikat anda kepada sembang yang boleh digunakan oleh pekerja untuk bertanya soalan.

- Sistem Cadangan: di mana anda boleh mencipta sistem yang memadankan nilai paling serupa contohnya filem, restoran dan banyak lagi.

- Perkhidmatan chatbot: anda boleh menyimpan sejarah sembang dan peribadikan perbualan berdasarkan data pengguna.

- Carian imej berdasarkan terbenam vektor, berguna apabila melakukan pengecaman imej dan pengesanan anomali.

## Ringkasan

Kami telah merangkumi kawasan asas RAG daripada menambah data kami ke aplikasi, pertanyaan pengguna dan output. Untuk memudahkan penciptaan RAG, anda boleh menggunakan rangka kerja seperti Semantic Kernel, LangChain atau AutoGen.

## Tugasan

Untuk meneruskan pembelajaran anda tentang Retrieval Augmented Generation (RAG) anda boleh membina:

- Membina front-end untuk aplikasi menggunakan rangka kerja pilihan anda

- Menggunakan rangka kerja, sama ada LangChain atau Semantic Kernel, dan mencipta semula aplikasi anda.

Tahniah kerana telah menamatkan pelajaran ini 👏.

## Pembelajaran tidak berhenti di sini, teruskan Perjalanan

Setelah menamatkan pelajaran ini, lihat koleksi [Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif anda!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->