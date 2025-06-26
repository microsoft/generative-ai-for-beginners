<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "57c41f2af71001a2cff9d8eb797cb843",
  "translation_date": "2025-06-25T07:15:36+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "id"
}
-->
# Berkontribusi

Proyek ini menyambut kontribusi dan saran. Sebagian besar kontribusi mengharuskan Anda menyetujui Perjanjian Lisensi Kontributor (CLA) yang menyatakan bahwa Anda memiliki hak untuk, dan benar-benar memberikan kami hak untuk menggunakan kontribusi Anda. Untuk detail lebih lanjut, kunjungi <https://cla.microsoft.com>.

> Penting: saat menerjemahkan teks dalam repo ini, pastikan Anda tidak menggunakan terjemahan mesin. Kami akan memverifikasi terjemahan melalui komunitas, jadi silakan hanya menjadi sukarelawan untuk terjemahan dalam bahasa yang Anda kuasai.

Ketika Anda mengajukan pull request, CLA-bot akan secara otomatis menentukan apakah Anda perlu memberikan CLA dan mendekorasi PR sesuai (misalnya, label, komentar). Cukup ikuti instruksi yang diberikan oleh bot. Anda hanya perlu melakukan ini sekali di semua repositori yang menggunakan CLA kami.

## Kode Etik

