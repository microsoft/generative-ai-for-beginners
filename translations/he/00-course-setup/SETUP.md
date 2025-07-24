<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:33:08+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "he"
}
-->
# הגדרת סביבת הפיתוח שלך

הקמנו את המאגר והקורס הזה עם [מיכל פיתוח](https://containers.dev?WT.mc_id=academic-105485-koreyst) שמכיל סביבת ריצה אוניברסלית התומכת בפיתוח ב-Python3, .NET, Node.js ו-Java. התצורה הרלוונטית מוגדרת בקובץ `devcontainer.json` שנמצא בתיקיית `.devcontainer/` שבשורש המאגר.

כדי להפעיל את מיכל הפיתוח, הפעל אותו ב-[GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (לסביבת ריצה בענן) או ב-[Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (לסביבת ריצה מקומית במחשב). קרא [את התיעוד הזה](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) לפרטים נוספים על אופן פעולת מיכלי הפיתוח בתוך VS Code.

> [!TIP]  
> אנו ממליצים להשתמש ב-GitHub Codespaces להתחלה מהירה עם מינימום מאמץ. הוא מספק [מכסת שימוש חינמית נדיבה](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) לחשבונות אישיים. הגדר [זמני הפסקה](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) לעצירת או מחיקת codespaces לא פעילות כדי למקסם את השימוש במכסה.

## 1. ביצוע משימות

לכל שיעור יהיו משימות _אופציונליות_ שעשויות להיות זמינות באחת או יותר משפות התכנות הבאות: Python, .NET/C#, Java ו-JavaScript/TypeScript. בסעיף זה תמצא הנחיות כלליות לביצוע המשימות הללו.

### 1.1 משימות Python

משימות Python מסופקות כיישומים (`.py` קבצים) או מחברות Jupyter (`.ipynb` קבצים).  
- כדי להריץ את המחברת, פתח אותה ב-Visual Studio Code, לחץ על _Select Kernel_ (למעלה מימין) ובחר באפשרות Python 3 המוגדרת כברירת מחדל. כעת תוכל ללחוץ על _Run All_ כדי להריץ את כל התאים במחברת.  
- כדי להריץ יישומי Python משורת הפקודה, עקוב אחרי ההוראות הספציפיות למשימה כדי לוודא שאתה בוחר את הקבצים הנכונים ומספק את הפרמטרים הנדרשים.

## 2. הגדרת ספקים

משימות **עשויות** להיות מוגדרות לעבודה מול פריסות של מודלים גדולים לשפה (LLM) דרך ספק שירות נתמך כמו OpenAI, Azure או Hugging Face. ספקים אלו מספקים _נקודת קצה מאוחסנת_ (API) שניתן לגשת אליה בצורה תכנותית עם האישורים הנכונים (מפתח API או טוקן). בקורס זה נדון בספקים הבאים:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) עם מגוון דגמים כולל סדרת GPT המרכזית.  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) לדגמי OpenAI עם דגש על מוכנות ארגונית  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) לדגמים בקוד פתוח ושרת אינפרנס

**תצטרך להשתמש בחשבונות שלך לתרגילים אלו**. המשימות הן אופציונליות, כך שתוכל לבחור להגדיר אחד, את כולם - או אף אחד - מהספקים בהתאם לתחומי העניין שלך. הנה כמה הנחיות להרשמה:

