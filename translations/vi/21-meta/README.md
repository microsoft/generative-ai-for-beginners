# Xây dựng với các mô hình Meta Family

## Giới thiệu

Bài học này sẽ bao gồm:

- Khám phá hai mô hình chính trong Meta family - Llama 3.1 và Llama 3.2
- Hiểu các trường hợp sử dụng và kịch bản cho từng mô hình
- Ví dụ mã để trình bày các tính năng độc đáo của từng mô hình

## Gia đình mô hình Meta

Trong bài học này, chúng ta sẽ khám phá 2 mô hình từ gia đình Meta hoặc "Llama Herd" - Llama 3.1 và Llama 3.2.

Các mô hình này có nhiều biến thể khác nhau và có sẵn trên GitHub Model marketplace. Dưới đây là chi tiết hơn về việc sử dụng GitHub Models để [phát thảo với các mô hình AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Các biến thể mô hình:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Lưu ý: Llama 3 cũng có sẵn trên GitHub Models nhưng sẽ không được đề cập trong bài học này*

## Llama 3.1

Với 405 Tỷ tham số, Llama 3.1 thuộc loại LLM mã nguồn mở.

Mô hình là bản nâng cấp so với phiên bản Llama 3 trước đó bằng cách cung cấp:

- Cửa sổ ngữ cảnh lớn hơn - 128k tokens so với 8k tokens
- Số token đầu ra tối đa lớn hơn - 4096 so với 2048
- Hỗ trợ đa ngôn ngữ tốt hơn - do tăng số lượng token huấn luyện

Những điều này giúp Llama 3.1 xử lý được các trường hợp sử dụng phức tạp hơn khi xây dựng ứng dụng GenAI bao gồm:
- Gọi hàm nội bộ - khả năng gọi các công cụ và hàm bên ngoài quy trình làm việc LLM
- Hiệu suất RAG tốt hơn - nhờ cửa sổ ngữ cảnh lớn hơn
- Tạo dữ liệu tổng hợp - khả năng tạo dữ liệu hiệu quả cho các tác vụ như tinh chỉnh mô hình

### Gọi hàm nội bộ

Llama 3.1 đã được tinh chỉnh để hiệu quả hơn trong việc gọi hàm hoặc công cụ. Nó cũng có hai công cụ tích hợp sẵn mà mô hình có thể nhận biết cần sử dụng dựa trên lời nhắc từ người dùng. Các công cụ này là:

- **Brave Search** - Có thể dùng để lấy thông tin cập nhật như thời tiết bằng cách thực hiện tìm kiếm trên web
- **Wolfram Alpha** - Dùng cho các phép tính toán học phức tạp hơn nên bạn không cần tự viết hàm riêng

Bạn cũng có thể tạo các công cụ tùy chỉnh của riêng mình mà LLM có thể gọi.

Trong ví dụ mã dưới đây:

- Chúng ta định nghĩa các công cụ có sẵn (brave_search, wolfram_alpha) trong lời nhắc hệ thống.
- Gửi lời nhắc người dùng hỏi về thời tiết ở một thành phố cụ thể.
- LLM sẽ trả lời kèm theo lời gọi công cụ tới Brave Search trông như sau `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Lưu ý: Ví dụ này chỉ thực hiện lời gọi công cụ, nếu bạn muốn nhận kết quả, bạn cần tạo tài khoản miễn phí trên trang Brave API và định nghĩa hàm đó.*

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

Mặc dù là một LLM, một hạn chế của Llama 3.1 là không hỗ trợ đa phương thức. Nghĩa là không thể dùng các loại đầu vào khác nhau như hình ảnh làm lời nhắc và cung cấp phản hồi. Khả năng này là một trong những tính năng chính của Llama 3.2. Các tính năng khác bao gồm:

- Hỗ trợ đa phương thức - có khả năng đánh giá cả lời nhắc văn bản và hình ảnh
- Các biến thể kích cỡ nhỏ đến trung bình (11B và 90B) - cho phép nhiều lựa chọn triển khai linh hoạt
- Biến thể chỉ văn bản (1B và 3B) - cho phép mô hình được triển khai trên thiết bị biên / di động và cung cấp độ trễ thấp

Hỗ trợ đa phương thức đại diện cho một bước tiến lớn trong thế giới các mô hình mã nguồn mở. Ví dụ mã dưới đây nhận cả lời nhắc hình ảnh và văn bản để phân tích hình ảnh từ Llama 3.2 90B.

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

## Việc học không dừng lại ở đây, tiếp tục hành trình

Sau khi hoàn thành bài học này, hãy khám phá [Bộ sưu tập học tập AI Generative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức về AI Generative!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ nguyên bản nên được xem là nguồn thông tin chính thống. Đối với những thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hay diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->