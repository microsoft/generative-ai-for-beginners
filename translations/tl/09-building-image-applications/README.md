<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:19:32+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "tl"
}
-->
# Pagbuo ng mga Aplikasyon para sa Pagbuo ng Imahe

May higit pa sa LLMs kaysa sa pagbuo ng teksto. Posible ring bumuo ng mga imahe mula sa mga paglalarawan ng teksto. Ang pagkakaroon ng mga imahe bilang isang modality ay maaaring maging lubos na kapaki-pakinabang sa iba't ibang larangan mula sa MedTech, arkitektura, turismo, pag-unlad ng laro at iba pa. Sa kabanatang ito, titingnan natin ang dalawang pinakasikat na modelo ng pagbuo ng imahe, DALL-E at Midjourney.

## Panimula

Sa araling ito, saklaw natin:

- Pagbuo ng imahe at kung bakit ito kapaki-pakinabang.
- DALL-E at Midjourney, ano sila, at paano sila gumagana.
- Paano ka makakagawa ng isang app para sa pagbuo ng imahe.

## Mga Layunin sa Pag-aaral

Pagkatapos makumpleto ang araling ito, magagawa mong:

- Bumuo ng isang aplikasyon para sa pagbuo ng imahe.
- Tukuyin ang mga hangganan para sa iyong aplikasyon gamit ang meta prompts.
- Makipagtulungan sa DALL-E at Midjourney.

## Bakit bumuo ng isang aplikasyon para sa pagbuo ng imahe?

Ang mga aplikasyon para sa pagbuo ng imahe ay isang mahusay na paraan upang tuklasin ang kakayahan ng Generative AI. Maaari silang magamit para sa, halimbawa:

- **Pag-edit at pag-synthesize ng imahe**. Maaari kang bumuo ng mga imahe para sa iba't ibang mga kaso ng paggamit, tulad ng pag-edit ng imahe at pag-synthesize ng imahe.

- **Inilapat sa iba't ibang industriya**. Maaari rin silang magamit upang bumuo ng mga imahe para sa iba't ibang industriya tulad ng Medtech, Turismo, Pag-unlad ng Laro at iba pa.

## Scenario: Edu4All

Bilang bahagi ng araling ito, magpapatuloy tayo sa pakikipagtulungan sa aming startup, Edu4All, sa araling ito. Ang mga mag-aaral ay lilikha ng mga imahe para sa kanilang mga pagsusuri, kung ano ang mga imahe ay nasa mga mag-aaral, ngunit maaari silang maging mga ilustrasyon para sa kanilang sariling kwento o lumikha ng bagong karakter para sa kanilang kwento o tulungan silang mailarawan ang kanilang mga ideya at konsepto.

Narito kung ano ang maaaring mabuo ng mga mag-aaral ng Edu4All halimbawa kung sila ay nagtatrabaho sa klase sa mga monumento:

![Edu4All startup, klase sa mga monumento, Eiffel Tower](../../../translated_images/startup.ec211d74fef9f4175010c3334942b715514230415744b9dd0a69a19f4ad68786.tl.png)

gamit ang prompt tulad ng

> "Aso sa tabi ng Eiffel Tower sa maagang sikat ng araw"

## Ano ang DALL-E at Midjourney?

Ang [DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) at [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) ay dalawa sa mga pinakasikat na modelo ng pagbuo ng imahe, pinapayagan ka nilang gumamit ng mga prompt upang bumuo ng mga imahe.

### DALL-E

Magsimula tayo sa DALL-E, na isang Generative AI model na bumubuo ng mga imahe mula sa mga paglalarawan ng teksto.

