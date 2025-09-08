<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T17:06:51+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "th"
}
-->
# การตั้งค่าบนเครื่อง 🖥️

**ใช้คู่มือนี้ถ้าคุณต้องการรันทุกอย่างบนแล็ปท็อปของตัวเอง**  
คุณมีสองทางเลือก: **(A) Python แบบ native + virtual-env** หรือ **(B) VS Code Dev Container กับ Docker**  
เลือกแบบที่คุณสะดวก—ทั้งสองแบบนำไปสู่บทเรียนเดียวกัน

## 1. สิ่งที่ต้องมี

| เครื่องมือ            | เวอร์ชัน / หมายเหตุ                                                                |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 ขึ้นไป (ดาวน์โหลดที่ <https://python.org>)                                     |
| **Git**            | เวอร์ชันล่าสุด (มากับ Xcode / Git for Windows / ตัวจัดการแพ็กเกจของ Linux)           |
| **VS Code**        | ไม่จำเป็นแต่แนะนำ <https://code.visualstudio.com>                                   |
| **Docker Desktop** | *เฉพาะ* สำหรับตัวเลือก B ติดตั้งฟรี: <https://docs.docker.com/desktop/>             |

> 💡 **Tip** – ตรวจสอบเครื่องมือในเทอร์มินัล:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. ตัวเลือก A – Python แบบ native (เร็วสุด)

### ขั้นตอนที่ 1 โคลน repo นี้

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### ขั้นตอนที่ 2 สร้าง & เปิดใช้งาน virtual environment

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ ตอนนี้ prompt ควรขึ้นต้นด้วย (.venv)—แปลว่าคุณอยู่ใน env แล้ว

### ขั้นตอนที่ 3 ติดตั้ง dependencies

```bash
pip install -r requirements.txt
```

ข้ามไปที่หัวข้อ 3 เรื่อง [API keys](../../../00-course-setup)

## 2. ตัวเลือก B – VS Code Dev Container (Docker)

เราเตรียม repository และคอร์สนี้ด้วย [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) ที่มี Universal runtime รองรับ Python3, .NET, Node.js และ Java การตั้งค่าที่เกี่ยวข้องอยู่ในไฟล์ `devcontainer.json` ในโฟลเดอร์ `.devcontainer/` ที่ root ของ repository นี้

>**ทำไมถึงเลือกแบบนี้?**
>สภาพแวดล้อมเหมือนกับ Codespaces; ไม่มีปัญหา dependency drift

### ขั้นตอนที่ 0 ติดตั้งสิ่งที่ต้องใช้เพิ่ม

Docker Desktop – ตรวจสอบว่า ```docker --version``` ใช้งานได้
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers)

### ขั้นตอนที่ 1 เปิด repo ใน VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code จะตรวจเจอ .devcontainer/ และขึ้น prompt

### ขั้นตอนที่ 2 เปิดใหม่ใน container

คลิก “Reopen in Container” Docker จะ build image (ประมาณ 3 นาทีครั้งแรก)
เมื่อเห็น prompt ในเทอร์มินัล แปลว่าคุณอยู่ใน container แล้ว

## 2. ตัวเลือก C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) เป็นตัวติดตั้งขนาดเล็กสำหรับ [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python และแพ็กเกจบางตัว
Conda เป็นตัวจัดการแพ็กเกจที่ช่วยให้ตั้งค่าและสลับระหว่าง [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) และแพ็กเกจต่าง ๆ ได้ง่าย นอกจากนี้ยังสะดวกสำหรับติดตั้งแพ็กเกจที่ไม่มีใน `pip`

### ขั้นตอนที่ 0 ติดตั้ง Miniconda

ทำตาม [คู่มือการติดตั้ง MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) เพื่อเริ่มต้น

```bash
conda --version
```

### ขั้นตอนที่ 1 สร้าง virtual environment

สร้างไฟล์ environment ใหม่ (*environment.yml*) ถ้าคุณใช้ Codespaces ให้สร้างในโฟลเดอร์ `.devcontainer` เช่น `.devcontainer/environment.yml`

### ขั้นตอนที่ 2 เติมข้อมูลใน environment file

เพิ่มโค้ดด้านล่างลงใน `environment.yml`

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

รันคำสั่งด้านล่างใน command line/terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

