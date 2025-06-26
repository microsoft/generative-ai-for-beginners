<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec385b41ee50579025d50cc03bfb3a25",
  "translation_date": "2025-06-25T20:29:21+00:00",
  "source_file": "12-designing-ux-for-ai-applications/README.md",
  "language_code": "ms"
}
-->
# Merancang UX untuk Aplikasi AI

Pengalaman pengguna adalah aspek yang sangat penting dalam membina aplikasi. Pengguna perlu dapat menggunakan aplikasi anda dengan cara yang cekap untuk melaksanakan tugas. Menjadi cekap adalah satu perkara tetapi anda juga perlu merancang aplikasi supaya ia boleh digunakan oleh semua orang, menjadikannya _boleh diakses_. Bab ini akan memberi tumpuan kepada bidang ini supaya anda diharapkan dapat mereka bentuk aplikasi yang orang boleh dan mahu gunakan.

## Pengenalan

Pengalaman pengguna adalah bagaimana pengguna berinteraksi dengan dan menggunakan produk atau perkhidmatan tertentu sama ada sistem, alat, atau reka bentuk. Apabila membangunkan aplikasi AI, pembangun bukan sahaja memberi tumpuan untuk memastikan pengalaman pengguna berkesan tetapi juga beretika. Dalam pelajaran ini, kami merangkumi cara membina aplikasi Kecerdasan Buatan (AI) yang memenuhi keperluan pengguna.

Pelajaran ini akan merangkumi bidang berikut:

- Pengenalan kepada Pengalaman Pengguna dan Memahami Keperluan Pengguna
- Merancang Aplikasi AI untuk Kepercayaan dan Ketelusan
- Merancang Aplikasi AI untuk Kerjasama dan Maklum Balas

## Matlamat Pembelajaran

Selepas mengambil pelajaran ini, anda akan dapat:

- Memahami cara membina aplikasi AI yang memenuhi keperluan pengguna.
- Merancang aplikasi AI yang menggalakkan kepercayaan dan kerjasama.

### Prasyarat

