# Kujenga Programu za Uundaji wa Maandishi

[![Kujenga Programu za Uundaji wa Maandishi](../../../translated_images/sw/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Bofya picha iliyo juu ili kuona video ya somo hili)_

Umeona hadi sasa kupitia mitaala hii kwamba kuna dhana msingi kama vile maagizo (prompts) na hata ujuzi mzima unaoitwa "ufunda wa maagizo" (prompt engineering). Zana nyingi unazoweza kutumia kama ChatGPT, Office 365, Microsoft Power Platform na zaidi, zinakuwezesha kutumia maagizo kufanikisha jambo fulani.

Ili kuongeza uzoefu kama huo kwenye programu, unahitaji kuelewa dhana kama maagizo, ukamilishaji na kuchagua maktaba ya kufanya nayo kazi. Hiyo kabisa ndilo utakalojifunza katika sura hii.

## Utangulizi

Katika sura hii, utajifunza:

- Jifunze kuhusu maktaba ya openai na dhana zake za msingi.
- Jenga programu ya uundaji wa maandishi ukitumia openai.
- Elewa jinsi ya kutumia dhana kama maagizo, joto, na tokeni kujenga programu ya uundaji wa maandishi.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- Eleza ni nini programu ya uundaji wa maandishi.
- Jenga programu ya uundaji wa maandishi ukitumia openai.
- Sanidi programu yako kutumia tokeni nyingi zaidi au chache na pia badilisha joto ili upate matokeo mbalimbali.

## Ni nini programu ya uundaji wa maandishi?

Kawaida unapo jenga programu huwa na aina fulani ya kiolesura kama ifuatavyo:

- Inayotegemea amri. Programu za console ni programu za kawaida ambapo unaandika amri na hufanya kazi fulani. Kwa mfano, `git` ni programu inayotegemea amri.
- Kiolesura cha mtumiaji (UI). Baadhi ya programu zina kiolesura cha picha (GUIs) ambapo una bonyeza vitufe, ingiza maandishi, chagua chaguzi na zaidi.

### Programu za console na UI zina mipaka

Linganisha na programu inayotegemea amri ambapo unaandika amri:

- **Ina mipaka**. Huwezi kuandika amri yoyote ile, ni zile tu programu inaunga mkono.
- **Lugha maalum**. Baadhi ya programu zinaunga mkono lugha nyingi, lakini kwa kawaida programu imetengenezwa kwa lugha fulani, hata kama unaweza kuongeza msaada wa lugha zaidi.

### Faida za programu za uundaji wa maandishi

Basi je, programu ya uundaji wa maandishi ni tofauti vipi?

Katika programu ya uundaji wa maandishi, una uhuru zaidi, huna mipaka ya amri maalum wala lugha maalum ya kuingiza. Badala yake, unaweza kutumia lugha ya asili kuingiliana na programu. Faida nyingine ni kwamba tayari unakutana na chanzo cha data kilichofunzwa na makusanyo makubwa ya taarifa, wakati programu ya kawaida inaweza kuwa na mipaka kuhusu inayo katika hifadhidata.

### Naweza kujenga nini kwa kutumia programu ya uundaji wa maandishi?

Kuna mambo mengi unayoweza kujenga. Kwa mfano:

- **Chatbot**. Chatbot inayojibu maswali kuhusu mada, kama kampuni yako na bidhaa zake inaweza kuwa chaguo zuri.
- **Msaidizi**. LLM ni zuri kwa mambo kama muhtasari wa maandishi, kupata maarifa kutoka maandishi, kuandika maandishi kama wasifu na zaidi.
- **Msaidizi wa nambari (Code assistant)**. Kutegemea mfano wa lugha unaotumia, unaweza kujenga msaidizi wa nambari anayekusaidia kuandika msimbo. Kwa mfano, unaweza kutumia bidhaa kama GitHub Copilot pamoja na ChatGPT kusaidia kuandika msimbo.

## Ninaanza vipi?

Vizuri, unahitaji njia ya kuunganishwa na LLM ambayo kawaida inajumuisha mbinu mbili zifuatazo:

- Tumia API. Hapa unaunda maombi ya mtandao kwa kutumia agizo lako na kurudiwa maandishi yaliyoandaliwa.
- Tumia maktaba. Maktaba husaidia kufungasha mwito wa API na kuufanya kuwa rahisi kutumia.

## Maktaba/SDKs

Kuna maktaba kadhaa maarufu kwa kufanya kazi na LLM kama:

- **openai**, maktaba hii hufanya iwe rahisi kuungana na mfano wako na kutuma maagizo.

Kisha kuna maktaba zinazofanya kazi kwa kiwango cha juu kama:

- **Langchain**. Langchain ni maarufu na inaunga mkono Python.
- **Semantic Kernel**. Semantic Kernel ni maktaba ya Microsoft inayounga mkono lugha za C#, Python, na Java.

## Programu ya kwanza ukitumia openai

Tutaona jinsi ya kujenga programu yetu ya kwanza, maktaba tunazohitaji, kiasi kinachohitajika na kadhalika.

### Sakinisha openai

Kuna maktaba nyingi za kuingiliana na OpenAI au Azure OpenAI. Inawezekana kutumia lugha mbalimbali za programu kama C#, Python, JavaScript, Java na zaidi. Tumetumia maktaba ya Python `openai`, hivyo tutatumia `pip` kuiweka.

```bash
pip install openai
```

### Unda rasilimali

Unahitaji kufanya hatua zifuatazo:

- Unda akaunti kwenye Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Pata ruhusa ya Azure OpenAI. Tembelea [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) na omba ruhusa.

  > [!NOTE]
  > Wakati wa kuandika, unahitaji kuomba ruhusa ya Azure OpenAI.

- Sakinisha Python <https://www.python.org/>
- Kuwa umeunda rasilimali ya Azure OpenAI Service. Angalia mwongozo huu wa jinsi ya [kuunda rasilimali](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Pata ufunguo wa API na njia ya kuunganishwa

Sasa, unahitaji kumwambia maktaba yako ya `openai` ni ufunguo gani wa API utakaotumia. Ili kupata ufunguo wako wa API, nenda kwenye sehemu ya "Keys and Endpoint" ya rasilimali yako ya Azure OpenAI na nakili thamani ya "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Sasa baada ya kupata taarifa hii, tuelekeze maktaba ziitumi.

> [!NOTE]
> Inafaa kutenganisha ufunguo wako wa API na msimbo wako. Unaweza kufanya hivyo kwa kutumia mazingira ya mazingira (environment variables).
>
> - Weka thamani ya mazingira `OPENAI_API_KEY` kwa ufunguo wako wa API.
>   `export OPENAI_API_KEY='sk-...'`

### Sanidi usanidi Azure

Ikiwa unatumia Azure OpenAI (sasa sehemu ya Microsoft Foundry), hapa ni jinsi unavyosaidia usanidi. Tunatumia mteja halisi `OpenAI` unaoelekezwa kwenye pini ya Azure OpenAI `/openai/v1/`, inayofanya kazi na API ya Majibu na haidingi `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Juu hapa tunaweka yafuatayo:

- `api_key`, huu ni ufunguo wako wa API uliopatikana kwenye Azure Portal au portal ya Microsoft Foundry.
- `base_url`, ni mwisho wa rasilimali yako Foundry ukiambatanisha `/openai/v1/`. Pini imara ya v1 hufanya kazi kwa OpenAI na Azure OpenAI bila usimamizi wa `api_version`.

> [!NOTE] > `os.environ` huchukua thamani za mazingira. Unaweza kuitumia kusoma mazingira kama `AZURE_OPENAI_API_KEY` na `AZURE_OPENAI_ENDPOINT`. Weka thamani hizi za mazingira kwenye terminal yako au kwa kutumia maktaba kama `dotenv`.

## Tengeneza maandishi

Njia ya kutengeneza maandishi ni kutumia API ya Majibu kupitia njia ya `responses.create`. Hapa kuna mfano:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # huu ndio jina la usambazaji wa mfano wako
    input=prompt,
    store=False,
)
print(response.output_text)
```

Katika msimbo huo hapo juu, tunaunda jibu na kuingiza mfano tunayotaka kutumia na agizo. Kisha tuna chapisha maandishi yaliyotengenezwa kupitia `response.output_text`.

### Mazungumzo ya mzunguko wengi

API ya Majibu inafaa vizuri kwa uundaji wa maandishi wa zamu moja na pia chatbots za mzunguko mingi - unatoa orodha ya ujumbe katika `input` kujenga mazungumzo:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Zaidi juu ya kazi hii katika sura ijayo.

## Zoefu - programu yako ya kwanza ya uundaji wa maandishi

Sasa tunapo jifunza jinsi ya kusanidi na usanidi openai, ni wakati wa kujenga programu yako ya kwanza ya uundaji wa maandishi. Kufanya hivyo, fuata hatua hizi:

1. Unda mazingira halisi (virtual environment) na sakinisha openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Ikiwa unatumia Windows andika `venv\Scripts\activate` badala ya `source venv/bin/activate`.

   > [!NOTE]
   > Pata ufunguo wako wa Azure OpenAI kwa kwenda [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) kisha tafuta `Open AI` na chagua `Open AI resource` kisha chagua `Keys and Endpoint` na nakili thamani ya `Key 1`.

1. Unda faili _app.py_ na uweke msimbo huu:

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

   # fanya ombi kwa kutumia API za Majibu
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # chapisha jibu
   print(response.output_text)
   ```

   > [!NOTE]
   > Ikiwa unatumia OpenAI wa kawaida (si Azure), tumia `client = OpenAI(api_key="<badilisha thamani hii kwa ufunguo wako wa OpenAI>")` (bila `base_url`) na toa jina la mfano kama `gpt-5-mini` badala ya jina la utoaji.

   Utakuwa unaona matokeo kama ifuatavyo:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Aina tofauti za maagizo, kwa mambo tofauti

Sasa umeona jinsi ya kutengeneza maandishi kwa kutumia agizo. Hata una programu inayotembea na unayoweza kubadilisha ili kupata aina tofauti za maandishi.

Maagizo yanaweza kutumika kwa kazi mbalimbali. Kwa mfano:

- **Tengeneza aina ya maandishi**. Kwa mfano, unaweza kuunda shairi, maswali kwa mtihani n.k.
- **Tafuta taarifa**. Unaweza kutumia maagizo kutafuta taarifa kama mfano huu 'CORS inamaanisha nini katika maendeleo ya wavuti?'.
- **Tengeneza msimbo**. Unaweza kutumia maagizo kutengeneza msimbo, kwa mfano kuunda regex ya kuthibitisha barua pepe au kwa nini si kuzalisha programu yote, kama programu ya wavuti?

## Mfano wa matumizi wa vitendo: kizalishaji cha mapishi

Fikiria una viungo nyumbani na unataka kupika kitu. Kwa hilo, unahitaji mapishi. Njia moja ya kupata mapishi ni kutumia mtambo wa kutafuta au unaweza kutumia LLM kufanya hivyo.

Unaweza kuandika agizo kama ifuatavyo:

> "Nioneshie mapishi 5 ya chakula chenye viungo vifuatavyo: kuku, viazi, na karoti. Kwa kila mapishi, orodhesha viungo vyote vilivyotumika"

Kutokana na agizo hapo juu, unaweza kupata jibu kama hii:

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

Matokeo haya ni mazuri, najua nini kupika. Sasa, mabadiliko yanayoweza kuwa na msaada ni:

- Kuchuja viungo ambavyo sipendi au nina mzio navyo.
- Tengeneza orodha ya manunuzi, endapo sina viungo vyote nyumbani.

Kwa hali hizi, tutaongeza agizo la ziada:

> "Tafadhali toa mapishi yenye vitunguu nusu kama nina mzio na badilisha na kitu kingine. Pia, tafadhali tengeneza orodha ya manunuzi kwa mapishi, ukizingatia kuwa tayari nina kuku, viazi na karoti nyumbani."

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

Haya ni mapishi yako matano, bila vitunguu na pia una orodha ya manunuzi ikizingatia unavyo viungo nyumbani.

## Zoefu - jenga kizalishaji cha mapishi

Sasa tumetumia mfano, andika msimbo kuendana na mfano huu. Kufanya hivyo, fuata hatua hizi:

1. Tumia faili lililopo la _app.py_ kama msingi
1. Tafuta mabadiliko ya `prompt` na badilisha msimbo wake kama ifuatavyo:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Ikiwa utaendesha msimbo sasa, utapata matokeo kama haya:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > KUMBUKA, LLM yako si ya kudhibitiwa kwa hakika, hivyo matokeo yanaweza kutofautiana kila unapoendesha programu.

   Vizuri, tuchunguze jinsi ya kuboresha mambo. Ili kuboresha, tunataka msimbo uwe rahisi kubadilishwa, viungo na idadi ya mapishi ziweze kurekebishwa.

1. Badilisha msimbo kama ifuatavyo:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # weka idadi ya mapishi katika maelekezo na viungo
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Kuendesha msimbo kama jaribio, unaweza kufanya hivi:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Boreshaji kwa kuongeza kichujio na orodha ya manunuzi

Sasa tuna programu inayofanya kazi ya kuunda mapishi na ni rahisi kwa sababu inategemea viingilio kutoka kwa mtumiaji, sehemu ya idadi ya mapishi na pia viungo vilivyotumika.

Ili kurekebisha zaidi, tunataka kuongeza yafuatayo:

- **Chuja viungo**. Tunataka kuwa na uwezo wa kuchuja viungo ambavyo hatupendi au tuna mzio navyo. Ili kufanya hivyo, tunaweza kuhariri agizo letu lililopo na kuongeza sharti la chujio mwishoni kama ifuatavyo:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Juu hapa, tunaongeza `{filter}` mwishoni mwa agizo na pia tunapata thamani ya chujio kutoka kwa mtumiaji.

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

  Kama unavyoona, mapishi yote yenye maziwa yametolewa. Lakini, ikiwa una intoleransi ya lactose, unaweza pia kutaka kuchuja mapishi yenye jibini, hivyo kuna haja ya kuwa wazi zaidi.


- **Tengeneza orodha ya ununuzi**. Tunataka kutengeneza orodha ya ununuzi, tukiangalia kile tulicho nacho tayari nyumbani.

  Kwa ajili ya utendaji huu, tunaweza kujaribu kutatua kila kitu kwa papo moja au tunaweza kuigawanya katika maprompt mawili. Tujaribu njia ya mwisho. Hapa tunapendekeza kuongeza prompt nyingine, lakini ili ifanye kazi, tunahitaji kuongeza matokeo ya prompt ya kwanza kama muktadha kwa prompt ya pili.

  Tafuta sehemu katika msimbo inayochapisha matokeo kutoka kwa prompt ya kwanza na ongeza msimbo ufuatao hapo chini:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # chapisha mwitikio
  print("Shopping list:")
  print(response.output_text)
  ```

  Kumbuka yafuatayo:

  1. Tunajenga prompt mpya kwa kuongeza matokeo kutoka kwa prompt ya kwanza kwenye prompt mpya:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Tunafanya ombi jipya, lakini pia tukiwa na kuzingatia idadi ya tokeni tuliyoomba kwenye prompt ya kwanza, kwa hivyo wakati huu tunasema `max_output_tokens` ni 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Tunapotumia msimbo huu, sasa tunapata matokeo yafuatayo:

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

Kile tulicho nacho mpaka sasa ni msimbo unaofanya kazi, lakini kuna marekebisho kadhaa tunapaswa kufanya ili kuboresha zaidi. Baadhi ya mambo tunapaswa kufanya ni:

- **Tenganisha siri kutoka kwenye msimbo**, kama funguo za API. Siri hazipaswi kuwekwa ndani ya msimbo na zinapaswa kuhifadhiwa mahali salama. Ili kutenganisha siri na msimbo, tunaweza kutumia vinasaba vya mazingira na maktaba kama `python-dotenv` kuzisoma kutoka kwenye faili. Hivi ndivyo inavyoweza kuonekana kwenye msimbo:

  1. Unda faili `.env` yenye yaliyomo yafuatayo:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Kumbuka, kwa Azure OpenAI katika Microsoft Foundry, unahitaji kuweka vinasaba vya mazingira vifuatavyo badala yake:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Katika msimbo, utawala vinasaba vya mazingira hivi kwa njia ifuatayo:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Neno kuhusu urefu wa tokeni**. Tunapaswa kuzingatia ni tokeni ngapi tunahitaji kuzalisha maandishi tunayoyataka. Tokeni zinagharimu pesa, kwa hivyo pale inapowezekana, tunapaswa kujitahidi kuwa na uhifadhi katika idadi ya tokeni tunazotumia. Kwa mfano, tunaweza kupanga prompt ili itumie tokeni chache?

  Kubadilisha tokeni zinazotumika, unaweza kutumia parameter `max_output_tokens`. Kwa mfano, ikiwa unataka kutumia tokeni 100, ungefanya:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Jaribu na joto (temperature)**. Joto ni jambo ambalo hatujawahi kulitaja hadi sasa lakini ni muktadha muhimu kwa jinsi programu yetu inavyofanya kazi. Thamani ya juu ya joto hufanya matokeo kuwa ya bahati zaidi. Kinyume chake, thamani ya chini ya joto hufanya matokeo kuwa yanayotabirika zaidi. Fikiria kama unataka mabadiliko katika matokeo yako au la.

  Kubadilisha joto, unaweza kutumia parameter ya `temperature`. Kwa mfano, ikiwa unataka kutumia joto la 0.5, ungefanya:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Kumbuka, kadri unavyokaribia 1.0, ndivyo matokeo yanavyobadilika zaidi.

- **Modeli za kufikiri hazitumi `temperature`**. Hii ni mabadiliko muhimu ya mwaka 2026. Modeli za sasa, zisizotumika tena Microsoft Foundry ni **modeli za kufikiri** (familia ya GPT-5, mfululizo o) - na hazitumi `temperature` au `top_p` (wala `max_tokens`; tumia `max_output_tokens`). Ikiwa utatumia `temperature` kwa `gpt-5-mini` utapata kosa la "parameter haitegemezwi". Hivyo jaribu mfano wa joto hapo juu kwa kutumia modeli inayounga mkono udhibiti wa sampuli - kwa mfano modeli ya wazi ya **Llama** kama `Llama-3.3-70B-Instruct` kutoka kwenye [katalogi ya modeli ya Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), inayopatikana kupitia Foundry Models / Azure AI Inference endpoint (sawa na sampuli za `githubmodels-*`). Kwa modeli za kufikiri kama GPT-5, unadhibiti matokeo kwa njia tofauti:
  - **Uhandisi wa prompt** - maelekezo wazi, mifano, na muundo wa matokeo (angalia somo [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) hufanya kazi ambayo vipimo vya sampuli vilifanya awali.
  - **Udhibiti wa fikira** - vigezo kama juhudi ya kufikiri/kubwa wa maelezo hutenganisha kina cha fikira dhidi ya muda wa majibu na gharama.

  Kwa kifupi: `temperature`/`top_p` bado ni halali kwenye modeli nyingi (Llama, Mistral, Phi, na familia ya GPT-4.x - ingawa GPT-4.x inaachwa), lakini mwelekeo wa maendeleo ni uhandisi wa prompt + udhibiti wa fikira kwenye modeli za kufikiri kama GPT-5.

## Kazi

Kwa kazi hii, unaweza kuchagua kile cha kujenga.

Hapa kuna mapendekezo:

- Rekebisha programu ya mtengenezaji wa mapishi ili kuiboresha zaidi. Jaribu thamani za joto na prompt kuona unachoweza kuja nacho.
- Tengeneza "mwenzi wa kusomea". Programu hii inapaswa kuwa na uwezo wa kujibu maswali kuhusu mada kama Python, unaweza kuwa na prompt kama "Nini mada fulani katika Python?", au unaweza kuwa na prompt inayosema, nionyeshe msimbo kwa mada fulani nk.
- Roboti wa historia, fanya historia iwe hai, amuru roboti acheze kama mhusika wa kihistoria fulani na umwulize maswali kuhusu maisha yake na nyakati zake.

## Suluhisho

### Mwenzi wa kusomea

Hapo chini ni prompt ya kuanzia, tazama jinsi unavyoweza kuitumia na kuibadilisha mpaka uyapende.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Roboti wa historia

Hapa kuna prompt ambazo unaweza kutumia:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Kagua maarifa

Nini maana ya dhana ya joto (temperature)?

1. Inadhibiti jinsi matokeo yanavyokuwa ya bahati.
1. Inadhibiti ukubwa wa jibu.
1. Inadhibiti ni tokeni ngapi zinatumiwa.

## 🚀 Changamoto

Unapofanya kazi kwenye kazi, jaribu kubadilisha joto, jaribu kulifanya 0, 0.5, na 1. Kumbuka 0 ni tofauti kidogo na 1 ni tofauti zaidi. Ni thamani gani inafanya kazi vizuri zaidi kwa programu yako?

## Kazi Nzuri! Endelea Kujifunza

Baada ya kumaliza somo hili, angalia [Mkusanyiko wa Mafunzo ya AI ya Kizazi kipya](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ili uendelee kuongeza maarifa yako ya AI ya Kizazi kipya!

Nenda kwenye Somo la 7 ambapo tutatazama jinsi ya [kujenga programu za mazungumzo](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->