# ការសាងសង់កម្មវិធីបង្កើតអត្ថបទ

[![ការសាងសង់កម្មវិធីបង្កើតអត្ថបទ](../../../translated_images/km/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(ចុចរូបភាពខាងលើដើម្បីមើលវីដេអូមេរៀននេះ)_

អ្នកបានឃើញនៅមុននេះតាមរយៈមេរៀននេះថាមានគំនិតមូលដ្ឋានដូចជា prompts និងវិស័យមួយទាំងមូលដែលហៅថា "engineering prompt"។ ឧបករណ៍ជាច្រើនដែលអ្នកអាចធ្វើអ៊ីនធឺរ៉ាក់ទិចជាមួយដូចជា ChatGPT, Office 365, Microsoft Power Platform និងផ្សេងទៀត គាំទ្រអ្នកក្នុងការប្រើ prompts ដើម្បីប completing task មួយ។

ដើម្បីបន្ថែមបទពិសោធន៍បែបនេះទៅកម្មវិធីមួយ អ្នកត្រូវឲ្យយល់ច្បាស់ពីគំនិតដូចជា prompts, completions ហើយជ្រើសរើសបណ្ណាល័យមួយដើម្បីធ្វើការជាមួយ។ នេះជាការសិក្សាដែលអ្នកនឹងរៀនក្នុងជំពូកនេះ។

## ការណែនាំ

ក្នុងជំពូកនេះ អ្នកនឹង:

- រៀនអំពីបណ្ណាល័យ openai និងគំនិតមូលដ្ឋានរបស់វា។
- បង្កើតកម្មវិធីបង្កើតអត្ថបទដោយប្រើ openai។
- ស្វែងយល់ពីរបៀបប្រើគំនិតដូចជា prompt, temperature និង tokens ដើម្បីបង្កើតកម្មវិធីបង្កើតអត្ថបទ។

## គោលដៅសិក្សា

នៅចុងបញ្ជាក់នៃមេរៀននេះ អ្នកនឹងអាច:

- ពន្យល់អំពីថាតើកម្មវិធីបង្កើតអត្ថបទជាអ្វី។
- បង្កើតកម្មវិធីបង្កើតអត្ថបទដោយប្រើ openai។
- កំណត់លំនាំកម្មវិធីរបស់អ្នកឲ្យប្រើ tokens ច្រើន ឬ តិច ហើយផ្លាស់ប្តូរពីកំដៅ (temperature) សម្រាប់លទ្ធផលខុសគ្នា។

## តើកម្មវិធីបង្កើតអត្ថបទជាអ្វី?

ជារឿយៗពេលអ្នកបង្កើតកម្មវិធីមួយ វាមានផ្ទៃមុខដូចជា៖

- ជាលក្ខណៈបញ្ជា។ កម្មវិធី console គឺជាកម្មវិធីផ្ដោតលើបញ្ជា ដែលអ្នកវាយបញ្ជា មួយហើយវាប្រតិបត្តិភារកិច្ចមួយ។ ឧទាហរណ៍ `git` គឺជាកម្មវិធីប្រើបញ្ជា។
- ផ្ទៃមុខអ្នកប្រើ (UI)។ កម្មវិធីខ្លះមានផ្ទៃមុខអ្នកប្រើជា graphical user interface (GUIs) ដែលអ្នកអាចចុចប៊ូតុង វាយអត្ថបទ ជ្រើសរើសជម្រើស និងផ្សេងៗទៀត។

### កម្មវិធី console និង UI មានកំណត់

ប្រៀបធៀបទៅនឹងកម្មវិធីប្រើបញ្ជាមួយដែលអ្នកវាយបញ្ជា៖

- **វាមានកំណត់**។ អ្នកមិនអាចវាយបញ្ជា ណាមួយដោយគ្រាន់តែចង់បានទេ តែត្រឹមតែបញ្ជាដែលកម្មវិធីគាំទ្រ។
- **ពិភាសាពិសេស**។ កម្មវិធីខ្លះគាំទ្រភាសាច្រើន ប៉ុន្តែដោយផ្ទាល់មួយកម្មវិធីត្រូវបានបង្កើតសម្រាប់ភាសាណាមួយ បើទោះបីអ្នកអាចបន្ថែមការគាំទ្រភាសាច្រើនក៏ដោយ។

### ពិសោធន៍ល្អនៃកម្មវិធីបង្កើតអត្ថបទ

តើកម្មវិធីបង្កើតអត្ថបទមានភាពខុសគ្នាយ៉ាងដូចម្តេច?

នៅក្នុងកម្មវិធីបង្កើតអត្ថបទ អ្នកមានភាពអាចបត់បែនច្រើនជាងនេះ អ្នកមិនមានកំណត់នឹងបញ្ជាឬភាសាបញ្ចូលជាក់លាក់ទេ។ ផ្ទុយទៅវិញ អ្នកអាចប្រើភាសាប្រលោមលោកដើម្បីធ្វើអ៊ីនធើរកម្មវិធី។ ផលប្រយោជន៍ផ្សេងគឺអ្នកកំពុងធ្វើអ៊ីនធឺរ៉ាក់ទិចជាមួយប្រភពទិន្នន័យដែលបានហ្វឹកហាត់លើ corpus ព័ត៌មានធំនៅពេលដែលកម្មវិធីប្រពៃណីអាចមានកំណត់លើអ្វីដែលមាននៅក្នុង database។

### តើខ្ញុំអាចបង្កើតអ្វីបានជាមួយកម្មវិធីបង្កើតអត្ថបទ?

មានរឿងជាច្រើនដែលអ្នកអាចបង្កើតបាន។ ឧទាហរណ៍៖

- **chatbot**។ chatbot ដែលឆ្លើយសំណួរអំពីប្រធានបទដូចជាក្រុមហ៊ុន និងផលិតផលរបស់អ្នកអាចជាជម្រើសល្អមួយ។
- **ជួយការ**។ LLMs សក្ដិសមសម្រាប់ការតូចតាចអត្ថបទ ស្វែងយល់ពីអត្ថបទ បង្កើតអត្ថបទដូច resume និងផ្សេងៗទៀត។
- **ជំនួយការ Code**។ អាស្រ័យទៅលើម៉ូឌែលភាសាដែលអ្នកប្រើ អ្នកអាចបង្កើតជំនួយការសរសេរកូដ បាន។ ឧទាហរណ៍ អ្នកអាចប្រើផលិតផលដូចជា GitHub Copilot រួមជាមួយ ChatGPT ដើម្បីជួយសរសេរកូដ។

## តើខ្ញុំអាចចាប់ផ្តើមដោយរបៀបណា?

អ្នកត្រូវស្វែងរកវិធីសាស្រ្តរួមបញ្ចូលជាមួយ LLM ដែលភាគច្រើនមានពីររបៀបដូចខាងក្រោម៖

- ប្រើ API។ នេះអ្នកកំពុងរៀបចំសំណើវែបដោយប្រាប់ prompt របស់អ្នក ហើយទទួលអត្ថបទបង្កើតវិញ។
- ប្រើបណ្ណាល័យ។ បណ្ណាល័យជួយបិទបាំងការហៅ API ហើយធ្វើឲ្យវាងាយស្រួលប្រើ។

## បណ្ណាល័យ/SDKs

មានបណ្ណាល័យពេញនិយមមួយចំនួនសម្រាប់ការធ្វើការជាមួយ LLMs ដូចជា៖

- **openai**, បណ្ណាល័យនេះធ្វើឲ្យងាយស្រួលក្នុងការតភ្ជាប់ទៅម៉ូឌែលរបស់អ្នក និងផ្ញើ prompts។

បន្ទាប់ពីមានបណ្ណាល័យដែលដំណើរការលើកម្រិតខ្ពស់ជាងនេះដូចជា៖

- **Langchain**. Langchain មានខ្លឹមសារល្បី និងគាំទ្រ Python។
- **Semantic Kernel**. Semantic Kernel ជាបណ្ណាល័យដោយ Microsoft គាំទ្រភាសា C#, Python និង Java។

## កម្មវិធីដំបូងប្រើ openai

មកមើលរបៀបដែលយើងអាចបង្កើតកម្មវិធីដំបូង របៀបត្រូវមានបណ្ណាល័យ អ្វីកាចាំបាច់ និងអ្វីផ្សេងទៀត។

### ដំឡើង openai

មានបណ្ណាល័យជាច្រើនសម្រាប់ធ្វើអ៊ីនធឺរ៉ាក់ទិចជាមួយ OpenAI ឬ Azure OpenAI។ អាចប្រើភាសាកម្មវិធីជាច្រើនដូចជា C#, Python, JavaScript, Java និងផ្សេងទៀត។ យើងបានជ្រើសរើសប្រើបណ្ណាល័យ Python `openai` ដូច្នេះយើងនឹងប្រើ `pip` ដើម្បីដំឡើងវា។

```bash
pip install openai
```

### បង្កើតធនធាន

អ្នកត្រូវអនុវត្តជំហានខាងក្រោម៖

- បង្កើតគណនីលើ Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)។
- ទទួលបានការចូលដំណើរការ Azure OpenAI។ ចូលទៅកាន់ [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) ហើយស្នើសុំការចូលដំណើរការ។

  > [!NOTE]
  > នៅពេលសរសេរ អ្នកត្រូវដាក់ពាក្យសុំចូលដំណើរការ Azure OpenAI។

- ដំឡើង Python <https://www.python.org/>
- មានធនធាន Azure OpenAI Service រួចហើយ។ មើលមគ្គុទេសក៍នេះសម្រាប់របៀប [បង្កើតធនធាន](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)។

### រកគន្លុះ API និងចំណុចបញ្ចប់

នៅពេលនេះ អ្នកត្រូវប្រាប់បណ្ណាល័យ `openai` របស់អ្នកពីគន្លុះ API ដែលត្រូវប្រើ។ ដើម្បីស្វែងរកគន្លុះ API របស់អ្នក ចូលទៅផ្នែក "Keys and Endpoint" នៃធនធាន Azure OpenAI របស់អ្នក ហើយចម្លងតម្លៃ "Key 1"។

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

ឥឡូវនេះ អ្នកបានចម្លងព័ត៌មាននេះរួច តោះយើងណែនាំបណ្ណាល័យឲ្យប្រើវា។

> [!NOTE]
> វាមានតម្លៃក្នុងការផ្លាស់ប្តូរគន្លុះ API របស់អ្នកពីកូដរបស់អ្នក។ អ្នកអាចធ្វើបានដោយប្រើអថេរបរិស្ថាន។
>
> - កំណត់អថេរបរិស្ថាន `OPENAI_API_KEY` ទៅគន្លុះ API របស់អ្នក។
>   `export OPENAI_API_KEY='sk-...'`

### កំណត់ការបញ្ជូនកំណត់ Azure

ប្រសិនបើអ្នកប្រើ Azure OpenAI (ឥឡូវជាផ្នែកមួយនៃ Microsoft Foundry) នេះជារបៀបកំណត់កំណត់។ យើងប្រើ client `OpenAI` ដែលត្រូវបញ្ជូនទៅចំណុចបញ្ចប់ Azure OpenAI `/openai/v1/` ដែលដំណើរការជាមួយ Responses API ហើយមិនចាំបាច់មាន `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

នៅលើនេះយើងកំពុងកំណត់៖

- `api_key`, នេះគឺជាគន្លុះ API របស់អ្នកដែលស្វែងរកបាននៅក្នុង Azure Portal ឬ Microsoft Foundry portal។
- `base_url`, នេះគឺជា ចំណុចបញ្ចប់ធនធាន Foundry របស់អ្នកដែលមាន `/openai/v1/` បន្ថែមចុង។ ចំណុចបញ្ចប់ v1 ដែលមានស្ថិរភាពដំណើរការភ្ជាប់ជាមួយ OpenAI និង Azure OpenAI ដោយមិនចាំបាច់គ្រប់គ្រង `api_version`។

> [!NOTE] > `os.environ` អានអថេរបរិស្ថាន។ អ្នកអាចប្រើវាដើម្បីអានអថេរបរិស្ថានដូចជា `AZURE_OPENAI_API_KEY` និង `AZURE_OPENAI_ENDPOINT`។ កំណត់អថេរបរិស្ថានទាំងនេះក្នុង terminal របស់អ្នក ឬប្រើបណ្ណាល័យដូចជា `dotenv`។

## បង្កើតអត្ថបទ

វិធីសាស្រ្តបង្កើតអត្ថបទគឺប្រើ Responses API តាមវិធីសាស្រ្ត `responses.create`។ នេះជាឧទាហរណ៍៖

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # នេះគឺជាឈ្មោះការចែកចាយម៉ូដែលរបស់អ្នក
    input=prompt,
    store=False,
)
print(response.output_text)
```

នៅក្នុងកូដខាងលើ យើងបង្កើតការឆ្លើយតបហើយបញ្ជូនម៉ូឌែលដែលយើងចង់ប្រើ និង prompt។ បន្ទាប់មក យើងបោះពុម្ភអត្ថបទបានបង្កើតតាមរយៈ `response.output_text`។

### ការពិភាក្សាច្រើនជុំ

Responses API ល្អសម្រាប់ទាំងការបង្កើតអត្ថបទជុំជាក់តែម្ដង និង chatbots ពហុជុំ - អ្នកផ្តល់នូវបញ្ជីសារនៅក្នុង `input` ដើម្បីកសាងការពិភាក្សា៖

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

ព័ត៌មានលម្អិតបន្ថែមអំពីមុខងារនេះនឹងមាននៅជំពូកមកក្រោយ។

## ហាត់ប្រាណ - កម្មវិធីបង្កើតអត្ថបទដំបូងរបស់អ្នក

ឥឡូវនេះយើងបានរៀនរបៀបកំណត់ និងកំណត់តម្លៃ openai រួចហើយ ពេលគឺដើម្បីបង្កើតកម្មវិធីបង្កើតអត្ថបទដំបូងរបស់អ្នក។ ដើម្បីបង្កើតកម្មវិធីអោយធ្វើតាមជំហានខាងក្រោម៖

1. បង្កើតបរិស្ថានវីរុវល និងដំឡើង openai៖

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > ប្រសិនបើអ្នកប្រើ Windows វាយ `venv\Scripts\activate` ជំនួស `source venv/bin/activate`។

   > [!NOTE]
   > ស្វែងរកគន្លុះ Azure OpenAI របស់អ្នកដោយចូលទៅ [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) ហើយស្វែងរក `Open AI` ជ្រើសរើស `Open AI resource` បន្ទាប់មកជ្រើសរើស `Keys and Endpoint` ហើយចម្លងតម្លៃ `Key 1`។

1. បង្កើតឯកសារ _app.py_ ហើយសរសេរកូដដូចខាងក្រោម៖

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # បន្ថែមកូដបញ្ចប់របស់អ្នក
   prompt = "Complete the following: Once upon a time there was a"

   # ផ្ញើការស្នើសុំប្រើ Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # បោះពុម្ពចម្លើយ
   print(response.output_text)
   ```

   > [!NOTE]
   > ប្រសិនបើអ្នកប្រើ OpenAI ដ៏សាមញ្ញ(មិនមែន Azure) ប្រើ `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (គ្មាន `base_url`) ហើយបញ្ជូនឈ្មោះម៉ូឌែលដូចជា `gpt-5-mini` ជំនួសឈ្មោះការចាក់ផ្សាយ។

   អ្នកគួរមើលឃើញលទ្ធផលដូចខាងក្រោម៖

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## ប្រភេទផ្សេងៗនៃ prompt សម្រាប់រឿងផ្សេងៗ

ឥឡូវនេះអ្នកបានឃើញរបៀបបង្កើតអត្ថបទដោយប្រើ prompt។ អ្នកក៏មានកម្មវិធីដំណើរការហើយដែលអ្នកអាចកែប្រែ និងផ្លាស់ប្តូរដើម្បីបង្កើតប្រភេទអត្ថបទផ្សេងៗ។

Prompts អាចប្រើសម្រាប់ភារកិច្ចវែងៗជាច្រើន ។ ឧទាហរណ៍៖

- **បង្កើតប្រភេទអត្ថបទ**។ ឧទាហរណ៍ អ្នកអាចបង្កើតកវី តម្រូវសំណួរសម្រាប់ល្បែង quiz និងផ្សេងៗទៀត។
- **ស្វែងរកព័ត៌មាន**។ អ្នកអាចប្រើ prompt ដើម្បីស្វែងរកព័ត៌មានដូចជាគំរូ 'CORS មានអ្វីក្នុងការអភិវឌ្ឍន៍បណ្តាញ?'។
- **បង្កើតកូដ**។ អ្នកអាចប្រើ prompt ដើម្បីបង្កើតកូដ ខណៈដែលអភិវឌ្ឍនregexp ដើម្បីធ្វើបច្ចោបច្ច័យអ៊ីមែល ឬ មិនដឹងតើដូចម្តេចត្រូវបង្កើតកម្មវិធីសរុបមួយដូចជា web app?

## ករណីប្រើប្រាស់ជាក់ស្តែងជាងនេះ៖ កម្មវិធីបង្កើតរូបមន្តចម្អិន

ស្រមើលទៅថាអ្នកមានគ្រឿងផ្សំនៅផ្ទះ និងចង់ចម្អិនអ្វីមួយ។ សម្រាប់នេះ អ្នកត្រូវការរូបមន្តចម្អិន។ របៀបស្វែងរករូបមន្តគឺប្រើម៉ាស៊ីនស្វែងរក ឬអ្នកអាចប្រើ LLM ដើម្បីធ្វើដូចនេះ។

អ្នកអាចសរសេរបញ្ចូល prompt ដូចខាងក្រោម៖

> "បង្ហាញខ្ញុំរូបមន្តចម្អិន ៥ ដែលមានគ្រឿងបញ្ចូលៈ មាន់, ដំឡូង, និងក្រូចឆ្មារ។ សម្រាប់រូបមន្តនីមួយៗ សូមរាប់បញ្ជីគ្រឿងសំភារៈទាំងអស់ដែលបានប្រើ។"

ដោយផ្អែកលើ prompt ខាងលើ អ្នកអាចទទួលបានចម្លើយដូចខាងក្រោម៖

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

លទ្ធផលនេះយ៉ាងអស្ចារ្យ ខ្ញុំដឹងតើយ៉ាងដូចម្តេចចម្អិន។ នៅពេលនេះ អ្វីដែលអាចជាមេរាងវៃឆ្លាតគឺ៖

- ការរើសកន្លែងគ្រឿងផ្សំដែលខ្ញុំមិនចូលចិត្ត ឬធ្វើអោយប៉ះពាល់ផ្នែកសុខភាព។
- បង្កើតបញ្ជីទំនិញ ដើម្បីបញ្ជាក់បើខ្ញុំមិនមានគ្រឿងផ្សំទាំងអស់នៅផ្ទះ។

សម្រាប់ករណីខាងលើ អ្នកអាចបន្ថែម prompt បន្ថែម៖

> "សូមយករូបមន្តដែលមានខ្ទឹមពីក្នុងមួយចេញទៀត សម្រាប់ខ្ញុំដែលអាលហ្ស៊ី ហើយជំនួសវាដោយអ្វីមួយផ្សេងទៀត។ លើសពីនេះសូមបង្កើតបញ្ជីទំនិញសម្រាប់រូបមន្ត ខណៈដែលខ្ញុំមានមាន់ ដំឡូង និងក្រូចឆ្មារស្រាប់នៅផ្ទះ។"

ឥឡូវនេះ អ្នកមានលទ្ធផលថ្មី គឺ៖

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

លោកអ្នកមានរូបមន្តប្រាំនេះ ដែលគ្មានខ្ទឹមដាក់ក្នុងរូបមន្ត និងមានបញ្ជីទំនិញដោយគិតពីអ្វីដែលអ្នកមាននៅផ្ទះរួចហើយ។

## ហាត់ប្រាណ - បង្កើតកម្មវិធីបង្កើតរូបមន្ត

ឥឡូវនេះ បណ្ដើរពិធីសិតនេះត្រូវបានបង្ហាញ អ្នកត្រូវសរសេរកូដដើម្បីឆ្លើយតបផលបង្ហាញនេះ។ ដើម្បីធ្វើដូច្នេះ សូមអនុវត្តជំហានដូចខាងក្រោម៖

1. ប្រើឯកសារ _app.py_ ដែលមានស្រាប់ជាចំណុចចាប់ផ្តើម
1. រកអថេរ `prompt` ហើយផ្លាស់ប្តូរកូដរបស់វាទៅដូចខាងក្រោម៖

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   ប្រសិនបើអ្នកដំណើរការ code ឥឡូវនេះ អ្នកគួរមានលទ្ធផលដូចខាងក្រោម៖

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ទន្ទឹមនេះ LLM របស់អ្នកមិនមែនជាស្ថិតស្ថេរទេ ដូច្នេះអ្នកប្រហែលជានឹងទទួលលទ្ធផលខុសគ្នាតែងតែពេលអ្នកដំណើរការ។

   ល្អណាស់ តោះទៅមើលរបៀបធ្វើឲ្យវាល្អប្រសើរឡើង។ ដើម្បីធ្វើឲ្យវាល្អប្រសើរឡើង អ្នកចង់ធ្វើឲ្យកូដអាចបត់បែន បានដូច្នេះគ្រឿងផ្សំ និងចំនួនរូបមន្តអាចកែលម្អ ហើយផ្លាស់ប្តូរបាន។

1. តោះផ្លាស់ប្តូរកូដក្នុងរបៀបដូចខាងក្រោម៖

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # បញ្ចូលចំនួនสูตรចូលក្នុងការស្នើសុំ និងគ្រឿងផ្សំ
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   ការយកកូដសម្រាប់ការប្រតិបត្តិការធ្វើតេស្ត អាចមានរបៀបដូចខាងក្រោម៖

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### បង្កើនលក្ខណៈដោយបន្ថែមការត្រង់ និងបញ្ជីទិញទំនិញ

ឥឡូវនេះយើងមានកម្មវិធីដំណើរការអាចបង្កើតរូបមន្ត ហើយវាអាចបត់បែនបាន ពីព្រោះវាអាស្រ័យលើការបញ្ចូលពីអ្នកប្រើ សង្កត់លើចំនួនរូបមន្ត និងគ្រឿងផ្សំដែលប្រើ។

ដើម្បីផ្ដល់ការកែលម្អបន្ថែម យើងចង់បន្ថែម៖

- **ត្រង់គ្រឿងផ្សំ**។ យើងចង់អាចត្រង់គ្រឿងផ្សំដែលយើងមិនចូលចិត្ត ឬដែលធ្វើអោយប៉ះពាល់សុខភាព។ ដើម្បីធ្វើការផ្លាស់ប្តូរនេះ អ្នកអាចកែប្រែ prompt ស្រាប់របស់យើង ហើយបន្ថែមលក្ខខណ្ឌត្រង់នៅចុងវា ដូចខាងក្រោម៖

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  នៅលើនេះ យើងបន្ថែម {filter} នៅចុង prompt ហើយយើងក៏ទទួលស្វែងចំនួន filter ពីអ្នកប្រើផងដែរ។

  ឧទាហរណ៍នៃការបញ្ចូលក្នុងកម្មវិធីអាចមានរបៀបដូចខាងក្រោម៖

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

  ដូចដែលអ្នកឃើញ រូបមន្តណាមួយមានដូងបានត្រូវត្រង់ចេញ។ ប៉ុន្តែ ប្រសិនបើអ្នកចាញ់ទឹកដោះគោ អ្នកអាចចង់ត្រង់រូបមន្តដែលមានឈីសផងដែរ ដូច្នេះមានតម្រូវការកំណត់អោយច្បាស់។


- **ផលិតបញ្ជីធ្វើសងចំណាំ** ។ យើងចង់ផលិតបញ្ជីធ្វើសងចំណាំ គិតពីអ្វីដែលយើងមាននៅផ្ទះរួចហើយ។

  សម្រាប់មុខងារនេះ យើងអាចសាកល្បងដំណោះស្រាយគ្រប់យ៉ាងក្នុងការបញ្ចូលមួយ ឬអាចបំបែកវាជាពីរការបញ្ចូល។ ចូរសាកល្បងវិធីបន្ទាប់។ នៅទីនេះ យើងបញ្ជាក់អំពីការបន្ថែមការបញ្ចូលបន្ថែមមួយ ប៉ុន្តែមុននឹងខាងក្រោម គួរតែបន្ថែមលទ្ធផលនៃការបញ្ចូលដើមជាសេចក្ដីបរិបទទៅការបញ្ចូលបន្ទាប់។

  ស្វែងរកផ្នែកក្នុងកូដដែលបង្ហាញលទ្ធផលពីការបញ្ចូលដើម ហើយបន្ថែមកូដដូចខាងក្រោម៖

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # បោះពុម្ពចេញការឆ្លើយតប
  print("Shopping list:")
  print(response.output_text)
  ```

  សម្គាល់អ្វីខាងក្រោម៖

  1. យើងកំពុងកសាងការបញ្ចូលថ្មីដោយបន្ថែមលទ្ធផលពីការបញ្ចូលដើមទៅការបញ្ចូលថ្មី៖

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. យើងធ្វើសំណើថ្មី ប៉ុន្តែស្តាប់លំអិតចំនួនតូកិនដែលយើងបានស្នើរនៅក្នុងការបញ្ចូលដើម ដូច្នេះពេលនេះយើងនិយាយថា `max_output_tokens` គឺ ១២០០។

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     យកកូដនេះពង្រីកលេង យើងភ្លាមឈានដល់លទ្ធផលដូចខាងក្រោម៖

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## បង្កើនការតំឡើងរបស់អ្នក

អ្វីដែលយើងមានជាឥឡូវនេះគឺកូដដែលបច្ចុប្បន្នប្រតិបត្តិបាន ប៉ុន្តែក៏មានការកែលម្អខ្លះៗដែលយើងគួរធ្វើបន្ថែម។ ការងារខ្លះៗដែលយើងគួរធ្វើមានដូចជា៖

- **បំបែកសម្ងាត់ពីកូដ**, ដូចជា key API។ សម្ងាត់មិនគួររក្សាទុកក្នុងកូដទេ និងគួរតែរក្សាទុកនៅកន្លែងមានសុវត្ថិភាព។ ដើម្បីបំបែកសម្ងាត់ពីកូដ យើងអាចប្រើភាគល្អិតបរិស្ថាន និងបណ្ណាល័យដូចជា `python-dotenv` ដើម្បីផ្ទុកពួកវាពីផ្ទាំងឯកសារ។ នេះគឺជារបៀបដែលវាមានរូបរាងនៅក្នុងកូដ៖

  1. បង្កើតឯកសារ `.env` ជាមួយខាងក្រោម៖

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > សម្គាល់, សម្រាប់ Azure OpenAI នៅ Microsoft Foundry, អ្នកត្រូវកំណត់ភាគល្អិតបរិស្ថានដូចខាងក្រោមជំនួស៖

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     នៅក្នុងកូដ អ្នកអាចផ្ទុកភាគល្អិតបរិស្ថានដូចខាងក្រោម៖

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **ពីសព្វថ្ងៃ token length**។ យើងគួរពិចារណាពីចំនួន tokens ដែលយើងត្រូវការដើម្បីបង្កើតអត្ថបទដែលយើងចង់បាន។ tokens មានតម្លៃចំណាយហើយ ដូច្នេះនៅទីកន្លែងដែលអាចធ្វើបាន យើងគួរប្រើ tokens ឲ្យម៉ត់ចត់បំផុត។ ឧទាហរណ៍ អាចធ្វើអោយ prompt មានទម្រង់ដែលអាចប្រើ tokens ទាបជាងមុនបានទេ?

  ដើម្បីផ្លាស់ប្ដូរចំនួន tokens ដែលប្រើ អ្នកអាចប្រើប៉ារ៉ាម៉ែត្រ `max_output_tokens`។ ឧទាហរណ៍ បើចង់ប្រើ ១០០ tokens អ្នកអាចធ្វើដូចខាងក្រោម៖

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **សាកល្បងជាមួយសីតុណ្ហភាព**។ សីតុណ្ហភាពគឺជាអ្វីមួយដែលយើងមិនទាន់បានរំលឹកទេទេ ប៉ុន្តែនេះជា context สำคัญណាស់សម្រាប់របៀបដែលកម្មវិធីយើងប្រតិបត្តិ។ តម្លៃសីតុណ្ហភាពខ្ពស់ បង្ហាញពីលទ្ធផលចៃដន្យច្រើនជាង។ ផ្ទុយទៅវិញ តម្លៃសីតុណ្ហភាពទាបបង្ហាញពីលទ្ធផលច្បាស់លាស់និងទុកចិត្តបាន។ ពិចារណាថាអ្នកចង់មានភាពបែបបន្ធូរបន្ថែម ឬមិនមាន។

  ដើម្បីផ្លាស់ប្ដូរសីតុណ្ហភាព អ្នកអាចប្រើប៉ារ៉ាម៉ែត្រ `temperature`។ ឧទាហរណ៍ បើចង់ប្រើសីតុណ្ហភាព 0.5 អ្នកអាចធ្វើដូចខាងក្រោម៖

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > សម្គាល់, តម្លៃជិត 1.0 លទ្ធផលនឹងមានភាពខុសគ្នាខ្លាំង។

- **ម៉ូដែលមិនប្រើ `temperature`**។ នេះជាចំហាល់សំខាន់សម្រាប់ឆ្នាំ ២០២៦។ ម៉ូដែលដែលមិនបញ្ឈប់ការគាំទ្រ នៅ Microsoft Foundry គឺម៉ូដែល reasoning (គ្រួសារ GPT-5, o-series) - ហើយពួកវា **មិនគាំទ្រ `temperature` ឬ `top_p`** (ហើយមិនគាំទ្រ `max_tokens`; សូមប្រើ `max_output_tokens`) មិនមានទេ។ ប្រសិនបើអ្នកផ្ញើ `temperature` ទៅ `gpt-5-mini` អ្នកនឹងទទួលបានកំហុស "parameter not supported"។ ដើម្បីសាកល្បងឧទាហរណ៍សីតុណ្ហភាពខាងលើ សូមបញ្ជូនទៅម៉ូដែលដែលនៅតែគាំទ្រការគ្រប់គ្រងការស្ទូច - ឧទាហរណ៍ម៉ូដែល open **Llama** ដូចជា `Llama-3.3-70B-Instruct` ពី [ទឹកជំហានម៉ូដែល Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), ដែលហៅតាម Foundry Models / Azure AI Inference endpoint (ដូចគ្នារូបមន្តជាមួយម៉ូដែល `githubmodels-*`) សម្រាប់ reasoning models ដូចជា GPT-5 អ្នកគ្រប់គ្រងលទ្ធផលដោយវិនិយោគខុសៗគ្នា៖
  - **Prompt engineering** - សេចក្តីណែនាំច្បាស់លាស់, ឧទាហរណ៍, និងលទ្ធផលមានរចនាសម្ព័ន្ធ (មើលមេរៀន [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) ធ្វើការងារដែល sampling knobs បានធ្វើមុន។
  - **ការគ្រប់គ្រង reasoning** - ប៉ារ៉ាម៉ែត្រ ដូចជា ការខិតខំ/ពណ៌នាយ៉ាងពិសេស សំរាប់រកការគ្រប់គ្រងជម្រៅ reasoning ប្រៀបធៀបនឹងពេលយឺតនិងតម្លៃ។

  សង្ខេប៖ `temperature`/`top_p` នៅតែមានប្រយោជន៍សម្រាប់ម៉ូដែលជាច្រើន (Llama, Mistral, Phi, និងគ្រួសារ GPT-4.x - ទោះបីជា GPT-4.x កំពុងឈប់ប្រើ), ប៉ុន្តូចំណុចដឹកនាំគឺ prompt engineering + reasoning controls សម្រាប់ reasoning models ដូចជា GPT-5។

## បំណងបេសកកម្ម

សម្រាប់បន្ទុកបេសកកម្មនេះ អ្នកអាចជ្រើសរើសអ្វីដែលអាចសង់បាន។

នេះជាការផ្តល់អនុសាសន៍មួយចំនួន៖

- កែប្រែកម្មវិធីចាក់ស្ដើងម្ហូបដើម្បីធ្វើឲ្យវាបានល្អឡើងទៀត។ ល្បែងជាមួយតម្លៃសីតុណ្ហភាព និងprompt ដើម្បីមើលថាអ្នកអាចបង្កើតអ្វីបានខ្លះ។
- សាងសង់ "មិត្តសិក្សា"។ កម្មវិធីនេះគួរអាចឆ្លើយសំណួរអំពីប្រធានបទណាមួយ ដូចជា Python អ្នកអាចមាន prompt ដូចជា "តើប្រធានបទមួយចំនួននៅ Python ជាអ្វី?" ឬអ្នកអាចមាន prompt ដែលថា ចូរបង្ហាញកូដសម្រាប់ប្រធានបទមួយចំនួន។
- បុរសប្រវត្តិសាស្ត្រ, ធ្វើឲ្យប្រវត្តិសាស្ត្រមានជីវិតឡើងវិញ, សូមណែនាំបុរសប្រវត្តិសាស្ត្រផ្សេងទៀត ហើយសួរពីជីវិត និងពេលវេលារបស់វា។

## ដំណោះស្រាយ

### មិត្តសិក្សា

ខាងក្រោមគឺជាការបញ្ចូលចាប់ផ្ដើម មើលថាអ្នកអាចប្រើវា ហើយប្ដូរយ៉ាងដូចម្តេចឲ្យសមស្រប។

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### បុរសប្រវត្តិសាស្ត្រ

នេះជាការបញ្ចូលខ្លះដែលអ្នកអាចប្រើបាន៖

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## ការត្រួតពិនិត្យចំណេះដឹង

តើមាតិកាសីតុណ្ហភាពមានន័យយ៉ាងដូចម្តេច?

1. វាគ្រប់គ្រងភាសា random អ្វីដែលបានបញ្ចេញ។
1. វាគ្រប់គ្រងទំហំសំណើតបន្ថែម។
1. វាគ្រប់គ្រងចំនួន tokens ដែលបានប្រើ។

## 🚀 ជំនាញបញ្ញាញ

នៅពេលធ្វើការបេសកកម្ម សូមសាកល្បងប្ដូរថ្មីសីតុណ្ហភាព សាកល្បងកំណត់ទៅ 0, 0.5, និង 1 ។ ជឿថា 0 គឺមានភាពបែបបន្តិចបំផុត និង 1 គឺខាងលើបំផុត។ តម្លៃណាដែលសាកសមសម្រាប់កម្មវិធីរបស់អ្នក?

## អ្នកបានធ្វើបានល្អ! បន្តការសិក្សារបស់អ្នក

បន្ទាប់ពីបញ្ចប់មេរៀននេះ សូមពិនិត្យមើល [ការប្រមូលផ្តុំរៀន Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) របស់យើងដើម្បីបន្តកម្រិតចំណេះដឹង Generative AI របស់អ្នក!

សូមចូលរួមមេរៀនទី 7 ដែលយើងនឹងមើលពីរបៀប [សង់កម្មវិធីchat](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->