<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-06-25T14:42:05+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "sw"
}
-->
# Kujenga Programu za Uzalishaji wa Maandishi

> _(Bonyeza picha hapo juu ili kutazama video ya somo hili)_

Mpaka sasa umeshajifunza kuwa kuna dhana za msingi kama vile prompts na hata taaluma nzima inayoitwa "prompt engineering". Zana nyingi unazoweza kuingiliana nazo kama ChatGPT, Office 365, Microsoft Power Platform na zaidi, zinakuunga mkono kutumia prompts kufanikisha jambo fulani.

Ili uweze kuongeza uzoefu kama huo kwenye programu, unahitaji kuelewa dhana kama prompts, completions na kuchagua maktaba ya kufanya kazi nayo. Hicho ndicho utakachojifunza katika sura hii.

## Utangulizi

Katika sura hii, utajifunza:

- Kuhusu maktaba ya openai na dhana zake za msingi.
- Kujenga programu ya uzalishaji wa maandishi ukitumia openai.
- Kuelewa jinsi ya kutumia dhana kama prompt, temperature, na tokens kujenga programu ya uzalishaji wa maandishi.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:

- Kuelezea programu ya uzalishaji wa maandishi ni nini.
- Kujenga programu ya uzalishaji wa maandishi ukitumia openai.
- Kusanidi programu yako kutumia tokens zaidi au chache na pia kubadilisha temperature, kwa matokeo tofauti.

## Programu ya Uzalishaji wa Maandishi ni Nini?

Kwa kawaida unapojenga programu ina aina fulani ya kiolesura kama ifuatavyo:

- Inayotegemea amri. Programu za console ni programu za kawaida ambapo unaandika amri na inafanya kazi fulani. Kwa mfano, `git` ni programu inayotegemea amri.
- Kiolesura cha mtumiaji (UI). Baadhi ya programu zina kiolesura cha picha (GUIs) ambapo unabonyeza vitufe, kuingiza maandishi, kuchagua chaguo na zaidi.

### Programu za Console na UI Zina Mipaka

Linganisha na programu inayotegemea amri ambapo unaandika amri:

- **Ina mipaka**. Huwezi tu kuandika amri yoyote, ni zile tu ambazo programu inasaidia.
- **Maalum kwa lugha**. Baadhi ya programu zinaunga mkono lugha nyingi, lakini kwa chaguo-msingi programu inajengwa kwa lugha maalum, hata kama unaweza kuongeza msaada wa lugha zaidi.

### Faida za Programu za Uzalishaji wa Maandishi

Kwa hiyo programu ya uzalishaji wa maandishi ina tofauti gani?

Katika programu ya uzalishaji wa maandishi, una uhuru zaidi, haujafungwa na seti ya amri au lugha maalum ya kuingiza. Badala yake, unaweza kutumia lugha ya kawaida kuingiliana na programu. Faida nyingine ni kwamba kwa sababu tayari unaingiliana na chanzo cha data ambacho kimefundishwa kwenye mkusanyiko mkubwa wa taarifa, ambapo programu ya kawaida inaweza kuwa na mipaka kwenye kile kilichopo kwenye hifadhidata.

### Naweza Kujenga Nini na Programu ya Uzalishaji wa Maandishi?

Kuna mambo mengi unayoweza kujenga. Kwa mfano:

- **Chatbot**. Chatbot inayojibu maswali kuhusu mada, kama kampuni yako na bidhaa zake inaweza kuwa mechi nzuri.
- **Msaidizi**. LLMs ni nzuri katika vitu kama kufupisha maandishi, kupata maarifa kutoka kwa maandishi, kutoa maandishi kama wasifu na zaidi.
- **Msaidizi wa Kode**. Kulingana na mfano wa lugha unayotumia, unaweza kujenga msaidizi wa kode anayekusaidia kuandika kode. Kwa mfano, unaweza kutumia bidhaa kama GitHub Copilot pamoja na ChatGPT kukusaidia kuandika kode.

## Ninawezaje Kuanza?

Naam, unahitaji kupata njia ya kuunganisha na LLM ambayo kwa kawaida inajumuisha njia mbili zifuatazo:

- Tumia API. Hapa unajenga maombi ya wavuti na prompt yako na unapata maandishi yaliyotengenezwa.
- Tumia maktaba. Maktaba husaidia kuficha miito ya API na kuifanya iwe rahisi kutumia.

