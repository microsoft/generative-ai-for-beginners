# AGENTS.md

## Tổng Quan Dự Án

Kho lưu trữ này chứa một chương trình giảng dạy đầy đủ gồm 21 bài học về cơ bản AI Tạo Sinh và phát triển ứng dụng. Khóa học được thiết kế dành cho người mới bắt đầu và bao quát từ các khái niệm cơ bản đến xây dựng các ứng dụng sẵn sàng sản xuất.

**Công Nghệ Chính:**
- Python 3.9+ với các thư viện: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript với Node.js và các thư viện: `openai` (Azure OpenAI qua endpoint v1 + API Responses), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Dịch vụ Azure OpenAI, API OpenAI, và Microsoft Foundry Models (GitHub Models sẽ ngừng hoạt động vào cuối tháng 7 năm 2026)
- Jupyter Notebooks cho học tương tác
- Dev Containers để có môi trường phát triển nhất quán

**Cấu Trúc Kho Lưu Trữ:**
- 21 thư mục bài học đánh số (00-21) chứa README, ví dụ mã, và bài tập
- Nhiều triển khai: Python, TypeScript, và đôi khi các ví dụ .NET
- Thư mục dịch thuật với hơn 40 phiên bản ngôn ngữ
- Cấu hình tập trung qua file `.env` (dùng `.env.copy` làm mẫu)

## Lệnh Thiết Lập

### Thiết Lập Kho Lưu Trữ Ban Đầu

```bash
# Sao chép kho lưu trữ
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Sao chép mẫu môi trường
cp .env.copy .env
# Chỉnh sửa .env với khóa API và điểm cuối của bạn
```

### Thiết Lập Môi Trường Python

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

### Thiết Lập Node.js/TypeScript

```bash
# Cài đặt các phụ thuộc cấp root (cho công cụ tài liệu)
npm install

# Đối với các ví dụ TypeScript từng bài học, điều hướng đến bài học cụ thể:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Thiết Lập Dev Container (Khuyến nghị)

Kho lưu trữ bao gồm cấu hình `.devcontainer` cho GitHub Codespaces hoặc VS Code Dev Containers:

1. Mở kho lưu trữ trong GitHub Codespaces hoặc VS Code với tiện ích Dev Containers
2. Dev Container sẽ tự động:
   - Cài đặt các phụ thuộc Python từ `requirements.txt`
   - Chạy script post-create (`.devcontainer/post-create.sh`)
   - Cấu hình kernel Jupyter

## Quy Trình Phát Triển

### Biến Môi Trường

Tất cả các bài học cần truy cập API sử dụng biến môi trường được định nghĩa trong `.env`:

- `OPENAI_API_KEY` - Cho API OpenAI
- `AZURE_OPENAI_API_KEY` - Cho Azure OpenAI trong Microsoft Foundry (Dịch vụ Azure OpenAI hiện là một phần của Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL endpoint Azure OpenAI (endpoint tài nguyên Foundry)
- `AZURE_OPENAI_DEPLOYMENT` - Tên triển khai mô hình chat completion
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Tên triển khai mô hình embeddings
- `AZURE_OPENAI_API_VERSION` - Phiên bản API (mặc định: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Cho mô hình Hugging Face
- `AZURE_INFERENCE_ENDPOINT` - Endpoint Microsoft Foundry Models (catalog mô hình đa nhà cung cấp)
- `AZURE_INFERENCE_CREDENTIAL` - Khóa API Microsoft Foundry Models (thay thế `GITHUB_TOKEN` sắp ngừng)

### Chạy Các Ví Dụ Python

```bash
# Điều hướng đến thư mục bài học
cd 06-text-generation-apps/python

# Chạy một script Python
python aoai-app.py
```

### Chạy Các Ví Dụ TypeScript

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
# Khởi động Jupyter trong thư mục gốc của kho lưu trữ
jupyter notebook

# Hoặc sử dụng VS Code với tiện ích mở rộng Jupyter
```

### Làm Việc Với Các Loại Bài Học Khác Nhau

- **Bài học "Học"**: Tập trung vào tài liệu README.md và lý thuyết
- **Bài học "Xây dựng"**: Bao gồm ví dụ mã chạy được bằng Python và TypeScript
- Mỗi bài học có README.md với lý thuyết, hướng dẫn mã và liên kết đến nội dung video

## Hướng Dẫn Phong Cách Mã

### Python

- Sử dụng `python-dotenv` để quản lý biến môi trường
- Import thư viện `openai` để tương tác API
- Dùng `pylint` để kiểm tra mã (một số ví dụ có `# pylint: disable=all` để đơn giản)
- Tuân thủ quy tắc đặt tên theo PEP 8
- Lưu trữ thông tin API trong file `.env`, không lưu trực tiếp trong mã

