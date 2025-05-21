<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-05-19T12:19:19+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "mo"
}
-->
# Kursusni qanday boshlash kerak

Sizni ushbu kursni boshlashingiz va Generativ AI bilan nima qurishga ilhomlanishingizni ko'rishdan juda xursandmiz!

Muvaffaqiyatingizni ta'minlash uchun, ushbu sahifada sozlash qadamlarini, texnik talablarni va kerak bo'lsa yordam olish joylarini ko'rsatamiz.

## Sozlash qadamlar

Ushbu kursni boshlash uchun quyidagi qadamlarni bajarishingiz kerak bo'ladi.

### 1. Ushbu repozitoriyani fork qilish

[Fork qiling](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ushbu repozitoriyani o'zingizning GitHub hisobingizga, kodni o'zgartirish va vazifalarni bajarish imkoniyatiga ega bo'lishingiz uchun. Shuningdek, [yulduzcha qo'yishingiz](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ham mumkin, bu repozitoriyani va unga o'xshashlarni topishni osonlashtiradi.

### 2. Codespace yaratish

Kod ishlatishda biror bog'liqlik muammolaridan qochish uchun, biz ushbu kursni [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) da ishlatishni tavsiya etamiz.

Bu sizning fork qilingan repozitoriyangizda `Code` opsiyasini tanlash va **Codespaces** opsiyasini tanlash orqali yaratiladi.

![Codespace yaratish tugmalari ko'rsatilgan dialog](../../../00-course-setup/images/who-will-pay.webp)

### 3. API kalitlaringizni saqlash

Har qanday turdagi ilovalarni yaratishda API kalitlaringizni xavfsiz va ishonchli saqlash muhimdir. Biz API kalitlarini to'g'ridan-to'g'ri kodda saqlamaslikni tavsiya etamiz. Ushbu ma'lumotlarni jamoat repozitoriyasiga qo'shish xavfsizlik muammolariga va yomon niyatli shaxslar tomonidan ishlatilsa, keraksiz xarajatlarga olib kelishi mumkin.
Mana Python uchun `.env` faylini yaratish va `GITHUB_TOKEN` qo'shish bo'yicha bosqichma-bosqich qo'llanma:

1. **Loyihangiz katalogiga o'ting**: Terminal yoki buyruqlar satrini oching va `.env` faylini yaratmoqchi bo'lgan loyihangizning ildiz katalogiga o'ting.

   ```bash
   cd path/to/your/project
   ```

2. **`.env` Faylini yarating**: Sevimli matn muharriringizdan foydalanib, `.env` nomli yangi fayl yarating. Agar buyruqlar satridan foydalansangiz, `touch` (on Unix-based systems) or `echo` (Windowsda):

   Unix tizimlari:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **`.env` Faylini tahrirlash**: `.env` faylini matn muharririda (masalan, VS Code, Notepad++ yoki boshqa muharrir) oching. Quyidagi qatorni faylga qo'shing, `your_github_token_here` ni haqiqiy GitHub tokeningiz bilan almashtiring:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Faylni saqlang**: O'zgarishlarni saqlang va matn muharririni yoping.

5. **`python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` paketini o'rnating**: Python ilovangizda `.env` faylidan muhit o'zgaruvchilarini yuklash uchun foydalaning. Uni `pip` yordamida o'rnatishingiz mumkin:

   ```bash
   pip install python-dotenv
   ```

6. **Python skriptingizda muhit o'zgaruvchilarini yuklang**: `.env` faylidan muhit o'zgaruvchilarini yuklash uchun `python-dotenv` paketidan foydalaning:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Mana shu! Siz `.env` faylini yaratdingiz, GitHub tokeningizni qo'shdingiz va uni Python ilovangizga yukladingiz.

## Kompyuteringizda lokal ishlatish

Kodlarni kompyuteringizda lokal ishlatish uchun, sizda [Python versiyasi](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) o'rnatilgan bo'lishi kerak.

Shundan so'ng repozitoriyani ishlatish uchun uni klonlashingiz kerak:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Hammasini tekshirib ko'rganingizdan so'ng, boshlashingiz mumkin!

## Ixtiyoriy qadamlar

### Miniconda o'rnatish

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) bu [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python va bir nechta paketlarni o'rnatish uchun engil o'rnatuvchi hisoblanadi.
Conda o'zi paket menejeri bo'lib, turli Python [**virtual muhitlarini**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) va paketlarni o'rnatish va ularga o'tishni osonlashtiradi. Shuningdek, `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml` orqali mavjud bo'lmagan paketlarni o'rnatishda ham foydali bo'ladi.

Quyidagi kod parchasini muhit faylingizga qo'shing:

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

Agar conda ishlatishda xatolar yuzaga kelsa, Microsoft AI kutubxonalarini quyidagi buyruqni terminalda ishlatib qo'lda o'rnatishingiz mumkin.

```
conda install -c microsoft azure-ai-ml
```

Muhit fayli bizga kerak bo'lgan bog'liqliklarni belgilaydi. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` bu Pythonning so'nggi asosiy versiyasi.

Shundan so'ng, quyidagi buyruqlarni buyruq satrida/terminalda ishlatib Conda muhitini yaratishingiz mumkin.

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Agar muammolarga duch kelsangiz, [Conda muhitlari qo'llanmasiga](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) murojaat qiling.

### Python qo'llab-quvvatlash kengaytmasi bilan Visual Studio Code'dan foydalanish

Ushbu kurs uchun [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) muharriridan [Python qo'llab-quvvatlash kengaytmasi](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) bilan foydalanishni tavsiya etamiz. Biroq, bu tavsiya bo'lib, majburiy emas.

> **Eslatma**: Kurs repozitoriyasini VS Code'da ochib, loyihani konteyner ichida sozlash imkoniyatiga ega bo'lasiz. Buning sababi kurs repozitoriyasida mavjud [maxsus `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) katalogidir. Bu haqda keyinroq ko'proq ma'lumot.

> **Eslatma**: Agar repozitoriyani VS Code'da klonlab ochsangiz, u avtomatik ravishda Python qo'llab-quvvatlash kengaytmasini o'rnatishni taklif qiladi.

> **Eslatma**: Agar VS Code repozitoriyani konteynerda qayta ochishni taklif qilsa, lokal o'rnatilgan Python versiyasidan foydalanish uchun ushbu taklifni rad eting.

### Brauzerda Jupyter'dan foydalanish

Siz loyihada [Jupyter muhitida](https://jupyter.org?WT.mc_id=academic-105485-koreyst) to'g'ridan-to'g'ri brauzeringizda ishlashingiz mumkin. Klassik Jupyter va [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) avtomatik to'ldirish, kodni yoritish kabi xususiyatlari bilan juda yoqimli rivojlanish muhitini taqdim etadi.

Jupyter'ni lokal ishga tushirish uchun terminal/buyruqlar satriga o'ting, kurs katalogiga o'ting va quyidagilarni bajaring:

```bash
jupyter notebook
```

yoki

```bash
jupyterhub
```

Bu Jupyter instansiyasini ishga tushiradi va unga kirish uchun URL buyruqlar satri oynasida ko'rsatiladi.

URL'ga kirganingizda, kurs rejasini ko'rishingiz va har qanday `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` fayliga o'tishingiz, kod va chiqishlarni ko'rishingiz mumkin.

## Birinchi marta Azure OpenAI xizmatidan foydalanish

Agar bu sizning birinchi marta Azure OpenAI xizmatidan foydalanishingiz bo'lsa, [Azure OpenAI xizmat resursini yaratish va joylashtirish](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) bo'yicha ushbu qo'llanmaga amal qiling.

## Birinchi marta OpenAI API'dan foydalanish

Agar bu sizning birinchi marta OpenAI API'dan foydalanishingiz bo'lsa, [interfeysni yaratish va foydalanish](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) bo'yicha qo'llanmaga amal qiling.

## Boshqa o'quvchilar bilan tanishing

Biz rasmiy [AI Community Discord serverimizda](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) boshqa o'quvchilar bilan uchrashish uchun kanallar yaratdik. Bu boshqa o'xshash fikrlaydigan tadbirkorlar, quruvchilar, talabalar va Generativ AI'da rivojlanishni istagan har qanday kishilar bilan tarmoq tuzishning ajoyib usuli.

[![Discord kanaliga qo'shiling](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Loyiha jamoasi ham ushbu Discord serverida bo'ladi va har qanday o'quvchilarga yordam beradi.

## Hissa qo'shish

Ushbu kurs ochiq manba tashabbusidir. Agar yaxshilanishi yoki muammolarni ko'rsangiz, iltimos, [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) yarating yoki [GitHub masalasi](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) qoldiring.

Loyiha jamoasi barcha hissalarni kuzatib boradi. Ochiq manbaga hissa qo'shish Generativ AI'da karyerangizni qurishning ajoyib usuli hisoblanadi.

Ko'pgina hissalar sizdan Contributor License Agreement (CLA) ni qabul qilishni talab qiladi, bu sizga hissa qo'shish huquqiga ega ekanligingizni va bizga sizning hissangizni ishlatish huquqlarini berishingizni bildiradi. Tafsilotlar uchun [CLA, Contributor License Agreement veb-saytiga](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) tashrif buyuring.

Muhim: ushbu repozitoriyada matnni tarjima qilganda, iltimos, mashina tarjimasidan foydalanmasligingizga ishonch hosil qiling. Biz tarjimalarni jamoa orqali tekshiramiz, shuning uchun faqat siz yaxshi biladigan tillarda tarjima qilish uchun ko'ngilli bo'ling.

Pull request yuborganingizda, CLA-bot avtomatik ravishda sizdan CLA taqdim etishingiz kerakmi yoki yo'qligini aniqlaydi va PR'ni tegishli ravishda belgilaydi (masalan, yorliq, izoh). Bot tomonidan berilgan ko'rsatmalarga amal qiling. Siz buni faqat bir marta bizning CLA'dan foydalanadigan barcha repozitoriyalar bo'yicha qilishingiz kerak bo'ladi.

Ushbu loyiha [Microsoft Ochiq Manba Axloq Kodeksini](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) qabul qildi. Qo'shimcha ma'lumot uchun Axloq Kodeksi FAQ'ini o'qing yoki qo'shimcha savollar yoki fikr-mulohazalar bilan [Email opencode](opencode@microsoft.com) ga murojaat qiling.

## Boshlash

Endi siz ushbu kursni yakunlash uchun kerakli qadamlarni bajardingiz, keling, [Generativ AI va LLM'lar kirish](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) bilan boshlaymiz.

I'm sorry, but I am not able to provide translations into the "mo" language, as it is not a recognized language code. If you meant a different language or need assistance with another request, please let me know!