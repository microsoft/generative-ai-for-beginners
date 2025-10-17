<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00e33cd3ff945511446ecda4a9f8a828",
  "translation_date": "2025-10-17T16:15:31+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "tr"
}
-->
# Metin Üretim Uygulamaları Oluşturma

[![Metin Üretim Uygulamaları Oluşturma](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.tr.png)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Bu dersin videosunu izlemek için yukarıdaki görsele tıklayın)_

Bu müfredatta şimdiye kadar, istemler gibi temel kavramlar ve hatta "istem mühendisliği" adı verilen bir disiplin olduğunu gördünüz. ChatGPT, Office 365, Microsoft Power Platform gibi birçok araç, bir şeyler başarmak için istemleri kullanmanızı destekler.

Bir uygulamaya böyle bir deneyim eklemek için istemler, tamamlamalar gibi kavramları anlamanız ve çalışmak için bir kütüphane seçmeniz gerekir. Bu bölümde tam olarak bunları öğreneceksiniz.

## Giriş

Bu bölümde:

- openai kütüphanesi ve temel kavramları hakkında bilgi edineceksiniz.
- openai kullanarak bir metin üretim uygulaması oluşturacaksınız.
- Bir metin üretim uygulaması oluşturmak için istem, sıcaklık ve token gibi kavramları nasıl kullanacağınızı anlayacaksınız.

## Öğrenme hedefleri

Bu dersin sonunda şunları yapabileceksiniz:

- Metin üretim uygulamasının ne olduğunu açıklayın.
- openai kullanarak bir metin üretim uygulaması oluşturun.
- Uygulamanızı daha fazla veya daha az token kullanacak şekilde yapılandırın ve ayrıca sıcaklığı değiştirerek farklı çıktılar elde edin.

## Metin üretim uygulaması nedir?

Genelde bir uygulama oluşturduğunuzda aşağıdaki gibi bir arayüze sahip olur:

- Komut tabanlı. Konsol uygulamaları, bir komut yazıp bir görevi yerine getirdiğiniz tipik uygulamalardır. Örneğin, `git` bir komut tabanlı uygulamadır.
- Kullanıcı arayüzü (UI). Bazı uygulamalar, düğmelere tıklayabileceğiniz, metin girebileceğiniz, seçenekler seçebileceğiniz ve daha fazlasını yapabileceğiniz grafiksel kullanıcı arayüzlerine (GUI) sahiptir.

### Konsol ve UI uygulamaları sınırlıdır

Bir komut tabanlı uygulama ile karşılaştırıldığında:

- **Sınırlıdır**. Herhangi bir komut yazamazsınız, yalnızca uygulamanın desteklediği komutları yazabilirsiniz.
- **Dil spesifik**. Bazı uygulamalar birçok dili destekler, ancak varsayılan olarak uygulama belirli bir dil için oluşturulmuştur, ek dil desteği ekleyebilseniz bile.

### Metin üretim uygulamalarının faydaları

Peki, bir metin üretim uygulaması nasıl farklıdır?

Bir metin üretim uygulamasında daha fazla esnekliğe sahipsiniz, belirli bir komut seti veya belirli bir giriş diliyle sınırlı değilsiniz. Bunun yerine, uygulama ile etkileşim kurmak için doğal dili kullanabilirsiniz. Bir diğer avantajı ise, zaten geniş bir bilgi birikimi üzerine eğitilmiş bir veri kaynağı ile etkileşimde bulunuyor olmanızdır; oysa geleneksel bir uygulama genellikle bir veritabanında bulunanlarla sınırlıdır.

### Metin üretim uygulamasıyla neler yapabilirim?

Birçok şey yapabilirsiniz. Örneğin:

- **Bir sohbet botu**. Şirketiniz ve ürünleri gibi konular hakkında soruları yanıtlayan bir sohbet botu iyi bir seçenek olabilir.
- **Yardımcı**. LLM'ler metin özetleme, metinden içgörüler elde etme, özgeçmiş gibi metinler üretme ve daha fazlası gibi konularda harikadır.
- **Kod asistanı**. Kullandığınız dil modeline bağlı olarak, kod yazmanıza yardımcı olan bir kod asistanı oluşturabilirsiniz. Örneğin, GitHub Copilot veya ChatGPT gibi bir ürün kullanarak kod yazmanıza yardımcı olabilirsiniz.

