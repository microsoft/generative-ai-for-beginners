<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a7fd0f95f9eb673b79da47c0814f4d4",
  "translation_date": "2025-07-09T13:30:48+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "tl"
}
-->
# Paggawa ng Mga Aplikasyon para sa Pagbuo ng Imahe

[![Paggawa ng Mga Aplikasyon para sa Pagbuo ng Imahe](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.tl.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Hindi lang teksto ang kaya ng LLMs. Maaari rin silang gumawa ng mga imahe mula sa mga paglalarawan sa teksto. Ang pagkakaroon ng mga imahe bilang modality ay napaka-kapaki-pakinabang sa iba't ibang larangan tulad ng MedTech, arkitektura, turismo, pagbuo ng laro, at iba pa. Sa kabanatang ito, titingnan natin ang dalawang pinakasikat na modelo para sa pagbuo ng imahe, ang DALL-E at Midjourney.

## Panimula

Sa araling ito, tatalakayin natin ang:

- Pagbuo ng imahe at kung bakit ito kapaki-pakinabang.
- Ano ang DALL-E at Midjourney, at paano sila gumagana.
- Paano ka makakagawa ng isang app para sa pagbuo ng imahe.

## Mga Layunin sa Pagkatuto

Pagkatapos matapos ang araling ito, magagawa mong:

- Gumawa ng isang aplikasyon para sa pagbuo ng imahe.
- Magtakda ng mga hangganan para sa iyong aplikasyon gamit ang meta prompts.
- Gumamit ng DALL-E at Midjourney.

## Bakit gumawa ng aplikasyon para sa pagbuo ng imahe?

Ang mga aplikasyon para sa pagbuo ng imahe ay mahusay na paraan para tuklasin ang kakayahan ng Generative AI. Maaari itong gamitin, halimbawa, para sa:

- **Pag-edit at synthesis ng imahe**. Maaari kang gumawa ng mga imahe para sa iba't ibang gamit, tulad ng pag-edit at synthesis ng imahe.

- **Paglalapat sa iba't ibang industriya**. Maaari rin itong gamitin upang gumawa ng mga imahe para sa iba't ibang industriya tulad ng Medtech, Turismo, Pagbuo ng laro, at iba pa.

## Senaryo: Edu4All

Bilang bahagi ng araling ito, magpapatuloy tayo sa pagtatrabaho kasama ang aming startup na Edu4All. Ang mga estudyante ay gagawa ng mga imahe para sa kanilang mga pagsusulit; kung anong mga imahe ang gagawin ay nasa kanila, maaaring mga ilustrasyon para sa kanilang sariling kwento, gumawa ng bagong karakter para sa kanilang kwento, o tulungan silang mailarawan ang kanilang mga ideya at konsepto.

Narito ang maaaring gawin ng mga estudyante ng Edu4All kung sila ay gumagawa sa klase tungkol sa mga monumento:

![Edu4All startup, klase tungkol sa mga monumento, Eiffel Tower](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.tl.png)

gamit ang prompt na

> "Aso sa tabi ng Eiffel Tower sa maagang sikat ng araw"

## Ano ang DALL-E at Midjourney?

Ang [DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) at [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) ay dalawa sa mga pinakasikat na modelo para sa pagbuo ng imahe, pinapayagan kang gumamit ng mga prompt para gumawa ng mga imahe.

### DALL-E

Magsimula tayo sa DALL-E, isang Generative AI model na gumagawa ng mga imahe mula sa mga paglalarawan sa teksto.

> [Ang DALL-E ay kombinasyon ng dalawang modelo, CLIP at diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, ay isang modelo na gumagawa ng embeddings, mga numerikal na representasyon ng data, mula sa mga imahe at teksto.

- **Diffused attention**, ay isang modelo na gumagawa ng mga imahe mula sa embeddings. Ang DALL-E ay sinanay gamit ang dataset ng mga imahe at teksto at maaaring gamitin upang gumawa ng mga imahe mula sa mga paglalarawan sa teksto. Halimbawa, maaaring gamitin ang DALL-E upang gumawa ng mga imahe ng pusa na may sumbrero, o aso na may mohawk.

### Midjourney

Ang Midjourney ay gumagana nang katulad ng DALL-E, gumagawa ito ng mga imahe mula sa mga text prompt. Maaari rin itong gamitin upang gumawa ng mga imahe gamit ang mga prompt tulad ng “pusa na may sumbrero”, o “aso na may mohawk”.

![Larawan na ginawa ng Midjourney, mechanical pigeon](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Larawan mula sa Wikipedia, gawa ng Midjourney_

## Paano gumagana ang DALL-E at Midjourney

Una, ang [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). Ang DALL-E ay isang Generative AI model na nakabase sa transformer architecture na may _autoregressive transformer_.

Ang _autoregressive transformer_ ay naglalarawan kung paano gumagawa ang modelo ng mga imahe mula sa mga paglalarawan sa teksto, isa-isang pixel ang ginagawa, at ginagamit ang mga nagawang pixel para gumawa ng susunod na pixel. Dumadaan ito sa maraming layers sa neural network hanggang sa makumpleto ang imahe.

Sa prosesong ito, kinokontrol ng DALL-E ang mga katangian, bagay, at iba pa sa imahe na ginagawa nito. Gayunpaman, ang DALL-E 2 at 3 ay may mas malawak na kontrol sa nagawang imahe.

## Paggawa ng iyong unang aplikasyon para sa pagbuo ng imahe

Ano ang kailangan para makagawa ng aplikasyon para sa pagbuo ng imahe? Kailangan mo ang mga sumusunod na library:

- **python-dotenv**, lubos na inirerekomenda na gamitin ito para itago ang iyong mga sikreto sa isang _.env_ file na hiwalay sa code.
- **openai**, ito ang library na gagamitin mo para makipag-ugnayan sa OpenAI API.
- **pillow**, para sa pagproseso ng mga imahe sa Python.
- **requests**, para makatulong sa paggawa ng HTTP requests.

1. Gumawa ng file na _.env_ na may sumusunod na nilalaman:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Hanapin ang impormasyong ito sa Azure Portal para sa iyong resource sa seksyong "Keys and Endpoint".

1. Ilagay ang mga library na ito sa isang file na tinatawag na _requirements.txt_ tulad nito:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Sunod, gumawa ng virtual environment at i-install ang mga library:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Para sa Windows, gamitin ang mga sumusunod na utos para gumawa at i-activate ang virtual environment:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Idagdag ang sumusunod na code sa file na tinatawag na _app.py_:

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

Ipapaliwanag natin ang code na ito:

- Una, ini-import natin ang mga library na kailangan, kabilang ang OpenAI library, dotenv library, requests library, at Pillow library.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Sunod, niloload natin ang mga environment variable mula sa _.env_ file.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Pagkatapos, itinatakda natin ang endpoint, key para sa OpenAI API, bersyon, at uri.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Sunod, ginagawa natin ang imahe:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Ang code sa itaas ay nagbabalik ng JSON object na naglalaman ng URL ng nagawang imahe. Maaari nating gamitin ang URL para i-download ang imahe at i-save ito sa isang file.

- Sa huli, binubuksan natin ang imahe at ginagamit ang karaniwang image viewer para ipakita ito:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Mas detalyadong paliwanag sa paggawa ng imahe

Tingnan natin nang mas malalim ang code na gumagawa ng imahe:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, ang text prompt na ginagamit para gumawa ng imahe. Sa kasong ito, ginagamit natin ang prompt na "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils".
- **size**, ang sukat ng imahe na gagawin. Sa kasong ito, gumagawa tayo ng imahe na 1024x1024 pixels.
- **n**, ang bilang ng mga imahe na gagawin. Sa kasong ito, gumagawa tayo ng dalawang imahe.
- **temperature**, isang parameter na kumokontrol sa randomness ng output ng Generative AI model. Ang temperature ay may halagang mula 0 hanggang 1 kung saan ang 0 ay nangangahulugang deterministic ang output at ang 1 ay nangangahulugang random ang output. Ang default na halaga ay 0.7.

Marami pang ibang bagay na maaari mong gawin sa mga imahe na tatalakayin natin sa susunod na bahagi.

## Karagdagang kakayahan sa pagbuo ng imahe

Nakita mo na kung paano tayo makakagawa ng imahe gamit ang ilang linya ng Python. Ngunit marami pang ibang bagay na maaari mong gawin sa mga imahe.

Maaari mo ring gawin ang mga sumusunod:

- **Gumawa ng mga edit**. Sa pamamagitan ng pagbibigay ng umiiral na imahe, mask, at prompt, maaari mong baguhin ang imahe. Halimbawa, maaari kang magdagdag ng isang bagay sa isang bahagi ng imahe. Isipin ang ating imahe ng kuneho, maaari kang magdagdag ng sumbrero sa kuneho. Gagawin mo ito sa pamamagitan ng pagbibigay ng imahe, mask (na tumutukoy sa bahagi na babaguhin), at text prompt na nagsasabi kung ano ang gagawin.

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

  Ang base na imahe ay naglalaman lamang ng kuneho ngunit ang huling imahe ay may sumbrero na sa kuneho.

- **Gumawa ng mga variation**. Ang ideya ay kumuha ng umiiral na imahe at hilingin na gumawa ng mga variation nito. Para gumawa ng variation, magbibigay ka ng imahe at text prompt at code tulad nito:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Tandaan, suportado lamang ito sa OpenAI

## Temperature

Ang temperature ay isang parameter na kumokontrol sa randomness ng output ng Generative AI model. Ang temperature ay may halagang mula 0 hanggang 1 kung saan ang 0 ay nangangahulugang deterministic ang output at ang 1 ay nangangahulugang random ang output. Ang default na halaga ay 0.7.

Tingnan natin ang halimbawa kung paano gumagana ang temperature, sa pamamagitan ng pagpapatakbo ng prompt na ito ng dalawang beses:

> Prompt : "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![Bunny on a horse holding a lollipop, version 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.tl.png)

Ngayon patakbuhin natin ang parehong prompt para makita na hindi pareho ang lalabas na imahe:

![Generated image of bunny on horse](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.tl.png)

Makikita mo, magkatulad ang mga imahe pero hindi pareho. Subukan nating baguhin ang halaga ng temperature sa 0.1 at tingnan ang resulta:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Pagbabago ng temperature

Subukan nating gawing mas deterministic ang sagot. Napansin natin sa dalawang nagawang imahe na sa unang imahe ay kuneho ang lumabas at sa pangalawa ay kabayo, kaya malaki ang pagkakaiba ng mga imahe.

Kaya babaguhin natin ang code at itatakda ang temperature sa 0, ganito:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Ngayon kapag pinatakbo mo ang code, makakakuha ka ng dalawang imahe na ito:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.tl.png)
- ![Temperature 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.tl.png)

Dito makikita mo nang malinaw kung paano mas nagkakatulad ang mga imahe.

## Paano magtakda ng mga hangganan para sa iyong aplikasyon gamit ang metaprompts

Sa demo natin, kaya na nating gumawa ng mga imahe para sa ating mga kliyente. Ngunit kailangan nating magtakda ng ilang hangganan para sa ating aplikasyon.

Halimbawa, ayaw nating gumawa ng mga imahe na hindi angkop sa trabaho, o hindi angkop para sa mga bata.

Magagawa natin ito gamit ang _metaprompts_. Ang metaprompts ay mga text prompt na ginagamit para kontrolin ang output ng isang Generative AI model. Halimbawa, maaari nating gamitin ang metaprompts para siguraduhing ang mga nagawang imahe ay ligtas sa trabaho, o angkop para sa mga bata.

### Paano ito gumagana?

Paano nga ba gumagana ang metaprompts?

Ang metaprompts ay mga text prompt na ginagamit para kontrolin ang output ng isang Generative AI model, inilalagay ito bago ang pangunahing text prompt, at ginagamit para kontrolin ang output ng modelo at isinasama sa mga aplikasyon para kontrolin ang output ng modelo. Pinagsasama ang prompt input at meta prompt input sa isang text prompt.

Isang halimbawa ng meta prompt ay ang sumusunod:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Ngayon, tingnan natin kung paano natin magagamit ang meta prompts sa ating demo.

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

Mula sa prompt sa itaas, makikita mo kung paano isinasaalang-alang ng lahat ng mga nagawang imahe ang metaprompt.

## Takdang-Aralin - bigyang kakayahan ang mga estudyante

Ipinakilala natin ang Edu4All sa simula ng araling ito. Ngayon ay panahon na para bigyang kakayahan ang mga estudyante na gumawa ng mga imahe para sa kanilang mga pagsusulit.

Gagawa ang mga estudyante ng mga imahe para sa kanilang mga pagsusulit na naglalaman ng mga monumento, kung anong mga monumento ay nasa kanila. Hinihikayat ang mga estudyante na gamitin ang kanilang pagkamalikhain sa gawaing ito upang ilagay ang mga monumento sa iba't ibang konteksto.

## Solusyon

Narito ang isang posibleng solusyon:

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

## Magaling! Ipagpatuloy ang Iyong Pag-aaral

Pagkatapos matapos ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para ipagpatuloy ang paghasa ng iyong kaalaman sa Generative AI!

Pumunta sa Lesson 10 kung saan titingnan natin kung paano [gumawa ng AI applications gamit ang low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.