<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:02:05+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "bn"
}
-->
# চিত্র তৈরির অ্যাপ্লিকেশন তৈরি করা

LLMs-এর আরও অনেক কিছু আছে যা কেবল টেক্সট তৈরি করা নয়। টেক্সট বর্ণনা থেকে চিত্র তৈরি করাও সম্ভব। চিত্রগুলিকে একটি মোডালিটি হিসাবে রাখা অনেক ক্ষেত্রে অত্যন্ত কার্যকর হতে পারে, যেমন MedTech, স্থাপত্য, পর্যটন, গেম ডেভেলপমেন্ট এবং আরও অনেক কিছু। এই অধ্যায়ে, আমরা দুটি সবচেয়ে জনপ্রিয় চিত্র তৈরির মডেল, DALL-E এবং Midjourney নিয়ে আলোচনা করব।

## পরিচিতি

এই পাঠে, আমরা আলোচনা করব:

- চিত্র তৈরি এবং কেন এটি কার্যকর।
- DALL-E এবং Midjourney, তারা কী এবং কীভাবে কাজ করে।
- আপনি কীভাবে একটি চিত্র তৈরির অ্যাপ তৈরি করবেন।

## শেখার লক্ষ্য

এই পাঠ শেষ করার পর, আপনি সক্ষম হবেন:

- একটি চিত্র তৈরির অ্যাপ্লিকেশন তৈরি করতে।
- মেটা প্রম্পট দিয়ে আপনার অ্যাপ্লিকেশনের সীমা নির্ধারণ করতে।
- DALL-E এবং Midjourney এর সাথে কাজ করতে।

## কেন একটি চিত্র তৈরির অ্যাপ্লিকেশন তৈরি করবেন?

চিত্র তৈরির অ্যাপ্লিকেশনগুলি জেনারেটিভ AI-এর ক্ষমতা অন্বেষণ করার একটি দুর্দান্ত উপায়। এগুলি ব্যবহার করা যেতে পারে, উদাহরণস্বরূপ:

- **চিত্র সম্পাদনা এবং সংশ্লেষণ**। আপনি চিত্র সম্পাদনা এবং চিত্র সংশ্লেষণের মতো বিভিন্ন ব্যবহারের জন্য চিত্র তৈরি করতে পারেন।

- **বিভিন্ন শিল্পে প্রয়োগ করা**। এগুলি Medtech, পর্যটন, গেম ডেভেলপমেন্ট এবং আরও অনেক কিছুর মতো বিভিন্ন শিল্পের জন্য চিত্র তৈরি করতে ব্যবহার করা যেতে পারে।

## দৃশ্য: Edu4All

এই পাঠের অংশ হিসাবে, আমরা আমাদের স্টার্টআপ, Edu4All-এর সাথে এই পাঠে কাজ চালিয়ে যাব। শিক্ষার্থীরা তাদের মূল্যায়নের জন্য চিত্র তৈরি করবে, কোন চিত্রগুলি তৈরি করতে হবে তা শিক্ষার্থীদের উপর নির্ভর করবে, তবে তারা তাদের নিজস্ব রূপকথার জন্য চিত্রণ তৈরি করতে পারে বা তাদের গল্পের জন্য একটি নতুন চরিত্র তৈরি করতে পারে বা তাদের ধারণা এবং ধারণাগুলি চিত্রিত করতে সহায়তা করতে পারে।

এখানে Edu4All-এর শিক্ষার্থীরা উদাহরণস্বরূপ কী তৈরি করতে পারে যদি তারা শ্রেণীকক্ষে স্মৃতিস্তম্ভ নিয়ে কাজ করে:

![Edu4All স্টার্টআপ, স্মৃতিস্তম্ভের ক্লাস, আইফেল টাওয়ার](../../../translated_images/startup.ec211d74fef9f4175010c3334942b715514230415744b9dd0a69a19f4ad68786.bn.png)

এমন একটি প্রম্পট ব্যবহার করে

> "সকালবেলার আলোতে আইফেল টাওয়ারের পাশে কুকুর"

