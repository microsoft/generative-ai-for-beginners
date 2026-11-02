# Paggawa ng Mga Aplikasyon sa Pagbuo ng Teksto

[![Paggawa ng Mga Aplikasyon sa Pagbuo ng Teksto](../../../translated_images/tl/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(I-click ang larawan sa itaas upang makita ang video ng leksyong ito)_

Nakita mo na sa kurikulum na ito na may mga pangunahing konsepto tulad ng mga prompt at pati na rin ang isang buong disiplina na tinatawag na "prompt engineering". Maraming mga tool na maaari mong makausap tulad ng ChatGPT, Office 365, Microsoft Power Platform at iba pa, na sumusuporta sa paggamit mo ng mga prompt upang makamit ang isang bagay.

Para maidagdag mo ang ganitong karanasan sa isang app, kailangan mong maunawaan ang mga konsepto tulad ng mga prompt, mga completion at pumili ng isang library na gagamitin. Iyan talaga ang matututunan mo sa kabanatang ito.

## Panimula

Sa kabanatang ito, matututuhan mo ang:

- Matuto tungkol sa openai library at mga pangunahing konsepto nito.
- Gumawa ng isang text generation app gamit ang openai.
- Maunawaan kung paano gamitin ang mga konsepto tulad ng prompt, temperature, at tokens upang makabuo ng text generation app.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng leksyon na ito, magagawa mong:

- Ipaliwanag kung ano ang isang text generation app.
- Gumawa ng isang text generation app gamit ang openai.
- I-configure ang iyong app upang gumamit ng mas marami o mas kaunting tokens at baguhin din ang temperature, para sa iba't ibang output.

## Ano ang text generation app?

Karaniwan kapag gumagawa ka ng app, mayroong interface tulad ng sumusunod:

- Command-based. Ang mga console app ay karaniwang app kung saan nagta-type ka ng utos at isinasagawa nito ang isang gawain. Halimbawa, ang `git` ay isang command-based app.
- User interface (UI). Ang ilang mga app ay may graphical user interfaces (GUIs) kung saan magki-click ka ng mga button, maglalagay ng teksto, pipili ng mga opsyon at iba pa.

### Limitado ang Console at UI apps

Ihambing ito sa isang command-based app kung saan nagta-type ka ng utos:

- **Limitado ito**. Hindi basta-basta makakapag-type ng anumang utos, kundi ang mga suportado ng app lamang.
- **Nakasentro sa wikang partikular**. Ang ilang app ay sumusuporta sa maraming wika, pero karaniwan ang app ay itinayo para sa isang partikular na wika, kahit maaari kang magdagdag ng suporta sa iba pang wika.

### Mga Benepisyo ng Text Generation Apps

Paano nga ba naiiba ang isang text generation app?

Sa isang text generation app, mas malawak ang iyong kakayahan, hindi ka naka-limit sa mga tiyak na utos o sa isang input na wika lamang. Sa halip, maaari kang gumamit ng natural na wika upang makipag-ugnayan sa app. Isa pang benepisyo ay nakikipag-ugnayan ka na sa isang data source na sinanay sa malawak na koleksyon ng impormasyon, samantalang ang karaniwang app ay maaaring limitado sa kung ano ang nasa database.

### Ano ang maaari kong gawin gamit ang isang text generation app?

Maraming bagay na maaari mong gawin. Halimbawa:

- **Isang chatbot**. Isang chatbot na sumasagot sa mga tanong tungkol sa mga paksa, tulad ng iyong kumpanya at mga produkto nito, ay maaaring maging mahusay na tugma.
- **Tulong**. Magaling ang LLMs sa mga bagay tulad ng pagsasummarize ng teksto, pagkuha ng mga insight mula sa teksto, paggawa ng teksto tulad ng mga resume at iba pa.
- **Tulong sa Code**. Depende sa language model na ginagamit mo, maaari kang gumawa ng code assistant na tumutulong sumulat ng code. Halimbawa, maaari mong gamitin ang mga produkto tulad ng GitHub Copilot pati na rin ang ChatGPT upang tumulong sumulat ng code.

## Paano Ako Magsisimula?

Kailangan mong hanapin ang paraan upang makipag-integrate sa isang LLM na kadalasan ay may dalawang paraan:

- Gamitin ang API. Dito ay bumubuo ka ng mga web request gamit ang iyong prompt at makakakuha ng generated na teksto bilang tugon.
- Gamitin ang library. Ang mga library ay tumutulong mag-encapsulate ng mga API call at gawing mas madali itong gamitin.

## Mga Libraries/SDKs

May ilang kilalang library para sa paggamit ng mga LLM tulad ng:

- **openai**, ang library na ito ay nagpapadali sa pagkonekta sa iyong modelo at pagpapadala ng mga prompt.

Mayroon ding mga library na gumagana sa mas mataas na antas tulad ng:

- **Langchain**. Kilala ang Langchain at sumusuporta sa Python.
- **Semantic Kernel**. Ang Semantic Kernel ay isang library ng Microsoft na sumusuporta sa mga wikang C#, Python, at Java.

## Unang App Gamit ang openai

Tingnan natin kung paano tayo makakagawa ng unang app natin, kung anong mga library ang kailangan, gaano kalaki ang kinakailangan at iba pa.

### I-install ang openai

Maraming library na pwedeng gamitin para makipag-ugnayan sa OpenAI o Azure OpenAI. Posible ring gumamit ng iba't ibang programming language gaya ng C#, Python, JavaScript, Java at iba pa. Pinili naming gamitin ang `openai` Python library, kaya't gagamitin namin ang `pip` upang i-install ito.

```bash
pip install openai
```

### Gumawa ng resource

Kailangan mong gawin ang mga sumusunod na hakbang:

- Gumawa ng account sa Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Kumuha ng access sa Azure OpenAI. Pumunta sa [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) at humiling ng access.

  > [!NOTE]
  > Sa oras ng pagsulat, kailangan mong mag-apply para sa access sa Azure OpenAI.

- Mag-install ng Python <https://www.python.org/>
- Nakagawa ka na ng Azure OpenAI Service resource. Tingnan ang gabay kung paano [lumikha ng resource](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Hanapin ang API key at endpoint

Sa puntong ito, kailangan mong sabihin sa iyong `openai` library kung aling API key ang gagamitin. Para mahanap ang API key, pumunta sa "Keys and Endpoint" seksyon ng iyong Azure OpenAI resource at kopyahin ang halagang "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Ngayon na nakopya mo na ang impormasyong ito, ituturo natin sa mga library na gamitin ito.

> [!NOTE]
> Maganda na paghiwalayin ang iyong API key mula sa iyong code. Maaari mong gawin ito gamit ang environment variables.
>
> - Itakda ang environment variable na `OPENAI_API_KEY` sa iyong API key.
>   `export OPENAI_API_KEY='sk-...'`

### Setup configuration para sa Azure

Kung ginagamit mo ang Azure OpenAI (ngayon ay bahagi na ng Microsoft Foundry), ganito ang pagsasaayos ng configuration. Ginagamit namin ang standard na `OpenAI` client na nakaturo sa Azure OpenAI `/openai/v1/` endpoint, na gumagana sa Responses API at hindi kailangan ng `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Sa itaas ay isinaset natin ang mga sumusunod:

- `api_key`, ito ang iyong API key na makikita sa Azure Portal o Microsoft Foundry portal.
- `base_url`, ito ang endpoint ng iyong Foundry resource na may kasamang `/openai/v1/`. Gumagana ang stable v1 endpoint sa OpenAI at Azure OpenAI nang walang `api_version` management.

> [!NOTE] > `os.environ` ay nagbabasa ng environment variables. Maaari mo itong gamitin para basahin ang mga environment variable tulad ng `AZURE_OPENAI_API_KEY` at `AZURE_OPENAI_ENDPOINT`. Itakda ang mga environment variable na ito sa iyong terminal o gamit ang library na tulad ng `dotenv`.

## Pagbuo ng Teksto

Ang paraan ng paggawa ng teksto ay gamit ang Responses API sa pamamagitan ng `responses.create` method. Heto ang isang halimbawa:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

Sa code sa itaas, gumagawa tayo ng response at ipinapasa ang model na gusto nating gamitin at ang prompt. Pagkatapos ay pinu-print natin ang generated na teksto gamit ang `response.output_text`.

### Multi-turn na pag-uusap

Ang Responses API ay angkop para sa parehong single-turn na text generation at multi-turn na chatbot – nagbibigay ka ng listahan ng mga mensahe sa `input` upang bumuo ng pag-uusap:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Dagdag pa ukol sa functionality na ito sa mga susunod na kabanata.

## Ehersisyo - iyong unang text generation app

Ngayon na natutunan natin kung paano mag-setup at mag-configure ng openai, panahon na upang gawin ang iyong unang text generation app. Sundin ang mga hakbang na ito upang gawin ang iyong app:

1. Gumawa ng virtual environment at i-install ang openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Kung gumagamit ka ng Windows, i-type ang `venv\Scripts\activate` sa halip na `source venv/bin/activate`.

   > [!NOTE]
   > Hanapin ang iyong Azure OpenAI key sa pamamagitan ng pagpunta sa [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) at hanapin ang `Open AI`, piliin ang `Open AI resource` at pagkatapos ay piliin ang `Keys and Endpoint` at kopyahin ang halagang `Key 1`.

1. Gumawa ng _app.py_ file at ilagay ang sumusunod na code:

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
   > Kung gumagamit ka ng plain OpenAI (hindi Azure), gamitin ang `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (walang `base_url`) at magpasa ng model name tulad ng `gpt-5-mini` sa halip na deployment name.

   Dapat makita mo ang output na tulad ng sumusunod:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Iba't ibang uri ng mga prompt, para sa iba't ibang bagay

Ngayon nakikita mo na kung paano mag-generate ng teksto gamit ang prompt. Mayroon ka nang program na tumatakbo na maaari mong baguhin para gumawa ng iba't ibang uri ng teksto.

Maaaring gamitin ang mga prompt para sa maraming uri ng gawain. Halimbawa:

- **Gumawa ng uri ng teksto**. Halimbawa, maaari kang gumawa ng tula, mga tanong para sa quiz at iba pa.
- **Maghanap ng impormasyon**. Maaari mong gamitin ang mga prompt upang maghanap ng impormasyon tulad ng halimbawa ay 'Ano ang ibig sabihin ng CORS sa web development?'.
- **Gumawa ng code**. Maaari mong gamitin ang mga prompt upang gumawa ng code, halimbawa pag-develop ng regular expression para i-validate ang mga email o bakit hindi gumawa ng buong programa, tulad ng web app?

## Isang mas praktikal na gamit: recipe generator

Isipin mo na mayroon kang mga sangkap sa bahay at gusto mong magluto ng isang ulam. Para doon, kailangan mo ng recipe. Ang paraan para makahanap ng recipe ay gumamit ng search engine o maaari kang gumamit ng LLM.

Maaari kang sumulat ng prompt tulad nito:

> "Ipakita sa akin ang 5 mga recipe para sa isang putahe na may mga sumusunod na sangkap: manok, patatas, at karot. Sa bawat recipe, ilista lahat ng mga sangkap na ginamit"

Batay sa prompt na ito, maaaring makakuha ka ng tugon na katulad nito:

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

Maganda ang resulta, alam ko na kung ano ang lulutuin ko. Sa puntong ito, maaaring maging kapaki-pakinabang ang mga pagbuti tulad ng:

- Pag-filter ng mga sangkap na ayaw ko o kung saan ako ay may allergy.
- Gumawa ng listahan ng pamimili, sakaling wala akong lahat ng mga sangkap sa bahay.

Para sa mga kasong ito, magdagdag tayo ng karagdagang prompt:

> "Paki-alis ang mga recipe na may bawang dahil ako ay allergic at palitan ito ng ibang bagay. At gumawa rin ng listahan ng pamimili para sa mga recipe, isinasama na mayroon na akong manok, patatas, at karot sa bahay."

Ngayon mayroon ka nang bagong resulta, ito ay:

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

Ito ang iyong limang recipe, walang nabanggit na bawang at mayroon ka ding listahan ng pamimili na isinasaalang-alang ang mga mayroon ka na sa bahay.

## Ehersisyo - gumawa ng recipe generator

Ngayon na naipakita ang isang senaryo, isulat natin ang code para tumugma sa ipinakitang senaryo. Sundin ang mga hakbang na ito:

1. Gamitin ang umiiral na _app.py_ file bilang panimulang punto
1. Hanapin ang `prompt` variable at palitan ang code nito sa mga sumusunod:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Kung tatakbuhin mo ngayon ang code, dapat makita mo ang output na tulad nito:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > TANDAAN, ang iyong LLM ay nondeterministic, kaya maaaring makakuha ka ng ibang resulta sa bawat beses na patakbuhin mo ang programa.

   Maganda, tingnan natin kung paano ito mapagbubuti. Para mapabuti ang mga bagay, gusto nating maging flexible ang code, kaya ang mga sangkap at bilang ng mga recipe ay maaaring baguhin at paunlarin.

1. Baguhin natin ang code sa ganitong paraan:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Ang pagkuha ng code para sa test run ay maaaring ganito:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Pabutiin sa pagdaragdag ng filter at listahan ng pamimili

Mayroon na tayong gumaganang app na kaya gumawa ng mga recipe at flexible dahil umaasa ito sa input ng gumagamit, kapwa sa bilang ng mga recipe pati na rin ang mga sangkap na ginagamit.

Para lalo pang pagbutihin, gusto nating idagdag ang mga sumusunod:

- **I-filter ang mga sangkap**. Gusto nating magkaroon ng kakayahan na i-filter ang mga sangkap na ayaw natin o tayo ay allergic. Para gawin ito, puwedeng baguhin ang umiiral nating prompt at idagdag ang kundisyon ng filter sa dulo nito tulad nito:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Sa itaas, idinagdag natin ang `{filter}` sa dulo ng prompt at kinukuha rin natin ang halaga ng filter mula sa user.

  Isang halimbawa ng input sa pagpapatakbo ng programa ay maaaring ganito:

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

  Tulad ng nakikita mo, anumang recipe na may gatas ay na-filter. Pero, kung lactose intolerant ka, gusto mo ring i-filter ang mga recipe na may keso, kaya kailangan malinaw ito.

- **Gumawa ng listahan ng pamimili**. Gusto nating gumawa ng listahan ng pamimili, isinasaalang-alang kung ano ang mayroon na sa atin sa bahay.

  Para sa functionality na ito, puwedeng subukan nating lutasin lahat sa isang prompt o puwedeng hatiin sa dalawang prompt. Subukan natin ang huli. Dito isinusuggest nating magdagdag ng karagdagang prompt, pero para gumana ito, kailangan nating idagdag ang resulta ng naunang prompt bilang konteksto sa susunod na prompt.

  Hanapin ang bahagi sa code na nagpi-print ng resulta mula sa unang prompt at idagdag ang sumusunod na code sa ibaba:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Pansinin ang mga sumusunod:

  1. Gumagawa tayo ng bagong prompt sa pamamagitan ng pagdagdag ng resulta mula sa unang prompt sa bagong prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Gumagawa tayo ng bagong request, ngunit isinasaalang-alang din ang bilang ng mga token na hiniling natin sa unang prompt, kaya sa pagkakataong ito sinasabi nating ang `max_output_tokens` ay 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Kapag pinatakbo ang code na ito, makakakuha tayo ng output tulad ng sumusunod:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Pabutin ang iyong setup

Ang mayroon tayo ngayon ay code na gumagana, ngunit may ilang mga pagbabago na dapat nating gawin upang lalo pang mapabuti ang mga bagay. Ilan sa mga dapat nating gawin ay:

- **Paghiwalayin ang mga sikreto mula sa code**, tulad ng API key. Hindi dapat kasama ang mga sikreto sa code at dapat itago ito sa isang ligtas na lugar. Para paghiwalayin ang mga sikreto mula sa code, maaari tayong gumamit ng mga environment variables at mga library tulad ng `python-dotenv` upang i-load ang mga ito mula sa isang file. Ganito ang magiging hitsura nito sa code:

  1. Gumawa ng isang `.env` file na may sumusunod na nilalaman:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Tandaan, para sa Azure OpenAI sa Microsoft Foundry, kailangan mong itakda ang mga sumusunod na environment variables sa halip:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Sa code, iloload mo ang environment variables ganito:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Isang salita tungkol sa haba ng token**. Dapat nating isaalang-alang kung ilang mga token ang kailangan natin upang makabuo ng nais nating teksto. May bayad ang mga token, kaya kung maaari, dapat tayong maging matipid sa dami ng token na ginagamit natin. Halimbawa, maaari ba nating baguhin ang pananalita sa prompt upang magamit ang mas kaunting token?

  Para palitan ang bilang ng token na gagamitin, maaari mong gamitin ang parameter na `max_output_tokens`. Halimbawa, kung gusto mong gumamit ng 100 tokens, gagawin mo ito ng ganito:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Pagsubok sa temperature**. Ang temperature ay isang bagay na hindi pa natin nabanggit ngunit mahalaga sa konteksto kung paano gumagana ang ating programa. Kapag mas mataas ang value ng temperature, mas random ang magiging output. Sa kabilang banda, kapag mas mababa ang temperature, mas predictable ang output. Isaalang-alang kung gusto mo ba ng pagkakaiba-iba sa iyong output o hindi.

  Para baguhin ang temperature, maaari mong gamitin ang parameter na `temperature`. Halimbawa, kung gusto mong gumamit ng temperature na 0.5, gagawin mo ito ng ganito:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Tandaan, kapag papalapit sa 1.0, mas nagiging varied ang output.

- **Hindi ginagamit ng mga reasoning models ang `temperature`**. Ito ay isang mahalagang pagbabagong mangyayari sa 2026. Ang mga kasalukuyang modelong hindi deprecated sa Microsoft Foundry ay mga **reasoning models** (ang pamilya ng GPT-5, o-series) - at **hindi nila sinusuportahan ang `temperature` o `top_p`** (pati na rin ang `max_tokens`; gamitin ang `max_output_tokens`). Kung magpapadala ka ng `temperature` sa `gpt-5-mini`, makakakuha ka ng error na "parameter not supported". Kaya para subukan ang halimbawa ng temperatura sa itaas, gamitin ito sa model na sumusuporta pa sa mga sampling controls - halimbawa isang open **Llama** model tulad ng `Llama-3.3-70B-Instruct` mula sa [Microsoft Foundry model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), tinatawag gamit ang Foundry Models / Azure AI Inference endpoint (kapareho ng `githubmodels-*` samples). Para sa mga reasoning models tulad ng GPT-5, iba ang paraan ng paggabay sa output:
  - **Prompt engineering** - malinaw na mga instruksiyon, mga halimbawa, at istrukturadong output (tingnan ang aralin [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) ang gumagawa ng trabaho na dating ginagampanan ng mga sampling knobs.
  - **Reasoning controls** - mga parameter tulad ng reasoning effort/verbosity ay nagtatrade sa lalim ng reasoning laban sa latency at gastos.

  Sa madaling salita: `temperature`/`top_p` ay valid pa rin sa maraming mga modelo (Llama, Mistral, Phi, at ang pamilya ng GPT-4.x - bagaman unti-unting tinatanggal ang GPT-4.x), ngunit ang direksyon ng pag-unlad ay nasa prompt engineering + reasoning controls sa mga reasoning models tulad ng GPT-5.

## Takdang Aralin

Sa takdang araling ito, maaari kang pumili kung ano ang iyong gagawin.

Narito ang ilang mga mungkahi:

- Baguhin ang recipe generator app upang lalo pa itong mapabuti. Maglaro gamit ang mga temperature values, at mga prompt upang makita kung ano ang kaya mong likhain.
- Gumawa ng isang "study buddy". Ang app na ito ay dapat kayang sumagot sa mga tanong tungkol sa isang paksa, halimbawa Python, maaari kang magkaroon ng mga prompt tulad ng "Ano ang isang tiyak na paksa sa Python?", o maari kang magkaroon ng prompt na nagsasabi, ipakita sa akin ang code para sa isang tiyak na paksa atbp.
- History bot, gawing buhay ang kasaysayan, utusan ang bot na gumanap bilang isang tiyak na makasaysayang karakter at tanungin ito tungkol sa buhay at mga panahon nito.

## Solusyon

### Study buddy

Nasa ibaba ang panimulang prompt, tingnan kung paano mo ito magagamit at maiaangkop ayon sa iyong nais.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### History bot

Narito ang ilang mga prompt na maaari mong gamitin:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Pagsusulit sa Kaalaman

Ano ang ginagawa ng konsepto na temperature?

1. Kinokontrol nito kung gaano ka-random ang output.
1. Kinokontrol nito kung gaano kalaki ang tugon.
1. Kinokontrol nito kung gaano karaming mga token ang ginagamit.

## 🚀 Hamon

Kapag nagtatrabaho sa takdang-aralin, subukang baguhin ang temperature, subukang itakda ito sa 0, 0.5, at 1. Tandaan na ang 0 ay ang hindi gaanong nagbabago at ang 1 ay ang pinaka nagbabago. Anong halaga ang pinakamainam para sa iyong app?

## Mahusay na Gawain! Ipagpatuloy ang Iyong Pag-aaral

Pagkatapos matapos ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang patuloy na pagbutihin ang iyong kaalaman sa Generative AI!

Pumunta sa Lesson 7 kung saan titingnan natin kung paano [gumawa ng mga chat application](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->