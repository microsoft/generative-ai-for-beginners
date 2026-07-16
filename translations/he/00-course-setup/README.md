# התחלה עם הקורס הזה

אנו מאוד נרגשים שתתחיל את הקורס הזה ותראה מה תתעורר השראה לבנות עם AI גנרטיבי!

על מנת להבטיח את הצלחתך, דף זה מפרט את שלבי ההגדרה, דרישות טכניות, ואיפה לקבל עזרה במידת הצורך.

## שלבי הגדרה

כדי להתחיל לקחת את הקורס הזה, תצטרך להשלים את השלבים הבאים.

### 1. העתק את הריפו הזה

[העתק את הריפו כולו הזה](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) לחשבון ה-GitHub שלך כדי שתוכל לשנות כל קוד ולהשלים את האתגרים. בנוסף, תוכל גם [לתת כוכב (🌟) לריפו הזה](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) כדי למצוא אותו וריפואים קשורים בקלות יותר.

### 2. צור codespace

כדי להימנע מבעיות תלות בעת הרצת הקוד, אנו ממליצים להריץ את הקורס הזה ב-[GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

בגרסה שהעתקת: **Code -> Codespaces -> New on main**

![דיאלוג המציג כפתורים ליצירת קודספייס](../../../translated_images/he/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 הוסף סוד

1. ⚙️ סמל גלגל שיניים -> Command Pallete-> Codespaces : ניהול סוד משתמש -> הוסף סוד חדש.
2. שם OPENAI_API_KEY, הדבק את המפתח שלך, שמור.

### 3. מה הלאה?

| אני רוצה…          | עבור אל…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| להתחיל את שיעור 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| לעבוד אופליין       | [`setup-local.md`](02-setup-local.md)                                   |
| להגדיר ספק LLM      | [`providers.md`](03-providers.md)                                        |
| לפגוש לומדים אחרים  | [הצטרף לשרת דיסקורד שלנו](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## פתרון תקלות


| תסמין                                   | תיקון                                                            |
|-------------------------------------------|-----------------------------------------------------------------|
| בניית מיכל תקועה > 10 דק'               | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | הטרמינל לא התחבר; לחץ **+** ➜ *bash*                            |
| `401 Unauthorized` מ-OpenAI               | מפתח `OPENAI_API_KEY` שגוי / פג תוקף                             |
| VS Code מציג “Dev container mounting…”   | רענן את לשונית הדפדפן—Codespaces לפעמים מאבד חיבור               |
| Kernel של פנקס המחברות חסר              | תפריט פנקס ➜ **Kernel ▸ Select Kernel ▸ Python 3**               |

   מערכות מבוססות Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **ערוך את קובץ `.env`**: פתח את קובץ ה-`.env` בעורך טקסט (למשל VS Code, Notepad++ או כל עורך אחר). הוסף את השורות הבאות לקובץ, החלף את הממלאים במידע האמיתי שלך על נקודת הקצה והמקשים של Microsoft Foundry Models (ראה [`providers.md`](03-providers.md) כיצד לקבל אותם):

   > **הערה:** GitHub Models (ונעל המשתנה `GITHUB_TOKEN`) ייסגרו בסוף יולי 2026. השתמש במקום זאת ב-[Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **שמור את הקובץ**: שמור את השינויים וסגור את עורך הטקסט.

5. **התקן את `python-dotenv`**: אם לא התקנת עדיין, תצטרך להתקין את חבילת `python-dotenv` כדי לטעון משתני סביבה מקובץ ה-`.env` לתוך אפליקציית הפייתון שלך. תוכל להתקין אותו באמצעות `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **טען משתני סביבה בסקריפט פייתון שלך**: בסקריפט הפייתון שלך, השתמש בחבילת `python-dotenv` כדי לטעון את משתני הסביבה מקובץ ה-`.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # טען משתני סביבה מקובץ .env
   load_dotenv()

   # גש למשתני Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

זהו זה! יצרת בהצלחה קובץ `.env`, הוספת את האישורים שלך של Microsoft Foundry Models, וטעית אותם לאפליקציית הפייתון שלך.

## כיצד להריץ מקומית במחשב שלך

כדי להריץ את הקוד מקומית במחשב שלך, תצטרך שיהיה מותקן אצלך [Python במחשב](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

כדי להשתמש במאגר, עליך לשכפל אותו:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

ברגע שיש לך הכל מוכן, תוכל להתחיל!

## שלבים אופציונליים

### התקנת Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) הוא מתקין קל משקל להתקנת [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), פייתון, ומספר חבילות.
קונדה עצמה היא מנהל חבילות, שמקל על התקנה והחלפה בין [**סביבות וירטואליות**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) שונות של פייתון וחבילות. היא אף שימושית להתקנת חבילות שאינן זמינות דרך `pip`.

תוכל לעקוב אחר [מדריך התקנת MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) כדי להגדיר זאת.

אחרי התקנת Miniconda, עליך לשכפל את ה[מאגר](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (אם לא עשית זאת כבר)

לאחר מכן, עליך ליצור סביבה וירטואלית. לשם כך עם Conda, עבור ויצר קובץ סביבה חדש (_environment.yml_). אם אתה עובד עם Codespaces, צור את זה בתוך התיקייה `.devcontainer`, כלומר `.devcontainer/environment.yml`.

המשך ומלא את קובץ הסביבה שלך בקטע שלמטה:

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

אם אתה נתקל בטעויות בשימוש עם conda, תוכל להתקין ידנית את ספריות ה-Microsoft AI באמצעות הפקודה הבאה בטרמינל.

```
conda install -c microsoft azure-ai-ml
```

קובץ הסביבה מגדיר את התלויות הנדרשות. `<environment-name>` הוא השם שברצונך להשתמש בו לסביבת ה-Conda שלך, ו-`<python-version>` הוא הגרסה של פייתון שברצונך להשתמש בה, לדוגמה, `3` היא הגרסה העיקרית האחרונה של פייתון.

לאחר מכן, תוכל ליצור את סביבת ה-Conda שלך על ידי הרצת הפקודות הבאות במסוף/טרמינל שלך

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # הנתיב המשני של .devcontainer חל רק על הגדרות Codespace
conda activate ai4beg
```

עיין ב[מדריך סביבות Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) אם תפגוש בעיות.

### שימוש ב-Visual Studio Code עם תוסף התמיכה בפייתון

אנו ממליצים להשתמש בעורך [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) עם [תוסף התמיכה בפייתון](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) מותקן לקורס הזה. עם זאת, זו יותר המלצה ולא דרישה מוחלטת.

> **הערה**: בעת פתיחת מאגר הקורס ב-VS Code, יש לך אפשרות להגדיר את הפרויקט בתוך מיכל. זאת בזכות התיקייה [המיוחדת `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) הנמצאת בתוך מאגר הקורס. מידע נוסף על כך בהמשך.

> **הערה**: ברגע שתשכפל ותפתח את התיקייה ב-VS Code, המערכת תציע לך אוטומטית להתקין את תוסף התמיכה בפייתון.

> **הערה**: אם VS Code מציע לך לפתוח מחדש את המאגר בתוך מיכל, דחה את הבקשה הזו כדי להשתמש בגרסת הפייתון המותקנת מקומית.

### שימוש ב-Jupyter בדפדפן

תוכל גם לעבוד על הפרויקט באמצעות סביבת [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ישירות בדפדפן שלך. גם Jupyter הקלאסי וגם [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) מספקים סביבת פיתוח נעימה עם תכונות כמו השלמה אוטומטית, הדגשת קוד וכו'.

כדי להפעיל את Jupyter במחשב המקומי שלך, עבור לטרמינל/שורת פקודה, נווט לתיקיית הקורס, והריץ:

```bash
jupyter notebook
```

או

```bash
jupyterhub
```

זה יפעיל מופע Jupyter וכתובת ה-URL לגישה אליו תוצג בחלון שורת הפקודה.

עם גישה לכתובת URL, תראה את תקציר הקורס ותוכל לנווט לכל קובץ `*.ipynb`. לדוגמה, `08-building-search-applications/python/oai-solution.ipynb`.

### הרצה בתוך מיכל

אפשרות חלופית להגדרה על המחשב שלך או ב-Codespace היא שימוש ב-[מיכל](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). תיקיית `.devcontainer` המיוחדת בתוך מאגר הקורס מאפשרת ל-VS Code להגדיר את הפרויקט בתוך מיכל. מחוץ ל-Codespaces, זה ידרוש התקנת Docker, ובכלל זה כרוך במעט עבודה, לכן אנו ממליצים על כך רק למי שיש לו ניסיון בעבודה עם מכולות.

אחת הדרכים הטובות ביותר לשמור על מפתחות ה-API שלך בטוחים בשימוש עם GitHub Codespaces היא באמצעות סודות Codespace. אנא עקוב אחר המדריך לניהול [סודות Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) כדי ללמוד עוד על זה.


## שיעורים ודרישות טכניות

לקורס יש 6 שיעורי מושג ו-6 שיעורי קידוד.

לשיעורי הקידוד, אנו משתמשים בשירות Azure OpenAI. תצטרך גישה לשירות Azure OpenAI ומפתח API כדי להריץ את הקוד הזה. תוכל להגיש בקשה לקבלת גישה על ידי [השלמת טופס זה](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

בזמן שאתה ממתין לעיבוד הבקשה שלך, כל שיעור קידוד כולל גם קובץ `README.md` שבו תוכל לצפות בקוד ובפלטים.

## שימוש בשירות Azure OpenAI בפעם הראשונה

אם זו הפעם הראשונה שאתה עובד עם שירות Azure OpenAI, אנא עקוב אחר מדריך זה כיצד [ליצור ולפרוס משאב של Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## שימוש בממשק OpenAI API בפעם הראשונה

אם זו הפעם הראשונה שאתה עובד עם ממשק OpenAI API, אנא עקוב אחר המדריך כיצד [ליצור ולהשתמש בממשק.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## פגוש לומדים אחרים

יצרנו ערוצים בשרת הדיסקורד הרשמי שלנו [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) למפגש עם לומדים אחרים. זו דרך מצוינת להתחבר ליזמים, בונים, סטודנטים וכל מי שמחפש להתקדם בעולמות ה-AI הגנרטיבי.

[![הצטרף לערוץ דיסקורד](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

צוות הפרויקט יהיה גם הוא בשרת דיסקורד הזה כדי לסייע לכל לומד.

## תרומה

קורס זה הוא יוזמה בקוד פתוח. אם אתה רואה שיפורים או בעיות, אנא צור [בקשת משיכה](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) או דו"ח [Issue ב-GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

צוות הפרויקט יעקוב אחרי כל התרומות. תרומה לקוד פתוח היא דרך נהדרת לבנות את הקריירה שלך ב-AI גנרטיבי.

רוב התרומות דורשות הסכמה להסכם רישוי לתרומות (CLA) המצהיר שיש לך את הזכות והיכולת להעניק לנו את הזכויות להשתמש בתרומתך. לפרטים, בקר באתר [CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

חשוב: בעת תרגום טקסטים במאגר זה, יש לוודא שאינך משתמש בתרגום מכונה. נבדוק את התרגומים באמצעות הקהילה, לכן אנא התנדב לתרגום רק בשפות שבהן אתה שולט.

בעת הגשת בקשת משיכה, רובוט CLA יזהה אוטומטית אם יש צורך לספק CLA ויעטר את ה-PR בהתאם (כגון תווית, תגובה). פשוט פעל לפי ההוראות של הבוט. יש צורך לעשות זאת רק פעם אחת בכל מאגרי הקוד שמשתמשים ב-CLA שלנו.


פרויקט זה אימץ את [קוד ההתנהגות למקור פתוח של מיקרוסופט](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). למידע נוסף קראו את השאלות הנפוצות על קוד ההתנהגות או צרו קשר עם [Email opencode](opencode@microsoft.com) עבור כל שאלה או הערה נוספת.

## בואו נתחיל

כעת לאחר שסיימתם את השלבים הדרושים להשלמת הקורס הזה, בואו נתחיל ב-[הקדמה לבינה מלאכותית יוצרת ו-LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->