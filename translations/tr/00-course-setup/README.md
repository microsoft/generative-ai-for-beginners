<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T16:47:57+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "tr"
}
-->
# Bu kursa Başlarken

Bu kursa başlaman ve Üretken Yapay Zeka ile neler inşa edeceğini görmek için çok heyecanlıyız!

Başarılı olman için, bu sayfada kurulum adımları, teknik gereksinimler ve ihtiyaç duyarsan nereden yardım alabileceğin anlatılıyor.

## Kurulum Adımları

Bu kursa başlamak için aşağıdaki adımları tamamlaman gerekiyor.

### 1. Bu Depoyu Fork'la

Herhangi bir kodu değiştirebilmek ve görevleri tamamlayabilmek için [bu tüm depoyu kendi GitHub hesabına fork'la](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst). Ayrıca, [bu depoyu yıldızlayarak (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) hem bu depoyu hem de ilgili depoları daha kolay bulabilirsin.

### 2. Bir codespace oluştur

Kodları çalıştırırken bağımlılık sorunları yaşamamak için, bu kursu [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) üzerinde çalıştırmanı öneriyoruz.

Kendi fork'unda: **Code -> Codespaces -> New on main**

![Codespace oluşturma butonlarını gösteren diyalog](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Bir gizli anahtar ekle

1. ⚙️ Dişli simgesi -> Komut Paleti -> Codespaces : Manage user secret -> Yeni bir gizli anahtar ekle.
2. İsim olarak OPENAI_API_KEY yaz, anahtarını yapıştır, Kaydet.

### 3.  Sırada ne var?

| Şunu yapmak istiyorum… | Şuraya git…                                                                |
|------------------------|-----------------------------------------------------------------------------|
| 1. Dersi başlat        | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)         |
| Çevrimdışı çalışmak    | [`setup-local.md`](02-setup-local.md)                                       |
| Bir LLM Sağlayıcı kurmak | [`providers.md`](providers.md)                                            |
| Diğer katılımcılarla tanışmak | [Discord'a katıl](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Sorun Giderme

| Belirti                                    | Çözüm                                                            |
|---------------------------------------------|------------------------------------------------------------------|
| Konteyner kurulumu 10 dakikadan uzun sürüyor| **Codespaces ➜ “Rebuild Container”**                             |
| `python: command not found`                 | Terminal bağlanmamış; **+** ➜ *bash* tıkla                       |
| OpenAI'dan `401 Unauthorized`               | Yanlış / süresi dolmuş `OPENAI_API_KEY`                          |
| VS Code “Dev container mounting…” gösteriyor| Tarayıcı sekmesini yenile—Codespaces bazen bağlantıyı kaybediyor |
| Notebook çekirdeği eksik                    | Notebook menüsü ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Unix tabanlı sistemler:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` Dosyasını Düzenle**: `.env` dosyasını bir metin düzenleyicide (ör. VS Code, Notepad++ veya başka bir editör) aç. Aşağıdaki satırı dosyaya ekle, `your_github_token_here` kısmını kendi GitHub token'ın ile değiştir:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Dosyayı Kaydet**: Değişiklikleri kaydet ve metin editörünü kapat.

5. **`python-dotenv` Kurulumu**: Henüz kurmadıysan, `.env` dosyasındaki ortam değişkenlerini Python uygulamana yüklemek için `python-dotenv` paketini kurman gerekir. `pip` ile kurabilirsin:

   ```bash
   pip install python-dotenv
   ```

6. **Python Scriptinde Ortam Değişkenlerini Yükle**: Python scriptinde, `.env` dosyasındaki ortam değişkenlerini yüklemek için `python-dotenv` paketini kullan:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Hepsi bu kadar! Başarıyla bir `.env` dosyası oluşturdun, GitHub token'ını ekledin ve Python uygulamana yükledin.

## Kendi Bilgisayarında Yerel Olarak Çalıştırma

Kodları kendi bilgisayarında çalıştırmak için, [Python'un bir sürümünün kurulu olması](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) gerekir.

Depoyu kullanmak için, önce klonlaman gerekir:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Her şeyi indirdikten sonra, hemen başlayabilirsin!

## Opsiyonel Adımlar

### Miniconda Kurulumu

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst), [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python ve birkaç paketi kurmak için hafif bir kurucudur.
Conda'nın kendisi bir paket yöneticisidir ve farklı Python [**sanallaştırılmış ortamlar**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ve paketler arasında kolayca geçiş yapmanı sağlar. Ayrıca, `pip` ile bulunmayan paketleri kurmak için de kullanışlıdır.

Kurmak için [MiniConda kurulum rehberini](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) takip edebilirsin.

Miniconda kurulduktan sonra, [depo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)'yu klonlaman gerekir (henüz yapmadıysan).

Sonrasında, bir sanal ortam oluşturman gerekir. Conda ile bunu yapmak için yeni bir ortam dosyası (_environment.yml_) oluştur. Codespaces kullanıyorsan, bunu `.devcontainer` dizininde oluştur, yani `.devcontainer/environment.yml`.

Aşağıdaki kod parçası ile ortam dosyanı doldurabilirsin:

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

Eğer conda kullanırken hata alırsan, Microsoft AI Kütüphanelerini aşağıdaki komutla terminalden manuel olarak kurabilirsin.

```
conda install -c microsoft azure-ai-ml
```

Ortam dosyası, ihtiyacımız olan bağımlılıkları belirtir. `<environment-name>` Conda ortamına vermek istediğin isim, `<python-version>` ise kullanmak istediğin Python sürümüdür; örneğin, `3` en güncel ana sürümdür.

Bunları yaptıktan sonra, aşağıdaki komutları komut satırında/terminalde çalıştırarak Conda ortamını oluşturabilirsin:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Herhangi bir sorun yaşarsan [Conda ortamları rehberine](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) göz atabilirsin.

### Python desteğiyle Visual Studio Code kullanmak

Bu kurs için [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editörünü ve [Python destek eklentisini](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) kullanmanı öneriyoruz. Ancak bu bir öneri, zorunluluk değil.

> **Not**: Kurs deposunu VS Code'da açtığında, projeyi bir konteyner içinde kurma seçeneğin olur. Bunun nedeni, kurs deposunda bulunan [özel `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) dizinidir. Buna daha sonra değineceğiz.

> **Not**: Depoyu klonlayıp VS Code'da açtığında, otomatik olarak Python destek eklentisini kurmanı önerecektir.

> **Not**: VS Code, depoyu bir konteynerde yeniden açmanı önerirse, yerel Python sürümünü kullanmak için bu isteği reddet.

### Tarayıcıda Jupyter Kullanmak

Projede [Jupyter ortamını](https://jupyter.org?WT.mc_id=academic-105485-koreyst) doğrudan tarayıcında da kullanabilirsin. Hem klasik Jupyter hem de [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst), otomatik tamamlama, kod vurgulama gibi özelliklerle oldukça keyifli bir geliştirme ortamı sunar.

Jupyter'ı yerel olarak başlatmak için terminal/komut satırına git, kurs dizinine geç ve şunu çalıştır:

```bash
jupyter notebook
```

veya

```bash
jupyterhub
```

Bu, bir Jupyter oturumu başlatır ve erişim için URL'yi komut satırında gösterir.

URL'ye eriştiğinde, kursun içeriğini görebilir ve istediğin herhangi bir `*.ipynb` dosyasına gidebilirsin. Örneğin, `08-building-search-applications/python/oai-solution.ipynb`.

### Bir konteynerde çalıştırmak

Her şeyi bilgisayarında veya Codespace'te kurmak yerine, [konteyner](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>) kullanabilirsin. Kurs deposundaki özel `.devcontainer` klasörü, VS Code'un projeyi bir konteynerde kurmasını sağlar. Codespaces dışında, bunun için Docker kurulumu gerekir ve biraz uğraştırıcı olabilir, bu yüzden konteynerlerle deneyimi olanlara öneriyoruz.

GitHub Codespaces kullanırken API anahtarlarını güvenli tutmanın en iyi yollarından biri Codespace Secrets kullanmaktır. Daha fazla bilgi için [Codespaces secrets yönetimi](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) rehberini inceleyebilirsin.

## Dersler ve Teknik Gereksinimler

Kurs 6 kavramsal ders ve 6 kodlama dersi içeriyor.

Kodlama derslerinde Azure OpenAI Servisi kullanıyoruz. Bu kodu çalıştırmak için Azure OpenAI servisine erişimin ve bir API anahtarın olması gerekiyor. [Bu başvuruyu tamamlayarak](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) erişim talebinde bulunabilirsin.

Başvurunun işlenmesini beklerken, her kodlama dersinde kodu ve çıktıları görebileceğin bir `README.md` dosyası da bulunuyor.

## Azure OpenAI Servisini ilk kez kullanmak

Azure OpenAI servisini ilk kez kullanıyorsan, [Azure OpenAI Servis kaynağı oluşturma ve dağıtma](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) rehberini takip et.

## OpenAI API'sini ilk kez kullanmak

OpenAI API'sini ilk kez kullanıyorsan, [Arayüz oluşturma ve kullanma rehberini](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) takip et.

## Diğer Katılımcılarla Tanış

Resmi [AI Community Discord sunucumuzda](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) diğer katılımcılarla tanışabileceğin kanallar oluşturduk. Bu, benzer düşünen girişimciler, geliştiriciler, öğrenciler ve Üretken Yapay Zeka'da kendini geliştirmek isteyen herkesle ağ kurmak için harika bir yol.

[![Discord kanalına katıl](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Proje ekibi de bu Discord sunucusunda olacak ve katılımcılara yardımcı olacak.

## Katkıda Bulun

Bu kurs açık kaynaklı bir girişimdir. Geliştirilmesi gereken veya sorunlu gördüğün alanlar varsa, lütfen bir [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) oluştur veya bir [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) bildir.

Proje ekibi tüm katkıları takip edecek. Açık kaynağa katkı sağlamak, Üretken Yapay Zeka alanında kariyerini geliştirmek için harika bir yoldur.

Çoğu katkı, Katılımcı Lisans Sözleşmesi'ni (CLA) kabul etmeni gerektirir. Bu, katkını kullanma hakkına sahip olduğunu ve bu hakkı bize verdiğini beyan eder. Detaylar için [CLA, Katılımcı Lisans Sözleşmesi web sitesini](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) ziyaret et.

Önemli: Bu depodaki metinleri çevirirken, makine çevirisi kullanmadığından emin ol. Çeviriler topluluk tarafından doğrulanacaktır, bu yüzden yalnızca yetkin olduğun dillerde çeviri gönüllüsü ol.

Pull request gönderdiğinde, bir CLA-bot otomatik olarak CLA gerekip gerekmediğini belirleyecek ve PR'ı uygun şekilde işaretleyecek (ör. etiket, yorum). Botun verdiği talimatları takip etmen yeterli. Bunu, CLA kullanan tüm depolarda yalnızca bir kez yapman gerekir.

Bu proje [Microsoft Açık Kaynak Davranış Kuralları'nı](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) benimsemiştir. Daha fazla bilgi için Davranış Kuralları SSS'yi oku veya ek soruların/yorumların için [Email opencode](opencode@microsoft.com) ile iletişime geç.

## Haydi Başlayalım
Artık bu kursu tamamlamak için gereken adımları tamamladığınıza göre, [Üretken Yapay Zeka ve Büyük Dil Modellerine giriş](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) ile başlayalım.

---

**Feragatname**:  
Bu belge, yapay zeka çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerde hata veya yanlışlıklar bulunabilir. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından doğabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.