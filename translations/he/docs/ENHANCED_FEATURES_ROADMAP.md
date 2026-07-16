# מפת דרכים לתכונות משופרות ושיפורים

מסמך זה מפרט שיפורים והמלצות לשדרוגים לתכנית הלימודים של הבינה המלאכותית הגנרטיבית למתחילים, בהתבסס על סקירת קוד מקיפה וניתוח של שיטות העבודה המובילות בתעשייה.

## סיכום מנהלים

בסיס הקוד נותח מבחינת אבטחה, איכות קוד ואפקטיביות חינוכית. מסמך זה מספק המלצות לתיקונים מיידיים, שיפורים לטווח הקרוב ושדרוגים עתידיים.

---

## 1. שיפורי אבטחה (עדיפות: קריטית)

### 1.1 תיקונים מיידיים (הושלם)

| סוגיה | קבצים מושפעים | מצב |
|-------|----------------|--------|
| מפתח סודי מקודד בקוד | `05-advanced-prompts/python/aoai-solution.py` | תוקן |
| חסר אימות env | מספר קבצי JS/TS | תוקן |
| קריאות פונקציה לא בטוחות | `11-integrating-with-function-calling/js-githubmodels/app.js` | תוקן |
| דליפות מנועי קבצים | `08-building-search-applications/scripts/` | תוקן |
| חסר timeouts בבקשות | `09-building-image-applications/python/` | תוקן |

### 1.2 תכונות אבטחה מומלצות נוספות

1. **דוגמאות להגבלת קצב**
   - הוסף קוד לדוגמה המציג כיצד ליישם הגבלת קצב לקריאות API
   - הצג דפוסי exponential backoff

2. **סיבוב מפתחות API**
   - הוסף תיעוד על שיטות עבודה מומלצות לסיבוב מפתחות API
   - כלול דוגמאות לשימוש ב-Azure Key Vault או שירותים דומים

3. **שילוב אבטחת תוכן**
   - הוסף דוגמאות המראות שימוש ב-Azure Content Safety API
   - הצג דפוסי בקרה על קלט/פלט

---

## 2. שיפורי איכות קוד

### 2.1 קבצי קונפיגורציה שהוספו

| קובץ | מטרה |
|------|---------|
| `.eslintrc.json` | כללי לינטינג ל-JavaScript/TypeScript |
| `.prettierrc` | סטנדרטים לעיצוב קוד |
| `pyproject.toml` | קונפיגורציית כלים לפייתון (Black, Ruff, mypy) |

### 2.2 כלים משותפים שנוצרו

מודול חדש `shared/python/` הכולל:
- `env_utils.py` - ניהול משתני סביבה
- `input_validation.py` - אימות וסינון קלט
- `api_utils.py` - עטיפות בטוחות לקריאות API

### 2.3 שיפורי קוד מומלצים

1. **כיסוי רמזי טיפוס**
   - הוסף רמזי טיפוס לכל קבצי פייתון
   - אפשר מצב TypeScript מחמיר בכל פרויקטי ה-TS

2. **סטנדרטים לתיעוד**
   - הוסף docstrings לכל פונקציות הפייתון
   - הוסף הערות JSDoc לכל פונקציות ה-JavaScript/TypeScript

3. **מסגרת בדיקות**
   - הוסף קונפיגורציית pytest ודוגמאות לבדיקות _(בוצע: קונפיגורציית pytest ב-`pyproject.toml`; דוגמאות לבדיקות לכלים המשותפים ב-[`tests/`](../../../tests) הפועלות ב-CI)_
   - הוסף קונפיגורציית Jest עבור JavaScript/TypeScript

---

## 3. שיפורים חינוכיים

### 3.1 נושאי שיעורים חדשים

1. **אבטחה ביישומי בינה מלאכותית** (שיעור מוצע 22)
   - התקפות הזרקת פרומפט ודרכי הגנה
   - ניהול מפתחות API
   - בקרה על תוכן
   - הגבלת קצב ומניעת שימוש לרעה

2. **פריסת ייצור** (שיעור מוצע 23)
   - מכולות עם Docker
   - צינורות CI/CD
   - ניטור ורישום לוגים
   - ניהול עלויות

3. **טכניקות RAG מתקדמות** (שיעור מוצע 24)
   - חיפוש היברידי (מילות מפתח + סמנטי)
   - אסטרטגיות מיון מחדש
   - RAG רב-מודאלי
   - מדדי הערכה

### 3.2 שיפורים בשיעורים קיימים

