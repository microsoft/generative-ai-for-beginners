<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:29:54+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "tr"
}
-->
# Geliştirme Ortamınızı Kurun

Bu depo ve kurs, Python3, .NET, Node.js ve Java geliştirmeyi destekleyen Evrensel bir çalışma zamanı içeren bir [geliştirme konteyneri](https://containers.dev?WT.mc_id=academic-105485-koreyst) ile hazırlandı. İlgili yapılandırma, bu deponun kök dizinindeki `.devcontainer/` klasöründe bulunan `devcontainer.json` dosyasında tanımlanmıştır.

Geliştirme konteynerini etkinleştirmek için, [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (bulut tabanlı çalışma zamanı için) veya [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (yerel cihazda çalışma zamanı için) üzerinde başlatın. VS Code içinde geliştirme konteynerlerinin nasıl çalıştığı hakkında daha fazla bilgi için [bu dokümana](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) göz atabilirsiniz.

> [!TIP]  
> Hızlı bir başlangıç için GitHub Codespaces kullanmanızı öneririz. Kişisel hesaplar için cömert bir [ücretsiz kullanım kotası](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) sunar. Kotanızı en iyi şekilde kullanmak için, kullanılmayan codespaces’leri durdurmak veya silmek üzere [zaman aşımı ayarlarını](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) yapılandırabilirsiniz.

## 1. Ödevleri Çalıştırma

Her ders, Python, .NET/C#, Java ve JavaScript/TypeScript dahil olmak üzere bir veya daha fazla programlama dilinde sunulabilecek _isteğe bağlı_ ödevler içerebilir. Bu bölüm, bu ödevlerin nasıl çalıştırılacağına dair genel rehberlik sağlar.

### 1.1 Python Ödevleri

Python ödevleri ya uygulama olarak (`.py` dosyaları) ya da Jupyter defterleri (`.ipynb` dosyaları) şeklinde sunulur.  
- Defteri çalıştırmak için, Visual Studio Code’da açın, ardından sağ üstteki _Select Kernel_ seçeneğine tıklayın ve varsayılan Python 3 seçeneğini seçin. Artık defteri çalıştırmak için _Run All_ yapabilirsiniz.  
- Komut satırından Python uygulamalarını çalıştırmak için, doğru dosyaları seçtiğinizden ve gerekli argümanları sağladığınızdan emin olmak için ödevlere özel talimatları izleyin.

## 2. Sağlayıcıları Yapılandırma

Ödevler, OpenAI, Azure veya Hugging Face gibi desteklenen servis sağlayıcılar aracılığıyla bir veya daha fazla Büyük Dil Modeli (LLM) dağıtımıyla çalışacak şekilde **ayarlanabilir**. Bu sağlayıcılar, doğru kimlik bilgileri (API anahtarı veya token) ile programatik olarak erişebileceğimiz _barındırılan bir uç nokta_ (API) sunar. Bu kursta aşağıdaki sağlayıcıları ele alıyoruz:

 - Çeşitli modeller içeren [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), temel GPT serisi dahil.
 - Kurumsal hazırda odaklanan OpenAI modelleri için [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)
 - Açık kaynak modeller ve çıkarım sunucusu için [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)

**Bu egzersizler için kendi hesaplarınızı kullanmanız gerekecek**. Ödevler isteğe bağlıdır, bu yüzden ilginize göre birini, hepsini veya hiç birini kurmayı seçebilirsiniz. Kayıt için bazı rehberlik:

| Kayıt | Ücret | API Anahtarı | Playground | Yorumlar |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [Fiyatlandırma](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [Proje bazlı](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Kod Gerektirmez, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Birden Çok Model Mevcut |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [Fiyatlandırma](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [SDK Hızlı Başlangıç](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Studio Hızlı Başlangıç](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Erişim İçin Ön Başvuru Gerekir](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Fiyatlandırma](https://huggingface.co/pricing) | [Erişim Tokenları](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat sınırlı modellere sahip](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Bu depoyu farklı sağlayıcılarla kullanmak üzere _yapılandırmak_ için aşağıdaki talimatları izleyin. Belirli bir sağlayıcı gerektiren ödevlerin dosya adlarında aşağıdaki etiketlerden biri bulunur:  
 - `aoai` - Azure OpenAI uç noktası ve anahtarı gerektirir  
 - `oai` - OpenAI uç noktası ve anahtarı gerektirir  
 - `hf` - Hugging Face token gerektirir  

Birini, hiçbirini veya hepsini yapılandırabilirsiniz. İlgili ödevler, eksik kimlik bilgileri durumunda hata verecektir.

### 2.1. `.env` dosyası oluşturma

Yukarıdaki rehberi okuduğunuzu, ilgili sağlayıcıya kaydolduğunuzu ve gerekli kimlik doğrulama bilgilerini (API_KEY veya token) aldığınızı varsayıyoruz. Azure OpenAI için, en az bir GPT modelinin sohbet tamamlaması için dağıtıldığı geçerli bir Azure OpenAI Hizmeti (uç noktası) dağıtımınızın da olduğunu varsayıyoruz.

Sonraki adım, **yerel ortam değişkenlerinizi** aşağıdaki şekilde yapılandırmaktır:

1. Kök klasörde `.env.copy` adlı bir dosya bulun; içeriği şu şekilde olmalıdır:

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

2. Aşağıdaki komutla bu dosyayı `.env` olarak kopyalayın. Bu dosya _gitignore_ içinde yer alır, böylece gizli bilgiler güvende kalır.

   ```bash
   cp .env.copy .env
   ```

3. Değerleri doldurun (sağdaki yer tutucuları `=` işaretinden sonra değiştirin) ve sonraki bölümde açıklanan şekilde tamamlayın.

3. (Opsiyonel) GitHub Codespaces kullanıyorsanız, ortam değişkenlerini bu depoya bağlı _Codespaces secrets_ olarak kaydetme seçeneğiniz vardır. Bu durumda yerel `.env` dosyası oluşturmanız gerekmez. **Ancak, bu seçenek yalnızca GitHub Codespaces kullanıyorsanız geçerlidir.** Docker Desktop kullanıyorsanız yine `.env` dosyasını yapılandırmanız gerekir.

### 2.2. `.env` dosyasını doldurma

Değişken adlarının ne anlama geldiğini hızlıca inceleyelim:

| Değişken  | Açıklama  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Profilinizde ayarladığınız kullanıcı erişim tokenı |
| OPENAI_API_KEY | Azure dışı OpenAI uç noktaları için yetkilendirme anahtarı |
| AZURE_OPENAI_API_KEY | Azure OpenAI servisi için yetkilendirme anahtarı |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI kaynağı için dağıtılmış uç nokta |
| AZURE_OPENAI_DEPLOYMENT | _Metin oluşturma_ model dağıtım uç noktası |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _Metin gömme_ model dağıtım uç noktası |
| | |

Not: Son iki Azure OpenAI değişkeni, sırasıyla sohbet tamamlaması (metin oluşturma) ve vektör araması (gömme) için varsayılan modelleri yansıtır. Bunların ayarlanmasıyla ilgili talimatlar ilgili ödevlerde verilecektir.

### 2.3 Azure’u Portal’dan Yapılandırma

Azure OpenAI uç noktası ve anahtar değerleri [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)’da bulunur, o yüzden oradan başlayalım.

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)’a gidin  
1. Kenar çubuğunda (sol menü) **Keys and Endpoint** seçeneğine tıklayın  
1. **Show Keys** butonuna tıklayın - aşağıdakileri görmelisiniz: KEY 1, KEY 2 ve Endpoint  
1. AZURE_OPENAI_API_KEY için KEY 1 değerini kullanın  
1. AZURE_OPENAI_ENDPOINT için Endpoint değerini kullanın  

Sonra, dağıttığımız belirli modellerin uç noktalarına ihtiyacımız var.

1. Azure OpenAI kaynağı için kenar çubuğunda (sol menü) **Model deployments** seçeneğine tıklayın  
1. Açılan sayfada **Manage Deployments** butonuna tıklayın  

Bu sizi Azure OpenAI Studio web sitesine götürecek, burada aşağıda açıklanan diğer değerleri bulacağız.

### 2.4 Azure’u Studio’dan Yapılandırma

1. Yukarıda açıklandığı gibi, kaynağınızdan [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst)’ya gidin  
1. Mevcut dağıtılmış modelleri görmek için sol kenar çubuğundaki **Deployments** sekmesine tıklayın  
1. İstediğiniz model dağıtılmamışsa, dağıtmak için **Create new deployment** seçeneğini kullanın  
1. Bir _metin oluşturma_ modeline ihtiyacınız olacak - önerimiz: **gpt-35-turbo**  
1. Bir _metin gömme_ modeline ihtiyacınız olacak - önerimiz: **text-embedding-ada-002**  

Şimdi ortam değişkenlerini, kullanılan _Deployment name_ (Dağıtım adı) ile güncelleyin. Bu genellikle model adıyla aynı olur, eğer açıkça değiştirmediyseniz. Örneğin, şöyle olabilir:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**İşiniz bittiğinde .env dosyasını kaydetmeyi unutmayın**. Dosyadan çıkabilir ve defteri çalıştırma talimatlarına dönebilirsiniz.

### 2.5 OpenAI’yi Profilden Yapılandırma

OpenAI API anahtarınızı [OpenAI hesabınızda](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) bulabilirsiniz. Henüz bir anahtarınız yoksa, hesap açıp bir API anahtarı oluşturabilirsiniz. Anahtarı aldıktan sonra `.env` dosyasındaki `OPENAI_API_KEY` değişkenini doldurmak için kullanabilirsiniz.

### 2.6 Hugging Face’i Profilden Yapılandırma

Hugging Face tokenınızı profilinizdeki [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) bölümünde bulabilirsiniz. Bunları kamuya açık şekilde paylaşmayın. Bunun yerine, bu proje için yeni bir token oluşturun ve `.env` dosyasındaki `HUGGING_FACE_API_KEY` değişkenine yapıştırın. _Not:_ Teknik olarak bu bir API anahtarı değildir ancak kimlik doğrulama için kullanıldığı için tutarlılık adına bu isimlendirmeyi koruyoruz.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.