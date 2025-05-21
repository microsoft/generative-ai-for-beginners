<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-05-19T12:24:50+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "tr"
}
-->
# Bu kursa başlarken

Bu kursa başlamanız ve Üretken Yapay Zeka ile neler inşa edebileceğinizi görmeniz için çok heyecanlıyız!

Başarınızı sağlamak için, bu sayfa kurulum adımlarını, teknik gereksinimleri ve gerektiğinde nereden yardım alabileceğinizi özetlemektedir.

## Kurulum Adımları

Bu kursu almaya başlamak için aşağıdaki adımları tamamlamanız gerekecek.

### 1. Bu Depoyu Çatallayın

Herhangi bir kodu değiştirebilmek ve zorlukları tamamlayabilmek için [bu tüm depoyu kendi GitHub hesabınıza çatallayın](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst). Ayrıca [bu depoyu yıldız (🌟) ekleyerek](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) daha kolay bulabilir ve ilgili depoları keşfedebilirsiniz.

### 2. Bir kod alanı oluşturun

Kodu çalıştırırken herhangi bir bağımlılık sorununu önlemek için, bu kursu bir [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) içinde çalıştırmanızı öneririz.

Bu, çatalladığınız depo sürümünde `Code` seçeneğini seçerek ve **Codespaces** seçeneğini belirleyerek oluşturulabilir.

![Bir kod alanı oluşturma butonlarını gösteren dialog](../../../00-course-setup/images/who-will-pay.webp)

### 3. API Anahtarlarınızı Saklama

Herhangi bir türde uygulama geliştirirken API anahtarlarınızı güvende ve emniyette tutmak önemlidir. API anahtarlarını doğrudan kodunuza kaydetmemenizi öneririz. Bu bilgileri herkese açık bir depoya yüklemek, güvenlik sorunlarına ve kötü niyetli bir kişi tarafından kullanıldığında istenmeyen maliyetlere yol açabilir. Python için bir `.env` dosyası oluşturma ve `GITHUB_TOKEN` ekleme konusunda adım adım bir kılavuz:

1. **Proje Dizininize Gitmek**: Terminalinizi veya komut istemcinizi açın ve `.env` dosyasını oluşturmak istediğiniz proje kök dizinine gidin.

   ```bash
   cd path/to/your/project
   ```

