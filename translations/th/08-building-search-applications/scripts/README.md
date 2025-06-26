<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-06-25T16:55:32+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "th"
}
-->
# การเตรียมข้อมูลการถอดเสียง

สคริปต์เตรียมข้อมูลการถอดเสียงดาวน์โหลดการถอดเสียงวิดีโอจาก YouTube และเตรียมข้อมูลเพื่อใช้กับตัวอย่างการค้นหาความหมายด้วย OpenAI Embeddings และ Functions

สคริปต์เตรียมข้อมูลการถอดเสียงได้รับการทดสอบบน Windows 11, macOS Ventura และ Ubuntu 22.04 (และรุ่นที่สูงกว่า)

## สร้างทรัพยากรที่จำเป็นสำหรับบริการ Azure OpenAI

> [!IMPORTANT]
> เราแนะนำให้คุณอัปเดต Azure CLI เป็นเวอร์ชันล่าสุดเพื่อให้แน่ใจว่าเข้ากันได้กับ OpenAI
> ดู [เอกสารประกอบ](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. สร้างกลุ่มทรัพยากร

> [!NOTE]
> สำหรับคำแนะนำเหล่านี้เราใช้กลุ่มทรัพยากรชื่อ "semantic-video-search" ใน East US
> คุณสามารถเปลี่ยนชื่อกลุ่มทรัพยากรได้ แต่เมื่อเปลี่ยนตำแหน่งของทรัพยากร 
> ตรวจสอบ [ตารางความพร้อมของโมเดล](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)

```console
az group create --name semantic-video-search --location eastus
```

1. สร้างทรัพยากรบริการ Azure OpenAI

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. รับ endpoint และคีย์สำหรับการใช้งานในแอปพลิเคชันนี้

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. ปรับใช้โมเดลต่อไปนี้:
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

## ซอฟต์แวร์ที่จำเป็น

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) หรือสูงกว่า

## ตัวแปรสภาพแวดล้อม

ตัวแปรสภาพแวดล้อมต่อไปนี้จำเป็นสำหรับการรันสคริปต์เตรียมข้อมูลการถอดเสียงจาก YouTube

### บน Windows

แนะนำให้เพิ่มตัวแปรใน `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### บน Linux และ macOS

แนะนำให้เพิ่มการส่งออกต่อไปนี้ในไฟล์ `~/.bashrc` or `~/.zshrc`

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## ติดตั้งไลบรารี Python ที่จำเป็น

1. ติดตั้ง [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) หากยังไม่ได้ติดตั้ง
1. จากหน้าต่าง `Terminal` ให้โคลนตัวอย่างไปยังโฟลเดอร์ repo ที่คุณต้องการ

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. ไปยังโฟลเดอร์ `data_prep`

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. สร้างสภาพแวดล้อมเสมือนของ Python

    บน Windows:

    ```powershell
    python -m venv .venv
    ```

    บน macOS และ Linux:

    ```bash
    python3 -m venv .venv
    ```

1. เปิดใช้งานสภาพแวดล้อมเสมือนของ Python

   บน Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   บน macOS และ Linux:

   ```bash
   source .venv/bin/activate
   ```

1. ติดตั้งไลบรารีที่จำเป็น

   บน Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   บน macOS และ Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## รันสคริปต์เตรียมข้อมูลการถอดเสียงจาก YouTube

### บน Windows

```powershell
.\transcripts_prepare.ps1
```

### บน macOS และ Linux

```bash
./transcripts_prepare.sh
```

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้เกิดความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้