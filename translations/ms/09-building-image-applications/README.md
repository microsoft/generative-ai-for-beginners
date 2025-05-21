<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:18:56+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ms"
}
-->
# Membina Aplikasi Penjanaan Imej

Terdapat lebih banyak perkara dalam LLM daripada penjanaan teks. Ia juga mungkin untuk menjana imej daripada deskripsi teks. Mempunyai imej sebagai satu modaliti boleh sangat berguna dalam beberapa bidang dari MedTech, seni bina, pelancongan, pembangunan permainan dan banyak lagi. Dalam bab ini, kita akan melihat dua model penjanaan imej yang paling popular, DALL-E dan Midjourney.

## Pengenalan

Dalam pelajaran ini, kita akan merangkumi:

- Penjanaan imej dan mengapa ia berguna.
- DALL-E dan Midjourney, apa mereka, dan bagaimana mereka berfungsi.
- Bagaimana anda akan membina aplikasi penjanaan imej.

## Matlamat Pembelajaran

Selepas melengkapkan pelajaran ini, anda akan dapat:

- Membina aplikasi penjanaan imej.
- Menentukan sempadan untuk aplikasi anda dengan meta prompts.
- Bekerja dengan DALL-E dan Midjourney.

## Mengapa membina aplikasi penjanaan imej?

Aplikasi penjanaan imej adalah cara yang hebat untuk meneroka keupayaan AI Generatif. Mereka boleh digunakan untuk, sebagai contoh:

- **Penyuntingan dan sintesis imej**. Anda boleh menjana imej untuk pelbagai kes penggunaan, seperti penyuntingan imej dan sintesis imej.

- **Diterapkan kepada pelbagai industri**. Mereka juga boleh digunakan untuk menjana imej untuk pelbagai industri seperti Medtech, Pelancongan, Pembangunan permainan dan banyak lagi.

## Senario: Edu4All

Sebagai sebahagian daripada pelajaran ini, kita akan terus bekerjasama dengan startup kita, Edu4All, dalam pelajaran ini. Para pelajar akan mencipta imej untuk penilaian mereka, imej yang tepat terpulang kepada pelajar, tetapi mereka boleh menjadi ilustrasi untuk dongeng mereka sendiri atau mencipta watak baru untuk cerita mereka atau membantu mereka menggambarkan idea dan konsep mereka.

Berikut adalah apa yang boleh dihasilkan oleh pelajar Edu4All jika mereka bekerja di kelas mengenai monumen:

menggunakan prompt seperti

> "Anjing di sebelah Menara Eiffel pada cahaya matahari pagi awal"

## Apakah DALL-E dan Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) dan [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) adalah dua model penjanaan imej yang paling popular, mereka membenarkan anda menggunakan prompt untuk menjana imej.

### DALL-E

Mari kita mulakan dengan DALL-E, yang merupakan model AI Generatif yang menjana imej dari deskripsi teks.

- **CLIP**, adalah model yang menjana embeddings, yang merupakan perwakilan data numerik, dari imej dan teks.

- **Perhatian tersebar**, adalah model yang menjana imej dari embeddings. DALL-E dilatih pada dataset imej dan teks dan boleh digunakan untuk menjana imej dari deskripsi teks. Sebagai contoh, DALL-E boleh digunakan untuk menjana imej kucing dalam topi, atau anjing dengan mohawk.

### Midjourney

Midjourney berfungsi dengan cara yang sama seperti DALL-E, ia menjana imej dari prompt teks. Midjourney, juga boleh digunakan untuk menjana imej menggunakan prompt seperti "kucing dalam topi", atau "anjing dengan mohawk".

## Bagaimana DALL-E dan Midjourney Berfungsi

Pertama, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E adalah model AI Generatif berdasarkan seni bina transformer dengan _transformer autoregresif_.

_Transformer autoregresif_ mendefinisikan bagaimana model menjana imej dari deskripsi teks, ia menjana satu piksel pada satu masa, dan kemudian menggunakan piksel yang dijana untuk menjana piksel seterusnya. Melalui beberapa lapisan dalam rangkaian neural, sehingga imej selesai.

