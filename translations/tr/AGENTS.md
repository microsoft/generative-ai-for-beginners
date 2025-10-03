<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:01:51+00:00",
  "source_file": "AGENTS.md",
  "language_code": "tr"
}
-->
# AGENTS.md

## Proje Genel Bakış

Bu depo, Generative AI temellerini ve uygulama geliştirmeyi öğreten 21 derslik kapsamlı bir müfredat içerir. Kurs, başlangıç seviyesindeki kullanıcılar için tasarlanmıştır ve temel kavramlardan üretime hazır uygulamalar oluşturmaya kadar her şeyi kapsar.

**Anahtar Teknolojiler:**
- Python 3.9+ ve kütüphaneler: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript ve Node.js kütüphaneleri: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Hizmeti, OpenAI API ve GitHub Modelleri
- Etkileşimli öğrenim için Jupyter Notebooks
- Tutarlı bir geliştirme ortamı için Dev Containers

**Depo Yapısı:**
- 21 numaralandırılmış ders dizini (00-21), README'ler, kod örnekleri ve ödevler içerir
- Birden fazla uygulama: Python, TypeScript ve bazen .NET örnekleri
- 40+ dil versiyonuyla çeviri dizini
- Merkezi yapılandırma `.env` dosyası üzerinden (şablon olarak `.env.copy` kullanın)

## Kurulum Komutları

### Depo İlk Kurulumu

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Python Ortamı Kurulumu

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Node.js/TypeScript Kurulumu

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container Kurulumu (Önerilir)

Depo, GitHub Codespaces veya VS Code Dev Containers için bir `.devcontainer` yapılandırması içerir:

1. Depoyu GitHub Codespaces veya Dev Containers uzantısı ile VS Code'da açın
2. Dev Container otomatik olarak:
   - `requirements.txt` dosyasından Python bağımlılıklarını yükler
   - Post-create script'i çalıştırır (`.devcontainer/post-create.sh`)
   - Jupyter kernelini kurar

## Geliştirme İş Akışı

### Ortam Değişkenleri

API erişimi gerektiren tüm dersler `.env` dosyasında tanımlanan ortam değişkenlerini kullanır:

- `OPENAI_API_KEY` - OpenAI API için
- `AZURE_OPENAI_API_KEY` - Azure OpenAI Hizmeti için
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI endpoint URL'si
- `AZURE_OPENAI_DEPLOYMENT` - Sohbet tamamlama modeli dağıtım adı
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Embeddings modeli dağıtım adı
- `AZURE_OPENAI_API_VERSION` - API versiyonu (varsayılan: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Hugging Face modelleri için
- `GITHUB_TOKEN` - GitHub Modelleri için

### Python Örneklerini Çalıştırma

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### TypeScript Örneklerini Çalıştırma

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Jupyter Notebooks ile Çalışma

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Farklı Ders Türleriyle Çalışma

- **"Learn" dersleri**: README.md belgelerine ve kavramlara odaklanır
- **"Build" dersleri**: Python ve TypeScript'te çalışan kod örnekleri içerir
- Her ders, teori, kod incelemeleri ve video içerik bağlantıları içeren bir README.md dosyasına sahiptir

## Kod Stili Yönergeleri

### Python

- Ortam değişkenlerini yönetmek için `python-dotenv` kullanın
- API etkileşimleri için `openai` kütüphanesini içe aktarın
- Linting için `pylint` kullanın (bazı örneklerde basitlik için `# pylint: disable=all` bulunur)
- PEP 8 adlandırma kurallarına uyun
- API kimlik bilgilerini `.env` dosyasında saklayın, kodda asla saklamayın

### TypeScript

- Ortam değişkenleri için `dotenv` paketini kullanın
- Her uygulama için `tsconfig.json` içinde TypeScript yapılandırması
- Azure hizmetleri için `@azure/openai` veya `@azure-rest/ai-inference` kullanın
- Otomatik yeniden yükleme ile geliştirme için `nodemon` kullanın
- Çalıştırmadan önce derleyin: `npm run build` ardından `npm start`

### Genel Kurallar

- Kod örneklerini basit ve eğitici tutun
- Anahtar kavramları açıklayan yorumlar ekleyin
- Her dersin kodu bağımsız ve çalıştırılabilir olmalıdır
- Tutarlı adlandırma kullanın: Azure OpenAI için `aoai-`, OpenAI API için `oai-`, GitHub Modelleri için `githubmodels-`

## Belgelendirme Yönergeleri

### Markdown Stili

- Tüm URL'ler `[metin](../../url)` formatında olmalı, ekstra boşluk olmamalı
- Göreceli bağlantılar `./` veya `../` ile başlamalı
- Microsoft alan adlarına yapılan tüm bağlantılar izleme kimliği içermeli: `?WT.mc_id=academic-105485-koreyst`
- URL'lerde ülkeye özgü yerel ayarları kullanmayın (örneğin `/en-us/`'tan kaçının)
- Görseller `./images` klasöründe açıklayıcı adlarla saklanmalı
- Dosya adlarında İngilizce karakterler, rakamlar ve tireler kullanılmalı

