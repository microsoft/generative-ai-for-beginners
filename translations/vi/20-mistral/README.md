# Xây dựng với các Mô hình Mistral 

## Giới thiệu 

Bài học này sẽ bao gồm: 
- Khám phá các mô hình Mistral khác nhau 
- Hiểu biết về các trường hợp sử dụng và kịch bản dành cho từng mô hình 
- Khám phá các ví dụ mã minh họa các tính năng độc đáo của từng mô hình. 

## Các mô hình Mistral 

Trong bài học này, chúng ta sẽ khám phá 3 mô hình Mistral khác nhau: 
**Mistral Large**, **Mistral Small** và **Mistral Nemo**. 

Mỗi mô hình này được cung cấp miễn phí trên [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Mã trong sổ tay này sẽ sử dụng các mô hình này để chạy mã.

> **Lưu ý:** GitHub Models sẽ ngừng hoạt động vào cuối tháng 7 năm 2026. Dưới đây là thêm chi tiết về việc sử dụng [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) để tạo nguyên mẫu với các mô hình AI. 


## Mistral Large 2 (2407)
Mistral Large 2 hiện là mô hình chủ lực từ Mistral và được thiết kế cho doanh nghiệp. 

Mô hình là bản nâng cấp của Mistral Large gốc với các điểm vượt trội như 
-  Cửa sổ ngữ cảnh lớn hơn - 128k so với 32k 
-  Hiệu suất tốt hơn trong các nhiệm vụ Toán học và Lập trình - độ chính xác trung bình 76.9% so với 60.4% 
-  Hiệu suất đa ngôn ngữ tăng cao - các ngôn ngữ bao gồm: Tiếng Anh, Pháp, Đức, Tây Ban Nha, Ý, Bồ Đào Nha, Hà Lan, Nga, Trung Quốc, Nhật Bản, Hàn Quốc, Ả Rập và Hindi.

Với những tính năng này, Mistral Large nổi bật trong 
- *Tạo Văn bản Tăng cường Truy xuất (RAG)* - nhờ cửa sổ ngữ cảnh lớn hơn
- *Gọi Hàm* - mô hình này hỗ trợ gọi hàm gốc cho phép tích hợp với các công cụ và API bên ngoài. Các cuộc gọi này có thể được thực hiện song song hoặc lần lượt theo thứ tự tuần tự. 
- *Tạo mã* - mô hình này xuất sắc trong việc tạo mã Python, Java, TypeScript và C++. 

### Ví dụ RAG sử dụng Mistral Large 2 

Trong ví dụ này, chúng tôi sử dụng Mistral Large 2 để chạy mẫu RAG trên một tài liệu văn bản. Câu hỏi được viết bằng tiếng Hàn và hỏi về các hoạt động của tác giả trước đại học. 

Nó sử dụng Mô hình Embeddings của Cohere để tạo embeddings cho tài liệu văn bản cũng như câu hỏi. Với ví dụ này, nó sử dụng gói Python faiss làm kho lưu trữ vector. 

Lời nhắc gửi tới mô hình Mistral bao gồm cả câu hỏi và các đoạn văn được truy xuất có nội dung tương tự câu hỏi. Mô hình sau đó cung cấp phản hồi bằng ngôn ngữ tự nhiên. 

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

# Lấy những thông tin này từ trang "Tổng quan" của dự án Microsoft Foundry của bạn
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
Mistral Small là một mô hình khác trong gia đình Mistral thuộc loại mô hình premier/doanh nghiệp. Như tên gọi, mô hình này là Mô hình Ngôn ngữ Nhỏ (SLM). Những ưu điểm khi sử dụng Mistral Small là: 
- Tiết kiệm chi phí so với các mô hình LLM Mistral như Mistral Large và NeMo - giảm giá 80%
- Độ trễ thấp - phản hồi nhanh hơn so với các LLM của Mistral
- Linh hoạt - có thể triển khai trên nhiều môi trường khác nhau với yêu cầu tài nguyên thấp hơn. 


Mistral Small rất phù hợp cho: 
- Các nhiệm vụ dựa trên văn bản như tóm tắt, phân tích cảm xúc và dịch thuật. 
- Các ứng dụng yêu cầu nhiều truy vấn do tính hiệu quả về chi phí 
- Các nhiệm vụ mã có độ trễ thấp như xem xét và gợi ý mã 

## So sánh Mistral Small và Mistral Large 

Để thấy sự khác biệt về độ trễ giữa Mistral Small và Large, hãy chạy các ô dưới đây. 

Bạn sẽ thấy sự khác biệt về thời gian phản hồi từ 3-5 giây. Cũng lưu ý độ dài và phong cách phản hồi trên cùng một lời nhắc.  

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

So với hai mô hình khác được thảo luận trong bài này, Mistral NeMo là mô hình duy nhất miễn phí với Giấy phép Apache2. 

Nó được xem như là bản nâng cấp của mô hình LLM mã nguồn mở trước đó từ Mistral, Mistral 7B. 

Một số tính năng khác của mô hình NeMo bao gồm: 

- *Phân tích ngôn ngữ (tokenization) hiệu quả hơn:* Mô hình này sử dụng trình phân tích Tekken thay vì tiktoken được sử dụng phổ biến hơn. Điều này giúp cải thiện hiệu suất cho nhiều ngôn ngữ và mã lệnh. 

- *Điều chỉnh tinh chỉnh (Finetuning):* Mô hình cơ sở có thể được tinh chỉnh. Điều này tăng sự linh hoạt cho các trường hợp cần tinh chỉnh. 

- *Gọi hàm gốc* - Giống như Mistral Large, mô hình này được đào tạo để gọi hàm. Điều này làm nó trở thành một trong những mô hình mã nguồn mở đầu tiên làm được điều này. 


### So sánh trình phân tích ngôn ngữ (Tokenizers) 

Trong ví dụ này, chúng ta sẽ xem cách Mistral NeMo xử lý phân tích ngôn ngữ so với Mistral Large. 

Cả hai ví dụ sử dụng cùng một lời nhắc nhưng bạn sẽ thấy NeMo trả về ít tokens hơn so với Mistral Large. 

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

## Học tập không kết thúc ở đây, hãy tiếp tục hành trình

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức về AI Tạo sinh!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->