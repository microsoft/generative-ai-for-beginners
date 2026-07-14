# בניית יישומים ליצירת טקסט

[![בניית יישומים ליצירת טקסט](../../../translated_images/he/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(לחצו על התמונה למעלה כדי לצפות בסרטון השיעור הזה)_

עד כה ראיתם במסגרת הלימודים שיש מושגים מרכזיים כמו פרומפטים ואפילו תחום שלם הנקרא "הנדסת פרומפטים". כלים רבים שאפשר להשתמש בהם כמו ChatGPT, Office 365, Microsoft Power Platform ועוד, תומכים בשימוש בפרומפטים כדי להשיג משהו.

כדי להוסיף חוויה כזו לאפליקציה, אתם צריכים להבין מושגים כמו פרומפטים, השלמות ולבחור ספריה לעבודה. זה בדיוק מה שתלמדו בפרק הזה.

## מבוא

בפרק זה, תלמדו:

- ללמוד על ספריית openai והמושגים המרכזיים שלה.
- לבנות אפליקציה ליצירת טקסט באמצעות openai.
- להבין איך להשתמש במושגים כמו פרומפט, טמפרטורה וטוקנים כדי לבנות אפליקציית יצירת טקסט.

## מטרות הלמידה

בסוף השיעור הזה, תדעו:

- להסביר מהי אפליקציית יצירת טקסט.
- לבנות אפליקציית יצירת טקסט באמצעות openai.
- להגדיר את האפליקציה להשתמש ביותר או פחות טוקנים וגם לשנות את הטמפרטורה, עבור פלט מגוון.

## מהי אפליקציית יצירת טקסט?

בדרך כלל כשבונים אפליקציה יש לה ממשק כלשהו כמו הבא:

- מבוסס פקודות. אפליקציות קונסולה הן אפליקציות טיפוסיות שבהן אתם מקלידים פקודה ומבצעים משימה. לדוגמה, `git` היא אפליקציה מבוססת פקודות.
- ממשק משתמש (UI). כמה אפליקציות כוללות ממשקי משתמש גרפיים (GUI) שבהם לוחצים על כפתורים, מזינים טקסט, בוחרים אפשרויות ועוד.

### אפליקציות קונסולה וממשק משתמש מוגבלות

השוו את זה לאפליקציה מבוססת פקודה שבה אתם מקלידים פקודה:

- **זה מוגבל**. לא תוכלו להקליד כל פקודה, רק את הפקודות שהאפליקציה תומכת בהן.
- **שפת מימוש ספציפית**. כמה אפליקציות תומכות בשפות רבות, אך כברירת מחדל האפליקציה בנויה לשפה ספציפית, אפילו אם ניתן להוסיף תמיכה בשפות נוספות.

### יתרונות אפליקציות יצירת טקסט

אז מה ההבדל באפליקציית יצירת טקסט?

באפליקציית יצירת טקסט יש יותר גמישות, אתם לא מוגבלים למערכת פקודות או שפת קלט ספציפית. במקום זאת, אתם יכולים להשתמש בשפה טבעית כדי לתקשר עם האפליקציה. יתרון נוסף הוא שאתם כבר מתקשרים עם מקור נתונים שנאמן על מאגר ידע ענק, בעוד שאפליקציה מסורתית עלולה להיות מוגבלת למה שיש בבסיס הנתונים.

### מה אפשר לבנות עם אפליקציית יצירת טקסט?

יש הרבה דברים שאפשר לבנות. לדוגמה:

- **צ'טבוט**. צ'טבוט שעונה על שאלות בנושאים כמו החברה שלכם והמוצרים שלה יכול להתאים היטב.
- **עוזר**. מודלים גדולים (LLMs) מצוינים במשימות כמו סיכום טקסט, הפקת תובנות מהטקסט, יצירת טקסטים כמו קורות חיים ועוד.
- **עוזר קוד**. בהתאם למודל השפה שבו משתמשים, אפשר לבנות עוזר קוד שעוזר לכם לכתוב קוד. לדוגמה, תוכלו להשתמש במוצרים כמו GitHub Copilot וגם ChatGPT שיעזרו לכתוב קוד.

## איך אפשר להתחיל?

ובכן, אתם צריכים למצוא דרך להתחבר ל-LLM שלרוב כוללת שתי גישות:

- שימוש ב-API. כאן אתם בונים בקשות רשת עם הפרומפט שלכם ומקבלים טקסט שנוצר בחזרה.
- שימוש בספרייה. ספריות מסייעות לארוז את קריאות ה-API ועושות אותן לקלות יותר.

## ספריות / SDKs

יש כמה ספריות מוכרות לעבודה עם LLMs כמו:

- **openai**, ספרייה זו מקלה על חיבור למודל שלכם ושליחת פרומפטים.

לאחר מכן יש ספריות שעובדות ברמה גבוהה יותר כמו:

- **Langchain**. Langchain מוכרת ותומכת בפייתון.
- **Semantic Kernel**. Semantic Kernel היא ספרייה של מיקרוסופט התומכת בשפות C#, Python ו-Java.

## האפליקציה הראשונה באמצעות openai

בואו נראה איך לבנות את האפליקציה הראשונה שלנו, אילו ספריות אנחנו צריכים, כמה נדרש וכדומה.

### התקנת openai

יש הרבה ספריות לעבוד עם OpenAI או Azure OpenAI. ניתן להשתמש בשפות תכנות רבות כמו C#, Python, JavaScript, Java ועוד. בחרנו להשתמש בספריית הפייתון `openai`, ולכן נשתמש ב-`pip` כדי להתקינה.

```bash
pip install openai
```

### יצירת משאב

יש לבצע את השלבים הבאים:

- צרו חשבון ב-Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- קבלו גישה ל-Azure OpenAI. עברו ל-[https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) ובקשו גישה.

  > [!NOTE]
  > בעת כתיבת מדריך זה, יש להגיש בקשה לקבלת גישה ל-Azure OpenAI.

- התקינו Python <https://www.python.org/>
- צרו משאב שירות Azure OpenAI. ראו מדריך ל[יצירת משאב](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### איתור מפתח API וסיום נקודה (endpoint)

בשלב זה עליכם להגדיר לספריית ה-`openai` איזה מפתח API להשתמש בו. כדי למצוא את מפתח ה-API שלכם, עברו לקטע "Keys and Endpoint" במשאב Azure OpenAI שלכם והעתיקו את הערך "Key 1".

![לוח משאבים Keys and Endpoint בפורטל Azure](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

כעת כשהמידע הזה מועתק, ננחה את הספריות להשתמש בו.

> [!NOTE]
> כדאי להפריד את מפתח ה-API מהקוד שלכם. ניתן לעשות זאת באמצעות משתני סביבה.
>
> - הגדרו את משתנה הסביבה `OPENAI_API_KEY` עם מפתח ה-API שלכם.
>   `export OPENAI_API_KEY='sk-...'`

### הגדרת תצורה ב-Azure

אם אתם משתמשים ב-Azure OpenAI (שכעת חלק מ-Microsoft Foundry), כך מגדירים את התצורה. אנו משתמשים בלקוח הסטנדרטי `OpenAI` הפונה לסיום הנקודה של Azure OpenAI `/openai/v1/`, הפועל עם Responses API ואינו זקוק ל-`api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

למעלה אנו מגדירים את הדברים הבאים:

- `api_key`, זה מפתח ה-API שלכם שנמצא בפורטל Azure או פורטל Microsoft Foundry.
- `base_url`, זה נקודת הקצה של משאב Foundry שלכם עם `/openai/v1/` נוסף בסוף. נקודת הקצה היציבה v1 פועלת הן ב-OpenAI והן ב-Azure OpenAI ללא ניהול `api_version`.

> [!NOTE] > `os.environ` קורא משתני סביבה. אפשר להשתמש בו כדי לקרוא משתני סביבה כמו `AZURE_OPENAI_API_KEY` ו-`AZURE_OPENAI_ENDPOINT`. הגדירו משתני סביבה אלה בטרמינל שלכם או באמצעות ספרייה כמו `dotenv`.

## יצירת טקסט

הדרך ליצור טקסט היא להשתמש ב-Responses API באמצעות מתודת `responses.create`. הנה דוגמה:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # זהו שם הפריסה של המודל שלך
    input=prompt,
    store=False,
)
print(response.output_text)
```

בקוד שלמעלה, אנו יוצרים תגובה ומעבירים את המודל שאנו רוצים להשתמש בו ואת הפרומפט. לאחר מכן מדפיסים את הטקסט שנוצר באמצעות `response.output_text`.

### שיחות עם מספר סבבים

ה-Responses API מתאים לשימוש ליצירת טקסט בסבב יחיד וגם לצ'טבוטים רב-סבביים - אתם מספקים רשימת הודעות ב-`input` כדי לבנות שיחה:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

על פונקציונליות זו נדון בפרק הבא.

## תרגיל - אפליקציית יצירת הטקסט הראשונה שלכם

עכשיו שלמדנו איך להגדיר ולתצרת את openai, הגיע הזמן לבנות את אפליקציית יצירת הטקסט הראשונה שלכם. כדי לבנות את האפליקציה, בצעו את השלבים הבאים:

1. צרו סביבה וירטואלית והתקינו את openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > אם אתם משתמשים ב-Windows הקלידו `venv\Scripts\activate` במקום `source venv/bin/activate`.

   > [!NOTE]
   > איתרו את מפתח Azure OpenAI שלכם דרך [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), חפשו `Open AI` ובחרו את המשאב `Open AI`, לאחר מכן בחרו ב-`Keys and Endpoint` והעתיקו את ערך `Key 1`.

1. צרו קובץ _app.py_ וכתבו בו את הקוד הבא:

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

   # הדפס את התגובה
   print(response.output_text)
   ```

   > [!NOTE]
   > אם אתם משתמשים ב-OpenAI רגיל (לא Azure), השתמשו ב- `client = OpenAI(api_key="<החליפו כאן במפתח OpenAI שלכם>")` (ללא `base_url`) ועברו שם מודל כמו `gpt-4o-mini` במקום שם פריסה.

   צפוי לראות פלט כזה:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## סוגים שונים של פרומפטים, לדברים שונים

עכשיו ראיתם איך ליצור טקסט באמצעות פרומפט. יש לכם כבר תוכנית שפועלת ואפשר לשנות אותה כדי ליצור סוגים שונים של טקסט.

פרומפטים יכולים לשמש למשימות מגוונות. לדוגמה:

- **יצירת סוג טקסט**. לדוגמה, ניתן ליצור שיר, שאלות למבחן ועוד.
- **חיפוש מידע**. אפשר להשתמש בפרומפטים כדי לחפש מידע כמו בדוגמה הבאה: 'מה המשמעות של CORS בפיתוח ווב?'.
- **יצירת קוד**. אפשר להשתמש בפרומפטים ליצירת קוד, למשל לפתח ביטוי רגולרי לבדיקת אימיילים או אפילו ליצור תוכנית שלמה, כמו אפליקציית ווב?

## מקרה שימוש מעשי יותר: מחולל מתכונים

דמיינו שיש לכם בבית מרכיבים ואתם רוצים לבשל משהו. בשביל זה יש צורך במתכון. דרך למצוא מתכונים היא להשתמש במנוע חיפוש או שניתן להשתמש ב-LLM לצורך כך.

תוכלו לכתוב פרומפט כך:

> "הראה לי 5 מתכונים למנה עם המרכיבים הבאים: עוף, תפוחי אדמה וגזר. לכל מתכון פרט את כל המרכיבים."

בהתחשב בפרומפט זה, תקבלו תגובה דומה ל:

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

התוצאה הזו מצוינת, אני יודע מה לבשל. בשלב זה שיפורים שיכולים להיות מועילים הם:

- סינון מרכיבים שלא אוהב או שאלרגי אליהם.
- יצירת רשימת קניות במקרה שאין לי את כל המרכיבים בבית.

למקרים הנ"ל, נוסיף פרומפט נוסף:

> "אנא הסר מתכונים עם שום כי יש לי אלרגיה והחלף במשהו אחר. כמו כן, אנא הפק רשימת קניות למתכונים בהתחשב שיש לי עוף, תפוחי אדמה וגזר בבית."

כעת יש לכם תוצאה חדשה, כלומר:

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

אלה חמשת המתכונים שלכם, ללא שום ומלווה גם ברשימת קניות בהתחשב במה שכבר יש בבית.

## תרגיל - בניית מחולל מתכונים

לאחר ששיחקנו תרחיש, נכתוב קוד שיתאים לתרחיש שהודגם. לשם כך, בצעו את השלבים הבאים:

1. השתמשו בקובץ _app.py_ הקיים כנקודת התחלה
1. איתרו את המשתנה `prompt` ושנו את קודו ל:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   אם תפעילו כעת את הקוד, אתם אמורים לראות פלט דומה ל:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > שימו לב, ה-LLM שלכם הוא לא דטרמיניסטי, לכן ייתכנו תוצאות שונות בכל הרצה.

   מעולה, בואו נראה איך אפשר לשפר. לשפר את העניין רוצה לוודא שהקוד גמיש, כך שניתן לשנות את המרכיבים ואת כמות המתכונים.

1. נשנה את הקוד כך:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # הצמד את מספר המתכונים לתוך ההודעה ואת המצרכים
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   הריצה לבדיקה יכולה להיראות כך:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### שיפור באמצעות הוספת סינון ורשימת קניות

יש לנו עכשיו אפליקציה פועלת שמסוגלת להפיק מתכונים והיא גמישה כי היא מסתמכת על קלט מהמשתמש, גם במספר המתכונים וגם במרכיבים.

כדי לשפר עוד יותר, נרצה להוסיף את הדברים הבאים:

- **סינון מרכיבים**. נרצה להיות מסוגלים לסנן מרכיבים שאנחנו לא אוהבים או אלרגיים אליהם. כדי להשיג את השינוי הזה, אפשר לערוך את הפרומפט הקיים ולהוסיף תנאי סינון בסופו כך:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  מעלה הוספנו `{filter}` לסוף הפרומפט ואגף גם את ערך הסינון מהמשתמש.

  דוגמת קלט בעת הרצת התוכנית יכולה להיראות כך:

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

  כפי שאתם רואים, כל המתכונים שכוללים חלב סוננו. אבל, אם אתם אלרגיים ללקטוז, אולי תרצו לסנן גם מתכונים שמכילים גבינה, לכן יש צורך להיות ברורים.


- **הפק רשימת קניות**. אנחנו רוצים להפיק רשימת קניות, בהתחשב במה שכבר יש לנו בבית.

  עבור פונקציונליות זו, נוכל לנסות לפתור הכל בבקשת פרומפט אחת או שנוכל לחלק אותה לשתי בקשות פרומפט. בואו ננסה את הגישה השנייה. כאן אנחנו מציעים להוסיף פרומפט נוסף, אבל בשביל שזה יעבוד, אנחנו צריכים להוסיף את תוצאת הפרומפט הראשון כהקשר לפרומפט השני.

  אתר את החלק בקוד שמדפיס את התוצאה מהפרומפט הראשון והוסף את הקוד הבא למטה:

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

  1. אנו בונים פרומפט חדש על ידי הוספת תוצאת הפרומפט הראשון לפרומפט החדש:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. אנו עושים בקשה חדשה, אך גם מתחשבים במספר הטוקנים שביקשנו בפרומפט הראשון, לכן הפעם אנו אומרים ש- `max_output_tokens` הוא 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     כאשר מפעילים קוד זה, אנו מגיעים לפלט הבא:

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

מה שיש לנו עד כה הוא קוד שעובד, אבל יש כמה שינויים שכדאי לעשות כדי לשפר את הדברים עוד יותר. כמה דברים שכדאי לעשות הם:

- **להפריד סודות מהקוד**, כמו מפתח ה-API. סודות לא אמורים להיות בקוד ויש לאחסן אותם במקום מאובטח. כדי להפריד סודות מהקוד, ניתן להשתמש במשתני סביבה ובספריות כמו `python-dotenv` לטעינתם מקובץ. כך זה ייראה בקוד:

  1. צור קובץ `.env` עם התוכן הבא:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > שים לב, עבור Azure OpenAI במייקרוסופט פאונדרי, יש להגדיר את משתני הסביבה הבאים במקום:

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

- **מילה על אורך טוקנים**. כדאי לשקול כמה טוקנים אנחנו צריכים לייצר את הטקסט הרצוי. טוקנים עולים כסף, לכן ככל האפשר, כדאי לנסות להיות חסכניים בכמות הטוקנים שבה משתמשים. למשל, האם נוכל לנסח את הפרומפט כך שנוכל להשתמש בפחות טוקנים?

  כדי לשנות את מספר הטוקנים, ניתן להשתמש בפרמטר `max_output_tokens`. למשל, אם רוצים להשתמש ב-100 טוקנים, עושים כך:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **ניסוי עם טמפרטורה**. טמפרטורה זה דבר שלא דיברנו עליו עד כה אבל הוא חשוב להקשר של איך התוכנית שלנו מתפקדת. ככל שערך הטמפרטורה גבוה יותר, הפלט יהיה אקראי יותר. לעומת זאת, ככל שערך הטמפרטורה נמוך יותר, הפלט יהיה צפוי יותר. שקול האם ברצונך בגיוון בפלט שלך או לא.

  לשינוי הטמפרטורה, אפשר להשתמש בפרמטר `temperature`. למשל, אם רוצים להשתמש בטמפרטורה של 0.5, עושים כך:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > שים לב, ככל שמתקרבים ל-1.0, כך הפלט משתנה יותר.

## מטלה

במטלה זו, ניתן לבחור מה לבנות.

הנה כמה הצעות:

- שפר את אפליקציית יוצר המתכונים עוד יותר. נסה לשחק עם ערכי הטמפרטורה, והפרומפטים כדי לראות מה תוכל להפיק.
- בנה "חבר ללמידה". אפליקציה זו צריכה להיות מסוגלת לענות על שאלות בנושא, לדוגמה Python, אפשר שיהיו פרומפטים כמו "מה זה נושא מסוים ב-Python?", או פרומפט שיגיד, הראה לי קוד לנושא מסוים וכו'.
- בוט היסטוריה, הפוך את ההיסטוריה לחיה, הנחה את הבוט לשחק דמות היסטורית מסוימת ושאל אותו שאלות על חייו וזמנו.

## פתרון

### חבר ללמידה

למטה יש פרומפט התחלה, ראה כיצד תוכל להשתמש בו ולשנות אותו לטעמך.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### בוט היסטוריה

הנה כמה פרומפטים שאפשר להשתמש בהם:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## בדיקת ידע

מה עושה המושג טמפרטורה?

1. הוא שולט כמה אקראי הפלט יהיה.
1. הוא שולט כמה גדול התגובה תהיה.
1. הוא שולט כמה טוקנים משמשים.

## 🚀 אתגר

כשעובדים על המטלה, נסה לגוון את הטמפרטורה, נסה להגדיר אותה ל-0, 0.5, ו-1. זכרו ש-0 הוא הכי פחות מגוון ו-1 הוא הכי מגוון. איזה ערך עובד הכי טוב עבור האפליקציה שלך?

## עבודה נהדרת! המשך ללמוד

לאחר שסיימת את השיעור הזה, עיין באוסף [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) שלנו כדי להמשיך ולשפר את הידע שלך ב-Generative AI!

עבור לשיעור 7 שבו נבחן כיצד [לבנות אפליקציות צ'אט](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->