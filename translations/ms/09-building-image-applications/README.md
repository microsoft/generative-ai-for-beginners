<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef74ad58fc01f7ad80788f79505f9816",
  "translation_date": "2025-08-26T18:27:39+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ms"
}
-->
# Membina Aplikasi Penjanaan Imej

[![Membina Aplikasi Penjanaan Imej](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.ms.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM bukan sahaja untuk penjanaan teks. Ia juga boleh digunakan untuk menjana imej daripada deskripsi teks. Mempunyai imej sebagai satu mod sangat berguna dalam pelbagai bidang seperti MedTech, seni bina, pelancongan, pembangunan permainan dan banyak lagi. Dalam bab ini, kita akan melihat dua model penjanaan imej yang paling popular, DALL-E dan Midjourney.

## Pengenalan

Dalam pelajaran ini, kita akan pelajari:

- Penjanaan imej dan kenapa ia berguna.
- DALL-E dan Midjourney, apa itu dan bagaimana ia berfungsi.
- Cara membina aplikasi penjanaan imej.

## Matlamat Pembelajaran

Selepas melengkapkan pelajaran ini, anda akan dapat:

- Membina aplikasi penjanaan imej.
- Menetapkan sempadan untuk aplikasi anda dengan meta prompt.
- Bekerja dengan DALL-E dan Midjourney.

## Kenapa bina aplikasi penjanaan imej?

Aplikasi penjanaan imej adalah cara yang bagus untuk meneroka keupayaan AI Generatif. Ia boleh digunakan untuk, contohnya:

- **Penyuntingan dan sintesis imej**. Anda boleh menjana imej untuk pelbagai kegunaan, seperti penyuntingan imej dan sintesis imej.

- **Digunakan dalam pelbagai industri**. Ia juga boleh digunakan untuk menjana imej untuk pelbagai industri seperti Medtech, Pelancongan, Pembangunan Permainan dan banyak lagi.

## Senario: Edu4All

Sebagai sebahagian daripada pelajaran ini, kita akan terus bekerja dengan syarikat permulaan kita, Edu4All. Para pelajar akan mencipta imej untuk tugasan mereka, jenis imej terpulang kepada pelajar, tetapi mereka boleh membuat ilustrasi untuk dongeng mereka sendiri atau mencipta watak baru untuk cerita mereka atau membantu mereka menggambarkan idea dan konsep mereka.

Contohnya, inilah apa yang pelajar Edu4All boleh hasilkan jika mereka sedang belajar tentang monumen di dalam kelas:

![Edu4All startup, kelas tentang monumen, Menara Eiffel](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.ms.png)

menggunakan prompt seperti

> "Anjing di sebelah Menara Eiffel pada waktu pagi yang cerah"

## Apa itu DALL-E dan Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) dan [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) adalah dua model penjanaan imej yang paling popular, ia membolehkan anda menggunakan prompt untuk menjana imej.

### DALL-E

Mari kita mulakan dengan DALL-E, iaitu model AI Generatif yang menjana imej daripada deskripsi teks.

> [DALL-E adalah gabungan dua model, CLIP dan diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, adalah model yang menghasilkan embedding, iaitu representasi berangka data, daripada imej dan teks.

- **Diffused attention**, adalah model yang menjana imej daripada embedding. DALL-E dilatih menggunakan set data imej dan teks dan boleh digunakan untuk menjana imej daripada deskripsi teks. Contohnya, DALL-E boleh digunakan untuk menjana imej kucing memakai topi, atau anjing dengan mohawk.

### Midjourney

Midjourney berfungsi hampir sama seperti DALL-E, ia menjana imej daripada prompt teks. Midjourney juga boleh digunakan untuk menjana imej menggunakan prompt seperti “kucing memakai topi”, atau “anjing dengan mohawk”.

![Imej dijana oleh Midjourney, burung merpati mekanikal](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Kredit imej Wikipedia, imej dijana oleh Midjourney_

## Bagaimana DALL-E dan Midjourney Berfungsi

Pertama, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E adalah model AI Generatif berasaskan seni bina transformer dengan _autoregressive transformer_.

_Autoregressive transformer_ menentukan bagaimana model menjana imej daripada deskripsi teks, ia menjana satu piksel pada satu masa, dan kemudian menggunakan piksel yang telah dijana untuk menjana piksel seterusnya. Proses ini melalui beberapa lapisan dalam rangkaian neural, sehingga imej siap sepenuhnya.

Dengan proses ini, DALL-E mengawal atribut, objek, ciri-ciri, dan banyak lagi dalam imej yang dijana. Namun, DALL-E 2 dan 3 mempunyai kawalan yang lebih baik ke atas imej yang dihasilkan.

## Membina aplikasi penjanaan imej pertama anda

Jadi, apa yang diperlukan untuk membina aplikasi penjanaan imej? Anda perlukan perpustakaan berikut:

- **python-dotenv**, sangat disarankan untuk menggunakan perpustakaan ini supaya rahsia anda disimpan dalam fail _.env_ dan tidak bercampur dengan kod.
- **openai**, perpustakaan ini digunakan untuk berinteraksi dengan API OpenAI.
- **pillow**, untuk bekerja dengan imej dalam Python.
- **requests**, untuk membantu anda membuat permintaan HTTP.

## Cipta dan deploy model Azure OpenAI

Jika belum dilakukan, ikuti arahan di halaman [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal)
untuk mencipta sumber dan model Azure OpenAI. Pilih DALL-E 3 sebagai model.  

## Cipta aplikasi

1. Cipta fail _.env_ dengan kandungan berikut:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Cari maklumat ini di Azure OpenAI Foundry Portal untuk sumber anda di bahagian "Deployments".

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

- Seterusnya, kita muatkan pembolehubah persekitaran dari fail _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Selepas itu, kita konfigurasikan klien perkhidmatan Azure OpenAI 

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Kemudian, kita jana imej:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Kod di atas akan membalas dengan objek JSON yang mengandungi URL imej yang dijana. Kita boleh gunakan URL ini untuk memuat turun imej dan menyimpannya ke fail.

- Akhir sekali, kita buka imej dan gunakan penonton imej standard untuk memaparkannya:

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

- **prompt**, adalah prompt teks yang digunakan untuk menjana imej. Dalam kes ini, kita menggunakan prompt "Arnab di atas kuda, memegang lolipop, di padang berkabus yang ditumbuhi daffodil".
- **size**, adalah saiz imej yang dijana. Dalam kes ini, kita menjana imej bersaiz 1024x1024 piksel.
- **n**, adalah bilangan imej yang dijana. Dalam kes ini, kita menjana dua imej.
- **temperature**, adalah parameter yang mengawal tahap rawak output model AI Generatif. Nilai temperature adalah antara 0 hingga 1 di mana 0 bermaksud output adalah deterministik dan 1 bermaksud output adalah rawak. Nilai lalai ialah 0.7.

Terdapat lebih banyak perkara yang boleh anda lakukan dengan imej yang akan kita bincangkan dalam bahagian seterusnya.

## Keupayaan tambahan penjanaan imej

Anda telah lihat bagaimana kita boleh menjana imej menggunakan beberapa baris kod Python. Namun, terdapat lebih banyak perkara yang boleh anda lakukan dengan imej.

Anda juga boleh lakukan perkara berikut:

- **Membuat suntingan**. Dengan memberikan imej sedia ada, topeng dan prompt, anda boleh mengubah imej. Contohnya, anda boleh menambah sesuatu pada bahagian tertentu imej. Bayangkan imej arnab kita, anda boleh menambah topi pada arnab. Cara melakukannya adalah dengan memberikan imej, topeng (menandakan bahagian yang ingin diubah) dan prompt teks untuk menyatakan apa yang perlu dilakukan. 
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

  Imej asas hanya mengandungi ruang tamu dengan kolam tetapi imej akhir akan ada flamingo:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="./images/sunlit_lounge.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/mask.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/sunlit_lounge_result.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Cipta variasi**. Ideanya ialah anda ambil imej sedia ada dan minta variasi dicipta. Untuk mencipta variasi, anda berikan imej dan prompt teks serta kod seperti berikut:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Nota, ini hanya disokong di OpenAI

## Temperature

Temperature adalah parameter yang mengawal tahap rawak output model AI Generatif. Nilai temperature adalah antara 0 hingga 1 di mana 0 bermaksud output adalah deterministik dan 1 bermaksud output adalah rawak. Nilai lalai ialah 0.7.

Mari kita lihat contoh bagaimana temperature berfungsi, dengan menjalankan prompt ini dua kali:

> Prompt : "Arnab di atas kuda, memegang lolipop, di padang berkabus yang ditumbuhi daffodil"

![Arnab di atas kuda memegang lolipop, versi 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.ms.png)

Sekarang mari kita jalankan prompt yang sama untuk melihat bahawa kita tidak akan mendapat imej yang sama dua kali:

![Imej dijana arnab di atas kuda](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.ms.png)

Seperti yang anda lihat, imej-imej ini serupa, tetapi tidak sama. Mari kita cuba ubah nilai temperature kepada 0.1 dan lihat apa yang berlaku:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Menukar temperature

Jadi mari kita cuba jadikan respons lebih deterministik. Kita boleh perhatikan daripada dua imej yang dijana bahawa dalam imej pertama, ada arnab dan dalam imej kedua, ada kuda, jadi imej sangat berbeza.

Jadi, mari kita ubah kod kita dan tetapkan temperature kepada 0, seperti berikut:

```python
generation_response = client.images.create(
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

## Cara menetapkan sempadan untuk aplikasi anda dengan metaprompt

Dengan demo kita, kita sudah boleh menjana imej untuk pelanggan kita. Namun, kita perlu menetapkan beberapa sempadan untuk aplikasi kita.

Contohnya, kita tidak mahu menjana imej yang tidak sesuai untuk tempat kerja, atau yang tidak sesuai untuk kanak-kanak.

Kita boleh lakukan ini dengan _metaprompt_. Metaprompt ialah prompt teks yang digunakan untuk mengawal output model AI Generatif. Contohnya, kita boleh gunakan metaprompt untuk mengawal output, dan memastikan imej yang dijana adalah selamat untuk tempat kerja, atau sesuai untuk kanak-kanak.

### Bagaimana ia berfungsi?

Jadi, bagaimana metaprompt berfungsi?

Metaprompt ialah prompt teks yang digunakan untuk mengawal output model AI Generatif, ia diletakkan sebelum prompt teks, dan digunakan untuk mengawal output model serta disematkan dalam aplikasi untuk mengawal output model. Ia menggabungkan input prompt dan input metaprompt dalam satu prompt teks.

Salah satu contoh metaprompt adalah seperti berikut:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Sekarang, mari kita lihat bagaimana kita boleh gunakan metaprompt dalam demo kita.

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

## Tugasan - mari bantu pelajar

Kita telah memperkenalkan Edu4All di permulaan pelajaran ini. Sekarang tiba masanya untuk membolehkan pelajar menjana imej untuk tugasan mereka.

Pelajar akan mencipta imej untuk tugasan mereka yang mengandungi monumen, jenis monumen terpulang kepada pelajar. Pelajar diminta menggunakan kreativiti mereka dalam tugasan ini untuk meletakkan monumen tersebut dalam pelbagai konteks.

## Penyelesaian

Berikut adalah salah satu penyelesaian yang mungkin:

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

## Syabas! Teruskan Pembelajaran Anda
Selepas selesai pelajaran ini, lihat koleksi [Pembelajaran AI Generatif](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) untuk terus meningkatkan pengetahuan anda tentang AI Generatif!

Teruskan ke Pelajaran 10 di mana kita akan melihat cara [membina aplikasi AI dengan kod rendah](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.