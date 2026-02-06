# Cài đặt cục bộ 🖥️

**Sử dụng hướng dẫn này nếu bạn muốn chạy mọi thứ trên laptop của riêng bạn.**  
Bạn có hai lựa chọn: **(A) Python gốc + virtual-env** hoặc **(B) VS Code Dev Container với Docker**.  
Chọn cách nào bạn thấy dễ hơn—cả hai đều dẫn đến cùng bài học.

## 1. Yêu cầu trước

| Công cụ            | Phiên bản / Ghi chú                                                                 |
|--------------------|-------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (tải từ <https://python.org>)                                                |
| **Git**            | Phiên bản mới nhất (đi kèm Xcode / Git cho Windows / trình quản lý gói Linux)       |
| **VS Code**        | Tùy chọn nhưng được khuyến nghị <https://code.visualstudio.com>                     |
| **Docker Desktop** | *Chỉ* cho Lựa chọn B. Cài đặt miễn phí: <https://docs.docker.com/desktop/>          |

> 💡 **Mẹo** – Kiểm tra công cụ trong terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Lựa chọn A – Python gốc (nhanh nhất)

### Bước 1  Sao chép repo này

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

✅ Dấu nhắc bây giờ sẽ bắt đầu với (.venv)—điều đó có nghĩa bạn đang ở trong môi trường ảo.

### Bước 3 Cài đặt các phụ thuộc

```bash
pip install -r requirements.txt
```

Bỏ qua đến Mục 3 về [API keys](../../../00-course-setup)

## 2. Lựa chọn B – VS Code Dev Container (Docker)

Chúng tôi thiết lập kho lưu trữ và khóa học này với một [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) có runtime đa năng hỗ trợ phát triển Python3, .NET, Node.js và Java. Cấu hình liên quan được định nghĩa trong file `devcontainer.json` nằm trong thư mục `.devcontainer/` ở thư mục gốc của repo này.

>**Tại sao chọn cách này?**  
>Môi trường giống hệt Codespaces; không bị lệch phụ thuộc.

### Bước 0 Cài đặt các phần bổ sung

Docker Desktop – xác nhận ```docker --version``` hoạt động.  
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers).

### Bước 1 Mở repo trong VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code phát hiện .devcontainer/ và hiện thông báo.

### Bước 2 Mở lại trong container

Nhấn “Reopen in Container”. Docker sẽ build image (≈ 3 phút lần đầu).  
Khi dấu nhắc terminal xuất hiện, bạn đang ở trong container.

## 2. Lựa chọn C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) là trình cài đặt nhẹ để cài đặt [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, cũng như một vài gói.  
Conda là trình quản lý gói, giúp dễ dàng thiết lập và chuyển đổi giữa các [môi trường ảo](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) và các gói Python khác nhau. Nó cũng hữu ích để cài các gói không có trên `pip`.

### Bước 0  Cài đặt Miniconda

Theo dõi [hướng dẫn cài đặt MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) để thiết lập.

```bash
conda --version
```

### Bước 1 Tạo môi trường ảo

Tạo file môi trường mới (*environment.yml*). Nếu bạn dùng Codespaces, tạo trong thư mục `.devcontainer`, tức là `.devcontainer/environment.yml`.

### Bước 2  Điền file môi trường

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

