# ছবি তৈরি অ্যাপ্লিকেশন নির্মাণ

[![ছবি তৈরি অ্যাপ্লিকেশন নির্মাণ](../../../translated_images/bn/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLM এর কাজ শুধু টেক্সট জেনারেশনেই সীমাবদ্ধ নয়। টেক্সট বর্ণনা থেকে ছবি তৈরি করাও সম্ভব। ছবি একটি মোড্যালিটি হিসেবে বিভিন্ন ক্ষেত্রে যেমন মেডটেক, আর্কিটেকচার, পর্যটন, গেম ডেভেলপমেন্ট এবং আরও অনেক কিছুতে অত্যন্ত উপকারী হতে পারে। এই অধ্যায়ে, আমরা সবচেয়ে জনপ্রিয় দুইটি ছবি তৈরি মডেল, DALL-E এবং Midjourney সম্পর্কে আলোচনা করব।

## পরিচিতি

এই পাঠে আমরা নিম্নলিখিত বিষয়গুলো আলোচনা করব:

- ছবি তৈরি এবং কেন এটি উপকারী।
- DALL-E এবং Midjourney কি এবং এগুলো কীভাবে কাজ করে।
- আপনি কীভাবে একটি ছবি তৈরি অ্যাপ্লিকেশন তৈরি করবেন।

## শেখার লক্ষ্য

এই পাঠ সমাপ্ত করার পর, আপনি পারবেন:

- একটি ছবি তৈরি অ্যাপ্লিকেশন তৈরি করতে।
- মেটা প্রম্পট দিয়ে আপনার অ্যাপ্লিকেশনের সীমা নির্ধারণ করতে।
- DALL-E এবং Midjourney এর সাথে কাজ করতে।

## কেন ছবি তৈরি অ্যাপ্লিকেশন তৈরি করবেন?

ছবি তৈরি অ্যাপ্লিকেশনগুলো জেনারেটিভ AI এর ক্ষমতাগুলো অন্বেষণের একটি দারুণ উপায়। এগুলো ব্যবহার করা যেতে পারে, উদাহরণস্বরূপ:

- **ছবি সম্পাদনা এবং সংশ্লেষণ।** আপনি বিভিন্ন ব্যবহার ক্ষেত্রে, যেমন ছবি সম্পাদনা এবং ছবি সংশ্লেষণের জন্য ছবি তৈরি করতে পারেন।

- **বিভিন্ন শিল্পে প্রয়োগ।** এগুলো বিভিন্ন শিল্প যেমন মেডটেক, পর্যটন, গেম ডেভেলপমেন্ট ইত্যাদির জন্য ছবি তৈরি করতে ব্যবহার করা যেতে পারে।

## দৃশ্যমান উদাহরণ: Edu4All

এই পাঠের অংশ হিসাবে, আমরা আমাদের স্টার্টআপ Edu4All এর সাথে কাজ চালিয়ে যাব। শিক্ষার্থীরা তাদের মূল্যায়নের জন্য ছবি তৈরি করবে, কোন ছবি তৈরি হবে সেটা শিক্ষার্থীদের উপর নির্ভর করবে, তবে এটা হতে পারে তাদের নিজস্ব পরী কাহিনীর জন্য উপস্থাপনা, কিংবা তাদের গল্পের নতুন চরিত্র তৈরি, অথবা ধারণা ও কনসেপ্টগুলো দৃশ্যমান করার জন্য।

উদাহরণস্বরূপ, যদি Edu4All এর শিক্ষার্থীরা শ্রেণিতে স্মৃতিসৌধ নিয়ে কাজ করে, তারা কি তৈরি করতে পারে তা এখানে দেওয়া হলো:

![Edu4All startup, class on monuments, Eiffel Tower](../../../translated_images/bn/startup.94d6b79cc4bb3f5a.webp)

এমন একটি প্রম্পট ব্যবহার করে

> "কালো হয়ে ওঠার আগের সূর্যের আলোতে আইফেল টাওয়ারের পাশে কুকুর"

## DALL-E এবং Midjourney কী?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) এবং [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) হলো দুইটি সবচেয়ে জনপ্রিয় ছবি তৈরি মডেল, যেখানে প্রম্পট ব্যবহার করে ছবি তৈরি করা যায়।

### DALL-E

চলুন DALL-E থেকে শুরু করা যাক, এটি একটি জেনারেটিভ AI মডেল যা টেক্সট বর্ণনা থেকে ছবি তৈরি করে।

> [DALL-E হলো CLIP এবং diffused attention এই দুই মডেলের সমন্বয়](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, একটি মডেল যা ছবি এবং টেক্সট থেকে সংখ্যাত্মক প্রতিনিধিত্ব (embedding) তৈরি করে।

- **Diffused attention**, একটি মডেল যা embedding থেকে ছবি তৈরি করে। DALL-E একটি ছবি ও টেক্সট ডাটাসেটে ট্রেইন করা হয়েছে এবং টেক্সট বর্ণনা থেকে ছবি তৈরি করতে পারে। উদাহরণস্বরূপ, DALL-E একটি টুপি পরা বিড়াল বা মোহক সহ একটি কুকুরের ছবি তৈরি করতে পারে।

### Midjourney

Midjourney DALL-E এর মতো কাজ করে, এটি টেক্সট প্রম্পট থেকে ছবি তৈরি করে। Midjourney-ও প্রম্পট ব্যবহার করে “একটি টুপি পরা বিড়াল” বা “মোহকযুক্ত কুকুর” এর মত ছবি তৈরি করতে পারে।

![Midjourney দ্বারা তৈরি একটি মেকানিক্যাল কবুতর](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_ছবির ক্রেডিট উইকিপিডিয়া, Midjourney দ্বারা তৈরি ছবি_

## DALL-E এবং Midjourney কীভাবে কাজ করে

প্রথমেই, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)। DALL-E হলো একটি জেনারেটিভ AI মডেল যা ট্রান্সফর্মার আর্কিটেকচারে ভিত্তি করে এবং একটি _অটোরিগ্রেসিভ ট্রান্সফর্মার_ ব্যবহার করে।

একটি _অটোরিগ্রেসিভ ট্রান্সফর্মার_ সংজ্ঞায়িত করে কিভাবে মডেল টেক্সট বর্ণনা থেকে ছবি তৈরি করে, এটি একবারে একটি পিক্সেল তৈরি করে এবং তারপর তৈরি পিক্সেলগুলো ব্যবহার করে পরবর্তী পিক্সেল তৈরি করে। এটি নিউরাল নেটওয়ার্কের একাধিক স্তর দিয়ে প্রবাহিত হয় যতক্ষণ না ছবি সম্পূর্ণ হয়।

এই প্রক্রিয়ার মাধ্যমে, DALL-E তৈরি ছবির বৈশিষ্ট্য, বস্তু, গুণাবলী ইত্যাদিকে নিয়ন্ত্রণ করে। তবে, DALL-E 2 এবং 3 আরও বেশি নিয়ন্ত্রণ দেয় তৈরি ছবির ওপর।

## আপনার প্রথম ছবি তৈরি অ্যাপ্লিকেশন তৈরি

তাহলে ছবি তৈরি অ্যাপ্লিকেশন তৈরি করতে কী প্রয়োজন? নিম্নলিখিত লাইব্রেরিগুলো দরকার:

- **python-dotenv**, এই লাইব্রেরি ব্যবহার করা খুবই প্রস্তাবিত আপনার সিক্রেটগুলো কোড থেকে আলাদা _.env_ ফাইলে রাখার জন্য।
- **openai**, এই লাইব্রেরি ব্যবহার করবেন OpenAI API এর সাথে যোগাযোগ করতে।
- **pillow**, পাইথনে ছবি নিয়ে কাজ করার জন্য।
- **requests**, HTTP অনুরোধ করতে সাহায্য করার জন্য।

## Azure OpenAI মডেল তৈরি এবং ডিপ্লয় করা

যদি এখনও না করে থাকেন, [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) পেজের নির্দেশনা অনুসরণ করে
Azure OpenAI রিসোর্স এবং মডেল তৈরি করুন। মডেল হিসেবে **gpt-image-1** নির্বাচন করুন (বর্তমানের Azure OpenAI ছবি মডেল; DALL-E 3 এখন পুরাতন এবং নতুন ডিপ্লয়মেন্টের জন্য উপলব্ধ নয়)।

## অ্যাপ তৈরি করুন

১. _.env_ নামে একটি ফাইল তৈরি করুন নিম্নলিখিত কনটেন্ট নিয়ে:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   Azure OpenAI Foundry পোর্টালে আপনার রিসোর্সের "Deployments" সেকশনে এই তথ্য locate করুন।

১. উপরের উল্লেখিত লাইব্রেরিগুলো একটি _requirements.txt_ ফাইলে সংগ্রহ করুন, যেমনটি নিচে দেওয়া হয়েছে:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

১. এরপর, ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন এবং লাইব্রেরিগুলো ইনস্টল করুন:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   উইন্ডোজে, ভার্চুয়াল এনভায়রনমেন্ট তৈরি এবং সক্রিয় করতে নিচের কমান্ডগুলো ব্যবহার করুন:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

১. _app.py_ নামে একটি ফাইলে নিচের কোড যোগ করুন:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # dotenv ইমপোর্ট করুন
    dotenv.load_dotenv()
    
    # Azure OpenAI সার্ভিস ক্লায়েন্ট কনফিগার করুন
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # ইমেজ জেনারেশন API ব্যবহার করে একটি ছবি তৈরি করুন
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # সংরক্ষিত ছবির জন্য ডিরেক্টরি সেট করুন
        image_dir = os.path.join(os.curdir, 'images')

        # যদি ডিরেক্টরি না থাকে, তাহলে সেটি তৈরি করুন
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # ইমেজ পাথ ইনিশিয়ালাইজ করুন (দ্রষ্টব্য: ফাইলটাইপ png হওয়া উচিত)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # তৈরি করা ছবি রিট্রিভ করুন
        image_url = generation_response.data[0].url  # রেসপন্স থেকে ইমেজ URL বের করুন
        generated_image = requests.get(image_url).content  # ছবি ডাউনলোড করুন
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # ডিফল্ট ইমেজ ভিউয়ারে ছবি প্রদর্শন করুন
        image = Image.open(image_path)
        image.show()

    # এক্সসেপশন ধরা
    except openai.BadRequestError as err:
        print(err)
   ```

চলুন এই কোড ব্যাখ্যা করি:

- প্রথমে, আমরা প্রয়োজনীয় লাইব্রেরি ইমপোর্ট করি, যার মধ্যে আছে OpenAI লাইব্রেরি, dotenv লাইব্রেরি, requests লাইব্রেরি, এবং Pillow লাইব্রেরি।

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- এরপর, আমরা _.env_ ফাইল থেকে পরিবেশ ভেরিয়েবলগুলো লোড করি।

  ```python
  # dotenv আমদানি করুন
  dotenv.load_dotenv()
  ```

- তারপর, Azure OpenAI সার্ভিস ক্লায়েন্ট কনফিগার করি 

  ```python
  # পরিবেশ ভেরিয়েবল থেকে এন্ডপয়েন্ট এবং কী সংগ্রহ করুন
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- এরপর, আমরা ছবি তৈরি করি:

  ```python
  # ইমেজ জেনারেশন API ব্যবহার করে একটি ছবি তৈরি করুন
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  উপরের কোডটি একটি JSON অবজেক্ট রেসপন্স দেয়, যেখানে তৈরি ছবির URL থাকে। আমরা এই URL ব্যবহার করে ছবি ডাউনলোড করে ফাইলে সংরক্ষণ করতে পারি।

- শেষে, আমরা ছবিটি খুলে সাধারণ ইমেজ ভিউয়ার দিয়ে প্রদর্শন করি:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### ছবির তৈরি সম্পর্কে আরও বিস্তারিত

আসুন ছবির তৈরি কোডটি বিস্তারিত দেখি:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, হলো সেই টেক্সট প্রম্পট যা ছবি তৈরির জন্য ব্যবহৃত হয়। এই ক্ষেত্রে, আমরা প্রম্পট হিসাবে "বনির ঘোড়ায় বসা, ললিপপ ধরে আছে, কুয়াশাচ্ছন্ন ময়দানে যেখানে ড্যাফোডিল ফুল ফোঁটে" ব্যবহার করছি।
- **size**, হলো তৈরি হওয়া ছবির আকার। এই ক্ষেত্রে, আমরা ১০২৪x১০২৪ পিক্সেলের ছবি তৈরি করছি।
- **n**, তৈরি হওয়া ছবির সংখ্যা। এই ক্ষেত্রে, আমরা দুটি ছবি তৈরি করছি।
- **temperature**, হলো একটি প্যারামিটার যা জেনারেটিভ AI মডেলের আউটপুটের এলোমেলোতা নিয়ন্ত্রণ করে। টেম্পারেচার ০ থেকে ১ এর মধ্যে একটি মান, যেখানে ০ মানে আউটপুট পূর্ণ নির্ধারিত এবং ১ মানে আউটপুট সম্পূর্ণ এলোমেলো। ডিফল্ট মান ০.৭।

ছবির সাথে আরও অনেক কিছু করতে পারেন যা আমরা পরবর্তী সেকশনে আলোচনা করব।

## ছবি তৈরির অতিরিক্ত ক্ষমতা

এখন পর্যন্ত আপনি দেখেছেন কিভাবে কয়েক লাইন পাইথন কোড দিয়ে ছবি তৈরি করা যায়। তবে ছবির সাথে আরও অনেক কিছু করার সুযোগ আছে।

আপনি নিম্নলিখিত কাজগুলোও করতে পারবেন:

- **সম্পাদনা করা।** বিদ্যমান একটি ছবির জন্য মাস্ক এবং প্রম্পট প্রদান করে ছবিটিকে পরিবর্তন করা যায়। উদাহরণস্বরূপ, একটি ছবির কিছু অংশে কিছু যোগ করা যায়। আমাদের বানির ছবির কথা ভাবুন, আপনি বানির মাথায় একটি টুপি যোগ করতে পারেন। এটা করার জন্য আপনাকে ছবিটি, মাস্ক (যা পরিবর্তনের অংশ চিহ্নিত করে) এবং টেক্সট প্রম্পট দিতে হবে যা বলে কী পরিবর্তন করা হবে। 
> লক্ষ্য করুন: এটি DALL-E 3 এ সমর্থিত নয়। 
 
এখানে GPT Image ব্যবহার করে একটি উদাহরণ দেওয়া হলো:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  বেস ইমেজে শুধু পুল সহ লাউঞ্জ থাকবে, কিন্তু চূড়ান্ত ছবিতে একটি ফ্ল্যামিঙ্গো থাকবে:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/bn/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/bn/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/bn/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **বিভিন্ন রূপ তৈরি করা।** এখানে ধারণাটি হলো আপনার কাছে একটি বিদ্যমান ছবি আছে এবং আপনি variations (বিভিন্ন রূপ) তৈরি করতে চান। একটি variation তৈরি করতে, আপনি একটি ছবি এবং একটি টেক্সট প্রম্পট দেন এবং নিচের মতো কোড ব্যবহার করেন:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > লক্ষ্য করুন, এটি শুধুমাত্র OpenAI এর DALL-E 2 মডেলে সমর্থিত, gpt-image-1 এ নয়

## টেম্পারেচার

টেম্পারেচার হলো একটি প্যারামিটার যা জেনারেটিভ AI মডেলের আউটপুটের এলোমেলোতা নিয়ন্ত্রণ করে। এটি ০ থেকে ১ এর মধ্যে মান গ্রহণ করে, যেখানে ০ মানে আউটপুট সম্পূর্ণ নির্ধারিত এবং ১ মানে আউটপুট এলোমেলো। ডিফল্ট মান হলো ০.৭।

চলুন একটি উদাহরণ দেখি কিভাবে টেম্পারেচার কাজ করে, একই প্রম্পট দুবার চালিয়ে:

> প্রম্পট: "বনির ঘোড়ায় বসা, ললিপপ ধরে আছে, কুয়াশাচ্ছন্ন ময়দানে যেখানে ড্যাফোডিল ফুল ফোঁটে"

![বনির ঘোড়ায় বসা, ললিপপ ধরে, ভার্সন ১](../../../translated_images/bn/v1-generated-image.a295cfcffa3c13c2.webp)

এবার একই প্রম্পট আবার চালাই দেখার জন্য যে আমরা একই ছবি পাবো না:

![বনির ঘোড়ায় তৈরি ছবি](../../../translated_images/bn/v2-generated-image.33f55a3714efe61d.webp)

আপনি দেখতে পাচ্ছেন, ছবিগুলো অনুরূপ কিন্তু একই নয়। এখন টেম্পারেচারের মান ০.১ করে দেখি কী হয়:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # এখানে আপনার প্রম্পট টেক্সট লিখুন
        size='1024x1024',
        n=2
    )
```

### টেম্পারেচার পরিবর্তন

তাই আমরা চেষ্টা করব উত্তরকে আরও নির্ধারিত করতে। আমরা প্রথম দুটি তৈরি ছবিতে পার্থক্য দেখতে পেয়েছি, প্রথম ছবিতে একটি বনির ছবি এবং দ্বিতীয় ছবিতে ঘোড়ার ছবি, তাই ছবি দুটির মধ্যে প্রচুর পার্থক্য ছিল।

তাই আমরা কোড পরিবর্তন করে টেম্পারেচার ০ করি, যেমন:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # এখানে আপনার প্রম্পট টেক্সট লিখুন
        size='1024x1024',
        n=2,
        temperature=0
    )
```

এবার এই কোড চালালে আপনি এই দুটি ছবি পাবেন:

- ![টেম্পারেচার ০, ভার্সন ১](../../../translated_images/bn/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![টেম্পারেচার ০, ভার্সন ২](../../../translated_images/bn/v2-temp-generated-image.871d0c920dbfb0f1.webp)

এখানে স্পষ্টভাবে দেখা যাচ্ছে ছবিগুলো বেশি অনুরূপ।

## মেটাপ্রম্পট দিয়ে আপনার অ্যাপ্লিকেশনের সীমা নির্ধারণ করতে কিভাবে করবেন

আমাদের ডেমো দিয়ে আমরা ইতোমধ্যেই গ্রাহকদের জন্য ছবি তৈরি করতে পারছি। কিন্তু আমাদের অ্যাপ্লিকেশনের জন্য কিছু সীমা তৈরি করতে হবে।

উদাহরণস্বরূপ, আমরা এমন ছবি তৈরি করতে চাই না যা কর্মক্ষেত্রে নিরাপদ নয়, অথবা শিশুদের জন্য উপযুক্ত নয়।

আমরা এটি _মেটাপ্রম্পট_ দিয়ে করতে পারি। মেটাপ্রম্পট হলো টেক্সট প্রম্পট যেগুলো জেনারেটিভ AI মডেলের আউটপুট নিয়ন্ত্রণ করে। উদাহরণস্বরূপ, আমরা মেটাপ্রম্পট ব্যবহার করে আউটপুট নিয়ন্ত্রণ করতে পারি এবং নিশ্চিত করতে পারি যে তৈরি হওয়া ছবি কর্মক্ষেত্রে নিরাপদ এবং শিশুর জন্য উপযুক্ত।

### এটা কিভাবে কাজ করে?

এখন, মেটাপ্রম্পট কিভাবে কাজ করে?

মেটাপ্রম্পট হলো টেক্সট প্রম্পট যা জেনারেটিভ AI মডেলের আউটপুট নিয়ন্ত্রণ করে, এগুলো টেক্সট প্রম্পটের আগে থাকে, মডেলের আউটপুট নিয়ন্ত্রণের জন্য ব্যবহৃত হয় এবং অ্যাপ্লিকেশনে এমবেড করা হয় যাতে মডেলের আউটপুট নিয়ন্ত্রণ করা যায়। মেটাপ্রম্পট এবং সাধারণ প্রম্পট একসাথে একটি টেক্সট প্রম্পটের মধ্যে রাখা হয়।

মেটাপ্রম্পটের একটি উদাহরণ হবে নিচের মতো:

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

# TODO ছবি তৈরি করার জন্য অনুরোধ যোগ করুন
```

উপরের প্রম্পট থেকে দেখা যাচ্ছে সব ছবিই মেটাপ্রম্পটকে বিবেচনা করে তৈরি হচ্ছে।

## অ্যাসাইনমেন্ট - শিক্ষার্থীদের সক্ষম করুন

আমরা এই পাঠের শুরুতেই Edu4All পরিচয় করিয়েছিলাম। এখন সময় এসেছে শিক্ষার্থীদের তাদের মূল্যায়নের জন্য ছবি তৈরি করার জন্য সক্ষম করতে।


শিক্ষার্থীরা তাদের মূল্যায়নের জন্য স্মৃতিস্তম্ভযুক্ত ছবি তৈরি করবে, কোন স্মৃতিস্তম্ভগুলি হবে তা সম্পূর্ণরূপে শিক্ষার্থীদের উপর নির্ভর করে। শিক্ষার্থীদের এই কাজটিতে তাদের সৃজনশীলতা ব্যবহার করে এই স্মৃতিস্তম্ভগুলোকে বিভিন্ন প্রসঙ্গে স্থাপন করতে বলা হয়েছে।

## সমাধান

এখানে একটি সম্ভাব্য সমাধান দেওয়া হলো:

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# dotenv ইমপোর্ট করুন
dotenv.load_dotenv()

# পরিবেশ ভেরিয়েবল থেকে এন্ডপয়েন্ট এবং কী পান
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
    # ইমেজ জেনারেশন API ব্যবহার করে একটি ছবি তৈরি করুন
    generation_response = client.images.generate(
        prompt=prompt,    # আপনার প্রম্পট টেক্সট এখানে লিখুন
        size='1024x1024',
        n=1,
    )
    # সংরক্ষিত ছবির জন্য ডিরেক্টরি নির্ধারণ করুন
    image_dir = os.path.join(os.curdir, 'images')

    # যদি ডিরেক্টরিটি না থাকে, তবে এটি তৈরি করুন
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # ইমেজ পথ নির্দিষ্ট করুন (নোট করুন ফাইলটাইপ অবশ্যই png হতে হবে)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # তৈরি হওয়া ছবি পুনরুদ্ধার করুন
    image_url = generation_response.data[0].url  # প্রতিক্রিয়া থেকে ছবি URL বের করুন
    generated_image = requests.get(image_url).content  # ছবিটি ডাউনলোড করুন
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # ডিফল্ট ইমেজ ভিউয়ারে ছবি প্রদর্শন করুন
    image = Image.open(image_path)
    image.show()

# ব্যতিক্রম ধরা হোক
except openai.BadRequestError as err:
    print(err)
```

## দারুণ কাজ! আপনার শিক্ষা চালিয়ে যান

এই পাঠ সম্পন্ন করার পরে, আমাদের [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) দেখুন যাতে আপনার Generative AI জ্ঞান আরও উন্নত করতে পারেন!

লেসন ১০ এ যান যেখানে আমরা দেখব কিভাবে [কম-কোডের মাধ্যমে AI অ্যাপ্লিকেশন তৈরি করা যায়](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->