<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:11:26+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "he"
}
-->
# בנייה עם דגמי משפחת Meta

## מבוא

בשיעור זה נסקור:

- חקירת שני הדגמים המרכזיים ממשפחת Meta - Llama 3.1 ו-Llama 3.2  
- הבנת מקרי השימוש והתסריטים לכל דגם  
- דוגמת קוד להדגמת התכונות הייחודיות של כל דגם  

## משפחת הדגמים של Meta

בשיעור זה נחקור שני דגמים ממשפחת Meta או "עדר Llama" - Llama 3.1 ו-Llama 3.2

דגמים אלו מגיעים בגרסאות שונות וזמינים בשוק הדגמים של GitHub. להלן פרטים נוספים על שימוש בדגמי GitHub ל[פרוטוטייפ עם דגמי AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

גרסאות הדגם:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*הערה: Llama 3 זמין גם ב-GitHub Models אך לא יכוסה בשיעור זה*

## Llama 3.1

עם 405 מיליארד פרמטרים, Llama 3.1 משתייך לקטגוריית ה-LLM בקוד פתוח.

הדגם הוא שדרוג לשחרור הקודם Llama 3 ומציע:

- חלון הקשר גדול יותר - 128k טוקנים לעומת 8k טוקנים  
- מקסימום טוקני פלט גדול יותר - 4096 לעומת 2048  
- תמיכה רב-לשונית משופרת - בזכות עלייה בכמות הטוקנים לאימון  

שיפורים אלו מאפשרים ל-Llama 3.1 להתמודד עם מקרי שימוש מורכבים יותר בעת בניית יישומי GenAI, כולל:  
- קריאה לפונקציות מקוריות - היכולת לקרוא לכלים ופונקציות חיצוניות מחוץ לזרימת העבודה של ה-LLM  
- ביצועי RAG משופרים - בזכות חלון ההקשר הרחב יותר  
- יצירת נתונים סינתטיים - היכולת ליצור נתונים יעילים למשימות כמו כוונון עדין  

### קריאה לפונקציות מקוריות

Llama 3.1 עבר כוונון עדין כדי להיות יעיל יותר בקריאות לפונקציות או כלים. יש לו גם שני כלים מובנים שהדגם יכול לזהות שיש להשתמש בהם בהתבסס על הפקודה מהמשתמש. כלים אלו הם:

- **Brave Search** - ניתן להשתמש בו לקבלת מידע עדכני כמו מזג האוויר באמצעות חיפוש באינטרנט  
- **Wolfram Alpha** - ניתן להשתמש בו לחישובים מתמטיים מורכבים יותר, כך שאין צורך לכתוב פונקציות משלך  

ניתן גם ליצור כלים מותאמים אישית שה-LLM יכול לקרוא להם.

בדוגמת הקוד למטה:

- מגדירים את הכלים הזמינים (brave_search, wolfram_alpha) בהנחיית המערכת.  
- שולחים פקודת משתמש ששואלת על מזג האוויר בעיר מסוימת.  
- ה-LLM יגיב בקריאה לכלי Brave Search שתיראה כך `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*הערה: דוגמה זו מבצעת רק את קריאת הכלי, אם תרצו לקבל את התוצאות, תצטרכו ליצור חשבון חינמי בדף ה-API של Brave ולהגדיר את הפונקציה עצמה*  

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

למרות ש-Llama 3.1 הוא LLM, יש לו מגבלה בתחום המולטימודאליות. כלומר, היכולת להשתמש בסוגי קלט שונים כמו תמונות כהנחיות ולקבל תגובות בהתאם. יכולת זו היא אחת התכונות המרכזיות של Llama 3.2. תכונות נוספות כוללות:

- מולטימודאליות - היכולת להעריך גם טקסט וגם תמונות כהנחיות  
- וריאציות בגודל קטן עד בינוני (11B ו-90B) - מאפשרות אפשרויות פריסה גמישות  
- וריאציות טקסט בלבד (1B ו-3B) - מאפשרות פריסה במכשירים קצה / ניידים ומספקות זמן תגובה נמוך  

התמיכה המולטימודאלית מהווה צעד משמעותי בעולם הדגמים בקוד פתוח. דוגמת הקוד למטה מקבלת גם תמונה וגם הנחיית טקסט לקבלת ניתוח של התמונה מ-Llama 3.2 90B.

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

## הלמידה לא נעצרת כאן, המשיכו במסע

לאחר סיום שיעור זה, בדקו את [אוסף הלמידה של Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) שלנו כדי להמשיך ולשפר את הידע שלכם ב-Generative AI!

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי אדם. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.