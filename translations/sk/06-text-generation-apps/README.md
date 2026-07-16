# Budovanie aplikácií na generovanie textu

[![Budovanie aplikácií na generovanie textu](../../../translated_images/sk/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

Doteraz ste v tomto kurze videli, že existujú základné koncepty ako promptovanie a dokonca celá disciplína nazývaná "prompt engineering". Mnoho nástrojov, s ktorými môžete komunikovať, ako ChatGPT, Office 365, Microsoft Power Platform a ďalšie, vás podporuje v používaní promptov na dosiahnutie cieľa.

Aby ste mohli pridať takúto skúsenosť do aplikácie, musíte porozumieť konceptom ako sú prompt, completions a vybrať si knižnicu, s ktorou budete pracovať. Presne to sa naučíte v tejto kapitole.

## Úvod

V tejto kapitole:

- Spoznáte knižnicu openai a jej základné koncepty.
- Vybudujete aplikáciu na generovanie textu pomocou openai.
- Pochopíte, ako používať koncepty ako prompt, teplota a tokeny na vytvorenie aplikácie na generovanie textu.

## Ciele učenia sa

Na konci tejto lekcie budete schopní:

- Vysvetliť, čo je aplikácia na generovanie textu.
- Vybudovať aplikáciu na generovanie textu pomocou openai.
- Nakonfigurovať svoju aplikáciu tak, aby používala viac alebo menej tokenov a tiež meniť teplotu, pre rozmanitejší výstup.

## Čo je to aplikácia na generovanie textu?

Zvyčajne, keď vytvárate aplikáciu, má nejaké rozhranie, napríklad takéto:

- Na základe príkazov. Konzolové aplikácie sú typické aplikácie, kde zadáte príkaz a vykoná sa úloha. Napríklad `git` je aplikácia založená na príkazoch.
- Používateľské rozhranie (UI). Niektoré aplikácie majú grafické používateľské rozhranie (GUI), kde klikáte na tlačidlá, zadávate text, vyberáte možnosti a podobne.

### Konzolové a UI aplikácie majú obmedzenia

Porovnajte to s aplikáciou založenou na príkazoch, kde zadávate príkaz:

- **Je obmedzené**. Nemôžete len tak zadať akýkoľvek príkaz, iba tie, ktoré aplikácia podporuje.
- **Jazykovo špecifické**. Niektoré aplikácie podporujú mnoho jazykov, ale predvolene je aplikácia nastavená pre konkrétny jazyk, aj keď môžete pridať podporu ďalších jazykov.

### Výhody aplikácií na generovanie textu

Ako je teda aplikácia na generovanie textu odlišná?

V aplikácii na generovanie textu máte väčšiu flexibilitu, nie ste obmedzení na sadu príkazov alebo konkrétny vstupný jazyk. Namiesto toho môžete použiť prirodzený jazyk na interakciu s aplikáciou. Ďalšou výhodou je, že už pracujete s dátovým zdrojom, ktorý bol vytrénovaný na obrovskom korpuse informácií, zatiaľ čo tradičná aplikácia môže byť obmedzená na obsah databázy.

### Čo môžem vytvoriť s aplikáciou na generovanie textu?

Existuje mnoho vecí, ktoré môžete vytvoriť. Napríklad:

- **Chatbot**. Chatbot zodpovedajúci otázky o témach ako vaša spoločnosť a jej produkty môže byť vhodným riešením.
- **Pomocník**. Veľké jazykové modely (LLM) sú skvelé na veci ako zhrnutie textu, získavanie poznatkov z textu, tvorbu textov ako životopisov a viac.
- **Asistent kódu**. V závislosti od jazykového modelu, ktorý používate, môžete vytvoriť asistenta kódu, ktorý vám pomáha písať kód. Napríklad môžete použiť produkt ako GitHub Copilot alebo ChatGPT.

## Ako začať?

Potrebujete nájsť spôsob, ako sa integrovať s veľkým jazykovým modelom (LLM), ktorý zvyčajne znamená tieto dve možnosti:

- Použiť API. Tu vytvárate webové požiadavky so svojím promptom a dostávate generovaný text späť.
- Použiť knižnicu. Knižnice pomáhajú zabaliť volania API a uľahčujú ich používanie.

## Knižnice/SDK

Existuje niekoľko dobre známych knižníc na prácu s LLM ako:

- **openai**, táto knižnica uľahčuje pripojenie k vášmu modelu a odosielanie promptov.

Potom sú tu knižnice, ktoré fungujú na vyššej úrovni, napríklad:

- **Langchain**. Langchain je dobre známy a podporuje Python.
- **Semantic Kernel**. Semantic Kernel je knižnica od Microsoftu podporujúca jazyky C#, Python a Java.

## Prvá aplikácia pomocou openai

Pozrime sa, ako môžeme vytvoriť našu prvú aplikáciu, aké knižnice potrebujeme, koľko je potrebné a tak ďalej.

### Inštalácia openai

Existuje mnoho knižníc pre interakciu s OpenAI alebo Azure OpenAI. Je možné použiť rôzne programovacie jazyky, ako C#, Python, JavaScript, Java a ďalšie. My sme zvolili použitie Python knižnice `openai`, preto použijeme `pip` na jej inštaláciu.

```bash
pip install openai
```

### Vytvorte zdroj

Musíte vykonať nasledujúce kroky:

- Vytvorte konto na Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Získajte prístup k Azure OpenAI. Choďte na [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) a požiadajte o prístup.

  > [!NOTE]
  > V čase písania je potrebné požiadať o prístup k Azure OpenAI.

- Nainštalujte Python <https://www.python.org/>
- Vytvorte zdroj služby Azure OpenAI. Pozrite si tento návod, ako [vytvoriť zdroj](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Nájdite API kľúč a endpoint

Teraz potrebujete knihovnej `openai` povedať, ktorý API kľúč použiť. Na nájdenie API kľúča choďte do sekcie "Keys and Endpoint" vášho zdroja Azure OpenAI a skopírujte hodnotu "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Teraz keď máte tieto údaje skopírované, nastavme knižnice, aby ich používali.

> [!NOTE]
> Je dobré oddeliť váš API kľúč od vášho kódu. Môžete to urobiť pomocou premenných prostredia.
>
> - Nastavte premennú prostredia `OPENAI_API_KEY` na váš API kľúč.
>   `export OPENAI_API_KEY='sk-...'`

### Nastavenie konfigurácie Azure

Ak používate Azure OpenAI (teraz súčasť Microsoft Foundry), tu je spôsob nastavenia konfigurácie. Používame štandardného klienta `OpenAI` nasmerovaného na Azure OpenAI endpoint `/openai/v1/`, ktorý pracuje s Responses API a nevyžaduje `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Hore nastavujeme nasledovné:

- `api_key`, to je váš API kľúč nájdený v Azure Portáli alebo Microsoft Foundry portáli.
- `base_url`, to je endpoint vášho Foundry zdroja s pridaným `/openai/v1/`. Stabilný endpoint v1 funguje pre OpenAI aj Azure OpenAI bez správy `api_version`.

> [!NOTE] > `os.environ` číta environmentálne premenné. Môžete ho použiť na načítanie premenných ako `AZURE_OPENAI_API_KEY` a `AZURE_OPENAI_ENDPOINT`. Nastavte tieto premenne vo vašom termináli alebo pomocou knižnice ako `dotenv`.

## Generovanie textu

Spôsob generovania textu je použitie Responses API cez metódu `responses.create`. Tu je príklad:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # toto je názov vášho nasadenia modelu
    input=prompt,
    store=False,
)
print(response.output_text)
```

V hore uvedenom kóde vytvárame odpoveď a odovzdávame model, ktorý chceme použiť, a prompt. Potom vytlačíme generovaný text cez `response.output_text`.

### Konverzácie s viacerými kolami (multi-turn)

Responses API je vhodné pre generovanie textu s jedným kolom aj pre viackolové chatboty - poskytnete zoznam správ v `input` na zostavenie konverzácie:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

Viac o tejto funkcii v nadchádzajúcej kapitole.

## Cvičenie - vaša prvá aplikácia na generovanie textu

Teraz keď sme si ukázali, ako nastaviť a nakonfigurovať openai, je čas vybudovať vašu prvú aplikáciu na generovanie textu. Postupujte podľa týchto krokov:

1. Vytvorte virtuálne prostredie a nainštalujte openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Ak používate Windows, napíšte `venv\Scripts\activate` namiesto `source venv/bin/activate`.

   > [!NOTE]
   > Nájdite svoj Azure OpenAI kľúč na [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), vyhľadajte `Open AI`, vyberte `Open AI resource` a potom `Keys and Endpoint` a skopírujte hodnotu `Key 1`.

1. Vytvorte súbor _app.py_ a vložte do neho nasledovný kód:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # pridajte váš dokončovací kód
   prompt = "Complete the following: Once upon a time there was a"

   # uskutočnite požiadavku pomocou API Responses
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # vytlačte odpoveď
   print(response.output_text)
   ```

   > [!NOTE]
   > Ak používate čistý OpenAI (nie Azure), použite `client = OpenAI(api_key="<nahraďte túto hodnotu vaším OpenAI kľúčom>")` (bez `base_url`) a pre model zadávajte názov napríklad `gpt-4o-mini` namiesto názvu deploymentu.

   Mali by ste vidieť výstup približne takýto:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Rôzne typy promptov pre rôzne účely

Teraz ste videli, ako generovať text pomocou promptu. Dokonca máte program bežiaci, ktorý môžete upravovať a meniť na generovanie rôznych typov textu.

Prompt možno použiť na rôzne úlohy, napríklad:

- **Generovanie typu textu**. Napríklad môžete vytvoriť báseň, otázky do kvízu a podobne.
- **Vyhľadávanie informácií**. Prompt môžete použiť na vyhľadávanie informácií, napríklad otázku 'Čo znamená CORS vo webovom vývoji?'.
- **Generovanie kódu**. Pomocou promptu môžete generovať kód, napríklad regulárny výraz na validáciu e-mailov alebo rovno vytvoriť celú aplikáciu, ako webovú aplikáciu.

## Praktickejší prípad použitia: generátor receptov

Predstavte si, že máte doma ingrediencie a chcete niečo uvariť. Potrebujete recept. Spôsob, ako nájsť recepty, je použiť vyhľadávač alebo môžete použiť LLM.

Môžete napísať prompt takto:

> "Ukáž mi 5 receptov na jedlo s týmito ingredienciami: kuracie mäso, zemiaky a mrkva. Pri každom recepte uveď všetky použité ingrediencie."

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

Tento výsledok je skvelý, viem, čo uvariť. Teraz by mohli byť užitočné tieto zlepšenia:

- Filtrovať ingrediencie, ktoré nemám rád alebo na ktoré som alergický.
- Vyrobiť nákupný zoznam, ak doma nemám všetky ingrediencie.

Pre tieto prípady pridajme ďalší prompt:

> "Prosím, odstráň recepty s cesnakom, pretože som alergický, a nahraď ho niečím iným. Tiež prosím vytvor nákupný zoznam pre tieto recepty s ohľadom na to, že doma už mám kuracie mäso, zemiaky a mrkvu."

Teraz máte nový výsledok, a to:

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

To sú vaše päť receptov bez cesnaku a zároveň máte nákupný zoznam podľa toho, čo už máte doma.

## Cvičenie - vytvorte generátor receptov

Keď sme si prešli scenár, napíšeme kód, ktorý mu bude zodpovedať. Postupujte podľa týchto krokov:

1. Použite existujúci súbor _app.py_ ako východiskový bod
1. Nájdite premennú `prompt` a zmeňte jej kód na nasledovný:

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

   > POZNÁMKA, váš LLM nie je deterministický, takže pri každom spustení programu môžete dostať odlišné výsledky.

   Výborne, teraz sa pozrime, ako môžeme veci vylepšiť. Na vylepšenie chceme zabezpečiť ako flexibilitu kódu, aby bolo možné meniť ingrediencie aj počet receptov.

1. Zmeňme kód nasledovne:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolujte počet receptov do výzvy a ingrediencií
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Kód pre testovanie môže vyzerať takto:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Vylepšenie pridaním filtra a nákupného zoznamu

Teraz máme funkčnú aplikáciu schopnú vytvárať recepty a je flexibilná, pretože závisí od vstupov používateľa, tak počtu receptov ako aj použitých ingrediencií.

Na ďalšie zlepšenie chceme pridať toto:

- **Filtrovať ingrediencie**. Chceme byť schopní filtrovať ingrediencie, ktoré nemáme radi alebo na ktoré sme alergickí. Na tento účel môžeme upraviť náš existujúci prompt pridaním filtra na konci takto:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Hore pridávame `{filter}` na koniec promptu a zároveň získavame hodnotu filtra od používateľa.

  Príklad vstupu pri spúšťaní programu teraz môže vyzerať takto:

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

  Ako vidíte, recepty s mliekom sú vyfiltrované. Ale ak ste laktózovo intolerantní, možno chcete vyfiltrovať aj recepty so syrom, takže treba byť jasný.


- **Vytvorte nákupný zoznam**. Chceme vytvoriť nákupný zoznam, pričom zohľadníme, čo už máme doma.

  Pre túto funkcionalitu môžeme buď skúsiť vyriešiť všetko v jednom promptu, alebo to rozdeliť na dva prompty. Vyskúšajme druhý prístup. Tu navrhujeme pridať ďalší prompt, no aby to fungovalo, musíme pridať výsledok prvého promptu ako kontext do druhého promptu.

  Nájdite časť v kóde, ktorá vypisuje výsledok z prvého promptu a pridajte nasledujúci kód pod ňu:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # vytlačiť odpoveď
  print("Shopping list:")
  print(response.output_text)
  ```

  Všimnite si nasledovné:

  1. Vytvárame nový prompt tak, že k novému promptu pridávame výsledok z prvého promptu:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Robíme nový request, ale zároveň berieme do úvahy počet tokenov, ktoré sme žiadali v prvom prompte, takže tentokrát hovoríme, že `max_output_tokens` je 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Keď si tento kód vyskúšame, dostaneme nasledujúci výstup:

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

To, čo máme zatiaľ, je kód, ktorý funguje, ale mali by sme urobiť niekoľko úprav, aby sme veci ešte viac zlepšili. Niektoré z vecí, ktoré by sme mali urobiť, sú:

- **Oddeliť tajné údaje od kódu**, ako napríklad API kľúč. Tajné údaje nepatria do kódu a mali by byť uložené na bezpečnom mieste. Na oddelenie tajných údajov od kódu môžeme použiť environmentálne premenné a knižnice ako `python-dotenv`, ktoré ich načítajú zo súboru. Takto by to vyzeralo v kóde:

  1. Vytvorte súbor `.env` s nasledovným obsahom:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Poznámka, pre Azure OpenAI v Microsoft Foundry je potrebné namiesto toho nastaviť nasledujúce environmentálne premenné:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     V kóde by ste mali načítať environmentálne premenné takto:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Slovo o dĺžke tokenov**. Mali by sme zvážiť, koľko tokenov potrebujeme na vygenerovanie textu, ktorý chceme. Toky stoja peniaze, preto by sme sa mali snažiť byť čo najekonomickejší s počtom použitých tokenov. Napríklad, môžeme formulovať prompt tak, aby sme mohli použiť menej tokenov?

  Na zmenu počtu použitých tokenov môžete použiť parameter `max_output_tokens`. Ak napríklad chcete použiť 100 tokenov, urobíte to takto:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Experimentovanie s teplotou**. Teplota je niečo, o čom sme zatiaľ nehovorili, ale je to dôležitý kontext pre výkon nášho programu. Čím je hodnota teploty vyššia, tým náhodnejší výstup bude. Naopak, čím je hodnota teploty nižšia, tým predvídateľnejší výstup bude. Zvážte, či chcete mať vo výstupe variabilitu alebo nie.

  Na zmenu teploty môžete použiť parameter `temperature`. Ak napríklad chcete použiť teplotu 0,5, urobíte to takto:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Poznámka, čím bližšie k 1.0, tým variabilnejší výstup.

## Zadanie

Pre toto zadanie si môžete vybrať, čo budete tvoriť.

Tu je niekoľko návrhov:

- Vylepšite aplikáciu na generovanie receptov. Hrajte sa s hodnotami teploty a promptmi, aby ste zistili, čo dokážete vytvoriť.
- Vytvorte „študijného kamaráta“. Táto aplikácia by mala byť schopná odpovedať na otázky o nejakej téme, napríklad Python, môžete mať prompty ako „Čo je určitá téma v Pythone?“ alebo prompt, ktorý povie, ukáž mi kód pre určitú tému a podobne.
- Historický bot, oživte históriu, nahraďte bota istou historickou postavou a pýtajte sa ho otázky o jej živote a dobe.

## Riešenie

### Študijný kamarát

Nižšie je štartovací prompt, pozrite sa, ako ho môžete použiť a upraviť podľa svojich predstáv.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Historický bot

Tu sú niektoré prompty, ktoré by ste mohli použiť:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Skúška vedomostí

Čo robí koncept teploty?

1. Kontroluje, ako náhodný bude výstup.
1. Kontroluje, aká veľká bude odpoveď.
1. Kontroluje, koľko tokenov sa použije.

## 🚀 Výzva

Pri práci na zadaní sa snaž meniť teplotu, nastavte ju na 0, 0,5 a 1. Pamätajte, že 0 je najmenej variabilný a 1 najviac. Aká hodnota najviac vyhovuje vašej aplikácii?

## Skvelá práca! Pokračujte vo vzdelávaní

Po dokončení tejto lekcie si pozrite našu [kolekciu učenia o generatívnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste pokračovali v zvyšovaní svojich znalostí o generatívnej AI!

Prejdite na lekciu 7, kde sa pozrieme, ako [vytvárať chatovacie aplikácie](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->