Luangkan sedikit masa dan baca lebih lanjut tentang [pengalaman pengguna dan pemikiran reka bentuk.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Pengenalan kepada Pengalaman Pengguna dan Memahami Keperluan Pengguna

Dalam startup pendidikan rekaan kami, kami mempunyai dua pengguna utama, guru dan pelajar. Setiap daripada dua pengguna ini mempunyai keperluan yang unik. Reka bentuk berpusatkan pengguna mengutamakan pengguna dengan memastikan produk adalah relevan dan bermanfaat untuk mereka yang dimaksudkan.

Aplikasi haruslah **berguna, boleh dipercayai, boleh diakses dan menyenangkan** untuk memberikan pengalaman pengguna yang baik.

### Kebolehgunaan

Berguna bermaksud aplikasi mempunyai fungsi yang sesuai dengan tujuan yang dimaksudkan, seperti mengautomasikan proses penilaian atau menjana kad imbas untuk ulang kaji. Aplikasi yang mengautomasikan proses penilaian harus dapat menilai kerja pelajar dengan tepat dan cekap berdasarkan kriteria yang telah ditetapkan. Begitu juga, aplikasi yang menjana kad imbas ulang kaji harus dapat mencipta soalan yang relevan dan pelbagai berdasarkan datanya.

### Kebolehpercayaan

Boleh dipercayai bermaksud aplikasi dapat melaksanakan tugasnya secara konsisten dan tanpa kesilapan. Walau bagaimanapun, AI seperti manusia tidak sempurna dan mungkin terdedah kepada kesilapan. Aplikasi mungkin menghadapi kesilapan atau situasi yang tidak dijangka yang memerlukan campur tangan atau pembetulan manusia. Bagaimana anda menangani kesilapan? Dalam bahagian terakhir pelajaran ini, kami akan membincangkan bagaimana sistem dan aplikasi AI direka untuk kerjasama dan maklum balas.

### Kebolehcapaian

Boleh diakses bermaksud memperluaskan pengalaman pengguna kepada pengguna dengan pelbagai keupayaan, termasuk mereka yang mempunyai kecacatan, memastikan tiada siapa yang tertinggal. Dengan mengikuti garis panduan dan prinsip kebolehcapaian, penyelesaian AI menjadi lebih inklusif, boleh digunakan, dan bermanfaat untuk semua pengguna.

### Menyenangkan

Menyenangkan bermaksud aplikasi seronok digunakan. Pengalaman pengguna yang menarik boleh memberi kesan positif kepada pengguna dengan menggalakkan mereka kembali ke aplikasi dan meningkatkan hasil perniagaan.

Tidak setiap cabaran boleh diselesaikan dengan AI. AI datang untuk menambah pengalaman pengguna anda, sama ada mengautomasikan tugas manual, atau memperibadikan pengalaman pengguna.

## Merancang Aplikasi AI untuk Kepercayaan dan Ketelusan

Membangunkan kepercayaan adalah penting apabila mereka bentuk aplikasi AI. Kepercayaan memastikan pengguna yakin bahawa aplikasi akan menyelesaikan kerja, memberikan hasil secara konsisten dan hasilnya adalah apa yang pengguna perlukan. Risiko dalam bidang ini adalah ketidakpercayaan dan kepercayaan berlebihan. Ketidakpercayaan berlaku apabila pengguna mempunyai sedikit atau tiada kepercayaan pada sistem AI, ini membawa kepada pengguna menolak aplikasi anda. Kepercayaan berlebihan berlaku apabila pengguna melebih-lebihkan kemampuan sistem AI, menyebabkan pengguna mempercayai sistem AI terlalu banyak. Sebagai contoh, sistem penilaian automatik dalam kes kepercayaan berlebihan mungkin menyebabkan guru tidak meneliti beberapa kertas untuk memastikan sistem penilaian berfungsi dengan baik. Ini boleh mengakibatkan gred yang tidak adil atau tidak tepat untuk pelajar, atau peluang untuk maklum balas dan penambahbaikan yang terlepas.

Dua cara untuk memastikan bahawa kepercayaan diletakkan betul-betul di tengah-tengah reka bentuk adalah kebolehjelasan dan kawalan.

### Kebolehjelasan

Apabila AI membantu memaklumkan keputusan seperti menyampaikan pengetahuan kepada generasi akan datang, adalah penting bagi guru dan ibu bapa untuk memahami bagaimana keputusan AI dibuat. Ini adalah kebolehjelasan - memahami bagaimana aplikasi AI membuat keputusan. Merancang untuk kebolehjelasan termasuk menambah butiran contoh tentang apa yang boleh dilakukan oleh aplikasi AI. Sebagai contoh, daripada "Mula dengan guru AI", sistem boleh menggunakan: "Ringkaskan nota anda untuk ulang kaji yang lebih mudah menggunakan AI."

Contoh lain ialah bagaimana AI menggunakan data pengguna dan peribadi. Sebagai contoh, pengguna dengan persona pelajar mungkin mempunyai batasan berdasarkan persona mereka. AI mungkin tidak dapat mendedahkan jawapan kepada soalan tetapi boleh membantu membimbing pengguna untuk berfikir bagaimana mereka boleh menyelesaikan masalah.

Bahagian terakhir yang penting dalam kebolehjelasan adalah penyederhanaan penjelasan. Pelajar dan guru mungkin bukan pakar AI, oleh itu penjelasan tentang apa yang aplikasi boleh atau tidak boleh lakukan harus dipermudahkan dan mudah difahami.

### Kawalan

AI generatif mencipta kerjasama antara AI dan pengguna, di mana contohnya pengguna boleh mengubah suai arahan untuk hasil yang berbeza. Selain itu, setelah output dijana, pengguna harus dapat mengubah hasil memberikan mereka rasa kawalan. Sebagai contoh, apabila menggunakan Bing, anda boleh menyesuaikan arahan anda berdasarkan format, nada dan panjang. Selain itu, anda boleh menambah perubahan pada output anda dan mengubah output seperti yang ditunjukkan di bawah:

Ciri lain dalam Bing yang membolehkan pengguna mempunyai kawalan ke atas aplikasi ialah keupayaan untuk memilih masuk dan keluar daripada data yang digunakan oleh AI. Untuk aplikasi sekolah, seorang pelajar mungkin ingin menggunakan nota mereka serta sumber guru sebagai bahan ulang kaji.

> Apabila mereka bentuk aplikasi AI, ketekunan adalah kunci dalam memastikan pengguna tidak terlalu mempercayai dengan menetapkan jangkaan yang tidak realistik terhadap kemampuannya. Salah satu cara untuk melakukan ini adalah dengan mewujudkan geseran antara arahan dan hasil. Mengingatkan pengguna, bahawa ini adalah AI dan bukan manusia sesama.

## Merancang Aplikasi AI untuk Kerjasama dan Maklum Balas

Seperti yang disebutkan sebelumnya, AI generatif mencipta kerjasama antara pengguna dan AI. Kebanyakan penglibatan adalah dengan pengguna memasukkan arahan dan AI menjana output. Bagaimana jika outputnya salah? Bagaimana aplikasi menangani kesilapan jika ia berlaku? Adakah AI menyalahkan pengguna atau meluangkan masa untuk menjelaskan kesilapan?

Aplikasi AI harus dibina untuk menerima dan memberikan maklum balas. Ini bukan sahaja membantu sistem AI memperbaiki tetapi juga membina kepercayaan dengan pengguna. Gelung maklum balas harus dimasukkan dalam reka bentuk, contohnya boleh menjadi ibu jari ke atas atau ke bawah pada output.

Cara lain untuk menangani ini adalah dengan jelas berkomunikasi tentang kemampuan dan batasan sistem. Apabila pengguna membuat kesilapan meminta sesuatu di luar kemampuan AI, harus ada cara untuk menangani ini, seperti yang ditunjukkan di bawah.

Kesilapan sistem adalah perkara biasa dengan aplikasi di mana pengguna mungkin memerlukan bantuan dengan maklumat di luar skop AI atau aplikasi mungkin mempunyai had pada berapa banyak soalan/subjek yang boleh dihasilkan oleh pengguna. Sebagai contoh, aplikasi AI yang dilatih dengan data mengenai subjek terhad misalnya, Sejarah dan Matematik mungkin tidak dapat menangani soalan mengenai Geografi. Untuk mengatasi ini, sistem AI boleh memberikan respons seperti: "Maaf, produk kami telah dilatih dengan data dalam subjek berikut....., saya tidak dapat menjawab soalan yang anda tanya."

Aplikasi AI tidak sempurna, oleh itu, mereka cenderung membuat kesilapan. Apabila mereka bentuk aplikasi anda, anda harus memastikan anda membuat ruang untuk maklum balas daripada pengguna dan pengendalian kesilapan dengan cara yang mudah dan mudah difahami.

## Tugasan

Ambil mana-mana aplikasi AI yang anda bina setakat ini, pertimbangkan untuk melaksanakan langkah-langkah di bawah dalam aplikasi anda:

- **Menyenangkan:** Pertimbangkan bagaimana anda boleh menjadikan aplikasi anda lebih menyenangkan. Adakah anda menambah penjelasan di mana-mana? Adakah anda menggalakkan pengguna untuk meneroka? Bagaimana anda menyusun kata mesej ralat anda?

- **Kebolehgunaan:** Membangun aplikasi web. Pastikan aplikasi anda boleh dinavigasi dengan tetikus dan papan kekunci.

- **Kepercayaan dan ketelusan:** Jangan percaya sepenuhnya pada AI dan outputnya, pertimbangkan bagaimana anda akan menambah manusia dalam proses untuk mengesahkan output. Juga, pertimbangkan dan laksanakan cara lain untuk mencapai kepercayaan dan ketelusan.

- **Kawalan:** Berikan pengguna kawalan terhadap data yang mereka sediakan kepada aplikasi. Laksanakan cara pengguna boleh memilih masuk dan keluar daripada pengumpulan data dalam aplikasi AI.

## Teruskan Pembelajaran Anda!

Selepas menyelesaikan pelajaran ini, lihat koleksi [Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif anda!

Pergi ke Pelajaran 13, di mana kita akan melihat bagaimana untuk [mengamankan aplikasi AI](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.