<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5ff3b6204a695a117d6f452403c95f7",
  "translation_date": "2025-05-19T20:45:47+00:00",
  "source_file": "10-building-low-code-ai-applications/README.md",
  "language_code": "id"
}
-->
# Membangun Aplikasi AI dengan Kode Rendah

[![Membangun Aplikasi AI dengan Kode Rendah](../../../translated_images/10-lesson-banner.84b607fa749c0d53ffe98212c5c3b81292bb041d1aec07da8fd720e9c01b5718.id.png)](https://aka.ms/gen-ai-lesson10-gh?WT.mc_id=academic-105485-koreyst)

> _(Klik gambar di atas untuk melihat video dari pelajaran ini)_

## Pendahuluan

Setelah kita belajar bagaimana membangun aplikasi penghasil gambar, mari kita bicara tentang kode rendah. AI generatif dapat digunakan untuk berbagai bidang termasuk kode rendah, tetapi apa itu kode rendah dan bagaimana kita bisa menambahkan AI ke dalamnya?

Membangun aplikasi dan solusi menjadi lebih mudah bagi pengembang tradisional dan non-pengembang melalui penggunaan Platform Pengembangan Kode Rendah. Platform Pengembangan Kode Rendah memungkinkan Anda membangun aplikasi dan solusi dengan sedikit atau tanpa kode. Ini dicapai dengan menyediakan lingkungan pengembangan visual yang memungkinkan Anda untuk menyeret dan melepaskan komponen untuk membangun aplikasi dan solusi. Ini memungkinkan Anda membangun aplikasi dan solusi lebih cepat dan dengan sumber daya yang lebih sedikit. Dalam pelajaran ini, kita akan mendalami bagaimana menggunakan kode rendah dan bagaimana meningkatkan pengembangan kode rendah dengan AI menggunakan Power Platform.

Power Platform memberikan organisasi kesempatan untuk memberdayakan tim mereka untuk membangun solusi mereka sendiri melalui lingkungan intuitif yang menggunakan kode rendah atau tanpa kode. Lingkungan ini membantu menyederhanakan proses pembangunan solusi. Dengan Power Platform, solusi dapat dibangun dalam hitungan hari atau minggu, bukan bulan atau tahun. Power Platform terdiri dari lima produk utama: Power Apps, Power Automate, Power BI, Power Pages, dan Copilot Studio.

Pelajaran ini mencakup:

- Pengantar AI Generatif di Power Platform
- Pengantar Copilot dan bagaimana menggunakannya
- Menggunakan AI Generatif untuk membangun aplikasi dan aliran di Power Platform
- Memahami Model AI di Power Platform dengan AI Builder

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan dapat:

- Memahami bagaimana Copilot bekerja di Power Platform.

- Membangun Aplikasi Pelacak Tugas Siswa untuk startup pendidikan kita.

- Membangun Aliran Pemrosesan Faktur yang menggunakan AI untuk mengekstraksi informasi dari faktur.

- Menerapkan praktik terbaik saat menggunakan Model AI Buat Teks dengan GPT.

Alat dan teknologi yang akan Anda gunakan dalam pelajaran ini adalah:

- **Power Apps**, untuk aplikasi Pelacak Tugas Siswa, yang menyediakan lingkungan pengembangan kode rendah untuk membangun aplikasi untuk melacak, mengelola, dan berinteraksi dengan data.

- **Dataverse**, untuk menyimpan data untuk aplikasi Pelacak Tugas Siswa di mana Dataverse akan menyediakan platform data kode rendah untuk menyimpan data aplikasi.

- **Power Automate**, untuk aliran Pemrosesan Faktur di mana Anda akan memiliki lingkungan pengembangan kode rendah untuk membangun alur kerja untuk mengotomatisasi proses Pemrosesan Faktur.

- **AI Builder**, untuk Model AI Pemrosesan Faktur di mana Anda akan menggunakan Model AI yang sudah dibangun untuk memproses faktur untuk startup kita.

## AI Generatif di Power Platform

Meningkatkan pengembangan dan aplikasi kode rendah dengan AI generatif adalah fokus utama untuk Power Platform. Tujuannya adalah untuk memungkinkan semua orang membangun aplikasi, situs, dasbor yang didukung AI dan mengotomatisasi proses dengan AI, _tanpa memerlukan keahlian ilmu data_. Tujuan ini dicapai dengan mengintegrasikan AI generatif ke dalam pengalaman pengembangan kode rendah di Power Platform dalam bentuk Copilot dan AI Builder.

### Bagaimana cara kerjanya?

Copilot adalah asisten AI yang memungkinkan Anda membangun solusi Power Platform dengan mendeskripsikan kebutuhan Anda dalam serangkaian langkah percakapan menggunakan bahasa alami. Anda dapat, misalnya, menginstruksikan asisten AI Anda untuk menyatakan bidang apa yang akan digunakan aplikasi Anda dan itu akan membuat baik aplikasi maupun model data dasar atau Anda dapat menentukan bagaimana mengatur aliran di Power Automate.

Anda dapat menggunakan fungsi yang didorong oleh Copilot sebagai fitur di layar aplikasi Anda untuk memungkinkan pengguna mengungkapkan wawasan melalui interaksi percakapan.

AI Builder adalah kemampuan AI kode rendah yang tersedia di Power Platform yang memungkinkan Anda menggunakan Model AI untuk membantu Anda mengotomatisasi proses dan memprediksi hasil. Dengan AI Builder Anda dapat membawa AI ke aplikasi dan aliran yang terhubung ke data Anda di Dataverse atau di berbagai sumber data cloud, seperti SharePoint, OneDrive, atau Azure.

Copilot tersedia di semua produk Power Platform: Power Apps, Power Automate, Power BI, Power Pages, dan Power Virtual Agents. AI Builder tersedia di Power Apps dan Power Automate. Dalam pelajaran ini, kita akan fokus pada bagaimana menggunakan Copilot dan AI Builder di Power Apps dan Power Automate untuk membangun solusi untuk startup pendidikan kita.

### Copilot di Power Apps

Sebagai bagian dari Power Platform, Power Apps menyediakan lingkungan pengembangan kode rendah untuk membangun aplikasi untuk melacak, mengelola, dan berinteraksi dengan data. Ini adalah rangkaian layanan pengembangan aplikasi dengan platform data yang dapat diskalakan dan kemampuan untuk terhubung ke layanan cloud dan data lokal. Power Apps memungkinkan Anda membangun aplikasi yang berjalan di browser, tablet, dan ponsel, dan dapat dibagikan dengan rekan kerja. Power Apps memudahkan pengguna dalam pengembangan aplikasi dengan antarmuka sederhana, sehingga setiap pengguna bisnis atau pengembang profesional dapat membangun aplikasi kustom. Pengalaman pengembangan aplikasi juga ditingkatkan dengan AI Generatif melalui Copilot.

Fitur asisten AI copilot di Power Apps memungkinkan Anda mendeskripsikan jenis aplikasi yang Anda butuhkan dan informasi apa yang Anda inginkan aplikasi Anda untuk melacak, mengumpulkan, atau menunjukkan. Copilot kemudian menghasilkan aplikasi Kanvas responsif berdasarkan deskripsi Anda. Anda kemudian dapat menyesuaikan aplikasi untuk memenuhi kebutuhan Anda. AI Copilot juga menghasilkan dan menyarankan Tabel Dataverse dengan bidang yang Anda butuhkan untuk menyimpan data yang ingin Anda lacak dan beberapa data contoh. Kita akan melihat apa itu Dataverse dan bagaimana Anda dapat menggunakannya di Power Apps dalam pelajaran ini nanti. Anda kemudian dapat menyesuaikan tabel untuk memenuhi kebutuhan Anda menggunakan fitur asisten AI Copilot melalui langkah percakapan. Fitur ini tersedia langsung dari layar utama Power Apps.

### Copilot di Power Automate

Sebagai bagian dari Power Platform, Power Automate memungkinkan pengguna membuat alur kerja otomatis antara aplikasi dan layanan. Ini membantu mengotomatisasi proses bisnis berulang seperti komunikasi, pengumpulan data, dan persetujuan keputusan. Antarmuka sederhana memungkinkan pengguna dengan setiap kompetensi teknis (dari pemula hingga pengembang berpengalaman) untuk mengotomatisasi tugas kerja. Pengalaman pengembangan alur kerja juga ditingkatkan dengan AI Generatif melalui Copilot.

Fitur asisten AI copilot di Power Automate memungkinkan Anda mendeskripsikan jenis aliran yang Anda butuhkan dan tindakan apa yang Anda inginkan aliran Anda untuk dilakukan. Copilot kemudian menghasilkan aliran berdasarkan deskripsi Anda. Anda kemudian dapat menyesuaikan aliran untuk memenuhi kebutuhan Anda. AI Copilot juga menghasilkan dan menyarankan tindakan yang Anda butuhkan untuk melakukan tugas yang ingin Anda otomatisasi. Kita akan melihat apa itu aliran dan bagaimana Anda dapat menggunakannya di Power Automate dalam pelajaran ini nanti. Anda kemudian dapat menyesuaikan tindakan untuk memenuhi kebutuhan Anda menggunakan fitur asisten AI Copilot melalui langkah percakapan. Fitur ini tersedia langsung dari layar utama Power Automate.

## Tugas: Mengelola tugas siswa dan faktur untuk startup kita, menggunakan Copilot

Startup kita menyediakan kursus online kepada siswa. Startup ini telah berkembang pesat dan sekarang kesulitan untuk memenuhi permintaan kursusnya. Startup telah mempekerjakan Anda sebagai pengembang Power Platform untuk membantu mereka membangun solusi kode rendah untuk membantu mereka mengelola tugas siswa dan faktur. Solusi mereka harus dapat membantu mereka melacak dan mengelola tugas siswa melalui aplikasi dan mengotomatisasi proses pemrosesan faktur melalui alur kerja. Anda telah diminta untuk menggunakan AI Generatif untuk mengembangkan solusi tersebut.

Saat Anda mulai menggunakan Copilot, Anda dapat menggunakan [Perpustakaan Prompt Copilot Power Platform](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) untuk memulai dengan prompt. Perpustakaan ini berisi daftar prompt yang dapat Anda gunakan untuk membangun aplikasi dan aliran dengan Copilot. Anda juga dapat menggunakan prompt dalam perpustakaan untuk mendapatkan ide tentang bagaimana mendeskripsikan kebutuhan Anda kepada Copilot.

### Membangun Aplikasi Pelacak Tugas Siswa untuk Startup Kita

Para pendidik di startup kita telah kesulitan melacak tugas siswa. Mereka telah menggunakan spreadsheet untuk melacak tugas tetapi ini menjadi sulit dikelola seiring dengan meningkatnya jumlah siswa. Mereka telah meminta Anda untuk membangun aplikasi yang akan membantu mereka melacak dan mengelola tugas siswa. Aplikasi ini harus memungkinkan mereka menambahkan tugas baru, melihat tugas, memperbarui tugas, dan menghapus tugas. Aplikasi ini juga harus memungkinkan pendidik dan siswa melihat tugas yang telah dinilai dan yang belum dinilai.

Anda akan membangun aplikasi menggunakan Copilot di Power Apps dengan mengikuti langkah-langkah di bawah ini:

1. Navigasikan ke layar utama [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

1. Gunakan area teks di layar utama untuk mendeskripsikan aplikasi yang ingin Anda bangun. Misalnya, **_Saya ingin membangun aplikasi untuk melacak dan mengelola tugas siswa_**. Klik tombol **Kirim** untuk mengirim prompt ke AI Copilot.

![Deskripsikan aplikasi yang ingin Anda bangun](../../../translated_images/copilot-chat-prompt-powerapps.8b18beb535e7bd1a26be1284c2ef1246dbadb4704fa1656f1b6b35214ddc1c89.id.png)

1. AI Copilot akan menyarankan Tabel Dataverse dengan bidang yang Anda butuhkan untuk menyimpan data yang ingin Anda lacak dan beberapa data contoh. Anda kemudian dapat menyesuaikan tabel untuk memenuhi kebutuhan Anda menggunakan fitur asisten AI Copilot melalui langkah percakapan.

   > **Penting**: Dataverse adalah platform data dasar untuk Power Platform. Ini adalah platform data kode rendah untuk menyimpan data aplikasi. Ini adalah layanan yang dikelola sepenuhnya yang menyimpan data dengan aman di Cloud Microsoft dan disediakan dalam lingkungan Power Platform Anda. Ini dilengkapi dengan kemampuan tata kelola data bawaan, seperti klasifikasi data, silsilah data, kontrol akses yang sangat detail, dan banyak lagi. Anda dapat mempelajari lebih lanjut tentang Dataverse [di sini](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Bidang yang disarankan dalam tabel baru Anda](../../../translated_images/copilot-dataverse-table-powerapps.35038be17c72f49f510a76a208db3c2c8b3c0928f08620694dca255b103f2929.id.png)

1. Para pendidik ingin mengirim email kepada siswa yang telah mengirimkan tugas mereka untuk memberi mereka informasi terbaru tentang kemajuan tugas mereka. Anda dapat menggunakan Copilot untuk menambahkan bidang baru ke tabel untuk menyimpan email siswa. Misalnya, Anda dapat menggunakan prompt berikut untuk menambahkan bidang baru ke tabel: **_Saya ingin menambahkan kolom untuk menyimpan email siswa_**. Klik tombol **Kirim** untuk mengirim prompt ke AI Copilot.

![Menambahkan bidang baru](../../../translated_images/copilot-new-column.48af3bb080c13599fb73ee32cc18101dc0cf61992d0dfe15b8bc4aa75a6c6a34.id.png)

1. AI Copilot akan menghasilkan bidang baru dan Anda kemudian dapat menyesuaikan bidang tersebut untuk memenuhi kebutuhan Anda.

1. Setelah Anda selesai dengan tabel, klik tombol **Buat aplikasi** untuk membuat aplikasi.

1. AI Copilot akan menghasilkan aplikasi Kanvas responsif berdasarkan deskripsi Anda. Anda kemudian dapat menyesuaikan aplikasi untuk memenuhi kebutuhan Anda.

1. Untuk pendidik mengirim email kepada siswa, Anda dapat menggunakan Copilot untuk menambahkan layar baru ke aplikasi. Misalnya, Anda dapat menggunakan prompt berikut untuk menambahkan layar baru ke aplikasi: **_Saya ingin menambahkan layar untuk mengirim email kepada siswa_**. Klik tombol **Kirim** untuk mengirim prompt ke AI Copilot.

![Menambahkan layar baru melalui instruksi prompt](../../../translated_images/copilot-new-screen.30341e89604440b4c91eb55d258276fd6e283bfab376c57501f0b3caeaaf2fda.id.png)

1. AI Copilot akan menghasilkan layar baru dan Anda kemudian dapat menyesuaikan layar tersebut untuk memenuhi kebutuhan Anda.

1. Setelah Anda selesai dengan aplikasi, klik tombol **Simpan** untuk menyimpan aplikasi.

1. Untuk berbagi aplikasi dengan pendidik, klik tombol **Bagikan** dan kemudian klik tombol **Bagikan** lagi. Anda kemudian dapat berbagi aplikasi dengan pendidik dengan memasukkan alamat email mereka.

> **Pekerjaan rumah Anda**: Aplikasi yang baru saja Anda buat adalah awal yang baik tetapi dapat ditingkatkan. Dengan fitur email, pendidik hanya dapat mengirim email kepada siswa secara manual dengan harus mengetik email mereka. Bisakah Anda menggunakan Copilot untuk membangun otomatisasi yang akan memungkinkan pendidik mengirim email kepada siswa secara otomatis ketika mereka mengirimkan tugas mereka? Petunjuk Anda adalah dengan prompt yang tepat Anda dapat menggunakan Copilot di Power Automate untuk membangun ini.

### Membangun Tabel Informasi Faktur untuk Startup Kita

Tim keuangan dari startup kita telah kesulitan melacak faktur. Mereka telah menggunakan spreadsheet untuk melacak faktur tetapi ini menjadi sulit dikelola seiring dengan meningkatnya jumlah faktur. Mereka telah meminta Anda untuk membangun tabel yang akan membantu mereka menyimpan, melacak, dan mengelola informasi faktur yang mereka terima. Tabel tersebut harus digunakan untuk membangun otomatisasi yang akan mengekstraksi semua informasi faktur dan menyimpannya di tabel. Tabel tersebut juga harus memungkinkan tim keuangan untuk melihat faktur yang telah dibayar dan yang belum dibayar.

Power Platform memiliki platform data dasar yang disebut Dataverse yang memungkinkan Anda menyimpan data untuk aplikasi dan solusi Anda. Dataverse menyediakan platform data kode rendah untuk menyimpan data aplikasi. Ini adalah layanan yang dikelola sepenuhnya yang menyimpan data dengan aman di Cloud Microsoft dan disediakan dalam lingkungan Power Platform Anda. Ini dilengkapi dengan kemampuan tata kelola data bawaan, seperti klasifikasi data, silsilah data, kontrol akses yang sangat detail, dan banyak lagi. Anda dapat mempelajari lebih lanjut [tentang Dataverse di sini](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Mengapa kita harus menggunakan Dataverse untuk startup kita? Tabel standar dan kustom dalam Dataverse menyediakan opsi penyimpanan yang aman dan berbasis cloud untuk data Anda. Tabel memungkinkan Anda menyimpan berbagai jenis data, mirip dengan bagaimana Anda mungkin menggunakan beberapa lembar kerja dalam satu buku kerja Excel. Anda dapat menggunakan tabel untuk menyimpan data yang spesifik untuk organisasi atau kebutuhan bisnis Anda. Beberapa manfaat yang akan didapatkan startup kita dari menggunakan Dataverse termasuk tetapi tidak terbatas pada:

- **Mudah dikelola**: Baik metadata maupun data disimpan di cloud, sehingga Anda tidak perlu khawatir tentang detail bagaimana mereka disimpan atau dikelola. Anda dapat fokus pada pembangunan aplikasi dan solusi Anda.

- **Aman**: Dataverse menyediakan opsi penyimpanan yang aman dan berbasis cloud untuk data Anda. Anda dapat mengontrol siapa yang memiliki akses ke data dalam tabel Anda dan bagaimana mereka dapat mengaksesnya menggunakan keamanan berbasis peran.

- **Metadata yang kaya**: Jenis data dan hubungan digunakan langsung dalam Power Apps

- **Logika dan validasi**: Anda dapat menggunakan aturan bisnis, bidang terhitung, dan aturan validasi untuk menegakkan logika bisnis dan menjaga keakuratan data.

Sekarang setelah Anda tahu apa itu Dataverse dan mengapa Anda harus menggunakannya, mari kita lihat bagaimana Anda dapat menggunakan Copilot untuk membuat tabel dalam Dataverse untuk memenuhi kebutuhan tim keuangan kita.

> **Catatan** : Anda akan menggunakan tabel ini di bagian berikutnya untuk membangun otomatisasi yang akan mengekstraksi semua informasi faktur dan menyimpannya di tabel. Untuk membuat tabel dalam Dataverse menggunakan Copilot, ikuti langkah-langkah di bawah ini: 1. Navigasikan ke layar utama [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst). 2. Pada bilah navigasi kiri, pilih **Tabel** dan kemudian klik **Deskripsikan Tabel baru**. ![Pilih tabel baru](../../../translated_images/describe-new-table.545cd3568f4bee6aded8021cc0653013ff982f4ccdc628b4800d1f0be5ddff9b.id.png) 1. Pada layar **Deskripsikan Tabel baru**, gunakan area teks untuk mendeskripsikan tabel yang ingin Anda buat. Misalnya, **_Saya ingin membuat tabel untuk menyimpan informasi faktur_**. Klik tombol **Kirim** untuk mengirim prompt ke AI Copilot. ![Deskripsikan tabel](../../../translated_images/copilot-chat-prompt-dataverse.22a6bc42a8fef6bf55b4a0fe2c5570b0991db3b72d4e832973008caa7f5902ed.id.png) 1. AI Copilot akan menyarankan Tabel Dataverse dengan bidang yang Anda butuhkan untuk menyimpan data yang ingin Anda lacak dan beberapa data contoh. Anda kemudian dapat menyesuaikan tabel untuk memenuhi kebutuhan Anda menggunakan fitur asisten AI Copilot melalui langkah percakapan. ![Tabel Dataverse yang disarankan](../../../translated_images/copilot-dataverse-table.c5f880524e2972b0af9112ce0d52624b8d8cc78ab992921f0e60c7edd393217a.id.png) 1. Tim keuangan ingin mengirim email kepada pemasok untuk memberi mereka informasi terbaru tentang status faktur mereka saat ini. Anda dapat menggunakan Copilot untuk menambahkan bidang baru ke tabel untuk menyimpan email pemasok. Misalnya, Anda dapat menggunakan prompt berikut untuk menambahkan bidang baru ke tabel: **_Saya ingin menambahkan kolom untuk menyimpan email pemasok_**. Klik tombol **Kirim** untuk mengirim prompt ke AI Copilot. 1. AI Copilot akan menghasilkan bidang baru dan Anda kemudian dapat menyesuaikan bidang tersebut untuk memenuhi kebutuhan Anda. 1. Setelah Anda selesai dengan tabel, klik tombol **Buat** untuk membuat tabel. ## Model AI di Power Platform dengan AI Builder AI Builder adalah kemampuan AI kode rendah yang tersedia di Power Platform yang memungkinkan Anda menggunakan Model AI untuk membantu Anda mengotomatisasi proses dan memprediksi hasil. Dengan AI Builder Anda dapat membawa AI ke aplikasi dan aliran yang terhubung ke data Anda di Dataverse atau di berbagai sumber data cloud, seperti SharePoint, OneDrive, atau Azure. ## Model AI yang Sudah Dibangun vs Model AI Kustom AI Builder menyediakan dua jenis Model AI: Model AI yang Sudah Dibangun dan Model AI Kustom. Model AI yang Sudah Dibangun adalah Model AI siap pakai yang dilatih oleh Microsoft dan tersedia di Power Platform. Ini membantu Anda menambahkan kecerdasan ke aplikasi dan aliran Anda tanpa harus mengumpulkan data dan kemudian membangun, melatih, dan menerbitkan model Anda sendiri. Anda dapat menggunakan model ini untuk mengotomatisasi proses dan memprediksi hasil. Beberapa Model AI yang Sudah Dibangun yang tersedia di Power Platform termasuk: - **Ekstraksi Frasa Kunci**: Model ini mengekstraksi frasa kunci dari teks. - **Deteksi Bahasa**: Model ini mendeteksi bahasa dari
- **Analisis Sentimen**: Model ini mendeteksi sentimen positif, negatif, netral, atau campuran dalam teks.
- **Pembaca Kartu Nama**: Model ini mengekstrak informasi dari kartu nama.
- **Pengenalan Teks**: Model ini mengekstrak teks dari gambar.
- **Deteksi Objek**: Model ini mendeteksi dan mengekstrak objek dari gambar.
- **Pemrosesan Dokumen**: Model ini mengekstrak informasi dari formulir.
- **Pemrosesan Faktur**: Model ini mengekstrak informasi dari faktur.

Dengan Model AI Kustom, Anda dapat membawa model Anda sendiri ke AI Builder sehingga dapat berfungsi seperti model kustom AI Builder lainnya, memungkinkan Anda melatih model menggunakan data Anda sendiri. Anda dapat menggunakan model ini untuk mengotomatisasi proses dan memprediksi hasil baik di Power Apps maupun Power Automate. Saat menggunakan model Anda sendiri, ada batasan yang berlaku. Baca lebih lanjut tentang [batasan](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst) ini.

## Tugas #2 - Membangun Alur Pemrosesan Faktur untuk Startup Kita

Tim keuangan telah mengalami kesulitan memproses faktur. Mereka telah menggunakan spreadsheet untuk melacak faktur tetapi ini menjadi sulit untuk dikelola karena jumlah faktur meningkat. Mereka meminta Anda untuk membangun alur kerja yang akan membantu mereka memproses faktur menggunakan AI. Alur kerja harus memungkinkan mereka mengekstrak informasi dari faktur dan menyimpan informasi tersebut dalam tabel Dataverse. Alur kerja juga harus memungkinkan mereka mengirim email ke tim keuangan dengan informasi yang diekstrak.

Sekarang Anda tahu apa itu AI Builder dan mengapa Anda harus menggunakannya, mari kita lihat bagaimana Anda dapat menggunakan Model AI Pemrosesan Faktur di AI Builder, yang telah kita bahas sebelumnya, untuk membangun alur kerja yang akan membantu tim keuangan memproses faktur. Untuk membangun alur kerja yang akan membantu tim keuangan memproses faktur menggunakan Model AI Pemrosesan Faktur di AI Builder, ikuti langkah-langkah berikut:

1. Navigasikan ke layar utama [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst).
2. Gunakan area teks di layar utama untuk menjelaskan alur kerja yang ingin Anda bangun. Misalnya, **_Proses faktur ketika tiba di kotak masuk saya_**. Klik tombol **Kirim** untuk mengirimkan prompt ke AI Copilot.
3. AI Copilot akan menyarankan tindakan yang perlu Anda lakukan untuk mengotomatisasi tugas yang Anda inginkan. Anda dapat mengklik tombol **Berikutnya** untuk melanjutkan ke langkah berikutnya.
4. Pada langkah berikutnya, Power Automate akan meminta Anda untuk mengatur koneksi yang diperlukan untuk alur. Setelah selesai, klik tombol **Buat alur** untuk membuat alur.
5. AI Copilot akan menghasilkan alur dan Anda kemudian dapat menyesuaikan alur agar sesuai dengan kebutuhan Anda.
6. Perbarui pemicu alur dan atur **Folder** ke folder tempat faktur akan disimpan. Misalnya, Anda dapat mengatur folder ke **Kotak Masuk**. Klik **Tampilkan opsi lanjutan** dan atur **Hanya dengan Lampiran** ke **Ya**. Ini akan memastikan bahwa alur hanya berjalan ketika email dengan lampiran diterima di folder tersebut.
7. Hapus tindakan berikut dari alur: **HTML ke teks**, **Compose**, **Compose 2**, **Compose 3** dan **Compose 4** karena Anda tidak akan menggunakannya.
8. Hapus tindakan **Condition** dari alur karena Anda tidak akan menggunakannya. Seharusnya terlihat seperti tangkapan layar berikut:
9. Klik tombol **Tambahkan tindakan** dan cari **Dataverse**. Pilih tindakan **Tambahkan baris baru**.
10. Pada tindakan **Ekstrak Informasi dari faktur**, perbarui **File Faktur** untuk menunjuk ke **Konten Lampiran** dari email. Ini akan memastikan bahwa alur mengekstrak informasi dari lampiran faktur.
11. Pilih **Tabel** yang Anda buat sebelumnya. Misalnya, Anda dapat memilih tabel **Informasi Faktur**. Pilih konten dinamis dari tindakan sebelumnya untuk mengisi bidang berikut:
   - ID
   - Jumlah
   - Tanggal
   - Nama
   - Status
   - Atur **Status** ke **Menunggu**.
   - Email Pemasok
   - Gunakan konten dinamis **Dari** dari pemicu **Ketika email baru tiba**.
12. Setelah selesai dengan alur, klik tombol **Simpan** untuk menyimpan alur. Anda kemudian dapat menguji alur dengan mengirim email dengan faktur ke folder yang Anda tentukan dalam pemicu.

> **Pekerjaan rumah Anda**: Alur yang baru saja Anda buat adalah awal yang baik, sekarang Anda perlu memikirkan bagaimana Anda dapat membangun otomatisasi yang akan memungkinkan tim keuangan kita mengirim email ke pemasok untuk memperbarui mereka dengan status terkini dari faktur mereka. Petunjuk Anda: alur harus berjalan ketika status faktur berubah.

## Menggunakan Model AI Generasi Teks di Power Automate

Model AI Buat Teks dengan GPT di AI Builder memungkinkan Anda menghasilkan teks berdasarkan prompt dan didukung oleh Microsoft Azure OpenAI Service. Dengan kemampuan ini, Anda dapat mengintegrasikan teknologi GPT (Generative Pre-Trained Transformer) ke dalam aplikasi dan alur kerja Anda untuk membangun berbagai alur otomatis dan aplikasi yang informatif.

Model GPT menjalani pelatihan ekstensif pada sejumlah besar data, memungkinkan mereka menghasilkan teks yang mirip dengan bahasa manusia ketika diberikan prompt. Ketika diintegrasikan dengan otomatisasi alur kerja, model AI seperti GPT dapat dimanfaatkan untuk menyederhanakan dan mengotomatisasi berbagai tugas.

Misalnya, Anda dapat membangun alur untuk secara otomatis menghasilkan teks untuk berbagai kasus penggunaan, seperti: draf email, deskripsi produk, dan lainnya. Anda juga dapat menggunakan model untuk menghasilkan teks untuk berbagai aplikasi, seperti chatbot dan aplikasi layanan pelanggan yang memungkinkan agen layanan pelanggan merespons dengan efektif dan efisien terhadap pertanyaan pelanggan.

Untuk mempelajari cara menggunakan Model AI ini di Power Automate, lihat modul [Tambahkan kecerdasan dengan AI Builder dan GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Kerja Bagus! Lanjutkan Pembelajaran Anda

Setelah menyelesaikan pelajaran ini, lihat [koleksi Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif Anda!

Beralihlah ke Pelajaran 11 di mana kita akan melihat bagaimana [mengintegrasikan AI Generatif dengan Pemanggilan Fungsi](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap disadari bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi penting, disarankan menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.