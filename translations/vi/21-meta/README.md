# Xây dựng với các mô hình Meta Family 

## Giới thiệu 

Bài học này sẽ bao gồm: 

- Khám phá hai mô hình chính của Meta Family - Llama 3.1 và Llama 3.2 
- Hiểu các trường hợp sử dụng và kịch bản cho từng mô hình 
- Ví dụ mã để trình bày các tính năng độc đáo của từng mô hình 


## Bộ mô hình Meta Family 

Trong bài học này, chúng ta sẽ khám phá 2 mô hình thuộc Meta Family hay "Đàn Llama" - Llama 3.1 và Llama 3.2.

Các mô hình này có các biến thể khác nhau và có sẵn trong [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Lưu ý:** GitHub Models sẽ ngừng hoạt động vào cuối tháng 7 năm 2026. Dưới đây là thêm thông tin về việc sử dụng [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) để thử nghiệm với các mô hình AI.

Các biến thể mô hình: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Lưu ý: Llama 3 cũng có trong Microsoft Foundry Models nhưng sẽ không được đề cập trong bài học này*

## Llama 3.1 

Với 405 tỷ tham số, Llama 3.1 thuộc loại mô hình LLM mã nguồn mở. 

Mô hình này là phiên bản nâng cấp của Llama 3 trước đó với việc cung cấp: 

- Cửa sổ ngữ cảnh lớn hơn - 128k token so với 8k token 
- Số token đầu ra tối đa lớn hơn - 4096 so với 2048 
- Hỗ trợ đa ngôn ngữ tốt hơn - nhờ tăng số token huấn luyện 

Những điều này giúp Llama 3.1 xử lý các trường hợp sử dụng phức tạp hơn khi xây dựng các ứng dụng GenAI bao gồm: 
- Gọi hàm gốc - khả năng gọi các công cụ và hàm bên ngoài luồng làm việc LLM
- Hiệu suất RAG tốt hơn - nhờ cửa sổ ngữ cảnh rộng hơn 
- Tạo dữ liệu tổng hợp - khả năng tạo dữ liệu hiệu quả cho các tác vụ như điều chỉnh tinh chỉnh 

### Gọi hàm gốc 

Llama 3.1 đã được tinh chỉnh để hiệu quả hơn trong việc gọi hàm hoặc công cụ. Nó cũng có hai công cụ tích hợp sẵn mà mô hình có thể nhận biết là cần sử dụng dựa trên lời nhắc từ người dùng. Các công cụ này là: 

- **Brave Search** - Có thể dùng để tìm thông tin cập nhật như thời tiết bằng cách thực hiện tìm kiếm web 
- **Wolfram Alpha** - Có thể dùng cho các phép tính toán học phức tạp hơn nên không cần phải tự viết hàm riêng. 

Bạn cũng có thể tạo các công cụ tùy chỉnh riêng mà LLM có thể gọi. 

Trong ví dụ mã bên dưới: 

- Chúng ta định nghĩa các công cụ có sẵn (brave_search, wolfram_alpha) trong lời nhắc hệ thống. 
- Gửi lời nhắc người dùng hỏi về thời tiết tại một thành phố nhất định. 
- LLM sẽ trả lời với một lời gọi công cụ đến Brave Search trông như thế này `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Lưu ý: Ví dụ này chỉ thực hiện lời gọi công cụ, nếu bạn muốn nhận kết quả, bạn cần tạo tài khoản miễn phí trên trang Brave API và định nghĩa hàm thực thi.*

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

Mặc dù là một LLM, một hạn chế của Llama 3.1 là thiếu khả năng đa phương thức. Tức là không thể sử dụng các loại đầu vào khác như hình ảnh làm lời nhắc và cung cấp phản hồi. Khả năng này là một trong những tính năng chính của Llama 3.2. Các tính năng này cũng bao gồm: 

- Đa phương thức - có khả năng đánh giá cả lời nhắc văn bản và hình ảnh 
- Các biến thể kích thước nhỏ đến trung bình (11B và 90B) - cung cấp các tùy chọn triển khai linh hoạt, 
- Các biến thể chỉ văn bản (1B và 3B) - cho phép mô hình được triển khai trên thiết bị biên / di động và cung cấp độ trễ thấp 

Hỗ trợ đa phương thức đại diện cho một bước tiến lớn trong thế giới các mô hình mã nguồn mở. Ví dụ mã dưới đây nhận đầu vào cả hình ảnh và văn bản để lấy phân tích hình ảnh từ Llama 3.2 90B. 


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

# Lấy những cái này từ trang "Tổng quan" của dự án Microsoft Foundry của bạn
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

## Việc học không dừng lại ở đây, tiếp tục hành trình

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức Generative AI của bạn!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->