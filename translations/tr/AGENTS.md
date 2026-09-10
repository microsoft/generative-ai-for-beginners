# AGENTS.md

## Proje Genel Bakışı

Bu depo, Üretken Yapay Zeka temel bilgileri ve uygulama geliştirmeyi öğreten kapsamlı 21 derslik bir müfredat içerir. Kurs, yeni başlayanlar için tasarlanmış olup temel kavramlardan üretime hazır uygulamalar oluşturmaya kadar her şeyi kapsar.

**Ana Teknolojiler:**
- Python 3.9+ ve kütüphaneler: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- Node.js ile TypeScript/JavaScript ve kütüphaneler: `openai` (Azure OpenAI v1 endpoint ve Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Modelleri)
- Azure OpenAI Servisi, OpenAI API ve Microsoft Foundry Modelleri (GitHub Modelleri Temmuz 2026 sonunda kullanımdan kalkıyor)
- Etkileşimli öğrenme için Jupyter Notebooks
- Tutarlı geliştirme ortamı için Dev Containers

**Depo Yapısı:**
- 21 numaralandırılmış ders dizinleri (00-21) içinde README’ler, kod örnekleri ve ödevler
- Birden çok uygulama: Python, TypeScript ve bazen .NET örnekleri
- 40+ dil versiyonları içeren çeviri dizini
- Merkezi yapılandırma `.env` dosyası ile (şablon olarak `.env.copy` kullanılabilir)

## Kurulum Komutları

### Başlangıç Depo Kurulumu

```bash
# Depoyu klonlayın
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Ortam şablonunu kopyalayın
cp .env.copy .env
# API anahtarlarınız ve uç noktalarınızla .env dosyasını düzenleyin
```

### Python Ortamının Kurulumu

```bash
# Sanal ortam oluştur
python3 -m venv venv

# Sanal ortamı aktifleştir
# macOS/Linux üzerinde:
source venv/bin/activate
# Windows üzerinde:
venv\Scripts\activate

# Bağımlılıkları yükle
pip install -r requirements.txt
```

### Node.js/TypeScript Kurulumu

```bash
# Kök düzeyde bağımlılıkları yükleyin (dokümantasyon araçları için)
npm install

# Bireysel ders TypeScript örnekleri için, belirli derse gidin:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container Kurulumu (Önerilir)

Depo, GitHub Codespaces veya VS Code Dev Containers için `.devcontainer` yapılandırmasını içerir:

1. Depoyu GitHub Codespaces veya Dev Containers eklentisi ile VS Code’da açın
2. Dev Container otomatik olarak:
   - `requirements.txt` dosyasından Python bağımlılıklarını yükler
   - Post-create scriptini çalıştırır (`.devcontainer/post-create.sh`)
   - Jupyter çekirdeğini kurar

## Geliştirme İş Akışı

### Ortam Değişkenleri

API erişimi gerektiren tüm dersler `.env` dosyasında tanımlanan ortam değişkenlerini kullanır:

- `OPENAI_API_KEY` - OpenAI API için
- `AZURE_OPENAI_API_KEY` - Microsoft Foundry’de Azure OpenAI için (Azure OpenAI Servisi artık Microsoft Foundry’nin parçası: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI uç nokta URL’si (Foundry kaynak uç noktası)
- `AZURE_OPENAI_DEPLOYMENT` - Chat tamamlama modeli dağıtım adı (kurs varsayılanı: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Embeddings modeli dağıtım adı (kurs varsayılanı: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - API sürümü (varsayılan: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Hugging Face modelleri için
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Modeller uç noktası (çok sağlayıcılı model kataloğu)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Modeller API anahtarı (`GITHUB_TOKEN` yerine geçer)
- `AZURE_INFERENCE_CHAT_MODEL` - `temperature` örneklerinde kullanılan, örnekleme kontrollerini desteklemeyen bir akıl yürütme modeli olmayan model (ör. `Llama-3.3-70B-Instruct`)

### Model Kuralları (önemli)

- **Varsayılan sohbet modeli `gpt-5-mini`** - güncel, kullanımdan kalkmamış bir **akıl yürütme** modeli. 2026 itibarıyla daha eski, sıcaklık destekli "mini" modeller (`gpt-4o-mini`, `gpt-4.1-mini`) *kullanımdan kaldırılmaktadır*, bu nedenle müfredat GPT-5 ailesine standartlaştırılmıştır.
- **Akıl yürütme modelleri `temperature` ve `top_p` parametrelerini reddeder**, ve `max_output_tokens` (Responses API) / `max_completion_tokens` (sohbet tamamlama) kullanır; `max_tokens` kullanılmaz. `gpt-5-mini` çağıran örneklere `temperature`/`top_p`/`max_tokens` eklemeyin.
- **`temperature` göstermek için** örneklerde Microsoft Foundry Modeller uç noktası (`AZURE_INFERENCE_CHAT_MODEL`) üzerinden bir **Llama** modeli (`Llama-3.3-70B-Instruct`) kullanılır. Akıl yürütme modellerini örnekleme düğmeleri yerine prompt mühendisliği ve akıl yürütme kontrolleriyle yönlendirin.
- **Mikro eğitim (ders 18)** `gpt-4.1-mini` modelini korur: GPT-5 yalnızca pekiştirmeli mikro eğitim (RFT) destekler, orada gösterilen denetimli mikro eğitim (SFT) değil.
- Dersler 20 (Mistral) ve 21 (Meta) `temperature`/`max_tokens` parametrelerini korur çünkü Mistral/Llama modellerini hedeflerler, bu parametreleri desteklerler.

### Python Örneklerini Çalıştırma

```bash
# Ders dizinine gidin
cd 06-text-generation-apps/python

