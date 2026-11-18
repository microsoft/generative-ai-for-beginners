# Tvorba aplikácií na generovanie textu

[![Tvorba aplikácií na generovanie textu](../../../translated_images/sk/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

Doteraz ste v tomto učebnom pláne videli, že existujú kľúčové koncepty ako prompt a dokonca celá disciplína nazvaná „prompt engineering“. Mnohé nástroje, s ktorými môžete interagovať, ako ChatGPT, Office 365, Microsoft Power Platform a ďalšie, vás podporujú pri používaní promptov na dosiahnutie určitého cieľa.

Aby ste mohli pridať takúto skúsenosť do aplikácie, musíte rozumieť konceptom ako prompt, doplnenia a vybrať knižnicu na prácu s nimi. Presne to sa naučíte v tejto kapitole.

## Úvod

V tejto kapitole sa naučíte:

- Spoznáte knižnicu openai a jej základné koncepty.
- Vytvoríte aplikáciu na generovanie textu pomocou openai.
- Pochopíte, ako používať koncepty ako prompt, teplota a tokeny na tvorbu aplikácie na generovanie textu.

## Ciele učenia

Na konci tejto lekcie budete schopní:

- Vysvetliť, čo je aplikácia na generovanie textu.
- Vytvoriť aplikáciu na generovanie textu pomocou openai.
- Nakonfigurovať aplikáciu na použitie viac alebo menej tokenov a tiež zmeniť teplotu pre rôzne výsledky.

## Čo je to aplikácia na generovanie textu?

Obvykle keď vytvárate aplikáciu, má nejaké používateľské rozhranie ako napríklad:

- Na báze príkazov. Konzolové aplikácie sú typické aplikácie, kde zadáte príkaz a ten vykoná úlohu. Napríklad `git` je aplikácia založená na príkazoch.
- Používateľské rozhranie (UI). Niektoré aplikácie majú grafické používateľské rozhranie (GUI), kde klikáte na tlačidlá, zadávate text, vyberáte možnosti a ďalšie.

### Konzolové a UI aplikácie majú obmedzenia

Porovnajte to s aplikáciou založenou na príkazoch, kde píšete príkaz:

- **Je obmedzená**. Nemôžete jednoducho zadať akýkoľvek príkaz, len tie, ktoré aplikácia podporuje.
- **Jazykovo špecifická**. Niektoré aplikácie podporujú mnoho jazykov, ale štandardne je aplikácia vytvorená pre konkrétny jazyk, aj keď možné je pridať podporu ďalších jazykov.

### Výhody aplikácií na generovanie textu

Ako sa teda líši aplikácia na generovanie textu?

V aplikácii na generovanie textu máte väčšiu flexibilitu, nie ste obmedzení na sada príkazov alebo konkrétny vstupný jazyk. Namiesto toho môžete používať prirodzený jazyk na interakciu s aplikáciou. Ďalšou výhodou je, že už interagujete so zdrojom údajov, ktorý bol vytrénovaný na obrovskom množstve informácií, zatiaľ čo tradičná aplikácia môže byť obmedzená tým, čo je v databáze.

### Čo môžem vytvoriť s aplikáciou na generovanie textu?

Existuje mnoho vecí, ktoré môžete vytvoriť, napríklad:

- **Chatbot**. Chatbot odpovedajúci na otázky o témach, ako vaša firma a jej produkty, môže byť dobrá voľba.
- **Pomocník**. LLM sú skvelé na veci ako zhrnutie textu, získanie poznatkov z textu, tvorbu textu ako životopisy a ďalšie.
- **Asistent kódu**. V závislosti od jazykového modelu, ktorý používate, môžete vytvoriť asistenta kódu, ktorý vám pomôže písať kód. Napríklad, môžete použiť produkt ako GitHub Copilot alebo ChatGPT na pomoc pri písaní kódu.

## Ako môžem začať?

Potrebujete nájsť spôsob, ako sa integrovať s LLM, čo obvykle zahŕňa tieto dva prístupy:

- Použiť API. Tu konštruujete webové požiadavky s vaším promptom a dostanete späť vygenerovaný text.
- Použiť knižnicu. Knižnice pomáhajú zachytiť volania API a zjednodušujú ich používanie.

## Knižnice/SDK

Existuje niekoľko známych knižníc na prácu s LLM, napríklad:

- **openai**, táto knižnica uľahčuje pripojenie k vášmu modelu a odosielanie promptov.

Potom sú knižnice, ktoré fungujú na vyššej úrovni, ako napríklad:

- **Langchain**. Langchain je známy a podporuje Python.
- **Semantic Kernel**. Semantic Kernel je knižnica od Microsoftu podporujúca jazyky C#, Python a Java.

## Prvá aplikácia pomocou openai

Pozrime sa, ako môžeme vytvoriť našu prvú aplikáciu, aké knižnice potrebujeme, koľko je potrebné a tak ďalej.

### Inštalácia openai

Existuje mnoho knižníc pre interakciu s OpenAI alebo Azure OpenAI. Je možné používať rôzne programovacie jazyky ako C#, Python, JavaScript, Java a ďalšie. My sme sa rozhodli použiť Python knižnicu `openai`, takže ju nainštalujeme pomocou `pip`.

```bash
pip install openai
```

### Vytvorenie zdroja

Musíte vykonať nasledujúce kroky:

- Vytvoriť účet v Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Získať prístup k Azure OpenAI. Prejdite na [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) a požiadajte o prístup.

  > [!NOTE]
  > V čase písania musíte požiadať o prístup k Azure OpenAI.

- Nainštalovať Python <https://www.python.org/>
- Vytvoriť Azure OpenAI Service zdroj. Pozrite si tento návod, ako [vytvoriť zdroj](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Nájdite API kľúč a endpoint

V tomto momente musíte knižnici `openai` povedať, ktorý API kľúč použiť. Na jeho nájdenie prejdite do sekcie „Kľúče a Endpoint“ vo vašom Azure OpenAI zdroji a skopírujte hodnotu „Kľúč 1“.

![Čepele kľúčov a endpointov zdrojov v Azure portáli](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Keď máte tieto informácie skopírované, necháme knižnice, aby ich použili.

> [!NOTE]
> Stojí za to oddeliť API kľúč od vášho kódu. Môžete tak urobiť použitím environmentálnych premenných.
>
> - Nastavte environmentálnu premennú `OPENAI_API_KEY` na váš API kľúč.
>   `export OPENAI_API_KEY='sk-...'`

### Nastavenie konfigurácie Azure

Ak používate Azure OpenAI (teraz súčasť Microsoft Foundry), takto nastavíte konfiguráciu. Používame štandardného klienta `OpenAI` so smerovaním na Azure OpenAI endpoint `/openai/v1/`, ktorý funguje s Responses API a nevyžaduje `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Vyššie nastavujeme nasledujúce:

- `api_key`, toto je váš API kľúč nájdený v Azure portáli alebo Microsoft Foundry portáli.
- `base_url`, toto je endpoint vašej Foundry služby s pridaným `/openai/v1/`. Stabilný v1 endpoint funguje pre OpenAI aj Azure OpenAI bez správy `api_version`.

> [!NOTE] > `os.environ` číta environmentálne premenné. Môžete ho použiť na čítanie environmentálnych premenných ako `AZURE_OPENAI_API_KEY` a `AZURE_OPENAI_ENDPOINT`. Nastavte tieto premenné v termináli alebo pomocou knižnice ako `dotenv`.

## Vygenerovať text

Spôsob, ako generovať text, je použiť Responses API cez metódu `responses.create`. Tu je príklad:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

V horeuvedenom kóde vytvoríme odpoveď, zadáme model, ktorý chceme použiť, a prompt. Potom vypíšeme vygenerovaný text pomocou `response.output_text`.

### Viackolové rozhovory

Responses API je dobre prispôsobené na jednorázové generovanie textu aj na viackolové chatboty – poskytnete zoznam správ v `input` na vytvorenie rozhovoru:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Viac o tejto funkcionalite v nasledujúcej kapitole.

## Cvičenie – vaša prvá aplikácia na generovanie textu

Teraz, keď sme sa naučili nastaviť a konfigurovať openai, je čas vytvoriť vašu prvú aplikáciu na generovanie textu. Na vytvorenie aplikácie postupujte podľa týchto krokov:

1. Vytvorte virtuálne prostredie a nainštalujte openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Ak používate Windows, zadajte `venv\Scripts\activate` namiesto `source venv/bin/activate`.

   > [!NOTE]
   > Nájdite váš Azure OpenAI kľúč prejdite na [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), vyhľadajte `Open AI`, vyberte `Open AI resource`, potom vyberte `Keys and Endpoint` a skopírujte hodnotu `Key 1`.

1. Vytvorte súbor _app.py_ a vložte do neho nasledujúci kód:

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
   > Ak používate čistý OpenAI (nie Azure), použite `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (bez `base_url`) a zadajte názov modelu ako `gpt-5-mini` namiesto názvu deploymentu.

   Mali by ste vidieť výstup podobný tomuto:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Rôzne typy promptov pre rôzne úlohy

Teraz ste videli, ako generovať text pomocou promptu. Máte dokonca program, ktorý beží a môžete ho upravovať a meniť na generovanie rôznych typov textu.

Prompty môžu byť využité na rôzne úlohy. Napríklad:

- **Generovanie typu textu**. Napríklad môžete generovať báseň, otázky do kvízu a pod.
- **Vyhľadávanie informácií**. Prompty môžete použiť na vyhľadanie informácií, ako napríklad: „Čo znamená CORS vo webovom vývoji?“.
- **Generovanie kódu**. Prompty môžete použiť na generovanie kódu, napríklad vytvorenie regulárneho výrazu na validáciu emailov alebo prečo nie, generovanie celej aplikácie ako webová appka?

## Praktickejší prípad použitia: generátor receptov

Predstavte si, že máte doma suroviny a chcete niečo uvariť. Na to potrebujete recept. Spôsob, ako nájsť recepty, je použiť vyhľadávač alebo môžete použiť LLM.

Môžete napísať prompt napríklad takto:

> „Ukáž mi 5 receptov na jedlo nasledujúcich ingrediencií: kuracie mäso, zemiaky a mrkva. Pre každý recept uveď všetky použité ingrediencie.“

Na základe tohto promptu môžete dostať odpoveď podobnú tejto:

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

Tento výsledok je skvelý, viem, čo variť. V tomto momente by mohli byť ešte užitočné tieto vylepšenia:

- Filtrovanie ingrediencií, ktoré nemám rád alebo na ktoré som alergický.
- Vytvorenie nákupného zoznamu, ak nemám doma všetky ingrediencie.

Pre tieto prípady pridajme ďalší prompt:

> „Prosím odstráň recepty s cesnakom, som na ne alergický a nahraď ich niečím iným. Tiež prosím vytvor nákupný zoznam pre recepty, berúc do úvahy, že doma už mám kuracie mäso, zemiaky a mrkvu.“

Teraz máte nový výsledok, konkrétne:

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

To je vašich päť receptov bez zmienky o cesnaku a zároveň máte nákupný zoznam s ohľadom na to, čo už máte doma.

## Cvičenie – vytvorte generátor receptov

Teraz keď sme si predstavili scénar, napíšme kód, ktorý zodpovedá ukázanému prípadu. Postupujte podľa týchto krokov:

1. Použite existujúci súbor _app.py_ ako východisko.
1. Nájdite premennú `prompt` a zmeňte jej kód na nasledovné:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Ak teraz spustíte kód, mali by ste vidieť výstup podobný tomuto:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > POZNÁMKA, váš LLM je nedeterministický, takže môžete dostať rôzne výsledky pri každom spustení programu.

   Výborne, pozrime sa, ako môžeme veci zlepšiť. Na zlepšenie chceme, aby bol kód flexibilný, aby bolo možné meniť ingrediencie aj počet receptov.

1. Zmeňme kód nasledujúcim spôsobom:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Testovanie kódu by mohlo vyzerať takto:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Vylepšenie pridaním filtra a nákupného zoznamu

Teraz máme funkčnú aplikáciu, ktorá dokáže produkovať recepty a zároveň je flexibilná, pretože závisí od vstupov používateľa, teda počtu receptov aj použitých ingrediencií.

Na ďalšie vylepšenie chceme pridať nasledujúce:

- **Filtrovanie ingrediencií**. Chceme byť schopní filtrovať ingrediencie, ktoré nemáme radi alebo na ktoré sme alergickí. Na to môžeme upraviť náš existujúci prompt a na jeho koniec pridať filter, napríklad takto:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Hore pridávame `{filter}` na koniec promptu a zároveň zachytíme filter od používateľa.

  Príklad vstupu pri spustení programu môže vyzerať takto:

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

  Ako vidíte, všetky recepty obsahujúce mlieko boli odstránené. Ale ak ste laktózovo intolerantní, možno budete chcieť filtrovať aj recepty so syrom, preto je dôležité byť jasný.

- **Vytvoriť nákupný zoznam**. Chceme vytvoriť nákupný zoznam s ohľadom na to, čo už máme doma.

  Táto funkcionalita sa dá vyriešiť buď v jednom prompte, alebo ju rozdeliť na dva prompty. Skúsme druhý prístup. Tu navrhujeme pridať ďalší prompt, ale aby to fungovalo, musí byť výsledok prvého promptu pridaný ako kontext do druhého promptu.

  Nájdite časť kódu, ktorá vypisuje výsledok z prvého promptu, a pridajte pod ňu nasledujúci kód:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Všimnite si nasledovné:

  1. Vytvárame nový prompt pridaním výsledku prvého promptu do nového promptu:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Vytvárame novú požiadavku, pričom berieme do úvahy počet tokenov žiadaný v prvom prompte, preto tentoraz nastavujeme `max_output_tokens` na 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Po spustení tohto kódu dostávame nasledujúci výstup:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Vylepšite svoje nastavenie

To, čo máme zatiaľ, je kód, ktorý funguje, ale existujú niektoré úpravy, ktoré by sme mali urobiť, aby sme veci ešte viac vylepšili. Niektoré veci, ktoré by sme mali urobiť, sú:

- **Oddeliť tajomstvá od kódu**, ako je napríklad API kľúč. Tajomstvá nepatria do kódu a mali by byť uložené na bezpečnom mieste. Na oddelenie tajomstiev od kódu môžeme použiť premenné prostredia a knižnice ako `python-dotenv` na načítanie z súboru. Takto by to vyzeralo v kóde:

  1. Vytvorte súbor `.env` s nasledujúcim obsahom:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Poznámka, pre Azure OpenAI v Microsoft Foundry musíte namiesto toho nastaviť nasledujúce premenné prostredia:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     V kóde by ste premenné prostredia načítali takto:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Slovo k dĺžke tokenov**. Mali by sme zvážiť, koľko tokenov potrebujeme na generovanie požadovaného textu. Tokeny stoja peniaze, takže kde je to možné, mali by sme sa snažiť byť úsporní s počtom použitých tokenov. Napríklad, môžeme formulovať prompt tak, aby sme použili menej tokenov?

  Na zmenu počtu použitých tokenov môžete použiť parameter `max_output_tokens`. Ak chcete použiť napríklad 100 tokenov, urobíte to takto:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Experimentovanie s teplotou**. Teplota je niečo, čo sme zatiaľ nespomenuli, ale je to dôležitý kontext, ako náš program funguje. Čím je hodnota teploty vyššia, tým je výstup náhodnejší. Naopak, čím je teplota nižšia, tým je výstup predvídateľnejší. Zvážte, či chcete vo výstupe variabilitu alebo nie.

  Na zmenu teploty môžete použiť parameter `temperature`. Ak chcete použiť teplotu 0,5, urobíte to takto:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Poznámka, čím bližšie k 1,0, tým je výstup rôznorodejší.

- **Modely na uvažovanie nepoužívajú `temperature`**. Toto je dôležitý posun v roku 2026. Súčasné, nepoužívané modely na Microsoft Foundry sú **modely na uvažovanie** (rodina GPT-5, o-series) - a **nepodporujú `temperature` ani `top_p`** (ani `max_tokens`; použite `max_output_tokens`). Ak pošlete `temperature` na `gpt-5-mini`, dostanete chybu "parameter not supported". Takže na vyskúšanie príkladu s teplotou vyššie, smerujte to na model, ktorý stále podporuje ovládanie vzorkovania - napríklad otvorený **Llama** model ako `Llama-3.3-70B-Instruct` z [Microsoft Foundry model katalogu](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), volaný cez Foundry Models / Azure AI Inference endpoint (rovnakým spôsobom ako `githubmodels-*` príklady). Pre modely na uvažovanie ako GPT-5 riadite výstup inak:
  - **Prompt engineering** - jasné inštrukcie, príklady a štruktúrovaný výstup (pozri lekciu [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) robia prácu, ktorú kedysi vykonávali ovládače vzorkovania.
  - **Ovládanie uvažovania** - parametre ako snaha o uvažovanie / verbóznosť vyvažujú hĺbku uvažovania s latenciou a nákladmi.

  Stručne: `temperature`/`top_p` sú stále platné na mnohých modeloch (Llama, Mistral, Phi a rodina GPT-4.x - hoci GPT-4.x je postupne vyraďovaný), ale smerom vývoja je prompt engineering + riadenie uvažovania na modeloch uvažovania ako GPT-5.

## Zadanie

Pre toto zadanie si môžete vybrať, čo postavíte.

Tu je niekoľko návrhov:

- Vylepšite aplikáciu generátora receptov. Experimentujte s hodnotami teploty a výzvami, aby ste zistili, čo všetko dokážete vytvoriť.
- Vytvorte "študijného kamaráta". Táto aplikácia by mala byť schopná odpovedať na otázky o nejakej téme, napríklad o Pythone, môžete mať výzvy ako "Čo je určitá téma v Pythone?", alebo výzvu "ukáž mi kód pre určitú tému" atď.
- História bot, oživte históriu, nastavte bota, aby hral určitú historickú postavu a pýtajte sa ho otázky o jeho živote a časoch.

## Riešenie

### Študijný kamarát

Nižšie je úvodná výzva, pozrite sa, ako ju môžete použiť a prispôsobiť podľa svojho gusta.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### História bot

Tu je niekoľko výziev, ktoré môžete použiť:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Overenie znalostí

Čo robí koncepcie teploty?

1. Kontroluje, ako náhodný je výstup.
1. Kontroluje, aká veľká je odpoveď.
1. Kontroluje, koľko tokenov sa použije.

## 🚀 Výzva

Pri práci na úlohe skúste meniť teplotu, nastavte ju na 0, 0,5 a 1. Pamätajte, že 0 znamená najmenej variabilný výstup a 1 najviac. Aká hodnota najlepšie funguje pre vašu aplikáciu?

## Skvelá práca! Pokračujte v učení

Po dokončení tejto lekcie si pozrite našu [kolekciu na učenie Generatívnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste ďalej zvyšovali svoje znalosti v oblasti generatívnej AI!

Prejdite na Lekciu 7, kde sa pozrieme na to, ako [vytvárať chatovacie aplikácie](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->