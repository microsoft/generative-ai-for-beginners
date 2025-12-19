<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85b754d4dc980f270f264d17116d9a5f",
  "translation_date": "2025-12-19T15:53:45+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "he"
}
-->
[![Open Source Models](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.he.png)](https://youtu.be/CuICgfuHFSg?si=x8SpFRUsIxM9dohN)

## מבוא

עולם ה-LLM בקוד פתוח מרגש ומתפתח כל הזמן. שיעור זה נועד לספק מבט מעמיק על מודלים בקוד פתוח. אם אתם מחפשים מידע על איך מודלים קנייניים משווים למודלים בקוד פתוח, עברו לשיעור ["חקירת והשוואת מודלים שונים של LLM"](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). שיעור זה יכסה גם את נושא ההתאמה המדויקת (fine-tuning) אך הסבר מפורט יותר ניתן למצוא בשיעור ["התאמה מדויקת של LLMs"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## מטרות הלמידה

- לקבל הבנה של מודלים בקוד פתוח
- להבין את היתרונות של עבודה עם מודלים בקוד פתוח
- לחקור את המודלים הפתוחים הזמינים ב-Hugging Face וב-Azure AI Studio

## מה הם מודלים בקוד פתוח?

תוכנה בקוד פתוח שיחקה תפקיד מרכזי בצמיחת הטכנולוגיה בתחומים שונים. יוזמת הקוד הפתוח (OSI) הגדירה [10 קריטריונים לתוכנה](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) כדי שתסווג כקוד פתוח. קוד המקור חייב להיות משותף בפומבי תחת רישיון שאושר על ידי OSI.

בעוד שפיתוח LLMs כולל אלמנטים דומים לפיתוח תוכנה, התהליך אינו זהה במדויק. זה עורר דיון רב בקהילה לגבי הגדרת קוד פתוח בהקשר של LLMs. כדי שמודל יתאים להגדרה המסורתית של קוד פתוח, המידע הבא צריך להיות זמין לציבור:

- מערכי נתונים ששימשו לאימון המודל.
- משקלי המודל המלאים כחלק מהאימון.
- קוד ההערכה.
- קוד ההתאמה המדויקת (fine-tuning).
- משקלי המודל המלאים ומדדי האימון.

כרגע קיימים רק כמה מודלים שעומדים בקריטריונים אלו. [מודל OLMo שפותח על ידי מכון אלן לאינטליגנציה מלאכותית (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) הוא אחד שמתאים לקטגוריה זו.

בשיעור זה, נתייחס למודלים כ"מודלים פתוחים" מכיוון שהם עשויים לא להתאים לקריטריונים הנ"ל בזמן הכתיבה.

## יתרונות של מודלים פתוחים

**ניתנים להתאמה גבוהה** - מכיוון שמודלים פתוחים משוחררים עם מידע מפורט על האימון, חוקרים ומפתחים יכולים לשנות את הפנימיות של המודל. זה מאפשר יצירת מודלים מתמחים מאוד המותאמים למשימה או תחום לימוד ספציפי. דוגמאות לכך הן יצירת קוד, פעולות מתמטיות וביולוגיה.

**עלות** - העלות לכל טוקן לשימוש ופריסה של מודלים אלו נמוכה יותר מזו של מודלים קנייניים. כאשר בונים יישומי AI גנרטיביים, יש לשקול את הביצועים מול המחיר בעת עבודה עם מודלים אלו במקרי השימוש שלכם.

![Model Cost](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.he.png)
מקור: Artificial Analysis

**גמישות** - עבודה עם מודלים פתוחים מאפשרת גמישות בשימוש במודלים שונים או בשילוב שלהם. דוגמה לכך היא [עוזרי HuggingChat](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst) שבה המשתמש יכול לבחור את המודל בשימוש ישירות בממשק המשתמש:

![Choose Model](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.he.png)

## חקירת מודלים פתוחים שונים

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), שפותח על ידי Meta, הוא מודל פתוח המותאם ליישומי שיחה. זאת בזכות שיטת ההתאמה המדויקת שלו, שכללה כמות גדולה של דיאלוג ומשוב אנושי. בשיטה זו, המודל מפיק תוצאות המותאמות יותר לציפיות האנושיות ומספק חוויית משתמש טובה יותר.

דוגמאות לגרסאות מותאמות של Llama כוללות את [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), שמתמחה ביפנית, ו-[Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), שהיא גרסה משופרת של המודל הבסיסי.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) הוא מודל פתוח עם דגש חזק על ביצועים גבוהים ויעילות. הוא משתמש בגישת Mixture-of-Experts שמשלבת קבוצת מודלים מומחים מתמחים למערכת אחת שבה בהתאם לקלט, נבחרים מודלים מסוימים לשימוש. זה הופך את החישוב ליעיל יותר כי המודלים מתמקדים רק בקלטים שבהם הם מתמחים.

דוגמאות לגרסאות מותאמות של Mistral כוללות את [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), שמתמקד בתחום הרפואי, ו-[OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), שמבצע חישובים מתמטיים.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) הוא LLM שפותח על ידי Technology Innovation Institute (**TII**). ה-Falcon-40B אומן על 40 מיליארד פרמטרים שהוכח כי הוא מבצע טוב יותר מ-GPT-3 עם תקציב חישוב נמוך יותר. זאת בזכות השימוש באלגוריתם FlashAttention ובתשומת לב מרובת שאילתות שמאפשרים לו להפחית את דרישות הזיכרון בזמן ההסקה. בזכות זמן ההסקה המופחת, ה-Falcon-40B מתאים ליישומי שיחה.

דוגמאות לגרסאות מותאמות של Falcon הן [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), עוזר שנבנה על מודלים פתוחים, ו-[GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), שמספק ביצועים גבוהים יותר מהמודל הבסיסי.

## איך לבחור

אין תשובה אחת לבחירת מודל פתוח. מקום טוב להתחיל הוא להשתמש בפילטר לפי משימה ב-Azure AI Studio. זה יעזור לכם להבין לאילו סוגי משימות המודל אומן. Hugging Face גם מחזיקה בלוח מובילים של LLM שמראה את המודלים הטובים ביותר לפי מדדים מסוימים.

כשמחפשים להשוות LLMs בין סוגים שונים, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) הוא משאב מצוין נוסף:

![Model Quality](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.he.png)
מקור: Artificial Analysis

אם עובדים על מקרה שימוש ספציפי, חיפוש גרסאות מותאמות שמתמקדות באותו תחום יכול להיות יעיל. ניסוי עם מספר מודלים פתוחים כדי לראות איך הם מתפקדים לפי הציפיות שלכם ושל המשתמשים הוא גם פרקטיקה טובה.

## צעדים הבאים

החלק הטוב במודלים פתוחים הוא שניתן להתחיל לעבוד איתם די מהר. בדקו את [קטלוג המודלים של Azure AI Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), שמציג אוסף ספציפי של Hugging Face עם המודלים שדיברנו עליהם כאן.

## הלמידה לא נעצרת כאן, המשיכו את המסע

לאחר שסיימתם את השיעור הזה, בדקו את [אוסף הלמידה של AI גנרטיבי](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) שלנו כדי להמשיך לשפר את הידע שלכם ב-AI גנרטיבי!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->