# בנייה עם מודלי מיסטרל 

## מבוא 

בשיעור זה נסקור: 
- חקר המודלים השונים של מיסטרל 
- הבנת מקרי השימוש והתסריטים לכל מודל 
- חקר דוגמאות קוד שמראות את התכונות הייחודיות של כל מודל. 

## מודלי מיסטרל 

בשיעור זה, נחקור 3 מודלים שונים של מיסטרל: 
**Mistral Large**, **Mistral Small** ו-**Mistral Nemo**. 

כל אחד מהמודלים האלה זמין בחינם ב-[Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). הקוד במחברת זו ישתמש במודלים אלו להרצת הקוד.

> **הערה:** GitHub Models פורש בסוף יולי 2026. לפרטים נוספים על שימוש ב-[Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) לפרוטוטייפ עם מודלי AI. 


## Mistral Large 2 (2407)
Mistral Large 2 הוא כיום המודל המוביל של מיסטרל ומיועד לשימוש ארגוני. 

המודל הוא שדרוג ל-Mistral Large המקורי ומציע 
- חלון הקשר גדול יותר – 128k לעומת 32k 
- ביצועים טובים יותר במשימות מתמטיקה וקוד – דיוק ממוצע של 76.9% לעומת 60.4% 
- שיפור בביצועים רב-לשוניים – שפות כוללות: אנגלית, צרפתית, גרמנית, ספרדית, איטלקית, פורטוגזית, הולנדית, רוסית, סינית, יפנית, קוריאנית, ערבית והינדי.

עם תכונות אלו, Mistral Large מצטיין ב 
- *יצירה משודרגת עם אחזור (RAG)* – בזכות חלון ההקשר הגדול יותר
- *קריאת פונקציות* – מודל זה כולל קריאה פונקציונלית מקומית המאפשרת אינטגרציה עם כלים ו-APIs חיצוניים. קריאות אלו יכולות להתבצע במקביל או בהמשך אחד אחרי השני בסדר רציף. 
- *יצירת קוד* – מודל זה מצטיין ביצירת קוד בפייתון, ג'אווה, TypeScript ו-C++. 

### דוגמת RAG באמצעות Mistral Large 2 

בדוגמה זו, אנו משתמשים ב-Mistral Large 2 כדי להריץ דפוס RAG על מסמך טקסט. השאלה כתובה בקוריאנית ושואלת על פעילויות המחבר לפני הקולג'. 

נעשה שימוש במודל ההטבעה Cohere ליצור הטבעות של מסמך הטקסט כמו גם של השאלה. בדוגמה זו, נעשה שימוש בחבילת פייתון faiss כאכסון וקטורי. 

ההנחיה שנשלחת למודל מיסטרל כוללת הן את השאלות והן את הקטעים שנשלפו שהם דומים לשאלה. המודל ואז מספק תגובה בשפה טבעית. 

```python 
pip install faiss-cpu
```

```python 
import requests
import numpy as np
import faiss
import os

from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference import EmbeddingsClient

# קבל את אלו מדף "סקירה כללית" של פרויקט Microsoft Foundry שלך
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-large"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = requests.get('https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/paul_graham/paul_graham_essay.txt')
text = response.text

chunk_size = 2048
chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
len(chunks)

embed_model_name = "cohere-embed-v3-multilingual" 

embed_client = EmbeddingsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token)
)

embed_response = embed_client.embed(
    input=chunks,
    model=embed_model_name
)



text_embeddings = []
for item in embed_response.data:
    length = len(item.embedding)
    text_embeddings.append(item.embedding)
text_embeddings = np.array(text_embeddings)


d = text_embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(text_embeddings)

question = "저자가 대학에 오기 전에 주로 했던 두 가지 일은 무엇이었나요?"

question_embedding = embed_client.embed(
    input=[question],
    model=embed_model_name
)

question_embeddings = np.array(question_embedding.data[0].embedding)


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # מרחק, אינדקס
retrieved_chunks = [chunks[i] for i in I.tolist()[0]]

prompt = f"""
Context information is below.
---------------------
{retrieved_chunks}
---------------------
Given the context information and not prior knowledge, answer the query.
Query: {question}
Answer:
"""


chat_response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content=prompt),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(chat_response.choices[0].message.content)
```

