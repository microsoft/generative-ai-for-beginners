<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:16:48+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "he"
}
-->
# בניית יישומי יצירת תמונות

יש יותר ב-LLMs מאשר יצירת טקסט. ניתן גם ליצור תמונות מתיאורים טקסטואליים. תמונות יכולות להיות שימושיות במגוון תחומים כמו מדטק, אדריכלות, תיירות, פיתוח משחקים ועוד. בפרק זה נבחן את שני המודלים הפופולריים ביותר ליצירת תמונות, DALL-E ו-Midjourney.

## מבוא

בשיעור זה נסקור:

- יצירת תמונות ולמה היא שימושית.
- DALL-E ו-Midjourney, מה הם וכיצד הם עובדים.
- כיצד לבנות אפליקציית יצירת תמונות.

## מטרות למידה

לאחר השלמת השיעור, תוכלו:

- לבנות אפליקציית יצירת תמונות.
- להגדיר גבולות לאפליקציה שלכם עם מטה פרומפטים.
- לעבוד עם DALL-E ו-Midjourney.

## למה לבנות אפליקציית יצירת תמונות?

אפליקציות יצירת תמונות הן דרך מצוינת לחקור את יכולות ה-AI הגנרטיבי. ניתן להשתמש בהן לדוגמה:

- **עריכת תמונות וסינתזה**. תוכלו ליצור תמונות למגוון שימושים, כמו עריכת תמונות וסינתזה של תמונות.

- **החלה על מגוון תעשיות**. ניתן גם להשתמש בהן ליצירת תמונות עבור מגוון תעשיות כמו מדטק, תיירות, פיתוח משחקים ועוד.

## תרחיש: Edu4All

כחלק מהשיעור הזה, נמשיך לעבוד עם הסטארטאפ שלנו, Edu4All. התלמידים ייצרו תמונות להערכות שלהם, בדיוק אילו תמונות תלוי בתלמידים, אך הם יכולים להיות איורים לסיפור שלהם או יצירת דמות חדשה לסיפור שלהם או לעזור להם להמחיש את הרעיונות והקונספטים שלהם.

לדוגמה, הנה מה שתלמידי Edu4All יכולים ליצור אם הם עובדים בכיתה על אנדרטאות:

באמצעות פרומפט כמו

> "כלב ליד מגדל אייפל באור השמש של הבוקר המוקדם"

## מה זה DALL-E ו-Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) ו-[Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) הם שניים מהמודלים הפופולריים ביותר ליצירת תמונות, המאפשרים להשתמש בפרומפטים כדי ליצור תמונות.

### DALL-E

נתחיל עם DALL-E, שהוא מודל AI גנרטיבי שיוצר תמונות מתיאורים טקסטואליים.

- **CLIP**, הוא מודל שיוצר אמבדינגים, שהם ייצוגים מספריים של נתונים, מתמונות וטקסט.

- **תשומת לב מפוזרת**, הוא מודל שיוצר תמונות מאמבדינגים. DALL-E מאומן על מאגר נתונים של תמונות וטקסט וניתן להשתמש בו ליצירת תמונות מתיאורים טקסטואליים. לדוגמה, ניתן להשתמש ב-DALL-E ליצירת תמונות של חתול בכובע, או כלב עם מוהוק.

### Midjourney

Midjourney עובד בצורה דומה ל-DALL-E, הוא יוצר תמונות מפרומפטים טקסטואליים. Midjourney, ניתן גם להשתמש בו ליצירת תמונות באמצעות פרומפטים כמו "חתול בכובע", או "כלב עם מוהוק".

## כיצד DALL-E ו-Midjourney עובדים

קודם כל, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E הוא מודל AI גנרטיבי המבוסס על ארכיטקטורת טרנספורמר עם _טרנספורמר אוטורגרסיבי_.

_טרנספורמר אוטורגרסיבי_ מגדיר כיצד מודל יוצר תמונות מתיאורים טקסטואליים, הוא יוצר פיקסל אחד בכל פעם, ולאחר מכן משתמש בפיקסלים שנוצרו כדי ליצור את הפיקסל הבא. עובר דרך שכבות רבות ברשת נוירונים, עד שהתמונה מושלמת.

