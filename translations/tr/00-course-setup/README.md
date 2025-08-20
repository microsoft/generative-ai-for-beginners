<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:08:52+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "tr"
}
-->
# Bu kursa Başlarken

Bu kursa başlamanız ve Üretken Yapay Zeka ile neler yaratabileceğiniz konusunda ilham almanız için çok heyecanlıyız!

Başarınızı sağlamak için, bu sayfada kurulum adımları, teknik gereksinimler ve gerekirse nereden yardım alabileceğiniz açıklanmıştır.

## Kurulum Adımları

Bu kursa başlamanız için aşağıdaki adımları tamamlamanız gerekmektedir.

### 1. Bu Depoyu Forklayın

[Tüm bu depoyu forklayın](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ve kendi GitHub hesabınıza kopyalayın. Böylece kodda değişiklik yapabilir ve görevleri tamamlayabilirsiniz. Ayrıca, bu depoyu ve ilgili depoları daha kolay bulmak için [yıldız (🌟) ekleyebilirsiniz](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst).

### 2. Bir codespace Oluşturun

Kodu çalıştırırken bağımlılık sorunları yaşamamak için bu kursu [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) üzerinde çalıştırmanızı öneririz.

Bunu, forkladığınız deponun `Code` seçeneğini seçip ardından **Codespaces** seçeneğini seçerek oluşturabilirsiniz.

![Codespace oluşturma butonlarını gösteren iletişim kutusu](../../../00-course-setup/images/who-will-pay.webp)

### 3. API Anahtarlarınızı Saklama

Herhangi bir uygulama geliştirirken API anahtarlarınızı güvende tutmak önemlidir. API anahtarlarını doğrudan kodunuzda saklamamanızı öneririz. Bu bilgileri herkese açık bir depoya göndermek güvenlik sorunlarına ve kötü niyetli kişiler tarafından kullanılması durumunda istenmeyen maliyetlere yol açabilir.  
Python için `.env` dosyası oluşturma ve `GITHUB_TOKEN` ekleme adımlarını aşağıda bulabilirsiniz:

1. **Proje Dizininize Gidin**: Terminal veya komut istemcisini açın ve `.env` dosyasını oluşturmak istediğiniz projenizin kök dizinine gidin.

   ```bash
   cd path/to/your/project
   ```

2. **`.env` Dosyasını Oluşturun**: Tercih ettiğiniz metin düzenleyici ile `.env` adlı yeni bir dosya oluşturun. Komut satırından yapıyorsanız, Unix tabanlı sistemlerde `touch`, Windows’ta ise `echo` komutlarını kullanabilirsiniz:

   Unix tabanlı sistemler:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` Dosyasını Düzenleyin**: `.env` dosyasını bir metin düzenleyicide (örneğin VS Code, Notepad++ veya başka bir editör) açın. Aşağıdaki satırı ekleyin, `your_github_token_here` kısmını gerçek GitHub tokenınızla değiştirin:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Dosyayı Kaydedin**: Değişiklikleri kaydedip metin düzenleyiciyi kapatın.

5. **`python-dotenv` Paketini Yükleyin**: Henüz yüklemediyseniz, `.env` dosyasındaki ortam değişkenlerini Python uygulamanıza yüklemek için `python-dotenv` paketini yüklemeniz gerekir. Bunu `pip` ile yapabilirsiniz:

   ```bash
   pip install python-dotenv
   ```

6. **Python Scriptinizde Ortam Değişkenlerini Yükleyin**: Python scriptinizde, `.env` dosyasındaki ortam değişkenlerini yüklemek için `python-dotenv` paketini kullanın:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Hepsi bu kadar! Başarıyla bir `.env` dosyası oluşturdunuz, GitHub tokenınızı eklediniz ve Python uygulamanıza yüklediniz.

## Kodu Bilgisayarınızda Yerel Olarak Çalıştırma

Kodu bilgisayarınızda yerel olarak çalıştırmak için bir Python sürümünün [kurulu olması gerekir](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Depoyu kullanmak için önce klonlamanız gerekir:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Her şey hazır olduğunda, başlayabilirsiniz!

## İsteğe Bağlı Adımlar

### Miniconda Kurulumu

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst), [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python ve bazı paketleri kurmak için hafif bir yükleyicidir.  
Conda, farklı Python [**sanal ortamları**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ve paketleri kolayca kurup yönetmenizi sağlayan bir paket yöneticisidir. Ayrıca `pip` ile bulunmayan paketleri kurmak için de kullanışlıdır.

Kurulum için [MiniConda kurulum rehberini](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) takip edebilirsiniz.

Miniconda kurulduktan sonra, [depo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (henüz klonlamadıysanız) klonlanmalıdır.

Sonra bir sanal ortam oluşturmanız gerekir. Conda ile bunu yapmak için yeni bir ortam dosyası (_environment.yml_) oluşturun. Codespaces kullanıyorsanız, bunu `.devcontainer` dizini içinde, yani `.devcontainer/environment.yml` olarak oluşturun.

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

Conda kullanırken hata alırsanız, Microsoft AI Kütüphanelerini terminalde aşağıdaki komutla manuel olarak yükleyebilirsiniz.

```
conda install -c microsoft azure-ai-ml
```

Ortam dosyası ihtiyaç duyduğumuz bağımlılıkları belirtir. `<environment-name>`, Conda ortamınız için kullanmak istediğiniz isimdir ve `<python-version>`, kullanmak istediğiniz Python sürümüdür; örneğin, `3` Python’un en son ana sürümüdür.

Bunu yaptıktan sonra, aşağıdaki komutları komut satırınızda/terminalinizde çalıştırarak Conda ortamınızı oluşturabilirsiniz:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Herhangi bir sorun yaşarsanız, [Conda ortamları rehberine](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) bakabilirsiniz.

### Visual Studio Code ve Python Destek Eklentisi Kullanımı

Bu kurs için [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editörünü ve [Python destek eklentisini](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) kullanmanızı öneririz. Ancak bu bir zorunluluk değil, sadece tavsiyedir.

> **Not**: Kurs deposunu VS Code’da açtığınızda, projeyi bir konteyner içinde kurma seçeneğiniz olur. Bunun sebebi, kurs deposunda bulunan [özel `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) dizinidir. Bu konuya daha sonra değineceğiz.

