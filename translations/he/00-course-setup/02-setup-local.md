# הגדרה מקומית 🖥️

**השתמש במדריך זה אם אתה מעדיף להפעיל הכל במחשב הנייד שלך.**   
יש לך שני מסלולים: **(A) פייתון מקורי + virtual-env** או **(B) VS Code Dev Container עם Docker**.  
בחר מה שנוח לך יותר—שניהם מובילים לאותם השיעורים.

## 1. דרישות מוקדמות

| כלי                | גרסה / הערות                                                                       |
|--------------------|------------------------------------------------------------------------------------|
| **Python**          | 3.10 + (קבל אותו מ- <https://python.org>)                                         |
| **Git**             | העדכנית ביותר (כולל Xcode / Git for Windows / מנהל החבילות בלינוקס)               |
| **VS Code**         | אופציונלי אך מומלץ <https://code.visualstudio.com>                                 |
| **Docker Desktop**  | *רק* לאפשרות B. התקנה חינמית: <https://docs.docker.com/desktop/>                  |

> 💡 **טיפ** – אמת את הכלים בטרמינל:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. אפשרות A – פייתון מקורי (המהיר ביותר)

### שלב 1  שלח את המאגר

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

✅ השורת הפקודה צריכה להתחיל כעת עם (.venv)—זה אומר שאתה בתוך הסביבה.

### שלב 3 התקן את התלויות

```bash
pip install -r requirements.txt
```

קפוץ לסעיף 3 לגבי [מפתחות API](#3-הוסף-את-מפתחות-ה-api-שלך)

## 2. אפשרות B – VS Code Dev Container (Docker)

הקמנו את המאגר והקורס הזה עם [מיכל פיתוח](https://containers.dev?WT.mc_id=academic-105485-koreyst) שיש בו סביבה אוניברסלית שתומכת בפיתוח ב-Python3, .NET, Node.js ו-Java. ההגדרה הרלוונטית מוגדרת בקובץ `devcontainer.json` שנמצא בתיקיית `.devcontainer/` בשורש המאגר.

>**למה לבחור בזה?**
>סביבה זהה ל-Codespaces; ללא סטיות תלות.

### שלב 0 התקן תוספים

Docker Desktop – אמת עם ```docker --version```.
תוסף VS Code Remote – Containers (מזהה: ms-vscode-remote.remote-containers).

### שלב 1 פתח את המאגר ב-VS Code

קובץ ▸ פתח תיקיה…  → generative-ai-for-beginners

VS Code מזהה את .devcontainer/ ומציג התראה.

### שלב 2 פתח מחדש בתוך המיכל

לחץ על "פתח מחדש במיכל". Docker בונה את התמונה (≈ 3 דקות בפעם הראשונה).
כאשר מופיעה שורת הפקודה בטרמינל, אתה בתוך המיכל.

## 2. אפשרות C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) היא מתקן התקנה קל משקל להתקנת [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), פייתון, וכמה חבילות נוספות.
Conda היא מנהל חבילות, שמקל על הקמת והחלפה בין סביבות [פייתון וירטואליות](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) וחבילות שונות. היא גם שימושית להתקנת חבילות שלא זמינות דרך `pip`.

### שלב 0 התקן Miniconda

פעל לפי [מדריך ההתקנה של MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) כדי להתקין.

```bash
conda --version
```

### שלב 1 צור סביבה וירטואלית

צור קובץ סביבה חדש (*environment.yml*). אם אתה עובד עם Codespaces, צור אותו בתוך תיקיית `.devcontainer` כלומר `.devcontainer/environment.yml`.

### שלב 2 מלא את קובץ הסביבה

הוסף את הקטע הבא ל-`environment.yml` שלך

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

הפעל את הפקודות למטה בשורת הפקודה/טרמינל שלך

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer התיקייה המשנית חלה רק על הגדרות Codespace בלבד
conda activate ai4beg
```

עיין ב-[מדריך הסביבות של Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) אם נתקלת בבעיות.

## 2  אפשרות D – Jupyter קלאסי / Jupyter Lab (בדפדפן שלך)

> **למי זה מיועד?**  
> למי שאוהב את הממשק הקלאסי של Jupyter או רוצה להפעיל פנקסים ללא VS Code.  

### שלב 1 ודא ש-Jupyter מותקן

כדי להפעיל את Jupyter מקומית, עבור לטרמינל/שורת הפקודה, נווט לתיקיית הקורס והפעל:

```bash
jupyter notebook
```

או

```bash
jupyterhub
```

זה יפעיל מופע Jupyter וכתובת ה-URL לגישה אליו תוצג בחלון שורת הפקודה.

ברגע שתיגש לכתובת ה-URL, תראה את מתווה הקורס ותוכל לנווט לכל קובץ `*.ipynb`. לדוגמה, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. הוסף את מפתחות ה-API שלך

שמירת מפתחות ה-API שלך בטוחים ומאובטחים חשובה כשבונים כל סוג של יישום. אנו ממליצים לא לאחסן מפתחות API ישירות בקוד שלך. התחייבות לפרטים אלו במאגר ציבורי עלולה לגרום לבעיות אבטחה ואפילו עלויות לא רצויות אם הם ינוצלו על ידי גורם זדוני.
הנה מדריך שלב אחר שלב כיצד ליצור קובץ `.env` עבור פייתון ולהוסיף את אישורי Microsoft Foundry Models שלך:

> **הערה:** GitHub Models (והמשתנה `GITHUB_TOKEN`) יפורש בסוף יולי 2026. מדריך זה משתמש ב-[Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) במקום. מעדיף לעבוד במצב לא מקוון? ראה [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **נווט לתיקיית הפרויקט שלך**: פתח את הטרמינל או שורת הפקודה ונווט לשורש תיקיית הפרויקט שבו ברצונך ליצור את קובץ `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **צור את הקובץ `.env`**: השתמש בעורך הטקסט המועדף עליך כדי ליצור קובץ חדש בשם `.env`. אם אתה עובד בשורת הפקודה, תוכל להשתמש ב-`touch` (במערכות מבוססות יוניקס) או ב-`echo` (בווינדוס):

   מערכות מבוססות יוניקס:

   ```bash
   touch .env
   ```

   ווינדוס:

   ```cmd
   echo . > .env
   ```

3. **ערוך את הקובץ `.env`**: פתח את הקובץ `.env` בעורך טקסט (למשל VS Code, Notepad++ או כל עורך אחר). הוסף את השורות הבאות, כשה-placeholder מוחלף בסיום הפרויקט ו-key של Microsoft Foundry שלך:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **שמור את הקובץ**: שמור את השינויים וסגור את עורך הטקסט.

5. **התקן את `python-dotenv`**: אם עדיין לא התקנת, תצטרך להתקין את חבילת `python-dotenv` כדי לטעון משתני סביבה מקובץ `.env` ליישום הפייתון שלך. תוכל להתקין אותה עם `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **טען משתני סביבה בסקריפט הפייתון שלך**: בסקריפט הפייתון שלך השתמש בחבילת `python-dotenv` כדי לטעון את משתני הסביבה מקובץ `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # טען משתני סביבה מקובץ .env
   load_dotenv()

   # גש למשתני דגמי Microsoft Foundry
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

זהו זה! יצרת בהצלחה קובץ `.env`, הוספת את אישורי Microsoft Foundry Models, וטעינתם לתוך יישום הפייתון שלך.

🔐 לעולם אל תתחייב ל-.env—הוא כבר נמצא בקובץ .gitignore.
הוראות ספק מלאות נמצאות ב-[`providers.md`](03-providers.md).

## 4. מה הלאה?

| אני רוצה…               | עבור אל…                                                               |
|-------------------------|-----------------------------------------------------------------------|
| להתחיל בשיעור 1         | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)   |
| להגדיר ספק LLM         | [`providers.md`](03-providers.md)                                     |
| לפגוש תלמידים אחרים     | [הצטרף לדיסקורד שלנו](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. פתרון תקלות

| תסמין                                    | תיקון                                                        |
|-------------------------------------------|------------------------------------------------------------|
| `python not found`                       | הוסף את Python ל-PATH או פתח מחדש את הטרמינל לאחר ההתקנה |
| `pip` לא מצליח לבנות גלגלים (Windows)    | הפעל `pip install --upgrade pip setuptools wheel` ואז נסה שוב.   |
| `ModuleNotFoundError: dotenv`            | הפעל `pip install -r requirements.txt` (הסביבה לא הותקנה).   |
| בניית Docker נכשלת *No space left*      | Docker Desktop ▸ *הגדרות* ▸ *משאבים* → הגדל את גודל הדיסק.  |
| VS Code ממשיך להציע לפתוח מחדש          | ייתכן שכל שתי האפשרויות פעילות; בחר אחת (venv **או** מיכל)     |
| שגיאות OpenAI 401 / 429                  | בדוק את ערך `OPENAI_API_KEY` / הגבלות קצב הבקשות.            |
| שגיאות בעת שימוש ב-Conda                  | התקן ספריות AI של מיקרוסופט באמצעות `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->