<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:11:37+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "vi"
}
-->
# Xây Dựng Với Các Mô Hình Gia Đình Meta

## Giới Thiệu

Bài học này sẽ bao gồm:

- Khám phá hai mô hình chính trong gia đình Meta - Llama 3.1 và Llama 3.2
- Hiểu các trường hợp sử dụng và kịch bản cho từng mô hình
- Ví dụ mã để thể hiện các tính năng độc đáo của từng mô hình

## Gia Đình Mô Hình Meta

Trong bài học này, chúng ta sẽ khám phá 2 mô hình từ gia đình Meta hay còn gọi là "Llama Herd" - Llama 3.1 và Llama 3.2

Các mô hình này có nhiều biến thể khác nhau và có sẵn trên GitHub Model marketplace. Dưới đây là thêm thông tin về cách sử dụng GitHub Models để [phát triển nguyên mẫu với các mô hình AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Các biến thể mô hình:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Lưu ý: Llama 3 cũng có trên GitHub Models nhưng sẽ không được đề cập trong bài học này*

## Llama 3.1

Với 405 tỷ tham số, Llama 3.1 thuộc loại LLM mã nguồn mở.

Mô hình này là bản nâng cấp của Llama 3 trước đó với các điểm cải tiến:

- Cửa sổ ngữ cảnh lớn hơn - 128k token so với 8k token
- Số token đầu ra tối đa lớn hơn - 4096 so với 2048
- Hỗ trợ đa ngôn ngữ tốt hơn - nhờ tăng số lượng token huấn luyện

Những cải tiến này giúp Llama 3.1 xử lý các trường hợp sử dụng phức tạp hơn khi xây dựng các ứng dụng GenAI bao gồm:
- Gọi hàm gốc - khả năng gọi các công cụ và hàm bên ngoài quy trình LLM
- Hiệu suất RAG tốt hơn - nhờ cửa sổ ngữ cảnh lớn hơn
- Tạo dữ liệu tổng hợp - khả năng tạo dữ liệu hiệu quả cho các tác vụ như tinh chỉnh mô hình

### Gọi Hàm Gốc

Llama 3.1 đã được tinh chỉnh để gọi hàm hoặc công cụ hiệu quả hơn. Nó cũng có hai công cụ tích hợp mà mô hình có thể nhận biết cần sử dụng dựa trên câu hỏi từ người dùng. Các công cụ này là:

- **Brave Search** - Có thể dùng để lấy thông tin cập nhật như thời tiết bằng cách tìm kiếm trên web
- **Wolfram Alpha** - Dùng cho các phép tính toán phức tạp, giúp bạn không cần phải tự viết hàm riêng

Bạn cũng có thể tạo các công cụ tùy chỉnh mà LLM có thể gọi.

Trong ví dụ mã dưới đây:

- Chúng ta định nghĩa các công cụ có sẵn (brave_search, wolfram_alpha) trong phần prompt hệ thống.
- Gửi một câu hỏi từ người dùng về thời tiết ở một thành phố cụ thể.
- LLM sẽ phản hồi bằng một lệnh gọi công cụ Brave Search trông như sau `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Lưu ý: Ví dụ này chỉ thực hiện lệnh gọi công cụ, nếu bạn muốn nhận kết quả, bạn cần tạo tài khoản miễn phí trên trang Brave API và định nghĩa hàm gọi công cụ đó*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


tool_prompt=f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha
Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="What is the weather in Stockholm?"),

]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## Llama 3.2

Mặc dù là một LLM, một hạn chế của Llama 3.1 là khả năng đa phương tiện. Tức là có thể sử dụng các loại đầu vào khác nhau như hình ảnh làm prompt và cung cấp phản hồi. Đây là một trong những tính năng chính của Llama 3.2. Các tính năng khác bao gồm:

- Đa phương tiện - có khả năng xử lý cả prompt văn bản và hình ảnh
- Các biến thể kích thước nhỏ đến trung bình (11B và 90B) - cung cấp các lựa chọn triển khai linh hoạt
- Các biến thể chỉ văn bản (1B và 3B) - cho phép mô hình được triển khai trên các thiết bị biên / di động với độ trễ thấp

Hỗ trợ đa phương tiện là một bước tiến lớn trong thế giới các mô hình mã nguồn mở. Ví dụ mã dưới đây sử dụng cả hình ảnh và prompt văn bản để nhận phân tích hình ảnh từ Llama 3.2 90B.

### Hỗ Trợ Đa Phương Tiện với Llama 3.2

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "Llama-3.2-90B-Vision-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="sample.jpg",
                        image_format="jpg",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
```

## Học Tập Không Dừng Lại Ở Đây, Hãy Tiếp Tục Hành Trình

Sau khi hoàn thành bài học này, hãy khám phá bộ sưu tập [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức về Generative AI!

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.