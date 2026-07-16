# ការសាងសង់កម្មវិធីបង្កើតអត្ថបទ

[![ការសាងសង់កម្មវិធីបង្កើតអត្ថបទ](../../../translated_images/km/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(ចុចលើរូបភាពខាងលើដើម្បីមើលវីដេអូមេរៀននេះ)_

អ្នកបានឃើញរហូតមកដល់ពេលនេះតាមអំពីកូរីគ្រឹះៗដូចជាការចាប់ផ្តើម (prompts) ហើយមានវិជ្ជាក៏មួយហៅថា "prompt engineering"។ ឧបករណ៍ជាច្រើនដែលអ្នកអាចប្រើបានដូចជា ChatGPT, Office 365, Microsoft Power Platform និងផ្សេងទៀត គាំទ្រឲ្យអ្នកប្រើការចាប់ផ្តើមដើម្បីធ្វើបញ្ហាណាមួយ។

ដើម្បីអោយអ្នកបញ្ចូលបទពិសោធន៍បែបនេះទៅកម្មវិធីមួយ អ្នកត្រូវយល់ដឹងពីសេចក្តីគំនិតដូចជាការចាប់ផ្តើម completions និងជ្រើសរើសបណ្ណាល័យមួយដើម្បីដំណើរការ។ នេះគឺជាអ្វីដែលអ្នកនឹងរៀននៅក្នុងជំពូកនេះ។

## ការណែនាំ

ក្នុងជំពូកនេះ អ្នកនឹង:

- រៀនអំពីបណ្ណាល័យ openai និងគំនិតគ្រឹះរបស់វា។
- សាងសង់កម្មវិធីបង្កើតអត្ថបទប្រើ openai។
- យល់ដឹងពីរបៀបប្រើគំនិតដូចជា prompt, temperature និង tokens ដើម្បីសាងសង់កម្មវិធីបង្កើតអត្ថបទ។

## គោលបំណងការសិក្សា

នៅចុងបាត់បង់មេរៀននេះ អ្នកនឹងអាច:

- ពន្យល់ថាតើកម្មវិធីបង្កើតអត្ថបទជាអ្វី។
- សាងសង់កម្មវិធីបង្កើតអត្ថបទប្រើ openai។
- កំណត់ការ configuration កម្មវិធីរបស់អ្នកឲ្យប្រើ tokens ច្រើន ឬតិច និងផ្លាស់ប្តូរបរិមាណ temperature សម្រាប់លទ្ធផលនានា។

## តើកម្មវិធីបង្កើតអត្ថបទជាអ្វី?

ជាទូទៅ នៅពេលអ្នកបង្កើតកម្មវិធី អ្នកមានអ៊ីនធឺហ្វេសមួយដូចជា:

- គំរូបញ្ជា។ កម្មវិធី console ជាឧទាហរណ៍ដែលអ្នកវាយបញ្ជា ហើយវាចCompletesការងារមួយ។ ដូចជាកម្មវិធី `git` ដែលមានបែបបទបញ្ជា។
- អ៊ីនធឺហ្វេសអ្នកប្រើ(UI)។ កម្មវិធីខ្លះមានអ៊ីនធឺហ្វេសក្រាហ្វិច(GUI) ដែលអ្នកចុចប៊ូតុង វាយអត្ថបទ ជ្រើសរើសជម្រើស ហើយផ្សេងទៀត។

### កម្មវិធី console និង UI មានកម្រិត

ប្រៀបធៀបវាជាមួយកម្មវិធីបែបទោលបញ្ជា ដែលអ្នកវាយបញ្ជាមួយ:

- **វាមានកម្រិត**។ អ្នកមិនអាចវាយបញ្ជាតែមួយណាក៏បានទេ មានតែបញ្ជាដែលកម្មវិធីគាំទ្រតែប៉ុណ្ណោះ។
- **មានភាសាបំណាក់បំណុល**។ កម្មវិធីខ្លះគាំទ្រភាសាច្រើន ប៉ុន្តែដើមអតីតកម្មវិធីនេះត្រូវបានបង្កើតសម្រាប់ភាសាមួយជាក់លាក់ ទោះបីអ្នកអាចបន្ថែមភាសាបានក៏ដោយ។

### គុណសម្បត្តិរបស់កម្មវិធីបង្កើតអត្ថបទ

តើកម្មវិធីបង្កើតអត្ថបទខុសគ្នាយ៉ាងដូចម្តេច?

នៅក្នុងកម្មវិធីបង្កើតអត្ថបទ អ្នកមានភាពបត់បែនច្រើន អ្នកមិនមានកំណត់ត្រឹមតែបញ្ជាសំរាប់ទីមួយ ឬភាសាអ្នកបញ្ចូលជាក់លាក់ទេ។ ភ្លាមៗ អ្នកអាចប្រើភាសាធម្មជាតិសម្រាប់អន្តរកម្មជាមួយកម្មវិធីនេះ។ គុណសម្បត្តិមួយទៀត គឺថាអ្នកមានអន្តរកម្មជាមួយប្រភពទិន្នន័យដែល​ត្រូវបានបណ្តុះបណ្តាលលើឯកសារធំធេងមួយ ដែលកម្មវិធីបែបចាស់គេអាចមានកំណត់នៅលើការទិន្នន័យក្នុងមូលដ្ឋានទិន្នន័យ។

### តើខ្ញុំអាចសាងសង់អ្វីបានខ្លះជាមួយកម្មវិធីបង្កើតអត្ថបទ?

មានអ្វីសំខាន់ជាច្រើនដែលអ្នកអាចបង្កើតបាន។ តាមការឧទាហរណ៍៖

- **Chatbot**។ Chatbot ត្រូវបានបង្កើតសម្រាប់ឆ្លើយសំណួរអំពីប្រធានបទជាច្រើន ដូចជាក្រុមហ៊ុនរបស់អ្នកនិងផលិតផលវា អាចជាជម្រើសល្អ។
- **ជំនួយការ**។ LLMs អាចវាយតំលៃ Text Summarization, ទទួលយកចំណុចសង្ខេបពីអត្ថបទ, ផលិតអត្ថបទដូចជា resume និងផ្សេងទៀត។
- **ជំនួយរចនាសម្ព័ន្ធកូដ**។ អាស្រ័យលើម៉ូដែលភាសាអ្នកប្រើ អ្នកអាចបង្កើតជំនួយរចនាសម្ព័ន្ធកូដ ដូចជា ការជួយសរសេរកូដ។ ឧទាហរណ៍ អ្នកអាចប្រើផលិតផលដូចជា GitHub Copilot ឬ ChatGPT សម្រាប់ជំនួយសរសេរកូដ។

## តើខ្ញុំអាចចាប់ផ្តើមបានយ៉ាងដូចម្តេច?

អ្នកត្រូវរកវិធីភ្ជាប់ជាមួយ LLM ដែលជាទូទៅរួមមានវិធីសាស្រ្តពីរខាងក្រោម:

- ប្រើ API។ នៅទីនេះ អ្នកកំពុងបង្កើតសំណើវេបសាយជាមួយ prompt របស់អ្នក ហើយទទួលបានអត្ថបទដែលបង្កើតវិញ។
- ប្រើបណ្ណាល័យ។ បណ្ណាល័យជួយបិទការហៅ API ហើយធ្វើឲ្យងាយស្រួលប្រើ។

## បណ្ណាល័យ/SDK

មានបណ្ណាល័យល្បីៗខ្លះសម្រាប់ដំណើរការជាមួយ LLMs ដូចជា:

- **openai**, បណ្ណាល័យនេះធ្វើឲ្យងាយស្រួលភ្ជាប់ទៅម៉ូដែលរបស់អ្នក និងផ្ញើការចាប់ផ្តើម។

បន្ទាប់មកមានបណ្ណាល័យដែលដំណើរការលើកម្រិតខ្ពស់ក៏ដូចជា:

- **Langchain**។ Langchain គឺល្បី និងគាំទ្រភាសា Python។
- **Semantic Kernel**។ Semantic Kernel គឺជាបណ្ណាល័យពី Microsoft ដែលគាំទ្រភាសា C#, Python និង Java។

## កម្មវិធីដំបូងប្រើ openai

មកមើលពីរបៀបវាយបង្កើតកម្មវិធីដំបូង បណ្ណាល័យដែលអ្នកត្រូវការយ៉ាងដូចម្តេច ចំនួនទាមទារបានប៉ុន្មាន និងផ្សេងៗទៀត។

### ដំឡើង openai

មានបណ្ណាល័យជាច្រើនសម្រាប់ផ្ទាល់ខ្លួនជាមួយ OpenAI ឬ Azure OpenAI។ អាចប្រើភាសាកូដជាច្រើនដូចជា C#, Python, JavaScript, Java និងផ្សេងៗទៀត។ យើងបានជ្រើសរើសប្រើបណ្ណាល័យ Python `openai` ដូច្នេះយើងនឹងប្រើ `pip` ដើម្បីដំឡើងវា។

```bash
pip install openai
```

### បង្កើតធនធាន

អ្នកត្រូវអនុវត្តជំហានដូចខាងក្រោម៖

- បង្កើតគណនីនៅលើ Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)។
- ទទួលសិទ្ធិចូលទៅ Azure OpenAI។ ទៅ [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) ហើយស្នើរសុំសិទ្ធិចូល។

  > [!NOTE]
  > នៅពេលដែលសរសេរនេះ អ្នកត្រូវដាក់ពាក្យសុំដើម្បីទទួលសិទ្ធិចូលទៅ Azure OpenAI។

- ដំឡើង Python <https://www.python.org/>
- មានធនធាន Azure OpenAI Service រួចហើយ។ មើលមគ្គុទេសក៍សម្រាប់របៀប [បង្កើតធនធាន](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)។

### ស្វែងរកសោ API និងendpoint

នៅពេលនេះ អ្នកត្រូវប្រាប់បណ្ណាល័យ `openai` របស់អ្នកថាតើសោ API ត្រូវប្រើអ្វី។ ដើម្បីស្វែងរកសោ API របស់អ្នក ចូលទៅផ្នែក "សោ និង Endpoint" នៃធនធាន Azure OpenAI របស់អ្នក ហើយចម្លង "សោ 1"។

![សោ និង Endpoint resource blade នៅក្នុង Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

ឥឡូវនេះដែលអ្នកចម្លងព័ត៌មាននេះរួចហើយ យើងនឹងបញ្ជាឲ្យបណ្ណាល័យប្រើវា។

> [!NOTE]
> វាកម្មប្រយោជន៍ក្នុងការបំបែកសោ API អอกจากកូដរបស់អ្នក។ អ្នកអាចធ្វើរឿងនេះដោយប្រើអថេរបរិវេណ។
>
> - កំណត់អថេរបរិវេណ `OPENAI_API_KEY` ទៅសោ API របស់អ្នក។
>   `export OPENAI_API_KEY='sk-...'`

### កំណត់ការការកំណត់ Azure

ប្រសិនបើអ្នកប្រើ Azure OpenAI (ឥឡូវជាផ្នែកនៃ Microsoft Foundry) នេះគឺរបៀបកំណត់ configuration។ យើងប្រើឈ្មោះថា `OpenAI` យោងទៅកាន់ endpoint Azure OpenAI `/openai/v1/` ដែលដំណើរការជាមួយ Responses API ហើយមិនត្រូវការបញ្ជាក់ `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

ខាងលើ យើងកំពុងកំណត់ជារបស់ដូចតទៅ៖

- `api_key`, នេះជាសោ API របស់អ្នកដែលបានរកឃើញក្នុង Azure Portal ឬ Microsoft Foundry portal។
- `base_url`, នេះជាអាសយដ្ឋាន endpoint Foundry របស់អ្នកដែលបានបន្ថែម `/openai/v1/` ទៅខាងចុង។ stable v1 endpoint ដំណើរការ ទៅលើ OpenAI និង Azure OpenAI ដោយមិនត្រូវការ `api_version`។

> [!NOTE] > `os.environ` អានអថេរបរិវេណ។ អ្នកអាចប្រើវាទៅអានអថេរបរិវេណដូចជា `AZURE_OPENAI_API_KEY` និង `AZURE_OPENAI_ENDPOINT`។ កំណត់អថេរបរិវេណទាំងនេះនៅក្នុង terminal របស់អ្នក ឬប្រើបណ្ណាល័យដូចជា `dotenv`។

## បង្កើតអត្ថបទ

វិធីបង្កើតអត្ថបទគឺប្រើ Responses API តាមរយៈវិធី `responses.create`។ នេះជាគំរូ៖

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # នេះគឺជាត្រគាការបង្ហោះម៉ូដែលរបស់អ្នក
    input=prompt,
    store=False,
)
print(response.output_text)
```

នៅក្នុងកូដខាងលើ យើងបង្កើតការឆ្លើយតបមួយនិងផ្ញើម៉ូដែលដែលចង់ប្រើ និង prompt។ បន្ទាប់មកយើងបោះពុម្ភអត្ថបទបង្កើតតាមរយៈ `response.output_text`។

### ការសន្ទនាច្រើនជុំ

Responses API សាកសមសម្រាប់ការបង្កើតអត្ថបទការសន្ទនាលើកតែមួយនិង chatbot ច្រើនជុំ - អ្នកផ្តល់បញ្ជីសារ `input` ដើម្បីបង្កើតការសន្ទនា៖

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

ព័ត៌មានបន្ថែមអំពីមុខងារនេះនៅជំពូកបន្ទាប់។

## លំហាត់ - កម្មវិធីបង្កើតអត្ថបទដំបូងរបស់អ្នក

ឥឡូវនេះចាប់ពីពេលដែលយើងបានរៀនរបៀបកំណត់ និង កំណត់តម្លៃ openai រួចហើយ ពេលវេលាជាការសាងសង់កម្មវិធីបង្កើតអត្ថបទដំបូងរបស់អ្នក។ ដើម្បីសាងសង់កម្មវិធីរបស់អ្នក សូមធ្វើតាមជំហានខាងក្រោម៖

1. បង្កើតបរិវេណ virtual ហើយដំឡើង openai៖

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > ប្រសិនបើអ្នកប្រើ Windows សូមវាយ `venv\Scripts\activate` ជំនួស `source venv/bin/activate`។

   > [!NOTE]
   > ស្វែងរកសោ Azure OpenAI របស់អ្នក ដោយចូលទៅ [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) កំណត់ស្វែងរកពាក្យ `Open AI` ហើយជ្រើសរើស `Open AI resource` រួចជ្រើសរើស `Keys and Endpoint` ហើយចម្លងតម្លៃ `Key 1`។

1. បង្កើតឯកសារ _app.py_ ហើយដាក់កូដដូចខាងក្រោម៖

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

   # ទាមទារដោយប្រើប្រាស់ Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # បោះពុម្ពការឆ្លើយតប
   print(response.output_text)
   ```

   > [!NOTE]
   > ប្រសិនបើអ្នកប្រើ OpenAI ធម្មតា (មិនមែន Azure) សូមប្រើ `client = OpenAI(api_key="<បញ្ចូលសោ OpenAI របស់អ្នក>")` (គ្មាន `base_url`) ហើយផ្ញើបញ្ចូលឈ្មោះម៉ូដែលដូចជា `gpt-4o-mini` ជំនួសឈ្មោះ deployment។

   អ្នកគួរតែឃើញលទ្ធផលដូចខាងក្រោម៖

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## ប្រភេទចាប់ផ្តើមខុសគ្នា សម្រាប់ការងារខុសគ្នា

ឥឡូវនេះ អ្នកបានឃើញរបៀបបង្កើតអត្ថបទដោយប្រើ prompt។ អ្នកមានកម្មវិធីដាន់ហើយដែលអាចកែប្រែបានដើម្បីបង្កើតអត្ថបទខុសគ្នា។

ចាប់ផ្តើមអាចប្រើសម្រាប់បញ្ហាច្រើន។ ដូចជាឧទាហរណ៍៖

- **បង្កើតអត្ថបទមួយប្រភេទ**។ ដូចជាការបង្កើតកំណាព្យ, សំណួរសម្រាប់ quiz ល។ 
- **ស្វែងរកព័ត៌មាន**។ អ្នកអាចប្រើ prompt ដើម្បីស្វែងរកព័ត៌មាន ដូចជា 'CORS មានន័យអ្វីនៅក្នុងការអភិវឌ្ឍន៍វេបសាយ?'។
- **បង្កើតកូដ**។ អ្នកអាចប្រើ prompt ដើម្បីបង្កើតកូដ ដូចជាការអភិវឌ្ឍវាយបញ្ជា regular expression សម្រាប់ផ្ទៀងផ្ទាត់អ៊ីមែល ឬបង្កើតកម្មវិធីមួយទាំងមូល ដូចជា web app។

## ករណីប្រើប្រាស់ច្បាស់លាស់: កម្មវិធីបង្កើតមួយចំនួនម្ហូប

សន្មត់ថា អ្នកមានធាតុដើមនៅផ្ទះ ហើយអ្នកចង់ចៀសវាងម្ហូបមួយ។ ដើម្បីធ្វើវា អ្នកត្រូវការតារាងម្ហូប។ វិធីដើម្បីស្វែងរកតារាងម្ហូបគឺប្រើវេបស្វែងរក ឬអាចប្រើ LLM។

អ្នកអាចសរសេរ prompt ដូចខាងក្រោម៖

> "បង្ហាញតារាងម្ហូប 5 សម្រាប់មួយចំណីដែលមានធាតុដើមដូចខាងក្រោម៖ ជ្រូក, ដំឡូង, និងការ៉ុត។ សម្រាប់តារាងម្ហូបមួយ សូមបញ្ជីធាតុដើមទាំងអស់ដែលប្រើ" 

អ្នកអាចទទួលបានចម្លើយដូចខាងក្រោម៖

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

លទ្ធផលនេះល្អណាស់ ខ្ញុំដឹងតើត្រូវចំអិនអ្វី។ ក្នុងពេលនេះ ការកែលម្អដែលអាចមានប្រយោជន៍គឺ៖

- ការតម្រងនូវធាតុដែលខ្ញុំមិនចូលចិត្ត ឬមានអាការៈរលាក។
- ផលិតបញ្ជីទិញសម្រាប់ម្ហូប បើខ្ញុំមិនមានធាតុដើមទាំងអស់នៅផ្ទះ។

សម្រាប់ករណីខាងលើ មកបន្ថែម prompt បន្ថែម៖

> "សូមដកម្ហូបដែលមានបន្លែនិងចេញ ព្រោះខ្ញុំមានអត្រារលាក ហើយសូមជំនួសរបស់ផ្សេងទៀត។ សូមផលិតបញ្ជីទិញសម្រាប់ម្ហូប ទាក់ទងនឹងខ្ញុំមានជ្រូក, ដំឡូង និងការ៉ុតរួចហើយនៅផ្ទះ។"

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

នេះជាតារាងម្ហូប 5 របស់អ្នក ដែលគ្មានបន្លែនិងអ្នកមានបញ្ជីទិញសម្រាប់ម្ហូបទាំងនោះ ដោយយកគិតពីធាតុដែលមាននៅផ្ទះ។

## លំហាត់ - សាងសង់កម្មវិធីបង្កើតតារាងម្ហូប

ឥឡូវនេះដែលយើងបានលេងស្ថានភាពមួយហើយ សូមសរសេរកូដអោយសមស្របនឹងស្ថានភាពដែលបង្ហាញ។ សូមធ្វើតាមជំហានខាងក្រោម៖

1. ប្រើឯកសារ _app.py_ ដែលមានស្រាប់ជាចំណុចចាប់ផ្តើម។
1. រកចំណុច `prompt` ហើយប្តូរកូដវាជាដូចខាងក្រោម៖

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   ប្រសិនបើអ្នករត់កូដនេះឥឡូវ អ្នកគួរតែឃើញលទ្ធផលដូចខាងក្រោម៖

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > សម្គាល់, LLM របស់អ្នកគឺមិនកំណត់ច្បាស់នោះទេ, ដូច្នេះអ្នកអាចទទួលបានលទ្ធផលខុសៗគ្នានៅពេលរត់កម្មវិធី។

   ល្អណាស់ សូមមើលពីរបៀបខ្ពស់លើកបច្ចេកវិទ្យា។ ដើម្បីកែលម្អវា យើងចង់ធានាថាកូដពន្យល់បត់បែនបាន ដូច្នេះធាតុ និងចំនួនម្ហូបអាចបន្ថែម និងផ្លាស់ប្តូរបាន។

1. សូមប្តូរកូដដោយរបៀបដូចខាងក្រោម៖

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # បញ្ចូលចំនួនរបៀបម្ហូបចូលទៅក្នុងប្រំផុតនិងគ្រឿងផ្សំ
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   ការយកកូដរបស់ការធ្វើតេស្ត អាចមើលទៅដូចខាងក្រោម៖

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### កែលម្អដោយបន្ថែមការតម្រង និងបញ្ជីទិញ

ឥឡូវនេះ យើងមានកម្មវិធីដំណើរការ ដែលអាចបង្កើតតារាងម្ហូបបាន ហើយវាបត់បែនបាន ដោយវាអាស្រ័យលើការបញ្ចូលពីអ្នកប្រើ ទាំងចំនួនម្ហូប និងធាតុដើម។

សម្រាប់កែលម្អជាថ្មី យើងចង់បន្ថែមអ្វីខាងក្រោម៖

- **តម្រងធាតុដើមចេញ**។ យើងចង់អោយការតម្រងធាតុដើមដែលយើងមិនចូលចិត្តឬមានអាការៈរលាកបាន។ ដើម្បីអនុវត្តបម្លែងនេះ អ្នកអាចកែប្រែក្នុង prompt បច្ចុប្បន្ន ហើយបន្ថែមលក្ខខណ្ឌតម្រងចុង prompt ដូចខាងក្រោម៖

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  ខាងលើ យើងបន្ថែម `{filter}` នៅចុង prompt ហើយយកតម្លៃ filter ពីអ្នកប្រើ។

  ដំណើរការមួយឧទាហរណ៍នៅពេលច្រកកម្មវិធីឥឡូវនេះអាចមើលទៅដូចខាងក្រោម៖

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

  ដូចដែលអ្នកឃើញ ម្ហូបណាមួយដែលមានទឹកដោះគោ បានតម្រងចេញ។ ប៉ុន្តែ ប្រសិនបើអ្នកមានជំងឺទទួលទឹកដោះគោមិនបាន អ្នកនឹងចង់តម្រងម្ហូបដែលមានឈីសផងដែរ ដូច្នេះមានការផ្តល់អោយច្បាស់។


- **ផលិតបញ្ជីទិញ**។ យើងចង់ផលិតបញ្ជីទិញ ដោយគិតពីអ្វីដែលយើងមាននៅផ្ទះរួចហើយ។

  សម្រាប់មុខងារនេះ យើងអាចព្យាយាមដោះស្រាយទាំងអស់ក្នុងការលើកទិសមួយ ឬយើងអាចបំបែកវាជាពីរជាការលើកទិស។ យើងសាកល្បងវិធីវិញ។ នៅទីនេះ យើងបង្កើតការបន្ថែមការលើកទិសមួយទៀត ប៉ុន្តែដើម្បីឱ្យវាដំណើរការ យើងត្រូវបន្ថែមលទ្ធផលពីការលើកទិសមុនជាភាសារយៈពេលសម្រាប់ការលើកទិសបន្ទាប់។

  ចូររកទីតាំងនៅក្នុងកូដដែលបោះពុម្ភលទ្ធផលពីការលើកទិសដំបូង ហើយបន្ថែមកូដដូចខាងក្រោមនៅខាងក្រោម៖

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # បោះពុម្ពចេញការឆ្លើយតប
  print("Shopping list:")
  print(response.output_text)
  ```

  សូមចំណាំដូចតទៅ៖

  1. យើងកំពុងបង្កើតការលើកទិសថ្មីដោយបន្ថែមលទ្ធផលពីការលើកទិសដំបូងទៅការលើកទិសថ្មី៖

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. យើងធ្វើសំណើថ្មីមួយ ប៉ុន្តែផងដែរ គិតពីចំនួនតួអក្សរដែលយើងទាមទារនៅក្នុងការលើកទិសដំបូង ដូច្នេះពេលនេះយើងកំណត់ `max_output_tokens` ជា 1200។

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     ដោយប្រើកូដនេះ ឥឡូវនេះយើងទទួលបានលទ្ធផលដូចខាងក្រោម៖

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## ធ្វើឱ្យការតំឡើងរបស់អ្នកប្រសើរឡើង

អ្វីដែលយើងមាននៅមុននេះគឺកូដដែលដំណើរការ ប៉ុន្តែមានការកែប្រែខ្លះៗដែលយើងគួរធ្វើដើម្បីធ្វើឱ្យវាប្រសើរឡើង។ អ្វីដែលយើងគួរធ្វើគឺ៖

- **បំបែកសម្ងាត់ពីកូដ**, ដូចជា Key API។ សម្ងាត់មិនគួរទៅក្នុងកូដទេ ហើយគួរត្រូវបានផ្ទុកនៅកន្លែងដែលមានសុវត្ថិភាព។ ដើម្បីបំបែកសម្ងាត់ពីកូដ អ្នកអាចប្រើអថេរបរិបទបរិយាកាស និងបណ្ណាល័យដូចជា `python-dotenv` ដើម្បីផ្ទុកវាពីឯកសារ។ នេះគឺជាវិធីដែលវានឹងមើលទៅក្នុងកូដ៖

  1. បង្កើតឯកសារ `.env` ជាមួយខ្លឹមសារដូចខាងក្រោម៖

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > សូមចំណាំ សម្រាប់ Azure OpenAI ក្នុង Microsoft Foundry អ្នកត្រូវតែកំណត់អថេរបរិបទបរិយាកាសដូចខាងក្រោមជំនួស៖

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     ក្នុងកូដ អ្នកនឹងផ្ទុកអថេរបរិបទបរិយាកាសដូចខាងក្រោម៖

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **ពាក្យមួយស្តីពីប្រវែងតួអក្សរ**។ យើងគួរត្រូវគិតថាត្រូវប្រើតួអក្សរប៉ុន្មានដើម្បីបង្កើតអត្ថបទដែលយើងចង់បាន។ តួអក្សរជាប្រភេទថ្លៃ ខណៈពេលដែលអាចនឹងមាន ការប្រើតួអក្សរជាប្រយោជន៍ទៅតាមលទ្ធផលដែលយើងយល់ចង់បាន។ ឧទាហរណ៍ អ្នកអាចរៀបចំលើកទិសបែបណា ដើម្បីអាចប្រើតួអក្សរតិចជាងបានទេ?

  ដើម្បីផ្លាស់ប្ដូរចំនួនតួអក្សរដែលប្រើ អ្នកអាចប្រើប៉ារ៉ាម៉ែត្រ `max_output_tokens`។ ឧទាហរណ៍ ប្រសិនបើចង់ប្រើតួអក្សរចំនួន 100 អ្នកអាចធ្វើ៖

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **សាកល្បងជាមួយសីតុណ្ហភាព**។ សីតុណ្ហភាពគឺជារឿងដែលយើងមិនបាននិយាយដល់ទេ ប៉ុន្តែលេខសំខាន់សម្រាប់បរិបទការដំណើរការប្រព័ន្ធ។ តម្លៃសីតុណ្ហភាពខ្ពស់បំផុតនឹងធ្វើឲ្យលទ្ធផលចេញពីកម្មវិធីរេឡាក់បន្ថែម។ ផ្ទុយគ្នាទៅតម្លៃសីតុណ្ហភាពទាប នឹងធ្វើឲ្យលទ្ធផលមើលទៅច្បាស់លាស់។ សូមពិចារណាថាតើអ្នកចង់មានការផ្លាស់ប្តូរនៅលទ្ធផលរបស់អ្នកឬអត់។

  ដើម្បីផ្លាស់ប្តូរសីតុណ្ហភាព អ្នកអាចប្រើប៉ារ៉ាម៉ែត្រ `temperature`។ ឧទាហរណ៍ ប្រសិនបើចង់ប្រើសីតុណ្ហភាព 0.5 អ្នកអាចធ្វើ៖

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > សូមចំណាំ កាន់តែជិត 1.0 កាន់តែមានការផ្លាស់ប្តូរសម្រាប់លទ្ធផល។

## ការផ្តល់ការងារ

សម្រាប់ការងារនេះ អ្នកអាចជ្រើសរើសអ្វីមួយក្នុងការសាងសង់។

ខាងក្រោមជាការផ្តល់អនុសាសន៍ខ្លះៗ៖

- កែប្រែនៅក្នុងកម្មវិធីបង្កើតមុខម្ហូប ដើម្បីធ្វើឱ្យវាបានល្អប្រសើរឡើង។ លេងជាមួយតម្លៃសីតុណ្ហភាព និងការលើកទិស ដើម្បីមើលអ្វីដែលអ្នកអាចបង្កើតបាន។
- បង្កើតកម្មវិធី "មិត្តសិក្សា"។ កម្មវិធីនេះគួរអាចឆ្លើយសំណួរអំពីប្រធានបទមួយ ឧទាហរណ៍ Python អ្នកអាចមានការលើកទិសដូចជា "តើប្រធានបទណាមួយនៅក្នុង Python ជាអ្វី?" ឬ អ្នកអាចមានការលើកទិសដែលនិយាយថា បង្ហាញខ្ញុំឯកសារ​កូដ​សម្រាប់ប្រធានបទមួយជាដើម។
- ប្រវត្តិសាស្ត្របុត់, ធ្វើឱ្យប្រវត្តិសាស្ត្រមានជីវិតឡើងវិញ បញ្ចេញការណែនាំឲ្យបុត់សំដែងតួអង្គប្រវត្តិសាស្ត្រល្បីមួយ ហើយសួរសំណួរអំពីជីវិត និងរយៈពេលរបស់វា។

## ដំណោះស្រាយ

### មិត្តសិក្សា

ខាងក្រោមគឺជាការលើកទិសចាប់ផ្តើម មើលថាអ្នកអាចប្រើវានិងកែប្រែវាឲ្យសមរម្យយ៉ាងដូចម្តេច។

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### បុត់ប្រវត្តិសាស្ត្រ

ខាងក្រោមជាការលើកទិសដែលអ្នកអាចប្រើ៖

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## ការត្រួតពិនិត្យចំណេះដឹង

តើមាតិកាសីតុណ្ហភាពមានមុខងារអ្វី?

1. វាគ្រប់គ្រងតើលទ្ធផលមានលំអិតយ៉ាងដូចម្តេច។
1. វាគ្រប់គ្រងតើចម្លើយធំសង្ខេបយ៉ាងណា។
1. វាគ្រប់គ្រងចំនួនតួអក្សរដែលបានប្រើ។

## 🚀 챌린지

នៅពេលធ្វើការងារ សូមព្យាយាមផ្លាស់ប្ដូរសីតុណ្ហភាព សាកល្បងកំណត់វា 0, 0.5 និង 1។ ចងចាំថា 0 គឺមានការផ្លាស់ប្តូរបំផុតតិចជាង និង 1 គឺមានការផ្លាស់ប្តូរច្រើនជាង។ តម្លៃណាដែលធ្វើការល្អសម្រាប់កម្មវិធីរបស់អ្នក?

## យកចិត្តទុកដាក់ល្អ! បន្តការរៀនរបស់អ្នក

បន្ទាប់ពីបញ្ចប់មេរៀននេះ សូមមើលការប្រមូលផ្តុំ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) របស់យើង ដើម្បីបន្តបង្កើនចំណេះដឹង Generative AI របស់អ្នក!

ទៅមេរៀនទី 7 ដែលយើងនឹងមើលពីរបៀប [សាងសង់កម្មវិធីជជែក](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->