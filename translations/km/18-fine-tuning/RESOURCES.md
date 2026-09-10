# ឧបករណ៍សម្រាប់រៀនដោយខ្លួនឯង

មេរៀននេះត្រូវបានបង្កើតឡើងដោយប្រើឧបករណ៍មូលដ្ឋានពី OpenAI និង Microsoft Foundry ជាការយោងសម្រាប់ពាក្យបច្ចេកទេស និងមេរៀន។ នេះគឺជាបញ្ជីមិនពេញលេញសម្រាប់ការរៀនដោយខ្លួនឯងរបស់អ្នក។ តំណភ្ជាប់ទាំងអស់ខាងក្រោមបញ្ជូនទៅឯកសារដែលទាន់សម័យ និងគាំទ្រ។

## 1. ឧបករណ៍មូលដ្ឋាន

| ចំណងជើង/តំណ | ការពិពណ៌នា |
| :--- | :--- |
| [ការបំប៉នលំដាប់ជាមួយគំរូ OpenAI](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | ការបំប៉នលំដាប់ធ្វើឱ្យការសិក្សា few-shot កាន់តែប្រសើរឡើងដោយហ្វឹកហ្វឺនលើឧទាហរណ៍ជាច្រេីនជាងអាចដាក់ក្នុង prompt - រក្សារចំណាយ បង្កើនគុណភាពចម្លើយ និងអាចធ្វើសំណើមានពេលវេលาตอบតិច។ **ទទួលបានមូលដ្ឋានចំពោះការបំប៉នលំដាប់ពី OpenAI។** |
| [ពេលណាដែលត្រូវប្រើការបំប៉នលំដាប់ Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | យល់ដឹងពី **អ្វីទៅជាការបំប៉នលំដាប់ (យោបល់)**, ហេតុអ្វីអ្នកគួរពិចារណា វត្ថុទិន្នន័យណាដែលត្រូវប្រើ, និងវិធីវាស់តម្លៃគុណភាព - ព្រមទាំងពេលណាដែល SFT, DPO, ឬ RFT គឺសមរម្យ។ |
| [ប្ដូរគំរូជាមួយការបំប៉នលំដាប់](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | ជំហ៊ានពីដើមដល់ចប់ **វិធី (ដំណើរការ)** សម្រាប់ការបំប៉នលំដាប់នៅ Microsoft Foundry ដោយប្រើទីផ្សារ OpenAI / Foundry Python SDK ឬ REST API - រួមមានការរៀបចំទិន្នន័យ ការបណ្តុះបណ្តាល ការចតុកោណ និងការដាក់ចេញ។ |
| [ការបំប៉នលំដាប់ជាបន្ត](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | ដំណើរការដ៏ស្ទាត់ដោយជ្រើសរើសគំរូដែលបានបំប៉នលំដាប់រួចមកជាគំរូមូលដ្ឋាន និង **បន្តបំប៉នលំដាប់វា** លើកំណត់ឧទាហរណ៍ការបណ្តុះបណ្តាលថ្មីៗ។ |
| [បំប៉នលំដាប់ជាមួយការហៅឧបករណ៍ (function)](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | បំប៉នលំដាប់គំរូរបស់អ្នក **ជាមួយឧទាហរណ៍ហៅឧបករណ៍** ធ្វើឱ្យ លទ្ធផលប្រសើរឡើង - មានភាពត្រឹមត្រូវ ជាប់លាប់ និងមានទ្រង់ទ្រាយស្រដៀងគ្នា ដោយប្រើ token prompt ច្រើនតិច។ |
| [ការបំប៉នលំដាប់គំរូ៖ ការណែនាំ Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | សូមមើល **គំរូណាខ្លះអាចបំប៉នលំដាប់បាន** វិធីសាស្រ្តដែលគាំទ្រ (SFT / DPO / RFT) និងតំបន់ដែលមានសេវាកម្មនេះ។ |
| [ទិដ្ឋភាពទូទៅបំផុត៖ បច្ចេកទេស និងរបៀបប្រើ](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | ប្រើប្រាស់ការបង្វឹកបីប្រភេទ (SFT, DPO, RFT) និងរបៀបពីរ (serverless និងគណនាគ្រប់គ្រង), មានការណែនាំរកគំរូមូលដ្ឋាន និងចាប់ផ្តើមការងារ។ |
| **មេរៀន**: [បំប៉នលំដាប់គំរូនៅ Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | បង្កើតឧទាហរណ៍ទិន្នន័យ ត្រៀមសរសេរការបំប៉នលំដាប់ ដំណើរការងារបំប៉នលំដាប់លើគំរូទំនើប `gpt-4.1-mini` និងដាក់ចេញគំរូបំប៉នលំដាប់លើ Azure។ |
| **មេរៀន**: [បំប៉នលំដាប់គំរូជាមួយការដាក់ចេញ API សេវាសេវា](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | ប្ដូរគំរូបើកចំហ និងគំរូដៃគូ (Phi, Llama, Mistral និងផ្សេងៗ) ជាមួយទិន្នន័យរបស់អ្នក _ដោយប្រើវគ្គ UI ចុចតិច ដំណើរការលោកខូដ_ ក្នុង Microsoft Foundry។ |
| **មេរៀន**: [បំប៉នលំដាប់គំរូ Hugging Face នៅ Azure Databricks](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | បំប៉នលំដាប់គំរូ Hugging Face ជាមួយបណ្ណាល័យ `transformers` លើ GPU តែមួយដោយប្រើ Azure Databricks និង Hugging Face Trainer។ |
| **កិច្ចបណ្តុះបណ្តាល**: [បំប៉នលំដាប់គំរូមូលដ្ឋានជាមួយ Azure Machine Learning](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | កាតាឡុកគំរូ Azure Machine Learning ផ្តល់ជាគំរូបើកចំហជាច្រើនដែលអ្នកអាចបំប៉នលំដាប់បាន។ ជាផ្នែកនៃ [ផ្លូវរៀន Azure ML Generative AI](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst)។ |
| **មេរៀន**: [ការបំប៉នលំដាប់ Azure OpenAI ជាមួយ Weights & Biases](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | តាមដាន និងវិភាគការរត់បំប៉នលំដាប់នៅ Azure ជាមួយ W&B។ បន្ថែមមគ្គុទេសក៏ OpenAI fine-tuning ដោយបន្ថែមជំហាន និងការតាមដានការសាកល្បងជាក់លាក់របស់ Azure។ |

## 2. ឧបករណ៍រង

ផ្នែកនេះផ្ទុកឧបករណ៍បន្ថែមល្អដែលគួររំពឹងមើលមើលតែពុំទាន់បានពិភាក្សានៅក្នុងមេរៀន។ ប្រើវាដើម្បីបង្កើតជំនាញរបស់អ្នកផ្ទាល់ខ្លួននៅលើប្រធានបទនេះ។

| ចំណងជើង/តំណ | ការពិពណ៌នា |
| :--- | :--- |
| **សៀវភៅម្ហូប OpenAI**: [ការរៀបចំទិន្នន័យ និងវិភាគសម្រាប់បំប៉នលំដាប់ម៉ូដែល chat](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | រៀបចំ និងវិភាគឧទាហរណ៍chat មួយ មុនពេលបំប៉នលំដាប់៖ ពិនិត្យកំហុសទ្រង់ទ្រាយ ទទួលបានស្ថិតិមូលដ្ឋាន និងប៉ាន់ប្រមាណចំនួន token (និងការចំណាយ)។ ចំណងជាមួយ [មគ្គុទេសក៏ OpenAI fine-tuning](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst)។ |
| **សៀវភៅម្ហូប OpenAI**: [ការបំប៉នសម្រាប់ការបង្កើតបន្ថែមដោយការទាញយក (RAG) ជាមួយ Qdrant](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | ឧទាហរណ៍ពេញលេញនៃការបំប៉នលំដាប់ម៉ូដែល OpenAI សម្រាប់ RAG, រួមបញ្ចូល Qdrant និងការសិក្សា few-shot ដើម្បីបង្កើនសមត្ថភាព និងកាត់បន្ថយការបរិច្ឆេទខុស។ |
| **សៀវភៅម្ហូប OpenAI**: [បំប៉ន GPT ជាមួយ Weights & Biases](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | ប្រើ W&B ដើម្បីតាមដានការបណ្តុះបណ្តាលម៉ូដែល និងការបំប៉នលំដាប់។ អានមគ្គុទេសក៏ [OpenAI Fine-Tuning](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst) ជាមុន បន្ទាប់មកសាកល្បងលំហាត់សៀវភៅម្ហូប។ |
| **មេរៀន Hugging Face**: [របៀបបំប៉ន LLMs ជាមួយ Hugging Face TRL](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | បំប៉ន LLMs បើកចំហដោយប្រើ Hugging Face TRL, Transformers និងឧទាហរណ៍ទិន្នន័យ៖ កំណត់ករណីប្រើប្រាស់, តំឡើងបរិយាកាសអភិវឌ្ឍ, រៀបចំឧទាហរណ៍ទិន្នន័យ, បំប៉នលំដាប់, វាយតម្លៃ និងដាក់ចេញ។ |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | បណ្ណាល័យគ្មានកូដ / កូដតិចពី Hugging Face សម្រាប់បំប៉នលំដាប់ម៉ូដែលប្រភេទជាច្រើន។ ប្រើវានៅភ័ព្វខ្សែភ្លើងរបស់អ្នក ឬនៅលើ Hugging Face Spaces រឺក្នុងលokalតាម GUI, CLI ឬកំណត់ค่า YAML។ |
| **Unsloth**: [មគ្គុទេសក៏បំប៉នលំដាប់ LLMs](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | ស៊ុមប្រភពបើក ដែលសម្រួលការបំប៉នលំដាប់ LLMs ក្នុងតំបន់ និងការរៀនបង្វឹកជំនួយ, មាន [ភ្ជាប់សៀវភៅកត់ត្រា](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) ដែលរួចទៅហើយ។ |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->