בתהליך זה, DALL-E, שולט בתכונות, אובייקטים, מאפיינים ועוד בתמונה שהוא יוצר. עם זאת, ל-DALL-E 2 ו-3 יש יותר שליטה על התמונה שנוצרת.

## בניית אפליקציית יצירת תמונות ראשונה

אז מה צריך כדי לבנות אפליקציית יצירת תמונות? תצטרכו את הספריות הבאות:

- **python-dotenv**, מומלץ מאוד להשתמש בספרייה זו כדי לשמור את הסודות שלכם בקובץ _.env_ רחוק מהקוד.
- **openai**, זו הספרייה שתשתמשו בה כדי לתקשר עם ה-API של OpenAI.
- **pillow**, לעבודה עם תמונות בפייתון.
- **requests**, כדי לעזור לכם לבצע בקשות HTTP.

1. צרו קובץ _.env_ עם התוכן הבא:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   מצאו את המידע הזה בפורטל Azure עבור המשאב שלכם בחלק "Keys and Endpoint".

1. אספו את הספריות הנ"ל בקובץ שנקרא _requirements.txt_ כך:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. לאחר מכן, צרו סביבה וירטואלית והתקינו את הספריות:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   עבור Windows, השתמשו בפקודות הבאות כדי ליצור ולהפעיל את הסביבה הווירטואלית שלכם:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. הוסיפו את הקוד הבא בקובץ שנקרא _app.py_:

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

בואו נסביר את הקוד הזה:

- קודם כל, אנו מייבאים את הספריות שאנחנו צריכים, כולל ספריית OpenAI, ספריית dotenv, ספריית requests, וספריית Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- לאחר מכן, אנו טוענים את משתני הסביבה מקובץ ה-_.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- לאחר מכן, אנו מגדירים את נקודת הקצה, המפתח עבור ה-API של OpenAI, הגרסה והסוג.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- לאחר מכן, אנו יוצרים את התמונה:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  הקוד הנ"ל מגיב עם אובייקט JSON שמכיל את ה-URL של התמונה שנוצרה. אנו יכולים להשתמש ב-URL כדי להוריד את התמונה ולשמור אותה לקובץ.

- לבסוף, אנו פותחים את התמונה ומשתמשים בצופה התמונה הסטנדרטי כדי להציג אותה:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### פרטים נוספים על יצירת התמונה

בואו נבחן את הקוד שיוצר את התמונה בפירוט נוסף:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, הוא הפרומפט הטקסטואלי שמשמש ליצירת התמונה. במקרה זה, אנו משתמשים בפרומפט "ארנב על סוס, מחזיק סוכרייה, באחו מעורפל שבו צומחים נרקיסים".
- **size**, הוא גודל התמונה שנוצרת. במקרה זה, אנו יוצרים תמונה בגודל 1024x1024 פיקסלים.
- **n**, הוא מספר התמונות שנוצרות. במקרה זה, אנו יוצרים שתי תמונות.
- **temperature**, הוא פרמטר ששולט באקראיות של התוצאה של מודל AI גנרטיבי. הטמפרטורה היא ערך בין 0 ל-1 שבו 0 אומר שהתוצאה דטרמיניסטית ו-1 אומר שהתוצאה אקראית. ערך ברירת המחדל הוא 0.7.

יש עוד דברים שאפשר לעשות עם תמונות שנכסה בחלק הבא.

## יכולות נוספות של יצירת תמונות

ראיתם עד כה כיצד הצלחנו ליצור תמונה באמצעות כמה שורות קוד בפייתון. עם זאת, יש עוד דברים שאפשר לעשות עם תמונות.

ניתן גם לבצע את הדברים הבאים:

- **לבצע עריכות**. על ידי מתן תמונה קיימת מסכה ופרומפט, תוכלו לשנות תמונה. לדוגמה, תוכלו להוסיף משהו לחלק מהתמונה. דמיינו את תמונת הארנב שלנו, תוכלו להוסיף כובע לארנב. כיצד תעשו זאת הוא על ידי מתן התמונה, מסכה (זיהוי החלק לשינוי) ופרומפט טקסטואלי כדי לומר מה יש לעשות.

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

  התמונה הבסיסית תכיל רק את הארנב אך התמונה הסופית תכיל את הכובע על הארנב.

