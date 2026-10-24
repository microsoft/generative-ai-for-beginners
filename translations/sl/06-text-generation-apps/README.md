# Izdelava aplikacij za generiranje besedil

[![Izdelava aplikacij za generiranje besedil](../../../translated_images/sl/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Kliknite zgornjo sliko za ogled videa te lekcije)_

Do zdaj ste v tem učnem načrtu videli, da obstajajo osnovni koncepti, kot so pozivi (prompti) in celo cela disciplina, imenovana "prompt engineering" (inženiring pozivov). Mnogi pripomočki, s katerimi lahko komunicirate, kot so ChatGPT, Office 365, Microsoft Power Platform in drugi, vas podpirajo pri uporabi pozivov za dosego nečesa.

Da bi takšno izkušnjo dodali aplikaciji, morate razumeti koncepte, kot so pozivi, zaključki in izbrati knjižnico za delo z njimi. Točno to se boste naučili v tem poglavju.

## Uvod

V tem poglavju boste:

- Spoznali knjižnico openai in njene osnovne koncepte.
- Izdelali aplikacijo za generiranje besedil z uporabo openai.
- Razumeli, kako uporabljati koncepte, kot so poziv, temperatura in žetoni, za izdelavo aplikacije za generiranje besedil.

## Cilji učenja

Na koncu te lekcije boste znali:

- Razložiti, kaj je aplikacija za generiranje besedil.
- Izdelati aplikacijo za generiranje besedil z uporabo openai.
- Konfigurirati svojo aplikacijo tako, da bo uporabila več ali manj žetonov in tudi spremenila temperaturo za raznoliko izhodno besedilo.

## Kaj je aplikacija za generiranje besedil?

Običajno, ko izdelujete aplikacijo, vsebuje nekakšen vmesnik, kot je naslednji:

- Na ukazni ravni. Konzolne aplikacije so tipične aplikacije, kjer vnesete ukaz in aplikacija opravi nalogo. Na primer, `git` je aplikacija na ukazni ravni.
- Uporabniški vmesnik (UI). Nekatere aplikacije imajo grafične uporabniške vmesnike (GUI), kjer klikate gumbe, vnašate besedilo, izbirate možnosti in drugo.

### Konzolne in UI aplikacije so omejene

Primerjajte to z aplikacijo na ukazni ravni, kjer vnesete ukaz:

- **So omejene**. Ne morete vnesti kar kateregakoli ukaza, mogoče so le tisti, ki jih aplikacija podpira.
- **Specifične za jezik**. Nekatere aplikacije podpirajo mnogo jezikov, a privzeto je aplikacija izdelana za določen jezik, četudi lahko dodate več jezikovne podpore.

### Prednosti aplikacij za generiranje besedil

Kako se torej aplikacija za generiranje besedil razlikuje?

V aplikaciji za generiranje besedil imate več prožnosti, niste omejeni na nabor ukazov ali specifičen vhodni jezik. Namesto tega lahko uporabljate naravni jezik za interakcijo z aplikacijo. Druga prednost je, da že komunicirate z virom podatkov, ki je bil usposobljen na obsežnem korpusu informacij, medtem ko je tradicionalna aplikacija lahko omejena na podatke v bazi.

### Kaj lahko ustvarim z aplikacijo za generiranje besedil?

Lahko ustvarite veliko stvari. Na primer:

- **Klepetalni robot (chatbot)**. Klepetalni robot, ki odgovarja na vprašanja o temah, kot so vaše podjetje in njegovi izdelki, bi bil dobra izbira.
- **Pomočnik**. LLM-ji so odlični pri nalogah, kot so povzemanje besedil, pridobivanje vpogledov iz besedil, ustvarjanje besedil, kot so življenjepisi in še več.
- **Asistent za kodo**. Glede na jezikovni model, ki ga uporabljate, lahko ustvarite asistenta za kodo, ki vam pomaga pisati kodo. Na primer, lahko uporabite izdelek, kot je GitHub Copilot, pa tudi ChatGPT za pomoč pri pisanju kode.

## Kako začeti?

Potrebno je najti način za integracijo z LLM, kar običajno vključuje naslednja dva pristopa:

- Uporaba API-ja. Tukaj sestavljate spletne zahteve s svojim pozivom in prejmete nazaj generirano besedilo.
- Uporaba knjižnice. Knjižnice pomagajo enkapsulirati klice API-ja in jih narediti lažje za uporabo.

## Knjižnice/SDK-ji

Obstajajo nekatere dobro znane knjižnice za delo z LLM-ji, kot so:

- **openai**, ta knjižnica olajša povezavo z vašim modelom in pošiljanje pozivov.

Nato so tu knjižnice, ki delujejo na višji ravni, kot so:

- **Langchain**. Langchain je dobro poznan in podpira Python.
- **Semantic Kernel**. Semantic Kernel je Microsoftova knjižnica, ki podpira jezike C#, Python in Java.

## Prva aplikacija z uporabo openai

Poglejmo, kako lahko ustvarimo prvo aplikacijo, katere knjižnice potrebujemo, koliko je potrebno in tako naprej.

### Namestitev openai

Obstaja veliko knjižnic za interakcijo z OpenAI ali Azure OpenAI. Možno je tudi uporabljati različne programske jezike, kot so C#, Python, JavaScript, Java in drugi. Izbrali smo knjižnico `openai` za Python, zato bomo uporabili `pip` za namestitev.

```bash
pip install openai
```

### Ustvarjanje vira

Izvedite naslednje korake:

- Ustvarite račun na Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Pridobite dostop do Azure OpenAI. Obiščite [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) in zaprosite za dostop.

  > [!NOTE]
  > Ob času pisanja morate zaprositi za dostop do Azure OpenAI.

- Namestite Python <https://www.python.org/>
- Ustvarili ste vir storitve Azure OpenAI. Oglejte si ta vodnik o tem, kako [ustvariti vir](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Poiščite ključ API in končno točko

V tem trenutku morate svoji knjižnici `openai` povedati, kateri ključ API naj uporablja. Da najdete svoj ključ API, pojdite v razdelek "Ključi in končne točke" vašega vira Azure OpenAI in kopirajte vrednost "Ključ 1".

![Razdelek Ključi in končne točke v Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Zdaj, ko imate te podatke kopirane, navodimo knjižnice, naj jih uporabijo.

> [!NOTE]
> Priporočljivo je, da ločite svoj ključ API od svoje kode. To lahko naredite z uporabo okolijskih spremenljivk.
>
> - Nastavite okoljsko spremenljivko `OPENAI_API_KEY` na vaš ključ API.
>   `export OPENAI_API_KEY='sk-...'`

### Nastavitev konfiguracije za Azure

Če uporabljate Azure OpenAI (sedaj del Microsoft Foundry), tukaj je, kako nastavite konfiguracijo. Uporabljamo standardnega odjemalca `OpenAI`, ki kaže na Azure OpenAI končno točko `/openai/v1/`, ki deluje z Responses API in ne potrebuje `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Zgoraj nastavljamo naslednje:

- `api_key`, to je vaš ključ API, najden v Azure Portalu ali portalu Microsoft Foundry.
- `base_url`, to je vaš končni naslov vira Foundry z dodanim `/openai/v1/`. Stabilna končna točka v1 deluje tako za OpenAI kot Azure OpenAI brez upravljanja `api_version`.

> [!NOTE] > `os.environ` bere okoljske spremenljivke. Uporabite ga lahko za branje okoljskih spremenljivk, kot so `AZURE_OPENAI_API_KEY` in `AZURE_OPENAI_ENDPOINT`. Nastavite te okoljske spremenljivke v terminalu ali z uporabo knjižnice, kot je `dotenv`.

## Generiranje besedila

Način za generiranje besedila je uporaba Responses API prek metode `responses.create`. Tukaj je primer:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

V zgornji kodi ustvarimo odgovor in podamo model, ki ga želimo uporabiti, in poziv. Nato natisnemo generirano besedilo preko `response.output_text`.

### Večkrožni pogovori

Responses API je primeren tako za generiranje besedila z enim krogom kot tudi za večkrožne klepetalne robote - podate seznam sporočil v `input` za izgradnjo pogovora:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Več o tej funkcionalnosti v prihodnjem poglavju.

## Vaja - vaša prva aplikacija za generiranje besedil

Zdaj, ko smo se naučili nastaviti in konfigurirati openai, je čas, da izdelate svojo prvo aplikacijo za generiranje besedil. Za izdelavo aplikacije sledite tem korakom:

1. Ustvarite virtualno okolje in namestite openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Če uporabljate Windows, vpišite `venv\Scripts\activate` namesto `source venv/bin/activate`.

   > [!NOTE]
   > Ključ vašega Azure OpenAI poiščite tako, da obiščete [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), iščete `Open AI`, izberete `Open AI resource` in nato izberete `Keys and Endpoint` ter kopirate vrednost `Key 1`.

1. Ustvarite datoteko _app.py_ in ji priskrbite naslednjo kodo:

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
   > Če uporabljate navadni OpenAI (ne Azure), uporabite `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (brez `base_url`) in posredujte ime modela, kot je `gpt-5-mini` namesto imena namestitve.

   Morali bi videti nekaj takega:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Različne vrste pozivov za različne stvari

Zdaj ste videli, kako generirati besedilo z uporabo poziva. Imate tudi program, ki ga lahko zaženete in spremenite za generiranje različnih vrst besedil.

Pozivi se lahko uporabljajo za različne naloge. Na primer:

- **Generiranje vrste besedila**. Na primer, lahko ustvarite pesem, vprašanja za kviz itd.
- **Iskanje informacij**. Pozivov lahko uporabite za iskanje informacij, kot je v naslednjem primeru 'Kaj pomeni CORS v spletnem razvoju?'.
- **Generiranje kode**. Pozivov lahko uporabite za generiranje kode, na primer za razvoj regularnih izrazov za preverjanje elektronskih naslovov ali zakaj ne ustvariti celoten program, kot je spletna aplikacija?

## Bolj praktičen primer: generator receptov

Predstavljajte si, da imate doma sestavine in želite nekaj skuhati. Za to potrebujete recept. Način za iskanje receptov je lahko uporaba iskalnika ali pa uporaba LLM-ja.

Lahko napišete poziv, kot je ta:

> "Pokaži mi 5 receptov za jed s sledečimi sestavinami: piščanec, krompir in korenje. Za vsak recept naštej vse uporabljene sestavine"

Glede na zgornji poziv lahko dobite odgovor, podoben naslednjemu:

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

Ta rezultat je super, vem, kaj skuhati. V tem trenutku bi bile uporabne izboljšave:

- Odstranitev sestavin, ki mi niso všeč ali sem nanje alergičen.
- Priprava nakupovalnega seznama, če doma nimam vseh sestavin.

Za zgornje primere dodajmo še en poziv:

> "Prosim, odstrani recepte z česnom, saj sem nanj alergičen, in jih nadomesti z nečim drugim. Prav tako prosim pripravi nakupovalni seznam za recepte, glede na to, da imam že doma piščanca, krompir in korenje."

Zdaj imate nov rezultat, in sicer:

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

To je vaših pet receptov, brez omembe česna, ter imate tudi nakupovalni seznam glede na to, kaj že imate doma.

## Vaja - izdelajte generator receptov

Zdaj, ko smo predstavili scenarij, napišimo kodo, ki ustreza prikazanemu scenariju. Sledite naslednjim korakom:

1. Uporabite obstoječo datoteko _app.py_ kot izhodišče
1. Poiščite spremenljivko `prompt` in spremenite njeno kodo na naslednjo:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Če zdaj zaženete kodo, bi morali videti nekaj podobnega:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > OPOZORILO, vaša LLM ni determinističen, zato boste morda vsakič, ko zaženete program, dobili drugačne rezultate.

   Super, poglejmo, kako lahko stvari izboljšamo. Za izboljšave želimo, da je koda prožna, tako da je mogoče izboljšati in spremeniti sestavine ter število receptov.

1. Spremenimo kodo na naslednji način:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Testni zagon kode bi lahko izgledal takole:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Izboljšajte z dodajanjem filtra in nakupovalnega seznama

Zdaj imamo delujočo aplikacijo, ki zna ustvarjati recepte in je prožna, saj se zanaša na uporabniške vnose, tako glede števila receptov kot uporabljenih sestavin.

Za nadaljnje izboljšave želimo dodati naslednje:

- **Filtriranje sestavin**. Želimo lahko odstraniti sestavine, ki jih ne maramo ali smo nanje alergični. Za to spremembo lahko uredimo obstoječi poziv in na njegov konec dodamo pogoj filtra, kot sledi:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Zgoraj dodajamo `{filter}` na konec poziva in zajemamo vrednost filtra od uporabnika.

  Primer vnosa za zagon programa lahko zdaj izgleda takole:

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

  Kot vidite, so bili recepti z mlekom filtrirani. Če pa imate laktozno intoleranco, boste morda želeli filtrirati tudi recepte s sirom, zato je pomembno biti jasen.

- **Izdelava nakupovalnega seznama**. Želimo ustvariti nakupovalni seznam, glede na to, kaj že imamo doma.

  Za to funkcionalnost lahko poskusimo vse rešiti v enem pozivu ali pa jo razdelimo na dva poziva. Poskusimo slednji pristop. Tukaj predlagamo dodati dodaten poziv, za kar je potrebno dodati rezultat prvega poziva kot kontekst drugemu pozivu.

  Poiščite v kodi del, ki izpiše rezultat prvega poziva, in pod njim dodajte naslednjo kodo:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Upoštevajte naslednje:

  1. Sestavljamo nov poziv tako, da k novemu pozivu dodamo rezultat prvega poziva:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Naredimo novo zahtevo, pri čemer upoštevamo tudi število žetonov, ki smo jih zahtevali v prvem pozivu, tako da tokrat nastavimo `max_output_tokens` na 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Z zagonom te kode zdaj dobimo naslednji izhod:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Izboljšajte svojo nastavitev

Kar imamo do zdaj, je koda, ki deluje, vendar bi morali narediti nekaj prilagoditev, da stvari še izboljšamo. Nekaj stvari, ki jih moramo storiti, so:

- **Ločite skrivnosti od kode**, kot je API ključ. Skrivnosti ne spadajo v kodo in jih je treba hraniti na varnem mestu. Za ločevanje skrivnosti od kode lahko uporabimo okoljske spremenljivke in knjižnice, kot je `python-dotenv`, da jih naložimo iz datoteke. Tako bi to izgledalo v kodi:

  1. Ustvarite datoteko `.env` z naslednjo vsebino:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Opomba, za Azure OpenAI v Microsoft Foundry morate namesto tega nastaviti naslednje okoljske spremenljivke:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     V kodi bi okoljske spremenljivke naložili tako:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Beseda o dolžini tokenov**. Treba je premisliti, koliko tokenov potrebujemo za generiranje želenega besedila. Tokeni stanejo denar, zato se moramo, kjer je mogoče, potruditi biti varčni s številom uporabljenih tokenov. Na primer, ali lahko oblikujemo poziv tako, da uporabimo manj tokenov?

  Za spremembo uporabljenih tokenov lahko uporabite parameter `max_output_tokens`. Na primer, če želite uporabiti 100 tokenov, naredite tako:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Eksperimentiranje s temperaturo**. Temperatura je nekaj, o čemer do sedaj nismo govorili, a je pomemben kontekst za delovanje našega programa. Višja vrednost temperature pomeni bolj naključen izhod. Nižja vrednost temperature pomeni bolj predvidljiv izhod. Premislite, ali želite variacije v svojem izhodu ali ne.

  Za spreminjanje temperature lahko uporabite parameter `temperature`. Na primer, če želite uporabiti temperaturo 0,5, naredite tako:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Opomba, bližje kot je vrednost 1, bolj raznolik je izhod.

- **Modeli za sklepanje ne uporabljajo `temperature`**. To je pomembna sprememba za leto 2026. Trenutni, neodpravljeni modeli na Microsoft Foundry so **modeli za sklepanje** (družina GPT-5, o-serija) - in **ne podpirajo `temperature` ali `top_p`** (niti `max_tokens`; uporabite `max_output_tokens`). Če pošljete `temperature` v `gpt-5-mini`, boste dobili napako "parameter ni podprt". Torej, da preizkusite zgornji primer temperature, uporabite model, ki še podpira kontrolnike za vzorčenje - na primer odprti model **Llama**, kot je `Llama-3.3-70B-Instruct` iz [Microsoft Foundry modelskega kataloga](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), poklican prek vmesnika Foundry Models / Azure AI Inference (na enak način kot vzorci `githubmodels-*`). Za modele za sklepanje, kot je GPT-5, pa upravljate izhod drugače:
  - **Inženiring pozivov** - jasna navodila, primeri in strukturiran izhod (oglejte si lekcijo [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) opravljajo delo, ki ga je prej opravljalo nastavljanje vzorčenja.
  - **Nadzor sklepanja** - parametri, kot so prizadevanje za sklepanje/večvrednostnost uravnotežijo globino sklepanja z zakasnitvijo in stroški.

  Na kratko: `temperature`/`top_p` sta še vedno veljavna pri mnogih modelih (Llama, Mistral, Phi in družina GPT-4.x - čeprav GPT-4.x izginja), vendar je smer razvoja inženiring pozivov + nadzor sklepanja pri modelih za sklepanje, kot je GPT-5.

## Domača naloga

Za to domačo nalogo lahko izberete, kaj boste naredili.

Tukaj je nekaj predlogov:

- Izboljšajte aplikacijo generatorja receptov. Poigrajte se z vrednostmi temperature in pozivi, da vidite, kaj lahko ustvarite.
- Ustvarite "študijskega prijatelja". Ta aplikacija mora znati odgovarjati na vprašanja o določeni temi, na primer Python, lahko imate pozive kot "Kaj je določena tema v Pythonu?" ali poziv, ki zahteva prikaz kode za določeno temo itd.
- Bot za zgodovino, naredite, da zgodovina oživi, ukažite botu, naj igra določeno zgodovinsko osebnost in mu postavljajte vprašanja o njegovem življenju in času.

## Rešitev

### Študijski prijatelj

Spodaj je začetni poziv, poglejte, kako ga lahko uporabite in prilagodite po svoji želji.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot za zgodovino

Tukaj je nekaj pozivov, ki jih lahko uporabljate:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Preverjanje znanja

Kaj počne koncept temperature?

1. Nadzoruje, kako naključen je izhod.
1. Nadzoruje, kako dolg je odgovor.
1. Nadzoruje, koliko tokenov se uporabi.

## 🚀 Izziv

Med delom na domači nalogi poskusite spreminjati temperaturo, jo poskusite nastaviti na 0, 0,5 in 1. Zapomnite si, da je 0 najmanj raznoliko, 1 pa najbolj raznoliko. Katera vrednost najbolje deluje za vašo aplikacijo?

## Odlično delo! Nadaljujte z učenjem

Po končani tej lekciji si oglejte našo [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da še naprej nadgrajujete svoje znanje o generativni umetni inteligenci!

Pojdite na lekcijo 7, kjer bomo pogledali, kako [izdelati klepetalne aplikacije](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->