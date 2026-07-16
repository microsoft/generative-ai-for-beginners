# การตั้งค่าเครื่องท้องถิ่น 🖥️

**ใช้คู่มือนี้หากคุณต้องการรันทุกอย่างบนแล็ปท็อปของตัวเอง**  
คุณมีสองทางเลือก: **(A) Python เนทีฟ + virtual-env** หรือ **(B) VS Code Dev Container กับ Docker**  
เลือกวิธีที่รู้สึกว่าง่ายกว่า—ทั้งสองวิธีนำไปสู่บทเรียนเดียวกัน  

## 1. ข้อกำหนดเบื้องต้น

| เครื่องมือ            | เวอร์ชัน / หมายเหตุ                                                               |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 ขึ้นไป (ดาวน์โหลดได้ที่ <https://python.org>)                                  |
| **Git**            | เวอร์ชันล่าสุด (มากับ Xcode / Git สำหรับ Windows / ตัวจัดการแพ็กเกจใน Linux)        |
| **VS Code**        | ทางเลือกแต่แนะนำ <https://code.visualstudio.com>                                   |
| **Docker Desktop** | *สำหรับตัวเลือก B เท่านั้น* ติดตั้งฟรี: <https://docs.docker.com/desktop/>         |

> 💡 **เคล็ดลับ** – ตรวจสอบเครื่องมือในเทอร์มินัล:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. ตัวเลือก A – Python เนทีฟ (เร็วที่สุด)

### ขั้นตอนที่ 1 โคลนรีโปนี้

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### ขั้นตอนที่ 2 สร้างและเปิดใช้งาน virtual environment

```bash
python -m venv .venv          # สร้างหนึ่ง
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ ตอนนี้พรอมต์ควรขึ้นชื่อ (.venv)—แสดงว่าคุณอยู่ในสภาพแวดล้อมแล้ว

### ขั้นตอนที่ 3 ติดตั้ง dependencies

```bash
pip install -r requirements.txt
```

ข้ามไปที่ส่วนที่ 3 สำหรับ [API keys](#3-เพิ่ม-api-keys-ของคุณ)

## 2. ตัวเลือก B – VS Code Dev Container (Docker)

เราตั้งค่ารีโพนี้และคอร์สด้วย [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) ที่มี Universal runtime รองรับ Python3, .NET, Node.js และการพัฒนา Java การตั้งค่าที่เกี่ยวข้องถูกกำหนดไว้ในไฟล์ `devcontainer.json` ในโฟลเดอร์ `.devcontainer/` ที่โฟลเดอร์รูทของรีโปนี้

>**ทำไมต้องเลือกวิธีนี้?**
>สภาพแวดล้อมเหมือนกับ Codespaces; ไม่มีปัญหา dependency drift

### ขั้นตอนที่ 0 ติดตั้งสิ่งที่ต้องใช้เพิ่มเติม

Docker Desktop – ยืนยันว่า ```docker --version``` ใช้งานได้
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers)

### ขั้นตอนที่ 1 เปิดรีโปใน VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code จะตรวจสอบ .devcontainer/ และแสดงพรอมต์ขึ้นมา

### ขั้นตอนที่ 2 เปิดใหม่ใน container

คลิก “Reopen in Container” Docker จะสร้างอิมเมจ (ประมาณ 3 นาทีครั้งแรก)
เมื่อพรอมต์เทอร์มินัลปรากฏขึ้น แสดงว่าคุณอยู่ในคอนเทนเนอร์แล้ว

## 2. ตัวเลือก C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) เป็นตัวติดตั้งขนาดเล็กสำหรับติดตั้ง [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python รวมถึงแพ็กเกจบางตัว
Conda เองเป็นตัวจัดการแพ็กเกจที่ทำให้ง่ายต่อการตั้งค่าและสลับระหว่าง [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) กับแพ็กเกจต่าง ๆ นอกจากนี้ยังเหมาะสำหรับติดตั้งแพ็กเกจที่ไม่มีใน `pip`

### ขั้นตอนที่ 0 ติดตั้ง Miniconda

ทำตาม [คู่มือการติดตั้ง MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) เพื่อทำการติดตั้ง

```bash
conda --version
```

### ขั้นตอนที่ 1 สร้าง virtual environment

สร้างไฟล์ environment ใหม่ (*environment.yml*) หากคุณใช้งานผ่าน Codespaces ให้สร้างในไดเรกทอรี `.devcontainer` ซึ่งจะได้เป็น `.devcontainer/environment.yml`

### ขั้นตอนที่ 2 เติมข้อมูลในไฟล์ environment

เพิ่มโค้ดข้างล่างนี้ใน `environment.yml` ของคุณ

```yml
name: <environment-name>
channels:
 - defaults
 - microsoft
dependencies:
- python=<python-version>
- openai
- python-dotenv
- pip
- pip:
    - azure-ai-ml

```

### ขั้นตอนที่ 3 สร้าง Conda environment ของคุณ

รันคำสั่งตามด้านล่างนี้ในคอมมานด์ไลน์/เทอร์มินัลของคุณ

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer โฟลเดอร์ย่อยนี้ใช้กับการตั้งค่า Codespace เท่านั้น
conda activate ai4beg
```

ดูที่ [คู่มือสภาพแวดล้อม Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) หากพบปัญหาใด ๆ

## 2  ตัวเลือก D – Jupyter คลาสสิก / Jupyter Lab (ในบราวเซอร์ของคุณ)

> **เหมาะกับใคร?**  
> คนที่ชอบอินเทอร์เฟซ Jupyter คลาสสิกหรืออยากรันโน้ตบุ๊กโดยไม่ใช้ VS Code  

### ขั้นตอนที่ 1 ตรวจสอบให้แน่ใจว่ามี Jupyter ติดตั้งแล้ว

เพื่อเริ่มใช้ Jupyter ในเครื่อง เปิดเทอร์มินัล/คอมมานด์ไลน์ ไปที่โฟลเดอร์ของคอร์ส แล้วรัน:

```bash
jupyter notebook
```

หรือ

```bash
jupyterhub
```

สิ่งนี้จะเริ่มต้นอินสแตนซ์ Jupyter และ URL สำหรับเข้าถึงจะปรากฏในหน้าคอมมานด์ไลน์

เมื่อคุณเข้าถึง URL นี้ จะเห็นโครงร่างคอร์สและสามารถเข้าไฟล์ `*.ipynb` ใดก็ได้ เช่น `08-building-search-applications/python/oai-solution.ipynb`

## 3. เพิ่ม API Keys ของคุณ

การรักษา API keys ให้ปลอดภัยเป็นสิ่งสำคัญเมื่อพัฒนาแอปพลิเคชันใดๆ เราแนะนำไม่ให้เก็บ API keys ไว้ในโค้ดโดยตรง การคอมมิตข้อมูลเหล่านั้นในรีโปสาธารณะอาจทำให้เกิดปัญหาด้านความปลอดภัยและค่าใช้จ่ายที่ไม่พึงประสงค์หากถูกใช้โดยผู้ไม่หวังดี
นี่คือคำแนะนำทีละขั้นตอนเกี่ยวกับการสร้างไฟล์ `.env` สำหรับ Python และเพิ่มข้อมูลรับรอง Microsoft Foundry Models ของคุณ:

> **หมายเหตุ:** GitHub Models (และตัวแปร `GITHUB_TOKEN`) จะเลิกใช้สิ้นเดือนกรกฎาคม 2026 คู่มือนี้ใช้ [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) แทน หากต้องการทำงานแบบออฟไลน์เต็มตัว ให้ดูที่ [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)

1. **ไปที่ไดเรกทอรีโปรเจกต์ของคุณ**: เปิดเทอร์มินัลหรือพรอมต์คำสั่ง แล้วไปที่โฟลเดอร์หลักของโปรเจกต์ที่คุณต้องการสร้างไฟล์ `.env`

   ```bash
   cd path/to/your/project
   ```

2. **สร้างไฟล์ `.env`**: ใช้แก้ไขข้อความที่คุณชื่นชอบเพื่อสร้างไฟล์ใหม่ชื่อ `.env` หากใช้คอมมานด์ไลน์ สามารถใช้ `touch` (บนระบบ Unix) หรือ `echo` (บน Windows):

   ระบบ Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **แก้ไขไฟล์ `.env`**: เปิดไฟล์ `.env` ในตัวแก้ไขข้อความ (เช่น VS Code, Notepad++ หรือโปรแกรมอื่น ๆ) เพิ่มบรรทัดต่อไปนี้โดยแทนที่ค่าตัวแปรด้วย endpoint โปรเจกต์ Microsoft Foundry และ API key ของคุณจริง ๆ:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **บันทึกไฟล์**: บันทึกการเปลี่ยนแปลงแล้วปิดตัวแก้ไขข้อความ

5. **ติดตั้ง `python-dotenv`**: ถ้ายังไม่ได้ติดตั้ง จำเป็นต้องติดตั้งแพ็กเกจ `python-dotenv` เพื่อโหลดตัวแปรสภาพแวดล้อมจากไฟล์ `.env` เข้าในแอป Python ของคุณ โดยติดตั้งผ่าน `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **โหลดตัวแปรสภาพแวดล้อมในสคริปต์ Python ของคุณ**: ในสคริปต์ Python ใช้แพ็กเกจ `python-dotenv` เพื่อโหลดตัวแปรจากไฟล์ `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # โหลดตัวแปรสภาพแวดล้อมจากไฟล์ .env
   load_dotenv()

   # เข้าถึงตัวแปร Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

เสร็จเรียบร้อย! คุณได้สร้างไฟล์ `.env` เพิ่มข้อมูลรับรอง Microsoft Foundry Models และโหลดเข้าสู่แอป Python ของคุณแล้ว

🔐 อย่าคอมมิตไฟล์ .env—มันถูกเพิ่มไว้ใน .gitignore แล้ว
คำแนะนำอย่างเต็มรูปแบบของผู้ให้บริการดูได้ที่ [`providers.md`](03-providers.md)

## 4. ต่อไปทำอะไรดี?

| ฉันต้องการ…          | ไปที่…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| เริ่มบทเรียนที่ 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| ตั้งค่าผู้ให้บริการ LLM | [`providers.md`](03-providers.md)                                      |
| พบปะผู้เรียนคนอื่น  | [เข้าร่วม Discord ของเรา](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. การแก้ไขปัญหาเบื้องต้น

| อาการ                                   | วิธีแก้ไข                                                         |
|-----------------------------------------|-----------------------------------------------------------------|
| `python not found`                      | เพิ่ม Python ลง PATH หรือเปิดเทอร์มินัลใหม่หลังติดตั้ง          |
| `pip` สร้าง wheels ไม่สำเร็จ (Windows) | รัน `pip install --upgrade pip setuptools wheel` แล้วลองใหม่    |
| `ModuleNotFoundError: dotenv`           | รัน `pip install -r requirements.txt` (ยังไม่ได้ติดตั้ง env)      |
| สร้าง Docker ล้มเหลว *No space left*   | ใน Docker Desktop ▸ *Settings* ▸ *Resources* → เพิ่มขนาดดิสก์   |
| VS Code แสดงพรอมต์ให้เปิดใหม่บ่อย   | อาจเปิดใช้งานทั้งสองตัวเลือกพร้อมกัน; เลือกเพียงอย่างใดอย่างหนึ่ง (venv **หรือ** container)|
| ข้อผิดพลาด OpenAI 401 / 429            | ตรวจสอบค่า `OPENAI_API_KEY` / ขีดจำกัดอัตราการเรียก API        |
| ข้อผิดพลาดในการใช้ Conda               | ติดตั้งไลบรารี AI ของไมโครซอฟท์ด้วย `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->