<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a7fd0f95f9eb673b79da47c0814f4d4",
  "translation_date": "2025-07-09T13:30:23+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ms"
}
-->
# Membangunkan Aplikasi Penjanaan Imej

[![Membangunkan Aplikasi Penjanaan Imej](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.ms.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM bukan sahaja untuk penjanaan teks. Ia juga boleh digunakan untuk menjana imej daripada deskripsi teks. Mempunyai imej sebagai modaliti boleh sangat berguna dalam pelbagai bidang seperti MedTech, seni bina, pelancongan, pembangunan permainan dan banyak lagi. Dalam bab ini, kita akan melihat dua model penjanaan imej yang paling popular, DALL-E dan Midjourney.

## Pengenalan

Dalam pelajaran ini, kita akan membincangkan:

- Penjanaan imej dan mengapa ia berguna.
- DALL-E dan Midjourney, apa itu, dan bagaimana ia berfungsi.
- Cara membina aplikasi penjanaan imej.

## Matlamat Pembelajaran

Selepas menamatkan pelajaran ini, anda akan dapat:

- Membangunkan aplikasi penjanaan imej.
- Menetapkan had untuk aplikasi anda dengan meta prompt.
- Bekerja dengan DALL-E dan Midjourney.

## Mengapa membina aplikasi penjanaan imej?

Aplikasi penjanaan imej adalah cara yang baik untuk meneroka keupayaan Generative AI. Ia boleh digunakan untuk, contohnya:

- **Penyuntingan dan sintesis imej**. Anda boleh menjana imej untuk pelbagai kegunaan, seperti penyuntingan imej dan sintesis imej.

- **Digunakan dalam pelbagai industri**. Ia juga boleh digunakan untuk menjana imej bagi pelbagai industri seperti Medtech, Pelancongan, Pembangunan permainan dan banyak lagi.

## Senario: Edu4All

Sebahagian daripada pelajaran ini, kita akan terus bekerja dengan startup kita, Edu4All. Pelajar akan mencipta imej untuk penilaian mereka, imej apa yang dihasilkan terpulang kepada pelajar, tetapi ia boleh menjadi ilustrasi untuk cerita dongeng mereka sendiri atau mencipta watak baru untuk cerita mereka atau membantu mereka memvisualisasikan idea dan konsep mereka.

Ini adalah contoh apa yang boleh dihasilkan oleh pelajar Edu4All jika mereka bekerja dalam kelas mengenai monumen:

![Edu4All startup, kelas mengenai monumen, Menara Eiffel](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.ms.png)

menggunakan prompt seperti

> "Anjing di sebelah Menara Eiffel pada cahaya matahari pagi awal"

## Apa itu DALL-E dan Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) dan [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) adalah dua model penjanaan imej yang paling popular, mereka membolehkan anda menggunakan prompt untuk menjana imej.

### DALL-E

Mari mulakan dengan DALL-E, ia adalah model Generative AI yang menjana imej daripada deskripsi teks.

> [DALL-E adalah gabungan dua model, CLIP dan diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, adalah model yang menjana embeddings, iaitu representasi berangka bagi data, daripada imej dan teks.

- **Diffused attention**, adalah model yang menjana imej daripada embeddings. DALL-E dilatih menggunakan dataset imej dan teks dan boleh digunakan untuk menjana imej daripada deskripsi teks. Contohnya, DALL-E boleh digunakan untuk menjana imej kucing memakai topi, atau anjing dengan mohawk.

### Midjourney

Midjourney berfungsi dengan cara yang serupa dengan DALL-E, ia menjana imej daripada prompt teks. Midjourney juga boleh digunakan untuk menjana imej menggunakan prompt seperti “kucing memakai topi”, atau “anjing dengan mohawk”.

![Imej dijana oleh Midjourney, merpati mekanikal](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Kredit imej Wikipedia, imej dijana oleh Midjourney_

## Bagaimana DALL-E dan Midjourney Berfungsi

Mula-mula, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E adalah model Generative AI berasaskan seni bina transformer dengan _autoregressive transformer_.

Sebuah _autoregressive transformer_ menentukan bagaimana model menjana imej daripada deskripsi teks, ia menjana satu piksel pada satu masa, kemudian menggunakan piksel yang dijana untuk menjana piksel seterusnya. Melalui beberapa lapisan dalam rangkaian neural, sehingga imej lengkap.

Dengan proses ini, DALL-E mengawal atribut, objek, ciri-ciri, dan banyak lagi dalam imej yang dijananya. Walau bagaimanapun, DALL-E 2 dan 3 mempunyai kawalan yang lebih baik ke atas imej yang dijana.

## Membangunkan aplikasi penjanaan imej pertama anda

Jadi, apa yang diperlukan untuk membina aplikasi penjanaan imej? Anda memerlukan perpustakaan berikut:

- **python-dotenv**, sangat disarankan untuk menggunakan perpustakaan ini untuk menyimpan rahsia anda dalam fail _.env_ jauh dari kod.
- **openai**, perpustakaan ini digunakan untuk berinteraksi dengan OpenAI API.
- **pillow**, untuk bekerja dengan imej dalam Python.
- **requests**, untuk membantu membuat permintaan HTTP.

1. Cipta fail _.env_ dengan kandungan berikut:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Cari maklumat ini di Azure Portal untuk sumber anda dalam bahagian "Keys and Endpoint".

1. Kumpulkan perpustakaan di atas dalam fail bernama _requirements.txt_ seperti berikut:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Seterusnya, cipta persekitaran maya dan pasang perpustakaan:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Untuk Windows, gunakan arahan berikut untuk mencipta dan mengaktifkan persekitaran maya anda:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Tambah kod berikut dalam fail bernama _app.py_:

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

Mari terangkan kod ini:

- Pertama, kita import perpustakaan yang diperlukan, termasuk perpustakaan OpenAI, dotenv, requests, dan Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Seterusnya, kita muatkan pembolehubah persekitaran dari fail _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Selepas itu, kita tetapkan endpoint, kunci untuk OpenAI API, versi dan jenis.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Seterusnya, kita jana imej:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Kod di atas membalas dengan objek JSON yang mengandungi URL imej yang dijana. Kita boleh menggunakan URL tersebut untuk memuat turun imej dan menyimpannya ke fail.

- Akhir sekali, kita buka imej dan gunakan penonton imej standard untuk memaparkannya:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Maklumat lanjut tentang penjanaan imej

Mari lihat kod yang menjana imej dengan lebih terperinci:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, adalah teks prompt yang digunakan untuk menjana imej. Dalam kes ini, kita menggunakan prompt "Arnab di atas kuda, memegang lollipop, di padang berkabus di mana tumbuh bunga daffodil".
- **size**, adalah saiz imej yang dijana. Dalam kes ini, kita menjana imej bersaiz 1024x1024 piksel.
- **n**, adalah bilangan imej yang dijana. Dalam kes ini, kita menjana dua imej.
- **temperature**, adalah parameter yang mengawal kebarangkalian output model Generative AI. Nilai temperature antara 0 dan 1 di mana 0 bermaksud output adalah deterministik dan 1 bermaksud output adalah rawak. Nilai lalai adalah 0.7.

Terdapat lebih banyak perkara yang boleh anda lakukan dengan imej yang akan kita bincangkan dalam bahagian seterusnya.

## Keupayaan tambahan penjanaan imej

Anda telah melihat bagaimana kita dapat menjana imej menggunakan beberapa baris kod Python. Namun, terdapat lebih banyak perkara yang boleh dilakukan dengan imej.

Anda juga boleh melakukan perkara berikut:

- **Melakukan penyuntingan**. Dengan menyediakan imej sedia ada, topeng (mask) dan prompt, anda boleh mengubah imej. Contohnya, anda boleh menambah sesuatu pada sebahagian imej. Bayangkan imej arnab kita, anda boleh menambah topi pada arnab tersebut. Cara melakukannya adalah dengan menyediakan imej, topeng (menandakan bahagian yang hendak diubah) dan prompt teks untuk menyatakan apa yang perlu dilakukan.

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

  Imej asas hanya mengandungi arnab tetapi imej akhir akan mempunyai topi pada arnab tersebut.

- **Mencipta variasi**. Idea adalah anda mengambil imej sedia ada dan meminta variasi dicipta. Untuk mencipta variasi, anda menyediakan imej dan prompt teks serta kod seperti berikut:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Nota, ini hanya disokong oleh OpenAI

## Temperature

Temperature adalah parameter yang mengawal kebarangkalian output model Generative AI. Nilai temperature antara 0 dan 1 di mana 0 bermaksud output adalah deterministik dan 1 bermaksud output adalah rawak. Nilai lalai adalah 0.7.

Mari lihat contoh bagaimana temperature berfungsi, dengan menjalankan prompt ini dua kali:

> Prompt : "Arnab di atas kuda, memegang lollipop, di padang berkabus di mana tumbuh bunga daffodil"

![Arnab di atas kuda memegang lollipop, versi 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.ms.png)

Sekarang mari jalankan prompt yang sama sekali lagi untuk melihat bahawa kita tidak akan mendapat imej yang sama dua kali:

![Imej dijana arnab di atas kuda](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.ms.png)

Seperti yang anda lihat, imej adalah serupa, tetapi tidak sama. Mari cuba tukar nilai temperature kepada 0.1 dan lihat apa yang berlaku:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Menukar temperature

Jadi mari kita cuba buat respons lebih deterministik. Kita boleh perhatikan dari dua imej yang dijana bahawa imej pertama ada arnab dan imej kedua ada kuda, jadi imej berbeza dengan ketara.

Oleh itu, mari kita tukar kod dan tetapkan temperature kepada 0, seperti berikut:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Sekarang apabila anda jalankan kod ini, anda akan dapat dua imej ini:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.ms.png)
- ![Temperature 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.ms.png)

Di sini anda boleh lihat dengan jelas bagaimana imej lebih menyerupai antara satu sama lain.

## Cara menetapkan had untuk aplikasi anda dengan metaprompt

Dengan demo kita, kita sudah boleh menjana imej untuk pelanggan kita. Namun, kita perlu menetapkan beberapa had untuk aplikasi kita.

Contohnya, kita tidak mahu menjana imej yang tidak sesuai untuk tempat kerja, atau yang tidak sesuai untuk kanak-kanak.

Kita boleh lakukan ini dengan _metaprompt_. Metaprompt adalah prompt teks yang digunakan untuk mengawal output model Generative AI. Contohnya, kita boleh gunakan metaprompt untuk mengawal output dan memastikan imej yang dijana selamat untuk tempat kerja, atau sesuai untuk kanak-kanak.

### Bagaimana ia berfungsi?

Jadi, bagaimana metaprompt berfungsi?

Metaprompt adalah prompt teks yang digunakan untuk mengawal output model Generative AI, ia diletakkan sebelum prompt teks, dan digunakan untuk mengawal output model serta disematkan dalam aplikasi untuk mengawal output model. Ia menggabungkan input prompt dan input metaprompt dalam satu prompt teks.

Satu contoh metaprompt adalah seperti berikut:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Sekarang, mari lihat bagaimana kita boleh gunakan metaprompt dalam demo kita.

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

Daripada prompt di atas, anda boleh lihat bagaimana semua imej yang dihasilkan mengambil kira metaprompt.

## Tugasan - mari beri kuasa kepada pelajar

Kita telah memperkenalkan Edu4All pada awal pelajaran ini. Kini tiba masanya untuk membolehkan pelajar menjana imej untuk penilaian mereka.

Pelajar akan mencipta imej untuk penilaian mereka yang mengandungi monumen, monumen apa yang dipilih terpulang kepada pelajar. Pelajar diminta menggunakan kreativiti mereka dalam tugasan ini untuk meletakkan monumen-monumen ini dalam konteks yang berbeza.

## Penyelesaian

Ini adalah satu penyelesaian yang mungkin:

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

prompt = f"""{meta_prompt}
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

## Kerja Hebat! Teruskan Pembelajaran Anda

Selepas menamatkan pelajaran ini, lihat koleksi [Pembelajaran Generative AI kami](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk terus meningkatkan pengetahuan Generative AI anda!

Teruskan ke Pelajaran 10 di mana kita akan melihat cara untuk [membangunkan aplikasi AI dengan low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.