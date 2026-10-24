# টেক্সট জেনারেশন অ্যাপ্লিকেশন তৈরি

[![টেক্সট জেনারেশন অ্যাপ্লিকেশন তৈরি](../../../translated_images/bn/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(এই পাঠের ভিডিও দেখতে উপরের চিত্রে ক্লিক করুন)_

এখন পর্যন্ত আপনি এই কারিকুলামের মাধ্যমে দেখেছেন যে প্রম্পটের মতো মূল ধারণাগুলো রয়েছে এবং এমনকি "প্রম্পট ইঞ্জিনিয়ারিং" নামে একটি পুরো ডিসিপ্লিনও আছে। অনেক টুল যেগুলোর সাথে আপনি ইন্টারঅ্যাক্ট করতে পারেন, যেমন ChatGPT, Office 365, Microsoft Power Platform ইত্যাদি, আপনাকে প্রম্পট ব্যবহার করে কিছু অর্জন করতে সাহায্য করে।

আপনাকে যদি এমন একটি অভিজ্ঞতা অ্যাপে যোগ করতে হয়, তাহলে আপনাকে প্রম্পট, কমপ্লিশন ইত্যাদি ধারণাগুলো বুঝতে হবে এবং কাজ করার জন্য একটি লাইব্রেরি নির্বাচন করতে হবে। এটাই আপনি এই অধ্যায়ে শিখবেন।

## পরিচিতি

এই অধ্যায়ে, আপনি:

- openai লাইব্রেরি এবং এর মূল ধারণাগুলো সম্পর্কে জানবেন।
- openai ব্যবহার করে একটি টেক্সট জেনারেশন অ্যাপ তৈরি করবেন।
- প্রম্পট, তাপমাত্রা, এবং টোকেনের মতো ধারণা ব্যবহার করে কিভাবে টেক্সট জেনারেশন অ্যাপ তৈরি করতে হয় বুঝবেন।

## শেখার লক্ষ্যসমূহ

এই পাঠের শেষে, আপনি সক্ষম হবেন:

- ব্যাখ্যা করতে টেক্সট জেনারেশন অ্যাপ কী।
- openai ব্যবহার করে একটি টেক্সট জেনারেশন অ্যাপ তৈরি করতে।
- আপনার অ্যাপে টোকেনের পরিমাণ বাড়ানো বা কমানো এবং তাপমাত্রা পরিবর্তন করে বিভিন্ন আউটপুট পাওয়া যায় এমনভাবে কনফিগার করতে।

## টেক্সট জেনারেশন অ্যাপ কী?

সাধারণত যখন আপনি একটি অ্যাপ তৈরি করেন, এতে কিছু ধরণের ইন্টারফেস থাকে যেমন নিচের মত:

- কমান্ড-ভিত্তিক। কনসোল অ্যাপগুলি সচরাচর অ্যাপ যেখানে আপনি একটি কমান্ড টাইপ করেন এবং এটি একটি কাজ সম্পন্ন করে। উদাহরণস্বরূপ, `git` একটি কমান্ড-ভিত্তিক অ্যাপ।
- ব্যবহারকারী ইন্টারফেস (UI)। কিছু অ্যাপে গ্রাফিক্যাল ইউজার ইন্টারফেস (GUI) থাকে যেখানে আপনি বাটনে ক্লিক করেন, টেক্সট ইনপুট দেন, অপশন নির্বাচন করেন ইত্যাদি।

### কনসোল এবং UI অ্যাপগুলোর সীমাবদ্ধতা

এটি একটি কমান্ড-ভিত্তিক অ্যাপের সাথে তুলনা করুন যেখানে আপনি একটি কমান্ড টাইপ করেন:

- **এটি সীমাবদ্ধ**। আপনি যেকোনো কমান্ড টাইপ করতে পারেন না, শুধুমাত্র যে কমান্ডগুলো অ্যাপ সমর্থন করে সেগুলোই টাইপ করতে পারেন।
- **ভাষা নির্দিষ্ট**। কিছু অ্যাপ অনেক ভাষাকে সমর্থন করে, কিন্তু ডিফল্ট হিসাবে অ্যাপটি একটি নির্দিষ্ট ভাষার জন্য তৈরি, যদিও আপনি আরো ভাষা যোগ করতে পারেন।

### টেক্সট জেনারেশন অ্যাপের সুবিধা

তাহলে টেক্সট জেনারেশন অ্যাপ কীভাবে আলাদা?

একটি টেক্সট জেনারেশন অ্যাপে, আপনার আরও নমনীয়তা থাকে, আপনি কমান্ডের একটি সেট বা নির্দিষ্ট ইনপুট ভাষায় সীমাবদ্ধ থাকেন না। পরিবর্তে, আপনি প্রাকৃতিক ভাষা ব্যবহার করে অ্যাপের সাথে ইন্টারঅ্যাক্ট করতে পারেন। আরেকটি সুবিধা হল আপনি ইতিমধ্যেই এমন একটি ডেটা সূত্রের সাথে ইন্টারঅ্যাক্ট করছেন যা বিশাল তথ্যভাণ্ডার থেকে প্রশিক্ষিত, যেখানে একটি প্রচলিত অ্যাপ হয়তো সীমাবদ্ধ যা ডেটাবেসে আছে।

### টেক্সট জেনারেশন অ্যাপ দিয়ে আমি কী তৈরি করতে পারি?

আপনি অনেক কিছু তৈরি করতে পারেন। উদাহরণস্বরূপ:

- **একটি চ্যাটবট**। একটি চ্যাটবট যা বিষয় সম্পর্কে প্রশ্নের উত্তর দেয়, যেমন আপনার কোম্পানি এবং এর পণ্যের বিষয়ে, একটা ভালো মিল হতে পারে।
- **সহায়ক**। LLM গুলো টেক্সট সারাংশ করা, টেক্সট থেকে তথ্য আহরণ, রেজুমে প্রভৃতি তৈরিতে ভালো।
- **কোড সহকারী**। আপনি যে ভাষার মডেল ব্যবহার করেন তার ওপর নির্ভর করে, আপনি একটি কোড সহকারী তৈরি করতে পারেন যা আপনাকে কোড লেখায় সাহায্য করে। উদাহরণস্বরূপ, আপনি GitHub Copilot এবং ChatGPT এর মতো পণ্য ব্যবহার করতে পারেন।

## কিভাবে শুরু করতে পারি?

ঠিক আছে, আপনাকে একটি LLM এর সাথে ইন্টিগ্রেট করার উপায় খুঁজে বের করতে হবে, যা সাধারণত নিচের দুইটি পন্থা অবলম্বন করে:

- API ব্যবহার করুন। এখানে আপনি আপনার প্রম্পট সহ ওয়েব রিকোয়েস্ট তৈরি করে জেনারেটেড টেক্সট ফিরে পাবেন।
- লাইব্রেরি ব্যবহার করুন। লাইব্রেরিগুলো API কলগুলো এনক্যাপসুলেট করে এবং ব্যবহার সহজ করে তোলে।

## লাইব্রেরি/SDK

LLM এর সাথে কাজ করার জন্য কিছু পরিচিত লাইব্রেরি আছে যেমন:

- **openai**, এই লাইব্রেরিটি আপনার মডেলের সাথে সংযোগ স্থাপন এবং প্রম্পট পাঠানো সহজ করে তোলে।

তারপর এমন লাইব্রেরি রয়েছে যা উচ্চতর পর্যায়ে কাজ করে যেমন:

- **Langchain**। Langchain খুব পরিচিত এবং Python সমর্থন করে।
- **Semantic Kernel**। Semantic Kernel হলো Microsoft এর একটি লাইব্রেরি যা C#, Python, এবং Java ভাষাগুলো সমর্থন করে।

## openai ব্যবহার করে প্রথম অ্যাপ

আসুন দেখি কিভাবে আমরা আমাদের প্রথম অ্যাপ তৈরি করতে পারি, কোন লাইব্রেরিগুলো দরকার, কতটুকু প্রয়োজন ইত্যাদি।

### openai ইনস্টল করুন

OpenAI বা Azure OpenAI-এর সাথে ইন্টারঅ্যাক্ট করার জন্য অনেক লাইব্রেরি উপলব্ধ। আপনি C#, Python, JavaScript, Java এবং আরও অনেক প্রোগ্রামিং ভাষা ব্যবহার করতে পারেন। আমরা Python লাইব্রেরি`openai` বেছে নিয়েছি, সুতরাং ইনস্টল করতে `pip` ব্যবহার করব।

```bash
pip install openai
```

### একটি রিসোর্স তৈরি করুন

আপনাকে নিম্নলিখিত পদক্ষেপগুলি অনুসরণ করতে হবে:

- Azure-তে একটি অ্যাকাউন্ট তৈরি করুন [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Azure OpenAI-তে অ্যাক্সেস পান। যান [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) এবং অ্যাক্সেসের জন্য আবেদন করুন।

  > [!NOTE]
  > লেখার সময় অনুযায়ী, আপনাকে Azure OpenAI-তে অ্যাক্সেসের জন্য আবেদন করতে হবে।

- Python ইনস্টল করুন <https://www.python.org/>
- একটি Azure OpenAI সার্ভিস রিসোর্স তৈরি করুন। কিভাবে [রিসোর্স তৈরি করবেন](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst সে গাইড দেখুন।

### API কী এবং এন্ডপয়েন্ট নির্ধারণ করুন

এই পর্যায়ে, আপনাকে আপনার `openai` লাইব্রেরিকে বলতে হবে কোন API কী ব্যবহার করতে হবে। আপনার API কী খুঁজে পেতে আপনার Azure OpenAI রিসোর্সের "Keys and Endpoint" বিভাগে যান এবং "Key 1" মানটি কপি করুন।

![Azure পোর্টালে Keys এবং Endpoint রিসোর্স ব্লেড](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

এখন যেহেতু আপনার কাছে এই তথ্য কপি করা আছে, আসুন লাইব্রেরিগুলোকে এটি ব্যবহারের নির্দেশ দিই।

> [!NOTE]
> আপনার API কী কোড থেকে আলাদা রাখা মূল্যবান। আপনি পরিবেশ ভেরিয়েবল ব্যবহার করে এটা করতে পারেন।
>
> - পরিবেশ ভেরিয়েবল `OPENAI_API_KEY` আপনার API কী-এ সেট করুন।
>   `export OPENAI_API_KEY='sk-...'`

### Azure কনফিগারেশন সেটআপ

আপনি যদি Azure OpenAI (এখন Microsoft Foundry-এর অংশ) ব্যবহার করেন, তাহলে কনফিগারেশন সেটআপ করার নিয়ম এখানে। আমরা স্ট্যান্ডার্ড `OpenAI` ক্লায়েন্ট ব্যবহার করি যা Azure OpenAI `/openai/v1/` এন্ডপয়েন্ট নির্দেশ করে, যা Responses API-র সাথে কাজ করে এবং কোন `api_version` দরকার হয় না:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

উপরে আমরা নিচেরগুলো সেট করছিলাম:

- `api_key`, এটি আপনার API কী যা Azure পোর্টাল অথবা Microsoft Foundry পোর্টাল থেকে পাওয়া যাবে।
- `base_url`, এটি আপনার Foundry রিসোর্স এন্ডপয়েন্ট যার সাথে `/openai/v1/` যুক্ত। স্টেবল v1 এন্ডপয়েন্ট OpenAI এবং Azure OpenAI উভয়ের জন্য কাজ করে এবং কোন `api_version` ব্যবস্থাপনা লাগে না।

> [!NOTE] > `os.environ` পরিবেশ ভেরিয়েবলগুলো পড়ে। আপনি এটি ব্যবহার করে `AZURE_OPENAI_API_KEY` এবং `AZURE_OPENAI_ENDPOINT` এর মতো পরিবেশ ভেরিয়েবল পড়তে পারেন। আপনার টার্মিনালে বা `dotenv` এর মত লাইব্রেরি ব্যবহার করে এই পরিবেশ ভেরিয়েবলগুলো সেট করুন।

## টেক্সট জেনারেট করুন

টেক্সট জেনারেট করার উপায় হল Responses API ব্যবহার করা `responses.create` মেথডের মাধ্যমে। এখানে একটি উদাহরণ:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

উপরের কোডে, আমরা একটি রেসপন্স তৈরি করছি এবং মডেল ও প্রম্পট পাস করছি। তারপর আমরা জেনারেটেড টেক্সট `response.output_text` এর মাধ্যমে প্রিন্ট করি।

### বহু-টান কথোপকথন

Responses API একক টার্ন টেক্সট জেনারেশন এবং বহু-টান চ্যাটবট উভয়ের জন্য উপযুক্ত - আপনি একটি কথোপকথন গঠনের জন্য `input`-এ মেসেজের একটি তালিকা প্রদান করেন:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

এই ফাংশনালিটির আরও বিস্তারিত একটি আসন্ন অধ্যায়ে আলোচনা করা হবে।

## অনুশীলন - আপনার প্রথম টেক্সট জেনারেশন অ্যাপ

এখন আমরা শিখেছি কিভাবে openai সেট আপ এবং কনফিগার করতে হয়, সময় এসেছে আপনার প্রথম টেক্সট জেনারেশন অ্যাপ তৈরি করার। তৈরি করার জন্য সেগুলো অনুসরণ করুন:

1. একটি ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন এবং openai ইনস্টল করুন:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > আপনি যদি Windows ব্যবহার করেন তবে `venv\Scripts\activate` টাইপ করুন `source venv/bin/activate` এর পরিবর্তে।

   > [!NOTE]
   > আপনার Azure OpenAI কী খুঁজে পেতে [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) যান, `Open AI` সear্চ করুন, তারপর `Open AI resource` নির্বাচন করুন, এরপর `Keys and Endpoint` নির্বাচন করুন এবং `Key 1` মান কপি করুন।

1. একটি _app.py_ ফাইল তৈরি করুন এবং নিচের কোড দিন:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"

   # make a request using the Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # print response
   print(response.output_text)
   ```

   > [!NOTE]
   > আপনি যদি সাধারণ OpenAI (Azure নয়) ব্যবহার করেন, তাহলে `client = OpenAI(api_key="<replace this value with your OpenAI key>")` ব্যবহার করুন (কোন `base_url` নয়) এবং একটি মডেল নাম যেমন `gpt-5-mini` পাস করুন ডিপ্লয়মেন্ট নামের পরিবর্তে।

   আপনি নিম্নলিখিত আউটপুট দেখতে পাবেন:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## বিভিন্ন ধরনের প্রম্পট, বিভিন্ন কাজের জন্য

এখন আপনি দেখেছেন কিভাবে প্রম্পট ব্যবহার করে টেক্সট জেনারেট করতে হয়। আপনার একটি কর্মরত প্রোগ্রামও আছে যা আপনি পরিবর্তন করে বিভিন্ন ধরনের টেক্সট জেনারেট করতে পারেন।

প্রম্পট বিভিন্ন ধরনের কাজের জন্য ব্যবহার করা যেতে পারে। উদাহরণস্বরূপ:

- **এক ধরণের টেক্সট তৈরি করুন**। উদাহরণস্বরূপ, আপনি কবিতা, কুইজের প্রশ্ন ইত্যাদি তৈরি করতে পারেন।
- **তথ্য অনুসন্ধান করুন**। আপনি প্রম্পট ব্যবহার করে তথ্য খুঁজতে পারেন যেমন "ওয়েব ডেভেলপমেন্টে CORS মানে কী?"।
- **কোড জেনারেট করুন**। আপনি প্রম্পট ব্যবহার করে কোড জেনারেট করতে পারেন, উদাহরণস্বরূপ ইমেইল সঠিকতা যাচাইয়ের জন্য একটি রেগুলার এক্সপ্রেশন তৈরি করা বা একটি সম্পূর্ণ প্রোগ্রাম যেমন একটি ওয়েব অ্যাপ তৈরি করা।

## একটি আরও ব্যবহারিক কেস: রেসিপি জেনারেটর

কল্পনা করুন, আপনার কাছে বাড়িতে উপকরণ আছে এবং আপনি কিছু রান্না করতে চান। এর জন্য আপনার একটি রেসিপি দরকার। রেসিপি খুঁজে পাওয়ার একটি উপায় হলো সার্চ ইঞ্জিন ব্যবহার করা অথবা আপনি একটি LLM ব্যবহার করতে পারেন।

আপনি নিচের মত একটি প্রম্পট লিখতে পারেন:

> "আমাকে নিম্নলিখিত উপকরণ দিয়ে একটি ডিশের ৫টি রেসিপি দেখান: মুরগি, আলু, এবং গাজর। প্রতিটি রেসিপির জন্য ব্যবহৃত সমস্ত উপকরণ তালিকাভুক্ত করুন"

উপরোক্ত প্রম্পট অনুযায়ী, আপনি নিম্নলিখিত রেসপন্স পেতে পারেন:

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

এই ফলাফল দারুণ, আমি জানতে পারছি কী রান্না করব। এখন, কোন উন্নতি সহায়ক হতে পারে তা হলো:

- এমন উপকরণ ফিল্টার করা যা আমি পছন্দ করি না অথবা যার প্রতি আমার এলার্জি আছে।
- একটি শপিং লিস্ট তৈরি করা, যদি আমার কাছে সব উপকরণ না থাকে।

উপরের ক্ষেত্রে, আমরা একটি অতিরিক্ত প্রম্পট যোগ করতে পারি:

> "অনুগ্রহ করে রেসিপিগুলো থেকে রসুন বাদ দিন কারণ আমার প্রতি এলার্জি আছে এবং এটি অন্য কিছুর সাথে প্রতিস্থাপন করুন। এছাড়া, রেসিপিগুলোর জন্য একটি শপিং লিস্ট তৈরি করুন, আমি ইতিমধ্যে মুরগি, আলু এবং গাজর আছে।"

এখন আপনার একটি নতুন ফলাফল থাকবে, অর্থাৎ:

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

এখানে আপনার পাঁচটি রেসিপি, রসুন বাদ দিয়ে এবং আপনার বাড়িতে যেগুলো আছে তা বিবেচনা করে একটি শপিং লিস্টও পেয়েছেন।

## অনুশীলন - একটি রেসিপি জেনারেটর তৈরি করুন

এখন আমরা একটি সিচুয়েশন প্লে আউট করেছি, আসুন কোড লিখে প্রদর্শিত সিচুয়েশন মেলান। এর জন্য নিচের ধাপগুলো অনুসরণ করুন:

1. বিদ্যমান _app.py_ ফাইলকে ধরা শুরু হিসাবে ব্যবহার করুন
1. `prompt` ভেরিয়েবলটি খুঁজে বের করুন এবং এর কোড নিচের মত পরিবর্তন করুন:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   এখন যদি কোড চালান, আপনি নিম্নলিখিত আউটপুট দেখতে পাবেন:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > মনে রাখবেন, আপনার LLM ননডিটারমিনিস্টিক, তাই প্রতি রান-এ ফলাফল ভিন্ন হতে পারে।

   দুর্দান্ত, আসুন দেখি কিভাবে আমরা উন্নতি করতে পারি। উন্নতির জন্য আমরা কোডটি নমনীয় করতে চাই যাতে উপকরণ এবং রেসিপির সংখ্যা পরিবর্তন এবং উন্নত করা যায়।

1. নিচের উপায়ে কোড পরিবর্তন করুন:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   কোড পরীক্ষা চালানোর জন্য এমন দেখতে পারে:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### ফিল্টার এবং শপিং লিস্ট যোগ করে উন্নতি করুন

এখন আমাদের একটি কাজের অ্যাপ রয়েছে যা রেসিপি তৈরি করতে পারে এবং এটি নমনীয় কারণ এটি ইউজারের ইনপুটের ওপর নির্ভর করে, যেমন রেসিপির সংখ্যা এবং ব্যবহৃত উপকরণ।

আরও উন্নতির জন্য, আমরা নিচেরগুলো যোগ করতে চাই:

- **উপকরণ ফিল্টার করুন**। আমরা এমন উপকরণ ফিল্টার করতে চাই যা আমাদের পছন্দ নয় বা যার প্রতি আমরা এলার্জিক। এই পরিবর্তনটি করতে আমরা আমাদের প্রম্পটের শেষে একটি ফিল্টার শর্ত যোগ করবো:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  আমরা প্রম্পটের শেষে `{filter}` যোগ করেছি এবং ইউজারের থেকে ফিল্টার ভ্যালু গ্রহন করছি।

  এখন প্রোগ্রাম চালানোর একটি উদাহরণ ইনপুট হতে পারে:

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

  আপনি দেখতে পাচ্ছেন, যেকোনো রেসিপি যেটিতে দুধ আছে তা ফিল্টার হয়েছে। কিন্তু আপনি যদি ল্যাক্টোজ ইনটলারেন্ট হন, তাহলে দুধজাতীয় খাদ্য যেমন পনিরও ফিল্টার করতে চাইতে পারেন, তাই স্পষ্ট হওয়া প্রয়োজন।

- **শপিং লিস্ট তৈরি করুন**। আমরা শপিং লিস্ট তৈরি করতে চাই যা বিবেচনা করবে আমাদের বাড়িতে ইতিমধ্যে কী আছে।

  এই ফাংশনালিটির জন্য, আমরা হয় সবকিছু এক প্রম্পটে সমাধান করার চেষ্টা করতে পারি অথবা এটিকে দুইটি প্রম্পটে ভাগ করতে পারি। চলুন দ্বিতীয় পন্থাটা চেষ্টা করি। এখানে আমরা একটি অতিরিক্ত প্রম্পট যোগ করার প্রস্তাব করছি, কিন্তু এর জন্য পূর্ববর্তী প্রম্পটের ফলাফলকে পরবর্তী প্রম্পটের প্রেক্ষাপট হিসেবে যোগ করতে হবে।

  কোডের সেই অংশ খুঁজুন যা প্রথম প্রম্পটের ফলাফল প্রিন্ট করে এবং নিচের কোডটি এর নীচে যোগ করুন:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  নিচের বিষয়গুলো লক্ষ্য করুন:

  1. আমরা একটি নতুন প্রম্পট তৈরি করছি পূর্বের প্রম্পট থেকে ফলাফল যোগ করে:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. আমরা নতুন একটি রিকোয়েস্ট পাঠাচ্ছি, কিন্তু প্রথম প্রম্পটে চাহিদা করা টোকেনের পরিমাণ বিবেচনা করে, এবার `max_output_tokens` হল 1200।

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     এই কোড চালানোর পর, আমরা নিম্নলিখিত আউটপুট পাই:

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

এখন পর্যন্ত যা আমাদের কাছে রয়েছে তা হল কাজ করা কোড, তবে কিছু সামঞ্জস্য করা উচিত যা বিষয়গুলো আরও উন্নত করবে। কিছু বিষয় যা আমাদের করা উচিত তা হল:

- **গোপনীয় তথ্য কোড থেকে পৃথক করা**, যেমন API কী। গোপনীয় তথ্য কোডে থাকার উচিত নয় এবং সেগুলো অবশ্যই নিরাপদ স্থানে সংরক্ষণ করতে হবে। গোপনীয় তথ্য কোড থেকে আলাদা করার জন্য, আমরা পরিবেশগত ভেরিয়েবল এবং `python-dotenv` মতো লাইব্রেরি ব্যবহার করতে পারি যেগুলো ফাইল থেকে গোপনীয় তথ্য লোড করে। কোডে এটা কেমন দেখাবে তা নিম্নরূপ:

  1. নিম্নলিখিত বিষয়বস্তু সহ একটি `.env` ফাইল তৈরি করুন:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > লক্ষ্য করুন, Microsoft Foundry-র Azure OpenAI এর জন্য আপনাকে নিম্নলিখিত পরিবেশগত ভেরিয়েবলগুলো সেট করতে হবে:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     কোডে আপনি পরিবেশগত ভেরিয়েবলগুলো এভাবেই লোড করবেন:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **টোকেনের দৈর্ঘ্য সম্পর্কে একটি কথা**। আমাদের ভাবা উচিত আমরা কতগুলো টোকেন ব্যবহার করব প্রয়োজনীয় টেক্সট তৈরি করতে। টোকেন ব্যবহারে খরচ হয়, তাই সম্ভব হলে আমাদের টোকেন ব্যবহারে সাশ্রয়ী হওয়া উচিত। উদাহরণস্বরূপ, আমরা কি প্রম্পট এমনভাবে তৈরি করতে পারি যাতে কম টোকেন ব্যবহৃত হয়?

  টোকেন পরিবর্তন করতে, আপনি `max_output_tokens` প্যারামিটার ব্যবহার করতে পারেন। উদাহরণস্বরূপ, আপনি যদি ১০০ টোকেন ব্যবহার করতে চান, তাহলে করবেন:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **তাপমাত্রার সাথে পরীক্ষা-নিরীক্ষা করা**। তাপমাত্রা একটি বিষয় যা আমরা এখন পর্যন্ত উল্লেখ করিনি কিন্তু এটি আমাদের প্রোগ্রামের কর্মক্ষমতার জন্য একটি গুরুত্বপুর্ণ প্রসঙ্গ। তাপমাত্রার মান যত বেশি হবে আউটপুট তত বেশি এলোমেলো হবে। পুনরুদ্ধারে তাপমাত্রার মান কম হলে আউটপুট তত বেশি পূর্বানুমেয় হবে। বিবেচনা করুন আপনি আউটপুটে বৈচিত্র্য চান কিনা।

  তাপমাত্রা পরিবর্তনের জন্য আপনি `temperature` প্যারামিটার ব্যবহার করতে পারেন। উদাহরণস্বরূপ, আপনি যদি ০.৫ তাপমাত্রা ব্যবহার করতে চান, তাহলে করবেন:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > লক্ষ্য করুন, ১.০ এর কাছে যত বেশি কাছাকাছি, আউটপুট তত বেশি বৈচিত্র্যময় হবে।

- **যুক্তি মডেলগুলো `temperature` ব্যবহার করে না**। এটি ২০২৬ সালের একটি গুরুত্বপূর্ণ পরিবর্তন। Microsoft Foundry-র বর্তমান ও অবহেলিত নয় এমন মডেলগুলো হল **যুক্তি মডেল** (GPT-5 পরিবার, o-series) - এবং তারা **`temperature` বা `top_p` সমর্থন করে না** (এবং নয় `max_tokens`; পরিবর্তে `max_output_tokens` ব্যবহার করুন)। আপনি `temperature` পাঠালে `gpt-5-mini` এ "parameter not supported" ত্রুটি পাবেন। তাই তাপমাত্রার উপরের উদাহরণ চেষ্টা করতে, এমন একটি মডেল ব্যবহার করুন যা এখনও স্যাম্পলিং নিয়ন্ত্রণ সমর্থন করে - উদাহরণস্বরূপ একটি ওপেন **Llama** মডেল যেমন `Llama-3.3-70B-Instruct` যা [Microsoft Foundry মডেল ক্যাটালগ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) থেকে, Foundry Models / Azure AI Inference endpoint থেকে কল করা যায় (ঠিক যেমন `githubmodels-*` এর স্যাম্পলগুলো)। GPT-5-এর মত যুক্তি মডেলগুলোর জন্য আউটপুট পরিচালনা করা হয় ভিন্নভাবে:
  - **প্রম্পট ইঞ্জিনিয়ারিং** - স্পষ্ট নির্দেশাবলী, উদাহরণ এবং সংগঠিত আউটপুট (দেখুন পাঠ [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) যা স্যাম্পলিং নিয়ন্ত্রণের কাজ করে।
  - **যুক্তি নিয়ন্ত্রণ** - যুক্তির প্রচেষ্টা/বিবরণীর মতো প্যারামিটারগুলো যুক্তির গভীরতা, বিলম্ব এবং খরচের মধ্যে ভারসাম্য করে।

  সংক্ষেপে: `temperature`/`top_p` এখনও অনেক মডেলে বৈধ (Llama, Mistral, Phi, এবং GPT-4.x পরিবার - যদিও GPT-4.x অবমুক্ত হচ্ছে), কিন্তু চলমান দিকে ধাবিত হচ্ছে প্রম্পট ইঞ্জিনিয়ারিং + যুক্তি নিয়ন্ত্রণের দিকে GPT-5-এর মত যুক্তি মডেলগুলোর জন্য।

## অ্যাসাইনমেন্ট

এই অ্যাসাইনমেন্টের জন্য, আপনি যা বানাতে চান তা নির্বাচন করতে পারেন।

এখানে কিছু পরামর্শ দেওয়া হলো:

- রেসিপি জেনারেটর অ্যাপটিকে আরও উন্নত করতে সামান্য পরিবর্তন করুন। তাপমাত্রার মান এবং প্রম্পটের সাথে খেলুন এবং দেখুন আপনি কী তৈরি করতে পারেন।
- একটি "স্টাডি বাডি" তৈরি করুন। এই অ্যাপ একটি বিষয়ে প্রশ্নের উত্তর দিতে পারবে, উদাহরণস্বরূপ পাইটন সম্পর্কে। আপনি প্রম্পট রাখতে পারেন যেমন "পাইটন-এর একটি নির্দিষ্ট বিষয় কি?" বা এমন প্রম্পট যা বলে, আমাকে একটি নির্দিষ্ট বিষয়ে কোড দেখাও ইত্যাদি।
- ইতিহাস বট, ইতিহাসকে জীবন্ত করুন, বটকে নির্দেশ দিন ঐতিহাসিক কোনো চরিত্রের ভূমিকায় অভিনয় করতে এবং তার জীবন ও সময়কাল সম্পর্কে প্রশ্ন করুন।

## সমাধান

### স্টাডি বাডি

নিচে একটি প্রাথমিক প্রম্পট দেওয়া হলো, দেখুন কীভাবে আপনি এটি ব্যবহার করতে পারেন এবং আপনার পছন্দ অনুযায়ী পরিবর্তন করতে পারেন।

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### ইতিহাস বট

এখানে কিছু প্রম্পট দেওয়া হলো যা আপনি ব্যবহার করতে পারেন:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## জ্ঞান যাচাই

তাপমাত্রা ধারণাটি কী করে?

1. এটি আউটপুট কতটা এলোমেলো হবে তা নিয়ন্ত্রণ করে।
1. এটি প্রতিক্রিয়ার আকার নিয়ন্ত্রণ করে।
1. এটি কতগুলো টোকেন ব্যবহৃত হবে তা নিয়ন্ত্রণ করে।

## 🚀 চ্যালেঞ্জ

অ্যাসাইনমেন্টে কাজ করার সময় তাপমাত্রা পরিবর্তন করে দেখুন, ০, ০.৫, এবং ১ এ সেট করার চেষ্টা করুন। মনে রাখবেন ০ সবচেয়ে কম বৈচিত্র্যময় এবং ১ সবচেয়ে বেশি। আপনার অ্যাপের জন্য কোন মান সবচেয়ে ভাল কাজ করে?

## চমৎকার কাজ! আপনার শেখা চালিয়ে যান

এই পাঠ শেষ করার পর আমাদের [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) দেখুন যাতে করে আপনি আপনার Generative AI জ্ঞান আরও উন্নত করতে পারেন!

পাঠ ৭ এ যান যেখানে আমরা কিভাবে [চ্যাট অ্যাপ্লিকেশন তৈরি করতে হয়](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) তা দেখব!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->