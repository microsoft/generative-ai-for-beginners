# Bắt Đầu Với Khóa Học Này

Chúng tôi rất hào hứng khi bạn bắt đầu khóa học này và mong đợi được thấy bạn sẽ được truyền cảm hứng để xây dựng điều gì với AI Tạo Sinh (Generative AI)!

Để đảm bảo bạn thành công, trang này sẽ hướng dẫn các bước thiết lập, yêu cầu kỹ thuật và nơi bạn có thể tìm kiếm sự trợ giúp nếu cần.

## Các Bước Thiết Lập

Để bắt đầu khóa học này, bạn cần hoàn thành các bước sau:

### 1. Fork kho lưu trữ này

[Fork toàn bộ kho lưu trữ này](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) vào tài khoản GitHub của bạn để bạn có thể chỉnh sửa mã và hoàn thành các thử thách. Bạn cũng có thể [gắn sao (🌟) kho lưu trữ này](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) để dễ dàng tìm lại nó và các kho liên quan.

### 2. Tạo Codespace

Để tránh gặp lỗi phụ thuộc khi chạy mã, chúng tôi khuyên bạn nên chạy khóa học này trong [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Bạn có thể tạo bằng cách chọn tùy chọn `Code` trong kho bạn đã fork và chọn **Codespaces**.

![Hộp thị hiển thị nút tạo codespace](../../images/who-will-pay.webp?WT.mc_id=academic-105485-koreyst)

### 3. Lưu Trữ API Key

Giữ API key an toàn và bảo mật là điều quan trọng khi xây dựng ứng dụng. Không nên lưu trực tiếp API key trong mã. Việc commit các thông tin đó vào kho công khai có thể dẫn đến vấn đề bảo mật hoặc phát sinh chi phí nếu bị kẻ xấu lợi dụng.
Dưới đây là hướng dẫn tạo file `.env` trong Python và thêm `GITHUB_TOKEN`:

1. **Đi tới thư mục dự án của bạn:**: Mở terminal hoặc command prompt và điều hướng đến thư mục gốc của dự án nơi bạn muốn tạo file `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Tạo file `.env`**: Sử dụng trình soạn thảo văn bản yêu thích để tạo file mới có tên `.env`. Nếu dùng dòng lệnh, bạn có thể dùng `touch` (trên hệ điều hành Unix) hoặc  `echo` (trên  Windows):

   Hệ thống Unix:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo. > .env
   ```

3. **Chỉnh sửa file `.env`**: Mở file `.env` trong trình soạn thảo văn bản (ví dụ: VS Code, Notepad++ hoặc trình khác). Thêm dòng sau vào file, thay thế `your_github_token_here` bằng token GitHub thực tế của bạn:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Lưu file**: Lưu thay đổi và đóng trình soạn thảo.

5. **Cài đặt `python-dotenv`**: Nếu bạn chưa cài đặt, hãy cài gói `python-dotenv` để nạp biến môi trường từ file `.env` vào ứng dụng Python. Bạn có thể dùng lệnh `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Tải biến môi trường trong mã Python**: Trong script Python, sử dụng gói `python-dotenv` để nạp biến môi trường từ file `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Nạp biến môi trường từ file .env
   load_dotenv()

   # Truy cập biến GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Vậy là xong! Bạn đã tạo file `.env`, thêm token GitHub, và tải nó vào ứng dụng Python thành công.

## Cách chạy cục bộ trên máy tính

Để chạy mã cục bộ trên máy tính, bạn cần cài đặt phiên bản nào đó của [Python installed](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Sau đó, clone kho lưu trữ:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Khi bạn đã tải xong, bạn có thể bắt đầu!

## Các bước tùy chọn

### Cài đặt Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) là trình cài nhẹ giúp bạn cài [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python và một số gói cần thiết.
Conda là trình quản lý gói giúp bạn dễ dàng tạo và chuyển đổi giữa các [**môi trường ảo Python**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst).Nó cũng hữu ích để cài đặt các gói không có trong `pip`.

Bạn có thể làm theo [hướng dẫn cài đặt Miniconda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

Sau khi cài Miniconda, clone lại [kho lưu trữ này](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (nếu bạn chưa làm).

Tiếp theo, bạn cần tạo môi trường ảo bằng cách tạo file (environment.yml).
Nếu dùng Codespaces, hãy tạo file này trong thư mục `.devcontainer`, tức là `.devcontainer/environment.yml`.

Nội dung ví dụ:

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

Nếu bạn gặp lỗi khi dùng conda, có thể cài thư viện AI của Microsoft bằng lệnh:

```
conda install -c microsoft azure-ai-ml
```

Trong file environment, `<environment-name>` là tên môi trường Conda bạn muốn đặt, và `<python-version>` là phiên bản Python bạn muốn dùng, ví dụ, `3`.

Tạo và kích hoạt môi trường:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # chỉ áp dụng với Codespaces
conda activate ai4beg
```

Xem thêm [hướng dẫn môi trường Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) nếu gặp sự cố.

### Sử dụng Visual Studio Code với extension Python

Chúng tôi khuyến nghị dùng [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) cùng  [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). Tuy nhiên đây chỉ là gợi ý, và không yêu cầu bắt buộc.

> **Lưu ý**: Khi mở repo khóa học trong VS Code, bạn có thể thiết lập dự án bên trong container nhờ thư mục [đặc biệt `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst).

> **Lưu ý**: VS Code sẽ gợi ý bạn cài extension hỗ trợ Python.

> **Lưu ý**: Nếu được hỏi mở trong container, hãy từ chối để dùng phiên bản Python cài trên máy.

### Sử dụng Jupyter trong trình duyệt

Bạn cũng có thể làm việc trong [môi trường Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) trên trình duyệt, bao gồm Jupyter Classic và [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst).

Khởi chạy Jupyter:

```bash
jupyter notebook
```

hoặc

```bash
jupyterhub
```

URL truy cập sẽ hiển thị trên terminal.

Sau khi truy cập, bạn có thể mở các file `*.ipynb`. Ví dụ, `08-building-search-applications/python/oai-solution.ipynb`.

### Chạy bằng container

Một cách khác là sử dụng [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). Thư mục `.devcontainer` trong repo cho phép VS Code thiết lập môi trường container. Ngoài Codespaces, bạn cần cài Docker – chỉ nên dùng nếu đã quen với container.

Đảm bảo bảo mật API key khi dùng GitHub Codespaces bằng cách thiết lập [Bảo mật Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst).

## Bài Học và Yêu Cầu Kỹ Thuật

Khóa học gồm 6 bài học lý thuyết và 6 bài học lập trình.

Các bài lập trình dùng Azure OpenAI Service. Bạn cần đăng ký và có API key để chạy mã. Đăng ký tại [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Trong thời gian chờ phê duyệt, bạn vẫn có thể xem mã và kết quả trong file `README.md` của từng bài học.

## Lần đầu sử dụng Azure OpenAI Service

Nếu lần đầu sử dụng, làm theo [hướng dẫn tạo và triển khai tài nguyên Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Lần đầu sử dụng OpenAI API

Làm theo [hướng dẫn khởi đầu với OpenAI API.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Gặp gỡ người học khác

Chúng tôi đã tạo các kênh trên [Discord cộng đồng AI chính thức](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) để bạn giao lưu với người học khác, nhà sáng tạo, sinh viên và kỹ sư AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Nhóm phát triển cũng sẽ có mặt trên Discord để hỗ trợ.

## Đóng góp

Khóa học là sáng kiến mã nguồn mở. Nếu bạn thấy phần nào cần cải thiện, hãy tạo [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) hoặc [báo lỗi](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Đóng góp mã nguồn mở là cách tuyệt vời để xây dựng sự nghiệp trong Generative AI.

Bạn có thể cần ký [Thỏa thuận Cấp phép Người đóng góp (CLA).](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Lưu ý: Không sử dụng dịch máy để dịch nội dung trong kho lưu trữ. Chỉ dịch sang ngôn ngữ bạn thành thạo.

Khi bạn gửi pull request, bot CLA sẽ xác định bạn có cần ký CLA không và hướng dẫn cụ thể.

Dự án này đã áp dụng [Bộ Quy Tắc Ứng Xử Mã Nguồn Mở của Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Để biết thêm thông tin, vui lòng đọc phần Câu Hỏi Thường Gặp về Bộ Quy Tắc Ứng Xử hoặc liên hệ qua [Email opencode](opencode@microsoft.com) nếu bạn có bất kỳ câu hỏi hoặc góp ý nào thêm.

## Bắt đầu thôi

Giờ bạn đã hoàn tất các bước thiết lập, hãy bắt đầu bằng cách đọc [Giới thiệu về Generative AI và LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).