| שיעור | שיפור מומלץ |
|--------|------------------------|
| 06 - יצירת טקסט | הוסף דוגמאות לתגובה בזרם |
| 07 - יישומי שיחה | הוסף דפוסי זיכרון שיחה |
| 08 - יישומי חיפוש | הוסף השוואות מסדי נתונים וקטוריים |
| 09 - יצירת תמונות | הוסף דוגמאות לעריכת תמונות/שינויים |
| 11 - קריאות פונקציה | הוסף קריאות פונקציה מקבילות |
| 15 - RAG | הוסף השוואת אסטרטגיית פירוק לחלקים |
| 17 - סוכני AI | הוסף תזמור רב-סוכני |

---

## 4. מודרניזציה של API

### 4.1 דפוסים מיושנים (הגירה הושלמה)

כל דוגמאות הצ'אט בפייתון ו-TypeScript הועברו מ-Chat Completions API ל-Responses API (`client.responses.create(...)` → `response.output_text`).

| דפוס ישן | דפוס חדש | מצב |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (צ'אט) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | הושלם |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | הושלם |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | חבילת `openai` `client.responses.create()` → `response.output_text` | הושלם |
| `df.append()` (pandas) | `pd.concat()` | הושלם |

> **הערה:** דוגמאות Microsoft Foundry Models המשתמשות ב-SDK `azure-ai-inference` / `@azure-rest/ai-inference` (`client.complete()`) נשארות על Model Inference API, שאינו תומך ב-Responses API. `AzureOpenAI()` נשמר במכוון במקומות שעדיין רלוונטיים (אמבדינג ויצירת תמונות).

### 4.2 תכונות API חדשות להדגמה

1. **פלטים מובנים** (OpenAI)
   - מצב JSON
   - קריאות פונקציה עם סכימות מחמירות

2. **יכולות ראייה**
   - ניתוח תמונות עם GPT-4o (ויז'ן)
   - פרומפטים רב-מודאליים

3. **כלים מובנים ב-Responses API** (מחזיק מקום ל-Assistants API הישן)
   - מפרש קוד
   - חיפוש בקבצים
   - חיפוש באינטרנט וכלים מותאמים אישית

---

## 5. שיפורי תשתית

### 5.1 שיפורים ב-CI/CD

מומשו ב-[`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): לינטינג/עיצוב פייתון (Ruff + Black) נאכף במודול הכלים המשותף `shared/` ופועל כייעוץ בשאר התכנית, בנוסף לריצת ESLint ייעוצית ל-JavaScript/TypeScript. קו הבסיס להמחשה היה:

```yaml
# .github/workflows/code-quality.yml
name: Code Quality

on: [push, pull_request]

jobs:
  python-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - run: pip install ruff black mypy
      - run: ruff check .
      - run: black --check .

  js-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npx eslint .
```

### 5.2 סריקת אבטחה

מומש ב-[`.github/workflows/security.yml`](../../../.github/workflows/security.yml): ניתוח CodeQL לפייתון ו-JavaScript/TypeScript (בהנחה, בבקשת משיכה ולוח זמנים שבועי) בנוסף לסקירת תלות בבקשות משיכה. קו הבסיס להמחשה היה:

```yaml
# .github/workflows/security.yml
name: Security Scan

on: [push, pull_request]

jobs:
  codeql:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: javascript, python
      - uses: github/codeql-action/analyze@v3

  dependency-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/dependency-review-action@v4
```

---

## 6. שיפורי חוויית מפתח

### 6.1 שיפורים ב-DevContainer

מומש ב-[`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) ו-[`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): המכולה כוללת כעת את Pylance, מעצב Black, Ruff, ESLint, Prettier, ותוספות Copilot, מאפשרת עיצוב שמירה המתואמת לקונפיגורציית Black/Prettier של הרפו, ומתקינה את כלי הפיתוח (`ruff`, `black`, `mypy`, `pytest`) כך שניתן לשחזר את [זרימת העבודה לקוד איכות](../../../.github/workflows/code-quality.yml) באופן מקומי. תצורת הבסיס להמחשה הייתה:

```json
{
  "name": "Generative AI for Beginners",
  "image": "mcr.microsoft.com/devcontainers/universal:2",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.11"
    },
    "ghcr.io/devcontainers/features/node:1": {
      "version": "20"
    }
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-toolsai.jupyter",
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "github.copilot"
      ],
      "settings": {
        "python.formatting.provider": "black",
        "editor.formatOnSave": true
      }
    }
  },
  "postCreateCommand": "pip install -e .[dev] && npm install"
}
```

### 6.2 מגרש משחקים אינטראקטיבי

מומלץ להוסיף:
- פנקסי Jupyter עם מפתחות API מראש (באמצעות סביבה)
- הדגמות Gradio/Streamlit ללומדים חזותיים
- חידונים אינטראקטיביים להערכת ידע

---

## 7. תמיכה רב-לשונית

### 7.1 כיסוי שפות נוכחי

| טכנולוגיה | שיעורים מכוסים | מצב |
|------------|-----------------|--------|
| Python | הכל | הושלם |
| TypeScript | 06-09, 11 | חלקי |
| JavaScript | 06-08, 11 | חלקי |
| .NET/C# | חלק מהשיעורים | חלקי |

### 7.2 תוספות מומלצות

1. **Go** - צובר כלים בבינה מלאכותית ולמידת מכונה
2. **Rust** - יישומים קריטיים לביצועים
3. **Java/Kotlin** - יישומי ארגונים

---

## 8. אופטימיזציות ביצועים

### 8.1 אופטימיזציות ברמת קוד

1. **דפוסי Async/Await**
   - הוסף דוגמאות אסינכרוניות לעיבוד מאצ'
   - הצג קריאות API מקבילות

2. **אסטרטגיות קאשינג**
   - הוסף דוגמאות לקאשינג אמבדינג
   - הצג דפוסי קאשינג לתגובות

3. **אופטימיזציה של טוקנים**
   - הוסף דוגמאות שימוש ב-tiktoken
   - הצג טכניקות דחיסת פרומפט

### 8.2 דוגמאות לאופטימיזצית עלויות

הוסף דוגמאות המציגות:
- בחירת מודל על פי מורכבות המשימה
- הנדסת פרומפט ליעילות בטוקנים
- עיבוד מאצ' לפעולות בכמויות גדולות

---

## 9. נגישות ובינלאומיות

### 9.1 סטטוס תרגום נוכחי

כל התרגומים **הושלמו** ומיוצרים אוטומטית על ידי [מתרגם Azure Co-op](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst), המפיק ושומר על סנכרון של יותר מ-50 גרסאות שפה לתכנית עם המקור באנגלית. התוכן המתורגם נמצא תחת `translations/` ותמונות מתורגמות תחת `translated_images/`; רשימת כל השפות זמינה מפורשת בראש ה-README של המאגר.

| היבט | מצב |
|--------|--------|
| כיסוי תרגום | הושלם — מעל 50 שפות, כל השיעורים |
| שיטת תרגום | אוטומטית באמצעות [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) |
| שמור סינכרון עם המקור באנגלית | כן — מיוצר מחדש אוטומטית |

### 9.2 שיפורי נגישות

1. הוסף טקסט אלטרנטיבי לכל התמונות
2. ודא שלדוגמאות הקוד יש הדגשת סינטקס נכונה
3. הוסף תמלילים לכל תוכן הווידאו
4. ודא ניגודיות צבעים בהתאם להנחיות WCAG

---

## 10. עדיפות ליישום

### שלב 1: מיידי (שבוע 1-2)
- [x] תיקון סוגיות אבטחה קריטיות
- [x] הוספת קונפיגורציית איכות קוד
- [x] יצירת כלים משותפים
- [x] תיעוד הנחיות אבטחה

### שלב 2: קצר טווח (שבוע 3-4)
- [x] עדכון דפוסי API מיושנים (Chat Completions → Responses API, פייתון + TypeScript)
- [ ] הוספת רמזי טיפוס לכל קבצי פייתון (בוצע למודול המשותף `shared/`; דוגמאות השיעורים הוכנסו בפשטות)
- [x] הוספת זרימות עבודה ל-CI/CD לאיכות קוד
- [x] יצירת זרימת סריקת אבטחה

### שלב 3: טווח בינוני (חודש 2-3)
- [ ] הוספת שיעור אבטחה חדש
- [ ] הוספת שיעור פריסת ייצור
- [x] שיפור תצורת DevContainer
- [ ] הוספת הדגמות אינטראקטיביות

### שלב 4: טווח ארוך (חודש 4+)
- [ ] הוספת שיעור RAG מתקדם
- [ ] הרחבת כיסוי השפות
- [ ] הוספת סט בדיקות מקיף
- [ ] יצירת תוכנית הסמכה

---

## סיכום

מפת דרך זו מספקת גישה מובנית לשיפור תכנית הלימודים לבינה מלאכותית גנרטיבית למתחילים. באמצעות טיפול בסוגיות אבטחה, מודרניזציה של APIs והוספת תוכן חינוכי, הקורס יכין טוב יותר את התלמידים לפיתוח אפליקציות בינה מלאכותית במציאות.

לשאלות או תרומות, אנא פתחו נושא במאגר GitHub.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->