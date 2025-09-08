<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T18:05:50+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "vi"
}
-->
# Cài Đặt Cục Bộ 🖥️

**Hãy dùng hướng dẫn này nếu bạn muốn chạy mọi thứ trên chính máy tính của mình.**  
Bạn có hai lựa chọn: **(A) Python gốc + virtual-env** hoặc **(B) VS Code Dev Container với Docker**.  
Chọn cách nào bạn thấy dễ hơn—cả hai đều dẫn đến cùng một nội dung học.

## 1.  Yêu cầu cần thiết

| Công cụ            | Phiên bản / Ghi chú                                                                 |
|--------------------|-------------------------------------------------------------------------------------|
| **Python**         | 3.10 trở lên (tải tại <https://python.org>)                                         |
| **Git**            | Mới nhất (có sẵn trong Xcode / Git for Windows / trình quản lý gói Linux)           |
| **VS Code**        | Không bắt buộc nhưng nên dùng <https://code.visualstudio.com>                       |
| **Docker Desktop** | *Chỉ* cho Lựa chọn B. Cài miễn phí: <https://docs.docker.com/desktop/>              |

> 💡 **Mẹo** – Kiểm tra công cụ trong terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Lựa chọn A – Python gốc (nhanh nhất)

### Bước 1  Clone repo này

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Bước 2 Tạo & kích hoạt môi trường ảo

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Dấu nhắc bây giờ sẽ bắt đầu với (.venv)—nghĩa là bạn đã vào môi trường ảo.

### Bước 3 Cài đặt các thư viện phụ thuộc

```bash
pip install -r requirements.txt
```

Chuyển sang Phần 3 về [API keys](../../../00-course-setup)

## 2. Lựa chọn B – VS Code Dev Container (Docker)

Chúng tôi đã thiết lập repo và khóa học này với một [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) có môi trường Universal hỗ trợ Python3, .NET, Node.js và Java. Cấu hình liên quan nằm trong file `devcontainer.json` ở thư mục `.devcontainer/` tại gốc repo.

>**Tại sao chọn cách này?**
>Môi trường giống hệt Codespaces; không lo lệch phiên bản thư viện.

### Bước 0 Cài đặt các phần bổ sung

Docker Desktop – xác nhận ```docker --version``` hoạt động.
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers).

### Bước 1 Mở repo trong VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code sẽ nhận diện .devcontainer/ và hiện thông báo.

### Bước 2 Mở lại trong container

Nhấn “Reopen in Container”. Docker sẽ build image (≈ 3 phút lần đầu).
Khi terminal hiện ra, bạn đã ở trong container.

## 2.  Lựa chọn C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) là trình cài đặt nhẹ để cài [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python và một số gói cơ bản.
Conda là trình quản lý gói, giúp dễ dàng thiết lập và chuyển đổi giữa các [**môi trường ảo**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) và các gói Python khác nhau. Nó cũng hữu ích khi cài các gói không có trên `pip`.

### Bước 0  Cài đặt Miniconda

Làm theo [hướng dẫn cài đặt MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) để thiết lập.

```bash
conda --version
```

### Bước 1 Tạo môi trường ảo

Tạo một file môi trường mới (*environment.yml*). Nếu bạn đang làm theo bằng Codespaces, hãy tạo file này trong thư mục `.devcontainer`, tức là `.devcontainer/environment.yml`.

### Bước 2  Thêm nội dung vào file môi trường

Thêm đoạn sau vào `environment.yml` của bạn

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

Chạy các lệnh dưới đây trong command line/terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Tham khảo [hướng dẫn về môi trường Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) nếu gặp vấn đề.

## 2  Lựa chọn D – Jupyter cổ điển / Jupyter Lab (trên trình duyệt)

> **Dành cho ai?**  
> Những ai thích giao diện Jupyter cổ điển hoặc muốn chạy notebook mà không cần VS Code.  

