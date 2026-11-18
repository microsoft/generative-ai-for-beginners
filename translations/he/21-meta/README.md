# בנייה עם דגמי משפחת Meta  

## מבוא  

שיעור זה יכסה:  

- חקירת שני הדגמים העיקריים ממשפחת Meta - Llama 3.1 ו-Llama 3.2, בנוסף לחלופות הזמינות כיום המשמשות בדוגמאות הקוד (Llama 3.3 ו-Llama 4)  
- הבנת מקרי השימוש והתסריטים עבור כל דגם  
- דוגמת קוד להדגמת התכונות הייחודיות של כל דגם  


## משפחת הדגמים של Meta  

בשיעור זה נחפור בשני דגמים ממשפחת Meta או "עדר ה-Llama" - Llama 3.1 ו-Llama 3.2. דוגמאות הקוד הניתנות להרצה משתמשות ב-Llama 3.3 ו-Llama 4, שהן החלופות הזמינות כיום בקטלוג דגמי Microsoft Foundry.  

דגמים אלה מגיעים בגרסאות שונות וזמינות ב[קטלוג דגמי Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).  

> **הערה:** GitHub Models מופסק בסוף יולי 2026. להלן פרטים נוספים על שימוש ב-[Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) לפרוטוטייפ עם דגמי AI.  

> **הערה:** הגרסאות הספציפיות של הדגמים עליהן נכתב שיעור זה במקור (Llama 3.1 70B/405B Instruct, Llama 3.2 11B/90B Vision Instruct) פורשו מאז מקטלוג דגמי Microsoft Foundry. דוגמאות הקוד למטה משתמשות ב-`Llama-3.3-70B-Instruct` ו-`Llama-4-Scout-17B-16E-Instruct` כחלופות הזמינות כיום בקטלוג דגמי Microsoft Foundry, ולכן עדיין רצות היום.  

וריאציות דגם (כמו שנדונו במקור בשיעור זה):  
- Llama 3.1 - 70B Instruct (פורש)  
- Llama 3.1 - 405B Instruct (פורש)  
- Llama 3.2 - 11B Vision Instruct (פורש)  
- Llama 3.2 - 90B Vision Instruct (פורש)  

חלופות זמינות כיום המשמשות בדוגמאות הקוד:  
- Llama 3.3 - 70B Instruct (`Llama-3.3-70B-Instruct`)  
- Llama 4 Scout - 17B 16E Instruct (`Llama-4-Scout-17B-16E-Instruct`)  

*הערה: וריאציות Llama 3 שנדונו לעיל נשמרות לצורך הקשר היסטורי ואינן זמינות עוד ב-Microsoft Foundry Models.*  

## Llama 3.1  

עם 405 מיליארד פרמטרים, Llama 3.1 משתייך לקטגוריית ה-LLM בקוד פתוח.  

הדגם הוא שדרוג לשחרור מוקדם יותר Llama 3 בכך שהוא מציע:  

- חלון הקשר גדול יותר - 128k טוקנים מול 8k טוקנים  
- מקסימום פלט גדול יותר - 4096 מול 2048  
- תמיכה רב-לשונית משופרת - בזכות העלייה בכמות הטוקנים לאימון  

אלה מאפשרים ל-Llama 3.1 להתמודד עם מקרי שימוש מסובכים יותר בבניית אפליקציות GenAI כולל:  
- קריאה לפונקציות מקוריות - היכולת לקרוא לכלים ופונקציות חיצוניים מחוץ לזרימת העבודה של ה-LLM  
- ביצועי RAG טובים יותר - בזכות חלון הקשר גבוה יותר  
- יצירת נתונים סינתטיים - היכולת לייצר נתונים אפקטיביים עבור משימות כמו כוונון מדויק  

### קריאה לפונקציות מקוריות  

Llama 3.1 עובר כוונון עדין כדי להיות יעיל יותר בקריאות לפונקציות או לכלים. יש לו גם שני כלים מובנים שהדגם יכול לזהות כדרושים לשימוש בהתבסס על ההנחיה מהמשתמש. כלים אלה הם:  

- **Brave Search** - ניתן להשתמש בו לקבלת מידע עדכני כמו מזג האוויר על ידי ביצוע חיפוש באינטרנט  
- **Wolfram Alpha** - ניתן להשתמש בו עבור חישובים מתמטיים מורכבים יותר ולכן לא נדרש לכתוב פונקציות משלך.  

אפשר גם ליצור כלים מותאמים אישית שה-LLM יכול לקרוא להם.  

בדוגמת הקוד למטה:  

- הגדרנו את הכלים הזמינים (brave_search, wolfram_alpha) בפירוט מערכת.  
- שלחנו הנחיית משתמש השואלת על מזג האוויר בעיר מסוימת.  
- ה-LLM יענה בקריאת כלי לכלי Brave Search שתיראה כך `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*הערה: דוגמה זו מבצעת רק את קריאת הכלי, אם ברצונך לקבל את התוצאות, תצטרך ליצור חשבון חינמי בדף ה-API של Brave ולהגדיר את הפונקציה עצמה.  

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Meta-Llama-3.1-405B-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-3.3-70B-Instruct, a currently available alternative, instead
model_name = "Llama-3.3-70B-Instruct"

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

למרות שהוא LLM, מגבלה של Llama 3.1 היא חוסר המולטימודליות שלו. כלומר, חוסר היכולת להשתמש בסוגי קלט שונים כמו תמונות כהנחיות ולספק תגובות. יכולת זו היא אחת התכונות המרכזיות של Llama 3.2. תכונות אלו כוללות גם:  

- מולטימודליות - יש לו היכולת להעריך גם טקסט וגם הנחיות תמונה  
- וריאציות בגודל קטן עד בינוני (11B ו-90B) - זה מספק אפשרויות פריסה גמישות,  
- וריאציות טקסט בלבד (1B ו-3B) - זה מאפשר לפרוס את הדגם על התקנים קצה / מובייל ומספק זמן השהייה נמוך  

התמיכה המולטימודלית מהווה צעד גדול בעולם הדגמים בקוד פתוח. דוגמת הקוד למטה מקבלת גם הנחיה של תמונה וגם טקסט כדי לקבל ניתוח התמונה. כיוון ש-Llama 3.2 90B Vision Instruct פורש, הדוגמה משתמשת ב-`Llama-4-Scout-17B-16E-Instruct`, חלופה מולטימודלית זמינה באופן טבעי.  


### תמיכה מולטימודלית עם Llama 3.2  

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

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Llama-3.2-90B-Vision-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-4-Scout-17B-16E-Instruct, a currently available natively multimodal alternative, instead
model_name = "Llama-4-Scout-17B-16E-Instruct"

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

## הלמידה לא נעצרת כאן, המשך את המסלול  

לאחר סיום שיעור זה, בדוק את [אוסף הלמידה של Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) כדי להמשיך ולשדרג את הידע שלך ב-Generative AI!  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->