<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T18:15:22+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "id"
}
-->
# Memilih & Mengonfigurasi Penyedia LLM 🔑

Tugas **bisa** juga diatur untuk bekerja dengan satu atau lebih deployment Large Language Model (LLM) melalui penyedia layanan yang didukung seperti OpenAI, Azure, atau Hugging Face. Penyedia ini menawarkan _hosted endpoint_ (API) yang bisa kita akses secara programatis dengan kredensial yang sesuai (API key atau token). Di kursus ini, kita membahas penyedia berikut:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) dengan berbagai model termasuk seri inti GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) untuk model OpenAI dengan fokus pada kesiapan enterprise
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) untuk model open-source dan inference server

**Kamu perlu menggunakan akunmu sendiri untuk latihan ini**. Tugas bersifat opsional, jadi kamu bisa memilih untuk mengatur satu, semua, atau tidak sama sekali penyedia sesuai minatmu. Berikut beberapa panduan untuk pendaftaran:

| Daftar | Biaya | API Key | Playground | Komentar |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Harga](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Berdasarkan Proyek](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Tanpa Kode, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Tersedia Banyak Model |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Harga](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Harus Ajukan Akses Terlebih Dahulu](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Harga](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Model di Hugging Chat terbatas](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Ikuti petunjuk di bawah untuk _mengonfigurasi_ repository ini agar bisa digunakan dengan berbagai penyedia. Tugas yang membutuhkan penyedia tertentu akan memiliki salah satu tag berikut di nama filenya:

- `aoai` - membutuhkan endpoint dan key Azure OpenAI
- `oai` - membutuhkan endpoint dan key OpenAI
- `hf` - membutuhkan token Hugging Face

Kamu bisa mengonfigurasi satu, tidak sama sekali, atau semua penyedia. Tugas terkait akan error jika kredensial tidak tersedia.

## Membuat file `.env`

Kami mengasumsikan kamu sudah membaca panduan di atas, mendaftar ke penyedia yang relevan, dan mendapatkan kredensial autentikasi yang dibutuhkan (API_KEY atau token). Untuk Azure OpenAI, kami juga mengasumsikan kamu sudah memiliki deployment Azure OpenAI Service (endpoint) yang valid dengan minimal satu model GPT yang sudah dideploy untuk chat completion.

Langkah selanjutnya adalah mengonfigurasi **environment variable lokal** seperti berikut:

1. Cari file `.env.copy` di folder root yang seharusnya berisi seperti ini:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Salin file tersebut menjadi `.env` dengan perintah di bawah. File ini sudah _gitignore_, jadi rahasia tetap aman.

   ```bash
   cp .env.copy .env
   ```

3. Isi nilai-nilainya (ganti placeholder di sisi kanan `=`) sesuai penjelasan di bagian berikutnya.

4. (Opsional) Jika kamu menggunakan GitHub Codespaces, kamu bisa menyimpan environment variable sebagai _Codespaces secrets_ yang terhubung dengan repository ini. Dengan cara ini, kamu tidak perlu mengatur file .env lokal. **Namun, opsi ini hanya berlaku jika kamu menggunakan GitHub Codespaces.** Kamu tetap perlu mengatur file .env jika menggunakan Docker Desktop.

## Mengisi file `.env`

Mari kita lihat nama variabelnya agar paham fungsinya:

| Variabel  | Deskripsi  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ini adalah access token pengguna yang kamu atur di profilmu |
| OPENAI_API_KEY | Ini adalah key otorisasi untuk menggunakan layanan endpoint OpenAI non-Azure |
| AZURE_OPENAI_API_KEY | Ini adalah key otorisasi untuk menggunakan layanan tersebut |
| AZURE_OPENAI_ENDPOINT | Ini adalah endpoint yang sudah dideploy untuk resource Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Ini adalah endpoint deployment model _text generation_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ini adalah endpoint deployment model _text embeddings_ |
| | |

Catatan: Dua variabel Azure OpenAI terakhir merepresentasikan model default untuk chat completion (text generation) dan pencarian vektor (embeddings). Instruksi pengaturannya akan dijelaskan di tugas terkait.

## Konfigurasi Azure: Dari Portal

Nilai endpoint dan key Azure OpenAI bisa ditemukan di [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), jadi mari mulai dari sana.

1. Buka [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klik opsi **Keys and Endpoint** di sidebar (menu kiri).
1. Klik **Show Keys** - kamu akan melihat: KEY 1, KEY 2, dan Endpoint.
1. Gunakan nilai KEY 1 untuk AZURE_OPENAI_API_KEY
1. Gunakan nilai Endpoint untuk AZURE_OPENAI_ENDPOINT

Selanjutnya, kita butuh endpoint untuk model spesifik yang sudah dideploy.

1. Klik opsi **Model deployments** di sidebar (menu kiri) untuk resource Azure OpenAI.
1. Di halaman tujuan, klik **Manage Deployments**

Ini akan membawamu ke website Azure OpenAI Studio, di mana kita akan menemukan nilai lain seperti dijelaskan di bawah.

## Konfigurasi Azure: Dari Studio

1. Akses [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **dari resource-mu** seperti dijelaskan di atas.
1. Klik tab **Deployments** (sidebar kiri) untuk melihat model yang sudah dideploy.
1. Jika model yang diinginkan belum dideploy, gunakan **Create new deployment** untuk mendeply-nya.
1. Kamu butuh model _text-generation_ - kami rekomendasikan: **gpt-35-turbo**
1. Kamu butuh model _text-embedding_ - kami rekomendasikan **text-embedding-ada-002**

Sekarang, update environment variable sesuai _Deployment name_ yang digunakan. Biasanya sama dengan nama model kecuali kamu mengubahnya. Sebagai contoh, kamu mungkin punya:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Jangan lupa simpan file .env setelah selesai**. Kamu bisa keluar dari file dan kembali ke instruksi menjalankan notebook.

## Konfigurasi OpenAI: Dari Profil

API key OpenAI-mu bisa ditemukan di [akun OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jika belum punya, kamu bisa daftar akun dan membuat API key. Setelah punya key-nya, gunakan untuk mengisi variabel `OPENAI_API_KEY` di file `.env`.

## Konfigurasi Hugging Face: Dari Profil

Token Hugging Face-mu bisa ditemukan di profil pada bagian [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Jangan posting atau bagikan token ini secara publik. Sebaiknya buat token baru khusus untuk proyek ini dan salin ke file `.env` di variabel `HUGGING_FACE_API_KEY`. _Catatan:_ Secara teknis ini bukan API key, tapi digunakan untuk autentikasi jadi penamaan tetap dipakai agar konsisten.

---

**Disclaimer**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan terjemahan yang akurat, harap diketahui bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemah profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.