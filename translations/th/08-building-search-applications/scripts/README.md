# การเตรียมข้อมูลการถอดเสียง

สคริปต์การเตรียมข้อมูลการถอดเสียงจะดาวน์โหลดบทรองรับวิดีโอ YouTube และเตรียมข้อมูลเหล่านั้นเพื่อใช้กับตัวอย่าง Semantic Search ด้วย OpenAI Embeddings และ Functions

สคริปต์การเตรียมข้อมูลการถอดเสียงได้รับการทดสอบบน Windows 11, macOS Ventura และ Ubuntu 22.04 (และสูงกว่า) เวอร์ชันล่าสุดแล้ว

## สร้างทรัพยากร Azure OpenAI Service ที่จำเป็น

> [!IMPORTANT]
> เราแนะนำให้คุณอัปเดต Azure CLI เป็นเวอร์ชันล่าสุดเพื่อให้แน่ใจว่าสามารถทำงานร่วมกับ OpenAI ได้
> ดูที่ [เอกสาร](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. สร้างกลุ่มทรัพยากร

> [!NOTE]
> สำหรับคำแนะนำเหล่านี้ เราใช้กลุ่มทรัพยากรชื่อ "semantic-video-search" ในภาคตะวันออกของสหรัฐอเมริกา
> คุณสามารถเปลี่ยนชื่อกลุ่มทรัพยากรได้ แต่เมื่อเปลี่ยนตำแหน่งสำหรับทรัพยากร,
> ตรวจสอบ [ตารางความพร้อมใช้งานของโมเดล](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)

```console
az group create --name semantic-video-search --location eastus
```

1. สร้างทรัพยากร Azure OpenAI Service

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. รับ endpoint และกุญแจสำหรับใช้งานในแอปพลิเคชันนี้

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. ติดตั้งโมเดลดังต่อไปนี้:
   - `text-embedding-ada-002` เวอร์ชัน `2` ขึ้นไป ชื่อ `text-embedding-ada-002`
   - `gpt-4o-mini` ชื่อ `gpt-4o-mini`

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

## ซอฟต์แวร์ที่จำเป็น

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) หรือสูงกว่า

## ตัวแปรสภาพแวดล้อม

ตัวแปรสภาพแวดล้อมต่อไปนี้จำเป็นสำหรับการรันสคริปต์การเตรียมข้อมูลการถอดเสียง YouTube

### บน Windows

แนะนำให้เพิ่มตัวแปรไปยังตัวแปรสภาพแวดล้อมของ `user` ของคุณ
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` สำหรับ [USER] > `New`

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- คุณสามารถเพิ่มตัวแปรสภาพแวดล้อมลงในโปรไฟล์ PowerShell ของคุณได้

```powershell
$env:AZURE_OPENAI_API_KEY = "<คีย์ API ของ Azure OpenAI Service ของคุณ>"
$env:AZURE_OPENAI_ENDPOINT = "<endpoint ของ Azure OpenAI Service ของคุณ>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<ชื่อโมเดลที่ติดตั้งของ Azure OpenAI Service ของคุณ>"
$env:GOOGLE_DEVELOPER_API_KEY = "<คีย์ API ของ Google developer ของคุณ>"
``` -->

### บน Linux และ macOS

แนะนำให้เพิ่ม exports เหล่านี้ในไฟล์ `~/.bashrc` หรือ `~/.zshrc` ของคุณ

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

1. สร้างสภาพแวดล้อม Python แบบเสมือน

    บน Windows:

    ```powershell
    python -m venv .venv
    ```

    บน macOS และ Linux:

    ```bash
    python3 -m venv .venv
    ```

1. เปิดใช้งานสภาพแวดล้อม Python แบบเสมือน

   บน Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   บน macOS และ Linux:

   ```bash
   source .venv/bin/activate
   ```

1. ติดตั้งไลบรารีที่จำเป็น

   บน windows:

   ```powershell
   pip install -r requirements.txt
   ```

   บน macOS และ Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## รันสคริปต์การเตรียมข้อมูลการถอดเสียง YouTube

### บน windows

```powershell
.\transcripts_prepare.ps1
```

### บน macOS และ Linux

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->