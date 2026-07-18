# Bắt đầu với khóa học này

Chúng tôi rất vui mừng khi bạn bắt đầu khóa học này và xem bạn sẽ được truyền cảm hứng xây dựng gì với Generative AI!

Để đảm bảo thành công của bạn, trang này trình bày các bước thiết lập, các yêu cầu kỹ thuật, và nơi để bạn nhận trợ giúp nếu cần.

## Các bước thiết lập

Để bắt đầu khóa học này, bạn sẽ cần hoàn thành các bước sau.

### 1. Sao chép Repo này

[Sao chép toàn bộ repo này](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) vào tài khoản GitHub của bạn để có thể thay đổi mã và hoàn thành các thử thách. Bạn cũng có thể [đánh dấu (🌟) repo này](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) để dễ dàng tìm lại repo và các repo liên quan.

### 2. Tạo một codespace

Để tránh các vấn đề phụ thuộc khi chạy mã, chúng tôi khuyên bạn nên chạy khóa học này trong [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Trong bản sao của bạn: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/vi/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Thêm một bí mật

1. ⚙️ Biểu tượng bánh răng -> Command Pallete -> Codespaces : Quản lý bí mật người dùng -> Thêm bí mật mới.
2. Đặt tên OPENAI_API_KEY, dán khóa của bạn, Lưu.

### 3. Tiếp theo là gì?

| Tôi muốn…          | Đi đến…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Bắt đầu Bài học 1  | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Làm việc offline   | [`setup-local.md`](02-setup-local.md)                                   |
| Thiết lập nhà cung cấp LLM | [`providers.md`](03-providers.md)                                        |
| Gặp gỡ học viên khác | [Tham gia Discord của chúng tôi](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Khắc phục sự cố


| Triệu chứng                               | Cách khắc phục                                                  |
|-------------------------------------------|-----------------------------------------------------------------|
| Quá trình xây dựng container dừng > 10 phút | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal chưa được đính kèm; nhấn **+** ➜ *bash*                 |
| `401 Unauthorized` từ OpenAI              | `OPENAI_API_KEY` sai hoặc hết hạn                                |
| VS Code hiển thị “Dev container mounting…” | Tải lại tab trình duyệt — Codespaces đôi khi mất kết nối         |
| Kernel notebook bị mất                    | Menu notebook ➜ **Kernel ▸ Chọn Kernel ▸ Python 3**             |

   Hệ thống dựa trên Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Chỉnh sửa file `.env`**: Mở file `.env` trong trình soạn thảo văn bản (ví dụ VS Code, Notepad++, hoặc bất kỳ trình soạn thảo nào khác). Thêm các dòng sau vào file, thay thế các chỗ giữ chỗ bằng endpoint và khóa thực tế của bạn từ Microsoft Foundry Models (xem [`providers.md`](03-providers.md) để biết cách lấy):

   > **Lưu ý:** GitHub Models (và biến `GITHUB_TOKEN` của nó) sẽ được ngừng hoạt động vào cuối tháng 7 năm 2026. Hãy sử dụng [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) thay thế.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Lưu file**: Lưu các thay đổi và đóng trình soạn thảo văn bản.

5. **Cài đặt `python-dotenv`**: Nếu bạn chưa có, bạn cần cài đặt gói `python-dotenv` để tải các biến môi trường từ file `.env` vào ứng dụng Python của bạn. Bạn có thể cài đặt bằng `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Tải biến môi trường vào script Python**: Trong script Python, sử dụng gói `python-dotenv` để tải các biến môi trường từ file `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Tải biến môi trường từ file .env
   load_dotenv()

   # Truy cập các biến của Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Thế là xong! Bạn đã tạo thành công file `.env`, thêm thông tin đăng nhập Microsoft Foundry Models của bạn, và tải chúng vào ứng dụng Python.

## Cách chạy trên máy tính cục bộ của bạn

Để chạy mã cục bộ trên máy tính của bạn, bạn cần phải có một phiên bản [Python được cài đặt](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Sau đó để sử dụng kho lưu trữ này, bạn cần clone nó:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Khi mọi thứ đã được tải xuống, bạn có thể bắt đầu!

## Các bước tùy chọn

### Cài đặt Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) là một trình cài đặt nhẹ để cài đặt [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, và một vài gói.
Conda là một trình quản lý gói, giúp dễ dàng thiết lập và chuyển đổi giữa các [môi trường ảo](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) và các gói Python khác nhau. Nó cũng rất hữu ích để cài các gói không có sẵn qua `pip`.

Bạn có thể theo hướng dẫn [cài đặt MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) để thiết lập.

Sau khi cài Miniconda, bạn cần clone [repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (nếu bạn chưa làm).

Tiếp theo, bạn cần tạo môi trường ảo. Để làm vậy với Conda, hãy tạo một file môi trường mới (_environment.yml_). Nếu bạn đang làm việc theo Codespaces, tạo file này trong thư mục `.devcontainer`, tức là `.devcontainer/environment.yml`.

Hãy điền đoạn sau vào file môi trường của bạn:

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

Nếu bạn gặp lỗi khi dùng conda, bạn có thể cài thủ công Microsoft AI Libraries bằng lệnh sau trong terminal.

```
conda install -c microsoft azure-ai-ml
```

File môi trường xác định các phụ thuộc cần thiết. `<environment-name>` là tên bạn muốn đặt cho môi trường Conda của bạn, và `<python-version>` là phiên bản Python bạn muốn dùng, ví dụ `3` là phiên bản chính mới nhất của Python.

Sau khi xong, bạn có thể tiến hành tạo môi trường Conda bằng cách chạy các lệnh dưới đây trong command line/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Đường dẫn phụ .devcontainer chỉ áp dụng cho các thiết lập Codespace
conda activate ai4beg
```

Tham khảo hướng dẫn [môi trường Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) nếu bạn gặp vấn đề.

### Sử dụng Visual Studio Code với tiện ích hỗ trợ Python

Chúng tôi khuyến nghị sử dụng trình soạn thảo [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) cùng với [tiện ích hỗ trợ Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) cho khóa học này. Tuy nhiên, đây chỉ là khuyến nghị chứ không phải yêu cầu bắt buộc.

> **Lưu ý**: Khi mở repo khóa học trong VS Code, bạn có thể thiết lập dự án trong một container nhờ thư mục [`.devcontainer` đặc biệt](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) có trong repo. Sẽ nói thêm về điều này sau.

> **Lưu ý**: Khi bạn clone và mở thư mục trong VS Code, nó sẽ tự động gợi ý bạn cài tiện ích hỗ trợ Python.

> **Lưu ý**: Nếu VS Code gợi ý bạn mở lại repo trong container, hãy từ chối để dùng phiên bản Python đã cài trên máy.

### Sử dụng Jupyter trên trình duyệt

Bạn cũng có thể làm việc trên dự án bằng môi trường [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ngay trong trình duyệt. Cả Jupyter truyền thống và [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) đều mang đến môi trường phát triển dễ chịu với các tính năng như tự động hoàn thành, tô sáng mã, v.v.

Để khởi động Jupyter trên máy cục bộ, hãy mở terminal/command line, chuyển đến thư mục khóa học và chạy:

```bash
jupyter notebook
```

hoặc

```bash
jupyterhub
```

Lệnh này sẽ khởi động một phiên bản Jupyter và URL truy cập sẽ hiển thị trong cửa sổ command line.

Khi truy cập URL, bạn sẽ thấy bố cục khóa học và có thể điều hướng vào bất kỳ file `*.ipynb` nào. Ví dụ, `08-building-search-applications/python/oai-solution.ipynb`.

### Chạy trong container

Một lựa chọn thay thế thay vì thiết lập mọi thứ trên máy tính hoặc Codespace là sử dụng [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Thư mục `.devcontainer` đặc biệt trong repo khóa học giúp VS Code có thể thiết lập dự án trong container. Nếu không dùng Codespaces, bạn cần cài Docker, và thật lòng mà nói thì khá phức tạp, vì vậy chúng tôi chỉ khuyên dùng cách này với những ai có kinh nghiệm làm việc với container.

Một trong những cách tốt nhất để giữ bảo mật các khóa API của bạn khi dùng GitHub Codespaces là sử dụng Bí mật Codespace. Vui lòng theo dõi [hướng dẫn quản lý bí mật Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) để biết thêm chi tiết.


## Các bài học và Yêu cầu kỹ thuật

Khóa học có các bài học "Học" giới thiệu các khái niệm Generative AI và các bài học "Xây dựng" với ví dụ mã thực hành bằng cả **Python** và **TypeScript** khi có thể.

Với các bài học mã hóa, chúng tôi sử dụng Azure OpenAI trong Microsoft Foundry. Bạn cần có đăng ký Azure và khóa API. Truy cập mở - không cần đăng ký - vì vậy bạn có thể [tạo tài nguyên Microsoft Foundry và triển khai mô hình](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) để lấy endpoint và khóa.

Mỗi bài học mã còn có file `README.md` để bạn xem mã và kết quả mà không cần chạy.

## Sử dụng Azure OpenAI Service lần đầu

Nếu đây là lần đầu bạn làm việc với dịch vụ Azure OpenAI, vui lòng theo hướng dẫn này về cách [tạo và triển khai tài nguyên Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Sử dụng OpenAI API lần đầu

Nếu đây là lần đầu bạn làm việc với OpenAI API, vui lòng theo hướng dẫn cách [tạo và sử dụng Giao diện.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Gặp gỡ Học viên khác

Chúng tôi đã tạo các kênh trong máy chủ chính thức [AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) để bạn có thể gặp gỡ những người học khác. Đây là cách tuyệt vời để kết nối với các doanh nhân, nhà xây dựng, sinh viên cùng chí hướng và bất kỳ ai muốn nâng cao trình độ trong Generative AI.

[![Tham gia kênh discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Nhóm dự án cũng sẽ có mặt trên máy chủ Discord này để hỗ trợ học viên.

## Đóng góp

Khóa học này là sáng kiến mã nguồn mở. Nếu bạn thấy chỗ nào cần cải thiện hoặc có lỗi, vui lòng tạo [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) hoặc ghi nhận [vấn đề trên GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Nhóm dự án sẽ theo dõi tất cả các đóng góp. Đóng góp vào mã nguồn mở là cách tuyệt vời để phát triển sự nghiệp trong Generative AI.

Hầu hết các đóng góp đòi hỏi bạn phải đồng ý với Thỏa thuận Cấp phép Người đóng góp (CLA) xác nhận rằng bạn có quyền và thực sự cấp cho chúng tôi quyền sử dụng đóng góp của bạn. Chi tiết xem tại [CLA, trang web Thỏa thuận Cấp phép Người đóng góp](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Quan trọng: khi dịch văn bản trong repo này, vui lòng đảm bảo bạn không sử dụng dịch máy. Chúng tôi sẽ xác minh bản dịch qua cộng đồng, vì vậy chỉ đăng ký dịch sang các ngôn ngữ mà bạn thành thạo.


Khi bạn gửi một yêu cầu kéo, một bot CLA sẽ tự động xác định xem bạn có cần cung cấp một CLA và trang trí PR một cách phù hợp (ví dụ: nhãn, bình luận). Chỉ cần làm theo hướng dẫn do bot cung cấp. Bạn chỉ cần làm điều này một lần cho tất cả các kho sử dụng CLA của chúng tôi.

Dự án này đã áp dụng [Bộ Quy Tắc Ứng Xử Mã Nguồn Mở Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Để biết thêm thông tin, hãy đọc phần Câu hỏi thường gặp về Bộ Quy Tắc Ứng Xử hoặc liên hệ [Email opencode](opencode@microsoft.com) nếu có bất kỳ câu hỏi hay nhận xét bổ sung nào.

## Bắt Đầu Nào

Bây giờ bạn đã hoàn thành các bước cần thiết để hoàn thành khóa học này, hãy bắt đầu bằng cách tìm hiểu [giới thiệu về AI Tạo Sinh và LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->