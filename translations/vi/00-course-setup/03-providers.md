# Lựa chọn & Cấu hình nhà cung cấp LLM 🔑

Các bài tập **có thể** được thiết lập để làm việc với một hoặc nhiều triển khai Mô hình Ngôn ngữ Lớn (LLM) thông qua nhà cung cấp dịch vụ được hỗ trợ như OpenAI, Azure hoặc Hugging Face. Những nhà cung cấp này cung cấp một _điểm cuối được lưu trữ_ (API) mà chúng ta có thể truy cập lập trình với các thông tin xác thực phù hợp (khóa API hoặc token). Trong khóa học này, chúng ta thảo luận về các nhà cung cấp sau:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) với các mô hình đa dạng bao gồm loạt GPT cốt lõi.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) dành cho các mô hình OpenAI với trọng tâm sẵn sàng cho doanh nghiệp
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) cho các mô hình mã nguồn mở và máy chủ suy luận

**Bạn sẽ cần sử dụng tài khoản riêng của mình cho các bài tập này**. Các bài tập là tùy chọn nên bạn có thể chọn thiết lập một, tất cả - hoặc không thiết lập nhà cung cấp nào dựa trên sở thích của bạn. Một số hướng dẫn đăng ký:

| Đăng ký | Chi phí | Khóa API | Playground | Bình luận |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Bảng giá](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Dựa trên dự án](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Không cần mã, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Nhiều mô hình có sẵn |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Bảng giá](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Bắt đầu nhanh SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Bắt đầu nhanh Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Phải đăng ký trước để được truy cập](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Bảng giá](https://huggingface.co/pricing) | [Token truy cập](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat có mô hình giới hạn](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Làm theo hướng dẫn dưới đây để _cấu hình_ kho lưu trữ này sử dụng với các nhà cung cấp khác nhau. Các bài tập yêu cầu nhà cung cấp cụ thể sẽ chứa một trong các thẻ này trong tên tệp:

- `aoai` - yêu cầu điểm cuối Azure OpenAI, khóa
- `oai` - yêu cầu điểm cuối OpenAI, khóa
- `hf` - yêu cầu token Hugging Face

Bạn có thể cấu hình một, không hoặc tất cả các nhà cung cấp. Các bài tập liên quan sẽ báo lỗi khi thiếu thông tin xác thực.

## Tạo tệp `.env`

Chúng tôi giả định bạn đã đọc hướng dẫn trên và đăng ký với nhà cung cấp liên quan, đồng thời đã lấy được thông tin xác thực cần thiết (API_KEY hoặc token). Trong trường hợp Azure OpenAI, chúng tôi giả định bạn cũng có một triển khai hợp lệ của Dịch vụ Azure OpenAI (điểm cuối) với ít nhất một mô hình GPT được triển khai cho hoàn thành trò chuyện.

Bước tiếp theo là cấu hình **biến môi trường cục bộ** của bạn như sau:

1. Tìm trong thư mục gốc tệp `.env.copy` có nội dung như sau:

   ```bash
   # Nhà cung cấp OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Mặc định đã được đặt!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Sao chép tệp đó thành `.env` bằng lệnh dưới đây. Tệp này được _gitignore_, giữ bí mật an toàn.

   ```bash
   cp .env.copy .env
   ```

3. Điền các giá trị (thay thế các chỗ giữ chỗ bên phải dấu `=`) như mô tả trong phần tiếp theo.

4. (Tùy chọn) Nếu bạn sử dụng GitHub Codespaces, bạn có thể lưu biến môi trường dưới dạng _bí mật Codespaces_ liên kết với kho lưu trữ này. Trong trường hợp đó, bạn không cần thiết lập tệp .env cục bộ. **Tuy nhiên, lưu ý rằng tùy chọn này chỉ hoạt động nếu bạn sử dụng GitHub Codespaces.** Bạn vẫn cần thiết lập tệp .env nếu sử dụng Docker Desktop.

## Điền tệp `.env`

Hãy xem nhanh các tên biến để hiểu chúng đại diện cho gì:

| Biến  | Mô tả  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Đây là token truy cập người dùng bạn thiết lập trong hồ sơ của mình |
| OPENAI_API_KEY | Đây là khóa ủy quyền để sử dụng dịch vụ cho các điểm cuối OpenAI không phải Azure |
| AZURE_OPENAI_API_KEY | Đây là khóa ủy quyền để sử dụng dịch vụ đó |
| AZURE_OPENAI_ENDPOINT | Đây là điểm cuối đã triển khai cho tài nguyên Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Đây là điểm cuối triển khai mô hình _tạo văn bản_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Đây là điểm cuối triển khai mô hình _nhúng văn bản_ |
| | |

Lưu ý: Hai biến Azure OpenAI cuối cùng phản ánh mô hình mặc định cho hoàn thành trò chuyện (tạo văn bản) và tìm kiếm vector (nhúng) tương ứng. Hướng dẫn thiết lập chúng sẽ được định nghĩa trong các bài tập liên quan.

## Cấu hình Azure: Từ Portal

Giá trị điểm cuối và khóa Azure OpenAI sẽ được tìm thấy trong [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) nên chúng ta bắt đầu từ đó.

1. Truy cập [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Nhấp vào tùy chọn **Keys and Endpoint** trong thanh bên (menu bên trái).
1. Nhấp **Show Keys** - bạn sẽ thấy các mục sau: KEY 1, KEY 2 và Endpoint.
1. Sử dụng giá trị KEY 1 cho AZURE_OPENAI_API_KEY
1. Sử dụng giá trị Endpoint cho AZURE_OPENAI_ENDPOINT

Tiếp theo, chúng ta cần điểm cuối cho các mô hình cụ thể đã triển khai.

1. Nhấp vào tùy chọn **Model deployments** trong thanh bên (menu bên trái) cho tài nguyên Azure OpenAI.
1. Trong trang đích, nhấp **Manage Deployments**

Điều này sẽ đưa bạn đến trang web Azure OpenAI Studio, nơi chúng ta sẽ tìm các giá trị khác như mô tả dưới đây.

## Cấu hình Azure: Từ Studio

1. Điều hướng đến [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **từ tài nguyên của bạn** như đã mô tả ở trên.
1. Nhấp tab **Deployments** (thanh bên, bên trái) để xem các mô hình đang được triển khai.
1. Nếu mô hình bạn muốn chưa được triển khai, sử dụng **Create new deployment** để triển khai nó.
1. Bạn sẽ cần một mô hình _text-generation_ - chúng tôi khuyên dùng: **gpt-35-turbo**
1. Bạn sẽ cần một mô hình _text-embedding_ - chúng tôi khuyên dùng **text-embedding-ada-002**

Bây giờ cập nhật các biến môi trường để phản ánh _Tên triển khai_ được sử dụng. Thông thường tên này sẽ giống tên mô hình trừ khi bạn thay đổi rõ ràng. Ví dụ, bạn có thể có:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Đừng quên lưu tệp .env khi hoàn thành**. Bạn có thể thoát tệp và quay lại hướng dẫn để chạy notebook.

## Cấu hình OpenAI: Từ Hồ sơ

Khóa API OpenAI của bạn có thể tìm thấy trong [tài khoản OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Nếu bạn chưa có, bạn có thể đăng ký tài khoản và tạo khóa API. Khi có khóa, bạn có thể dùng nó để điền biến `OPENAI_API_KEY` trong tệp `.env`.

## Cấu hình Hugging Face: Từ Hồ sơ

Token Hugging Face của bạn có thể tìm thấy trong hồ sơ của bạn tại [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Đừng đăng hoặc chia sẻ công khai. Thay vào đó, tạo một token mới cho dự án này và sao chép vào tệp `.env` dưới biến `HUGGING_FACE_API_KEY`. _Lưu ý:_ Về kỹ thuật đây không phải là khóa API nhưng được dùng để xác thực nên chúng tôi giữ tên biến cho nhất quán.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->