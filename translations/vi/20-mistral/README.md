# Xây dựng với các Mô hình Mistral 

## Giới thiệu 

Bài học này sẽ bao gồm: 
- Khám phá các mô hình Mistral khác nhau 
- Hiểu các trường hợp sử dụng và kịch bản cho từng mô hình 
- Khám phá các ví dụ mã nguồn thể hiện các tính năng độc đáo của từng mô hình. 

## Các Mô hình Mistral 

Trong bài học này, chúng ta sẽ khám phá 3 mô hình Mistral khác nhau: 
**Mistral Large**, **Mistral Small** và **Mistral Nemo**. 

Mỗi mô hình này đều có sẵn miễn phí trên [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Mã trong sổ tay này sẽ sử dụng các mô hình đó để chạy mã.

> **Lưu ý:** GitHub Models sẽ ngừng hoạt động vào cuối tháng 7 năm 2026. Dưới đây là thêm thông tin về cách sử dụng [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) để thiết kế mẫu với các mô hình AI. 


## Mistral Large 2 (2407)
Mistral Large 2 hiện là mô hình chủ lực từ Mistral và được thiết kế cho doanh nghiệp. 

Mô hình này là bản nâng cấp của Mistral Large ban đầu với: 
- Cửa sổ ngữ cảnh lớn hơn - 128k so với 32k 
- Hiệu suất tốt hơn trên các bài toán Toán và Lập trình - độ chính xác trung bình 76,9% so với 60,4% 
- Nâng cao hiệu suất đa ngôn ngữ - bao gồm các ngôn ngữ: Tiếng Anh, Pháp, Đức, Tây Ban Nha, Ý, Bồ Đào Nha, Hà Lan, Nga, Trung Quốc, Nhật Bản, Hàn Quốc, Ả Rập và Hindi.

Với các tính năng này, Mistral Large nổi bật tại: 
- *Sinh văn bản tăng cường truy hồi (RAG)* - do cửa sổ ngữ cảnh lớn hơn
- *Gọi hàm* - mô hình này có khả năng gọi hàm gốc cho phép tích hợp với các công cụ và API bên ngoài. Các cuộc gọi này có thể thực hiện đồng thời hoặc tuần tự nối tiếp. 
- *Sinh mã* - mô hình này nổi bật với sinh mã Python, Java, TypeScript và C++. 

### Ví dụ RAG sử dụng Mistral Large 2 

Trong ví dụ này, chúng ta sử dụng Mistral Large 2 để chạy mẫu RAG trên tài liệu văn bản. Câu hỏi được viết bằng tiếng Hàn và hỏi về các hoạt động của tác giả trước khi vào đại học. 

Nó sử dụng mô hình Nhúng Cohere để tạo các nhúng của tài liệu văn bản cũng như câu hỏi. Với mẫu này, nó sử dụng gói faiss Python làm kho vector. 

Lời nhắc gửi đến mô hình Mistral bao gồm cả các câu hỏi và các đoạn được lấy ra tương tự với câu hỏi. Sau đó, Mô hình đưa ra phản hồi ngôn ngữ tự nhiên. 

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

# Lấy những cái này từ trang "Tổng quan" của dự án Microsoft Foundry của bạn
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # khoảng cách, chỉ số
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
Mistral Small là một mô hình khác trong dòng Mistral thuộc loại mô hình hạng nhất/doanh nghiệp. Như tên gọi, đây là một Mô hình Ngôn ngữ Nhỏ (SLM). Ưu điểm của việc sử dụng Mistral Small là: 
- Tiết kiệm chi phí so với các LLM Mistral như Mistral Large và NeMo - giảm giá 80%
- Độ trễ thấp - phản hồi nhanh hơn so với các LLM của Mistral
- Linh hoạt - có thể triển khai trên nhiều môi trường khác nhau với ít giới hạn về tài nguyên cần thiết. 


Mistral Small rất phù hợp cho: 
- Các tác vụ dựa trên văn bản như tóm tắt, phân tích cảm xúc và dịch thuật. 
- Các ứng dụng có yêu cầu truy vấn thường xuyên nhờ hiệu quả về chi phí 
- Các tác vụ mã có độ trễ thấp như xem xét và gợi ý mã 

## So sánh Mistral Small và Mistral Large 

Để thấy sự khác biệt về độ trễ giữa Mistral Small và Large, chạy các ô bên dưới. 

Bạn sẽ thấy sự khác biệt về thời gian phản hồi khoảng 3-5 giây. Cũng lưu ý độ dài và phong cách câu trả lời với cùng một lời nhắc.  

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

So với hai mô hình khác được thảo luận trong bài học này, Mistral NeMo là mô hình duy nhất miễn phí với Giấy phép Apache2. 

Nó được xem là bản nâng cấp của LLM mã nguồn mở trước đó từ Mistral, Mistral 7B. 

Một số tính năng khác của mô hình NeMo là: 

- *Mã hóa token hiệu quả hơn:* Mô hình này sử dụng bộ mã hóa Tekken thay vì tiktoken thường dùng. Điều này cho phép hiệu suất tốt hơn với nhiều ngôn ngữ và mã nguồn. 

- *Tinh chỉnh:* Mô hình cơ sở có sẵn để tinh chỉnh. Điều này cho phép linh hoạt hơn cho các trường hợp sử dụng cần tinh chỉnh. 

- *Gọi hàm gốc* - Giống Mistral Large, mô hình này được huấn luyện với gọi hàm. Điều này khiến nó trở nên độc đáo như một trong những mô hình mã nguồn mở đầu tiên có tính năng này. 


### So sánh Bộ mã hóa Token 

Trong ví dụ này, chúng ta sẽ xem cách Mistral NeMo xử lý mã hóa token so với Mistral Large. 

Cả hai ví dụ đều nhận cùng một lời nhắc nhưng bạn sẽ thấy NeMo trả về ít token hơn so với Mistral Large. 

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

# Mã hóa một danh sách các tin nhắn
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

## Học hỏi không dừng lại ở đây, tiếp tục hành trình

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức về AI Tạo sinh!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->