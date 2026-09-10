# خود رہنمائی کے لیے وسائل

اس سبق کی تشکیل اوپنAI اور مائیکروسافٹ فاؤنڈری کے بنیادی وسائل کو حوالہ کے طور پر استعمال کرتے ہوئے کی گئی ہے تاکہ اصطلاحات اور Tutorials کا تعین کیا جا سکے۔ یہاں آپ کی اپنی خود رهنمائی کے سفر کے لیے ایک غیر مکمل فہرست ہے۔ نیچے دیے گئے ہر لنک موجودہ، معاون مواد کی طرف اشارہ کرتے ہیں۔

## 1. بنیادی وسائل

| عنوان/لنک | وضاحت |
| :--- | :--- |
| [اوپنAI ماڈلز کے ساتھ Fine-tuning](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | Fine-tuning چند شٹ لرننگ کو بہتر بناتا ہے کیونکہ یہ ان مثالوں پر تربیت دیتا ہے جو پرامپٹ میں فٹ ہونے سے کہیں زیادہ ہیں - لاگت بچاتا ہے، جواب کی کوالٹی بہتر بناتا ہے، اور کم تاخیر والی درخواستوں کو قابل بناتا ہے۔ **اوپنAI سے Fine-tuning کا جائزہ حاصل کریں۔** |
| [مائیکروسافٹ فاؤنڈری Fine-tuning کب استعمال کریں](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | سمجھیں کہ **Fine-tuning کیا ہے (مفہوم)**، آپ کو اسے کیوں مدنظر رکھنا چاہیے، کون سی ڈیٹا استعمال کریں، اور کوالٹی کو کیسے ناپیں - نیز کب SFT، DPO، یا RFT مناسب ہے۔ |
| [Fine-tuning کے ساتھ ماڈل کو تخصیص کرنا](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | پورٹل، اوپنAI/فاؤنڈری پائتھن SDK، یا REST API استعمال کرتے ہوئے مائیکروسافٹ فاؤنڈری میں Fine-tuning کے لیے مرحلہ وار **طریقہ (process)** - ڈیٹا کی تیاری، تربیت، چیک پوائنٹس اور تعیناتی شامل ہیں۔ |
| [مسلسل Fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | ایک پہلے ہی Fine-tuned ماڈل کو بیس ماڈل کے طور پر منتخب کرنے اور **نئی تربیتی مثالوں کے سیٹ پر اسے مزید Fine-tune کرنے** کا تکراری عمل۔ |
| [ٹول (فنکشن) کالنگ کے ساتھ Fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | اپنے ماڈل کو **ٹول-کالنگ کی مثالوں کے ساتھ Fine-tune کرنا** آؤٹ پٹ کو بہتر بناتا ہے - زیادہ درست، مستقل، اور مماثل فارمیٹ میں جوابات کم پرامپٹ ٹوکنز استعمال کرتے ہوئے۔ |
| [Fine-tuning ماڈلز: مائیکروسافٹ فاؤنڈری کی رہنمائی](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | دیکھیں کہ **کون سے ماڈلز Fine-tune کیے جا سکتے ہیں**، وہ کون سے طریقے (SFT / DPO / RFT) حمایت کرتے ہیں، اور وہ کن علاقوں میں دستیاب ہیں۔ |
| [Fine-tuning کا جائزہ: تکنیکس اور ماڈالٹیز](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | تین تربیتی تکنیکس (SFT، DPO، RFT) اور دو ماڈالٹیز (سرورلیس بمقابلہ منظم کمپیوٹ) کا موازنہ کریں، ساتھ ہی بیس ماڈل منتخب کرنے اور شروع کرنے کی رہنمائی۔ |
| **Tutorial**: [مائیکروسافٹ فاؤنڈری میں ماڈل Fine-tune کریں](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | ایک نمونہ ڈیٹاسیٹ بنائیں، Fine-tuning کی تیاری کریں، حالیہ معاون ماڈل جیسے `gpt-4.1-mini` پر Fine-tuning کی جاب چلائیں، اور Fine-tuned ماڈل کو Azure پر تعینات کریں۔ |
| **Tutorial**: [سرورلیس API تعینات پر ماڈلز Fine-tune کریں](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | Microsoft Foundry میں ایک کم کوڈ، UI-based ورک فلو استعمال کرتے ہوئے اپنے ڈیٹاسیٹس کے لیے کھلے اور پارٹنر ماڈلز (Phi، Llama، Mistral، اور دیگر) کو ٹیلر کریں۔ |
| **Tutorial**: [Azure Databricks پر Hugging Face ماڈلز Fine-tune کریں](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | Azure Databricks اور Hugging Face Trainer کا استعمال کرتے ہوئے ایک GPU پر `transformers` لائبریری کے ساتھ Hugging Face ماڈل Fine-tune کریں۔ |
| **Training**: [Azure Machine Learning کے ساتھ بنیاد ماڈل Fine-tune کریں](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Azure Machine Learning ماڈل کیٹلاگ میں کئی اوپن سورس ماڈلز موجود ہیں جنہیں آپ Fine-tune کر سکتے ہیں۔ یہ [Azure ML Generative AI Learning Path](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) کا حصہ ہے۔ |
| **Tutorial**: [Weights & Biases کے ساتھ Azure OpenAI Fine-tuning](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | Azure پر Fine-tuning رنز کو W&B کے ساتھ ٹریک اور تجزیہ کریں۔ اوپنAI Fine-tuning گائیڈ کو Azure مخصوص مراحل اور تجربہ ٹریکنگ کے ساتھ بڑھاتا ہے۔ |

## 2. ثانوی وسائل

یہ سیکشن اضافی وسائل کو شامل کرتا ہے جو اس سبق میں شامل کرنے کا وقت نہیں تھا لیکن انہیں دیکھنا قیمتی ہے۔ انہیں استعمال کریں تاکہ آپ اس موضوع پر اپنی مہارت بنا سکیں۔

| عنوان/لنک | وضاحت |
| :--- | :--- |
| **OpenAI Cookbook**: [چیٹ ماڈل Fine-tuning کے لیے ڈیٹا کی تیاری اور تجزیہ](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | Fine-tuning سے پہلے چیٹ ڈیٹاسیٹ کی پری پروسیسنگ اور تجزیہ کریں: فارمیٹ کی غلطیوں کی جانچ کریں، بنیادی اعداد و شمار حاصل کریں، اور ٹوکن کی تعداد (اور لاگت) کا تخمینہ لگائیں۔ [OpenAI Fine-tuning guide](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) کے ساتھ جوڑا جاتا ہے۔ |
| **OpenAI Cookbook**: [Qdrant کے ساتھ Retrieval Augmented Generation (RAG) کے لیے Fine-tuning](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | RAG کے لیے اوپنAI ماڈلز کی Fine-tuning کی جامع مثال، Qdrant اور few-shot learning کو مربوط کرکے کارکردگی بڑھانے اور غلط بیانی کو کم کرنے کے لیے۔ |
| **OpenAI Cookbook**: [Weights & Biases کے ساتھ GPT Fine-tuning](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | ماڈل کی تربیت اور Fine-tuning کو W&B کے ذریعے ٹریک کریں۔ ان کی [OpenAI Fine-Tuning](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst) گائیڈ پہلے پڑھیں، پھر Cookbook کی مشق آزمائیں۔ |
| **Hugging Face Tutorial**: [Hugging Face TRL کے ساتھ LLMs کو Fine-tune کیسے کریں](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | Hugging Face TRL، Transformers، اور ڈیٹاسیٹس استعمال کرتے ہوئے اوپن LLMs کو Fine-tune کریں: استعمال کیس کی تعریف کریں، ڈویلپمنٹ ماحول تیار کریں، ڈیٹاسیٹ تیار کریں، Fine-tune کریں، جائزہ لیں، اور تعینات کریں۔ |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | Hugging Face کی جانب سے کئی قسم کے ماڈلز کو Fine-tune کرنے کے لیے کوئی کوڈ / کم کوڈ لائبریری۔ آپ اسے اپنی کلاؤڈ میں، Hugging Face Spaces پر، یا GUI، CLI، یا YAML کنفیگریشن کے ذریعے مقامی طور پر چلا سکتے ہیں۔ |
| **Unsloth**: [LLMs Fine-tuning گائیڈ](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | ایک اوپن سورس فریم ورک جو مقامی LLMs Fine-tuning اور reinforcement learning کو آسان بناتا ہے، تیار استعمال کے لیے [نوٹ بکس](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) کے ساتھ۔ |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->