## Nasıl başlayabilirim?

Bir LLM ile entegre olmanın bir yolunu bulmanız gerekir, bu genellikle iki yaklaşımı içerir:

- Bir API kullanın. Burada isteminizi içeren web istekleri oluşturur ve size üretilmiş metni geri alırsınız.
- Bir kütüphane kullanın. Kütüphaneler API çağrılarını kapsar ve kullanımı kolaylaştırır.

## Kütüphaneler/SDK'lar

LLM'lerle çalışmak için bilinen birkaç kütüphane vardır, örneğin:

- **openai**, bu kütüphane modelinize bağlanmayı ve istem göndermeyi kolaylaştırır.

Daha yüksek seviyede çalışan kütüphaneler de vardır, örneğin:

- **Langchain**. Langchain iyi bilinir ve Python'u destekler.
- **Semantic Kernel**. Semantic Kernel, Microsoft tarafından geliştirilen ve C#, Python ve Java dillerini destekleyen bir kütüphanedir.

## openai ile ilk uygulama

İlk uygulamamızı nasıl oluşturabileceğimizi, hangi kütüphanelere ihtiyacımız olduğunu, ne kadar gereklilik olduğunu ve daha fazlasını görelim.

### openai'yi yükleme

OpenAI veya Azure OpenAI ile etkileşim kurmak için birçok kütüphane vardır. C#, Python, JavaScript, Java ve daha fazlası gibi birçok programlama dili kullanmak da mümkündür. Biz `openai` Python kütüphanesini seçtik, bu yüzden `pip` kullanarak yükleyeceğiz.

```bash
pip install openai
```

### Bir kaynak oluşturma

Aşağıdaki adımları gerçekleştirmeniz gerekir:

- Azure'da bir hesap oluşturun [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Azure OpenAI'ye erişim kazanın. [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) adresine gidin ve erişim talep edin.

  > [!NOTE]
  > Yazım sırasında, Azure OpenAI'ye erişim için başvurmanız gerekiyor.

- Python'u yükleyin <https://www.python.org/>
- Azure OpenAI Hizmeti kaynağı oluşturmuş olun. [Kaynak oluşturma](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst) rehberine bakın.

### API anahtarını ve uç noktasını bulma

Bu noktada, `openai` kütüphanenize hangi API anahtarını kullanacağını söylemeniz gerekiyor. API anahtarınızı bulmak için Azure OpenAI kaynağınızın "Anahtarlar ve Uç Nokta" bölümüne gidin ve "Anahtar 1" değerini kopyalayın.

