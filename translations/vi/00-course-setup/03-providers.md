<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T18:06:12+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "vi"
}
-->
# Lựa chọn & Cấu hình Nhà cung cấp LLM 🔑

Bạn **có thể** thiết lập các bài tập để làm việc với một hoặc nhiều mô hình ngôn ngữ lớn (LLM) thông qua các nhà cung cấp dịch vụ được hỗ trợ như OpenAI, Azure hoặc Hugging Face. Các dịch vụ này cung cấp _endpoint được lưu trữ_ (API) mà bạn có thể truy cập thông qua lập trình với thông tin xác thực phù hợp (API key hoặc token). Trong khóa học này, chúng ta sẽ tìm hiểu về các nhà cung cấp sau:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) với nhiều mô hình đa dạng, bao gồm dòng GPT chủ lực.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) cung cấp các mô hình OpenAI với khả năng sẵn sàng cho doanh nghiệp
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) dành cho các mô hình mã nguồn mở và máy chủ suy luận

**Bạn sẽ cần sử dụng tài khoản cá nhân cho các bài tập này**. Các bài tập là tùy chọn, vì vậy bạn có thể chọn thiết lập một, tất cả - hoặc không thiết lập nhà cung cấp nào - tùy theo sở thích. Một số hướng dẫn đăng ký:

| Đăng ký | Chi phí | API Key | Playground | Ghi chú |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Bảng giá](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Theo dự án](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Có nhiều mô hình |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Bảng giá](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Cần đăng ký trước để được cấp quyền](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Bảng giá](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat chỉ hỗ trợ một số mô hình nhất định](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Làm theo hướng dẫn bên dưới để _cấu hình_ kho lưu trữ này sử dụng với các nhà cung cấp khác nhau. Các bài tập yêu cầu một nhà cung cấp cụ thể sẽ có một trong các tag sau trong tên file:

- `aoai` - yêu cầu endpoint và key của Azure OpenAI
- `oai` - yêu cầu endpoint và key của OpenAI
- `hf` - yêu cầu token của Hugging Face

Bạn có thể cấu hình một, không hoặc tất cả các nhà cung cấp. Các bài tập liên quan sẽ báo lỗi nếu thiếu thông tin xác thực.

## Tạo file `.env`

Chúng tôi giả định bạn đã đọc hướng dẫn ở trên, đăng ký với nhà cung cấp phù hợp và lấy được thông tin xác thực cần thiết (API_KEY hoặc token). Với Azure OpenAI, bạn cũng cần có một dịch vụ Azure OpenAI đã triển khai (endpoint) với ít nhất một mô hình GPT phục vụ cho chat completion.

Bước tiếp theo là cấu hình **biến môi trường cục bộ** như sau:

1. Tìm file `.env.copy` trong thư mục gốc, file này sẽ có nội dung như sau:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Sao chép file đó thành `.env` bằng lệnh dưới đây. File này đã được _gitignore_, giúp bảo mật thông tin.

   ```bash
   cp .env.copy .env
   ```

3. Điền giá trị (thay thế các placeholder bên phải dấu `=`) như hướng dẫn ở phần tiếp theo.

4. (Tùy chọn) Nếu bạn sử dụng GitHub Codespaces, bạn có thể lưu biến môi trường dưới dạng _Codespaces secrets_ liên kết với kho lưu trữ này. Khi đó, bạn không cần tạo file .env cục bộ. **Tuy nhiên, lưu ý tùy chọn này chỉ áp dụng khi dùng GitHub Codespaces.** Nếu bạn dùng Docker Desktop, vẫn cần thiết lập file .env.

## Điền giá trị vào file `.env`

Hãy cùng điểm qua các tên biến để hiểu ý nghĩa của chúng:

| Biến  | Mô tả  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Đây là access token bạn tạo trong hồ sơ cá nhân |
| OPENAI_API_KEY | Đây là key xác thực để sử dụng dịch vụ OpenAI (không phải Azure) |
| AZURE_OPENAI_API_KEY | Đây là key xác thực để sử dụng dịch vụ Azure OpenAI |
| AZURE_OPENAI_ENDPOINT | Đây là endpoint đã triển khai cho tài nguyên Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Đây là endpoint triển khai mô hình _text generation_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Đây là endpoint triển khai mô hình _text embeddings_ |
| | |

Lưu ý: Hai biến cuối của Azure OpenAI phản ánh mô hình mặc định cho chat completion (tạo văn bản) và tìm kiếm vector (embeddings). Hướng dẫn thiết lập sẽ có trong các bài tập liên quan.

## Cấu hình Azure: Từ Portal

Endpoint và key của Azure OpenAI sẽ được tìm thấy trong [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), hãy bắt đầu từ đây.

1. Truy cập [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Chọn mục **Keys and Endpoint** ở thanh bên (menu bên trái).
1. Nhấn **Show Keys** - bạn sẽ thấy: KEY 1, KEY 2 và Endpoint.
1. Dùng giá trị KEY 1 cho AZURE_OPENAI_API_KEY
1. Dùng giá trị Endpoint cho AZURE_OPENAI_ENDPOINT

Tiếp theo, chúng ta cần endpoint cho các mô hình đã triển khai.

1. Chọn mục **Model deployments** ở thanh bên (menu trái) của tài nguyên Azure OpenAI.
1. Ở trang đích, nhấn **Manage Deployments**

Bạn sẽ được chuyển đến trang Azure OpenAI Studio, nơi tìm các giá trị khác như mô tả bên dưới.

## Cấu hình Azure: Từ Studio

1. Truy cập [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **từ tài nguyên của bạn** như hướng dẫn ở trên.
1. Nhấn tab **Deployments** (thanh bên trái) để xem các mô hình đã triển khai.
1. Nếu mô hình bạn cần chưa được triển khai, dùng **Create new deployment** để triển khai.
1. Bạn cần một mô hình _text-generation_ - khuyến nghị: **gpt-35-turbo**
1. Bạn cần một mô hình _text-embedding_ - khuyến nghị **text-embedding-ada-002**

Bây giờ hãy cập nhật biến môi trường với _Deployment name_ đã sử dụng. Thông thường, tên này sẽ giống tên mô hình trừ khi bạn đã đổi tên. Ví dụ:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Đừng quên lưu file .env sau khi hoàn thành**. Bạn có thể đóng file và quay lại hướng dẫn chạy notebook.

## Cấu hình OpenAI: Từ hồ sơ cá nhân

API key của bạn có thể tìm thấy trong [tài khoản OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Nếu chưa có, bạn có thể đăng ký tài khoản và tạo API key. Sau khi có key, hãy điền vào biến `OPENAI_API_KEY` trong file `.env`.

## Cấu hình Hugging Face: Từ hồ sơ cá nhân

Token của bạn trên Hugging Face có thể tìm thấy trong hồ sơ cá nhân tại mục [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Không đăng tải hoặc chia sẻ token này công khai. Thay vào đó, hãy tạo một token mới dành riêng cho dự án này và sao chép vào file `.env` dưới biến `HUGGING_FACE_API_KEY`. _Lưu ý:_ Về mặt kỹ thuật, đây không phải là API key nhưng được dùng để xác thực nên chúng tôi giữ cách đặt tên này cho nhất quán.

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.