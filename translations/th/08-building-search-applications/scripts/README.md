# การเตรียมข้อมูลการถอดความ

สคริปต์การเตรียมข้อมูลการถอดความจะดาวน์โหลดการถอดความวิดีโอ YouTube และเตรียมข้อมูลสำหรับใช้งานกับตัวอย่าง Semantic Search ด้วย OpenAI Embeddings และ Functions

สคริปต์การเตรียมข้อมูลการถอดความได้รับการทดสอบบน Windows 11, macOS Ventura และ Ubuntu 22.04 (และรุ่นล่าสุด) แล้ว

## สร้างทรัพยากรของ Azure OpenAI Service ที่ต้องการ

> [!IMPORTANT]
> เราแนะนำให้คุณอัปเดต Azure CLI เป็นเวอร์ชันล่าสุดเพื่อให้แน่ใจว่ามีความเข้ากันได้กับ OpenAI
> ดูได้ที่ [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. สร้าง resource group

> [!NOTE]
> สำหรับคำแนะนำนี้ เราใช้ resource group ที่ชื่อว่า "semantic-video-search" ใน East US
> คุณสามารถเปลี่ยนชื่อของ resource group ได้ แต่ถ้าเปลี่ยนตำแหน่งที่ตั้งของทรัพยากร,
> โปรดตรวจสอบตาราง [ความพร้อมใช้งานของโมเดล](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)

```console
az group create --name semantic-video-search --location eastus
```

1. สร้าง Azure OpenAI Service resource

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. รับ endpoint และ keys สำหรับใช้งานในแอปพลิเคชันนี้

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. ปล่อยใช้โมเดลต่อไปนี้:
   - `text-embedding-ada-002` เวอร์ชัน `2` หรือสูงกว่า ชื่อ `text-embedding-ada-002`
   - `gpt-5-mini` ชื่อ `gpt-5-mini`

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

## ซอฟต์แวร์ที่ต้องใช้

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) หรือสูงกว่า

## ตัวแปรแวดล้อม (Environment variables)

ตัวแปรแวดล้อมต่อไปนี้จำเป็นสำหรับการรันสคริปต์เตรียมข้อมูลการถอดความจาก YouTube

### บน Windows

แนะนำให้เพิ่มตัวแปรเหล่านี้ในตัวแปรแวดล้อม `user`
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` สำหรับ [USER] > `New`

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- คุณสามารถเพิ่มตัวแปรแวดล้อมลงในโปรไฟล์ PowerShell ของคุณได้

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### บน Linux และ macOS

แนะนำให้เพิ่มการส่งออกตัวแปรดังต่อไปนี้ในไฟล์ `~/.bashrc` หรือ `~/.zshrc` ของคุณ

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

1. ไปที่โฟลเดอร์ `data_prep`

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

## รันสคริปต์เตรียมข้อมูลการถอดความจาก YouTube

### บน Windows

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