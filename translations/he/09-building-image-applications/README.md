<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-06-25T17:26:57+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "he"
}
-->
# בניית אפליקציות ליצירת תמונות

יש יותר ב-LLMs מאשר יצירת טקסט. ניתן גם ליצור תמונות מתיאורי טקסט. תמונות כמודל יכולות להיות מאוד שימושיות בתחומים רבים כמו מדטק, אדריכלות, תיירות, פיתוח משחקים ועוד. בפרק זה נסקור את שני המודלים הפופולריים ביותר ליצירת תמונות, DALL-E ו-Midjourney.

## הקדמה

בשיעור זה נכסה:

- יצירת תמונות ולמה זה שימושי.
- DALL-E ו-Midjourney, מה הם ואיך הם עובדים.
- איך לבנות אפליקציה ליצירת תמונות.

## מטרות למידה

לאחר השלמת שיעור זה, תוכל:

- לבנות אפליקציה ליצירת תמונות.
- להגדיר גבולות לאפליקציה שלך עם מטה-פרומפטים.
- לעבוד עם DALL-E ו-Midjourney.

## למה לבנות אפליקציה ליצירת תמונות?

אפליקציות ליצירת תמונות הן דרך מצוינת לחקור את היכולות של AI גנרטיבי. ניתן להשתמש בהן, לדוגמה:

- **עריכת תמונות וסינתזה**. ניתן ליצור תמונות למגוון שימושים, כגון עריכת תמונות וסינתזה של תמונות.

- **מיושם על מגוון תעשיות**. ניתן גם להשתמש בהן ליצירת תמונות למגוון תעשיות כמו מדטק, תיירות, פיתוח משחקים ועוד.

## תרחיש: Edu4All

כחלק מהשיעור הזה, נמשיך לעבוד עם הסטארט-אפ שלנו, Edu4All, בשיעור זה. התלמידים ייצרו תמונות להערכות שלהם, בדיוק אילו תמונות זה תלוי בתלמידים, אבל הם יכולים להיות איורים לסיפור האגדה שלהם או ליצור דמות חדשה לסיפור שלהם או לעזור להם לדמיין את הרעיונות והקונספטים שלהם.

הנה מה שתלמידי Edu4All יכולים ליצור לדוגמה אם הם עובדים בכיתה על אנדרטאות:

> "כלב ליד מגדל אייפל באור שמש מוקדם בבוקר"

## מה זה DALL-E ו-Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) ו-[Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) הם שניים מהמודלים הפופולריים ביותר ליצירת תמונות, הם מאפשרים להשתמש בפרומפטים כדי ליצור תמונות.

### DALL-E

נתחיל עם DALL-E, שהוא מודל AI גנרטיבי שמייצר תמונות מתיאורי טקסט.

- **CLIP**, הוא מודל שמייצר הטבעות, שהן ייצוגים מספריים של נתונים, מתמונות וטקסט.

- **Diffused attention**, הוא מודל שמייצר תמונות מהטבעות. DALL-E מאומן על מערך נתונים של תמונות וטקסט וניתן להשתמש בו כדי ליצור תמונות מתיאורי טקסט. לדוגמה, ניתן להשתמש ב-DALL-E כדי ליצור תמונות של חתול בכובע, או כלב עם מוהוק.

### Midjourney

Midjourney עובד בצורה דומה ל-DALL-E, הוא מייצר תמונות מפרומפטים טקסטואליים. Midjourney, ניתן גם להשתמש בו כדי ליצור תמונות באמצעות פרומפטים כמו "חתול בכובע", או "כלב עם מוהוק".

## איך DALL-E ו-Midjourney עובדים

ראשית, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E הוא מודל AI גנרטיבי המבוסס על ארכיטקטורת טרנספורמר עם _טרנספורמר אוטורגרסיבי_.

טרנספורמר אוטורגרסיבי מגדיר איך מודל מייצר תמונות מתיאורי טקסט, הוא מייצר פיקסל אחד בכל פעם, ואז משתמש בפיקסלים שנוצרו כדי לייצר את הפיקסל הבא. עובר דרך שכבות רבות ברשת עצבית, עד שהתמונה שלמה.

עם תהליך זה, DALL-E, שולט בתכונות, אובייקטים, מאפיינים ועוד בתמונה שהוא מייצר. עם זאת, ל-DALL-E 2 ו-3 יש יותר שליטה על התמונה המיוצרת.

## בניית אפליקציה ראשונה ליצירת תמונות

אז מה נדרש כדי לבנות אפליקציה ליצירת תמונות? אתה צריך את הספריות הבאות:

- **python-dotenv**, מומלץ מאוד להשתמש בספרייה זו כדי לשמור את הסודות שלך בקובץ _.env_ הרחק מהקוד.
- **openai**, ספרייה זו היא מה שתשתמש בו כדי לתקשר עם ה-API של OpenAI.
- **pillow**, לעבוד עם תמונות בפייתון.
- **requests**, כדי לעזור לך לבצע בקשות HTTP.

