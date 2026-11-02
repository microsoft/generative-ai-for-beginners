# Menyumbang

Projek ini mengalu-alukan sumbangan dan cadangan. Kebanyakan sumbangan memerlukan anda
bersetuju dengan Perjanjian Lesen Penyumbang (CLA) yang menyatakan anda mempunyai hak untuk,
dan benar-benar memberikan, kami hak untuk menggunakan sumbangan anda. Untuk maklumat lanjut, lawati
<https://cla.microsoft.com>.

> Penting: apabila menterjemah teks dalam repositori ini, pastikan anda tidak menggunakan terjemahan mesin. Kami akan mengesahkan terjemahan melalui komuniti, jadi sila hanya menjadi sukarelawan untuk terjemahan dalam bahasa yang anda mahir.

Apabila anda menghantar permintaan tarik, bot CLA secara automatik akan menentukan sama ada anda perlu
menyediakan CLA dan menghias PR dengan sewajarnya (contoh: label, komen). Ikuti sahaja
arahan yang diberikan oleh bot. Anda hanya perlu melakukan ini sekali sahaja merentasi semua repositori yang menggunakan CLA kami.

## Kod Etika

Projek ini telah mengguna Pakai [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst).
Untuk maklumat lanjut baca [Soalan Lazim Kod Etika](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) atau hubungi [opencode@microsoft.com](mailto:opencode@microsoft.com) untuk sebarang soalan atau komen tambahan.

## Soalan atau Masalah?

Sila jangan buka isu GitHub untuk soalan sokongan am kerana senarai GitHub sepatutnya digunakan untuk permintaan ciri dan laporan pepijat. Dengan cara ini kami boleh mengesan isu sebenar atau pepijat dari kod dengan lebih mudah dan membezakan perbincangan am daripada kod sebenar.

## Kesalahan Ejaan, Isu, Pepijat dan sumbangan

Apabila anda menghantar apa-apa perubahan ke repositori Generative AI for Beginners, sila ikut cadangan ini.

* Sentiasa buat garpu repositori ke akaun anda sebelum melakukan pengubahsuaian
* Jangan gabungkan pelbagai perubahan ke dalam satu permintaan tarik. Contohnya, hantar pembaikan pepijat dan kemas kini dokumentasi menggunakan PR berasingan
* Jika permintaan tarik anda menunjukkan konflik penggabungan, pastikan anda mengemas kini main tempatan untuk menjadi cermin apa yang ada dalam repositori main sebelum membuat pengubahsuaian
* Jika anda menghantar terjemahan, sila buat satu PR untuk semua fail yang diterjemah kerana kami tidak menerima terjemahan sebahagian untuk kandungan
* Jika anda menghantar pembetulan ejaan atau dokumentasi, anda boleh menggabungkan pengubahsuaian ke dalam PR tunggal jika sesuai

## Skop editorial dan produk pihak ketiga

Kurikulum ini memfokuskan pada teknologi Microsoft dan piawaian terbuka vendor-neutral. Sumbangan harus berperanan jelas dalam pendidikan dan tidak boleh bertujuan utama untuk memperkenalkan atau mempromosikan produk komersial pihak ketiga, perkhidmatan dihoskan, penghala model, SDK, pelayan MCP, atau tawaran khusus vendor lain.

Perisian sumber terbuka dan kebergantungan pihak ketiga boleh dirujuk apabila diperlukan untuk menerangkan piawaian terbuka atau senario interoperabiliti, dipersembahkan secara neutral, dan tidak tertumpu pada produk vendor atau titik akhir yang dihoskan. Jika sumbangan anda termasuk produk atau perkhidmatan vendor-spesifik, buka isu dan dapatkan kelulusan penyelia sebelum menghantar permintaan tarik.

Penyumbang mesti mendedahkan sebarang pekerjaan, pemilikan, penajaan, atau afiliasi lain yang berkaitan dengan produk atau perkhidmatan yang dirujuk dalam sumbangan mereka. Jangan sertakan tuntutan harga, prestasi, keselamatan, privasi, atau perbandingan yang tidak disokong. Contoh boleh dijalankan mesti tidak menghantar data pelajar atau melakukan tindakan awam melalui perkhidmatan pihak ketiga secara lalai.

