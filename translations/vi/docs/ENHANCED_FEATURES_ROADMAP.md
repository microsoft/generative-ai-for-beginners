# Lộ Trình Các Tính Năng và Cải Tiến Nâng Cao

Tài liệu này phác thảo các cải tiến và nâng cấp được đề xuất cho chương trình đào tạo Generative AI cho Người mới bắt đầu, dựa trên việc đánh giá mã nguồn toàn diện và phân tích các thực tiễn tốt nhất trong ngành.

## Tóm Tắt Điều Hành

Mã nguồn đã được phân tích về bảo mật, chất lượng mã và hiệu quả giáo dục. Tài liệu này cung cấp các khuyến nghị cho việc sửa lỗi ngay lập tức, các cải tiến trong ngắn hạn và các nâng cấp trong tương lai.

---

## 1. Các Cải Tiến về Bảo Mật (Ưu Tiên: Quan Trọng)

### 1.1 Sửa Lỗi Ngay Lập Tức (Đã Hoàn Thành)

| Vấn đề | Các Tệp Liên Quan | Trạng thái |
|-------|------------------|-----------|
| SECRET_KEY được mã hóa cứng | `05-advanced-prompts/python/aoai-solution.py` | Đã sửa |
| Thiếu xác thực biến môi trường | Nhiều tệp JS/TS | Đã sửa |
| Các cuộc gọi hàm không an toàn | `11-integrating-with-function-calling/js-githubmodels/app.js` | Đã sửa |
| Rò rỉ handle tệp | `08-building-search-applications/scripts/` | Đã sửa |
| Thiếu timeout cho request | `09-building-image-applications/python/` | Đã sửa |

### 1.2 Các Tính Năng Bảo Mật Bổ Sung Được Đề Xuất

1. **Ví dụ về Giới hạn tỷ lệ**
   - Thêm mã ví dụ cho cách triển khai giới hạn tỷ lệ cho các cuộc gọi API
   - Minh họa các mẫu lùi lại theo cấp số nhân

2. **Xoay vòng khóa API**
   - Thêm tài liệu về các thực tiễn tốt nhất cho xoay vòng khóa API
   - Bao gồm ví dụ sử dụng Azure Key Vault hoặc các dịch vụ tương tự

3. **Tích hợp An toàn Nội dung**
   - Thêm ví dụ sử dụng Azure Content Safety API
   - Minh họa các mẫu điều tiết đầu vào/đầu ra

---

## 2. Cải Tiến Chất Lượng Mã

### 2.1 Đã Thêm Tệp Cấu Hình

| Tệp | Mục đích |
|-----|-----------|
| `.eslintrc.json` | Quy tắc lint cho JavaScript/TypeScript |
| `.prettierrc` | Tiêu chuẩn định dạng mã |
| `pyproject.toml` | Cấu hình công cụ Python (Black, Ruff, mypy) |

### 2.2 Đã Tạo Tiện Ích Chung

Mô-đun `shared/python/` mới với:
- `env_utils.py` - Xử lý biến môi trường
- `input_validation.py` - Kiểm tra và làm sạch đầu vào
- `api_utils.py` - Vỏ bọc cuộc gọi API an toàn

### 2.3 Các Cải Tiến Mã Được Đề Xuất

1. **Phủ sóng Gợi ý kiểu**
   - Thêm gợi ý kiểu cho tất cả các tệp Python
   - Kích hoạt chế độ nghiêm ngặt TypeScript trong tất cả dự án TS

2. **Tiêu chuẩn Tài liệu**
   - Thêm docstrings cho tất cả các hàm Python
   - Thêm bình luận JSDoc cho tất cả hàm JavaScript/TypeScript

3. **Khung Kiểm thử**
   - Thêm cấu hình pytest và ví dụ kiểm thử _(đã làm: cấu hình pytest trong `pyproject.toml`; ví dụ kiểm thử cho tiện ích chia sẻ trong [`tests/`](../../../tests) chạy trong CI)_
   - Thêm cấu hình Jest cho JavaScript/TypeScript

---

## 3. Nâng cao Giáo dục

### 3.1 Chủ đề Bài học Mới

1. **Bảo mật trong Ứng dụng AI** (Bài học đề xuất 22)
   - Tấn công tiêm lệnh prompt và phòng thủ
   - Quản lý khóa API
   - Điều tiết nội dung
   - Giới hạn tỷ lệ và ngăn ngừa lạm dụng

2. **Triển khai Sản xuất** (Bài học đề xuất 23)
   - Đóng gói container với Docker
   - Các pipeline CI/CD
   - Giám sát và ghi nhật ký
   - Quản lý chi phí

3. **Kỹ thuật RAG Nâng cao** (Bài học đề xuất 24)
   - Tìm kiếm kết hợp (từ khóa + ngữ nghĩa)
   - Chiến lược xếp hạng lại
   - RAG đa phương thức
   - Các chỉ số đánh giá

### 3.2 Cải Tiến Bài học Hiện có