Proyek ini telah mengadopsi [Kode Etik Sumber Terbuka Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Untuk informasi lebih lanjut, baca [FAQ Kode Etik](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) atau hubungi [opencode@microsoft.com](mailto:opencode@microsoft.com) dengan pertanyaan atau komentar tambahan.

## Pertanyaan atau Masalah?

Jangan membuka masalah GitHub untuk pertanyaan dukungan umum karena daftar GitHub harus digunakan untuk permintaan fitur dan laporan bug. Dengan cara ini kami dapat lebih mudah melacak masalah atau bug aktual dari kode dan menjaga diskusi umum terpisah dari kode sebenarnya.

## Kesalahan Ketik, Masalah, Bug, dan Kontribusi

Setiap kali Anda mengajukan perubahan ke repositori Generative AI for Beginners, harap ikuti rekomendasi ini.

* Selalu fork repositori ke akun Anda sendiri sebelum membuat modifikasi
* Jangan gabungkan beberapa perubahan ke satu pull request. Misalnya, ajukan perbaikan bug dan pembaruan dokumentasi menggunakan PR terpisah
* Jika pull request Anda menunjukkan konflik penggabungan, pastikan untuk memperbarui main lokal Anda agar menjadi cermin dari yang ada di repositori utama sebelum membuat modifikasi
* Jika Anda mengajukan terjemahan, harap buat satu PR untuk semua file yang diterjemahkan karena kami tidak menerima terjemahan parsial untuk konten
* Jika Anda mengajukan perbaikan kesalahan ketik atau dokumentasi, Anda dapat menggabungkan modifikasi ke satu PR jika sesuai

## Panduan Umum untuk Penulisan

- Pastikan semua URL Anda dibungkus dalam tanda kurung siku diikuti oleh tanda kurung tanpa spasi tambahan di sekitarnya atau di dalamnya `[](../..)`.
- Pastikan setiap tautan relatif (yaitu tautan ke file dan folder lain dalam repositori) dimulai dengan `./` merujuk ke file atau folder yang terletak di direktori kerja saat ini atau `../` merujuk ke file atau folder yang terletak di direktori kerja induk.
- Pastikan setiap tautan relatif (yaitu tautan ke file dan folder lain dalam repositori) memiliki ID pelacakan (yaitu `?` atau `&` kemudian `wt.mc_id=` atau `WT.mc_id=`) di akhir.
- Pastikan setiap URL dari domain berikut _github.com, microsoft.com, visualstudio.com, aka.ms, dan azure.com_ memiliki ID pelacakan (yaitu `?` atau `&` kemudian `wt.mc_id=` atau `WT.mc_id=`) di akhir.
- Pastikan tautan Anda tidak memiliki lokal khusus negara di dalamnya (yaitu `/en-us/` atau `/en/`).
- Pastikan semua gambar disimpan di folder `./images`.
- Pastikan gambar memiliki nama deskriptif menggunakan karakter Inggris, angka, dan tanda hubung dalam nama gambar Anda.

## Alur Kerja GitHub

Ketika Anda mengajukan pull request, empat alur kerja berbeda akan dipicu untuk memvalidasi aturan sebelumnya.
Cukup ikuti instruksi yang tercantum di sini untuk lulus pemeriksaan alur kerja.

- [Periksa Jalur Relatif Rusak](../..)
- [Periksa Jalur Memiliki Pelacakan](../..)
- [Periksa URL Memiliki Pelacakan](../..)
- [Periksa URL Tidak Memiliki Lokal](../..)

### Periksa Jalur Relatif Rusak

Alur kerja ini memastikan bahwa setiap jalur relatif dalam file Anda berfungsi.
Repositori ini diterapkan ke halaman GitHub sehingga Anda perlu sangat berhati-hati saat mengetik tautan yang menyatukan semuanya agar tidak mengarahkan siapa pun ke tempat yang salah.

Untuk memastikan tautan Anda berfungsi dengan baik, cukup gunakan kode VS untuk memeriksa.

Misalnya, saat Anda mengarahkan mouse ke tautan apa pun dalam file Anda, Anda akan diminta untuk mengikuti tautan dengan menekan **ctrl + klik**

![Cuplikan layar ikuti tautan VS code](../../translated_images/vscode-follow-link.85520ab6a1237adcf01cc9cd8c228ce7b32ae685a034250bd5109e2682b9dfca.id.png)

Jika Anda mengklik tautan dan tidak berfungsi secara lokal, maka alur kerja pasti akan dipicu dan tidak akan berfungsi di GitHub.

Untuk memperbaiki masalah ini, coba ketik tautan dengan bantuan kode VS.

Saat Anda mengetik `./` atau `../` kode VS akan meminta Anda memilih dari opsi yang tersedia sesuai dengan apa yang Anda ketik.

![Cuplikan layar pilih jalur relatif VS code](../../translated_images/vscode-select-relative-path.3804eb73c3a9e5f2d345e3d3288f8173a9e584254d0e505d8bcbc6461dbf1f6c.id.png)

Ikuti jalur dengan mengklik file atau folder yang diinginkan dan Anda akan yakin bahwa jalur Anda tidak rusak.

Setelah Anda menambahkan jalur relatif yang benar, simpan, dan dorong perubahan Anda, alur kerja akan dipicu lagi untuk memverifikasi perubahan Anda.
Jika Anda lulus pemeriksaan maka Anda siap untuk melanjutkan.

### Periksa Jalur Memiliki Pelacakan

Alur kerja ini memastikan bahwa setiap jalur relatif memiliki pelacakan di dalamnya.
Repositori ini diterapkan ke halaman GitHub sehingga kita perlu melacak pergerakan antara file dan folder yang berbeda.

Untuk memastikan jalur relatif Anda memiliki pelacakan di dalamnya, cukup periksa teks berikut `?wt.mc_id=` di akhir jalur.
Jika teks ini ditambahkan ke jalur relatif Anda, maka Anda akan lulus pemeriksaan ini.

Jika tidak, Anda mungkin mendapatkan kesalahan berikut.

![Cuplikan layar komentar jalur kehilangan pelacakan GitHub](../../translated_images/github-check-paths-missing-tracking-comment.880d4afe03e898ffadeebe0f61f7fdea7525c25238bead9fecabc81a0a83b1c0.id.png)

Untuk memperbaiki masalah ini, coba buka jalur file yang disorot oleh alur kerja dan tambahkan ID pelacakan ke akhir jalur relatif.

Setelah Anda menambahkan ID pelacakan, simpan, dan dorong perubahan Anda, alur kerja akan dipicu lagi untuk memverifikasi perubahan Anda.
Jika Anda lulus pemeriksaan maka Anda siap untuk melanjutkan.

### Periksa URL Memiliki Pelacakan

Alur kerja ini memastikan bahwa setiap URL web memiliki pelacakan di dalamnya.
Repositori ini tersedia untuk semua orang sehingga Anda perlu memastikan untuk melacak akses untuk mengetahui dari mana lalu lintas berasal.

Untuk memastikan URL Anda memiliki pelacakan di dalamnya, cukup periksa teks berikut `?wt.mc_id=` di akhir URL.
Jika teks ini ditambahkan ke URL Anda, maka Anda akan lulus pemeriksaan ini.

Jika tidak, Anda mungkin mendapatkan kesalahan berikut.

![Cuplikan layar komentar URL kehilangan pelacakan GitHub](../../translated_images/github-check-urls-missing-tracking-comment.1bd00d20b24a1e2e3179e59e1bd7d44f16637a1bb1ab265562565251166841ef.id.png)

Untuk memperbaiki masalah ini, coba buka jalur file yang disorot oleh alur kerja dan tambahkan ID pelacakan ke akhir URL.

Setelah Anda menambahkan ID pelacakan, simpan, dan dorong perubahan Anda, alur kerja akan dipicu lagi untuk memverifikasi perubahan Anda.
Jika Anda lulus pemeriksaan maka Anda siap untuk melanjutkan.

### Periksa URL Tidak Memiliki Lokal

Alur kerja ini memastikan bahwa setiap URL web tidak memiliki lokal khusus negara di dalamnya.
Repositori ini tersedia untuk semua orang di seluruh dunia sehingga Anda perlu memastikan untuk tidak menyertakan lokal negara Anda dalam URL.

Untuk memastikan URL Anda tidak memiliki lokal negara di dalamnya, cukup periksa teks berikut `/en-us/` atau `/en/` atau lokal bahasa lainnya di mana saja dalam URL.
Jika teks ini tidak ada dalam URL Anda, maka Anda akan lulus pemeriksaan ini.

Jika tidak, Anda mungkin mendapatkan kesalahan berikut.

![Cuplikan layar komentar lokal negara GitHub](../../translated_images/github-check-country-locale-comment.2f4fe93228161dee6ec8210f3d6ccc66af6864f6b178b8d96f30818498fba72a.id.png)

Untuk memperbaiki masalah ini, coba buka jalur file yang disorot oleh alur kerja dan hapus lokal negara dari URL.

Setelah Anda menghapus lokal negara, simpan, dan dorong perubahan Anda, alur kerja akan dipicu lagi untuk memverifikasi perubahan Anda.
Jika Anda lulus pemeriksaan maka Anda siap untuk melanjutkan.

Selamat! Kami akan segera menghubungi Anda dengan umpan balik tentang kontribusi Anda.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk mencapai ketepatan, harap disadari bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi penting, disarankan menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.