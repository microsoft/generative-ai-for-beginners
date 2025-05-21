<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:53:59+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "vi"
}
-->
# Thiết lập môi trường phát triển của bạn

Chúng tôi thiết lập kho lưu trữ này và khóa học với một [container phát triển](https://containers.dev?WT.mc_id=academic-105485-koreyst) có runtime Universal hỗ trợ phát triển Python3, .NET, Node.js và Java. Cấu hình liên quan được định nghĩa trong tệp `devcontainer.json` nằm trong thư mục `.devcontainer/` ở gốc kho lưu trữ này.

Để kích hoạt container phát triển, khởi chạy nó trong [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (cho runtime được lưu trữ trên đám mây) hoặc trong [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (cho runtime được lưu trữ trên thiết bị cục bộ). Đọc [tài liệu này](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) để biết thêm chi tiết về cách container phát triển hoạt động trong VS Code.

> [!TIP]  
> Chúng tôi khuyên bạn nên sử dụng GitHub Codespaces để bắt đầu nhanh chóng với ít nỗ lực nhất. Nó cung cấp một [hạn mức sử dụng miễn phí](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) hào phóng cho các tài khoản cá nhân. Cấu hình [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) để dừng hoặc xóa các codespaces không hoạt động để tối đa hóa việc sử dụng hạn mức của bạn.

## 1. Thực hiện bài tập

Mỗi bài học sẽ có các bài tập _tùy chọn_ có thể được cung cấp trong một hoặc nhiều ngôn ngữ lập trình bao gồm: Python, .NET/C#, Java và JavaScript/TypeScript. Phần này cung cấp hướng dẫn chung liên quan đến việc thực hiện các bài tập đó.

### 1.1 Bài tập Python

Các bài tập Python được cung cấp dưới dạng ứng dụng (tệp `.py`) hoặc notebook Jupyter (tệp `.ipynb`).
- Để chạy notebook, mở nó trong Visual Studio Code sau đó nhấp vào _Select Kernel_ (ở góc trên bên phải) và chọn tùy chọn Python 3 mặc định hiển thị. Bạn có thể _Run All_ để thực hiện notebook.
- Để chạy ứng dụng Python từ dòng lệnh, hãy làm theo hướng dẫn cụ thể của bài tập để đảm bảo bạn chọn đúng tệp và cung cấp các đối số cần thiết.

## 2. Cấu hình nhà cung cấp

Các bài tập **có thể** cũng được thiết lập để làm việc với một hoặc nhiều triển khai Large Language Model (LLM) thông qua một nhà cung cấp dịch vụ hỗ trợ như OpenAI, Azure hoặc Hugging Face. Những nhà cung cấp này cung cấp một _điểm cuối lưu trữ_ (API) mà chúng ta có thể truy cập thông qua lập trình với các thông tin đăng nhập đúng (API key hoặc token). Trong khóa học này, chúng ta thảo luận về các nhà cung cấp này:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) với nhiều mô hình đa dạng bao gồm loạt GPT cốt lõi.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) cho các mô hình OpenAI với sự sẵn sàng cho doanh nghiệp.
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) cho các mô hình mã nguồn mở và máy chủ suy diễn.

**Bạn sẽ cần sử dụng tài khoản của riêng mình cho các bài tập này**. Các bài tập là tùy chọn nên bạn có thể chọn thiết lập một, tất cả - hoặc không - nhà cung cấp dựa trên sở thích của bạn. Một số hướng dẫn đăng ký:

