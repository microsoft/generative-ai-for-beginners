# Menyumbang

Projek ini mengalu-alukan sumbangan dan cadangan. Kebanyakan sumbangan memerlukan anda
bersetuju dengan Perjanjian Lesen Penyumbang (CLA) yang menyatakan bahawa anda mempunyai hak untuk,
dan benar-benar memberikan, hak kepada kami untuk menggunakan sumbangan anda. Untuk maklumat lanjut, lawati
<https://cla.microsoft.com>.

> Penting: apabila menterjemah teks dalam repo ini, sila pastikan anda tidak menggunakan penterjemahan mesin. Kami akan mengesahkan terjemahan melalui komuniti, jadi sila hanya sukarela untuk terjemahan dalam bahasa yang anda mahir.

Apabila anda menghantar permintaan tarik, CLA-bot akan secara automatik menentukan sama ada anda perlu
menyediakan CLA dan menghiasi PR dengan sewajarnya (contohnya, label, komen). Ikut sahaja
arahan yang diberikan oleh bot. Anda hanya perlu melakukan ini sekali sahaja di semua repositori yang menggunakan CLA kami.

## Kod Etika

Projek ini telah mengamalkan [Kod Etika Sumber Terbuka Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst).
Untuk maklumat lanjut, baca [FAQ Kod Etika](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) atau hubungi [opencode@microsoft.com](mailto:opencode@microsoft.com) untuk sebarang soalan atau komen tambahan.

## Soalan atau Masalah?

Sila jangan buka isu GitHub untuk soalan sokongan umum kerana senarai GitHub perlu digunakan untuk permintaan ciri dan laporan pepijat. Dengan cara ini, kami boleh mengesan isu sebenar atau pepijat daripada kod dan memisahkan perbincangan umum daripada kod sebenar.

## Kesalahan Ejaan, Isu, Pepijat dan sumbangan

Apabila anda menghantar apa-apa perubahan ke repositori Generative AI for Beginners, sila ikuti cadangan-cadangan ini.

* Sentiasa buat forking repositori ke akaun anda sendiri sebelum membuat pengubahsuaian
* Jangan gabungkan pelbagai perubahan ke dalam satu permintaan tarik. Contohnya, hantar pembetulan pepijat dan kemas kini dokumentasi menggunakan PR berasingan
* Jika permintaan tarik anda menunjukkan konflik penggabungan, pastikan mengemas kini main tempatan anda agar menjadi cerminan apa yang ada dalam repositori main sebelum membuat pengubahsuaian
* Jika anda menghantar terjemahan, sila buat satu PR untuk semua fail terjemahan kerana kami tidak menerima terjemahan separa untuk kandungan
* Jika anda menghantar pembetulan kesalahan ejaan atau dokumentasi, anda boleh menggabungkan pengubahsuaian ke dalam satu PR jika sesuai

## Skop editorial dan produk pihak ketiga

Kurikulum ini memfokuskan pada teknologi Microsoft dan piawaian terbuka bebas vendor. Sumbangan harus mempunyai tujuan pendidikan yang jelas dan tidak boleh bertujuan utama untuk memperkenalkan atau mempromosikan produk komersial pihak ketiga, perkhidmatan dihoskan, model penghala, SDK, server MCP, atau tawaran spesifik vendor lain.

Perisian sumber terbuka dan pergantungan pihak ketiga boleh dirujuk apabila ia diperlukan untuk menerangkan piawaian terbuka atau senario interoperabiliti, dipersembahkan secara neutral, dan tidak tertumpu kepada produk vendor atau titik hujung yang dihoskan. Jika sumbangan yang dicadangkan merangkumi produk atau perkhidmatan vendor-spesifik, buka isu dan dapatkan kelulusan penyelenggara sebelum menghantar permintaan tarik.

Penyumbang mesti mendedahkan apa-apa pekerjaan, pemilikan, penajaan, atau penglibatan lain yang berkaitan dengan produk atau perkhidmatan yang dirujuk dalam sumbangan mereka. Jangan sertakan tuntutan harga, prestasi, keselamatan, privasi, atau perbandingan yang tidak disokong. Contoh yang boleh dijalankan tidak boleh menghantar data pelajar atau melakukan tindakan awam melalui perkhidmatan pihak ketiga secara lalai.

