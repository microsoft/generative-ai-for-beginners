# Bắt đầu với khóa học này

Chúng tôi rất hào hứng khi bạn bắt đầu khóa học này và xem bạn được truyền cảm hứng để xây dựng gì với Generative AI!

Để đảm bảo bạn thành công, trang này sẽ trình bày các bước cài đặt, yêu cầu kỹ thuật và nơi bạn có thể nhận được trợ giúp nếu cần.

## Các bước thiết lập

Để bắt đầu tham gia khóa học này, bạn cần hoàn thành các bước sau.

### 1. Fork repo này

[Fork toàn bộ repo này](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) vào tài khoản GitHub cá nhân của bạn để có thể chỉnh sửa bất kỳ mã nào và hoàn thành các thử thách. Bạn cũng có thể [đánh dấu sao (🌟) repo này](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) để dễ dàng tìm thấy nó và các repo liên quan.

### 2. Tạo codespace

Để tránh các vấn đề về phụ thuộc khi chạy mã, chúng tôi khuyên bạn nên chạy khóa học này trong [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Trong fork của bạn: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/vi/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Thêm một bí mật

1. ⚙️ Biểu tượng bánh răng -> Command Palette -> Codespaces : Manage user secret -> Add a new secret.
2. Đặt tên OPENAI_API_KEY, dán khóa của bạn, Lưu.

### 3. Tiếp theo là gì?

| Tôi muốn…          | Đi tới…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Bắt đầu Bài học 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Làm việc offline        | [`setup-local.md`](02-setup-local.md)                                   |
| Thiết lập Nhà cung cấp LLM | [`providers.md`](03-providers.md)                                        |
| Gặp gỡ các học viên khác | [Tham gia Discord của chúng tôi](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Khắc phục sự cố


| Triệu chứng                                   | Cách khắc phục                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| Quá trình dựng Container bị treo > 10 phút            | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal chưa được đính kèm; click **+** ➜ *bash*                    |
| `401 Unauthorized` từ OpenAI            | `OPENAI_API_KEY` sai hoặc hết hạn                                |
| VS Code hiển thị “Dev container mounting…”   | Làm tươi lại tab trình duyệt — Codespaces đôi khi mất kết nối   |
| Kernel notebook bị thiếu                   | Menu notebook ➜ **Kernel ▸ Chọn Kernel ▸ Python 3**           |

   Hệ thống Unix-based:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Chỉnh sửa file `.env`**: Mở file `.env` bằng trình soạn thảo văn bản (ví dụ: VS Code, Notepad++, hoặc bất kỳ trình soạn thảo nào khác). Thêm các dòng sau vào file, thay thế các chỗ giữ chỗ bằng endpoint và khóa thực tế của bạn cho Microsoft Foundry Models (xem [`providers.md`](03-providers.md) để biết cách lấy các thông tin này):

   > **Lưu ý:** GitHub Models (và biến `GITHUB_TOKEN` của nó) sẽ ngừng hoạt động vào cuối tháng 7 năm 2026. Hãy sử dụng [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) thay thế.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Lưu file**: Lưu những thay đổi và đóng trình soạn thảo văn bản lại.

5. **Cài đặt `python-dotenv`**: Nếu bạn chưa cài, bạn cần cài gói `python-dotenv` để tải các biến môi trường từ file `.env` vào ứng dụng Python của bạn. Bạn có thể cài đặt nó bằng `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Tải biến môi trường trong script Python của bạn**: Trong script Python, dùng gói `python-dotenv` để tải các biến môi trường từ file `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Tải các biến môi trường từ file .env
   load_dotenv()

   # Truy cập các biến Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Thế là xong! Bạn đã tạo thành công file `.env`, thêm thông tin xác thực Microsoft Foundry Models, và tải chúng vào ứng dụng Python.

## Cách chạy local trên máy tính của bạn

Để chạy mã local trên máy tính, bạn cần cài một phiên bản [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Sau đó, để sử dụng repo, bạn cần clone nó:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Khi đã có mọi thứ, bạn có thể bắt đầu!

## Các bước tùy chọn

### Cài Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) là trình cài nhỏ gọn để cài đặt [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, cùng một vài gói.
Conda tự nó là trình quản lý gói, giúp bạn dễ dàng thiết lập và chuyển đổi giữa các [môi trường ảo](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python và gói. Nó cũng rất hữu dụng để cài những gói không có trên `pip`.

Bạn có thể làm theo [hướng dẫn cài MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst).

Khi đã cài Miniconda, bạn cần clone [repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (nếu chưa).

Tiếp theo, bạn cần tạo môi trường ảo. Để làm điều này với Conda, hãy tạo file môi trường mới (_environment.yml_). Nếu bạn theo học bằng Codespaces, hãy tạo file trong thư mục `.devcontainer`, tức là `.devcontainer/environment.yml`.

Hãy điền vào file môi trường bằng đoạn dưới đây:

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

Nếu bạn gặp lỗi khi dùng conda, bạn có thể cài thủ công thư viện Microsoft AI bằng lệnh sau trong terminal.

```
conda install -c microsoft azure-ai-ml
```

File môi trường chỉ định các phụ thuộc cần thiết. `<environment-name>` là tên bạn muốn dùng cho môi trường Conda, còn `<python-version>` là phiên bản Python bạn muốn dùng, ví dụ `3` là phiên bản lớn mới nhất của Python.

Khi xong, bạn có thể tạo môi trường Conda bằng cách chạy các lệnh dưới đây trong command line/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path chỉ áp dụng cho các thiết lập Codespace
conda activate ai4beg
```

Tham khảo [hướng dẫn môi trường Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) nếu gặp sự cố.

### Dùng Visual Studio Code với tiện ích hỗ trợ Python

Chúng tôi khuyên dùng trình soạn thảo [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) với [tiện ích hỗ trợ Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) được cài để học khóa này. Dù vậy, đây chỉ là khuyến nghị chứ không phải bắt buộc.

> **Lưu ý**: Khi mở repo khóa học trong VS Code, bạn có thể chọn thiết lập dự án trong container. Vì trong repo có thư mục đặc biệt [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). Sẽ giải thích thêm phía sau.

> **Lưu ý**: Khi bạn clone và mở thư mục trong VS Code, nó sẽ tự động gợi ý bạn cài tiện ích hỗ trợ Python.

> **Lưu ý**: Nếu VS Code gợi mở lại repo trong container, hãy từ chối để dùng Python đã cài trên máy cục bộ.

### Dùng Jupyter trong trình duyệt

Bạn cũng có thể làm việc trên dự án bằng [môi trường Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ngay trong trình duyệt. Cả Jupyter cổ điển và [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) đều cung cấp môi trường phát triển dễ chịu với các tính năng như tự động hoàn thành, tô sáng cú pháp...

Để bắt đầu Jupyter local, mở terminal/cmd, chuyển đến thư mục khóa học, và chạy:

```bash
jupyter notebook
```

hoặc

```bash
jupyterhub
```

Lệnh này sẽ khởi động một phiên Jupyter và URL truy cập sẽ được hiển thị trong cửa sổ dòng lệnh.

Sau khi truy cập URL, bạn sẽ thấy đề cương khóa học và có thể điều hướng tới bất kỳ file `*.ipynb` nào, ví dụ, `08-building-search-applications/python/oai-solution.ipynb`.

### Chạy trong container

Một lựa chọn thay thế cho việc thiết lập trên máy tính hoặc Codespace là sử dụng [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Thư mục đặc biệt `.devcontainer` trong repo khóa học cho phép VS Code thiết lập dự án trong container. Ngoài Codespaces, việc này sẽ cần cài Docker và khá phức tạp, nên chỉ khuyên dùng với những người có kinh nghiệm làm việc với container.

Một trong những cách tốt nhất để giữ khóa API an toàn khi dùng GitHub Codespaces là sử dụng Codespace Secrets. Hãy làm theo hướng dẫn [Quản lý bí mật Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) để biết thêm chi tiết.


## Các bài học và Yêu cầu kỹ thuật

Khóa học có 6 bài học khái niệm và 6 bài học lập trình.

Với các bài học lập trình, chúng ta sử dụng Dịch vụ Azure OpenAI. Bạn cần truy cập dịch vụ Azure OpenAI và có khóa API để chạy mã. Bạn có thể đăng ký truy cập bằng cách [hoàn thành ứng dụng này](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Trong khi chờ xử lý đơn đăng ký, mỗi bài học lập trình cũng bao gồm file `README.md` để bạn xem mã và kết quả đầu ra.

## Sử dụng Azure OpenAI Service lần đầu

Nếu đây là lần đầu bạn làm việc với Azure OpenAI service, hãy làm theo hướng dẫn này về cách [tạo và triển khai tài nguyên Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Sử dụng OpenAI API lần đầu

Nếu đây là lần đầu bạn làm việc với OpenAI API, hãy theo dõi hướng dẫn cách [tạo và sử dụng giao diện.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Gặp gỡ các học viên khác

Chúng tôi đã tạo các kênh trong [máy chủ Discord cộng đồng AI chính thức](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) để gặp gỡ các học viên khác. Đây là cách tuyệt vời để kết nối với các doanh nhân, nhà xây dựng, sinh viên cùng chí hướng, và bất kỳ ai muốn nâng cao kỹ năng với Generative AI.

[![Tham gia kênh discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Đội dự án cũng sẽ có mặt trên máy chủ Discord này để hỗ trợ các học viên.

## Đóng góp

Khóa học này là một sáng kiến mã nguồn mở. Nếu bạn thấy có điểm cần cải thiện hoặc lỗi, vui lòng tạo [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) hoặc ghi nhận [vấn đề trên GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Đội dự án sẽ theo dõi mọi đóng góp. Đóng góp vào mã nguồn mở là cách tuyệt vời để phát triển sự nghiệp của bạn trong Generative AI.

Hầu hết các đóng góp yêu cầu bạn đồng ý với Thỏa thuận Giấy phép Người đóng góp (CLA) tuyên bố bạn có quyền và thực sự cấp cho chúng tôi quyền sử dụng đóng góp của bạn. Chi tiết xem tại [CLA, trang web Thỏa thuận Giấy phép Người đóng góp](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Quan trọng: khi dịch văn bản trong repo này, xin hãy chắc chắn không sử dụng dịch máy. Chúng tôi sẽ xác minh bản dịch qua cộng đồng, nên vui lòng chỉ tình nguyện dịch các ngôn ngữ mà bạn thành thạo.

Khi bạn gửi pull request, CLA-bot sẽ tự động xác định xem bạn có cần nộp CLA hay không và sẽ gắn nhãn phù hợp lên PR (ví dụ: nhãn, bình luận). Chỉ cần làm theo hướng dẫn của bot. Bạn chỉ cần làm điều này một lần cho tất cả các repo sử dụng CLA của chúng tôi.


Dự án này đã áp dụng [Bộ Quy tắc Ứng xử Mã nguồn Mở của Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Để biết thêm thông tin, vui lòng đọc phần Câu hỏi thường gặp về Bộ Quy tắc Ứng xử hoặc liên hệ [Email opencode](opencode@microsoft.com) với bất kỳ câu hỏi hoặc phản hồi bổ sung nào.

## Bắt Đầu Nào

Bây giờ bạn đã hoàn thành các bước cần thiết để hoàn thành khóa học này, hãy bắt đầu bằng cách xem [giới thiệu về AI Sinh và LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc sai sót. Tài liệu gốc bằng ngôn ngữ gốc nên được coi là nguồn tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->