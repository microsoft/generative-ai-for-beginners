# AGENTS.md

## Proje Genel Bakışı

Bu depo, Üretken Yapay Zeka temellerini ve uygulama geliştirmeyi öğreten kapsamlı, 21 derslik bir müfredat içerir. Kurs, yeni başlayanlar için tasarlanmış olup temel kavramlardan üretime hazır uygulamalar geliştirmeye kadar her şeyi kapsar.

**Temel Teknolojiler:**
- Python 3.9+ ve kütüphaneler: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- Node.js ile TypeScript/JavaScript ve kütüphaneler: `openai` (Azure OpenAI v1 uç noktası + Yanıtlar API), `@azure-rest/ai-inference` (Microsoft Foundry Modelleri)
- Azure OpenAI Hizmeti, OpenAI API ve Microsoft Foundry Modelleri (GitHub Modelleri Temmuz 2026 sonunda kullanımdan kalkıyor)
- Etkileşimli öğrenme için Jupyter Notebooks
- Tutarlı geliştirme ortamı için Dev Containers

**Depo Yapısı:**
- 21 numaralandırılmış ders dizini (00-21) içerisinde README'ler, kod örnekleri ve ödevler
- Birden çok uygulama: Python, TypeScript ve bazen .NET örnekleri
- 40+ dil sürümü içeren çeviri dizini
- `.env` dosyası aracılığıyla merkezi konfigürasyon (`.env.copy` şablon olarak kullanılır)

## Kurulum Komutları

### İlk Depo Kurulumu

```bash
# Depoyu klonla
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Ortam şablonunu kopyala
cp .env.copy .env
# .env dosyasını API anahtarlarınız ve uç noktalarınız ile düzenleyin
```

### Python Ortamının Kurulumu

```bash
# Sanal ortam oluştur
python3 -m venv venv

# Sanal ortamı etkinleştir
# macOS/Linux üzerinde:
source venv/bin/activate
# Windows üzerinde:
venv\Scripts\activate

# Bağımlılıkları yükle
pip install -r requirements.txt
```

### Node.js/TypeScript Kurulumu

```bash
# Kök düzeyde bağımlılıkları kurun (belgelendirme araçları için)
npm install

# Bireysel ders TypeScript örnekleri için, belirli derse gidin:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container Kurulumu (Önerilir)

Depo, GitHub Codespaces veya VS Code Dev Containers için `.devcontainer` konfigürasyonu içerir:

1. Depoyu GitHub Codespaces veya VS Code Dev Containers uzantısı ile açın
2. Dev Container otomatik olarak:
   - `requirements.txt` içindeki Python bağımlılıklarını kurar
   - Oluşturma sonrası betiği çalıştırır (`.devcontainer/post-create.sh`)
   - Jupyter çekirdeği kurar

## Geliştirme İş Akışı

### Ortam Değişkenleri

API erişimi gerektiren tüm dersler `.env` dosyasında tanımlanan ortam değişkenlerini kullanır:

- `OPENAI_API_KEY` - OpenAI API için
- `AZURE_OPENAI_API_KEY` - Microsoft Foundry'de Azure OpenAI için (Azure OpenAI Hizmeti artık Microsoft Foundry parçası: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI uç nokta URL'si (Foundry kaynak uç noktası)
- `AZURE_OPENAI_DEPLOYMENT` - Sohbet tamamlama modeli dağıtım adı
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Embeddings modeli dağıtım adı
- `AZURE_OPENAI_API_VERSION` - API sürümü (varsayılan: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Hugging Face modelleri için
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Modelleri uç noktası (çok sağlayıcılı model kataloğu)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Modelleri API anahtarı (emekliye ayrılan `GITHUB_TOKEN` yerine)

### Python Örneklerini Çalıştırmak

```bash
# Ders dizinine gidin
cd 06-text-generation-apps/python

# Bir Python betiği çalıştırın
python aoai-app.py
```

### TypeScript Örneklerini Çalıştırmak

```bash
# TypeScript uygulama dizinine git
cd 06-text-generation-apps/typescript/recipe-app

# TypeScript kodunu derle
npm run build

# Uygulamayı çalıştır
npm start
```

### Jupyter Notebooks Çalıştırmak

```bash
# Jupyter'ı depo kökünde başlat
jupyter notebook

# Veya Jupyter eklentisi ile VS Code kullanın
```

### Farklı Ders Türleri ile Çalışmak

- **"Learn" dersleri**: README.md belgeleri ve kavramlara odaklanır
- **"Build" dersleri**: Python ve TypeScript'te çalışan kod örnekleri içerir
- Her ders bir README.md içerir: teori, kod açılamaları ve video bağlantıları

## Kod Stili Rehberi

### Python

- Ortam değişkeni yönetimi için `python-dotenv` kullanın
- API etkileşimleri için `openai` kütüphanesini içe aktarın
- Kod incelemesi için `pylint` kullanın (bazı örneklerde basitlik için `# pylint: disable=all` vardır)
- PEP 8 isimlendirme kurallarına uyun
- API kimlik bilgilerini `.env` dosyasında saklayın, asla koda yazmayın

### TypeScript

- Ortam değişkenleri için `dotenv` paketi kullanın
- Her uygulama için `tsconfig.json` TypeScript konfigürasyonu
- Azure OpenAI için `openai` paketi (istemciyi `/openai/v1/` uç noktasına yönlendirin ve `client.responses.create` çağırın); Microsoft Foundry Modelleri için `@azure-rest/ai-inference` kullanın
- Oto-yenilemeli geliştirme için `nodemon` kullanın
- Çalıştırmadan önce derleyin: `npm run build` sonra `npm start`

### Genel Kurallar

- Kod örneklerini basit ve eğitici tutun
- Anahtar kavramları açıklayan yorumlar ekleyin
- Her dersin kodu kendi içinde tam ve çalıştırılabilir olmalı
- Tutarlı isimlendirme kullanın: Azure OpenAI için `aoai-`, OpenAI API için `oai-`, Microsoft Foundry Modelleri için `githubmodels-` (GitHub Modelleri döneminden kalan eski önek)

## Dokümantasyon Kılavuzları

### Markdown Stili

- Tüm URL'ler `[text](../../url)` formatında boşluksuz olmalıdır
- Göreli bağlantılar `./` veya `../` ile başlamalıdır
- Microsoft alan adlarına yapılan tüm bağlantılar izleme kimliği içermelidir: `?WT.mc_id=academic-105485-koreyst`
- URL'lerde ülkeye özgü yerel ayarlar kullanılmamalıdır (örneğin `/en-us/` kaçının)
- Görseller `./images` klasöründe açıklayıcı isimlerle saklanmalı
- Dosya adlarında İngilizce karakterler, rakamlar ve tireler kullanılmalı

### Çeviri Desteği

- Depo, GitHub Actions ile 40+ dili otomatik olarak destekler
- Çeviriler `translations/` dizininde saklanır
- Kısmi çeviri gönderimleri yapılmamalıdır
- Makine çevirileri kabul edilmez
- Çevrilmiş görseller `translated_images/` dizininde saklanır

## Test ve Doğrulama

### Gönderim Öncesi Kontroller

Bu depo, doğrulama için GitHub Actions kullanır. PR göndermeden önce:

1. **Markdown Bağlantılarını Kontrol Edin**:
   ```bash
   # validate-markdown.yml iş akışı şunları kontrol eder:
   # - Kırık göreli yollar
   # - Yollarda eksik izleme kimlikleri
   # - URL'lerde eksik izleme kimlikleri
   # - Ülke yerel ayarına sahip URL'ler
   # - Kırık harici URL'ler
   ```

2. **Manuel Test**:
   - Python örneklerini test edin: venv'i etkinleştirin ve betikleri çalıştırın
   - TypeScript örneklerini test edin: `npm install`, `npm run build`, `npm start`
   - Ortam değişkenlerinin doğru yapılandırıldığını doğrulayın
   - API anahtarlarının kod örnekleri ile çalıştığını kontrol edin

3. **Kod Örnekleri**:
   - Tüm kodun hatasız çalışmasını sağlayın
   - Uygun olduğunda hem Azure OpenAI hem OpenAI API ile test edin
   - Desteklenen yerlerde Microsoft Foundry Modelleri ile örneklerin çalıştığını doğrulayın

### Otomatik Test Yok

Bu eğitim deposu, öğreticiler ve örnekler üzerine odaklıdır. Çalıştırılacak birim testi veya entegrasyon testi yoktur. Doğrulama esas olarak:
- Kod örneklerinin manuel testi
- Markdown doğrulaması için GitHub Actions
- Eğitim içeriğinin topluluk incelemesi

## Pull Request Kılavuzları

### Göndermeden Önce

1. Uygunsa hem Python hem TypeScript kod değişikliklerini test edin
2. Markdown doğrulamasını çalıştırın (PR ile otomatik tetiklenir)
3. Tüm Microsoft URL'lerinde izleme kimliklerinin olduğundan emin olun
4. Göreli bağlantıların geçerli olduğunu kontrol edin
5. Görsellerin doğru şekilde referans verildiğini doğrulayın

