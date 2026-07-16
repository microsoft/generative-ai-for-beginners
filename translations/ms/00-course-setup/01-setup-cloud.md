# Persediaan Awan ☁️ – GitHub Codespaces

**Gunakan panduan ini jika anda tidak mahu memasang apa-apa secara tempatan.**  
Codespaces memberi anda contoh VS Code berasaskan pelayar yang percuma dengan semua kebergantungan telah dipasang.

---

## 1.  Mengapa Codespaces?

| Manfaat | Apa maksudnya untuk anda |
|---------|----------------------|
| ✅ Tiada pemasangan | Berfungsi pada Chromebook, iPad, PC makmal sekolah… |
| ✅ Kontena dev siap sedia | Python 3, Node.js, .NET, Java sudah tersedia |
| ✅ Kuota percuma | Akaun peribadi dapat **120 jam teras / 60 GB-jam sebulan** |

> 💡 **Petua**  
> Kekalkan kuota anda dengan **menghentikan** atau **menghapus** codespaces yang tidak aktif  
> (Lihat ▸ Palet Perintah ▸ *Codespaces: Stop Codespace*).

---

## 2.  Cipta Codespace (satu klik)

1. **Fork** repositori ini (butang **Fork** di atas kanan).  
2. Dalam fork anda, klik **Kod ▸ Codespaces ▸ Buat codespace pada main**.  
   ![Dialog menunjukkan butang untuk mencipta codespace](../../../translated_images/ms/who-will-pay.4c0609b1c7780f44.webp)

✅ Tetingkap VS Code dalam pelayar akan dibuka dan kontena dev mula dibina.
Ini mengambil masa **~2 minit** kali pertama.

## 3. Tambah kunci API anda (cara selamat)

### Pilihan A Rahsia Codespaces — Disyorkan

1. ⚙️ Ikon gear -> Palet Perintah -> Codespaces : Urus rahsia pengguna -> Tambah rahsia baru.
2. Nama: OPENAI_API_KEY
3. Nilai: tampal kunci anda → Tambah rahsia

Itu sahaja—kod kami akan mengambilnya secara automatik.

### Pilihan B fail .env (jika anda benar-benar memerlukan)

```bash
cp .env.copy .env
code .env         # isi OPENAI_API_KEY=kunci_anda_di_sini
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->