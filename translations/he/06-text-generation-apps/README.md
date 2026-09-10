# בניית אפליקציות ליצירת טקסט

[![בניית אפליקציות ליצירת טקסט](../../../translated_images/he/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(לחץ על התמונה מעלה כדי לצפות בסרטון של השיעור)_

עד כה ראית במסגרת תוכנית לימודים זו שיש מושגים מרכזיים כמו prompts ואפילו תחום שלם שנקרא "הנדסת פרומפטים". כלים רבים בהם אתה יכול להשתמש כמו ChatGPT, Office 365, Microsoft Power Platform ועוד, תומכים בשימוש בפרומפטים כדי להשיג מטרה מסוימת.

כדי להוסיף חוויה כזו לאפליקציה, עליך להבין מושגים כמו prompts, completions ולבחור ספרייה לעבודה איתה. זה בדיוק מה שלמדת בפרק זה.

## מבוא

בפרק זה, תלמד:

- ללמוד על ספריית openai והמושגים המרכזיים שלה.
- לבנות אפליקציית יצירת טקסט באמצעות openai.
- להבין איך להשתמש במושגים כמו prompt, טמפרטורה, וטוקנים כדי לבנות אפליקציית יצירת טקסט.

## מטרות הלמידה

בסיום שיעור זה, תהיה מסוגל:

- להסביר מהי אפליקציית יצירת טקסט.
- לבנות אפליקציית יצירת טקסט באמצעות openai.
- להגדיר את האפליקציה שלך כך שתשתמש ביותר או פחות טוקנים וכן לשנות את הטמפרטורה, לקבלת פלט מגוון.

## מהי אפליקציית יצירת טקסט?

בדרך כלל כשאתה בונה אפליקציה יש לה איזושהי ממשק כמו הבא:

- מבוססת פקודות. אפליקציות קונסולה הן אפליקציות טיפוסיות שבהן אתה מקליד פקודה והיא מבצעת משימה. לדוגמה, `git` היא אפליקציה מבוססת פקודות.
- ממשק משתמש (UI). יש אפליקציות עם ממשקי משתמש גרפיים (GUI) שבהם אתה לוחץ על כפתורים, מזין טקסט, בוחר אפשרויות ועוד.

### אפליקציות קונסולה וממשק UI מוגבלות

השווה את זה לאפליקציה מבוססת פקודות שבה אתה מקליד פקודה:

- **הן מוגבלות**. אתה לא יכול להקליד סתם כל פקודה, אלא רק את אלה שהאפליקציה תומכת בהן.
- **שפות ספציפיות**. יש אפליקציות שתומכות בהרבה שפות, אבל כברירת מחדל האפליקציה בנויה לשפה ספציפית, גם אם אפשר להוסיף תמיכה בשפות נוספות.

### יתרונות של אפליקציות יצירת טקסט

אז במה אפליקציית יצירת טקסט שונה?

באפליקציית יצירת טקסט יש לך יותר גמישות, אינך מוגבל למערכת פקודות או לשפת קלט ספציפית. במקום זאת, אתה עשוי להשתמש בשפה טבעית כדי לתקשר עם האפליקציה. יתרון נוסף הוא שאתה כבר מתקשר עם מקור נתונים שהוכשר על מאגר מידע עצום, בעוד שאפליקציה מסורתית יכולה להיות מוגבלת למה שיש במסד הנתונים.

### מה אפשר לבנות עם אפליקציית יצירת טקסט?

יש הרבה דברים שאפשר לבנות. לדוגמה:

- **צ'אטבוט**. צ'אטבוט שעונה על שאלות בנושא כמו החברה שלך והמוצרים שלה יכול להיות פתרון טוב.
- **עוזר**. LLMs מצוינים לעבודה כמו סיכום טקסט, קבלת תובנות מתוך טקסט, הפקת טקסט כמו קורות חיים ועוד.
- **עוזר קוד**. בהתאם למודל השפה שתשתמש בו, תוכל לבנות עוזר קוד שיעזור לך לכתוב קוד. לדוגמה, אתה יכול להשתמש במוצר כמו GitHub Copilot וגם ב-ChatGPT כדי לסייע בכתיבת קוד.

## איך אפשר להתחיל?

ובכן, עליך למצוא דרך לשלב עם LLM שלרוב כוללת את שתי הגישות הבאות:

- שימוש ב-API. כאן אתה בונה בקשות רשת עם הפרומפט שלך ומקבל טקסט שנוצר בחזרה.
- שימוש בספרייה. ספריות מסייעות לארוז את קריאות ה-API ולהקל על השימוש.

## ספריות/SDKs

יש כמה ספריות מוכרות לעבודה עם LLMs כגון:

- **openai**, ספרייה זו מקלה על חיבור למודל שלך ושליחת פרומפטים.

לאחר מכן יש ספריות שפועלות ברמה גבוהה יותר כמו:

- **Langchain**. Langchain מוכרת ותומכת בפייתון.
- **Semantic Kernel**. Semantic Kernel היא ספרייה מבית מיקרוסופט התומכת בשפות C#, Python ו-Java.

## האפליקציה הראשונה בשימוש openai

בוא נסתכל איך לבנות את האפליקציה הראשונה שלנו, איזו ספרייה אנחנו צריכים, כמה נדרש ועוד.

### התקנת openai

ישנן ספריות רבות לעבודה עם OpenAI או Azure OpenAI. ניתן להשתמש בשפות תכנות רבות כמו C#, Python, JavaScript, Java ועוד. החלטנו להשתמש בספריית `openai` בפייתון, לכן נשתמש ב-`pip` כדי להתקין אותה.

```bash
pip install openai
```

### יצירת משאב

עליך לבצע את השלבים הבאים:

- צור חשבון ב-Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- השג גישה ל-Azure OpenAI. עבור אל [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) ובקש גישה.

  > [!NOTE]
  > בזמן כתיבה זו, יש להגיש בקשה לקבלת גישה ל-Azure OpenAI.

- התקן את Python <https://www.python.org/>
- צור משאב שירות Azure OpenAI. ראה מדריך זה כיצד [ליצור משאב](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### איתור מפתח API ו-endpoint

בשלב זה, עליך לספר לספריית `openai` איזה מפתח API להשתמש. כדי למצוא את מפתח ה-API שלך, עבור למדור "Keys and Endpoint" במשאב Azure OpenAI שלך והעתק את הערך "Key 1".

![משאב Keys and Endpoint ב- Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

עכשיו כשיש לך את המידע הזה מועתק, בוא ננחה את הספריות להשתמש בו.

> [!NOTE]
> כדאי להפריד את מפתח ה-API שלך מהקוד. ניתן לעשות זאת באמצעות משתני סביבה.
>
> - הגדר את משתנה הסביבה `OPENAI_API_KEY` למפתח ה-API שלך.
>   `export OPENAI_API_KEY='sk-...'`

### הגדרת תצורה ל-Azure

אם אתה משתמש ב-Azure OpenAI (כעת חלק מ-Microsoft Foundry), כך תגדיר את התצורה. אנו משתמשים בלקוח הסטנדרטי `OpenAI` שפונה ל-endpoint של Azure OpenAI `/openai/v1/`, שעובד עם Responses API ואינו דורש `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

למעלה אנו מגדירים את הדברים הבאים:

- `api_key`, זהו מפתח ה-API שלך שנמצא בפורטל Azure או בפורטל Microsoft Foundry.
- `base_url`, זהו ה-endpoint של משאב Foundry שלך עם `/openai/v1/` בקצה. ה-endpoint היציב v1 פועל גם ב-OpenAI וגם ב-Azure OpenAI ללא ניהול `api_version`.

> [!NOTE] > `os.environ` קורא משתני סביבה. תוכל להשתמש בו כדי לקרוא משתנים כמו `AZURE_OPENAI_API_KEY` ו-`AZURE_OPENAI_ENDPOINT`. הגדר משתני סביבה אלה בטרמינל שלך או באמצעות ספרייה כמו `dotenv`.

## יצירת טקסט

הדרך ליצור טקסט היא באמצעות Responses API דרך השיטה `responses.create`. הנה דוגמה:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # זהו שם הפריסה של הדגם שלך
    input=prompt,
    store=False,
)
print(response.output_text)
```

בקוד למעלה, אנו יוצרים תגובה ומעבירים את המודל שבו נרצה להשתמש ואת הפרומפט. אז אנו מדפיסים את הטקסט שנוצר דרך `response.output_text`.

### שיחות מולטי-טורניות

ה-Responses API מתאים הן ליצירת טקסט בסיבוב יחיד והן לצ'אטבוטים מרובי סבבים - אתה מספק רשימת הודעות ב-`input` לבניית שיחה:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

מידע נוסף על פונקציונליות זו בפרק עתידי.

## תרגיל - האפליקציה הראשונה ליצירת טקסט

עכשיו שלמדנו איך להגדיר ולכוונן את openai, הגיע הזמן לבנות את אפליקציית יצירת הטקסט הראשונה שלך. כדי לבנות את האפליקציה, בצע את השלבים הבאים:

1. צור סביבה וירטואלית והתקן את openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > אם אתה משתמש ב-Windows הקלד `venv\Scripts\activate` במקום `source venv/bin/activate`.

   > [!NOTE]
   > אתר את מפתח Azure OpenAI על ידי כניסה ל-[https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) וחפש `Open AI` ובחר ב-`Open AI resource` ואז ב-`Keys and Endpoint` והעתק את הערך `Key 1`.

1. צור קובץ _app.py_ וכתוב בו את הקוד הבא:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # הוסף את קוד ההשלמה שלך
   prompt = "Complete the following: Once upon a time there was a"

   # בצע בקשה באמצעות ממשק ה-API של התגובות
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # הדפס תגובה
   print(response.output_text)
   ```

   > [!NOTE]
   > אם אתה משתמש ב-OpenAI רגיל (לא Azure), השתמש ב-`client = OpenAI(api_key="<replace this value with your OpenAI key>")` (ללא `base_url`) ועבור שם המודל כמו `gpt-5-mini` במקום שם פריסה.

   תראה פלט כמו הבא:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## סוגים שונים של פרומפטים, לדברים שונים

עכשיו ראית איך ליצור טקסט באמצעות פרומפט. יש לך אפילו תוכנית רצה שאתה יכול לשנות ולשפר כדי ליצור סוגים שונים של טקסט.

פרומפטים יכולים לשמש למשימות מכל סוג. לדוגמה:

- **יצירת סוג טקסט**. לדוגמה, ניתן ליצור שיר, שאלות לחידון ועוד.
- **חיפוש מידע**. ניתן להשתמש בפרומפטים כדי להשיג מידע כמו בדוגמה הבאה 'מה המשמעות של CORS בפיתוח ווב?'.
- **יצירת קוד**. ניתן להשתמש בפרומפטים ליצירת קוד, לדוגמה פיתוח ביטוי רגולרי לאימות דואר אלקטרוני, או אפילו ליצירת תוכנית שלמה, כמו אפליקציית ווב.

## מקרה שימוש מעשי יותר: יוצר מתכונים

דמיין שיש לך בבית רכיבים ואתה רוצה לבשל משהו. לשם כך אתה צריך מתכון. דרך למצוא מתכונים היא שימוש במנוע חיפוש או שאתה יכול להשתמש ב-LLM כדי לעשות זאת.

תוכל לכתוב פרומפט כזה:

> "הראה לי 5 מתכונים למנה עם הרכיבים הבאים: עוף, תפוחי אדמה וגזר. עבור כל מתכון, פרט את כל הרכיבים המשמשים בו"

בהתחשב בפרומפט שלמעלה, ייתכן שתקבל תגובה דומה ל:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 2 cloves garlic, minced
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
```

התוצאה הזו מצוינת, אני יודע מה לבשל. בשלב זה, מה שיכול להיות שיפור מועיל הוא:

- סינון רכיבים שאני לא אוהב או אלרגי להם.
- הפקת רשימת קניות, למקרה שאין לי את כל הרכיבים בבית.

למקרים אלה, נוסיף פרומפט נוסף:

> "אנא הסר מתכונים עם שום כי אני אלרגי, והחליף למשהו אחר. בנוסף, הפק רשימת קניות למתכונים, בהתחשב שיש לי כבר בבית עוף, תפוחי אדמה וגזר."

עכשיו יש לך תוצאה חדשה, כדלקמן:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano

Shopping List:
- Olive oil
- Onion
- Thyme
- Oregano
- Salt
- Pepper
```

אלה חמשת המתכונים שלך, ללא שום כפי שביקשת וגם יש לך רשימת קניות בהתחשב במה שיש לך בבית.

## תרגיל - בנה יוצר מתכונים

עכשיו כששיחקנו בסצנריו, נכתוב קוד שיתאים לסצנריו שהודגם. לצורך כך, בצע את השלבים הבאים:

1. השתמש בקובץ הקיים _app.py_ כנקודת התחלה
1. אתר את המשתנה `prompt` ושנה את הקוד שלו כך:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   כשתפעיל את הקוד עכשיו, תראה פלט דומה ל:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > שים לב, ה-LLM שלך לא דטרמיניסטי, לכן יתכנו תוצאות שונות בכל ריצה.

   מצוין, נבחן כיצד ניתן לשפר את הדברים. לשיפור, נרצה לוודא שהקוד גמיש כך שניתן לשנות את הרכיבים ומספר המתכונים.

1. נבצע שינוי בקוד באופן הבא:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # לאינטרפולציה את מספר המתכונים לתוך ההנחיה והמרכיבים
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   לקוד להרצת בדיקה, זה עלול להראות כך:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### שפר באמצעות הוספת סינון ורשימת קניות

כעת יש לנו אפליקציה שעובדת ומסוגלת להפיק מתכונים והיא גמישה כי היא מתבססת על קלטים מהמשתמש, גם מבחינת כמות המתכונים וגם מבחינת הרכיבים.

כדי לשפר אותה עוד יותר, נרצה להוסיף את הדברים הבאים:

- **סינון רכיבים**. נרצה להיות מסוגלים לסנן רכיבים שאנחנו לא אוהבים או אלרגיים להם. לשינוי זה, אפשר לערוך את הפרומפט הקיים ולהוסיף תנאי סינון לסופו כך:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  למעלה, הוספנו `{filter}` לסוף הפרומפט ואנחנו גם לוכדים את ערך הסינון מהמשתמש.

  דוגמה לקלט בהרצת התוכנית יכולה להראות כך:

  ```output
  No of recipes (for example, 5): 3
  List of ingredients (for example, chicken, potatoes, and carrots): onion,milk
  Filter (for example, vegetarian, vegan, or gluten-free): no milk

  1. French Onion Soup

  Ingredients:

  -1 large onion, sliced
  -3 cups beef broth
  -1 cup milk
  -6 slices french bread
  -1/4 cup shredded Parmesan cheese
  -1 tablespoon butter
  -1 teaspoon dried thyme
  -1/4 teaspoon salt
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add beef broth, milk, thyme, salt, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Place french bread slices on soup bowls.
  5. Ladle soup over bread.
  6. Sprinkle with Parmesan cheese.

  2. Onion and Potato Soup

  Ingredients:

  -1 large onion, chopped
  -2 cups potatoes, diced
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add potatoes, vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Serve hot.

  3. Creamy Onion Soup

  Ingredients:

  -1 large onion, chopped
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper
  -1/4 cup all-purpose flour
  -1/2 cup shredded Parmesan cheese

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. In a small bowl, whisk together flour and Parmesan cheese until smooth.
  5. Add to soup and simmer for an additional 5 minutes, or until soup has thickened.
  ```

  כפי שאתה רואה, כל המתכונים עם חלב סוננו החוצה. אבל, אם אתה לא סובל לאקטוז, יכול להיות שתרצה לסנן גם מתכונים עם גבינה, לכן יש צורך להיות ברורים.


- **להפיק רשימת קניות**. אנו רוצים להפיק רשימת קניות, תוך התחשבות במה שכבר יש לנו בבית.

  עבור פונקציונליות זו, ניתן לנסות לפתור הכל בפעם אחת או לחלק זאת לשני הפניות. בואו ננסה את הגישה השנייה. כאן אנו מציעים להוסיף הפניה נוספת, אבל כדי שזה יעבוד, יש להוסיף את התוצאה של ההפניה הראשונה כהקשר להפניה השנייה.

  אתר את החלק בקוד שמדפיס את התוצאה מההפניה הראשונה והוסף את הקוד הבא מתחתיו:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # הדפס תגובה
  print("Shopping list:")
  print(response.output_text)
  ```

  שים לב לדברים הבאים:

  1. אנו בונים הפניה חדשה על ידי הוספת התוצאה מההפניה הראשונה להפניה החדשה:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. מבצעים בקשה חדשה, אך גם מתחשבים במספר הטוקנים שביקשנו בהפניה הראשונה, ולכן הפעם נגדיר `max_output_tokens` כ-1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     אחרי הרצת הקוד הזה, נקבל את הפלט הבא:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## שפר את ההגדרות שלך

מה שיש לנו עד כה הוא קוד שעובד, אבל יש כמה שיפורים שנוכל לעשות כדי לשפר עוד יותר. כמה דברים שכדאי לעשות הם:

- **להפריד סודות מהקוד**, כמו מפתח ה-API. סודות לא שייכים לקוד ויש לאחסן אותם במיקום מאובטח. כדי להפריד סודות מהקוד, אפשר להשתמש במשתני סביבה וספריות כמו `python-dotenv` כדי לטעון אותם מקובץ. כך זה ייראה בקוד:

  1. צור קובץ `.env` עם התוכן הבא:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > שים לב, עבור Azure OpenAI ב-Microsoft Foundry, יש להגדיר את משתני הסביבה הבאים:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     בקוד, תטען את משתני הסביבה כך:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **מילה על אורך טוקנים**. יש לשקול כמה טוקנים אנחנו צריכים כדי לייצר את הטקסט הרצוי. טוקנים עולים כסף, ולכן כשאפשר, כדאי לנסות להיות יעילים בכמות הטוקנים שבהם נעשה שימוש. לדוגמה, האם ניתן לנסח את ההפניה כך שנשתמש בפחות טוקנים?

  כדי לשנות את מספר הטוקנים, ניתן להשתמש בפרמטר `max_output_tokens`. לדוגמה, אם רוצים להשתמש ב-100 טוקנים, נעשה כך:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **ניסויים עם טמפרטורה**. הטמפרטורה היא פרט שעד כה לא הזכרנו אבל הוא חשוב להקשר של ביצועי התוכנית שלנו. ככל שערך הטמפרטורה גבוה יותר, הפלט יהיה אקראי יותר. לעומת זאת, ככל שערך הטמפרטורה נמוך יותר, הפלט יהיה צפוי יותר. שקול אם אתה רוצה שינוי בפלט או לא.

  כדי לשנות את הטמפרטורה, ניתן להשתמש בפרמטר `temperature`. לדוגמה, אם רוצים להשתמש בטמפרטורה של 0.5, עושים כך:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > שים לב, ככל שהנתון קרוב יותר ל-1.0, כך הפלט יהיה מגוונת יותר.

- **דגמי הסקה לא משתמשים ב-`temperature`**. זו תפנית חשובה לשנת 2026. הדגמים הנוכחיים, שאינם מיושנים, ב-Microsoft Foundry הם **דגמי הסקה** (משפחת GPT-5, סדרת o) - והם **לא תומכים ב-`temperature` או `top_p`** (וגם לא ב-`max_tokens`; יש להשתמש ב-`max_output_tokens`). אם תשלח `temperature` ל-`gpt-5-mini` תקבל שגיאה ש"פרמטר לא נתמך". לכן, כדי לנסות את דוגמת הטמפרטורה שצוינה למעלה, יש להפעיל אותו על דגם שתומך עדיין בבקרות דגימה - לדוגמה דגם פתוח של **Llama** כגון `Llama-3.3-70B-Instruct` מתוך [קטלוג דגמי Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), שנקרא דרך נקודת הקצה Azure AI Inference של Foundry Models (באותו אופן כמו דוגמות `githubmodels-*`). עבור דגמי הסקה כמו GPT-5, אתה מנווט את הפלט אחרת:
  - **הנדסת הפניות** - הוראות ברורות, דוגמאות ופלט מובנה (ראה שיעור [04 - הנדסת הפניות](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) מחליפים את הפונקציות שהיו בעבר לשינוי טמפרטורה.
  - **בקרות הסקה** - פרמטרים כמו מאמץ הסקה/הרחבה סוחרים בין עומק ההסבר לבין זמן ההמתנה והעלות.

  בקיצור: `temperature`/`top_p` עדיין תקפים ברבים מהדגמים (Llama, Mistral, Phi, ומשפחת GPT-4.x - אף ש-GPT-4.x נמצאת בתהליך פחת), אבל הכיוון הוא הנדסת הפניות + בקרות הסקה בדגמי הסקה כמו GPT-5.

## מטלה

במטלה זו, אתה יכול לבחור מה לבנות.

הנה כמה הצעות:

- שפר את אפליקציית יוצר המתכונים להמשיך ולשפר אותה. נסה לשחק עם ערכי הטמפרטורה וההפניות כדי לראות מה אפשר ליצור.
- בנה "חבר לימודים". אפליקציה זו צריכה להיות מסוגלת לענות על שאלות בנושא מסוים, למשל פייתון, אפשר שיהיו הפניות כמו "מה זה נושא מסוים בפייתון?", או אפשר שיהיו הפניות שיגידו, תראה לי קוד לנושא מסוים וכדומה.
- בוט היסטוריה, הפוך את ההיסטוריה לחיה, הנחה את הבוט לשחק דמות היסטורית מסוימת ושאל אותו שאלות על חייו וזמנו.

## פתרון

### חבר לימודים

למטה יש הפניה התחלית, ראה איך תוכל להשתמש בה ולשנות אותה לפי טעמך.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### בוט היסטוריה

הנה כמה הפניות שתוכל להשתמש בהן:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## בדיקת ידע

מה עושה מושג הטמפרטורה?

1. הוא שולט בכמה הפלט אקראי.
1. הוא שולט כמה גדול התגובה.
1. הוא שולט בכמה טוקנים נעשה שימוש.

## 🚀 אתגר

כשאתה עובד על המטלה, נסה לשנות את הטמפרטורה, הגדר אותה ל-0, 0.5 ו-1. זכור ש-0 הוא המגוון הכי פחות ו-1 הוא הכי מגוון. איזה ערך עובד הכי טוב לאפליקציה שלך?

## עבודה נהדרת! המשך ללמוד

אחרי שסיימת את השיעור הזה, בדוק את [אוסף הלמידה ב-AI גנרטיבי שלנו](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) כדי להמשיך ולשפר את הידע שלך ב-AI גנרטיבי!

עבור לשיעור 7 שבו נבחן איך לבנות [אפליקציות שיחה](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->