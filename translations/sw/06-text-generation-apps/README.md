<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df027997f1448323d6159b78a1b669bf",
  "translation_date": "2025-10-17T21:08:56+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "sw"
}
-->
# Kujenga Programu za Uzalishaji wa Maandishi

[![Kujenga Programu za Uzalishaji wa Maandishi](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.sw.png)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Bofya picha hapo juu kutazama video ya somo hili)_

Umeona hadi sasa kupitia mtaala huu kwamba kuna dhana za msingi kama maelekezo na hata taaluma nzima inayoitwa "uhandisi wa maelekezo". Zana nyingi unazoweza kuingiliana nazo kama ChatGPT, Office 365, Microsoft Power Platform na zaidi, zinakuwezesha kutumia maelekezo kufanikisha jambo fulani.

Ili kuongeza uzoefu kama huo kwenye programu, unahitaji kuelewa dhana kama maelekezo, kukamilisha na kuchagua maktaba ya kufanya kazi nayo. Hicho ndicho hasa utakachojifunza katika sura hii.

## Utangulizi

Katika sura hii, utajifunza:

- Kuhusu maktaba ya openai na dhana zake za msingi.
- Kujenga programu ya uzalishaji wa maandishi kwa kutumia openai.
- Kuelewa jinsi ya kutumia dhana kama maelekezo, joto, na tokeni kujenga programu ya uzalishaji wa maandishi.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- Kuelezea programu ya uzalishaji wa maandishi ni nini.
- Kujenga programu ya uzalishaji wa maandishi kwa kutumia openai.
- Kuseti programu yako kutumia tokeni zaidi au kidogo na pia kubadilisha joto, kwa matokeo tofauti.

## Programu ya Uzalishaji wa Maandishi ni nini?

Kwa kawaida unapoandika programu ina aina fulani ya kiolesura kama ifuatavyo:

- Inayotegemea amri. Programu za console ni programu za kawaida ambapo unaandika amri na inatekeleza kazi fulani. Kwa mfano, `git` ni programu inayotegemea amri.
- Kiolesura cha mtumiaji (UI). Baadhi ya programu zina kiolesura cha picha (GUIs) ambapo unabonyeza vitufe, unaingiza maandishi, unachagua chaguo na zaidi.

### Programu za Console na UI zina mipaka

Linganisheni na programu inayotegemea amri ambapo unaandika amri:

- **Ina mipaka**. Huwezi tu kuandika amri yoyote, ni zile tu ambazo programu inasaidia.
- **Lugha maalum**. Baadhi ya programu zinaunga mkono lugha nyingi, lakini kwa kawaida programu imejengwa kwa lugha maalum, hata kama unaweza kuongeza msaada wa lugha zaidi.

### Faida za Programu za Uzalishaji wa Maandishi

Kwa hivyo programu ya uzalishaji wa maandishi ni tofauti vipi?

Katika programu ya uzalishaji wa maandishi, una uhuru zaidi, hauko na mipaka ya seti ya amri au lugha maalum ya kuingiza. Badala yake, unaweza kutumia lugha ya kawaida kuingiliana na programu. Faida nyingine ni kwamba tayari unashirikiana na chanzo cha data ambacho kimefundishwa kwenye mkusanyiko mkubwa wa taarifa, wakati programu ya kawaida inaweza kuwa na mipaka kwa kile kilicho kwenye hifadhidata.

### Unaweza Kujenga Nini na Programu ya Uzalishaji wa Maandishi?

Kuna mambo mengi unayoweza kujenga. Kwa mfano:

- **Chatbot**. Chatbot inayojibu maswali kuhusu mada, kama kampuni yako na bidhaa zake inaweza kuwa chaguo nzuri.
- **Msaidizi**. LLMs ni nzuri katika mambo kama muhtasari wa maandishi, kupata maarifa kutoka kwa maandishi, kuzalisha maandishi kama wasifu na zaidi.
- **Msaidizi wa kuandika kodikodi**. Kutegemea na mfano wa lugha unayotumia, unaweza kujenga msaidizi wa kodikodi anayekusaidia kuandika kodikodi. Kwa mfano, unaweza kutumia bidhaa kama GitHub Copilot pamoja na ChatGPT kukusaidia kuandika kodikodi.

