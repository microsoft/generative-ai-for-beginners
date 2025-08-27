<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T18:21:49+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "ms"
}
-->
# Memilih & Mengkonfigurasi Penyedia LLM 🔑

Tugasan **mungkin** juga boleh disediakan untuk digunakan dengan satu atau lebih deployment Model Bahasa Besar (LLM) melalui penyedia servis yang disokong seperti OpenAI, Azure atau Hugging Face. Penyedia ini menawarkan _endpoint yang dihoskan_ (API) yang boleh diakses secara programatik dengan kelayakan yang betul (kunci API atau token). Dalam kursus ini, kita bincangkan penyedia berikut:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) dengan pelbagai model termasuk siri teras GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) untuk model OpenAI dengan fokus pada kesediaan perusahaan
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) untuk model sumber terbuka dan pelayan inferens

**Anda perlu menggunakan akaun sendiri untuk latihan ini**. Tugasan adalah pilihan, jadi anda boleh pilih untuk menyediakan satu, semua - atau tiada - penyedia mengikut minat anda. Beberapa panduan untuk pendaftaran:

| Daftar | Kos | Kunci API | Playground | Komen |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Harga](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Berdasarkan Projek](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Tanpa Kod, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Pelbagai Model Tersedia |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Harga](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Perlu Mohon Awal Untuk Akses](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Harga](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat hanya ada model terhad](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Ikuti arahan di bawah untuk _mengkonfigurasi_ repositori ini supaya boleh digunakan dengan pelbagai penyedia. Tugasan yang memerlukan penyedia tertentu akan mengandungi salah satu tag ini dalam nama failnya:

- `aoai` - memerlukan endpoint dan kunci Azure OpenAI
- `oai` - memerlukan endpoint dan kunci OpenAI
- `hf` - memerlukan token Hugging Face

Anda boleh konfigur satu, tiada, atau semua penyedia. Tugasan berkaitan akan gagal jika kelayakan tidak disediakan.

## Cipta fail `.env`

Kami anggap anda sudah baca panduan di atas dan telah mendaftar dengan penyedia yang berkaitan, serta dapatkan kelayakan pengesahan yang diperlukan (API_KEY atau token). Untuk Azure OpenAI, kami anggap anda juga sudah ada deployment Azure OpenAI Service (endpoint) yang sah dengan sekurang-kurangnya satu model GPT yang telah dideploy untuk chat completion.

Langkah seterusnya ialah mengkonfigurasi **pembolehubah persekitaran tempatan** anda seperti berikut:

1. Cari fail `.env.copy` dalam folder root yang sepatutnya mengandungi kandungan seperti ini:

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

2. Salin fail itu ke `.env` menggunakan arahan di bawah. Fail ini _diabaikan oleh git_, jadi rahsia anda selamat.

   ```bash
   cp .env.copy .env
   ```

3. Isikan nilai (gantikan placeholder di sebelah kanan `=`) seperti yang diterangkan dalam bahagian seterusnya.

4. (Pilihan) Jika anda guna GitHub Codespaces, anda boleh simpan pembolehubah persekitaran sebagai _Codespaces secrets_ yang dikaitkan dengan repositori ini. Dalam kes ini, anda tidak perlu sediakan fail .env secara tempatan. **Namun, pilihan ini hanya berfungsi jika anda guna GitHub Codespaces.** Anda masih perlu sediakan fail .env jika anda guna Docker Desktop.

## Isi fail `.env`

Mari kita lihat nama pembolehubah untuk faham apa yang diwakili:

| Pembolehubah  | Penerangan  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Ini ialah token akses pengguna yang anda sediakan dalam profil anda |
| OPENAI_API_KEY | Ini ialah kunci pengesahan untuk menggunakan servis bagi endpoint OpenAI bukan Azure |
| AZURE_OPENAI_API_KEY | Ini ialah kunci pengesahan untuk menggunakan servis tersebut |
| AZURE_OPENAI_ENDPOINT | Ini ialah endpoint yang telah dideploy untuk sumber Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Ini ialah endpoint deployment model _penjanaan teks_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Ini ialah endpoint deployment model _embedding teks_ |
| | |

Nota: Dua pembolehubah terakhir Azure OpenAI merujuk kepada model lalai untuk chat completion (penjanaan teks) dan carian vektor (embedding) masing-masing. Arahan untuk menetapkannya akan diberikan dalam tugasan berkaitan.

## Konfigurasi Azure: Dari Portal

Nilai endpoint dan kunci Azure OpenAI boleh didapati dalam [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), jadi mari mula di sana.

1. Pergi ke [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klik pilihan **Keys and Endpoint** di bar sisi (menu kiri).
1. Klik **Show Keys** - anda akan nampak: KEY 1, KEY 2 dan Endpoint.
1. Guna nilai KEY 1 untuk AZURE_OPENAI_API_KEY
1. Guna nilai Endpoint untuk AZURE_OPENAI_ENDPOINT

Seterusnya, kita perlukan endpoint untuk model spesifik yang telah dideploy.

1. Klik pilihan **Model deployments** di bar sisi (menu kiri) untuk sumber Azure OpenAI.
1. Di halaman destinasi, klik **Manage Deployments**

Ini akan membawa anda ke laman web Azure OpenAI Studio, di mana kita akan cari nilai lain seperti yang diterangkan di bawah.

## Konfigurasi Azure: Dari Studio

1. Navigasi ke [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **dari sumber anda** seperti yang diterangkan di atas.
1. Klik tab **Deployments** (bar sisi, kiri) untuk lihat model yang telah dideploy.
1. Jika model yang anda mahu belum dideploy, guna **Create new deployment** untuk deploy.
1. Anda perlukan model _penjanaan teks_ - kami cadangkan: **gpt-35-turbo**
1. Anda perlukan model _embedding teks_ - kami cadangkan **text-embedding-ada-002**

Sekarang kemas kini pembolehubah persekitaran supaya mencerminkan _nama Deployment_ yang digunakan. Biasanya ini sama dengan nama model kecuali anda ubah secara khusus. Sebagai contoh, anda mungkin ada:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Jangan lupa simpan fail .env selepas siap**. Anda kini boleh keluar dari fail dan kembali ke arahan untuk menjalankan notebook.

## Konfigurasi OpenAI: Dari Profil

Kunci API OpenAI anda boleh didapati dalam [akaun OpenAI anda](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Jika anda belum ada, anda boleh daftar akaun dan cipta kunci API. Selepas dapat kunci, anda boleh gunakan untuk isi pembolehubah `OPENAI_API_KEY` dalam fail `.env`.

## Konfigurasi Hugging Face: Dari Profil

Token Hugging Face anda boleh didapati dalam profil anda di bawah [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Jangan siarkan atau kongsi token ini secara terbuka. Sebaliknya, cipta token baru untuk projek ini dan salin ke fail `.env` di bawah pembolehubah `HUGGING_FACE_API_KEY`. _Nota:_ Secara teknikal ini bukan kunci API tetapi digunakan untuk pengesahan jadi kami kekalkan penamaan itu untuk konsistensi.

---

**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.