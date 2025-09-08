<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T19:01:41+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "he"
}
-->
# בנייה עם דגמי Mistral

## מבוא

בשיעור זה נסקור:  
- חקירת דגמי Mistral השונים  
- הבנת מקרי השימוש והתסריטים לכל דגם  
- דוגמאות קוד שמדגימות את התכונות הייחודיות של כל דגם.

## דגמי Mistral

בשיעור זה נבחן 3 דגמי Mistral שונים:  
**Mistral Large**, **Mistral Small** ו-**Mistral Nemo**.

כל אחד מהדגמים הללו זמין בחינם בשוק הדגמים של Github. הקוד במחברת זו ישתמש בדגמים אלו להרצת הקוד. להלן פרטים נוספים על שימוש בדגמי Github ל[פרוטוטייפ עם דגמי AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)  
Mistral Large 2 הוא כיום הדגם המוביל של Mistral ומיועד לשימוש ארגוני.

הדגם הוא שדרוג ל-Mistral Large המקורי ומציע:  
- חלון הקשר גדול יותר - 128k לעומת 32k  
- ביצועים טובים יותר במשימות מתמטיקה וקידוד - דיוק ממוצע של 76.9% לעומת 60.4%  
- ביצועים משופרים בריבוי שפות - כולל: אנגלית, צרפתית, גרמנית, ספרדית, איטלקית, פורטוגזית, הולנדית, רוסית, סינית, יפנית, קוריאנית, ערבית והינדי.

עם תכונות אלו, Mistral Large מצטיין ב:  
- *Retrieval Augmented Generation (RAG)* - בזכות חלון ההקשר הגדול יותר  
- *Function Calling* - לדגם זה יש קריאות פונקציה מובנות המאפשרות אינטגרציה עם כלים ו-APIs חיצוניים. קריאות אלו יכולות להתבצע במקביל או ברצף.  
- *יצירת קוד* - הדגם מצטיין ביצירת קוד ב-Python, Java, TypeScript ו-C++.

### דוגמה ל-RAG עם Mistral Large 2

בדוגמה זו אנו משתמשים ב-Mistral Large 2 להרצת דפוס RAG על מסמך טקסט. השאלה כתובה בקוריאנית ושואלת על פעילויות המחבר לפני הקולג'.

הדגם משתמש ב-Cohere Embeddings Model ליצירת אמבדינגים של מסמך הטקסט ושל השאלה. בדוגמה זו נעשה שימוש בחבילת faiss בפייתון כאחסון וקטורי.

הפרומפט שנשלח לדגם Mistral כולל גם את השאלות וגם את הקטעים שהוחזרו הדומים לשאלה. הדגם מספק תגובה בשפה טבעית.

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
Mistral Small הוא דגם נוסף ממשפחת Mistral תחת קטגוריית הפרימיום/ארגוני. כפי שהשם מרמז, זהו דגם שפת קטן (SLM). היתרונות בשימוש ב-Mistral Small הם:  
- חיסכון בעלויות לעומת דגמי Mistral LLM כמו Mistral Large ו-NeMo - ירידה של 80% במחיר  
- זמן תגובה נמוך - מהיר יותר לעומת דגמי Mistral LLM  
- גמישות - ניתן לפרוס אותו בסביבות שונות עם פחות הגבלות על משאבים נדרשים.

Mistral Small מתאים במיוחד ל:  
- משימות מבוססות טקסט כמו סיכום, ניתוח סנטימנט ותרגום  
- יישומים עם בקשות תכופות בזכות עלות-תועלת גבוהה  
- משימות קוד עם זמן תגובה נמוך כמו סקירה והצעות קוד

## השוואה בין Mistral Small ל-Mistral Large

כדי להראות את ההבדלים בזמן התגובה בין Mistral Small ל-Large, הריצו את התאים הבאים.

תוכלו לראות הבדל בזמני התגובה של בין 3 ל-5 שניות. שימו לב גם לאורך התגובות והסגנון על אותו פרומפט.

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

בהשוואה לשני הדגמים האחרים שנדונו בשיעור זה, Mistral NeMo הוא הדגם החינמי היחיד עם רישיון Apache2.

הוא נחשב לשדרוג לדגם הקוד הפתוח הקודם של Mistral, Mistral 7B.

כמה תכונות נוספות של דגם NeMo הן:

- *טוקניזציה יעילה יותר:* דגם זה משתמש בטוקניזר Tekken במקום ב-tiktoken הנפוץ יותר. זה מאפשר ביצועים טובים יותר בשפות ובקוד שונים.

- *פיינטונינג:* הדגם הבסיסי זמין לפיינטונינג, מה שמאפשר גמישות רבה יותר במקרי שימוש שבהם נדרש פיינטונינג.

- *קריאות פונקציה מובנות* - בדומה ל-Mistral Large, דגם זה עבר אימון על קריאות פונקציה. זה הופך אותו לייחודי כאחד הדגמים הפתוחים הראשונים שעושים זאת.

### השוואת טוקניזרים

בדוגמה זו נבחן כיצד Mistral NeMo מטפל בטוקניזציה בהשוואה ל-Mistral Large.

שני הדגמים מקבלים את אותו הפרומפט, אך תראו כי NeMo מחזיר פחות טוקנים לעומת Mistral Large.

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

## הלמידה לא נעצרת כאן, המשיכו במסע

לאחר שסיימתם את השיעור, בדקו את [אוסף הלמידה של Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) שלנו כדי להמשיך ולשפר את הידע שלכם ב-Generative AI!

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.