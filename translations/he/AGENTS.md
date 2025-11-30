<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:06:04+00:00",
  "source_file": "AGENTS.md",
  "language_code": "he"
}
-->
# AGENTS.md

## סקירת הפרויקט

מאגר זה מכיל תוכנית לימודים מקיפה בת 21 שיעורים המלמדת את יסודות הבינה המלאכותית הגנרטיבית ופיתוח יישומים. הקורס מיועד למתחילים ומכסה הכל, החל ממושגים בסיסיים ועד לבניית יישומים מוכנים לייצור.

**טכנולוגיות מרכזיות:**
- Python 3.9+ עם ספריות: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript עם Node.js וספריות: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- שירות Azure OpenAI, OpenAI API ודגמי GitHub
- Jupyter Notebooks ללמידה אינטראקטיבית
- Dev Containers לסביבת פיתוח עקבית

**מבנה המאגר:**
- 21 תיקיות שיעורים ממוספרות (00-21) המכילות קבצי README, דוגמאות קוד ומשימות
- יישומים מרובים: Python, TypeScript ולעיתים דוגמאות .NET
- תיקיית תרגומים עם גרסאות ב-40+ שפות
- קונפיגורציה מרכזית באמצעות קובץ `.env` (השתמש ב-`.env.copy` כתבנית)

## פקודות התקנה

### התקנה ראשונית של המאגר

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### התקנת סביבת Python

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### התקנת Node.js/TypeScript

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### התקנת Dev Container (מומלץ)

המאגר כולל קונפיגורציה `.devcontainer` עבור GitHub Codespaces או VS Code Dev Containers:

1. פתח את המאגר ב-GitHub Codespaces או VS Code עם הרחבת Dev Containers
2. Dev Container יתקין באופן אוטומטי:
   - תלות Python מתוך `requirements.txt`
   - יריץ סקריפט לאחר יצירה (`.devcontainer/post-create.sh`)
   - יגדיר את Jupyter kernel

## זרימת עבודה בפיתוח

### משתני סביבה

כל השיעורים הדורשים גישה ל-API משתמשים במשתני סביבה המוגדרים ב-`.env`:

