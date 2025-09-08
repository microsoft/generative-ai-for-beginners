<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ce8224073b86b728ed52b19bed7932fd",
  "translation_date": "2025-07-09T11:51:00+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "bn"
}
-->
# টেক্সট জেনারেশন অ্যাপ্লিকেশন তৈরি করা

[![Building Text Generation Applications](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.bn.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(এই লেসনের ভিডিও দেখতে উপরের ছবিতে ক্লিক করুন)_

এখন পর্যন্ত আপনি এই কারিকুলামের মাধ্যমে দেখেছেন যে প্রম্পটের মতো মূল ধারণাগুলো আছে এবং এমনকি "prompt engineering" নামে একটি সম্পূর্ণ শাখাও রয়েছে। অনেক টুলস যেমন ChatGPT, Office 365, Microsoft Power Platform ইত্যাদি আপনাকে প্রম্পট ব্যবহার করে কিছু অর্জন করতে সাহায্য করে।

আপনি যদি এমন একটি অভিজ্ঞতা কোনো অ্যাপে যোগ করতে চান, তাহলে আপনাকে প্রম্পট, কমপ্লিশন ইত্যাদি ধারণাগুলো বুঝতে হবে এবং কাজ করার জন্য একটি লাইব্রেরি বেছে নিতে হবে। ঠিক এইটাই আপনি এই অধ্যায়ে শিখবেন।

## পরিচিতি

এই অধ্যায়ে আপনি:

- openai লাইব্রেরি এবং এর মূল ধারণাগুলো সম্পর্কে জানবেন।
- openai ব্যবহার করে একটি টেক্সট জেনারেশন অ্যাপ তৈরি করবেন।
- প্রম্পট, টেম্পারেচার, টোকেনের মতো ধারণাগুলো কীভাবে ব্যবহার করে টেক্সট জেনারেশন অ্যাপ তৈরি করা যায় তা বুঝবেন।

## শেখার লক্ষ্য

এই লেসনের শেষে আপনি পারবেন:

- টেক্সট জেনারেশন অ্যাপ কী তা ব্যাখ্যা করতে।
- openai ব্যবহার করে একটি টেক্সট জেনারেশন অ্যাপ তৈরি করতে।
- আপনার অ্যাপকে কনফিগার করতে যাতে বেশি বা কম টোকেন ব্যবহার করা যায় এবং টেম্পারেচার পরিবর্তন করে বিভিন্ন আউটপুট পাওয়া যায়।

## টেক্সট জেনারেশন অ্যাপ কী?

সাধারণত যখন আপনি একটি অ্যাপ তৈরি করেন, তখন তার কিছু ধরণের ইন্টারফেস থাকে, যেমন:

- কমান্ড-ভিত্তিক। কনসোল অ্যাপগুলো সাধারণত এমন অ্যাপ যেখানে আপনি একটি কমান্ড টাইপ করেন এবং এটি একটি কাজ সম্পন্ন করে। উদাহরণস্বরূপ, `git` একটি কমান্ড-ভিত্তিক অ্যাপ।
- ইউজার ইন্টারফেস (UI)। কিছু অ্যাপে গ্রাফিক্যাল ইউজার ইন্টারফেস (GUI) থাকে যেখানে আপনি বাটনে ক্লিক করেন, টেক্সট ইনপুট দেন, অপশন নির্বাচন করেন ইত্যাদি।

### কনসোল এবং UI অ্যাপগুলো সীমাবদ্ধ

একটি কমান্ড-ভিত্তিক অ্যাপের সাথে তুলনা করুন যেখানে আপনি একটি কমান্ড টাইপ করেন:

- **সীমাবদ্ধ**। আপনি যেকোনো কমান্ড টাইপ করতে পারবেন না, শুধুমাত্র সেই কমান্ডগুলো যা অ্যাপ সমর্থন করে।
- **ভাষা নির্দিষ্ট**। কিছু অ্যাপ অনেক ভাষা সমর্থন করে, কিন্তু ডিফল্টভাবে অ্যাপটি একটি নির্দিষ্ট ভাষার জন্য তৈরি, যদিও আপনি আরও ভাষা যোগ করতে পারেন।

### টেক্সট জেনারেশন অ্যাপের সুবিধা

তাহলে টেক্সট জেনারেশন অ্যাপ কীভাবে আলাদা?

একটি টেক্সট জেনারেশন অ্যাপে আপনি বেশি নমনীয়তা পান, আপনি নির্দিষ্ট কমান্ড বা নির্দিষ্ট ইনপুট ভাষায় সীমাবদ্ধ নন। পরিবর্তে, আপনি প্রাকৃতিক ভাষা ব্যবহার করে অ্যাপের সাথে যোগাযোগ করতে পারেন। আরেকটি সুবিধা হলো, আপনি এমন একটি ডেটা সোর্সের সাথে কাজ করছেন যা বিশাল তথ্যভাণ্ডারে প্রশিক্ষিত, যেখানে একটি প্রচলিত অ্যাপ ডাটাবেসের মধ্যে সীমাবদ্ধ থাকতে পারে।

### টেক্সট জেনারেশন অ্যাপ দিয়ে কী তৈরি করা যায়?

অনেক কিছু তৈরি করা যায়। উদাহরণস্বরূপ:

- **একটি চ্যাটবট**। একটি চ্যাটবট যা আপনার কোম্পানি এবং এর পণ্য সম্পর্কে প্রশ্নের উত্তর দিতে পারে, এটি একটি ভালো উদাহরণ।
- **সহায়ক**। LLM গুলো টেক্সট সারাংশ তৈরি, টেক্সট থেকে তথ্য আহরণ, রিজিউমে তৈরি ইত্যাদিতে খুব ভালো।
- **কোড সহকারী**। আপনি যে ভাষার মডেল ব্যবহার করেন তার উপর নির্ভর করে, আপনি এমন একটি কোড সহকারী তৈরি করতে পারেন যা কোড লেখায় সাহায্য করে। উদাহরণস্বরূপ, GitHub Copilot এবং ChatGPT ব্যবহার করে কোড লেখা সহজ করা যায়।

## কীভাবে শুরু করবেন?

আপনাকে একটি LLM এর সাথে ইন্টিগ্রেট করার উপায় খুঁজে বের করতে হবে, যা সাধারণত নিম্নলিখিত দুইটি পদ্ধতি অনুসরণ করে:

- API ব্যবহার করুন। এখানে আপনি আপনার প্রম্পট সহ ওয়েব রিকোয়েস্ট তৈরি করেন এবং জেনারেটেড টেক্সট ফিরে পান।
- লাইব্রেরি ব্যবহার করুন। লাইব্রেরিগুলো API কলগুলোকে ইনক্যাপসুলেট করে এবং ব্যবহার সহজ করে।

## লাইব্রেরি/SDK

LLM এর সাথে কাজ করার জন্য কিছু পরিচিত লাইব্রেরি আছে, যেমন:

- **openai**, এই লাইব্রেরি আপনার মডেলের সাথে সংযোগ করা এবং প্রম্পট পাঠানো সহজ করে।

তারপর এমন লাইব্রেরি আছে যা উচ্চ স্তরে কাজ করে, যেমন:

- **Langchain**। Langchain পরিচিত এবং Python সমর্থন করে।
- **Semantic Kernel**। Semantic Kernel হলো Microsoft এর একটি লাইব্রেরি যা C#, Python, এবং Java ভাষা সমর্থন করে।

## openai ব্যবহার করে প্রথম অ্যাপ

চলুন দেখি কিভাবে আমরা আমাদের প্রথম অ্যাপ তৈরি করব, কোন লাইব্রেরি দরকার, কতটুকু প্রয়োজন ইত্যাদি।

### openai ইনস্টল করুন

OpenAI বা Azure OpenAI এর সাথে ইন্টারঅ্যাক্ট করার জন্য অনেক লাইব্রেরি আছে। বিভিন্ন প্রোগ্রামিং ভাষা ব্যবহার করা সম্ভব যেমন C#, Python, JavaScript, Java ইত্যাদি। আমরা `openai` Python লাইব্রেরি ব্যবহার করার সিদ্ধান্ত নিয়েছি, তাই `pip` দিয়ে এটি ইনস্টল করব।

```bash
pip install openai
```

### একটি রিসোর্স তৈরি করুন

নিম্নলিখিত ধাপগুলো অনুসরণ করতে হবে:

- Azure এ একটি অ্যাকাউন্ট তৈরি করুন [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)।
- Azure OpenAI অ্যাক্সেস পান। যান [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) এবং অ্যাক্সেসের জন্য আবেদন করুন।

  > [!NOTE]
  > লেখার সময়, Azure OpenAI অ্যাক্সেসের জন্য আবেদন করতে হয়।

- Python ইনস্টল করুন <https://www.python.org/>
- একটি Azure OpenAI Service রিসোর্স তৈরি করুন। কিভাবে রিসোর্স তৈরি করবেন দেখুন [create a resource](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)।

### API কী এবং এন্ডপয়েন্ট খুঁজে বের করুন

এখন আপনাকে `openai` লাইব্রেরিকে কোন API কী ব্যবহার করতে হবে তা বলতে হবে। আপনার API কী পেতে Azure OpenAI রিসোর্সের "Keys and Endpoint" সেকশনে যান এবং "Key 1" এর মান কপি করুন।

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

এখন যেহেতু আপনার কাছে এই তথ্য আছে, চলুন লাইব্রেরিগুলোকে এটি ব্যবহার করতে বলি।

> [!NOTE]
> আপনার API কী কোড থেকে আলাদা রাখা ভালো। আপনি পরিবেশ ভেরিয়েবল ব্যবহার করে এটি করতে পারেন।
>
> - পরিবেশ ভেরিয়েবল `OPENAI_API_KEY` আপনার API কী দিয়ে সেট করুন।
>   `export OPENAI_API_KEY='sk-...'`

### Azure কনফিগারেশন সেটআপ করুন

যদি আপনি Azure OpenAI ব্যবহার করেন, তাহলে কনফিগারেশন সেটআপ এরকম হবে:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

উপরের কোডে আমরা নিচেরগুলো সেট করছি:

- `api_type` কে `azure` সেট করছি। এটি লাইব্রেরিকে বলে Azure OpenAI ব্যবহার করতে, OpenAI নয়।
- `api_key`, এটি আপনার Azure পোর্টালে পাওয়া API কী।
- `api_version`, এটি API এর সংস্করণ। লেখার সময় সর্বশেষ সংস্করণ `2023-05-15`।
- `api_base`, এটি API এর এন্ডপয়েন্ট। Azure পোর্টালে আপনার API কী এর পাশে এটি পাওয়া যাবে।

> [!NOTE]
> `os.getenv` একটি ফাংশন যা পরিবেশ ভেরিয়েবল পড়ে। আপনি এটি ব্যবহার করে `OPENAI_API_KEY` এবং `API_BASE` এর মতো পরিবেশ ভেরিয়েবল পড়তে পারেন। টার্মিনালে বা `dotenv` লাইব্রেরি ব্যবহার করে এগুলো সেট করুন।

## টেক্সট জেনারেট করা

টেক্সট জেনারেট করার জন্য `Completion` ক্লাস ব্যবহার করা হয়। উদাহরণ:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

উপরের কোডে, আমরা একটি completion অবজেক্ট তৈরি করেছি এবং মডেল ও প্রম্পট পাস করেছি। তারপর জেনারেটেড টেক্সট প্রিন্ট করেছি।

### চ্যাট কমপ্লিশন

এখন পর্যন্ত আপনি দেখেছেন আমরা `Completion` ব্যবহার করে টেক্সট জেনারেট করছি। কিন্তু আরেকটি ক্লাস আছে `ChatCompletion` যা চ্যাটবটের জন্য বেশি উপযোগী। উদাহরণ:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

এই ফিচার সম্পর্কে আরও বিস্তারিত পরবর্তী অধ্যায়ে।

## অনুশীলন - আপনার প্রথম টেক্সট জেনারেশন অ্যাপ

এখন আমরা শিখেছি কিভাবে openai সেটআপ ও কনফিগার করতে হয়, চলুন আপনার প্রথম টেক্সট জেনারেশন অ্যাপ তৈরি করি। নিম্নলিখিত ধাপগুলো অনুসরণ করুন:

1. একটি ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন এবং openai ইনস্টল করুন:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > যদি আপনি Windows ব্যবহার করেন, তাহলে `source venv/bin/activate` এর পরিবর্তে `venv\Scripts\activate` টাইপ করুন।

   > [!NOTE]
   > আপনার Azure OpenAI কী খুঁজে পেতে যান [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) এবং `Open AI` সার্চ করুন, তারপর `Open AI resource` নির্বাচন করুন, এরপর `Keys and Endpoint` থেকে `Key 1` কপি করুন।

1. একটি _app.py_ ফাইল তৈরি করুন এবং নিচের কোড দিন:

   ```python
   import openai

   openai.api_key = "<replace this value with your open ai key or Azure OpenAI key>"

   openai.api_type = 'azure'
   openai.api_version = '2023-05-15'
   openai.api_base = "<endpoint found in Azure Portal where your API key is>"
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"
   messages = [{"role": "user", "content": prompt}]

   # make completion
   completion = openai.chat.completions.create(model=deployment_name, messages=messages)

   # print response
   print(completion.choices[0].message.content)
   ```

   > [!NOTE]
   > যদি আপনি Azure OpenAI ব্যবহার করেন, তাহলে `api_type` কে `azure` এবং `api_key` কে আপনার Azure OpenAI কী সেট করতে হবে।

   আপনি নিচের মতো আউটপুট দেখতে পাবেন:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## বিভিন্ন ধরনের প্রম্পট, বিভিন্ন কাজের জন্য

এখন আপনি দেখেছেন কিভাবে প্রম্পট ব্যবহার করে টেক্সট জেনারেট করা যায়। এমন একটি প্রোগ্রামও তৈরি করেছেন যা আপনি পরিবর্তন করে বিভিন্ন ধরনের টেক্সট তৈরি করতে পারেন।

প্রম্পট বিভিন্ন কাজের জন্য ব্যবহার করা যায়। উদাহরণস্বরূপ:

- **এক ধরনের টেক্সট তৈরি করা**। যেমন, কবিতা, কুইজের প্রশ্ন ইত্যাদি।
- **তথ্য অনুসন্ধান**। প্রম্পট ব্যবহার করে তথ্য খোঁজা যায়, যেমন 'ওয়েব ডেভেলপমেন্টে CORS মানে কী?'।
- **কোড তৈরি করা**। প্রম্পট ব্যবহার করে কোড তৈরি করা যায়, যেমন ইমেইল যাচাই করার জন্য রেগুলার এক্সপ্রেশন তৈরি করা বা একটি সম্পূর্ণ প্রোগ্রাম, যেমন ওয়েব অ্যাপ তৈরি করা।

## আরও ব্যবহারিক একটি উদাহরণ: রেসিপি জেনারেটর

ধরুন আপনার বাড়িতে কিছু উপকরণ আছে এবং আপনি কিছু রান্না করতে চান। এর জন্য একটি রেসিপি দরকার। রেসিপি খুঁজতে আপনি সার্চ ইঞ্জিন ব্যবহার করতে পারেন অথবা LLM ব্যবহার করতে পারেন।

আপনি এমন একটি প্রম্পট লিখতে পারেন:

> "আমার কাছে নিম্নলিখিত উপকরণ আছে: মুরগি, আলু, এবং গাজর। এই উপকরণ দিয়ে ৫টি রেসিপি দেখাও। প্রতিটি রেসিপির জন্য ব্যবহৃত সব উপকরণ তালিকাভুক্ত করো।"

উপরের প্রম্পট অনুযায়ী আপনি এমন একটি উত্তর পেতে পারেন:

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

এই ফলাফল খুব ভালো, আমি কী রান্না করব তা বুঝতে পারছি। এখন কিছু উন্নতি হতে পারে:

- আমি পছন্দ না করা বা এলার্জি থাকা উপকরণগুলো ফিল্টার করা।
- যদি সব উপকরণ না থাকে, তাহলে একটি শপিং লিস্ট তৈরি করা।

এই জন্য আমরা একটি অতিরিক্ত প্রম্পট যোগ করব:

> "আমার গার্লিকের প্রতি এলার্জি আছে, তাই গার্লিক যুক্ত রেসিপিগুলো বাদ দাও এবং অন্য কিছু দিয়ে প্রতিস্থাপন করো। এছাড়াও, আমার কাছে মুরগি, আলু এবং গাজর আছে ধরে নিয়ে রেসিপিগুলোর জন্য একটি শপিং লিস্ট তৈরি করো।"

এখন আপনি নতুন ফলাফল পাবেন, যেমন:

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

এগুলো আপনার পাঁচটি রেসিপি, গার্লিক ছাড়া এবং আপনার কাছে যা আছে তা বিবেচনা করে একটি শপিং লিস্ট।

## অনুশীলন - একটি রেসিপি জেনারেটর তৈরি করুন

এখন যেহেতু আমরা একটি পরিস্থিতি খেলেছি, চলুন সেই অনুযায়ী কোড লিখি। এর জন্য নিম্নলিখিত ধাপ অনুসরণ করুন:

1. বিদ্যমান _app.py_ ফাইলটি শুরু হিসেবে ব্যবহার করুন।
1. `prompt` ভেরিয়েবলটি খুঁজে বের করুন এবং এর কোড নিচের মতো পরিবর্তন করুন:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   এখন কোড চালালে আপনি এমন একটি আউটপুট দেখতে পাবেন:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, আপনার LLM ননডিটারমিনিস্টিক, তাই প্রতিবার চালালে ভিন্ন ফলাফল পেতে পারেন।

দারুণ, চলুন দেখি কিভাবে উন্নতি করা যায়। উন্নতির জন্য আমরা চাই কোড নমনীয় হোক, যাতে রেসিপির সংখ্যা এবং উপকরণ পরিবর্তন করা যায়।

1. কোড নিচের মতো পরিবর্তন করুন:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   টেস্ট রান এর জন্য কোড এমন হতে পারে:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### ফিল্টার এবং শপিং লিস্ট যোগ করে উন্নতি

এখন আমাদের একটি কাজ করা অ্যাপ আছে যা রেসিপি তৈরি করতে পারে এবং এটি নমনীয় কারণ এটি ব্যবহারকারীর ইনপুটের উপর নির্ভর করে, যেমন রেসিপির সংখ্যা এবং ব্যবহৃত উপকরণ।

আরও উন্নতির জন্য আমরা নিম্নলিখিত যোগ করতে চাই:

- **উপকরণ ফিল্টার করা**। আমরা এমন উপকরণ ফিল্টার করতে চাই যা আমরা পছন্দ করি না বা যার প্রতি এলার্জি আছে। এটি করার জন্য আমরা আমাদের বিদ্যমান প্রম্পটের শেষে একটি ফিল্টার শর্ত যোগ করব, যেমন:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  উপরে, আমরা প্রম্পটের শেষে `{filter}` যোগ করেছি এবং ব্যবহারকারীর কাছ থেকে ফিল্টার মানও নিচ্ছি।

  প্রোগ্রাম চালানোর একটি উদাহরণ ইনপুট হতে পারে:

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

  যেমন দেখা যাচ্ছে, দুধ যুক্ত রেসিপিগুলো ফিল্টার করা হয়েছে। কিন্তু যদি আপনি ল্যাকটোজ ইনটলারেন্ট হন, তাহলে পনির যুক্ত রেসিপিও ফিল্টার করতে চাইবেন, তাই স্পষ্ট হওয়া দরকার।

- **শপিং লিস্ট তৈরি করা**। আমরা একটি শপিং লিস্ট তৈরি করতে চাই, যা বিবেচনা করবে যে বাড়িতে কি কি উপকরণ আছে।

  এই ফিচারটির জন্য আমরা সবকিছু এক প্রম্পটে করার চেষ্টা করতে পারি অথবা দুইটি প্রম্পটে ভাগ করতে পারি। আমরা দ্বিতীয় পদ্ধতি চেষ্টা করব। এখানে আমরা একটি অতিরিক্ত প্রম্পট যোগ করার পরামর্শ দিচ্ছি, কিন্তু এটি কাজ করার জন্য প্রথম প্রম্পটের ফলাফলকে দ্বিতীয় প্রম্পটের প্রসঙ্গ হিসেবে যোগ করতে হবে।

  কোডের সেই অংশ যেখানে প্রথম প্রম্পটের ফলাফল প্রিন্ট করা হয়, তার নিচে নিচের কোড যোগ করুন:

  ```python
  old_prompt_result = completion.choices[0].message.content
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  messages = [{"role": "user", "content": new_prompt}]
  completion = openai.Completion.create(engine=deployment_name, messages=messages, max_tokens=1200)

  # print response
  print("Shopping list:")
  print(completion.choices[0].message.content)
  ```

  লক্ষ্য করুন:

  1. আমরা একটি নতুন প্রম্পট তৈরি করছি যেখানে প্রথম প্রম্পটের ফলাফল নতুন প্রম্পটের সাথে যোগ করা হয়েছে:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```
1. আমরা একটি নতুন অনুরোধ করি, তবে প্রথম প্রম্পটে আমরা যতো টোকেন চেয়েছিলাম তা বিবেচনায় রেখে, এবার বলি `max_tokens` 1200।

```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

এই কোডটি চালিয়ে আমরা নিম্নলিখিত আউটপুট পাই:

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

এখন পর্যন্ত আমাদের কাছে এমন কোড আছে যা কাজ করে, কিন্তু আরও উন্নতির জন্য কিছু পরিবর্তন করা উচিত। কিছু কাজ যা করা উচিত:

- **গোপন তথ্য কোড থেকে আলাদা করুন**, যেমন API কী। গোপন তথ্য কোডে থাকা উচিত নয় এবং সেগুলো নিরাপদ স্থানে সংরক্ষণ করা উচিত। গোপন তথ্য কোড থেকে আলাদা করতে আমরা পরিবেশ ভেরিয়েবল এবং `python-dotenv` এর মতো লাইব্রেরি ব্যবহার করতে পারি যা ফাইল থেকে সেগুলো লোড করে। কোডে এটি কেমন দেখাবে তার উদাহরণ:

  ১. একটি `.env` ফাইল তৈরি করুন নিম্নলিখিত বিষয়বস্তু সহ:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     
> লক্ষ্য করুন, Azure এর জন্য আপনাকে নিম্নলিখিত পরিবেশ ভেরিয়েবল সেট করতে হবে:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     কোডে, আপনি পরিবেশ ভেরিয়েবলগুলো এভাবে লোড করবেন:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **টোকেন দৈর্ঘ্য সম্পর্কে একটি কথা**। আমাদের কতগুলো টোকেন দরকার তা বিবেচনা করা উচিত যাতে আমরা কাঙ্ক্ষিত টেক্সট তৈরি করতে পারি। টোকেনের জন্য খরচ হয়, তাই যেখানে সম্ভব, টোকেনের ব্যবহার কমানোর চেষ্টা করা উচিত। উদাহরণস্বরূপ, আমরা কি প্রম্পট এমনভাবে সাজাতে পারি যাতে কম টোকেন ব্যবহার হয়?

  টোকেনের সংখ্যা পরিবর্তন করতে, আপনি `max_tokens` প্যারামিটার ব্যবহার করতে পারেন। উদাহরণস্বরূপ, যদি আপনি ১০০ টোকেন ব্যবহার করতে চান, তাহলে করবেন:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **তাপমাত্রা নিয়ে পরীক্ষা-নিরীক্ষা**। তাপমাত্রা এমন একটি বিষয় যা এখন পর্যন্ত উল্লেখ করা হয়নি, কিন্তু এটি আমাদের প্রোগ্রামের পারফরম্যান্সের জন্য গুরুত্বপূর্ণ। তাপমাত্রার মান যত বেশি হবে আউটপুট তত বেশি এলোমেলো হবে। বিপরীতে, তাপমাত্রার মান যত কম হবে আউটপুট তত বেশি পূর্বানুমানযোগ্য হবে। আপনি কি আউটপুটে বৈচিত্র্য চান তা বিবেচনা করুন।

  তাপমাত্রা পরিবর্তন করতে, আপনি `temperature` প্যারামিটার ব্যবহার করতে পারেন। উদাহরণস্বরূপ, যদি আপনি ০.৫ তাপমাত্রা ব্যবহার করতে চান, তাহলে করবেন:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > লক্ষ্য করুন, ১.০ এর কাছাকাছি মানে আউটপুট আরও বৈচিত্র্যময় হবে।

## অ্যাসাইনমেন্ট

এই অ্যাসাইনমেন্টে, আপনি যা বানাতে চান তা বেছে নিতে পারেন।

কিছু পরামর্শ:

- রেসিপি জেনারেটর অ্যাপটি আরও উন্নত করতে পরিবর্তন করুন। তাপমাত্রার মান এবং প্রম্পট নিয়ে পরীক্ষা-নিরীক্ষা করুন এবং দেখুন আপনি কী করতে পারেন।
- একটি "স্টাডি বাডি" তৈরি করুন। এই অ্যাপটি একটি বিষয় সম্পর্কে প্রশ্নের উত্তর দিতে সক্ষম হওয়া উচিত, যেমন Python। আপনি এমন প্রম্পট রাখতে পারেন, "Python এ একটি নির্দিষ্ট বিষয় কী?", অথবা এমন প্রম্পট রাখতে পারেন যা বলে, আমাকে একটি নির্দিষ্ট বিষয়ে কোড দেখাও ইত্যাদি।
- ইতিহাস বট, ইতিহাসকে জীবন্ত করুন, বটকে একটি নির্দিষ্ট ঐতিহাসিক চরিত্র হিসেবে নির্দেশ দিন এবং তার জীবন ও সময় সম্পর্কে প্রশ্ন করুন।

## সমাধান

### স্টাডি বাডি

নিচে একটি শুরু করার প্রম্পট দেওয়া হলো, দেখুন কীভাবে এটি ব্যবহার করতে পারেন এবং আপনার পছন্দমতো পরিবর্তন করতে পারেন।

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

1. এটি নিয়ন্ত্রণ করে আউটপুট কতটা এলোমেলো হবে।
1. এটি নিয়ন্ত্রণ করে প্রতিক্রিয়ার আকার কত বড় হবে।
1. এটি নিয়ন্ত্রণ করে কতগুলো টোকেন ব্যবহার হবে।

## 🚀 চ্যালেঞ্জ

অ্যাসাইনমেন্টে কাজ করার সময়, তাপমাত্রা পরিবর্তন করার চেষ্টা করুন, ০, ০.৫, এবং ১ সেট করুন। মনে রাখবেন ০ সবচেয়ে কম বৈচিত্র্যময় এবং ১ সবচেয়ে বেশি। আপনার অ্যাপের জন্য কোন মান সবচেয়ে ভালো কাজ করে?

## দুর্দান্ত কাজ! আপনার শেখা চালিয়ে যান

এই পাঠ শেষ করার পর, আমাদের [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) দেখুন যাতে আপনার Generative AI জ্ঞান আরও উন্নত হয়!

পরবর্তী পাঠ ৭ এ যান যেখানে আমরা দেখব কিভাবে [চ্যাট অ্যাপ্লিকেশন তৈরি করতে হয়](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।