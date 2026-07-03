# ការសាងសង់ជាមួយម៉ូឌែលគ្រួសារ Meta

## ការណែនាំ

មេរៀននេះនឹងគ្របដណ្តប់៖

- ស្វែងយល់អំពីម៉ូឌែលគ្រួសារ Meta សំខាន់ៗពីរ - Llama 3.1 និង Llama 3.2
- យល់ពីករណីប្រើប្រាស់ និងស្ថានการณ์សម្រាប់ម៉ូឌែលនីមួយៗ
- ទិដ្ឋភាពកូដបង្ហាញលក្ខណៈពិសេសរបស់ម៉ូឌែលនីមួយៗ

## គ្រួសារម៉ូឌែល Meta

ក្នុងមេរៀននេះ យើងនឹងស្វែងយល់ពីម៉ូឌែល 2 ពីគ្រួសារ Meta ឬ "Llama Herd" - Llama 3.1 និង Llama 3.2

ម៉ូឌែលទាំងនេះមានវ៉ារីយ៉ង់ផ្សេងៗ ហើយមាននៅលើទីផ្សារម៉ូឌែល GitHub។ នេះជាព័ត៌មានបន្ថែមអំពីការប្រើម៉ូឌែល GitHub ដើម្បី [ធ្វើគំរូជាមួយម៉ូឌែល AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)។

វ៉ារីយ៉ង់ម៉ូឌែល៖
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*ចំណាំៈ Llama 3 ក៏មាននៅលើម៉ូឌែល GitHub ផងដែរ ប៉ុន្តែមិនមានក្នុងមេរៀននេះទេ*

## Llama 3.1

នៅកម្រិត 405 ព្រះរាជាណាចក្របារ៉ាម៉ែត្រ Llama 3.1 យោងតាមប្រភេទ LLM គោលបើកផ្សាយ។

ម៉ូឌែលនេះជាការអាប់ដេតពីការចេញផ្សាយមុន Llama 3 ដោយផ្តល់៖

- បង្អែក context ធំជាង - 128k តុក្កតា ប្រៀបធៀបទៅ 8k តុក្កតា
- លទ្ធផលអតិបរមា តុក្កតា ចេញធំជាង - 4096 ប្រៀបធៀបទៅ 2048
- គាំទ្រភាសាច្រើនកាន់តែប្រសើរ - ដោយសារការបន្ថែមតុក្កតាដែលបានហ្វឹកហាត់

លក្ខណៈទាំងនេះអនុញ្ញាតឱ្យ Llama 3.1 អាចគ្រប់គ្រងករណីប្រើប្រាស់ស្មុគស្មាញកាន់តែច្រើននៅពេលសាងសង់កម្មវិធី GenAI រួមមាន៖
- ការហៅមុខងារពីក្នុង - សមត្ថភាពហៅឧបករណ៍ និង មុខងារខាងក្រៅ workflow LLM
- ការធ្វើការល្អប្រសើរជាមួយ RAG - ដោយសារបង្អែក context ខ្ពស់
- ការបង្កើតទិន្នន័យសំរបសំរួល - សមត្ថភាពបង្កើតទិន្នន័យមានប្រសិទ្ធភាពសម្រាប់ភារកិច្ចដូចជាការសម្រឹកសមរាងឆ្ពោះទៅតូច

### ការហៅមុខងារពីក្នុង

Llama 3.1 ត្រូវបានហ្វឹកហាត់បន្ថែមឲ្យប្រសើរឡើងក្នុងការហៅមុខងារ ឬឧបករណ៍។ វាក៏មានឧបករណ៍ 2 built-in ដែលម៉ូឌែលអាចអះអាងថាត្រូវបានប្រើយ៉ាងត្រឹមត្រូវបន្ទាប់ពីការឈ្នួលពីអ្នកប្រើ។ ឧបករណ៍ទាំងនេះមាន៖

- **Brave Search** - អាចប្រើសម្រាប់ទទួលព័ត៌មានទាន់សម័យដូចជាកាលអាកាសធាតុ ដោយធ្វើការស្វែងរកក្នុងបណ្តាញ
- **Wolfram Alpha** - អាចប្រើសម្រាប់គណិតវិទ្យាកំរិតស្មុគស្មាញ ដូច្នេះមិនចាំបាច់សរសេរមុខងារផ្ទាល់ខ្លួនទេ។

