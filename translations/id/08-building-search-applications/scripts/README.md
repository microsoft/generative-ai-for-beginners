# Persiapan data transkripsi

Skrip persiapan data transkripsi mengunduh transkrip video YouTube dan menyiapkannya untuk digunakan dengan contoh Pencarian Semantik dengan OpenAI Embeddings dan Functions.

Skrip persiapan data transkripsi telah diuji pada rilis terbaru Windows 11, macOS Ventura dan Ubuntu 22.04 (dan yang lebih baru).

## Buat sumber daya Azure OpenAI Service yang diperlukan

> [!IMPORTANT]
> Kami menyarankan Anda memperbarui Azure CLI ke versi terbaru untuk memastikan kompatibilitas dengan OpenAI
> Lihat [Dokumentasi](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Buat grup sumber daya

> [!NOTE]
> Untuk petunjuk ini kami menggunakan grup sumber daya bernama "semantic-video-search" di East US.
> Anda dapat mengubah nama grup sumber daya, tetapi saat mengubah lokasi sumber daya,
> periksa [tabel ketersediaan model](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Buat sumber daya Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Dapatkan endpoint dan kunci untuk digunakan dalam aplikasi ini

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Pasang model berikut:
   - `text-embedding-ada-002` versi `2` atau lebih tinggi, bernama `text-embedding-ada-002`
   - `gpt-4o-mini` bernama `gpt-4o-mini`

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

## Perangkat lunak yang diperlukan

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) atau lebih tinggi

## Variabel lingkungan

Variabel lingkungan berikut diperlukan untuk menjalankan skrip persiapan data transkripsi YouTube.

### Di Windows

Disarankan menambahkan variabel ini ke variabel lingkungan `user` Anda.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` untuk [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Anda dapat menambahkan variabel lingkungan ini ke profil PowerShell Anda.

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### Di Linux dan macOS

Disarankan menambahkan ekspor berikut ke dalam file `~/.bashrc` atau `~/.zshrc` Anda.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Instal pustaka Python yang diperlukan

1. Instal [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) jika belum terinstal.
1. Dari jendela `Terminal`, kloning contoh ini ke folder repo yang Anda pilih.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Masuk ke folder `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Buat lingkungan virtual Python.

    Di Windows:

    ```powershell
    python -m venv .venv
    ```

    Di macOS dan Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Aktifkan lingkungan virtual Python.

   Di Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Di macOS dan Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Pasang pustaka yang diperlukan.

   Di Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Di macOS dan Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Jalankan skrip persiapan data transkripsi YouTube

### Di Windows

```powershell
.\transcripts_prepare.ps1
```

### Di macOS dan Linux

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->