# Szöveggeneráló alkalmazások építése

[![Szöveggeneráló alkalmazások építése](../../../translated_images/hu/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Kattints a fenti képre a lecke videójának megtekintéséhez)_

Eddig a tananyag során láthattad, hogy léteznek olyan alapfogalmak, mint a promptok, és még egy teljes tudományterület is létezik "prompt mérnökség" néven. Számos eszköz, amivel interakcióba léphetsz, például a ChatGPT, az Office 365, a Microsoft Power Platform és mások, támogatják a promptok használatát valamilyen cél elérésére.

Ahhoz, hogy az ilyen élményt egy alkalmazáshoz adj, meg kell értened olyan fogalmakat, mint a promptok, befejezések és ki kell választanod egy könyvtárat a használathoz. Pontosan ezt fogod megtanulni ebben a fejezetben.

## Bevezetés

Ebben a fejezetben a következőket fogod megtenni:

- Megismerkedsz az openai könyvtárral és annak alapfogalmaival.
- Építesz egy szöveggeneráló alkalmazást az openai segítségével.
- Megérted, hogyan használhatók olyan fogalmak, mint a prompt, hőmérséklet és tokenek egy szöveggeneráló alkalmazás építéséhez.

## Tanulási célok

A lecke végére képes leszel:

- Megmagyarázni, mi az a szöveggeneráló alkalmazás.
- Szöveggeneráló alkalmazást építeni az openai segítségével.
- Beállítani az alkalmazásodat úgy, hogy több vagy kevesebb token használjon, és változtathasd a hőmérsékletet a változatos kimenet érdekében.

## Mi az a szöveggeneráló alkalmazás?

Általában, amikor egy alkalmazást építesz, az valamilyen felülettel rendelkezik, például az alábbiak szerint:

- Parancs alapú. A konzolos alkalmazások tipikus példák, ahol beírsz egy parancsot, és az végrehajt egy feladatot. Például a `git` egy parancs alapú alkalmazás.
- Felhasználói felület (UI). Néhány alkalmazás grafikus felhasználói felülettel (GUI) rendelkezik, ahol gombokat kattintasz, szöveget viszel be, opciókat választasz és így tovább.

### A konzolos és UI alkalmazások korlátoltak

Hasonlítsd össze egy parancs alapú alkalmazással, ahol beírsz egy parancsot:

- **Korlátolt**. Nem írhatsz be akármit, csak azokat a parancsokat, amelyeket az alkalmazás támogat.
- **Nyelvspecifikus**. Néhány alkalmazás sok nyelvet támogat, de alapértelmezésben az alkalmazást egy adott nyelvre építik, még ha több nyelvi támogatást is hozzáadhatsz.

### A szöveggeneráló alkalmazások előnyei

Miben különbözik tehát egy szöveggeneráló alkalmazás?

Egy szöveggeneráló alkalmazásban nagyobb a rugalmasság, nem vagy korlátozva egy parancskészletre vagy egy adott bemeneti nyelvre. Ehelyett természetes nyelvet használhatsz az alkalmazással való interakcióra. Egy másik előny, hogy egy olyan adatforrással lépsz interakcióba, amelyet egy hatalmas információkorpuszra tanítottak, míg egy hagyományos alkalmazás korlátozott lehet az adatbázisban lévő tartalmakra.

### Mit építhetek egy szöveggeneráló alkalmazással?

Sokféle dolgot építhetsz. Például:

- **Csevegőbot**. Egy olyan csevegőbot, amely kérdésekre válaszol témákban, például a cégedről és termékeiről, jó választás lehet.
- **Segéd**. A nagyméretű nyelvi modellek (LLM-ek) nagyszerűek például szöveg összegzésére, szövegből való betekintések nyerésére, önéletrajzok, és más szövegek létrehozására.
- **Kódsegéd**. A használt nyelvi modelltől függően építhetsz kódsegédet, amely segít kódot írni. Például használhatod a GitHub Copilot terméket vagy a ChatGPT-t is kódírás támogatására.

## Hogyan kezdjek hozzá?

Nos, meg kell találnod a módját, hogy hogyan integrálódj egy LLM-mel, ami általában a következő két megközelítést jelenti:

- Használj API-t. Itt webes kéréseket építesz a promptoddal, és visszakapod a generált szöveget.
- Használj könyvtárat. A könyvtárak segítenek becsomagolni az API hívásokat, és egyszerűbbé teszik a használatot.

## Könyvtárak/SDK-k

Néhány jól ismert könyvtár LLM-ekkel való munka esetén:

- **openai**, ez a könyvtár megkönnyíti a modellhez való csatlakozást és a promptok elküldését.

Ezek mellett vannak magasabb szintű könyvtárak is, mint például:

- **Langchain**. A Langchain ismert és támogatja a Pythont.
- **Semantic Kernel**. A Semantic Kernel egy Microsoft által fejlesztett könyvtár, amely támogatja a C#, Python és Java nyelveket.

## Első alkalmazás az openai könyvtárral

Nézzük meg, hogyan építhetjük meg első alkalmazásunkat, milyen könyvtárakra van szükségünk, menyi minden szükséges és így tovább.

### openai telepítése

Számos könyvtár elérhető az OpenAI vagy az Azure OpenAI használatához. Több programozási nyelvet is használhatsz, például C#, Python, JavaScript, Java és még sok mást. Mi az `openai` Python könyvtárat választottuk, ezért a `pip` csomagkezelővel fogjuk telepíteni.

```bash
pip install openai
```

### Erőforrás létrehozása

A következő lépéseket kell elvégezned:

- Regisztrálj egy fiókot az Azure-on a következő címen: [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Szerezz hozzáférést az Azure OpenAI-hoz. Menj a [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) oldalra és kérelmezd a hozzáférést.

  > [!NOTE]
  > A cikk írásának időpontjában kérelmezni kell az Azure OpenAI használati hozzáférést.

- Telepítsd a Python-t <https://www.python.org/>
- Hozz létre egy Azure OpenAI szolgáltatás erőforrást. Lásd az útmutatót arról, hogyan kell [erőforrást létrehozni](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### API kulcs és végpont keresése

Ekkor meg kell adnod az `openai` könyvtáradnak, hogy melyik API kulcsot használja. Az API kulcsod megtalálásához menj az Azure OpenAI erőforrásod "Kulcsok és végpont" szekciójára, és másold ki az "1. kulcs" értékét.

![Kulcsok és végpont erőforrás panel az Azure Portálban](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Miután ezt az információt kimásoltad, adjuk utasítást a könyvtáraknak, hogy használják azt.

> [!NOTE]
> Érdemes az API kulcsot különválasztani a kódtól. Ezt megteheted környezeti változók használatával.
>
> - Állítsd be az `OPENAI_API_KEY` környezeti változót az API kulcsodra.
>   `export OPENAI_API_KEY='sk-...'`

### Azure konfiguráció beállítása

Ha Azure OpenAI-t használsz (most a Microsoft Foundry része), így állítod be a konfigurációt. Az alapértelmezett `OpenAI` kliens az Azure OpenAI `/openai/v1/` végpontjára mutat, ami a Responses API-val működik és nem igényel `api_version` megadását:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Fent a következőket állítjuk be:

- `api_key`, ez az API kulcs, amit az Azure Portálból vagy a Microsoft Foundry portálról találsz.
- `base_url`, ez a Foundry erőforrásod végpontja, aminek a végén a `/openai/v1/` szerepel. Az stabil v1 végpont az OpenAI és az Azure OpenAI esetén is működik `api_version` kezelés nélkül.

> [!NOTE] > Az `os.environ` környezeti változókat olvas be. Használhatod az `AZURE_OPENAI_API_KEY` és `AZURE_OPENAI_ENDPOINT` környezeti változók beolvasására. Állítsd be ezeket a környezeti változókat a terminálodban vagy használj hozzá például `dotenv` könyvtárat.

## Szöveg generálása

A szöveggenerálás módja a Responses API használata a `responses.create` metódussal. Íme egy példa:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # ez a modell telepítési neve
    input=prompt,
    store=False,
)
print(response.output_text)
```

A fenti kódban létrehozunk egy választ, és megadjuk a használni kívánt modellt és a promptot. Ezután a generált szöveget kiírjuk a `response.output_text` segítségével.

### Többfordulós beszélgetések

A Responses API jól használható egyfordulós szöveggeneráláshoz és többfordulós chatbotokhoz is - a `input` paraméterben üzenetlistát adsz meg a beszélgetés felépítéséhez:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

Erről a funkcionalitásról egy későbbi fejezetben lesz szó.

## Gyakorlat - az első szöveggeneráló alkalmazásod

Most, hogy megtanultuk, hogyan állítsuk be és konfiguráljuk az openai-t, itt az ideje, hogy megépítsd az első szöveggeneráló alkalmazásodat. Az alkalmazás elkészítéséhez kövesd az alábbi lépéseket:

1. Hozz létre egy virtuális környezetet és telepítsd az openai könyvtárat:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Ha Windows-t használsz, írd be a `venv\Scripts\activate` parancsot a `source venv/bin/activate` helyett.

   > [!NOTE]
   > Az Azure OpenAI kulcsodat az alábbi címen találhatod meg: [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst). Keresd meg az `Open AI` szót, válaszd az `Open AI erőforrás`-t, majd a `Kulcsok és végpont` részt, és másold ki az `1. kulcs` értékét.

1. Hozz létre egy _app.py_ fájlt, és add meg neki a következő kódot:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # add hozzá a teljesítési kódodat
   prompt = "Complete the following: Once upon a time there was a"

   # küldj egy kérést a Responses API segítségével
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # írd ki a választ
   print(response.output_text)
   ```

   > [!NOTE]
   > Ha sima OpenAI-t használsz (nem Azure-t), akkor használd ezt: `client = OpenAI(api_key="<helyettesítsd az OpenAI kulcsoddal>")` (`base_url` nélkül) és model helyett adj meg egy modellt, például `gpt-4o-mini` a deployment név helyett.

   Kimenetként valami hasonlót fogsz látni:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Különböző típusú promptok különböző feladatokra

Most már láttad, hogyan generálhatsz szöveget egy prompt segítségével. Van már egy programod, amely fut, és amelyet módosíthatsz, változtathatsz különböző típusú szövegek előállításához.

A promptokat sokféle feladatra használhatod. Például:

- **Szövegtípus generálása**. Például generálhatsz verset, kvízkérdéseket stb.
- **Információ keresése**. Promptokkal kereshetsz információkat, pl. "Mit jelent a CORS a webfejlesztésben?".
- **Kód generálása**. Promptokkal kódot is generálhatsz, például szabályos kifejezéseket e-mail címek ellenőrzésére, vagy akár egész programokat, például webalkalmazásokat.

## Egy gyakorlatiasabb eset: receptgenerátor

Képzeld el, hogy vannak alapanyagaid otthon, és főzni szeretnél valamit. Ehhez recept kell. Recept keresésére használhatsz keresőmotort, vagy használhatod az LLM-et is.

Írhatsz egy promptot így:

> "Mutass 5 receptet egy olyan ételhez, amelynek a következő alapanyagai vannak: csirke, burgonya, és sárgarépa. Receptenként sorold fel az összes használt alapanyagot."

A fenti prompt alapján a válasz hasonló lehet:

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

Ez a kimenet szuper, tudom, mit főzzek. Itt hasznos fejlesztések lehetnek:

- Szűrni azokat az alapanyagokat, amelyeket nem szeretek vagy amelyekre allergiás vagyok.
- Bevásárlólistát készíteni, arra az esetre, ha nem lenne meg mind az összetevő otthon.

Ehhez az alábbi plusz promptot adjuk hozzá:

> "Kérlek, távolítsd el a receptek közül a fokhagymásakat, mert allergiás vagyok rá, és helyettesítsd valami mással. Kérlek, készíts bevásárlólistát a receptekhez, figyelembe véve, hogy otthon már van csirkém, burgonyám és sárgarépám."

Most új eredményt kapsz, mégpedig:

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

Ez az öt recept, aminél nem szerepel a fokhagyma, és emellett van egy bevásárlólista is, figyelembe véve az otthon rendelkezésre álló alapanyagokat.

## Gyakorlat - építs receptgenerátort

Most, hogy végigvettünk egy forgatókönyvet, írjunk kódot a bemutatott forgatókönyvhez. Ehhez kövesd az alábbi lépéseket:

1. Használd az eddigi _app.py_ fájlt kiindulási pontként
1. Keresd meg a `prompt` változót és változtasd meg a kódját a következőre:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Ha most lefuttatod a kódot, hasonló kimenetet fogsz látni:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > MEGJEGYZÉS, az LLM nem determinisztikus, így minden futtatásnál más-más eredményt kaphatsz.

   Nagyszerű, nézzük, hogyan fejleszthetjük tovább. A kódot rugalmasabbá akarjuk tenni, hogy az alapanyagok és a receptek száma egyszerűen változtatható legyen.

1. A kódot módosítsuk az alábbiak szerint:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # a receptek számát interpolálja a bemenetbe és az összetevőkbe
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Egy tesztfutásban így nézhet ki a kód:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Fejlesztés szűrő és bevásárlólista hozzáadásával

Most már van egy működő alkalmazásunk, ami képes recepteket előállítani, és rugalmas, mert a felhasználó bemenetein alapul, mind a receptek számát, mind az alapanyagokat illetően.

További fejlesztésként a következőket akarjuk hozzáadni:

- **Alapanyagok szűrése**. Szeretnénk tudni szűrni azokat az alapanyagokat, amelyeket nem szeretünk vagy amelyekre allergiásak vagyunk. Ehhez a változtatáshoz szerkesszük az eddigi promptunkat és adjunk hozzá egy szűrési feltételt a prompt végéhez így:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Fent a prompt végéhez adjuk a `{filter}` változót, és a szűrési feltételt is begyűjtjük a felhasználótól.

  Egy példa a program futására most így nézhet ki:

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

  Mint látod, azok a receptek, amelyek tejterméket tartalmaznak, most ki lettek szűrve. De ha laktózérzékeny vagy, akkor lehet, hogy a sajtot tartalmazó recepteket is ki szeretnéd szűrni, ezért fontos hogy világos legyen a feltétel.


- **Készíts bevásárlólistát**. Szeretnénk készíteni egy bevásárlólistát, figyelembe véve, mi van már otthon.

  Ehhez a funkcióhoz megpróbálhatjuk egyszerre megoldani az egészet egy prompttal, vagy két részre bonthatjuk, és a második promptba hozzáadjuk az első prompt eredményét kontextusként. Próbáljuk meg az utóbbi megközelítést.

  Keressük meg a kódban azt a részt, ahol az első prompt eredményét kiírja, és alatta adjuk hozzá a következő kódot:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # válasz nyomtatása
  print("Shopping list:")
  print(response.output_text)
  ```

  Vegyük figyelembe a következőket:

  1. Új promptot állítunk össze az első prompt eredményének hozzáadásával:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Új kérést teszünk, figyelembe véve az első promptnál megadott tokenmennyiséget, ezért most `max_output_tokens` értéke 1200 lesz.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Ezt a kódot lefuttatva, a következő kimenetet kapjuk:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Fejleszd tovább a beállításod

Ami eddig van, az működő kód, de van néhány finomhangolás, amit meg kell tennünk a további javítás érdekében. Néhány teendő:

- **Válaszd szét a titkokat és a kódot**, mint például az API kulcsot. A titkok nem tartoznak a kódba, és biztonságos helyen kell tárolni őket. A titkok szétválasztásához használhatunk környezeti változókat és olyan könyvtárakat, mint a `python-dotenv`, hogy fájlból töltsük be őket. Így nézne ki a kód:

  1. Hozz létre egy `.env` fájlt a következő tartalommal:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Megjegyzés: Azure OpenAI használatakor Microsoft Foundry-ban a következő környezeti változókat kell beállítani helyette:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Kódban a környezeti változókat így töltenéd be:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Szó a token hosszáról**. Fontoljuk meg, hány tokenre van szükségünk a kívánt szöveg generálásához. A tokenek költséggel járnak, ezért ahol lehet, spóroljunk a tokenek számával. Például, megfogalmazhatjuk úgy a promptot, hogy kevesebb token szükséges?

  A használt tokenek számát a `max_output_tokens` paraméterrel változtathatjuk. Például, ha 100 tokent akarunk használni, így kell tennünk:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Kísérletezés a hőmérséklettel**. A hőmérséklet olyan paraméter, amit eddig nem említettünk, de fontos szerepe van a program viselkedésében. Minél magasabb a hőmérséklet értéke, annál véletlenszerűbb lesz a kimenet. Ezzel szemben minél alacsonyabb az érték, annál kiszámíthatóbb a kimenet. Döntsd el, hogy változatosságot akarsz-e az eredményben, vagy sem.

  A hőmérséklet módosításához használd a `temperature` paramétert. Például, ha 0.5-ös hőmérsékletet akarsz, így állítsd be:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Megjegyzés: minél közelebb van az érték 1.0-hoz, annál változatosabb lesz a kimenet.

## Feladat

Ehhez a feladathoz te döntheted el, mit szeretnél megvalósítani.

Íme néhány javaslat:

- Finomíts tovább a receptgeneráló alkalmazást. Próbálj ki különböző hőmérsékleti értékeket és promptokat, hogy meglásd, milyen eredményt érhetsz el.
- Készíts egy "tanulótársat". Ez az app képes legyen kérdésekre válaszolni egy témáról, például Pythont illetően; lehetnek promptok, mint "Mi a(z) X a Pythonban?", vagy kérheted, hogy mutasson példakódot egy adott témához.
- Történelmi bot, keltsd életre a történelmet, utasítsd a botot, hogy játsszon egy adott történelmi személyt, és kérdezd őt az életéről és koráról.

## Megoldás

### Tanulótárs

Az alábbi prompt egy induló pont, nézd meg, hogyan használhatod és alakíthatod a saját ízlésed szerint.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Történelmi bot

Íme néhány prompt, amiket használhatsz:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Tudásellenőrzés

Mit csinál a hőmérséklet fogalma?

1. Az irányítja, mennyire véletlenszerű a kimenet.
1. Az irányítja, mekkora a válasz mérete.
1. Az irányítja, mennyi token kerül felhasználásra.

## 🚀 Kihívás

A feladaton dolgozva próbáld ki a hőmérséklet változtatását: állítsd 0-ra, 0.5-re és 1-re. Ne feledd, 0 a legkevésbé változatos, 1 a leginkább. Melyik érték a legjobb a te alkalmazásodhoz?

## Nagyszerű munka! Folytasd a tanulást

A lecke befejezése után nézd meg a [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) gyűjteményünket, hogy tovább fejleszd generatív MI tudásodat!

Indulj neki a 7. leckének, ahol a [chat alkalmazások építésének](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) módját nézzük majd meg!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->