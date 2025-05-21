<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:18:26+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "id"
}
-->
# Membangun Aplikasi Pembuatan Gambar

Ada lebih banyak hal dalam LLM selain pembuatan teks. Anda juga dapat membuat gambar dari deskripsi teks. Memiliki gambar sebagai modalitas dapat sangat berguna dalam berbagai bidang seperti MedTech, arsitektur, pariwisata, pengembangan game, dan lainnya. Dalam bab ini, kita akan melihat dua model pembuatan gambar paling populer, DALL-E dan Midjourney.

## Pengantar

Dalam pelajaran ini, kita akan membahas:

- Pembuatan gambar dan mengapa itu berguna.
- DALL-E dan Midjourney, apa mereka, dan bagaimana cara kerjanya.
- Bagaimana Anda akan membangun aplikasi pembuatan gambar.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan dapat:

- Membangun aplikasi pembuatan gambar.
- Mendefinisikan batasan untuk aplikasi Anda dengan meta prompts.
- Bekerja dengan DALL-E dan Midjourney.

## Mengapa membangun aplikasi pembuatan gambar?

Aplikasi pembuatan gambar adalah cara yang bagus untuk mengeksplorasi kemampuan Generative AI. Mereka dapat digunakan, misalnya:

- **Pengeditan dan sintesis gambar**. Anda dapat membuat gambar untuk berbagai kasus penggunaan, seperti pengeditan gambar dan sintesis gambar.

- **Diterapkan pada berbagai industri**. Mereka juga dapat digunakan untuk membuat gambar untuk berbagai industri seperti MedTech, Pariwisata, Pengembangan game, dan lainnya.

## Skenario: Edu4All

Sebagai bagian dari pelajaran ini, kita akan terus bekerja dengan startup kita, Edu4All, dalam pelajaran ini. Para siswa akan membuat gambar untuk penilaian mereka, gambar apa yang dibuat terserah siswa, tetapi mereka dapat berupa ilustrasi untuk dongeng mereka sendiri atau membuat karakter baru untuk cerita mereka atau membantu mereka memvisualisasikan ide dan konsep mereka.

Berikut adalah contoh apa yang bisa dihasilkan oleh siswa Edu4All jika mereka bekerja di kelas pada monumen:

menggunakan prompt seperti

> "Anjing di samping Menara Eiffel dalam sinar matahari pagi"

## Apa itu DALL-E dan Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) dan [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) adalah dua model pembuatan gambar yang paling populer, mereka memungkinkan Anda menggunakan prompt untuk membuat gambar.

### DALL-E

Mari kita mulai dengan DALL-E, yang merupakan model Generative AI yang membuat gambar dari deskripsi teks.

- **CLIP**, adalah model yang menghasilkan embeddings, yang merupakan representasi numerik dari data, dari gambar dan teks.

- **Diffused attention**, adalah model yang membuat gambar dari embeddings. DALL-E dilatih pada kumpulan data gambar dan teks dan dapat digunakan untuk membuat gambar dari deskripsi teks. Misalnya, DALL-E dapat digunakan untuk membuat gambar kucing dengan topi, atau anjing dengan mohawk.

### Midjourney

Midjourney bekerja dengan cara yang mirip dengan DALL-E, ia membuat gambar dari prompt teks. Midjourney, juga dapat digunakan untuk membuat gambar menggunakan prompt seperti "kucing dengan topi", atau "anjing dengan mohawk".

## Bagaimana DALL-E dan Midjourney Bekerja

Pertama, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E adalah model Generative AI berdasarkan arsitektur transformer dengan _transformer autoregressive_.

Sebuah _transformer autoregressive_ mendefinisikan bagaimana sebuah model membuat gambar dari deskripsi teks, ia membuat satu piksel pada satu waktu, dan kemudian menggunakan piksel yang dihasilkan untuk membuat piksel berikutnya. Melewati beberapa lapisan dalam jaringan saraf, hingga gambar selesai.

Dengan proses ini, DALL-E, mengontrol atribut, objek, karakteristik, dan lainnya dalam gambar yang dihasilkan. Namun, DALL-E 2 dan 3 memiliki lebih banyak kontrol atas gambar yang dihasilkan.

## Membangun aplikasi pembuatan gambar pertama Anda

Jadi apa yang diperlukan untuk membangun aplikasi pembuatan gambar? Anda membutuhkan pustaka berikut:

- **python-dotenv**, sangat disarankan untuk menggunakan pustaka ini untuk menyimpan rahasia Anda dalam file _.env_ jauh dari kode.
- **openai**, pustaka ini adalah apa yang akan Anda gunakan untuk berinteraksi dengan API OpenAI.
- **pillow**, untuk bekerja dengan gambar di Python.
- **requests**, untuk membantu Anda membuat permintaan HTTP.

