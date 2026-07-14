# Gelişmiş Özellikler ve İyileştirmeler Yol Haritası

Bu belge, kapsamlı bir kod incelemesi ve sektörün en iyi uygulamalarının analizi temelinde Başlangıç Seviyesi Üretken AI müfredatı için önerilen geliştirmeler ve iyileştirmeleri özetlemektedir.

## Yönetici Özeti

Kod tabanı güvenlik, kod kalitesi ve eğitsel etkinlik açısından analiz edilmiştir. Bu belge, hemen uygulanacak düzeltmeler, kısa vadeli iyileştirmeler ve gelecekteki geliştirmeler için öneriler sunmaktadır.

---

## 1. Güvenlik İyileştirmeleri (Öncelik: Kritik)

### 1.1 Hemen Düzeltmeler (Tamamlandı)

| Sorun | Etkilenen Dosyalar | Durum |
|-------|----------------|--------|
| Sabit kodlanmış SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Düzeltildi |
| Eksik env doğrulaması | Birden fazla JS/TS dosyası | Düzeltildi |
| Güvensiz fonksiyon çağrıları | `11-integrating-with-function-calling/js-githubmodels/app.js` | Düzeltildi |
| Dosya tutucu sızıntıları | `08-building-search-applications/scripts/` | Düzeltildi |
| Eksik istek zaman aşımı | `09-building-image-applications/python/` | Düzeltildi |

### 1.2 Önerilen Ek Güvenlik Özellikleri

1. **Oran Sınırlandırma Örnekleri**
   - API çağrıları için oran sınırlandırmanın nasıl uygulanacağını gösteren örnek kod ekleyin
   - Üssel geri çekilme desenlerini gösterin

2. **API Anahtarı Rotasyonu**
   - API anahtarlarının rotasyonu için en iyi uygulamalar hakkında dokümantasyon ekleyin
   - Azure Key Vault veya benzeri servislerin kullanım örneklerini dahil edin

3. **İçerik Güvenliği Entegrasyonu**
   - Azure İçerik Güvenliği API'si kullanarak örnekler ekleyin
   - Girdi/çıktı moderasyonu desenlerini gösterin

---

## 2. Kod Kalitesi İyileştirmeleri

### 2.1 Konfigürasyon Dosyaları Eklendi

| Dosya | Amaç |
|------|---------|
| `.eslintrc.json` | JavaScript/TypeScript lint kuralları |
| `.prettierrc` | Kod formatlama standartları |
| `pyproject.toml` | Python araç konfigürasyonu (Black, Ruff, mypy) |

### 2.2 Ortak Yardımcılar Oluşturuldu

Yeni `shared/python/` modülü ile:
- `env_utils.py` - Ortam değişkeni işlemleri
- `input_validation.py` - Girdi doğrulama ve temizleme
- `api_utils.py` - Güvenli API istek sarmalayıcıları

### 2.3 Önerilen Kod İyileştirmeleri

1. **Tür İpucu Kapsamı**
   - Tüm Python dosyalarına tür ipuçları ekleyin
   - Tüm TS projelerinde katı TypeScript modu etkinleştirin

2. **Dokümantasyon Standartları**
   - Tüm Python fonksiyonlarına docstring ekleyin
   - Tüm JavaScript/TypeScript fonksiyonlarına JSDoc yorumları ekleyin

3. **Test Çerçevesi**
   - pytest konfigürasyonu ve örnek testler ekleyin _(tamamlandı: `pyproject.toml` içinde pytest konfigürasyonu; paylaşılan yardımcı modüller için [`tests/`](../../../tests) içinde örnek testler CI’da çalıştırılıyor)_
   - JavaScript/TypeScript için Jest konfigürasyonu ekleyin

---

## 3. Eğitsel İyileştirmeler

### 3.1 Yeni Ders Konuları

1. **AI Uygulamalarında Güvenlik** (Önerilen Ders 22)
   - İstem enjeksiyonu saldırıları ve savunmaları
   - API anahtarı yönetimi
   - İçerik moderasyonu
   - Oran sınırlandırma ve kötüye kullanım önleme

2. **Üretim Dağıtımı** (Önerilen Ders 23)
   - Docker ile konteynerleştirme
   - CI/CD boru hatları
   - İzleme ve günlükleme
   - Maliyet yönetimi

3. **Gelişmiş RAG Teknikleri** (Önerilen Ders 24)
   - Hibrit arama (anahtar kelime + anlamsal)
   - Yeniden sıralama stratejileri
   - Çok modlu RAG
   - Değerlendirme metrikleri

### 3.2 Mevcut Ders İyileştirmeleri

