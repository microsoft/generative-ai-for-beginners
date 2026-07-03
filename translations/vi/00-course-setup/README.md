# Bắt đầu với khóa học này

Chúng tôi rất hào hứng khi bạn bắt đầu khóa học này và xem bạn được truyền cảm hứng để xây dựng gì với AI Tạo sinh!

Để đảm bảo bạn thành công, trang này sẽ trình bày các bước thiết lập, yêu cầu kỹ thuật và nơi để nhận trợ giúp nếu cần.

## Các bước thiết lập

Để bắt đầu học khóa học này, bạn cần hoàn thành các bước sau.

### 1. Fork Repo này

[Hãy fork toàn bộ repo này](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) vào tài khoản GitHub của bạn để có thể thay đổi bất kỳ mã nào và hoàn thành các thử thách. Bạn cũng có thể [star (🌟) repo này](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) để dễ dàng tìm kiếm nó và các repo liên quan.

### 2. Tạo một codespace

Để tránh các vấn đề về phụ thuộc khi chạy mã, chúng tôi khuyên bạn nên chạy khóa học này trong một [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Trong fork của bạn: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/vi/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Thêm một bí mật

1. ⚙️ Biểu tượng Bánh răng -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Đặt tên OPENAI_API_KEY, dán khóa của bạn vào, Lưu.

### 3. Tiếp theo là gì?

| Tôi muốn…              | Đến…                                                                  |
|------------------------|-------------------------------------------------------------------------|
| Bắt đầu Bài học 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Làm việc ngoại tuyến    | [`setup-local.md`](02-setup-local.md)                                   |
| Thiết lập Nhà cung cấp LLM | [`providers.md`](03-providers.md)                                        |
| Gặp gỡ các học viên khác | [Tham gia Discord của chúng tôi](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Khắc phục sự cố

| Triệu chứng                                  | Khắc phục                                                       |
|----------------------------------------------|-----------------------------------------------------------------|
| Container build kẹt > 10 phút                 | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`                    | Terminal không được gắn; nhấn **+** ➜ *bash*                    |
| `401 Unauthorized` từ OpenAI                   | Sai / hết hạn `OPENAI_API_KEY`                                  |
| VS Code hiển thị “Dev container mounting…”    | Làm mới tab trình duyệt — Codespaces đôi khi mất kết nối        |
| Kernel của Notebook bị mất                      | Menu notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Hệ điều hành Unix-based:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Chỉnh sửa File `.env`**: Mở file `.env` bằng trình soạn thảo văn bản (ví dụ: VS Code, Notepad++, hoặc bất cứ trình nào khác). Thêm dòng sau vào file, thay `your_github_token_here` bằng token GitHub của bạn:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Lưu file**: Lưu thay đổi và đóng trình soạn thảo.

5. **Cài `python-dotenv`**: Nếu bạn chưa có, bạn cần cài gói `python-dotenv` để tải các biến môi trường từ file `.env` vào ứng dụng Python của bạn. Bạn có thể cài bằng `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Tải biến môi trường trong script Python của bạn**: Trong script Python, sử dụng gói `python-dotenv` để tải biến môi trường từ file `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Tải các biến môi trường từ file .env
   load_dotenv()

   # Truy cập biến GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Xong rồi! Bạn đã tạo thành công file `.env`, thêm token GitHub và tải nó vào ứng dụng Python của bạn.

## Cách chạy code trên máy tính của bạn

Để chạy code trên máy tính của bạn, bạn cần có một phiên bản [Python được cài đặt](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Sau đó để sử dụng repository, bạn cần clone nó:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Khi đã có mọi thứ, bạn có thể bắt đầu!

## Các bước tùy chọn

### Cài Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) là một trình cài đặt nhẹ để cài [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python cũng như một số gói khác. Conda là trình quản lý gói giúp dễ dàng thiết lập và chuyển đổi giữa các [**môi trường ảo Python**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) và các gói. Nó cũng tiện lợi để cài các gói không có sẵn qua `pip`.

Bạn có thể theo hướng dẫn [Cài đặt MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) để thiết lập.

Khi đã cài Miniconda, bạn cần clone [repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (nếu bạn chưa clone).

Tiếp theo, bạn cần tạo một môi trường ảo. Để làm điều này với Conda, hãy tạo một file môi trường mới (_environment.yml_). Nếu bạn theo học trên Codespaces, hãy tạo file này trong thư mục `.devcontainer`, tức là `.devcontainer/environment.yml`.

Hãy thêm đoạn dưới vào file môi trường của bạn:

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

Nếu bạn gặp lỗi khi dùng conda, bạn có thể cài thủ công Thư viện AI của Microsoft bằng lệnh sau trong terminal.

```
conda install -c microsoft azure-ai-ml
```

File môi trường chỉ định các phụ thuộc cần thiết. `<environment-name>` là tên bạn muốn dùng cho môi trường Conda của bạn, và `<python-version>` là phiên bản Python bạn muốn dùng, ví dụ `3` là phiên bản chính mới nhất của Python.

Khi đã sẵn sàng, bạn có thể tạo môi trường Conda bằng cách chạy các lệnh dưới đây trong command line/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Đường dẫn phụ .devcontainer chỉ áp dụng cho các thiết lập Codespace
conda activate ai4beg
```

Tham khảo [hướng dẫn môi trường Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) nếu gặp vấn đề.

### Dùng Visual Studio Code với tiện ích hỗ trợ Python

Chúng tôi khuyên dùng trình soạn thảo [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) với tiện ích [hỗ trợ Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) để học. Tuy nhiên đây chỉ là khuyến nghị, không phải bắt buộc.

> **Lưu ý**: Khi mở repository khóa học trong VS Code, bạn có thể thiết lập dự án trong container. Do trong repo có thư mục đặc biệt [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). Chúng tôi sẽ nói thêm về điều này sau.

> **Lưu ý**: Khi clone và mở thư mục trong VS Code, nó sẽ tự động gợi ý bạn cài tiện ích hỗ trợ Python.

> **Lưu ý**: Nếu VS Code gợi ý bạn mở lại repo trong container, hãy từ chối để dùng phiên bản Python cài trên máy.

### Dùng Jupyter trên trình duyệt

Bạn cũng có thể làm việc với dự án bằng môi trường [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ngay trên trình duyệt của bạn. Cả Jupyter cổ điển lẫn [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) đều cung cấp môi trường phát triển tốt với các tính năng như tự hoàn thành, tô sáng mã, v.v.

Để khởi động Jupyter trên máy, mở terminal/dòng lệnh, chuyển đến thư mục khóa học và chạy:

```bash
jupyter notebook
```

hoặc

```bash
jupyterhub
```

Điều này sẽ khởi tạo một phiên Jupyter và URL truy cập sẽ được hiện trong cửa sổ dòng lệnh.

Khi truy cập URL, bạn sẽ thấy đề cương khóa học và có thể mở bất cứ file `*.ipynb` nào. Ví dụ như `08-building-search-applications/python/oai-solution.ipynb`.

### Chạy trong container

Một lựa chọn thay thế cho việc thiết lập mọi thứ trên máy hoặc Codespace là dùng [container](<https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Thư mục đặc biệt `.devcontainer` trong repo khóa học cho phép VS Code thiết lập dự án trong container. Ngoài Codespaces, bạn cần cài Docker, và thẳng thắn mà nói, việc này khá phức tạp, nên chúng tôi chỉ khuyên những ai có kinh nghiệm với container nên làm.

Một trong những cách tốt nhất để giữ an toàn cho các khóa API khi dùng GitHub Codespaces là sử dụng Bí mật Codespace. Xin theo dõi hướng dẫn về [quản lý bí mật Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) để tìm hiểu thêm.

## Các bài học và yêu cầu kỹ thuật

Khóa học gồm 6 bài học về khái niệm và 6 bài học lập trình.

Với các bài học lập trình, chúng tôi dùng Azure OpenAI Service. Bạn cần có quyền truy cập dịch vụ Azure OpenAI và một khóa API để chạy mã. Bạn có thể đăng ký truy cập bằng cách [hoàn thành đơn đăng ký này](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Trong khi chờ duyệt đơn, mỗi bài học lập trình cũng có file `README.md` để bạn xem mã và kết quả.

## Lần đầu dùng Azure OpenAI Service

Nếu đây là lần đầu bạn làm việc với dịch vụ Azure OpenAI, vui lòng làm theo hướng dẫn này về cách [tạo và triển khai tài nguyên Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Lần đầu dùng OpenAI API

Nếu đây là lần đầu bạn làm việc với OpenAI API, vui lòng làm theo hướng dẫn về cách [tạo và sử dụng giao diện.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Gặp gỡ các học viên khác

Chúng tôi đã tạo các kênh trên server [AI Community Discord chính thức](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) để gặp gỡ các học viên khác. Đây là cách tuyệt vời để kết nối với các doanh nhân, nhà xây dựng, sinh viên cùng chí hướng, và bất kỳ ai muốn nâng cao trình độ về AI Tạo sinh.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Nhóm dự án cũng sẽ có mặt trên server Discord này để hỗ trợ mọi học viên.

## Đóng góp

Khóa học này là sáng kiến mã nguồn mở. Nếu bạn thấy điểm cần cải tiến hoặc lỗi, vui lòng tạo [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) hoặc ghi nhận một [vấn đề GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Nhóm dự án sẽ theo dõi tất cả các đóng góp. Đóng góp vào mã nguồn mở là cách tuyệt vời để xây dựng sự nghiệp trong AI Tạo sinh.

Phần lớn đóng góp yêu cầu bạn đồng ý Thỏa thuận Cấp phép Người đóng góp (CLA) xác nhận bạn có quyền và thực sự cấp cho chúng tôi quyền sử dụng đóng góp của bạn. Chi tiết xem tại [CLA, Trang web Thỏa thuận Cấp phép Người đóng góp](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Quan trọng: khi dịch văn bản trong repo này, vui lòng không sử dụng dịch máy. Chúng tôi sẽ xác thực bản dịch qua cộng đồng, nên chỉ nhận tình nguyện dịch những ngôn ngữ bạn thông thạo.

Khi bạn gửi pull request, bot CLA-bot sẽ tự động xác định xem bạn có cần cung cấp CLA không và đánh dấu PR phù hợp (ví dụ: nhãn, bình luận). Hãy làm theo hướng dẫn của bot. Bạn chỉ cần làm một lần cho tất cả các repo dùng CLA của chúng tôi.

Dự án này đã áp dụng [Bộ Quy tắc Ứng xử Mã nguồn mở của Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Thông tin thêm xem FAQ về Bộ Quy tắc Ứng xử hoặc liên hệ [Email opencode](opencode@microsoft.com) nếu có thắc mắc.

## Hãy bắt đầu nào!
Bây giờ bạn đã hoàn thành các bước cần thiết để hoàn thành khóa học này, hãy bắt đầu bằng cách xem [giới thiệu về AI Tạo Sinh và LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi nỗ lực đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Văn bản gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->