<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:13:24+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "vi"
}
-->
# Bắt đầu với khóa học này

Chúng tôi rất hào hứng khi bạn bắt đầu khóa học này và khám phá những gì bạn có thể tạo ra với Generative AI!

Để đảm bảo bạn thành công, trang này sẽ hướng dẫn các bước thiết lập, yêu cầu kỹ thuật và nơi bạn có thể nhận được trợ giúp khi cần.

## Các bước thiết lập

Để bắt đầu khóa học này, bạn cần hoàn thành các bước sau.

### 1. Fork repo này

[Hãy fork toàn bộ repo này](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) vào tài khoản GitHub của bạn để có thể chỉnh sửa mã và hoàn thành các thử thách. Bạn cũng có thể [star (🌟) repo này](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) để dễ dàng tìm lại repo và các repo liên quan.

### 2. Tạo codespace

Để tránh các vấn đề về phụ thuộc khi chạy mã, chúng tôi khuyên bạn nên chạy khóa học này trong [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Bạn có thể tạo codespace bằng cách chọn tùy chọn `Code` trên phiên bản repo đã fork của bạn và chọn **Codespaces**.

![Hộp thoại hiển thị các nút để tạo codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Lưu trữ API Keys của bạn

Việc giữ an toàn và bảo mật các API keys rất quan trọng khi xây dựng bất kỳ ứng dụng nào. Chúng tôi khuyên bạn không nên lưu trực tiếp API keys trong mã nguồn. Việc commit những thông tin này lên repo công khai có thể dẫn đến các vấn đề bảo mật và thậm chí phát sinh chi phí không mong muốn nếu bị kẻ xấu lợi dụng.  
Dưới đây là hướng dẫn từng bước để tạo file `.env` cho Python và thêm `GITHUB_TOKEN`:

1. **Đi đến thư mục dự án của bạn**: Mở terminal hoặc command prompt và điều hướng đến thư mục gốc của dự án nơi bạn muốn tạo file `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Tạo file `.env`**: Sử dụng trình soạn thảo văn bản bạn thích để tạo file mới tên là `.env`. Nếu dùng dòng lệnh, bạn có thể dùng `touch` (trên hệ thống Unix) hoặc `echo` (trên Windows):

   Hệ thống Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Chỉnh sửa file `.env`**: Mở file `.env` trong trình soạn thảo (ví dụ VS Code, Notepad++, hoặc bất kỳ trình soạn thảo nào). Thêm dòng sau vào file, thay `your_github_token_here` bằng token GitHub thực tế của bạn:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Lưu file**: Lưu các thay đổi và đóng trình soạn thảo.

5. **Cài đặt `python-dotenv`**: Nếu bạn chưa cài, bạn cần cài gói `python-dotenv` để tải biến môi trường từ file `.env` vào ứng dụng Python của bạn. Bạn có thể cài bằng `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Tải biến môi trường trong script Python**: Trong script Python, sử dụng gói `python-dotenv` để tải biến môi trường từ file `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Xong rồi! Bạn đã tạo thành công file `.env`, thêm token GitHub và tải nó vào ứng dụng Python của bạn.

## Cách chạy trên máy tính cá nhân

Để chạy mã trên máy tính cá nhân, bạn cần cài đặt một phiên bản [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Sau đó, để sử dụng repo, bạn cần clone nó:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Khi đã có đầy đủ, bạn có thể bắt đầu!

## Các bước tùy chọn

### Cài đặt Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) là trình cài đặt nhẹ để cài đặt [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python và một số gói khác.  
Conda là trình quản lý gói giúp bạn dễ dàng thiết lập và chuyển đổi giữa các [môi trường ảo](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python và các gói. Nó cũng hữu ích khi cài các gói không có trên `pip`.

Bạn có thể theo dõi [hướng dẫn cài đặt MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) để thiết lập.

Sau khi cài Miniconda, bạn cần clone [repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (nếu chưa làm).

Tiếp theo, bạn cần tạo môi trường ảo. Để làm điều này với Conda, hãy tạo file môi trường mới (_environment.yml_). Nếu bạn dùng Codespaces, tạo file này trong thư mục `.devcontainer`, tức là `.devcontainer/environment.yml`.

Hãy điền nội dung cho file môi trường theo đoạn dưới đây:

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

Nếu gặp lỗi khi dùng conda, bạn có thể cài thủ công Microsoft AI Libraries bằng lệnh sau trong terminal.

```
conda install -c microsoft azure-ai-ml
```

File môi trường xác định các phụ thuộc cần thiết. `<environment-name>` là tên bạn muốn đặt cho môi trường Conda, và `<python-version>` là phiên bản Python bạn muốn dùng, ví dụ `3` là phiên bản chính mới nhất của Python.

Sau khi xong, bạn có thể tạo môi trường Conda bằng cách chạy các lệnh dưới đây trong command line/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Tham khảo [hướng dẫn môi trường Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) nếu gặp vấn đề.

### Sử dụng Visual Studio Code với extension hỗ trợ Python

Chúng tôi khuyên bạn dùng trình soạn thảo [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) cùng với [extension hỗ trợ Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) cho khóa học này. Tuy nhiên, đây chỉ là khuyến nghị, không bắt buộc.

> **Lưu ý**: Khi mở repo khóa học trong VS Code, bạn có thể thiết lập dự án trong container. Điều này nhờ thư mục đặc biệt [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) có trong repo. Sẽ nói thêm về điều này sau.

> **Lưu ý**: Khi bạn clone và mở thư mục trong VS Code, nó sẽ tự động gợi ý cài extension hỗ trợ Python.

> **Lưu ý**: Nếu VS Code gợi ý mở lại repo trong container, bạn có thể từ chối để sử dụng phiên bản Python cài đặt trên máy.

### Sử dụng Jupyter trên trình duyệt

Bạn cũng có thể làm việc trên dự án bằng môi trường [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ngay trên trình duyệt. Cả Jupyter cổ điển và [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) đều cung cấp môi trường phát triển thân thiện với các tính năng như tự động hoàn thành, tô sáng mã, v.v.

Để khởi động Jupyter trên máy, mở terminal/command line, điều hướng đến thư mục khóa học và chạy:

```bash
jupyter notebook
```

hoặc

```bash
jupyterhub
```

Lệnh này sẽ khởi động một phiên Jupyter và URL truy cập sẽ hiển thị trong cửa sổ dòng lệnh.

Khi truy cập URL, bạn sẽ thấy đề cương khóa học và có thể mở bất kỳ file `*.ipynb` nào. Ví dụ, `08-building-search-applications/python/oai-solution.ipynb`.

### Chạy trong container

Một lựa chọn khác thay vì thiết lập trên máy hoặc Codespace là dùng [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Thư mục đặc biệt `.devcontainer` trong repo khóa học cho phép VS Code thiết lập dự án trong container. Ngoài Codespaces, bạn sẽ cần cài Docker, và thực sự việc này khá phức tạp, nên chúng tôi chỉ khuyên dùng cho những ai có kinh nghiệm với container.

Một trong những cách tốt nhất để giữ an toàn cho API keys khi dùng GitHub Codespaces là sử dụng Codespace Secrets. Vui lòng theo dõi hướng dẫn [Quản lý secrets trong Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) để tìm hiểu thêm.

## Các bài học và yêu cầu kỹ thuật

Khóa học gồm 6 bài học về khái niệm và 6 bài học lập trình.

Đối với các bài học lập trình, chúng tôi sử dụng Azure OpenAI Service. Bạn cần có quyền truy cập dịch vụ Azure OpenAI và API key để chạy mã. Bạn có thể đăng ký quyền truy cập bằng cách [hoàn thành đơn đăng ký này](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Trong khi chờ xử lý đơn, mỗi bài học lập trình cũng có file `README.md` để bạn xem mã và kết quả.

## Sử dụng Azure OpenAI Service lần đầu

Nếu đây là lần đầu bạn làm việc với Azure OpenAI service, vui lòng theo dõi hướng dẫn về cách [tạo và triển khai tài nguyên Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Sử dụng OpenAI API lần đầu

Nếu đây là lần đầu bạn làm việc với OpenAI API, vui lòng theo dõi hướng dẫn về cách [tạo và sử dụng giao diện.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Gặp gỡ các học viên khác

Chúng tôi đã tạo các kênh trong [server Discord cộng đồng AI chính thức](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) để bạn gặp gỡ các học viên khác. Đây là cách tuyệt vời để kết nối với các doanh nhân, nhà phát triển, sinh viên và bất kỳ ai muốn nâng cao kỹ năng về Generative AI.

[![Tham gia kênh discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Nhóm dự án cũng sẽ có mặt trên server Discord này để hỗ trợ các học viên.

## Đóng góp

Khóa học này là một sáng kiến mã nguồn mở. Nếu bạn thấy điểm cần cải thiện hoặc lỗi, vui lòng tạo [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) hoặc ghi nhận [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Nhóm dự án sẽ theo dõi tất cả các đóng góp. Đóng góp cho mã nguồn mở là cách tuyệt vời để phát triển sự nghiệp trong Generative AI.

Hầu hết các đóng góp yêu cầu bạn đồng ý với Thỏa thuận Cấp phép Đóng góp (Contributor License Agreement - CLA) xác nhận bạn có quyền và thực sự cấp cho chúng tôi quyền sử dụng đóng góp của bạn. Chi tiết xem tại [CLA, trang web Thỏa thuận Cấp phép Đóng góp](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Quan trọng: khi dịch văn bản trong repo này, vui lòng đảm bảo không sử dụng dịch máy. Chúng tôi sẽ xác minh bản dịch qua cộng đồng, nên chỉ nhận dịch những ngôn ngữ mà bạn thành thạo.

Khi bạn gửi pull request, bot CLA sẽ tự động xác định xem bạn có cần cung cấp CLA hay không và đánh dấu PR phù hợp (ví dụ, nhãn, bình luận). Chỉ cần làm theo hướng dẫn của bot. Bạn chỉ cần làm việc này một lần cho tất cả các repo sử dụng CLA của chúng tôi.

Dự án này đã áp dụng [Bộ Quy tắc Ứng xử Mã nguồn mở của Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Để biết thêm thông tin, đọc FAQ về Quy tắc Ứng xử hoặc liên hệ [Email opencode](opencode@microsoft.com) nếu có câu hỏi hoặc góp ý.

## Bắt đầu thôi

Bây giờ bạn đã hoàn thành các bước cần thiết để học khóa này, hãy bắt đầu với [giới thiệu về Generative AI và LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.