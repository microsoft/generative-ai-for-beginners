# Xây Dựng Với Các Mô Hình Gia Đình Meta

## Giới Thiệu

Bài học này sẽ bao gồm:

- Khám phá hai mô hình chính trong gia đình Meta - Llama 3.1 và Llama 3.2, cùng với các lựa chọn thay thế hiện có được sử dụng trong các ví dụ mã (Llama 3.3 và Llama 4)
- Hiểu về các trường hợp sử dụng và kịch bản của từng mô hình
- Ví dụ mã để thể hiện các tính năng độc đáo của từng mô hình


## Gia Đình Các Mô Hình Meta

Trong bài học này, chúng ta sẽ khám phá 2 mô hình từ gia đình Meta hay "Llama Herd" - Llama 3.1 và Llama 3.2. Các ví dụ mã có thể chạy được sử dụng Llama 3.3 và Llama 4, là các lựa chọn thay thế hiện có trong danh mục Microsoft Foundry Models.

Các mô hình này xuất hiện với các biến thể khác nhau và có sẵn trong [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Lưu ý:** GitHub Models sẽ ngừng hoạt động vào cuối tháng 7 năm 2026. Dưới đây là thêm chi tiết về việc sử dụng [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) để thử nghiệm với các mô hình AI.

> **Lưu ý:** Các phiên bản mô hình cụ thể mà bài học này ban đầu sử dụng (Llama 3.1 70B/405B Instruct, Llama 3.2 11B/90B Vision Instruct) đã được ngừng hỗ trợ trong danh mục Microsoft Foundry Models. Các ví dụ mã dưới đây dùng `Llama-3.3-70B-Instruct` và `Llama-4-Scout-17B-16E-Instruct` như các lựa chọn thay thế hiện có trong danh mục Microsoft Foundry Models, nên vẫn chạy tốt cho đến nay.

Các biến thể mô hình (như bài học ban đầu đề cập):
- Llama 3.1 - 70B Instruct (đã ngừng hỗ trợ)
- Llama 3.1 - 405B Instruct (đã ngừng hỗ trợ)
- Llama 3.2 - 11B Vision Instruct (đã ngừng hỗ trợ)
- Llama 3.2 - 90B Vision Instruct (đã ngừng hỗ trợ)

Các lựa chọn thay thế hiện có được sử dụng trong ví dụ mã:
- Llama 3.3 - 70B Instruct (`Llama-3.3-70B-Instruct`)
- Llama 4 Scout - 17B 16E Instruct (`Llama-4-Scout-17B-16E-Instruct`)

*Lưu ý: Các biến thể Llama 3 được thảo luận ở trên được giữ lại để tham khảo lịch sử và hiện không có sẵn trong Microsoft Foundry Models.*

## Llama 3.1

Với 405 Tỷ Tham Số, Llama 3.1 thuộc danh mục LLM mã nguồn mở.

Mô hình là bản nâng cấp của phiên bản Llama 3 trước đó với các cải tiến:

- Cửa sổ ngữ cảnh lớn hơn - 128k token so với 8k token
- Số lượng token đầu ra tối đa lớn hơn - 4096 so với 2048
- Hỗ trợ đa ngôn ngữ tốt hơn - do tăng số lượng token huấn luyện

Những điều này cho phép Llama 3.1 xử lý các trường hợp sử dụng phức tạp hơn khi xây dựng các ứng dụng GenAI bao gồm:
- Gọi Hàm Bản Địa - khả năng gọi các công cụ và hàm bên ngoài quy trình làm việc LLM
- Hiệu suất RAG tốt hơn - nhờ cửa sổ ngữ cảnh lớn hơn
- Tạo dữ liệu tổng hợp - khả năng tạo dữ liệu hiệu quả cho các tác vụ như tinh chỉnh mô hình

### Gọi Hàm Bản Địa

Llama 3.1 đã được tinh chỉnh để hiệu quả hơn trong việc gọi hàm hoặc công cụ. Nó cũng có hai công cụ tích hợp mà mô hình có thể nhận diện là cần sử dụng dựa trên đề bài từ người dùng. Những công cụ này là:

- **Brave Search** - Có thể được sử dụng để lấy thông tin cập nhật như thời tiết bằng cách tìm kiếm trên web
- **Wolfram Alpha** - Có thể được sử dụng cho các phép tính toán học phức tạp hơn, nên không cần viết hàm riêng

Bạn cũng có thể tạo các công cụ tùy chỉnh mà LLM có thể gọi.

Trong ví dụ mã dưới đây:

- Chúng ta định nghĩa các công cụ có sẵn (brave_search, wolfram_alpha) trong prompt hệ thống.
- Gửi prompt người dùng hỏi về thời tiết ở một thành phố cụ thể.
- LLM sẽ phản hồi với một lệnh gọi công cụ tới Brave Search, trông như thế này `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Lưu ý: Ví dụ này chỉ thực hiện lệnh gọi công cụ, nếu bạn muốn nhận kết quả, bạn cần tạo tài khoản miễn phí trên trang API của Brave và định nghĩa hàm thực tế.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Meta-Llama-3.1-405B-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-3.3-70B-Instruct, a currently available alternative, instead
model_name = "Llama-3.3-70B-Instruct"

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

Mặc dù là một LLM, một hạn chế của Llama 3.1 là thiếu khả năng đa phương thức. Tức là không thể dùng các loại đầu vào khác như hình ảnh làm prompt và phản hồi lại. Khả năng này là một trong những tính năng chính của Llama 3.2. Các tính năng đó cũng bao gồm:

- Đa phương thức - có thể đánh giá cả prompt văn bản và hình ảnh
- Các biến thể kích thước từ nhỏ đến trung bình (11B và 90B) - cung cấp các tùy chọn triển khai linh hoạt,
- Các biến thể chỉ văn bản (1B và 3B) - cho phép mô hình được triển khai trên các thiết bị biên / di động và cung cấp độ trễ thấp

Hỗ trợ đa phương thức đại diện cho một bước tiến lớn trong thế giới các mô hình mã nguồn mở. Ví dụ mã dưới đây nhận cả đầu vào hình ảnh và văn bản để phân tích hình ảnh. Vì Llama 3.2 90B Vision Instruct đã bị ngừng hỗ trợ, ví dụ sử dụng `Llama-4-Scout-17B-16E-Instruct`, một lựa chọn thay thế đa phương thức hiện có sẵn.


### Hỗ Trợ Đa Phương Thức với Llama 3.2

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

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Llama-3.2-90B-Vision-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-4-Scout-17B-16E-Instruct, a currently available natively multimodal alternative, instead
model_name = "Llama-4-Scout-17B-16E-Instruct"

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

## Học hỏi không dừng lại ở đây, tiếp tục hành trình

Sau khi hoàn thành bài học này, hãy xem bộ sưu tập [Học Tập AI Tạo Sinh](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) của chúng tôi để tiếp tục nâng cao kiến thức về AI Tạo Sinh!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->