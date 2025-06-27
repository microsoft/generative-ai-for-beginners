<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:49:56+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "th"
}
-->
# เริ่มต้นกับคอร์สนี้

เราตื่นเต้นมากที่คุณจะได้เริ่มต้นคอร์สนี้และดูว่าคุณจะได้รับแรงบันดาลใจในการสร้างอะไรกับ Generative AI!

เพื่อให้คุณประสบความสำเร็จ หน้านี้จะอธิบายขั้นตอนการตั้งค่า ข้อกำหนดทางเทคนิค และที่ที่จะขอความช่วยเหลือหากจำเป็น

## ขั้นตอนการตั้งค่า

เพื่อเริ่มต้นคอร์สนี้ คุณจะต้องทำตามขั้นตอนต่อไปนี้

### 1. Fork Repo นี้

[Fork repo ทั้งหมดนี้](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ไปยังบัญชี GitHub ของคุณเองเพื่อให้สามารถเปลี่ยนแปลงโค้ดและทำภารกิจให้เสร็จสิ้นได้ คุณยังสามารถ [star (🌟) repo นี้](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) เพื่อหามันและ repo ที่เกี่ยวข้องได้ง่ายขึ้น

### 2. สร้าง codespace

เพื่อหลีกเลี่ยงปัญหาการพึ่งพาเมื่อรันโค้ด เราแนะนำให้รันคอร์สนี้ใน [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)

สามารถสร้างได้โดยเลือกตัวเลือก `Code` ในเวอร์ชัน forked ของ repo นี้และเลือกตัวเลือก **Codespaces**

![ไดอะล็อกแสดงปุ่มเพื่อสร้าง codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. การเก็บรักษา API Keys ของคุณ

การรักษา API keys ของคุณให้ปลอดภัยและมั่นคงเป็นสิ่งสำคัญเมื่อสร้างแอปพลิเคชันประเภทใดก็ตาม เราแนะนำไม่ให้เก็บ API keys ไว้ในโค้ดของคุณโดยตรง การ commit รายละเอียดเหล่านั้นไปยัง public repository อาจส่งผลให้เกิดปัญหาด้านความปลอดภัยและค่าใช้จ่ายที่ไม่ต้องการหากถูกใช้โดยผู้ไม่หวังดี
นี่คือคำแนะนำทีละขั้นตอนเกี่ยวกับวิธีการสร้างไฟล์ `.env` สำหรับ Python และเพิ่ม `GITHUB_TOKEN`:

1. **ไปยังไดเรกทอรีโปรเจ็กต์ของคุณ**: เปิด terminal หรือ command prompt และไปยังไดเรกทอรีรากของโปรเจ็กต์ที่คุณต้องการสร้างไฟล์ `.env`

   ```bash
   cd path/to/your/project
   ```

2. **สร้างไฟล์ `.env`**: ใช้ text editor ที่คุณชื่นชอบเพื่อสร้างไฟล์ใหม่ชื่อ `.env` หากคุณใช้ command line คุณสามารถใช้ `touch` (on Unix-based systems) or `echo` (บน Windows):

   ระบบ Unix:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **แก้ไขไฟล์ `.env`**: เปิดไฟล์ `.env` ใน text editor (เช่น VS Code, Notepad++ หรือ editor อื่น ๆ) เพิ่มบรรทัดต่อไปนี้ในไฟล์ โดยแทนที่ `your_github_token_here` ด้วย GitHub token ของคุณ:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **บันทึกไฟล์**: บันทึกการเปลี่ยนแปลงและปิด text editor

5. **ติดตั้งแพ็กเกจ `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` เพื่อโหลดตัวแปรสภาพแวดล้อมจากไฟล์ `.env` เข้าไปในแอปพลิเคชัน Python ของคุณ คุณสามารถติดตั้งได้โดยใช้ `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **โหลดตัวแปรสภาพแวดล้อมในสคริปต์ Python ของคุณ**: ในสคริปต์ Python ของคุณ ใช้แพ็กเกจ `python-dotenv` เพื่อโหลดตัวแปรสภาพแวดล้อมจากไฟล์ `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

แค่นั้นแหละ! คุณได้สร้างไฟล์ `.env` เพิ่ม GitHub token ของคุณ และโหลดมันเข้าไปในแอปพลิเคชัน Python ของคุณเรียบร้อยแล้ว

## วิธีรันบนคอมพิวเตอร์ของคุณ

เพื่อรันโค้ดบนคอมพิวเตอร์ของคุณ คุณจะต้องมี [Python ติดตั้งไว้](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) บางเวอร์ชัน

จากนั้นเพื่อใช้ repository คุณต้อง clone มัน:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

เมื่อคุณมีทุกอย่างพร้อมแล้ว คุณก็สามารถเริ่มต้นได้!

## ขั้นตอนเสริม

### การติดตั้ง Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) เป็นตัวติดตั้งน้ำหนักเบาสำหรับติดตั้ง [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst) Python รวมถึงแพ็กเกจบางอย่าง
Conda เองเป็นตัวจัดการแพ็กเกจที่ทำให้การตั้งค่าและสลับระหว่าง [**สภาพแวดล้อมเสมือนของ Python**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) และแพ็กเกจต่าง ๆ ง่ายขึ้น มันยังมีประโยชน์สำหรับการติดตั้งแพ็กเกจที่ไม่สามารถใช้ได้ผ่าน `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`

ไปข้างหน้าและเพิ่มไฟล์สภาพแวดล้อมของคุณด้วย snippet ด้านล่าง:

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

หากคุณพบข้อผิดพลาดในการใช้ conda คุณสามารถติดตั้ง Microsoft AI Libraries ด้วยตนเองโดยใช้คำสั่งต่อไปนี้ใน terminal

```
conda install -c microsoft azure-ai-ml
```

ไฟล์สภาพแวดล้อมระบุการพึ่งพาที่เราต้องการ `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` คือเวอร์ชันหลักล่าสุดของ Python

เมื่อเสร็จแล้ว คุณสามารถสร้างสภาพแวดล้อม Conda ของคุณได้โดยรันคำสั่งด้านล่างใน command line/terminal ของคุณ

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

อ้างอิงถึง [คู่มือสภาพแวดล้อม Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) หากคุณพบปัญหาใด ๆ

### การใช้ Visual Studio Code กับส่วนขยายสนับสนุน Python

เราแนะนำให้ใช้ [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor พร้อมกับ [ส่วนขยายสนับสนุน Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ที่ติดตั้งไว้สำหรับคอร์สนี้ อย่างไรก็ตาม นี่เป็นเพียงคำแนะนำไม่ใช่ข้อกำหนดที่แน่นอน

> **หมายเหตุ**: โดยการเปิด repository คอร์สใน VS Code คุณมีตัวเลือกในการตั้งค่าโปรเจ็กต์ภายใน container นี่เป็นเพราะ [ไดเรกทอรีพิเศษ `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ที่พบภายใน repository ของคอร์ส จะมีข้อมูลเพิ่มเติมในภายหลัง

> **หมายเหตุ**: เมื่อคุณ clone และเปิดไดเรกทอรีใน VS Code มันจะเสนอให้คุณติดตั้งส่วนขยายสนับสนุน Python โดยอัตโนมัติ

> **หมายเหตุ**: หาก VS Code เสนอให้คุณเปิด repository ใน container ใหม่ ให้ปฏิเสธคำขอนี้เพื่อใช้เวอร์ชัน Python ที่ติดตั้งในเครื่อง

### การใช้ Jupyter ในเบราว์เซอร์

คุณยังสามารถทำงานในโปรเจ็กต์โดยใช้ [สภาพแวดล้อม Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ในเบราว์เซอร์ของคุณได้ทั้ง Jupyter แบบคลาสสิกและ [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) ให้สภาพแวดล้อมการพัฒนาที่น่าพอใจพร้อมคุณสมบัติเช่น การเติมคำอัตโนมัติ การไฮไลต์โค้ด เป็นต้น

เพื่อเริ่ม Jupyter ในเครื่อง ไปที่ terminal/command line ไปยังไดเรกทอรีคอร์สและรัน:

```bash
jupyter notebook
```

หรือ

```bash
jupyterhub
```

นี่จะเริ่มต้นอินสแตนซ์ Jupyter และ URL เพื่อเข้าถึงจะถูกแสดงในหน้าต่าง command line

เมื่อคุณเข้าถึง URL คุณควรเห็นโครงร่างคอร์สและสามารถไปยังไฟล์ `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` ใด ๆ ที่คุณสามารถดูโค้ดและผลลัพธ์ได้

## การใช้บริการ Azure OpenAI เป็นครั้งแรก

หากนี่เป็นครั้งแรกที่คุณทำงานกับบริการ Azure OpenAI โปรดทำตามคำแนะนำเกี่ยวกับวิธีการ [สร้างและปรับใช้ทรัพยากรบริการ Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## การใช้ OpenAI API เป็นครั้งแรก

หากนี่เป็นครั้งแรกที่คุณทำงานกับ OpenAI API โปรดทำตามคำแนะนำเกี่ยวกับวิธีการ [สร้างและใช้ Interface](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## พบปะผู้เรียนคนอื่น ๆ

เราได้สร้างช่องทางในเซิร์ฟเวอร์ Discord ชุมชน AI อย่างเป็นทางการของเราเพื่อพบปะกับผู้เรียนคนอื่น ๆ นี่เป็นวิธีที่ดีในการสร้างเครือข่ายกับผู้ประกอบการที่มีความคิดเดียวกัน ผู้สร้าง นักศึกษา และใครก็ตามที่ต้องการพัฒนาทักษะใน Generative AI

[![เข้าร่วมช่องทาง discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

ทีมงานโปรเจ็กต์จะอยู่ในเซิร์ฟเวอร์ Discord นี้ด้วยเพื่อช่วยผู้เรียน

## การมีส่วนร่วม

คอร์สนี้เป็นโครงการโอเพนซอร์ส หากคุณเห็นพื้นที่ที่ต้องการการปรับปรุงหรือปัญหา โปรดสร้าง [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) หรือบันทึก [ปัญหา GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)

ทีมงานโปรเจ็กต์จะติดตามการมีส่วนร่วมทั้งหมด การมีส่วนร่วมในโอเพนซอร์สเป็นวิธีที่น่าทึ่งในการสร้างอาชีพของคุณใน Generative AI

การมีส่วนร่วมส่วนใหญ่ต้องการให้คุณยอมรับข้อตกลงใบอนุญาตผู้มีส่วนร่วม (CLA) โดยประกาศว่าคุณมีสิทธิ์และจริง ๆ แล้วให้สิทธิ์เราในการใช้การมีส่วนร่วมของคุณ สำหรับรายละเอียด โปรดเยี่ยมชม [เว็บไซต์ CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)

สำคัญ: เมื่อแปลข้อความใน repo นี้ โปรดมั่นใจว่าคุณไม่ได้ใช้การแปลด้วยเครื่อง เราจะตรวจสอบการแปลผ่านชุมชน ดังนั้นโปรดอาสาเฉพาะการแปลในภาษาที่คุณมีความชำนาญ

เมื่อคุณส่ง pull request, CLA-bot จะกำหนดโดยอัตโนมัติว่าคุณจำเป็นต้องให้ CLA หรือไม่และประดับ PR อย่างเหมาะสม (เช่น label, comment) เพียงทำตามคำแนะนำที่บอทให้ คุณจะต้องทำเช่นนี้เพียงครั้งเดียวในทุก repository ที่ใช้ CLA ของเรา

โปรเจ็กต์นี้ได้รับการยอมรับ [รหัสประพฤติโอเพนซอร์สของ Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) สำหรับข้อมูลเพิ่มเติมโปรดอ่านคำถามที่พบบ่อยเกี่ยวกับรหัสประพฤติหรือส่งอีเมลไปที่ [Email opencode](opencode@microsoft.com) หากมีคำถามหรือข้อคิดเห็นเพิ่มเติม

## มาเริ่มกันเลย

ตอนนี้คุณได้ทำตามขั้นตอนที่จำเป็นเพื่อทำคอร์สนี้ให้เสร็จแล้ว มาเริ่มกันเลยโดยการดู [บทนำสู่ Generative AI และ LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาที่เป็นภาษาแม่ควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ แนะนำให้ใช้บริการแปลภาษามนุษย์ที่มีความเชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้