## DALL-E এবং Midjourney কী?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) এবং [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) দুটি সবচেয়ে জনপ্রিয় চিত্র তৈরির মডেল, তারা আপনাকে প্রম্পট ব্যবহার করে চিত্র তৈরি করতে দেয়।

### DALL-E

চলুন শুরু করি DALL-E দিয়ে, যা একটি জেনারেটিভ AI মডেল যা টেক্সট বর্ণনা থেকে চিত্র তৈরি করে।

> [DALL-E দুটি মডেলের সংমিশ্রণ, CLIP এবং diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, একটি মডেল যা এম্বেডিং তৈরি করে, যা চিত্র এবং টেক্সট থেকে ডেটার সংখ্যাসূচক উপস্থাপনা।

- **Diffused attention**, একটি মডেল যা এম্বেডিং থেকে চিত্র তৈরি করে। DALL-E একটি চিত্র এবং টেক্সট ডেটাসেটে প্রশিক্ষিত এবং টেক্সট বর্ণনা থেকে চিত্র তৈরি করতে ব্যবহার করা যেতে পারে। উদাহরণস্বরূপ, DALL-E একটি টুপি পরা বিড়াল বা মোহক সহ একটি কুকুরের চিত্র তৈরি করতে ব্যবহার করা যেতে পারে।

### Midjourney

Midjourney DALL-E এর মতোই কাজ করে, এটি টেক্সট প্রম্পট থেকে চিত্র তৈরি করে। Midjourney, প্রম্পট ব্যবহার করে চিত্র তৈরি করতেও ব্যবহার করা যেতে পারে যেমন "একটি টুপি পরা বিড়াল", বা "মোহক সহ একটি কুকুর"।

![Midjourney দ্বারা তৈরি চিত্র, যান্ত্রিক কবুতর](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_চিত্র ক্রেডিট উইকিপিডিয়া, Midjourney দ্বারা তৈরি চিত্র_

## DALL-E এবং Midjourney কীভাবে কাজ করে

প্রথমে, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)। DALL-E একটি জেনারেটিভ AI মডেল যা _অটোরিগ্রেসিভ ট্রান্সফরমার_ সহ ট্রান্সফরমার আর্কিটেকচারের উপর ভিত্তি করে।

একটি _অটোরিগ্রেসিভ ট্রান্সফরমার_ সংজ্ঞায়িত করে কীভাবে একটি মডেল টেক্সট বর্ণনা থেকে চিত্র তৈরি করে, এটি একবারে একটি পিক্সেল তৈরি করে এবং তারপরে পরবর্তী পিক্সেল তৈরি করতে তৈরি পিক্সেলগুলি ব্যবহার করে। একটি নিউরাল নেটওয়ার্কের একাধিক স্তরের মধ্য দিয়ে যাওয়া, যতক্ষণ না চিত্রটি সম্পূর্ণ হয়।

এই প্রক্রিয়ার সাথে, DALL-E, চিত্রে এটি যে গুণাবলী, বস্তু, বৈশিষ্ট্য এবং আরও অনেক কিছু নিয়ন্ত্রণ করে। তবে, DALL-E 2 এবং 3 তৈরি চিত্রের উপর আরও বেশি নিয়ন্ত্রণ রয়েছে।

## আপনার প্রথম চিত্র তৈরির অ্যাপ্লিকেশন তৈরি করা

তাহলে একটি চিত্র তৈরির অ্যাপ্লিকেশন তৈরি করতে কী লাগে? আপনার নিম্নলিখিত লাইব্রেরিগুলির প্রয়োজন:

- **python-dotenv**, আপনার গোপনীয়তাগুলি কোড থেকে দূরে একটি _.env_ ফাইলে রাখতে এই লাইব্রেরিটি ব্যবহার করার জন্য আপনাকে অত্যন্ত সুপারিশ করা হয়।
- **openai**, এই লাইব্রেরি হল আপনি OpenAI API-এর সাথে যোগাযোগ করতে যা ব্যবহার করবেন।
- **pillow**, পাইথনে চিত্রের সাথে কাজ করতে।
- **requests**, আপনাকে HTTP অনুরোধ করতে সাহায্য করতে।

1. নিম্নলিখিত বিষয়বস্তু সহ একটি ফাইল _.env_ তৈরি করুন:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Azure Portal-এ আপনার রিসোর্সের জন্য "কী এবং এন্ডপয়েন্ট" বিভাগে এই তথ্যটি সন্ধান করুন।

1. উপরের লাইব্রেরিগুলি একটি _requirements.txt_ নামে একটি ফাইলে সংগ্রহ করুন যেমন:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. পরবর্তী, ভার্চুয়াল পরিবেশ তৈরি করুন এবং লাইব্রেরিগুলি ইনস্টল করুন:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows-এর জন্য, আপনার ভার্চুয়াল পরিবেশ তৈরি এবং সক্রিয় করতে নিম্নলিখিত কমান্ডগুলি ব্যবহার করুন:

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

এই কোড ব্যাখ্যা করা যাক:

- প্রথমে, আমরা প্রয়োজনীয় লাইব্রেরিগুলি আমদানি করি, যার মধ্যে OpenAI লাইব্রেরি, dotenv লাইব্রেরি, requests লাইব্রেরি এবং Pillow লাইব্রেরি রয়েছে।

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- পরবর্তী, আমরা _.env_ ফাইল থেকে পরিবেশ ভেরিয়েবলগুলি লোড করি।

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- তারপরে, আমরা OpenAI API-এর জন্য এন্ডপয়েন্ট, কী, সংস্করণ এবং প্রকার সেট করি।

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- পরবর্তী, আমরা চিত্রটি তৈরি করি:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  উপরের কোডটি একটি JSON অবজেক্টের সাথে সাড়া দেয় যা তৈরি করা চিত্রের URL ধারণ করে। আমরা চিত্রটি ডাউনলোড করতে এবং একটি ফাইলে সংরক্ষণ করতে URL ব্যবহার করতে পারি।

- সর্বশেষে, আমরা চিত্রটি খুলে স্ট্যান্ডার্ড চিত্র দর্শক ব্যবহার করে এটি প্রদর্শন করি:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### চিত্র তৈরি সম্পর্কে আরও বিশদ

চলুন চিত্র তৈরি করে এমন কোডটি আরও বিশদভাবে দেখি:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, হল টেক্সট প্রম্পট যা চিত্র তৈরি করতে ব্যবহৃত হয়। এই ক্ষেত্রে, আমরা "বনির উপর ঘোড়া, ললিপপ ধরে, কুয়াশাচ্ছন্ন মেঠো জমিতে যেখানে ড্যাফোডিল জন্মায়" প্রম্পট ব্যবহার করছি।
- **size**, হল তৈরি করা চিত্রের আকার। এই ক্ষেত্রে, আমরা 1024x1024 পিক্সেলের একটি চিত্র তৈরি করছি।
- **n**, হল তৈরি করা চিত্রের সংখ্যা। এই ক্ষেত্রে, আমরা দুটি চিত্র তৈরি করছি।
- **temperature**, একটি জেনারেটিভ AI মডেলের আউটপুটের এলোমেলোতা নিয়ন্ত্রণ করে এমন একটি প্যারামিটার। তাপমাত্রা 0 এবং 1 এর মধ্যে একটি মান যেখানে 0 মানে আউটপুট নির্ধারিত এবং 1 মানে আউটপুট এলোমেলো। ডিফল্ট মান হল 0.7।

আপনি চিত্রের সাথে আরও অনেক কিছু করতে পারেন যা আমরা পরবর্তী বিভাগে আলোচনা করব।

## চিত্র তৈরির অতিরিক্ত ক্ষমতা

আপনি এতক্ষণ দেখেছেন কিভাবে আমরা পাইথনে কয়েকটি লাইনের মাধ্যমে একটি চিত্র তৈরি করতে সক্ষম হয়েছি। তবে, আপনি চিত্রের সাথে আরও অনেক কিছু করতে পারেন।

আপনি নিম্নলিখিতগুলি করতে পারেন:

- **সম্পাদনা করুন**। একটি বিদ্যমান চিত্র, একটি মাস্ক এবং একটি প্রম্পট প্রদান করে, আপনি একটি চিত্র পরিবর্তন করতে পারেন। উদাহরণস্বরূপ, আপনি একটি চিত্রের একটি অংশে কিছু যোগ করতে পারেন। আমাদের বনির চিত্র কল্পনা করুন, আপনি বনির সাথে একটি টুপি যোগ করতে পারেন। আপনি কীভাবে এটি করবেন তা হল চিত্রটি প্রদান করা, একটি মাস্ক (পরিবর্তনের জন্য অংশটি চিহ্নিত করা) এবং একটি টেক্সট প্রম্পট যা কী করা উচিত তা বলতে।

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

  বেস ইমেজটিতে শুধুমাত্র খরগোশ থাকবে কিন্তু চূড়ান্ত চিত্রটিতে খরগোশের উপর টুপি থাকবে।

- **প্রকরণ তৈরি করুন**। ধারণাটি হল আপনি একটি বিদ্যমান চিত্র গ্রহণ করেন এবং প্রকরণগুলি তৈরি করার জন্য অনুরোধ করেন। একটি প্রকরণ তৈরি করতে, আপনি একটি চিত্র এবং একটি টেক্সট প্রম্পট প্রদান করেন এবং কোডটি এমনভাবে প্রদান করেন:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > নোট, এটি শুধুমাত্র OpenAI-এ সমর্থিত

## তাপমাত্রা

তাপমাত্রা একটি প্যারামিটার যা একটি জেনারেটিভ AI মডেলের আউটপুটের এলোমেলোতা নিয়ন্ত্রণ করে। তাপমাত্রা 0 এবং 1 এর মধ্যে একটি মান যেখানে 0 মানে আউটপুট নির্ধারিত এবং 1 মানে আউটপুট এলোমেলো। ডিফল্ট মান হল 0.7।

চলুন তাপমাত্রা কীভাবে কাজ করে তার একটি উদাহরণ দেখি, এই প্রম্পটটি দুবার চালিয়ে:

> প্রম্পট : "বনির উপর ঘোড়া, ললিপপ ধরে, কুয়াশাচ্ছন্ন মেঠো জমিতে যেখানে ড্যাফোডিল জন্মায়"

![বনির উপর ঘোড়া ললিপপ ধরে, সংস্করণ 1](../../../translated_images/v1-generated-image.208ba0525ed6ae505504aa852e28d334c0440e9931b7c97f9508176a22d2dd54.bn.png)

এখন আসুন একই প্রম্পটটি চালাই শুধু দেখার জন্য যে আমরা একই চিত্রটি দুবার পাব না:

![বনির উপর ঘোড়া তৈরি করা চিত্র](../../../translated_images/v2-generated-image.f0a88c05ef476e95f3682d4b21c9ba2f4807ae71cc29e9c05b42ebbf497cf61b.bn.png)

আপনি দেখতে পাচ্ছেন, চিত্রগুলি একই নয়, তবে অনুরূপ। আসুন তাপমাত্রার মান 0.1 পরিবর্তন করি এবং দেখি কী হয়:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### তাপমাত্রা পরিবর্তন করা

তাহলে আসুন প্রতিক্রিয়াটি আরও নির্ধারিত করার চেষ্টা করি। আমরা যে দুটি চিত্র তৈরি করেছি তা থেকে আমরা দেখতে পারি যে প্রথম চিত্রে একটি খরগোশ আছে এবং দ্বিতীয় চিত্রে একটি ঘোড়া আছে, তাই চিত্রগুলি খুব বেশি পরিবর্তিত হয়।

আসুন তাই আমাদের কোড পরিবর্তন করি এবং তাপমাত্রা 0 সেট করি, যেমন:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

এখন আপনি যখন এই কোডটি চালান, আপনি এই দুটি চিত্র পাবেন:

- ![তাপমাত্রা 0, v1](../../../translated_images/v1-temp-generated-image.d8557be792b5c81c2c6d2804cb7b210fe8b340106fe4ffcadf9cf7de1cd7b991.bn.png)
- ![তাপমাত্রা 0 , v2](../../../translated_images/v2-temp-generated-image.bd412fcfbd43379312b1382212a332aa311ca1a80ea692dea50a8b876a487c61.bn.png)

এখানে আপনি স্পষ্টভাবে দেখতে পারেন কিভাবে চিত্রগুলি একে অপরের সাথে আরও বেশি সাদৃশ্যপূর্ণ।

## মেটাপ্রম্পট দিয়ে আপনার অ্যাপ্লিকেশনের জন্য সীমা কীভাবে সংজ্ঞায়িত করবেন

আমাদের ডেমো দিয়ে, আমরা ইতিমধ্যে আমাদের ক্লায়েন্টদের জন্য চিত্র তৈরি করতে পারি। তবে, আমাদের অ্যাপ্লিকেশনের জন্য কিছু সীমা তৈরি করতে হবে।

উদাহরণস্বরূপ, আমরা এমন চিত্র তৈরি করতে চাই না যা কাজের জন্য নিরাপদ নয়, বা যা শিশুদের জন্য উপযুক্ত নয়।

আমরা এটি _মেটাপ্রম্পট_ দিয়ে করতে পারি। মেটাপ্রম্পটগুলি টেক্সট প্রম্পট যা একটি জেনারেটিভ AI মডেলের আউটপুট নিয়ন্ত্রণ করতে ব্যবহৃত হয়। উদাহরণস্বরূপ, আমরা মেটাপ্রম্পট ব্যবহার করতে পারি আউটপুট নিয়ন্ত্রণ করতে, এবং নিশ্চিত করতে যে তৈরি করা চিত্রগুলি কাজের জন্য নিরাপদ বা শিশুদের জন্য উপযুক্ত।

### এটি কীভাবে কাজ করে?

এখন, মেটা প্রম্পটগুলি কীভাবে কাজ করে?

মেটা প্রম্পটগুলি টেক্সট প্রম্পট যা একটি জেনারেটিভ AI মডেলের আউটপুট নিয়ন্ত্রণ করতে ব্যবহৃত হয়, তারা টেক্সট প্রম্পটের আগে অবস্থান করে এবং মডেলের আউটপুট নিয়ন্ত্রণ করতে ব্যবহৃত হয় এবং মডেলের আউটপুট নিয়ন্ত্রণ করতে অ্যাপ্লিকেশনগুলিতে এম্বেড করা হয়। প্রম্পট ইনপুট এবং মেটা প্রম্পট ইনপুটকে একক টেক্সট প্রম্পটে এনক্যাপসুলেট করা।

একটি মেটা প্রম্পটের একটি উদাহরণ হবে নিম্নলিখিত:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

এখন, আসুন দেখি কিভাবে আমাদের ডেমোতে মেটা প্রম্পট ব্যবহার করতে পারি।

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

উপরের প্রম্পট থেকে, আপনি দেখতে পাচ্ছেন কিভাবে তৈরি করা সমস্ত চিত্র মেটাপ্রম্পট বিবেচনা করে।

## অ্যাসাইনমেন্ট - আসুন শিক্ষার্থীদের সক্ষম করি

আমরা এই পাঠের শুরুতে Edu4All পরিচয় করিয়ে দিয়েছি। এখন সময় এসেছে শিক্ষার্থীদের তাদের মূল্যায়নের জন্য চিত্র তৈরি করতে সক্ষম করার।

শিক্ষার্থীরা তাদের মূল্যায়নের জন্য স্মৃতিস্তম্ভ সম্বলিত চিত্র তৈরি করবে, ঠিক কোন স্মৃতিস্তম্ভগুলি শিক্ষার্থীদের উপর নির্ভর করবে। শিক্ষার্থীদের এই কাজে তাদের সৃজনশীলতা ব্যবহার করতে বলা হয় এই স্মৃতিস্তম্ভগুলিকে বিভিন্ন প্রসঙ্গে স্থাপন করতে।

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

## চমৎকার কাজ! আপনার শেখা চালিয়ে যান

এই পাঠ শেষ করার পরে, আমাদের [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) দেখুন আপনার জেনারেটিভ AI জ্ঞানকে আরও উন্নত করতে!

Lesson 10 এ যান যেখানে আমরা [লো-কোড দিয়ে AI অ্যাপ্লিকেশন তৈরি করার](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) কথা বলব।

**অস্বীকৃতি**:  
এই নথিটি এআই অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে দয়া করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। এর মূল ভাষায় থাকা আসল নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।