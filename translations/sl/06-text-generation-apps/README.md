# Gradnja aplikacij za generiranje besedila

[![Gradnja aplikacij za generiranje besedila](../../../translated_images/sl/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Kliknite na zgornjo sliko, da si ogledate video te lekcije)_

Doslej ste skozi ta kurikulum videli, da obstajajo osnovni koncepti, kot so pozivi (prompts) in celo cela disciplina imenovana "inženiring pozivov". Mnogi orodji, s katerimi lahko sodelujete, kot so ChatGPT, Office 365, Microsoft Power Platform in več, podpirajo uporabo pozivov za doseganje nečesa.

Da bi takšno izkušnjo dodali aplikaciji, morate razumeti koncepte, kot so pozivi, dopolnitve in izbrati knjižnico za delo z njimi. Prav to se boste naučili v tem poglavju.

## Uvod

V tem poglavju boste:

- Spoznali knjižnico openai in njene osnovne koncepte.
- Zgradili aplikacijo za generiranje besedila z uporabo openai.
- Razumeli, kako uporabiti koncepte, kot so prompt, temperatura in tokni za gradnjo aplikacije za generiranje besedila.

## Cilji učenja

Na koncu te lekcije boste znali:

- Razložiti, kaj je aplikacija za generiranje besedila.
- Zgraditi aplikacijo za generiranje besedila z uporabo openai.
- Nastaviti svojo aplikacijo za uporabo več ali manj tokenov in spremeniti temperaturo za raznolik izhod.

## Kaj je aplikacija za generiranje besedila?

Običajno, ko gradite aplikacijo, ima nekakšen vmesnik, kot je naslednji:

- Na ukaze osnovana. Konzolne aplikacije so tipične aplikacije, kjer vnesete ukaz in opravi nalogo. Na primer, `git` je aplikacija na ukaze.
- Uporabniški vmesnik (UI). Nekatere aplikacije imajo grafične uporabniške vmesnike (GUI), kjer klikate gumbe, vnašate besedilo, izbirate možnosti in še več.

### Konzolne in UI aplikacije so omejene

Primerjaj to z aplikacijo na ukaze, kjer vtipkate ukaz:

- **Omejeno je**. Ne morete vtipkati kateregakoli ukaza, le tiste, ki jih aplikacija podpira.
- **Specifično glede jezika**. Nekatere aplikacije podpirajo več jezikov, vendar je aplikacija po privzetku zgrajena za določen jezik, čeprav lahko dodate podporo za več jezikov.

### Prednosti aplikacij za generiranje besedila

Kako je torej aplikacija za generiranje besedila drugačna?

V aplikaciji za generiranje besedila imate večjo prilagodljivost, niste omejeni na niz ukazov ali specifičen vhodni jezik. Namesto tega lahko uporabljate naravni jezik za interakcijo z aplikacijo. Druga prednost je, da že komunicirate z virom podatkov, ki je bil usposobljen na ogromnem korpusu informacij, medtem ko je tradicionalna aplikacija lahko omejena na vsebino baze podatkov.

### Kaj lahko zgradim z aplikacijo za generiranje besedila?

Obstaja veliko stvari, ki jih lahko zgradite. Na primer:

- **Klepetalni robot (chatbot)**. Chatbot, ki odgovarja na vprašanja o temah, kot je vaše podjetje in njegovi izdelki, bi bil dobra izbira.
- **Pomočnik**. LLM-ji so odlični pri stvareh, kot so povzemanje besedil, pridobivanje vpogledov iz besedila, ustvarjanje besedil, kot so življenjepisi in več.
- **Pomočnik za kodo**. Glede na jezikovni model, ki ga uporabljate, lahko zgradite pomočnika za kodo, ki pomaga pri pisanju kode. Na primer, lahko uporabite produkt kot GitHub Copilot ali ChatGPT za pomoč pri pisanju kode.

## Kako začeti?

Najprej morate najti način za integracijo z LLM, kar običajno vključuje naslednja dva pristopa:

- Uporabite API. Tukaj gradite spletne zahteve z vašim pozivom in prejmete nazaj generirano besedilo.
- Uporabite knjižnico. Knjižnice pomagajo zapakirati klice API-ja in jih naredijo lažje za uporabo.

## Knjižnice/SDK-ji

Obstaja nekaj dobro znanih knjižnic za delo z LLM-ji, kot so:

- **openai**, ta knjižnica omogoča preprosto povezavo z vašim modelom in pošiljanje pozivov.

Nato so tu knjižnice, ki delujejo na višji ravni, kot so:

- **Langchain**. Langchain je dobro znan in podpira Python.
- **Semantic Kernel**. Semantic Kernel je knjižnica podjetja Microsoft, ki podpira jezike C#, Python in Java.

## Prva aplikacija z uporabo openai

Poglejmo, kako lahko zgradimo našo prvo aplikacijo, katere knjižnice potrebujemo, koliko je zahtevano in tako naprej.

### Namestitev openai

Obstaja mnogo knjižnic za interakcijo z OpenAI ali Azure OpenAI. Možno je uporabljati različne programske jezike, kot so C#, Python, JavaScript, Java in še več. Odločili smo se uporabiti Python knjižnico `openai`, zato bomo uporabili `pip` za namestitev.

```bash
pip install openai
```

### Ustvarite vir

Potrebno je izvesti naslednje korake:

- Ustvarite račun na Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Pridobite dostop do Azure OpenAI. Pojdite na [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) in zaprosite za dostop.

  > [!NOTE]
  > Ob pisanju tega gradiva morate zaprositi za dostop do Azure OpenAI.

- Namestite Python <https://www.python.org/>
- Ustvarili ste vir Azure OpenAI storitve. Oglejte si ta vodič kako [ustvariti vir](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Poiščite API ključ in končno točko

V tem trenutku morate povedati knjižnici `openai`, kateri API ključ naj uporablja. Za iskanje vašega API ključa pojdite v razdelek "Keys and Endpoint" vašega vira Azure OpenAI in kopirajte vrednost "Key 1".

![Vrstica ključev in končnih točk v Azure Portalu](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Zdaj, ko imate te informacije kopirane, naj knjižnice to uporabijo.

> [!NOTE]
> Vredno je ločiti svoj API ključ od kode. To lahko storite z uporabo okoljskih spremenljivk.
>
> - Nastavite okoljsko spremenljivko `OPENAI_API_KEY` na vaš API ključ.
>   `export OPENAI_API_KEY='sk-...'`

### Nastavitev konfiguracije Azure

Če uporabljate Azure OpenAI (zdaj del Microsoft Foundry), tako nastavite konfiguracijo. Uporabljamo standardnega odjemalca `OpenAI` usmerjenega na končno točko Azure OpenAI `/openai/v1/`, ki deluje z Responses API in ne potrebuje `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Zgoraj nastavljamo naslednje:

- `api_key`, to je vaš API ključ, najden v Azure Portalu ali portalu Microsoft Foundry.
- `base_url`, to je končna točka vašega vira Foundry z dodatkom `/openai/v1/`. Stabilna v1 končna točka deluje preko OpenAI in Azure OpenAI brez potrebe po upravljanju `api_version`.

> [!NOTE] > `os.environ` bere okoljske spremenljivke. Uporabite ga lahko za branje okolijskih spremenljivk, kot so `AZURE_OPENAI_API_KEY` in `AZURE_OPENAI_ENDPOINT`. Nastavite te okoljske spremenljivke v svojem terminalu ali z uporabo knjižnice, kot je `dotenv`.

## Generiranje besedila

Način generiranja besedila je uporaba Responses API preko metode `responses.create`. Primer:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # to je ime vaše implementacije modela
    input=prompt,
    store=False,
)
print(response.output_text)
```

V zgornji kodi ustvarimo odziv in posredujemo model, ki ga želimo uporabiti, in poziv. Nato izpišemo generirano besedilo preko `response.output_text`.

### Pogovori z več izmenjavami

Responses API je dobro primeren tako za generiranje besedila z enim izmenjavo kot za večizmenjavne klepetalne bote - zagotovite seznam sporočil v `input` za gradnjo pogovora:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Več o tej funkcionalnosti v prihajajočem poglavju.

## Vaja - vaša prva aplikacija za generiranje besedila

Zdaj, ko smo se naučili, kako nastaviti in konfigurirati openai, je čas, da zgradite svojo prvo aplikacijo za generiranje besedila. Za gradnjo aplikacije sledite tem korakom:

1. Ustvarite virtualno okolje in namestite openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Če uporabljate Windows, tipkajte `venv\Scripts\activate` namesto `source venv/bin/activate`.

   > [!NOTE]
   > Poiščite svoj Azure OpenAI ključ tako, da pojdite na [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), iščete `Open AI`, izberete `Open AI resource` in nato `Keys and Endpoint` ter kopirate vrednost `Key 1`.

1. Ustvarite datoteko _app.py_ in ji dodajte naslednjo kodo:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # dodajte svojo kodo za dokončanje
   prompt = "Complete the following: Once upon a time there was a"

   # izvedite zahtevo z uporabo Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # izpiši odgovor
   print(response.output_text)
   ```

   > [!NOTE]
   > Če uporabljate običajni OpenAI (ne Azure), uporabite `client = OpenAI(api_key="<tukaj zamenjajte vrednost z vašim OpenAI ključem>")` (brez `base_url`) in navedite ime modela, kot je `gpt-5-mini` namesto imena namestitve.

   Moral bi videti izpis, podoben naslednjemu:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Različne vrste pozivov, za različne stvari

Zdaj ste videli, kako generirati besedilo z uporabo poziva. Imate tudi program, ki deluje in ga lahko spreminjate za generiranje različnih vrst besedila.

Pozivi se lahko uporabijo za vse vrste nalog. Na primer:

- **Generiranje vrste besedila**. Na primer, lahko ustvarite pesem, vprašanja za kviz itd.
- **Iskanje informacij**. Z pozivi lahko iščete informacije, kot v naslednjem primeru: 'Kaj pomeni CORS pri spletnem razvoju?'.
- **Generiranje kode**. Z pozivi lahko ustvarite kodo, na primer razvijate regularni izraz za preverjanje e-pošte ali zakaj ne ustvarite celoten program, kot npr. spletno aplikacijo?

## Bolj praktičen primer: generator receptov

Predstavljajte si, da imate doma sestavine in želite kaj skuhati. Za to potrebujete recept. Način iskanja receptov je uporaba iskalnika ali pa uporabite LLM.

Lahko napišete poziv takole:

> "Pokaži mi 5 receptov za jed z naslednjimi sestavinami: piščanec, krompir in korenje. Na recept pripiši vse uporabljene sestavine."

Glede na zgornji poziv, lahko dobite odgovor podoben:

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

Ta rezultat je odličen, vem kaj bom kuhal. V tem trenutku bi bile koristne izboljšave:

- Odstranjanje sestavin, ki jih ne maram ali sem nanje alergičen.
- Priprava nakupovalnega seznam, če določene sestavine nimam doma.

Za zgoraj navedene primere dodajmo še naslednji poziv:

> "Prosim, odstrani recepte s česnom, ker sem nanj alergičen, in nadomesti s čim drugim. Prav tako prosim pripravi nakupovalni seznam za recepte, ob upoštevanju, da imam doma že piščanca, krompir in korenje."

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

To je vaših pet receptov, brez omenjenega česna, in imate tudi nakupovalni seznam glede na sestavine, ki jih že imate doma.

## Vaja - zgradite generator receptov

Zdaj, ko smo prikazali scenarij, napišimo kodo, ki ustreza prikazanemu primeru. Za to sledite tem korakom:

1. Uporabite obstoječo datoteko _app.py_ kot izhodišče
1. Poiščite spremenljivko `prompt` in spremenite njeno kodo v naslednjo:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Če zdaj zaženete kodo, bi morali videti izpis, podoben naslednjemu:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > OPOZORILO, vaš LLM ni determinističen, zato lahko dobite različne rezultate vsakič, ko program zaženete.

   Odlično, poglejmo, kako lahko zadeve izboljšamo. Da izboljšamo, želimo zagotoviti, da je koda prilagodljiva, tako da se lahko spreminjajo sestavine in število receptov.

1. Spremenimo kodo na naslednji način:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolirajte število receptov v poziv in sestavine
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

Zdaj imamo delujočo aplikacijo, ki lahko ustvari recepte in je prilagodljiva, saj temelji na vhodih uporabnika, tako glede števila receptov kot tudi uporabljenih sestavin.

Za nadaljnjo izboljšavo želimo dodati naslednje:

- **Filtriranje sestavin**. Želimo lahko filtrirati sestavine, ki jih ne maramo ali smo nanje alergični. Za dosego te spremembe lahko uredimo naš obstoječi poziv in dodamo pogoj filtra na konec, kot sledi:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Zgoraj smo dodali `{filter}` na konec poziva in ujeli vrednost filtra od uporabnika.

  Primer vnosa ob zagonu programa lahko zdaj izgleda tako:

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

  Kot vidite, so vsi recepti, ki vsebujejo mleko, bili filtrirani. Vendar, če ste laktozno intolerantni, bi mogoče želeli filtrirati tudi recepte, ki vsebujejo sir, zato je treba biti jasen.


- **Ustvarite nakupovalni seznam**. Želimo ustvariti nakupovalni seznam, pri čemer upoštevamo, kaj že imamo doma.

  Za to funkcionalnost lahko poskusimo rešiti vse v enem pozivu ali pa jo razdelimo na dva poziva. Poskusimo slednji pristop. Tukaj predlagamo dodajanje dodatnega poziva, vendar za to, da bo delovalo, moramo rezultat prvega poziva dodati kot kontekst drugemu pozivu.

  Poiščite del v kodi, ki izpiše rezultat prvega poziva, in pod to dodajte naslednjo kodo:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # izpiši odgovor
  print("Shopping list:")
  print(response.output_text)
  ```

  Upoštevajte naslednje:

  1. Sestavljamo nov poziv tako, da dodamo rezultat prvega poziva v nov poziv:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Naredimo nov zahtevek, pri čemer upoštevamo tudi število tokenov, ki smo jih zahtevali v prvem pozivu, zato tokrat nastavimo `max_output_tokens` na 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Ko zaženemo to kodo, dobimo naslednji izhod:

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

Kode, ki jo imamo do zdaj, deluje, vendar bi morali narediti nekaj izboljšav. Nekaj stvari, ki jih moramo narediti, so:

- **Ločite skrivnosti od kode**, kot je na primer API ključ. Skrivnosti ne sodijo v kodo in jih je treba shranjevati na varno mesto. Za ločevanje skrivnosti od kode lahko uporabimo okoljske spremenljivke in knjižnice, kot je `python-dotenv`, da jih naložimo iz datoteke. Tako bi to izgledalo v kodi:

  1. Ustvarite `.env` datoteko z naslednjo vsebino:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Opomba, za Azure OpenAI v Microsoft Foundry morate namesto tega nastaviti naslednje okoljske spremenljivke:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     V kodi boste okoljske spremenljivke naložili tako:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Beseda o dolžini tokenov**. Moramo razmisliti, koliko tokenov potrebujemo za generiranje želenega besedila. Tokeni nekaj stanejo, zato se po možnosti trudimo biti varčni s številom uporabljenih tokenov. Na primer, ali lahko oblikujemo poziv tako, da uporabimo manj tokenov?

  Za nastavitev uporabljenih tokenov lahko uporabite parameter `max_output_tokens`. Na primer, če želite uporabiti 100 tokenov, storite tako:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Eksperimentiranje s temperaturo**. Temperatura je nekaj, kar do zdaj nismo omenili, vendar je pomemben kontekst za delovanje našega programa. Višja vrednost temperature pomeni bolj naključne rezultate. Nasprotno pa nižja temperatura pomeni bolj predvidljiv izhod. Razmislite, ali želite različnost v svojem izhodu ali ne.

  Za spreminjanje temperature lahko uporabite parameter `temperature`. Na primer, če želite temperaturo 0,5, naredite tako:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Opomba, bližje kot je vrednost 1, bolj raznolik bo izhod.

- **Razumski modeli ne uporabljajo `temperature`**. To je pomembna sprememba za leto 2026. Trenutni, nepreklicani modeli v Microsoft Foundry so **razumski modeli** (družina GPT-5, o-serija) - in **ne podpirajo `temperature` ali `top_p`** (prav tako ne `max_tokens`; uporabite `max_output_tokens`). Če pošljete `temperature` modelu `gpt-5-mini`, boste dobili napako "parameter ni podprt". Zato za poskus zgornjega primera temperature uporabite model, ki še podpira kontrole vzorčenja - na primer odprti **Llama** model, kot je `Llama-3.3-70B-Instruct` iz [kataloga modelov Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), ki ga pokličete prek končne točke Foundry Models / Azure AI Inference (na enak način kot vzorci `githubmodels-*`). Za razumske modele, kot je GPT-5, izhod krmilite drugače:
  - **Inženiring pozivov** - jasna navodila, primeri in strukturiran izhod (glejte lekcijo [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) opravljajo delo, ki so ga prej opravljali nastavitveni gumbi za vzorčenje.
  - **Razumske kontrole** - parametri kot so trud pri sklepanju/podrobnost teksta izmenjujejo globino sklepanja s časovno zamudo in stroški.

  Na kratko: `temperature`/`top_p` sta še vedno veljavna pri mnogih modelih (Llama, Mistral, Phi in družina GPT-4.x - čeprav GPT-4.x ukinja uporabo), vendar je smer razvoja inženiring pozivov + razumske kontrole na razumskih modelih, kot je GPT-5.

## Naloga

Za to nalogo lahko izberete, kaj boste ustvarili.

Tukaj je nekaj predlogov:

- Izboljšajte aplikacijo generatorja receptov. Igrajte se z vrednostmi temperature in pozivi, da vidite, kaj lahko ustvarite.
- Ustvarite "študijskega prijatelja". Aplikacija naj bo sposobna odgovarjati na vprašanja o določeni temi, npr. Python, lahko imate pozive kot "Kaj je določena tema v Pythonu?" ali pa poziv, ki zahteva prikaz kode za določeno temo itd.
- Zgodovinski bot, oživite zgodovino, dajte navodila botu, naj igra določeno zgodovinsko osebo in ga sprašujte o njegovem življenju in času.

## Rešitev

### Študijski prijatelj

Spodaj je začetni poziv, poglejte, kako ga lahko uporabite in prilagodite po želji.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Zgodovinski bot

Tukaj je nekaj pozivov, ki jih lahko uporabite:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Preverjanje znanja

Kaj počne koncept temperatura?

1. Nadzira, kako naključen je izhod.
1. Nadzira, kako velik je odgovor.
1. Nadzira, koliko tokenov se uporabi.

## 🚀 Izziv

Med delom na nalogi poskusite spreminjati temperaturo, nastavite jo na 0, 0,5 in 1. Zapomnite si, da je 0 najmanj raznoliko, 1 pa najbolj raznoliko. Katera vrednost najbolje deluje za vašo aplikacijo?

## Odlično delo! Nadaljujte z učenjem

Po zaključku te lekcije si oglejte našo [kolekcijo učenja generativne AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), da še naprej nadgrajujete svoje znanje o generativni AI!

Pojdite na lekcijo 7, kjer si bomo ogledali, kako [ustvariti klepetalne aplikacije](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->