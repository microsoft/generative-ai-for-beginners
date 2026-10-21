# Kujenga Programu za Uzalishaji wa Maandishi

[![Kujenga Programu za Uzalishaji wa Maandishi](../../../translated_images/sw/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Bonyeza picha hapo juu kutazama video ya somo hili)_

Umeona hadi sasa katika mtaala huu kwamba kuna dhana kuu kama vile prompts na hata taaluma nzima inayoitwa "ufundi wa prompts". Zana nyingi unazoweza kuingiliana nazo kama ChatGPT, Office 365, Microsoft Power Platform na zaidi, zinakuunga mkono kutumia prompts kufanya jambo fulani.

Ili kuongeza uzoefu kama huo kwenye programu, unahitaji kuelewa dhana kama prompts, completions na kuchagua maktaba ya kufanya nayo kazi. Hiyo ndio hasa utaijifunza katika sura hii.

## Utangulizi

Katika sura hii, utajifunza:

- Kujifunza kuhusu maktaba ya openai na dhana zake kuu.
- Kujenga programu ya uzalishaji wa maandishi kwa kutumia openai.
- Kuelewa jinsi ya kutumia dhana kama prompt, temperature, na tokens kujenga programu ya uzalishaji wa maandishi.

## Malengo ya kujifunza

Mwisho wa somo hili, utakuwa na uwezo wa:

- Eleza ni nini programu ya uzalishaji wa maandishi.
- Kujenga programu ya uzalishaji wa maandishi kwa kutumia openai.
- Sanidi programu yako kutumia tokens zaidi au kidogo na pia badilisha temperature, kwa kupata matokeo tofauti.

## Programu ya uzalishaji wa maandishi ni nini?

Kwa kawaida unapojenga programu ina aina fulani ya kiolesura kama ifuatavyo:

- Imegusa amri. Programu za koni ni programu za kawaida ambapo unaandika amri na ifanye kazi. Kwa mfano, `git` ni programu ya aina hii ya amri.
- Kiolesura cha mtumiaji (UI). Baadhi ya programu zina kiolesura cha mtumiaji cha picha (GUIs) ambapo unabonyeza vifungo, kuingiza maandishi, kuchagua chaguzi na zaidi.

### Programu za Koni na UI zina mipaka

Linganisha na programu ya amri ambapo unaandika amri:

- **Ina mipaka**. Huwezi tu kuandika amri yoyote, ni zile tu ambazo programu inaunga mkono.
- **Lugha maalum**. Baadhi ya programu zinaunga mkono lugha nyingi, lakini kwa kawaida programu imejengwa kwa lugha maalum, hata kama unaweza kuongeza msaada wa lugha zaidi.

### Manufaa ya programu za uzalishaji wa maandishi

Basi, programu ya uzalishaji wa maandishi ni tofauti vipi?

Katika programu ya uzalishaji wa maandishi, una uhuru zaidi, huna mipaka kwa seti ya amri au lugha maalum ya kuingiza. Badala yake, unaweza kutumia lugha ya asili kuingiliana na programu. Faida nyingine ni kwamba tayari unaingiliana na chanzo cha data ambacho kimefundishwa kwenye maudhui makubwa ya taarifa, huku programu ya kawaida inaweza kuwa na mipaka kwa kile kilicho kwenye hifadhidata.

### Nini ninaweza kujenga kwa programu ya uzalishaji wa maandishi?

Kuna mambo mengi unayoweza kujenga. Kwa mfano:

- **Boti ya mazungumzo**. Boti ya mazungumzo inayojibu maswali kuhusu mada, kama kampuni yako na bidhaa zake inaweza kuwa chaguo zuri.
- **Msaidizi**. LLMs ni mzuri katika mambo kama vile kufupisha maandishi, kupata maarifa kutoka kwenye maandishi, kuzalisha maandishi kama wasifu na zaidi.
- **Msaidizi wa msimbo**. Kutegemea mfano wa lugha unayotumia, unaweza kujenga msaidizi wa msimbo anayekusaidia kuandika msimbo. Kwa mfano, unaweza kutumia bidhaa kama GitHub Copilot pamoja na ChatGPT kusaidia kuandika msimbo.

## Ninawezaje kuanza?

Vizuri, unahitaji kupata njia ya kuunganishwa na LLM ambayo kwa kawaida inajumuisha njia mbili zifuatazo:

- Tumia API. Hapa unaunda maombi ya wavuti kwa kutumia prompt yako na kupata maandishi yaliyozalishwa.
- Tumia maktaba. Maktaba husaidia kufunga miito ya API na kufanya iwe rahisi kutumia.

## Maktaba/SDKs

Kuna maktaba maarufu kadhaa za kufanya kazi na LLMs kama:

- **openai**, maktaba hii inafanya iwe rahisi kuungana na mfano wako na kutuma prompts.

Kisha kuna maktaba zinazofanya kazi kwa kiwango cha juu kama:

- **Langchain**. Langchain ni maarufu na inaunga mkono Python.
- **Semantic Kernel**. Semantic Kernel ni maktaba ya Microsoft inayounga mkono lugha za C#, Python, na Java.

## Programu ya kwanza kwa kutumia openai

Tuwone jinsi tunavyoweza kujenga programu yetu ya kwanza, maktaba tunazohitaji, kiasi kinachohitajika na kadhalika.

### Sakinisha openai

Kuna maktaba nyingi huko kwa kuingiliana na OpenAI au Azure OpenAI. Inawezekana kutumia lugha mbalimbali za programu kama C#, Python, JavaScript, Java na zaidi. Tumechagua kutumia maktaba ya Python ya `openai`, kwa hivyo tutatumia `pip` kuisakinisha.

```bash
pip install openai
```

### Unda rasilimali

Unahitaji kufanya hatua zifuatazo:

- Unda akaunti kwenye Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Pata upatikanaji wa Azure OpenAI. Nenda [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) na omba upatikanaji.

  > [!NOTE]
  > Wakati wa kuandika, unahitaji kuomba upatikanaji wa Azure OpenAI.

- Sakinisha Python <https://www.python.org/>
- Kuwa umeunda rasilimali ya Azure OpenAI Service. Tazama mwongozo huu kuhusu jinsi ya [kuunda rasilimali](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Tafuta API key na endpoint

Hivi sasa, unahitaji kusema maktaba yako ya `openai` ni funguo gani za API itumie. Ili kupata funguo za API, nenda kwenye sehemu ya "Keys and Endpoint" ya rasilimali yako ya Azure OpenAI nakili thamani ya "Key 1".

![Blade ya funguo na endpoint katika Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Sasa ume nakili taarifa hii, hebu tuiamuru maktaba kuitumia.

> [!NOTE]
> Inafaa kutenga funguo yako ya API kutoka kwenye msimbo wako. Unaweza kufanya hivyo kwa kutumia vigezo vya mazingira.
>
> - Weka kigezo cha mazingira `OPENAI_API_KEY` kuwa funguo yako ya API.
>   `export OPENAI_API_KEY='sk-...'`

### Sanidi mipangilio Azure

Ikiwa unatumia Azure OpenAI (sasa sehemu ya Microsoft Foundry), hapa jinsi unavyosanidi mipangilio. Tunatumia mteja wa kawaida wa `OpenAI` unaolenga kwenye endpoint ya Azure OpenAI `/openai/v1/`, unaofanya kazi na Responses API na hauhitaji `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Juu tunaseti yafuatayo:

- `api_key`, hii ni funguo yako ya API iliyo katika Azure Portal au Microsoft Foundry portal.
- `base_url`, hii ni endpoint ya rasilimali ya Foundry iliyoongezwa na `/openai/v1/`. Endpoint thabiti ya v1 hufanya kazi kwa OpenAI na Azure OpenAI bila usimamizi wa `api_version`.

> [!NOTE] > `os.environ` husoma vigezo vya mazingira. Unaweza kuitumia kusoma vigezo vya mazingira kama `AZURE_OPENAI_API_KEY` na `AZURE_OPENAI_ENDPOINT`. Weka vigezo hivi vya mazingira kwenye terminali yako au kwa kutumia maktaba kama `dotenv`.

## Tengeneza maandishi

Njia ya kutengeneza maandishi ni kutumia Responses API kupitia njia ya `responses.create`. Hapa kuna mfano:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

Katika msimbo huu wa juu, tunaunda jibu na tunapita mfano tunayotaka kutumia na prompt. Kisha tunachapisha maandishi yaliyozalishwa kupitia `response.output_text`.

### Mazungumzo yenye duru nyingi

Responses API inafaa kwa uzalishaji wa maandishi wa duru moja na pia boti za mazungumzo yenye duru nyingi - unatoa orodha ya ujumbe katika `input` kujenga mazungumzo:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Zaidi kuhusu kipengele hiki katika sura inayokuja.

## Zoefu - programu yako ya kwanza ya uzalishaji wa maandishi

Sasa tunapoijua jinsi ya kusanidi na kuandaa openai, ni wakati wa kujenga programu yako ya kwanza ya uzalishaji wa maandishi. Ili kujenga programu yako, fuata hatua hizi:

1. Unda mazingira ya mtumiaji na sakinisha openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Ikiwa unatumia Windows andika `venv\Scripts\activate` badala ya `source venv/bin/activate`.

   > [!NOTE]
   > Tafuta funguo yako ya Azure OpenAI kwa kwenda [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) na tafuta `Open AI` kisha chagua `Open AI resource` kisha chagua `Keys and Endpoint` nakili thamani ya `Key 1`.

1. Unda faili _app.py_ na uteupe msimbo ufuatao:

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
   > Ikiwa unatumia OpenAI wa kawaida (sio Azure), tumia `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (bila `base_url`) na pita jina la mfano kama `gpt-5-mini` badala ya jina la deployment.

   Utapaswa kuona matokeo kama ifuatavyo:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Aina tofauti za prompts, kwa mambo tofauti

Sasa umeona jinsi ya kutengeneza maandishi kwa kutumia prompt. Hata una programu inayoendesha ambayo unaweza kubadilisha na kugeuza kuzalisha aina tofauti za maandishi.

Prompts zinaweza kutumika kwa aina zote za kazi. Kwa mfano:

- **Zalisha aina ya maandishi**. Kwa mfano, unaweza kuzalisha shairi, maswali kwa quiz nk.
- **Tafuta taarifa**. Unaweza kutumia prompts kutafuta taarifa kama mfano huu 'CORS ina maana gani katika uzinduaji wa wavuti?'.
- **Zalisha msimbo**. Unaweza kutumia prompts kuzalisha msimbo, kwa mfano kuunda regex ya kutathmini barua pepe au kwanini usizalishe programu nzima, kama programu ya wavuti?

## Mfano wa matumizi ya vitendo: kizalishaji cha mapishi

Fikiria una rasilimali nyumbani na unataka kupika kitu. Kwa hilo, unahitaji mapishi. Njia ya kupata mapishi ni kutumia injini ya utafutaji au unaweza kutumia LLM kufanya hivyo.

Unaweza kuandika prompt kama ifuatavyo:

> "Nionyeshe mapishi 5 ya chakula chenye viambato vifuatavyo: kuku, viazi, na karoti. Kwa kila mapishi, orodhesha viambato vyote vilivyotumika"

Kutokana na prompt ya juu, unaweza kupata majibu kama haya:

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

Matokeo haya ni mazuri, najua nini kupika. Hivi sasa, maboresho yanayoweza kusaidia ni:

- Kutenganisha viambato nisivyopenda au ambavyo nina mzio navyo.
- Tengeneza orodha ya kununua, iwapo sina viambato vyote nyumbani.

Kwa hali hizi, tukaeongeza prompt ya ziada:

> "Tafadhali ondoa mapishi yenye kitunguu saumu kwani nina mzio na badilisha na kitu kingine. Pia, tafadhali tengeneza orodha ya kununua kwa mapishi hayo, ukizingatia kwamba tayari nina kuku, viazi na karoti nyumbani."

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

Hayo ni mapishi yako matano, bila kutaja kitunguu saumu na pia una orodha ya kununua ukizingatia unavyo vitu tayari nyumbani.

## Zoefu - jenga kizalishaji cha mapishi

Sasa tunapojua jinsi ya kucheza hali ya tukio, wacha tuandike msimbo kuendana na tukio lililoonyeshwa. Kwa kufanya hivyo, fuata hatua hizi:

1. Tumia faili lililotumika la _app.py_ kama chanzo
1. Tafuta kichujio cha `prompt` na badilisha msimbo wake kama ifuatavyo:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Ukikimbiza msimbo sasa, unapaswa kuona matokeo kama ifuatavyo:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > KUMBUKA, LLM yako haina utabiri thabiti, hivyo unaweza kupata matokeo tofauti kila mara unapotumia programu.

   Nzuri, tutaone jinsi ya kuboresha mambo. Ili kuboresha mambo, tunataka kuhakikisha msimbo ni rahisi kubadilika, hivyo viambato na idadi ya mapishi vinaweza kuboreshwa na kubadilishwa.

1. Tabadilisha msimbo kwa njia ifuatayo:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Kuendesha msimbo huu kama jaribio, unaweza kuona ifuatavyo:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Boreshwa kwa kuongeza kichujio na orodha ya kununua

Sasa tuna programu inayofanya kazi ya kuzalisha mapishi na ni rahisi kubadilika kwa kuwa inategemea maingizo kutoka kwa mtumiaji, kwa idadi ya mapishi lakini pia viambato vilivyotumika.

Ili kuboresha zaidi, tunataka kuongeza yafuatayo:

- **Chuja viambato**. Tunataka kuweza kuchuja viambato visivyopendwa au vyenye mzio. Ili kufanya mabadiliko haya, tunaweza kuhariri prompt yetu na kuongeza sharti la kuchuja mwishoni kama ifuatavyo:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Juu, tunaongeza `{filter}` mwishoni mwa prompt na pia tunakamata thamani ya kichujio kutoka kwa mtumiaji.

  Mfano wa kuendesha programu sasa unaweza kuonekana kama ifuatavyo:

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

  Kama unavyoona, mapishi yote yenye maziwa yametolewa. Lakini, kama una ugumu wa kufagia maziwa, unaweza kutaka pia kuchuja mapishi yenye jibini, hivyo inahitaji kuwa wazi.

- **Tengeneza orodha ya kununua**. Tunataka kutengeneza orodha ya kununua, tukizingatia kile already tunacho nyumbani.

  Kwa kipengele hiki, tunaweza kujaribu kutatua kila kitu katika prompt moja au kuzitenga katika prompts mbili. Hebu jaribu njia ya pili. Hapa tunapendekeza kuongeza prompt ya ziada, lakini ili ifanye kazi, tunahitaji kuongeza matokeo ya prompt ya kwanza kama muktadha kwa prompt ya pili.

  Tafuta sehemu ya msimbo inayochapisha matokeo kutoka kwa prompt ya kwanza na ongeza msimbo ufuatao chini yake:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Kumbuka yafuatayo:

  1. Tunaunda prompt mpya kwa kuongeza matokeo ya prompt ya kwanza kwenye prompt mpya:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Tunatuma ombi jipya, lakini pia tukizingatia idadi ya tokens tuliyoomba katika prompt ya kwanza, kwa mara hii tunasema `max_output_tokens` ni 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Kuendesha msimbo huu sasa tunapata matokeo yafuatayo:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Boreshaji la usanidi wako

Kile tulichonacho hadi sasa ni msimbo unaofanya kazi, lakini kuna marekebisho kadhaa tunayopaswa kufanya kuboresha mambo zaidi. Baadhi ya mambo tunayopaswa kufanya ni:

- **Tenganisha siri na msimbo**, kama vile ufunguo wa API. Siri hazipaswi kuwepo kwenye msimbo na zinapaswa kuhifadhiwa mahali salama. Kutenganisha siri na msimbo, tunaweza kutumia vigezo vya mazingira na maktaba kama `python-dotenv` kuvipakia kutoka kwenye faili. Hivi ndivyo itakavyokuwa kwenye msimbo:

  1. Tengeneza faili `.env` yenye yaliyomo kama yafuatavyo:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Kumbuka, kwa Azure OpenAI katika Microsoft Foundry, unapaswa kuweka vigezo vya mazingira vifuatavyo badala yake:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Katika msimbo, utapakia vigezo vya mazingira kama ifuatavyo:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Neno kuhusu urefu wa tokeni**. Tunapaswa kuzingatia ni tokeni ngapi tunazohitaji kuzalisha maandishi tunayoyataka. Tokeni zinagharimu pesa, hivyo inapowezekana, tunapaswa kutumia tokeni kwa uangalifu. Kwa mfano, tunaweza kuweka maelekezo kwa njia ambayo tutatumia tokeni chache?

  Kubadilisha idadi ya tokeni zinazotumika, unaweza kutumia kiparameta cha `max_output_tokens`. Kwa mfano, ukitaka kutumia tokeni 100, utafanya hivi:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Kujaribu joto la matumizi**. Joto ni jambo ambalo hatujalizungumzia hadi sasa lakini ni muktadha muhimu kwa jinsi programu yetu inavyofanya kazi. Joto juu zaidi husababisha matokeo kuwa ya kubahatisha zaidi. Kinyume chake, joto la chini husababisha matokeo kuwa ya kutabirika zaidi. Fikiria kama unataka utofauti katika matokeo yako au la.

  Kubadilisha joto, unaweza kutumia kiparameta cha `temperature`. Kwa mfano, ukitaka kutumia joto la 0.5, utafanya hivi:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Kumbuka, kadri unavyokaribia 1.0, ndivyo matokeo yanavyokuwa na utofauti zaidi.

- **Mifano ya uelewa haituzii `temperature`**. Huu ni mwelekeo muhimu wa mwaka 2026. Mifano ya sasa, isiyotumika tena Microsoft Foundry ni **mifano ya uelewa** (familia ya GPT-5, mfululizo wa o-series) - na **haitumii `temperature` au `top_p`** (pamoja na `max_tokens`; tumia `max_output_tokens`). Ukitumia `temperature` kwenye `gpt-5-mini` utapata kosa la "kiparameta hakitumiki". Kwa hivyo kupima mfano wa joto ulio juu, tumia mfano ambao bado una mkazo wa manyanyaso ya sampuli - kwa mfano mfano wazi wa **Llama** kama `Llama-3.3-70B-Instruct` kutoka kwenye [katalogi ya mifano ya Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), unaopatikana kupitia Foundry Models / Azure AI Inference endpoint (kwa njia ile ile ya sampuli za `githubmodels-*`). Kwa mifano ya uelewa kama GPT-5, unafanikisha matokeo kwa njia tofauti:
  - **Uhandisi wa maelekezo** - maagizo wazi, mifano, na matokeo yenye muundo (tazama somo [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) hufanya kazi ambayo vigezo vya sampuli vilifanya hapo awali.
  - **Udhibiti wa uelewa** - vigezo kama jitihada ya uelewa/uwelezaji huweka usawa kati ya kina cha mantiki dhidi ya ucheleweshaji na gharama.

  Kwa ufupi: `temperature`/`top_p` bado vina manufaa kwenye mifano mingi (Llama, Mistral, Phi, na familia ya GPT-4.x - ingawa GPT-4.x inazidi kuachwa), lakini mwelekeo ni uhandisi wa maelekezo + udhibiti wa uelewa kwenye mifano ya uelewa kama GPT-5.

## Kazi ya Nyumbani

Kwa kazi hii ya nyumbani, unaweza kuchagua kile cha kujenga.

Haya ni mapendekezo:

- Rekebisha programu ya jenereta ya mapishi kuboresha zaidi. Jaribu kutumia thamani tofauti za joto, na maelekezo ili kuona unachoweza kupata.
- Tengeneza "mwenzi wa kusoma". Programu hii inapaswa kuwaze uwezo wa kujibu maswali kuhusu mada fulani kama Python, unaweza kuwa na maelekezo kama "Nini mada fulani katika Python?", au unaweza kuwa na maelekezo yanayosema, nionyeshe msimbo wa mada fulani nk.
- Bot wa historia, fanya historia iwe hai, elekeza bot kucheza kama mhusika fulani wa kihistoria na umuulize maswali kuhusu maisha yake na nyakati zake.

## Suluhisho

### Mwenzi wa Kusoma

Hapo chini ni maelekezo ya kuanzia, tazama jinsi unavyoweza kuyatumia na kuyarekebisha kama unavyopenda.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot wa Historia

Haya ni maelekezo unaweza kutumia:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Ukaguzi wa Maarifa

Kazi gani dhana ya joto hufanya?

1. Hudhibiti jinsi matokeo yanavyokuwa ya kubahatisha.
1. Hudhibiti ukubwa wa jibu.
1. Hudhibiti idadi ya tokeni zinazotumika.

## 🚀 Changamoto

Unapofanya kazi ya nyumbani, jaribu kubadilisha joto, jaribu kuziweka 0, 0.5, na 1. Kumbuka kuwa 0 ni tofauti kidogo zaidi na 1 ni tofauti zaidi kabisa. Ni thamani gani inafaa zaidi kwa programu yako?

## Kazi Nzuri! Endelea Kujifunza

Baada ya kumaliza somo hili, tembelea [Mkusanyiko wa Kujifunza AI ya Kizazi](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendeleza maarifa yako ya AI ya Kizazi!

Nenda Somo la 7 ambapo tutaangalia jinsi ya [kujenga programu za mazungumzo](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->