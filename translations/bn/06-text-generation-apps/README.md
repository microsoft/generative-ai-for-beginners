# টেক্সট জেনারেশন অ্যাপ্লিকেশন তৈরি

[![টেক্সট জেনারেশন অ্যাপ্লিকেশন তৈরি](../../../translated_images/bn/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(এই পাঠের ভিডিও দেখতে উপরের ছবিতে ক্লিক করুন)_

এই পাঠক্রমে এখন পর্যন্ত আপনি দেখে এসেছেন যে মুল ধারণাগুলো যেমন প্রম্পট এবং এমনকি একটি পূর্ণাঙ্গ শাখা রয়েছে যার নাম "প্রম্পট ইঞ্জিনিয়ারিং"। অনেক সরঞ্জাম যেমন ChatGPT, Office 365, Microsoft Power Platform ইত্যাদি আপনাকে প্রম্পট ব্যবহার করে কাজ সম্পাদনে সাহায্য করে।

এ জাতীয় অভিজ্ঞতা একটি অ্যাপে যোগ করতে হলে আপনাকে প্রম্পট, কমপ্লিশন এর মত ধারণাগুলো বুঝতে হবে এবং কাজ করার জন্য একটি গ্রন্থাগার বেছে নিতে হবে। ঠিক এইটাই আপনি এই অধ্যায়ে শিখবেন।

## পরিচিতি

এই অধ্যায়ে আপনি:

- openai লাইব্রেরি ও এর মুল ধারণা সম্পর্কে জানতে পারবেন।
- openai ব্যবহার করে একটি টেক্সট জেনারেশন অ্যাপ তৈরি করতে পারবেন।
- প্রম্পট, তাপমাত্রা, ও টোকেন এর মত ধারণাগুলো কিভাবে ব্যবহার করে একটি টেক্সট জেনারেশন অ্যাপ নির্মাণ করা যায় তা বুঝতে পারবেন।

## শেখার লক্ষ্য

এই পাঠের শেষে আপনি সক্ষম হবেন:

- টেক্সট জেনারেশন অ্যাপ কি তা ব্যাখ্যা করতে।
- openai ব্যবহার করে একটি টেক্সট জেনারেশন অ্যাপ তৈরি করতে।
- আপনার অ্যাপকে বেশি বা কম টোকেন ব্যবহার করতে এবং তাপমাত্রা পরিবর্তন করে বৈচিত্র্যময় আউটপুট পেতে কনফিগার করতে।

## টেক্সট জেনারেশন অ্যাপ কী?

সাধারণত যখন আপনি একটি অ্যাপ তৈরি করেন, এর কিছু ধরণের ইন্টারফেস থাকে যেমন নিচের উদাহরণগুলো:

- কমান্ড-ভিত্তিক। কনসোল অ্যাপস সাধারণত এমন অ্যাপ যেখানে আপনি একটি কমান্ড টাইপ করেন এবং এটি একটি কাজ সম্পন্ন করে। উদাহরণস্বরূপ, `git` একটি কমান্ড-ভিত্তিক অ্যাপ।
- ব্যবহারকারী ইন্টারফেস (UI)। কিছু অ্যাপে গ্রাফিক্যাল ইউজার ইন্টারফেস (GUI) থাকে, যেখানে আপনি বাটনে ক্লিক করেন, টেক্সট ইনপুট দেন, অপশন নির্বাচন করেন ইত্যাদি।

### কনসোল ও UI অ্যাপ সীমিত

একটি কমান্ড-ভিত্তিক অ্যাপের সাথে তুলনা করুন যেখানে আপনি একটি কমান্ড টাইপ করেন:

- **এটি সীমিত**। আপনি যেকোনো কমান্ড টাইপ করতে পারবেন না, শুধুমাত্র যেগুলো অ্যাপ সমর্থন করে।
- **ভাষা নির্দিষ্ট**। কিছু অ্যাপ অনেক ভাষা সমর্থন করে, তবে ডিফল্ট হিসেবে অ্যাপটি একটি নির্দিষ্ট ভাষার জন্য তৈরি হয়, যদিও আপনি আরও ভাষা সমর্থন যোগ করতে পারেন।

### টেক্সট জেনারেশন অ্যাপের সুবিধা

তাহলে টেক্সট জেনারেশন অ্যাপ কিভাবে আলাদা?

একটি টেক্সট জেনারেশন অ্যাপে, আপনার আরও বেশি নমনীয়তা আছে, আপনি নির্দিষ্ট কিছু কমান্ড বা নির্দিষ্ট ইনপুট ভাষায় সীমাবদ্ধ নন। পরিবর্তে, আপনি প্রাকৃতিক ভাষা ব্যবহার করে অ্যাপের সাথে যোগাযোগ করতে পারেন। আরেকটি সুবিধা হলো, আপনি ইতিমধ্যেই এমন একটি তথ্য উৎসের সাথে যোগাযোগ করছেন যা একটি বিশাল তথ্যভাণ্ডারে প্রশিক্ষিত, যেখানে একটি প্রচলিত অ্যাপ হয়তো ডাটাবেসের মধ্যে থাকা কিছুর মধ্যেই সীমাবদ্ধ।

### টেক্সট জেনারেশন অ্যাপ দিয়ে আমি কী তৈরি করতে পারি?

আপনি অনেক কিছু তৈরি করতে পারেন। যেমন:

- **একটি চ্যাটবট**। একটি চ্যাটবট যা বিষয়সমূহ সম্পর্কে প্রশ্নের উত্তর দেয়, যেমন আপনার কোম্পানি ও এর পণ্যসমূহ ভাল মিল হতে পারে।
- **সহায়ক**। LLM গুলো যেমন পাঠ সংক্ষেপ করতে, তথ্য থেকে অন্তর্দৃষ্টি পেতে, রিজিউমে এবং আরও অনেক ধরনের টেক্সট উৎপাদনে চমৎকার।
- **কোড সহকারী**। আপনি যে ভাষা মডেল ব্যবহার করেন তার উপর নির্ভর করে, আপনি একটি কোড সহকারী তৈরি করতে পারেন যা আপনাকে কোড লেখায় সাহায্য করে। উদাহরণস্বরূপ, আপনি GitHub Copilot এবং ChatGPT এর মত পণ্য ব্যবহার করতে পারেন কোড লেখায় সাহায্যের জন্য।

## আমি কীভাবে শুরু করতে পারি?

সাধারণত, LLM এর সাথে ইন্টিগ্রেট করার দুটি পদ্ধতি থাকে:

- API ব্যবহার করুন। এখানে আপনি আপনার প্রম্পট সহ ওয়েব রিকোয়েস্ট তৈরি করেন এবং উৎপন্ন টেক্সট পেয়ে থাকেন।
- একটি লাইব্রেরি ব্যবহার করুন। লাইব্রেরি API কলগুলোকে ক্যাপসুলেট করে এবং এগুলোকে ব্যবহারে সহজ করে তোলে।

## লাইব্রেরি/SDK

LLM এর সাথে কাজ করার জন্য বেশ কিছু পরিচিত লাইব্রেরি রয়েছে যেমন:

- **openai**, এই লাইব্রেরি আপনার মডেলের সাথে সহজে সংযোগ স্থাপন এবং প্রম্পট পাঠাতে সাহায্য করে।

এছাড়া আরও উচ্চ স্তরের কিছু লাইব্রেরি আছে যেমন:

- **Langchain**। Langchain পরিচিত একটি লাইব্রেরি যা পাইথন সমর্থন করে।
- **Semantic Kernel**। Semantic Kernel একটি Microsoft লাইব্রেরি যা C#, Python, এবং Java ভাষা সমর্থন করে।

## প্রথম অ্যাপ openai ব্যবহার করে তৈরী করা

চলুন দেখি কিভাবে আমরা প্রথম অ্যাপ তৈরি করতে পারি, কোন লাইব্রেরির দরকার, কতটুকু প্রয়োজন ইত্যাদি।

### openai ইনস্টল করা

OpenAI বা Azure OpenAI এর সাথে ইন্টারঅ্যাক্ট করতে অনেক লাইব্রেরি রয়েছে। বিভিন্ন প্রোগ্রামিং ভাষায় ব্যবহার করা যায় যেমন C#, Python, JavaScript, Java ইত্যাদি। আমরা নির্বাচিত করেছি `openai` পাইথন লাইব্রেরি, তাই আমরা `pip` দিয়ে এটি ইনস্টল করব।

```bash
pip install openai
```

### একটি রিসোর্স তৈরি করা

আপনাকে নিম্নলিখিত ধাপগুলি অনুসরণ করতে হবে:

- Azure এ একটি অ্যাকাউন্ট তৈরি করুন [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)।
- Azure OpenAI এর অ্যাক্সেস পান। যান [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) এবং অ্যাক্সেসের জন্য অনুরোধ করুন।

  > [!NOTE]
  > লেখার সময়ে, Azure OpenAI এর জন্য অ্যাক্সেস আবেদন করতে হয়।

- পাইথন ইনস্টল করুন <https://www.python.org/>
- Azure OpenAI Service রিসোর্স তৈরি করেছেন। কিভাবে [রিসোর্স তৈরি করবেন](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst) এই গাইডটি দেখুন।

### API কী এবং এন্ডপয়েন্ট অনুসন্ধান করুন

এখন, আপনাকে `openai` লাইব্রেরিকে কোন API কী ব্যবহার করতে হবে তা জানাতে হবে। আপনার API কী খুঁজে পেতে, আপনার Azure OpenAI রিসোর্সের "Keys and Endpoint" বিভাগে যান এবং "Key 1" এর মান কপি করুন।

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

এখন এই তথ্যটি কপি করে নেওয়ার পর, লাইব্রেরিগুলোকে এটি ব্যবহারের জন্য নির্দেশ দিন।

> [!NOTE]
> আপনার API কী কোড থেকে আলাদা রাখা বাঞ্ছনীয়। আপনি পরিবেশ ভেরিয়েবল ব্যবহার করে এটি করতে পারেন।
>
> - পরিবেশ ভেরিয়েবল `OPENAI_API_KEY` সেট করুন আপনার API কী দিয়ে।
>   `export OPENAI_API_KEY='sk-...'`

### Azure কনফিগারেশন সেটআপ

আপনি যদি Azure OpenAI ব্যবহার করেন (এখন Microsoft Foundry এর অংশ), তবে কনফিগারেশন সেটআপ করার ধরণ হলো: আমরা স্ট্যান্ডার্ড `OpenAI` ক্লায়েন্ট ব্যবহার করি যেটি Azure OpenAI `/openai/v1/` এন্ডপয়েন্ট নির্দেশ করে, যা Responses API সঙ্গে কাজ করে এবং `api_version` দরকার হয় না:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

উপরের কোডে আমরা নিচের জিনিসগুলো সেট করছি:

- `api_key`, এটি আপনার Azure Portal বা Microsoft Foundry পোর্টালে পাওয়া API কী।
- `base_url`, এটি আপনার Foundry রিসোর্সের এন্ডপয়েন্ট যেখানে `/openai/v1/` যোগ করা হয়েছে। স্থিতিশীল v1 এন্ডপয়েন্ট OpenAI এবং Azure OpenAI উভয়ের জন্য কাজ করে, `api_version` ব্যবস্থাপনা ছাড়াই।

> [!NOTE] > `os.environ` পরিবেশ ভেরিয়েবল পড়ে। আপনি এটি ব্যবহার করে পরিবেশ ভেরিয়েবল যেমন `AZURE_OPENAI_API_KEY` এবং `AZURE_OPENAI_ENDPOINT` পড়তে পারেন। এই পরিবেশ ভেরিয়েবলগুলো টার্মিনালে বা `dotenv` এর মত লাইব্রেরি ব্যবহার করে সেট করুন।

## টেক্সট জেনারেট করুন

টেক্সট জেনারেট করার জন্য Responses API এর `responses.create` পদ্ধতি ব্যবহার করা হয়। উদাহরণ:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # এটি আপনার মডেল মোতায়েন নাম
    input=prompt,
    store=False,
)
print(response.output_text)
```

উপরোক্ত কোডে, আমরা একটি রেসপন্স তৈরি করি এবং মডেল ও প্রম্পট পাস করি। তারপর `response.output_text` এর মাধ্যমে উৎপন্ন টেক্সট প্রিন্ট করি।

### মাল্টি-টার্ন কথোপকথন

Responses API একক-টার্ন টেক্সট জেনারেশন এবং মাল্টি-টার্ন চ্যাটবট উভয়ের জন্য উপযুক্ত — আপনি `input` এ মেসেজের একটি তালিকা দেন কথোপকথন গঠনের জন্য:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

এই ফাংশনালিটি সম্পর্কে আরও জানতে পরবর্তী অধ্যায় দেখুন।

## অনুশীলন - আপনার প্রথম টেক্সট জেনারেশন অ্যাপ

এখন আমরা শিখেছি কিভাবে openai সেটআপ ও কনফিগার করতে হয়, সময় আপনার প্রথম টেক্সট জেনারেশন অ্যাপ তৈরি করার। আপনার অ্যাপ তৈরি করতে নিচের ধাপ অনুসরণ করুন:

১. একটি ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন এবং openai ইনস্টল করুন:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > উইন্ডোজে ব্যবহার করলে `source venv/bin/activate` এর পরিবর্তে `venv\Scripts\activate` টাইপ করুন।

   > [!NOTE]
   > আপনার Azure OpenAI কী পেতে যান [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) এবং `Open AI` সার্চ করে `Open AI resource` নির্বাচন করুন, তারপর `Keys and Endpoint` এ গিয়ে `Key 1` কপি করুন।

২. একটি _app.py_ ফাইল তৈরি করুন এবং এতে নিচের কোড দিন:

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

   # প্রতিক্রিয়া মুদ্রণ করুন
   print(response.output_text)
   ```

   > [!NOTE]
   > আপনি যদি সাধারণ OpenAI ব্যবহার করেন (Azure নয়), তাহলে `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (কোন `base_url` ছাড়া) ব্যবহার করুন এবং মডেল নাম হিসেবে একটি নাম দিন যেমন `gpt-5-mini` ডিপ্লয়মেন্ট নামের পরিবর্তে।

   আপনি নিম্নরূপ আউটপুট দেখতে পাবেন:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## বিভিন্ন ধরনের প্রম্পট, বিভিন্ন কাজের জন্য

এখন আপনি প্রম্পট ব্যবহার করে কিভাবে টেক্সট তৈরি করতে হয় তা দেখেছেন। এমনকি একটি প্রোগ্রাম চলমান আছে যা আপনি পরিবর্তন করে বিভিন্ন ধরনের টেক্সট তৈরি করতে পারেন।

প্রম্পট বিভিন্ন কাজের জন্য ব্যবহার করা যায়। উদাহরণস্বরূপ:

- **এক ধরনের টেক্সট তৈরি করুন**। যেমন, আপনি একটি কবিতা, কুইজের প্রশ্ন ইত্যাদি জেনারেট করতে পারেন।
- **তথ্য অনুসন্ধান করুন**। প্রম্পট ব্যবহার করে তথ্য খুঁজতে পারেন যেমন 'ওয়েব ডেভেলপমেন্টে CORS মানে কী?' ।
- **কোড তৈরি করুন**। প্রম্পট ব্যবহার করে কোড তৈরি করতে পারেন, যেমন ইমেইল যাচাইয়ের জন্য একটি রেগুলার এক্সপ্রেশন বা একটি পূর্ণাঙ্গ প্রোগ্রাম, যেমন একটি ওয়েব অ্যাপ?

## একটি ব্যবহারিক উদাহরণ: রেসিপি জেনারেটর

ভাবুন আপনার কাছে বাড়িতে কিছু উপাদান রয়েছে এবং আপনি কিছু রান্না করতে চান। এর জন্য একটি রেসিপি দরকার। রেসিপি খুঁজে পেতে আপনি সার্চ ইঞ্জিন ব্যবহার করতে পারেন অথবা একটি LLM ব্যবহার করতে পারেন।

আপনি এমন একটি প্রম্পট লিখতে পারেন:

> "আমার কাছে নিম্নলিখিত উপাদান আছে: মুরগি, আলু, গাজর সহ একটি ডিশের জন্য ৫টি রেসিপি দেখান। প্রতি রেসিপিতে ব্যবহৃত সমস্ত উপাদানের তালিকা দিন"

উপরোক্ত প্রম্পট অনুযায়ী, আপনি হয়তো নিম্নরূপ উত্তর পাবেন:

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

এই ফলাফল দুর্দান্ত, আমি কী রান্না করবো জানি। এখন যা উন্নতি হতে পারে:

- আমি পছন্দ না বা এলার্জি যেসব উপাদান আছে সেগুলো ফিল্টার করা।
- যদি বাড়িতে সব উপাদান না থাকে তাহলে কেনাকাটার তালিকা তৈরি করা।

উপরোক্ত জন্য, আমরা একটি অতিরিক্ত প্রম্পট যোগ করব:

> "দয়া করে যেখানে রসুন রয়েছে সেই রেসিপিগুলো বাদ দিন কারণ আমি এর প্রতি এলার্জিক এবং তা অন্য কোনো জিনিস দিয়ে প্রতিস্থাপন করুন। আরেকটু, অনুগ্রহ করে রেসিপিগুলোর জন্য কেনাকাটার তালিকা তৈরি করুন, আমি মুরগি, আলু এবং গাজর ইতিমধ্যেই বাড়িতে রেখেছি।"

এখন আপনার একটি নতুন ফলাফল আছে, অর্থাৎ:

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

এই হলো আপনার পাঁচটি রেসিপি, যেখানে রসুন নেই এবং বাড়িতে যা আছে বিবেচনা করে একটি কেনাকাটার তালিকাও আছে।

## অনুশীলন - রেসিপি জেনারেটর তৈরি করুন

এখন যেহেতু এক সিনারিও আমরা দেখাছি, আসুন সেই অনুযায়ী কোড লিখি। এর জন্য নিচের ধাপগুলো অনুসরণ করুন:

১. বিদ্যমান _app.py_ ফাইলটি শুরু হিসেবে ব্যবহার করুন
১. `prompt` ভ্যারিয়েবল খুঁজে বের করে এর কোড নিচের মত পরিবর্তন করুন:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   এখন যদি কোড চালান, নিম্নরূপ আউটপুট দেখতে পাবেন:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > লক্ষ্য করুন, আপনার LLM ননডিটারমিনিস্টিক, তাই প্রতিবার চালানোর সময় ভিন্ন ফলাফল পেতে পারেন।

   চমৎকার, চলুন দেখি কীভাবে উন্নতি করা যায়। উন্নতির জন্য আমরা চাই কোড নমনীয় হোক যাতে উপাদান এবং রেসিপির সংখ্যা সহজে পরিবর্তন ও উন্নত করা যায়।

১. কোড নিচের মতো পরিবর্তন করুন:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # রেসিপির সংখ্যা এবং উপকরণ সমূহ প্রম্পটে অন্তর্ভুক্ত করুন
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   টেস্ট চালানোর জন্য কোড এমন হতে পারে:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### ফিল্টার এবং কেনাকাটার তালিকা যোগ করে উন্নতি করুন

এখন আমাদের একটি কাজ করা অ্যাপ আছে যা রেসিপি তৈরি করতে পারে এবং ব্যবহারকারীর ইনপুটের উপর নির্ভর করে নমনীয়, যেমন রেসিপির সংখ্যা এবং ব্যবহৃত উপাদান।

আরও উন্নতির জন্য আমরা নিচের বিষয়গুলো যোগ করতে চাই:

- **উপাদান ফিল্টার করুন**। আমরা উপাদান ফিল্টার করতে চাই যা আমরা পছন্দ না করি বা যা আমরা এলার্জি। এটা করতে, আমরা আমাদের প্রম্পটের শেষে একটি ফিল্টার শর্ত যোগ করব, যেমন:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  উপরে, আমরা প্রম্পটের শেষে `{filter}` যোগ করেছি এবং ব্যবহারকারীর থেকে ফিল্টার মান নিয়েছি।

  প্রোগ্রাম চালানোর একটি উদাহরণ ইনপুট এখন এই রকম হতে পারে:

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

  আপনি দেখতে পাচ্ছেন, যেসব রেসিপিতে দুধ আছে সেগুলো ফিল্টার হয়ে গেছে। কিন্তু, যদি আপনি ল্যাকটোজ ইনটলারেন্ট (দুধজনিত সমস্যা) হন, তাহলে আপনি চিজসহ রেসিপিতেও ফিল্টার চান, তাই এটি স্পষ্ট করা দরকার।


- **একটি শপিং লিস্ট তৈরি করুন**। আমরা একটি শপিং লিস্ট তৈরি করতে চাই, আমাদের ঘরে যা আছে তা বিবেচনা করে।

  এই ফাংশনালিটির জন্য, আমরা বা তো সবকিছু একবারে এক প্রম্পটে সমাধান করার চেষ্টা করতে পারি, অথবা আমরা এটিকে দুইটি প্রম্পটে বিভক্ত করতে পারি। চলুন আমরা পরবর্তী পদ্ধতি চেষ্টা করি। এখানে আমরা একটি অতিরিক্ত প্রম্পট যোগ করার পরামর্শ দিচ্ছি, তবে এটি কাজ করার জন্য, আমাদের প্রথম প্রম্পটের ফলাফলটিকে পরবর্তী প্রম্পটের প্রসঙ্গে যুক্ত করতে হবে।

  কোডের সেই অংশটি খুঁজুন যা প্রথম প্রম্পট থেকে প্রাপ্ত ফলাফল প্রিন্ট করে এবং নিচের কোডটি সেখানে যোগ করুন:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # প্রতিক্রিয়া মুদ্রণ করুন
  print("Shopping list:")
  print(response.output_text)
  ```

  নিম্নলিখিত বিষয়গুলি লক্ষ করুন:

  1. আমরা একটি নতুন প্রম্পট গঠন করছি যেখানে প্রথম প্রম্পট থেকে প্রাপ্ত ফলাফল নতুন প্রম্পটে যোগ করা হচ্ছে:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. আমরা একটি নতুন অনুরোধ করছি, তবে প্রথম প্রম্পটে যে সংখ্যক টোকেন চেয়েছিলাম তা বিবেচনায় রেখে, তাই এবার আমরা বলছি `max_output_tokens` হলো 1200।

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     এই কোডটি চালিয়ে আমরা এখন নিম্নলিখিত আউটপুট পেয়েছি:

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

এখন পর্যন্ত আমাদের কাছে কাজ করা কোড আছে, কিন্তু আরও উন্নতির জন্য কিছু টুইক করা উচিত। আমাদের যা করা উচিত সেগুলো হলো:

- **কোড থেকে সিক্রেট আলাদা করুন**, যেমন API কী। সিক্রেট কোডে থাকা উচিত নয় এবং সেগুলো নিরাপদ স্থানে সংরক্ষণ করা উচিত। সিক্রেট কোড থেকে আলাদা করার জন্য আমরা পরিবেশ ভেরিয়েবল এবং `python-dotenv` এর মতো লাইব্রেরি ব্যবহার করতে পারি যেগুলো ফাইল থেকে লোড করতে সাহায্য করে। কোডে এটি কেমন দেখাবে তা নিচে দেওয়া হলো:

  1. নিম্নলিখিত বিষয়বস্তু সহ একটি `.env` ফাইল তৈরি করুন:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > নোট করুন, Microsoft Foundry এর Azure OpenAI এর জন্য, আপনাকে নিম্নলিখিত পরিবেশ ভেরিয়েবল সেট করতে হবে:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     কোডে পরিবেশ ভেরিয়েবলগুলি এভাবে লোড করবেন:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **টোকেন দৈর্ঘ্য সম্পর্কে একটি কথা**। আমাদের যে টেক্সট জেনারেট করতে হবে তার জন্য কত টোকেন দরকার তা বিবেচনা করা উচিত। টোকেন ব্যবহারে অর্থ ব্যয় হয়, তাই যেখানে সম্ভব, টোকেন ব্যবহারে সাশ্রয়ী হওয়া উচিত। উদাহরণস্বরূপ, আমরা কি প্রম্পট এমনভাবে ফ্রেইজ করতে পারি যাতে কম টোকেন ব্যবহার হয়?

  টোকেন পরিবর্তন করতে, আপনি `max_output_tokens` প্যারামিটার ব্যবহার করতে পারেন। উদাহরণস্বরূপ, আপনি যদি ১০০ টোকেন ব্যবহার করতে চান, তাহলে করবেন:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **তাপমাত্রা পরীক্ষা করা**। তাপমাত্রা এমন একটি প্যারামিটার যা আমরা এখন পর্যন্ত উল্লেখ করিনি কিন্তু এটি আমাদের প্রোগ্রামের কর্মক্ষমতার জন্য গুরুত্বপূর্ণ। তাপমাত্রার মান যত বেশি হবে আউটপুট তত বেশি এলোমেলো হবে। বিপরীতে, তাপমাত্রার মান যত কম হবে আউটপুট তত বেশি পূর্বানুমেয় হবে। ভাবুন আপনি আপনার আউটপুটে বৈচিত্র্য চান কিনা।

  তাপমাত্রা পরিবর্তন করতে, আপনি `temperature` প্যারামিটার ব্যবহার করতে পারেন। উদাহরণস্বরূপ, আপনি যদি ০.৫ তাপমাত্রা সেট করতে চান, তাহলে করবেন:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > নোট করুন, ১.০ এর কাছে যাত্রা করলে আউটপুট আরও বৈচিত্র্যময় হবে।

- **রিজনিং মডেলগুলি `temperature` ব্যবহার করে না**। এটি ২০২৬ সালের একটি গুরুত্বপূর্ণ পরিবর্তন। Microsoft Foundry এর বর্তমান, অব্যাহত নয় এমন মডেলগুলো হলো **রিজনিং মডেল** (GPT-5 পরিবার, o-series) - এবং তারা **`temperature` বা `top_p` সমর্থন করে না** (না `max_tokens`; পরিবর্তে `max_output_tokens` ব্যবহার করুন)। আপনি যদি `gpt-5-mini` এ `temperature` পাঠান তবে "parameter not supported" ত্রুটি পাবেন। তাই উপরের তাপমাত্রা উদাহরণ চেষ্টা করতে, এমন একটি মডেলে নির্দেশ দিন যা এখনও স্যাম্পলিং কন্ট্রোল সমর্থন করে - উদাহরণস্বরূপ একটি ওপেন **Llama** মডেল যেমন `Llama-3.3-70B-Instruct` যা Microsoft Foundry মডেল ক্যাটালগ থেকে পাওয়া যাবে (https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), Foundry Models / Azure AI Inference এন্ডপয়েন্টের মাধ্যমে কল করা হয় (ঠিক যেমন `githubmodels-*` স্যাম্পলগুলো)। GPT-5 এর মতো রিজনিং মডেলগুলোর আউটপুট নিয়ন্ত্রণ এরকম:
  - **প্রম্পট ইঞ্জিনিয়ারিং** - স্পষ্ট নির্দেশনা, উদাহরণ এবং গঠিত আউটপুট (পাঠ দেখুন [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) তারা স্যাম্পলিং নিয়ন্ত্রণের কাজ করে।
  - **রিজনিং নিয়ন্ত্রণ** - রিজনিং প্রচেষ্টা/বিস্তারের মতো প্যারামিটারগুলো রিজনিং এর গভীরতা এবং বিলম্ব ও খরচের মধ্যে সন্মিলন ঘটায়।

  সংক্ষেপে: `temperature`/`top_p` এখনো অনেক মডেলে বৈধ (Llama, Mistral, Phi, এবং GPT-4.x পরিবার - যদিও GPT-4.x অববাহিত হচ্ছে), কিন্তু রিজনিং মডেল GPT-5 এর জন্য যাত্রাপথ হলো প্রম্পট ইঞ্জিনিয়ারিং + রিজনিং নিয়ন্ত্রণ।

## অ্যাসাইনমেন্ট

এই অ্যাসাইনমেন্টের জন্য, আপনি যা বানাতে চান তা নির্বাচন করতে পারেন।

এখানে কিছু পরামর্শ:

- রেসিপি জেনারেটর অ্যাপটিকে আরও উন্নত করুন। তাপমাত্রার মান এবং প্রম্পটগুলোর সাথে খেলুন এবং দেখুন আপনি কী তৈরি করতে পারেন।
- একটি "স্টাডি বাডি" তৈরী করুন। এই অ্যাপটি একটি বিষয় সম্পর্কে প্রশ্নের উত্তর দিতে পারবে; উদাহরণস্বরূপ Pythonএর জন্য, আপনি এমন প্রম্পট দিতে পারেন "Python এ একটি নির্দিষ্ট বিষয় কী?", অথবা এমন প্রম্পট দিতে পারেন যা বলে, নির্দিষ্ট বিষয়ের কোড দেখাও ইত্যাদি।
- ইতিহাস বট, ইতিহাসকে জীবন্ত করুন, বটকে নির্দেশ দিন একটি নির্দিষ্ট ঐতিহাসিক চরিত্রের ভূমিকায় অভিনয় করতে এবং তার জীবন ও সময় সম্পর্কে প্রশ্ন করুন।

## সমাধান

### স্টাডি বাডি

নিচে একটি স্টার্টার প্রম্পট দেওয়া হলো, দেখুন কীভাবে ব্যবহার করতে পারেন এবং আপনার পছন্দ অনুযায়ী কীভাবে পরিবর্তন করবেন।

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

## জ্ঞান পরীক্ষা

তাপমাত্রার ধারণাটি কী করে?

1. এটি আউটপুট কতটা এলোমেলো হবে তা নিয়ন্ত্রণ করে।
1. এটি প্রতিক্রিয়ার আকার কত বড় হবে তা নিয়ন্ত্রণ করে।
1. এটি কত টোকেন ব্যবহৃত হবে তা নিয়ন্ত্রণ করে।

## 🚀 চ্যালেঞ্জ

অ্যাসাইনমেন্টে কাজ করার সময়, তাপমাত্রা পরিবর্তন করার চেষ্টা করুন, ০, ০.৫, এবং ১ সেট করুন। মনে রাখবেন, ০ সবচেয়ে কম বৈচিত্রময় এবং ১ সবচেয়ে বেশি। আপনার অ্যাপের জন্য কোন মান সবচেয়ে ভাল কাজ করে?

## দারুন কাজ! আপনার শেখা চালিয়ে যান

এই পাঠ শেষ করলে, আমাদের [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) পরীক্ষা করুন যাতে আপনি আপনার Generative AI জ্ঞান আরও উন্নত করতে পারেন!

পাঠ ৭ এ যান যেখানে আমরা দেখবো কিভাবে [চ্যাট অ্যাপ্লিকেশন তৈরি করতে হয়](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->