## Mistral Small 
Mistral Small הוא מודל נוסף במשפחת מיסטרל בקטגוריית הפרמייר/ארגונית. כשמו כן הוא, מודל זה הוא מודל שפה קטן (SLM). היתרונות של שימוש ב-Mistral Small הם: 
- חסכון בעלויות לעומת LLM של מיסטרל כמו Mistral Large ו-NeMo – ירידה של 80% במחיר
- זמן השהייה נמוך - תגובה מהירה יותר לעומת LLM של מיסטרל
- גמיש - ניתן לפרוס בסביבות שונות עם פחות מגבלות על משאבים נדרשים. 


Mistral Small מצוין ל: 
- משימות מבוססות טקסט כמו סיכום, ניתוח סנטימנט ותרגום. 
- אפליקציות שבהן מבוצעות בקשות תכופות בשל עלות כספית יעילה 
- משימות קוד עם זמן השהייה נמוך כמו סקירה והצעות קוד 

## השוואה בין Mistral Small ו-Mistral Large 

כדי להראות הבדלים בזמן השהייה בין Mistral Small ל-Large, הריצו את התאים שלמטה. 

עליכם לראות הבדל בזמני תגובה בין 3 ל-5 שניות. שימו לב גם לאורך התגובות והסגנון עבור אותה הנחיה.  

```python 

import os 
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-small"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful coding assistant."),
        UserMessage(content="Can you write a Python function to the fizz buzz test?"),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(response.choices[0].message.content)

```

```python 

import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-large"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful coding assistant."),
        UserMessage(content="Can you write a Python function to the fizz buzz test?"),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(response.choices[0].message.content)

```

## Mistral NeMo

לעומת שני המודלים האחרים שדנו בהם בשיעור זה, Mistral NeMo הוא המודל החינמי היחיד עם רישיון Apache2. 

הוא נחשב לשדרוג ל-LLM הקודמת בקוד פתוח ממיסטרל, Mistral 7B. 

כמה תכונות נוספות של מודל NeMo הן: 

- *טוקניזציה יעילה יותר:* מודל זה משתמש בטוקניזר Tekken במקום ב-tiktoken הנפוץ יותר. זה מאפשר ביצועים טובים יותר על יותר שפות וקוד. 

- *אימון מחדש:* המודל הבסיסי זמין לאימון מחדש. זה מאפשר גמישות רבה יותר למקרי שימוש שבהם ייתכן צורך באימון מחדש. 

- *קריאת פונקציות מקומית* - כמו Mistral Large, מודל זה אומן לקריאת פונקציות. זה הופך אותו לייחודי כאחד המודלים בקוד פתוח הראשונים שעושים זאת. 


### השוואת טוקניזרים 

בדוגמה זו, נבחן כיצד Mistral NeMo מטפל בטוקניזציה בהשוואה ל-Mistral Large. 

שני הדוגמאות לוקחות את אותה הנחיה אך עליכם לראות כי NeMo מחזיר פחות טוקנים מ-Mistral Large. 

```bash
pip install mistral-common
```

```python 
# ייבא חבילות נדרשות:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# טען את המפענח של מיסטרל

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# הפרד רשימת הודעות לטוקנים
tokenized = tokenizer.encode_chat_completion(
    ChatCompletionRequest(
        tools=[
            Tool(
                function=Function(
                    name="get_current_weather",
                    description="Get the current weather",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA",
                            },
                            "format": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "The temperature unit to use. Infer this from the user's location.",
                            },
                        },
                        "required": ["location", "format"],
                    },
                )
            )
        ],
        messages=[
            UserMessage(content="What's the weather like today in Paris"),
        ],
        model=model_name,
    )
)
tokens, text = tokenized.tokens, tokenized.text

# ספר את מספר הטוקנים
print(len(tokens))
```

```python
# ייבא את החבילות הדרושות:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# טען את הטוקניזר של מיסטרל

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# בטוקנן רשימת הודעות
tokenized = tokenizer.encode_chat_completion(
    ChatCompletionRequest(
        tools=[
            Tool(
                function=Function(
                    name="get_current_weather",
                    description="Get the current weather",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA",
                            },
                            "format": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "The temperature unit to use. Infer this from the user's location.",
                            },
                        },
                        "required": ["location", "format"],
                    },
                )
            )
        ],
        messages=[
            UserMessage(content="What's the weather like today in Paris"),
        ],
        model=model_name,
    )
)
tokens, text = tokenized.tokens, tokenized.text

# ספר את מספר הטוקנים
print(len(tokens))
```

## הלמידה לא מסתיימת כאן, המשיכו במסע 

לאחר שסיימתם שיעור זה, בדקו את [אוסף הלמידה על AI יצירתי שלנו](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) כדי להמשיך לשדרג את הידע שלכם ב-AI יצירתי!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->