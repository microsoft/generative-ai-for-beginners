<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b5b016b0eb8a1cef2e3097620d8aa23",
  "translation_date": "2025-12-19T15:55:46+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "he"
}
-->
# בחירה והגדרת ספק LLM 🔑

המשימות **יכולות** להיות מוגדרות גם לעבודה מול פריסות של מודל שפה גדול (LLM) דרך ספק שירות נתמך כמו OpenAI, Azure או Hugging Face. אלה מספקים _נקודת קצה מתארחת_ (API) אליה ניתן לגשת באופן תכנותי עם האישורים הנכונים (מפתח API או טוקן). בקורס זה נדון בספקים הבאים:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) עם מודלים מגוונים כולל סדרת GPT המרכזית.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) למודלים של OpenAI עם דגש על מוכנות ארגונית
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) למודלים בקוד פתוח ושרת אינפרנס

**תצטרכו להשתמש בחשבונות שלכם לתרגילים אלה**. המשימות הן אופציונליות כך שתוכלו לבחור להגדיר אחד, את כולם - או אף אחד - מהספקים בהתאם לתחומי העניין שלכם. כמה הנחיות להרשמה:

| הרשמה | עלות | מפתח API | Playground | הערות |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [תמחור](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [מבוסס פרויקט](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [ללא קוד, ווב](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | מודלים מרובים זמינים |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [תמחור](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [התחלה מהירה SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [התחלה מהירה Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [חובה להגיש בקשה מראש לגישה](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [תמחור](https://huggingface.co/pricing) | [טוקני גישה](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [ל-Hugging Chat יש מודלים מוגבלים](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

עקבו אחר ההוראות למטה כדי _להגדיר_ את המאגר הזה לשימוש עם ספקים שונים. משימות שדורשות ספק מסוים יכילו אחד מהתגים האלה בשם הקובץ שלהן:

- `aoai` - דורש נקודת קצה ומפתח של Azure OpenAI
- `oai` - דורש נקודת קצה ומפתח של OpenAI
- `hf` - דורש טוקן של Hugging Face

ניתן להגדיר אחד, אף אחד, או את כל הספקים. משימות קשורות פשוט יכשלו אם חסרים האישורים.

## יצירת קובץ `.env`

אנו מניחים שכבר קראתם את ההנחיות למעלה ונרשמתם אצל הספק הרלוונטי, וקיבלתם את האישורים הנדרשים (API_KEY או טוקן). במקרה של Azure OpenAI, אנו מניחים שיש לכם גם פריסה תקפה של שירות Azure OpenAI (נקודת קצה) עם לפחות מודל GPT אחד לפריסת שיחה.

השלב הבא הוא להגדיר את **משתני הסביבה המקומיים** שלכם כך:

1. חפשו בתיקיית השורש קובץ `.env.copy` שצריך להכיל תוכן כמו זה:

   ```bash
   # ספק OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # ברירת המחדל נקבעה!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. העתיקו את הקובץ ל-`.env` באמצעות הפקודה למטה. קובץ זה הוא _gitignore-ד_, לשמירת סודות בבטחה.

   ```bash
   cp .env.copy .env
   ```

3. מלאו את הערכים (החליפו את הממלאים בצד ימין של `=`) כפי שמתואר בסעיף הבא.

4. (אופציונלי) אם אתם משתמשים ב-GitHub Codespaces, יש לכם אפשרות לשמור משתני סביבה כ_סודות Codespaces_ המשויכים למאגר זה. במקרה כזה, לא תצטרכו להגדיר קובץ .env מקומי. **עם זאת, שימו לב שאפשרות זו פועלת רק אם אתם משתמשים ב-GitHub Codespaces.** עדיין תצטרכו להגדיר את קובץ .env אם אתם משתמשים ב-Docker Desktop במקום.

## מילוי קובץ `.env`

בואו נסתכל במהירות על שמות המשתנים כדי להבין מה הם מייצגים:

| משתנה  | תיאור  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | זהו טוקן הגישה של המשתמש שהגדרתם בפרופיל שלכם |
| OPENAI_API_KEY | זהו מפתח האישור לשימוש בשירות לנקודות קצה שאינן Azure OpenAI |
| AZURE_OPENAI_API_KEY | זהו מפתח האישור לשימוש בשירות זה |
| AZURE_OPENAI_ENDPOINT | זו נקודת הקצה המופעלת למשאב Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | זו נקודת הקצה לפריסת מודל _יצירת טקסט_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | זו נקודת הקצה לפריסת מודל _הטמעת טקסט_ |
| | |

הערה: שני המשתנים האחרונים של Azure OpenAI משקפים מודל ברירת מחדל להשלמת שיחה (יצירת טקסט) ולחיפוש וקטורי (הטמעות) בהתאמה. ההוראות להגדרתם יוגדרו במשימות הרלוונטיות.

## הגדרת Azure: מפורטל

ערכי נקודת הקצה והמפתח של Azure OpenAI יימצאו ב-[פורטל Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) אז נתחיל שם.

1. גשו ל-[פורטל Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. לחצו על אפשרות **Keys and Endpoint** בסרגל הצד (תפריט משמאל).
1. לחצו על **Show Keys** - אמור להופיע: KEY 1, KEY 2 ו-Endpoint.
1. השתמשו בערך KEY 1 עבור AZURE_OPENAI_API_KEY
1. השתמשו בערך Endpoint עבור AZURE_OPENAI_ENDPOINT

לאחר מכן, נצטרך את נקודות הקצה למודלים הספציפיים שהפעלנו.

1. לחצו על אפשרות **Model deployments** בסרגל הצד (תפריט שמאל) למשאב Azure OpenAI.
1. בדף היעד, לחצו על **Manage Deployments**

זה יוביל אתכם לאתר Azure OpenAI Studio, שם נמצא את הערכים הנוספים כפי שמתואר למטה.

## הגדרת Azure: מ-Studio

1. נווטו ל-[Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **מהמשאב שלכם** כפי שתואר למעלה.
1. לחצו על לשונית **Deployments** (סרגל צד, שמאל) כדי לראות את המודלים המופעלים כרגע.
1. אם המודל הרצוי לא מופעל, השתמשו ב-**Create new deployment** כדי להפעילו.
1. תזדקקו למודל _text-generation_ - אנו ממליצים: **gpt-35-turbo**
1. תזדקקו למודל _text-embedding_ - אנו ממליצים על **text-embedding-ada-002**

כעת עדכנו את משתני הסביבה כדי לשקף את שם ה_Deployment_ שבו השתמשתם. בדרך כלל זה יהיה זהה לשם המודל אלא אם שיניתם אותו במפורש. לדוגמה, ייתכן שיהיה לכם:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**אל תשכחו לשמור את קובץ ה-.env בסיום**. כעת תוכלו לצאת מהקובץ ולחזור להוראות להרצת המחברת.

## הגדרת OpenAI: מהפרופיל

מפתח ה-API של OpenAI שלכם נמצא ב-[חשבון OpenAI שלכם](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). אם אין לכם, תוכלו להירשם וליצור מפתח API. לאחר שיש לכם את המפתח, תוכלו למלא את המשתנה `OPENAI_API_KEY` בקובץ `.env`.

## הגדרת Hugging Face: מהפרופיל

הטוקן של Hugging Face שלכם נמצא בפרופיל תחת [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). אל תפרסמו או תשתפו אותם בפומבי. במקום זאת, צרו טוקן חדש לשימוש בפרויקט זה והעתיקו אותו לקובץ `.env` תחת המשתנה `HUGGING_FACE_API_KEY`. _הערה:_ טכנית זה לא מפתח API אך משמש לאימות ולכן אנו שומרים על השם הזה למען עקביות.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי אדם. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->