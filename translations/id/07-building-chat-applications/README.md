<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5308963a56cfbad2d73b0fa99fe84b3",
  "translation_date": "2025-10-17T20:47:26+00:00",
  "source_file": "07-building-chat-applications/README.md",
  "language_code": "id"
}
-->
# Membangun Aplikasi Chat Berbasis AI Generatif

[![Membangun Aplikasi Chat Berbasis AI Generatif](../../../translated_images/07-lesson-banner.a279b937f2843833fe28b4597f51bdef92d0ad03efee7ba52d0f166dea7574e5.id.png)](https://youtu.be/R9V0ZY1BEQo?si=IHuU-fS9YWT8s4sA)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

Setelah kita melihat bagaimana membangun aplikasi generasi teks, mari kita bahas aplikasi chat.

Aplikasi chat telah menjadi bagian dari kehidupan sehari-hari kita, menawarkan lebih dari sekadar sarana percakapan santai. Mereka adalah bagian penting dari layanan pelanggan, dukungan teknis, dan bahkan sistem penasihat yang canggih. Kemungkinan besar Anda pernah mendapatkan bantuan dari aplikasi chat belum lama ini. Ketika kita mengintegrasikan teknologi yang lebih maju seperti AI generatif ke dalam platform ini, kompleksitasnya meningkat, begitu pula tantangannya.

Beberapa pertanyaan yang perlu dijawab adalah:

- **Membangun aplikasi**. Bagaimana kita dapat membangun dan mengintegrasikan aplikasi berbasis AI ini secara efisien untuk kasus penggunaan tertentu?
- **Pemantauan**. Setelah diterapkan, bagaimana kita dapat memantau dan memastikan bahwa aplikasi beroperasi pada tingkat kualitas tertinggi, baik dari segi fungsi maupun kepatuhan terhadap [enam prinsip AI yang bertanggung jawab](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

Saat kita semakin memasuki era yang ditentukan oleh otomatisasi dan interaksi manusia-mesin yang mulus, memahami bagaimana AI generatif mengubah cakupan, kedalaman, dan adaptabilitas aplikasi chat menjadi sangat penting. Pelajaran ini akan menyelidiki aspek arsitektur yang mendukung sistem yang rumit ini, membahas metodologi untuk menyempurnakan tugas-tugas spesifik domain, dan mengevaluasi metrik serta pertimbangan yang relevan untuk memastikan penerapan AI yang bertanggung jawab.

## Pendahuluan

Pelajaran ini mencakup:

- Teknik untuk membangun dan mengintegrasikan aplikasi chat secara efisien.
- Cara menerapkan kustomisasi dan penyempurnaan pada aplikasi.
- Strategi dan pertimbangan untuk memantau aplikasi chat secara efektif.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- Menjelaskan pertimbangan untuk membangun dan mengintegrasikan aplikasi chat ke dalam sistem yang ada.
- Menyesuaikan aplikasi chat untuk kasus penggunaan tertentu.
- Mengidentifikasi metrik utama dan pertimbangan untuk memantau dan menjaga kualitas aplikasi chat berbasis AI secara efektif.
- Memastikan aplikasi chat memanfaatkan AI secara bertanggung jawab.

## Mengintegrasikan AI Generatif ke dalam Aplikasi Chat

Meningkatkan aplikasi chat melalui AI generatif tidak hanya berfokus pada membuatnya lebih pintar; ini tentang mengoptimalkan arsitektur, kinerja, dan antarmuka pengguna untuk memberikan pengalaman pengguna yang berkualitas. Ini melibatkan penyelidikan fondasi arsitektur, integrasi API, dan pertimbangan antarmuka pengguna. Bagian ini bertujuan untuk memberikan Anda peta jalan yang komprehensif untuk menavigasi lanskap yang kompleks ini, baik Anda mengintegrasikannya ke dalam sistem yang ada atau membangunnya sebagai platform mandiri.

Pada akhir bagian ini, Anda akan memiliki keahlian yang diperlukan untuk membangun dan mengintegrasikan aplikasi chat secara efisien.

### Chatbot atau Aplikasi Chat?

Sebelum kita membahas cara membangun aplikasi chat, mari kita bandingkan 'chatbot' dengan 'aplikasi chat berbasis AI,' yang memiliki peran dan fungsi yang berbeda. Tujuan utama chatbot adalah mengotomatisasi tugas percakapan tertentu, seperti menjawab pertanyaan yang sering diajukan atau melacak paket. Biasanya, chatbot diatur oleh logika berbasis aturan atau algoritma AI yang kompleks. Sebaliknya, aplikasi chat berbasis AI adalah lingkungan yang jauh lebih luas yang dirancang untuk memfasilitasi berbagai bentuk komunikasi digital, seperti teks, suara, dan video di antara pengguna manusia. Fitur yang membedakannya adalah integrasi model AI generatif yang mensimulasikan percakapan yang bernuansa dan mirip manusia, menghasilkan respons berdasarkan berbagai input dan petunjuk kontekstual. Aplikasi chat berbasis AI generatif dapat terlibat dalam diskusi domain terbuka, beradaptasi dengan konteks percakapan yang berkembang, dan bahkan menghasilkan dialog yang kreatif atau kompleks.

Tabel di bawah ini merangkum perbedaan dan kesamaan utama untuk membantu kita memahami peran unik mereka dalam komunikasi digital.

| Chatbot                               | Aplikasi Chat Berbasis AI Generatif    |
| ------------------------------------- | -------------------------------------- |
| Berfokus pada tugas dan berbasis aturan | Sadar konteks                          |
| Sering diintegrasikan ke dalam sistem yang lebih besar | Dapat menjadi host satu atau beberapa chatbot |
| Terbatas pada fungsi yang diprogram   | Mengintegrasikan model AI generatif    |
| Interaksi yang terstruktur & spesifik | Mampu berdiskusi domain terbuka        |

### Memanfaatkan Fitur yang Sudah Ada dengan SDK dan API

Saat membangun aplikasi chat, langkah awal yang baik adalah menilai apa yang sudah tersedia. Menggunakan SDK dan API untuk membangun aplikasi chat adalah strategi yang menguntungkan karena berbagai alasan. Dengan mengintegrasikan SDK dan API yang terdokumentasi dengan baik, Anda secara strategis memposisikan aplikasi Anda untuk kesuksesan jangka panjang, mengatasi masalah skalabilitas dan pemeliharaan.

- **Mempercepat proses pengembangan dan mengurangi biaya**: Mengandalkan fitur yang sudah ada daripada proses mahal untuk membangunnya sendiri memungkinkan Anda fokus pada aspek lain dari aplikasi Anda yang mungkin lebih penting, seperti logika bisnis.
- **Kinerja yang lebih baik**: Saat membangun fitur dari awal, Anda akhirnya akan bertanya pada diri sendiri "Bagaimana skalabilitasnya? Apakah aplikasi ini mampu menangani lonjakan pengguna secara tiba-tiba?" SDK dan API yang terawat baik sering kali memiliki solusi bawaan untuk masalah ini.
- **Pemeliharaan yang lebih mudah**: Pembaruan dan peningkatan lebih mudah dikelola karena sebagian besar API dan SDK hanya memerlukan pembaruan pustaka saat versi yang lebih baru dirilis.
- **Akses ke teknologi mutakhir**: Memanfaatkan model yang telah disempurnakan dan dilatih pada dataset yang luas memberikan kemampuan bahasa alami pada aplikasi Anda.

Mengakses fitur dari SDK atau API biasanya melibatkan mendapatkan izin untuk menggunakan layanan yang disediakan, yang sering kali melalui penggunaan kunci unik atau token autentikasi. Kita akan menggunakan OpenAI Python Library untuk mengeksplorasi seperti apa ini. Anda juga dapat mencobanya sendiri di [notebook untuk OpenAI](./python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) atau [notebook untuk Azure OpenAI Services](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) untuk pelajaran ini.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
    api_key=API_KEY
    )

chat_completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Suggest two titles for an instructional lesson on chat applications for generative AI."}])
```

Contoh di atas menggunakan model GPT-3.5 Turbo untuk menyelesaikan prompt, tetapi perhatikan bahwa kunci API diatur sebelum melakukannya. Anda akan menerima kesalahan jika tidak mengatur kunci tersebut.

## Pengalaman Pengguna (UX)

Prinsip umum UX berlaku untuk aplikasi chat, tetapi ada beberapa pertimbangan tambahan yang menjadi sangat penting karena komponen pembelajaran mesin yang terlibat.

- **Mekanisme untuk mengatasi ambiguitas**: Model AI generatif kadang-kadang menghasilkan jawaban yang ambigu. Fitur yang memungkinkan pengguna meminta klarifikasi dapat membantu jika mereka menghadapi masalah ini.
- **Retensi konteks**: Model AI generatif yang canggih memiliki kemampuan untuk mengingat konteks dalam percakapan, yang dapat menjadi aset yang diperlukan untuk pengalaman pengguna. Memberikan pengguna kemampuan untuk mengontrol dan mengelola konteks meningkatkan pengalaman pengguna, tetapi memperkenalkan risiko menyimpan informasi sensitif pengguna. Pertimbangan tentang berapa lama informasi ini disimpan, seperti memperkenalkan kebijakan retensi, dapat menyeimbangkan kebutuhan konteks dengan privasi.
- **Personalisasi**: Dengan kemampuan untuk belajar dan beradaptasi, model AI menawarkan pengalaman yang disesuaikan untuk pengguna. Menyesuaikan pengalaman pengguna melalui fitur seperti profil pengguna tidak hanya membuat pengguna merasa dipahami, tetapi juga membantu mereka menemukan jawaban spesifik, menciptakan interaksi yang lebih efisien dan memuaskan.

Salah satu contoh personalisasi adalah pengaturan "Custom instructions" di ChatGPT OpenAI. Fitur ini memungkinkan Anda memberikan informasi tentang diri Anda yang mungkin menjadi konteks penting untuk prompt Anda. Berikut adalah contoh pengaturan custom instruction.

![Pengaturan Custom Instructions di ChatGPT](../../../translated_images/custom-instructions.b96f59aa69356fcfed456414221919e8996f93c90c20d0d58d1bc0221e3c909f.id.png)

"Profil" ini meminta ChatGPT untuk membuat rencana pelajaran tentang linked list. Perhatikan bahwa ChatGPT mempertimbangkan bahwa pengguna mungkin menginginkan rencana pelajaran yang lebih mendalam berdasarkan pengalamannya.

![Prompt di ChatGPT untuk rencana pelajaran tentang linked list](../../../translated_images/lesson-plan-prompt.cc47c488cf1343df5d67aa796a1acabca32c380e5b782971e289f6ab8b21cf5a.id.png)

### Kerangka Pesan Sistem Microsoft untuk Model Bahasa Besar

[Microsoft telah memberikan panduan](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) untuk menulis pesan sistem yang efektif saat menghasilkan respons dari LLM yang dibagi menjadi 4 area:

1. Mendefinisikan untuk siapa model tersebut, serta kemampuan dan keterbatasannya.
2. Mendefinisikan format output model.
3. Memberikan contoh spesifik yang menunjukkan perilaku yang diinginkan dari model.
4. Memberikan pengamanan perilaku tambahan.

### Aksesibilitas

Baik pengguna memiliki gangguan visual, pendengaran, motorik, atau kognitif, aplikasi chat yang dirancang dengan baik harus dapat digunakan oleh semua orang. Daftar berikut merinci fitur-fitur spesifik yang ditujukan untuk meningkatkan aksesibilitas bagi berbagai gangguan pengguna.

- **Fitur untuk Gangguan Visual**: Tema kontras tinggi dan teks yang dapat disesuaikan ukurannya, kompatibilitas dengan pembaca layar.
- **Fitur untuk Gangguan Pendengaran**: Fungsi teks-ke-suara dan suara-ke-teks, petunjuk visual untuk notifikasi audio.
- **Fitur untuk Gangguan Motorik**: Dukungan navigasi keyboard, perintah suara.
- **Fitur untuk Gangguan Kognitif**: Pilihan bahasa yang disederhanakan.

## Kustomisasi dan Penyempurnaan untuk Model Bahasa Spesifik Domain

Bayangkan sebuah aplikasi chat yang memahami istilah khusus perusahaan Anda dan mengantisipasi pertanyaan spesifik yang sering diajukan oleh basis pengguna. Ada beberapa pendekatan yang patut disebutkan:

- **Memanfaatkan model DSL**. DSL adalah singkatan dari domain specific language. Anda dapat memanfaatkan model DSL yang dilatih pada domain tertentu untuk memahami konsep dan skenario di dalamnya.
- **Menerapkan penyempurnaan**. Penyempurnaan adalah proses pelatihan lebih lanjut pada model Anda dengan data spesifik.

## Kustomisasi: Menggunakan DSL

Memanfaatkan model bahasa spesifik domain (DSL Models) dapat meningkatkan keterlibatan pengguna dengan menyediakan interaksi yang khusus dan relevan secara kontekstual. Ini adalah model yang dilatih atau disempurnakan untuk memahami dan menghasilkan teks yang terkait dengan bidang, industri, atau subjek tertentu. Opsi untuk menggunakan model DSL dapat bervariasi dari melatih model dari awal, hingga menggunakan model yang sudah ada melalui SDK dan API. Opsi lainnya adalah penyempurnaan, yang melibatkan pengadaptasian model yang sudah dilatih sebelumnya untuk domain tertentu.

## Kustomisasi: Menerapkan Penyempurnaan

Penyempurnaan sering kali dipertimbangkan ketika model yang sudah dilatih sebelumnya tidak cukup untuk domain khusus atau tugas tertentu.

Sebagai contoh, pertanyaan medis bersifat kompleks dan membutuhkan banyak konteks. Ketika seorang profesional medis mendiagnosis pasien, itu didasarkan pada berbagai faktor seperti gaya hidup atau kondisi yang sudah ada sebelumnya, dan bahkan mungkin bergantung pada jurnal medis terbaru untuk memvalidasi diagnosis mereka. Dalam skenario yang rumit seperti itu, aplikasi chat AI umum tidak dapat menjadi sumber yang dapat diandalkan.

### Skenario: aplikasi medis

Pertimbangkan aplikasi chat yang dirancang untuk membantu praktisi medis dengan menyediakan referensi cepat untuk pedoman pengobatan, interaksi obat, atau temuan penelitian terbaru.

Model umum mungkin cukup untuk menjawab pertanyaan medis dasar atau memberikan saran umum, tetapi mungkin kesulitan dengan hal berikut:

- **Kasus yang sangat spesifik atau kompleks**. Misalnya, seorang ahli saraf mungkin bertanya kepada aplikasi, "Apa praktik terbaik saat ini untuk mengelola epilepsi yang resisten terhadap obat pada pasien anak?"
- **Kurangnya kemajuan terbaru**. Model umum mungkin kesulitan memberikan jawaban terkini yang mencakup kemajuan terbaru dalam neurologi dan farmakologi.

Dalam kasus seperti ini, menyempurnakan model dengan dataset medis khusus dapat secara signifikan meningkatkan kemampuannya untuk menangani pertanyaan medis yang rumit dengan lebih akurat dan dapat diandalkan. Ini membutuhkan akses ke dataset yang besar dan relevan yang mewakili tantangan dan pertanyaan spesifik domain yang perlu dijawab.

## Pertimbangan untuk Pengalaman Chat Berbasis AI yang Berkualitas Tinggi

Bagian ini menguraikan kriteria untuk aplikasi chat "berkualitas tinggi," yang mencakup pengukuran metrik yang dapat ditindaklanjuti dan kepatuhan terhadap kerangka kerja yang memanfaatkan teknologi AI secara bertanggung jawab.

### Metrik Utama

Untuk menjaga kinerja aplikasi yang berkualitas tinggi, penting untuk melacak metrik utama dan pertimbangan. Pengukuran ini tidak hanya memastikan fungsi aplikasi tetapi juga menilai kualitas model AI dan pengalaman pengguna. Di bawah ini adalah daftar yang mencakup metrik dasar, AI, dan pengalaman pengguna yang perlu dipertimbangkan.

| Metrik                        | Definisi                                                                                                             | Pertimbangan untuk Pengembang Chat                                        |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Uptime**                    | Mengukur waktu aplikasi beroperasi dan dapat diakses oleh pengguna.                                                   | Bagaimana Anda akan meminimalkan waktu tidak aktif?                       |
| **Waktu Respons**             | Waktu yang diperlukan aplikasi untuk membalas pertanyaan pengguna.                                                    | Bagaimana Anda dapat mengoptimalkan pemrosesan kueri untuk meningkatkan waktu respons? |
| **Presisi**                   | Rasio prediksi positif yang benar terhadap jumlah total prediksi positif.                                             | Bagaimana Anda akan memvalidasi presisi model Anda?                       |
| **Recall (Sensitivitas)**     | Rasio prediksi positif yang benar terhadap jumlah positif yang sebenarnya.                                            | Bagaimana Anda akan mengukur dan meningkatkan recall?                     |
| **Skor F1**                   | Rata-rata harmonis dari presisi dan recall, yang menyeimbangkan trade-off antara keduanya.                            | Berapa target Skor F1 Anda? Bagaimana Anda akan menyeimbangkan presisi dan recall? |
| **Perplexity**                | Mengukur seberapa baik distribusi probabilitas yang diprediksi oleh model sesuai dengan distribusi data yang sebenarnya. | Bagaimana Anda akan meminimalkan perplexity?                              |
| **Metrik Kepuasan Pengguna**  | Mengukur persepsi pengguna terhadap aplikasi. Biasanya ditangkap melalui survei.                                      | Seberapa sering Anda akan mengumpulkan umpan balik pengguna? Bagaimana Anda akan beradaptasi berdasarkan umpan balik tersebut? |
| **Tingkat Kesalahan**         | Tingkat di mana model membuat kesalahan dalam memahami atau output.                                                   | Strategi apa yang Anda miliki untuk mengurangi tingkat kesalahan?         |
| **Siklus Pelatihan Ulang**    | Frekuensi di mana model diperbarui untuk mengintegrasikan data dan wawasan baru.                                      | Seberapa sering Anda akan melatih ulang model? Apa yang memicu siklus pelatihan ulang? |
| **Deteksi Anomali**           | Alat dan teknik untuk mengidentifikasi pola yang tidak biasa yang tidak sesuai dengan perilaku yang diharapkan.         | Bagaimana Anda akan merespons terhadap anomali?                                      |

### Menerapkan Praktik AI yang Bertanggung Jawab dalam Aplikasi Chat

Pendekatan Microsoft terhadap AI yang Bertanggung Jawab telah mengidentifikasi enam prinsip yang harus memandu pengembangan dan penggunaan AI. Berikut adalah prinsip-prinsip tersebut, definisinya, serta hal-hal yang perlu dipertimbangkan oleh pengembang aplikasi chat dan alasan mengapa hal tersebut penting.

| Prinsip                | Definisi Microsoft                                    | Pertimbangan untuk Pengembang Chat                                      | Mengapa Hal Ini Penting                                                                  |
| ---------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Keadilan              | Sistem AI harus memperlakukan semua orang secara adil. | Pastikan aplikasi chat tidak mendiskriminasi berdasarkan data pengguna. | Untuk membangun kepercayaan dan inklusivitas di antara pengguna; menghindari konsekuensi hukum. |
| Keandalan dan Keamanan | Sistem AI harus berfungsi dengan andal dan aman.       | Terapkan pengujian dan langkah-langkah pengamanan untuk meminimalkan kesalahan dan risiko. | Menjamin kepuasan pengguna dan mencegah potensi bahaya.                                 |
| Privasi dan Keamanan   | Sistem AI harus aman dan menghormati privasi.          | Terapkan enkripsi yang kuat dan langkah-langkah perlindungan data.      | Untuk melindungi data sensitif pengguna dan mematuhi undang-undang privasi.             |
| Inklusivitas           | Sistem AI harus memberdayakan semua orang dan melibatkan mereka. | Rancang UI/UX yang dapat diakses dan mudah digunakan untuk berbagai audiens. | Memastikan berbagai kalangan dapat menggunakan aplikasi secara efektif.                 |
| Transparansi           | Sistem AI harus dapat dipahami.                       | Sediakan dokumentasi yang jelas dan alasan untuk respons AI.            | Pengguna lebih mungkin mempercayai sistem jika mereka dapat memahami bagaimana keputusan dibuat. |
| Akuntabilitas          | Orang harus bertanggung jawab atas sistem AI.         | Tetapkan proses yang jelas untuk mengaudit dan meningkatkan keputusan AI. | Memungkinkan perbaikan berkelanjutan dan tindakan korektif jika terjadi kesalahan.       |

## Tugas

Lihat [tugas](../../../07-building-chat-applications/python). Tugas ini akan membawa Anda melalui serangkaian latihan mulai dari menjalankan prompt chat pertama Anda, hingga mengklasifikasi dan merangkum teks, dan lainnya. Perhatikan bahwa tugas tersedia dalam berbagai bahasa pemrograman!

## Kerja Hebat! Lanjutkan Perjalanan Anda

Setelah menyelesaikan pelajaran ini, lihat [koleksi Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan Anda tentang AI Generatif!

Lanjutkan ke Pelajaran 8 untuk melihat bagaimana Anda dapat mulai [membangun aplikasi pencarian](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.