# Bir Python betiği çalıştırın
python aoai-app.py
```

### TypeScript Örneklerini Çalıştırma

```bash
# TypeScript uygulama dizinine gidin
cd 06-text-generation-apps/typescript/recipe-app

# TypeScript kodunu derleyin
npm run build

# Uygulamayı çalıştırın
npm start
```

### Jupyter Notebooks Çalıştırma

```bash
# Depo kökünde Jupyter'i başlat
jupyter notebook

# Veya Jupyter eklentisi ile VS Code'u kullanın
```

### Farklı Ders Türleriyle Çalışma

- **"Öğren" dersleri**: README.md belgeleri ve kavramlara odaklanır
- **"İnşa et" dersleri**: Python ve TypeScript'te çalışan kod örnekleri içerir
- Her dersin teori, kod açıklamaları ve video bağlantıları içeren bir README.md dosyası vardır

## Kod Stili Kılavuzları

### Python

- Ortam değişkenleri yönetimi için `python-dotenv` kullanın
- API etkileşimleri için `openai` kütüphanesini içe aktarın
- Linting için `pylint` kullanın (bazı örneklerde basitlik için `# pylint: disable=all` bulunmaktadır)
- PEP 8 isimlendirme kurallarına uyun
- API kimlik bilgilerini `.env` dosyasına kaydedin, kodda asla tutmayın

### TypeScript

- Ortam değişkenleri için `dotenv` paketi kullanın
- Her uygulama için `tsconfig.json` TypeScript yapılandırması
- Azure OpenAI için `openai` paketini kullanın (istemciyi `/openai/v1/` endpoint’ine yönlendirin ve `client.responses.create` çağırın); Microsoft Foundry Modelleri için `@azure-rest/ai-inference` kullanın
- Otomatik yenileme ile geliştirme için `nodemon` kullanın
- Çalıştırmadan önce inşa edin: `npm run build` sonra `npm start`

### Genel Kurallar

- Kod örneklerini basit ve öğretici tutun
- Anahtar kavramları açıklayan yorumlar ekleyin
- Her dersin kodu kendi içinde tamamlanabilir ve çalıştırılabilir olmalı
- Tutarlı isimlendirme kullanın: Azure OpenAI için `aoai-` ön eki, OpenAI API için `oai-`, Microsoft Foundry Modelleri için `githubmodels-` (GitHub Modelleri döneminden kalan eski ön ek)

