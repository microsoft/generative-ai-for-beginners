<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:54:10+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "vi"
}
-->
# Bắt đầu với khóa học này

Chúng tôi rất vui mừng khi bạn bắt đầu khóa học này và xem bạn sẽ được truyền cảm hứng để xây dựng gì với AI Sinh Tạo!

Để đảm bảo bạn thành công, trang này phác thảo các bước cài đặt, yêu cầu kỹ thuật và nơi để nhận sự giúp đỡ nếu cần.

## Các bước cài đặt

Để bắt đầu khóa học này, bạn sẽ cần hoàn thành các bước sau.

### 1. Fork kho lưu trữ này

[Fork toàn bộ kho lưu trữ này](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) vào tài khoản GitHub của bạn để có thể thay đổi mã và hoàn thành các thử thách. Bạn cũng có thể [gắn sao (🌟) kho lưu trữ này](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) để dễ dàng tìm thấy nó và các kho lưu trữ liên quan.

### 2. Tạo một mã không gian

Để tránh các vấn đề phụ thuộc khi chạy mã, chúng tôi khuyên bạn nên chạy khóa học này trong [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Điều này có thể được thực hiện bằng cách chọn tùy chọn `Code` trên phiên bản fork của kho lưu trữ này và chọn tùy chọn **Codespaces**.

![Hộp thoại hiển thị các nút để tạo một mã không gian](../../../00-course-setup/images/who-will-pay.webp)

### 3. Lưu trữ khóa API của bạn

Giữ an toàn và bảo mật khóa API của bạn là rất quan trọng khi xây dựng bất kỳ loại ứng dụng nào. Chúng tôi khuyên bạn không nên lưu trữ bất kỳ khóa API nào trực tiếp trong mã của bạn. Đưa các chi tiết đó vào kho lưu trữ công khai có thể dẫn đến các vấn đề bảo mật và thậm chí là chi phí không mong muốn nếu bị kẻ xấu sử dụng. Dưới đây là hướng dẫn từng bước về cách tạo tệp `.env` cho Python và thêm `GITHUB_TOKEN`:

1. **Điều hướng đến thư mục dự án của bạn**: Mở terminal hoặc command prompt và điều hướng đến thư mục gốc của dự án nơi bạn muốn tạo tệp `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Tạo tệp `.env`**: Sử dụng trình soạn thảo văn bản ưa thích của bạn để tạo một tệp mới có tên `.env`. Nếu bạn sử dụng dòng lệnh, bạn có thể sử dụng `touch` (on Unix-based systems) or `echo` (trên Windows):

   Hệ thống dựa trên Unix:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Chỉnh sửa tệp `.env`**: Mở tệp `.env` trong một trình soạn thảo văn bản (ví dụ: VS Code, Notepad++, hoặc bất kỳ trình soạn thảo nào khác). Thêm dòng sau vào tệp, thay thế `your_github_token_here` bằng mã thông báo GitHub thực của bạn:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Lưu tệp**: Lưu các thay đổi và đóng trình soạn thảo văn bản.

5. **Cài đặt gói `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` để tải các biến môi trường từ tệp `.env` vào ứng dụng Python của bạn. Bạn có thể cài đặt nó bằng `pip`:

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

Vậy là xong! Bạn đã tạo thành công tệp `.env`, thêm mã thông báo GitHub của bạn và tải nó vào ứng dụng Python của bạn.

## Cách chạy cục bộ trên máy tính của bạn

Để chạy mã cục bộ trên máy tính của bạn, bạn cần có một số phiên bản [Python đã cài đặt](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Để sử dụng kho lưu trữ, bạn cần clone nó:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Khi bạn đã kiểm tra xong mọi thứ, bạn có thể bắt đầu!

## Các bước tùy chọn

### Cài đặt Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) là một trình cài đặt nhẹ để cài đặt [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, cũng như một số gói. Conda tự nó là một trình quản lý gói, giúp dễ dàng thiết lập và chuyển đổi giữa các [**môi trường ảo**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) và các gói Python khác nhau. Nó cũng rất hữu ích để cài đặt các gói không có sẵn qua `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Tiến hành và điền vào tệp môi trường của bạn với đoạn mã dưới đây:

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

Nếu bạn gặp lỗi khi sử dụng conda, bạn có thể cài đặt thủ công các Thư viện AI của Microsoft bằng cách sử dụng lệnh sau trong terminal.

```
conda install -c microsoft azure-ai-ml
```

Tệp môi trường chỉ định các phụ thuộc mà chúng ta cần. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` là phiên bản chính mới nhất của Python.

Sau khi hoàn thành, bạn có thể tạo môi trường Conda của mình bằng cách chạy các lệnh dưới đây trong dòng lệnh/terminal của bạn

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Tham khảo [hướng dẫn về môi trường Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) nếu bạn gặp phải bất kỳ vấn đề nào.

### Sử dụng Visual Studio Code với phần mở rộng hỗ trợ Python

Chúng tôi khuyến nghị sử dụng trình soạn thảo [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) với phần mở rộng hỗ trợ Python [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) được cài đặt cho khóa học này. Tuy nhiên, đây chỉ là một gợi ý và không phải là yêu cầu bắt buộc.

> **Lưu ý**: Bằng cách mở kho lưu trữ khóa học trong VS Code, bạn có tùy chọn để thiết lập dự án trong một container. Điều này là do [thư mục đặc biệt `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) được tìm thấy trong kho lưu trữ khóa học. Sẽ có thêm thông tin về điều này sau.

