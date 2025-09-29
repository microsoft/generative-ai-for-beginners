<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T22:09:08+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "sw"
}
-->
# Kujenga Programu za Kuzalisha Picha

[![Kujenga Programu za Kuzalisha Picha](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.sw.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLMs zina uwezo zaidi ya kuzalisha maandishi pekee. Inawezekana pia kuzalisha picha kutoka kwa maelezo ya maandishi. Kuwa na picha kama njia ya mawasiliano kunaweza kuwa muhimu sana katika maeneo mbalimbali kama MedTech, usanifu majengo, utalii, ukuzaji wa michezo, na zaidi. Katika sura hii, tutachunguza mifano miwili maarufu ya kuzalisha picha, DALL-E na Midjourney.

## Utangulizi

Katika somo hili, tutajadili:

- Kuzalisha picha na umuhimu wake.
- DALL-E na Midjourney, ni nini na jinsi zinavyofanya kazi.
- Jinsi ya kujenga programu ya kuzalisha picha.

## Malengo ya Kujifunza

Baada ya kukamilisha somo hili, utaweza:

- Kujenga programu ya kuzalisha picha.
- Kufafanua mipaka ya programu yako kwa kutumia meta prompts.
- Kufanya kazi na DALL-E na Midjourney.

## Kwa nini kujenga programu ya kuzalisha picha?

Programu za kuzalisha picha ni njia nzuri ya kuchunguza uwezo wa Generative AI. Zinatumika kwa mfano:

- **Uhariri na muunganiko wa picha**. Unaweza kuzalisha picha kwa matumizi mbalimbali, kama vile uhariri wa picha na muunganiko wa picha.

- **Kutumika katika sekta mbalimbali**. Zinatumika pia kuzalisha picha kwa sekta mbalimbali kama MedTech, Utalii, ukuzaji wa michezo, na zaidi.

## Hali: Edu4All

Kama sehemu ya somo hili, tutaendelea kufanya kazi na kampuni yetu ya kuanzisha, Edu4All. Wanafunzi wataunda picha kwa ajili ya tathmini zao, aina ya picha ni juu yao, lakini zinaweza kuwa michoro ya hadithi yao ya kufikirika, kuunda mhusika mpya kwa hadithi yao, au kuwasaidia kuona mawazo na dhana zao.

Hapa kuna mfano wa kile wanafunzi wa Edu4All wanaweza kuzalisha ikiwa wanajifunza darasani kuhusu makaburi:

![Kampuni ya Edu4All, darasa kuhusu makaburi, Mnara wa Eiffel](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.sw.png)

kwa kutumia prompt kama

> "Mbwa karibu na Mnara wa Eiffel katika mwanga wa jua wa asubuhi mapema"

## DALL-E na Midjourney ni nini?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) na [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) ni mifano miwili maarufu ya kuzalisha picha, zinakuruhusu kutumia prompts kuzalisha picha.

### DALL-E

Tuanzie na DALL-E, ambayo ni mfano wa Generative AI unaozalisha picha kutoka kwa maelezo ya maandishi.

> [DALL-E ni mchanganyiko wa mifano miwili, CLIP na diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, ni mfano unaozalisha embeddings, ambazo ni uwakilishi wa namba wa data, kutoka kwa picha na maandishi.

- **Diffused attention**, ni mfano unaozalisha picha kutoka kwa embeddings. DALL-E imefundishwa kwa seti ya data ya picha na maandishi na inaweza kutumika kuzalisha picha kutoka kwa maelezo ya maandishi. Kwa mfano, DALL-E inaweza kutumika kuzalisha picha ya paka aliyevaa kofia, au mbwa mwenye mohawk.

### Midjourney

Midjourney inafanya kazi kwa njia sawa na DALL-E, inazalisha picha kutoka kwa prompts za maandishi. Midjourney, inaweza pia kutumika kuzalisha picha kwa kutumia prompts kama "paka aliyevaa kofia", au "mbwa mwenye mohawk".

![Picha iliyozalishwa na Midjourney, njiwa wa mitambo](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Picha kwa hisani ya Wikipedia, picha iliyozalishwa na Midjourney_

## Jinsi DALL-E na Midjourney Zinavyofanya Kazi

Kwanza, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E ni mfano wa Generative AI unaotegemea usanifu wa transformer na _autoregressive transformer_.

_Autoregressive transformer_ hufafanua jinsi mfano unavyotoa picha kutoka kwa maelezo ya maandishi, inazalisha pikseli moja kwa wakati, na kisha kutumia pikseli zilizozalishwa kuzalisha pikseli inayofuata. Inapitia tabaka nyingi katika mtandao wa neva, hadi picha ikamilike.

Kwa mchakato huu, DALL-E, inadhibiti sifa, vitu, tabia, na zaidi katika picha inayozalishwa. Hata hivyo, DALL-E 2 na 3 zina udhibiti zaidi juu ya picha inayozalishwa.

## Kujenga programu yako ya kwanza ya kuzalisha picha

Kwa hivyo, inachukua nini kujenga programu ya kuzalisha picha? Unahitaji maktaba zifuatazo:

- **python-dotenv**, inashauriwa sana kutumia maktaba hii kuweka siri zako katika faili ya _.env_ mbali na msimbo.
- **openai**, maktaba hii ndiyo utatumia kuwasiliana na API ya OpenAI.
- **pillow**, kufanya kazi na picha katika Python.
- **requests**, kusaidia kufanya maombi ya HTTP.

## Unda na peleka mfano wa Azure OpenAI

Ikiwa bado hujafanya, fuata maelekezo kwenye ukurasa wa [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) 
kuunda rasilimali ya Azure OpenAI na mfano. Chagua DALL-E 3 kama mfano.  

## Unda programu

1. Unda faili _.env_ yenye maudhui yafuatayo:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Tafuta taarifa hii katika Azure OpenAI Foundry Portal kwa rasilimali yako katika sehemu ya "Deployments".

1. Kusanya maktaba zilizo hapo juu katika faili inayoitwa _requirements.txt_ kama ifuatavyo:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Kisha, unda mazingira ya kawaida na usakinishe maktaba:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Kwa Windows, tumia amri zifuatazo kuunda na kuamsha mazingira yako ya kawaida:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Ongeza msimbo ufuatao katika faili inayoitwa _app.py_:

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

Tueleze msimbo huu:

- Kwanza, tunaleta maktaba tunazohitaji, ikiwa ni pamoja na maktaba ya OpenAI, maktaba ya dotenv, maktaba ya requests, na maktaba ya Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Kisha, tunapakia vigezo vya mazingira kutoka kwa faili ya _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Baada ya hapo, tunasanidi mteja wa huduma ya Azure OpenAI 

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Kisha, tunazalisha picha:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Msimbo hapo juu unajibu na kitu cha JSON kinachojumuisha URL ya picha iliyozalishwa. Tunaweza kutumia URL kupakua picha na kuihifadhi kwenye faili.

- Mwisho, tunafungua picha na kutumia kionyeshi cha picha cha kawaida kuionyesha:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Maelezo zaidi kuhusu kuzalisha picha

Hebu tuangalie msimbo unaozalisha picha kwa undani zaidi:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, ni prompt ya maandishi inayotumika kuzalisha picha. Katika kesi hii, tunatumia prompt "Sungura juu ya farasi, akiwa na lollipop, kwenye uwanda wenye ukungu ambapo maua ya daffodils yanamea".
- **size**, ni ukubwa wa picha inayozalishwa. Katika kesi hii, tunazalisha picha yenye ukubwa wa pikseli 1024x1024.
- **n**, ni idadi ya picha zinazozalishwa. Katika kesi hii, tunazalisha picha mbili.
- **temperature**, ni parameter inayodhibiti nasibu ya matokeo ya mfano wa Generative AI. Temperature ni thamani kati ya 0 na 1 ambapo 0 inamaanisha matokeo ni ya uhakika na 1 inamaanisha matokeo ni ya nasibu. Thamani ya default ni 0.7.

Kuna mambo zaidi unayoweza kufanya na picha ambayo tutajadili katika sehemu inayofuata.

## Uwezo wa ziada wa kuzalisha picha

Umeona hadi sasa jinsi tulivyoweza kuzalisha picha kwa mistari michache katika Python. Hata hivyo, kuna mambo zaidi unayoweza kufanya na picha.

Unaweza pia kufanya yafuatayo:

- **Kufanya uhariri**. Kwa kutoa picha iliyopo, mask, na prompt, unaweza kubadilisha picha. Kwa mfano, unaweza kuongeza kitu kwenye sehemu ya picha. Fikiria picha yetu ya sungura, unaweza kuongeza kofia kwa sungura. Jinsi unavyoweza kufanya hivyo ni kwa kutoa picha, mask (kutambua sehemu ya eneo la mabadiliko) na prompt ya maandishi kusema nini kifanyike. 
> Kumbuka: hii haijaungwa mkono katika DALL-E 3. 
 
Hapa kuna mfano wa kutumia GPT Image:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  Picha ya msingi ingekuwa na lounge tu na bwawa lakini picha ya mwisho ingekuwa na flamingo:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.sw.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.sw.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.sw.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Kuunda tofauti**. Wazo ni kwamba unachukua picha iliyopo na kuomba kwamba tofauti zifanywe. Ili kuunda tofauti, unatoa picha na prompt ya maandishi na msimbo kama ifuatavyo:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Kumbuka, hii inaungwa mkono tu kwenye OpenAI

## Temperature

Temperature ni parameter inayodhibiti nasibu ya matokeo ya mfano wa Generative AI. Temperature ni thamani kati ya 0 na 1 ambapo 0 inamaanisha matokeo ni ya uhakika na 1 inamaanisha matokeo ni ya nasibu. Thamani ya default ni 0.7.

Hebu tuangalie mfano wa jinsi temperature inavyofanya kazi, kwa kuendesha prompt hii mara mbili:

> Prompt : "Sungura juu ya farasi, akiwa na lollipop, kwenye uwanda wenye ukungu ambapo maua ya daffodils yanamea"

![Sungura juu ya farasi akiwa na lollipop, toleo la 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.sw.png)

Sasa hebu tuendeshe prompt hiyo hiyo ili kuona kwamba hatutapata picha sawa mara mbili:

![Picha iliyozalishwa ya sungura juu ya farasi](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.sw.png)

Kama unavyoona, picha zinafanana, lakini si sawa. Hebu jaribu kubadilisha thamani ya temperature hadi 0.1 na kuona kinachotokea:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Kubadilisha temperature

Kwa hivyo hebu jaribu kufanya majibu yawe ya uhakika zaidi. Tunaweza kuona kutoka kwa picha mbili tulizozalisha kwamba katika picha ya kwanza, kuna sungura na katika picha ya pili, kuna farasi, kwa hivyo picha zinatofautiana sana.

Hebu basi tubadilishe msimbo wetu na kuweka temperature hadi 0, kama ifuatavyo:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Sasa unapoendesha msimbo huu, unapata picha hizi mbili:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.sw.png)
- ![Temperature 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.sw.png)

Hapa unaweza kuona wazi jinsi picha zinavyofanana zaidi.

## Jinsi ya kufafanua mipaka ya programu yako kwa metaprompts

Kwa demo yetu, tunaweza tayari kuzalisha picha kwa wateja wetu. Hata hivyo, tunahitaji kuunda mipaka kwa programu yetu.

Kwa mfano, hatutaki kuzalisha picha ambazo si salama kwa kazi, au ambazo si sahihi kwa watoto.

Tunaweza kufanya hivi kwa _metaprompts_. Metaprompts ni prompts za maandishi zinazotumika kudhibiti matokeo ya mfano wa Generative AI. Kwa mfano, tunaweza kutumia metaprompts kudhibiti matokeo, na kuhakikisha kwamba picha zinazozalishwa ni salama kwa kazi, au sahihi kwa watoto.

### Inafanyaje kazi?

Sasa, metaprompts zinafanyaje kazi?

Metaprompts ni prompts za maandishi zinazotumika kudhibiti matokeo ya mfano wa Generative AI, zinapangwa kabla ya prompt ya maandishi, na zinatumika kudhibiti matokeo ya mfano na kuingizwa katika programu kudhibiti matokeo ya mfano. Kuunganisha prompt ya pembejeo na prompt ya meta katika prompt moja ya maandishi.

Mfano mmoja wa metaprompt ungekuwa kama ifuatavyo:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Sasa, hebu tuone jinsi tunavyoweza kutumia metaprompts katika demo yetu.

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

Kutoka kwa prompt hapo juu, unaweza kuona jinsi picha zote zinazozalishwa zinazingatia metaprompt.

## Kazi - hebu tuwasaidie wanafunzi

Tulianzisha Edu4All mwanzoni mwa somo hili. Sasa ni wakati wa kuwawezesha wanafunzi kuzalisha picha kwa tathmini zao.

Wanafunzi wataunda picha kwa tathmini zao zinazohusiana na makaburi, ni makaburi gani ni juu yao. Wanafunzi wanahimizwa kutumia ubunifu wao katika kazi hii kuweka makaburi haya katika muktadha tofauti.

## Suluhisho

Hapa kuna suluhisho moja linalowezekana:
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

## Kazi Nzuri! Endelea Kujifunza

Baada ya kumaliza somo hili, angalia [Mkusanyiko wa Kujifunza kuhusu AI ya Kizazi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kukuza maarifa yako kuhusu AI ya Kizazi!

Nenda kwenye Somo la 10 ambapo tutachunguza jinsi ya [kuunda programu za AI kwa kutumia low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.