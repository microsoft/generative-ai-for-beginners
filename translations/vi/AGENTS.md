<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:06:37+00:00",
  "source_file": "AGENTS.md",
  "language_code": "vi"
}
-->
# AGENTS.md

## Tổng quan dự án

Kho lưu trữ này chứa một chương trình giảng dạy gồm 21 bài học toàn diện về các nguyên tắc cơ bản của AI tạo sinh và phát triển ứng dụng. Khóa học được thiết kế cho người mới bắt đầu và bao gồm mọi thứ từ các khái niệm cơ bản đến xây dựng ứng dụng sẵn sàng cho sản xuất.

**Công nghệ chính:**
- Python 3.9+ với các thư viện: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript với Node.js và các thư viện: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Dịch vụ Azure OpenAI, OpenAI API, và GitHub Models
- Jupyter Notebooks để học tương tác
- Dev Containers để đảm bảo môi trường phát triển nhất quán

**Cấu trúc kho lưu trữ:**
- 21 thư mục bài học được đánh số (00-21) chứa các tệp README, ví dụ mã, và bài tập
- Nhiều triển khai: Python, TypeScript, và đôi khi có cả ví dụ .NET
- Thư mục dịch với hơn 40 phiên bản ngôn ngữ
- Cấu hình tập trung qua tệp `.env` (sử dụng `.env.copy` làm mẫu)

## Lệnh thiết lập

### Thiết lập ban đầu cho kho lưu trữ

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Thiết lập môi trường Python

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Thiết lập Node.js/TypeScript

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Thiết lập Dev Container (Khuyến nghị)

Kho lưu trữ bao gồm cấu hình `.devcontainer` dành cho GitHub Codespaces hoặc Dev Containers của VS Code:

1. Mở kho lưu trữ trong GitHub Codespaces hoặc VS Code với tiện ích mở rộng Dev Containers
2. Dev Container sẽ tự động:
   - Cài đặt các phụ thuộc Python từ `requirements.txt`
   - Chạy script sau khi tạo (`.devcontainer/post-create.sh`)
   - Thiết lập kernel Jupyter

## Quy trình phát triển

### Biến môi trường

Tất cả các bài học yêu cầu truy cập API sử dụng các biến môi trường được định nghĩa trong `.env`:

