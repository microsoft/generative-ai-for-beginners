# Bir LLM Sağlayıcısı Seçme ve Yapılandırma 🔑

Ödevler, OpenAI, Azure veya Hugging Face gibi desteklenen bir hizmet sağlayıcısı aracılığıyla bir veya daha fazla Büyük Dil Modeli (LLM) dağıtımına karşı çalışacak şekilde **ayarlanabilir**. Bunlar, doğru kimlik bilgileri (API anahtarı veya belirteci) ile programatik olarak erişebileceğimiz _barındırılan bir uç nokta_ (API) sağlar. Bu derste, bu sağlayıcıları tartışıyoruz:

 - Çeşitli modelleri içeren [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), temel GPT serisi dahil.
 - Kurumsal hazır olma odaklı OpenAI modelleri için [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)
 - Açık kaynak modeller ve çıkarım sunucusu için [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)

**Bu alıştırmalar için kendi hesaplarınızı kullanmanız gerekecek**. Ödevler isteğe bağlıdır, bu nedenle ilgi alanlarınıza göre birini, hepsini veya hiçbiri sağlayıcıyı kurmayı seçebilirsiniz. Kayıt için bazı rehberlik:

| Kayıt | Ücret | API Anahtarı | Oyun Alanı | Yorumlar |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Fiyatlandırma](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Proje bazlı](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Kod Gerektirmez, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Birden Çok Model Mevcut |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Fiyatlandırma](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Hızlı Başlangıç](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Hızlı Başlangıç](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Erişim İçin Önceden Başvurulmalı](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Fiyatlandırma](https://huggingface.co/pricing) | [Erişim Belirteçleri](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat sınırlı modellere sahip](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Bu depoyu farklı sağlayıcılarla kullanmak üzere _yapılandırmak_ için aşağıdaki talimatları izleyin. Belirli bir sağlayıcı gerektiren ödevler, dosya adlarında aşağıdaki etiketlerden birini içerecektir:

- `aoai` - Azure OpenAI uç noktası, anahtarı gerektirir
- `oai` - OpenAI uç noktası, anahtarı gerektirir
- `hf` - Hugging Face belirteci gerektirir

Birini, hiçbirini veya tüm sağlayıcıları yapılandırabilirsiniz. İlgili ödevler, eksik kimlik bilgileri durumunda hata verecektir.

## `.env` dosyası oluşturun

Yukarıdaki rehberi okuduğunuzu, ilgili sağlayıcıya kaydolduğunuzu ve gerekli kimlik doğrulama bilgilerini (API_KEY veya belirteç) aldığınızı varsayıyoruz. Azure OpenAI durumunda, en az bir GPT modeli sohbet tamamlama için dağıtılmış geçerli bir Azure OpenAI Hizmeti (uç noktası) dağıtımınızın da olduğunu varsayıyoruz.

Bir sonraki adım, **yerel ortam değişkenlerinizi** aşağıdaki gibi yapılandırmaktır:

1. Kök klasörde `.env.copy` adlı bir dosya arayın; içeriği şu şekilde olmalıdır:

   ```bash
   # OpenAI Sağlayıcı
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Varsayılan ayarlandı!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Aşağıdaki komutla bu dosyayı `.env` olarak kopyalayın. Bu dosya _gitignore_ edilmiştir, sırları güvende tutar.

   ```bash
   cp .env.copy .env
   ```

3. Değerleri doldurun (`=` işaretinin sağ tarafındaki yer tutucuları değiştirin) ve sonraki bölümde açıklandığı gibi.

4. (İsteğe bağlı) GitHub Codespaces kullanıyorsanız, ortam değişkenlerini bu depoyla ilişkili _Codespaces sırları_ olarak kaydetme seçeneğiniz vardır. Bu durumda, yerel .env dosyası kurmanıza gerek kalmaz. **Ancak, bu seçeneğin yalnızca GitHub Codespaces kullanıyorsanız çalıştığını unutmayın.** Docker Desktop kullanıyorsanız yine .env dosyasını kurmanız gerekecektir.

## `.env` dosyasını doldurun

Değişken adlarının ne anlama geldiğini anlamak için hızlıca bakalım:

| Değişken  | Açıklama  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Profilinizde ayarladığınız kullanıcı erişim belirtecidir |
| OPENAI_API_KEY | Azure dışı OpenAI uç noktaları için hizmeti kullanma yetkilendirme anahtarıdır |
| AZURE_OPENAI_API_KEY | Bu hizmeti kullanmak için yetkilendirme anahtarıdır |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI kaynağı için dağıtılmış uç noktadır |
| AZURE_OPENAI_DEPLOYMENT | _metin oluşturma_ model dağıtım uç noktasıdır |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _metin gömme_ model dağıtım uç noktasıdır |
| | |

Not: Son iki Azure OpenAI değişkeni sırasıyla sohbet tamamlama (metin oluşturma) ve vektör arama (gömmeler) için varsayılan modeli yansıtır. Bunların ayarlanmasıyla ilgili talimatlar ilgili ödevlerde tanımlanacaktır.

## Azure'u Yapılandırma: Portal Üzerinden

Azure OpenAI uç noktası ve anahtar değerleri [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) içinde bulunur, o yüzden oradan başlayalım.

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) adresine gidin
1. Kenar çubuğunda (sol menü) **Anahtarlar ve Uç Nokta** seçeneğine tıklayın.
1. **Anahtarları Göster**e tıklayın - aşağıdakileri görmelisiniz: ANAHTAR 1, ANAHTAR 2 ve Uç Nokta.
1. AZURE_OPENAI_API_KEY için ANAHTAR 1 değerini kullanın
1. AZURE_OPENAI_ENDPOINT için Uç Nokta değerini kullanın

Sonra, dağıttığımız belirli modellerin uç noktalarına ihtiyacımız var.

1. Azure OpenAI kaynağı için kenar çubuğunda (sol menü) **Model dağıtımları** seçeneğine tıklayın.
1. Hedef sayfada, **Dağıtımları Yönet**e tıklayın

Bu sizi Azure OpenAI Studio web sitesine götürecek, diğer değerleri aşağıda açıklandığı gibi burada bulacağız.

## Azure'u Yapılandırma: Studio Üzerinden

1. Yukarıda açıklandığı gibi, kaynağınızdan [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) adresine gidin.
1. Şu anda dağıtılmış modelleri görmek için kenar çubuğunda (sol) **Dağıtımlar** sekmesine tıklayın.
1. İstediğiniz model dağıtılmamışsa, dağıtmak için **Yeni dağıtım oluştur**u kullanın.
1. Bir _metin oluşturma_ modeline ihtiyacınız olacak - önerimiz: **gpt-35-turbo**
1. Bir _metin gömme_ modeline ihtiyacınız olacak - önerimiz **text-embedding-ada-002**

Şimdi ortam değişkenlerini, kullanılan _Dağıtım adı_ ile güncelleyin. Bu genellikle modeli açıkça değiştirmediyseniz model adıyla aynı olur. Örneğin, şöyle olabilir:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**İşiniz bittiğinde .env dosyasını kaydetmeyi unutmayın**. Artık dosyadan çıkabilir ve not defterini çalıştırma talimatlarına dönebilirsiniz.

## OpenAI'yi Yapılandırma: Profil Üzerinden

OpenAI API anahtarınız [OpenAI hesabınızda](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) bulunabilir. Henüz yoksa, bir hesap için kaydolabilir ve bir API anahtarı oluşturabilirsiniz. Anahtarı aldıktan sonra `.env` dosyasındaki `OPENAI_API_KEY` değişkenini doldurmak için kullanabilirsiniz.

## Hugging Face'i Yapılandırma: Profil Üzerinden

Hugging Face belirteciniz, profilinizdeki [Erişim Belirteçleri](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) altında bulunabilir. Bunları halka açık paylaşmayın veya yayınlamayın. Bunun yerine, bu proje kullanımı için yeni bir belirteç oluşturun ve `.env` dosyasındaki `HUGGING_FACE_API_KEY` değişkenine kopyalayın. _Not:_ Teknik olarak bu bir API anahtarı değildir ancak kimlik doğrulama için kullanılır, bu yüzden tutarlılık için bu adlandırma biçimini koruyoruz.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->