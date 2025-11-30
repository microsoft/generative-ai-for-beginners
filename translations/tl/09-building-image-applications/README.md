<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "238cde5c90363d70ecc939569378da51",
  "translation_date": "2025-10-17T13:23:50+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "tl"
}
-->
# Paggawa ng Mga Aplikasyon para sa Paggawa ng Imahe

[![Paggawa ng Mga Aplikasyon para sa Paggawa ng Imahe](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.tl.png)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

Hindi lang text generation ang kayang gawin ng LLMs. Posible rin ang paggawa ng mga imahe mula sa mga text na deskripsyon. Ang pagkakaroon ng mga imahe bilang modality ay maaaring maging napaka-kapaki-pakinabang sa iba't ibang larangan tulad ng MedTech, arkitektura, turismo, game development, at marami pang iba. Sa kabanatang ito, tatalakayin natin ang dalawang pinakasikat na modelo ng paggawa ng imahe, ang DALL-E at Midjourney.

## Panimula

Sa araling ito, tatalakayin natin ang:

- Paggawa ng imahe at kung bakit ito mahalaga.
- DALL-E at Midjourney, ano ang mga ito, at paano ito gumagana.
- Paano gumawa ng isang application para sa paggawa ng imahe.

## Mga Layunin sa Pagkatuto

Pagkatapos ng araling ito, magagawa mo ang:

- Gumawa ng isang application para sa paggawa ng imahe.
- Tukuyin ang mga limitasyon para sa iyong application gamit ang meta prompts.
- Gumamit ng DALL-E at Midjourney.

## Bakit gumawa ng application para sa paggawa ng imahe?

Ang mga application para sa paggawa ng imahe ay isang mahusay na paraan upang tuklasin ang kakayahan ng Generative AI. Maaari itong magamit, halimbawa:

- **Pag-edit at synthesis ng imahe**. Maaari kang gumawa ng mga imahe para sa iba't ibang gamit, tulad ng pag-edit at synthesis ng imahe.

- **Maaaring gamitin sa iba't ibang industriya**. Maaari rin itong gamitin upang gumawa ng mga imahe para sa iba't ibang industriya tulad ng MedTech, Turismo, Game Development, at iba pa.

## Scenario: Edu4All

Bilang bahagi ng araling ito, ipagpapatuloy natin ang pagtatrabaho sa ating startup, ang Edu4All. Ang mga mag-aaral ay gagawa ng mga imahe para sa kanilang mga pagsusuri, kung anong mga imahe ang gagawin ay nakasalalay sa mga mag-aaral, ngunit maaari itong maging mga ilustrasyon para sa kanilang sariling kwentong pambata, lumikha ng bagong karakter para sa kanilang kwento, o tulungan silang mailarawan ang kanilang mga ideya at konsepto.

Narito ang maaaring gawin ng mga mag-aaral ng Edu4All, halimbawa, kung nagtatrabaho sila sa klase tungkol sa mga monumento:

![Startup ng Edu4All, klase tungkol sa mga monumento, Eiffel Tower](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.tl.png)

gamit ang prompt na

> "Aso sa tabi ng Eiffel Tower sa maagang liwanag ng araw"

## Ano ang DALL-E at Midjourney?

Ang [DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) at [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) ay dalawa sa pinakasikat na mga modelo ng paggawa ng imahe, na nagbibigay-daan sa iyo na gumamit ng mga prompt upang makabuo ng mga imahe.

### DALL-E

Simulan natin sa DALL-E, na isang Generative AI model na gumagawa ng mga imahe mula sa mga text na deskripsyon.

> [Ang DALL-E ay kombinasyon ng dalawang modelo, CLIP at diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, ay isang modelo na gumagawa ng embeddings, na mga numerikal na representasyon ng data, mula sa mga imahe at text.

- **Diffused attention**, ay isang modelo na gumagawa ng mga imahe mula sa embeddings. Ang DALL-E ay sinanay gamit ang dataset ng mga imahe at text at maaaring gamitin upang gumawa ng mga imahe mula sa mga text na deskripsyon. Halimbawa, maaaring gamitin ang DALL-E upang gumawa ng imahe ng pusa na may sombrero, o aso na may mohawk.

### Midjourney

Ang Midjourney ay gumagana sa parehong paraan tulad ng DALL-E, gumagawa ito ng mga imahe mula sa mga text prompt. Ang Midjourney ay maaari ring gamitin upang gumawa ng mga imahe gamit ang mga prompt tulad ng “pusa na may sombrero”, o “aso na may mohawk”.

![Larawang ginawa ng Midjourney, mekanikal na kalapati](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Credito sa Wikipedia, larawang ginawa ng Midjourney_

## Paano gumagana ang DALL-E at Midjourney

Una, ang [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). Ang DALL-E ay isang Generative AI model na nakabase sa transformer architecture na may _autoregressive transformer_.

Ang _autoregressive transformer_ ay tumutukoy kung paano gumagawa ng mga imahe mula sa mga text na deskripsyon ang isang modelo, gumagawa ito ng isang pixel sa bawat pagkakataon, at pagkatapos ay ginagamit ang mga nagawang pixel upang makabuo ng susunod na pixel. Dumadaan ito sa maraming layer sa isang neural network, hanggang sa mabuo ang imahe.

Sa prosesong ito, ang DALL-E ay may kontrol sa mga katangian, bagay, karakteristika, at iba pa sa imahe na ginagawa nito. Gayunpaman, ang DALL-E 2 at 3 ay may mas mataas na kontrol sa nagawang imahe.

## Paggawa ng iyong unang application para sa paggawa ng imahe

Ano ang kailangan upang makagawa ng isang application para sa paggawa ng imahe? Kakailanganin mo ang mga sumusunod na library:

- **python-dotenv**, inirerekomenda na gamitin ang library na ito upang itago ang iyong mga lihim sa isang _.env_ file na hiwalay sa code.
- **openai**, ang library na ito ang gagamitin mo upang makipag-ugnayan sa OpenAI API.
- **pillow**, upang magtrabaho sa mga imahe gamit ang Python.
- **requests**, upang makatulong sa paggawa ng mga HTTP request.

## Gumawa at i-deploy ang isang Azure OpenAI model

Kung hindi pa nagagawa, sundin ang mga tagubilin sa [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) page upang gumawa ng Azure OpenAI resource at model. Piliin ang DALL-E 3 bilang modelo.

## Gumawa ng app

1. Gumawa ng file na _.env_ na may ganitong nilalaman:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Hanapin ang impormasyong ito sa Azure OpenAI Foundry Portal para sa iyong resource sa seksyong "Deployments".

1. Kolektahin ang mga library sa isang file na tinatawag na _requirements.txt_ tulad nito:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Susunod, gumawa ng virtual environment at i-install ang mga library:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Para sa Windows, gamitin ang mga sumusunod na command upang gumawa at i-activate ang iyong virtual environment:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Idagdag ang sumusunod na code sa isang file na tinatawag na _app.py_:

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

Ipaliwanag natin ang code na ito:

- Una, ini-import natin ang mga library na kailangan natin, kabilang ang OpenAI library, dotenv library, requests library, at Pillow library.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Susunod, ina-load natin ang mga environment variable mula sa _.env_ file.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Pagkatapos nito, kino-configure natin ang Azure OpenAI service client.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Susunod, ginagawa natin ang imahe:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Ang code sa itaas ay nagbabalik ng isang JSON object na naglalaman ng URL ng nagawang imahe. Maaari nating gamitin ang URL upang i-download ang imahe at i-save ito sa isang file.

- Sa huli, binubuksan natin ang imahe at ginagamit ang standard image viewer upang ipakita ito:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Higit pang detalye sa paggawa ng imahe

Tingnan natin ang code na gumagawa ng imahe nang mas detalyado:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, ay ang text prompt na ginagamit upang gumawa ng imahe. Sa kasong ito, ginagamit natin ang prompt na "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils".
- **size**, ay ang laki ng imahe na ginagawa. Sa kasong ito, gumagawa tayo ng imahe na 1024x1024 pixels.
- **n**, ay ang bilang ng mga imaheng ginagawa. Sa kasong ito, gumagawa tayo ng dalawang imahe.
- **temperature**, ay isang parameter na kumokontrol sa randomness ng output ng isang Generative AI model. Ang temperature ay isang halaga sa pagitan ng 0 at 1 kung saan ang 0 ay nangangahulugang deterministic ang output at ang 1 ay nangangahulugang random ang output. Ang default na halaga ay 0.7.

May iba pang mga bagay na maaari mong gawin sa mga imahe na tatalakayin natin sa susunod na seksyon.

## Karagdagang kakayahan ng paggawa ng imahe

Nakita mo na kung paano tayo nakagawa ng imahe gamit ang ilang linya ng Python. Gayunpaman, may iba pang mga bagay na maaari mong gawin sa mga imahe.

Maaari mo ring gawin ang mga sumusunod:

- **Mag-edit ng mga imahe**. Sa pamamagitan ng pagbibigay ng isang umiiral na imahe, mask, at prompt, maaari mong baguhin ang isang imahe. Halimbawa, maaari kang magdagdag ng isang bagay sa isang bahagi ng imahe. Isipin ang ating imahe ng kuneho, maaari kang magdagdag ng sombrero sa kuneho. Paano mo ito gagawin ay sa pamamagitan ng pagbibigay ng imahe, mask (na tumutukoy sa bahagi ng lugar para sa pagbabago) at isang text prompt upang sabihin kung ano ang dapat gawin.
> Tandaan: hindi ito suportado sa DALL-E 3.

Narito ang isang halimbawa gamit ang GPT Image:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  Ang base image ay naglalaman lamang ng lounge na may pool ngunit ang final image ay may flamingo:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.tl.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.tl.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.tl.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **Gumawa ng mga variation**. Ang ideya ay kumuha ng umiiral na imahe at hilingin na gumawa ng mga variation. Upang gumawa ng variation, magbigay ng imahe at isang text prompt at code tulad nito:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Tandaan, ito ay suportado lamang sa OpenAI.

## Temperature

Ang temperature ay isang parameter na kumokontrol sa randomness ng output ng isang Generative AI model. Ang temperature ay isang halaga sa pagitan ng 0 at 1 kung saan ang 0 ay nangangahulugang deterministic ang output at ang 1 ay nangangahulugang random ang output. Ang default na halaga ay 0.7.

Tingnan natin ang isang halimbawa kung paano gumagana ang temperature, sa pamamagitan ng pagtakbo ng prompt na ito nang dalawang beses:

> Prompt: "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![Bunny sa kabayo na may hawak na lollipop, bersyon 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.tl.png)

Ngayon, ulitin natin ang parehong prompt upang makita na hindi natin makukuha ang parehong imahe nang dalawang beses:

![Ginawang imahe ng kuneho sa kabayo](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.tl.png)

Tulad ng nakikita mo, magkatulad ang mga imahe, ngunit hindi pareho. Subukan nating baguhin ang halaga ng temperature sa 0.1 at tingnan ang mangyayari:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Pagbabago ng temperature

Subukan nating gawing mas deterministic ang tugon. Napansin natin mula sa dalawang imaheng ginawa na sa unang imahe, may kuneho at sa pangalawang imahe, may kabayo, kaya't malaki ang pagkakaiba ng mga imahe.

Kaya't baguhin natin ang ating code at itakda ang temperature sa 0, tulad nito:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Ngayon kapag pinatakbo mo ang code na ito, makakakuha ka ng dalawang imaheng ito:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.tl.png)
- ![Temperature 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.tl.png)

Dito malinaw mong makikita kung paano mas magkahawig ang mga imahe.

## Paano tukuyin ang mga limitasyon para sa iyong application gamit ang metaprompts

Sa ating demo, maaari na tayong gumawa ng mga imahe para sa ating mga kliyente. Gayunpaman, kailangan nating magtakda ng ilang mga limitasyon para sa ating application.

Halimbawa, ayaw nating gumawa ng mga imahe na hindi ligtas para sa trabaho, o hindi angkop para sa mga bata.

Magagawa natin ito gamit ang _metaprompts_. Ang metaprompts ay mga text prompt na ginagamit upang kontrolin ang output ng isang Generative AI model. Halimbawa, maaari nating gamitin ang metaprompts upang kontrolin ang output, at tiyakin na ang mga nagawang imahe ay ligtas para sa trabaho, o angkop para sa mga bata.

### Paano ito gumagana?

Ngayon, paano gumagana ang meta prompts?

Ang meta prompts ay mga text prompt na ginagamit upang kontrolin ang output ng isang Generative AI model, inilalagay ang mga ito bago ang text prompt, at ginagamit upang kontrolin ang output ng modelo at naka-embed sa mga application upang kontrolin ang output ng modelo. Pinagsasama ang input ng prompt at ang input ng meta prompt sa isang text prompt.

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

Mula sa prompt sa itaas, makikita mo kung paano isinasaalang-alang ng lahat ng mga imaheng nilikha ang metaprompt.

## Gawain - tulungan ang mga mag-aaral

Ipinakilala natin ang Edu4All sa simula ng araling ito. Ngayon ay oras na upang tulungan ang mga mag-aaral na gumawa ng mga imahe para sa kanilang mga pagsusuri.

Ang mga mag-aaral ay gagawa ng mga imahe para sa kanilang mga pagsusuri na naglalaman ng mga monumento, kung anong mga monumento ang gagawin ay nakasalalay sa mga mag-aaral. Ang mga mag-aaral ay hinihikayat na gamitin ang kanilang pagkamalikhain sa gawaing ito upang ilagay ang mga monumento sa iba't ibang konteksto.

## Solusyon

Narito ang isang posibleng solusyon:
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

## Magaling na Trabaho! Ipagpatuloy ang Iyong Pag-aaral

Pagkatapos makumpleto ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang patuloy na paunlarin ang iyong kaalaman sa Generative AI!

Pumunta sa Lesson 10 kung saan tatalakayin natin kung paano [bumuo ng AI applications gamit ang low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na mapagkakatiwalaang pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.