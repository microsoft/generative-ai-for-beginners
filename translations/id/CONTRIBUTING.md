# Kontribusi

Proyek ini menyambut kontribusi dan saran. Sebagian besar kontribusi mengharuskan Anda untuk
menyetujui Perjanjian Lisensi Kontributor (CLA) yang menyatakan bahwa Anda memiliki hak untuk,
dan benar-benar memberi kami hak untuk menggunakan kontribusi Anda. Untuk detailnya, kunjungi
<https://cla.microsoft.com>.

> Penting: saat menerjemahkan teks dalam repositori ini, pastikan Anda tidak menggunakan terjemahan mesin. Kami akan memverifikasi terjemahan melalui komunitas, jadi harap hanya menjadi relawan untuk terjemahan dalam bahasa yang Anda kuasai.

Saat Anda mengirimkan permintaan tarik, bot CLA secara otomatis akan menentukan apakah Anda perlu
menyediakan CLA dan menghiasi PR dengan tepat (misalnya, label, komentar). Cukup ikuti
instruksi yang diberikan oleh bot. Anda hanya perlu melakukan ini sekali untuk semua repositori yang menggunakan CLA kami.

## Kode Etik

Proyek ini telah mengadopsi [Kode Etik Sumber Terbuka Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst).
Untuk informasi lebih lanjut baca [FAQ Kode Etik](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) atau hubungi [opencode@microsoft.com](mailto:opencode@microsoft.com) untuk pertanyaan atau komentar tambahan.

## Pertanyaan atau Masalah?

Harap jangan membuka isu GitHub untuk pertanyaan dukungan umum karena daftar GitHub sebaiknya digunakan untuk permintaan fitur dan laporan bug. Dengan cara ini kami dapat lebih mudah melacak masalah atau bug sebenarnya dari kode dan menjaga diskusi umum terpisah dari kode aslinya.

## Salah ketik, Masalah, Bug dan kontribusi

Setiap kali Anda mengirimkan perubahan ke repositori Generative AI for Beginners, harap ikuti rekomendasi ini.

* Selalu fork repositori ke akun Anda sebelum membuat modifikasi
* Jangan gabungkan beberapa perubahan ke dalam satu permintaan tarik. Misalnya, kirim perbaikan bug dan pembaruan dokumentasi menggunakan PR terpisah
* Jika permintaan tarik Anda menunjukkan konflik penggabungan, pastikan untuk memperbarui main lokal Anda agar mencerminkan repositori main sebelum melakukan modifikasi
* Jika Anda mengirimkan terjemahan, buat satu PR untuk semua file yang diterjemahkan karena kami tidak menerima terjemahan sebagian untuk konten
* Jika Anda mengirimkan perbaikan salah ketik atau dokumentasi, Anda dapat menggabungkan modifikasi ke satu PR bila cocok

## Lingkup editorial dan produk pihak ketiga

Kurikulum ini fokus pada teknologi Microsoft dan standar terbuka yang netral vendor. Kontribusi harus memiliki tujuan edukasi yang jelas dan tidak boleh terutama dimaksudkan untuk memperkenalkan atau mempromosikan produk komersial pihak ketiga, layanan yang di-host, pengarah model, SDK, server MCP, atau penawaran khusus vendor lainnya.

Perangkat lunak sumber terbuka dan ketergantungan pihak ketiga dapat direferensikan ketika diperlukan untuk menjelaskan standar terbuka atau skenario interoperabilitas, disajikan secara netral, dan tidak terpusat pada produk vendor atau titik akhir yang di-host. Jika kontribusi yang diusulkan mencakup produk atau layanan khusus vendor, buka isu dan dapatkan persetujuan pemelihara sebelum mengirim permintaan tarik.

Kontributor harus mengungkapkan pekerjaan, kepemilikan, sponsor, atau afiliasi lain yang relevan dengan produk atau layanan yang dirujuk dalam kontribusi mereka. Jangan menyertakan klaim harga, performa, keamanan, privasi, atau perbandingan yang tidak didukung. Contoh yang dapat dijalankan harus tidak mengirimkan data pembelajar atau melakukan tindakan publik melalui layanan pihak ketiga eksternal secara default.

