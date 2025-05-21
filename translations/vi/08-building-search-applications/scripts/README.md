<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T18:52:50+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "vi"
}
-->
# Chuẩn bị dữ liệu chuyển ngữ

Các script chuẩn bị dữ liệu chuyển ngữ tải xuống bản ghi video YouTube và chuẩn bị chúng để sử dụng với mẫu Tìm kiếm Ngữ nghĩa với OpenAI Embeddings và Functions.

Các script chuẩn bị dữ liệu chuyển ngữ đã được kiểm tra trên các phiên bản mới nhất của Windows 11, macOS Ventura và Ubuntu 22.04 (và cao hơn).

## Tạo các tài nguyên cần thiết cho Azure OpenAI Service

> [!IMPORTANT]
> Chúng tôi khuyên bạn nên cập nhật Azure CLI lên phiên bản mới nhất để đảm bảo tương thích với OpenAI
> Xem [Tài liệu](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Tạo một nhóm tài nguyên

> [!NOTE]
> Trong các hướng dẫn này, chúng tôi sử dụng nhóm tài nguyên có tên "semantic-video-search" ở khu vực Đông Mỹ.
> Bạn có thể thay đổi tên nhóm tài nguyên, nhưng khi thay đổi vị trí cho các tài nguyên, 
> hãy kiểm tra [bảng khả dụng của mô hình](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Tạo một tài nguyên Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Lấy endpoint và các khóa để sử dụng trong ứng dụng này

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Triển khai các mô hình sau:
   - `text-embedding-ada-002` version `2` or greater, named `text-embedding-ada-002`
   - `gpt-35-turbo` version `0613` or greater, named `gpt-35-turbo`

```console
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --scale-settings-scale-type "Standard"
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name gpt-35-turbo \
    --model-name gpt-35-turbo \
    --model-version "0613"  \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## Phần mềm cần thiết

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) hoặc cao hơn

## Biến môi trường

Các biến môi trường sau đây là cần thiết để chạy các script chuẩn bị dữ liệu chuyển ngữ từ YouTube.

### Trên Windows

Khuyên bạn nên thêm các biến vào `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Trên Linux và macOS

Khuyên bạn nên thêm các lệnh xuất sau vào tệp `~/.bashrc` or `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Cài đặt các thư viện Python cần thiết

1. Cài đặt [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) nếu chưa được cài đặt.
1. Từ cửa sổ `Terminal`, clone mẫu vào thư mục repo ưa thích của bạn.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Điều hướng đến thư mục `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Tạo một môi trường ảo Python.

    Trên Windows:

    ```powershell
    python -m venv .venv
    ```

    Trên macOS và Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Kích hoạt môi trường ảo Python.

   Trên Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Trên macOS và Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Cài đặt các thư viện cần thiết.

   Trên Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Trên macOS và Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Chạy các script chuẩn bị dữ liệu chuyển ngữ từ YouTube

### Trên Windows

```powershell
.\transcripts_prepare.ps1
```

### Trên macOS và Linux

```bash
./transcripts_prepare.sh
```

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sự không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin có thẩm quyền. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp của con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.