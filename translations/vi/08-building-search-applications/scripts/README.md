<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:11:27+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "vi"
}
-->
# Chuẩn bị dữ liệu phiên âm

Các script chuẩn bị dữ liệu phiên âm tải xuống bản ghi video YouTube và chuẩn bị chúng để sử dụng với mẫu Semantic Search với OpenAI Embeddings và Functions.

Các script chuẩn bị dữ liệu phiên âm đã được kiểm tra trên các phiên bản mới nhất của Windows 11, macOS Ventura và Ubuntu 22.04 (và các phiên bản mới hơn).

## Tạo các tài nguyên Azure OpenAI Service cần thiết

> [!IMPORTANT]
> Chúng tôi khuyên bạn nên cập nhật Azure CLI lên phiên bản mới nhất để đảm bảo tương thích với OpenAI
> Xem [Tài liệu](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Tạo một nhóm tài nguyên

> [!NOTE]
> Trong hướng dẫn này, chúng tôi sử dụng nhóm tài nguyên có tên "semantic-video-search" ở khu vực East US.
> Bạn có thể thay đổi tên nhóm tài nguyên, nhưng khi thay đổi vị trí cho các tài nguyên,
> hãy kiểm tra [bảng khả dụng mô hình](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Tạo một tài nguyên Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Lấy endpoint và khóa để sử dụng trong ứng dụng này

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Triển khai các mô hình sau:
   - `text-embedding-ada-002` phiên bản `2` trở lên, đặt tên là `text-embedding-ada-002`
   - `gpt-35-turbo` phiên bản `0613` trở lên, đặt tên là `gpt-35-turbo`

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

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) hoặc mới hơn

## Biến môi trường

Các biến môi trường sau đây là bắt buộc để chạy các script chuẩn bị dữ liệu phiên âm YouTube.

### Trên Windows

Khuyến nghị thêm các biến vào biến môi trường `user` của bạn.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` cho [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```



### Trên Linux và macOS

Khuyến nghị thêm các lệnh export sau vào file `~/.bashrc` hoặc `~/.zshrc` của bạn.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Cài đặt các thư viện Python cần thiết

1. Cài đặt [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) nếu bạn chưa có.
1. Từ cửa sổ `Terminal`, clone mẫu về thư mục repo bạn muốn.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Điều hướng đến thư mục `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Tạo môi trường ảo Python.

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

## Chạy các script chuẩn bị dữ liệu phiên âm YouTube

### Trên Windows

```powershell
.\transcripts_prepare.ps1
```

### Trên macOS và Linux

```bash
./transcripts_prepare.sh
```

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.