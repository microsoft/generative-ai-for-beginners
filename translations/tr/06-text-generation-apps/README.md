# Metin Üretimi Uygulamaları Oluşturma

[![Metin Üretimi Uygulamaları Oluşturma](../../../translated_images/tr/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Bu dersin videosunu görüntülemek için yukarıdaki resme tıklayın)_

Bu eğitim müfredatı boyunca gördüğünüz gibi, istemler gibi temel kavramlar ve hatta "istem mühendisliği" adı verilen bir disiplin vardır. ChatGPT, Office 365, Microsoft Power Platform ve diğer pek çok araç gibi birçok araç, bir şeyleri başarmak için istemleri kullanmanızı destekler.

Böyle bir deneyimi bir uygulamaya eklemek için istemler, tamamlamalar gibi kavramları anlamalı ve çalışmak için bir kitaplık seçmelisiniz. İşte tam da bu bölümde öğreneceksiniz.

## Giriş

Bu bölümde:

- openai kitaplığı ve temel kavramlarını öğreneceksiniz.
- openai kullanarak bir metin üretimi uygulaması oluşturacaksınız.
- Bir metin üretimi uygulaması oluşturmak için istem, sıcaklık ve tokenlar gibi kavramların nasıl kullanıldığını anlayacaksınız.

## Öğrenme hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- Metin üretimi uygulamasının ne olduğunu açıklayabileceksiniz.
- openai kullanarak bir metin üretimi uygulaması oluşturabileceksiniz.
- Uygulamanızı daha fazla veya daha az token kullanacak şekilde ve ayrıca farklı çıktıların elde edilmesi için sıcaklığı ayarlayacak şekilde yapılandırabileceksiniz.

## Metin üretimi uygulaması nedir?

Normalde bir uygulama oluşturduğunuzda aşağıdaki türde bir arayüze sahiptir:

- Komut tabanlı. Konsol uygulamaları, bir komut yazıp görevini yerine getiren tipik uygulamalardır. Örneğin, `git` komut tabanlı bir uygulamadır.
- Kullanıcı arayüzü (UI). Bazı uygulamalar, butonlara tıklayıp, metin girip, seçenekler seçtiğiniz grafiksel kullanıcı arayüzlerine (GUI) sahiptir.

### Konsol ve UI uygulamaları sınırlıdır

Yazdığınız bir komut ile komut tabanlı bir uygulama ile karşılaştırın:

- **Sınırlıdırlar**. Sadece uygulamanın desteklediği komutları yazabilirsiniz, her komutu yazamazsınız.
- **Dil spesifikidir**. Bazı uygulamalar birçok dili desteklese de, varsayılan olarak belirli bir dil için tasarlanmıştır; daha fazla dil desteği ekleyebilirsiniz ama temel dil zaten belirlenmiştir.

### Metin üretimi uygulamalarının faydaları

Peki metin üretimi uygulaması nasıl farklıdır?

Metin üretimi uygulamasında daha fazla esneklik vardır, belirli komutlar veya belirli bir giriş diliyle sınırlı değilsiniz. Bunun yerine, uygulama ile doğal dili kullanarak etkileşim kurabilirsiniz. Bir diğer fayda ise, geleneksel bir uygulamanın sınırlı olduğu veri tabanındaki bilgilerin aksine, zaten büyük bir bilgi kümesi üzerinde eğitilmiş veri kaynağı ile etkileşim halindesinizdir.

### Metin üretimi uygulaması ile ne oluşturabilirim?

Birçok şey oluşturabilirsiniz. Örneğin:

- **Bir sohbet botu**. Şirketiniz ve ürünleri hakkında soruları yanıtlayan bir sohbet botu iyi bir eşleşme olabilir.
- **Yardımcı**. Büyük dil modelleri (LLM'ler) metni özetlemek, metinden çıkarımlar yapmak, özgeçmiş gibi metinler üretmek gibi görevlerde mükemmeldir.
- **Kod asistanı**. Kullandığınız dil modeline bağlı olarak, kod yazmanıza yardımcı olan bir kod asistanı oluşturabilirsiniz. Örneğin, GitHub Copilot ve ChatGPT gibi ürünleri kod yazarken yardımcı olmak için kullanabilirsiniz.

## Nasıl başlayabilirim?

Genellikle iki yaklaşım vardır, bir büyük dil modeli (LLM) ile entegre olmanın yolları:

- Bir API kullanmak. Burada isteminizle web istekleri oluşturup üretilen metni geri alırsınız.
- Bir kitaplık kullanmak. Kitaplıklar API çağrılarını kapsüller ve kullanımı kolaylaştırır.

## Kitaplıklar/SDK'lar

LLM'lerle çalışmak için bilinen birkaç kitaplık vardır, örneğin:

- **openai**, bu kitaplık modelinize bağlanmayı ve istem göndermeyi kolaylaştırır.

Ayrıca daha üst seviyede çalışan kitaplıklar da vardır, örneğin:

- **Langchain**. Langchain iyi bilinir ve Python'u destekler.
- **Semantic Kernel**. Semantic Kernel, Microsoft tarafından geliştirilen ve C#, Python ve Java dillerini destekleyen bir kitaplıktır.

## openai kullanarak ilk uygulama

İlk uygulamamızı nasıl oluşturacağımızı, hangi kitaplıklara ihtiyacımız olduğunu, ne kadar gereksinim olduğunu görelim.

### openai kurulumu

OpenAI veya Azure OpenAI ile etkileşim için birçok kitaplık vardır. C#, Python, JavaScript, Java gibi çeşitli programlama dilleri de kullanılabilir. Biz `openai` Python kitaplığını kullanmayı seçtik, bu nedenle yüklemek için `pip` kullanacağız.

```bash
pip install openai
```

### Bir kaynak oluştur

Şu adımları gerçekleştirmeniz gerekiyor:

- Azure'da bir hesap oluşturun [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Azure OpenAI erişimi kazanın. Bunu yapmak için [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) adresine gidin ve erişim talebinde bulunun.

  > [!NOTE]
  > Yazının yazıldığı tarihte Azure OpenAI erişimi için başvuruda bulunmanız gerekmektedir.

- Python'u yükleyin <https://www.python.org/>
- Bir Azure OpenAI Servis kaynağı oluşturmuş olun. Kaynak oluşturma hakkında bilgi için bu rehbere bakabilirsiniz [kaynak oluşturma](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### API anahtarı ve uç noktayı bulun

Şimdi, `openai` kitaplığınıza hangi API anahtarını kullanacağını belirtmeniz gerekiyor. API anahtarınızı bulmak için Azure OpenAI kaynağınızın "Anahtarlar ve Uç Nokta" bölümüne gidin ve "Anahtar 1" değerini kopyalayın.

![Azure Portal'da Anahtarlar ve Uç Nokta kaynak paneli](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Bu bilgiyi kopyaladıktan sonra, kitaplıklara bunu kullanacaklarını talimat verelim.

> [!NOTE]
> API anahtarınızı kodunuzdan ayrı tutmak faydalıdır. Bunu ortam değişkenleri kullanarak yapabilirsiniz.
>
> - Ortam değişkeni olarak `OPENAI_API_KEY` değerini API anahtarınızla ayarlayın.
>   `export OPENAI_API_KEY='sk-...'`

### Azure yapılandırmasını ayarlama

Azure OpenAI (şimdi Microsoft Foundry'nin bir parçası) kullanıyorsanız, işte yapılandırmayı nasıl ayarlayacağınız. Standart `OpenAI` istemcisini Azure OpenAI `/openai/v1/` uç noktasına yönlendiriyoruz; bu, Responses API ile çalışır ve `api_version` gerektirmez:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Yukarıda aşağıdakileri ayarlıyoruz:

- `api_key`, bu Azure Portal veya Microsoft Foundry portalında bulunan API anahtarınızdır.
- `base_url`, bu Foundry kaynak uç noktanızdır ve sonuna `/openai/v1/` eklenmiştir. Kararlı v1 uç noktası, OpenAI ve Azure OpenAI arasında `api_version` yönetimi olmadan çalışır.

> [!NOTE] > `os.environ` ortam değişkenlerini okur. `AZURE_OPENAI_API_KEY` ve `AZURE_OPENAI_ENDPOINT` gibi ortam değişkenlerini okumak için kullanabilirsiniz. Bu ortam değişkenlerini terminalinizde veya `dotenv` gibi bir kütüphane kullanarak ayarlayın.

## Metin oluşturma

Metin oluşturmanın yolu, Responses API'yi `responses.create` yöntemi aracılığıyla kullanmaktır. İşte bir örnek:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

Yukarıdaki kodda, bir yanıt oluşturuyoruz ve kullanmak istediğimiz modeli ve istemi geçiriyoruz. Ardından `response.output_text` ile oluşturulan metni yazdırıyoruz.

### Çok turlu sohbetler

Responses API, hem tek turluk metin oluşturma hem de çok turlu sohbet botları için uygundur - bir konuşma oluşturmak için `input` içinde mesaj listesi sağlarsınız:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Bu işlevsellik hakkında daha fazlası ilerleyen bir bölümde.

## Alıştırma - ilk metin oluşturma uygulamanız

OpenAI'yı nasıl ayarlayacağımızı ve yapılandıracağımızı öğrendiğimize göre, ilk metin oluşturma uygulamanızı oluşturma zamanı. Uygulamanızı oluşturmak için şu adımları izleyin:

1. Bir sanal ortam oluşturun ve openai yükleyin:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Windows kullanıyorsanız, `venv\Scripts\activate` yazın, `source venv/bin/activate` yerine.

   > [!NOTE]
   > Azure OpenAI anahtarınızı bulmak için [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) adresine gidin, `Open AI`'yi arayın, ardından `Open AI resource` seçin, sonra `Keys and Endpoint` seçin ve `Key 1` değerini kopyalayın.

1. _app.py_ dosyası oluşturun ve şu kodu yazın:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"

   # make a request using the Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # print response
   print(response.output_text)
   ```

   > [!NOTE]
   > Düz OpenAI (Azure olmayan) kullanıyorsanız, `client = OpenAI(api_key="<replace this value with your OpenAI key>")` kullanın (`base_url` olmadan) ve `gpt-5-mini` gibi bir model adını dağıtım adı yerine geçirin.

   Aşağıdaki gibi bir çıktı görmelisiniz:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Farklı şeyler için farklı istemler

Artık bir istem kullanarak metin oluşturmayı gördünüz. Hatta değiştirip farklı türde metinler oluşturabileceğiniz çalışan bir programınız var.

İstemler her türlü görev için kullanılabilir. Örneğin:

- **Bir metin türü oluşturma**. Örneğin, bir şiir, quiz için sorular vb. oluşturabilirsiniz.
- **Bilgi arama**. İstemleri, 'Web geliştirmede CORS ne anlama gelir?' gibi bilgi aramak için kullanabilirsiniz.
- **Kod oluşturma**. Kod oluşturmak için istemler kullanabilirsiniz, örneğin e-postaları doğrulamak için düzenli bir ifade geliştirmek veya neden bir web uygulaması gibi tüm bir program oluşturmayasınız?

## Daha pratik bir kullanım: tarif oluşturucu

Evde malzemeleriniz olduğunu ve bir şeyler pişirmek istediğinizi hayal edin. Bunun için bir tarife ihtiyacınız var. Tarif bulmanın bir yolu arama motoru kullanmak ya da LLM kullanmak olabilir.

Şöyle bir istem yazabilirsiniz:

> "Aşağıdaki malzemelerle yapılabilecek 5 yemek tarifi göster: tavuk, patates ve havuç. Her bir tarif için kullanılan tüm malzemeleri listele"

Yukarıdaki isteme, benzer bir yanıt alabilirsiniz:

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

Bu sonuç harika, ne pişireceğimi biliyorum. Bu noktada faydalı olabilecek geliştirmeler şunlar olabilir:

- Sevmediğim veya alerjim olan malzemeleri filtrelemek.
- Evde tüm malzemeler yoksa alışveriş listesi oluşturmak.

Yukarıdaki durumlar için ek bir istem ekleyelim:

> "Sarımsak alerjim olduğu için tariflerden çıkarın ve yerine başka birşey koyun. Ayrıca, evde tavuk, patates ve havuç olduğunu dikkate alarak tarifler için alışveriş listesi oluşturun."

İşte yeni bir sonuç aldınız, şöyle ki:

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

İşte sarımsak içermeyen beş tarifiniz ve evde olanları dikkate alan alışveriş listeniz.

## Alıştırma - tarif oluşturucu yapın

Bir senaryoyu oynadığımıza göre, gösterilen senaryoya uygun kod yazalım. Bunun için şu adımları takip edin:

1. Mevcut _app.py_ dosyasını başlangıç noktası olarak kullanın
1. `prompt` değişkenini bulun ve kodunu şu şekilde değiştirin:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Şimdi kodu çalıştırırsanız, şöyle bir çıktı görmelisiniz:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOT: LLM'niz deterministik değildir, bu yüzden programı her çalıştırdığınızda farklı sonuçlar alabilirsiniz.

   Harika, şimdi nasıl geliştirebileceğimize bakalım. Geliştirmek için kodun esnek olmasını istemeliyiz, böylece tarif sayısı ve malzemeler değiştirilebilir ve geliştirilebilir.

1. Şu şekilde kodu değiştelim:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Test amaçlı çalıştırdığımızda, şöyle görünebilir:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Filtre ve alışveriş listesi ekleyerek geliştirme

Şimdi kullanıcı girdilerine bağlı olarak hem tarif sayısı hem de kullanılan malzemeleri değiştirebilen çalışan bir uygulamamız var.

Bunu daha da geliştirmek için şunları eklemek istiyoruz:

- **Malzemeleri filtreleme**. Sevmediğimiz veya alerjimiz olan malzemeleri filtreleyebilmeliyiz. Bunu yapmak için mevcut istemimizi şu şekilde değiştirebilir ve sonunda filtre koşulu ekleyebiliriz:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Yukarıda, istemin sonuna `{filter}` ekliyoruz ve kullanıcıdan filtre değerini alıyoruz.

  Program çalıştırılırken örnek bir giriş şu şekilde olabilir:

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

  Gördüğünüz gibi, içinde süt olan tarifler filtrelendi. Ancak laktoz intoleransınız varsa peynir içeren tarifleri de filtrelemek isteyebilirsiniz; bu nedenle bu durumun net olması gerekir.

- **Alışveriş listesi oluşturma**. Evde olanları dikkate alarak alışveriş listesi oluşturmak istiyoruz.

  Bu işlevsellik için her şeyi tek bir istemle çözmeye çalışabiliriz ya da iki ayrı isteme bölebiliriz. İkinci yöntemi deneyelim. Burada ek bir istem eklemeyi öneriyoruz, ancak bunun çalışması için önceki istemin sonucunu sonraki isteme bağlam olarak eklememiz gerekir.

  Koddaki ilk istemin sonucunu yazdıran kısmı bulun ve aşağıdaki kodu altına ekleyin:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Şuna dikkat edin:

  1. Yeni bir istem oluşturuyoruz, önceki istemin sonucunu yeni isteme ekleyerek:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Yeni bir istek yapıyoruz, ancak ilk istemde istediğimiz token sayısını da dikkate alarak, bu sefer `max_output_tokens` 1200 olarak ayarlanmıştır.

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

Şu ana kadar elimizde çalışan bir kod var, ancak işleri daha da iyileştirmek için yapmamız gereken bazı ince ayarlar var. Yapmamız gereken bazı şeyler şunlardır:

- **Gizli bilgileri koddan ayırın**, örneğin API anahtarı gibi. Gizli bilgiler kodda olmamalı ve güvenli bir yerde saklanmalıdır. Gizli bilgileri koddan ayırmak için ortam değişkenlerini ve `python-dotenv` gibi bir dosyadan yüklemek için kütüphaneleri kullanabiliriz. Bunun kodda nasıl görüneceği şöyle olur:

  1. Aşağıdaki içeriğe sahip bir `.env` dosyası oluşturun:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Not, Microsoft Foundry'deki Azure OpenAI için aşağıdaki ortam değişkenlerini ayarlamanız gerekir:

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

- **Token uzunluğuna dair bir not**. İstediğimiz metni oluşturmak için kaç token gerektiğini dikkate almalıyız. Tokenlar para tutar, bu yüzden mümkün olan yerlerde, kullandığımız token sayısında ekonomik olmaya çalışmalıyız. Örneğin, prompt'u daha az token kullanacak şekilde formüle edebilir miyiz?

  Kullanılan token sayısını değiştirmek için `max_output_tokens` parametresini kullanabilirsiniz. Örneğin, 100 token kullanmak isterseniz, şöyle yaparsınız:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Sıcaklıkla denemeler yapmak**. Sıcaklıktan şimdiye kadar bahsetmedik ancak programımızın performansı açısından önemli bir bağlamdır. Sıcaklık değeri ne kadar yüksekse, çıktı o kadar rastgele olur. Tersine, sıcaklık değeri ne kadar düşükse, çıktı o kadar öngörülebilir olur. Çıktınızda varyasyon isteyip istemediğinizi düşünün.

  Sıcaklığı değiştirmek için `temperature` parametresini kullanabilirsiniz. Örneğin, 0.5 sıcaklık kullanmak isterseniz, şöyle yaparsınız:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Not, 1.0'a ne kadar yakınsa çıktı o kadar çeşitli olur.

- **Akıl yürütme modelleri `temperature` kullanmaz**. Bu önemli bir 2026 değişikliği. Microsoft Foundry'deki mevcut, kullanım dışı olmayan modeller **akıl yürütme modelleridir** (GPT-5 ailesi, o-serisi) - ve **`temperature` veya `top_p` desteklemezler** (ayrıca `max_tokens` değil; onun yerine `max_output_tokens` kullanın). Eğer `temperature` gönderirseniz `gpt-5-mini` için "parametre desteklenmiyor" hatası alırsınız. Yukarıdaki sıcaklık örneğini denemek için, örneğin açık bir **Llama** modeli olan `Llama-3.3-70B-Instruct`'u [Microsoft Foundry model kataloğu](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) üzerinden Foundry Modelleri / Azure AI Inference uç noktasıyla çağırabilirsiniz (tıpkı `githubmodels-*` örneklerinde olduğu gibi). GPT-5 gibi akıl yürütme modellerinde çıktıyı farklı şekilde yönlendirirsiniz:
  - **Prompt mühendisliği** - açık talimatlar, örnekler ve yapılandırılmış çıktı (bkz. ders [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) örnek ayar düğmelerinin yaptığı işi yapar.
  - **Muhakeme kontrolleri** - muhakeme çabası/ayrıntı parametreleri, muhakemenin derinliği ile gecikme ve maliyet arasında bir denge kurar.

  Kısaca: `temperature`/`top_p` birçok modelde hala geçerlidir (Llama, Mistral, Phi ve GPT-4.x ailesi - ancak GPT-4.x kullanım dışı kalıyor), ancak ilerleme yönü GPT-5 gibi muhakeme modellerinde prompt mühendisliği + muhakeme kontrolleridir.

## Ödev

Bu ödev için ne yapacağınıza kendiniz karar verebilirsiniz.

İşte bazı öneriler:

- Tarif oluşturucu uygulamasını daha da geliştirmek için ince ayar yapın. Sıcaklık değerleriyle ve promptlarla oynayın, neler yapabileceğinizi görün.
- Bir "çalışma arkadaşı" yapın. Bu uygulama, örneğin Python konusu hakkında soruları yanıtlayabilmeli, "Python'da belirli bir konu nedir?" gibi promptlarınız olabilir ya da "Bir konuda kod göster" gibi promptlar kullanabilirsiniz.
- Tarih botu, tarihi canlandırın, bota belirli tarihi bir karakteri oynatmasını söyleyin ve onun hayatı ve dönemi hakkında sorular sorun.

## Çözüm

### Çalışma arkadaşı

Aşağıda bir başlangıç promptu var, nasıl kullanabileceğinizi görün ve isteğinize göre değiştirin.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Tarih botu

İşte kullanabileceğiniz bazı promptlar:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Bilgi kontrolü

Sıcaklık kavramı ne yapar?

1. Çıktının ne kadar rastgele olduğunu kontrol eder.
1. Yanıtın ne kadar büyük olduğunu kontrol eder.
1. Kaç token kullanıldığını kontrol eder.

## 🚀 Meydan Okuma

Ödev üzerinde çalışırken sıcaklığı değiştirin, 0, 0.5 ve 1 olarak ayarlamayı deneyin. Unutmayın, 0 en az değişken ve 1 en çok değişkendir. Uygulamanız için hangi değer en iyi çalışıyor?

## Harika İş! Öğrenmeye Devam Edin

Bu dersi tamamladıktan sonra, Generative AI bilginizi geliştirmeye devam etmek için [Generative AI Öğrenme koleksiyonumuza](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) göz atın!

Ders 7'ye geçin, burada [sohbet uygulamaları nasıl geliştirilir](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) öğreneceğiz!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->