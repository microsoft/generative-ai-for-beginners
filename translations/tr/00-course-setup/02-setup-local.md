<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5cf0b10ab3c485e6334101f5784f1f3",
  "translation_date": "2025-12-19T14:58:33+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "tr"
}
-->
# Yerel Kurulum 🖥️

**Her şeyi kendi dizüstü bilgisayarınızda çalıştırmayı tercih ediyorsanız bu kılavuzu kullanın.**  
İki yolunuz var: **(A) yerel Python + virtual-env** veya **(B) Docker ile VS Code Geliştirme Konteyneri**.  
Hangisi daha kolay geliyorsa onu seçin—ikisi de aynı derslere götürür.

## 1.  Ön Koşullar

| Araç               | Sürüm / Notlar                                                                      |
|--------------------|------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (<https://python.org> adresinden alın)                                      |
| **Git**            | En son sürüm (Xcode / Windows için Git / Linux paket yöneticisi ile gelir)          |
| **VS Code**        | İsteğe bağlı ama önerilir <https://code.visualstudio.com>                           |
| **Docker Desktop** | *Sadece* Seçenek B için. Ücretsiz kurulum: <https://docs.docker.com/desktop/>      |

> 💡 **İpucu** – Araçları terminalde doğrulayın:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Seçenek A – Yerel Python (en hızlı)

### Adım 1  Bu repoyu klonlayın

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

✅ Komut istemi artık (.venv) ile başlamalı—bu, ortamın içinde olduğunuz anlamına gelir.

### Adım 3 Bağımlılıkları yükleyin

```bash
pip install -r requirements.txt
```

[API anahtarları](../../../00-course-setup) bölümüne geçin

## 2. Seçenek B – VS Code Geliştirme Konteyneri (Docker)

Bu depo ve kurs, Python3, .NET, Node.js ve Java geliştirmeyi destekleyen Evrensel bir çalışma zamanı içeren bir [geliştirme konteyneri](https://containers.dev?WT.mc_id=academic-105485-koreyst) ile ayarlandı. İlgili yapılandırma, bu deponun kök dizinindeki `.devcontainer/` klasöründe bulunan `devcontainer.json` dosyasında tanımlanmıştır.

>**Neden bunu seçmelisiniz?**  
>Codespaces ile aynı ortam; bağımlılık sürüklenmesi yok.

### Adım 0 Ekstraları yükleyin

Docker Desktop – ```docker --version``` komutunun çalıştığını doğrulayın.  
VS Code Remote – Containers eklentisi (ID: ms-vscode-remote.remote-containers).

### Adım 1 Repoyu VS Code’da açın

Dosya ▸ Klasör Aç…  → generative-ai-for-beginners

VS Code `.devcontainer/` klasörünü algılar ve bir istem çıkarır.

### Adım 2 Konteyner içinde yeniden açın

“Reopen in Container”a tıklayın. Docker imajı oluşturur (ilk sefer ≈ 3 dk).  
Terminal istemi göründüğünde konteyner içindesiniz demektir.

## 2.  Seçenek C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst), [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python ve birkaç paketi kurmak için hafif bir yükleyicidir.  
Conda, farklı Python [**sanal ortamları**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ve paketler arasında kolayca geçiş yapmayı sağlayan bir paket yöneticisidir. Ayrıca `pip` ile bulunmayan paketleri kurmak için de kullanışlıdır.

### Adım 0  Miniconda’yı yükleyin

Kurulum için [MiniConda kurulum kılavuzunu](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) takip edin.

```bash
conda --version
```

### Adım 1 Sanal ortam oluşturun

Yeni bir ortam dosyası oluşturun (*environment.yml*). Codespaces kullanıyorsanız, bunu `.devcontainer` dizini içinde, yani `.devcontainer/environment.yml` olarak oluşturun.

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

Aşağıdaki komutları komut satırınızda/terminalinizde çalıştırın

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer alt yolu yalnızca Codespace kurulumları için geçerlidir
conda activate ai4beg
```

Herhangi bir sorun yaşarsanız [Conda ortamları kılavuzuna](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) bakabilirsiniz.

## 2  Seçenek D – Klasik Jupyter / Jupyter Lab (tarayıcınızda)

> **Kimler için?**  
> Klasik Jupyter arayüzünü seven veya not defterlerini VS Code olmadan çalıştırmak isteyen herkes.

### Adım 1  Jupyter’ın kurulu olduğundan emin olun

Jupyter’ı yerel başlatmak için terminale/komut satırına gidin, kurs dizinine geçin ve şu komutu çalıştırın:

```bash
jupyter notebook
```

veya

```bash
jupyterhub
```

Bu, bir Jupyter örneği başlatacak ve erişim URL’si komut satırı penceresinde gösterilecektir.

URL’ye eriştiğinizde kurs içeriğini görmeli ve herhangi bir `*.ipynb` dosyasına gidebilmelisiniz. Örneğin, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. API Anahtarlarınızı Ekleyin

Herhangi bir uygulama geliştirirken API anahtarlarınızı güvenli tutmak önemlidir. API anahtarlarını doğrudan kodunuzda saklamamanızı öneririz. Bu bilgileri herkese açık bir depoya göndermek güvenlik sorunlarına ve kötü niyetli kişiler tarafından kullanılması durumunda istenmeyen maliyetlere yol açabilir.  
Python için bir `.env` dosyası oluşturma ve `GITHUB_TOKEN` ekleme adım adım rehberi:

1. **Proje Dizininize Gidin**: Terminal veya komut istemcisini açın ve `.env` dosyasını oluşturmak istediğiniz projenizin kök dizinine gidin.

   ```bash
   cd path/to/your/project
   ```

2. **`.env` Dosyasını Oluşturun**: Tercih ettiğiniz metin düzenleyici ile `.env` adlı yeni bir dosya oluşturun. Komut satırı kullanıyorsanız, Unix tabanlı sistemlerde `touch`, Windows’ta `echo` kullanabilirsiniz:

   Unix tabanlı sistemler:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` Dosyasını Düzenleyin**: `.env` dosyasını bir metin düzenleyicide (örneğin VS Code, Notepad++ veya başka bir editör) açın. Aşağıdaki satırı dosyaya ekleyin, `your_github_token_here` kısmını gerçek GitHub tokenınızla değiştirin:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Dosyayı Kaydedin**: Değişiklikleri kaydedin ve metin düzenleyiciyi kapatın.

5. **`python-dotenv` Paketini Yükleyin**: Henüz yüklemediyseniz, `.env` dosyasından ortam değişkenlerini Python uygulamanıza yüklemek için `python-dotenv` paketini yüklemeniz gerekir. Bunu `pip` ile yapabilirsiniz:

   ```bash
   pip install python-dotenv
   ```

6. **Python Scriptinizde Ortam Değişkenlerini Yükleyin**: Python scriptinizde, `.env` dosyasından ortam değişkenlerini yüklemek için `python-dotenv` paketini kullanın:

   ```python
   from dotenv import load_dotenv
   import os

   # .env dosyasından ortam değişkenlerini yükle
   load_dotenv()

   # GITHUB_TOKEN değişkenine eriş
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Hepsi bu! Başarıyla bir `.env` dosyası oluşturdunuz, GitHub tokenınızı eklediniz ve Python uygulamanıza yüklediniz.

🔐 `.env` dosyasını asla commit etmeyin—zaten `.gitignore` içinde.  
Tüm sağlayıcı talimatları [`providers.md`](03-providers.md) dosyasında bulunur.

## 4. Sonraki Adımlar?

| Yapmak istiyorum…   | Gitmek istediğim yer…                                                    |
|---------------------|-------------------------------------------------------------------------|
| Ders 1’e başla      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Bir LLM Sağlayıcısı Kur | [`providers.md`](03-providers.md)                                       |
| Diğer öğrenenlerle tanış | [Discord’umuza katıl](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Sorun Giderme

| Belirti                                   | Çözüm                                                             |
|-------------------------------------------|------------------------------------------------------------------|
| `python not found`                        | Python’u PATH’e ekleyin veya kurulum sonrası terminali yeniden açın |
| `pip` tekerlekleri oluşturamıyor (Windows) | `pip install --upgrade pip setuptools wheel` komutunu çalıştırıp tekrar deneyin. |
| `ModuleNotFoundError: dotenv`             | `pip install -r requirements.txt` komutunu çalıştırın (ortam kurulmamış). |
| Docker build başarısız *No space left*    | Docker Desktop ▸ *Ayarlar* ▸ *Kaynaklar* → disk boyutunu artırın. |
| VS Code sürekli yeniden açmayı öneriyor   | Her iki Seçenek de aktif olabilir; birini seçin (venv **veya** konteyner) |
| OpenAI 401 / 429 hataları                  | `OPENAI_API_KEY` değerini ve istek hız sınırlarını kontrol edin.  |
| Conda kullanırken hatalar                   | Microsoft AI kütüphanelerini `conda install -c microsoft azure-ai-ml` ile yükleyin |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->