<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T17:56:36+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "he"
}
-->
# התקנה מקומית 🖥️

**השתמש במדריך הזה אם אתה מעדיף להריץ הכל על הלפטופ שלך.**  
יש לך שתי אפשרויות: **(A) פייתון מקורי + virtual-env** או **(B) VS Code Dev Container עם Docker**.  
בחר מה שנוח לך—שתיהן מובילות לאותם שיעורים.

## 1. דרישות מוקדמות

| כלי                | גרסה / הערות                                                                       |
|--------------------|------------------------------------------------------------------------------------|
| **Python**         | 3.10 ומעלה (להורדה מ-<https://python.org>)                                         |
| **Git**            | הגרסה האחרונה (מגיע עם Xcode / Git ל-Windows / מנהל חבילות בלינוקס)                |
| **VS Code**        | לא חובה אבל מומלץ <https://code.visualstudio.com>                                  |
| **Docker Desktop** | *רק* לאפשרות B. התקנה חינמית: <https://docs.docker.com/desktop/>                   |

> 💡 **טיפ** – בדוק את הכלים בטרמינל:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. אפשרות A – פייתון מקורי (הכי מהיר)

### שלב 1  שכפל את המאגר הזה

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### שלב 2 צור והפעל סביבה וירטואלית

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ כעת השורה בטרמינל אמורה להתחיל ב-(.venv)—זה אומר שאתה בתוך הסביבה.

### שלב 3 התקן את התלויות

```bash
pip install -r requirements.txt
```

דלג לסעיף 3 על [מפתחות API](../../../00-course-setup)

## 2. אפשרות B – VS Code Dev Container (Docker)

הגדרנו את המאגר הזה ואת הקורס עם [קונטיינר פיתוח](https://containers.dev?WT.mc_id=academic-105485-koreyst) שיש לו סביבת ריצה אוניברסלית שיכולה לתמוך בפיתוח ב-Python3, .NET, Node.js ו-Java. ההגדרות נמצאות בקובץ `devcontainer.json` בתיקיית `.devcontainer/` בשורש המאגר.

>**למה לבחור בזה?**
>סביבה זהה ל-Codespaces; אין סטייה בתלויות.

### שלב 0 התקן את התוספות

Docker Desktop – ודא ש-```docker --version``` עובד.
VS Code Remote – הרחבת Containers (מזהה: ms-vscode-remote.remote-containers).

### שלב 1 פתח את המאגר ב-VS Code

קובץ ▸ פתח תיקיה…  → generative-ai-for-beginners

VS Code מזהה את .devcontainer/ ומציג הודעה.

### שלב 2 פתח מחדש בתוך קונטיינר

לחץ על “Reopen in Container”. Docker בונה את התמונה (≈ 3 דקות בפעם הראשונה).
כשהטרמינל מופיע, אתה בתוך הקונטיינר.

## 2. אפשרות C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) הוא מתקין קל להתקנת [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), פייתון, וכמה חבילות.
Conda הוא מנהל חבילות שמקל להגדיר ולעבור בין [**סביבות וירטואליות**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) שונות של פייתון וחבילות. הוא גם שימושי להתקנת חבילות שלא זמינות דרך `pip`.

### שלב 0  התקן Miniconda

עקוב אחרי [מדריך ההתקנה של MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) כדי להגדיר אותו.

```bash
conda --version
```

### שלב 1 צור סביבה וירטואלית

צור קובץ סביבה חדש (*environment.yml*). אם אתה עובד עם Codespaces, צור אותו בתוך תיקיית `.devcontainer`, כלומר `.devcontainer/environment.yml`.

### שלב 2  מלא את קובץ הסביבה שלך

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

### שלב 3 צור את סביבת ה-Conda שלך

הרץ את הפקודות הבאות בטרמינל/שורת הפקודה שלך

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

עיין ב-[מדריך סביבות Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) אם אתה נתקל בבעיות.

## 2  אפשרות D – Jupyter קלאסי / Jupyter Lab (בדפדפן שלך)

> **למי זה מתאים?**  
> כל מי שאוהב את הממשק הקלאסי של Jupyter או רוצה להריץ מחברות בלי VS Code.  

### שלב 1  ודא ש-Jupyter מותקן

כדי להפעיל Jupyter מקומית, עבור לטרמינל/שורת הפקודה, נווט לתיקיית הקורס, והרץ:

```bash
jupyter notebook
```

או

```bash
jupyterhub
```

זה יפעיל מופע של Jupyter והכתובת לגישה תוצג בחלון שורת הפקודה.

לאחר שתיכנס לכתובת, תראה את מבנה הקורס ותוכל לנווט לכל קובץ `*.ipynb`. לדוגמה, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. הוסף את מפתחות ה-API שלך

שמירה על מפתחות ה-API שלך בטוחים ופרטיים חשובה בכל פיתוח אפליקציה. מומלץ לא לשמור מפתחות API ישירות בקוד שלך. אם תעלה אותם למאגר ציבורי, זה עלול לגרום לבעיות אבטחה ואפילו להוצאות לא רצויות אם מישהו ינצל אותם.
הנה מדריך שלב-אחר-שלב ליצירת קובץ `.env` לפייתון והוספת `GITHUB_TOKEN`:

1. **נווט לתיקיית הפרויקט שלך**: פתח את הטרמינל או שורת הפקודה ונווט לתיקיית השורש של הפרויקט, שם תרצה ליצור את קובץ ה-`.env`.

   ```bash
   cd path/to/your/project
   ```

2. **צור את קובץ ה-`.env`**: השתמש בעורך הטקסט המועדף עליך כדי ליצור קובץ חדש בשם `.env`. אם אתה משתמש בשורת הפקודה, תוכל להשתמש ב-`touch` (במערכות מבוססות יוניקס) או `echo` (ב-Windows):

   מערכות מבוססות יוניקס:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **ערוך את קובץ ה-`.env`**: פתח את קובץ ה-`.env` בעורך טקסט (למשל VS Code, Notepad++, או כל עורך אחר). הוסף את השורה הבאה לקובץ, והחלף את `your_github_token_here` בטוקן שלך:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **שמור את הקובץ**: שמור את השינויים וסגור את העורך.

5. **התקן את `python-dotenv`**: אם עדיין לא עשית זאת, תצטרך להתקין את החבילה `python-dotenv` כדי לטעון משתני סביבה מקובץ ה-`.env` לאפליקציית הפייתון שלך. תוכל להתקין אותה עם `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **טען משתני סביבה בסקריפט הפייתון שלך**: בסקריפט שלך, השתמש ב-`python-dotenv` כדי לטעון את המשתנים מקובץ ה-`.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

זהו! יצרת קובץ `.env`, הוספת את הטוקן של GitHub, וטעינת אותו לאפליקציית הפייתון שלך.

🔐 לעולם אל תעלה את .env—הוא כבר נמצא ב-.gitignore.
הוראות מלאות לכל ספק נמצאות ב-[`providers.md`](03-providers.md).

## 4. מה הלאה?

| אני רוצה…           | עבור אל…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| להתחיל שיעור 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| להגדיר ספק LLM      | [`providers.md`](03-providers.md)                                       |
| להכיר לומדים נוספים | [הצטרף ל-Discord שלנו](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. פתרון תקלות

| סימפטום                                   | פתרון                                                           |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | הוסף את פייתון ל-PATH או פתח מחדש את הטרמינל אחרי ההתקנה        |
| `pip` לא מצליח לבנות wheels (Windows)    | `pip install --upgrade pip setuptools wheel` ואז נסה שוב.        |
| `ModuleNotFoundError: dotenv`             | הרץ `pip install -r requirements.txt` (הסביבה לא הותקנה).        |
| Docker build נכשל *No space left*         | Docker Desktop ▸ *הגדרות* ▸ *משאבים* → הגדל את גודל הדיסק.      |
| VS Code ממשיך להציע לפתוח מחדש            | ייתכן ששתי אפשרויות פעילות; בחר אחת (venv **או** container)      |
| שגיאות OpenAI 401 / 429                   | בדוק את הערך של `OPENAI_API_KEY` / מגבלות קצב הבקשות.           |
| שגיאות עם Conda                           | התקן ספריות AI של Microsoft עם `conda install -c microsoft azure-ai-ml`|

---

**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית הוא המקור הסמכותי. למידע קריטי, מומלץ לפנות לתרגום מקצועי על ידי אדם. איננו אחראים לכל אי-הבנה או פירוש שגוי הנובעים מהשימוש בתרגום זה.