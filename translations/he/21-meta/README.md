<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:33:05+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "he"
}
-->
# בנייה עם מודלים ממשפחת Meta

## מבוא

שיעור זה יעסוק ב:

- חקר שני המודלים העיקריים ממשפחת Meta - Llama 3.1 ו-Llama 3.2
- הבנת מקרי השימוש והתסריטים עבור כל מודל
- דוגמת קוד להדגמת התכונות הייחודיות של כל מודל

## משפחת המודלים של Meta

בשיעור זה, נחקור שני מודלים ממשפחת Meta או "עדר Llama" - Llama 3.1 ו-Llama 3.2

מודלים אלו מגיעים בגרסאות שונות וזמינים בשוק המודלים של GitHub. הנה פרטים נוספים על השימוש במודלים של GitHub ל[יצירת אב-טיפוס עם מודלים של AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

גרסאות מודל:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*הערה: Llama 3 זמין גם ב-GitHub Models אך לא יכוסה בשיעור זה*

## Llama 3.1

עם 405 מיליארד פרמטרים, Llama 3.1 משתייך לקטגוריית LLM בקוד פתוח.

המודל הוא שדרוג של הגרסה הקודמת Llama 3 על ידי הצעת:

- חלון הקשר גדול יותר - 128k טוקנים לעומת 8k טוקנים
- מספר טוקנים מקסימלי גדול יותר - 4096 לעומת 2048
- תמיכה רב-לשונית משופרת - בזכות הגדלת מספר הטוקנים באימון

תכונות אלו מאפשרות ל-Llama 3.1 להתמודד עם מקרי שימוש מורכבים יותר בבניית יישומי GenAI כולל:
- קריאה לפונקציות מקוריות - היכולת לקרוא לכלים ופונקציות חיצוניות מחוץ לזרימת העבודה של LLM
- ביצועי RAG משופרים - בזכות חלון ההקשר הגדול יותר
- יצירת נתונים סינתטיים - היכולת ליצור נתונים יעילים למשימות כגון כוונון עדין

### קריאה לפונקציות מקוריות

Llama 3.1 עבר כוונון עדין כדי להיות יעיל יותר בקריאה לפונקציות או כלים. יש לו גם שני כלים מובנים שהמודל יכול לזהות שיש להשתמש בהם בהתבסס על ההנחיה מהמשתמש. כלים אלו הם:

- **Brave Search** - ניתן להשתמש בו כדי לקבל מידע עדכני כמו מזג האוויר על ידי ביצוע חיפוש באינטרנט
- **Wolfram Alpha** - ניתן להשתמש בו לחישובים מתמטיים מורכבים יותר כך שאין צורך לכתוב פונקציות משלך.

ניתן גם ליצור כלים מותאמים אישית שה-LLM יכול לקרוא להם.

בדוגמת הקוד למטה:

- אנו מגדירים את הכלים הזמינים (brave_search, wolfram_alpha) בהנחיית המערכת.
- שולחים הנחיית משתמש ששואלת על מזג האוויר בעיר מסוימת.
- ה-LLM יגיב בקריאה לכלי Brave Search שתיראה כך `<|python_tag|>brave_search.call(query="Stockholm weather")`

*הערה: דוגמה זו רק מבצעת את הקריאה לכלי, אם תרצו לקבל את התוצאות, תצטרכו ליצור חשבון חינמי בדף ה-API של Brave ולהגדיר את הפונקציה עצמה*

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

למרות היותו LLM, אחת המגבלות של Llama 3.1 היא רב-מודליות. כלומר, היכולת להשתמש בסוגי קלט שונים כגון תמונות כהנחיות ולספק תגובות. יכולת זו היא אחת התכונות העיקריות של Llama 3.2. תכונות אלו כוללות גם:

- רב-מודליות - יש לו את היכולת להעריך הן טקסט והן הנחיות תמונה
- וריאציות בגודל קטן עד בינוני (11B ו-90B) - זה מספק אפשרויות פריסה גמישות,
- וריאציות טקסט בלבד (1B ו-3B) - זה מאפשר למודל להיות נפרס בקצה / מכשירים ניידים ומספק השהייה נמוכה

התמיכה הרב-מודלית מייצגת צעד גדול בעולם המודלים בקוד פתוח. דוגמת הקוד למטה לוקחת הן תמונה והן הנחיית טקסט כדי לקבל ניתוח של התמונה מ-Llama 3.2 90B.

### תמיכה רב-מודלית עם Llama 3.2

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

## הלמידה לא נעצרת כאן, המשיכו במסע

לאחר השלמת שיעור זה, בדקו את [אוסף הלמידה של AI גנרטיבי](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) שלנו כדי להמשיך לשפר את הידע שלכם ב-AI גנרטיבי!

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום אנושי מקצועי. אנו לא נושאים באחריות לאי הבנות או פירושים שגויים הנובעים משימוש בתרגום זה.