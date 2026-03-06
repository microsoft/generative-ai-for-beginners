# בנייה עם דגמי משפחת Meta

## מבוא

בחלק זה יכוסו:

- חקר שני הדגמים המרכזיים ממשפחת Meta - Llama 3.1 ו-Llama 3.2
- הבנת מקרים ושימושים עבור כל דגם
- דוגמת קוד להדגמת התכונות הייחודיות של כל דגם

## משפחת דגמי Meta

בחלק זה נחקור 2 דגמים ממשפחת Meta או "ללמה העדר" - Llama 3.1 ו-Llama 3.2.

דגמים אלה מגיעים בגרסאות שונות וזמינים בשוק הדגמים של GitHub. להלן פרטים נוספים על שימוש בדגמי GitHub כדי [לאפיין עם דגמי AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

גרסאות דגם:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*הערה: Llama 3 זמין גם בדגמי GitHub אך לא ייכלל בחלק זה*

## Llama 3.1

עם 405 מיליארד פרמטרים, Llama 3.1 משתייך לקטגוריית ה-LLM בקוד פתוח.

הדגם הוא שדרוג לגרסה הקודמת Llama 3 ומציע:

- חלון הקשר גדול יותר - 128k טוקנים לעומת 8k טוקנים
- מספר טוקני פלט מקסימלי גדול יותר - 4096 לעומת 2048
- תמיכה רב-לשונית משופרת - בזכות העלייה במספר טוקני האימון

תכונות אלו מאפשרות ל-Llama 3.1 להתמודד עם מקרים מורכבים יותר בבניית יישומי GenAI, כולל:
- קריאה לפונקציות מקוריות - היכולת לקרוא לכלים ופונקציות חיצוניות מחוץ לזרימת העבודה של ה-LLM
- ביצועי RAG טובים יותר - בעקבות חלון ההקשר הגבוה יותר
- יצירת נתונים סינתטיים - היכולת ליצור נתונים יעילים למשימות כמו כוונון מדויק

### קריאה לפונקציות מקוריות

Llama 3.1 הותאם במיוחד להיות יעיל יותר בקריאות לפונקציות או כלים. כמו כן, יש לו שני כלים מובנים שהדגם יכול לזהות כי יש להשתמש בהם בהתאם לפרומפט מהמשתמש. כלים אלו הם:

- **Brave Search** - ניתן להשתמש לקבלת מידע מעודכן כמו מזג האוויר על ידי חיפוש באינטרנט
- **Wolfram Alpha** - לשימוש בחישובים מתמטיים מורכבים כך שאין צורך לכתוב פונקציות משלך.

ניתן גם ליצור כלים מותאמים אישית שה-LLM יכול לקרוא להם.

בדוגמת הקוד שלמטה:

- אנו מגדירים את הכלים הזמינים (brave_search, wolfram_alpha) בפרומפט המערכת.
- שולחים פרומפט משתמש השואל על מזג האוויר בעיר מסוימת.
- ה-LLM ישיב עם קריאת כלי ל-Brave Search שתיראה כך `<|python_tag|>brave_search.call(query="Stockholm weather")`

*הערה: דוגמה זו מבצעת רק את קריאת הכלי, כדי לקבל את התוצאות יש ליצור חשבון חינמי בדף ה-API של Brave ולהגדיר את הפונקציה עצמה.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


tool_prompt=f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha
Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="What is the weather in Stockholm?"),

]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## Llama 3.2

למרות שהוא LLM, מגבלה של Llama 3.1 היא חוסר מולטימודאליות. כלומר, חוסר היכולת לקבל קלט מסוגים שונים כמו תמונות כפרומפטים ולהחזיר תגובות. יכולת זו היא אחת התכונות המרכזיות של Llama 3.2. תכונות אלו כוללות גם:

- מולטימודאליות - היכולת להעריך גם פרומפטים טקסטואליים וגם תמונות
- וריאציות קטנות עד בינוניות (11B ו-90B) - המאפשרות אפשרויות פריסה גמישות,
- וריאציות של טקסט בלבד (1B ו-3B) - מאפשרות לפרוס את הדגם במכשירים שוליים/ניידים ומספקות השהייה נמוכה

התמיכה במולטימודאליות מהווה צעד גדול בעולם דגמי הקוד הפתוח. דוגמת הקוד שלמטה מקבלת גם תמונה וגם פרומפט טקסט בכדי לקבל ניתוח של התמונה מ-Llama 3.2 90B.

### תמיכה מולטימודאלית עם Llama 3.2

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "Llama-3.2-90B-Vision-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="sample.jpg",
                        image_format="jpg",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
```

## הלמידה לא נעצרת כאן, המשך את המסע

לאחר סיום חלק זה, עיין ב-[אוסף הלמידה ב-AI גנרטיבי](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) כדי להמשיך ולשדרג את הידע שלך ב-AI גנרטיבי!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**הצהרת אחריות**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). על אף שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפת המקור שלו הוא המקור המוסמך והמהימן. למידע קריטי מומלץ להשתמש בתרגום מקצועי של בן אדם. אנו לא נושאים באחריות לכל הבנה שגויה או פרשנות מוטעית הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->