> **Not**: Depoyu klonlayıp VS Code’da açtığınızda, Python destek eklentisini yüklemeniz otomatik olarak önerilir.

> **Not**: VS Code, depoyu bir konteyner içinde yeniden açmanızı önerirse, yerel Python sürümünü kullanmak için bu isteği reddedin.

### Tarayıcıda Jupyter Kullanımı

Projede çalışmak için tarayıcınızda [Jupyter ortamını](https://jupyter.org?WT.mc_id=academic-105485-koreyst) da kullanabilirsiniz. Hem klasik Jupyter hem de [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) otomatik tamamlama, kod vurgulama gibi özelliklerle oldukça keyifli bir geliştirme ortamı sunar.

Jupyter’ı yerel olarak başlatmak için terminal/komut satırına gidin, kurs dizinine geçin ve şu komutu çalıştırın:

```bash
jupyter notebook
```

veya

```bash
jupyterhub
```

Bu, bir Jupyter örneği başlatacak ve erişim için URL komut satırı penceresinde gösterilecektir.

URL’ye eriştiğinizde, kurs içeriğini görebilir ve herhangi bir `*.ipynb` dosyasına gidebilirsiniz. Örneğin, `08-building-search-applications/python/oai-solution.ipynb`.

### Konteyner İçinde Çalıştırma

Bilgisayarınızda veya Codespace’de her şeyi kurmak yerine bir [konteyner](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) kullanmak da bir seçenektir. Kurs deposundaki özel `.devcontainer` klasörü, VS Code’un projeyi bir konteyner içinde kurmasını sağlar. Codespaces dışında bunu kullanmak için Docker kurulumu gerekir ve biraz uğraştırıcıdır, bu yüzden konteynerlerle deneyimi olanlara öneriyoruz.

GitHub Codespaces kullanırken API anahtarlarınızı güvende tutmanın en iyi yollarından biri Codespace Secrets kullanmaktır. Daha fazla bilgi için [Codespaces secrets yönetimi](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) rehberini takip edin.

## Dersler ve Teknik Gereksinimler

Kurs 6 kavramsal ders ve 6 kodlama dersi içerir.

Kodlama derslerinde Azure OpenAI Service kullanıyoruz. Bu kodu çalıştırmak için Azure OpenAI servisine erişiminiz ve bir API anahtarınız olması gerekir. Erişim için [bu başvuruyu tamamlayarak](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) talepte bulunabilirsiniz.

Başvurunuz işlenirken, her kodlama dersi ayrıca kodu ve çıktıları görebileceğiniz bir `README.md` dosyası içerir.

## Azure OpenAI Servisini İlk Kez Kullanma

Azure OpenAI servisi ile ilk kez çalışıyorsanız, lütfen [Azure OpenAI Service kaynağı oluşturma ve dağıtma rehberini](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) takip edin.

## OpenAI API’sini İlk Kez Kullanma

OpenAI API ile ilk kez çalışıyorsanız, lütfen [Arayüz oluşturma ve kullanma rehberini](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) takip edin.

## Diğer Öğrenenlerle Tanışın

Resmi [AI Community Discord sunucumuzda](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) diğer öğrenenlerle tanışmak için kanallar oluşturduk. Bu, benzer düşünen girişimciler, geliştiriciler, öğrenciler ve Üretken Yapay Zeka alanında kendini geliştirmek isteyen herkesle ağ kurmak için harika bir yoldur.

[![Discord kanalına katıl](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Proje ekibi de bu Discord sunucusunda öğrenenlere destek olacaktır.

## Katkıda Bulunma

Bu kurs açık kaynaklı bir girişimdir. İyileştirme alanları veya sorunlar görürseniz, lütfen bir [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) oluşturun veya bir [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) kaydedin.

Proje ekibi tüm katkıları takip edecektir. Açık kaynağa katkıda bulunmak, Üretken Yapay Zeka alanında kariyerinizi geliştirmek için harika bir yoldur.

Çoğu katkı, katkınızın kullanım haklarını bize verdiğinizi beyan eden bir Katkı Lisans Anlaşması’na (CLA) imza atmanızı gerektirir. Detaylar için [CLA, Katkı Lisans Anlaşması web sitesini](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) ziyaret edin.

Önemli: Bu depoda metin çevirisi yaparken, lütfen makine çevirisi kullanmayın. Çeviriler topluluk tarafından doğrulanacaktır, bu yüzden yalnızca iyi bildiğiniz dillerde gönüllü olun.

Pull request gönderdiğinizde, CLA-bot otomatik olarak CLA sağlamanız gerekip gerekmediğini belirleyecek ve PR’ı uygun şekilde işaretleyecektir (örneğin, etiket, yorum). Botun verdiği talimatları takip edin. Bu işlemi tüm depolarda yalnızca bir kez yapmanız yeterlidir.

Bu proje, [Microsoft Açık Kaynak Davranış Kuralları](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) kurallarını benimsemiştir. Daha fazla bilgi için Davranış Kuralları SSS bölümünü okuyabilir veya ek sorularınız için [Email opencode](opencode@microsoft.com) ile iletişime geçebilirsiniz.

## Haydi Başlayalım

Bu kursu tamamlamak için gereken adımları tamamladığınıza göre, şimdi [Üretken Yapay Zeka ve LLM’lere giriş](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) ile başlayalım.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.