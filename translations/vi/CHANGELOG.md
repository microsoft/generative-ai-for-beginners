# Nhật ký thay đổi

Tất cả các thay đổi đáng chú ý cho chương trình đào tạo Generative AI cho Người mới bắt đầu đều được ghi lại trong tệp này.

Định dạng dựa trên [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Bởi vì đây là một
chương trình học thay vì một gói phần mềm có phiên bản, các phần được nhóm theo ngày.

## [2026-07-16] — Xác thực nội dung + Tài sản hình ảnh Bài học 09

### Đã thay đổi

- **Bài học 10 (ứng dụng AI low-code):** cập nhật hai liên kết `docs.microsoft.com/powerapps/...` Dataverse đã nghỉ hưu
  thành `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro` hiện tại
  (đã xác thực còn hoạt động).
- **Bài học 17 (đại lý AI):** hiện đại hóa một ví dụ mô hình lỗi thời (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) và một tên triển khai giữ chỗ trong mẫu Khung Đại lý
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Gốc `README.md`:** thêm ID theo dõi `?WT.mc_id=academic-105485-koreyst` bị thiếu vào
  liên kết *Microsoft for Startups*.
- **Tài sản hình ảnh Bài học 09** được tạo lại với mô hình `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, và
  `images/startup.png` (cặp hình ảnh trước/sau của ví dụ chỉnh sửa được sản xuất qua cuộc gọi thực tế
  `client.images.edit` với mặt nạ được tạo).

### Đã xác thực

- Đã kiểm tra các README của các bài học 01, 03, 05, 12, 14 và 16 — tất cả đều hiện tại (tên và liên kết Microsoft Foundry chính xác);
  không cần thay đổi.
- Đã chạy kiểm tra hợp lệ markdown toàn diện trên tất cả 41 tập tin markdown trong kho (không bao gồm bản dịch) để
  các đường dẫn tài liệu đã lỗi thời, `/en-us/` địa phương hóa Microsoft, tên sản phẩm/mẫu cũ, thiếu ID theo dõi,
  và các liên kết/hình ảnh tương đối bị hỏng. Chỉ có duy nhất khoảng trống ID theo dõi *Microsoft for Startups* là
  có thể xử lý; tất cả các cảnh báo khác đều được xác nhận là dương tính giả (liên kết dịch tự động tạo,
  các chỗ giữ chỗ bị ghi chú, và URL cấu trúc bên thứ ba `/en/`).

## [2026-07-15] — Bài học 09 (Ứng dụng hình ảnh) Viết lại cho các Mô hình Hình ảnh GPT

### Đã thay đổi

- **Viết lại bài học 09 "Xây dựng Ứng dụng tạo Hình ảnh"** xoay quanh **`gpt-image`** hiện tại
  gia đình mô hình (mặc định **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` cũng là GA), thay thế cho
  nội dung DALL·E 2/3 cũ. Các sửa chữa chính:
  - các mô hình `gpt-image` trả về hình ảnh dưới dạng **base64 (`b64_json`)**, không phải URL. Cập nhật tất cả các mẫu để
    sử dụng `base64.b64decode(...)` thay vì tải xuống một `url` với `requests`.
  - Nâng cấp phiên bản API hình ảnh lên `2025-04-01-preview`.
  - Thay thế phần "nhiệt độ" giả tạo (mô hình hình ảnh không nhận `temperature`) và phần
    các **biến thể** hình ảnh chỉ dành cho DALL·E-2 bằng phần **chỉnh sửa hình ảnh** (mask/inpainting).
  - Cập nhật `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, cả
    các sổ tay bài tập (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), và sổ tay .NET `.dib`.

### Đã loại bỏ

- Xóa các mẫu `python/aoai-app-variation.py` và `python/oai-app-variation.py` lỗi thời
  (`images.create_variation` chỉ dành cho DALL·E-2 và không được hỗ trợ bởi `gpt-image`).
- Xóa 4 tài sản hình ảnh bỏ rơi liên quan đến phần so sánh nhiệt độ đã xóa
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Bỏ phụ thuộc `requests` không cần thiết khỏi các mẫu Python và yêu cầu của bài học.

### Đã xác thực

- Chạy `aoai-app.py` toàn bộ với mô hình `gpt-image-1.5` đã triển khai và xác nhận luồng giải mã/lưu base64
  tạo ra PNG. Các sổ tay được xác nhận hợp lệ JSON.

## [2026-07-14] — Cập nhật Mô hình Mặc định + Hướng dẫn Mô hình Lập luận

### Đã thay đổi

- **Mô hình chat mặc định `gpt-4o-mini` → `gpt-5-mini`** trong tất cả các mẫu chạy thử, tài liệu, và cấu hình của chương trình.
  Điều này được thúc đẩy bởi trạng thái vòng đời mô hình: trên Microsoft Foundry,
  `gpt-4o-mini` (nghỉ hưu 2026-10-01) và toàn bộ gia đình `gpt-4.1` (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, nghỉ hưu 2026-10-14) đang **Ngừng sử dụng**, trong khi gia đình **GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) hiện Được Phát Hành Công Khai** (nghỉ hưu 2027-02-06). Cập nhật:
  - `.env.copy`, `00-course-setup/03-providers.md` (lệnh triển khai khuyến nghị và `az cognitiveservices`
    triển khai), và các README cho các bài học 04, 06, 07, và 15.
  - Mẫu Python trong bài học 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) và tập lệnh bài học 08.
  - Mẫu TypeScript / JavaScript trong các bài học 06, 07, và 11, và sổ tay .NET `.dib` cho
    các bài học 06 và 07.
  - Sổ tay bài tập trong các bài học 04, 06, 07, và 11 (ô mã), cộng với ví dụ docstring `shared/python/api_utils.py`.
- **Hướng dẫn tham số mô hình lập luận (mới).** `gpt-5-mini` là một mô hình *lập luận*: nó **không**
  hỗ trợ `temperature`/`top_p`, và sử dụng `max_completion_tokens` (chat completions) /
  `max_output_tokens` (Responses API) thay cho `max_tokens`. Theo đó:
  - Loại bỏ `temperature`/`top_p`/`max_tokens` khỏi các mẫu hiện mặc định sử dụng `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, README bài học 15 RAG).
  - Thêm chú thích **"Mô hình lập luận không dùng `temperature`"** vào bài học 06, giải thích rằng
    các mô hình lập luận được điều khiển bằng **kỹ thuật prompt + kiểm soát lập luận** thay vì
    các núm sampling, trong khi `temperature`/`top_p` vẫn hợp lệ với các mô hình không lập luận
    (GPT-4.x, Mistral, Llama, Phi, mô hình mở).
- **`gpt-5-mini` không được dùng cho hướng dẫn fine-tuning (bài học 18).** GPT-5 chỉ hỗ trợ
  fine-tuning tăng cường (RFT); hướng dẫn fine-tuning có giám sát (SFT) của bài học 18 vẫn sử dụng
  `gpt-4.1-mini`, hỗ trợ SFT/DPO.
- **Các demo nhiệt độ dùng mô hình Llama.** Để tiếp tục dạy `temperature` (bị các mô hình lập luận
  từ chối), một mô hình `Llama-3.3-70B-Instruct` được dùng qua endpoint Foundry Models. Thêm biến mới
  `AZURE_INFERENCE_CHAT_MODEL` vào `.env.copy`; các sổ tay `githubmodels` của bài 04/06 và mẫu `06` `js-githubmodels`
  đọc biến này (sẽ dùng `Llama-3.3-70B-Instruct` nếu không có) và giữ các demo của chúng `temperature`/`top_p`/`max_tokens`.
- **Mẫu JS / .NET cập nhật cho GPT-5.** Bỏ `temperature`/`top_p`/`max_tokens` khỏi mẫu GPT-5
  (`06` `recipe-app` TypeScript, `06` `.dib` .NET - cũng sửa lỗi `MaxOutputTokenCount`
  để kết quả lập luận không bị cắt bớt). Mẫu `06` `js-githubmodels` hiện dùng Llama để giữ demo nhiệt độ của nó.
  Mẫu `.dib` nói rằng dùng `Azure.AI.Inference` + một mô hình Llama là cách để
  trình diễn `Temperature` trong .NET.
- Giữ nguyên `gpt-4o-mini` / `gpt-5-mini` ở những nơi chúng vẫn chính xác: tài liệu mã hóa token `tiktoken`,
  danh sách tính khả dụng của catalog mô hình, và mô hình giọng nói bài 02 (`gpt-4o-transcribe`).
- Các mẫu bài học 20 (Mistral) và 21 (Meta) giữ lại `temperature`/`max_tokens` vì chúng hướng đến
  các mô hình Mistral/Llama, hỗ trợ các tham số đó.

## [2026-07-06] — Làm mới Nâng cao Nội dung

Một làm mới tổng thể để giữ cho chương trình học chính xác cho năm 2026: API hiện đại, tên sản phẩm hiện tại và


### Đã thêm

