# Bu kursa başlamak

Bu kursa başlamanız ve Üretken Yapay Zeka ile neler yaratacağınız konusunda ilham almanızı görmek için çok heyecanlıyız!

Başarınızı sağlamak için, bu sayfa kurulum adımlarını, teknik gereksinimleri ve gerektiğinde nereden yardım alabileceğinizi özetlemektedir.

## Kurulum Adımları

Bu kursa başlamanız için aşağıdaki adımları tamamlamanız gerekmektedir.

### 1. Bu Depoyu Forklayın

[Tüm bu depoyu forkladığınız GitHub hesabınıza](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) kodları değiştirebilmek ve görevleri tamamlayabilmek için. Ayrıca, [bu depoya 🌟 yıldıza basarak](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ve ilgili depolara daha kolay erişebilirsiniz.

### 2. Bir Codespace Oluşturun

Kodu çalıştırırken bağımlılık sorunlarından kaçınmak için bu kursu bir [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) içinde çalıştırmanızı öneririz.

Forkunuzda: **Code -> Codespaces -> New on main**

![Bir codespace oluşturmak için düğmeleri gösteren iletişim kutusu](../../../translated_images/tr/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Bir gizli anahtar ekleyin

1. ⚙️ Dişli simgesi -> Komut Paleti -> Codespaces: Kullanıcı gizli anahtarını yönet -> Yeni gizli anahtar ekle.
2. Ad olarak OPENAI_API_KEY yazın, anahtarınızı yapıştırın, Kaydet.

### 3. Sonra ne olacak?

| Yapmak istiyorum…       | Gitmek istediğim yer…                                                   |
|------------------------|------------------------------------------------------------------------|
| Ders 1’e başla         | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Çevrimdışı çalış        | [`setup-local.md`](02-setup-local.md)                                   |
| Bir LLM Sağlayıcısı Ayarla | [`providers.md`](03-providers.md)                                        |
| Diğer öğrencilerle tanış | [Discord’umuza katıl](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Sorun Giderme

| Belirti                                        | Çözüm                                                              |
|------------------------------------------------|-------------------------------------------------------------------|
| Konteyner yapımı 10 dakikadan uzun sürüyorsa   | **Codespaces ➜ “Rebuild Container” (Konteyneri Yeniden İnşa Et)** |
| `python: command not found` hatası alırsanız    | Terminal bağlanmamış; **+** → *bash* tıklayın                      |
| OpenAI’dan `401 Unauthorized` hatası alırsanız | Yanlış veya süresi dolmuş `OPENAI_API_KEY`                         |
| VS Code “Dev container mounting…” gösteriyorsa | Tarayıcı sekmesini yenileyin — Codespaces bazen bağlantıyı kaybedebilir |
| Notebook çekirdeği eksikse                       | Notebook menüsü ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix tabanlı sistemler:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` Dosyasını Düzenleyin**: `.env` dosyasını bir metin düzenleyicide (ör. VS Code, Notepad++ veya başka bir editör) açın. Dosyaya aşağıdaki satırı ekleyin, `your_github_token_here` kısmını gerçek GitHub tokenınızla değiştirin:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Dosyayı Kaydedin**: Değişiklikleri kaydedin ve metin düzenleyiciyi kapatın.

5. **`python-dotenv` Paketini Yükleyin**: Henüz yüklemediyseniz, `.env` dosyasındaki ortam değişkenlerini Python uygulamanıza yüklemek için `python-dotenv` paketini yükleyin. Bunu `pip` ile yükleyebilirsiniz:

   ```bash
   pip install python-dotenv
   ```

6. **Python Kodunuzda Ortam Değişkenlerini Yükleyin**: Python scriptinizde `.env` dosyasından ortam değişkenlerini yüklemek için `python-dotenv` paketini kullanın:

   ```python
   from dotenv import load_dotenv
   import os

   # .env dosyasından ortam değişkenlerini yükle
   load_dotenv()

   # GITHUB_TOKEN değişkenine eriş
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

İşte bu kadar! Başarıyla bir `.env` dosyası oluşturdunuz, GitHub tokenınızı eklediniz ve Python uygulamanıza yüklediniz.

## Kodunuzu Bilgisayarınızda Yerel Olarak Çalıştırma

Kodunuzu bilgisayarınızda yerel olarak çalıştırmak için [Python’un bir sürümünün yüklü olması gerekir](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Depoyu kullanmak için, onu klonlamanız gerekir:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Her şeyi hallettikten sonra başlamaya hazırsınız!

## İsteğe Bağlı Adımlar

### Miniconda Kurulumu

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst), [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python ve bazı paketleri kurmak için hafif bir yükleyicidir. Conda kendisi, farklı Python [**sanal ortamlarını**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ve paketleri kurup yönetmeyi kolaylaştıran bir paket yöneticisidir. Ayrıca `pip` ile bulunmayan paketlerin kurulumu için faydalıdır.

Kurulum için [MiniConda kurulum rehberini](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) takip edebilirsiniz.

Miniconda yüklüyse, [depoyu](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) klonlayın (henüz yapmadıysanız).

Sonra bir sanal ortam oluşturmanız gerekir. Conda ile bunu yapmak için yeni bir ortam dosyası oluşturun (_environment.yml_). Codespaces kullanıyorsanız, bunu `.devcontainer` dizini içinde, yani `.devcontainer/environment.yml` olarak oluşturun.

Ortam dosyanızı aşağıdaki örnekle doldurun:

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

Conda kullanırken hata alırsanız, Microsoft AI Kütüphanelerini el ile terminalde aşağıdaki komutla yükleyebilirsiniz.

```
conda install -c microsoft azure-ai-ml
```

Ortam dosyası ihtiyaç duyulan bağımlılıkları belirler. `<environment-name>` Conda ortamı için kullanmak istediğiniz isim, `<python-version>` kullanmak istediğiniz Python sürümüdür, örneğin `3` Python’un en son büyük sürümüdür.

Bununla, aşağıdaki komutları terminalinizde çalıştırarak Conda ortamınızı oluşturabilirsiniz:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer alt yolu yalnızca Codespace kurulumu için geçerlidir
conda activate ai4beg
```

Herhangi bir sorun yaşarsanız, [Conda ortam rehberine](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) bakabilirsiniz.

### Visual Studio Code ve Python destek eklentisini kullanmak

Bu kurs için [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editörü ve [Python destek uzantısı](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) kullanmanızı öneririz. Ancak bu bir zorunluluk değil, bir öneridir.

> **Not**: Kurs deposunu VS Code’da açarsanız, projeyi bir konteyner içinde kurmayı seçebilirsiniz. Bunun sebebi, kurs deposunun içinde bulunan [özel `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) dizinidir. Buna daha sonra değineceğiz.

> **Not**: Depoyu klonlayıp VS Code’da açtığınızda Python destek uzantısı yüklemenizi otomatik önerir.

> **Not**: VS Code depoyu bir konteyner içinde açmayı önerirse, yerel Python sürümünü kullanmak için bu teklifi reddedin.

### Tarayıcıda Jupyter Kullanmak

Proje üzerinde ayrıca tarayıcınız içinde bulunan [Jupyter ortamını](https://jupyter.org?WT.mc_id=academic-105485-koreyst) kullanarak da çalışabilirsiniz. Hem klasik Jupyter hem de [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) otomatik tamamlama, kod vurgulama gibi özelliklerle oldukça keyifli bir geliştirme ortamı sunar.

Jupyter’ı yerelde çalıştırmak için terminale gidip kurs dizinine geçtikten sonra şunu çalıştırın:

```bash
jupyter notebook
```

ya da

```bash
jupyterhub
```

Bu, bir Jupyter örneğini başlatır ve erişim URL’si komut satırı penceresinde gösterilir.

URL’ye eriştiğinizde kurs içeriği görünmeli ve herhangi bir `*.ipynb` dosyasına gidebilmelisiniz. Örneğin, `08-building-search-applications/python/oai-solution.ipynb`.

### Bir konteynerde çalıştırmak

Her şeyi bilgisayarınızda veya Codespace üzerinde kurmak yerine [konteyner](https://en.wikipedia.org/wiki/Containerization_%28computing%29?WT.mc_id=academic-105485-koreyst) kullanabilirsiniz. Kurs deposundaki özel `.devcontainer` klasörü, VS Code’un projeyi bir konteyner içinde kurmasını sağlar. Codespaces dışında bunu yapmak için Docker kurulumu şarttır ve biraz uğraş gerektirir; bu yüzden konteynerle çalışmaya deneyimli olanlara öneririz.

GitHub Codespaces kullanırken API anahtarlarınızı güvende tutmanın en iyi yollarından biri Codespaces Secrets kullanmaktır. Daha fazla bilgi için [Codespaces gizli anahtar yönetimi](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) rehberini takip edin.

## Dersler ve Teknik Gereksinimler

Kurs, 6 kavramsal ders ve 6 kodlama dersinden oluşur.

Kodlama dersleri için Azure OpenAI Servisi kullanıyoruz. Bu kodu çalıştırmak için Azure OpenAI servisine erişim ve bir API anahtarı gereklidir. Erişim almak için [bu başvuruyu tamamlayarak](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) talepte bulunabilirsiniz.

Başvurunuz işlenirken, her kodlama dersi içinde kodları ve çıktılarını görebileceğiniz bir `README.md` dosyası da yer alır.

## Azure OpenAI Servisini ilk kez kullanıyorsanız

Azure OpenAI servisi ile ilk kez çalışıyorsanız, [Azure OpenAI Hizmet Kaynağı oluşturma ve dağıtma](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) rehberini takip edin.

## OpenAI API’yi ilk kez kullanıyorsanız

OpenAI API ile ilk kez çalışıyorsanız, [Arabirim oluşturma ve kullanma](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) rehberini izleyin.

## Diğer Öğrencilerle Tanışın

Resmi [AI Community Discord sunucumuzda](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) diğer öğrencilerle tanışmak için kanallar açtık. Bu, ortak düşünen girişimciler, geliştiriciler, öğrenciler ve Üretken Yapay Zeka’da gelişmek isteyen herkesle network kurmak için harika bir fırsat.

[![Discord kanalına katıl](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Proje ekibi de bu Discord sunucusunda öğrencilerin sorularını yanıtlamak için olacak.

## Katkıda Bulunmak

Bu ders açık kaynak bir girişimdir. İyileştirme alanları veya sorunlar görürseniz, lütfen [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) oluşturun veya bir [GitHub sorunu](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) kaydedin.

Proje ekibi tüm katkıları takip edecek. Açık kaynak katkısı, Üretken Yapay Zeka alanında kariyer inşa etmek için harika bir yoldur.

Çoğu katkı için, katkınızı kullanma hakkı verdiğinizi beyan eden bir Katkı Lisansı Anlaşması’na (CLA) uymanız gerekir. Ayrıntılar için [CLA, Katkı Lisansı Anlaşması websitesine](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) bakabilirsiniz.

Önemli: Bu depoda metin çevirirken, lütfen makine çevirisi kullanmayın. Topluluk tarafından çeviriler doğrulanacaktır, bu nedenle yalnızca iyi bildiğiniz dillerde çeviri gönüllüsü olun.

Pull request gönderdiğinizde, CLA-bot otomatik olarak CLA gerekip gerekmediğini kontrol edecek ve PR’yı uygun şekilde etiketleyecek (örneğin, etiket, yorum). Botun talimatlarını izleyin. Tüm depolarda CLA uygulaması için bunu yalnızca bir kez yapmanız yeterlidir.

Bu proje [Microsoft Açık Kaynak Davranış Kuralları](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) ile uyumludur. Daha fazla bilgi için Davranış Kuralları SSS’yı okuyun veya ek sorularınız için [Email opencode](opencode@microsoft.com) ile iletişime geçin.

## Haydi Başlayalım
Bu kursu tamamlamak için gereken adımları tamamladığınıza göre, [Generatif Yapay Zeka ve LLM'lere giriş](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) ile başlayalım.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi tavsiye edilmektedir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek herhangi bir yanlış anlama veya yorum hatasından sorumlu olmayız.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->