<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:19:20+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "he"
}
-->
# בנייה עם מודלים של מיסטרל

## מבוא

בשיעור זה נעסוק ב:
- חקר המודלים השונים של מיסטרל
- הבנת מקרי השימוש והתרחישים לכל מודל
- דוגמאות קוד המדגימות את התכונות הייחודיות של כל מודל.

## מודלי מיסטרל

בשיעור זה נחקור 3 מודלים שונים של מיסטרל: **Mistral Large**, **Mistral Small** ו-**Mistral Nemo**.

כל אחד מהמודלים הללו זמין בחינם בשוק המודלים של Github. הקוד במחברת זו ישתמש במודלים אלה כדי להפעיל את הקוד. הנה פרטים נוספים על השימוש במודלים של Github ל[אב-טיפוס עם מודלים של AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## מיסטרל לארג' 2 (2407)
Mistral Large 2 הוא כיום המודל המוביל של מיסטרל ומיועד לשימוש ארגוני.

המודל הוא שדרוג למודל המקורי Mistral Large על ידי הצעת:
- חלון הקשר גדול יותר - 128k לעומת 32k
- ביצועים טובים יותר במשימות מתמטיקה וקידוד - 76.9% דיוק ממוצע לעומת 60.4%
- ביצועים רב-לשוניים מוגברים - השפות כוללות: אנגלית, צרפתית, גרמנית, ספרדית, איטלקית, פורטוגזית, הולנדית, רוסית, סינית, יפנית, קוריאנית, ערבית והינדית.

עם תכונות אלה, Mistral Large מצטיין ב:
- *יצירת מידע מוגברת על ידי שליפה (RAG)* - הודות לחלון ההקשר הגדול יותר
- *קריאה לפונקציות* - למודל זה יש קריאה לפונקציות מובנית המאפשרת אינטגרציה עם כלים ו-API חיצוניים. ניתן לבצע קריאות אלו במקביל או אחת אחרי השנייה בסדר רציף.
- *יצירת קוד* - מודל זה מצטיין ביצירת קוד ב-Python, Java, TypeScript ו-C++.

### דוגמת RAG באמצעות Mistral Large 2

בדוגמה זו, אנו משתמשים ב-Mistral Large 2 כדי להפעיל תבנית RAG על מסמך טקסט. השאלה נכתבת בקוריאנית ושואלת על הפעילויות של המחבר לפני הקולג'.

הוא משתמש במודל Cohere Embeddings ליצירת הטמעות של מסמך הטקסט וגם של השאלה. לדוגמה זו, הוא משתמש בחבילת הפייתון faiss כחנות וקטורים.

ההנחיה שנשלחת למודל מיסטרל כוללת גם את השאלות וגם את החלקים שנשלפו שדומים לשאלה. המודל מספק לאחר מכן תגובה בשפה טבעית.

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

## מיסטרל סמול
Mistral Small הוא מודל נוסף במשפחת המודלים של מיסטרל תחת הקטגוריה היוקרתית/ארגונית. כפי שמרמז השם, מודל זה הוא מודל שפה קטן (SLM). היתרונות בשימוש ב-Mistral Small הם:
- חיסכון בעלויות בהשוואה ל-LLM של מיסטרל כמו Mistral Large ו-NeMo - ירידה של 80% במחיר
- זמן תגובה נמוך - תגובה מהירה יותר בהשוואה ל-LLM של מיסטרל
- גמישות - ניתן לפרוס בסביבות שונות עם פחות מגבלות על משאבים נדרשים.

Mistral Small מתאים ל:
- משימות מבוססות טקסט כמו סיכום, ניתוח רגשות ותרגום.
- יישומים שבהם נעשות בקשות תכופות בשל יעילות העלות שלו
- משימות קוד בעלות זמן תגובה נמוך כמו סקירה והצעות קוד

## השוואה בין Mistral Small ל-Mistral Large

כדי להראות את ההבדלים בזמן התגובה בין Mistral Small ל-Large, הפעל את התאים הבאים.

אתם אמורים לראות הבדל בזמני התגובה בין 3-5 שניות. שימו לב גם לאורך וסגנון התגובות לאותה הנחיה.

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

## מיסטרל נמו

בהשוואה לשני המודלים האחרים שנדונו בשיעור זה, Mistral NeMo הוא המודל החינמי היחיד עם רישיון Apache2.

הוא נתפס כשדרוג ל-LLM הפתוח הקודם של מיסטרל, Mistral 7B.

תכונות נוספות של מודל NeMo כוללות:

- *קידוד יעיל יותר:* מודל זה משתמש במקודד Tekken במקום המקודד הנפוץ יותר tiktoken. זה מאפשר ביצועים טובים יותר ביותר שפות וקודים.

- *כיוונון עדין:* המודל הבסיסי זמין לכיוונון עדין. זה מאפשר יותר גמישות למקרי שימוש שבהם ייתכן ויידרש כיוונון עדין.

- *קריאה לפונקציות מובנית* - כמו Mistral Large, מודל זה אומן על קריאה לפונקציות. זה הופך אותו לייחודי כאחד המודלים הפתוחים הראשונים שעושים זאת.

### השוואת מקודדים

בדוגמה זו, נבחן כיצד Mistral NeMo מתמודד עם קידוד בהשוואה ל-Mistral Large.

שני הדוגמאות לוקחות את אותה הנחיה אך אתם אמורים לראות ש-NeMo מחזיר פחות טוקנים בהשוואה ל-Mistral Large.

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

## הלמידה לא נגמרת כאן, המשיכו את המסע

לאחר השלמת השיעור הזה, עיינו באוסף [למידת AI גנרטיבית](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) שלנו כדי להמשיך ולשפר את הידע שלכם ב-AI גנרטיבי!

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). בעוד אנו שואפים לדיוק, אנא היו מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. יש להתייחס למסמך המקורי בשפתו המקורית כמקור סמכותי. עבור מידע קריטי, מומלץ תרגום מקצועי אנושי. אנו לא נושאים באחריות לכל אי הבנה או פירוש שגוי הנובע משימוש בתרגום זה.