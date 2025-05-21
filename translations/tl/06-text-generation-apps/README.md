<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-05-19T17:11:31+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "tl"
}
-->
# Pagbuo ng Mga Aplikasyon sa Pagbuo ng Teksto

> _(I-click ang imahe sa itaas para mapanood ang video ng araling ito)_

Sa ngayon, nakita mo na sa kurikulum na ito na may mga pangunahing konsepto tulad ng mga prompt at kahit isang buong disiplina na tinatawag na "prompt engineering". Maraming mga tool na maaari mong makasalamuha tulad ng ChatGPT, Office 365, Microsoft Power Platform at iba pa, na sumusuporta sa paggamit ng mga prompt upang makamit ang isang bagay.

Para maidagdag mo ang ganitong karanasan sa isang app, kailangan mong maunawaan ang mga konsepto tulad ng mga prompt, completions at pumili ng library na gagamitin. Iyan mismo ang matututuhan mo sa kabanatang ito.

## Panimula

Sa kabanatang ito, ikaw ay:

- Matututo tungkol sa openai library at mga pangunahing konsepto nito.
- Bubuo ng isang app sa pagbuo ng teksto gamit ang openai.
- Mauunawaan kung paano gamitin ang mga konsepto tulad ng prompt, temperature, at tokens para bumuo ng app sa pagbuo ng teksto.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- Ipaliwanag kung ano ang isang app sa pagbuo ng teksto.
- Bumuo ng app sa pagbuo ng teksto gamit ang openai.
- I-configure ang iyong app upang gumamit ng mas marami o mas kaunting mga token at baguhin din ang temperature, para sa iba't ibang output.

## Ano ang isang app sa pagbuo ng teksto?

Karaniwan kapag bumuo ka ng isang app ito ay may ilang uri ng interface tulad ng mga sumusunod:

- Batay sa command. Ang mga console app ay mga tipikal na app kung saan nagta-type ka ng command at ito ay nagsasagawa ng gawain. Halimbawa, ang `git` ay isang command-based app.
- User interface (UI). Ang ilang mga app ay may mga graphical user interface (GUIs) kung saan nagki-click ka ng mga button, naglalagay ng teksto, pumipili ng mga opsyon at iba pa.

### Limitado ang mga Console at UI app

Ihambing ito sa isang command-based app kung saan nagta-type ka ng command:

- **Ito ay limitado**. Hindi ka basta-basta makakapag-type ng anumang command, tanging ang mga sinusuportahan ng app lamang.
- **Tiyak sa wika**. Ang ilang mga app ay sumusuporta sa maraming wika, ngunit sa pamamagitan ng default ang app ay binuo para sa isang tiyak na wika, kahit na maaari kang magdagdag ng higit pang suporta sa wika.

### Mga Benepisyo ng mga app sa pagbuo ng teksto

Kaya paano naiiba ang isang app sa pagbuo ng teksto?

Sa isang app sa pagbuo ng teksto, mayroon kang higit na kakayahang umangkop, hindi ka limitado sa isang set ng mga command o isang tiyak na input na wika. Sa halip, maaari mong gamitin ang natural na wika upang makipag-ugnayan sa app. Ang isa pang benepisyo ay dahil nakikipag-ugnayan ka na sa isang mapagkukunan ng data na sinanay sa isang malawak na korpus ng impormasyon, samantalang ang isang tradisyonal na app ay maaaring limitado sa kung ano ang nasa database.

### Ano ang maaari kong itayo gamit ang isang app sa pagbuo ng teksto?

Maraming bagay ang maaari mong itayo. Halimbawa:

- **Isang chatbot**. Ang isang chatbot na sumasagot sa mga tanong tungkol sa mga paksa, tulad ng iyong kumpanya at mga produkto nito ay maaaring isang magandang tugma.
- **Helper**. Mahusay ang mga LLM sa mga bagay tulad ng pagbubuod ng teksto, pagkuha ng mga insight mula sa teksto, paggawa ng teksto tulad ng mga resume at higit pa.
- **Code assistant**. Depende sa modelong pangwika na ginagamit mo, maaari kang bumuo ng isang code assistant na tumutulong sa iyo na magsulat ng code. Halimbawa, maaari mong gamitin ang isang produkto tulad ng GitHub Copilot pati na rin ang ChatGPT upang matulungan kang magsulat ng code.

