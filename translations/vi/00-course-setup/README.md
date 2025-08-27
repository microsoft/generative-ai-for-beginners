<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T18:06:33+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "vi"
}
-->
# Bắt đầu với khóa học này

Chúng tôi rất hào hứng khi bạn bắt đầu khóa học này và mong chờ xem bạn sẽ được truyền cảm hứng để xây dựng gì với AI Tạo sinh!

Để đảm bảo bạn thành công, trang này sẽ hướng dẫn các bước cài đặt, yêu cầu kỹ thuật và nơi bạn có thể nhận hỗ trợ nếu cần.

## Các bước cài đặt

Để bắt đầu khóa học này, bạn cần hoàn thành các bước sau.

### 1. Fork repo này

[Fork toàn bộ repo này](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) về tài khoản GitHub của bạn để có thể thay đổi mã nguồn và hoàn thành các thử thách. Bạn cũng có thể [gắn sao (🌟) repo này](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) để dễ dàng tìm lại nó và các repo liên quan.

### 2. Tạo codespace

Để tránh các vấn đề về phụ thuộc khi chạy mã, chúng tôi khuyến nghị bạn học khóa này trong [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Trong repo bạn đã fork: **Code -> Codespaces -> New on main**

![Hộp thoại hiển thị các nút để tạo codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Thêm một secret

1. ⚙️ Biểu tượng bánh răng -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Đặt tên OPENAI_API_KEY, dán key của bạn vào, Lưu lại.

### 3. Tiếp theo là gì?

| Tôi muốn…            | Đến…                                                                      |
|----------------------|---------------------------------------------------------------------------|
| Bắt đầu Bài học 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)       |
| Làm việc offline     | [`setup-local.md`](02-setup-local.md)                                     |
| Cài đặt nhà cung cấp LLM | [`providers.md`](providers.md)                                        |
| Gặp gỡ các học viên khác | [Tham gia Discord của chúng tôi](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Xử lý sự cố


| Triệu chứng                                 | Cách khắc phục                                                    |
|---------------------------------------------|-------------------------------------------------------------------|
| Xây dựng container bị treo > 10 phút        | **Codespaces ➜ “Rebuild Container”**                              |
| `python: command not found`                 | Terminal chưa được gắn; nhấn **+** ➜ *bash*                       |
| `401 Unauthorized` từ OpenAI                | `OPENAI_API_KEY` sai hoặc đã hết hạn                              |
| VS Code hiển thị “Dev container mounting…”  | Làm mới tab trình duyệt—Codespaces đôi khi bị mất kết nối         |
| Thiếu kernel cho Notebook                   | Menu Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**             |

   Hệ điều hành dựa trên Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Chỉnh sửa file `.env`**: Mở file `.env` bằng trình soạn thảo văn bản (ví dụ: VS Code, Notepad++, hoặc bất kỳ trình soạn thảo nào khác). Thêm dòng sau vào file, thay `your_github_token_here` bằng token GitHub thực tế của bạn:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Lưu file**: Lưu thay đổi và đóng trình soạn thảo.

5. **Cài đặt `python-dotenv`**: Nếu bạn chưa cài, bạn cần cài gói `python-dotenv` để nạp biến môi trường từ file `.env` vào ứng dụng Python. Bạn có thể cài bằng `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Nạp biến môi trường trong script Python**: Trong script Python của bạn, sử dụng gói `python-dotenv` để nạp biến môi trường từ file `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Vậy là xong! Bạn đã tạo thành công file `.env`, thêm token GitHub và nạp nó vào ứng dụng Python của mình.

## Cách chạy cục bộ trên máy tính của bạn

Để chạy mã trên máy tính cá nhân, bạn cần cài đặt một phiên bản [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Sau đó, để sử dụng repo, bạn cần clone nó:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Khi đã kiểm tra xong mọi thứ, bạn có thể bắt đầu!

## Các bước tùy chọn

### Cài đặt Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) là trình cài đặt nhẹ để cài [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, cùng một số gói cơ bản.
Conda là trình quản lý gói, giúp bạn dễ dàng thiết lập và chuyển đổi giữa các [**môi trường ảo**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python và các gói. Nó cũng rất hữu ích khi cài các gói không có sẵn qua `pip`.

Bạn có thể làm theo [hướng dẫn cài đặt MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) để thiết lập.

Sau khi cài Miniconda, bạn cần clone [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (nếu chưa làm).

Tiếp theo, bạn cần tạo một môi trường ảo. Để làm điều này với Conda, hãy tạo một file môi trường mới (_environment.yml_). Nếu bạn đang làm theo bằng Codespaces, hãy tạo file này trong thư mục `.devcontainer`, tức là `.devcontainer/environment.yml`.

Hãy điền nội dung sau vào file môi trường của bạn:

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

Nếu bạn gặp lỗi khi dùng conda, bạn có thể cài thủ công các thư viện AI của Microsoft bằng lệnh sau trong terminal.

```
conda install -c microsoft azure-ai-ml
```

File môi trường chỉ định các phụ thuộc cần thiết. `<environment-name>` là tên bạn muốn đặt cho môi trường Conda, và `<python-version>` là phiên bản Python bạn muốn dùng, ví dụ, `3` là phiên bản chính mới nhất của Python.

Sau đó, bạn có thể tạo môi trường Conda bằng cách chạy các lệnh sau trong dòng lệnh/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Tham khảo [hướng dẫn về môi trường Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) nếu bạn gặp vấn đề.

### Sử dụng Visual Studio Code với extension hỗ trợ Python

Chúng tôi khuyến nghị bạn sử dụng trình soạn thảo [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) với extension [hỗ trợ Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) cho khóa học này. Tuy nhiên, đây chỉ là khuyến nghị, không bắt buộc.

> **Lưu ý**: Khi mở repo khóa học trong VS Code, bạn có thể thiết lập dự án trong container. Điều này là nhờ thư mục [đặc biệt `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) có trong repo. Sẽ nói thêm về điều này sau.

> **Lưu ý**: Khi bạn clone và mở thư mục trong VS Code, VS Code sẽ tự động gợi ý cài extension hỗ trợ Python.

> **Lưu ý**: Nếu VS Code gợi ý bạn mở lại repo trong container, hãy từ chối để sử dụng phiên bản Python đã cài trên máy.

### Sử dụng Jupyter trên trình duyệt

Bạn cũng có thể làm việc với dự án bằng môi trường [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ngay trên trình duyệt. Cả Jupyter cổ điển và [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) đều cung cấp môi trường phát triển thân thiện với các tính năng như tự động hoàn thành, tô sáng mã, v.v.

Để khởi động Jupyter cục bộ, hãy mở terminal/dòng lệnh, chuyển đến thư mục khóa học và chạy:

```bash
jupyter notebook
```

hoặc

```bash
jupyterhub
```

Lệnh này sẽ khởi động một phiên Jupyter và URL truy cập sẽ hiển thị trong cửa sổ dòng lệnh.

Khi truy cập URL, bạn sẽ thấy cấu trúc khóa học và có thể mở bất kỳ file `*.ipynb` nào. Ví dụ, `08-building-search-applications/python/oai-solution.ipynb`.

### Chạy trong container

Một lựa chọn khác thay vì cài đặt mọi thứ trên máy hoặc Codespace là sử dụng [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Thư mục `.devcontainer` đặc biệt trong repo giúp VS Code thiết lập dự án trong container. Ngoài Codespaces, bạn sẽ cần cài Docker, và thực sự, cách này hơi phức tạp nên chỉ khuyến nghị cho những ai đã quen làm việc với container.

Một trong những cách tốt nhất để giữ an toàn cho API key khi dùng GitHub Codespaces là sử dụng Codespace Secrets. Hãy làm theo [hướng dẫn quản lý secrets của Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) để tìm hiểu thêm.


## Các bài học và yêu cầu kỹ thuật

Khóa học gồm 6 bài học lý thuyết và 6 bài học lập trình.

Với các bài học lập trình, chúng tôi sử dụng Azure OpenAI Service. Bạn sẽ cần quyền truy cập dịch vụ Azure OpenAI và một API key để chạy mã. Bạn có thể đăng ký quyền truy cập bằng cách [điền đơn này](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Trong lúc chờ xét duyệt, mỗi bài học lập trình cũng có file `README.md` để bạn xem mã và kết quả.

## Sử dụng Azure OpenAI Service lần đầu

Nếu đây là lần đầu bạn làm việc với Azure OpenAI Service, hãy làm theo hướng dẫn này để [tạo và triển khai tài nguyên Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Sử dụng OpenAI API lần đầu

Nếu đây là lần đầu bạn làm việc với OpenAI API, hãy làm theo hướng dẫn [tạo và sử dụng Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Gặp gỡ các học viên khác

Chúng tôi đã tạo các kênh trên [máy chủ Discord AI Community chính thức](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) để bạn gặp gỡ các học viên khác. Đây là cách tuyệt vời để kết nối với các doanh nhân, lập trình viên, sinh viên và bất kỳ ai muốn nâng cao kỹ năng về AI Tạo sinh.

[![Tham gia kênh discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Nhóm dự án cũng sẽ có mặt trên Discord này để hỗ trợ các học viên.

## Đóng góp

Khóa học này là một sáng kiến mã nguồn mở. Nếu bạn thấy có điểm cần cải thiện hoặc phát hiện lỗi, hãy tạo [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) hoặc báo cáo [vấn đề trên GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Nhóm dự án sẽ theo dõi mọi đóng góp. Đóng góp cho mã nguồn mở là cách tuyệt vời để phát triển sự nghiệp của bạn trong lĩnh vực AI Tạo sinh.

Hầu hết các đóng góp yêu cầu bạn đồng ý với Thỏa thuận cấp phép cho người đóng góp (CLA), xác nhận rằng bạn có quyền và thực sự cấp cho chúng tôi quyền sử dụng đóng góp của bạn. Xem chi tiết tại [trang web CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Lưu ý: khi dịch nội dung trong repo này, vui lòng không sử dụng dịch máy. Chúng tôi sẽ xác minh bản dịch qua cộng đồng, vì vậy chỉ nên tham gia dịch sang ngôn ngữ mà bạn thành thạo.

Khi bạn gửi pull request, một CLA-bot sẽ tự động xác định bạn có cần ký CLA không và đánh dấu PR phù hợp (ví dụ, nhãn, bình luận). Chỉ cần làm theo hướng dẫn của bot. Bạn chỉ cần làm việc này một lần cho tất cả các repo sử dụng CLA của chúng tôi.

Dự án này tuân theo [Bộ quy tắc ứng xử mã nguồn mở của Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Để biết thêm thông tin, hãy đọc phần Câu hỏi thường gặp về Quy tắc ứng xử hoặc liên hệ [Email opencode](opencode@microsoft.com) nếu có câu hỏi hoặc góp ý.

## Hãy bắt đầu nào
Bây giờ bạn đã hoàn thành các bước cần thiết để kết thúc khóa học này, hãy bắt đầu bằng việc tìm hiểu [giới thiệu về AI sinh tạo và các mô hình ngôn ngữ lớn (LLM)](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.