## Ninawezaje Kuanza?

Naam, unahitaji kupata njia ya kuunganisha na LLM ambayo kwa kawaida inajumuisha njia mbili:

- Tumia API. Hapa unaunda maombi ya wavuti na maelekezo yako na kupata maandishi yaliyotengenezwa.
- Tumia maktaba. Maktaba husaidia kufupisha maombi ya API na kuyafanya rahisi kutumia.

## Maktaba/SDKs

Kuna maktaba chache zinazojulikana za kufanya kazi na LLMs kama:

- **openai**, maktaba hii inafanya iwe rahisi kuunganishwa na mfano wako na kutuma maelekezo.

Kisha kuna maktaba zinazofanya kazi kwa kiwango cha juu zaidi kama:

- **Langchain**. Langchain inajulikana sana na inaunga mkono Python.
- **Semantic Kernel**. Semantic Kernel ni maktaba ya Microsoft inayounga mkono lugha za C#, Python, na Java.

## Programu ya Kwanza kwa Kutumia openai

Hebu tuone jinsi tunavyoweza kujenga programu yetu ya kwanza, ni maktaba gani tunazohitaji, ni kiasi gani kinachohitajika na kadhalika.

### Sakinisha openai

Kuna maktaba nyingi huko nje za kuingiliana na OpenAI au Azure OpenAI. Inawezekana kutumia lugha nyingi za programu pia kama C#, Python, JavaScript, Java na zaidi. Tumechagua kutumia maktaba ya Python `openai`, kwa hivyo tutatumia `pip` kuisakinisha.

```bash
pip install openai
```

### Unda rasilimali

Unahitaji kufanya hatua zifuatazo:

- Unda akaunti kwenye Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Pata ufikiaji wa Azure OpenAI. Nenda [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) na omba ufikiaji.

  > [!NOTE]
  > Kwa wakati wa kuandika, unahitaji kuomba ufikiaji wa Azure OpenAI.

