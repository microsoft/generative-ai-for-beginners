# Membangun Aplikasi Chat Bertenaga AI Generatif

[![Membangun Aplikasi Chat Bertenaga AI Generatif](../../../translated_images/id/07-lesson-banner.a279b937f2843833.webp)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

Sekarang setelah kita melihat bagaimana kita dapat membangun aplikasi pembuatan teks, mari kita lihat aplikasi chat.

Aplikasi chat telah menjadi bagian dari kehidupan sehari-hari kita, menawarkan lebih dari sekadar sarana percakapan santai. Mereka merupakan bagian integral dari layanan pelanggan, dukungan teknis, dan bahkan sistem penasihat yang canggih. Kemungkinan besar Anda telah mendapatkan bantuan dari aplikasi chat tak lama yang lalu. Saat kita mengintegrasikan teknologi yang lebih canggih seperti AI generatif ke dalam platform ini, kompleksitasnya meningkat dan begitu juga tantangannya.

Beberapa pertanyaan yang perlu kita jawab adalah:

- **Membangun aplikasi**. Bagaimana kita membangun dan mengintegrasikan aplikasi bertenaga AI ini secara efisien untuk kasus penggunaan tertentu?
- **Pemantauan**. Setelah diterapkan, bagaimana kita dapat memantau dan memastikan bahwa aplikasi beroperasi pada tingkat kualitas tertinggi, baik dari segi fungsi dan kepatuhan terhadap [enam prinsip AI yang bertanggung jawab](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

Saat kita melangkah lebih jauh ke era yang didefinisikan oleh otomatisasi dan interaksi manusia-mesin yang mulus, memahami bagaimana AI generatif mengubah cakupan, kedalaman, dan kemampuan adaptasi aplikasi chat menjadi sangat penting. Pelajaran ini akan menyelidiki aspek arsitektur yang mendukung sistem rumit ini, mendalami metodologi untuk menyetel mereka untuk tugas khusus domain, dan mengevaluasi metrik dan pertimbangan yang relevan untuk memastikan penerapan AI yang bertanggung jawab.

## Pendahuluan

Pelajaran ini mencakup:

- Teknik untuk membangun dan mengintegrasikan aplikasi chat secara efisien.
- Cara menerapkan kustomisasi dan penyetelan untuk aplikasi.
- Strategi dan pertimbangan untuk memantau aplikasi chat secara efektif.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- Mendeskripsikan pertimbangan dalam membangun dan mengintegrasikan aplikasi chat ke dalam sistem yang ada.
- Mengkustomisasi aplikasi chat untuk kasus penggunaan tertentu.
- Mengidentifikasi metrik utama dan pertimbangan untuk memantau dan mempertahankan kualitas aplikasi chat bertenaga AI secara efektif.
- Memastikan aplikasi chat memanfaatkan AI secara bertanggung jawab.

## Mengintegrasikan AI Generatif ke dalam Aplikasi Chat

Meningkatkan aplikasi chat melalui AI generatif tidak hanya berpusat pada membuatnya lebih pintar; ini tentang mengoptimalkan arsitektur, kinerja, dan antarmuka pengguna untuk memberikan pengalaman pengguna yang berkualitas. Ini melibatkan penyelidikan dasar arsitektur, integrasi API, dan pertimbangan antarmuka pengguna. Bagian ini bertujuan memberikan Anda peta jalan komprehensif untuk menavigasi lanskap kompleks ini, baik Anda menghubungkannya ke sistem yang sudah ada atau membangunnya sebagai platform mandiri.

Pada akhir bagian ini, Anda akan memiliki keahlian yang diperlukan untuk membangun dan menggabungkan aplikasi chat secara efisien.

### Chatbot atau Aplikasi Chat?

Sebelum kita menyelam dalam membangun aplikasi chat, mari kita bandingkan 'chatbot' dengan 'aplikasi chat bertenaga AI,' yang memiliki peran dan fungsi berbeda. Tujuan utama chatbot adalah mengotomatiskan tugas percakapan tertentu, seperti menjawab pertanyaan yang sering diajukan atau melacak paket. Biasanya diatur oleh logika berbasis aturan atau algoritma AI yang kompleks. Sebaliknya, aplikasi chat bertenaga AI adalah lingkungan yang jauh lebih luas yang dirancang untuk memfasilitasi berbagai bentuk komunikasi digital, seperti chat teks, suara, dan video antar pengguna manusia. Fitur utamanya adalah integrasi model AI generatif yang mensimulasikan percakapan yang bernuansa dan mirip manusia, menghasilkan respons berdasarkan berbagai input dan petunjuk kontekstual. Aplikasi chat bertenaga AI generatif dapat terlibat dalam diskusi domain terbuka, beradaptasi dengan konteks percakapan yang berkembang, dan bahkan menghasilkan dialog kreatif atau kompleks.

Tabel di bawah ini menguraikan perbedaan dan persamaan utama untuk membantu kita memahami peran unik mereka dalam komunikasi digital.

| Chatbot                               | Aplikasi Chat Bertenaga AI Generatif           |
| ------------------------------------- | ---------------------------------------------- |
| Fokus pada tugas dan berbasis aturan | Sadar konteks                                  |
| Sering terintegrasi ke sistem yang lebih besar | Dapat menampung satu atau beberapa chatbot  |
| Terbatas pada fungsi yang diprogram   | Menggabungkan model AI generatif               |
| Interaksi yang terspesialisasi & terstruktur | Mampu diskusi domain terbuka                  |

### Memanfaatkan fungsi bawaan dengan SDK dan API

Saat membangun aplikasi chat, langkah pertama yang bagus adalah menilai apa yang sudah ada. Menggunakan SDK dan API untuk membangun aplikasi chat adalah strategi yang menguntungkan karena berbagai alasan. Dengan mengintegrasikan SDK dan API yang terdokumentasi dengan baik, Anda secara strategis memposisikan aplikasi Anda untuk kesuksesan jangka panjang, mengatasi masalah skalabilitas dan pemeliharaan.

- **Mempercepat proses pengembangan dan mengurangi beban**: Mengandalkan fungsi bawaan daripada proses mahal membangunnya sendiri memungkinkan Anda fokus pada aspek lain dari aplikasi yang mungkin lebih penting, seperti logika bisnis.
- **Kinerja yang lebih baik**: Saat membangun fungsi dari awal, Anda akan bertanya pada diri sendiri "Bagaimana ini skala? Apakah aplikasi ini mampu menangani lonjakan pengguna tiba-tiba?" SDK dan API yang dikelola dengan baik sering memiliki solusi bawaan untuk masalah ini.
- **Pemeliharaan lebih mudah**: Pembaruan dan perbaikan lebih mudah dikelola karena sebagian besar API dan SDK hanya membutuhkan pembaruan pustaka saat versi baru dirilis.
- **Akses ke teknologi mutakhir**: Memanfaatkan model yang telah disetel dan dilatih pada dataset yang luas memberikan aplikasi Anda kemampuan bahasa alami.

Mengakses fungsi SDK atau API biasanya melibatkan memperoleh izin untuk menggunakan layanan yang disediakan, yang seringkali melalui penggunaan kunci unik atau token autentikasi. Kita akan menggunakan Perpustakaan Python OpenAI untuk mengeksplorasi seperti apa bentuknya. Anda juga dapat mencobanya sendiri dalam [notebook untuk OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) atau [notebook untuk Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) untuk pelajaran ini.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

response = client.responses.create(model="gpt-4o-mini", input="Suggest two titles for an instructional lesson on chat applications for generative AI.", store=False)
print(response.output_text)
```

Contoh di atas menggunakan model GPT-4o mini dengan API Respons untuk menyelesaikan prompt, tetapi perhatikan bahwa kunci API disetel terlebih dahulu. Anda akan menerima kesalahan jika tidak menyetel kunci tersebut.

## Pengalaman Pengguna (UX)

Prinsip UX umum berlaku untuk aplikasi chat, tetapi berikut adalah beberapa pertimbangan tambahan yang menjadi sangat penting karena komponen pembelajaran mesin yang terlibat.

- **Mekanisme untuk mengatasi ambiguitas**: Model AI generatif terkadang menghasilkan jawaban yang ambigu. Fitur yang memungkinkan pengguna meminta klarifikasi dapat membantu jika mereka menghadapi masalah ini.
- **Mempertahankan konteks**: Model AI generatif yang canggih memiliki kemampuan untuk mengingat konteks dalam percakapan, yang bisa menjadi aset penting bagi pengalaman pengguna. Memberikan pengguna kemampuan untuk mengontrol dan mengelola konteks meningkatkan pengalaman pengguna, tetapi memperkenalkan risiko mempertahankan informasi sensitif pengguna. Pertimbangan tentang berapa lama informasi ini disimpan, seperti memperkenalkan kebijakan retensi, dapat menyeimbangkan kebutuhan konteks dengan privasi.
- **Personalisasi**: Dengan kemampuan untuk belajar dan beradaptasi, model AI menawarkan pengalaman yang dipersonalisasi untuk pengguna. Menyesuaikan pengalaman pengguna melalui fitur seperti profil pengguna tidak hanya membuat pengguna merasa dipahami, tetapi juga membantu pencarian mereka menemukan jawaban spesifik, menciptakan interaksi yang lebih efisien dan memuaskan.

Salah satu contoh personalisasi adalah pengaturan "Instruksi Khusus" di ChatGPT OpenAI. Ia memungkinkan Anda memberikan informasi tentang diri Anda yang mungkin menjadi konteks penting untuk prompt Anda. Berikut contoh instruksi khusus.

![Pengaturan Instruksi Khusus di ChatGPT](../../../translated_images/id/custom-instructions.b96f59aa69356fcf.webp)

"Profil" ini meminta ChatGPT membuat rencana pelajaran tentang linked lists. Perhatikan bahwa ChatGPT mempertimbangkan bahwa pengguna mungkin menginginkan rencana pelajaran yang lebih mendalam berdasarkan pengalamannya.

![Prompt di ChatGPT untuk rencana pelajaran tentang linked lists](../../../translated_images/id/lesson-plan-prompt.cc47c488cf1343df.webp)

### Kerangka Pesan Sistem Microsoft untuk Model Bahasa Besar

[Microsoft telah menyediakan panduan](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) untuk menulis pesan sistem yang efektif saat menghasilkan respons dari LLM yang dibagi menjadi 4 area:

1. Mendefinisikan siapa model ditujukan, serta kemampuannya dan keterbatasannya.
2. Mendefinisikan format keluaran model.
3. Memberikan contoh spesifik yang menunjukkan perilaku yang diinginkan dari model.
4. Memberikan batasan perilaku tambahan.

### Aksesibilitas

Baik pengguna memiliki gangguan penglihatan, pendengaran, motorik, atau kognitif, aplikasi chat yang dirancang dengan baik harus dapat digunakan oleh semua orang. Daftar berikut merinci fitur spesifik yang bertujuan meningkatkan aksesibilitas untuk berbagai gangguan pengguna.

- **Fitur untuk Gangguan Visual**: Tema kontras tinggi dan teks yang dapat diubah ukurannya, kompatibilitas pembaca layar.
- **Fitur untuk Gangguan Pendengaran**: Fungsi teks-ke-suara dan suara-ke-teks, petunjuk visual untuk notifikasi audio.
- **Fitur untuk Gangguan Motorik**: Dukungan navigasi keyboard, perintah suara.
- **Fitur untuk Gangguan Kognitif**: Opsi bahasa yang disederhanakan.

## Kustomisasi dan Penyempurnaan Model Bahasa Domain-Spesifik

Bayangkan sebuah aplikasi chat yang memahami jargon perusahaan Anda dan mengantisipasi pertanyaan spesifik yang umum dari basis penggunanya. Ada beberapa pendekatan yang patut disebutkan:

- **Memanfaatkan model DSL**. DSL berarti domain specific language. Anda dapat memanfaatkan model DSL yang dilatih pada domain tertentu untuk memahami konsep dan skenarionya.
- **Menerapkan fine-tuning**. Fine-tuning adalah proses pelatihan lebih lanjut model Anda dengan data spesifik.

## Kustomisasi: Menggunakan DSL

Memanfaatkan model bahasa domain-spesifik (model DSL) dapat meningkatkan keterlibatan pengguna dengan menyediakan interaksi khusus dan relevan secara kontekstual. Ini adalah model yang dilatih atau disetel untuk memahami dan menghasilkan teks terkait bidang, industri, atau subjek tertentu. Opsi menggunakan model DSL dapat bervariasi dari melatih satu dari awal, hingga menggunakan yang sudah ada melalui SDK dan API. Opsi lain adalah fine-tuning, yang melibatkan mengambil model yang sudah dilatih sebelumnya dan menyesuaikannya untuk domain tertentu.

## Kustomisasi: Menerapkan fine-tuning

Fine-tuning sering dipertimbangkan ketika model pra-latih tidak cukup dalam domain khusus atau tugas tertentu.

Misalnya, pertanyaan medis itu kompleks dan membutuhkan banyak konteks. Ketika seorang profesional medis mendiagnosis pasien, itu didasarkan pada berbagai faktor seperti gaya hidup atau kondisi yang sudah ada sebelumnya, dan bahkan mungkin mengandalkan jurnal medis terbaru untuk memvalidasi diagnosa mereka. Dalam skenario yang bernuansa seperti itu, aplikasi chat AI tujuan umum tidak bisa menjadi sumber yang dapat dipercaya.

### Skenario: aplikasi medis

Pertimbangkan aplikasi chat yang dirancang untuk membantu praktisi medis dengan menyediakan referensi cepat ke pedoman pengobatan, interaksi obat, atau temuan penelitian terbaru.

Model tujuan umum mungkin memadai untuk menjawab pertanyaan medis dasar atau memberikan saran umum, tetapi mungkin kesulitan dengan hal-hal berikut:

- **Kasus yang sangat spesifik atau kompleks**. Misalnya, seorang ahli saraf mungkin bertanya kepada aplikasi, "Apa praktik terbaik saat ini untuk mengelola epilepsi yang resisten obat pada pasien pediatrik?"
- **Kekurangan kemajuan terbaru**. Model tujuan umum mungkin kesulitan memberikan jawaban terkini yang memasukkan kemajuan terbaru dalam neurologi dan farmakologi.

Dalam kasus seperti ini, menyetel model dengan dataset medis khusus dapat secara signifikan meningkatkan kemampuannya untuk menangani pertanyaan medis yang rumit ini secara lebih akurat dan dapat diandalkan. Ini memerlukan akses ke dataset yang besar dan relevan yang mewakili tantangan dan pertanyaan domain-spesifik yang perlu diatasi.

## Pertimbangan untuk Pengalaman Chat Bertenaga AI Berkualitas Tinggi

Bagian ini menguraikan kriteria untuk aplikasi chat "berkualitas tinggi," yang mencakup pengumpulan metrik yang dapat ditindaklanjuti dan kepatuhan pada kerangka kerja yang memanfaatkan teknologi AI secara bertanggung jawab.

### Metrik Kunci

Untuk mempertahankan kinerja aplikasi yang berkualitas tinggi, penting untuk melacak metrik dan pertimbangan kunci. Pengukuran ini tidak hanya memastikan fungsi aplikasi tetapi juga menilai kualitas model AI dan pengalaman pengguna. Berikut daftar yang mencakup metrik dasar, AI, dan pengalaman pengguna yang harus dipertimbangkan.

| Metrik                        | Definisi                                                                                                             | Pertimbangan untuk Pengembang Chat                                         |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Waktu Aktif (Uptime)**      | Mengukur lamanya aplikasi beroperasi dan dapat diakses oleh pengguna.                                                  | Bagaimana Anda meminimalkan waktu tidak aktif?                            |
| **Waktu Respons**             | Waktu yang dibutuhkan aplikasi untuk menjawab pertanyaan pengguna.                                                    | Bagaimana Anda mengoptimalkan pemrosesan kueri untuk memperbaiki waktu respons? |
| **Presisi**                   | Rasio prediksi positif benar terhadap total jumlah prediksi positif.                                                  | Bagaimana Anda memvalidasi presisi model Anda?                            |
| **Recall (Sensitivitas)**     | Rasio prediksi positif benar terhadap jumlah positif sebenarnya.                                                      | Bagaimana Anda mengukur dan meningkatkan recall?                         |
| **Skor F1**                  | Mean harmonik dari presisi dan recall, yang menyeimbangkan trade-off antara keduanya.                                  | Apa target Skor F1 Anda? Bagaimana Anda menyeimbangkan presisi dan recall?|
| **Perplexity**                | Mengukur seberapa baik distribusi probabilitas yang diprediksi model sesuai dengan distribusi data sebenarnya.         | Bagaimana Anda meminimalkan perplexity?                                  |
| **Metrik Kepuasan Pengguna** | Mengukur persepsi pengguna terhadap aplikasi. Sering dikumpulkan melalui survei.                                       | Seberapa sering Anda mengumpulkan umpan balik pengguna? Bagaimana Anda beradaptasi berdasarkan itu? |
| **Tingkat Kesalahan**         | Tingkat kesalahan model dalam memahami atau menghasilkan output.                                                       | Strategi apa yang Anda miliki untuk mengurangi tingkat kesalahan?        |
| **Siklus Pelatihan Ulang**   | Frekuensi model diperbarui untuk memasukkan data dan wawasan baru.                                                    | Seberapa sering Anda akan melatih ulang model? Apa yang memicu siklus pelatihan ulang? |

| **Deteksi Anomali**         | Alat dan teknik untuk mengidentifikasi pola tidak biasa yang tidak sesuai dengan perilaku yang diharapkan.                        | Bagaimana Anda akan merespons anomali?                                        |

### Menerapkan Praktik AI Bertanggung Jawab dalam Aplikasi Chat

Pendekatan Microsoft terhadap AI Bertanggung Jawab telah mengidentifikasi enam prinsip yang harus menjadi panduan dalam pengembangan dan penggunaan AI. Berikut adalah prinsip-prinsip tersebut, definisinya, dan hal-hal yang harus dipertimbangkan oleh pengembang chat serta mengapa mereka harus menganggapnya serius.

| Prinsip                | Definisi Microsoft                                    | Pertimbangan untuk Pengembang Chat                                      | Mengapa Ini Penting                                                                     |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Keadilan               | Sistem AI harus memperlakukan semua orang secara adil. | Pastikan aplikasi chat tidak mendiskriminasi berdasarkan data pengguna.  | Untuk membangun kepercayaan dan inklusivitas di antara pengguna; menghindari konsekuensi hukum.                |
| Keandalan dan Keamanan | Sistem AI harus bekerja secara andal dan aman.         | Terapkan pengujian dan mekanisme pengaman untuk meminimalkan kesalahan dan risiko.         | Menjamin kepuasan pengguna dan mencegah potensi kerugian.                                 |
| Privasi dan Keamanan   | Sistem AI harus aman dan menghormati privasi.           | Terapkan enkripsi kuat dan langkah perlindungan data.              | Untuk melindungi data sensitif pengguna dan mematuhi undang-undang privasi.                         |
| Inklusivitas           | Sistem AI harus memberdayakan semua orang dan melibatkan mereka. | Rancang UI/UX yang dapat diakses dan mudah digunakan oleh audiens yang beragam. | Memastikan lebih banyak orang dapat menggunakan aplikasi secara efektif.                   |
| Transparansi           | Sistem AI harus dapat dipahami.                         | Sediakan dokumentasi yang jelas dan alasan untuk respons AI.            | Pengguna lebih cenderung mempercayai sistem jika mereka dapat memahami bagaimana keputusan dibuat. |
| Akuntabilitas          | Orang harus bertanggung jawab atas sistem AI.           | Tetapkan proses yang jelas untuk audit dan perbaikan keputusan AI.     | Memungkinkan perbaikan berkelanjutan dan tindakan korektif jika terjadi kesalahan.               |

## Tugas

Lihat [assignment](../../../07-building-chat-applications/python). Ini akan membawa Anda melalui serangkaian latihan mulai dari menjalankan prompt chat pertama Anda, mengklasifikasikan dan meringkas teks, dan lain-lain. Perhatikan bahwa tugas tersedia dalam berbagai bahasa pemrograman!

## Kerja Hebat! Lanjutkan Perjalanan

Setelah menyelesaikan pelajaran ini, lihat koleksi [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan Generative AI Anda!

Pergi ke Pelajaran 8 untuk melihat bagaimana Anda dapat mulai [membangun aplikasi pencarian](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->