2. **`.env` Dosyasını Oluşturun**: Tercih ettiğiniz metin düzenleyiciyi kullanarak `.env` adlı yeni bir dosya oluşturun. Komut satırını kullanıyorsanız, `touch` (on Unix-based systems) or `echo` (Windows'ta) kullanabilirsiniz:

   Unix tabanlı sistemler:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **`.env` Dosyasını Düzenleyin**: `.env` dosyasını bir metin düzenleyicide (örneğin, VS Code, Notepad++ veya başka bir düzenleyici) açın. Aşağıdaki satırı dosyaya ekleyin, `your_github_token_here` kısmını gerçek GitHub tokenınızla değiştirin:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Dosyayı Kaydedin**: Değişiklikleri kaydedin ve metin düzenleyiciyi kapatın.

5. **`python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` paketini kurarak `.env` dosyasından Python uygulamanıza ortam değişkenlerini yükleyin. Bunu `pip` kullanarak yükleyebilirsiniz:

   ```bash
   pip install python-dotenv
   ```

6. **Python Scriptinizde Ortam Değişkenlerini Yükleyin**: Python scriptinizde, `.env` dosyasından ortam değişkenlerini yüklemek için `python-dotenv` paketini kullanın:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

İşte bu kadar! Başarıyla bir `.env` dosyası oluşturduğunuz, GitHub tokenınızı eklediğiniz ve Python uygulamanıza yüklediğiniz.

## Bilgisayarınızda Yerel Olarak Çalıştırma

Kodu bilgisayarınızda yerel olarak çalıştırmak için, bir [Python sürümünün kurulu](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) olması gerekecek.

Daha sonra depoyu kullanmak için, onu klonlamanız gerekecek:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Her şeyi kontrol ettiğinizde, başlamaya hazırsınız!

## Opsiyonel Adımlar 

### Miniconda Kurulumu 

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst), [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python ve birkaç paketi kurmak için hafif bir yükleyicidir.
Conda, farklı Python [**sanallaştırılmış ortamlar**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ve paketler arasında geçiş yapmayı kolaylaştıran bir paket yöneticisidir. Ayrıca `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml` üzerinden bulunamayan paketleri yüklemek için de faydalıdır.

Ortam dosyanızı aşağıdaki kod parçacığı ile doldurun:

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

Conda kullanırken hatalar alırsanız, terminalde aşağıdaki komutu kullanarak Microsoft AI Kütüphanelerini manuel olarak yükleyebilirsiniz.

```
conda install -c microsoft azure-ai-ml
```

Ortam dosyası, ihtiyaç duyduğumuz bağımlılıkları belirtir. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` Python'un en son büyük sürümüdür.

Bu işlemi tamamladıktan sonra, komut satırı/terminalde aşağıdaki komutları çalıştırarak Conda ortamınızı oluşturabilirsiniz

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Herhangi bir sorun yaşarsanız, [Conda ortamları kılavuzuna](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) başvurabilirsiniz.

### Python destek uzantısı ile Visual Studio Code kullanma

Bu kurs için [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editörünü, [Python destek uzantısı](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ile kullanmanızı öneririz. Ancak bu, daha çok bir öneri olup kesin bir gereklilik değildir.

> **Not**: VS Code'da kurs deposunu açarak, projeyi bir konteyner içinde kurma seçeneğine sahip olursunuz. Bunun nedeni, kurs deposunda bulunan [özel `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) dizinidir. Daha fazla bilgi daha sonra.

> **Not**: Depoyu klonlayıp VS Code'da açtığınızda, Python destek uzantısını yüklemenizi otomatik olarak önerir.

> **Not**: VS Code size depoyu bir konteyner içinde yeniden açmanızı önerirse, bu isteği reddedin ve yerel olarak kurulu Python sürümünü kullanın.

### Tarayıcıda Jupyter Kullanma

Projeyi [Jupyter ortamı](https://jupyter.org?WT.mc_id=academic-105485-koreyst) kullanarak doğrudan tarayıcınızda da çalışabilirsiniz. Hem klasik Jupyter hem de [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst), otomatik tamamlama, kod vurgulama gibi özelliklerle oldukça hoş bir geliştirme ortamı sağlar.

Jupyter'i yerel olarak başlatmak için, terminal/komut satırına gidin, kurs dizinine gidin ve şu komutu çalıştırın:

```bash
jupyter notebook
```

veya

```bash
jupyterhub
```

Bu, bir Jupyter instance'ı başlatacak ve erişim URL'si komut satırı penceresinde gösterilecektir.

URL'ye eriştiğinizde, kurs içeriğini görebilmeli ve herhangi bir `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` dosyasına giderek kodları ve çıktıları inceleyebilmelisiniz.

## Azure OpenAI Hizmetini ilk kez kullanma

Azure OpenAI hizmeti ile ilk kez çalışıyorsanız, bir Azure OpenAI Hizmeti kaynağı [oluşturma ve dağıtma](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) konusunda bu kılavuzu takip edin.

## OpenAI API'sini ilk kez kullanma

OpenAI API ile ilk kez çalışıyorsanız, [Arayüz oluşturma ve kullanma](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) konusunda kılavuzu takip edin.

## Diğer Öğrencilerle Tanışın

Diğer öğrencilerle tanışmak için resmi [AI Community Discord sunucumuzda](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) kanallar oluşturduk. Bu, Üretken Yapay Zeka'da seviyesini yükseltmek isteyen diğer girişimciler, yapıcılar, öğrenciler ve herkesle ağ kurmanın harika bir yoludur.

[![Discord kanalına katıl](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Proje ekibi de bu Discord sunucusunda öğrencilere yardımcı olacaktır.

## Katkıda Bulunun

Bu kurs açık kaynaklı bir girişimdir. İyileştirme alanları veya sorunlar görürseniz, lütfen bir [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) oluşturun veya bir [GitHub sorunu](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) kaydedin.

Proje ekibi tüm katkıları takip edecektir. Açık kaynaklı projelere katkıda bulunmak, Üretken Yapay Zeka kariyerinizi inşa etmek için harika bir yoldur.

Çoğu katkı, bir Katkıda Bulunan Lisans Sözleşmesi (CLA) imzalamanızı gerektirir. Bu, katkınızın kullanım haklarını bize vermeye hakkınız olduğunu ve gerçekten de verdiğinizi beyan eder. Detaylar için [CLA, Katkıda Bulunan Lisans Sözleşmesi web sitesini](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) ziyaret edin.

Önemli: Bu depodaki metni çevirirken, lütfen makine çevirisi kullanmadığınızdan emin olun. Çevirileri topluluk aracılığıyla doğrulayacağız, bu yüzden lütfen yalnızca yetkin olduğunuz dillerde çeviriler için gönüllü olun.

Bir çekme isteği gönderdiğinizde, bir CLA-botu otomatik olarak bir CLA sağlamanız gerekip gerekmediğini belirleyecek ve PR'ı uygun şekilde süsleyecektir (örneğin, etiket, yorum). Bot tarafından sağlanan talimatları takip edin. Tüm depolarımızı kullandığınızda bunu yalnızca bir kez yapmanız gerekecektir.

Bu proje, [Microsoft Açık Kaynak Davranış Kuralları](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)'nı benimsemiştir. Daha fazla bilgi için Davranış Kuralları SSS'yi okuyun veya ek sorular veya yorumlar için [Email opencode](opencode@microsoft.com) ile iletişime geçin.

## Başlayalım

Bu kursu tamamlamak için gereken adımları tamamladığınıza göre, [Üretken Yapay Zeka ve LLM'lere giriş](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) ile başlayalım.

**Sorumluluk Reddi**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanılmasından doğabilecek yanlış anlaşılmalar veya yanlış yorumlamalardan sorumlu değiliz.