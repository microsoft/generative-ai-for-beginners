# Bir LLM Sağlayıcısı Seçme ve Yapılandırma 🔑

Ödevler **belirli durumlarda** OpenAI, Azure veya Hugging Face gibi desteklenen hizmet sağlayıcılar aracılığıyla bir veya daha fazla Büyük Dil Modeli (LLM) dağıtımıyla çalışacak şekilde ayarlanabilir. Bunlar, doğru kimlik bilgileriyle (API anahtarı veya belirteç) programlı olarak erişebileceğimiz _barındırılan bir uç nokta_ (API) sağlar. Bu derste, bu sağlayıcılar hakkında konuşacağız:

 - Çeşitli modeller içeren çekirdek GPT serisi dahil olmak üzere [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst).
 - Kurumsal hazır bulunuşluk odaklı OpenAI modelleri için [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst).
 - OpenAI, Meta, Mistral, Cohere, Microsoft ve daha fazlasından yüzlerce modele tek bir uç nokta ve API anahtarı ile erişmek için [Microsoft Foundry Modelleri](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) (GitHub Modellerinin yerini alır, Temmuz 2026 sonunda kullanımdan kalkacak)
 - Açık kaynak modeller ve çıkarım servisi için [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst).
 - Modelleri tamamen çevrimdışı olarak kendi cihazınızda çalıştırmak isterseniz, bulut aboneliği gerekmeden [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) veya [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst).

**Bu egzersizler için kendi hesaplarınızı kullanmanız gerekir**. Ödevler isteğe bağlıdır, ilgi alanlarınıza göre birini, tümünü veya hiçbirini kurmayı seçebilirsiniz. Kayıt için bazı rehberlik:

