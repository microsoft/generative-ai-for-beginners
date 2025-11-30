<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "807f0d9fc1747e796433534e1be6a98a",
  "translation_date": "2025-10-17T20:06:34+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "he"
}
-->
[![מודלים בקוד פתוח](../../../translated_images/18-lesson-banner.f30176815b1a5074fce9cceba317720586caa99e24001231a92fd04eeb54a121.he.png)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# כיוונון עדין של מודל השפה הגדול שלך

שימוש במודלים שפתיים גדולים לבניית יישומי AI גנרטיביים מביא עמו אתגרים חדשים. אחד האתגרים המרכזיים הוא להבטיח את איכות התגובות (דיוק ורלוונטיות) בתוכן שנוצר על ידי המודל עבור בקשה מסוימת של משתמש. בשיעורים הקודמים דנו בטכניקות כמו הנדסת הנחיות והפקת מידע מוגברת שמנסות לפתור את הבעיה על ידי _שינוי קלט ההנחיה_ למודל הקיים.

בשיעור של היום נדון בטכניקה שלישית, **כיוונון עדין**, שמנסה להתמודד עם האתגר על ידי _אימון מחדש של המודל עצמו_ עם נתונים נוספים. בואו נצלול לפרטים.

## מטרות למידה

שיעור זה מציג את מושג הכיוונון העדין עבור מודלים שפתיים שהוכנו מראש, בוחן את היתרונות והאתגרים של גישה זו, ומספק הנחיות מתי וכיצד להשתמש בכיוונון עדין כדי לשפר את ביצועי המודלים הגנרטיביים שלכם.

בסוף השיעור הזה, תוכלו לענות על השאלות הבאות:

- מהו כיוונון עדין עבור מודלים שפתיים?
- מתי ולמה כיוונון עדין הוא שימושי?
- איך ניתן לכוונן מודל שהוכן מראש?
- מהם המגבלות של כיוונון עדין?

מוכנים? בואו נתחיל.

## מדריך מאויר

רוצים לקבל תמונה כללית של מה שנכסה לפני שנצלול פנימה? עיינו במדריך המאויר שמתאר את מסע הלמידה של השיעור הזה - החל מלמידת המושגים המרכזיים והמוטיבציה לכיוונון עדין, ועד להבנת התהליך והפרקטיקות הטובות ביותר לביצוע משימת הכיוונון העדין. זהו נושא מרתק לחקירה, אז אל תשכחו לבדוק את [Resources](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) למידע נוסף שיתמוך במסע הלמידה העצמאי שלכם!

![מדריך מאויר לכיוונון עדין של מודלים שפתיים](../../../translated_images/18-fine-tuning-sketchnote.11b21f9ec8a703467a120cb79a28b5ac1effc8d8d9d5b31bbbac6b8640432e14.he.png)

## מהו כיוונון עדין עבור מודלים שפתיים?

לפי ההגדרה, מודלים שפתיים גדולים הם _מודלים שהוכנו מראש_ על כמויות גדולות של טקסט שמקורו במקורות מגוונים, כולל האינטרנט. כפי שלמדנו בשיעורים הקודמים, אנו זקוקים לטכניקות כמו _הנדסת הנחיות_ ו_הפקת מידע מוגברת_ כדי לשפר את איכות התגובות של המודל לשאלות המשתמש ("הנחיות").

טכניקה פופולרית בהנדסת הנחיות כוללת מתן הנחיות נוספות למודל על מה מצופה בתגובה, או על ידי מתן _הוראות_ (הכוונה מפורשת) או _מתן כמה דוגמאות_ (הכוונה משתמעת). זה נקרא _למידה עם מעט דוגמאות_, אך יש לה שתי מגבלות:

- מגבלות טוקנים במודל יכולות להגביל את מספר הדוגמאות שניתן לתת, ולהגביל את היעילות.
- עלויות טוקנים במודל יכולות להפוך את הוספת הדוגמאות לכל הנחיה ליקרה, ולהגביל את הגמישות.

כיוונון עדין הוא פרקטיקה נפוצה במערכות למידת מכונה שבה אנו לוקחים מודל שהוכן מראש ומאמנים אותו מחדש עם נתונים חדשים כדי לשפר את ביצועיו במשימה מסוימת. בהקשר של מודלים שפתיים, ניתן לכוונן את המודל שהוכן מראש _עם סט דוגמאות מותאם למשימה או תחום יישום מסוים_ כדי ליצור **מודל מותאם אישית** שעשוי להיות מדויק ורלוונטי יותר למשימה או תחום ספציפי זה. יתרון נוסף של כיוונון עדין הוא שהוא יכול גם להפחית את מספר הדוגמאות הנדרשות ללמידה עם מעט דוגמאות - מה שמפחית את השימוש בטוקנים ואת העלויות הקשורות.

## מתי ולמה כדאי לכוונן מודלים?

בהקשר _זה_, כשאנו מדברים על כיוונון עדין, אנו מתייחסים לכיוונון עדין **מונחה** שבו האימון מחדש מתבצע על ידי **הוספת נתונים חדשים** שלא היו חלק ממערך הנתונים המקורי. זה שונה מגישה של כיוונון עדין לא מונחה שבה המודל מאומן מחדש על הנתונים המקוריים, אך עם פרמטרים שונים.

הדבר המרכזי שיש לזכור הוא שכיוונון עדין הוא טכניקה מתקדמת שדורשת רמה מסוימת של מומחיות כדי להשיג את התוצאות הרצויות. אם הוא מבוצע בצורה לא נכונה, הוא עשוי לא לספק את השיפורים הצפויים, ואף עלול לפגוע בביצועי המודל עבור התחום הממוקד שלכם.

לכן, לפני שלומדים "איך" לכוונן מודלים שפתיים, צריך לדעת "למה" כדאי לבחור בדרך זו, ו"מתי" להתחיל את תהליך הכיוונון העדין. התחילו בשאלות הבאות:

- **מקרה שימוש**: מהו _מקרה השימוש_ שלכם לכיוונון עדין? איזה היבט של המודל שהוכן מראש אתם רוצים לשפר?
- **חלופות**: האם ניסיתם _טכניקות אחרות_ כדי להשיג את התוצאות הרצויות? השתמשו בהן כדי ליצור בסיס להשוואה.
  - הנדסת הנחיות: נסו טכניקות כמו הנחיות עם מעט דוגמאות הכוללות דוגמאות לתגובות הנחיה רלוונטיות. העריכו את איכות התגובות.
  - הפקת מידע מוגברת: נסו להוסיף להנחיות תוצאות חיפוש שנמצאו על ידי חיפוש בנתונים שלכם. העריכו את איכות התגובות.
- **עלויות**: האם זיהיתם את העלויות לכיוונון עדין?
  - יכולת כיוונון - האם המודל שהוכן מראש זמין לכיוונון עדין?
  - מאמץ - להכנת נתוני אימון, הערכת ושיפור המודל.
  - חישוב - להרצת משימות כיוונון עדין, ולפריסת המודל המכוונן.
  - נתונים - גישה לדוגמאות איכותיות מספיק להשפעת הכיוונון העדין.
- **יתרונות**: האם אישרתם את היתרונות של כיוונון עדין?
  - איכות - האם המודל המכוונן עדין עלה על הבסיס?
  - עלות - האם הוא מפחית את השימוש בטוקנים על ידי פישוט הנחיות?
  - הרחבה - האם ניתן להתאים את המודל הבסיסי לתחומים חדשים?

על ידי מענה על שאלות אלו, תוכלו להחליט אם כיוונון עדין הוא הגישה הנכונה למקרה השימוש שלכם. באופן אידיאלי, הגישה תקפה רק אם היתרונות עולים על העלויות. לאחר שתחליטו להמשיך, הגיע הזמן לחשוב על _איך_ ניתן לכוונן את המודל שהוכן מראש.

רוצים לקבל תובנות נוספות על תהליך קבלת ההחלטות? צפו ב-[To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## איך ניתן לכוונן מודל שהוכן מראש?

כדי לכוונן מודל שהוכן מראש, אתם צריכים:

- מודל שהוכן מראש לכיוונון
- מערך נתונים לשימוש בכיוונון
- סביבת אימון להרצת משימת הכיוונון
- סביבת אירוח לפריסת המודל המכוונן

## כיוונון עדין בפעולה

המשאבים הבאים מספקים מדריכים שלב אחר שלב שיעזרו לכם לעבור דוגמה אמיתית באמצעות מודל נבחר עם מערך נתונים מותאם. כדי לעבוד דרך מדריכים אלו, תצטרכו חשבון אצל ספק מסוים, יחד עם גישה למודל ולמערכי הנתונים הרלוונטיים.

| ספק          | מדריך                                                                                                                                                                       | תיאור                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [How to fine-tune chat models](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | למדו לכוונן `gpt-35-turbo` עבור תחום ספציפי ("עוזר מתכונים") על ידי הכנת נתוני אימון, הרצת משימת הכיוונון, ושימוש במודל המכוונן לצורך הסקת מסקנות.                                                                                                                                                                                                                                              |
| Azure OpenAI | [GPT 3.5 Turbo fine-tuning tutorial](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | למדו לכוונן מודל `gpt-35-turbo-0613` **ב-Azure** על ידי ביצוע צעדים ליצירה והעלאת נתוני אימון, הרצת משימת הכיוונון. פרסו והשתמשו במודל החדש.                                                                                                                                                                                                                                                                 |
| Hugging Face | [Fine-tuning LLMs with Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | פוסט זה בבלוג מדריך אתכם בכיוונון עדין של _מודל שפה פתוח_ (לדוגמה: `CodeLlama 7B`) באמצעות ספריית [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) ו-[Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst]) עם [מערכי נתונים פתוחים](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) ב-Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Fine-tuning LLMs with AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (או AutoTrain Advanced) היא ספריית פייתון שפותחה על ידי Hugging Face שמאפשרת כיוונון עדין למשימות רבות, כולל כיוונון עדין של מודלים שפתיים. AutoTrain היא פתרון ללא קוד וכיוונון עדין יכול להתבצע בענן שלכם, ב-Hugging Face Spaces או מקומית. היא תומכת גם בממשק מבוסס אינטרנט, CLI ואימון באמצעות קבצי תצורה yaml.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## משימה

בחרו אחד מהמדריכים לעיל ועברו דרכו. _ייתכן שנשכפל גרסה של מדריכים אלו במחברות Jupyter במאגר זה לצורך התייחסות בלבד. אנא השתמשו במקורות המקוריים ישירות כדי לקבל את הגרסאות העדכניות ביותר_.

## עבודה נהדרת! המשיכו ללמוד.

לאחר השלמת השיעור הזה, בדקו את [אוסף הלמידה של AI גנרטיבי](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) כדי להמשיך להעמיק את הידע שלכם ב-AI גנרטיבי!

ברכות!! סיימתם את השיעור האחרון מסדרת v2 של הקורס הזה! אל תפסיקו ללמוד ולבנות. \*\*בדקו את [RESOURCES](RESOURCES.md?WT.mc_id=academic-105485-koreyst) למידע נוסף בנושא זה.

סדרת השיעורים v1 שלנו גם עודכנה עם משימות ומושגים נוספים. אז קחו רגע לרענן את הידע שלכם - ואל תהססו [לשתף שאלות ומשוב](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) כדי לעזור לנו לשפר את השיעורים האלו עבור הקהילה.

---

**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. איננו אחראים לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.