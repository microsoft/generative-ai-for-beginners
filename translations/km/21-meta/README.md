# ការសង់ជាមួយគំរូគ្រួសារ Meta  

## ការណែនាំ  

មេរៀននេះនឹងគ្របដណ្តប់ ៖ 

- ការស្វែងយល់ពីគំរូគ្រួសារ Meta សំខាន់ៗពីរជាមួយ Llama 3.1 និង Llama 3.2 បូករួមជាមួយជម្រើសដែលមានស្រាប់គឺ Llama 3.3 និង Llama 4 ដែលប្រើក្នុងឧទាហរណ៍កូដ  
- ការយល់ដឹងពីករណីប្រើប្រាស់ និងសេចក្តីលម្អិតសម្រាប់គំរូទាំងអស់  
- ឧទាហរណ៍កូដដើម្បីបង្ហាញលក្ខណៈពិសេសដោយឡែកនៃគំរូនីមួយៗ  


## គ្រួសារ Meta នៃគំរូ  

ក្នុងមេរៀននេះ យើងនឹងស្វែងយល់ពីគំរូពីរ ពីគ្រួសារ Meta ឬ "ក្រុម Llama" គឺ Llama 3.1 និង Llama 3.2។ ឧទាហរណ៍កូដដែលអាចរត់បាន ប្រើ Llama 3.3 និង Llama 4 ដែលជាជម្រើសដែលមានស្រាប់ក្នុងកាតាឡុកគំរូ Microsoft Foundry។  

គំរូទាំងនេះ មាននៅក្នុងបម្រើជាច្រើន និងអាចរកបាននៅក្នុង [កាតាឡុកគំរូ Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)។  

