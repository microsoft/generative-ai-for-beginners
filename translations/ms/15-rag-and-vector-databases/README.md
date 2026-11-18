# Generasi Ditambah Pemulihan (RAG) dan Pangkalan Data Vektor

[![Generasi Ditambah Pemulihan (RAG) dan Pangkalan Data Vektor](../../../translated_images/ms/15-lesson-banner.ac49e59506175d4f.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Dalam pelajaran aplikasi carian, kita telah belajar secara ringkas bagaimana untuk mengintegrasikan data anda sendiri ke dalam Model Bahasa Besar (LLM). Dalam pelajaran ini, kita akan mendalami lagi konsep membumikan data anda dalam aplikasi LLM anda, mekanik prosesnya dan kaedah penyimpanan data, termasuk kedua-dua embedding dan teks.

> **Video Akan Datang**

## Pengenalan

Dalam pelajaran ini kita akan merangkumi perkara berikut:

- Pengenalan kepada RAG, apa itu dan mengapa ia digunakan dalam AI (kecerdasan buatan).

- Memahami apa itu pangkalan data vektor dan mencipta satu untuk aplikasi kita.

- Contoh praktikal tentang cara mengintegrasikan RAG ke dalam aplikasi.

## Matlamat Pembelajaran

Selepas menyelesaikan pelajaran ini, anda akan dapat:

- Jelaskan kepentingan RAG dalam pemulihan dan pemprosesan data.

- Menyediakan aplikasi RAG dan membumikan LLM dengan data anda

- Mengintegrasikan RAG dan pangkalan data vektor dengan berkesan dalam aplikasi LLM.

## Senario Kami: mempertingkatkan LLM kami dengan data kami sendiri

Untuk pelajaran ini, kami ingin menambah nota kami sendiri ke dalam startup pendidikan, yang membolehkan chatbot mendapatkan lebih banyak maklumat mengenai subjek yang berbeza. Dengan menggunakan nota yang kami ada, pelajar akan dapat belajar dengan lebih baik dan memahami topik berbeza, menjadikannya lebih mudah untuk ulang kaji bagi peperiksaan mereka. Untuk mencipta senario kami, kami akan menggunakan:

- `Azure OpenAI:` LLM yang akan kami gunakan untuk mencipta chatbot kami

- `AI for beginners' lesson on Neural Networks`: ini akan menjadi data yang kami bumikan LLM kami ke atasnya

- `Azure AI Search` dan `Azure Cosmos DB:` pangkalan data vektor untuk menyimpan data kami dan mencipta indeks carian

Pengguna akan dapat mencipta kuiz latihan dan kad ulang kaji dari nota mereka serta meringkaskan nota tersebut menjadi ringkasan padat. Untuk memulakan, mari kita lihat apa itu RAG dan bagaimana ia berfungsi:

## Generasi Ditambah Pemulihan (RAG)

Chatbot yang dikuasakan oleh LLM memproses arahan pengguna untuk menghasilkan maklum balas. Ia direka untuk menjadi interaktif dan berinteraksi dengan pengguna dalam pelbagai topik. Walau bagaimanapun, maklum balasnya terhad kepada konteks yang diberikan dan data latihan asasnya. Sebagai contoh, had pengetahuan GPT-4 ialah September 2021, bermakna, ia tidak mempunyai pengetahuan tentang peristiwa yang berlaku selepas tempoh ini. Selain itu, data yang digunakan untuk melatih LLM tidak termasuk maklumat sulit seperti nota peribadi atau manual produk syarikat.

### Bagaimana RAG (Generasi Ditambah Pemulihan) berfungsi

![lukisan yang menunjukkan bagaimana RAG berfungsi](../../../translated_images/ms/how-rag-works.f5d0ff63942bd3a6.webp?WT.mc_id=academic-105485-koreyst)

Andaian anda ingin melancarkan chatbot yang mencipta kuiz dari nota anda, anda memerlukan sambungan ke pangkalan pengetahuan. Di sinilah RAG membantu. RAG beroperasi seperti berikut:

- **Pangkalan pengetahuan:** Sebelum pemulihan, dokumen ini perlu dimasukkan dan dipra-proses, biasanya memecahkan dokumen besar kepada bahagian lebih kecil, menukarnya kepada embedding teks dan menyimpannya dalam pangkalan data.

- **Pertanyaan Pengguna:** pengguna mengemukakan soalan

- **Pemulihan:** Apabila seorang pengguna mengemukakan soalan, model embedding mengambil maklumat relevan dari pangkalan pengetahuan kami untuk menyediakan konteks tambahan yang akan dimasukkan ke dalam prompt.

- **Generasi Ditambah:** LLM meningkatkan maklum balasnya berdasarkan data yang dipulihkan. Ini membolehkan maklum balas yang dihasilkan bukan sahaja berdasarkan data latihan pra-sedia tetapi juga maklumat relevan dari konteks tambahan. Data yang dipulihkan digunakan untuk menambah baik maklum balas LLM. Kemudian LLM memberi jawapan kepada soalan pengguna.

![Diagram yang menunjukkan seni bina RAG](../../../translated_images/ms/encoder-decode.f2658c25d0eadee2.webp?WT.mc_id=academic-105485-koreyst)

RAG menggabungkan pengambil dengan penjana: pertanyaan ditukar menjadi vektor, dipadankan dengan indeks dokumen untuk mencari potongan teks yang relevan, dan potongan tersebut dibekalkan sebagai konteks kepada LLM, yang menghasilkannya sebagai maklum balas. Pengambil dan penjana mungkin menggunakan model yang berbeza; RAG tidak memerlukan transformer penyandi-penyahkod.

Dua pendekatan apabila melaksanakan RAG menurut kertas cadangan yang dicadangkan: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) adalah:

- **_RAG-Sequence_** menggunakan dokumen yang dipulihkan untuk meramalkan jawapan terbaik kepada pertanyaan pengguna

- **RAG-Token** menggunakan dokumen untuk menjana token seterusnya, kemudian memulihkannya untuk menjawab pertanyaan pengguna

### Mengapa anda menggunakan RAG? 

- **Kekayaan maklumat:** memastikan maklum balas teks adalah terkini dan semasa. Oleh itu, ia meningkatkan prestasi dalam tugasan khusus bidang dengan mengakses pangkalan pengetahuan dalaman.

- Mengurangkan rekaan dengan menggunakan **data yang boleh disahkan** dalam pangkalan pengetahuan untuk menyediakan konteks kepada pertanyaan pengguna.

- Ia **berkesan dari segi kos** kerana ia lebih ekonomik berbanding menyesuaikan LLM secara khusus

## Mencipta pangkalan pengetahuan

Aplikasi kami berasaskan data peribadi kami, iaitu pelajaran Rangkaian Neural daripada kurikulum AI untuk Pemula.

### Pangkalan Data Vektor

Pangkalan data vektor, berbeza dengan pangkalan data tradisional, adalah pangkalan data khusus yang direka untuk menyimpan, mengurus dan mencari vektor tersemat. Ia menyimpan perwakilan bernombor dokumen. Memecahkan data kepada embedding bernombor memudahkan sistem AI kami memahami dan memproses data tersebut.

Kerana LLM mempunyai had jumlah token input, kami memecah dokumen kepada bahagian sebelum embedding. Apabila pengguna mengemukakan soalan, embedding yang paling serupa dengan pertanyaan mengenal pasti potongan teks yang relevan, yang dikembalikan bersama prompt. Pemecahan ini juga mengurangkan bilangan token yang dihantar ke LLM dan oleh itu boleh mengurangkan kos.

Beberapa pangkalan data vektor popular termasuk Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant dan DeepLake. Anda boleh mencipta model Azure Cosmos DB menggunakan Azure CLI dengan arahan berikut:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Dari teks ke embedding

Sebelum kami menyimpan data kami, kami perlu menukarnya kepada embedding vektor sebelum disimpan dalam pangkalan data. Jika anda bekerja dengan dokumen besar atau teks panjang, anda boleh memecahkannya berdasarkan pertanyaan yang anda jangkakan. Pemecahan boleh dilakukan pada tahap ayat, atau perenggan. Kerana pemecahan mengambil makna dari kata-kata di sekitarnya, anda boleh menambah konteks lain kepada bahagian, contohnya, dengan menambah tajuk dokumen atau memasukkan beberapa teks sebelum atau selepas bahagian tersebut. Anda boleh memecah data seperti berikut:

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

Setelah dipecah, kita kemudian boleh membuat embedding teks kita menggunakan model embedding yang berbeza. Beberapa model yang anda boleh gunakan termasuk: word2vec, ada-002 oleh OpenAI, Azure Computer Vision dan banyak lagi. Pemilihan model yang digunakan bergantung pada bahasa yang anda gunakan, jenis kandungan yang dikodkan (teks/gambar/audio), saiz input yang boleh dikod dan panjang output embedding.

Contoh embedding teks menggunakan model `text-embedding-ada-002` OpenAI ialah:
![embedding perkataan cat](../../../translated_images/ms/cat.74cbd7946bc9ca38.webp?WT.mc_id=academic-105485-koreyst)

## Pemulihan dan Carian Vektor

Apabila pengguna mengemukakan soalan, pengambil menukarnya kepada vektor menggunakan penyandi pertanyaan, kemudian mencari dalam indeks carian dokumen kami untuk vektor yang relevan dalam dokumen yang berkaitan dengan input. Setelah selesai, ia menukar kedua-dua vektor input dan vektor dokumen kepada teks dan menghantarnya melalui LLM.

### Pemulihan

Pemulihan berlaku apabila sistem cuba mencari dokumen dari indeks yang memenuhi kriteria carian dengan cepat. Matlamat pengambil adalah untuk mendapatkan dokumen yang akan digunakan untuk menyediakan konteks dan membumikan LLM pada data anda.

Terdapat beberapa cara untuk melakukan carian dalam pangkalan data kami seperti:

- **Carian kata kunci** - digunakan untuk carian teks

- **Carian vektor** - menukar dokumen dari teks kepada perwakilan vektor menggunakan model embedding, membolehkan **carian semantik** menggunakan makna kata. Pemulihan dilakukan dengan membuat pertanyaan ke dokumen yang perwakilan vektornya paling hampir dengan soalan pengguna.

- **Hibrid** - gabungan carian kata kunci dan carian vektor.

Cabaran dengan pemulihan muncul apabila tiada maklum balas serupa dalam pangkalan data, sistem akan mengembalikan maklumat terbaik yang boleh diperoleh, namun, anda boleh menggunakan taktik seperti menetapkan jarak maksimum untuk relevan atau menggunakan carian hibrid yang menggabungkan kedua-dua carian kata kunci dan vektor. Dalam pelajaran ini kita akan menggunakan carian hibrid, gabungan carian vektor dan kata kunci. Kita akan menyimpan data kita ke dalam dataframe dengan lajur yang mengandungi potongan serta embedding.

### Kesamaan Vektor

Pengambil akan mencari melalui pangkalan pengetahuan untuk embedding yang hampir antara satu sama lain—jiran terdekat—kerana mereka mewakili teks yang serupa. Dalam senario ini, apabila pengguna menghantar pertanyaan, ia pertama kali di-embed dan kemudian dipadankan dengan embedding yang serupa. Pengukuran paling biasa digunakan untuk membandingkan kesamaan vektor ialah kesamaan kosinus, yang berdasarkan sudut antara dua vektor.

Metrik lain yang boleh digunakan untuk mengukur kesamaan termasuk jarak Euclidean, iaitu garis lurus antara titik akhir vektor, dan hasil titik (dot product), yang mengukur jumlah hasil darab elemen-elemen padanan dalam dua vektor.

### Indeks carian

Apabila melakukan pemulihan, kita perlu membina indeks carian untuk pangkalan pengetahuan kita sebelum kita melakukan carian. Indeks akan menyimpan embedding kita dan boleh cepat mengambil potongan yang paling serupa walaupun dalam pangkalan data yang besar. Kita boleh mencipta indeks kita secara tempatan menggunakan:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Penyusunan semula

Setelah anda membuat pertanyaan ke pangkalan data, anda mungkin perlu menyusun hasil dari yang paling relevan. LLM penyusun semula menggunakan Pembelajaran Mesin untuk meningkatkan relevan hasil carian dengan mengaturnya dari yang paling relevan. Dengan menggunakan Azure AI Search, penyusunan semula dilakukan secara automatik untuk anda menggunakan penurunan semantik (semantic reranker). Contoh bagaimana penyusunan semula berfungsi dengan jiran terdekat:

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

Langkah terakhir adalah menambah LLM kita ke dalam campuran untuk dapat memperoleh maklum balas yang dibumikan pada data kita. Kita boleh melaksanakannya seperti berikut:

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

### Metrik Penilaian

- Kualiti maklum balas yang diberikan memastikan ia kedengaran semula jadi, lancar dan seperti manusia

- Ketegasan data: menilai sama ada maklum balas yang datang dari dokumen yang disediakan

- Relevan: menilai sama ada maklum balas sepadan dan berkaitan dengan soalan yang ditanya

- Kelancaran - sama ada maklum balas masuk akal dari segi tatabahasa

## Kes penggunaan untuk menggunakan RAG (Generasi Ditambah Pemulihan) dan pangkalan data vektor

Terdapat banyak kes penggunaan yang berbeza di mana RAG boleh meningkatkan aplikasi anda, seperti:

- Soal Jawab: membumikan data syarikat anda ke dalam perbualan yang boleh digunakan oleh pekerja untuk mengemukakan soalan.

- Sistem Cadangan: di mana anda boleh mencipta sistem yang memadankan nilai paling serupa contohnya filem, restoran dan banyak lagi.

- Perkhidmatan chatbot: anda boleh menyimpan sejarah perbualan dan memperibadikan perbualan berdasarkan data pengguna.

- Carian imej berdasarkan embedding vektor, berguna apabila melakukan pengecaman imej dan pengesanan anomali.

## Rumusan

Kami telah merangkumi bidang asas RAG dari menambah data kami ke aplikasi, pertanyaan pengguna dan output. Untuk mempermudah penciptaan RAG, anda boleh menggunakan rangka kerja seperti Semantic Kernel, LangChain atau AutoGen.

## Tugasan

Untuk meneruskan pembelajaran Generasi Ditambah Pemulihan (RAG) anda, anda boleh membina:

- Membangunkan front-end untuk aplikasi menggunakan rangka kerja pilihan anda

- Menggunakan rangka kerja, sama ada LangChain atau Semantic Kernel, dan mengulang cipta aplikasi anda.

Tahniah kerana menamatkan pelajaran 👏.

## Pembelajaran tidak berhenti di sini, teruskan Perjalanan

Selepas menamatkan pelajaran ini, lihat [koleksi Pembelajaran AI Generatif kami](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk terus meningkatkan pengetahuan AI Generatif anda!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->