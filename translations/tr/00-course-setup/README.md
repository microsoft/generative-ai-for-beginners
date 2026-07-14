# Bu kursa Başlarken

Bu kursa başlamanız ve Generative AI ile neler yapmaya ilham alacağınızı görmeniz için çok heyecanlıyız!

Başarınızı sağlamak için, bu sayfa kurulum adımlarını, teknik gereksinimleri ve gerekirse nereden yardım alacağınızı özetlemektedir.

## Kurulum Adımları

Bu kursa başlamanız için aşağıdaki adımları tamamlamanız gerekecek.

### 1. Bu Depoyu Kopyalayın

[Bu tüm depoyu kopyalayın](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) kendi GitHub hesabınıza, böylece herhangi bir kodu değiştirebilir ve görevleri tamamlayabilirsiniz. Ayrıca [bu depoyu (🌟) yıldızlayabilirsiniz](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ve ilgili depoları daha kolay bulabilirsiniz.

### 2. Bir Codespace Oluşturun

Kodu çalıştırırken bağımlılık sorunlarından kaçınmak için bu kursu [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) içinde çalıştırmanızı öneririz.

Kopyanızda: **Code -> Codespaces -> Main üzerinde Yeni**

![Bir kod alanı oluşturmak için düğmeler gösteren iletişim kutusu](../../../translated_images/tr/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Bir gizli anahtar ekleyin

1. ⚙️ Dişli simgesi -> Komut Paleti -> Codespaces : Kullanıcı gizliliğini yönetin -> Yeni bir gizli anahtar ekle.
2. Ad olarak OPENAI_API_KEY yazın, anahtarınızı yapıştırın, Kaydedin.

### 3. Sonraki adım ne?

| Şunu yapmak istiyorum…    | Git…                                                                  |
|---------------------------|-------------------------------------------------------------------------|
| Ders 1’e başla            | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Çevrimdışı çalış          | [`setup-local.md`](02-setup-local.md)                                   |
| Bir LLM Sağlayıcısı Kur   | [`providers.md`](03-providers.md)                                        |
| Diğer öğrencilerle tanış  | [Discord’umuza Katıl](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Sorun Giderme


| Belirti                                   | Çözüm                                                           |
|-------------------------------------------|-----------------------------------------------------------------|
| Konteyner oluşturma 10 dakikadan fazla sürüyor | **Codespaces ➜ “Konteyneri Yeniden Oluştur”**                   |
| `python: command not found`               | Terminal bağlanmadı; **+** tıklayın ➜ *bash*                    |
| OpenAI’dan `401 Unauthorized` hatası      | Yanlış veya süresi dolmuş `OPENAI_API_KEY`                      |
| VS Code “Dev container mounting…” gösteriyor | Tarayıcı sekmesini yenileyin—Codespaces bazen bağlantısını kaybeder |
| Notebook çekirdeği eksik                   | Notebook menüsü ➜ **Kernel ▸ Çekirdeği Seç ▸ Python 3**           |

Unix tabanlı sistemler:

   ```bash
   touch .env
   ```

Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` Dosyasını Düzenleyin**: Bir metin editöründe (`VS Code`, `Notepad++` veya başka bir editör) `.env` dosyasını açın. Aşağıdaki satırları, gerçek Microsoft Foundry Modelleri uç noktası ve anahtarınız ile değiştirerek dosyaya ekleyin (detaylar için [`providers.md`](03-providers.md) sayfasına bakın):

> **Not:** GitHub Modelleri (ve `GITHUB_TOKEN` değişkeni), Temmuz 2026 sonunda emekliye ayrılıyor. Bunun yerine [Microsoft Foundry Modellerini](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) kullanın.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Dosyayı Kaydedin**: Değişiklikleri kaydedin ve metin editörünü kapatın.

5. **`python-dotenv` Paketini Kurun**: Henüz kurmadıysanız, `.env` dosyasındaki ortam değişkenlerini Python uygulamanıza yüklemek için `python-dotenv` paketini kurmanız gerekecek. `pip` kullanarak kurabilirsiniz:

   ```bash
   pip install python-dotenv
   ```

6. **Python Script’inizde Ortam Değişkenlerini Yükleyin**: Python script’inizde `python-dotenv` paketini kullanarak `.env` dosyasındaki ortam değişkenlerini yükleyin:

   ```python
   from dotenv import load_dotenv
   import os

   # .env dosyasından ortam değişkenlerini yükle
   load_dotenv()

   # Microsoft Foundry Modelleri değişkenlerine erişim sağla
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Hepsi bu kadar! Bir `.env` dosyası oluşturdunuz, Microsoft Foundry Modelleri kimlik bilgilerinizi eklediniz ve bunları Python uygulamanıza yüklediniz.

## Kendi bilgisayarınızda yerel olarak nasıl çalıştırılır

Kodu yerel olarak bilgisayarınızda çalıştırmak için bir sürüm [Python kurulu](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) olması gerekir.

Ardından depoyu kullanmak için klonlamanız gerekir:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Her şeyi kontrol ettikten sonra başlayabilirsiniz!

## İsteğe bağlı adımlar

### Miniconda Kurulumu

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst), [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python ve birkaç paketin kurulumu için hafif bir yükleyicidir.
Conda, farklı Python [**sanallaştırılmış ortamları**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ve paketleri kolayca kurmanıza ve arasında geçiş yapmanıza olanak sağlayan bir paket yöneticisidir. Ayrıca `pip` ile bulunmayan paketlerin kurulumu için de kullanışlıdır.

Kurulum için [Miniconda kurulum rehberini](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) takip edebilirsiniz.

Miniconda yüklendikten sonra, henüz yapmadıysanız depoyu [klonlamanız](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) gerekir.

Sonra bir sanal ortam oluşturmanız gerekir. Conda ile bunu yapmak için yeni bir ortam dosyası (_environment.yml_) oluşturun. Codespaces kullanıyorsanız, bunu `.devcontainer` dizini içinde oluşturun, yani `.devcontainer/environment.yml`.

Ortam dosyanızı aşağıdaki snippet ile doldurun:

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

Conda kullanırken hata alıyorsanız, Microsoft AI Kütüphanelerini manuel olarak terminalde aşağıdaki komutla kurabilirsiniz.

```
conda install -c microsoft azure-ai-ml
```

Ortam dosyası gerekli bağımlılıkları belirtir. `<environment-name>`, Conda ortamınız için kullanmak istediğiniz isim, `<python-version>` ise kullanmak istediğiniz Python sürümüdür, örneğin `3` Python’un en son ana sürümüdür.

Bunu yaptıktan sonra, aşağıdaki komutları komut satırında/terminalde çalıştırarak Conda ortamınızı oluşturabilirsiniz.

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer alt yolu sadece Codespace kurulumları için geçerlidir
conda activate ai4beg
```

Herhangi bir sorun yaşarsanız, [Conda ortamları rehberine](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) bakınız.

### Visual Studio Code’u Python destek uzantısıyla kullanma

Bu kurs için [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editörünü, [Python destek uzantısı](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) yüklenmiş olarak kullanmanızı öneririz. Ancak bu bir öneri olup kesin zorunluluk değildir.

> **Not**: Kurs deposunu VS Code’da açarak projeyi bir konteyner içinde ayarlama seçeneğiniz vardır. Bunun nedeni, kurs deposu içinde bulunan [özel `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) dizinidir. Bu konu daha sonra ayrıntılı anlatılacaktır.

> **Not**: Depoyu klonlayıp VS Code'da açtığınızda, otomatik olarak Python destek uzantısını kurmanızı önerecektir.

> **Not**: VS Code, depoyu bir konteyner içinde yeniden açmanızı önerirse, yerel kurulu Python sürümünü kullanmak için bu isteği reddedin.

### Tarayıcıda Jupyter kullanımı

Proje üzerinde, tarayıcınızda doğrudan [Jupyter ortamı](https://jupyter.org?WT.mc_id=academic-105485-koreyst) kullanarak da çalışabilirsiniz. Hem klasik Jupyter hem de [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst), otomatik tamamlama, kod vurgulama gibi özelliklerle oldukça hoş bir geliştirme ortamı sunar.

Yerel olarak Jupyter’i başlatmak için terminal veya komut satırına gidin, kurs dizinine geçin ve şu komutu yürütün:

```bash
jupyter notebook
```

veya

```bash
jupyterhub
```

Bu, bir Jupyter örneği başlatır ve erişim için URL komut satırında gösterilir.

URL'ye eriştiğinizde, kurs çerçevesini görmeli ve herhangi bir `*.ipynb` dosyasına gidebilmelisiniz. Örneğin, `08-building-search-applications/python/oai-solution.ipynb`.

### Konteynerde çalıştırma

Bilgisayarınıza veya Codespace'inize her şeyi kurmanın alternatifi olarak bir [konteyner](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) kullanabilirsiniz. Kurs deposunun içindeki özel `.devcontainer` klasörü, VS Code’un projeyi bir konteyner içinde kurmasını sağlar. Codespaces dışındaysanız, Docker kurulumu gerekir ve açıkçası biraz uğraş gerektirir, bu yüzden konteynerlerle deneyimi olanlara öneriyoruz.

GitHub Codespaces kullanırken API anahtarlarınızı güvende tutmanın en iyi yollarından biri Codespace Gizlilikleri kullanmaktır. Daha fazla bilgi için [Codespaces gizli yönetimi](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) rehberini takip edin.


## Dersler ve Teknik Gereksinimler

Kurs 6 kavramsal ders ve 6 kodlama dersi içeriyor.

Kodlama dersleri için Azure OpenAI Servisi kullanıyoruz. Bu kodu çalıştırmak için Azure OpenAI servisine erişiminiz ve bir API anahtarınız olmalı. [Başvuru yaparak](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) erişim talebinde bulunabilirsiniz.

Başvurunuz işlenirken, her kodlama dersi ayrıca kodları ve çıktıları görebileceğiniz bir `README.md` dosyası içerir.

## Azure OpenAI Servisini ilk kez kullanma

Azure OpenAI servisi ile ilk kez çalışıyorsanız, lütfen [Azure OpenAI Hizmet kaynağı oluşturma ve dağıtma](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) rehberini takip edin.

## OpenAI API’yi ilk kez kullanma

OpenAI API ile ilk kez çalışıyorsanız, lütfen [Arayüzü oluşturma ve kullanma](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) rehberini takip edin.

## Diğer Öğrencilerle Tanışın

Resmi [AI Topluluğu Discord sunucumuzda](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) diğer öğrencilerle tanışmanız için kanallar oluşturduk. Bu, aynı fikirdeki girişimciler, geliştiriciler, öğrenciler ve Generative AI alanında kendini geliştirmek isteyen herkesle ağ kurmak için harika bir yoldur.

[![Discord kanalına katıl](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Proje ekibi, bu Discord sunucusunda öğrencilere yardımcı olmak için de bulunacaktır.

## Katkıda Bulunun

Bu kurs açık kaynaklı bir girişimdir. Geliştirilmesi gereken yerler veya problemler görürseniz lütfen bir [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) oluşturun veya bir [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) kaydedin.

Proje ekibi tüm katkıları takip edecektir. Açık kaynak projelere katkıda bulunmak, Generative AI alanında kariyerinizi geliştirmek için harika bir yoldur.

Çoğu katkı için, gönderiminizin haklarına sahip olduğunuzu ve bu hakları bize verdiğinizi belirten bir Katkıda Bulunan Lisans Anlaşması’na (CLA) kabul etmeniz gerekir. Ayrıntılar için [CLA, Katkıda Bulunan Lisans Anlaşması sitesini](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) ziyaret edin.

Önemli: Bu depoda metin çevirisi yaparken lütfen makine çevirisi kullanmayın. Topluluk tarafından çeviriler doğrulanacaktır, bu yüzden yalnızca iyi bildiğiniz diller için gönüllü olun.

Bir pull request gönderdiğinizde, CLA-bot otomatik olarak CLA sağlayıp sağlamanız gerektiğini ve PR'yi uygun şekilde (örneğin, etiket, yorum ile) süsleyip süslemeyeceğini belirleyecektir. Botun verdiği talimatları takip edin. CLA işlemi, bizden CLA isteyen tüm depolarda yalnızca bir kez yapılır.


Bu proje [Microsoft Açık Kaynak Davranış Kuralları](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) benimsenmiştir. Daha fazla bilgi için Davranış Kuralları SSS bölümünü okuyabilir veya ek sorularınız ya da yorumlarınız için [Email opencode](opencode@microsoft.com) ile iletişime geçebilirsiniz.

## Hadi Başlayalım

Bu kursu tamamlamak için gerekli adımları tamamladığınıza göre, [Yaratıcı Yapay Zeka ve LLM'lere giriş](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) ile başlayalım.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->