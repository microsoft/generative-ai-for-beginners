<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:11:36+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "id"
}
-->
# Persiapan data transkripsi

Skrip persiapan data transkripsi mengunduh transkrip video YouTube dan menyiapkannya untuk digunakan dengan contoh Semantic Search dengan OpenAI Embeddings dan Functions.

Skrip persiapan data transkripsi telah diuji pada rilis terbaru Windows 11, macOS Ventura, dan Ubuntu 22.04 (dan versi lebih baru).

## Membuat sumber daya Azure OpenAI Service yang diperlukan

> [!IMPORTANT]
> Kami menyarankan Anda memperbarui Azure CLI ke versi terbaru untuk memastikan kompatibilitas dengan OpenAI
> Lihat [Dokumentasi](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Buat resource group

> [!NOTE]
> Untuk petunjuk ini kami menggunakan resource group bernama "semantic-video-search" di East US.
> Anda dapat mengubah nama resource group, tetapi saat mengubah lokasi sumber daya, 
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

1. Deploy model berikut:
   - `text-embedding-ada-002` versi `2` atau lebih tinggi, dengan nama `text-embedding-ada-002`
   - `gpt-35-turbo` versi `0613` atau lebih tinggi, dengan nama `gpt-35-turbo`

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

## Perangkat lunak yang dibutuhkan

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) atau versi lebih baru

## Variabel lingkungan

Variabel lingkungan berikut diperlukan untuk menjalankan skrip persiapan data transkripsi YouTube.

### Di Windows

Disarankan menambahkan variabel ke variabel lingkungan `user` Anda.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` untuk [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```



### Di Linux dan macOS

Disarankan menambahkan ekspor berikut ke file `~/.bashrc` atau `~/.zshrc` Anda.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Instalasi pustaka Python yang dibutuhkan

1. Instal [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) jika belum terpasang.
1. Dari jendela `Terminal`, clone contoh ini ke folder repo pilihan Anda.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Masuk ke folder `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Buat virtual environment Python.

    Di Windows:

    ```powershell
    python -m venv .venv
    ```

    Di macOS dan Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Aktifkan virtual environment Python.

   Di Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Di macOS dan Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Instal pustaka yang dibutuhkan.

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

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.