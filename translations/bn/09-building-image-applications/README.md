<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef74ad58fc01f7ad80788f79505f9816",
  "translation_date": "2025-08-26T15:40:44+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "bn"
}
-->
# ইমেজ জেনারেশন অ্যাপ্লিকেশন তৈরি

[![ইমেজ জেনারেশন অ্যাপ্লিকেশন তৈরি](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.bn.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM-এ শুধু টেক্সট জেনারেশনই নয়, টেক্সট বর্ণনা থেকে ছবি তৈরি করাও সম্ভব। ছবি একটি গুরুত্বপূর্ণ মাধ্যম, যা মেডটেক, স্থাপত্য, পর্যটন, গেম ডেভেলপমেন্টসহ নানা ক্ষেত্রে কাজে লাগে। এই অধ্যায়ে আমরা দুটি জনপ্রিয় ইমেজ জেনারেশন মডেল, DALL-E এবং Midjourney নিয়ে আলোচনা করব।

## পরিচিতি

এই পাঠে আপনি শিখবেন:

- ইমেজ জেনারেশন কী এবং কেন এটি দরকার।
- DALL-E এবং Midjourney কী, এবং কীভাবে কাজ করে।
- কীভাবে একটি ইমেজ জেনারেশন অ্যাপ তৈরি করবেন।

## শেখার লক্ষ্য

এই পাঠ শেষে আপনি পারবেন:

- একটি ইমেজ জেনারেশন অ্যাপ তৈরি করতে।
- মেটাপ্রম্পট দিয়ে অ্যাপের সীমা নির্ধারণ করতে।
- DALL-E এবং Midjourney ব্যবহার করতে।

## কেন ইমেজ জেনারেশন অ্যাপ তৈরি করবেন?

ইমেজ জেনারেশন অ্যাপ্লিকেশন জেনারেটিভ AI-এর ক্ষমতা অন্বেষণের দারুণ উপায়। এগুলো ব্যবহার করা যায়, যেমন:

- **ইমেজ এডিটিং ও সিন্থেসিস**। বিভিন্ন কাজে ছবি তৈরি ও সম্পাদনা করা যায়।

- **বিভিন্ন শিল্পে প্রয়োগ**। মেডটেক, পর্যটন, গেম ডেভেলপমেন্টসহ নানা শিল্পে ছবি তৈরি করা যায়।

## দৃশ্যপট: Edu4All

এই পাঠে আমরা আমাদের স্টার্টআপ Edu4All নিয়ে কাজ চালিয়ে যাব। শিক্ষার্থীরা তাদের মূল্যায়নের জন্য ছবি তৈরি করবে, কী ছবি হবে তা তাদের ওপর নির্ভর করবে—তারা চাইলে নিজের রূপকথার জন্য ইলাস্ট্রেশন, নতুন চরিত্র, বা তাদের ধারণা ও কনসেপ্ট দৃশ্যায়ন করতে পারে।

যেমন, Edu4All-এর শিক্ষার্থীরা যদি ক্লাসে মনুমেন্ট নিয়ে কাজ করে, তারা এমন ছবি তৈরি করতে পারে:

![Edu4All স্টার্টআপ, মনুমেন্ট ক্লাস, আইফেল টাওয়ার](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.bn.png)

এমন একটি প্রম্পট ব্যবহার করে

> "Dog next to Eiffel Tower in early morning sunlight"

## DALL-E এবং Midjourney কী?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) এবং [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) দুটি জনপ্রিয় ইমেজ জেনারেশন মডেল, যেখানে প্রম্পট দিয়ে ছবি তৈরি করা যায়।

### DALL-E

DALL-E হলো একটি জেনারেটিভ AI মডেল, যা টেক্সট বর্ণনা থেকে ছবি তৈরি করে।

> [DALL-E দুটি মডেলের সংমিশ্রণ—CLIP এবং diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)।

- **CLIP** হলো একটি মডেল, যা ছবি ও টেক্সট থেকে এম্বেডিং তৈরি করে, অর্থাৎ ডেটার সংখ্যাগত উপস্থাপন।

- **Diffused attention** হলো একটি মডেল, যা এম্বেডিং থেকে ছবি তৈরি করে। DALL-E ছবি ও টেক্সটের ডেটাসেটে প্রশিক্ষিত এবং টেক্সট বর্ণনা থেকে ছবি তৈরি করতে পারে। যেমন, DALL-E দিয়ে টুপি পরা বিড়াল বা মোহকসহ কুকুরের ছবি তৈরি করা যায়।

### Midjourney

Midjourney-ও DALL-E-এর মতোই টেক্সট প্রম্পট থেকে ছবি তৈরি করে। Midjourney-তে "a cat in a hat" বা "dog with a mohawk" টাইপের প্রম্পট দিয়েও ছবি বানানো যায়।

![Midjourney দিয়ে তৈরি ছবি, যান্ত্রিক কবুতর](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_ছবির উৎস: উইকিপিডিয়া, Midjourney দিয়ে তৈরি_

## DALL-E এবং Midjourney কীভাবে কাজ করে

প্রথমে, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)। DALL-E হলো ট্রান্সফর্মার আর্কিটেকচারের ওপর ভিত্তি করে তৈরি একটি জেনারেটিভ AI মডেল, যেখানে _autoregressive transformer_ ব্যবহৃত হয়।

_autoregressive transformer_ ঠিক করে কীভাবে মডেল টেক্সট বর্ণনা থেকে ছবি তৈরি করবে—একবারে একটি পিক্সেল তৈরি করে, তারপর সেই পিক্সেল ব্যবহার করে পরবর্তী পিক্সেল তৈরি করে। নিউরাল নেটওয়ার্কের একাধিক স্তর পেরিয়ে, ছবিটি সম্পূর্ণ হয়।

এইভাবে DALL-E ছবিতে বিভিন্ন বৈশিষ্ট্য, বস্তু, চরিত্র ইত্যাদি নিয়ন্ত্রণ করতে পারে। তবে DALL-E 2 এবং 3-এ ছবির ওপর আরও বেশি নিয়ন্ত্রণ পাওয়া যায়।

## প্রথম ইমেজ জেনারেশন অ্যাপ তৈরি

ইমেজ জেনারেশন অ্যাপ তৈরি করতে কী লাগে? নিচের লাইব্রেরিগুলো দরকার:

- **python-dotenv**—গোপন তথ্য _.env_ ফাইলে রাখতে এই লাইব্রেরি ব্যবহার করা ভালো।
- **openai**—OpenAI API-র সাথে কাজ করতে এই লাইব্রেরি লাগবে।
- **pillow**—Python-এ ছবি নিয়ে কাজ করতে।
- **requests**—HTTP অনুরোধ পাঠাতে।

## Azure OpenAI মডেল তৈরি ও ডিপ্লয় করুন

যদি আগে না করে থাকেন, [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) পেজের নির্দেশনা অনুসরণ করুন
Azure OpenAI রিসোর্স ও মডেল তৈরি করতে। মডেল হিসেবে DALL-E 3 নির্বাচন করুন।  

## অ্যাপ তৈরি করুন

১. _.env_ নামে একটি ফাইল তৈরি করুন, নিচের কনটেন্ট দিয়ে:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Azure OpenAI Foundry Portal-এ আপনার রিসোর্সের "Deployments" সেকশনে এই তথ্য পাবেন।

২. উপরের লাইব্রেরিগুলো _requirements.txt_ ফাইলে লিখুন:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

৩. এরপর ভার্চুয়াল এনভায়রনমেন্ট তৈরি করে লাইব্রেরিগুলো ইনস্টল করুন:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows-এ ভার্চুয়াল এনভায়রনমেন্ট তৈরি ও অ্যাক্টিভেট করতে নিচের কমান্ড ব্যবহার করুন:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

৪. _app.py_ নামে ফাইলে নিচের কোড লিখুন:

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

এই কোড ব্যাখ্যা করা যাক:

- প্রথমে প্রয়োজনীয় লাইব্রেরি ইম্পোর্ট করি, যেমন OpenAI, dotenv, requests, Pillow।

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- এরপর _.env_ ফাইল থেকে এনভায়রনমেন্ট ভ্যারিয়েবল লোড করি।

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- তারপর Azure OpenAI সার্ভিস ক্লায়েন্ট কনফিগার করি 

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- এরপর ছবি তৈরি করি:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  উপরের কোডে একটি JSON অবজেক্ট পাওয়া যায়, যেখানে তৈরি ছবির URL থাকে। এই URL ব্যবহার করে ছবি ডাউনলোড করে ফাইলে সংরক্ষণ করা যায়।

- শেষে, ছবি ওপেন করে স্ট্যান্ডার্ড ইমেজ ভিউয়ারে দেখাই:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### ছবি তৈরির আরও বিস্তারিত

ছবি তৈরির কোডটা একটু বিস্তারিতভাবে দেখা যাক:

    ```python
      generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                            )
    ```

- **prompt**—ছবি তৈরির জন্য টেক্সট প্রম্পট। এখানে "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils" ব্যবহার করা হয়েছে।
- **size**—তৈরি ছবির সাইজ। এখানে 1024x1024 পিক্সেল।
- **n**—কয়টি ছবি তৈরি হবে। এখানে দুটি ছবি।
- **temperature**—জেনারেটিভ AI মডেলের আউটপুটে কতটা র‍্যান্ডমনেস থাকবে তা নিয়ন্ত্রণ করে। মান ০ থেকে ১, যেখানে ০ মানে নির্ধারিত আউটপুট, ১ মানে র‍্যান্ডম। ডিফল্ট ০.৭।

ছবি নিয়ে আরও অনেক কিছু করা যায়, যা পরবর্তী অংশে আলোচনা করা হবে।

## ইমেজ জেনারেশনের অতিরিক্ত ক্ষমতা

এখন পর্যন্ত দেখেছেন, কয়েক লাইনে Python কোডে ছবি তৈরি করা যায়। তবে আরও কিছু কাজ করা যায়।

এগুলোও করা যায়:

- **এডিট করা**। বিদ্যমান ছবিতে মাস্ক ও প্রম্পট দিয়ে ছবি পরিবর্তন করা যায়। যেমন, কোনো ছবির অংশে কিছু যোগ করা। ধরুন, আমাদের বানির ছবিতে একটি টুপি যোগ করতে চাই। এজন্য ছবি, মাস্ক (যে অংশে পরিবর্তন হবে) এবং টেক্সট প্রম্পট দিতে হয়।
> Note: DALL-E 3-এ এটি সাপোর্টেড নয়। 
 
এখানে GPT Image ব্যবহার করে একটি উদাহরণ:

    ```python
    response = client.images.edit(
        model="gpt-image-1",
        image=open("sunlit_lounge.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo"
    )
    image_url = response.data[0].url
    ```

  বেস ছবিতে শুধু লাউঞ্জ ও পুল থাকবে, কিন্তু চূড়ান্ত ছবিতে ফ্লেমিংগো যোগ হবে:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="./images/sunlit_lounge.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/mask.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/sunlit_lounge_result.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **ভ্যারিয়েশন তৈরি**। বিদ্যমান ছবি থেকে ভিন্ন ভিন্ন সংস্করণ তৈরি করা যায়। এজন্য ছবি ও টেক্সট প্রম্পট দিয়ে নিচের মতো কোড লিখতে হয়:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Note, এটি শুধু OpenAI-তে সাপোর্টেড

## Temperature

Temperature হলো একটি প্যারামিটার, যা জেনারেটিভ AI মডেলের আউটপুটে কতটা র‍্যান্ডমনেস থাকবে তা নিয়ন্ত্রণ করে। মান ০ থেকে ১, যেখানে ০ মানে নির্ধারিত আউটপুট, ১ মানে র‍্যান্ডম। ডিফল্ট মান ০.৭।

Temperature কীভাবে কাজ করে, একটি উদাহরণ দেখা যাক—একই প্রম্পট দুইবার চালিয়ে:

> Prompt : "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![Bunny on a horse holding a lollipop, version 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.bn.png)

এবার একই প্রম্পট আবার চালিয়ে দেখুন, একই ছবি পাবেন না:

![Generated image of bunny on horse](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.bn.png)

দেখা যাচ্ছে, ছবি দুটো মিল আছে, কিন্তু এক নয়। এবার temperature মান ০.১ করে দেখি কী হয়:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Temperature পরিবর্তন

এবার চেষ্টা করি আউটপুট আরও নির্ধারিত করতে। আগের দুটি ছবিতে দেখা গেল, একটিতে বানি, অন্যটিতে ঘোড়া—ছবির পার্থক্য বেশি।

তাই কোডে temperature ০ করে দিই:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

এবার কোড চালালে দুটি ছবি পাবেন:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.bn.png)
- ![Temperature 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.bn.png)

এখানে স্পষ্টভাবে দেখা যায়, ছবিগুলো আরও বেশি মিলছে।

## মেটাপ্রম্পট দিয়ে অ্যাপের সীমা নির্ধারণ

আমাদের ডেমোতে ক্লায়েন্টদের জন্য ছবি তৈরি করা যাচ্ছে। তবে অ্যাপের জন্য কিছু সীমা নির্ধারণ করা দরকার।

যেমন, আমরা চাই না এমন ছবি তৈরি হোক, যা কর্মক্ষেত্রে নিরাপদ নয় বা শিশুদের জন্য অনুপযুক্ত।

এটা করা যায় _মেটাপ্রম্পট_ দিয়ে। মেটাপ্রম্পট হলো টেক্সট প্রম্পট, যা জেনারেটিভ AI মডেলের আউটপুট নিয়ন্ত্রণে ব্যবহৃত হয়। যেমন, মেটাপ্রম্পট দিয়ে নিশ্চিত করা যায়, তৈরি ছবি কর্মক্ষেত্রে নিরাপদ বা শিশুদের জন্য উপযুক্ত।

### কীভাবে কাজ করে?

তাহলে, মেটাপ্রম্পট কীভাবে কাজ করে?

মেটাপ্রম্পট হলো টেক্সট প্রম্পট, যা মডেলের আউটপুট নিয়ন্ত্রণে ব্যবহৃত হয়। এগুলো মূল প্রম্পটের আগে দেওয়া হয় এবং অ্যাপ্লিকেশনে এম্বেড করা হয়, যাতে মডেলের আউটপুট নিয়ন্ত্রণ করা যায়। মূল প্রম্পট ও মেটাপ্রম্পট একসাথে একটি টেক্সট প্রম্পটে দেওয়া হয়।

মেটাপ্রম্পটের একটি উদাহরণ:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

এবার দেখি, ডেমোতে কীভাবে মেটাপ্রম্পট ব্যবহার করা যায়।

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

উপরের প্রম্পট থেকে দেখা যায়, সব ছবি তৈরিতে মেটাপ্রম্পট বিবেচনা করা হচ্ছে।

## অ্যাসাইনমেন্ট - শিক্ষার্থীদের সক্রিয় করুন

পাঠের শুরুতে Edu4All পরিচয় করিয়ে দেওয়া হয়েছিল। এবার শিক্ষার্থীদের তাদের মূল্যায়নের জন্য ছবি তৈরি করতে দিন।

শিক্ষার্থীরা তাদের মূল্যায়নে মনুমেন্টের ছবি তৈরি করবে, কোন মনুমেন্ট হবে তা তাদের ইচ্ছা। শিক্ষার্থীদের বলা হবে, তারা যেন সৃজনশীলভাবে এই মনুমেন্টগুলো বিভিন্ন প্রেক্ষাপটে উপস্থাপন করে।

## সমাধান

এখানে একটি সম্ভাব্য সমাধান দেওয়া হলো:

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

## দারুণ কাজ! আরও শিখতে থাকুন
এই পাঠটি শেষ করার পর, আমাদের [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) দেখে নিতে ভুলবেন না, যাতে আপনি আপনার Generative AI জ্ঞানের স্তর আরও বাড়াতে পারেন!

এবার চলুন যাই পাঠ ১০-এ, যেখানে আমরা দেখব কীভাবে [লো-কোড দিয়ে AI অ্যাপ্লিকেশন তৈরি করা যায়](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**দায়িত্ব পরিত্যাগের ঘোষণা**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য নির্ভুলতা বজায় রাখার চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হবে। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হচ্ছে। এই অনুবাদের ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।