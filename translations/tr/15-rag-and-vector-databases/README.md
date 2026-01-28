<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2210a0466c812d9defc4df2d9a709ff9",
  "translation_date": "2026-01-18T18:16:20+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "tr"
}
-->
# Retrieval Augmented Generation (RAG) ve Vektör Veritabanları

[![Retrieval Augmented Generation (RAG) ve Vektör Veritabanları](../../../../../translated_images/tr/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

Arama uygulamaları dersinde, kendi verilerinizi Büyük Dil Modellerine (LLM'ler) nasıl entegre edeceğinizi kısaca öğrendik. Bu derste, LLM uygulamanızda verilerinizi temel alma kavramına, sürecin mekaniklerine ve hem gömme hem de metin verilerinin depolanma yöntemlerine daha derinlemesine bakacağız.

> **Video Yakında Gelecek**

## Giriş

Bu derste şunları ele alacağız:

- RAG'ın tanıtımı, ne olduğu ve yapay zekada (AI) neden kullanıldığı.

- Vektör veritabanlarının ne olduğunu anlamak ve uygulamamız için bir tane oluşturmak.

- RAG'ı bir uygulamaya entegre etme üzerine pratik bir örnek.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra:

- RAG'ın veri erişimi ve işleme açısından önemini açıklayabileceksiniz.

- RAG uygulamasını kurup verilerinizi bir LLM'ye dayandırabileceksiniz.

- RAG ve Vektör Veritabanlarının LLM uygulamalarında etkili entegrasyonunu gerçekleştirebileceksiniz.

## Senaryomuz: Kendi verilerimizle LLM'lerimizi geliştirmek

Bu ders için, eğitim girişimimize kendi notlarımızı eklemek istiyoruz; böylece sohbet botu farklı konular hakkında daha fazla bilgi alabilir. Elimizdeki notları kullanarak, öğrenciler daha iyi çalışıp farklı konuları anlayabilecek ve sınavlarına hazırlanmak daha kolay olacak. Senaryomuzu oluşturmak için şunları kullanacağız:

- `Azure OpenAI:` sohbet botumuzu oluşturmak için kullanacağımız LLM

- `AI for beginners' lesson on Neural Networks`: LLM'imizi dayandıracağımız veri

- `Azure AI Search` ve `Azure Cosmos DB:` verilerimizi depolamak ve bir arama dizini oluşturmak için vektör veritabanı

Kullanıcılar notlarından pratik quizler oluşturabilecek, tekrar kartları hazırlayabilecek ve bunları özetleyerek kısa genel bakışlar elde edebilecekler. Başlamak için RAG'ın ne olduğunu ve nasıl çalıştığını inceleyelim:

## Retrieval Augmented Generation (RAG)

LLM destekli bir sohbet botu, kullanıcı istemlerini işleyerek yanıtlar oluşturur. Etkileşimli olacak şekilde tasarlanmıştır ve kullanıcılarla çok çeşitli konularda etkileşime girer. Ancak yanıtları, sağlanan bağlam ve temel eğitim verileri ile sınırlıdır. Örneğin, GPT-4'ün bilgi kesim tarihi Eylül 2021'dir; bu, bu tarihten sonra gerçekleşen olayları bilmediği anlamına gelir. Ayrıca, LLM'leri eğitmek için kullanılan veri, kişisel notlar veya bir şirketin ürün kılavuzu gibi gizli bilgileri içermez.

### RAG'lar (Retrieval Augmented Generation) nasıl çalışır?

![RAG'ların nasıl çalıştığını gösteren çizim](../../../../../translated_images/tr/how-rag-works.f5d0ff63942bd3a6.webp)

Diyelim ki notlarınızdan quizler oluşturan bir sohbet botu dağıtmak istiyorsunuz; bilgi tabanına bağlantıya ihtiyacınız olacak. İşte burada RAG devreye girer. RAG'lar şu şekilde çalışır:

- **Bilgi tabanı:** Erişimden önce, bu belgelerin alınması ve ön işlenmesi gerekir; genellikle büyük belgeler küçük parçalara bölünür, metin gömmeye dönüştürülür ve bir veritabanına kaydedilir.

- **Kullanıcı Sorgusu:** kullanıcı soru sorar

- **Erişim:** Kullanıcı soru sorduğunda, gömme modeli bilgi tabanımızdan ilgili bilgileri alır ve isteğe bağlanacak daha fazla bağlam sağlamak için kullanır.

- **Geliştirilmiş Üretim:** LLM, alınan verilere dayanarak yanıtını geliştirir. Bu, oluşturulan yanıtın sadece önceden eğitilmiş verilere değil, eklenen bağlamdan alınan ilgili bilgilere dayanmasını sağlar. Erişilen veriler, LLM yanıtlarını geliştirmek için kullanılır. Sonra LLM, kullanıcının sorusuna cevap verir.

![RAG'ların mimarisini gösteren çizim](../../../../../translated_images/tr/encoder-decode.f2658c25d0eadee2.webp)

RAG mimarisi iki bölümden oluşan transformer kullanılarak uygulanır: bir kodlayıcı (encoder) ve bir çözücü (decoder). Örneğin, kullanıcı bir soru sorduğunda, giriş metni kelimelerin anlamını yakalayan vektörlere 'kodlanır' ve bu vektörler belgesi dizinine 'çözümlenir' ve kullanıcı sorgusuna göre yeni metin oluşturulur. LLM, çıktıyı üretmek için hem kodlayıcı-çözücü modelini kullanır.

Önerilen makaleye göre RAG uygulamalarında iki yaklaşım vardır: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst):

- **_RAG-Sequence_**: Kullanıcının sorgusuna en iyi olası cevabı tahmin etmek için erişilen belgeleri kullanma

- **RAG-Token**: Belgeyi sonraki token'ı üretmek için kullanır, ardından kullanıcı sorgusunu yanıtlamak için geri getirir

### Neden RAG kullanırsınız?

- **Bilgi zenginliği:** Metin yanıtlarının güncel ve güncel kalmasını sağlar. Böylece, dahili bilgi tabanına erişerek alan özel görevlerde performansı artırır.

- Doğrulanabilir veriyi kullanarak **uydurma**yı azaltır ve kullanıcı sorgularına bağlam sağlar.

- Bir LLM'yi ince ayar yapmaya göre daha **maliyet etkili**dir.

## Bir bilgi tabanı oluşturmak

Uygulamamız kişisel verilere dayanır; yani AI For Beginners müfredatındaki Sinir Ağları dersi.

### Vektör Veritabanları

Vektör veritabanı, geleneksel veritabanlarından farklı olarak gömülü vektörleri saklamak, yönetmek ve aramak için tasarlanmış özel bir veritabanıdır. Belgelerin sayısal temsillerini depolar. Verileri sayısal gömme vektörlerine dönüştürmek, yapay zeka sistemimizin verileri anlamasını ve işlemesini kolaylaştırır.

Gömme verilerimizi vektör veritabanlarında depolarız çünkü LLM'lerin giriş olarak kabul ettiği token sayısında bir sınır vardır. Tüm gömmeleri bir LLM'ye gönderemezsiniz, bu yüzden bunları parçalara ayırmanız gerekir ve kullanıcı bir soru sorduğunda, soruyla en çok eşleşen gömmeler isteğe birlikte geri döner. Parçalama, LLM'ye gönderilen token sayısının maliyetini de azaltır.

Popüler bazı vektör veritabanları Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant ve DeepLake'dir. Azure CLI kullanarak Azure Cosmos DB modeli oluşturmak için şu komutu kullanabilirsiniz:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### Metinden gömme vektörlerine

Verilerimizi depolamadan önce, önce onları vektör gömme biçimine dönüştürmemiz gerekir. Büyük belgeler veya uzun metinlerle çalışıyorsanız, beklediğiniz sorgulara göre parçalayabilirsiniz. Parçalama cümle veya paragraf seviyesinde yapılabilir. Parçalama, çevresindeki kelimelerden anlam çıkardığı için, bölüme başka bağlamlar ekleyebilirsiniz; örneğin, belge başlığını ekleyerek veya bölüme önce veya sonra bir metin ekleyerek. Verileri şöyle parçalayabilirsiniz:

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

Bölümlendikten sonra, metnimizi çeşitli gömme modelleri ile gömebiliriz. Kullanabileceğiniz modeller arasında word2vec, OpenAI tarafından ada-002, Azure Computer Vision ve daha fazlası vardır. Kullanılacak model, kullandığınız diller, kodlanan içerik türü (metin/görsel/ses), kodlanabilecek giriş boyutu ve gömme çıktısının uzunluğuna bağlıdır.

OpenAI'nin `text-embedding-ada-002` modeli ile oluşturulmuş gömülü metne bir örnek:
![cat kelimesinin gömmesi](../../../../../translated_images/tr/cat.74cbd7946bc9ca38.webp)

## Erişim ve Vektör Arama

Kullanıcı bir soru sorduğunda, erişici (retriever) sorguyu sorgu kodlayıcısı kullanarak vektöre dönüştürür, ardından belge arama dizinimizde girdiyle ilgili belgelerden ilgili vektörleri arar. İşlem tamamlandığında, hem giriş vektörünü hem de belge vektörlerini metne dönüştürür ve bunları LLM'ye geçirir.

### Erişim

Erişim, sistemin dizindeki arama kriterlerini karşılayan belgeleri hızlıca bulmaya çalıştığı andır. Erişimcinin (retriever's) amacı, bağlam sağlamak ve LLM'yi verilerinize dayandırmak üzere kullanılacak belgeleri almaktır.

Veritabanımızda arama yapmak için birkaç yöntem vardır:

- **Anahtar kelime araması** - metin aramaları için kullanılır

- **Vektör araması** - belgeleri metinden gömme modelleri aracılığıyla vektör temsillerine dönüştürerek, kelimelerin anlamını kullanarak **anlamsal arama** yapılmasına izin verir. Erişim, kullanıcının sorusuna en yakın vektör temsiline sahip belgeleri sorgulayarak gerçekleştirilir.

- **Hibrit** - hem anahtar kelime hem de vektör aramasının birleşimidir.

Erişim sorunları, veritabanında sorguya benzer yanıt olmadığında ortaya çıkar; sistem o zaman elde edebildiği en iyi bilgiyi döndürecektir. Ancak, uygunluğu maksimum mesafe ile sınırlandırmak veya hem anahtar kelime hem vektör aramasını birleştiren karma arama kullanmak gibi taktikler uygulanabilir. Bu derste, hem vektör hem anahtar kelime aramasının birleşimi olan hibrit aramayı kullanacağız. Verilerimizi, parçaları ve gömmeleri içeren sütunları olan bir veri çerçevesinde depolayacağız.

### Vektör Benzerliği

Erişimci, bilgi veritabanında yakın olan gömmeleri arar; en yakın komşu, çünkü metinler benzerdir. Bir kullanıcı sorgu sorduğunda, öncelikle gömülür ve ardından benzer gömmelerle eşleştirilir. Farklı vektörlerin ne kadar benzer olduğunu ölçmek için yaygın kullanılan ölçüm, iki vektör arasındaki açıya göre hesaplanan kosinüs benzerliğidir.

Benzerliği ölçmek için kullanılabilecek diğer alternatifler, vektör uç noktaları arasındaki doğru çizgi olan Öklid uzaklığı ve iki vektörün karşılık gelen elemanlarının çarpımlarının toplamını ölçen nokta çarpımıdır.

### Arama dizini

Erişim yaparken, arama gerçekleştirmeden önce bilgi tabanımız için bir arama dizini oluşturmalıyız. Dizinimiz gömmelerimizi depolar ve büyük bir veritabanında bile en benzer parçaları hızlıca geri getirebilir. Dizini yerel olarak şöyle oluşturabiliriz:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Arama indeksini oluşturun
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# İndeksi sorgulamak için kneighbors metodunu kullanabilirsiniz
distances, indices = nbrs.kneighbors(embeddings)
```

### Yeniden sıralama

Veritabanını sorguladıktan sonra, sonuçları en uygun olandan başlayarak sıralamanız gerekebilir. Yeniden sıralama LLM'si, makine öğrenimi kullanarak arama sonuçlarının uygunluğunu artırır ve onları en alakalıdan itibaren sıralar. Azure AI Search kullanılırken, yeniden sıralama semantik bir yeniden sıralayıcı ile otomatik olarak yapılır. En yakın komşuları kullanarak yeniden sıralamanın nasıl çalıştığına bir örnek:

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

Son adım, verilerimize dayalı yanıtlar alabilmek için LLM'imizi karışıma eklemektir. Bunu şöyle uygulayabiliriz:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Soruyu bir sorgu vektörüne dönüştür
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

    # Yanıt oluşturmak için sohbet tamamlamasını kullan
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```

## Uygulamamızı değerlendirmek

### Değerlendirme Ölçütleri

- Sağlanan yanıtların kalitesi: doğal, akıcı ve insan benzeri olması

- Verilerin dayandırılmışlığı: yanıtın sağlanan belgelerden gelip gelmediğinin değerlendirilmesi

- Uygunluk: yanıtın soruyla eşleşip ilişkili olması

- Akıcılık: yanıtın dilbilgisel olarak mantıklı olup olmadığı

## RAG (Retrieval Augmented Generation) ve vektör veritabanları kullanım durumları

Fonksiyon çağrıları uygulamanızı iyileştirebileceği birçok farklı kullanım durumu vardır, örneğin:

- Soru ve Cevaplama: şirket verilerinizi çalışanların soru sormak için kullanabileceği bir sohbete dayandırmak.

- Öneri Sistemleri: en benzer değerleri eşleştiren sistemler oluşturmak, örneğin film, restoran ve daha fazlası.

- Sohbet botu hizmetleri: sohbet geçmişini depolayabilir ve kullanıcı verilerine göre kişiselleştirilmiş konuşma sağlayabilirsiniz.

- Vektör gömmelerine dayalı görsel arama, görsel tanıma ve anomali tespitinde faydalıdır.

## Özet

RAG'ın temel alanlarını, verilerimizin uygulamaya eklenmesinden kullanıcı sorgularına ve çıktıya kadar ele aldık. RAG oluşturmayı kolaylaştırmak için Semanti Kernel, Langchain veya Autogen gibi çerçeveleri kullanabilirsiniz.

## Ödev

Retrieval Augmented Generation (RAG) öğreniminize devam etmek için şunları yapabilirsiniz:

- Tercih ettiğiniz çerçeveyi kullanarak uygulama için bir ön yüz oluşturun

- LangChain veya Semantic Kernel gibi bir çerçeveyi kullanarak uygulamanızı yeniden oluşturun.

Dersi tamamladığınız için tebrikler 👏.

## Öğrenme burada bitmiyor, yolculuğa devam edin

Bu dersi tamamladıktan sonra, [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) koleksiyonumuzu inceleyerek Üretken Yapay Zeka bilginizi geliştirmeye devam edin!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba gösterilse de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->