អ្នកក៏អាចបង្កើតឧបករណ៍ផ្ទាល់ខ្លួនដែល LLM អាចហៅបានផងដែរ។

ក្នុងកូដឧទាហរណ៍ខាងក្រោម៖

- យើងកំណត់ឧបករណ៍ដែលមាន (brave_search, wolfram_alpha) ក្នុង system prompt។
- ផ្ញើការស្នើរបស់អ្នកប្រើដែលស្នើពីអាកាសធាតុក្នុងទីក្រុងណាមួយ។
- LLM នឹងឆ្លើយតបជាមួយការហៅឧបករណ៍ Brave Search ដែលមានរូបរាងដូចជា `<|python_tag|>brave_search.call(query="Stockholm weather")`

*ចំណាំៈ ឧទាហរណ៍នេះធ្វើតែនៅក្នុងការហៅឧបករណ៍ បើអ្នកចង់ទទួលលទ្ធផល អ្នកត្រូវបង្កើតគណនីឥតគិតថ្លៃនៅលើទំព័រ Brave API ហើយកំណត់មុខងារដោយខ្លួនឯង។*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"

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

បើទោះជាគឺ LLM មួយ កំណត់ខ្វក់មួយរបស់ Llama 3.1 គឺការខ្វះមុខងារ multimodality។ នោះគឺមិនអាចប្រើប្រាស់ប្រភេទទិន្នន័យបញ្ចូលផ្សេងៗដូចជារូបភាពជាការស្នើរបាន ហើយផ្តល់ចម្លើយបាន។ សមត្ថភាពនេះគឺជាលក្ខណៈសំខាន់មួយរបស់ Llama 3.2។ លក្ខណៈទាំងនេះរួមមាន៖

- Multimodality - មានសមត្ថភាពវាយតម្លៃទាំងសារនិងរូបភាពស្នើរ
- ផ្លាស់ប្តូរទំហំ តូចដល់មធ្យម (11B និង 90B) - ផ្ដល់ជម្រើសការចេញផ្សាយបត់បែនបាន
- វ៉ារីយ៉ង់សម្រាប់អត្ថបទតែប៉ុណ្ណោះ (1B និង 3B) - អាចប្រើបានលើឧបករណ៍គោលដៅ/ទូរស័ព្ទ និងផ្តល់ latency ចន្លោះទាប

ការគាំទ្រម៉ុលទីម៉ូឌယ်គឺជាជំហានដ៏ធំមួយនៅក្នុងពិភពម៉ូឌែលប្រភពបើក។ ឧទាហរណ៍កូដខាងក្រោមទទួលបានទាំងរូបភាព និងស្នើរសារអត្ថបទសម្រាប់ទទួលបានវិភាគរូបភាពពី Llama 3.2 90B។

### ការគាំទ្រម៉ុលទីម៉ូឌែលជាមួយ Llama 3.2

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

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
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

## ការរៀនមិនឈប់នៅទីនេះ បន្តដំណើរការ

បន្ទាប់ពីបញ្ចប់មេរៀននេះ សូមពិនិត្យមើល [សំណុំបែបបទសិក្សា Generative AI របស់យើង](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ដើម្បីបន្តកម្រិតចំណេះដឹង Generative AI របស់អ្នក!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការជូនដំណឹង**៖  
ឯកសារនេះត្រូវបានបង្រ្កាបដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំប្រឹងប្រែងដើម្បីភាពត្រឹមត្រូវ សូមយក​ចិត្តទុកដាក់ថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុសឬការមិនត្រឹមត្រូវបាន។ ឯកសារដើមក្នុងភាសាទីប្រឹក្សារបស់វាគួរត្រូវបានពិចារណាជា աղբប្រឹក្សា​ដែលមានសិទ្ធិស្គាល់។ សម្រាប់ព័ត៌មានសំខាន់ អ្នកត្រូវបានណែនាំឱ្យប្រើការបកប្រែដោយមនុស្សជំនាញវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->