<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ce8224073b86b728ed52b19bed7932fd",
  "translation_date": "2025-07-09T12:05:26+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "sw"
}
-->
# Kujenga Programu za Uundaji wa Maandishi

[![Kujenga Programu za Uundaji wa Maandishi](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.sw.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(Bonyeza picha hapo juu kutazama video ya somo hili)_

Umeona hadi sasa kupitia mtaala huu kuwa kuna dhana kuu kama vile prompts na hata somo zima linaloitwa "prompt engineering". Zana nyingi unazoweza kuingiliana nazo kama ChatGPT, Office 365, Microsoft Power Platform na nyingine nyingi, zinakusaidia kutumia prompts kufanikisha jambo fulani.

Ili kuongeza uzoefu kama huo kwenye programu, unahitaji kuelewa dhana kama prompts, completions na kuchagua maktaba ya kutumia. Hiyo ndiyo hasa utakayojifunza katika sura hii.

## Utangulizi

Katika sura hii, utajifunza:

- Kuhusu maktaba ya openai na dhana zake kuu.
- Kujenga programu ya uundaji wa maandishi kwa kutumia openai.
- Kuelewa jinsi ya kutumia dhana kama prompt, temperature, na tokens kujenga programu ya uundaji wa maandishi.

## Malengo ya kujifunza

Mwisho wa somo hili, utaweza:

- Eleza ni nini programu ya uundaji wa maandishi.
- Jenga programu ya uundaji wa maandishi kwa kutumia openai.
- Sanidi programu yako kutumia tokens zaidi au kidogo na pia badilisha temperature, kwa matokeo tofauti.

## Programu ya uundaji wa maandishi ni nini?

Kawaida unapo jenga programu huwa na aina fulani ya kiolesura kama ifuatavyo:

- Inayotegemea amri. Programu za console ni programu za kawaida ambapo unaandika amri na inatekeleza kazi. Kwa mfano, `git` ni programu inayotegemea amri.
- Kiolesura cha mtumiaji (UI). Baadhi ya programu zina kiolesura cha picha (GUIs) ambapo unabonyeza vifungo, kuingiza maandishi, kuchagua chaguzi na zaidi.

### Programu za console na UI zina mipaka

Linganisho na programu inayotegemea amri ambapo unaandika amri:

- **Ina mipaka**. Huwezi kuandika amri yoyote, ni zile tu ambazo programu inaziiunga mkono.
- **Lugha maalum**. Baadhi ya programu zinaunga mkono lugha nyingi, lakini kwa kawaida programu imejengwa kwa lugha maalum, hata kama unaweza kuongeza msaada wa lugha zaidi.

### Faida za programu za uundaji wa maandishi

Basi programu ya uundaji wa maandishi ni tofauti vipi?

Katika programu ya uundaji wa maandishi, una uhuru zaidi, huna kikomo kwa seti ya amri au lugha maalum ya kuingiza. Badala yake, unaweza kutumia lugha ya asili kuingiliana na programu. Faida nyingine ni kwamba kwa kuwa tayari unatumia chanzo cha data kilichofunzwa kwa mkusanyiko mkubwa wa taarifa, wakati programu ya kawaida inaweza kuwa na mipaka kwa kile kilicho kwenye hifadhidata.

### Naweza kujenga nini kwa programu ya uundaji wa maandishi?

Kuna mambo mengi unayoweza kujenga. Kwa mfano:

- **Chatbot**. Chatbot inayojibu maswali kuhusu mada mbalimbali, kama kampuni yako na bidhaa zake inaweza kuwa chaguo zuri.
- **Msaidizi**. LLMs ni nzuri katika mambo kama kufupisha maandishi, kupata maarifa kutoka kwa maandishi, kutengeneza maandishi kama wasifu na zaidi.
- **Msaidizi wa msimbo**. Kulingana na mfano wa lugha unayotumia, unaweza kujenga msaidizi wa msimbo anayekusaidia kuandika msimbo. Kwa mfano, unaweza kutumia bidhaa kama GitHub Copilot pamoja na ChatGPT kusaidia kuandika msimbo.

## Ninawezaje kuanza?

Kweli, unahitaji njia ya kuunganishwa na LLM ambayo kawaida inahusisha mbinu mbili zifuatazo:

- Tumia API. Hapa unaunda maombi ya wavuti kwa kutumia prompt yako na kurudishiwa maandishi yaliyotengenezwa.
- Tumia maktaba. Maktaba husaidia kufunga miito ya API na kuifanya iwe rahisi kutumia.

## Maktaba/SDKs

Kuna maktaba maarufu kadhaa za kufanya kazi na LLM kama:

- **openai**, maktaba hii inafanya iwe rahisi kuungana na mfano wako na kutuma prompts.

Kisha kuna maktaba zinazofanya kazi kwa kiwango cha juu zaidi kama:

- **Langchain**. Langchain ni maarufu na inaunga mkono Python.
- **Semantic Kernel**. Semantic Kernel ni maktaba ya Microsoft inayounga mkono lugha za C#, Python, na Java.

## Programu ya kwanza kwa kutumia openai

Tuchunguze jinsi ya kujenga programu yetu ya kwanza, maktaba tunazohitaji, kiasi kinachohitajika na kadhalika.

### Sakinisha openai

Kuna maktaba nyingi kwa ajili ya kuingiliana na OpenAI au Azure OpenAI. Inawezekana kutumia lugha mbalimbali za programu kama C#, Python, JavaScript, Java na zaidi. Tumechagua kutumia maktaba ya Python ya `openai`, hivyo tutatumia `pip` kuiweka.

```bash
pip install openai
```

### Unda rasilimali

Unahitaji kufanya hatua zifuatazo:

- Unda akaunti kwenye Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Pata ufikiaji wa Azure OpenAI. Nenda [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) na omba ufikiaji.

  > [!NOTE]
  > Wakati wa kuandika, unahitaji kuomba ufikiaji wa Azure OpenAI.

- Sakinisha Python <https://www.python.org/>
- Kuwa umeunda rasilimali ya Azure OpenAI Service. Angalia mwongozo huu wa jinsi ya [kuunda rasilimali](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Pata API key na endpoint

Sasa, unahitaji kusema maktaba yako ya `openai` ni API key gani itumie. Ili kupata API key yako, nenda sehemu ya "Keys and Endpoint" ya rasilimali yako ya Azure OpenAI na nakili thamani ya "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Sasa baada ya kupata taarifa hii, tuambie maktaba zitumie.

> [!NOTE]
> Inafaa kutenganisha API key yako na msimbo wako. Unaweza kufanya hivyo kwa kutumia environment variables.
>
> - Weka environment variable `OPENAI_API_KEY` kwa API key yako.
>   `export OPENAI_API_KEY='sk-...'`

### Sanidi usanidi wa Azure

Kama unatumia Azure OpenAI, hivi ndivyo unavyosanidi usanidi:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Hapo juu tunasanidi yafuatayo:

- `api_type` kuwa `azure`. Hii inamwambia maktaba itumie Azure OpenAI badala ya OpenAI.
- `api_key`, hii ni API key yako uliyoipata kwenye Azure Portal.
- `api_version`, hii ni toleo la API unalotaka kutumia. Wakati wa kuandika, toleo la hivi karibuni ni `2023-05-15`.
- `api_base`, hii ni endpoint ya API. Unaweza kuipata kwenye Azure Portal karibu na API key yako.

> [!NOTE] > `os.getenv` ni function inayosoma environment variables. Unaweza kuitumia kusoma environment variables kama `OPENAI_API_KEY` na `API_BASE`. Weka environment variables hizi kwenye terminal yako au kwa kutumia maktaba kama `dotenv`.

## Tengeneza maandishi

Njia ya kutengeneza maandishi ni kutumia darasa la `Completion`. Hapa kuna mfano:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

Katika msimbo hapo juu, tunaunda kitu cha completion na kuingiza mfano tunayotaka kutumia na prompt. Kisha tunachapisha maandishi yaliyotengenezwa.

### Chat completions

Hadi sasa, umeona jinsi tunavyotumia `Completion` kutengeneza maandishi. Lakini kuna darasa jingine linaloitwa `ChatCompletion` ambalo linafaa zaidi kwa chatbots. Hapa kuna mfano wa kutumia:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Zaidi kuhusu utendaji huu katika sura inayofuata.

## Zoef - programu yako ya kwanza ya uundaji wa maandishi

Sasa tumepata jinsi ya kusanidi na kutumia openai, ni wakati wa kujenga programu yako ya kwanza ya uundaji wa maandishi. Kufanya hivyo, fuata hatua hizi:

1. Unda mazingira ya virtual na sakinisha openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Kama unatumia Windows andika `venv\Scripts\activate` badala ya `source venv/bin/activate`.

   > [!NOTE]
   > Pata Azure OpenAI key yako kwa kwenda [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) na tafuta `Open AI` kisha chagua `Open AI resource` na kisha chagua `Keys and Endpoint` na nakili thamani ya `Key 1`.

1. Unda faili _app.py_ na uweke msimbo ufuatao:

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
   > Kama unatumia Azure OpenAI, unahitaji kuweka `api_type` kuwa `azure` na kuweka `api_key` kuwa Azure OpenAI key yako.

   Utapata matokeo kama ifuatavyo:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Aina tofauti za prompts, kwa mambo tofauti

Sasa umeona jinsi ya kutengeneza maandishi kwa kutumia prompt. Hata una programu inayotumika ambayo unaweza kubadilisha na kurekebisha kutengeneza aina tofauti za maandishi.

Prompts zinaweza kutumika kwa kazi mbalimbali. Kwa mfano:

- **Tengeneza aina ya maandishi**. Kwa mfano, unaweza kutengeneza shairi, maswali kwa jaribio n.k.
- **Tafuta taarifa**. Unaweza kutumia prompts kutafuta taarifa kama mfano huu 'CORS inamaanisha nini katika maendeleo ya wavuti?'.
- **Tengeneza msimbo**. Unaweza kutumia prompts kutengeneza msimbo, kwa mfano kuunda regular expression inayotumika kuthibitisha barua pepe au kwa nini usitengeneze programu nzima, kama programu ya wavuti?

## Mfano wa matumizi halisi: mtengenezaji wa mapishi

Fikiria una viungo nyumbani na unataka kupika kitu. Kwa hilo, unahitaji mapishi. Njia ya kupata mapishi ni kutumia injini ya utafutaji au unaweza kutumia LLM kufanya hivyo.

Unaweza kuandika prompt kama hii:

> "Nionyeshe mapishi 5 ya chakula chenye viungo vifuatavyo: kuku, viazi, na karoti. Kwa kila mapishi, orodhesha viungo vyote vilivyotumika"

Kutokana na prompt hapo juu, unaweza kupata jibu kama ifuatavyo:

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

Matokeo haya ni mazuri, najua nini kupika. Sasa, maboresho yanayoweza kuwa na maana ni:

- Kuchuja viungo ambavyo sipendi au nina mzio navyo.
- Tengeneza orodha ya manunuzi, ikiwa sina viungo vyote nyumbani.

Kwa hali hizi, tutaongeza prompt ya ziada:

> "Tafadhali toa mapishi yenye kitunguu saumu kwa sababu nina mzio na badilisha na kitu kingine. Pia, tafadhali tengeneza orodha ya manunuzi kwa mapishi hayo, ukizingatia tayari nina kuku, viazi na karoti nyumbani."

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

Hayo ni mapishi yako matano, pasipo kutajwa kitunguu saumu na pia una orodha ya manunuzi ukizingatia unavyo viungo nyumbani.

## Zoef - tengeneza mtengenezaji wa mapishi

Sasa tumeshuhudia hali halisi, andika msimbo unaolingana na hali hiyo. Kufanya hivyo, fuata hatua hizi:

1. Tumia faili lililopo _app.py_ kama msingi
1. Tafuta variable ya `prompt` na badilisha msimbo wake kuwa kama ifuatavyo:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Ukikimbia msimbo sasa, unapaswa kuona matokeo kama ifuatavyo:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, LLM yako si ya kutabirika, hivyo unaweza kupata matokeo tofauti kila mara unapoendesha programu.

   Vizuri, tuchunguze jinsi ya kuboresha mambo. Ili kuboresha, tunataka kuhakikisha msimbo ni rahisi kubadilika, hivyo viungo na idadi ya mapishi vinaweza kubadilishwa.

1. Badilisha msimbo kwa njia ifuatayo:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Kuendesha msimbo kama jaribio, inaweza kuwa kama hii:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Boresha kwa kuongeza chujio na orodha ya manunuzi

Sasa tuna programu inayofanya kazi inayoweza kutoa mapishi na ni rahisi kwa kuwa inategemea maingizo kutoka kwa mtumiaji, kwa idadi ya mapishi na pia viungo vinavyotumika.

Ili kuboresha zaidi, tunataka kuongeza yafuatayo:

- **Chuja viungo**. Tunataka kuweza kuchuja viungo ambavyo hatupendi au tuna mzio navyo. Ili kufanikisha hili, tunaweza kuhariri prompt yetu iliyopo na kuongeza sharti la chujio mwishoni kama ifuatavyo:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Hapo juu, tunaongeza `{filter}` mwishoni mwa prompt na pia tunachukua thamani ya chujio kutoka kwa mtumiaji.

  Mfano wa kuendesha programu sasa unaweza kuwa kama ifuatavyo:

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

  Kama unavyoona, mapishi yoyote yenye maziwa yamechujwa. Lakini, kama una ugumu wa kumeng'enya lactose, unaweza pia kutaka kuchuja mapishi yenye jibini, hivyo kuna haja ya kuwa wazi.

- **Tengeneza orodha ya manunuzi**. Tunataka kutengeneza orodha ya manunuzi, tukizingatia kile tayari tunacho nyumbani.

  Kwa utendaji huu, tunaweza kujaribu kutatua yote kwa prompt moja au tukagawanya kuwa prompts mbili. Tujaribu njia ya pili. Hapa tunapendekeza kuongeza prompt ya ziada, lakini ili ifanye kazi, tunahitaji kuongeza matokeo ya prompt ya kwanza kama muktadha kwa prompt ya pili.

  Tafuta sehemu ya msimbo inayochapisha matokeo ya prompt ya kwanza na ongeza msimbo ufuatao chini yake:

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

  1. Tunaunda prompt mpya kwa kuongeza matokeo ya prompt ya kwanza kwenye prompt mpya:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```
1. Tunafanya ombi jipya, lakini pia tukizingatia idadi ya tokeni tulizozitaka katika ombi la kwanza, kwa hivyo wakati huu tunasema `max_tokens` ni 1200.

   ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

   Tukichukua msimbo huu kujaribu, sasa tunapata matokeo yafuatayo:

   ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Boresha usanidi wako

Hadi sasa tunayo msimbo unaofanya kazi, lakini kuna marekebisho ambayo tunapaswa kufanya ili kuboresha zaidi. Baadhi ya mambo tunayopaswa kufanya ni:

- **Tofautisha siri na msimbo**, kama vile API key. Siri hazipaswi kuwepo ndani ya msimbo na zinapaswa kuhifadhiwa mahali salama. Ili kutofautisha siri na msimbo, tunaweza kutumia mabadiliko ya mazingira (environment variables) na maktaba kama `python-dotenv` kuzisoma kutoka kwenye faili. Hivi ndivyo inavyoonekana kwenye msimbo:

  1. Tengeneza faili `.env` yenye maudhui yafuatayo:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     
> Note, kwa Azure, unahitaji kuweka mabadiliko ya mazingira yafuatayo:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     Katika msimbo, ungesoma mabadiliko ya mazingira hivi:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Neno kuhusu urefu wa tokeni**. Tunapaswa kuzingatia ni tokeni ngapi tunazohitaji kuzalisha maandishi tunayotaka. Tokeni zinagharimu, hivyo pale panapowezekana, tunapaswa kuwa makini na idadi ya tokeni tunazotumia. Kwa mfano, je, tunaweza kuandika ombi kwa njia ambayo tunatumia tokeni chache?

  Kubadilisha tokeni zinazotumika, unaweza kutumia kigezo `max_tokens`. Kwa mfano, ikiwa unataka kutumia tokeni 100, ungefanya hivi:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Kujaribu na joto (temperature)**. Joto ni jambo ambalo hatujalizungumzia hadi sasa lakini ni muktadha muhimu kwa jinsi programu yetu inavyofanya kazi. Kadri thamani ya joto inavyoongezeka, ndivyo matokeo yanavyokuwa ya nasibu zaidi. Kinyume chake, kadri joto linavyopungua, ndivyo matokeo yanavyokuwa yanayoweza kutabirika zaidi. Fikiria kama unataka mabadiliko katika matokeo yako au la.

  Kubadilisha joto, unaweza kutumia kigezo `temperature`. Kwa mfano, ikiwa unataka kutumia joto la 0.5, ungefanya hivi:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Note, kadri unavyokaribia 1.0, ndivyo matokeo yanavyobadilika zaidi.

## Kazi ya nyumbani

Kwa kazi hii, unaweza kuchagua unachotaka kujenga.

Hapa kuna mapendekezo:

- Rekebisha app ya kizalishaji cha mapishi ili kuboresha zaidi. Jaribu mabadiliko ya joto, na maombi (prompts) kuona unachoweza kuunda.
- Tengeneza "mwenzi wa kusoma". App hii inapaswa kuwa na uwezo wa kujibu maswali kuhusu mada fulani, kwa mfano Python, unaweza kuwa na maombi kama "Nini mada fulani katika Python?", au unaweza kuwa na ombi linalosema, nionyeshe msimbo wa mada fulani n.k.
- Bot wa historia, fanya historia iwe hai, elekeza bot kucheza kama mhusika fulani wa kihistoria na umuulize maswali kuhusu maisha yake na nyakati zake.

## Suluhisho

### Mwenzi wa kusoma

Hapa chini ni ombi la kuanzia, angalia jinsi unavyoweza kulitumia na kuliboresha kwa ladha yako.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot wa historia

Hapa kuna baadhi ya maombi unayoweza kutumia:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Ukaguzi wa maarifa

Je, dhana ya joto (temperature) inafanya nini?

1. Inadhibiti jinsi matokeo yanavyokuwa ya nasibu.
1. Inadhibiti ukubwa wa jibu.
1. Inadhibiti ni tokeni ngapi zinatumiwa.

## 🚀 Changamoto

Unapofanya kazi ya nyumbani, jaribu kubadilisha joto, jaribu kuweka 0, 0.5, na 1. Kumbuka kuwa 0 ni joto lenye mabadiliko kidogo na 1 ni joto lenye mabadiliko mengi. Ni thamani gani inafaa zaidi kwa app yako?

## Kazi Nzuri! Endelea Kujifunza

Baada ya kumaliza somo hili, angalia [Mkusanyiko wa Kujifunza AI ya Kizazi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendelea kuongeza maarifa yako ya AI ya Kizazi!

Nenda kwenye Somo la 7 ambapo tutaangalia jinsi ya [kujenga programu za mazungumzo](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Kiarifu cha Msamaha**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.