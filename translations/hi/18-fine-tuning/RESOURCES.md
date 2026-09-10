# स्व-निर्देशित सीखने के लिए संसाधन

पाठ OpenAI और Microsoft Foundry के कोर संसाधनों का उपयोग करते हुए टर्मिनोलॉजी और ट्यूटोरियल के संदर्भ के रूप में बनाया गया था। यहाँ आपके अपने स्व-निर्देशित सीखने की यात्राओं के लिए एक असंपूर्ण सूची दी गई है। नीचे हर लिंक वर्तमान, समर्थित सामग्री की ओर इंगित करता है।

## 1. प्राथमिक संसाधन

| शीर्षक/लिंक | विवरण |
| :--- | :--- |
| [OpenAI मॉडल के साथ फाइन-ट्यूनिंग](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | फाइन-ट्यूनिंग फ्यू-शॉट लर्निंग को बेहतर बनाता है कई अधिक उदाहरणों पर प्रशिक्षण देकर जो प्रॉम्प्ट में फिट हो सकते हैं – लागत बचाता है, प्रतिक्रिया गुणवत्ता सुधारता है, और कम विलंबता अनुरोध सक्षम करता है। **OpenAI से फाइन-ट्यूनिंग का अवलोकन प्राप्त करें।** |
| [Microsoft Foundry फाइन-ट्यूनिंग कब उपयोग करें](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | समझें **फाइन-ट्यूनिंग क्या है (धारणा)**, क्यों आपको इसे विचार करना चाहिए, कौन सा डेटा उपयोग करना है, और गुणवत्ता कैसे मापें - साथ ही कब SFT, DPO, या RFT उपयुक्त है। |
| [फाइन-ट्यूनिंग के साथ मॉडल को अनुकूलित करें](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | Microsoft Foundry में पोर्टल, OpenAI / Foundry Python SDK, या REST API का उपयोग करते हुए फाइन-ट्यूनिंग के लिए एंड-टू-एंड **कैसे करें (प्रक्रिया)** - डेटा तैयारी, प्रशिक्षण, चेकपॉइंट्स, और डिप्लॉयमेंट को कवर करता है। |
| [निरंतर फाइन-ट्यूनिंग](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | एक पहले से फाइन-ट्यून किए गए मॉडल को बेस मॉडल के रूप में चुनने और नए प्रशिक्षण उदाहरणों के सेट पर इसे **आगे फाइन-ट्यून करने** की पुनरावृत्तिमूलक प्रक्रिया। |
| [उपकरण (फंक्शन) कॉलिंग के साथ फाइन-ट्यूनिंग](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | अपने मॉडल को **उपकरण-कॉलिंग उदाहरणों के साथ फाइन-ट्यूनिंग** करना आउटपुट को बेहतर बनाता है - अधिक सटीक, सुसंगत, समान रूप से स्वरूपित प्रतिक्रियाएं कम प्रॉम्प्ट टोकन का उपयोग करते हुए। |
| [फाइन-ट्यूनिंग मॉडल: Microsoft Foundry मार्गदर्शन](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | खोजें **कौन से मॉडल फाइन-ट्यून किए जा सकते हैं**, वे कौन से तरीके समर्थन करते हैं (SFT / DPO / RFT), और वे किन क्षेत्रों में उपलब्ध हैं। |
| [फाइन-ट्यूनिंग अवलोकन: तकनीकें और प्रकार](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | तीन प्रशिक्षण तकनीकों (SFT, DPO, RFT) और दो प्रकारों (सर्वरलेस बनाम प्रबंधित कंप्यूट) की तुलना करें, साथ ही एक बेस मॉडल चुनने और शुरू करने के लिए मार्गदर्शन। |
| **ट्यूटोरियल**: [Microsoft Foundry में एक मॉडल फाइन-ट्यून करें](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | एक नमूना डेटासेट बनाएं, फाइन-ट्यूनिंग के लिए तैयार करें, वर्तमान समर्थित मॉडल जैसे `gpt-4.1-mini` पर फाइन-ट्यूनिंग जॉब चलाएं, और Azure पर फाइन-ट्यून किया गया मॉडल डिप्लॉय करें। |
| **ट्यूटोरियल**: [सर्वरलेस API डिप्लॉयमेंट के साथ मॉडल फाइन-ट्यून करें](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | Microsoft Foundry में एक कम-कोड, UI-आधारित वर्कफ़्लो का उपयोग करके अपने डेटासेट के लिए खुले और भागीदार मॉडल (Phi, Llama, Mistral, और अन्य) को अनुकूलित करें। |
| **ट्यूटोरियल**: [Azure Databricks पर Hugging Face मॉडल फाइन-ट्यून करें](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | `transformers` लाइब्रेरी का उपयोग करके एक सिंगल GPU पर Azure Databricks और Hugging Face Trainer के साथ एक Hugging Face मॉडल को फाइन-ट्यून करें। |
| **प्रशिक्षण**: [Azure Machine Learning के साथ एक फाउंडेशन मॉडल फाइन-ट्यून करें](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Azure Machine Learning मॉडल कैटलॉग कई ओपन-सोर्स मॉडल प्रदान करता है जिन्हें आप फाइन-ट्यून कर सकते हैं। यह [Azure ML Generative AI लर्निंग पाथ](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) का भाग है। |
| **ट्यूटोरियल**: [Weights & Biases के साथ Azure OpenAI फाइन-ट्यूनिंग](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | W&B के साथ Azure पर फाइन-ट्यूनिंग रन ट्रैक और विश्लेषण करें। OpenAI फाइन-ट्यूनिंग गाइड को Azure-विशिष्ट चरणों और प्रयोग ट्रैकिंग के साथ विस्तारित करता है। |

## 2. द्वितीयक संसाधन

यह अनुभाग अतिरिक्त संसाधनों को संजोता है जिन्हें तलाशने लायक है जिन्हें हमने पाठ में कवर करने का समय नहीं पाया। इनका उपयोग इस विषय के आसपास अपनी विशेषज्ञता बनाने के लिए करें।

| शीर्षक/लिंक | विवरण |
| :--- | :--- |
| **OpenAI कुकबुक**: [चैट मॉडल फाइन-ट्यूनिंग के लिए डेटा तैयारी और विश्लेषण](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | फाइन-ट्यूनिंग से पहले चैट डेटासेट को पूर्व-संसाधित और विश्लेषण करें: फॉर्मेट त्रुटियों की जांच करें, बुनियादी सांख्यिकी प्राप्त करें, और टोकन गणना (और लागत) का अनुमान लगाएं। [OpenAI फाइन-ट्यूनिंग गाइड](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) के साथ युग्मित। |
| **OpenAI कुकबुक**: [Retrieval Augmented Generation (RAG) के लिए Qdrant के साथ फाइन-ट्यूनिंग](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | RAG के लिए OpenAI मॉडल की फाइन-ट्यूनिंग का एक व्यापक उदाहरण, Qdrant और फ्यू-शॉट लर्निंग को एकीकृत करता है प्रदर्शन बढ़ाने और काल्पनिकताओं को कम करने के लिए। |
| **OpenAI कुकबुक**: [Weights & Biases के साथ GPT फाइन-ट्यूनिंग](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | मॉडल प्रशिक्षण और फाइन-ट्यूनिंग को ट्रैक करने के लिए W&B का उपयोग करें। पहले उनकी [OpenAI फाइन-ट्यूनिंग](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst) गाइड पढ़ें, फिर कुकबुक अभ्यास करें। |
| **Hugging Face ट्यूटोरियल**: [Hugging Face TRL के साथ LLMs कैसे फाइन-ट्यून करें](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | Hugging Face TRL, Transformers, और datasets का उपयोग करके खुले LLMs को फाइन-ट्यून करें: एक उपयोग मामला परिभाषित करें, विकास वातावरण सेट अप करें, एक डेटासेट तैयार करें, फाइन-ट्यून करें, मूल्यांकन करें, और डिप्लॉय करें। |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | Hugging Face से कई मॉडल प्रकारों के लिए एक नो-कोड/लो-कोड लाइब्रेरी। इसे अपनी स्वयं की क्लाउड, Hugging Face Spaces, या लोकल GUI, CLI, या YAML कॉन्फ़िग के माध्यम से चलाएँ। |
| **Unsloth**: [LLMs फाइन-ट्यूनिंग गाइड](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | एक ओपन-सोर्स फ्रेमवर्क जो स्थानीय LLM फाइन-ट्यूनिंग और रिइंफोर्समेंट लर्निंग को सरल बनाता है, तैयार-से-उपयोग के लिए [नोटबुक्स](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) के साथ। |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->