# Pagbuo ng Mga Aplikasyon para sa Text Generation

[![Building Text Generation Applications](../../../translated_images/tl/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(I-click ang larawan sa itaas upang panoorin ang video ng araling ito)_

Nakita mo na sa kurikulum na ito na may mga pangunahing konsepto tulad ng prompts at pati na rin ang isang buong disiplina na tinatawag na "prompt engineering". Maraming mga tool na maaari mong makipag-ugnayan tulad ng ChatGPT, Office 365, Microsoft Power Platform at iba pa, na sumusuporta sa iyo sa paggamit ng prompts upang makamit ang isang bagay.

Para maidagdag mo ang ganitong karanasan sa isang app, kailangan mong maunawaan ang mga konsepto tulad ng prompts, completions at pumili ng isang library na gagamitin. Iyan mismo ang iyong matututuhan sa kabanatang ito.

## Panimula

Sa kabanatang ito, ikaw ay:

- Matututo tungkol sa openai library at ang mga pangunahing konsepto nito.
- Gagawa ng isang text generation app gamit ang openai.
- Maiintindihan kung paano gamitin ang mga konsepto tulad ng prompt, temperature, at tokens upang bumuo ng isang text generation app.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- Ipaliwanag kung ano ang isang text generation app.
- Bumuo ng isang text generation app gamit ang openai.
- I-configure ang iyong app upang gumamit ng mas marami o mas kaunting tokens at pati na rin baguhin ang temperature, para sa isang varied na output.

## Ano ang isang text generation app?

Karaniwan kapag gumagawa ka ng app, ito ay may uri ng interface tulad ng sumusunod:

- Batay sa command. Ang mga console apps ay karaniwang apps kung saan ikaw ay nagta-type ng command at ito ay nagsasagawa ng isang gawain. Halimbawa, ang `git` ay isang command-based app.
- User interface (UI). Ang ilang apps ay may graphical user interfaces (GUIs) kung saan maaari kang mag-click ng mga button, mag-input ng teksto, pumili ng mga opsyon at iba pa.

### Limitado ang mga Console at UI apps

Ihambing ito sa isang command-based app kung saan nagta-type ka ng command:

- **Ito ay limitado**. Hindi ka maaaring mag-type ng kahit anong command, tanging ang mga sinusuportahan ng app lang.
- **Nakasentro sa wika**. Ang ilang mga app ay sumusuporta sa maraming wika, ngunit sa default ay ginawa para sa isang partikular na wika, kahit na maaari ka namang magdagdag ng suporta para sa iba pang wika.

### Mga Benepisyo ng text generation apps

Kaya paano naiiba ang isang text generation app?

Sa isang text generation app, mayroon kang mas maraming flexibility, hindi ka limitado sa isang set ng mga command o isang partikular na input language. Sa halip, maaari kang gumamit ng natural na wika upang makipag-ugnayan sa app. Isa pang benepisyo ay nakikipag-ugnayan ka na sa isang data source na na-train sa isang malawak na koleksyon ng impormasyon, samantalang ang tradisyunal na app ay maaaring limitado lamang sa kung ano ang nasa database.

### Ano ang maaari kong gawin gamit ang isang text generation app?

Maraming mga bagay ang pwede mong gawin. Halimbawa:

- **Isang chatbot**. Isang chatbot na sumasagot ng mga tanong tungkol sa mga paksang tulad ng iyong kumpanya at mga produkto nito ay maaaring maging angkop.
- **Tumutulong**. Mahusay ang mga LLM sa mga bagay tulad ng pagbuod ng teksto, pagkuha ng mga insight mula sa teksto, paggawa ng teksto tulad ng resume at iba pa.
- **Assistant sa code**. Depende sa language model na ginagamit mo, maaari kang gumawa ng isang code assistant na tumutulong sa pagsulat ng code. Halimbawa, maaari kang gumamit ng mga produkto tulad ng GitHub Copilot pati na rin ang ChatGPT upang tumulong sa pagsulat ng code.

## Paano ako makapagsimula?

Kailangan mong makahanap ng paraan upang makipag-integrate sa isang LLM na karaniwang may dalawang paraan:

- Gumamit ng API. Dito, gumagawa ka ng mga web requests gamit ang iyong prompt at nakakakuha ng generated na teksto pabalik.
- Gumamit ng library. Ang mga libraries ay tumutulong sa pag-encapsulate ng mga API call at ginagawang mas madali ang paggamit.

## Mga Libraries/SDKs

Mayroon ilang kilalang libraries para sa pakikipagtrabaho sa LLMs tulad ng:

- **openai**, ang library na ito ay nagpapadali ng koneksyon sa iyong modelo at pagpapadala ng mga prompt.

Pagkatapos ay may mga libraries na gumagana sa mas mataas na antas tulad ng:

- **Langchain**. Kilala ang Langchain at sumusuporta sa Python.
- **Semantic Kernel**. Ang Semantic Kernel ay isang library mula sa Microsoft na sumusuporta sa mga wikang C#, Python, at Java.

## Unang app gamit ang openai

Tingnan natin kung paano tayo makakagawa ng unang app, anong mga libraries ang kailangan, magkano ang kailangang gawin, atbp.

### Mag-install ng openai

Maraming mga libraries na pwede gamitin para makipag-ugnayan sa OpenAI o Azure OpenAI. Posible ring gumamit ng iba't ibang programming languages tulad ng C#, Python, JavaScript, Java at iba pa. Pinili namin gamitin ang `openai` Python library, kaya gagamitin namin ang `pip` para i-install ito.

```bash
pip install openai
```

### Gumawa ng resource

Kailangan mong gawin ang mga sumusunod na hakbang:

- Gumawa ng account sa Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Kumuha ng access sa Azure OpenAI. Pumunta sa [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) at mag-request ng access.

  > [!NOTE]
  > Sa panahon ng pagsulat, kailangan mong mag-apply para sa access sa Azure OpenAI.

- Mag-install ng Python <https://www.python.org/>
- Gumawa ng Azure OpenAI Service resource. Tingnan ang gabay kung paano [gumawa ng resource](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Hanapin ang API key at endpoint

Sa puntong ito, kailangan mong sabihin sa iyong `openai` library kung anong API key ang gagamitin. Para mahanap ang iyong API key, pumunta sa seksyon na "Keys and Endpoint" ng iyong Azure OpenAI resource at kopyahin ang "Key 1" na value.

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Ngayon na nakopya mo na ang impormasyong ito, ituturo natin sa mga library na gamitin ito.

> [!NOTE]
> Makabubuting ihiwalay ang iyong API key mula sa iyong code. Magagawa mo ito sa pamamagitan ng paggamit ng environment variables.
>
> - Itakda ang environment variable na `OPENAI_API_KEY` sa iyong API key.
>   `export OPENAI_API_KEY='sk-...'`

### I-setup ang configuration ng Azure

Kung gumagamit ka ng Azure OpenAI (na ngayon ay bahagi ng Microsoft Foundry), ganito ang paraan ng pag-setup ng configuration. Ginagamit namin ang pangkaraniwang `OpenAI` client na naka-point sa Azure OpenAI `/openai/v1/` endpoint, na gumagana sa Responses API at hindi kailangan ng `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Sa itaas ay itinakda natin ang mga sumusunod:

- `api_key`, ito ang iyong API key na makikita sa Azure Portal o Microsoft Foundry portal.
- `base_url`, ito ang iyong Foundry resource endpoint na may `/openai/v1/` na nakaappend. Ang stable v1 endpoint ay gumagana sa OpenAI at Azure OpenAI nang walang `api_version` management.

> [!NOTE] > `os.environ` ay nagbabasa ng environment variables. Magagamit mo ito para basahin ang mga environment variables tulad ng `AZURE_OPENAI_API_KEY` at `AZURE_OPENAI_ENDPOINT`. Itakda ang mga environment variables na ito sa iyong terminal o gamit ang library tulad ng `dotenv`.

## Paggawa ng teksto

Ang paraan ng paggawa ng teksto ay ang paggamit ng Responses API sa pamamagitan ng `responses.create` method. Narito ang halimbawang code:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

Sa code sa itaas, gumagawa tayo ng response at pinapasa ang model na gusto nating gamitin at ang prompt. Pagkatapos ay pini-print natin ang generated na teksto gamit ang `response.output_text`.

### Mga multi-turn na pag-uusap

Ang Responses API ay angkop para sa parehong single-turn text generation at mga multi-turn chatbot — nagbibigay ka ng listahan ng mga mensahe sa `input` upang bumuo ng pag-uusap:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Higit pa tungkol sa functionality na ito sa susunod na kabanata.

## Ehersisyo - ang iyong unang text generation app

Ngayon na natutunan mo kung paano mag-setup at mag-configure ng openai, panahon na para gawin ang iyong unang text generation app. Para gawin ang iyong app, sundan ang mga hakbang:

1. Gumawa ng virtual environment at i-install ang openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Kung gumagamit ka ng Windows, i-type ang `venv\Scripts\activate` imbes na `source venv/bin/activate`.

   > [!NOTE]
   > Hanapin ang iyong Azure OpenAI key sa pamamagitan ng pagpunta sa [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), hanapin ang `Open AI`, piliin ang `Open AI resource`, at pagkatapos piliin ang `Keys and Endpoint`, kopyahin ang value ng `Key 1`.

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
   > Kung gumagamit ka ng plain OpenAI (hindi Azure), gamitin ang `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (walang `base_url`) at magpasa ng pangalan ng model tulad ng `gpt-5-mini` sa halip na deployment name.

   Makikita mo ang output na tulad ng sumusunod:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Iba't ibang uri ng prompts, para sa iba't ibang bagay

Ngayon ay nakita mo na kung paano gumawa ng teksto gamit ang prompt. Mayroon ka nang programa na tumatakbo na maaari mong baguhin upang makagawa ng iba't ibang uri ng teksto.

Ang mga prompts ay maaaring gamitin para sa lahat ng uri ng gawain. Halimbawa:

- **Gumawa ng isang uri ng teksto**. Halimbawa, maaari kang gumawa ng isang tula, mga tanong para sa quiz, atbp.
- **Maghanap ng impormasyon**. Maaari mong gamitin ang prompts para humanap ng impormasyon tulad ng halimbawa 'Ano ang ibig sabihin ng CORS sa web development?'.
- **Gumawa ng code**. Maaari kang gumamit ng prompts para gumawa ng code, halimbawa pag-develop ng regular expression na ginagamit para validasyon ng mga email o bakit hindi gumawa ng isang buong programa, tulad ng web app?

## Isang mas praktikal na halimbawa: isang recipe generator

Isipin na mayroon kang mga sangkap sa bahay at gusto mong magluto ng isang bagay. Para dito, kailangan mo ng recipe. Isang paraan upang makahanap ng recipes ay ang paggamit ng search engine o maaari mong gamitin ang LLM para dito.

Maaari kang magsulat ng prompt tulad nito:

> "Ipakita sa akin ang 5 recipe para sa ulam gamit ang mga sumusunod na sangkap: manok, patatas, at karot. Sa bawat recipe, ilista ang lahat ng mga sangkap na ginamit"

Batay sa prompt sa itaas, maaaring makakuha ka ng sagot katulad ng:

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

Maganda ang resulta nito, alam ko na kung ano ang lulutuin. Sa puntong ito, ang mga maaaring maging kapaki-pakinabang na pagpapabuti ay:

- Pagsala ng mga sangkap na ayaw ko o delikado ako rito.
- Gumawa ng shopping list, kung sakaling wala ako ng lahat ng sangkap sa bahay.

Para sa mga nabanggit, magdagdag tayo ng karagdagang prompt:

> "Pakibura ang mga recipe na may bawang dahil ako ay may allergy at palitan ito ng ibang sangkap. At gumawa rin ng shopping list para sa mga recipe, kung saan isinaalang-alang na mayroon na akong manok, patatas, at karot sa bahay."

Ngayon ay mayroon kang bagong resulta, ito ay:

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

Yan ang limang recipe mo, na walang binanggit na bawang at mayroon ka ring shopping list base sa mga sangkap na meron ka na sa bahay.

## Ehersisyo - gumawa ng isang recipe generator

Ngayon na naglaro na tayo ng isang senaryo, isusulat naman natin ang code para tugunan ang iprinisintang senaryo. Sundin ang mga hakbang:

1. Gamitin ang umiiral na _app.py_ file bilang panimulang punto
1. Hanapin ang variable na `prompt` at palitan ang code nito ng sumusunod:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Kung patakbuhin mo ngayon ang code, makakakita ka ng output na katulad nito:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > PAALALA, ang iyong LLM ay non-deterministic, kaya maaaring makakuha ka ng iba't ibang resulta sa bawat pagpapatakbo ng programa.

   Magaling, tingnan natin kung paano pa ito mapapaayos. Para mapabuti ang mga bagay, gusto nating gawing flexible ang code, kaya ang mga sangkap at bilang ng mga recipe ay maaaring baguhin.

1. Baguhin natin ang code nang ganito:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Ang code para sa test run ay maaaring maging ganito:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Pagbutihin sa pamamagitan ng pagdagdag ng filter at shopping list

Mayroong tayo ngayong gumaganang app na kayang gumawa ng mga recipe at ito ay flexible dahil umaasa sa input mula sa user, parehong sa bilang ng mga recipe pati na rin ang mga sangkap na ginamit.

Para lalo pang mapabuti ito, gusto nating idagdag ang mga sumusunod:

- **I-filter ang mga sangkap**. Gusto nating magkakaroon ng kakayahan na ma-filter ang mga sangkap na ayaw natin o may allergy tayo. Para gawin ito, maaari nating baguhin ang dati nating prompt at magdagdag ng kondisyon para sa filter sa dulo ng prompt tulad nito:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Sa itaas, nagdagdag tayo ng `{filter}` sa dulo ng prompt at kinukuha din natin ang filter value mula sa user.

  Narito ang isang halimbawang input para patakbuhin ang programa:

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

  Makikita mo na ang anumang mga recipe na may gatas ay na-filter na. Ngunit kung lactose intolerant ka, maaaring gusto mong i-filter din ang mga recipe na may keso, kaya kailangang maging malinaw.

- **Gumawa ng shopping list**. Gusto nating gumawa ng shopping list, isinasaalang-alang na mayroon na tayong ilang sangkap sa bahay.

  Para sa functionality na ito, maaari nating subukan lutasin lahat sa isang prompt o hatiin ito sa dalawang prompts. Subukan natin ang huli. Sa ganitong paraan magdadagdag tayo ng karagdagang prompt, ngunit para gumana ito, kailangan nating idagdag ang resulta mula sa unang prompt bilang konteksto sa pangalawang prompt.

  Hanapin ang bahagi ng code na nagpi-print ng resulta mula sa unang prompt at idagdag ang sumusunod na code sa ibaba nito:

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

  1. Gumagawa tayo ng bagong request, ngunit isinasaalang-alang ang bilang ng tokens na hiniling sa unang prompt, kaya sa pagkakataong ito sinasabi natin na `max_output_tokens` ay 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Sa pagtakbo ng code na ito, makakakuha tayo ng sumusunod na output:

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

Ang meron tayo ngayon ay code na gumagana, ngunit may mga ilang pagbabago na dapat nating gawin upang mapabuti pa ito. Ilan sa mga dapat nating gawin ay:

- **Ihiwalay ang mga sikreto mula sa code**, tulad ng API key. Ang mga sikreto ay hindi dapat kasama sa code at dapat itago sa isang ligtas na lugar. Para ihiwalay ang mga sikreto mula sa code, maaari nating gamitin ang mga environment variable at mga library tulad ng `python-dotenv` para i-load ang mga ito mula sa isang file. Ganito ang hitsura nito sa code:

  1. Gumawa ng isang `.env` na file na may sumusunod na nilalaman:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Tandaan, para sa Azure OpenAI sa Microsoft Foundry, kailangan mong itakda ang mga sumusunod na environment variable:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Sa code, gagamitin mo ang pag-load ng environment variables tulad nito:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Isang salita tungkol sa haba ng token**. Dapat nating isaalang-alang kung ilang token ang kailangan para mabuo ang teksto na gusto natin. May bayad ang mga token, kaya kung saan posible, dapat tayong maging matipid sa bilang ng mga token na ginagamit. Halimbawa, maaari ba nating iayos ang prompt para mas kaunti ang magamit na token?

  Para baguhin ang bilang ng token, maaari mong gamitin ang parameter na `max_output_tokens`. Halimbawa, kung gusto mong gumamit ng 100 token, ito ang gagawin mo:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Pagsubok sa temperature**. Ang temperature ay isang bagay na hindi pa natin nababanggit ngunit mahalaga sa konteksto kung paano gumagana ang ating programa. Kapag mas mataas ang value ng temperature, mas random ang magiging output. Sa kabilang banda, kapag mas mababa ang temperature, mas predictable ang output. Isaalang-alang kung gusto mo ng pagkakaiba-iba sa output mo o hindi.

  Para baguhin ang temperature, maaari mong gamitin ang parameter na `temperature`. Halimbawa, kung gusto mong gamitin ang temperature na 0.5, ito ang gagawin mo:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Tandaan, kapag mas malapit sa 1.0, mas nagiging iba-iba ang output.

- **Ang mga reasoning models ay hindi gumagamit ng `temperature`**. Ito ay isang mahalagang pagbabago para sa 2026. Ang kasalukuyang mga non-deprecated na modelo sa Microsoft Foundry ay mga **reasoning models** (ang GPT-5 family, o-series) - at hindi sila **sumusuporta sa `temperature` o `top_p`** (pati na rin sa `max_tokens`; gamitin ang `max_output_tokens`). Kung magpapadala ka ng `temperature` sa `gpt-5-mini` makakatanggap ka ng error na "parameter not supported." Kaya upang subukan ang halimbawa ng temperature sa itaas, gamitin ang modelong sumusuporta pa sa sampling controls - halimbawa isang open **Llama** model tulad ng `Llama-3.3-70B-Instruct` mula sa [Microsoft Foundry model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), tinatawag gamit ang Foundry Models / Azure AI Inference endpoint (pareho ng paraan sa `githubmodels-*` samples). Para naman sa mga reasoning models tulad ng GPT-5, iba ang paraan ng pag-steer ng output:
  - **Prompt engineering** - malinaw na instruksyon, mga halimbawa, at istrakturadong output (tingnan ang aralin [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) ang gumagampan sa trabaho na dating ginagawa ng sampling knobs.
  - **Reasoning controls** - mga parameter tulad ng reasoning effort/verbosity na nagsusukat ng lalim ng pag-iisip laban sa latency at gastos.

  Sa madaling salita: ang `temperature`/`top_p` ay valid pa rin sa maraming modelo (Llama, Mistral, Phi, at GPT-4.x family - kahit na unti-unting tinatanggal ang GPT-4.x), ngunit ang direksyon ay nasa prompt engineering + reasoning controls sa mga reasoning models tulad ng GPT-5.

## Takdang Aralin

Para sa takdang araling ito, maaari kang pumili ng iyong gagawin.

Narito ang ilang mga suhestiyon:

- Baguhin ang recipe generator app para lalo pang mapabuti. Mag-eksperimento sa mga values ng temperature, at mga prompt upang makita kung ano ang maaari mong mabuo.
- Gumawa ng isang "study buddy". Ang app na ito ay dapat kayang sagutin ang mga tanong tungkol sa isang paksa, halimbawa Python, maaari kang gumawa ng mga prompt tulad ng "Ano ang isang tiyak na paksa sa Python?", o isang prompt na nagsasabi, ipakita sa akin ang code para sa isang tiyak na paksa, atbp.
- History bot, gawing buhay ang kasaysayan, utusan ang bot na maging isang tiyak na makasaysayang karakter at magtanong tungkol sa kanyang buhay at panahon.

## Solusyon

### Study buddy

Narito ang isang panimulang prompt, tingnan kung paano mo ito magagamit at mababago ayon sa gusto mo.

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
1. Kinokontrol nito kung gaano kalaki ang sagot.
1. Kinokontrol nito kung ilang token ang ginagamit.

## 🚀 Hamon

Kapag nagtatrabaho sa takdang aralin, subukan mong baguhin ang temperature, subukan ito sa 0, 0.5, at 1. Tandaan na ang 0 ay ang pinaka-kaunting pagkakaiba at ang 1 ay ang pinakamarami. Aling value ang pinakamainam para sa iyong app?

## Mahusay na Gawain! Ipagpatuloy ang Iyong Pagkatuto

Pagkatapos matapos ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pagpapalawak ng iyong kaalaman sa Generative AI!

Pumunta sa Lesson 7 kung saan titingnan natin kung paano [gumawa ng chat applications](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->