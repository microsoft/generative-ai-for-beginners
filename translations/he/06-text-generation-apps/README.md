<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-05-19T17:06:19+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "he"
}
-->
# בניית יישומים ליצירת טקסט

> _(לחץ על התמונה למעלה לצפייה בסרטון של שיעור זה)_

עד כה ראית דרך תוכנית הלימודים הזו שיש מושגים מרכזיים כמו הנחיות ואפילו תחום שלם שנקרא "הנדסת הנחיות". כלים רבים שאתה יכול לתקשר איתם כמו ChatGPT, Office 365, Microsoft Power Platform ועוד, תומכים בך בשימוש בהנחיות כדי להשיג משהו.

כדי להוסיף חוויה כזו ליישום, עליך להבין מושגים כמו הנחיות, השלמות ולבחור ספרייה לעבוד איתה. זה בדיוק מה שתלמד בפרק הזה.

## מבוא

בפרק זה, תלמד:

- על ספריית openai ועל המושגים המרכזיים שלה.
- לבנות יישום ליצירת טקסט באמצעות openai.
- להבין כיצד להשתמש במושגים כמו הנחיה, טמפרטורה וטוקנים כדי לבנות יישום ליצירת טקסט.

## מטרות לימוד

בסוף השיעור הזה, תוכל:

- להסביר מהו יישום ליצירת טקסט.
- לבנות יישום ליצירת טקסט באמצעות openai.
- להגדיר את היישום שלך לשימוש ביותר או פחות טוקנים וגם לשנות את הטמפרטורה, לתוצאה מגוונת.

## מהו יישום ליצירת טקסט?

בדרך כלל כשאתה בונה יישום יש לו סוג של ממשק כמו הבאים:

- מבוסס פקודה. יישומי קונסולה הם יישומים טיפוסיים שבהם אתה מקליד פקודה והיא מבצעת משימה. לדוגמה, `git` הוא יישום מבוסס פקודה.
- ממשק משתמש (UI). יש יישומים עם ממשקי משתמש גרפיים (GUIs) שבהם אתה לוחץ על כפתורים, מזין טקסט, בוחר אפשרויות ועוד.

### יישומי קונסולה ו-UI מוגבלים

השווה זאת ליישום מבוסס פקודה שבו אתה מקליד פקודה:

- **זה מוגבל**. אתה לא יכול פשוט להקליד כל פקודה, רק את אלה שהיישום תומך בהן.
- **ספציפי לשפה**. יש יישומים שתומכים בשפות רבות, אבל כברירת מחדל היישום בנוי לשפה ספציפית, גם אם אתה יכול להוסיף תמיכה בשפות נוספות.

### יתרונות יישומי יצירת טקסט

אז איך יישום ליצירת טקסט שונה?

ביישום ליצירת טקסט יש לך יותר גמישות, אתה לא מוגבל למערכת פקודות או לשפת קלט ספציפית. במקום זאת, אתה יכול להשתמש בשפה טבעית כדי לתקשר עם היישום. יתרון נוסף הוא שכשאתה כבר מתקשר עם מקור נתונים שאומן על קורפוס מידע רחב, בעוד שיישום מסורתי עשוי להיות מוגבל למה שיש בבסיס נתונים.

### מה אני יכול לבנות עם יישום ליצירת טקסט?

יש הרבה דברים שאתה יכול לבנות. לדוגמה:

- **צ'אטבוט**. צ'אטבוט שעונה על שאלות על נושאים, כמו החברה שלך ומוצריה יכול להיות התאמה טובה.
- **עוזר**. LLMs מצוינים בדברים כמו סיכום טקסט, קבלת תובנות מטקסט, יצירת טקסט כמו קורות חיים ועוד.
- **עוזר קוד**. בהתאם לדגם השפה שאתה משתמש בו, אתה יכול לבנות עוזר קוד שעוזר לך לכתוב קוד. לדוגמה, אתה יכול להשתמש במוצר כמו GitHub Copilot וכן ChatGPT כדי לעזור לך לכתוב קוד.

## איך אני יכול להתחיל?

ובכן, אתה צריך למצוא דרך להשתלב עם LLM שלרוב כוללת את שתי הגישות הבאות:

- שימוש ב-API. כאן אתה בונה בקשות אינטרנט עם ההנחיה שלך ומקבל טקסט שנוצר בחזרה.
- שימוש בספרייה. ספריות עוזרות לעטוף את קריאות ה-API ולהקל על השימוש בהן.

## ספריות/SDKs

יש כמה ספריות מוכרות לעבודה עם LLMs כמו:

- **openai**, הספרייה הזו מקלה על חיבור למודל שלך ושליחת הנחיות.

