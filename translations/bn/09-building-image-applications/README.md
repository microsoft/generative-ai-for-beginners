<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a7fd0f95f9eb673b79da47c0814f4d4",
  "translation_date": "2025-07-09T13:20:36+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "bn"
}
-->
# ইমেজ জেনারেশন অ্যাপ্লিকেশন তৈরি করা

[![ইমেজ জেনারেশন অ্যাপ্লিকেশন তৈরি করা](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.bn.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLM শুধুমাত্র টেক্সট জেনারেশনের জন্য নয়। টেক্সট বর্ণনা থেকে ছবি তৈরি করাও সম্ভব। ছবি একটি মাধ্যম হিসেবে বিভিন্ন ক্ষেত্রে যেমন মেডটেক, আর্কিটেকচার, পর্যটন, গেম ডেভেলপমেন্ট ইত্যাদিতে খুবই উপকারী হতে পারে। এই অধ্যায়ে, আমরা দুটি জনপ্রিয় ইমেজ জেনারেশন মডেল, DALL-E এবং Midjourney সম্পর্কে জানব।

## পরিচিতি

এই পাঠে আমরা আলোচনা করব:

- ইমেজ জেনারেশন এবং কেন এটি গুরুত্বপূর্ণ।
- DALL-E এবং Midjourney কী, এবং কীভাবে কাজ করে।
- কিভাবে একটি ইমেজ জেনারেশন অ্যাপ তৈরি করবেন।

## শেখার লক্ষ্য

এই পাঠ শেষ করার পর, আপনি সক্ষম হবেন:

- একটি ইমেজ জেনারেশন অ্যাপ্লিকেশন তৈরি করতে।
- মেটা প্রম্পট ব্যবহার করে আপনার অ্যাপ্লিকেশনের সীমা নির্ধারণ করতে।
- DALL-E এবং Midjourney এর সাথে কাজ করতে।

## কেন একটি ইমেজ জেনারেশন অ্যাপ্লিকেশন তৈরি করবেন?

ইমেজ জেনারেশন অ্যাপ্লিকেশনগুলি জেনারেটিভ AI এর ক্ষমতা অন্বেষণের একটি চমৎকার উপায়। এগুলো ব্যবহার করা যেতে পারে, উদাহরণস্বরূপ:

- **ইমেজ এডিটিং এবং সিন্থেসিস**। বিভিন্ন ব্যবহারের জন্য ছবি তৈরি করা যায়, যেমন ছবি সম্পাদনা এবং ছবি সংমিশ্রণ।

- **বিভিন্ন শিল্পে প্রয়োগ**। মেডটেক, পর্যটন, গেম ডেভেলপমেন্ট সহ বিভিন্ন শিল্পের জন্য ছবি তৈরি করা যায়।

## পরিস্থিতি: Edu4All

এই পাঠের অংশ হিসেবে, আমরা আমাদের স্টার্টআপ Edu4All এর সাথে কাজ চালিয়ে যাব। শিক্ষার্থীরা তাদের মূল্যায়নের জন্য ছবি তৈরি করবে, কোন ছবি তৈরি হবে তা শিক্ষার্থীদের উপর নির্ভর করবে, তবে তারা তাদের নিজের গল্পের জন্য ইলাস্ট্রেশন তৈরি করতে পারে, নতুন চরিত্র তৈরি করতে পারে অথবা তাদের ধারণা ও কনসেপ্ট ভিজুয়ালাইজ করতে সাহায্য করতে পারে।

যদি তারা ক্লাসে স্মৃতিস্তম্ভ নিয়ে কাজ করে, তাহলে Edu4All এর শিক্ষার্থীরা উদাহরণস্বরূপ নিম্নলিখিত ছবি তৈরি করতে পারে:

![Edu4All startup, class on monuments, Eiffel Tower](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.bn.png)

এই ধরনের প্রম্পট ব্যবহার করে

> "Dog next to Eiffel Tower in early morning sunlight"

## DALL-E এবং Midjourney কী?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) এবং [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) হলো দুটি জনপ্রিয় ইমেজ জেনারেশন মডেল, যেগুলো প্রম্পট ব্যবহার করে ছবি তৈরি করতে দেয়।

### DALL-E

চলুন DALL-E দিয়ে শুরু করি, এটি একটি জেনারেটিভ AI মডেল যা টেক্সট বর্ণনা থেকে ছবি তৈরি করে।

> [DALL-E হলো দুটি মডেলের সংমিশ্রণ, CLIP এবং diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)।

- **CLIP**, একটি মডেল যা ছবি এবং টেক্সট থেকে এম্বেডিং তৈরি করে, যা ডেটার সংখ্যাসূচক উপস্থাপনা।

- **Diffused attention**, একটি মডেল যা এম্বেডিং থেকে ছবি তৈরি করে। DALL-E একটি ছবি ও টেক্সট ডেটাসেটে প্রশিক্ষিত এবং টেক্সট বর্ণনা থেকে ছবি তৈরি করতে পারে। উদাহরণস্বরূপ, DALL-E ব্যবহার করে একটি টুপি পরা বিড়াল বা মোহক সহ একটি কুকুরের ছবি তৈরি করা যায়।

### Midjourney

Midjourney DALL-E এর মতোই কাজ করে, এটি টেক্সট প্রম্পট থেকে ছবি তৈরি করে। Midjourney ব্যবহার করে “a cat in a hat” বা “a dog with a mohawk” এর মতো প্রম্পট দিয়ে ছবি তৈরি করা যায়।

![Midjourney দ্বারা তৈরি ছবি, মেকানিক্যাল কবুতর](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)  
_ছবির উৎস: উইকিপিডিয়া, Midjourney দ্বারা তৈরি_

## DALL-E এবং Midjourney কীভাবে কাজ করে

প্রথমে, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)। DALL-E হলো একটি জেনারেটিভ AI মডেল যা ট্রান্সফরমার আর্কিটেকচারের উপর ভিত্তি করে তৈরি, যার মধ্যে রয়েছে _autoregressive transformer_।

একটি _autoregressive transformer_ নির্ধারণ করে কিভাবে মডেল টেক্সট বর্ণনা থেকে ছবি তৈরি করে, এটি একবারে একটি পিক্সেল তৈরি করে এবং তারপর তৈরি পিক্সেল ব্যবহার করে পরবর্তী পিক্সেল তৈরি করে। এটি নিউরাল নেটওয়ার্কের একাধিক স্তর পেরিয়ে যায় যতক্ষণ না ছবি সম্পূর্ণ হয়।

এই প্রক্রিয়ায়, DALL-E ছবিতে অবজেক্ট, বৈশিষ্ট্য, এবং অন্যান্য গুণাবলী নিয়ন্ত্রণ করে। তবে, DALL-E 2 এবং 3 এ ছবির উপর আরও বেশি নিয়ন্ত্রণ রয়েছে।

## আপনার প্রথম ইমেজ জেনারেশন অ্যাপ্লিকেশন তৈরি করা

তাহলে একটি ইমেজ জেনারেশন অ্যাপ্লিকেশন তৈরি করতে কী কী লাগে? আপনার দরকার নিম্নলিখিত লাইব্রেরিগুলো:

- **python-dotenv**, এই লাইব্রেরি ব্যবহার করে আপনার গোপন তথ্য _.env_ ফাইলে কোড থেকে আলাদা রাখা ভালো।
- **openai**, এই লাইব্রেরি OpenAI API এর সাথে ইন্টারঅ্যাক্ট করার জন্য।
- **pillow**, পাইথনে ছবি নিয়ে কাজ করার জন্য।
- **requests**, HTTP রিকোয়েস্ট করার জন্য।

1. একটি _.env_ ফাইল তৈরি করুন নিচের বিষয়বস্তু সহ:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Azure পোর্টালে আপনার রিসোর্সের "Keys and Endpoint" সেকশনে এই তথ্য পাওয়া যাবে।

1. উপরের লাইব্রেরিগুলো একটি _requirements.txt_ ফাইলে সংগ্রহ করুন:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. এরপর, ভার্চুয়াল এনভায়রনমেন্ট তৈরি করে লাইব্রেরিগুলো ইনস্টল করুন:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   উইন্ডোজে ভার্চুয়াল এনভায়রনমেন্ট তৈরি ও সক্রিয় করতে নিচের কমান্ডগুলো ব্যবহার করুন:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ নামে একটি ফাইলে নিচের কোড যোগ করুন:

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

এই কোড ব্যাখ্যা করি:

- প্রথমে, আমরা প্রয়োজনীয় লাইব্রেরিগুলো ইমপোর্ট করি, যার মধ্যে OpenAI, dotenv, requests এবং Pillow লাইব্রেরি রয়েছে।

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- এরপর, _.env_ ফাইল থেকে পরিবেশ ভেরিয়েবল লোড করি।

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- তারপর, OpenAI API এর জন্য endpoint, key, version এবং type সেট করি।

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- এরপর, ছবি তৈরি করি:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  উপরের কোড একটি JSON অবজেক্ট রিটার্ন করে যার মধ্যে তৈরি হওয়া ছবির URL থাকে। আমরা URL ব্যবহার করে ছবি ডাউনলোড করে ফাইলে সংরক্ষণ করতে পারি।

- সর্বশেষে, আমরা ছবি ওপেন করে স্ট্যান্ডার্ড ইমেজ ভিউয়ার দিয়ে প্রদর্শন করি:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### ছবির জেনারেশন সম্পর্কে আরও বিস্তারিত

চলুন ছবির জেনারেশন কোডটি আরও বিস্তারিত দেখি:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, হলো টেক্সট প্রম্পট যা ছবি তৈরি করতে ব্যবহৃত হয়। এখানে আমরা ব্যবহার করছি "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"।
- **size**, তৈরি হওয়া ছবির আকার। এখানে 1024x1024 পিক্সেল।
- **n**, তৈরি হওয়া ছবির সংখ্যা। এখানে দুইটি ছবি তৈরি করা হচ্ছে।
- **temperature**, একটি প্যারামিটার যা জেনারেটিভ AI মডেলের আউটপুটের র‍্যান্ডমনেস নিয়ন্ত্রণ করে। এর মান 0 থেকে 1 এর মধ্যে হয়, যেখানে 0 মানে আউটপুট নির্ধারিত এবং 1 মানে আউটপুট সম্পূর্ণ র‍্যান্ডম। ডিফল্ট মান 0.7।

পরবর্তী অংশে আমরা ছবির সাথে আরও কাজ করার বিষয়গুলো আলোচনা করব।

## ইমেজ জেনারেশনের অতিরিক্ত ক্ষমতা

এখন পর্যন্ত আপনি দেখেছেন কিভাবে কয়েক লাইনের পাইথন কোড দিয়ে ছবি তৈরি করা যায়। তবে, ছবির সাথে আরও অনেক কিছু করা সম্ভব।

আপনি নিম্নলিখিত কাজগুলোও করতে পারেন:

- **সম্পাদনা করা**। একটি বিদ্যমান ছবির জন্য মাস্ক এবং প্রম্পট দিয়ে ছবির অংশ পরিবর্তন করা যায়। উদাহরণস্বরূপ, আমাদের খরগোশের ছবিতে একটি টুপি যোগ করা যেতে পারে। এর জন্য ছবিটি, মাস্ক (যেখানে পরিবর্তন হবে সেই অংশ চিহ্নিত করে) এবং টেক্সট প্রম্পট দিতে হবে।

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

  বেসিক ছবিতে শুধুমাত্র খরগোশ থাকবে, কিন্তু চূড়ান্ত ছবিতে খরগোশের মাথায় টুপি থাকবে।

- **ভ্যারিয়েশন তৈরি করা**। বিদ্যমান একটি ছবি নিয়ে তার বিভিন্ন রূপ তৈরি করা যায়। ভ্যারিয়েশন তৈরি করতে, একটি ছবি এবং টেক্সট প্রম্পট দিয়ে নিচের মতো কোড ব্যবহার করা হয়:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > লক্ষ্য করুন, এটি শুধুমাত্র OpenAI তে সমর্থিত।

## Temperature

Temperature হলো একটি প্যারামিটার যা জেনারেটিভ AI মডেলের আউটপুটের র‍্যান্ডমনেস নিয়ন্ত্রণ করে। এর মান 0 থেকে 1 এর মধ্যে হয়, যেখানে 0 মানে আউটপুট নির্ধারিত এবং 1 মানে আউটপুট সম্পূর্ণ র‍্যান্ডম। ডিফল্ট মান 0.7।

চলুন একটি উদাহরণ দেখি temperature কীভাবে কাজ করে, নিচের প্রম্পটটি দুইবার চালিয়ে:

> প্রম্পট: "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![Bunny on a horse holding a lollipop, version 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.bn.png)

এখন একই প্রম্পট আবার চালাই, দেখতে পাবো একই ছবি আসবে না:

![Generated image of bunny on horse](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.bn.png)

আপনি দেখতে পাচ্ছেন, ছবিগুলো মিল আছে কিন্তু এক নয়। এবার temperature মান 0.1 করে দেখি কী হয়:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Temperature পরিবর্তন

চলুন আউটপুটকে আরও নির্ধারিত করার চেষ্টা করি। আমরা দেখেছি প্রথম ছবিতে খরগোশ আছে, দ্বিতীয় ছবিতে ঘোড়া, তাই ছবিগুলো অনেক ভিন্ন।

সুতরাং, আমাদের কোড পরিবর্তন করে temperature 0 করি, যেমন:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

এখন কোড চালালে এই দুই ছবি পাবেন:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.bn.png)
- ![Temperature 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.bn.png)

