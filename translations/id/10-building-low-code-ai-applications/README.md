# Membangun Aplikasi AI Low Code

[![Membangun Aplikasi AI Low Code](../../../translated_images/id/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Klik gambar di atas untuk melihat video pelajaran ini)_

## Pendahuluan

Sekarang kita telah belajar cara membangun aplikasi penghasil gambar, mari kita bahas mengenai low code. Generative AI dapat digunakan untuk berbagai bidang termasuk low code, tapi apa itu low code dan bagaimana kita dapat menambahkan AI ke dalamnya?

Membangun aplikasi dan solusi menjadi lebih mudah bagi pengembang tradisional maupun non-pengembang melalui penggunaan Platform Pengembangan Low Code. Platform Pengembangan Low Code memungkinkan Anda membangun aplikasi dan solusi dengan sedikit atau tanpa kode. Ini dicapai dengan menyediakan lingkungan pengembangan visual yang memungkinkan Anda menggeser dan melepaskan komponen untuk membangun aplikasi dan solusi. Ini memungkinkan Anda membangun aplikasi dan solusi lebih cepat dan dengan sumber daya yang lebih sedikit. Dalam pelajaran ini, kami membahas secara mendalam cara menggunakan Low Code dan bagaimana meningkatkan pengembangan low code dengan AI menggunakan Power Platform.

Power Platform memberikan organisasi kesempatan untuk memberdayakan tim mereka membangun solusi sendiri melalui lingkungan dengan kode rendah atau tanpa kode yang intuitif. Lingkungan ini membantu menyederhanakan proses pembangunan solusi. Dengan Power Platform, solusi dapat dibuat dalam hitungan hari atau minggu, bukan bulan atau tahun. Power Platform terdiri dari lima produk utama: Power Apps, Power Automate, Power BI, Power Pages, dan Copilot Studio.

Pelajaran ini mencakup:

- Pengenalan Generative AI di Power Platform
- Pengenalan Copilot dan cara menggunakannya
- Menggunakan Generative AI untuk membangun aplikasi dan alur di Power Platform
- Memahami Model AI di Power Platform dengan AI Builder
- Membangun agen cerdas dengan Microsoft Copilot Studio

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan mampu:

- Memahami cara kerja Copilot di Power Platform.

- Membangun Aplikasi Pengelola Tugas Mahasiswa untuk startup pendidikan kami.

- Membangun Alur Pemrosesan Faktur yang menggunakan AI untuk mengekstrak informasi dari faktur.

- Menerapkan praktik terbaik saat menggunakan Model AI Buat Teks dengan GPT.

- Memahami apa itu Microsoft Copilot Studio dan cara membangun agen cerdas dengannya.

Alat dan teknologi yang akan Anda gunakan dalam pelajaran ini adalah:

- **Power Apps**, untuk aplikasi Pengelola Tugas Mahasiswa, yang menyediakan lingkungan pengembangan low-code untuk membangun aplikasi guna melacak, mengelola, dan berinteraksi dengan data.

- **Dataverse**, untuk penyimpanan data aplikasi Pengelola Tugas Mahasiswa dimana Dataverse akan menyediakan platform data low-code untuk menyimpan data aplikasi.

- **Power Automate**, untuk alur Pemrosesan Faktur dimana Anda akan memiliki lingkungan pengembangan low-code untuk membangun workflow mengotomatisasi proses Pemrosesan Faktur.

- **AI Builder**, untuk Model AI Pemrosesan Faktur dimana Anda akan menggunakan Model AI yang sudah dibuat untuk memproses faktur untuk startup kami.

## Generative AI di Power Platform

Meningkatkan pengembangan dan aplikasi low-code dengan generative AI adalah fokus utama untuk Power Platform. Tujuannya adalah memungkinkan setiap orang membangun aplikasi, situs, dashboard bertenaga AI, dan mengotomatisasi proses dengan AI, _tanpa memerlukan keahlian data science_. Tujuan ini dicapai dengan mengintegrasikan generative AI ke pengalaman pengembangan low-code di Power Platform dalam bentuk Copilot dan AI Builder.

### Bagaimana cara kerjanya?

Copilot adalah asisten AI yang memungkinkan Anda membangun solusi Power Platform dengan mendeskripsikan kebutuhan Anda dalam serangkaian langkah percakapan menggunakan bahasa alami. Anda bisa misalnya menginstruksikan asisten AI Anda untuk menyatakan bidang apa saja yang akan digunakan aplikasi Anda dan ia akan membuat aplikasi beserta model data dasarnya atau Anda bisa menentukan bagaimana mengatur alur di Power Automate.

Anda dapat menggunakan fungsionalitas yang didukung Copilot sebagai fitur di layar aplikasi Anda untuk memungkinkan pengguna menemukan wawasan melalui interaksi percakapan.

AI Builder adalah kemampuan AI low-code yang tersedia di Power Platform yang memungkinkan Anda menggunakan Model AI untuk membantu mengotomatisasi proses dan memprediksi hasil. Dengan AI Builder Anda dapat membawa AI ke aplikasi dan alur yang terhubung ke data Anda di Dataverse atau berbagai sumber data cloud, seperti SharePoint, OneDrive, atau Azure.

Copilot tersedia di semua produk Power Platform: Power Apps, Power Automate, Power BI, Power Pages, dan Copilot Studio (sebelumnya Power Virtual Agents). AI Builder tersedia di Power Apps dan Power Automate. Dalam pelajaran ini, kami akan fokus pada cara menggunakan Copilot dan AI Builder di Power Apps dan Power Automate untuk membangun solusi bagi startup pendidikan kami.

### Copilot di Power Apps

Sebagai bagian dari Power Platform, Power Apps menyediakan lingkungan pengembangan low-code untuk membangun aplikasi guna melacak, mengelola, dan berinteraksi dengan data. Ini adalah rangkaian layanan pengembangan aplikasi dengan platform data yang dapat diskalakan dan kemampuan untuk terhubung ke layanan cloud dan data lokal. Power Apps memungkinkan Anda membangun aplikasi yang berjalan di browser, tablet, dan ponsel, dan dapat dibagikan dengan rekan kerja. Power Apps memudahkan pengguna dalam pengembangan aplikasi dengan antarmuka yang sederhana, sehingga setiap pengguna bisnis atau pengembang profesional dapat membangun aplikasi kustom. Pengalaman pengembangan aplikasi juga diperkuat dengan Generative AI melalui Copilot.

Fitur asisten AI Copilot di Power Apps memungkinkan Anda menjelaskan jenis aplikasi yang Anda butuhkan dan informasi apa yang ingin aplikasi Anda lacak, kumpulkan, atau tampilkan. Copilot kemudian menghasilkan aplikasi Canvas responsif berdasarkan deskripsi Anda. Anda kemudian dapat menyesuaikan aplikasi agar sesuai kebutuhan Anda. AI Copilot juga menghasilkan dan menyarankan Tabel Dataverse dengan kolom yang Anda perlukan untuk menyimpan data yang ingin Anda lacak dan beberapa data contoh. Kita akan melihat apa itu Dataverse dan bagaimana Anda dapat menggunakannya di Power Apps dalam pelajaran ini nanti. Anda kemudian dapat menyesuaikan tabel agar sesuai kebutuhan Anda menggunakan fitur asisten AI Copilot melalui langkah-langkah percakapan. Fitur ini tersedia langsung dari layar beranda Power Apps.

### Copilot di Power Automate

Sebagai bagian dari Power Platform, Power Automate memungkinkan pengguna membuat workflow otomatis antara aplikasi dan layanan. Ini membantu mengotomatisasi proses bisnis yang berulang seperti komunikasi, pengumpulan data, dan persetujuan keputusan. Antarmuka yang sederhana memungkinkan pengguna dengan berbagai tingkat kompetensi teknis (dari pemula hingga pengembang berpengalaman) untuk mengotomatisasi tugas kerja. Pengalaman pengembangan workflow juga diperkuat dengan Generative AI melalui Copilot.

Fitur asisten AI Copilot di Power Automate memungkinkan Anda menjelaskan jenis alur yang Anda butuhkan dan tindakan apa yang ingin alur Anda lakukan. Copilot kemudian menghasilkan alur berdasarkan deskripsi Anda. Anda dapat menyesuaikan alur agar sesuai kebutuhan Anda. AI Copilot juga menghasilkan dan menyarankan tindakan yang Anda perlukan untuk menyelesaikan tugas yang ingin Anda otomasi. Kita akan melihat apa itu alur dan bagaimana Anda dapat menggunakannya di Power Automate dalam pelajaran ini nanti. Anda kemudian dapat menyesuaikan tindakan untuk memenuhi kebutuhan Anda menggunakan fitur asisten AI Copilot melalui langkah percakapan. Fitur ini tersedia langsung dari layar beranda Power Automate.

## Membangun Agen Cerdas dengan Microsoft Copilot Studio

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst) (sebelumnya Power Virtual Agents) adalah anggota low-code dari Power Platform untuk membangun **agen AI** — copilot percakapan yang dapat menjawab pertanyaan, mengambil tindakan, dan mengotomatisasi tugas atas nama pengguna Anda. Sama seperti bagian lain dari Power Platform, Anda membangun agen ini dalam pengalaman visual yang mengutamakan bahasa alami: Anda mendeskripsikan apa yang ingin dilakukan agen, dan Copilot Studio membantu membangun instruksi, pengetahuan, dan tindakannya.

