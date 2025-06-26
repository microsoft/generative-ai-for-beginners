<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:18:32+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "tr"
}
-->
# Geliştirme Ortamınızı Kurun

Bu depo ve kursu, Python3, .NET, Node.js ve Java geliştirmeyi destekleyebilen Evrensel bir çalışma zamanı içeren bir [geliştirme konteyneri](https://containers.dev?WT.mc_id=academic-105485-koreyst) ile kurduk. İlgili yapılandırma, bu deponun kökündeki `.devcontainer/` klasöründe bulunan `devcontainer.json` dosyasında tanımlanmıştır.

Geliştirme konteynerini etkinleştirmek için, [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (bulut barındırmalı çalışma zamanı için) veya [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (yerel cihaz barındırmalı çalışma zamanı için) içinde başlatın. VS Code içinde geliştirme konteynerlerinin nasıl çalıştığı hakkında daha fazla bilgi için [bu belgeleri](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) okuyun.

> [!TIP]  
> Hızlı ve minimum çaba ile başlamak için GitHub Codespaces kullanmanızı öneririz. Kişisel hesaplar için cömert bir [ücretsiz kullanım kotası](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) sağlar. Kotanızı maksimum kullanmak için [zaman aşımı ayarlarını](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) yapılandırarak etkin olmayan codespaces'leri durdurun veya silin.

## 1. Ödevleri Çalıştırma

Her ders, Python, .NET/C#, Java ve JavaScript/TypeScript dahil olmak üzere bir veya daha fazla programlama dilinde sunulabilecek _isteğe bağlı_ ödevler içerecektir. Bu bölüm, bu ödevlerin yürütülmesiyle ilgili genel rehberlik sağlar.

### 1.1 Python Ödevleri

Python ödevleri, uygulamalar (`.py` dosyaları) veya Jupyter defterleri (`.ipynb` dosyaları) olarak sağlanır.
- Defteri çalıştırmak için Visual Studio Code'da açın, ardından _Select Kernel_ (sağ üstte) tıklayın ve gösterilen varsayılan Python 3 seçeneğini seçin. Artık defteri yürütmek için _Run All_ seçeneğini kullanabilirsiniz.
- Komut satırından Python uygulamalarını çalıştırmak için, doğru dosyaları seçtiğinizden ve gerekli argümanları sağladığınızdan emin olmak için ödevle ilgili talimatları izleyin.

## 2. Sağlayıcıları Yapılandırma

Ödevler, OpenAI, Azure veya Hugging Face gibi desteklenen bir hizmet sağlayıcısı aracılığıyla bir veya daha fazla Büyük Dil Modeli (LLM) dağıtımına karşı çalışacak şekilde **ayarlanabilir**. Bunlar, doğru kimlik bilgileri (API anahtarı veya token) ile programlı olarak erişebileceğimiz bir _barındırılan uç nokta_ (API) sağlar. Bu kursta, bu sağlayıcıları tartışıyoruz:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) ile çekirdek GPT serisi dahil olmak üzere çeşitli modeller.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) için kurumsal hazır olma odaklı OpenAI modelleri.
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) için açık kaynak modeller ve çıkarım sunucusu.

**Bu alıştırmalar için kendi hesaplarınızı kullanmanız gerekecek**. Ödevler isteğe bağlıdır, bu nedenle ilgi alanlarınıza göre bir, tüm veya hiçbir sağlayıcıyı ayarlamayı seçebilirsiniz. Kayıt için bazı yönergeler:

