<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T17:57:37+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "he"
}
-->
# בחירת והגדרת ספק LLM 🔑

ניתן להגדיר משימות לעבוד מול פריסות של מודלים גדולים (LLM) דרך ספקי שירות נתמכים כמו OpenAI, Azure או Hugging Face. ספקים אלו מספקים _נקודת קצה מתארחת_ (API) שניתן לגשת אליה בתכנות עם האישורים המתאימים (מפתח API או טוקן). בקורס זה נדון בספקים הבאים:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) עם מגוון מודלים כולל סדרת GPT המרכזית.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) עבור מודלים של OpenAI עם דגש על מוכנות לארגונים
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) עבור מודלים בקוד פתוח ושרת הסקה

**יהיה עליכם להשתמש בחשבונות האישיים שלכם בתרגולים האלו**. המשימות הן רשות, כך שתוכלו לבחור להגדיר ספק אחד, את כולם – או אף אחד – לפי תחומי העניין שלכם. כמה הנחיות להרשמה:

| הרשמה | עלות | מפתח API | Playground | הערות |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [תמחור](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [מבוסס פרויקט](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [ללא קוד, בדפדפן](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | קיימים מספר מודלים |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [תמחור](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [התחלה מהירה עם SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [התחלה מהירה עם Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [חובה להגיש בקשה מראש לגישה](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [תמחור](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [ל-Hugging Chat יש מספר מודלים מוגבל](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

עקבו אחרי ההוראות למטה כדי _להגדיר_ את המאגר הזה לשימוש עם ספקים שונים. משימות שדורשות ספק מסוים יכילו אחד מהתגים האלו בשם הקובץ:

- `aoai` - דורש נקודת קצה ומפתח של Azure OpenAI
- `oai` - דורש נקודת קצה ומפתח של OpenAI
- `hf` - דורש טוקן של Hugging Face

ניתן להגדיר ספק אחד, אף אחד, או את כולם. משימות רלוונטיות פשוט ייכשלו אם יחסר אישור.

## יצירת קובץ `.env`

אנו מניחים שכבר קראתם את ההנחיות למעלה ונרשמתם לספק הרלוונטי, וקיבלתם את האישורים הנדרשים (API_KEY או טוקן). במקרה של Azure OpenAI, אנו מניחים שיש לכם גם פריסה תקפה של שירות Azure OpenAI (נקודת קצה) עם לפחות מודל GPT אחד לפריסת השלמת שיחה.

השלב הבא הוא להגדיר את **משתני הסביבה המקומיים** שלכם כך:

1. חפשו בתיקיית השורש קובץ בשם `.env.copy` שצריך להיראות כך:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. העתיקו את הקובץ ל-`.env` בעזרת הפקודה הבאה. קובץ זה _נמצא ב-.gitignore_, כך שהסודות נשמרים בטוחים.

   ```bash
   cp .env.copy .env
   ```

3. מלאו את הערכים (החליפו את המשתנים בצד ימין של ה-`=`) כפי שמוסבר בסעיף הבא.

4. (אופציונלי) אם אתם משתמשים ב-GitHub Codespaces, יש לכם אפשרות לשמור משתני סביבה כ-_Codespaces secrets_ המשויכים למאגר הזה. במקרה כזה, לא תצטרכו להגדיר קובץ .env מקומי. **שימו לב: אפשרות זו עובדת רק אם אתם משתמשים ב-GitHub Codespaces.** עדיין תצטרכו להגדיר קובץ .env אם תשתמשו ב-Docker Desktop.

## מילוי קובץ `.env`

בואו נסקור בקצרה את שמות המשתנים כדי להבין למה הם משמשים:

| משתנה  | תיאור  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | זהו טוקן הגישה שהגדרתם בפרופיל שלכם |
| OPENAI_API_KEY | זהו מפתח ההרשאה לשימוש בשירות עבור נקודות קצה של OpenAI שאינן Azure |
| AZURE_OPENAI_API_KEY | זהו מפתח ההרשאה לשימוש בשירות הזה |
| AZURE_OPENAI_ENDPOINT | זו נקודת הקצה שפרסתם עבור משאב Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | זו נקודת הקצה של פריסת מודל _הפקת טקסט_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | זו נקודת הקצה של פריסת מודל _הטמעת טקסט_ |
| | |

הערה: שני המשתנים האחרונים של Azure OpenAI משקפים מודל ברירת מחדל להשלמת שיחה (הפקת טקסט) ולחיפוש וקטורי (הטמעות) בהתאמה. הוראות להגדרתם יופיעו במשימות הרלוונטיות.

## הגדרת Azure: מהפורטל

ערכי נקודת הקצה והמפתח של Azure OpenAI יימצאו ב-[Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), אז נתחיל שם.

1. היכנסו ל-[Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. לחצו על האפשרות **Keys and Endpoint** בתפריט הצדדי (תפריט משמאל).
1. לחצו על **Show Keys** – תראו את KEY 1, KEY 2 ו-Endpoint.
1. השתמשו בערך של KEY 1 עבור AZURE_OPENAI_API_KEY
1. השתמשו בערך של Endpoint עבור AZURE_OPENAI_ENDPOINT

כעת נצטרך את נקודות הקצה של המודלים הספציפיים שפרסנו.

1. לחצו על האפשרות **Model deployments** בתפריט הצדדי (משמאל) עבור משאב Azure OpenAI.
1. בדף היעד, לחצו על **Manage Deployments**

זה ייקח אתכם לאתר Azure OpenAI Studio, שם נמצא את הערכים הנוספים כפי שמוסבר למטה.

## הגדרת Azure: מהסטודיו

1. עברו ל-[Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **מהמשאב שלכם** כפי שתואר למעלה.
1. לחצו על לשונית **Deployments** (תפריט צדדי, שמאלי) כדי לראות את המודלים שפרסתם.
1. אם המודל הרצוי לא נפרס, השתמשו ב-**Create new deployment** כדי לפרוס אותו.
1. תצטרכו מודל _text-generation_ – אנו ממליצים על: **gpt-35-turbo**
1. תצטרכו מודל _text-embedding_ – אנו ממליצים על **text-embedding-ada-002**

כעת עדכנו את משתני הסביבה כך שישקפו את _שם הפריסה_ בו השתמשתם. לרוב זה יהיה זהה לשם המודל אלא אם שיניתם אותו במפורש. לדוגמה, ייתכן שיהיה לכם:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**אל תשכחו לשמור את קובץ ה-.env בסיום**. כעת תוכלו לצאת מהקובץ ולחזור להוראות להרצת המחברת.

## הגדרת OpenAI: מהפרופיל

מפתח ה-API של OpenAI שלכם נמצא ב-[חשבון OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). אם אין לכם אחד, תוכלו להירשם וליצור מפתח API. לאחר שיש לכם את המפתח, השתמשו בו כדי למלא את המשתנה `OPENAI_API_KEY` בקובץ `.env`.

## הגדרת Hugging Face: מהפרופיל

הטוקן של Hugging Face שלכם נמצא בפרופיל תחת [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). אל תפרסמו או תשתפו אותו בפומבי. במקום זאת, צרו טוקן חדש לשימוש בפרויקט הזה והעתיקו אותו לקובץ `.env` תחת המשתנה `HUGGING_FACE_API_KEY`. _הערה:_ זה לא מפתח API טכנית, אבל הוא משמש לאימות ולכן שמרנו על השם הזה לצורך אחידות.

---

**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עשויים להכיל טעויות או אי-דיוקים. המסמך המקורי בשפתו המקורית הוא המקור הסמכותי. למידע קריטי, מומלץ לפנות לתרגום מקצועי על ידי אדם. איננו אחראים לכל אי-הבנה או פירוש שגוי הנובעים מהשימוש בתרגום זה.