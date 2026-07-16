# เริ่มต้นกับหลักสูตรนี้

เราตื่นเต้นมากที่คุณจะเริ่มหลักสูตรนี้และดูสิ่งที่คุณได้รับแรงบันดาลใจให้สร้างด้วย Generative AI!

เพื่อให้แน่ใจในความสำเร็จของคุณ หน้านี้จะสรุปขั้นตอนการตั้งค่า ความต้องการทางเทคนิค และแหล่งที่ขอความช่วยเหลือหากจำเป็น

## ขั้นตอนการตั้งค่า

ในการเริ่มเรียนหลักสูตรนี้ คุณจะต้องทำขั้นตอนดังต่อไปนี้ให้สมบูรณ์

### 1. ฟอร์ก (Fork) รีโพนี้

[ฟอร์กรีโพทั้งหมดนี้](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ไปยังบัญชี GitHub ของคุณเองเพื่อให้คุณสามารถเปลี่ยนแปลงโค้ดและทำความท้าทายได้ คุณยังสามารถ [กดดาว (🌟) รีโพนี้](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) เพื่อให้ง่ายต่อการค้นหารีโพนี้และรีโพที่เกี่ยวข้อง

### 2. สร้าง Codespace

เพื่อหลีกเลี่ยงปัญหาเกี่ยวกับการพึ่งพาเมื่อรันโค้ด เราแนะนำให้รันหลักสูตรนี้ใน [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)

ในฟอร์กของคุณ: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/th/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 เพิ่มความลับ (Secret)

1. ⚙️ ไอคอนรูปเฟือง -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret
2. ตั้งชื่อว่า OPENAI_API_KEY, วางคีย์ของคุณ, บันทึก

### 3. ขั้นตอนถัดไปคืออะไร?

| ฉันต้องการ...        | ไปที่...                                                            |
|---------------------|--------------------------------------------------------------------|
| เริ่มบทเรียนที่ 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md) |
| ทำงานแบบออฟไลน์     | [`setup-local.md`](02-setup-local.md)                              |
| ตั้งค่าผู้ให้บริการ LLM | [`providers.md`](03-providers.md)                                  |
| พบปะผู้เรียนคนอื่น   | [เข้าร่วม Discord ของเรา](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## การแก้ไขปัญหา


| อาการ                                   | วิธีแก้ไข                                                       |
|-----------------------------------------|----------------------------------------------------------------|
| การสร้าง Container ค้างนานกว่า 10 นาที | **Codespaces ➜ “Rebuild Container”**                           |
| `python: command not found`             | เทอร์มินัลไม่เชื่อมต่อ; คลิก **+** ➜ *bash*                    |
| `401 Unauthorized` จาก OpenAI           | `OPENAI_API_KEY` ผิดหรือหมดอายุ                                 |
| VS Code แสดง “Dev container mounting…” | รีเฟรชแท็บเบราว์เซอร์—บางครั้ง Codespaces สูญเสียการเชื่อมต่อ   |
| ไม่มี Kernel ของ Notebook               | เมนู Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   ระบบยูนิกส์ (Unix-based):

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **แก้ไขไฟล์ `.env`**: เปิดไฟล์ `.env` ในโปรแกรมแก้ไขข้อความ เช่น VS Code, Notepad++ หรือโปรแกรมแก้ไขอื่น ๆ เพิ่มบรรทัดต่อไปนี้โดยแทนที่ตัวแทนด้วยค่า endpoint และคีย์ Microsoft Foundry Models ที่แท้จริงของคุณ (ดูที่ [`providers.md`](03-providers.md) สำหรับวิธีการรับ):

   > **หมายเหตุ:** GitHub Models (และตัวแปร `GITHUB_TOKEN`) จะเลิกใช้ในสิ้นเดือนกรกฎาคม 2026 กรุณาใช้ [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) แทน

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **บันทึกไฟล์**: บันทึกการเปลี่ยนแปลงและปิดโปรแกรมแก้ไขข้อความ

5. **ติดตั้ง `python-dotenv`**: หากคุณยังไม่ได้ติดตั้ง คุณจะต้องติดตั้งแพ็กเกจ `python-dotenv` เพื่อโหลดตัวแปรสภาพแวดล้อมจากไฟล์ `.env` เข้าสู่แอปพลิเคชัน Python ของคุณ คุณสามารถติดตั้งโดยใช้ `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **โหลดตัวแปรสภาพแวดล้อมในสคริปต์ Python ของคุณ**: ในสคริปต์ Python ของคุณ ใช้แพ็กเกจ `python-dotenv` เพื่อโหลดตัวแปรสภาพแวดล้อมจากไฟล์ `.env`:

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

เสร็จเรียบร้อย! คุณได้สร้างไฟล์ `.env` เพิ่มข้อมูลรับรอง Microsoft Foundry Models และโหลดเข้าสู่แอปพลิเคชัน Python ของคุณเรียบร้อยแล้ว

## วิธีรันโค้ดบนเครื่องของคุณ

ในการรันโค้ดบนเครื่องของคุณ คุณจะต้องติดตั้ง [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) เวอร์ชันใดเวอร์ชันหนึ่ง

จากนั้นในการใช้รีโพนี้ คุณต้องโคลนรีโพ:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

เมื่อคุณเตรียมทุกอย่างเสร็จแล้ว คุณก็สามารถเริ่มต้นได้เลย!

## ขั้นตอนเสริม

### การติดตั้ง Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) เป็นตัวติดตั้งน้ำหนักเบาสำหรับติดตั้ง [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python รวมถึงแพ็กเกจบางตัวด้วย
Conda เองเป็นตัวจัดการแพ็กเกจที่ช่วยให้ง่ายต่อการตั้งค่าและสลับระหว่าง [สภาพแวดล้อมเสมือน (virtual environments)](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) และแพ็กเกจต่าง ๆ นอกจากนี้ยังเป็นประโยชน์สำหรับการติดตั้งแพ็กเกจที่ไม่มีใน `pip`

คุณสามารถทำตาม [คู่มือการติดตั้ง MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) เพื่อทำการตั้งค่า

หลังจากติดตั้ง Miniconda แล้ว คุณต้องโคลน [รีโพ](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ถ้ายังไม่ได้โคลน)

ต่อไปคุณต้องสร้างสภาพแวดล้อมเสมือน ด้วย Conda ให้สร้างไฟล์สภาพแวดล้อมใหม่ (_environment.yml_) หากคุณกำลังใช้ Codespaces ให้สร้างในไดเรกทอรี `.devcontainer` คือ `.devcontainer/environment.yml`

ให้กรอกข้อมูลในไฟล์สภาพแวดล้อมด้วยโค้ดตัวอย่างด้านล่างนี้

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

หากคุณพบข้อผิดพลาดในการใช้ conda คุณสามารถติดตั้ง Microsoft AI Libraries ด้วยตนเองโดยใช้คำสั่งต่อไปนี้ในเทอร์มินัล

```
conda install -c microsoft azure-ai-ml
```

ไฟล์นี้ระบุ dependencies ที่เราต้องการ `<environment-name>` หมายถึงชื่อที่คุณต้องการใช้สำหรับสภาพแวดล้อม Conda ของคุณ และ `<python-version>` คือเวอร์ชัน Python ที่ต้องการใช้ เช่น `3` คือเวอร์ชันหลักล่าสุดของ Python

หลังจากนั้นคุณสามารถสร้างสภาพแวดล้อม Conda ของคุณได้โดยรันคำสั่งด้านล่างนี้ใน command line/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer เส้นทางย่อยใช้กับการตั้งค่า Codespace เท่านั้น
conda activate ai4beg
```

ดูคู่มือ [Conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) หากเจอปัญหาใด ๆ

### การใช้ Visual Studio Code พร้อมส่วนขยายสนับสนุน Python

เราแนะนำให้ใช้โปรแกรมแก้ไข [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) พร้อมติดตั้ง [ส่วนขยายสนับสนุน Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) สำหรับหลักสูตรนี้ อย่างไรก็ตาม นี่เป็นเพียงคำแนะนำ ไม่ใช่ข้อบังคับ

> **หมายเหตุ**: การเปิดรีโพหลักสูตรใน VS Code คุณมีทางเลือกตั้งโปรเจกต์ใน container เนื่องจากมีไดเรกทอรีพิเศษ [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) อยู่ในรีโพหลักสูตร จะเล่าละเอียดเพิ่มเติมในภายหลัง

> **หมายเหตุ**: เมื่อคุณโคลนและเปิดโฟลเดอร์ใน VS Code โปรแกรมจะแนะนำให้ติดตั้งส่วนขยายสนับสนุน Python อัตโนมัติ

> **หมายเหตุ**: หาก VS Code แนะนำให้คุณเปิดรีโพใน container ใหม่ ให้ปฏิเสธคำขอนี้เพื่อใช้ Python ที่ติดตั้งบนเครื่อง

### การใช้ Jupyter ในเบราว์เซอร์

คุณยังสามารถทำงานบนโปรเจกต์โดยใช้ [สภาพแวดล้อม Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ภายในเบราว์เซอร์ของคุณได้ ทั้ง Jupyter แบบคลาสสิกและ [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ให้สภาพแวดล้อมการพัฒนาที่ดีพร้อมฟีเจอร์อย่างการเติมคำอัตโนมัติ การเน้นโค้ด ฯลฯ

เพื่อเริ่ม Jupyter บนเครื่อง ให้ไปยังเทอร์มินัล/คอมมานด์ไลน์ เข้าไปยังไดเรกทอรีหลักสูตร และรัน:

```bash
jupyter notebook
```

หรือ

```bash
jupyterhub
```

จะเป็นการเริ่มอินสแตนซ์ Jupyter และแสดง URL เพื่อเข้าถึงในหน้าต่างคอมมานด์ไลน์

เมื่อคุณเข้าถึง URL แล้ว คุณควรเห็นโครงร่างหลักสูตรและสามารถนำทางไปยังไฟล์ `*.ipynb` ได้ เช่น `08-building-search-applications/python/oai-solution.ipynb`

### การรันใน container

อีกทางเลือกแทนการตั้งค่าบนเครื่องของคุณหรือ Codespace คือการใช้ [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) โฟลเดอร์พิเศษ `.devcontainer` ในรีโพหลักสูตรช่วยให้ VS Code ตั้งโปรเจกต์ใน container ได้ หากไม่ใช่ Codespaces จะต้องติดตั้ง Docker และต้องใช้ความรู้เรื่อง container พอสมควร เราจึงแนะนำสำหรับผู้มีประสบการณ์เท่านั้น

วิธีที่ดีที่สุดในการเก็บ API keys ของคุณให้ปลอดภัยเมื่อใช้ GitHub Codespaces คือการใช้ Codespace Secrets โปรดดูคู่มือ [การจัดการความลับใน Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) เพื่อเรียนรู้เพิ่มเติม


## บทเรียนและความต้องการทางเทคนิค

หลักสูตรมีทั้งหมด 6 บทเรียนทฤษฎีและ 6 บทเรียนเขียนโค้ด

ในบทเรียนเขียนโค้ด เราใช้ Azure OpenAI Service คุณจะต้องเข้าถึงบริการ Azure OpenAI และมีคีย์ API เพื่อรันโค้ดนี้ คุณสามารถสมัครขอรับสิทธิ์เข้าถึงได้โดย [กรอกใบสมัครนี้](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)

ในระหว่างรอการอนุมัติใบสมัคร บทเรียนเขียนโค้ดแต่ละบทมีไฟล์ `README.md` ให้ดูโค้ดและผลลัพธ์ได้

## วิธีใช้ Azure OpenAI Service เป็นครั้งแรก

หากนี่เป็นครั้งแรกที่คุณทำงานกับ Azure OpenAI service โปรดทำตามคู่มือนี้เกี่ยวกับวิธี [สร้างและเปิดใช้งานทรัพยากร Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## วิธีใช้ OpenAI API เป็นครั้งแรก

หากนี่เป็นครั้งแรกที่คุณทำงานกับ OpenAI API โปรดทำตามคู่มือเกี่ยวกับวิธี [สร้างและใช้งานอินเทอร์เฟซ](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## พบปะผู้เรียนคนอื่น

เราได้สร้างช่องทางใน [เซิร์ฟเวอร์ Discord ชุมชน AI อย่างเป็นทางการของเรา](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) เพื่อให้ผู้เรียนได้พบปะกัน นี่เป็นวิธีที่ดีในการสร้างเครือข่ายกับผู้ประกอบการ ผู้สร้าง นักเรียน และผู้ที่ต้องการพัฒนาทักษะใน Generative AI

[![เข้าร่วมช่อง Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

ทีมโปรเจกต์จะอยู่ใน Discord นี้เพื่อช่วยเหลือผู้เรียนทุกคนด้วย

## การมีส่วนร่วม

หลักสูตรนี้เป็นความริเริ่มแบบโอเพ่นซอร์ส หากคุณเห็นพื้นที่ที่ควรปรับปรุงหรือพบปัญหา โปรดสร้าง [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) หรือแจ้ง [ปัญหาใน GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)

ทีมโปรเจกต์จะติดตามดูแลทุกการมีส่วนร่วม การมีส่วนร่วมในโอเพ่นซอร์สเป็นวิธีที่ยอดเยี่ยมในการสร้างอาชีพด้าน Generative AI

การมีส่วนร่วมส่วนใหญ่ต้องการให้คุณยอมรับ Contributor License Agreement (CLA) ที่ประกาศว่าคุณมีสิทธิ์และให้สิทธิ์เราใช้ผลงานของคุณ สำหรับรายละเอียด โปรดเยี่ยมชม [เว็บไซต์ CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)

หมายเหตุสำคัญ: เมื่อแปลข้อความในรีโพนี้ กรุณาอย่าใช้การแปลด้วยเครื่อง เราจะตรวจสอบการแปลผ่านชุมชน ดังนั้นโปรดอาสาแปลเฉพาะในภาษาที่คุณชำนาญเท่านั้น

เมื่อคุณส่ง pull request ระบบ CLA-bot จะตรวจสอบให้ว่าคุณจำเป็นต้องจัดเตรียม CLA หรือไม่ และติดป้ายหรือแสดงความคิดเห็นใน PR ตามที่เหมาะสม (เช่น ป้าย, ความคิดเห็น) โปรดปฏิบัติตามคำแนะนำของบอท คุณจะต้องทำเพียงครั้งเดียวในทุกรีโพที่ใช้ CLA นี้


โครงการนี้ได้นำ [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) มาใช้ สำหรับข้อมูลเพิ่มเติมโปรดอ่านคำถามที่พบบ่อยเกี่ยวกับหลักปฏิบัติ หรือ ติดต่อที่ [Email opencode](opencode@microsoft.com) หากมีคำถามหรือข้อคิดเห็นเพิ่มเติม

## มาเริ่มต้นกันเถอะ

ตอนนี้คุณได้ทำตามขั้นตอนที่จำเป็นเพื่อจบหลักสูตรนี้แล้ว เรามาเริ่มต้นด้วยการดู [บทนำเกี่ยวกับ Generative AI และ LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) กัน

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->