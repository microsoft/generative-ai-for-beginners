# ការជ្រើសរើស និងកំណត់រចនាសម្ព័ន្ធអ្នកផ្គត់ផ្គង់ LLM 🔑

តំណែងការងារ **អាច** ត្រូវបានកំណត់ដំណើរការ ដើម្បីធ្វើការជាមួយការចុះបញ្ជីម៉ូដែលភាសាធំ (LLM) មួយឬច្រើន តាមរយៈអ្នកផ្គត់ផ្គង់សេវាកម្មដែលគាំទ្រដូចជា OpenAI, Azure ឬ Hugging Face។ អ្នកផ្គត់ផ្គង់ទាំងនេះផ្តល់នូវ _ចំណុចចូលផ្ទះ (API)_ ដែលយើងអាចចូលប្រើបានដោយកម្មវិធីជាមួយអត្តសញ្ញាណត្រឹមត្រូវ (កូនសោ API ឬតូកែន)។ នៅក្នុងមេរៀននេះ យើងពិនិត្យអ្នកផ្គត់ផ្គង់ទាំងនេះ៖

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) ជាមួយម៉ូដែលផ្សេងៗដែលរួមមានស៊េរី GPT មូលដ្ឋាន។
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) សម្រាប់ម៉ូដែល OpenAI ដែលផ្តោតលើភាពរួមបញ្ចូលសម្រាប់អង្គការធំ
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) សម្រាប់ម៉ូដែលដើមចេញ និងម៉ាស៊ីនបម្រើបម្លែងសេចក្ដីសន្និដ្ឋាន

**អ្នកត្រូវប្រើគណនីផ្ទាល់ខ្លួនសម្រាប់មេរៀនទាំងនេះ**។ តំណែងការងារត្រូវបានជាជម្រើស ដូច្នេះអ្នកអាចជ្រើសកំណត់លំហូរមួយ ឬគ្រប់គ្រាន់ ឬមិនមានអ្នកផ្គត់ផ្គង់ណាមួយផ្អែកលើចំណាប់អារម្មណ៍របស់អ្នក។ ការណែនាំខ្លះសម្រាប់ការចុះឈ្មោះ៖

| ចុះឈ្មោះ | តម្លៃ | តួកូនសោ API | លំហូរ | អត្ថបទបន្ថែម |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [តម្លៃ](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [គម្រោងផ្អែក](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [គ្មានកូដ, វេបសាយ](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | មានម៉ូដែលជាច្រើនជ្រើសរើស |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [តម្លៃ](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [ដំណើរការឆាប់រហ័ស SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [ដំណើរការStudioឆាប់រហ័ស](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [ត្រូវដាក់ពាក្យជាមុនសម្រាប់ការចូលប្រើ](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [តម្លៃ](https://huggingface.co/pricing) | [តូកែនចូលដំណើរការ](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat មានម៉ូដែលកំណត់](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

អនុវត្តតាមការណែនាំខាងក្រោម ដើម្បី _កំណត់រចនាសម្ព័ន្ធ_ ឃ្លាំងសម្រង់នេះសម្រាប់ប្រើជាមួយអ្នកផ្គត់ផ្គង់ផ្សេងៗ។ តំណែងការងារដែលត្រូវការ​ការផ្គត់ផ្គង់ជាក់លាក់ នឹងមានស្លាកដូចខាងក្រោមក្នុងឈ្មោះឯកសារ៖

- `aoai` - ត្រូវការ Azure OpenAI endpoint និងកូនសោ
- `oai` - ត្រូវការ OpenAI endpoint និងកូនសោ
- `hf` - ត្រូវការ Hugging Face token

អ្នកអាចកំណត់រចនាសម្ព័ន្ធអ្នកផ្គត់ផ្គង់មួយ ឬគ្មាន ឬគ្រប់គ្រាន់។ ការងារដែលពាក់ព័ន្ធនឹងបង្ហាញកំហុសនៅពេលគ្មានតំណរភ្ជាប់ដែលត្រូវបានផ្តល់។

## បង្កើតឯកសារ `.env`

យើងសន្មត់ថាអ្នកបានអានការណែនាំខាងលើរួចហើយ និងបានចុះឈ្មោះជាមួយអ្នកផ្គត់ផ្គង់សមស្រប ហើយបានទទួលអត្តសញ្ញាណផ្ទៀងផ្ទាត់ត្រូវការ (API_KEY ឬ token)។ សម្រាប់ Azure OpenAI យើងសន្មត់ថាអ្នកមានការចុះបញ្ជីសេវាកម្ម Azure OpenAI (endpoint) ដែលបានដំណើរការ មួយក៏ដូចជាម៉ូដែល GPT មួយយ៉ាងហោចណាស់សម្រាប់បញ្ចប់ការឆាត។

ជំហានបន្ទាប់គឺកំណត់រចនាសម្ព័ន្ធ **អថេរបរិស្ថាន​ក្នុងបរិបទ​តំបន់​ផ្ទាល់** របស់អ្នក ដូចខាងក្រោម៖

1. ស្វែងរកឯកសារ `.env.copy` នៅថតម៉ាស៊ីនដើមដែលមានមាតិកាមើលទៅដូចជា៖

   ```bash
   # អ្នកផ្គត់ផ្គង់ OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # ការកំណត់លំនាំដើមបានដាក់សោហើយ!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. ចម្លងឯកសារនោះទៅ `.env` ដោយប្រើពាក្យបញ្ជាក្រោមនេះ។ ឯកសារនេះ _gitignore-d_ ដើម្បីរក្សាគន្លងសម្ងាត់។

   ```bash
   cp .env.copy .env
   ```

3. បំពេញតម្លៃ (ជំនួសម៉ាកកន្លែងផ្នែកខាងស្ដាំនៃ `=`) ដូចបានពិពណ៌នាក្នុងផ្នែកបន្ទាប់។

4. (ជាជម្រើស) ប្រសិនបើអ្នកប្រើ GitHub Codespaces អ្នកអាចរក្សាទុកអថេរបរិស្ថានជារឿង _Codespaces secrets_ ដែលភ្ជាប់ជាមួយឃ្លាំងនេះ។ នៅក្នុងករណីនោះ អ្នកមិនចាំបាច់កំណត់ឯកសារ .env ក្នុងតំបន់ផ្ទាល់ទេ។ **ប៉ុន្តែ សូមចំណាំថាជម្រើសនេះដំណើរការតែប្រសិនបើអ្នកប្រើ GitHub Codespaces ប៉ុណ្ណោះ។** អ្នកត្រូវកំណត់ឯកសារ .env នៅក្នុងតំបន់ផ្ទាល់ ប្រសិនបើអ្នកប្រើ Docker Desktop ចំពោះវិធីសាស្រ្តផ្សេង។

## បំពេញព័ត៌មានក្នុងឯកសារ `.env`

មកមើលឈ្មោះអថេរដើម្បីយល់ពីតើវាបង្ហាញអ្វី៖

| អថេរ | សេចក្ដីពិពណ៌នា |
| :--- | :--- |
| HUGGING_FACE_API_KEY | នេះគឺជា token ចូលប្រើរបស់អ្នកដែលអ្នកបានកំណត់នៅក្នុងគណនីផ្ទាល់ខ្លួន |
| OPENAI_API_KEY | នេះគឺជាកូនសោអនុញ្ញាតសម្រាប់ប្រើសេវាដែលមិនមែន Azure OpenAI |
| AZURE_OPENAI_API_KEY | នេះគឺជាកូនសោអនុញ្ញាតសម្រាប់ប្រើសេវាកម្មនោះ |
| AZURE_OPENAI_ENDPOINT | នេះគឺជា endpoint ដែលបានដំណើរការសម្រាប់ធនធាន Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | នេះគឺជា endpoint ការចុះបញ្ជីម៉ូដែល _បង្កើតអត្ថបទ_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | នេះគឺជា endpoint ការចុះបញ្ជីម៉ូដែល _វេកទ័រអត្ថបទ_ |
| | |

ចំណាំៈ អថេរចុងក្រោយពី Azure OpenAI សំដៅទៅលើម៉ូដែលលំនាំដើមសម្រាប់បញ្ចប់ការឆាត (បង្កើតអត្ថបទ) និងស្វែងរកវ៉ិចទ័រ (វេកទ័រ) តាមលំដាប់។ សេចក្ដីណែនាំសម្រាប់កំណត់រចនាសម្ព័ន្ធនឹងត្រូវបានបញ្ជាក់នៅក្នុងតំណែងការងារពាក់ព័ន្ធ។

## កំណត់រចនាសម្ព័ន្ធ Azure៖ ពី Portal

តម្លៃ endpoint និងកូនសោ Azure OpenAI អាចរកបាននៅក្នុង [ផតថល Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) ដូច្នេះចូរចាប់ផ្តើមនៅទីនោះ។

1. ចូរចូលទៅ [ផតថល Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. ចុចជម្រើស **Keys and Endpoint** ក្នុងផ្នែកម៉ឺនុយខាងឆ្វេង។
1. ចុច **បង្ហាញកូនសោ** - អ្នកគួរមើលឃើញ KEY 1, KEY 2 និង Endpoint។
1. ប្រើតម្លៃ KEY 1 សម្រាប់ AZURE_OPENAI_API_KEY
1. ប្រើតម្លៃ Endpoint សម្រាប់ AZURE_OPENAI_ENDPOINT

បន្ទាប់មក យើងត្រូវការចំណុចចូលសម្រាប់ម៉ូឌែលជាក់លាក់ដែលបានចុះបញ្ជី។

1. ចុចជម្រើស **Model deployments** នៅផ្នែកម៉ឺនុយខាងឆ្វេង សម្រាប់ធនធាន Azure OpenAI។
1. នៅផ្នែកផ្ទាំងគោលដៅ ចុច **គ្រប់គ្រងការចុះបញ្ជី**

នេះនឹងនាំអ្នកទៅគេហទំព័រ Azure OpenAI Studio ដែលយើងនឹងឃើញតម្លៃផ្សេងៗដូចបានពិពណ៌នាខាងក្រោម។

## កំណត់រចនាសម្ព័ន្ធ Azure៖ ពី Studio

1. ចូលទៅ [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **ពីធនធានរបស់អ្នក** ដូចបានពិពណ៌នាពីមុន។
1. ចុចផ្ទាំង **Deployments** (ម៉ឺនុយខាងឆ្វេង) ដើម្បីមើលម៉ូឌែលដែលបានចុះបញ្ជីឡើងវិញ។
1. ប្រសិនបើម៉ូឌែលដែលអ្នកចង់ប្រើមិនមានទេ សូមប្រើ **បង្កើតការចុះបញ្ជីថ្មី** ដើម្បីចុះបញ្ជីវា។
1. អ្នកត្រូវការ ម៉ូឌែល _បង្កើតអត្ថបទ_ — យើងផ្តល់អនុសាសន៍: **gpt-35-turbo**
1. អ្នកត្រូវការ ម៉ូឌែល _វេកទ័រអត្ថបទ_ — យើងផ្តល់អនុសាសន៍ **text-embedding-ada-002**

ឥឡូវធ្វើបច្ចុប្បន្នភាពអថេរបរិស្ថាន ដើម្បីបង្ហាញសេចក្ដីយោងទៅ _ឈ្មោះការចុះបញ្ជី_ ដែលបានប្រើ។ ជាទូទៅវានឹងដូចគ្នានៅជាមួយឈ្មោះម៉ូឌែល លុះត្រាតែអ្នកបានផ្លាស់ប្តូរយ៉ាងច្បាស់លាស់។ ឧទាហរណ៍ អ្នកអាចមាន៖

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**កុំភ្លេចរក្សាទុកឯកសារ .env ពេលបញ្ចប់**។ អ្នកអាចចាកចេញពីឯកសារនោះ ហើយត្រឡប់ទៅការណែនាំសម្រាប់រត់ notebook ។

## កំណត់រចនាសម្ព័ន្ធ OpenAI៖ ពីគណនីអង្គភាព

កូនសោ API របស់ OpenAI អាចរកបាននៅក្នុង [គណនី OpenAI របស់អ្នក](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)។ ប្រសិនបើអ្នកមិនមានទេ អ្នកអាចចុះឈ្មោះគណនី ហើយបង្កើតកូនសោ API បាន។ បន្ទាប់ពីមានកូនសោ អ្នកអាចប្រើសម្រាប់បំពេញអថេរ `OPENAI_API_KEY` នៅក្នុងឯកសារ `.env` ។

## កំណត់រចនាសម្ព័ន្ធ Hugging Face៖ ពីគណនីផ្ទាល់ខ្លួន

តូកែន Hugging Face របស់អ្នកអាចរកបាននៅក្នុងគណនីផ្ទាល់ខ្លួនរបស់អ្នកក្រោម[Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst)។ មិនត្រូវបង្ហោះឬចែករំលែកវាជាសាធារណៈទេ។ ផ្ទុយពីនេះ សូមបង្កើត token ថ្មីសម្រាប់គម្រោងនេះ ហើយចម្លងវាចូលក្នុងឯកសារ `.env` ក្រោមអថេរ `HUGGING_FACE_API_KEY`។ _ចំណាំ៖_ នេះបច្ចេកទេសមិនមែនជា key API នេះទេ ប៉ុន្តែប្រើសម្រាប់អត្តសញ្ញាណ តែយើងរក្សា ឈ្មោះនេះសម្រាប់ការត្រួតពិនិត្យតម្រូវការដូចគ្នា។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការកំណត់សូមប្រយ័ត្ន**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះបីយើងខិតខំទុកចិត្តលទ្ធផលឱ្យមានភាពត្រឹមត្រូវ ក៏សូមយល់ឲ្យបានដឹងថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុสนិងការមិនត្រឹមត្រូវ។ ឯកសារដើមភាសាម្ចាស់៖​ គួរតែចាត់ទុកថាជា ដៃគូប្រឹក្សាផ្លូវការដែលមានសិទ្ធិ។ សម្រាប់ព័ត៌មានសំខាន់ៗ ការបកប្រែដោយមនុស្សជំនាញត្រូវបានណែនាំ។ យើងមិនទទួលបន្ទុកចំពោះការយល់ច្រឡំនូវការច្រឡំណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->