### TypeScript

- Sử dụng package `dotenv` cho biến môi trường
- Cấu hình TypeScript trong `tsconfig.json` cho từng ứng dụng
- Dùng package `openai` cho Azure OpenAI (chỉ định client tới endpoint `/openai/v1/` và gọi `client.responses.create`); dùng `@azure-rest/ai-inference` cho Microsoft Foundry Models
- Sử dụng `nodemon` để phát triển với tự động tải lại
- Xây dựng trước khi chạy: `npm run build` rồi `npm start`

### Quy Ước Chung

- Giữ các ví dụ mã đơn giản và mang tính giáo dục
- Bao gồm chú thích giải thích các khái niệm chính
- Mỗi đoạn mã của bài học phải đầy đủ và có thể chạy được
- Dùng tên gọi nhất quán: tiền tố `aoai-` cho Azure OpenAI, `oai-` cho OpenAI API, `githubmodels-` cho Microsoft Foundry Models (giữ tiền tố kế thừa từ thời GitHub Models)

## Hướng Dẫn Tài Liệu

### Phong Cách Markdown

- Tất cả URL phải bọc trong định dạng `[text](../../url)` không có khoảng trắng thừa
- Liên kết tương đối phải bắt đầu với `./` hoặc `../`
- Tất cả liên kết tới các miền Microsoft phải có ID theo dõi: `?WT.mc_id=academic-105485-koreyst`
- Không sử dụng địa phương hóa theo quốc gia trong URL (tránh `/en-us/`)
- Hình ảnh lưu trong thư mục `./images` với tên mô tả
- Sử dụng ký tự tiếng Anh, số và dấu gạch nối trong tên file

### Hỗ Trợ Dịch Thuật

- Kho lưu trữ hỗ trợ hơn 40 ngôn ngữ thông qua GitHub Actions tự động
- Bản dịch lưu trong thư mục `translations/`
- Không gửi bản dịch chưa hoàn chỉnh
- Không chấp nhận bản dịch máy
- Hình ảnh được dịch lưu trong thư mục `translated_images/`

## Kiểm Tra và Xác Thực

### Kiểm Tra Trước Khi Gửi

Kho lưu trữ này sử dụng GitHub Actions để validate. Trước khi gửi PR:

1. **Kiểm tra các liên kết Markdown**:
   ```bash
   # Quy trình validate-markdown.yml kiểm tra:
   # - Đường dẫn tương đối bị hỏng
   # - Thiếu ID theo dõi trên các đường dẫn
   # - Thiếu ID theo dõi trên các URL
   # - URL chứa vùng ngôn ngữ quốc gia
   # - URL bên ngoài bị hỏng
   ```

2. **Kiểm tra thủ công**:
   - Thử các ví dụ Python: Kích hoạt venv và chạy script
   - Thử các ví dụ TypeScript: `npm install`, `npm run build`, `npm start`
   - Xác nhận biến môi trường được cấu hình đúng
   - Kiểm tra khóa API hoạt động với ví dụ mã

3. **Ví dụ mã**:
   - Đảm bảo tất cả mã chạy không lỗi
   - Thử với cả Azure OpenAI và OpenAI API khi có thể
   - Xác nhận ví dụ hoạt động với Microsoft Foundry Models khi được hỗ trợ

### Không Có Kiểm Tra Tự Động

Đây là kho lưu trữ giáo dục tập trung vào hướng dẫn và ví dụ. Không có kiểm tra đơn vị hay kiểm tra tích hợp tự động. Xác thực chủ yếu gồm:
- Kiểm tra thủ công các ví dụ mã
- GitHub Actions để xác thực Markdown
- Đánh giá cộng đồng về nội dung giáo dục

## Hướng Dẫn Pull Request

### Trước Khi Gửi

1. Kiểm tra thay đổi mã trong cả Python và TypeScript khi có thể
2. Chạy xác thực Markdown (tự động khi gửi PR)
3. Đảm bảo tất cả URL Microsoft có ID theo dõi
4. Kiểm tra liên kết tương đối hợp lệ
5. Xác nhận hình ảnh được tham chiếu đúng

### Định Dạng Tiêu Đề PR

- Dùng tiêu đề mô tả: `[Lesson 06] Sửa lỗi gõ trong ví dụ Python` hoặc `Cập nhật README cho bài 08`
- Tham chiếu số issue nếu có: `Fixes #123`

### Mô Tả PR

