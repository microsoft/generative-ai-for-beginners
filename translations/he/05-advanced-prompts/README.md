<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:35:44+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "he"
}
-->

> "ליצור קוד עבור API ווב בפייתון"
הרצת הפקודה שוב נותנת לנו את התוצאה הבאה:

```python
#import necessary libraries
import flask
from flask import request, jsonify

#create a Flask app
app = flask.Flask(__name__)

#create a route for the API
@app.route('/api', methods=['GET'])
def api_call():
    #get the data from the request
    data = request.get_json()

    #process the data
    result = process_data(data)

    #return the result
    return jsonify(result)

#define the process_data function
def process_data(data):
    #do something with the data
    result = data + 1

    #return the result
    return result

#run the app
if __name__ == '__main__':
    app.run()

```

יש רק הבדל קטן בין שתי התוצאות האלה. הפעם נעשה את ההפך, נגדיר את ה-temperature ל-0.9:

```python
# Import necessary libraries
import flask
from flask import request, jsonify

# Create a Flask app
app = flask.Flask(__name__)

# Create a route for the API
@app.route('/api', methods=['GET'])
def api_call():
    # Get the data from the request
    data = request.args

    # Process the data
    result = process_data(data)

    # Return the result
    return jsonify(result)

# Function to process the data
def process_data(data):
    # Do something with the data
    result = data + 1

    # Return the result
    return result

# Run the app
if __name__ == '__main__':
    app.run()

```

והניסיון השני עם ערך ה-temperature של 0.9:

```python
import flask
from flask import request, jsonify

# create the Flask app
app = flask.Flask(__name__)
app.config['DEBUG'] = True

# create some test data
books = [
    {'id': 0, 'title': 'A Fire Upon The Deep', 'author': 'Vernor Vinge', 'first_sentence': 'The coldsleep itself was dreamless.', 'year_published': '1992'},
    {'id': 1, 'title': 'The Ones Who Walk Away From Omelas', 'author': 'Ursula K. Le Guin', 'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.', 'published': '1973'},
    {'id': 2, 'title': 'Dhalgren', 'author': 'Samuel R. Delany', 'first_sentence': 'to wound the autumnal city.', 'published': '1975'}
]

# create an endpoint
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to our book API!</h1>'''

@app.route('/api/v1/resources/books

```

כפי שאתם רואים, התוצאות יכולות להיות מגוונות מאוד.

> [!NOTE] ישנם פרמטרים נוספים שניתן לשנות כדי לגוון את התוצאה, כמו top-k, top-p, repetition penalty, length penalty ו-diversity penalty, אך אלה מחוץ לתחום הקורס הזה.

## שיטות עבודה מומלצות

ישנן שיטות רבות שניתן ליישם כדי לנסות לקבל את מה שאתם רוצים. עם הזמן, ככל שתשתמשו ב-prompting יותר, תמצאו את הסגנון האישי שלכם.

בנוסף לטכניקות שכבר סקרנו, יש כמה שיטות עבודה מומלצות שכדאי לקחת בחשבון כשמפעילים LLM.

הנה כמה שיטות עבודה מומלצות שכדאי לזכור:

- **ציינו הקשר**. ההקשר חשוב, ככל שתוכלו לציין יותר פרטים כמו תחום, נושא וכו', כך התוצאה תהיה טובה יותר.
- הגבילו את הפלט. אם אתם רוצים מספר פריטים מסוים או אורך מסוים, ציינו זאת.
- **ציינו גם מה וגם איך**. זכרו לציין גם מה אתם רוצים וגם איך אתם רוצים את זה, למשל "צור API ב-Python עם Flask עם מסלולים products ו-customers, חלק את הקוד ל-3 קבצים".
- **השתמשו בתבניות**. לעיתים תרצו להעשיר את ה-prompts שלכם עם נתונים מהחברה שלכם. השתמשו בתבניות לכך. לתבניות יכולים להיות משתנים שתחליפו בנתונים אמיתיים.
- **איות נכון**. LLMs עשויים לספק תשובה נכונה, אבל אם תכתבו באיות תקין, תקבלו תשובה טובה יותר.

## מטלה

הנה קוד ב-Python שמראה איך לבנות API פשוט באמצעות Flask:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()
```

השתמשו בעוזר AI כמו GitHub Copilot או ChatGPT ויישמו את טכניקת ה-"self-refine" כדי לשפר את הקוד.

## פתרון

אנא נסו לפתור את המטלה על ידי הוספת prompts מתאימים לקוד.

> [!TIP]
> ניסחו prompt שיבקש שיפור, מומלץ להגביל את מספר השיפורים. אפשר גם לבקש שיפור בכיוון מסוים, למשל ארכיטקטורה, ביצועים, אבטחה וכו'.

[פתרון](../../../05-advanced-prompts/python/aoai-solution.py)

## בדיקת ידע

למה כדאי להשתמש ב-chain-of-thought prompting? הציגו תשובה נכונה אחת ו-2 תשובות שגויות.

1. ללמד את ה-LLM איך לפתור בעיה.
1. ב, ללמד את ה-LLM למצוא שגיאות בקוד.
1. ג, להנחות את ה-LLM להציע פתרונות שונים.

תשובה: 1, כי chain-of-thought עוסקת בהדגמת תהליך פתרון הבעיה ל-LLM על ידי מתן סדרת שלבים, בעיות דומות ואופן הפתרון שלהן.

## 🚀 אתגר

רק עכשיו השתמשתם בטכניקת ה-self-refine במטלה. קחו כל תוכנית שבניתם וחשבו אילו שיפורים הייתם רוצים להחיל עליה. עכשיו השתמשו בטכניקת ה-self-refine כדי ליישם את השינויים שהצעתם. מה חשבתם על התוצאה, טובה יותר או גרועה יותר?

## עבודה מצוינת! המשיכו ללמוד

לאחר שסיימתם את השיעור הזה, בדקו את [אוסף הלמידה של Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) שלנו כדי להמשיך לשפר את הידע שלכם ב-Generative AI!

המשיכו לשיעור 6 שבו ניישם את הידע שלנו ב-Prompt Engineering על ידי [בניית אפליקציות ליצירת טקסט](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.