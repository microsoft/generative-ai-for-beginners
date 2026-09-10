# AGENTS.md

## Tổng quan dự án

Kho lưu trữ này chứa một chương trình giảng dạy toàn diện gồm 21 bài học về các kiến thức cơ bản và phát triển ứng dụng AI Tổng hợp. Khóa học dành cho người mới bắt đầu và bao quát mọi thứ từ các khái niệm cơ bản đến xây dựng các ứng dụng sẵn sàng đưa vào sản xuất.

**Công nghệ chính:**
- Python 3.9+ với các thư viện: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript với Node.js và các thư viện: `openai` (Azure OpenAI qua endpoint v1 + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Dịch vụ Azure OpenAI, OpenAI API, và Microsoft Foundry Models (GitHub Models sẽ ngừng hoạt động vào cuối tháng 7 năm 2026)
- Jupyter Notebooks cho học tập tương tác
- Dev Containers cho môi trường phát triển nhất quán

**Cấu trúc kho lưu trữ:**
- 21 thư mục bài học đánh số (00-21) chứa README, ví dụ mã, và bài tập
- Nhiều triển khai: Python, TypeScript, và đôi khi có ví dụ .NET
- Thư mục bản dịch với hơn 40 phiên bản ngôn ngữ
- Cấu hình tập trung qua tệp `.env` (dùng `.env.copy` làm mẫu)

## Lệnh Thiết lập

### Thiết lập kho lưu trữ ban đầu

```bash
# Sao chép kho lưu trữ
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Sao chép mẫu môi trường
cp .env.copy .env
# Chỉnh sửa .env với khóa API và điểm cuối của bạn
```

### Thiết lập môi trường Python

```bash
# Tạo môi trường ảo
python3 -m venv venv

# Kích hoạt môi trường ảo
# Trên macOS/Linux:
source venv/bin/activate
# Trên Windows:
venv\Scripts\activate

# Cài đặt các phụ thuộc
pip install -r requirements.txt
```

### Thiết lập Node.js/TypeScript

```bash
# Cài đặt các phụ thuộc cấp root (cho công cụ tài liệu)
npm install

# Đối với các ví dụ TypeScript của từng bài học, điều hướng đến bài học cụ thể:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Thiết lập Dev Container (Khuyến nghị)

Kho lưu trữ bao gồm cấu hình `.devcontainer` cho GitHub Codespaces hoặc VS Code Dev Containers:

1. Mở kho lưu trữ trong GitHub Codespaces hoặc VS Code với tiện ích Dev Containers
2. Dev Container sẽ tự động:
   - Cài đặt các phụ thuộc Python từ `requirements.txt`
   - Chạy script post-create (`.devcontainer/post-create.sh`)
   - Thiết lập kernel Jupyter

## Quy trình phát triển

### Biến môi trường

Tất cả các bài học cần truy cập API sử dụng các biến môi trường được định nghĩa trong `.env`:

- `OPENAI_API_KEY` - Dùng cho OpenAI API
- `AZURE_OPENAI_API_KEY` - Dùng cho Azure OpenAI trong Microsoft Foundry (Dịch vụ Azure OpenAI hiện thuộc Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL endpoint Azure OpenAI (endpoint tài nguyên Foundry)
- `AZURE_OPENAI_DEPLOYMENT` - Tên triển khai mô hình chat completion (mặc định khóa học: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Tên triển khai mô hình embeddings (mặc định khóa học: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - Phiên bản API (mặc định: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Dùng cho các mô hình Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - Endpoint Microsoft Foundry Models (catalog mô hình đa nhà cung cấp)
- `AZURE_INFERENCE_CREDENTIAL` - Khóa API Microsoft Foundry Models (thay thế `GITHUB_TOKEN` sắp ngừng hoạt động)
- `AZURE_INFERENCE_CHAT_MODEL` - Một mô hình không suy luận (ví dụ: `Llama-3.3-70B-Instruct`) dùng trong các ví dụ `temperature`, vì các mô hình suy luận không hỗ trợ các điều khiển sampling

### Quy ước mô hình (quan trọng)

- **Mô hình chat mặc định là `gpt-5-mini`** - một mô hình **suy luận** hiện tại, chưa bị loại bỏ. Tính đến năm 2026 các mô hình "mini" hỗ trợ nhiệt độ cũ hơn (`gpt-4o-mini`, `gpt-4.1-mini`) đang *bị loại bỏ*, vì vậy chương trình chuẩn hóa sử dụng dòng GPT-5.
- **Các mô hình suy luận không chấp nhận `temperature` và `top_p`**, thay vào đó sử dụng `max_output_tokens` (Responses API) / `max_completion_tokens` (chat completions) thay cho `max_tokens`. Không **thêm** các tham số `temperature`/`top_p`/`max_tokens` vào các mẫu gọi `gpt-5-mini`.
- **Để minh họa `temperature`**, các mẫu dùng mô hình **Llama** (`Llama-3.3-70B-Instruct`) qua endpoint Microsoft Foundry Models (`AZURE_INFERENCE_CHAT_MODEL`). Điều khiển mô hình suy luận bằng kỹ thuật prompt và các điều khiển suy luận thay vì núm sampling.
- **Fine-tuning (bài 18)** giữ `gpt-4.1-mini`: GPT-5 chỉ hỗ trợ fine-tuning gia cường (RFT), không hỗ trợ fine-tuning giám sát (SFT) như đã trình bày.
- Bài 20 (Mistral) và 21 (Meta) giữ `temperature`/`max_tokens` vì chúng nhắm vào mô hình Mistral/Llama, vốn hỗ trợ các tham số đó.

### Chạy ví dụ Python

```bash
# Điều hướng đến thư mục bài học
cd 06-text-generation-apps/python

# Chạy một tập lệnh Python
python aoai-app.py
```

### Chạy ví dụ TypeScript

```bash
# Điều hướng đến thư mục ứng dụng TypeScript
cd 06-text-generation-apps/typescript/recipe-app

# Xây dựng mã TypeScript
npm run build

# Chạy ứng dụng
npm start
```

### Chạy Jupyter Notebooks

```bash
# Khởi động Jupyter ở thư mục gốc của kho lưu trữ
jupyter notebook

# Hoặc sử dụng VS Code với tiện ích mở rộng Jupyter
```

### Làm việc với các loại bài học khác nhau

- **Bài học "Học"**: Tập trung vào tài liệu README.md và các khái niệm
- **Bài học "Xây dựng"**: Bao gồm ví dụ mã hoạt động bằng Python và TypeScript
- Mỗi bài học có README.md với lý thuyết, giải thích mã, và liên kết đến nội dung video

## Hướng dẫn phong cách mã

### Python

- Sử dụng `python-dotenv` để quản lý biến môi trường
- Import thư viện `openai` để tương tác API
- Dùng `pylint` để đánh giá mã (một số ví dụ có `# pylint: disable=all` để đơn giản)
- Tuân theo quy ước đặt tên PEP 8
- Lưu trữ thông tin API trong tệp `.env`, không lưu trong mã nguồn

### TypeScript

- Dùng gói `dotenv` để quản lý biến môi trường
- Cấu hình TypeScript trong `tsconfig.json` cho từng ứng dụng
- Dùng gói `openai` cho Azure OpenAI (chỉ định client tới endpoint `/openai/v1/` và gọi `client.responses.create`); dùng `@azure-rest/ai-inference` cho Microsoft Foundry Models
- Sử dụng `nodemon` để phát triển với tự động tải lại
- Xây dựng trước khi chạy: `npm run build` rồi `npm start`

### Quy ước chung

- Giữ ví dụ mã đơn giản và mang tính giáo dục
- Bao gồm các chú thích giải thích các khái niệm chính
- Mã của mỗi bài học phải tự chứa và có thể chạy được
- Sử dụng đặt tên nhất quán: tiền tố `aoai-` cho Azure OpenAI, `oai-` cho OpenAI API, `githubmodels-` cho Microsoft Foundry Models (giữ tiền tố cũ từ thời GitHub Models)

## Hướng dẫn tài liệu

### Phong cách Markdown

- Tất cả URL phải được bọc trong định dạng `[text](../../url)` không có khoảng trắng thừa
- Các liên kết tương đối phải bắt đầu bằng `./` hoặc `../`
- Tất cả liên kết tới miền Microsoft phải bao gồm ID theo dõi: `?WT.mc_id=academic-105485-koreyst`
- Không dùng địa phương quốc gia trong URL (tránh `/en-us/`)
- Hình ảnh được lưu trong thư mục `./images` với tên mô tả
- Dùng ký tự tiếng Anh, số và dấu gạch ngang trong tên file

### Hỗ trợ dịch thuật

- Kho lưu trữ hỗ trợ hơn 40 ngôn ngữ thông qua GitHub Actions tự động
- Bản dịch lưu trong thư mục `translations/`
- Không gửi bản dịch chưa hoàn chỉnh
- Không chấp nhận dịch máy
- Hình ảnh đã được dịch lưu trong thư mục `translated_images/`

## Kiểm thử và xác minh

### Kiểm tra trước khi gửi

Kho lưu trữ sử dụng GitHub Actions để xác minh. Trước khi gửi PR:

1. **Kiểm tra liên kết Markdown**:
   ```bash
   # Quy trình làm việc validate-markdown.yml kiểm tra:
   # - Đường dẫn tương đối bị hỏng
   # - Thiếu ID theo dõi trên các đường dẫn
   # - Thiếu ID theo dõi trên các URL
   # - URL có ngôn ngữ quốc gia
   # - URL bên ngoài bị hỏng
   ```

2. **Kiểm thử thủ công**:
   - Thử ví dụ Python: Kích hoạt venv và chạy script
   - Thử ví dụ TypeScript: `npm install`, `npm run build`, `npm start`
   - Xác nhận biến môi trường được cấu hình đúng
   - Kiểm tra các khóa API hoạt động trong ví dụ mã

3. **Ví dụ mã**:
   - Đảm bảo tất cả mã chạy không lỗi
   - Thử với cả Azure OpenAI và OpenAI API khi có thể
   - Xác nhận ví dụ dùng được với Microsoft Foundry Models khi hỗ trợ

### Không có kiểm thử tự động

Đây là kho lưu trữ giáo dục tập trung vào bài học và ví dụ. Không có kiểm thử đơn vị hay kiểm thử tích hợp. Xác minh chủ yếu là:
- Kiểm thử thủ công các ví dụ mã
- GitHub Actions để kiểm tra Markdown
- Đánh giá nội dung học tập bởi cộng đồng

## Hướng dẫn Pull Request

### Trước khi gửi

1. Kiểm thử thay đổi mã trong cả Python và TypeScript khi có thể
2. Chạy kiểm tra Markdown (tự động chạy khi PR)
3. Đảm bảo có ID theo dõi trên tất cả URL Microsoft
4. Kiểm tra các liên kết tương đối hợp lệ
5. Xác minh tham chiếu hình ảnh chính xác

### Định dạng tiêu đề PR

- Dùng tiêu đề mô tả: `[Lesson 06] Sửa lỗi chính tả ví dụ Python` hoặc `Cập nhật README cho bài 08`
- Tham chiếu số issue nếu có: `Fixes #123`

### Mô tả PR

- Giải thích thay đổi gì và tại sao
- Liên kết tới các issue liên quan
- Với thay đổi mã, chỉ rõ các ví dụ đã thử nghiệm
- Với PR dịch thuật, bao gồm tất cả file để bản dịch đầy đủ

### Yêu cầu đóng góp

- Ký Microsoft CLA (tự động khi PR đầu tiên)
- Fork kho lưu trữ vào tài khoản của bạn trước khi thay đổi
- Một PR cho một thay đổi logic (không gộp các sửa chữa không liên quan)
- Giữ PR tập trung và nhỏ nếu có thể

## Quy trình thường gặp

### Thêm ví dụ mã mới

1. Điều hướng tới thư mục bài học tương ứng
2. Tạo ví dụ trong thư mục con `python/` hoặc `typescript/`
3. Tuân theo quy ước đặt tên: `{provider}-{example-name}.{py|ts|js}`
4. Thử với thông tin đăng nhập API thực tế
5. Ghi chú các biến môi trường mới trong README bài học

### Cập nhật tài liệu

1. Chỉnh sửa README.md trong thư mục bài học
2. Tuân thủ hướng dẫn Markdown (ID theo dõi, liên kết tương đối)
3. Cập nhật bản dịch được xử lý bởi GitHub Actions (không chỉnh sửa thủ công)
4. Kiểm tra mọi liên kết đều hợp lệ

### Làm việc với Dev Containers

1. Kho lưu trữ bao gồm `.devcontainer/devcontainer.json`
2. Script post-create tự động cài đặt phụ thuộc Python
3. Tiện ích mở rộng Python và Jupyter đã được cấu hình sẵn
4. Môi trường dựa trên `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Triển khai và Xuất bản

Đây là kho học tập - không có quy trình triển khai. Chương trình được sử dụng qua:

1. **Kho GitHub**: Truy cập trực tiếp mã và tài liệu
2. **GitHub Codespaces**: Môi trường phát triển tức thì với thiết lập sẵn
3. **Microsoft Learn**: Nội dung có thể được phát hành trên nền tảng học chính thức
4. **docsify**: Trang tài liệu xây dựng từ Markdown (xem `docsifytopdf.js` và `package.json`)

### Xây dựng trang tài liệu

```bash
# Tạo PDF từ tài liệu (nếu cần)
npm run convert
```

## Khắc phục sự cố

### Vấn đề thường gặp

**Lỗi import Python**:
- Đảm bảo môi trường ảo được kích hoạt
- Chạy `pip install -r requirements.txt`
- Kiểm tra phiên bản Python là 3.9+

**Lỗi build TypeScript**:
- Chạy `npm install` trong thư mục ứng dụng cụ thể
- Kiểm tra phiên bản Node.js tương thích
- Xoá thư mục `node_modules` và cài lại nếu cần thiết

**Lỗi xác thực API**:
- Xác nhận tệp `.env` tồn tại và có giá trị đúng
- Kiểm tra các khóa API hợp lệ và chưa hết hạn
- Đảm bảo URL endpoint đúng vùng của bạn

**Thiếu biến môi trường**:
- Sao chép `.env.copy` thành `.env`
- Điền đầy đủ các giá trị cần thiết cho bài học bạn đang làm
- Khởi động lại ứng dụng sau khi cập nhật `.env`

## Tài nguyên bổ sung

- [Hướng dẫn thiết lập khóa học](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Hướng dẫn đóng góp](./CONTRIBUTING.md)
- [Bộ quy tắc ứng xử](./CODE_OF_CONDUCT.md)
- [Chính sách bảo mật](./SECURITY.md)
- [Discord Azure AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Bộ sưu tập ví dụ mã nâng cao](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Ghi chú riêng về dự án

- Đây là **kho lưu trữ giáo dục** tập trung vào học tập, không phải mã sản xuất
- Ví dụ được thiết kế đơn giản và tập trung vào giảng dạy khái niệm
- Chất lượng mã được cân bằng với độ rõ ràng giáo dục
- Mỗi bài học là tự chứa và có thể hoàn thành độc lập
- Kho hỗ trợ nhiều nhà cung cấp API: Azure OpenAI, OpenAI, Microsoft Foundry Models, và nhà cung cấp ngoại tuyến như Foundry Local và Ollama
- Nội dung đa ngôn ngữ với quy trình dịch tự động
- Cộng đồng hoạt động trên Discord để hỏi đáp và hỗ trợ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->