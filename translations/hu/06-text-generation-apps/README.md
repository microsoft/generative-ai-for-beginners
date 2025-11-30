<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df027997f1448323d6159b78a1b669bf",
  "translation_date": "2025-10-17T21:22:22+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "hu"
}
-->
# Szövegalkotó alkalmazások építése

[![Szövegalkotó alkalmazások építése](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.hu.png)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Kattints a fenti képre a leckéhez tartozó videó megtekintéséhez)_

Eddig már láthattad ebben a tananyagban, hogy vannak alapvető fogalmak, mint például a promptok, és még egy egész diszciplína is létezik, amit "prompt mérnökségnek" neveznek. Számos eszköz, mint például a ChatGPT, az Office 365, a Microsoft Power Platform és mások, támogatják a promptok használatát bizonyos feladatok elvégzéséhez.

Ahhoz, hogy ilyen élményt adhass az alkalmazásodhoz, meg kell értened a promptok, a kiegészítések fogalmát, és ki kell választanod egy könyvtárat, amellyel dolgozhatsz. Pontosan ezt fogod megtanulni ebben a fejezetben.

## Bevezetés

Ebben a fejezetben:

- Megismerkedsz az openai könyvtárral és annak alapvető fogalmaival.
- Építesz egy szövegalkotó alkalmazást az openai segítségével.
- Megérted, hogyan használhatod a prompt, hőmérséklet és tokenek fogalmát egy szövegalkotó alkalmazás létrehozásához.

## Tanulási célok

A lecke végére képes leszel:

- Elmagyarázni, mi az a szövegalkotó alkalmazás.
- Építeni egy szövegalkotó alkalmazást az openai segítségével.
- Konfigurálni az alkalmazásodat, hogy több vagy kevesebb tokent használjon, illetve változtasd a hőmérsékletet a különböző kimenetek érdekében.

## Mi az a szövegalkotó alkalmazás?

Általában, amikor egy alkalmazást építesz, valamilyen felülettel rendelkezik, például:

- Parancsalapú. Konzolos alkalmazások tipikus példái azok az appok, ahol beírsz egy parancsot, és az végrehajt egy feladatot. Például a `git` egy parancsalapú alkalmazás.
- Felhasználói felület (UI). Néhány alkalmazás grafikus felhasználói felülettel (GUI) rendelkezik, ahol gombokat kattintasz, szöveget írsz be, opciókat választasz, stb.

### Konzolos és UI alkalmazások korlátai

Hasonlítsd össze egy parancsalapú alkalmazással, ahol beírsz egy parancsot:

- **Korlátozott**. Nem írhatsz be bármilyen parancsot, csak azokat, amelyeket az alkalmazás támogat.
- **Nyelvspecifikus**. Néhány alkalmazás több nyelvet is támogat, de alapértelmezés szerint az alkalmazás egy adott nyelvre van tervezve, még akkor is, ha további nyelvi támogatást hozzá lehet adni.

### Szövegalkotó alkalmazások előnyei

Miért különbözik egy szövegalkotó alkalmazás?

Egy szövegalkotó alkalmazásban nagyobb rugalmasságot kapsz, nem korlátozódik egy adott parancskészletre vagy bemeneti nyelvre. Ehelyett természetes nyelvet használhatsz az alkalmazással való interakcióhoz. További előny, hogy már egy hatalmas információs korpuszon képzett adatforrással lépsz kapcsolatba, míg egy hagyományos alkalmazás korlátozott lehet az adatbázisban található információkra.

### Mit lehet építeni egy szövegalkotó alkalmazással?

Számos dolgot lehet építeni. Például:

- **Chatbot**. Egy chatbot, amely válaszol kérdésekre különböző témákban, például a cégedről és annak termékeiről, jó választás lehet.
- **Segítő**. Az LLM-ek kiválóak olyan feladatokban, mint a szöveg összefoglalása, betekintések nyújtása szövegből, szöveg előállítása, például önéletrajzok készítése stb.
- **Kódsegéd**. Az általad használt nyelvi modell függvényében építhetsz egy kódsegédet, amely segít kódot írni. Például használhatsz olyan termékeket, mint a GitHub Copilot vagy a ChatGPT, hogy segítsenek a kódírásban.

## Hogyan kezdjek neki?

Nos, meg kell találnod egy módot az LLM integrálására, ami általában a következő két megközelítést foglalja magában:

- API használata. Itt webes kéréseket állítasz össze a promptoddal, és visszakapod a generált szöveget.
- Könyvtár használata. A könyvtárak segítenek az API-hívások becsomagolásában és könnyebbé teszik azok használatát.