## Maktaba/SDKs

Kuna maktaba chache zinazojulikana kwa kufanya kazi na LLMs kama:

- **openai**, maktaba hii inafanya iwe rahisi kuunganisha na mfano wako na kutuma prompts.

Kisha kuna maktaba zinazofanya kazi kwenye kiwango cha juu kama:

- **Langchain**. Langchain inajulikana na inasaidia Python.
- **Semantic Kernel**. Semantic Kernel ni maktaba ya Microsoft inayounga mkono lugha za C#, Python, na Java.

## Programu ya Kwanza Kutumia openai

Tuone jinsi tunavyoweza kujenga programu yetu ya kwanza, ni maktaba gani tunahitaji, ni kiasi gani kinachohitajika na kadhalika.

### Sakinisha openai

Kuna maktaba nyingi huko nje kwa kuingiliana na OpenAI au Azure OpenAI. Inawezekana kutumia lugha nyingi za programu kama C#, Python, JavaScript, Java na zaidi. Tumechagua kutumia maktaba ya `openai` ya Python, hivyo tutatumia `pip` kuiweka.

```bash
pip install openai
```

### Unda Rasilimali

Unahitaji kutekeleza hatua zifuatazo:

- Unda akaunti kwenye Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Pata ufikiaji wa Azure OpenAI. Nenda [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) na omba ufikiaji.

  > [!NOTE]
  > Kwa wakati wa kuandika, unahitaji kuomba ufikiaji wa Azure OpenAI.

