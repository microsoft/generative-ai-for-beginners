# Pagbuo ng Mga Aplikasyon para sa Text Generation

[![Pagbuo ng Mga Aplikasyon para sa Text Generation](../../../translated_images/tl/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(I-click ang larawan sa itaas upang makita ang video ng araling ito)_

Nakita mo na sa kurikulum na ito na may mga pangunahing konsepto tulad ng mga prompt at pati na rin ang isang buong disiplina na tinatawag na "prompt engineering". Maraming mga tool na maaari mong gamitin gaya ng ChatGPT, Office 365, Microsoft Power Platform at iba pa, na sumusuporta sa paggamit ng mga prompt upang makamit ang isang bagay.

Para idagdag ang ganitong karanasan sa isang app, kailangan mong maunawaan ang mga konsepto tulad ng prompt, completion at pumili ng isang library na gagamitin. Ito ang eksaktong matututunan mo sa kabanatang ito.

## Panimula

Sa kabanatang ito, malalaman mo ang mga sumusunod:

- Matutunan ang tungkol sa openai library at mga pangunahing konsepto nito.
- Gumawa ng isang text generation app gamit ang openai.
- Unawain kung paano gamitin ang mga konsepto tulad ng prompt, temperature, at tokens sa paggawa ng isang text generation app.

## Mga Layuning Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- Ipaliwanag kung ano ang isang text generation app.
- Gumawa ng isang text generation app gamit ang openai.
- I-configure ang iyong app upang gumamit ng mas maraming o mas kaunting tokens at baguhin ang temperature para sa iba't ibang resulta.

## Ano ang isang text generation app?

Karaniwan kapag gumagawa ka ng isang app, mayroong itong uri ng interface tulad ng mga sumusunod:

- Batay sa command. Ang mga console apps ay mga typical na apps kung saan nagta-type ka ng command at isinasagawa nito ang isang gawain. Halimbawa, ang `git` ay isang command-based app.
- User interface (UI). Ang ilang mga app ay may graphical user interfaces (GUIs) kung saan nagki-click ka ng mga button, naglalagay ng teksto, pumipili ng mga option at iba pa.

### Limitado ang Console at UI apps

Ihambing ito sa isang command-based app kung saan nagta-type ka ng command:

- **Limitado ito**. Hindi mo basta-basta matatype ang anumang command, kundi yung mga sinusuportahan lang ng app.
- **Nakasentro sa wika**. Ang ilan sa mga app ay sumusuporta sa maraming wika, ngunit sa default, ang app ay ginawa para sa isang partikular na wika, kahit na maaari kang magdagdag ng suporta sa ibang wika.

### Mga Benepisyo ng Itext Generation Apps

Kaya paano naiiba ang isang text generation app?

Sa isang text generation app, mayroon kang mas maraming kalayaan, hindi ka limitado sa isang set ng mga command o isang partikular na input language. Sa halip, maaari kang gumamit ng natural na wika upang makipag-ugnayan sa app. Isa pang benepisyo ay na ikaw ay nakikipag-ugnayan na sa isang data source na na-train sa isang malawak na corpus ng impormasyon, samantalang ang isang tradisyunal na app ay maaaring limitado sa kung ano ang nasa database.

### Ano ang maaari kong gawin gamit ang isang text generation app?

Maraming bagay ang maaari mong gawin. Halimbawa:

- **Isang chatbot**. Isang chatbot na sumasagot sa mga tanong tungkol sa mga paksa tulad ng iyong kumpanya at mga produkto nito ay maaaring maging angkop.
- **Helper**. Magaling ang LLMs sa mga bagay tulad ng pagsasummarize ng teksto, pagkuha ng mga insight mula sa teksto, paggawa ng teksto tulad ng mga resume at marami pa.
- **Code assistant**. Depende sa language model na gagamitin mo, maaari kang gumawa ng code assistant na tumutulong sa pag-sulat ng code. Halimbawa, maaari mong gamitin ang mga produkto tulad ng GitHub Copilot pati na rin ang ChatGPT para tulungan kang magsulat ng code.

## Paano ako makakapagsimula?

Kailangan mong hanapan ng paraan upang makipag-integrate sa isang LLM na karaniwang nangangailangan ng dalawang sumusunod na pamamaraan:

- Gumamit ng API. Dito ay bumubuo ka ng mga web request gamit ang iyong prompt at nakakakuha ng generated na teksto pabalik.
- Gumamit ng library. Ang mga library ay tumutulong mag-encapsulate sa mga API call at ginagawang mas madaling gamitin ang mga ito.

## Mga Library/SDKs

May ilang kilalang library para sa pagtatrabaho sa mga LLM tulad ng:

- **openai**, ang library na ito ay nagpapadali upang kumonekta sa iyong model at magpadala ng mga prompt.

Mayroon din mga library na gumagana sa mas mataas na antas tulad ng:

- **Langchain**. Kilala ang Langchain at sinusuportahan ang Python.
- **Semantic Kernel**. Ang Semantic Kernel ay isang library mula sa Microsoft na sumusuporta sa mga wika tulad ng C#, Python, at Java.

## Unang app gamit ang openai

Tingnan natin kung paano tayo makakagawa ng unang app, ano ang mga kailangang library, kung gaano kalaki ang kailangan at iba pa.

### I-install ang openai

Maraming mga library na magagamit para makipag-ugnayan sa OpenAI o Azure OpenAI. Posible ring gumamit ng maraming programming languages gaya ng C#, Python, JavaScript, Java at iba pa. Pinili naming gamitin ang `openai` Python library, kaya gagamitin namin ang `pip` upang i-install ito.

```bash
pip install openai
```

### Gumawa ng resource

Kailangan mong gawin ang mga sumusunod na hakbang:

- Gumawa ng account sa Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Kumuha ng access sa Azure OpenAI. Pumunta sa [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) at humingi ng access.

  > [!NOTE]
  > Sa oras ng pagsulat, kailangan mong mag-apply para sa access sa Azure OpenAI.

- Mag-install ng Python <https://www.python.org/>
- Nakagawa ng Azure OpenAI Service resource. Tingnan ang gabay na ito kung paano [lumikha ng resource](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Hanapin ang API key at endpoint

Sa puntong ito, kailangan mong sabihin sa iyong `openai` library kung anong API key ang gagamitin. Para mahanap ang iyong API key, pumunta sa "Keys and Endpoint" na seksyon ng iyong Azure OpenAI resource at kopyahin ang "Key 1" na halaga.

![Mga Keys at Endpoint resource blade sa Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Ngayon na nakuha mo na ang impormasyong ito, gagabayan natin ang mga library na gamitin ito.

> [!NOTE]
> Mabuting paghiwalayin ang iyong API key mula sa iyong code. Maaari mo itong gawin gamit ang environment variables.
>
> - Itakda ang environment variable `OPENAI_API_KEY` sa iyong API key.
>   `export OPENAI_API_KEY='sk-...'`

### I-setup ang configuration sa Azure

Kung ginagamit mo ang Azure OpenAI (na ngayon ay bahagi ng Microsoft Foundry), ganito ang pagsesetup ng configuration. Ginagamit namin ang standard `OpenAI` client na naka-point sa Azure OpenAI `/openai/v1/` endpoint, na gumagana sa Responses API at hindi kailangan ng `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Sa itaas, itinatakda namin ang mga sumusunod:

- `api_key`, ito ang iyong API key na makikita sa Azure Portal o Microsoft Foundry portal.
- `base_url`, ito ang iyong Foundry resource endpoint na may `/openai/v1/` na nakalakip. Ang stable v1 endpoint ay gumagana sa OpenAI at Azure OpenAI nang walang `api_version` na pamamahala.

> [!NOTE] > Ang `os.environ` ay nagbabasa ng mga environment variables. Maaari mo itong gamitin upang basahin ang mga environment variable tulad ng `AZURE_OPENAI_API_KEY` at `AZURE_OPENAI_ENDPOINT`. Itakda ang mga environment variable na ito sa iyong terminal o gamit ang isang library tulad ng `dotenv`.

## Paggawa ng teksto

Ang paraan upang gumawa ng teksto ay gamitin ang Responses API sa pamamagitan ng `responses.create` method. Heto ang isang halimbawa:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

Sa code sa itaas, gumawa tayo ng response at ipinasok ang model na gusto nating gamitin pati na ang prompt. Pagkatapos ay prinint natin ang generated text gamit ang `response.output_text`.

### Multi-turn conversations

Ang Responses API ay angkop para sa parehong single-turn na text generation at multi-turn na chatbots - nagbibigay ka ng listahan ng mga mensahe sa `input` upang buuin ang isang pag-uusap:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Higit pang detalye tungkol sa functionality na ito sa susunod na kabanata.

## Ehersisyo - ang iyong unang text generation app

Ngayon na natutunan natin kung paano i-setup at i-configure ang openai, panahon na upang gawin ang iyong unang text generation app. Upang gawin ito, sundin ang mga sumusunod na hakbang:

1. Gumawa ng virtual environment at i-install ang openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Kung gumagamit ka ng Windows, i-type ang `venv\Scripts\activate` imbes na `source venv/bin/activate`.

   > [!NOTE]
   > Hanapin ang iyong Azure OpenAI key sa pamamagitan ng pagpunta sa [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) at hanapin ang `Open AI` piliin ang `Open AI resource` at pagkatapos ay piliin ang `Keys and Endpoint` at kopyahin ang `Key 1` na halaga.

1. Gumawa ng isang _app.py_ file at ibigay dito ang sumusunod na code:

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
   > Kung gumagamit ka ng plain OpenAI (hindi Azure), gamitin ang `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (walang `base_url`) at ipasa ang pangalan ng model tulad ng `gpt-5-mini` imbes na deployment name.

   Dapat mong makita ang output na katulad ng sumusunod:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Iba't ibang uri ng prompts, para sa iba't ibang bagay

Ngayon ay nakita mo kung paano gumawa ng teksto gamit ang isang prompt. Mayroon ka ring program na tumatakbo na maaari mong baguhin upang gumawa ng iba't ibang uri ng teksto.

Maaaring gamitin ang mga prompt para sa iba't ibang gawain. Halimbawa:

- **Gumawa ng isang uri ng teksto**. Halimbawa, maaari kang gumawa ng tula, mga tanong para sa isang pagsusulit, atbp.
- **Maghanap ng impormasyon**. Maaari mong gamitin ang mga prompt upang maghanap ng impormasyon tulad ng halimbawa, 'Ano ang ibig sabihin ng CORS sa web development?'.
- **Gumawa ng code**. Maaari mong gamitin ang mga prompt upang gumawa ng code, halimbawa paggawa ng regular expression na ginagamit para i-validate ang mga email o bakit hindi gumawa ng buong programa, tulad ng isang web app?

## Isang mas praktikal na kaso: isang recipe generator

Isipin mong mayroon kang mga sangkap sa bahay at gusto mong magluto ng isang bagay. Para dito, kailangan mo ng recipe. Isang paraan upang makahanap ng mga recipe ay gumamit ng search engine o maaari kang gumamit ng isang LLM para dito.

Maaari kang magsulat ng prompt tulad nito:

> "Ipakita sa akin ang 5 recipe para sa isang ulam na may sumusunod na sangkap: manok, patatas, at karot. Sa bawat recipe, ilista lahat ng sangkap na ginamit"

Batay sa prompt sa itaas, maaaring makakuha ka ng tugon na katulad nito:

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

Maganda ang resulta na ito, alam ko na kung ano ang lulutuin. Sa puntong ito, ang mga posibleng kapaki-pakinabang na pagpapabuti ay:

- Pagsala sa mga sangkap na hindi ko gusto o ako ay may allergy.
- Gumawa ng shopping list, sakaling hindi ko pa lahat ng sangkap sa bahay.

Para sa mga nabanggit na kaso, magdagdag tayo ng karagdagang prompt:

> "Pakialis ang mga recipe na may bawang dahil ako ay allergic at palitan ito ng iba. Gayundin, paki-produce ang shopping list para sa mga recipe, isinasaalang-alang na mayroon na akong manok, patatas at karot sa bahay."

Ngayon ay may bago kang resulta, na ganito:

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

Ito ang iyong limang recipe, walang binanggit na bawang at mayroon ka ring shopping list batay sa mga mayroon ka sa bahay.

## Ehersisyo - gumawa ng recipe generator

Ngayon na na-play out na natin ang isang scenario, sumulat tayo ng code para tumugma sa ipinakitang scenario. Sundin ang mga hakbang na ito:

1. Gamitin ang kasalukuyang _app.py_ file bilang panimulang punto
1. Hanapin ang variable na `prompt` at palitan ang code nito ng sumusunod:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Kapag pinatakbo mo na ang code, dapat kang makakita ng output na katulad nito:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > TANDAAN, ang iyong LLM ay nondeterministic, kaya maaaring makakuha ka ng iba't ibang resulta sa bawat pagpapatakbo ng programa.

   Maganda, tingnan natin kung paano natin mapapabuti ang mga bagay. Para mapabuti ito, gusto nating siguraduhin na flexible ang code, kaya ang mga sangkap at bilang ng mga recipe ay maaaring baguhin at paunlarin.

1. Baguhin natin ang code sa ganitong paraan:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Ang pagsusubok sa code ay maaaring ganito:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Pagbutihin sa pagdagdag ng filter at shopping list

Mayroon na tayong gumaganang app na kayang gumawa ng mga recipe at flexible dahil umaasa ito sa input mula sa gumagamit, pati na sa bilang ng mga recipe at sa mga sangkap na ginamit.

Para lalo pa itong mapabuti, gusto nating idagdag ang mga sumusunod:

- **I-filter ang mga sangkap**. Gusto nating ma-filter ang mga sangkap na hindi natin gusto o tayo ay allergic. Para magawa ito, maaari nating baguhin ang kasalukuyang prompt at magdagdag ng filter condition sa dulo nito ng ganito:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Sa itaas, dinagdag natin ang `{filter}` sa dulo ng prompt at kinukuha rin natin ang value ng filter mula sa gumagamit.

  Ang isang halimbawa ng input sa pagpapatakbo ng programa ay maaaring ganito:

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

  Makikita mo na ang mga recipe na may gatas ay na-filter out na. Ngunit, kung ikaw ay lactose intolerant, maaaring gusto mong i-filter ang mga recipe na may keso rin, kaya kailangan itong ipaliwanag ng malinaw.

- **Gumawa ng shopping list**. Gusto nating gumawa ng shopping list, isinasaalang-alang ang mga mayroon na tayo sa bahay.

  Para sa functionality na ito, maaari nating subukang ayusin lahat sa isang prompt o hatiin ito sa dalawang prompt. Subukan natin ang pangalawang approach. Narito ang iminungkahing idagdag ang karagdagang prompt, ngunit para gumana ito, kailangan nating idagdag ang resulta ng unang prompt bilang konteksto sa ikalawang prompt.

  Hanapin sa code ang bahagi na nagpapakita ng resulta mula sa unang prompt at idagdag ang sumusunod na code sa ibaba nito:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Tandaan ang mga sumusunod:

  1. Gumagawa tayo ng bagong prompt sa pamamagitan ng pagdagdag ng resulta mula sa unang prompt sa bagong prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Gumawa tayo ng bagong request, ngunit isinasaalang-alang ang bilang ng tokens na hiniling natin sa unang prompt, kaya sa oras na ito sinabi natin na `max_output_tokens` ay 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Kapag pinaandar ang code na ito, makakakuha tayo ng sumusunod na output:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Pagbutihin ang iyong setup

Ang mayroon tayo sa ngayon ay code na gumagana, ngunit may ilang mga pagsasaayos na dapat nating gawin upang mas mapabuti pa ang mga bagay. Ilan sa mga dapat nating gawin ay:

- **Ihiwalay ang mga sikreto mula sa code**, tulad ng API key. Hindi dapat kasama sa code ang mga sikreto at dapat itong itago sa isang ligtas na lugar. Para mahiwalay ang mga sikreto mula sa code, maaari nating gamitin ang mga environment variable at mga library tulad ng `python-dotenv` upang i-load ang mga ito mula sa isang file. Ganito ang magiging itsura nito sa code:

  1. Gumawa ng isang `.env` file na may sumusunod na nilalaman:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Tandaan, para sa Azure OpenAI sa Microsoft Foundry, kailangan mong itakda ang mga sumusunod na environment variable:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Sa code, i-load mo ang mga environment variable ng ganito:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Isang salita tungkol sa haba ng token**. Dapat nating isaalang-alang kung ilang token ang kailangan natin upang mabuo ang text na gusto natin. May halaga ang tokens, kaya kung maaari, dapat tayong maging maingat sa dami ng token na ginagamit natin. Halimbawa, maaari ba nating ayusin ang prompt upang magamit ng mas kaunting token?

  Para baguhin ang ginagamit na token, maaari mong gamitin ang parameter na `max_output_tokens`. Halimbawa, kung gusto mong gumamit ng 100 tokens, gagawin mo ito:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Pagsubok sa temperature**. Ang temperature ay isang bagay na hindi pa natin nabanggit ngunit mahalaga sa konteksto ng kung paano gumagana ang ating programa. Kapag mas mataas ang halaga ng temperature, mas random ang magiging output. Sa kabilang banda, kapag mas mababa ang temperature, mas predictable ang output. Isaalang-alang kung gusto mo ng pagkakaiba-iba sa output o hindi.

  Para baguhin ang temperature, maaari mong gamitin ang parameter na `temperature`. Halimbawa, kung gusto mong gumamit ng temperature na 0.5, gagawin mo ito:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Tandaan, kapag mas malapit sa 1.0, mas nagiging varied ang output.

- **Hindi gumagamit ang mga reasoning models ng `temperature`**. Ito ay isang mahalagang pagbabago sa 2026. Ang kasalukuyan, hindi pa deprecate na mga modelo sa Microsoft Foundry ay **reasoning models** (ang pamilya ng GPT-5, o-series) - at **hindi sinusuportahan ang `temperature` o `top_p`** (gaya ng hindi rin ang `max_tokens`; gamitin ang `max_output_tokens`). Kung magpapadala ka ng `temperature` sa `gpt-5-mini` makakatanggap ka ng error na "parameter not supported". Kaya para subukan ang halimbawa ng temperature sa itaas, ituro ito sa modelong sumusuporta pa rin sa sampling controls - halimbawa isang bukas na **Llama** model tulad ng `Llama-3.3-70B-Instruct` mula sa [Microsoft Foundry model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), na tinatawagan sa pamamagitan ng Foundry Models / Azure AI Inference endpoint (katulad ng paraan ng `githubmodels-*` samples). Para sa mga reasoning models gaya ng GPT-5, ibang paraan ang pagtutok sa output:
  - **Prompt engineering** - malinaw na mga instruksyon, mga halimbawa, at istrakturadong output (tingnan ang aralin [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) ang gumagawa ng trabaho na dating ginagawa ng mga sampling knobs.
  - **Mga kontrol sa pangangatwiran** - mga parameter tulad ng pagsisikap sa pangangatwiran/kalabisan na tinitimbang ang lalim ng pangangatwiran laban sa pagkaantala at gastos.

  Sa madaling salita: `temperature`/`top_p` ay nananatiling balido sa maraming modelo (Llama, Mistral, Phi, at ang pamilya ng GPT-4.x - kahit na ang GPT-4.x ay unti-unting hindi na ginagamit), ngunit ang direksyon ng pag-unlad ay prompt engineering + mga kontrol sa pangangatwiran sa mga reasoning models tulad ng GPT-5.

## Takdang Aralin

Para sa takdang araling ito, maaari kang pumili kung ano ang gagawin mo.

Narito ang ilang mga mungkahi:

- Ayusin pa ang recipe generator app upang lalo pa itong mapabuti. Maglaro sa mga temperature values, at sa mga prompts upang makita kung ano ang maaari mong malikha.
- Gumawa ng "study buddy". Ang app na ito ay dapat kaya na sagutin ang mga tanong tungkol sa isang paksa, halimbawa Python, maaari kang magkaroon ng mga prompt tulad ng "Ano ang isang partikular na paksa sa Python?", o maaari kang magkaroon ng prompt na nagsasabing, ipakita sa akin ang code para sa isang partikular na paksa atbp.
- History bot, gawing buhay ang kasaysayan, utusan ang bot na gumanap bilang isang partikular na karakter sa kasaysayan at tanungin ito tungkol sa buhay at panahon nito.

## Solusyon

### Study buddy

Nasa ibaba ang panimulang prompt, tingnan kung paano mo ito magagamit at ayusin ayon sa iyong gusto.

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

## Pagsusuri ng Kaalaman

Ano ang ginagawa ng konsepto ng temperature?

1. Kinokontrol nito kung gaano ka-random ang output.
1. Kinokontrol nito kung gaano kalaki ang tugon.
1. Kinokontrol nito kung ilang token ang ginagamit.

## 🚀 Hamon

Kapag nagtatrabaho sa assignment, subukang baguhin ang temperature, subukang itakda ito sa 0, 0.5, at 1. Tandaan na ang 0 ay ang pinaka-kaunti ang pagkakaiba at ang 1 ang pinakamarami. Anong halaga ang pinakamainam para sa iyong app?

## Napakahusay na Trabaho! Ipagpatuloy ang Iyong Pag-aaral

Pagkatapos makumpleto ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pag-level up ng iyong kaalaman sa Generative AI!

Pumunta sa Lesson 7 kung saan titingnan natin kung paano [gumawa ng mga chat application](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->