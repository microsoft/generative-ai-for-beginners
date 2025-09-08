<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T17:07:31+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "th"
}
-->
# เริ่มต้นกับคอร์สนี้

เราตื่นเต้นมากที่คุณจะได้เริ่มต้นคอร์สนี้ และอยากเห็นว่าคุณจะได้รับแรงบันดาลใจในการสร้างอะไรกับ Generative AI!

เพื่อให้คุณประสบความสำเร็จ หน้านี้จะอธิบายขั้นตอนการตั้งค่า ข้อกำหนดทางเทคนิค และช่องทางขอความช่วยเหลือหากจำเป็น

## ขั้นตอนการตั้งค่า

เพื่อเริ่มเรียนคอร์สนี้ คุณต้องทำตามขั้นตอนต่อไปนี้

### 1. Fork Repo นี้

[Fork repo นี้ทั้งหมด](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ไปยังบัญชี GitHub ของคุณเอง เพื่อให้คุณสามารถแก้ไขโค้ดและทำโจทย์ต่าง ๆ ได้ คุณยังสามารถ [กดดาว (🌟) repo นี้](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) เพื่อกลับมาค้นหา repo นี้และ repo ที่เกี่ยวข้องได้ง่ายขึ้น

### 2. สร้าง codespace

เพื่อหลีกเลี่ยงปัญหา dependency เวลารันโค้ด เราแนะนำให้คุณเรียนคอร์สนี้ใน [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)

ใน repo ที่คุณ fork: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 เพิ่ม secret

1. ⚙️ ไอคอนรูปเฟือง -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret
2. ตั้งชื่อว่า OPENAI_API_KEY, วาง key ของคุณ, กด Save

### 3.  ต่อไปทำอะไรดี?

| ฉันต้องการ…         | ไปที่…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| เริ่มบทเรียนที่ 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| ทำงานแบบออฟไลน์    | [`setup-local.md`](02-setup-local.md)                                   |
| ตั้งค่า LLM Provider | [`providers.md`](providers.md)                                         |
| พบปะผู้เรียนคนอื่น  | [เข้าร่วม Discord ของเรา](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## การแก้ไขปัญหา


| อาการ                                         | วิธีแก้                                                           |
|-----------------------------------------------|-------------------------------------------------------------------|
| Container build ค้าง > 10 นาที                | **Codespaces ➜ “Rebuild Container”**                              |
| `python: command not found`                   | Terminal ไม่ได้แนบ; คลิก **+** ➜ *bash*                           |
| `401 Unauthorized` จาก OpenAI                 | `OPENAI_API_KEY` ผิดหรือหมดอายุ                                   |
| VS Code แสดง “Dev container mounting…”       | รีเฟรชแท็บเบราว์เซอร์—Codespaces บางครั้งหลุดการเชื่อมต่อ        |
| ไม่พบ Notebook kernel                        | เมนู Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**             |

   ระบบ Unix-based:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **แก้ไขไฟล์ `.env`**: เปิดไฟล์ `.env` ใน text editor (เช่น VS Code, Notepad++ หรือ editor อื่น ๆ) เพิ่มบรรทัดต่อไปนี้ลงในไฟล์ โดยแทนที่ `your_github_token_here` ด้วย GitHub token ของคุณจริง ๆ:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **บันทึกไฟล์**: บันทึกการเปลี่ยนแปลงและปิด text editor

5. **ติดตั้ง `python-dotenv`**: หากคุณยังไม่ได้ติดตั้ง คุณต้องติดตั้งแพ็กเกจ `python-dotenv` เพื่อโหลด environment variables จากไฟล์ `.env` เข้าแอป Python ของคุณ สามารถติดตั้งได้ด้วย `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **โหลด Environment Variables ใน Python Script ของคุณ**: ในสคริปต์ Python ของคุณ ให้ใช้แพ็กเกจ `python-dotenv` เพื่อโหลด environment variables จากไฟล์ `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

เรียบร้อย! คุณได้สร้างไฟล์ `.env` เพิ่ม GitHub token ของคุณ และโหลดเข้าแอป Python แล้ว

## วิธีรันโค้ดบนคอมพิวเตอร์ของคุณ

หากต้องการรันโค้ดบนคอมพิวเตอร์ของคุณเอง คุณต้องมี [Python ติดตั้งอยู่](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) บางเวอร์ชัน

จากนั้นเพื่อใช้งาน repository นี้ คุณต้อง clone มันมาก่อน:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

เมื่อคุณมีทุกอย่างพร้อมแล้ว ก็เริ่มต้นได้เลย!

## ขั้นตอนเสริม

### การติดตั้ง Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) เป็นตัวติดตั้งขนาดเล็กสำหรับ [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python และแพ็กเกจบางตัว
Conda เองเป็นตัวจัดการแพ็กเกจ ที่ช่วยให้ตั้งค่าและสลับระหว่าง [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) และแพ็กเกจต่าง ๆ ได้ง่าย นอกจากนี้ยังสะดวกสำหรับติดตั้งแพ็กเกจที่ไม่มีใน `pip`

คุณสามารถดู [คู่มือการติดตั้ง MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) เพื่อเริ่มต้นได้

เมื่อคุณติดตั้ง Miniconda แล้ว ให้ clone [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ถ้ายังไม่ได้ทำ)

ถัดไป คุณต้องสร้าง virtual environment โดยใช้ Conda ให้สร้างไฟล์ environment ใหม่ (_environment.yml_) ถ้าคุณใช้ Codespaces ให้สร้างไฟล์นี้ในโฟลเดอร์ `.devcontainer` เช่น `.devcontainer/environment.yml`

เติมเนื้อหาในไฟล์ environment ด้วยโค้ดตัวอย่างด้านล่างนี้:

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

ถ้าคุณเจอปัญหาในการใช้ conda คุณสามารถติดตั้ง Microsoft AI Libraries ด้วยคำสั่งนี้ใน terminal ได้เอง

```
conda install -c microsoft azure-ai-ml
```

ไฟล์ environment จะระบุ dependencies ที่เราต้องใช้ `<environment-name>` คือชื่อ environment ที่คุณต้องการตั้ง และ `<python-version>` คือเวอร์ชัน Python ที่ต้องการ เช่น `3` คือเวอร์ชันหลักล่าสุดของ Python

เมื่อเสร็จแล้ว ให้สร้าง Conda environment โดยรันคำสั่งด้านล่างใน command line/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

หากเจอปัญหาใด ๆ ดู [คู่มือ Conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)

### ใช้ Visual Studio Code พร้อมส่วนขยาย Python

เราแนะนำให้ใช้ [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) พร้อม [ส่วนขยาย Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) สำหรับคอร์สนี้ แต่ก็เป็นเพียงคำแนะนำ ไม่ใช่ข้อบังคับ

> **Note**: เมื่อเปิด repository คอร์สใน VS Code คุณสามารถตั้งค่าโปรเจกต์ใน container ได้ เพราะมี [โฟลเดอร์ `.devcontainer` พิเศษ](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) อยู่ใน repo นี้ รายละเอียดเพิ่มเติมจะกล่าวถึงภายหลัง

> **Note**: เมื่อคุณ clone และเปิดโฟลเดอร์ใน VS Code ระบบจะแนะนำให้ติดตั้งส่วนขยาย Python อัตโนมัติ

> **Note**: หาก VS Code แนะนำให้เปิด repo ใน container ให้ปฏิเสธ เพื่อใช้ Python ที่ติดตั้งในเครื่องของคุณ

### ใช้ Jupyter ในเบราว์เซอร์

คุณสามารถทำโปรเจกต์นี้ผ่าน [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ในเบราว์เซอร์ได้เลย ทั้ง Jupyter แบบคลาสสิกและ [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ให้ประสบการณ์พัฒนาโค้ดที่ดี เช่น auto-completion, code highlighting ฯลฯ

หากต้องการเริ่ม Jupyter ในเครื่อง ให้เปิด terminal/command line ไปยังโฟลเดอร์คอร์ส แล้วรันคำสั่ง:

```bash
jupyter notebook
```

หรือ

```bash
jupyterhub
```

จะมี Jupyter instance เริ่มทำงาน และแสดง URL สำหรับเข้าใช้งานในหน้าต่าง command line

เมื่อเข้า URL ดังกล่าว คุณจะเห็นโครงสร้างคอร์ส และสามารถเข้าไปยังไฟล์ `*.ipynb` ใดก็ได้ เช่น `08-building-search-applications/python/oai-solution.ipynb`

### รันใน container

อีกทางเลือกหนึ่งนอกจากตั้งค่าทุกอย่างในเครื่องหรือ Codespace คือใช้ [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) โฟลเดอร์ `.devcontainer` พิเศษใน repo นี้ ช่วยให้ VS Code ตั้งค่าโปรเจกต์ใน container ได้ นอก Codespaces คุณต้องติดตั้ง Docker และอาจต้องใช้ความชำนาญ จึงแนะนำสำหรับผู้ที่มีประสบการณ์กับ container เท่านั้น

หนึ่งในวิธีที่ดีที่สุดในการเก็บ API key ให้ปลอดภัยเมื่อใช้ GitHub Codespaces คือใช้ Codespace Secrets โปรดดู [คู่มือการจัดการ Codespaces secrets](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) เพื่อเรียนรู้เพิ่มเติม

## บทเรียนและข้อกำหนดทางเทคนิค

คอร์สนี้มีบทเรียนแนวคิด 6 บท และบทเรียนโค้ด 6 บท

สำหรับบทเรียนโค้ด เราใช้ Azure OpenAI Service คุณต้องมีสิทธิ์เข้าถึง Azure OpenAI service และ API key เพื่อรันโค้ดนี้ คุณสามารถขอสิทธิ์ได้โดย [กรอกแบบฟอร์มนี้](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)

ระหว่างรอการอนุมัติ ในแต่ละบทเรียนโค้ดจะมีไฟล์ `README.md` ให้คุณดูโค้ดและผลลัพธ์ได้

## การใช้ Azure OpenAI Service ครั้งแรก

ถ้านี่เป็นครั้งแรกที่คุณใช้ Azure OpenAI service โปรดดูคู่มือวิธี [สร้างและ deploy Azure OpenAI Service resource](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## การใช้ OpenAI API ครั้งแรก

ถ้านี่เป็นครั้งแรกที่คุณใช้ OpenAI API โปรดดูคู่มือวิธี [สร้างและใช้งาน Interface](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## พบปะผู้เรียนคนอื่น

เราได้สร้างช่องทางใน [AI Community Discord server อย่างเป็นทางการ](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) สำหรับพบปะผู้เรียนคนอื่น ๆ นี่เป็นโอกาสดีในการสร้างเครือข่ายกับผู้ประกอบการ นักพัฒนา นักศึกษา และทุกคนที่อยากพัฒนาทักษะด้าน Generative AI

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

ทีมงานโปรเจกต์จะอยู่ใน Discord server นี้เพื่อช่วยเหลือผู้เรียนด้วย

## มีส่วนร่วม

คอร์สนี้เป็นโครงการ open-source หากคุณเห็นจุดที่ควรปรับปรุงหรือพบปัญหา โปรดสร้าง [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) หรือแจ้ง [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)

ทีมงานจะติดตามทุกการมีส่วนร่วม การร่วมพัฒนา open source เป็นวิธีที่ยอดเยี่ยมในการสร้างเส้นทางอาชีพในสาย Generative AI

การมีส่วนร่วมส่วนใหญ่จะต้องให้คุณยอมรับ Contributor License Agreement (CLA) เพื่อยืนยันว่าคุณมีสิทธิ์และอนุญาตให้เราใช้ผลงานของคุณ รายละเอียดดูที่ [เว็บไซต์ CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)

สำคัญ: เมื่อแปลเนื้อหาใน repo นี้ กรุณาอย่าใช้เครื่องมือแปลภาษา เราจะตรวจสอบการแปลผ่านชุมชน ดังนั้นโปรดอาสาแปลเฉพาะภาษาที่คุณถนัดจริง ๆ

เมื่อคุณส่ง pull request, CLA-bot จะตรวจสอบโดยอัตโนมัติว่าคุณต้องยื่น CLA หรือไม่ และจะติดป้ายกำกับหรือคอมเมนต์ให้ทำตามคำแนะนำของ bot คุณต้องทำขั้นตอนนี้เพียงครั้งเดียวสำหรับทุก repo ที่ใช้ CLA ของเรา

โปรเจกต์นี้ใช้ [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) ดูข้อมูลเพิ่มเติมได้ที่ Code of Conduct FAQ หรืออีเมล [Email opencode](opencode@microsoft.com) หากมีคำถามหรือข้อเสนอแนะ

## มาเริ่มกันเลย!
เมื่อคุณได้ทำตามขั้นตอนที่จำเป็นเพื่อจบคอร์สนี้แล้ว มาเริ่มต้นกันด้วยการทำความรู้จักกับ Generative AI และ LLMs ได้ที่นี่ [แนะนำ Generative AI และ LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)

---

**ข้อจำกัดความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้การแปลถูกต้องที่สุด แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ แนะนำให้ใช้บริการแปลโดยนักแปลมืออาชีพ ทางเราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่เกิดจากการใช้การแปลนี้