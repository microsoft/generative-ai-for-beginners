# בנייה עם דגמי משפחת Meta

## מבוא

שיעור זה יכסה:

- חקירת שני הדגמים המרכזיים ממשפחת Meta - Llama 3.1 ו-Llama 3.2
- הבנת השימושים והתסריטים לכל דגם
- דוגמת קוד להדגמת התכונות הייחודיות של כל דגם


## משפחת דגמי Meta

בשיעור זה, נחקור שני דגמים ממשפחת Meta או "עדר Llama" - Llama 3.1 ו-Llama 3.2.

דגמים אלו מגיעים בגרסאות שונות וזמינים ב[קטלוג דגמי Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **הערה:** GitHub Models מפסיקה פעילות בסוף יולי 2026. להלן פרטים נוספים על שימוש ב-[Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) לבניית אב טיפוס עם דגמי AI.

גרסאות הדגם:
- Llama 3.1 - 70 מיליארד הוראות
- Llama 3.1 - 405 מיליארד הוראות
- Llama 3.2 - 11 מיליארד הוראות חזון
- Llama 3.2 - 90 מיליארד הוראות חזון

*הערה: Llama 3 זמינה גם ב-Microsoft Foundry Models אך לא תיכלל בשיעור זה*

## Llama 3.1

עם 405 מיליארד פרמטרים, Llama 3.1 משתייכת לקטגוריית ה-LLM קוד פתוח.

הדגם הוא שדרוג לשחרור הקודם Llama 3 ומציע:

- חלון הקשר גדול יותר - 128k טוקנים לעומת 8k טוקנים
- כמות מקסימלית גדולה יותר של טוקני פלט - 4096 לעומת 2048
- תמיכה רב-לשונית טובה יותר - בשל גידול בכמות הטוקנים לאימון

זה מאפשר ל-Llama 3.1 לטפל במקרים מורכבים יותר בעת בניית יישומי GenAI כולל:
- קריאת פונקציות מקורית - היכולת לקרוא לכלים ופונקציות חיצוניות מחוץ לזרימת עבודה של ה-LLM
- ביצועי RAG טובים יותר - בזכות חלון ההקשר הגבוה יותר
- יצירת נתונים סינתטיים - היכולת ליצור נתונים יעילים למשימות כמו כיוונון מדויק

### קריאת פונקציות מקורית

ל-Llama 3.1 בוצע כיוונון מדויק כדי להיות יעילה יותר בביצוע קריאות לפונקציות או כלים. יש לו גם שני כלים מובנים שהדגם מזהה כשיש צורך להשתמש בהם בהתאם לפקודה מהמשתמש. כלים אלו הם:

- **Brave Search** - ניתן להשתמש לקבלת מידע מעודכן כמו מזג האוויר באמצעות חיפוש אינטרנטי
- **Wolfram Alpha** - ניתן להשתמש לחישובים מתמטיים מורכבים כך שאין צורך לכתוב פונקציות בעצמך.

ניתן גם ליצור כלים מותאמים אישית שה-LLM יכול לקרוא להם.

בדוגמת הקוד למטה:

- אנו מגדירים את הכלים הזמינים (brave_search, wolfram_alpha) במערכת הפקודה.
- שולחים פקודה משתמש שמבקשת מידע על מזג האוויר בעיר מסוימת.
- ה-LLM יגיב עם קריאת כלי לכלי Brave Search, שתיראה כך `<|python_tag|>brave_search.call(query="Stockholm weather")`

*הערה: הדוגמה עושה רק את קריאת הכלי, אם תרצו לקבל את התוצאות, תצטרכו ליצור חשבון בחינם בדף ה-API של Brave ולהגדיר את הפונקציה עצמה.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# קבל את אלה מדף "סקירה כללית" של פרויקט Foundry של Microsoft שלך
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

למרות שזוהי LLM, מגבלה של Llama 3.1 היא חוסר הרב-מודליות. כלומר, חוסר היכולת להשתמש בסוגי קלט שונים כמו תמונות כפירומטים ולהגיב בהתאם. יכולת זו היא אחת התכונות המרכזיות של Llama 3.2. תכונות נוספות כוללות:

- רב-מודליות - היכולת להעריך גם טקסט וגם תמונות כפירומטים
- גרסאות בגדלים קטנים עד בינוניים (11B ו-90B) - מספקות אפשרויות פריסה גמישות,
- גרסאות טקסט בלבד (1B ו-3B) - מאפשרות פריסה במכשירים קצה / מובייל ומספקות השהייה נמוכה

התמיכה הרב-מודלית מייצגת צעד משמעותי בעולם הדגמים בקוד פתוח. דוגמת הקוד למטה מקבלת גם תמונה וגם פקודת טקסט לקבלת ניתוח של התמונה מ-Llama 3.2 90B.


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

# קבל אותם מדף "סקירה כללית" של פרויקט Microsoft Foundry שלך
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

## הלמידה לא תיפסק כאן, המשך את המסע

לאחר סיום שיעור זה, בדוק את [אוסף הלמידה של AI גנרטיבי שלנו](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) כדי להמשיך ולהרחיב את הידע שלך ב-AI גנרטיבי!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->