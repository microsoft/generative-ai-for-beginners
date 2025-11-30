<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df027997f1448323d6159b78a1b669bf",
  "translation_date": "2025-10-17T21:52:48+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "sk"
}
-->
# Vytváranie aplikácií na generovanie textu

[![Vytváranie aplikácií na generovanie textu](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.sk.png)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Kliknite na obrázok vyššie, aby ste si pozreli video k tejto lekcii)_

Doteraz ste v tomto kurze videli, že existujú základné koncepty ako prompty a dokonca celá disciplína nazývaná "prompt engineering". Mnohé nástroje, s ktorými môžete interagovať, ako ChatGPT, Office 365, Microsoft Power Platform a ďalšie, vám umožňujú používať prompty na dosiahnutie určitých cieľov.

Ak chcete pridať takúto skúsenosť do aplikácie, musíte pochopiť koncepty ako prompty, dokončenia a vybrať knižnicu, s ktorou budete pracovať. Presne to sa naučíte v tejto kapitole.

## Úvod

V tejto kapitole sa naučíte:

- O knižnici openai a jej základných konceptoch.
- Ako vytvoriť aplikáciu na generovanie textu pomocou openai.
- Ako používať koncepty ako prompt, teplota a tokeny na vytvorenie aplikácie na generovanie textu.

## Ciele učenia

Na konci tejto lekcie budete schopní:

- Vysvetliť, čo je aplikácia na generovanie textu.
- Vytvoriť aplikáciu na generovanie textu pomocou openai.
- Konfigurovať svoju aplikáciu na použitie viac alebo menej tokenov a tiež zmeniť teplotu pre rôznorodý výstup.

## Čo je aplikácia na generovanie textu?

Bežne, keď vytvárate aplikáciu, má nejaký druh rozhrania, ako napríklad:

- Na základe príkazov. Konzolové aplikácie sú typické aplikácie, kde zadáte príkaz a vykoná sa úloha. Napríklad `git` je aplikácia na základe príkazov.
- Užívateľské rozhranie (UI). Niektoré aplikácie majú grafické užívateľské rozhrania (GUI), kde klikáte na tlačidlá, zadávate text, vyberáte možnosti a podobne.

### Konzolové a UI aplikácie sú obmedzené

Porovnajte to s aplikáciou na základe príkazov, kde zadávate príkaz:

- **Je to obmedzené**. Nemôžete zadať akýkoľvek príkaz, iba tie, ktoré aplikácia podporuje.
- **Špecifické pre jazyk**. Niektoré aplikácie podporujú mnoho jazykov, ale predvolene je aplikácia vytvorená pre konkrétny jazyk, aj keď môžete pridať podporu ďalších jazykov.

### Výhody aplikácií na generovanie textu

Ako sa teda aplikácia na generovanie textu líši?

V aplikácii na generovanie textu máte väčšiu flexibilitu, nie ste obmedzení na sadu príkazov alebo konkrétny vstupný jazyk. Namiesto toho môžete používať prirodzený jazyk na interakciu s aplikáciou. Ďalšou výhodou je, že už interagujete s dátovým zdrojom, ktorý bol trénovaný na obrovskom korpuse informácií, zatiaľ čo tradičná aplikácia môže byť obmedzená na to, čo je v databáze.

### Čo môžem vytvoriť s aplikáciou na generovanie textu?

Existuje mnoho vecí, ktoré môžete vytvoriť. Napríklad:

- **Chatbot**. Chatbot odpovedajúci na otázky o témach, ako je vaša spoločnosť a jej produkty, by mohol byť dobrým riešením.
- **Pomocník**. LLM sú skvelé na veci ako sumarizovanie textu, získavanie poznatkov z textu, produkovanie textu ako životopisov a podobne.
- **Asistent kódu**. V závislosti od jazykového modelu, ktorý používate, môžete vytvoriť asistenta kódu, ktorý vám pomôže písať kód. Napríklad môžete použiť produkt ako GitHub Copilot, ako aj ChatGPT na pomoc pri písaní kódu.

## Ako môžem začať?

Musíte nájsť spôsob, ako integrovať LLM, čo zvyčajne zahŕňa nasledujúce dva prístupy:

- Použiť API. Tu konštruujete webové požiadavky s vaším promptom a dostanete generovaný text späť.
- Použiť knižnicu. Knižnice pomáhajú zapúzdriť volania API a uľahčujú ich používanie.

## Knižnice/SDK

Existuje niekoľko známych knižníc na prácu s LLM, ako napríklad:

