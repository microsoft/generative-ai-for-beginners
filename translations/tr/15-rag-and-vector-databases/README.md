# Geri Getirmeyle Güçlendirilmiş Üretim (RAG) ve Vektör Veritabanları

[![Geri Getirmeyle Güçlendirilmiş Üretim (RAG) ve Vektör Veritabanları](../../../translated_images/tr/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Arama uygulamaları dersinde, kendi verilerinizi Büyük Dil Modellerine (LLM'ler) nasıl entegre edeceğinizi kısaca öğrendik. Bu derste, LLM uygulamanızda verilerinizi dayandırma kavramlarına, sürecin mekaniklerine ve hem gömme hem de metin dahil verilerin depolanma yöntemlerine daha derinlemesine bakacağız.

> **Video Yakında Gelecek**

## Giriş

Bu derste şu konuları ele alacağız:

- RAG'a giriş, nedir ve yapay zekada (artificial intelligence) neden kullanılır.

- Vektör veritabanlarının ne olduğunu anlama ve uygulamamız için bir tane oluşturma.

- RAG'ı bir uygulamaya nasıl entegre edeceğinize dair pratik bir örnek.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları yapabileceksiniz:

- RAG'ın veri getirme ve işleme alanındaki önemini açıklamak.

- RAG uygulamasını kurmak ve verilerinizi bir LLM'e dayandırmak.

- LLM uygulamalarında RAG ve Vektör Veritabanlarının etkili entegrasyonu.

## Senaryomuz: Kendi verilerimizle LLM'lerimizi geliştirmek

Bu ders için eğitim girişimimize kendi notlarımızı eklemek istiyoruz; bu, sohbet botunun farklı konular hakkında daha fazla bilgi edinmesini sağlar. Elimizdeki notları kullanarak, öğrenenler daha iyi çalışabilir ve farklı konuları anlayabilir, böylece sınavlara daha kolay tekrar yapabilir. Senaryomuzu oluşturmak için şu kaynakları kullanacağız:

- `Azure OpenAI:` sohbet botumuzu oluşturmak için kullanacağımız LLM

- `AI for beginners' dersindeki Sinir Ağları` : LLM'imizi dayandıracağımız veriler

- `Azure AI Search` ve `Azure Cosmos DB:` verilerimizi depolamak ve arama dizini oluşturmak için vektör veritabanı

Kullanıcılar notlarından pratik sınavlar oluşturabilecek, tekrar kartları hazırlayacak ve bunları özlü özetlere dönüştürebilecek. Başlamak için, RAG'ın ne olduğuna ve nasıl çalıştığına bakalım:

## Geri Getirmeyle Güçlendirilmiş Üretim (RAG)

LLM destekli bir sohbet botu, kullanıcı istemlerini yanıtlar üretmek için işler. Etkileşimli olacak şekilde tasarlanmıştır ve kullanıcılarla çok çeşitli konularda etkileşime girer. Ancak yanıtları, verilen bağlam ve eğitim verilerinin temeliyle sınırlıdır. Örneğin, GPT-4'ün bilgi kesiş tarihi Eylül 2021'dir, yani bu tarihten sonraki olaylardan habersizdir. Ayrıca, LLM'leri eğiten veriler kişisel notlar veya bir şirketin ürün kılavuzu gibi gizli bilgileri içermez.

### RAG'lar (Geri Getirmeyle Güçlendirilmiş Üretimler) nasıl çalışır

![RAG'ların nasıl çalıştığını gösteren çizim](../../../translated_images/tr/how-rag-works.f5d0ff63942bd3a6.webp)

Diyelim ki notlarınızdan sınavlar oluşturan bir sohbet botu dağıtmak istiyorsunuz, bunun için bilgi tabanına bağlantı gereklidir. İşte RAG devreye girer. RAG'lar şu şekilde çalışır:

- **Bilgi tabanı:** Getirmeden önce, bu belgeler alınır ve ön işleme tabi tutulur; genellikle büyük belgeler daha küçük parçalara bölünür, metin gömmelerine dönüştürülür ve bir veritabanında saklanır.

- **Kullanıcı Sorgusu:** kullanıcı bir soru sorar.

- **Getirme:** Bir kullanıcı soru sorduğunda, gömme modeli bilgi tabanımızdan ilgili bilgileri alır ve istemin içine eklemek üzere daha fazla bağlam sağlar.

- **Güçlendirilmiş Üretim:** LLM, getirilen verilere dayanarak yanıtını geliştirir. Bu, yanıtın yalnızca önceden eğitilmiş verilere değil, ayrıca eklenen bağlamdan gelen alakalı bilgilere de dayanmasını sağlar. Getirilen veriler LLM'nin yanıtlarını güçlendirmek için kullanılır. LLM sonra kullanıcının sorusuna cevap verir.

![RAG mimarisini gösteren çizim](../../../translated_images/tr/encoder-decode.f2658c25d0eadee2.webp)

RAG mimarisi, kodlayıcı ve kod çözücüden oluşan dönüştürücüler kullanılarak uygulanır. Örneğin, bir kullanıcı soru sorduğunda, giriş metni kelimelerin anlamını yakalayan vektörlere 'kodlanır' ve vektörler belge dizinimize 'kod çözülür' ve kullanıcı sorgusuna dayalı yeni text oluşturur. LLM, çıktıyı oluşturmak için kodlayıcı-kod çözücü modelini kullanır.

Önerilen makaleye göre [Bilgi Yoğun NLP Görevleri için Geri Getirmeyle Güçlendirilmiş Üretim (RAG) (natural language processing software)](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) RAG'ı uygularken iki yaklaşım vardır:

- **_RAG-Dizisi_** erişilen belgeleri kullanarak kullanıcı sorgusuna en uygun yanıtı tahmin etmek

- **RAG-Kelimesi** belgeleri kullanarak sonraki kelimeyi üretmek, sonra bunları kullanıcının sorgusunu yanıtlamak için getirmek

### Neden RAG kullanmalısınız? 

- **Bilgi zenginliği:** metin yanıtlarının güncel ve güncel olmasını sağlar. Böylece, dahili bilgi tabanına erişerek alan özel görevlerde performansı artırır.

- Kullanıcı sorgularına bağlam sağlamak için bilgi tabanında bulunan **doğrulanabilir verileri** kullanarak uydurmayı azaltır.

- Bir LLM'yi ince ayar yapmaya kıyasla daha ekonomik olması nedeniyle **maliyet etkin**dir.

## Bir bilgi tabanı oluşturmak

Uygulamamız kişisel verilerimize, yani AI For Beginners müfredatındaki Sinir Ağı dersine dayanmaktadır.

### Vektör Veritabanları

Vektör veritabanı, geleneksel veritabanlarının aksine, gömülü vektörleri depolamak, yönetmek ve aramak için tasarlanmış özel bir veritabanıdır. Belgelerin sayısal temsillerini depolar. Veriyi sayısal gömme olarak bölmek, yapay zeka sistemimizin veriyi anlamasını ve işlemesini kolaylaştırır.

Gömme verilerimizi vektör veritabanlarında saklıyoruz çünkü LLM'lerin girdi olarak kabul ettiği belirli bir token sayısı limiti vardır. Tüm gömmeleri bir kerede bir LLM'ye veremezsiniz, bu yüzden onları parçalara ayırmamız gerekir ve bir kullanıcı soru sorduğunda, soruya en yakın gömmeler istemle birlikte döndürülür. Parçalama, LLM'den geçen token sayısını da azaltarak maliyetleri düşürür.

Popüler vektör veritabanlarından bazıları Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant ve DeepLake'dir. Azure CLI ile aşağıdaki komutla bir Azure Cosmos DB modeli oluşturabilirsiniz:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Metinden gömmeye

Verimizi depolamadan önce, veriyi veritabanına kaydedilmeden önce vektör gömmelerine dönüştürmemiz gerekir. Büyük belgeler veya uzun metinlerle çalışıyorsanız, beklenen sorgulara göre bunları parçalara ayırabilirsiniz. Parçalama cümle veya paragraf seviyesinde yapılabilir. Parçalama, çevresindeki kelimelerin anlamını çıkardığı için bir parçaya farklı bağlamlar ekleyebilirsiniz; örneğin, belge başlığını ekleyerek veya parçadan önce veya sonra bazı metinleri dahil ederek. Veriyi şu şekilde parçalara ayırabilirsiniz:

```python
def split_text(text, max_length, min_length):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(' '.join(current_chunk)) < max_length and len(' '.join(current_chunk)) > min_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = []

    # Son parça minimum uzunluğa ulaşmadıysa bile yine de ekle
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Parçalara ayırdıktan sonra metnimizi farklı gömme modelleriyle gömebiliriz. Kullanabileceğiniz modeller arasında word2vec, OpenAI tarafından ada-002, Azure Bilgisayar Görüşü ve daha fazlası vardır. Kullanacağınız modeli seçmek, kullandığınız dillere, kodlanacak içeriğin (metin/görüntü/ses) türüne, kodlayabileceği girişin büyüklüğüne ve gömme çıkışının uzunluğuna bağlıdır.

OpenAI'nin `text-embedding-ada-002` modelini kullanarak gömme yapılmış metne bir örnek:
![cat kelimesinin gömme resmi](../../../translated_images/tr/cat.74cbd7946bc9ca38.webp)

## Getirme ve Vektör Arama

Bir kullanıcı soru sorduğunda, alıcı sorgu kodlayıcı ile bunu bir vektöre dönüştürür, sonra belge arama dizinimizde ilgili vektörleri arar. Bu işlem tamamlandıktan sonra hem giriş vektörü hem de belge vektörleri metne dönüştürülerek LLM'ye iletilir.

### Getirme

Getirme, sistemin arama kriterini karşılayan belgeleri dizinden hızlıca bulmaya çalıştığı andır. Alıcının amacı, LLM'yi verilerinizle dayandırmak ve bağlam sağlamak için kullanılacak belgeleri getirmektir.

Veritabanımızda arama yapmak için çeşitli yöntemler vardır, örneğin:

- **Anahtar kelime araması** - metin aramaları için kullanılır

- **Vektör araması** - belgeleri embedding modelleri kullanarak metinden vektör temsillerine dönüştürür, kelimelerin anlamını kullanarak **anlamsal arama** yapmayı sağlar. Getirme, kullanıcı sorgusuna en yakın vektörlere sahip belgeleri sorgulayarak yapılır.

- **Hibrit** - hem anahtar kelime hem vektör aramasının birleşimi.

Getirmede zorluk, veritabanında sorguya benzer yanıt olmadığında ortaya çıkar; sistem o zaman elde edebildiği en iyi bilgiyi verir. Ancak, alakayı ayarlamak için maksimum mesafe belirleme veya hem anahtar kelime hem vektör aramasını birleştiren hibrit arama kullanabilirsiniz. Bu derste hibrit aramayı kullanacağız. Verilerimizi hem parçaları hem gömmeleri içeren bir veri çerçevesinde depolayacağız.

### Vektör Benzerliği

Alıcı, bilgi tabanında birbirine yakın gömmeleri arar, en yakın komşular gibi, çünkü bunlar benzer metinlerdir. Kullanıcı bir sorgu sorduğunda, önce gömme yapılır ve sonra benzer gömmelerle eşleştirilir. Farklı vektörlerin ne kadar benzer olduğunu bulmak için yaygın ölçüt, iki vektör arasındaki açıya dayanan kosinüs benzerliğidir.

Benzerliği ölçmek için kullanılabilecek diğer alternatifler, vektör uç noktaları arasındaki doğru çizgi olan Öklidyen mesafe ve iki vektörün karşılık gelen elemanlarının çarpımlarının toplamını ölçen nokta çarpımıdır.

### Arama dizini

Getirme yaparken, arama yapmadan önce bilgi tabanımız için bir arama dizini oluşturmamız gerekir. Bir dizin gömmelerimizi depolar ve büyük veritabanlarında bile en benzer parçaları hızlıca getirebilir. Dizini yerel olarak şu şekilde oluşturabiliriz:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Arama dizinini oluştur
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# İndeksi sorgulamak için kneighbors yöntemini kullanabilirsiniz
distances, indices = nbrs.kneighbors(embeddings)
```

### Yeniden sıralama

Veritabanını sorguladıktan sonra sonuçları en alakalı olandan başlayarak sıralamanız gerekebilir. Yeniden sıralama LLM'si, makine öğrenmesini kullanarak arama sonuçlarının alakalılığını artırır ve sonuçları en alakalısından başlayarak sıralar. Azure AI Search kullanıldığında, yeniden sıralama otomatik olarak semantik yeniden sıralayıcı ile yapılır. Yeniden sıralamanın en yakın komşularla nasıl çalıştığına dair bir örnek:

```python
# En benzer belgeleri bulun
distances, indices = nbrs.kneighbors([query_vector])

index = []
# En benzer belgeleri yazdırın
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Hepsini bir araya getirmek

Son adım, verilerimize dayalı yanıtlar alabilmek için LLM'imizi karışıma eklemektir. Bunu şu şekilde uygulayabiliriz:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Sorguyu bir sorgu vektörüne dönüştür
    query_vector = create_embeddings(user_input)

    # En benzer belgeleri bul
    distances, indices = nbrs.kneighbors([query_vector])

    # Bağlam sağlamak için belgelere sorgu ekle
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # Geçmişi ve kullanıcı girdisini birleştir
    history.append(user_input)

    # Bir mesaj nesnesi oluştur
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # Yanıt oluşturmak için Responses API'sini kullan
    response = client.responses.create(
        model="gpt-4o-mini",
        temperature=0.7,
        max_output_tokens=800,
        input=messages,
        store=False,
    )

    return response.output_text

chatbot(user_input)
```

## Uygulamamızı değerlendirmek

### Değerlendirme Ölçütleri

- Doğal, akıcı ve insan benzeri ses çıkaran verilen yanıtların kalitesi

- Verinin dayandırılması: verilen yanıtın sağlanan belgelerden gelip gelmediğinin değerlendirilmesi

- Alaka: yanıtın sorulan soruyla eşleşip ilgili olup olmadığının değerlendirilmesi

- Akıcılık - yanıtın dilbilgisel olarak mantıklı olup olmadığı

## RAG (Geri Getirmeyle Güçlendirilmiş Üretim) ve vektör veritabanları kullanım alanları

Fonksiyon çağrılarının uygulamanızı geliştirebileceği birçok farklı kullanım alanı vardır, örneğin:

- Soru ve Cevaplama: şirket verilerinizi, çalışanların sorular sorabileceği bir sohbet ortamına dayandırmak.

- Tavsiye Sistemi: en benzer değerleri eşleştiren (örneğin filmler, restoranlar ve daha fazlası) bir sistem oluşturabilirsiniz.

- Sohbet botu hizmetleri: sohbet geçmişini saklayabilir ve kullanıcı verilerine göre konuşmayı kişiselleştirebilirsiniz.

- Vektör gömmelerine dayalı görsel arama, görüntü tanıma ve anomali tespiti için faydalıdır.

## Özet

RAG'ın temel alanlarını, verilerimizi uygulamaya nasıl ekleyeceğimizi, kullanıcı sorgusunu ve çıktıyı ele aldık. RAG oluşturmayı basitleştirmek için Semanti Kernel, Langchain veya Autogen gibi çerçeveleri kullanabilirsiniz.

## Ödev

Geri Getirmeyle Güçlendirilmiş Üretim'i (RAG) öğrenmeye devam etmek için şunları inşa edebilirsiniz:

- Tercih ettiğiniz çerçeve kullanarak uygulama için bir ön yüz oluşturun

- LangChain veya Semantic Kernel gibi bir çerçeveyi kullanarak uygulamanızı yeniden oluşturun.

Dersi tamamladığınız için tebrikler 👏.

## Öğrenme burada bitmiyor, yolculuğa devam edin

Bu dersi tamamladıktan sonra, Üretken Yapay Zeka bilgilerinizi geliştirmeye devam etmek için [Üretken AI Öğrenme koleksiyonumuza](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) göz atın!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->