| Bài học | Cải tiến Được Đề xuất |
|--------|----------------------|
| 06 - Tạo Văn Bản | Thêm ví dụ phản hồi theo luồng |
| 07 - Ứng dụng Chat | Thêm mẫu lưu nhớ hội thoại |
| 08 - Ứng dụng Tìm kiếm | Thêm so sánh cơ sở dữ liệu vector |
| 09 - Tạo Ảnh | Thêm ví dụ chỉnh sửa/biến thể ảnh |
| 11 - Gọi Hàm | Thêm gọi hàm song song |
| 15 - RAG | Thêm so sánh chiến lược chia đoạn |
| 17 - Tác nhân AI | Thêm điều phối đa tác nhân |

---

## 4. Hiện đại hóa API

### 4.1 Các Mẫu API Ngừng Hỗ Trợ (Đã Di chuyển)

Tất cả mẫu chat Python và TypeScript đã được di chuyển từ Chat Completions API sang **Responses API** (`client.responses.create(...)` → `response.output_text`).

| Mẫu Cũ | Mẫu Mới | Trạng thái |
|---------|---------|-----------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (chat) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | Đã hoàn thành |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | Đã hoàn thành |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | gói `openai` `client.responses.create()` → `response.output_text` | Đã hoàn thành |
| `df.append()` (pandas) | `pd.concat()` | Đã hoàn thành |

> **Lưu ý:** Các mẫu Microsoft Foundry Models sử dụng SDK `azure-ai-inference` / `@azure-rest/ai-inference` (`client.complete()`) vẫn dùng Model Inference API, không hỗ trợ Responses API. `AzureOpenAI()` được giữ lại có chủ ý với các trường hợp còn hợp lệ (nhúng và tạo hình ảnh).

### 4.2 Các Tính Năng API Mới Để Minh Họa

1. **Đầu ra Cấu trúc** (OpenAI)
   - Chế độ JSON
   - Gọi hàm với các schema nghiêm ngặt

2. **Khả năng Thị giác**
   - Phân tích hình ảnh bằng GPT-4o (vision)
   - Prompt đa phương thức

3. **Công cụ tích hợp Responses API** (thay thế API Assistants cũ)
   - Phiên dịch mã
   - Tìm kiếm tệp
   - Tìm kiếm web và công cụ tùy chỉnh

---

## 5. Cải Tiến Hạ Tầng

### 5.1 Nâng cao CI/CD

Đã triển khai trong [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): linting/định dạng Python (Ruff + Black) được **áp dụng bắt buộc** trên mô-đun tiện ích `shared/` bảo trì và chạy **khuyên dùng** trên phần còn lại của khóa học, cùng với một chạy ESLint khuyên dùng cho JavaScript/TypeScript. Mức cơ bản minh họa là:

```yaml
# .github/workflows/code-quality.yml
name: Code Quality

on: [push, pull_request]

jobs:
  python-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - run: pip install ruff black mypy
      - run: ruff check .
      - run: black --check .

  js-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npx eslint .
```

### 5.2 Quét Bảo Mật

Đã triển khai trong [`.github/workflows/security.yml`](../../../.github/workflows/security.yml): phân tích CodeQL cho Python và JavaScript/TypeScript (khi push, pull request và theo lịch hàng tuần) cộng với đánh giá phụ thuộc trên pull request. Mức cơ bản minh họa là:

```yaml
# .github/workflows/security.yml
name: Security Scan

on: [push, pull_request]

jobs:
  codeql:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: javascript, python
      - uses: github/codeql-action/analyze@v3

  dependency-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/dependency-review-action@v4
```

---

## 6. Cải Thiện Trải Nghiệm Nhà Phát Triển

### 6.1 Nâng cấp DevContainer

Đã triển khai trong [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) và [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): container hiện tích hợp Pylance, trình định dạng Black, Ruff, ESLint, Prettier và các tiện ích mở rộng Copilot, kích hoạt tự động định dạng khi lưu liên kết với cấu hình Black/Prettier của repo, và cài đặt công cụ phát triển (`ruff`, `black`, `mypy`, `pytest`) để [luồng công việc đánh giá chất lượng mã](../../../.github/workflows/code-quality.yml) có thể tái tạo tại địa phương. Hình ảnh cơ sở `mcr.microsoft.com/devcontainers/universal` đã bao gồm Python và Node, nên không cần thêm tính năng nào. Mức cơ bản minh họa là:

```json
{
  "name": "Generative AI for Beginners",
  "image": "mcr.microsoft.com/devcontainers/universal:2",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.11"
    },
    "ghcr.io/devcontainers/features/node:1": {
      "version": "20"
    }
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-toolsai.jupyter",
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "github.copilot"
      ],
      "settings": {
        "python.formatting.provider": "black",
        "editor.formatOnSave": true
      }
    }
  },
  "postCreateCommand": "pip install -e .[dev] && npm install"
}
```

### 6.2 Khu vực Thử nghiệm Tương tác

