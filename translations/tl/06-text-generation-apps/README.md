# Paggawa ng Mga Aplikasyon sa Text Generation

[![Building Text Generation Applications](../../../translated_images/tl/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(I-click ang larawan sa itaas upang panoorin ang video ng araling ito)_

Nakita mo na sa kurikulum na ito na may pangunahing mga konsepto tulad ng mga prompt at mayroon ding buong disiplina na tinatawag na "prompt engineering". Maraming mga tool na maaari mong gamitin gaya ng ChatGPT, Office 365, Microsoft Power Platform at iba pa, na sumusuporta sa iyo gamit ang mga prompt upang makamit ang isang bagay.

Para maidagdag mo ang ganitong karanasan sa isang app, kailangan mong maunawaan ang mga konsepto tulad ng mga prompt, completions at pumili ng isang library para gamitin. Iyan mismo ang matututuhan mo sa kabanatang ito.

## Panimula

Sa kabanatang ito, ikaw ay:

- Matututo tungkol sa openai library at ang mga pangunahing konsepto nito.
- Gumawa ng app na nagsasagawa ng text generation gamit ang openai.
- Maunawaan kung paano gamitin ang mga konsepto tulad ng prompt, temperature, at tokens upang makabuo ng text generation app.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- Ipaliwanag kung ano ang text generation app.
- Gumawa ng text generation app gamit ang openai.
- I-configure ang iyong app upang gumamit ng mas maraming o mas kaunting tokens at baguhin ang temperature, para sa iba't ibang output.

## Ano ang text generation app?

Karaniwang kapag gumagawa ka ng app, ito ay may uri ng interface tulad ng sumusunod:

- Batay sa command. Ang mga console apps ay karaniwang mga app kung saan nagta-type ka ng command at ito ay nagsasagawa ng isang gawain. Halimbawa, ang `git` ay isang command-based app.
- User interface (UI). Ang ilang apps ay may graphical user interfaces (GUIs) kung saan nagki-click ka ng mga button, maglalagay ng teksto, pipili ng mga opsyon at iba pa.

### Limitado ang Console at UI apps

Ihambing ito sa isang command-based app kung saan nagta-type ka ng command:

- **Limitado ito**. Hindi ka pwedeng mag-type ng kahit anong command, tanging ang mga sinusuportahan lang ng app.
- **Partikular sa isang wika**. Ang ilang apps ay sumusuporta ng maraming wika, pero karaniwan ang app ay ginawa para sa isang tiyak na wika, kahit pa pwede kang magdagdag ng suporta sa ibang mga wika.

### Mga Benepisyo ng text generation apps

Paano naman nagkakaiba ang text generation app?

Sa isang text generation app, mas malawak ang iyong kalayaan, hindi ka limitado sa isang set ng mga command o isang partikular na input na wika. Sa halip, maaari mong gamitin ang natural na wika upang makipag-ugnayan sa app. Isa pang benepisyo ay nakikipag-ugnayan ka na sa isang data source na na-train sa malawak na koleksyon ng impormasyon, habang ang tradisyunal na app ay maaaring limitado lang sa nasa database.

### Ano ang maaari kong gawin gamit ang text generation app?

Maraming bagay ang maaari mong gawin. Halimbawa:

- **Chatbot**. Isang chatbot na sumasagot sa mga katanungan tungkol sa mga paksa, tulad ng iyong kumpanya at mga produkto nito ay maaaring maging magandang halimbawa.
- **Helper**. Magaling ang LLM sa mga bagay tulad ng pagbubuod ng teksto, pagkuha ng mga insight mula sa teksto, paggawa ng teksto tulad ng mga resume at iba pa.
- **Code assistant**. Depende sa language model na gamit mo, maaari kang gumawa ng code assistant na tumutulong sa iyo magsulat ng code. Halimbawa, maaari mong gamitin ang produkto tulad ng GitHub Copilot pati na rin ang ChatGPT upang tumulong sa pagsusulat ng code.

## Paano ako makakapagsimula?

Kailangan mong hanapan ng paraan na makapag-integrate sa LLM na karaniwang may dalawang paraan:

- Gumamit ng API. Dito ikaw ay gumagawa ng mga web request gamit ang iyong prompt at nakakakuha ng generated text bilang tugon.
- Gumamit ng library. Ang mga library ay tumutulong pang-encapsulate ng mga API call at gawing mas madali itong gamitin.

## Mga Library/SDK

May ilang kilalang mga library para sa paggamit ng LLM tulad ng:

- **openai**, ang library na ito ay nagpapadali para kumonekta sa iyong model at magsend ng mga prompt.

Meron ding mga library na gumagana sa mas mataas na antas tulad ng:

- **Langchain**. Kilala ang Langchain at sumusuporta sa Python.
- **Semantic Kernel**. Ang Semantic Kernel ay isang library mula sa Microsoft na sumusuporta sa mga wikang C#, Python, at Java.

## Unang app gamit ang openai

Tingnan natin kung paano tayo makakagawa ng unang app, anong mga library ang kailangan, gaano kalaki ang requirements at iba pa.

### I-install ang openai

Maraming mga library ang available para makipag-ugnayan sa OpenAI o Azure OpenAI. Posible rin gamitin ang iba't ibang mga programming language tulad ng C#, Python, JavaScript, Java at iba pa. Pinili naming gamitin ang `openai` Python library, kaya gagamit tayo ng `pip` para i-install ito.

```bash
pip install openai
```

### Gumawa ng resource

Kailangan mong gawin ang mga sumusunod na hakbang:

- Gumawa ng account sa Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Kumuha ng access sa Azure OpenAI. Pumunta sa [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) at mag-request ng access.

  > [!NOTE]
  > Sa panahon ng pagsulat, kailangan mong mag-apply para sa access sa Azure OpenAI.

- Mag-install ng Python <https://www.python.org/>
- Makagawa ng Azure OpenAI Service resource. Tingnan ang gabay kung paano [gumawa ng resource](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Hanapin ang API key at endpoint

Sa puntong ito, kailangan mong sabihin sa iyong `openai` library kung anong API key ang gagamitin. Para makuha ang iyong API key, pumunta sa "Keys and Endpoint" na seksyon ng iyong Azure OpenAI resource at kopyahin ang "Key 1" na halaga.

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Ngayon na nakopya mo na ang impormasyong ito, instruksyon natin ang mga library para gamitin ito.

> [!NOTE]
> Maganda kung ihiwalay mo ang iyong API key mula sa iyong code. Maaari mo itong gawin gamit ang environment variables.
>
> - I-set ang environment variable na `OPENAI_API_KEY` sa iyong API key.
>   `export OPENAI_API_KEY='sk-...'`

### I-setup ang configuration para sa Azure

Kung gagamit ka ng Azure OpenAI (na ngayon ay bahagi ng Microsoft Foundry), ganito ang pag-setup ng configuration. Ginagamit natin ang standard na `OpenAI` client na nakaturo sa Azure OpenAI `/openai/v1/` endpoint, na gumagana sa Responses API at hindi kailangan ng `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Sa itaas, sinasabi natin ang mga sumusunod:

- `api_key`, ito ang iyong API key na makikita sa Azure Portal o Microsoft Foundry portal.
- `base_url`, ito ang iyong Foundry resource endpoint na may idinagdag na `/openai/v1/`. Ang stable v1 endpoint ay gumagana para sa OpenAI at Azure OpenAI nang walang `api_version` na kailangang i-manage.

> [!NOTE] > Binabasa ng `os.environ` ang mga environment variables. Maaari mo itong gamitin para basahin ang mga environment variables tulad ng `AZURE_OPENAI_API_KEY` at `AZURE_OPENAI_ENDPOINT`. I-set ang mga environment variables na ito sa iyong terminal o gamit ang library tulad ng `dotenv`.

## Pag-generate ng teksto

Ang paraan ng pag-generate ng teksto ay gamit ang Responses API sa pamamagitan ng `responses.create` method. Heto ang isang halimbawa:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # ito ang pangalan ng iyong pag-deploy ng modelo
    input=prompt,
    store=False,
)
print(response.output_text)
```

Sa code sa itaas, gumawa tayo ng response at pinasa ang model na gusto nating gamitin at ang prompt. Pagkatapos ay piniprint natin ang generated text sa pamamagitan ng `response.output_text`.

### Multi-turn na mga pag-uusap

Ang Responses API ay angkop para sa single-turn na text generation at pati na rin para sa multi-turn na chatbots - nagbibigay ka ng listahan ng mga mensahe sa `input` para makabuo ng pag-uusap:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

Karagdagang paliwanag tungkol sa functionality na ito sa mga susunod na kabanata.

## Ehersisyo - ang iyong unang text generation app

Ngayon na natutunan na natin kung paano mag-setup at mag-configure ng openai, panahon na para gawin ang iyong unang text generation app. Para gawin ito, sundin ang mga hakbang:

1. Gumawa ng virtual environment at i-install ang openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Kung nasa Windows ka, i-type ang `venv\Scripts\activate` sa halip ng `source venv/bin/activate`.

   > [!NOTE]
   > Hanapin ang iyong Azure OpenAI key sa pamamagitan ng pagpunta sa [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) at hanapin ang `Open AI` at piliin ang `Open AI resource` tapos piliin ang `Keys and Endpoint` at kopyahin ang `Key 1` na halaga.

1. Gumawa ng _app.py_ file at lagyan ito ng sumusunod na code:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # idagdag ang iyong completion code
   prompt = "Complete the following: Once upon a time there was a"

   # gumawa ng kahilingan gamit ang Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # i-print ang tugon
   print(response.output_text)
   ```

   > [!NOTE]
   > Kung gagamit ka ng plain OpenAI (hindi Azure), gamitin ang `client = OpenAI(api_key="<palitan ito ng iyong OpenAI key>")` (walang `base_url`) at ipasa ang pangalan ng model tulad ng `gpt-4o-mini` sa halip na deployment name.

   Makikita mo ang output na ganito:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Iba't ibang uri ng prompt, para sa iba't ibang gamit

Ngayon ay nakita mo na kung paano mag-generate ng teksto gamit ang prompt. Mayroon ka nang programang tumatakbo na pwedeng baguhin para gumawa ng iba't ibang uri ng teksto.

Maaaring gamitin ang mga prompt para sa lahat ng klase ng gawain. Halimbawa:

- **Mag-generate ng isang uri ng teksto**. Halimbawa, pwede kang gumawa ng tula, mga tanong para sa quiz atbp.
- **Maghanap ng impormasyon**. Pwede mong gamitin ang mga prompt upang maghanap ng impormasyon tulad ng halimbawa: 'Ano ang ibig sabihin ng CORS sa web development?'.
- **Mag-generate ng code**. Pwede mong gamitin ang mga prompt upang gumawa ng code, halimbawa para gumawa ng regular expression na ginagamit sa pag-validate ng email o gumawa ng buong programa tulad ng web app?

## Isang mas praktikal na gamit: isang recipe generator

Isipin mo na may mga sangkap ka sa bahay at gusto mong magluto ng isang pagkain. Para dito, kailangan mo ng recipe. Isang paraan para makahanap ng mga recipe ay gumamit ng search engine o pwede mong gamitin ang LLM para doon.

Maaari kang gumawa ng prompt na ganito:

> "Ipakita ang 5 recipe para sa isang putahe na may mga sumusunod na sangkap: manok, patatas, at karot. Para sa bawat recipe, ilista ang lahat ng sangkap na ginamit"

Batay sa prompt na ito, maaari kang makakuha ng tugon na tulad nito:

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

Maganda ang resulta, alam ko na ang lulutuin. Sa puntong ito, makatutulong ang mga sumusunod na pagpapabuti:

- Pagsala sa mga sangkap na ayaw ko o may allergy ako.
- Gumawa ng shopping list, kung sakaling wala akong lahat ng sangkap sa bahay.

Para sa mga nabanggit na kaso, dagdagan natin ng isa pang prompt:

> "Paki-alis ang mga recipe na may bawang dahil allergic ako at palitan ito ng ibang sangkap. Paki-gawa rin ng shopping list para sa mga recipe, isinasaalang-alang na mayroon na akong manok, patatas, at karot sa bahay."

Ngayon ay may bagong resulta, na:

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

Iyan ang limang recipe mo, walang binanggit na bawang at mayroon ka ring shopping list base sa mga sangkap na mayroon ka na sa bahay.

## Ehersisyo - gumawa ng recipe generator

Ngayon na naipakita na natin ang isang scenario, isulat natin ang code para gumawa ng parehong scenario. Para dito, gawin ang mga sumusunod:

1. Gamitin ang kasalukuyang _app.py_ file bilang panimulang punto
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

   > TANDAAN, ang iyong LLM ay hindi deterministic, kaya maaring mag-iba ang mga resulta sa bawat pagpapatakbo ng programa.

   Maganda, tingnan natin kung paano ito mapapaganda pa. Para sa pagpapabuti, gusto nating maging flexible ang code, kaya maari nating baguhin ang mga ingredients at bilang ng mga recipe.

1. Baguhin natin ang code sa ganitong paraan:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # ipasok ang bilang ng mga resipe sa prompt ng mga sangkap
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Ang pagsubok ng code ay maaaring ganito:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Pahusayin sa pagdagdag ng filter at shopping list

Ngayon ay mayroon tayong gumaganang app na kayang gumawa ng mga recipe at flexible ito dahil umaasa sa input ng user, sa bilang ng mga recipe at pati na rin sa mga sangkap.

Para higit pang mapabuti ito, nais nating idagdag ang mga sumusunod:

- **Salain ang mga sangkap**. Gusto nating makapag-filter ng mga sangkap na ayaw natin o may allergy tayo. Para gawin ito, maari nating baguhin ang ating prompt at magdagdag ng filter na kondisyon sa dulo nito tulad nito:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Sa itaas, idinadagdag natin ang `{filter}` sa dulo ng prompt at kinukuha rin ang value ng filter mula sa user.

  Halimbawa ng input sa pagpapatakbo ng programa ay maaaring ganito:

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

  Makikita mo, ang mga recipe na may gatas ay nasala na. Pero kung lactose intolerant ka, baka gusto mo ring salain ang mga recipe na may keso, kaya dapat maging malinaw.


- **Gumawa ng listahan ng pamimili**. Nais nating gumawa ng listahan ng pamimili, isinasaalang-alang ang mga mayroon na tayo sa bahay.

  Para sa functionality na ito, maaari nating subukang lutasin lahat sa isang prompt o hatiin ito sa dalawang prompt. Subukan natin ang huli. Dito, inirerekomenda nating magdagdag ng karagdagang prompt, ngunit para gumana ito, kailangan nating idagdag ang resulta ng unang prompt bilang konteksto sa pangalawang prompt.

  Hanapin ang bahagi sa code na nagpi-print ng resulta mula sa unang prompt at idagdag ang sumusunod na code sa ibaba:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # i-print ang tugon
  print("Shopping list:")
  print(response.output_text)
  ```

  Tandaan ang mga sumusunod:

  1. Gumagawa tayo ng bagong prompt sa pamamagitan ng pagdagdag ng resulta mula sa unang prompt sa bagong prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Gumagawa tayo ng bagong request, kasama na ang pagsasaalang-alang sa bilang ng tokens na hiniling natin sa unang prompt, kaya sa pagkakataong ito ay sinasabing `max_output_tokens` ay 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Kapag sinubukan ang code na ito, makukuha natin ang sumusunod na output:

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

Ang mayroon tayo sa ngayon ay code na gumagana, ngunit may mga ilang pag-aayos na dapat gawin upang mas mapabuti pa ito. Ilan sa mga dapat gawin ay:

- **Ihiwalay ang mga lihim mula sa code**, tulad ng API key. Hindi dapat kasama sa code ang mga lihim at dapat itong itago sa isang ligtas na lugar. Para ihiwalay ang lihim mula sa code, maaari tayong gumamit ng environment variables at mga libraries tulad ng `python-dotenv` upang i-load sila mula sa isang file. Ganito ang magiging hitsura nito sa code:

  1. Gumawa ng `.env` na file na may sumusunod na nilalaman:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Tandaan, para sa Azure OpenAI sa Microsoft Foundry, kailangan mong itakda ang mga sumusunod na environment variables:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Sa code, i-load mo ang environment variables ng ganito:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Isang salita tungkol sa haba ng token**. Dapat nating isaalang-alang kung gaano karaming tokens ang kailangan natin para mabuo ang tekstong gusto natin. May bayad ang tokens, kaya hangga't maaari, dapat tayong maging matipid sa bilang ng tokens na ginagamit. Halimbawa, maaari ba nating ipahayag ang prompt nang mas maikli upang magamit ang mas kaunting tokens?

  Para baguhin ang bilang ng tokens na ginagamit, maaari mong gamitin ang parameter na `max_output_tokens`. Halimbawa, kung gusto mong gumamit ng 100 tokens, gagawin mo ito ng:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Eksperimento sa temperature**. Ang temperature ay isang bagay na hindi pa natin nababanggit pero mahalaga sa konteksto ng pagganap ng ating programa. Kapag mas mataas ang halaga ng temperature, mas random ang magiging output. Sa kabilang banda, kapag mababa ang temperature, mas predictable ang output. Isipin mo kung gusto mo ng pagbabago-bago o hindi sa iyong output.

  Para baguhin ang temperature, maaari mong gamitin ang parameter na `temperature`. Halimbawa, kung gusto mong gamitin ang temperature na 0.5, gagawin mo ito ng:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Tandaan, kapag mas malapit sa 1.0, mas nag-iiba-iba ang output.

## Takdang-aralin

Para sa takdang-aralin, maaari kang pumili kung ano ang itatayo.

Narito ang ilang mga mungkahi:

- Baguhin pa ang recipe generator app upang mas mapabuti ito. Subukan ang iba't ibang halaga ng temperature, at ang mga prompt upang makita kung ano ang kaya mong malikha.
- Gumawa ng isang "study buddy". Ang app na ito ay dapat kayang sagutin ang mga tanong tungkol sa isang paksa, halimbawa Python. Maaari kang magkaroon ng mga prompt tulad ng "Ano ang isang partikular na paksa sa Python?", o kaya'y prompt na nagsasabi, ipakita sa akin ang code para sa isang partikular na paksa atbp.
- History bot, buhayin ang kasaysayan, utusan ang bot na gumanap bilang isang partikular na makasaysayang tauhan at tanungin ito tungkol sa kanyang buhay at panahon.

## Solusyon

### Study buddy

Nasa ibaba ang panimulang prompt, tingnan kung paano mo ito magagamit at mababago ayon sa gusto mo.

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
1. Kinokontrol nito kung gaano kalaki ang sagot.
1. Kinokontrol nito kung ilan ang tokens na ginagamit.

## 🚀 Hamon

Kapag nagtatrabaho sa takdang-aralin, subukang baguhin ang temperature, subukang itakda ito sa 0, 0.5, at 1. Tandaan na ang 0 ang pinaka-kakaunti ang pagbabago at ang 1 ang pinaka-marami. Ano ang pinakamahusay na halaga para sa iyong app?

## Magaling na Trabaho! Ipagpatuloy ang Iyong Pag-aaral

Pagkatapos mong matapos ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pag-level up ng iyong kaalaman sa Generative AI!

Pumunta sa Aralin 7 kung saan titingnan natin kung paano [gumawa ng mga chat application](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->