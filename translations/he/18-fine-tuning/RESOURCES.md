# משאבים ללמידה עצמית

השיעור נבנה תוך שימוש במשאבים מרכזיים מ-OpenAI ו-Microsoft Foundry כהפניות למונחולוגיה והדרכות. להלן רשימה לא מקיפה למסעות למידה עצמית משלכם. כל קישור למטה מפנה לחומר עכשווי ומגובה.

## 1. משאבים ראשוניים

| כותרת/קישור | תיאור |
| :--- | :--- |
| [כיוונון מדויק עם מודלי OpenAI](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | כיוונון מדויק משפר את הלמידה עם כמה דוגמאות באמצעות אימון על הרבה דוגמאות מעבר למה שנכנס בפרומפט - חוסך עלויות, משפר את איכות התגובה, ומאפשר בקשות עם השהייה נמוכה יותר. **קבל סקירה כללית על כיוונון מדויק מ-OpenAI.** |
| [מתי להשתמש בכיוונון מדויק של Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | הבן **מהו כיוונון מדויק (מושג)**, מדוע כדאי לשקול זאת, אילו נתונים להשתמש וכיצד למדוד איכות - בנוסף מתי SFT, DPO או RFT הם המתאימים. |
| [התאמה אישית של מודל באמצעות כיוונון מדויק](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | ה-**כיצד-לעשות (תהליך)** מלא לכיוונון מדויק ב-Microsoft Foundry באמצעות הפורטל, OpenAI / Foundry Python SDK, או REST API - כולל הכנת נתונים, אימון, נקודות ביקורת ופריסה. |
| [כיוונון מדויק רציף](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | תהליך איטרטיבי של בחירת מודל שכבר כוונן כבסיס והמשך כיוונון מדויק שלו על קבוצות חדשות של דוגמאות אימון. |
| [כיוונון מדויק עם קריאה לכלי (פונקציה)](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | כיוונון מדויק של המודל שלך **עם דוגמאות לקריאה לכלי** משפר את הפלט - תגובות מדויקות, עקביות ובפורמט דומה המשתמשות בכמה שפחות טוקנים בפרומפט. |
| [הנחיות לכיוונון מודלים: Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | בדוק **איזה מודלים ניתנים לכיוונון מדויק**, את שיטות התמיכה (SFT / DPO / RFT) ואת האזורים בהם הם זמינים. |
| [סקירת כיוונון מדויק: טכניקות ומודליים](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | השווה בין שלוש טכניקות האימון (SFT, DPO, RFT) והשני המודלים (שרת ללא שרת מול חישוב מנוהל), עם הנחיות לבחירת מודל בסיס ולהתחלה. |
| **מדריך**: [כיוונון מודל ב-Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | צור מאגר נתונים לדוגמה, הכין לכיוונון מדויק, הפעל משימת כיוונון על מודל נתמך כמו `gpt-4.1-mini`, ופרוס את המודל הכוונן ב-Azure. |
| **מדריך**: [כיוונון מודלים עם פריסות API ללא שרת](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | התאם מודלים פתוחים ושותפים (Phi, Llama, Mistral ועוד) למאגר הנתונים שלך _באמצעות תהליך עבודה מבוסס ממשק משתמש וללא קוד_ ב-Microsoft Foundry. |
| **מדריך**: [כיוונון מודלים של Hugging Face ב-Azure Databricks](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | כוונן מודל Hugging Face עם ספריית `transformers` על GPU יחיד באמצעות Azure Databricks ו-Hugging Face Trainer. |
| **הדרכה**: [כיוונון מודל בסיס עם Azure Machine Learning](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | קטלוג המודלים של Azure Machine Learning מציע מודלים רבים בקוד פתוח אותם ניתן לכוונן. חלק מ[נתיב הלמידה של Azure ML Generative AI](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst). |
| **מדריך**: [כיוונון Azure OpenAI עם Weights & Biases](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | עקוב ונתח ריצות כיוונון מדויק ב-Azure עם W&B. מרחיב את מדריך הכיוונון המדויק של OpenAI עם שלבים ספציפיים ל-Azure ומעקב ניסויים. |

## 2. משאבים משניים

קטע זה מכיל משאבים נוספים שכדאי לחקור אותם שלא הספקנו לכסות בשיעור. השתמש בהם לבניית המומחיות שלך בנושא זה.

| כותרת/קישור | תיאור |
| :--- | :--- |
| **OpenAI Cookbook**: [הכנת נתונים וניתוח לכיוונון מדויק של מודל שיחה](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | לעבד ולנתח מאגר שיחות לפני כיוונון: בדוק שגיאות בפורמט, קבל סטטיסטיקות בסיסיות, והכן אומדן של ספירות טוקנים (ולעלות). מתאים עם [מדריך הכיוונון המדויק של OpenAI](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst). |
| **OpenAI Cookbook**: [כיוונון מדויק עבור יצירתיות משופרת (RAG) עם Qdrant](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | דוגמה מקיפה לכיוונון מודלי OpenAI עבור RAG, המשווה שילוב Qdrant ולמידה עם כמה דוגמאות לשיפור ביצועים ולהפחתת המצאות. |
| **OpenAI Cookbook**: [כיוונון GPT עם Weights & Biases](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | השתמש ב-W&B למעקב והכשרה של מודלים וכיוונון מדויק. קרא קודם את [מדריך ה-OpenAI Fine-Tuning](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst), ואז נסה את תרגיל ה-Cookbook. |
| **מדריך Hugging Face**: [כיצד לכוונן LLMs עם Hugging Face TRL](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | כוונן מודלי LLM פתוחים באמצעות Hugging Face TRL, Transformers ומאגרים: הגדר מקרה שימוש, הקם סביבת פיתוח, הכין מאגר נתונים, כוונן, הערך ופרוס. |
| **Hugging Face**: [AutoTrain מתקדם](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | ספריית ללא קוד / קוד נמוך מ-Hugging Face לכיוונון סוגים רבים של מודלים. הפעל בענן שלך, על Hugging Face Spaces, או מקומית באמצעות GUI, CLI, או קונפיגורצית YAML. |
| **Unsloth**: [מדריך לכיוונון LLMs](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | מסגרת בקוד פתוח שמפשטת כיוונון LLM מקומי ולמידה בחיזוק, עם [פנקסי הערות](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) מוכנים לשימוש. |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->