<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-06-25T14:35:27+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "he"
}
-->
# בניית יישומים ליצירת טקסט

> _(לחץ על התמונה למעלה לצפייה בסרטון של השיעור הזה)_

עד כה, ראיתם דרך תוכנית הלימודים הזו שישנם מושגים בסיסיים כמו פקודות ואפילו תחום שלם שנקרא "הנדסת פקודות". כלים רבים שבהם תוכלו להשתמש, כמו ChatGPT, Office 365, Microsoft Power Platform ועוד, תומכים בשימוש בפקודות כדי להשיג משהו.

כדי להוסיף חוויה כזו לאפליקציה, עליך להבין מושגים כמו פקודות, השלמות ולבחור ספרייה לעבוד איתה. זה בדיוק מה שתלמד בפרק זה.

## מבוא

בפרק זה תלמדו:

- על ספריית openai והמושגים הבסיסיים שלה.
- לבנות אפליקציה ליצירת טקסט באמצעות openai.
- להבין כיצד להשתמש במושגים כמו פקודה, טמפרטורה וטוקנים כדי לבנות אפליקציה ליצירת טקסט.

## מטרות למידה

בסוף השיעור הזה תוכל:

- להסביר מהי אפליקציה ליצירת טקסט.
- לבנות אפליקציה ליצירת טקסט באמצעות openai.
- להגדיר את האפליקציה שלך לשימוש ביותר או פחות טוקנים וגם לשנות את הטמפרטורה, עבור תוצאה מגוונת.

## מהי אפליקציה ליצירת טקסט?

בדרך כלל, כשאתה בונה אפליקציה יש לה סוג של ממשק כמו הבא:

- מבוסס פקודות. אפליקציות קונסולה הן אפליקציות טיפוסיות שבהן אתה מקליד פקודה והיא מבצעת משימה. לדוגמה, `git` היא אפליקציה מבוססת פקודות.
- ממשק משתמש (UI). ישנן אפליקציות עם ממשקי משתמש גרפיים (GUIs) שבהן אתה לוחץ על כפתורים, מכניס טקסט, בוחר אפשרויות ועוד.

### אפליקציות קונסולה ו-UI מוגבלות

השווה זאת לאפליקציה מבוססת פקודות שבה אתה מקליד פקודה:

- **זה מוגבל**. אתה לא יכול להקליד כל פקודה, רק את אלה שהאפליקציה תומכת בהן.
- **שפה ספציפית**. ישנן אפליקציות שתומכות בשפות רבות, אך כברירת מחדל האפליקציה בנויה לשפה מסוימת, גם אם ניתן להוסיף תמיכה בשפות נוספות.

### יתרונות של אפליקציות ליצירת טקסט

אז איך אפליקציה ליצירת טקסט שונה?

באפליקציה ליצירת טקסט יש לך יותר גמישות, אתה לא מוגבל למערכת פקודות או לשפת קלט ספציפית. במקום זאת, אתה יכול להשתמש בשפה טבעית כדי לתקשר עם האפליקציה. יתרון נוסף הוא שאתה כבר מתקשר עם מקור נתונים שאומן על כמות עצומה של מידע, בעוד שאפליקציה מסורתית עשויה להיות מוגבלת למה שיש במסד הנתונים.

### מה אני יכול לבנות עם אפליקציה ליצירת טקסט?

ישנם דברים רבים שתוכל לבנות. לדוגמה:

- **צ'אטבוט**. צ'אטבוט שעונה על שאלות בנושאים, כמו החברה שלך והמוצרים שלה, יכול להיות התאמה טובה.
- **עוזר**. LLMs מצוינים בדברים כמו סיכום טקסט, קבלת תובנות מטקסט, יצירת טקסט כמו קורות חיים ועוד.
- **עוזר קוד**. בהתאם לדגם השפה שבו אתה משתמש, אתה יכול לבנות עוזר קוד שעוזר לך לכתוב קוד. לדוגמה, אתה יכול להשתמש במוצר כמו GitHub Copilot וגם ב-ChatGPT כדי לעזור לך לכתוב קוד.

## איך אני יכול להתחיל?

ובכן, אתה צריך למצוא דרך לשלב עם LLM שבדרך כלל כוללת את שתי הגישות הבאות:

- השתמש ב-API. כאן אתה בונה בקשות אינטרנט עם הפקודה שלך ומקבל טקסט שנוצר בחזרה.
- השתמש בספרייה. ספריות עוזרות להקיף את קריאות ה-API ולהפוך אותן לקלות יותר לשימוש.

