# Nhật ký thay đổi

Mọi thay đổi đáng chú ý đối với chương trình đào tạo Generative AI cho Người mới bắt đầu đều được ghi lại trong tệp này.

Định dạng dựa trên [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Vì đây là một chương trình đào tạo thay vì một phần mềm có phiên bản, các mục được nhóm theo ngày.


## [2026-07-16] — Xác thực nội dung + Tài sản hình ảnh Bài học 09

### Đã thay đổi

- **Bài học 10 (ứng dụng AI low-code):** cập nhật hai liên kết `docs.microsoft.com/powerapps/...` Dataverse đã ngừng hoạt động
  với `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro` hiện tại
  (đã kiểm tra trực tiếp).
- **Bài học 17 (đại lý AI):** hiện đại hóa một ví dụ mô hình cũ (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) và một tên triển khai giữ chỗ trong mẫu Agent Framework
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`).
- **Root `README.md`:** thêm ID theo dõi `?WT.mc_id=academic-105485-koreyst` còn thiếu vào
  liên kết *Microsoft for Startups*.
- **Tài nguyên hình ảnh bài học 09** được tạo lại bằng mô hình `gpt-image`: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png`, và
  `images/startup.png` (cặp trước/sau của ví dụ chỉnh sửa được tạo ra qua một trường hợp thực tế
  `client.images.edit` gọi với một mặt nạ được tạo ra).

### Đã được xác thực

- Đã kiểm tra các README cho bài học 01, 03, 05, 12, 14 và 16 — tất cả đều hợp lệ (đúng tên và liên kết Microsoft Foundry hiện tại);
  không cần thay đổi.
- Đã chạy kiểm tra hợp lệ markdown đầy đủ trên tất cả 41 tệp markdown trong kho (không bao gồm bản dịch)
  để tìm đường dẫn tài liệu lỗi thời, `/en-us/` các địa điểm Microsoft, tên sản phẩm/mô hình lỗi thời, thiếu ID theo dõi,
  và liên kết/hình ảnh tương đối hỏng. Chỉ có một khoảng trống ID theo dõi *Microsoft for Startups* là
  có thể hành động được; tất cả các tín hiệu khác được xác nhận là dương tính giả (liên kết bản dịch tự động tạo,
  chỗ giữ chỗ bị chú thích, và URL cấu trúc của bên thứ ba `/en/`).

## [2026-07-15] — Viết lại Bài học 09 (Ứng dụng Hình ảnh) cho Mô hình Hình ảnh GPT

### Đã thay đổi

- **Viết lại bài học 09 "Xây dựng Ứng dụng Tạo ảnh"** xoay quanh hiện tại **`gpt-image`**
  họ mô hình (mặc định **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` cũng GA), thay thế cho
  nội dung DALL·E 2/3 cũ. Các sửa lỗi chính:
  - các mô hình `gpt-image` trả về hình ảnh dưới dạng **base64 (`b64_json`)**, không phải URL. Cập nhật tất cả mẫu sang
    `base64.b64decode(...)` thay vì tải xuống một `url` với `requests`.
  - Nâng cấp phiên bản API hình ảnh lên `2025-04-01-preview`.
  - Thay thế phần "nhiệt độ" giả định (mô hình hình ảnh không lấy `temperature`) và nội dung
    các **biến thể** hình ảnh chỉ của DALL·E-2 bằng phần **chỉnh sửa hình ảnh** (mask/inpainting).
  - Cập nhật `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py`, cả hai
    sổ tay giao bài (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`), và sổ tay .NET `.dib`.

### Đã xóa

- Đã xóa các ví dụ `python/aoai-app-variation.py` và `python/oai-app-variation.py` không còn sử dụng
  (`images.create_variation` chỉ dành cho DALL·E-2 và không được `gpt-image` hỗ trợ).
- Đã xóa 4 ảnh rời rạc liên quan đến phần so sánh nhiệt độ đã bị xóa
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Đã bỏ phụ thuộc `requests` không cần thiết từ các ví dụ Python và yêu cầu của bài học.

### Đã xác nhận

- Đã chạy `aoai-app.py` hoàn chỉnh với mô hình `gpt-image-1.5` đã triển khai và xác nhận luồng giải mã/lưu base64 tạo ra PNG. Các notebook được xác nhận là JSON hợp lệ.


## [2026-07-14] — Cập nhật Mô hình Mặc định + Hướng dẫn Mô hình Lý luận

### Thay đổi

- **Mô hình chat mặc định `gpt-4o-mini` → `gpt-5-mini`** trên tất cả các ví dụ chạy được trong chương trình học,
  tài liệu và cấu hình. Điều này do trạng thái vòng đời mô hình quyết định: trên Microsoft Foundry,
  `gpt-4o-mini` (nghỉ hưu 2026-10-01) và toàn bộ gia đình `gpt-4.1` (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, nghỉ hưu 2026-10-14) đang **Ngưng sử dụng**, trong khi **gia đình GPT-5
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) là Phiên bản Đang Có Sẵn** (nghỉ hưu 2027-02-06). Cập nhật:
  - `.env.copy`, `00-course-setup/03-providers.md` (lệnh triển khai được khuyến nghị và `az cognitiveservices`
    lệnh deploy), và các tệp README cho các bài học 04, 06, 07, và 15.
  - Ví dụ Python trong bài học 06 (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) và các script trong bài học 08.
  - Ví dụ TypeScript / JavaScript trong các bài học 06, 07, và 11, và sổ tay `.dib` .NET cho
    bài học 06 và 07.
  - Sổ tay bài tập trong các bài 04, 06, 07 và 11 (ô mã), cộng với `shared/python/api_utils.py`
    ví dụ docstring.
