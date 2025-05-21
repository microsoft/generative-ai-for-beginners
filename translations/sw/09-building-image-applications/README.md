<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:20:21+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "sw"
}
-->
# Kujenga Programu za Uzalishaji wa Picha

[![Kujenga Programu za Uzalishaji wa Picha](../../../translated_images/09-lesson-banner.d0229c79fda6596b8a678478e20301b74964cb8161e0c2e4a7c203655c623330.sw.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Kuna mengi zaidi kwenye LLMs kuliko uzalishaji wa maandishi. Inawezekana pia kuzalisha picha kutoka kwa maelezo ya maandishi. Kuwa na picha kama njia inaweza kuwa muhimu sana katika maeneo kadhaa kama MedTech, usanifu, utalii, ukuzaji wa michezo na zaidi. Katika sura hii, tutachunguza mifano miwili maarufu ya uzalishaji wa picha, DALL-E na Midjourney.

## Utangulizi

Katika somo hili, tutajadili:

- Uzalishaji wa picha na kwa nini ni muhimu.
- DALL-E na Midjourney, ni nini, na jinsi zinavyofanya kazi.
- Jinsi ya kujenga programu ya uzalishaji wa picha.

## Malengo ya Kujifunza

Baada ya kukamilisha somo hili, utaweza:

- Kujenga programu ya uzalishaji wa picha.
- Kufafanua mipaka kwa programu yako kwa kutumia meta prompts.
- Kufanya kazi na DALL-E na Midjourney.

## Kwa nini kujenga programu ya uzalishaji wa picha?

Programu za uzalishaji wa picha ni njia nzuri ya kuchunguza uwezo wa AI ya Kizazi. Zinatumika, kwa mfano:

- **Uhariri na usanisi wa picha**. Unaweza kuzalisha picha kwa matumizi mbalimbali, kama vile uhariri wa picha na usanisi wa picha.

- **Kutumika katika sekta mbalimbali**. Zinatumika pia kuzalisha picha kwa sekta mbalimbali kama Medtech, Utalii, Ukuzaji wa michezo na zaidi.

## Hali: Edu4All

Kama sehemu ya somo hili, tutaendelea kufanya kazi na kampuni yetu mpya, Edu4All. Wanafunzi wataunda picha kwa ajili ya tathmini zao, ni picha gani ni juu ya wanafunzi, lakini wanaweza kuwa michoro ya hadithi yao wenyewe au kuunda mhusika mpya kwa hadithi yao au kuwasaidia kuona mawazo na dhana zao.

Hivi ndivyo wanafunzi wa Edu4All wanaweza kuzalisha kwa mfano ikiwa wanajifunza darasani kuhusu makaburi:

![Kampuni ya Edu4All, darasa kuhusu makaburi, Mnara wa Eiffel](../../../translated_images/startup.ec211d74fef9f4175010c3334942b715514230415744b9dd0a69a19f4ad68786.sw.png)

kutumia maelezo kama

> "Mbwa karibu na Mnara wa Eiffel katika mwanga wa jua wa asubuhi"

## DALL-E na Midjourney ni nini?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) na [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) ni mifano miwili maarufu ya uzalishaji wa picha, zinakuruhusu kutumia maelezo kuzalisha picha.

### DALL-E

Tuanze na DALL-E, ambayo ni mfano wa AI ya Kizazi inayozalisha picha kutoka kwa maelezo ya maandishi.

> [DALL-E ni mchanganyiko wa mifano miwili, CLIP na diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, ni mfano unaozalisha embeddings, ambazo ni uwakilishi wa nambari wa data, kutoka kwa picha na maandishi.

- **Diffused attention**, ni mfano unaozalisha picha kutoka kwa embeddings. DALL-E imefundishwa kwenye seti ya data ya picha na maandishi na inaweza kutumika kuzalisha picha kutoka kwa maelezo ya maandishi. Kwa mfano, DALL-E inaweza kutumika kuzalisha picha za paka aliyevaa kofia, au mbwa aliye na mohawk.

### Midjourney

Midjourney inafanya kazi kwa njia sawa na DALL-E, inazalisha picha kutoka kwa maelezo ya maandishi. Midjourney, inaweza pia kutumika kuzalisha picha kwa kutumia maelezo kama "paka aliyevaa kofia", au "mbwa aliye na mohawk".

![Picha iliyozalishwa na Midjourney, njiwa wa mitambo](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Makredi ya Picha Wikipedia, picha iliyozalishwa na Midjourney_

## DALL-E na Midjourney hufanya kazi vipi

Kwanza, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E ni mfano wa AI ya Kizazi inayotegemea usanifu wa transformer na _autoregressive transformer_.

_Autoregressive transformer_ inafafanua jinsi mfano unavyotoa picha kutoka kwa maelezo ya maandishi, inazalisha pikseli moja kwa wakati, na kisha kutumia pikseli zilizozalishwa kuzalisha pikseli inayofuata. Kupitia tabaka nyingi kwenye mtandao wa neva, hadi picha itakapokamilika.

Kwa mchakato huu, DALL-E, inadhibiti sifa, vitu, tabia, na zaidi katika picha inayozalishwa. Hata hivyo, DALL-E 2 na 3 zina udhibiti zaidi juu ya picha iliyozalishwa.

## Kujenga programu yako ya kwanza ya uzalishaji wa picha

Je, inachukua nini kujenga programu ya uzalishaji wa picha? Unahitaji maktaba zifuatazo:

- **python-dotenv**, inashauriwa sana kutumia maktaba hii kuweka siri zako kwenye faili ya _.env_ mbali na msimbo.
- **openai**, maktaba hii ndio utatumia kuingiliana na API ya OpenAI.
- **pillow**, kufanya kazi na picha katika Python.
- **requests**, kusaidia kufanya maombi ya HTTP.

1. Unda faili _.env_ na maudhui yafuatayo:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Pata taarifa hii katika Azure Portal kwa rasilimali yako katika sehemu ya "Keys and Endpoint".

1. Kusanya maktaba zilizo juu katika faili inayoitwa _requirements.txt_ kama ifuatavyo:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Kisha, unda mazingira ya virtual na usakinishe maktaba:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Kwa Windows, tumia amri zifuatazo kuunda na kuamsha mazingira yako ya virtual:

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

Tueleze msimbo huu:

- Kwanza, tunaleta maktaba tunazohitaji, ikiwa ni pamoja na maktaba ya OpenAI, maktaba ya dotenv, maktaba ya requests, na maktaba ya Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Kisha, tunapakia vigezo vya mazingira kutoka kwenye faili ya _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Baada ya hapo, tunaset endpoint, key kwa API ya OpenAI, version na type.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Kisha, tunazalisha picha:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Msimbo wa juu unajibu kwa kitu cha JSON ambacho kina URL ya picha iliyozalishwa. Tunaweza kutumia URL kupakua picha na kuihifadhi kwenye faili.

- Mwisho, tunafungua picha na kutumia kionyeshi cha picha cha kawaida kuionyesha:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Maelezo zaidi juu ya kuzalisha picha

Tuangalie msimbo unaozalisha picha kwa undani zaidi:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, ni maelezo ya maandishi yanayotumika kuzalisha picha. Katika kesi hii, tunatumia maelezo "Sungura juu ya farasi, ameshika pipi, kwenye uwanda wa ukungu ambapo inakua daffodils".
- **size**, ni ukubwa wa picha inayozalishwa. Katika kesi hii, tunazalisha picha yenye pikseli 1024x1024.
- **n**, ni idadi ya picha zinazozalishwa. Katika kesi hii, tunazalisha picha mbili.
- **temperature**, ni parameter inayodhibiti nasibu ya matokeo ya mfano wa AI ya Kizazi. Joto ni thamani kati ya 0 na 1 ambapo 0 inamaanisha kuwa matokeo ni ya uhakika na 1 inamaanisha kuwa matokeo ni ya nasibu. Thamani ya default ni 0.7.

Kuna mambo zaidi unayoweza kufanya na picha ambayo tutajadili katika sehemu inayofuata.

## Uwezo wa ziada wa uzalishaji wa picha

Umeona hadi sasa jinsi tulivyoweza kuzalisha picha kwa kutumia mistari michache katika Python. Hata hivyo, kuna mambo zaidi unayoweza kufanya na picha.

Unaweza pia kufanya yafuatayo:

- **Fanya uhariri**. Kwa kutoa picha iliyopo mask na maelezo, unaweza kubadilisha picha. Kwa mfano, unaweza kuongeza kitu kwenye sehemu ya picha. Fikiria picha yetu ya sungura, unaweza kuongeza kofia kwa sungura. Jinsi unavyoweza kufanya hivyo ni kwa kutoa picha, mask (kutambulisha sehemu ya eneo la mabadiliko) na maelezo ya maandishi kusema nini kinapaswa kufanywa.

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

  Picha ya msingi ingekuwa na sungura tu lakini picha ya mwisho ingekuwa na kofia juu ya sungura.

- **Unda tofauti**. Wazo ni kwamba unachukua picha iliyopo na kuuliza kwamba tofauti zinaundwa. Kuunda tofauti, unatoa picha na maelezo ya maandishi na msimbo kama ifuatavyo:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Kumbuka, hii inasaidiwa tu kwenye OpenAI

## Joto

Joto ni parameter inayodhibiti nasibu ya matokeo ya mfano wa AI ya Kizazi. Joto ni thamani kati ya 0 na 1 ambapo 0 inamaanisha kuwa matokeo ni ya uhakika na 1 inamaanisha kuwa matokeo ni ya nasibu. Thamani ya default ni 0.7.

Tuangalie mfano wa jinsi joto linavyofanya kazi, kwa kuendesha maelezo haya mara mbili:

> Maelezo : "Sungura juu ya farasi, ameshika pipi, kwenye uwanda wa ukungu ambapo inakua daffodils"

![Sungura juu ya farasi ameshika pipi, toleo la 1](../../../translated_images/v1-generated-image.208ba0525ed6ae505504aa852e28d334c0440e9931b7c97f9508176a22d2dd54.sw.png)

Sasa tuendeshe maelezo hayo tena ili kuona kwamba hatutapata picha sawa mara mbili:

![Picha iliyozalishwa ya sungura juu ya farasi](../../../translated_images/v2-generated-image.f0a88c05ef476e95f3682d4b21c9ba2f4807ae71cc29e9c05b42ebbf497cf61b.sw.png)

Kama unavyoona, picha zinafanana, lakini si sawa. Hebu jaribu kubadilisha thamani ya joto hadi 0.1 na kuona nini kinatokea:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Kubadilisha joto

Kwa hivyo jaribu kufanya majibu yawe ya uhakika zaidi. Tunaweza kuona kutoka kwa picha mbili tulizozalisha kwamba kwenye picha ya kwanza, kuna sungura na kwenye picha ya pili, kuna farasi, kwa hivyo picha zinatofautiana sana.

Kwa hivyo hebu tubadilishe msimbo wetu na kuweka joto hadi 0, kama ifuatavyo:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Sasa unapoendesha msimbo huu, unapata picha hizi mbili:

- ![Joto 0, v1](../../../translated_images/v1-temp-generated-image.d8557be792b5c81c2c6d2804cb7b210fe8b340106fe4ffcadf9cf7de1cd7b991.sw.png)
- ![Joto 0, v2](../../../translated_images/v2-temp-generated-image.bd412fcfbd43379312b1382212a332aa311ca1a80ea692dea50a8b876a487c61.sw.png)

Hapa unaweza kuona wazi jinsi picha zinavyofanana zaidi.

## Jinsi ya kufafanua mipaka kwa programu yako kwa kutumia metaprompts

Kwa demo yetu, tunaweza tayari kuzalisha picha kwa wateja wetu. Hata hivyo, tunahitaji kuunda mipaka kwa programu yetu.

Kwa mfano, hatutaki kuzalisha picha ambazo hazifai kwa kazi, au ambazo hazifai kwa watoto.

Tunaweza kufanya hivi kwa kutumia _metaprompts_. Metaprompts ni maelezo ya maandishi yanayotumika kudhibiti matokeo ya mfano wa AI ya Kizazi. Kwa mfano, tunaweza kutumia metaprompts kudhibiti matokeo, na kuhakikisha kwamba picha zinazozalishwa zinafaa kwa kazi, au zinafaa kwa watoto.

### Inafanyaje kazi?

Sasa, metaprompts zinafanyaje kazi?

Metaprompts ni maelezo ya maandishi yanayotumika kudhibiti matokeo ya mfano wa AI ya Kizazi, yanawekwa kabla ya maelezo ya maandishi, na yanatumika kudhibiti matokeo ya mfano na kuingizwa katika programu kudhibiti matokeo ya mfano. Kukusanya maelezo ya ingizo na maelezo ya metaprompt katika maelezo moja ya maandishi.

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

Sasa, tuone jinsi tunavyoweza kutumia metaprompts katika demo yetu.

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

Kutoka kwa maelezo ya juu, unaweza kuona jinsi picha zote zinazoundwa zinazingatia metaprompt.

## Kazi - hebu tuwawezeshe wanafunzi

Tulianzisha Edu4All mwanzoni mwa somo hili. Sasa ni wakati wa kuwawezesha wanafunzi kuzalisha picha kwa tathmini zao.

Wanafunzi wataunda picha kwa tathmini zao zinazohusisha makaburi, ni makaburi gani ni juu ya wanafunzi. Wanafunzi wanatakiwa kutumia ubunifu wao katika kazi hii kuweka makaburi haya katika muktadha tofauti.

## Suluhisho

Hapa kuna suluhisho moja linalowezekana:

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

## Kazi Nzuri! Endelea Kujifunza

Baada ya kukamilisha somo hili, angalia mkusanyiko wetu wa [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuimarisha maarifa yako ya AI ya Kizazi!

Nenda kwenye Somo la 10 ambapo tutatazama jinsi ya [kujenga programu za AI kwa kutumia kodikidogo](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Kanusho**: 
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia tafsiri ya kitaalamu ya kibinadamu. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.