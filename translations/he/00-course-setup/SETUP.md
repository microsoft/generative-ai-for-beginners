<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:53:16+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "he"
}
-->
# הגדר את סביבת הפיתוח שלך

הגדרנו את המאגר ואת הקורס הזה עם [מיכל פיתוח](https://containers.dev?WT.mc_id=academic-105485-koreyst) שיש לו סביבת הרצה אוניברסלית שתומכת בפיתוח ב-Python3, .NET, Node.js ו-Java. התצורה הקשורה מוגדרת בקובץ `devcontainer.json` שנמצא בתיקיית `.devcontainer/` בשורש המאגר הזה.

כדי להפעיל את מיכל הפיתוח, הפעל אותו ב-[GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (לסביבת הרצה בענן) או ב-[Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (לסביבת הרצה במכשיר מקומי). קרא [את התיעוד הזה](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) לפרטים נוספים על איך מיכלי פיתוח עובדים בתוך VS Code.

> [!TIP]  
> אנו ממליצים להשתמש ב-GitHub Codespaces להתחלה מהירה עם מינימום מאמץ. הוא מספק [מכסת שימוש חינמית נדיבה](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) לחשבונות אישיים. הגדר [הפסקות](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) כדי להפסיק או למחוק קודים לא פעילים כדי למקסם את השימוש במכסה שלך.

## 1. ביצוע משימות

כל שיעור יכלול משימות _אופציונליות_ שעשויות להיות מסופקות באחת או יותר משפות תכנות כולל: Python, .NET/C#, Java ו-JavaScript/TypeScript. חלק זה מספק הנחיות כלליות לביצוע המשימות הללו.

### 1.1 משימות Python

משימות Python מסופקות או כאפליקציות (קבצי `.py`) או מחברות Jupyter (קבצי `.ipynb`).
- כדי להריץ את המחברת, פתח אותה ב-Visual Studio Code ואז לחץ על _Select Kernel_ (בפינה העליונה הימנית) ובחר באפשרות Python 3 המוצגת כברירת מחדל. כעת תוכל ללחוץ על _Run All_ כדי להפעיל את המחברת.
- כדי להריץ אפליקציות Python משורת הפקודה, עקוב אחר ההוראות הספציפיות למשימה כדי לוודא שאתה בוחר את הקבצים הנכונים ומספק את הפרמטרים הנדרשים.

## 2. הגדרת ספקים

ייתכן שמשימות **עשויות** גם להיות מוגדרות לעבודה מול פריסות של מודלים של שפה גדולה (LLM) אחד או יותר דרך ספק שירות נתמך כמו OpenAI, Azure או Hugging Face. אלה מספקים _נקודת קצה מתארחת_ (API) שניתן לגשת אליה באופן תכנותי עם האישורים הנכונים (מפתח API או טוקן). בקורס זה, אנו דנים בספקים הבאים:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) עם מודלים מגוונים כולל סדרת ה-GPT המרכזית.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) עבור מודלים של OpenAI עם מוכנות לארגון במוקד.
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) עבור מודלים בקוד פתוח ושרת חיזוי.

**תצטרך להשתמש בחשבונות שלך עבור תרגילים אלה**. המשימות הן אופציונליות כך שתוכל לבחור להגדיר אחד, את כולם - או אף אחד - מהספקים בהתאם לתחומי העניין שלך. הנה כמה הנחיות להרשמה:

