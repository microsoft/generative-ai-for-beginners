<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef74ad58fc01f7ad80788f79505f9816",
  "translation_date": "2025-08-26T18:36:51+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "tl"
}
-->
# Pagbuo ng Mga Application para sa Paglikha ng Larawan

[![Pagbuo ng Mga Application para sa Paglikha ng Larawan](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.tl.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Hindi lang text generation ang kaya ng LLMs. Posible ring lumikha ng mga larawan mula sa mga deskripsyon sa teksto. Ang pagkakaroon ng mga larawan bilang modality ay napaka-kapaki-pakinabang sa maraming larangan tulad ng MedTech, arkitektura, turismo, game development at iba pa. Sa kabanatang ito, tatalakayin natin ang dalawang pinakasikat na modelo para sa paglikha ng larawan, ang DALL-E at Midjourney.

## Panimula

Sa araling ito, tatalakayin natin ang:

- Paglikha ng larawan at kung bakit ito mahalaga.
- DALL-E at Midjourney, ano ang mga ito, at paano sila gumagana.
- Paano ka makakagawa ng isang image generation app.

## Mga Layunin sa Pagkatuto

Pagkatapos ng araling ito, magagawa mong:

- Gumawa ng application para sa paglikha ng larawan.
- Magtakda ng mga limitasyon para sa iyong application gamit ang meta prompts.
- Gumamit ng DALL-E at Midjourney.

## Bakit gagawa ng application para sa paglikha ng larawan?

Ang mga application para sa paglikha ng larawan ay mahusay na paraan para tuklasin ang kakayahan ng Generative AI. Maaari itong gamitin para sa, halimbawa:

- **Pag-edit at synthesis ng larawan**. Maaari kang lumikha ng mga larawan para sa iba't ibang gamit, tulad ng pag-edit at synthesis ng larawan.

- **Maaaring gamitin sa iba't ibang industriya**. Maaari rin itong gamitin para lumikha ng mga larawan para sa iba't ibang industriya tulad ng Medtech, Turismo, Game development at iba pa.

## Scenario: Edu4All

Bilang bahagi ng araling ito, ipagpapatuloy natin ang pagtatrabaho sa ating startup na Edu4All. Ang mga estudyante ay gagawa ng mga larawan para sa kanilang mga assessment, kung anong larawan ang gagawin ay depende sa estudyante, maaaring ito ay mga ilustrasyon para sa kanilang sariling kwento, lumikha ng bagong karakter para sa kanilang kwento, o tulungan silang mailarawan ang kanilang mga ideya at konsepto.

Halimbawa, ito ang maaaring malikha ng mga estudyante ng Edu4All kung nagtatrabaho sila sa klase tungkol sa mga monumento:

![Edu4All startup, class on monuments, Eiffel Tower](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.tl.png)

gamit ang prompt na tulad ng

> "Aso sa tabi ng Eiffel Tower sa umaga habang sumisikat ang araw"

## Ano ang DALL-E at Midjourney?

Ang [DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) at [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) ay dalawa sa pinakasikat na modelo para sa paglikha ng larawan, na nagbibigay-daan sa iyo na gumamit ng mga prompt para lumikha ng mga larawan.

### DALL-E

Simulan natin sa DALL-E, isang Generative AI model na lumilikha ng mga larawan mula sa mga deskripsyon sa teksto.

> [Ang DALL-E ay kombinasyon ng dalawang modelo, CLIP at diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, ay isang modelo na lumilikha ng embeddings, na mga numerikal na representasyon ng data, mula sa mga larawan at teksto.

- **Diffused attention**, ay isang modelo na lumilikha ng mga larawan mula sa embeddings. Ang DALL-E ay sinanay gamit ang dataset ng mga larawan at teksto at maaaring gamitin para lumikha ng mga larawan mula sa mga deskripsyon sa teksto. Halimbawa, maaaring gamitin ang DALL-E para lumikha ng larawan ng pusa na may sumbrero, o aso na may mohawk.

### Midjourney

Gumagana ang Midjourney na halos katulad ng DALL-E, lumilikha ito ng mga larawan mula sa mga text prompt. Maaari ring gamitin ang Midjourney para lumikha ng mga larawan gamit ang mga prompt tulad ng “pusa na may sumbrero”, o “aso na may mohawk”.

![Larawang nilikha ng Midjourney, mechanical pigeon](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Larawan mula sa Wikipedia, nilikha gamit ang Midjourney_

## Paano gumagana ang DALL-E at Midjourney

Una, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). Ang DALL-E ay isang Generative AI model na nakabase sa transformer architecture na may _autoregressive transformer_.

Ang _autoregressive transformer_ ay tumutukoy kung paano lumilikha ng larawan ang isang modelo mula sa mga deskripsyon sa teksto, nililikha nito ang larawan isang pixel kada pagkakataon, at ginagamit ang mga nagawang pixel para lumikha ng susunod na pixel. Dumadaan ito sa maraming layer ng neural network hanggang mabuo ang larawan.

Sa prosesong ito, nakokontrol ng DALL-E ang mga katangian, bagay, karakteristik, at iba pa sa larawang nililikha nito. Ngunit, mas malaki ang kontrol ng DALL-E 2 at 3 sa nililikhang larawan.

## Pagbuo ng iyong unang image generation application

Ano ang kailangan para makagawa ng image generation application? Kailangan mo ng mga sumusunod na library:

- **python-dotenv**, inirerekomenda na gamitin ito para itago ang iyong mga secrets sa _.env_ file na hiwalay sa code.
- **openai**, ito ang library na gagamitin mo para makipag-ugnayan sa OpenAI API.
- **pillow**, para magtrabaho sa mga larawan gamit ang Python.
- **requests**, para tumulong sa paggawa ng HTTP requests.

## Gumawa at mag-deploy ng Azure OpenAI model

Kung hindi mo pa nagagawa, sundin ang mga tagubilin sa [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) page
para gumawa ng Azure OpenAI resource at model. Piliin ang DALL-E 3 bilang model.  

## Gumawa ng app

1. Gumawa ng file na _.env_ na may ganitong laman:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Hanapin ang impormasyong ito sa Azure OpenAI Foundry Portal para sa iyong resource sa seksyong "Deployments".

1. Ilista ang mga nabanggit na library sa file na _requirements.txt_ tulad nito:

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

   Para sa Windows, gamitin ang mga sumusunod na command para gumawa at i-activate ang iyong virtual environment:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Idagdag ang sumusunod na code sa file na _app.py_:

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

- Sunod, niloload natin ang environment variables mula sa _.env_ file.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Pagkatapos, kinokonpigure natin ang Azure OpenAI service client 

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Sunod, nililikha natin ang larawan:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Ang code sa itaas ay magbabalik ng JSON object na naglalaman ng URL ng nilikhang larawan. Maaari nating gamitin ang URL para i-download ang larawan at i-save ito sa file.

- Sa huli, binubuksan natin ang larawan at ginagamit ang standard image viewer para ipakita ito:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Karagdagang detalye sa paglikha ng larawan

Tingnan natin nang mas detalyado ang code na lumilikha ng larawan:

    ```python
      generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                            )
    ```

- **prompt**, ito ang text prompt na ginagamit para lumikha ng larawan. Sa kasong ito, ginagamit natin ang prompt na "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils".
- **size**, ito ang laki ng larawang nililikha. Sa kasong ito, gumagawa tayo ng larawang 1024x1024 pixels.
- **n**, ito ang bilang ng larawang nililikha. Sa kasong ito, dalawang larawan ang nililikha natin.
- **temperature**, ito ay parameter na kumokontrol sa randomness ng output ng Generative AI model. Ang temperature ay value mula 0 hanggang 1 kung saan ang 0 ay deterministic at ang 1 ay random ang output. Default value ay 0.7.

Marami pang ibang bagay na maaari mong gawin sa mga larawan na tatalakayin natin sa susunod na seksyon.

## Karagdagang kakayahan ng image generation

Nakita mo na kung paano tayo nakalikha ng larawan gamit ang ilang linya ng Python. Pero marami pang ibang bagay na maaari mong gawin sa mga larawan.

Maaari mo ring gawin ang mga sumusunod:

- **Mag-edit ng larawan**. Sa pamamagitan ng pagbibigay ng existing na larawan, mask, at prompt, maaari mong baguhin ang isang larawan. Halimbawa, maaari kang magdagdag ng bagay sa isang bahagi ng larawan. Isipin ang larawan ng bunny, maaari kang magdagdag ng sumbrero sa bunny. Gagawin mo ito sa pamamagitan ng pagbibigay ng larawan, mask (tinutukoy ang bahagi ng area na babaguhin) at text prompt para sabihin kung ano ang dapat gawin. 
> Note: hindi ito suportado sa DALL-E 3. 
 
Narito ang halimbawa gamit ang GPT Image:

    ```python
    response = client.images.edit(
        model="gpt-image-1",
        image=open("sunlit_lounge.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo"
    )
    image_url = response.data[0].url
    ```

  Ang base image ay naglalaman lang ng lounge na may pool pero ang final image ay may flamingo na:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="./images/sunlit_lounge.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/mask.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/sunlit_lounge_result.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Gumawa ng mga variation**. Ang ideya ay kumuha ng existing na larawan at hilingin na gumawa ng mga variation. Para gumawa ng variation, magbibigay ka ng larawan at text prompt at code tulad nito:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Note, ito ay suportado lamang sa OpenAI

## Temperature

Ang temperature ay parameter na kumokontrol sa randomness ng output ng Generative AI model. Ang temperature ay value mula 0 hanggang 1 kung saan ang 0 ay deterministic at ang 1 ay random ang output. Default value ay 0.7.

Tingnan natin ang halimbawa kung paano gumagana ang temperature, sa pamamagitan ng pagpapatakbo ng prompt na ito ng dalawang beses:

> Prompt : "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![Bunny on a horse holding a lollipop, version 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.tl.png)

Ngayon, patakbuhin natin ulit ang parehong prompt para makita na hindi pareho ang larawang lalabas:

![Generated image of bunny on horse](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.tl.png)

Makikita mo na magkahawig ang mga larawan, pero hindi magkapareho. Subukan nating baguhin ang temperature value sa 0.1 at tingnan ang mangyayari:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Pagbabago ng temperature

Subukan nating gawing mas deterministic ang response. Mapapansin natin sa dalawang larawang nagawa na sa una, may bunny at sa pangalawa, may kabayo, kaya magkaiba talaga ang mga larawan.

Kaya, baguhin natin ang code at itakda ang temperature sa 0, ganito:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Kapag pinatakbo mo ang code na ito, makakakuha ka ng dalawang larawang ito:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.tl.png)
- ![Temperature 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.tl.png)

Dito, makikita mong mas magkahawig na ang mga larawan.

## Paano magtakda ng boundaries para sa iyong application gamit ang metaprompts

Sa demo natin, kaya na nating lumikha ng mga larawan para sa ating mga kliyente. Pero kailangan nating magtakda ng mga limitasyon para sa ating application.

Halimbawa, ayaw nating lumikha ng mga larawang hindi angkop sa trabaho, o hindi angkop para sa mga bata.

Magagawa natin ito gamit ang _metaprompts_. Ang metaprompts ay mga text prompt na ginagamit para kontrolin ang output ng Generative AI model. Halimbawa, maaari tayong gumamit ng metaprompts para kontrolin ang output, at tiyaking ang mga larawang nililikha ay ligtas sa trabaho, o angkop para sa mga bata.

### Paano ito gumagana?

Paano nga ba gumagana ang meta prompts?

Ang meta prompts ay mga text prompt na ginagamit para kontrolin ang output ng Generative AI model, inilalagay ito bago ang text prompt, at ginagamit para kontrolin ang output ng model at ini-embed sa mga application para kontrolin ang output ng model. Pinagsasama ang prompt input at meta prompt input sa isang text prompt.

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

Mula sa prompt sa itaas, makikita mo kung paano isinasaalang-alang ng lahat ng larawang nililikha ang metaprompt.

## Assignment - bigyang kakayahan ang mga estudyante

Ipinakilala natin ang Edu4All sa simula ng araling ito. Ngayon, panahon na para bigyang kakayahan ang mga estudyante na lumikha ng mga larawan para sa kanilang assessment.

Ang mga estudyante ay gagawa ng mga larawan para sa kanilang assessment na may mga monumento, kung anong monumento ay depende sa estudyante. Hinihikayat ang mga estudyante na gamitin ang kanilang pagkamalikhain sa gawaing ito at ilagay ang mga monumento sa iba't ibang konteksto.

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

## Mahusay! Ipagpatuloy ang Iyong Pagkatuto
Pagkatapos mong matapos ang araling ito, bisitahin ang aming [Koleksyon ng Pagkatuto sa Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para patuloy na palawakin ang iyong kaalaman sa Generative AI!

Pumunta na sa Aralin 10 kung saan tatalakayin natin kung paano [bumuo ng AI applications gamit ang low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring lumitaw mula sa paggamit ng pagsasaling ito.