> **ចំណាំ៖** GitHub Models នឹងផ្អាកនៅចុងខែកក្កដាឆ្នាំ ២០២៦។ នេះជារបាយការណ៍លម្អិតបន្ថែមស្ដីពីការប្រើប្រាស់ [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ដើម្បីបង្កើតម៉ូឌែល AI ។  

> **ចំណាំ៖** រូបមន្តម៉ូឌែលដែលបានសរសេរជាលើកដំបូងសម្រាប់មេរៀននេះ (Llama 3.1 70B/405B Instruct, Llama 3.2 11B/90B Vision Instruct) ត្រូវបានផ្អាកចេញពីកាតាឡុកគំរូ Microsoft Foundry។ ឧទាហរណ៍កូដខាងក្រោមប្រើ `Llama-3.3-70B-Instruct` និង `Llama-4-Scout-17B-16E-Instruct` ជាជម្រើសដែលមានស្រាប់ក្នុងកាតាឡុកគំរូ Microsoft Foundry ដូច្នេះវានៅតែអាចដំណើរការបាននៅថ្ងៃនេះ។  

រូបមន្តម៉ូឌែល (ដូចបានគ្របដណ្តប់នៅលើក្នុងមេរៀននេះ)៖  
- Llama 3.1 - 70B Instruct (បានផ្អាក)  
- Llama 3.1 - 405B Instruct (បានផ្អាក)  
- Llama 3.2 - 11B Vision Instruct (បានផ្អាក)  
- Llama 3.2 - 90B Vision Instruct (បានផ្អាក)  

ជម្រើសដែលមានស្រាប់ដែលប្រើក្នុងឧទាហរណ៍កូដ៖  
- Llama 3.3 - 70B Instruct (`Llama-3.3-70B-Instruct`)  
- Llama 4 Scout - 17B 16E Instruct (`Llama-4-Scout-17B-16E-Instruct`)  

*ចំណាំ៖ រូបមន្ត Llama 3 ដែលបានពិភាក្សាខាងលើ ត្រូវបានរក្សាទុកសម្រាប់បរិបទប្រវត្តិសាស្ត្រនិងគ្មាននៅក្នុង Microsoft Foundry Models ទៀតទេ។*  

## Llama 3.1  

ក្នុងចំណោម ៤០៥ ពាន់លានពាក្យ (Parameters) Llama 3.1 ត្រូវបានថែមស្ថានភាពជាក្រុម LLM ប្រភពរ open source។  

គំរូនេះជាបំណែលបន្ថែមពីការបញ្ចេញ Llama 3 មុននេះ ដោយផ្តល់ជូន៖  

- បង្អួច context លេខៈ ១២៨k tokens ប្រៀបធៀបនឹង ៨k tokens  
- ចំនួន tokens លទ្ធផលអតិបរមា ៤០៩៦ ប្រៀបធៀបនឹង ២០៤៨   
- ការគាំទ្រជាភាសាច្រៀងខ្ពស់បំផុត - ដោយសារតែបន្ថែម tokens សម្រាប់ហ្វឹកហាត់  

អ្នកនឹងអាចប្រើ Llama 3.1 ដើម្បីដោះស្រាយករណីប្រើប្រាស់ស្មុគស្មាញនៅក្នុងការបង្កើតកម្មវិធី GenAI រួមមាន៖  
- ការហៅមុខងារជាដើម - សមត្ថភាពក្នុងការហៅឧបករណ៍ និងមុខងារចេញពីលំហកម្មវិធី LLM  
- ការសម្រួល RAG ប្រសើរជាងមុន - ដោយសារបង្អួច context ខ្ពស់  
- ការបង្កើតទិន្នន័យស៊ីនថិតិច - សមត្ថភាពក្នុងការបង្កើតទិន្នន័យមានប្រសិទ្ធភាពសម្រាប់ភារកិច្ចដូចជាការប្រឹងប្រែងជំរុញ  

### ការហៅមុខងារជាដើម  

Llama 3.1 ត្រូវបានបង្កើតបន្ថែមឡើងសម្រាប់ការប្រើប្រាស់ហៅមុខងារ ឬឧបករណ៍បានមានប្រសិទ្ធភាពកាន់តែខ្ពស់។ វានៅមានឧបករណ៍ពីរចាក់បញ្ចូលនៅក្នុងដែលគំរូអាចសម្គាល់ថាត្រូវប្រើពិចារណាចេញពី prompt ពីអ្នកប្រើ។ ឧបករណ៍ទាំងនេះគឺ៖  

- **Brave Search** - អាចប្រើស្វែងរកព័ត៌មានទាន់សម័យដូចជាអាកាសធាតុ ដោយបញ្ចូលការស្វែងរកតាមវេបសាយ  
- **Wolfram Alpha** - អាចប្រើសំរាប់គណនា​គណិតវិទ្យាស្មុគស្មាញ ដូច្នេះមិនចាំបាច់សរសេរមុខងារផ្ទាល់ខ្លួនទេ។  

អ្នកក៏អាចបង្កើតឧបករណ៍ផ្ទាល់ខ្លួនដែល LLM អាចហៅបានផងដែរ។  

ក្នុងឧទាហរណ៍កូដខាងក្រោម៖  

- យើងកំណត់ឧបករណ៍ដែលមានស្រាប់ (brave_search, wolfram_alpha) នៅក្នុង prompt ប្រព័ន្ធ។  
- ផ្ញើ prompt អ្នកប្រើសួរអំពីអាកាសធាតុក្នុងទីក្រុងមួយច្បាស់លាស់។  
- LLM នឹងឆ្លើយបញ្ចេញការហៅឧបករណ៍ទៅកាន់ឧបករណ៍ Brave Search ដែលនឹងមើលទៅដូចជា `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*ចំណាំ៖ ឧទាហរណ៍នេះគ្រាន់តែធ្វើការហៅឧបករណ៍ បើអ្នកចង់ទទួលបានលទ្ធផល អ្នកត្រូវបង្កើតគណនីដោយឥតគិតថ្លៃនៅផែនទី Brave API ហើយកំណត់មុខងារផ្ទាល់ខ្លួន។  

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Meta-Llama-3.1-405B-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-3.3-70B-Instruct, a currently available alternative, instead
model_name = "Llama-3.3-70B-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


tool_prompt=f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha
Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="What is the weather in Stockholm?"),

]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## Llama 3.2  

ទោះបីជាជា LLM ក៏ដោយ ខ្សោយមួយរបស់ Llama 3.1 គឺការខ្វះលទ្ធភាពមូលដ្ឋានមួយឈ្មោះម៉ុលទីម៉ូដាល។ គឺ ឯកភាពរបស់វាដែលមិនអាចប្រើប្រភេទការបញ្ចូលផ្សេងៗគ្នាទេ ដូចជារូបភាពជារូបមន្ត ហើយផ្តល់ការឆ្លើយតបបាន។ សមត្ថភាពនេះជាលក្ខណៈសំខាន់មួយរបស់ Llama 3.2។ លក្ខណៈទាំងនេះរួមមាន៖  

- ម៉ុលទីម៉ូដាល - មានសមត្ថភាពវាយតម្លៃទាំង prompt ខ្លឹមសារ និងរូបភាព  
- ការបម្លែងទំហំតូចរហូតមធ្យម (11B និង 90B) - ផ្តល់ជម្រើសប្រើប្រាស់បតអាចបត់បែនបាន  
- ការបម្លែងតែក្នុងខ្លឹមសារ (1B និង 3B) - អនុញ្ញាតឲ្យគំរូត្រូវបានដាក់នៅលើឧបករណ៍ edge / ទូរស័ព្ទចល័ត និងផ្តល់ការឆ្លើយតបបន្ទាន់ទាប  

ការគាំទ្រម៉ុលទីម៉ូដាលនេះតំណាងឱ្យជាប្រភេទជំហានធំមួយក្នុងពិភពគំរូប្រភពចំហ។ ឧទាហរណ៍កូដខាងក្រោមទទួលទាំងរូបភាពនិង prompt ខ្លឹមសារ ដើម្បីទទួលបានការវិភាគរូបភាព។ ដោយសារ Llama 3.2 90B Vision Instruct ត្រូវបានផ្អាក ឧទាហរណ៍នេះប្រើ `Llama-4-Scout-17B-16E-Instruct` ដែលជាជម្រើសមានស្រាប់ និងគាំទ្រម៉ូលទីម៉ូដាលដោយដើម។  


### ការគាំទ្រម៉ុលទីម៉ូដាលជាមួយ Llama 3.2  

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Llama-3.2-90B-Vision-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-4-Scout-17B-16E-Instruct, a currently available natively multimodal alternative, instead
model_name = "Llama-4-Scout-17B-16E-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="sample.jpg",
                        image_format="jpg",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
```

## ការរៀនមិនឈប់នៅទីនេះ ត្រូវបន្តដំណើរ  

បន្ទាប់ពីបញ្ចប់មេរៀននេះ សូមពិនិត្យមើល [ការប្រមូលផ្តុំការសិក្សា Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) របស់យើង ដើម្បីបន្តកម្ដៅចំណេះដឹង Generative AI របស់អ្នក!  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->