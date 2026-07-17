# موارد للتعلم الذاتي

تم بناء الدرس باستخدام موارد أساسية من OpenAI و Microsoft Foundry كمراجع للمصطلحات والدروس التعليمية. إليك قائمة غير شاملة لرحلات التعلم الذاتي الخاصة بك. كل رابط أدناه يشير إلى مواد حديثة ومدعومة.

## 1. الموارد الأساسية

| العنوان/الرابط | الوصف |
| :--- | :--- |
| [التخصيص الدقيق باستخدام نماذج OpenAI](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | التخصيص الدقيق يُحسّن التعلم بعدد قليل من الأمثلة عبر التدريب على أمثلة أكثر بكثير من التي يمكن وضعها في الموجه - مما يوفر التكاليف، يحسّن جودة الاستجابات، ويمكّن من استجابات بأقل زمن انتظار. **احصل على نظرة عامة على التخصيص الدقيق من OpenAI.** |
| [متى تستخدم التخصيص الدقيق في Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | افهم **ما هو التخصيص الدقيق (المفهوم)**، لماذا يجب أن تأخذه بعين الاعتبار، ما البيانات التي يجب استخدامها، وكيف تقيس الجودة - بالإضافة إلى متى يكون SFT أو DPO أو RFT هو الاختيار الصحيح. |
| [تخصيص نموذج باستخدام التخصيص الدقيق](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | الخطوات الشاملة **كيفية (العملية)** للتخصيص الدقيق في Microsoft Foundry باستخدام البوابة، أو Python SDK الخاص بـ OpenAI / Foundry، أو REST API - ويشمل إعداد البيانات، التدريب، نقاط التحقق، والنشر. |
| [التخصيص الدقيق المستمر](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | العملية التكرارية لاختيار نموذج مُخصص مسبقًا كنموذج أساسي و**تخصيصه بشكل إضافي** على مجموعات جديدة من أمثلة التدريب. |
| [التخصيص الدقيق مع استدعاء أدوات (وظائف)](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | تخصيص النموذج الخاص بك **مع أمثلة استدعاء الأدوات** يحسّن المخرجات - استجابات أكثر دقة، اتساقًا، ومتشكلة بشكل مماثل باستخدام رموز موجه أقل. |
| [توجيهات تخصيص النماذج: Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | تحقق **من النماذج التي يمكن تخصيصها بدقة**، وطرقها المدعومة (SFT / DPO / RFT)، والمناطق التي تتوفر فيها. |
| [نظرة عامة على التخصيص الدقيق: التقنيات والأساليب](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | قارن بين ثلاث تقنيات تدريب (SFT، DPO، RFT) والطريقتين (التشغيل بدون خادم مقابل الحوسبة المدارة)، مع إرشادات لاختيار نموذج أساسي والبدء. |
| **درس تعليمي**: [تخصيص نموذج في Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | أنشئ مجموعة بيانات نموذجية، حضر للتخصيص الدقيق، شغّل عملية تخصيص دقيقة على نموذج مدعوم حاليًا مثل `gpt-4.1-mini`، وانشر النموذج المُخصص على Azure. |
| **درس تعليمي**: [تخصيص النماذج مع نشر API بدون خادم](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | خصص النماذج المفتوحة وشركاء (Phi، Llama، Mistral، والمزيد) لمجموعات بياناتك _باستخدام سير عمل منخفض التعليمات البرمجية ومبني على واجهة المستخدم_ في Microsoft Foundry. |
| **درس تعليمي**: [تخصيص نماذج Hugging Face على Azure Databricks](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | خصّص نموذج Hugging Face باستخدام مكتبة `transformers` على GPU واحد باستخدام Azure Databricks والمدرب Hugging Face Trainer. |
| **تدريب**: [تخصيص نموذج أساسي مع Azure Machine Learning](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | يقدم كتالوج نماذج Azure Machine Learning العديد من النماذج مفتوحة المصدر التي يمكنك تخصيصها. جزء من [مسار تعلم AI التوليدي في Azure ML](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst). |
| **درس تعليمي**: [التخصيص الدقيق في Azure OpenAI مع Weights & Biases](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | تتبع وحلل عمليات التخصيص الدقيق على Azure باستخدام W&B. يُوسّع دليلك إلى التخصيص الدقيق لـ OpenAI بخطوات محددة لـ Azure وتعقب التجارب. |

## 2. الموارد الثانوية

هذه القسم يجمع موارد إضافية جديرة بالاستكشاف لم تتسن لنا تغطيتها في الدرس. استخدمها لبناء خبرتك الخاصة بهذا الموضوع.

| العنوان/الرابط | الوصف |
| :--- | :--- |
| **OpenAI Cookbook**: [إعداد البيانات وتحليلها لتخصيص نموذج المحادثة](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | قم بتهيئة وتحليل مجموعة بيانات المحادثة قبل التخصيص الدقيق: راجع وجود أخطاء في التنسيق، احصل على إحصائيات أساسية، واحسب عدد الرموز (والتكلفة). يرتبط بدليل [OpenAI للتخصيص الدقيق](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst). |
| **OpenAI Cookbook**: [التخصيص الدقيق لتوليد البحث المعزز (RAG) مع Qdrant](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | مثال شامل لتخصيص نماذج OpenAI لـ RAG، بدمج Qdrant والتعلم بعدد قليل من الأمثلة لتعزيز الأداء وتقليل التصنع. |
| **OpenAI Cookbook**: [تخصيص GPT مع Weights & Biases](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | استخدم W&B لتتبع تدريب النموذج والتخصيص الدقيق. ابدأ بدليلهم [OpenAI Fine-Tuning](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst) ثم جرّب تمرين Cookbook. |
| **درس تعليمي من Hugging Face**: [كيفية تخصيص نماذج اللغة الكبيرة مع Hugging Face TRL](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | خصص نماذج LLM المفتوحة باستخدام Hugging Face TRL وTransformers ومجموعات البيانات: حدد حالة استخدام، أعد بيئة تطوير، جهّز مجموعة بيانات، خصّص، قيّم وانشر. |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | مكتبة لا تعليمات برمجية / قليلة التعليمات البرمجية من Hugging Face لتخصيص عدة أنواع من النماذج. شغّلها في السحابة الخاصة بك، على Hugging Face Spaces، أو محليًا عبر واجهة المستخدم الرسومية، CLI، أو إعداد YAML. |
| **Unsloth**: [دليل تخصيص نماذج اللغة الكبيرة](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | إطار مفتوح المصدر يبسط تخصيص نماذج اللغة الكبيرة محليًا والتعلم التعزيزي، مع [دفاتر] جاهزة للاستخدام (https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->