## Panduan Umum untuk menulis

- Pastikan semua URL Anda dibungkus dalam tanda kurung siku diikuti oleh tanda kurung tanpa spasi tambahan di sekitar atau di dalamnya `[]()`.
- Pastikan setiap tautan relatif (misalnya tautan ke file dan folder lain di repositori) dimulai dengan `./` yang merujuk ke file atau folder yang terletak di direktori kerja saat ini atau `../` yang merujuk ke file atau folder yang terletak di direktori kerja induk.
- Pastikan setiap tautan relatif (misalnya tautan ke file dan folder lain di repositori) memiliki ID pelacakan (misalnya `?` atau `&` lalu `wt.mc_id=` atau `WT.mc_id=`) di akhir tautan tersebut.
- Pastikan setiap URL dari domain berikut _github.com, microsoft.com, visualstudio.com, aka.ms, dan azure.com_ memiliki ID pelacakan (misalnya `?` atau `&` lalu `wt.mc_id=` atau `WT.mc_id=`) di akhir URL.
- Pastikan tautan Anda tidak memiliki lokal khusus negara (misalnya `/en-us/` atau `/en/`).
- Pastikan semua gambar disimpan di folder `./images`.
- Pastikan gambar memiliki nama deskriptif menggunakan karakter bahasa Inggris, angka, dan tanda hubung dalam nama gambar Anda.

## Alur Kerja GitHub

Saat Anda mengirimkan permintaan tarik, empat alur kerja berbeda akan dipicu untuk memvalidasi aturan sebelumnya.
Cukup ikuti instruksi yang tercantum di sini untuk melewati pemeriksaan alur kerja.

