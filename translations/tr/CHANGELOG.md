# Değişiklik Günlüğü

Başlangıç Seviyesi Üretken Yapay Zeka müfredatındaki tüm önemli değişiklikler bu dosyada belgelenmiştir.

Biçim [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) esas alınmıştır. Bu bir
sürümlenmiş yazılım paketi değil, bir öğrenme müfredatı olduğundan, girdiler tarihe göre gruplanmıştır.

## [2026-07-16] — İçerik Doğrulama + Ders 09 Görsel Varlıkları

### Değiştirildi

- **Ders 10 (düşük kodlu AI uygulamaları):** iki kullanımdan kaldırılmış `docs.microsoft.com/powerapps/...` Dataverse
  linki güncel `learn.microsoft.com/power-apps/maker/data-platform/data-platform-intro` ile değiştirildi
  (canlı olarak doğrulandı).
- **Ders 17 (AI ajanlar):** eski bir model örneği (`GPT-3.5, GPT-4, Llama-2` →
  `GPT-5, GPT-4o, and Llama 3.3`) modernize edildi ve Agent Framework örneğindeki yer tutucu dağıtım adı
  (`my-gpt-4o-deployment` → `my-gpt-5-mini-deployment`) güncellendi.
- **Root `README.md`:** *Microsoft for Startups* linkine eksik `?WT.mc_id=academic-105485-koreyst` takip kimliği
  eklendi.
- **Ders 09 görsel varlıkları** `gpt-image` modeli ile yeniden oluşturuldu: `images/generated-image.png`,
  `images/sunlit_lounge.png`, `images/mask.png`, `images/sunlit_lounge_result.png` ve
  `images/startup.png` (düzenleme örneğinin önce/sonra çifti, gerçek
  `client.images.edit` çağrısı ile oluşturulan maske kullanılarak üretildi).

### Doğrulandı

- Ders 01, 03, 05, 12, 14 ve 16'nın README dosyaları denetlendi — hepsi güncel (doğru Microsoft Foundry
  isimlendirme ve linkler); değişiklik gerekmedi.
- Depreciated doküman yolları, `/en-us/` Microsoft yerelleri, eski ürün/model isimleri,
  eksik takip ID'leri ve bozuk göreceli linkler/görseller açısından 41 depo içi markdown dosyasının (çeviriler hariç)
  tam markdown doğrulaması yapıldı. Tek uygulanabilir sorun *Microsoft for Startups* takip kimliği boşluğu
  bulundu; diğer tüm işaretler yanlış pozitif olarak doğrulandı (otomatik oluşturulmuş çeviri linkleri,
  yorum satırı içindeki yer tutucular ve üçüncü taraf `/en/` yapısal URL’leri).

## [2026-07-15] — Ders 09 (Görsel Uygulamalar) GPT Görsel Modelleri için Yeniden Yazıldı

### Değiştirildi

- **Ders 09 "Görsel Üretim Uygulamaları Geliştirme" mevcut **`gpt-image`** etrafında yeniden yazıldı**
  model ailesi (varsayılan **`gpt-image-2`**; `gpt-image-1.5` / `gpt-image-1-mini` ayrıca GA), değiştirerek
  eski DALL·E 2/3 içeriği. Önemli düzeltmeler:
  - `gpt-image` modelleri resmi bir URL yerine **base64 (`b64_json`)** olarak döndürür. Tüm örnekler buna göre güncellendi
    `base64.b64decode(...)` indirmek yerine `url` ile `requests`.
  - Görüntü API sürümü `2025-04-01-preview` olarak artırıldı.
  - Üretilmiş "sıcaklık" bölümü (görüntü modelleri `temperature` almaz) ve DALL·E-2'ye özgü görüntü **varyasyonları** içeriği, bir **görüntü düzenleme** (maske/yeniden boyama) bölümüyle değiştirildi.
    
  - Hem `README.md`, `python/aoai-app.py`, `python/oai-app.py`, `python/aoai-solution.py` güncellendi,
    atama not defterleri (`aoai-assignment.ipynb`, `oai-assignment.ipynb`),
    `typescript/image-generation-app` (`main.ts`, `.env-sample`) ve .NET `.dib` not defteri.

### Kaldırıldı

- Kullanımdan kaldırılmış `python/aoai-app-variation.py` ve `python/oai-app-variation.py` örnekleri silindi
  (`images.create_variation` sadece DALL·E-2 içindir ve `gpt-image` tarafından desteklenmez).