Dengan proses ini, DALL-E, mengawal atribut, objek, ciri, dan lebih banyak lagi dalam imej yang dihasilkannya. Walau bagaimanapun, DALL-E 2 dan 3 mempunyai lebih banyak kawalan ke atas imej yang dijana.

## Membina aplikasi penjanaan imej pertama anda

Jadi apa yang diperlukan untuk membina aplikasi penjanaan imej? Anda memerlukan perpustakaan berikut:

- **python-dotenv**, sangat disyorkan untuk menggunakan perpustakaan ini untuk menyimpan rahsia anda dalam fail _.env_ jauh dari kod.
- **openai**, perpustakaan ini adalah apa yang anda akan gunakan untuk berinteraksi dengan API OpenAI.
- **pillow**, untuk bekerja dengan imej dalam Python.
- **requests**, untuk membantu anda membuat permintaan HTTP.

1. Buat fail _.env_ dengan kandungan berikut:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Cari maklumat ini di Azure Portal untuk sumber anda dalam bahagian "Kunci dan Endpoint".

1. Kumpulkan perpustakaan di atas dalam fail yang dipanggil _requirements.txt_ seperti berikut:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Seterusnya, buat persekitaran maya dan pasang perpustakaan:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Untuk Windows, gunakan arahan berikut untuk membuat dan mengaktifkan persekitaran maya anda:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Tambahkan kod berikut dalam fail yang dipanggil _app.py_:

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

Mari kita terangkan kod ini:

- Pertama, kita import perpustakaan yang kita perlukan, termasuk perpustakaan OpenAI, perpustakaan dotenv, perpustakaan requests, dan perpustakaan Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Seterusnya, kita memuatkan pembolehubah persekitaran dari fail _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Selepas itu, kita menetapkan endpoint, kunci untuk API OpenAI, versi dan jenis.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Seterusnya, kita menjana imej:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Kod di atas membalas dengan objek JSON yang mengandungi URL imej yang dijana. Kita boleh menggunakan URL untuk memuat turun imej dan menyimpannya ke fail.

- Akhirnya, kita membuka imej dan menggunakan penonton imej standard untuk memaparkannya:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Lebih banyak butiran mengenai penjanaan imej

Mari kita lihat kod yang menjana imej dengan lebih terperinci:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, adalah prompt teks yang digunakan untuk menjana imej. Dalam kes ini, kita menggunakan prompt "Arnab di atas kuda, memegang lollipop, di padang berkabus di mana ia tumbuh daffodils".
- **size**, adalah saiz imej yang dijana. Dalam kes ini, kita menjana imej yang berukuran 1024x1024 piksel.
- **n**, adalah bilangan imej yang dijana. Dalam kes ini, kita menjana dua imej.
- **temperature**, adalah parameter yang mengawal kebolehacakan output model AI Generatif. Suhu adalah nilai antara 0 dan 1 di mana 0 bermaksud output adalah deterministik dan 1 bermaksud output adalah acak. Nilai lalai adalah 0.7.

Terdapat lebih banyak perkara yang boleh anda lakukan dengan imej yang akan kita bincangkan dalam bahagian seterusnya.

## Keupayaan tambahan penjanaan imej

Anda telah melihat setakat ini bagaimana kita dapat menjana imej menggunakan beberapa baris dalam Python. Walau bagaimanapun, terdapat lebih banyak perkara yang boleh anda lakukan dengan imej.

Anda juga boleh melakukan perkara berikut:

- **Melakukan penyuntingan**. Dengan menyediakan imej sedia ada, topeng dan prompt, anda boleh mengubah imej. Sebagai contoh, anda boleh menambah sesuatu kepada sebahagian imej. Bayangkan imej arnab kita, anda boleh menambah topi kepada arnab. Bagaimana anda akan melakukannya adalah dengan menyediakan imej, topeng (mengenal pasti bahagian kawasan untuk perubahan) dan prompt teks untuk mengatakan apa yang perlu dilakukan.

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

  Imej asas hanya akan mengandungi arnab tetapi imej akhir akan mempunyai topi pada arnab.

