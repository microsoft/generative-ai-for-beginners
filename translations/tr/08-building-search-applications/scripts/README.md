# Transkripsiyon veri hazırlığı

Transkripsiyon veri hazırlık betikleri, YouTube video transkriptlerini indirir ve bunları OpenAI Embeddings ve Functions ile Semantik Arama örneğinde kullanılmak üzere hazırlar.

Transkripsiyon veri hazırlık betikleri, en son sürümler olan Windows 11, macOS Ventura ve Ubuntu 22.04 (ve üzeri) üzerinde test edilmiştir.

## Gerekli Azure OpenAI Hizmeti kaynaklarını oluşturma

> [!IMPORTANT]
> Azure CLI'yi, OpenAI ile uyumluluğu sağlamak için en son sürüme güncellemenizi öneririz
> Bakınız [Dokümantasyon](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Bir kaynak grubu oluşturun

> [!NOTE]
> Bu talimatlarda "semantic-video-search" adlı kaynak grubunu East US bölgesinde kullanıyoruz.
> Kaynak grubunun adını değiştirebilirsiniz, ancak kaynakların konumunu değiştirirken,
> [model kullanılabilirlik tablosunu](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) kontrol edin.

```console
az group create --name semantic-video-search --location eastus
```

1. Bir Azure OpenAI Hizmeti kaynağı oluşturun.

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

1. Aşağıdaki modelleri konuşlandırın:
   - `text-embedding-ada-002` versiyon `2` veya üstü, adı `text-embedding-ada-002`
   - `gpt-4o-mini` adı `gpt-4o-mini`

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
    --deployment-name gpt-4o-mini \
    --model-name gpt-4o-mini \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## Gerekli yazılımlar

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) veya üzeri

## Ortam değişkenleri

YouTube transkripsiyon veri hazırlık betiklerini çalıştırmak için aşağıdaki ortam değişkenleri gereklidir.

### Windows'da

Değişkenleri `kullanıcı` ortam değişkenlerine eklemenizi öneririz.
`Windows Başlat` > `Sistem ortam değişkenlerini düzenle` > `Ortam Değişkenleri` > [KULLANICI] için `Kullanıcı değişkenleri` > `Yeni`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Ortam değişkenlerini PowerShell profilinize ekleyebilirsiniz.

```powershell
$env:AZURE_OPENAI_API_KEY = "<Azure OpenAI Hizmet API anahtarınız>"
$env:AZURE_OPENAI_ENDPOINT = "<Azure OpenAI Hizmet uç noktanız>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<Azure OpenAI Hizmet model dağıtım adınız>"
$env:GOOGLE_DEVELOPER_API_KEY = "<Google geliştirici API anahtarınız>"
``` -->

### Linux ve macOS'ta

Aşağıdaki dışa aktarmaları `~/.bashrc` veya `~/.zshrc` dosyanıza eklemeniz önerilir.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Gerekli Python kütüphanelerini yükleyin

1. [Git istemcisini](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) henüz yüklemediyseniz yükleyin.
1. Bir `Terminal` penceresinden örneği tercih ettiğiniz depo klasörüne klonlayın.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` klasörüne gidin.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Bir Python sanal ortamı oluşturun.

    Windows'da:

    ```powershell
    python -m venv .venv
    ```

    macOS ve Linux'ta:

    ```bash
    python3 -m venv .venv
    ```

1. Python sanal ortamını etkinleştirin.

   Windows'da:

   ```powershell
   .venv\Scripts\activate
   ```

   macOS ve Linux'ta:

   ```bash
   source .venv/bin/activate
   ```

1. Gerekli kütüphaneleri yükleyin.

   Windows'da:

   ```powershell
   pip install -r requirements.txt
   ```

   macOS ve Linux'ta:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube transkripsiyon veri hazırlık betiklerini çalıştırın

### Windows'da

```powershell
.\transcripts_prepare.ps1
```

### macOS ve Linux'ta

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->