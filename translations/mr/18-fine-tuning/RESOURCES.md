# स्व-संचालित शिक्षणासाठी संसाधने

धडा OpenAI आणि Microsoft Foundry मधील कोअर संसाधनांचा वापर करून तयार केला गेला आहे, ज्यात संज्ञापन आणि Tutorials साठी संदर्भ म्हणून वापरले गेले आहे. स्व-संचालित शिक्षण यात्रांसाठी येथे आपल्यासाठी एक संपूर्ण नसलेली यादी आहे. खालील प्रत्येक दुवा सद्यस्थितीत समर्थित सामग्रीकडे निर्देशित करतो.

## 1. प्राथमिक संसाधने

| शीर्षक/दुवा | वर्णन |
| :--- | :--- |
| [OpenAI मॉडेलसह फाइन-ट्युनिंग](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | फाइन-ट्युनिंग फ्यू-शॉट लर्निंगच्या सुधारणा करते जे प्रॉम्प्टमध्ये बसतील त्या पेक्षा खूप अधिक उदाहरणांवर प्रशिक्षण देऊन - खर्च बचत करते, प्रतिसाद गुणवत्तेत सुधारणा करते आणि कमी विलंबित विनंत्या सक्षम करतो. **OpenAI कडून फाइन-ट्युनिंगचं अवलोकन मिळवा.** |
| [Microsoft Foundry फाइन-ट्युनिंग केव्हा वापरायचं](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | समजून घ्या **फाइन-ट्युनिंग म्हणजे काय (संकल्पना)**, का विचार करावा, कोणता डेटा वापरायचा, आणि गुणवत्ता कशी मोजायची - शिवाय SFT, DPO, किंवा RFT कधी योग्य आहे. |
| [फाइन-ट्युनिंगसह मॉडेल कस्टमाइज करा](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | Microsoft Foundry मध्ये पोर्टल, OpenAI / Foundry Python SDK किंवा REST API वापरून फाइन-ट्युनिंग चे संपूर्ण **कसे करायचे (प्रक्रिया)** - डेटा तयारी, प्रशिक्षण, चेकपॉइंट्स आणि डिप्लॉयमेंट कव्हर करते. |
| [सतत फाइन-ट्युनिंग](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | आधीच फाइन-ट्यून केलेल्या मॉडेलला बेस मॉडेल म्हणून निवडण्याची आणि नवीन प्रशिक्षण उदाहरणांच्या संचावर **पुढे फाइन-ट्युनिंग करण्याची** पुनरावृत्ती प्रक्रिया. |
| [टूल (फंक्शन) कॉलिंगसह फाइन-ट्युनिंग](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | टूल-कॉलिंग उदाहरणांसह मॉडेलचे फाइन-ट्युनिंग केल्याने आउटपुट सुधारते - अधिक अचूक, सुसंगत, समान पद्धतीने फॉरमॅट केलेले प्रतिसाद कमी प्रॉम्प्ट टोकन्स वापरून. |
| [फाइन-ट्युनिंग मॉडेल: Microsoft Foundry मार्गदर्शन](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | पाहा **कोणते मॉडेल्स फाइन-ट्यून केले जाऊ शकतात**, त्याच्या समर्थीत पद्धती (SFT / DPO / RFT), आणि उपलब्ध असलेल्या प्रदेशांची माहिती. |
| [फाइन-ट्युनिंग आढावा: तंत्रे आणि प्रकार](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | तीन प्रशिक्षण तंत्र (SFT, DPO, RFT) आणि दोन प्रकार (सर्व्हरलेस विरुद्ध व्यवस्थापित संगणन) यांची तुलना करा, बेस मॉडेल निवडणे आणि प्रारंभ करण्याबाबत मार्गदर्शन करा. |
| **Tutorial**: [Microsoft Foundry मध्ये मॉडेल फाइन-ट्यून करा](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | एक नमुना डेटासेट तयार करा, फाइन-ट्युनिंगसाठी तयारी करा, सध्याच्या समर्थित मॉडेलवर (जसे `gpt-4.1-mini`) फाइन-ट्युनिंग जॉब चालवा, आणि फाइन-ट्यून केलेले मॉडेल Azure वर डिप्लॉय करा. |
| **Tutorial**: [सर्व्हरलेस API डिप्लॉयमेंटसह मॉडेल्स फाइन-ट्यून करा](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | आपले डेटासेटसाठी खुले आणि भागीदार मॉडेल (Phi, Llama, Mistral, आणि अधिक) Microsoft Foundry मध्ये _लो-कोड, UI-आधारित कार्यप्रवाह वापरून_ सानुकूल करा. |
| **Tutorial**: [Azure Databricks वर Hugging Face मॉडेल्स फाइन-ट्यून करा](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | Azure Databricks आणि Hugging Face Trainer वापरून `transformers` लायब्ररीसह एक GPU वर Hugging Face मॉडेल फाइन-ट्यून करा. |
| **Training**: [Azure Machine Learning सह फाउंडेशन मॉडेल फाइन-ट्यून करा](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Azure Machine Learning मॉडेल कॅटलॉगमध्ये अनेक ओपन-सोर्स मॉडेल्स उपलब्ध आहेत जे आपण फाइन-ट्यून करू शकता. [Azure ML Generative AI Learning Path](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) चा भाग. |
| **Tutorial**: [Weights & Biases सह Azure OpenAI फाइन-ट्युनिंग](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | W&B सह Azure वर फाइन-ट्युनिंग रन ट्रॅक आणि विश्लेषण करा. OpenAI फाइन-ट्युनिंग मार्गदर्शनास Azure-विशिष्ट चरणे आणि प्रयोग ट्रॅकिंगसह विस्तार देते. |

## 2. द्वितीयक संसाधने

हा विभाग त्याविषयी आपला स्वतःचा कौशल्य विकसित करण्यासाठी अभ्यास करण्याजोग्या अतिरिक्त संसाधनांना झळकवितो ज्यावर आपल्याला धड्यात वेळ नव्हता. त्यांचा वापर करून या विषयावर आपली स्वतःची कौशल्ये तयार करा.

| शीर्षक/दुवा | वर्णन |
| :--- | :--- |
| **OpenAI Cookbook**: [चॅट मॉडेल फाइन-ट्युनिंगसाठी डेटा तयारी आणि विश्लेषण](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | फाइन-ट्युनिंगपूर्वी चॅट डेटासेटचे पूर्वप्रक्रियाकरण आणि विश्लेषण करा: फॉरमॅट त्रुटी तपासा, मूलभूत आकडेवारी मिळवा, आणि टोकन मोजणीचा (आणि खर्चाचा) अंदाज लावा. [OpenAI फाइन-ट्युनिंग मार्गदर्शन](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) सह जोडलेले आहे. |
| **OpenAI Cookbook**: [Qdrant सह Retrieval Augmented Generation (RAG) साठी फाइन-ट्युनिंग](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | RAG साठी OpenAI मॉडेल्सचे सखोल फाइन-ट्युनिंगचे उदाहरण, ज्यात Qdrant समाकलित करून फ्यू-शॉट लर्निंग वापरून कार्यप्रदर्शन वाढवले आणि भासकांश कमी केले. |
| **OpenAI Cookbook**: [Weights & Biases सह GPT फाइन-ट्युनिंग](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | मॉडेल प्रशिक्षण आणि फाइन-ट्युनिंगसाठी W&B वापरा. प्रथम त्यांचा [OpenAI Fine-Tuning](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst) मार्गदर्शक वाचा, नंतर Cookbook उदाहरणाचा प्रयत्न करा. |
| **Hugging Face Tutorial**: [Hugging Face TRL सह LLMs कसे फाइन-ट्यून करायचे](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | Hugging Face TRL, Transformers, आणि डेटासेट्स वापरून खुले LLMs फाइन-ट्यून करा: वापर प्रकरण ठरवा, विकास वातावरण तयार करा, डेटासेट तयार करा, फाइन-ट्युन करा, मूल्यांकन करा, आणि डिप्लॉय करा. |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | Hugging Face कडून अनेक मॉडेल प्रकारांचे फाइन-ट्युनिंग करण्यासाठी नो-कोड / लो-कोड लायब्ररी. आपल्या स्वतःच्या क्लाउडवर, Hugging Face Spaces वर, किंवा स्थानिक GUI, CLI, किंवा YAML कॉन्फिग वापरून चालवा. |
| **Unsloth**: [LLMs फाइन-ट्युनिंग मार्गदर्शक](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | स्थानिक LLM फाइन-ट्युनिंग आणि पुनर्बलन शिकवणीसाठी एक ओपन-सोर्स फ्रेमवर्क, तयार-करण्यासाठी वापरण्यायोग्य [नोटबुक्स](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) सह. |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->