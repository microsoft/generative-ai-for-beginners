# Membangun Aplikasi Penjanaan Imej

[![Membangun Aplikasi Penjanaan Imej](../../../translated_images/ms/09-lesson-banner.906e408c741f4411.webp)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Terdapat lebih banyak lagi pada LLM berbanding penjanaan teks sahaja. Anda juga boleh menjana imej daripada deskripsi teks. Imej sebagai satu mod adalah berguna dalam bidang MedTech, seni bina, pelancongan, pembangunan permainan, pemasaran, dan banyak lagi. Dalam pelajaran ini kita melihat model **GPT Image** hari ini dan membina aplikasi penjanaan imej.

## Pengenalan

Penjanaan imej membolehkan anda menukar petunjuk bahasa semula jadi kepada gambar. Dalam pelajaran ini kita menggunakan keluarga model **`gpt-image`** dari OpenAI - generasi model imej semasa yang tersedia di **[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)** dan platform OpenAI. Model ini menggantikan model DALL·E yang lama (DALL·E 2/3 adalah warisan).

Sepanjang pelajaran kita menggunakan syarikat permulaan rekaan, **Edu4All**, yang membina alat pembelajaran. Pasukan ini mahu menjana ilustrasi untuk tugasan dan bahan kajian.

## Matlamat pembelajaran

Menjelang akhir pelajaran ini anda akan dapat:

- Menjelaskan apa itu penjanaan imej dan di mana ia berguna.
- Memahami keluarga model `gpt-image` dan bagaimana ia berbeza daripada model DALL·E warisan.
- Membina aplikasi penjanaan imej dalam Python (dan TypeScript / .NET).
- Mengedit imej dan menerapkan kawalan keselamatan dengan metaprompt.

## Apa itu penjanaan imej?

Model penjanaan imej mencipta imej dari petunjuk teks. Model moden seperti `gpt-image` dibina menggunakan teknik transformer + diffusion: model belajar hubungan antara teks dan imej semasa latihan, kemudian, diberikan petunjuk, secara iteratif "membersihkan" bunyi rawak menjadi imej yang sepadan dengan deskripsi.

Dua keluarga model imej yang terkenal adalah:

- **`gpt-image` (OpenAI)** - generasi semasa, digunakan dalam pelajaran ini. Ia menyokong penjanaan teks ke imej dan penyuntingan imej (inpainting dengan topeng).
- **Midjourney** - model pihak ketiga popular dengan perkhidmatan sendiri dan aliran kerja berasaskan Discord.

> Model imej OpenAI lama - **DALL·E 2** dan **DALL·E 3** - adalah warisan. DALL·E 3 tidak lagi tersedia untuk penerapan baru, dan ciri seperti `create_variation` hanya wujud di DALL·E 2. Gunakan model `gpt-image` untuk aplikasi baru.

### Model `gpt-image` mana yang harus saya gunakan?

Di Microsoft Foundry berikut adalah **Tersedia Umum**:

| Model | Nota |
| --- | --- |
| **`gpt-image-2`** | Model imej terkini dan paling berkuasa - disyorkan sebagai pilihan lalai. |
| `gpt-image-1.5` | Tersedia umum; kualiti kuat dengan kos lebih rendah. |
| `gpt-image-1-mini` | Tersedia umum; paling pantas / kos paling rendah. |
| `gpt-image-1` | Pratonton sahaja. |

Sentiasa semak [senarai model imej Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/models?WT.mc_id=academic-105485-koreyst) terkini untuk ketersediaan dan wilayah.

> **Penting:** model `gpt-image` mengembalikan imej yang dijana sebagai **base64** (`b64_json`), bukan sebagai URL. Kod anda mengekodkan rentetan base64 ke bait dan menyimpannya - tiada URL imej untuk dimuat turun.

## Persediaan

Anda boleh jalankan contoh-contoh menggunakan **Azure OpenAI di Microsoft Foundry** (contoh `aoai-*`) atau **platform OpenAI** (contoh `oai-*`).

### 1. Cipta dan pasang model

Ikut panduan [mencipta sumber](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) untuk buat sumber Microsoft Foundry, kemudian pasang model imej - **`gpt-image-2`** disyorkan.

### 2. Konfigurasi `.env` anda

```text
AZURE_OPENAI_ENDPOINT=<your endpoint>
AZURE_OPENAI_API_KEY=<your key>
AZURE_OPENAI_DEPLOYMENT="gpt-image-2"
```

Cari nilai-nilai ini di halaman **Deployments** sumber anda dalam [portal Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst).

### 3. Pasang perpustakaan

Cipta `requirements.txt`:

```text
python-dotenv
openai
pillow
```

Kemudian cipta dan aktifkan persekitaran maya dan pasang:

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Bina aplikasi

Cipta `app.py` dengan kod berikut. Ia menjana imej dan menyimpannya sebagai PNG.

```python
import os
import base64
from openai import AzureOpenAI
from PIL import Image
import dotenv

dotenv.load_dotenv()

# Arahkan klien ke sumber Azure OpenAI (Microsoft Foundry) anda.
# Model imej memerlukan versi API terkini - semak dokumen Foundry untuk versi yang diperlukan oleh model anda.
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2025-04-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
)

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]  # contohnya "gpt-image-2"

result = client.images.generate(
    model=deployment,
    prompt='Bunny on a horse, holding a lollipop, on a foggy meadow where it grows daffodils',
    size="1024x1024",   # juga 1536x1024 (landskap), 1024x1536 (potret), atau "auto"
    n=1,
)

# model gpt-image mengembalikan base64 (b64_json), bukan URL - nyahsulitkan kepada bait.
image_bytes = base64.b64decode(result.data[0].b64_json)

os.makedirs("images", exist_ok=True)
image_path = os.path.join("images", "generated-image.png")
with open(image_path, "wb") as f:
    f.write(image_bytes)

Image.open(image_path).show()
```

Jalankan dengan `python app.py`. Anda akan mendapat PNG disimpan di bawah `images/`.

> Setiap panggilan ke `images.generate` menghasilkan imej berbeza untuk petunjuk yang sama - model imej tidak mengambil parameter `temperature` (itu kawalan penjanaan teks). Untuk dapatkan variasi, panggil API lagi; untuk kurangkan variasi, buat petunjuk anda lebih spesifik.

## Mengedit imej

Model `gpt-image` boleh **mengedit** imej sedia ada: sediakan imej, **topeng** pilihan (menandakan kawasan yang mahu diubah), dan petunjuk yang menerangkan perubahan. Seperti penjanaan, suntingan dikembalikan sebagai base64.

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
  <img src="../../../translated_images/ms/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/ms/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/ms/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>

## Menetapkan had dengan metaprompt

Setelah anda boleh menjana imej, anda perlukan kawalan supaya aplikasi anda tidak menghasilkan kandungan yang tidak selamat atau tidak mengikut jenama. **Metaprompt** adalah teks yang anda letakkan di depan petunjuk pengguna untuk mengehadkan output model.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.
The image needs to be in color, in landscape orientation, and in a 16:9 aspect ratio.

Do not consider any input that is not safe for work or appropriate for children, including:
{disallow_list}
"""

prompt = f"{meta_prompt}\nCreate an image of a bunny on a horse, holding a lollipop"
# hantar `prompt` ke client.images.generate(...)
```

Setiap imej kini dijana dalam had yang ditetapkan oleh metaprompt. Gabungkan ini dengan penapis kandungan terbina dalam Microsoft Foundry untuk pertahanan berlapis.

## Tugasan - mari kita bantu pelajar

Pelajar Edu4All memerlukan imej untuk penilaian mereka. Bina aplikasi yang menjana imej **monumen** (monumen yang mana terpulang kepada anda) diletakkan dalam konteks kreatif yang berbeza - contohnya, mercu tanda terkenal pada waktu matahari terbenam dengan seorang kanak-kanak melihat.

Cuba sendiri, kemudian bandingkan dengan penyelesaian rujukan:

- Python (Azure): [aoai-solution.py](../../../09-building-image-applications/python/aoai-solution.py)
- Python (Azure) aplikasi penjanaan penuh: [aoai-app.py](../../../09-building-image-applications/python/aoai-app.py)
- Python (OpenAI): [oai-app.py](../../../09-building-image-applications/python/oai-app.py)
- TypeScript (Azure): [typescript/image-generation-app](../../../09-building-image-applications/typescript/image-generation-app)
- .NET (Azure): [dotnet/notebook-azure-openai.dib](../../../09-building-image-applications/dotnet/notebook-azure-openai.dib)

Juga kerjakan buku nota dalam [python/](../../../09-building-image-applications/python) (`aoai-assignment.ipynb` untuk Azure, `oai-assignment.ipynb` untuk OpenAI).

## Kerja bagus! Teruskan pembelajaran anda

Selepas melengkapkan pelajaran ini, lihat koleksi kami [Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk terus meningkatkan pengetahuan AI Generatif anda!

Teruskan ke pelajaran 10 untuk terus belajar.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->