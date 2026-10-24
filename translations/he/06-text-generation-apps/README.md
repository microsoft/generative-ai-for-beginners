# בניית יישומים ליצירת טקסט

[![בניית יישומים ליצירת טקסט](../../../translated_images/he/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(לחץ על התמונה למעלה לצפייה בסרטון של השיעור)_

עד כה ראיתם דרך תוכנית הלימודים שיש מושגים מרכזיים כמו פרומפטים ואפילו תחום שלם שנקרא "הנדסת פרומפטים". כלים רבים שניתן להשתמש איתם כמו ChatGPT, Office 365, Microsoft Power Platform ועוד, תומכים בשימוש בפרומפטים כדי להשיג משהו מסוים.

כדי להוסיף חוויה כזו לאפליקציה, עליך להבין מושגים כמו פרומפטים, השלמות ולבחור ספרייה לעבודה. זה בדיוק מה שלמדת בפרק זה.

## מבוא

בפרק זה תלמד:

- ללמוד על ספריית openai ומושגיה המרכזיים.
- לבנות אפליקציה ליצירת טקסט באמצעות openai.
- להבין כיצד להשתמש במושגים כמו פרומפט, טמפרטורה וטוקנים כדי לבנות אפליקציית יצירת טקסט.

## מטרות הלמידה

בסיום שיעור זה תוכל:

- להסביר מהי אפליקציה ליצירת טקסט.
- לבנות אפליקציה ליצירת טקסט באמצעות openai.
- להגדיר את האפליקציה לשימוש יותר או פחות טוקנים וגם לשנות את הטמפרטורה, לקבלת פלט מגוון.

## מהי אפליקציה ליצירת טקסט?

בדרך כלל כשאתה בונה אפליקציה יש לה ממשק כלשהו כמו הבא:

- מבוסס פקודות. אפליקציות קונסולה הן אפליקציות טיפוסיות שבהן אתה מקליד פקודה והן מבצעות משימה. לדוגמה, `git` היא אפליקציה מבוססת פקודות.
- ממשק משתמש (UI). באפליקציות מסוימות יש ממשקי משתמש גרפיים (GUIs) שבהם לוחצים על כפתורים, מזינים טקסט, בוחרים אפשרויות ועוד.

### אפליקציות קונסולה ו-UI מוגבלות

השווה זאת לאפליקציה מבוססת פקודה שבה אתה מקליד פקודה:

- **זו הגבלה**. אתה לא יכול פשוט להקליד כל פקודה, רק את אלה שהאפליקציה תומכת בהן.
- **שפה ספציפית**. באפליקציות מסוימות יש תמיכה בשפות רבות, אך כברירת מחדל האפליקציה בנויה עבור שפה מסוימת, גם אם ניתן להוסיף תמיכה בשפות נוספות.

### יתרונות של אפליקציות ליצירת טקסט

אז איך אפליקציית יצירת טקסט שונה?

באפליקציה ליצירת טקסט יש לך יותר גמישות, אינך מוגבל למערך פקודות או לשפת קלט מסוימת. במקום זאת, תוכל להשתמש בשפה טבעית כדי לתקשר עם האפליקציה. יתרון נוסף הוא שכבר אתה מתקשר עם מקור מידע שאומן על קבוצה נרחבת של נתונים, בעוד אפליקציה מסורתית עשויה להיות מוגבלת למה שנמצא בבסיס הנתונים.

### מה ניתן לבנות עם אפליקציית יצירת טקסט?

יש הרבה דברים שאפשר לבנות. לדוגמה:

- **צ'אטבוט**. צ'אטבוט שמענה על שאלות בנושאים שונים, כמו החברה שלך ומוצריה, יכול להתאים מאוד.
- **עוזר**. LLMs מצטיינים בדברים כמו סיכום טקסט, הוצאת תובנות מטקסט, יצירת טקסט כמו קורות חיים ועוד.
- **עוזר קוד**. בהתאם לדגם השפה שבו אתה משתמש, תוכל לבנות עוזר קוד שעוזר לך לכתוב קוד. למשל, תוכל להשתמש במוצר כמו GitHub Copilot וגם ChatGPT כדי לעזור לך לכתוב קוד.

## איך אפשר להתחיל?

ובכן, צריך למצוא דרך להשתלב עם LLM שבדרך כלל כוללת את שתי הגישות הבאות:

- להשתמש ב-API. כאן אתה בונה בקשות ווב עם הפרומפט שלך ומקבל טקסט שנוצר בחזרה.
- להשתמש בספרייה. ספריות עוזרות לארוז את קריאות ה-API ולהפוך אותן לקלות יותר לשימוש.

## ספריות/SDKs

יש כמה ספריות מוכרות לעבודה עם LLMs כמו:

- **openai**, ספרייה זו מקלה על החיבור לדגם שלך ושליחת פרומפטים.

אחר כך יש ספריות שפועלות ברמה גבוהה יותר כמו:

- **Langchain**. Langchain ידועה ותומכת בפייתון.
- **Semantic Kernel**. Semantic Kernel היא ספרייה של מיקרוסופט התומכת בשפות C#, Python ו-Java.

## האפליקציה הראשונה באמצעות openai

נראה איך אפשר לבנות את האפליקציה הראשונה שלנו, אילו ספריות אנחנו צריכים, כמה זה דרוש וכן הלאה.

### התקנת openai

יש הרבה ספריות לעבודה עם OpenAI או Azure OpenAI. ניתן להשתמש גם בשפות תכנות רבות כמו C#, Python, JavaScript, Java ועוד. בחרנו להשתמש בספריית `openai` ב-Python, לכן נשתמש ב-`pip` כדי להתקין אותה.

```bash
pip install openai
```

### יצירת משאב

יש לבצע את הצעדים הבאים:

- ליצור חשבון על Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- לקבל גישה ל-Azure OpenAI. עבור אל [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) ובקש גישה.

  > [!NOTE]
  > בזמן כתיבת שורות אלו, יש להגיש בקשה לגישה ל-Azure OpenAI.

- התקן פייתון <https://www.python.org/>
- ליצור משאב שירות Azure OpenAI. ראה מדריך כיצד [ליצור משאב](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### מצא את מפתח ה-API וכתובת הקצה

בשלב זה, אתה צריך ליידע את ספריית `openai` איזה מפתח API להשתמש. כדי למצוא את מפתח ה-API שלך, עבור לקטגוריית "מפתחות וכתובות קצה" במשאב Azure OpenAI והעתק את הערך "Key 1".

![לוח מפתחות וכתובות קצה בפורטל Azure](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

עכשיו כשיש לך מידע זה, ננחה את הספריות להשתמש בו.

> [!NOTE]
> כדאי להפריד את מפתח ה-API מהקוד שלך. ניתן לעשות זאת באמצעות משתני סביבה.
>
> - הגדר את משתנה הסביבה `OPENAI_API_KEY` למפתח ה-API שלך.
>   `export OPENAI_API_KEY='sk-...'`

### הגדרות Azure

אם אתה משתמש ב-Azure OpenAI (כעת חלק מ-Microsoft Foundry), כך תגדיר את ההגדרות. אנו משתמשים בלקוח `OpenAI` סטנדרטי שמכוון לכתובת הקצה של Azure OpenAI `/openai/v1/`, שעובד עם Responses API ואין צורך ב-`api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

למעלה אנו מגדירים את הדברים הבאים:

- `api_key`, זה המפתח API שלך שנמצא בפורטל Azure או בפורטל Microsoft Foundry.
- `base_url`, זה כתובת הקצה של המשאב Foundry עם `/openai/v1/` שמצורף. כתובת הקצה היציבה v1 עובדת גם עם OpenAI וגם עם Azure OpenAI ללא ניהול `api_version`.

> [!NOTE] > `os.environ` קורא משתני סביבה. ניתן להשתמש בו כדי לקרוא משתני סביבה כמו `AZURE_OPENAI_API_KEY` ו-`AZURE_OPENAI_ENDPOINT`. הגדר משתני סביבה אלה בטרמינל או באמצעות ספרייה כמו `dotenv`.

## יצירת טקסט

הדרך ליצירת טקסט היא להשתמש ב-Responses API באמצעות המתודה `responses.create`. להלן דוגמה:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

בקוד שלמעלה, אנו יוצרים תגובה ומעבירים את הדגם שבו אנו רוצים להשתמש ואת הפרומפט. לאחר מכן מדפיסים את הטקסט שנוצר באמצעות `response.output_text`.

### שיחות מרובות סבבים

Responses API מתאים גם ליצירת טקסט בסבב יחיד וגם לצ'אטבוטים רב-סבביים - אתה מספק רשימת הודעות ב-`input` כדי לבנות שיחה:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

פרטים נוספים על פונקציונליות זו בפרק הבא.

## תרגיל - אפליקציית יצירת הטקסט הראשונה שלך

כעת שלמדנו כיצד להגדיר ולהקים את openai, הגיע הזמן לבנות את אפליקציית יצירת הטקסט הראשונה שלך. כדי לבנות את האפליקציה, בצע את השלבים הבאים:

1. צור סביבת פייתון וירטואלית והתקן את openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > אם אתה משתמש ב-Windows, הקלד `venv\Scripts\activate` במקום `source venv/bin/activate`.

   > [!NOTE]
   > אתר את מפתח Azure OpenAI שלך על ידי כניסה ל-[https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) וחפש `Open AI` ובחר `Open AI resource` ואז בחר `Keys and Endpoint` והעתק את הערך `Key 1`.

1. צור קובץ _app.py_ ותן לו את הקוד הבא:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"

   # make a request using the Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # print response
   print(response.output_text)
   ```

   > [!NOTE]
   > אם אתה משתמש ב-OpenAI רגיל (לא ב-Azure), השתמש ב-`client = OpenAI(api_key="<replace this value with your OpenAI key>")` (ללא `base_url`) ועבר שם דגם כמו `gpt-5-mini` במקום שם פריסת שירות.

   אתה אמור לראות פלט כזה:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## סוגים שונים של פרומפטים, לדברים שונים

עתה ראית כיצד ליצור טקסט באמצעות פרומפט. אפילו יש לך תוכנית פועלת שאותה תוכל לשנות ולשדרג כדי ליצור סוגים שונים של טקסט.

אפשר להשתמש בפרומפטים לכל מיני משימות. לדוגמה:

- **ליצור סוג של טקסט**. לדוגמה, אפשר ליצור שיר, שאלות לחידון ועוד.
- **לחפש מידע**. ניתן להשתמש בפרומפטים כדי לחפש מידע כמו בדוגמה הבאה 'מה משמעות CORS בפיתוח ווב?'.
- **ליצור קוד**. אפשר להשתמש בפרומפטים כדי ליצור קוד, למשל לפיתוח ביטוי רגולרי לאימות מיילים או אפילו לייצר תוכנית שלמה, כמו אפליקציית ווב.

## מקרה שימוש מעשי יותר: מחולל מתכונים

דמיין שיש לך חומרי גלם בבית ואתה רוצה לבשל משהו. בשביל זה, אתה צריך מתכון. דרך למצוא מתכונים היא להשתמש במנוע חיפוש או שתוכל להשתמש ב-LLM כדי לעשות זאת.

תוכל לכתוב פרומפט כך:

> "הראה לי 5 מתכונים למנה עם החומרים הבאים: עוף, תפוחי אדמה וגזר. עבור כל מתכון, רשום את כל חומרי הגלם."

לפי הפרומפט הנ"ל, ייתכן שתקבל תגובה דומה ל:

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

התוצאה טובה, אני יודע מה לבשל. בשלב זה, שיפורים שיכולים להיות מועילים הם:

- סינון חומרים שאינם אהובים עלי או אלרגיים אליהם.
- יצירת רשימת קניות, למקרה שאין לי את כל החומרים בבית.

למקרים לעיל, נוסיף פרומפט נוסף:

> "אנא הסר מתכונים עם שום כי אני אלרגי והחלף במשהו אחר. בנוסף, אנא הפק רשימת קניות עבור המתכונים, תוך התחשבות שכבר יש לי עוף, תפוחי אדמה וגזר בבית."

עכשיו יש לך תוצאה חדשה, כלומר:

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

אלה הם חמשת המתכונים שלך, ללא שום שמוזכר וגם יש לך רשימת קניות בהתחשב במה שכבר יש לך בבית.

## תרגיל - בניית מחולל מתכונים

עכשיו כששיחקנו תסריט, בוא נכתוב קוד שיתאים לתסריט שהודגם. לשם כך, בצע את השלבים הבאים:

1. השתמש בקובץ הקיים _app.py_ כנקודת התחלה
1. אתר את המשתנה `prompt` ושנה את הקוד שלו כך:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   אם תפעיל כעת את הקוד, אמור להופיע פלט דומה ל:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > שים לב, ה-LLM שלך אינו דטרמיניסטי, לכן ייתכן שתקבל תוצאות שונות בכל הרצה.

   מעולה, נראה כיצד לשפר את הדברים. לשיפור, אנו רוצים שלקוד יהיה גמישות, כך שניתן ישתנה ויוגדל מספר המתכונים וגם החומרים.

1. נשנה את הקוד כך:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   לקיחת הקוד להרצה לבדיקה, יכול להראות כך:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### שפר עם הוספת סינון ורשימת קניות

כעת יש לנו אפליקציה פועלת המסוגלת להפיק מתכונים והיא גמישה כיוון שהיא מתבססת על קלט מהמשתמש, הן במספר המתכונים והן בחומרים בשימוש.

כדי לשפרה עוד, נרצה להוסיף את הדברים הבאים:

- **סינון חומרים**. נרצה להיות מסוגלים לסנן חומרים שאיננו אוהבים או אלרגיים אליהם. לשם כך נשנה את הפרומפט הקיים ונוסיף תנאי סינון בסופו כך:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  למעלה הוספנו `{filter}` בסוף הפרומפט וגם לוכדים את ערך הסינון מהמשתמש.

  קלט לדוגמה להרצת התוכנית יכול להיראות כך:

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

  כפי שאתה רואה, כל מתכונים עם חלב סוננו החוצה. אבל אם אתה צליאקי, ייתכן שתרצה לסנן גם מתכונים עם גבינה, לכן יש צורך להיות ברורים.

- **יצירת רשימת קניות**. נרצה לייצר רשימת קניות בהתחשב במה שכבר יש לנו בבית.

  עבור פונקציונליות זו, נוכל לנסות לפתור הכל בפרומפט אחד או לחלק לשני פרומפטים. ננסה את הגישה השנייה. כאן אנו מציעים להוסיף פרומפט נוסף, אך כדי שזה יעבוד, נצטרך להוסיף את תוצאת הפרומפט הקודם בהקשר לפרומפט החדש.

  אתר את החלק בקוד שמדפיס את התוצאה מהפרומפט הראשון והוסף את הקוד הבא מתחתיו:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  שים לב לדברים הבאים:

  1. אנו בונים פרומפט חדש על ידי הוספת התוצאה מהפרומפט הראשון לפרומפט החדש:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. אנו מבצעים בקשה חדשה, אך גם מתחשבים במספר הטוקנים שביקשנו בפרומפט הראשון, לכן הפעם אנו אומרים ש-`max_output_tokens` הוא 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     הרצת הקוד הזה מביאה כעת לפלט הבא:

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

- **להפריד סודות מהקוד**, כמו מפתח ה-API. סודות אינם שייכים לקוד וצריכים להישמר במיקום מאובטח. כדי להפריד בין סודות לקוד, אפשר להשתמש במשתני סביבה ובספריות כמו `python-dotenv` כדי לטעון אותם מקובץ. כך זה ייראה בקוד:

  1. צור קובץ `.env` עם התוכן הבא:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > שים לב, עבור Azure OpenAI ב-Microsoft Foundry, עליך להגדיר במקום זאת את משתני הסביבה הבאים:

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

- **מילה על אורך הטוקנים**. כדאי שנחשוב כמה טוקנים אנחנו זקוקים כדי לייצר את הטקסט הרצוי. טוקנים עולים כסף, אז היכן שאפשר, כדאי שנשתדל להיות חסכוניים במספר הטוקנים שבהם אנו משתמשים. למשל, האם אפשר לנסח את ההנחיה כך שנוכל להשתמש בפחות טוקנים?

  כדי לשנות את מספר הטוקנים בהם משתמשים, אפשר להשתמש בפרמטר `max_output_tokens`. לדוגמה, אם תרצה להשתמש ב-100 טוקנים, תעשה כך:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **התנסות בטמפרטורה**. טמפרטורה היא משהו שעד כה לא דיברנו עליו אבל היא הקשר חשוב לתפקוד התוכנית שלנו. ככל שערך הטמפרטורה גבוה יותר, הפלט יהיה אקראי יותר. לעומת זאת, ככל שערך הטמפרטורה נמוך יותר, הפלט יהיה יותר צפוי. שקול אם אתה רוצה גיוון בפלט שלך או לא.

  כדי לשנות את הטמפרטורה, אפשר להשתמש בפרמטר `temperature`. לדוגמה, אם תרצה להשתמש בטמפרטורה של 0.5, תעשה כך:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > שים לב, ככל שמתקרבים ל-1.0, הפלט יהיה מגוון יותר.

- **מודלים של סיבה לא משתמשים ב-`temperature`**. זהו שינוי חשוב לשנת 2026. המודלים הנוכחיים שאינם מיושנים ב-Microsoft Foundry הם **מודלי סיבה** (משפחת GPT-5, סדרת o) - ואלה **לא תומכים ב-`temperature` או `top_p`** (וגם לא ב-`max_tokens`; השתמש ב-`max_output_tokens`). אם תשלח `temperature` ל-`gpt-5-mini` תקבל שגיאה "פרמטר לא נתמך". אז כדי לנסות את דוגמת הטמפרטורה למעלה, פנה למודל שעדיין תומך בשליטה בדגימה - למשל מודל פתוח **Llama** כמו `Llama-3.3-70B-Instruct` מה- [קטלוג המודלים של Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), שמופעל דרך נקודת הקצה Foundry Models / Azure AI Inference (באותו אופן כמו הדוגמאות של `githubmodels-*`). למודלים של סיבה כמו GPT-5, מכוונים את הפלט אחרת:
  - **הנדסת הנחיות** - הוראות ברורות, דוגמאות ופלט מובנה (ראה שיעור [04 - הנדסת הנחיות](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) מבצעים את העבודה שהכפתורי דגימה היו עושים.
  - **בקרות סיבה** - פרמטרים כמו ניסיון סינון/ריבוי מילים שמאזנים עומק הסיבה מול זמן תגובה ועלות.

  בקיצור: `temperature`/`top_p` עדיין תקפים ברבים מהמודלים (Llama, Mistral, Phi, ומשפחת GPT-4.x - אם כי GPT-4.x מתיישן), אבל הכיוון הוא הנדסת הנחיות + בקרות סיבה במודלים של סיבה כמו GPT-5.

## משימה

למשימה זו, אתה יכול לבחור מה לבנות.

הנה כמה הצעות:

- שפר את אפליקציית מחולל המתכונים כדי לשפר אותה עוד. שחק עם ערכי טמפרטורה, והנחיות כדי לראות מה אתה יכול ליצור.
- בנה "חבר ללמידה". אפליקציה זו צריכה להיות מסוגלת לענות על שאלות בנושא מסוים, לדוגמה Python, תוכל שיהיו הנחיות כמו "מה זה נושא מסוים ב-Python?", או שתוכל לנסח הנחיה שתציג לי קוד בנושא מסוים וכו'.
- בוט היסטוריה, הפוך את ההיסטוריה לחיה, הנחה את הבוט לגלם דמות היסטורית מסוימת ושאל אותו שאלות על חייו וזמנו.

## פתרון

### חבר ללמידה

להלן הנחיה התחלתית, ראה כיצד תוכל להשתמש בה ולשנות אותה לטעמך.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### בוט היסטוריה

הנה כמה הנחיות שאפשר להשתמש בהן:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## בדיקת ידע

מה עושה מושג הטמפרטורה?

1. הוא שולט כמה אקראי הפלט יהיה.
1. הוא שולט כמה גדול התגובה תהיה.
1. הוא שולט בכמה טוקנים משתמשים.

## 🚀 אתגר

כשאתה עובד על המשימה, נסה לשנות את הטמפרטורה, נסה להגדיר אותה ל-0, 0.5, ו-1. זכור ש-0 הוא הכי פחות מגוון ו-1 הוא הכי מגוון. איזה ערך עובד הכי טוב לאפליקציה שלך?

## עבודה נהדרת! המשך ללמוד

לאחר שסיימת את השיעור, בדוק את [אוסף הלמידה של Generative AI שלנו](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) כדי להמשיך לפתח את הידע שלך ב-Generative AI!

עבור לשיעור 7 בו נבחן כיצד [לבנות אפליקציות צ'אט](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->