## Paano ako makakapagsimula?

Kailangan mong makahanap ng paraan upang mag-integrate sa isang LLM na karaniwang nangangailangan ng sumusunod na dalawang diskarte:

- Gumamit ng API. Dito ka bumubuo ng mga web request gamit ang iyong prompt at bumabalik ang nabuo na teksto.
- Gumamit ng library. Ang mga library ay tumutulong sa pag-encapsulate ng mga tawag sa API at gawing mas madali ang mga ito.

## Mga Library/SDKs

Mayroong ilang kilalang mga library para sa pagtatrabaho sa mga LLM tulad ng:

- **openai**, ginagawang madali ng library na ito na kumonekta sa iyong modelo at magpadala ng mga prompt.

Pagkatapos ay may mga library na gumagana sa mas mataas na antas tulad ng:

- **Langchain**. Kilala ang Langchain at sumusuporta sa Python.
- **Semantic Kernel**. Ang Semantic Kernel ay isang library ng Microsoft na sumusuporta sa mga wika tulad ng C#, Python, at Java.

## Unang app gamit ang openai

Tingnan natin kung paano natin mabubuo ang ating unang app, kung anong mga library ang kailangan natin, kung gaano karami ang kailangan at iba pa.

### I-install ang openai

Maraming mga library diyan para makipag-ugnayan sa OpenAI o Azure OpenAI. Posible ring gumamit ng maraming programming languages tulad ng C#, Python, JavaScript, Java at iba pa. Pinili naming gamitin ang `openai` Python library, kaya gagamitin namin ang `pip` para i-install ito.

```bash
pip install openai
```

### Lumikha ng isang resource

Kailangan mong isagawa ang mga sumusunod na hakbang:

- Gumawa ng account sa Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Kumuha ng access sa Azure OpenAI. Pumunta sa [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) at humiling ng access.

  > [!NOTE]
  > Sa oras ng pagsulat, kailangan mong mag-apply para sa access sa Azure OpenAI.