1. Buat file _.env_ dengan konten berikut:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Temukan informasi ini di Azure Portal untuk sumber daya Anda di bagian "Keys and Endpoint".

1. Kumpulkan pustaka di atas dalam file bernama _requirements.txt_ seperti ini:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Selanjutnya, buat lingkungan virtual dan instal pustaka:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Untuk Windows, gunakan perintah berikut untuk membuat dan mengaktifkan lingkungan virtual Anda:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Tambahkan kode berikut dalam file bernama _app.py_:

   ```python
   import openai
   import os
   import requests
   from PIL import Image
   import dotenv

   # import dotenv
   dotenv.load_dotenv()

   # Get endpoint and key from environment variables
   openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
   openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

   # Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
   openai.api_version = '2023-06-01-preview'
   openai.api_type = 'azure'


   try:
       # Create an image by using the image generation API
       generation_response = openai.Image.create(
           prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
           size='1024x1024',
           n=2,
           temperature=0,
       )
       # Set the directory for the stored image
       image_dir = os.path.join(os.curdir, 'images')

       # If the directory doesn't exist, create it
       if not os.path.isdir(image_dir):
           os.mkdir(image_dir)

       # Initialize the image path (note the filetype should be png)
       image_path = os.path.join(image_dir, 'generated-image.png')

       # Retrieve the generated image
       image_url = generation_response["data"][0]["url"]  # extract image URL from response
       generated_image = requests.get(image_url).content  # download the image
       with open(image_path, "wb") as image_file:
           image_file.write(generated_image)

       # Display the image in the default image viewer
       image = Image.open(image_path)
       image.show()

   # catch exceptions
   except openai.InvalidRequestError as err:
       print(err)

   ```

Mari kita jelaskan kode ini:

- Pertama, kita mengimpor pustaka yang kita butuhkan, termasuk pustaka OpenAI, pustaka dotenv, pustaka requests, dan pustaka Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Selanjutnya, kita memuat variabel lingkungan dari file _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Setelah itu, kita menetapkan endpoint, kunci untuk API OpenAI, versi dan tipe.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Selanjutnya, kita membuat gambar:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Kode di atas merespons dengan objek JSON yang berisi URL gambar yang dihasilkan. Kita dapat menggunakan URL untuk mengunduh gambar dan menyimpannya ke file.

- Terakhir, kita membuka gambar dan menggunakan penampil gambar standar untuk menampilkannya:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Detail lebih lanjut tentang membuat gambar

Mari kita lihat kode yang membuat gambar lebih detail:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, adalah prompt teks yang digunakan untuk membuat gambar. Dalam hal ini, kita menggunakan prompt "Kelinci di atas kuda, memegang lolipop, di padang rumput berkabut di mana tumbuh bunga daffodil".
- **size**, adalah ukuran gambar yang dihasilkan. Dalam hal ini, kita membuat gambar yang berukuran 1024x1024 piksel.
- **n**, adalah jumlah gambar yang dihasilkan. Dalam hal ini, kita membuat dua gambar.
- **temperature**, adalah parameter yang mengontrol kebetulan output dari model Generative AI. Temperature adalah nilai antara 0 dan 1 di mana 0 berarti bahwa output deterministik dan 1 berarti bahwa output acak. Nilai default adalah 0.7.

Ada lebih banyak hal yang dapat Anda lakukan dengan gambar yang akan kita bahas di bagian berikutnya.

## Kemampuan tambahan dari pembuatan gambar

Anda telah melihat sejauh ini bagaimana kita dapat membuat gambar menggunakan beberapa baris dalam Python. Namun, ada lebih banyak hal yang dapat Anda lakukan dengan gambar.

Anda juga dapat melakukan hal berikut:

- **Melakukan pengeditan**. Dengan memberikan gambar yang ada sebuah masker dan prompt, Anda dapat mengubah gambar. Misalnya, Anda dapat menambahkan sesuatu ke bagian gambar. Bayangkan gambar kelinci kita, Anda dapat menambahkan topi ke kelinci. Cara Anda melakukannya adalah dengan memberikan gambar, masker (mengidentifikasi bagian area untuk perubahan) dan prompt teks untuk mengatakan apa yang harus dilakukan.

  ```python
  response = openai.Image.create_edit(
    image=open("base_image.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="An image of a rabbit with a hat on its head.",
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  Gambar dasar hanya akan berisi kelinci tetapi gambar akhir akan memiliki topi di kelinci.

- **Membuat variasi**. Ide ini adalah bahwa Anda mengambil gambar yang ada dan meminta agar variasi dibuat. Untuk membuat variasi, Anda memberikan gambar dan prompt teks dan kode seperti ini:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Catatan, ini hanya didukung di OpenAI

## Temperature

Temperature adalah parameter yang mengontrol kebetulan output dari model Generative AI. Temperature adalah nilai antara 0 dan 1 di mana 0 berarti bahwa output deterministik dan 1 berarti bahwa output acak. Nilai default adalah 0.7.

Mari kita lihat contoh bagaimana temperature bekerja, dengan menjalankan prompt ini dua kali:

> Prompt: "Kelinci di atas kuda, memegang lolipop, di padang rumput berkabut di mana tumbuh bunga daffodil"

Sekarang mari kita jalankan prompt yang sama hanya untuk melihat bahwa kita tidak akan mendapatkan gambar yang sama dua kali:

Seperti yang Anda lihat, gambar-gambar tersebut mirip, tetapi tidak sama. Mari kita coba mengubah nilai temperature menjadi 0.1 dan lihat apa yang terjadi:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Mengubah temperature

Jadi mari kita coba membuat respons lebih deterministik. Kita dapat mengamati dari dua gambar yang kita buat bahwa dalam gambar pertama, ada kelinci dan dalam gambar kedua, ada kuda, jadi gambar-gambar tersebut sangat bervariasi.

Mari kita ubah kode kita dan atur temperature menjadi 0, seperti ini:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Sekarang ketika Anda menjalankan kode ini, Anda mendapatkan dua gambar ini:

Di sini Anda dapat dengan jelas melihat bagaimana gambar-gambar tersebut lebih mirip satu sama lain.

## Cara mendefinisikan batasan untuk aplikasi Anda dengan metaprompts

Dengan demo kita, kita sudah dapat membuat gambar untuk klien kita. Namun, kita perlu membuat beberapa batasan untuk aplikasi kita.

Misalnya, kita tidak ingin membuat gambar yang tidak aman untuk bekerja, atau yang tidak sesuai untuk anak-anak.

Kita dapat melakukannya dengan _metaprompts_. Metaprompts adalah prompt teks yang digunakan untuk mengontrol output dari model Generative AI. Misalnya, kita dapat menggunakan metaprompts untuk mengontrol output, dan memastikan bahwa gambar yang dihasilkan aman untuk bekerja, atau sesuai untuk anak-anak.

### Bagaimana cara kerjanya?

Sekarang, bagaimana metaprompts bekerja?

Metaprompts adalah prompt teks yang digunakan untuk mengontrol output dari model Generative AI, mereka diposisikan sebelum prompt teks, dan digunakan untuk mengontrol output dari model dan tertanam dalam aplikasi untuk mengontrol output dari model. Mengenkapsulasi input prompt dan input metaprompt dalam satu prompt teks.

Salah satu contoh metaprompt adalah sebagai berikut:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Sekarang, mari kita lihat bagaimana kita dapat menggunakan metaprompts dalam demo kita.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt =f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"{meta_prompt}
Create an image of a bunny on a horse, holding a lollipop"

# TODO add request to generate image
```

Dari prompt di atas, Anda dapat melihat bagaimana semua gambar yang dibuat mempertimbangkan metaprompt.

## Tugas - mari kita berdayakan siswa

Kami memperkenalkan Edu4All di awal pelajaran ini. Sekarang saatnya untuk memberdayakan siswa untuk membuat gambar untuk penilaian mereka.

Para siswa akan membuat gambar untuk penilaian mereka yang berisi monumen, tepatnya monumen apa yang dibuat terserah siswa. Para siswa diminta untuk menggunakan kreativitas mereka dalam tugas ini untuk menempatkan monumen ini dalam konteks yang berbeda.

## Solusi

Berikut adalah salah satu solusi yang mungkin:

```python
import openai
import os
import requests
from PIL import Image
import dotenv

# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
openai.api_base = "<replace with endpoint>"
openai.api_key = "<replace with api key>"

# Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
openai.api_version = '2023-06-01-preview'
openai.api_type = 'azure'

disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}"""

prompt = f"""{metaprompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
""""

try:
    # Create an image by using the image generation API
    generation_response = openai.Image.create(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response["data"][0]["url"]  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.InvalidRequestError as err:
    print(err)
```

## Kerja Bagus! Lanjutkan Pembelajaran Anda

Setelah menyelesaikan pelajaran ini, lihat [Koleksi Pembelajaran Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan Generative AI Anda!

Pergilah ke Pelajaran 10 di mana kita akan melihat bagaimana [membangun aplikasi AI dengan kode rendah](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi penting, disarankan untuk menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.