| Kayıt | Maliyet | API Anahtarı | Oyun Alanı | Yorumlar |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Fiyatlandırma](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Proje bazlı](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Kod Yok, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Birden Fazla Model Mevcut |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Fiyatlandırma](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Hızlı Başlangıç](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Stüdyo Hızlı Başlangıç](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Erişim İçin Önceden Başvuru Yapılmalıdır](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Fiyatlandırma](https://huggingface.co/pricing) | [Erişim Tokenleri](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat sınırlı modellere sahiptir](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Aşağıdaki yönergeleri takip ederek bu depoyu farklı sağlayıcılarla kullanım için _yapılandırın_. Belirli bir sağlayıcı gerektiren ödevler, dosya adında bu etiketlerden birini içerecektir:
- `aoai` - Azure OpenAI uç noktası, anahtar gerektirir
- `oai` - OpenAI uç noktası, anahtar gerektirir
- `hf` - Hugging Face token gerektirir

Bir, hiçbir veya tüm sağlayıcıları yapılandırabilirsiniz. İlgili ödevler, eksik kimlik bilgileri durumunda basitçe hata verecektir.

### 2.1. `.env` Dosyası Oluşturun

Yukarıdaki rehberi okuduğunuzu ve ilgili sağlayıcıya kaydolduğunuzu ve gerekli kimlik doğrulama bilgilerini (API_KEY veya token) edindiğinizi varsayıyoruz. Azure OpenAI durumunda, en az bir GPT modelini sohbet tamamlama için dağıtmış olan geçerli bir Azure OpenAI Hizmeti (uç noktası) dağıtımına sahip olduğunuzu varsayıyoruz.

Bir sonraki adım, **yerel ortam değişkenlerinizi** aşağıdaki gibi yapılandırmaktır:

1. `.env.copy` dosyasını içeriği aşağıdaki gibi olan kök klasörde arayın:

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

2. Bu dosyayı `.env` dosyasına aşağıdaki komutu kullanarak kopyalayın. Bu dosya _gitignore-d_ ile gizli bilgileri güvende tutar.

   ```bash
   cp .env.copy .env
   ```

3. Aşağıdaki bölümde açıklanan şekilde değerleri (sağ taraftaki yer tutucuları `=` ile değiştirin) doldurun.

3. (Seçenek) GitHub Codespaces kullanıyorsanız, bu depoyla ilişkilendirilmiş _Codespaces secrets_ olarak ortam değişkenlerini kaydetme seçeneğiniz vardır. Bu durumda, yerel bir .env dosyası ayarlamanıza gerek kalmaz. **Ancak, bu seçeneğin yalnızca GitHub Codespaces kullandığınızda çalıştığını unutmayın.** Bunun yerine Docker Desktop kullanıyorsanız yine de .env dosyasını ayarlamanız gerekecektir.

### 2.2. `.env` Dosyasını Doldurun

Değişken adlarının neyi temsil ettiğini anlamak için hızlıca göz atalım:

| Değişken  | Açıklama  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Profilinizde ayarladığınız kullanıcı erişim tokeni |
| OPENAI_API_KEY | Azure dışı OpenAI uç noktaları için hizmeti kullanma yetki anahtarı |
| AZURE_OPENAI_API_KEY | Bu hizmeti kullanma yetki anahtarı |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI kaynağı için dağıtılmış uç nokta |
| AZURE_OPENAI_DEPLOYMENT | Bu _metin üretimi_ model dağıtım uç noktası |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Bu _metin gömme_ model dağıtım uç noktası |
| | |

Not: Son iki Azure OpenAI değişkeni, sırasıyla sohbet tamamlama (metin üretimi) ve vektör arama (gömme) için varsayılan bir modeli yansıtır. Onları ayarlama talimatları ilgili ödevlerde tanımlanacaktır.

### 2.3 Azure'u Yapılandırın: Portal Üzerinden

Azure OpenAI uç noktası ve anahtar değerleri [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) içinde bulunacaktır, bu yüzden oradan başlayalım.

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) adresine gidin.
1. Yan panelde (sol menüde) **Anahtarlar ve Uç Nokta** seçeneğine tıklayın.
1. **Anahtarları Göster**'e tıklayın - aşağıdakileri görmelisiniz: ANAHTAR 1, ANAHTAR 2 ve Uç Nokta.
1. AZURE_OPENAI_API_KEY için ANAHTAR 1 değerini kullanın.
1. AZURE_OPENAI_ENDPOINT için Uç Nokta değerini kullanın.

Sonraki adımda, dağıttığımız belirli modeller için uç noktaları almamız gerekiyor.

1. Azure OpenAI kaynağı için yan panelde (sol menüde) **Model dağıtımları** seçeneğine tıklayın.
1. Hedef sayfada **Dağıtımları Yönet**'e tıklayın.

Bu sizi Azure OpenAI Studio web sitesine götürecektir, burada aşağıda açıklanan diğer değerleri bulacağız.

### 2.4 Azure'u Yapılandırın: Studio Üzerinden

1. Yukarıda açıklandığı gibi **kaynağınızdan** [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) adresine gidin.
1. Mevcut dağıtılmış modelleri görmek için **Dağıtımlar** sekmesine (yan panel, sol) tıklayın.
1. İstediğiniz model dağıtılmamışsa, **Yeni dağıtım oluştur** kullanarak onu dağıtın.
1. Bir _metin üretimi_ modeline ihtiyacınız olacak - önerimiz: **gpt-35-turbo**
1. Bir _metin gömme_ modeline ihtiyacınız olacak - önerimiz **text-embedding-ada-002**

Şimdi, kullanılan _Dağıtım adını_ yansıtacak şekilde ortam değişkenlerini güncelleyin. Bu genellikle model adı ile aynı olacaktır, ancak açıkça değiştirmediyseniz. Yani, örnek olarak, aşağıdakine sahip olabilirsiniz:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**İşiniz bittiğinde .env dosyasını kaydetmeyi unutmayın**. Dosyadan çıkabilir ve defteri çalıştırma talimatlarına dönebilirsiniz.

### 2.5 OpenAI'yi Yapılandırın: Profil Üzerinden

OpenAI API anahtarınız [OpenAI hesabınızda](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) bulunabilir. Eğer yoksa, bir hesap oluşturabilir ve bir API anahtarı oluşturabilirsiniz. Anahtarı aldıktan sonra, `.env` dosyasındaki `OPENAI_API_KEY` değişkenini doldurmak için kullanabilirsiniz.

### 2.6 Hugging Face'i Yapılandırın: Profil Üzerinden

Hugging Face tokeniniz, [Erişim Tokenleri](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) altında profilinizde bulunabilir. Bunları kamuya açık bir şekilde paylaşmayın veya yayınlamayın. Bunun yerine, bu proje kullanımı için yeni bir token oluşturun ve bunu `.env` dosyasındaki `HUGGING_FACE_API_KEY` değişkenine kopyalayın. _Not:_ Bu teknik olarak bir API anahtarı değildir ancak kimlik doğrulama için kullanılır, bu yüzden tutarlılık için bu adlandırma kuralını koruyoruz.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için, profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.