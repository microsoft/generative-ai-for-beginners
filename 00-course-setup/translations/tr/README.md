# Kursa Başlarken

Bu kursa başlamanız ve Üretken Yapay Zeka (Generative AI) ile neler inşa edebileceğinizi keşfetmeniz için çok heyecanlıyız!

Başarıya ulaşmanızı sağlamak için bu sayfada kurulum adımları, teknik gereksinimler ve gerektiğinde nasıl yardım alabileceğiniz açıklanmaktadır.

## Kurulum Adımları

Bu kursu almaya başlamak için aşağıdaki adımları tamamlamanız gerekmektedir.

### 1. Bu repoyu kendi deponuza ekleyin

Bu kurs kapsamında kodu değiştirebilmek ve alıştırmaları tamamlayabilmek için [bu depoyu kendi GitHub hesabınıza forklayın](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) Ayrıca, bu ve ilgili diğer depoları daha kolay bulmak için [bu repoyu yıldızlayabilirsiniz (🌟).](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)

### 2. Bir Codespace Oluşturun

Kodun çalıştırılması sırasında bağımlılık sorunlarını önlemek için, bu kursu bir [GitHub Codespace](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) ortamında yürütmenizi öneririz.

Bunun için, çatalladığınız depo üzerinde `Code` oseçeneğine tıklayın ve **Codespaces** seçeneğini belirleyin.

![Kod alanı oluşturmak için düğmeleri gösteren iletişim kutusu](../../images/who-will-pay.webp?WT.mc_id=academic-105485-koreyst)

### 3. API Anahtarlarınızı Güvenli Bir Şekilde Saklayın

API anahtarlarınızı güvenli bir şekilde saklamak, herhangi bir uygulama geliştirirken önemlidir. API anahtarlarını doğrudan koda kaydetmemenizi öneririz. Anahtarları herkese açık bir depoya yüklemek güvenlik sorunlarına ve kötü niyetli kullanım nedeniyle maliyetlere yol açabilir.
`.env` Dosyası ile `GITHUB_TOKEN` Anahtarlarını Saklama:

1. **Proje Dizininize Gidin**: Terminalinizi veya komut isteminizi açın ve `.env` dosyasını oluşturmak istediğiniz projenizin kök dizinine gidin.

   ```bash
   cd path/to/your/project
   ```

