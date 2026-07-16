# Membina Aplikasi AI Kod Rendah

[![Membina Aplikasi AI Kod Rendah](../../../translated_images/ms/10-lesson-banner.a01ac8fe3fd86310.webp)](https://youtu.be/1vzq3Nd8GBA?si=h6LHWJXdmqf6mhDg)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

## Pengenalan

Sekarang bahawa kita telah belajar bagaimana membina aplikasi penjanaan imej, mari kita berbincang tentang kod rendah. AI generatif boleh digunakan untuk pelbagai bidang termasuk kod rendah, tetapi apa itu kod rendah dan bagaimana kita boleh menambah AI kepadanya?

Membina aplikasi dan penyelesaian telah menjadi lebih mudah bagi pembangun tradisional dan bukan pembangun melalui penggunaan Platform Pembangunan Kod Rendah. Platform Pembangunan Kod Rendah membolehkan anda membina aplikasi dan penyelesaian dengan sedikit atau tanpa kod. Ini dicapai dengan menyediakan persekitaran pembangunan visual yang membolehkan anda seret dan lepas komponen untuk membina aplikasi dan penyelesaian. Ini membolehkan anda membina aplikasi dan penyelesaian dengan lebih cepat dan menggunakan sumber yang lebih sedikit. Dalam pelajaran ini, kita menyelami bagaimana menggunakan Kod Rendah dan bagaimana meningkatkan pembangunan kod rendah dengan AI menggunakan Power Platform.

Power Platform menyediakan organisasi peluang untuk memperkasakan pasukan mereka untuk membina penyelesaian mereka sendiri melalui persekitaran kod rendah atau tiada kod yang intuitif. Persekitaran ini membantu mempermudah proses membina penyelesaian. Dengan Power Platform, penyelesaian boleh dibina dalam beberapa hari atau minggu dan bukannya bulan atau tahun. Power Platform terdiri daripada lima produk utama: Power Apps, Power Automate, Power BI, Power Pages dan Copilot Studio.

Pelajaran ini merangkumi:

- Pengenalan kepada AI Generatif dalam Power Platform
- Pengenalan kepada Copilot dan cara menggunakannya
- Menggunakan AI Generatif untuk membina aplikasi dan aliran dalam Power Platform
- Memahami Model AI dalam Power Platform dengan AI Builder
- Membina ejen pintar dengan Microsoft Copilot Studio

## Objektif Pembelajaran

Pada akhir pelajaran ini, anda akan dapat:

- Memahami bagaimana Copilot berfungsi dalam Power Platform.

- Membina Aplikasi Penjejak Tugasan Pelajar untuk startup pendidikan kami.

- Membina Aliran Pemprosesan Invois yang menggunakan AI untuk mengekstrak maklumat daripada invois.

- Mengamalkan amalan terbaik apabila menggunakan Model AI Buat Teks dengan GPT.

- Memahami apa itu Microsoft Copilot Studio dan bagaimana membina ejen pintar dengannya.

Alat dan teknologi yang akan anda gunakan dalam pelajaran ini adalah:

- **Power Apps**, untuk aplikasi Penjejak Tugasan Pelajar, yang menyediakan persekitaran pembangunan kod rendah untuk membina aplikasi bagi menjejak, mengurus dan berinteraksi dengan data.

- **Dataverse**, untuk menyimpan data bagi aplikasi Penjejak Tugasan Pelajar di mana Dataverse akan menyediakan platform data kod rendah untuk menyimpan data aplikasi tersebut.

- **Power Automate**, untuk aliran Pemprosesan Invois di mana anda akan mempunyai persekitaran pembangunan kod rendah untuk membina aliran kerja bagi mengautomasikan proses Pemprosesan Invois.

- **AI Builder**, untuk Model AI Pemprosesan Invois di mana anda akan menggunakan Model AI sedia ada untuk memproses invois bagi startup kami.

## AI Generatif dalam Power Platform

Meningkatkan pembangunan kod rendah dan aplikasi dengan AI generatif adalah bidang fokus utama untuk Power Platform. Matlamatnya adalah untuk membolehkan semua orang membina aplikasi yang dikuasakan AI, laman web, papan pemuka dan mengautomasikan proses dengan AI, _tanpa memerlukan kepakaran sains data_. Matlamat ini dicapai dengan mengintegrasikan AI generatif ke dalam pengalaman pembangunan kod rendah dalam Power Platform dalam bentuk Copilot dan AI Builder.

### Bagaimana ia berfungsi?

Copilot adalah pembantu AI yang membolehkan anda membina penyelesaian Power Platform dengan menerangkan keperluan anda dalam siri langkah perbualan menggunakan bahasa semula jadi. Sebagai contoh, anda boleh mengarahkan pembantu AI anda untuk menyatakan medan apa yang akan digunakan aplikasi anda dan ia akan mencipta aplikasi serta model data asas atau anda boleh menentukan bagaimana untuk menyediakan aliran dalam Power Automate.

Anda boleh menggunakan fungsi yang digerakkan oleh Copilot sebagai ciri dalam skrin aplikasi anda untuk membolehkan pengguna menemui pandangan melalui interaksi perbualan.

AI Builder adalah keupayaan AI kod rendah yang tersedia dalam Power Platform yang membolehkan anda menggunakan Model AI untuk membantu mengautomasikan proses dan meramalkan hasil. Dengan AI Builder anda boleh membawa AI ke dalam aplikasi dan aliran anda yang bersambung ke data anda dalam Dataverse atau pelbagai sumber data awan, seperti SharePoint, OneDrive atau Azure.

Copilot tersedia dalam semua produk Power Platform: Power Apps, Power Automate, Power BI, Power Pages dan Copilot Studio (dahulu Power Virtual Agents). AI Builder tersedia dalam Power Apps dan Power Automate. Dalam pelajaran ini, kita akan fokus pada cara menggunakan Copilot dan AI Builder dalam Power Apps dan Power Automate untuk membina penyelesaian bagi startup pendidikan kami.

### Copilot dalam Power Apps

Sebagai sebahagian daripada Power Platform, Power Apps menyediakan persekitaran pembangunan kod rendah untuk membina aplikasi bagi menjejak, mengurus dan berinteraksi dengan data. Ia adalah suite perkhidmatan pembangunan aplikasi dengan platform data boleh skala dan kemampuan untuk menyambung ke perkhidmatan awan dan data tempatan. Power Apps membolehkan anda membina aplikasi yang boleh dijalankan di pelayar, tablet dan telefon, dan boleh dikongsi dengan rakan sekerja. Power Apps memudahkan pengguna memasuki pembangunan aplikasi dengan antara muka yang mudah, supaya setiap pengguna perniagaan atau pembangun profesional boleh membina aplikasi tersuai. Pengalaman pembangunan aplikasi juga dipertingkatkan dengan AI Generatif melalui Copilot.

Ciri pembantu AI Copilot dalam Power Apps membolehkan anda menerangkan jenis aplikasi yang anda perlukan dan maklumat apa yang anda ingin aplikasi anda jejak, kumpul, atau tunjukkan. Copilot kemudian menjana aplikasi Canvas responsif berdasarkan penerangan anda. Anda boleh mengubah suai aplikasi tersebut untuk memenuhi keperluan anda. AI Copilot juga menjana dan mencadangkan Jadual Dataverse dengan medan yang anda perlukan untuk menyimpan data yang anda ingin jejak dan beberapa data contoh. Kita akan lihat apa itu Dataverse dan bagaimana anda boleh menggunakannya dalam Power Apps dalam pelajaran ini nanti. Anda kemudian boleh mengubah suai jadual tersebut untuk memenuhi keperluan anda menggunakan ciri pembantu AI Copilot melalui langkah perbualan. Ciri ini tersedia secara mudah dari skrin utama Power Apps.

### Copilot dalam Power Automate

Sebagai sebahagian daripada Power Platform, Power Automate membolehkan pengguna mencipta aliran kerja automatik antara aplikasi dan perkhidmatan. Ia membantu mengautomasikan proses perniagaan berulang seperti komunikasi, pengumpulan data, dan kelulusan keputusan. Antara muka yang mudah membolehkan pengguna dari semua tahap teknikal (dari pemula hingga pembangun berpengalaman) mengautomasikan tugas kerja. Pengalaman pembangunan aliran kerja juga dipertingkatkan dengan AI Generatif melalui Copilot.

Ciri pembantu AI Copilot dalam Power Automate membolehkan anda menerangkan jenis aliran yang anda perlukan dan tindakan apa yang anda mahu aliran anda lakukan. Copilot kemudian menjana aliran berdasarkan penerangan anda. Anda boleh mengubah suai aliran tersebut untuk memenuhi keperluan anda. AI Copilot juga menjana dan mencadangkan tindakan yang anda perlu lakukan untuk tugasan yang anda mahu automatikkan. Kita akan lihat apa itu aliran dan bagaimana anda boleh menggunakannya dalam Power Automate dalam pelajaran ini nanti. Anda kemudian boleh mengubah suai tindakan tersebut untuk memenuhi keperluan anda menggunakan ciri pembantu AI Copilot melalui langkah perbualan. Ciri ini tersedia secara mudah dari skrin utama Power Automate.

## Membina Ejen Pintar dengan Microsoft Copilot Studio

[Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio?WT.mc_id=academic-105485-koreyst) (dahulu Power Virtual Agents) adalah ahli kod rendah dalam Power Platform untuk membina **ejen AI** — copilots perbualan yang boleh menjawab soalan, melakukan tindakan, dan mengautomasikan tugasan bagi pihak pengguna anda. Sama seperti selebihnya Power Platform, anda membina ejen ini dalam pengalaman visual yang berfokuskan bahasa semula jadi: anda menerangkan apa yang anda mahu ejen lakukan, dan Copilot Studio membantu merangka arahan, pengetahuan, dan tindakan ejen tersebut.

Untuk startup pendidikan kami, anda boleh membina ejen yang menjawab soalan pelajar tentang kursus, memeriksa tarikh akhir tugasan, dan malah menghantar emel kepada pengajar — semua ini tanpa menulis kod.

Berikut adalah beberapa kapasiti terkini yang menjadikan Copilot Studio berkuasa:

- **Jawapan generatif daripada pengetahuan anda**. Daripada menulis setiap perbualan secara manual, anda boleh menyambungkan **sumber pengetahuan** — laman web awam, SharePoint, OneDrive, Dataverse, fail yang dimuat naik, atau data perusahaan melalui penyambung — dan ejen menjana jawapan berasaskan sumber tersebut.

- **Orkestra generatif**. Daripada bergantung pada frasa pencetus yang kaku, ejen menggunakan AI untuk memahami permintaan dan secara dinamik memutuskan pengetahuan, topik, dan tindakan mana yang digabungkan untuk memenuhinya, termasuk merangkai beberapa langkah bersama.

- **Tindakan dan penyambung**. Ejen boleh *melakukan* perkara, bukan sekadar bersembang. Anda boleh memberikan tindakan kepada ejen yang disokong oleh lebih 1,500 penyambung Power Platform yang sudah dibina, aliran Power Automate, REST API tersuai, arahan, atau **Model Context Protocol (MCP)** pelayan.

- **Ejen autonomi**. Ejen tidak terhad untuk bertindak balas dalam tetingkap sembang sahaja. Anda boleh membina **ejen autonomi** yang dicetuskan oleh peristiwa — seperti emel baru, rekod baru dalam Dataverse, atau fail yang dimuat naik — dan kemudian bertindak di latar belakang untuk menyelesaikan tugasan.

- **Orkestra multi-ejen**. Ejen boleh memanggil ejen lain. Ejen Copilot Studio boleh menyerahkan kepada, atau diperluaskan oleh, ejen lain, termasuk ejen yang diterbitkan ke Microsoft 365 Copilot dan ejen dibina dalam Microsoft Foundry.

- **Pilihan model**. Selain model terbina dalam, anda boleh membawa model dari katalog model Microsoft Foundry untuk menyesuaikan cara ejen anda berfikir dan bertindak balas.

- **Terbitkan di mana-mana**. Setelah dibina, ejen boleh diterbitkan ke pelbagai saluran — Microsoft Teams, Microsoft 365 Copilot, laman web atau aplikasi tersuai, dan banyak lagi — dengan keselamatan, pengesahan, dan analitik diurus melalui pengalaman pentadbir Power Platform.

Anda boleh mula membina ejen pertama anda di [copilotstudio.microsoft.com](https://copilotstudio.microsoft.com?WT.mc_id=academic-105485-koreyst) dan belajar lebih lanjut dalam [dokumentasi Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/?WT.mc_id=academic-105485-koreyst).

## Tugasan: Urus tugasan pelajar dan invois untuk startup kami, menggunakan Copilot

Startup kami menyediakan kursus dalam talian kepada pelajar. Startup ini telah berkembang dengan pesat dan kini menghadapi kesukaran untuk memenuhi permintaan kursusnya. Startup ini telah mengupah anda sebagai pembangun Power Platform untuk membantu mereka membina penyelesaian kod rendah untuk membantu mereka mengurus tugasan pelajar dan invois mereka. Penyelesaian mereka harus dapat membantu mereka menjejak dan mengurus tugasan pelajar melalui aplikasi dan mengautomasikan proses pemprosesan invois melalui aliran kerja. Anda telah diminta untuk menggunakan AI Generatif untuk membangunkan penyelesaian tersebut.

Apabila anda memulakan penggunaan Copilot, anda boleh menggunakan [Perpustakaan Prompt Power Platform Copilot](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) untuk mula menggunakan prompt. Perpustakaan ini mengandungi senarai prompt yang anda boleh gunakan untuk membina aplikasi dan aliran dengan Copilot. Anda juga boleh menggunakan prompt dalam perpustakaan untuk mendapatkan idea tentang bagaimana menerangkan keperluan anda kepada Copilot.

### Membina Aplikasi Penjejak Tugasan Pelajar untuk Startup Kami

Para pendidik di startup kami menghadapi kesukaran untuk menjejak tugasan pelajar. Mereka telah menggunakan helaian kerja untuk menjejak tugasan tetapi ini telah menjadi sukar untuk diurus kerana bilangan pelajar meningkat. Mereka telah meminta anda membina aplikasi yang akan membantu mereka menjejak dan mengurus tugasan pelajar. Aplikasi itu harus membolehkan mereka menambah tugasan baru, melihat tugasan, mengemas kini tugasan dan memadam tugasan. Aplikasi itu juga harus membolehkan pendidik dan pelajar melihat tugasan yang telah dinilai dan yang belum dinilai.

Anda akan membina aplikasi menggunakan Copilot dalam Power Apps mengikut langkah-langkah berikut:

1. Navigasi ke skrin utama [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

1. Gunakan ruang teks di skrin utama untuk menerangkan aplikasi yang anda ingin bina. Sebagai contoh, **_Saya ingin membina aplikasi untuk menjejak dan mengurus tugasan pelajar_**. Klik butang **Hantar** untuk menghantar prompt kepada AI Copilot.

![Terangkan aplikasi yang anda ingin bina](../../../translated_images/ms/copilot-chat-prompt-powerapps.84250f341d060830.webp)

1. AI Copilot akan mencadangkan Jadual Dataverse dengan medan yang anda perlukan untuk menyimpan data yang anda ingin jejak dan beberapa data contoh. Anda kemudian boleh mengubah suai jadual tersebut untuk memenuhi keperluan anda menggunakan ciri pembantu AI Copilot melalui langkah perbualan.

   > **Penting**: Dataverse adalah platform data asas untuk Power Platform. Ia adalah platform data kod rendah untuk menyimpan data aplikasi. Ia adalah perkhidmatan yang diurus sepenuhnya yang menyimpan data dengan selamat di Microsoft Cloud dan dipasangkan dalam persekitaran Power Platform anda. Ia dilengkapi dengan keupayaan tadbir urus data terbina dalam, seperti pengelasan data, garis keturunan data, kawalan akses terperinci, dan lainnya. Anda boleh belajar lebih lanjut tentang Dataverse [di sini](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Medan yang dicadangkan dalam jadual baru anda](../../../translated_images/ms/copilot-dataverse-table-powerapps.f4cc07b5d5f9327b.webp)

1. Para pendidik mahu menghantar emel kepada pelajar yang telah menyerahkan tugasan untuk mengemas kini mereka tentang kemajuan tugasan. Anda boleh menggunakan Copilot untuk menambah medan baru ke jadual untuk menyimpan emel pelajar. Sebagai contoh, anda boleh menggunakan prompt berikut untuk menambah medan baru ke jadual: **_Saya mahu menambah lajur untuk menyimpan emel pelajar_**. Klik butang **Hantar** untuk menghantar prompt kepada AI Copilot.

![Menambah medan baru](../../../translated_images/ms/copilot-new-column.35e15ff21acaf274.webp)

1. AI Copilot akan menjana medan baru dan anda kemudian boleh mengubah suai medan tersebut untuk memenuhi keperluan anda.


1. Setelah anda selesai dengan jadual, klik pada butang **Create app** untuk membuat aplikasi.

1. AI Copilot akan menjana aplikasi Canvas yang responsif berdasarkan penerangan anda. Anda kemudian boleh menyesuaikan aplikasi tersebut mengikut keperluan anda.

1. Untuk pendidik menghantar emel kepada pelajar, anda boleh menggunakan Copilot untuk menambah skrin baru ke aplikasi. Contohnya, anda boleh menggunakan arahan berikut untuk menambah skrin baru ke aplikasi: **_Saya mahu menambah skrin untuk menghantar emel kepada pelajar_**. Klik pada butang **Send** untuk menghantar arahan tersebut ke AI Copilot.

![Adding a new screen via a prompt instruction](../../../translated_images/ms/copilot-new-screen.2e0bef7132a17392.webp)

1. AI Copilot akan menjana skrin baru dan anda kemudian boleh menyesuaikan skrin tersebut mengikut keperluan anda.

1. Setelah anda selesai dengan aplikasi, klik pada butang **Save** untuk menyimpan aplikasi.

1. Untuk berkongsi aplikasi dengan pendidik, klik pada butang **Share** dan kemudian klik lagi pada butang **Share**. Anda kemudian boleh berkongsi aplikasi dengan pendidik dengan memasukkan alamat emel mereka.

> **Kerja rumah anda**: Aplikasi yang baru anda bina adalah permulaan yang baik tetapi boleh diperbaiki. Dengan ciri emel, pendidik hanya boleh menghantar emel kepada pelajar secara manual dengan menaip emel mereka. Bolehkah anda menggunakan Copilot untuk membina automasi yang akan membolehkan pendidik menghantar emel kepada pelajar secara automatik apabila mereka menghantar tugasan mereka? Petunjuk anda ialah dengan arahan yang betul anda boleh menggunakan Copilot dalam Power Automate untuk membina ini.

### Bina Jadual Maklumat Invois untuk Startup Kami

Pasukan kewangan startup kami menghadapi kesukaran untuk mengesan invois. Mereka menggunakan hamparan untuk mengesan invois tetapi ia menjadi sukar untuk diurus kerana bilangan invois yang semakin meningkat. Mereka telah meminta anda untuk membina jadual yang akan membantu mereka menyimpan, mengesan dan menguruskan maklumat invois yang diterima. Jadual tersebut harus digunakan untuk membina automasi yang akan mengekstrak semua maklumat invois dan menyimpannya dalam jadual itu. Jadual itu juga harus membolehkan pasukan kewangan melihat invois yang telah dibayar dan yang belum dibayar.

Power Platform mempunyai platform data asas yang dipanggil Dataverse yang membolehkan anda menyimpan data untuk aplikasi dan penyelesaian anda. Dataverse menyediakan platform data berkod rendah untuk menyimpan data aplikasi. Ia adalah perkhidmatan yang dikendalikan sepenuhnya yang menyimpan data dengan selamat dalam Microsoft Cloud dan disediakan dalam persekitaran Power Platform anda. Ia dilengkapi dengan keupayaan tadbir urus data terbina dalam, seperti pengelasan data, garis keturunan data, kawalan akses terperinci, dan banyak lagi. Anda boleh belajar lebih lanjut [tentang Dataverse di sini](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

Kenapa kita perlu menggunakan Dataverse untuk startup kita? Jadual standard dan tersuai dalam Dataverse menyediakan pilihan penyimpanan yang selamat dan berasaskan awan untuk data anda. Jadual membolehkan anda menyimpan pelbagai jenis data, serupa dengan bagaimana anda menggunakan beberapa helaian kerja dalam satu buku kerja Excel. Anda boleh menggunakan jadual untuk menyimpan data yang khusus kepada organisasi atau keperluan perniagaan anda. Beberapa faedah yang akan diperoleh startup kami dari penggunaan Dataverse termasuk tetapi tidak terhad kepada:

- **Mudah diurus**: Kedua-dua metadata dan data disimpan dalam awan, jadi anda tidak perlu risau tentang bagaimana ia disimpan atau diurus. Anda boleh fokus pada pembangunan aplikasi dan penyelesaian anda.

- **Selamat**: Dataverse menyediakan pilihan penyimpanan data yang selamat dan berasaskan awan. Anda boleh mengawal siapa yang boleh mengakses data dalam jadual anda dan bagaimana mereka boleh mengaksesnya menggunakan keselamatan berdasarkan peranan.

- **Metadata kaya**: Jenis data dan hubungan digunakan terus dalam Power Apps

- **Logik dan pengesahan**: Anda boleh menggunakan peraturan perniagaan, medan yang dikira, dan peraturan pengesahan untuk menguatkuasakan logik perniagaan dan mengekalkan ketepatan data.

Sekarang anda sudah tahu apa itu Dataverse dan mengapa anda harus menggunakannya, mari kita lihat bagaimana anda boleh menggunakan Copilot untuk mencipta jadual dalam Dataverse untuk memenuhi keperluan pasukan kewangan kami.

> **Nota** : Anda akan menggunakan jadual ini dalam seksyen seterusnya untuk membina automasi yang akan mengekstrak semua maklumat invois dan menyimpannya dalam jadual.

Untuk mencipta jadual dalam Dataverse menggunakan Copilot, ikuti langkah-langkah berikut:

1. Pergi ke skrin utama [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

2. Pada bar navigasi sebelah kiri, pilih **Tables** dan kemudian klik pada **Describe the new Table**.

![Select new table](../../../translated_images/ms/describe-new-table.0792373eb757281e.webp)

1. Pada skrin **Describe the new Table**, gunakan ruang teks untuk menerangkan jadual yang anda ingin cipta. Contohnya, **_Saya mahu mencipta jadual untuk menyimpan maklumat invois_**. Klik pada butang **Send** untuk menghantar arahan tersebut ke AI Copilot.

![Describe the table](../../../translated_images/ms/copilot-chat-prompt-dataverse.feb2f81e5872b9d2.webp)

1. AI Copilot akan mencadangkan Jadual Dataverse dengan medan yang anda perlukan untuk menyimpan data yang ingin anda jejak dan beberapa data contoh. Anda kemudian boleh menyesuaikan jadual mengikut keperluan menggunakan ciri pembantu AI Copilot melalui langkah perbualan.

![Suggested Dataverse table](../../../translated_images/ms/copilot-dataverse-table.b3bc936091324d9d.webp)

1. Pasukan kewangan mahu menghantar emel kepada pembekal untuk mengemas kini mereka dengan status semasa invois mereka. Anda boleh menggunakan Copilot untuk menambah medan baru dalam jadual untuk menyimpan emel pembekal. Contohnya, anda boleh menggunakan arahan berikut untuk menambah medan baru ke dalam jadual: **_Saya mahu menambah ruangan untuk menyimpan emel pembekal_**. Klik pada butang **Send** untuk menghantar arahan tersebut ke AI Copilot.

1. AI Copilot akan menjana medan baru dan anda boleh menyesuaikan medan tersebut mengikut keperluan anda.

1. Setelah anda selesai dengan jadual, klik pada butang **Create** untuk mencipta jadual.

## Model AI dalam Power Platform dengan AI Builder

AI Builder adalah keupayaan AI berkod rendah yang tersedia dalam Power Platform yang membolehkan anda menggunakan Model AI untuk membantu mengautomasikan proses dan meramalkan hasil. Dengan AI Builder, anda boleh membawa AI ke aplikasi dan aliran anda yang disambungkan ke data anda dalam Dataverse atau dalam pelbagai sumber data awan, seperti SharePoint, OneDrive atau Azure.

## Model AI Pra-Bina vs Model AI Tersuai

AI Builder menyediakan dua jenis Model AI: Model AI Pra-Bina dan Model AI Tersuai. Model AI Pra-Bina adalah Model AI sedia digunakan yang dilatih oleh Microsoft dan tersedia dalam Power Platform. Ini membantu anda menambah kecerdasan ke aplikasi dan aliran tanpa perlu mengumpul data dan kemudian membina, melatih dan menerbitkan model anda sendiri. Anda boleh menggunakan model ini untuk mengautomasikan proses dan meramalkan hasil.

Beberapa Model AI Pra-Bina yang tersedia di Power Platform termasuk:

- **Ekstrak Frasa Utama**: Model ini mengekstrak frasa utama daripada teks.
- **Pengesanan Bahasa**: Model ini mengesan bahasa teks.
- **Analisis Sentimen**: Model ini mengesan sentimen positif, negatif, neutral, atau bercampur dalam teks.
- **Pembaca Kad Perniagaan**: Model ini mengekstrak maklumat daripada kad perniagaan.
- **Pengecaman Teks**: Model ini mengekstrak teks daripada imej.
- **Pengesanan Objek**: Model ini mengesan dan mengekstrak objek daripada imej.
- **Pemprosesan Dokumen**: Model ini mengekstrak maklumat daripada borang.
- **Pemprosesan Invois**: Model ini mengekstrak maklumat daripada invois.

Dengan Model AI Tersuai anda boleh membawa model anda sendiri ke AI Builder supaya ia boleh berfungsi seperti mana-mana model tersuai AI Builder, membolehkan anda melatih model menggunakan data anda sendiri. Anda boleh menggunakan model ini untuk mengautomasikan proses dan meramalkan hasil dalam Power Apps dan Power Automate. Apabila menggunakan model anda sendiri terdapat had yang dikenakan. Baca lebih lanjut tentang [had ini](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![AI builder models](../../../translated_images/ms/ai-builder-models.8069423b84cfc47f.webp)

## Tugasan #2 - Bina Aliran Pemprosesan Invois untuk Startup Kami

Pasukan kewangan menghadapi kesukaran untuk memproses invois. Mereka menggunakan hamparan untuk mengesan invois tetapi ia menjadi sukar diurus kerana bilangan invois meningkat. Mereka meminta anda untuk membina aliran kerja yang akan membantu mereka memproses invois menggunakan AI. Aliran kerja itu harus membolehkan mereka mengekstrak maklumat daripada invois dan menyimpan maklumat itu dalam jadual Dataverse. Aliran kerja itu juga harus membolehkan mereka menghantar emel kepada pasukan kewangan dengan maklumat yang diekstrak.

Sekarang anda sudah tahu apa itu AI Builder dan mengapa anda harus menggunakannya, mari kita lihat bagaimana anda boleh menggunakan Model AI Pemprosesan Invois di AI Builder, yang telah kita bincangkan sebelum ini, untuk membina aliran kerja yang akan membantu pasukan kewangan memproses invois.

Untuk membina aliran kerja yang akan membantu pasukan kewangan memproses invois menggunakan Model AI Pemprosesan Invois di AI Builder, ikuti langkah berikut:

1. Pergi ke skrin utama [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst).

2. Gunakan ruang teks pada skrin utama untuk menerangkan aliran kerja yang anda ingin bina. Contoh, **_Proses invois apabila ia tiba di peti mel saya_**. Klik pada butang **Send** untuk menghantar arahan tersebut ke AI Copilot.

   ![Copilot power automate](../../../translated_images/ms/copilot-chat-prompt-powerautomate.f377e478cc8412de.webp)

3. AI Copilot akan mencadangkan tindakan yang anda perlu lakukan untuk tugasan yang ingin anda automasikan. Anda boleh klik pada butang **Next** untuk meneruskan langkah seterusnya.

4. Pada langkah seterusnya, Power Automate akan menggesa anda untuk menyediakan sambungan yang diperlukan untuk aliran. Setelah selesai, klik pada butang **Create flow** untuk mencipta aliran.

5. AI Copilot akan menjana aliran dan anda boleh menyesuaikan aliran tersebut mengikut keperluan anda.

6. Kemaskini pencetus aliran dan tetapkan **Folder** kepada folder di mana invois akan disimpan. Contohnya, anda boleh tetapkan folder kepada **Inbox**. Klik pada **Show advanced options** dan tetapkan **Only with Attachments** kepada **Yes**. Ini akan memastikan aliran hanya berjalan apabila emel dengan lampiran diterima di folder tersebut.

7. Alih keluar tindakan berikut dari aliran: **HTML to text**, **Compose**, **Compose 2**, **Compose 3** dan **Compose 4** kerana anda tidak akan menggunakannya.

8. Alih keluar tindakan **Condition** dari aliran kerana anda tidak akan menggunakannya. Ia harus kelihatan seperti tangkapan skrin berikut:

   ![power automate, remove actions](../../../translated_images/ms/powerautomate-remove-actions.7216392fe684ceba.webp)

9. Klik pada butang **Add an action** dan cari **Dataverse**. Pilih tindakan **Add a new row**.

10. Pada tindakan **Extract Information from invoices**, kemaskini **Invoice File** untuk merujuk kepada **Attachment Content** dari emel. Ini akan memastikan aliran mengekstrak maklumat dari lampiran invois.

11. Pilih **Table** yang anda cipta sebelumnya. Contohnya, anda boleh memilih jadual **Invoice Information**. Pilih kandungan dinamik dari tindakan sebelumnya untuk mengisi medan berikut:

    - ID
    - Jumlah
    - Tarikh
    - Nama
    - Status - Tetapkan **Status** kepada **Pending**.
    - Emel Pembekal - Gunakan kandungan dinamik **From** dari pencetus **When a new email arrives**.

    ![power automate add row](../../../translated_images/ms/powerautomate-add-row.5edce45e5dd3d51e.webp)

12. Setelah anda selesai dengan aliran, klik pada butang **Save** untuk menyimpan aliran. Anda kemudian boleh menguji aliran dengan menghantar emel dengan invois ke folder yang anda tetapkan dalam pencetus.

> **Kerja rumah anda**: Aliran yang baru anda bina adalah permulaan yang baik, kini anda perlu fikir bagaimana untuk membina automasi yang akan membolehkan pasukan kewangan kita menghantar emel kepada pembekal untuk mengemas kini mereka dengan status semasa invois mereka. Petunjuk anda: aliran mesti berjalan apabila status invois berubah.

## Gunakan Model AI Penjanaan Teks dalam Power Automate

Model AI Create Text with GPT dalam AI Builder membolehkan anda menghasilkan teks berdasarkan arahan dan dikuasakan oleh Microsoft Azure OpenAI Service. Dengan keupayaan ini, anda boleh menggabungkan teknologi GPT (Generative Pre-Trained Transformer) ke dalam aplikasi dan aliran anda untuk membina pelbagai aliran automatik dan aplikasi bermaklumat.

Model GPT menjalani latihan secara meluas dengan jumlah data yang banyak, membolehkan mereka menghasilkan teks yang hampir menyerupai bahasa manusia apabila diberikan arahan. Apabila digabungkan dengan automasi aliran kerja, model AI seperti GPT boleh digunakan untuk mempermudah dan mengautomasikan pelbagai tugas.

Contohnya, anda boleh membina aliran untuk menjana teks secara automatik untuk pelbagai kes penggunaan, seperti: draf emel, penerangan produk, dan banyak lagi. Anda juga boleh menggunakan model ini untuk menjana teks bagi pelbagai aplikasi, seperti chatbot dan aplikasi khidmat pelanggan yang membolehkan ejen khidmat pelanggan memberi respon dengan berkesan dan efisien kepada pertanyaan pelanggan.

![create a prompt](../../../translated_images/ms/create-prompt-gpt.69d429300c2e870a.webp)


Untuk belajar bagaimana menggunakan Model AI ini dalam Power Automate, lalui modul [Tambah kepintaran dengan AI Builder dan GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## Kerja Hebat! Teruskan Pembelajaran Anda

Selepas menamatkan pelajaran ini, lihat koleksi [Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif anda!

Mahu menyesuaikan dan mendapatkan lebih daripada Copilot? Terokai [Awesome Copilot](https://github.com/github/awesome-copilot?WT.mc_id=academic-105485-koreyst) — satu koleksi sumbangan komuniti yang mengandungi arahan, agen, kemahiran, dan konfigurasi untuk membantu anda memanfaatkan GitHub Copilot sepenuhnya.

Pergi ke Pelajaran 11 di mana kita akan melihat bagaimana untuk [mengintegrasikan AI Generatif dengan Panggilan Fungsi](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->