- Sakinisha Python <https://www.python.org/>
- Kuwa umeunda rasilimali ya Huduma ya Azure OpenAI. Tazama mwongozo huu wa jinsi ya [kuunda rasilimali](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Pata funguo za API na endpoint

Kwa wakati huu, unahitaji kuambia maktaba yako ya `openai` ni funguo gani ya API ya kutumia. Ili kupata funguo yako ya API, nenda kwenye sehemu ya "Keys and Endpoint" ya rasilimali yako ya Azure OpenAI na nakili thamani ya "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Sasa kwa kuwa una taarifa hii, hebu tuwaelekeze maktaba kuitumia.

> [!NOTE]
> Inafaa kutenganisha funguo yako ya API na kodikodi yako. Unaweza kufanya hivyo kwa kutumia vigezo vya mazingira.
>
> - Weka kigezo cha mazingira `OPENAI_API_KEY` kwa funguo yako ya API.
>   `export OPENAI_API_KEY='sk-...'`

### Usanidi wa Azure

Ikiwa unatumia Azure OpenAI, hivi ndivyo unavyoseti usanidi:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Hapo juu tunaseti yafuatayo:

- `api_type` kuwa `azure`. Hii inaambia maktaba kutumia Azure OpenAI na si OpenAI.
- `api_key`, hii ni funguo yako ya API inayopatikana kwenye Azure Portal.
- `api_version`, hii ni toleo la API unalotaka kutumia. Kwa wakati wa kuandika, toleo la hivi karibuni ni `2023-05-15`.
- `api_base`, hii ni endpoint ya API. Unaweza kuipata kwenye Azure Portal karibu na funguo yako ya API.

> [!NOTE] > `os.getenv` ni kazi inayosoma vigezo vya mazingira. Unaweza kuitumia kusoma vigezo vya mazingira kama `OPENAI_API_KEY` na `API_BASE`. Weka vigezo hivi vya mazingira kwenye terminal yako au kwa kutumia maktaba kama `dotenv`.

## Kuzalisha Maandishi

Njia ya kuzalisha maandishi ni kutumia darasa la `Completion`. Hapa kuna mfano:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

Katika kodikodi hapo juu, tunaunda kitu cha kukamilisha na kupitisha mfano tunaotaka kutumia na maelekezo. Kisha tunachapisha maandishi yaliyotengenezwa.

### Kukamilisha Mazungumzo

Hadi sasa, umeona jinsi tunavyotumia `Completion` kuzalisha maandishi. Lakini kuna darasa lingine linaloitwa `ChatCompletion` ambalo linafaa zaidi kwa chatbots. Hapa kuna mfano wa jinsi ya kuitumia:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Zaidi kuhusu utendaji huu katika sura inayokuja.

## Zoezi - Programu yako ya kwanza ya uzalishaji wa maandishi

Sasa kwa kuwa tumejifunza jinsi ya kusanidi na kusanidi openai, ni wakati wa kujenga programu yako ya kwanza ya uzalishaji wa maandishi. Ili kujenga programu yako, fuata hatua hizi:

1. Unda mazingira ya kawaida na usakinishe openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Ikiwa unatumia Windows andika `venv\Scripts\activate` badala ya `source venv/bin/activate`.

   > [!NOTE]
   > Pata funguo yako ya Azure OpenAI kwa kwenda [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) na tafuta `Open AI` kisha chagua `Open AI resource` na kisha chagua `Keys and Endpoint` na nakili thamani ya `Key 1`.

1. Unda faili _app.py_ na uweke kodikodi ifuatayo:

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
   > Ikiwa unatumia Azure OpenAI, unahitaji kuseti `api_type` kuwa `azure` na kuseti `api_key` kwa funguo yako ya Azure OpenAI.

   Unapaswa kuona matokeo kama yafuatayo:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Aina tofauti za maelekezo, kwa mambo tofauti

Sasa umeona jinsi ya kuzalisha maandishi kwa kutumia maelekezo. Hata una programu inayofanya kazi ambayo unaweza kuibadilisha na kubadilisha ili kuzalisha aina tofauti za maandishi.

Maelekezo yanaweza kutumika kwa kazi za kila aina. Kwa mfano:

- **Kuzalisha aina ya maandishi**. Kwa mfano, unaweza kuzalisha shairi, maswali ya mtihani n.k.
- **Kutafuta taarifa**. Unaweza kutumia maelekezo kutafuta taarifa kama mfano huu 'CORS inamaanisha nini katika maendeleo ya wavuti?'.
- **Kuzalisha kodikodi**. Unaweza kutumia maelekezo kuzalisha kodikodi, kwa mfano kuunda usemi wa kawaida unaotumika kuthibitisha barua pepe au kwa nini usizalishe programu nzima, kama programu ya wavuti?

## Matumizi ya vitendo zaidi: jenereta ya mapishi

Fikiria una viungo nyumbani na unataka kupika kitu. Kwa hilo, unahitaji mapishi. Njia ya kupata mapishi ni kutumia injini ya utafutaji au unaweza kutumia LLM kufanya hivyo.

Unaweza kuandika maelekezo kama hivi:

> "Nionyeshe mapishi 5 ya sahani yenye viungo vifuatavyo: kuku, viazi, na karoti. Kwa kila mapishi, orodhesha viungo vyote vinavyotumika"

Kwa maelekezo hapo juu, unaweza kupata jibu linalofanana na:

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

Matokeo haya ni mazuri, najua nini cha kupika. Kwa wakati huu, maboresho yanayoweza kuwa muhimu ni:

- Kuchuja viungo ambavyo sipendi au nina mzio navyo.
- Kutengeneza orodha ya ununuzi, iwapo sina viungo vyote nyumbani.

Kwa kesi zilizo hapo juu, hebu tuongeze maelekezo ya ziada:

> "Tafadhali ondoa mapishi yenye vitunguu saumu kwani nina mzio na badilisha na kitu kingine. Pia, tafadhali tengeneza orodha ya ununuzi kwa mapishi, ukizingatia tayari nina kuku, viazi na karoti nyumbani."

Sasa una matokeo mapya, yaani:

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

Hayo ni mapishi yako matano, bila kutaja vitunguu saumu na pia una orodha ya ununuzi ukizingatia kile ulichonacho nyumbani.

## Zoezi - kujenga jenereta ya mapishi

Sasa kwa kuwa tumeshughulikia hali fulani, hebu tuandike kodikodi inayolingana na hali iliyoonyeshwa. Ili kufanya hivyo, fuata hatua hizi:

1. Tumia faili _app.py_ iliyopo kama sehemu ya kuanzia
1. Tafuta kigezo cha `prompt` na badilisha kodikodi yake kuwa ifuatayo:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Ikiwa sasa utaendesha kodikodi, unapaswa kuona matokeo yanayofanana na:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, LLM yako haina uhakika wa matokeo, kwa hivyo unaweza kupata matokeo tofauti kila wakati unapendesha programu.

   Nzuri, hebu tuone jinsi tunavyoweza kuboresha mambo. Ili kuboresha mambo, tunataka kuhakikisha kodikodi ni rahisi, kwa hivyo viungo na idadi ya mapishi vinaweza kuboreshwa na kubadilishwa.

1. Hebu badilisha kodikodi kwa njia ifuatayo:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Kuchukua kodikodi kwa majaribio, inaweza kuonekana kama hii:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Boresha kwa kuongeza kichujio na orodha ya ununuzi

Sasa tuna programu inayofanya kazi inayoweza kuzalisha mapishi na ni rahisi kwani inategemea maingizo kutoka kwa mtumiaji, wote juu ya idadi ya mapishi lakini pia viungo vinavyotumika.

Ili kuboresha zaidi, tunataka kuongeza yafuatayo:

- **Chuja viungo**. Tunataka kuwa na uwezo wa kuchuja viungo ambavyo hatupendi au tuna mzio navyo. Ili kufanikisha mabadiliko haya, tunaweza kuhariri maelekezo yetu yaliyopo na kuongeza hali ya kichujio mwishoni mwa maelekezo kama hivi:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Hapo juu, tunaongeza `{filter}` mwishoni mwa maelekezo na pia tunachukua thamani ya kichujio kutoka kwa mtumiaji.

  Mfano wa maingizo ya kuendesha programu sasa unaweza kuonekana kama hivi:

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

  Kama unavyoona, mapishi yoyote yenye maziwa yamechujwa. Lakini, ikiwa una matatizo ya lactose, unaweza kutaka kuchuja mapishi yenye jibini pia, kwa hivyo kuna haja ya kuwa wazi.

- **Tengeneza orodha ya ununuzi**. Tunataka kutengeneza orodha ya ununuzi, ukizingatia kile tulichonacho nyumbani.

  Kwa utendaji huu, tunaweza kujaribu kutatua kila kitu katika maelekezo moja au tunaweza kuyagawanya katika maelekezo mawili. Hebu jaribu njia ya pili. Hapa tunapendekeza kuongeza maelekezo ya ziada, lakini kwa hilo kufanya kazi, tunahitaji kuongeza matokeo ya maelekezo ya awali kama muktadha kwa maelekezo ya pili.

  Tafuta sehemu katika kodikodi inayochapisha matokeo kutoka kwa maelekezo ya kwanza na ongeza kodikodi ifuatayo chini yake:
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

  Kumbuka yafuatayo:

  1. Tunatengeneza maelezo mapya kwa kuongeza matokeo kutoka maelezo ya kwanza kwenye maelezo mapya:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Tunafanya ombi jipya, lakini pia tukizingatia idadi ya tokeni tulizoomba kwenye maelezo ya kwanza, kwa hivyo safari hii tunasema `max_tokens` ni 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     Tukijaribu msimbo huu, sasa tunapata matokeo yafuatayo:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Boresha mpangilio wako

Kile tulicho nacho hadi sasa ni msimbo unaofanya kazi, lakini kuna marekebisho tunapaswa kufanya ili kuboresha mambo zaidi. Baadhi ya mambo tunapaswa kufanya ni:

- **Tenganisha siri kutoka kwa msimbo**, kama vile API key. Siri hazipaswi kuwepo kwenye msimbo na zinapaswa kuhifadhiwa mahali salama. Ili kutenganisha siri kutoka kwa msimbo, tunaweza kutumia vigezo vya mazingira na maktaba kama `python-dotenv` kupakia kutoka kwenye faili. Hivi ndivyo ingeonekana kwenye msimbo:

  1. Tengeneza faili `.env` yenye maudhui yafuatayo:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Kumbuka, kwa Azure, unahitaji kuweka vigezo vya mazingira vifuatavyo:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     Katika msimbo, ungepakia vigezo vya mazingira kama ifuatavyo:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Neno kuhusu urefu wa tokeni**. Tunapaswa kuzingatia ni tokeni ngapi tunahitaji kuzalisha maandishi tunayotaka. Tokeni zinagharimu pesa, kwa hivyo pale inapowezekana, tunapaswa kujaribu kuwa na uchumi na idadi ya tokeni tunazotumia. Kwa mfano, je, tunaweza kuunda maelezo ili kutumia tokeni chache?

  Ili kubadilisha tokeni zinazotumika, unaweza kutumia parameter ya `max_tokens`. Kwa mfano, ikiwa unataka kutumia tokeni 100, ungefanya:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Kujaribu na joto**. Joto ni kitu ambacho hatujakitaja hadi sasa lakini ni muktadha muhimu kwa jinsi programu yetu inavyofanya kazi. Thamani ya joto ikiwa juu zaidi, matokeo yatakuwa ya nasibu zaidi. Kinyume chake, thamani ya joto ikiwa chini zaidi, matokeo yatakuwa ya kutabirika zaidi. Fikiria ikiwa unataka mabadiliko katika matokeo yako au la.

  Ili kubadilisha joto, unaweza kutumia parameter ya `temperature`. Kwa mfano, ikiwa unataka kutumia joto la 0.5, ungefanya:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Kumbuka, kadri unavyokaribia 1.0, matokeo yanakuwa na mabadiliko zaidi.

## Kazi

Kwa kazi hii, unaweza kuchagua nini cha kujenga.

Hapa kuna mapendekezo:

- Rekebisha programu ya jenereta ya mapishi ili kuiboresha zaidi. Jaribu kucheza na thamani za joto, na maelezo ili kuona unachoweza kuunda.
- Jenga "rafiki wa kujifunza". Programu hii inapaswa kuwa na uwezo wa kujibu maswali kuhusu mada fulani kwa mfano Python, unaweza kuwa na maelezo kama "Je, mada fulani katika Python ni nini?", au unaweza kuwa na maelezo yanayosema, nionyeshe msimbo wa mada fulani nk.
- Bot ya historia, fanya historia iwe hai, elekeza bot kucheza kama mhusika wa kihistoria fulani na muulize maswali kuhusu maisha yake na nyakati zake.

## Suluhisho

### Rafiki wa kujifunza

Hapa chini kuna maelezo ya kuanzia, angalia jinsi unavyoweza kuyatumia na kuyarekebisha upendavyo.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot ya historia

Hapa kuna maelezo unayoweza kutumia:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Ukaguzi wa maarifa

Je, dhana ya joto inafanya nini?

1. Inadhibiti jinsi matokeo yanavyokuwa ya nasibu.
1. Inadhibiti jinsi majibu yanavyokuwa makubwa.
1. Inadhibiti idadi ya tokeni zinazotumika.

## 🚀 Changamoto

Unapofanya kazi kwenye kazi, jaribu kubadilisha joto, jaribu kuliweka kuwa 0, 0.5, na 1. Kumbuka kwamba 0 ni lenye mabadiliko kidogo na 1 ni lenye mabadiliko zaidi. Thamani gani inafanya kazi vizuri zaidi kwa programu yako?

## Kazi Nzuri! Endelea Kujifunza

Baada ya kukamilisha somo hili, angalia [Mkusanyiko wa Kujifunza AI ya Kizazi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuongeza maarifa yako ya AI ya kizazi!

Nenda kwenye Somo la 7 ambapo tutatazama jinsi ya [kujenga programu za mazungumzo](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.