### Çeviri Desteği

- Depo, GitHub Actions aracılığıyla 40+ dili destekler
- Çeviriler `translations/` dizininde saklanır
- Kısmi çeviriler gönderilmemelidir
- Makine çevirileri kabul edilmez
- Çevrilmiş görseller `translated_images/` dizininde saklanır

## Test ve Doğrulama

### Gönderim Öncesi Kontroller

Bu depo, doğrulama için GitHub Actions kullanır. PR göndermeden önce:

1. **Markdown Bağlantılarını Kontrol Et**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Manuel Test**:
   - Python örneklerini test edin: venv'i etkinleştirin ve scriptleri çalıştırın
   - TypeScript örneklerini test edin: `npm install`, `npm run build`, `npm start`
   - Ortam değişkenlerinin doğru yapılandırıldığını doğrulayın
   - API anahtarlarının kod örnekleriyle çalıştığını kontrol edin

3. **Kod Örnekleri**:
   - Tüm kodun hatasız çalıştığından emin olun
   - Uygulanabilir olduğunda hem Azure OpenAI hem de OpenAI API ile test edin
   - GitHub Modelleri desteklendiğinde örneklerin çalıştığını doğrulayın

### Otomatik Test Yok

Bu, eğitim odaklı bir depo olup, öğreticiler ve örnekler üzerine yoğunlaşır. Çalıştırılacak birim testleri veya entegrasyon testleri yoktur. Doğrulama öncelikle:
- Kod örneklerinin manuel testi
- Markdown doğrulaması için GitHub Actions
- Eğitim içeriğinin topluluk incelemesi

## Pull Request Yönergeleri

### Göndermeden Önce

1. Python ve TypeScript'teki kod değişikliklerini test edin (uygulanabilir olduğunda)
2. Markdown doğrulamasını çalıştırın (PR'de otomatik olarak tetiklenir)
3. Tüm Microsoft URL'lerinde izleme kimliklerinin bulunduğundan emin olun
4. Göreceli bağlantıların geçerli olduğunu kontrol edin
5. Görsellerin doğru şekilde referans alındığını doğrulayın

### PR Başlık Formatı

- Açıklayıcı başlıklar kullanın: `[Lesson 06] Fix Python example typo` veya `Update README for lesson 08`
- Uygulanabilir olduğunda sorun numaralarına referans verin: `Fixes #123`

### PR Açıklaması

- Ne değiştiğini ve neden değiştiğini açıklayın
- İlgili sorunlara bağlantı verin
- Kod değişiklikleri için hangi örneklerin test edildiğini belirtin
- Çeviri PR'leri için tüm dosyaları içeren eksiksiz bir çeviri ekleyin

### Katılım Gereksinimleri

- Microsoft CLA'yı imzalayın (ilk PR'de otomatik olarak yapılır)
- Deponun bir kopyasını hesabınıza fork edin ve değişiklikleri yapın
- Her mantıksal değişiklik için bir PR gönderin (ilgili olmayan düzeltmeleri birleştirmeyin)
- PR'leri mümkün olduğunca odaklı ve küçük tutun