1. צור קובץ _.env_ עם התוכן הבא:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   מצא את המידע הזה בפורטל Azure עבור המשאב שלך בסעיף "Keys and Endpoint".

1. אסוף את הספריות לעיל בקובץ שנקרא _requirements.txt_ כך:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. לאחר מכן, צור סביבה וירטואלית והתקן את הספריות:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   עבור Windows, השתמש בפקודות הבאות כדי ליצור ולהפעיל את הסביבה הווירטואלית שלך:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. הוסף את הקוד הבא בקובץ שנקרא _app.py_:

   ```python
   import openai
   import os
   import requests
   from PIL import Image
   import dotenv

   # import dotenv
   dotenv.load_dotenv()

   # Get endpoint and key from environment variables
   openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
   openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

   # Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
   openai.api_version = '2023-06-01-preview'
   openai.api_type = 'azure'


   try:
       # Create an image by using the image generation API
       generation_response = openai.Image.create(
           prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
           size='1024x1024',
           n=2,
           temperature=0,
       )
       # Set the directory for the stored image
       image_dir = os.path.join(os.curdir, 'images')

       # If the directory doesn't exist, create it
       if not os.path.isdir(image_dir):
           os.mkdir(image_dir)

       # Initialize the image path (note the filetype should be png)
       image_path = os.path.join(image_dir, 'generated-image.png')

       # Retrieve the generated image
       image_url = generation_response["data"][0]["url"]  # extract image URL from response
       generated_image = requests.get(image_url).content  # download the image
       with open(image_path, "wb") as image_file:
           image_file.write(generated_image)

       # Display the image in the default image viewer
       image = Image.open(image_path)
       image.show()

   # catch exceptions
   except openai.InvalidRequestError as err:
       print(err)

   ```

בוא נסביר את הקוד הזה:

- קודם, אנחנו מייבאים את הספריות שאנחנו צריכים, כולל את ספריית OpenAI, ספריית dotenv, ספריית requests, וספריית Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- לאחר מכן, אנחנו טוענים את משתני הסביבה מהקובץ _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- אחרי זה, אנחנו מגדירים את נקודת הקצה, המפתח ל-API של OpenAI, גרסה וסוג.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- לאחר מכן, אנחנו מייצרים את התמונה:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  הקוד לעיל מגיב עם אובייקט JSON שמכיל את ה-URL של התמונה שנוצרה. אנחנו יכולים להשתמש ב-URL כדי להוריד את התמונה ולשמור אותה בקובץ.

- לבסוף, אנחנו פותחים את התמונה ומשתמשים בצופה תמונות סטנדרטי כדי להציג אותה:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### פרטים נוספים על יצירת התמונה

בואו נסתכל על הקוד שמייצר את התמונה בפירוט נוסף:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, הוא הפרומפט הטקסטואלי שמשמש ליצירת התמונה. במקרה זה, אנחנו משתמשים בפרומפט "ארנב על סוס, מחזיק סוכרייה על מקל, על אחו ערפילי בו צומחים נרקיסים".
- **size**, הוא הגודל של התמונה שנוצרת. במקרה זה, אנחנו מייצרים תמונה בגודל 1024x1024 פיקסלים.
- **n**, הוא מספר התמונות שנוצרות. במקרה זה, אנחנו מייצרים שתי תמונות.
- **temperature**, הוא פרמטר ששולט באקראיות של התוצר של מודל AI גנרטיבי. הטמפרטורה היא ערך בין 0 ל-1 כאשר 0 אומר שהתוצר דטרמיניסטי ו-1 אומר שהתוצר אקראי. ערך ברירת המחדל הוא 0.7.

יש עוד דברים שאתה יכול לעשות עם תמונות שנכסה בסעיף הבא.

## יכולות נוספות של יצירת תמונות

ראית עד כה איך הצלחנו ליצור תמונה באמצעות כמה שורות בפייתון. עם זאת, יש עוד דברים שאתה יכול לעשות עם תמונות.

אתה יכול גם לעשות את הדברים הבאים:

