<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec385b41ee50579025d50cc03bfb3a25",
  "translation_date": "2025-05-19T22:01:43+00:00",
  "source_file": "12-designing-ux-for-ai-applications/README.md",
  "language_code": "ms"
}
-->
# Merancang UX untuk Aplikasi AI

Pengalaman pengguna adalah aspek yang sangat penting dalam membina aplikasi. Pengguna perlu dapat menggunakan aplikasi anda dengan cara yang cekap untuk melaksanakan tugas. Menjadi cekap adalah satu perkara tetapi anda juga perlu mereka bentuk aplikasi supaya ia boleh digunakan oleh semua orang, menjadikannya _mudah diakses_. Bab ini akan memberi tumpuan kepada kawasan ini supaya anda akhirnya dapat merancang aplikasi yang orang boleh dan mahu gunakan.

## Pengenalan

Pengalaman pengguna ialah cara pengguna berinteraksi dengan dan menggunakan produk atau perkhidmatan tertentu sama ada sistem, alat, atau reka bentuk. Apabila membangunkan aplikasi AI, pembangun bukan sahaja memberi tumpuan kepada memastikan pengalaman pengguna berkesan tetapi juga beretika. Dalam pelajaran ini, kami merangkumi cara membina aplikasi Kecerdasan Buatan (AI) yang memenuhi keperluan pengguna.

Pelajaran ini akan merangkumi bidang berikut:

- Pengenalan kepada Pengalaman Pengguna dan Memahami Keperluan Pengguna
- Merancang Aplikasi AI untuk Kepercayaan dan Ketelusan
- Merancang Aplikasi AI untuk Kerjasama dan Maklum Balas

## Matlamat Pembelajaran

Selepas mengikuti pelajaran ini, anda akan dapat:

- Memahami cara membina aplikasi AI yang memenuhi keperluan pengguna.
- Merancang aplikasi AI yang mempromosikan kepercayaan dan kerjasama.

### Prasyarat

