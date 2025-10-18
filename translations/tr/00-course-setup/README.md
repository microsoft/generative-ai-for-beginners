<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-18T01:01:11+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "tr"
}
-->
# Bu kursa başlama

Bu kursa başlamanız ve Üretken Yapay Zeka ile neler inşa edebileceğinizi görmeniz için çok heyecanlıyız!

Başarınızı sağlamak için, bu sayfada kurulum adımları, teknik gereksinimler ve gerektiğinde yardım alabileceğiniz yerler açıklanmaktadır.

## Kurulum Adımları

Bu kursa başlamak için aşağıdaki adımları tamamlamanız gerekecek.

### 1. Bu Depoyu Çatallayın

[Bu tüm depoyu çatallayın](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) ve kendi GitHub hesabınıza kopyalayarak kodda değişiklik yapabilir ve zorlukları tamamlayabilirsiniz. Ayrıca [bu depoyu yıldızlayabilirsiniz (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ve ilgili depoları daha kolay bulabilirsiniz.

### 2. Bir Codespace oluşturun

Kodun çalıştırılması sırasında herhangi bir bağımlılık sorununu önlemek için bu kursu [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) üzerinde çalıştırmanızı öneririz.

Çatalladığınız depoda: **Code -> Codespaces -> New on main**

![Codespace oluşturma düğmelerini gösteren diyalog](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Bir gizli anahtar ekleyin

1. ⚙️ Dişli simgesi -> Komut Paleti -> Codespaces : Kullanıcı gizli anahtarını yönet -> Yeni bir gizli anahtar ekle.
2. Adı OPENAI_API_KEY olarak belirleyin, anahtarınızı yapıştırın, Kaydedin.

### 3.  Sırada ne var?

| Yapmak istediğim…   | Git…                                                                  |
|---------------------|----------------------------------------------------------------------|
| Ders 1'e başla      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)  |
| Çevrimdışı çalış    | [`setup-local.md`](02-setup-local.md)                                |
| Bir LLM Sağlayıcısı kur | [`providers.md`](03-providers.md)                                   |
| Diğer öğrenenlerle tanış | [Discord sunucumuza katılın](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Sorun Giderme

| Belirti                                   | Çözüm                                                           |
|-------------------------------------------|-----------------------------------------------------------------|
| Konteyner oluşturma > 10 dk sürdü         | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal bağlanmadı; **+** ➜ *bash* tıklayın                    |
| OpenAI'den `401 Unauthorized`             | Yanlış / süresi dolmuş `OPENAI_API_KEY`                         |
| VS Code “Dev container mounting…” gösteriyor | Tarayıcı sekmesini yenileyin—Codespaces bazen bağlantıyı kaybediyor |
| Notebook çekirdeği eksik                  | Notebook menüsü ➜ **Kernel ▸ Select Kernel ▸ Python 3**         |

   Unix tabanlı sistemler:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` Dosyasını Düzenleyin**: `.env` dosyasını bir metin düzenleyicisinde (ör. VS Code, Notepad++ veya başka bir düzenleyici) açın. Dosyaya aşağıdaki satırı ekleyin ve `your_github_token_here` kısmını gerçek GitHub tokeninizle değiştirin:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Dosyayı Kaydedin**: Değişiklikleri kaydedin ve metin düzenleyiciyi kapatın.

5. **`python-dotenv` Kurun**: Henüz yapmadıysanız, `.env` dosyasından Python uygulamanıza ortam değişkenlerini yüklemek için `python-dotenv` paketini kurmanız gerekecek. `pip` kullanarak kurabilirsiniz:

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

İşte bu kadar! Başarıyla bir `.env` dosyası oluşturdunuz, GitHub tokeninizi eklediniz ve Python uygulamanıza yüklediniz.

## Bilgisayarınızda Yerel Olarak Çalıştırma

Kodları bilgisayarınızda yerel olarak çalıştırmak için, [Python'un bir sürümünü yüklemeniz](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) gerekecek.

Daha sonra depoyu kullanmak için, onu klonlamanız gerekecek:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Her şeyi kontrol ettikten sonra, başlayabilirsiniz!

## İsteğe Bağlı Adımlar

### Miniconda Kurulumu

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst), [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python ve birkaç paketi yüklemek için hafif bir yükleyicidir. Conda, farklı Python [**sanallaştırılmış ortamları**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ve paketleri kurmayı ve geçiş yapmayı kolaylaştıran bir paket yöneticisidir. Ayrıca `pip` aracılığıyla bulunamayan paketleri yüklemek için de kullanışlıdır.

[MiniConda kurulum kılavuzunu](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) takip ederek kurulum yapabilirsiniz.

Miniconda kurulduktan sonra, [depo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (henüz yapmadıysanız) klonlanmalıdır.

Sonrasında, bir sanal ortam oluşturmanız gerekecek. Conda ile bunu yapmak için yeni bir ortam dosyası (_environment.yml_) oluşturun. Codespaces kullanıyorsanız, bunu `.devcontainer` dizini içinde oluşturun, yani `.devcontainer/environment.yml`.

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

Eğer conda kullanırken hata alırsanız, Microsoft AI Kütüphanelerini manuel olarak aşağıdaki komutla bir terminalde kurabilirsiniz.

```
conda install -c microsoft azure-ai-ml
```

Ortam dosyası, ihtiyaç duyduğumuz bağımlılıkları belirtir. `<environment-name>` Conda ortamınız için kullanmak istediğiniz adı ve `<python-version>` Python'un kullanmak istediğiniz sürümünü ifade eder, örneğin, `3` Python'un en son ana sürümüdür.

Bunu yaptıktan sonra, aşağıdaki komutları komut satırında/terminalde çalıştırarak Conda ortamınızı oluşturabilirsiniz:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Herhangi bir sorunla karşılaşırsanız, [Conda ortamları kılavuzuna](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) başvurabilirsiniz.

### Python destek eklentisi ile Visual Studio Code kullanımı

Bu kurs için [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) düzenleyicisini, [Python destek eklentisi](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ile birlikte kullanmanızı öneririz. Ancak bu bir öneri olup kesin bir gereklilik değildir.

> **Not**: Kurs deposunu VS Code'da açarak projeyi bir konteyner içinde kurma seçeneğine sahip olursunuz. Bu, kurs deposunda bulunan [özel `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) dizini sayesinde mümkündür. Daha fazla bilgi için ilerleyen bölümlere bakabilirsiniz.

> **Not**: Depoyu klonlayıp VS Code'da açtığınızda, Python destek eklentisini yüklemenizi otomatik olarak önerecektir.

> **Not**: VS Code, depoyu bir konteyner içinde yeniden açmanızı önerirse, bu isteği reddedin ve yerel olarak yüklenmiş Python sürümünü kullanın.

### Tarayıcıda Jupyter Kullanımı

Projede [Jupyter ortamını](https://jupyter.org?WT.mc_id=academic-105485-koreyst) doğrudan tarayıcınızda kullanarak çalışabilirsiniz. Hem klasik Jupyter hem de [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst), otomatik tamamlama, kod vurgulama gibi özelliklerle oldukça hoş bir geliştirme ortamı sunar.

Jupyter'i yerel olarak başlatmak için terminal/komut satırına gidin, kurs dizinine gidin ve şu komutları çalıştırın:

```bash
jupyter notebook
```

veya

```bash
jupyterhub
```

Bu, bir Jupyter oturumu başlatacak ve erişim URL'si komut satırı penceresinde gösterilecektir.

URL'ye eriştiğinizde, kurs içeriğini görebilir ve herhangi bir `*.ipynb` dosyasına gidebilirsiniz. Örneğin, `08-building-search-applications/python/oai-solution.ipynb`.

### Bir konteynerde çalıştırma

Bilgisayarınızda veya Codespace'de her şeyi kurmanın alternatif bir yolu, bir [konteyner](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) kullanmaktır. Kurs deposundaki özel `.devcontainer` klasörü, VS Code'un projeyi bir konteyner içinde kurmasını mümkün kılar. Codespaces dışında, Docker'ın yüklenmesini gerektirir ve oldukça fazla iş gerektirir, bu yüzden bunu yalnızca konteynerlerle çalışma deneyimi olanlara öneriyoruz.

GitHub Codespaces kullanırken API anahtarlarınızı güvende tutmanın en iyi yollarından biri, Codespace Secrets kullanmaktır. Daha fazla bilgi edinmek için [Codespaces gizli anahtar yönetimi](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) kılavuzunu takip edin.

## Dersler ve Teknik Gereksinimler

Kurs, 6 kavramsal ders ve 6 kodlama dersi içermektedir.

Kodlama dersleri için Azure OpenAI Hizmeti'ni kullanıyoruz. Bu kodu çalıştırmak için Azure OpenAI hizmetine erişim ve bir API anahtarına ihtiyacınız olacak. Erişim almak için [bu başvuruyu tamamlayarak](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) başvurabilirsiniz.

Başvurunuzun işlenmesini beklerken, her kodlama dersi ayrıca kodu ve çıktıları görebileceğiniz bir `README.md` dosyası içermektedir.

## Azure OpenAI Hizmetini İlk Kez Kullanma

Azure OpenAI hizmetini ilk kez kullanıyorsanız, [Azure OpenAI Hizmeti kaynağı oluşturma ve dağıtma](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) kılavuzunu takip edin.

## OpenAI API'sini İlk Kez Kullanma

OpenAI API'sini ilk kez kullanıyorsanız, [Arayüz oluşturma ve kullanma](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) kılavuzunu takip edin.

## Diğer Öğrenenlerle Tanışın

Resmi [AI Community Discord sunucumuzda](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) diğer öğrenenlerle tanışmanız için kanallar oluşturduk. Bu, Üretken Yapay Zeka alanında kendini geliştirmek isteyen girişimciler, geliştiriciler, öğrenciler ve benzer düşünen kişilerle ağ kurmanın harika bir yoludur.

[![Discord kanalına katıl](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Proje ekibi de bu Discord sunucusunda öğrenenlere yardımcı olmak için bulunacak.

## Katkıda Bulunun

Bu kurs, açık kaynaklı bir girişimdir. İyileştirme veya sorun gördüğünüz alanlar varsa, lütfen bir [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) oluşturun veya bir [GitHub sorunu](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) bildirin.

Proje ekibi tüm katkıları takip edecektir. Açık kaynağa katkıda bulunmak, Üretken Yapay Zeka alanında kariyerinizi geliştirmek için harika bir yoldur.

Çoğu katkı, bir Katkıda Bulunan Lisans Sözleşmesi (CLA) imzalamanızı gerektirir. Bu sözleşme, bize katkınızı kullanma hakkı verdiğinizi ve bu hakka sahip olduğunuzu beyan eder. Ayrıntılar için [CLA, Katkıda Bulunan Lisans Sözleşmesi web sitesini](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) ziyaret edin.

Bir pull request gönderdiğinizde, bir CLA-bot otomatik olarak bir CLA sağlayıp sağlamanız gerekip gerekmediğini belirleyecek ve PR'ı uygun şekilde işaretleyecektir (örneğin, etiket, yorum). Bot tarafından sağlanan talimatları takip etmeniz yeterlidir. Bunu, CLA kullanan tüm depolar için yalnızca bir kez yapmanız gerekecek.

Bu proje, [Microsoft Açık Kaynak Davranış Kurallarını](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) benimsemiştir. Daha fazla bilgi için Davranış Kuralları SSS'yi okuyun veya [Email opencode](opencode@microsoft.com) adresine ek sorularınızı veya yorumlarınızı gönderin.

## Haydi Başlayalım
Bu kursu tamamlamak için gereken adımları tamamladığınıza göre, hadi [Üretken Yapay Zeka ve LLM'lere giriş](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) ile başlayalım.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmez.