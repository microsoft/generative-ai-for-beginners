<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T18:50:13+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "tr"
}
-->
# Transkripsiyon veri hazırlığı

Transkripsiyon veri hazırlık betikleri, YouTube video transkriptlerini indirir ve bunları OpenAI Embeddings ve Functions örneği ile Semantik Arama için kullanıma hazırlar.

Transkripsiyon veri hazırlık betikleri, en son Windows 11, macOS Ventura ve Ubuntu 22.04 (ve üzeri) sürümlerinde test edilmiştir.

## Gerekli Azure OpenAI Hizmet kaynaklarını oluşturun

> [!IMPORTANT]
> OpenAI ile uyumluluğu sağlamak için Azure CLI'yi en son sürüme güncellemenizi öneririz
> [Belgeler](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst) adresine bakın

1. Bir kaynak grubu oluşturun

> [!NOTE]
> Bu talimatlar için Doğu ABD'de "semantic-video-search" adlı kaynak grubunu kullanıyoruz.
> Kaynak grubunun adını değiştirebilirsiniz, ancak kaynakların konumunu değiştirirken 
> [model kullanılabilirlik tablosunu](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) kontrol edin.

```console
az group create --name semantic-video-search --location eastus
```

1. Bir Azure OpenAI Hizmet kaynağı oluşturun.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Bu uygulamada kullanım için uç noktayı ve anahtarları alın

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Aşağıdaki modelleri dağıtın:
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

## Gerekli yazılım

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) veya üzeri

## Ortam değişkenleri

YouTube transkripsiyon veri hazırlık betiklerini çalıştırmak için aşağıdaki ortam değişkenleri gereklidir.

### Windows'ta

Değişkenleri `user` environment variables.
`Windows Başlat` > `Sistem ortam değişkenlerini düzenle` > `Ortam Değişkenleri` > `Kullanıcı değişkenleri` for [USER] > `Yeni` kısmına eklemenizi öneririz.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Linux ve macOS'ta

Aşağıdaki değişkenleri `~/.bashrc` or `~/.zshrc` dosyanıza eklemenizi öneririz.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Gerekli Python kütüphanelerini yükleyin

1. [Git istemcisi](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) yüklü değilse yükleyin.
1. `Terminal` penceresinden, örneği tercih ettiğiniz depo klasörüne klonlayın.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` klasörüne gidin.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Bir Python sanal ortamı oluşturun.

    Windows'ta:

    ```powershell
    python -m venv .venv
    ```

    macOS ve Linux'ta:

    ```bash
    python3 -m venv .venv
    ```

1. Python sanal ortamını etkinleştirin.

   Windows'ta:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS ve Linux'ta:

   ```bash
   source .venv/bin/activate
   ```

1. Gerekli kütüphaneleri yükleyin.

   Windows'ta:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS ve Linux'ta:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube transkripsiyon veri hazırlık betiklerini çalıştırın

### Windows'ta

```powershell
.\transcripts_prepare.ps1
```

### macOS ve Linux'ta

```bash
./transcripts_prepare.sh
```

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlaşılmalar veya yanlış yorumlamalardan sorumlu değiliz.