<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a7fd0f95f9eb673b79da47c0814f4d4",
  "translation_date": "2025-07-09T13:28:58+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "he"
}
-->
# בניית אפליקציות ליצירת תמונות

[![בניית אפליקציות ליצירת תמונות](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.he.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

למודלים גדולים של שפה (LLMs) יש יותר מיצירת טקסט בלבד. אפשר גם ליצור תמונות מתיאורי טקסט. השימוש בתמונות כמדיום יכול להיות מאוד שימושי בתחומים רבים כמו מדטק, אדריכלות, תיירות, פיתוח משחקים ועוד. בפרק זה נבחן את שני המודלים הפופולריים ביותר ליצירת תמונות, DALL-E ו-Midjourney.

## מבוא

בשיעור זה נלמד על:

- יצירת תמונות ולמה זה שימושי.
- DALL-E ו-Midjourney – מה הם ואיך הם פועלים.
- איך לבנות אפליקציה ליצירת תמונות.

## מטרות הלמידה

בסיום השיעור תוכל:

- לבנות אפליקציה ליצירת תמונות.
- להגדיר גבולות לאפליקציה שלך באמצעות מטה-פרומפטים.
- לעבוד עם DALL-E ו-Midjourney.

## למה לבנות אפליקציה ליצירת תמונות?

אפליקציות ליצירת תמונות הן דרך מצוינת לחקור את יכולות ה-AI הגנרטיבי. אפשר להשתמש בהן, למשל, ל:

- **עריכה וסינתזה של תמונות**. ניתן ליצור תמונות למגוון שימושים, כמו עריכה וסינתזה של תמונות.

- **שימוש במגוון תעשיות**. אפשר גם ליצור תמונות עבור תעשיות שונות כמו מדטק, תיירות, פיתוח משחקים ועוד.

## תרחיש: Edu4All

כחלק מהשיעור נמשיך לעבוד עם הסטארטאפ שלנו, Edu4All. התלמידים ייצרו תמונות עבור המטלות שלהם, איזה תמונות בדיוק – זה תלוי בהם, אבל זה יכול להיות איורים לסיפור האגדות שלהם, יצירת דמות חדשה לסיפור או עזרה בהמחשת רעיונות ומושגים.

כך לדוגמה, תלמידי Edu4All יכולים ליצור תמונות אם הם עובדים בכיתה על אנדרטאות:

![סטארטאפ Edu4All, שיעור על אנדרטאות, מגדל אייפל](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.he.png)

עם פרומפט כמו

> "כלב ליד מגדל אייפל בשמש של בוקר מוקדם"

## מה זה DALL-E ו-Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) ו-[Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) הם שניים מהמודלים הפופולריים ביותר ליצירת תמונות, שמאפשרים להשתמש בפרומפטים כדי ליצור תמונות.

### DALL-E

נתחיל עם DALL-E, מודל AI גנרטיבי שיוצר תמונות מתיאורי טקסט.

> [DALL-E הוא שילוב של שני מודלים, CLIP ו-diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** הוא מודל שיוצר ייצוגים מספריים (embeddings) של נתונים, מתמונות וטקסט.

- **Diffused attention** הוא מודל שיוצר תמונות מתוך ה-embeddings. DALL-E מאומן על מאגר נתונים של תמונות וטקסט ויכול ליצור תמונות מתיאורי טקסט. לדוגמה, DALL-E יכול ליצור תמונות של חתול עם כובע, או כלב עם מוהוק.

### Midjourney

Midjourney פועל בדומה ל-DALL-E, הוא יוצר תמונות מפרומפטים טקסטואליים. גם Midjourney יכול ליצור תמונות עם פרומפטים כמו "חתול עם כובע" או "כלב עם מוהוק".

![תמונה שנוצרה על ידי Midjourney, יונה מכנית](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)  
_קרדיט לתמונה: ויקיפדיה, תמונה שנוצרה על ידי Midjourney_

## איך DALL-E ו-Midjourney פועלים

נתחיל עם [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E הוא מודל AI גנרטיבי מבוסס ארכיטקטורת טרנספורמר עם _טרנספורמר אוטורגרסיבי_.

טרנספורמר אוטורגרסיבי מגדיר איך המודל יוצר תמונות מתיאורי טקסט, הוא מייצר פיקסל אחד בכל פעם, ומשתמש בפיקסלים שנוצרו כדי לייצר את הפיקסל הבא. התהליך עובר דרך שכבות רבות ברשת נוירונים, עד שהתמונה שלמה.

בתהליך זה, DALL-E שולט בתכונות, עצמים, מאפיינים ועוד בתמונה שהוא יוצר. עם זאת, ב-DALL-E 2 ו-3 יש שליטה רבה יותר על התמונה שנוצרת.

## בניית אפליקציית יצירת תמונות ראשונה

אז מה צריך כדי לבנות אפליקציה ליצירת תמונות? תזדקק לספריות הבאות:

- **python-dotenv** – מומלץ מאוד להשתמש בספריה זו כדי לשמור סודות בקובץ _.env_ נפרד מהקוד.
- **openai** – ספריה שתשמש אותך לתקשורת עם ה-API של OpenAI.
- **pillow** – לעבודה עם תמונות בפייתון.
- **requests** – לעזרה בביצוע בקשות HTTP.

1. צור קובץ _.env_ עם התוכן הבא:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   מצא את המידע הזה בפורטל Azure עבור המשאב שלך תחת "Keys and Endpoint".

1. אסוף את הספריות הנ"ל בקובץ בשם _requirements.txt_ כך:

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

   עבור Windows, השתמש בפקודות הבאות ליצירה והפעלה של הסביבה הווירטואלית:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. הוסף את הקוד הבא בקובץ בשם _app.py_:

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

נסביר את הקוד:

- תחילה, מייבאים את הספריות הדרושות, כולל ספריית OpenAI, dotenv, requests ו-Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- לאחר מכן, טוענים את משתני הסביבה מקובץ _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- לאחר מכן, מגדירים את ה-endpoint, המפתח ל-API של OpenAI, הגרסה והסוג.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- לאחר מכן, מייצרים את התמונה:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  הקוד לעיל מחזיר אובייקט JSON שמכיל את כתובת ה-URL של התמונה שנוצרה. אפשר להשתמש בכתובת זו כדי להוריד את התמונה ולשמור אותה לקובץ.

- לבסוף, פותחים את התמונה ומשתמשים בצופה תמונות סטנדרטי כדי להציג אותה:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### פרטים נוספים על יצירת התמונה

נבחן את הקוד שיוצר את התמונה ביתר פירוט:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt** הוא פרומפט הטקסט שמשמש ליצירת התמונה. במקרה זה, הפרומפט הוא "ארנב על סוס, מחזיק סוכרייה על מקל, בערבת ערפל שבה צומחים נרקיסים".
- **size** הוא גודל התמונה שנוצרת. כאן, התמונה היא בגודל 1024x1024 פיקסלים.
- **n** הוא מספר התמונות שנוצרות. כאן, נוצרות שתי תמונות.
- **temperature** הוא פרמטר ששולט ברנדומליות של הפלט של מודל AI גנרטיבי. הטמפרטורה היא ערך בין 0 ל-1, כאשר 0 אומר שהפלט דטרמיניסטי ו-1 אומר שהפלט אקראי. הערך ברירת המחדל הוא 0.7.

יש עוד דברים שאפשר לעשות עם תמונות שנכסה בחלק הבא.

## יכולות נוספות ביצירת תמונות

כבר ראית איך הצלחנו ליצור תמונה בכמה שורות קוד בפייתון. עם זאת, יש עוד דברים שאפשר לעשות עם תמונות.

אפשר גם:

- **לבצע עריכות**. על ידי מתן תמונה קיימת, מסכה ופרומפט, אפשר לשנות תמונה. לדוגמה, אפשר להוסיף משהו לחלק מסוים בתמונה. נניח בתמונת הארנב שלנו, אפשר להוסיף לו כובע. איך עושים זאת? מספקים את התמונה, מסכה (שמציינת את האזור לשינוי) ופרומפט טקסטואלי שמסביר מה יש לעשות.

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

  התמונה הבסיסית תכיל רק את הארנב, אבל התמונה הסופית תכלול את הכובע על הארנב.

- **ליצור וריאציות**. הרעיון הוא לקחת תמונה קיימת ולבקש ליצור וריאציות שלה. כדי ליצור וריאציה, מספקים תמונה ופרומפט טקסטואלי וקוד כזה:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > שים לב, זה נתמך רק ב-OpenAI

## טמפרטורה

טמפרטורה היא פרמטר ששולט ברנדומליות של הפלט של מודל AI גנרטיבי. הטמפרטורה היא ערך בין 0 ל-1, כאשר 0 אומר שהפלט דטרמיניסטי ו-1 אומר שהפלט אקראי. הערך ברירת המחדל הוא 0.7.

נראה דוגמה לאיך הטמפרטורה פועלת, על ידי הרצת הפרומפט הזה פעמיים:

> פרומפט: "ארנב על סוס, מחזיק סוכרייה על מקל, בערבת ערפל שבה צומחים נרקיסים"

![ארנב על סוס מחזיק סוכרייה על מקל, גרסה 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.he.png)

עכשיו נריץ את אותו פרומפט שוב כדי לראות שלא נקבל את אותה תמונה פעמיים:

![תמונה שנוצרה של ארנב על סוס](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.he.png)

כפי שניתן לראות, התמונות דומות אך לא זהות. ננסה לשנות את ערך הטמפרטורה ל-0.1 ונראה מה קורה:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### שינוי הטמפרטורה

ננסה להפוך את התגובה ליותר דטרמיניסטית. מהתמונות שיצרנו ראינו שבתמונה הראשונה יש ארנב ובשנייה סוס, כלומר התמונות שונות מאוד.

לכן נשנה את הקוד ונגדיר את הטמפרטורה ל-0, כך:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

כעת כשמריצים את הקוד, מקבלים את שתי התמונות הבאות:

- ![טמפרטורה 0, גרסה 1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.he.png)
- ![טמפרטורה 0, גרסה 2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.he.png)

כאן רואים בבירור שהתמונות דומות זו לזו יותר.

## איך להגדיר גבולות לאפליקציה שלך עם מטה-פרומפטים

בדמו שלנו, כבר אפשר ליצור תמונות ללקוחות. עם זאת, צריך להגדיר גבולות לאפליקציה.

לדוגמה, לא נרצה ליצור תמונות שאינן מתאימות לעבודה או שאינן מתאימות לילדים.

אפשר לעשות זאת עם _מטה-פרומפטים_. מטה-פרומפטים הם פרומפטים טקסטואליים שמשמשים לשליטה על הפלט של מודל AI גנרטיבי. לדוגמה, אפשר להשתמש במטה-פרומפטים כדי לוודא שהתמונות שנוצרות בטוחות לעבודה או מתאימות לילדים.

### איך זה עובד?

איך מטה-פרומפטים פועלים?

מטה-פרומפטים הם פרומפטים טקסטואליים שממוקמים לפני פרומפט הטקסט, ומשמשים לשליטה על הפלט של המודל. הם משולבים באפליקציות כדי לשלוט על הפלט של המודל, על ידי שילוב פרומפט הקלט והמטה-פרומפט בפרומפט טקסטואלי אחד.

דוגמה למטה-פרומפט תהיה:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

עכשיו נראה איך אפשר להשתמש במטה-פרומפטים בדמו שלנו.

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

מהפרומפט שלמעלה אפשר לראות שכל התמונות שנוצרות מתחשבות במטה-פרומפט.

## משימה – נאפשר לתלמידים

הכרנו את Edu4All בתחילת השיעור. עכשיו הגיע הזמן לאפשר לתלמידים ליצור תמונות עבור המטלות שלהם.

התלמידים ייצרו תמונות למטלות הכוללות אנדרטאות, איזה אנדרטאות בדיוק – זה תלוי בהם. התלמידים מתבקשים להשתמש ביצירתיות שלהם במשימה זו כדי למקם את האנדרטאות בהקשרים שונים.

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

prompt = f"""{meta_prompt}
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

## עבודה מצוינת! המשך ללמוד

בסיום השיעור, בדוק את [אוסף הלמידה של Generative AI שלנו](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) כדי להמשיך להעמיק את הידע שלך ב-AI גנרטיבי!

עבור לשיעור 10 שבו נלמד איך [לבנות אפליקציות AI בקוד נמוך](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.