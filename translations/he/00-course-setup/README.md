<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-17T20:03:17+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "he"
}
-->
# התחלת הקורס

אנחנו מאוד נרגשים שתתחילו את הקורס הזה ונראה מה תצליחו ליצור בהשראת Generative AI!

כדי להבטיח את הצלחתכם, עמוד זה מפרט את שלבי ההגדרה, הדרישות הטכניות, ואיפה ניתן לקבל עזרה במידת הצורך.

## שלבי הגדרה

כדי להתחיל את הקורס, תצטרכו להשלים את השלבים הבאים.

### 1. יצירת Fork למאגר הזה

[צרו Fork למאגר כולו](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) לחשבון GitHub שלכם כדי שתוכלו לשנות קוד ולהשלים את האתגרים. תוכלו גם [לסמן בכוכב (🌟) את המאגר הזה](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) כדי למצוא אותו ואת מאגרים קשורים בקלות רבה יותר.

### 2. יצירת Codespace

כדי להימנע מבעיות תלות בעת הרצת הקוד, אנו ממליצים להריץ את הקורס הזה ב-[GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

ב-Fork שלכם: **Code -> Codespaces -> New on main**

![דיאלוג שמראה כפתורים ליצירת Codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 הוספת Secret

1. ⚙️ אייקון גלגל שיניים -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.  
2. שם OPENAI_API_KEY, הדביקו את המפתח שלכם, שמרו.

### 3. מה הלאה?

| אני רוצה...         | לעבור ל...                                                              |
|---------------------|-------------------------------------------------------------------------|
| להתחיל שיעור 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| לעבוד במצב לא מקוון | [`setup-local.md`](02-setup-local.md)                                   |
| להגדיר ספק LLM      | [`providers.md`](03-providers.md)                                        |
| להכיר לומדים אחרים  | [הצטרפו ל-Discord שלנו](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## פתרון בעיות

| סימפטום                                   | פתרון                                                           |
|-------------------------------------------|-----------------------------------------------------------------|
| בניית הקונטיינר נתקעת > 10 דקות           | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | הטרמינל לא התחבר; לחצו **+** ➜ *bash*                          |
| `401 Unauthorized` מ-OpenAI               | מפתח `OPENAI_API_KEY` שגוי או פג תוקף                          |
| VS Code מציג “Dev container mounting…”    | רעננו את לשונית הדפדפן—Codespaces לפעמים מאבד חיבור             |
| חסר Kernel במחברת                        | תפריט מחברת ➜ **Kernel ▸ Select Kernel ▸ Python 3**            |

   מערכות מבוססות Unix:

   ```bash
   touch .env
   ```
  
   Windows:

   ```cmd
   echo . > .env
   ```
  
3. **ערכו את קובץ `.env`**: פתחו את קובץ `.env` בעורך טקסט (למשל, VS Code, Notepad++ או כל עורך אחר). הוסיפו את השורה הבאה לקובץ, והחליפו את `your_github_token_here` עם הטוקן האמיתי שלכם:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```
  
4. **שמרו את הקובץ**: שמרו את השינויים וסגרו את עורך הטקסט.

5. **התקינו `python-dotenv`**: אם עדיין לא עשיתם זאת, תצטרכו להתקין את חבילת `python-dotenv` כדי לטעון משתני סביבה מקובץ `.env` לתוך אפליקציית Python שלכם. ניתן להתקין זאת באמצעות `pip`:

   ```bash
   pip install python-dotenv
   ```
  
6. **טענו משתני סביבה בסקריפט Python שלכם**: בסקריפט Python שלכם, השתמשו בחבילת `python-dotenv` כדי לטעון את משתני הסביבה מקובץ `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```
  
זהו! יצרתם בהצלחה קובץ `.env`, הוספתם את הטוקן של GitHub, וטענתם אותו לאפליקציית Python שלכם.

## איך להריץ מקומית על המחשב שלכם

כדי להריץ את הקוד מקומית על המחשב שלכם, תצטרכו להתקין גרסה כלשהי של [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

לאחר מכן, כדי להשתמש במאגר, תצטרכו לשכפל אותו:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```
  
לאחר ששכפלתם את הכל, תוכלו להתחיל!

## שלבים אופציונליים

### התקנת Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) הוא מתקין קל משקל להתקנת [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, וכמה חבילות נוספות.  
Conda עצמו הוא מנהל חבילות שמקל על הגדרה והחלפה בין [**סביבות וירטואליות**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) שונות של Python וחבילות. הוא גם שימושי להתקנת חבילות שאינן זמינות דרך `pip`.

תוכלו לעקוב אחרי [מדריך ההתקנה של Miniconda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) כדי להגדיר אותו.

לאחר התקנת Miniconda, תצטרכו לשכפל את [המאגר](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (אם עדיין לא עשיתם זאת).

לאחר מכן, תצטרכו ליצור סביבה וירטואלית. כדי לעשות זאת עם Conda, צרו קובץ סביבה חדש (_environment.yml_). אם אתם עובדים עם Codespaces, צרו את הקובץ הזה בתוך תיקיית `.devcontainer`, כלומר `.devcontainer/environment.yml`.

מלאו את קובץ הסביבה עם הקטע הבא:

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
  
אם אתם נתקלים בבעיות עם Conda, תוכלו להתקין ידנית את ספריות Microsoft AI באמצעות הפקודה הבאה בטרמינל.

```
conda install -c microsoft azure-ai-ml
```
  
קובץ הסביבה מציין את התלויות שאנחנו צריכים. `<environment-name>` מתייחס לשם שתרצו להשתמש בו עבור סביבת Conda שלכם, ו-`<python-version>` הוא גרסת Python שתרצו להשתמש בה, לדוגמה, `3` היא הגרסה העדכנית ביותר של Python.

לאחר מכן, תוכלו ליצור את סביבת Conda שלכם על ידי הרצת הפקודות הבאות בשורת הפקודה/טרמינל שלכם:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```
  
עיינו במדריך [סביבות Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) אם אתם נתקלים בבעיות.

### שימוש ב-Visual Studio Code עם תוסף תמיכה ב-Python

אנו ממליצים להשתמש בעורך [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) עם [תוסף תמיכה ב-Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) המותקן עבור הקורס הזה. עם זאת, זו המלצה בלבד ולא דרישה מוחלטת.

> **הערה**: על ידי פתיחת מאגר הקורס ב-VS Code, יש לכם אפשרות להגדיר את הפרויקט בתוך קונטיינר. זאת בזכות תיקיית [`.devcontainer` המיוחדת](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) שנמצאת בתוך מאגר הקורס. מידע נוסף על כך בהמשך.

> **הערה**: לאחר שתשכפלו ותפתחו את התיקייה ב-VS Code, הוא יציע לכם להתקין תוסף תמיכה ב-Python.

> **הערה**: אם VS Code מציע לכם לפתוח את המאגר בתוך קונטיינר, דחו את הבקשה כדי להשתמש בגרסה המקומית של Python.

### שימוש ב-Jupyter בדפדפן

תוכלו גם לעבוד על הפרויקט באמצעות סביבת [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ישירות בדפדפן שלכם. גם Jupyter הקלאסי וגם [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) מספקים סביבת פיתוח נעימה עם תכונות כמו השלמה אוטומטית, הדגשת קוד ועוד.

כדי להתחיל את Jupyter מקומית, גשו לטרמינל/שורת הפקודה, נווטו לתיקיית הקורס, והריצו:

```bash
jupyter notebook
```
  
או

```bash
jupyterhub
```
  
זה יפעיל מופע של Jupyter וה-URL לגישה אליו יוצג בחלון שורת הפקודה.

לאחר שתיגשו ל-URL, תוכלו לראות את מתווה הקורס ולנווט לכל קובץ `*.ipynb`. לדוגמה, `08-building-search-applications/python/oai-solution.ipynb`.

### הרצה בתוך קונטיינר

אלטרנטיבה להגדרת הכל על המחשב שלכם או ב-Codespace היא שימוש ב-[קונטיינר](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). תיקיית `.devcontainer` המיוחדת בתוך מאגר הקורס מאפשרת ל-VS Code להגדיר את הפרויקט בתוך קונטיינר. מחוץ ל-Codespaces, זה ידרוש התקנת Docker, ובכנות, זה כרוך במעט עבודה, ולכן אנו ממליצים על כך רק למי שיש לו ניסיון בעבודה עם קונטיינרים.

אחת הדרכים הטובות ביותר לשמור על מפתחות ה-API שלכם מאובטחים בעת שימוש ב-GitHub Codespaces היא באמצעות שימוש ב-Codespace Secrets. אנא עקבו אחרי [מדריך ניהול Secrets ב-Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) כדי ללמוד עוד על כך.

## שיעורים ודרישות טכניות

הקורס כולל 6 שיעורי מושגים ו-6 שיעורי קוד.

עבור שיעורי הקוד, אנו משתמשים ב-Azure OpenAI Service. תצטרכו גישה לשירות Azure OpenAI ומפתח API כדי להריץ את הקוד הזה. תוכלו להגיש בקשה לקבלת גישה על ידי [מילוי הבקשה הזו](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

בזמן שאתם מחכים לעיבוד הבקשה שלכם, כל שיעור קוד כולל גם קובץ `README.md` שבו תוכלו לצפות בקוד ובתוצאות.

## שימוש ב-Azure OpenAI Service בפעם הראשונה

אם זו הפעם הראשונה שלכם בעבודה עם שירות Azure OpenAI, אנא עקבו אחרי המדריך כיצד [ליצור ולפרוס משאב של Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## שימוש ב-OpenAI API בפעם הראשונה

אם זו הפעם הראשונה שלכם בעבודה עם OpenAI API, אנא עקבו אחרי המדריך כיצד [ליצור ולהשתמש בממשק.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## הכירו לומדים אחרים

יצרנו ערוצים בשרת [Discord הקהילתי הרשמי של AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) כדי להכיר לומדים אחרים. זו דרך נהדרת ליצור קשרים עם יזמים, בונים, סטודנטים, וכל מי שמעוניין להתקדם בתחום ה-Generative AI.

[![הצטרפו לערוץ הדיסקורד](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

צוות הפרויקט יהיה גם בשרת Discord הזה כדי לעזור לכל הלומדים.

## תרומה

הקורס הזה הוא יוזמה בקוד פתוח. אם אתם רואים אזורים לשיפור או בעיות, אנא צרו [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) או רשמו [בעיה ב-GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

צוות הפרויקט יעקוב אחרי כל התרומות. תרומה לקוד פתוח היא דרך מדהימה לבנות את הקריירה שלכם ב-Generative AI.

רוב התרומות דורשות מכם להסכים להסכם רישיון תורם (CLA) שמצהיר שיש לכם את הזכות ובאמת מעניקים לנו את הזכויות להשתמש בתרומתכם. לפרטים נוספים, בקרו באתר [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

חשוב: כאשר אתם מתרגמים טקסט במאגר הזה, אנא ודאו שאינכם משתמשים בתרגום מכונה. אנו נוודא את התרגומים דרך הקהילה, אז אנא התנדבו לתרגם רק בשפות שבהן אתם שולטים.

כאשר תגישו Pull Request, CLA-bot יבדוק באופן אוטומטי אם אתם צריכים לספק CLA ויעדכן את ה-PR בהתאם (למשל, תווית, תגובה). פשוט עקבו אחרי ההוראות שהבוט יספק. תצטרכו לעשות זאת רק פעם אחת בכל המאגרים שמשתמשים ב-CLA שלנו.

הפרויקט הזה אימץ את [קוד ההתנהגות של קוד פתוח של מיקרוסופט](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). למידע נוסף קראו את השאלות הנפוצות על קוד ההתנהגות או צרו קשר עם [Email opencode](opencode@microsoft.com) לכל שאלה או הערה נוספת.

## בואו נתחיל!
עכשיו, לאחר שסיימת את השלבים הנדרשים להשלמת הקורס, בוא נתחיל עם [מבוא ל-AI גנרטיבי ו-LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. איננו אחראים לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.