| Ders | Önerilen İyileştirme |
|--------|------------------------|
| 06 - Metin Üretimi | Akışlı yanıt örnekleri ekleyin |
| 07 - Sohbet Uygulamaları | Konuşma hafızası desenleri ekleyin |
| 08 - Arama Uygulamaları | Vektör veritabanı karşılaştırması ekleyin |
| 09 - Görsel Üretimi | Görsel düzenleme/çeşitlendirme örnekleri ekleyin |
| 11 - Fonksiyon Çağrısı | Paralel fonksiyon çağrısı ekleyin |
| 15 - RAG | Parçalama stratejisi karşılaştırması ekleyin |
| 17 - AI Ajanları | Çoklu ajan orkestrasyonu ekleyin |

---

## 4. API Modernizasyonu

### 4.1 Kullanımdan Kaldırılmış API Desenleri (Geçiş Tamamlandı)

Tüm Python ve TypeScript **sohbet** örnekleri, Chat Completions API'den **Responses API**'e (`client.responses.create(...)` → `response.output_text`) taşındı.

| Eski Desen | Yeni Desen | Durum |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (sohbet) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | Tamamlandı |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | Tamamlandı |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | `openai` paketi `client.responses.create()` → `response.output_text` | Tamamlandı |
| `df.append()` (pandas) | `pd.concat()` | Tamamlandı |

> **Not:** `azure-ai-inference` / `@azure-rest/ai-inference` SDK'sını (`client.complete()`) kullanan Microsoft Foundry Modelleri örnekleri Model İnferans API'sinde kalmaya devam ediyor ve Responses API'yi desteklememektedir. `AzureOpenAI()` hala geçerli olduğu yerlerde (embedding ve görsel üretim) kasıtlı olarak korunmuştur.

### 4.2 Gösterilecek Yeni API Özellikleri

1. **Yapılandırılmış Çıktılar** (OpenAI)
   - JSON modu
   - Kesin şemalarla fonksiyon çağrısı

2. **Görsel Yetenekler**
   - GPT-4o (görsel) ile görüntü analizi
   - Çok modlu istemler

