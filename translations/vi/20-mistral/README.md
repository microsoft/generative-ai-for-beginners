# Xây dựng với các Mô hình Mistral

## Giới thiệu

Bài học này sẽ bao gồm:
- Khám phá các mô hình Mistral khác nhau
- Hiểu các trường hợp sử dụng và kịch bản cho từng mô hình
- Khám phá các ví dụ mã cho thấy các tính năng độc đáo của từng mô hình.

## Các Mô hình Mistral

Trong bài học này, chúng ta sẽ khám phá 3 mô hình Mistral khác nhau:
**Mistral Large**, **Mistral Small** và **Mistral Nemo**.

Mỗi mô hình này đều có sẵn miễn phí trên GitHub Model marketplace. Mã trong sổ tay này sẽ sử dụng các mô hình này để chạy mã. Dưới đây là thêm chi tiết về việc sử dụng GitHub Models để [nguyên mẫu với các mô hình AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Mistral Large 2 hiện là mô hình chủ lực của Mistral và được thiết kế cho mục đích doanh nghiệp.

Mô hình này là bản nâng cấp so với Mistral Large gốc bằng cách cung cấp
- Cửa sổ ngữ cảnh lớn hơn - 128k so với 32k
- Hiệu suất tốt hơn trong các nhiệm vụ Toán học và Lập trình - độ chính xác trung bình 76,9% so với 60,4%
- Hiệu suất đa ngôn ngữ tăng cường - các ngôn ngữ bao gồm: tiếng Anh, tiếng Pháp, tiếng Đức, tiếng Tây Ban Nha, tiếng Ý, tiếng Bồ Đào Nha, tiếng Hà Lan, tiếng Nga, tiếng Trung Quốc, tiếng Nhật, tiếng Hàn, tiếng Ả Rập và tiếng Hindi.

Với những tính năng này, Mistral Large nổi bật ở
- *Tạo nội dung tăng cường truy xuất (RAG)* - nhờ cửa sổ ngữ cảnh lớn hơn
- *Gọi chức năng* - mô hình này có chức năng gọi hàm bản địa cho phép tích hợp với các công cụ và API bên ngoài. Các cuộc gọi này có thể thực hiện đồng thời hoặc tuần tự từng cái một.
- *Tạo mã* - mô hình này nổi bật trong việc tạo mã Python, Java, TypeScript và C++.

### Ví dụ RAG sử dụng Mistral Large 2

Trong ví dụ này, chúng ta sử dụng Mistral Large 2 để chạy mô hình RAG trên một tài liệu văn bản. Câu hỏi được viết bằng tiếng Hàn và hỏi về các hoạt động của tác giả trước khi vào đại học.

Nó sử dụng Mô hình Nhúng Cohere để tạo nhúng của tài liệu văn bản cũng như câu hỏi. Đối với ví dụ này, nó sử dụng gói Python faiss làm kho vector.

Lời nhắc gửi tới mô hình Mistral bao gồm cả câu hỏi và các đoạn văn được lấy ra tương tự như câu hỏi. Mô hình sau đó trả lời bằng ngôn ngữ tự nhiên.

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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # khoảng cách, chỉ mục
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
Mistral Small là một mô hình khác trong gia đình Mistral thuộc loại mô hình cao cấp/doanh nghiệp. Như tên gọi, đây là một Mô hình Ngôn ngữ Nhỏ (SLM). Ưu điểm của việc sử dụng Mistral Small là:
- Tiết kiệm chi phí so với các LLM Mistral như Mistral Large và NeMo - giảm giá 80%
- Độ trễ thấp - phản hồi nhanh hơn so với các LLM của Mistral
- Linh hoạt - có thể triển khai trên nhiều môi trường khác nhau với ít yêu cầu về tài nguyên hơn.

Mistral Small rất tốt cho:
- Các nhiệm vụ dựa trên văn bản như tóm tắt, phân tích cảm xúc và dịch thuật.
- Ứng dụng có yêu cầu truy cập thường xuyên nhờ hiệu quả về chi phí
- Các nhiệm vụ liên quan đến mã có độ trễ thấp như xem xét và gợi ý mã

## So sánh Mistral Small và Mistral Large

Để thấy sự khác biệt về độ trễ giữa Mistral Small và Large, hãy chạy các ô bên dưới.

Bạn sẽ thấy khác biệt về thời gian phản hồi trong khoảng 3-5 giây. Ngoài ra, hãy chú ý đến độ dài và phong cách trả lời trên cùng một lời nhắc.

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

So với hai mô hình khác được thảo luận trong bài học này, Mistral NeMo là mô hình duy nhất miễn phí và có giấy phép Apache2.

Nó được xem như một bản nâng cấp của LLM mã nguồn mở trước đó từ Mistral, Mistral 7B.

Một vài điểm nổi bật khác của mô hình NeMo là:

- *Phân tách token hiệu quả hơn:* Mô hình này dùng bộ phân tách token Tekken thay cho tiktoken thường thấy. Điều này cho phép hiệu suất tốt hơn với nhiều ngôn ngữ và mã hơn.

- *Tinh chỉnh:* Mô hình cơ sở có sẵn để tinh chỉnh. Điều này giúp linh hoạt hơn cho các trường hợp sử dụng cần tinh chỉnh.

- *Gọi chức năng bản địa* - Giống như Mistral Large, mô hình này đã được đào tạo gọi hàm. Điều này làm cho nó trở nên độc đáo khi là một trong những mô hình mã nguồn mở đầu tiên làm được điều này.

### So sánh bộ phân tách token

Trong ví dụ này, chúng ta sẽ xem cách Mistral NeMo xử lý phân tách token so với Mistral Large.

Cả hai ví dụ đều sử dụng cùng một lời nhắc nhưng bạn sẽ thấy NeMo trả về ít token hơn Mistral Large.

```bash
pip install mistral-common
```

```python 
# Nhập các gói cần thiết:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Tải bộ mã hóa Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Mã hóa một danh sách tin nhắn
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

# Đếm số lượng token
print(len(tokens))
```

```python
# Nhập khẩu các gói cần thiết:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Tải bộ mã hóa Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Mã hóa danh sách các tin nhắn
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

# Đếm số lượng token
print(len(tokens))
```

## Học tập không dừng lại ở đây, tiếp tục hành trình

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Học tập AI Tạo sinh của chúng tôi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) để tiếp tục nâng cao kiến thức về AI Tạo sinh của bạn!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được xem là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu nhầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->