- **בצע עריכות**. על ידי מתן תמונה קיימת מסכה ופרומפט, אתה יכול לשנות תמונה. לדוגמה, אתה יכול להוסיף משהו לחלק מתמונה. דמיין את תמונת הארנב שלנו, אתה יכול להוסיף כובע לארנב. איך היית עושה זאת הוא על ידי מתן התמונה, מסכה (שמזהה את החלק של האזור לשינוי) ופרומפט טקסטואלי לומר מה צריך להיעשות.

  ```python
  response = openai.Image.create_edit(
    image=open("base_image.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="An image of a rabbit with a hat on its head.",
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  התמונה הבסיסית תכיל רק את הארנב אבל התמונה הסופית תכיל את הכובע על הארנב.

- **צור וריאציות**. הרעיון הוא שאתה לוקח תמונה קיימת ומבקש שיווצרו וריאציות. כדי ליצור וריאציה, אתה מספק תמונה ופרומפט טקסטואלי וקוד כמו כך:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > הערה, זה נתמך רק על OpenAI

## טמפרטורה

טמפרטורה הוא פרמטר ששולט באקראיות של התוצר של מודל AI גנרטיבי. הטמפרטורה היא ערך בין 0 ל-1 כאשר 0 אומר שהתוצר דטרמיניסטי ו-1 אומר שהתוצר אקראי. ערך ברירת המחדל הוא 0.7.

בואו נסתכל על דוגמה איך טמפרטורה עובדת, על ידי הרצת פרומפט זה פעמיים:

> פרומפט: "ארנב על סוס, מחזיק סוכרייה על מקל, על אחו ערפילי בו צומחים נרקיסים"

עכשיו בואו נריץ את אותו הפרומפט רק כדי לראות שלא נקבל את אותה תמונה פעמיים:

כפי שאתה יכול לראות, התמונות דומות, אבל לא זהות. בואו ננסה לשנות את ערך הטמפרטורה ל-0.1 ונראה מה קורה:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### שינוי הטמפרטורה

אז בואו ננסה להפוך את התגובה ליותר דטרמיניסטית. אנחנו יכולים לראות מהשתי התמונות שיצרנו שבדמות הראשונה יש ארנב ובדמות השנייה יש סוס, כך שהתמונות משתנות מאוד.

לכן בואו נשנה את הקוד שלנו ונגדיר את הטמפרטורה ל-0, כך:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

עכשיו כשאתה מריץ את הקוד הזה, אתה מקבל את שתי התמונות האלה:

כאן אתה יכול לראות בבירור איך התמונות דומות יותר זו לזו.

## איך להגדיר גבולות לאפליקציה שלך עם מטה-פרומפטים

עם הדמו שלנו, אנחנו כבר יכולים ליצור תמונות עבור הלקוחות שלנו. עם זאת, אנחנו צריכים ליצור כמה גבולות לאפליקציה שלנו.

לדוגמה, אנחנו לא רוצים ליצור תמונות שאינן בטוחות לעבודה, או שאינן מתאימות לילדים.

אנחנו יכולים לעשות זאת עם _מטה-פרומפטים_. מטה-פרומפטים הם פרומפטים טקסטואליים שמשמשים לשלוט בתוצר של מודל AI גנרטיבי. לדוגמה, אנחנו יכולים להשתמש במטה-פרומפטים כדי לשלוט בתוצר, ולוודא שהתמונות שנוצרות בטוחות לעבודה, או מתאימות לילדים.

### איך זה עובד?

עכשיו, איך מטה פרומפטים עובדים?

מטה פרומפטים הם פרומפטים טקסטואליים שמשמשים לשלוט בתוצר של מודל AI גנרטיבי, הם ממוקמים לפני הפרומפט הטקסטואלי, ומשמשים לשלוט בתוצר של המודל ומוטמעים באפליקציות כדי לשלוט בתוצר של המודל. מקיפים את קלט הפרומפט ואת קלט המטה פרומפט בפרומפט טקסטואלי אחד.

דוגמה אחת למטה פרומפט תהיה הבאה:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

עכשיו, בואו נראה איך אנחנו יכולים להשתמש במטה פרומפטים בדמו שלנו.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt =f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"{meta_prompt}
Create an image of a bunny on a horse, holding a lollipop"

# TODO add request to generate image
```

מהפרומפט לעיל, אתה יכול לראות איך כל התמונות שנוצרות לוקחות בחשבון את המטה פרומפט.

## משימה - בואו נאפשר לתלמידים

הצגנו את Edu4All בתחילת השיעור הזה. עכשיו זה הזמן לאפשר לתלמידים ליצור תמונות להערכות שלהם.

התלמידים ייצרו תמונות להערכות שלהם המכילות אנדרטאות, בדיוק אילו אנדרטאות זה תלוי בתלמידים. התלמידים מתבקשים להשתמש ביצירתיות שלהם במשימה זו כדי למקם את האנדרטאות בהקשרים שונים.

## פתרון

הנה פתרון אפשרי אחד:

```python
import openai
import os
import requests
from PIL import Image
import dotenv

# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
openai.api_base = "<replace with endpoint>"
openai.api_key = "<replace with api key>"

# Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
openai.api_version = '2023-06-01-preview'
openai.api_type = 'azure'

disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}"""

prompt = f"""{metaprompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
""""

try:
    # Create an image by using the image generation API
    generation_response = openai.Image.create(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response["data"][0]["url"]  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.InvalidRequestError as err:
    print(err)
```

## עבודה נהדרת! המשך ללמוד

לאחר השלמת שיעור זה, בדוק את [אוסף הלמידה של AI גנרטיבי](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) כדי להמשיך לשפר את הידע שלך ב-AI גנרטיבי!

המשך לשיעור 10 שבו נסתכל איך [לבנות אפליקציות AI עם קוד נמוך](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. אנו לא נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות מהשימוש בתרגום זה.