## Dokümantasyon Kılavuzları

### Markdown Stili

- Tüm URL’ler fazladan boşluk olmadan `[text](../../url)` formatında olmalı
- Göreceli bağlantılar `./` veya `../` ile başlamalı
- Microsoft alan adlarına yapılan tüm bağlantılar izleme kimliği içermeli: `?WT.mc_id=academic-105485-koreyst`
- URL'lerde ülkeye özel yerel ayarlar olmamalı (örneğin `/en-us/` kullanımından kaçının)
- Görseller `./images` klasöründe açıklayıcı adlarla saklanır
- Dosya adlarında İngilizce harfler, sayılar ve tire kullanılmalı

### Çeviri Desteği

- Depo, otomatik GitHub Actions ile 40+ dil desteği sunar
- Çeviriler `translations/` dizininde tutulur
- Kısmi çeviriler gönderilmemelidir
- Makine çevirileri kabul edilmez
- Çevrilmiş görseller `translated_images/` dizininde saklanır

## Test ve Doğrulama

### Gönderim Öncesi Kontroller

Bu depo doğrulama için GitHub Actions kullanır. PR göndermeden önce:

1. **Markdown Bağlantılarını Kontrol Edin**:
   ```bash
   # The validate-markdown.yml iş akışı şunları kontrol eder:
   # - Kırık göreli yollar
   # - Yollarda eksik takip kimlikleri
   # - URL'lerde eksik takip kimlikleri
   # - Ülke yerel ayarına sahip URL'ler
   # - Kırık dış URL'ler
   ```

2. **Manuel Test**:
   - Python örneklerini test edin: Sanal ortamı etkinleştirin ve betikleri çalıştırın
   - TypeScript örneklerini test edin: `npm install`, `npm run build`, `npm start`
   - Ortam değişkenlerinin doğru yapılandırıldığını doğrulayın
   - Kod örnekleriyle API anahtarlarının çalıştığını kontrol edin

3. **Kod Örnekleri**:
   - Tüm kodun hatasız çalıştığından emin olun
   - Uygunsa hem Azure OpenAI hem OpenAI API ile test edin
   - Desteklenen yerlerde Microsoft Foundry Modellerle çalıştığını doğrulayın

### Otomatik Test Yok

Bu eğitim amaçlı bir depo olup birim testi veya entegrasyon testi yoktur. Doğrulama öncelikle şunlardan oluşur:
- Kod örneklerinin manuel testi
- Markdown doğrulama için GitHub Actions
- Eğitim içeriğinin topluluk incelemesi

## Çekme İsteği (Pull Request) Kılavuzları

### Göndermeden Önce

1. Uygun ise hem Python hem TypeScript’te kod değişikliklerini test edin
2. Markdown doğrulamasını çalıştırın (PR ile otomatik tetiklenir)
3. Tüm Microsoft URL’lerinde izleme kimliklerinin varlığını doğrulayın
4. Göreceli bağlantıların geçerli olduğunu kontrol edin
5. Görsellerin doğru referanslandığını doğrulayın

### PR Başlık Formatı

- Açıklayıcı başlıklar kullanın: `[Lesson 06] Python örneğinde yazım hatası düzeltme` veya `Ders 08 için README güncellemesi`
- Uygunsa ilgili issue numaralarına referans verin: `Fixes #123`

### PR Açıklaması

- Ne değiştirildi ve neden açıkça belirtin
- İlgili issue’lara bağlantı verin
- Kod değişikliklerinde hangi örneklerin test edildiğini açıklayın
- Çeviri PR’lerinde tamamlanmış çeviri için tüm dosyalar dahil edilmeli

### Katkı Koşulları

- Microsoft CLA’ya imza atın (ilk PR’de otomatik)
- Değişiklik yapmadan önce depoyu kendi hesabınıza fork edin
- Her mantıksal değişiklik için bir PR oluşturun (ilgili olmayan düzeltmeleri birleştirmeyin)
- Mümkün olduğunca PR’leri odaklı ve küçük tutun

## Ortak İş Akışları

