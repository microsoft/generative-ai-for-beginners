<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T16:47:13+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "tr"
}
-->
# Yerel Kurulum 🖥️

**Her şeyi kendi bilgisayarınızda çalıştırmak istiyorsanız bu rehberi kullanın.**  
İki seçeneğiniz var: **(A) yerel Python + virtual-env** veya **(B) VS Code Dev Container ile Docker**.  
Hangisi size daha kolay geliyorsa onu seçin—ikisi de aynı derslere götürür.

## 1.  Gereksinimler

| Araç                | Sürüm / Notlar                                                                      |
|---------------------|-------------------------------------------------------------------------------------|
| **Python**          | 3.10 + (<https://python.org> adresinden edinebilirsiniz)                            |
| **Git**             | En güncel sürüm (Xcode / Git for Windows / Linux paket yöneticisi ile gelir)        |
| **VS Code**         | Opsiyonel ama önerilir <https://code.visualstudio.com>                              |
| **Docker Desktop**  | *Sadece* Seçenek B için. Ücretsiz kurulum: <https://docs.docker.com/desktop/>       |

> 💡 **İpucu** – Araçları terminalde doğrulayın:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Seçenek A – Yerel Python (en hızlısı)

### Adım 1  Bu repoyu klonlayın

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Adım 2 Sanal ortam oluşturun ve etkinleştirin

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Komut satırı artık (.venv) ile başlamalı—bu, ortamın içindesiniz demektir.

### Adım 3 Bağımlılıkları yükleyin

```bash
pip install -r requirements.txt
```

[API anahtarları](../../../00-course-setup) bölümüne geçin

## 2. Seçenek B – VS Code Dev Container (Docker)

Bu depo ve kursu, Python3, .NET, Node.js ve Java geliştirmeyi destekleyen Evrensel bir çalışma zamanı içeren bir [geliştirme konteyneri](https://containers.dev?WT.mc_id=academic-105485-koreyst) ile hazırladık. İlgili yapılandırma, bu deponun kökünde `.devcontainer/` klasöründe bulunan `devcontainer.json` dosyasında tanımlanmıştır.

>**Neden bunu seçmelisiniz?**
>Aynı ortamı Codespaces ile elde edersiniz; bağımlılık uyuşmazlığı olmaz.

### Adım 0 Ekstra araçları kurun

Docker Desktop – ```docker --version``` komutunun çalıştığını doğrulayın.
VS Code Remote – Containers eklentisi (ID: ms-vscode-remote.remote-containers).

### Adım 1 Repoyu VS Code’da açın

Dosya ▸ Klasör Aç…  → generative-ai-for-beginners

VS Code .devcontainer/ klasörünü algılar ve bir uyarı gösterir.

### Adım 2 Konteynerde yeniden açın

“Reopen in Container”a tıklayın. Docker imajı oluşturur (ilk seferde ≈ 3 dakika).
Terminalde komut satırı göründüğünde, artık konteynerin içindesiniz.

## 2.  Seçenek C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst), [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python ve birkaç paketi kurmak için hafif bir yükleyicidir.
Conda, farklı Python [**sanal ortamlarını**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ve paketleri kolayca kurup geçiş yapmanızı sağlayan bir paket yöneticisidir. Ayrıca, `pip` ile yüklenemeyen paketler için de kullanışlıdır.

### Adım 0  Miniconda’yı kurun

[MiniConda kurulum rehberini](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) takip ederek kurun.

```bash
conda --version
```

### Adım 1 Sanal ortam oluşturun

Yeni bir ortam dosyası oluşturun (*environment.yml*). Codespaces kullanıyorsanız, bunu `.devcontainer` dizininde oluşturun, yani `.devcontainer/environment.yml`.

### Adım 2  Ortam dosyanızı doldurun

Aşağıdaki kodu `environment.yml` dosyanıza ekleyin

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

### Adım 3 Conda ortamınızı oluşturun

Aşağıdaki komutları komut satırında/terminalde çalıştırın

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Herhangi bir sorun yaşarsanız [Conda ortamları rehberine](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) bakabilirsiniz.

## 2  Seçenek D – Klasik Jupyter / Jupyter Lab (tarayıcıda)

> **Kimler için?**  
> Klasik Jupyter arayüzünü sevenler veya VS Code olmadan notebook çalıştırmak isteyenler için.  

### Adım 1  Jupyter’ın kurulu olduğundan emin olun

Jupyter’ı yerel olarak başlatmak için terminale/komut satırına gidin, kurs dizinine geçin ve şunu çalıştırın:

```bash
jupyter notebook
```

veya

```bash
jupyterhub
```

Bu, bir Jupyter oturumu başlatır ve erişim URL’si komut satırında gösterilir.

URL’ye eriştiğinizde, kursun ana hatlarını görmeli ve istediğiniz herhangi bir `*.ipynb` dosyasına gidebilmelisiniz. Örneğin, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. API Anahtarlarınızı Ekleyin

Herhangi bir uygulama geliştirirken API anahtarlarınızı güvenli tutmak çok önemlidir. API anahtarlarını doğrudan kodunuza kaydetmemenizi öneririz. Bu bilgileri herkese açık bir depoya göndermek, güvenlik sorunlarına ve kötü niyetli kişiler tarafından kullanılırsa istenmeyen maliyetlere yol açabilir.
Python için `.env` dosyası oluşturma ve `GITHUB_TOKEN` ekleme adımlarını aşağıda bulabilirsiniz:

1. **Proje Dizininize Gidin**: Terminal veya komut istemcisini açın ve `.env` dosyasını oluşturmak istediğiniz proje kök dizinine gidin.

   ```bash
   cd path/to/your/project
   ```

2. **`.env` Dosyasını Oluşturun**: Tercih ettiğiniz metin düzenleyiciyle `.env` adında yeni bir dosya oluşturun. Komut satırı kullanıyorsanız, Unix tabanlı sistemlerde `touch`, Windows’ta ise `echo` kullanabilirsiniz:

   Unix tabanlı sistemler:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` Dosyasını Düzenleyin**: `.env` dosyasını bir metin düzenleyicide açın (ör. VS Code, Notepad++ veya başka bir editör). Aşağıdaki satırı dosyaya ekleyin, `your_github_token_here` kısmını kendi GitHub token’ınız ile değiştirin:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Dosyayı Kaydedin**: Değişiklikleri kaydedin ve editörü kapatın.

5. **`python-dotenv` Paketini Kurun**: Henüz kurmadıysanız, `.env` dosyasındaki ortam değişkenlerini Python uygulamanıza yüklemek için `python-dotenv` paketini kurmanız gerekir. `pip` ile kurabilirsiniz:

   ```bash
   pip install python-dotenv
   ```

6. **Python Script’inizde Ortam Değişkenlerini Yükleyin**: Python script’inizde, `.env` dosyasındaki ortam değişkenlerini yüklemek için `python-dotenv` paketini kullanın:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Hepsi bu kadar! Artık bir `.env` dosyası oluşturdunuz, GitHub token’ınızı eklediniz ve Python uygulamanıza yüklediniz.

🔐 .env dosyasını asla commit etmeyin—zaten .gitignore’da var.
Tüm sağlayıcı talimatları [`providers.md`](03-providers.md) dosyasında.

## 4. Sırada ne var?

| İstediğim…          | Git…                                                                  |
|---------------------|-----------------------------------------------------------------------|
| 1. Derse başla      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)   |
| LLM sağlayıcı kur   | [`providers.md`](03-providers.md)                                     |
| Diğer katılımcılarla tanış | [Discord’a katıl](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Sorun Giderme

| Belirti                                    | Çözüm                                                            |
|--------------------------------------------|------------------------------------------------------------------|
| `python not found`                         | Python’u PATH’e ekleyin veya kurulumdan sonra terminali yeniden açın |
| `pip` Windows’ta wheel oluşturamıyor       | `pip install --upgrade pip setuptools wheel` komutunu çalıştırıp tekrar deneyin. |
| `ModuleNotFoundError: dotenv`              | `pip install -r requirements.txt` çalıştırın (ortam kurulmamış). |
| Docker build başarısız *No space left*     | Docker Desktop ▸ *Ayarlar* ▸ *Kaynaklar* → disk boyutunu artırın.|
| VS Code sürekli yeniden açılmasını istiyor | İki seçeneği birden kullanıyor olabilirsiniz; birini seçin (venv **veya** container)|
| OpenAI 401 / 429 hataları                  | `OPENAI_API_KEY` değerini ve istek sınırlarını kontrol edin.      |
| Conda ile ilgili hatalar                   | Microsoft AI kütüphanelerini `conda install -c microsoft azure-ai-ml` ile kurun|

---

**Feragatname**:
Bu belge, yapay zeka çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerde hata veya yanlışlıklar bulunabilir. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından doğabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.