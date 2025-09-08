<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T19:01:54+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "vi"
}
-->
# Xây dựng với các Mô hình Mistral

## Giới thiệu

Bài học này sẽ bao gồm:  
- Khám phá các mô hình Mistral khác nhau  
- Hiểu các trường hợp sử dụng và kịch bản cho từng mô hình  
- Các ví dụ mã minh họa các tính năng đặc trưng của từng mô hình.

## Các Mô hình Mistral

Trong bài học này, chúng ta sẽ khám phá 3 mô hình Mistral khác nhau:  
**Mistral Large**, **Mistral Small** và **Mistral Nemo**.

Mỗi mô hình này đều có sẵn miễn phí trên Github Model marketplace. Mã trong notebook này sẽ sử dụng các mô hình đó để chạy. Dưới đây là thêm thông tin về cách sử dụng Github Models để [phát triển nguyên mẫu với các mô hình AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)

Mistral Large 2 hiện là mô hình chủ lực của Mistral và được thiết kế cho mục đích doanh nghiệp.

Mô hình này là bản nâng cấp của Mistral Large ban đầu với các điểm nổi bật:  
- Cửa sổ ngữ cảnh lớn hơn - 128k so với 32k  
- Hiệu suất tốt hơn trong các tác vụ Toán học và Lập trình - độ chính xác trung bình 76.9% so với 60.4%  
- Hiệu suất đa ngôn ngữ được cải thiện - bao gồm các ngôn ngữ: Tiếng Anh, Pháp, Đức, Tây Ban Nha, Ý, Bồ Đào Nha, Hà Lan, Nga, Trung Quốc, Nhật, Hàn, Ả Rập và Hindi.

Với những tính năng này, Mistral Large nổi bật trong các lĩnh vực:  
- *Retrieval Augmented Generation (RAG)* - nhờ cửa sổ ngữ cảnh lớn hơn  
- *Function Calling* - mô hình này có khả năng gọi hàm gốc, cho phép tích hợp với các công cụ và API bên ngoài. Các cuộc gọi này có thể thực hiện song song hoặc tuần tự.  
- *Code Generation* - mô hình này rất mạnh trong việc tạo mã Python, Java, TypeScript và C++.

### Ví dụ RAG sử dụng Mistral Large 2

Trong ví dụ này, chúng ta sử dụng Mistral Large 2 để chạy mô hình RAG trên một tài liệu văn bản. Câu hỏi được viết bằng tiếng Hàn và hỏi về các hoạt động của tác giả trước khi vào đại học.

Mô hình sử dụng Cohere Embeddings để tạo embeddings cho tài liệu văn bản cũng như câu hỏi. Trong ví dụ này, gói Python faiss được dùng làm kho vector.

Lời nhắc gửi đến mô hình Mistral bao gồm cả câu hỏi và các đoạn văn bản được truy xuất có nội dung tương tự câu hỏi. Mô hình sau đó trả về câu trả lời bằng ngôn ngữ tự nhiên.

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

Mistral Small là một mô hình khác trong gia đình Mistral thuộc nhóm premier/enterprise. Như tên gọi, đây là một Mô hình Ngôn ngữ Nhỏ (SLM). Ưu điểm khi sử dụng Mistral Small là:  
- Tiết kiệm chi phí so với các LLM của Mistral như Mistral Large và NeMo - giảm giá khoảng 80%  
- Độ trễ thấp - phản hồi nhanh hơn so với các LLM của Mistral  
- Linh hoạt - có thể triển khai trên nhiều môi trường khác nhau với yêu cầu tài nguyên thấp hơn.

Mistral Small rất phù hợp cho:  
- Các tác vụ dựa trên văn bản như tóm tắt, phân tích cảm xúc và dịch thuật.  
- Ứng dụng có tần suất yêu cầu cao nhờ chi phí hiệu quả  
- Các tác vụ mã có độ trễ thấp như xem xét và gợi ý mã.

## So sánh Mistral Small và Mistral Large

Để thấy sự khác biệt về độ trễ giữa Mistral Small và Large, hãy chạy các ô lệnh dưới đây.

Bạn sẽ thấy sự chênh lệch thời gian phản hồi khoảng 3-5 giây. Đồng thời lưu ý độ dài và phong cách câu trả lời trên cùng một lời nhắc.

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

So với hai mô hình khác được đề cập trong bài học này, Mistral NeMo là mô hình duy nhất miễn phí với giấy phép Apache2.

Nó được xem là bản nâng cấp của mô hình mã nguồn mở trước đó của Mistral, Mistral 7B.

Một số tính năng khác của mô hình NeMo bao gồm:

- *Tokenization hiệu quả hơn:* Mô hình này sử dụng bộ phân tách Tekken thay vì tiktoken phổ biến hơn. Điều này giúp cải thiện hiệu suất trên nhiều ngôn ngữ và mã nguồn.

- *Finetuning:* Mô hình cơ sở có thể được tinh chỉnh thêm. Điều này mang lại sự linh hoạt hơn cho các trường hợp cần tinh chỉnh mô hình.

- *Native Function Calling* - Giống như Mistral Large, mô hình này được huấn luyện để gọi hàm. Điều này làm cho nó trở thành một trong những mô hình mã nguồn mở đầu tiên có tính năng này.

### So sánh Tokenizers

Trong ví dụ này, chúng ta sẽ xem cách Mistral NeMo xử lý tokenization so với Mistral Large.

Cả hai ví dụ đều sử dụng cùng một lời nhắc, nhưng bạn sẽ thấy NeMo trả về ít token hơn so với Mistral Large.

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

## Học tập không dừng lại ở đây, tiếp tục hành trình

Sau khi hoàn thành bài học này, hãy khám phá bộ sưu tập [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức về Generative AI!

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.