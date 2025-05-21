<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T10:59:52+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "he"
}
-->
# בנייה עם מודלים של מיסטרל

## הקדמה

השיעור הזה יעסוק ב:
- חקר המודלים השונים של מיסטרל
- הבנת השימושים והתסריטים לכל מודל
- דוגמאות קוד שמראות את התכונות הייחודיות של כל מודל.

## מודלי מיסטרל

בשיעור הזה נחקור 3 מודלים שונים של מיסטרל: **Mistral Large**, **Mistral Small** ו- **Mistral Nemo**.

כל אחד מהמודלים האלה זמין בחינם בשוק המודלים של גיטהאב. הקוד במחברת זו ישתמש במודלים אלה להריץ את הקוד. כאן יש עוד פרטים על שימוש במודלים של גיטהאב ל[יצירת אב טיפוס עם מודלים של AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)

Mistral Large 2 הוא כרגע המודל המוביל של מיסטרל ומיועד לשימוש ארגוני.

המודל הוא שדרוג למודל המקורי של Mistral Large על ידי הצעת:
- חלון הקשר גדול יותר - 128k לעומת 32k
- ביצועים טובים יותר במשימות מתמטיקה וקידוד - 76.9% דיוק ממוצע לעומת 60.4%
- ביצועים רב-לשוניים מוגברים - שפות כוללות: אנגלית, צרפתית, גרמנית, ספרדית, איטלקית, פורטוגזית, הולנדית, רוסית, סינית, יפנית, קוריאנית, ערבית והינדית.

עם התכונות האלה, Mistral Large מצטיין ב:
- *הפקת מידע מוגברת (RAG)* - בשל חלון ההקשר הגדול יותר
- *קריאת פונקציות* - למודל הזה יש קריאת פונקציות טבעית שמאפשרת אינטגרציה עם כלים חיצוניים ו-API. ניתן לבצע קריאות אלה במקביל או אחת אחרי השנייה בסדר רציף.
- *הפקת קוד* - המודל מצטיין בהפקת קוד ב-Python, Java, TypeScript ו-C++.

### דוגמת RAG באמצעות Mistral Large 2

בדוגמה הזו, אנחנו משתמשים ב-Mistral Large 2 להריץ דפוס RAG על מסמך טקסט. השאלה כתובה בקוריאנית ושואלת על פעילויות המחבר לפני הקולג'.

היא משתמשת במודל Cohere Embeddings ליצירת הטמעות של מסמך הטקסט כמו גם השאלה. לדוגמה הזו, היא משתמשת בחבילת Python faiss כמאגר וקטורים.

הבקשה שנשלחת למודל מיסטרל כוללת את השאלות ואת החלקים שנשלפו שדומים לשאלה. המודל מספק תגובה בשפה טבעית.

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

endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-large"
token = os.environ["GITHUB_TOKEN"]

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

question = "저자가 대학에 오기 전에 주로 했던 두 가지 일은 무엇이었나요?？"

question_embedding = embed_client.embed(
    input=[question],
    model=embed_model_name
)

question_embeddings = np.array(question_embedding.data[0].embedding)


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # distance, index
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

Mistral Small הוא מודל נוסף במשפחת המודלים של מיסטרל תחת קטגוריית הפרמייר/ארגוני. כפי שמשתמע מהשם, המודל הזה הוא מודל שפה קטן (SLM). היתרונות בשימוש ב-Mistral Small הם:
- חיסכון בעלויות לעומת Mistral LLMs כמו Mistral Large ו-NeMo - ירידת מחיר של 80%
- זמן תגובה נמוך - תגובה מהירה לעומת ה-LLMs של מיסטרל
- גמישות - ניתן לפרוס בסביבות שונות עם פחות הגבלות על משאבים נדרשים.

Mistral Small מצוין עבור:
- משימות מבוססות טקסט כמו סיכום, ניתוח תחושות ותרגום.
- יישומים שבהם מתבצעות בקשות תכופות בשל היעילות הכלכלית שלו
- משימות קוד עם זמן תגובה נמוך כמו סקירה והצעות קוד

## השוואת Mistral Small ו-Mistral Large

כדי להראות את ההבדלים בזמן תגובה בין Mistral Small ו-Large, הרץ את התאים הבאים.

אתה אמור לראות הבדל בזמני תגובה בין 3-5 שניות. שים לב גם לאורך התגובות וסגנון על אותה בקשה.

```python 

import os 
endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-small"
token = os.environ["GITHUB_TOKEN"]

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

endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-large"
token = os.environ["GITHUB_TOKEN"]

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

לעומת שני המודלים האחרים שנדונו בשיעור זה, Mistral NeMo הוא המודל החינמי היחיד עם רישיון Apache2.

הוא נחשב לשדרוג למודל ה-LLM קוד פתוח הקודם של מיסטרל, Mistral 7B.

כמה תכונות נוספות של מודל NeMo הן:

- *תהליך טוקניזציה יעיל יותר:* המודל הזה משתמש בטוקניזר Tekken במקום הטוקניזר tiktoken הנפוץ יותר. זה מאפשר ביצועים טובים יותר על פני יותר שפות וקוד.

- *התאמה אישית:* מודל הבסיס זמין להתאמה אישית. זה מאפשר יותר גמישות לשימושים שבהם עשויה להידרש התאמה אישית.

- *קריאת פונקציות טבעית* - כמו Mistral Large, המודל הזה אומן על קריאת פונקציות. זה הופך אותו לייחודי כאחד המודלים הראשונים בקוד פתוח שעושה זאת.

### השוואת טוקניזרים

בדוגמה זו, נבחן כיצד Mistral NeMo מתמודד עם טוקניזציה לעומת Mistral Large.

שני הדוגמאות לוקחות את אותה בקשה אבל אתה אמור לראות ש-NeMo מחזיר פחות טוקנים לעומת Mistral Large.

```bash
pip install mistral-common
```

```python 
# Import needed packages:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Load Mistral tokenizer

model_name = "open-mistral-nemo	"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenize a list of messages
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
                                "description": "The temperature unit to use. Infer this from the users location.",
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

# Count the number of tokens
print(len(tokens))
```

```python
# Import needed packages:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Load Mistral tokenizer

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenize a list of messages
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
                                "description": "The temperature unit to use. Infer this from the users location.",
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

# Count the number of tokens
print(len(tokens))
```

## הלמידה לא עוצרת כאן, המשך המסע

לאחר סיום השיעור הזה, בדוק את [אוסף הלמידה של AI יצירתי](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) שלנו כדי להמשיך לשפר את הידע שלך ב-AI יצירתי!

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). בעוד אנו שואפים לדיוק, אנא היו מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. למידע קריטי, מומלץ תרגום אנושי מקצועי. אנו לא אחראים לאי הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.