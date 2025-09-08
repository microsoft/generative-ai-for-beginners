<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:10:15+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "th"
}
-->
# การเตรียมข้อมูลการถอดเสียง

สคริปต์การเตรียมข้อมูลการถอดเสียงจะดาวน์โหลดคำบรรยายวิดีโอ YouTube และเตรียมข้อมูลเหล่านั้นเพื่อใช้งานร่วมกับตัวอย่าง Semantic Search ด้วย OpenAI Embeddings และ Functions

สคริปต์การเตรียมข้อมูลการถอดเสียงได้รับการทดสอบบน Windows 11, macOS Ventura และ Ubuntu 22.04 (และเวอร์ชันที่ใหม่กว่า)

## สร้างทรัพยากร Azure OpenAI Service ที่จำเป็น

> [!IMPORTANT]
> เราแนะนำให้อัปเดต Azure CLI เป็นเวอร์ชันล่าสุดเพื่อให้แน่ใจว่าสามารถใช้งานร่วมกับ OpenAI ได้อย่างราบรื่น
> ดูรายละเอียดได้ที่ [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. สร้าง resource group

> [!NOTE]
> ในคำแนะนำนี้ เราใช้ resource group ชื่อ "semantic-video-search" ใน East US
> คุณสามารถเปลี่ยนชื่อ resource group ได้ แต่ถ้าจะเปลี่ยนตำแหน่งที่ตั้งของทรัพยากร
> โปรดตรวจสอบที่ [ตารางความพร้อมใช้งานของโมเดล](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)

```console
az group create --name semantic-video-search --location eastus
```

1. สร้างทรัพยากร Azure OpenAI Service

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. ดึง endpoint และ keys เพื่อใช้งานในแอปพลิเคชันนี้

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. ติดตั้งโมเดลต่อไปนี้:
   - `text-embedding-ada-002` เวอร์ชัน `2` ขึ้นไป ชื่อ `text-embedding-ada-002`
   - `gpt-35-turbo` เวอร์ชัน `0613` ขึ้นไป ชื่อ `gpt-35-turbo`

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

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) หรือเวอร์ชันที่ใหม่กว่า

## ตัวแปรสภาพแวดล้อม

ตัวแปรสภาพแวดล้อมต่อไปนี้จำเป็นสำหรับการรันสคริปต์เตรียมข้อมูลการถอดเสียง YouTube

### บน Windows

แนะนำให้เพิ่มตัวแปรเหล่านี้ในตัวแปรสภาพแวดล้อมของ `user`
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` สำหรับ [USER] > `New`

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### บน Linux และ macOS

แนะนำให้เพิ่มคำสั่ง export เหล่านี้ในไฟล์ `~/.bashrc` หรือ `~/.zshrc`

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

1. เข้าไปที่โฟลเดอร์ `data_prep`

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. สร้าง Python virtual environment

    บน Windows:

    ```powershell
    python -m venv .venv
    ```

    บน macOS และ Linux:

    ```bash
    python3 -m venv .venv
    ```

1. เปิดใช้งาน Python virtual environment

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

## รันสคริปต์เตรียมข้อมูลการถอดเสียง YouTube

### บน Windows

```powershell
.\transcripts_prepare.ps1
```

### บน macOS และ Linux

```bash
./transcripts_prepare.sh
```

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้