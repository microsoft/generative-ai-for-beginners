# Lựa chọn & Cấu hình nhà cung cấp LLM 🔑

Bài tập **có thể** được thiết lập để làm việc với một hoặc nhiều triển khai Mô hình Ngôn ngữ Lớn (LLM) thông qua nhà cung cấp dịch vụ được hỗ trợ như OpenAI, Azure hoặc Hugging Face. Những nhà cung cấp này cung cấp một _điểm cuối được lưu trữ_ (API) mà chúng ta có thể truy cập chương trình với các thông tin xác thực phù hợp (khóa API hoặc token). Trong khóa học này, chúng ta thảo luận về các nhà cung cấp sau:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) với các mô hình đa dạng bao gồm loạt GPT cốt lõi.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) dành cho các mô hình OpenAI với trọng tâm là sẵn sàng cho doanh nghiệp
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) cung cấp một điểm cuối và khóa API duy nhất để truy cập hàng trăm mô hình từ OpenAI, Meta, Mistral, Cohere, Microsoft và nhiều hơn nữa (thay thế GitHub Models, sẽ ngừng hoạt động vào cuối tháng 7 năm 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) dành cho mô hình mã nguồn mở và máy chủ suy luận
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) hoặc [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) nếu bạn muốn chạy mô hình hoàn toàn ngoại tuyến trên thiết bị của mình, không cần đăng ký cloud

**Bạn sẽ cần sử dụng tài khoản riêng của mình cho các bài tập này**. Bài tập là tùy chọn nên bạn có thể chọn thiết lập một, tất cả hoặc không thiết lập nhà cung cấp nào dựa trên sở thích của bạn. Dưới đây là một số hướng dẫn đăng ký:

| Đăng ký | Chi phí | Khóa API | Khu vực thử nghiệm | Bình luận |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Giá cả](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Dựa trên dự án](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Không cần mã, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Nhiều mô hình có sẵn |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Giá cả](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Khởi động nhanh SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Khởi động nhanh Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Phải đăng ký trước để truy cập](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Giá cả](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Trang tổng quan dự án](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Khu vực thử nghiệm Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Có hạng mục miễn phí; một điểm cuối + khoá cho nhiều nhà cung cấp mô hình |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Giá cả](https://huggingface.co/pricing) | [Token truy cập](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat có giới hạn các mô hình](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Miễn phí (chạy trên thiết bị của bạn) | Không bắt buộc | [CLI/SDK Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Hoàn toàn ngoại tuyến, điểm cuối tương thích OpenAI |
| | | | | |

Làm theo hướng dẫn bên dưới để _cấu hình_ kho lưu trữ này để sử dụng với các nhà cung cấp khác nhau. Các bài tập yêu cầu nhà cung cấp cụ thể sẽ chứa một trong các thẻ này trong tên tệp của chúng:

- `aoai` - yêu cầu điểm cuối và khoá Azure OpenAI
- `oai` - yêu cầu điểm cuối và khoá OpenAI
- `hf` - yêu cầu token Hugging Face
- `githubmodels` - yêu cầu điểm cuối và khoá Microsoft Foundry Models (GitHub Models sẽ ngừng hoạt động vào cuối tháng 7 năm 2026)

Bạn có thể cấu hình một, không hoặc tất cả các nhà cung cấp. Các bài tập liên quan sẽ báo lỗi khi thiếu thông tin xác thực.

## Tạo file `.env`

Chúng tôi giả định rằng bạn đã đọc hướng dẫn ở trên và đăng ký với nhà cung cấp liên quan, đồng thời nhận được các thông tin xác thực cần thiết (API_KEY hoặc token). Trong trường hợp Azure OpenAI, chúng tôi giả định bạn cũng có một triển khai hợp lệ của Dịch vụ Azure OpenAI (điểm cuối) với ít nhất một mô hình GPT được triển khai cho hoàn thành cuộc trò chuyện.

Bước tiếp theo là cấu hình **biến môi trường cục bộ** của bạn như sau:

1. Tìm trong thư mục gốc tệp `.env.copy` mà nên có nội dung như sau:

   ```bash
   # Nhà cung cấp OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI trong Microsoft Foundry
   ## (Dịch vụ Azure OpenAI hiện là một phần của Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Mặc định đã được thiết lập! (phiên bản API ổn định GA hiện tại)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Mô hình Microsoft Foundry (danh mục mô hình đa nhà cung cấp, thay thế Mô hình GitHub, sẽ ngừng hoạt động vào cuối tháng 7 năm 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Sao chép tệp đó thành `.env` bằng lệnh dưới đây. Tệp này được _bỏ qua git_, giữ bí mật an toàn.

   ```bash
   cp .env.copy .env
   ```

3. Điền các giá trị (thay thế các chỗ giữ chỗ bên phải dấu `=`) như mô tả trong phần tiếp theo.

4. (Tùy chọn) Nếu bạn sử dụng GitHub Codespaces, bạn có thể lưu các biến môi trường dưới dạng _bí mật Codespaces_ liên kết với kho lưu trữ này. Trong trường hợp đó, bạn không cần thiết lập file .env cục bộ. **Tuy nhiên, lưu ý rằng tùy chọn này chỉ hoạt động nếu bạn sử dụng GitHub Codespaces.** Bạn vẫn cần thiết lập tệp .env nếu sử dụng Docker Desktop.

## Điền file `.env`

Hãy xem nhanh các tên biến để hiểu ý nghĩa của chúng:

| Biến | Mô tả |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Đây là token truy cập người dùng bạn thiết lập trong hồ sơ của bạn |
| OPENAI_API_KEY | Đây là khoá ủy quyền để sử dụng dịch vụ cho các điểm cuối OpenAI không phải Azure |
| AZURE_OPENAI_API_KEY | Đây là khoá ủy quyền để sử dụng dịch vụ đó |
| AZURE_OPENAI_ENDPOINT | Đây là điểm cuối đã được triển khai cho tài nguyên Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Đây là điểm triển khai mô hình _tạo văn bản_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Đây là điểm triển khai mô hình _tích hợp văn bản_ |
| AZURE_INFERENCE_ENDPOINT | Đây là điểm cuối cho dự án Microsoft Foundry của bạn, dùng cho Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Đây là khoá API cho dự án Microsoft Foundry của bạn |
| | |

Lưu ý: Hai biến Azure OpenAI cuối cùng phản ánh một mô hình mặc định cho hoàn thành trò chuyện (tạo văn bản) và tìm kiếm vector (embedding) tương ứng. Hướng dẫn thiết lập chúng sẽ được định nghĩa trong các bài tập liên quan.

## Cấu hình Azure OpenAI: Từ Portal

> **Lưu ý:** Dịch vụ Azure OpenAI hiện là một phần của [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Các tài nguyên và triển khai vẫn hiển thị trên Azure Portal, nhưng quản lý mô hình hàng ngày (triển khai, khu vực thử nghiệm, giám sát) giờ chuyển sang cổng Foundry thay vì "Azure OpenAI Studio" độc lập cũ.

Giá trị điểm cuối và khoá Azure OpenAI sẽ được tìm thấy trong [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), vậy hãy bắt đầu từ đó.

1. Truy cập [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Nhấp tùy chọn **Keys and Endpoint** trong thanh bên (menu bên trái).
1. Nhấp **Show Keys** - bạn sẽ thấy các mục: KEY 1, KEY 2 và Endpoint.
1. Dùng giá trị KEY 1 cho AZURE_OPENAI_API_KEY
1. Dùng giá trị Endpoint cho AZURE_OPENAI_ENDPOINT

Tiếp theo, chúng ta cần điểm cuối cho các mô hình cụ thể đã triển khai.

1. Nhấp lựa chọn **Model deployments** trong thanh bên (menu trái) cho tài nguyên Azure OpenAI.
1. Trong trang đích, nhấp **Go to Microsoft Foundry portal** (hoặc **Manage Deployments**, tùy loại tài nguyên)

Bạn sẽ được đưa đến cổng Microsoft Foundry, nơi chúng ta sẽ tìm các giá trị khác như mô tả bên dưới.

## Cấu hình Azure OpenAI: Từ cổng Microsoft Foundry

1. Điều hướng đến [Microsoft Foundry portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **từ tài nguyên của bạn** như mô tả trên.
1. Nhấp tab **Deployments** (thanh bên, bên trái) để xem các mô hình đã triển khai hiện có.
1. Nếu mô hình bạn muốn chưa được triển khai, dùng **Deploy model** để triển khai từ [danh mục mô hình](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Bạn sẽ cần một mô hình _text-generation_ - chúng tôi đề xuất: **gpt-4o-mini**
1. Bạn sẽ cần một mô hình _text-embedding_ - chúng tôi đề xuất **text-embedding-3-small**

Bây giờ cập nhật các biến môi trường phản ánh _Tên triển khai_ được sử dụng. Thông thường tên này sẽ giống với tên mô hình trừ khi bạn thay đổi rõ ràng. Ví dụ, bạn có thể có:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Đừng quên lưu tệp .env khi hoàn tất**. Bạn có thể đóng tệp và quay lại hướng dẫn chạy notebook.

## Cấu hình OpenAI: Từ Hồ sơ

Khóa API OpenAI của bạn có thể tìm thấy trong [tài khoản OpenAI của bạn](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Nếu bạn chưa có, bạn có thể đăng ký tài khoản và tạo khóa API. Khi có khóa, bạn có thể dùng nó để điền biến `OPENAI_API_KEY` trong tệp `.env`.

## Cấu hình Hugging Face: Từ Hồ sơ

Token Hugging Face của bạn có thể tìm thấy trong hồ sơ của bạn dưới [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Không đăng tải hoặc chia sẻ công khai các token này. Thay vào đó, tạo token mới cho dự án này và sao chép vào tệp `.env` trong biến `HUGGING_FACE_API_KEY`. _Lưu ý:_ Về kỹ thuật đây không phải là khóa API nhưng được dùng để xác thực nên chúng ta giữ tên gọi cho nhất quán.

## Cấu hình Microsoft Foundry Models: Từ Portal

> **Lưu ý:** GitHub Models sẽ ngừng hoạt động vào cuối tháng 7 năm 2026. Microsoft Foundry Models là bộ thay thế trực tiếp, cung cấp danh mục mẫu miễn phí thử và trải nghiệm SDK Azure AI Inference / OpenAI SDK tương tự.

1. Truy cập [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) và tạo (hoặc mở) một dự án Foundry.
1. Duyệt [danh mục mô hình](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) và triển khai một mô hình, ví dụ `gpt-4o-mini`.
1. Trên trang **Tổng quan** của dự án, sao chép **điểm cuối** và **khóa API**.
1. Dùng giá trị điểm cuối cho `AZURE_INFERENCE_ENDPOINT` và khóa API cho `AZURE_INFERENCE_CREDENTIAL` trong tệp `.env`.

## Nhà cung cấp Ngoại tuyến / Cục bộ

Nếu bạn không muốn sử dụng đăng ký đám mây, bạn có thể chạy các mô hình mã mở tương thích trực tiếp trên thiết bị của mình:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - môi trường chạy trên thiết bị của Microsoft. Nó tự động chọn nhà cung cấp thực thi tốt nhất (NPU, GPU hoặc CPU) và cung cấp điểm cuối tương thích OpenAI, giúp bạn tái sử dụng hầu hết mã mẫu trong khóa học này với thay đổi tối thiểu. Xem [tài liệu Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) để bắt đầu, hoặc cài đặt với `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - một lựa chọn phổ biến để chạy mô hình mở như Llama, Phi, Mistral và Gemma cục bộ.


Xem [Bài học 19: Xây dựng với SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) để có các ví dụ thực hành sử dụng cả hai tùy chọn.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->