## Yaygın İş Akışları

### Yeni Bir Kod Örneği Ekleme

1. İlgili ders dizinine gidin
2. `python/` veya `typescript/` alt dizininde örnek oluşturun
3. Adlandırma kurallarına uyun: `{provider}-{example-name}.{py|ts|js}`
4. Gerçek API kimlik bilgileriyle test edin
5. Yeni ortam değişkenlerini ders README'sinde belgeleyin

### Belgeleri Güncelleme

1. Ders dizinindeki README.md dosyasını düzenleyin
2. Markdown yönergelerine uyun (izleme kimlikleri, göreceli bağlantılar)
3. Çeviri güncellemeleri GitHub Actions tarafından işlenir (manuel olarak düzenlemeyin)
4. Tüm bağlantıların geçerli olduğunu test edin

### Dev Containers ile Çalışma

1. Depo `.devcontainer/devcontainer.json` içerir
2. Post-create script Python bağımlılıklarını otomatik olarak yükler
3. Python ve Jupyter için uzantılar önceden yapılandırılmıştır
4. Ortam `mcr.microsoft.com/devcontainers/universal:2.11.2` tabanlıdır

## Dağıtım ve Yayınlama

Bu bir öğrenim deposudur - herhangi bir dağıtım süreci yoktur. Müfredat şu yollarla tüketilir:

1. **GitHub Deposu**: Kod ve belgelere doğrudan erişim
2. **GitHub Codespaces**: Önceden yapılandırılmış kurulumla anında geliştirme ortamı
3. **Microsoft Learn**: İçerik resmi öğrenim platformuna aktarılabilir
4. **docsify**: Markdown'dan oluşturulan belge sitesi (bkz. `docsifytopdf.js` ve `package.json`)

### Belge Sitesi Oluşturma

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Sorun Giderme

### Yaygın Sorunlar

**Python İçe Aktarma Hataları**:
- Sanal ortamın etkinleştirildiğinden emin olun
- `pip install -r requirements.txt` çalıştırın
- Python sürümünün 3.9+ olduğundan emin olun

**TypeScript Derleme Hataları**:
- Belirli uygulama dizininde `npm install` çalıştırın
- Node.js sürümünün uyumlu olduğundan emin olun
- `node_modules` klasörünü temizleyin ve yeniden yükleyin

**API Kimlik Doğrulama Hataları**:
- `.env` dosyasının mevcut olduğunu ve doğru değerler içerdiğini doğrulayın
- API anahtarlarının geçerli ve süresi dolmamış olduğundan emin olun
- Endpoint URL'lerinin bölgeniz için doğru olduğundan emin olun

**Eksik Ortam Değişkenleri**:
- `.env.copy` dosyasını `.env` olarak kopyalayın
- Çalıştığınız ders için gerekli tüm değerleri doldurun
- `.env` güncellendikten sonra uygulamanızı yeniden başlatın

## Ek Kaynaklar

- [Kurs Kurulum Kılavuzu](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Katkı Sağlama Yönergeleri](./CONTRIBUTING.md)
- [Davranış Kuralları](./CODE_OF_CONDUCT.md)
- [Güvenlik Politikası](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Gelişmiş Kod Örnekleri Koleksiyonu](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projeye Özel Notlar

- Bu, **eğitim odaklı bir depo** olup, üretim koduna değil öğrenmeye odaklanır
- Örnekler, kavramları öğretmeye odaklanarak kasıtlı olarak basittir
- Kod kalitesi, eğitimsel açıklıkla dengelenmiştir
- Her ders bağımsızdır ve tek başına tamamlanabilir
- Depo, birden fazla API sağlayıcısını destekler: Azure OpenAI, OpenAI ve GitHub Modelleri
- İçerik, otomatik çeviri iş akışlarıyla çok dilli olarak sunulur
- Sorular ve destek için Discord'da aktif bir topluluk bulunmaktadır

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı bir yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dilindeki hali, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmez.