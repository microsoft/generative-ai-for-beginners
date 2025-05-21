<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:48:04+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "tr"
}
-->
# Geliştirme Ortamınızı Kurun

Bu depo ve kursu, Python3, .NET, Node.js ve Java geliştirmesini destekleyebilen Evrensel bir çalışma zamanı içeren bir [geliştirme konteyneri](https://containers.dev?WT.mc_id=academic-105485-koreyst) ile kurduk. İlgili yapılandırma, bu deponun kökündeki `.devcontainer/` klasöründe bulunan `devcontainer.json` dosyasında tanımlanmıştır.

Geliştirme konteynerini etkinleştirmek için, [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (bulut barındırmalı çalışma zamanı için) veya [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (yerel cihaz barındırmalı çalışma zamanı için) içinde başlatın. Geliştirme konteynerlerinin VS Code içinde nasıl çalıştığı hakkında daha fazla bilgi için [bu dokümanı](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) okuyun.  

> [!TIP]  
> Minimum çaba ile hızlı bir başlangıç için GitHub Codespaces kullanmanızı öneririz. Kişisel hesaplar için cömert bir [ücretsiz kullanım kotası](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) sunar. Kotanızı en iyi şekilde kullanmak için [zaman aşımı ayarlarını](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) yapılandırarak etkin olmayan codespaces'leri durdurun veya silin.


## 1. Ödevleri Çalıştırma

Her ders, Python, .NET/C#, Java ve JavaScript/TypeScript gibi bir veya daha fazla programlama dilinde sağlanabilecek _isteğe bağlı_ ödevler içerecektir. Bu bölüm, bu ödevlerin nasıl yürütüleceğine dair genel rehberlik sağlar.

### 1.1 Python Ödevleri

Python ödevleri, uygulamalar (`.py` dosyaları) veya Jupyter defterleri (`.ipynb` dosyaları) olarak sağlanır. 
- Defteri çalıştırmak için, Visual Studio Code'da açın ve ardından _Çekirdek Seç_ (sağ üstte) seçeneğine tıklayın ve gösterilen varsayılan Python 3 seçeneğini seçin. Artık defteri çalıştırmak için _Tümünü Çalıştır_ seçeneğini kullanabilirsiniz.
- Komut satırından Python uygulamalarını çalıştırmak için, doğru dosyaları seçtiğinizden ve gerekli argümanları sağladığınızdan emin olmak için ödev özel talimatlarını izleyin.

## 2. Sağlayıcıları Yapılandırma

Ödevler, OpenAI, Azure veya Hugging Face gibi desteklenen bir hizmet sağlayıcısı aracılığıyla bir veya daha fazla Büyük Dil Modeli (LLM) dağıtımına karşı çalışacak şekilde **ayarlanabilir**. Bunlar, doğru kimlik bilgileri (API anahtarı veya token) ile programlı olarak erişebileceğimiz bir _barındırılan uç nokta_ (API) sağlar. Bu kursta, bu sağlayıcıları tartışıyoruz:

 - Çeşitli modelleri içeren temel GPT serisi ile [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst).
 - Kurumsal hazırlık odaklı OpenAI modelleri için [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)
 - Açık kaynak modeller ve çıkarım sunucusu için [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)

**Bu egzersizler için kendi hesaplarınızı kullanmanız gerekecek**. Ödevler isteğe bağlıdır, bu nedenle ilgi alanlarınıza göre birini, hepsini veya hiçbirini kurmayı seçebilirsiniz. Kayıt için bazı rehberlik:

| Kayıt | Maliyet | API Anahtarı | Oyun Alanı | Yorumlar |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Fiyatlandırma](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Proje bazlı](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Kodsuz, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Çeşitli Modeller Mevcut |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Fiyatlandırma](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Hızlı Başlangıç](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Stüdyo Hızlı Başlangıç](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Erişim İçin Önceden Başvurulmalı](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Fiyatlandırma](https://huggingface.co/pricing) | [Erişim Tokenları](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat sınırlı modellere sahiptir](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Aşağıdaki yönergeleri izleyerek bu depoyu farklı sağlayıcılarla kullanmak üzere _yapılandırın_. Belirli bir sağlayıcı gerektiren ödevler, dosya adlarında bu etiketlerden birini içerecektir:
 - `aoai` - Azure OpenAI uç noktası, anahtar gerektirir
 - `oai` - OpenAI uç noktası, anahtar gerektirir
 - `hf` - Hugging Face tokenı gerektirir

Bir, hiçbiri veya tüm sağlayıcıları yapılandırabilirsiniz. İlgili ödevler, eksik kimlik bilgileri nedeniyle hata verecektir.

###  2.1. `.env` Dosyası Oluşturun

Yukarıdaki rehberi okuduğunuzu ve ilgili sağlayıcıya kaydolduğunuzu ve gerekli kimlik doğrulama bilgilerini (API_KEY veya token) edindiğinizi varsayıyoruz. Azure OpenAI durumunda, en az bir GPT modeli konuşma tamamlaması için dağıtılmış bir Azure OpenAI Hizmeti (uç noktası) dağıtımına da sahip olduğunuzu varsayıyoruz.

Bir sonraki adım, **yerel ortam değişkenlerinizi** aşağıdaki gibi yapılandırmaktır:


1. Aşağıdaki gibi içeriklere sahip olması gereken bir `.env.copy` dosyası için kök klasöre bakın:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Bu dosyayı aşağıdaki komutu kullanarak `.env` dosyasına kopyalayın. Bu dosya _gitignore-d_'dır, bu da sırları güvende tutar.

   ```bash
   cp .env.copy .env
   ```

3. Değerleri (sağ taraftaki `=` işaretinin yer tutucularını değiştirin) bir sonraki bölümde açıklandığı gibi doldurun.

3. (Seçenek) GitHub Codespaces kullanıyorsanız, ortam değişkenlerini bu depo ile ilişkili _Codespaces secrets_ olarak kaydetme seçeneğiniz vardır. Bu durumda, yerel bir .env dosyası kurmanız gerekmez. **Ancak, bu seçeneğin yalnızca GitHub Codespaces kullanıyorsanız çalıştığını unutmayın.** Docker Desktop kullanıyorsanız yine de .env dosyasını kurmanız gerekecektir.


### 2.2. `.env` Dosyasını Doldurun

Değişken adlarının neyi temsil ettiğini anlamak için hızlıca bir göz atalım:

| Değişken  | Açıklama  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Profilinizde ayarladığınız kullanıcı erişim tokenıdır |
| OPENAI_API_KEY | Azure dışı OpenAI uç noktaları için hizmeti kullanma yetki anahtarıdır |
| AZURE_OPENAI_API_KEY | Bu hizmeti kullanma yetki anahtarıdır |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI kaynağı için dağıtılmış uç noktadır |
| AZURE_OPENAI_DEPLOYMENT | Bu _metin oluşturma_ modeli dağıtım uç noktasıdır |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Bu _metin yerleştirmeleri_ modeli dağıtım uç noktasıdır |
| | |

Not: Son iki Azure OpenAI değişkeni, sırasıyla sohbet tamamlama (metin oluşturma) ve vektör arama (yerleştirmeler) için varsayılan bir modeli yansıtır. Bunları ayarlama talimatları ilgili ödevlerde tanımlanacaktır.


### 2.3 Azure'u Yapılandırma: Portal'dan

Azure OpenAI uç noktası ve anahtar değerleri [Azure Portalı](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) içinde bulunacaktır, bu yüzden oradan başlayalım.

1. [Azure Portalı](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) adresine gidin.
1. Kenar çubuğundaki (sol menüdeki) **Anahtarlar ve Uç Nokta** seçeneğine tıklayın.
1. **Anahtarları Göster** seçeneğine tıklayın - aşağıdaki gibi görmelisiniz: ANAHTAR 1, ANAHTAR 2 ve Uç Nokta.
1. AZURE_OPENAI_API_KEY için ANAHTAR 1 değerini kullanın.
1. AZURE_OPENAI_ENDPOINT için Uç Nokta değerini kullanın.

Sonraki adımda, dağıttığımız belirli modeller için uç noktalar gereklidir.

1. Azure OpenAI kaynağı için kenar çubuğundaki (sol menüdeki) **Model dağıtımları** seçeneğine tıklayın.
1. Hedef sayfada, **Dağıtımları Yönet** seçeneğine tıklayın.

Bu, Azure OpenAI Studio web sitesine götürecektir, burada aşağıda açıklanan diğer değerleri bulacağız.

### 2.4 Azure'u Yapılandırma: Studio'dan

1. [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) adresine **kaynağınızdan** yukarıda açıklandığı gibi gidin.
1. Şu anda dağıtılmış modelleri görüntülemek için **Dağıtımlar** sekmesine (kenar çubuğu, sol) tıklayın.
1. İstediğiniz model dağıtılmamışsa, onu dağıtmak için **Yeni dağıtım oluştur** seçeneğini kullanın.
1. Bir _metin oluşturma_ modeli gerekecektir - önerimiz: **gpt-35-turbo**
1. Bir _metin yerleştirme_ modeli gerekecektir - önerimiz **text-embedding-ada-002**

Şimdi ortam değişkenlerini kullanılan _Dağıtım adı_ yansıtacak şekilde güncelleyin. Bu genellikle model adıyla aynı olacaktır, ancak açıkça değiştirmediyseniz. Öyleyse, bir örnek olarak, şunlara sahip olabilirsiniz:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**İşiniz bittiğinde .env dosyasını kaydetmeyi unutmayın**. Şimdi dosyadan çıkabilir ve defteri çalıştırma talimatlarına dönebilirsiniz.

### 2.5 OpenAI'yi Yapılandırma: Profil'den

OpenAI API anahtarınız [OpenAI hesabınızda](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) bulunabilir. Bir hesabınız yoksa, bir hesap oluşturup bir API anahtarı oluşturabilirsiniz. Anahtarı aldıktan sonra, `.env` dosyasındaki `OPENAI_API_KEY` değişkenini doldurmak için kullanabilirsiniz.

### 2.6 Hugging Face'i Yapılandırma: Profil'den

Hugging Face tokenınız, profilinizdeki [Erişim Tokenları](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) altında bulunabilir. Bunları herkese açık olarak paylaşmayın veya yayınlamayın. Bunun yerine, bu proje kullanımı için yeni bir token oluşturun ve `.env` dosyasındaki `HUGGING_FACE_API_KEY` değişkenine kopyalayın. _Not:_ Bu teknik olarak bir API anahtarı değildir, ancak kimlik doğrulama için kullanılır, bu yüzden tutarlılık için bu adlandırma kuralını koruyoruz.

**Feragatname**: 
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini unutmayın. Orijinal belge, kendi dilinde otoriter kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.