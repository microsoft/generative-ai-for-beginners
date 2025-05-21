<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T18:53:04+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "id"
}
-->
# Persiapan Data Transkripsi

Skrip persiapan data transkripsi mengunduh transkrip video YouTube dan mempersiapkannya untuk digunakan dengan contoh Pencarian Semantik menggunakan OpenAI Embeddings dan Fungsi.

Skrip persiapan data transkripsi telah diuji pada rilis terbaru Windows 11, macOS Ventura, dan Ubuntu 22.04 (dan di atasnya).

## Membuat sumber daya Azure OpenAI Service yang diperlukan

> [!IMPORTANT]
> Kami menyarankan Anda memperbarui Azure CLI ke versi terbaru untuk memastikan kompatibilitas dengan OpenAI
> Lihat [Dokumentasi](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Buat grup sumber daya

> [!NOTE]
> Untuk instruksi ini kami menggunakan grup sumber daya bernama "semantic-video-search" di East US.
> Anda dapat mengubah nama grup sumber daya, tetapi ketika mengubah lokasi untuk sumber daya,
> periksa [tabel ketersediaan model](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Buat sumber daya Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Dapatkan endpoint dan kunci untuk penggunaan dalam aplikasi ini

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Terapkan model berikut:
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

## Perangkat lunak yang diperlukan

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) atau lebih tinggi

## Variabel lingkungan

Variabel lingkungan berikut diperlukan untuk menjalankan skrip persiapan data transkripsi YouTube.

### Pada Windows

Disarankan menambahkan variabel ke `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Pada Linux dan macOS

Disarankan menambahkan ekspor berikut ke file `~/.bashrc` or `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Instal pustaka Python yang diperlukan

1. Instal [klien git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) jika belum terinstal.
1. Dari jendela `Terminal`, klon contoh ke folder repo pilihan Anda.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Arahkan ke folder `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Buat lingkungan virtual Python.

    Pada Windows:

    ```powershell
    python -m venv .venv
    ```

    Pada macOS dan Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Aktifkan lingkungan virtual Python.

   Pada Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Pada macOS dan Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Instal pustaka yang diperlukan.

   Pada Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Pada macOS dan Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Jalankan skrip persiapan data transkripsi YouTube

### Pada Windows

```powershell
.\transcripts_prepare.ps1
```

### Pada macOS dan Linux

```bash
./transcripts_prepare.sh
```

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi penting, disarankan menggunakan terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.