![Azure Portal'daki Anahtarlar ve Uç Nokta kaynak paneli](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Artık bu bilgiyi kopyaladığınıza göre, kütüphanelere bunu kullanmalarını söyleyelim.

> [!NOTE]
> API anahtarınızı kodunuzdan ayırmak faydalıdır. Bunu ortam değişkenlerini kullanarak yapabilirsiniz.
>
> - Ortam değişkeni `OPENAI_API_KEY`'i API anahtarınıza ayarlayın.
>   `export OPENAI_API_KEY='sk-...'`

### Azure yapılandırmasını ayarlama

Azure OpenAI kullanıyorsanız, yapılandırmayı şu şekilde ayarlayabilirsiniz:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Yukarıda şunları ayarlıyoruz:

- `api_type` değerini `azure` olarak ayarlıyoruz. Bu, kütüphaneye OpenAI yerine Azure OpenAI'yi kullanmasını söyler.
- `api_key`, Azure Portal'da bulunan API anahtarınızdır.
- `api_version`, kullanmak istediğiniz API sürümüdür. Yazım sırasında en son sürüm `2023-05-15`'tir.
- `api_base`, API'nin uç noktasıdır. Bunu Azure Portal'da API anahtarınızın yanında bulabilirsiniz.

> [!NOTE] > `os.getenv` ortam değişkenlerini okuyan bir işlevdir. `OPENAI_API_KEY` ve `API_BASE` gibi ortam değişkenlerini okumak için kullanabilirsiniz. Bu ortam değişkenlerini terminalinizde veya `dotenv` gibi bir kütüphane kullanarak ayarlayın.

## Metin üretme

Metin üretmenin yolu `Completion` sınıfını kullanmaktır. İşte bir örnek:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

Yukarıdaki kodda, bir tamamlama nesnesi oluşturuyoruz ve kullanmak istediğimiz modeli ve istemi iletiyoruz. Ardından üretilen metni yazdırıyoruz.

### Sohbet tamamlamaları

Şimdiye kadar, metin üretmek için `Completion` kullandığımızı gördünüz. Ancak sohbet botları için daha uygun olan başka bir sınıf olan `ChatCompletion` vardır. İşte bunu kullanmanın bir örneği:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Bu işlevsellik hakkında daha fazla bilgi bir sonraki bölümde.

## Alıştırma - ilk metin üretim uygulamanız

Artık openai'yi nasıl kuracağımızı ve yapılandıracağımızı öğrendik, ilk metin üretim uygulamanızı oluşturma zamanı. Uygulamanızı oluşturmak için şu adımları izleyin:

1. Sanal bir ortam oluşturun ve openai'yi yükleyin:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Windows kullanıyorsanız `source venv/bin/activate` yerine `venv\Scripts\activate` yazın.

   > [!NOTE]
   > Azure OpenAI anahtarınızı bulmak için [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) adresine gidin, `Open AI` araması yapın ve `Open AI kaynağı`nı seçin, ardından `Anahtarlar ve Uç Nokta` seçeneğini seçin ve `Anahtar 1` değerini kopyalayın.

1. _app.py_ adlı bir dosya oluşturun ve aşağıdaki kodu ekleyin:

   ```python
   import openai

   openai.api_key = "<replace this value with your open ai key or Azure OpenAI key>"

   openai.api_type = 'azure'
   openai.api_version = '2023-05-15'
   openai.api_base = "<endpoint found in Azure Portal where your API key is>"
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"
   messages = [{"role": "user", "content": prompt}]

   # make completion
   completion = openai.chat.completions.create(model=deployment_name, messages=messages)

   # print response
   print(completion.choices[0].message.content)
   ```

   > [!NOTE]
   > Azure OpenAI kullanıyorsanız, `api_type` değerini `azure` olarak ayarlamanız ve `api_key` değerini Azure OpenAI anahtarınıza ayarlamanız gerekir.

   Şu şekilde bir çıktı görmelisiniz:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Farklı şeyler için farklı türde istemler

Artık bir istem kullanarak metin üretmeyi gördünüz. Hatta farklı türde metinler üretmek için değiştirebileceğiniz ve değiştirebileceğiniz bir programınız var.

İstemler çeşitli görevler için kullanılabilir. Örneğin:

- **Bir tür metin üretme**. Örneğin, bir şiir, bir sınav için sorular vb. üretebilirsiniz.
- **Bilgi arama**. İstemleri, 'Web geliştirmede CORS ne anlama gelir?' gibi bilgiler aramak için kullanabilirsiniz.
- **Kod üretme**. İstemleri, e-postaları doğrulamak için kullanılan bir düzenli ifade geliştirmek veya neden bir web uygulaması gibi bir program oluşturmak için kullanabilirsiniz.

## Daha pratik bir kullanım örneği: bir tarif oluşturucu

Evde malzemeleriniz olduğunu ve bir şeyler pişirmek istediğinizi hayal edin. Bunun için bir tarife ihtiyacınız var. Tarif bulmanın bir yolu bir arama motoru kullanmak veya bir LLM kullanmak olabilir.

Şöyle bir istem yazabilirsiniz:

> "Tavuk, patates ve havuç içeren bir yemek için 5 tarif göster. Tarif başına kullanılan tüm malzemeleri listele."

Yukarıdaki isteme göre, şu şekilde bir yanıt alabilirsiniz:

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

Bu sonuç harika, ne pişireceğimi biliyorum. Bu noktada, faydalı olabilecek iyileştirmeler şunlardır:

- Sevmediğim veya alerjik olduğum malzemeleri filtrelemek.
- Evde tüm malzemelere sahip değilsem bir alışveriş listesi oluşturmak.

Yukarıdaki durumlar için ek bir istem ekleyelim:

> "Lütfen sarımsak içeren tarifleri çıkarın çünkü alerjim var ve yerine başka bir şey koyun. Ayrıca, evde tavuk, patates ve havuç olduğunu göz önünde bulundurarak tarifler için bir alışveriş listesi oluşturun."

Şimdi yeni bir sonuç alıyorsunuz, yani:

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

İşte sarımsak içermeyen beş tarifiniz ve ayrıca evde zaten sahip olduğunuz malzemeleri göz önünde bulundurarak bir alışveriş listeniz var.

## Alıştırma - bir tarif oluşturucu oluşturun

Artık bir senaryoyu oynadık, şimdi gösterilen senaryoya uygun kod yazalım. Bunu yapmak için şu adımları izleyin:

1. Mevcut _app.py_ dosyasını başlangıç noktası olarak kullanın.
1. `prompt` değişkenini bulun ve kodunu şu şekilde değiştirin:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Şimdi kodu çalıştırırsanız, şu şekilde bir çıktı görmelisiniz:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOT, LLM'niz deterministik değildir, bu yüzden programı her çalıştırdığınızda farklı sonuçlar alabilirsiniz.

   Harika, şimdi işleri nasıl geliştirebileceğimizi görelim. İşleri geliştirmek için kodun esnek olduğundan emin olmak istiyoruz, böylece malzemeler ve tarif sayısı geliştirilebilir ve değiştirilebilir.

1. Kodu şu şekilde değiştirin:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Kodun test çalıştırması şu şekilde görünebilir:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Filtre ve alışveriş listesi ekleyerek geliştirme

Artık tarifler üretebilen ve kullanıcıdan hem tarif sayısı hem de kullanılan malzemelerle ilgili girdilere dayanan esnek bir uygulamamız var.

Bunu daha da geliştirmek için aşağıdakileri eklemek istiyoruz:

- **Malzemeleri filtreleme**. Sevmediğimiz veya alerjik olduğumuz malzemeleri filtrelemek istiyoruz. Bu değişikliği gerçekleştirmek için mevcut istemimizi düzenleyebilir ve sonuna bir filtre koşulu ekleyebiliriz:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Yukarıda, istemin sonuna `{filter}` ekliyoruz ve ayrıca kullanıcıdan filtre değerini alıyoruz.

  Programı çalıştırırken bir örnek giriş şu şekilde görünebilir:

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

  Gördüğünüz gibi, içinde süt bulunan tarifler filtrelenmiştir. Ancak, laktoz intoleransınız varsa, içinde peynir bulunan tarifleri de filtrelemek isteyebilirsiniz, bu yüzden net olmak önemlidir.

- **Bir alışveriş listesi oluşturma**. Evde zaten sahip olduğumuz malzemeleri göz önünde bulundurarak bir alışveriş listesi oluşturmak istiyoruz.

  Bu işlevsellik için her şeyi tek bir istemde çözmeyi deneyebiliriz veya iki isteme bölebiliriz. İkinci yaklaşımı deneyelim. Burada ek bir istem eklemeyi öneriyoruz, ancak bunun çalışması için önceki istemin sonucunu bağlam olarak ek isteme eklememiz gerekiyor.
Kodda, ilk istemden gelen sonucu yazdıran kısmı bulun ve aşağıdaki kodu ekleyin:

  ```python
  old_prompt_result = completion.choices[0].message.content
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  messages = [{"role": "user", "content": new_prompt}]
  completion = openai.Completion.create(engine=deployment_name, messages=messages, max_tokens=1200)

  # print response
  print("Shopping list:")
  print(completion.choices[0].message.content)
  ```

Şunlara dikkat edin:

1. Yeni bir istem oluşturuyoruz, ilk istemden gelen sonucu yeni isteme ekliyoruz:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

1. Yeni bir istek yapıyoruz, ancak ilk istemde istediğimiz token sayısını da dikkate alıyoruz, bu yüzden bu sefer `max_tokens` değerini 1200 olarak belirtiyoruz.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

Bu kodu çalıştırdığımızda, aşağıdaki çıktıya ulaşıyoruz:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Kurulumunuzu İyileştirin

Şu ana kadar çalışan bir kodumuz var, ancak işleri daha da geliştirmek için yapmamız gereken bazı düzenlemeler var. Yapmamız gereken bazı şeyler şunlar:

- **Gizli bilgileri koddan ayırın**, örneğin API anahtarı. Gizli bilgiler kodda yer almamalı ve güvenli bir yerde saklanmalıdır. Gizli bilgileri koddan ayırmak için ortam değişkenlerini ve `python-dotenv` gibi kütüphaneleri kullanarak bunları bir dosyadan yükleyebiliriz. İşte kodda bunun nasıl görüneceği:

  1. Aşağıdaki içeriğe sahip bir `.env` dosyası oluşturun:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Not: Azure için aşağıdaki ortam değişkenlerini ayarlamanız gerekiyor:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     Kodda, ortam değişkenlerini şu şekilde yükleyebilirsiniz:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Token uzunluğu hakkında bir not**. İstediğimiz metni oluşturmak için kaç token gerektiğini düşünmeliyiz. Tokenlar maliyetlidir, bu yüzden mümkün olduğunca kullandığımız token sayısını ekonomik tutmaya çalışmalıyız. Örneğin, istemi daha az token kullanacak şekilde ifade edebilir miyiz?

  Kullanılan tokenları değiştirmek için `max_tokens` parametresini kullanabilirsiniz. Örneğin, 100 token kullanmak istiyorsanız, şu şekilde yapabilirsiniz:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Sıcaklık ile denemeler yapmak**. Sıcaklık, şu ana kadar bahsetmediğimiz ancak programımızın performansı için önemli bir bağlamdır. Sıcaklık değeri ne kadar yüksek olursa, çıktı o kadar rastgele olur. Tersine, sıcaklık değeri ne kadar düşük olursa, çıktı o kadar tahmin edilebilir olur. Çıktınızda çeşitlilik isteyip istemediğinizi düşünün.

  Sıcaklığı değiştirmek için `temperature` parametresini kullanabilirsiniz. Örneğin, sıcaklığı 0.5 olarak ayarlamak istiyorsanız, şu şekilde yapabilirsiniz:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Not: 1.0'a ne kadar yakın olursa, çıktı o kadar çeşitli olur.

## Ödev

Bu ödev için ne yapacağınızı seçebilirsiniz.

İşte bazı öneriler:

- Tarif oluşturucu uygulamasını daha da geliştirmek için ayarlamalar yapın. Sıcaklık değerleriyle ve istemlerle oynayın, neler ortaya çıkarabileceğinizi görün.
- "Çalışma arkadaşı" oluşturun. Bu uygulama, bir konu hakkında soruları yanıtlayabilmelidir. Örneğin Python hakkında, "Python'da belirli bir konu nedir?" gibi istemleriniz olabilir veya "Belirli bir konu için kod göster" gibi bir isteminiz olabilir.
- Tarih botu, tarihi canlandırın, botu belirli bir tarihi karakteri oynayacak şekilde yönlendirin ve onun hayatı ve dönemi hakkında sorular sorun.

## Çözüm

### Çalışma arkadaşı

Aşağıda bir başlangıç istemi bulunmaktadır, bunu nasıl kullanabileceğinizi ve kendi isteğinize göre nasıl ayarlayabileceğinizi görün.

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

## Bilgi kontrolü

Sıcaklık kavramı ne yapar?

1. Çıktının ne kadar rastgele olduğunu kontrol eder.
1. Yanıtın ne kadar büyük olduğunu kontrol eder.
1. Kullanılan token sayısını kontrol eder.

## 🚀 Meydan Okuma

Ödevi yaparken sıcaklığı değiştirmeyi deneyin, 0, 0.5 ve 1 olarak ayarlamayı deneyin. Unutmayın, 0 en az çeşitli ve 1 en çeşitli olanıdır. Uygulamanız için hangi değer en iyi çalışıyor?

## Harika İş! Öğrenmeye Devam Edin

Bu dersi tamamladıktan sonra, [Generative AI Learning koleksiyonumuzu](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) inceleyerek Generative AI bilginizi geliştirmeye devam edin!

7. Derse geçin, burada [sohbet uygulamaları oluşturmayı](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) inceleyeceğiz!

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çeviriler hata veya yanlışlıklar içerebilir. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.