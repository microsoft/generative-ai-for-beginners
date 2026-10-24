# Szöveg generáló alkalmazások építése

[![Szöveg generáló alkalmazások építése](../../../translated_images/hu/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Kattintson a fenti képre a lecke videójának megtekintéséhez)_

Eddig a tananyag során láttad, hogy léteznek alapvető fogalmak, mint a promptok, és akár egy egész tudományág is van, amit "prompt mérnökségnek" hívnak. Sok eszköz, amellyel interakcióba léphetsz, mint a ChatGPT, Office 365, Microsoft Power Platform és mások, támogatja a promptok használatát valami elérésére.

Ahhoz, hogy ilyen élményt adhass egy alkalmazáshoz, értened kell olyan fogalmakat, mint a promptok, befejezések, és ki kell választanod egy könyvtárat, amivel dolgozhatsz. Pontosan ezt tanulod meg ebben a fejezetben.

## Bevezetés

Ebben a fejezetben:

- Megismerkedsz az openai könyvtárral és annak alapfogalmaival.
- Készítesz egy szöveg generáló alkalmazást az openai használatával.
- Megérted, hogyan használhatók olyan fogalmak, mint a prompt, hőmérséklet és tokenek egy szöveg generáló alkalmazás építéséhez.

## Tanulási célok

A lecke végére képes leszel:

- Elmagyarázni, mi az a szöveg generáló alkalmazás.
- Egy szöveg generáló alkalmazás építésére az openai használatával.
- Az alkalmazásod beállítására, hogy több vagy kevesebb token használatával és a hőmérséklet módosításával változatos kimenetet generáljon.

## Mi az a szöveg generáló alkalmazás?

Normálisan, amikor egy alkalmazást építesz, valamilyen felhasználói felülettel rendelkezik, ilyen például:

- Parancs alapú. A konzolos alkalmazások tipikus példái annak, amikor beírsz egy parancsot és az elvégzi a feladatot. Például az `git` egy parancs alapú alkalmazás.
- Felhasználói felület (UI). Egyes alkalmazások grafikus felhasználói felülettel (GUI) rendelkeznek, ahol gombokra kattintasz, beírsz szöveget, opciókat választasz, és így tovább.

### A konzolos és UI alkalmazások korlátozottak

Hasonlítsd össze egy parancs alapú alkalmazással, ahol beírsz egy parancsot:

- **Korlátozott**. Nem írhatod be bármelyik parancsot, csak azokat, amelyeket az alkalmazás támogat.
- **Nyelvspecifikus**. Egyes alkalmazások több nyelvet támogatnak, de alapértelmezésben az alkalmazás egy adott nyelvre épül, még ha több nyelvi támogatást hozzá is adhatsz.

### A szöveg generáló alkalmazások előnyei

Miben más egy szöveg generáló alkalmazás?

Egy szöveg generáló alkalmazásban nagyobb a rugalmasság, nem vagy korlátozva parancsok halmazára vagy egy adott bemeneti nyelvre. Ehelyett természetes nyelvet használhatsz az alkalmazással való interakcióhoz. Egy másik előnye, hogy már egy hatalmas adathalmazon tanult adatforrással lépsz kapcsolatba, míg egy hagyományos alkalmazás korlátozva lehet az adatbázis tartalmára.

### Mit lehet építeni egy szöveg generáló alkalmazással?

Sok mindent lehet építeni, például:

- **Csevegőrobot**. Egy chatbot, amely kérdésekre válaszol különféle témákról, például a cégedről és termékeiről, jó választás lehet.
- **Segítő**. A nagyméretű nyelvi modellek (LLM) kiválóak szöveg összefoglalására, szövegből nyert betekintésekre, szövegek (például önéletrajzok) generálására és így tovább.
- **Kódsegítő**. A használt nyelvi modelltől függően egy kódsegítőt is építhetsz, amely segít kódot írni. Például használhatsz olyan termékeket, mint a GitHub Copilot vagy a ChatGPT, hogy segítsenek a kódírásban.

## Hogyan kezdjek hozzá?

Általában két megközelítés van egy LLM-mel való integrációhoz:

- Használj API-t. Itt web-kéréseket építesz fel a promptoddal, és visszakapod a generált szöveget.
- Használj könyvtárat. A könyvtárak az API hívásokat csomagolják és egyszerűbbé teszik a használatot.

## Könyvtárak/SDK-k

Néhány ismert könyvtár az LLM-ek használatához:

- **openai**, ez a könyvtár megkönnyíti a modellhez való csatlakozást és a promptok küldését.

Ezen felül léteznek magasabb szintű könyvtárak, mint például:

- **Langchain**. A Langchain ismert, és támogatja a Pythont.
- **Semantic Kernel**. A Semantic Kernel egy Microsoft által fejlesztett könyvtár, amely támogatja a C#, Python és Java nyelveket.

## Első alkalmazás openai használatával

Nézzük, hogyan építhetjük meg első alkalmazásunkat, milyen könyvtárakra van szükség, mennyi erőforrást igényel és így tovább.

### openai telepítése

Sok könyvtár létezik az OpenAI vagy Azure OpenAI-val való interakcióhoz. Több programozási nyelvet is használhatsz, például C#, Python, JavaScript, Java és mások. Mi az `openai` Python könyvtárat választottuk, így azt `pip` segítségével telepítjük.

```bash
pip install openai
```

### Erőforrás létrehozása

Végezd el a következő lépéseket:

- Hozz létre egy fiókot az Azure-on [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)].
- Szerezz hozzáférést az Azure OpenAI-hoz. Látogass el a [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) oldalra és kérj hozzáférést.

  > [!NOTE]
  > A cikk írásakor szükséges hozzáférést kérni az Azure OpenAI-hoz.