### PR Başlık Formatı

- Açıklayıcı başlıklar kullanın: `[Lesson 06] Python örneği hata düzeltme` veya `Ders 08 için README güncelleme`
- Uygunsa ilgili sorun numaralarını referans gösterin: `Fixes #123`

### PR Açıklaması

- Nelerin değiştirildiğini ve nedenini açıklayın
- İlgili sorunlara bağlantı verin
- Kod değişiklikleri için hangi örneklerin test edildiğini belirtin
- Çeviri PR'ları için tüm dosyaların tam çeviri olarak eklendiğinden emin olun

### Katkı Koşulları

- Microsoft CLA imzalayın (ilk PR'de otomatik)
- Değişiklik yapmadan önce depoyu kendi hesabınıza çatallayın
- Her mantıksal değişiklik için bir PR yapın (alakasız düzeltmeleri birleştirmeyin)
- Mümkünse PR'ları odaklı ve küçük tutun

## Yaygın İş Akışları

### Yeni Bir Kod Örneği Ekleme

1. İlgili ders dizinine gidin
2. Örneği `python/` veya `typescript/` alt dizininde oluşturun
3. İsimlendirme kuralına uyun: `{provider}-{example-name}.{py|ts|js}`
4. Gerçek API kimlik bilgileri ile test edin
5. Herhangi yeni ortam değişkenlerini ders README'sinde belgeleyin

### Dokümantasyonu Güncelleme

1. Ders dizinindeki README.md dosyasını düzenleyin
2. Markdown kurallarına uyun (izleme kimlikleri, göreli bağlantılar)
3. Çeviriler GitHub Actions tarafından yönetilir (manüel düzenlemeyin)
4. Tüm bağlantıların geçerli olduğunu test edin

### Dev Containers ile Çalışma

1. Depoda `.devcontainer/devcontainer.json` dosyası bulunur
2. Oluşturma sonrası betik, Python bağımlılıklarını otomatik kurar
3. Python ve Jupyter eklentileri önceden yapılandırılmıştır
4. Ortam `mcr.microsoft.com/devcontainers/universal:2.11.2` bazlıdır

## Dağıtım ve Yayınlama

Bu bir öğrenim deposudur - herhangi bir dağıtım süreci yoktur. Müfredat şu yollarla kullanılır:

1. **GitHub Deposu**: Koda ve dokümantasyona doğrudan erişim
2. **GitHub Codespaces**: Önceden yapılandırılmış anlık geliştirme ortamı
3. **Microsoft Learn**: İçerik resmi öğrenme platformunda yayınlanabilir
4. **docsify**: Markdown'dan oluşturulmuş dokümantasyon sitesi (bkz. `docsifytopdf.js` ve `package.json`)

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
- Python sürümünün 3.9+ olduğunu kontrol edin

**TypeScript Derleme Hataları**:
- İlgili uygulama dizininde `npm install` çalıştırın
- Node.js sürümünün uyumlu olduğundan emin olun
- Gerekirse `node_modules` klasörünü temizleyip yeniden kurun

**API Doğrulama Hataları**:
- `.env` dosyasının varlığını ve doğru değerleri kontrol edin
- API anahtarlarının geçerli ve süresi dolmamış olduğundan emin olun
- Bölgenize uygun uç nokta URL'lerinin doğru olduğundan emin olun

**Eksik Ortam Değişkenleri**:
- `.env.copy` dosyasını `.env` olarak kopyalayın
- Üzerinde çalıştığınız ders için tüm gerekli değerleri doldurun
- `.env` güncellendikten sonra uygulamanızı yeniden başlatın

## Ek Kaynaklar

- [Kurs Kurulum Rehberi](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Katkı Kılavuzu](./CONTRIBUTING.md)
- [Davranış Kuralları](./CODE_OF_CONDUCT.md)
- [Güvenlik Politikası](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Gelişmiş Kod Örnekleri Koleksiyonu](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Proje Özel Notları

- Bu, üretim kodu değil, öğrenime odaklı bir **eğitim deposu**
- Örnekler kasıtlı olarak basit ve kavram öğretmeye yönelik
- Kod kalitesi eğitim açıklığı ile dengelenmiştir
- Her ders bağımsız tamamlanabilir, kendi içinde tamdır
- Depo, birden çok API sağlayıcısını destekler: Azure OpenAI, OpenAI, Microsoft Foundry Modelleri ve Foundry Local ile Ollama gibi çevrimdışı sağlayıcılar
- İçerik çok dilli olup otomatik çeviri iş akışlarına sahiptir
- Sorular ve destek için aktif bir Discord topluluğu mevcuttur

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->