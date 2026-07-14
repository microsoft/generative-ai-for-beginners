# টেক্সট জেনারেশন অ্যাপ্লিকেশন তৈরি করা

[![টেক্সট জেনারেশন অ্যাপ্লিকেশন তৈরি করা](../../../translated_images/bn/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(এই লেসনের ভিডিও দেখতে উপরের ছবিতে ক্লিক করুন)_

আপনি এখন পর্যন্ত এই কারিকুলামের মাধ্যমে দেখেছেন যে প্রম্পটের মতো মূল ধারণাগুলো এবং এমনকি "প্রম্পট ইঞ্জিনিয়ারিং" নামের একটি সম্পূর্ণ শৃঙ্খলাও রয়েছে। আপনি যেমন টুলসের সাথে ইন্টারঅ্যাক্ট করতে পারেন যেমন ChatGPT, Office 365, Microsoft Power Platform এবং আরও অনেক কিছু, সেগুলো প্রম্পট ব্যবহার করে কিছু অর্জন করতে সাহায্য করে।

একটি অ্যাপে এমন অভিজ্ঞতা যোগ করতে, আপনাকে প্রম্পট, কমপ্লিশন-এর মতো ধারণাগুলো বুঝতে হবে এবং কাজ করার জন্য একটি লাইব্রেরি বেছে নিতে হবে। ঠিক এইটাই আপনি এই অধ্যায়ে শিখবেন।

## ভূমিকা

এই অধ্যায়ে, আপনি:

- openai লাইব্রেরি এবং এর মূল ধারণাগুলো সম্পর্কে জানবেন।
- openai ব্যবহার করে একটি টেক্সট জেনারেশন অ্যাপ তৈরি করবেন।
- টেক্সট জেনারেশন অ্যাপ তৈরি করতে প্রম্পট, তাপমাত্রা, এবং টোকেনের মতো ধারণাগুলো কিভাবে ব্যবহার করবেন তা বুঝবেন।

## শেখার লক্ষ্যসমূহ

এই লেসনের শেষে, আপনি সক্ষম হবেন:

- একটি টেক্সট জেনারেশন অ্যাপ কী তা ব্যাখ্যা করতে।
- openai ব্যবহার করে একটি টেক্সট জেনারেশন অ্যাপ তৈরি করতে।
- আপনার অ্যাপকে কনফিগার করতে যাতে বেশি বা কম টোকেন ব্যবহার করা যায় এবং তাপমাত্রাও পরিবর্তন করা যায়, যা ভিন্ন আউটপুট দেয়।

## টেক্সট জেনারেশন অ্যাপ কী?

সাধারণত যখন আপনি একটি অ্যাপ তৈরি করেন, তখন তার কিছু ধরণের ইন্টারফেস থাকে যেমন নিম্নরূপ:

- কমান্ড-ভিত্তিক। কনসোল অ্যাপগুলো সাধারণত এমন অ্যাপ যেখানে আপনি একটি কমান্ড টাইপ করেন এবং এটি একটি কাজ সম্পন্ন করে। উদাহরণস্বরূপ, `git` একটি কমান্ড-ভিত্তিক অ্যাপ।
- ব্যবহারকারী ইন্টারফেস (UI)। কিছু অ্যাপের গ্রাফিকাল ইউজার ইন্টারফেস (GUI) থাকে যেখানে আপনি বোতামে ক্লিক করেন, টেক্সট ইনপুট করেন, বিকল্প নির্বাচন করেন এবং আরও অনেক কিছু।

### কনসোল ও UI অ্যাপগুলো সীমাবদ্ধ

এটি একটি কমান্ড-ভিত্তিক অ্যাপের সাথে তুলনা করুন যেখানে আপনি একটি কমান্ড টাইপ করেন:

- **এটি সীমাবদ্ধ**। আপনি যে কোনও কমান্ড টাইপ করতে পারবেন না, শুধু সেই গুলো যা অ্যাপ সমর্থন করে।
- **ভাষা নির্দিষ্ট**। কিছু অ্যাপ অনেক ভাষা সমর্থন করে, তবে ডিফল্টভাবে অ্যাপটি একটি নির্দিষ্ট ভাষার জন্য তৈরি হয়, যদিও আপনি আরও ভাষা সমর্থন যোগ করতে পারেন।

### টেক্সট জেনারেশন অ্যাপের সুবিধাসমূহ

তাহলে টেক্সট জেনারেশন অ্যাপটি কিভাবে আলাদা?

একটি টেক্সট জেনারেশন অ্যাপে আপনার বেশি নমনীয়তা থাকে, আপনি একটি নির্দিষ্ট কমান্ডের সেট বা নির্দিষ্ট ইনপুট ভাষার সাথে সীমাবদ্ধ নন। পরিবর্তে, আপনি প্রকৃত ভাষা ব্যবহার করে অ্যাপের সাথে ইন্টারঅ্যাক্ট করতে পারেন। আরেকটি সুবিধা হচ্ছে আপনি এমন একটি ডেটা সোর্সের সাথে কাজ করছেন যা অনেক বড় তথ্যভান্ডারের উপর প্রশিক্ষিত, যেখানে ঐতিহ্যগত অ্যাপটি ডেটাবেসে যেই তথ্য আছে শুধু তাই সীমাবদ্ধ থাকতে পারে।

### আমি টেক্সট জেনারেশন অ্যাপ দিয়ে কী কী তৈরি করতে পারি?

অনেক কিছু তৈরি করা যায়। উদাহরণস্বরূপ:

- **একটি চ্যাটবট**। আপনার কোম্পানি এবং তার পণ্য সম্পর্কে প্রশ্নের উত্তর দেয় এমন চ্যাটবট ভালো একটি উদাহরণ হতে পারে।
- **সহকারী**। LLM গুলো যেমন টেক্সট সংক্ষেপণ, টেক্সট থেকে তথ্য আহরণ, রিজিউমে প্রস্তুত করা ইত্যাদিতে দারুণ।
- **কোড সহকারী**। আপনি যে ভাষার মডেল ব্যবহার করেন তার উপর নির্ভর করে, আপনি একটি কোড সহকারী তৈরি করতে পারেন যা কোড লেখায় সাহায্য করে। উদাহরণস্বরূপ, আপনি GitHub Copilot বা ChatGPT ব্যবহার করে কোড লেখা সাহায্য নিতে পারেন।

## আমি কিভাবে শুরু করব?

ঠিক আছে, আপনাকে একটি LLM এর সাথে ইন্টিগ্রেট করার উপায় খুঁজে বের করতে হবে যা সাধারণত নিম্নলিখিত দুটি পদ্ধতির অংশ:

- একটি API ব্যবহার করুন। এখানে আপনি আপনার প্রম্পট দিয়ে ওয়েব রিকোয়েস্ট তৈরি করেন এবং জেনারেটেড টেক্সট ফেরত পান।
- একটি লাইব্রেরি ব্যবহার করুন। লাইব্রেরিগুলো API কলগুলোকে এনক্যাপসুলেট করে এবং ব্যবহার সহজ করে তোলে।

## লাইব্রেরি/SDKs

LLM নিয়ে কাজ করার জন্য কিছু পরিচিত লাইব্রেরি রয়েছে:

- **openai**, এই লাইব্রেরি আপনার মডেলের সাথে সংযোগ করা এবং প্রম্পট পাঠানো সহজ করে।

এরপর আরও উচ্চস্তরের লাইব্রেরি রয়েছে:

- **Langchain**। Langchain জনপ্রিয় এবং Python সমর্থন করে।
- **Semantic Kernel**। Semantic Kernel হলো Microsoft এর একটি লাইব্রেরি, যা C#, Python, এবং Java ভাষাগুলো সমর্থন করে।

## openai ব্যবহার করে প্রথম অ্যাপ

চলুন দেখি কিভাবে প্রথম অ্যাপ তৈরি করবেন, কী লাইব্রেরি দরকার, কতটা দরকার ইত্যাদি।

### openai ইনস্টল করা

OpenAI বা Azure OpenAI এর সাথে ইন্টারঅ্যাক্ট করার জন্য অনেক লাইব্রেরি পাওয়া যায়। আপনি C#, Python, JavaScript, Java ইত্যাদি বিভিন্ন প্রোগ্রামিং ভাষাও ব্যবহার করতে পারেন। আমরা `openai` Python লাইব্রেরি ব্যবহারের সিদ্ধান্ত নিয়েছি, তাই `pip` দিয়ে এটি ইনস্টল করব।

```bash
pip install openai
```

### একটি রিসোর্স তৈরি করুন

আপনাকে নিম্নলিখিত ধাপগুলো অনুসরণ করতে হবে:

- Azure এ একটি অ্যাকাউন্ট তৈরি করুন [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)।
- Azure OpenAI এর জন্য অ্যাক্সেস নিন। যান [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) এবং অ্যাক্সেসের জন্য আবেদন করুন।

  > [!NOTE]
  > লেখার সময়ে, আপনাকে Azure OpenAI এর জন্য অ্যাক্সেসের আবেদন করতে হবে।

- Python ইনস্টল করুন <https://www.python.org/>
- একটি Azure OpenAI Service রিসোর্স তৈরি করেছেন। কীভাবে [রিসোর্স তৈরি করবেন](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst) এই গাইডটি দেখুন।

### API কী এবং endpoint খুঁজে বের করা

এই মুহূর্তে, আপনাকে আপনার `openai` লাইব্রেরিকে বলা দরকার কোন API কী ব্যবহার করবে। API কী জানতে, আপনার Azure OpenAI রিসোর্সের "Keys and Endpoint" সেকশনে যান এবং "Key 1" মানটি কপি করুন।

![Azure Portal এ Keys and Endpoint রিসোর্স ব্লেড](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

এখন যেহেতু আপনি এই তথ্য কপি করে নিয়েছেন, লাইব্রেরিগুলোকে এটি ব্যবহার করতে বলুন।

> [!NOTE]
> আপনার API কী কোড থেকে আলাদা রাখা ভাল। আপনি পরিবেশ ভেরিয়েবল ব্যবহার করে এটা করতে পারেন।
>
> - পরিবেশ ভেরিয়েবল `OPENAI_API_KEY` আপনার API কী হিসেবে সেট করুন।
>   `export OPENAI_API_KEY='sk-...'`

### Azure কনফিগারেশন সেটআপ

আপনি যদি Azure OpenAI ব্যবহার করেন (এখন এটি Microsoft Foundry এর অংশ), তাহলে কীভাবে কনফিগারেশন করবেন, সেটা এখানে দেয়া হলো। আমরা স্ট্যান্ডার্ড `OpenAI` ক্লায়েন্ট ব্যবহার করি যা Azure OpenAI `/openai/v1/` endpoint নির্দেশ করে, যা Responses API এর সাথে কাজ করে এবং কোন `api_version` লাগে না:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

উপরে আমরা নিচের গুলো সেট করছি:

- `api_key`, এটি আপনার Azure Portal বা Microsoft Foundry পোর্টালে পাওয়া API কী।
- `base_url`, এটি আপনার Foundry রিসোর্সের endpoint যার শেষে `/openai/v1/` যুক্ত আছে। স্টেবল v1 endpoint OpenAI এবং Azure OpenAI উভয়েই কাজ করে কোন `api_version` ম্যানেজমেন্ট ছাড়াই।

> [!NOTE] > `os.environ` পরিবেশ ভেরিয়েবল পড়তে ব্যবহৃত হয়। আপনি এটি `AZURE_OPENAI_API_KEY` এবং `AZURE_OPENAI_ENDPOINT` এর মতো পরিবেশ ভেরিয়েবল পড়ার জন্য ব্যবহার করতে পারেন। টার্মিনালে অথবা `dotenv` এর মত লাইব্রেরি ব্যবহার করে এই পরিবেশ ভেরিয়েবলগুলো সেট করুন।

## টেক্সট জেনারেট করা

টেক্সট জেনারেট করার উপায় হল Responses API এর `responses.create` মেথড ব্যবহার করা। এখানে একটি উদাহরণ:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # এটি আপনার মডেল ডিপ্লয়মেন্টের নাম
    input=prompt,
    store=False,
)
print(response.output_text)
```

উপরের কোডে, আমরা একটি রেসপন্স তৈরি করি এবং আমরা যে মডেল ব্যবহার করতে চাই এবং প্রম্পটটি পাঠাই। তারপর আমরা `response.output_text` দিয়ে জেনারেটেড টেক্সট প্রিন্ট করি।

### মাল্টি-টার্ন আলোচনা

Responses API একক টার্ন টেক্সট জেনারেশন এবং মাল্টি-টার্ন চ্যাটবট উভয়ের জন্য উপযুক্ত - আপনি `input` এ মেসেজের একটি তালিকা দেন যা একটি সংলাপ তৈরি করে:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

এই ফাংশনালিটির আরও বিস্তারিত আসন্ন কোনো অধ্যায়ে আলোচনা করা হবে।

## অনুশীলন - আপনার প্রথম টেক্সট জেনারেশন অ্যাপ

এখন আমরা শিখেছি কিভাবে openai সেটআপ এবং কনফিগার করতে হয়, সময় এসেছে আপনি আপনার প্রথম টেক্সট জেনারেশন অ্যাপ তৈরি করুন। আপনার অ্যাপ তৈরি করতে নিম্নলিখিত ধাপগুলি অনুসরণ করুন:

1. একটি ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন এবং openai ইনস্টল করুন:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > আপনি যদি Windows ব্যবহার করেন, তাহলে `source venv/bin/activate` এর পরিবর্তে `venv\Scripts\activate` টাইপ করুন।

   > [!NOTE]
   > আপনার Azure OpenAI কী পেতে যান [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), সেখানে `Open AI` সার্চ করুন, `Open AI resource` সিলেক্ট করুন এবং তারপর `Keys and Endpoint` থেকে `Key 1` কপি করুন।

1. একটি _app.py_ ফাইল তৈরি করুন এবং এতে নিম্নলিখিত কোড দিন:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # আপনার সম্পূর্ণকরণ কোড যোগ করুন
   prompt = "Complete the following: Once upon a time there was a"

   # Responses API ব্যবহার করে একটি অনুরোধ করুন
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # উত্তর প্রিন্ট করুন
   print(response.output_text)
   ```

   > [!NOTE]
   > আপনি যদি সাধারণ OpenAI ব্যবহার করেন (Azure নয়), তাহলে `client = OpenAI(api_key="<আপনার OpenAI কী এখানে দিন>")` ব্যবহার করুন (কোন `base_url` থাকবে না) এবং `gpt-4o-mini` এর মত মডেল নাম দিন ডিপ্লয়মেন্ট নামের পরিবর্তে।

   আপনি নিম্নলিখিত ফলাফলের মতো দেখতে পাবেন:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## বিভিন্ন প্রকারের প্রম্পট, বিভিন্ন কাজের জন্য

এখন আপনি দেখেছেন কীভাবে প্রম্পট ব্যবহার করে টেক্সট জেনারেট করবেন। আপনার একটি প্রোগ্রাম আছে যা চলছে এবং আপনি তা পরিবর্তন করে বিভিন্ন ধরনের টেক্সট তৈরি করতে পারেন।

বিভিন্ন কাজে প্রম্পট ব্যবহার করা যায়। উদাহরণস্বরূপ:

- **এক ধরনের টেক্সট জেনারেট করা**। উদাহরণস্বরূপ, আপনি একটি কবিতা, কোয়িজের জন্য প্রশ্ন ইত্যাদি তৈরি করতে পারেন।
- **তথ্য খুঁজে বের করা**। আপনি প্রম্পট ব্যবহার করে তথ্য খুঁজে পেতে পারেন, যেমন 'ওয়েব ডেভেলপমেন্টে CORS মানে কী?' এর মতো উদাহরণ।
- **কোড জেনারেট করা**। প্রম্পট ব্যবহার করে কোড জেনারেট করতে পারেন, যেমন ইমেইল যাচাই করার জন্য রেগুলার এক্সপ্রেশন তৈরি করা বা একটি সম্পূর্ণ প্রোগ্রাম, যেমন একটি ওয়েব অ্যাপ তৈরি করা।

## আরও ব্যবহারিক একটি উদাহরণ: রেসিপি জেনারেটর

ভাবুন আপনার বাড়িতে কিছু উপকরণ আছে এবং আপনি কিছু রান্না করতে চান। এর জন্য একটি রেসিপি দরকার। রেসিপি খুঁজতে আপনি সার্চ ইঞ্জিন ব্যবহার করতে পারেন বা একটি LLM ব্যবহার করতে পারেন।

আপনি নিম্নলিখিত প্রম্পট লিখতে পারেন:

> "নিম্নলিখিত উপকরণ দিয়ে একটি ডিশের জন্য ৫টি রেসিপি দেখাও: মুরগি, আলু এবং গাজর। প্রতিটি রেসিপির জন্য ব্যবহৃত সকল উপকরণ তালিকাভুক্ত করুন"

উপরের প্রম্পট অনুযায়ী, আপনি এমন একটি উত্তর পেতে পারেন:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 2 cloves garlic, minced
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
```

এই ফলাফল দারুণ, আমি কী রান্না করব তা জানি। এই পর্যায়ে, কার্যকর উন্নতি হতে পারে:

- আমি যা পছন্দ করি না বা এলার্জি আছে এমন উপকরণ বাদ দেওয়া।
- যদি বাড়িতে সব উপকরণ না থাকে, একটি শপিং লিস্ট তৈরি করা।

উপরের ক্ষেত্রে, আমরা অতিরিক্ত একটি প্রম্পট যোগ করি:

> "লطفاً রেসিপিগুলো থেকে রসুন বাদ দিন কারণ আমি তার প্রতি অ্যালার্জিক, এবং সেটার পরিবর্তে অন্য কিছু দিন। সেইসাথে, আমি বাড়িতে এখন মুরগি, আলু এবং গাজর আছে ধরে নিয়ে রেসিপিগুলোর জন্য একটি শপিং লিস্ট তৈরি করুন।"

এখন আপনার একটি নতুন ফলাফল আছে, যেমন:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano

Shopping List:
- Olive oil
- Onion
- Thyme
- Oregano
- Salt
- Pepper
```

এটি আপনার পাঁচটি রেসিপি, যেখানে রসুন নেই এবং আপনি একটি শপিং লিস্টও পেয়েছেন যা আপনার বাড়িতে যা আছে তা বিবেচনা করে।

## অনুশীলন - একটি রেসিপি জেনারেটর তৈরি করুন

এখন যেহেতু আমরা একটি সিনারিও প্লে করেছি, আসুন সেই অনুযায়ী কোড লিখি। জন্য, নিচের ধাপগুলো অনুসরণ করুন:

1. বিদ্যমান _app.py_ ফাইলটি সূচনা হিসেবে ব্যবহার করুন
1. `prompt` ভেরিয়েবলটি খুঁজে বের করুন এবং এর কোড নিচের মত পরিবর্তন করুন:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   এখন যদি আপনি কোড রান করেন, তাহলে কিছুদিন ফলাফল দেখতে পাবেন যা এরকম হতে পারে:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > মনে রাখবেন, আপনার LLM ননডিটারমিনিস্টিক, তাই আপনি প্রতি বার কোড চালানোর সময় ভিন্ন ফলাফল পেতে পারেন।

   দারুণ, আসুন দেখি আমরা কীভাবে উন্নতি করতে পারি। উন্নতির জন্য, আমরা চাই কোডটি নমনীয় হোক যেন রেসিপির সংখ্যা এবং উপকরণ পরিবর্তন করা যায়।

1. কোড নিম্নরূপ পরিবর্তন করুন:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # রেসিপির সংখ্যা এবং উপকরণগুলিকে প্রম্পটে অন্তর্ভুক্ত করুন
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   টেস্ট রান করার জন্য কোডটি এরকম দেখতে পারে:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### ফিল্টার এবং শপিং লিস্ট যোগ করে উন্নতি করুন

এখন আমাদের একটি কাজ করা অ্যাপ আছে যা রেসিপি তৈরি করতে সক্ষম এবং এটি নমনীয় কারণ এটি ইউজারের ইনপুট এর ওপর নির্ভর করে, রেসিপির সংখ্যা এবং ব্যবহৃত উপকরণ উভয়ের ক্ষেত্রেই।

আরও উন্নত করার জন্য, আমরা নিম্নলিখিত যোগ করতে চাই:

- **উপকরণ ফিল্টার করা**। আমরা এমন উপকরণ ফিল্টার করতে চাই যা আমরা পছন্দ করি না বা যার প্রতি আমাদের অ্যালার্জি আছে। এর জন্য, আমরা আমাদের বিদ্যমান প্রম্পট এ একটি ফিল্টার শর্ত যোগ করতে পারি এর শেষাংশে, যেমন:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  উপরে, আমরা প্রম্পটের শেষে `{filter}` যোগ করেছি এবং ব্যবহারকারীর কাছ থেকে ফিল্টার মান নিয়েছি।

  প্রোগ্রাম রান করার উদাহরণ ইনপুট এখন এরকম হতে পারে:

  ```output
  No of recipes (for example, 5): 3
  List of ingredients (for example, chicken, potatoes, and carrots): onion,milk
  Filter (for example, vegetarian, vegan, or gluten-free): no milk

  1. French Onion Soup

  Ingredients:

  -1 large onion, sliced
  -3 cups beef broth
  -1 cup milk
  -6 slices french bread
  -1/4 cup shredded Parmesan cheese
  -1 tablespoon butter
  -1 teaspoon dried thyme
  -1/4 teaspoon salt
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add beef broth, milk, thyme, salt, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Place french bread slices on soup bowls.
  5. Ladle soup over bread.
  6. Sprinkle with Parmesan cheese.

  2. Onion and Potato Soup

  Ingredients:

  -1 large onion, chopped
  -2 cups potatoes, diced
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add potatoes, vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Serve hot.

  3. Creamy Onion Soup

  Ingredients:

  -1 large onion, chopped
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper
  -1/4 cup all-purpose flour
  -1/2 cup shredded Parmesan cheese

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. In a small bowl, whisk together flour and Parmesan cheese until smooth.
  5. Add to soup and simmer for an additional 5 minutes, or until soup has thickened.
  ```

  যেমন আপনি দেখতে পাচ্ছেন, দুধ থাকা যেকোনো রেসিপি ফিল্টার আউট হয়েছে। কিন্তু যদি আপনি ল্যাকটোস অসহনীয় হন, আপনি চাইতে পারেন পনির থাকা রেসিপিও ফিল্টার করতে, তাই স্পষ্ট হওয়া দরকার।


- **একটি শপিং লিস্ট তৈরি করুন**। আমরা একটি শপিং লিস্ট তৈরি করতে চাই, আমাদের বাড়িতে যা রয়েছে তা বিবেচনা করে।

  এই কার্যকারিতার জন্য, আমরা হয় একটি প্রম্পটেই সব কিছু সমাধান করার চেষ্টা করতে পারি অথবা দুইটি প্রম্পটে বিভক্ত করতে পারি। চলুন দ্বিতীয় পদ্ধতি চেষ্টা করি। এখানে আমরা একটি অতিরিক্ত প্রম্পট যোগ করার পরামর্শ দিচ্ছি, কিন্তু সেটি কাজ করার জন্য, আমাদের প্রথম প্রম্পটের ফলাফলকে দ্বিতীয় প্রম্পটের প্রসঙ্গে যোগ করতে হবে।

  প্রথম প্রম্পট থেকে ফলাফল প্রদর্শন করা অংশটি কোডে খুঁজে বের করুন এবং নিচের কোডটি নিচে যোগ করুন:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # প্রতিক্রিয়া মুদ্রণ করুন
  print("Shopping list:")
  print(response.output_text)
  ```

  নিম্নলিখিত বিষয়গুলি লক্ষ্য করুন:

  ১। আমরা একটি নতুন প্রম্পট তৈরি করছি প্রথম প্রম্পটের ফলাফল নতুন প্রম্পটের সাথে যোগ করে:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  ১। আমরা একটি নতুন অনুরোধ করছি, তবে প্রথম প্রম্পটে আমরা কতগুলি টোকেন চাইছিলাম তা বিবেচনায় রেখে, তাই এবার আমরা বলছি `max_output_tokens` হল 1200।

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     এই কোডটি চালিয়ে আমরা এখন নিম্নলিখিত আউটপুট পাই:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## আপনার সেটআপ উন্নত করুন

এখন পর্যন্ত যা আমাদের আছে তা কাজ করে, কিন্তু আরও উন্নতির জন্য কিছু টুইক করা উচিত। আমাদের করণীয় কিছু বিষয় হলো:

- **সিক্রেটগুলো কোড থেকে আলাদা করুন**, যেমন API কী। সিক্রেটগুলো কোডে থাকা উচিত নয় এবং একটি নিরাপদ স্থানে সংরক্ষণ করা উচিত। সিক্রেটগুলো কোড থেকে আলাদা রাখতে, আমরা পরিবেশ ভেরিয়েবল এবং `python-dotenv` এর মতো লাইব্রেরি ব্যবহার করতে পারি যেগুলো ফাইল থেকে লোড করে। কোডে এটি কেমন দেখাবে তা এখানে দেওয়া হল:

  ১। একটি `.env` ফাইল তৈরি করুন নিচের বিষয়বস্তু সহ:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > লক্ষ্য করুন, Microsoft Foundry এর Azure OpenAI এর জন্য, নিম্নলিখিত পরিবেশ ভেরিয়েবলগুলো সেট করতে হবে:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     কোডে, পরিবেশ ভেরিয়েবলগুলো এভাবে লোড করবেন:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **টোকেন দৈর্ঘ্য সম্পর্কে একটি কথা**। আমাদের বিবেচনা করা উচিত কতগুলি টোকেন প্রয়োজন টেক্সট জেনারেট করতে যা আমরা চাই। টোকেনের জন্য মূল্য দিতে হয়, তাই যেখানে সম্ভব, টোকেনের সংখ্যা কম রাখা উচিত। উদাহরণস্বরূপ, কি আমরা প্রম্পট এমনভাবে বিন্যস্ত করতে পারি যাতে কম টোকেন ব্যবহার হয়?

  টোকেন পরিবর্তন করতে, আপনি `max_output_tokens` প্যারামিটার ব্যবহার করতে পারেন। উদাহরণস্বরূপ, যদি আপনি ১০০ টোকেন ব্যবহার করতে চান, তবে এভাবে করবেন:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **তাপমাত্রা নিয়ে পরীক্ষা-নিরীক্ষা করা**। তাপমাত্রা এখনো উল্লেখ করা হয়নি কিন্তু এটি আমাদের প্রোগ্রামের কর্মক্ষমতার জন্য একটি গুরুত্বপূর্ণ প্রসঙ্গ। তাপমাত্রার মান যত বেশি হবে আউটপুট তত বেশি এলোমেলো হবে। বিপরীতভাবে, তাপমাত্রা যত কম হবে আউটপুট তত বেশি পূর্বানুমেয় হবে। আপনার আউটপুটে পরিবর্তন চান কি না তা বিবেচনা করুন।

  তাপমাত্রা পরিবর্তন করতে, আপনি `temperature` প্যারামিটার ব্যবহার করতে পারেন। উদাহরণস্বরূপ, আপনি যদি ০.৫ তাপমাত্রা ব্যবহার করতে চান, তাহলে এভাবে করবেন:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > লক্ষ্য করুন, ১.০ এর কাছে যত বেশি কাছে, আউটপুট তত বেশি বৈচিত্র্যময় হবে।

## অ্যাসাইনমেন্ট

এই অ্যাসাইনমেন্টের জন্য, আপনি যা তৈরি করতে চান তা নির্বাচন করতে পারেন।

এখানে কিছু পরামর্শ দেওয়া হলো:

- রেসিপি জেনারেটর অ্যাপটি আরও উন্নত করতে টুইক করুন। তাপমাত্রা মান এবং প্রম্পট সমূহ নিয়ে খেলুন এবং দেখুন আপনি কী করতে পারেন।
- একটি "স্টাডি বাডি" তৈরি করুন। এই অ্যাপ একটি বিষয়, যেমন পাইথন সম্পর্কে প্রশ্নের উত্তর দিতে সক্ষম হওয়া উচিত, যেমন "পাইথনে একটি নির্দিষ্ট বিষয় কী?", অথবা আপনি প্রম্পট দিতে পারেন, যেমন "একটি নির্দিষ্ট বিষয়ে কোড দেখাও" ইত্যাদি।
- ইতিহাস বট, ইতিহাসকে জীবন্ত করে তুলুন, বটকে একটি নির্দিষ্ট ঐতিহাসিক চরিত্র হিসেবে নির্দেশ দিন এবং তার জীবন ও সময় সম্পর্কে প্রশ্ন করুন।

## সমাধান

### স্টাডি বাডি

নিচেরটিই একটি স্টার্টার প্রম্পট, দেখুন আপনি কীভাবে এটি ব্যবহার করতে পারেন এবং ইচ্ছামত টুইক করতে পারেন।

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### ইতিহাস বট

এখানে কিছু প্রম্পট রয়েছে যা আপনি ব্যবহার করতে পারেন:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## জ্ঞান যাচাইকরণ

তাপমাত্রার ধারণাটি কী করে?

১। এটি নিয়ন্ত্রণ করে আউটপুট কতটা এলোমেলো।
১। এটি নিয়ন্ত্রণ করে উত্তর কত বড় হবে।
১। এটি নিয়ন্ত্রণ করে কতগুলি টোকেন ব্যবহার হয়।

## 🚀 চ্যালেঞ্জ

অ্যাসাইনমেন্ট করার সময়, তাপমাত্রা পরিবর্তন করার চেষ্টা করুন, যেমন ০, ০.৫, এবং ১ সেট করুন। মনে রাখবেন ০ সবচেয়ে কম বৈচিত্র্যময় এবং ১ সবচেয়ে বেশি। আপনার অ্যাপের জন্য কোন মানটি সবচেয়ে ভালো কাজ করে?

## চমৎকার কাজ! আপনার শেখা চালিয়ে যান

এই পাঠ শেষ করার পর, আমাদের [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) দেখুন যাতে আপনার Generative AI জ্ঞান আরও উন্নত হয়!

লেসন ৭ এ যান যেখানে আমরা দেখব কিভাবে [চ্যাট অ্যাপ্লিকেশন বানাবেন](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->