- `OPENAI_API_KEY` - עבור OpenAI API
- `AZURE_OPENAI_API_KEY` - עבור שירות Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - כתובת URL של נקודת הקצה של Azure OpenAI
- `AZURE_OPENAI_DEPLOYMENT` - שם פריסת מודל השלמת שיחה
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - שם פריסת מודל הטמעה
- `AZURE_OPENAI_API_VERSION` - גרסת API (ברירת מחדל: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - עבור דגמי Hugging Face
- `GITHUB_TOKEN` - עבור דגמי GitHub

### הרצת דוגמאות Python

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### הרצת דוגמאות TypeScript

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### הרצת Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### עבודה עם סוגי שיעורים שונים

- **שיעורי "Learn"**: מתמקדים בתיעוד README.md ובמושגים
- **שיעורי "Build"**: כוללים דוגמאות קוד עובדות ב-Python וב-TypeScript
- לכל שיעור יש README.md עם תיאוריה, סקירות קוד וקישורים לתוכן וידאו

## הנחיות לסגנון קוד

### Python

- השתמש ב-`python-dotenv` לניהול משתני סביבה
- ייבא את ספריית `openai` לאינטראקציות API
- השתמש ב-`pylint` לבדיקת קוד (חלק מהדוגמאות כוללות `# pylint: disable=all` לפשטות)
- עקוב אחר מוסכמות השמות של PEP 8
- אחסן אישורי API בקובץ `.env`, לעולם לא בקוד

### TypeScript

- השתמש בחבילת `dotenv` עבור משתני סביבה
- קונפיגורציית TypeScript ב-`tsconfig.json` לכל אפליקציה
- השתמש ב-`@azure/openai` או `@azure-rest/ai-inference` עבור שירותי Azure
- השתמש ב-`nodemon` לפיתוח עם טעינה אוטומטית
- בנה לפני הרצה: `npm run build` ואז `npm start`

### מוסכמות כלליות

- שמור על דוגמאות קוד פשוטות וחינוכיות
- כלול הערות המסבירות מושגים מרכזיים
- קוד של כל שיעור צריך להיות עצמאי וניתן להרצה
- השתמש בשמות עקביים: `aoai-` עבור Azure OpenAI, `oai-` עבור OpenAI API, `githubmodels-` עבור דגמי GitHub

## הנחיות לתיעוד

### סגנון Markdown

- כל כתובות ה-URL חייבות להיות עטופות בפורמט `[text](../../url)` ללא רווחים נוספים
- קישורים יחסיים חייבים להתחיל ב-`./` או `../`
- כל הקישורים לדומיינים של Microsoft חייבים לכלול מזהה מעקב: `?WT.mc_id=academic-105485-koreyst`
- אין להשתמש בלוקאלים ספציפיים למדינה בכתובות URL (להימנע מ-`/en-us/`)
- תמונות מאוחסנות בתיקיית `./images` עם שמות תיאוריים
- השתמש בתווים באנגלית, מספרים ומקפים בשמות קבצים

### תמיכה בתרגום

- המאגר תומך ב-40+ שפות באמצעות GitHub Actions אוטומטי
- תרגומים מאוחסנים בתיקיית `translations/`
- אין להגיש תרגומים חלקיים
- תרגומים מכונה אינם מתקבלים
- תמונות מתורגמות מאוחסנות בתיקיית `translated_images/`

## בדיקות ואימות

### בדיקות לפני הגשה

מאגר זה משתמש ב-GitHub Actions לאימות. לפני הגשת PRs:

1. **בדוק קישורי Markdown**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **בדיקות ידניות**:
   - בדוק דוגמאות Python: הפעל venv והרץ סקריפטים
   - בדוק דוגמאות TypeScript: `npm install`, `npm run build`, `npm start`
   - ודא שמשתני הסביבה מוגדרים כראוי
   - בדוק שמפתחות API עובדים עם דוגמאות הקוד

3. **דוגמאות קוד**:
   - ודא שכל הקוד רץ ללא שגיאות
   - בדוק עם Azure OpenAI וגם OpenAI API כאשר רלוונטי
   - ודא שהדוגמאות עובדות עם דגמי GitHub כאשר נתמך

### אין בדיקות אוטומטיות

זהו מאגר חינוכי המתמקד במדריכים ודוגמאות. אין בדיקות יחידה או בדיקות אינטגרציה להרצה. האימות מתבצע בעיקר:
- בדיקות ידניות של דוגמאות קוד
- GitHub Actions לאימות Markdown
- סקירת תוכן חינוכי על ידי הקהילה

## הנחיות להגשת Pull Request

### לפני הגשה

1. בדוק שינויים בקוד גם ב-Python וגם ב-TypeScript כאשר רלוונטי
2. הרץ אימות Markdown (מופעל אוטומטית ב-PR)
3. ודא שמזהי מעקב קיימים בכל כתובות ה-URL של Microsoft
4. בדוק שקישורים יחסיים תקינים
5. ודא שהתמונות מתייחסות כראוי

### פורמט כותרת PR

- השתמש בכותרות תיאוריות: `[Lesson 06] Fix Python example typo` או `Update README for lesson 08`
- התייחס למספרי בעיות כאשר רלוונטי: `Fixes #123`

### תיאור PR

- הסבר מה שונה ולמה
- קישור לבעיות קשורות
- עבור שינויים בקוד, ציין אילו דוגמאות נבדקו
- עבור PRs של תרגום, כלול את כל הקבצים לתרגום מלא

### דרישות לתרומה

- חתום על Microsoft CLA (אוטומטי ב-PR הראשון)
- בצע Fork למאגר לחשבונך לפני ביצוע שינויים
- PR אחד לכל שינוי לוגי (אל תשלב תיקונים לא קשורים)
- שמור על PRs ממוקדים וקטנים כאשר אפשרי

## זרימות עבודה נפוצות

### הוספת דוגמת קוד חדשה

1. נווט לתיקיית השיעור המתאימה
2. צור דוגמה בתיקיית `python/` או `typescript/`
3. עקוב אחר מוסכמת השמות: `{provider}-{example-name}.{py|ts|js}`
4. בדוק עם אישורי API אמיתיים
5. תעד כל משתני סביבה חדשים ב-README של השיעור

### עדכון תיעוד

1. ערוך את README.md בתיקיית השיעור
2. עקוב אחר הנחיות Markdown (מזהי מעקב, קישורים יחסיים)
3. עדכון תרגומים מתבצע על ידי GitHub Actions (אל תערוך ידנית)
4. בדוק שכל הקישורים תקינים

### עבודה עם Dev Containers

1. המאגר כולל `.devcontainer/devcontainer.json`
2. סקריפט לאחר יצירה מתקין תלות Python באופן אוטומטי
3. הרחבות עבור Python ו-Jupyter מוגדרות מראש
4. הסביבה מבוססת על `mcr.microsoft.com/devcontainers/universal:2.11.2`

## פריסה ופרסום

זהו מאגר לימודי - אין תהליך פריסה. התוכנית נצרכת על ידי:

1. **מאגר GitHub**: גישה ישירה לקוד ולתיעוד
2. **GitHub Codespaces**: סביבת פיתוח מיידית עם הגדרות מראש
3. **Microsoft Learn**: תוכן עשוי להיות מסונכרן לפלטפורמת הלמידה הרשמית
4. **docsify**: אתר תיעוד שנבנה מ-Markdown (ראה `docsifytopdf.js` ו-`package.json`)

### בניית אתר תיעוד

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## פתרון בעיות

### בעיות נפוצות

**שגיאות ייבוא Python**:
- ודא שסביבת העבודה הווירטואלית מופעלת
- הרץ `pip install -r requirements.txt`
- בדוק שגרסת Python היא 3.9+

**שגיאות בנייה TypeScript**:
- הרץ `npm install` בתיקיית האפליקציה הספציפית
- בדוק שגרסת Node.js תואמת
- נקה `node_modules` והתקן מחדש אם נדרש

**שגיאות אימות API**:
- ודא שקובץ `.env` קיים ויש בו ערכים נכונים
- בדוק שמפתחות API תקפים ולא פגי תוקף
- ודא שכתובות URL של נקודות הקצה נכונות לאזור שלך

**משתני סביבה חסרים**:
- העתק את `.env.copy` ל-`.env`
- מלא את כל הערכים הנדרשים עבור השיעור שאתה עובד עליו
- הפעל מחדש את האפליקציה לאחר עדכון `.env`

## משאבים נוספים

- [מדריך התקנת הקורס](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [הנחיות לתרומה](./CONTRIBUTING.md)
- [קוד התנהגות](./CODE_OF_CONDUCT.md)
- [מדיניות אבטחה](./SECURITY.md)
- [Discord של Azure AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [אוסף דוגמאות קוד מתקדמות](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## הערות ספציפיות לפרויקט

- זהו **מאגר חינוכי** המתמקד בלמידה, לא בקוד ייצור
- דוגמאות הן פשוטות בכוונה ומתמקדות בהוראת מושגים
- איכות הקוד מאוזנת עם בהירות חינוכית
- כל שיעור הוא עצמאי וניתן להשלמה בנפרד
- המאגר תומך במספר ספקי API: Azure OpenAI, OpenAI ודגמי GitHub
- התוכן הוא רב-לשוני עם זרימות עבודה אוטומטיות לתרגום
- קהילה פעילה ב-Discord לשאלות ותמיכה

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.