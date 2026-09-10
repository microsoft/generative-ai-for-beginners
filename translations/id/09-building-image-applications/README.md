# Membangun Aplikasi Generasi Gambar

[![Membangun Aplikasi Generasi Gambar](../../../translated_images/id/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Ada lebih dari sekadar LLMs untuk generasi teks. Anda juga dapat menghasilkan gambar dari deskripsi teks. Gambar sebagai modalitas berguna di MedTech, arsitektur, pariwisata, pengembangan game, pemasaran, dan lainnya. Dalam pelajaran ini kita melihat model **GPT Image** saat ini dan membangun aplikasi generasi gambar.

## Pendahuluan

Generasi gambar memungkinkan Anda mengubah prompt bahasa alami menjadi gambar. Dalam pelajaran ini kita bekerja dengan keluarga model **`gpt-image`** dari OpenAI - generasi model gambar saat ini yang tersedia di **[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)** dan platform OpenAI. Model ini menggantikan model DALL·E lama (DALL·E 2/3 adalah warisan).

Sepanjang pelajaran kita menggunakan startup fiktif, **Edu4All**, yang membangun alat pembelajaran. Tim ingin menghasilkan ilustrasi untuk tugas dan materi belajar.

## Tujuan pembelajaran

Pada akhir pelajaran ini Anda akan bisa:

- Menjelaskan apa itu generasi gambar dan dimana berguna.
- Memahami keluarga model `gpt-image` dan bagaimana bedanya dengan model DALL·E warisan.
- Membangun aplikasi generasi gambar dalam Python (dan TypeScript / .NET).
- Mengedit gambar dan menerapkan pengamanan dengan metaprompt.

## Apa itu generasi gambar?

Model generasi gambar membuat gambar dari prompt teks. Model modern seperti `gpt-image` dibangun dengan teknik transformer + difusi: model mempelajari hubungan antara teks dan gambar selama pelatihan, lalu, diberikan prompt, secara iteratif "menghilangkan noise" menjadi gambar yang cocok dengan deskripsi.

Dua keluarga model gambar yang terkenal adalah:

- **`gpt-image` (OpenAI)** - generasi saat ini, digunakan dalam pelajaran ini. Mendukung generasi teks-ke-gambar dan pengeditan gambar (inpainting dengan masker).
- **Midjourney** - model pihak ketiga populer dengan layanan sendiri dan alur kerja berbasis Discord.

> Model gambar OpenAI lama - **DALL·E 2** dan **DALL·E 3** - adalah model warisan. DALL·E 3 tidak lagi tersedia untuk penempatan baru, dan fitur seperti `create_variation` hanya ada di DALL·E 2. Gunakan model `gpt-image` untuk aplikasi baru.

### Model `gpt-image` mana yang harus saya gunakan?

Di Microsoft Foundry berikut ini adalah **Tersedia Umum**:

| Model | Catatan |
| --- | --- |
| **`gpt-image-2`** | Model gambar terbaru dan paling mampu - default yang direkomendasikan. |
| `gpt-image-1.5` | Tersedia umum; kualitas kuat dengan biaya lebih rendah. |
| `gpt-image-1-mini` | Tersedia umum; tercepat / biaya terendah. |
| `gpt-image-1` | Hanya pratinjau. |

Selalu cek daftar [Foundry image models](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) untuk ketersediaan dan wilayah saat ini.

> **Penting:** model `gpt-image` mengembalikan gambar yang dihasilkan sebagai **base64** (`b64_json`), bukan sebagai URL. Kode Anda mendekode string base64 menjadi bytes dan menyimpannya - tidak ada URL gambar untuk diunduh.

## Persiapan

Anda dapat menjalankan contoh terhadap **Azure OpenAI di Microsoft Foundry** (contoh `aoai-*`) atau **platform OpenAI** (contoh `oai-*`).

### 1. Buat dan tempatkan model

Ikuti panduan [membuat resource](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) untuk membuat resource Microsoft Foundry, lalu tempatkan model gambar - **`gpt-image-2`** direkomendasikan.

### 2. Konfigurasi `.env` Anda

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

Temukan nilai ini di halaman **Deployments** dari resource Anda di [Foundry portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst).

### 3. Install pustaka

Buat `requirements.txt`:

```text
python-dotenv
openai
pillow
```

Kemudian buat dan aktifkan lingkungan virtual dan pasang:

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Bangun aplikasi

Buat `app.py` dengan kode berikut. Ini menghasilkan gambar dan menyimpannya sebagai PNG.

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# Arahkan klien ke sumber daya Azure OpenAI (Microsoft Foundry) Anda.
# Model gambar memerlukan versi API terbaru - periksa dokumen Foundry untuk versi yang dibutuhkan model Anda.
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # misalnya "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # juga 1536x1024 (lanskap), 1024x1536 (potret), atau "otomatis"
    n=1,
)

# model gpt-image mengembalikan base64 (b64_json), bukan URL - dekode menjadi byte.
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

Jalankan dengan `python app.py`. Anda akan mendapatkan PNG yang tersimpan di dalam `images/`.

> Setiap panggilan ke `images.generate` menghasilkan gambar berbeda untuk prompt yang sama - model gambar tidak menggunakan parameter `temperature` (itu kontrol generasi teks). Untuk mendapatkan variasi, cukup panggil API lagi; untuk mengurangi variasi, buat prompt Anda lebih spesifik.

## Mengedit gambar

Model `gpt-image` dapat **mengedit** gambar yang ada: sediakan gambar, **masker** opsional (yang menandai area yang akan diubah), dan prompt yang menggambarkan perubahan. Seperti generasi, editan dikembalikan sebagai base64.

```python
result = client.images.edit(
    model=deployment,
    image=open("sunlit_lounge.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="A sunlit indoor lounge area with a pool containing a flamingo",
)
image_bytes = base64.b64decode(result.data[0].b64_json)
with open("images/edited-image.png", "wb") as f:
    f.write(image_bytes)
```

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/id/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/id/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/id/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## Menetapkan batas dengan metaprompt

Setelah Anda bisa menghasilkan gambar, Anda perlu pengaman agar aplikasi Anda tidak memproduksi konten yang tidak aman atau tidak sesuai merek. **Metaprompt** adalah teks yang Anda tambahkan sebelum prompt pengguna untuk membatasi keluaran model.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# berikan `prompt` ke client.images.generate(...)
```

Setiap gambar kini dihasilkan dalam batas yang ditentukan oleh metaprompt. Gabungkan ini dengan filter konten bawaan Microsoft Foundry untuk pertahanan mendalam.

## Tugas - mari beri kemampuan pada siswa

Siswa Edu4All membutuhkan gambar untuk penilaian mereka. Buat aplikasi yang menghasilkan gambar **monumen** (monumen apa terserah Anda) ditempatkan dalam konteks yang berbeda dan kreatif - misalnya, landmark terkenal saat matahari terbenam dengan anak melihat.

Cobalah sendiri, lalu bandingkan dengan solusi referensi:

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) aplikasi generasi penuh: [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

Kerjakan juga notebook di [python/](../../../09-building-image-applications/python) (`aoai-assignment.ipynb` untuk Azure, `oai-assignment.ipynb` untuk OpenAI).

## Kerja bagus! Lanjutkan pembelajaran Anda

Setelah menyelesaikan pelajaran ini, lihat koleksi [Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan AI Generatif Anda!

Lanjut ke pelajaran 10 untuk terus belajar.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->