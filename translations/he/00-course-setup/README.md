# התחלה עם הקורס הזה

אנחנו מאוד נרגשים שאתה מתחיל את הקורס הזה וראה למה אתה תתלהב לבנות עם בינה מלאכותית ייצירתית!

כדי להבטיח את ההצלחה שלך, דף זה מפרט את שלבי ההתקנה, דרישות טכניות, ואיפה לקבל עזרה אם יש צורך.

## שלבי התקנה

כדי להתחיל ללמוד את הקורס הזה, תצטרך להשלים את השלבים הבאים.

### 1. יצירת Fork לריפו הזה

[צור Fork לכל הריפוזיטורי הזה](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) לחשבון ה-GitHub שלך כדי שתוכל לשנות כל קוד ולהשלים את האתגרים. אתה גם יכול [לסמן בכוכב (🌟) את הריפו הזה](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) כדי למצוא אותו ואת הריפוזיטוריים הקשורים בקלות.

### 2. צור Codespace

כדי להימנע מבעיות תלות בעת הרצת הקוד, אנו ממליצים להריץ את הקורס הזה ב-[GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

ב-Fork שלך: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/he/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 הוסף סוד

1. ⚙️ סמל הגלגל שיניים -> Command Pallete-> Codespaces : Manage user secret -> הוסף סוד חדש.
2. שם OPENAI_API_KEY, הדבק את המפתח שלך, שמור.

### 3. מה הלאה?

| אני רוצה…          | עבור אל…                                                                |
|---------------------|-------------------------------------------------------------------------|
| להתחיל שיעור 1     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| לעבוד אופליין       | [`setup-local.md`](02-setup-local.md)                                   |
| להגדיר ספק LLM      | [`providers.md`](03-providers.md)                                        |
| לפגוש לומדים אחרים | [הצטרף ל-Discord שלנו](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## פתרון בעיות


| תסמין                                   | תיקון                                                            |
|-------------------------------------------|-----------------------------------------------------------------|
| בניית הקונטיינר תקועה > 10 דקות           | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | הטרמינל לא התחבר; לחץ **+** ➜ *bash*                             |
| `401 Unauthorized` מ-OpenAI                 | `OPENAI_API_KEY` שגוי/פג תוקף                                   |
| VS Code מציג “Dev container mounting…”    | רענן את לשונית הדפדפן—לעיתים Codespaces מאבד חיבור              |
| Kernel של הדפדפן חסר                     | תפריט המחברת ➜ **Kernel ▸ Select Kernel ▸ Python 3**            |

   מערכות מבוססות Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **ערוך את קובץ `.env`**: פתח את קובץ `.env` בעורך טקסט (למשל VS Code, Notepad++, או כל עורך אחר). הוסף את השורות הבאות לקובץ, החלף את השמות במרחבים עם נקודת הסיום והמפתח האמיתיים שלך של Microsoft Foundry Models (ראה [`providers.md`](03-providers.md) כיצד להשיג זאת):

   > **הערה:** GitHub Models (והמשתנה `GITHUB_TOKEN`) יפורשו בסוף יולי 2026. השתמש במקום זאת ב-[Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **שמור את הקובץ**: שמור את השינויים וסגור את עורך הטקסט.

5. **התקן את `python-dotenv`**: אם טרם התקנת, תצטרך להתקין את חבילת `python-dotenv` כדי לטעון משתני סביבה מקובץ `.env` לתוך יישום הפייתון שלך. ניתן להתקין באמצעות `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **טען משתני סביבה בסקריפט פייתון שלך**: בסקריפט הפייתון שלך, השתמש ב-`python-dotenv` כדי לטעון משתני סביבה מקובץ `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # טעינת משתני סביבה מקובץ .env
   load_dotenv()

   # גישה למשתני Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

זהו זה! יצרת בהצלחה קובץ `.env`, הוספת את האישורים שלך ל-Microsoft Foundry Models, וטעינתם לתוך יישום הפייתון שלך.

## כיצד להריץ באופן מקומי במחשב שלך

כדי להריץ את הקוד באופן מקומי במחשב שלך, תצטרך שיהיה מותקן אצלך [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

כדי להשתמש במאגר, תצטרך לשכפל אותו:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

ברגע שיש לך את הכל מוכן, אתה יכול להתחיל!

## שלבים אופציונליים

### התקנת Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) הוא מתקין קל משקל עבור התקנת [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), פייתון, וכמה חבילות.
Conda עצמה היא מנהלת חבילות, המאפשרת התקנה והחלפה קלות בין [**סביבות וירטואליות**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) שונות של פייתון וחבילות. זה גם שימושי להתקנת חבילות שאינן זמינות דרך `pip`.

ניתן לעקוב אחרי [מדריך ההתקנה של MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) כדי להתקין אותו.

לאחר התקנת Miniconda, תצטרך לשכפל את ה[ריפו](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (אם לא עשית זאת כבר)

לאחר מכן, תצטרך ליצור סביבה וירטואלית. כדי לעשות זאת עם Conda, צור קובץ סביבה חדש (_environment.yml_). אם אתה עובד מסביבת Codespaces, צור את זה בתיקיית `.devcontainer`, כלומר `.devcontainer/environment.yml`.

המשך ומלא את קובץ הסביבה שלך בקטע למטה:

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

אם אתה נתקל בשגיאות בשימוש ב-conda, אתה יכול להתקין ידנית את ספריות הבינה המלאכותית של מיקרוסופט באמצעות הפקודה הבאה בטרמינל.

```
conda install -c microsoft azure-ai-ml
```

קובץ הסביבה מגדיר את התלויות שנדרשות. `<environment-name>` הוא השם שתבחר לסביבת ה-Conda שלך, ו-`<python-version>` היא גרסת הפייתון שבה תרצה להשתמש, למשל, `3` היא הגרסה העיקרית האחרונה של פייתון.

לאחר שסיימת, תוכל ליצור את סביבת ה-Conda שלך על ידי הרצת הפקודות הבאות בשורת הפקודה/טרמינל

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # הנתיב המשני .devcontainer חל רק על הגדרות Codespace
conda activate ai4beg
```

עיין ב-[מדריך סביבות Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) אם נתקלת בבעיות.

### שימוש ב-Visual Studio Code עם הרחבת Python

אנו ממליצים להשתמש בעורך [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) עם [הרחבת התמיכה ב-Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) מותקנת לקורס זה. עם זאת, זו המלצה ולא דרישה מחייבת.

> **הערה**: בעת פתיחת ריפוזיטורי הקורס ב-VS Code, יש לך אפשרות להגדיר את הפרויקט בתוך קונטיינר. זאת בזכות תיקיית ה-[`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) המיוחדת שנמצאת בריפוזיטורי הקורס. נדון בזה בהמשך.

> **הערה**: לאחר ששכפלת ופתחת את התיקייה ב-VS Code, הוא יציע אוטומטית להתקין את הרחבת התמיכה ב-Python.

> **הערה**: אם VS Code מציע לפתוח את הריפוזיטורי מחדש בקונטיינר, סרב לבקשה זו כדי להשתמש בגרסת ה-Python המותקנת למחשב.

### שימוש ב-Jupyter בדפדפן

ניתן גם לעבוד על הפרויקט באמצעות סביבה [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ישירות בדפדפן שלך. הן Jupyter הקלאסי והן [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) מספקים סביבת פיתוח נעימה עם תכונות כגון השלמה אוטומטית, הדגשת קוד וכו'.

כדי להפעיל Jupyter באופן מקומי, גש לטרמינל/שורת הפקודה, נווט לתיקיית הקורס, והרץ:

```bash
jupyter notebook
```

או

```bash
jupyterhub
```

הפקודה תפעיל מופע Jupyter וה-URL לגישה לו יוצג בחלון שורת הפקודה.

לאחר שתיגש ל-URL, תראה את מתאר הקורס ותוכל לגלוש לכל קובץ `*.ipynb`. לדוגמה, `08-building-search-applications/python/oai-solution.ipynb`.

### הרצה בתוך קונטיינר

אלטרנטיבה להגדרת הכול במחשב שלך או ב-Codespace היא להשתמש ב[קונטיינר](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). תיקיית ה-`.devcontainer` המיוחדת בריפוזיטורי הקורס מאפשרת ל-VS Code להגדיר את הפרויקט בתוך קונטיינר. מחוץ ל-Codespaces, יש צורך בהתקנת Docker, וכנות לומר, מדובר בעבודת הכנה מועטה, לכן אנו ממליצים על כך רק למי שיש לו ניסיון עם קונטיינרים.

אחת הדרכים הטובות ביותר לשמור על מפתחות ה-API שלך בטוחים בעת שימוש ב-GitHub Codespaces היא על ידי שימוש ב-Codespace Secrets. אנא עקוב אחרי מדריך [ניהול סודות ב-Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) ללמוד עוד על כך.


## שיעורים ודרישות טכניות

הקורס כולל שיעורי "לימוד" שמסבירים מושגים של בינה מלאכותית יצירתית ושיעורי "בנייה" עם דוגמאות קוד מעשיות ב-**Python** ו-**TypeScript** במידת האפשר.

לשיעורי הקוד, אנו משתמשים ב-Azure OpenAI ב-Microsoft Foundry. תצטרך מנוי Azure ומפתח API. הגישה פתוחה - אין צורך בבקשה - אז תוכל [ליצור משאב Microsoft Foundry ולפרוס מודל](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) כדי לקבל את נקודת הסיום והמפתח.

כל שיעור קוד כולל גם קובץ `README.md` שבו תוכל לראות את הקוד והתוצאות ללא צורך בהרצה.

## שימוש בשירות Azure OpenAI לראשונה

אם זו הפעם הראשונה שאתה עובד עם שירות Azure OpenAI, אנא עקוב אחר המדריך כיצד [ליצור ולפרוס משאב Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## שימוש ב-OpenAI API לראשונה

אם זו הפעם הראשונה שאתה עובד עם API של OpenAI, אנא עקוב אחר המדריך כיצד [ליצור ולהשתמש בממשק.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## פגוש לומדים אחרים

יצרנו ערוצים בשרת ה-Discord הרשמי שלנו של [קהילת AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) לפגוש לומדים אחרים. זו דרך מצוינת ליצור קשר עם יזמים, בוני פרויקטים, סטודנטים וכל אחד שמעוניין להתקדם בבינה מלאכותית יצירתית.

[![הצטרף לערוץ דיסקורד](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

צוות הפרויקט יוצג גם הוא בשרת דיסקורד זה כדי לעזור לכל הלומדים.

## תרומה

הקורס הוא יוזמה בקוד פתוח. אם אתה רואה נקודות לשיפור או בעיות, אנא צור [בקשת משיכה](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) או דווח על [בעיה ב-GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

צוות הפרויקט ינטר את כל התרומות. תרומה לקוד פתוח היא דרך נהדרת לבנות את הקריירה שלך בבינה מלאכותית יצירתית.

רוב התרומות דורשות הסכמה להסכם רישיון תורם (CLA) המצהיר שיש לך את הזכות והיכולת לתת לנו רישיון להשתמש בתרומתך. לפרטים, בקר באתר [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

חשוב: בעת תרגום טקסט בריפו זה, אנא וודא שאינך משתמש בתרגום מכונה. אנו נאמת את התרגומים באמצעות הקהילה, אז אנא התנדב לתרגום רק בשפות שבהן אתה שולט.


כאשר אתה מגיש בקשת משיכה, רובוט CLA יחליט אוטומטית האם עליך לספק CLA ויעניק את הקישוט המתאים לבקשה (למשל, תווית, הערה). פשוט עקוב אחר ההוראות שמספק הרובוט. תצטרך לעשות זאת רק פעם אחת בכל המחסנים שמשתמשים ב-CLA שלנו.

פרויקט זה אימץ את [קוד ההתנהגות בקוד פתוח של מיקרוסופט](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). למידע נוסף קרא את שאלות נפוצות על קוד ההתנהגות או פנה ל-[דואר אלקטרוני opencode](opencode@microsoft.com) עם שאלות או הערות נוספות.

## בואו נתחיל

כעת, לאחר שסיימת את השלבים הנדרשים לסיים קורס זה, בוא נתחיל עם [הקדמה לבינה יוצרת ו-LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->