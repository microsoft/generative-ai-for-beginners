<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T21:59:45+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "my"
}
-->
# ပုံဖန်တီးခြင်း အက်ပလီကေးရှင်းများ တည်ဆောက်ခြင်း

[![ပုံဖန်တီးခြင်း အက်ပလီကေးရှင်းများ တည်ဆောက်ခြင်း](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.my.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLMs တွေဟာ စာသားဖန်တီးခြင်းထက် ပိုပြီးစွမ်းဆောင်နိုင်ပါတယ်။ စာသားဖော်ပြချက်များမှ ပုံများကို ဖန်တီးနိုင်ခြင်းလည်း ရနိုင်ပါတယ်။ ပုံများကို modality အနေနဲ့ အသုံးပြုခြင်းဟာ MedTech, အိမ်ဆောက်လုပ်ရေး, ခရီးသွားလုပ်ငန်း, ဂိမ်းဖွံ့ဖြိုးရေးနဲ့ အခြားသော နယ်ပယ်များတွင် အလွန်အသုံးဝင်နိုင်ပါတယ်။ ဒီအခန်းမှာတော့ DALL-E နဲ့ Midjourney ဆိုတဲ့ ပုံဖန်တီးခြင်း မော်ဒယ်များနှစ်ခုကို လေ့လာသွားမှာဖြစ်ပါတယ်။

## အကျဉ်းချုပ်

ဒီသင်ခန်းစာမှာ ကျွန်တော်တို့ လေ့လာမယ့်အရာတွေကတော့:

- ပုံဖန်တီးခြင်းနဲ့ အဘယ်ကြောင့် အကျိုးရှိသလဲ။
- DALL-E နဲ့ Midjourney, အဲဒါတွေက ဘာလဲ၊ ဘယ်လိုအလုပ်လုပ်လဲ။
- ပုံဖန်တီးခြင်း အက်ပလီကေးရှင်းကို ဘယ်လိုတည်ဆောက်မလဲ။

## သင်ယူရမယ့် ရည်မှန်းချက်များ

ဒီသင်ခန်းစာပြီးဆုံးတဲ့အခါမှာ သင်တော်မူနိုင်မယ့်အရာတွေကတော့:

- ပုံဖန်တီးခြင်း အက်ပလီကေးရှင်းတစ်ခုကို တည်ဆောက်နိုင်မယ်။
- meta prompts အသုံးပြုပြီး သင့်အက်ပလီကေးရှင်းအတွက် အကန့်အသတ်များ သတ်မှတ်နိုင်မယ်။
- DALL-E နဲ့ Midjourney ကို အသုံးပြုနိုင်မယ်။

## အဘယ်ကြောင့် ပုံဖန်တီးခြင်း အက်ပလီကေးရှင်းတစ်ခုကို တည်ဆောက်ရမလဲ?

ပုံဖန်တီးခြင်း အက်ပလီကေးရှင်းတွေဟာ Generative AI ရဲ့ စွမ်းရည်တွေကို စူးစမ်းဖို့ အကောင်းဆုံးနည်းလမ်းတစ်ခုဖြစ်ပါတယ်။ အဲဒါတွေကို အောက်ပါအတိုင်း အသုံးပြုနိုင်ပါတယ်:

- **ပုံတည်းဖြတ်ခြင်းနဲ့ ပုံပေါင်းစပ်ခြင်း**။ ပုံတည်းဖြတ်ခြင်းနဲ့ ပုံပေါင်းစပ်ခြင်းလို အမျိုးမျိုးသော အသုံးပြုမှုများအတွက် ပုံများကို ဖန်တီးနိုင်ပါတယ်။

- **အမျိုးမျိုးသော စက်မှုလုပ်ငန်းများတွင် အသုံးချနိုင်ခြင်း**။ MedTech, ခရီးသွားလုပ်ငန်း, ဂိမ်းဖွံ့ဖြိုးရေးနဲ့ အခြားသော စက်မှုလုပ်ငန်းများအတွက် ပုံများကို ဖန်တီးနိုင်ပါတယ်။

## အခြေအနေ: Edu4All

ဒီသင်ခန်းစာရဲ့ အစိတ်အပိုင်းတစ်ခုအနေနဲ့ ကျွန်တော်တို့ရဲ့ စတတ်အပ်ဖြစ်တဲ့ Edu4All ကို ဆက်လက်အလုပ်လုပ်သွားမှာဖြစ်ပါတယ်။ ကျောင်းသားတွေဟာ သူတို့ရဲ့ အကဲဖြတ်မှုများအတွက် ပုံများကို ဖန်တီးမယ်၊ ဘယ်လိုပုံတွေဖန်တီးမယ်ဆိုတာ ကျောင်းသားတွေကို အားပေးမှာဖြစ်ပြီး သူတို့ရဲ့ ကိုယ်ပိုင် fairytale အတွက် ပုံဖန်တီးခြင်း၊ သူတို့ရဲ့ ဇာတ်ကောင်အသစ်တစ်ခု ဖန်တီးခြင်း၊ သူတို့ရဲ့ အကြံဉာဏ်နဲ့ အယူအဆတွေကို ရှင်းလင်းဖော်ပြဖို့ ကူညီခြင်း စသည်တို့ကို လုပ်ဆောင်နိုင်ပါတယ်။

Edu4All ရဲ့ ကျောင်းသားတွေဟာ ဥပမာအားဖြင့် အတန်းထဲမှာ အထိမ်းအမှတ်အဆောက်အအုံများအပေါ် အလုပ်လုပ်နေတဲ့အခါ ဖန်တီးနိုင်တဲ့ ပုံတွေကတော့:

![Edu4All စတတ်အပ်, အထိမ်းအမှတ်အဆောက်အအုံများအတန်း, Eiffel Tower](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.my.png)

prompt တစ်ခုက

> "နံနက်စောစောအလင်းရောင်မှာ Eiffel Tower အနားမှာ ခွေး"

## DALL-E နဲ့ Midjourney ဆိုတာ ဘာလဲ?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) နဲ့ [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) ဟာ ပုံဖန်တီးခြင်း မော်ဒယ်များအနက် အလွန်လူကြိုက်များတဲ့ မော်ဒယ်နှစ်ခုဖြစ်ပြီး prompt တွေကို အသုံးပြုပြီး ပုံများကို ဖန်တီးနိုင်ပါတယ်။

### DALL-E

DALL-E ကို စတင်လေ့လာကြရအောင်။ DALL-E ဟာ စာသားဖော်ပြချက်များမှ ပုံများကို ဖန်တီးပေးတဲ့ Generative AI မော်ဒယ်တစ်ခုဖြစ်ပါတယ်။

> [DALL-E ဟာ CLIP နဲ့ diffused attention ဆိုတဲ့ မော်ဒယ်နှစ်ခုရဲ့ ပေါင်းစပ်ဖြစ်ပါတယ်](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)။

- **CLIP** ဟာ ပုံနဲ့ စာသားတွေကနေ data ကို နံပါတ်အဖြစ် ဖော်ပြတဲ့ embeddings တွေကို ဖန်တီးပေးတဲ့ မော်ဒယ်တစ်ခုဖြစ်ပါတယ်။

- **Diffused attention** ဟာ embeddings တွေကနေ ပုံတွေကို ဖန်တီးပေးတဲ့ မော်ဒယ်တစ်ခုဖြစ်ပါတယ်။ DALL-E ကို ပုံနဲ့ စာသားတွေပါဝင်တဲ့ dataset ပေါ်မှာ လေ့ကျင့်ထားပြီး စာသားဖော်ပြချက်များမှ ပုံများကို ဖန်တီးနိုင်ပါတယ်။ ဥပမာအားဖြင့် DALL-E ကို ဦးထုပ်ဝတ်ထားတဲ့ ကြောင်တစ်ကောင်၊ mohawk ရှိတဲ့ ခွေးတစ်ကောင်ရဲ့ ပုံကို ဖန်တီးဖို့ အသုံးပြုနိုင်ပါတယ်။

### Midjourney

Midjourney ဟာ DALL-E နဲ့ ဆင်တူတဲ့ နည်းလမ်းနဲ့ အလုပ်လုပ်ပြီး စာသား prompt တွေကနေ ပုံတွေကို ဖန်တီးပေးပါတယ်။ Midjourney ကို “ဦးထုပ်ဝတ်ထားတဲ့ ကြောင်တစ်ကောင်”၊ “mohawk ရှိတဲ့ ခွေးတစ်ကောင်” စတဲ့ prompt တွေကို အသုံးပြုပြီး ပုံဖန်တီးဖို့ အသုံးပြုနိုင်ပါတယ်။

![Midjourney ဖန်တီးထားတဲ့ ပုံ, mechanical pigeon](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_ပုံအရင်းအမြစ် Wikipedia, Midjourney ဖန်တီးထားတဲ့ ပုံ_

## DALL-E နဲ့ Midjourney ဘယ်လိုအလုပ်လုပ်လဲ

ပထမဆုံး [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ရအောင်။ DALL-E ဟာ transformer architecture ကို အခြေခံထားတဲ့ Generative AI မော်ဒယ်တစ်ခုဖြစ်ပြီး _autoregressive transformer_ ပါဝင်ပါတယ်။

_autoregressive transformer_ ဟာ စာသားဖော်ပြချက်များမှ ပုံများကို ဖန်တီးပေးတဲ့ နည်းလမ်းကို သတ်မှတ်ပေးပြီး pixel တစ်ခုချင်းစီကို ဖန်တီးပေးပါတယ်။ ဖန်တီးထားတဲ့ pixel တွေကို အသုံးပြုပြီး နောက်ထပ် pixel ကို ဖန်တီးပေးပါတယ်။ ဒီလိုနဲ့ neural network ရဲ့ အလွှာများစွာကို ဖြတ်သွားပြီး ပုံကို ပြည့်စုံအောင် ဖန်တီးပေးပါတယ်။

ဒီလုပ်ငန်းစဉ်နဲ့ DALL-E ဟာ ဖန်တီးထားတဲ့ ပုံမှာ attributes, objects, characteristics စသည်တို့ကို ထိန်းချုပ်ပေးပါတယ်။ သို့သော် DALL-E 2 နဲ့ 3 ဟာ ဖန်တီးထားတဲ့ ပုံကို ပိုမိုထိန်းချုပ်နိုင်ပါတယ်။

## ပုံဖန်တီးခြင်း အက်ပလီကေးရှင်းကို ပထမဆုံးတည်ဆောက်ခြင်း

ပုံဖန်တီးခြင်း အက်ပလီကေးရှင်းတစ်ခုကို တည်ဆောက်ဖို့ ဘာတွေလိုအပ်မလဲ? အောက်ပါ libraries တွေလိုအပ်ပါတယ်:

- **python-dotenv**, သင့်ရဲ့ secrets တွေကို _.env_ ဖိုင်ထဲမှာ code ကနေ ခွဲထားဖို့ ဒီ library ကို အသုံးပြုဖို့ အကြံပြုပါတယ်။
- **openai**, OpenAI API နဲ့ ဆက်သွယ်ဖို့ ဒီ library ကို အသုံးပြုပါမယ်။
- **pillow**, Python မှာ ပုံတွေနဲ့ အလုပ်လုပ်ဖို့။
- **requests**, HTTP requests တွေကို လုပ်ဆောင်ဖို့ ကူညီပေးမယ့် library ဖြစ်ပါတယ်။

## Azure OpenAI မော်ဒယ်တစ်ခုကို ဖန်တီးပြီး deploy လုပ်ပါ

မလုပ်ဆောင်ရသေးပါက [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) စာမျက်နှာမှာ ရှိတဲ့ လမ်းညွှန်ချက်တွေကို လိုက်နာပြီး Azure OpenAI resource နဲ့ မော်ဒယ်တစ်ခုကို ဖန်တီးပါ။ မော်ဒယ်အနေနဲ့ DALL-E 3 ကို ရွေးချယ်ပါ။

## အက်ပလီကေးရှင်းကို ဖန်တီးပါ

1. _.env_ ဆိုတဲ့ ဖိုင်တစ်ခုကို အောက်ပါအတိုင်း content ဖြင့် ဖန်တီးပါ:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   ဒီအချက်အလက်တွေကို Azure OpenAI Foundry Portal ရဲ့ "Deployments" အပိုင်းမှာ သင့် resource အတွက် ရှာဖွေပါ။

1. အထက်ပါ libraries တွေကို _requirements.txt_ ဆိုတဲ့ ဖိုင်တစ်ခုထဲမှာ အောက်ပါအတိုင်း စုစည်းပါ:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. နောက်တစ်ဆင့်မှာ virtual environment တစ်ခုကို ဖန်တီးပြီး libraries တွေကို install လုပ်ပါ:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows အတွက်တော့ virtual environment ကို ဖန်တီးပြီး activate လုပ်ဖို့ အောက်ပါ command တွေကို အသုံးပြုပါ:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ ဆိုတဲ့ ဖိုင်တစ်ခုထဲမှာ အောက်ပါ code ကို ထည့်ပါ:

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

ဒီ code ကို ရှင်းပြပါမယ်:

- ပထမဆုံး OpenAI library, dotenv library, requests library, Pillow library အပါအဝင် လိုအပ်တဲ့ libraries တွေကို import လုပ်ပါတယ်။

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- နောက်တစ်ဆင့်မှာ _.env_ ဖိုင်ထဲက environment variables တွေကို load လုပ်ပါတယ်။

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- အဲဒီနောက်မှာ Azure OpenAI service client ကို configure လုပ်ပါတယ်။

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- နောက်တစ်ဆင့်မှာ ပုံကို ဖန်တီးပါတယ်:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  အထက်ပါ code ဟာ ဖန်တီးထားတဲ့ ပုံရဲ့ URL ပါဝင်တဲ့ JSON object ကို ပြန်ပေးပါတယ်။ ဒီ URL ကို အသုံးပြုပြီး ပုံကို download လုပ်ပြီး ဖိုင်အဖြစ် save လုပ်နိုင်ပါတယ်။

- နောက်ဆုံးမှာ ပုံကို ဖွင့်ပြီး standard image viewer ကို အသုံးပြုပြီး ပြသပါတယ်:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### ပုံဖန်တီးခြင်းကို ပိုမိုအသေးစိတ်ကြည့်ရှုခြင်း

ပုံကို ဖန်တီးပေးတဲ့ code ကို ပိုမိုအသေးစိတ်ကြည့်ရှုရအောင်:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt** ဟာ ပုံကို ဖန်တီးဖို့ အသုံးပြုတဲ့ စာသား prompt ဖြစ်ပါတယ်။ ဒီအခါမှာ "မြူခိုးထူထူမြေခင်းပေါ်မှာ daffodils ပေါက်နေတဲ့နေရာမှာ မြင်းပေါ်မှာ လိမ္မော်ရည်လုံးကို ကိုင်ထားတဲ့ ကြွက်" ဆိုတဲ့ prompt ကို အသုံးပြုထားပါတယ်။
- **size** ဟာ ဖန်တီးထားတဲ့ ပုံရဲ့ အရွယ်အစားဖြစ်ပါတယ်။ ဒီအခါမှာ 1024x1024 pixels ရှိတဲ့ ပုံကို ဖန်တီးထားပါတယ်။
- **n** ဟာ ဖန်တီးထားတဲ့ ပုံရဲ့ အရေအတွက်ဖြစ်ပါတယ်။ ဒီအခါမှာ ပုံနှစ်ပုံကို ဖန်တီးထားပါတယ်။
- **temperature** ဟာ Generative AI မော်ဒယ်ရဲ့ output ရဲ့ အလွတ်တန်းကို ထိန်းချုပ်ပေးတဲ့ parameter ဖြစ်ပါတယ်။ temperature ဟာ 0 နဲ့ 1 ကြားမှာရှိပြီး 0 ဆိုတာ output ဟာ deterministic ဖြစ်တယ်ဆိုလိုတာဖြစ်ပြီး 1 ဆိုတာ output ဟာ random ဖြစ်တယ်ဆိုလိုတာဖြစ်ပါတယ်။ default value က 0.7 ဖြစ်ပါတယ်။

ပုံတွေနဲ့ ဆက်လက်လုပ်ဆောင်နိုင်တဲ့ အခြားအရာတွေကို နောက်ပိုင်းအပိုင်းမှာ လေ့လာသွားပါမယ်။

## ပုံဖန်တီးခြင်းရဲ့ အပိုစွမ်းရည်များ

Python မှာ အနည်းငယ်သော code တွေကို အသုံးပြုပြီး ပုံတစ်ပုံကို ဖန်တီးနိုင်တာကို သင်တွေ့မြင်ခဲ့ပါပြီ။ သို့သော် ပုံတွေနဲ့ ဆက်လက်လုပ်ဆောင်နိုင်တဲ့ အခြားအရာတွေရှိပါတယ်။

သင်လုပ်ဆောင်နိုင်တဲ့ အခြားအရာတွေကတော့:

- **တည်းဖြတ်မှုများ ဆောင်ရွက်ခြင်း**။ ရှိပြီးသားပုံတစ်ပုံကို mask နဲ့ prompt တစ်ခုကို ပေးပြီး ပုံကို ပြောင်းလဲနိုင်ပါတယ်။ ဥပမာအားဖြင့် ပုံတစ်ပုံရဲ့ တစ်စိတ်တစ်ပိုင်းကို အရာတစ်ခုခု ထည့်သွင်းနိုင်ပါတယ်။ ဥပမာအားဖြင့် ကြွက်ပုံမှာ ဦးထုပ်တစ်လုံးကို ထည့်သွင်းနိုင်ပါတယ်။ အဲဒါကို ပုံ, mask (ပြောင်းလဲမှုအတွက် အပိုင်းကို သတ်မှတ်ပေးတဲ့ mask) နဲ့ text prompt ကို ပေးပြီး ပြုလုပ်နိုင်ပါတယ်။
> မှတ်ချက်: DALL-E 3 မှာ ဒီ feature ကို မပံ့ပိုးထားပါ။

GPT Image ကို အသုံးပြုတဲ့ ဥပမာကတော့:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  အခြေခံပုံမှာ ရေကူးကန်နဲ့ lounge ပုံသာ ပါဝင်မှာဖြစ်ပြီး နောက်ဆုံးပုံမှာ flamingo ပါဝင်မှာဖြစ်ပါတယ်:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.my.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.my.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.my.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **အမျိုးမျိုးသော မူကွဲများ ဖန်တီးခြင်း**။ ရှိပြီးသားပုံတစ်ပုံကို ယူပြီး မူကွဲများကို ဖန်တီးဖို့ တောင်းဆိုနိုင်ပါတယ်။ မူကွဲတစ်ခုကို ဖန်တီးဖို့ ပုံတစ်ပုံနဲ့ text prompt ကို ပေးပြီး အောက်ပါအတိုင်း code ကို အသုံးပြုနိုင်ပါတယ်:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > မှတ်ချက်, OpenAI မှာသာ ဒီ feature ကို ပံ့ပိုးထားပါတယ်။

## Temperature

Temperature ဟာ Generative AI မော်ဒယ်ရဲ့ output ရဲ့ အလွတ်တန်းကို ထိန်းချုပ်ပေးတဲ့ parameter ဖြစ်ပါတယ်။ Temperature ဟာ 0 နဲ့ 1 ကြားမှာရှိပြီး 0 ဆိုတာ output ဟာ deterministic ဖြစ်တယ်ဆိုလိုတာဖြစ်ပြီး 1 ဆိုတာ output ဟာ random ဖြစ်တယ်ဆိုလိုတာဖြစ်ပါတယ်။ Default value က 0.7 ဖြစ်ပါတယ်။

Temperature ဘယ်လိုအလုပ်လုပ်လဲဆိုတာကို ဥပမာတစ်ခုနဲ့ ကြည့်ရှုရအောင်:

> Prompt : "မြူခိုးထူထူမြေခင်းပေါ်မှာ daffodils ပေါက်နေတဲ့နေရာမှာ မြင်းပေါ်မှာ လိမ္မော်ရည်လုံးကို ကိုင်ထားတဲ့ ကြ
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

## အလွန်ကောင်းမွန်သောအလုပ်! သင့်ရဲ့သင်ယူမှုကို ဆက်လက်လုပ်ဆောင်ပါ

ဒီသင်ခန်းစာကိုပြီးမြောက်ပြီးနောက်မှာ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ကိုကြည့်ရှုပြီး Generative AI အကြောင်းနဲ့ပတ်သက်တဲ့ သင့်ရဲ့အသိပညာကို ဆက်လက်မြှင့်တင်ပါ!

Lesson 10 ကိုသွားပြီး [low-code နဲ့ AI applications တည်ဆောက်ခြင်း](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) အကြောင်းကိုလေ့လာကြမယ်!

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြု၍ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားယူမှုမှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။