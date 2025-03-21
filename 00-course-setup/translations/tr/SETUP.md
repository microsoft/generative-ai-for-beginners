# Geliştirme Ortamınızı Kurun

Bu depo ve kurs, Python3, .NET, Node.js ve Java geliştirmesini destekleyen Evrensel bir çalışma zamanı içeren bir [geliştirme konteyneri](https://containers.dev?WT.mc_id=academic-105485-koreyst) ile yapılandırılmıştır. İlgili yapılandırma, bu deposunun kök dizininde bulunan `.devcontainer/` klasöründeki `devcontainer.json` dosyasında tanımlanmıştır.

Geliştirme konteynerini etkinleştirmek için: [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) kullanarak (bulut tabanlı çalışma zamanı) ya da [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) kullanarak (yerel cihaz üzerinde barındırılan çalışma zamanı). Geliştirme konteynerlerinin VS Code içinde nasıl çalıştığını daha detaylı öğrenmek için [bu dokümantasyona](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) göz atabilirsiniz.  

> [!TIP]  
> Hızlı ve kolay bir başlangıç için GitHub Codespaces kullanmanızı öneririz. Kişisel hesaplar için cömert bir [ücretsiz kullanım kotası](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) sunar. Ayrıca, boşta kalan çalışma alanlarını durdurmak veya silmek için [zaman aşımı ayarlarını](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) yapılandırarak kotanızı verimli şekilde kullanabilirsiniz. 🚀


## 1. Görevleri Çalıştırma

Her derste, Python, .NET/C#, Java ve JavaScript/TypeScript gibi farklı programlama dillerinde sunulabilecek **isteğe bağlı** görevler yer alacaktır. Bu bölüm, bu görevleri çalıştırmaya yönelik genel yönergeleri sağlar.

### 1.1 Python Görevleri

Python görevleri, uygulamalar (`.py` dosyaları) veya Jupyter not defterleri (`.ipynb` dosyaları) olarak sağlanır.

- **Jupyter not defterini çalıştırmak için**:  
  - Visual Studio Code'da açın.  
  - Sağ üst köşede bulunan _"Select Kernel"_ seçeneğine tıklayın.  
  - Varsayılan **Python 3** seçeneğini seçin.  
  - **"Run All"** butonuna basarak tüm hücreleri çalıştırabilirsiniz.

- **Python uygulamalarını komut satırından çalıştırmak için**:  
  - Doğru dosyaları seçtiğinizden ve gerekli argümanları sağladığınızdan emin olun.  
  - Göreve özel talimatları takip edin.


## 2. Sağlayıcıları Yapılandırma

Görevler, desteklenen bir hizmet sağlayıcı aracılığıyla bir veya daha fazla Büyük Dil Modeli (LLM) dağıtımıyla çalışacak şekilde ayarlanabilir. Bu sağlayıcılar, uygun kimlik bilgileri (API anahtarı veya token) ile programlı olarak erişebileceğimiz **barındırılmış uç noktalar (API)** sağlar. Bu kursta aşağıdaki sağlayıcıları ele alıyoruz:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) – Çekirdek GPT serisi de dahil olmak üzere çeşitli modeller sunar.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) – OpenAI modellerine kurumsal ölçekli erişim sağlar.
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) – Açık kaynak modelleri ve çıkarım sunucusu (inference server) sunar.

**Bu alıştırmalar için kendi hesaplarınızı kullanmanız gerekecek**. Görevler isteğe bağlıdır, bu yüzden ilginize bağlı olarak birini, tümünü veya hiçbirini kurmayı seçebilirsiniz. Kayıt süreciyle ilgili bazı rehberlik aşağıda verilmiştir:


| Kayıt | Maliyet | API Anahtarı | Playground | Açıklamalar |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [Fiyatlandırma](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [Proje Bazlı](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Kod Gerektirmeyen, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Birden Fazla Model Mevcut |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [Fiyatlandırma](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [SDK Hızlı Başlangıç](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Studio Hızlı Başlangıç](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Önceden Başvuru Gerekir](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Fiyatlandırma](https://huggingface.co/pricing) | [Erişim Tokenları](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat sınırlı modellere sahiptir](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Aşağıdaki talimatları izleyerek bu depoyu farklı sağlayıcılarla kullanım için _yapılandırın_. Belirli bir sağlayıcı gerektiren ödevlerin dosya adlarında aşağıdaki etiketlerden biri bulunacaktır:
 - `aoai` - Azure OpenAI uç noktası ve anahtarı gerektirir
 - `oai` - OpenAI uç noktası ve anahtarı gerektirir
 - `hf` - Hugging Face token gerektirir

Bir veya daha fazla sağlayıcıyı yapılandırabilirsiniz. İlgili ödevler, gerekli kimlik bilgileri eksikse hata verecektir.


###  2.1. Create `.env` file

İlgili sağlayıcıya kaydolduğunuzu ve gerekli kimlik doğrulama bilgilerini (API_KEY veya token) aldığınızı varsayıyoruz. Azure OpenAI durumunda, sohbet tamamlama için en az bir GPT modeli dağıtılmış olan geçerli bir Azure OpenAI Hizmeti (uç nokta) dağıtımınız olduğunu varsayıyoruz.

Bir sonraki adım, **yerel ortam değişkenlerinizi** aşağıdaki gibi yapılandırmaktır:

1. Ana dizinde `.env.copy` adlı bir dosya bulun. İçeriği şu şekilde olmalıdır:

   ```bash
   # OpenAI Sağlayıcısı
   OPENAI_API_KEY='<OpenAI API anahtarınızı buraya ekleyin>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Varsayılan ayar
   AZURE_OPENAI_API_KEY='<Azure OpenAI anahtarınızı buraya ekleyin>'
   AZURE_OPENAI_ENDPOINT='<Azure OpenAI hizmet uç noktanızı buraya ekleyin>'
   AZURE_OPENAI_DEPLOYMENT='<Konuşma tamamlama modelinizin adını buraya ekleyin>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<Gömme modelinizin adını buraya ekleyin>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<Hugging Face API anahtarınızı veya tokeninizi buraya ekleyin>'
   ```

2. Bu dosyayı `.env` olarak kopyalamak için aşağıdaki komutu kullanın. Bu dosya _gitignore-d_, olduğu için gizli bilgileriniz korunur.

   ```bash
   cp .env.copy .env
   ```

3. Değerleri (`=` işaretinin sağ tarafındaki yer tutucuları) bir sonraki bölümde açıklandığı gibi doldurun.

3. (İsteğe bağlı) GitHub Codespaces kullanıyorsanız, ortam değişkenlerini bu depoya bağlı _Codespaces sırları_ olarak kaydetme seçeneğiniz vardır. Bu durumda, yerel bir .env dosyası kurmanıza gerek kalmaz. **Ancak, bu seçeneğin yalnızca GitHub Codespaces kullanıyorsanız çalıştığını unutmayın.** Bunun yerine Docker Desktop kullanıyorsanız, yine de .env dosyasını kurmanız gerekecektir.


### 2.2. Populate `.env` file

Değişken adlarının ne anlama geldiğini anlamak için hızlıca göz atalım:

| Değişken  | Açıklama  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Profilinizde kurduğunuz kullanıcı erişim tokeni |
| OPENAI_API_KEY | Azure olmayan OpenAI uç noktaları için hizmeti kullanma yetkilendirme anahtarı |
| AZURE_OPENAI_API_KEY | Bu hizmeti kullanmak için yetkilendirme anahtarı |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI kaynağı için dağıtılmış uç nokta |
| AZURE_OPENAI_DEPLOYMENT | _Metin üretimi_ model dağıtım uç noktası |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _Metin gömme_ model dağıtım uç noktası |
| | |

Not: Son iki Azure OpenAI değişkeni, sırasıyla sohbet tamamlama (metin üretimi) ve vektör arama (gömme) için varsayılan bir modeli yansıtır. Bunları ayarlama talimatları ilgili ödevlerde tanımlanacaktır.


### 2.3 Configure Azure: From Portal

Azure OpenAI uç noktası ve anahtar değerleri [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)'da bulunacaktır, bu yüzden oradan başlayalım.

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)'a gidin
2. Kenar çubuğundaki (soldaki menü) **Anahtarlar ve Uç Nokta** seçeneğine tıklayın.
3. **Anahtarları Göster**'e tıklayın - şunları görmelisiniz: ANAHTAR 1, ANAHTAR 2 ve Uç Nokta.
4. ANAHTAR 1 değerini AZURE_OPENAI_API_KEY için kullanın
5. Uç Nokta değerini AZURE_OPENAI_ENDPOINT için kullanın

Ardından, dağıttığımız belirli modeller için uç noktaları belirlememiz gerekiyor.

1. Azure OpenAI kaynağı için kenar çubuğundaki (sol menü) **Model dağıtımları** seçeneğine tıklayın.
2. Hedef sayfada **Dağıtımları Yönet**'e tıklayın

Bu sizi Azure OpenAI Studio web sitesine götürecek, burada diğer değerleri aşağıda açıklandığı gibi bulacağız.

### 2.4 Configure Azure: From Studio

1. Yukarıda açıklandığı gibi **kaynağınızdan** [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst)'ya gidin.
2. Şu anda dağıtılmış modelleri görüntülemek için **Dağıtımlar** sekmesine tıklayın (kenar çubuğu, sol).
3. İstediğiniz model dağıtılmamışsa, dağıtmak için **Yeni dağıtım oluştur**'u kullanın.
4. Bir _metin üretimi_ modeline ihtiyacınız olacak - önerimiz: **gpt-35-turbo**
5. Bir _metin gömme_ modeline ihtiyacınız olacak - önerimiz: **text-embedding-ada-002**

Şimdi ortam değişkenlerini kullanılan _Dağıtım adını_ yansıtacak şekilde güncelleyin. Bu genellikle açıkça değiştirmediyseniz model adıyla aynı olacaktır. Örneğin, şöyle olabilir:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**İşlem bittiğinde .env dosyasını kaydetmeyi unutmayın**. Artık dosyadan çıkabilir ve not defterini çalıştırma talimatlarına dönebilirsiniz.

### 2.5 Configure OpenAI: From Profile

OpenAI API anahtarınızı [OpenAI hesabınızda](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) bulabilirsiniz. Eğer hesabınız yoksa, bir hesap oluşturup API anahtarı oluşturabilirsiniz. Anahtarı aldıktan sonra, `.env` dosyasındaki `OPENAI_API_KEY` değişkenini doldurabilirsiniz.

### 2.6 Configure Hugging Face: From Profile

Hugging Face tokeninizi profilinizde [Erişim Tokenleri](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) altında bulabilirsiniz. Bunları herkese açık olarak paylaşmayın. Bunun yerine, bu proje kullanımı için yeni bir token oluşturun ve bunu `.env` dosyasında `HUGGING_FACE_API_KEY` değişkeni altına kopyalayın. _Not:_ Bu teknik olarak bir API anahtarı değildir ancak kimlik doğrulama için kullanılır, bu yüzden tutarlılık için bu isimlendirme kuralını koruyoruz.
