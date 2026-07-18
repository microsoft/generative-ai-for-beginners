# בנייה עם מודלי מיסטרל

## מבוא

שיעור זה יכלול:
- חקר מודלי מיסטרל השונים
- הבנת מקרים ותסריטים לשימוש בכל מודל
- חקר דוגמאות קוד שמציגות את התכונות הייחודיות של כל מודל.

## מודלי מיסטרל

בשיעור זה נחקור 3 מודלים שונים של מיסטרל:
**Mistral Large**, **Mistral Small** ו-**Mistral Nemo**.

כל אחד מהמודלים האלו זמין בחינם ב-[Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). הקוד במחברת זו ישתמש במודלים אלה כדי להריץ את הקוד.

> **הערה:** GitHub Models ייסגר בסוף יולי 2026. להלן פרטים נוספים על השימוש ב-[Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) לפרוטוטייפ עם מודלי AI.


## Mistral Large 2 (2407)
Mistral Large 2 הוא כרגע המודל הדגל של מיסטרל ומיועד לשימוש בארגוני.

המודל מהווה שדרוג למודל Mistral Large המקורי בכך שהוא מציע
- חלון הקשר גדול יותר - 128k לעומת 32k
- ביצועים משופרים במשימות מתמטיקה וקידוד - 76.9% דיוק ממוצע לעומת 60.4%
- ביצועים משופרים בריבוי שפות - שפות כוללות: אנגלית, צרפתית, גרמנית, ספרדית, איטלקית, פורטוגזית, הולנדית, רוסית, סינית, יפנית, קוריאנית, ערבית והינדי.

עם תכונות אלה, Mistral Large מצטיין ב
- *הפקה משודרגת עם אחזור (RAG)* - בזכות חלון ההקשר הגדול יותר
- *קריאות פונקציה* - למודל זה יש קריאות פונקציה מובנות המאפשרות אינטגרציה עם כלים ו-APIs חיצוניים. קריאות אלה יכולות להתבצע במקביל או לפי סדר רציף.
- *יצירת קוד* - מודל זה מצטיין ביצירת Python, Java, TypeScript ו-C++.

### דוגמה ל-RAG באמצעות Mistral Large 2

בדוגמה זו, אנו משתמשים ב-Mistral Large 2 כדי להריץ תבנית RAG על מסמך טקסט. השאלה נכתבת בקוריאנית ושואלת על פעילויות המחבר לפני המכללה.

הוא משתמש במודל האמבדינג של Cohere ליצירת אמבדינגים של מסמך הטקסט ושל השאלה. בדוגמה זו, נעשה שימוש בחבילת faiss בפייתון כאחסון וקטורי.

ההנחיה שנשלחת למודל מיסטרל כוללת גם את השאלות וגם את הקטעים שנמצאו והם דומים לשאלה. המודל מספק תגובה בשפה טבעית.

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

# קבל אותם מדף "סקירה" של פרויקט Foundry שלך ב-Microsoft
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
Mistral Small הוא מודל נוסף ממשפחת מיסטרל תחת קטגוריית פרמייר/ארגוני. כפי ששמו מרמז, מודל זה הוא מודל שפה קטן (SLM). היתרונות של שימוש ב-Mistral Small הם:
- חיסכון בעלויות בהשוואה ל-LLM של מיסטרל כמו Mistral Large ו-NeMo - ירידה במחיר של 80%
- זמן תגובה נמוך - מהיר יותר בתגובה לעומת LLM של מיסטרל
- גמישות - יכול להיות מופעל בסביבות שונות עם פחות הגבלות על משאבים דרושים.


Mistral Small מתאים ל:
- משימות מבוססות טקסט כגון סיכום, ניתוח סנטימנט ותרגום.
- אפליקציות בהן נעשות בקשות תכופות בשל יעילות העלות
- משימות קוד עם זמני תגובה נמוכים כמו סקירה והצעות קוד

## השוואה בין Mistral Small ל-Mistral Large

כדי להראות הבדל בזמני תגובה בין Mistral Small ל-Large, הריצו את התאים למטה.

תראו הבדל בזמני תגובה של בין 3 ל-5 שניות. שימו לב גם לאורך התגובות וסגנונן על אותה הנחיה.

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

בהשוואה לשני המודלים האחרים שנדונו בשיעור זה, Mistral NeMo הוא המודל היחיד החופשי עם רישיון Apache2.

הוא נחשב לשדרוג ל-LLM הקודמת בקוד פתוח של מיסטרל, Mistral 7B.

כמה תכונות נוספות של מודל NeMo הן:

- *טוקניזציה יעילה יותר:* מודל זה משתמש בטוקנייזר Tekken במקום tiktoken הנפוץ יותר. זה מאפשר ביצועים טובים יותר בשפות ובקוד רבים יותר.

- *פיינטונינג:* המודל הבסיסי זמין לפיינטונינג. זה מאפשר גמישות רבה יותר למקרים שבהם יש צורך בפיינטונינג.

- *קריאות פונקציה מובנות* - כמו Mistral Large, מודל זה אומן גם לקריאות פונקציה. זה הופך אותו לייחודי כאחד מהמודלים הראשונים בקוד פתוח לעשות כך.


### השוואת טוקנייזרים

בדוגמה זו, נבחן כיצד Mistral NeMo מטפל בטוקניזציה בהשוואה ל-Mistral Large.

שתי הדוגמאות לוקחות את אותה הנחיה אך תראו כי NeMo מחזיר פחות טוקנים מ-Mistral Large.

```bash
pip install mistral-common
```

```python 
# ייבוא חבילות נחוצות:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# טען את מגדל המילים של Mistral

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
# ייבא את החבילות הנדרשות:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# טען את המטען של מיסטרל

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# המיר רשימת הודעות לטוקנים
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

# ספור את מספר הטוקנים
print(len(tokens))
```

## הלמידה לא נגמרת כאן, המשיכו במסע

לאחר סיום שיעור זה, בדקו את [אוסף הלמידה ב-AI גנרטיבי שלנו](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) כדי להמשיך להעמיק את הידע שלכם ב-AI גנרטיבי!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->