Luangkan masa dan baca lebih lanjut mengenai [pengalaman pengguna dan pemikiran reka bentuk.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Pengenalan kepada Pengalaman Pengguna dan Memahami Keperluan Pengguna

Dalam syarikat permulaan pendidikan rekaan kami, kami mempunyai dua pengguna utama, guru dan pelajar. Setiap daripada dua pengguna mempunyai keperluan unik. Reka bentuk yang berpusatkan pengguna mengutamakan pengguna memastikan produk adalah relevan dan bermanfaat untuk mereka yang dimaksudkan.

Aplikasi itu sepatutnya **berguna, boleh dipercayai, mudah diakses dan menyenangkan** untuk memberikan pengalaman pengguna yang baik.

### Kebolehgunaan

Menjadi berguna bermakna aplikasi mempunyai fungsi yang sepadan dengan tujuan yang dimaksudkan, seperti mengautomasikan proses penilaian atau menjana kad imbas untuk ulang kaji. Aplikasi yang mengautomasikan proses penilaian sepatutnya boleh memberikan markah kepada kerja pelajar secara tepat dan cekap berdasarkan kriteria yang telah ditetapkan. Begitu juga, aplikasi yang menjana kad imbas ulang kaji sepatutnya boleh mencipta soalan yang relevan dan pelbagai berdasarkan datanya.

### Kebolehpercayaan

Menjadi boleh dipercayai bermakna aplikasi boleh melaksanakan tugasnya secara konsisten dan tanpa kesilapan. Walau bagaimanapun, AI seperti manusia tidak sempurna dan mungkin terdedah kepada kesilapan. Aplikasi mungkin menghadapi kesilapan atau situasi yang tidak dijangka yang memerlukan campur tangan atau pembetulan manusia. Bagaimana anda mengendalikan kesilapan? Dalam bahagian terakhir pelajaran ini, kami akan membincangkan cara sistem dan aplikasi AI direka bentuk untuk kerjasama dan maklum balas.

### Kebolehcapaian

Menjadi mudah diakses bermakna meluaskan pengalaman pengguna kepada pengguna dengan pelbagai keupayaan, termasuk mereka yang kurang upaya, memastikan tiada siapa yang tertinggal. Dengan mengikuti garis panduan dan prinsip kebolehcapaian, penyelesaian AI menjadi lebih inklusif, boleh digunakan, dan bermanfaat untuk semua pengguna.

### Menyenangkan

Menjadi menyenangkan bermakna aplikasi itu menyeronokkan untuk digunakan. Pengalaman pengguna yang menarik boleh memberi kesan positif kepada pengguna, menggalakkan mereka kembali ke aplikasi dan meningkatkan hasil perniagaan.

Tidak setiap cabaran boleh diselesaikan dengan AI. AI datang untuk menambah pengalaman pengguna anda, sama ada mengautomasikan tugas manual, atau memperibadikan pengalaman pengguna.

## Merancang Aplikasi AI untuk Kepercayaan dan Ketelusan

Membina kepercayaan adalah penting apabila merancang aplikasi AI. Kepercayaan memastikan pengguna yakin bahawa aplikasi akan menyelesaikan kerja, memberikan hasil secara konsisten dan hasilnya adalah apa yang pengguna perlukan. Risiko dalam bidang ini adalah ketidakpercayaan dan kepercayaan berlebihan. Ketidakpercayaan berlaku apabila pengguna mempunyai sedikit atau tiada kepercayaan terhadap sistem AI, ini menyebabkan pengguna menolak aplikasi anda. Kepercayaan berlebihan berlaku apabila pengguna melebih-lebihkan keupayaan sistem AI, menyebabkan pengguna terlalu mempercayai sistem AI. Sebagai contoh, sistem penilaian automatik dalam kes kepercayaan berlebihan mungkin menyebabkan guru tidak meneliti beberapa kertas untuk memastikan sistem penilaian berfungsi dengan baik. Ini boleh mengakibatkan markah yang tidak adil atau tidak tepat untuk pelajar, atau peluang untuk maklum balas dan penambahbaikan terlepas.

Dua cara untuk memastikan bahawa kepercayaan diletakkan tepat di tengah-tengah reka bentuk adalah kebolehan penjelasan dan kawalan.

### Kebolehan Penjelasan

Apabila AI membantu memaklumkan keputusan seperti menyampaikan pengetahuan kepada generasi akan datang, adalah penting bagi guru dan ibu bapa untuk memahami bagaimana keputusan AI dibuat. Ini adalah kebolehan penjelasan - memahami bagaimana aplikasi AI membuat keputusan. Merancang untuk kebolehan penjelasan termasuk menambah butiran contoh tentang apa yang aplikasi AI boleh lakukan. Sebagai contoh, daripada "Mula dengan guru AI", sistem boleh menggunakan: "Ringkaskan nota anda untuk ulang kaji yang lebih mudah menggunakan AI."

Contoh lain adalah bagaimana AI menggunakan data pengguna dan peribadi. Sebagai contoh, seorang pengguna dengan persona pelajar mungkin mempunyai had berdasarkan persona mereka. AI mungkin tidak dapat mendedahkan jawapan kepada soalan tetapi mungkin membantu membimbing pengguna untuk memikirkan cara mereka boleh menyelesaikan masalah.

Bahagian terakhir yang penting dalam kebolehan penjelasan ialah penyederhanaan penjelasan. Pelajar dan guru mungkin bukan pakar AI, oleh itu penjelasan tentang apa yang aplikasi boleh atau tidak boleh lakukan sepatutnya disederhanakan dan mudah difahami.

### Kawalan

AI generatif mencipta kerjasama antara AI dan pengguna, di mana contohnya pengguna boleh mengubah suai arahan untuk hasil yang berbeza. Selain itu, setelah output dijana, pengguna seharusnya dapat mengubah suai hasilnya memberi mereka rasa kawalan. Sebagai contoh, apabila menggunakan Bing, anda boleh menyesuaikan arahan anda berdasarkan format, nada, dan panjang. Selain itu, anda boleh menambah perubahan kepada output anda dan mengubah suai output seperti yang ditunjukkan di bawah:

Ciri lain dalam Bing yang membolehkan pengguna mempunyai kawalan ke atas aplikasi ialah keupayaan untuk memilih masuk dan keluar daripada data yang digunakan AI. Untuk aplikasi sekolah, pelajar mungkin ingin menggunakan nota mereka serta sumber guru sebagai bahan ulang kaji.

> Apabila merancang aplikasi AI, niat adalah kunci dalam memastikan pengguna tidak terlalu mempercayai dengan menetapkan jangkaan yang tidak realistik terhadap keupayaannya. Salah satu cara untuk melakukan ini adalah dengan mencipta geseran antara arahan dan hasil. Mengingatkan pengguna, bahawa ini adalah AI dan bukan manusia

## Merancang Aplikasi AI untuk Kerjasama dan Maklum Balas

Seperti yang disebutkan sebelum ini, AI generatif mencipta kerjasama antara pengguna dan AI. Kebanyakan penglibatan adalah dengan pengguna memasukkan arahan dan AI menjana output. Bagaimana jika output salah? Bagaimana aplikasi mengendalikan kesilapan jika ia berlaku? Adakah AI menyalahkan pengguna atau meluangkan masa untuk menerangkan kesilapan?

Aplikasi AI sepatutnya dibina untuk menerima dan memberi maklum balas. Ini bukan sahaja membantu sistem AI memperbaiki tetapi juga membina kepercayaan dengan pengguna. Satu gelung maklum balas sepatutnya dimasukkan dalam reka bentuk, contohnya boleh menjadi ibu jari ke atas atau ke bawah yang mudah pada output.

Cara lain untuk menangani ini ialah dengan jelas mengkomunikasikan keupayaan dan batasan sistem. Apabila pengguna membuat kesilapan meminta sesuatu di luar keupayaan AI, sepatutnya ada cara untuk menangani ini, seperti yang ditunjukkan di bawah.

Kesilapan sistem adalah biasa dengan aplikasi di mana pengguna mungkin memerlukan bantuan dengan maklumat di luar skop AI atau aplikasi mungkin mempunyai had berapa banyak soalan/subjek yang boleh dijana oleh pengguna. Sebagai contoh, aplikasi AI yang dilatih dengan data pada subjek terhad, contohnya, Sejarah dan Matematik mungkin tidak dapat menangani soalan sekitar Geografi. Untuk mengurangkan ini, sistem AI boleh memberikan respons seperti: "Maaf, produk kami telah dilatih dengan data dalam subjek berikut....., saya tidak dapat menjawab soalan yang anda tanya."

Aplikasi AI tidak sempurna, oleh itu, ia pasti membuat kesilapan. Apabila merancang aplikasi anda, anda harus memastikan anda mencipta ruang untuk maklum balas daripada pengguna dan pengendalian kesilapan dengan cara yang mudah dan mudah dijelaskan.

## Tugasan

Ambil mana-mana aplikasi AI yang telah anda bina setakat ini, pertimbangkan untuk melaksanakan langkah-langkah di bawah dalam aplikasi anda:

- **Menyenangkan:** Pertimbangkan bagaimana anda boleh membuat aplikasi anda lebih menyenangkan. Adakah anda menambah penjelasan di mana-mana? Adakah anda menggalakkan pengguna untuk meneroka? Bagaimana anda menyusun mesej ralat anda?

- **Kebolehgunaan:** Membina aplikasi web. Pastikan aplikasi anda boleh dinavigasi oleh tetikus dan papan kekunci.

- **Kepercayaan dan ketelusan:** Jangan percayakan AI sepenuhnya dan outputnya, pertimbangkan bagaimana anda akan menambah manusia dalam proses untuk mengesahkan output. Juga, pertimbangkan dan laksanakan cara lain untuk mencapai kepercayaan dan ketelusan.

- **Kawalan:** Berikan pengguna kawalan ke atas data yang mereka berikan kepada aplikasi. Laksanakan cara pengguna boleh memilih masuk dan keluar daripada pengumpulan data dalam aplikasi AI.

## Teruskan Pembelajaran Anda!

Selepas menyelesaikan pelajaran ini, lihat koleksi [Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif anda!

Pergi ke Pelajaran 13, di mana kita akan melihat cara [mengamankan aplikasi AI](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.