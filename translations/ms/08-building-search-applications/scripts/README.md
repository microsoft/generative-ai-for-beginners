<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:11:44+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "ms"
}
-->
# Penyediaan data transkripsi

Skrip penyediaan data transkripsi memuat turun transkrip video YouTube dan menyediakan data tersebut untuk digunakan dengan contoh Semantic Search menggunakan OpenAI Embeddings dan Functions.

Skrip penyediaan data transkripsi telah diuji pada versi terkini Windows 11, macOS Ventura dan Ubuntu 22.04 (dan ke atas).

## Cipta sumber Azure OpenAI Service yang diperlukan

> [!IMPORTANT]
> Kami mengesyorkan anda mengemas kini Azure CLI ke versi terkini untuk memastikan keserasian dengan OpenAI
> Lihat [Dokumentasi](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Cipta kumpulan sumber

> [!NOTE]
> Untuk arahan ini, kami menggunakan kumpulan sumber bernama "semantic-video-search" di East US.
> Anda boleh menukar nama kumpulan sumber, tetapi apabila menukar lokasi sumber, 
> semak [jadual ketersediaan model](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Cipta sumber Azure OpenAI Service.

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

1. Lancarkan model berikut:
   - `text-embedding-ada-002` versi `2` atau lebih tinggi, dinamakan `text-embedding-ada-002`
   - `gpt-35-turbo` versi `0613` atau lebih tinggi, dinamakan `gpt-35-turbo`

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

## Perisian yang diperlukan

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) atau lebih tinggi

## Pembolehubah persekitaran

Pembolehubah persekitaran berikut diperlukan untuk menjalankan skrip penyediaan data transkripsi YouTube.

### Pada Windows

Disyorkan untuk menambah pembolehubah ini ke pembolehubah persekitaran `user` anda.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` untuk [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```



### Pada Linux dan macOS

Disyorkan untuk menambah eksport berikut ke dalam fail `~/.bashrc` atau `~/.zshrc` anda.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Pasang perpustakaan Python yang diperlukan

1. Pasang [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) jika belum dipasang.
1. Dari tetingkap `Terminal`, klon contoh ke folder repo pilihan anda.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Pergi ke folder `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Cipta persekitaran maya Python.

    Pada Windows:

    ```powershell
    python -m venv .venv
    ```

    Pada macOS dan Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Aktifkan persekitaran maya Python.

   Pada Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Pada macOS dan Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Pasang perpustakaan yang diperlukan.

   Pada Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Pada macOS dan Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Jalankan skrip penyediaan data transkripsi YouTube

### Pada Windows

```powershell
.\transcripts_prepare.ps1
```

### Pada macOS dan Linux

```bash
./transcripts_prepare.sh
```

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.