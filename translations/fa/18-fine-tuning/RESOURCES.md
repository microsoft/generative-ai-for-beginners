# منابع برای یادگیری خودراهبر

این درس با استفاده از منابع اصلی OpenAI و Microsoft Foundry به عنوان مراجع برای اصطلاحات و آموزش‌ها ساخته شده است. در اینجا فهرستی غیرجامع برای مسیرهای یادگیری خودراهبر شما ارائه شده است. هر لینک زیر به مطالب فعلی و پشتیبانی‌شده اشاره دارد.

## 1. منابع اولیه

| عنوان/لینک | توضیحات |
| :--- | :--- |
| [تنظیم دقیق با مدل‌های OpenAI](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | تنظیم دقیق با استفاده از آموزش بر روی نمونه‌های بسیار بیشتر از آنچه در پرامپت جا می‌شود، عملکرد یادگیری چندنمونه‌ای را بهبود می‌بخشد - صرفه‌جویی در هزینه‌ها، بهبود کیفیت پاسخ و امکان درخواست‌های با تأخیر کمتر. **مروری بر تنظیم دقیق از OpenAI دریافت کنید.** |
| [چه زمانی باید تنظیم دقیق Microsoft Foundry را استفاده کرد](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | درک کنید **تنظیم دقیق چیست (مفهوم)**، چرا باید آن را در نظر بگیرید، چه داده‌هایی باید استفاده شود و چگونه کیفیت را بسنجید - علاوه بر زمانی که SFT، DPO، یا RFT مناسب است. |
| [شخصی‌سازی مدل با تنظیم دقیق](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | **روند گام به گام (چگونگی)** تنظیم دقیق در Microsoft Foundry با استفاده از پرتال، SDK پایتون OpenAI / Foundry، یا REST API - شامل آماده‌سازی داده، آموزش، نقطه‌های بررسی و استقرار. |
| [تنظیم دقیق مستمر](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | روند تکراری انتخاب یک مدل قبلاً تنظیم شده به عنوان مدل پایه و **تنظیم دقیق بیشتر** آن بر روی مجموعه‌های جدید مثال‌های آموزشی. |
| [تنظیم دقیق با فراخوانی ابزار (تابع)](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | تنظیم دقیق مدل شما **با مثال‌های فراخوانی ابزار** خروجی را بهبود می‌بخشد - پاسخ‌های دقیق‌تر، سازگارتر و با قالب‌بندی مشابه با استفاده از توکن‌های کمتر در پرامپت. |
| [راهنمای تنظیم دقیق مدل‌ها: Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | ببینید **کدام مدل‌ها را می‌توان تنظیم دقیق کرد**، روش‌های پشتیبانی‌شده (SFT / DPO / RFT) و مناطقی که در دسترس هستند. |
| [مرور کلی تنظیم دقیق: تکنیک‌ها و حالت‌ها](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | مقایسه سه تکنیک آموزش (SFT، DPO، RFT) و دو حالت (بدون سرور در مقابل محاسبات مدیریت شده)، با راهنمایی در انتخاب مدل پایه و شروع کار. |
| **آموزش**: [تنظیم دقیق یک مدل در Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | ایجاد یک مجموعه داده نمونه، آماده‌سازی برای تنظیم دقیق، اجرای یک کار تنظیم دقیق روی مدل‌های فعلی مانند `gpt-4.1-mini` و استقرار مدل تنظیم شده روی Azure. |
| **آموزش**: [تنظیم دقیق مدل‌ها با استقرار API بدون سرور](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | سفارشی‌سازی مدل‌های باز و شریک (Phi، Llama، Mistral و غیره) به داده‌های شما _با استفاده از یک جریان کاری کم‌کد و مبتنی بر رابط کاربری_ در Microsoft Foundry. |
| **آموزش**: [تنظیم دقیق مدل‌های Hugging Face در Azure Databricks](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | تنظیم دقیق مدل Hugging Face با کتابخانه `transformers` روی یک کارت گرافیک واحد با استفاده از Azure Databricks و Hugging Face Trainer. |
| **آموزش**: [تنظیم دقیق مدل پایه با Azure Machine Learning](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | فهرست مدل‌های Azure Machine Learning شامل بسیاری از مدل‌های متن‌باز است که می‌توانید تنظیم دقیق کنید. بخشی از مسیر یادگیری [Azure ML Generative AI](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst). |
| **آموزش**: [تنظیم دقیق Azure OpenAI با Weights & Biases](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | ردیابی و تحلیل جلسات تنظیم دقیق در Azure با W&B. راهنمای تنظیم دقیق OpenAI را با مراحل خاص Azure و ردیابی آزمایش‌ها گسترش می‌دهد. |

## 2. منابع ثانویه

این بخش منابع اضافی قابل توجهی را در بر می‌گیرد که فرصت بررسی آنها در درس پیش نیامده بود. از آنها برای ساخت تخصص خود در این موضوع استفاده کنید.

| عنوان/لینک | توضیحات |
| :--- | :--- |
| **OpenAI Cookbook**: [آماده‌سازی داده و تحلیل برای تنظیم دقیق مدل چت](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | پیش‌پردازش و تحلیل یک مجموعه داده چت قبل از تنظیم دقیق: بررسی خطاهای فرمت، به دست آوردن آمار پایه و برآورد تعداد توکن‌ها (و هزینه). مرتبط با راهنمای [تنظیم دقیق OpenAI](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst). |
| **OpenAI Cookbook**: [تنظیم دقیق برای تولید افزوده بازیابی‌شده (RAG) با Qdrant](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | مثال جامعی از تنظیم دقیق مدل‌های OpenAI برای RAG، با ادغام Qdrant و یادگیری چندنمونه‌ای برای افزایش عملکرد و کاهش ساختگی‌ها. |
| **OpenAI Cookbook**: [تنظیم دقیق GPT با Weights & Biases](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | استفاده از W&B برای ردیابی آموزش و تنظیم دقیق مدل. ابتدا راهنمای [تنظیم دقیق OpenAI](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst) آنها را بخوانید و سپس تمرین Cookbook را امتحان کنید. |
| **آموزش Hugging Face**: [چگونه LLMها را با Hugging Face TRL تنظیم دقیق کنیم](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | تنظیم دقیق LLMهای باز با استفاده از Hugging Face TRL، Transformers و مجموعه داده‌ها: تعریف مورد استفاده، ایجاد محیط توسعه، آماده‌سازی داده، تنظیم دقیق، ارزیابی و استقرار. |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | کتابخانه‌ای بدون کد/کم‌کد از Hugging Face برای تنظیم دقیق بسیاری از انواع مدل‌ها. می‌توانید آن را در فضای ابری خود، در Hugging Face Spaces یا به صورت محلی از طریق GUI، CLI یا پیکربندی YAML اجرا کنید. |
| **Unsloth**: [راهنمای تنظیم دقیق LLMها](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | چارچوب متن‌باز که تنظیم دقیق LLMها به صورت محلی و یادگیری تقویتی را ساده می‌کند، همراه با [دفترچه‌های آماده](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->