3. **Responses API Yerleşik Araçları** (eski Assistants API'nin yerine geçer)
   - Kod yorumlayıcı
   - Dosya arama
   - Web arama ve özel araçlar

---

## 5. Altyapı İyileştirmeleri

### 5.1 CI/CD İyileştirmeleri

[`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml) dosyasında uygulandı: Python linting/formatlama (Ruff + Black) `shared/` yardımcı modülünde **zorunlu** olup müfredatın geri kalanında **öneri** olarak çalışır, ayrıca JavaScript/TypeScript için öneri ESLint geçişi içerir. Örnek temel şudur:

```yaml
# .github/workflows/code-quality.yml
name: Code Quality

on: [push, pull_request]

jobs:
  python-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - run: pip install ruff black mypy
      - run: ruff check .
      - run: black --check .

  js-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npx eslint .
```

### 5.2 Güvenlik Taraması

[`.github/workflows/security.yml`](../../../.github/workflows/security.yml) dosyasında uygulandı: Python ve JavaScript/TypeScript için CodeQL analizi (push, pull request ve haftalık takvimde) ve bağımlılık incelemesi pull requestlerde. Örnek temel şudur:

```yaml
# .github/workflows/security.yml
name: Security Scan

on: [push, pull_request]

jobs:
  codeql:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: javascript, python
      - uses: github/codeql-action/analyze@v3

  dependency-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/dependency-review-action@v4
```

---

## 6. Geliştirici Deneyimi İyileştirmeleri

### 6.1 DevContainer İyileştirmeleri

[`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) ve [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh) içinde uygulandı: konteyner artık Pylance, Black , Ruff, ESLint, Prettier ve Copilot eklentileriyle birlikte gelir, kayıt sırasında formatlama özelliği repo'nun Black/Prettier konfigürasyonuna bağlı olarak etkinleştirilir ve geliştirici araçları (`ruff`, `black`, `mypy`, `pytest`) kurulur, böylece [code-quality workflow](../../../.github/workflows/code-quality.yml) yerel olarak tekrarlanabilir. `mcr.microsoft.com/devcontainers/universal` temel imajı Python ve Node içerdiğinden ekstra özellik gerekmez. Örnek temel şudur:

```json
{
  "name": "Generative AI for Beginners",
  "image": "mcr.microsoft.com/devcontainers/universal:2",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.11"
    },
    "ghcr.io/devcontainers/features/node:1": {
      "version": "20"
    }
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-toolsai.jupyter",
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "github.copilot"
      ],
      "settings": {
        "python.formatting.provider": "black",
        "editor.formatOnSave": true
      }
    }
  },
  "postCreateCommand": "pip install -e .[dev] && npm install"
}
```

### 6.2 Etkileşimli Oyun Alanı

Şunları eklemeyi düşünün:
- Ortam değişkeni ile önceden doldurulmuş API anahtarları içeren Jupyter defterleri
- Görsel öğrenenler için Gradio/Streamlit demoları
- Bilgi değerlendirmesi için etkileşimli testler

---

## 7. Çok Dilli Destek

### 7.1 Mevcut Dil Kapsamı

| Teknoloji | Kapsanan Dersler | Durum |
|------------|-----------------|--------|
| Python | Tüm dersler | Tamamlandı |
| TypeScript | 06-09, 11 | Kısmi |
| JavaScript | 06-08, 11 | Kısmi |
| .NET/C# | Bazı dersler | Kısmi |

### 7.2 Önerilen Eklentiler

1. **Go** - AI/ML araçlarında büyüyor
2. **Rust** - Performans kritik uygulamalar
3. **Java/Kotlin** - Kurumsal uygulamalar

---

## 8. Performans Optimizasyonları

### 8.1 Kod Seviyesi Optimizasyonlar

1. **Async/Await Desenleri**
   - Toplu işlem için async örnekleri ekleyin
   - Eşzamanlı API çağrılarını gösterin

2. **Önbellekleme Stratejileri**
   - Embedding önbellekleme örnekleri ekleyin
   - Yanıt önbellekleme desenlerini gösterin

3. **Token Optimizasyonu**
   - tiktoken kullanım örnekleri ekleyin
   - İstem sıkıştırma tekniklerini gösterin

### 8.2 Maliyet Optimizasyonu Örnekleri

Aşağıdaki konuları gösteren örnekler ekleyin:
- Görev karmaşıklığına göre model seçimi
- Token verimliliği için istem mühendisliği
- Toplu işlemler için batch işleme

---

## 9. Erişilebilirlik ve Uluslararasılaştırma

### 9.1 Mevcut Çeviri Durumu

Tüm çeviriler, müfredatın İngilizce kaynağı ile senkronize edilen 50'den fazla dil versiyonu otomatik olarak üreten ve güncelleyen [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) tarafından otomatik olarak tamamlanmıştır. Çevrilmiş içerik `translations/` altında, yerelleştirilmiş görseller `translated_images/` altında bulunmakta; mevcut dillerin tam listesi depo README'sinin başında yayınlanmıştır.

| Kapsam | Durum |
|--------|--------|
| Çeviri kapsamı | Tamamlandı — 50+ dil, tüm dersler |
| Çeviri yöntemi | Otomatik, [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) aracılığıyla |
| İngilizce kaynakla senkron | Evet — otomatik yeniden üretim |

### 9.2 Erişilebilirlik İyileştirmeleri

1. Tüm görsellere alt metin ekleyin
2. Kod örneklerinin doğru sözdizimi vurgulamasına sahip olduğundan emin olun
3. Tüm video içerikleri için video transkriptleri ekleyin
4. Renk kontrastının WCAG yönergelerine uyduğundan emin olun

---

## 10. Uygulama Önceliği

### Aşama 1: Hemen (1-2. Hafta)
- [x] Kritik güvenlik sorunlarını düzeltin
- [x] Kod kalitesi konfigürasyonu ekleyin
- [x] Ortak yardımcılar oluşturun
- [x] Güvenlik yönergelerini belgeleyin

### Aşama 2: Kısa Vadeli (3-4. Hafta)
- [x] Kullanımdan kaldırılmış API desenlerini güncelleyin (Chat Completions → Responses API, Python + TypeScript)
- [ ] Tüm Python dosyalarına tür ipuçları ekleyin (`shared/` modülü için yapıldı; ders örnekleri basit tutuldu)
- [x] Kod kalitesi için CI/CD iş akışları ekleyin
- [x] Güvenlik tarama iş akışı oluşturun

### Aşama 3: Orta Vadeli (2-3. Ay)
- [ ] Yeni güvenlik dersi ekleyin
- [ ] Üretim dağıtım dersi ekleyin
- [x] DevContainer kurulumu iyileştirin
- [ ] Etkileşimli demolar ekleyin

### Aşama 4: Uzun Vadeli (4. Ay ve sonrası)
- [ ] Gelişmiş RAG dersi ekleyin
- [ ] Dil kapsamını genişletin
- [ ] Kapsamlı test süiti ekleyin
- [ ] Sertifikasyon programı oluşturun

---

## Sonuç

Bu yol haritası, Başlangıç Seviyesi Üretken AI müfredatını iyileştirmek için yapılandırılmış bir yaklaşım sunar. Güvenlik endişelerini ele alarak, API'leri modernize ederek ve eğitsel içerik ekleyerek, kurs öğrencileri gerçek dünya AI uygulama geliştirme için daha iyi hazırlayacaktır.

Sorular veya katkılar için lütfen GitHub deposunda bir issue açın.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->