# Lựa chọn & Cấu hình Nhà cung cấp LLM 🔑

Bài tập **cũng có thể** được thiết lập để hoạt động với một hoặc nhiều triển khai Mô hình Ngôn ngữ Lớn (LLM) thông qua nhà cung cấp dịch vụ được hỗ trợ như OpenAI, Azure hoặc Hugging Face. Những nhà cung cấp này cung cấp một _điểm cuối được lưu trữ_ (API) mà chúng ta có thể truy cập một cách lập trình với các thông tin xác thực phù hợp (khóa API hoặc token). Trong khóa học này, chúng ta sẽ thảo luận về các nhà cung cấp sau:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) với các mô hình đa dạng bao gồm loạt GPT chính.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) dành cho các mô hình OpenAI với trọng tâm là sẵn sàng cho doanh nghiệp
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) với một điểm cuối và khóa API duy nhất để truy cập hàng trăm mô hình từ OpenAI, Meta, Mistral, Cohere, Microsoft và nhiều hơn nữa (thay thế GitHub Models, sẽ ngừng hoạt động vào cuối tháng 7 năm 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) cho các mô hình mã nguồn mở và máy chủ suy luận
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) hoặc [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) nếu bạn muốn chạy các mô hình hoàn toàn ngoại tuyến trên thiết bị của riêng bạn mà không cần đăng ký đám mây

**Bạn sẽ cần sử dụng tài khoản của riêng bạn cho các bài tập này**. Bài tập là tùy chọn nên bạn có thể chọn thiết lập một, tất cả - hoặc không sử dụng nhà cung cấp nào dựa trên sở thích của bạn. Dưới đây là một số hướng dẫn đăng ký:

