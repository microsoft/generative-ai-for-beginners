# เริ่มต้นกับหลักสูตรนี้

เราตื่นเต้นมากที่คุณจะเริ่มต้นหลักสูตรนี้และดูว่าอะไรจะเป็นแรงบันดาลใจให้คุณสร้างสรรค์ด้วย Generative AI!

เพื่อให้คุณประสบความสำเร็จ หน้านี้จะสรุปขั้นตอนการตั้งค่า ความต้องการทางเทคนิค และสถานที่สำหรับขอความช่วยเหลือหากจำเป็น

## ขั้นตอนการตั้งค่า

เพื่อเริ่มเรียนหลักสูตรนี้ คุณจะต้องทำตามขั้นตอนดังต่อไปนี้

### 1. Fork รีโพทั้งหมดนี้

[ทำการ Fork รีโพทั้งหมดนี้](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ไปยังบัญชี GitHub ของคุณเองเพื่อให้คุณสามารถแก้ไขโค้ดและทำแบบท้าทายให้เสร็จได้ คุณยังสามารถ [กดดาว (🌟) รีโพนี้](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) เพื่อให้ค้นหารีโพนี้และรีโพที่เกี่ยวข้องได้ง่ายขึ้น

### 2. สร้าง Codespace

เพื่อหลีกเลี่ยงปัญหาการพึ่งพาระบบเมื่อนำโค้ดไปรัน เราแนะนำให้รันหลักสูตรนี้ใน [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)

ในรีโพที่คุณ Fork : **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/th/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 เพิ่มความลับ (secret)

1. ⚙️ ไอคอนเกียร์ -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. ตั้งชื่อ OPENAI_API_KEY, วางรหัส API ของคุณ, กดบันทึก

### 3. ต่อไปต้องทำอะไร?

| ฉันต้องการ…          | ไปที่…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| เริ่มบทเรียนที่ 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| ทำงานแบบออฟไลน์    | [`setup-local.md`](02-setup-local.md)                                   |
| ตั้งค่า LLM provider | [`providers.md`](03-providers.md)                                        |
| พบเพื่อนผู้เรียนอื่น | [เข้าร่วม Discord ของเรา](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## การแก้ไขปัญหา


| อาการ                                   | วิธีแก้                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| การสร้าง container ค้างเกิน 10 นาที       | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | เทอร์มินัลไม่ได้เชื่อมต่อ; คลิก **+** ➜ *bash*                 |
| `401 Unauthorized` จาก OpenAI            | คีย์ `OPENAI_API_KEY` ผิดหรือหมดอายุ                            |
| VS Code แสดงข้อความ “Dev container mounting…” | รีเฟรชแท็บเบราว์เซอร์—บางครั้ง Codespaces ขาดการเชื่อมต่อ      |
| Notebook kernel หายไป                     | เมนู Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   ระบบปฏิบัติการแบบ Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **แก้ไขไฟล์ `.env`**: เปิดไฟล์ `.env` ในโปรแกรมแก้ไขข้อความ (เช่น VS Code, Notepad++ หรือโปรแกรมแก้ไขอื่นใด) เพิ่มบรรทัดต่อไปนี้ในไฟล์ โดยแทนที่ `your_github_token_here` ด้วยโทเค็น GitHub ของคุณจริงๆ:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **บันทึกไฟล์**: บันทึกการเปลี่ยนแปลงและปิดโปรแกรมแก้ไขข้อความ

5. **ติดตั้ง `python-dotenv`**: หากยังไม่ติดตั้ง คุณต้องติดตั้งแพ็กเกจ `python-dotenv` เพื่อโหลด environment variables จากไฟล์ `.env` เข้าสู่แอปพลิเคชัน Python ของคุณ คุณสามารถติดตั้งได้โดยใช้คำสั่ง `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **โหลด environment variables ในสคริปต์ Python ของคุณ**: ในสคริปต์ Python ใช้แพ็กเกจ `python-dotenv` เพื่อโหลด environment variables จากไฟล์ `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # โหลดตัวแปรสภาพแวดล้อมจากไฟล์ .env
   load_dotenv()

   # เข้าถึงตัวแปร GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

เสร็จเรียบร้อย! คุณได้สร้างไฟล์ `.env` เพิ่มโทเค็น GitHub ของคุณ และโหลดมันเข้าสู่แอป Python ได้สำเร็จแล้ว

## วิธีรันโค้ดบนเครื่องของคุณ

เพื่อรันโค้ดบนเครื่องของคุณเอง คุณจะต้องมี [Python ติดตั้งในเครื่อง](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) บางเวอร์ชัน

จากนั้นเพื่อใช้รีโพนี้ คุณต้องโคลนมัน:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

เมื่อทุกอย่างถูกเช็คเอาต์แล้ว คุณก็พร้อมเริ่มต้น!

## ขั้นตอนเสริม

### การติดตั้ง Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) คือโปรแกรมติดตั้งขนาดเล็กเพื่อติดตั้ง [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python และแพ็กเกจบางตัว
Conda เป็นตัวจัดการแพ็กเกจที่ช่วยให้ง่ายต่อการตั้งค่าและสลับใช้งาน [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ของ Python และแพ็กเกจต่างๆ ให้เหมาะสม นอกจากนี้ยังช่วยติดตั้งแพ็กเกจที่ไม่มีใน `pip`

คุณสามารถติดตาม [คู่มือการติดตั้ง MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) เพื่อทำการติดตั้งได้

เมื่อคุณติดตั้ง Miniconda แล้ว คุณต้องโคลน [รีโพ](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (หากยังไม่ได้ทำ)

ต่อไปคุณต้องสร้าง virtual environment โดยใช้ Conda สร้างไฟล์ environment ใหม่ (_environment.yml_) ถ้าใช้งานใน Codespaces ให้สร้างไฟล์นี้ในไดเรกทอรี `.devcontainer` เป็น `.devcontainer/environment.yml`

เพิ่มเนื้อหาในไฟล์ environment ดังต่อไปนี้:

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

ถ้าคุณพบข้อผิดพลาดในการใช้ conda คุณสามารถติดตั้ง Microsoft AI Libraries ด้วยคำสั่งต่อไปนี้ในเทอร์มินัลได้

```
conda install -c microsoft azure-ai-ml
```

ไฟล์ environment จะกำหนด dependencies ที่ต้องใช้ `<environment-name>` คือชื่อ environment ของ Conda ที่คุณต้องการใช้ และ `<python-version>` คือเวอร์ชัน Python เช่น `3` คือเวอร์ชันใหญ่ล่าสุดของ Python

เมื่อเสร็จแล้ว คุณสามารถสร้าง Conda environment ของคุณโดยรันคำสั่งด้านล่างนี้ใน command line/เทอร์มินัล

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # เส้นทางย่อย .devcontainer ใช้ได้กับการตั้งค่า Codespace เท่านั้น
conda activate ai4beg
```

ดูรายละเอียดเพิ่มเติมได้ใน [คู่มือจัดการ Conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) หากเจอปัญหา

### การใช้ Visual Studio Code พร้อมส่วนขยาย Python

เราแนะนำให้ใช้ [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) พร้อมติดตั้ง [ส่วนขยาย Python support](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) สำหรับหลักสูตรนี้ อย่างไรก็ดี นี่เป็นเพียงคำแนะนำ ไม่ใช่ข้อบังคับ

> **หมายเหตุ**: เมื่อคุณเปิดรีโพหลักสูตรนี้ใน VS Code คุณสามารถตั้งค่าโปรเจกต์ภายใน container ได้ เพราะภายในรีโพมีไดเรกทอรีพิเศษ [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ซึ่งจะกล่าวถึงในภายหลัง

> **หมายเหตุ**: เมื่อโคลนและเปิดไดเรกทอรีนี้ใน VS Code โปรแกรมจะเสนอให้คุณติดตั้งส่วนขยาย Python โดยอัตโนมัติ

> **หมายเหตุ**: หาก VS Code เสนอให้เปิดรีโพนี้ใน container ให้ปฏิเสธคำขอนี้หากคุณต้องการใช้ Python ที่ติดตั้งในเครื่องแทน

### ใช้ Jupyter บนเว็บเบราว์เซอร์

คุณยังสามารถทำงานกับโปรเจกต์นี้โดยใช้ [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ผ่านเว็บเบราว์เซอร์ของคุณ Jupyter แบบคลาสสิก และ [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) จะมีสภาพแวดล้อมการพัฒนาที่ดี มีฟีเจอร์เช่น auto-completion, การเน้นไฮไลต์โค้ด ฯลฯ

เพื่อเริ่ม Jupyter บนเครื่อง ให้เปิดเทอร์มินัล/คอมมานด์ไลน์ ไปยังไดเรกทอรีหลักสูตร และรัน:

```bash
jupyter notebook
```

หรือ

```bash
jupyterhub
```

คำสั่งนี้จะเริ่มเซิร์ฟเวอร์ Jupyter และ URL สำหรับเข้าถึงจะปรากฏในหน้าต่างคอมมานด์ไลน์

หลังจากเปิด URL แล้ว คุณจะเห็นโครงร่างหลักสูตรและสามารถเปิดไฟล์ `*.ipynb` ใดๆ ได้ เช่น `08-building-search-applications/python/oai-solution.ipynb`

### รันใน container

อีกทางเลือกหนึ่งนอกจากการตั้งค่าบนเครื่องหรือ Codespace คือการใช้ [container](https://en.wikipedia.org/wiki/Containerization_%28computing%29?WT.mc_id=academic-105485-koreyst) ไดเรกทอรีพิเศษ `.devcontainer` ในรีโพนี้ช่วยให้ VS Code ตั้งโปรเจกต์ใน container ได้

นอกเหนือจาก Codespaces จะต้องติดตั้ง Docker และจริงๆ แล้วอาจซับซ้อน เราจึงแนะนำเฉพาะผู้ที่มีประสบการณ์กับ container เท่านั้น

วิธีที่ดีที่สุดในการเก็บ API keys อย่างปลอดภัยขณะใช้ GitHub Codespaces คือการใช้ Secrets ของ Codespace โปรดดูคู่มือ [การจัดการ Secrets สำหรับ Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) เพื่อเรียนรู้เพิ่มเติม

## บทเรียนและความต้องการทางเทคนิค

หลักสูตรประกอบด้วยบทเรียนแนวคิด 6 บทและบทเรียนเขียนโค้ด 6 บท

สำหรับบทเรียนเขียนโค้ด เราใช้ Azure OpenAI Service คุณจะต้องเข้าถึงบริการ Azure OpenAI และมีคีย์ API เพื่อรันโค้ดนี้ คุณสามารถสมัครเข้าถึงได้โดย [กรอกใบสมัครนี้](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)

ขณะที่รอใบสมัครของคุณได้รับการอนุมัติ ในแต่ละบทเรียนเขียนโค้ดยังมีไฟล์ `README.md` ให้คุณดูโค้ดและผลลัพธ์ล่วงหน้า

## การใช้ Azure OpenAI Service ครั้งแรก

ถ้านี่เป็นครั้งแรกที่คุณใช้บริการ Azure OpenAI โปรดทำตามคำแนะนำนี้ในการ [สร้างและปรับใช้ Azure OpenAI Service resource](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## การใช้ OpenAI API ครั้งแรก

ถ้านี่เป็นครั้งแรกที่คุณใช้ OpenAI API โปรดทำตามคำแนะนำสำหรับ [วิธีสร้างและใช้ Interface](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## พบปะผู้เรียนคนอื่น

เราสร้างช่องทางในเซิร์ฟเวอร์ [AI Community Discord อย่างเป็นทางการ](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) เพื่อให้ผู้เรียนได้พบปะกัน นี่เป็นวิธีที่ดีในการสร้างเครือข่ายกับผู้ประกอบการ นักสร้าง นักศึกษา และทุกคนที่ต้องการพัฒนาฝีมือด้าน Generative AI

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

ทีมโปรเจกต์จะอยู่ใน Discord นี้เพื่อช่วยเหลือผู้เรียน

## การมีส่วนร่วม

หลักสูตรนี้เป็นโครงการโอเพ่นซอร์ส ถ้าคุณเห็นจุดที่ควรปรับปรุงหรือพบปัญหา โปรดสร้าง [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) หรือลงบันทึก [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)

ทีมโปรเจกต์จะติดตามการมีส่วนร่วมทั้งหมด การร่วมพัฒนาซอฟต์แวร์โอเพ่นซอร์สเป็นวิธีที่ยอดเยี่ยมในการสร้างอาชีพในด้าน Generative AI

ส่วนใหญ่การมีส่วนร่วมจะต้องยอมรับ Contributor License Agreement (CLA) ซึ่งระบุว่าคุณมีสิทธิ์อนุญาตให้เราใช้ผลงานของคุณ โปรดดูรายละเอียดที่ [เว็บไซต์ CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)

สำคัญ: เมื่อแปลข้อความในรีโพนี้ โปรดอย่าใช้การแปลโดยเครื่องมืออัตโนมัติ เราจะตรวจสอบความถูกต้องของการแปลผ่านชุมชน ดังนั้นโปรดแปลในภาษาที่คุณมีความชำนาญเท่านั้น

เมื่อคุณส่ง pull request, CLA-bot จะตรวจสอบโดยอัตโนมัติว่าคุณต้องส่ง CLA หรือไม่ และแสดงป้ายหรือข้อความใน PR ให้ปฏิบัติตามคำแนะนำของบอท คุณจะต้องทำเพียงครั้งเดียวสำหรับทุกรีโพที่ใช้ CLA ของเรา

โปรเจกต์นี้นำ [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) มาใช้ อ่านข้อมูลเพิ่มเติมใน FAQ ของ Code of Conduct หรือส่งอีเมลถึง [opencode@microsoft.com](opencode@microsoft.com) หากมีคำถามหรือความคิดเห็นเพิ่มเติม

## มาเริ่มกันเลย!
ตอนนี้คุณได้ทำขั้นตอนที่จำเป็นเพื่อเสร็จสิ้นหลักสูตรนี้แล้ว มาเริ่มต้นกันด้วยการรับ [บทนำสู่ Generative AI และ LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) กันเถอะครับ/ค่ะ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาด้วย AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นฉบับควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้การแปลโดยมืออาชีพที่เป็นมนุษย์ ทางเราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใดๆ ที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->