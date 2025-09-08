<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T17:58:22+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "he"
}
-->
# מתחילים עם הקורס הזה

אנחנו מאוד מתרגשים שתתחיל את הקורס הזה ונראה לאן תגיע עם ההשראה שלך לבנות בעזרת בינה מלאכותית גנרטיבית!

כדי להבטיח את ההצלחה שלך, עמוד זה מסביר את שלבי ההגדרה, הדרישות הטכניות, ואיפה אפשר לקבל עזרה במידת הצורך.

## שלבי הגדרה

כדי להתחיל את הקורס, תצטרך להשלים את השלבים הבאים.

### 1. עשה Fork לריפוזיטורי הזה

[בצע Fork לכל הריפוזיטורי](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) לחשבון ה-GitHub שלך כדי שתוכל לשנות קוד ולהשלים את האתגרים. אפשר גם [לסמן בכוכב (🌟) את הריפוזיטורי](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) כדי למצוא אותו וריפוזיטוריז קשורים בקלות.

### 2. צור Codespace

כדי להימנע מבעיות תלויות בהרצת הקוד, אנחנו ממליצים להריץ את הקורס הזה ב-[GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

ב-Fork שלך: **Code -> Codespaces -> New on main**

![דיאלוג שמראה כפתורים ליצירת Codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 הוסף Secret

1. ⚙️ אייקון גלגל שיניים -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. תן שם OPENAI_API_KEY, הדבק את המפתח שלך, ושמור.

### 3. מה הלאה?

| אני רוצה…           | עבור אל…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| להתחיל שיעור 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| לעבוד לא מקוון      | [`setup-local.md`](02-setup-local.md)                                   |
| להגדיר ספק LLM      | [`providers.md`](providers.md)                                          |
| להכיר לומדים נוספים | [הצטרף ל-Discord שלנו](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## פתרון תקלות

| סימפטום                                   | פתרון                                                           |
|-------------------------------------------|-----------------------------------------------------------------|
| בניית הקונטיינר נתקעה ליותר מ-10 דקות     | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | הטרמינל לא התחבר; לחץ **+** ➜ *bash*                           |
| `401 Unauthorized` מ-OpenAI               | `OPENAI_API_KEY` שגוי או שפג תוקפו                              |
| VS Code מציג “Dev container mounting…”    | רענן את לשונית הדפדפן—Codespaces לפעמים מאבד חיבור              |
| חסר Kernel במחברת                         | תפריט המחברת ➜ **Kernel ▸ Select Kernel ▸ Python 3**            |

   מערכות מבוססות יוניקס:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **ערוך את קובץ `.env`**: פתח את קובץ ה-`.env` בעורך טקסט (למשל VS Code, Notepad++, או כל עורך אחר). הוסף את השורה הבאה לקובץ, והחלף את `your_github_token_here` בטוקן ה-GitHub שלך:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **שמור את הקובץ**: שמור את השינויים וסגור את עורך הטקסט.

5. **התקן את `python-dotenv`**: אם עדיין לא עשית זאת, תצטרך להתקין את החבילה `python-dotenv` כדי לטעון משתני סביבה מקובץ ה-`.env` לאפליקציית הפייתון שלך. אפשר להתקין בעזרת `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **טען משתני סביבה בסקריפט פייתון שלך**: בסקריפט שלך, השתמש ב-`python-dotenv` כדי לטעון את משתני הסביבה מקובץ ה-`.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

וזהו! יצרת בהצלחה קובץ `.env`, הוספת את טוקן ה-GitHub שלך, וטעינת אותו לאפליקציית הפייתון שלך.

## איך להריץ מקומית על המחשב שלך

כדי להריץ את הקוד מקומית על המחשב, תצטרך שתהיה מותקנת אצלך איזושהי גרסה של [פייתון](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

כדי להשתמש בריפוזיטורי, עליך לשכפל אותו:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

לאחר ששכפלת הכל, אפשר להתחיל!

## שלבים אופציונליים

### התקנת Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) הוא מתקין קל להתקנת [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), פייתון, וכמה חבילות נוספות.
Conda עצמו הוא מנהל חבילות שמקל להגדיר ולעבור בין [**סביבות וירטואליות**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) שונות של פייתון וחבילות. הוא גם שימושי להתקנת חבילות שלא זמינות דרך `pip`.

אפשר לעקוב אחרי [מדריך ההתקנה של MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) כדי להגדיר אותו.

לאחר התקנת Miniconda, יש לשכפל את [הריפוזיטורי](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (אם עדיין לא עשית זאת).

השלב הבא הוא ליצור סביבה וירטואלית. כדי לעשות זאת עם Conda, צור קובץ סביבה חדש (_environment.yml_). אם אתה עובד עם Codespaces, צור אותו בתוך תיקיית `.devcontainer`, כלומר `.devcontainer/environment.yml`.

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

אם אתה נתקל בשגיאות עם conda, אפשר להתקין ידנית את ספריות ה-AI של מיקרוסופט בעזרת הפקודה הבאה בטרמינל.

```
conda install -c microsoft azure-ai-ml
```

קובץ הסביבה מגדיר את התלויות הנדרשות. `<environment-name>` הוא שם הסביבה שתרצה, ו-`<python-version>` היא גרסת הפייתון, לדוג' `3` היא הגרסה העדכנית ביותר.

לאחר מכן, תוכל ליצור את סביבת ה-Conda שלך על ידי הרצת הפקודות הבאות בטרמינל/שורת הפקודה:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

אם נתקלת בבעיות, עיין ב-[מדריך סביבות Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### שימוש ב-Visual Studio Code עם תוסף תמיכה בפייתון

אנו ממליצים להשתמש בעורך [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) עם [תוסף תמיכה בפייתון](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) עבור הקורס הזה. זו המלצה בלבד ולא דרישה מחייבת.

> **הערה**: כאשר תפתח את ריפוזיטור הקורס ב-VS Code, תוכל להגדיר את הפרויקט בתוך קונטיינר. זה מתאפשר בזכות תיקיית [`.devcontainer` המיוחדת](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) שנמצאת בריפוזיטורי. עוד על כך בהמשך.

> **הערה**: לאחר שתשכפל ותפתח את התיקייה ב-VS Code, הוא יציע לך אוטומטית להתקין את תוסף הפייתון.

> **הערה**: אם VS Code מציע לפתוח את הריפוזיטורי בקונטיינר, דחה את הבקשה כדי להשתמש בגרסת הפייתון המקומית שלך.

### שימוש ב-Jupyter בדפדפן

אפשר גם לעבוד על הפרויקט בסביבת [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ישירות בדפדפן. גם Jupyter הקלאסי וגם [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) מספקים סביבת פיתוח נוחה עם השלמה אוטומטית, הדגשת קוד ועוד.

כדי להפעיל Jupyter מקומית, עבור לטרמינל/שורת הפקודה, נווט לתיקיית הקורס, והרץ:

```bash
jupyter notebook
```

או

```bash
jupyterhub
```

זה יפעיל מופע של Jupyter וה-URL לגישה יוצג בחלון שורת הפקודה.

לאחר שתיגש ל-URL, תראה את מבנה הקורס ותוכל לנווט לכל קובץ `*.ipynb`. לדוג', `08-building-search-applications/python/oai-solution.ipynb`.

### הרצה בקונטיינר

אפשרות נוספת היא להשתמש ב-[קונטיינר](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) במקום להגדיר הכל על המחשב או ב-Codespace. תיקיית `.devcontainer` המיוחדת בריפוזיטורי מאפשרת ל-VS Code להגדיר את הפרויקט בתוך קונטיינר. מחוץ ל-Codespaces, זה דורש התקנת Docker, וזה מעט מורכב, לכן אנו ממליצים על כך רק למי שיש ניסיון עם קונטיינרים.

אחת הדרכים הטובות ביותר לשמור על מפתחות ה-API שלך מאובטחים ב-GitHub Codespaces היא שימוש ב-Codespace Secrets. עקוב אחרי [מדריך ניהול הסודות של Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) למידע נוסף.

## שיעורים ודרישות טכניות

הקורס כולל 6 שיעורי מושג ו-6 שיעורי קידוד.

בשיעורי הקידוד אנו משתמשים ב-Azure OpenAI Service. תצטרך גישה לשירות Azure OpenAI ומפתח API כדי להריץ את הקוד. אפשר להגיש בקשה לגישה על ידי [מילוי טופס זה](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

בזמן ההמתנה לאישור הבקשה, בכל שיעור קידוד יש גם קובץ `README.md` בו תוכל לצפות בקוד ובפלטים.

## שימוש ב-Azure OpenAI Service בפעם הראשונה

אם זו הפעם הראשונה שלך עם Azure OpenAI, עקוב אחרי המדריך ל-[יצירה ופריסה של משאב Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst).

## שימוש ב-OpenAI API בפעם הראשונה

אם זו הפעם הראשונה שלך עם OpenAI API, עקוב אחרי המדריך ל-[יצירה ושימוש בממשק](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst).

## להכיר לומדים נוספים

יצרנו ערוצים בשרת ה-Discord הרשמי של קהילת ה-AI שלנו [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) כדי להכיר לומדים נוספים. זו דרך נהדרת להכיר יזמים, בונים, סטודנטים וכל מי שרוצה להתקדם בבינה מלאכותית גנרטיבית.

[![הצטרף לערוץ הדיסקורד](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

צוות הפרויקט יהיה גם הוא בשרת הזה כדי לעזור ללומדים.

## תרומה

הקורס הזה הוא יוזמה בקוד פתוח. אם אתה רואה מקום לשיפור או בעיות, צור [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) או דווח על [בעיה ב-GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

צוות הפרויקט יעקוב אחרי כל התרומות. תרומה לקוד פתוח היא דרך נהדרת לבנות קריירה בבינה מלאכותית גנרטיבית.

רוב התרומות דורשות ממך להסכים ל-CLA (הסכם רישיון תורם) שמצהיר שיש לך את הזכות להעניק לנו את הזכויות להשתמש בתרומתך. לפרטים, בקר ב-[אתר CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

חשוב: כאשר אתה מתרגם טקסט בריפוזיטורי הזה, ודא שאינך משתמש בתרגום מכונה. נבדוק את התרגומים דרך הקהילה, אז אנא התנדב רק לשפות שאתה שולט בהן היטב.

כשאתה מגיש Pull Request, בוט ה-CLA יבדוק אוטומטית אם עליך לחתום על ההסכם ויוסיף תווית/תגובה בהתאם. פשוט עקוב אחרי ההוראות של הבוט. תצטרך לעשות זאת רק פעם אחת לכל הריפוזיטוריז שמשתמשים ב-CLA שלנו.

הפרויקט הזה מאמץ את [קוד ההתנהגות של קוד פתוח של מיקרוסופט](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). למידע נוסף קרא את ה-FAQ של קוד ההתנהגות או פנה ל-[Email opencode](opencode@microsoft.com) עם שאלות או הערות.

## בואו נתחיל
עכשיו כשסיימת את השלבים הנדרשים להשלמת הקורס, בוא נתחיל עם [היכרות עם בינה מלאכותית גנרטיבית ו-LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

Certainly! Here is your requested translation to Hebrew:

**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. יש לראות במסמך המקורי בשפתו המקורית כמקור הסמכותי. למידע קריטי, מומלץ לפנות לתרגום מקצועי על ידי אדם. איננו אחראים לכל אי-הבנות או פירושים שגויים הנובעים מהשימוש בתרגום זה.