Untuk startup pendidikan kami, Anda bisa membangun agen yang menjawab pertanyaan mahasiswa tentang kursus, memeriksa tenggat tugas, dan bahkan mengirim email ke pengajar — semua tanpa menulis kode.

Berikut ini beberapa kemampuan terbaru yang membuat Copilot Studio kuat:

- **Jawaban generatif dari pengetahuan Anda**. Alih-alih menyusun setiap percakapan secara manual, Anda dapat menghubungkan **sumber pengetahuan** — situs web publik, SharePoint, OneDrive, Dataverse, file yang diunggah, atau data perusahaan melalui konektor — dan agen menghasilkan jawaban yang didasarkan pada sumber tersebut.

- **Orkestrasi generatif**. Alih-alih bergantung pada frasa pemicu yang kaku, agen menggunakan AI untuk memahami permintaan dan secara dinamis memutuskan pengetahuan, topik, dan tindakan mana yang dikombinasikan untuk memenuhinya, termasuk menggabungkan beberapa langkah.

- **Tindakan dan konektor**. Agen bisa *melakukan* sesuatu, tidak hanya mengobrol. Anda dapat memberikan agen tindakan yang didukung oleh lebih dari 1.500 konektor Power Platform yang sudah dibangun, alur Power Automate, API REST kustom, prompt, atau server **Model Context Protocol (MCP)**.

