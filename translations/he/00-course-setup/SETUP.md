<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:23:25+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "he"
}
-->
# הגדרת סביבת הפיתוח שלך

הגדרנו את המאגר והקורס הזה עם [מיכל פיתוח](https://containers.dev?WT.mc_id=academic-105485-koreyst) שמכיל סביבת ריצה אוניברסלית שיכולה לתמוך בפיתוח ב-Python3, .NET, Node.js ו-Java. התצורה הקשורה מוגדרת בקובץ `devcontainer.json` שנמצא בתיקיית `.devcontainer/` בשורש המאגר הזה.

כדי להפעיל את מיכל הפיתוח, הפעל אותו ב-[GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (לסביבת ריצה בענן) או ב-[Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (לסביבת ריצה במכשיר מקומי). קרא [תיעוד זה](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) לפרטים נוספים על איך מיכלי פיתוח עובדים בתוך VS Code.

> [!TIP]  
> אנו ממליצים להשתמש ב-GitHub Codespaces להתחלה מהירה עם מאמץ מינימלי. הוא מספק [מכסת שימוש חינמית נדיבה](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) לחשבונות אישיים. הגדר [הפסקות זמן](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) כדי להפסיק או למחוק קודים לא פעילים כדי למקסם את השימוש במכסה שלך.

## 1. ביצוע משימות

כל שיעור יכיל משימות _אופציונליות_ שעשויות להינתן בשפה אחת או יותר, כולל: Python, .NET/C#, Java ו-JavaScript/TypeScript. חלק זה מספק הנחיות כלליות הקשורות לביצוע המשימות הללו.

### 1.1 משימות Python

משימות Python ניתנות או כיישומים (קבצי `.py`) או מחברות Jupyter (קבצי `.ipynb`).
- כדי להפעיל את המחברת, פתח אותה ב-Visual Studio Code ואז לחץ על _Select Kernel_ (בפינה הימנית העליונה) ובחר באפשרות ברירת המחדל Python 3 המוצגת. כעת תוכל ללחוץ על _Run All_ כדי להפעיל את המחברת.
- כדי להפעיל יישומי Python משורת הפקודה, עקוב אחר ההוראות הספציפיות למשימה כדי לוודא שאתה בוחר את הקבצים הנכונים ומספק את הפרמטרים הנדרשים.

## 2. הגדרת ספקים

ייתכן שמשימות **יוגדרו** גם לעבודה מול פריסות של מודל שפה גדול (LLM) אחד או יותר באמצעות ספק שירות נתמך כמו OpenAI, Azure או Hugging Face. אלה מספקים _נקודת קצה מתארחת_ (API) שניתן לגשת אליה באופן תכנותי עם האישורים הנכונים (מפתח API או אסימון). בקורס זה, נדון בספקים הבאים:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) עם דגמים מגוונים כולל סדרת ה-GPT המרכזית.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) עבור דגמי OpenAI עם מוכנות ארגונית במוקד.
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) עבור דגמים קוד פתוח ושרת הסקת מסקנות.

**תצטרך להשתמש בחשבונות שלך לתרגילים אלה**. המשימות הן אופציונליות כך שתוכל לבחור להגדיר אחד, את כולם - או אף אחד מהספקים בהתאם לתחומי העניין שלך. כמה הנחיות לרישום:

| רישום | עלות | מפתח API | מגרש משחקים | הערות |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [תמחור](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [מבוסס פרויקט](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [ללא קוד, אינטרנט](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | מספר דגמים זמינים |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [תמחור](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [התחלה מהירה של SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [התחלה מהירה של סטודיו](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [חובה להגיש בקשה מראש לגישה](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [תמחור](https://huggingface.co/pricing) | [אסימוני גישה](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat מכיל דגמים מוגבלים](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

עקוב אחר ההוראות למטה כדי _להגדיר_ מאגר זה לשימוש עם ספקים שונים. משימות הדורשות ספק מסוים יכילו אחת מהתגיות הללו בשם הקובץ שלהן:
- `aoai` - דורש נקודת קצה של Azure OpenAI, מפתח
- `oai` - דורש נקודת קצה של OpenAI, מפתח
- `hf` - דורש אסימון של Hugging Face

תוכל להגדיר אחד, אף אחד, או את כל הספקים. משימות קשורות פשוט יציגו שגיאה בהיעדר אישורים.

### 2.1. צור קובץ `.env`

אנו מניחים שכבר קראת את ההנחיות לעיל ונרשמת עם הספק הרלוונטי, והשגת את האישורים הנדרשים לאימות (API_KEY או אסימון). במקרה של Azure OpenAI, אנו מניחים שיש לך גם פריסה תקפה של שירות Azure OpenAI (נקודת קצה) עם לפחות מודל GPT אחד פרוס להשלמת צ'אט.

השלב הבא הוא להגדיר את **משתני הסביבה המקומיים** שלך באופן הבא:

1. חפש בתיקיית השורש קובץ `.env.copy` שצריך לכלול תוכן כזה:

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

2. העתק את הקובץ ל-`.env` באמצעות הפקודה למטה. קובץ זה הוא _gitignore-d_, שומר על סודות בטוחים.

   ```bash
   cp .env.copy .env
   ```

3. מלא את הערכים (החלף את הממלאי בצד ימין של `=`) כפי שמתואר בסעיף הבא.

3. (אפשרות) אם אתה משתמש ב-GitHub Codespaces, יש לך אפשרות לשמור משתני סביבה כ_סודות של Codespaces_ המשויכים למאגר זה. במקרה כזה, לא תצטרך להגדיר קובץ .env מקומי. **עם זאת, שים לב שאפשרות זו פועלת רק אם אתה משתמש ב-GitHub Codespaces.** עדיין תצטרך להגדיר את קובץ ה-.env אם אתה משתמש ב-Docker Desktop במקום.

### 2.2. מלא את קובץ `.env`

בואו נסתכל במהירות על שמות המשתנים כדי להבין מה הם מייצגים:

| משתנה  | תיאור  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | זהו אסימון הגישה של המשתמש שהגדרת בפרופיל שלך |
| OPENAI_API_KEY | זהו מפתח האימות לשימוש בשירות עבור נקודות קצה שאינן של Azure OpenAI |
| AZURE_OPENAI_API_KEY | זהו מפתח האימות לשימוש בשירות זה |
| AZURE_OPENAI_ENDPOINT | זו נקודת הקצה הפרוסה עבור משאב Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | זהו נקודת הקצה של מודל _יצירת טקסט_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | זהו נקודת הקצה של מודל _הטמעת טקסט_ |
| | |

הערה: שני המשתנים האחרונים של Azure OpenAI משקפים מודל ברירת מחדל להשלמת צ'אט (יצירת טקסט) וחיפוש וקטורי (הטמעות) בהתאמה. הוראות להגדרתן יוגדרו במשימות הרלוונטיות.

### 2.3 הגדרת Azure: מהפורטל

ערכי נקודת הקצה והמפתח של Azure OpenAI יימצאו ב[פורטל Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) אז נתחיל שם.

1. עבור ל[פורטל Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. לחץ על האפשרות **Keys and Endpoint** בסרגל הצד (תפריט משמאל).
1. לחץ על **Show Keys** - אתה אמור לראות את הדברים הבאים: KEY 1, KEY 2 ו-Endpoint.
1. השתמש בערך KEY 1 עבור AZURE_OPENAI_API_KEY
1. השתמש בערך Endpoint עבור AZURE_OPENAI_ENDPOINT

כעת, אנו זקוקים לנקודות הקצה עבור הדגמים הספציפיים שהפרסנו.

1. לחץ על האפשרות **Model deployments** בסרגל הצד (תפריט שמאלי) עבור משאב Azure OpenAI.
1. בדף היעד, לחץ על **Manage Deployments**

זה יוביל אותך לאתר Azure OpenAI Studio, שם נמצא את הערכים האחרים כפי שמתואר למטה.

### 2.4 הגדרת Azure: מהסטודיו

1. נווט ל[Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **מהמשאב שלך** כפי שתואר לעיל.
1. לחץ על לשונית **Deployments** (סרגל צד, שמאל) כדי להציג דגמים שכרגע פרוסים.
1. אם המודל הרצוי שלך אינו פרוס, השתמש ב-**Create new deployment** כדי לפרוס אותו.
1. תזדקק למודל _יצירת טקסט_ - אנו ממליצים על: **gpt-35-turbo**
1. תזדקק למודל _הטמעת טקסט_ - אנו ממליצים על **text-embedding-ada-002**

כעת עדכן את משתני הסביבה כדי לשקף את _שם הפריסה_ שהשתמשת בו. זה בדרך כלל יהיה זהה לשם המודל אלא אם שינית אותו במפורש. אז, כדוגמה, ייתכן שיהיה לך:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**אל תשכח לשמור את קובץ ה-.env כאשר סיימת**. כעת תוכל לצאת מהקובץ ולחזור להוראות להפעלת המחברת.

### 2.5 הגדרת OpenAI: מהפרופיל

מפתח ה-API שלך ל-OpenAI ניתן למצוא בחשבון [OpenAI שלך](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). אם אין לך אחד, תוכל להירשם לחשבון וליצור מפתח API. ברגע שיש לך את המפתח, תוכל להשתמש בו כדי למלא את המשתנה `OPENAI_API_KEY` בקובץ `.env`.

### 2.6 הגדרת Hugging Face: מהפרופיל

האסימון שלך ל-Hugging Face ניתן למצוא בפרופיל שלך תחת [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). אל תפרסם או שתף את אלה בפומבי. במקום זאת, צור אסימון חדש לשימוש בפרויקט זה והעתק אותו לקובץ `.env` תחת המשתנה `HUGGING_FACE_API_KEY`. _הערה:_ טכנית זה לא מפתח API אבל הוא משמש לאימות כך שאנו שומרים על אותה מוסכמה לשם עקביות.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). בעוד אנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית יש להחשיב כמקור סמכותי. למידע קריטי, מומלץ תרגום מקצועי על ידי בני אדם. איננו אחראים לכל אי הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.