# Pengaturan Cloud ☁️ – GitHub Codespaces

**Gunakan panduan ini jika Anda tidak ingin menginstal apa pun secara lokal.**  
Codespaces memberi Anda instance VS Code berbasis browser gratis dengan semua dependensi sudah terpasang.

---

## 1.  Mengapa Codespaces?

| Manfaat | Apa artinya untuk Anda |
|---------|----------------------|
| ✅ Tanpa instalasi | Berfungsi di Chromebook, iPad, PC lab sekolah… |
| ✅ Kontainer dev pra-bangun | Python 3, Node.js, .NET, Java sudah termasuk |
| ✅ Kuota gratis | Akun pribadi mendapatkan **120 core-hours / 60 GB-hours per bulan** |

> 💡 **Tip**  
> Jaga kesehatan kuota Anda dengan **menghentikan** atau **menghapus** codespaces yang tidak aktif  
> (Lihat ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Membuat Codespace (satu klik)

1. **Fork** repo ini (tombol **Fork** kanan atas).  
2. Di fork Anda, klik **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialog showing buttons to create a codespace](../../../translated_images/id/who-will-pay.4c0609b1c7780f44.webp)

✅ Jendela VS Code di browser terbuka dan kontainer dev mulai dibuat.
Ini memakan waktu sekitar **~2 menit** untuk pertama kali.

## 3. Tambahkan kunci API Anda (dengan cara aman)

### Opsi A Rahasia Codespaces — Direkomendasikan

1. ⚙️ Ikon gear -> Command Palette -> Codespaces : Manage user secret -> Tambah rahasia baru.
2. Nama: OPENAI_API_KEY
3. Nilai: tempel kunci Anda → Tambah rahasia

Selesai—kode kami akan mengaksesnya secara otomatis.

### Opsi B file .env (jika benar-benar diperlukan)

```bash
cp .env.copy .env
code .env         # isi dengan OPENAI_API_KEY=kunci_anda_di_sini
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->