| Kayıt | Ücret | API Anahtarı | Oyun Alanı | Yorumlar |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Fiyatlandırma](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Proje bazlı](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Kod Gerektirmez, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Birden Çok Model Mevcut |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Fiyatlandırma](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Hızlı Başlangıç](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Stüdyo Hızlı Başlangıç](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Erişim İçin Ön Başvuru Şart](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Fiyatlandırma](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Proje Genel Bakış sayfası](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Oyun Alanı](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Ücretsiz katman mevcut; çoklu model sağlayıcıları için bir uç nokta + anahtar |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Fiyatlandırma](https://huggingface.co/pricing) | [Erişim Belirteçleri](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat sınırlı modellere sahip](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Ücretsiz (cihazınızda çalışır) | Gerekli değil | [Yerel CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Tamamen çevrimdışı, OpenAI uyumlu uç nokta |
| | | | | |

Bu depoyu farklı sağlayıcılarla kullanmak için _yapılandırmak_ için aşağıdaki talimatları izleyin. Belirli bir sağlayıcı gerektiren ödevler dosya adlarında aşağıdaki etiketlerden birini içerecektir:

- `aoai` - Azure OpenAI uç noktası, anahtarı gerektirir
- `oai` - OpenAI uç noktası, anahtarı gerektirir
- `hf` - Hugging Face belirteci gerektirir
- `githubmodels` - Microsoft Foundry Modelleri uç noktası, anahtarı gerektirir (GitHub Modelleri Temmuz 2026 sonunda emekliye ayrılacak)

Birini, hiçbirini veya tüm sağlayıcıları yapılandırabilirsiniz. İlgili ödevler kimlik bilgileri eksik olduğunda hata verir.

## `.env` dosyası oluşturun

İlgili sağlayıcıya kaydolduğunuzu, gerekli kimlik doğrulama kimlik bilgilerini (API_KEY veya belirteç) aldığınızı varsayıyoruz. Azure OpenAI için, sohbet tamamlama için en az bir GPT modeli dağıtılmış geçerli bir Azure OpenAI Servis (uç nokta) dağıtımınız olduğunu varsayıyoruz.

Bir sonraki adım **yerel ortam değişkenlerinizi** aşağıdaki şekilde yapılandırmaktır:

1. Kök klasörde `.env.copy` adlı bir dosya arayın; içeriği aşağıdaki gibi olmalıdır:

   ```bash
   # OpenAI Sağlayıcısı
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Microsoft Foundry'de Azure OpenAI
   ## (Azure OpenAI Hizmeti artık Microsoft Foundry'nin bir parçasıdır: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Varsayılan ayarlandı! (mevcut kararlı GA API sürümü)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry Modelleri (çoklu sağlayıcı model kataloğu, GitHub Modellerin yerine geçer, Temmuz 2026 sonunda kullanımdan kalkacak)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Aşağıdaki komutu kullanarak bu dosyayı `.env` olarak kopyalayın. Bu dosya _gitignore_ içerisinde gizli tutularak sırlar korunur.

   ```bash
   cp .env.copy .env
   ```

3. Değerleri (sağdaki yer tutucuları `=` işaretinden sonra) bir sonraki bölümde açıklandığı gibi doldurun.

4. (İsteğe Bağlı) GitHub Codespaces kullanıyorsanız, bu depoya bağlı _Codespaces sırları_ olarak ortam değişkenlerini kaydetme seçeneğiniz vardır. Bu durumda yerel bir .env dosyası kurmanıza gerek kalmaz. **Ancak, bu seçenek yalnızca GitHub Codespaces kullanıyorsanız geçerlidir.** Docker Desktop kullanıyorsanız yine de .env dosyası kurmanız gerekir.

## `.env` dosyasını doldurun

Değişken adlarının ne anlama geldiğini hızlıca anlayalım:

| Değişken  | Açıklama  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Profilinizde ayarladığınız kullanıcı erişim belirteci |
| OPENAI_API_KEY | Azure dışı OpenAI uç noktaları için hizmet kullanma yetkilendirme anahtarı |
| AZURE_OPENAI_API_KEY | Bu servisi kullanmak için yetkilendirme anahtarı |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI kaynağı için dağıtılmış uç nokta |
| AZURE_OPENAI_DEPLOYMENT | _metin oluşturma_ modeli dağıtım uç noktası |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _metin gömme_ modeli dağıtım uç noktası |
| AZURE_INFERENCE_ENDPOINT | Microsoft Foundry projeniz için uç nokta, Microsoft Foundry Modelleri için kullanılır |
| AZURE_INFERENCE_CREDENTIAL | Microsoft Foundry projeniz için API anahtarı |
| | |

Not: Son iki Azure OpenAI değişkeni sırasıyla sohbet tamamlama (metin oluşturma) ve vektör araması (gömme) için varsayılan bir modeli yansıtır. Ayarlama talimatları ilgili ödevlerde belirtilecektir.

## Azure OpenAI Yapılandırması: Portal'dan

> **Not:** Azure OpenAI Hizmeti artık [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) parçasıdır. Kaynaklar ve dağıtımlar hâlâ Azure Portal'da görünür, ancak günlük model yönetimi (dağıtımlar, oyun alanı, izleme) eski bağımsız "Azure OpenAI Studio" yerine Foundry portalında gerçekleşmektedir.

Azure OpenAI uç noktası ve anahtar değerleri [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) içinde bulunur, bu yüzden oradan başlayalım.

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) adresine gidin
1. Kenar çubuğunda (soldaki menü) **Anahtarlar ve Uç Nokta** seçeneğine tıklayın.
1. **Anahtarları Göster**'e tıklayın - aşağıdakileri görmelisiniz: ANAHTAR 1, ANAHTAR 2 ve Uç Nokta.
1. `AZURE_OPENAI_API_KEY` için ANAHTAR 1 değerini kullanın
1. `AZURE_OPENAI_ENDPOINT` için Uç Nokta değerini kullanın

Sonraki olarak, dağıttığımız belirli modeller için uç noktalara ihtiyacımız var.

1. Azure OpenAI kaynağı için kenar çubuğunda (sol menü) **Model dağıtımları** seçeneğine tıklayın.
1. Hedef sayfada, **Microsoft Foundry portalına git** (veya kaynak türünüze bağlı olarak **Dağıtımları Yönet**) seçeneğine tıklayın.

Bu sizi Microsoft Foundry portalına götürecek; diğer değerleri burada aşağıda açıklandığı şekilde bulacağız.

## Azure OpenAI Yapılandırması: Microsoft Foundry portalından

1. Yukarıda açıklandığı gibi kendi kaynağınızdan [Microsoft Foundry portalına](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) gidin.
1. Şu anda dağıtılmış modelleri görmek için **Dağıtımlar** sekmesine (sol kenar çubuğu) tıklayın.
1. İstediğiniz model dağıtılmamışsa, [model kataloğundan](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) dağıtmak için **Model dağıt** kullanın.
1. _metin oluşturma_ modeli gerekecek - önerimiz: **gpt-5-mini**
1. _metin gömme_ modeli gerekecek - önerimiz **text-embedding-3-small**

Şimdi ortam değişkenlerini, kullanılan _Dağıtım adı'nı yansıtacak şekilde güncelleyin. Bu genellikle model adı ile aynıdır, eğer açıkça değiştirmediyseniz. Örnek olarak aşağıdakilere sahip olabilirsiniz:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**İşiniz bittiğinde .env dosyasını kaydetmeyi unutmayın**. Dosyadan çıkabilir ve not defterini çalıştırma talimatlarına dönebilirsiniz.

## OpenAI Yapılandırması: Profil'den

OpenAI API anahtarınız [OpenAI hesabınızda](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) bulunabilir. Eğer yoksa, bir hesap oluşturabilir ve bir API anahtarı yaratabilirsiniz. Anahtarı aldıktan sonra `.env` dosyasındaki `OPENAI_API_KEY` değişkenine yazabilirsiniz.

## Hugging Face Yapılandırması: Profil'den

Hugging Face belirteciniz profilinizde [Erişim Belirteçleri](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) altında bulunabilir. Bunları kamuya açık paylaşmayın. Bunun yerine, bu proje kullanımı için yeni bir belirteç yaratın ve bunu `.env` dosyasındaki `HUGGING_FACE_API_KEY` değişkenine kopyalayın. _Not:_ Teknik olarak bu bir API anahtarı değil, ancak kimlik doğrulama için kullanıldığı için tutarlılık açısından bu isimlendirme korunuyor.

## Microsoft Foundry Modellerini Yapılandırma: Portal'dan

> **Not:** GitHub Modelleri Temmuz 2026 sonunda emekliye ayrılacak. Microsoft Foundry Modelleri, aynı ücretsiz deneme amaçlı model kataloğu ve Azure AI Çıkarım SDK / OpenAI SDK deneyimini sunarak doğrudan yerini alır.

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) adresine gidin ve bir Foundry projesi oluşturun (veya açın).
1. [Model kataloğunu](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) gezin ve örneğin `gpt-5-mini` modelini dağıtın.
1. Projenin **Genel Bakış** sayfasında, **uç nokta** ve **API anahtarı**nı kopyalayın.
1. Uç nokta değerini `.env` dosyanızda `AZURE_INFERENCE_ENDPOINT` olarak, anahtar değerini `AZURE_INFERENCE_CREDENTIAL` olarak kullanın.

## Çevrimdışı / Yerel Sağlayıcılar

Bulut aboneliği kullanmak istemiyorsanız, uyumlu açık modelleri doğrudan kendi cihazınızda çalıştırabilirsiniz:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft’un cihaz üzeri çalışma zamanı. En iyi yürütme sağlayıcısını (NPU, GPU veya CPU) otomatik seçer ve OpenAI uyumlu bir uç nokta sunar, böylece bu dersteki örnek kodun çoğunu çok az değişiklikle yeniden kullanabilirsiniz. Başlamak için [Foundry Local belgelerine](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) bakın veya Windows için `winget install Microsoft.FoundryLocal`, macOS için `brew install microsoft/foundrylocal/foundrylocal` komutunu kullanarak yükleyin.
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - Llama, Phi, Mistral ve Gemma gibi açık modelleri yerelde çalıştırmak için popüler bir alternatif.


Her iki seçeneği de kullanarak pratik örnekler için bkz. [Ders 19: SLM'lerle İnşa Etmek](../19-slm/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->