- **Hướng dẫn tham số mô hình suy luận (mới).** `gpt-5-mini` là một mô hình *suy luận*: nó **không**
  hỗ trợ `temperature`/`top_p`, và sử dụng `max_completion_tokens` (hoàn thành trò chuyện) /
  `max_output_tokens` (Responses API) thay cho `max_tokens`. Do đó:
  - Đã loại bỏ `temperature`/`top_p`/`max_tokens` khỏi các mẫu bây giờ mặc định là `gpt-5-mini`
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, README RAG bài 15).
  - Thêm ghi chú **"Mô hình suy luận không sử dụng `temperature`"** vào bài học 06, giải thích rằng
    các mô hình suy luận được điều khiển bằng **kỹ thuật prompt + kiểm soát suy luận** thay vì
    các núm sampling, trong khi `temperature`/`top_p` vẫn hợp lệ trên các mô hình không phải suy luận
    (GPT-4.x, Mistral, Llama, Phi, các mô hình mở).
- **`gpt-5-mini` không được sử dụng cho bài hướng dẫn fine-tuning (bài học 18).** GPT-5 chỉ hỗ trợ
  fine-tuning tăng cường (RFT); bài học 18 hướng dẫn fine-tuning có giám sát (SFT) vẫn giữ
  `gpt-4.1-mini`, hỗ trợ SFT/DPO.
- **Các demo Nhiệt độ sử dụng mô hình Llama.** Để tiếp tục dạy `temperature` (mà các mô hình suy luận
  từ chối), một mô hình `Llama-3.3-70B-Instruct` được sử dụng qua endpoint Foundry Models. Thêm biến mới
  `AZURE_INFERENCE_CHAT_MODEL` vào `.env.copy`; các notebook `githubmodels` bài học 04/06 và
  mẫu `06` `js-githubmodels` đọc biến này (dùng phương án dự phòng `Llama-3.3-70B-Instruct`) và giữ các demo
  `temperature`/`top_p`/`max_tokens` của họ.
- **Mẫu JS / .NET cập nhật cho GPT-5.** Đã loại bỏ `temperature`/`top_p`/`max_tokens` trong GPT-5
  các ví dụ (`06` `recipe-app` TypeScript, `06` `.dib` .NET - cũng làm tăng `MaxOutputTokenCount`
  nên đầu ra suy luận không bị cắt ngắn). Ví dụ `06` `js-githubmodels` giờ đây sử dụng Llama để giữ
  bản demo nhiệt độ. `.dib` lưu ý rằng `Azure.AI.Inference` + một mô hình Llama là cách để
  trình diễn `Temperature` trong .NET.
- Giữ nguyên `gpt-4o-mini` / `gpt-5-mini` tại chỗ để chúng vẫn chính xác: `tiktoken` tham chiếu mã hóa token,
  danh sách có sẵn mô hình trong danh mục, và mô hình phát âm bài 02 (`gpt-4o-transcribe`).
- Các ví dụ bài 20 (Mistral) và 21 (Meta) giữ `temperature`/`max_tokens` vì chúng hướng tới
  mô hình Mistral/Llama, những mô hình hỗ trợ các tham số đó.

## [2026-07-06] — Cập nhật hiện đại hóa nội dung

Làm mới tổng thể để giữ chương trình học chính xác cho năm 2026: API hiện đại, tên sản phẩm và
tên mô hình hiện tại, hướng dẫn cập nhật cho nhà cung cấp, và công cụ trải nghiệm nhà phát triển mới.

### Đã thêm