ואז יש ספריות שפועלות ברמה גבוהה יותר כמו:

- **Langchain**. Langchain ידועה ותומכת בפייתון.
- **Semantic Kernel**. Semantic Kernel היא ספרייה של Microsoft התומכת בשפות C#, Python ו-Java.

## יישום ראשון באמצעות openai

בוא נראה איך אנחנו יכולים לבנות את היישום הראשון שלנו, אילו ספריות אנחנו צריכים, כמה נדרש וכן הלאה.

### התקנת openai

יש הרבה ספריות שם לחיבור עם OpenAI או Azure OpenAI. ניתן להשתמש בשפות תכנות רבות כמו C#, Python, JavaScript, Java ועוד. בחרנו להשתמש בספריית `openai` Python, אז נשתמש ב-`pip` כדי להתקין אותה.

### יצירת משאב

אתה צריך לבצע את השלבים הבאים:

- צור חשבון ב-Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- קבל גישה ל-Azure OpenAI. עבור אל [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) ובקש גישה.

  > [!NOTE]
  > בזמן כתיבת השורות האלה, אתה צריך להגיש בקשה לגישה ל-Azure OpenAI.

- התקן Python <https://www.python.org/>
- צור משאב שירות Azure OpenAI. ראה את המדריך הזה כיצד [ליצור משאב](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### מצא את מפתח ה-API והנקודת קצה

בשלב זה, אתה צריך לומר לספריית `openai` שלך איזה מפתח API להשתמש. כדי למצוא את מפתח ה-API שלך, עבור לסעיף "Keys and Endpoint" של משאב Azure OpenAI שלך והעתק את הערך "Key 1".

עכשיו שיש לך את המידע הזה מועתק, בוא ננחה את הספריות להשתמש בו.

> [!NOTE]
> כדאי להפריד את מפתח ה-API שלך מהקוד. אתה יכול לעשות זאת באמצעות משתני סביבה.

### הגדרת תצורה של Azure

אם אתה משתמש ב-Azure OpenAI, הנה איך אתה מגדיר את התצורה:

במעלה אנחנו מגדירים את הדברים הבאים:

בקטע הקוד לעיל, אנו יוצרים אובייקט השלמה ומעבירים את המודל שאנחנו רוצים להשתמש בו ואת ההנחיה. ואז אנו מדפיסים את הטקסט שנוצר.

### השלמות צ'אט

עד כה, ראית איך השתמשנו ב-`Completion` to generate text. But there's another class called `ChatCompletion` שמתאים יותר לצ'אטבוטים. הנה דוגמה לשימוש בזה:

עוד על פונקציונליות זו בפרק הקרוב.

## תרגיל - יישום ליצירת טקסט הראשון שלך

עכשיו שלמדנו איך להגדיר ולהגדיר openai, הגיע הזמן לבנות את יישום ליצירת הטקסט הראשון שלך. כדי לבנות את היישום שלך, בצע את השלבים הבאים:

1. צור סביבה וירטואלית והתקן openai:

   > [!NOTE]
   > אם אתה משתמש ב-Windows הקלד `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` value.

1. צור קובץ _app.py_ ותן לו את הקוד הבא:

   > [!NOTE]
   > אם אתה משתמש ב-Azure OpenAI, אתה צריך להגדיר את `api_type` to `azure` and set the `api_key` למפתח Azure OpenAI שלך.

   אתה אמור לראות פלט כמו הבא:

## סוגים שונים של הנחיות, לדברים שונים

עכשיו ראית איך לייצר טקסט באמצעות הנחיה. יש לך אפילו תוכנית פועלת שאתה יכול לשנות ולהתאים כדי לייצר סוגים שונים של טקסט.

ניתן להשתמש בהנחיות לכל מיני משימות. לדוגמה:

- **יצירת סוג טקסט**. לדוגמה, אתה יכול לייצר שיר, שאלות לטריוויה וכו'.
- **חיפוש מידע**. אתה יכול להשתמש בהנחיות כדי לחפש מידע כמו הדוגמה הבאה 'מה המשמעות של CORS בפיתוח אתרים?'.
- **יצירת קוד**. אתה יכול להשתמש בהנחיות כדי לייצר קוד, לדוגמה פיתוח ביטוי רגולרי המשמש לאימות אימיילים או למה לא לייצר תוכנית שלמה, כמו יישום אינטרנט?

## מקרה שימוש מעשי יותר: מחולל מתכונים

דמיין שיש לך מרכיבים בבית ואתה רוצה לבשל משהו. בשביל זה, אתה צריך מתכון. דרך למצוא מתכונים היא להשתמש במנוע חיפוש או שאתה יכול להשתמש ב-LLM כדי לעשות זאת.

אתה יכול לכתוב הנחיה כמו כך:

> "הראה לי 5 מתכונים למנה עם המרכיבים הבאים: עוף, תפוחי אדמה וגזר. עבור כל מתכון, רשום את כל המרכיבים המשמשים"

בהתחשב בהנחיה לעיל, אתה עשוי לקבל תגובה דומה ל:

התוצאה הזו נהדרת, אני יודע מה לבשל. בשלב זה, מה שיכול להיות שיפורים מועילים הם:

- סינון מרכיבים שאני לא אוהב או אלרגי אליהם.
- יצירת רשימת קניות, במקרה שאין לי את כל המרכיבים בבית.

למקרים לעיל, בוא נוסיף הנחיה נוספת:

> "אנא הסר מתכונים עם שום מכיוון שאני אלרגי והחלף אותו במשהו אחר. בנוסף, אנא צור רשימת קניות למתכונים, בהתחשב בכך שכבר יש לי עוף, תפוחי אדמה וגזר בבית."

עכשיו יש לך תוצאה חדשה, כלומר:

אלה חמשת המתכונים שלך, ללא שום מוזכר ויש לך גם רשימת קניות בהתחשב במה שכבר יש לך בבית.

## תרגיל - בניית מחולל מתכונים

עכשיו ששיחקנו תרחיש, בוא נכתוב קוד שיתאים לתרחיש שהוצג. כדי לעשות זאת, בצע את השלבים הבאים:

1. השתמש בקובץ _app.py_ הקיים כנקודת התחלה
1. מצא את משתנה ה-`prompt` ושנה את הקוד שלו לבא:

   אם אתה מריץ את הקוד עכשיו, אתה אמור לראות פלט דומה ל:

   > NOTE, ה-LLM שלך אינו דטרמיניסטי, כך שאתה עשוי לקבל תוצאות שונות בכל פעם שאתה מריץ את התוכנית.

   נהדר, בוא נראה איך אנחנו יכולים לשפר דברים. כדי לשפר דברים, אנחנו רוצים לוודא שהקוד גמיש, כך שמרכיבים ומספר המתכונים יכולים להיות משופרים ומשתנים.

1. בוא נשנה את הקוד בדרך הבאה:

   לקיחת הקוד לבדיקה, יכולה להיראות כך:

### שיפור על ידי הוספת מסנן ורשימת קניות

יש לנו עכשיו יישום עובד שמסוגל לייצר מתכונים והוא גמיש מכיוון שהוא מסתמך על קלטים מהמשתמש, הן על מספר המתכונים וגם על המרכיבים המשמשים.

כדי לשפר אותו עוד יותר, אנחנו רוצים להוסיף את הדברים הבאים:

- **סינון מרכיבים**. אנחנו רוצים להיות מסוגלים לסנן מרכיבים שאנחנו לא אוהבים או אלרגיים אליהם. כדי להשיג שינוי זה, אנחנו יכולים לערוך את ההנחיה הקיימת שלנו ולהוסיף תנאי סינון לסופה כמו כך:

  מעל, אנחנו מוסיפים `{filter}` לסוף ההנחיה ואנחנו גם לוכדים את ערך המסנן מהמשתמש.

  דוגמה לקלט של הרצת התוכנית יכולה להיראות כך:

  כפי שאתה יכול לראות, כל מתכונים עם חלב סוננו החוצה. אבל, אם אתה רגיש ללקטוז, אתה עשוי לרצות לסנן גם מתכונים עם גבינה, כך שיש צורך להיות ברור.

- **יצירת רשימת קניות**. אנחנו רוצים ליצור רשימת קניות, בהתחשב במה שכבר יש לנו בבית.

  עבור פונקציונליות זו, אנחנו יכולים לנסות לפתור הכל בהנחיה אחת או שאנחנו יכולים לחלק אותה לשתי הנחיות. בוא ננסה את הגישה האחרונה. כאן אנחנו מציעים להוסיף הנחיה נוספת, אבל כדי שזה יעבוד, אנחנו צריכים להוסיף את התוצאה מההנחיה הראשונה כקונטקסט להנחיה השנייה.

  מצא את החלק בקוד שמדפיס את התוצאה מההנחיה הראשונה והוסף את הקוד הבא למטה:

  שים לב לדברים הבאים:

  1. אנחנו בונים הנחיה חדשה על ידי הוספת התוצאה מההנחיה הראשונה להנחיה החדשה:

  1. אנחנו מבצעים בקשה חדשה, אבל גם בהתחשב במספר הטוקנים שביקשנו בהנחיה הראשונה, אז הפעם אנחנו אומרים ש-`max_tokens` הוא 1200.

     לקיחת הקוד לסיבוב, אנחנו מגיעים עכשיו לפלט הבא:

## שפר את ההגדרה שלך

מה שיש לנו עד כה הוא קוד שעובד, אבל יש כמה שיפורים שאנחנו צריכים לעשות כדי לשפר דברים עוד יותר. כמה דברים שאנחנו צריכים לעשות הם:

- **הפרדת סודות מהקוד**, כמו מפתח ה-API. סודות לא שייכים לקוד וצריכים להיות מאוחסנים במיקום מאובטח. כדי להפריד סודות מהקוד, אנחנו יכולים להשתמש במשתני סביבה ובספריות כמו `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` קובץ עם התוכן הבא:

     > שים לב, עבור Azure, אתה צריך להגדיר את משתני הסביבה הבאים:

     בקוד, אתה תטען את משתני הסביבה כמו כך:

- **מילה על אורך הטוקנים**. אנחנו צריכים לשקול כמה טוקנים אנחנו צריכים כדי לייצר את הטקסט שאנחנו רוצים. טוקנים עולים כסף, אז אם אפשר, אנחנו צריכים לנסות להיות חסכוניים במספר הטוקנים שאנחנו משתמשים בהם. לדוגמה, האם אנחנו יכולים לנסח את ההנחיה כך שנוכל להשתמש בפחות טוקנים?

  כדי לשנות את הטוקנים המשמשים, אתה יכול להשתמש בפרמטר `max_tokens`. לדוגמה, אם אתה רוצה להשתמש ב-100 טוקנים, אתה תעשה:

- **ניסוי עם טמפרטורה**. טמפרטורה היא משהו שלא הזכרנו עד כה אבל הוא הקשר חשוב לאופן שבו התוכנית שלנו מתפקדת. ככל שערך הטמפרטורה גבוה יותר, כך הפלט יהיה אקראי יותר. לעומת זאת, ככל שערך הטמפרטורה נמוך יותר, כך הפלט יהיה צפוי יותר. שקול אם אתה רוצה גיוון בפלט שלך או לא.

  כדי לשנות את הטמפרטורה, אתה יכול להשתמש בפרמטר `temperature`. לדוגמה, אם אתה רוצה להשתמש בטמפרטורה של 0.5, אתה תעשה:

  > שים לב, ככל שקרוב יותר ל-1.0, כך הפלט יהיה מגוון יותר.

## משימה

עבור המשימה הזו, אתה יכול לבחור מה לבנות.

הנה כמה הצעות:

- שפר את יישום מחולל המתכונים כדי לשפר אותו עוד יותר. שחק עם ערכי הטמפרטורה, וההנחיות כדי לראות מה אתה יכול להמציא.
- בנה "חבר ללימודים". יישום זה צריך להיות מסוגל לענות על שאלות על נושא, לדוגמה פייתון, אתה יכול לקבל הנחיות כמו "מהו נושא מסוים בפייתון?", או שאתה יכול לקבל הנחיה שאומרת, הראה לי קוד עבור נושא מסוים וכו'.
- בוט היסטוריה, הפוך את ההיסטוריה לחיה, הנחה את הבוט לשחק דמות היסטורית מסוימת ושאל אותו שאלות על חייו וזמנו.

## פתרון

### חבר ללימודים

להלן הנחיה התחלתית, ראה איך אתה יכול להשתמש בה ולשפר אותה לפי רצונך.

### בוט היסטוריה

הנה כמה הנחיות שאתה יכול להשתמש בהן:

## בדיקת ידע

מה עושה מושג הטמפרטורה?

1. הוא שולט כמה אקראי הפלט.
1. הוא שולט כמה גדול התגובה.
1. הוא שולט כמה טוקנים משמשים.

## 🚀 אתגר

כשעובדים על המשימה, נסו לשנות את הטמפרטורה, נסו להגדיר אותה ל-0, 0.5 ו-1. זכרו ש-0 הוא הכי פחות מגוון ו-1 הוא הכי מגוון, איזה ערך עובד הכי טוב עבור היישום שלך?

## עבודה נהדרת! המשך את הלמידה שלך

לאחר השלמת השיעור הזה, בדוק את [אוסף הלמידה של AI גנרטיבי שלנו](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) כדי להמשיך להעמיק את הידע שלך ב-AI גנרטיבי!

עבור לשיעור 7 שבו נבחן כיצד [לבנות יישומי צ'אט](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי בני אדם. אנו לא אחראים לאי-הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.