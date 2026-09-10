# Xây dựng với các mô hình trong họ Meta

## Giới thiệu

Bài học này sẽ bao gồm:

- Khám phá hai mô hình chính trong họ Meta - Llama 3.1 và Llama 3.2
- Hiểu các trường hợp sử dụng và kịch bản cho từng mô hình
- Mẫu mã để thể hiện các tính năng độc đáo của từng mô hình


## Họ mô hình Meta

Trong bài học này, chúng ta sẽ khám phá 2 mô hình từ họ Meta hay "Llama Herd" - Llama 3.1 và Llama 3.2.

Các mô hình này có nhiều biến thể và được cung cấp trong [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Lưu ý:** GitHub Models sẽ ngừng hoạt động vào cuối tháng 7 năm 2026. Đây là chi tiết thêm về việc sử dụng [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) để thử nghiệm với các mô hình AI.

Các biến thể mô hình:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Lưu ý: Llama 3 cũng có trong Microsoft Foundry Models nhưng sẽ không được đề cập trong bài học này*

## Llama 3.1

Với 405 Tỷ tham số, Llama 3.1 thuộc loại LLM mã nguồn mở.

Mô hình này là phiên bản nâng cấp của Llama 3 trước đó cung cấp:

- Cửa sổ ngữ cảnh lớn hơn - 128k token so với 8k token
- Số token đầu ra tối đa lớn hơn - 4096 so với 2048
- Hỗ trợ đa ngôn ngữ tốt hơn - nhờ số lượng token huấn luyện tăng lên

Những điều này cho phép Llama 3.1 xử lý các trường hợp sử dụng phức tạp hơn khi xây dựng các ứng dụng GenAI bao gồm:
- Gọi hàm gốc - khả năng gọi các công cụ và hàm bên ngoài quy trình làm việc của LLM
- Hiệu suất RAG tốt hơn - nhờ cửa sổ ngữ cảnh mở rộng
- Tạo dữ liệu tổng hợp - khả năng tạo dữ liệu hiệu quả cho các tác vụ như tinh chỉnh

### Gọi hàm gốc

Llama 3.1 đã được tinh chỉnh để hiệu quả hơn trong việc gọi hàm hoặc công cụ. Nó cũng có hai công cụ tích hợp mà mô hình có thể nhận biết cần sử dụng dựa trên lời nhắc từ người dùng. Các công cụ này là:

- **Brave Search** - Có thể được dùng để lấy thông tin cập nhật như thời tiết bằng cách tìm kiếm web
- **Wolfram Alpha** - Có thể dùng cho các phép tính toán học phức tạp hơn để không cần viết hàm riêng

Bạn cũng có thể tạo các công cụ tùy chỉnh mà LLM có thể gọi.

Trong ví dụ mã dưới đây:

- Chúng ta định nghĩa các công cụ sẵn có (brave_search, wolfram_alpha) trong lời nhắc hệ thống.
- Gửi lời nhắc người dùng hỏi về thời tiết ở một thành phố nhất định.
- LLM sẽ phản hồi với một cuộc gọi công cụ đến Brave Search trông giống như `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Lưu ý: Ví dụ này chỉ thực hiện cuộc gọi công cụ, nếu bạn muốn nhận kết quả, bạn cần tạo tài khoản miễn phí trên trang Brave API và định nghĩa hàm tương ứng.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Lấy những cái này từ trang "Tổng quan" của dự án Microsoft Foundry của bạn
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Meta-Llama-3.1-405B-Instruct"

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

Mặc dù là một LLM, một hạn chế của Llama 3.1 là thiếu đa phương thức. Tức là, không thể sử dụng các loại đầu vào khác nhau như hình ảnh làm lời nhắc và cung cấp phản hồi. Khả năng này là một trong những tính năng chính của Llama 3.2. Các tính năng này cũng bao gồm:

- Đa phương thức - có khả năng đánh giá cả lời nhắc bằng văn bản và hình ảnh
- Các biến thể kích thước nhỏ đến trung bình (11B và 90B) - cung cấp các lựa chọn triển khai linh hoạt,
- Các biến thể chỉ có văn bản (1B và 3B) - cho phép mô hình được triển khai trên thiết bị biên / di động và cung cấp độ trễ thấp

Hỗ trợ đa phương thức là một bước tiến lớn trong thế giới các mô hình mã nguồn mở. Ví dụ mã dưới đây sử dụng cả lời nhắc hình ảnh và văn bản để lấy phân tích về hình ảnh từ Llama 3.2 90B.


### Hỗ trợ đa phương thức với Llama 3.2

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

# Lấy những thông tin này từ trang "Tổng quan" của dự án Microsoft Foundry của bạn
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
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

## Học tập không dừng lại ở đây, hãy tiếp tục hành trình

Sau khi hoàn thành bài học này, hãy khám phá [Bộ sưu tập Học tập AI Tạo sinh](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức về AI Tạo sinh của bạn!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->