- **Agen otonom**. Agen tidak terbatas hanya merespon di jendela obrolan. Anda dapat membangun **agen otonom** yang dipicu oleh peristiwa — seperti email baru, catatan baru di Dataverse, atau file yang diunggah — dan kemudian bertindak di latar belakang untuk menyelesaikan tugas.

- **Orkestrasi multi-agen**. Agen dapat memanggil agen lain. Agen Copilot Studio dapat menyerahkan tugas ke, atau diperluas dengan, agen lain, termasuk agen yang dipublikasikan ke Microsoft 365 Copilot dan agen yang dibangun di Microsoft Foundry.

- **Pilihan model**. Selain model bawaan, Anda dapat membawa model dari katalog model Microsoft Foundry untuk menyesuaikan cara agen Anda berpikir dan merespon.

- **Publikasi di mana saja**. Setelah dibangun, agen dapat dipublikasikan ke beberapa saluran — Microsoft Teams, Microsoft 365 Copilot, situs web atau aplikasi kustom, dan lainnya — dengan keamanan, autentikasi, dan analitik yang dikelola melalui pengalaman admin Power Platform.

Anda dapat mulai membangun agen pertama Anda di [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) dan mempelajari lebih lanjut di [dokumentasi Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst).

## Tugas: Kelola tugas siswa dan faktur untuk startup kami, menggunakan Copilot