- **openai**, táto knižnica uľahčuje pripojenie k vášmu modelu a odosielanie promptov.

Potom existujú knižnice, ktoré fungujú na vyššej úrovni, ako napríklad:

- **Langchain**. Langchain je dobre známy a podporuje Python.
- **Semantic Kernel**. Semantic Kernel je knižnica od Microsoftu podporujúca jazyky C#, Python a Java.

## Prvá aplikácia pomocou openai

Pozrime sa, ako môžeme vytvoriť našu prvú aplikáciu, aké knižnice potrebujeme, koľko je potrebné a podobne.

### Inštalácia openai

Existuje mnoho knižníc na interakciu s OpenAI alebo Azure OpenAI. Je možné použiť rôzne programovacie jazyky, ako C#, Python, JavaScript, Java a ďalšie. Vybrali sme si knižnicu `openai` pre Python, takže ju nainštalujeme pomocou `pip`.

```bash
pip install openai
```

### Vytvorenie zdroja

Musíte vykonať nasledujúce kroky:

- Vytvorte si účet na Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Získajte prístup k Azure OpenAI. Prejdite na [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) a požiadajte o prístup.

  > [!NOTE]
  > V čase písania je potrebné požiadať o prístup k Azure OpenAI.

- Nainštalujte Python <https://www.python.org/>
- Vytvorte zdroj služby Azure OpenAI. Pozrite si tento návod, ako [vytvoriť zdroj](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Nájdite API kľúč a endpoint

V tomto bode musíte povedať knižnici `openai`, aký API kľúč má používať. Ak chcete nájsť svoj API kľúč, prejdite do sekcie "Keys and Endpoint" vášho zdroja Azure OpenAI a skopírujte hodnotu "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Teraz, keď máte tieto informácie skopírované, poďme inštruovať knižnice, aby ich použili.

> [!NOTE]
> Stojí za to oddeliť váš API kľúč od vášho kódu. Môžete to urobiť pomocou environmentálnych premenných.
>
> - Nastavte environmentálnu premennú `OPENAI_API_KEY` na váš API kľúč.
>   `export OPENAI_API_KEY='sk-...'`

### Nastavenie konfigurácie Azure

Ak používate Azure OpenAI, tu je postup, ako nastaviť konfiguráciu:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Vyššie nastavujeme nasledujúce:

- `api_type` na `azure`. To hovorí knižnici, aby používala Azure OpenAI a nie OpenAI.
- `api_key`, to je váš API kľúč nájdený v Azure Portáli.
- `api_version`, to je verzia API, ktorú chcete použiť. V čase písania je najnovšia verzia `2023-05-15`.
- `api_base`, to je endpoint API. Nájdete ho v Azure Portáli vedľa vášho API kľúča.

> [!NOTE] > `os.getenv` je funkcia, ktorá číta environmentálne premenné. Môžete ju použiť na čítanie environmentálnych premenných, ako sú `OPENAI_API_KEY` a `API_BASE`. Nastavte tieto environmentálne premenné vo vašom termináli alebo pomocou knižnice ako `dotenv`.

## Generovanie textu

Spôsob, ako generovať text, je použiť triedu `Completion`. Tu je príklad:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

V uvedenom kóde vytvárame objekt completion a zadávame model, ktorý chceme použiť, a prompt. Potom vytlačíme generovaný text.

### Chat completions

Doteraz ste videli, ako sme používali `Completion` na generovanie textu. Ale existuje ďalšia trieda nazývaná `ChatCompletion`, ktorá je vhodnejšia pre chatboty. Tu je príklad jej použitia:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Viac o tejto funkcii v nadchádzajúcej kapitole.

## Cvičenie - vaša prvá aplikácia na generovanie textu

Teraz, keď sme sa naučili, ako nastaviť a konfigurovať openai, je čas vytvoriť vašu prvú aplikáciu na generovanie textu. Ak chcete vytvoriť svoju aplikáciu, postupujte podľa týchto krokov:

1. Vytvorte virtuálne prostredie a nainštalujte openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Ak používate Windows, zadajte `venv\Scripts\activate` namiesto `source venv/bin/activate`.

   > [!NOTE]
   > Nájdite svoj Azure OpenAI kľúč tak, že prejdete na [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), vyhľadáte `Open AI` a vyberiete `Open AI resource`, potom vyberiete `Keys and Endpoint` a skopírujete hodnotu `Key 1`.

1. Vytvorte súbor _app.py_ a vložte do neho nasledujúci kód:

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
   > Ak používate Azure OpenAI, musíte nastaviť `api_type` na `azure` a nastaviť `api_key` na váš Azure OpenAI kľúč.

   Mali by ste vidieť výstup podobný nasledujúcemu:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Rôzne typy promptov pre rôzne veci

Teraz ste videli, ako generovať text pomocou promptu. Dokonca máte program, ktorý môžete upraviť a zmeniť na generovanie rôznych typov textu.

Prompty môžu byť použité na rôzne úlohy. Napríklad:

- **Generovanie typu textu**. Napríklad môžete generovať báseň, otázky na kvíz a podobne.
- **Vyhľadávanie informácií**. Môžete použiť prompty na vyhľadávanie informácií, ako napríklad 'Čo znamená CORS vo webovom vývoji?'.
- **Generovanie kódu**. Môžete použiť prompty na generovanie kódu, napríklad na vývoj regulárneho výrazu na validáciu e-mailov alebo prečo nie na generovanie celého programu, ako je webová aplikácia?

## Praktickejší prípad použitia: generátor receptov

Predstavte si, že máte doma ingrediencie a chcete niečo uvariť. Na to potrebujete recept. Spôsob, ako nájsť recepty, je použiť vyhľadávač alebo môžete použiť LLM.

Môžete napísať prompt, ako napríklad:

> "Ukáž mi 5 receptov na jedlo s nasledujúcimi ingredienciami: kuracie mäso, zemiaky a mrkva. Pre každý recept uveďte všetky použité ingrediencie."

Na základe vyššie uvedeného promptu môžete dostať odpoveď podobnú:

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

Tento výsledok je skvelý, viem, čo variť. V tomto bode by mohli byť užitočné vylepšenia, ako napríklad:

- Odstránenie ingrediencií, ktoré nemám rád alebo na ktoré som alergický.
- Vytvorenie nákupného zoznamu, ak nemám všetky ingrediencie doma.

Pre vyššie uvedené prípady pridajme ďalší prompt:

> "Prosím, odstráň recepty s cesnakom, pretože som naň alergický, a nahraď ho niečím iným. Tiež prosím vytvor nákupný zoznam pre recepty, berúc do úvahy, že už mám doma kuracie mäso, zemiaky a mrkvu."

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

To sú vaše päť receptov, bez zmienky o cesnaku, a tiež máte nákupný zoznam berúc do úvahy, čo už máte doma.

## Cvičenie - vytvorte generátor receptov

Teraz, keď sme si prešli scenár, napíšme kód, ktorý zodpovedá demonštrovanému scenáru. Ak to chcete urobiť, postupujte podľa týchto krokov:

1. Použite existujúci súbor _app.py_ ako východiskový bod.
1. Nájdite premennú `prompt` a zmeňte jej kód na nasledujúci:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Ak teraz spustíte kód, mali by ste vidieť výstup podobný:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > POZNÁMKA, váš LLM je nedeterministický, takže môžete dostať rôzne výsledky zakaždým, keď spustíte program.

   Skvelé, pozrime sa, ako môžeme veci vylepšiť. Aby sme veci vylepšili, chceme sa uistiť, že kód je flexibilný, takže ingrediencie a počet receptov môžu byť vylepšené a zmenené.

1. Zmeňme kód nasledujúcim spôsobom:

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

### Vylepšenie pridaním filtra a nákupného zoznamu

Teraz máme funkčnú aplikáciu schopnú produkovať recepty a je flexibilná, pretože sa spolieha na vstupy od používateľa, ako na počet receptov, tak aj na použité ingrediencie.

Aby sme to ďalej vylepšili, chceme pridať nasledujúce:

- **Odstránenie ingrediencií**. Chceme byť schopní odstrániť ingrediencie, ktoré nemáme radi alebo na ktoré sme alergickí. Na dosiahnutie tejto zmeny môžeme upraviť náš existujúci prompt a pridať podmienku filtra na jeho koniec, ako napríklad:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Vyššie pridávame `{filter}` na koniec promptu a tiež zachytávame hodnotu filtra od používateľa.

  Príklad vstupu pri spustení programu teraz môže vyzerať takto:

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

  Ako vidíte, akékoľvek recepty s mliekom boli odfiltrované. Ale ak ste intolerantní na laktózu, možno budete chcieť odfiltrovať aj recepty so syrom, takže je potrebné byť jasný.

- **Vytvorenie nákupného zoznamu**. Chceme vytvoriť nákupný zoznam, berúc do úvahy, čo už máme doma.

  Pre túto funkciu by sme mohli buď skúsiť vyriešiť všetko v jednom prompte, alebo by sme to mohli rozdeliť na dva prompty. Skúsme druhý prístup. Tu navrhujeme pridať ďalší prompt, ale aby to fungovalo, musíme pridať výsledok prvého promptu ako kontext k druhému promptu.

  Nájdite časť v kóde, ktorá vypisuje výsledok z prvého promptu, a pridajte nasledujúci kód nižšie:
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

  Všimnite si nasledujúce:

  1. Konštruujeme nový prompt pridaním výsledku z prvého promptu k novému promptu:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Vytvárame novú požiadavku, ale zároveň berieme do úvahy počet tokenov, ktoré sme požadovali v prvom prompte, takže tentokrát nastavíme `max_tokens` na 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     Po vyskúšaní tohto kódu sme dospeli k nasledujúcemu výstupu:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Zlepšite svoje nastavenie

To, čo máme doteraz, je kód, ktorý funguje, ale existujú určité úpravy, ktoré by sme mali vykonať, aby sme veci ešte viac zlepšili. Niektoré veci, ktoré by sme mali urobiť, sú:

- **Oddelenie tajomstiev od kódu**, ako napríklad API kľúč. Tajomstvá nepatria do kódu a mali by byť uložené na bezpečnom mieste. Na oddelenie tajomstiev od kódu môžeme použiť environmentálne premenné a knižnice ako `python-dotenv`, ktoré ich načítajú zo súboru. Takto by to vyzeralo v kóde:

  1. Vytvorte súbor `.env` s nasledujúcim obsahom:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Poznámka: Pre Azure je potrebné nastaviť nasledujúce environmentálne premenné:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     V kóde by ste environmentálne premenné načítali takto:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Poznámka k dĺžke tokenov**. Mali by sme zvážiť, koľko tokenov potrebujeme na generovanie textu, ktorý chceme. Tokeny stoja peniaze, takže kde je to možné, mali by sme sa snažiť byť ekonomickí s počtom použitých tokenov. Napríklad, môžeme formulovať prompt tak, aby sme použili menej tokenov?

  Na zmenu počtu použitých tokenov môžete použiť parameter `max_tokens`. Napríklad, ak chcete použiť 100 tokenov, urobili by ste:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Experimentovanie s teplotou**. Teplota je niečo, čo sme doteraz nespomenuli, ale je dôležitým kontextom pre to, ako náš program funguje. Čím vyššia je hodnota teploty, tým náhodnejší bude výstup. Naopak, čím nižšia je hodnota teploty, tým predvídateľnejší bude výstup. Zvážte, či chcete variáciu vo výstupe alebo nie.

  Na zmenu teploty môžete použiť parameter `temperature`. Napríklad, ak chcete použiť teplotu 0.5, urobili by ste:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Poznámka: Čím bližšie k 1.0, tým rozmanitejší bude výstup.

## Zadanie

Pre toto zadanie si môžete vybrať, čo chcete vytvoriť.

Tu sú niektoré návrhy:

- Vylepšite aplikáciu na generovanie receptov. Experimentujte s hodnotami teploty a promptmi, aby ste zistili, čo dokážete vytvoriť.
- Vytvorte "študijného partnera". Táto aplikácia by mala byť schopná odpovedať na otázky o téme, napríklad Python. Mohli by ste mať prompty ako "Čo je určitá téma v Pythone?" alebo prompt, ktorý hovorí "Ukáž mi kód pre určitú tému" atď.
- Historický bot, oživte históriu, inštruujte bota, aby hral určitú historickú postavu a pýtajte sa ho otázky o jeho živote a dobe.

## Riešenie

### Študijný partner

Nižšie je úvodný prompt, pozrite sa, ako ho môžete použiť a prispôsobiť podľa svojich predstáv.

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

## Kontrola vedomostí

Čo robí koncept teploty?

1. Ovláda, ako náhodný je výstup.
1. Ovláda, aký veľký je výstup.
1. Ovláda, koľko tokenov sa použije.

## 🚀 Výzva

Pri práci na zadaní skúste meniť teplotu, nastavte ju na 0, 0.5 a 1. Pamätajte, že 0 je najmenej rozmanitá a 1 je najrozmanitejšia. Aká hodnota najlepšie funguje pre vašu aplikáciu?

## Skvelá práca! Pokračujte vo svojom učení

Po dokončení tejto lekcie si pozrite našu [zbierku učenia o generatívnej AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst), aby ste pokračovali v rozvíjaní svojich znalostí o generatívnej AI!

Prejdite na Lekciu 7, kde sa pozrieme na to, ako [vytvárať chatovacie aplikácie](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.