2. **`.env` Dosyasını Oluşturun**: Tercih ettiğiniz metin editörünü kullanarak `.env` adında yeni bir dosya oluşturun. Komut satırını kullanıyorsanız, `touch` (Unix tabanlı sistemlerde) veya `echo`    (Windows'ta) kullanabilirsiniz:

   Unix tabanlı sistemler:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo. > .env
   ```

3. **`.env` Dosyasını Düzenleyin**: `.env` dosyasını bir metin düzenleyicide açın (örneğin, VS Code, Notepad++ veya başka bir düzenleyici). Aşağıdaki satırı dosyaya ekleyin ve `your_github_token_here` yerine gerçek GitHub tokenınızı yazın:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Dosyayı Kaydet**: Değişiklikleri kaydedin ve metin düzenleyiciyi kapatın.

5. **`python-dotenv`** paketini yükleyin: Henüz yüklemediyseniz, ortam değişkenlerini `.env` dosyasından Python uygulamanıza yüklemek için `python-dotenv` paketini yüklemeniz gerekir. Bunu `pip` kullanarak yükleyebilirsiniz:

   ```bash
   pip install python-dotenv
   ```

6. **Ortam Değişkenlerini Python Betiklerinize Yükleyin**: Python betiğinizde, `.env` dosyasından ortam değişkenlerini yüklemek için `python-dotenv` paketini kullanın:

   ```python
   from dotenv import load_dotenv
   import os

   # .env dosyasından ortam değişkenlerini yükle
   load_dotenv()

   # GITHUB_TOKEN değişkenine erişin
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

İşte bu kadar! Başarıyla bir `.env` dosyası oluşturdunuz, GitHub token'ınızı eklediniz ve Python uygulamanıza yüklediniz.

## Bilgisayarınızda yerel olarak nasıl çalıştırılır

Kodu bilgisayarınızda yerel olarak çalıştırmak için, aşağıdaki programların bir sürümüne sahip olmanız gerekir [Python'u yükleyin](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Daha sonra depoyu kullanmak için onu klonlamanız gerekir:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Her şeyi kontrol ettikten sonra başlayabilirsiniz!

### Miniconda Kurulumu (isteğe bağlı)

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst), [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python ve birkaç paket yüklemek için hafif bir yükleyicidir.
Conda'nın kendisi, farklı Python [**sanal ortamlar**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ve paketler arasında kurulum ve geçişi kolaylaştıran bir paket yöneticisidir. Ayrıca `pip` aracılığıyla kullanılamayan paketleri yüklemek için de kullanışlıdır.

Kurulum için [MiniConda kurulum kılavuzu](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)'nu takip edebilirsiniz.

Miniconda yüklendiğinde, [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)'yi klonlamanız gerekir (eğer henüz yapmadıysanız)

Ardından, sanal bir ortam oluşturmanız gerekir. Bunu Conda ile yapmak için, devam edin ve yeni bir ortam dosyası (_environment.yml_) oluşturun. Codespaces kullanarak takip ediyorsanız, bunu `.devcontainer` dizini içinde oluşturun, böylece `.devcontainer/environment.yml`.

Devam edin ve ortam dosyanızı aşağıdaki kod parçacığı ile doldurun:

```yml
name: <environment-name>
channels:
 - defaults
dependencies:
- python=<python-version>
- openai
- python-dotenv
- microsoft azure-ai-ml

```

Eğer conda kullanırken hata alıyorsanız, aşağıdaki komutu terminalde kullanarak Microsoft AI Kütüphanelerini manuel olarak yükleyebilirsiniz. 

```
conda install -c microsoft azure-ai-ml
```

Ortam dosyası ihtiyacımız olan bağımlılıkları belirtir. `<environment-name>` Conda ortamınız için kullanmak istediğiniz ismi, `<python-version>` ise kullanmak istediğiniz Python sürümünü ifade eder, örneğin `3` Python'un en son ana sürümüdür.

Bunu yaptıktan sonra, aşağıdaki komutları komut satırınızda/terminalinizde çalıştırarak Conda ortamınızı oluşturabilirsiniz

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer alt yolu yalnızca Codespace kurulumları için geçerlidir
conda activate ai4beg
```

Herhangi bir sorunla karşılaşırsanız [Conda ortamları kılavuzuna] (https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) bakın.

### Visual Studio Code'u Python eklentisi ile kullanma

Bu kurs için [Python eklentisi](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) yüklü [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) düzenleyicisini kullanmanızı öneririz. Ancak bu daha çok bir tavsiyedir ve kesin bir gereklilik değildir

> **Not**: Kurs deposunu VS Code'da açtığınızda, projeyi bir konteyner içinde kurma seçeneğiniz vardır. Bunun nedeni, kurs deposunda bulunan [özel `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) dizinidir. Bu konuda daha sonra bilgi vereceğiz.

> **Not**: Dizini klonlayıp VS Code'da açtığınızda, otomatik olarak bir Python destek uzantısı yüklemenizi önerecektir.

> **Not**: VS Code, depoyu bir kapsayıcıda yeniden açmanızı önerirse, Python'un yerel olarak yüklenmiş sürümünü kullanmak için bu isteği reddedin.

### Tarayıcıda Jupyter Kullanımı

Ayrıca [Jupyter environment](https://jupyter.org?WT.mc_id=academic-105485-koreyst)'ı doğrudan tarayıcınızda kullanarak proje üzerinde çalışabilirsiniz. Hem klasik Jupyter hem de [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) otomatik tamamlama, kod vurgulama gibi özelliklerle oldukça hoş bir geliştirme ortamı sağlar.

Jupyter'i yerel olarak başlatmak için terminal/komut satırına gidin, kurs dizinine gidin ve çalıştırın:

```bash
jupyter notebook
```

or

```bash
jupyterhub
```

Bu, bir Jupyter örneği başlatacak ve ona erişmek için URL komut satırı penceresinde gösterilecektir.

URL'ye eriştiğinizde, kurs taslağını görmeli ve herhangi bir `*.ipynb` dosyasına gidebilmelisiniz. Örneğin, `08-building-search-applications/python/oai-solution.ipynb`.

### Konteyner içinde çalıştırma

Her şeyi bilgisayarınızda veya Codespace'de kurmanın bir alternatifi de [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst) kullanmaktır. Kurs deposundaki özel `.devcontainer` klasörü, VS Code'un projeyi bir konteyner içinde kurmasını mümkün kılar. Codespaces dışında, bu Docker'ın kurulmasını gerektirecektir ve açıkçası, biraz çalışma gerektirir, bu nedenle bunu yalnızca konteynerlerle çalışma deneyimi olanlara öneririz.

GitHub Codespaces kullanırken API anahtarlarınızı güvende tutmanın en iyi yollarından biri Codespace Secrets kullanmaktır. Bu konuda daha fazla bilgi edinmek için lütfen [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) kılavuzunu izleyin.

## Dersler ve Teknik Gereksinimler

Kursta 6 kavram dersi ve 6 kodlama dersi bulunmaktadır.

Kodlama dersleri için Azure OpenAI Hizmetini kullanıyoruz. Bu kodu çalıştırmak için Azure OpenAI hizmetine erişmeniz ve bir API anahtarına ihtiyacınız olacak. Erişim almak için [bu başvuruyu tamamlayarak](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) başvurabilirsiniz.

Siz uygulamanızın işlenmesini beklerken her kodlama dersi, kodu ve çıktıları görüntüleyebileceğiniz bir `README.md` dosyası da içerir.

## Azure OpenAI Hizmetini ilk kez kullanma

Azure OpenAI hizmeti ile ilk kez çalışıyorsanız, lütfen [Azure OpenAI Hizmeti kaynağı oluşturma ve dağıtma](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) hakkındaki bu kılavuzu izleyin.

## OpenAI API'sini ilk kez kullanma

OpenAI API ile ilk kez çalışıyorsanız, lütfen [Arayüzün nasıl oluşturulacağı ve kullanılacağı](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) hakkındaki kılavuzu izleyin.

## Diğer Öğrencilerle Tanışın

Diğer öğrencilerle tanışmak için resmi [AI Community Discord sunucumuzda](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) kanallar oluşturduk. Bu, benzer düşünen diğer girişimciler, inşaatçılar, öğrenciler ve Üretken Yapay Zeka'da seviye atlamak isteyen herkesle ağ kurmak için harika bir yoldur.

[![Discord kanalına katılın](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Proje ekibi de öğrencilere yardımcı olmak için bu Discord sunucusunda olacaktır.

## Katkıda bulunun

Bu kurs bir açık kaynak girişimidir. İyileştirme alanları veya sorunlar görürseniz, lütfen bir [Çekme İsteği](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) oluşturun veya bir [GitHub sorunu](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) kaydedin.

Proje ekibi tüm katkıları takip edecektir. Açık kaynağa katkıda bulunmak, Üretken Yapay Zeka alanında kariyerinizi geliştirmenin harika bir yoludur.

Çoğu katkı, katkınızı kullanma hakkına sahip olduğunuzu ve aslında bize katkınızı kullanma haklarını verdiğinizi beyan eden bir Katılımcı Lisans Sözleşmesini (CLA) kabul etmenizi gerektirir. Ayrıntılar için [CLA, Contributor License Agreement web sitesini](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) ziyaret edin.

Önemli: Bu depodaki metni çevirirken lütfen makine çevirisi kullanmadığınızdan emin olun. Çevirileri topluluk aracılığıyla doğrulayacağız, bu nedenle lütfen yalnızca yetkin olduğunuz dillerdeki çeviriler için gönüllü olun.

Pull request gönderdiğinizde, bir CLA-bot otomatik olarak bir Katkıda Bulunma Lisans Sözleşmesi (CLA) gerekip gerekmediğini belirler ve PR'nizi uygun şekilde etiketler (örneğin, etiket, yorum ekler). Bot tarafından verilen talimatları takip etmeniz yeterlidir. Bu işlemi, CLA kullanan tüm depolar için yalnızca bir kez yapmanız gerekecektir.

Bu proje [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) sayfasını okuyabilir veya ek sorularınız için [Email opencode](opencode@microsoft.com) adresine e-posta gönderebilirsiniz.

## Başlayalım

Bu kursu tamamlamak için gerekli adımları tamamladığınıza göre, şimdi [Üretken Yapay Zeka ve Büyük Dil Modellerine (LLM'ler)](../../../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) giriş yaparak başlayalım.
