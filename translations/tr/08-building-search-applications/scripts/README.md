<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:09:53+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "tr"
}
-->
# Transkripsiyon veri hazırlığı

Transkripsiyon veri hazırlama betikleri, YouTube video transkriptlerini indirir ve bunları OpenAI Embeddings ve Fonksiyonları ile Semantik Arama örneğinde kullanıma hazırlar.

Transkripsiyon veri hazırlama betikleri, Windows 11, macOS Ventura ve Ubuntu 22.04 (ve üzeri) en son sürümlerinde test edilmiştir.

## Gerekli Azure OpenAI Hizmeti kaynaklarını oluşturma

> [!IMPORTANT]
> Uyumluluğu sağlamak için Azure CLI'yi en son sürüme güncellemenizi öneririz
> Detaylar için [Dokümantasyon](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst) sayfasına bakabilirsiniz

1. Bir kaynak grubu oluşturun

> [!NOTE]
> Bu talimatlarda "semantic-video-search" adlı kaynak grubunu East US bölgesinde kullanıyoruz.
> Kaynak grubunun adını değiştirebilirsiniz, ancak kaynakların konumunu değiştirirken
> [model kullanılabilirlik tablosunu](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) kontrol edin.

```console
az group create --name semantic-video-search --location eastus
```

1. Bir Azure OpenAI Hizmeti kaynağı oluşturun.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Bu uygulamada kullanmak üzere uç nokta ve anahtarları alın

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Aşağıdaki modelleri dağıtın:
   - `text-embedding-ada-002` sürüm `2` veya üzeri, adı `text-embedding-ada-002`
   - `gpt-35-turbo` sürüm `0613` veya üzeri, adı `gpt-35-turbo`

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

## Gerekli yazılımlar

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) veya üzeri

## Ortam değişkenleri

YouTube transkripsiyon veri hazırlama betiklerini çalıştırmak için aşağıdaki ortam değişkenleri gereklidir.

### Windows üzerinde

Değişkenleri `user` ortam değişkenlerinize eklemeniz önerilir.  
`Windows Başlat` > `Sistem ortam değişkenlerini düzenle` > `Ortam Değişkenleri` > [USER] için `Kullanıcı değişkenleri` > `Yeni`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Linux ve macOS üzerinde

Aşağıdaki export komutlarını `~/.bashrc` veya `~/.zshrc` dosyanıza eklemeniz önerilir.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Gerekli Python kütüphanelerini yükleme

1. Eğer yüklü değilse [git istemcisini](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) yükleyin.  
1. Bir `Terminal` penceresinden örneği tercih ettiğiniz depo klasörüne klonlayın.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` klasörüne gidin.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Bir Python sanal ortamı oluşturun.

    Windows üzerinde:

    ```powershell
    python -m venv .venv
    ```

    macOS ve Linux üzerinde:

    ```bash
    python3 -m venv .venv
    ```

1. Python sanal ortamını etkinleştirin.

   Windows üzerinde:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS ve Linux üzerinde:

   ```bash
   source .venv/bin/activate
   ```

1. Gerekli kütüphaneleri yükleyin.

   Windows üzerinde:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS ve Linux üzerinde:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube transkripsiyon veri hazırlama betiklerini çalıştırma

### Windows üzerinde

```powershell
.\transcripts_prepare.ps1
```

### macOS ve Linux üzerinde

```bash
./transcripts_prepare.sh
```

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.