| הרשמה | עלות | מפתח API | סביבת עבודה | הערות |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [תמחור](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [מבוסס פרויקט](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [ללא קוד, אינטרנט](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | זמינות מודלים מרובים |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [תמחור](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [התחלה מהירה של SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [התחלה מהירה של סטודיו](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [יש להגיש בקשה מראש לגישה](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [תמחור](https://huggingface.co/pricing) | [אסימוני גישה](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [ל-Hugging Chat יש מודלים מוגבלים](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

עקוב אחר ההוראות למטה כדי _להגדיר_ מאגר זה לשימוש עם ספקים שונים. משימות שדורשות ספק ספציפי יכילו אחד מהתגים הללו בשם הקובץ שלהן:
 - `aoai` - דורש נקודת קצה ומפתח של Azure OpenAI
 - `oai` - דורש נקודת קצה ומפתח של OpenAI
 - `hf` - דורש טוקן של Hugging Face

אתה יכול להגדיר אחד, אף אחד, או את כל הספקים. משימות קשורות פשוט ייכשלו אם יחסר להם האישורים הנדרשים.

### 2.1 יצירת קובץ `.env`

אנו מניחים שכבר קראת את ההנחיות לעיל ונרשמת אצל הספק הרלוונטי, וקיבלת את האישורים הנדרשים לאימות (מפתח API או טוקן). במקרה של Azure OpenAI, אנו מניחים שיש לך גם פריסה תקפה של שירות Azure OpenAI (נקודת קצה) עם לפחות מודל GPT אחד לפריסת השלמת שיחה.

השלב הבא הוא להגדיר את **משתני הסביבה המקומיים** שלך כדלקמן:

1. חפש בתיקיית השורש קובץ `.env.copy` שצריך להכיל תוכן כזה:

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

2. העתק את הקובץ ל-`.env` באמצעות הפקודה הבאה. קובץ זה _gitignore-d_, שומר על סודות בטוחים.

   ```bash
   cp .env.copy .env
   ```

3. מלא את הערכים (החלף את המילויים בצד הימני של `=`) כפי שמתואר בסעיף הבא.

3. (אפשרות) אם אתה משתמש ב-GitHub Codespaces, יש לך אפשרות לשמור משתני סביבה כ- _Codespaces secrets_ המשויכים למאגר זה. במקרה זה, לא תצטרך להגדיר קובץ .env מקומי. **עם זאת, שים לב שאפשרות זו עובדת רק אם אתה משתמש ב-GitHub Codespaces.** תצטרך עדיין להגדיר את קובץ ה-.env אם אתה משתמש ב-Docker Desktop במקום.

### 2.2. מילוי קובץ `.env`

בואו נסתכל במהירות על שמות המשתנים כדי להבין מה הם מייצגים:

| משתנה  | תיאור  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | זהו טוקן הגישה למשתמש שהגדרת בפרופיל שלך |
| OPENAI_API_KEY | זהו מפתח האימות לשימוש בשירות עבור נקודות קצה של OpenAI שאינן של Azure |
| AZURE_OPENAI_API_KEY | זהו מפתח האימות לשימוש בשירות זה |
| AZURE_OPENAI_ENDPOINT | זו נקודת הקצה הפרוסה עבור משאב Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | זו נקודת הקצה לפריסת מודל _יצירת טקסט_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | זו נקודת הקצה לפריסת מודל _טקסט אמבדינגס_ |
| | |

הערה: שני המשתנים האחרונים של Azure OpenAI משקפים מודל ברירת מחדל להשלמת שיחה (יצירת טקסט) וחיפוש וקטורים (אמבדינגס) בהתאמה. הוראות להגדרתם יוגדרו במשימות הרלוונטיות.

### 2.3 הגדרת Azure: מהפורטל

ערכי נקודת הקצה והמפתח של Azure OpenAI יימצאו ב-[פורטל Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) אז נתחיל שם.

1. עבור ל-[פורטל Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. לחץ על האפשרות **Keys and Endpoint** בסרגל הצד (תפריט משמאל).
1. לחץ על **Show Keys** - אתה אמור לראות את הדברים הבאים: KEY 1, KEY 2 ו-EndPoint.
1. השתמש בערך KEY 1 עבור AZURE_OPENAI_API_KEY
1. השתמש בערך Endpoint עבור AZURE_OPENAI_ENDPOINT

לאחר מכן, אנו צריכים את נקודות הקצה עבור המודלים הספציפיים שהפרסנו.

1. לחץ על האפשרות **Model deployments** בסרגל הצד (תפריט שמאלי) עבור משאב Azure OpenAI.
1. בדף היעד, לחץ על **Manage Deployments**

זה יוביל אותך לאתר האינטרנט של Azure OpenAI Studio, שם נמצא את הערכים האחרים כפי שמתואר להלן.

### 2.4 הגדרת Azure: מהסטודיו

1. נווט ל-[Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **מהמשאב שלך** כפי שתואר לעיל.
1. לחץ על הכרטיסייה **Deployments** (סרגל צדדי, שמאלי) כדי להציג מודלים שכרגע פרוסים.
1. אם המודל הרצוי שלך לא פרוס, השתמש ב-**Create new deployment** כדי לפרוס אותו.
1. תצטרך מודל _יצירת טקסט_ - אנו ממליצים: **gpt-35-turbo**
1. תצטרך מודל _טקסט אמבדינג_ - אנו ממליצים **text-embedding-ada-002**

כעת עדכן את משתני הסביבה כך שישקפו את _שם הפריסה_ שבו השתמשת. זה יהיה בדרך כלל זהה לשם המודל אלא אם שינית אותו במפורש. לדוגמה, ייתכן שיהיה לך:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**אל תשכח לשמור את קובץ ה-.env כשסיימת**. כעת תוכל לצאת מהקובץ ולחזור להוראות להפעלת המחברת.

### 2.5 הגדרת OpenAI: מהפרופיל

ניתן למצוא את מפתח ה-API של OpenAI שלך ב-[חשבון OpenAI שלך](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). אם אין לך אחד, תוכל להירשם לחשבון וליצור מפתח API. לאחר שיש לך את המפתח, תוכל להשתמש בו כדי למלא את המשתנה `OPENAI_API_KEY` בקובץ `.env`.

### 2.6 הגדרת Hugging Face: מהפרופיל

ניתן למצוא את הטוקן של Hugging Face בפרופיל שלך תחת [אסימוני גישה](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). אל תפרסם או שתף אותם בפומבי. במקום זאת, צור טוקן חדש לשימוש בפרויקט זה והעתק אותו לקובץ `.env` תחת המשתנה `HUGGING_FACE_API_KEY`. _הערה:_ זה לא ממש מפתח API אבל משמש לאימות, ולכן אנו שומרים על אותו שם לשם עקביות.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, אנא היו מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום אנושי מקצועי. אנו לא נושאים באחריות על אי הבנות או פירושים שגויים הנובעים משימוש בתרגום זה.