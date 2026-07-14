# Kujenga Programu za Kizalishaji Picha

[![Kujenga Programu za Kizalishaji Picha](../../../translated_images/sw/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLMs haziwezi tu kuzalisha maandishi. Pia inawezekana kuzalisha picha kutoka kwa maelezo ya maandishi. Kuwa na picha kama njia ya mawasiliano inaweza kuwa na manufaa makubwa katika maeneo kadhaa kama MedTech, usanifu, utalii, kuendeleza michezo na mengineyo. Katika sura hii, tutaangazia mifano miwili maarufu ya kizalishaji picha, DALL-E na Midjourney.

## Utangulizi

Katika somo hili, tutashughulikia:

- Kizalishaji picha na kwa nini ni muhimu.
- DALL-E na Midjourney, ni nini, na zinafanya kazi vipi.
- Jinsi unavyoweza kujenga programu ya kizalishaji picha.

## Malengo ya Kujifunza

Baada ya kumaliza somo hili, utaweza:

- Kujenga programu ya kizalishaji picha.
- Kuweka mipaka kwa programu yako kwa kutumia meta prompts.
- Kufanya kazi na DALL-E na Midjourney.

## Kwa nini ujenge programu ya kizalishaji picha?

Programu za kizalishaji picha ni njia nzuri ya kuchunguza uwezo wa AI Inayozalisha. Zinaweza kutumiwa, kwa mfano:

- **KuHariri na Kuchanganya Picha**. Unaweza kuzalisha picha kwa matumizi mbalimbali, kama vile kuhariri picha na kuchanganya picha.

- **Kutumika katika sekta mbalimbali**. Pia zinaweza kutumika kuzalisha picha kwa sekta tofauti kama Medtech, Utalii, Uendelezaji wa Michezo na mengineyo.

## Hali ya Mfano: Edu4All

Kama sehemu ya somo hili, tutaendelea kufanya kazi na startup yetu, Edu4All, katika somo hili. Wanafunzi wataunda picha kwa tathmini zao, ni picha gani ni chaguo la wanafunzi, lakini inaweza kuwa michoro ya hadithi zao au kuunda mhusika mpya kwa hadithi zao au kuwasaidia kuona mawazo na dhana zao.

Hapa ni kile wanafunzi wa Edu4All wanaweza kuzalisha mfano ikiwa wanafanya kazi darasani juu ya makumbusho:

![Startup ya Edu4All, darasa kuhusu makumbusho, Mnara wa Eiffel](../../../translated_images/sw/startup.94d6b79cc4bb3f5a.webp)

kwa kutumia kauli kama

> "Mbwa kando ya Mnara wa Eiffel katika mwanga wa jua wa asubuhi"

## DALL-E na Midjourney ni nini?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) na [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) ni mifano miwili maarufu ya kizalishaji picha, inakuwezesha kutumia maelezo (prompts) kuzalisha picha.

### DALL-E

Tuanzie na DALL-E, ambayo ni mfano wa AI Inayozalisha picha kutoka kwa maelezo ya maandishi.

> [DALL-E ni mchanganyiko wa mifano miwili, CLIP na diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, ni mfano unaozalisha embeddings, ambazo ni uwakilishi wa data kwa nambari, kutoka kwa picha na maandishi.

- **Diffused attention**, ni mfano unaozalisha picha kutoka kwa embeddings. DALL-E imetengenezwa kwa dataset ya picha na maandishi na inaweza kutumiwa kuzalisha picha kutoka kwa maelezo ya maandishi. Kwa mfano, DALL-E inaweza kutumiwa kuzalisha picha ya paka aliyevaa kofia, au mbwa aliye na mohawk.

### Midjourney

Midjourney hufanya kazi kwa njia sawa na DALL-E, huchuja picha kutoka kwa maelezo ya maandishi. Midjourney pia inaweza kutumiwa kuzalisha picha kwa kutumia maelezo kama "paka aliyevaa kofia", au "mbwa aliye na mohawk".

![Picha iliyozalishwa na Midjourney, njiwa wa mitambo](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Picha kwa mkopo Wikipedia, picha iliyozalishwa na Midjourney_

## Jinsi DALL-E na Midjourney Zinavyofanya Kazi

Kwanza, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E ni mfano wa AI Inayozalisha ukiwa na usanifu wa transformer na _autoregressive transformer_.

_Autoregressive transformer_ huamua jinsi mfano unavyozalisha picha kutoka kwa maelezo ya maandishi, huzalisha pixel moja kwa moja, kisha hutumia pixels zilizozalishwa kuzalisha pixel inayofuata. Hupitia tabaka nyingi katika mtandao wa neva, hadi picha iwe kamili.

Katika mchakato huu, DALL-E hudhibiti sifa, vitu, tabia, na zaidi kwenye picha inayozalishwa. Hata hivyo, DALL-E 2 na 3 zina udhibiti zaidi wa picha inayozalishwa.

## Kujenga Programu yako ya Kizalishaji Picha ya Kwanza

Sasa inahitaji nini kujenga programu ya kizalishaji picha? Unahitaji maktaba zifuatazo:

- **python-dotenv**, inashauriwa sana kutumia maktaba hii kuweka siri zako katika faili ya _.env_ mbali na msimbo.
- **openai**, maktaba hii ndiyo utakayotumia kuingiliana na API ya OpenAI.
- **pillow**, kufanya kazi na picha kwa Python.
- **requests**, kusaidia kutuma maombi ya HTTP.

## Unda na tuma mfano wa Azure OpenAI

Ikiwa bado haujafanya, fuata maelekezo kwenye ukurasa wa [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)
kuunda rasilimali na mfano wa Azure OpenAI. Chagua **gpt-image-1** kama mfano (mfano wa sasa wa kizazi wa picha wa Azure OpenAI; DALL-E 3 ni ya zamani na haipatikani tena kwa utoaji mpya).

## Tengeneza programu

1. Unda faili _.env_ ikiwa na maudhui yafuatayo:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   Tafuta taarifa hizi kwenye Azure OpenAI Foundry Portal kwa rasilimali yako kwenye sehemu ya "Deployments".

1. Kusanya maktaba hapo juu kwenye faili liitwalo _requirements.txt_ kama ifuatavyo:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Kisha, unda mazingira ya virtual na weka maktaba:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Kwa Windows, tumia amri zifuatazo kuunda na kuanzisha mazingira yako ya virtual:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Ongeza msimbo ufuatao kwenye faili liitwalo _app.py_:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # ingiza dotenv
    dotenv.load_dotenv()
    
    # weka mteja wa huduma ya Azure OpenAI
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # Tengeneza picha kwa kutumia API ya kizazi cha picha
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Weka saraka kwa picha iliyo hifadhiwa
        image_dir = os.path.join(os.curdir, 'images')

        # Ikiwa saraka haipo, unda
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Anzisha njia ya picha (zingatia aina ya faili iwe png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Pata picha iliyozalishwa
        image_url = generation_response.data[0].url  # toa URL ya picha kutoka kwa majibu
        generated_image = requests.get(image_url).content  # pakua picha
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # Onyesha picha kwenye mzunguzi wa picha wa chaguo-msingi
        image = Image.open(image_path)
        image.show()

    # shika makosa
    except openai.BadRequestError as err:
        print(err)
   ```

Hebu tuelezee msimbo huu:

- Kwanza, tunaingiza maktaba tunazohitaji, ikiwemo maktaba ya OpenAI, dotenv, requests, na Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Kisha, tunapakia mabadiliko ya mazingira kutoka faili _.env_.

  ```python
  # ingiza dotenv
  dotenv.load_dotenv()
  ```

- Baada yake, tunasanidi mteja wa huduma ya Azure OpenAI

  ```python
  # Pata anuani ya mwisho na funguo kutoka kwa mabadiliko ya mazingira
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- Kisha, tunazalisha picha:

  ```python
  # Tengeneza picha kwa kutumia API ya uundaji picha
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Msimbo hapo juu unajibu kwa kitu cha JSON kinachojumuisha URL ya picha iliyozalishwa. Tunaweza kutumia URL kupakua picha na kuihifadhi kwenye faili.

- Mwishowe, tunafungua picha na kuitumia viewer ya picha ya kawaida kuionyesha:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Maelezo zaidi kuhusu kuzalisha picha

Hebu tazame msimbo unaozalisha picha kwa undani zaidi:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, ni maelezo ya maandishi yanayotumiwa kuzalisha picha. Katika kesi hii, tunatumia kauli "Bunny juu ya farasi, akishikilia lollipop, kwenye uwanja wenye ukungu ambapo wanakua daffodils".
- **size**, ni ukubwa wa picha inayozalishwa. Katika kesi hii, tunazalisha picha ya ukubwa wa 1024x1024 pixels.
- **n**, ni idadi ya picha zinazozalishwa. Katika kesi hii, tunazalisha picha mbili.
- **temperature**, ni kipimo kinachodhibiti randomness ya matokeo ya mfano wa AI Inayozalisha. Joto ni thamani kati ya 0 na 1 ambapo 0 inamaanisha matokeo ni ya kubashiri na 1 inamaanisha matokeo ni ya kubahatisha. Thamani ya default ni 0.7.

Kuna mambo zaidi unaweza kufanya na picha ambayo tutayajadili katika sehemu inayofuata.

## Uwezo Zaidi wa Kizalishaji Picha

Umeona hivi sasa jinsi tulivyoweza kuzalisha picha kwa mistari michache ya Python. Hata hivyo, kuna mambo zaidi unaweza kufanya na picha.

Pia unaweza kufanya yafuatayo:

- **Fanya marekebisho**. Kwa kutoa picha iliyopo, mask na kauli, unaweza kubadilisha picha. Kwa mfano, unaweza kuongeza kitu sehemu ya picha. Fikiria picha yetu ya bunny, unaweza kuongeza kofia kwa bunny. Unavyofanya hivyo ni kwa kutoa picha, mask (inayoonyesha sehemu ya eneo la kubadilisha) na kauli ya maandishi kuelezea kinachotakiwa kufanywa.
> Kumbuka: hii haitegemezwi katika DALL-E 3.
 
Hapa kuna mfano kutumia GPT Image:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  Picha ya msingi itakuwa na chumba cha kupumzika na bwawa tu lakini picha ya mwisho itakuwa na flamingo:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sw/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sw/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sw/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **Tengeneza mabadiliko**. Wazo ni kwamba unachukua picha iliyopo na kuomba mabadiliko yazalishwe. Kutengeneza mabadiliko, unatoa picha na kauli ya maandishi na msimbo kama ifuatavyo:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > Kumbuka, hii inategemezwa tu katika mfano wa OpenAI wa DALL-E 2, sio gpt-image-1

## Joto (Temperature)

Joto ni kipimo kinachodhibiti randomness ya matokeo ya mfano wa AI Inayozalisha. Joto ni thamani kati ya 0 na 1 ambapo 0 inamaanisha matokeo ni ya kubashiri na 1 inamaanisha matokeo ni ya kubahatisha. Thamani ya default ni 0.7.

Hebu tazame mfano wa jinsi joto linavyofanya kazi, kwa kuendesha kauli hii mara mbili:

> Kauli : "Bunny juu ya farasi, akishikilia lollipop, kwenye uwanja wenye ukungu ambapo wanakua daffodils"

![Bunny juu ya farasi akishikilia lollipop, toleo la 1](../../../translated_images/sw/v1-generated-image.a295cfcffa3c13c2.webp)

Sasa tuendeshe kauli hiyo tena kuona kwamba hatutapata picha moja kwa mara mbili:

![Picha iliyozalishwa ya bunny juu ya farasi](../../../translated_images/sw/v2-generated-image.33f55a3714efe61d.webp)

Kama unavyoona, picha ni sawa, lakini sio sawa kabisa. Hebu jaribu kubadilisha thamani ya joto kuwa 0.1 na tazame kinachotokea:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Ingiza maandishi ya ombi lako hapa
        size='1024x1024',
        n=2
    )
```

### Kubadilisha joto

Kwa hivyo hebu jaribu kufanya majibu yawe ya kubashiri zaidi. Tunaweza kuona kutoka kwa picha mbili tulizozalisha kwamba katika picha ya kwanza, kuna bunny na katika picha ya pili kuna farasi, hivyo picha zinatofautiana sana.

Kwa hivyo badilisha msimbo wetu na kuweka joto kuwa 0, kama ifuatavyo:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Weka maandishi yako ya haraka hapa
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Sasa unapoendesha msimbo huu, unapata picha hizi mbili:

- ![Joto 0, v1](../../../translated_images/sw/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![Joto 0, v2](../../../translated_images/sw/v2-temp-generated-image.871d0c920dbfb0f1.webp)

Hapa unaweza kuona wazi jinsi picha zinavyofanana zaidi.

## Jinsi ya kuweka mipaka kwa programu yako kwa kutumia metaprompts

Kwa maonyesho yetu, tayari tunaweza kuzalisha picha kwa wateja wetu. Hata hivyo, tunahitaji kuweka mipaka kwa programu yetu.

Kwa mfano, hatutaki kuzalisha picha zisizo salama kwa mahali pa kazi, au zisizofaa kwa watoto.

Tunaweza kufanya hivi kwa kutumia _metaprompts_. Metaprompts ni kauli za maandishi zinazotumiwa kudhibiti matokeo ya mfano wa AI Inayozalisha. Kwa mfano, tunaweza kutumia metaprompts kudhibiti matokeo, na kuhakikisha picha zinazozalishwa ni salama kwa mahali pa kazi, au zinazofaa kwa watoto.

### Inafanyaje kazi?

Sasa, je, metaprompts zinafanya kazi vipi?

Metaprompts ni kauli za maandishi zinazotumiwa kudhibiti matokeo ya mfano wa AI Inayozalisha, zipo kabla ya kauli kuu, na hutumiwa kudhibiti matokeo ya mfano na kuingizwa katika programu kudhibiti matokeo ya mfano. Hufungasha maingizo ya prompt na meta prompt katika prompt moja ya maandishi.

Mfano mmoja wa meta prompt ungekuwa kama ifuatavyo:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Sasa, tazame jinsi tunavyoweza kutumia meta prompts katika maonyesho yetu.

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

# TODO ongeza ombi la kuunda picha
```

Kutoka kwenye kauli hiyo hapo juu, unaweza kuona jinsi zote picha zinazozalishwa zinazingatia metaprompt.

## Kazi ya nyumbani - tuwezeshe wanafunzi

Tulizindua Edu4All mwanzoni mwa somo hili. Sasa ni wakati wa kuwawezesha wanafunzi kuzalisha picha kwa ajili ya tathmini zao.


Wanafunzi wataunda picha kwa tathmini zao zenye sanamu, ni sanamu gani hasa ni mbali na wanafunzi. Wanafunzi wanaombwa kutumia ubunifu wao katika kazi hii kuweka sanamu hizi katika muktadha tofauti.

## Suluhisho

Hapa kuna suluhisho moja lililowezekana:

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# import dotenv
dotenv.load_dotenv()

# Pata sehemu ya mwisho na ufunguo kutoka kwa vigezo vya mazingira
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-10-21"
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
"""

try:
    # Unda picha kwa kutumia API ya kizazi cha picha
    generation_response = client.images.generate(
        prompt=prompt,    # Weka maandishi yako ya maelekezo hapa
        size='1024x1024',
        n=1,
    )
    # Weka saraka kwa picha iliyohifadhiwa
    image_dir = os.path.join(os.curdir, 'images')

    # Ikiwa saraka haipo, iunde
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Anzisha njia ya picha (kumbuka aina ya faili inapaswa kuwa png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Pata picha iliyotengenezwa
    image_url = generation_response.data[0].url  # toa URL ya picha kutoka kwa majibu
    generated_image = requests.get(image_url).content  # pakua picha
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Onyesha picha katika mtazamaji wa picha wa chaguo-msingi
    image = Image.open(image_path)
    image.show()

# shika makosa
except openai.BadRequestError as err:
    print(err)
```

## Kazi Nzuri! Endelea Kujifunza

Baada ya kumaliza somo hili, angalia [Mkusanyiko wa Kujifunza AI Inayotengeneza](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) kuendelea kuongeza uelewa wako wa AI Inayotengeneza!

Nenda Somo la 10 ambapo tutaangalia jinsi ya [kujenga programu za AI kwa nambari kidogo](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->