Startup kami menyediakan kursus daring untuk siswa. Startup ini tumbuh dengan cepat dan kini kesulitan memenuhi permintaan kursusnya. Startup ini telah mempekerjakan Anda sebagai pengembang Power Platform untuk membantu mereka membangun solusi low code guna mengelola tugas siswa dan faktur mereka. Solusinya harus mampu membantu mereka melacak dan mengelola tugas siswa melalui aplikasi dan mengotomatisasi proses pemrosesan faktur melalui workflow. Anda diminta menggunakan Generative AI untuk mengembangkan solusi ini.

Saat memulai menggunakan Copilot, Anda dapat menggunakan [Perpustakaan Prompt Copilot Power Platform](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) untuk memulai dengan prompt-prompt yang tersedia. Perpustakaan ini berisi daftar prompt yang dapat Anda gunakan untuk membangun aplikasi dan alur dengan Copilot. Anda juga dapat menggunakan prompt di perpustakaan untuk mendapatkan ide bagaimana mendeskripsikan kebutuhan Anda kepada Copilot.

### Bangun Aplikasi Pengelola Tugas Mahasiswa untuk Startup Kami

Para pendidik di startup kami kesulitan untuk melacak tugas siswa. Mereka menggunakan spreadsheet untuk melacak tugas tapi kini sulit dikelola karena jumlah siswa bertambah. Mereka meminta Anda membangun aplikasi yang membantu mereka melacak dan mengelola tugas siswa. Aplikasi harus memungkinkan mereka menambah tugas baru, melihat tugas, memperbarui tugas, dan menghapus tugas. Aplikasi juga harus memungkinkan pendidik dan siswa melihat tugas yang sudah dinilai dan yang belum dinilai.

Anda akan membangun aplikasi menggunakan Copilot di Power Apps dengan mengikuti langkah berikut:

