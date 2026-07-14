# Kujenga Programu za Utoaji wa Maandishi

[![Kujenga Programu za Utoaji wa Maandishi](../../../translated_images/sw/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Bonyeza picha hapo juu kutazama video ya somo hili)_

Umeona hadi sasa kupitia mtaala huu kwamba kuna dhana msingi kama vile maelekezo na hata somo zima linaloitwa "uhandisi wa maelekezo". Zana nyingi unazoweza kuingiliana nazo kama ChatGPT, Office 365, Microsoft Power Platform na zaidi, zinakusaidia kutumia maelekezo kufanikisha jambo fulani.

Ili kuongeza uzoefu kama huo kwenye programu, unahitaji kuelewa dhana kama maelekezo, ukamilishaji na kuchagua maktaba ya kufanya kazi nayo. Hilo ndilo hasa utalojifunza katika sura hii.

## Utangulizi

Katika sura hii, utajifunza:

- Kujifunza kuhusu maktaba ya openai na dhana zake msingi.
- Kujenga programu ya utoaji wa maandishi kwa kutumia openai.
- Kuelewa jinsi ya kutumia dhana kama maelekezo, joto, na tokeni kujenga programu ya utoaji wa maandishi.

## Malengo ya kujifunza

Mwishoni mwa somo hili, utaweza:

- Eleza ni nini programu ya utoaji wa maandishi.
- Kujenga programu ya utoaji wa maandishi kwa kutumia openai.
- Sanidi programu yako kutumia tokeni nyingi au chache pia kubadilisha joto, kwa matokeo yanayobadilika.

## Ni nini programu ya utoaji wa maandishi?

Kawaida unaporounda programu huwa na aina fulani ya kiolesura kama ifuatavyo:

- Inayotumia amri. Programu za console ni programu za kawaida ambapo unaandika amri na hufanya kazi fulani. Kwa mfano, `git` ni programu inayotumia amri.
- Kiolesura cha mtumiaji (UI). Baadhi ya programu zina violesura vya picha (GUI) ambapo una bonyeza vifungo, ingiza maandishi, chagua chaguzi na zaidi.

### Programu za console na UI zina vikwazo

Linganisha na programu inayotumia amri ambapo unaandika amri:

- **Ina vikwazo**. Huwezi tu kuandika amri yoyote, ni zile ambazo programu inaziiunga mkono tu.
- **Lugha maalum**. Baadhi ya programu zinaunga mkono lugha nyingi, lakini kwa kawaida programu imejengwa kwa lugha maalum, hata kama unaweza kuongeza lugha zaidi.

### Faida za programu za utoaji wa maandishi

Hivyo basi, programu ya utoaji wa maandishi ni tofauti vipi?

Katika programu ya utoaji wa maandishi, una uhuru zaidi, huna vikwazo vya amri fulani au lugha ya kuingiza mahsusi. Badala yake, unaweza kutumia lugha ya asili kuingiliana na programu. Faida nyingine ni kwamba tayari unaingiliana na chanzo cha data ambacho kimefundishwa kwa maktaba kubwa ya taarifa, badala ya programu ya kawaida ambayo inaweza kuwa na vikwazo kwa kile kilicho kwenye hifadhidata.

### Na nini naweza kujenga na programu ya utoaji wa maandishi?

Kuna mambo mengi unaweza kujenga. Kwa mfano:

- **Chatbot**. Chatbot inayojibu maswali kuhusu mada, kama kampuni yako na bidhaa zake inaweza kuwa chaguo zuri.
- **Msaidizi**. LLM ni nzuri katika mambo kama kufupisha maandishi, kupata ufahamu kutoka maandishi, kuzalisha maandishi kama wasifu na zaidi.
- **Msaidizi wa msimbo**. Kutegemea mfano wa lugha unayotumia, unaweza kujenga msaidizi wa kuandika msimbo ambayo itakusaidia kuandika msimbo. Kwa mfano, unaweza kutumia bidhaa kama GitHub Copilot pamoja na ChatGPT kusaidia kuandika msimbo.

## Naweza kuanza vipi?

Naam, unahitaji kupata njia ya kuungana na LLM ambako kawaida inahusisha njia mbili zifuatazo:

- Tumia API. Hapa unajenga maombi ya wavuti kwa maelekezo yako na kupata maandishi yaliyotolewa nyuma.
- Tumia maktaba. Maktaba husaidia kujumuisha wito za API na kuziweka rahisi kutumia.

## Maktaba/SDKs

Kuna maktaba chache maarufu za kufanya kazi na LLM kama vile:

- **openai**, maktaba hii hufanya iwe rahisi kuungana na mfano wako na kutuma maelekezo.

Kisha kuna maktaba zinazofanya kazi kwa ngazi ya juu kama vile:

- **Langchain**. Langchain ni maarufu na inaunga mkono Python.
- **Semantic Kernel**. Semantic Kernel ni maktaba ya Microsoft inayounga mkono lugha za C#, Python, na Java.

## Programu ya kwanza kutumia openai

Tuchukulie jinsi ya kujenga programu yetu ya kwanza, ni maktaba zipi tunazohitaji, kiasi gani kinahitajika na kadhalika.

### Sakinisha openai

Kuna maktaba nyingi huko nje ya kuingiliana na OpenAI au Azure OpenAI. Inawezekana kutumia lugha nyingi za programu kama vile C#, Python, JavaScript, Java na zaidi. Tumetumia maktaba ya Python `openai`, hivyo tutatumia `pip` kuisakinisha.

```bash
pip install openai
```

### Unda rasilimali

Unapaswa kufanya hatua zifuatazo:

- Unda akaunti kwenye Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Pata ruhusa ya Azure OpenAI. Nenda [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) na omba ruhusa.

  > [!NOTE]
  > Wakati wa kuandika, unahitaji kuomba ruhusa ya Azure OpenAI.

- Sakinisha Python <https://www.python.org/>
- Kuwa umeunda rasilimali ya Azure OpenAI Service. Tazama mwongozo huu wa jinsi ya [kuunda rasilimali](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Tafuta funguo za API na kiunganishi

Kwa sasa, unahitaji kusema maktaba yako ya `openai` ni funguo gani za API itumie. Ili kupata funguo zako za API, nenda sehemu ya "Keys and Endpoint" ya rasilimali yako ya Azure OpenAI na nakili thamani ya "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Sasa baada ya kuwa na taarifa hii, tuelekeze maktaba zitumie.

> [!NOTE]
> Ni vyema kutenga funguo zako za API kutoka kwenye msimbo wako. Unaweza kufanya hivyo kwa kutumia mabadiliko ya mazingira.
>
> - Weka mabadiliko ya mazingira `OPENAI_API_KEY` na funguo zako za API.
>   `export OPENAI_API_KEY='sk-...'`

### Sanidi usanidi Azure

Ikiwa unatumia Azure OpenAI (sasa ni sehemu ya Microsoft Foundry), hapa ndio jinsi ya kusanidi. Tunatumia mteja wa kawaida `OpenAI` ulioelekezwa kwenye kiunganishi cha Azure OpenAI `/openai/v1/`, kinachofanya kazi na API ya Majibu bila kuhitaji `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Juu tunaweka yafuatayo:

- `api_key`, hii ni funguo zako za API ulizopata kwenye Azure Portal au Microsoft Foundry portal.
- `base_url`, hii ni kiunganishi cha rasilimali yako ya Foundry kikiwa na `/openai/v1/` kilichowekwa. Kiunganishi imara cha v1 hufanya kazi kwa OpenAI na Azure OpenAI bila usimamizi wa `api_version`.

> [!NOTE] > `os.environ` husoma mabadiliko ya mazingira. Unaweza kuitumia kusoma mabadiliko kama `AZURE_OPENAI_API_KEY` na `AZURE_OPENAI_ENDPOINT`. Weka mabadiliko haya kwenye terminal yako au kwa kutumia maktaba kama `dotenv`.

## Tengeneza maandishi

Njia ya kutengeneza maandishi ni kutumia API ya Majibu kupitia njia `responses.create`. Hapa kuna mfano:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # huu ni jina la usambazaji wa mfano wako
    input=prompt,
    store=False,
)
print(response.output_text)
```

Katika msimbo hapo juu, tunaunda jibu na kupitisha mfano tunayotaka kutumia pamoja na maelekezo. Kisha tunachapisha maandishi yaliyotengenezwa kupitia `response.output_text`.

### Mazungumzo ya mizunguko mingi

API ya Majibu ni nzuri kwa ajili ya utoaji wa maandishi wa mizunguko ya single na chatbot za mizunguko mingi - unatoa orodha ya ujumbe katika `input` kujenga mazungumzo:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

Zaidi kuhusu kazi hii katika sura ijayo.

## Mazoezi - programu yako ya kwanza ya utoaji wa maandishi

Sasa tumepata jinsi ya kusanidi na kuanzisha openai, ni wakati wa kujenga programu yako ya kwanza ya utoaji wa maandishi. Ili kujenga programu yako, fuata hatua hizi:

1. Unda mazingira ya mtandao na sakinisha openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Ikiwa unatumia Windows andika `venv\Scripts\activate` badala ya `source venv/bin/activate`.

   > [!NOTE]
   > Tafuta funguo zako za Azure OpenAI kwa kwenda [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) na tafuta `Open AI` kisha chagua `Open AI resource` na baadae chagua `Keys and Endpoint` nakili thamani ya `Key 1`.

1. Unda faili _app.py_ na uweke msimbo ufuatao:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # ongeza msimbo wako wa kukamilisha
   prompt = "Complete the following: Once upon a time there was a"

   # tengeneza ombi ukitumia API ya Majibu
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # chapisha jibu
   print(response.output_text)
   ```

   > [!NOTE]
   > Ikiwa unatumia OpenAI wa kawaida (si Azure), tumia `client = OpenAI(api_key="<badilisha hii na funguo yako ya OpenAI>")` (bila `base_url`) na pitia jina la mfano kama `gpt-4o-mini` badala ya jina la uenezi.

   Utapata matokeo kama yafuatayo:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Aina tofauti za maelekezo, kwa mambo tofauti

Sasa umeona jinsi ya kuunda maandishi kwa kutumia maelekezo. Hata una programu inayotumika ambayo unaweza kurekebisha na kubadilisha kutoa aina tofauti za maandishi.

Maelekezo yanaweza kutumika kwa kazi mbalimbali. Kwa mfano:

- **Toa aina ya maandishi**. Kwa mfano, unaweza kuunda shairi, maswali ya kizzo n.k.
- **Tafuta taarifa**. Unaweza kutumia maelekezo kutafuta taarifa kama mfano 'CORS ina maana gani katika maendeleo ya wavuti?'.
- **Tengeneza msimbo**. Unaweza kutumia maelekezo kuunda msimbo, kwa mfano kutengeneza mlinganyo wa kawaida (regular expression) unaotumika kuthibitisha barua pepe au kwa nini usitumie kuunda programu nzima, kama programu ya wavuti?

## Mfano wa matumizi halisi: mtoaji wa mapishi

Fikiria una viungo nyumbani na unataka kupika kitu. Kwa hayo, unahitaji mapishi. Njia ya kupata mapishi ni kutumia injini ya utafutaji au unaweza kutumia LLM kufanya hivyo.

Unaweza kuandika maelekezo kama hii:

> "Nionyeshe mapishi 5 ya chakula chenye viungo vifuatavyo: kuku, viazi, na karoti. Kwa kila mapishi, orodhesha viungo vyote vilivyotumika"

Kulingana na maelekezo hapo juu, unaweza kupata jibu kama ifuatavyo:

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

Matokeo haya ni mazuri, najua nini kupika. Kwa sasa, maboresho yanayoweza kuwa na manufaa ni:

- Kuchuja viungo ambavyo sipendi au nina mzio navyo.
- Tengeneza orodha ya ununuzi, ikiwa sina baadhi ya viungo nyumbani.

Kwa hali hizi, tutaongeza maelekezo ya ziada:

> "Tafadhali toa mapishi yenye vitunguu kama mimi nina mzio na badilisha na kitu kingine. Pia, tafadhali tengeneza orodha ya ununuzi kwa mapishi haya, nikizingatia tayari nina kuku, viazi na karoti nyumbani."

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

Haya ni mapishi yako matano, bila vitunguu na pia una orodha ya ununuzi ikizingatia kile ulicho nacho nyumbani.

## Mazoezi - jenga mtoaji wa mapishi

Sasa tunapoenda kuonesha hali, andika msimbo unaoendana na hali hii iliyoonyesha. Ili kufanya hivyo, fuata hatua hizi:

1. Tumia faili _app.py_ ulilolotumia kama taasisi
1. Tafuta kipengele cha `prompt` na badilisha msimbo wake kuwa ufuatao:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Ikiwa sasa utaendesha msimbo, utapaswa kuona matokeo yanayofanana na:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > KUMBUKA, LLM yako sio ya utabiri wa moja kwa moja, hivyo unaweza kupata matokeo tofauti kila mara unapoendesha programu.

   Nzuri, tuangalie jinsi tunavyoweza kuboresha mambo. Ili kuboresha, tunataka kuhakikisha msimbo ni rahisi kubadilika, hivyo viungo na idadi ya mapishi vinaweza kuboreshwa na kubadilishwa.

1. Tubadilishe msimbo kwa njia zifuatazo:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # weka idadi ya mapishi katika maelekezo na viambato
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Kuchukua msimbo kwa ajili ya majaribio ya mtihani, inaweza kuonekana kama hii:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Boreshaji kwa kuongeza kichujio na orodha ya ununuzi

Sasa tuna programu inayofanya kazi inayoweza kuzalisha mapishi na ni rahisi kwa kuwa inategemea ingizo kutoka kwa mtumiaji, kwa idadi ya mapishi na pia viungo vilivyotumika.

Ili kuboresha zaidi, tunataka kuongeza yafuatayo:

- **Chuja viungo**. Tunataka kuwa na uwezo wa kuchuja viungo ambavyo hatupendi au tuna mzio navyo. Ili kufanikisha hili, tunaweza kuhariri maelekezo yetu ya sasa na kuongeza sharti la kuchuja mwishoni kama hii:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Juu tunaongeza `{filter}` mwishoni mwa maelekezo na pia tunachukua thamani ya kichujio kutoka kwa mtumiaji.

  Mfano wa ingizo wa kuendesha programu sasa unaweza kuwa kama ifuatavyo:

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

  Kama unavyoweza kuona, mapishi yoyote yenye maziwa yametolewa. Lakini, ikiwa una matatizo ya kusaga maziwa kidogo, unaweza pia kuchuja mapishi yenye jibini ndani yao, hivyo kuna haja ya kuwa wazi.


- **Tengeneza orodha ya manunuzi**. Tunataka kutengeneza orodha ya manunuzi, tukizingatia kile tunachokipata tayari nyumbani.

  Kwa ajili ya utendaji huu, tunaweza kujaribu kutatua kila kitu kwa ombi moja au tunaweza kugawanya kuwa maombi mawili. Tujaribu njia ya pili. Hapa tunapendekeza kuongeza ombi la ziada, lakini ili kufanya kazi hiyo, tunahitaji kuongeza matokeo ya ombi la kwanza kama muktadha kwa ombi la pili.

  Tafuta sehemu katika msimbo inayochapisha matokeo kutoka kwa ombi la kwanza kisha ongeza msimbo ufuatao hapa chini:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # chapisha jibu
  print("Shopping list:")
  print(response.output_text)
  ```

  Kumbuka yafuatayo:

  1. Tunajenga ombi jipya kwa kuongeza matokeo ya ombi la kwanza kwenye ombi mpya:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Tunafanya ombi jipya, lakini pia tukizingatia idadi ya tokeni tulizoomba katika ombi la kwanza, kwa hiyo wakati huu tunasema `max_output_tokens` ni 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Tukichukua msimbo huu kwa jaribio, sasa tunapata matokeo yafuatayo:

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

Tunachonacho hadi sasa ni msimbo unaofanya kazi, lakini kuna marekebisho ambayo tunapaswa kufanya ili kuboresha zaidi. Baadhi ya mambo tunayopaswa kufanya ni:

- **Tofautisha siri kutoka kwa msimbo**, kama kitufe cha API. Siri hazipaswi kuwepo katika msimbo na zinapaswa kuhifadhiwa mahali salama. Ili kutofautisha siri kutoka msimbo, tunaweza kutumia mabadiliko ya mazingira na maktaba kama `python-dotenv` kuziweka kutoka kwenye faili. Hivyo ndivyo itakavyoonekana kwenye msimbo:

  1. Unda faili `.env` yenye maudhui yafuatayo:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Kumbuka, kwa Azure OpenAI katika Microsoft Foundry, unahitaji kuweka mabadiliko ya mazingira yafuatayo badala yake:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Katika msimbo, ungepakua mabadiliko ya mazingira kama ifuatavyo:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Neno kuhusu urefu wa tokeni**. Tunapaswa kuzingatia ni tokeni ngapi tunazohitaji kuzalisha maandishi tunayoyataka. Tokeni huhitaji pesa, hivyo pale ambapo inawezekana, tunapaswa kuwa makini na idadi ya tokeni tunazotumia. Kwa mfano, je, tunaweza kuweka ombi kwa njia ambayo tunatumia tokeni chache?

  Kubadilisha tokeni zinazotumiwa, unaweza kutumia parameta ya `max_output_tokens`. Kwa mfano, ukitaka kutumia tokeni 100, ungefanya kama ifuatavyo:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Jaribio na joto**. Joto ni kitu ambacho hatujazungumzia hapo awali lakini ni muktadha muhimu kwa jinsi programu yetu inavyofanya kazi. Kadiri thamani ya joto inavyoongezeka ndivyo matokeo yanavyokuwa ya kubahatisha zaidi. Kinyume chake, kadiri thamani ya joto inavyopungua ndivyo matokeo yanavyokuwa yanayoweza kutabirika zaidi. Fikiria kama unataka mabadiliko katika matokeo yako au la.

  Kubadilisha joto, unaweza kutumia parameta ya `temperature`. Kwa mfano, ukitaka kutumia joto la 0.5, ungefanya kama ifuatavyo:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Kumbuka, kadri inavyo karibu na 1.0, ndivyo matokeo yanavyokuwa tofauti zaidi.

## Kazi ya Nyumbani

Kwa kazi hii, unaweza kuchagua nini cha kujenga.

Hapa kuna mapendekezo kadhaa:

- Rekebisha programu ya kizalishaji cha mapishi ili kuboresha zaidi. Jaribu thamani za joto na maombi kuona unaweza kuja na nini.
- Tengeneza “rafiki wa kusoma”. Programu hii inapaswa kuwa na uwezo wa kujibu maswali kuhusu mada kama Python, unaweza kuwa na maombi kama "Ni nini mada fulani katika Python?", au unaweza kuwa na ombi linasema, nionyeshe msimbo wa mada fulani n.k.
- Bot wa historia, fanya historia iwe hai, elekeza bot kucheza kama mhusika fulani wa kihistoria na umuulize maswali kuhusu maisha na nyakati zake.

## Suluhisho

### Rafiki wa Kusoma

Hapa chini ni ombi la kuanzia, angalia jinsi unavyoweza kulitumia na kulibadilisha upendavyo.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot wa Historia

Hapa kuna baadhi ya maombi unaweza kutumia:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Angalia Maarifa

Dhana ya joto hufanya nini?

1. Huidhibiti jinsi matokeo yanavyokuwa ya kubahatisha.
1. Huidhibiti ukubwa wa jibu.
1. Huidhibiti ni tokeni ngapi zinapotumika.

## 🚀 Changamoto

Unapofanya kazi kwenye kazi ya nyumbani, jaribu kubadilisha joto, jaribu kuweka 0, 0.5, na 1. Kumbuka 0 ni tofauti kidogo na 1 ni tofauti zaidi. Ni thamani gani inafanya kazi vizuri kwa programu yako?

## Kazi Nzuri! Endelea Kujifunza

Baada ya kumaliza somo hili, angalia [Mkusanyiko wetu wa Mafunzo ya AI Inayozalisha](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili kuendeleza ujuzi wako wa AI Inayozalisha!

Nenda kwenye Somo la 7 ambapo tutatazama jinsi ya [kujenga programu za mazungumzo](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->