- **Mencipta variasi**. Idea ini adalah anda mengambil imej sedia ada dan meminta variasi dicipta. Untuk mencipta variasi, anda menyediakan imej dan prompt teks dan kod seperti berikut:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Nota, ini hanya disokong pada OpenAI

## Suhu

Suhu adalah parameter yang mengawal kebolehacakan output model AI Generatif. Suhu adalah nilai antara 0 dan 1 di mana 0 bermaksud output adalah deterministik dan 1 bermaksud output adalah acak. Nilai lalai adalah 0.7.

Mari kita lihat contoh bagaimana suhu berfungsi, dengan menjalankan prompt ini dua kali:

> Prompt : "Arnab di atas kuda, memegang lollipop, di padang berkabus di mana ia tumbuh daffodils"

Sekarang mari kita jalankan prompt yang sama hanya untuk melihat bahawa kita tidak akan mendapat imej yang sama dua kali:

Seperti yang anda lihat, imej adalah serupa, tetapi tidak sama. Mari kita cuba mengubah nilai suhu kepada 0.1 dan lihat apa yang berlaku:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Mengubah suhu

Jadi mari kita cuba membuat tindak balas lebih deterministik. Kita boleh melihat dari dua imej yang kita hasilkan bahawa dalam imej pertama, ada arnab dan dalam imej kedua, ada kuda, jadi imej berbeza dengan ketara.

Oleh itu, mari kita ubah kod kita dan tetapkan suhu kepada 0, seperti berikut:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Sekarang apabila anda menjalankan kod ini, anda mendapat dua imej ini:

Di sini anda boleh dengan jelas melihat bagaimana imej lebih menyerupai satu sama lain.

## Bagaimana untuk menentukan sempadan untuk aplikasi anda dengan metaprompts

Dengan demo kita, kita sudah boleh menjana imej untuk pelanggan kita. Walau bagaimanapun, kita perlu membuat beberapa sempadan untuk aplikasi kita.

Sebagai contoh, kita tidak mahu menjana imej yang tidak selamat untuk kerja, atau yang tidak sesuai untuk kanak-kanak.

Kita boleh melakukan ini dengan _metaprompts_. Metaprompts adalah prompt teks yang digunakan untuk mengawal output model AI Generatif. Sebagai contoh, kita boleh menggunakan metaprompts untuk mengawal output, dan memastikan bahawa imej yang dijana adalah selamat untuk kerja, atau sesuai untuk kanak-kanak.

### Bagaimana ia berfungsi?

Sekarang, bagaimana metaprompts berfungsi?

Metaprompts adalah prompt teks yang digunakan untuk mengawal output model AI Generatif, mereka diletakkan sebelum prompt teks, dan digunakan untuk mengawal output model dan dibenamkan dalam aplikasi untuk mengawal output model. Menggabungkan input prompt dan input metaprompt dalam satu prompt teks.

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

Sekarang, mari kita lihat bagaimana kita boleh menggunakan metaprompts dalam demo kita.

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

Dari prompt di atas, anda boleh melihat bagaimana semua imej yang dihasilkan mempertimbangkan metaprompt.

## Tugasan - mari kita aktifkan pelajar

Kami memperkenalkan Edu4All pada permulaan pelajaran ini. Sekarang sudah tiba masanya untuk membolehkan pelajar menjana imej untuk penilaian mereka.

Pelajar akan mencipta imej untuk penilaian mereka yang mengandungi monumen, monumen yang tepat terpulang kepada pelajar. Pelajar diminta menggunakan kreativiti mereka dalam tugasan ini untuk meletakkan monumen ini dalam konteks yang berbeza.

## Penyelesaian

Berikut adalah satu penyelesaian yang mungkin:

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

## Kerja Hebat! Teruskan Pembelajaran Anda

Selepas melengkapkan pelajaran ini, semak koleksi pembelajaran AI Generatif kami [di sini](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk terus meningkatkan pengetahuan AI Generatif anda!

Pergi ke Pelajaran 10 di mana kita akan melihat bagaimana untuk [membina aplikasi AI dengan kod rendah](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.