- Mục **Microsoft Agent Framework** trong bài học `17-ai-agents`, bao gồm các agent chat đơn,

  (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** được mô tả như nhà cung cấp offline / trên thiết bị (cùng với Ollama) trong
  `00-course-setup/03-providers.md` và bài học `19-slm`.
- **Quy trình tích hợp liên tục**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (bắt buộc với module `shared/` duy trì,
    khuyến cáo trong phần còn lại của chương trình), chạy ESLint kiểm tra, và công việc pytest.
  - `.github/workflows/security.yml` — Phân tích CodeQL (Python + JavaScript/TypeScript) và
    đánh giá phụ thuộc trên các pull request.
- **Bộ kiểm thử** dưới `tests/` — 41 bài kiểm thử pytest bao phủ module tiện ích chung.
- **Kỹ năng di trú Azure OpenAI → Responses API** dưới
  `.github/skills/azure-openai-to-responses/` dùng để hướng dẫn di trú API.

### Đã thay đổi

- **Chat Completions API → Responses API** trên tất cả mẫu chat Python và TypeScript

- **API Hoàn Thành Chat → API Phản Hồi** trên tất cả các mẫu chat Python và TypeScript
  (`client.responses.create(...)` → `response.output_text`), bao gồm các bài học 04, 06, 07, 11,
  15 và 18, cùng với các README của chúng.
- **GitHub Models → Microsoft Foundry Models** trong toàn bộ văn bản, liên kết, và ví dụ. GitHub Models
  sẽ nghỉ hưu vào cuối tháng 7 năm 2026; các ví dụ hiện trỏ đến danh mục mô hình Microsoft Foundry và sử dụng
  các biến môi trường `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md`, và tài liệu nhà cung cấp** được cập nhật để phản ánh rằng Azure OpenAI hiện là một phần
  của Microsoft Foundry, và phiên bản API mặc định được nâng lên `2024-10-21`.
- **Ví dụ TypeScript** (bài học 06, 07, 08, 11) được chuyển từ SDK `@azure/openai` beta đã lỗi thời
  sang gói `openai` (ứng dụng chat sử dụng API Responses; ứng dụng tìm kiếm sử dụng
  client embeddings).
- **Sổ tay .NET** (`dotnet/*.dib`) tiêu chuẩn hóa trên `Azure.AI.OpenAI` **2.1.0**: bài học 06 và 07
  sử dụng API `ChatClient`, bài học 08 sử dụng `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), và
  bài học 09 sử dụng `ImageClient` (`GenerateImage`) với `gpt-image-1`, thay thế cho
  `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` cũ từ `1.0.0-beta.9`.
- **Hiện đại hóa tên sản phẩm**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (bài học 14, 16, 17) và "Bing" → **Microsoft Copilot** (bài học 12), nơi những tên này đề cập đến
  các sản phẩm hiện tại.
- **DevContainer** (`.devcontainer/`) hiện bao gồm các tiện ích mở rộng Pylance, Black, Ruff, ESLint, Prettier và Copilot,
  kích hoạt định dạng khi lưu, và cài đặt `ruff`, `black`, `mypy`, và `pytest` để
  có thể tái tạo các kiểm tra CI trên máy cục bộ.
- **Tạo ảnh** (bài học 09) đề xuất `gpt-image-1` cho Azure (danh mục Azure đã loại bỏ
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** đã được cập nhật để phản ánh công việc đã hoàn thành (di chuyển API, CI,
  DevContainer, kiểm thử) và các sự kiện hiện tại (bản dịch được tự động tạo bởi
  Azure Co-op Translator; API Assistants đã được thay thế bởi API Responses).

### Đã sửa

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` giờ trả về
  chuỗi rỗng cho dữ liệu đầu vào chỉ chứa khoảng trắng thay vì phát sinh lỗi "quá ngắn" (như trong
  trường hợp `None`). Đã phát hiện và được bao phủ bởi bộ kiểm thử mới.
- **Hình mẫu bài học 09** — sửa lỗi thực tế: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  và một biến đã che khuất module `openai`.
- **Sổ tay RAG bài học 15** — sửa thiết lập client, thay thế `DataFrame.append` đã bị loại bỏ
  bằng `pd.concat`, và hiện đại hóa việc sử dụng SDK cũ.
- Tên mô hình ngưng hỗ trợ / đã nghỉ hưu (`gpt-3.5-turbo`, `gpt-35-turbo`) được thay thế bằng `gpt-4o-mini`
  trong các mẫu đang dùng; kết quả tinh chỉnh nâng cao lịch sử trong bài học 18 được giữ nguyên và chú thích
  chứ không viết lại.

### Ngưng hỗ trợ / Ghi chú

- **Mẫu Microsoft Foundry Models** sử dụng SDK `azure-ai-inference` / `@azure-rest/ai-inference`
  (`client.complete()`) — các mẫu `githubmodels-*` và `js-githubmodels` và bài học 19, 20,
  và 21 — vẫn còn dùng Model Inference API, vốn **không** hỗ trợ Responses API. Những mẫu này
  được giữ nguyên trên SDK đó theo ý định.
- `AzureOpenAI()` được giữ nguyên nếu còn thích hợp (nhúng và tạo hình ảnh),
  vì các luồng công việc đó không thuộc di chuyển sang Responses API.
- Các tham chiếu `text-embedding-ada-002` được giữ lại khi một chỉ mục nhúng tính trước phụ thuộc vào chúng.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->