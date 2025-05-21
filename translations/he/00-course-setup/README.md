<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-05-19T12:30:37+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "he"
}
-->
# התחלת קורס זה

אנחנו מאוד מתרגשים שתתחיל את הקורס הזה ונראה מה תתן לך השראה לבנות עם AI גנרטיבי!

כדי להבטיח את הצלחתך, דף זה מתאר את שלבי ההגדרה, הדרישות הטכניות, ואיפה לקבל עזרה אם יש צורך.

## שלבי הגדרה

כדי להתחיל לקחת את הקורס הזה, תצטרך להשלים את השלבים הבאים.

### 1. יצירת Fork למאגר זה

[צור Fork למאגר כולו](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) לחשבון GitHub שלך כדי שתוכל לשנות כל קוד ולהשלים את האתגרים. אתה יכול גם [לככב (🌟) למאגר זה](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) כדי למצוא אותו ומאגרים קשורים בקלות רבה יותר.

### 2. יצירת Codespace

כדי להימנע מבעיות תלות בעת הרצת הקוד, אנו ממליצים להריץ את הקורס הזה ב-[GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

זה יכול להיווצר על ידי בחירת האפשרות `Code` בגרסת ה-Fork שלך של המאגר הזה ובחירת האפשרות **Codespaces**.

![דיאלוג שמראה כפתורים ליצירת Codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. אחסון מפתחות ה-API שלך

שמירת מפתחות ה-API שלך בטוחים ומאובטחים היא חשובה בעת בניית כל סוג של יישום. אנו ממליצים לא לאחסן מפתחות API ישירות בקוד שלך. התחייבות לפרטים אלה למאגר ציבורי יכולה לגרום לבעיות אבטחה ואפילו עלויות לא רצויות אם ישמשו על ידי שחקן רע.
הנה מדריך שלב אחר שלב כיצד ליצור קובץ `.env` עבור Python ולהוסיף את `GITHUB_TOKEN`:

1. **נווט לתיקיית הפרויקט שלך**: פתח את הטרמינל או שורת הפקודה ונווט לתיקיית השורש של הפרויקט שלך שבה אתה רוצה ליצור את קובץ `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **צור את קובץ `.env`**: השתמש בעורך הטקסט המועדף עליך כדי ליצור קובץ חדש בשם `.env`. אם אתה משתמש בשורת הפקודה, תוכל להשתמש ב-`touch` (on Unix-based systems) or `echo` (ב-Windows):

   מערכות מבוססות Unix:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **ערוך את קובץ `.env`**: פתח את קובץ `.env` בעורך טקסט (לדוגמה, VS Code, Notepad++ או כל עורך אחר). הוסף את השורה הבאה לקובץ, החלף `your_github_token_here` בטוקן GitHub שלך:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **שמור את הקובץ**: שמור את השינויים וסגור את עורך הטקסט.

5. **התקן את חבילת `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` כדי לטעון משתני סביבה מהקובץ `.env` לתוך יישום Python שלך. תוכל להתקין אותה באמצעות `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **טען משתני סביבה בתסריט Python שלך**: בתסריט Python שלך, השתמש בחבילת `python-dotenv` כדי לטעון את משתני הסביבה מהקובץ `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

זהו זה! יצרת בהצלחה קובץ `.env`, הוספת את הטוקן GitHub שלך וטענת אותו לתוך יישום Python שלך.

## כיצד להריץ מקומית על המחשב שלך

כדי להריץ את הקוד מקומית על המחשב שלך, תצטרך שיהיה לך גרסה כלשהי של [Python מותקנת](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

כדי להשתמש במאגר, אתה צריך לשכפל אותו:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

ברגע שיש לך הכל מאומת, אתה יכול להתחיל!

## שלבים אופציונליים

### התקנת Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) הוא מתקין קל משקל להתקנת [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, כמו גם כמה חבילות.
Conda עצמה היא מנהל חבילות, שמקל על הגדרת והחלפת בין [**סביבות וירטואליות**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) שונות של Python וחבילות. זה גם שימושי להתקנת חבילות שלא זמינות באמצעות `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

לך קדימה ואכלס את קובץ הסביבה שלך עם הקטע הבא:

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

אם אתה מוצא שאתה מקבל שגיאות בשימוש ב-conda אתה יכול להתקין ידנית את ספריות ה-AI של Microsoft באמצעות הפקודה הבאה בטרמינל.

```
conda install -c microsoft azure-ai-ml
```

קובץ הסביבה מפרט את התלות שאנחנו צריכים. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` הוא הגרסה הראשית האחרונה של Python.

עם זה נעשה, אתה יכול להמשיך וליצור את סביבת Conda שלך על ידי הרצת הפקודות הבאות בשורת הפקודה/טרמינל שלך

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

עיין במדריך הסביבות של [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) אם אתה נתקל בבעיות.

### שימוש ב-Visual Studio Code עם הרחבת תמיכת Python

אנו ממליצים להשתמש בעורך [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) עם הרחבת [תמיכת Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) מותקנת לקורס זה. זה, עם זאת, יותר המלצה ולא דרישה מוחלטת

> **הערה**: על ידי פתיחת מאגר הקורס ב-VS Code, יש לך את האפשרות להגדיר את הפרויקט בתוך מיכל. זאת בגלל [תיקיית `.devcontainer` מיוחדת](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) שנמצאת בתוך מאגר הקורס. עוד על זה מאוחר יותר.

> **הערה**: ברגע שאתה משכפל ופותח את התיקייה ב-VS Code, הוא יציע אוטומטית להתקין הרחבת תמיכת Python.

> **הערה**: אם VS Code מציע לך לפתוח מחדש את המאגר במיכל, דחה את הבקשה הזו כדי להשתמש בגרסה המקומית המותקנת של Python.

### שימוש ב-Jupyter בדפדפן

אתה יכול גם לעבוד על הפרויקט באמצעות סביבת [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ישירות בדפדפן שלך. גם Jupyter הקלאסי וגם [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) מספקים סביבת פיתוח נעימה למדי עם תכונות כמו השלמה אוטומטית, הדגשת קוד, ועוד.

כדי להתחיל את Jupyter מקומית, פנה לטרמינל/שורת הפקודה, נווט לתיקיית הקורס, ובצע:

```bash
jupyter notebook
```

או

```bash
jupyterhub
```

זה יתחיל מופע Jupyter וה-URL לגישה אליו יוצג בתוך חלון שורת הפקודה.

ברגע שאתה ניגש ל-URL, אתה אמור לראות את מתווה הקורס ולהיות מסוגל לנווט לכל קובץ `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` שבו אתה יכול לצפות בקוד ובפלטים.

## שימוש בשירות Azure OpenAI בפעם הראשונה

אם זו הפעם הראשונה שלך בעבודה עם שירות Azure OpenAI, אנא עקוב אחר מדריך זה כיצד [ליצור ולפרוס משאב שירות Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## שימוש ב-API של OpenAI בפעם הראשונה

אם זו הפעם הראשונה שלך בעבודה עם ה-API של OpenAI, אנא עקוב אחר המדריך כיצד [ליצור ולהשתמש בממשק.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## פגוש לומדים אחרים

יצרנו ערוצים בשרת [Discord של קהילת AI הרשמית שלנו](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) למפגש עם לומדים אחרים. זו דרך מצוינת ליצור קשר עם יזמים, בונים, סטודנטים, וכל מי שמחפש לשפר את יכולותיו ב-AI גנרטיבי.

[![הצטרף לערוץ דיסקורד](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

צוות הפרויקט יהיה גם בשרת דיסקורד זה כדי לעזור לכל לומד.

## תרום

הקורס הזה הוא יוזמה קוד פתוח. אם אתה רואה אזורים לשיפור או בעיות, אנא צור [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) או רשום [בעיה ב-GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

צוות הפרויקט יעקוב אחרי כל התרומות. תרומה לקוד פתוח היא דרך מדהימה לבנות את הקריירה שלך ב-AI גנרטיבי.

רוב התרומות דורשות ממך להסכים להסכם רישיון תורם (CLA) שמצהיר שיש לך את הזכות ולמעשה מעניק לנו את הזכויות להשתמש בתרומתך. לפרטים, בקר באתר [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

חשוב: בעת תרגום טקסט במאגר זה, אנא וודא שאתה לא משתמש בתרגום מכונה. אנחנו נאמת תרגומים דרך הקהילה, אז אנא התנדב רק לתרגומים בשפות שבהן אתה שולט.

כאשר אתה שולח בקשת משיכה, CLA-bot יקבע אוטומטית אם אתה צריך לספק CLA ויעטר את PR בהתאם (למשל, תווית, תגובה). פשוט עקוב אחר ההוראות שסופקו על ידי הבוט. תצטרך לעשות זאת רק פעם אחת בכל המאגרי שלנו המשתמשים ב-CLA שלנו.

פרויקט זה אימץ את [קוד ההתנהגות של קוד פתוח של Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). למידע נוסף קרא את השאלות הנפוצות על קוד ההתנהגות או צור קשר עם [Email opencode](opencode@microsoft.com) עם שאלות או הערות נוספות.

## בוא נתחיל

עכשיו כשסיימת את השלבים הנדרשים להשלמת הקורס הזה, בוא נתחיל על ידי קבלת [מבוא ל-AI גנרטיבי ו-LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). בעוד אנו שואפים לדיוק, אנא היו מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. אנו לא אחראים לכל אי הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.