# Gradnja aplikacij za generiranje besedil

[![Gradnja aplikacij za generiranje besedil](../../../translated_images/sl/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Kliknite na zgornjo sliko za ogled videa te lekcije)_

Do sedaj ste v tem učnem načrtu videli, da obstajajo osnovni koncepti, kot so pozivi (prompts) in celo cela disciplina, imenovana "inženiring pozivov". Mnogo orodij, s katerimi lahko komunicirate, kot so ChatGPT, Office 365, Microsoft Power Platform in drugo, vas podpira z uporabo pozivov za doseganje nečesa.

Da bi takšno izkušnjo dodali v aplikacijo, morate razumeti koncepte, kot so pozivi, dokončanja (completions) in izbrati knjižnico za delo. To boste pravzaprav izvedeli v tem poglavju.

## Uvod

V tem poglavju boste:

- Spoznali knjižnico openai in njene osnovne koncepte.
- Zgradili aplikacijo za generiranje besedil z uporabo openai.
- Razumeli, kako uporabiti koncepte, kot so poziv (prompt), temperatura in žetoni (tokens) za gradnjo aplikacije za generiranje besedil.

## Cilji učenja

Na koncu te lekcije boste znali:

- Razložiti, kaj je aplikacija za generiranje besedil.
- Zgraditi aplikacijo za generiranje besedil z uporabo openai.
- Konfigurirati svojo aplikacijo, da uporablja več ali manj žetonov in tudi spreminjati temperaturo za raznolik izhod.

## Kaj je aplikacija za generiranje besedil?

Običajno, ko zgradite aplikacijo, ima nekakšen vmesnik, kot je naslednji:

- Ukazna. Konzolne aplikacije so tipične aplikacije, kjer vnesete ukaz in opravi določeno nalogo. Na primer, `git` je ukazna aplikacija.
- Uporabniški vmesnik (UI). Nekatere aplikacije imajo grafične uporabniške vmesnike (GUI), kjer klikate gumbe, vnašate besedilo, izbirate možnosti in podobno.

### Konzolne in UI aplikacije so omejene

Primerjajte to z ukazno aplikacijo, kjer vnesete ukaz:

- **Je omejena**. Ne morete preprosto vnašati kateregakoli ukaza, samo tiste, ki jih aplikacija podpira.
- **Je jezikovno specifična**. Nekatere aplikacije podpirajo več jezikov, vendar je aplikacija po privzetku zgrajena za določen jezik, četudi lahko dodate podporo za več jezikov.

### Prednosti aplikacij za generiranje besedil

Kako je torej aplikacija za generiranje besedil drugačna?

V aplikaciji za generiranje besedil imate več prilagodljivosti, niste omejeni na niz ukazov ali določen vhodni jezik. Namesto tega lahko uporabite naravni jezik za interakcijo z aplikacijo. Druga prednost je, da že komunicirate z virom podatkov, ki je bil usposobljen na velikem korpusu informacij, medtem ko je lahko tradicionalna aplikacija omejena na to, kar je v podatkovni zbirki.

### Kaj lahko zgradim z aplikacijo za generiranje besedil?

Obstaja veliko stvari, ki jih lahko zgradite. Na primer:

- **Klepetalnik (chatbot)**. Klepetalnik, ki odgovarja na vprašanja o temah, kot so vaše podjetje in njegovi izdelki, bi bil dober primer.
- **Pomočnik**. LLM-ji so odlični pri stvareh, kot so povzema besedila, pridobivanje vpogledov iz besedila, ustvarjanje besedil, kot so življenjepisi in drugo.
- **Pomočnik za kodo**. Glede na jezikovni model, ki ga uporabljate, lahko zgradite pomočnika za kodo, ki vam pomaga pisati kodo. Na primer, lahko uporabite produkt, kot je GitHub Copilot, kot tudi ChatGPT za pomoč pri pisanju kode.

## Kako začeti?

Potrebno je najti način za integracijo z LLM, kar običajno vključuje naslednji dve poti:

- Uporaba API-ja. Tukaj sestavljate spletne zahteve s svojim pozivom in dobite nazaj generirano besedilo.
- Uporaba knjižnice. Knjižnice pomagajo zajeti klice API-ja in jih narediti lažje za uporabo.

## Knjižnice/SDK-ji

Obstaja nekaj dobro poznanih knjižnic za delo z LLM-ji, kot so:

- **openai**, ta knjižnica omogoča enostavno povezavo z vašim modelom in pošiljanje pozivov.

Obstajajo tudi knjižnice, ki delujejo na višji ravni, kot so:

- **Langchain**. Langchain je dobro poznan in podpira Python.
- **Semantic Kernel**. Semantic Kernel je knjižnica Microsofta, ki podpira jezike C#, Python in Java.

## Prva aplikacija z uporabo openai

Poglejmo, kako lahko zgradimo prvo aplikacijo, katere knjižnice potrebujemo, koliko je potrebnih in tako naprej.

### Namestitev openai

Obstaja veliko knjižnic za interakcijo z OpenAI ali Azure OpenAI. Možno je uporabljati tudi številne programske jezike, kot so C#, Python, JavaScript, Java in drugi. Izbrali smo uporabo Python knjižnice `openai`, zato bomo uporabili `pip` za namestitev.

```bash
pip install openai
```

### Ustvarite vir

Potrebno je opraviti naslednje korake:

- Ustvarite račun na Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Pridobite dostop do Azure OpenAI. Pojdite na [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) in zaprosite za dostop.

  > [!NOTE]
  > Ob času pisanja morate zaprositi za dostop do Azure OpenAI.

- Namestite Python <https://www.python.org/>
- Ustvarite Azure OpenAI Service vir. Oglejte si ta vodič o [kako ustvariti vir](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Poiščite API ključ in končno točko

Zdaj morate knjižnici `openai` povedati, kateri API ključ naj uporablja. Za iskanje vašega API ključa pojdite v razdelek "Keys and Endpoint" na viru Azure OpenAI in kopirajte vrednost "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Ko imate te informacije kopirane, naj knjižnice začnejo te informacije uporabljati.

> [!NOTE]
> Priporočljivo je, da ločite svoj API ključ od svoje kode. To lahko naredite z uporabo okoljskih spremenljivk.
>
> - Nastavite okoljsko spremenljivko `OPENAI_API_KEY` na svoj API ključ.
>   `export OPENAI_API_KEY='sk-...'`

### Nastavitev konfiguracije Azure

Če uporabljate Azure OpenAI (zdaj del Microsoft Foundry), tako nastavite konfiguracijo. Uporabljamo standardni `OpenAI` klient usmerjen na Azure OpenAI `/openai/v1/` končno točko, ki deluje z Responses API in ne potrebuje `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Zgornje nastavitve določajo:

- `api_key`, to je vaš API ključ, najden v Azure portalu ali Microsoft Foundry portalu.
- `base_url`, to je vaša Foundry končna točka vira z dodanim `/openai/v1/`. Stabilna v1 končna točka deluje tako za OpenAI kot Azure OpenAI brez upravljanja `api_version`.

> [!NOTE] > `os.environ` bere okoljske spremenljivke. Lahko ga uporabite za branje okoljskih spremenljivk, kot so `AZURE_OPENAI_API_KEY` in `AZURE_OPENAI_ENDPOINT`. Te okoljske spremenljivke nastavite v terminalu ali z uporabo knjižnice, kot je `dotenv`.

## Generiranje besedila

Način generiranja besedila je uporaba Responses API preko metode `responses.create`. Tukaj je primer:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # to je ime vaše nameščene naprave modela
    input=prompt,
    store=False,
)
print(response.output_text)
```

V zgornji kodi ustvarimo odgovor in posredujemo model, ki ga želimo uporabiti, in poziv. Nato izpišemo generirano besedilo preko `response.output_text`.

### Večkratna pogajanja (multi-turn conversations)

Responses API je primeren tako za enokrožno generiranje kot za večkratne klepetalnike – podate seznam sporočil v `input`, da sestavite pogovor:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

Več o tej funkcionalnosti v prihajajočem poglavju.

## Vaja - vaša prva aplikacija za generiranje besedil

Zdaj, ko smo se naučili, kako nastaviti in konfigurirati openai, je čas, da zgradite svojo prvo aplikacijo za generiranje besedil. Za gradnjo aplikacije sledite naslednjim korakom:

1. Ustvarite virtualno okolje in namestite openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Če uporabljate Windows, vnesite `venv\Scripts\activate` namesto `source venv/bin/activate`.

   > [!NOTE]
   > Poiščite svoj Azure OpenAI ključ tako, da pojdite na [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) in poiščete `Open AI`, nato izberete `Open AI vir` ter izberete `Keys and Endpoint` in kopirate vrednost `Key 1`.

1. Ustvarite datoteko _app.py_ in ji dodajte naslednjo kodo:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # dodajte vašo kodo za dokončanje
   prompt = "Complete the following: Once upon a time there was a"

   # naredite zahtevo z uporabo Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # izpišite odgovor
   print(response.output_text)
   ```

   > [!NOTE]
   > Če uporabljate običajni OpenAI (ne Azure), uporabite `client = OpenAI(api_key="<zamenjajte to vrednost z vašim OpenAI ključem>")` (brez `base_url`) in posredujte ime modela, kot je `gpt-4o-mini`, namesto imena nameščene različice.

   Videti bi morali izpis, kot je naslednji:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Različne vrste pozivov za različne namene

Zdaj vidite, kako generirati besedilo s pozivom. Imate celo program, ki teče in ga lahko spreminjate ter prilagajate za ustvarjanje različnih vrst besedil.

Pozivi se lahko uporabijo za vse vrste opravil. Na primer:

- **Generiranje določene vrste besedila**. Na primer, lahko generirate pesem, vprašanja za kviz itd.
- **Iskanje informacij**. Z pozivi lahko iščete informacije, na primer: 'Kaj pomeni CORS v spletni razvoj?'
- **Generiranje kode**. Z pozivi lahko generirate kodo, na primer razvijete regularni izraz za preverjanje elektronskih naslovov ali celo generirate celoten program, na primer spletno aplikacijo.

## Bolj praktičen primer: generator receptov

Predstavljajte si, da imate doma sestavine in želite skuhati nekaj. Za to potrebujete recept. Recept poiščete lahko z iskalnikom ali pa uporabite LLM za to.

Lahko napišete poziv takole:

> "Pokaži mi 5 receptov za jed s sledečimi sestavinami: piščanec, krompir in korenje. Na recept navedite vse uporabljene sestavine."

Glede na zgornji poziv lahko dobite odgovor, podoben:

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

Ta rezultat je odličen, vem, kaj bom kuhal. V tem trenutku bi bile uporabne izboljšave:

- Filtrirati sestavine, ki mi niso všeč ali sem nanje alergičen.
- Izdelati nakupovalni seznam, če nimam vseh sestavin doma.

Za zgornje primere dodajmo dodatni poziv:

> "Prosim, odstrani recepte s česnom, ker sem na njega alergičen, in ga nadomesti z nečim drugim. Prav tako, prosim, izdela nakupovalni seznam za recepte, ob upoštevanju, da imam doma že piščanca, krompir in korenje."

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

To so vaši pet receptov, brez omenjenega česna, prav tako pa imate nakupovalni seznam glede na sestavine, ki jih že imate doma.

## Vaja - zgradite generator receptov

Zdaj, ko smo odigrali scenarij, napišimo kodo, ki odgovarja prikazanemu scenariju. Sledite naslednjim korakom:

1. Uporabite obstoječo datoteko _app.py_ kot izhodišče
1. Poiščite spremenljivko `prompt` in spremenite njeno kodo na naslednje:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Če zdaj zaženete kodo, boste videli izpis, podoben:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > OPOMBA: vaš LLM ni determinističen, zato lahko vsakič, ko zaženete program, dobite različne rezultate.

   Odlično, poglejmo, kako lahko zadeve izboljšamo. Za izboljšavo želimo, da je koda prilagodljiva, tako da lahko spremenimo sestavine in število receptov.

1. Spremenimo kodo na naslednji način:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolirajte število receptov v poziv in sestavine
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Preizkusni zagon kode bi lahko izgledal tako:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Izboljšajte z dodajanjem filtra in nakupovalnega seznama

Zdaj imamo delujočo aplikacijo, sposobno izdelave receptov, ki je prilagodljiva, saj se zanaša na vnos uporabnika, tako glede števila receptov kot uporabljenih sestavin.

Za nadaljnjo izboljšavo želimo dodati naslednje:

- **Filtriranje sestavin**. Želimo biti sposobni filtrirati sestavine, ki nam niso všeč ali pa smo nanje alergični. Za to spremembo lahko uredimo obstoječi poziv in na njegov konec dodamo pogoj filtra, kot sledi:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Zgoraj dodamo `{filter}` na konec poziva in tudi pridobimo vrednost filtra od uporabnika.

  Primer vnosa pri zagonu programa lahko zdaj izgleda takole:

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

  Kot vidite, so bili recepti, ki vsebujejo mleko, odfiltrirani. Če pa ste laktozno intolerantni, boste morda želeli filtrirati tudi recepte s sirom, zato je pomembno biti jasen.


- **Naredite nakupovalni seznam**. Želimo izdelati nakupovalni seznam, ob upoštevanju tega, kar že imamo doma.

  Za to funkcionalnost bi lahko poskušali rešiti vse v enem pozivu ali pa bi jo lahko razdelili na dva poziva. Poskusimo slednji pristop. Tu predlagamo dodajanje dodatnega poziva, vendar za to, da bo delovalo, moramo rezultat prvega poziva dodati kot kontekst drugemu pozivu.

  Poiščite del kode, ki izpiše rezultat prvega poziva, in spodaj dodajte naslednjo kodo:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # natisni odgovor
  print("Shopping list:")
  print(response.output_text)
  ```

  Upoštevajte naslednje:

  1. Ustvarjamo nov poziv tako, da rezultat prvega poziva dodamo novemu pozivu:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Naredimo nov zahtevek, pri čemer upoštevamo tudi število žetonov, ki smo jih zahtevali v prvem pozivu, zato tokrat rečemo, da je `max_output_tokens` 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     S testiranjem te kode pridemo do naslednjega rezultata:

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

Kar imamo doslej, je delujoča koda, vendar bi jo morali še dodatno izboljšati. Nekaj stvari, ki bi jih morali storiti, je:

- **Ločite skrivnosti od kode**, kot je API ključ. Skrivnosti ne spadajo v kodo in jih je treba shraniti na varno mesto. Za ločevanje skrivnosti od kode lahko uporabimo spremenljivke okolja in knjižnice, kot je `python-dotenv`, za nalaganje iz datoteke. Tako bi to izgledalo v kodi:

  1. Ustvarite `.env` datoteko z naslednjo vsebino:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Opomba, za Azure OpenAI v Microsoft Foundry morate namesto tega nastaviti naslednje spremenljivke okolja:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     V kodi bi spremenljivke okolja naložili tako:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Beseda o dolžini žetonov**. Moramo razmisliti, koliko žetonov potrebujemo za ustvarjanje željenega besedila. Žetoni stanejo, zato moramo, kjer je mogoče, biti varčni z njihovim številom. Na primer, ali lahko poziv oblikujemo tako, da uporabimo manj žetonov?

  Za spremembo uporabljenih žetonov lahko uporabite parameter `max_output_tokens`. Na primer, če želite uporabiti 100 žetonov, storite tako:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Poskusi z nastavitvijo temperature**. Temperatura je nekaj, kar doslej nismo omenjali, vendar je pomemben kontekst za delovanje našega programa. Višja kot je vrednost temperature, bolj naključni bodo rezultati. Nasprotno pa nižja kot je temperatura, bolj predvidljiv bo izhod. Razmislite, ali želite v svojem izhodu variacije ali ne.

  Za spreminjanje temperature lahko uporabite parameter `temperature`. Na primer, če želite uporabiti temperaturo 0,5, storite tako:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Opomba, bolj ko se približate 1, tem bolj raznolik bo izhod.

## Naloga

Pri tej nalogi lahko izberete, kaj boste izdelali.

Tukaj je nekaj predlogov:

- Prilagodite aplikacijo za generator receptov in jo še dodatno izboljšajte. Preizkusite različne vrednosti temperature in pozive ter preverite, kaj lahko ustvarite.
- Ustvarite "učnega prijatelja". Ta aplikacija bi morala znati odgovarjati na vprašanja o določeni temi, na primer Python. Lahko bi imeli pozive, kot so "Kaj je določena tema v Pythonu?", ali pa poziv, ki pravi, pokaži mi kodo za določeno temo itd.
- Zgodovinski bot, oživite zgodovino, naročite botu, naj odigra določen zgodovinski lik in postavljajte mu vprašanja o njegovem življenju in časih.

## Rešitev

### Učni prijatelj

Spodaj je začetni poziv, preverite, kako ga lahko uporabite in prilagodite po svoji želji.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Zgodovinski bot

Tukaj je nekaj pozivov, ki jih lahko uporabljate:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Preverjanje znanja

Kaj počne koncept temperature?

1. Nadzoruje, kako naključen je izhod.
1. Nadzoruje, kako velik je odgovor.
1. Nadzoruje, koliko žetonov je uporabljenih.

## 🚀 Izziv

Med delom na nalogi poskusite spreminjati temperaturo, nastavite jo na 0, 0,5 in 1. Ne pozabite, da je 0 najmanj raznoliko, 1 pa najbolj raznoliko. Katera vrednost najbolje deluje za vašo aplikacijo?

## Odlično delo! Nadaljujte z učenjem

Po zaključku te lekcije si oglejte našo [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da nadaljujete z nadgradnjo svojega znanja o generativni umetni inteligenci!

Pojdite na Lekcijo 7, kjer bomo pogledali, kako [izdelati klepetalne aplikacije](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->