এখানে স্পষ্ট দেখা যাচ্ছে ছবিগুলো একে অপরের সাথে অনেক বেশি মিল রয়েছে।

## মেটাপ্রম্পট দিয়ে আপনার অ্যাপ্লিকেশনের সীমা নির্ধারণ করা

আমাদের ডেমোতে আমরা ইতোমধ্যেই ক্লায়েন্টদের জন্য ছবি তৈরি করতে পারি। তবে, আমাদের অ্যাপ্লিকেশনের জন্য কিছু সীমা তৈরি করা দরকার।

উদাহরণস্বরূপ, আমরা এমন ছবি তৈরি করতে চাই না যা কাজের জন্য নিরাপদ নয়, বা যা শিশুদের জন্য উপযুক্ত নয়।

আমরা এটি _মেটাপ্রম্পট_ ব্যবহার করে করতে পারি। মেটাপ্রম্পট হলো টেক্সট প্রম্পট যা জেনারেটিভ AI মডেলের আউটপুট নিয়ন্ত্রণ করতে ব্যবহৃত হয়। উদাহরণস্বরূপ, আমরা মেটাপ্রম্পট ব্যবহার করে নিশ্চিত করতে পারি যে তৈরি হওয়া ছবি কাজের জন্য নিরাপদ এবং শিশুদের জন্য উপযুক্ত।

