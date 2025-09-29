<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T21:50:51+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ms"
}
-->
# Membina Aplikasi Penjanaan Imej

[![Membina Aplikasi Penjanaan Imej](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.ms.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM bukan hanya untuk penjanaan teks. Ia juga boleh digunakan untuk menjana imej daripada deskripsi teks. Mempunyai imej sebagai satu modaliti boleh menjadi sangat berguna dalam pelbagai bidang seperti MedTech, seni bina, pelancongan, pembangunan permainan, dan banyak lagi. Dalam bab ini, kita akan melihat dua model penjanaan imej yang paling popular, DALL-E dan Midjourney.

## Pengenalan

Dalam pelajaran ini, kita akan membincangkan:

- Penjanaan imej dan mengapa ia berguna.
- DALL-E dan Midjourney, apa itu dan bagaimana ia berfungsi.
- Cara membina aplikasi penjanaan imej.

## Matlamat Pembelajaran

Selepas menyelesaikan pelajaran ini, anda akan dapat:

- Membina aplikasi penjanaan imej.
- Menentukan sempadan untuk aplikasi anda dengan meta prompt.
- Bekerja dengan DALL-E dan Midjourney.

## Mengapa membina aplikasi penjanaan imej?

Aplikasi penjanaan imej adalah cara yang hebat untuk meneroka keupayaan AI Generatif. Ia boleh digunakan untuk, sebagai contoh:

- **Penyuntingan dan sintesis imej**. Anda boleh menjana imej untuk pelbagai kegunaan seperti penyuntingan imej dan sintesis imej.

- **Digunakan dalam pelbagai industri**. Ia juga boleh digunakan untuk menjana imej untuk pelbagai industri seperti MedTech, Pelancongan, Pembangunan Permainan, dan banyak lagi.

## Senario: Edu4All

Sebagai sebahagian daripada pelajaran ini, kita akan terus bekerja dengan startup kita, Edu4All. Pelajar akan mencipta imej untuk penilaian mereka, jenis imej yang akan dihasilkan bergantung kepada pelajar, tetapi mereka boleh membuat ilustrasi untuk dongeng mereka sendiri, mencipta watak baru untuk cerita mereka, atau membantu mereka menggambarkan idea dan konsep mereka.

Berikut adalah contoh imej yang boleh dihasilkan oleh pelajar Edu4All jika mereka sedang belajar tentang monumen di kelas:

![Startup Edu4All, kelas tentang monumen, Menara Eiffel](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.ms.png)

menggunakan prompt seperti

> "Anjing di sebelah Menara Eiffel pada waktu pagi yang cerah"

## Apa itu DALL-E dan Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) dan [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) adalah dua model penjanaan imej yang paling popular, yang membolehkan anda menggunakan prompt untuk menjana imej.

### DALL-E

Mari kita mulakan dengan DALL-E, iaitu model AI Generatif yang menjana imej daripada deskripsi teks.

> [DALL-E adalah gabungan dua model, CLIP dan perhatian tersebar](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, adalah model yang menjana embedding, iaitu representasi numerik data, daripada imej dan teks.

- **Perhatian tersebar**, adalah model yang menjana imej daripada embedding. DALL-E dilatih menggunakan dataset imej dan teks dan boleh digunakan untuk menjana imej daripada deskripsi teks. Sebagai contoh, DALL-E boleh digunakan untuk menjana imej kucing memakai topi, atau anjing dengan gaya rambut mohawk.

### Midjourney

Midjourney berfungsi dengan cara yang sama seperti DALL-E, ia menjana imej daripada prompt teks. Midjourney juga boleh digunakan untuk menjana imej menggunakan prompt seperti "kucing memakai topi", atau "anjing dengan gaya rambut mohawk".

![Imej yang dijana oleh Midjourney, burung merpati mekanikal](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Kredit imej Wikipedia, imej dijana oleh Midjourney_

## Bagaimana DALL-E dan Midjourney Berfungsi

Pertama, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E adalah model AI Generatif berdasarkan seni bina transformer dengan _transformer autoregresif_.

_Transformer autoregresif_ menentukan bagaimana model menjana imej daripada deskripsi teks, ia menjana satu piksel pada satu masa, dan kemudian menggunakan piksel yang dijana untuk menjana piksel seterusnya. Proses ini melalui beberapa lapisan dalam rangkaian neural sehingga imej selesai.

Dengan proses ini, DALL-E mengawal atribut, objek, ciri, dan banyak lagi dalam imej yang dijana. Walau bagaimanapun, DALL-E 2 dan 3 mempunyai kawalan yang lebih besar terhadap imej yang dijana.

## Membina aplikasi penjanaan imej pertama anda

Jadi, apa yang diperlukan untuk membina aplikasi penjanaan imej? Anda memerlukan perpustakaan berikut:

- **python-dotenv**, sangat disarankan untuk menggunakan perpustakaan ini untuk menyimpan rahsia anda dalam fail _.env_ jauh daripada kod.
- **openai**, perpustakaan ini digunakan untuk berinteraksi dengan API OpenAI.
- **pillow**, untuk bekerja dengan imej dalam Python.
- **requests**, untuk membantu anda membuat permintaan HTTP.

## Cipta dan terapkan model Azure OpenAI

Jika belum dilakukan, ikuti arahan di halaman [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) untuk mencipta sumber dan model Azure OpenAI. Pilih DALL-E 3 sebagai model.  

## Cipta aplikasi

1. Cipta fail _.env_ dengan kandungan berikut:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Cari maklumat ini di Portal Azure OpenAI Foundry untuk sumber anda dalam bahagian "Deployments".

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

1. Tambahkan kod berikut dalam fail bernama _app.py_:

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

Mari kita terangkan kod ini:

- Pertama, kita import perpustakaan yang diperlukan, termasuk perpustakaan OpenAI, dotenv, requests, dan Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Seterusnya, kita memuatkan pembolehubah persekitaran daripada fail _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Selepas itu, kita mengkonfigurasi klien perkhidmatan Azure OpenAI.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Seterusnya, kita menjana imej:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Kod di atas memberikan respons dalam bentuk objek JSON yang mengandungi URL imej yang dijana. Kita boleh menggunakan URL tersebut untuk memuat turun imej dan menyimpannya ke fail.

- Akhir sekali, kita membuka imej dan menggunakan penonton imej standard untuk memaparkannya:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Maklumat lanjut tentang penjanaan imej

Mari kita lihat kod yang menjana imej dengan lebih terperinci:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, adalah teks prompt yang digunakan untuk menjana imej. Dalam kes ini, kita menggunakan prompt "Arnab di atas kuda, memegang lolipop, di padang berkabus di mana tumbuh bunga daffodil".
- **size**, adalah saiz imej yang dijana. Dalam kes ini, kita menjana imej bersaiz 1024x1024 piksel.
- **n**, adalah bilangan imej yang dijana. Dalam kes ini, kita menjana dua imej.
- **temperature**, adalah parameter yang mengawal kebarangkalian output model AI Generatif. Nilai temperature adalah antara 0 dan 1 di mana 0 bermaksud output adalah deterministik dan 1 bermaksud output adalah rawak. Nilai lalai adalah 0.7.

Terdapat lebih banyak perkara yang boleh dilakukan dengan imej yang akan kita bincangkan dalam bahagian seterusnya.

## Keupayaan tambahan penjanaan imej

Anda telah melihat bagaimana kita dapat menjana imej menggunakan beberapa baris kod dalam Python. Walau bagaimanapun, terdapat lebih banyak perkara yang boleh dilakukan dengan imej.

Anda juga boleh melakukan perkara berikut:

- **Melakukan penyuntingan**. Dengan memberikan imej sedia ada, topeng, dan prompt, anda boleh mengubah imej. Sebagai contoh, anda boleh menambah sesuatu pada bahagian imej. Bayangkan imej arnab kita, anda boleh menambah topi pada arnab. Cara melakukannya adalah dengan memberikan imej, topeng (mengenal pasti bahagian kawasan untuk perubahan) dan prompt teks untuk mengatakan apa yang perlu dilakukan. 
> Nota: ini tidak disokong dalam DALL-E 3. 
 
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

  Imej asas hanya akan mengandungi ruang santai dengan kolam tetapi imej akhir akan mempunyai flamingo:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.ms.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.ms.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.ms.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Mencipta variasi**. Ideanya adalah anda mengambil imej sedia ada dan meminta variasi dicipta. Untuk mencipta variasi, anda memberikan imej dan prompt teks serta kod seperti berikut:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Nota, ini hanya disokong pada OpenAI

## Temperature

Temperature adalah parameter yang mengawal kebarangkalian output model AI Generatif. Nilai temperature adalah antara 0 dan 1 di mana 0 bermaksud output adalah deterministik dan 1 bermaksud output adalah rawak. Nilai lalai adalah 0.7.

Mari kita lihat contoh bagaimana temperature berfungsi, dengan menjalankan prompt ini dua kali:

> Prompt : "Arnab di atas kuda, memegang lolipop, di padang berkabus di mana tumbuh bunga daffodil"

![Arnab di atas kuda memegang lolipop, versi 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.ms.png)

Sekarang mari kita jalankan prompt yang sama untuk melihat bahawa kita tidak akan mendapat imej yang sama dua kali:

![Imej yang dijana arnab di atas kuda](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.ms.png)

Seperti yang anda lihat, imej-imej tersebut serupa, tetapi tidak sama. Mari kita cuba ubah nilai temperature kepada 0.1 dan lihat apa yang berlaku:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Mengubah temperature

Jadi mari kita cuba membuat respons lebih deterministik. Kita dapat melihat daripada dua imej yang dijana bahawa dalam imej pertama, terdapat arnab dan dalam imej kedua, terdapat kuda, jadi imej-imej tersebut berbeza dengan ketara.

Oleh itu, mari kita ubah kod kita dan tetapkan temperature kepada 0, seperti berikut:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Sekarang apabila anda menjalankan kod ini, anda akan mendapat dua imej berikut:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.ms.png)
- ![Temperature 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.ms.png)

Di sini anda dapat melihat dengan jelas bagaimana imej-imej tersebut lebih menyerupai satu sama lain.

## Cara menentukan sempadan untuk aplikasi anda dengan metaprompt

Dengan demo kita, kita sudah boleh menjana imej untuk pelanggan kita. Walau bagaimanapun, kita perlu mencipta beberapa sempadan untuk aplikasi kita.

Sebagai contoh, kita tidak mahu menjana imej yang tidak sesuai untuk tempat kerja, atau yang tidak sesuai untuk kanak-kanak.

Kita boleh melakukan ini dengan _metaprompt_. Metaprompt adalah teks prompt yang digunakan untuk mengawal output model AI Generatif. Sebagai contoh, kita boleh menggunakan metaprompt untuk mengawal output, dan memastikan imej yang dijana sesuai untuk tempat kerja, atau sesuai untuk kanak-kanak.

### Bagaimana ia berfungsi?

Sekarang, bagaimana metaprompt berfungsi?

Metaprompt adalah teks prompt yang digunakan untuk mengawal output model AI Generatif, ia diletakkan sebelum teks prompt, dan digunakan untuk mengawal output model serta disematkan dalam aplikasi untuk mengawal output model. Menggabungkan input prompt dan input metaprompt dalam satu teks prompt.

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

Sekarang, mari kita lihat bagaimana kita boleh menggunakan metaprompt dalam demo kita.

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

Daripada prompt di atas, anda dapat melihat bagaimana semua imej yang dihasilkan mengambil kira metaprompt.

## Tugasan - mari kita bantu pelajar

Kami memperkenalkan Edu4All pada permulaan pelajaran ini. Sekarang tiba masanya untuk membolehkan pelajar menjana imej untuk penilaian mereka.

Pelajar akan mencipta imej untuk penilaian mereka yang mengandungi monumen, jenis monumen yang akan dihasilkan bergantung kepada pelajar. Pelajar diminta menggunakan kreativiti mereka dalam tugasan ini untuk meletakkan monumen ini dalam konteks yang berbeza.

## Penyelesaian

Berikut adalah satu penyelesaian yang mungkin:
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

## Kerja Hebat! Teruskan Pembelajaran Anda

Selepas menyelesaikan pelajaran ini, lihat koleksi [Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kami untuk terus meningkatkan pengetahuan anda tentang AI Generatif!

Pergi ke Pelajaran 10 di mana kita akan melihat cara [membina aplikasi AI dengan kod rendah](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.