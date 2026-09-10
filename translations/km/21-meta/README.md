# ការសាងសង់ជាមួយម៉ូដែលគ្រួសារមេតា 

## ការណែនាំ 

មេរៀននេះនឹងគ្របដណ្តប់: 

- ការត្រៀមទូទៅពីម៉ូដែលគ្រួសារមេតា២សំណុំចម្បង - Llama 3.1 និង Llama 3.2 
- ការយល់ដឹងអំពីករណីប្រើប្រាស់ និងស្ថានភាពសម្រាប់ម៉ូដែលនីមួយៗ 
- ឧទាហរណ៍កូដដើម្បីបង្ហាញលក្ខណៈពិសេសរបស់ម៉ូដែលនីមួយៗ 


## ក្រុមម៉ូដែលគ្រួសារមេតា 

នៅក្នុងមេរៀននេះ សូមយើងរុករកម៉ូដែល ២ ពីគ្រួសារមេតា ឬ "Llama Herd" គឺ Llama 3.1 និង Llama 3.2។

ម៉ូដែលទាំងនេះមានរាងខុសគ្នា និងមានលក់ក្នុង [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)។

> **សម្គាល់៖** GitHub Models នឹងបញ្ចប់ដំណើរការនៅចុងខែ֊កក្កដា ២០២៦។ នេះជាលម្អិតបន្ថែមអំពីការប្រើប្រាស់ [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ដើម្បីសាកល្បងជាមួយម៉ូដែល AI។

ប្រភេទម៉ូដែល: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*សម្គាល់៖ Llama 3 ក៏មានផ្តល់មានក្នុង Microsoft Foundry Models ដែរ ប៉ុន្តែមិនត្រូវបានគ្របដណ្តប់ក្នុងមេរៀននេះទេ*

## Llama 3.1 

ជាមួយនឹង ៤០៥ ពានប៉ារ៉ាម៉ែត្រ Llama 3.1 ចូលទៅក្នុងប្រភេទ LLM open source ។ 

ម៉ូដែលនេះជាការអាប់ដេតពីការចេញផ្សាយ Llama 3 មុន ដោយផ្តល់: 

- បង្អួចនៃcontext ធំជាង - ១២៨,០០០ token ប្រឆាំងនឹង ៨,០០០ token 
- លេខបញ្ចេញចាប់ Token អតិបរមាធំជាង - ៤០៩៦ ភាគនៃ ២០៤៨ 
- គាំទ្រភាសាច្រើនល្អជាង - ដោយសារការកើនឡើងនៃ training tokens 

អ្នកអាចប្រើ Llama 3.1 ក្នុងករណីប្រើប្រាស់រឹងមាំពេលសាងសង់កម្មវិធី GenAI រួមមាន: 
- Native Function Calling - សមត្ថភាពក្នុងការហៅឧបករណ៍ និងមុខពិសេសខាងក្រៅ workflow LLM
- ប្រសិទ្ធភាព RAG ល្អជាង - ដោយសារបង្អួច context ខ្ពស់
- ការបង្កើតទិន្នន័យសំណុំ - សមត្ថភាពបង្កើតទិន្នន័យមានប្រសិទ្ធភាពសម្រាប់ការប្រតិបត្តិ fine-tuning

### Native Function Calling 

Llama 3.1 ត្រូវបានលុបបំបាត់ឱ្យមានប្រសិទ្ធភាពក្នុងការហៅមុខងារ ឬឧបករណ៍។ វាក៏មានឧបករណ៍ពីរដែលទេពទេពអាចកំណត់ថាត្រូវបានប្រើប្រាស់ដោយផ្អែកទៅលើការបញ្ចូលពីអ្នកប្រើ។ ឧបករណ៍ទាំងនេះមាន: 

- **Brave Search** - អាចប្រើស្វែងរកព័ត៌មានថ្មីៗដូចជាគ្រោះអាកាសធាតុ តាមការស្វែងរកវែបសាយ 
- **Wolfram Alpha** - អាចប្រើសម្រាប់គណិតវិទ្យាដែលស្មុគស្មាញ ដូច្នេះមិនចាំបាច់សរសេរមុខងាររបស់អ្នកទេ។ 

អ្នកក៏អាចបង្កើតឧបករណ៍ផ្ទាល់ខ្លួនដែល LLM អាចហៅបាន។

នៅក្នុងឧទាហរណ៍កូដខាងក្រោម: 

- យើងកំណត់ឧបករណ៍ដែលមាន (brave_search, wolfram_alpha) នៅក្នុង system prompt។ 
- ផ្ញើសំណួរពីអ្នកប្រើដែលសួរអំពីអាកាសធាតុក្នុងទីក្រុងណាមួយ។ 
- LLM នឹងឆ្លើយតបជាមួយការហៅឧបករណ៍ទៅឧបករណ៍ Brave Search ដែលនឹងបង្ហាញដូចជា `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*សម្គាល់៖ ឧទាហរណ៍នេះគ្រាន់តែធ្វើការហៅឧបករណ៍ប៉ុណ្ណោះ ប្រសិនបើអ្នកចង់បានលទ្ធផល អ្នកត្រូវបង្កើតគណនីឥតគិតថ្លៃនៅទំព័រ Brave API និងកំណត់មុខងារផ្ទាល់ខ្លួន។*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# ទាញយកវាទៅពីទំព័រ "ទិដ្ឋភាពទូទៅ" នៃគម្រោង Microsoft Foundry របស់អ្នក
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Meta-Llama-3.1-405B-Instruct"

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

ទោះបីជាមានជាគ្រឿង LLM ក៏ដោយ កំណត់ចំនួនមួយនៃ Llama 3.1 គឺមិនមានបច្ចេកទេស multimodality។ មានន័យថា មិនអាចប្រើប្រភេទការបញ្ចូលផ្សេងៗដូចជារូបភាពជាសញ្ញាឬផ្តល់ចម្លើយ។ សមត្ថភាពនេះគឺជាលក្ខណៈសំខាន់មួយនៃ Llama 3.2។ លក្ខណៈទាំងនេះរួមមាន: 

- Multimodality - មានសមត្ថភាពវាយតម្លៃទាំងអត្ថបទ និងសញ្ញារូបភាព 
- ការប្រែប្រួលទំហំតូចទៅមធ្យម (11B និង 90B) - ផ្តល់ជម្រើសដាក់ឧបករណ៍ដោយបត់បែន, 
- ការប្រែប្រួលអត្ថបទតែប៉ុណ្ណោះ (1B និង 3B) - អនុញ្ញាតឱ្យម៉ូដែលត្រូវបានដាក់លើឧបករណ៍ edge / ឧបករណ៍ចល័ត ហើយផ្តល់ latency ទាប 

ការគាំទ្រ multimodal គឺជាចំណុចវិនិយោគដ៏ធំមួយនៅក្នុងពិភពម៉ូដែល open source។ ឧទាហរណ៍កូដខាងក្រោមយកទាំងរូបភាព និងអត្ថបទជាសញ្ញា ដើម្បីទទួលបានការវិភាគពី Llama 3.2 90B។ 


### ការគាំទ្រ Multimodal ជាមួយ Llama 3.2

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

# ទទួលបានទាំងនេះពី​ទំព័រ "ទិដ្ឋភាពទូទៅ" នៃគoproject Microsoft Foundry របស់អ្នក
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Llama-3.2-90B-Vision-Instruct"

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

## ការសិក្សាមិនបញ្ឈប់នៅទីនេះ បន្តដំណើរការ 

បន្ទាប់ពីបញ្ចប់មេរៀននេះ សូមពិនិត្យមើល [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) របស់យើង ដើម្បីបន្តបង្កើនចំណេះដឹង AI យ៉ាងមានប្រសិទ្ធភាព!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->