## ספריות/SDKs

ישנן כמה ספריות ידועות לעבודה עם LLMs כמו:

- **openai**, ספרייה זו מקלה על החיבור לדגם שלך ושליחת פקודות.

ואז יש ספריות שפועלות ברמה גבוהה יותר כמו:

- **Langchain**. Langchain ידועה ותומכת ב-Python.
- **Semantic Kernel**. Semantic Kernel היא ספרייה של מיקרוסופט התומכת בשפות C#, Python ו-Java.

## אפליקציה ראשונה באמצעות openai

בואו נראה איך אנחנו יכולים לבנות את האפליקציה הראשונה שלנו, אילו ספריות אנחנו צריכים, כמה נדרש וכדומה.

### התקנת openai

ישנן ספריות רבות שם כדי לתקשר עם OpenAI או Azure OpenAI. ניתן להשתמש בשפות תכנות רבות כמו C#, Python, JavaScript, Java ועוד. בחרנו להשתמש בספריית `openai` Python, אז נשתמש ב-`pip` כדי להתקין אותה.

```bash
pip install openai
```

### יצירת משאב

עליך לבצע את השלבים הבאים:

- צור חשבון ב-Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- קבל גישה ל-Azure OpenAI. עבור ל-[https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) ובקש גישה.

  > [!NOTE]
  > בזמן כתיבת שורות אלה, עליך להגיש בקשה לגישה ל-Azure OpenAI.

