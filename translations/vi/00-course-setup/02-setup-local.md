# Cài Đặt Cục Bộ 🖥️

**Sử dụng hướng dẫn này nếu bạn muốn chạy mọi thứ trên laptop của mình.**   
Bạn có hai lựa chọn: **(A) Python bản gốc + virtual-env** hoặc **(B) VS Code Dev Container với Docker**.  
Chọn cách nào thấy dễ hơn—cả hai đều dẫn đến cùng bài học.

## 1.  Yêu Cầu Trước

| Công cụ            | Phiên bản / Ghi chú                                                                |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**          | 3.10 + (lấy tại <https://python.org>)                                               |
| **Git**             | Mới nhất (đi kèm Xcode / Git cho Windows / trình quản lý gói trên Linux)             |
| **VS Code**         | Tùy chọn nhưng khuyên dùng <https://code.visualstudio.com>                          |
| **Docker Desktop**  | *Chỉ* cho Tùy chọn B. Cài đặt miễn phí: <https://docs.docker.com/desktop/>           |

> 💡 **Mẹo** – Kiểm tra công cụ trong terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Tùy Chọn A – Python bản gốc (nhanh nhất)

### Bước 1  Clone repo này

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Bước 2 Tạo & kích hoạt môi trường ảo

```bash
python -m venv .venv          # tạo một
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Dấu nhắc lệnh giờ nên bắt đầu với (.venv)—tức là bạn đã vào trong môi trường.

### Bước 3 Cài đặt phụ thuộc

```bash
pip install -r requirements.txt
```

Bỏ qua đến Mục 3 về [khóa API](#3-thêm-khóa-api-của-bạn)

## 2. Tùy Chọn B – VS Code Dev Container (Docker)

Chúng tôi thiết lập repo và khóa học này với một [container phát triển](https://containers.dev?WT.mc_id=academic-105485-koreyst) có môi trường runtime đa năng hỗ trợ phát triển Python3, .NET, Node.js và Java. Cấu hình liên quan được định nghĩa trong file `devcontainer.json` nằm trong thư mục `.devcontainer/` ở thư mục gốc của repo.

>**Tại sao chọn cách này?**
>Môi trường giống hệt Codespaces; không bị lệch phụ thuộc.

### Bước 0 Cài đặt bổ sung

Docker Desktop – kiểm tra ```docker --version``` vận hành.
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers).

### Bước 1 Mở repo trong VS Code

File ▸ Mở Thư mục…  → generative-ai-for-beginners

VS Code sẽ phát hiện .devcontainer/ và hiển thị lời nhắc.

### Bước 2 Mở lại trong container

Nhấn “Mở lại trong Container”. Docker xây dựng image (≈ 3 phút lần đầu).  
Khi dấu nhắc terminal xuất hiện, bạn đang ở trong container.

## 2.  Tùy Chọn C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) là trình cài đặt nhẹ để cài [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python và một vài gói khác.  
Bản thân Conda là trình quản lý gói, giúp dễ dàng thiết lập và chuyển đổi giữa các [môi trường ảo](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python và các gói. Nó cũng hữu ích khi cài các gói không có sẵn qua `pip`.

### Bước 0  Cài đặt Miniconda

Theo [hướng dẫn cài đặt MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) để thiết lập.

```bash
conda --version
```

### Bước 1 Tạo môi trường ảo

Tạo file môi trường mới (*environment.yml*). Nếu bạn dùng Codespaces theo hướng dẫn, tạo trong thư mục `.devcontainer`, tức là `.devcontainer/environment.yml`.

### Bước 2  Điền nội dung file môi trường

Thêm đoạn sau vào file `environment.yml`

```yml
name: <environment-name>
channels:
 - defaults
 - microsoft
dependencies:
- python=<python-version>
- openai
- python-dotenv
- pip
- pip:
    - azure-ai-ml

```

### Bước 3 Tạo môi trường Conda

Chạy các lệnh dưới đây trong dòng lệnh/terminal của bạn

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Đường dẫn con .devcontainer chỉ áp dụng cho các thiết lập Codespace
conda activate ai4beg
```

Tham khảo [hướng dẫn môi trường Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) nếu gặp lỗi.

## 2  Tùy Chọn D – Jupyter / Jupyter Lab cổ điển (trên trình duyệt)

> **Dành cho ai?**  
> Ai yêu giao diện Jupyter cổ điển hoặc muốn chạy notebook mà không cần VS Code.  

### Bước 1  Đảm bảo đã cài Jupyter

Để bắt đầu Jupyter cục bộ, vào terminal/dòng lệnh, chuyển đến thư mục khóa học rồi chạy:

```bash
jupyter notebook
```

hoặc

```bash
jupyterhub
```

Lệnh này sẽ khởi động một instance Jupyter và URL truy cập sẽ hiển thị trong cửa sổ dòng lệnh.

Khi truy cập URL đó, bạn sẽ thấy đề cương khóa học và có thể mở mọi file `*.ipynb`. Ví dụ, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Thêm Khóa API Của Bạn

Giữ khóa API an toàn rất quan trọng khi xây dựng ứng dụng. Chúng tôi khuyên bạn không lưu khóa API trực tiếp trong code. Đưa chi tiết vào repo công khai có thể gây rủi ro bảo mật và phí phát sinh nếu bị người xấu sử dụng.
Đây là hướng dẫn từng bước cách tạo file `.env` cho Python và thêm thông tin đăng nhập Microsoft Foundry Models:

> **Lưu ý:** GitHub Models (và biến `GITHUB_TOKEN`) sẽ ngưng hoạt động cuối tháng 7 năm 2026. Hướng dẫn này dùng [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) thay thế. Muốn làm việc hoàn toàn offline? Xem [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Đi đến Thư mục Dự án**: Mở terminal hoặc command prompt, chuyển tới thư mục gốc dự án nơi bạn muốn tạo file `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Tạo file `.env`**: Dùng trình soạn thảo yêu thích tạo file mới tên `.env`. Nếu dùng dòng lệnh, bạn có thể dùng `touch` (trên hệ Unix) hoặc `echo` (trên Windows):

   Hệ Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Chỉnh sửa file `.env`**: Mở file `.env` trong trình soạn thảo (ví dụ VS Code, Notepad++, hay bất kỳ editor nào). Thêm dòng sau, thay các chỗ giữ chỗ bằng endpoint dự án Microsoft Foundry và khóa API thật của bạn:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Lưu file**: Lưu lại và đóng trình soạn thảo.

5. **Cài `python-dotenv`**: Nếu chưa cài, bạn cần cài package `python-dotenv` để tải biến môi trường từ file `.env` vào ứng dụng Python. Dùng `pip` để cài:

   ```bash
   pip install python-dotenv
   ```

6. **Tải biến môi trường trong script Python**: Trong script Python, dùng package `python-dotenv` để tải biến từ file `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Tải các biến môi trường từ tệp .env
   load_dotenv()

   # Truy cập các biến Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Xong rồi! Bạn đã tạo file `.env`, thêm thông tin Microsoft Foundry Models và tải vào ứng dụng Python thành công.

🔐 Không bao giờ commit .env—nó đã nằm trong .gitignore rồi.
Hướng dẫn đầy đủ của nhà cung cấp nằm trong [`providers.md`](03-providers.md).

## 4. Tiếp theo là gì?

| Tôi muốn…          | Đến…                                                                 |
|---------------------|---------------------------------------------------------------------|
| Bắt đầu Bài 1       | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md) |
| Cài đặt Nhà cung cấp LLM | [`providers.md`](03-providers.md)                                  |
| Gặp gỡ học viên khác | [Tham gia Discord của chúng tôi](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Xử lý sự cố

| Triệu chứng                              | Cách khắc phục                                                  |
|-----------------------------------------|----------------------------------------------------------------|
| `python không tìm thấy`                  | Thêm Python vào PATH hoặc mở lại terminal sau khi cài đặt       |
| `pip` không thể build wheels (Windows)  | Chạy `pip install --upgrade pip setuptools wheel` rồi thử lại.  |
| `ModuleNotFoundError: dotenv`            | Chạy `pip install -r requirements.txt` (chưa cài env).          |
| Lỗi build Docker *No space left*         | Docker Desktop ▸ *Settings* ▸ *Resources* → tăng dung lượng đĩa|
| VS Code cứ nhắc mở lại                   | Có thể cả hai Tùy chọn đang hoạt động; chỉ chọn một (venv **hoặc** container)|
| OpenAI lỗi 401 / 429                      | Kiểm tra giá trị `OPENAI_API_KEY` / hạn mức yêu cầu             |
| Lỗi khi dùng Conda                       | Cài thư viện Microsoft AI bằng `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->