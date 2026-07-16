# AGENTS.md

## סקירה כללית של הפרויקט

מאגר זה מכיל תכנית לימודים מקיפה בעלת 21 שיעורים המלמדת יסודות של בינה מלאכותית יוצרת ופיתוח יישומים. הקורס מיועד למתחילים וכולל הכל, מרעיונות בסיסיים ועד לבניית יישומים מוכנים לייצור.

**טכנולוגיות מרכזיות:**
- Python 3.9+ עם ספריות: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript עם Node.js וספריות: `openai` (Azure OpenAI דרך נקודת קצה v1 + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- שירות Azure OpenAI, API של OpenAI, ומודלים של Microsoft Foundry (GitHub Models יסגר בסוף יולי 2026)
- מחברות Jupyter ללמידה אינטראקטיבית
- מכולות פיתוח לסביבת פיתוח עקבית

**מבנה המאגר:**
- 21 תיקיות שיעורים ממוספרות (00-21) המכילות README, דוגמאות קוד, ומשימות
- יישומים מרובים: דוגמאות ב-Python, TypeScript, ולעיתים גם דוגמאות ב-.NET
- תיקיית תרגומים עם מעל 40 גרסאות שפה
- קונפיגורציה מרכזית דרך קובץ `.env` (שימוש בתבנית `.env.copy`)

## פקודות התקנה

### התקנת המאגר הראשוני

```bash
# שכפל את המאגר
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# העתק את תבנית הסביבה
cp .env.copy .env
# ערוך את .env עם מפתחות ה-API והנקודות הקצה שלך
```

### הגדרת סביבה ב-Python

```bash
# ליצור סביבה וירטואלית
python3 -m venv venv

# להפעיל את הסביבה הוירטואלית
# במאק או לינוקס:
source venv/bin/activate
# בוינדוס:
venv\Scripts\activate

# להתקין את התלויות
pip install -r requirements.txt
```

### הגדרת Node.js/TypeScript

```bash
# התקן תלותיות ברמת השורש (לכלי תיעוד)
npm install

# עבור לדוגמאות TypeScript של שיעור בודד, נווט לשיעור הספציפי:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### הגדרת מכולת פיתוח (מומלץ)

המאגר כולל קובץ קונפיגורציה `.devcontainer` לשימוש ב-GitHub Codespaces או VS Code עם תוספת Dev Containers:

1. פתח את המאגר ב-GitHub Codespaces או ב-VS Code עם הרחבת Dev Containers
2. מכולת הפיתוח תבצע אוטומטית:
   - התקנת תלותיות Python מתוך `requirements.txt`
   - הרצת סקריפט לאחר יצירה (`.devcontainer/post-create.sh`)
   - הקמת kerner ל-Jupyter

## תהליך הפיתוח

### משתני סביבה

כל השיעורים הדורשים גישה ל-API משתמשים במשתני סביבה המוגדרים בקובץ `.env`:

- `OPENAI_API_KEY` - עבור OpenAI API
- `AZURE_OPENAI_API_KEY` - עבור Azure OpenAI ב-Microsoft Foundry (שירות Azure OpenAI הוא כעת חלק מ-Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL של נקודת הקצה של Azure OpenAI (נקודת קצה של Foundry)
- `AZURE_OPENAI_DEPLOYMENT` - שם פריסת מודל השלמת שיחה
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - שם פריסת מודל ההטמעה
- `AZURE_OPENAI_API_VERSION` - גרסת ה-API (ברירת מחדל: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - עבור מודלים של Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - נקודת הקצה של מודלים ב-Microsoft Foundry (קטלוג מודלים מרובת ספקים)
- `AZURE_INFERENCE_CREDENTIAL` - מפתח API של Microsoft Foundry Models (מחליף את `GITHUB_TOKEN` שייצא)

### הפעלת דוגמאות Python

```bash
# נווט לתיקיית השיעור
cd 06-text-generation-apps/python

# הרץ סקריפט פייתון
python aoai-app.py
```

### הפעלת דוגמאות TypeScript

```bash
# נווט לספריית האפליקציה של TypeScript
cd 06-text-generation-apps/typescript/recipe-app

# בנה את קוד ה-TypeScript
npm run build

# הרץ את האפליקציה
npm start
```

### הפעלת מחברות Jupyter

```bash
# התחלת Jupyter בשורש המאגר
jupyter notebook

# או להשתמש ב-VS Code עם הרחבת Jupyter
```

### עבודה עם סוגי שיעורים שונים

- **שיעורי "למד"**: התמקדות בתיעוד README.md ובמושגים
- **שיעורי "בנה"**: כוללים דוגמאות קוד עובדות ב-Python ו-TypeScript
- בכל שיעור יש README.md עם תיאוריה, הסברים של הקוד, וקישורים לתוכן וידאו

## הנחיות לסגנון הקוד

### Python

- השתמש ב-`python-dotenv` לניהול משתני סביבה
- ייבא את ספריית `openai` לאינטראקציות עם ה-API
- השתמש ב-`pylint` ללינטינג (בחלק מהדוגמאות מופיע `# pylint: disable=all` להקלות)
- עקוב אחרי קונבנציות שמות של PEP 8
- אחסן אישורי API בקובץ `.env`, לעולם לא בקוד

### TypeScript

- השתמש בחבילת `dotenv` עבור משתני הסביבה
- קונפיגורציית TypeScript ב-`tsconfig.json` לכל אפליקציה
- השתמש בחבילת `openai` עבור Azure OpenAI (הפנה את הקליינט לנקודת הקצה `/openai/v1/` וקרא ל-`client.responses.create`); השתמש ב-`@azure-rest/ai-inference` עבור Microsoft Foundry Models
- השתמש ב-`nodemon` לפיתוח עם טעינה אוטומטית מחדש
- רוץ בניה לפני הפעלה: `npm run build` ואז `npm start`

### קונבנציות כלליות

- שמור דוגמאות קוד פשוטות וחינוכיות
- הוסף הערות המסבירות מושגים מרכזיים
- הקוד של כל שיעור אמור להיות עצמאי והרצתו אמורה להיות אפשרית
- השתמש בשמות עקביים: קידומת `aoai-` עבור Azure OpenAI, `oai-` עבור OpenAI API, `githubmodels-` עבור Microsoft Foundry Models (קידומת ישנה שנשמרה מתקופת GitHub Models)

## הנחיות לתיעוד

### סגנון Markdown

- כל כתובות ה-URL צריכות להיות בתוך פורמט `[text](../../url)` ללא רווחים מיותרים
- קישורים יחסיים צריכים להתחיל ב-`./` או `../`
- כל הקישורים לדומיינים של מיקרוסופט חייבים לכלול מזהה מעקב: `?WT.mc_id=academic-105485-koreyst`
- אין להשתמש במקומות ספציפיים למדינה בכתובות URL (הימנע מ-`/en-us/`)
- תמונות נשמרות בתיקיית `./images` עם שמות תיאוריים
- השתמש בתווים באנגלית, מספרים ומקפים בשמות הקבצים

### תמיכה בתרגום

- המאגר תומך ב-40+ שפות באמצעות GitHub Actions אוטומטיים
- תרגומים נשמרים בתיקיית `translations/`
- אין להגיש תרגומים חלקיים
- תרגום ממוחשב אינו מתקבל
- תמונות מתורגמות נשמרות בתיקיית `translated_images/`

## בדיקות ואימות

### בדיקות לפני הגשה

מאגר זה משתמש ב-GitHub Actions לאימות. לפני הגשת PR:

1. **בדוק קישורי Markdown**:
   ```bash
   # זרימת העבודה validate-markdown.yml בודקת:
   # - נתיבים יחסיים שבורים
   # - מזהי מעקב חסרים בנתיבים
   # - מזהי מעקב חסרים בכתובות URL
   # - כתובות URL עם מיקום מדינה
   # - כתובות URL חיצוניות שבורות
   ```

2. **בדיקות ידניות**:
   - בדוק דוגמאות Python: הפעל venv והריץ סקריפטים
   - בדוק דוגמאות TypeScript: `npm install`, `npm run build`, `npm start`
   - ודא שמשתני הסביבה מוגדרים נכונה
   - בדוק שמפתחות API פועלים עם דוגמאות הקוד

3. **דוגמאות קוד**:
   - ודא שכל הקוד רץ ללא שגיאות
   - בדוק עם Azure OpenAI ו-OpenAI API כאשר רלוונטי
   - ודא שדוגמאות עובדות עם Microsoft Foundry Models במקומות שמתמכים

### אין בדיקות אוטומטיות

זהו מאגר חינוכי שמתרכז במדריכים ודוגמאות. אין בדיקות יחידה או בדיקות אינטגרציה להפעלה. האימות נעשה בעיקר על ידי:
- בדיקות ידניות של דוגמאות הקוד
- GitHub Actions לאימות Markdown
- ביקורת קהילתית על התוכן החינוכי

## הנחיות להעלאת בקשות משיכה

### לפני ההגשה

1. בדוק שינויים בקוד גם ב-Python וגם ב-TypeScript כאשר אפשרי
2. הרץ אימות Markdown (מופעל אוטומטית על PR)
3. ודא שמזהי מעקב קיימים בכל כתובות ה-Microsoft
4. בדוק שקישורים יחסיים תקינים
5. ודא שהתמונות מופנות כראוי

### פורמט כותרת PR

- השתמש בכותרות מתארות: `[Lesson 06] תיקון שגיאת הקלדה בדוגמת Python` או `עדכן README לשיעור 08`
- התייחס למספרי בעיות כאשר רלוונטי: `Fixes #123`

### תיאור PR

- הסבר מה שונה ולמה
- הוסף קישורים לבעיות קשורות
- עבור שינויים בקוד, פרט אילו דוגמאות נבדקו
- עבור PR תרגום, כללו את כל הקבצים לתרגום מלא

### דרישות לתרומה

- חתום על Microsoft CLA (אוטומטי ב-PR הראשון)
- בצע Fork למאגר לחשבונך לפני ביצוע שינויים
- בקשה אחת לכל שינוי לוגי (לא לשלב תיקונים לא קשורים)
- שמור את ה-PR ממוקד וקטן כשאפשרי

## תהליכים נפוצים

### הוספת דוגמת קוד חדשה

1. נווט לתיקיית השיעור הרלוונטית
2. צור דוגמה בתיקיית `python/` או `typescript/` המשנית
3. עקוב אחרי שיטת השמות: `{provider}-{example-name}.{py|ts|js}`
4. בדוק עם אישורי API אמיתיים
5. תעד כל משתנה סביבה חדש ב-README של השיעור

### עדכון התיעוד

1. ערוך README.md בתיקיית השיעור
2. עקוב אחרי הנחיות Markdown (מזהי מעקב, קישורים יחסיים)
3. עדכון התרגומים מנוהל על ידי GitHub Actions (לא לערוך ידנית)
4. בדוק שכל הקישורים תקינים

### עבודה עם מכולות פיתוח

1. המאגר כולל `.devcontainer/devcontainer.json`
2. סקריפט לאחר יצירה מתקין אוטומטית תלותיות Python
3. הרחבות ל-Python ו-Jupyter מוגדרות מראש
4. הסביבה מבוססת על `mcr.microsoft.com/devcontainers/universal:2.11.2`

## פריסה ופרסום

זהו מאגר למידה - אין תהליך פריסה. תכנית הלימודים נגישה באמצעות:

1. **מאגר GitHub**: גישה ישירה לקוד ולתיעוד
2. **GitHub Codespaces**: סביבת פיתוח מיידית עם הגדרות מוכנות מראש
3. **Microsoft Learn**: התוכן עשוי להיות משודר לפלטפורמת הלמידה הרשמית
4. **docsify**: אתר תיעוד הנבנה מ-Markdown (ראה `docsifytopdf.js` ו-`package.json`)

### בניית אתר תיעוד

```bash
# ליצור PDF מהתיעוד (אם נדרש)
npm run convert
```

## פתרון בעיות

### תקלות נפוצות

**שגיאות ייבוא ב-Python**:
- ודא שסביבת הפיתוח הווירטואלית מופעלת
- הרץ `pip install -r requirements.txt`
- בדוק שגרסת Python היא 3.9+

**שגיאות בניית TypeScript**:
- הרץ `npm install` בתיקיית האפליקציה הספציפית
- בדוק שתוכנת Node.js תואמת
- נקה את תיקיית `node_modules` והתקן מחדש במידת הצורך

**שגיאות אימות API**:
- ודא שקובץ `.env` קיים ושיש בו ערכים נכונים
- בדוק שמפתחות ה-API תקפים ולא פגו תוקף
- ודא ש-URLs של נקודות הקצה נכונים לאזור שלך

**משתני סביבה חסרים**:
- העתק `.env.copy` ל-`.env`
- מלא את כל הערכים הדרושים עבור השיעור שבו אתה עובד
- הפעל מחדש את האפליקציה לאחר עדכון `.env`

## משאבים נוספים

- [מדריך התקנת הקורס](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [הנחיות לתרומה](./CONTRIBUTING.md)
- [קוד ההתנהגות](./CODE_OF_CONDUCT.md)
- [מדיניות אבטחה](./SECURITY.md)
- [שרת דיסקורד של Azure AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [אוסף דוגמאות קוד מתקדמות](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## הערות ספציפיות לפרויקט

- זהו **מאגר חינוכי** המתמקד בלמידה, לא בקוד לשימוש ייצור
- הדוגמאות פשוטות במכוון וממוקדות בלימוד מושגים
- איכות הקוד מאוזנת עם בהירות חינוכית
- כל שיעור עצמאי וניתן להשלים אותו בנפרד
- המאגר תומך במספר ספקי API: Azure OpenAI, OpenAI, Microsoft Foundry Models, וספקים לא מקוונים כגון Foundry Local ו-Ollama
- התוכן רב-לשוני עם תהליכי תרגום אוטומטיים
- קהילה פעילה בדיסקורד לשאלות ותמיכה

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->