### Bước 1  Đảm bảo đã cài Jupyter

Để khởi động Jupyter tại máy, mở terminal/command line, chuyển đến thư mục khóa học, và chạy:

```bash
jupyter notebook
```

hoặc

```bash
jupyterhub
```

Lệnh này sẽ khởi động Jupyter và hiển thị URL truy cập trong cửa sổ command line.

Khi truy cập URL, bạn sẽ thấy mục lục khóa học và có thể mở bất kỳ file `*.ipynb` nào. Ví dụ, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Thêm API Key của bạn

Giữ an toàn cho API key là rất quan trọng khi xây dựng bất kỳ ứng dụng nào. Chúng tôi khuyên bạn không nên lưu API key trực tiếp trong mã nguồn. Đẩy thông tin này lên repo công khai có thể gây rủi ro bảo mật và phát sinh chi phí không mong muốn nếu bị kẻ xấu sử dụng.
Dưới đây là hướng dẫn từng bước để tạo file `.env` cho Python và thêm `GITHUB_TOKEN`:

1. **Chuyển đến thư mục dự án**: Mở terminal hoặc command prompt và chuyển đến thư mục gốc dự án nơi bạn muốn tạo file `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Tạo file `.env`**: Dùng trình soạn thảo bạn thích để tạo file mới tên là `.env`. Nếu dùng command line, có thể dùng `touch` (trên hệ Unix) hoặc `echo` (trên Windows):

   Hệ Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Chỉnh sửa file `.env`**: Mở file `.env` bằng trình soạn thảo (VD: VS Code, Notepad++, hoặc bất kỳ editor nào). Thêm dòng sau vào file, thay `your_github_token_here` bằng token GitHub thực tế của bạn:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Lưu file**: Lưu lại và đóng trình soạn thảo.

5. **Cài đặt `python-dotenv`**: Nếu chưa cài, bạn cần cài gói `python-dotenv` để nạp biến môi trường từ file `.env` vào ứng dụng Python. Cài bằng `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Nạp biến môi trường trong script Python**: Trong script Python, dùng gói `python-dotenv` để nạp biến môi trường từ file `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Vậy là xong! Bạn đã tạo thành công file `.env`, thêm GitHub token và nạp nó vào ứng dụng Python.

🔐 Không bao giờ commit .env—file này đã nằm trong .gitignore rồi.
Hướng dẫn chi tiết cho từng nhà cung cấp nằm trong [`providers.md`](03-providers.md).

## 4. Tiếp theo làm gì?

| Tôi muốn…           | Đến…                                                                      |
|---------------------|---------------------------------------------------------------------------|
| Bắt đầu Bài 1       | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)       |
| Thiết lập LLM Provider | [`providers.md`](03-providers.md)                                         |
| Gặp gỡ các học viên khác | [Tham gia Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Xử lý sự cố

| Triệu chứng                                 | Cách khắc phục                                                    |
|---------------------------------------------|-------------------------------------------------------------------|
| `python not found`                          | Thêm Python vào PATH hoặc mở lại terminal sau khi cài đặt         |
| `pip` không build được wheels (Windows)     | `pip install --upgrade pip setuptools wheel` rồi thử lại.         |
| `ModuleNotFoundError: dotenv`               | Chạy `pip install -r requirements.txt` (chưa cài môi trường).     |
| Docker build lỗi *No space left*            | Docker Desktop ▸ *Settings* ▸ *Resources* → tăng dung lượng ổ đĩa.|
| VS Code liên tục nhắc mở lại                | Có thể bạn đang dùng cả hai lựa chọn; chọn một (venv **hoặc** container)|
| Lỗi OpenAI 401 / 429                        | Kiểm tra giá trị `OPENAI_API_KEY` / giới hạn tần suất request.    |
| Lỗi khi dùng Conda                          | Cài thư viện AI của Microsoft bằng `conda install -c microsoft azure-ai-ml`|

---

**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.