| הרשמה | עלות | מפתח API | Playground | הערות |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [תמחור](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [מבוסס פרויקט](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [ללא קוד, ווב](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | דגמים רבים זמינים |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [תמחור](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [התחלה מהירה SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [התחלה מהירה Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [יש להגיש בקשה מראש לגישה](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [תמחור](https://huggingface.co/pricing) | [טוקני גישה](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [ל-Hugging Chat יש דגמים מוגבלים](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

עקוב אחרי ההוראות למטה כדי _להגדיר_ את המאגר הזה לשימוש עם ספקים שונים. משימות שדורשות ספק מסוים יכילו אחת מהתוויות האלו בשם הקובץ:  
 - `aoai` - דורש נקודת קצה ומפתח של Azure OpenAI  
 - `oai` - דורש נקודת קצה ומפתח של OpenAI  
 - `hf` - דורש טוקן של Hugging Face

תוכל להגדיר אחד, אף אחד או את כולם. משימות רלוונטיות פשוט יזרקו שגיאה אם האישורים חסרים.

### 2.1 יצירת קובץ `.env`

אנו מניחים שקראת כבר את ההנחיות למעלה ונרשמת אצל הספק הרלוונטי, וקיבלת את האישורים הדרושים (API_KEY או טוקן). במקרה של Azure OpenAI, אנו מניחים שיש לך גם פריסה תקפה של שירות Azure OpenAI (נקודת קצה) עם לפחות דגם GPT אחד לפריסת שיחות.

השלב הבא הוא להגדיר את **משתני הסביבה המקומיים** שלך כך:

1. חפש בתיקיית השורש קובץ בשם `.env.copy` שצריך להכיל תוכן דומה לזה:

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

2. העתק את הקובץ ל-`.env` באמצעות הפקודה הבאה. קובץ זה נמצא ב-gitignore, כך שהסודות נשמרים בטוחים.

   ```bash
   cp .env.copy .env
   ```

3. מלא את הערכים (החלף את הממלאים בצד ימין של `=`) כפי שמתואר בסעיף הבא.

3. (אופציונלי) אם אתה משתמש ב-GitHub Codespaces, יש לך אפשרות לשמור את משתני הסביבה כסודות של Codespaces המשויכים למאגר זה. במקרה כזה, לא תצטרך להגדיר קובץ .env מקומי. **עם זאת, שים לב שאפשרות זו פועלת רק אם אתה משתמש ב-GitHub Codespaces.** אם אתה משתמש ב-Docker Desktop, עדיין תצטרך להגדיר את קובץ ה-.env.

### 2.2 מילוי קובץ `.env`

בוא נסתכל בקצרה על שמות המשתנים כדי להבין מה הם מייצגים:

| משתנה | תיאור |
| :--- | :--- |
| HUGGING_FACE_API_KEY | זהו טוקן הגישה של המשתמש שהגדרת בפרופיל שלך |
| OPENAI_API_KEY | זהו מפתח האישור לשימוש בשירות עבור נקודות קצה שאינן Azure OpenAI |
| AZURE_OPENAI_API_KEY | זהו מפתח האישור לשימוש בשירות Azure OpenAI |
| AZURE_OPENAI_ENDPOINT | זו נקודת הקצה של משאב Azure OpenAI שהופעל |
| AZURE_OPENAI_DEPLOYMENT | זו נקודת הקצה לפריסת דגם _יצירת טקסט_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | זו נקודת הקצה לפריסת דגם _הטמעת טקסט_ |
| | |

הערה: שני המשתנים האחרונים של Azure OpenAI משקפים דגם ברירת מחדל להשלמת שיחה (יצירת טקסט) ולחיפוש וקטורי (הטמעות) בהתאמה. ההוראות להגדרתם יופיעו במשימות הרלוונטיות.

### 2.3 הגדרת Azure: מהפורטל

ערכי נקודת הקצה והמפתח של Azure OpenAI יימצאו ב-[פורטל Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), אז נתחיל שם.

1. עבור ל-[פורטל Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
1. לחץ על האפשרות **Keys and Endpoint** בסרגל הצד (תפריט משמאל).  
1. לחץ על **Show Keys** - תראה את הפריטים הבאים: KEY 1, KEY 2 ו-Endpoint.  
1. השתמש בערך KEY 1 עבור AZURE_OPENAI_API_KEY  
1. השתמש בערך Endpoint עבור AZURE_OPENAI_ENDPOINT

כעת, נצטרך את נקודות הקצה לדגמים הספציפיים שהפעלנו.

1. לחץ על האפשרות **Model deployments** בסרגל הצד (תפריט משמאל) עבור משאב Azure OpenAI.  
1. בדף היעד, לחץ על **Manage Deployments**

זה יוביל אותך לאתר Azure OpenAI Studio, שם נמצא את הערכים הנוספים כפי שמתואר למטה.

### 2.4 הגדרת Azure: מהסטודיו

1. עבור ל-[Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **מהמשאב שלך** כפי שתואר למעלה.  
1. לחץ על לשונית **Deployments** (סרגל צד, שמאל) כדי לראות את הדגמים המופעלים כרגע.  
1. אם הדגם הרצוי לא מופעל, השתמש ב-**Create new deployment** כדי להפעילו.  
1. תזדקק לדגם _יצירת טקסט_ - אנו ממליצים על: **gpt-35-turbo**  
1. תזדקק לדגם _הטמעת טקסט_ - אנו ממליצים על **text-embedding-ada-002**

כעת עדכן את משתני הסביבה כך שישקפו את שם ה_פריסה_ (Deployment name) שהשתמשת בו. בדרך כלל זה יהיה אותו שם כמו הדגם אלא אם שינית אותו במפורש. לדוגמה, ייתכן שיהיה לך:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**אל תשכח לשמור את קובץ ה-.env בסיום**. כעת תוכל לצאת מהקובץ ולחזור להוראות להרצת המחברת.

### 2.5 הגדרת OpenAI: מהפרופיל

מפתח ה-API של OpenAI שלך נמצא ב-[חשבון OpenAI שלך](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). אם אין לך אחד, תוכל להירשם וליצור מפתח API. לאחר שיש לך את המפתח, תוכל למלא את המשתנה `OPENAI_API_KEY` בקובץ `.env`.

### 2.6 הגדרת Hugging Face: מהפרופיל

הטוקן של Hugging Face שלך נמצא בפרופיל שלך תחת [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). אל תפרסם או תשתף אותם בפומבי. במקום זאת, צור טוקן חדש לשימוש בפרויקט זה והעתק אותו לקובץ `.env` תחת המשתנה `HUGGING_FACE_API_KEY`. _הערה:_ טכנית זה לא מפתח API, אך הוא משמש לאימות ולכן אנו שומרים על השם הזה למען עקביות.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.