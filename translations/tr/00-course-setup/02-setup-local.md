# Yerel Kurulum 🖥️

**Her şeyi kendi dizüstü bilgisayarınızda çalıştırmayı tercih ediyorsanız bu rehberi kullanın.**   
İki yolunuz var: **(A) yerel Python + virtual-env** veya **(B) Docker ile VS Code Geliştirme Konteyneri**.  
Hangisi daha kolay gelirse onu seçin—ikisi de aynı derslere götürür.

## 1. Önkoşullar

| Araç               | Sürüm / Notlar                                                                        |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (<https://python.org> adresinden edinin)                                      |
| **Git**            | En son sürüm (Xcode / Windows için Git / Linux paket yöneticisi ile gelir)            |
| **VS Code**        | Opsiyonel ama tavsiye edilir <https://code.visualstudio.com>                         |
| **Docker Desktop** | *Sadece* Seçenek B için. Ücretsiz kurulum: <https://docs.docker.com/desktop/>        |

> 💡 **İpucu** – Araçları terminalden doğrulayın:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Seçenek A – Yerel Python (en hızlı)

### Adım 1 Bu repoyu klonlayın

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Adım 2 Sanal ortam oluşturun ve etkinleştirin

```bash
python -m venv .venv          # bir tane yap
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Komut satırı şimdi (.venv) ile başlamalı—bu, ortamın içinde olduğunuz anlamına gelir.

### Adım 3 Bağımlılıkları yükleyin

```bash
pip install -r requirements.txt
```

[API anahtarları](#3-api-anahtarlarınızı-ekleyin) bölümüne geçin

## 2. Seçenek B – VS Code Geliştirme Konteyneri (Docker)

Bu depo ve kurs, Python3, .NET, Node.js ve Java geliştirmeyi destekleyen Evrensel çalışma zamanı olan bir [geliştirme konteyneri](https://containers.dev?WT.mc_id=academic-105485-koreyst) ile kuruldu. İlgili yapılandırma, bu deponun kökündeki `.devcontainer/` klasöründe bulunan `devcontainer.json` dosyasında tanımlanmıştır.

>**Neden bunu seçmelisiniz?**
>Codespaces ile aynı ortam; bağımlılık kayması yok.

### Adım 0 Ekstraları yükleyin

Docker Desktop – ```docker --version``` çalıştığını doğrulayın.
VS Code Remote – Containers uzantısı (ID: ms-vscode-remote.remote-containers).

### Adım 1 Repoyu VS Code'da açın

Dosya ▸ Klasör Aç… → generative-ai-for-beginners

VS Code `.devcontainer/` klasörünü algılar ve bir açılır pencere gösterir.

### Adım 2 Konteyner içinde tekrar açın

“Konteyner içinde tekrar aç”a tıklayın. Docker imajı oluşturur (ilk sefer yaklaşık 3 dk).
Terminal istemi görünce konteyner içindesiniz demektir.

## 2. Seçenek C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst), [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python ve bazı paketleri yüklemek için hafif bir yükleyicidir.
Conda, farklı Python [**sanal ortamlarını**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ve paketleri kurmayı ve aralarında geçiş yapmayı kolaylaştıran bir paket yöneticisidir. Ayrıca `pip` ile yüklenemeyen paketler için çok işe yarar.

### Adım 0 Miniconda'yı yükleyin

Kurmak için [MiniConda kurulum kılavuzunu](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) izleyin.

```bash
conda --version
```

### Adım 1 Bir sanal ortam oluşturun

Yeni bir ortam dosyası oluşturun (*environment.yml*). Codespaces kullanıyorsanız, bunu `.devcontainer` dizini içinde oluşturun, yani `.devcontainer/environment.yml`.

### Adım 2 Ortam dosyanızı doldurun

Aşağıdaki parçayı `environment.yml` dosyanıza ekleyin

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

Komut satırı/terminalde aşağıdaki komutları çalıştırın

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer alt yolu yalnızca Codespace kurulumlarına uygulanır
conda activate ai4beg
```

Herhangi bir sorunla karşılaşırsanız [Conda ortamları rehberine](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) bakabilirsiniz.

## 2 Seçenek D – Klasik Jupyter / Jupyter Lab (tarayıcınızda)

> **Kimler için?**  
> Klasik Jupyter arayüzünü seven veya defterleri VS Code olmadan çalıştırmak isteyen herkes için.  

### Adım 1 Jupyter'in kurulu olduğundan emin olun

Jupyter’i yerel başlatmak için terminal/komut satırına gidin, kurs dizinine geçin ve şu komutu çalıştırın:

```bash
jupyter notebook
```

veya

```bash
jupyterhub
```

Bu, bir Jupyter örneği başlatacak ve erişim için URL, komut satırı penceresinde gösterilecektir.

URL'ye eriştiğinizde kurs dökümünü görmeli ve herhangi bir `*.ipynb` dosyasına gidebilmelisiniz. Örnek olarak, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. API Anahtarlarınızı Ekleyin

API anahtarlarınızı güvenli tutmak, herhangi bir uygulama geliştirirken önemlidir. API anahtarlarını doğrudan kodunuzda saklamamanızı öneririz. Bu ayrıntıların herkese açık bir depoya yüklenmesi güvenlik sorunlarına ve kötü niyetli kullanım halinde istenmeyen maliyetlere yol açabilir.
İşte Python için bir `.env` dosyası oluşturup Microsoft Foundry Modelleri kimlik bilgilerinizi nasıl ekleyeceğinize dair adım adım rehber:

> **Not:** GitHub Modelleri (ve `GITHUB_TOKEN` değişkeni) Temmuz 2026 sonunda kullanımdan kalkacaktır. Bu rehber bunun yerine [Microsoft Foundry Modelleri](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) kullanır. Tamamen çevrimdışı çalışmak mı istiyorsunuz? [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) adresine bakın.

1. **Proje Dizinize Gidin**: Terminal veya komut istemcisini açın ve `.env` dosyasını oluşturmak istediğiniz projenizin kök dizinine gidin.

   ```bash
   cd path/to/your/project
   ```

2. **`.env` Dosyasını Oluşturun**: Tercih ettiğiniz metin düzenleyiciyle `.env` adlı yeni dosya oluşturun. Komut satırı kullanıyorsanız, Unix tabanlı sistemlerde `touch` veya Windows’ta `echo` kullanabilirsiniz:

   Unix tabanlı sistemler:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` Dosyasını Düzenleyin**: `.env` dosyasını bir metin düzenleyicide (örneğin, VS Code, Notepad++ veya başka bir düzenleyici) açın. Aşağıdaki satırları, yer tutucuları gerçek Microsoft Foundry proje uç noktası ve API anahtarınızla değiştirerek ekleyin:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Dosyayı Kaydedin**: Değişiklikleri kaydedin ve metin düzenleyiciyi kapatın.

5. **`python-dotenv` Yükleyin**: Henüz yüklemediyseniz, `.env` dosyasındaki ortam değişkenlerini Python uygulamanıza yüklemek için `python-dotenv` paketini kurmanız gerekir. Bunu `pip` ile yükleyebilirsiniz:

   ```bash
   pip install python-dotenv
   ```

6. **Python Scriptinizde Ortam Değişkenlerini Yükleyin**: Python scriptinizde, `.env` dosyasındaki ortam değişkenlerini yüklemek için `python-dotenv` paketini kullanın:

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

İşte bu kadar! `.env` dosyası oluşturdunuz, Microsoft Foundry Modelleri kimlik bilgilerinizi eklediniz ve Python uygulamanıza yüklediniz.

🔐 `.env` dosyasını asla commit etmeyin—zaten `.gitignore` içinde.
Sağlayıcıya özel talimatlar [`providers.md`](03-providers.md) dosyasında mevcut.

## 4. Sonraki Adım?

| Ne yapmak istiyorum…  | Gitmek istediğim yer…                                                   |
|---------------------|-------------------------------------------------------------------------|
| Ders 1'e başla       | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Bir LLM Sağlayıcısı Kur | [`providers.md`](03-providers.md)                                       |
| Diğer öğrenenlerle tanış | [Discordımıza Katıl](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Sorun Giderme

| Belirti                                 | Çözüm                                                             |
|-----------------------------------------|-----------------------------------------------------------------|
| `python bulunamadı`                     | Python'u PATH'e ekleyin veya kurulumu takiben terminali yeniden açın |
| `pip` tekerlekler oluşturamıyor (Windows) | `pip install --upgrade pip setuptools wheel` komutunu çalıştırıp tekrar deneyin. |
| `ModuleNotFoundError: dotenv`           | `pip install -r requirements.txt` çalıştırın (ortam kurulmamış).  |
| Docker build hatası *Boş alan kalmadı* | Docker Desktop ▸ *Ayarlar* ▸ *Kaynaklar* → disk boyutunu artırın.  |
| VS Code sürekli yeniden açma isteği     | Her iki seçeneği birden etkin olabilir; birini seçin (venv **veya** konteyner) |
| OpenAI 401 / 429 hataları                | `OPENAI_API_KEY` değerini ve istek oran limitlerini kontrol edin.  |
| Conda kullanırken hatalar                | Microsoft AI kitaplıklarını `conda install -c microsoft azure-ai-ml` ile yükleyin |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->