<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T16:47:35+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "tr"
}
-->
# Bir LLM Sağlayıcısı Seçmek ve Yapılandırmak 🔑

Ödevler, OpenAI, Azure veya Hugging Face gibi desteklenen bir servis sağlayıcı üzerinden bir veya birden fazla Büyük Dil Modeli (LLM) dağıtımıyla çalışacak şekilde de ayarlanabilir. Bu sağlayıcılar, doğru kimlik bilgileriyle (API anahtarı veya token) programlı olarak erişebileceğimiz _barındırılan bir uç nokta_ (API) sunar. Bu derste şu sağlayıcıları ele alıyoruz:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst): Çekirdek GPT serisi dahil olmak üzere çeşitli modeller sunar.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst): Kurumsal odaklı OpenAI modelleri için
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst): Açık kaynak modeller ve çıkarım sunucusu için

**Bu alıştırmalar için kendi hesaplarınızı kullanmanız gerekecek.** Ödevler isteğe bağlıdır; ilginize göre birini, hepsini veya hiçbirini kurabilirsiniz. Kayıt için bazı öneriler:

| Kayıt | Maliyet | API Anahtarı | Playground | Yorumlar |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Fiyatlandırma](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Proje bazlı](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Kodsuz, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Birden fazla model mevcut |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Fiyatlandırma](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Hızlı Başlangıç](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Hızlı Başlangıç](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Erişim için önceden başvuru yapılmalı](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Fiyatlandırma](https://huggingface.co/pricing) | [Erişim Tokenları](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat'te sınırlı model var](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Aşağıdaki adımları izleyerek bu depoyu farklı sağlayıcılarla kullanmak için _yapılandırabilirsiniz_. Belirli bir sağlayıcı gerektiren ödevlerin dosya adında şu etiketlerden biri bulunur:

- `aoai` - Azure OpenAI uç noktası ve anahtarı gerekir
- `oai` - OpenAI uç noktası ve anahtarı gerekir
- `hf` - Hugging Face token gerekir

Bir, hiçbir veya tüm sağlayıcıları yapılandırabilirsiniz. İlgili ödevler, kimlik bilgileri eksikse hata verecektir.

## `.env` Dosyası Oluşturma

Yukarıdaki yönergeleri okuduğunuzu, ilgili sağlayıcıya kaydolduğunuzu ve gerekli kimlik bilgilerini (API_KEY veya token) aldığınızı varsayıyoruz. Azure OpenAI için ayrıca, en az bir GPT modelinin sohbet tamamlaması için dağıtıldığı geçerli bir Azure OpenAI Servisi (uç nokta) dağıtımınızın olduğunu varsayıyoruz.

Bir sonraki adımda, **yerel ortam değişkenlerinizi** şu şekilde yapılandırmalısınız:

1. Kök klasörde, aşağıdaki gibi içeriğe sahip bir `.env.copy` dosyası arayın:

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

2. Bu dosyayı aşağıdaki komutla `.env` olarak kopyalayın. Bu dosya _gitignore_ ile gizlenir, böylece gizli bilgiler korunur.

   ```bash
   cp .env.copy .env
   ```

3. Sonraki bölümde açıklandığı gibi değerleri doldurun (`=` işaretinin sağındaki yer tutucuları değiştirin).

4. (Opsiyonel) GitHub Codespaces kullanıyorsanız, ortam değişkenlerini bu depoyla ilişkili _Codespaces secrets_ olarak kaydedebilirsiniz. Bu durumda, yerel bir .env dosyası oluşturmanıza gerek kalmaz. **Ancak, bu seçenek yalnızca GitHub Codespaces kullanıyorsanız geçerlidir.** Docker Desktop kullanıyorsanız yine de .env dosyasını oluşturmanız gerekir.

## `.env` Dosyasını Doldurma

Değişken adlarının neyi temsil ettiğini hızlıca inceleyelim:

| Değişken  | Açıklama  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Profilinizde oluşturduğunuz kullanıcı erişim tokenıdır |
| OPENAI_API_KEY | Azure dışı OpenAI uç noktaları için servis yetkilendirme anahtarıdır |
| AZURE_OPENAI_API_KEY | Bu servisi kullanmak için yetkilendirme anahtarıdır |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI kaynağı için dağıtılmış uç noktadır |
| AZURE_OPENAI_DEPLOYMENT | _Metin üretimi_ modeli dağıtım uç noktasıdır |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _Metin gömme_ modeli dağıtım uç noktasıdır |
| | |

Not: Son iki Azure OpenAI değişkeni, sırasıyla sohbet tamamlaması (metin üretimi) ve vektör arama (gömme) için varsayılan modeli yansıtır. Bunların nasıl ayarlanacağı ilgili ödevlerde açıklanacaktır.

## Azure'u Yapılandırma: Portal Üzerinden

Azure OpenAI uç noktası ve anahtar değerlerini [Azure Portalı](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) üzerinden bulabilirsiniz, bu yüzden oradan başlayalım.

1. [Azure Portalı](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) adresine gidin
1. Sol menüde **Anahtarlar ve Uç Nokta** seçeneğine tıklayın.
1. **Anahtarları Göster**'e tıklayın - şu değerleri görmelisiniz: KEY 1, KEY 2 ve Uç Nokta.
1. AZURE_OPENAI_API_KEY için KEY 1 değerini kullanın
1. AZURE_OPENAI_ENDPOINT için Uç Nokta değerini kullanın

Şimdi, dağıttığımız belirli modellerin uç noktalarına ihtiyacımız var.

1. Azure OpenAI kaynağı için sol menüde **Model dağıtımları** seçeneğine tıklayın.
1. Açılan sayfada **Dağıtımları Yönet**'e tıklayın

Bu sizi Azure OpenAI Studio web sitesine götürecek, burada aşağıda açıklandığı gibi diğer değerleri bulacağız.

## Azure'u Yapılandırma: Studio Üzerinden

1. Yukarıda açıklandığı gibi **kaynağınızdan** [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) adresine gidin.
1. Sol menüde **Dağıtımlar** sekmesine tıklayarak mevcut dağıtılmış modelleri görüntüleyin.
1. İstediğiniz model dağıtılmamışsa, **Yeni dağıtım oluştur** seçeneğiyle dağıtın.
1. Bir _metin üretimi_ modeline ihtiyacınız olacak - önerimiz: **gpt-35-turbo**
1. Bir _metin gömme_ modeline ihtiyacınız olacak - önerimiz **text-embedding-ada-002**

Şimdi ortam değişkenlerini, kullandığınız _Dağıtım adı_ ile güncelleyin. Bunu değiştirmediyseniz genellikle model adıyla aynıdır. Örneğin şöyle olabilir:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**İşiniz bittiğinde .env dosyasını kaydetmeyi unutmayın.** Artık dosyadan çıkabilir ve not defterini çalıştırma talimatlarına dönebilirsiniz.

## OpenAI'yi Yapılandırma: Profil Üzerinden

OpenAI API anahtarınızı [OpenAI hesabınızda](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) bulabilirsiniz. Henüz bir anahtarınız yoksa, bir hesap oluşturup API anahtarı oluşturabilirsiniz. Anahtarı aldıktan sonra, `.env` dosyasındaki `OPENAI_API_KEY` değişkenine ekleyebilirsiniz.

## Hugging Face'i Yapılandırma: Profil Üzerinden

Hugging Face tokenınızı profilinizde [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) bölümünde bulabilirsiniz. Bunları herkese açık olarak paylaşmayın veya yayınlamayın. Bunun yerine, bu proje için yeni bir token oluşturun ve bunu `.env` dosyasındaki `HUGGING_FACE_API_KEY` değişkenine ekleyin. _Not:_ Teknik olarak bu bir API anahtarı değildir, ancak kimlik doğrulama için kullanılır, bu yüzden tutarlılık için bu isimlendirme kullanılmıştır.

---

**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerde hata veya yanlışlıklar bulunabilir. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından doğabilecek herhangi bir yanlış anlama veya yanlış yorumlamadan sorumlu değiliz.