ดู [คู่มือ Conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ถ้าพบปัญหา

## 2 ตัวเลือก D – Jupyter / Jupyter Lab แบบคลาสสิก (ในเบราว์เซอร์)

> **เหมาะกับใคร?**  
> สำหรับคนที่ชอบหน้าตา Jupyter แบบเดิม หรืออยากรันโน้ตบุ๊กโดยไม่ใช้ VS Code  

### ขั้นตอนที่ 1 ตรวจสอบว่าติดตั้ง Jupyter แล้ว

เพื่อเริ่ม Jupyter บนเครื่อง ให้เปิด terminal/command line ไปที่โฟลเดอร์คอร์ส แล้วรัน:

```bash
jupyter notebook
```

หรือ

```bash
jupyterhub
```

จะเริ่ม Jupyter และแสดง URL สำหรับเข้าใช้งานในหน้าต่าง command line

เมื่อเข้า URL แล้ว คุณจะเห็นโครงร่างคอร์สและสามารถเข้าไปที่ไฟล์ `*.ipynb` ได้ เช่น `08-building-search-applications/python/oai-solution.ipynb`

## 3. เพิ่ม API Keys ของคุณ

การเก็บ API keys ให้ปลอดภัยเป็นเรื่องสำคัญในการสร้างแอปพลิเคชันทุกประเภท เราแนะนำว่าอย่าเก็บ API keys ไว้ในโค้ดโดยตรง การ commit ข้อมูลเหล่านี้ลง public repository อาจทำให้เกิดปัญหาด้านความปลอดภัยและค่าใช้จ่ายที่ไม่คาดคิดถ้ามีคนไม่หวังดีนำไปใช้
นี่คือวิธีสร้างไฟล์ `.env` สำหรับ Python และเพิ่ม `GITHUB_TOKEN`:

1. **ไปที่โฟลเดอร์โปรเจกต์ของคุณ**: เปิด terminal หรือ command prompt แล้วไปที่ root directory ของโปรเจกต์ที่ต้องการสร้างไฟล์ `.env`

   ```bash
   cd path/to/your/project
   ```

2. **สร้างไฟล์ `.env`**: ใช้ text editor ที่คุณชอบสร้างไฟล์ใหม่ชื่อ `.env` ถ้าใช้ command line สามารถใช้ `touch` (บน Unix-based) หรือ `echo` (บน Windows):

   ระบบ Unix-based:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **แก้ไขไฟล์ `.env`**: เปิดไฟล์ `.env` ใน text editor (เช่น VS Code, Notepad++ หรืออื่น ๆ) เพิ่มบรรทัดนี้ลงไป โดยแทนที่ `your_github_token_here` ด้วย GitHub token ของคุณจริง ๆ

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **บันทึกไฟล์**: เซฟและปิด text editor

5. **ติดตั้ง `python-dotenv`**: ถ้ายังไม่ได้ติดตั้ง ต้องติดตั้งแพ็กเกจ `python-dotenv` เพื่อโหลด environment variables จากไฟล์ `.env` เข้า Python application ใช้ `pip` ติดตั้งได้เลย:

   ```bash
   pip install python-dotenv
   ```

6. **โหลด Environment Variables ใน Python Script**: ในสคริปต์ Python ให้ใช้แพ็กเกจ `python-dotenv` เพื่อโหลด environment variables จากไฟล์ `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

เรียบร้อย! คุณสร้างไฟล์ `.env` เพิ่ม GitHub token และโหลดเข้า Python application แล้ว

🔐 อย่า commit .env—มันถูกใส่ไว้ใน .gitignore แล้ว
คำแนะนำสำหรับผู้ให้บริการแบบเต็มอยู่ใน [`providers.md`](03-providers.md)

## 4. ต่อไปทำอะไรดี?

| ฉันต้องการ…         | ไปที่…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| เริ่มบทเรียนที่ 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| ตั้งค่า LLM Provider | [`providers.md`](03-providers.md)                                       |
| พบเพื่อนร่วมเรียน  | [เข้าร่วม Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. แก้ปัญหาเบื้องต้น

| อาการ                                      | วิธีแก้                                                          |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | เพิ่ม Python ใน PATH หรือเปิด terminal ใหม่หลังติดตั้ง           |
| `pip` ไม่สามารถ build wheels (Windows)   | `pip install --upgrade pip setuptools wheel` แล้วลองใหม่         |
| `ModuleNotFoundError: dotenv`             | รัน `pip install -r requirements.txt` (env ยังไม่ได้ติดตั้ง)     |
| Docker build ล้มเหลว *No space left*     | Docker Desktop ▸ *Settings* ▸ *Resources* → เพิ่มขนาดดิสก์      |
| VS Code เด้งถามให้ reopen ตลอด           | อาจเปิดทั้งสองตัวเลือกพร้อมกัน; เลือกแบบเดียว (venv **หรือ** container)|
| OpenAI 401 / 429 errors                   | ตรวจสอบค่า `OPENAI_API_KEY` / ข้อจำกัด request rate            |
| มีปัญหาใช้ Conda                         | ติดตั้งไลบรารี AI ของ Microsoft ด้วย `conda install -c microsoft azure-ai-ml`|

---

**ข้อจำกัดความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ ขอแนะนำให้ใช้บริการแปลโดยนักแปลมืออาชีพ ทางเราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่เกิดจากการใช้การแปลนี้