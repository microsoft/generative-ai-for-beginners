<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:12:56+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "he"
}
-->
# התחלה עם הקורס הזה

אנחנו מאוד מתרגשים שאתה מתחיל את הקורס הזה ומגלים מה תתלהב לבנות עם Generative AI!

כדי להבטיח את ההצלחה שלך, עמוד זה מפרט את שלבי ההתקנה, הדרישות הטכניות, ואיפה לקבל עזרה במידת הצורך.

## שלבי התקנה

כדי להתחיל ללמוד את הקורס, תצטרך להשלים את השלבים הבאים.

### 1. יצירת Fork לריפוזיטורי הזה

[צור Fork לכל הריפוזיטורי הזה](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) לחשבון ה-GitHub שלך כדי שתוכל לשנות כל קוד ולהשלים את האתגרים. בנוסף, תוכל גם [להוסיף כוכב (🌟) לריפוזיטורי הזה](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) כדי למצוא אותו ואת הריפוזיטוריים הקשורים בקלות רבה יותר.

### 2. יצירת Codespace

כדי למנוע בעיות תלות בעת הרצת הקוד, אנו ממליצים להריץ את הקורס הזה ב-[GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

ניתן ליצור זאת על ידי בחירת אפשרות `Code` בגרסה שלך של הריפוזיטורי ולבחור באפשרות **Codespaces**.

![דיאלוג המציג כפתורים ליצירת codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. אחסון מפתחות ה-API שלך

שמירה על מפתחות ה-API שלך בטוחים ומוגנים היא חשובה כשבונים כל סוג של אפליקציה. אנו ממליצים לא לאחסן מפתחות API ישירות בקוד שלך. העלאת פרטים אלה לריפוזיטורי ציבורי עלולה לגרום לבעיות אבטחה ואפילו לעלויות לא רצויות אם ייעשה בהם שימוש על ידי גורם זדוני.  
הנה מדריך שלב-אחר-שלב כיצד ליצור קובץ `.env` לפייתון ולהוסיף את `GITHUB_TOKEN`:

1. **נווט לתיקיית הפרויקט שלך**: פתח את הטרמינל או שורת הפקודה ונווט לתיקיית השורש של הפרויקט שלך שבה תרצה ליצור את קובץ ה-`.env`.

   ```bash
   cd path/to/your/project
   ```

2. **צור את קובץ ה-`.env`**: השתמש בעורך הטקסט המועדף עליך כדי ליצור קובץ חדש בשם `.env`. אם אתה עובד בשורת הפקודה, תוכל להשתמש בפקודת `touch` (במערכות מבוססות יוניקס) או `echo` (בווינדוס):

   מערכות מבוססות יוניקס:

   ```bash
   touch .env
   ```

   ווינדוס:

   ```cmd
   echo . > .env
   ```

3. **ערוך את קובץ ה-`.env`**: פתח את קובץ ה-`.env` בעורך טקסט (למשל VS Code, Notepad++ או כל עורך אחר). הוסף את השורה הבאה לקובץ, כשהחלף את `your_github_token_here` במפתח GitHub האמיתי שלך:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **שמור את הקובץ**: שמור את השינויים וסגור את עורך הטקסט.

5. **התקן את `python-dotenv`**: אם עדיין לא התקנת, תצטרך להתקין את חבילת `python-dotenv` כדי לטעון משתני סביבה מקובץ ה-`.env` לאפליקציית הפייתון שלך. ניתן להתקין באמצעות `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **טען משתני סביבה בסקריפט הפייתון שלך**: בסקריפט הפייתון שלך, השתמש בחבילת `python-dotenv` כדי לטעון את משתני הסביבה מקובץ ה-`.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

זהו! יצרת בהצלחה קובץ `.env`, הוספת את מפתח ה-GitHub שלך וטעונת אותו לאפליקציית הפייתון שלך.

## איך להריץ מקומית במחשב שלך

כדי להריץ את הקוד מקומית במחשב שלך, תצטרך שיהיה מותקן אצלך [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

כדי להשתמש בריפוזיטורי, תצטרך לשכפל אותו:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

לאחר שיש לך את כל הקבצים, תוכל להתחיל!

## שלבים אופציונליים

### התקנת Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) הוא מתקין קל משקל להתקנת [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), פייתון, וכמה חבילות נוספות.  
Conda היא מנהל חבילות שמקל על ההתקנה והמעבר בין [סביבות וירטואליות](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) שונות של פייתון וחבילות. היא גם שימושית להתקנת חבילות שאינן זמינות דרך `pip`.

תוכל לעקוב אחרי [מדריך ההתקנה של MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) כדי להגדיר זאת.

לאחר התקנת Miniconda, תצטרך לשכפל את [הריפוזיטורי](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (אם עדיין לא עשית זאת).

לאחר מכן, תצטרך ליצור סביבה וירטואלית. כדי לעשות זאת עם Conda, צור קובץ סביבה חדש (_environment.yml_). אם אתה עובד עם Codespaces, צור אותו בתוך תיקיית `.devcontainer`, כלומר `.devcontainer/environment.yml`.

מלא את קובץ הסביבה שלך עם הקטע הבא:

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

אם אתה נתקל בשגיאות בשימוש ב-conda, תוכל להתקין ידנית את ספריות ה-Microsoft AI באמצעות הפקודה הבאה בטרמינל.

```
conda install -c microsoft azure-ai-ml
```

קובץ הסביבה מגדיר את התלויות הדרושות לנו. `<environment-name>` מתייחס לשם שתרצה לתת לסביבת ה-Conda שלך, ו-`<python-version>` היא גרסת הפייתון שברצונך להשתמש בה, לדוגמה, `3` היא הגרסה העיקרית האחרונה של פייתון.

לאחר מכן, תוכל ליצור את סביבת ה-Conda שלך על ידי הרצת הפקודות הבאות בשורת הפקודה/טרמינל:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

אם תיתקל בבעיות, עיין ב-[מדריך סביבות Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### שימוש ב-Visual Studio Code עם תוסף התמיכה בפייתון

אנו ממליצים להשתמש בעורך [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) עם [תוסף התמיכה בפייתון](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) מותקן עבור הקורס הזה. עם זאת, זו המלצה בלבד ולא דרישה מחייבת.

> **הערה**: בעת פתיחת ריפוזיטורי הקורס ב-VS Code, יש לך אפשרות להגדיר את הפרויקט בתוך מכולה (container). זאת בזכות תיקיית ה-[`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) המיוחדת שנמצאת בריפוזיטורי הקורס. נרחיב על כך בהמשך.

> **הערה**: לאחר ששכפלת ופתחת את התיקייה ב-VS Code, הוא יציע אוטומטית להתקין את תוסף התמיכה בפייתון.

> **הערה**: אם VS Code מציע לפתוח מחדש את הריפוזיטורי בתוך מכולה, סרב לבקשה זו כדי להשתמש בגרסת הפייתון המותקנת מקומית.

### שימוש ב-Jupyter בדפדפן

ניתן גם לעבוד על הפרויקט באמצעות סביבת [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ישירות בדפדפן שלך. גם Jupyter הקלאסי וגם [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) מספקים סביבת פיתוח נוחה עם תכונות כמו השלמה אוטומטית, הדגשת קוד ועוד.

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

### הרצה בתוך מכולה (container)

חלופה להגדרת הכל במחשב שלך או ב-Codespace היא שימוש ב-[מכולה](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). תיקיית ה-`.devcontainer` המיוחדת בריפוזיטורי הקורס מאפשרת ל-VS Code להגדיר את הפרויקט בתוך מכולה. מחוץ ל-Codespaces, זה ידרוש התקנת Docker, ובאופן כללי מדובר בעבודה מסוימת, לכן אנו ממליצים על כך רק למי שיש לו ניסיון בעבודה עם מכולות.

אחת הדרכים הטובות ביותר לשמור על מפתחות ה-API שלך בטוחים בעת שימוש ב-GitHub Codespaces היא באמצעות Codespace Secrets. אנא עקוב אחרי מדריך [ניהול סודות ב-Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) כדי ללמוד עוד על כך.

## שיעורים ודרישות טכניות

הקורס כולל 6 שיעורי מושג ו-6 שיעורי קידוד.

בשיעורי הקידוד אנו משתמשים בשירות Azure OpenAI. תצטרך גישה לשירות Azure OpenAI ומפתח API כדי להריץ את הקוד. ניתן להגיש בקשה לקבלת גישה על ידי [מילוי טופס זה](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

בזמן שאתה ממתין לעיבוד הבקשה שלך, כל שיעור קידוד כולל גם קובץ `README.md` שבו תוכל לצפות בקוד ובפלטים.

## שימוש בשירות Azure OpenAI בפעם הראשונה

אם זו הפעם הראשונה שלך בעבודה עם שירות Azure OpenAI, אנא עקוב אחרי המדריך כיצד [ליצור ולפרוס משאב שירות Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## שימוש ב-OpenAI API בפעם הראשונה

אם זו הפעם הראשונה שלך בעבודה עם OpenAI API, אנא עקוב אחרי המדריך כיצד [ליצור ולהשתמש בממשק.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## הכירו לומדים אחרים

יצרנו ערוצים בשרת ה-[Discord הרשמי של קהילת ה-AI שלנו](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) כדי להכיר לומדים אחרים. זו דרך מצוינת ליצור קשר עם יזמים, בוני פרויקטים, סטודנטים וכל מי שמעוניין להתקדם בתחום ה-Generative AI.

[![הצטרף לערוץ דיסקורד](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

צוות הפרויקט יהיה גם הוא בשרת דיסקורד זה כדי לסייע לכל הלומדים.

## תרומה

הקורס הזה הוא יוזמה בקוד פתוח. אם אתה רואה תחומים לשיפור או בעיות, אנא צור [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) או דווח על [בעיה ב-GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

צוות הפרויקט יעקוב אחרי כל התרומות. תרומה לקוד פתוח היא דרך נהדרת לבנות את הקריירה שלך ב-Generative AI.

רוב התרומות מחייבות הסכמה להסכם רישיון תורם (CLA) המצהיר שיש לך את הזכות, ושאתה מעניק לנו את הזכויות להשתמש בתרומתך. לפרטים, בקר ב-[אתר הסכם הרישיון לתורמים (CLA)](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

חשוב: בעת תרגום טקסט בריפוזיטורי זה, ודא שאינך משתמש בתרגום מכונה. נבדוק את התרגומים דרך הקהילה, לכן אנא התנדב לתרגום רק בשפות שבהן אתה שולט.

כאשר תגיש Pull Request, בוט CLA יזהה אוטומטית אם עליך לספק CLA ויעניק תגיות מתאימות ל-PR (כגון תווית, תגובה). פשוט עקוב אחר ההוראות של הבוט. תצטרך לעשות זאת רק פעם אחת בכל הריפוזיטוריים המשתמשים ב-CLA שלנו.

פרויקט זה אימץ את [קוד ההתנהגות של מיקרוסופט לקוד פתוח](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). למידע נוסף קרא את שאלות נפוצות על קוד ההתנהגות או פנה ל-[דוא"ל opencode](opencode@microsoft.com) עם שאלות או הערות נוספות.

## בואו נתחיל

כעת, לאחר שסיימת את השלבים הנדרשים להשלמת הקורס, בוא נתחיל עם [הקדמה ל-Generative AI ול-LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי אדם. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.