> **Lưu ý**: Khi bạn clone và mở thư mục trong VS Code, nó sẽ tự động đề xuất bạn cài đặt phần mở rộng hỗ trợ Python.

> **Lưu ý**: Nếu VS Code đề xuất bạn mở lại kho lưu trữ trong một container, từ chối yêu cầu này để sử dụng phiên bản Python đã cài đặt cục bộ.

### Sử dụng Jupyter trong trình duyệt

Bạn cũng có thể làm việc trên dự án bằng cách sử dụng môi trường [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ngay trong trình duyệt của bạn. Cả Jupyter cổ điển và [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) đều cung cấp một môi trường phát triển khá thú vị với các tính năng như tự động hoàn thành, tô sáng mã, v.v.

Để bắt đầu Jupyter cục bộ, hãy mở terminal/dòng lệnh, điều hướng đến thư mục khóa học và thực thi:

```bash
jupyter notebook
```

hoặc

```bash
jupyterhub
```

Điều này sẽ khởi động một phiên bản Jupyter và URL để truy cập nó sẽ được hiển thị trong cửa sổ dòng lệnh.

Khi bạn truy cập URL, bạn sẽ thấy đề cương khóa học và có thể điều hướng đến bất kỳ tệp `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` nào để xem mã và đầu ra.

## Sử dụng Dịch vụ Azure OpenAI lần đầu tiên

Nếu đây là lần đầu tiên bạn làm việc với dịch vụ Azure OpenAI, vui lòng làm theo hướng dẫn về cách [tạo và triển khai một tài nguyên Dịch vụ Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Sử dụng API OpenAI lần đầu tiên

Nếu đây là lần đầu tiên bạn làm việc với API OpenAI, vui lòng làm theo hướng dẫn về cách [tạo và sử dụng Giao diện.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Gặp gỡ các học viên khác

Chúng tôi đã tạo các kênh trong máy chủ Discord cộng đồng AI chính thức của chúng tôi để gặp gỡ các học viên khác. Đây là một cách tuyệt vời để kết nối với các doanh nhân, nhà xây dựng, sinh viên và bất kỳ ai có cùng chí hướng đang tìm cách nâng cao kỹ năng trong AI Sinh Tạo.

[![Tham gia kênh discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Đội dự án cũng sẽ có mặt trên máy chủ Discord này để giúp đỡ bất kỳ học viên nào.

## Đóng góp

Khóa học này là một sáng kiến mã nguồn mở. Nếu bạn thấy có khu vực cần cải thiện hoặc vấn đề, vui lòng tạo một [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) hoặc ghi lại một [vấn đề GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Đội dự án sẽ theo dõi tất cả các đóng góp. Đóng góp cho mã nguồn mở là một cách tuyệt vời để xây dựng sự nghiệp của bạn trong AI Sinh Tạo.

Hầu hết các đóng góp yêu cầu bạn đồng ý với Thỏa thuận Cấp phép Người đóng góp (CLA) tuyên bố rằng bạn có quyền và thực sự cấp cho chúng tôi quyền sử dụng đóng góp của bạn. Để biết thêm chi tiết, hãy truy cập [trang web CLA, Thỏa thuận Cấp phép Người đóng góp](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Quan trọng: khi dịch văn bản trong kho lưu trữ này, vui lòng đảm bảo rằng bạn không sử dụng dịch máy. Chúng tôi sẽ xác minh các bản dịch thông qua cộng đồng, vì vậy chỉ tình nguyện dịch trong các ngôn ngữ mà bạn thông thạo.

Khi bạn gửi một yêu cầu kéo, một bot CLA sẽ tự động xác định liệu bạn có cần cung cấp một CLA và trang trí PR một cách phù hợp (ví dụ: nhãn, bình luận). Chỉ cần làm theo hướng dẫn do bot cung cấp. Bạn chỉ cần làm điều này một lần cho tất cả các kho lưu trữ sử dụng CLA của chúng tôi.

Dự án này đã áp dụng [Bộ Quy tắc Ứng xử Mã nguồn Mở của Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Để biết thêm thông tin, hãy đọc Câu hỏi thường gặp về Quy tắc Ứng xử hoặc liên hệ [Email opencode](opencode@microsoft.com) với bất kỳ câu hỏi hoặc bình luận bổ sung nào.

## Hãy bắt đầu

Bây giờ bạn đã hoàn thành các bước cần thiết để hoàn thành khóa học này, hãy bắt đầu bằng cách nhận [giới thiệu về AI Sinh Tạo và LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.