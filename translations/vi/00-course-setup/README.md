<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-17T20:33:48+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "vi"
}
-->
# Bắt đầu với khóa học này

Chúng tôi rất hào hứng khi bạn bắt đầu khóa học này và khám phá những điều bạn có thể tạo ra với AI Tạo sinh!

Để đảm bảo bạn thành công, trang này sẽ hướng dẫn các bước thiết lập, yêu cầu kỹ thuật và nơi bạn có thể nhận được sự hỗ trợ nếu cần.

## Các bước thiết lập

Để bắt đầu tham gia khóa học này, bạn cần hoàn thành các bước sau.

### 1. Fork kho lưu trữ này

[Fork toàn bộ kho lưu trữ này](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) vào tài khoản GitHub của bạn để có thể thay đổi bất kỳ mã nào và hoàn thành các thử thách. Bạn cũng có thể [gắn sao (🌟) cho kho lưu trữ này](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) để dễ dàng tìm thấy nó và các kho lưu trữ liên quan.

### 2. Tạo một Codespace

Để tránh bất kỳ vấn đề phụ thuộc nào khi chạy mã, chúng tôi khuyến nghị bạn chạy khóa học này trong [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Trong kho lưu trữ của bạn: **Code -> Codespaces -> New on main**

![Hộp thoại hiển thị các nút để tạo một codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Thêm một secret

1. ⚙️ Biểu tượng bánh răng -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Đặt tên là OPENAI_API_KEY, dán khóa của bạn, Lưu.

### 3. Tiếp theo là gì?

| Tôi muốn…           | Đi tới…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Bắt đầu Bài học 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Làm việc offline    | [`setup-local.md`](02-setup-local.md)                                   |
| Thiết lập nhà cung cấp LLM | [`providers.md`](03-providers.md)                                        |
| Gặp gỡ các học viên khác | [Tham gia Discord của chúng tôi](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Xử lý sự cố

| Triệu chứng                                | Cách khắc phục                                                  |
|-------------------------------------------|-----------------------------------------------------------------|
| Xây dựng container bị kẹt > 10 phút       | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal không được đính kèm; nhấp **+** ➜ *bash*               |
| `401 Unauthorized` từ OpenAI              | Sai / hết hạn `OPENAI_API_KEY`                                  |
| VS Code hiển thị “Dev container mounting…”| Làm mới tab trình duyệt—Codespaces đôi khi mất kết nối          |
| Kernel của Notebook bị thiếu              | Menu Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Hệ thống dựa trên Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Chỉnh sửa tệp `.env`**: Mở tệp `.env` trong trình chỉnh sửa văn bản (ví dụ: VS Code, Notepad++, hoặc bất kỳ trình chỉnh sửa nào khác). Thêm dòng sau vào tệp, thay thế `your_github_token_here` bằng token GitHub thực của bạn:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Lưu tệp**: Lưu các thay đổi và đóng trình chỉnh sửa văn bản.

5. **Cài đặt `python-dotenv`**: Nếu bạn chưa cài đặt, bạn cần cài đặt gói `python-dotenv` để tải các biến môi trường từ tệp `.env` vào ứng dụng Python của bạn. Bạn có thể cài đặt nó bằng `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Tải các biến môi trường trong script Python của bạn**: Trong script Python của bạn, sử dụng gói `python-dotenv` để tải các biến môi trường từ tệp `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Vậy là xong! Bạn đã tạo thành công tệp `.env`, thêm token GitHub của bạn và tải nó vào ứng dụng Python của bạn.

## Cách chạy trên máy tính của bạn

Để chạy mã trên máy tính của bạn, bạn cần cài đặt một phiên bản [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Sau đó, để sử dụng kho lưu trữ, bạn cần clone nó:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Khi bạn đã kiểm tra mọi thứ, bạn có thể bắt đầu!

## Các bước tùy chọn

### Cài đặt Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) là một trình cài đặt nhẹ để cài đặt [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, cũng như một số gói.
Conda là một trình quản lý gói, giúp dễ dàng thiết lập và chuyển đổi giữa các [**môi trường ảo**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python khác nhau và các gói. Nó cũng rất hữu ích để cài đặt các gói không có sẵn qua `pip`.

Bạn có thể làm theo [hướng dẫn cài đặt MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) để thiết lập.

Khi đã cài đặt Miniconda, bạn cần clone [kho lưu trữ](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (nếu bạn chưa làm).

Tiếp theo, bạn cần tạo một môi trường ảo. Để làm điều này với Conda, hãy tạo một tệp môi trường mới (_environment.yml_). Nếu bạn đang làm theo hướng dẫn sử dụng Codespaces, hãy tạo tệp này trong thư mục `.devcontainer`, tức là `.devcontainer/environment.yml`.

Hãy điền vào tệp môi trường của bạn với đoạn mã dưới đây:

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

Nếu bạn gặp lỗi khi sử dụng conda, bạn có thể cài đặt thủ công các Thư viện AI của Microsoft bằng lệnh sau trong terminal.

```
conda install -c microsoft azure-ai-ml
```

Tệp môi trường chỉ định các phụ thuộc mà chúng ta cần. `<environment-name>` là tên bạn muốn sử dụng cho môi trường Conda của mình, và `<python-version>` là phiên bản Python bạn muốn sử dụng, ví dụ, `3` là phiên bản chính mới nhất của Python.

Khi hoàn tất, bạn có thể tạo môi trường Conda của mình bằng cách chạy các lệnh dưới đây trong dòng lệnh/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Tham khảo [hướng dẫn về môi trường Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) nếu bạn gặp bất kỳ vấn đề nào.

### Sử dụng Visual Studio Code với tiện ích mở rộng hỗ trợ Python

Chúng tôi khuyến nghị sử dụng trình chỉnh sửa [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) với tiện ích mở rộng [hỗ trợ Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) được cài đặt cho khóa học này. Tuy nhiên, đây chỉ là một khuyến nghị và không phải là yêu cầu bắt buộc.

> **Lưu ý**: Bằng cách mở kho lưu trữ khóa học trong VS Code, bạn có tùy chọn thiết lập dự án trong một container. Điều này là nhờ vào thư mục [đặc biệt `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) có trong kho lưu trữ khóa học. Thông tin chi tiết sẽ được cung cấp sau.

> **Lưu ý**: Khi bạn clone và mở thư mục trong VS Code, nó sẽ tự động gợi ý bạn cài đặt tiện ích mở rộng hỗ trợ Python.

> **Lưu ý**: Nếu VS Code gợi ý bạn mở lại kho lưu trữ trong một container, hãy từ chối yêu cầu này để sử dụng phiên bản Python đã cài đặt trên máy tính của bạn.

### Sử dụng Jupyter trong trình duyệt

Bạn cũng có thể làm việc trên dự án bằng môi trường [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ngay trong trình duyệt của mình. Cả Jupyter cổ điển và [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) đều cung cấp môi trường phát triển rất tiện lợi với các tính năng như tự động hoàn thành, làm nổi bật mã, v.v.

Để bắt đầu Jupyter trên máy tính, hãy mở terminal/dòng lệnh, điều hướng đến thư mục khóa học và thực hiện:

```bash
jupyter notebook
```

hoặc

```bash
jupyterhub
```

Điều này sẽ khởi động một phiên bản Jupyter và URL để truy cập sẽ được hiển thị trong cửa sổ dòng lệnh.

Khi bạn truy cập URL, bạn sẽ thấy nội dung khóa học và có thể điều hướng đến bất kỳ tệp `*.ipynb` nào. Ví dụ, `08-building-search-applications/python/oai-solution.ipynb`.

### Chạy trong container

Một lựa chọn khác để thiết lập mọi thứ trên máy tính hoặc Codespace của bạn là sử dụng một [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Thư mục `.devcontainer` đặc biệt trong kho lưu trữ khóa học cho phép VS Code thiết lập dự án trong một container. Ngoài Codespaces, điều này sẽ yêu cầu cài đặt Docker, và thực sự, nó đòi hỏi một chút công việc, vì vậy chúng tôi chỉ khuyến nghị điều này cho những người có kinh nghiệm làm việc với container.

Một trong những cách tốt nhất để bảo mật các khóa API của bạn khi sử dụng GitHub Codespaces là sử dụng Codespace Secrets. Vui lòng làm theo hướng dẫn [quản lý secret của Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) để tìm hiểu thêm.

## Các bài học và yêu cầu kỹ thuật

Khóa học bao gồm 6 bài học lý thuyết và 6 bài học thực hành.

Đối với các bài học thực hành, chúng tôi sử dụng Azure OpenAI Service. Bạn sẽ cần quyền truy cập vào dịch vụ Azure OpenAI và một khóa API để chạy mã này. Bạn có thể đăng ký quyền truy cập bằng cách [hoàn thành đơn đăng ký này](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Trong khi chờ đơn đăng ký của bạn được xử lý, mỗi bài học thực hành cũng bao gồm một tệp `README.md` nơi bạn có thể xem mã và kết quả.

## Sử dụng Azure OpenAI Service lần đầu tiên

Nếu đây là lần đầu tiên bạn làm việc với dịch vụ Azure OpenAI, vui lòng làm theo hướng dẫn về cách [tạo và triển khai tài nguyên dịch vụ Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Sử dụng OpenAI API lần đầu tiên

Nếu đây là lần đầu tiên bạn làm việc với OpenAI API, vui lòng làm theo hướng dẫn về cách [tạo và sử dụng giao diện.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Gặp gỡ các học viên khác

Chúng tôi đã tạo các kênh trong [máy chủ Discord cộng đồng AI chính thức](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) để bạn gặp gỡ các học viên khác. Đây là một cách tuyệt vời để kết nối với các doanh nhân, nhà sáng tạo, sinh viên và bất kỳ ai muốn nâng cao kỹ năng về AI Tạo sinh.

[![Tham gia kênh discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Đội ngũ dự án cũng sẽ có mặt trên máy chủ Discord này để hỗ trợ các học viên.

## Đóng góp

Khóa học này là một sáng kiến mã nguồn mở. Nếu bạn thấy có những điểm cần cải thiện hoặc vấn đề, vui lòng tạo một [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) hoặc ghi lại một [vấn đề trên GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Đội ngũ dự án sẽ theo dõi tất cả các đóng góp. Đóng góp cho mã nguồn mở là một cách tuyệt vời để xây dựng sự nghiệp của bạn trong lĩnh vực AI Tạo sinh.

Hầu hết các đóng góp yêu cầu bạn đồng ý với Thỏa thuận Cấp phép Người đóng góp (CLA) tuyên bố rằng bạn có quyền và thực sự cấp cho chúng tôi quyền sử dụng đóng góp của bạn. Để biết thêm chi tiết, hãy truy cập [trang web Thỏa thuận Cấp phép Người đóng góp CLA](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Quan trọng: khi dịch văn bản trong kho lưu trữ này, vui lòng đảm bảo rằng bạn không sử dụng công cụ dịch tự động. Chúng tôi sẽ xác minh các bản dịch thông qua cộng đồng, vì vậy chỉ nên tham gia dịch trong các ngôn ngữ mà bạn thông thạo.

Khi bạn gửi một pull request, CLA-bot sẽ tự động xác định liệu bạn có cần cung cấp CLA hay không và sẽ gắn nhãn PR phù hợp (ví dụ: nhãn, bình luận). Chỉ cần làm theo hướng dẫn được cung cấp bởi bot. Bạn chỉ cần làm điều này một lần cho tất cả các kho lưu trữ sử dụng CLA của chúng tôi.

Dự án này đã áp dụng [Quy tắc ứng xử mã nguồn mở của Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Để biết thêm thông tin, hãy đọc FAQ về Quy tắc ứng xử hoặc liên hệ [Email opencode](opencode@microsoft.com) với bất kỳ câu hỏi hoặc ý kiến bổ sung nào.

## Hãy bắt đầu nào!
Bây giờ bạn đã hoàn thành các bước cần thiết để hoàn thành khóa học này, hãy bắt đầu bằng cách tìm hiểu [giới thiệu về AI tạo sinh và LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, chúng tôi khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.