- Phần **Microsoft Agent Framework** trong bài học `17-ai-agents` bao gồm các đại lý trò chuyện đơn,
  gọi hàm công cụ, cấu hình Azure OpenAI (Microsoft Foundry), và đa tác nhân
  điều phối workflow (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local** được ghi chép là nhà cung cấp ngoại tuyến / trên thiết bị (cùng với Ollama) trong
  `00-course-setup/03-providers.md` và bài học `19-slm`.
- **Workflow tích hợp liên tục**:
  - `.github/workflows/code-quality.yml` — Ruff + Black (thực thi trên module `shared/` được duy trì,
    tư vấn trên phần còn lại của chương trình), một lượt kiểm tra ESLint tư vấn, và một công việc pytest.
  - `.github/workflows/security.yml` — Phân tích CodeQL (Python + JavaScript/TypeScript) và
    xem xét phụ thuộc trên các pull request.
- **Bộ kiểm thử** dưới `tests/` — 41 bài kiểm thử pytest bao phủ module tiện ích dùng chung.
- **Kỹ năng di cư từ Azure OpenAI → Responses API** dưới
  `.github/skills/azure-openai-to-responses/` dùng để hướng dẫn việc di cư API.

### Đã thay đổi

- **Chat Completions API → Responses API** trên tất cả mẫu chat Python và TypeScript
  (`client.responses.create(...)` → `response.output_text`), bao gồm các bài học 04, 06, 07, 11,
  15, và 18, cùng với các README của chúng.
- **GitHub Models → Microsoft Foundry Models** trên toàn bộ văn bản, liên kết và mẫu. GitHub Models
  sẽ nghỉ hưu vào cuối tháng 7 năm 2026; các mẫu hiện nay trỏ tới danh mục mô hình Microsoft Foundry và sử dụng
  biến môi trường `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL`.
- **`.env.copy`, `AGENTS.md`, và tài liệu nhà cung cấp** được cập nhật để phản ánh rằng Azure OpenAI hiện là một phần
  của Microsoft Foundry, và phiên bản API mặc định được nâng lên `2024-10-21`.
- **Mẫu TypeScript** (bài học 06, 07, 08, 11) di cư khỏi SDK `@azure/openai` beta đã lỗi thời
  sang gói `openai` (ứng dụng chat sử dụng Responses API; ứng dụng tìm kiếm sử dụng
  client embeddings).
- **Sổ tay .NET** (`dotnet/*.dib`) chuẩn hóa trên `Azure.AI.OpenAI` **2.1.0**: các bài học 06 và 07
  sử dụng API `ChatClient`, bài học 08 sử dụng `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`), và
  bài học 09 sử dụng `ImageClient` (`GenerateImage`) với `gpt-image-1`, thay thế
  các `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` cũ từ `1.0.0-beta.9`.
- **Hiện đại hóa tên sản phẩm**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (bài học 14, 16, 17) và "Bing" → **Microsoft Copilot** (bài học 12), ở những nơi đề cập tới
  các sản phẩm hiện tại.
- **DevContainer** (`.devcontainer/`) hiện bao gồm các tiện ích mở rộng Pylance, Black, Ruff, ESLint, Prettier, và Copilot,
  kích hoạt tính năng định dạng khi lưu, và cài đặt `ruff`, `black`, `mypy`, và `pytest` để các kiểm
  tra CI có thể được tái tạo cục bộ.
- **Tạo ảnh** (bài học 09) đề xuất `gpt-image-1` cho Azure (danh mục Azure đã bỏ
  `dall-e-3`).
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** được cập nhật để phản ánh công việc đã hoàn thành (di chuyển API, CI,
  DevContainer, kiểm thử) và các thực tế hiện tại (bản dịch được tạo tự động bởi
  Azure Co-op Translator; API Assistants đã bị thay thế bởi API Responses).

### Đã sửa

- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` hiện trả về
  chuỗi rỗng cho đầu vào chỉ chứa khoảng trắng thay vì gây lỗi "quá ngắn" (phù hợp với
  Trường hợp `None`). Được tìm thấy và bao phủ bởi bộ kiểm thử mới.
- **Mẫu ảnh bài học 09** — sửa lỗi thực tế: `InvalidRequestError` → `BadRequestError`,
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,
  và một biến che khuất mô-đun `openai`.
- **Sổ tay RAG bài học 15** — sửa thiết lập client, thay thế `DataFrame.append` đã bị loại bỏ
  bằng `pd.concat`, và hiện đại hóa việc sử dụng SDK cũ.
- Tên mô hình bị ngưng / loại bỏ (`gpt-3.5-turbo`, `gpt-35-turbo`) được thay thế bằng `gpt-4o-mini`
  trong các mẫu đang hoạt động; đầu ra tinh chỉnh lịch sử ở bài học 18 được giữ nguyên và chú thích
  thay vì viết lại.

### Bị ngưng / Ghi chú

- **Mẫu Microsoft Foundry Models** sử dụng `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK (`client.complete()`) — các mẫu `githubmodels-*` và `js-githubmodels` cùng bài học 19, 20,
  và 21 — vẫn nằm trên Model Inference API, vốn **không** hỗ trợ Responses API. Những phần này
  được cố ý giữ lại trên SDK đó.
- `AzureOpenAI()` được giữ lại một cách có chủ đích khi vẫn phù hợp (embedding và tạo hình ảnh),
  vì các quy trình này không thuộc di chuyển sang Responses API.
- Các tham chiếu `text-embedding-ada-002` được giữ lại khi một chỉ mục embedding đã được tính trước phụ thuộc vào chúng.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->