<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:13:32+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "he"
}
-->
# בנייה עם מודלים ממשפחת מטא

## הקדמה

השיעור הזה יכסה:

- חקר שני המודלים המרכזיים ממשפחת מטא - Llama 3.1 ו-Llama 3.2
- הבנת השימושים והתסריטים לכל מודל
- דוגמת קוד להראות את התכונות הייחודיות של כל מודל

## משפחת המודלים של מטא

בשיעור זה נחקור שני מודלים ממשפחת מטא או "עדר Llama" - Llama 3.1 ו-Llama 3.2

מודלים אלה מגיעים בגרסאות שונות וזמינים בשוק המודלים של GitHub. הנה פרטים נוספים על שימוש במודלים של GitHub ל[אב-טיפוס עם מודלים של AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

גרסאות מודלים:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*הערה: Llama 3 זמין גם במודלים של GitHub אך לא יכוסה בשיעור זה*

## Llama 3.1

עם 405 מיליארד פרמטרים, Llama 3.1 משתייך לקטגוריית LLM בקוד פתוח.

המודל הוא שדרוג לשחרור הקודם Llama 3 על ידי הצעת:

- חלון הקשר גדול יותר - 128k טוקנים לעומת 8k טוקנים
- מקסימום טוקנים לפלט גדול יותר - 4096 לעומת 2048
- תמיכה רב-לשונית טובה יותר - בשל עלייה בטוקנים אימון

אלה מאפשרים ל-Llama 3.1 להתמודד עם מקרים שימוש מורכבים יותר בעת בניית יישומי GenAI כולל:
- קריאה לפונקציות מקוריות - היכולת לקרוא לכלים חיצוניים ופונקציות מחוץ לזרימת העבודה של LLM
- ביצועי RAG טובים יותר - בזכות חלון ההקשר הגבוה יותר
- יצירת נתונים סינתטיים - היכולת ליצור נתונים אפקטיביים למשימות כגון כוונון עדין

### קריאה לפונקציות מקוריות

Llama 3.1 כוונן כדי להיות יעיל יותר בביצוע קריאות לפונקציות או כלים. יש לו גם שני כלים מובנים שהמודל יכול לזהות כצריך להשתמש בהם על סמך ההנחיה מהמשתמש. כלים אלה הם:

- **Brave Search** - ניתן להשתמש בו לקבלת מידע עדכני כמו מזג האוויר על ידי ביצוע חיפוש ברשת
- **Wolfram Alpha** - ניתן להשתמש בו לחישובים מתמטיים מורכבים יותר כך שאין צורך לכתוב פונקציות משלך.

אתה יכול גם ליצור כלים מותאמים אישית משלך ש-LLM יכול לקרוא להם.

בדוגמת הקוד למטה:

- אנו מגדירים את הכלים הזמינים (brave_search, wolfram_alpha) בהנחיית המערכת.
- שולחים הנחיית משתמש ששואלת על מזג האוויר בעיר מסוימת.
- ה-LLM יגיב עם קריאה לכלי Brave Search שתראה כך `<|python_tag|>brave_search.call(query="Stockholm weather")`

*הערה: דוגמה זו רק מבצעת את קריאת הכלי, אם תרצה לקבל את התוצאות, תצטרך ליצור חשבון חינם בדף ה-API של Brave ולהגדיר את הפונקציה עצמה*

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

למרות שהוא LLM, מגבלה אחת שיש ל-Llama 3.1 היא מולטימודאליות. כלומר, היכולת להשתמש בסוגים שונים של קלט כמו תמונות כהנחיות ולספק תגובות. יכולת זו היא אחת התכונות המרכזיות של Llama 3.2. תכונות אלה כוללות גם:

- מולטימודאליות - יש לו את היכולת להעריך הן הנחיות טקסט והן תמונה
- גרסאות קטנות עד בינוניות (11B ו-90B) - זה מספק אפשרויות פריסה גמישות,
- גרסאות טקסט בלבד (1B ו-3B) - זה מאפשר למודל להיפרס על מכשירי קצה / נייד ומספק זמן תגובה נמוך

התמיכה המולטימודאלית מייצגת צעד גדול בעולם המודלים בקוד פתוח. דוגמת הקוד למטה לוקחת גם תמונה וגם הנחיית טקסט כדי לקבל ניתוח של התמונה מ-Llama 3.2 90B.

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

## הלמידה לא נעצרת כאן, המשך המסע

לאחר סיום השיעור הזה, בדוק את [אוסף הלמידה של AI יצירתי](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) שלנו כדי להמשיך לשפר את הידע שלך ב-AI יצירתי!

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, אנא היו מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. אנו לא נושאים באחריות לכל אי הבנה או פרשנות מוטעית הנובעת משימוש בתרגום זה.