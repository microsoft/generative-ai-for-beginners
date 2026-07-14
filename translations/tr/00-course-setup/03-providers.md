# Bir LLM Sağlayıcısı Seçme ve Yapılandırma 🔑

Atamalar, OpenAI, Azure veya Hugging Face gibi desteklenen bir hizmet sağlayıcısı aracılığıyla bir veya daha fazla Büyük Dil Modeli (LLM) dağıtımıyla çalışacak şekilde de ayarlanabilir. Bunlar, doğru kimlik bilgileri (API anahtarı veya belirteci) ile programatik olarak erişebileceğimiz _barındırılan uç noktalar_ (API) sağlar. Bu kursta, bu sağlayıcıları tartışıyoruz:

 - Çekirdek GPT serisi de dahil olmak üzere çeşitli modeller sunan [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst).
 - Kurumsal hazır olma odaklı OpenAI modelleri için [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst).
 - OpenAI, Meta, Mistral, Cohere, Microsoft ve daha fazlasından yüzlerce modele tek uç nokta ve API anahtarıyla erişim sağlayan [Microsoft Foundry Modelleri](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) (27 Temmuz 2026 sonunda emekliye ayrılacak olan GitHub Modellerinin yerini alır).
 - Açık kaynak modeller ve çıkarım sunucusu için [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst).
 - Kendi cihazınızda tamamen çevrimdışı çalıştırmak isterseniz, bulut aboneliği gerektirmeyen [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) veya [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst).

**Bu egzersizler için kendi hesaplarınızı kullanmanız gerekecek**. Atamalar isteğe bağlıdır, böylece ilginize göre birini, tamamını veya hiçbirini yapılandırmayı seçebilirsiniz. Kayıt için bazı rehberlik:

