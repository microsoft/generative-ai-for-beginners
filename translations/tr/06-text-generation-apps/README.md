# Metin Üretim Uygulamaları Geliştirme

[![Metin Üretim Uygulamaları Geliştirme](../../../translated_images/tr/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Bu dersin videosunu görüntülemek için yukarıdaki resme tıklayın)_

Bu eğitim müfredatı boyunca gördünüz ki istemler gibi temel kavramlar ve hatta "istem mühendisliği" adı verilen bir disiplin var. ChatGPT, Office 365, Microsoft Power Platform gibi etkileşim kurabileceğiniz birçok araç, bir şeyi başarmak için istemler kullanmanızı destekliyor.

Böyle bir deneyimi bir uygulamaya eklemek için istemler, tamamlamalar gibi kavramları anlamanız ve çalışmak için bir kütüphane seçmeniz gerekir. İşte bu bölümde tam olarak öğreneceğiniz şey budur.

## Giriş

Bu bölümde şunları yapacaksınız:

- openai kütüphanesini ve temel kavramlarını öğrenmek.
- openai kullanarak bir metin üretim uygulaması geliştirmek.
- İstem, sıcaklık ve tokenlar gibi kavramları kullanarak bir metin üretim uygulaması geliştirmeyi anlamak.

## Öğrenme hedefleri

Dersin sonunda şunları yapabileceksiniz:

- Metin üretim uygulamasının ne olduğunu açıklamak.
- openai kullanarak bir metin üretim uygulaması geliştirmek.
- Daha fazla veya daha az token kullanmak ve ayrıca çıktıyı çeşitlendirmek için sıcaklığı değiştirmek üzere uygulamanızı yapılandırmak.

## Metin üretim uygulaması nedir?

Normalde bir uygulama geliştirdiğinizde aşağıdaki gibi bir arayüzü olur:

- Komut tabanlı. Konsol uygulamaları tipik olarak bir komut yazdığınız ve bir görevi gerçekleştirdiği uygulamalardır. Örneğin, `git` komut tabanlı bir uygulamadır.
- Kullanıcı arayüzü (UI). Bazı uygulamalar, düğmelere tıklama, metin girme, seçenekleri seçme gibi işlemler yapabileceğiniz grafiksel kullanıcı arayüzlerine (GUI) sahiptir.

### Konsol ve UI uygulamaları sınırlıdır

Bir komut tabanlı uygulamayla karşılaştırın, bir komut yazarsınız:

- **Sınırlıdır**. Sadece uygulamanın desteklediği komutları yazabilirsiniz, herhangi bir komutu yazamazsınız.
- **Dile özgü**. Bazı uygulamalar birçok dili destekler, ama varsayılan olarak uygulama belirli bir dil için geliştirilir, dil desteği ekleyebilseniz bile.

### Metin üretim uygulamalarının faydaları

Peki metin üretim uygulaması nasıl farklıdır?

Metin üretim uygulamasında daha fazla esnekliğiniz vardır, belirli komut setleri veya belirli bir girdi dili ile sınırlı değilsiniz. Bunun yerine doğal dili kullanarak uygulama ile etkileşim kurabilirsiniz. Ayrıca başka bir fayda, geleneksel uygulamanın veritabanındaki bilgilerle sınırlı olabileceği yerde, zaten büyük bir bilgi külliyatı üzerinde eğitilmiş bir veri kaynağıyla etkileşimde olmanızdır.

### Metin üretim uygulamasıyla neler yapabilirim?

Birçok şey yapabilirsiniz. Örneğin:

- **Bir sohbet botu**. Şirketiniz ve ürünleri hakkında soruları yanıtlayan bir sohbet botu iyi bir eşleşme olabilir.
- **Yardımcı**. LLM'ler (Büyük Dil Modelleri) metin özetleme, metinden içgörü çıkarma, özgeçmiş gibi metinler üretme gibi görevlerde harikadır.
- **Kod asistanı**. Kullandığınız dil modeline bağlı olarak size kod yazmada yardımcı olan bir kod asistanı geliştirebilirsiniz. Örneğin, GitHub Copilot veya ChatGPT gibi ürünler kod yazmanıza yardımcı olabilir.

## Nasıl başlayabilirim?

Genelde bir LLM ile entegrasyon sağlamak için aşağıdaki iki yaklaşım olur:

- Bir API kullanmak. Burada isteğinizi prompt ile oluşturup oluşturulan metni geri alırsınız.
- Bir kütüphane kullanmak. Kütüphaneler API çağrılarını kapsüller ve kullanımı kolaylaştırır.

## Kütüphaneler/SDK'lar

LLM'lerle çalışmak için iyi bilinen birkaç kütüphane vardır:

- **openai**, bu kütüphane modelinize kolayca bağlanmayı ve istem göndermeyi sağlar.

Daha yüksek seviyede çalışan kütüphaneler ise:

- **Langchain**. Langchain iyi bilinir ve Python'u destekler.
- **Semantic Kernel**. Semantic Kernel Microsoft tarafından geliştirilmiş C#, Python ve Java dillerini destekleyen bir kütüphanedir.

## openai kullanarak ilk uygulama

İlk uygulamamızı nasıl oluşturacağımıza, hangi kütüphanelerin gerektiğine, ne kadarının gerekli olduğuna bakalım.

### openai kurulum

OpenAI veya Azure OpenAI ile etkileşim için birçok kütüphane vardır. C#, Python, JavaScript, Java gibi birçok programlama dilini kullanmak mümkündür. Biz `openai` Python kütüphanesini seçtik, bu yüzden `pip` ile kuracağız.

```bash
pip install openai
```

### Bir kaynak oluşturun

Şu adımları yapmalısınız:

- Azure'da bir hesap oluşturun [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Azure OpenAI erişimi alın. [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) adresinden erişim talep edin.

  > [!NOTE]
  > Yazım esnasında, Azure OpenAI için erişim başvurusu yapmanız gerekmektedir.

- Python yükleyin <https://www.python.org/>
- Azure OpenAI Hizmet kaynağı oluşturun. Kaynak oluşturma hakkında rehbere bakabilirsiniz [https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### API anahtarı ve uç noktayı bulun

Artık `openai` kütüphanesine hangi API anahtarını kullanacağını belirtmeniz gerekir. Azure OpenAI kaynağınızın "Keys and Endpoint" bölümüne gidip "Key 1" değerini kopyalayın.

![Azure Portal'da Keys and Endpoint kaynak ekranı](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Artık bu bilgiyi kopyaladığınıza göre, kütüphanelere bunu kullanmasını söyleyelim.

> [!NOTE]
> API anahtarınızı koddan ayırmak faydalıdır. Bunu ortam değişkenleri kullanarak yapabilirsiniz.
>
> - Ortam değişkeni `OPENAI_API_KEY` değerini API anahtarınız olarak ayarlayın.
>   `export OPENAI_API_KEY='sk-...'`

### Azure yapılandırması ayarlama

Azure OpenAI kullanıyorsanız (şimdi Microsoft Foundry'nin parçası), yapılandırmayı şu şekilde ayarlayın. Azure OpenAI `/openai/v1/` uç noktasına işaret eden standart `OpenAI` istemcisini kullanıyoruz, bu Responses API ile çalışır ve `api_version` gerekmez:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Yukarıda şunları yapıyoruz:

- `api_key`, bu Azure Portal veya Microsoft Foundry portalında bulunan API anahtarınızdır.
- `base_url`, bu Foundry kaynak uç noktanızdır ve sonuna `/openai/v1/` eklenmiştir. Stabil v1 uç noktası OpenAI ve Azure OpenAI arasında `api_version` yönetimi olmadan çalışır.

> [!NOTE] > `os.environ` ortam değişkenlerini okur. Bunu `AZURE_OPENAI_API_KEY` ve `AZURE_OPENAI_ENDPOINT` gibi ortam değişkenlerini okumak için kullanabilirsiniz. Bu ortam değişkenlerini terminalinizde veya `dotenv` gibi bir kütüphane kullanarak ayarlayın.

## Metin üretme

Metin üretmenin yolu, `responses.create` yöntemi aracılığıyla Responses API kullanmaktır. İşte bir örnek:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # bu sizin model dağıtım adınızdır
    input=prompt,
    store=False,
)
print(response.output_text)
```

Yukarıdaki kodda, bir cevap oluşturuyoruz ve kullanmak istediğimiz modeli ve istemi (prompt) geçiriyoruz. Sonra `response.output_text` ile üretilen metni yazdırıyoruz.

### Çok turlu sohbetler

Responses API, hem tek turlu metin üretimine hem de çok turlu chatbotlara uygundur - `input` içinde bir mesajlar listesi vererek bir sohbet oluşturabilirsiniz:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

Bu işlev hakkında daha fazlası yaklaşan bir bölümde.

## Alıştırma - ilk metin üretim uygulamanız

openai'nin nasıl kurulup yapılandırılacağını öğrendik, şimdi ilk metin üretim uygulamanızı oluşturma zamanı. Uygulamanızı oluşturmak için şu adımları izleyin:

1. Bir sanal ortam oluşturun ve openai yükleyin:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Windows kullanıyorsanız `source venv/bin/activate` yerine `venv\Scripts\activate` yazın.

   > [!NOTE]
   > Azure OpenAI anahtarınızı bulmak için [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) sitesine gidin, `Open AI` araması yapın, `Open AI resource` seçin, ardından `Keys and Endpoint` ve `Key 1` değerini kopyalayın.

1. _app.py_ dosyasını oluşturun ve içine aşağıdaki kodu yazın:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # tamamlayıcı kodunuzu ekleyin
   prompt = "Complete the following: Once upon a time there was a"

   # Responses API'sini kullanarak bir istek yapın
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # yanıtı yazdırın
   print(response.output_text)
   ```

   > [!NOTE]
   > Salt OpenAI (Azure değil) kullanıyorsanız `client = OpenAI(api_key="<OpenAI anahtarınız ile değiştirin>")` (base_url olmadan) kullanın ve model adı olarak dağıtım adı yerine `gpt-4o-mini` gibi bir model verin.

   Aşağıdaki gibi bir çıktı görmelisiniz:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Farklı türde istemler, farklı işler için

Artık bir istem kullanarak nasıl metin oluşturulacağını gördünüz. Hatta modifiye edip farklı türde metinler üretebileceğiniz çalışan bir programınız var.

İstemler çeşitli görevler için kullanılabilir. Örneğin:

- **Bir tür metin üretme**. Örneğin, şiir, sınav soruları vb. üretebilirsiniz.
- **Bilgi arama**. 'Web geliştirmede CORS ne demek?' gibi bilgiler için istemler kullanabilirsiniz.
- **Kod üretme**. İstemlerle örneğin e-postaları doğrulamak için kullanılan düzenli ifade veya bütünüyle bir program (web uygulaması gibi) üretebilirsiniz.

## Daha pratik bir kullanım: tarif üretici

Evde malzemeleriniz olduğunu ve yemek yapmak istediğinizi hayal edin. Bunun için bir tarife ihtiyacınız var. Tarif bulmak için bir arama motoru kullanabilir veya bir LLM kullanabilirsiniz.

Aşağıdaki gibi bir istem yazabilirsiniz:

> "Aşağıdaki malzemelere sahip bir yemek için 5 tarif göster: tavuk, patates ve havuç. Her tarif için kullanılan tüm malzemeleri listele"

Yukarıdaki istemle benzer bir yanıt alabilirsiniz:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 2 cloves garlic, minced
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
```

Bu sonuç çok güzel, ne pişireceğimi biliyorum. Şimdi faydalı olabilecek geliştirmeler şunlar olabilir:

- Sevmediğim veya alerjim olan malzemelerin filtrelenmesi.
- Evde olmayan malzemeler için alışveriş listesi oluşturulması.

Yukarıdaki durumlar için ek bir istem ekleyelim:

> "Lütfen sarımsak içeren tarifleri çıkar çünkü alerjim var ve yerine başka şey koy. Ayrıca, evde halihazırda tavuk, patates ve havuç olduğunu hesaba katarak tarifler için alışveriş listesi oluştur."

İşte yeni sonuç:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano

Shopping List:
- Olive oil
- Onion
- Thyme
- Oregano
- Salt
- Pepper
```

İşte sarımsak içermeyen beş tarif ve evdeki malzemelere göre bir alışveriş listeniz var.

## Alıştırma - tarif üretici yapma

Bir senaryoyu oynadık, şimdi bu senaryoya uygun kod yazalım. Bunu yapmak için şu adımları izleyin:

1. Mevcut _app.py_ dosyasını başlangıç noktası olarak kullanın
1. `prompt` değişkenini bulun ve kodunu aşağıdaki gibi değiştirin:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Şu an kodu çalıştırırsanız aşağıdakine benzer bir çıktı görmelisiniz:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOT: LLM'niz deterministik değildir, bu yüzden programı her çalıştırdığınızda farklı sonuçlar alabilirsiniz.

   Harika, şimdi nasıl geliştirebileceğimize bakalım. Geliştirmek için kodun esnek olmasını isteriz, böylece hem tarif sayısı hem de malzemeler geliştirilebilir ve değiştirilebilir.

1. Kodu şu şekilde değiştirelim:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # tarif sayısını, bir malzemeler istemine yerleştiriniz
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Test çalışması için kod şöyle görünebilir:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Filtre ve alışveriş listesi ekleyerek geliştirme

Şimdi kullanıcıdan tarif sayısı ve kullanılan malzemeleri alarak tarifler oluşturabilen çalışan ve esnek bir uygulamamız var.

Daha da geliştirmek için şunları eklemek istiyoruz:

- **Malzeme filtreleme**. Sevmediğiniz veya alerjiniz olan malzemeleri filtreleyebilmek istiyoruz. Bunu yapmak için mevcut istemimizi düzenleyip sonuna şöyle bir filtre şartı ekleyebiliriz:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Yukarıda, istemin sonuna `{filter}` ekliyoruz ve ayrıca kullanıcıdan filtre değerini alıyoruz.

  Program çalıştırılırken örnek bir girdi şöyle olabilir:

  ```output
  No of recipes (for example, 5): 3
  List of ingredients (for example, chicken, potatoes, and carrots): onion,milk
  Filter (for example, vegetarian, vegan, or gluten-free): no milk

  1. French Onion Soup

  Ingredients:

  -1 large onion, sliced
  -3 cups beef broth
  -1 cup milk
  -6 slices french bread
  -1/4 cup shredded Parmesan cheese
  -1 tablespoon butter
  -1 teaspoon dried thyme
  -1/4 teaspoon salt
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add beef broth, milk, thyme, salt, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Place french bread slices on soup bowls.
  5. Ladle soup over bread.
  6. Sprinkle with Parmesan cheese.

  2. Onion and Potato Soup

  Ingredients:

  -1 large onion, chopped
  -2 cups potatoes, diced
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add potatoes, vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Serve hot.

  3. Creamy Onion Soup

  Ingredients:

  -1 large onion, chopped
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper
  -1/4 cup all-purpose flour
  -1/2 cup shredded Parmesan cheese

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. In a small bowl, whisk together flour and Parmesan cheese until smooth.
  5. Add to soup and simmer for an additional 5 minutes, or until soup has thickened.
  ```

  Gördüğünüz gibi, içeriğinde süt olan tarifler filtrelenmiş. Ama laktoz intoleransınız varsa peynir içeren tarifleri de filtrelemek isteyebilirsiniz, bu nedenle net olmak gerekir.


- **Bir alışveriş listesi oluşturun**. Evde zaten sahip olduklarımızı göz önünde bulundurarak bir alışveriş listesi oluşturmak istiyoruz.

  Bu işlevsellik için her şeyi tek bir istemde çözmeye çalışabiliriz veya bunu iki isteme bölebiliriz. İkinci yaklaşımı deneyelim. Burada ek bir istem eklemeyi öneriyoruz, ancak bunun çalışması için, önceki istemin sonucunu sonraki isteme bağlam olarak eklememiz gerekiyor.

  İlk istemin sonucunu yazdıran kod bölümünü bulun ve aşağıdaki kodu altına ekleyin:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # yanıtı yazdır
  print("Shopping list:")
  print(response.output_text)
  ```

  Şu noktalara dikkat edin:

  1. İlk istemin sonucunu yeni isteme ekleyerek yeni bir istem oluşturuyoruz:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Yeni bir istek yapıyoruz ama ilk istemde istediğimiz token sayısını da dikkate alıyoruz, bu yüzden bu sefer `max_output_tokens` değerini 1200 olarak belirtiyoruz.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Bu kodu çalıştırdığımızda aşağıdaki çıktıya ulaşıyoruz:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Kurulumunuzu geliştirin

Şimdiye kadar elimizde çalışan bir kod var, ancak işleri daha da geliştirmek için yapmamız gereken bazı ayarlamalar var. Yapmamız gereken bazı şeyler şunlardır:

- **API anahtarı gibi gizli bilgileri koddan ayırın**. Gizli bilgiler kodda olmamalı ve güvenli bir yerde saklanmalıdır. Gizli bilgileri koddan ayırmak için ortam değişkenleri kullanabilir ve `python-dotenv` gibi kütüphanelerle bu bilgileri bir dosyadan yükleyebilirsiniz. Kodda bu şöyle görünebilir:

  1. Aşağıdaki içeriğe sahip bir `.env` dosyası oluşturun:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Not, Microsoft Foundry'deki Azure OpenAI için bunun yerine şu ortam değişkenlerini ayarlamanız gerekir:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Kodda ortam değişkenlerini şöyle yüklersiniz:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Token uzunluğuna dair bir not**. Metni oluşturmak için kaç token gerektiğini düşünmeliyiz. Tokenler maliyetlidir, bu yüzden mümkün olduğunda kullandığımız token sayısında tasarruf etmeye çalışmalıyız. Örneğin, prompt'u daha az token kullanacak şekilde ifade edebilir miyiz?

  Kullanılan token sayısını değiştirmek için `max_output_tokens` parametresini kullanabilirsiniz. Örneğin, 100 token kullanmak istiyorsanız şöyle yaparsınız:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Sıcaklık ile denemeler yapmak**. Sıcaklıktan daha önce bahsetmedik ancak programımızın nasıl çalıştığı açısından önemli bir bağlamdır. Sıcaklık değeri arttıkça çıktı daha rastgele olur. Düşük sıcaklık değeri ise çıktıyı daha öngörülebilir yapar. Çıktınızda varyasyon isteyip istemediğinizi düşünün.

  Sıcaklığı değiştirmek için `temperature` parametresini kullanabilirsiniz. Örneğin, 0.5 sıcaklığı kullanmak isterseniz şöyle yaparsınız:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Not, 1.0'a ne kadar yakınsa çıktı o kadar çeşitli olur.

## Ödev

Bu ödev için ne yapacağınıza siz karar verebilirsiniz.

İşte bazı öneriler:

- Tarif oluşturucu uygulamasını daha da geliştirin. Sıcaklık değerleri ve istemlerle oynayarak neler yapabileceğinizi görün.
- Bir "çalışma arkadaşı" yapın. Bu uygulama, örneğin Python hakkında soruları yanıtlayabilmeli. "Python'da belirli bir konu nedir?" gibi istemler olabilir ya da "Bana belirli bir konu için kod göster" gibi istemler olabilir.
- Tarih botu yapın, tarihi canlandırın, bota belirli bir tarihi karakteri oynatın ve hayatı ve zamanı hakkında sorular sorun.

## Çözüm

### Çalışma arkadaşı

Aşağıda başlangıç için bir istem var, nasıl kullanabileceğinizi ve zevkinize göre nasıl değiştirebileceğinizi görün.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Tarih botu

Kullanabileceğiniz bazı istemler şunlardır:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Bilgi testi

Sıcaklık kavramı ne işe yarar?

1. Çıktının ne kadar rastgele olduğunu kontrol eder.
1. Cevabın ne kadar büyük olduğunu kontrol eder.
1. Kaç token kullanıldığını kontrol eder.

## 🚀 Meydan Okuma

Ödev üzerinde çalışırken sıcaklığı değiştirin, 0, 0.5 ve 1 olarak ayarlamayı deneyin. 0 en az varyasyonlu, 1 ise en çok varyasyonlu. Uygulamanız için hangi değer en iyi sonuç veriyor?

## Harika İş! Öğrenmeye Devam Et

Bu dersi tamamladıktan sonra, Generatif Yapay Zeka bilginizi artırmaya devam etmek için [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) koleksiyonumuza göz atın!

7. Derse gidin; burada [chat uygulamalarının nasıl inşa edileceğine](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) bakacağız!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->