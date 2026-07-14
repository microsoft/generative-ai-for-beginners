# בנייה עם דגמי משפחת Meta

## مقدמה

השיעור הזה יכסה:

- חקר שני דגמי משפחת Meta המרכזיים - Llama 3.1 ו-Llama 3.2
- הבנת המקרים והשימושים של כל דגם
- דוגמת קוד להדגמת התכונות הייחודיות של כל דגם


## משפחת דגמי Meta

בשיעור זה, נחקור שני דגמים ממשפחת Meta או "להקת Llama" - Llama 3.1 ו-Llama 3.2.

דגמים אלו מגיעים בגרסאות שונות וזמינים בקטלוג [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **הערה:** GitHub Models יצא משימוש בסוף יולי 2026. לפירוט נוסף על השימוש ב-[Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ליצירת אב-טיפוס עם דגמי בינה מלאכותית.

גרסאות הדגם:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*הערה: Llama 3 זמינה גם ב-Microsoft Foundry Models אך לא תכוסה בשיעור זה*

## Llama 3.1

עם 405 מיליארד פרמטרים, Llama 3.1 משתייכת לקטגוריית ה-LLM בקוד פתוח.

הדגם הוא שדרוג לגרסת Llama 3 הקודמת באמצעות:

- חלון הקשר גדול יותר - 128k טוקנים לעומת 8k טוקנים
- מקסימום טוקנים ביציאה גדול יותר - 4096 לעומת 2048
- תמיכה רב לשונית משופרת - בשל עלייה בכמות הטוקנים לאימון

אלו מאפשרים ל-Llama 3.1 להתמודד עם מקרים מורכבים יותר בעת בניית יישומי GenAI הכוללים:
- קריאה לפונקציות מובנות - היכולת לקרוא לכלים ולפונקציות חיצוניות מחוץ לזרימת העבודה של ה-LLM
- ביצועים טובים יותר ב-RAG - הודות לחלון ההקשר הגדול יותר
- יצירת נתונים סינתטיים - היכולת ליצור נתונים יעילים למשימות כמו כוונון עדין

### קריאה לפונקציות מובנות

Llama 3.1 כוונה להיות יעילה יותר בקריאות לפונקציות או כלים. יש לה גם שני כלים מובנים שהדגם יכול לזהות שיש להשתמש בהם בהתבסס על ההנחיה מהמשתמש. כלים אלו הם:

- **Brave Search** - ניתן להשתמש בו לקבלת מידע עדכני כמו מזג האוויר דרך חיפוש באינטרנט
- **Wolfram Alpha** - מתאים לחישובים מתמטיים מורכבים כך שאין צורך לכתוב פונקציות משלך.

ניתן גם ליצור כלים מותאמים אישית שה-LLM יכול לקרוא להם.

בדוגמת הקוד למטה:

- אנו מגדירים את הכלים הזמינים (brave_search, wolfram_alpha) בהנחיית המערכת.
- שולחים הנחיית משתמש ששואלת על מזג האוויר בעיר מסוימת.
- ה-LLM יגיב בקריאה לכלי Brave Search שתראה כך `<|python_tag|>brave_search.call(query="Stockholm weather")`

*הערה: בדוגמה זו מתבצעת רק קריאה לכלי. אם ברצונך לקבל את התוצאות, יהיה עליך ליצור חשבון חינם בדף API של Brave ולהגדיר את הפונקציה עצמה.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# קבל אותם מעמוד "סקירה" של פרויקט Microsoft Foundry שלך
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Meta-Llama-3.1-405B-Instruct"

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

למרות שזו LLM, מגבלה של Llama 3.1 היא חוסר המולטימודאליות שלה. כלומר, חוסר היכולת להשתמש בקלט מסוגים שונים כמו תמונות כהנחיות ולהגיב בהתאם. יכולת זו היא אחת התכונות המרכזיות של Llama 3.2. תכונות נוספות כוללות:

- מולטימודאליות - היכולת להעריך גם טקסט וגם תמונות כהנחיות
- וריאציות בגודל קטן עד בינוני (11B ו-90B) - מה שמאפשר אפשרויות פריסה גמישות
- וריאציות טקסט בלבד (1B ו-3B) - מאפשרות פריסה במכשירים קצה/ניידים ומספקות זמני תגובה נמוכים

התמיכה המולטימודאלית מהווה צעד גדול בעולם דגמי הקוד הפתוח. דוגמת הקוד למטה מקבלת גם תמונת קלט וגם הנחיית טקסט כדי לקבל ניתוח של התמונה מ-Llama 3.2 בגודל 90B.


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

# קבל את אלה מדף "סקירה כללית" של פרויקט Microsoft Foundry שלך
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
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

## הלמידה לא נעצרת כאן, המשך במסע

לאחר שסיימת שיעור זה, בדוק את [אוסף הלמידה בגנרטיב AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) שלנו כדי להמשיך ולשפר את הידע שלך בגנרטיב AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->