### Yeni Bir Kod Örneği Ekleme

1. İlgili ders dizinine gidin
2. `python/` veya `typescript/` alt dizininde örnek oluşturun
3. İsimlendirme kurallarına uyun: `{provider}-{örnek-ismi}.{py|ts|js}`
4. Gerçek API kimlik bilgileriyle test edin
5. Yeni ortam değişkenlerini ders README’sinde belgeleyin

### Dokümantasyonu Güncelleme

1. Ders dizinindeki README.md dosyasını düzenleyin
2. Markdown kurallarına uyun (izleme kimlikleri, göreceli bağlantılar)
3. Çeviriler GitHub Actions tarafından otomatik güncellenir (manuel değişiklik yapmayın)
4. Tüm bağlantıların geçerli olduğundan emin olun

### Dev Containers ile Çalışma

1. Depoda `.devcontainer/devcontainer.json` dosyası bulunur
2. Post-create script otomatik olarak Python bağımlılıklarını yükler
3. Python ve Jupyter için eklentiler önceden yapılandırılmıştır
4. Ortam `mcr.microsoft.com/devcontainers/universal:2.11.2` temel alınmıştır

## Dağıtım ve Yayınlama

Bu öğrenme amaçlı bir depo - dağıtım süreci yoktur. Müfredat şu yollardan tüketilir:

1. **GitHub Deposu**: Koda ve dokümantasyona doğrudan erişim
2. **GitHub Codespaces**: Önceden yapılandırılmış anlık geliştirme ortamı
3. **Microsoft Learn**: İçerik resmi öğrenme platformuna entegre edilebilir
4. **docsify**: Markdown’dan oluşturulmuş dokümantasyon sitesi (`docsifytopdf.js` ve `package.json` bakınız)

### Dokümantasyon Sitesi Oluşturma

```bash
# Gerekirse belgelerden PDF oluşturun
npm run convert
```

## Sorun Giderme

### Yaygın Sorunlar

**Python İçe Aktarma Hataları**:
- Sanal ortamın etkinleştirildiğinden emin olun
- `pip install -r requirements.txt` komutunu çalıştırın
- Python sürümünün 3.9+ olduğundan emin olun

**TypeScript Derleme Hataları**:
- Belirli uygulama dizininde `npm install` çalıştırın
- Node.js sürümünün uyumlu olduğunu kontrol edin
- Gerekirse `node_modules` klasörünü temizleyip yeniden yükleyin

**API Kimlik Doğrulama Hataları**:
- `.env` dosyasının mevcut ve doğru değerler içerdiğini doğrulayın
- API anahtarlarının geçerli ve süresinin dolmamış olduğunu kontrol edin
- Bölgenize uygun uç nokta URL’lerinin doğru olduğundan emin olun

**Eksik Ortam Değişkenleri**:
- `.env.copy` dosyasını `.env` olarak kopyalayın
- Üzerinde çalıştığınız derse ait tüm gerekli değerleri doldurun
- `.env` güncellendikten sonra uygulamanızı yeniden başlatın

## Ek Kaynaklar

- [Kurs Kurulum Kılavuzu](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Katkı Sağlama Kılavuzları](./CONTRIBUTING.md)
- [Davranış Kuralları](./CODE_OF_CONDUCT.md)
- [Güvenlik Politikası](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Gelişmiş Kod Örnekleri Koleksiyonu](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projeye Özel Notlar

- Bu bir **eğitim deposu** olup üretim kodu için değil
- Örnekler bilinçli olarak basit ve kavram öğretmeye odaklıdır
- Kod kalitesi eğitimde açıklıkla dengelenmiştir
- Her ders bağımsızdır ve tek başına tamamlanabilir
- Depo birden çok API sağlayıcısını destekler: Azure OpenAI, OpenAI, Microsoft Foundry Modelleri ve offline sağlayıcılar (Foundry Local, Ollama gibi)
- İçerik çok dilli olup otomatik çeviri iş akışları vardır
- Sorular ve destek için Discord’da aktif bir topluluk mevcuttur

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->