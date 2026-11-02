# Kontribusi

Proyek ini menyambut kontribusi dan saran. Sebagian besar kontribusi mengharuskan Anda untuk
menyetujui Perjanjian Lisensi Kontributor (CLA) yang menyatakan bahwa Anda memiliki hak untuk,
dan benar-benar memberikan, hak kepada kami untuk menggunakan kontribusi Anda. Untuk detailnya, kunjungi
<https://cla.microsoft.com>.

> Penting: saat menerjemahkan teks di repo ini, harap pastikan bahwa Anda tidak menggunakan terjemahan mesin. Kami akan memverifikasi terjemahan melalui komunitas, jadi harap hanya sukarela untuk terjemahan dalam bahasa yang Anda kuasai.

Saat Anda mengirimkan pull request, CLA-bot akan secara otomatis menentukan apakah Anda perlu
menyediakan CLA dan memberi tanda pada PR dengan tepat (misalnya, label, komentar). Cukup ikuti
instruksi yang diberikan oleh bot. Anda hanya perlu melakukan ini sekali di semua repositori yang menggunakan CLA kami.

## Kode Etik

Proyek ini telah mengadopsi [Kode Etik Sumber Terbuka Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst).
Untuk informasi lebih lanjut baca [FAQ Kode Etik](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) atau hubungi [opencode@microsoft.com](mailto:opencode@microsoft.com) untuk pertanyaan atau komentar tambahan.

## Pertanyaan atau Masalah?

Harap jangan membuka isu GitHub untuk pertanyaan dukungan umum karena daftar GitHub harus digunakan untuk permintaan fitur dan laporan bug. Dengan cara ini kami dapat lebih mudah melacak isu atau bug aktual dari kode dan menjaga diskusi umum terpisah dari kode yang sebenarnya.

## Typo, Masalah, Bug dan kontribusi

Setiap kali Anda mengirimkan perubahan ke repositori Generative AI for Beginners, harap ikuti rekomendasi ini.

* Selalu fork repositori ke akun Anda sendiri sebelum melakukan modifikasi
* Jangan menggabungkan beberapa perubahan ke satu pull request. Misalnya, kirimkan perbaikan bug dan pembaruan dokumentasi menggunakan PR yang terpisah
* Jika pull request Anda menunjukkan konflik merge, pastikan untuk memperbarui local main Anda agar mencerminkan apa yang ada di repositori utama sebelum melakukan modifikasi
* Jika Anda mengirimkan terjemahan, harap buat satu PR untuk semua file terjemahan karena kami tidak menerima terjemahan sebagian untuk konten tersebut
* Jika Anda mengirimkan perbaikan typo atau dokumentasi, Anda dapat menggabungkan modifikasi ke satu PR jika sesuai

## Ruang lingkup editorial dan produk pihak ketiga

Kurikulum ini fokus pada teknologi Microsoft dan standar terbuka netral vendor. Kontribusi harus memiliki tujuan edukasi yang jelas dan tidak boleh terutama dimaksudkan untuk memperkenalkan atau mempromosikan produk komersial pihak ketiga, layanan hosting, model router, SDK, server MCP, atau penawaran spesifik vendor lainnya.

Perangkat lunak sumber terbuka dan ketergantungan pihak ketiga dapat dirujuk ketika diperlukan untuk menjelaskan standar terbuka atau skenario interoperabilitas, disajikan secara netral, dan tidak berpusat pada produk vendor atau titik akhir hosting. Jika kontribusi yang Anda usulkan mencakup produk atau layanan spesifik vendor, buka isu dan dapatkan persetujuan pemelihara sebelum mengirimkan pull request.

Kontributor harus mengungkapkan setiap hubungan kerja, kepemilikan, sponsor, atau afiliasi lain yang relevan dengan produk atau layanan yang dirujuk dalam kontribusi mereka. Jangan sertakan klaim harga, kinerja, keamanan, privasi, atau perbandingan yang tidak didukung. Contoh yang dapat dijalankan tidak boleh mengirim data pembelajar atau melakukan aksi publik melalui layanan pihak ketiga eksternal secara default.

## Panduan Umum untuk menulis

- Pastikan semua URL Anda dibungkus dalam tanda kurung siku diikuti tanda kurung biasa tanpa spasi ekstra di sekitarnya atau di dalamnya `[]()`.
- Pastikan setiap tautan relatif (misalnya tautan ke file dan folder lain dalam repositori) dimulai dengan `./` yang merujuk ke file atau folder yang berada di direktori kerja saat ini atau `../` yang merujuk ke file atau folder yang berada di direktori induk.
- Pastikan setiap tautan relatif (misalnya tautan ke file dan folder lain dalam repositori) memiliki ID pelacakan (misalnya `?` atau `&` lalu `wt.mc_id=` atau `WT.mc_id=`) di akhir tautan.
- Pastikan setiap URL dari domain berikut _github.com, microsoft.com, visualstudio.com, aka.ms, dan azure.com_ memiliki ID pelacakan (misalnya `?` atau `&` lalu `wt.mc_id=` atau `WT.mc_id=`) di akhir URL.
- Pastikan tautan Anda tidak memiliki lokal negara tertentu (misalnya `/en-us/` atau `/en/`).
- Pastikan semua gambar disimpan di folder `./images`.
- Pastikan gambar memiliki nama deskriptif menggunakan karakter bahasa Inggris, angka, dan tanda hubung dalam nama gambar Anda.

## Alur Kerja GitHub

Saat Anda mengirimkan pull request, empat alur kerja berbeda akan dipicu untuk memvalidasi aturan sebelumnya.
Cukup ikuti instruksi yang tercantum di sini untuk melewati pemeriksaan alur kerja.

