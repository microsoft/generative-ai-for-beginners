# Vytváranie aplikácií na generovanie textu

[![Vytváranie aplikácií na generovanie textu](../../../translated_images/sk/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

Doteraz ste si v tomto vzdelávacom programe všimli, že existujú základné koncepty ako prompt a dokonca celá disciplína nazývaná "prompt engineering". Mnoho nástrojov, s ktorými môžete komunikovať, ako ChatGPT, Office 365, Microsoft Power Platform a ďalšie, podporujú používanie promptov na dosiahnutie niečoho.

Ak chcete takýto zážitok pridať do aplikácie, musíte rozumieť konceptom ako prompty, completions a vybrať si knižnicu na prácu. Presne to sa naučíte v tejto kapitole.

## Úvod

V tejto kapitole sa naučíte:

- Spoznáte knižnicu openai a jej základné pojmy.
- Vytvoríte aplikáciu na generovanie textu pomocou openai.
- Pochopíte, ako používať koncepty ako prompt, temperature a tokens na vytvorenie aplikácie na generovanie textu.

## Ciele učenia

Na konci tejto lekcie budete schopní:

- Vysvetliť, čo je aplikácia na generovanie textu.
- Vytvoriť aplikáciu na generovanie textu pomocou openai.
- Nakonfigurovať vašu aplikáciu tak, aby používala viac alebo menej tokenov a tiež upraviť teplotu pre rôznorodý výstup.

## Čo je aplikácia na generovanie textu?

Bežne, keď vytvárate aplikáciu, má nejaké rozhranie ako napríklad:

- Príkazové. Konzolové aplikácie sú typické aplikácie, kde zadáte príkaz a aplikácia vykoná úlohu. Napríklad `git` je takáto príkazová aplikácia.
- Užívateľské rozhranie (UI). Niektoré aplikácie majú grafické užívateľské rozhranie (GUI), kde klikáte na tlačidlá, zadávate text, vyberáte možnosti a podobne.

### Konzolové a UI aplikácie majú obmedzenia

Porovnajte to s príkazovou aplikáciou, kde zadávate príkaz:

- **Je to obmedzené**. Nemôžete zadať akýkoľvek príkaz, iba tie, ktoré aplikácia podporuje.
- **Jazykovo špecifické**. Niektoré aplikácie podporujú viacero jazykov, ale štandardne sú vytvorené pre konkrétny jazyk, aj keď môžete pridať podporu iných jazykov.

### Výhody aplikácií na generovanie textu

Ako je teda aplikácia na generovanie textu iná?

V takejto aplikácii máte viac flexibility, nie ste obmedzení na množinu príkazov alebo konkrétny vstupný jazyk. Namiesto toho môžete používať prirodzený jazyk na komunikáciu s aplikáciou. Ďalšou výhodou je, že už komunikujete so zdrojom dát, ktorý bol vytrénovaný na rozsiahlej korpuse informácií, zatiaľ čo tradičná aplikácia môže byť obmedzená na to, čo je v databáze.

### Čo môžem vytvoriť pomocou aplikácie na generovanie textu?

Existuje mnoho vecí, ktoré môžete vytvoriť. Napríklad:

- **Chatbot**. Chatbot odpovedajúci na otázky o témach, napríklad o vašej spoločnosti a jej produktoch, by bol dobrým kandidátom.
- **Asistent**. LLM sú skvelé na veci ako zhrnutie textu, získavanie poznatkov z textu, tvorbu textov ako životopisy a viac.
- **Asistent pri kódovaní**. V závislosti od použitého jazykového modelu môžete vytvoriť asistenta pri písaní kódu. Napríklad môžete použiť produkty ako GitHub Copilot alebo ChatGPT na pomoc s kódovaním.

## Ako začať?

Musíte nájsť spôsob, ako sa integrovať s LLM, čo zvyčajne znamená nasledujúce dve metódy:

- Použiť API. Tu konštruujete webové požiadavky so svojím promptom a získavate generovaný text späť.
- Použiť knižnicu. Knižnice pomáhajú zapuzdriť volania API a sprístupniť ich jednoduchšie použiteľné.

## Knižnice/SDK

Existuje niekoľko dobre známych knižníc pre prácu s LLM, napríklad:

- **openai**, táto knižnica uľahčuje pripojenie k vášmu modelu a odosielanie promptov.

Potom sú knižnice, ktoré pracujú na vyššej úrovni, ako napríklad:

- **Langchain**. Langchain je dobre známy a podporuje Python.
- **Semantic Kernel**. Semantic Kernel je knižnica od Microsoftu podporujúca jazyky C#, Python a Java.

## Prvá aplikácia s openai

Pozrime sa, ako môžeme vytvoriť našu prvú aplikáciu, aké knižnice potrebujeme, koľko je potrebné a podobne.

### Inštalácia openai

Existuje veľa knižníc na komunikáciu s OpenAI alebo Azure OpenAI. Je možné použiť tiež rôzne programovacie jazyky, ako C#, Python, JavaScript, Java a ďalšie. My sme si vybrali použiť knižnicu Python `openai`, takže ju nainštalujeme cez `pip`.

```bash
pip install openai
```

### Vytvorenie zdroja

Musíte vykonať nasledovné kroky:

- Vytvoriť konto na Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Získať prístup k Azure OpenAI. Choďte na [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) a požiadajte o prístup.

  > [!NOTE]
  > V čase písania tohto textu je potrebné požiadať o prístup k Azure OpenAI.

- Nainštalovať Python <https://www.python.org/>
- Vytvoriť Azure OpenAI Service zdroj. Pozrite si návod, ako [vytvoriť zdroj](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Nájdite API kľúč a koncový bod

Teraz musíte povedať knižnici `openai`, ktorý API kľúč používať. Na nájdenie API kľúča choďte do sekcie "Kľúče a koncový bod" vo vašom Azure OpenAI zdroji a skopírujte hodnotu "Kľúč 1".

![Kľúče a koncový bod v Azure portáli](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Keď máte tieto informácie skopírované, nasleduje ich použitie v knižniciach.

> [!NOTE]
> Je vhodné oddeliť váš API kľúč od kódu. Môžete to urobiť pomocou premenných prostredia.
>
> - Nastavte premennú prostredia `OPENAI_API_KEY` na váš API kľúč.
>   `export OPENAI_API_KEY='sk-...'`

### Nastavenie konfigurácie Azure

Ak používate Azure OpenAI (teraz súčasť Microsoft Foundry), takto nastavíte konfiguráciu. Používame štandardného klienta `OpenAI` namiereného na Azure OpenAI `/openai/v1/` koncový bod, ktorý pracuje s Responses API a nevyžaduje `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Vyššie nastavujeme:

- `api_key`, čo je váš API kľúč nájdený v Azure Portáli alebo Microsoft Foundry portáli.
- `base_url`, čo je váš Foundry zdrojový koncový bod s pripojeným `/openai/v1/`. Stabilný v1 koncový bod funguje naprieč OpenAI a Azure OpenAI bez správy `api_version`.

> [!NOTE] > `os.environ` číta premenné prostredia. Môžete ho použiť na čítanie premenných ako `AZURE_OPENAI_API_KEY` a `AZURE_OPENAI_ENDPOINT`. Nastavte tieto premenné vášho prostredia v termináli alebo pomocou knižnice ako `dotenv`.

## Generovanie textu

Spôsob generovania textu je použitie Responses API cez metódu `responses.create`. Tu je príklad:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

V príklade kódu vytvárame odpoveď a zadávame model, ktorý chceme použiť, a prompt. Potom vytlačíme generovaný text cez `response.output_text`.

### Konverzácie s viacerými kolami

Responses API je vhodné ako pre jednorázové generovanie textu, tak pre viackolové chatboty - poskytujete zoznam správ v `input` na vybudovanie konverzácie:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Viac o tejto funkcii v nasledujúcej kapitole.

## Cvičenie - vaša prvá aplikácia na generovanie textu

Teraz keď sme sa naučili ako nastaviť a konfigurovať openai, je čas vytvoriť vašu prvú aplikáciu na generovanie textu. Postupujte podľa týchto krokov:

1. Vytvorte virtuálne prostredie a nainštalujte openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Ak používate Windows, zadajte `venv\Scripts\activate` namiesto `source venv/bin/activate`.

   > [!NOTE]
   > Nájdenie vášho Azure OpenAI kľúča je možné na [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), vyhľadajte `Open AI` a vyberte `Open AI resource`, potom vyberte `Keys and Endpoint` a skopírujte hodnotu `Key 1`.

1. Vytvorte súbor _app.py_ a vložte doň nasledujúci kód:

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

   Mali by ste vidieť výstup podobný tomu, ako je uvedené nižšie:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Rôzne typy promptov pre rôzne úlohy

Teraz ste videli, ako generovať text pomocou promptu. Dokonca máte program bežiaci, ktorý môžete modifikovať a meniť na generovanie rôznych typov textu.

Prompty možno použiť na množstvo úloh. Napríklad:

- **Vygenerovanie typu textu**. Napríklad môžete vygenerovať báseň, otázky do kvízu a podobne.
- **Vyhľadanie informácií**. Môžete použiť prompt na vyhľadanie informácie, ako v príklade „Čo znamená CORS vo vývoji webu?“
- **Generovanie kódu**. Môžete použiť prompt na generovanie kódu, napríklad vytvorenie regulárneho výrazu na validáciu e-mailov alebo prečo nevygenerovať celý program, napríklad webovú aplikáciu?

## Praktická ukážka: generátor receptov

Predstavme si, že máte doma ingrediencie a chcete uvariť niečo. Na to potrebujete recept. Spôsob, ako nájsť recepty je použiť vyhľadávač alebo použiť LLM.

Môžete napísať prompt takto:

> "Ukáž mi 5 receptov na jedlo s nasledujúcimi ingredienciami: kuracie, zemiaky a mrkva. Ku každému receptu uveď všetky použité ingrediencie."

Na základe tohoto promptu môžete získať odpoveď podobnú tejto:

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

Tento výsledok je skvelý, viem čo variť. V tomto bode by bolo užitočné vylepšiť:

- Filtrovať ingrediencie, ktoré nemám rád alebo na ktoré som alergický.
- Vytvoriť nákupný zoznam, ak nemám doma všetky ingrediencie.

Pre tieto prípady pridajme ďalší prompt:

> "Prosím odstráň recepty, ktoré obsahujú cesnak, lebo som na ne alergický, a nahraď ho niečím iným. Tiež prosím vytvor nákupný zoznam pre recepty, pričom počítaj s tým, že doma už mám kuracie, zemiaky a mrkvu."

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

To je vašich päť receptov bez cesnaku a tiež máte nákupný zoznam so zohľadnením toho, čo už doma máte.

## Cvičenie - vytvorte generátor receptov

Keď sme si prešli scenár, napíšme kód zodpovedajúci zobrazenému scenáru. Postupujte podľa týchto krokov:

1. Použite existujúci súbor _app.py_ ako východiskový bod
1. Nájdenie premennej `prompt` a zmena jej kódu na nasledujúce:

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

   > POZNÁMKA, váš LLM nie je deterministický, takže výsledky sa môžu meniť pri každom spustení programu.

   Výborne, pozrime sa, ako to môžeme zlepšiť. Aby bol kód flexibilnejší, aby sa dali vylepšiť a meniť množstvo ingrediencií i počet receptov.

1. Zmeňme kód nasledovne:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Testovanie kódu môže vyzerať takto:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Vylepšiť pridaním filtra a nákupného zoznamu

Teraz máme funkčnú aplikáciu schopnú produkovať recepty a je flexibilná, pretože sa spolieha na vstupy používateľa, počnúc počtom receptov až po ingrediencie.

Na ďalšie zlepšenie chceme pridať nasledujúce:

- **Filtrovať ingrediencie**. Chceme vedieť filtrovať ingrediencie, ktoré nemáme radi alebo na ktoré sme alergickí. Na tento účel môžeme upraviť existujúci prompt a pridať filter na konci takto:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Vyššie sme pridali `{filter}` na koniec promptu a tiež zachytávame hodnotu filtra od používateľa.

  Príklad vstupu pri spustení programu teraz vyzerá takto:

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

  Ako vidíte, recepty obsahujúce mlieko sú odfiltrované. Ak ste intolerantní na laktózu, možno budete chcieť odfiltrovať aj recepty s obsahom syra, takže je potrebné byť konkrétny.

- **Vytvoriť nákupný zoznam**. Chceme vytvoriť nákupný zoznam na základe toho, čo už doma máme.

  Túto funkcionalitu môžeme riešiť jedným promptom alebo rozdeliť na dva prompty. Skúsme druhý prístup. Tu navrhujeme pridať ďalší prompt, ale na to, aby to fungovalo, musíme pridať výsledok prvého promptu ako kontext do druhého promptu.

  Nájdenie časti kódu, ktorá vytlačí výsledok prvého promptu, a pridanie nasledujúceho kódu pod ňu:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Všimnite si nasledujúce:

  1. Konštruujeme nový prompt pridaním výsledku z prvého promptu k novému promptu:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Vytvárame novú požiadavku, pričom zohľadňujeme počet tokenov, ktoré sme požadovali v prvom prompte, takže teraz je `max_output_tokens` nastavený na 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Keď spustíme tento kód, dostaneme nasledujúci výstup:

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

Čo doteraz máme, je kód, ktorý funguje, ale existujú určité úpravy, ktoré by sme mali urobiť na ďalšie zlepšenie. Niektoré veci, ktoré by sme mali urobiť, sú:

- **Oddeliť tajomstvá od kódu**, ako napríklad API kľúč. Tajomstvá nepatria do kódu a mali by byť uložené na bezpečnom mieste. Na oddelenie tajomstiev od kódu môžeme použiť premenné prostredia a knižnice ako `python-dotenv` na ich načítanie zo súboru. Takto by to vyzeralo v kóde:

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

     V kóde by ste načítali premenné prostredia takto:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Slovo o dĺžke tokenu**. Mali by sme zvážiť, koľko tokenov potrebujeme na vygenerovanie požadovaného textu. Tokeny stoja peniaze, takže kdekoľvek je to možné, mali by sme byť ekonomickí s počtom tokenov, ktoré používame. Napríklad, môžeme formulovať prompt tak, aby sme použili menej tokenov?

  Na zmenu počtu použitých tokenov môžete použiť parameter `max_output_tokens`. Napríklad, ak chcete použiť 100 tokenov, urobíte to takto:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Experimentovanie s teplotou**. Teplota je niečo, o čom sme doteraz nehovorili, ale je to dôležitý kontext toho, ako náš program funguje. Čím vyššia je hodnota teploty, tým náhodnejší bude výsledok. Naopak, čím nižšia teplota, tým predvídateľnejší bude výsledok. Zvážte, či chcete mať vo výstupe variabilitu alebo nie.

  Na zmenu teploty môžete použiť parameter `temperature`. Napríklad, ak chcete použiť teplotu 0,5, urobíte to takto:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Poznámka, čím bližšie k 1.0, tým rozmanitejší výstup.

- **Modely na uvažovanie nepoužívajú `temperature`**. Toto je dôležitý posun v roku 2026. Súčasné, neodporúčané modely v Microsoft Foundry sú **modely na uvažovanie** (rodina GPT-5, o-séria) - a **nepodporujú `temperature` alebo `top_p`** (ani `max_tokens`; používajte `max_output_tokens`). Ak pošlete `temperature` do `gpt-5-mini`, dostanete chybu "parameter nie je podporovaný". Takže ak chcete vyskúšať príklad s teplotou vyššie, zamerajte sa na model, ktorý stále podporuje ovládanie generovania - napríklad otvorený **Llama** model ako `Llama-3.3-70B-Instruct` z [katalógu modelov Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), volaný cez Foundry Models / Azure AI Inference endpoint (rovnakým spôsobom ako príklady `githubmodels-*`). Pre modely na uvažovanie ako GPT-5 riadite výstup inak:
  - **Prompt engineering** - jasné inštrukcie, príklady a štruktúrovaný výstup (pozri lekciu [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) robia prácu, ktorú kedysi robili ovládacie prvky generovania.
  - **Ovládanie uvažovania** - parametre ako úsilie uvažovania/hovorovosť vyvažujú hĺbku uvažovania voči latencii a nákladom.

  Skrátka: `temperature`/`top_p` sú stále platné na mnohých modeloch (Llama, Mistral, Phi a rodina GPT-4.x - hoci GPT-4.x sa už prestáva používať), ale smer vývoja je prompt engineering + ovládanie uvažovania na modeloch na uvažovanie ako GPT-5.

## Zadanie

Pre toto zadanie si môžete vybrať, čo chcete vytvoriť.

Tu sú niektoré návrhy:

- Vylepšite aplikáciu generátora receptov. Hrajte sa s hodnotami teploty a promptami, aby ste zistili, čo všetko vymyslíte.
- Vytvorte "študijného kamaráta". Táto aplikácia by mala vedieť odpovedať na otázky o téme, napríklad Python, môžete mať prompty ako "Čo je určitá téma v Pythone?", alebo prompt, ktorý povie, ukáž mi kód pre určitú tému a pod.
- História bot, oživte históriu, nechajte bota hrať určitú historickú postavu a pýtajte sa ho na otázky o jej živote a dobách.

## Riešenie

### Študijný kamarát

Nižšie je štartovací prompt, pozrite sa, ako ho môžete použiť a prispôsobiť podľa seba.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### História bot

Tu sú niektoré prompty, ktoré by ste mohli použiť:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Overenie vedomostí

Čo robí koncept teploty?

1. Riadi, aký náhodný bude výstup.
1. Riadi, aká veľká bude odpoveď.
1. Riadi, koľko tokenov sa použije.

## 🚀 Výzva

Pri práci na zadaní skúšajte meniť teplotu, nastavte ju na 0, 0,5 a 1. Pamätajte, že 0 je najmenej variabilné a 1 najviac. Aká hodnota funguje najlepšie pre vašu aplikáciu?

## Skvelá práca! Pokračujte v učení

Po dokončení tejto lekcie si pozrite našu [kolekciu vzdelávania o generatívnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste pokračovali vo zvyšovaní svojich znalostí o generatívnej AI!

Choďte do Lekcie 7, kde sa pozrieme na to, ako [vytvárať chatovacie aplikácie](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->