- Sakinisha Python <https://www.python.org/>
- Uwe umekamilisha kuunda rasilimali ya Azure OpenAI Service. Tazama mwongozo huu jinsi ya [kuunda rasilimali](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Tafuta Kitufe cha API na Endpoint

Kwa sasa, unahitaji kuambia maktaba yako ya `openai` ni kitufe gani cha API cha kutumia. Ili kupata kitufe chako cha API, nenda kwenye sehemu ya "Keys and Endpoint" ya rasilimali yako ya Azure OpenAI na nakili thamani ya "Key 1".

Sasa kwa kuwa una taarifa hii iliyokopiwa, hebu tuagize maktaba kuitumia.

> [!NOTE]
> Inafaa kutenganisha kitufe chako cha API kutoka kwa kode yako. Unaweza kufanya hivyo kwa kutumia vigezo vya mazingira.
>
> - Weka kigezo cha mazingira `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### Sanidi Usanidi wa Azure

Ikiwa unatumia Azure OpenAI, hivi ndivyo unavyosanidi usanidi:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Hapo juu tunasanidi yafuatayo:

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion` class. Hapa kuna mfano:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

Katika kode hapo juu, tunaunda kitu cha completion na kupitisha mfano tunaotaka kutumia na prompt. Kisha tunachapisha maandishi yaliyotengenezwa.

### Chat completions

Mpaka sasa, umeona jinsi tumekuwa tukitumia `Completion` to generate text. But there's another class called `ChatCompletion` ambayo inafaa zaidi kwa chatbots. Hapa kuna mfano wa kuitumia:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Zaidi juu ya utendaji huu katika sura ijayo.

## Zoezi - programu yako ya kwanza ya uzalishaji wa maandishi

Sasa kwa kuwa tumejifunza jinsi ya kusanidi na kuunganisha openai, ni wakati wa kujenga programu yako ya kwanza ya uzalishaji wa maandishi. Ili kujenga programu yako, fuata hatua hizi:

1. Unda mazingira ya kawaida na usakinishe openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Ikiwa unatumia Windows andika `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` value.

1. Unda faili _app.py_ na uipe kode ifuatayo:

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
   > Ikiwa unatumia Azure OpenAI, unahitaji kuweka `api_type` to `azure` and set the `api_key` kwenye kitufe chako cha Azure OpenAI.

   Unapaswa kuona matokeo kama yafuatayo:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Aina tofauti za prompts, kwa mambo tofauti

Sasa umeona jinsi ya kuzalisha maandishi kwa kutumia prompt. Hata una programu inayoendesha ambayo unaweza kubadilisha na kubadilisha ili kuzalisha aina tofauti za maandishi.

Prompts zinaweza kutumika kwa kazi zote za aina. Kwa mfano:

- **Kuzalisha aina ya maandishi**. Kwa mfano, unaweza kuzalisha shairi, maswali ya mtihani n.k.
- **Kutafuta taarifa**. Unaweza kutumia prompts kutafuta taarifa kama mfano ufuatao 'CORS inamaanisha nini katika ukuzaji wa wavuti?'.
- **Kuzalisha kode**. Unaweza kutumia prompts kuzalisha kode, kwa mfano kuunda usemi wa kawaida unaotumika kuthibitisha barua pepe au kwa nini usizalishe programu nzima, kama programu ya wavuti?

## Kesi ya matumizi ya vitendo zaidi: jenereta ya mapishi

Fikiria una viungo nyumbani na unataka kupika kitu. Kwa hiyo, unahitaji mapishi. Njia ya kupata mapishi ni kutumia injini ya utafutaji au unaweza kutumia LLM kufanya hivyo.

Unaweza kuandika prompt kama hii:

> "Nionyeshe mapishi 5 ya sahani na viungo vifuatavyo: kuku, viazi, na karoti. Kwa kila mapishi, orodhesha viungo vyote vilivyotumika"

Kwa kuzingatia prompt hiyo hapo juu, unaweza kupata jibu kama ifuatavyo:

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

Matokeo haya ni mazuri, najua nini cha kupika. Kwa wakati huu, maboresho ambayo yanaweza kuwa muhimu ni:

- Kuchuja viungo nisivyopenda au nina mzio navyo.
- Kutengeneza orodha ya ununuzi, iwapo sina viungo vyote nyumbani.

Kwa kesi hizo hapo juu, hebu tuongeze prompt ya ziada:

> "Tafadhali ondoa mapishi yenye vitunguu saumu kwani nina mzio na ubadilishe na kitu kingine. Pia, tafadhali tengeneza orodha ya ununuzi kwa mapishi, ukizingatia tayari nina kuku, viazi na karoti nyumbani."

Sasa una matokeo mapya, ambayo ni:

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

Hayo ni mapishi yako matano, bila kutaja vitunguu saumu na pia una orodha ya ununuzi ukizingatia kile ulichonacho tayari nyumbani.

## Zoezi - tengeneza jenereta ya mapishi

Sasa kwa kuwa tumeshafanya hali ya mfano, hebu tuandike kode inayolingana na hali iliyotolewa. Ili kufanya hivyo, fuata hatua hizi:

1. Tumia faili iliyopo _app.py_ kama mwanzo
1. Tafuta kigezo cha `prompt` na ubadilishe kode yake kuwa ifuatayo:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Ikiwa sasa unaendesha kode, unapaswa kuona matokeo sawa na:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > KUMBUKA, LLM yako siyo ya uhakika, hivyo unaweza kupata matokeo tofauti kila wakati unapoendesha programu.

   Nzuri, hebu tuone jinsi tunavyoweza kuboresha mambo. Ili kuboresha mambo, tunataka kuhakikisha kode ni rahisi kubadilika, hivyo viungo na idadi ya mapishi vinaweza kuboreshwa na kubadilishwa.

1. Hebu tubadilishe kode kwa njia ifuatayo:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Kuchukua kode kwa majaribio, inaweza kuonekana kama hii:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Boresha kwa kuongeza kichujio na orodha ya ununuzi

Sasa tuna programu inayofanya kazi yenye uwezo wa kutoa mapishi na ni rahisi kubadilika kwani inategemea maingizo kutoka kwa mtumiaji, zote kwenye idadi ya mapishi lakini pia viungo vilivyotumika.

Ili kuboresha zaidi, tunataka kuongeza yafuatayo:

- **Chuja viungo**. Tunataka kuwa na uwezo wa kuchuja viungo tusivyopenda au tuna mzio navyo. Ili kutekeleza mabadiliko haya, tunaweza kuhariri prompt yetu iliyopo na kuongeza hali ya kichujio mwishoni mwa hiyo kama ifuatavyo:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Hapo juu, tunaongeza `{filter}` mwishoni mwa prompt na pia tunakamata thamani ya kichujio kutoka kwa mtumiaji.

  Mfano wa maingizo ya kuendesha programu sasa unaweza kuonekana kama ifuatavyo:

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

  Kama unavyoona, mapishi yoyote yenye maziwa yamechujwa. Lakini, ikiwa una uvumilivu mdogo wa lactose, unaweza kutaka kuchuja mapishi yenye jibini pia, kwa hivyo kuna haja ya kuwa wazi.

- **Tengeneza orodha ya ununuzi**. Tunataka kutengeneza orodha ya ununuzi, ukizingatia kile tunachokuwa nacho tayari nyumbani.

  Kwa utendaji huu, tunaweza kujaribu kutatua kila kitu katika prompt moja au tunaweza kuigawanya katika prompts mbili. Hebu jaribu mbinu ya pili. Hapa tunapendekeza kuongeza prompt ya ziada, lakini ili hiyo ifanye kazi, tunahitaji kuongeza matokeo ya prompt ya kwanza kama muktadha kwa prompt ya pili.

  Tafuta sehemu katika kode inayochapisha matokeo kutoka kwa prompt ya kwanza na ongeza kode ifuatayo chini:

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

  1. Tunaunda prompt mpya kwa kuongeza matokeo kutoka kwa prompt ya kwanza kwa prompt mpya:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Tunafanya ombi jipya, lakini pia tukizingatia idadi ya tokens tulizoomba katika prompt ya kwanza, kwa hivyo wakati huu tunasema `max_tokens` ni 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     Kuchukua kode hii kwa majaribio, sasa tunapata matokeo yafuatayo:

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

Kile tunacho hadi sasa ni kode inayofanya kazi, lakini kuna marekebisho tunayopaswa kufanya ili kuboresha mambo zaidi. Baadhi ya mambo tunayopaswa kufanya ni:

- **Tenganisha siri kutoka kwa kode**, kama kitufe cha API. Siri hazipaswi kuwa katika kode na zinapaswa kuhifadhiwa mahali salama. Ili kutenganisha siri kutoka kwa kode, tunaweza kutumia vigezo vya mazingira na maktaba kama `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` faili yenye maudhui yafuatayo:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Kumbuka, kwa Azure, unahitaji kuweka vigezo vya mazingira vifuatavyo:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     Katika kode, ungepakiwa vigezo vya mazingira kama ifuatavyo:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Neno juu ya urefu wa token**. Tunapaswa kuzingatia ni tokens ngapi tunahitaji kuzalisha maandishi tunayohitaji. Tokens zinagharimu pesa, kwa hivyo inapowezekana, tunapaswa kujaribu kuwa na uchumi na idadi ya tokens tunazotumia. Kwa mfano, tunaweza kuunda prompt ili tuweze kutumia tokens chache?

  Ili kubadilisha tokens zinazotumiwa, unaweza kutumia parameter ya `max_tokens`. Kwa mfano, ikiwa unataka kutumia tokens 100, ungefanya:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Kujaribu na temperature**. Temperature ni kitu ambacho hatujakitaja hadi sasa lakini ni muktadha muhimu kwa jinsi programu yetu inavyofanya kazi. Juu zaidi thamani ya temperature, ndivyo matokeo yatakavyokuwa ya nasibu zaidi. Kinyume chake, chini zaidi thamani ya temperature, ndivyo matokeo yatakavyokuwa ya kutabirika zaidi. Fikiria ikiwa unataka utofauti katika matokeo yako au la.

  Ili kubadilisha temperature, unaweza kutumia parameter ya `temperature`. Kwa mfano, ikiwa unataka kutumia temperature ya 0.5, ungefanya:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Kumbuka, karibu na 1.0, ndivyo utofauti wa matokeo unavyokuwa mkubwa zaidi.

## Kazi

Kwa kazi hii, unaweza kuchagua nini cha kujenga.

Hapa kuna mapendekezo:

- Rekebisha programu ya jenereta ya mapishi ili kuiboresha zaidi. Cheza na thamani za temperature, na prompts ili uone unachoweza kubuni.
- Jenga "study buddy". Programu hii inapaswa kuwa na uwezo wa kujibu maswali kuhusu mada kwa mfano Python, unaweza kuwa na prompts kama "Ni mada gani fulani katika Python?", au unaweza kuwa na prompt inayosema, nionyeshe kode kwa mada fulani n.k.
- Historia bot, fanya historia ije hai, mwagize bot kuigiza mhusika wa kihistoria fulani na muulize maswali kuhusu maisha na nyakati zake.

## Suluhisho

### Study buddy

Hapo chini kuna prompt ya kuanzia, angalia jinsi unavyoweza kuitumia na kuibadilisha kulingana na upendavyo.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Historia bot

Hapa kuna baadhi ya prompts unazoweza kutumia:

@@CODE_BLOCK

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya kiasili inapaswa kuzingatiwa kama chanzo chenye mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya kibinadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.