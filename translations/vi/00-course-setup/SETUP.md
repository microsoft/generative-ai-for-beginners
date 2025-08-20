<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:33:31+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "vi"
}
-->
# Thiết Lập Môi Trường Phát Triển

Chúng tôi thiết lập kho mã và khóa học này với một [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) có runtime đa năng hỗ trợ phát triển Python3, .NET, Node.js và Java. Cấu hình liên quan được định nghĩa trong file `devcontainer.json` nằm trong thư mục `.devcontainer/` ở thư mục gốc của kho mã này.

Để kích hoạt dev container, bạn có thể khởi chạy nó trong [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (cho runtime trên đám mây) hoặc trong [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (cho runtime trên thiết bị cục bộ). Đọc [tài liệu này](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) để biết thêm chi tiết về cách dev container hoạt động trong VS Code.

> [!TIP]  
> Chúng tôi khuyên bạn nên sử dụng GitHub Codespaces để bắt đầu nhanh chóng với ít công sức. Nó cung cấp [quota sử dụng miễn phí](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) khá rộng rãi cho tài khoản cá nhân. Bạn có thể cấu hình [thời gian chờ](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) để tự động dừng hoặc xóa các codespace không hoạt động nhằm tối đa hóa việc sử dụng quota.

## 1. Thực Thi Bài Tập

Mỗi bài học sẽ có các bài tập _tùy chọn_ có thể được cung cấp bằng một hoặc nhiều ngôn ngữ lập trình như Python, .NET/C#, Java và JavaScript/TypeScript. Phần này cung cấp hướng dẫn chung liên quan đến việc thực thi các bài tập đó.

### 1.1 Bài Tập Python

Bài tập Python được cung cấp dưới dạng ứng dụng (`.py` files) hoặc sổ tay Jupyter (`.ipynb` files).  
- Để chạy sổ tay, mở nó trong Visual Studio Code rồi nhấn _Select Kernel_ (ở góc trên bên phải) và chọn tùy chọn Python 3 mặc định. Sau đó bạn có thể chọn _Run All_ để thực thi toàn bộ sổ tay.  
- Để chạy ứng dụng Python từ dòng lệnh, làm theo hướng dẫn cụ thể của từng bài tập để đảm bảo bạn chọn đúng file và cung cấp các tham số cần thiết.

## 2. Cấu Hình Nhà Cung Cấp

Bài tập **có thể** được thiết lập để làm việc với một hoặc nhiều triển khai Large Language Model (LLM) thông qua các nhà cung cấp dịch vụ được hỗ trợ như OpenAI, Azure hoặc Hugging Face. Các nhà cung cấp này cung cấp một _hosted endpoint_ (API) mà ta có thể truy cập lập trình với các thông tin xác thực phù hợp (API key hoặc token). Trong khóa học này, chúng ta sẽ tìm hiểu các nhà cung cấp sau:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) với nhiều mô hình đa dạng bao gồm cả dòng GPT chính.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) dành cho các mô hình OpenAI với khả năng sẵn sàng doanh nghiệp.
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) cho các mô hình mã nguồn mở và máy chủ suy luận.

**Bạn sẽ cần sử dụng tài khoản riêng của mình cho các bài tập này**. Các bài tập là tùy chọn nên bạn có thể chọn thiết lập một, tất cả hoặc không thiết lập nhà cung cấp nào tùy theo sở thích. Một số hướng dẫn đăng ký:

| Đăng ký | Chi phí | API Key | Playground | Ghi chú |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Bảng giá](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Dựa trên dự án](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Không cần code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Có nhiều mô hình khác nhau |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Bảng giá](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Phải đăng ký trước để được truy cập](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Bảng giá](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat có mô hình giới hạn](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Làm theo hướng dẫn dưới đây để _cấu hình_ kho mã này sử dụng với các nhà cung cấp khác nhau. Các bài tập yêu cầu nhà cung cấp cụ thể sẽ có một trong các tag sau trong tên file:  
 - `aoai` - yêu cầu endpoint và key Azure OpenAI  
 - `oai` - yêu cầu endpoint và key OpenAI  
 - `hf` - yêu cầu token Hugging Face  

Bạn có thể cấu hình một, không hoặc tất cả các nhà cung cấp. Các bài tập liên quan sẽ báo lỗi nếu thiếu thông tin xác thực.

###  2.1. Tạo file `.env`

Chúng tôi giả định bạn đã đọc hướng dẫn trên và đăng ký với nhà cung cấp phù hợp, đồng thời đã có thông tin xác thực cần thiết (API_KEY hoặc token). Với Azure OpenAI, giả định bạn cũng đã có một triển khai hợp lệ của dịch vụ Azure OpenAI (endpoint) với ít nhất một mô hình GPT được triển khai cho chat completion.

Bước tiếp theo là cấu hình **biến môi trường cục bộ** như sau:

1. Tìm file `.env.copy` trong thư mục gốc, file này có nội dung tương tự như sau:

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

2. Sao chép file đó thành `.env` bằng lệnh dưới đây. File này được _gitignore_, giúp giữ bí mật an toàn.

   ```bash
   cp .env.copy .env
   ```

3. Điền các giá trị (thay thế các placeholder bên phải dấu `=`) như mô tả trong phần tiếp theo.

3. (Tùy chọn) Nếu bạn dùng GitHub Codespaces, bạn có thể lưu biến môi trường dưới dạng _Codespaces secrets_ liên kết với kho mã này. Trong trường hợp đó, bạn không cần tạo file .env cục bộ. **Tuy nhiên, lưu ý rằng tùy chọn này chỉ hoạt động khi bạn dùng GitHub Codespaces.** Nếu dùng Docker Desktop, bạn vẫn cần tạo file .env.

### 2.2. Điền thông tin vào file `.env`

Hãy xem qua tên các biến để hiểu ý nghĩa của chúng:

| Biến  | Mô tả  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Đây là token truy cập người dùng bạn thiết lập trong hồ sơ cá nhân |
| OPENAI_API_KEY | Đây là khóa ủy quyền dùng dịch vụ cho các endpoint OpenAI không phải Azure |
| AZURE_OPENAI_API_KEY | Đây là khóa ủy quyền dùng dịch vụ Azure OpenAI |
| AZURE_OPENAI_ENDPOINT | Đây là endpoint đã triển khai cho tài nguyên Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Đây là endpoint triển khai mô hình _text generation_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Đây là endpoint triển khai mô hình _text embeddings_ |
| | |

Lưu ý: Hai biến Azure OpenAI cuối cùng phản ánh mô hình mặc định cho chat completion (tạo văn bản) và tìm kiếm vector (embeddings) tương ứng. Hướng dẫn thiết lập sẽ được mô tả trong các bài tập liên quan.

### 2.3 Cấu hình Azure: Từ Portal

Giá trị endpoint và key Azure OpenAI có thể tìm thấy trong [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), vậy hãy bắt đầu từ đó.

1. Truy cập [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
2. Nhấn vào tùy chọn **Keys and Endpoint** trong thanh bên (menu bên trái).  
3. Nhấn **Show Keys** - bạn sẽ thấy các mục: KEY 1, KEY 2 và Endpoint.  
4. Dùng giá trị KEY 1 cho biến AZURE_OPENAI_API_KEY  
5. Dùng giá trị Endpoint cho biến AZURE_OPENAI_ENDPOINT  

Tiếp theo, ta cần lấy endpoint cho các mô hình cụ thể đã triển khai.

1. Nhấn vào tùy chọn **Model deployments** trong thanh bên (menu trái) của tài nguyên Azure OpenAI.  
2. Ở trang đích, nhấn **Manage Deployments**  

Điều này sẽ đưa bạn đến trang web Azure OpenAI Studio, nơi bạn sẽ tìm thấy các giá trị khác như mô tả dưới đây.

### 2.4 Cấu hình Azure: Từ Studio

1. Truy cập [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **từ tài nguyên của bạn** như đã mô tả ở trên.  
2. Nhấn tab **Deployments** (thanh bên trái) để xem các mô hình đã triển khai hiện tại.  
3. Nếu mô hình bạn muốn chưa được triển khai, hãy dùng **Create new deployment** để triển khai nó.  
4. Bạn sẽ cần một mô hình _text-generation_ - chúng tôi khuyên dùng: **gpt-35-turbo**  
5. Bạn sẽ cần một mô hình _text-embedding_ - chúng tôi khuyên dùng **text-embedding-ada-002**  

Bây giờ cập nhật các biến môi trường để phản ánh _Tên triển khai_ được sử dụng. Thông thường tên này sẽ giống tên mô hình trừ khi bạn đổi tên rõ ràng. Ví dụ, bạn có thể có:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Đừng quên lưu file .env khi hoàn tất**. Bạn có thể đóng file và quay lại hướng dẫn chạy sổ tay.

### 2.5 Cấu hình OpenAI: Từ Hồ Sơ

Khóa API OpenAI của bạn có thể tìm thấy trong [tài khoản OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Nếu chưa có, bạn có thể đăng ký tài khoản và tạo khóa API. Khi có khóa, bạn dùng nó để điền vào biến `OPENAI_API_KEY` trong file `.env`.

### 2.6 Cấu hình Hugging Face: Từ Hồ Sơ

Token Hugging Face của bạn có thể tìm thấy trong hồ sơ cá nhân tại mục [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Không đăng tải hoặc chia sẻ token này công khai. Thay vào đó, tạo một token mới cho dự án này và sao chép vào file `.env` dưới biến `HUGGING_FACE_API_KEY`. _Lưu ý:_ Về kỹ thuật đây không phải là API key nhưng được dùng để xác thực nên chúng tôi giữ tên biến cho đồng nhất.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.