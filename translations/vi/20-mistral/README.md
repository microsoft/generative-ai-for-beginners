<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:19:41+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "vi"
}
-->
# Xây dựng với Mô hình Mistral

## Giới thiệu

Bài học này sẽ bao gồm:
- Khám phá các mô hình Mistral khác nhau
- Hiểu các trường hợp sử dụng và tình huống cho từng mô hình
- Mẫu mã cho thấy các đặc điểm độc đáo của từng mô hình.

## Các Mô hình Mistral

Trong bài học này, chúng ta sẽ khám phá 3 mô hình Mistral khác nhau: **Mistral Large**, **Mistral Small** và **Mistral Nemo**.

Mỗi mô hình này đều có sẵn miễn phí trên thị trường Model của Github. Mã trong notebook này sẽ sử dụng các mô hình này để chạy mã. Dưới đây là chi tiết về việc sử dụng Github Models để [tạo mẫu với mô hình AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)

Mistral Large 2 hiện là mô hình hàng đầu từ Mistral và được thiết kế cho sử dụng trong doanh nghiệp.

Mô hình này là một bản nâng cấp từ Mistral Large ban đầu bằng cách cung cấp
- Cửa sổ ngữ cảnh lớn hơn - 128k so với 32k
- Hiệu suất tốt hơn trong các nhiệm vụ Toán học và Lập trình - độ chính xác trung bình 76.9% so với 60.4%
- Hiệu suất đa ngôn ngữ tăng lên - các ngôn ngữ bao gồm: Tiếng Anh, Tiếng Pháp, Tiếng Đức, Tiếng Tây Ban Nha, Tiếng Ý, Tiếng Bồ Đào Nha, Tiếng Hà Lan, Tiếng Nga, Tiếng Trung, Tiếng Nhật, Tiếng Hàn, Tiếng Ả Rập, và Tiếng Hindi.

Với những đặc điểm này, Mistral Large vượt trội trong
- *Retrieval Augmented Generation (RAG)* - nhờ cửa sổ ngữ cảnh lớn hơn
- *Gọi hàm* - mô hình này có khả năng gọi hàm gốc cho phép tích hợp với các công cụ và API bên ngoài. Các cuộc gọi này có thể được thực hiện song song hoặc tuần tự.
- *Tạo mã* - mô hình này xuất sắc trong việc tạo mã Python, Java, TypeScript và C++.

### Ví dụ RAG sử dụng Mistral Large 2

Trong ví dụ này, chúng ta đang sử dụng Mistral Large 2 để chạy một mẫu RAG trên một tài liệu văn bản. Câu hỏi được viết bằng tiếng Hàn và hỏi về hoạt động của tác giả trước khi vào đại học.

Nó sử dụng Cohere Embeddings Model để tạo các embeddings của tài liệu văn bản cũng như câu hỏi. Trong mẫu này, nó sử dụng gói faiss Python làm kho lưu trữ vector.

Đề xuất gửi đến mô hình Mistral bao gồm cả câu hỏi và các đoạn văn bản được truy xuất tương tự với câu hỏi. Mô hình sau đó cung cấp một phản hồi bằng ngôn ngữ tự nhiên.

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

Mistral Small là một mô hình khác trong gia đình mô hình Mistral thuộc danh mục hàng đầu/doanh nghiệp. Như tên gọi, mô hình này là một Mô hình Ngôn ngữ Nhỏ (SLM). Các lợi ích của việc sử dụng Mistral Small là:
- Tiết kiệm chi phí so với các LLM của Mistral như Mistral Large và NeMo - giảm giá 80%
- Độ trễ thấp - phản hồi nhanh hơn so với các LLM của Mistral
- Linh hoạt - có thể triển khai trên nhiều môi trường khác nhau với ít hạn chế về tài nguyên yêu cầu.

Mistral Small rất tốt cho:
- Các nhiệm vụ dựa trên văn bản như tóm tắt, phân tích cảm xúc và dịch thuật.
- Các ứng dụng nơi yêu cầu thường xuyên được thực hiện do tính hiệu quả về chi phí
- Nhiệm vụ mã có độ trễ thấp như đánh giá và gợi ý mã

## So sánh Mistral Small và Mistral Large

Để cho thấy sự khác biệt về độ trễ giữa Mistral Small và Large, hãy chạy các ô dưới đây.

Bạn sẽ thấy sự khác biệt về thời gian phản hồi từ 3-5 giây. Cũng lưu ý độ dài và phong cách phản hồi trên cùng một đề xuất.

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

So với hai mô hình khác được thảo luận trong bài học này, Mistral NeMo là mô hình miễn phí duy nhất với Giấy phép Apache2.

Nó được xem như một bản nâng cấp từ LLM nguồn mở trước đó từ Mistral, Mistral 7B.

Một số đặc điểm khác của mô hình NeMo là:

- *Tokenization hiệu quả hơn:* Mô hình này sử dụng bộ token Tekken thay vì tiktoken thường được sử dụng. Điều này cho phép hiệu suất tốt hơn trên nhiều ngôn ngữ và mã.

- *Tùy chỉnh:* Mô hình cơ bản có sẵn để tùy chỉnh. Điều này cho phép linh hoạt hơn cho các trường hợp sử dụng nơi cần tùy chỉnh.

- *Gọi hàm gốc* - Giống như Mistral Large, mô hình này đã được đào tạo trên việc gọi hàm. Điều này làm cho nó trở nên độc đáo khi là một trong những mô hình nguồn mở đầu tiên làm điều này.

### So sánh các Tokenizers

Trong mẫu này, chúng ta sẽ xem cách Mistral NeMo xử lý tokenization so với Mistral Large.

Cả hai mẫu đều sử dụng cùng một đề xuất nhưng bạn sẽ thấy rằng NeMo trả về ít token hơn so với Mistral Large.

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

Sau khi hoàn thành bài học này, hãy khám phá bộ sưu tập [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) để tiếp tục nâng cao kiến thức về Generative AI của bạn!

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.