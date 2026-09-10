# Bu kursa Başlarken

Bu kursa başlamanız ve Üretken AI ile neler yaratmaya ilham aldığınızı görmeniz için çok heyecanlıyız!

Başarınızı sağlamak için, bu sayfada kurulum adımları, teknik gereksinimler ve gerektiğinde nereden yardım alabileceğiniz anlatılmaktadır.

## Kurulum Adımları

Bu kursa başlamak için aşağıdaki adımları tamamlamanız gerekmektedir.

### 1. Bu Depoyu Fork’layın

Herhangi bir kodu değiştirebilmek ve görevleri tamamlayabilmek için [bu tüm depoyu](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) kendi GitHub hesabınıza fork’layın. Ayrıca, bu depoyu ve ilgili depoları daha kolay bulabilmek için [yıldız (🌟) basarak](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) işaretleyebilirsiniz.

### 2. Bir codespace oluşturun

Kodu çalıştırırken herhangi bir bağımlılık sorunu yaşamamak için bu kursu [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) içinde çalıştırmanızı öneririz.

Fork’unuzda: **Code -> Codespaces -> New on main**

![Codespace oluşturma butonlarını gösteren dialog](../../../translated_images/tr/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Bir gizli anahtar ekleyin

1. ⚙️ Dişli simgesi -> Komut Paleti -> Codespaces : Kullanıcı gizli anahtarını yönet -> Yeni bir gizli anahtar ekle.
2. Adı OPENAI_API_KEY olarak belirleyin, anahtarınızı yapıştırın, Kaydet.

### 3. Sonra ne var?

| Şunu yapmak istiyorum... | Şuraya git...                                                             |
|-------------------------|-------------------------------------------------------------------------|
| Ders 1’i başlatmak      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Çevrimdışı çalışmak     | [`setup-local.md`](02-setup-local.md)                                   |
| Bir LLM Sağlayıcısı kurmak | [`providers.md`](03-providers.md)                                        |
| Diğer öğrenenlerle tanışmak | [Discord’a Katıl](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Sorun Giderme


| Belirti                                      | Çözüm                                                          |
|---------------------------------------------|----------------------------------------------------------------|
| Container yapımı 10 dakikadan uzun sürüyor   | **Codespaces ➜ “Rebuild Container”**                           |
| `python: command not found`                   | Terminal bağlanmadı; **+** tuşuna tıklayın ➜ *bash*             |
| OpenAI’den `401 Unauthorized` hatası         | Yanlış veya süresi dolmuş `OPENAI_API_KEY`                      |
| VS Code “Dev container mounting…” gösteriyor | Tarayıcı sekmesini yenileyin—Codespaces bazen bağlantıyı kaybeder |
| Notebook çekirdeği eksik                       | Notebook menüsü ➜ **Kernel ▸ Select Kernel ▸ Python 3**         |

   Unix tabanlı sistemlerde:

   ```bash
   touch .env
   ```

   Windows’da:

   ```cmd
   echo . > .env
   ```

3. **`.env` Dosyasını Düzenleyin**: `.env` dosyasını bir metin editöründe (örneğin VS Code, Notepad++ ya da başka bir editör) açın. Aşağıdaki satırları dosyaya, yer tutucuları gerçek Microsoft Foundry Modeller uç noktası ve anahtarınızla değiştirerek ekleyin (bu bilgileri edinmek için [`providers.md`](03-providers.md) dosyasına bakabilirsiniz):

   > **Not:** GitHub Modelleri (ve `GITHUB_TOKEN` değişkeni) Temmuz 2026 sonunda kullanımdan kaldırılacak. Bunun yerine [Microsoft Foundry Modellerini](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) kullanın.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Dosyayı Kaydedin**: Değişiklikleri kaydedin ve metin editörünü kapatın.

5. **`python-dotenv` Paketini Kurun**: Henüz yapmadıysanız, `.env` dosyasından ortam değişkenlerini Python uygulamanıza yüklemek için `python-dotenv` paketini kurmanız gerekecek. Bunu `pip` ile kurabilirsiniz:

   ```bash
   pip install python-dotenv
   ```

6. **Python Script’inde Ortam Değişkenlerini Yükleyin**: Python script’inizde, `.env` dosyasından ortam değişkenlerini yüklemek için `python-dotenv` paketini kullanın:

   ```python
   from dotenv import load_dotenv
   import os

   # .env dosyasından ortam değişkenlerini yükle
   load_dotenv()

   # Microsoft Foundry Modelleri değişkenlerine erişim
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Hepsi bu kadar! Başarıyla bir `.env` dosyası oluşturdunuz, Microsoft Foundry Modelleri kimlik bilgilerinizi eklediniz ve bunları Python uygulamanıza yüklediniz.

## Kendi bilgisayarınızda yerel olarak nasıl çalıştırılır

Kodu kendi bilgisayarınızda yerel olarak çalıştırmak için bir sürüm [Python kurulu olmalıdır](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Daha sonra depoyu kullanmak için klonlamanız gerekir:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Her şeyi tamamladıktan sonra başlayabilirsiniz!

## İsteğe Bağlı Adımlar

### Miniconda Kurulumu

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst), [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python ve birkaç paketi kurmak için hafif bir yükleyicidir.
Conda, farklı Python [**sanal ortamları**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ve paketleri kolayca kurup değiştirmeyi sağlayan bir paket yöneticisidir. Ayrıca `pip` ile bulunmayan paketlerin kurulumu için de kullanışlıdır.

[MiniConda kurulum rehberini](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) takip ederek kurulum yapabilirsiniz.

Miniconda kurulduktan sonra, [depo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (eğer daha önce klonlamadıysanız) klonlanmalıdır.

Ardından bir sanal ortam oluşturmanız gerekir. Conda ile bunu yapmak için yeni bir ortam dosyası (_environment.yml_) oluşturun. Codespaces kullanıyorsanız, bunu `.devcontainer` dizini içinde oluşturun, yani `.devcontainer/environment.yml`.

Ortam dosyanızı aşağıdaki parçayla doldurun:

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

Eğer conda kullanırken hatalar alıyorsanız, Microsoft AI Kütüphanelerini terminalde aşağıdaki komutla manuel olarak kurabilirsiniz.

```
conda install -c microsoft azure-ai-ml
```

Ortam dosyası gerekli bağımlılıkları belirtir. `<environment-name>` Conda ortamınız için seçtiğiniz ad, `<python-version>` ise kullanmak istediğiniz Python sürümüdür; örneğin `3` Python’un en son ana sürümüdür.

Bu işlemi tamamladıktan sonra, aşağıdaki komutları komut satırınızda/terminalinizde çalıştırarak Conda ortamınızı oluşturabilirsiniz

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer alt yolu sadece Codespace kurulumları için geçerlidir
conda activate ai4beg
```

Herhangi bir sorunla karşılaşırsanız, [Conda ortamları rehberine](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) başvurabilirsiniz.

### Python desteği uzantısıyla Visual Studio Code kullanımı

Bu kurs için, [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editörünü ve [Python desteği uzantısını](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) kullanmanızı öneririz. Ancak bu sadece bir öneridir, zorunlu değildir.

> **Not**: Kurs deposunu VS Code’da açtığınızda, projeyi bir konteyner içinde kurma seçeneğiniz olur. Bunun sebebi kursta bulunan özel [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) klasörüdür. Bu konuya daha sonra değinilecektir.

> **Not**: Depoyu klonlayıp VS Code’da açtığınızda, otomatik olarak bir Python desteği uzantısı kurmanızı önerecektir.

> **Not**: VS Code size deposu bir konteyner içinde yeniden açmanızı önerirse, bu isteği reddedin; böylece yerel Python sürümünü kullanabilirsiniz.

### Tarayıcıda Jupyter kullanımı

Projeyi tarayıcınızda doğrudan kullanabileceğiniz [Jupyter ortamı](https://jupyter.org?WT.mc_id=academic-105485-koreyst) da vardır. Hem klasik Jupyter hem de [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) otomatik tamamlama, kod vurgulama gibi oldukça kullanışlı geliştirme ortamları sunar.

Yerelde Jupyter başlatmak için terminal/komut satırına gidin, kurs klasörüne geçin ve çalıştırın:

```bash
jupyter notebook
```

veya

```bash
jupyterhub
```

Bu, bir Jupyter örneği başlatacak ve erişim URL’si komut satırı penceresinde gösterilecektir.

URL’ye eriştiğinizde kurs içeriğini görmeli ve herhangi bir `*.ipynb` dosyasına gidebilmelisiniz. Örneğin, `08-building-search-applications/python/oai-solution.ipynb`.

### Bir konteyner içinde çalıştırma

Bilgisayarınızda veya Codespace’de her şeyi kurmanın alternatif yolu bir [konteyner kullanmaktır](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Kurs deposundaki özel `.devcontainer` klasörü, VS Code’un projeyi konteyner içinde kurmasını sağlar. Codespaces dışında bu, Docker kurulumu gerektirir ve biraz zahmetlidir; bu yüzden konteynerlerle deneyimi olanlara öneriyoruz.

GitHub Codespaces kullanırken API anahtarlarınızı güvenli tutmanın en iyi yollarından biri Codespace Secrets’ı kullanmaktır. Bunu öğrenmek için [Codespaces gizli yönetimi](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) rehberini takip edin.


## Dersler ve Teknik Gereksinimler

Kursta, Üretken AI kavramlarını açıklayan "Öğren" dersleri ve mümkün oldukça **Python** ve **TypeScript** ile uygulamalı kod örnekleri içeren "Inşa Et" dersleri vardır.

Kodlama dersleri için Microsoft Foundry’de Azure OpenAI kullanıyoruz. Bir Azure aboneliği ve API anahtarına ihtiyacınız olacak. Erişim açıktır—başvuru gerekmez—böylece [Microsoft Foundry kaynağı oluşturup model dağıtabilirsiniz](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) ve uç noktası ile anahtarınızı alabilirsiniz.

Her kodlama dersi ayrıca kodu çalıştırmadan da kodu ve çıktıları görüntüleyebileceğiniz bir `README.md` dosyasına sahiptir.

## Azure OpenAI Servisini ilk kez kullanma

Azure OpenAI servisini ilk kez kullanıyorsanız, lütfen [bir Azure OpenAI Servis kaynağı nasıl oluşturulur ve dağıtılır](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) rehberini takip edin.

## OpenAI API’yi ilk kez kullanma

OpenAI API’yı ilk kez kullanıyorsanız, lütfen [arayüzü nasıl oluşturup kullanacağınıza](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) dair rehberi takip edin.

## Diğer Öğrenenlerle Tanışın

Resmi [AI Topluluğu Discord sunucumuzda](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) diğer öğrenenlerle tanışmak için kanallar oluşturduk. Bu, Generative AI seviyenizi artırmak isteyen girişimciler, geliştiriciler, öğrenciler ve benzer düşünen insanlarla ağ kurmanın harika bir yoludur.

[![Discord kanalına katıl](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Proje ekibi de bu Discord sunucusunda öğrenenlere yardımcı olacaktır.

## Katkıda Bulunma

Bu kurs açık kaynaklı bir girişimdir. İyileştirme alanları veya sorunlar görürseniz, lütfen bir [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) oluşturun veya bir [GitHub sorunu](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) kaydedin.

Proje ekibi tüm katkıları takip etmektedir. Açık kaynağa katkıda bulunmak, Üretken AI alanında kariyerinizi geliştirmek için mükemmel bir yoldur.

Çoğu katkı için, katkınızın kullanılma hakkını bize verdiğinizi beyan eden bir Katılımcı Lisans Sözleşmesi’ni (CLA) kabul etmeniz gerekir. Ayrıntılar için [CLA, Katılımcı Lisans Sözleşmesi web sitesine](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) bakınız.

Önemli: Bu depoda metin çevirisi yaparken lütfen makine çevirisi kullanmayınız. Çevirileri toplum tarafından doğrulayacağız, bu nedenle yalnızca iyi bildiğiniz dillerde gönüllü olunuz.


Bir pull request gönderdiğinizde, bir CLA-botu otomatik olarak bir CLA sağlamanız gerekip gerekmediğini belirleyecek ve PR'ı uygun şekilde süsleyecektir (örneğin, etiket, yorum). Yalnızca bot tarafından verilen talimatları izleyin. CLA'mızı kullanan tüm depolar genelinde bunu yalnızca bir kez yapmanız yeterlidir.

Bu proje [Microsoft Açık Kaynak Davranış Kuralları](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) uygulanmıştır. Daha fazla bilgi için Davranış Kuralları SSS bölümünü okuyun veya ek sorularınız ya da yorumlarınız için [Email opencode](opencode@microsoft.com) ile iletişime geçin.

## Haydi Başlayalım

Bu kursu tamamlamak için gerekli adımları tamamladığınıza göre, şimdi [Üretici Yapay Zeka ve LLM'lere Giriş](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) ile başlayalım.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->