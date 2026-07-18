# ការជ្រើសរើស និងកំណត់រចនាសម្ព័ន្ធអ្នកផ្គត់ផ្គង់ LLM 🔑

ការចាត់តាំង **អាច** ត្រូវបានកំណត់ឡើងវិញដើម្បីធ្វើការតបទៅលើការតំឡើងម៉ូដែលភាសាធំ (LLM) មួយឬច្រើនតាមរយៈអ្នកផ្គត់ផ្គង់សេវាដែលគាំទ្រដូចជា OpenAI, Azure ឬ Hugging Face។ ពួកនេះផ្ដល់ជូននូវ _ចំណុចបញ្ចប់ដែលផ្ទុកនៅលើម៉ោងបម្រើ_ (API) ដែលយើងអាចចូលដំណើរការដោយកម្មវិធីជាមួយសញ្ញាបត្រដូចជាគន្លង API ឬសញ្ញា token ដែលត្រឹមត្រូវ។ ក្នុងវគ្គបណ្ដុះបណ្ដាលនេះ យើងនិយាយពីអ្នកផ្គត់ផ្គង់ទាំងនេះ៖

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) ជាមួយម៉ូដែលចម្រុះ រួមទាំងស៊េរី GPT ហ្នឹង។
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) សម្រាប់ម៉ូដែល OpenAI ដែលផ្តោតលើភាពរួមមានសមត្ថភាពសម្រាប់សហគ្រាស។
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) សម្រាប់ចំណុចបញ្ចប់ និងគន្លង API មួយដើម្បីចូលដំណើរការម៉ូដែលរយៈរាប់រយពី OpenAI, Meta, Mistral, Cohere, Microsoft និងផ្សេងៗទៀត (ជំនួសម៉ូដែល GitHub ដែលនឹងផុតកំណត់នៅចុងខែកក្កដា ២០២៦)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) សម្រាប់ម៉ូដែលវិជ្ជាជីវៈដើម និងម៉ាស៊ីនបំលែងសម្រាប់និយាយភាសា
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ឬ [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ប្រសិនបើអ្នកចង់ដំណើរការម៉ូដែលពេញលេញជាលក្ខណៈមូលដ្ឋាននៅលើឧបករណ៍ផ្ទាល់ខ្លួន រួមមិនមានការជាវសេវាមេឃទេ។

**អ្នកត្រូវការប្រើគណនីផ្ទាល់ខ្លួនសម្រាប់លំហាត់ទាំងនេះ**។ ការចាត់តាំងជាច្រើនគឺជាជម្រើស អ្នកអាចជ្រើសបានកំណត់មួយ រឺទាំងអស់ ឬមួយផងដោយផ្អែកលើចំណាប់អារម្មណ៍របស់អ្នក។ ការណែនាំខ្លះសម្រាប់ការចុះឈ្មោះ៖

| ចុះឈ្មោះ | ថ្លៃ | គន្លង API | កន្លែងលេង | កំណត់ចំណាំ |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [តម្លៃ](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [ផ្អែកលើគម្រោង](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [គ្មានកូដ, វេបសាយ](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | មានម៉ូដែលជាច្រើន |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [តម្លៃ](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [ចាប់ផ្តើមរហ័ស SDK](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [ចាប់ផ្តើមរហ័ស Studio](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [ត្រូវតែដាក់ពាក្យស្នើសុំចូលមុន](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [តម្លៃ](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [ទំព័រពិពណ៌នាគម្រោង](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | មានជាន់ឥតគិតថ្លៃ; ចំណុចបញ្ចប់ និងគន្លងសម្រាប់អ្នកផ្គត់ផ្គង់ម៉ូដែលជាច្រើន |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [តម្លៃ](https://huggingface.co/pricing) | [សញ្ញាអ្នកចូលប្រើ](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat មានម៉ូដែលកំណត់](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | ឥតគិតថ្លៃ (ដំណើរការនៅលើឧបករណ៍របស់អ្នក) | មិនត្រូវការទេ | [Local CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | ពេញលេញក្រៅបណ្តាញ, ចំណុចបញ្ចប់សមរម្យនឹង OpenAI |
| | | | | |

អនុវត្តតាមសេចក្តីណែនាំខាងក្រោមដើម្បី _កំណត់រចនាសម្ព័ន្ធ_ រឹងរាំងនេះសម្រាប់ប្រើជាមួយអ្នកផ្គត់ផ្គង់ផ្សេងគ្នា។ ការចាត់តាំងដែលតម្រូវឲ្យមានអ្នកផ្គត់ផ្គង់ជាក់លាក់នឹងមានម៉ាកនេះនៅក្នុងឈ្មោះឯកសារ៖

- `aoai` - តម្រូវឲ្យមានចំណុចបញ្ចប់ Azure OpenAI និងគន្លង API
- `oai` - តម្រូវឲ្យមានចំណុចបញ្ចប់ OpenAI និងគន្លង API
- `hf` - តម្រូវឲ្យមានសញ្ញា Hugging Face
- `githubmodels` - តម្រូវឲ្យមានចំណុចបញ្ចប់ Microsoft Foundry Models និងគន្លង API (ម៉ូដែល GitHub នឹងផុតកំណត់នៅចុងខែកក្កដា ២០២៦)

អ្នកអាចកំណត់រចនាសម្ព័ន្ធបានមួយ មិនបានកំណត់ ឬទាំងអស់។ ការចាត់តាំងដែលទាក់ទងនឹងនឹងបង្ហាញកំហុសពេលវេលាដែលគន្លងសម្គាល់បាត់។

## បង្កើតឯកសារ `.env`

យើងសន្មត់ថាអ្នកបានអានណែនាំខាងលើរួចហើយ និងបានចុះឈ្មោះជាមួយអ្នកផ្គត់ផ្គង់ពាក់ព័ន្ធ ហើយបានទទួលសញ្ញាបត្រផ្ទៀងផ្ទាត់ដែលត្រូវការ (API_KEY ឬ token)។ នៅបរិបទ Azure OpenAI យើងសន្មត់ថាអ្នកក៏មានការតំឡើងបំរើ Azure OpenAI ដែលត្រឹមត្រូវ (ចំណុចបញ្ចប់) រួចហើយ ជាមួយម៉ូដែល GPT ឯកណាមួយសម្រាប់ការបញ្ចប់ការសន្ទនា។

ជំហ៊ានបន្ទាប់គឺការកំណត់រចនាសម្ព័ន្ធ **អថេរសាសន៍បរិយាកាសក្នុងម៉ាស៊ីនកុំព្យូទ័រផ្ទាល់** ដូចតទៅ៖

1. មើលក្នុងថតរ៉ូត ចំពោះឯកសារ `.env.copy` ដែលគួរតែមានមាតិកាដូចនេះ៖

   ```bash
   # អ្នកផ្ដល់សេវា OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI នៅ Microsoft Foundry
   ## (សេវា Azure OpenAI ឥឡូវនេះជាផ្នែកមួយនៃ Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # តម្លៃលំនាំដើមត្រូវបានកំណត់រួច! (កំណែ API GA ដែលមានស្ថិរភាពបច្ចុប្បន្ន)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## ម៉ូដែល Microsoft Foundry (ការសម្រុកម៉ូដែលអ្នកផ្ដល់សេវាច្រើនជំហាន ជំនួសម៉ូដែល GitHub ដែលនឹងបញ្ឈប់តែមេចុងខែកក្កដាឆ្នាំ 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. ចម្លងឯកសារនោះទៅជា `.env` ដោយប្រើពាក្យបញ្ជាខាងក្រោម។ ឯកសារនេះ _ត្រូវបាន gitignore_ ដើម្បីរក្សាសម្ងាត់ឲ្យបានសុវត្ថិភាព។

   ```bash
   cp .env.copy .env
   ```

3. បញ្ចូលតម្លៃ (ជំនួសទីដូចដែលមាននៅផ្នែកស្តាំក្រោមសញ្ញា `=`) ដូចបានពិពណ៌នានៅផ្នែកបន្ទាប់។

4. (ជម្រើស) ប្រសិនបើអ្នកប្រើ GitHub Codespaces អ្នកអាចរក្សាអថេរសាសន៍បរិយាកាសជា _Codespaces secrets_ ដែលភ្ជាប់ជាមួយឃ្លាំងនេះ។ គ្រាន់តែប៉ុន្នេះ អ្នកមិនចាំបាច់ត្រូវកំណត់ឯកសារ .env នៅក្នុងម៉ាស៊ីនផ្ទាល់ខ្លួនទេ។ **យ៉ាងណាមិញ សូមចំណាំថាជម្រើសនេះមានប្រសិទ្ធិភាពតែពេលអ្នកប្រើ GitHub Codespaces ប៉ុណ្ណោះ។** អ្នកត្រូវតែបង្កើតឯកសារ .env ប្រសិនបើប្រើ Docker Desktop ជំនួស។

## បំពេញឯកសារ `.env`

យើងមកមើលឈ្មោះអថេរដើម្បីយល់ថាវាតំណាងអ្វីបានខ្លះ៖

| អថេរ | សេចក្តីពិពណ៌នា |
| :--- | :--- |
| HUGGING_FACE_API_KEY | នេះជាសញ្ញាចូលប្រើដែលអ្នកកំណត់នៅក្នុងប្រវត្តិរូបរបស់អ្នក |
| OPENAI_API_KEY | នេះជាគន្លងអនុញ្ញាតសម្រាប់ប្រើសេវាកម្ម OpenAI លើអ្នកផ្គត់ផ្គង់ដែលមិនមែន Azure OpenAI |
| AZURE_OPENAI_API_KEY | នេះជាគន្លងអនុញ្ញាតសម្រាប់ប្រើសេវាកម្ម Azure OpenAI |
| AZURE_OPENAI_ENDPOINT | នេះជាចំណុចបញ្ចប់ដែលបានស្នាក់នៅសម្រាប់ធនធាន Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | នេះជាចំណុចបញ្ចប់សម្រាប់ការតំឡើងម៉ូដែល _ការបង្កើតអត្ថបទ_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | នេះជាចំណុចបញ្ចប់សម្រាប់ការតំឡើងម៉ូដែល _ធ្វើតួអង្គអត្ថបទ_ |
| AZURE_INFERENCE_ENDPOINT | នេះជាចំណុចបញ្ចប់សម្រាប់គម្រោង Microsoft Foundry របស់អ្នក ដែលប្រើសម្រាប់ម៉ូដែល Microsoft Foundry |
| AZURE_INFERENCE_CREDENTIAL | នេះជាគន្លង API សម្រាប់គម្រោង Microsoft Foundry របស់អ្នក |
| | |

សម្គាល់៖ អថេរពីរចុងក្រោយ Azure OpenAI បង្ហាញពីម៉ូដែលមូលដ្ឋានសម្រាប់ការបញ្ចប់ការសន្ទនា (ការបង្កើតអត្ថបទ) និងស្វែងរកតួអង្គ (ការធ្វើតួអង្គអត្ថបទ) តាមលំដាប់។ សេចក្តីណែនាំសម្រាប់កំណត់វាត្រូវបានកំណត់ក្នុងការចាត់តាំងពាក់ព័ន្ធ។

## កំណត់រចនាសម្ព័ន្ធ Azure OpenAI៖ ពីព្រលឹងបញ្ជាទិញ Portal

> **សម្គាល់៖** សេវាកម្ម Azure OpenAI កំពុងជាប់ជារូបរាង [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)។ ធនធាន និងការតំឡើងនៅតែបង្ហាញនៅក្នុង Azure Portal ប៉ុន្តែការគ្រប់គ្រងម៉ូដែលប្រចាំថ្ងៃ (ការតំឡើង, កន្លែងលេង, ត្រួតពិនិត្យ) ឥឡូវនេះធ្វើនៅក្នុងក្រៅផ្ទាំង Microsoft Foundry ជំនួសលើ "Azure OpenAI Studio" ដែលមានឡើយ។

តម្លៃចំណុចបញ្ចប់ និងគន្លង API របស់ Azure OpenAI អាចរកបាននៅក្នុង [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) ដូច្នេះយើងចាប់ផ្តើមនៅទីនោះ។

1. ទៅកាន់ [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. ចុចជម្រើស **គន្លងនិងចំណុចបញ្ចប់** នៅក្នុងចំហៀងម៉ឺនុយ (ម៉ឺនុយខាងឆ្វេង)។
1. ចុច **បង្ហាញគន្លង** - អ្នកគួរតែឃើញ៖ គន្លង 1, គន្លង 2 និងចំណុចបញ្ចប់។
1. ប្រើតម្លៃគន្លង 1 សម្រាប់ AZURE_OPENAI_API_KEY
1. ប្រើតម្លៃចំណុចបញ្ចប់សម្រាប់ AZURE_OPENAI_ENDPOINT

បន្ទាប់មក យើងត្រូវការចំណុចបញ្ចប់សម្រាប់ម៉ូដែលដែលបានតំឡើង។

1. ចុចជម្រើស **ការតំឡើងម៉ូដែល** នៅចំហៀងម៉ឺនុយ (ម៉ឺនុយខាងឆ្វេង) សម្រាប់ធនធាន Azure OpenAI។
1. នៅលើទំព័រទទួល ទៅកាន់ **Microsoft Foundry portal** (ឬ **គ្រប់គ្រងការតំឡើង**, អាស្រ័យលើប្រភេទធនធានរបស់អ្នក)

នេះនឹងនាំអ្នកទៅកាន់ Microsoft Foundry portal ដែលអ្នកនឹងស្វែងរកតម្លៃផ្សេងៗដូចបានពិពណ៌នាខាងក្រោម។

## កំណត់រចនាសម្ព័ន្ធ Azure OpenAI៖ ពី Microsoft Foundry portal

1. ទៅកាន់ [Microsoft Foundry portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **ពីធនធានរបស់អ្នក** ដូចបានអធិប្បាយខាងលើ។
1. ចុចផ្ទាំង**ការតំឡើង** (ចំហៀងម៉ឺនុយ) ដើម្បីមើលម៉ូដែលដែលបានតំឡើងបច្ចុប្បន្ន។
1. ប្រសិនបើម៉ូដែលដែលអ្នកចង់បានមិនទាន់តំឡើងទេ ប្រើ **តំឡើងម៉ូដែល** ដើម្បីដំឡើងវាពី [កាតាឡុកម៉ូដែល](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)។
1. អ្នកត្រូវការម៉ូដែល _ការបង្កើតអត្ថបទ_ - យើងណែនាំ៖ **gpt-5-mini**
1. អ្នកត្រូវការម៉ូដែល _ធ្វើតួអង្គអត្ថបទ_ - យើងណែនាំ **text-embedding-3-small**

ឥឡូវនេះ បន្ទាន់សម័យអថេរសាសន៍បរិយាកាស ដើម្បីបង្ហាញឈ្មោះ _ការតំឡើង_ ដែលបានប្រើ។ វាធម្មតានឹងដូចគ្នានឹងឈ្មោះម៉ូដែល លុះត្រាតែអ្នកបានផ្លាស់ប្តូរវាផ្ទាល់។ ដូចជាគំរូ អ្នកអាចមាន៖

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**កុំភ្លេចរក្សាទុកឯកសារ .env ពេលសម្រេចចិត្តហើយ**។ ឥឡូវនេះអ្នកអាចបញ្ចប់ការងារខាងក្នុងឯកសារ និងត្រឡប់ទៅនឹងការណែនាំដំណើរការកំណត់សៀវភៅ។

## កំណត់រចនាសម្ព័ន្ធ OpenAI៖ ពីប្រវត្តិរូប

គន្លង API OpenAI របស់អ្នកអាចរកបានក្នុង [គណនី OpenAI របស់អ្នក](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)។ ប្រសិនបើអ្នកមិនមានទេ អ្នកអាចចុះឈ្មោះក៏បង្កើតគន្លង API។ នៅពេលមានគន្លង រួច អ្នកអាចប្រើវាសម្រាប់បំពេញអថេរ `OPENAI_API_KEY` នៅឯកសារ `.env`។

## កំណត់រចនាសម្ព័ន្ធ Hugging Face៖ ពីប្រវត្តិរូប

សញ្ញា Hugging Face របស់អ្នកអាចរកបានក្នុងប្រវត្តិរូបនៅក្រោម [សញ្ញាចូលប្រើ](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst)។ កុំបង្ហោះឬចែករំលែកទូទៅ។ ត្រូវបង្កើតសញ្ញាថ្មីសម្រាប់ការប្រើប្រាស់គម្រោងនេះ ហើយចម្លងវាទៅក្នុងឯកសារ `.env` នៅក្រោមអថេរ `HUGGING_FACE_API_KEY`។ _សម្គាល់ៈ_ វាមានន័យបច្ចេកទេសមិនមែនជាគន្លង API តែក្នុងការផ្ទៀងផ្ទាត់ អ្នកយើងនៅតែរក្សាប្រើឈ្មោះនោះសម្រាប់ភាពស្របគ្នា។

## កំណត់រចនាសម្ព័ន្ធ Microsoft Foundry Models: ពី Portal

> **សម្គាល់ៈ** ម៉ូដែល GitHub នឹងផុតកំណត់នៅចុងខែកក្កដា ២០២៦។ ម៉ូដែល Microsoft Foundry គឺជារូបមន្តជំនួសផ្ទាល់ ដោយផ្តល់នូវកាតាឡុកម៉ូដែលដែលអាចសាកល្បងដោយឥតគិតថ្លៃ និងបទពិសោធន៍ SDK Azure AI Inference / OpenAI SDK ដូចមួយ។

1. ទៅកាន់ [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) និងបង្កើត (ឬបើក) គម្រោង Foundry ។
1. រុករក [កាតាឡុកម៉ូដែល](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ហើយតំឡើងម៉ូដែល មួយដូចជា `gpt-5-mini` ។
1. នៅលើទំព័រពិពណ៌នាគម្រោង, ចម្លង **ចំណុចបញ្ចប់** និង **គន្លង API** ។
1. ប្រើតម្លៃចំណុចបញ្ចប់សម្រាប់ `AZURE_INFERENCE_ENDPOINT` និងតម្លៃគន្លងសម្រាប់ `AZURE_INFERENCE_CREDENTIAL` នៅក្នុងឯកសារ `.env` របស់អ្នក។

## អ្នកផ្គត់ផ្គង់ក្រៅបណ្តាញ / ផ្ទាល់ខ្លួន

ប្រសិនបើអ្នកមិនចង់ប្រើការជាវសេវាមេឃទេ អ្នកអាចដំណើរការម៉ូដែលបើកប្រភពត្រូវគ្នាជាផ្ទាល់លើឧបករណ៍របស់អ្នក៖

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - រត់នៅលើឧបករណ៍ Microsoft អ្នកប្រើប្រាស់។ វាជ្រើសរើសអ្នកផ្គត់ផ្គង់ដំណើរការល្អបំផុត (NPU, GPU, ឬ CPU) ដោយស្វ័យប្រវត្តិ ហើយបង្ហាញចំណុចបញ្ចប់ដែលសមរម្យនឹង OpenAI ដូច្នេះអ្នកអាចប្រើកូដគំរូភាគច្រើនក្នុងវគ្គនេះដោយការផ្លាស់ប្តូរតិចបំផុត។ មើលឯកសារនៃ [Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) ដើម្បីចាប់ផ្តើម ឬដំឡើងជាមួយ `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS) ។
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - ជាជម្រើសពេញនិយមក្នុងការប្រើម៉ូដែលបើកប្រភពដូចជា Llama, Phi, Mistral និង Gemma ជាផ្ទាល់។


សូមមើល [មេរៀនទី 19៖ ការសង់ជាមួយ SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) សម្រាប់ឧទាហរណ៍ជាក់ស្តែងដែលប្រើទាំងពីរជម្រើស។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->