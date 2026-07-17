# Paggawa ng Mga Aplikasyon sa Pagbuo ng Teksto

[![Paggawa ng Mga Aplikasyon sa Pagbuo ng Teksto](../../../translated_images/tl/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(I-click ang larawan sa itaas upang makita ang video ng araling ito)_

Nakita mo na sa kurikulum na ito na may mga pangunahing konsepto tulad ng mga prompt at pati na rin isang buong disiplina na tinatawag na "prompt engineering". Maraming mga tool na maaari mong gamitin tulad ng ChatGPT, Office 365, Microsoft Power Platform at iba pa, na sumusuporta sa iyo gamit ang mga prompt upang makamit ang isang bagay.

Para maidagdag mo ang ganitong karanasan sa isang app, kailangan mong maintindihan ang mga konsepto tulad ng mga prompt, completions at pumili ng isang library na gagamitin. Iyan mismo ang matututunan mo sa kabanatang ito.

## Panimula

Sa kabanatang ito, ikaw ay:

- Matututo tungkol sa openai library at ang mga pangunahing konsepto nito.
- Gumawa ng isang text generation app gamit ang openai.
- Maintindihan kung paano gamitin ang mga konsepto tulad ng prompt, temperature, at tokens para gumawa ng isang text generation app.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- Ipaliwanag kung ano ang isang text generation app.
- Gumawa ng isang text generation app gamit ang openai.
- I-configure ang iyong app upang gumamit ng mas marami o kaunting tokens at baguhin din ang temperature, para sa iba't ibang mga output.

## Ano ang isang text generation app?

Karaniwan kapag gumagawa ka ng app, ito ay may isang uri ng interface tulad ng sumusunod:

- Batay sa command. Ang console apps ay mga tipikal na app kung saan nagta-type ka ng command at isinasagawa nito ang isang gawain. Halimbawa, ang `git` ay isang command-based na app.
- User interface (UI). Ang ilang mga app ay may graphical user interfaces (GUIs) kung saan tumatakbo ka sa pamamagitan ng pag-click sa mga button, pag-input ng teksto, pagpili ng mga opsyon at iba pa.

### Limitado ang Console at UI apps

Ihambing ito sa isang command-based na app kung saan nagta-type ka ng command:

- **Ito ay limitado**. Hindi ka basta makakapag-type ng kahit anong command, tanging ang mga suportado ng app lang.
- **Tiyak sa wika**. Ang ilang app ay sumusuporta sa maraming wika, ngunit sa default, ang app ay ginawa para sa isang partikular na wika, kahit na maaari kang magdagdag ng suporta para sa iba pang mga wika.

### Mga Benepisyo ng text generation apps

Paano naman naiiba ang isang text generation app?

Sa isang text generation app, mas malawak ang iyong kakayahan, hindi ka limitado sa set ng mga command o isang partikular na input na wika. Sa halip, maaari mong gamitin ang natural na wika upang makipag-ugnayan sa app. Isang benepisyo pa ay nakikipag-ugnayan ka na sa isang pinagkukunan ng datos na na-train sa isang malawak na korpus ng impormasyon, samantalang ang tradisyonal na app ay maaaring limitado sa nilalaman ng isang database.

### Ano ang maaari kong gawin gamit ang isang text generation app?

Maraming bagay ang maaari mong gawin. Halimbawa:

- **Isang chatbot**. Isang chatbot na sumasagot ng mga tanong tungkol sa mga paksa, tulad ng iyong kumpanya at mga produkto nito ay maaaring magandang tugma.
- **Tumutulong**. Magaling ang mga LLM sa mga bagay tulad ng pagsasummarize ng teksto, pagkuha ng mga insight mula sa teksto, paggawa ng teksto tulad ng resumes at iba pa.
- **Assistant sa code**. Depende sa language model na gagamitin mo, maaari kang gumawa ng assistant sa code na tutulong sa iyo magsulat ng code. Halimbawa, maaari kang gumamit ng produkto tulad ng GitHub Copilot pati na rin ang ChatGPT upang makatulong sa pagsulat ng code.

## Paano ako makakapagsimula?

Kailangan mong makahanap ng paraan para kumonekta sa isang LLM na karaniwang sumusunod sa dalawang pamamaraan:

- Gumamit ng API. Dito, bumubuo ka ng web requests gamit ang iyong prompt at nakakatanggap ng generated na teksto pabalik.
- Gumamit ng library. Nakakatulong ang mga library upang i-encapsulate ang mga API calls at gawing mas madali itong gamitin.

## Mga Libraries/SDKs

May ilang kilalang mga library para sa pakikipagtrabaho sa LLM tulad ng:

- **openai**, ang libraryang ito ay nagpapadali upang kumonekta sa iyong model at magpadala ng mga prompt.

Mayroon ding mga library na gumagana sa mas mataas na lebel tulad ng:

- **Langchain**. Kilala ang Langchain at sumusuporta sa Python.
- **Semantic Kernel**. Ang Semantic Kernel ay isang library mula sa Microsoft na sumusuporta sa mga wikang C#, Python, at Java.

## Unang app gamit ang openai

Tingnan natin kung paano tayo makakagawa ng ating unang app, kung anong mga library ang kailangan, gaano karami ang hinihingi at iba pa.

### I-install ang openai

Maraming mga library na para sa pakikipag-ugnayan sa OpenAI o Azure OpenAI. Posible ring gumamit ng iba’t ibang programming languages tulad ng C#, Python, JavaScript, Java at iba pa. Pinili naming gamitin ang `openai` Python library, kaya gagamit kami ng `pip` para mai-install ito.

```bash
pip install openai
```

### Gumawa ng resource

Kailangan mong gawin ang sumusunod na mga hakbang:

- Gumawa ng account sa Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Makakuha ng access sa Azure OpenAI. Pumunta sa [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) at humiling ng access.

  > [!NOTE]
  > Sa panahon ng pagsulat, kailangan mong mag-aplay para sa access sa Azure OpenAI.

- Mag-install ng Python <https://www.python.org/>
- Nakagawa ng Azure OpenAI Service resource. Tingnan ang gabay para sa paano [gumawa ng resource](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Hanapin ang API key at endpoint

Sa puntong ito, kailangan mong sabihin sa `openai` library mo kung aling API key ang gagamitin. Upang makita ang iyong API key, pumunta sa seksyong "Keys and Endpoint" ng iyong Azure OpenAI resource at kopyahin ang "Key 1" na halaga.

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Ngayon na mayroon ka nang kopyang impormasyon, turuan natin ang mga library na gamitin ito.

> [!NOTE]
> Mainam na paghiwalayin ang iyong API key mula sa iyong code. Maaari mong gawin ito gamit ang mga environment variable.
>
> - Itakda ang environment variable na `OPENAI_API_KEY` sa iyong API key.
>   `export OPENAI_API_KEY='sk-...'`

### I-set up ang configuration para sa Azure

Kung gumagamit ka ng Azure OpenAI (na ngayon ay bahagi ng Microsoft Foundry), ganito mo i-setup ang configuration. Ginagamit namin ang standard na `OpenAI` client na tumutukoy sa Azure OpenAI `/openai/v1/` endpoint, na gumagana sa Responses API at hindi nangangailangan ng `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Sa itaas, itinatakda natin ang mga sumusunod:

- `api_key`, ito ang iyong API key na makikita sa Azure Portal o Microsoft Foundry portal.
- `base_url`, ito ang endpoint ng iyong Foundry resource na may kasamang `/openai/v1/`. Ang stable v1 endpoint ay gumagana nang pareho sa OpenAI at Azure OpenAI nang walang `api_version` management.

> [!NOTE] > Binabasa ng `os.environ` ang mga environment variable. Maaari mo itong gamitin para basahin ang mga environment variable tulad ng `AZURE_OPENAI_API_KEY` at `AZURE_OPENAI_ENDPOINT`. Itakda ang mga ito sa iyong terminal o gamit ang library tulad ng `dotenv`.

## Pagbuo ng teksto

Ang paraan ng pagbuo ng teksto ay gamit ang Responses API sa pamamagitan ng `responses.create` na metoda. Narito ang isang halimbawa:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # ito ang pangalan ng deployment ng iyong modelo
    input=prompt,
    store=False,
)
print(response.output_text)
```

Sa code sa itaas, gumagawa tayo ng response at ipinapasa ang model na gusto nating gamitin at ang prompt. Pagkatapos ay inilalabas natin ang generated na teksto gamit ang `response.output_text`.

### Mga multi-turn na usapan

Ang Responses API ay angkop para sa parehong single-turn na pagbuo ng teksto at multi-turn na chatbots - nagbibigay ka ng isang listahan ng mga mensahe sa `input` upang bumuo ng isang pag-uusap:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Higit pang impormasyon sa functionality na ito sa mga susunod na kabanata.

## Ehersisyo - ang iyong unang text generation app

Ngayon na natutunan natin paano i-setup at i-configure ang openai, oras na para gumawa ng iyong unang text generation app. Upang gawin ang iyong app, sundin ang mga hakbang na ito:

1. Gumawa ng virtual environment at i-install ang openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Kung gumagamit ka ng Windows, i-type ang `venv\Scripts\activate` imbes na `source venv/bin/activate`.

   > [!NOTE]
   > Hanapin ang iyong Azure OpenAI key sa pamamagitan ng pagpunta sa [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) at hanapin ang `Open AI` at piliin ang `Open AI resource` at pagkatapos ay piliin ang `Keys and Endpoint` at kopyahin ang `Key 1` na halaga.

1. Gumawa ng _app.py_ file at ilagay ang sumusunod na code:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # idagdag ang iyong code para sa kompletong sagot
   prompt = "Complete the following: Once upon a time there was a"

   # gumawa ng kahilingan gamit ang Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # i-print ang sagot
   print(response.output_text)
   ```

   > [!NOTE]
   > Kung gumagamit ka ng plain OpenAI (hindi Azure), gamitin ang `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (walang `base_url`) at magpasa ng pangalan ng model tulad ng `gpt-5-mini` imbes na pangalan ng deployment.

   Makikita mo ang output na tulad ng sumusunod:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Iba't ibang uri ng prompt, para sa iba't ibang bagay

Ngayon ay nakita mo na kung paano bumuo ng teksto gamit ang isang prompt. Mayroon ka nang program na tumatakbo at maaari mong baguhin ito upang gumawa ng iba't ibang uri ng teksto.

Maaaring gamitin ang mga prompt para sa lahat ng uri ng mga gawain. Halimbawa:

- **Mag-generate ng uri ng teksto**. Halimbawa, maaari kang gumawa ng tula, mga tanong para sa isang quiz at iba pa.
- **Maghanap ng impormasyon**. Maaari mong gamitin ang mga prompt upang maghanap ng impormasyon tulad ng halimbawa na 'Ano ang ibig sabihin ng CORS sa web development?'.
- **Mag-generate ng code**. Maaari kang gumamit ng mga prompt upang gumawa ng code, halimbawa gumawa ng regular expression para i-validate ang mga email o bakit hindi gumawa ng buong programa, tulad ng isang web app?

## Isang mas praktikal na kaso: isang recipe generator

Isipin mong may mga sangkap ka sa bahay at gusto mong magluto ng isang bagay. Para doon, kailangan mo ng recipe. Isang paraan para makahanap ng mga recipe ay ang paggamit ng search engine o maaari kang gumamit ng LLM para dito.

Maaari kang gumawa ng prompt na ganito:

> "Ipakita sa akin ang 5 recipe para sa ulam na may mga sumusunod na sangkap: manok, patatas, at karot. Sa bawat recipe, ilista lahat ng sangkap na ginamit"

Batay sa prompt na ito, maaari kang makatanggap ng tugon na katulad ng:

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

Maganda ang kinalabasan na ito, alam ko na ang lulutuin ko. Sa puntong ito, ang mga maaaring maging kapaki-pakinabang na pagpapahusay ay:

- Pagsala ng mga sangkap na ayaw ko o di ako makain.
- Gumawa ng listahan ng pamimili, sakaling wala akong lahat ng sangkap sa bahay.

Para sa mga nabanggit na kaso, magdagdag tayo ng dagdag na prompt:

> "Pakialis ang mga recipe na may bawang dahil ako ay allergic at palitan ito ng ibang sangkap. At, gumawa rin ng listahan ng pamimili para sa mga recipe, isinasaalang-alang na mayroon na akong manok, patatas at karot sa bahay."

Ngayon ay may bago kang resulta, ito ay:

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

Iyan ang limang recipe mo, walang binanggit na bawang at mayroon ka ring listahan ng pamimili batay sa mga sangkap na mayroon ka na sa bahay.

## Ehersisyo - gumawa ng recipe generator

Ngayon na naipakita natin ang isang senaryo, magsulat tayo ng code upang tumugma sa senaryong iyon. Gawin ito sa pamamagitan ng pagsunod sa mga hakbang:

1. Gamitin ang kasalukuyang _app.py_ file bilang panimulang punto
1. Hanapin ang variable na `prompt` at palitan ang code nito ng sumusunod:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Kung patatakbuhin mo ngayon ang code, makikita mo ang isang output na tulad nito:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > PAALALA, ang iyong LLM ay nondeterministic, kaya maaaring mag-iba-iba ang mga resulta sa bawat pagpapatakbo ng programa.

   Magaling, tingnan natin kung paano pa mapapabuti. Upang mapaayos pa ito, gusto nating siguruhin na flexible ang code, kaya ang mga sangkap at bilang ng mga recipe ay maaaring baguhin at paunlarin.

1. Palitan natin ang code sa ganitong paraan:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # i-interpolate ang bilang ng mga resipi sa prompt at mga sangkap
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Ang pagkuha ng code para sa isang test run ay maaaring ganito:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Pagbutihin sa pamamagitan ng pagdagdag ng filter at shopping list

Mayroon na tayong working app na kayang gumawa ng mga recipe at ito ay flexible dahil umaasa ito sa mga input mula sa gumagamit, parehong sa bilang ng recipe pati na rin sa mga sangkap na ginagamit.

Para lalo pa itong mapaganda, gusto nating idagdag ang mga sumusunod:

- **Salain ang mga sangkap**. Nais nating magkaroon ng kakayahan na salain ang mga sangkap na ayaw natin o dito tayo allergic. Para magawa ito, maaari nating baguhin ang ating prompt at magdagdag ng kundisyon ng filter sa dulo nito tulad nito:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Sa itaas, idinagdag natin ang `{filter}` sa dulo ng prompt at huli na rin nating kinukuha ang filter na halaga mula sa user.

  Ang halimbawa ng input kapag pinatakbo ang programa ay maaaring ganito:

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

  Tulad ng makikita mo, ang anumang recipe na may gatas ay na-filter na. Ngunit, kung lactose intolerant ka, maaaring gusto mo ring salain ang mga recipe na may keso, kaya kailangang maging malinaw.


- **Gumawa ng listahan sa pamimili**. Nais nating gumawa ng listahan sa pamimili, isinasaalang-alang kung ano na ang mayroon tayo sa bahay.

  Para sa functionality na ito, maaari nating subukang lutasin ang lahat sa isang prompt o maaari rin nating hatiin ito sa dalawang prompt. Subukan natin ang huli na paraan. Dito, nagmumungkahi kami ng pagdagdag ng karagdagang prompt, ngunit para gumana ito, kailangan nating idagdag ang resulta ng unang prompt bilang konteksto sa pangalawang prompt.

  Hanapin ang bahagi ng code na nagpi-print ng resulta mula sa unang prompt at idagdag ang sumusunod na kodigo sa ibaba nito:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # iprinta ang sagot
  print("Shopping list:")
  print(response.output_text)
  ```

  Pansinin ang mga sumusunod:

  1. Gumagawa tayo ng bagong prompt sa pamamagitan ng pagdagdag ng resulta mula sa unang prompt sa bagong prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Gumagawa tayo ng bagong request, isinasaalang-alang din ang bilang ng mga token na hiniling natin sa unang prompt, kaya sa oras na ito sinasabi natin na `max_output_tokens` ay 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Sa paggamit ng kodigo na ito, narito na ang sumusunod na output:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Pahusayin ang iyong setup

Ang mayroon tayo sa ngayon ay kodigo na gumagana, ngunit may ilang mga pagbabago na dapat nating gawin upang mapabuti pa ito. Ang ilang mga bagay na dapat gawin ay:

- **Ihiwalay ang mga sikreto mula sa kodigo**, tulad ng API key. Ang mga sikreto ay hindi dapat isama sa kodigo at dapat itago sa isang ligtas na lokasyon. Upang paghiwalayin ang mga sikreto mula sa kodigo, maaari nating gamitin ang mga environment variables at mga library tulad ng `python-dotenv` upang i-load ang mga ito mula sa isang file. Ganito ang itsura nito sa kodigo:

  1. Gumawa ng `.env` file na may nilalaman na ganito:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Tandaan, para sa Azure OpenAI sa Microsoft Foundry, kailangan mong itakda ang mga sumusunod na environment variables imbes:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Sa kodigo, ganito mo iloload ang mga environment variables:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Isang salita tungkol sa haba ng token**. Dapat nating isaalang-alang kung ilang token ang kailangan natin upang makabuo ng nais nating teksto. Ang mga token ay may gastos, kaya't kung maaari, dapat tayong maging matipid sa dami ng token na ginagamit. Halimbawa, maaari ba nating ayusin ang prompt upang gumamit ng mas kaunting token?

  Para baguhin ang bilang ng token na ginagamit, maaari mong gamitin ang parameter na `max_output_tokens`. Halimbawa, kung gusto mong gumamit ng 100 token, maaaring ganito:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Pagsubok sa temperatura**. Ang temperatura ay isang bagay na hindi pa natin nabanggit ngunit mahalaga sa konteksto kung paano gumagana ang ating programa. Mas mataas ang halaga ng temperatura, mas random ang magiging output. Sa kabilang banda, mas mababa ang temperatura, mas predictable ang output. Isaalang-alang kung nais mo ba ng pagkakaiba-iba sa iyong output o hindi.

  Para baguhin ang temperatura, maaari mong gamitin ang parameter na `temperature`. Halimbawa, kung nais mong gamitin ang temperatura na 0.5, ganito ang gawin:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Tandaan, habang mas malapit sa 1.0, mas nagkakaiba-iba ang output.

- **Ang mga reasoning models ay hindi gumagamit ng `temperature`**. Ito ay isang mahalagang pagbabago sa 2026. Ang mga kasalukuyang modelo na hindi deprecated sa Microsoft Foundry ay **mga reasoning models** (ang GPT-5 family, o-series) - at hindi nila sinusuportahan ang `temperature` o `top_p` (gaya ng `max_tokens`; gamitin ang `max_output_tokens`). Kung magpapadala ka ng `temperature` sa `gpt-5-mini` makakatanggap ka ng error na "parameter not supported". Kaya upang subukan ang temperature example sa itaas, gamitin ang modelong sumusuporta pa sa sampling controls - halimbawa ang open **Llama** model tulad ng `Llama-3.3-70B-Instruct` mula sa [Microsoft Foundry model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), na tinatawag gamit ang Foundry Models / Azure AI Inference endpoint (pareho ng paraan sa `githubmodels-*` samples). Para sa mga reasoning models tulad ng GPT-5, naiiba ang paraan ng pagpapaandar ng output:
  - **Prompt engineering** - malinaw na mga instruksyon, mga halimbawa, at istrukturadong output (tingnan ang lesson na [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) ang gumagawa ng trabaho na dating ginawa ng sampling knobs.
  - **Reasoning controls** - mga parameter tulad ng reasoning effort/verbosity na nag-babalanse sa lalim ng pag-iisip laban sa latency at gastos.

  Sa madaling salita: ang `temperature`/`top_p` ay valid pa rin sa maraming modelo (Llama, Mistral, Phi, at ang GPT-4.x family - bagama't unti-unting hindi na ginagamit ang GPT-4.x), ngunit ang direksyon ay prompt engineering + reasoning controls sa mga reasoning models tulad ng GPT-5.

## Takdang-Aralin

Para sa takdang-aralin na ito, maaari kang pumili kung ano ang gagawin.

Narito ang ilang suhestiyon:

- Ayusin pa ang recipe generator app upang mas mapabuti ito. Maglaro sa mga halaga ng temperatura, at mga prompt para makita kung ano ang maaari mong malikha.
- Gumawa ng "study buddy". Ang app na ito ay dapat kayang sumagot sa mga tanong tungkol sa isang tema, halimbawa Python, maaari kang magkaroon ng mga prompt tulad ng "Ano ang isang tiyak na paksa sa Python?", o maaaring may prompt na nagsasabi, ipakita ang kodigo para sa isang partikular na paksa atbp.
- History bot, gawin ang kasaysayan na buhay na buhay, utusan ang bot na gumanap bilang isang tiyak na karakter sa kasaysayan at itanong sa kanya ang tungkol sa kanyang buhay at panahon.

## Solusyon

### Study buddy

Narito ang isang panimulang prompt, tingnan kung paano mo ito magagamit at ayusin ayon sa iyong gusto.

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

Ano ang ibig sabihin ng konseptong temperatura?

1. Kinokontrol nito kung gaano karandom ang output.
1. Kinokontrol nito kung gaano kalaki ang sagot.
1. Kinokontrol nito kung gaano karaming mga token ang ginagamit.

## 🚀 Hamon

Kapag ginagawa ang takdang-aralin, subukang baguhin ang temperatura, subukang itakda ito sa 0, 0.5, at 1. Tandaan na 0 ang pinakakaunti ang pagkakaiba-iba at 1 ang pinakamaraming pagkakaiba-iba. Anong halaga ang pinakamahusay para sa iyong app?

## Magaling na Trabaho! Ipagpatuloy ang Iyong Pag-aaral

Pagkatapos matapos ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pag-level up ng iyong kaalaman sa Generative AI!

Puntahan ang Lesson 7 kung saan titingnan natin kung paano [gumawa ng mga chat applications](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->