- **ליצור וריאציות**. הרעיון הוא לקחת תמונה קיימת ולבקש שייוצרו וריאציות. כדי ליצור וריאציה, תספקו תמונה ופרומפט טקסטואלי וקוד כך:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > שימו לב, זה נתמך רק ב-OpenAI

## טמפרטורה

טמפרטורה היא פרמטר ששולט באקראיות של התוצאה של מודל AI גנרטיבי. הטמפרטורה היא ערך בין 0 ל-1 שבו 0 אומר שהתוצאה דטרמיניסטית ו-1 אומר שהתוצאה אקראית. ערך ברירת המחדל הוא 0.7.

בואו נבחן דוגמה כיצד הטמפרטורה עובדת, על ידי הרצת פרומפט זה פעמיים:

> פרומפט: "ארנב על סוס, מחזיק סוכרייה, באחו מעורפל שבו צומחים נרקיסים"

עכשיו נריץ את אותו פרומפט רק כדי לראות שלא נקבל את אותה תמונה פעמיים:

כפי שאתם יכולים לראות, התמונות דומות, אך לא זהות. בואו ננסה לשנות את ערך הטמפרטורה ל-0.1 ולראות מה קורה:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### שינוי הטמפרטורה

אז בואו ננסה להפוך את התגובה לדטרמיניסטית יותר. יכולנו להבחין מהשתי התמונות שיצרנו שבאחת מהן יש ארנב ובשנייה יש סוס, כך שהתמונות שונות מאוד.

לכן בואו נשנה את הקוד שלנו ונגדיר את הטמפרטורה ל-0, כך:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

עכשיו כשאתם מריצים את הקוד הזה, תקבלו את שתי התמונות הללו:

כאן אתם יכולים לראות בבירור כיצד התמונות דומות יותר זו לזו.

## כיצד להגדיר גבולות לאפליקציה שלכם עם מטה פרומפטים

עם הדמו שלנו, אנחנו כבר יכולים ליצור תמונות עבור הלקוחות שלנו. עם זאת, אנחנו צריכים ליצור כמה גבולות לאפליקציה שלנו.

לדוגמה, אנחנו לא רוצים ליצור תמונות שאינן בטוחות לעבודה, או שאינן מתאימות לילדים.

אנחנו יכולים לעשות זאת עם _מטה פרומפטים_. מטה פרומפטים הם פרומפטים טקסטואליים שמשמשים לשלוט בתוצאה של מודל AI גנרטיבי. לדוגמה, אנחנו יכולים להשתמש במטה פרומפטים כדי לשלוט בתוצאה, ולוודא שהתמונות שנוצרות הן בטוחות לעבודה, או מתאימות לילדים.

### כיצד זה עובד?

עכשיו, איך מטה פרומפטים עובדים?

מטה פרומפטים הם פרומפטים טקסטואליים שמשמשים לשלוט בתוצאה של מודל AI גנרטיבי, הם ממוקמים לפני הפרומפט הטקסטואלי, ומשמשים לשלוט בתוצאה של המודל ומוטמעים באפליקציות כדי לשלוט בתוצאה של המודל. עוטפים את הקלט של הפרומפט ואת הקלט של המטה פרומפט בפרומפט טקסטואלי אחד.

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

מהפרומפט הנ"ל, אתם יכולים לראות כיצד כל התמונות שנוצרות מתחשבות במטה פרומפט.

## משימה - בואו נאפשר לתלמידים

הצגנו את Edu4All בתחילת השיעור הזה. עכשיו זה הזמן לאפשר לתלמידים ליצור תמונות להערכות שלהם.

התלמידים ייצרו תמונות להערכות שלהם הכוללות אנדרטאות, בדיוק אילו אנדרטאות תלוי בתלמידים. התלמידים מתבקשים להשתמש ביצירתיות שלהם במשימה זו כדי למקם את האנדרטאות בהקשרים שונים.

## פתרון

הנה פתרון אפשרי:

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

## עבודה נהדרת! המשיכו ללמוד

לאחר השלמת השיעור, בדקו את [אוסף הלמידה של AI גנרטיבי](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) כדי להמשיך לשפר את הידע שלכם ב-AI גנרטיבי!

עברו לשיעור 10 שבו נבחן כיצד [לבנות אפליקציות AI עם קוד נמוך](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). בעוד שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. אנו לא אחראים על אי הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.