> [Ang DALL-E ay isang kombinasyon ng dalawang modelo, CLIP at diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, ay isang modelo na bumubuo ng embeddings, na mga numerikal na representasyon ng data, mula sa mga imahe at teksto.

- **Diffused attention**, ay isang modelo na bumubuo ng mga imahe mula sa embeddings. Ang DALL-E ay sinanay sa isang dataset ng mga imahe at teksto at maaaring magamit upang bumuo ng mga imahe mula sa mga paglalarawan ng teksto. Halimbawa, ang DALL-E ay maaaring magamit upang bumuo ng mga imahe ng isang pusa na may sombrero, o isang aso na may mohawk.

### Midjourney

Ang Midjourney ay gumagana sa isang katulad na paraan sa DALL-E, ito ay bumubuo ng mga imahe mula sa mga text prompt. Ang Midjourney, ay maaari ring magamit upang bumuo ng mga imahe gamit ang mga prompt tulad ng “isang pusa na may sombrero”, o isang “aso na may mohawk”.

![Imahe na nabuo ng Midjourney, mekanikal na kalapati](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Kredito sa Imahe Wikipedia, imahe na nabuo ng Midjourney_

## Paano Gumagana ang DALL-E at Midjourney

Una, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). Ang DALL-E ay isang Generative AI model batay sa transformer architecture na may _autoregressive transformer_.

Ang _autoregressive transformer_ ay nagtatakda kung paano bumubuo ang isang modelo ng mga imahe mula sa mga paglalarawan ng teksto, ito ay bumubuo ng isang pixel sa isang pagkakataon, at pagkatapos ay ginagamit ang mga nabuo na pixel upang bumuo ng susunod na pixel. Dumadaan sa maraming layer sa isang neural network, hanggang sa makumpleto ang imahe.

Sa prosesong ito, ang DALL-E, ay kumokontrol sa mga katangian, mga bagay, mga katangian, at higit pa sa imahe na ito ay bumubuo. Gayunpaman, ang DALL-E 2 at 3 ay may higit na kontrol sa nabuo na imahe.

## Pagbuo ng iyong unang aplikasyon para sa pagbuo ng imahe

Ano ang kinakailangan upang bumuo ng isang aplikasyon para sa pagbuo ng imahe? Kailangan mo ang mga sumusunod na library:

- **python-dotenv**, lubos na inirerekomenda na gamitin ang library na ito upang itago ang iyong mga lihim sa isang _.env_ na file na malayo sa code.
- **openai**, ang library na ito ay kung ano ang gagamitin mo upang makipag-ugnayan sa OpenAI API.
- **pillow**, upang magtrabaho sa mga imahe sa Python.
- **requests**, upang tulungan kang gumawa ng mga HTTP request.

1. Lumikha ng isang file _.env_ na may sumusunod na nilalaman:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Hanapin ang impormasyong ito sa Azure Portal para sa iyong resource sa seksyon na "Keys and Endpoint".

1. Kolektahin ang mga library sa itaas sa isang file na tinatawag na _requirements.txt_ tulad nito:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Susunod, lumikha ng virtual environment at i-install ang mga library:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Para sa Windows, gamitin ang mga sumusunod na command upang lumikha at i-activate ang iyong virtual environment:

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

Ipaliwanag natin ang code na ito:

- Una, ina-import natin ang mga library na kailangan natin, kabilang ang OpenAI library, ang dotenv library, ang requests library, at ang Pillow library.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Susunod, in-load natin ang mga environment variables mula sa _.env_ na file.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Pagkatapos nito, itinakda natin ang endpoint, key para sa OpenAI API, version at type.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Susunod, bumubuo tayo ng imahe:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Ang code sa itaas ay tumutugon sa isang JSON object na naglalaman ng URL ng nabuo na imahe. Maaari nating gamitin ang URL upang i-download ang imahe at i-save ito sa isang file.

- Sa huli, binubuksan natin ang imahe at ginagamit ang standard image viewer upang ipakita ito:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Higit pang mga detalye sa pagbuo ng imahe

Tingnan natin ang code na bumubuo ng imahe sa mas detalyadong paraan:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, ay ang text prompt na ginagamit upang bumuo ng imahe. Sa kasong ito, ginagamit natin ang prompt na "Bunny sa kabayo, may hawak na lollipop, sa foggy meadow kung saan tumutubo ang daffodils".
- **size**, ay ang laki ng imahe na nabuo. Sa kasong ito, bumubuo tayo ng imahe na 1024x1024 pixels.
- **n**, ay ang bilang ng mga imahe na nabuo. Sa kasong ito, bumubuo tayo ng dalawang imahe.
- **temperature**, ay isang parameter na kumokontrol sa randomness ng output ng isang Generative AI model. Ang temperatura ay isang halaga sa pagitan ng 0 at 1 kung saan ang 0 ay nangangahulugang ang output ay deterministic at 1 ay nangangahulugang ang output ay random. Ang default na halaga ay 0.7.

Mayroon pang mga bagay na maaari mong gawin sa mga imahe na saklaw natin sa susunod na seksyon.

## Karagdagang kakayahan ng pagbuo ng imahe

Nakita mo na sa ngayon kung paano tayo nakabuo ng isang imahe gamit ang ilang linya sa Python. Gayunpaman, may higit pang mga bagay na maaari mong gawin sa mga imahe.

Maaari mo ring gawin ang mga sumusunod:

- **Gumawa ng mga edit**. Sa pamamagitan ng pagbibigay ng isang umiiral na imahe ng mask at isang prompt, maaari mong baguhin ang isang imahe. Halimbawa, maaari kang magdagdag ng isang bagay sa isang bahagi ng imahe. Isipin ang ating imahe ng kuneho, maaari kang magdagdag ng sombrero sa kuneho. Paano mo gagawin iyon ay sa pamamagitan ng pagbibigay ng imahe, isang mask (pagkilala sa bahagi ng lugar para sa pagbabago) at isang text prompt upang sabihin kung ano ang dapat gawin.

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

  Ang base image ay maglalaman lamang ng kuneho ngunit ang panghuling imahe ay magkakaroon ng sombrero sa kuneho.

- **Lumikha ng mga variation**. Ang ideya ay kumuha ka ng isang umiiral na imahe at humiling na lumikha ng mga variation. Upang lumikha ng isang variation, nagbibigay ka ng imahe at isang text prompt at code tulad nito:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Tandaan, ito ay sinusuportahan lamang sa OpenAI

## Temperatura

Ang temperatura ay isang parameter na kumokontrol sa randomness ng output ng isang Generative AI model. Ang temperatura ay isang halaga sa pagitan ng 0 at 1 kung saan ang 0 ay nangangahulugang ang output ay deterministic at 1 ay nangangahulugang ang output ay random. Ang default na halaga ay 0.7.

Tingnan natin ang isang halimbawa kung paano gumagana ang temperatura, sa pamamagitan ng pagtakbo ng prompt na ito ng dalawang beses:

> Prompt: "Bunny sa kabayo, may hawak na lollipop, sa foggy meadow kung saan tumutubo ang daffodils"

![Bunny sa kabayo na may hawak na lollipop, bersyon 1](../../../translated_images/v1-generated-image.208ba0525ed6ae505504aa852e28d334c0440e9931b7c97f9508176a22d2dd54.tl.png)

Ngayon ay patakbuhin natin ang parehong prompt upang makita na hindi natin makukuha ang parehong imahe ng dalawang beses:

![Nabuo na imahe ng bunny sa kabayo](../../../translated_images/v2-generated-image.f0a88c05ef476e95f3682d4b21c9ba2f4807ae71cc29e9c05b42ebbf497cf61b.tl.png)

Tulad ng nakikita mo, ang mga imahe ay magkatulad, ngunit hindi pareho. Subukan natin baguhin ang halaga ng temperatura sa 0.1 at tingnan kung ano ang mangyayari:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Pagbabago ng temperatura

Kaya subukan nating gawing mas deterministic ang tugon. Mapapansin natin mula sa dalawang imahe na nabuo na sa unang imahe, mayroong isang bunny at sa pangalawang imahe, mayroong isang kabayo, kaya't ang mga imahe ay lubos na nag-iiba.

Kaya't baguhin natin ang ating code at itakda ang temperatura sa 0, tulad nito:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Ngayon kapag patakbuhin mo ang code na ito, makakakuha ka ng mga sumusunod na dalawang imahe:

- ![Temperatura 0, v1](../../../translated_images/v1-temp-generated-image.d8557be792b5c81c2c6d2804cb7b210fe8b340106fe4ffcadf9cf7de1cd7b991.tl.png)
- ![Temperatura 0 , v2](../../../translated_images/v2-temp-generated-image.bd412fcfbd43379312b1382212a332aa311ca1a80ea692dea50a8b876a487c61.tl.png)

Dito makikita mo nang malinaw kung paano mas magkatulad ang mga imahe.

## Paano tukuyin ang mga hangganan para sa iyong aplikasyon gamit ang metaprompts

Sa aming demo, maaari na kaming bumuo ng mga imahe para sa aming mga kliyente. Gayunpaman, kailangan nating lumikha ng ilang mga hangganan para sa aming aplikasyon.

Halimbawa, ayaw naming bumuo ng mga imahe na hindi ligtas para sa trabaho, o na hindi angkop para sa mga bata.

Magagawa natin ito gamit ang _metaprompts_. Ang metaprompts ay mga text prompt na ginagamit upang kontrolin ang output ng isang Generative AI model. Halimbawa, maaari nating gamitin ang metaprompts upang kontrolin ang output, at tiyakin na ang mga nabuo na imahe ay ligtas para sa trabaho, o angkop para sa mga bata.

### Paano ito gumagana?

Ngayon, paano gumagana ang mga meta prompt?

Ang mga meta prompt ay mga text prompt na ginagamit upang kontrolin ang output ng isang Generative AI model, sila ay inilalagay bago ang text prompt, at ginagamit upang kontrolin ang output ng modelo at naka-embed sa mga aplikasyon upang kontrolin ang output ng modelo. Ini-encapsulate ang input ng prompt at ang input ng meta prompt sa isang solong text prompt.

Ang isang halimbawa ng meta prompt ay ang sumusunod:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Ngayon, tingnan natin kung paano natin magagamit ang mga meta prompt sa ating demo.

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

Mula sa prompt sa itaas, makikita mo kung paano ang lahat ng mga imahe na nilikha ay isinasaalang-alang ang metaprompt.

## Takdang-aralin - hayaan nating paganahin ang mga mag-aaral

Ipinakilala namin ang Edu4All sa simula ng araling ito. Ngayon ay oras na upang paganahin ang mga mag-aaral na bumuo ng mga imahe para sa kanilang mga pagsusuri.

Ang mga mag-aaral ay lilikha ng mga imahe para sa kanilang mga pagsusuri na naglalaman ng mga monumento, kung ano ang mga monumento ay nasa mga mag-aaral. Ang mga mag-aaral ay hinihiling na gamitin ang kanilang pagkamalikhain sa gawaing ito upang ilagay ang mga monumento sa iba't ibang konteksto.

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

## Magaling na Trabaho! Ipagpatuloy ang Iyong Pag-aaral

Pagkatapos makumpleto ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pagpapahusay ng iyong kaalaman sa Generative AI!

Pumunta sa Lesson 10 kung saan titingnan natin kung paano [bumuo ng mga AI application na may low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat pinagsisikapan naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatumpak. Ang orihinal na dokumento sa sarili nitong wika ay dapat ituring na mapagkakatiwalaang sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaintindihan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.