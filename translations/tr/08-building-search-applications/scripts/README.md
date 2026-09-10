# Transkripsiyon veri hazırlığı

Transkripsiyon veri hazırlığı betikleri, YouTube video transkriptlerini indirir ve Semantic Search with OpenAI Embeddings and Functions örneği ile kullanıma hazırlar.

Transkripsiyon veri hazırlığı betikleri, Windows 11, macOS Ventura ve Ubuntu 22.04 (ve üstü) en son sürümlerinde test edilmiştir.

## Gerekli Azure OpenAI Hizmeti kaynaklarını oluşturma

> [!IMPORTANT]
> Uyumluluğu sağlamak için Azure CLI'yi en son sürüme güncellemenizi öneririz
> Bkz. [Dokümantasyon](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Bir kaynak grubu oluşturun

> [!NOTE]
> Bu talimatlarda, East US'de "semantic-video-search" adlı kaynak grubu kullanılmıştır.
> Kaynak grubunun adını değiştirebilirsiniz, ancak kaynakların konumunu değiştirirken,
> [model uygunluk tablosunu](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) kontrol edin.

```console
az group create --name semantic-video-search --location eastus
```

1. Bir Azure OpenAI Hizmeti kaynağı oluşturun.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Bu uygulamada kullanım için uç nokta ve anahtarları alın

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Aşağıdaki modelleri dağıtın:
   - `text-embedding-ada-002` sürüm `2` veya üzeri, adı `text-embedding-ada-002`
   - `gpt-5-mini` adı `gpt-5-mini`

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
    --deployment-name gpt-5-mini \
    --model-name gpt-5-mini \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## Gerekli yazılım

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) veya üzeri

## Ortam değişkenleri

Aşağıdaki ortam değişkenleri, YouTube transkripsiyon veri hazırlığı betiklerini çalıştırmak için gereklidir.

### Windows'ta

Değişkenleri `kullanıcı` ortam değişkenlerinize eklemenizi öneririz.
`Windows Başlat` > `Sistem ortam değişkenlerini düzenle` > `Ortam Değişkenleri` > [KULLANICI] için `Kullanıcı değişkenleri` > `Yeni`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Ortam değişkenlerini PowerShell profilinize de ekleyebilirsiniz.

```powershell
$env:AZURE_OPENAI_API_KEY = "<Azure OpenAI Hizmeti API anahtarınız>"
$env:AZURE_OPENAI_ENDPOINT = "<Azure OpenAI Hizmeti uç noktanız>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<Azure OpenAI Hizmeti model dağıtım adınız>"
$env:GOOGLE_DEVELOPER_API_KEY = "<Google geliştirici API anahtarınız>"
``` -->

### Linux ve macOS'ta

Aşağıdaki export komutlarını `~/.bashrc` veya `~/.zshrc` dosyanıza eklemenizi öneririz.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Gerekli Python kütüphanelerini yükleyin

1. [git istemcisini](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) yüklü değilse yükleyin.
1. Bir `Terminal` penceresinden, örneği tercih ettiğiniz depo klasörüne klonlayın.

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

## YouTube transkripsiyon veri hazırlığı betiklerini çalıştırın

### Windows'ta

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