## Panduan Umum menulis

- Pastikan semua URL anda dibungkus dalam kurungan segi empat diikuti dengan kurungan bulat tanpa ruang tambahan di sekeliling atau di dalamnya `[]()`.
- Pastikan mana-mana pautan relatif (contohnya pautan ke fail dan folder lain dalam repositori) bermula dengan `./` merujuk kepada fail atau folder yang terletak dalam direktori kerja semasa atau `../` merujuk kepada fail atau folder yang terletak dalam direktori kerja induk.
- Pastikan mana-mana pautan relatif (contohnya pautan ke fail dan folder lain dalam repositori) mempunyai ID penjejakan (contohnya `?` atau `&` kemudian `wt.mc_id=` atau `WT.mc_id=`) di hujungnya.
- Pastikan mana-mana URL daripada domain berikut _github.com, microsoft.com, visualstudio.com, aka.ms, dan azure.com_ mempunyai ID penjejakan (contohnya `?` atau `&` kemudian `wt.mc_id=` atau `WT.mc_id=`) di hujungnya.
- Pastikan pautan anda tidak mempunyai lokal khusus negara (contohnya `/en-us/` atau `/en/`).
- Pastikan semua imej disimpan dalam folder `./images`.
- Pastikan imej mempunyai nama yang deskriptif menggunakan aksara Inggeris, nombor, dan sengkang dalam nama imej anda.

## Aliran Kerja GitHub

Apabila anda menghantar permintaan tarik, empat aliran kerja berbeza akan dicetuskan untuk mengesahkan peraturan sebelumnya.
Ikuti sahaja arahan yang disenaraikan di sini untuk melepasi pemeriksaan aliran kerja.

