<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:48:40+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "tr"
}
-->
# Bu kursa başlarken

Bu kursa başlamanız ve Üretken Yapay Zeka ile neler inşa etmek için ilham alacağınızı görmek için çok heyecanlıyız!

Başarınızı sağlamak için bu sayfa, kurulum adımlarını, teknik gereksinimleri ve gerekirse nereden yardım alabileceğinizi özetlemektedir.

## Kurulum Adımları

Bu kursa başlamak için aşağıdaki adımları tamamlamanız gerekecek.

### 1. Bu Depoyu Çatallayın

Herhangi bir kodu değiştirebilmek ve zorlukları tamamlayabilmek için [bu tüm depoyu](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) kendi GitHub hesabınıza çatallayın. Ayrıca bu depoyu ve ilgili depoları daha kolay bulmak için [yıldız (🌟) ekleyebilirsiniz](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst).

### 2. Bir kod alanı oluşturun

Kod çalıştırırken herhangi bir bağımlılık sorunundan kaçınmak için bu kursu [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) içinde çalıştırmanızı öneririz.

Bu, çatalladığınız depo sürümünde `Code` seçeneğini seçerek ve **Codespaces** seçeneğini seçerek oluşturulabilir.

![Bir kod alanı oluşturma düğmelerini gösteren diyalog](../../../00-course-setup/images/who-will-pay.webp)

### 3. API Anahtarlarınızı Saklama

Herhangi bir tür uygulama geliştirirken API anahtarlarınızı güvende ve emniyette tutmak önemlidir. Herhangi bir API anahtarını doğrudan kodunuza kaydetmemenizi öneririz. Bu bilgileri herkese açık bir depoya yüklemek, kötü niyetli bir kişi tarafından kullanılması durumunda güvenlik sorunlarına ve hatta istenmeyen maliyetlere neden olabilir. Python için bir `.env` dosyasının nasıl oluşturulacağı ve `GITHUB_TOKEN` eklenmesi konusunda adım adım bir kılavuz:

1. **Proje Dizininize Gidin**: Terminalinizi veya komut istemcinizi açın ve `.env` dosyasını oluşturmak istediğiniz projenizin kök dizinine gidin.

   ```bash
   cd path/to/your/project
   ```