- Kaldırılan sıcaklık karşılaştırma bölümüyle bağlantılı 4 sahipsiz resim varlığı silindi
  (`v1-generated-image.png`, `v2-generated-image.png`, `v1-temp-generated-image.png`,
  `v2-temp-generated-image.png`).
- Dersin Python örnekleri ve gereksinimlerinden gereksiz `requests` bağımlılığı kaldırıldı.

### Doğrulandı

- `aoai-app.py` dağıtılmış bir `gpt-image-1.5` modeli üzerinde uçtan uca çalıştırıldı ve base64
  çözme/kaydetme akışının bir PNG ürettiği doğrulandı. Not defterlerinin geçerli JSON olduğu onaylandı.

## [2026-07-14] — Varsayılan Model Güncellemesi + Akıl yürütme Modeli Rehberliği

### Değiştirildi

- **Müfredatın çalıştırılabilir örnekleri, belgeleri ve yapılandırması genelinde varsayılan sohbet modeli `gpt-4o-mini` → `gpt-5-mini`** olarak değiştirildi,
  Bu, model yaşam döngüsü durumu tarafından yönlendirildi: Microsoft Foundry'de,
  `gpt-4o-mini` (2026-10-01'de emekli oluyor) ve tüm `gpt-4.1` ailesi (`gpt-4.1`, `gpt-4.1-mini`,
  `gpt-4.1-nano`, 2026-10-14'te emekli oluyor) **Kullanımdan Kaldırılıyor**, oysa **GPT-5 ailesi
  (`gpt-5-mini`, `gpt-5`, `gpt-5-nano`) Genel Kullanıma Açık** (2027-02-06'da emekli oluyor). Güncellendi:
  - `.env.copy`, `00-course-setup/03-providers.md` (önerilen dağıtım ve `az cognitiveservices`
    dağıtım komutları), ve 04, 06, 07 ve 15 dakikleri için README dosyaları.
  - 06 dersindeki Python örnekleri (`oai-app.py`, `oai-app-recipe.py`, `oai-history-bot.py`,
    `oai-study-buddy.py`, `githubmodels-app.py`) ve 08 dersindeki betikler.
  - 06, 07 ve 11 derslerindeki TypeScript / JavaScript örnekleri, ve 06 ve 07 dersleri için `.dib` .NET not defterleri.
  - 04, 06, 07 ve 11 derslerinde atama not defterleri (kod hücreleri) ve ayrıca `shared/python/api_utils.py`
    docstring örnekleri.
    belgelendirme dizesi örnekleri.
- **Sebep-sonuç modeli parametre rehberi (yeni).** `gpt-5-mini` bir *sebep-sonuç* modelidir: **desteklemez**
  `temperature`/`top_p`, ve `max_completion_tokens` (sohbet tamamlama) / 
  `max_output_tokens` (Yanıtlar API) kullanır, `max_tokens` yerine. Buna göre:
  - `temperature`/`top_p`/`max_tokens` kaldırıldı; örneklerde artık varsayılan `gpt-5-mini` oldu
    (`githubmodels-app.py`, `aoai-app-recipe.py`, `oai-app-recipe.py`, ders 15 RAG README).
  - Ders 06'ya, **"Sebep-sonuç modelleri `temperature` kullanmaz"** notu eklendi; sebep-sonuç modellerinin 
    örnekleme düğmeleri yerine **prompt mühendisliği + sebep-sonuç kontrolleri** ile yönlendirildiği
    açıklaması yapıldı; `temperature`/`top_p` ise sebep-sonuç olmayan modellerde geçerliliğini koruyor
    (GPT-4.x, Mistral, Llama, Phi, açık modeller).
- **`gpt-5-mini` ince ayar eğitiminde (ders 18) kullanılmıyor.** GPT-5 sadece
  pekiştirmeli ince ayar (RFT) destekliyor; ders 18 denetimli ince ayar (SFT) kılavuzu `gpt-4.1-mini` kullanmaya devam ediyor,
  bu da SFT/DPO'yu destekliyor.
- **Sıcaklık demoları bir Llama modeli kullanıyor.** Sebep-sonuç modellerinin reddettiği `temperature` öğretimine devam etmek için,
  Foundry Modelleri uç noktası üzerinden bir `Llama-3.3-70B-Instruct` modeli kullanıldı. `AZURE_INFERENCE_CHAT_MODEL` değişkeni eklendi `.env.copy`'a; ders 04/06 `githubmodels` defterleri ve
  `06` `js-githubmodels` örneği bu değişkeni okuyor (varsayılan olarak `Llama-3.3-70B-Instruct`'e dönüyor) ve
  `temperature`/`top_p`/`max_tokens` demolarını koruyor.
- **JS / .NET örnekleri GPT-5 için güncellendi.** GPT-5 örneklerinden `temperature`/`top_p`/`max_tokens` kaldırıldı
  (`06` `recipe-app` TypeScript, `06` `.dib` .NET - ayrıca `MaxOutputTokenCount`
  ekler, böylece sebep-sonuç çıktısı kesilmiyor). `06` `js-githubmodels` örneği artık sıcaklık demosunu sürdürmek için Llama kullanıyor.
  `.dib` notları, .NET'te `Azure.AI.Inference` + Llama modelinin `Temperature`'i göstermek için uygun yol olduğunu söylüyor.
- Doğruluğunu koruyan yerlerde `gpt-4o-mini` / `gpt-5-mini` bırakıldı: `tiktoken`
  token-kodlama referansları, model-katalog erişim listeleri ve ders 02 konuşma modelleri (`gpt-4o-transcribe`).
- Ders 20 (Mistral) ve 21 (Meta) örnekleri `temperature`/`max_tokens` kullandığı sürece aynen korunuyor,
  çünkü Mistral/Llama modellerini hedefliyor, bu parametreleri destekliyorlar.

## [2026-07-06] — İçerik Modernizasyon Yenilemesi

## [2026-07-06] — İçerik Modernizasyonu Yenilemesi

2026 için müfredatı doğru tutmak adına geniş çaplı bir yenileme: modern API'ler, güncel ürün isimleri ve
model isimleri, güncellenmiş sağlayıcı rehberliği ve yeni geliştirici deneyimi araçları.

### Eklendi

- Tek sohbet ajanlarını kapsayan ders `17-ai-agents` içindeki **Microsoft Agent Framework** bölümü,
  araçlar/fonksiyon çağrısı, Azure OpenAI (Microsoft Foundry) yapılandırması ve çoklu ajan
  iş akışı orkestrasyonu (`SequentialBuilder` / `ConcurrentBuilder`).
- **Foundry Local**, `00-course-setup/03-providers.md` ve ders `19-slm` içinde Ollama ile birlikte çevrimdışı / cihaz üstü bir sağlayıcı olarak belgelenmiştir.

- **Sürekli entegrasyon iş akışları**:
  - `.github/workflows/code-quality.yml` — Bakımı yapılan `shared/`
    modülde zorunlu olan Ruff + Black, müfredatın geri kalanında tavsiye edilen ESLint kontrolü ve pytest görevi.
  - `.github/workflows/security.yml` — Kod incelemesinde Python + JavaScript/TypeScript için CodeQL analizi ve bağımlılık gözden geçirme.

- Paylaşılan yardımcı modülü kapsayan 41 pytest testi içeren **Test paketi** `tests/` altında.
- API geçişini yönlendirmek için kullanılan `.github/skills/azure-openai-to-responses/` altında **Azure OpenAI → Responses API geçiş becerisi**.




- **Chat Tamamlama API'si → Yanıtlar API'si** tüm Python ve TypeScript sohbet örneklerinde
  (`client.responses.create(...)` → `response.output_text`), dersler 04, 06, 07, 11, 
  15 ve 18, artı bunların README dosyaları dahil.
- **GitHub Modelleri → Microsoft Foundry Modelleri** tüm metin, bağlantılar ve örneklerde. GitHub Modelleri
  Temmuz 2026 sonunda kullanım dışı bırakılıyor; örnekler artık Microsoft Foundry model kataloğuna işaret ediyor ve
  `AZURE_INFERENCE_ENDPOINT` / `AZURE_INFERENCE_CREDENTIAL` ortam değişkenlerini kullanıyor.
- **`.env.copy`, `AGENTS.md` ve sağlayıcı dokümanları** Azure OpenAI artık Microsoft Foundry'nin bir parçası olarak güncellendi,
  ve varsayılan API sürümü `2024-10-21` olarak yükseltildi.
- **TypeScript örnekleri** (dersler 06, 07, 08, 11) kullanımdan kaldırılan `@azure/openai`
  beta SDK'dan `openai` paketine taşındı (sohbet uygulamaları Responses API'sini; arama uygulaması
  embeddings istemcisini kullanıyor).
- **.NET not defterleri** (`dotnet/*.dib`) `Azure.AI.OpenAI` **2.1.0** üzerinde standartlaştırıldı: dersler 06 ve 07
  `ChatClient` API'sini kullanıyor, ders 08 `EmbeddingClient` (`GenerateEmbedding` / `ToFloats`) kullanıyor ve
  ders 09 `ImageClient` (`GenerateImage`) ile `gpt-image-1` kullanıyor; bu, eski `OpenAIClient` / `GetEmbeddingsAsync` / `GetImageGenerationsAsync` yerine
  `1.0.0-beta.9`'den gelen miras kodları değiştiriyor.
- **Ürün adı modernizasyonu**: "Azure AI Studio" / "Azure AI Foundry" → **Microsoft Foundry**
  (dersler 14, 16, 17) ve "Bing" → **Microsoft Copilot** (ders 12), mevcut ürünlere atıfta bulunulduğunda.
  mevcut ürünler.
- **DevContainer** (`.devcontainer/`) artık Pylance, Black, Ruff, ESLint, Prettier ve Copilot ile geliyor
  uzantılar, kayıt sırasında biçimlendirmeyi etkinleştirir ve CI kontrollerinin yerel olarak çoğaltılabilmesi için `ruff`, `black`, `mypy` ve `pytest` yükler.
  kontrolleri yerel olarak çoğaltılabilir.
- **Görüntü oluşturma** (ders 09) Azure için `gpt-image-1` önerir (Azure kataloğu `dall-e-3`'yi kaldırdı).
  
- **`docs/ENHANCED_FEATURES_ROADMAP.md`** tamamlanmış çalışmaları (API migrasyonu, CI,
  DevContainer, testler) ve güncel gerçekleri yansıtacak şekilde güncellendi (çeviriler, Azure Co-op Translator tarafından otomatik olarak üretilmektedir; Assistants API, Responses API ile değiştirilmiştir).




- **`shared/python/input_validation.py`** — `validate_text_input(allow_empty=True)` artık sadece boşluk içeren girdi için "çok kısa" hatası vermek yerine boş bir dize döndürüyor (bu, `None` durumu ile tutarlıdır). Yeni test paketi tarafından bulundu ve kapsandı.
  
- **Ders 09 resim örnekleri** — gerçek hatalar düzeltildi: `InvalidRequestError` → `BadRequestError`,  
  `images.create` → `images.generate`, `Image.create_variation` → `client.images.create_variation`,  
  ve `openai` modülünü gölgeleyen bir değişken.  
- **Ders 15 RAG defteri** — istemci kurulumu onarıldı, kaldırılan `DataFrame.append` ile `pd.concat` değiştirildi ve eski SDK kullanımı modernize edildi.  
- Kullanımdan kaldırılmış / emekliye ayrılmış model isimleri (`gpt-3.5-turbo`, `gpt-35-turbo`) aktif örneklerde `gpt-4o-mini` ile değiştirildi; ders 18'deki geçmiş ince ayar çıktıları korunarak yeniden yazılmayıp notlandırıldı.  
 
### Kullanımdan kaldırılmış / Notlar  
 
  yeniden yazılmak yerine.

### Kullanımdan Kaldırıldı / Notlar

- **Microsoft Foundry Modelleri örnekleri** `azure-ai-inference` / `@azure-rest/ai-inference`
  SDK'sını (`client.complete()`) kullanır — `githubmodels-*` ve `js-githubmodels` örnekleri ve 19, 20,
  ve 21. dersler — Model Çıkarım API'si üzerinde kalır, bu API Yanıtlar API'sini **desteklemez**. Bunlar
  bilerek o SDK üzerinde bırakıldı.
- `AzureOpenAI()`, hala uygun olduğu yerlerde (gömülü içerikler ve görüntü oluşturma) bilerek korunmuştur,
  çünkü bu iş akışları Yanıtlar API geçişinin bir parçası değildir.
- `text-embedding-ada-002` referansları, önceden hesaplanmış bir gömülü dizin bunlara bağlı olduğu durumlarda muhafaza edilir.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->