- Giải thích thay đổi gì và tại sao
- Liên kết đến các issue liên quan
- Với thay đổi mã, chỉ rõ ví dụ đã được thử
- Với PR dịch thuật, bao gồm tất cả file cho bản dịch hoàn chỉnh

### Yêu Cầu Đóng Góp

- Ký Microsoft CLA (tự động khi PR đầu tiên)
- Fork kho lưu trữ vào tài khoản của bạn trước khi thay đổi
- Một PR cho một thay đổi logic (không gộp các sửa lỗi không liên quan)
- Giữ PR tập trung và nhỏ khi có thể

## Các Quy Trình Thông Dụng

### Thêm Ví Dụ Mã Mới

1. Điều hướng đến thư mục bài học tương ứng
2. Tạo ví dụ trong thư mục con `python/` hoặc `typescript/`
3. Tuân thủ quy ước đặt tên: `{provider}-{example-name}.{py|ts|js}`
4. Thử nghiệm với thông tin API thực tế
5. Ghi tài liệu các biến môi trường mới trong README bài học

### Cập Nhật Tài Liệu

1. Sửa README.md trong thư mục bài học
2. Tuân thủ hướng dẫn Markdown (ID theo dõi, liên kết tương đối)
3. Cập nhật dịch thuật được xử lý bởi GitHub Actions (không sửa tay)
4. Kiểm tra tất cả liên kết hợp lệ

### Làm Việc Với Dev Containers

1. Kho lưu trữ có file `.devcontainer/devcontainer.json`
2. Script post-create tự động cài phụ thuộc Python
3. Các tiện ích mở rộng cho Python và Jupyter được cấu hình sẵn
4. Môi trường dựa trên `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Triển Khai và Xuất Bản

Đây là kho lưu trữ học tập - không có quy trình triển khai. Chương trình được sử dụng qua:

1. **Kho Lưu Trữ GitHub**: Truy cập trực tiếp mã và tài liệu
2. **GitHub Codespaces**: Môi trường dev ngay lập tức với thiết lập sẵn
3. **Microsoft Learn**: Nội dung có thể được phân phối trên nền tảng học chính thức
4. **docsify**: Trang tài liệu được xây dựng từ Markdown (xem `docsifytopdf.js` và `package.json`)

### Xây Dựng Trang Tài Liệu

```bash
# Tạo PDF từ tài liệu (nếu cần)
npm run convert
```

## Khắc Phục Sự Cố

### Các Vấn Đề Thường Gặp

**Lỗi Import Python**:
- Đảm bảo kích hoạt môi trường ảo
- Chạy `pip install -r requirements.txt`
- Kiểm tra phiên bản Python >= 3.9

**Lỗi Biên Dịch TypeScript**:
- Chạy `npm install` trong thư mục ứng dụng tương ứng
- Kiểm tra phiên bản Node.js tương thích
- Xóa thư mục `node_modules` và cài lại nếu cần

**Lỗi Xác Thực API**:
- Xác nhận file `.env` tồn tại và có giá trị đúng
- Kiểm tra các khóa API hợp lệ và chưa hết hạn
- Đảm bảo URL endpoint đúng khu vực của bạn

**Thiếu Biến Môi Trường**:
- Sao chép `.env.copy` thành `.env`
- Điền đầy đủ các giá trị cần thiết cho bài học đang làm
- Khởi động lại ứng dụng sau khi cập nhật `.env`

## Tài Nguyên Bổ Sung

- [Hướng Dẫn Thiết Lập Khóa Học](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Hướng Dẫn Đóng Góp](./CONTRIBUTING.md)
- [Quy Tắc Ứng Xử](./CODE_OF_CONDUCT.md)
- [Chính Sách Bảo Mật](./SECURITY.md)
- [Discord Azure AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Bộ Sưu Tập Mẫu Mã Nâng Cao](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Ghi Chú Riêng Cho Dự Án

- Đây là kho lưu trữ **giáo dục** tập trung vào học tập, không phải mã sản xuất
- Các ví dụ được thiết kế đơn giản nhằm mục đích giảng dạy các khái niệm
- Chất lượng mã được cân bằng với tính rõ ràng giáo dục
- Mỗi bài học độc lập và có thể hoàn thành riêng lẻ
- Kho lưu trữ hỗ trợ nhiều nhà cung cấp API: Azure OpenAI, OpenAI, Microsoft Foundry Models, và các nhà cung cấp offline như Foundry Local và Ollama
- Nội dung đa ngôn ngữ với quy trình dịch tự động
- Cộng đồng hoạt động trên Discord để hỗ trợ và trả lời câu hỏi

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->