- התקן Python <https://www.python.org/>
- צור משאב של Azure OpenAI Service. ראה מדריך זה כיצד [ליצור משאב](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### מצא את מפתח ה-API והנקודת קצה

בשלב זה, עליך להגיד לספריית `openai` שלך איזה מפתח API להשתמש. כדי למצוא את מפתח ה-API שלך, עבור לקטע "Keys and Endpoint" במשאב Azure OpenAI שלך והעתק את הערך "Key 1".

עכשיו כשיש לך את המידע הזה מועתק, בוא ננחה את הספריות להשתמש בו.

> [!NOTE]
> כדאי להפריד את מפתח ה-API שלך מהקוד. ניתן לעשות זאת על ידי שימוש במשתני סביבה.
>
> - הגדר את משתנה הסביבה `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### הגדרת תצורה ב-Azure

אם אתה משתמש ב-Azure OpenAI, הנה איך אתה מגדיר את התצורה:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

למעלה אנחנו מגדירים את הדברים הבאים:

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion` class. הנה דוגמה:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

בקוד למעלה, אנחנו יוצרים אובייקט השלמה ומעבירים את הדגם שאנחנו רוצים להשתמש בו ואת הפקודה. לאחר מכן אנחנו מדפיסים את הטקסט שנוצר.

### השלמות צ'אט

עד כה, ראית איך השתמשנו ב-`Completion` to generate text. But there's another class called `ChatCompletion` שמתאים יותר לצ'אטבוטים. הנה דוגמה לשימוש בו:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

עוד על פונקציונליות זו בפרק הקרוב.

## תרגיל - האפליקציה הראשונה שלך ליצירת טקסט

עכשיו שלמדנו כיצד להגדיר ולהגדיר את openai, הגיע הזמן לבנות את האפליקציה הראשונה שלך ליצירת טקסט. כדי לבנות את האפליקציה שלך, בצע את השלבים הבאים:

1. צור סביבה וירטואלית והתקן openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > אם אתה משתמש ב-Windows הקלד `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` value.

1. צור קובץ _app.py_ ותן לו את הקוד הבא:

   ```python
   import openai

   openai.api_key = "<replace this value with your open ai key or Azure OpenAI key>"

   openai.api_type = 'azure'
   openai.api_version = '2023-05-15'
   openai.api_base = "<endpoint found in Azure Portal where your API key is>"
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"
   messages = [{"role": "user", "content": prompt}]

   # make completion
   completion = openai.chat.completions.create(model=deployment_name, messages=messages)

   # print response
   print(completion.choices[0].message.content)
   ```

   > [!NOTE]
   > אם אתה משתמש ב-Azure OpenAI, עליך להגדיר את `api_type` to `azure` and set the `api_key` למפתח Azure OpenAI שלך.

   אתה אמור לראות פלט כמו הבא:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## סוגים שונים של פקודות, לדברים שונים

עכשיו ראית איך לייצר טקסט באמצעות פקודה. יש לך אפילו תוכנית פועלת שתוכל לשנות ולשנות כדי לייצר סוגים שונים של טקסט.

פקודות יכולות לשמש לכל מיני משימות. לדוגמה:

- **יצירת סוג של טקסט**. לדוגמה, אתה יכול לייצר שיר, שאלות לחידון וכו'.
- **חיפוש מידע**. אתה יכול להשתמש בפקודות כדי לחפש מידע כמו בדוגמה הבאה 'מה המשמעות של CORS בפיתוח אתרים?'.
- **יצירת קוד**. אתה יכול להשתמש בפקודות כדי ליצור קוד, לדוגמה לפתח ביטוי רגולרי המשמש לאימות כתובות דוא"ל או למה לא ליצור תוכנית שלמה, כמו אפליקציית אינטרנט?

## מקרה שימוש מעשי יותר: יוצר מתכונים

דמיין שיש לך מרכיבים בבית ואתה רוצה לבשל משהו. לשם כך, אתה צריך מתכון. דרך למצוא מתכונים היא להשתמש במנוע חיפוש או שאתה יכול להשתמש ב-LLM כדי לעשות זאת.

תוכל לכתוב פקודה כמו כך:

> "הראה לי 5 מתכונים למנה עם המרכיבים הבאים: עוף, תפוחי אדמה וגזר. לכל מתכון, רשום את כל המרכיבים המשמשים"

בהינתן הפקודה לעיל, ייתכן שתקבל תגובה דומה ל:

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

תוצאה זו נהדרת, אני יודע מה לבשל. בשלב זה, מה שיכול להיות שיפורים מועילים הם:

- סינון מרכיבים שאני לא אוהב או שאני אלרגי אליהם.
- יצירת רשימת קניות, במקרה שאין לי את כל המרכיבים בבית.

למקרים לעיל, נוסיף פקודה נוספת:

> "אנא הסר מתכונים עם שום כי אני אלרגי והחלף אותו במשהו אחר. כמו כן, אנא צור רשימת קניות למתכונים, בהתחשב בכך שכבר יש לי עוף, תפוחי אדמה וגזר בבית."

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

אלה חמשת המתכונים שלך, ללא שום מוזכר ויש לך גם רשימת קניות בהתחשב במה שכבר יש לך בבית.

## תרגיל - בניית יוצר מתכונים

עכשיו ששיחקנו תרחיש, בואו נכתוב קוד שיתאים לתרחיש שהודגם. כדי לעשות זאת, בצע את השלבים הבאים:

1. השתמש בקובץ _app.py_ הקיים כנקודת התחלה
1. מצא את המשתנה `prompt` ושנה את הקוד שלו לקוד הבא:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   אם עכשיו תריץ את הקוד, אתה אמור לראות פלט דומה ל:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > הערה, ה-LLM שלך הוא לא דטרמיניסטי, כך שייתכן שתקבל תוצאות שונות בכל פעם שאתה מריץ את התוכנית.

   נהדר, בואו נראה איך אנחנו יכולים לשפר את הדברים. כדי לשפר את הדברים, אנחנו רוצים לוודא שהקוד גמיש, כך שניתן לשפר ולשנות את המרכיבים ומספר המתכונים.

1. בואו נשנה את הקוד בדרך הבאה:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   לקחת את הקוד לריצת מבחן, יכול להיראות כך:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### שיפור על ידי הוספת סינון ורשימת קניות

כעת יש לנו אפליקציה עובדת שמסוגלת לייצר מתכונים והיא גמישה שכן היא מסתמכת על קלטים מהמשתמש, גם במספר המתכונים וגם במרכיבים המשמשים.

כדי לשפר עוד יותר, אנחנו רוצים להוסיף את הדברים הבאים:

- **סינון מרכיבים**. אנחנו רוצים להיות מסוגלים לסנן מרכיבים שאנחנו לא אוהבים או שאנחנו אלרגיים אליהם. כדי לבצע שינוי זה, אנחנו יכולים לערוך את הפקודה הקיימת שלנו ולהוסיף תנאי סינון לסופה כך:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  למעלה, אנחנו מוסיפים `{filter}` לסוף הפקודה ואנחנו גם תופסים את ערך הסינון מהמשתמש.

  דוגמה לקלט של הפעלת התוכנית יכולה להיראות כך:

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

  כפי שאתה רואה, כל המתכונים עם חלב סוננו החוצה. אבל, אם אתה רגיש ללקטוז, ייתכן שתרצה לסנן מתכונים עם גבינה גם כן, אז יש צורך להיות ברור.

- **יצירת רשימת קניות**. אנחנו רוצים ליצור רשימת קניות, בהתחשב במה שכבר יש לנו בבית.

  לפונקציונליות זו, נוכל לנסות לפתור הכל בפקודה אחת או שנוכל לפצל אותה לשתי פקודות. בואו ננסה את הגישה השנייה. כאן אנחנו מציעים להוסיף פקודה נוספת, אבל כדי שזה יעבוד, אנחנו צריכים להוסיף את תוצאת הפקודה הראשונה כקונטקסט לפקודה השנייה.

  מצא את החלק בקוד שמדפיס את התוצאה מהפקודה הראשונה והוסף את הקוד הבא למטה:

  ```python
  old_prompt_result = completion.choices[0].message.content
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  messages = [{"role": "user", "content": new_prompt}]
  completion = openai.Completion.create(engine=deployment_name, messages=messages, max_tokens=1200)

  # print response
  print("Shopping list:")
  print(completion.choices[0].message.content)
  ```

  שים לב לדברים הבאים:

  1. אנחנו בונים פקודה חדשה על ידי הוספת התוצאה מהפקודה הראשונה לפקודה החדשה:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. אנחנו מבצעים בקשה חדשה, אך גם בהתחשב במספר הטוקנים שביקשנו בפקודה הראשונה, כך שהפעם אנחנו אומרים ש-`max_tokens` הוא 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     לקחת את הקוד לסיבוב, אנחנו עכשיו מגיעים לפלט הבא:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## שפר את ההגדרה שלך

מה שיש לנו עד כה הוא קוד שעובד, אבל יש כמה שיפורים שאנחנו צריכים לעשות כדי לשפר את הדברים עוד יותר. כמה דברים שאנחנו צריכים לעשות הם:

- **הפרדת סודות מהקוד**, כמו מפתח ה-API. סודות לא שייכים לקוד ויש לאחסן אותם במקום מאובטח. כדי להפריד סודות מהקוד, אנחנו יכולים להשתמש במשתני סביבה וספריות כמו `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` file עם התוכן הבא:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > שים לב, עבור Azure, עליך להגדיר את משתני הסביבה הבאים:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     בקוד, היית טוען את משתני הסביבה כך:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **מילה על אורך טוקנים**. אנחנו צריכים לשקול כמה טוקנים אנחנו צריכים כדי לייצר את הטקסט שאנחנו רוצים. טוקנים עולים כסף, אז במידת האפשר, אנחנו צריכים לנסות להיות חסכוניים עם מספר הטוקנים שאנחנו משתמשים בהם. לדוגמה, האם אנחנו יכולים לנסח את הפקודה כך שנוכל להשתמש בפחות טוקנים?

  כדי לשנות את הטוקנים המשמשים, אתה יכול להשתמש בפרמטר `max_tokens`. לדוגמה, אם אתה רוצה להשתמש ב-100 טוקנים, היית עושה:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **ניסוי עם טמפרטורה**. טמפרטורה היא משהו שלא הזכרנו עד כה אבל היא הקשר חשוב לאופן שבו התוכנית שלנו פועלת. ככל שערך הטמפרטורה גבוה יותר, כך הפלט יהיה אקראי יותר. לעומת זאת, ככל שערך הטמפרטורה נמוך יותר, כך הפלט יהיה צפוי יותר. שקול אם אתה רוצה וריאציה בפלט שלך או לא.

  כדי לשנות את הטמפרטורה, אתה יכול להשתמש בפרמטר `temperature`. לדוגמה, אם אתה רוצה להשתמש בטמפרטורה של 0.5, היית עושה:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > שים לב, ככל שהערך קרוב יותר ל-1.0, כך הפלט יהיה מגוון יותר.

## מטלה

למטלה זו, תוכל לבחור מה לבנות.

הנה כמה הצעות:

- שנה את אפליקציית יוצר המתכונים כדי לשפר אותה עוד יותר. שחק עם ערכי הטמפרטורה והפקודות כדי לראות מה תוכל להמציא.
- בנה "חבר לימודים". אפליקציה זו צריכה להיות מסוגלת לענות על שאלות בנושא, לדוגמה Python, תוכל לכלול פקודות כמו "מהו נושא מסוים ב-Python?", או תוכל לכלול פקודה שאומרת, הצג לי קוד לנושא מסוים וכו'.
- בוט היסטוריה, הפוך את ההיסטוריה לחיה, הנ

**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). בעוד שאנו שואפים לדיוק, אנא היו מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. יש לראות במסמך המקורי בשפתו המקורית כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. אנו לא נושאים באחריות לאי הבנות או לפרשנויות מוטעות הנובעות מהשימוש בתרגום זה.