| Đăng ký | Chi phí | API Key | Playground | Bình luận |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Giá](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Dựa trên dự án](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Không mã, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Nhiều mô hình có sẵn |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Giá](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Phải đăng ký trước để truy cập](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Giá](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat có mô hình hạn chế](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Làm theo hướng dẫn dưới đây để _cấu hình_ kho lưu trữ này để sử dụng với các nhà cung cấp khác nhau. Các bài tập yêu cầu một nhà cung cấp cụ thể sẽ chứa một trong những thẻ này trong tên tệp của chúng:

- `aoai` - yêu cầu điểm cuối Azure OpenAI, key
- `oai` - yêu cầu điểm cuối OpenAI, key
- `hf` - yêu cầu token Hugging Face

Bạn có thể cấu hình một, không hoặc tất cả các nhà cung cấp. Các bài tập liên quan sẽ chỉ lỗi khi thiếu thông tin đăng nhập.

### 2.1. Tạo tệp `.env`

Chúng tôi giả định rằng bạn đã đọc hướng dẫn ở trên và đăng ký với nhà cung cấp liên quan, và đã có thông tin đăng nhập cần thiết (API_KEY hoặc token). Trong trường hợp của Azure OpenAI, chúng tôi giả định rằng bạn cũng đã triển khai dịch vụ Azure OpenAI hợp lệ (điểm cuối) với ít nhất một mô hình GPT được triển khai để hoàn thành cuộc trò chuyện.

Bước tiếp theo là cấu hình **biến môi trường cục bộ** của bạn như sau:

1. Tìm trong thư mục gốc tệp `.env.copy` mà nội dung có thể như thế này:

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

2. Sao chép tệp đó sang `.env` bằng lệnh dưới đây. Tệp này được _gitignore-d_, giữ bí mật an toàn.

   ```bash
   cp .env.copy .env
   ```

3. Điền vào các giá trị (thay thế các chỗ giữ chỗ bên phải của `=`) như được mô tả trong phần tiếp theo.

3. (Tùy chọn) Nếu bạn sử dụng GitHub Codespaces, bạn có tùy chọn lưu các biến môi trường dưới dạng _Codespaces secrets_ liên kết với kho lưu trữ này. Trong trường hợp đó, bạn sẽ không cần thiết lập tệp .env cục bộ. **Tuy nhiên, lưu ý rằng tùy chọn này chỉ hoạt động nếu bạn sử dụng GitHub Codespaces.** Bạn vẫn cần thiết lập tệp .env nếu bạn sử dụng Docker Desktop.

### 2.2. Điền vào tệp `.env`

Hãy xem nhanh tên biến để hiểu chúng đại diện cho điều gì:

| Biến | Mô tả |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Đây là token truy cập người dùng mà bạn thiết lập trong hồ sơ của mình |
| OPENAI_API_KEY | Đây là key ủy quyền để sử dụng dịch vụ cho các điểm cuối không phải Azure OpenAI |
| AZURE_OPENAI_API_KEY | Đây là key ủy quyền để sử dụng dịch vụ đó |
| AZURE_OPENAI_ENDPOINT | Đây là điểm cuối được triển khai cho tài nguyên Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Đây là điểm cuối triển khai mô hình _text generation_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Đây là điểm cuối triển khai mô hình _text embeddings_ |
| | |

Lưu ý: Hai biến Azure OpenAI cuối cùng phản ánh mô hình mặc định cho hoàn thành cuộc trò chuyện (tạo văn bản) và tìm kiếm vector (embedding) tương ứng. Hướng dẫn thiết lập chúng sẽ được định nghĩa trong các bài tập liên quan.

### 2.3 Cấu hình Azure: Từ Portal

Các giá trị điểm cuối và key Azure OpenAI sẽ được tìm thấy trong [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) nên hãy bắt đầu từ đó.

1. Đi đến [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Nhấp vào tùy chọn **Keys and Endpoint** trong thanh bên (menu ở bên trái).
1. Nhấp vào **Show Keys** - bạn sẽ thấy: KEY 1, KEY 2 và Endpoint.
1. Sử dụng giá trị KEY 1 cho AZURE_OPENAI_API_KEY
1. Sử dụng giá trị Endpoint cho AZURE_OPENAI_ENDPOINT

Tiếp theo, chúng ta cần các điểm cuối cho các mô hình cụ thể mà chúng ta đã triển khai.

1. Nhấp vào tùy chọn **Model deployments** trong thanh bên (menu bên trái) cho tài nguyên Azure OpenAI.
1. Trên trang đích, nhấp vào **Manage Deployments**

Điều này sẽ đưa bạn đến trang web Azure OpenAI Studio, nơi chúng ta sẽ tìm các giá trị khác như được mô tả dưới đây.

### 2.4 Cấu hình Azure: Từ Studio

1. Điều hướng đến [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **từ tài nguyên của bạn** như đã mô tả ở trên.
1. Nhấp vào tab **Deployments** (thanh bên, bên trái) để xem các mô hình hiện đang triển khai.
1. Nếu mô hình mong muốn của bạn chưa được triển khai, sử dụng **Create new deployment** để triển khai nó.
1. Bạn sẽ cần một mô hình _text-generation_ - chúng tôi khuyên dùng: **gpt-35-turbo**
1. Bạn sẽ cần một mô hình _text-embedding_ - chúng tôi khuyên dùng **text-embedding-ada-002**

Bây giờ hãy cập nhật các biến môi trường để phản ánh tên _Deployment_ đã sử dụng. Điều này thường sẽ giống như tên mô hình trừ khi bạn thay đổi nó một cách rõ ràng. Vì vậy, ví dụ, bạn có thể có:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Đừng quên lưu tệp .env khi hoàn tất**. Bạn có thể thoát khỏi tệp và quay lại hướng dẫn để chạy notebook.

### 2.5 Cấu hình OpenAI: Từ Hồ sơ

API key của bạn OpenAI có thể được tìm thấy trong [tài khoản OpenAI của bạn](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Nếu bạn chưa có, bạn có thể đăng ký một tài khoản và tạo API key. Khi bạn có key, bạn có thể sử dụng nó để điền vào biến `OPENAI_API_KEY` trong tệp `.env`.

### 2.6 Cấu hình Hugging Face: Từ Hồ sơ

Token Hugging Face của bạn có thể được tìm thấy trong hồ sơ của bạn dưới [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Đừng đăng hoặc chia sẻ chúng công khai. Thay vào đó, tạo một token mới cho việc sử dụng dự án này và sao chép nó vào tệp `.env` dưới biến `HUGGING_FACE_API_KEY`. _Lưu ý:_ Đây về mặt kỹ thuật không phải là API key nhưng được sử dụng để xác thực nên chúng tôi giữ nguyên quy ước đặt tên đó để nhất quán.

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa của nó nên được coi là nguồn thông tin có thẩm quyền. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.