# ការបង្កើតកម្មវិធីបង្កើតអត្ថបទ

[![ការបង្កើតកម្មវិធីបង្កើតអត្ថបទ](../../../translated_images/km/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(ចុចរូបភាពខាងលើដើម្បីមើលវីដេអូសម្រាប់មេរៀននេះ)_

អ្នកបានឃើញរហូតមកទល់បច្ចុប្បន្នតាមរយៈមេរៀននេះថា មានគំនិតមូលដ្ឋានដូចជា prompt និងប្រធានបទមួយទូលំទូលាយដែលហៅថា "បច្ចេកវិទ្យា prompt"។ មានឧបករណ៍ជាច្រើនដែលអ្នកអាចធ្វើអន្តរកម្មជាមួយដូចជា ChatGPT, Office 365, Microsoft Power Platform និងផ្សេងទៀត ដែលគាំទ្រអ្នកដោយប្រើ prompt ដើម្បីបំពេញភារកិច្ចមួយណាមួយ។

ដើម្បីឲ្យអ្នកបន្ថែមបទពិសោធន៍ដូចនេះទៅកម្មវិធីមួយ អ្នកត្រូវយល់ពីគំនិតដូចជា prompt, completions និងជ្រើសរើសបណ្ណាល័យមួយសម្រាប់ធ្វើការ។ នេះជាការសិក្សាដែលអ្នកនឹងរៀននៅក្នុងជំពូកនេះ។

## ការណែនាំ

ក្នុងជំពូកនេះ អ្នកនឹង:

- រៀនអំពីបណ្ណាល័យ openai និងគំនិតមូលដ្ឋានរបស់វា។
- បង្កើតកម្មវិធីបង្កើតអត្ថបទដោយប្រើ openai។
- យល់ពីរបៀបប្រើប្រាស់គំនិតដូចជា prompt, temperature, និង tokens ដើម្បីបង្កើតកម្មវិធីបង្កើតអត្ថបទ។

## គោលដៅការសិក្សា

នៅចុងបញ្ចប់មេរៀននេះ អ្នកនឹងអាច:

- ពន្យល់ថាកម្មវិធីបង្កើតអត្ថបទមានអ្វីខ្លះ។
- បង្កើតកម្មវិធីបង្កើតអត្ថបទដោយប្រើ openai។
- កំណត់កម្មវិធីរបស់អ្នកឲ្យប្រើ tokens ច្រើន ឬតិច និងក៏ផ្លាស់ប្តូរ temperature ដើម្បីឲ្យមានលទ្ធផលនានា។

## កម្មវិធីបង្កើតអត្ថបទមានអ្វីខ្លះ?

ជាទូទៅ នៅពេលអ្នកបង្កើតកម្មវិធីមួយ វាមានប្រភេទមួយនៃចំណុចប្រទាក់ដូចខាងក្រោម៖

- មួយដែលផ្អែកលើការបញ្ជា។ កម្មវិធី console ជាកម្មវិធីបែបសរសេរបញ្ជា ហើយវាកែសម្រួលភារកិច្ចមួយ។ ឧទាហរណ៍ `git` គឺកម្មវិធីដែលផ្អែកលើបញ្ជា។
- ចំណុចប្រទាក់អ្នកប្រើ (UI)។ កម្មវិធីខ្លះមានចំណុចប្រទាក់ប្រព័ន្ធប្រើប្រាស់ក្រាហ្វិក(GUI) ដែលអ្នកចុចប៊ូតុង បញ្ចូលអត្ថបទ ជ្រើសរើសជម្រើស និងផ្សេងទៀត។

### កម្មវិធី console និង UI មានកំណត់

ព្យាយាមប្រៀបធៀបវាទៅនឹងកម្មវិធីផ្អែកលើបញ្ជាជាមួយការចុចបញ្ជា៖

- **វាមានកំណត់**។ អ្នកមិនអាចបញ្ចូលបញ្ជាទាំងអស់បានទេ គ្រាន់តែបញ្ជាដែលកម្មវិធីគាំទ្រ។
- **ជាភាសាកំណត់**។ កម្មវិធីខ្លះគាំទ្រភាសាជាច្រើន ប៉ុន្តែកម្មវិធីតែងតែបង្កើតសម្រាប់ភាសាដែលកំណត់ទាំងអស់ ទោះបីជាអ្នកអាចបន្ថែមការគាំទ្រភាសាបាន។

### ប្រយោជន៍នៃកម្មវិធីបង្កើតអត្ថបទ

តើកម្មវិធីបង្កើតអត្ថបទមានអ្វីខុសគ្នា?

នៅក្នុងកម្មវិធីបង្កើតអត្ថបទ អ្នកមានភាពបត់បែនច្រើន ជាងគេ អ្នកមិនត្រូវបានកំណត់ត្រឹមបញ្ជាឬភាសាបញ្ចូលជាក់លាក់ទេ។ ត្រូវប្រើភាសាប្រសើរដើម្បីធ្វើអន្តរកម្មជាមួយកម្មវិធី។ ប្រាក់ចំណេញផ្សេងទៀត គឺអ្នកកំពុងធ្វើអន្តរកម្មជាមួយប្រ៊ូសម្រាវទិន្នន័យដែលបានបណ្តុះបណ្តាលលើទិន្នន័យធំ ក្រោមការពារដោយផ្អែកលើកម្មវិធីបែបបុរាណដែលមានកំណត់ត្រឹមតែអ្វីដែលមានក្នុងកន្លែងទិន្នន័យ។

### តើអ្វីដែលខ្ញុំអាចបង្កើតជាមួយកម្មវិធីបង្កើតអត្ថបទ?

មានអ្វីជាច្រើនដែលអ្នកអាចបង្កើតបាន។ ឧទាហរណ៍៖

- **chatbot**។ chatbot ការឆ្លើយសំណួរអំពីប្រធានបទ ហើយផ្ដល់ពត៌មានអំពីក្រុមហ៊ុន និងផលិតផលរបស់លោកអ្នកអាចនឹងជាជម្រើសល្អ។
- **ជំនួយការ (Helper)**។ LLMs អាចធ្វើការប្រមាណសង្ខេបអត្ថបទ ទាញយកការយល់ដឹងពីអត្ថបទ បង្កើតអត្ថបទដូចជា resume និងផ្សេងទៀត។
- **ជំនួយការសរសេរកូដ**។ អាស្រ័យលើម៉ូឌែលភាសាដែលអ្នកប្រើ អ្នកអាចបង្កើតជំនួយការសរសេរកូដ ជួយសរសេរកូដ។ ឧទាហរណ៍ អ្នកអាចប្រើផលិតផលដូចជា GitHub Copilot និង ChatGPT ដើម្បីជួយសរសេរកូដ។

## តើខ្ញុំអាចចាប់ផ្តើមដូចម្តេច?

ដូច្នេះ អ្នកត្រូវការរកវិធីសម្រាប់ភ្ជាប់ជាមួយ LLM ដែលជារបៀបធម្មតាមមានពីរជម្រើស:

- ប្រើ API។ នៅទីនេះ អ្នកបង្កើតសំណើវេបសាយដោយបញ្ចូល prompt ហើយទទួលបានអត្ថបទដែលបានបង្កើតហើយវិញ។
- ប្រើបណ្ណាល័យ។ បណ្ណាល័យជួយបង្កប់ការហៅ API និងធ្វើឲ្យងាយប្រើ។

## បណ្ណាល័យ/SDKs

មានបណ្ណាល័យមួយចំនួនដែលត្រូវបានគេស្គាល់សម្រាប់ធ្វើការជាមួយ LLM ដូចជា៖

- **openai**, បណ្ណាល័យនេះធ្វើឲ្យងាយស្រួលក្នុងការតភ្ជាប់ទៅម៉ូឌែលរបស់អ្នក និងផ្ញើ prompt។

បន្ទាប់មកមានបណ្ណាល័យដែលដំណើរការលើកម្រិតខ្ពស់ដូចជា៖

- **Langchain**។ Langchain គឺស្គាល់ល្អ និងគាំទ្រភាសា Python។
- **Semantic Kernel**។ Semantic Kernel គឺជាបណ្ណាល័យពី Microsoft គាំទ្រភាសា C#, Python, និង Java។

## កម្មវិធីដំបូងជាមួយ openai

មកមើលវិធីបង្កើតកម្មវិធីដំបូងគេ កន្លែងដែលយើងត្រូវការបណ្ណាល័យ និងតើត្រូវការប៉ុន្មាន។

### ដំឡើង openai

មានបណ្ណាល័យជាច្រើនសម្រាប់អន្តរកម្មជាមួយ OpenAI ឬ Azure OpenAI។ អាចប្រើប្រាស់ភាសាបណ្តុំនានាពីរដូចជា C#, Python, JavaScript, Java និងផ្សេងទៀត។ យើងបានជ្រើសប្រើបណ្ណាល័យ Python `openai` ដូច្នេះយើងនឹងប្រើ `pip` ដើម្បីដំឡើងវា។

```bash
pip install openai
```

### បង្កើត resource

អ្នកត្រូវអនុវត្តជំហានដូចខាងក្រោម៖

- បង្កើតគណនីនៅលើ Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)។
- ទទួលបានការចូលប្រើ Azure OpenAI។ ទៅកាន់ [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) និងស្នើសុំការចូលប្រើ។

  > [!NOTE]
  > នៅពេលនេះ អ្នកត្រូវព្យាយាមដាក់ពាក្យស្នើសុំដើម្បីចូលប្រើ Azure OpenAI។

- ដំឡើង Python <https://www.python.org/>
- មានបានបង្កើត Azure OpenAI Service resource។ សូមមើលមគ្គុទេសក៍នេះសម្រាប់របៀប [បង្កើត resource](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)។

### រក API key និង endpoint

នៅពេលនេះ អ្នកត្រូវប្រាប់បណ្ណាល័យ `openai` របស់អ្នកពី API key ដែលត្រូវប្រើ។ ដើម្បីរក API key របស់អ្នក ទៅទីតាំង "Keys and Endpoint" នៃ resource Azure OpenAI របស់អ្នក ហើយចម្លងតម្លៃ "Key 1"។

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

ឥឡូវក្រោយពេលអ្នកចម្លងព័ត៌មាននេះរួច តោះណែនាំបណ្ណាល័យឲ្យប្រើវា។

> [!NOTE]
> វាគួរឱ្យបំបែក API key របស់អ្នកចេញពីកូដ។ អ្នកអាចធ្វើវាតាមការប្រើប្រាស់ environment variables។
>
> - កំណត់ environment variable `OPENAI_API_KEY` ទៅនឹង API key របស់អ្នក។
>   `export OPENAI_API_KEY='sk-...'`

### កំណត់ការកំណត់រចនាសម្ព័ន្ធ Azure

ប្រសិនបើអ្នកប្រើ Azure OpenAI (ឥឡូវពាក់ផ្តើម Microsoft Foundry) នេះជាវិធីកំណត់រចនាសម្ព័ន្ធ។ យើងប្រើ client `OpenAI` ទូទៅ បង្ហាញទៅកាន់ endpoint Azure OpenAI `/openai/v1/` ដែលដំណើរការជាមួយ API Responses ហើយមិនចាំបាច់មាន `api_version`៖

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

ខាងលើយើងកំពុងកំណត់៖

- `api_key`, នេះជាចន្លោះ API key របស់អ្នកដែលរកបាននៅ Azure Portal ឬ Microsoft Foundry portal។
- `base_url`, នេះជាអាសយដ្ឋាន resource Foundry របស់អ្នកដោយបានបន្ថែម `/openai/v1/`។ stable v1 endpoint ដំណើរការជាទូទៅគ្រប់ OpenAI និង Azure OpenAI មិនចាំបាច់គ្រប់គ្រង `api_version`។

> [!NOTE] > `os.environ` អាន environment variables។ អ្នកអាចប្រើវាដើម្បីអាន environment variables ដូចជា `AZURE_OPENAI_API_KEY` និង `AZURE_OPENAI_ENDPOINT`។ កំណត់ environment variables ទាំងនេះនៅក្នុង terminal របស់អ្នក ឬប្រើបណ្ណាល័យដូចជា `dotenv`។

## បង្កើតអត្ថបទ

របៀបបង្កើតអត្ថបទគឺប្រើ API Responses តាមវិធីសាស្រ្ត `responses.create`។ មានឧទាហរណ៍ដូចខាងក្រោម៖

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

ក្នុងកូដខាងលើ យើងបង្កើត response ហើយផ្តល់ម៉ូឌែលដែលចង់ប្រើ និង prompt។ បន្ទាប់មកយើងបោះពុម្ពអត្ថបទដែលបានបង្កើតតាម `response.output_text`។

### ការសន្ទនាច្រើនជំហាន

API Responses មានសោភ័ណភាពល្អសម្រាប់ការបង្កើតអត្ថបទមួយជំហាន និង chatbot ដែលមានសន្ទនាច្រើនជំហាន - អ្នកផ្តល់បញ្ជីសារជាមួយ `input` ដើម្បីបង្កើតសន្ទនា៖

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

ព័ត៌មានបន្ថែមអំពីមុខងារនេះនៅជំពូកខាងមុខ។

## កិច្ចការអនុវត្ត - កម្មវិធីបង្កើតអត្ថបទដំបូងរបស់អ្នក

ឥឡូវនេះ យើងបានរៀនរបៀបកំណត់ និងកំណត់រចនាសម្ព័ន្ធ openai រួច ខណៈនេះពេលវេលាឯកសារបង្កើតកម្មវិធីបង្កើតអត្ថបទដំបូងរបស់អ្នក។ ដើម្បីបង្កើតកម្មវិធី រុំតាមជំហានដូចខាងក្រោម៖

1. បង្កើតបរិយាកាស virtual ហើយដំឡើង openai៖

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > ប្រសិនបើអ្នកប្រើ Windows សូមវាយ `venv\Scripts\activate` ជំនួស `source venv/bin/activate`។

   > [!NOTE]
   > រក Azure OpenAI key របស់អ្នកដោយទៅកាន់ [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) និងស្វែងរក `Open AI` ចុច `Open AI resource` បន្ទាប់មកជ្រើស `Keys and Endpoint` ហើយចម្លងតម្លៃ `Key 1`។

1. បង្កើតឯកសារ _app.py_ ហើយសរសេរកូដដូចខាងក្រោម៖

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
   > ប្រសិនបើអ្នកប្រើ OpenAI ទូទៅ (មិនមែន Azure) សូមប្រើ `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (មិនមាន `base_url`) និងផ្ដល់ឈ្មោះម៉ូឌែលដូចជា `gpt-5-mini` ជំនួសឈ្មោះ deployment។

   អ្នកគួរតែឃើញលទ្ធផលដូចខាងក្រោម៖

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## ប្រភេទ prompt អន្ដរជាតិនានា សម្រាប់ការងារផ្សេងៗ

ឥឡូវនេះ អ្នកបានឃើញរបៀបបង្កើតអត្ថបទដោយប្រើ prompt។ អ្នកមានកម្មវិធីមួយដំណើរការ និងអាចកែប្រែបំលែងដើម្បីបង្កើតអត្ថបទប្រភេទផ្សេងៗ។

Prompts អាចប្រើសម្រាប់ភារកិច្ចគ្រប់ប្រភេទ។ ឧទាហរណ៍៖

- **បង្កើតអត្ថបទប្រភេទមួយ**។ ឧទាហរណ៍ អ្នកអាចបង្កើតកាព្យ។ សំណួរសម្រាប់វគ្គផ្សេងៗ។
- **ស្វែងរកព័ត៌មាន**។ អ្នកអាចប្រើ prompt ដើម្បីស្វែងរកព័ត៌មាន ដូចជាឧទាហរណ៍ 'CORS មានន័យអ្វីក្នុងការអភិវឌ្ឍវេបសាយ?'។
- **បង្កើតកូដ**។ អ្នកអាចប្រើ prompt ដើម្បីបង្កើតកូដ, ដូចជាការអភិវឌ្ឍ regex សម្រាប់ផ្ទៀងផ្ទាត់អ៊ីមែល ឬបង្កើតកម្មវិធីមួយទាំងមូល ដូចជា web app។

## ករណីប្រើប្រាស់ជាក់ស្តែង: កម្មវិធីបង្កើតរេស៊ីប៊ី

សូមគន់ថាអ្នកមានគ្រឿងផ្សំនៅផ្ទះ ហើយចង់طبْخនូវអ្វីមួយ។ ដើម្បីធ្វើនោះ អ្នកត្រូវការរេស៊ីប៊ីមួយ។ វិធីសម្រាប់ស្វែងរករេស៊ីប៊ីគឺប្រើម៉ាស៊ីនស្វែងរក ឬអាចប្រើ LLM ដើម្បីធ្វើ។

អ្នកអាចសរសេរ prompt ដូចខាងក្រោម៖

> "បង្ហាញខ្ញុំរេស៊ីប៊ី 5 សម្រាប់ម្ហូបផ្អែកលើគ្រឿងផ្សំដូចខាងក្រោម៖ ហុងស៊ុបមាន់, ដំឡូងនិងក្រូចឆ្មារ។ ក្នុងរេស៊ីប៊ីនីមួយៗ សូមរាយបញ្ជីគ្រឿងផ្សំទាំងអស់។"

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

លទ្ធផលនេះល្អណាស់ ខ្ញុំដឹងថាត្រូវធ្វើម្ហូបអ្វី។ នៅពេលនេះ បន្ទាប់ពីលទ្ធផល អ្វីខ្លះជាការកែលម្អមានប្រយោជន៍:

- ការតម្រៀបចេញគ្រឿងផ្សំដែលខ្ញុំមិនស្រឡាញ់ ឬល្អី។
- បង្កើតបញ្ជីទិញសម្រាប់គ្រឿងផ្សំ ប្រសិនបើខ្ញុំមិនមានគ្រឿងផ្សំទាំងអស់នៅផ្ទះ។

សម្រាប់ករណីខាងលើ តោះបន្ថែម prompt មួយទៀត៖

> "សូមដករេស៊ីប៊ីដែលមានខ្ទឹមសេចក្តីខ្ញុំសុទ្ធតែឆ្អែតខ្ទឹម និងជំនួសវាជាអ្វីមួយផ្សេងទៀត។ ក៏សូមបង្កើតបញ្ជីទិញសម្រាប់រេស៊ីប៊ីទាំងនេះ ដោយគិតថាខ្ញុំមានហុងស៊ុបមាន់, ដំឡូងនិងក្រូចឆ្មារួចហើយ។"

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

អ្នកមានរេស៊ីប៊ី 5 នេះដែលមិនបានរៀបរាប់ខ្ទឹម ហើយក៏មានបញ្ជីទិញផងដែរ ដោយគិតថាអ្នកមានគ្រឿងផ្សំហើយនៅផ្ទះ។

## កិច្ចការអនុវត្ត - បង្កើតកម្មវិធីបង្កើតរេស៊ីប៊ី

ឥឡូវនេះ យើងបានលេងករណីជាក់ស្តែងហើយ តោះសរសេរកូដសម្រាប់ត្បាញស្នាដៃតាមសេចក្តីបង្ហាញ។ ដើម្បីធ្វើវា អនុវត្តតាមជំហានទាំងនេះ៖

1. ប្រើឯកសារ _app.py_ មានស្រាប់ជាចំណុចចាប់ផ្តើម។
1. រក `prompt` variable ហើយផ្លាស់ប្តូរកូដរបស់វាទៅដូចខាងក្រោម៖

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   ប្រសិនបើអ្នករត់កូដនេះ យល់ថាលទ្ធផលមានសំណុំទិន្នន័យប្រហែល៖

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > កំណត់សម្គាល់ អ្នក LLM គឺមិនមានលទ្ធផលកំណត់មួយទេ ដូច្នេះអ្នកអាចបានលទ្ធផលផ្សេងគ្នាក្នុងពេលដែលដំណើរការប្រសិនបើបន្ត។

   ល្អណាស់ តោះមើលវិធីកែលម្អ។ ដើម្បីកែលម្អ អ្នកចង់ឲ្យកូដមានបត់បែន ដូច្នេះគ្រឿងផ្សំ និងចំនួនរេស៊ីប៊ីអាចកែប្រែបាន។

1. យើងកែប្រែកូដដោយរបៀបដូចខាងក្រោម៖

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   ការដំណើរការកូដសាកល្បងអាចមានទម្រង់ដូចនេះ៖

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### កែលម្អដោយបន្ថែមតម្រង និងបញ្ជីទិញ

ឥឡូវនេះ យើងមានកម្មវិធីដំណើរការដែលអាចបង្កើតរេស៊ីប៊ី ហើយវាបត់បែនព្រោះវាអាស្រ័យលើការបញ្ចូលពីអ្នកប្រើ ដូចជាចំនួនរេស៊ីប៊ី និងគ្រឿងផ្សំដែលប្រើ។

ដើម្បីកែលម្អបន្ថែម យើងចង់បន្ថែមដូចខាងក្រោម៖

- **តម្រងគ្រឿងផ្សំចេញ**។ យើងចង់អាចតម្រងគ្រឿងផ្សំដែលយើងមិនចូលចិត្ត ឬជា្ជអាលក្លនិចបាន។ ដើម្បីអនុវត្តកែប្រែនេះ យើងអាចកែប្រែ prompt មានស្រាប់និងបន្ថែមលក្ខខណ្ឌតម្រងនៅចុងវាដូចខាងក្រោម៖

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  ខាងលើ យើងបានបន្ថែម `{filter}` នៅចុង prompt ហើយយើងក៏ចាប់តម្លៃតម្រងពីអ្នកប្រើផងដែរ។

  ឧទាហរណ៍នៃការបញ្ចូលការរត់កម្មវិធីធ្លាប់មានទម្រង់ដូចខាងក្រោម៖

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

  ដូចដែលអ្នកឃើញ រេស៊ីប៊ីណាមួយមានដូងប្រេងគោត្រូវបានតម្រងចេញ ។ ប៉ុន្តែ ប្រសិនបើអ្នកទទួលមិនបាន lactose អ្នកប្រហែលចង់តម្រងរេស៊ីប៊ីមានជ័រចេញផង ដូច្នេះត្រូវមានការបញ្ជាក់ច្បាស់លាស់។

- **បង្កើតបញ្ជីទិញ**។ យើងចង់បង្កើតបញ្ជីទិញ ដោយគិតថាអ្នកមានគ្រាន់តែគ្រឿងផ្សំមួយចំនួននៅផ្ទះ។

  សម្រាប់មុខងារនេះ អ្នកអាចព្យាយាមដោះស្រាយគ្រប់យ៉ាងក្នុង prompt មួយឬចែកចេញទៅជា២ prompt។ យើងនឹង សាកល្បងវិធីទី២។ នៅទីនេះយើងស្នើរឲ្យបន្ថែម prompt ផ្សេងទៀត ប៉ុន្តែដើម្បីធ្វើបាន អ្នកត្រូវបន្ថែមលទ្ធផលពី prompt មុនជាការរំពឹងទុកទៅ prompt ថ្មី។

  ស្វែងរកផ្នែកកូដែលបោះពុម្ពលទ្ធផលពី prompt ដំបូង ហើយបន្ថែមកូដដូចខាងក្រោម៖

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  សូមចំណាំ៖

  1. យើងកំពុងបង្កើត prompt ថ្មី ដោយបន្ថែមលទ្ធផលពី prompt មុនទៅ prompt ថ្មី។

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. យើងធ្វើសំណើថ្មី ក៏ព្យាយាមគិតពេលទទួល tokens ដែលបានស្នើនៅ prompt ដំបូង ដូច្នេះការបញ្ជាក់អស់កំហុស `max_output_tokens` គឺ 1200។

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     យកកូដនេះដំណើរការ ឥឡូវនេះ យើងទទួលបានលទ្ធផលដូចខាងក្រោម៖

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## កែលម្អការកំណត់រចនាសម្ព័ន្ធរបស់អ្នក

អ្វីដែលយើងមានរហូតមកនេះគឺកូដដែលដំណើរការ ប៉ុន្តែមានការកែប្រែខ្លះដែលយើងគួរតែធ្វើ ដើម្បីធ្វើឲ្យរឿងមានភាពល្អប្រសើរឡើងទៀត។ អ្វីដែលយើងគួរទើបធ្វើមាន:

- **បំបែកសម្ងាត់ពីកូដ** ដូចជាគ្រាប់ API។ សម្ងាត់មិនសមរម្យនៅក្នុងកូដទេ ហើយគួរតែរក្សាទុកនៅកន្លែងមានសុវត្ថិភាព។ ដើម្បីបំបែកសម្ងាត់ពីកូដ យើងអាចប្រើអថេរបរិស្ថាន និងបណ្ណាល័យដូចជា `python-dotenv` ដើម្បីផ្ទុកពួកវាពីឯកសារ។ ខាងក្រោមនេះជារបៀបដែលវាមើលទៅក្នុងកូដ:

  1. បង្កើតឯកសារ `.env` ដែលមានមាតិកាដូចខាងក្រោម:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > សូមចំណាំ សម្រាប់ Azure OpenAI នៅ Microsoft Foundry អ្នកត្រូវកំណត់អថេរបរិស្ថានដូចខាងក្រោមជំនួស:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     នៅក្នុងកូដ អ្នកនឹងផ្ទុកអថេរបរិស្ថានដូចខាងក្រោម:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **ពាក្យមួយអំពីប្រវែងស្លាកសញ្ញា**។ យើងគួរពិចារណាថាចំនួនស្លាកសញ្ញាប៉ុន្មានដែលយើងត្រូវការដើម្បីបង្កើតអត្ថបទដែលយើងចង់បាន។ ស្លាកសញ្ញាភាគច្រើនត្រូវការចំណាយប្រាក់ ដូច្នេះនៅពេលដែលអាចធ្វើបាន យើងគួររៀបចំប្រើពេញប្រសើរនៅចំនួនស្លាកសញ្ញាដែលយើងប្រើ។ ឧទាហរណ៍ តើយើងអាចប្តូរប្រមូលផ្តុំការផ្តល់ពត៌មានជាមធ្យមវិធីដែលយើងអាចប្រើស្លាកសញ្ញាន้อย?

  ដើម្បីប្ដូរចំនួនស្លាកសញ្ញាដែលប្រើ អ្នកអាចប្រើប៉ារ៉ាម៉ែត្រ `max_output_tokens`។ ឧទាហរណ៍ ប្រសិនបើអ្នកចង់ប្រើស្លាកសញ្ញា ១០០ អ្នកនឹងធ្វើបែបនេះ:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **ការពិសោធន៍ជាមួយសីតុណ្ហភាព**។ សីតុណ្ហភាពគឺជារឿងដែលយើងមិនបានរៀនទុកមុន តែមើលទៅជាcontextសំខាន់សម្រាប់របៀបដែលកម្មវិធីរៀបចំ។ តម្លៃសីតុណ្ហភាពខ្ពស់បណ្តាលឲ្យលទ្ធផលមានការប្រែប្រួលច្រើន។ ផ្ទុយទៅវិញ តម្លៃសីតុណ្ហភាពទាប ធ្វើឲ្យលទ្ធផលគឺអាចទាយបានច្រើនជាង។ គិតពីថាតើអ្នកចង់បានភាពផ្សេងគ្នានៅលទ្ធផលរបស់អ្នកឬអត់។

  ដើម្បីប្ដូរសីតុណ្ហភាព អ្នកអាចប្រើប៉ារ៉ាម៉ែត្រ `temperature`។ ឧទាហរណ៍ ប្រសិនបើអ្នកចង់ប្រើសីតុណ្ហភាព 0.5 អ្នកនឹងធ្វើបែបនេះ:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > សូមចំណាំ ថាមើលទៅជិត 1.0 លទ្ធផលនឹងមានភាពខុសគ្នាអំពីច្រើន។

- **ម៉ូឌែលហិរញ្ញវត្ថុ reasoning មិនប្រើ `temperature`**។ នេះគឺជាការប្រែប្រួលសំខាន់ឆ្នាំ 2026។ ម៉ូឌែលបច្ចុប្បន្នដែលមិនមែនជាទម្រង់ចាស់នៅ Microsoft Foundry គឺជាម៉ូឌែលវិភាគ reasoning (គ្រួសារ GPT-5, បន្ទាត់ o-series) - ហើយគេ **មិនគាំទ្រ `temperature` ឬ `top_p`** ទេ (ហើយក៏មិន `max_tokens`; ប្រើ `max_output_tokens` ទេ)។ ប្រសិនបើអ្នកផ្ញើ `temperature` ទៅកាន់ `gpt-5-mini` អ្នកនឹងទទួលបានកំហុស "parameter not supported"។ ដូច្នេះដើម្បីសាកល្បងឧទាហរណ៍សីតុណ្ហភាពខាងលើ អ្នកគួរតែសំគាល់ទៅម៉ូឌែលដែលនៅតែគាំទ្រការគ្រប់គ្រងការគំរូ - ឧទាហរណ៍ម៉ូឌែល Llama បើកដូចជា `Llama-3.3-70B-Instruct` ពី [បញ្ជីម៉ូឌែល Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ដែលហៅតាមមុខងារផ្លូវ (endpoint) Foundry Models / Azure AI Inference (ដូចគ្នានឹងគំរូ `githubmodels-*`)។ សម្រាប់ reasoning models ដូចជា GPT-5 អ្នកបញ្ជាអោយលទ្ធផលតាមរបៀបផ្សេងចេញ៖
  - **Prompt engineering** - ការណែនាំច្បាស់ ការដាក់ឧទាហរណ៍ ហើយលទ្ធផលដែលមានរចនាប័ទ្ម (មើលមេរៀន [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) ធ្វើការងារជំនួសគ្រឿងបញ្ជាការគំរូដែលបានប្រើមុន។
  - **ការគ្រប់គ្រង reasoning** - ប៉ារ៉ាម៉ែត្រដូចជាការខំប្រឹង reasoning / ភាពថ្លៃថ្នូរ ដាក់ពិចារណារវាងកម្រិតជ្រៅ reasoning និងពេលវេលានិងចំណាយ។

  ជាសង្ខេប: `temperature`/`top_p` នៅតែមានប្រសិទ្ធភាពនៅលើម៉ូឌែលជាច្រើន (Llama, Mistral, Phi និងគ្រួសារ GPT-4.x - ប៉ុន្តែ GPT-4.x កំពុងតែបញ្ឈប់), ប៉ុន្តែទិសដៅគឺ prompt engineering + ការគ្រប់គ្រង reasoning លើម៉ូឌែល reasoning ដូចជា GPT-5។

## ការចាត់ចែងការងារ

សម្រាប់ការងារនេះ អ្នកអាចជ្រើសរើសអ្វីដែលចង់បង្កើតបាន។

ខាងក្រោមនេះជាការផ្តល់អនុសាសន៍ខ្លះៗ៖

- កែប្រែកម្មវិធីកម្មវិធីបង្កើតបច្ចេកទេសម្ហូបដើម្បីធ្វើឱ្យវាល្អប្រសើរឡើងទៀត។ លេងជាមួយតម្លៃសីតុណ្ហភាព និង prompt ដើម្បីមើលអ្វីដែលអ្នកអាចធ្វើបាន។
- បង្កើត "មិត្តសិក្សា"។ កម្មវិធីនេះគួរអាចឆ្លើយសំនួរអំពីប្រធានបទមួយ ឧទាហរណ៍ Python អ្នកអាចមាន prompt ដូចជា "តើប្រធានបទមួយចំពោះ Python ជាអ្វី?" ឬអ្នកអាចមាន prompt ដែលស្នើឲ្យបង្ហាញកូដសម្រាប់ប្រធានបទណាមួយ។
- ប្រព័ន្ធប្រវត្តិសាស្ត្រ បង្កើតការរស់រវើករបស់ប្រវត្តិសាស្ត្រ បញ្ជាឱ្យប្រព័ន្ធលេងតួអង្គប្រវត្តិសាស្ត្រមួយ ហើយសួរខ្លះៗអំពីជីវិតនិងរយៈពេលរបស់វា។

## ដំណោះស្រាយ

### មិត្តសិក្សា

ខាងក្រោមនេះជាការចាប់ផ្តើម prompt មួយ មើលថាតើអ្នកអាចប្រើវា និងកែប្រែវា ដើម្បីឲ្យសាកសម។

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### ប្រព័ន្ធប្រវត្តិសាស្ត្រ

ខាងក្រោមជាសំណុំ prompt ដែលអ្នកអាចប្រើបាន:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## ការត្រួតពិនិត្យចំណេះដឹង

តើមូលដ្ឋានសីតុណ្ហភាពធ្វើអ្វី?

1. វាគ្រប់គ្រងថាលទ្ធផលគឺចៃដន្យប៉ុណ្ណា។
1. វាគ្រប់គ្រងថាចម្លើយមានទំហំធំប៉ុណ្ណា។
1. វាគ្រប់គ្រងថាចំនួនស្លាកសញ្ញាត្រូវបានប្រើប៉ុណ្ណា។

## 🚀 챌린지

នៅពេលធ្វើការងារ ព្យាយាមបម្លែងសីតុណ្ហភាព ដាក់វាទៅ 0, 0.5, និង 1។ ចងចាំថា 0 ជាការប្រែប្រួលតិចជាងគេ និង 1 ជាការប្រែប្រួលច្រើនជាងគេ។ តម្លៃណាដែលល្អបំផុតសម្រាប់កម្មវិធីរបស់អ្នក?

## ការងារល្អណាស់! បន្តរៀនរបស់អ្នក

បន្ទាប់ពីបញ្ចប់មេរៀននេះ សូមពិនិត្យមើល [ប្រមូលផ្តុំការរៀន Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ដើម្បីបន្តកម្រិតចំណេះដឹង Generative AI របស់អ្នក!

ចូលទៅមេរៀន 7 ដែលយើងនឹងមើលវិធី [បង្កើតកម្មវិធីការជជែក](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->