# AGENTS.md

## סקירת פרויקט

מאגר זה מכיל תוכנית לימודים מקיפה של 21 שיעורים המלמדים יסודות אינטיליגנציה מלאכותית גנרטיבית ופיתוח אפליקציות. הקורס מיועד למתחילים ומכסה הכל מרעיונות בסיסיים ועד בניית אפליקציות מוכנות לייצור.

**טכנולוגיות מרכזיות:**
- Python 3.9+ עם הספריות: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript עם Node.js והספריות: `openai` (Azure OpenAI דרך נקודת הקצה v1 + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- שירות Azure OpenAI, OpenAI API, ומודלים של Microsoft Foundry (GitHub Models מפסיקים לפעול בסוף יולי 2026)
- מחברות Jupyter ללמידה אינטראקטיבית
- מיכלי פיתוח לסביבת פיתוח עקבית

**מבנה המאגר:**
- 21 תיקיות שיעורים ממוספרים (00-21) שמכילות קבצי README, דוגמאות קוד, ומשימות
- מימושים מרובים: דוגמאות ב-Python, TypeScript, ולפעמים .NET
- תיקיית תרגומים עם למעלה מ-40 גרסאות בשפות שונות
- תצורה מרכזית דרך קובץ `.env` (השתמש ב-`.env.copy` כתבנית)

## פקודות התקנה

### התקנה ראשונית של המאגר

```bash
# לשכפל את מאגר הקוד
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# להעתיק את תבנית הסביבה
cp .env.copy .env
# לערוך את קובץ .env עם מפתחות ה-API והנקודות הקצה שלך
```

### התקנת סביבת Python

```bash
# צור סביבה וירטואלית
python3 -m venv venv

# הפעל סביבה וירטואלית
# במק או לינוקס:
source venv/bin/activate
# בוינדוס:
venv\Scripts\activate

# התקן תלותיים
pip install -r requirements.txt
```

### התקנת Node.js/TypeScript

```bash
# התקן תלותיות ברמת השורש (לכלי תיעוד)
npm install

# עבור דוגמאות TypeScript של שיעורים בודדים, נווט לשיעור הספציפי:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### התקנת מיכל פיתוח (מומלץ)

המאגר כולל תצורת `.devcontainer` ל-GitHub Codespaces או ל-VS Code Dev Containers:

1. פתח את המאגר ב-GitHub Codespaces או ב-VS Code עם תוסף Dev Containers
2. מיכל הפיתוח יפעל אוטומטית:
   - יתקין תלותיות Python מתוך `requirements.txt`
   - יריץ סקריפט אחרי יצירה (`.devcontainer/post-create.sh`)
   - יקים את ליבת Jupyter

## זרימת עבודה לפיתוח

### משתני סביבה

כל השיעורים שדורשים גישה ל-API משתמשים במשתני סביבה המוגדרים ב-`.env`:

- `OPENAI_API_KEY` - לממשק OpenAI API
- `AZURE_OPENAI_API_KEY` - ל-Azure OpenAI ב-Microsoft Foundry (שירות Azure OpenAI הוא חלק מ-Microsoft Foundry כעת: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - כתובת נקודת הקצה ל-Azure OpenAI (נקודת קצה של Foundry resource)
- `AZURE_OPENAI_DEPLOYMENT` - שם פריסת מודל השלמת שיחה (ברירת מחדל בקורס: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - שם פריסת מודל האנשה (ברירת מחדל בקורס: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - גרסת API (ברירת מחדל: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - למודלים של Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - נקודת קצה למודלים של Microsoft Foundry (קטלוג מודלים מרובה ספקים)
- `AZURE_INFERENCE_CREDENTIAL` - מפתח API למודלים של Microsoft Foundry (מחליף את `GITHUB_TOKEN` שמפסיק לפעול)
- `AZURE_INFERENCE_CHAT_MODEL` - מודל לא-מנתח (למשל `Llama-3.3-70B-Instruct`) המשמש בדוגמאות עם `temperature`, כי מודלים מנתחים אינם תומכים בשליטה בדגימה

### קונבנציות מודלים (חשוב)

- **מודל השיחה ברירת המחדל הוא `gpt-5-mini`** - מודל **מנתח** עדכני ולא מיושן. החל מ-2026, מודלי "מיני" ותיקי-הטמפרטורה (`gpt-4o-mini`, `gpt-4.1-mini`) מתבטלים, לכן תוכנית הלימודים מתאחדת סביב משפחת GPT-5.
- **מודלים מנתחים אינם מקבלים `temperature` ו-`top_p`**, ומעדיפים שימוש ב-`max_output_tokens` (Responses API) / `max_completion_tokens` (השלמות שיחה) במקום `max_tokens`. אל תוסיף `temperature`/`top_p`/`max_tokens` לדוגמאות שמפעילות את `gpt-5-mini`.
- **כדי להדגים את `temperature`**, דוגמאות משתמשות במודל **Llama** (`Llama-3.3-70B-Instruct`) דרך נקודת קצה Microsoft Foundry Models (`AZURE_INFERENCE_CHAT_MODEL`). נהל מודלים מנתחים עם הנדסת פרומפט + בקרות ניתוח במקום כפתורי דגימה.
- **כיוונון עדין (שיעור 18)** משתמש ב-`gpt-4.1-mini`: GPT-5 תומך רק בכיוונון עדין עם חיזוק (RFT), לא בכיוונון עדין מפוקח (SFT) שמוצג שם.
- שיעורים 20 (Mistral) ו-21 (Meta) שומרים על `temperature`/`max_tokens` מכיוון שהם ממוקדים במודלים Mistral/Llama התומכים בכך.

### הרצת דוגמאות Python

```bash
# לעבור לספריית השיעור
cd 06-text-generation-apps/python

# להריץ סקריפט פייתון
python aoai-app.py
```

### הרצת דוגמאות TypeScript

```bash
# עבור לתיקיית אפליקציית TypeScript
cd 06-text-generation-apps/typescript/recipe-app

# תבנה את קוד TypeScript
npm run build

# הפעל את היישום
npm start
```

### הרצת מחברות Jupyter

```bash
# הפעל את Jupyter בתיקיית השורש של המאגר
jupyter notebook

# או השתמש ב-VS Code עם תוסף Jupyter
```

### עבודה עם סוגי שיעורים שונים

- **שיעורי "לימוד"**: מתמקדים בתיעוד README.md וברעיונות
- **שיעורי "בניית"**: כוללים דוגמאות קוד עובדות ב-Python ו-TypeScript
- לכל שיעור יש README.md עם תאוריה, הסברים על קוד וקישורים לתוכן וידאו

## הנחיות לסגנון קוד

### Python

- השתמש ב-`python-dotenv` לניהול משתני סביבה
- ייבא את הספרייה `openai` לאינטראקציות API
- השתמש ב-`pylint` ללינטינג (בחלק מהדוגמאות מופיע `# pylint: disable=all` לפשטות)
- עוקב אחרי קונבנציות שם לפי PEP 8
- אחסן אישורי API בקובץ `.env`, לא בקוד

### TypeScript

- השתמש בחבילת `dotenv` למשתני סביבה
- קונפיגורציית TypeScript בקובץ `tsconfig.json` לכל אפליקציה
- השתמש בחבילת `openai` ל-Azure OpenAI (הפנה את הלקוח לנקודת הקצה `/openai/v1/` וקרא ל-`client.responses.create`); השתמש ב-`@azure-rest/ai-inference` למודלים של Microsoft Foundry
- השתמש ב-`nodemon` לפיתוח עם טעינה מחדש אוטומטית
- בנייה לפני הריצה: `npm run build` ואז `npm start`

### קונבנציות כלליות

- שמור על דוגמאות קוד פשוטות וחינוכיות
- כלל הערות שמסבירות מושגים מרכזיים
- כל קוד של שיעור צריך להיות עצמאי והרציונלי
- השתמש בשמות עקביים: קידומת `aoai-` ל-Azure OpenAI, `oai-` ל-OpenAI API, `githubmodels-` ל-Microsoft Foundry Models (קידומת ישנה מימי GitHub Models)

## הנחיות לתיעוד

### סגנון Markdown

- כל כתובות האתרים חייבות להיות בתבנית `[text](../../url)` ללא רווחים מיותרים
- קישורים יחסיים חייבים להתחיל ב-`./` או `../`
- כל הקישורים לדומיינים של Microsoft חייבים לכלול מזהה מעקב: `?WT.mc_id=academic-105485-koreyst`
- אין להשתמש בלוקאלים ספציפיים למדינה בכתובות (להימנע מ-`/en-us/`)
- תמונות נשמרות בתיקיית `./images` עם שמות תיאוריים
- השתמש בתווים אנגליים, מספרים וקווים בקבצי התמונות

### תמיכה בתרגום

- המאגר תומך ביותר מ-40 שפות דרך פעולות אוטומטיות של GitHub
- התרגומים מאוחסנים בתיקיית `translations/`
- אין להגיש תרגומים חלקיים
- תרגומים מכונתיים אינם מתקבלים
- תמונות מתורגמות מאוחסנות בתיקיית `translated_images/`

## בדיקות ואימות

### בדיקות לפני ההגשה

מאגר זה משתמש ב-GitHub Actions לאימות. לפני הגשת PRs:

1. **בדוק קישורי Markdown**:
   ```bash
   # זרימת העבודה validate-markdown.yml בודקת:
   # - נתיבים יחסיים שבורים
   # - חוסרים מזהי מעקב בנתיבים
   # - חוסרים מזהי מעקב בכתובות URL
   # - כתובות URL עם אזור שפה של מדינה
   # - כתובות URL חיצוניות שבורות
   ```

2. **בדיקות ידניות**:
   - בדוק דוגמאות Python: הפעל venv והריץ סקריפטים
   - בדוק דוגמאות TypeScript: `npm install`, `npm run build`, `npm start`
   - אמת שתצורת משתני הסביבה נכונה
   - בדוק שמפתחות ה-API פועלים עם דוגמאות הקוד

3. **דוגמאות קוד**:
   - וודא שכל הקוד רץ ללא שגיאות
   - בדוק עם Azure OpenAI ו-OpenAI API כשנדרש
   - אמת שדוגמאות פועלות עם Microsoft Foundry Models שם נתמך

### אין בדיקות אוטומטיות

זה מאגר חינוכי המתמקד בהדרכות ודוגמאות. אין בדיקות יחידה או אינטגרציה להפעלה. האימות הוא בעיקר:
- בדיקות ידניות של דוגמאות קוד
- GitHub Actions לאימות Markdown
- סקירת קהילה לתוכן חינוכי

## הנחיות לבקשת משיכה (PR)

### לפני הגשה

1. בדוק שינויים בקוד ב-Python ו-TypeScript כשנדרש
2. הרץ אימות Markdown (מתבצע אוטומטית ב-PR)
3. ודא שמזהי המעקב קיימים בכל כתובות Microsoft
4. בדוק שקישורים יחסיים תקינים
5. אמת שתמונות מופיעות נכון

### פורמט כותרת PR

- השתמש בכותרות תיאוריות: `[Lesson 06] תיקון טעות בדוגמת Python` או `עדכון README לשיעור 08`
- הפנה למספרי בעיות כשנדרש: `Fixes #123`

### תיאור PR

- הסבר מה שונה ולמה
- קשר לבעיות רלוונטיות
- עבור שינויים בקוד, פרט אילו דוגמאות נבדקו
- עבור PR תרגום, כלול את כל הקבצים לתרגום מלא

### דרישות תרומה

- חתום על Microsoft CLA (אוטומטי בהגשה ראשונה)
- פצל את המאגר לחשבון שלך לפני ביצוע שינויים
- כל PR לשינוי לוגי אחד (אל תשלב תיקונים לא קשורים)
- שמור את ה-PR ממוקדים וקטנים ככל האפשר

## זרימות עבודה נפוצות

### הוספת דוגמת קוד חדשה

1. נווט לתיקיית השיעור הרלוונטית
2. צור דוגמה בתיקיית `python/` או `typescript/`
3. פעל לפי קונבנציית השמות: `{provider}-{example-name}.{py|ts|js}`
4. בדוק עם אישורי API אמיתיים
5. תעד כל משתנה סביבה חדש ב-README של השיעור

### עדכון תיעוד

1. ערוך את README.md בתיקיית השיעור
2. עקוב אחר הנחיות Markdown (מזהי מעקב, קישורים יחסיים)
3. תרגומים מתעדכנים באמצעות פעולות GitHub אוטומטיות (אל תערוך ידנית)
4. בדוק שכל הקישורים תקינים

### עבודה עם מיכלי פיתוח

1. המאגר כולל `.devcontainer/devcontainer.json`
2. סקריפט אחרי יצירה מתקין תלותיות Python אוטומטית
3. תוספים עבור Python ו-Jupyter מוגדרים מראש
4. הסביבה מבוססת על `mcr.microsoft.com/devcontainers/universal:2.11.2`

## פריסה ופרסום

זה מאגר למידה - אין תהליך פריסה. התכנית נצרכת באמצעות:

1. **מאגר GitHub**: גישה ישירה לקוד ולתיעוד
2. **GitHub Codespaces**: סביבת פיתוח מיידית עם הגדרת מראש
3. **Microsoft Learn**: יתכן שהתוכן יסונף לפלטפורמת למידה רשמית
4. **docsify**: אתר תיעוד הבנוי Markdown (ראה `docsifytopdf.js` ו-`package.json`)

### בניית אתר תיעוד

```bash
# ליצור PDF מהתיעוד (אם יש צורך)
npm run convert
```

## פתרון בעיות

### בעיות נפוצות

**שגיאות ייבוא Python**:
- וודא שסביבת וירטואלית מופעלת
- הרץ `pip install -r requirements.txt`
- בדוק שגרסת Python היא 3.9 ומעלה

**שגיאות בניית TypeScript**:
- הרץ `npm install` בתיקיית האפליקציה הספציפית
- בדוק שגרסת Node.js תואמת
- נקה את `node_modules` והתקן מחדש אם צריך

**שגיאות אימות API**:
- אמת שקובץ `.env` קיים עם ערכים נכונים
- בדוק שמפתחות ה-API תקפים ולא פגו תוקף
- ודא שכתובות נקודת הקצה נכונות לאזור שלך

**משתני סביבה חסרים**:
- העתק את `.env.copy` ל-`.env`
- מלא את כל הערכים הנדרשים לשיעור שאתה עובד עליו
- הפעל מחדש את האפליקציה לאחר עדכון `.env`

## משאבים נוספים

- [מדריך התקנת קורס](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [הנחיות לתרומה](./CONTRIBUTING.md)
- [קוד ההתנהגות](./CODE_OF_CONDUCT.md)
- [מדיניות אבטחה](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [אוסף דוגמאות קוד מתקדמות](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## הערות ספציפיות לפרויקט

- זהו **מאגר חינוכי** הממוקד בלימוד, לא בקוד לייצור
- דוגמאות מכוונות להיות פשוטות וממוקדות ללימוד מושגים
- איכות הקוד מאזנת בין דיוק חינוכי ובהירות
- כל שיעור עצמאי וניתן לסיום בנפרד
- המאגר תומך בכמה ספקי API: Azure OpenAI, OpenAI, Microsoft Foundry Models, וספקים לא מקוונים כמו Foundry Local ו-Ollama
- תוכן רב-לשוני עם זרימות עבודה לתרגום אוטומטי
- קהילה פעילה בדיסקורד לשאלות ותמיכה

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->