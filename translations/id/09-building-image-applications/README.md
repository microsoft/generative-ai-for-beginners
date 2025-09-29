<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T21:50:05+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "id"
}
-->
# Membangun Aplikasi Generasi Gambar

[![Membangun Aplikasi Generasi Gambar](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.id.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Generasi AI tidak hanya terbatas pada teks. Kita juga dapat menghasilkan gambar dari deskripsi teks. Memiliki gambar sebagai modalitas dapat sangat berguna di berbagai bidang seperti MedTech, arsitektur, pariwisata, pengembangan game, dan lainnya. Dalam bab ini, kita akan membahas dua model generasi gambar yang paling populer, DALL-E dan Midjourney.

## Pendahuluan

Dalam pelajaran ini, kita akan membahas:

- Generasi gambar dan mengapa itu berguna.
- DALL-E dan Midjourney, apa itu, dan bagaimana cara kerjanya.
- Cara membangun aplikasi generasi gambar.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan dapat:

- Membangun aplikasi generasi gambar.
- Menentukan batasan untuk aplikasi Anda dengan meta prompt.
- Bekerja dengan DALL-E dan Midjourney.

## Mengapa membangun aplikasi generasi gambar?

Aplikasi generasi gambar adalah cara yang bagus untuk mengeksplorasi kemampuan Generative AI. Aplikasi ini dapat digunakan untuk, misalnya:

- **Pengeditan dan sintesis gambar**. Anda dapat menghasilkan gambar untuk berbagai kasus penggunaan, seperti pengeditan gambar dan sintesis gambar.

- **Diterapkan pada berbagai industri**. Aplikasi ini juga dapat digunakan untuk menghasilkan gambar untuk berbagai industri seperti MedTech, Pariwisata, Pengembangan Game, dan lainnya.

## Skenario: Edu4All

Sebagai bagian dari pelajaran ini, kita akan melanjutkan bekerja dengan startup kita, Edu4All. Para siswa akan membuat gambar untuk penilaian mereka, jenis gambar yang dibuat terserah kepada siswa, tetapi mereka dapat membuat ilustrasi untuk dongeng mereka sendiri, menciptakan karakter baru untuk cerita mereka, atau membantu mereka memvisualisasikan ide dan konsep mereka.

Berikut adalah contoh gambar yang dapat dihasilkan oleh siswa Edu4All jika mereka sedang belajar tentang monumen di kelas:

![Startup Edu4All, kelas tentang monumen, Menara Eiffel](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.id.png)

menggunakan prompt seperti

> "Anjing di samping Menara Eiffel saat matahari pagi"

## Apa itu DALL-E dan Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) dan [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) adalah dua model generasi gambar yang paling populer, yang memungkinkan Anda menggunakan prompt untuk menghasilkan gambar.

### DALL-E

Mari kita mulai dengan DALL-E, yang merupakan model Generative AI yang menghasilkan gambar dari deskripsi teks.

> [DALL-E adalah kombinasi dari dua model, CLIP dan diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, adalah model yang menghasilkan embeddings, yaitu representasi numerik dari data, dari gambar dan teks.

- **Diffused attention**, adalah model yang menghasilkan gambar dari embeddings. DALL-E dilatih pada dataset gambar dan teks dan dapat digunakan untuk menghasilkan gambar dari deskripsi teks. Misalnya, DALL-E dapat digunakan untuk menghasilkan gambar kucing dengan topi, atau anjing dengan mohawk.

### Midjourney

Midjourney bekerja dengan cara yang mirip dengan DALL-E, yaitu menghasilkan gambar dari prompt teks. Midjourney juga dapat digunakan untuk menghasilkan gambar menggunakan prompt seperti "kucing dengan topi", atau "anjing dengan mohawk".

![Gambar yang dihasilkan oleh Midjourney, merpati mekanik](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Kredit gambar Wikipedia, gambar dihasilkan oleh Midjourney_

## Bagaimana cara kerja DALL-E dan Midjourney

Pertama, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E adalah model Generative AI yang berbasis pada arsitektur transformer dengan _autoregressive transformer_.

_Autoregressive transformer_ mendefinisikan bagaimana model menghasilkan gambar dari deskripsi teks, yaitu dengan menghasilkan satu piksel pada satu waktu, dan kemudian menggunakan piksel yang dihasilkan untuk menghasilkan piksel berikutnya. Proses ini melewati beberapa lapisan dalam jaringan neural hingga gambar selesai.

Dengan proses ini, DALL-E dapat mengontrol atribut, objek, karakteristik, dan lainnya dalam gambar yang dihasilkan. Namun, DALL-E 2 dan 3 memiliki kontrol lebih besar terhadap gambar yang dihasilkan.

## Membangun aplikasi generasi gambar pertama Anda

Jadi, apa yang diperlukan untuk membangun aplikasi generasi gambar? Anda memerlukan pustaka berikut:

- **python-dotenv**, sangat disarankan untuk menggunakan pustaka ini untuk menyimpan rahasia Anda dalam file _.env_ yang terpisah dari kode.
- **openai**, pustaka ini digunakan untuk berinteraksi dengan API OpenAI.
- **pillow**, untuk bekerja dengan gambar di Python.
- **requests**, untuk membantu Anda membuat permintaan HTTP.

## Membuat dan menerapkan model Azure OpenAI

Jika belum dilakukan, ikuti petunjuk di halaman [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) untuk membuat sumber daya dan model Azure OpenAI. Pilih DALL-E 3 sebagai model.

## Membuat aplikasi

1. Buat file _.env_ dengan konten berikut:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Temukan informasi ini di Portal Azure OpenAI Foundry untuk sumber daya Anda di bagian "Deployments".

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
    from openai import OpenAI, AzureOpenAI
    
    # import dotenv
    dotenv.load_dotenv()
    
    # configure Azure OpenAI service client 
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
    try:
        # Create an image by using the image generation API
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Set the directory for the stored image
        image_dir = os.path.join(os.curdir, 'images')

        # If the directory doesn't exist, create it
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Initialize the image path (note the filetype should be png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Retrieve the generated image
        image_url = generation_response.data[0].url  # extract image URL from response
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

- Setelah itu, kita mengonfigurasi klien layanan Azure OpenAI.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Selanjutnya, kita menghasilkan gambar:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Kode di atas merespons dengan objek JSON yang berisi URL gambar yang dihasilkan. Kita dapat menggunakan URL untuk mengunduh gambar dan menyimpannya ke file.

- Terakhir, kita membuka gambar dan menggunakan penampil gambar standar untuk menampilkannya:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Detail lebih lanjut tentang menghasilkan gambar

Mari kita lihat kode yang menghasilkan gambar secara lebih rinci:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, adalah teks prompt yang digunakan untuk menghasilkan gambar. Dalam kasus ini, kita menggunakan prompt "Kelinci di atas kuda, memegang lolipop, di padang rumput berkabut tempat tumbuh bunga daffodil".
- **size**, adalah ukuran gambar yang dihasilkan. Dalam kasus ini, kita menghasilkan gambar berukuran 1024x1024 piksel.
- **n**, adalah jumlah gambar yang dihasilkan. Dalam kasus ini, kita menghasilkan dua gambar.
- **temperature**, adalah parameter yang mengontrol tingkat keacakan output model Generative AI. Nilai temperature adalah antara 0 dan 1, di mana 0 berarti output deterministik dan 1 berarti output acak. Nilai default adalah 0.7.

Ada lebih banyak hal yang dapat Anda lakukan dengan gambar yang akan kita bahas di bagian berikutnya.

## Kemampuan tambahan generasi gambar

Sejauh ini Anda telah melihat bagaimana kita dapat menghasilkan gambar menggunakan beberapa baris kode Python. Namun, ada lebih banyak hal yang dapat Anda lakukan dengan gambar.

Anda juga dapat melakukan hal berikut:

- **Melakukan pengeditan**. Dengan memberikan gambar yang ada, sebuah mask, dan prompt, Anda dapat mengubah gambar. Misalnya, Anda dapat menambahkan sesuatu ke bagian tertentu dari gambar. Bayangkan gambar kelinci kita, Anda dapat menambahkan topi ke kelinci. Cara melakukannya adalah dengan memberikan gambar, mask (mengidentifikasi bagian area untuk perubahan), dan prompt teks untuk mengatakan apa yang harus dilakukan. 
> Catatan: ini tidak didukung di DALL-E 3.

Berikut adalah contoh menggunakan GPT Image:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  Gambar dasar hanya akan berisi lounge dengan kolam renang, tetapi gambar akhir akan memiliki flamingo:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.id.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.id.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.id.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **Membuat variasi**. Ide dasarnya adalah Anda mengambil gambar yang ada dan meminta agar variasi dibuat. Untuk membuat variasi, Anda memberikan gambar dan prompt teks serta kode seperti ini:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Catatan, ini hanya didukung di OpenAI.

## Temperature

Temperature adalah parameter yang mengontrol tingkat keacakan output model Generative AI. Nilai temperature adalah antara 0 dan 1, di mana 0 berarti output deterministik dan 1 berarti output acak. Nilai default adalah 0.7.

Mari kita lihat contoh bagaimana temperature bekerja, dengan menjalankan prompt ini dua kali:

> Prompt: "Kelinci di atas kuda, memegang lolipop, di padang rumput berkabut tempat tumbuh bunga daffodil"

![Kelinci di atas kuda memegang lolipop, versi 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.id.png)

Sekarang mari kita jalankan prompt yang sama untuk melihat bahwa kita tidak akan mendapatkan gambar yang sama dua kali:

![Gambar yang dihasilkan dari kelinci di atas kuda](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.id.png)

Seperti yang Anda lihat, gambar-gambar tersebut serupa, tetapi tidak sama. Mari kita coba mengubah nilai temperature menjadi 0.1 dan lihat apa yang terjadi:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Mengubah temperature

Jadi mari kita coba membuat respons lebih deterministik. Kita dapat mengamati dari dua gambar yang dihasilkan bahwa pada gambar pertama, ada kelinci, dan pada gambar kedua, ada kuda, sehingga gambar-gambar tersebut sangat bervariasi.

Oleh karena itu, mari kita ubah kode kita dan atur temperature menjadi 0, seperti ini:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Sekarang ketika Anda menjalankan kode ini, Anda mendapatkan dua gambar berikut:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.id.png)
- ![Temperature 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.id.png)

Di sini Anda dapat dengan jelas melihat bagaimana gambar-gambar tersebut lebih mirip satu sama lain.

## Cara menentukan batasan untuk aplikasi Anda dengan metaprompt

Dengan demo kita, kita sudah dapat menghasilkan gambar untuk klien kita. Namun, kita perlu membuat beberapa batasan untuk aplikasi kita.

Misalnya, kita tidak ingin menghasilkan gambar yang tidak aman untuk pekerjaan, atau yang tidak sesuai untuk anak-anak.

Kita dapat melakukan ini dengan _metaprompt_. Metaprompt adalah teks prompt yang digunakan untuk mengontrol output model Generative AI. Misalnya, kita dapat menggunakan metaprompt untuk mengontrol output, dan memastikan bahwa gambar yang dihasilkan aman untuk pekerjaan, atau sesuai untuk anak-anak.

### Bagaimana cara kerjanya?

Sekarang, bagaimana metaprompt bekerja?

Metaprompt adalah teks prompt yang digunakan untuk mengontrol output model Generative AI, mereka ditempatkan sebelum teks prompt, dan digunakan untuk mengontrol output model serta diintegrasikan dalam aplikasi untuk mengontrol output model. Metaprompt menggabungkan input prompt dan input metaprompt dalam satu teks prompt.

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

Sekarang, mari kita lihat bagaimana kita dapat menggunakan metaprompt dalam demo kita.

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

## Tugas - mari kita bantu siswa

Kami memperkenalkan Edu4All di awal pelajaran ini. Sekarang saatnya untuk membantu siswa menghasilkan gambar untuk penilaian mereka.

Para siswa akan membuat gambar untuk penilaian mereka yang berisi monumen, jenis monumen yang dibuat terserah kepada siswa. Para siswa diminta menggunakan kreativitas mereka dalam tugas ini untuk menempatkan monumen-monumen tersebut dalam berbagai konteks.

## Solusi

Berikut adalah salah satu solusi yang mungkin:
```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-02-01"
  )


disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"""{meta_prompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
""""

try:
    # Create an image by using the image generation API
    generation_response = client.images.generate(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=1,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response.data[0].url  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.BadRequestError as err:
    print(err)
```

## Kerja Hebat! Lanjutkan Pembelajaran Anda

Setelah menyelesaikan pelajaran ini, lihat koleksi [Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan Anda tentang AI Generatif!

Lanjutkan ke Pelajaran 10 di mana kita akan melihat cara [membangun aplikasi AI dengan kode rendah](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.