| Kayıt | Ücret | API Anahtarı | Oyun Alanı | Yorumlar |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [Fiyatlandırma](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [Proje bazlı](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Kod Gerektirmez, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Birden Fazla Model Mevcut |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [Fiyatlandırma](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [SDK Hızlı Başlangıç](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Studio Hızlı Başlangıç](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Erişim İçin Önceden Başvurulmalı](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Fiyatlandırma](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Proje Genel Bakış sayfası](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Oyun Alanı](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Ücretsiz katman mevcut; çoklu model sağlayıcılar için tek uç nokta + anahtar |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Fiyatlandırma](https://huggingface.co/pricing) | [Erişim Belirteçleri](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat sınırlı modellere sahip](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Ücretsiz (cihazınızda çalışır) | Gerekli değil | [Yerel CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Tamamen çevrimdışı, OpenAI uyumlu uç nokta |
| | | | | |

Bu havuzu farklı sağlayıcılarla kullanmak için _yapılandırma_ talimatlarını takip edin. Belirli bir sağlayıcı gerektiren atamaların dosya adında aşağıdaki etiketlerden biri bulunacaktır:

- `aoai` - Azure OpenAI uç noktası, anahtarı gerektirir
- `oai` - OpenAI uç noktası, anahtarı gerektirir
- `hf` - Hugging Face belirteci gerektirir
- `githubmodels` - Microsoft Foundry Modelleri uç noktası, anahtarı gerektirir (GitHub Modelleri 27 Temmuz 2026 sonunda emekliye ayrılacak)

Birini, hiçbirini veya tüm sağlayıcıları yapılandırabilirsiniz. İlgili atamalar, kimlik bilgileri eksikse hata verecektir.

## `.env` dosyası oluşturun

Yukarıdaki rehberi okuduğunuzu, ilgili sağlayıcıya kaydolduğunuzu ve gerekli kimlik doğrulama bilgilerini (API_KEY veya belirteç) aldığınızı varsayıyoruz. Azure OpenAI durumunda, en az bir GPT modeli dağıtılmış geçerli Azure OpenAI Hizmeti (uç noktası) kurulumunuzun olduğunu varsayıyoruz.

Sonraki adım, **yerel ortam değişkenlerinizi** aşağıdaki gibi yapılandırmaktır:

1. Kök klasörde `.env.copy` adlı içinde aşağıdaki gibi içerik bulunan bir dosya arayın:

   ```bash
   # OpenAI Sağlayıcısı
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Microsoft Foundry'de Azure OpenAI
   ## (Azure OpenAI Hizmeti şimdi Microsoft Foundry'nin bir parçası: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Varsayılan ayarlandı! (mevcut kararlı GA API sürümü)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry Modelleri (çoklu sağlayıcı model kataloğu, GitHub Modellerinin yerine geçer, Temmuz 2026 sonunda kullanımdan kalkacak)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Aşağıdaki komutla bu dosyayı `.env` olarak kopyalayın. Bu dosya _gitignore_ edilmiştir, gizliliği korur.

   ```bash
   cp .env.copy .env
   ```

3. Değerleri doldurun (sağ taraftaki yer tutucuları değiştirin) bir sonraki bölümde açıklanan şekilde.

4. (Opsiyonel) GitHub Codespaces kullanıyorsanız, ortam değişkenlerini bu depoyla ilişkili _Codespaces gizli anahtarları_ olarak kaydetme seçeneğiniz var. Bu durumda, yerel bir .env dosyası kurmanıza gerek kalmaz. **Ancak, bu seçeneğin yalnızca GitHub Codespaces kullanıyorsanız çalıştığını unutmayın.** Docker Desktop kullanıyorsanız .env dosyasını yine de yapılandırmanız gerekir.

## `.env` dosyasını doldurun

Değişken adlarına hızlıca bakalım ve ne anlama geldiklerini anlayalım:

| Değişken  | Açıklama  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Profilinizde oluşturduğunuz kullanıcı erişim belirteci |
| OPENAI_API_KEY | Azure olmayan OpenAI uç noktalarını kullanmak için yetkilendirme anahtarı |
| AZURE_OPENAI_API_KEY | Bu servisi kullanmak için yetkilendirme anahtarı |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI kaynağı için dağıtılmış uç nokta |
| AZURE_OPENAI_DEPLOYMENT | _Metin oluşturma_ model dağıtımı uç noktası |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _Metin gömme_ model dağıtımı uç noktası |
| AZURE_INFERENCE_ENDPOINT | Microsoft Foundry projeniz için uç nokta, Microsoft Foundry Modelleri için kullanılır |
| AZURE_INFERENCE_CREDENTIAL | Microsoft Foundry projeniz için API anahtarı |
| | |

Not: Son iki Azure OpenAI değişkeni sırasıyla sohbet tamamlama (metin oluşturma) ve vektör arama (gömme) için varsayılan modeli yansıtır. Bunları ayarlama talimatları ilgili atamalarda açıklanacaktır.

## Azure OpenAI Yapılandırması: Portal üzerinden

> **Not:** Azure OpenAI Hizmeti artık [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) parçası. Kaynaklar ve dağıtımlar hâlâ Azure Portal'da görünür ancak günlük model yönetimi (dağıtımlar, oyun alanı, izleme) artık eskiden bağımsız olan "Azure OpenAI Studio" yerine Foundry portalında gerçekleşiyor.

Azure OpenAI uç noktası ve anahtar değerleri [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)'da bulunur, o yüzden oradan başlayalım.

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)'a gidin
1. Kenar çubuğundaki (soldaki menü) **Anahtarlar ve Uç Nokta** seçeneğine tıklayın.
1. **Anahtarları Göster**'e tıklayın - şu görüntülenmelidir: ANAHTAR 1, ANAHTAR 2 ve Uç Nokta.
1. AZURE_OPENAI_API_KEY için ANAHTAR 1 değerini kullanın
1. AZURE_OPENAI_ENDPOINT için Uç Nokta değerini kullanın

Sonra, dağıttığımız özel modeller için uç noktalara ihtiyacımız var.

1. Azure OpenAI kaynak için kenar çubuğundaki (soldaki menü) **Model dağıtımları** seçeneğine tıklayın.
1. Hedef sayfada **Microsoft Foundry portalına git**'e tıklayın (veya kaynak türünüze bağlı olarak **Dağıtımları Yönet**).

Bu sizi Microsoft Foundry portalına götürecektir; diğer değerleri aşağıda açıklanan şekilde orada bulacağız.

## Azure OpenAI Yapılandırması: Microsoft Foundry portalından

1. Yukarıdaki açıklamaya göre kaynağınızdan [Microsoft Foundry portalına](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) gidin.
1. Dağıtılmış modelleri görmek için **Dağıtımlar** sekmesine (kenar çubuğu, sol) tıklayın.
1. İstediğiniz model dağıtılmamışsa, [model kataloğundan](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) dağıtmak için **Model dağıt** seçeneğini kullanın.
1. Bir _metin oluşturma_ modeline ihtiyacınız olacak - önerimiz: **gpt-4o-mini**
1. Bir _metin gömme_ modeline ihtiyacınız olacak - önerimiz **text-embedding-3-small**

Artık ortam değişkenlerini kullandığınız _Dağıtım adı_ ile güncelleyin. Bu genellikle model adıyla aynı olacaktır, eğer açıkça değiştirmediyseniz. Örnek olarak şunlara sahip olabilirsiniz:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**İşiniz bittiğinde .env dosyasını kaydetmeyi unutmayın**. Artık dosyadan çıkabilir ve defter çalıştırma talimatlarına dönebilirsiniz.

## OpenAI Yapılandırması: Profil üzerinden

OpenAI API anahtarınız, [OpenAI hesabınızda](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) bulunabilir. Yoksa, bir hesap oluşturabilir ve API anahtarı oluşturabilirsiniz. Anahtarı aldıktan sonra, `.env` dosyasındaki `OPENAI_API_KEY` değişkenini doldurmak için kullanabilirsiniz.

## Hugging Face Yapılandırması: Profil üzerinden

Hugging Face belirteciniz profilinizde [Erişim Belirteçleri](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) altında bulunabilir. Bunları halka açık paylaşmayın. Bunun yerine, bu proje kullanımı için yeni bir belirteç oluşturun ve `.env` dosyasındaki `HUGGING_FACE_API_KEY` değişkenine yapıştırın. _Not:_ Teknik olarak bu bir API anahtarı değildir ama kimlik doğrulama için kullanılır, bu yüzden tutarlılık açısından bu adlandırma korunuyor.

## Microsoft Foundry Modelleri Yapılandırması: Portal üzerinden

> **Not:** GitHub Modelleri 27 Temmuz 2026 sonunda emekliye ayrılıyor. Microsoft Foundry Modelleri doğrudan onun yerine geçiyor, aynı ücretsiz deneme model kataloğu ve Azure AI Inference SDK / OpenAI SDK deneyimini sunuyor.

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)'a gidin ve bir Foundry projesi oluşturun (veya açın).
1. [Model kataloğunu](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) inceleyin ve örneğin `gpt-4o-mini` modelini dağıtın.
1. Projenin **Genel Bakış** sayfasında **uç nokta** ve **API anahtarını** kopyalayın.
1. `.env` dosyanızda `AZURE_INFERENCE_ENDPOINT` için uç nokta değerini, `AZURE_INFERENCE_CREDENTIAL` için anahtar değerini kullanın.

## Çevrimdışı / Yerel Sağlayıcılar

Bulut aboneliği hiç kullanmak istemiyorsanız, uyumlu açık modelleri doğrudan kendi cihazınızda çalıştırabilirsiniz:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft'un cihaz üzeri çalışma zamanı. En iyi yürütme sağlayıcısını (NPU, GPU veya CPU) otomatik olarak seçer ve OpenAI uyumlu uç nokta sunar, böylece bu kurstaki örnek kodların çoğunu minimal değişiklikle tekrar kullanabilirsiniz. Başlamak için [Foundry Local belgelerine](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) bakın veya `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS) ile kurun.
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - Llama, Phi, Mistral ve Gemma gibi açık modelleri yerel olarak çalıştırmak için popüler bir alternatif.


Her iki seçeneği de kullanarak uygulamalı örnekler için [Ders 19: SLM'lerle İnşaat](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) sayfasına bakın.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->