<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T18:47:28+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "mo"
}
-->
# Persiapan data transkripsi

Skrip persiapan data transkripsi mengunduh transkrip video YouTube dan mempersiapkannya untuk digunakan dengan contoh Pencarian Semantik menggunakan OpenAI Embeddings dan Functions.

Skrip persiapan data transkripsi telah diuji pada rilis terbaru Windows 11, macOS Ventura, dan Ubuntu 22.04 (dan di atasnya).

## Buat sumber daya Azure OpenAI Service yang diperlukan

1. Buat grup sumber daya

> Kami menggunakan grup sumber daya bernama "semantic-video-search" di East US untuk instruksi ini. Anda dapat mengubah nama grup sumber daya, tetapi saat mengubah lokasi untuk sumber daya, periksa [tabel ketersediaan model](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Buat sumber daya Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Dapatkan titik akhir dan kunci untuk penggunaan dalam aplikasi ini

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Sebarkan model berikut:
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

### Di Windows

Disarankan untuk menambahkan variabel ke `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Di Linux dan macOS

Disarankan untuk menambahkan ekspor berikut ke file `~/.bashrc` or `~/.zshrc`.

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

1. Navigasi ke folder `data_prep`.

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

1. Instal pustaka yang diperlukan.

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

Sure, here is the text translated to Māori:

---

**Whakakāhoretanga**:  
Kua whakamāoritia tēnei tuhinga mā te ratonga whakamāori AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ahakoa e whai ana mātou ki te tika, me mōhio tonu ka taea e ngā whakamāoritanga aunoa te kawe mai i ngā hapa, i ngā hē rānei. Ko te tuhinga taketake i roto i tōna reo māori me whakaarotia hei puna mana. Mō ngā pārongo hira, e tūtohutia ana kia whakamahia te whakamāori ā-ringa a te tangata. Kāore mātou e whai hāngai mō ngā māramatanga hē, mō ngā whakamaoritanga hē i puta mai i te whakamahinga o tēnei whakamāoritanga.

---