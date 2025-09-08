<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T18:14:53+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "id"
}
-->
# Cloud Setup ☁️ – GitHub Codespaces

**Gunakan panduan ini jika kamu tidak ingin menginstal apa pun di komputer lokal.**  
Codespaces memberikanmu VS Code berbasis browser secara gratis dengan semua dependensi sudah terpasang.

---

## 1.  Kenapa Codespaces?

| Keuntungan | Artinya untukmu |
|------------|-----------------|
| ✅ Tanpa instalasi | Bisa digunakan di Chromebook, iPad, PC lab sekolah… |
| ✅ Dev container sudah siap pakai | Python 3, Node.js, .NET, Java sudah tersedia di dalamnya |
| ✅ Kuota gratis | Akun personal mendapat **120 core-jam / 60 GB-jam per bulan** |

> 💡 **Tip**  
> Jaga kuotamu tetap aman dengan **menghentikan** atau **menghapus** codespace yang tidak digunakan  
> (View ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Buat Codespace (satu klik)

1. **Fork** repo ini (tombol **Fork** di kanan atas).  
2. Di repo hasil fork, klik **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![ialog showing buttons to create a codespace](../../../00-course-setup/images/who-will-pay.webp)

✅ Jendela VS Code di browser akan terbuka dan dev container mulai dibangun.
Proses ini memakan waktu **sekitar 2 menit** untuk pertama kali.

## 3. Tambahkan API key-mu (cara aman)

### Opsi A Codespaces Secrets — Direkomendasikan

1. ⚙️ Ikon gear -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Nama: OPENAI_API_KEY
3. Nilai: tempelkan key-mu → Add secret

Selesai—kode kita akan otomatis mendeteksinya.

### Opsi B File .env (jika memang perlu)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Disclaimer**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan terjemahan yang akurat, harap diketahui bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemah profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.