## Panduan Am untuk penulisan

- Pastikan semua URL anda dibungkus dalam kurungan persegi diikuti dengan kurungan bulat tanpa ruang tambahan di sekeliling atau di dalamnya `[]()`.
- Pastikan sebarang pautan relatif (iaitu pautan ke fail dan folder lain dalam repositori) bermula dengan `./` yang merujuk kepada fail atau folder yang terletak dalam direktori kerja semasa atau `../` merujuk kepada fail atau folder yang terletak dalam direktori kerja induk.
- Pastikan sebarang pautan relatif (iaitu pautan ke fail dan folder lain dalam repositori) mempunyai ID penjejakan (iaitu `?` atau `&` diikuti `wt.mc_id=` atau `WT.mc_id=`) di hujungnya.
- Pastikan sebarang URL dari domain berikut _github.com, microsoft.com, visualstudio.com, aka.ms, dan azure.com_ mempunyai ID penjejakan (iaitu `?` atau `&` diikuti `wt.mc_id=` atau `WT.mc_id=`) di hujungnya.
- Pastikan pautan anda tidak mempunyai lokal khusus negara di dalamnya (iaitu `/en-us/` atau `/en/`).
- Pastikan semua imej disimpan dalam folder `./images`.
- Pastikan imej mempunyai nama yang deskriptif menggunakan aksara Inggeris, nombor, dan tanda sengkang dalam nama imej anda.

## Aliran Kerja GitHub

Apabila anda menghantar permintaan tarik, empat aliran kerja berbeza akan dicetuskan untuk mengesahkan peraturan sebelumnya.
Ikuti sahaja arahan yang disenaraikan di sini untuk lulus pemeriksaan aliran kerja.