Xem xét thêm:
- Các notebook Jupyter với khóa API được điền sẵn (thông qua biến môi trường)
- Demo Gradio/Streamlit cho người học hình ảnh
- Bộ câu hỏi tương tác để đánh giá kiến thức

---

## 7. Hỗ Trợ Đa Ngôn Ngữ

### 7.1 Phạm vi Ngôn ngữ Hiện tại

| Công nghệ | Các Bài học Bao phủ | Trạng thái |
|----------|--------------------|----------|
| Python | Tất cả | Hoàn thành |
| TypeScript | 06-09, 11 | Một phần |
| JavaScript | 06-08, 11 | Một phần |
| .NET/C# | Một số | Một phần |

### 7.2 Các bổ sung Được Đề xuất

1. **Go** - Đang phát triển trong công cụ AI/ML
2. **Rust** - Ứng dụng yêu cầu hiệu năng cao
3. **Java/Kotlin** - Ứng dụng doanh nghiệp

---

## 8. Tối Ưu Hiệu Suất

### 8.1 Tối ưu ở cấp độ Mã

1. **Mẫu Async/Await**
   - Thêm ví dụ bất đồng bộ cho xử lý theo lô
   - Minh họa các cuộc gọi API đồng thời

2. **Chiến lược Bộ nhớ đệm**
   - Thêm ví dụ bộ nhớ đệm nhúng
   - Minh họa các mẫu bộ nhớ đệm phản hồi

3. **Tối ưu Token**
   - Thêm ví dụ sử dụng tiktoken
   - Minh họa kỹ thuật nén prompt

### 8.2 Ví dụ Tối ưu Chi phí

Thêm ví dụ minh họa:
- Lựa chọn mô hình dựa trên độ phức tạp công việc
- Kỹ thuật thiết kế prompt cho hiệu quả token
- Xử lý theo lô cho các thao tác lớn

---

## 9. Truy cập và Quốc tế hóa

### 9.1 Trạng thái Dịch thuật Hiện tại

Tất cả bản dịch đều **hoàn thành** và được tạo tự động bởi [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst), công cụ duy trì trên 50 ngôn ngữ của chương trình đào tạo đồng bộ với bản gốc tiếng Anh. Nội dung dịch được lưu dưới thư mục `translations/` và hình ảnh bản địa hóa dưới `translated_images/`; danh sách đầy đủ các ngôn ngữ có sẵn được đăng ở đầu README của kho.

| Khía cạnh | Trạng thái |
|----------|----------|
| Phủ sóng Dịch thuật | Hoàn thành — 50+ ngôn ngữ, toàn bộ bài học |
| Phương pháp Dịch thuật | Tự động qua [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) |
| Đồng bộ với bản tiếng Anh | Có — tự động tái tạo |

### 9.2 Các Cải Tiến Truy cập

1. Thêm văn bản thay thế cho tất cả hình ảnh
2. Đảm bảo các mẫu code có tô sáng cú pháp chính xác
3. Thêm bản ghi chú cho tất cả nội dung video
4. Đảm bảo độ tương phản màu sắc theo tiêu chuẩn WCAG

---

## 10. Ưu tiên Triển khai

### Giai đoạn 1: Ngay lập tức (Tuần 1-2)
- [x] Sửa các vấn đề bảo mật nghiêm trọng
- [x] Thêm cấu hình chất lượng mã
- [x] Tạo tiện ích dùng chung
- [x] Tài liệu hướng dẫn bảo mật

### Giai đoạn 2: Ngắn hạn (Tuần 3-4)
- [x] Cập nhật các mẫu API ngừng hỗ trợ (Chat Completions → Responses API, Python + TypeScript)
- [ ] Thêm gợi ý kiểu cho tất cả các tệp Python (đã làm cho mô-đun `shared/`; ví dụ bài học giữ đơn giản)
- [x] Thêm luồng công việc CI/CD cho chất lượng mã
- [x] Tạo luồng quét bảo mật

### Giai đoạn 3: Trung hạn (Tháng 2-3)
- [ ] Thêm bài học bảo mật mới
- [ ] Thêm bài học triển khai sản xuất
- [x] Cải thiện cấu hình DevContainer
- [ ] Thêm demo tương tác

### Giai đoạn 4: Dài hạn (Tháng 4+)
- [ ] Thêm bài học RAG nâng cao
- [ ] Mở rộng phạm vi ngôn ngữ
- [ ] Thêm bộ kiểm thử toàn diện
- [ ] Tạo chương trình chứng nhận

---

## Kết luận

Lộ trình này cung cấp một phương pháp có cấu trúc để cải thiện chương trình đào tạo Generative AI cho Người mới bắt đầu. Bằng cách giải quyết các mối quan tâm về bảo mật, hiện đại hóa API và thêm nội dung giáo dục, khóa học sẽ chuẩn bị tốt hơn cho học viên phát triển ứng dụng AI trong thực tế.

Nếu có câu hỏi hoặc đóng góp, vui lòng mở một issue trên kho GitHub.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->