## Könyvtárak/SDK-k

Néhány jól ismert könyvtár létezik az LLM-ekkel való munkához, például:

- **openai**, ez a könyvtár megkönnyíti a modellhez való csatlakozást és a promptok küldését.

Aztán vannak magasabb szintű könyvtárak, mint például:

- **Langchain**. A Langchain jól ismert, és támogatja a Python nyelvet.
- **Semantic Kernel**. A Semantic Kernel egy Microsoft által fejlesztett könyvtár, amely támogatja a C#, Python és Java nyelveket.

## Első alkalmazás openai használatával

Nézzük meg, hogyan építhetjük meg az első alkalmazásunkat, milyen könyvtárakra van szükség, mennyi munka szükséges, stb.

### openai telepítése

Számos könyvtár létezik az OpenAI vagy az Azure OpenAI használatához. Számos programozási nyelvet is használhatsz, mint például C#, Python, JavaScript, Java és mások. Mi az `openai` Python könyvtárat választottuk, így a `pip` segítségével telepítjük.

```bash
pip install openai
```

### Erőforrás létrehozása

A következő lépéseket kell végrehajtanod:

- Hozz létre egy fiókot az Azure-on [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Szerezz hozzáférést az Azure OpenAI-hoz. Látogass el ide: [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) és kérj hozzáférést.

  > [!NOTE]
  > A jelenlegi írás idején hozzáférést kell kérni az Azure OpenAI-hoz.

- Telepítsd a Python-t <https://www.python.org/>
- Hozz létre egy Azure OpenAI Service erőforrást. Lásd ezt az útmutatót az erőforrás [létrehozásához](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### API kulcs és végpont megkeresése

Ezen a ponton meg kell adnod az `openai` könyvtárnak, hogy melyik API kulcsot használja. Az API kulcsot az Azure OpenAI erőforrás "Keys and Endpoint" szekciójában találod, másold ki a "Key 1" értéket.

![Keys and Endpoint erőforrás panel az Azure Portálon](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Most, hogy ezt az információt kimásoltad, utasítsd a könyvtárakat, hogy használják.

> [!NOTE]
> Érdemes az API kulcsot elkülöníteni a kódtól. Ezt megteheted környezeti változók használatával.
>
> - Állítsd be az `OPENAI_API_KEY` környezeti változót az API kulcsodra.
>   `export OPENAI_API_KEY='sk-...'`

### Azure konfiguráció beállítása

Ha az Azure OpenAI-t használod, itt van, hogyan állítsd be a konfigurációt:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

A fentiekben a következőket állítjuk be:

- Az `api_type` értéke `azure`. Ez azt jelzi a könyvtárnak, hogy az Azure OpenAI-t használja, nem az OpenAI-t.
- `api_key`, ez az API kulcs, amelyet az Azure Portálon találsz.
- `api_version`, ez az API verziója, amelyet használni szeretnél. A jelenlegi írás idején a legújabb verzió a `2023-05-15`.
- `api_base`, ez az API végpontja. Az Azure Portálon található az API kulcs mellett.

> [!NOTE] > Az `os.getenv` egy olyan függvény, amely olvassa a környezeti változókat. Használhatod arra, hogy olvasd az olyan környezeti változókat, mint az `OPENAI_API_KEY` és az `API_BASE`. Állítsd be ezeket a környezeti változókat a terminálodban vagy egy `dotenv` nevű könyvtár segítségével.

## Szöveg generálása

A szöveg generálásának módja a `Completion` osztály használata. Íme egy példa:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

A fenti kódban létrehozunk egy kiegészítési objektumot, és megadjuk a használni kívánt modellt és a promptot. Ezután kiírjuk a generált szöveget.

### Chat kiegészítések

Eddig láthattad, hogyan használjuk a `Completion` osztályt szöveg generálására. Van azonban egy másik osztály, a `ChatCompletion`, amely jobban illik chatbotokhoz. Íme egy példa annak használatára:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Erről a funkcióról bővebben a következő fejezetben lesz szó.

## Gyakorlat - az első szövegalkotó alkalmazásod

Most, hogy megtanultuk, hogyan állítsuk be és konfiguráljuk az openai-t, itt az ideje, hogy megépítsd az első szövegalkotó alkalmazásodat. Az alkalmazás építéséhez kövesd az alábbi lépéseket:

1. Hozz létre egy virtuális környezetet és telepítsd az openai-t:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Ha Windows-t használsz, írd be `venv\Scripts\activate` a `source venv/bin/activate` helyett.

   > [!NOTE]
   > Keresd meg az Azure OpenAI kulcsodat a [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) oldalon, keress rá az `Open AI`-ra, válaszd ki az `Open AI erőforrást`, majd válaszd ki a `Keys and Endpoint` opciót, és másold ki a `Key 1` értéket.

1. Hozz létre egy _app.py_ fájlt, és add meg neki a következő kódot:

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
   > Ha az Azure OpenAI-t használod, be kell állítanod az `api_type` értékét `azure`-ra, és az `api_key`-t az Azure OpenAI kulcsodra.

   A következőhöz hasonló kimenetet kell látnod:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Különböző típusú promptok, különböző dolgokhoz

Most már láttad, hogyan lehet szöveget generálni egy prompt segítségével. Még egy működő programod is van, amelyet módosíthatsz és megváltoztathatsz különböző típusú szövegek generálásához.

A promptok mindenféle feladatra használhatók. Például:

- **Egy adott típusú szöveg generálása**. Például generálhatsz egy verset, kvízkérdéseket stb.
- **Információ keresése**. A promptok segítségével információt kereshetsz, például a következő kérdésre: "Mit jelent a CORS a webfejlesztésben?".
- **Kód generálása**. A promptok segítségével kódot generálhatsz, például egy e-mail címek érvényesítésére szolgáló reguláris kifejezést, vagy akár egy teljes programot, például egy webalkalmazást.

## Egy gyakorlatiasabb felhasználási eset: receptgenerátor

Képzeld el, hogy vannak otthon hozzávalóid, és szeretnél főzni valamit. Ehhez szükséged van egy receptre. Egy módja a receptek keresésének, ha keresőmotort használsz, vagy használhatsz egy LLM-et is erre.

Írhatsz egy ilyen promptot:

> "Mutass 5 receptet egy ételhez a következő hozzávalókkal: csirke, burgonya és sárgarépa. Receptenként sorold fel az összes felhasznált hozzávalót."

A fenti prompt alapján a következő választ kaphatod:

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

Ez az eredmény nagyszerű, tudom, mit főzzek. Ezen a ponton hasznos fejlesztések lehetnek:

- Azoknak a hozzávalóknak a kiszűrése, amelyeket nem szeretek vagy allergiás vagyok rájuk.
- Bevásárlólista készítése, arra az esetre, ha nem lenne meg minden hozzávaló otthon.

A fenti esetekhez adjunk hozzá egy további promptot:

> "Kérlek, távolítsd el a fokhagymát tartalmazó recepteket, mivel allergiás vagyok rá, és helyettesítsd valami mással. Továbbá készíts egy bevásárlólistát a receptekhez, figyelembe véve, hogy már van otthon csirke, burgonya és sárgarépa."

Most egy új eredményt kapsz, nevezetesen:

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

Ez az öt recept, fokhagyma nélkül, és van egy bevásárlólistád is, amely figyelembe veszi, hogy mi van már otthon.

## Gyakorlat - receptgenerátor építése

Most, hogy lejátszottunk egy forgatókönyvet, írjunk kódot, amely megfelel a bemutatott forgatókönyvnek. Ehhez kövesd az alábbi lépéseket:

1. Használd a meglévő _app.py_ fájlt kiindulási pontként.
1. Keresd meg a `prompt` változót, és módosítsd a kódját a következőre:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Ha most futtatod a kódot, a következőhöz hasonló kimenetet kell látnod:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > MEGJEGYZÉS, az LLM nem determinisztikus, így minden alkalommal eltérő eredményeket kaphatsz, amikor futtatod a programot.

   Nagyszerű, nézzük meg, hogyan lehet javítani a dolgokat. A javítás érdekében biztosítani szeretnénk, hogy a kód rugalmas legyen, így a hozzávalók és a receptek száma is módosítható és változtatható.

1. Módosítsd a kódot a következő módon:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   A kód tesztelése így nézhet ki:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Javítás szűrő és bevásárlólista hozzáadásával

Most már van egy működő alkalmazásunk, amely képes recepteket előállítani, és rugalmas, mivel a felhasználó bemeneteire támaszkodik, mind a receptek számában, mind a felhasznált hozzávalókban.

A további fejlesztés érdekében a következőket szeretnénk hozzáadni:

- **Hozzávalók kiszűrése**. Szeretnénk kiszűrni azokat a hozzávalókat, amelyeket nem szeretünk vagy allergiásak vagyunk rájuk. Ennek eléréséhez módosíthatjuk a meglévő promptot, és hozzáadhatunk egy szűrőfeltételt a végéhez, például így:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Fent hozzáadjuk a `{filter}`-t a prompt végéhez, és a szűrő értékét is begyűjtjük a felhasználótól.

  Egy példa bemenet a program futtatására most így nézhet ki:

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

  Ahogy látható,
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

  Jegyezd meg a következőket:

  1. Új promptot hozunk létre azáltal, hogy az első prompt eredményét hozzáadjuk az új prompthoz:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Új kérést küldünk, de figyelembe vesszük az első promptban kért tokenek számát is, így ezúttal a `max_tokens` értéke 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     Ha kipróbáljuk ezt a kódot, a következő eredményre jutunk:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Javítsd a beállításaidat

Amit eddig elértünk, az egy működő kód, de van néhány finomhangolás, amit elvégezhetünk, hogy tovább javítsuk a dolgokat. Néhány dolog, amit meg kell tennünk:

- **Válaszd el a titkos adatokat a kódtól**, például az API kulcsot. A titkos adatok nem tartoznak a kódba, ezeket biztonságos helyen kell tárolni. A titkos adatok elkülönítéséhez használhatunk környezeti változókat és olyan könyvtárakat, mint a `python-dotenv`, hogy egy fájlból töltsük be őket. Így néz ki ez a kódban:

  1. Hozz létre egy `.env` fájlt a következő tartalommal:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Megjegyzés: Az Azure esetében a következő környezeti változókat kell beállítani:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     A kódban így töltenéd be a környezeti változókat:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Egy megjegyzés a tokenek hosszáról**. Fontolóra kell vennünk, hogy hány tokenre van szükségünk a kívánt szöveg generálásához. A tokenek pénzbe kerülnek, ezért ahol csak lehet, próbáljunk meg takarékoskodni a felhasznált tokenek számával. Például megfogalmazhatjuk úgy a promptot, hogy kevesebb tokent használjunk.

  A felhasznált tokenek számának módosításához használhatod a `max_tokens` paramétert. Például, ha 100 tokent szeretnél használni, akkor ezt így teheted meg:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Kísérletezés a hőmérséklettel**. A hőmérséklet egy olyan tényező, amit eddig nem említettünk, de fontos szerepet játszik a program működésében. Minél magasabb a hőmérséklet értéke, annál véletlenszerűbb lesz az output. Ezzel szemben, minél alacsonyabb a hőmérséklet értéke, annál kiszámíthatóbb lesz az output. Fontold meg, hogy szeretnél-e változatosságot az eredményben vagy sem.

  A hőmérséklet módosításához használhatod a `temperature` paramétert. Például, ha 0.5 hőmérsékletet szeretnél használni, akkor ezt így teheted meg:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Megjegyzés: Minél közelebb van az érték az 1.0-hoz, annál változatosabb lesz az output.

## Feladat

A feladat során te döntheted el, hogy mit szeretnél készíteni.

Íme néhány javaslat:

- Finomítsd tovább a receptgeneráló alkalmazást. Kísérletezz a hőmérséklet értékekkel és a promptokkal, hogy meglásd, mit tudsz kihozni belőle.
- Készíts egy "tanulótársat". Ez az alkalmazás képes válaszolni egy adott témával kapcsolatos kérdésekre, például Python. Lehetnek olyan promptok, mint "Mi egy bizonyos téma a Pythonban?", vagy lehet egy olyan prompt, amely azt mondja, hogy mutasson kódot egy adott témához stb.
- Történelmi bot, keltsd életre a történelmet, utasítsd a botot, hogy játsszon el egy bizonyos történelmi karaktert, és tegyél fel neki kérdéseket az életéről és koráról.

## Megoldás

### Tanulótárs

Az alábbiakban egy kezdő promptot találsz, nézd meg, hogyan tudod használni és a saját ízlésed szerint alakítani.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Történelmi bot

Íme néhány prompt, amit használhatsz:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Tudásellenőrzés

Mit csinál a hőmérséklet koncepciója?

1. Szabályozza, hogy mennyire legyen véletlenszerű az output.
1. Szabályozza, hogy mekkora legyen a válasz.
1. Szabályozza, hogy hány tokent használjon.

## 🚀 Kihívás

A feladat megoldása során próbáld meg változtatni a hőmérsékletet, állítsd be 0-ra, 0.5-re és 1-re. Ne feledd, hogy 0 a legkevésbé változatos, míg 1 a legváltozatosabb. Melyik érték működik a legjobban az alkalmazásodhoz?

## Szép munka! Folytasd a tanulást

A leckét befejezve nézd meg a [Generatív AI tanulási gyűjteményt](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejleszthesd a generatív AI tudásodat!

Lépj tovább a 7. leckére, ahol megnézzük, hogyan lehet [chat alkalmazásokat készíteni](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.