- `OPENAI_API_KEY` - Dành cho OpenAI API
- `AZURE_OPENAI_API_KEY` - Dành cho dịch vụ Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL endpoint của Azure OpenAI
- `AZURE_OPENAI_DEPLOYMENT` - Tên triển khai mô hình hoàn thành hội thoại
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Tên triển khai mô hình embeddings
- `AZURE_OPENAI_API_VERSION` - Phiên bản API (mặc định: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Dành cho các mô hình Hugging Face
- `GITHUB_TOKEN` - Dành cho GitHub Models

### Chạy các ví dụ Python

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### Chạy các ví dụ TypeScript

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Chạy Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Làm việc với các loại bài học khác nhau

- **Bài học "Learn"**: Tập trung vào tài liệu README.md và các khái niệm
- **Bài học "Build"**: Bao gồm các ví dụ mã hoạt động bằng Python và TypeScript
- Mỗi bài học có một tệp README.md với lý thuyết, hướng dẫn mã, và liên kết đến nội dung video

## Hướng dẫn phong cách mã

### Python

- Sử dụng `python-dotenv` để quản lý biến môi trường
- Import thư viện `openai` để tương tác với API
- Sử dụng `pylint` để kiểm tra mã (một số ví dụ bao gồm `# pylint: disable=all` để đơn giản hóa)
- Tuân theo quy ước đặt tên PEP 8
- Lưu thông tin xác thực API trong tệp `.env`, không bao giờ trong mã

### TypeScript

- Sử dụng gói `dotenv` cho biến môi trường
- Cấu hình TypeScript trong `tsconfig.json` cho mỗi ứng dụng
- Sử dụng `@azure/openai` hoặc `@azure-rest/ai-inference` cho các dịch vụ Azure
- Sử dụng `nodemon` để phát triển với tính năng tự động tải lại
- Biên dịch trước khi chạy: `npm run build` sau đó `npm start`

### Quy ước chung

- Giữ các ví dụ mã đơn giản và mang tính giáo dục
- Bao gồm các chú thích giải thích các khái niệm chính
- Mã của mỗi bài học nên tự chứa và có thể chạy được
- Sử dụng cách đặt tên nhất quán: tiền tố `aoai-` cho Azure OpenAI, `oai-` cho OpenAI API, `githubmodels-` cho GitHub Models

## Hướng dẫn tài liệu

### Phong cách Markdown

- Tất cả các URL phải được bao bọc trong định dạng `[text](../../url)` mà không có khoảng trắng thừa
- Liên kết tương đối phải bắt đầu bằng `./` hoặc `../`
- Tất cả các liên kết đến miền Microsoft phải bao gồm ID theo dõi: `?WT.mc_id=academic-105485-koreyst`
- Không sử dụng các địa chỉ URL có ngôn ngữ cụ thể (tránh `/en-us/`)
- Hình ảnh được lưu trữ trong thư mục `./images` với tên mô tả
- Sử dụng ký tự tiếng Anh, số, và dấu gạch ngang trong tên tệp

### Hỗ trợ dịch thuật

- Kho lưu trữ hỗ trợ hơn 40 ngôn ngữ thông qua GitHub Actions tự động
- Các bản dịch được lưu trong thư mục `translations/`
- Không gửi các bản dịch không đầy đủ
- Không chấp nhận các bản dịch bằng máy
- Hình ảnh được dịch lưu trong thư mục `translated_images/`

## Kiểm tra và xác thực

### Kiểm tra trước khi gửi

Kho lưu trữ này sử dụng GitHub Actions để xác thực. Trước khi gửi PR:

1. **Kiểm tra liên kết Markdown**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Kiểm tra thủ công**:
   - Kiểm tra các ví dụ Python: Kích hoạt venv và chạy các script
   - Kiểm tra các ví dụ TypeScript: `npm install`, `npm run build`, `npm start`
   - Xác minh các biến môi trường được cấu hình chính xác
   - Kiểm tra rằng các khóa API hoạt động với các ví dụ mã

3. **Ví dụ mã**:
   - Đảm bảo tất cả mã chạy không có lỗi
   - Kiểm tra với cả Azure OpenAI và OpenAI API khi áp dụng
   - Xác minh các ví dụ hoạt động với GitHub Models nếu được hỗ trợ

### Không có kiểm tra tự động

Đây là một kho lưu trữ giáo dục tập trung vào các hướng dẫn và ví dụ. Không có kiểm tra đơn vị hoặc kiểm tra tích hợp nào cần chạy. Việc xác thực chủ yếu là:
- Kiểm tra thủ công các ví dụ mã
- GitHub Actions để xác thực Markdown
- Đánh giá nội dung giáo dục từ cộng đồng

## Hướng dẫn gửi Pull Request

### Trước khi gửi

1. Kiểm tra các thay đổi mã trong cả Python và TypeScript khi áp dụng
2. Chạy xác thực Markdown (tự động kích hoạt trên PR)
3. Đảm bảo các ID theo dõi có mặt trên tất cả các URL của Microsoft
4. Kiểm tra rằng các liên kết tương đối hợp lệ
5. Xác minh hình ảnh được tham chiếu đúng cách

### Định dạng tiêu đề PR

- Sử dụng tiêu đề mô tả: `[Lesson 06] Fix Python example typo` hoặc `Update README for lesson 08`
- Tham chiếu số vấn đề khi áp dụng: `Fixes #123`

### Mô tả PR

- Giải thích những gì đã thay đổi và lý do
- Liên kết đến các vấn đề liên quan
- Đối với thay đổi mã, chỉ rõ các ví dụ nào đã được kiểm tra
- Đối với PR dịch thuật, bao gồm tất cả các tệp để hoàn thành bản dịch

### Yêu cầu đóng góp

- Ký Microsoft CLA (tự động trên PR đầu tiên)
- Fork kho lưu trữ vào tài khoản của bạn trước khi thực hiện thay đổi
- Một PR cho mỗi thay đổi logic (không kết hợp các sửa lỗi không liên quan)
- Giữ PR tập trung và nhỏ gọn khi có thể

## Quy trình làm việc phổ biến

### Thêm một ví dụ mã mới

1. Điều hướng đến thư mục bài học phù hợp
2. Tạo ví dụ trong thư mục con `python/` hoặc `typescript/`
3. Tuân theo quy ước đặt tên: `{provider}-{example-name}.{py|ts|js}`
4. Kiểm tra với thông tin xác thực API thực tế
5. Tài liệu hóa bất kỳ biến môi trường mới nào trong README của bài học

### Cập nhật tài liệu

1. Chỉnh sửa README.md trong thư mục bài học
2. Tuân theo hướng dẫn Markdown (ID theo dõi, liên kết tương đối)
3. Cập nhật bản dịch được xử lý bởi GitHub Actions (không chỉnh sửa thủ công)
4. Kiểm tra tất cả các liên kết hợp lệ

### Làm việc với Dev Containers

1. Kho lưu trữ bao gồm `.devcontainer/devcontainer.json`
2. Script sau khi tạo tự động cài đặt các phụ thuộc Python
3. Các tiện ích mở rộng cho Python và Jupyter được cấu hình sẵn
4. Môi trường dựa trên `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Triển khai và xuất bản

Đây là một kho lưu trữ học tập - không có quy trình triển khai. Chương trình giảng dạy được sử dụng bởi:

1. **Kho lưu trữ GitHub**: Truy cập trực tiếp vào mã và tài liệu
2. **GitHub Codespaces**: Môi trường phát triển tức thì với thiết lập được cấu hình sẵn
3. **Microsoft Learn**: Nội dung có thể được đồng bộ hóa lên nền tảng học tập chính thức
4. **docsify**: Trang tài liệu được xây dựng từ Markdown (xem `docsifytopdf.js` và `package.json`)

### Xây dựng trang tài liệu

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Xử lý sự cố

### Các vấn đề phổ biến

**Lỗi import Python**:
- Đảm bảo môi trường ảo đã được kích hoạt
- Chạy `pip install -r requirements.txt`
- Kiểm tra phiên bản Python là 3.9+

**Lỗi biên dịch TypeScript**:
- Chạy `npm install` trong thư mục ứng dụng cụ thể
- Kiểm tra phiên bản Node.js tương thích
- Xóa `node_modules` và cài đặt lại nếu cần

**Lỗi xác thực API**:
- Xác minh tệp `.env` tồn tại và có giá trị chính xác
- Kiểm tra các khóa API hợp lệ và chưa hết hạn
- Đảm bảo URL endpoint chính xác cho khu vực của bạn

**Thiếu biến môi trường**:
- Sao chép `.env.copy` thành `.env`
- Điền tất cả các giá trị cần thiết cho bài học bạn đang làm
- Khởi động lại ứng dụng sau khi cập nhật `.env`

## Tài nguyên bổ sung

- [Hướng dẫn thiết lập khóa học](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Hướng dẫn đóng góp](./CONTRIBUTING.md)
- [Quy tắc ứng xử](./CODE_OF_CONDUCT.md)
- [Chính sách bảo mật](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Bộ sưu tập các ví dụ mã nâng cao](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Ghi chú cụ thể về dự án

- Đây là một **kho lưu trữ giáo dục** tập trung vào học tập, không phải mã sản xuất
- Các ví dụ được thiết kế đơn giản và tập trung vào việc giảng dạy các khái niệm
- Chất lượng mã được cân bằng với tính rõ ràng trong giáo dục
- Mỗi bài học là tự chứa và có thể hoàn thành độc lập
- Kho lưu trữ hỗ trợ nhiều nhà cung cấp API: Azure OpenAI, OpenAI, và GitHub Models
- Nội dung đa ngôn ngữ với quy trình dịch tự động
- Cộng đồng hoạt động trên Discord để đặt câu hỏi và hỗ trợ

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.