- I-install ang Python <https://www.python.org/>
- Lumikha ng Azure OpenAI Service resource. Tingnan ang gabay na ito para sa kung paano [lumikha ng isang resource](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Hanapin ang API key at endpoint

Sa puntong ito, kailangan mong sabihin sa iyong `openai` library kung anong API key ang gagamitin. Para hanapin ang iyong API key, pumunta sa seksyong "Keys and Endpoint" ng iyong Azure OpenAI resource at kopyahin ang "Key 1" na halaga.

Ngayon na nakopya mo na ang impormasyong ito, sabihin natin sa mga library na gamitin ito.

> [!NOTE]
> Mahalaga ang paghiwalayin ang iyong API key mula sa iyong code. Maaari mo itong gawin sa pamamagitan ng paggamit ng mga environment variable.
>
> - Itakda ang environment variable `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### Setup configuration Azure

Kung gumagamit ka ng Azure OpenAI, narito kung paano mo ise-setup ang configuration:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Sa itaas, isinusulat natin ang mga sumusunod:

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion` class. Narito ang isang halimbawa:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

Sa code sa itaas, gumagawa tayo ng completion object at ipinapasa ang modelong nais nating gamitin at ang prompt. Pagkatapos ay ipinapakita natin ang nabuo na teksto.

### Mga Chat completions

Sa ngayon, nakita mo kung paano natin ginagamit ang `Completion` to generate text. But there's another class called `ChatCompletion` na mas angkop para sa mga chatbot. Narito ang isang halimbawa ng paggamit nito:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Higit pa sa functionality na ito sa isang paparating na kabanata.

## Ehersisyo - ang iyong unang app sa pagbuo ng teksto

Ngayon na natutunan natin kung paano i-set up at i-configure ang openai, oras na para bumuo ng iyong unang app sa pagbuo ng teksto. Upang bumuo ng iyong app, sundin ang mga hakbang na ito:

1. Gumawa ng virtual environment at i-install ang openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Kung gumagamit ka ng Windows, i-type ang `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` value.

1. Gumawa ng _app.py_ file at ilagay ang sumusunod na code:

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
   > Kung gumagamit ka ng Azure OpenAI, kailangan mong itakda ang `api_type` to `azure` and set the `api_key` sa iyong Azure OpenAI key.

   Makikita mo ang isang output na katulad ng sumusunod:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Iba't ibang uri ng mga prompt, para sa iba't ibang bagay

Ngayon nakita mo na kung paano bumuo ng teksto gamit ang isang prompt. Mayroon ka pang program na gumagana na maaari mong baguhin at palitan upang makabuo ng iba't ibang uri ng teksto.

Ang mga prompt ay maaaring gamitin para sa iba't ibang gawain. Halimbawa:

- **Bumuo ng uri ng teksto**. Halimbawa, maaari kang bumuo ng isang tula, mga tanong para sa isang pagsusulit at iba pa.
- **Maghanap ng impormasyon**. Maaari mong gamitin ang mga prompt upang maghanap ng impormasyon tulad ng sumusunod na halimbawa 'Ano ang ibig sabihin ng CORS sa web development?'.
- **Bumuo ng code**. Maaari mong gamitin ang mga prompt upang bumuo ng code, halimbawa pagbuo ng isang regular na expression na ginagamit upang i-validate ang mga email o bakit hindi bumuo ng isang buong programa, tulad ng isang web app?

## Isang mas praktikal na kaso ng paggamit: isang recipe generator

Isipin mo na mayroon kang mga sangkap sa bahay at gusto mong magluto ng isang bagay. Para diyan, kailangan mo ng recipe. Isang paraan para makahanap ng mga recipe ay ang paggamit ng search engine o maaari mong gamitin ang isang LLM upang gawin ito.

Maaari kang magsulat ng isang prompt tulad nito:

> "Ipakita sa akin ang 5 recipe para sa isang ulam na may mga sumusunod na sangkap: manok, patatas, at karot. Sa bawat recipe, ilista ang lahat ng mga sangkap na ginamit"

Dahil sa itaas na prompt, maaari kang makakuha ng tugon na katulad ng:

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

Mahusay ang resulta na ito, alam ko na kung ano ang lulutuin. Sa puntong ito, ang mga maaaring maging kapaki-pakinabang na pagpapabuti ay:

- Pagtatanggal ng mga sangkap na hindi ko gusto o allergic ako.
- Gumawa ng listahan ng pamimili, kung sakaling wala ako lahat ng mga sangkap sa bahay.

Para sa mga nabanggit na kaso, magdagdag tayo ng karagdagang prompt:

> "Mangyaring alisin ang mga recipe na may bawang dahil ako ay allergic at palitan ito ng iba. Gayundin, mangyaring gumawa ng listahan ng pamimili para sa mga recipe, isinasaalang-alang na mayroon na akong manok, patatas at karot sa bahay."

Ngayon mayroon kang bagong resulta, na:

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

Iyan ang iyong limang recipe, na walang bawang na binanggit at mayroon ka ring listahan ng pamimili na isinasaalang-alang kung ano ang mayroon ka na sa bahay.

## Ehersisyo - bumuo ng isang recipe generator

Ngayon na naglaro tayo ng isang senaryo, isulat natin ang code upang tumugma sa ipinakitang senaryo. Upang gawin ito, sundin ang mga hakbang na ito:

1. Gamitin ang umiiral na _app.py_ file bilang panimulang punto
1. Hanapin ang `prompt` variable at baguhin ang code nito sa sumusunod:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Kung patakbuhin mo na ngayon ang code, makikita mo ang isang output na katulad ng:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, ang iyong LLM ay hindi tiyak, kaya maaari kang makakuha ng iba't ibang resulta sa tuwing tatakbo ang programa.

   Mahusay, tingnan natin kung paano natin mapapabuti ang mga bagay. Upang mapabuti ang mga bagay, gusto nating tiyakin na ang code ay flexible, kaya ang mga sangkap at bilang ng mga recipe ay maaaring mapabuti at mabago.

1. Baguhin natin ang code sa sumusunod na paraan:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Ang pagkuha ng code para sa isang pagsubok na pagtakbo, ay maaaring magmukhang ganito:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Pagbutihin sa pamamagitan ng pagdaragdag ng filter at listahan ng pamimili

Ngayon ay mayroon na tayong gumaganang app na may kakayahang gumawa ng mga recipe at ito ay flexible dahil umaasa ito sa mga input mula sa user, kapwa sa bilang ng mga recipe ngunit pati na rin sa mga sangkap na ginamit.

Upang higit pang mapabuti ito, nais naming idagdag ang mga sumusunod:

- **Tanggalin ang mga sangkap**. Gusto naming magawang tanggalin ang mga sangkap na hindi namin gusto o allergic kami. Upang maisakatuparan ang pagbabagong ito, maaari naming i-edit ang aming umiiral na prompt at magdagdag ng kondisyon ng filter sa dulo nito tulad nito:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Sa itaas, nagdagdag kami ng `{filter}` sa dulo ng prompt at kinukuha rin namin ang halaga ng filter mula sa user.

  Ang isang halimbawa ng input ng pagpapatakbo ng programa ay maaari na ngayong magmukhang ganito:

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

  Tulad ng nakikita mo, anumang mga recipe na may gatas sa kanila ay na-filter out. Ngunit, kung ikaw ay lactose intolerant, maaaring gusto mong alisin ang mga recipe na may keso din sa kanila, kaya may pangangailangan na maging malinaw.

- **Gumawa ng listahan ng pamimili**. Gusto naming gumawa ng listahan ng pamimili, isinasaalang-alang kung ano ang mayroon na kami sa bahay.

  Para sa functionality na ito, maaari naming subukang lutasin ang lahat sa isang prompt o maaari naming hatiin ito sa dalawang prompt. Subukan natin ang huling diskarte. Dito ay nagmumungkahi kaming magdagdag ng karagdagang prompt, ngunit para gumana iyon, kailangan nating idagdag ang resulta ng dating prompt bilang konteksto sa huli.

  Hanapin ang bahagi sa code na nagpi-print ng resulta mula sa unang prompt at idagdag ang sumusunod na code sa ibaba:

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

  Pansinin ang mga sumusunod:

  1. Gumagawa kami ng bagong prompt sa pamamagitan ng pagdaragdag ng resulta mula sa unang prompt sa bagong prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Gumagawa kami ng bagong request, ngunit isinasaalang-alang din ang bilang ng mga token na hiniling namin sa unang prompt, kaya sa pagkakataong ito sinasabi namin na `max_tokens` ay 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     Ang pagkuha ng code na ito para sa isang pagtakbo, ngayon ay umaabot kami sa sumusunod na output:

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

Ang mayroon tayo sa ngayon ay code na gumagana, ngunit may ilang mga pag-tweak na dapat nating gawin upang higit pang mapabuti ang mga bagay. Ang ilang mga bagay na dapat nating gawin ay:

- **Paghiwalayin ang mga lihim mula sa code**, tulad ng API key. Ang mga lihim ay hindi nabibilang sa code at dapat itago sa isang ligtas na lokasyon. Upang paghiwalayin ang mga lihim mula sa code, maaari nating gamitin ang mga environment variable at mga library tulad ng `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` file na may sumusunod na nilalaman:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Tandaan, para sa Azure, kailangan mong itakda ang mga sumusunod na environment variable:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     Sa code, iloload mo ang mga environment variable tulad nito:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Isang salita sa haba ng token**. Dapat nating isaalang-alang kung gaano karaming mga token ang kailangan natin upang makabuo ng teksto na gusto natin. Ang mga token ay nagkakahalaga ng pera, kaya kung saan maaari, dapat tayong magsikap na maging matipid sa bilang ng mga token na ginagamit natin. Halimbawa, maaari ba nating ipahayag ang prompt upang makagamit tayo ng mas kaunting mga token?

  Upang baguhin ang mga token na ginamit, maaari mong gamitin ang `max_tokens` parameter. Halimbawa, kung gusto mong gumamit ng 100 token, gagawin mo:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Pag-eksperimento sa temperature**. Ang temperature ay isang bagay na hindi pa natin nabanggit sa ngayon ngunit isang mahalagang konteksto para sa kung paano gumaganap ang ating programa. Ang mas mataas na halaga ng temperature ay mas random ang output. Sa kabaligtaran, mas mababa ang halaga ng temperature ay mas predictable ang output. Isaalang-alang kung gusto mo ng pagkakaiba-iba sa iyong output o hindi.

  Upang

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman pinagsisikapan namin ang pagiging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatumpak. Ang orihinal na dokumento sa kanyang katutubong wika ay dapat ituring na mapagkakatiwalaang pinagmulan. Para sa kritikal na impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Kami ay hindi mananagot para sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.