| Đăng ký | Chi phí | Khóa API | Playground | Bình luận |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Giá](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Dựa trên dự án](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Không cần mã, trên web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Nhiều mô hình có sẵn |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Giá](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Khởi đầu SDK](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Khởi đầu Studio](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Cần đăng ký truy cập trước](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Giá](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Trang tổng quan dự án](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Playground Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Có tầng miễn phí; một điểm cuối + khóa cho nhiều nhà cung cấp mô hình |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Giá](https://huggingface.co/pricing) | [Token truy cập](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat có mô hình hạn chế](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Miễn phí (chạy trên thiết bị của bạn) | Không cần | [CLI/SDK địa phương](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Điểm cuối tương thích OpenAI hoàn toàn ngoại tuyến |
| | | | | |

Làm theo hướng dẫn bên dưới để _cấu hình_ kho lưu trữ này sử dụng với các nhà cung cấp khác nhau. Các bài tập yêu cầu nhà cung cấp cụ thể sẽ có một trong những thẻ này trong tên tệp:

- `aoai` - yêu cầu điểm cuối và khóa Azure OpenAI
- `oai` - yêu cầu điểm cuối và khóa OpenAI
- `hf` - yêu cầu token Hugging Face
- `githubmodels` - yêu cầu điểm cuối và khóa Microsoft Foundry Models (GitHub Models sẽ ngừng hoạt động vào cuối tháng 7 năm 2026)

Bạn có thể cấu hình một, không hoặc tất cả các nhà cung cấp. Các bài tập liên quan sẽ báo lỗi khi thiếu thông tin xác thực.

## Tạo tệp `.env`

Chúng tôi giả định bạn đã đọc hướng dẫn ở trên, đăng ký với nhà cung cấp tương ứng và có được các thông tin xác thực cần thiết (API_KEY hoặc token). Trong trường hợp Azure OpenAI, chúng tôi giả định bạn cũng có một triển khai hợp lệ của Dịch vụ Azure OpenAI (điểm cuối) với ít nhất một mô hình GPT được triển khai cho hoàn thành trò chuyện.

Bước tiếp theo là cấu hình **biến môi trường cục bộ** của bạn như sau:

1. Tìm trong thư mục gốc một tệp `.env.copy` có nội dung như sau:

   ```bash
   # Nhà cung cấp OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI trong Microsoft Foundry
   ## (Dịch vụ Azure OpenAI hiện là một phần của Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Mặc định đã được đặt! (phiên bản API ổn định GA hiện tại)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Mô hình Microsoft Foundry (danh mục mô hình đa nhà cung cấp, thay thế Mô hình GitHub, sẽ ngừng hoạt động vào cuối tháng 7 năm 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Sao chép tệp đó thành `.env` bằng lệnh dưới đây. Tệp này được _gitignore_, giữ bí mật an toàn.

   ```bash
   cp .env.copy .env
   ```

3. Điền các giá trị (thay thế chỗ giữ chỗ ở bên phải dấu `=`) như mô tả trong phần tiếp theo.

4. (Tùy chọn) Nếu bạn sử dụng GitHub Codespaces, bạn có thể lưu biến môi trường dưới dạng _bí mật Codespaces_ liên kết với kho lưu trữ này. Trong trường hợp đó, bạn sẽ không cần cấu hình tệp .env cục bộ. **Tuy nhiên, lưu ý rằng tùy chọn này chỉ hoạt động nếu bạn sử dụng GitHub Codespaces.** Bạn vẫn cần thiết lập tệp .env nếu sử dụng Docker Desktop.

## Điền tệp `.env`

Hãy cùng xem qua tên các biến để hiểu chúng đại diện cho gì:

| Biến  | Mô tả  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Đây là token truy cập người dùng bạn đã thiết lập trong hồ sơ của mình |
| OPENAI_API_KEY | Đây là khóa ủy quyền để sử dụng dịch vụ với điểm cuối không phải Azure OpenAI |
| AZURE_OPENAI_API_KEY | Đây là khóa ủy quyền để sử dụng dịch vụ Azure OpenAI |
| AZURE_OPENAI_ENDPOINT | Đây là điểm cuối đã được triển khai cho tài nguyên Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Đây là điểm cuối triển khai mô hình _tạo văn bản_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Đây là điểm cuối triển khai mô hình _nhúng văn bản_ |
| AZURE_INFERENCE_ENDPOINT | Đây là điểm cuối cho dự án Microsoft Foundry của bạn, dùng cho Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Đây là khóa API cho dự án Microsoft Foundry của bạn |
| | |

Lưu ý: Hai biến Azure OpenAI cuối phản ánh mô hình mặc định cho hoàn thành trò chuyện (tạo văn bản) và tìm kiếm vector (nhúng) tương ứng. Hướng dẫn thiết lập chúng sẽ được định nghĩa trong các bài tập liên quan.

## Cấu hình Azure OpenAI: Từ Cổng

> **Lưu ý:** Dịch vụ Azure OpenAI giờ là một phần của [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Các tài nguyên và triển khai vẫn hiển thị trong Azure Portal, nhưng quản lý mô hình hàng ngày (triển khai, playground, giám sát) bây giờ diễn ra trong cổng Foundry thay vì "Azure OpenAI Studio" độc lập cũ.

Giá trị điểm cuối và khóa Azure OpenAI sẽ được tìm thấy trong [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), bắt đầu từ đó nhé.

1. Vào [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Nhấp vào tùy chọn **Keys and Endpoint** trong thanh bên (menu bên trái).
1. Nhấp vào **Show Keys** - bạn sẽ thấy các mục: KEY 1, KEY 2 và Endpoint.
1. Sử dụng giá trị KEY 1 cho AZURE_OPENAI_API_KEY
1. Sử dụng giá trị Endpoint cho AZURE_OPENAI_ENDPOINT

Tiếp theo, cần có điểm cuối cho các mô hình cụ thể bạn đã triển khai.

1. Nhấp vào tùy chọn **Model deployments** trong thanh bên (menu trái) cho tài nguyên Azure OpenAI.
1. Ở trang đích, nhấn **Go to Microsoft Foundry portal** (hoặc **Manage Deployments**, tùy loại tài nguyên)

Điều này sẽ đưa bạn đến cổng Microsoft Foundry, nơi chúng ta sẽ tìm các giá trị khác như mô tả bên dưới.

## Cấu hình Azure OpenAI: Từ cổng Microsoft Foundry

1. Truy cập [cổng Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **từ tài nguyên của bạn** như hướng dẫn phía trên.
1. Nhấp tab **Deployments** (bên trái) để xem các mô hình đã triển khai hiện tại.
1. Nếu mô hình bạn muốn chưa được triển khai, dùng **Deploy model** để triển khai từ [danh mục mô hình](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Bạn sẽ cần mô hình _text-generation_ - chúng tôi khuyên dùng: **gpt-5-mini**
1. Bạn sẽ cần mô hình _text-embedding_ - chúng tôi khuyên dùng **text-embedding-3-small**

Bây giờ cập nhật các biến môi trường để phản ánh tên _Deployment_ sử dụng. Thông thường, nó sẽ giống tên mô hình trừ khi bạn đổi tên rõ ràng. Ví dụ bạn có thể có:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Đừng quên lưu tệp .env khi xong**. Bạn có thể thoát tệp và tiếp tục với hướng dẫn chạy notebook.

## Cấu hình OpenAI: Từ Hồ sơ

Khóa API OpenAI của bạn có thể thấy trong [tài khoản OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Nếu bạn chưa có, hãy đăng ký tài khoản và tạo khóa API. Sau khi có khóa, hãy điền vào biến `OPENAI_API_KEY` trong tệp `.env`.

## Cấu hình Hugging Face: Từ Hồ sơ

Token Hugging Face của bạn tìm thấy trong hồ sơ tại [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Không đăng công khai hoặc chia sẻ rộng rãi. Thay vào đó, tạo một token mới dùng cho dự án này và sao chép vào tệp `.env` dưới biến `HUGGING_FACE_API_KEY`. _Lưu ý:_ Về kỹ thuật đây không phải khóa API nhưng được dùng để xác thực nên giữ tên biến cho nhất quán.

## Cấu hình Microsoft Foundry Models: Từ Cổng

> **Lưu ý:** GitHub Models sẽ ngừng hoạt động vào cuối tháng 7 năm 2026. Microsoft Foundry Models là thay thế trực tiếp, cung cấp cùng catalog mô hình miễn phí dùng thử và trải nghiệm Azure AI Inference SDK / OpenAI SDK.

1. Vào [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) và tạo hoặc mở dự án Foundry.
1. Duyệt trong [danh mục mô hình](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) và triển khai một mô hình, ví dụ `gpt-5-mini`.
1. Trên trang **Tổng quan** của dự án, sao chép **điểm cuối** và **khóa API**.
1. Sử dụng giá trị điểm cuối cho `AZURE_INFERENCE_ENDPOINT` và khóa API cho `AZURE_INFERENCE_CREDENTIAL` trong tệp `.env`.

## Nhà cung cấp chạy ngoại tuyến / cục bộ

Nếu bạn không muốn dùng đăng ký đám mây, bạn có thể chạy các mô hình mở tương thích trực tiếp trên thiết bị của mình:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - môi trường chạy trên thiết bị của Microsoft. Nó tự động chọn nhà cung cấp thực thi tốt nhất (NPU, GPU, hoặc CPU) và cung cấp điểm cuối tương thích OpenAI, nên bạn có thể sử dụng lại hầu hết mã mẫu trong khóa học này với ít thay đổi. Xem [tài liệu Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) để bắt đầu, hoặc cài đặt bằng `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - một lựa chọn phổ biến để chạy các mô hình mở như Llama, Phi, Mistral, và Gemma cục bộ.


Xem [Bài học 19: Xây dựng với SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) để biết các ví dụ thực hành sử dụng cả hai tùy chọn.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->