<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:13:47+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "vi"
}
-->
# Xây dựng với các mô hình Meta Family

## Giới thiệu

Bài học này sẽ bao gồm:

- Khám phá hai mô hình chính của Meta Family - Llama 3.1 và Llama 3.2
- Hiểu các trường hợp sử dụng và kịch bản cho mỗi mô hình
- Mẫu mã để hiển thị các tính năng độc đáo của mỗi mô hình

## Các mô hình của Meta Family

Trong bài học này, chúng ta sẽ khám phá 2 mô hình từ Meta Family hoặc "Llama Herd" - Llama 3.1 và Llama 3.2

Các mô hình này có nhiều biến thể khác nhau và có sẵn trên thị trường mô hình GitHub. Dưới đây là chi tiết hơn về việc sử dụng GitHub Models để [tạo mẫu với các mô hình AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Biến thể mô hình:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Lưu ý: Llama 3 cũng có sẵn trên GitHub Models nhưng sẽ không được đề cập trong bài học này*

## Llama 3.1

Với 405 tỷ tham số, Llama 3.1 nằm trong danh mục LLM mã nguồn mở.

Chế độ này là một bản nâng cấp cho phiên bản trước Llama 3 bằng cách cung cấp:

- Cửa sổ ngữ cảnh lớn hơn - 128k tokens so với 8k tokens
- Số lượng token đầu ra tối đa lớn hơn - 4096 so với 2048
- Hỗ trợ đa ngôn ngữ tốt hơn - do tăng số lượng token đào tạo

Điều này cho phép Llama 3.1 xử lý các trường hợp sử dụng phức tạp hơn khi xây dựng các ứng dụng GenAI bao gồm:
- Gọi hàm gốc - khả năng gọi các công cụ và hàm bên ngoài luồng công việc LLM
- Hiệu suất RAG tốt hơn - nhờ cửa sổ ngữ cảnh cao hơn
- Tạo dữ liệu tổng hợp - khả năng tạo dữ liệu hiệu quả cho các nhiệm vụ như tinh chỉnh

### Gọi hàm gốc

Llama 3.1 đã được tinh chỉnh để hiệu quả hơn trong việc thực hiện các cuộc gọi hàm hoặc công cụ. Nó cũng có hai công cụ tích hợp sẵn mà mô hình có thể xác định là cần sử dụng dựa trên lời nhắc từ người dùng. Những công cụ này là:

- **Brave Search** - Có thể được sử dụng để lấy thông tin cập nhật như thời tiết bằng cách thực hiện tìm kiếm trên web
- **Wolfram Alpha** - Có thể được sử dụng cho các phép tính toán học phức tạp hơn nên không cần viết các hàm của riêng bạn.

Bạn cũng có thể tạo các công cụ tùy chỉnh của riêng mình mà LLM có thể gọi.

Trong ví dụ mã dưới đây:

- Chúng ta định nghĩa các công cụ có sẵn (brave_search, wolfram_alpha) trong lời nhắc hệ thống.
- Gửi một lời nhắc người dùng hỏi về thời tiết ở một thành phố nào đó.
- LLM sẽ phản hồi bằng một cuộc gọi công cụ đến công cụ Brave Search sẽ trông như thế này `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Lưu ý: Ví dụ này chỉ thực hiện cuộc gọi công cụ, nếu bạn muốn nhận kết quả, bạn sẽ cần tạo một tài khoản miễn phí trên trang API của Brave và định nghĩa hàm đó*

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

Mặc dù là một LLM, một hạn chế mà Llama 3.1 gặp phải là đa phương tiện. Đó là, khả năng sử dụng các loại đầu vào khác nhau như hình ảnh làm lời nhắc và cung cấp phản hồi. Khả năng này là một trong những tính năng chính của Llama 3.2. Các tính năng này cũng bao gồm:

- Đa phương tiện - có khả năng đánh giá cả lời nhắc văn bản và hình ảnh
- Các biến thể kích thước nhỏ đến trung bình (11B và 90B) - điều này cung cấp các tùy chọn triển khai linh hoạt,
- Các biến thể chỉ văn bản (1B và 3B) - điều này cho phép mô hình được triển khai trên các thiết bị biên / di động và cung cấp độ trễ thấp

Hỗ trợ đa phương tiện đại diện cho một bước tiến lớn trong thế giới các mô hình mã nguồn mở. Ví dụ mã dưới đây nhận cả hình ảnh và lời nhắc văn bản để nhận phân tích hình ảnh từ Llama 3.2 90B.

### Hỗ trợ đa phương tiện với Llama 3.2

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

## Học không dừng lại ở đây, tiếp tục hành trình

Sau khi hoàn thành bài học này, hãy xem [Bộ sưu tập học AI tạo sinh](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức về AI tạo sinh của bạn!

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin đáng tin cậy. Đối với thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.