- [Periksa Laluan Relatif Rosak](#check-broken-relative-paths)
- [Periksa Laluan Ada Penjejakan](#check-paths-have-tracking)
- [Periksa URL Ada Penjejakan](#check-urls-have-tracking)
- [Periksa URL Tiada Lokal](#check-urls-dont-have-locale)

### Periksa Laluan Relatif Rosak

Aliran kerja ini memastikan sebarang laluan relatif dalam fail anda berfungsi.
Repositori ini dikerahkan ke GitHub pages jadi anda perlu berhati-hati ketika menaip pautan bagi mengelakkan mengarah ke tempat yang salah.

Untuk pastikan pautan anda berfungsi dengan betul, gunakan VS code untuk memeriksanya.

Contohnya, apabila anda melayangkan tetikus ke mana-mana pautan dalam fail anda, anda akan digesa untuk mengikuti pautan dengan menekan **ctrl + klik**

![Skrin tangkap VS code ikuti pautan](../../translated_images/ms/vscode-follow-link.85520ab6a1237adc.webp?WT.mc_id=academic-105485-koreyst "Screenshot dari arahan vs code untuk mengikuti pautan apabila anda melayangkan tetikus ke pautan.")

Jika anda klik pautan dan ia tiada berfungsi secara tempatan, maka pasti ia akan mencetuskan aliran kerja dan tidak berfungsi di GitHub.

Untuk membetulkan isu ini, cuba taip pautan dengan bantuan VS code.

Apabila anda taip `./` atau `../`, VS code akan menggesa anda memilih dari pilihan yang ada mengikut apa yang anda taip.

![Skrin tangkap VS code pilih laluan relatif](../../translated_images/ms/vscode-select-relative-path.3804eb73c3a9e5f2.webp?WT.mc_id=academic-105485-koreyst "Screenshot dari arahan vs code pilih laluan relatif dari senarai timbul.")

Ikuti laluan dengan klik pada fail atau folder yang dikehendaki dan anda pasti laluan anda tidak rosak.

Setelah anda menambah laluan relatif yang betul, simpan, dan seret perubahan anda, aliran kerja akan dicetuskan semula untuk mengesahkan perubahan anda.
Jika anda lulus pemeriksaan, maka anda sudah sedia.

### Periksa Laluan Ada Penjejakan

Aliran kerja ini memastikan mana-mana laluan relatif mempunyai penjejakan di dalamnya.
Repositori ini dikerahkan ke GitHub pages jadi kita perlu mengesan pergerakan antara fail dan folder yang berbeza.

Untuk pastikan laluan relatif anda ada penjejakan, periksa teks berikut `?wt.mc_id=` di hujung laluan.
Jika ia ditambah pada laluan relatif anda, maka anda akan lulus pemeriksaan ini.

Jika tidak, anda boleh mendapatkan ralat berikut.

![GitHub periksa laluan tiada penjejakan komen skrin tangkap](../../translated_images/ms/github-check-paths-missing-tracking-comment.880d4afe03e898ff.webp?WT.mc_id=academic-105485-koreyst "Screenshot dari komen github yang menunjukkan tiada penjejakan dari laluan relatif")

Untuk membetulkan isu ini, cuba buka laluan fail yang diwarnakan oleh aliran kerja dan tambah ID penjejakan ke hujung laluan relatif.

Setelah anda tambahkan ID penjejakan, simpan, dan seret perubahan anda, aliran kerja akan dicetuskan semula untuk mengesahkan perubahan anda.
Jika anda lulus pemeriksaan, maka anda sudah sedia.

### Periksa URL Ada Penjejakan

Aliran kerja ini memastikan mana-mana URL web mempunyai penjejakan di dalamnya.
Repositori ini tersedia untuk semua orang jadi anda perlu pastikan untuk menjejaki akses bagi mengetahui dari mana trafik datang.

Untuk pastikan URL anda ada penjejakan, periksa teks berikut `?wt.mc_id=` di hujung URL.
Jika ia ditambah pada URL anda, maka anda akan lulus pemeriksaan ini.

Jika tidak, anda boleh mendapatkan ralat berikut.

![GitHub periksa url tiada penjejakan komen skrin tangkap](../../translated_images/ms/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e.webp?WT.mc_id=academic-105485-koreyst "Screenshot dari komen github yang menunjukkan tiada penjejakan dari url")

Untuk membetulkan isu ini, cuba buka laluan fail yang diwarnakan oleh aliran kerja dan tambah ID penjejakan ke hujung URL.

Setelah anda tambahkan ID penjejakan, simpan, dan seret perubahan anda, aliran kerja akan dicetuskan semula untuk mengesahkan perubahan anda.
Jika anda lulus pemeriksaan, maka anda sudah sedia.

### Periksa URL Tiada Lokal

Aliran kerja ini memastikan mana-mana URL web tidak mempunyai lokal spesifik negara.
Repositori ini tersedia untuk semua orang di seluruh dunia jadi anda perlu pastikan tidak memasukkan lokal negara anda dalam URL.

Untuk pastikan URL anda tiada lokal negara di dalamnya, periksa teks berikut `/en-us/` atau `/en/` atau mana-mana lokal bahasa lain di mana-mana dalam URL.
Jika ia tiada dalam URL anda, maka anda akan lulus pemeriksaan ini.

Jika tidak, anda boleh mendapatkan ralat berikut.

![GitHub periksa lokal negara komen skrin tangkap](../../translated_images/ms/github-check-country-locale-comment.2f4fe93228161dee.webp?WT.mc_id=academic-105485-koreyst "Screenshot dari komen github yang menunjukkan tambahan lokal negara ke url")

Untuk membetulkan isu ini, cuba buka laluan fail yang diwarnakan oleh aliran kerja dan keluarkan lokal negara dari URL.

Setelah anda keluarkan lokal negara, simpan, dan seret perubahan anda, aliran kerja akan dicetuskan semula untuk mengesahkan perubahan anda.
Jika anda lulus pemeriksaan, maka anda sudah sedia.

Tahniah! Kami akan menghubungi anda secepat mungkin dengan maklum balas tentang sumbangan anda.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->