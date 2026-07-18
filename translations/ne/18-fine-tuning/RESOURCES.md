# आत्मनिर्देशित सिकाइका लागि स्रोतहरू

पाठ OpenAI र Microsoft Foundry का मुख्य स्रोतहरूलाई सन्दर्भका रूपमा प्रयोग गरी बनाइएको थियो जसले शब्दावली र ट्युटोरियलहरू समेट्छ। यहाँ तपाईंको आफ्नै आत्मनिर्देशित सिकाइ यात्राका लागि एउटा अप्रतिबद्ध सूची छ। तलका प्रत्येक लिंक वर्तमान, समर्थित सामग्रीलाई संकेत गर्दछ।

## १. प्राथमिक स्रोतहरू

| शीर्षक/लिंक | विवरण |
| :--- | :--- |
| [OpenAI मोडेलहरू सँग फाइन-ट्यूनिङ](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | फाइन-ट्यूनिङले कम उदाहरणहरूमा आधारित फ्यु-शट सिकाइभन्दा धेरै उदाहरणहरूमा प्रशिक्षण गरेर सुधार गर्छ - लागत बचत, प्रतिक्रिया गुणस्तर सुधार, र कम-लेटेन्सी अनुरोधहरू सक्षम पार्दै। **OpenAI बाट फाइन-ट्यूनिङको एक सिंहावलोकन प्राप्त गर्नुहोस्।** |
| [Microsoft Foundry फाइन-ट्यूनिङ कहिले प्रयोग गर्ने](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | बुझ्नुहोस् **फाइन-ट्यूनिङ के हो (सिद्धान्त)**, किन तपाईंले विचार गर्नुपर्नेछ, कुन डाटा प्रयोग गर्ने, र गुणस्तर कसरी मापन गर्ने - साथै SFT, DPO, वा RFT कहिले उपयुक्त हुन्छ। |
| [फाइन-ट्यूनिङ गरेर मोडेल अनुकूलन गर्नुहोस्](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | Microsoft Foundry मा पोर्टल, OpenAI / Foundry Python SDK, वा REST API प्रयोग गरी फाइन-ट्यूनिङको अन्त्य-देखि-अन्त प्रक्रिया - डाटा तयारी, प्रशिक्षण, checkpoints, र तैनाती समेटिएको। |
| [लगातार फाइन-ट्यूनिङ](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | पहिले नै फाइन-ट्यून गरिएको मोडेललाई आधार मोडेलको रूपमा चयन गरी नयाँ प्रशिक्षण उदाहरणहरूको सेटहरूमा **अझै फाइन-ट्यूनिङ गर्ने** पुनरावृत्ति प्रक्रिया। |
| [उपकरण (कार्य) कलिङसँग फाइन-ट्यूनिङ](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | उपकरण-कलिङ उदाहरणहरू सहित आफ्नो मोडेललाई फाइन-ट्यूनिङ गर्दा उत्पादन सुधार हुन्छ - कम प्रॉम्प्ट टोकनहरू प्रयोग गरेर बढी सही, सुसंगत, र समान रूपमा स्वरूप गरिएको प्रतिक्रिया। |
| [फाइन-ट्यूनिङ मोडेलहरू: Microsoft Foundry दिशानिर्देशन](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | **कसरी मोडेलहरू फाइन-ट्यून गर्न सकिन्छ**, तिनीहरूले समर्थन गर्ने विधिहरू (SFT / DPO / RFT), र उपलब्ध क्षेत्रहरूको बारेमा जानकारी लिनुहोस्। |
| [फाइन-ट्यूनिङ सिंहावलोकन: प्रविधिहरू र मोडालिटीहरू](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | तीन प्रशिक्षण प्रविधिहरू (SFT, DPO, RFT) र दुई मोडालिटीहरू (सर्भरलेस बनाम व्यवस्थापन गरिएको कम्प्युट) तुलना गर्नुहोस्, आधार मोडेल छनौट र प्रारम्भ गर्ने मार्गदर्शन सहित। |
| **ट्युटोरियल**: [Microsoft Foundry मा मोडेल फाइन-ट्यून गर्नुहोस्](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | एउटा नमूना डेटासेट सिर्जना गर्नुहोस्, फाइन-ट्यूनिङको तयारी गर्नुहोस्, हाल समर्थित मोडेल जस्तै `gpt-4.1-mini` मा फाइन-ट्यूनिङ कार्य चलाउनुहोस्, र Azure मा फाइन-ट्यून गरिएको मोडेल तैनाथ गर्नुहोस्। |
| **ट्युटोरियल**: [सर्भरलेस API तैनातीहरूसँग मोडेल फाइन-ट्यून गर्नुहोस्](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | Microsoft Foundry मा कम-कोड, UI-आधारित कार्यप्रवाह प्रयोग गरी आफ्नो डेटासेटमा खुला र साझेदार मोडेलहरू (Phi, Llama, Mistral, र थप) अनुकूलित गर्नुहोस्। |
| **ट्युटोरियल**: [Azure Databricks मा Hugging Face मोडेलहरू फाइन-ट्यून गर्नुहोस्](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | Azure Databricks र Hugging Face Trainer प्रयोग गरी `transformers` पुस्तकालयका साथ एकल GPU मा Hugging Face मोडेल फाइन-ट्यून गर्नुहोस्। |
| **प्रशिक्षण**: [Azure Machine Learning सँग आधार मोडेल फाइन-ट्यून गर्नुहोस्](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Azure Machine Learning मोडेल क्याटलगले तपाईंलाई थुप्रै खुला-स्रोत मोडेलहरू फाइन-ट्यून गर्न अनुमति दिन्छ। [Azure ML Generative AI Learning Path](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) को भाग। |
| **ट्युटोरियल**: [Weights & Biases सँग Azure OpenAI फाइन-ट्यूनिङ](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | Azure मा W&B सँग फाइन-ट्यूनिङ रनहरू ट्र्याक र विश्लेषण गर्नुहोस्। OpenAI फाइन-ट्यूनिङ मार्गदर्शनलाई Azure-विशिष्ट चरणहरू र प्रयोग ट्र्याकिङ संग विस्तार गर्दछ। |

## २. दोस्रो स्रोतहरू

यो खण्डले थप स्रोतहरू समेट्छ जुन हामी पाठमा समेट्न समय पाइनौं। यसलाई यस विषयमा तपाईँको विशेषज्ञता विकास गर्न प्रयोग गर्नुहोस्।

| शीर्षक/लिंक | विवरण |
| :--- | :--- |
| **OpenAI कुकबुक**: [च्याट मोडेल फाइन-ट्यूनिङका लागि डाटा तयारी र विश्लेषण](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | फाइन-ट्यूनिङ अघि च्याट dataset लाई पूर्वप्रक्रिया र विश्लेषण गर्नुहोस्: ढाँचा त्रुटिहरू जाँच गर्नुहोस्, आधारभूत तथ्याङ्क प्राप्त गर्नुहोस्, र टोकन गणना (र लागत) अनुमान लगाउनुहोस्। [OpenAI फाइन-ट्युनिङ मार्गदर्शन](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) सँग जोडिएको। |
| **OpenAI कुकबुक**: [Retrieval Augmented Generation (RAG) को लागि Qdrant सँग फाइन-ट्यूनिङ](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | RAG का लागि OpenAI मोडेलहरूको फाइन-ट्यूनिङको व्यापक उदाहरण, Qdrant र झन्डै-शट सिकाइ एकीकरण गरेर प्रदर्शन बढाउने र फेब्रिकेसनहरू घटाउने। |
| **OpenAI कुकबुक**: [Weights & Biases सँग GPT फाइन-ट्यूनिङ](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | मोडेल प्रशिक्षण र फाइन-ट्यूनिङ ट्र्याक गर्न W&B प्रयोग गर्नुहोस्। पहिला तिनीहरूको [OpenAI फाइन-ट्यूनिङ](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst) मार्गदर्शन पढ्नुहोस्, अनि कुकबुक अभ्यास प्रयास गर्नुहोस्। |
| **Hugging Face ट्युटोरियल**: [Hugging Face TRL सँग LLMs कसरी फाइन-ट्यून गर्ने](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | Hugging Face TRL, Transformers, र datasets प्रयोग गरी खुला LLMs फाइन-ट्यून गर्नुहोस्: प्रयोग केस परिभाषित गर्नुहोस्, विकास वातावरण सेट अप गर्नुहोस्, डेटासेट तयार गर्नुहोस्, फाइन-ट्युनिङ, मूल्याङ्कन, र तैनाथ। |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | Hugging Face बाट कुनै-कोड / कम-कोड पुस्तकालय जसले धेरै मोडेल प्रकारहरूलाई फाइन-ट्यून गर्ने सुविधा दिन्छ। यो तपाईंको आफ्नै क्लाउड, Hugging Face Spaces, वा GUI, CLI, वा YAML कन्फिग मार्फत स्थानीय रूपमा चलाउन सकिन्छ। |
| **Unsloth**: [LLMs फाइन-ट्यूनिङ मार्गदर्शन](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | स्थानीय LLM फाइन-ट्यूनिङ र सुदृढ सिकाइलाई सजीव बनाउने खुला-श्रोत फ्रेमवर्क, तयार [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) सहित। |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->