### এটি কীভাবে কাজ করে?

মেটাপ্রম্পট কীভাবে কাজ করে?

মেটাপ্রম্পট হলো টেক্সট প্রম্পট যা মডেলের আউটপুট নিয়ন্ত্রণ করে, এগুলো টেক্সট প্রম্পটের আগে রাখা হয় এবং মডেলের আউটপুট নিয়ন্ত্রণের জন্য অ্যাপ্লিকেশনে এমবেড করা হয়। প্রম্পট ইনপুট এবং মেটাপ্রম্পট ইনপুট একত্রে একটি টেক্সট প্রম্পট হিসেবে ব্যবহৃত হয়।

মেটাপ্রম্পটের একটি উদাহরণ হতে পারে:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

এখন, চলুন দেখি কিভাবে আমরা আমাদের ডেমোতে মেটাপ্রম্পট ব্যবহার করতে পারি।

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

উপরের প্রম্পট থেকে দেখা যায় কিভাবে তৈরি হওয়া সব ছবি মেটাপ্রম্পট বিবেচনা করে তৈরি হচ্ছে।

## অ্যাসাইনমেন্ট - শিক্ষার্থীদের সক্ষম করুন

এই পাঠের শুরুতে আমরা Edu4All পরিচয় করিয়েছি। এখন শিক্ষার্থীদের তাদের মূল্যায়নের জন্য ছবি তৈরি করার সুযোগ দেওয়ার সময়।

শিক্ষার্থীরা তাদের মূল্যায়নের জন্য স্মৃতিস্তম্ভের ছবি তৈরি করবে, কোন স্মৃতিস্তম্ভ হবে তা শিক্ষার্থীদের উপর নির্ভর করবে। শিক্ষার্থীদের সৃজনশীলতা ব্যবহার করে এই স্মৃতিস্তম্ভগুলো বিভিন্ন প্রেক্ষাপটে স্থাপন করতে বলা হয়েছে।

## সমাধান

এখানে একটি সম্ভাব্য সমাধান:

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

## অসাধারণ কাজ! আপনার শেখা চালিয়ে যান

এই পাঠ শেষ করার পর, আমাদের [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) দেখুন এবং আপনার জেনারেটিভ AI জ্ঞান আরও উন্নত করুন!

পরবর্তী পাঠে যান যেখানে আমরা দেখব কিভাবে [লো-কোড দিয়ে AI অ্যাপ্লিকেশন তৈরি করবেন](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।