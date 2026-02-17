# התחלה עם הקורס הזה

אנחנו מאוד נרגשים שאתם מתחילים את הקורס הזה ולראות למה תתלהבו לבנות עם בינה מלאכותית תורמת!

כדי להבטיח את הצלחתכם, דף זה מפרט את שלבי ההתקנה, הדרישות הטכניות, ואיפה ניתן לקבל עזרה במידת הצורך.

## שלבי ההתקנה

כדי להתחיל לקחת חלק בקורס הזה, תצטרכו להשלים את השלבים הבאים.

### 1. שכפול מאגר זה

[שכפלו את כל המאגר הזה](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) לחשבון הגיטהאב שלכם כדי שתוכלו לשנות כל קוד ולהשלים את האתגרים. תוכלו גם [לסמן בכוכב (🌟) את המאגר הזה](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) כדי למצוא אותו ואת המאגריים הקשורים בקלות רבה יותר.

### 2. יצירת סביבות קוד (codespace)

כדי להימנע מבעיות תלות בעת הרצת הקוד, אנו ממליצים להריץ את הקורס הזה ב-[GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

במאגר שלך: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/he/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 הוסף סוד

1. ⚙️ סמל גלגל שיניים -> Command Pallete -> Codespaces : ניהול סוד משתמש -> הוסף סוד חדש.
2. קרא לו OPENAI_API_KEY, הדבק את המפתח שלך, שמור.

### 3. מה הלאה?

| אני רוצה…          | עבור ל…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| להתחיל בשיעור 1     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| לעבוד במצב לא מקוון | [`setup-local.md`](02-setup-local.md)                                   |
| להגדיר ספק LLM      | [`providers.md`](03-providers.md)                                        |
| לפגוש לומדים אחרים | [הצטרפו ל-Discord שלנו](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## פתרון תקלות

| סימפטום                                 | תיקון                                                             |
|----------------------------------------|-----------------------------------------------------------------|
| בניית מכולה תקועה מעל 10 דקות          | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`             | הטרמינל לא התחבר; לחץ על **+** ➜ *bash*                         |
| `401 Unauthorized` מ-OpenAI             | מפתח `OPENAI_API_KEY` שגוי או שפג תוקפו                           |
| VS Code מציג “Dev container mounting…” | רענן את לשונית הדפדפן—לעיתים Codespaces מאבדים חיבור            |
| הליבה של פנקס הרישומים חסרה           | תפריט פנקס הרישומים ➜ **Kernel ▸ Select Kernel ▸ Python 3**       |

   מערכות מבוססות יוניקס:

   ```bash
   touch .env
   ```

   חלונות:

   ```cmd
   echo . > .env
   ```

3. **ערוך את הקובץ `.env`**: פתח את הקובץ `.env` בעורך טקסט (כגון VS Code, Notepad++, או כל עורך אחר). הוסף את השורה הבאה לקובץ, והחלף את `your_github_token_here` בטוקן הגיטהאב האמיתי שלך:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **שמור את הקובץ**: שמור את השינויים וסגור את עורך הטקסט.

5. **התקן את `python-dotenv`**: אם לא התקנת עדיין, עליך להתקין את חבילת `python-dotenv` כדי לטעון משתני סביבה מהקובץ `.env` לתוך אפליקציית הפייתון שלך. ניתן להתקין באמצעות `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **טען משתני סביבה בסקריפט הפייתון שלך**: בסקריפט הפייתון שלך, השתמש בחבילת `python-dotenv` כדי לטעון את משתני הסביבה מהקובץ `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # טען משתני סביבה מקובץ .env
   load_dotenv()

   # גש למשתנה GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

זהו! יצרת בהצלחה קובץ `.env`, הוספת את טוקן הגיטהאב שלך, וטעינת אותו לאפליקציית הפייתון שלך.

## איך להריץ מקומית במחשב שלך

כדי להריץ את הקוד מקומית במחשב שלך, תצטרך שיהיה מותקן אצלך [פייתון](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

לאחר מכן, לשימוש במאגר, עליך לשכפל אותו:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

לאחר שהכל מוכן, תוכל להתחיל!

## שלבים אופציונליים

### התקנת Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) הוא מתקין קל משקל להתקנת [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), פייתון, וכמה חבילות נוספות.  
Conda עצמה היא מנהל חבילות שמקל על ההגדרה והמעבר בין [סביבות וירטואליות](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) שונות של פייתון וחבילות. כמו כן, היא שימושית להתקנת חבילות שאינן זמינות דרך `pip`.

ניתן לעקוב אחרי [מדריך ההתקנה של MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) כדי להגדיר זאת.

עם התקנת Miniconda, תצטרך לשכפל את [המאגר](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (אם עדיין לא עשית זאת).

לאחר מכן, עליך ליצור סביבה וירטואלית. לעשות זאת עם Conda, צור קובץ סביבה חדש (_environment.yml_). אם אתה עובד עם Codespaces, צור אותו בתוך התיקייה `.devcontainer`, כלומר `.devcontainer/environment.yml`.

מלא את קובץ הסביבה שלך בקוד הבא:

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

אם אתה נתקל בשגיאות ב-conda תוכל להתקין ידנית את ספריות המיקרוסופט ל-AI באמצעות הפקודה הבאה בטרמינל.

```
conda install -c microsoft azure-ai-ml
```

קובץ הסביבה מגדיר את התלויות הדרושות. `<environment-name>` מתייחס לשם שתרצה לסביבה שלך ב-Conda, ו-`<python-version>` היא גרסת הפייתון שתרצה להשתמש בה, לדוגמה, `3` שהיא הגרסה הראשית האחרונה של פייתון.

לאחר מכן תוכל ליצור את סביבת Conda שלך על ידי הרצת הפקודות למטה בשורת הפקודה/טרמינל

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # נתיב משנה של .devcontainer חל רק על הגדרות Codespace
conda activate ai4beg
```

עיין ב[מדריך סביבות Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) אם תיתקל בבעיות.

### שימוש ב-Visual Studio Code עם תוסף תמיכה בפייתון

אנו ממליצים להשתמש בעורך [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) עם [תוסף התמיכה בפייתון](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) מותקן עבור הקורס הזה. זאת עם זאת, המלצה בלבד ולא דרישה מחייבת.

> **הערה**: על ידי פתיחת מאגר הקורס ב-VS Code, יש לך אפשרות להגדיר את הפרויקט בתוך מכולה. זה בזכות התיקייה המיוחדת [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) שנמצאת בתוך המאגר. נרחיב על כך בהמשך.

> **הערה**: לאחר ששכפלת ופתחת את התיקייה ב-VS Code, הוא יציע אוטומטית להתקין תוסף תמיכה בפייתון.

> **הערה**: אם VS Code מציע לך לפתוח מחדש את המאגר בתוך מכולה, דחה את הבקשה כדי להשתמש בגרסת הפייתון המותקנת מקומית.

### שימוש ב-Jupyter בדפדפן

ניתן גם לעבוד על הפרויקט באמצעות סביבת [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) בדפדפן. גם Jupyter הקלאסי וגם [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) מספקים סביבת פיתוח מהנה עם תכונות כמו השלמת קוד אוטומטית, הדגשת סינטקס, ועוד.

כדי להתחיל Jupyter מקומית, עבור אל הטרמינל / שורת הפקודה, נווט לתיקיית הקורס, והריץ:

```bash
jupyter notebook
```

או

```bash
jupyterhub
```

זה יפעיל מופע Jupyter ויציג את כתובת ה-URL לגישה אליו בחלון שורת הפקודה.

כאשר תיגש ל-URL, תראה את מבנה הקורס ותוכל לנווט לכל קובץ `*.ipynb`, לדוגמה, `08-building-search-applications/python/oai-solution.ipynb`.

### הרצה בתוך מכולה

חלופה להגדיר הכל במחשב שלך או ב-Codespace היא שימוש ב-[מכולה](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). תיקיית `.devcontainer` המיוחדת במאגר הקורס מאפשרת ל-VS Code להגדיר את הפרויקט בתוך מכולה. מחוץ ל-Codespaces, הדבר דורש התקנת Docker, ויכלול קצת עבודה, לכן אנו ממליצים זאת רק למשתמשים עם ניסיון בעבודה עם מכולות.

אחת הדרכים הטובות ביותר לשמור על מפתחות ה-API שלך בטוחים בשימוש ב-GitHub Codespaces היא על ידי שימוש ב-Codespace Secrets. אנא עקוב אחרי [מדריך ניהול סודות ב-Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) כדי ללמוד עוד על כך.

## שיעורים ודרישות טכניות

לקורס יש 6 שיעורים רעיוניים ו-6 שיעורי קידוד.

לשיעורי הקידוד אנו משתמשים בשירות Azure OpenAI. תצטרך גישה לשירות Azure OpenAI ומפתח API כדי להריץ את הקוד הזה. ניתן להגיש בקשה לקבלת גישה על ידי [השלמת טופס זה](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

בזמן שאתה ממתין לעיבוד הבקשה שלך, כל שיעור קידוד כולל גם קובץ `README.md` שבו תוכל לצפות בקוד ובפלטים.

## שימוש ראשון בשירות Azure OpenAI

אם זוהי הפעם הראשונה שלך בעבודה עם שירות Azure OpenAI, אנא עקוב אחר המדריך כיצד [ליצור ולפרוס משאב שירות Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## שימוש ראשון ב-OpenAI API

אם זוהי הפעם הראשונה שלך בעבודה עם OpenAI API, אנא עקוב אחרי המדריך איך [ליצור ולהשתמש בממשק.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## פגש לומדים אחרים

יצרנו ערוצים בשרת Discord הרשמי של [קהילת הבינה המלאכותית שלנו](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) לפגישה עם לומדים אחרים. זו דרך מצוינת ליצור קשר עם יזמים, בונים, סטודנטים וכל מי שמעוניין לשפר את היכולות שלו ב-Generative AI.

[![הצטרף לערוץ דסקורד](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

צוות הפרויקט גם יהיה בשרת Discord זה כדי לסייע לכל לומד.

## תרומה

הקורס הזה הוא יוזמה קוד פתוח. אם אתה רואה מקומות לשיפור או בעיות, אנא צור [בקשת מיזוג (Pull Request)](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) או דווח על [בעיית GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

צוות הפרויקט יעקוב אחר כל התרומות. תרומה לקוד פתוח היא דרך מעולה לבנות את הקריירה שלך ב-Generative AI.

רוב התרומות דורשות הסכמתך ל[רישיון תורם (CLA)](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) המצהיר שיש לך את הזכות ומעניק לנו את הזכויות להשתמש בתרומתך. לפרטים, בקר באתר רישיון התורם.

חשוב: בעת תרגום טקסט במאגר זה, ודא שאינך משתמש בתרגום מכונה. אנו נאמת את התרגומים דרך הקהילה, לכן אנא התנדב לתרגם רק בשפות שאתה שולט בהן.

כאשר תגיש בקשת משיכה, בוט CLA יבדוק באופן אוטומטי אם יש צורך לספק CLA ויקשט את ה-PR בהתאם (כגון תווית, תגובה). פשוט עקוב אחרי ההוראות של הבוט. תצטרך לעשות זאת רק פעם אחת בכל המאגריים המשתמשים ב-CLA שלנו.

פרויקט זה אימץ את [קוד ההתנהגות של מיקרוסופט בקוד פתוח](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). למידע נוסף קרא את שאלות נפוצות על קוד ההתנהגות או פנה ל-[דוא"ל opencode](opencode@microsoft.com) עם שאלות או הערות נוספות.

## בואו נתחיל
עכשיו כשסיימתם את השלבים הדרושים להשלמת הקורס הזה, בואו נתחיל עם [הקדמה ל-AI יצירתי ו-LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ תרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->