Chạy các lệnh dưới đây trong dòng lệnh/terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Đường dẫn phụ .devcontainer chỉ áp dụng cho các thiết lập Codespace
conda activate ai4beg
```

Tham khảo [hướng dẫn môi trường Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) nếu gặp sự cố.

## 2  Lựa chọn D – Jupyter / Jupyter Lab cổ điển (trên trình duyệt)

> **Dành cho ai?**  
> Ai yêu thích giao diện Jupyter cổ điển hoặc muốn chạy notebook mà không cần VS Code.  

### Bước 1  Đảm bảo đã cài Jupyter

Để khởi động Jupyter cục bộ, mở terminal/dòng lệnh, chuyển đến thư mục khóa học, và chạy:

```bash
jupyter notebook
```

hoặc

```bash
jupyterhub
```

Điều này sẽ khởi động một phiên Jupyter và URL truy cập sẽ hiển thị trong cửa sổ dòng lệnh.

Khi truy cập URL, bạn sẽ thấy đề cương khóa học và có thể mở bất kỳ file `*.ipynb` nào. Ví dụ, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Thêm API Keys của bạn

Giữ an toàn cho API keys rất quan trọng khi xây dựng ứng dụng. Chúng tôi khuyên bạn không lưu API keys trực tiếp trong code. Đưa thông tin này lên repo công khai có thể gây rủi ro bảo mật và chi phí không mong muốn nếu bị kẻ xấu lợi dụng.  
Dưới đây là hướng dẫn từng bước tạo file `.env` cho Python và thêm `GITHUB_TOKEN`:

1. **Đi đến thư mục dự án của bạn**: Mở terminal hoặc command prompt và chuyển đến thư mục gốc dự án nơi bạn muốn tạo file `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Tạo file `.env`**: Dùng trình soạn thảo yêu thích để tạo file mới tên `.env`. Nếu dùng dòng lệnh, bạn có thể dùng `touch` (trên hệ Unix) hoặc `echo` (trên Windows):

   Hệ Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Chỉnh sửa file `.env`**: Mở file `.env` trong trình soạn thảo (ví dụ VS Code, Notepad++, hoặc bất kỳ trình nào). Thêm dòng sau, thay `your_github_token_here` bằng token GitHub thật của bạn:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Lưu file**: Lưu thay đổi và đóng trình soạn thảo.

5. **Cài đặt `python-dotenv`**: Nếu chưa có, bạn cần cài gói `python-dotenv` để load biến môi trường từ file `.env` vào ứng dụng Python. Cài bằng `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Load biến môi trường trong script Python**: Trong script Python, dùng gói `python-dotenv` để load biến môi trường từ file `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Tải các biến môi trường từ tệp .env
   load_dotenv()

   # Truy cập biến GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Xong rồi! Bạn đã tạo thành công file `.env`, thêm token GitHub, và load nó vào ứng dụng Python.

🔐 Không bao giờ commit .env—file này đã được thêm vào .gitignore.  
Hướng dẫn đầy đủ cho nhà cung cấp có trong [`providers.md`](03-providers.md).

## 4. Tiếp theo là gì?

| Tôi muốn…           | Đi đến…                                                                 |
|---------------------|------------------------------------------------------------------------|
| Bắt đầu Bài học 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)    |
| Thiết lập nhà cung cấp LLM | [`providers.md`](03-providers.md)                                  |
| Gặp gỡ các học viên khác | [Tham gia Discord của chúng tôi](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Khắc phục sự cố

| Triệu chứng                              | Cách sửa                                                         |
|-----------------------------------------|------------------------------------------------------------------|
| `python not found`                      | Thêm Python vào PATH hoặc mở lại terminal sau khi cài đặt        |
| `pip` không thể build wheels (Windows) | `pip install --upgrade pip setuptools wheel` rồi thử lại.        |
| `ModuleNotFoundError: dotenv`           | Chạy `pip install -r requirements.txt` (chưa cài env).           |
| Docker build lỗi *No space left*         | Docker Desktop ▸ *Settings* ▸ *Resources* → tăng dung lượng đĩa. |
| VS Code liên tục nhắc mở lại             | Có thể bạn đang kích hoạt cả hai lựa chọn; chọn một (venv **hoặc** container)|
| Lỗi OpenAI 401 / 429                    | Kiểm tra giá trị `OPENAI_API_KEY` / giới hạn tốc độ yêu cầu.      |
| Lỗi khi dùng Conda                      | Cài thư viện Microsoft AI bằng `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->