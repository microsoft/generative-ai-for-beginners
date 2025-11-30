<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "238cde5c90363d70ecc939569378da51",
  "translation_date": "2025-10-17T14:55:26+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "bn"
}
-->
# ইমেজ জেনারেশন অ্যাপ্লিকেশন তৈরি করা

[![ইমেজ জেনারেশন অ্যাপ্লিকেশন তৈরি করা](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.bn.png)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

টেক্সট জেনারেশনের বাইরে LLM-এর আরও অনেক কিছু আছে। টেক্সট বর্ণনা থেকে ইমেজ তৈরি করাও সম্ভব। ইমেজ একটি মাধ্যম হিসেবে বিভিন্ন ক্ষেত্রে যেমন মেডটেক, স্থাপত্য, পর্যটন, গেম ডেভেলপমেন্ট এবং আরও অনেক কিছুতে অত্যন্ত কার্যকর হতে পারে। এই অধ্যায়ে, আমরা দুটি জনপ্রিয় ইমেজ জেনারেশন মডেল, DALL-E এবং Midjourney সম্পর্কে আলোচনা করব।

## পরিচিতি

এই পাঠে আমরা আলোচনা করব:

- ইমেজ জেনারেশন এবং কেন এটি গুরুত্বপূর্ণ।
- DALL-E এবং Midjourney, তারা কী এবং কীভাবে কাজ করে।
- কীভাবে আপনি একটি ইমেজ জেনারেশন অ্যাপ তৈরি করবেন।

## শেখার লক্ষ্য

এই পাঠ শেষ করার পর, আপনি সক্ষম হবেন:

- একটি ইমেজ জেনারেশন অ্যাপ্লিকেশন তৈরি করতে।
- মেটা প্রম্পট দিয়ে আপনার অ্যাপ্লিকেশনের সীমা নির্ধারণ করতে।
- DALL-E এবং Midjourney এর সাথে কাজ করতে।

## কেন ইমেজ জেনারেশন অ্যাপ্লিকেশন তৈরি করবেন?

ইমেজ জেনারেশন অ্যাপ্লিকেশন জেনারেটিভ AI-এর ক্ষমতা অন্বেষণ করার একটি চমৎকার উপায়। এগুলো ব্যবহার করা যেতে পারে, যেমন:

- **ইমেজ সম্পাদনা এবং সংশ্লেষণ**। বিভিন্ন ব্যবহারের জন্য ইমেজ তৈরি করা যেতে পারে, যেমন ইমেজ সম্পাদনা এবং ইমেজ সংশ্লেষণ।

- **বিভিন্ন শিল্পে প্রয়োগ**। এগুলো মেডটেক, পর্যটন, গেম ডেভেলপমেন্ট এবং আরও অনেক শিল্পের জন্য ইমেজ তৈরি করতে ব্যবহার করা যেতে পারে।

## দৃশ্যপট: Edu4All

এই পাঠের অংশ হিসেবে, আমরা আমাদের স্টার্টআপ Edu4All-এর সাথে কাজ চালিয়ে যাব। শিক্ষার্থীরা তাদের মূল্যায়নের জন্য ইমেজ তৈরি করবে, ঠিক কী ধরনের ইমেজ তা শিক্ষার্থীদের উপর নির্ভর করবে, তবে তারা তাদের নিজস্ব রূপকথার জন্য চিত্র তৈরি করতে পারে বা তাদের গল্পের জন্য একটি নতুন চরিত্র তৈরি করতে পারে বা তাদের ধারণা এবং ধারণাগুলি চিত্রিত করতে সাহায্য করতে পারে।

যদি তারা ক্লাসে স্মৃতিস্তম্ভ নিয়ে কাজ করে, তাহলে Edu4All-এর শিক্ষার্থীরা উদাহরণস্বরূপ এটি তৈরি করতে পারে:

![Edu4All স্টার্টআপ, ক্লাসে স্মৃতিস্তম্ভ, আইফেল টাওয়ার](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.bn.png)

একটি প্রম্পট ব্যবহার করে যেমন:

> "সকালবেলার সূর্যের আলোতে আইফেল টাওয়ারের পাশে একটি কুকুর"

## DALL-E এবং Midjourney কী?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) এবং [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) দুটি জনপ্রিয় ইমেজ জেনারেশন মডেল, যা আপনাকে প্রম্পট ব্যবহার করে ইমেজ তৈরি করতে দেয়।

### DALL-E

চলুন শুরু করি DALL-E দিয়ে, এটি একটি জেনারেটিভ AI মডেল যা টেক্সট বর্ণনা থেকে ইমেজ তৈরি করে।

> [DALL-E দুটি মডেল, CLIP এবং diffused attention-এর সংমিশ্রণ](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)।

- **CLIP**, একটি মডেল যা ইমেজ এবং টেক্সট থেকে এমবেডিং তৈরি করে, যা ডেটার সংখ্যাসূচক উপস্থাপনা।

- **Diffused attention**, একটি মডেল যা এমবেডিং থেকে ইমেজ তৈরি করে। DALL-E একটি ইমেজ এবং টেক্সটের ডেটাসেটে প্রশিক্ষিত এবং এটি টেক্সট বর্ণনা থেকে ইমেজ তৈরি করতে ব্যবহার করা যেতে পারে। উদাহরণস্বরূপ, DALL-E একটি টুপি পরা বিড়াল বা একটি মোহক সহ কুকুরের ইমেজ তৈরি করতে ব্যবহার করা যেতে পারে।

### Midjourney

Midjourney DALL-E-এর মতোই কাজ করে, এটি টেক্সট প্রম্পট থেকে ইমেজ তৈরি করে। Midjourney প্রম্পট ব্যবহার করে ইমেজ তৈরি করতে পারে যেমন "একটি টুপি পরা বিড়াল" বা "মোহক সহ একটি কুকুর"।

![Midjourney দ্বারা তৈরি ইমেজ, যান্ত্রিক কবুতর](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_চিত্র ক্রেডিট উইকিপিডিয়া, Midjourney দ্বারা তৈরি ইমেজ_

## DALL-E এবং Midjourney কীভাবে কাজ করে

প্রথমে, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)। DALL-E একটি জেনারেটিভ AI মডেল যা ট্রান্সফর্মার আর্কিটেকচারের উপর ভিত্তি করে তৈরি এবং একটি _অটোরিগ্রেসিভ ট্রান্সফর্মার_।

একটি _অটোরিগ্রেসিভ ট্রান্সফর্মার_ সংজ্ঞায়িত করে কীভাবে একটি মডেল টেক্সট বর্ণনা থেকে ইমেজ তৈরি করে, এটি একবারে একটি পিক্সেল তৈরি করে এবং তারপর পরবর্তী পিক্সেল তৈরি করতে তৈরি পিক্সেলগুলি ব্যবহার করে। একটি নিউরাল নেটওয়ার্কের একাধিক স্তর পেরিয়ে, যতক্ষণ না ইমেজ সম্পূর্ণ হয়।

এই প্রক্রিয়ার মাধ্যমে, DALL-E, তৈরি করা ইমেজে বৈশিষ্ট্য, বস্তু, বৈশিষ্ট্য এবং আরও অনেক কিছু নিয়ন্ত্রণ করে। তবে, DALL-E 2 এবং 3 তৈরি করা ইমেজের উপর আরও বেশি নিয়ন্ত্রণ প্রদান করে।

## আপনার প্রথম ইমেজ জেনারেশন অ্যাপ্লিকেশন তৈরি করা

তাহলে একটি ইমেজ জেনারেশন অ্যাপ্লিকেশন তৈরি করতে কী লাগে? আপনাকে নিম্নলিখিত লাইব্রেরিগুলোর প্রয়োজন হবে:

- **python-dotenv**, আপনার গোপনীয়তাগুলি _.env_ ফাইলে কোড থেকে দূরে রাখতে এই লাইব্রেরি ব্যবহার করার পরামর্শ দেওয়া হয়।
- **openai**, এই লাইব্রেরি OpenAI API-এর সাথে ইন্টারঅ্যাক্ট করতে ব্যবহার করা হবে।
- **pillow**, পাইথনে ইমেজ নিয়ে কাজ করার জন্য।
- **requests**, HTTP অনুরোধ করতে সাহায্য করার জন্য।

## একটি Azure OpenAI মডেল তৈরি এবং ডিপ্লয় করুন

যদি এখনও না করা হয়, [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) পৃষ্ঠার নির্দেশাবলী অনুসরণ করুন
একটি Azure OpenAI রিসোর্স এবং মডেল তৈরি করতে। মডেল হিসেবে DALL-E 3 নির্বাচন করুন।  

## অ্যাপ তৈরি করুন

1. _.env_ নামে একটি ফাইল তৈরি করুন নিম্নলিখিত বিষয়বস্তু সহ:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   আপনার রিসোর্সের "Deployments" বিভাগে Azure OpenAI Foundry Portal-এ এই তথ্যটি খুঁজুন।

1. উপরের লাইব্রেরিগুলি _requirements.txt_ নামে একটি ফাইলে সংগ্রহ করুন:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. এরপর, ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন এবং লাইব্রেরিগুলি ইনস্টল করুন:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   উইন্ডোজের জন্য, আপনার ভার্চুয়াল এনভায়রনমেন্ট তৈরি এবং সক্রিয় করতে নিম্নলিখিত কমান্ডগুলি ব্যবহার করুন:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ নামে একটি ফাইলে নিম্নলিখিত কোড যোগ করুন:

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

এই কোডটি ব্যাখ্যা করা যাক:

- প্রথমে, আমরা প্রয়োজনীয় লাইব্রেরিগুলি আমদানি করি, যার মধ্যে OpenAI লাইব্রেরি, dotenv লাইব্রেরি, requests লাইব্রেরি এবং Pillow লাইব্রেরি রয়েছে।

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- এরপর, আমরা _.env_ ফাইল থেকে পরিবেশ ভেরিয়েবলগুলি লোড করি।

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- তারপর, আমরা Azure OpenAI সার্ভিস ক্লায়েন্ট কনফিগার করি 

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- এরপর, আমরা ইমেজ তৈরি করি:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  উপরের কোডটি একটি JSON অবজেক্টের সাথে সাড়া দেয় যা তৈরি করা ইমেজের URL ধারণ করে। আমরা ইমেজটি ডাউনলোড করতে এবং একটি ফাইলে সংরক্ষণ করতে URL ব্যবহার করতে পারি।

- সর্বশেষে, আমরা ইমেজটি খুলে স্ট্যান্ডার্ড ইমেজ ভিউয়ার ব্যবহার করে এটি প্রদর্শন করি:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### ইমেজ তৈরি করার আরও বিস্তারিত

চলুন ইমেজ তৈরি করার কোডটি আরও বিস্তারিতভাবে দেখি:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, টেক্সট প্রম্পট যা ইমেজ তৈরি করতে ব্যবহৃত হয়। এই ক্ষেত্রে, আমরা প্রম্পট ব্যবহার করছি "ঘোড়ার উপর খরগোশ, ললিপপ ধরে আছে, কুয়াশাচ্ছন্ন মাঠে যেখানে ড্যাফোডিল জন্মায়"।
- **size**, তৈরি করা ইমেজের আকার। এই ক্ষেত্রে, আমরা 1024x1024 পিক্সেলের একটি ইমেজ তৈরি করছি।
- **n**, তৈরি করা ইমেজের সংখ্যা। এই ক্ষেত্রে, আমরা দুটি ইমেজ তৈরি করছি।
- **temperature**, একটি প্যারামিটার যা জেনারেটিভ AI মডেলের আউটপুটের র্যান্ডমনেস নিয়ন্ত্রণ করে। টেম্পারেচার 0 থেকে 1 এর মধ্যে একটি মান যেখানে 0 মানে আউটপুট নির্ধারিত এবং 1 মানে আউটপুট র্যান্ডম। ডিফল্ট মান 0.7।

ইমেজের সাথে আরও অনেক কিছু করা যায় যা আমরা পরবর্তী বিভাগে আলোচনা করব।

## ইমেজ জেনারেশনের অতিরিক্ত ক্ষমতা

আপনি এখন পর্যন্ত দেখেছেন কীভাবে আমরা পাইথনে কয়েকটি লাইনের মাধ্যমে একটি ইমেজ তৈরি করতে সক্ষম হয়েছি। তবে, ইমেজের সাথে আরও অনেক কিছু করা যায়।

আপনি নিম্নলিখিত কাজগুলোও করতে পারেন:

- **সম্পাদনা করুন**। একটি বিদ্যমান ইমেজ, একটি মাস্ক এবং একটি প্রম্পট প্রদান করে, আপনি একটি ইমেজ পরিবর্তন করতে পারেন। উদাহরণস্বরূপ, আপনি একটি ইমেজের একটি অংশে কিছু যোগ করতে পারেন। আমাদের খরগোশের ইমেজ কল্পনা করুন, আপনি খরগোশের মাথায় একটি টুপি যোগ করতে পারেন। এটি করার জন্য আপনাকে ইমেজ, একটি মাস্ক (পরিবর্তনের জন্য অংশটি চিহ্নিত করে) এবং একটি টেক্সট প্রম্পট প্রদান করতে হবে যা কী করা উচিত তা বলে। 
> নোট: এটি DALL-E 3-এ সমর্থিত নয়। 
 
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

  বেস ইমেজটি শুধুমাত্র পুল সহ লাউঞ্জটি ধারণ করবে কিন্তু চূড়ান্ত ইমেজে একটি ফ্লেমিঙ্গো থাকবে:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.bn.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.bn.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.bn.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **ভ্যারিয়েশন তৈরি করুন**। ধারণাটি হল আপনি একটি বিদ্যমান ইমেজ নেন এবং অনুরোধ করেন যে ভিন্ন ভিন্ন সংস্করণ তৈরি করা হয়। একটি ভ্যারিয়েশন তৈরি করতে, আপনি একটি ইমেজ এবং একটি টেক্সট প্রম্পট প্রদান করেন এবং কোডটি নিম্নরূপ:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > নোট, এটি শুধুমাত্র OpenAI-এ সমর্থিত

## টেম্পারেচার

টেম্পারেচার একটি প্যারামিটার যা জেনারেটিভ AI মডেলের আউটপুটের র্যান্ডমনেস নিয়ন্ত্রণ করে। টেম্পারেচার 0 থেকে 1 এর মধ্যে একটি মান যেখানে 0 মানে আউটপুট নির্ধারিত এবং 1 মানে আউটপুট র্যান্ডম। ডিফল্ট মান 0.7।

চলুন একটি উদাহরণ দেখি কীভাবে টেম্পারেচার কাজ করে, এই প্রম্পটটি দুইবার চালিয়ে:

> প্রম্পট: "ঘোড়ার উপর খরগোশ, ললিপপ ধরে আছে, কুয়াশাচ্ছন্ন মাঠে যেখানে ড্যাফোডিল জন্মায়"

![ঘোড়ার উপর ললিপপ ধরে থাকা খরগোশ, সংস্করণ 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.bn.png)

এখন একই প্রম্পটটি চালিয়ে দেখি যে আমরা একই ইমেজ দুইবার পাই না:

![ঘোড়ার উপর খরগোশের তৈরি ইমেজ](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.bn.png)

আপনি দেখতে পাচ্ছেন, ইমেজগুলো একই রকম, কিন্তু একেবারে এক নয়। এবার টেম্পারেচার মান 0.1-এ পরিবর্তন করে দেখি কী ঘটে:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### টেম্পারেচার পরিবর্তন করা

তাহলে চলুন প্রতিক্রিয়াকে আরও নির্ধারিত করার চেষ্টা করি। আমরা যে দুটি ইমেজ তৈরি করেছি তা থেকে পর্যবেক্ষণ করতে পারি যে প্রথম ইমেজে একটি খরগোশ আছে এবং দ্বিতীয় ইমেজে একটি ঘোড়া আছে, তাই ইমেজগুলো অনেকটা ভিন্ন।

তাহলে আমাদের কোড পরিবর্তন করে টেম্পারেচার 0 সেট করি, যেমন:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

এখন আপনি এই কোডটি চালালে, আপনি এই দুটি ইমেজ পাবেন:

- ![টেম্পারেচার 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.bn.png)
- ![টেম্পারেচার 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.bn.png)

এখানে আপনি স্পষ্টভাবে দেখতে পারেন কীভাবে ইমেজগুলো আরও বেশি একে অপরের সাথে সাদৃশ্যপূর্ণ।

## মেটাপ্রম্পট দিয়ে আপনার অ্যাপ্লিকেশনের সীমা নির্ধারণ করার উপায়

আমাদের ডেমো দিয়ে, আমরা ইতিমধ্যে আমাদের ক্লায়েন্টদের জন্য ইমেজ তৈরি করতে পারি। তবে, আমাদের অ্যাপ্লিকেশনের জন্য কিছু সীমা তৈরি করতে হবে।

উদাহরণস্বরূপ, আমরা এমন ইমেজ তৈরি করতে চাই না যা কাজের জন্য নিরাপদ নয় বা যা শিশুদের জন্য উপযুক্ত নয়।

আমরা এটি _মেটাপ্রম্পট_ দিয়ে করতে পারি। মেটাপ্রম্পট হল টেক্সট প্রম্পট যা জেনারেটিভ AI মডেলের আউটপুট নিয়ন্ত্রণ করতে ব্যবহৃত হয়। উদাহরণস্বরূপ, আমরা মেটাপ্রম্পট ব্যবহার করে আউটপুট নিয়ন্ত্রণ করতে পারি এবং নিশ্চিত করতে পারি যে তৈরি করা ইমেজগুলো কাজের জন্য নিরাপদ বা শিশুদের জন্য উপযুক্ত।

### এটি কীভাবে কাজ করে?

তাহলে, মেটাপ্রম্পট কীভাবে কাজ করে?

মেটাপ্রম্পট হল টেক্সট প্রম্পট যা জেনারেটিভ AI মডেলের আউটপুট নিয়ন্ত্রণ করতে ব্যবহৃত হয়, এগুলো টেক্সট প্রম্পটের আগে অবস্থান করে এবং মডেলের আউটপুট নিয়ন্ত্রণ করতে ব্যবহৃত হয় এবং মডেলের আউটপুট নিয়ন্ত্রণ করতে অ্যাপ্লিকেশনে এম্বেড করা হয়। প্রম্পট ইনপুট এবং মেটাপ্রম্পট ইনপুটকে একটি একক টেক্সট প্রম্পটে আবদ্ধ করে।

একটি মেটাপ্রম্পটের একটি উদাহরণ হতে পারে নিম্নলিখিত:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

এখন, চলুন দেখি কীভাবে আমরা আমাদের ডেমোতে মেটাপ্রম্পট ব্যবহার করতে পারি।

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

উপরের প্রম্পট থেকে, আপনি দেখতে পারেন কীভাবে তৈরি করা সমস্ত ইমেজ মেটাপ্রম্পট বিবেচনা করে।

## অ্যাসাইনমেন্ট - শিক্ষার্থীদের সক্ষম করুন

আমরা এই পাঠের শুরুতে Edu4All পরিচয় করিয়েছি। এখন সময় এসেছে শিক্ষার্থীদের তাদের মূল্যায়নের জন্য ইমেজ তৈরি করতে সক্ষম করার।

শিক্ষার্থীরা তাদের মূল্যায়নের জন্য স্মৃতিস্তম্ভের ইমেজ তৈরি করবে, ঠিক কোন স্মৃতিস্তম্ভ তা শিক্ষার্থীদের উপর নির্ভর করবে। শিক্ষার্থীদের এই কাজে তাদের সৃজনশীলতা ব্যবহার করতে বলা হয়েছে যাতে তারা বিভিন্ন প্রেক্ষাপটে এই স্মৃতিস্তম্ভগুলো স্থাপন করতে পারে।

## সমাধান

এখানে একটি সম্ভাব্য সমাধান:
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

## চমৎকার কাজ! আপনার শেখা চালিয়ে যান

এই পাঠটি সম্পন্ন করার পর, আমাদের [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) দেখুন, যাতে আপনার Generative AI জ্ঞানের স্তর আরও উন্নত করতে পারেন!

পাঠ ১০-এ যান, যেখানে আমরা দেখব কীভাবে [কম-কোড ব্যবহার করে AI অ্যাপ্লিকেশন তৈরি করা যায়](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী থাকব না।