1. Buka layar beranda [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

1. Gunakan area teks di layar beranda untuk mendeskripsikan aplikasi yang ingin Anda bangun. Contohnya, **_Saya ingin membangun aplikasi untuk melacak dan mengelola tugas siswa_**. Klik tombol **Kirim** untuk mengirim prompt ke AI Copilot.

![Deskripsikan aplikasi yang ingin Anda bangun](../../../translated_images/id/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. AI Copilot akan menyarankan Tabel Dataverse dengan kolom yang Anda perlukan untuk menyimpan data yang ingin Anda lacak serta beberapa data contoh. Anda kemudian dapat menyesuaikan tabel agar memenuhi kebutuhan Anda menggunakan fitur asisten AI Copilot melalui langkah percakapan.

   > **Penting**: Dataverse adalah platform data dasar untuk Power Platform. Ini adalah platform data low-code untuk menyimpan data aplikasi. Ini adalah layanan yang dikelola penuh yang menyimpan data dengan aman di Microsoft Cloud dan dipasang dalam lingkungan Power Platform Anda. Dataverse dilengkapi dengan kemampuan pengelolaan data bawaan, seperti klasifikasi data, jejak data, kontrol akses yang terperinci, dan lainnya. Anda dapat mempelajari lebih lanjut tentang Dataverse [di sini](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Kolom yang disarankan dalam tabel baru Anda](../../../translated_images/id/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. Para pendidik ingin mengirim email kepada siswa yang telah mengumpulkan tugas agar tetap mendapat informasi tentang perkembangan tugas mereka. Anda dapat menggunakan Copilot untuk menambahkan kolom baru pada tabel untuk menyimpan email siswa. Misalnya, Anda dapat menggunakan prompt berikut untuk menambahkan kolom baru ke tabel: **_Saya ingin menambahkan kolom untuk menyimpan email siswa_**. Klik tombol **Kirim** untuk mengirim prompt ke AI Copilot.

![Menambahkan kolom baru](../../../translated_images/id/copilot-new-column.35e15ff21acaf274.webp)

1. AI Copilot akan menghasilkan kolom baru dan Anda kemudian dapat menyesuaikan kolom agar sesuai kebutuhan Anda.


1. Setelah Anda selesai dengan tabel, klik tombol **Create app** untuk membuat aplikasi.

1. AI Copilot akan menghasilkan aplikasi Canvas responsif berdasarkan deskripsi Anda. Anda kemudian dapat menyesuaikan aplikasi tersebut sesuai kebutuhan Anda.

1. Untuk pendidik mengirim email kepada siswa, Anda dapat menggunakan Copilot untuk menambahkan layar baru ke aplikasi. Misalnya, Anda dapat menggunakan perintah berikut untuk menambahkan layar baru ke aplikasi: **_I want to add a screen to send emails to students_**. Klik tombol **Send** untuk mengirim perintah ke AI Copilot.

![Adding a new screen via a prompt instruction](../../../translated_images/id/copilot-new-screen.2e0bef7132a17392.webp)

1. AI Copilot akan menghasilkan layar baru dan Anda kemudian dapat menyesuaikan layar tersebut agar sesuai dengan kebutuhan Anda.

1. Setelah Anda selesai dengan aplikasi, klik tombol **Save** untuk menyimpan aplikasi.

1. Untuk membagikan aplikasi kepada para pendidik, klik tombol **Share** lalu klik tombol **Share** lagi. Anda kemudian dapat membagikan aplikasi tersebut kepada para pendidik dengan memasukkan alamat email mereka.

> **Pekerjaan rumah Anda**: Aplikasi yang baru Anda buat adalah awal yang baik tetapi bisa diperbaiki. Dengan fitur email, pendidik hanya bisa mengirim email ke siswa secara manual dengan mengetik alamat email mereka. Bisakah Anda menggunakan Copilot untuk membangun automasi yang memungkinkan pendidik mengirim email ke siswa secara otomatis ketika mereka mengirimkan tugas? Petunjuk Anda adalah dengan perintah yang tepat Anda dapat menggunakan Copilot di Power Automate untuk membuat ini.

### Bangun Tabel Informasi Faktur untuk Startup Kami

Tim keuangan startup kami mengalami kesulitan melacak faktur. Mereka telah menggunakan spreadsheet untuk melacak faktur tetapi hal ini menjadi sulit untuk dikelola seiring bertambahnya jumlah faktur. Mereka meminta Anda untuk membuat tabel yang akan membantu mereka menyimpan, melacak, dan mengelola informasi dari faktur yang mereka terima. Tabel ini harus digunakan untuk membangun automasi yang akan mengekstrak semua informasi faktur dan menyimpannya dalam tabel. Tabel ini juga harus memungkinkan tim keuangan untuk melihat faktur yang sudah dibayar dan yang belum dibayar.

Power Platform memiliki platform data dasar yang disebut Dataverse yang memungkinkan Anda untuk menyimpan data untuk aplikasi dan solusi Anda. Dataverse menyediakan platform data low-code untuk menyimpan data aplikasi. Ini adalah layanan yang sepenuhnya dikelola yang menyimpan data dengan aman di Microsoft Cloud dan disediakan dalam lingkungan Power Platform Anda. Dataverse dilengkapi dengan kemampuan tata kelola data bawaan, seperti klasifikasi data, jejak data, kontrol akses terperinci, dan lain-lain. Anda dapat mempelajari lebih lanjut [tentang Dataverse di sini](https://learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Mengapa kita harus menggunakan Dataverse untuk startup kita? Tabel standar dan khusus dalam Dataverse menyediakan opsi penyimpanan yang aman dan berbasis cloud untuk data Anda. Tabel memungkinkan Anda menyimpan berbagai jenis data, mirip seperti Anda menggunakan beberapa worksheet dalam satu workbook Excel. Anda dapat menggunakan tabel untuk menyimpan data yang spesifik untuk organisasi atau kebutuhan bisnis Anda. Beberapa manfaat yang akan didapat startup kami dari menggunakan Dataverse termasuk tetapi tidak terbatas pada:

- **Mudah dikelola**: Baik metadata maupun data disimpan di cloud, jadi Anda tidak perlu khawatir tentang detail bagaimana data tersebut disimpan atau dikelola. Anda dapat fokus membangun aplikasi dan solusi Anda.

- **Aman**: Dataverse menyediakan opsi penyimpanan yang aman dan berbasis cloud untuk data Anda. Anda dapat mengontrol siapa yang memiliki akses ke data di tabel Anda dan bagaimana mereka dapat mengaksesnya menggunakan keamanan berbasis peran.

- **Metadata kaya**: Tipe data dan relasi digunakan langsung dalam Power Apps

- **Logika dan validasi**: Anda dapat menggunakan aturan bisnis, field yang dihitung, dan aturan validasi untuk menegakkan logika bisnis dan menjaga akurasi data.

Sekarang Anda tahu apa itu Dataverse dan mengapa Anda harus menggunakannya, mari kita lihat bagaimana Anda dapat menggunakan Copilot untuk membuat tabel di Dataverse sesuai kebutuhan tim keuangan kami.

> **Catatan** : Anda akan menggunakan tabel ini di bagian berikutnya untuk membangun automasi yang akan mengekstrak semua informasi faktur dan menyimpannya di tabel.

Untuk membuat tabel di Dataverse menggunakan Copilot, ikuti langkah-langkah berikut:

1. Buka layar utama [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

2. Pada bilah navigasi kiri, pilih **Tables** lalu klik **Describe the new Table**.

![Select new table](../../../translated_images/id/describe-new-table.0792373eb757281e.webp)

1. Pada layar **Describe the new Table**, gunakan area teks untuk mendeskripsikan tabel yang ingin Anda buat. Misalnya, **_I want to create a table to store invoice information_**. Klik tombol **Send** untuk mengirim perintah ke AI Copilot.

![Describe the table](../../../translated_images/id/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. AI Copilot akan menyarankan Tabel Dataverse dengan bidang yang Anda butuhkan untuk menyimpan data yang ingin Anda lacak dan beberapa contoh data. Anda kemudian dapat menyesuaikan tabel tersebut menggunakan fitur asisten AI Copilot melalui langkah percakapan.

![Suggested Dataverse table](../../../translated_images/id/copilot-dataverse-table.b3bc936091324d9d.webp)

1. Tim keuangan ingin mengirim email ke pemasok untuk memperbarui status faktur mereka saat ini. Anda dapat menggunakan Copilot untuk menambahkan bidang baru ke tabel untuk menyimpan email pemasok. Misalnya, Anda dapat menggunakan perintah berikut untuk menambahkan bidang baru ke tabel: **_I want to add a column to store supplier email_**. Klik tombol **Send** untuk mengirim perintah ke AI Copilot.

1. AI Copilot akan membuat bidang baru dan Anda kemudian dapat menyesuaikan bidang tersebut sesuai kebutuhan Anda.

1. Setelah Anda selesai dengan tabel, klik tombol **Create** untuk membuat tabel.

## Model AI di Power Platform dengan AI Builder

AI Builder adalah kapabilitas AI low-code yang tersedia di Power Platform yang memungkinkan Anda menggunakan Model AI untuk membantu mengotomatisasi proses dan memprediksi hasil. Dengan AI Builder Anda dapat membawa AI ke aplikasi dan alur yang terhubung ke data Anda di Dataverse atau berbagai sumber data cloud, seperti SharePoint, OneDrive, atau Azure.

## Model AI Prebuilt vs Model AI Kustom

AI Builder menyediakan dua jenis Model AI: Model AI Prebuilt dan Model AI Kustom. Model AI Prebuilt adalah Model AI siap pakai yang dilatih oleh Microsoft dan tersedia di Power Platform. Ini membantu Anda menambahkan kecerdasan ke aplikasi dan alur tanpa harus mengumpulkan data dan kemudian membangun, melatih, dan menerbitkan model Anda sendiri. Anda dapat menggunakan model ini untuk mengotomatisasi proses dan memprediksi hasil.

Beberapa Model AI Prebuilt yang tersedia di Power Platform meliputi:

- **Key Phrase Extraction**: Model ini mengekstrak frasa kunci dari teks.
- **Language Detection**: Model ini mendeteksi bahasa sebuah teks.
- **Sentiment Analysis**: Model ini mendeteksi sentimen positif, negatif, netral, atau campuran dalam teks.
- **Business Card Reader**: Model ini mengekstrak informasi dari kartu nama.
- **Text Recognition**: Model ini mengekstrak teks dari gambar.
- **Object Detection**: Model ini mendeteksi dan mengekstrak objek dari gambar.
- **Document processing**: Model ini mengekstrak informasi dari formulir.
- **Invoice Processing**: Model ini mengekstrak informasi dari faktur.

Dengan Model AI Kustom Anda dapat membawa model Anda sendiri ke AI Builder sehingga dapat berfungsi seperti model kustom AI Builder lainnya, memungkinkan Anda melatih model menggunakan data Anda sendiri. Anda dapat menggunakan model ini untuk mengotomatisasi proses dan memprediksi hasil baik di Power Apps maupun Power Automate. Saat menggunakan model Anda sendiri ada batasan yang berlaku. Baca lebih lanjut tentang [batasan ini](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![AI builder models](../../../translated_images/id/ai-builder-models.8069423b84cfc47f.webp)

## Tugas #2 - Bangun Alur Pemrosesan Faktur untuk Startup Kami

Tim keuangan mengalami kesulitan memproses faktur. Mereka sudah menggunakan spreadsheet untuk melacak faktur tetapi hal ini menjadi sulit untuk dikelola seiring bertambahnya jumlah faktur. Mereka meminta Anda membangun alur kerja yang akan membantu mereka memproses faktur menggunakan AI. Alur kerja harus memungkinkan mereka mengekstrak informasi dari faktur dan menyimpan informasi tersebut di tabel Dataverse. Alur kerja juga harus memungkinkan mereka mengirim email ke tim keuangan dengan informasi yang telah diekstrak.

Sekarang Anda tahu apa itu AI Builder dan mengapa Anda harus menggunakannya, mari kita lihat bagaimana Anda dapat menggunakan Model AI Pemrosesan Faktur di AI Builder, yang sudah kita bahas sebelumnya, untuk membangun alur kerja yang membantu tim keuangan memproses faktur.

Untuk membangun alur kerja yang membantu tim keuangan memproses faktur menggunakan Model AI Pemrosesan Faktur di AI Builder, ikuti langkah-langkah berikut:

1. Buka layar utama [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst).

2. Gunakan area teks pada layar utama untuk mendeskripsikan alur kerja yang ingin Anda buat. Misalnya, **_Process an invoice when it arrives in my mailbox_**. Klik tombol **Send** untuk mengirim perintah ke AI Copilot.

   ![Copilot power automate](../../../translated_images/id/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. AI Copilot akan menyarankan tindakan yang perlu Anda lakukan untuk mengotomatiskan tugas yang ingin dilakukan. Anda dapat mengklik tombol **Next** untuk melalui langkah-langkah berikutnya.

4. Pada langkah berikutnya, Power Automate akan meminta Anda mengatur koneksi yang diperlukan untuk alur tersebut. Setelah selesai, klik tombol **Create flow** untuk membuat alur.

5. AI Copilot akan menghasilkan alur dan Anda dapat menyesuaikan alur tersebut sesuai kebutuhan Anda.

6. Perbarui trigger alur dan atur **Folder** ke folder tempat faktur disimpan. Misalnya, Anda dapat mengatur folder ke **Inbox**. Klik **Show advanced options** dan atur **Only with Attachments** ke **Yes**. Ini akan memastikan alur hanya berjalan ketika email dengan lampiran diterima di folder tersebut.

7. Hapus tindakan berikut dari alur: **HTML to text**, **Compose**, **Compose 2**, **Compose 3**, dan **Compose 4** karena Anda tidak akan menggunakannya.

8. Hapus tindakan **Condition** dari alur karena Anda tidak akan menggunakannya. Alur harus terlihat seperti screenshot berikut:

   ![power automate, remove actions](../../../translated_images/id/powerautomate-remove-actions.7216392fe684ceba.webp)

9. Klik tombol **Add an action** dan cari **Dataverse**. Pilih tindakan **Add a new row**.

10. Pada tindakan **Extract Information from invoices**, perbarui **Invoice File** untuk mengarah ke **Attachment Content** dari email. Ini akan memastikan alur mengekstrak informasi dari lampiran faktur.

11. Pilih **Table** yang Anda buat sebelumnya. Misalnya, Anda dapat memilih tabel **Invoice Information**. Pilih konten dinamis dari tindakan sebelumnya untuk mengisi bidang berikut:

    - ID
    - Amount
    - Date
    - Name
    - Status - Atur **Status** menjadi **Pending**.
    - Supplier Email - Gunakan konten dinamis **From** dari trigger **When a new email arrives**.

    ![power automate add row](../../../translated_images/id/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. Setelah selesai dengan alur, klik tombol **Save** untuk menyimpan alur. Anda kemudian dapat menguji alur dengan mengirim email berisi faktur ke folder yang Anda tentukan di trigger.

> **Pekerjaan rumah Anda**: Alur yang baru Anda buat adalah awal yang baik, sekarang Anda harus memikirkan bagaimana membangun automasi yang memungkinkan tim keuangan kami mengirim email ke pemasok untuk memperbarui mereka dengan status faktur saat ini. Petunjuk Anda: alur harus dijalankan ketika status faktur berubah.

## Gunakan Model AI Generasi Teks di Power Automate

Model AI Create Text with GPT di AI Builder memungkinkan Anda menghasilkan teks berdasarkan perintah dan didukung oleh Microsoft Azure OpenAI Service. Dengan kemampuan ini, Anda dapat mengintegrasikan teknologi GPT (Generative Pre-Trained Transformer) ke dalam aplikasi dan alur Anda untuk membangun berbagai alur otomatis dan aplikasi yang informatif.

Model GPT menjalani pelatihan intensif pada jumlah data yang sangat besar, memungkinkan mereka menghasilkan teks yang sangat mirip dengan bahasa manusia ketika diberi perintah. Ketika diintegrasikan dengan automasi alur kerja, model AI seperti GPT dapat digunakan untuk menyederhanakan dan mengotomatisasi berbagai tugas.

Misalnya, Anda dapat membangun alur untuk secara otomatis menghasilkan teks untuk berbagai kasus penggunaan, seperti: draf email, deskripsi produk, dan lainnya. Anda juga dapat menggunakan model ini untuk menghasilkan teks bagi berbagai aplikasi, seperti chatbot dan aplikasi layanan pelanggan yang memungkinkan agen layanan pelanggan merespons pertanyaan pelanggan secara efektif dan efisien.

![create a prompt](../../../translated_images/id/create-prompt-gpt.69d429300c2e870a.webp)


Untuk mempelajari cara menggunakan Model AI ini di Power Automate, melalui modul [Tambahkan kecerdasan dengan AI Builder dan GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Kerja Bagus! Lanjutkan Pembelajaran Anda

Setelah menyelesaikan pelajaran ini, lihat koleksi [Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif Anda!

Ingin menyesuaikan dan mendapatkan lebih banyak dari Copilot? Jelajahi [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) — sebuah koleksi kontribusi komunitas berisi instruksi, agen, keterampilan, dan konfigurasi untuk membantu Anda memaksimalkan GitHub Copilot.

Pergi ke Pelajaran 11 di mana kita akan melihat cara [mengintegrasikan AI Generatif dengan Function Calling](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->