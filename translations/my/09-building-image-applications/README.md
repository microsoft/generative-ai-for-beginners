<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "238cde5c90363d70ecc939569378da51",
  "translation_date": "2025-10-18T02:01:02+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "my"
}
-->
# ပုံဖန်တီးမှုအက်ပလီကေးရှင်းများ တည်ဆောက်ခြင်း

[![ပုံဖန်တီးမှုအက်ပလီကေးရှင်းများ တည်ဆောက်ခြင်း](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.my.png)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLMs တွေဟာ စာသားဖန်တီးမှုထက်ပိုပြီး အသုံးဝင်ပါတယ်။ စာသားဖော်ပြချက်တွေကနေ ပုံတွေကိုလည်း ဖန်တီးနိုင်ပါတယ်။ ပုံတွေကို modality အနေနဲ့ အသုံးပြုခြင်းဟာ MedTech, အိမ်ဆောက်လုပ်ရေး, ခရီးသွားလုပ်ငန်း, ဂိမ်းဖွံ့ဖြိုးရေးနဲ့ အခြားသော နေရာများစွာမှာ အလွန်အသုံးဝင်ပါတယ်။ ဒီအခန်းမှာတော့ DALL-E နဲ့ Midjourney ဆိုတဲ့ ပုံဖန်တီးမှုမော်ဒယ်တွေကို လေ့လာကြမယ်။

## အကျဉ်းချုပ်

ဒီသင်ခန်းစာမှာ ကျွန်တော်တို့ လေ့လာမယ့်အရာတွေကတော့ -

- ပုံဖန်တီးမှုနဲ့ အဘယ်ကြောင့် အရေးကြီးသလဲ။
- DALL-E နဲ့ Midjourney, အဲဒါတွေက ဘာလဲ၊ ဘယ်လိုအလုပ်လုပ်လဲ။
- ပုံဖန်တီးမှုအက်ပလီကေးရှင်းတစ်ခုကို ဘယ်လိုတည်ဆောက်မလဲ။

## သင်ယူရမယ့်ရည်မှန်းချက်များ

ဒီသင်ခန်းစာကို ပြီးမြောက်ပြီးနောက်မှာ သင်တစ်ဦးက -

- ပုံဖန်တီးမှုအက်ပလီကေးရှင်းတစ်ခုကို တည်ဆောက်နိုင်မယ်။
- meta prompts တွေကို အသုံးပြုပြီး သင့်အက်ပလီကေးရှင်းအတွက် အကန့်အသတ်တွေ သတ်မှတ်နိုင်မယ်။
- DALL-E နဲ့ Midjourney ကို အသုံးပြုနိုင်မယ်။

## အဘယ်ကြောင့် ပုံဖန်တီးမှုအက်ပလီကေးရှင်းတစ်ခုကို တည်ဆောက်သင့်သလဲ?

ပုံဖန်တီးမှုအက်ပလီကေးရှင်းတွေဟာ Generative AI ရဲ့ စွမ်းရည်တွေကို စူးစမ်းဖို့ အကောင်းဆုံးနည်းလမ်းတစ်ခုဖြစ်ပါတယ်။ အဲဒါတွေကို အောက်ပါအတိုင်း အသုံးပြုနိုင်ပါတယ် -

- **ပုံတည်းဖြတ်ခြင်းနဲ့ ပုံပေါင်းစပ်ခြင်း**။ ပုံတည်းဖြတ်ခြင်းနဲ့ ပုံပေါင်းစပ်ခြင်းလို အမျိုးမျိုးသော အသုံးအဆောင်များအတွက် ပုံတွေကို ဖန်တီးနိုင်ပါတယ်။

- **စက်မှုလုပ်ငန်းအမျိုးမျိုးမှာ အသုံးချနိုင်ခြင်း**။ MedTech, ခရီးသွားလုပ်ငန်း, ဂိမ်းဖွံ့ဖြိုးရေးနဲ့ အခြားသော စက်မှုလုပ်ငန်းအမျိုးမျိုးအတွက် ပုံတွေကို ဖန်တီးနိုင်ပါတယ်။

## အခြေအနေ - Edu4All

ဒီသင်ခန်းစာရဲ့ အစိတ်အပိုင်းတစ်ခုအနေနဲ့ ကျွန်တော်တို့ရဲ့ စတတ်အပ်ဖြစ်တဲ့ Edu4All နဲ့ ဆက်လက်လုပ်ဆောင်သွားမှာဖြစ်ပါတယ်။ ကျောင်းသားတွေဟာ သူတို့ရဲ့ အကဲဖြတ်မှုအတွက် ပုံတွေကို ဖန်တီးမှာဖြစ်ပြီး၊ ဘယ်လိုပုံတွေဖန်တီးမယ်ဆိုတာ ကျောင်းသားတွေကို အပ်နှံထားပါတယ်။ သူတို့ရဲ့ fairytale အတွက် ပုံတွေဖန်တီးတာဖြစ်စေ၊ သူတို့ရဲ့ ဇာတ်လမ်းအတွက် ဇာတ်ကောင်အသစ်တစ်ခု ဖန်တီးတာဖြစ်စေ၊ သူတို့ရဲ့ အကြံဉာဏ်နဲ့ အယူအဆတွေကို ရှင်းလင်းဖော်ပြဖို့ အကူအညီပေးတာဖြစ်စေ၊ သူတို့ကိုယ်တိုင် ဆုံးဖြတ်နိုင်ပါတယ်။

ဥပမာအားဖြင့် Edu4All ရဲ့ ကျောင်းသားတွေဟာ အတန်းထဲမှာ အထိမ်းအမှတ်တွေကို လေ့လာနေကြတယ်ဆိုရင် -

![Edu4All စတတ်အပ်၊ အထိမ်းအမှတ်အတန်း၊ Eiffel Tower](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.my.png)

ဒီလို prompt တစ်ခုကို အသုံးပြုနိုင်ပါတယ် -

> "နံနက်စောစောအလင်းရောင်မှာ Eiffel Tower အနားမှာ ခွေး"

## DALL-E နဲ့ Midjourney ဆိုတာဘာလဲ?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) နဲ့ [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) ဟာ ပုံဖန်တီးမှုမော်ဒယ်တွေထဲမှာ အလွန်လူကြိုက်များတဲ့ မော်ဒယ်နှစ်ခုဖြစ်ပြီး၊ prompt တွေကို အသုံးပြုပြီး ပုံတွေကို ဖန်တီးနိုင်ပါတယ်။

### DALL-E

DALL-E ကို စတင်လေ့လာကြရအောင်။ DALL-E ဟာ Generative AI မော်ဒယ်တစ်ခုဖြစ်ပြီး စာသားဖော်ပြချက်တွေကနေ ပုံတွေကို ဖန်တီးပါတယ်။

> [DALL-E ဟာ CLIP နဲ့ diffused attention ဆိုတဲ့ မော်ဒယ်နှစ်ခုရဲ့ ပေါင်းစပ်မှုဖြစ်ပါတယ်](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)။

- **CLIP** ဟာ ပုံနဲ့ စာသားတွေကနေ data တွေကို နံပါတ်ပုံစံအဖြစ် ဖန်တီးပေးတဲ့ မော်ဒယ်တစ်ခုဖြစ်ပါတယ်။

- **Diffused attention** ဟာ embeddings တွေကနေ ပုံတွေကို ဖန်တီးပေးတဲ့ မော်ဒယ်တစ်ခုဖြစ်ပါတယ်။ DALL-E ဟာ ပုံနဲ့ စာသား dataset တွေကို သင်ကြားထားပြီး စာသားဖော်ပြချက်တွေကနေ ပုံတွေကို ဖန်တီးနိုင်ပါတယ်။ ဥပမာအားဖြင့် DALL-E ကို ဦးထုပ်ဝတ်ထားတဲ့ ကြောင်တစ်ကောင်၊ ဒါမှမဟုတ် mohawk ရှိတဲ့ ခွေးတစ်ကောင်ရဲ့ ပုံတွေကို ဖန်တီးဖို့ အသုံးပြုနိုင်ပါတယ်။

### Midjourney

Midjourney ဟာ DALL-E နဲ့ တူညီတဲ့နည်းလမ်းနဲ့ အလုပ်လုပ်ပြီး စာသား prompt တွေကနေ ပုံတွေကို ဖန်တီးပါတယ်။ Midjourney ကိုလည်း “ဦးထုပ်ဝတ်ထားတဲ့ ကြောင်တစ်ကောင်” ဒါမှမဟုတ် “mohawk ရှိတဲ့ ခွေးတစ်ကောင်” ဆိုတဲ့ prompt တွေကို အသုံးပြုပြီး ပုံတွေ ဖန်တီးနိုင်ပါတယ်။

![Midjourney ဖန်တီးထားတဲ့ ပုံ၊ mechanical pigeon](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_ပုံအခွင့်အရေး Wikipedia, Midjourney ဖန်တီးထားတဲ့ ပုံ_

## DALL-E နဲ့ Midjourney ဘယ်လိုအလုပ်လုပ်သလဲ

ပထမဆုံး [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst) ကို ကြည့်ပါ။ DALL-E ဟာ transformer architecture အပေါ်မှာ အခြေခံထားတဲ့ Generative AI မော်ဒယ်ဖြစ်ပြီး _autoregressive transformer_ ပါရှိပါတယ်။

_autoregressive transformer_ ဟာ မော်ဒယ်တစ်ခုက စာသားဖော်ပြချက်တွေကနေ ပုံတွေကို ဘယ်လိုဖန်တီးမလဲဆိုတာ သတ်မှတ်ပေးပြီး pixel တစ်ခုချင်းစီကို ဖန်တီးပါတယ်။ ဖန်တီးထားတဲ့ pixel တွေကို အသုံးပြုပြီး နောက် pixel ကို ဖန်တီးပါတယ်။ neural network ရဲ့ အလွှာများစွာကို ဖြတ်သွားပြီး ပုံကို ပြည့်စုံအောင် ဖန်တီးပါတယ်။

ဒီလုပ်ငန်းစဉ်နဲ့ DALL-E ဟာ ဖန်တီးထားတဲ့ ပုံထဲမှာ attribute, object, characteristic တွေကို ထိန်းချုပ်ပါတယ်။ သို့သော် DALL-E 2 နဲ့ 3 ဟာ ဖန်တီးထားတဲ့ ပုံကို ပိုမိုထိန်းချုပ်နိုင်ပါတယ်။

## ပုံဖန်တီးမှုအက်ပလီကေးရှင်းကို ပထမဆုံးတည်ဆောက်ခြင်း

ပုံဖန်တီးမှုအက်ပလီကေးရှင်းတစ်ခုကို တည်ဆောက်ဖို့ ဘာတွေလိုအပ်သလဲဆိုရင် အောက်ပါ library တွေလိုအပ်ပါတယ် -

- **python-dotenv**, သင့်ရဲ့ secrets တွေကို _.env_ ဖိုင်ထဲမှာ code ကနေ ခွဲထားဖို့ ဒီ library ကို အသုံးပြုဖို့ အကြံပြုပါတယ်။
- **openai**, ဒီ library ဟာ OpenAI API နဲ့ ဆက်သွယ်ဖို့ အသုံးပြုမယ့် library ဖြစ်ပါတယ်။
- **pillow**, Python မှာ ပုံတွေနဲ့ အလုပ်လုပ်ဖို့။
- **requests**, HTTP requests တွေကို လုပ်ဆောင်ဖို့ အကူအညီပေးပါတယ်။

## Azure OpenAI မော်ဒယ်တစ်ခုကို ဖန်တီးပြီး deploy လုပ်ခြင်း

မလုပ်ဆောင်ရသေးပါက [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) စာမျက်နှာမှာ လမ်းညွှန်ချက်တွေကို လိုက်နာပြီး Azure OpenAI resource နဲ့ မော်ဒယ်တစ်ခုကို ဖန်တီးပါ။ မော်ဒယ်အဖြစ် DALL-E 3 ကို ရွေးချယ်ပါ။

## အက်ပလီကေးရှင်းကို ဖန်တီးခြင်း

1. _.env_ ဆိုတဲ့ ဖိုင်တစ်ခုကို အောက်ပါအကြောင်းအရာနဲ့ ဖန်တီးပါ -

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   ဒီအချက်အလက်တွေကို Azure OpenAI Foundry Portal မှာ သင့်ရဲ့ resource ရဲ့ "Deployments" အပိုင်းမှာ ရှာပါ။

1. အထက်ပါ library တွေကို _requirements.txt_ ဆိုတဲ့ ဖိုင်တစ်ခုထဲမှာ စုစည်းပါ -

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. နောက်တစ်ဆင့်မှာ virtual environment ကို ဖန်တီးပြီး library တွေကို install လုပ်ပါ -

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows အတွက်တော့ virtual environment ကို ဖန်တီးပြီး activate လုပ်ဖို့ အောက်ပါ command တွေကို အသုံးပြုပါ -

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ ဆိုတဲ့ ဖိုင်ထဲမှာ အောက်ပါ code ကို ထည့်ပါ -

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

ဒီ code ကို ရှင်းပြပါ -

- ပထမဆုံး OpenAI library, dotenv library, requests library, Pillow library အပါအဝင် လိုအပ်တဲ့ library တွေကို import လုပ်ပါတယ်။

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- နောက်တစ်ဆင့် _.env_ ဖိုင်က environment variables တွေကို load လုပ်ပါတယ်။

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

- နောက်တစ်ဆင့်မှာ ပုံကို ဖန်တီးပါတယ် -

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  အထက်ပါ code ဟာ ဖန်တီးထားတဲ့ ပုံရဲ့ URL ပါဝင်တဲ့ JSON object ကို ပြန်လည်တုံ့ပြန်ပါတယ်။ ဒီ URL ကို အသုံးပြုပြီး ပုံကို download လုပ်ပြီး ဖိုင်အဖြစ် သိမ်းဆည်းနိုင်ပါတယ်။

- နောက်ဆုံးမှာ ပုံကို ဖွင့်ပြီး standard image viewer ကို အသုံးပြုပြီး ပြသပါတယ် -

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### ပုံကို ဖန်တီးခြင်းအကြောင်း အခြေခံအချက်များ

ပုံကို ဖန်တီးတဲ့ code ကို ပိုမိုအသေးစိတ်ကြည့်ရအောင် -

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt** ဟာ ပုံကို ဖန်တီးဖို့ အသုံးပြုတဲ့ စာသား prompt ဖြစ်ပါတယ်။ ဒီအခါမှာ "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils" ဆိုတဲ့ prompt ကို အသုံးပြုထားပါတယ်။
- **size** ဟာ ဖန်တီးထားတဲ့ ပုံရဲ့ အရွယ်အစားဖြစ်ပါတယ်။ ဒီအခါမှာ 1024x1024 pixels အရွယ်အစားရှိတဲ့ ပုံကို ဖန်တီးထားပါတယ်။
- **n** ဟာ ဖန်တီးထားတဲ့ ပုံအရေအတွက်ဖြစ်ပါတယ်။ ဒီအခါမှာ ပုံနှစ်ပုံကို ဖန်တီးထားပါတယ်။
- **temperature** ဟာ Generative AI မော်ဒယ်ရဲ့ output ရဲ့ random ဖြစ်မှုကို ထိန်းချုပ်တဲ့ parameter ဖြစ်ပါတယ်။ temperature ဟာ 0 နဲ့ 1 ကြားမှာရှိပြီး 0 ဆိုတာ output ဟာ deterministic ဖြစ်တယ်ဆိုတာကို ဆိုလိုပါတယ်။ 1 ဆိုတာ output ဟာ random ဖြစ်တယ်ဆိုတာကို ဆိုလိုပါတယ်။ default value က 0.7 ဖြစ်ပါတယ်။

ပုံတွေနဲ့ ပိုပြီးလုပ်ဆောင်နိုင်တဲ့ အရာတွေကို နောက်အပိုင်းမှာ ဆက်လက်လေ့လာပါမယ်။

## ပုံဖန်တီးမှုရဲ့ ထပ်ဆင့်စွမ်းရည်များ

Python မှာ အကြောင်းအရာအနည်းငယ်နဲ့ ပုံတစ်ပုံကို ဖန်တီးနိုင်တာကို သင်တွေ့မြင်ခဲ့ပါပြီ။ သို့သော် ပုံတွေနဲ့ ပိုပြီးလုပ်ဆောင်နိုင်တဲ့ အရာတွေရှိပါတယ်။

သင်လုပ်ဆောင်နိုင်တဲ့ အခြားအရာတွေကတော့ -

- **တည်းဖြတ်မှုများလုပ်ဆောင်ခြင်း**။ ရှိပြီးသားပုံတစ်ပုံကို mask နဲ့ prompt တစ်ခုကို ပေးပြီး ပုံကို ပြောင်းလဲနိုင်ပါတယ်။ ဥပမာအားဖြင့် ပုံတစ်ပုံရဲ့ တစ်စိတ်တစ်ပိုင်းကို အရာတစ်ခုခု ထည့်သွင်းနိုင်ပါတယ်။ ဥပမာအားဖြင့် ကျွန်တော်တို့ Bunny ပုံမှာ Bunny ကို ဦးထုပ်တစ်လုံး ထည့်သွင်းနိုင်ပါတယ်။ အဲဒါကို ပုံ, mask (ပြောင်းလဲမှုအတွက် အပိုင်းကို သတ်မှတ်ခြင်း) နဲ့ ဘာလုပ်ဆောင်သင့်တယ်ဆိုတာကို ပြောတဲ့ စာသား prompt တစ်ခုကို ပေးပြီး လုပ်ဆောင်နိုင်ပါတယ်။
> မှတ်ချက် - ဒီ feature ဟာ DALL-E 3 မှာ မပံ့ပိုးထားပါဘူး။

GPT Image ကို အသုံးပြုတဲ့ ဥပမာကတော့ -

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  အခြေခံပုံဟာ lounge နဲ့ pool ကိုသာ ပါဝင်မှာဖြစ်ပြီး နောက်ဆုံးပုံမှာ flamingo ပါဝင်မှာဖြစ်ပါတယ် -

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.my.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.my.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.my.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **အမျိုးမျိုးသောပုံတွေ ဖန်တီးခြင်း**။ အဓိကအကြောင်းအရာက ရှိပြီးသားပုံတစ်ပုံကို ယူပြီး အမျိုးမျိုးသော variation တွေကို ဖန်တီးဖို့ တောင်းဆိုတာဖြစ်ပါတယ်။ variation တစ်ခုကို ဖန်တီးဖို့ ပုံတစ်ပုံနဲ့ စာသား prompt တစ်ခုကို ပေးပြီး အောက်ပါ code ကို အသုံးပြုနိုင်ပါတယ် -

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > မှတ်ချက် - ဒီ feature ဟာ OpenAI မှာသာ ပံ့ပိုးထားပါတယ်။

## Temperature

Temperature ဟာ Generative AI မော်ဒယ်ရဲ့ output ရဲ့ random ဖြစ်မှုကို ထိန်းချုပ်တဲ့ parameter ဖြစ်ပါတယ်။ Temperature ဟာ 0 နဲ့ 1 ကြားမှာရှိပြီး 0 ဆိုတာ output ဟာ deterministic ဖြစ်တယ်ဆိုတာကို ဆိုလိုပါတယ်။ 1 ဆိုတာ output ဟာ random ဖြစ်တယ်ဆိုတာကို ဆိုလိုပါတယ်။ Default value က 0.7 ဖြစ်ပါတယ်။

Temperature ဘယ်လိုအလုပ်လုပ်လဲဆိုတာကို ဥပမာတစ်ခုနဲ့ ကြည့်ရအောင် -

> Prompt : "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![Bunny on a horse holding a lollipop, version 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.my.png)

အဲဒီ prompt ကို ထပ်ပြီး run လုပ်ကြည့်ရင် ပုံတစ်ပုံတည်းကို မရနိုင်ဘဲ -

![Generated image of bunny on horse](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.my.png)

သင်မြ
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

ဒီသင်ခန်းစာကိုပြီးမြောက်ပြီးနောက်မှာ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ကိုကြည့်ရှုပြီး Generative AI အသိပညာကို ဆက်လက်မြှင့်တင်ပါ!

Lesson 10 ကိုသွားပြီး [low-code ဖြင့် AI applications တည်ဆောက်ခြင်း](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) ကိုလေ့လာကြမယ်!

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။