- Telepítsd a Pythont <https://www.python.org/>
- Hozz létre egy Azure OpenAI szolgáltatás erőforrást. Erről részletes útmutató van, hogyan kell [erőforrást létrehozni](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### API kulcs és végpont megtalálása

Itt meg kell adnod az `openai` könyvtárnak, melyik API kulcsot használja. Az API kulcs megtalálásához nyisd meg az Azure OpenAI erőforrásod "Kulcsok és végpontok" szekcióját és másold a "Kulcs 1" értéket.

![Kulcsok és végpont erőforrás nézet az Azure Portalon](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Most, hogy megvan az információ, utasítsuk a könyvtárakat a használatára.

> [!NOTE]
> Érdemes az API kulcsodat elkülöníteni a kódtól. Ezt megteheted környezeti változók használatával.
>
> - Állítsd be a környezeti változót `OPENAI_API_KEY` értékére az API kulcsodat.
>   `export OPENAI_API_KEY='sk-...'`

### Azure konfiguráció beállítása

Ha Azure OpenAI-t használsz (most már a Microsoft Foundry része), így állíthatod be a konfigurációt. A szabványos `OpenAI` klienssel dolgozunk, ami az Azure OpenAI `/openai/v1/` végpontjára mutat, amely kompatibilis a Responses API-val, és nem igényel `api_version` használatát:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Fent a következőket állítjuk be:

- `api_key`, ez az Azure Portalon vagy Microsoft Foundry portálon megtalálható API kulcs.
- `base_url`, ez a Foundry erőforrás végpontja, amelyhez hozzá van fűzve `/openai/v1/`. A stabil v1 végpont működik OpenAI és Azure OpenAI esetén is, `api_version` menedzsment nélkül.

> [!NOTE] > `os.environ` olvassa a környezeti változókat. Használhatod az `AZURE_OPENAI_API_KEY` vagy `AZURE_OPENAI_ENDPOINT` környezeti változók olvasására. Állítsd be ezeket a terminálodban vagy használj egy könyvtárat, például `dotenv`.

## Szöveg generálása

A szöveg generálásának módja a Responses API használata a `responses.create` metódussal. Íme egy példa:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

A fenti kódban létrehozunk egy választ, megadjuk a használni kívánt modellt és a promptot. Ezután kiírjuk a generált szöveget a `response.output_text` használatával.

### Többszörös beszélgetések

A Responses API jól használható egy egyszeres szöveggeneráláshoz és többszörös körös chatbotokhoz is - egy üzenetlistát adsz meg a `input` segítségével, amely egy beszélgetést épít fel:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Erről a funkcióról egy későbbi fejezetben bővebben.

## Gyakorlat - az első szöveg generáló alkalmazásod

Most, hogy megtanultuk hogyan állítsuk be és konfiguráljuk az openai-t, ideje elkészíteni az első szöveg generáló alkalmazásod. Ehhez kövesd az alábbi lépéseket:

1. Hozz létre egy virtuális környezetet és telepítsd az openai-t:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Windows rendszeren `venv\Scripts\activate`-t írj a `source venv/bin/activate` helyett.

   > [!NOTE]
   > Azure OpenAI kulcsod megtalálásához látogass el ide: [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst)], keresd meg az `Open AI`-t, válaszd ki az `Open AI resource`-t, majd válaszd az `Keys and Endpoint`-t és másold ki az `Key 1` értékét.

1. Hozz létre egy _app.py_ fájlt az alábbi kóddal:

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
   > Ha sima OpenAI-t használsz (nem Azure), használd a `client = OpenAI(api_key="<replace this value with your OpenAI key>")`-t (nem `base_url`), és add meg a modell nevét, például `gpt-5-mini`-t a telepítés neve helyett.

   Ilyen kimenetet kell látnod:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Különböző prompt típusok, különböző feladatokra

Most már láttad, hogyan generálhatsz szöveget egy prompt segítségével. Van egy futó programod is, amit módosíthatsz, hogy különböző típusú szöveget állítson elő.

A promptokat mindenféle feladatra használhatod, például:

- **Szöveg típus generálása**. Például generálhatsz egy verset, kérdéseket egy kvízhez stb.
- **Információ lekérése**. Promptokat használhatsz információ keresésére, pl. 'Mit jelent a CORS a webfejlesztésben?'.
- **Kód generálás**. Promptokat használhatsz kód generálására, például egy reguláris kifejezés írására, amivel e-maileket ellenőriznek, vagy akár egy teljes program, például webes alkalmazás írására.

## Egy praktikus példa: recept generátor

Képzeld el, hogy otthon vannak alapanyagok, és valamit főzni szeretnél. Ehhez kell egy recept. Egy módja a receptek keresésének, ha használod a keresőmotort, de használhatsz egy LLM-et is.

Írhatsz egy ilyen promptot:

> "Mutass nekem 5 receptet egy ételhez, amely a következő hozzávalókat tartalmazza: csirke, burgonya és sárgarépa. Receptenként sorold fel az összes használt hozzávalót."

A fenti prompt alapján egy válasz hasonló lehet:

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

Ez remek, tudom, mit főzzek. Itt hasznos fejlesztések lehetnének például:

- Szűrni azokat az alapanyagokat, amiket nem szeretek vagy allergiás vagyok rájuk.
- Bevásárlólista készítése, ha nincs meg otthon minden hozzávaló.

Ezekhez adjunk egy további promptot:

> "Kérlek, távolítsd el a receptek közül a fokhagymásakat, mert allergiás vagyok rá, és cseréld ki valami másra. Emellett kérlek, készíts bevásárlólistát a receptekhez, figyelembe véve, hogy már van otthon csirke, burgonya és sárgarépa."

Most új eredményt kapsz, nevezetesen:

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

Ezek a te öt recepted, amelyben nincs fokhagyma, és van bevásárlólista, figyelembe véve, mi van már otthon.

## Gyakorlat - recept generátor építése

Miután lejátszottuk a szcenáriót, írjunk le kódot a bemutatott esethez. Ehhez kövesd a következő lépéseket:

1. Használd az existing _app.py_ fájlt kiindulópontként.
1. Keresd meg az `prompt` változót és cseréld a kódját a következőre:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Ha most futtatod a kódot, ilyesmi kimenetet kell látnod:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > MEGJEGYZÉS: az LLM-ed nem determinisztikus, így változó eredményeket kaphatsz futtatásról futtatásra.

   Nagyszerű, nézzük, hogyan lehet javítani a dolgon. Ahhoz, hogy rugalmasabb legyen, azt szeretnénk, hogy a hozzávalókat és a receptek számát könnyű legyen módosítani.

1. Így változtassuk a kódot:

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

Most már van egy működő alkalmazásunk, ami képes receptek előállítására, és rugalmas, mert a felhasználótól függ, hány recept legyen és milyen hozzávalókkal.

Az alábbiak hozzáadásával tovább javíthatjuk:

- **Szűrje ki az összetevőket**. Ki akarjuk szűrni azokat az alapanyagokat, amiket nem szeretünk vagy allergiásak vagyunk rájuk. Ehhez módosítsuk a meglévő promptunkat azzal, hogy a végére hozzáadunk egy szűrőfeltételt, így:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Fent hozzáadtuk a `{filter}`-t a prompt végéhez, és a felhasználótól kapjuk a szűrő értékét is.

  Egy példa bemenet a program futtatására így nézhet ki:

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

  Látható, hogy a tejjel készült receptek ki vannak szűrve. De ha laktózérzékeny vagy, talán a sajtos recepteket is ki szeretnéd szűrni, így egyértelműnek kell lenni.

- **Bevásárlólista készítése**. Szeretnénk egy bevásárlólistát készíteni, figyelembe véve, hogy mi van már otthon.

  Ehhez a funkcióhoz mindent egy promptban is megpróbálhatunk megoldani, vagy kettéválaszthatjuk két promptra. Próbáljuk meg az utóbbit. Ehhez javasoljuk egy további prompt hozzáadását, de ahhoz, hogy ez működjön, az első prompt eredményét kontextusként hozzá kell adnunk a második prompthoz.

  Keresd meg a kódban azt a részt, ahol az első prompt eredményét kiíratod, és add hozzá az alábbi kódot alulra:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Figyeld meg a következőket:

  1. Új promptot szerkesztünk azzal, hogy az első prompt eredményét hozzáfűzzük az új prompthoz:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Új kérést teszünk, figyelembe véve az első promptban kért tokenek számát, így itt az `max_output_tokens` értéke 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Ezzel a kóddal futtatva az alábbi kimenetet kapjuk:

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

Amit eddig látunk, az működő kód, de vannak apróbb módosítások, amiket meg kellene tennünk a további fejlesztés érdekében. Néhány dolog, amit meg kellene tennünk:

- **Titkok különválasztása a kódtól**, például az API kulcs esetében. A titkok nem tartoznak a kódba, és biztonságos helyen kell tárolni őket. A titkok és a kód elkülönítéséhez környezeti változókat és olyan könyvtárakat használhatunk, mint a `python-dotenv`, hogy fájlból töltse be őket. Így nézne ki ez a kódban:

  1. Készíts egy `.env` fájlt a következő tartalommal:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Megjegyzés, az Azure OpenAI Microsoft Foundry-ban az alábbi környezeti változókat kell beállítani helyette:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     A kódban így töltenéd be a környezeti változókat:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Egy szó a token hosszáról**. Fontolóra kell vennünk, hány tokenre van szükség a kívánt szöveg generálásához. A tokenek pénzbe kerülnek, ezért ahol lehet, takarékosnak kell lennünk a tokenek számával. Például, megfogalmazhatjuk-e a promptot úgy, hogy kevesebb token legyen szükséges?

  A használt tokenek számának módosításához használhatod a `max_output_tokens` paramétert. Például, ha 100 tokent akarsz használni, így tennéd:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Kísérletezés a hőmérséklettel (temperature)**. A hőmérséklet egy olyan paraméter, amit eddig nem említettünk, de fontos tényező a program teljesítményében. Minél magasabb a hőmérséklet értéke, annál véletlenszerűbb lesz a kimenet. Fordítva, minél alacsonyabb a hőmérséklet értéke, annál kiszámíthatóbb lesz a kimenet. Gondold át, szeretnél-e változatosságot a kimenetben vagy sem.

  A hőmérséklet megváltoztatásához használhatod a `temperature` paramétert. Például, ha 0.5-ös hőmérsékletet szeretnél, így tennéd:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Megjegyzés, minél közelebb van az érték 1.0-hoz, annál változatosabb a kimenet.

- **Az érvelő modellek nem használják a `temperature`-t**. Ez egy fontos 2026-os váltás. A Microsoft Foundry jelenlegi, nem elavult modelljei **érvelő modellek** (a GPT-5 család, o-széria) - és **nem támogatják a `temperature` vagy `top_p`-t** (sem a `max_tokens`-t; használj inkább `max_output_tokens`-t). Ha `temperature`-t küldesz `gpt-5-mini`-nak, "paraméter nem támogatott" hibát kapsz. Tehát a fent említett hőmérséklet példát próbáld meg olyan modellen, ami még támogatja a mintavételezési vezérlőket - például egy nyílt **Llama** modellt, mint a `Llama-3.3-70B-Instruct` a [Microsoft Foundry modell katalógusból](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), amit a Foundry Models / Azure AI Inference végponton keresztül hívtak (ugyanúgy, mint a `githubmodels-*` példák esetében). Az olyan érvelő modellekhez, mint a GPT-5, a kimenetet más módon irányítjuk:
  - **Prompt tervezés** - világos utasítások, példák és strukturált kimenet (lásd a [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst) leckét) végzik azt a munkát, amit korábban a mintavételezési beállítások.
  - **Érvelési vezérlők** - olyan paraméterek, mint az érvelési erőfeszítés/verőzsiósság, amelyek az érvelés mélységét a késleltetés és költség ellenében szabályozzák.

  Röviden: a `temperature`/`top_p` még sok modellen érvényes (Llama, Mistral, Phi, és a GPT-4.x család - bár a GPT-4.x kikopóban van), de az irányvonal a prompt tervezés + érvelési vezérlők az érvelő modellek, például a GPT-5 esetében.

## Feladat

Ehhez a feladathoz bármit építhetsz, amit szeretnél.

Íme néhány javaslat:

- Az ételrecept generátor alkalmazást finomhangold tovább. Kísérletezz a hőmérséklet értékekkel és a promptokkal, hogy kiderítsd, mit tudsz elérni.
- Készíts "tanulótársat". Ez az alkalmazás képes legyen válaszolni egy témával kapcsolatos kérdésekre, például Python esetén lehetnek olyan promptok, hogy "Mi az a bizonyos téma Pythonban?", vagy hogy mutasson kódot egy adott témához stb.
- Történelmi bot, éleszd fel a történelmet, utasítsd a botot, hogy játsszon egy bizonyos történelmi figurát, és kérdezd meg az életéről, koráról.

## Megoldás

### Tanulótárs

Lent található egy kezdő prompt, nézd meg, hogyan tudod használni és tetszés szerint módosítani.

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

## Tudásfelmérés

Mit csinál a temperature (hőmérséklet) fogalom?

1. Szabályozza, mennyire véletlenszerű a kimenet.
1. Szabályozza, milyen nagy a válasz.
1. Szabályozza, hány token használódik fel.

## 🚀 Kihívás

A feladat során próbáld meg változtatni a hőmérsékletet, állítsd 0-ra, 0.5-re, és 1-re. Ne feledd, 0 a legkevésbé változatos, 1 pedig a legváltozatosabb. Melyik érték működik legjobban az alkalmazásodban?

## Szép munka! Folytasd a tanulást

A lecke befejezése után nézd meg a [Generatív AI tanulási gyűjteményünket](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), hogy tovább fejleszd a Generatív AI ismereteidet!

Lépj tovább a 7. leckére, ahol megnézzük, hogyan lehet [chat alkalmazásokat építeni](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->