# בנייה עם דגמי Mistral

## מבוא

שיעור זה יכסה:
- חקר הדגמים השונים של Mistral
- הבנת מקרים ושימושים לכל דגם
- חקר דוגמאות קוד המראות את התכונות הייחודיות של כל דגם.

## דגמי Mistral

בשיעור זה נחקור 3 דגמי Mistral שונים:
**Mistral Large**, **Mistral Small** ו-**Mistral Nemo**.

כל אחד מהדגמים הללו זמין בחינם בשוק הדגמים של GitHub. הקוד במחברת זו ישתמש בדגמים אלו להרצת הקוד. הנה פרטים נוספים על שימוש בדגמי GitHub כדי [לבצע אב-טיפוס עם מודלים של AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 הוא כיום הדגם הדגל של Mistral ומיועד לשימוש ארגוני.

הדגם הוא שדרוג ל-Mistral Large המקורי ומציע
- חלון הקשר גדול יותר - 128k לעומת 32k
- ביצועים טובים יותר במשימות מתמטיקה וקידוד - 76.9% דיוק ממוצע לעומת 60.4%
- ביצועים מוגברים בריבוי שפות - שפות כוללות: אנגלית, צרפתית, גרמנית, ספרדית, איטלקית, פורטוגזית, הולנדית, רוסית, סינית, יפנית, קוריאנית, ערבית והינדי.

עם התכונות הללו, Mistral Large מצטיין ב
- *יצירת תוכן מוגבר בהסתמך על אחזור (RAG)* - בזכות חלון ההקשר הגדול יותר
- *קריאת פונקציות* - דגם זה כולל קריאת פונקציות מובנית המאפשרת אינטגרציה עם כלים ו-API חיצוניים. ניתן לבצע קריאות אלו גם במקביל או אחת אחרי השנייה בסדר רציף.
- *יצירת קוד* - דגם זה מצטיין ביצירה של קוד בפייתון, ג'אווה, TypeScript ו-C++.

### דוגמה ל-RAG עם Mistral Large 2

בדוגמה זו, אנו משתמשים ב-Mistral Large 2 להרצת תבנית RAG על מסמך טקסט. השאלה נכתבת בקוריאנית ושואלת על פעילויות המחבר לפני המכללה.

המערכת משתמשת בדגם Embeddings של Cohere ליצירת אמבדינגים של מסמך הטקסט וכן של השאלה. לדוגמה זו, נעשה שימוש בחבילת faiss של פייתון כאחסון וקטורי.

הפירומפט שנשלח אל דגם Mistral כולל הן את השאלות והן את הקטעים שהוחזרו וקרובים לשאלה. הדגם מספק לאחר מכן תגובה בשפה טבעית.

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
Mistral Small הוא דגם נוסף במשפחת דגמי Mistral תחת הקטגוריה הפרמייר/ארגונית. כפי שהשם מרמז, דגם זה הוא מודל שפה קטן (SLM). היתרונות של שימוש ב-Mistral Small הם:
- חיסכון בעלויות לעומת דגמי LLM של Mistral כמו Mistral Large ו-NeMo - ירידה של 80% במחיר
- זמן תגובה נמוך - תגובה מהירה יותר לעומת דגמי LLM של Mistral
- גמישות - ניתן לפרוס בסביבות שונות עם פחות מגבלות על משאבים נדרשים.

Mistral Small מצוין עבור:
- משימות מבוססות טקסט כגון סיכום, ניתוח סנטימנט ותירגום
- יישומים בהם נעשות בקשות תכופות בזכות יעילות עלות
- משימות קוד עם זמן תגובה נמוך כמו סקירה והצעות לקוד

## השוואה בין Mistral Small ל-Mistral Large

כדי להראות הבדלים בזמן תגובה בין Mistral Small ל-Mistral Large, הרץ את התאים הבאים.

עליך לראות הבדל בזמן תגובה בין 3-5 שניות. שים לב גם לאורך התגובות והסגנון על אותו פירומפט.

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

בהשוואה לשני הדגמים האחרים שנדונו בשיעור זה, Mistral NeMo הוא הדגם היחיד הזמין בחינם ברישיון Apache2.

הוא נחשב לשדרוג לדגם הקוד הפתוח הקודם של Mistral, Mistral 7B.

כמה תכונות נוספות של דגם NeMo הן:

- *טוקניזציה יעילה יותר:* דגם זה משתמש בטוקניזר Tekken במקום ב-tiktoken הנפוץ יותר. זה מאפשר ביצועים טובים יותר על מגוון שפות וקוד.

- *כיוונון עדין:* הדגם הבסיסי זמין לכיוונון עדין. זה מאפשר גמישות רבה יותר במקרים בהם יש צורך בכיוונון נוסף.

- *קריאת פונקציות מובנית* - בדומה ל-Mistral Large, דגם זה עבר אימון על קריאת פונקציות. זה ייחודי בכך שהוא אחד מהדגמים הפתוחים הראשונים שעושים זאת.

### השוואת טוקניזרים

בדוגמה זו, נבחן כיצד Mistral NeMo מטפל בטוקניזציה בהשוואה ל-Mistral Large.

שתי הדוגמאות לוקחות את אותו הפירומפט אך תראה כי NeMo מחזיר פחות טוקנים לעומת Mistral Large.

```bash
pip install mistral-common
```

```python 
# ייבא חבילות נחוצות:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# טען את מימוש מיסטרל

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# בצע טוקניזציה לרשימת הודעות
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
# ייבוא חבילות נדרשות:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# טעינת מְפַרְקֵד מיסטרל

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# פירוק לרצועות רשימת הודעות
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

# ספירת מספר הרצועות
print(len(tokens))
```

## הלמידה אינה מסתיימת כאן, המשך במסע

לאחר השלמת שיעור זה, בדוק את קבוצת הלמידה שלנו ל-[למידה בינה מלאכותית גנרטיבית](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) כדי להמשיך ולשפר את הידע שלך בבינה מלאכותית גנרטיבית!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי־דיוקים. המסמך המקורי בשפת המקור שלו הוא המקור הרשמי והמהימן. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. איננו אחראים לשום אי הבנה או פרשנות מוטעית הנובעת משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->