- [Periksa Laluan Relatif Rosak](#check-broken-relative-paths)
- [Periksa Laluan Ada Penjejakan](#check-paths-have-tracking)
- [Periksa URL Ada Penjejakan](#check-urls-have-tracking)
- [Periksa URL Tidak Ada Lokal](#check-urls-dont-have-locale)

### Periksa Laluan Relatif Rosak

Aliran kerja ini memastikan bahawa sebarang laluan relatif dalam fail anda berfungsi.
Repositori ini dikerahkan ke halaman GitHub jadi anda perlu berhati-hati apabila menaip pautan yang menghubungkan segala-galanya agar tidak mengarahkan sesiapa ke tempat yang salah.

Untuk memastikan pautan anda berfungsi dengan betul, gunakan VS Code untuk memeriksa.

Contohnya, apabila anda mengarahkan tetikus ke mana-mana pautan dalam fail anda, anda akan diberi cadangan untuk mengikuti pautan itu dengan menekan **ctrl + klik**

![Tangkapan skrin VS Code mengikuti pautan](../../translated_images/ms/vscode-follow-link.85520ab6a1237adc.webp?WT.mc_id=academic-105485-koreyst "Tangkapan skrin dari prompt VS Code untuk mengikuti pautan apabila anda mengarahkan tetikus ke atas pautan.")

Jika anda klik pada pautan dan ia tidak berfungsi secara tempatan, maka sudah pasti ia akan mencetuskan aliran kerja dan tidak akan berfungsi di GitHub.

Untuk membetulkan isu ini, cuba taip pautan dengan bantuan VS Code.

Apabila anda menaip `./` atau `../`, VS Code akan mencadangkan pilihan yang tersedia mengikut apa yang anda taip.

![Tangkapan skrin VS Code memilih laluan relatif](../../translated_images/ms/vscode-select-relative-path.3804eb73c3a9e5f2.webp?WT.mc_id=academic-105485-koreyst "Tangkapan skrin dari prompt VS Code untuk memilih laluan relatif dari senarai pop up.")

Ikut laluan dengan mengklik pada fail atau folder yang dikehendaki dan anda akan pasti laluan anda tidak rosak.

Setelah anda menambah laluan relatif yang betul, simpan, dan tolak perubahan anda, aliran kerja akan dicetuskan semula untuk mengesahkan perubahan anda.
Jika anda lulus pemeriksaan, anda boleh teruskan.

### Periksa Laluan Ada Penjejakan

Aliran kerja ini memastikan bahawa sebarang laluan relatif mempunyai penjejakan di dalamnya.
Repositori ini dikerahkan ke halaman GitHub jadi kami perlu menjejaki pergerakan antara fail dan folder yang berbeza.

Untuk memastikan laluan relatif anda ada penjejakan, periksa teks berikut `?wt.mc_id=` di hujung laluan.
Jika ia ditambah di hujung laluan relatif anda, maka anda akan lulus pemeriksaan ini.

Jika tidak, anda mungkin mendapat ralat berikut.

![Tangkapan skrin komen GitHub periksa laluan tiada penjejakan](../../translated_images/ms/github-check-paths-missing-tracking-comment.880d4afe03e898ff.webp?WT.mc_id=academic-105485-koreyst "Tangkapan skrin dari komen GitHub yang menunjukkan tiada penjejakan dari laluan relatif")

Untuk membetulkan isu ini, cuba buka laluan fail yang diserlahkan oleh aliran kerja dan tambah ID penjejakan di hujung laluan relatif.

Setelah anda menambah ID penjejakan, simpan, dan tolak perubahan anda, aliran kerja akan dicetuskan semula untuk mengesahkan perubahan anda.
Jika anda lulus pemeriksaan, anda boleh teruskan.

### Periksa URL Ada Penjejakan

Aliran kerja ini memastikan bahawa sebarang URL web mempunyai penjejakan di dalamnya.
Repositori ini tersedia untuk semua orang jadi anda perlu pastikan untuk menjejaki akses untuk mengetahui dari mana trafik datang.

Untuk memastikan URL anda ada penjejakan, periksa teks berikut `?wt.mc_id=` di hujung URL.
Jika ia ditambah pada URL anda, maka anda akan lulus pemeriksaan ini.

Jika tidak, anda mungkin mendapat ralat berikut.

![Tangkapan skrin komen GitHub periksa URL tiada penjejakan](../../translated_images/ms/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e.webp?WT.mc_id=academic-105485-koreyst "Tangkapan skrin dari komen GitHub yang menunjukkan tiada penjejakan dari URL")

Untuk membetulkan isu ini, cuba buka laluan fail yang diserlahkan oleh aliran kerja dan tambah ID penjejakan di hujung URL.

Setelah anda menambah ID penjejakan, simpan, dan tolak perubahan anda, aliran kerja akan dicetuskan semula untuk mengesahkan perubahan anda.
Jika anda lulus pemeriksaan, anda boleh teruskan.

### Periksa URL Tiada Lokal

Aliran kerja ini memastikan bahawa sebarang URL web tidak mempunyai lokal khusus negara di dalamnya.
Repositori ini tersedia untuk semua orang di seluruh dunia jadi anda perlu pastikan tidak menyertakan lokal negara anda dalam URL.

Untuk memastikan URL anda tidak mempunyai lokal negara, periksa teks berikut `/en-us/` atau `/en/` atau mana-mana lokal bahasa lain di mana-mana dalam URL.
Jika ia tidak hadir dalam URL anda, maka anda akan lulus pemeriksaan ini.

Jika tidak, anda mungkin mendapat ralat berikut.

![Tangkapan skrin komen GitHub periksa lokal negara](../../translated_images/ms/github-check-country-locale-comment.2f4fe93228161dee.webp?WT.mc_id=academic-105485-koreyst "Tangkapan skrin dari komen GitHub yang menunjukkan lokal negara ditambah ke URL")

Untuk membetulkan isu ini, cuba buka laluan fail yang diserlahkan oleh aliran kerja dan keluarkan lokal negara dari URL.

Setelah anda mengeluarkan lokal negara, simpan, dan tolak perubahan anda, aliran kerja akan dicetuskan semula untuk mengesahkan perubahan anda.
Jika anda lulus pemeriksaan, anda boleh teruskan.

Tahniah! Kami akan menghubungi anda secepat mungkin dengan maklum balas tentang sumbangan anda.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->