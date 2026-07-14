# ការសង់ជាមួយគ្រួសារម៉ូដែល Meta

## ការណែនាំ

មេរៀននេះ​នឹងគ្របដណ្តប់៖

- ការស្វែងយល់ពីម៉ូដែលគ្រួសារមេតាសំខាន់ៗពីរ - Llama 3.1 និង Llama 3.2
- ការយល់ដឹងអំពីការប្រើប្រាស់ និងស្ថានភាពសម្រាប់ម៉ូដែលនិមួយៗ
- លិខិតកូដសម្រាប់បង្ហាញលក្ខណៈពិសេសពិសេសនៃម៉ូដែលនិមួយៗ


## គ្រួសារម៉ូដែល Meta

ក្នុងមេរៀននេះ យើងនឹងស្វែងយល់ពីម៉ូដែល 2 ឈ្មោះពីគ្រួសារម៉ូដែល Meta ឬ "Llama Herd" - Llama 3.1 និង Llama 3.2។

ម៉ូដែលទាំងនេះមានបំរែបំរួលផ្សេងៗ និងអាចរកបានក្នុង [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)។

> **សម្គាល់៖** GitHub Models នឹងផ្អាកប្រើបញ្ចប់នៅចុងខែ​កក្កដា ឆ្នាំ ២០២៦។ នេះ​គឺជាព័ត៌មាន​លម្អិតបន្ថែមអំពីការប្រើប្រាស់ [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ដើម្បីសាកល្បងជាមួយម៉ូដែល AI។

បំរែបំរួលរបស់ម៉ូដែល៖
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*សម្គាល់ៈ Llama 3 គឺមាន זמវចក្នុង Microsoft Foundry Models ផងដែរ ប៉ុន្តែមិនត្រូវបានគ្របដណ្តប់ក្នុងមេរៀននេះទេ*

## Llama 3.1

នៅកម្រិត 405 ពាន់លានាភាគរយ, Llama 3.1 ត្រូវបានចាត់ទុកជា LLM ប្រភេទបើកប្រភពសេរី។

ម៉ូដែលនេះគឺជាការអាប់ដេតពី Llama 3 ម៉ូដែលដែលបានឲ្យមុន ដោយផ្តល់ជូននូវ៖

- កញ្ចក់បរិបទធំជាងមុន - 128k tokens ប្រៀបធៀបទៅនឹង 8k tokens
- អតិបរមានៃចំនួន​តួអក្សរចេញធំជាង - 4096 ប្រៀបធៀបនឹង 2048
- ការគាំទ្រភាសាច្រើនល្អជាងមុន - ដោយសារការកើនឡើង​នៃ token សម្រាប់ហ្វឹកហាត់

អ្វីៗទាំងនេះធ្វើឲ្យ Llama 3.1 អាចដោះស្រាយករណីប្រើប្រាស់ស្មុគស្មាញជាងមុននៅពេលសាងសង់កម្មវិធី GenAI រួមមាន៖
- ការហៅមុខងារបណ្ដាញដើម - សមត្ថភាពក្នុងការហៅឧបករណ៍ និងមុខងារបណ្តោះអាសន្នក្រៅពីប្រព័ន្ធ LLM
- តុបតែង RAG ដោយការគាំទ្របរិបទធំជាង
- ការបង្កើតទិន្នន័យសិនថេតិច - សមត្ថភាពបង្កើតទិន្នន័យមានប្រសិទ្ធភាពសម្រាប់ការប្រតិបត្តិការដូចជា fine-tuning

### ការហៅមុខងារដើម

Llama 3.1 ត្រូវបានលំហាត់ពិសេសដើម្បីធ្វើមុខងារហៅឧបករណ៍ឲ្យមានប្រសិទ្ធភាពជាងមុន។ វាក៏មានឧបករណ៍ដង្ហែពីរដែលម៉ូដែលអាចសម្គាល់ថាត្រូវប្រើប្រាស់ដោយផ្អែកលើការបញ្ចូលពីអ្នកប្រើ។ ឧបករណ៍ទាំងនេះមាន៖

- **Brave Search** - អាចប្រើស្វែងរកព័ត៌មានថ្មីៗដូចជា តែអាកាសធាតុ តាមរយៈការស្វែងរកតាមវេបសាយ
- **Wolfram Alpha** - អាចប្រើសម្រាប់គណនាគណិតវិទ្យាស្មុគស្មាញ ដូច្នេះមិនចាំបាច់ត្រូវសរសេរមុខងាររបស់អ្នកផ្ទាល់។

អ្នកក៏អាចបង្កើតឧបករណ៍ផ្ទាល់ខ្លួនដែលម៉ូដែលអាចហៅបានផងដែរ។

ក្នុងឧទាហរណ៍កូដខាងក្រោម៖

- យើងកំណត់ឧបករណ៍ដែលមាន (brave_search, wolfram_alpha) នៅក្នុងប្រព័ន្ធ prompt។
- ផ្ញើការស្នើសុំពីអ្នកប្រើដែលសួរអំពីអាកាសធាតុរបស់ទីក្រុងមួយណា។
- LLM នឹងឆ្លើយតបជាមួយការហៅឧបករណ៍ទៅ Brave Search ដែលត្រូវពង្រឹងក្នុងទម្រង់ `<|python_tag|>brave_search.call(query="Stockholm weather")`

*សម្គាល់ៈ ឧទាហរណ៍នេះគ្រាន់តែធ្វើការហៅឧបករណ៍ប៉ុណ្ណោះ ប្រសិនបើអ្នកចង់ទទួលលទ្ធផល អ្នកត្រូវបង្កើតគណនីឥតគិតថ្លៃនៅលើទំព័រ Brave API ហើយកំណត់មុខងារផង។*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# ទទួលយកទាំងនេះពីទំព័រ "ទិដ្ឋភាពទូទៅ" របស់គម្រោង Microsoft Foundry របស់អ្នក
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

ទោះបីជាគឺជាម៉ូដែល LLM ក៏ដោយ ការលំបាកមួយរបស់ Llama 3.1 គឺមិនគាំទ្រពហុរូបមន្ត (មិនអាចប្រើបញ្ចូលចម្លងជាប្រភេទផ្សេងៗដូចជា រូបភាពជាព្រមជាមួយការស្នើសុំ និងផ្តល់ចម្លើយ)។ សមត្ថភាពនេះគឺជាលក្ខណៈមួយសំខាន់នៃ Llama 3.2។ លក្ខណៈទាំងនេះរួមមាន៖

- ពហុរូបមន្ត - មានសមត្ថភាពវាយតម្លៃទាំងតែ​ខ្លឹម​សារ និងរូបភាព
- មានបំរែបំរួលទំហំតូចទៅមធ្យម (11B និង 90B) - ផ្តល់ជូនជម្រើសដាក់ចេញដែលបត់បែនបាន
- បំរែបំរួលសម្រាប់តែ​អត្ថបទតែប៉ុណ្ណោះ (1B និង 3B) - អនុញ្ញាតឲ្យម៉ូដែលបង្ហោះលើឧបករណ៍ Edge / Mobile ហើយផ្តល់នូវពេលលំដាប់ទាប

ការគាំទ្រពហុរូបមន្តនេះជាជំហានដ៏ធំមួយក្នុងពិភពម៉ូដែលបើកប្រភព។ ឧទាហរណ៍កូដខាងក្រោមចូលចិត្តទាំងរូបភាព និងតែ​សម្រាប់ស្វែងយល់វិភាគរូបភាពពី Llama 3.2 90B។


### ការគាំទ្រពហុរូបមន្តជាមួយ Llama 3.2

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

# ទាញយកផ្ទាំងនេះពីទំព័រពិពណ៌នាសរុប "Overview" នៃគម្រោង Microsoft Foundry របស់អ្នក
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

## ការសិក្សាមិនទប់ស្កាត់នៅទីនេះ ត្រូវបន្តដំណើរទៀត

បន្ទាប់ពីបញ្ចប់មេរៀននេះ សូមពិនិត្យមើល [ការប្រមូលផ្តុំការសិក្សា AI ការបង្កើត](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) របស់យើង ដើម្បីបន្តធ្វើឲ្យចំណេះដឹង Generative AI របស់អ្នកកើនឡើង!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->