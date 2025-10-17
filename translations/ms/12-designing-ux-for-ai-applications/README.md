<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78bbeed50fd4dc9fdee931f5daf98cb3",
  "translation_date": "2025-10-17T20:52:11+00:00",
  "source_file": "12-designing-ux-for-ai-applications/README.md",
  "language_code": "ms"
}
-->
# Merancang UX untuk Aplikasi AI

[![Merancang UX untuk Aplikasi AI](../../../translated_images/12-lesson-banner.c53c3c7c802e8f563953ce388f6a987ca493472c724d924b060be470951c53c8.ms.png)](https://youtu.be/VKbCejSICA8?si=MKj7GQYHfXRZyWW6)

> _(Klik imej di atas untuk menonton video pelajaran ini)_

Pengalaman pengguna adalah aspek yang sangat penting dalam membina aplikasi. Pengguna perlu dapat menggunakan aplikasi anda dengan cara yang efisien untuk melaksanakan tugas. Menjadi efisien adalah satu perkara, tetapi anda juga perlu merancang aplikasi supaya ia boleh digunakan oleh semua orang, menjadikannya _mudah diakses_. Bab ini akan memberi tumpuan kepada kawasan ini supaya anda akhirnya dapat merancang aplikasi yang orang boleh dan mahu gunakan.

## Pengenalan

Pengalaman pengguna adalah bagaimana seseorang berinteraksi dengan dan menggunakan produk atau perkhidmatan tertentu, sama ada sistem, alat, atau reka bentuk. Apabila membangunkan aplikasi AI, pembangun bukan sahaja memberi tumpuan kepada memastikan pengalaman pengguna berkesan tetapi juga beretika. Dalam pelajaran ini, kita akan membincangkan cara membina aplikasi Kecerdasan Buatan (AI) yang memenuhi keperluan pengguna.

Pelajaran ini akan merangkumi perkara berikut:

- Pengenalan kepada Pengalaman Pengguna dan Memahami Keperluan Pengguna
- Merancang Aplikasi AI untuk Kepercayaan dan Ketelusan
- Merancang Aplikasi AI untuk Kerjasama dan Maklum Balas

## Matlamat Pembelajaran

Selepas mengikuti pelajaran ini, anda akan dapat:

- Memahami cara membina aplikasi AI yang memenuhi keperluan pengguna.
- Merancang aplikasi AI yang mempromosikan kepercayaan dan kerjasama.

### Prasyarat

Luangkan masa dan baca lebih lanjut tentang [pengalaman pengguna dan pemikiran reka bentuk.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Pengenalan kepada Pengalaman Pengguna dan Memahami Keperluan Pengguna

Dalam syarikat permulaan pendidikan rekaan kita, terdapat dua pengguna utama, guru dan pelajar. Setiap daripada mereka mempunyai keperluan unik. Reka bentuk berpusatkan pengguna mengutamakan pengguna, memastikan produk relevan dan bermanfaat untuk mereka yang dimaksudkan.

Aplikasi harus **berguna, boleh dipercayai, mudah diakses dan menyenangkan** untuk memberikan pengalaman pengguna yang baik.

### Kebolehgunaan

Menjadi berguna bermaksud aplikasi mempunyai fungsi yang sesuai dengan tujuannya, seperti mengautomasi proses penilaian atau menghasilkan kad imbas untuk ulang kaji. Aplikasi yang mengautomasi proses penilaian harus dapat memberikan skor kepada kerja pelajar dengan tepat dan efisien berdasarkan kriteria yang telah ditetapkan. Begitu juga, aplikasi yang menghasilkan kad imbas ulang kaji harus dapat mencipta soalan yang relevan dan pelbagai berdasarkan datanya.

### Kebolehpercayaan

Menjadi boleh dipercayai bermaksud aplikasi dapat melaksanakan tugasnya secara konsisten dan tanpa kesilapan. Walau bagaimanapun, AI seperti manusia tidak sempurna dan mungkin terdedah kepada kesilapan. Aplikasi mungkin menghadapi kesilapan atau situasi yang tidak dijangka yang memerlukan campur tangan atau pembetulan manusia. Bagaimana anda menangani kesilapan? Dalam bahagian terakhir pelajaran ini, kita akan membincangkan bagaimana sistem dan aplikasi AI direka untuk kerjasama dan maklum balas.

### Kebolehcapaian

Menjadi mudah diakses bermaksud memperluaskan pengalaman pengguna kepada pengguna dengan pelbagai keupayaan, termasuk mereka yang mempunyai kecacatan, memastikan tiada siapa yang tertinggal. Dengan mengikuti garis panduan dan prinsip kebolehcapaian, penyelesaian AI menjadi lebih inklusif, boleh digunakan, dan bermanfaat untuk semua pengguna.

### Menyenangkan

Menjadi menyenangkan bermaksud aplikasi itu seronok digunakan. Pengalaman pengguna yang menarik boleh memberi kesan positif kepada pengguna, mendorong mereka untuk kembali menggunakan aplikasi dan meningkatkan hasil perniagaan.

![imej yang menggambarkan pertimbangan UX dalam AI](../../../translated_images/uxinai.d5b4ed690f5cefff0c53ffcc01b480cdc1828402e1fdbc980490013a3c50935a.ms.png)

Tidak semua cabaran boleh diselesaikan dengan AI. AI digunakan untuk meningkatkan pengalaman pengguna, sama ada mengautomasi tugas manual atau memperibadikan pengalaman pengguna.

## Merancang Aplikasi AI untuk Kepercayaan dan Ketelusan

Membina kepercayaan adalah kritikal apabila merancang aplikasi AI. Kepercayaan memastikan pengguna yakin bahawa aplikasi akan menyelesaikan kerja, memberikan hasil secara konsisten, dan hasilnya adalah apa yang pengguna perlukan. Risiko dalam kawasan ini adalah ketidakpercayaan dan kepercayaan berlebihan. Ketidakpercayaan berlaku apabila pengguna mempunyai sedikit atau tiada kepercayaan terhadap sistem AI, yang menyebabkan pengguna menolak aplikasi anda. Kepercayaan berlebihan berlaku apabila pengguna terlalu menganggarkan kemampuan sistem AI, menyebabkan pengguna terlalu mempercayai sistem AI. Sebagai contoh, sistem penilaian automatik dalam kes kepercayaan berlebihan mungkin menyebabkan guru tidak menyemak beberapa kertas untuk memastikan sistem penilaian berfungsi dengan baik. Ini boleh mengakibatkan gred yang tidak adil atau tidak tepat untuk pelajar, atau peluang untuk maklum balas dan penambahbaikan yang terlepas.

Dua cara untuk memastikan kepercayaan diletakkan di tengah-tengah reka bentuk adalah kebolehjelasan dan kawalan.

### Kebolehjelasan

Apabila AI membantu membuat keputusan seperti menyampaikan pengetahuan kepada generasi akan datang, adalah penting bagi guru dan ibu bapa untuk memahami bagaimana keputusan AI dibuat. Ini adalah kebolehjelasan - memahami bagaimana aplikasi AI membuat keputusan. Merancang untuk kebolehjelasan termasuk menambah butiran yang menonjolkan bagaimana AI mencapai hasilnya. Audiens mesti sedar bahawa hasilnya dihasilkan oleh AI dan bukan manusia. Sebagai contoh, daripada mengatakan "Mulakan berbual dengan tutor anda sekarang" katakan "Gunakan tutor AI yang menyesuaikan diri dengan keperluan anda dan membantu anda belajar mengikut kadar anda."

![halaman aplikasi dengan ilustrasi jelas tentang kebolehjelasan dalam aplikasi AI](../../../translated_images/explanability-in-ai.134426a96b498fbfdc80c75ae0090aedc0fc97424ae0734fccf7fb00a59a20d9.ms.png)

Contoh lain adalah bagaimana AI menggunakan data pengguna dan peribadi. Sebagai contoh, pengguna dengan persona pelajar mungkin mempunyai batasan berdasarkan persona mereka. AI mungkin tidak dapat mendedahkan jawapan kepada soalan tetapi boleh membantu membimbing pengguna untuk berfikir bagaimana mereka boleh menyelesaikan masalah.

![AI menjawab soalan berdasarkan persona](../../../translated_images/solving-questions.b7dea1604de0cbd2e9c5fa00b1a68a0ed77178a035b94b9213196b9d125d0be8.ms.png)

Satu lagi bahagian penting dalam kebolehjelasan adalah penyederhanaan penjelasan. Pelajar dan guru mungkin bukan pakar AI, oleh itu penjelasan tentang apa yang aplikasi boleh atau tidak boleh lakukan harus disederhanakan dan mudah difahami.

![penjelasan yang disederhanakan tentang kemampuan AI](../../../translated_images/simplified-explanations.4679508a406c3621fa22bad4673e717fbff02f8b8d58afcab8cb6f1aa893a82f.ms.png)

### Kawalan

AI generatif mencipta kerjasama antara AI dan pengguna, di mana contohnya pengguna boleh mengubah suai arahan untuk mendapatkan hasil yang berbeza. Selain itu, setelah hasil dihasilkan, pengguna harus dapat mengubah suai hasil tersebut memberikan mereka rasa kawalan. Sebagai contoh, semasa menggunakan Bing, anda boleh menyesuaikan arahan anda berdasarkan format, nada, dan panjang. Selain itu, anda boleh menambah perubahan pada hasil anda dan mengubah suai hasil seperti yang ditunjukkan di bawah:

![hasil carian Bing dengan pilihan untuk mengubah suai arahan dan hasil](../../../translated_images/bing1.293ae8527dbe2789b675c8591c9fb3cb1aa2ada75c2877f9aa9edc059f7a8b1c.ms.png)

Satu lagi ciri dalam Bing yang membolehkan pengguna mempunyai kawalan terhadap aplikasi adalah keupayaan untuk memilih masuk dan keluar daripada data yang digunakan oleh AI. Untuk aplikasi sekolah, seorang pelajar mungkin ingin menggunakan nota mereka serta sumber guru sebagai bahan ulang kaji.

![hasil carian Bing dengan pilihan untuk mengubah suai arahan dan hasil](../../../translated_images/bing2.309f4845528a88c28c1c9739fb61d91fd993dc35ebe6fc92c66791fb04fceb4d.ms.png)

> Apabila merancang aplikasi AI, niat adalah kunci untuk memastikan pengguna tidak terlalu mempercayai dengan menetapkan jangkaan yang tidak realistik terhadap kemampuannya. Satu cara untuk melakukan ini adalah dengan mencipta geseran antara arahan dan hasil. Mengingatkan pengguna bahawa ini adalah AI dan bukan manusia lain.

## Merancang Aplikasi AI untuk Kerjasama dan Maklum Balas

Seperti yang disebutkan sebelum ini, AI generatif mencipta kerjasama antara pengguna dan AI. Kebanyakan interaksi adalah dengan pengguna memasukkan arahan dan AI menghasilkan hasil. Bagaimana jika hasilnya tidak betul? Bagaimana aplikasi menangani kesilapan jika ia berlaku? Adakah AI menyalahkan pengguna atau meluangkan masa untuk menjelaskan kesilapan?

Aplikasi AI harus dibina untuk menerima dan memberikan maklum balas. Ini bukan sahaja membantu sistem AI meningkatkan tetapi juga membina kepercayaan dengan pengguna. Gelung maklum balas harus dimasukkan dalam reka bentuk, contohnya boleh menjadi tanda suka atau tidak suka pada hasil.

Cara lain untuk menangani ini adalah dengan jelas menyampaikan kemampuan dan batasan sistem. Apabila pengguna membuat kesilapan meminta sesuatu di luar kemampuan AI, harus ada cara untuk menangani ini, seperti yang ditunjukkan di bawah.

![Memberi maklum balas dan menangani kesilapan](../../../translated_images/feedback-loops.7955c134429a94663443ad74d59044f8dc4ce354577f5b79b4bd2533f2cafc6f.ms.png)

Kesilapan sistem adalah perkara biasa dengan aplikasi di mana pengguna mungkin memerlukan bantuan dengan maklumat di luar skop AI atau aplikasi mungkin mempunyai had pada berapa banyak soalan/subjek yang boleh dijana ringkasannya oleh pengguna. Sebagai contoh, aplikasi AI yang dilatih dengan data pada subjek terhad seperti Sejarah dan Matematik mungkin tidak dapat menangani soalan tentang Geografi. Untuk mengatasi ini, sistem AI boleh memberikan respons seperti: "Maaf, produk kami telah dilatih dengan data dalam subjek berikut....., saya tidak dapat menjawab soalan yang anda tanya."

Aplikasi AI tidak sempurna, oleh itu, ia cenderung membuat kesilapan. Apabila merancang aplikasi anda, anda harus memastikan anda mencipta ruang untuk maklum balas daripada pengguna dan pengendalian kesilapan dengan cara yang mudah dan mudah difahami.

## Tugasan

Ambil mana-mana aplikasi AI yang telah anda bina setakat ini, pertimbangkan untuk melaksanakan langkah-langkah berikut dalam aplikasi anda:

- **Menyenangkan:** Pertimbangkan bagaimana anda boleh menjadikan aplikasi anda lebih menyenangkan. Adakah anda menambah penjelasan di mana-mana? Adakah anda menggalakkan pengguna untuk meneroka? Bagaimana anda menyusun mesej kesilapan anda?

- **Kebolehgunaan:** Membina aplikasi web. Pastikan aplikasi anda boleh dinavigasi oleh tetikus dan papan kekunci.

- **Kepercayaan dan ketelusan:** Jangan mempercayai AI sepenuhnya dan hasilnya, pertimbangkan bagaimana anda akan menambah manusia dalam proses untuk mengesahkan hasil. Juga, pertimbangkan dan laksanakan cara lain untuk mencapai kepercayaan dan ketelusan.

- **Kawalan:** Berikan pengguna kawalan terhadap data yang mereka berikan kepada aplikasi. Laksanakan cara pengguna boleh memilih masuk dan keluar daripada pengumpulan data dalam aplikasi AI.

<!-- ## [Kuiz selepas kuliah](../../../12-designing-ux-for-ai-applications/quiz-url) -->

## Teruskan Pembelajaran Anda!

Selepas menyelesaikan pelajaran ini, lihat [koleksi Pembelajaran AI Generatif kami](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk terus meningkatkan pengetahuan AI Generatif anda!

Pergi ke Pelajaran 13, di mana kita akan melihat bagaimana untuk [melindungi aplikasi AI](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.