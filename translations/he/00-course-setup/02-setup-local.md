<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5cf0b10ab3c485e6334101f5784f1f3",
  "translation_date": "2025-12-19T15:56:58+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "he"
}
-->
# התקנה מקומית 🖥️

**השתמש במדריך זה אם אתה מעדיף להריץ הכל במחשב הנייד שלך.**  
יש לך שתי דרכים: **(A) פייתון מקומי + virtual-env** או **(B) מיכל פיתוח VS Code עם Docker**.  
בחר את מה שנראה לך קל יותר—שניהם מובילים לאותן השיעורים.

## 1. דרישות מוקדמות

| כלי                | גרסה / הערות                                                                       |
|--------------------|------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (הורד מ- <https://python.org>)                                              |
| **Git**            | העדכנית ביותר (מגיעה עם Xcode / Git ל-Windows / מנהל החבילות של לינוקס)           |
| **VS Code**        | אופציונלי אך מומלץ <https://code.visualstudio.com>                                 |
| **Docker Desktop** | *רק* לאופציה B. התקנה חינמית: <https://docs.docker.com/desktop/>                  |

> 💡 **טיפ** – אמת את הכלים בטרמינל:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. אופציה A – פייתון מקומי (המהירה ביותר)

### שלב 1  שכפל את המאגר הזה

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### שלב 2 צור והפעל סביבה וירטואלית

```bash
python -m venv .venv          # ליצור אחד
source .venv/bin/activate     # macOS / לינוקס
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ השורת פקודה צריכה להתחיל כעת ב-(.venv)—זה אומר שאתה בתוך הסביבה.

### שלב 3 התקן תלותים

```bash
pip install -r requirements.txt
```

דלג לסעיף 3 על [מפתחות API](../../../00-course-setup)

## 2. אופציה B – מיכל פיתוח VS Code (Docker)

הגדרנו את המאגר והקורס הזה עם [מיכל פיתוח](https://containers.dev?WT.mc_id=academic-105485-koreyst) שיש לו סביבת ריצה אוניברסלית התומכת בפיתוח Python3, .NET, Node.js ו-Java. ההגדרות הרלוונטיות מוגדרות בקובץ `devcontainer.json` שנמצא בתיקיית `.devcontainer/` בשורש המאגר הזה.

>**למה לבחור בזה?**  
>סביבה זהה ל-Codespaces; ללא סטייה בתלויות.

### שלב 0 התקן את התוספים

Docker Desktop – אמת ש-```docker --version``` עובד.  
תוסף VS Code Remote – Containers (מזהה: ms-vscode-remote.remote-containers).

### שלב 1 פתח את המאגר ב-VS Code

קובץ ▸ פתח תיקייה… → generative-ai-for-beginners

VS Code מזהה את .devcontainer/ ומציג הודעה.

### שלב 2 פתח מחדש במיכל

לחץ על "Reopen in Container". Docker בונה את התמונה (כ-3 דקות בפעם הראשונה).  
כשהטרמינל מופיע, אתה בתוך המיכל.

## 2. אופציה C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) הוא מתקין קל משקל להתקנת [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), פייתון, וכמה חבילות.  
Conda עצמה היא מנהל חבילות, שמקל על יצירה והחלפה בין [סביבות וירטואליות](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) שונות של פייתון וחבילות. היא גם שימושית להתקנת חבילות שאינן זמינות דרך `pip`.

### שלב 0 התקן את Miniconda

עקוב אחרי [מדריך ההתקנה של MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) כדי להגדיר אותה.

```bash
conda --version
```

### שלב 1 צור סביבה וירטואלית

צור קובץ סביבה חדש (*environment.yml*). אם אתה עובד עם Codespaces, צור אותו בתוך תיקיית `.devcontainer`, כלומר `.devcontainer/environment.yml`.

### שלב 2 מלא את קובץ הסביבה שלך

הוסף את הקטע הבא ל-`environment.yml`

```yml
name: <environment-name>
channels:
 - defaults
 - microsoft
dependencies:
- python=<python-version>
- openai
- python-dotenv
- pip
- pip:
    - azure-ai-ml

```

### שלב 3 צור את סביבת Conda שלך

הרץ את הפקודות הבאות בשורת הפקודה/טרמינל שלך

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer הנתיב המשני חל רק על הגדרות Codespace
conda activate ai4beg
```

עיין ב-[מדריך סביבות Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) אם נתקלת בבעיות.

## 2  אופציה D – Jupyter קלאסי / Jupyter Lab (בדפדפן שלך)

> **למי זה מתאים?**  
> לכל מי שאוהב את הממשק הקלאסי של Jupyter או רוצה להריץ מחברות ללא VS Code.

### שלב 1 ודא ש-Jupyter מותקן

כדי להפעיל Jupyter מקומית, עבור לטרמינל/שורת הפקודה, נווט לתיקיית הקורס, והריץ:

```bash
jupyter notebook
```

או

```bash
jupyterhub
```

זה יפעיל מופע Jupyter וכתובת ה-URL לגישה אליו תוצג בחלון שורת הפקודה.

כשתיגש לכתובת ה-URL, תראה את מתווה הקורס ותוכל לנווט לכל קובץ `*.ipynb`. לדוגמה, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. הוסף את מפתחות ה-API שלך

שמירה על מפתחות ה-API שלך בטוחים היא חשובה בעת בניית כל סוג של אפליקציה. אנו ממליצים לא לאחסן מפתחות API ישירות בקוד שלך. העלאת פרטים אלה למאגר ציבורי עלולה לגרום לבעיות אבטחה ואפילו לעלויות לא רצויות אם ישתמש בהם גורם זדוני.  
הנה מדריך שלב-אחר-שלב כיצד ליצור קובץ `.env` לפייתון ולהוסיף את `GITHUB_TOKEN`:

1. **נווט לתיקיית הפרויקט שלך**: פתח את הטרמינל או שורת הפקודה ונווט לשורש תיקיית הפרויקט שבו תרצה ליצור את קובץ ה-`.env`.

   ```bash
   cd path/to/your/project
   ```

2. **צור את קובץ `.env`**: השתמש בעורך הטקסט המועדף עליך כדי ליצור קובץ חדש בשם `.env`. אם אתה משתמש בשורת הפקודה, תוכל להשתמש ב-`touch` (במערכות מבוססות יוניקס) או ב-`echo` (ב-Windows):

   מערכות מבוססות יוניקס:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **ערוך את קובץ `.env`**: פתח את קובץ ה-`.env` בעורך טקסט (למשל VS Code, Notepad++ או כל עורך אחר). הוסף את השורה הבאה לקובץ, כשהחלף את `your_github_token_here` בטוקן GitHub האמיתי שלך:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **שמור את הקובץ**: שמור את השינויים וסגור את עורך הטקסט.

5. **התקן את `python-dotenv`**: אם עדיין לא התקנת, תצטרך להתקין את חבילת `python-dotenv` כדי לטעון משתני סביבה מקובץ `.env` לאפליקציית הפייתון שלך. ניתן להתקין באמצעות `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **טען משתני סביבה בסקריפט הפייתון שלך**: בסקריפט הפייתון שלך, השתמש בחבילת `python-dotenv` כדי לטעון את משתני הסביבה מקובץ `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # טען משתני סביבה מקובץ .env
   load_dotenv()

   # גש למשתנה GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

זהו! יצרת בהצלחה קובץ `.env`, הוספת את טוקן GitHub שלך וטעונת אותו לאפליקציית הפייתון שלך.

🔐 לעולם אל תבצע commit ל-.env—הוא כבר נמצא ב-.gitignore.  
הוראות מלאות לספקים נמצאות ב-[`providers.md`](03-providers.md).

## 4. מה הלאה?

| אני רוצה…          | עבור אל…                                                                |
|---------------------|------------------------------------------------------------------------|
| להתחיל בשיעור 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| להגדיר ספק LLM     | [`providers.md`](03-providers.md)                                       |
| לפגוש לומדים אחרים | [הצטרף ל-Discord שלנו](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. פתרון תקלות

| תסמין                                    | תיקון                                                            |
|------------------------------------------|-----------------------------------------------------------------|
| `python not found`                       | הוסף את Python ל-PATH או פתח מחדש את הטרמינל לאחר ההתקנה       |
| `pip` לא מצליח לבנות גלגלים (Windows)   | הרץ `pip install --upgrade pip setuptools wheel` ואז נסה שוב.  |
| `ModuleNotFoundError: dotenv`            | הרץ `pip install -r requirements.txt` (הסביבה לא הותקנה).      |
| Docker build נכשל *No space left*         | Docker Desktop ▸ *Settings* ▸ *Resources* → הגדל את גודל הדיסק.  |
| VS Code ממשיך להציע לפתוח מחדש           | ייתכן ששתי האופציות פעילות; בחר אחת (venv **או** container)    |
| שגיאות OpenAI 401 / 429                  | בדוק את ערך `OPENAI_API_KEY` / מגבלות קצב הבקשות.              |
| שגיאות בשימוש ב-Conda                    | התקן ספריות AI של Microsoft באמצעות `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי אדם. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->