- [Periksa Jalur Relatif Rusak](#check-broken-relative-paths)
- [Periksa Jalur Memiliki Pelacakan](#check-paths-have-tracking)
- [Periksa URL Memiliki Pelacakan](#check-urls-have-tracking)
- [Periksa URL Tidak Memiliki Lokal](#check-urls-dont-have-locale)

### Periksa Jalur Relatif Rusak

Alur kerja ini memastikan bahwa setiap jalur relatif dalam file Anda berfungsi.
Repositori ini dideploy ke halaman GitHub jadi Anda harus sangat hati-hati saat mengetik tautan yang menghubungkan semuanya agar tidak mengarahkan siapa pun ke tempat yang salah.

Untuk memastikan tautan Anda berfungsi dengan baik cukup gunakan VS code untuk memeriksanya.

Misalnya, saat Anda mengarahkan kursor ke tautan dalam file Anda, Anda akan diminta mengikuti tautan dengan menekan **ctrl + klik**

![Tangkapan layar mengikuti tautan VS code](../../translated_images/id/vscode-follow-link.85520ab6a1237adc.webp?WT.mc_id=academic-105485-koreyst "Tangkapan layar dari prompt vs code untuk mengikuti tautan saat mengarahkan kursor di atas tautan.")

Jika Anda klik tautan dan itu tidak berfungsi secara lokal, maka pasti akan memicu alur kerja dan tidak akan berfungsi di GitHub.

Untuk memperbaiki masalah ini, coba ketik tautan dengan bantuan VS code.

Saat Anda mengetik `./` atau `../` VS code akan memberi Anda pilihan dari opsi yang tersedia sesuai dengan yang Anda ketik.

![Tangkapan layar memilih jalur relatif VS code](../../translated_images/id/vscode-select-relative-path.3804eb73c3a9e5f2.webp?WT.mc_id=academic-105485-koreyst "Tangkapan layar dari prompt VS code untuk memilih jalur relatif dari daftar pop up.")

Ikuti jalur dengan mengklik file atau folder yang diinginkan dan Anda akan yakin bahwa jalur Anda tidak rusak.

Setelah Anda menambahkan jalur relatif yang benar, simpan, dan dorong perubahan Anda, alur kerja akan dipicu lagi untuk memverifikasi perubahan Anda.
Jika Anda lolos pemeriksaan maka Anda siap melanjutkan.

### Periksa Jalur Memiliki Pelacakan

Alur kerja ini memastikan bahwa setiap jalur relatif memiliki pelacakan di dalamnya.
Repositori ini dideploy ke halaman GitHub jadi kita perlu melacak pergerakan antar file dan folder yang berbeda.

Untuk memastikan jalur relatif Anda memiliki pelacakan di dalamnya cukup periksa teks berikut `?wt.mc_id=` di akhir jalur.
Jika itu ditambahkan ke jalur relatif Anda maka Anda akan lolos pemeriksaan ini.

Jika tidak, Anda mungkin mendapatkan kesalahan berikut.

![Tangkapan layar komentar cek jalur GitHub kekurangan pelacakan](../../translated_images/id/github-check-paths-missing-tracking-comment.880d4afe03e898ff.webp?WT.mc_id=academic-105485-koreyst "Tangkapan layar dari komentar github yang menunjukkan kekurangan pelacakan dari jalur relatif")

Untuk memperbaiki masalah ini, coba buka jalur file yang disorot oleh alur kerja dan tambahkan ID pelacakan di akhir jalur relatif.

Setelah Anda menambahkan ID pelacakan, simpan, dan dorong perubahan Anda, alur kerja akan dipicu lagi untuk memverifikasi perubahan Anda.
Jika Anda lolos pemeriksaan maka Anda siap melanjutkan.

### Periksa URL Memiliki Pelacakan

Alur kerja ini memastikan bahwa setiap URL web memiliki pelacakan di dalamnya.
Repositori ini tersedia untuk semua orang jadi Anda perlu memastikan untuk melacak akses agar tahu dari mana sumber trafik berasal.

Untuk memastikan URL Anda memiliki pelacakan di dalamnya cukup periksa teks berikut `?wt.mc_id=` di akhir URL.
Jika itu ditambahkan ke URL Anda maka Anda akan lolos pemeriksaan ini.

Jika tidak, Anda mungkin mendapatkan kesalahan berikut.

![Tangkapan layar komentar cek url GitHub kekurangan pelacakan](../../translated_images/id/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e.webp?WT.mc_id=academic-105485-koreyst "Tangkapan layar dari komentar github yang menunjukkan kekurangan pelacakan dari url")

Untuk memperbaiki masalah ini, coba buka jalur file yang disorot oleh alur kerja dan tambahkan ID pelacakan di akhir URL.

Setelah Anda menambahkan ID pelacakan, simpan, dan dorong perubahan Anda, alur kerja akan dipicu lagi untuk memverifikasi perubahan Anda.
Jika Anda lolos pemeriksaan maka Anda siap melanjutkan.

### Periksa URL Tidak Memiliki Lokal

Alur kerja ini memastikan bahwa setiap URL web tidak memiliki lokal spesifik negara di dalamnya.
Repositori ini tersedia untuk semua orang di seluruh dunia jadi Anda perlu memastikan untuk tidak menyertakan lokal negara Anda dalam URL.

Untuk memastikan URL Anda tidak memiliki lokal negara di dalamnya cukup periksa teks berikut `/en-us/` atau `/en/` atau lokal bahasa lain di mana pun dalam URL.
Jika tidak ada dalam URL Anda maka Anda akan lolos pemeriksaan ini.

Jika tidak, Anda mungkin mendapatkan kesalahan berikut.

![Tangkapan layar komentar cek lokal negara GitHub](../../translated_images/id/github-check-country-locale-comment.2f4fe93228161dee.webp?WT.mc_id=academic-105485-koreyst "Tangkapan layar dari komentar github yang menunjukkan penambahan lokal negara ke url")

Untuk memperbaiki masalah ini, coba buka jalur file yang disorot oleh alur kerja dan hapus lokal negara dari URL.

Setelah Anda menghapus lokal negara, simpan, dan dorong perubahan Anda, alur kerja akan dipicu lagi untuk memverifikasi perubahan Anda.
Jika Anda lolos pemeriksaan maka Anda siap melanjutkan.

Selamat! Kami akan segera menghubungi Anda dengan umpan balik tentang kontribusi Anda.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->