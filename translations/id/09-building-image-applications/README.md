<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef74ad58fc01f7ad80788f79505f9816",
  "translation_date": "2025-08-26T18:20:10+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "id"
}
-->
# Membangun Aplikasi Generasi Gambar

[![Membangun Aplikasi Generasi Gambar](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.id.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM tidak hanya untuk menghasilkan teks. Kita juga bisa membuat gambar dari deskripsi teks. Gambar sebagai salah satu bentuk output sangat berguna di berbagai bidang seperti MedTech, arsitektur, pariwisata, pengembangan game, dan lainnya. Di bab ini, kita akan membahas dua model generasi gambar yang paling populer, DALL-E dan Midjourney.

## Pendahuluan

Di pelajaran ini, kita akan membahas:

- Generasi gambar dan manfaatnya.
- DALL-E dan Midjourney, apa itu dan cara kerjanya.
- Cara membangun aplikasi generasi gambar.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, kamu akan bisa:

- Membangun aplikasi generasi gambar.
- Menentukan batasan aplikasi dengan meta prompt.
- Menggunakan DALL-E dan Midjourney.

## Kenapa membangun aplikasi generasi gambar?

Aplikasi generasi gambar adalah cara yang bagus untuk mengeksplorasi kemampuan AI Generatif. Aplikasi ini bisa digunakan untuk, misalnya:

- **Edit dan sintesis gambar**. Kamu bisa membuat gambar untuk berbagai kebutuhan, seperti mengedit gambar atau membuat gambar baru.

- **Bisa diterapkan di berbagai industri**. Aplikasi ini juga bisa digunakan untuk membuat gambar di berbagai bidang seperti Medtech, Pariwisata, Pengembangan Game, dan lainnya.

## Skenario: Edu4All

Sebagai bagian dari pelajaran ini, kita akan lanjut bekerja dengan startup kita, Edu4All. Para siswa akan membuat gambar untuk tugas mereka, gambar apa yang dibuat terserah siswa, bisa berupa ilustrasi dongeng mereka sendiri, membuat karakter baru untuk cerita mereka, atau membantu mereka memvisualisasikan ide dan konsep.

Contohnya, jika siswa Edu4All sedang belajar tentang monumen di kelas:

![Startup Edu4All, kelas tentang monumen, Menara Eiffel](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.id.png)

menggunakan prompt seperti

> "Anjing di samping Menara Eiffel saat matahari pagi"

## Apa itu DALL-E dan Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) dan [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) adalah dua model generasi gambar yang paling populer, yang memungkinkan kamu menggunakan prompt untuk membuat gambar.

### DALL-E

Mari mulai dengan DALL-E, yaitu model AI Generatif yang membuat gambar dari deskripsi teks.

> [DALL-E adalah gabungan dua model, CLIP dan diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, adalah model yang menghasilkan embedding, yaitu representasi numerik dari data, baik dari gambar maupun teks.

- **Diffused attention**, adalah model yang membuat gambar dari embedding. DALL-E dilatih dengan dataset gambar dan teks, sehingga bisa digunakan untuk membuat gambar dari deskripsi teks. Misalnya, DALL-E bisa digunakan untuk membuat gambar kucing memakai topi, atau anjing dengan mohawk.

### Midjourney

Midjourney bekerja mirip dengan DALL-E, menghasilkan gambar dari prompt teks. Midjourney juga bisa digunakan untuk membuat gambar dengan prompt seperti “kucing memakai topi”, atau “anjing dengan mohawk”.

![Gambar yang dihasilkan Midjourney, burung merpati mekanik](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Kredit gambar Wikipedia, gambar dihasilkan oleh Midjourney_

## Bagaimana Cara Kerja DALL-E dan Midjourney

Pertama, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E adalah model AI Generatif yang berbasis arsitektur transformer dengan _autoregressive transformer_.

_Autoregressive transformer_ menentukan bagaimana model membuat gambar dari deskripsi teks, yaitu dengan membuat satu piksel setiap kali, lalu menggunakan piksel yang sudah dibuat untuk membuat piksel berikutnya. Proses ini melewati beberapa lapisan dalam neural network, sampai gambar selesai.

Dengan proses ini, DALL-E bisa mengatur atribut, objek, karakteristik, dan lainnya dalam gambar yang dihasilkan. Namun, DALL-E 2 dan 3 punya kontrol lebih terhadap gambar yang dihasilkan.

## Membangun aplikasi generasi gambar pertama kamu

Jadi, apa saja yang dibutuhkan untuk membangun aplikasi generasi gambar? Kamu perlu beberapa library berikut:

- **python-dotenv**, sangat disarankan untuk menyimpan rahasia di file _.env_ terpisah dari kode.
- **openai**, library ini digunakan untuk berinteraksi dengan API OpenAI.
- **pillow**, untuk mengolah gambar di Python.
- **requests**, untuk membantu melakukan HTTP request.

## Membuat dan mendepoy model Azure OpenAI

Jika belum, ikuti instruksi di halaman [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal)
untuk membuat resource dan model Azure OpenAI. Pilih DALL-E 3 sebagai model.  

## Membuat aplikasinya

1. Buat file _.env_ dengan isi berikut:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Informasi ini bisa ditemukan di Azure OpenAI Foundry Portal pada bagian "Deployments" untuk resource kamu.

1. Kumpulkan library di atas dalam file _requirements.txt_ seperti berikut:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Selanjutnya, buat virtual environment dan install library-nya:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Untuk Windows, gunakan perintah berikut untuk membuat dan mengaktifkan virtual environment:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Tambahkan kode berikut ke file bernama _app.py_:

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

- Pertama, kita import library yang dibutuhkan, termasuk OpenAI, dotenv, requests, dan Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Selanjutnya, kita load environment variable dari file _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Setelah itu, kita konfigurasi client Azure OpenAI service 

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Berikutnya, kita menghasilkan gambar:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Kode di atas akan memberikan respons berupa objek JSON yang berisi URL gambar yang dihasilkan. Kita bisa menggunakan URL tersebut untuk mengunduh gambar dan menyimpannya ke file.

- Terakhir, kita buka gambar dan gunakan image viewer standar untuk menampilkannya:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Detail lebih lanjut tentang proses generasi gambar

Mari kita lihat kode yang menghasilkan gambar secara lebih detail:

    ```python
      generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                            )
    ```

- **prompt**, adalah teks yang digunakan untuk membuat gambar. Dalam contoh ini, kita menggunakan prompt "Kelinci di atas kuda, memegang lolipop, di padang berkabut yang tumbuh bunga daffodil".
- **size**, adalah ukuran gambar yang dihasilkan. Di sini, kita membuat gambar berukuran 1024x1024 piksel.
- **n**, adalah jumlah gambar yang dihasilkan. Di sini, kita membuat dua gambar.
- **temperature**, adalah parameter yang mengatur tingkat acak output dari model AI Generatif. Nilainya antara 0 dan 1, di mana 0 berarti output pasti dan 1 berarti output acak. Nilai default adalah 0.7.

Masih banyak hal lain yang bisa dilakukan dengan gambar, yang akan kita bahas di bagian berikutnya.

## Kemampuan tambahan dari generasi gambar

Kamu sudah melihat bagaimana kita bisa membuat gambar hanya dengan beberapa baris kode Python. Tapi, masih banyak hal lain yang bisa dilakukan dengan gambar.

Kamu juga bisa melakukan hal berikut:

- **Edit gambar**. Dengan memberikan gambar yang sudah ada, sebuah mask, dan prompt, kamu bisa mengubah gambar. Misalnya, kamu bisa menambahkan sesuatu ke bagian gambar. Bayangkan gambar kelinci tadi, kamu bisa menambahkan topi ke kelinci. Caranya dengan memberikan gambar, mask (menandai bagian yang ingin diubah), dan prompt teks untuk menjelaskan perubahan yang diinginkan.
> Catatan: fitur ini tidak didukung di DALL-E 3. 
 
Berikut contoh menggunakan GPT Image:

    ```python
    response = client.images.edit(
        model="gpt-image-1",
        image=open("sunlit_lounge.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo"
    )
    image_url = response.data[0].url
    ```

  Gambar dasar hanya berisi lounge dengan kolam renang, tapi gambar akhir akan ada flamingo:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="./images/sunlit_lounge.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/mask.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/sunlit_lounge_result.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Membuat variasi**. Ide dasarnya adalah kamu mengambil gambar yang sudah ada dan meminta dibuatkan variasinya. Untuk membuat variasi, kamu memberikan gambar dan prompt teks serta kode seperti berikut:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Catatan, fitur ini hanya didukung di OpenAI

## Temperature

Temperature adalah parameter yang mengatur tingkat acak output dari model AI Generatif. Nilainya antara 0 dan 1, di mana 0 berarti output pasti dan 1 berarti output acak. Nilai default adalah 0.7.

Mari kita lihat contoh cara kerja temperature, dengan menjalankan prompt ini dua kali:

> Prompt : "Kelinci di atas kuda, memegang lolipop, di padang berkabut yang tumbuh bunga daffodil"

![Kelinci di atas kuda memegang lolipop, versi 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.id.png)

Sekarang jalankan prompt yang sama, dan lihat bahwa hasilnya tidak akan sama persis:

![Gambar kelinci di atas kuda](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.id.png)

Seperti yang terlihat, gambarnya mirip, tapi tidak sama. Sekarang coba ubah nilai temperature ke 0.1 dan lihat hasilnya:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Mengubah temperature

Sekarang kita coba membuat respons lebih pasti. Dari dua gambar yang dihasilkan, di gambar pertama ada kelinci dan di gambar kedua ada kuda, jadi gambarnya cukup berbeda.

Mari kita ubah kode dan set temperature ke 0, seperti berikut:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Saat kamu jalankan kode ini, hasilnya adalah dua gambar berikut:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.id.png)
- ![Temperature 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.id.png)

Di sini kamu bisa lihat gambar yang dihasilkan lebih mirip satu sama lain.

## Cara menentukan batasan aplikasi dengan metaprompt

Dengan demo kita, kita sudah bisa membuat gambar untuk klien. Tapi, kita perlu membuat batasan untuk aplikasi kita.

Misalnya, kita tidak ingin membuat gambar yang tidak layak untuk lingkungan kerja, atau yang tidak cocok untuk anak-anak.

Kita bisa melakukan ini dengan _metaprompt_. Metaprompt adalah prompt teks yang digunakan untuk mengontrol output dari model AI Generatif. Misalnya, kita bisa menggunakan metaprompt untuk memastikan gambar yang dihasilkan aman untuk lingkungan kerja, atau cocok untuk anak-anak.

### Cara kerjanya

Jadi, bagaimana cara kerja meta prompt?

Meta prompt adalah prompt teks yang digunakan untuk mengontrol output dari model AI Generatif, ditempatkan sebelum prompt utama, dan digunakan untuk mengatur output model serta diintegrasikan ke aplikasi untuk mengontrol output model. Prompt utama dan meta prompt digabungkan dalam satu prompt teks.

Salah satu contoh meta prompt adalah berikut:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Sekarang, mari kita lihat cara menggunakan meta prompt di demo kita.

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

Dari prompt di atas, kamu bisa lihat semua gambar yang dibuat mempertimbangkan metaprompt.

## Tugas - mari beri kesempatan pada siswa

Kita sudah memperkenalkan Edu4All di awal pelajaran ini. Sekarang saatnya memberi kesempatan pada siswa untuk membuat gambar untuk tugas mereka.

Siswa akan membuat gambar untuk tugas mereka yang berisi monumen, monumen apa saja terserah siswa. Siswa diminta untuk berkreasi dalam menempatkan monumen tersebut di berbagai konteks.

## Solusi

Berikut salah satu solusi yang mungkin:

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

## Kerja Bagus! Lanjutkan Belajar
Setelah menyelesaikan pelajaran ini, cek [koleksi Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan Anda tentang AI Generatif!

Lanjutkan ke Pelajaran 10 di mana kita akan membahas cara [membangun aplikasi AI dengan low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Disclaimer**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan terjemahan yang akurat, harap diketahui bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemah profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.