- [Periksa Jalur Relatif Rusak](#check-broken-relative-paths)
- [Periksa Path Memiliki Pelacakan](#check-paths-have-tracking)
- [Periksa URL Memiliki Pelacakan](#check-urls-have-tracking)
- [Periksa URL Tidak Memiliki Lokal](#check-urls-dont-have-locale)

### Periksa Jalur Relatif Rusak

Alur kerja ini memastikan bahwa setiap jalur relatif dalam file Anda berfungsi.
Repositori ini dideploy ke halaman GitHub sehingga Anda harus sangat berhati-hati saat mengetik tautan yang mengikat semuanya agar tidak mengarahkan siapa pun ke tempat yang salah.

Untuk memastikan tautan Anda berfungsi dengan baik, cukup gunakan VS code untuk memeriksanya.

Misalnya, saat Anda mengarahkan kursor ke atas tautan mana pun di file Anda, Anda akan diminta mengikuti tautan dengan menekan **ctrl + klik**

![Screenshot ikuti tautan di VS code](../../translated_images/id/vscode-follow-link.85520ab6a1237adc.webp?WT.mc_id=academic-105485-koreyst "Screenshot dari prompt vs code untuk mengikuti tautan saat kursor diarahkan ke tautan.")

Jika Anda mengklik tautan dan itu tidak berfungsi secara lokal maka, pasti akan memicu alur kerja dan tidak akan berfungsi di GitHub.

Untuk memperbaiki masalah ini, coba ketik tautan dengan bantuan VS code.

Saat Anda mengetik `./` atau `../` VS code akan meminta Anda memilih dari opsi yang tersedia sesuai apa yang Anda ketik.

![Screenshot pilih jalur relatif di VS code](../../translated_images/id/vscode-select-relative-path.3804eb73c3a9e5f2.webp?WT.mc_id=academic-105485-koreyst "Screenshot dari prompt vs code untuk memilih jalur relatif dari daftar pop up.")

Ikuti jalur dengan mengklik file atau folder yang diinginkan dan Anda akan yakin bahwa jalur Anda tidak rusak.

Setelah Anda menambahkan jalur relatif yang benar, simpan, dan dorong perubahan Anda, alur kerja akan dipicu lagi untuk memverifikasi perubahan Anda.
Jika Anda lulus pemeriksaan maka Anda siap melanjutkan.

### Periksa Path Memiliki Pelacakan

Alur kerja ini memastikan bahwa setiap jalur relatif memiliki pelacakan di dalamnya.
Repositori ini dideploy ke halaman GitHub jadi kita perlu melacak perpindahan antar file dan folder.

Untuk memastikan jalur relatif Anda memiliki pelacakan di dalamnya cukup periksa teks berikut `?wt.mc_id=` di akhir jalur.
Jika teks tersebut ditambahkan ke jalur relatif Anda, maka Anda akan lulus pemeriksaan ini.

Jika tidak, Anda mungkin mendapatkan kesalahan berikut.

![Screenshot komentar github cek jalur hilang pelacakan](../../translated_images/id/github-check-paths-missing-tracking-comment.880d4afe03e898ff.webp?WT.mc_id=academic-105485-koreyst "Screenshot komentar github yang menunjukkan hilangnya pelacakan dari jalur relatif")

Untuk memperbaiki masalah ini, coba buka jalur file yang disorot oleh alur kerja dan tambahkan ID pelacakan ke akhir jalur relatif.

Setelah Anda menambahkan ID pelacakan, simpan, dan dorong perubahan Anda alur kerja akan dipicu lagi untuk memverifikasi perubahan Anda.
Jika Anda lulus pemeriksaan maka Anda siap melanjutkan.

### Periksa URL Memiliki Pelacakan

Alur kerja ini memastikan bahwa setiap URL web memiliki pelacakan di dalamnya.
Repositori ini tersedia untuk semua orang sehingga Anda harus memastikan melacak akses untuk mengetahui dari mana lalu lintas berasal.

Untuk memastikan URL Anda memiliki pelacakan di dalamnya cukup periksa teks berikut `?wt.mc_id=` di akhir URL.
Jika teks tersebut ditambahkan ke URL Anda maka Anda akan lulus pemeriksaan ini.

Jika tidak, Anda mungkin mendapatkan kesalahan berikut.

![Screenshot komentar github cek url hilang pelacakan](../../translated_images/id/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e.webp?WT.mc_id=academic-105485-koreyst "Screenshot komentar github yang menunjukkan hilangnya pelacakan dari url")

Untuk memperbaiki masalah ini, coba buka jalur file yang disorot oleh alur kerja dan tambahkan ID pelacakan ke akhir URL.

Setelah Anda menambahkan ID pelacakan, simpan, dan dorong perubahan Anda alur kerja akan dipicu lagi untuk memverifikasi perubahan Anda.
Jika Anda lulus pemeriksaan maka Anda siap melanjutkan.

### Periksa URL Tidak Memiliki Lokal

Alur kerja ini memastikan bahwa setiap URL web tidak memiliki lokal negara tertentu di dalamnya.
Repositori ini tersedia untuk semua orang di seluruh dunia sehingga Anda harus memastikan untuk tidak menyertakan lokal negara Anda dalam URL.

Untuk memastikan URL Anda tidak memiliki lokal negara, cukup periksa teks berikut `/en-us/` atau `/en/` atau lokal bahasa lain di mana pun dalam URL.
Jika tidak ada dalam URL Anda maka Anda akan lulus pemeriksaan ini.

Jika tidak, Anda mungkin mendapatkan kesalahan berikut.

![Screenshot komentar github cek lokal negara pada url](../../translated_images/id/github-check-country-locale-comment.2f4fe93228161dee.webp?WT.mc_id=academic-105485-koreyst "Screenshot komentar github yang menunjukkan penambahan lokal negara pada url")

Untuk memperbaiki masalah ini, coba buka jalur file yang disorot oleh alur kerja dan hapus lokal negara dari URL.

Setelah Anda menghapus lokal negara, simpan, dan dorong perubahan Anda alur kerja akan dipicu lagi untuk memverifikasi perubahan Anda.
Jika Anda lulus pemeriksaan maka Anda siap melanjutkan.

Selamat! Kami akan segera menghubungi Anda dengan umpan balik tentang kontribusi Anda.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->