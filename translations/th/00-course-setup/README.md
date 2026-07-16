# เริ่มต้นกับคอร์สนี้

เราตื่นเต้นมากที่คุณจะเริ่มคอร์สนี้และดูว่าอะไรที่จะเป็นแรงบันดาลใจให้คุณสร้างสรรค์ด้วย Generative AI!

เพื่อความสำเร็จของคุณ หน้านี้จะอธิบายขั้นตอนการตั้งค่า ข้อกำหนดทางเทคนิค และแหล่งขอความช่วยเหลือหากจำเป็น

## ขั้นตอนการตั้งค่า

ในการเริ่มเรียนคอร์สนี้ คุณจะต้องทำตามขั้นตอนต่อไปนี้ให้ครบถ้วน

### 1. Fork รีโพนี้

[Fork รีโพทั้งหมดนี้](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ไปยังบัญชี GitHub ของคุณเอง เพื่อให้คุณสามารถแก้ไขโค้ดและทำความท้าทายได้ นอกจากนี้คุณยังสามารถ [กดดาว (🌟) ให้รีโพนี้](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) เพื่อค้นหารีโพนี้และรีโพที่เกี่ยวข้องได้ง่ายขึ้น

### 2. สร้าง codespace

เพื่อหลีกเลี่ยงปัญหา dependencies เมื่อรันโค้ด เราแนะนำให้รันคอร์สนี้ใน [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)

ใน fork ของคุณ: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/th/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 เพิ่มความลับ (secret)

1. ⚙️ ไอคอนเฟือง -> Command Palette-> Codespaces : Manage user secret -> Add a new secret
2. ตั้งชื่อ OPENAI_API_KEY, วางคีย์ของคุณ, บันทึก

### 3. ขั้นตอนถัดไปคืออะไร?

| ฉันต้องการ…           | ไปที่…                                                                |
|---------------------|-------------------------------------------------------------------------|
| เริ่มบทเรียนที่ 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| ทำงานออฟไลน์          | [`setup-local.md`](02-setup-local.md)                                   |
| ตั้งค่าผู้ให้บริการ LLM| [`providers.md`](03-providers.md)                                       |
| พบปะผู้เรียนคนอื่น     | [เข้าร่วม Discord ของเรา](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## การแก้ไขปัญหา


| อาการ                                      | วิธีแก้ไข                                                            |
|-------------------------------------------|--------------------------------------------------------------------|
| Container สร้างติดแค่นานกว่า 10 นาที      | **Codespaces ➜ “Rebuild Container”**                               |
| `python: command not found`                 | Terminal ไม่ได้แนบ; คลิก **+** ➜ *bash*                            |
| `401 Unauthorized` จาก OpenAI               | `OPENAI_API_KEY` ผิดหรือหมดอายุ                                    |
| VS Code แสดง “Dev container mounting…”    | รีเฟรชแท็บเบราว์เซอร์—Codespaces อาจหลุดการเชื่อมต่อ             |
| Notebook kernel หายไป                        | เมนู Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**              |

   ระบบ Unix-based:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **แก้ไขไฟล์ `.env`**: เปิดไฟล์ `.env` ในโปรแกรมแก้ไขข้อความ (เช่น VS Code, Notepad++ หรือโปรแกรมอื่นใด) เพิ่มบรรทัดต่อไปนี้ในไฟล์โดยแทนที่ค่าตัวแปรด้วย endpoint และคีย์ของ Microsoft Foundry Models ของคุณ (ดูรายละเอียดได้ที่ [`providers.md`](03-providers.md)):

   > **หมายเหตุ:** GitHub Models (และตัวแปร `GITHUB_TOKEN`) จะถูกเลิกใช้ในปลายเดือนกรกฎาคม 2026 กรุณาใช้ [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) แทน

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **บันทึกไฟล์**: บันทึกการเปลี่ยนแปลงและปิดโปรแกรมแก้ไขข้อความ

5. **ติดตั้ง `python-dotenv`**: หากยังไม่ได้ติดตั้งคุณจะต้องติดตั้งแพ็กเกจ `python-dotenv` เพื่อโหลดตัวแปรแวดล้อมจากไฟล์ `.env` เข้าสู่แอปพลิเคชัน Python ของคุณโดยใช้คำสั่ง `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **โหลดตัวแปรแวดล้อมในสคริปต์ Python ของคุณ**: ในสคริปต์ Python ให้ใช้แพ็กเกจ `python-dotenv` เพื่อโหลดตัวแปรแวดล้อมจากไฟล์ `.env`:

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

เท่านี้เอง! คุณได้สร้างไฟล์ `.env` สำเร็จ เพิ่มข้อมูลรับรอง Microsoft Foundry Models และโหลดเข้าแอปพลิเคชัน Python ของคุณแล้ว

## วิธีรันโค้ดในเครื่องของคุณเอง

ในการรันโค้ดในเครื่องของคุณ คุณจะต้องมี [ติดตั้ง Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) บางเวอร์ชัน

จากนั้นหากต้องการใช้รีโพนี้ คุณต้องโคลนมัน:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

เมื่อคุณดาวน์โหลดทุกอย่างมาเรียบร้อย คุณก็เริ่มได้เลย!

## ขั้นตอนเพิ่มเติม (Optional)

### การติดตั้ง Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) เป็นตัวติดตั้งน้ำหนักเบาสำหรับติดตั้ง [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python และแพ็กเกจบางส่วน
Conda คือเครื่องมือจัดการแพ็กเกจที่ช่วยให้ตั้งค่าและสลับการใช้งานระหว่าง [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ของ Python และแพ็กเกจต่างๆ ได้ง่าย นอกจากนี้ยังช่วยในการติดตั้งแพ็กเกจที่ไม่มีใน `pip`

คุณสามารถทำตาม [คู่มือการติดตั้ง MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) เพื่อทำการติดตั้งได้

หลังจากติดตั้ง Miniconda แล้ว คุณจะต้องโคลน [รีโพ](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (ถ้ายังไม่ได้โคลน)

ต่อไป คุณต้องสร้าง virtual environment โดยใช้ Conda ซึ่งให้สร้างไฟล์ environment ใหม่ ชื่อ (_environment.yml_) หากคุณทำตามใน Codespaces ให้สร้างในโฟลเดอร์ `.devcontainer` เช่น `.devcontainer/environment.yml`

เติมข้อมูลในไฟล์ environment ด้วยโค้ดส่วนนี้:

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

หากคุณพบข้อผิดพลาดในการใช้ conda คุณสามารถติดตั้ง Microsoft AI Libraries ด้วยตัวเองได้โดยใช้คำสั่งในเทอร์มินัลนี้

```
conda install -c microsoft azure-ai-ml
```

ไฟล์ environment ระบุ dependencies ที่จำเป็น `<environment-name>` คือชื่อสำหรับ Conda environment และ `<python-version>` คือเวอร์ชันของ Python ที่ต้องการใช้ เช่น `3` คือเวอร์ชันหลักล่าสุดของ Python

เมื่อเสร็จแล้ว ให้คุณสร้าง Conda environment โดยรันคำสั่งต่อไปนี้ใน command line/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # พาธย่อย .devcontainer ใช้ได้กับการตั้งค่า Codespace เท่านั้น
conda activate ai4beg
```

หากเจอปัญหาใดๆ ให้ดูที่ [คู่มือ Conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)

### การใช้งาน Visual Studio Code กับส่วนเสริม Python support

แนะนำให้ใช้ [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) พร้อมติดตั้ง [ส่วนเสริม Python support](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) สำหรับคอร์สนี้ อย่างไรก็ตาม นี่เป็นเพียงคำแนะนำ ไม่ใช่ข้อบังคับ

> **หมายเหตุ:** เมือเปิดรีโพของคอร์สนี้ใน VS Code คุณสามารถตั้งค่าโปรเจคใน container ได้ เพราะในรีโพมีโฟลเดอร์พิเศษ [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ซึ่งจะกล่าวถึงต่อไป

> **หมายเหตุ:** เมื่อคุณโคลนและเปิดไดเรกทอรีใน VS Code โปรแกรมจะเสนอให้คุณติดตั้งส่วนเสริม Python support โดยอัตโนมัติ

> **หมายเหตุ:** หาก VS Code เสนอให้คุณเปิดรีโพใน container ใหม่ กรุณาปฏิเสธ เพื่อใช้ Python ที่ติดตั้งในเครื่องของคุณแทน

### การใช้งาน Jupyter ในเบราว์เซอร์

คุณยังสามารถพัฒนาโปรเจคนี้โดยใช้ [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst) บนเบราว์เซอร์ได้ ทั้งแบบ Jupyter แบบดั้งเดิมและ [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) มีสภาพแวดล้อมในการพัฒนาที่ดี พร้อมฟีเจอร์เช่น การเติมคำอัตโนมัติ การเน้นโค้ด ฯลฯ

เพื่อเริ่มต้น Jupyter ในเครื่อง ให้ไปที่เทอร์มินัล/คอนโซลคำสั่ง ไปยังโฟลเดอร์คอร์ส และรันคำสั่งนี้:

```bash
jupyter notebook
```

หรือ

```bash
jupyterhub
```

คำสั่งดังกล่าวจะเริ่ม Jupyter instance และแสดง URL สำหรับเข้าถึงในหน้าต่างคอนโซล

เมื่อคุณเข้าถึง URL ดังกล่าว ควรเห็นโครงร่างคอร์สและไปยังไฟล์ `*.ipynb` ใดก็ได้ เช่น `08-building-search-applications/python/oai-solution.ipynb`

### การรันใน container

อีกทางเลือกหนึ่งแทนการตั้งค่าทั้งหมดในเครื่องหรือ Codespace คือใช้ [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) โฟลเดอร์พิเศษ `.devcontainer` ในรีโพนี้ทำให้ VS Code ตั้งค่าโปรเจคใน container ได้ นอก Codespaces จะต้องติดตั้ง Docker และค่อนข้างยุ่งยาก จึงแนะนำสำหรับผู้มีประสบการณ์ใช้งาน container เท่านั้น

วิธีที่ดีที่สุดวิธีหนึ่งในการรักษาคีย์ API ของคุณให้ปลอดภัยเมื่อใช้ GitHub Codespaces คือใช้ Codespace Secrets โปรดติดตาม [คำแนะนำการจัดการ secrets ใน Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) เพื่อเรียนรู้เพิ่มเติม


## บทเรียนและข้อกำหนดทางเทคนิค

คอร์สนี้มีบทเรียน "Learn" ที่อธิบายแนวคิด Generative AI และบทเรียน "Build" ที่ลงมือเขียนโค้ดจริงในทั้ง **Python** และ **TypeScript** เท่าที่เป็นไปได้

สำหรับบทเรียนการเขียนโค้ด เราใช้ Azure OpenAI ใน Microsoft Foundry คุณจะต้องมีการสมัครใช้งาน Azure และคีย์ API การเข้าถึงเปิดให้ใช้โดยไม่ต้องสมัครล่วงหน้า คุณสามารถ [สร้างทรัพยากร Microsoft Foundry และปรับใช้โมเดล](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) เพื่อรับ endpoint และคีย์ของคุณ

ในแต่ละบทเรียนเขียนโค้ดยังมีไฟล์ `README.md` ที่คุณสามารถดูโค้ดและผลลัพธ์โดยไม่ต้องรัน

## การใช้งาน Azure OpenAI Service เป็นครั้งแรก

หากนี่คือครั้งแรกที่คุณใช้ Azure OpenAI Service โปรดทำตามคำแนะนำวิธี [สร้างและปรับใช้ Azure OpenAI Service](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## การใช้งาน OpenAI API เป็นครั้งแรก

หากนี่คือครั้งแรกที่คุณใช้ OpenAI API กรุณาทำตามคำแนะนำวิธี [สร้างและใช้งานอินเตอร์เฟซ](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## พบปะผู้เรียนคนอื่น

เราได้สร้างช่องทางใน [เซิร์ฟเวอร์ Discord ชุมชน AI อย่างเป็นทางการ](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) สำหรับพบปะผู้เรียนคนอื่น นี่เป็นโอกาสที่ดีในการสร้างเครือข่ายกับผู้ประกอบการ ผู้สร้าง นักเรียน และใครก็ตามที่ต้องการพัฒนาทักษะ Generative AI

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

ทีมโปรเจคจะอยู่ใน Discord นี้เพื่อช่วยเหลือผู้เรียนทุกคน

## การร่วมพัฒนา (Contribute)

คอร์สนี้เป็นโครงการโอเพนซอร์ส หากคุณพบจุดที่ควรปรับปรุงหรือปัญหา กรุณาสร้าง [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) หรือล็อก [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)

ทีมโปรเจคจะติดตามการร่วมพัฒนา ท่านการร่วมพัฒนาโอเพนซอร์สเป็นวิธีที่ยอดเยี่ยมในการสร้างเส้นทางอาชีพใน Generative AI

การร่วมพัฒนาส่วนใหญ่จะต้องคุณตกลงกับ Contributor License Agreement (CLA) ซึ่งประกาศว่าคุณมีสิทธิและมอบสิทธิให้เราใช้ผลงานของคุณ สำหรับรายละเอียด กรุณาเยี่ยมชม [เว็บไซต์ CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)

สำคัญ: เมื่อแปลข้อความในรีโพนี้ กรุณาอย่าใช้การแปลโดยเครื่อง เราจะตรวจสอบคำแปลผ่านชุมชน ดังนั้นโปรดอาสาแปลเฉพาะภาษาที่คุณมีความชำนาญเท่านั้น


เมื่อคุณส่งคำขอดึงเข้ารหัส (pull request) ระบบ CLA-bot จะตรวจสอบโดยอัตโนมัติว่าคุณต้องให้ CLA หรือไม่ และตกแต่งคำขอดึงเข้ารหัสนั้นให้เหมาะสม (เช่น แปะป้ายชื่อ แสดงความคิดเห็น) เพียงทำตามคำแนะนำที่บอทให้ คุณจะต้องทำเช่นนี้เพียงครั้งเดียวเท่านั้นสำหรับทุกที่เก็บรหัสที่ใช้ CLA ของเรา

โครงการนี้ได้นำ [ข้อบังคับการปฏิบัติตนสำหรับซอฟต์แวร์โอเพนซอร์สของ Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) มาใช้ สำหรับข้อมูลเพิ่มเติม โปรดอ่านคำถามที่พบบ่อยเกี่ยวกับข้อบังคับการปฏิบัติตน หรือ ติดต่อ [Email opencode](opencode@microsoft.com) หากมีคำถามหรือข้อคิดเห็นเพิ่มเติม

## มาเริ่มกันเลย

ตอนนี้ที่คุณได้ทำขั้นตอนที่จำเป็นสำหรับหลักสูตรนี้เสร็จแล้ว มาเริ่มต้นด้วยการเรียนรู้ [บทนำเกี่ยวกับ Generative AI และ LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) กันเถอะ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->