2. **`.env` Dosyasını Oluşturun**: Tercih ettiğiniz metin düzenleyiciyi kullanarak `.env` adlı yeni bir dosya oluşturun. Komut satırını kullanıyorsanız, `touch` (on Unix-based systems) or `echo` kullanabilirsiniz (Windows'ta):

   Unix tabanlı sistemler:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **`.env` Dosyasını Düzenleyin**: `.env` dosyasını bir metin düzenleyicide (örneğin, VS Code, Notepad++ veya başka bir düzenleyici) açın. Aşağıdaki satırı dosyaya ekleyin, `your_github_token_here` ifadesini gerçek GitHub jetonunuzla değiştirin:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Dosyayı Kaydedin**: Değişiklikleri kaydedin ve metin düzenleyiciyi kapatın.

5. `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` paketini yükleyerek `.env` dosyasından Python uygulamanıza ortam değişkenlerini yükleyin. `pip` kullanarak yükleyebilirsiniz:

   ```bash
   pip install python-dotenv
   ```

6. **Python Betiğinizde Ortam Değişkenlerini Yükleyin**: Python betiğinizde, `.env` dosyasından ortam değişkenlerini yüklemek için `python-dotenv` paketini kullanın:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

İşte bu kadar! Başarıyla bir `.env` dosyası oluşturdunuz, GitHub jetonunuzu eklediniz ve bunu Python uygulamanıza yüklediniz.

## Bilgisayarınızda Yerel Olarak Çalıştırma

Kodları bilgisayarınızda yerel olarak çalıştırmak için, [Python'un bir sürümünü yüklemeniz](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) gerekir.

Daha sonra depoyu kullanmak için, klonlamanız gerekir:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Her şeyi kontrol ettikten sonra, başlayabilirsiniz!

## Opsiyonel Adımlar

### Miniconda Yükleme

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst), [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python ve birkaç paketi yüklemek için hafif bir yükleyicidir. Conda'nın kendisi bir paket yöneticisidir ve farklı Python [**sanallaştırma ortamları**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ve paketleri arasında geçiş yapmayı kolaylaştırır. Ayrıca `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml` aracılığıyla bulunamayan paketleri yüklerken de işe yarar.

Aşağıdaki kod parçacığıyla ortam dosyanızı doldurun:

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

Conda kullanırken hata alıyorsanız, terminalde aşağıdaki komutu kullanarak Microsoft AI Kütüphanelerini manuel olarak yükleyebilirsiniz.

```
conda install -c microsoft azure-ai-ml
```

Ortam dosyası, ihtiyaç duyduğumuz bağımlılıkları belirtir. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3`, Python'un en son ana sürümüdür.

Bunu yaptıktan sonra, komut satırı/terminalde aşağıdaki komutları çalıştırarak Conda ortamınızı oluşturabilirsiniz:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Herhangi bir sorunla karşılaşırsanız [Conda ortamları kılavuzuna](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) başvurun.

### Python destek uzantısı ile Visual Studio Code kullanma

Bu kurs için [Python destek uzantısı](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) yüklü [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editörünü kullanmanızı öneririz. Ancak bu daha çok bir tavsiye olup kesin bir gereklilik değildir.

> **Not**: Kurs deposunu VS Code'da açarak projeyi bir konteyner içinde kurma seçeneğiniz vardır. Bu, kurs deposunda bulunan [özel `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) dizini nedeniyle mümkündür. Daha fazlası daha sonra.

> **Not**: Depoyu klonlayıp VS Code'da açtığınızda, Python destek uzantısını yüklemenizi otomatik olarak önerecektir.

> **Not**: VS Code, depoyu bir konteyner içinde yeniden açmanızı önerirse, yerel olarak yüklü Python sürümünü kullanmak için bu isteği reddedin.

### Tarayıcıda Jupyter Kullanma

Projeyi doğrudan tarayıcınızda [Jupyter ortamı](https://jupyter.org?WT.mc_id=academic-105485-koreyst) kullanarak da çalışabilirsiniz. Hem klasik Jupyter hem de [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst), otomatik tamamlama, kod vurgulama gibi özelliklerle oldukça hoş bir geliştirme ortamı sunar.

Jupyter'i yerel olarak başlatmak için terminal/komut satırına gidin, kurs dizinine gidin ve şunu çalıştırın:

```bash
jupyter notebook
```

veya

```bash
jupyterhub
```

Bu, bir Jupyter oturumu başlatacak ve erişim URL'si komut satırı penceresinde gösterilecektir.

URL'ye eriştiğinizde, kurs içeriğini görebilir ve herhangi bir `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` dosyasına gidip kodu ve çıktıları görebilirsiniz.

## Azure OpenAI Hizmetini ilk kez kullanma

Azure OpenAI hizmeti ile ilk kez çalışıyorsanız, bir Azure OpenAI Hizmet kaynağının nasıl [oluşturulup dağıtılacağına](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) dair bu kılavuzu takip edin.

## OpenAI API'sini ilk kez kullanma

OpenAI API ile ilk kez çalışıyorsanız, Arayüzün nasıl [oluşturulup kullanılacağına](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) dair kılavuzu takip edin.

## Diğer Öğrenicilerle Tanışın

Resmi [AI Topluluk Discord sunucumuzda](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) diğer öğrenicilerle tanışmak için kanallar oluşturduk. Bu, aynı düşünceye sahip girişimciler, geliştiriciler, öğrenciler ve Üretken Yapay Zeka alanında kendini geliştirmek isteyen herkesle ağ kurmanın harika bir yoludur.

[![Discord kanalına katılın](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Proje ekibi de bu Discord sunucusunda öğrencilere yardımcı olacaktır.

## Katkıda Bulunun

Bu kurs, açık kaynaklı bir girişimdir. İyileştirme alanları veya sorunlar görürseniz, lütfen bir [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) oluşturun veya bir [GitHub sorunu](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) kaydedin.

Proje ekibi tüm katkıları takip edecektir. Açık kaynağa katkıda bulunmak, Üretken Yapay Zeka alanında kariyerinizi geliştirmenin harika bir yoludur.

Çoğu katkı, bize katkınızı kullanma hakkı verdiğinizi ve bu hakka sahip olduğunuzu beyan eden bir Katkıda Bulunan Lisans Anlaşması (CLA) kabul etmenizi gerektirir. Detaylar için [CLA, Katkıda Bulunan Lisans Anlaşması web sitesini](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) ziyaret edin.

Bu depodaki metinleri çevirirken, lütfen makine çevirisi kullanmadığınızdan emin olun. Çevirileri topluluk aracılığıyla doğrulayacağız, bu yüzden lütfen yalnızca yetkin olduğunuz dillerde çeviri yapmaya gönüllü olun.

Bir pull request gönderdiğinizde, bir CLA-botu otomatik olarak bir CLA sağlamanız gerekip gerekmediğini belirleyecek ve PR'yi uygun şekilde süsleyecektir (örneğin, etiket, yorum). Bot tarafından sağlanan talimatları takip edin. Bunu tüm depolarımızda yalnızca bir kez yapmanız gerekecek.

Bu proje, [Microsoft Açık Kaynak Davranış Kurallarını](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) benimsemiştir. Daha fazla bilgi için Davranış Kuralları SSS'yi okuyun veya [Email opencode](opencode@microsoft.com) ile ek sorularınız veya yorumlarınız için iletişime geçin.

## Başlayalım

Bu kursu tamamlamak için gereken adımları tamamladığınıza göre, [Üretken Yapay Zeka ve LLM'lere giriş](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) ile başlayalım.

**Feragatname**: 
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için, profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından doğabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.