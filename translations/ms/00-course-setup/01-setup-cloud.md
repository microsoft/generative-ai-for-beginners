<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T18:21:23+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "ms"
}
-->
# Persediaan Cloud ☁️ – GitHub Codespaces

**Guna panduan ini jika anda tidak mahu memasang apa-apa secara lokal.**  
Codespaces membolehkan anda menggunakan VS Code berasaskan pelayar secara percuma, dengan semua keperluan sudah dipasang.

---

## 1.  Kenapa Codespaces?

| Kelebihan | Apa maksudnya untuk anda |
|-----------|-------------------------|
| ✅ Tiada pemasangan | Berfungsi di Chromebook, iPad, PC makmal sekolah… |
| ✅ Kontena pembangunan siap sedia | Python 3, Node.js, .NET, Java sudah tersedia |
| ✅ Kuota percuma | Akaun peribadi dapat **120 jam-teras / 60 GB-jam sebulan** |

> 💡 **Tip**  
> Pastikan kuota anda sentiasa cukup dengan **memberhentikan** atau **memadam** codespace yang tidak digunakan  
> (View ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Cipta Codespace (satu klik)

1. **Fork** repo ini (butang **Fork** di kanan atas).  
2. Dalam fork anda, klik **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![ialog showing buttons to create a codespace](../../../00-course-setup/images/who-will-pay.webp)

✅ Tetingkap VS Code dalam pelayar akan dibuka dan kontena pembangunan mula dibina.
Proses ini mengambil masa **~2 minit** untuk kali pertama.

## 3. Tambah kunci API anda (cara selamat)

### Pilihan A Rahsia Codespaces — Disyorkan

1. Ikon ⚙️ -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Nama: OPENAI_API_KEY
3. Nilai: tampal kunci anda → Add secret

Itu sahaja—kod kita akan mengesan secara automatik.

### Pilihan B Fail .env (jika anda benar-benar perlukan)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.